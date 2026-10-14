"""Build the Coca-Cola calibration packet (as of 1989-02-27).

  # once: OCR the 1986 and 1987 scans (ocrmypdf + poppler via Homebrew); the
  # 1988 report's ProQuest text layer is used as is.
  ocrmypdf --force-ocr -l eng ko-annual-report-1987.pdf /tmp/ar1987.pdf && pdftotext -layout /tmp/ar1987.pdf ocr/ar1987.txt
  ocrmypdf --force-ocr -l eng ko-10k-1986.pdf          /tmp/ar1986.pdf && pdftotext -layout /tmp/ar1986.pdf ocr/ar1986.txt
  pdftotext -layout ko-annual-report-1988.pdf ocr/ar1988.txt
  # news/upi-1988-07-14.txt and news/upi-1989-01-31.txt: article text pasted by hand
  python check_financials.py      # statement totals must all add up
  python build_packet.py                  # packet/: includes the 1988 annual report
  python build_packet.py --upi-only       # packet-upi-only/: 1988 known only from the UPI stories

Sources (primary or contemporaneous only; no hindsight write-ups):
  - 1988 annual report (ProQuest; chairman's letter signed 1989-02-18, auditor's
    report 1989-01-27). Probably not mailed to shareholders before the cutoff:
    the packet says so. The 1988 figures were public through the 1989-01-31
    earnings release (UPI story).
  - 1987 annual report (ProQuest, dated 1988-02-18): primary for 1987.
  - 1986 annual report (auditor's report dated 1987-02-02): primary for 1985-1986,
    as originally reported. Later reports restate earlier years; financials.md
    says which basis each column uses.
  - UPI wire stories of 1988-07-14 (first half) and 1989-01-31 (full year 1988).
  - Yahoo daily prices, un-adjusted x16 for the 2-for-1 splits of 1990-05-01,
    1992-05-01, 1996-05-01 and 2012-07-27 (Coca-Cola investor relations).
    Prices stop at the last close before as_of.
Report and news text is copyrighted and git-ignored.
"""

import csv
import datetime as dt
import re
import sys
from pathlib import Path

from check_financials import DATA  # verified figures, $ thousands

HERE = Path(__file__).parent
UPI_ONLY = "--upi-only" in sys.argv  # leave out the 1988 annual report and everything derived from it
PACKET = HERE / ("packet-upi-only" if UPI_ONLY else "packet")
AS_OF = dt.date(1989, 2, 27)
SPLIT_FACTOR = 2 ** 4
SHARES_OUT = {1987: 415_977_479 - 43_621_336, 1988: 417_394_567 - 62_606_056}  # issued less treasury

# OCR misreads confirmed against the page image (see check_financials.CORRECTIONS):
# (line must contain, regex to replace, replacement)
TEXT_FIXES = {
    "ar1986": [("Current maturities of long-term debt", r"\b2212\b", "23,212")],
    "ar1988": [("eq-f", r"Net Operating Revenue.*", "Net Operating Revenues   $8,337,831   $7,658,341   $6,976,558")],
}

# OCR variants of names ("Coca-CoLta", "ofCoca-Cola", "CocaCl", "Coe Cols", "Kuough"),
# normalized so the anonymizer's aliases catch them.
NAME_FIXES = [
    (re.compile(r"(?i)(?<=[a-z])(?=c[o0]ca\W?\w)"), " "),           # "THECOCA-COLA", "ofCoca-Cola"
    (re.compile(r"(?i)\bc[o0]ca\W?\w*"), "Coca-Cola"),  # "Coca-CoLta", "Coca-Cala", "CocaÏola", "CocaCl", "Coca-ColdGompany"
    (re.compile(r"\bCoe Cols\b"), "Coca-Cola"),
    (re.compile(r"\bK[a-z]{1,2}ough\b"), "Keough"),
]

NOTES = {
    "ar1988": ("NOTE ON AVAILABILITY: The chairman's letter in this report is signed February 18, 1989, and "
               "the auditor's report is dated January 27, 1989. The printed report was probably not mailed to "
               "shareholders before the as-of date. The 1988 results themselves were public from the "
               "company's January 31, 1989 earnings release (see document upi-1989-01-31)."),
    "upi-1989-01-31": ("UPI wire story, January 31, 1989, reporting the company's full-year 1988 results release. "
                       "Text as published; it states gross profit as \"$4.6 million\", which should read billion."),
    "upi-1988-07-14": "UPI wire story, July 14, 1988, reporting the company's first-half 1988 results. Text as published.",
}

