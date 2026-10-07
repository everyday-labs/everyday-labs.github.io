#!/usr/bin/env python3
"""Build Claude-artifact versions of the Bulkmate product pages.

The website pages in bulkmate/*.html are the source of truth. Artifacts can't
load /assets/bulkmate.css or follow site-relative links, so this inlines the
shared stylesheet and points the series links at the matching artifacts.
Artifacts get their own <!doctype>/<head> wrapper when published, so the output
is just <title> + <style> + the page body.

Usage: python3 _tools/sync_artifacts.py <out-dir>
Then publish each <out-dir>/<name>.html to its artifact URL (ARTIFACTS below).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ARTIFACTS = {
    '/bulkmate/':          'https://claude.ai/code/artifact/0af25bd7-8405-4942-b3eb-036036c1e59a',
    '/bulkmate/receipts/': 'https://claude.ai/code/artifact/11f7fa05-1be7-4780-bca5-d507b7fa96a5',
    '/bulkmate/scanner/':  'https://claude.ai/code/artifact/a4c5f932-308b-4f3a-a5c6-ea85eb271ef4',
    '/bulkmate/rewards/':  'https://claude.ai/code/artifact/98d46a4f-00d1-4454-a21d-23e8070fcc14',
    '/bulkmate/spending/': 'https://claude.ai/code/artifact/41d899b9-b02c-4ba5-a517-783c365f4899',
}
PAGES = {'index': '/bulkmate/', 'receipts': '/bulkmate/receipts/', 'scanner': '/bulkmate/scanner/',
         'rewards': '/bulkmate/rewards/', 'spending': '/bulkmate/spending/'}


def build(name: str) -> str:
    src = (ROOT / 'bulkmate' / f'{name}.html').read_text()
    title = re.search(r'<title>(.*?)</title>', src, re.S).group(1)
    page_css = re.search(r'<style data-page>(.*?)</style>', src, re.S).group(1)
    body = re.search(r'<!-- page -->(.*?)<!-- /page -->', src, re.S).group(1)
    shared = (ROOT / 'assets' / 'bulkmate.css').read_text()
    for path, url in ARTIFACTS.items():
        body = body.replace(f'href="{path}"', f'href="{url}"')
    leftover = re.findall(r'href="/[^"]*"', body)
    if leftover:
        raise SystemExit(f'{name}: unmapped site-relative links {leftover}')
    return f'<title>{title}</title>\n<style>\n{shared}\n{page_css}</style>\n{body.strip()}\n'


if __name__ == '__main__':
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name in PAGES:
        (out / f'{name}.html').write_text(build(name))
        print(f'{name}.html -> {ARTIFACTS[PAGES[name]]}')
