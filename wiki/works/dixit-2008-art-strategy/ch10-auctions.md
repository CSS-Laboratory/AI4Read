---
id: dixit-2008-art-strategy/ch10-auctions
work: dixit-2008-art-strategy
unit: "10. Auctions, Bidding, and Contests"
pages: 281-309
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Auctions, Bidding, and Contests

## L0 — One line
In sealed-bid and Dutch auctions you should bid as if you have already won; bidders also adapt to the rules, so many rule changes do not change what the seller gets.

## L1 — The gist (≤ 120 words)
How should you bid, and does the auction format matter? The authors show that in a Vickrey (second-price: the winner pays the second-highest bid) auction, bidding your true value is a dominant strategy. English and Japanese (rising-price) auctions end at the Vickrey outcome. Dutch (falling-price) and sealed-bid auctions match each other, and (private values, symmetric bidders) revenue equivalence says all four give the seller the same average revenue. To avoid the winner's curse (winning but overpaying), bid as if you have already won. Rule changes are often offset by bidder adaptation. Preemption games (who moves first) and wars of attrition (who outlasts) can be modelled as auctions. The spectrum case shows tacit cooperation (gains without agreement).

**Prerequisites:** dominant strategy; averages and uniform probability; conditional expectation ("given I won"); idea of equilibrium.

## L2 — Key ideas (5–10 bullets)
- **Value = walkaway number**: the price at which you are indifferent between winning and losing. Values may be private or common (p. 283).
- **Vickrey auction**: the highest bid wins and pays the second-highest bid. Bidding your true value is dominant, shown by comparing a $50 bid with a $60 bid (pp. 284–286).
- **Equivalences**: English and Japanese auctions give the Vickrey outcome (with small bid increments). Dutch auctions match sealed-bid auctions. Revenue equivalence holds for private values and symmetric bidders (pp. 286, 296).
- **Bid as if you've won** (condition on winning). This is the authors' key tool against the winner's curse (ACME, pp. 291–294).
- **Rules change, strategies adapt**: the buyer's premium is borne by the seller if buyers take it into account, and the T-bill pricing change may leave the Treasury's cost unchanged (pp. 287, 296, 298).
- **eBay** resembles a Vickrey auction, but the authors explain sniping by information leaks and, as their best explanation, by bidders who do not know their own value (pp. 288–290).
- **Preemption and war of attrition** can be modelled as auctions: fire when the two success chances sum to 1; a war of attrition has no single best strategy, so seek a deal (pp. 300–303).
- **Spectrum case**: in the authors' simplified two-license simultaneous auction, the weaker bidder can settle for one license and the stronger bidder rationally lets it. This is tacit cooperation (pp. 305–308).

## L3 — Walkthrough

### Introduction (pp. 281–282)
An auction has one seller and many buyers, and the high bidder wins (p. 281). A **procurement auction** has one buyer and many sellers, and the lowest bid wins (p. 281). The authors raise the **winner's curse** (regret from winning and over-paying) and the question of whether to bid at all (p. 282).

### English and Japanese auctions (pp. 282–284)
- **English (ascending) auction**: bids rise; the optimal strategy is to bid until the price exceeds your value, then drop out (p. 282). The authors assume very small increments, so endgame issues do not matter (p. 282).
- **Value** is your walkaway number: the highest price at which you still want to win. At a dollar more you would pass. It may include a premium for denying a rival, the excitement of winning, and resale value (pp. 282–283).
- **Private value**: your value does not depend on others' views. **Common value**: the item is worth the same to all, but each has a different estimate (e.g. an offshore oil lease). Real items usually mix both (p. 283).
- In an English auction you do not see who is silently willing to bid, nor how high a dropout would have gone (p. 283).
- **Japanese auction**: all bidders start with hands raised and a clock rises. Lowering your hand is permanent. The auction ends when one bidder remains. Everyone sees how many bidders are active and where each drops out (pp. 283–284).
- Result: bidders drop out at their value, so the highest-value bidder wins and pays the second-highest valuation (p. 284).

### Vickrey auction (pp. 284–286)
- Rules: sealed bids; the highest bid wins; the winner pays the *second-highest bid* (p. 284).
- Claim: bidding your true valuation is a **dominant strategy**, meaning best whatever others do. You need not know how many rivals there are or what they do (pp. 284–285). In an ordinary pay-your-bid sealed auction the problem is complicated (p. 284).
- Argument (value $60, compare bid $50 with bid $60), by the highest rival bid (pp. 285–286):
  - Above $60 (e.g. $63): both bids lose, so no difference (p. 285).
  - Below $50 (e.g. $43): both win and pay $43, so no difference (p. 285).
  - Between $50 and $60 (e.g. $53): bidding $60 wins at $53; bidding $50 loses. Since value is $60, you prefer winning (pp. 285–286).
