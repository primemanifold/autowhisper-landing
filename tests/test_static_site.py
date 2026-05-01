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

    def parse_html(self):
        html = self.read("site/index.html")
        parser = LinkCollector()
        parser.feed(html)
        return html, parser

    def test_required_project_files_exist(self):
        for relative in [
            "PRODUCT.md",
            "DESIGN.md",
            "README.md",
            "site/index.html",
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
