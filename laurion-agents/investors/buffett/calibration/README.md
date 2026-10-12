# Buffett calibration trades

Recommended set: five trades covering a buy, a sell, a pass, an admitted mistake and a less memorized position. Full candidate list with sources is in `../trades.csv`.

| # | Folder | Trade | as_of (draft) | Tests | Leakage risk | Data |
|---|---|---|---|---|---|---|
| 1 | `1988-ko-buy` | Coca-Cola buy | 1988-06-30 | The classic quality-at-fair-price buy | **Very high**: use it as the leakage benchmark (compare named vs anonymized runs) | Pre-EDGAR: 10-Ks via Baker Library; prices via CRSP |
| 2 | `2011-ibm-buy` | IBM buy | 2011-03-31 | Admitted mistake. Does the agent make the same error for the same reasons? Also tests the "no tech" caricature. | Medium-high | EDGAR + XBRL work |
| 3 | `2020-airlines-sell` | Sale of US airline stakes | 2020-04-01 | Sell discipline when the future becomes unknowable | Medium | EDGAR + XBRL work; AGM 2020 explains it (excluded by date) |
| 4 | `2020-japan-buy` | Five Japanese trading houses | 2020-07-31 | Non-US; capital allocation; yen-funded | Medium | Company IR reports (not on EDGAR) |
| 5 | `1999-tech-pass` | Passing on a dot-com era tech leader | 1999-06-30 | PASS for the right reasons: circle of competence plus valuation | Medium | EDGAR 10-K text |

Alternates: PetroChina buy 2002-03 (obscure, good for leakage) and GEICO 1976 (Graham-to-quality transition).

**Holdout:** Keep #4 and #5 back. Tune the framework and prompts on #1-#3 only, freeze the agent, then run #4 and #5 once and report the results as they come.

## For each trade
1. Create `<folder>/packet/packet.yaml` and its documents. Use only material public before `as_of`: the company's filings, the price, contemporaneous news. Add aliases for anonymization: company, ticker, brands, CEO, HQ city.
2. Create `<folder>/truth.yaml` from Buffett's own explanation, which the agent never sees. Every documented reason should cite an archive id.
3. Run:
   ```bash
   python -m shared.run_agent --investor investors/buffett \
       --packet investors/buffett/calibration/<folder>/packet --runs 5 --both --probe
   python -m shared.judge --trade investors/buffett/calibration/<folder>
   ```
4. Write `<folder>/writeup.md`: where the agent matched and diverged, and why.
