# Stage 4: Valuation (§5) and Catalyst / timing (§6), Coca-Cola as of 1989-02-27

**Price:** $46.56, the close on 1989-02-24 (`prices`).

**Share count:** about 355M. This is 372.36M at year-end 1987, less 18.9M bought back in 1988, plus about 1.3M of option exercises at the recent annual rate. The packet's $17.34B market value uses the stale 372M count. On 355M shares the market value is about **$16.5B**.

---

## 5. Valuation as the framework's section states it: buy below net working capital

The only valuation rule in the framework is the 1965 bargain test: what is the stock worth against "net working capital alone (before placing any value on the plants and equipment)" (`bpl-letter-1965`)? I apply it literally to the latest balance sheet in the packet, year-end 1987 (`ar-1987`).

| $M, 12/31/1987 | |
|---|---|
| Total current assets | 4,136.2 |
| Total current liabilities | (4,118.5) |
| **Net working capital** | **17.7**, about **$0.05/share** |
| Less long-term debt | (803.4) |
| Less deferred income taxes | (209.9) |
| **Current assets less all liabilities** | **–995.6**, negative |
| Book value per share | $8.66 |

At $46.56 the stock sells for about 930 times net working capital per share and 5.4 times book value. **Under the framework's stated valuation rule, Coca-Cola fails completely.** It is nowhere near a "generals"-type bargain.

**Why the analysis doesn't stop here.** By the as-of date, the investor's own writing says this test no longer applies to businesses like this one:
- "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… In the interim, I searched for 'bargains' – and had the misfortune to find some" (`brk-letter-1987#18`).
- "We may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting." Purchases should be "at prices that will make sense, even should the future of the acquired enterprise develop much along the lines of its past" (`brk-letter-1981#3`).
- Values are found in "fractional positions in companies with excellent business franchises and competent, honest managements" (`brk-letter-1981#3`).

These statements appear in the evidence passages, not in the framework's Valuation section, which contains only the net-working-capital rule. The test the framework's later writing implies is this: **does the price make sense if the future looks like the past, measured in owner earnings (§3)?** That is the calculation below. The decision should give weight to the fact that it relies on the evidence passages rather than on a rule the framework spells out.

---

## 5 (continued). Does the price make sense if the future looks like the past? An owner-earnings test

### Step 1: Owner earnings per share (from Stage 2, §3)

| Item | Basis | Per share |
|---|---|---|
| 1988 reported EPS | `upi-1989-01-31` | $2.85 |
| Owner earnings, base case (≈85% of reported) | 1987 owner earnings with maintenance capex ≈ depreciation (~$806M of $916M). Cross-check: 1985–87 the company paid out about 90% of earnings as dividends and buybacks with net debt roughly flat, after funding all capex and bottler investments | **≈ $2.42** |
| Owner earnings, conservative (all capex treated as maintenance) | Same ratio as 1987's $606M of $916M | ≈ $1.90 |
| Less distributed affiliate income, so affiliates are counted only once | 1988 equity income fell 57% (`upi-1989-01-31`); the distributed part is small | –$0.02 |
| **Core owner earnings used** | | **$2.40** |

The cash cross-check matters for growth. Because about 90% of earnings were distributed while the growth investments were still funded, $2.40 is roughly what owners can take out *after* paying for growth. That means growth in operating earnings can be applied to it without deducting growth capex a second time. To avoid counting the same dollars twice, I don't add any extra per-share growth from buybacks, since buybacks are paid out of this distributable cash.

### Step 2: Assets outside the core

| $M | Carrying value, 12/31/87 (`ar-1987`) |
|---|---|
| Columbia Pictures Entertainment (CPE, 49%) | 989.4 |
| Coca-Cola Enterprises (CCE, 49%) | 749.2 |
| T.C.C. Beverages (49%) | 84.5 |
| Other affiliates | 435.5 |
| **Total** | **2,258.6** |

The market value of the publicly traded investees was only $44M above their carrying value at year-end 1987. CPE took write-downs in 1988. The company also has $394M of contingent guarantees and is liable on $325M of CPE receivables sold with recourse. I therefore take about **$1.8B, or roughly $5 per share**. Net debt was about $0.4B, and interest on it is already deducted in earnings, so I make no separate adjustment for it.

**Price paid for the core:** $46.56 – $5 = **$41.56**, which is **17.3 times** core owner earnings, a **5.8% owner-earnings yield**.

### Step 3: What does "the future like the past" mean?

| Past measure | Figure | Source |
|---|---|---|
| EPS from continuing operations, 1981 to 1988 | $1.17 → $2.85, **13.6% a year** | `ar-1987`, `upi-1989-01-31` |
| Contribution from currency | Key currencies strengthened 27% (1986), 16% (1987), 10% (1988) | `ar-1986`, `ar-1987`, `upi-1989-01-31` |
| Currency-neutral growth in operating income | International: 1987 +25% reported, about 9% local; 1988 +21% reported, about 11% local. US: +10% (1987), +9% (1988) | same |
| Contribution from buybacks | Average shares 396M (1984) → ~365M (1988), about 2% a year | `ar-1987` |
| ROE 1988 / payout ratio | 33% / about 42% | `upi-1989-01-31`, `prices` |
| Remaining room to grow | International per-capita consumption is 16% of the US level | `ar-1986` |

With currency and buybacks removed, the business itself has grown operating earnings at about **10% a year**. Including the buyback effect, per-share growth has been about **12%**.

### Step 4: Value of the core per share, plus $5 for affiliates

