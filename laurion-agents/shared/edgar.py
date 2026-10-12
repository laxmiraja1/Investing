"""Point-in-time helpers for SEC EDGAR.

SEC requires a descriptive User-Agent with contact info: set
SEC_USER_AGENT="Your Name your.email@school.edu" in your environment.

Point-in-time rules applied here:
  * filings are filtered on *filing date*, never period-end date;
  * for XBRL facts, each fiscal period keeps the latest value that had been
    *filed* by `as_of` -- so restatements filed later are invisible.

XBRL company facts only exist from ~2009. For older calibration trades,
use the raw 10-K/10-Q text (list_filings + fetch_document) or Compustat
Point-in-Time via WRDS.

Usage:
  python -m shared.edgar filings KO 1988-06-30
  python -m shared.edgar facts KO 2015-03-31 Revenues NetIncomeLoss
"""

import os
import sys
import time
from datetime import date
from functools import lru_cache
from typing import Dict, List

import requests

_SESSION = requests.Session()
_LAST_CALL = [0.0]


def _get(url: str) -> requests.Response:
    ua = os.environ.get("SEC_USER_AGENT")
    if not ua:
        raise RuntimeError('Set SEC_USER_AGENT="Your Name your.email@school.edu"')
    wait = 0.11 - (time.time() - _LAST_CALL[0])  # SEC fair access: <=10 req/s
    if wait > 0:
        time.sleep(wait)
    _LAST_CALL[0] = time.time()
    r = _SESSION.get(url, headers={"User-Agent": ua}, timeout=30)
    r.raise_for_status()
    return r


@lru_cache(maxsize=1)
def _ticker_map() -> Dict[str, int]:
    data = _get("https://www.sec.gov/files/company_tickers.json").json()
    return {v["ticker"].upper(): int(v["cik_str"]) for v in data.values()}


def cik_for(ticker_or_cik: str) -> int:
    """Current tickers only -- for delisted/renamed companies, pass the CIK."""
    if ticker_or_cik.isdigit():
        return int(ticker_or_cik)
    return _ticker_map()[ticker_or_cik.upper()]


def list_filings(ticker_or_cik: str, as_of: date,
                 forms=("10-K", "10-Q", "8-K", "DEF 14A")) -> List[dict]:
    """Filings with filing date strictly before `as_of`, newest first."""
    cik = cik_for(ticker_or_cik)
    sub = _get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json").json()
    blocks = [sub["filings"]["recent"]]
    for f in sub["filings"].get("files", []):
        blocks.append(_get(f"https://data.sec.gov/submissions/{f['name']}").json())
    out = []
    for b in blocks:
        for i, form in enumerate(b["form"]):
            filed = date.fromisoformat(b["filingDate"][i])
            if form in forms and filed < as_of:
                acc = b["accessionNumber"][i]
                out.append({
                    "form": form,
                    "filing_date": filed.isoformat(),
                    "report_date": b["reportDate"][i],
                    "accession": acc,
                    "url": (f"https://www.sec.gov/Archives/edgar/data/{cik}/"
                            f"{acc.replace('-', '')}/{b['primaryDocument'][i]}"),
                })
    return sorted(out, key=lambda x: x["filing_date"], reverse=True)


def fetch_document(url: str) -> str:
    return _get(url).text


def facts_as_of(ticker_or_cik: str, as_of: date, concepts: List[str],
                taxonomy: str = "us-gaap") -> Dict[str, List[dict]]:
    """XBRL values as they were known on `as_of` (latest filing per period)."""
    cik = cik_for(ticker_or_cik)
    data = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json").json()
    out = {}
    for concept in concepts:
        node = data["facts"].get(taxonomy, {}).get(concept)
        if not node:
            continue
        latest: Dict[tuple, dict] = {}
        for unit, rows in node["units"].items():
            for r in rows:
                if date.fromisoformat(r["filed"]) >= as_of:
                    continue
                key = (unit, r.get("start"), r["end"], r.get("fp"))
                if key not in latest or r["filed"] > latest[key]["filed"]:
                    latest[key] = {"unit": unit, **r}
        out[concept] = sorted(latest.values(), key=lambda r: r["end"])
    return out


if __name__ == "__main__":
    cmd, who, when = sys.argv[1], sys.argv[2], date.fromisoformat(sys.argv[3])
    if cmd == "filings":
        for f in list_filings(who, when)[:25]:
            print(f["filing_date"], f["form"], f["url"])
    elif cmd == "facts":
        for c, rows in facts_as_of(who, when, sys.argv[4:]).items():
            for r in rows[-8:]:
                print(c, r.get("fp"), r["end"], r["val"], r["unit"], "filed", r["filed"])
