# Stage 4: Valuation (§5) and Catalyst / timing (§6)

## §5 as written: buy below net working capital (`bpl-letter-1965`)

At this date the framework's only valuation rule is the net-working-capital bargain test. Applied to the end-1988 balance sheet (`ar-1988`):

| $M | End-1988 |
|---|---|
| Current assets | 3,245.4 |
| − Current liabilities | (2,868.9) |
| **Net working capital** | **376.5**, or **$1.06 per share** on 354.8M shares |
| − Long-term debt, other liabilities, deferred taxes, preferred | (1,536.4) |
| Net working capital less all prior claims | negative |
| Tangible book (common equity $3,045.3M − intangibles $56.5M) | $2,988.8M, or $8.42 per share |

At $46.56 the stock sells for **44 times net working capital** and **5.5 times tangible book**. **It fails the rule completely.**

Should the analysis stop there? The investor's own writing from this period says the bargain test is no longer the operative standard for a franchise business:

- `brk-letter-1987#18`: "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… In the interim, I searched for 'bargains' – and had the misfortune to find some."
- `brk-letter-1981#3`: "We may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting." The test there is prices "that will make sense, even should the future of the acquired enterprise develop much along the lines of its past."
- `bpl-letter-1963#5`: the earlier measure was "value to a private owner," and the net-working-capital figure was only a floor under that.

**I note the failure, and I value the business the way that evidence directs.** The method is owner earnings (§3.3, `brk-letter-1986`), valued on the assumption that the future looks like the past, not on management's forecasts. Management's guidance of "mid-teens" EPS growth for 1989 (`upi-1989-01-31`) is a projection, and the framework says projections are "of little interest" (`brk-letter-1982`). I do not use it.

---

## Inputs

**1. Owner earnings, core business only.** Starting from Stage 2, I remove the affiliates (valued separately below) and the financing items (net interest and preferred, deducted separately):

| $M, 1988 | Low | Mid | High |
|---|---|---|---|
| Owner earnings (from Stage 2) | 827.7 (all capex treated as maintenance, no deferred tax) | 913.0 (3-year average capex) | 1,088.6 (maintenance capex ≈ depreciation) |
| − Equity income | (48.3) | (48.3) | (48.3) |
| + After-tax net interest ($31.2M × 0.66) | 20.6 | 20.6 | 20.6 |
| **Core owner earnings** | **≈ 800** | **≈ 885** | **≈ 1,061** |

**2. Growth "along the lines of its past."** This uses aggregate figures, so the buyback boost to per-share numbers is excluded.
- Operating income rose from $602M (1978) to $1,598M (1988), about 10.3% a year (`ar-1988` selected data, restated basis).
- Net income rose from $375M to $1,045M, about 10.8% a year.

**Past-like case:** 10% a year for 10 years, then 5%. **Slower case:** 7%, then 4%. The slower case allows for some of 1986–88 having been helped by the weak dollar.

**3. Discount rate. The packet does not contain it.** The investor would compare against long-term government bond yields, which the packet does not give. I use management's own after-tax cost of capital, **12%** (`ar-1988` MD&A), as the demanding case, and **10%** as an alternative. This assumption is not supported by anything in the packet and moves the answer more than any other input.

**4. Other assets and claims.**
- Affiliates: carried at $1,912M. Publicly traded investees are worth $291M more than that (`ar-1988` Note 3), so I value them at about **$2,203M**.
- Claims ahead of the common: net debt $893M ($2,124M total debt − $1,231M cash and securities) plus $300M of preferred, about **$1,193M**. This leaves out about $324M of finance-subsidiary receivables, which is conservative.
- Net addition to the core value: **+$1,010M, or +$2.85 per share.**

---

## Calculation

Value of the core business = present value of years 1–10 of owner earnings + present value of a terminal value at year 10.

**Worked example: mid case, 10%/5% growth, 12% discount rate.**
- Years 1–10: $885M × Σ(1.10/1.12)^t = $885M × 9.069 = $8,026M.
- Year-10 owner earnings: $885M × 1.10^10 = $2,296M. Year 11: $2,410M.
- Terminal value: $2,410M / (0.12 − 0.05) = $34,433M. Discounted: ÷ 1.12^10 (3.106) = $11,087M.
- Core value: $19,113M. Plus $1,010M = $20,123M equity, or **$56.72 per share**.

**Results per share** (354.8M shares; price $46.56). Margin of safety = (value − price) / value.

| Growth case | Discount rate | Low owner earnings | Mid owner earnings | High owner earnings |
|---|---|---|---|---|
| Past-like (10% → 5%) | 12% | $51.5 (MoS 10%) | **$56.7 (MoS 18%)** | $67.4 (MoS 31%) |
| Past-like (10% → 5%) | 10% | $72.8 (36%) | $80.2 (42%) | $95.6 (51%) |
| Slower (7% → 4%) | 12% | n/a | **$43.0 (price 8% above value)** | n/a |
| Slower (7% → 4%) | 10% | n/a | $57.1 (18%) | n/a |
| No growth at all | 12% | n/a | $885M / 0.12 + $1,010M = **$23.6** | n/a |