I discount over two stages: 10 years at growth rate *g*, then 5% a year forever. The 5% terminal growth is conservative given the international runway.

**Discount rate.** The packet doesn't give a long-term government bond yield, which is what the investor would normally compare against. The only rate in the packet is **management's own 12% after-tax cost of capital** (`ar-1986`, `ar-1987`). I use 12% as the conservative anchor and show 10% as a sensitivity.

| Scenario | g for years 1–10 | Value at 12% | Price ÷ value | Value at 10% | Price ÷ value |
|---|---|---|---|---|---|
| Bear: the franchise matures now | 5% forever | $41 | 114% | $55 | 84% |
| Conservative: half the past rate | 8% | $50 | 93% | n/c | n/c |
| **Base: the past, currency-neutral** | **10%** | **$57** | **82%** | **$79** | **59%** |
| The past, including buyback effect | 12% | $65 | 72% | $92 | 51% |
| Management's guidance ("mid-teens") | 15% | $80 | 58% | n/c | n/c |

n/c = not calculated.

Example of the base case at 12%: the present value of 10 years of owner earnings growing from $2.40 is $21.76. Year-10 owner earnings are $6.23; the terminal value is $6.23 × 1.05 ÷ 0.07 = $93.4, worth $30.06 today. Core value is $51.8, plus $5 for affiliates, giving **about $57**.

### Step 5: Reverse test (what the price implies)

What permanent growth rate in owner earnings does $41.56 for the core imply at 12%?

$2.40 × (1 + g) ÷ (0.12 – g) = $41.56 → **g ≈ 5.9% a year forever**

The market is pricing the business as if growth drops at once to about half of its currency-neutral record and stays there permanently. That is despite ROE of about 30%, earnings retention of about 58%, and international consumption at one-sixth of US levels.

---

## Margin of safety against the hurdle

| Hurdle | Source | Result |
|---|---|---|
| **The framework's stated rule: buy below net working capital** | `bpl-letter-1965` | **Not met.** Net working capital is about $0.05/share against a $46.56 price. |
| **The later standard in the evidence: a sensible price that holds up if the future resembles the past** | `brk-letter-1981#3`, `brk-letter-1987#18` | **Met.** Value is about $57 at a punitive 12% with currency-neutral 10% growth, and about $65 at the 12% rate including buybacks. The price is 72–82% of value. |
| **A "comfortable margin of safety"** | `bpl-letter-1961#3`, `bpl-letter-1962#4` | **Moderate, not wide.** About 18–28% at 12%, about 40–50% at 10%. It depends on the discount rate, which the packet cannot pin down. It disappears only if growth falls to about 8% at the 12% rate. |

The margin of safety comes from the reliability of the business: a strong moat, a long record, and simple economics (Stages 2–3). It does not come from a statistical discount on the balance sheet. That fits the concentration standard of "an extremely high probability that our facts and reasoning are correct with a very low probability that anything could drastically change the underlying value" (`bpl-letter-1965`). I carry this into the sizing stage.

**Price context, not a forecast.** The stock is up about 33% from the 1988 lows ($35.04) and near the top of its 52-week range ($49.12). On the 1988 average price of about $39, the company's own buybacks were much cheaper than today's price. This doesn't affect the valuation, but it means Mr. Market is not offering a panic price now.

---

## 6. Catalyst and timing

- **No catalyst needed** (`brk-letter-1987`): "The market may ignore business success for a while, but eventually will confirm it." No catalyst is required here. The value comes from compounding owner earnings that grow in the low-to-mid teens. The buyback program, with about 14.5M of its 40M shares still to buy, adds to per-share value steadily, but it isn't a catalyst.
- **Work-outs** (`bpl-letter-1957`): not applicable. There is no pending merger, liquidation, tender or sale.
- **Controls** (`bpl-letter-1963`): not applicable. The company is worth $16.5B, is not neglected, and is not cheap enough for a controlling stake to be either possible or the point.
- **Mr. Market** (`brk-letter-1987`): "Mr. Market is there to serve you, not to guide you." The decision should rest on value against price, not on the stock's recent strength or weakness. The framework doesn't call for waiting for a lower price as a timing tool.

---

## Data the valuation needs that the packet doesn't have

1. **The long-term government bond yield on the as-of date.** This is the main gap. The value ranges from about $57 to about $79 depending on whether the discount rate is 12% or 10%.
2. **The 1988 cash flow statement and capex,** to confirm the $2.40 owner-earnings base, which is currently extrapolated from 1987.
3. **Currency-neutral volume and price data,** to confirm the 10% growth figure.
4. **CPE's market value after its 1988 write-downs,** and the current market value of the CCE stake. The latest per-share figure for CCE is $14.25 at year-end 1986.
5. **The exact share count on the as-of date** and the dollar amount of 1988 buybacks.

---

## Conclusion for Stage 4

Under the framework's literal valuation rule (buy below net working capital), **Coca-Cola is a pass**. Under the standard the investor had adopted by this date (an outstanding business at a price that makes sense if the future resembles the past), it **qualifies**.

- Core owner earnings: about $2.40/share.
- Intrinsic value: about **$57–65 per share** at management's conservative 12% discount rate, and about $79–92 at 10%. Price is $46.56.
- Margin of safety: about **18–28%** on conservative assumptions.
- The price implies only about 6% permanent growth for a business that has grown about 10% a year in local currency and about 12% per share.
- No catalyst is needed.

Two things carry forward to the sizing stage: the margin depends on a discount rate the packet can't fix, and the buy case rests on the investor's later principle rather than on the framework's stated valuation rule.