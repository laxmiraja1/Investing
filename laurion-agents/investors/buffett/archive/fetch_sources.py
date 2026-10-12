"""Download the non-letter Buffett sources that have a public copy.

  python investors/buffett/archive/fetch_sources.py            # everything
  python investors/buffett/archive/fetch_sources.py bpl agm    # some groups

Groups:
  bpl       Buffett Partnership letters 1957-1970, split out of a public
            compilation PDF into one file per letter (dates checked
            against the table below).
  agm       Berkshire annual meeting transcripts 1994-2024 from CNBC's
            Warren Buffett Archive (morning + afternoon in one file).
  articles  Fortune 1977/1999/2001, Superinvestors (1984), Owner's
            Manual (1996).

Files land at their manifest.csv paths under archive/private/ (git-ignored:
all of this is copyrighted; each teammate downloads their own copy).
Existing files are kept unless shorter than the group's minimum length.
Anything with no scriptable public copy is listed at the end for manual
download (see MANUAL).
"""

import csv
import html
import re
import sys
import time
from datetime import date
from pathlib import Path

from fetch_brk_letters import HEADERS, fetch, html_to_text, pdf_to_text  # same folder

HERE = Path(__file__).parent

# --- Buffett Partnership letters ---------------------------------------------

BPL_SOURCES = [  # same compilation, two hosts
    "https://focusedcompounding.com/wp-content/uploads/2018/04/Complete_Buffett_partnership_letters-1957-70.pdf",
    "https://brianlangis.wordpress.com/wp-content/uploads/2017/01/warren-buffett-partnership-letters-1957-70.pdf",
]
# (manifest id, date on the letter) in compilation order. 1957 is undated.
BPL_LETTERS = [
    ("bpl-letter-1957", None),
    ("bpl-letter-1958", "1959-02-11"),
    ("bpl-letter-1959", "1960-02-20"),
    ("bpl-letter-1960", "1961-01-30"),
    ("bpl-letter-1961-mid", "1961-07-22"),
    ("bpl-letter-1961", "1962-01-24"),
    ("bpl-letter-1962-mid", "1962-07-06"),
    ("bpl-letter-1962-nov", "1962-11-01"),
    ("bpl-letter-1962", "1963-01-18"),
    ("bpl-letter-1963-mid", "1963-07-10"),
    ("bpl-letter-1963-nov", "1963-11-06"),
    ("bpl-letter-1963", "1964-01-18"),
    ("bpl-letter-1964-mid", "1964-07-08"),
    ("bpl-letter-1964", "1965-01-18"),
    ("bpl-letter-1965-mid", "1965-07-09"),
    ("bpl-letter-1965-nov", "1965-11-01"),
    ("bpl-letter-1965", "1966-01-20"),
    ("bpl-letter-1966-mid", "1966-07-12"),
    ("bpl-letter-1966", "1967-01-25"),
    ("bpl-letter-1967-mid", "1967-07-12"),
    ("bpl-letter-1967-oct", "1967-10-09"),
    ("bpl-letter-1967", "1968-01-24"),
    ("bpl-letter-1968-mid", "1968-07-11"),
    ("bpl-letter-1968", "1969-01-22"),
    ("bpl-letter-1969-may", "1969-05-29"),
    ("bpl-letter-1969-oct", "1969-10-09"),
    ("bpl-letter-1969-dec05", "1969-12-05"),
    ("bpl-letter-1969-dec26", "1969-12-26"),
    ("bpl-letter-1970-feb", "1970-02-25"),
]
_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]
_LETTERHEAD = re.compile(
    r"WARREN E\.? BUFFETT\s*\n?\s*5202 Underwood|BUFFETT PARTNERSHIP[,.] LTD\.?\s*\n?\s*[68]10 KIEWIT", re.I)


