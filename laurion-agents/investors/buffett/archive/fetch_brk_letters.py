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
import logging
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
MIN_WORDS = 2000  # every real letter is longer; shorter means a bad download

logging.getLogger("pypdf").setLevel(logging.ERROR)  # font-encoding noise


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(html: str) -> str:
    p = _Text()
    p.feed(html)
    return re.sub(r"\n{3,}", "\n\n", "".join(p.parts)).strip()


def pdf_to_text(data: bytes) -> str:
    from pypdf import PdfReader
    return "\n".join(page.extract_text() or "" for page in PdfReader(io.BytesIO(data)).pages)


def fetch(url: str) -> requests.Response:
    # The site sends some pages Brotli-compressed whether or not we ask;
    # requests decodes them only when the `brotli` package is installed.
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    if r.headers.get("Content-Encoding", "").lower() == "br" and r.content[:1] not in (b"<", b"%"):
        sys.exit("Got undecoded Brotli content: pip install -r requirements.txt (needs brotli).")
    return r


def letter_text(year: int, url: str) -> str:
    r = fetch(url)
    if url.lower().endswith(".pdf"):
        return pdf_to_text(r.content)
    html = r.content.decode("cp1252", errors="replace")  # pages are Word-97 HTML, windows-1252
    text = html_to_text(html)
    if len(text.split()) < MIN_WORDS:
        # 1998-2003: a landing page linking to separate HTML and PDF versions.
        inner = re.findall(rf'href="({year}[^"]*\.(?:html|pdf))"', html, re.I)
        if inner:
            inner.sort(key=lambda h: not h.lower().endswith(".html"))  # prefer HTML
            return letter_text(year, urljoin(url, inner[0]))
    return text


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
    short = []
    for year, url in sorted(links.items()):
        dest = OUT / f"brk-{year}.txt"
        if dest.exists() and len(dest.read_text(encoding="utf-8").split()) >= MIN_WORDS:
            continue
        text = letter_text(year, url)
        dest.write_text(text, encoding="utf-8")
        words = len(text.split())
        print(f"{year}: {words:,} words  <- {url}")
        if words < MIN_WORDS:
            short.append(year)
        time.sleep(0.5)
    if short:
        print("Suspiciously short (check by hand):", *short)

    with (HERE / "manifest.csv").open(newline="", encoding="utf-8") as f:
        wanted = [r["path"] for r in csv.DictReader(f)
                  if r["id"].startswith("brk-letter-")]
    missing = [p for p in wanted if not (HERE / p).exists()]
    if missing:
        print("Still missing (download manually):", *missing, sep="\n  ")


if __name__ == "__main__":
    main()
