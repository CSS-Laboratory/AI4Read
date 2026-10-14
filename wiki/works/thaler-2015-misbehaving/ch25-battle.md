---
id: thaler-2015-misbehaving/ch25-battle
work: thaler-2015-misbehaving
unit: "25. The Battle of Closed-End Funds"
pages: 192-198
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Battle of Closed-End Funds

## L0 — One line
Closed-end funds that trade away from their net asset value break the law of one price, and Thaler and co-authors argue that the shifting "investor sentiment" of individual (noise-trading) investors helps explain why the discounts vary; Merton Miller attacked the paper.

## L1 — The gist (≤ 120 words)
Can we show that stock prices are wrong when intrinsic value is hard to measure? Thaler uses the law of one price, a core principle of the efficient market hypothesis (EMH). A closed-end fund holds assets, yet its shares usually sell at a discount to the value of those assets, and sometimes at a premium. The authors list four puzzles. They postulate that individual investors act as noise traders (who react to non-news) and conjecture that shifting sentiment moves the discounts. The average discount was correlated with the small-minus-large stock return difference. Merton Miller attacked the paper, which led to a four-part published exchange. Both sides claimed victory, and the fight drew attention to the paper.

**Prerequisites:** arbitrage (riskless profit from price gaps); what a mutual fund is; correlation; the EMH idea that prices reflect value.

