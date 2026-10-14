# Stage 4: Valuation (Framework §5) and Catalyst / timing (§6)

## 5.1 The framework's valuation rule: net working capital

The only valuation rule the framework records is the Partnership-era bargain test: value "net working capital alone (before placing any value on the plants and equipment)" (`bpl-letter-1965`).

**End-1987 figures (`ar-1987` balance sheet), the latest balance sheet in the packet:**

| | $M |
|---|---|
| Total current assets | 4,136.2 |
| Total current liabilities | (4,118.5) |
| **Net working capital** | **~17.7** |
| Per share (372.4M shares) | **~$0.05** |
| Price (1989-02-24) | **$46.56** |

Net working capital per share is about $0.05 against a price of $46.56. The company fails this test completely, and would fail it at almost any price.

**Why the framework doesn't stop at that result.** By the as-of date, the framework's own evidence has moved this test out of use for businesses like this one:
- "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price … In the interim, I searched for 'bargains' – and had the misfortune to find some" (`brk-letter-1987#18`).
- The standard has become "prices that will make sense, even should the future of the acquired enterprise develop much along the lines of its past" (`brk-letter-1981#3`).
- The yardstick for value has always been "value to a private owner" (`bpl-letter-1963#5`, `bpl-letter-1961#3`).
- The measure the framework defines for that purpose is **owner earnings** (`brk-letter-1986`, §3.3).

So the method below is: capitalize the owner earnings from Stage 2, ask what a private owner would pay, and test the result against the 1981 "future like the past" standard. Turning a stream of owner earnings into a value requires present-value arithmetic, which I show openly. The inputs come from the framework's own measures, not from a generic projection model.

## 5.2 Inputs

**(a) Core owner earnings, normalized for 1988**

