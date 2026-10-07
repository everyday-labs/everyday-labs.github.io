# everyday-labs.github.io

Source for the [Everyday Labs](https://everyday-labs.org) website — a small home for
open-source apps.

Plain Markdown, built automatically by GitHub Pages (Jekyll, `minima` theme). Edit a `.md`
file, push to `main`, and the site updates in about a minute. The custom domain
`everyday-labs.org` is set by `CNAME`; site title, contact email (`hello@everyday-labs.org`) and
the nav bar live in `_config.yml`.

| Page | File |
|---|---|
| Home | `index.md` |
| About | `about.md` |
| Bulkmate (5 product pages + feedback) | `bulkmate/*.html` |
| Bulkmate privacy policy | `bulkmate/privacy.md` (copy of `costco-mobile/docs/PRIVACY.md`) |
| Bulkmate support | `bulkmate/support.md` |
| Price-drop alerts (universal-link fallback) | `alerts/index.md` |
| Universal-link file for iOS | `.well-known/apple-app-site-association` |

`costco-mobile/docs/PRIVACY.md` lives in the Bulkmate app repo (`costco-app`) and is the source
of truth: edit it there, then copy it into `bulkmate/privacy.md` below the front matter (drop the
`# Bulkmate — Privacy Policy` heading, the page layout supplies the title).

Bulkmate's price-drop emails link to `https://everyday-labs.org/alerts`. With the app installed,
iOS opens it straight to the Alerts screen via the `apple-app-site-association` file (app ID
`XX3T25NCVV.com.twonk0609.bulkmate`); otherwise `alerts/index.md` shows a button that opens the
app. `_config.yml` includes `.well-known`, which Jekyll would otherwise skip.

Bulkmate's product pages (`bulkmate/index.html`, `receipts`, `scanner`, `rewards`,
`spending`, `feedback`) are standalone HTML sharing `assets/bulkmate.css`.
`_tools/sync_artifacts.py` turns the five product pages into the matching Claude artifact files:
run `python3 _tools/sync_artifacts.py <out-dir>`, then publish each output file to the artifact
URL listed in the script's `ARTIFACTS` map.