ALIASES = {
    "The Coca-Cola Company": "Company A",
    "Coca-Cola Enterprises": "Company A's bottling affiliate",
    "Coca-Cola": "Brand A",
    "Coke": "Brand A",
    "KO": "AAA",
    "Roberto C. Goizueta": "the Chairman and CEO",
    "Goizueta": "the Chairman and CEO",
    "Donald R. Keough": "the President",
    "Keough": "the President",
    "M. Douglas Ivester": "an executive",
    "Ivester": "an executive",
    "Peter V. Ueberroth": "a director",
    "Ueberroth": "a director",
    "Atlanta": "the headquarters city",
    "Georgia": "the home state",
    "Robert W. Woodruff": "the former chairman",
    "Woodruff": "the former chairman",
    "Columbia Pictures Entertainment": "the entertainment affiliate",
    "Columbia Pictures": "the film studio",
    "Tri-Star": "the second film studio",
    "Columbia": "the film studio",
    "T.C.C. Beverages": "the Canadian bottling affiliate",
    "Minute Maid": "Juice Brand M",
    "Hi-C": "Juice Brand H",
    "Five Alive": "Juice Brand F",
    "Sprite": "Brand S",
    "Fanta": "Brand F",
    "Fresca": "Brand R",
    "Mello Yello": "Brand Y",
    "TAB": "Brand T",
}


def clean_text(path: Path, key: str) -> str:
    out = [NOTES[key], ""] if key in NOTES else []
    for line in path.read_text(encoding="utf-8").splitlines():
        if any(s in line for s in ("Reproduced with permission", "ProQuest", "Add as preferred source")):
            continue  # scanner / website furniture, not part of the document
        toks = line.split()
        if len(toks) >= 8 and sum(len(t) <= 2 for t in toks) / len(toks) > 0.6:
            continue  # OCR noise from decorative rules and photos
        for anchor, wrong, right in TEXT_FIXES.get(key, []):
            if anchor in line:
                assert re.search(wrong, line), f"expected OCR text {wrong!r} on line: {line}"
                line = re.sub(wrong, right, line)
        for pat, repl in NAME_FIXES:
            line = pat.sub(repl, line)
        out.append(re.sub(r" {3,}", "   ", line.rstrip()))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def m(x):  # $ thousands -> $ millions
    return f"{x / 1000:,.1f}"


