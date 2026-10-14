# Stage 4: Valuation (§5) and Catalyst/Timing (§6)

---

## Step 1: Apply the framework's stated valuation rule (§5: "buy below net working capital")

§5 contains one rule, the Partnership-era net-working-capital bargain test (`bpl-letter-1965`). Applied to the latest balance sheet in the packet (31 Dec 1987, `ar-1987`):

| Item | $M |
|---|---|
| Total current assets | 4,136.2 |
| Total current liabilities | (4,118.5) |
| **Net working capital** | **≈ 17.7** |
| Per share (≈ 372M) | **≈ $0.05** |

The figure is still tiny if I adjust for the $335M in-kind dividend payable, since that removes an asset of equal size. Price is $46.56. Book value is $8.66 a share, so price is roughly 5.4x book. **The NWC rule fails completely**, and the stock would never pass the quantitative screen in §1 (`bpl-letter-1963`).

**Why this is not where the analysis ends.** The framework's own later rules, in force at the as-of date, say this is the wrong test for this kind of business:
- "the same energies and talent are much better employed in a good business purchased at a fair price than in a poor business purchased at a bargain price" (`brk-letter-1979`, §2)
- "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… I searched for 'bargains' — and had the misfortune to find some" (`brk-letter-1987#18`)
- "We may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting… prices that will make sense, even should the future of the acquired enterprise develop much along the lines of its past" (`brk-letter-1981#3`)
- If you pay six times book for a high-return business, "that does not change [its] return on equity" (`brk-letter-1987#1`).

For an outstanding franchise at this date, the framework therefore judges price against **owner earnings** (§3), using the 1981 standard: does the price make sense if the future looks much like the past? The margin-of-safety idea carries over from the Partnership letters: "This substantial excess of value creates a comfortable margin of safety" (`bpl-letter-1961#3`, `bpl-letter-1962#4`). The framework gives **no numeric discount rate and no numeric margin-of-safety percentage** for franchise businesses. I state my assumptions where I need them.

---

## Step 2: Inputs

