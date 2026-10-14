---
id: thaler-2015-misbehaving/ch26-fruit
work: thaler-2015-misbehaving
unit: "26. Fruit Flies, Icebergs, and Negative Stock Prices"
pages: 199-208
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Fruit Flies, Icebergs, and Negative Stock Prices

## L0 — One line
Clear violations of the law of one price (identical assets should sell at the same price), such as 3Com/Palm and Royal Dutch/Shell, show that prices can be wrong and stay wrong, because noise traders (irrational buyers) exist and smart money (informed arbitrageurs) faces limits, so policy-makers should not assume prices are always right.

## L1 — The gist (≤ 120 words)
Can markets get simple arithmetic right? After Palm's 2000 IPO, the market priced the rest of 3Com at about minus $23 billion, which is impossible for a limited-liability stock. Thaler argues that such a mispricing needs noise traders (irrational buyers) plus obstacles for smart traders (here, scarce shares to short). Royal Dutch/Shell and the hedge fund LTCM show that smart traders can also be ruined while prices stay wrong. He splits the efficient market hypothesis (EMH): "no free lunch" is mostly true, "price is right" (price equals value) is much weaker. Wrong prices cause misallocation, as in the housing boom, so policy-makers may sensibly lean against bubbles.

**Prerequisites:** what a stock, a short sale and an IPO are; the idea of arbitrage (riskless profit from price gaps); the EMH in outline.

## L2 — Key ideas (5–10 bullets)
- The law of one price says 3Com's price should equal 1.5 × Palm's price plus a non-negative stub value. In March 2000 the implied stub was −$61 per share (p. 201–202).
- Two ingredients are necessary for such a violation to persist: noise traders and a barrier to smart-money correction. For Palm the barrier was too few Palm shares to borrow (p. 203).
- Royal Dutch/Shell: the gap from the 1.5 ratio could and did last for decades. Arbitrageurs such as LTCM were hurt when the spread widened (p. 204).
- Limits of arbitrage: when prices move against a manager and investors withdraw money, a vicious spiral can follow (p. 204).
- Fama saw these cases as too small to matter. Thaler calls them finance's "fruit flies", where intrinsic value can be bounded (p. 205).
- Descriptive EMH has two parts: "no free lunch" is "mostly true", while "price is right" gets a much lower opinion (p. 206).
- Wrong prices can misallocate resources (housing boom, liar loans), so leaning against the wind can make sense (p. 207).

## L3 — Walkthrough

### The 3Com/Palm carve-out (pp. 199–201)
- Thaler returned to the law of one price with Owen Lamont (p. 199). 3Com (networking, plus Palm via a merger) had a flat share price in summer 1999 while tech stocks soared (pp. 199–200).
- On March 2, 2000, 3Com sold part of Palm to the public in an **equity carve-out**: about 4% in the IPO, about 1% to a consortium, and 95% retained (p. 200).
- Even the split puzzles EMH advocates. With Econs (fully rational agents), the value of 3Com would equal Palm plus the rest of 3Com, so a split should change nothing (p. 200).
- Yet 3Com rose from about $40 (announcement, Dec 13, 1999) to over $100 by the IPO (p. 200).
- The plan: after a few months each 3Com shareholder would get 1.5 Palm shares. A 3Com share therefore contains 1.5 Palm shares plus the "stub value" (the rest of 3Com). Rationally:
$$P_{3Com} = 1.5\,P_{Palm} + s$$ (Figure 16, p. 202; text p. 201)
- Palm was priced at $38 in the IPO and closed its first day at a bit over $95. 1.5 × $95 is about $143, and 3Com's remaining business was profitable, so 3Com should have closed at $143 or more (p. 201).
- Instead 3Com closed at $82. Solving gives $s = 82 - 143 \approx -61$ per share, about −$23 billion in total (pp. 201–202). Figure 16 prints $82 = $95 × 1.5 + (−$61).
- A stock price cannot be negative, since shares can be thrown away and liability is limited. Buying 3Com at $82 also beat buying Palm at $95 directly (p. 202). The stub stayed negative for several months despite press coverage (p. 202).

*Intuition note:* Buying 3Com gave you more Palm shares for less money, plus a free business. A negative price for that business is impossible, so the market's arithmetic was wrong.

