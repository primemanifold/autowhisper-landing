import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.tags = []
        self.heading_stack = []
        self.meta_names = set()
        self.current_tag = None
        self.current_attrs = {}
        self.text_by_tag = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        self.current_tag = tag
        self.current_attrs = attrs
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "meta" and attrs.get("name"):
            self.meta_names.add(attrs["name"])
        if tag in {"h1", "h2", "h3"}:
            self.heading_stack.append(tag)

    def handle_data(self, data):
        if self.current_tag and data.strip():
            self.text_by_tag.append((self.current_tag, data.strip()))


class StaticSiteTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def parse_page(self, relative):
        html = self.read(relative)
        parser = LinkCollector()
        parser.feed(html)
        return html, parser

    def parse_html(self):
        return self.parse_page("site/index.html")

    def test_required_project_files_exist(self):
        for relative in [
            "PRODUCT.md",
            "DESIGN.md",
            "README.md",
            "site/index.html",
            "site/roadmap.html",
            "site/styles.css",
            "site/.nojekyll",
            ".github/workflows/pages.yml",
        ]:
            self.assertTrue((ROOT / relative).exists(), f"missing {relative}")

    def test_html_parses_and_has_accessibility_landmarks(self):
        html, parser = self.parse_html()
        self.assertIn('<html lang="en">', html)
        self.assertIn('href="#main"', html)
        self.assertIn('id="main"', html)
        self.assertIn("viewport", parser.meta_names)
        self.assertEqual(parser.heading_stack[0], "h1")
        self.assertIn("aria-label", html)

    def test_product_copy_covers_required_distribution_paths(self):
        html, parser = self.parse_html()
        text = re.sub(r"\s+", " ", html)
        required = [
            "Download for macOS",
            "View latest release",
            "Ubuntu / Debian",
            "sudo add-apt-repository ppa:primemanifold/autowhisper",
            "sudo apt install autowhisper",
            "Local-first",
            "privacy",
            "whisper.cpp",
        ]
        for phrase in required:
            self.assertIn(phrase, text)
        self.assertIn("https://github.com/primemanifold/autowhisper/releases/latest", parser.links)
        self.assertIn("https://github.com/primemanifold/autowhisper", parser.links)

    def test_public_repo_links_are_honest_about_private_main_repo(self):
        html, _ = self.parse_html()
        self.assertIn("If the main repository is private", html)
        self.assertIn("Public release links will work once the AutoWhisper repository or mirrored assets are public", html)

    def test_landing_page_has_complete_workflow_story(self):
        html, _ = self.parse_html()
        text = re.sub(r"\s+", " ", html)
        required = [
            "Drop audio or video",
            "Clean transcript output",
            "Export subtitles and notes",
            "Search your transcript library",
            "Batch process long recordings",
            "Hours of audio. Minutes to text.",
            "SRT",
            "VTT",
            "TXT",
            "Markdown",
        ]
        for phrase in required:
            self.assertIn(phrase, text)
        for class_name in [
            "workflow-section",
            "format-dropzone",
            "transcript-compare",
            "export-pills",
            "library-search",
            "batch-queue",
            "contrast-section",
        ]:
            self.assertIn(class_name, html)

    def test_design_system_is_cross_platform_and_machine_readable(self):
        design = self.read("DESIGN.md")
        required = [
            "AutoWhisper Design System",
            "macOS",
            "Linux",
            "mobile",
            "landing page",
            "warm technical minimalism",
            "privacy-first",
            "evidence-backed",
            "Cross-platform implementation notes",
        ]
        for phrase in required:
            self.assertIn(phrase, design)
        self.assertIn('primary: "#18181B"', design)
        self.assertIn('tertiary: "#D97706"', design)

    def test_css_uses_design_system_sections_and_dark_contrast(self):
        css = self.read("site/styles.css")
        required = [
            "--paper",
            "--accent-warm",
            "--success",
            ".workflow-section",
            ".transcript-compare",
            ".export-pills",
            ".library-search",
            ".batch-queue",
            ".contrast-section",
        ]
        for phrase in required:
            self.assertIn(phrase, css)

    def test_no_framework_runtime_or_tracking(self):
        html = self.read("site/index.html")
        css = self.read("site/styles.css")
        combined = (html + css).lower()
        banned = [
            "react", "astro", "vite", "next/script", "googletagmanager", "google-analytics",
            "plausible", "segment.com", "cdn.jsdelivr", "unpkg.com", "script src=",
            "@import", "background-clip: text", "border-left:", "border-right:",
        ]
        for token in banned:
            self.assertNotIn(token, combined)

    def test_copy_avoids_ai_slop_markers(self):
        combined = self.read("site/index.html") + self.read("site/styles.css")
        banned_phrases = [
            "seamless", "unlock", "revolutionize", "supercharge", "game-changing",
            "AI-powered", "cutting-edge", "elevate your", "try it today", "—",
        ]
        for phrase in banned_phrases:
            self.assertNotIn(phrase, combined)

    def test_css_has_responsive_and_focus_states(self):
        css = self.read("site/styles.css")
        self.assertIn("@media", css)
        self.assertRegex(css, r":focus-visible|:focus")
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("oklch", css)
        self.assertNotIn("#000", css)
        self.assertNotIn("#fff", css.lower())

    def test_roadmap_page_is_linked_and_collects_requests_static_safely(self):
        index_html, index_parser = self.parse_html()
        roadmap_html, roadmap_parser = self.parse_page("site/roadmap.html")
        roadmap_text = re.sub(r"\s+", " ", roadmap_html)

        self.assertIn("roadmap.html", index_parser.links)
        self.assertIn("Roadmap", index_html)
        self.assertIn('<form class="request-form"', roadmap_html)
        self.assertIn('method="post"', roadmap_html)
        self.assertRegex(roadmap_html, r'action="mailto:[^"]+subject=AutoWhisper%20roadmap%20request"')
        self.assertIn('enctype="text/plain"', roadmap_html)
        for field in ['name="name"', 'name="email"', 'name="comment"']:
            self.assertIn(field, roadmap_html)
        for label in ["Name", "Email", "Comment"]:
            self.assertRegex(roadmap_html, rf"<label[^>]*>{label}</label>")
        self.assertIn("No request is stored in the browser", roadmap_text)
        self.assertIn("opens your email client", roadmap_text)
        self.assertIn("https://github.com/primemanifold/autowhisper-landing/issues/new", roadmap_parser.links)

    def test_roadmap_page_has_planned_in_progress_and_shipped_sections(self):
        roadmap_html, _ = self.parse_page("site/roadmap.html")
        roadmap_text = re.sub(r"\s+", " ", roadmap_html)
        for phrase in [
            "Now",
            "Next",
            "Later",
            "Recently shipped",
            "macOS onboarding",
            "local-first",
            "Roadmap requests",
        ]:
            self.assertIn(phrase, roadmap_text)
        self.assertIn("roadmap-board", roadmap_html)
        self.assertIn("request-panel", roadmap_html)

    def test_roadmap_page_keeps_static_no_runtime_policy(self):
        roadmap_html = self.read("site/roadmap.html").lower()
        banned = [
            "script src=", "tailwind", "googletagmanager", "google-analytics",
            "plausible", "segment.com", "cdn.jsdelivr", "unpkg.com", "react",
        ]
        for token in banned:
            self.assertNotIn(token, roadmap_html)

    def test_pages_workflow_deploys_public_static_site(self):
        workflow = self.read(".github/workflows/pages.yml")
        required = [
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v3",
            "actions/deploy-pages@v4",
            "path: site",
            "branches: [main]",
        ]
        for phrase in required:
            self.assertIn(phrase, workflow)
        self.assertNotIn("repository.private == false", workflow)


if __name__ == "__main__":
    unittest.main()
