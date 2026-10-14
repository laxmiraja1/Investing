# Coca-Cola, 1988 buy

Berkshire bought Coca-Cola from mid-1988 (14,172,500 shares at year-end 1988; 23,350,000 at year-end 1989). The cutoff is **1989-02-27**, the day before the 1988 letter (dated 1989-02-28), which is the earliest archive document disclosing the position. That date is provisional: see `truth.yaml`. Grading uses both the 1988 and 1989 letters.

## Files

| File | What it is |
|---|---|
| `truth.yaml` | What Buffett did and said; every reason quoted verbatim from the 1988 or 1989 letter. The agent never sees it. |
| `check_financials.py` | Recomputes every subtotal and total in the 1986, 1987 and 1988 annual reports' income statements and balance sheets (97 checks). OCR corrections are listed with the page image they were checked against. |
| `build_packet.py` | Builds `packet/` (with the 1988 annual report) or `packet-upi-only/` (`--upi-only`: 1988 known only from UPI wire stories). |
| `ko-prices-yahoo.txt` | Yahoo daily prices, 1986 to 1989-02-27, split-adjusted. The packet un-adjusts them x16 for the 2-for-1 splits of 1990-05-01, 1992-05-01, 1996-05-01 and 2012-07-27 (Coca-Cola investor relations). |
| `packet/`, `packet-upi-only/` | Committed: `packet.yaml`, `financials.md`, `prices.md`. Not committed: the annual-report and UPI text (copyrighted; rebuild locally). |

Not in git (copyrighted, local only): the three annual-report PDFs (ProQuest), `ocr/`, `news/`, and the report and news text inside the packet folders.

## Batches

Every run is Opus at high effort through `claude -p`, as of 1989-02-27, with the framework filtered to that date. Each batch is 5 named + 5 anonymised runs unless noted. Run folders and `meta.json` carry the batch label.

| Label | Folder | Packet | 1988 information |
|---|---|---|---|
| `pilot` | `runs-pilot/` | `packet/` before the 1988 sources were added | none (1 named + 1 anonymised, plus the leakage probe) |
| `without-1988` | `runs-without-1988/` | `packet/` before the 1988 sources were added | none |
| `with-1988-results` | `runs/` | `packet/` | 1988 annual report (signed 1989-02-18, probably not mailed before the cutoff) + UPI stories |
| `upi-only` | `runs/` | `packet-upi-only/` | UPI stories of 1988-07-14 and 1989-01-31 only (public before the cutoff) |

Scores: per-run `score.json`; `runs-pilot/scores.csv` and `runs-without-1988/scores.csv`; for `runs/` (with-1988-results and upi-only) the grader writes `scores.csv` in this folder.

## Results (price $46.56)

| | without-1988 | with-1988-results | upi-only |
|---|---|---|---|
| Decision | BUY x10 | BUY x10 | BUY x10 |
| Position size | 20% x4, 25% x6 | 25% x10 | 20% x1, 25% x9 |
| Conviction 5 | 0/10 | 5/10 | 0/10 |
| Central intrinsic value, mean (named / anon) | ~$61 / ~$69 | ~$92 / ~$73 | ~$69 / ~$70 |
| Reasoning fidelity, mean (named / anon) | 3.8 / 3.6 | 4.0 / 4.0 | 3.8 / 3.6 |
| Reasons matched of 5, mean (named / anon) | 3.4 / 2.8 | 4.0 / 4.0 | 2.6 / 3.0 |
| "CEO combines marketing and finance" matched | 1/10 | 7/10 | 0/10 |
| Leakage flagged by the grader | 0 | 0 | 0 |

- The decision, a concentrated BUY, is the same in all 30 runs.
- The higher fidelity and valuations in `with-1988-results` disappear when only the public UPI figures are given. They come from the 1988 annual report's detail, which was probably not public at the cutoff. `upi-only` is the batch consistent with the point-in-time rule.
- The leakage probe (`runs-pilot/leakage_probe.json`) identified the anonymised company as Coca-Cola with high confidence and knew the outcome, so named and anonymised runs both draw on the model's memory of this trade.
- Five runs per arm, graded by a model: treat small differences as noise.
