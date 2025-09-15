# Mid-Willamette Area Council Website

This repository contains the public website for the **Mid-Willamette Area Council of Square & Round Dance Clubs**. It’s built with **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** and hosted for free on **GitHub Pages**.

Live site: [https://mwasquaredance.github.io/website/](https://mwasquaredance.github.io/website/)

## Why this repo exists

* Provide a simple, low-cost home for council and club info.
* Make it easy for other councils/clubs to **fork or copy** the site and adapt it for their own use.
* Keep everything plain Markdown with a bit of configuration and simple coding elements.

## Reuse this site (please do!)

Other councils/clubs are **encouraged to fork or copy anything** in this repo.

**Fastest path (fork + rename):**

1. Click **Fork**.
2. In your fork, update `mkdocs.yml`:

   * `site_name`
   * `site_url`
   * Navigation under `nav:`
   * Theme options (logo, palette, etc.)
   * Plugins as needed
3. Replace content in `docs/` with your pages.
4. Enable GitHub Pages or host anywhere you like.

**Copy-paste path:**

* Copy the `mkdocs.yml` and the `docs/` folder structure into your repo and customize.
* Keep the `requirements.txt` so others can reproduce the build.

Attribution is appreciated but not required—see License.

## Built with

* **MkDocs** — static site generator for Markdown
* **Material for MkDocs** — theme and components
* **GitHub Pages** — free hosting
* **Optional plugins** — add what you like in `requirements.txt` and `mkdocs.yml`

## Local development

Prereqs: Python 3.10+ and `pip`.

```bash
# from the repository root
pip install -r requirements.txt
mkdocs serve
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to preview.

## Project structure

```
.
├── docs/                 # All site content (Markdown + assets)
│   ├── index.md          # Home page
│   ├── assets /          # Images, custom CSS & javascript
│   ├── clubs/            # Club pages
│   ├── council/          # Council pages (about, directory)
│   ├── culture/          # General information about square dancing
│   └── dance/            # Other dance opportunities and orgs in Oregon
│   ├── data/             # Single source for directory and other information
├── mkdocs.yml            # Site configuration (nav, theme, plugins)
├── requirements.txt      # Python deps (mkdocs, theme, plugins)
└── .github/workflows/    # (optional) CI for deploy
```

## Contributing

Issues and PRs are welcome. Keep content family-friendly and focused on supporting dancers, callers, cuers, and clubs.

## License

* **Code/config** (everything outside `docs/`): **MIT License**
* **Content** (Markdown, images under `docs/`): **CC BY 4.0**

This means you can copy, remix, and reuse. For content, please include a brief credit like “Content adapted from Mid-Willamette Area Council” with a link back.

## Acknowledgments

* Theme: **Material for MkDocs** by Martin Donath and contributors
* Hosting: **GitHub Pages**

## Contact

For corrections or updates, open an issue or PR on this repository.
