# AutoWhisper Landing

Public static website for AutoWhisper.

- Framework-free HTML and CSS.
- No runtime JavaScript.
- No analytics or tracking scripts.
- Deploys through GitHub Pages from `site/`.

## Local checks

```bash
python3 -m unittest discover tests -v
python3 -m http.server 8080 --directory site
```

Open <http://127.0.0.1:8080/> for local preview.

## Deploy

Push to `main`. The `Deploy GitHub Pages` workflow uploads `site/` and publishes the page through GitHub Pages.

## Main app repo

The primary application repository is <https://github.com/primemanifold/autowhisper>. If that repository or its releases are private, public visitors may not be able to access source or release assets until the app repo is made public or assets are mirrored.