**What the price implies.** Market value of $16.52B, plus $1.19B of claims, minus $2.20B of affiliates, leaves **$15.51B for the core**. That is about **17.5 times mid owner earnings**, an owner-earnings yield of about **5.7%**, or about 9.7 times 1988 pretax operating income. At a 12% discount rate, that price assumes owner earnings grow about **8% a year for a decade, then 4–5%**. The company's own record over the last decade was about 10–11%.

---

## Cross-checks

- **The stock's own history** (`ar-1988` selected data). P/E was about 9.8x at end-1980, 13x in 1984, and about 15.3–15.7x in 1985–88. Today it is 16.3x on 1988 EPS. The stock is not cheap relative to its own past. It sits near its 52-week high of $49.12 (`prices`). Mr. Market is not offering a bargain today. He is pricing a great business at roughly its usual multiple.
- **Private-owner check.** A buyer paying $16.5B gets about $0.9B of owner earnings that require little capital to grow, plus a world-share position that is rising (Stage 2). That passes the `brk-letter-1981#3` test only if the past-like future holds. With no growth, the core is worth about half the price.
- **Stage 3 buyback question.** On the 12%, past-like range of about $51–67, the company's 1988 repurchases at about $40 were made roughly 22–40% below value. That is "below," and at the upper values "well below," the line set in `brk-letter-1984#4`.
- **Imprecision.** "Business value is a soft number… two equally well-informed observers might make judgments more than 10% apart" (`brk-letter-1986#0`). The range above is wider than 10%, which is appropriate.

---

## Margin of safety against the hurdle

- **Strict §5 hurdle (below net working capital): no margin of safety; fails.**
- **Franchise standard ("a sensible price"; "comfortable margin of safety," `bpl-letter-1962#4`).** The framework sets no number. At management's demanding 12% rate, the margin is modest: **about 10–30%, centered near 18%**. It is wiped out if growth slows to about 7%. At a 10% rate the margin is **35–50%**. In every case the margin depends entirely on the moat holding for more than ten years, not on assets.

That makes the decision a bet on Stage 2's judgment of the business, not on the balance sheet. The moat evidence is strong: share rising from 38% to 45%, international per-capita consumption about one-fifth of the U.S. level, and pricing power. A margin that depends on durability is exactly the kind of margin `brk-letter-1987#18` describes accepting for "an outstanding business at a sensible price." It also explains why the framework links large position size to "a very low probability that anything could drastically change the underlying value" (`bpl-letter-1965`, §7).

**My reading:** this is a sensible price, not a bargain. The value is about $57 per share against a price of $46.56 on the central case at a demanding discount rate, and noticeably more if the long-term interest rate missing from the packet is near 10%.

---

## §6 Catalyst / timing

| Rule | Applies? | Reason |
|---|---|---|
| **No catalyst needed** (`brk-letter-1987`: "The market may ignore business success for a while, but eventually will confirm it") | **Yes, this is the governing rule** | The thesis is that owner earnings compound at about 10% or more. The price follows over time. Nothing has to happen. |
| **Work-out** (`bpl-letter-1957`) | No | No sale, merger, liquidation or tender is pending. The ongoing buyback (14.4M shares left under the 40M authorization, `ar-1988`) is not a work-out. It is a slow positive for a long-term holder, whose percentage ownership rises as the company buys stock. |
| **Control** (`bpl-letter-1963`) | No | With a $16.5B market value, Berkshire would be a passive minority owner, like its three "permanent holdings" (`brk-letter-1987#18`). |
| **"Mr. Market is there to serve you, not to guide you"** (`brk-letter-1987`) | Yes, as a caution | The price is near its 52-week high and at the top of its decade-long multiple range. That is not a timing signal, since the framework does not forecast markets (`bpl-letter-1966-mid`). It does mean the margin of safety comes from the business's growth, not from today's price. |

---

## Missing from the packet

1. **The long-term government bond yield.** This is the investor's real alternative and the largest swing factor: about $57 versus about $80 per share.
2. **The split between maintenance and growth capex.** It moves owner earnings by about ±$130M.
3. **Constant-currency growth.** Needed to know how much of 1986–88 was the weak dollar. About 79% of soft-drink operating income is earned abroad.
4. **Berkshire's own opportunity set and available cash on this date.** This is relevant to sizing in the next stage.

**Carry-forward to Stage 5 (risk and sizing):** whether the probability of a drastic change to the franchise is low enough to justify concentrating at a modest, durability-based margin of safety.