| Step | $M |
|---|---|
| 1988 reported net income (`upi-1989-01-31`) | 1,044 |
| Less 1988 equity income (1987's $118.5M, down 57% per release) | (~51) |
| Core net income | ~993 |
| × owner-earnings ratio from Stage 2 (1987 core: ~$720M / ~$798M ≈ 0.90) | ~895 |
| Less ~7% currency haircut (10% weaker dollar on international, ~77% of soft-drink operating income) | (~60) |
| **Normalized core owner earnings** | **~$870M** |
| Shares outstanding, end-1988 (est.: 372.4 − 18.9 + ~1.3 options) | ~354.8M |
| **Per share (OE₀)** | **~$2.45** |

**(b) Reinvestment needed to grow.** Owner earnings deduct only *maintenance* capital spending, so growth has to be paid for out of them.
- From 1981 to 1988, net income rose about $560M. Over the same period, capital retained in the business plus added net debt came to roughly $1.2B, excluding buybacks, which shrink the share count rather than grow the business.
- That implies incremental returns of about 45%, flattered by currency and the tax cut.
- I use **40%**. Required reinvestment is then growth ÷ 0.40 of owner earnings, and only the remainder is counted as distributable.

**(c) Non-core assets and debt**
- *Equity stakes* (CCE, entertainment affiliate, Canadian bottler, others): market value "over $2.3 billion" at end-1987 (`ar-1987`). Allowing for the entertainment affiliate's 1988 write-downs, I use **~$2.1B**.
- *Net debt*: about $0.58B at end-1987. 1988 is not in the packet; after about $750M of 1988 buybacks I assume **~$0.8B**.
- Net adjustment: about **+$1.3B, or +$3.70 per share**.

**(d) Discount rate.** The framework gives none, and the packet contains no government bond yield.
- The company's own recent dollar notes carry 9⅞–11⅝% coupons.
- I assume a **9%** long-term government rate as the base.
- I also show **12%**, management's stated after-tax cost of capital (`ar-1987` MD&A), as a stress case.

## 5.3 Value per share

Each scenario uses a ten-year first stage, then a perpetual rate. Distributable owner earnings = OE₀ × (1 − g/0.40).

| Scenario | Growth (yrs 1–10 → after) | Distributable OE₀ | Value at 9% | Value at 12% |
|---|---|---|---|---|
| Stagnation: inflation-type growth only | 4% → 4% | $2.21 | **~$50** | ~$33 |
| Bear: growth halves from history | 6% → 3% | $2.08 | **~$51** | ~$36 |
| **Base: modestly below the past** | **10% → 4%** | **$1.84** | **~$73** | **~$44** |
| Management's guide ("mid-teens") | 15% → 4% | $1.53 | ~$103 | ~$59 |

All figures include the +$3.70 for equity stakes net of debt. The 12% column approximates management's cost of capital and serves as a stress test.

**Checking the base case against the 1981 standard.** Per-share earnings compounded about 11.7% a year from 1977 to 1988 ($0.84 → $2.85) and about 11.9% from 1981. The base case assumes 10% for ten years. That is below the past, so it satisfies "make sense even should the future … develop much along the lines of its past." Several things support the assumption:
- volume runway: international per-capita consumption is 16% of the US level;
- pricing power;
- market share gains in every year shown (Stage 2).

**Implied expectations.** At $46.56, the market is pricing the core business roughly as if it will grow at inflation-type rates forever. That is the stagnation case, for a business that has compounded at about 12% per share for eleven years.

## 5.4 Margin of safety

The framework sets no numeric hurdle. Its language is a "substantial excess of value [creating] a comfortable margin of safety" (`bpl-letter-1962#4`) and prices "well below per-share intrinsic business value" (`brk-letter-1984#4`). I apply two tests:
1. In the base case, the price should be no more than about two-thirds of value.
2. In the bear case, value should still be at least the price, so that a permanent loss of capital is unlikely (§9, `bpl-letter-1967-oct`).

| Test (9% rate) | Value | Price | Price / value | Margin |
|---|---|---|---|---|
| Base | ~$73 | $46.56 | 0.64 | **~36%** ✔ |
| Bear | ~$51 | $46.56 | 0.91 | ~9% ✔ (covered) |
| Stagnation | ~$50 | $46.56 | 0.93 | ~7% ✔ (covered) |

**At a 9% rate, both hurdles are met.** The downside is protected by the business itself rather than by its assets: even with no real growth, value roughly equals the price. The upside depends on the franchise continuing to compound, which Stage 2 judged highly probable.

**The result depends on the discount rate.** At 12%, the base case (~$44) is about equal to the price, and only management's growth guide gives a margin. Two things favour the 9% basis:
- the framework never uses a corporate "cost of capital";
- management's 12% includes a risk premium that the Stage 2 franchise evidence argues against for this business.

Still, the conclusion holds only if long government rates are near 9%. That rate is the most important missing figure.

**Summary:** this is not a "toad-like" price (`brk-letter-1981#3`). It is a sensible price for an outstanding business, about 16x reported 1988 EPS and about 19x normalized core owner earnings. That price still sits roughly a third below a conservative estimate of what a private owner should pay.

## 6. Catalyst / timing

- **No catalyst is required** (`brk-letter-1987`): "The market may ignore business success for a while, but eventually will confirm it." This is a "general," not a work-out. No sale, merger or tender is announced. Company buybacks (25.5M of the 40M-share programme done, ~14.5M left) are supportive, but the case doesn't rely on them.
- **Work-out** (`bpl-letter-1957`): does not apply.
- **Control** (`bpl-letter-1963`): not available at about $16.5B of market value. A large, passive "non-voting partnership" stake (`brk-letter-1981#3`) is the realistic form.
- **Mr. Market** (`brk-letter-1986`, `brk-letter-1987`):
  - The price is not a fear price today. The stock is near its 52-week high ($49.12) and up about 24% from mid-1988.
  - The fearful period was October 1987 to mid-1988: a $28.96 low and $35–40 at about 13x.
  - The framework forbids waiting on a market forecast (`bpl-letter-1966-mid`). The question is value against price, not timing.
  - Mr. Market is still pricing this franchise roughly as a no-growth business, and that pricing, not the recent move, is what matters.

## Missing figures the framework would want

1. **Long-term government bond yield** on the as-of date. This is the decisive input; I assumed 9%.
2. **1988 balance sheet and cash flow**: net debt, actual share count, capex, maintenance versus growth split.
3. **Constant-currency 1988 results**, to replace my ~7% haircut.
4. **Market values of the equity stakes after 1988**, particularly the entertainment affiliate after its write-downs.
5. **1988 buyback prices**, which show what management itself considered value.
6. **Inflation rate**, to separate real from nominal growth in both the history and the base case.

## Stage 4 conclusion

The company fails the framework's only formal valuation rule, net working capital, as any franchise business would. The framework has itself retired that rule for outstanding businesses.

On owner earnings at a 9% base rate, value is about $73 per share in the base case and about $50–51 in the stagnation and bear cases. Against $46.56, that is a ~36% margin of safety with the downside covered. The case does not need a catalyst.

The margin disappears at a 12% rate, so position size in Stage 5 should depend on how confident one can be that this franchise warrants a near-government-bond discount rate.