def financials_md() -> str:
    a8, a7, a6 = DATA["ar1988"], DATA["ar1987"], DATA["ar1986"]
    rows = [
        ("Net operating revenues", "revenue"), ("Gross profit", "gross"), ("Operating income", "op_income"),
        ("Net income", "net_income"),
    ]
    cols = [("1985", a6["is"][1985], a6["bs"][1985], "1986 AR"), ("1986", a6["is"][1986], a6["bs"][1986], "1986 AR"),
            ("1987", a7["is"][1987], a7["bs"][1987], "1987 AR")]
    if UPI_ONLY:
        intro = ("$ millions except per share. Each year comes from that year's own annual report as originally "
                 "reported: 1985-1986 from the 1986 report, 1987 from the 1987 report (dated 1988-02-18). "
                 "1988 results are known only from the company's earnings releases as reported by UPI "
                 "(documents upi-1988-07-14 and upi-1989-01-31).")
    else:
        cols.append(("1988", a8["is"][1988], a8["bs"][1988], "1988 AR"))
        intro = ("$ millions except per share. Each year comes from that year's own annual report as originally "
                 "reported: 1985-1986 from the 1986 report, 1987 from the 1987 report (dated 1988-02-18), 1988 from "
                 "the 1988 report (chairman's letter signed 1989-02-18; probably not mailed before the as-of date, "
                 "but the 1988 income figures were public in the 1989-01-31 earnings release).")
    lines = [
        f"# The Coca-Cola Company: financial summary, 1985-{cols[-1][0]}",
        "",
        intro + " Every figure was checked so that the statement subtotals and totals add up. Per-share "
        "figures are in the dollars of the time (after the 1986 3-for-1 split).",
        "",
        "| | " + " | ".join(f"{y} ({s})" for y, _, _, s in cols) + " |",
        "|---|" + "---|" * len(cols),
    ]
    for label, k in rows:
        lines.append(f"| {label} | " + " | ".join(m(i[k]) for _, i, _, _ in cols) + " |")
    lines.append("| Net income per common share ($) | " + " | ".join(f"{i['eps']:.2f}" for _, i, _, _ in cols) + " |")
    lines.append("| Average common shares (millions) | " + " | ".join(f"{i['avg_shares'] / 1000:,.1f}" for _, i, _, _ in cols) + " |")
    for label, keys in [("Total assets", ("total_assets",)), ("Shareholders' equity", ("equity",)),
                        ("Loans, notes and current maturities", ("loans", "loans_fin_sub", "current_maturities_ltd")),
                        ("Long-term debt", ("ltd", "ltd_fin_sub")), ("Treasury stock, at cost", ("treasury",))]:
        lines.append(f"| {label} | " + " | ".join(m(sum(b.get(k, 0) for k in keys)) for _, _, b, _ in cols) + " |")
    lines.append("| Net income / year-end equity | " + " | ".join(
        f"{i['net_income'] / b['equity']:.1%}" for _, i, b, _ in cols) + " |")
    r = a7["is"]
    lines += [
        "",
        "## Restated bases",
        "",
        "- The 1987 report restates 1985 and 1986 with the entertainment business deconsolidated (it became "
        "Columbia Pictures Entertainment, Inc., a 49%-owned affiliate, in 1987). Net income is unchanged; "
        "revenues and operating income are lower:",
        "",
        "| | 1985 (restated) | 1986 (restated) | 1987 |",
        "|---|---|---|---|",
    ]
    for label, k in rows:
        lines.append(f"| {label} | {m(r[1985][k])} | {m(r[1986][k])} | {m(r[1987][k])} |")
    if not UPI_ONLY:
        b87 = a8["bs"][1987]
        lines += [
            "",
            f"- The 1988 report restates the 1987 balance sheet to consolidate a finance subsidiary: total assets "
            f"{m(b87['total_assets'])} (originally {m(a7['bs'][1987]['total_assets'])}), shareholders' equity "
            f"{m(b87['equity'])} (originally {m(a7['bs'][1987]['equity'])}). 1987 revenue and net income are unchanged.",
        ]
    lines += [
        "",
        ("Not in this packet: the 1988 annual report and 1988 quarterly reports (10-Q). 1988 results appear only "
         "through the UPI stories." if UPI_ONLY else
         "Not in this packet: 1988 quarterly reports (10-Q). Interim 1988 results appear only through the "
         "UPI story of 1988-07-14."),
    ]
    return "\n".join(lines) + "\n"


def prices_md():
    rows, divs = [], []
    with (HERE / "ko-prices-yahoo.txt").open() as f:
        r = csv.reader(f, delimiter="\t")
        next(r)
        for rec in r:
            day = dt.datetime.strptime(rec[0].strip(), "%b %d, %Y").date()
            if day >= AS_OF:
                continue
            if len(rec) == 7:
                rows.append((day, *(float(x) * SPLIT_FACTOR for x in rec[1:5])))
            elif "Dividend" in rec[1]:
                divs.append((day, float(rec[1].split()[0]) * SPLIT_FACTOR))
    rows.sort()
    last_day, *_, last_close = rows[-1]
    year_ago = [x for x in rows if x[0] > last_day - dt.timedelta(days=365)]
    hi, lo = max(x[2] for x in year_ago), min(x[3] for x in year_ago)
    eps87, eps88 = DATA["ar1987"]["is"][1987]["eps"], DATA["ar1988"]["is"][1988]["eps"]
    div88 = sum(d for day, d in divs if day.year == 1988)
    sh_year = 1987 if UPI_ONLY else 1988
    sh = SHARES_OUT[sh_year]
    sh_src = ("issued less treasury, 1987 annual report; the company reported buying back 18.9 million "
              "shares during 1988" if UPI_ONLY else "issued less treasury, 1988 annual report")
    out = [
        "# KO common stock: prices to the last close before the as-of date",
        "",
        f"New York Stock Exchange prices in dollars of the time (after the 1986 3-for-1 split). "
        f"Last close in this table: {last_day.isoformat()}.",
        "",
        f"- Last close ({last_day}): ${last_close:.2f}",
        f"- 52-week range: ${lo:.2f} - ${hi:.2f}",
        f"- Shares outstanding at {sh_year} year-end: {sh:,} ({sh_src}); "
        f"market value at the last close on that count: ${last_close * sh / 1e9:.2f} billion",
        f"- Price / 1988 net income per share (${eps88:.2f}, reported 1989-01-31): {last_close / eps88:.1f}x; "
        f"on 1987 (${eps87:.2f}): {last_close / eps87:.1f}x",
        f"- Dividends paid in 1988: ${div88:.2f} per share ({len([d for d in divs if d[0].year == 1988])} quarterly payments)",
        "",
        "## Month-end closes",
        "",
        "| Month | Close | Month high | Month low |",
        "|---|---|---|---|",
    ]
    months = {}
    for day, o, h, l, c in rows:
        if day >= dt.date(1986, 7, 1):
            mo = months.setdefault((day.year, day.month), {"c": c, "h": h, "l": l})
            mo["c"], mo["h"], mo["l"] = c, max(mo["h"], h), min(mo["l"], l)
    for (y, mo), v in sorted(months.items()):
        out.append(f"| {y}-{mo:02d} | {v['c']:.2f} | {v['h']:.2f} | {v['l']:.2f} |")
    out += ["", "## Daily closes, last 20 trading days", "", "| Date | Close |", "|---|---|"]
    out += [f"| {d.isoformat()} | {c:.2f} |" for d, *_, c in rows[-20:]]
    return "\n".join(out) + "\n", last_day