- So the only time bidding below your value changes the outcome is when you lose an auction you wish you had won. "A similar argument shows" you never want to bid above it (p. 286).
- *Intuition note:* Your bid only decides whether you win. The price you pay is set by someone else's bid. So you want to win exactly when the price is below your value, and bidding your value does that.

### Revenue equivalence, first form (pp. 286–287)
- English/Japanese and Vickrey reach the same place: the highest-value person wins and pays the second-highest valuation (p. 286). Increments cause small deviations (p. 286).
- Difference: in English and Japanese auctions bidders learn about others' values. In Vickrey they learn nothing until the end. With private values this information is irrelevant, so the seller makes the same amount in all three (pp. 286–287).
- This is part of a more general result: in many cases, a rule change does not change seller revenue (p. 287).

### Buyer's premium (pp. 287–288)
- Sotheby's and Christie's add a 20% premium: a $1,000 winning bid means a $1,200 check (p. 287).
- The authors say the seller pays, provided buyers know the rule and take it into account (p. 287). A collector with a $600 value should bid $500 (p. 287).
- The premium works like a currency conversion: "$100" means $120. The winner pays the same total as before; the auction house takes a share of it, so the cost falls on the seller (p. 287).
- Takeaway: players adapt strategies to new rules, and in many cases they precisely offset the change (p. 288).

### Online auctions (pp. 288–290)
- eBay uses **proxy bids**: you authorise eBay to bid up to your maximum, and it bids the minimum needed (p. 288).
- Example: proxies A $26, B $33, C $100. C wins and pays $34, just above the second-highest proxy (p. 288).
- If all proxy bids were submitted once and simultaneously, the game would equal a Vickrey auction, and true-value bidding would be dominant (p. 288).
- Departures from Vickrey:
  - **Several similar items** (e.g. ten Pearl Export drum sets) mean your value depends on what else is for sale, now and later (pp. 288–289).
  - **Sniping** (bidding at the last minute, or via services like Bidnapper) occurs in practice even for one-of-a-kind items (p. 289).