def _letter_date(body: str):
    """Date under the letterhead (1961+) or in the sign-off, e.g. '2-11-59'."""
    m = re.search(r"(%s)\s*(\d{1,2})?(?:st|nd|rd|th)?\s*,?\s*(19[5-7]\d)" % "|".join(_MONTHS), body[:400])
    if m and m.group(2):
        return date(int(m.group(3)), _MONTHS.index(m.group(1)) + 1, int(m.group(2)))
    sig = re.findall(r"Buffett\s+[A-Za-z]{0,4}\s*(?:(\d{1,2})-(\d{1,2})-(\d\d)|(%s) (\d{1,2}), (19\d\d))" % "|".join(_MONTHS),
                     body[-800:], re.I)
    if sig:
        mo, d, yy, mname, d2, yyyy = sig[-1]
        return date(1900 + int(yy), int(mo), int(d)) if mo else date(int(yyyy), _MONTHS.index(mname) + 1, int(d2))
    return None


def bpl(paths: dict) -> list:
    problems = []
    for url in BPL_SOURCES:
        try:
            text = re.sub(r"[ \t]+", " ", pdf_to_text(fetch(url).content))
            break
        except Exception as e:  # try the mirror
            print(f"  {url}: {e}")
    else:
        return ["bpl: no compilation host reachable"]
    starts = [m.start() for m in _LETTERHEAD.finditer(text)]
    if len(starts) != len(BPL_LETTERS):
        return [f"bpl: found {len(starts)} letters, expected {len(BPL_LETTERS)}; layout changed, split by hand"]
    for k, (doc_id, expected) in enumerate(BPL_LETTERS):
        body = text[starts[k]: starts[k + 1] if k + 1 < len(starts) else len(text)]
        got = _letter_date(body)
        if (got.isoformat() if got else None) != expected:
            problems.append(f"bpl: {doc_id} dated {got} in the text, expected {expected}")
        dest = HERE / paths[doc_id]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(body.strip() + "\n", encoding="utf-8")
        print(f"  {doc_id}: {len(body.split()):,} words")
    return problems


# --- Annual meetings (CNBC Warren Buffett Archive) ----------------------------

CNBC = "https://buffett.cnbc.com"


def _meeting_date(year_html: str, year: int, links: list):
    m = re.search(r"Annual Meeting\s*[—-]+\s*\((%s) (\d{1,2}), (\d{4})\)" % "|".join(_MONTHS),
                  html_to_text(year_html).replace("\n", " "))
    if m:
        return date(int(m.group(3)), _MONTHS.index(m.group(1)) + 1, int(m.group(2)))
    for l in links:  # 2020 page has no date line; its URLs end "may-02-2020"
        m = re.search(r"-(may|april)-(\d\d)-(%d)" % year, l)
        if m:
            return date(year, 5 if m.group(1) == "may" else 4, int(m.group(2)))
    return None


def _unmangle(s: str) -> str:
    """CNBC stores some punctuation double-encoded (an em dash arrives as
    'â\\x80\\x94'). Re-decode just those runs."""
    def fix(m):
        try:
            return m.group(0).encode("latin-1").decode("utf-8")
        except UnicodeError:
            return m.group(0)
    return re.sub(r"[\xc2-\xf4][\x80-\xbf]{1,3}", fix, s)


def _transcript(url: str) -> str:
    page = fetch(url).content.decode("utf-8", errors="replace")  # no charset header; don't let requests guess
    paras = re.findall(r'<p data-speaker="[^"]*"[^>]*>(.*?)</p>', page, re.S)
    return "\n\n".join(_unmangle(html.unescape(re.sub(r"<[^>]+>", "", p))).strip() for p in paras)


def agm(paths: dict, years=range(1994, 2025)) -> list:
    problems = []
    for y in years:
        doc_id = f"agm-{y}"
        dest = HERE / paths[doc_id]
        if dest.exists() and len(dest.read_text(encoding="utf-8").split()) > 10000:
            continue
        page = fetch(f"{CNBC}/{y}-berkshire-hathaway-annual-meeting/").text
        links = sorted(set(re.findall(r'href="(%s/video/\d{4}/\d\d/\d\d/[^"]+\.html)"' % CNBC, page)))
        sessions = [l for l in links if re.search(r"morning-session|afternoon-session|/part-\d|annual-meeting(-qa)?--+may", l)]
        sessions.sort(key=lambda l: (("afternoon" in l or "part-2" in l or "-qa-" in l), l))
        when = _meeting_date(page, y, sessions)
        if not sessions or not when:
            problems.append(f"agm: {y} sessions={len(sessions)} date={when}; fetch by hand")
            continue
        parts = []
        for i, l in enumerate(sessions, 1):  # CNBC's slugs can name the wrong year (2021 says 2019)
            parts.append(f"=== Session {i} of {len(sessions)} ({l}) ===\n\n{_transcript(l)}")
            time.sleep(1)
        text = f"Berkshire Hathaway annual meeting, {when.isoformat()}\nSource: {CNBC}/{y}-berkshire-hathaway-annual-meeting/\n\n" + "\n\n".join(parts)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(f"  {doc_id}: {when}  {len(text.split()):,} words, {len(sessions)} sessions")
        time.sleep(1)
    return problems