### Why it persisted; other cases (pp. 203–205)
- Two necessary ingredients (p. 203):
  1. Noise traders ("Summers's IDIOTS") who want pure Palm. Even buyers who know Palm is overvalued need such people to sell to later.
  2. Something that stops smart money. The smart trade is to buy 3Com and short Palm, then repay the loan with the Palm shares received. This leaves the 3Com stub value as profit, "a trade that cannot lose". But too few Palm shares were sold to lend to everyone wanting to borrow (p. 203).
- Footnote: a Chicago PhD student made tens of thousands of dollars, not tens of millions, by borrowing Palm shares from many brokers (p. 208).
- Other cases: in 1923 Graham bought DuPont and shorted GM, since DuPont's stub was near zero (p. 203). Yahoo/Alibaba in mid-2014 was similar (footnote, p. 208).
- **Royal Dutch Shell:** the 1907 merger gave 60% of profits to Royal Dutch holders and 40% to Shell holders, so the price ratio should be 1.5. Royal Dutch traded up to 30% too low and sometimes 15% too high (pp. 203–204).
- Both shares were widely traded and easy to borrow, and nothing prevented the trade. The gap lasted decades, so waiting is risky (p. 204).
- LTCM shorted the expensive Royal Dutch and bought cheap Shell. In August 1998 (Asia, Russian default) it and other hedge funds had to unwind, and the spread widened against them. LTCM collapsed within weeks, also from other trades that "got worse before they got better" (p. 204).
- Shleifer and Vishny (1997) had described such a spiral as the "limits of arbitrage": losses prompt withdrawals, which push prices further against the manager (p. 204). Lesson: smart money cannot always set prices right (p. 204).
- Footnote: a pension fund CEO insisted smart money would buy the cheaper share, yet his fund held the pricier Dutch share via an S&P 500 index (p. 208).

*Intuition note:* In the Royal Dutch/Shell case the gap could widen before it closed. An arbitrageur forced to exit early, as LTCM was, could lose on a trade that would have paid if held to the end (our reading of p. 204).

### Fruit flies and icebergs (pp. 205–206)
- Fama said closed-end funds and Palm/3Com are minor assets, so the stakes are too small (p. 205).
- Thaler: these are finance's fruit flies, rare cases where intrinsic value can be bounded. No one knows the right price of Palm, but 3Com had to be at least 1.5 × Palm (p. 205).
- He called them the tip of the iceberg. Fama's view, in Thaler's words, was that "we had beheld the entire iceberg" (p. 205).
- If the law of one price can be violated in such obvious cases, Thaler says it is "abundantly clear" that even greater disparities can occur for the overall market. Nobody could prove the Internet bubble then or now, but the NASDAQ could be overpriced as well. It does not seem to him a coincidence that the expensive part of the trade was the sexy Palm division (p. 205).

### Verdict on the EMH (pp. 205–207)
- As a normative benchmark the EMH has been extraordinarily useful. In a world of Econs Thaler believes it would be true. Behavioral finance needs it as a starting point, and no benchmark behavioral theory of prices exists yet (pp. 205–206).
- As a description: "no free lunch" is "mostly true". Markets over- and underreact, but most active managers fail to beat the market. Even when investors know prices are wrong, the prices can stay wrong or get more wrong, which should scare would-be exploiters. Making money is possible but not easy. Investors who accept the EMH and buy low-cost index funds "cannot be faulted" (p. 206).
- "Price is right": much lower opinion. Fischer Black wrote that "we might define" an efficient market as price within a factor of 2 of value (he calls the factor arbitrary). He thought almost all markets are efficient almost all of the time, with "almost all" meaning at least 90% (p. 206).
- Thaler finds a factor of 2 very wide. He thinks Black, who died in 1996 before the technology and real estate bubbles, could be convinced to revise it to "right within a factor of 3" (pp. 206–207). The NASDAQ lost over two-thirds of its value between 2000 and 2002 (p. 207).