## L2 — Key ideas
- The law of one price says an efficient market cannot price the same asset two ways, because arbitrage would remove the gap. A violation would hit a core EMH tenet (pp. 192–193).
- The EMH predicts that closed-end fund shares trade at net asset value (NAV, the value of the fund's underlying assets). Fund tables show that funds typically sell at discounts, often 10–20% below NAV, and sometimes at premia (p. 194).
- Four puzzles: overpaying at issue, the existence of discounts, their variation, and convergence to NAV when a fund converts to open-end (pp. 195–196).
- Variation in the discounts rules out many simple explanations, such as fees or mismanagement. Convergence to NAV rules out a miscalculated NAV (p. 196).
- The authors' hypothesis: individual investors are noise traders (they react to things that are not real news) with changing "investor sentiment", and discounts shrink when they feel optimistic (p. 196).
- Evidence: the average discount was correlated with the return gap between small and large firms (p. 197).
- Miller's published comment, the authors' reply, and further replies made a four-part exchange. Thaler says it drew a lot of attention to the paper (pp. 197–198).

## L3 — Walkthrough

### Opening: the 1988 Chicago panel (p. 192)
- Shiller's work hurt the "price-is-right" part of the EMH, but it was not considered a fatal attack. Methodology disputes remained, and EMH advocates would not rule out a rational explanation of October 1987 (p. 192).
- **Fama's view:** the market deserves congratulation for reaching its new equilibrium quickly. Thaler reports Fama as meaning that something must have happened to make people revise down their estimates of future returns, and prices adjusted immediately (p. 192).
- Thaler asked whether the present value of dividends had fallen 20% on Black Monday. Few hands went up. Fama raised his hand, smiling, though he had not conceded (p. 192).
- Intrinsic value cannot be determined with precision, which makes it hard to prove that prices deviate from it. One possible approach to testing whether prices are "right" is the law of one price (p. 192).

### The law of one price and closed-end funds (pp. 192–194)
- **Law of one price:** in an efficient market the same asset cannot sell at two prices at once. Otherwise there is an **arbitrage opportunity**, a series of trades with a guaranteed riskless profit (pp. 192–193).
- Example: gold at $1,000 in New York and $1,010 in London. Buy in New York, sell in London, and if transaction costs are small, profit continues until prices converge. Many alert traders should make the law hold "almost precisely and instantaneously" (p. 193).
- **Open-end fund:** investors can add or withdraw money at any time, at a price set by the **Net Asset Value (NAV)**, the value of the fund's assets. Example: Apple at $100, $1,000 invested buys ten fund shares. If Apple doubles to $200, cashing out returns $2,000, less fees (p. 193).
- **Closed-end fund:** managers raise a fixed sum (say $100 million). No money can be added or withdrawn. Investors sell their shares at the fund's market price (p. 193).
- If an Apple closed-end fund (one share = one Apple share) traded at anything other than Apple's price, Apple would be available at two prices, violating the law of one price (pp. 193–194).
- **EMH prediction:** price = NAV. Tables (figure 15) show price, NAV and premium or discount. Funds typically sell at 10–20% discounts but sometimes at premia (p. 194).
- Figure 15 (as of Dec. 31, 2014): Gabelli Utility Trust NAV $6.28, price $7.42, +18.2%. Firsthand Technology Value NAV $29.70, price $18.59, −37.4% (p. 194).

*Intuition note:* A closed-end fund is a box of stocks whose shares you can buy and sell. If the box is worth less than its contents, the same assets have two prices. The EMH says this should not persist, yet it appears in a published table (p. 194).

### The research project (pp. 195–196)
- Charles Lee, a Cornell accounting PhD student, did a course project on closed-end funds. Around then Larry Summers and former students wrote about "noise traders" (p. 195).
- Fischer Black made "noise" a technical term in finance, as a contrast to "news". A **noise trader** decides on SIFs, not real news. SIFs are not defined in these pages (p. 195).
- De Long, Shleifer, Waldmann and Summers built a model using closed-end funds as an example, without empirical tests; Summers also had an unpublished solo paper that opens "THERE ARE IDIOTS. Look around." Lee, Shleifer and Thaler then wrote the empirical paper (p. 195).
- **Four puzzles:**
  1. Funds are sold with a commission of about 7%, but within six months they typically trade at a discount above 10%. Why pay $107 for something predictably worth $90? Thaler says Graham called funds "an expensive monument erected to the inertia and stupidity of stockholders." Thaler calls "THERE ARE IDIOTS" the only satisfactory answer (p. 195).
  2. Discounts and premia exist at all (p. 196).
  3. They vary across time and funds. This rules out many simple explanations, such as discounts compensating for fees or mismanagement, since neither varies much over time (p. 196).
  4. When a discounted fund converts to open-end, its price converges to NAV. So NAV was not miscalculated (p. 196).
- Footnote: buying at a discount can be smart, but buying at issue with a commission is foolish (p. 198).

### The sentiment hypothesis and evidence (pp. 196–197)
- U.S. closed-end funds are mainly held by individuals, not institutions. The authors postulated that individuals are the noise traders. They are flightier, with moods of optimism or pessimism called **investor sentiment**, an example of "animal spirits" (p. 196).
- **Conjecture:** the discounts shrink when individuals feel "perky" and grow when they are depressed or scared (p. 196).
- **Measurement:** individuals hold small-company shares more than institutions do. Institutions avoid small stocks because of low liquidity. Funds avoid closed-end funds because customers dislike paying two sets of fees (pp. 196–197).
- So sentiment should show up both in discounts and in small-versus-large relative returns. Small firms do better on average, but not in every period (p. 197).
- **Finding:** the average discount was correlated with the return difference between small and large stocks. The greater the discount, the larger the difference (p. 197).

*Intuition note:* If one group of investors moves both fund prices and small-stock prices, the two should move together. The authors found this co-movement. Thaler compares the finding to finding footprints for Bigfoot, a creature thought to be a myth (p. 197).

### The Miller dispute (pp. 197–198)
- Thompson found that buying the biggest-discount funds earned superior returns. Graham and Burton Malkiel also advocated this strategy (p. 197).
- Miller was infuriated. **Thaler's guess:** the authors skipped the usual apologies for anomalies, and used one anomaly (the small firm effect) to explain another (p. 197).
- Miller lobbied editor René Stulz to reject the paper. Stulz accepted it and told Miller to write a comment (p. 197).
- Miller, Nai-fu Chen and Raymond Kan wrote that Lee et al. "can't" kill two puzzles with one stone (p. 198).
- Lee et al. replied with new data, which Miller saw as a protocol violation. Miller insisted on a reply to the reply, which, by tradition, meant the original authors got the last word. Both sides declared victory (p. 198).
- Thaler's conclusion: the four-part exchange drew hundreds of financial economists to the paper, so Miller ended up "doing us a big favor" (p. 198).

## Toy example (ours)
A closed-end fund holds one share of stock X per fund share. X trades at $100, so NAV = $100.
- Market price $85: discount = (85 − 100)/100 = −15%.
- If the fund converts to open-end and price converges to NAV, a buyer at $85 gains (100 − 85)/85 ≈ 17.6%.
- Puzzle 1 pattern (our numbers): pay $107 at issue, a 7% commission over NAV $100. Six months later the price is at a 10% discount to a NAV still at $100, so $90. The loss is (107 − 90)/107 ≈ 15.9%.

Both cases show the same asset priced two ways.

## Concepts
- [[law-of-one-price]] (new) — the same asset cannot sell at two prices at once in an efficient market (p. 192)
- [[arbitrage]] (new) — trades guaranteed to give a riskless profit (pp. 192–193)
- [[closed-end-fund-puzzle]] (new) — funds trade at discounts or premia to NAV, with four associated puzzles (pp. 194–196)
- [[net-asset-value]] (new) — the value of a fund's underlying assets (p. 193)
- [[noise traders]] — traders who act on noise rather than news (Black, Summers) (p. 195)
- [[investor-sentiment]] (new) — shifting optimism or pessimism of individual investors (p. 196)
- [[animal spirits]] — investor sentiment is called an example of them (p. 196)
- [[efficient market hypothesis (weak/semi-strong/strong)]] — here the price-is-right part and the law of one price (pp. 192–194)

## Canonical instances
- [[closed-end-fund-discounts]] (new) — a clear visible violation of the law of one price (p. 194)
- [[black-monday-panel]] (new) — Fama says the market adjusted quickly; Thaler asks whether dividend present value fell 20% (p. 192)
- [[lee-shleifer-thaler-1991]] (new) — discounts linked to the small-versus-large return gap (p. 197)

## Bridges (candidates)
- [structural-analogy] law of one price ↔ economics-finance: no-arbitrage pricing — both rest on price gaps for the same payoff being eliminated by traders.
- [structural-analogy] investor sentiment as shared mood ↔ economics-finance: narrative contagion — both link group moods to prices (not stated here).
- [metaphor] Miller–Thaler exchange ↔ scientific debate as attention market — the fight drew readers to the paper.

## Questions this raises
- Why do arbitrageurs not eliminate the discount if the fund's assets can be priced? (The text does not say.)
- Does a correlation with small-minus-large returns rule out rational explanations?
- If buying biggest-discount funds earns superior returns, why do the discounts persist?
- How would one measure investor sentiment other than by discounts?

## Reading notes
- Printed page = pdf page − 41.
- Figure 15 was read from the page image; the percentages match the NAV and price columns to within rounding (DNP: 10.55 vs 10.50 gives about +0.5%, printed +0.4).
- The text layer is clean except that Figure 15's table is only in the image. "SIFs" is used on p. 195 without definition in these pages.
- Footnotes appear on p. 198: Black's handwritten "noise traders" comment, and the point about buying at a discount versus at issue.