def main() -> None:
    PACKET.mkdir(exist_ok=True)
    reports = ["ar1986", "ar1987"] + ([] if UPI_ONLY else ["ar1988"])
    for key in reports:
        (PACKET / f"ar-{key[2:]}.txt").write_text(clean_text(HERE / "ocr" / f"{key}.txt", key), encoding="utf-8")
    for key in ("upi-1988-07-14", "upi-1989-01-31"):
        src = HERE / "news" / f"{key}.txt"
        if not src.exists() or not src.read_text(encoding="utf-8").strip():
            raise SystemExit(f"{src} is missing or empty: paste the article text first.")
        (PACKET / f"{key}.txt").write_text(clean_text(src, key), encoding="utf-8")
    (PACKET / "financials.md").write_text(financials_md(), encoding="utf-8")
    prices, last_day = prices_md()
    (PACKET / "prices.md").write_text(prices, encoding="utf-8")
    alias_lines = "\n".join(f'  "{k}": "{v}"' for k, v in ALIASES.items())
    ar88 = "" if UPI_ONLY else """\
  # Signed 1989-02-18, probably not mailed before as_of (see the note at the top of the text).
  - {id: ar-1988, type: annual-report, date_published: 1989-02-18, path: ar-1988.txt}
"""
    fin_date = "1988-02-18" if UPI_ONLY else "1989-02-18"
    (PACKET / "packet.yaml").write_text(f"""\
# Coca-Cola calibration packet{" (UPI-only variant: no 1988 annual report)" if UPI_ONLY else ""}. Built by ../build_packet.py; edit that, not this.
ticker: KO
company: The Coca-Cola Company
as_of: {AS_OF.isoformat()}   # day before the 1988 letter (1989-02-28) disclosed Berkshire's position
question: "Should we buy The Coca-Cola Company at today's price, and how much?"

documents:
  - {{id: ar-1986, type: annual-report, date_published: 1987-02-19, path: ar-1986.txt}}
  - {{id: ar-1987, type: annual-report, date_published: 1988-02-18, path: ar-1987.txt}}
  - {{id: upi-1988-07-14, type: news, date_published: 1988-07-14, path: upi-1988-07-14.txt}}
  - {{id: upi-1989-01-31, type: news, date_published: 1989-01-31, path: upi-1989-01-31.txt}}
{ar88}  - {{id: fin-summary, type: financials, date_published: {fin_date}, path: financials.md}}
  - {{id: prices, type: prices, date_published: {last_day.isoformat()}, path: prices.md}}

aliases:
{alias_lines}
""", encoding="utf-8")
    for p in sorted(PACKET.iterdir()):
        print(f"{p.name}: {len(p.read_text(encoding='utf-8').split()):,} words")


if __name__ == "__main__":
    main()