### Policy lessons (p. 207)
- Conclusion: price is often wrong, sometimes very wrong, and misallocation can be big (p. 207).
- Regions with the fastest price rises and high price-to-rent ratios had the most optimistic price expectations in Shiller's surveys. Rational lenders would have tightened mortgage terms but instead offered low down payments and "liar loans" (p. 207).
- If policy-makers simply take it as a matter of faith that prices are always right, they will never see any need for preventive action. Once bubbles are granted to be possible and the private sector appears to be feeding the frenzy, it can make sense to lean against the wind (p. 207).
- Thaler calls it irrational to complain about extraordinary recovery measures while opposing minor steps to reduce the chance of another crisis (p. 207).
- Footnote disclosure: Thaler is a partner in Fuller and Thaler Asset Management, which looks for mispricing from behavioral biases. Its survival suggests skill, luck, or both (p. 208).

## Toy example (ours)
Firm A owns 2 shares of firm B per A share. Law of one price: $P_A = 2P_B + s$, with $s \ge 0$.
- Suppose $P_B = \$10$ and $P_A = \$18$. Then $s = 18 - 2(10) = -\$2$, which is impossible.
- Trade: buy 1 A for $18; short 2 B and receive $2 × 10 = $20. Net cash is +$2.
- At the distribution, A's holder receives 2 B and returns them to close the short. What remains is the true stub, worth $s^* \ge 0$. Total gain is $2 + s^* \ge \$2$, if held to the end.
- Limit: if B rises to $12 and A stays at $18 meanwhile, the short shows a paper loss of $2 × (12 − 10) = \$4$. A forced exit then turns the sure gain into a loss.

## Concepts
- [[law-of-one-price]] (new) — identical assets should sell at the same price; here, 3Com's price ≥ 1.5 × Palm's (p. 199, 201)
- [[stub-value]] (new) — value of a parent firm after subtracting its stake in a subsidiary (p. 201)
- [[equity-carve-out]] (new) — a parent sells a fraction of a subsidiary to the public (here about 5% of Palm) (p. 200)
- [[noise-traders]] — investors with an inexplicable desire to own an overpriced asset (a.k.a. "Summers's IDIOTS") (p. 203)
- [[limits-to-arbitrage]] — prices can stay wrong or worsen; smart money cannot always correct them (p. 204)
- [[short-selling]] (new) — borrow shares, sell them, and repay later; here the borrowable supply was too small (p. 203)
- [[efficient-market-hypothesis]] — Thaler splits it into "no free lunch" and "price is right" (p. 206)
- [[finance-fruit-flies]] (new) — rare clean cases in which intrinsic-value bounds can be tested (p. 205)

## Canonical instances
- [[3com-palm-1999-2000]] — negative implied stub of −$23 billion (pp. 201–202)
- [[royal-dutch-shell-ratio]] — 60/40 split; ratio deviated for decades (pp. 203–204)
- [[ltcm-1998]] — arbitrageur collapses when spreads widen (p. 204)
- [[dupont-gm-1923]] — Graham's near-zero stub trade (p. 203)
- [[us-housing-bubble-liar-loans]] — optimistic expectations and lax lending (p. 207)

## Bridges (candidates)
- [structural-analogy] Stub-value bound ↔ no-arbitrage & risk-neutral pricing: a price bound follows from a hedging argument, not beliefs about returns.
- [structural-analogy] Withdrawals forcing sales that push prices further against the fund ↔ debt deflation: forced selling feeds further price falls.
- [metaphor] Fruit flies as simple model organisms ↔ natural experiments for testing otherwise untestable ideas.

## Questions this raises
- If the Palm trade was riskless to completion, why did no large fund close the gap? Is the short-supply explanation enough?
- Is a "factor of 2" or "factor of 3" band a meaningful definition of efficiency, or is it too loose to test?
- Can one use fruit-fly cases to estimate how far whole-market mispricing goes?

## Reading notes
- Printed page = pdf − 41 (pdf 240 = p. 199).
- The text gives March 2, 2000 for the carve-out sale (p. 200) and March 1, 2000 for the IPO (p. 200); the two dates are not reconciled.
- p. 203 says "the supply of shares to lend exceeded the demand from people who wanted to borrow them". The preceding sentence ("not enough to satisfy everyone who wanted to borrow") says the opposite, so this is probably a slip. I followed the context.
- Figure 16 (p. 202) prints $s = -\$61$; exactly $82 - 142.5 = -60.5$, so the −$61 is rounded.
- Closed-end funds and the Miller debate are only mentioned (pp. 199, 205) and are not explained in this unit.