# --- Articles -----------------------------------------------------------------

def _fortune(url: str) -> str:
    page = fetch(url).text
    out = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", page, re.S):
        t = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", p)).split())
        if len(t) < 40 or re.search(r"Subscribe|Fortune Media IP|FORTUNE may receive|©|Sign up|newsletter|^Also from", t):
            continue
        out.append(t)
    return "\n\n".join(out)


def _html(url: str) -> str:
    return html_to_text(fetch(url).content.decode("cp1252", errors="replace"))


def _pdf(url: str) -> str:
    return pdf_to_text(fetch(url).content)


def _superinvestors(url: str) -> str:
    # This copy is a book appendix: drop the book editor's (post-1984) note
    # and start at the first line of the talk.
    text = _pdf(url)
    start = text.find("Is the Graham and Dodd")
    return text[start:] if start >= 0 else ""


ARTICLES = {  # manifest id: (url, extractor, minimum words)
    "fortune-1977-inflation": ("https://fortune.com/2011/06/12/buffett-how-inflation-swindles-the-equity-investor-fortune-classics-1977/", _fortune, 5000),
    "fortune-1999-market": ("https://fortune.com/1999/11/22/warren-buffett-on-stock-market/", _fortune, 3500),
    "fortune-2001-market": ("https://dc.fortune.com/2001/12/10/warren-buffett-stock-market/", _fortune, 3500),
    "superinvestors-1984": ("https://www.lapasserelle.com/courses/advanced_finance/documents/TheSuperinvestorsofGraham-and-Doddsville-WarrenE.Buffett.pdf", _superinvestors, 5000),
    "owners-manual-1996": ("https://berkshirehathaway.com/1996ar/manual.html", _html, 5000),
}

MANUAL = {
    "nyt-2008-buy-american": "https://www.nytimes.com/2008/10/17/opinion/17buffett.html "
                             "(paywalled; blocks scripts). Save the article text only.",
}


def articles(paths: dict) -> list:
    problems = []
    for doc_id, (url, extract, min_words) in ARTICLES.items():
        dest = HERE / paths[doc_id]
        if dest.exists() and len(dest.read_text(encoding="utf-8").split()) >= min_words:
            continue
        try:
            text = extract(url)
        except Exception as e:
            problems.append(f"{doc_id}: {e}; fetch by hand from {url}")
            continue
        words = len(text.split())
        if words < min_words:
            problems.append(f"{doc_id}: only {words:,} words (expected {min_words:,}+); check {url}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(f"  {doc_id}: {words:,} words")
        time.sleep(0.5)
    return problems


def main() -> None:
    with (HERE / "manifest.csv").open(newline="", encoding="utf-8") as f:
        paths = {r["id"]: r["path"] for r in csv.DictReader(f)}
    groups = sys.argv[1:] or ["bpl", "agm", "articles"]
    problems = []
    for g in groups:
        print(f"[{g}]")
        problems += {"bpl": bpl, "agm": agm, "articles": articles}[g](paths)
    missing = [i for i in MANUAL
               if not (HERE / paths[i]).exists() or not (HERE / paths[i]).read_text(encoding="utf-8").strip()]
    if missing:
        print("\nDownload by hand (save as plain text at the manifest path):")
        for i in missing:
            print(f"  {i} -> {paths[i]}\n      {MANUAL[i]}")
    if problems:
        print("\nProblems:", *problems, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
