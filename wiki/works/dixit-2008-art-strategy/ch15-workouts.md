---
id: dixit-2008-art-strategy/ch15-workouts
work: dixit-2008-art-strategy
unit: "Chapter 15 (Workouts) — solutions to ten 'Trips to the Gym'"
pages: 409-418
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Workouts: worked answers to ten "Trips to the Gym"

## L0 — One line
Ten short worked solutions apply backward reasoning, best responses, credible commitment, dominant strategies and incentive design to concrete cases (flags, pricing, nuclear threats, auctions, preemption, commissions, royalties).

## L1 — The gist (≤ 120 words)
This chapter gives the authors' answers to ten problems called "Trips to the Gym" (the problem statements are not on these pages). The questions: who wins a flag-taking game, how a cost advantage changes a price duel, how a threat changes a game tree, what bidders should do in auctions, when to shoot first, and how pay schemes shape effort. The answers: work backward from the end; check equilibrium by testing best responses; model a threat as removing options from the game tree; check how much extra pay a better result brings. Small changes can have large effects, such as a 42% cost edge producing a 69% profit edge. The tables and trees mentioned are not in the text of these pages.

**Prerequisites:** basic probability (uniform chance), linear formulas, reading a payoff table or game tree, high-school algebra for a maximum. Terms used: best response = your best choice given the rival's choice; dominant strategy = a choice that is best whatever the rival does.