| Input | Value | Source / basis |
|---|---|---|
| Price, 24 Feb 1989 | **$46.56** | `prices` |
| Shares outstanding | **≈ 355M** | 372.4M at end-1987, less 18.9M bought back in 1988, plus about 1.3M from options (my estimate; the packet's 372M count is stale) |
| Market value | **≈ $16.5B** | 46.56 × 355M |
| 1988 reported EPS | $2.85 (P/E 16.3x) | `upi-1989-01-31` |
| 1988 owner earnings per share | **≈ $2.30–2.70, midpoint $2.50** | Stage 2 estimate. The 1988 cash-flow statement is not in the packet |
| Equity investments (CPE net of distributed shares ≈ $654M, CCE $749M, Canadian bottler $84M, other $435M) | ≈ $1.9B carrying at end-1987; I use $1.5–2.0B given CPE's 1988 write-downs | `ar-1987`; public investees traded about $44M above carrying value |
| Net debt | ≈ $0.6B at end-1987 (15.3% of capital); I assume $0.6–1.0B after 1988's ~$750M of buybacks | `ar-1987`; 1988 balance sheet missing |
| Non-core net assets per share | **≈ +$2–3** (investments less net debt) | Derived. Separately, $394M of contingent guarantees is noted |

Owner earnings already exclude undistributed equity income. The affiliates are therefore counted once, as assets at about carrying value, and not again through earnings.

---

## Step 3: What return does the price imply if the future looks like the past?

The core business needs little capital (Stage 2). Owner earnings are therefore roughly *all distributable*, through dividends ($1.20 a share in 1988) plus buybacks. A buyer's long-run return is then approximately:

**owner-earnings yield + growth in owner earnings, ± any change in the valuation multiple**

- Owner-earnings yield at $46.56: 2.30 to 2.70 ÷ 46.56 = **4.9–5.8%, midpoint 5.4%**. Reported earnings yield is 6.1%.
- **How fast has it grown? ("along the lines of its past")**
  - Company-level net income went from $432M (1981) to $1,040M (1988), about 13.4% a year.
  - Unit volume grew 6–10% a year, and margins widened.
  - Part of that growth was currency translation (key currencies rose against the dollar by 27%, 16% and 10% in 1986–88) and part was acquisitions.
  - Size will slow growth over time, a point `brk-letter-1983#0` makes about Berkshire itself.
  - I use **8% as the conservative case, 10–12% as the central case and 15% as the optimistic case**, applied to underlying business growth before buybacks.

| Growth (10 yrs) | Multiple holds (≈ 18.6x owner earnings) | Multiple falls to 10x by year 10 (the 1981 level, ≈ –6%/yr drag) |
|---|---|---|
| 8% | ≈ 13% / yr | ≈ 7% / yr |
| 12% | ≈ 17% / yr | ≈ 11% / yr |
| 15% | ≈ 20% / yr | ≈ 14% / yr |

Even with the multiple falling back to the roughly 10x the market paid for this franchise in 1981, the central case returns about 11% a year. At unchanged multiples, returns run in the high teens. That is comfortably above the "average large American corporation" yardstick in `brk-letter-1983#0`.

---

## Step 4: Intrinsic value range (owner earnings capitalized)

To turn the return test into a value, I need a discount rate. **The packet and framework give none.** The long Treasury yield, the natural yardstick, is missing. As a stand-in I use the company's own stated **12% after-tax cost of capital** (`ar-1986`, `ar-1987`) and show 10% for sensitivity. The method is to grow owner earnings for 10 years at g, then at 5% a year forever, and add about $2.50 a share of non-core net assets.

| g (yrs 1–10) | Value at 12% | Margin vs $46.56 | Value at 10% | Margin vs $46.56 |
|---|---|---|---|---|
| 8% (conservative) | ≈ $49 | ≈ 5% | ≈ $69 | ≈ 32% |
| 10% | ≈ $56 | ≈ 18% | — | — |
| 12% (central) | ≈ $65 | ≈ 28% | ≈ $93 | ≈ 50% |
| 15% (optimistic) | ≈ $80 | ≈ 42% | — | — |

**Working for the central case (12% discount, 12% growth).** Each year's owner earnings have a present value of about $2.50, so ten years total $25.0. Owner earnings in year 11 are about $8.15. Capitalized at 7% (12% minus 5%) that gives $116, worth $37.5 today. Adding $2.5 of non-core assets gives about **$65**.

**Central intrinsic value: about $55–65 a share at a 12% discount rate**, and well above that if the right discount rate is nearer 10%.

---

## Step 5: Margin of safety against the framework's hurdle

The framework sets two standards:

1. **The 1981 standard, "prices that will make sense even should the future develop much along the lines of its past."** **Passes.** If owner earnings keep growing at anything near the 1981–88 rate of about 13%, value is $65–80 against a price of $46.56.
2. **The Partnership standard, "substantial excess of value" giving "a comfortable margin of safety."** **Passes in the central case, about 18–28% below value. It is roughly at fair value in the conservative case at 12%.** The margin is moderate, not large. The protection comes mainly from the quality of the business, not from a cheap price. That fits the framework's own view that low "probability that anything could drastically change the underlying value" matters as much as the discount (`bpl-letter-1965`, §7).

**Considerations that cut against a large margin:**
- The P/E has already risen from about 10x (1981) to 16x. Part of the easy re-rating is gone.
- The stock is near its 52-week high of $49.12, up about 24% in twelve months and about 60% above the October 1987 low of $29. Mr. Market offered much better prices sixteen months ago. "Be fearful when others are greedy" (`brk-letter-1986`) argues for discipline on price, though the packet shows no sign of general euphoria around this stock.
- Some recent growth is currency translation that can reverse.

**Considerations that support it:**
- Pricing power and low capital needs make this one of the few businesses that can protect owners' real returns against inflation. The framework treats that as decisive (`fortune-1977-inflation`, `brk-letter-1979#2`).
- The core castle earns very high returns on its own capital, and the long international runway (per-capita consumption at 16% of the U.S. rate) supports the central growth case.

**Overall: an outstanding business at a sensible price. This is fair-to-attractive, not a bargain.** The margin is about 20–30% in the central case and thin in the conservative case.

---

## Step 6: Catalyst / timing (§6)

- **No catalyst needed** (`brk-letter-1987`: "The market may ignore business success for a while, but eventually will confirm it"). This would be a general purchase held for business growth. The return is driven by owner earnings compounding at 10%-plus, not by a re-rating event.
- **Work-out (`bpl-letter-1957`): not applicable.** No sale, merger, liquidation or tender is pending. The CPE distribution is complete. The ongoing buyback (about 14.5M shares left in the 40M program) is a mild support. It also competes with any buyer for stock, while raising a holder's percentage ownership over time.
- **Control (`bpl-letter-1963`): not applicable.** At about $16.5B the company cannot be controlled, and "We will not engage in unfriendly takeovers" (`brk-letter-1986#10`). Any stake would be a "non-voting partnership" of the kind `brk-letter-1981#3` describes.
- **Timing: no market forecast** (`bpl-letter-1966-mid`; `fortune-1977-inflation`: "Forecasts usually tell us more of the forecaster than of the future"). The decision rests on price against value today. Mr. Market "is there to serve you, not to guide you" (`brk-letter-1987`). If the price fell back toward the 1988 range of $35–39, the margin would widen to about 35–45% and the case for buying more would strengthen.

---

## Facts the framework would want that the packet lacks

1. **Long-term government bond yield**, the opportunity-cost yardstick needed to pick the discount rate. The single biggest missing input; values swing about 40% between 10% and 12%.
2. **1988 balance sheet and cash-flow statement**: net debt, the investment carrying values after the CPE write-downs, capex and depreciation, all needed to firm up 1988 owner earnings.
3. **Current market values of CCE, CPE and the Canadian bottler stakes** at the as-of date.
4. **Split of capex between maintenance and growth.**
5. **Trading volume** and the size of a position that could be built without moving the price. At 5% ownership, a stake would cost about $0.8B.

---

## Stage 4 conclusion

- **§5 NWC test:** fails. NWC is about $0.05 a share against a price of $46.56. Under the framework's own later rules (`brk-letter-1979`, `brk-letter-1981#3`, `brk-letter-1987#18`) this test is superseded for an outstanding franchise.
- **Owner-earnings valuation:** about 5.4% owner-earnings yield on a business that grows owner earnings at an estimated 10–13% while needing little capital. Implied returns are about 11–17% a year, and about 7% even in the conservative case with the multiple falling back to 10x. **Intrinsic value is about $55–65 a share** at the company's own 12% cost of capital, more at lower discount rates.
- **Margin of safety:** about 18–28% in the central case, thin in the conservative case. **It passes the framework's "sensible price for an outstanding business" standard; it is not a deep-discount bargain.**
- **§6:** no catalyst is needed and none exists. This is a long-term general holding with no market timing. A pullback would widen the margin and warrant buying more.