- Explanation 1: others may learn from your early proxy bid. A dealer bidding on a Bauhaus chair signals it is authentic, so rivals would pay more. The authors note this implies the bidder's identity is known to others; since sniping is so common, they suggest there are other explanations (pp. 289–290).
- Explanation 2 (the authors' "best explanation"): many bidders do not know their own value. A lazy $1,000 proxy on a Porsche valued at $19,000 by an expert would push the price up early and prompt homework; sniping keeps rivals ignorant until too late (p. 290).
- *Intuition note:* Proxy bidding looks like a sealed second-price auction but is not one: other bidders may learn from your bid before the auction ends. Hiding information then has value.

### Bidding as if you've won; ACME (pp. 290–293)
- **Consequentialist** thinking: look ahead and assume the situation in which your action matters. Example: when proposing marriage, presume the answer is yes. If you would then regret it, do not ask (pp. 290–291).
- **ACME game**: your improvements raise ACME's value by 50%. The current value is uniform on $2M–$12M (mean $7M). You make one take-it-or-leave-it bid. Owners accept if the bid exceeds the current value (p. 291).
  - Example: bid $10M. If the value is $8M, it becomes $12M, profit $2M. If the value is $4M, it becomes $6M, a $4M loss (p. 291).
- The aim is the break-even bid, a cap on what you would bid; always bid less than it (pp. 291–292).
- **Naive reasoning** (the common error): the average is $7M, ×1.5 = $10.5M, so bid up to $10.5M (p. 292).
- **Correct reasoning**: condition on acceptance (p. 292).
  - Offer $10.5M: acceptance implies value in $2M–$10.5M, mean $6.25M; ×1.5 = $9.375M < $10.5M (p. 292).
  - Offer $8M: acceptance implies mean $5M; ×1.5 = $7.5M < $8M (p. 292).
  - Offer $6M: acceptance implies value in $2M–$6M, mean $4M; ×1.5 = $6M, so break-even (p. 292).
- Rejected offers do not matter, since you do not get the firm then (pp. 292–293).
- *Intuition note:* Being accepted is itself information: it tells you the firm is worth less than you hoped. Price your offer on that bad news, not on the unconditional average.

### Sealed-bid auctions (pp. 293–294)
- Rules: the highest bidder wins and pays their own bid (p. 293).
- Never bid your value: you at best break even. Bidding below it ("shading") dominates (p. 293).
- How much to shade depends on rivals' bids, which depend on yours, an "infinite loop". The way out: bid as if you've won, assuming all other bidders are below you (p. 293).
- **Confederate argument**: suppose an insider lowers your bid from $100 to $80 when you would win, and does nothing otherwise (p. 293).
  - If $100 would lose, $80 also loses (p. 294).
  - If $100 would win, you end at $80 (p. 294).
  - Hence bidding $80 from the start is identical, so choose your bid assuming you will win (p. 294).

### Dutch auctions (pp. 294–296)
- The clock starts high and falls. The first to stop it wins and pays that price. At Aalsmeer, the Dutch flower market, bidding goes in reverse (p. 294). It is the reverse of the Japanese auction (p. 294).
- Instruct an agent to bid at a price (e.g. €86.3). At that price you know everyone else is still waiting. Waiting longer saves money but raises the risk of losing. At your optimum the saving is no longer worth the risk (p. 295).
- A Dutch auction equals a sealed-bid auction, except you know you have won when you act. Sealed-bid advice (bid as if you've won) matches the Dutch situation exactly (p. 295).
- Hence, sealed-bid and Dutch bids are the same, as are Vickrey and English, and sellers get the same amount (p. 296).
- **Revenue equivalence theorem** (as stated, p. 296): with private valuations and a symmetric game, the seller makes the same average amount whether the auction is English, Vickrey, Dutch or sealed-bid. A symmetric equilibrium of Dutch and sealed-bid auctions has each bidder bid what they expect the next-highest value to be, given that they hold the highest (p. 296).
- Worked numbers: values uniform on 0–100; your value is 60. Bid 30 with one rival, 40 with two, 45 with three (p. 296).
  - (added step) Check: with $n$ rivals, each uniform on 0–60, the expected highest rival value is $60\cdot\frac{n}{n+1}$, which gives 30, 40, 45.
- Moral: players undo rule changes. Pay twice your bid and you bid half; pay the square and you bid the square root. In pay-your-bid auctions bidders shade down to the expected second-highest value (pp. 296–297).
- *Intuition note:* Pay-your-bid and second-price auctions differ in rules, but bidders shade so that the price comes out about the same.

### T-bills (pp. 297–298)
- The Treasury auctions debt weekly. Until the early 1990s winners were paid their bid rates. After prodding from Milton Friedman and others, it tried uniform pricing in 1992 and made it permanent in 1998 (p. 297).
- Example: $100M of notes. The Treasury takes the lowest rates first. The $10M bid at 3.1% and the $20M at 3.25% win, up to all bids at or below 3.6%, plus half of the $20M bid at 3.72% (pp. 297–298).
  - Old rule: each winner gets its own rate (3.1%, 3.25%, … 3.72%) (pp. 297–298).
  - New rule: everyone gets the highest winning rate, 3.72% (p. 298).
- With the *same* bids, the new rule looks worse for the government. But bids will change (p. 298).
- Analogy: if the Treasury paid 1% less than the bid, everyone would bid 1% higher and nothing would change. Like Newton's Third Law, reactions offset rule changes "at least for the cases we've looked at" (p. 298).
- After adjustment, the authors say the Treasury should expect to pay the same rates, while bidders' job is simpler: a bidder whose value is 3.33% can bid it (p. 298).

### Preemption game (pp. 299–301)
- Examples: Apple's Newton (launched 1993, scrapped 1998) was too early, while Palm Pilot (1996) succeeded. Gannett's USA Today (1982) lost over a billion dollars and took twelve years to break even. The fear was that Knight Ridder would launch first, as the market could support at most one national paper (pp. 299–300).
- Preemption: the first to launch may own the market if it succeeds. Too early means failing; too late means being beaten (p. 300).
- Model as a **duel** auction: your bid is the time to shoot, the lowest bid shoots first, and low bids lower the chance of success (p. 300).
- Both players fire at the same time, even with different abilities. If you plan 10 and the rival 8, the rival should wait to 9.99; whoever goes first should wait until just before the rival would shoot (p. 300).
- Setup (Gym 8): success chances are $p(t)$ for you and $q(t)$ for the rival. A hit ends the game; after a miss the other waits and hits with certainty (p. 301).
- Reasoning: waiting is worth it only if being shot at, hoping the rival misses, is as good as shooting now. The right time is when your success chance equals the rival's failure chance. Since failure is $1-q$, shoot at the first moment when $p(t)+q(t)=1$. This is the same time for both (p. 301).
- Assumptions: both know each other's success chances, and trying and failing pays the same as letting the other win (p. 301).

### War of attrition (pp. 301–303)
- Objective: outlast the rival. Modeled as an auction in which *all* participants pay their bid (time in the game) and the highest bid wins; it may make sense to bid more than your value (p. 301).
- **BSB vs. Murdoch**: BSB won the satellite TV license in 1986. Murdoch's Astra-satellite channels arrived in June 1988. After a year the firms had lost a combined £1.5B. The authors call this predictable. Past losses are irrelevant; only the extra cost versus the prize matters (pp. 301–302).
- There is no single best strategy: if the rival is about to fold, stay in; you think so because you think they believe you will stay (p. 302).
- With no consistency check, both can be overconfident, leading to massive overbidding or losses (p. 303).
- Advice: work out a deal. Murdoch merged with BSB at the eleventh hour. Ability to withstand losses set the split, and the fact that both firms were in danger of going under forced the government's hand in allowing the only two players to merge (p. 303).

### Case study: spectrum auctions (pp. 303–309)
- The FCC raised over $40B between 1994 and 2005, and the English 3G auction raised £22.5B (p. 303).
- Setup: two bidders (AT&T, MCI), two licenses (NY, LA), common knowledge of valuations (pp. 303, 305). Selling in sequence has problems (budget, uncertainty over the second license) (p. 303).
- FCC solution: a **simultaneous auction** in rounds. You cannot bid on a license where you are already the high bidder. The auction ends only when a round has no bids (p. 304).
- Valuations are in a table not reproduced in the text layer: AT&T values both licenses more than MCI. AT&T values NY at 10 and LA at 9. MCI's values appear to be 9 and 8, inferred from its stated willingness to bid up to "9 and 8" (pp. 305–307).
- Case discussion:
  - Bidding 10 and 9 wins both but yields 0, and is weakly dominated (p. 306).
  - Bidding 9 and 8 gives a profit of 1 per city, 2 total (p. 306).
  - Starting at 5 and 5 triggers escalation, ending near 9–10 in NY and 8–9 in LA, no better than 2 (pp. 306–307).
  - Better: if MCI bids 6 in LA, stop bidding. You win NY at 5, a gain of 5 (p. 307).
  - Better still: MCI opened at 0 in NY and 1 in LA. You bid 1 in NY, and do not bid for LA. The auction ends and you gain 9 (p. 307).
- Reason: MCI will bid up to 9 and 8 before leaving empty-handed. Denying MCI any license means bidding a total of 17, so the second license costs 16 beyond the 1 paid for NY, above your value. You need not win both just because you can (pp. 307–308).
- Not collusion in the strict sense: no agreement; each side acts in its own interest. The seller loses. Authors call it **tacit cooperation** (p. 308).
- One approach for a seller who wants to avoid it is to sell the licenses in sequence: MCI cannot rebid on NY, so AT&T has nothing to lose bidding for LA (p. 308).
- Larger lesson: when two games are combined, strategies across them become possible. when Fuji entered the US film market, Kodak could respond in the US or in Japan; a price war in the US would have been costly to Kodak, while one in Japan was costly to Fuji and not to Kodak, who had little share there (p. 308). Moral: "look for the larger game" (pp. 308–309).
- *Intuition note:* Two licenses sold together create a link: outbidding the rival on one can raise the price you pay on both. This changes what winning the second license really costs.

## Toy example (ours, not from the text)
**Main idea: price your bid on the news that you won.**
A firm's current value is uniform on $5M–$15M (mean $10M). You can raise any firm's value by 20%. You make one take-it-or-leave-it bid $b$; the owner accepts if $b$ exceeds the current value.
- Naive: mean 10 × 1.2 = 12, so bid up to $12M.
- Check $b = 12$: accepted if the value is in 5–12, mean (5+12)/2 = 8.5; ×1.2 = 10.2 < 12. A loss of 1.8 on average.
- Break-even: accepted value mean is $(5+b)/2$. Set $1.2\cdot(5+b)/2 = b$, so $3+0.6b=b$, so $b=7.5$.
- Check $b = 7.5$: accepted if value in 5–7.5, mean 6.25; ×1.2 = 7.5. ✓ So the cap is $7.5M, and you should bid below it.

## Concepts
- [[dominant / dominated strategy]] — best (or never best) whatever others do; true-value bidding in Vickrey (p. 284)
- [[mechanism design]] — the authors' stated goal is to design a game so that players need not be strategic; the Vickrey auction is their example (p. 284)
- [[incentive compatibility & revelation principle]] — truth-telling is optimal; Vickrey has bidders bid their true value (p. 284); the revelation principle itself is not discussed in this unit
- [[best response]] — in Dutch auctions, bidding where the saving from waiting is no longer worth the added risk (p. 295)
- [[Nash equilibrium]] — symmetric equilibrium in sealed-bid and Dutch auctions; the preemption "can't be an equilibrium" argument (pp. 296, 300)
- [[mutual vs. common knowledge]] — spectrum case: valuations known to both, "and so on" (p. 305)
- [[credible commitment]] — related only loosely; omitted from this unit's claims
- [[bounded rationality]] — related only loosely (bidders not knowing own values, p. 290); omitted
- [[winner's curse]] (new) — winning tells you the item is worth less than you thought; avoid by bidding as if you've won (pp. 282, 291–292)
- [[private vs. common value]] (new) — whether your value depends on others' estimates (p. 283)
- [[Vickrey (second-price) auction]] (new) — highest bid wins, pays second-highest bid (p. 284)
- [[revenue equivalence]] (new) — private values, symmetric bidders: same average seller revenue across four formats (p. 296)
- [[bid as if you've won]] (new) — condition your bid on winning (p. 293)
- [[preemption game]] (new) — moving first can win the market but too early risks failing (p. 300)
- [[war of attrition]] (new) — all pay; winner outlasts the rival (p. 301)
- [[tacit cooperation]] (new) — each side's own interest leaves both firms better off without any agreement (p. 308)

## Canonical instances
- [[acme-bid]] — conditioning on acceptance lowers the break-even bid from $10.5M to $6M (p. 292)
- [[ebay-proxy-and-sniping]] — Vickrey-like but with information effects (pp. 288–290)
- [[buyers-premium]] — rule change borne by the seller (p. 287)
- [[tbill-uniform-price]] — pricing rule change offset by bidding (pp. 297–298)
- [[newton-usa-today-preemption]] — Newton, USA Today as preemption (pp. 299–300)
- [[bsb-murdoch]] — war of attrition ending in merger (pp. 301–303)
- [[spectrum-auction-ny-la]] — simultaneous auction with tacit cooperation (pp. 303–308)
- [[kodak-fuji]] — cross-game punishment (p. 308)

## Bridges (candidates)
- [structural-analogy] Revenue equivalence ↔ mechanism design: different rules, same outcomes when bidders adapt.
- [structural-analogy] Bid as if you've won ↔ statistics: conditioning on selection (winner's curse as selection bias).
- [structural-analogy] Dutch auction ↔ sealed bid: both require committing without learning others' moves.
- [metaphor] T-bill rule change ↔ Newton's Third Law (authors' own analogy, p. 298).

## Questions this raises
- Which assumptions of revenue equivalence (private values, symmetry) fail in real auctions, and what happens then?
- Does the "bid as if you've won" logic extend to common-value auctions in general?
- How can a seller design simultaneous auctions to prevent tacit cooperation?
- In a war of attrition, how can parties commit to quitting credibly?

## Exercises worth doing
- Gym 6 (p. 285) — value of knowing rivals' bids in a Vickrey auction — easy
- Gym 7 (p. 295) — optimal sealed bid with one uniform rival on 0–100 — medium
- Gym 8 (p. 301) — time to shoot in the duel; prove both fire together — medium

## Reading notes
- Printed = pdf page numbers (281–309); both labels agree.
- The tables (T-bill bids, spectrum bids and valuations) are not in the text layer, so their numbers are not transcribed; MCI's values are inferred from the surrounding text and flagged as such.
- Possible inconsistency: the T-bill text says "ten bids" (p. 297) and later "the same eight bids" (p. 298); the table cannot be checked here.
- Misprints: "This is a called a procurement auction" (p. 281); "less that this amount" (pp. 291–292); "two battle of wills" (p. 299).
- In the sniping example the text says the lazy $1,000 proxy "will push the price right up to $1,000" (p. 290). The authors' claim that the seller bears the buyer's premium is stated under the assumption that buyers account for it (p. 287).
- Asterisks and a dagger mark footnotes (e.g. pp. 281, 284, 287, 293, 296) whose text is not on these pages.
