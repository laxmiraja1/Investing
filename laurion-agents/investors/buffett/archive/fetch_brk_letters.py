"""Download Berkshire Hathaway shareholder letters (1977 onward) as text.

  pip install pypdf
  python investors/buffett/archive/fetch_brk_letters.py

Reads the index at berkshirehathaway.com/letters/letters.html, saves each
letter to archive/private/letters/brk-<year>.txt (git-ignored: the letters
are copyrighted, so each teammate downloads their own copy), and reports
any year in manifest.csv that is still missing.

The partnership letters (1957-1970) are not on Berkshire's site; collect
them separately (see sources.md).
"""

import csv
import io
import re
import sys
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

import requests

INDEX = "https://www.berkshirehathaway.com/letters/letters.html"
HERE = Path(__file__).parent
OUT = HERE / "private" / "letters"
HEADERS = {"User-Agent": "laurion-agents research (academic project)"}


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(html: str) -> str:
    p = _Text()
    p.feed(html)
    return re.sub(r"\n{3,}", "\n\n", "".join(p.parts)).strip()


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader
    return "\n".join(page.extract_text() or "" for page in PdfReader(io.BytesIO(data)).pages)


def letter_links() -> dict:
    html = requests.get(INDEX, headers=HEADERS, timeout=30).text
    links = {}
    for href, label in re.findall(r'href="([^"]+\.(?:html|pdf))"[^>]*>(.*?)</a>', html, re.I | re.S):
        m = re.search(r"\b(19[789]\d|20\d\d)\b", label + " " + href)
        if m:
            links.setdefault(int(m.group(1)), urljoin(INDEX, href))
    return links


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    links = letter_links()
    if not links:
        sys.exit("No letter links found -- the index page layout may have changed.")
    for year, url in sorted(links.items()):
        dest = OUT / f"brk-{year}.txt"
        if dest.exists():
            continue
        r = requests.get(url, headers=HEADERS, timeout=60)
        r.raise_for_status()
        text = pdf_to_text(r.content) if url.lower().endswith(".pdf") else html_to_text(r.text)
        dest.write_text(text, encoding="utf-8")
        print(f"{year}: {len(text.split()):,} words  <- {url}")
        time.sleep(0.5)

    with (HERE / "manifest.csv").open(newline="", encoding="utf-8") as f:
        wanted = [r["path"] for r in csv.DictReader(f)
                  if r["id"].startswith("brk-letter-")]
    missing = [p for p in wanted if not (HERE / p).exists()]
    if missing:
        print("Still missing (download manually):", *missing, sep="\n  ")


if __name__ == "__main__":
    main()