## L2 — Key ideas (5–10 bullets)
- In the flag game, reasoning backward shows which starting totals lose: 5, 9, …, 21. The first mover does not always have the advantage (p. 409).
- The price-duel payoff tables come from a linear sales formula and the firms' costs; the authors show how to compute them by hand or in a spreadsheet (pp. 409–410).
- A modest cost advantage (42%) produces a larger profit advantage (69%) in the Nash equilibrium (a pair of prices, each a best reply to the other), because of the lower cost and because the price cut also shifts customers (p. 413).
- A U.S. nuclear-response threat removes options from the U.S. node, so the Soviets prefer the status quo (payoff 0 over −100) (p. 414).
- In a Vickrey auction (the winner pays the second-highest bid), you would pay nothing to learn rivals' bids, assuming private values (p. 415).
- A sealed-bid auction (each bidder names one number; the highest wins and pays its own bid) can be derived from a Vickrey auction; with two bidders and values uniform on 0–100, bidding half your value is an equilibrium (pp. 415–416).
- In the preemption game (each side chooses when to shoot; $p(t)$ and $q(t)$ are the two sides' chances of winning by shooting at time $t$, inferred), both sides wait until $p(t)+q(t)=1$ and then shoot (pp. 416–417).
- A flat percentage commission gives weak incentives (p. 417). A nonlinear scheme raises the extra pay for a higher price but creates conflict over the threshold (p. 417).
- Author and publisher disagree on the best list price ($20 vs $24.30) because the publisher's effective printing cost is about $8.60 (p. 418).

## L3 — Walkthrough

**No. 1 (flag game, p. 409).** The rules are not restated here. The reasoning ("groups of four", "forced to take" 1) implies each turn takes 1–3 flags and the player who takes the last flag loses (inferred from the text).
- Leaving the rival 1 flag wins, since he is forced to take it. So starting a turn with 2, 3 or 4 is winning (p. 409).
- Hence 5 is losing, because every move leaves 2, 3 or 4. Next, 9 is losing, and so on to 21 (p. 409).
- A player facing 21 loses, assuming the rival always brings the total down in groups of four (p. 409).
- Equivalent view: taking the next-to-last flag wins. With 21 flags you act as if there were 20 and try to take the last one of the twenty; this is a losing position, at least if the other side understands the game (p. 409).
- The first mover need not always have the advantage (p. 409).

*Intuition note:* Solve from the end of the game. Positions where every move hands the rival a win are losing. The pattern repeats every four flags.

**No. 2 (pricing duel, pp. 409–410).** Sales of RE are

$$\text{quantity}_{RE} = 2800 - 100\times P_{RE} + 80\times P_{BB}$$

BB's sales are the mirror image. Both have cost $20, so

$$\text{profit}_{RE} = (P_{RE}-20)\times \text{quantity}_{RE}.$$

- Spreadsheet: RE's prices go down column A and BB's prices across row 1. Cell B2 is `=MAX(2800-100*$A2+80*B$1,0)`. The MAX stops sales going negative when prices differ a lot (p. 410).
- RE's cost goes in J2. Profit cell B8 is `=B2*($A8-$J$2)`. BB's quantity is `=MAX(2800-100*B$1+80*$A14,0)`, with cost in J3 and profit `=B14*(B$1-$J$3)` (p. 410).
- Changing the numbers changes the experiment (p. 410).

**No. 3 (RE's cost falls to $11.60, pp. 412–413).** Set J2 = 11.60 and enter the new profits in the payoff table. The authors had to use a range of lower prices to locate best responses (p. 413).
- New Nash equilibrium: BB charges $38 and RE charges $35 (p. 413).
- BB's profit falls from $40,000 to $32,400. RE's rises from $40,000 to $54,756 (p. 413).
- RE's cost edge is 42% ($11.60 is 58% of $20). Its profit edge is 69% ($54,756 is 1.69 × $32,400) (p. 413).
- RE gains twice: lower cost, and a price cut that takes customers from BB (p. 413).

*Intuition note:* RE's lower cost lets it cut its price, and the price cut also shifts customers from BB. RE benefits twice and BB's profit falls, so the profit gap (69%) exceeds the cost gap (42%).

**No. 4 (nuclear commitment, pp. 413–414).** The game-tree pictures are not in the text.
- Without a move, after a Soviet invasion the U.S. can accept (some loss of prestige), fight conventionally (defeat, casualties, maybe more lost prestige), or use nukes (far worse, due to Soviet counterattack). The least-bad U.S. response is to abandon Western Europe (p. 414).
- The threat "we will respond with nuclear weapons if you attack" removes the first two U.S. branches (p. 414).
- The Soviets then get −100 from invading and 0 from the status quo, so they accept the status quo (p. 414).
- Chapters 6 and 7 discuss how to make the threat credible (p. 414).

**No. 5 (airline fares, p. 414).**
- Participation constraint (business travelers): fare $215 is below their willingness to pay of $300, so it holds (p. 414).
- Incentive compatibility (tourists): economy gives $140 − 140 = 0 surplus. First class would give $175 − 215 = −40, so they do not switch (p. 414).

**No. 6 (Vickrey auction, pp. 414–415).**
- You would pay nothing to learn the others' bids. Bidding your true value is a dominant strategy, so you would bid the same whatever you learn (p. 415).
- Caveat: this assumes a private value. In a common-value Vickrey auction you might change your bid, but only because what others do changes what you think the item is worth (p. 415).

**No. 7 (from Vickrey to sealed-bid, pp. 415–416).** Two bidders, values uniform on 0–100 (p. 415).
1. In a Vickrey auction with value 60, you bid 60. If you win, you pay the second-highest bid, which is uniform on 0–60, so on average $30 (p. 415).
2. In general you expect to pay $X/2 when you win with value X. So replace the second-price rule with "pay X/2 when you win". The average outcome is the same, so your optimal bid should not change (p. 415).
3. Let everyone follow this rule. Now it is a sealed-bid auction where you pay half your number, like paying in dollars instead of pounds (p. 415).
4. A bid of "$80" really means $40. If you must pay your whole bid, everyone halves their bids. Equilibrium: each bids half their value (p. 416).

Check: suppose the other bids half his value. If you bid $X$, you win when his value is below $2X$, with probability $2X/100$ (p. 416). Your payoff with true value $V$:

$$\text{Prob}(X\text{ wins})\times(V-X)=\left(\frac{2X}{100}\right)(V-X)$$

This is maximized at $X=V/2$ (p. 416). (added step: the derivative $\tfrac{2}{100}(V-2X)$ is zero there.) So this is a Nash equilibrium. Checking an equilibrium is easier than finding one (p. 416).

*Intuition note:* Shading your bid below your value trades a lower winning chance for a lower price. If the rival bids half his value (two bidders, uniform values), the best trade-off is exactly half.

**No. 8 (preemption, pp. 416–417).** Here $p(t)$ is your chance of winning if you shoot at $t$, and $q(t)$ is the rival's (inferred from the text).
- If the rival will act at $t=10$, you can shoot at 9.99 (winning chance about $p(10)$) or wait and win if she fails (chance $1-q(10)$). Preempt if $p(10) > 1-q(10)$ (p. 416).
- The rival does the same calculation. If she thinks you will preempt at 9.99, she prefers to move first at 9.98 if $q(9.98) > 1-p(9.98)$ (p. 416).
- The time at which neither side wants to preempt is given by $p(t)\le 1-q(t)$ and $q(t)\le 1-p(t)$ (p. 416). These are one and the same condition (p. 417):

$$p(t)+q(t)\le 1.$$

- Both wait until $p(t)+q(t)=1$ and then shoot (p. 417).

**No. 9 (house sale commission, p. 417).**
- A $250,000 sale gives a $15,000 commission, generally split evenly between your agent and the buyer's agent. When your agent brings in an extra $20,000, that is just $600 more after the split, and the agent typically has to share with the agency, leaving only $300. So agents have an incentive to do the deal quickly rather than get the best price (p. 417).
- Nonlinear scheme: 2.5% on the first $200,000 and 20% above. At $250,000 the commission is still $15,000. At $270,000 it rises by $2,000 even after the split (p. 417).
- Problem: where to put the threshold. You may think $300,000 is possible and want the threshold near $250,000. The agent argues $250,000 is the market price and wants it at $200,000. This creates conflict at the start (p. 417).

**No. 10 (book royalties, pp. 417–418).**
- Typically the publisher gets 50% of list price as its wholesale price; it pays the author 15%, and the cost to print and ship an average hardcover is around $3. At list price $p$ with sales $q(p)$:

$$(0.5p-0.15p-3)\times q(p)=0.35\times(p-8.6)\times q(p)$$

- The publisher keeps about 35% of the list price but bears the whole printing cost. This is like an effective printing cost of $8.60, almost three times the real one (p. 418).
- With $q(p)=40-p$ (thousands), the author, maximizing revenue, picks $20. The publisher, maximizing profit, picks $24.30 (p. 418). (added step: revenue $p(40-p)$ peaks at $p=20$. Profit $0.35(p-8.6)(40-p)$ peaks at $p=(40+8.6)/2=24.3$.)

*Intuition note:* The author is paid per dollar of sales, so wants revenue maximized. The publisher bears the printing cost, which acts like a higher cost per copy, so wants a higher price and fewer copies.

## Toy example (ours, not from the text)
Redo the No. 7 check with value $V=60$, assuming the other bidder bids half his value and values are uniform on 0–100. Payoff $=\frac{2X}{100}(60-X)$.
- $X=20$: $0.40\times 40=16$.
- $X=30$: $0.60\times 30=18$.
- $X=40$: $0.80\times 20=16$.

Bidding 30 $=V/2$ beats bidding 20 or 40. It also matches the Vickrey expectation, where you pay $60/2=30$ on average when you win. This holds for $X\le 50$; above that the winning probability would exceed 1.

## Concepts
- [[backward-induction]] — solve from the end: positions leaving the rival a winning move are losing (p. 409)
- [[nash-equilibrium]] — each side's choice is a best response to the other's (pp. 413, 416)
- [[best-response]] — the action that maximizes your payoff given the rival's action; used to locate equilibrium prices and bids (pp. 413, 416)
- [[extensive-form-game]] — a game tree; the threat removes branches (p. 414)
- [[credible-commitment]] — in the model, the U.S. threat removes its other options so the Soviets face a nuclear response; how to make it credible is deferred to chapters 6–7 (p. 414)
- [[dominant-dominated-strategy]] — truthful bidding in a Vickrey auction is dominant (p. 415)
- [[incentive-compatibility-revelation]] — participation and incentive-compatibility constraints in the fare example (p. 414)
- [[strategic-normal-form-game]] — payoff tables for pricing (p. 412)
- [[private-vs-common-value]] (new) — whether your valuation is independent of what others think (p. 415)
- [[linear-vs-nonlinear-incentive-pay]] (new) — pay proportional to outcome vs. a rate that changes at a threshold (p. 417)

## Canonical instances
- [[flag-game]] — backward induction; losing totals 5, 9, …, 21 (p. 409)
- [[price-duel-cost-advantage]] — RE vs. BB pricing; equilibrium $35 vs $38 (p. 413)
- [[nato-nuclear-threat]] — a threat modelled as removing branches from the game tree; NATO members wanted a credible U.S. commitment (p. 414)
- [[airline-fare-discrimination]] — participation and incentive-compatibility checks (p. 414)
- [[vickrey-auction]] — truth-telling is dominant (p. 415)
- [[sealed-bid-first-price-auction]] — bid half your value, uniform 0–100 (p. 416)
- [[preemption-game]] — shoot when $p+q=1$ (p. 417)
- [[real-estate-commission]] — weak incentives under linear commission (p. 417)
- [[book-royalty-conflict]] — author and publisher disagree on list price (p. 418)

## Bridges (candidates)
- [structural-analogy] Dollars-for-pounds relabeling (No. 7) ↔ revenue-equivalence-style reasoning: show two auction rules give equal expected payments, then convert one into the other.
- [same-math] Optimal bid $X=V/2$ (maximizing $\frac{2X}{100}(V-X)$) ↔ monopoly pricing with linear demand: both maximize a product of two linear terms.
- [structural-analogy] Nonlinear commission threshold ↔ principal–agent contract design: the principal and agent disagree on the target.

## Questions this raises
- How does the bid-half rule change with $n$ bidders or a different value distribution? (The text covers only two bidders, uniform values.)
- How can a threat like the U.S. nuclear response be made credible? (Pointed to chapters 6–7, p. 414.)
- Can a commission scheme be designed so the threshold conflict does not arise?
- How might $p(t)$ and $q(t)$ change over time in the preemption game, and what happens if the rival's skill is uncertain? (not covered here)

## Reading notes
- Printed page = pdf page (no offset).
- The tables on pp. 411–412 and the game-tree figures on pp. 413–414 are not in the text layer, and I did not see their images. Table values are not reproduced; the figures in L3 come from the prose. I confirmed from the formulas that RE's $54,756 and BB's $32,400 follow from prices $35 and $38.
- The rules of the flag game, and the definitions of $p(t)$, $q(t)$ and the fare context, are not given on these pages (the text points to earlier chapters) and are inferred here.
- p. 418 calls the effective printing cost "$8.60"; $3/0.35$ is about $8.57, so the text rounds.
- Only the formula image on p. 416 was checked against the page image; it matches the text above.
- This unit contains solutions only, not the original exercise statements, so no exercise list is given.
