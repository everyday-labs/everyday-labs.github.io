# everyday-labs.github.io

Source for the [Everyday Labs](https://everyday-labs.github.io) website — a small home for
open-source apps.

Plain Markdown, built automatically by GitHub Pages (Jekyll, `minima` theme). Edit a `.md`
file, push to `main`, and the site updates in about a minute.

| Page | File |
|---|---|
| Home | `index.md` |
| About | `about.md` |
| Bulkmate (5 product pages + feedback) | `bulkmate/*.html` |
| Bulkmate privacy policy | `bulkmate/privacy.md` (copy of `costco-mobile/docs/PRIVACY.md`) |
| Bulkmate support | `bulkmate/support.md` |

Bulkmate's product pages (`bulkmate/index.html`, `receipts`, `scanner`, `rewards`,
`spending`, `feedback`) are standalone HTML sharing `assets/bulkmate.css`.
`_tools/sync_artifacts.py` turns them into the matching Claude artifact files.
