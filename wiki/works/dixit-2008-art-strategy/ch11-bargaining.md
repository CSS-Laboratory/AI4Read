---
id: dixit-2008-art-strategy/ch11-bargaining
work: dixit-2008-art-strategy
unit: "11. Bargaining"
pages: 310-330
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Bargaining

## L0 — One line
Reasoning backward predicts a quick split that favours the side with the better fallback, the proposer, or the more patient party; strikes begin because the two sides lack a common view of where the talks will end.

## L1 — The gist (≤ 120 words)
The chapter asks who gets how much of a bargaining "pie", when agreement comes, and why strikes happen. With alternating offers and a deadline, backward reasoning gives a near 50:50 split and agreement on day one. Better outside options (BATNAs), sole power to propose, or greater patience shift the split. The pie is the extra value created beyond the BATNAs. Strikes arise because the sides lack a common view of the end; each tries to prove it can wait longer (brinkmanship: a threat that risks breakdown). Virtual strikes would keep the pain for the parties and spare outsiders. The appendix solves the no-deadline case (Rubinstein) and gets $\delta/(1+\delta)$ for the responder (equal patience).

**Prerequisites:** looking ahead and reasoning back (the ultimatum game of ch. 2); simple fractions and algebra with one unknown; discounting ("a dollar later is worth less").

## L2 — Key ideas (5–10 bullets)
- With alternating offers and a known last day, backward reasoning gives the last proposer an edge that shrinks with the number of rounds: $505 vs $495 on a 101-day season, so, when offers come quickly and the horizon is long, the rule is "split the total down the middle" (pp. 311–312).
- Fallback options act like golf handicaps: each side first gets its outside income, and the remainder is split evenly (e.g. union $650 vs management $350) (p. 313).
- The pie is the extra value from agreeing, beyond each side's BATNA. In the airfare case it is $1,000, not $2,818, which changes the fair split (pp. 314–316).
- A strategic move that hurts the rival more than yourself raises your share, even if it also hurts you (union $450 instead of $400) (p. 316).
- Strikes occur because the sides lack a common view of the end. They prove low waiting costs by taking on costs or risk, and brinkmanship (a threat that leaves a small, rising chance of breakdown) keeps strikes going day by day (pp. 317–319).
- A virtual strike (work goes on as normal, but neither side is paid) aims to replicate the bargaining costs to the parties while leaving third parties unharmed; with the same BATNAs, neither side gains from a real strike over a virtual one (pp. 321–323).
- Sole power to propose gives most of the pie, but over many rounds the responder may have an incentive to appear irrational, to teach the proposer a lesson (pp. 324–326).
- Rubinstein: with no end date and equally patient sides, the responder gets $\delta/(1+\delta)$, where $\delta$ is the share of value left if the deal is done one round later. If the sides differ, the more patient side gets more (pp. 326–330).

## L3 — Walkthrough

### Opening and the basic model (pp. 310–312)
The author asks: will there be agreement, will it be amicable, who concedes, who gets how much? The chapter reuses "look ahead, reason back" from the ultimatum game (ch. 2) (p. 310).

**Setup.** A hotel's season lasts 101 days. Each open day yields $1,000 profit. The union and management alternate offers, one per day. The hotel opens only after agreement (pp. 310–311).

**Backward reasoning.**
- Last day, union's turn: management accepts anything above nothing, so the union gets all $1,000 (p. 311).
- Day before, management's turn: the union can reject and get $1,000 on the last day, so management must offer that. The union cannot get more, so management offers no more. Of the $2,000 over two days, each gets $500 per day (p. 311).
- One day earlier, union's turn: the union offers management $1,000 and asks $2,000, which is $667 per day for the union and $333 for management (p. 311).
- The proposer has an advantage, but it shrinks with the number of rounds. At the start of the 101-day season the split is about $505 vs $495 (pp. 311–312). (The tables themselves are not in the text layer.)
- Almost the same split would emerge if management made the last offer, or if there were no rigid rules (p. 312).
- Alternating offers and a finite horizon are devices to help us look ahead. They are harmless when offers come quickly and the horizon is long. The result is "split the total down the middle" (p. 312).
- Second prediction: agreement on the first day, since both sides foresee the same outcome and have no reason to lose $1,000 a day. Real strikes happen, and later sections explain them (p. 312).

*Intuition note:* Each side knows what the other can get by waiting one round. So today's offer must at least match that, and need not exceed it. Many rounds make the proposer's edge tiny.

### The handicap system (pp. 312–313)
Cost of waiting matters. If union members can earn $300 a day outside, then at each turn management must offer at least that for the current day plus what the union could get a day later. Agreement is still immediate, but the union does better (p. 312).

- Union handicap $300 leaves $700 to split evenly, $350 each. The union gets $650 and management $350 (p. 313).
- If management can run the hotel with scabs (replacement workers) at $500 profit a day and the union has no outside income, management gets $750 and the union $250 (p. 313).
- With both ($300 and $500), only $200 remains. Split evenly, management gets $600 and the union $400 (p. 313).
- General idea: the better a party can do alone without agreement, the larger its share (p. 313).

### Measuring the pie (pp. 314–316)
The size of the pie is the value created by agreement compared with no agreement. In the example it is $200, not $1,000 (p. 314). Fallbacks of $300 and $500 are **BATNAs** (Best Alternative to a Negotiated Agreement; term from Fisher and Ury): the best you can get without agreement with this party. The point of negotiation is the value above the sum of BATNAs (p. 314).

**Airfare case.** A New York lawyer serves a Houston company and a San Francisco (SF) company. He flew the triangle route NY–Houston–SF–NY for $2,818 total (p. 314). Separate round trips would cost $1,332 for Houston (twice $666) and $2,486 for SF, total $3,818 (p. 315). Ad hoc splits:

| Rule | Houston pays | SF pays |
|---|---|---|
| Equal split | $1,409 | $1,409 |
| Leg by leg, shared middle leg | $1,120.50 | $1,697.50 |
| Proportional to round-trip fares | $983 | $1,835 |

Houston would reject the equal split because its solo round trip is only $1,332 (p. 315).

**BATNA approach.** The fallback is two separate trips. The extra cost of those over the triangle is $3,818 − $2,818 = $1,000, which is the pie (p. 315). Each company is equally valuable in creating the savings. If they are equally patient, they split it evenly: each saves $500 relative to its round-trip fare. Houston pays $832 and SF pays $1,986 (p. 315). The split should not follow mileage or relative fares, because without agreement the whole $1,000 is lost (p. 315). The authors say this approach can be traced to the Talmud's principle of the divided cloth (p. 316).

If BATNAs are not fixed, you want to raise your own and lower the other side's. These aims may conflict (p. 316).

### This will hurt you more than it hurts me (pp. 316–317)
What matters is your outside opportunity relative to the rival's. A commitment or threat that lowers both, but damages the rival more, helps you (p. 316).

**Example.** Start from union $300 and management $500, which gave $400 and $600. The union gives up $100 a day of outside income to intensify picketing, which cuts management's profit by $200 a day. Starting points become $200 and $300. The remaining $500 is split equally, so the union gets $450 and management $550, an extra $50 for the union (p. 316).

**Baseball 1980.** Players struck in the exhibition season, returned for the regular season, and threatened a strike from Memorial Day weekend. Owners' gate and television revenues are low early and rise from Memorial Day. So the owners' loss relative to the players' was highest in those periods (pp. 316–317). The owners gave in just before the second half of the threatened strike, but the first half actually occurred. So the theory is incomplete: why are there strikes? (p. 317).

### Brinkmanship and strikes (pp. 317–320)
Even before a contract expires, delay is costly. Negotiation itself carries risk: misperception, tension, personality clashes, suspicion of bad faith. The process may break down although both sides want it to succeed (p. 317).

- The sides may not share information or perspective, so they do not see the same end. Each must guess the other's cost of waiting. A low waiting cost helps, so each side claims it is low. Such claims must be proved by incurring costs and showing it can hold out longer, or by accepting greater risk (p. 318).
- A strike is signaling. It costs efficiency, since both sides would like to prove their low costs without the losses (p. 318).
- A threat of immediate breakdown lacks credibility while time remains. A smaller threat can be credible: rising tension may cause a breakdown that the union does not want. This is good for the union if management fears it more. Brinkmanship is a weapon for the party that fears a breakdown less (p. 318).
- Working under an expired contract is usually disadvantageous to the union, which seeks revision. It needs some chance of a strike to motivate the firm. Continuing work is seen as a sign of union weakness (pp. 318–319).
- What keeps a strike going? A threat never to return would not be credible, but waiting one more day or week is credible, because the loss is smaller than the potential gain. If workers believe they will win soon, waiting is worthwhile. Management may see it differently. If it believes the workers are about to concede, one more day's loss is worth a better contract. So both hold out (p. 319).
- A strike is a large chance, even certainty, of a small loss, instead of a small chance of a large loss. The loss grows as the strike continues. One side backs down when it finds the other truly stronger. Strength can come from valuable alternatives, from a win mattering for other negotiations, or from a loss being very costly (p. 319).
- Application to nations: in talks on defence cost-sharing, the U.S. works under an "expired contract", so allies are content to let talks drag on. The text asks whether the U.S. should use brinkmanship (pp. 319–320).
- With brinkmanship, the parties sometimes do go over the brink. Breakdowns can be regretted but take on momentum (p. 320).

*Intuition note:* The two sides may hold different beliefs about who can wait longer, since each must guess the other's cost of waiting. A strike is a way to prove a low waiting cost, though it costs efficiency. Each day's loss is small, but it grows as the strike continues.

### Simultaneous bargaining over many issues (pp. 320–321)
Many dimensions (wages, health benefits, pensions, CO₂ allocations) can be reduced to money, but the sides may value items differently. Example: group health cover costs the company $1,000 per year instead of $2,000 for individuals. Workers would rather have cover than $1,500 extra wages, and the company would rather give cover than $1,500 in wages. Joint bargaining can then make both better off. The text says broad GATT/WTO trade talks have had better success than narrow ones (p. 320).

Linking issues also lets one issue create threats in another. For example, the U.S. might threaten the military relationship to win market access from Japan. Japan would insist on negotiating the issues separately (pp. 320–321).

### The virtues of a virtual strike (pp. 321–323)
Strikes harm outsiders: UPS customers, Air France holidaymakers, future generations in a global-warming dispute (p. 321). In the 2002 U.S. dock lockout (ten days, ended by President Bush invoking Taft-Hartley), disruption cost more than $10 billion over a $20 million dispute, 500 times larger (p. 321).

**Virtual strike (or lockout):** work and production go on as normal, but neither side gets paid. Workers work for nothing. The firm gives up all its revenue (not profit, which might be too hard to measure and might understate the true cost to the firm). The money could go to the government, a charity, or customers (free product). Management and labour feel the pain; outsiders get a windfall (pp. 321–322).

- Actual strikes can permanently destroy demand. The 2004–5 NHL lockout lost the whole season (p. 322).
- Reported cases: Jenkins valve plant, Bridgeport (WWII, navy); 1960 Miami bus strike (free rides); 1999 Meridiana airline in Italy (receipts to charities); 2000 Italian Transport Union (100 million lire forfeited, 300 pilots, a medical device for a children's hospital) (p. 322).
- A problem: a real strike is often designed to inconvenience consumers, so forfeiting profits may not replicate its cost. In all four examples management forfeited its entire gross revenue (p. 322).
- Workers would accept the arrangement to impose pain and prove a low cost of waiting. We might expect them to work harder, since each sale hurts the firm (p. 323).
- If BATNAs are the same in the virtual and real strike, neither side gains from the real strike. The sides could agree in advance to use a virtual strike if talks fail (p. 323).

### Case study: 'tis better to give than to receive? (pp. 323–326)
**Setup:** only management makes offers each day. Labour accepts or rejects. The potential profit falls as the season passes (p. 323).

**Backward reasoning (p. 324).** On the last day labour accepts any positive amount, say $1. A day earlier it accepts $2, and so on up to the first day. Management proposes $101 to labour and labour accepts. This suggests that, in making offers, 'tis better to give than to receive. The author expects an outcome far from 50:50, with management getting close to the entire amount and agreement on day one. (The amounts are as printed; the tables are not in the text layer.)

Postponing a day costs management $999 and labour only $1. This exaggerates management's power. To the extent that labour cares about how its pay compares with management's, such a radically unequal split will not be possible. Management should find the minimum acceptable amount. If labour in the last period might be willing to accept $200 against $800 (when its alternative is zero), management can keep a 4:1 split every day and take 80% of the total (p. 324).

**Why to be suspicious.** In a one-shot game, a wrong assumption ends the game. In the 101-round game, the receiver can play tough early to show he may be irrational or hold a 50:50 norm (p. 325).

**Two-day example (pp. 325–326).** You offer 80:20 on day 1 and are refused. Had the receiver accepted, he would have had 200 on each of two days, so 400. A calculating receiver would refuse if that led to 50:50 in the final round, i.e. 500. If it is a bluff, you can stay at 80:20 in the last round. If you offered 67:33 and were refused, accepting would have given 333 per day, 666 in all. Now the best he can hope for is 500, so he would be worse off even if he wins. This is some evidence that it is not a bluff, and it may make sense to offer 50:50 in the last round (p. 326).

Conclusion: the receiver can show your theory is not working. The other side will often gain by appearing irrational, so you cannot simply accept irrationality at face value. But if the damage to themselves (and you) is too large for a bluff to help, you may want to reassess their objectives (p. 326).

*Intuition note:* In one round, the proposer can lean on the responder's "better than nothing". In many rounds the responder may have an incentive to refuse at first, to show he is perhaps not that kind of player.

### Appendix: Rubinstein bargaining (pp. 326–330)
**Model.** Two sides alternate offers dividing a pie of size 1: a proposal $(X,1-X)$. The game ends when one side accepts. Delay is costly (p. 326). Time is money: $1 now equals $1.10 a year later at 10% interest. Delay also risks permanent loss of customers and jobs, so impatience is the probability of this in a week (p. 327).

**Impatience.** $\delta$ is the share of value left if the deal is done next round instead of today. For example, $\delta=0.99$ if a dollar next week is worth 99¢ today. $\delta$ close to 1 means patient. $\delta=1/3$ means two-thirds is lost each week. The degree of impatience generally depends on the time between offers; a shorter gap means $\delta$ closer to 1 (e.g. 0.999999 for a minute) (p. 327).

**Derivation.** First, can the least you will accept be zero? No. If the other side offered zero and you refused, you could offer them $\delta$ tomorrow, which they accept because waiting costs them (they would only get 1 in their best-case scenario, in which you accept 0 in two periods). That leaves you $1-\delta$ tomorrow, so you never accept less than $\delta(1-\delta)$ today (pp. 327–328). The argument is not fully consistent, since it assumed you take zero in two periods. What is needed is a number that holds steady over time (p. 328).

Let $L$ be the lowest division you will ever accept. If you reject and counter, the other side can never hope for more than $1-L$ at its next turn. So they should accept $\delta(1-L)$ tomorrow. That leaves you $1-\delta(1-L)$ tomorrow for sure. So today you never take less than $\delta(1-\delta(1-L))$ (p. 328). So:

$$L > \delta\bigl(1-\delta(1-L)\bigr) \quad \text{(as printed, p. 328)}$$

$$\text{(added step; weak inequality, as in the page's final line)}\quad L \ge \delta-\delta^2+\delta^2L \;\Rightarrow\; L(1-\delta^2)\ge\delta(1-\delta)$$

$$L \ge \frac{\delta(1-\delta)}{1-\delta^2}=\frac{\delta}{1+\delta} \quad \text{(p. 328)}$$

The other side also never accepts less than $\delta/(1+\delta)$. Let $M$ be the most you can ever hope for. Next period you get at most $1-\delta/(1+\delta)=1/(1+\delta)$. So today you always accept $\delta\cdot\frac{1}{1+\delta}=\frac{\delta}{1+\delta}$ (p. 329). Hence

$$L \ge \frac{\delta}{1+\delta}, \qquad M \le \frac{\delta}{1+\delta}$$

The least you accept and the amount you always accept coincide, so the responder gets $\delta/(1+\delta)$. The proposer will not offer less (it would be refused) or more (not needed) (p. 329). (By addition, the proposer keeps $1/(1+\delta)$ — added step.)

**Special cases.**
- $\delta\to1$: split is $1/2$ each. The first mover has no edge (p. 329).
- $\delta=0$: split $(0,1)$, the ultimatum game (p. 330).
- $\delta=1/2$: the text states a 2:1 division. The proposer has a claim to the half of the pie that is lost if you refuse (1/2). Of the half that remains, you get half, i.e. 1/4. After two rounds he has collected 1/2 and you 1/4, and we are back to the start, so in each pair of offers he collects twice as much as you (p. 330). By the formula (added step) the responder gets $\frac{1/2}{3/2}=\frac13$ and the proposer $\frac23$.

**Different patience.** The more patient side gets a bigger slice. As the time between offers shrinks, the pie is split in the ratio of waiting costs. A side twice as impatient gets one-third, half as much as the other (p. 330). The authors argue that U.S. politics and media foster impatience, which helps rival nations (p. 330).

*Intuition note:* The more patient side gets a bigger slice; as the time between offers shrinks, the pie is split in the ratio of the waiting costs (p. 330).

## Toy example (ours)
A freelancer and a firm may agree a job. If they agree, it creates value 100. If not, the freelancer earns 20 elsewhere and the firm gets 30 by hiring another person.
1. Sum of BATNAs: 20 + 30 = 50.
2. Pie = 100 − 50 = 50.
3. Equal patience, equal importance: each gets 25 of the pie.
4. Freelancer gets 20 + 25 = 45. Firm gets 30 + 25 = 55. Total 100.
Check with the chapter's logic: if the freelancer's outside option rose to 30, the pie would be 100 − 60 = 40, each gets 20, and the freelancer gets 50. A better BATNA moves the split in your favour.

## Concepts
- [[backward induction]] — solve from the last round, so today's offer matches what waiting would bring (pp. 310–311)
- [[best response]] — each side offers at least what the other could get by waiting, and no more (p. 311)
- [[batna]] (new) — best alternative to a negotiated agreement, the best you get without agreeing (p. 314)
- [[bargaining-pie]] (new) — extra value created by agreement beyond the sum of BATNAs (p. 314)
- [[bargaining-power]] (new) — advantage from the better fallback, patience, or being the proposer (pp. 313, 324, 330)
- [[credible commitment]] — in brinkmanship, a small risk or one more day of waiting is credible, a total threat is not (pp. 318–319)
- [[signaling]] — a strike or taking risk proves low waiting costs, at a cost to efficiency (p. 318)
- [[brinkmanship]] (new) — a threat that leaves some chance of breakdown and rises over time (pp. 318–319)
- [[shadow of the future]] — the cost of waiting is measured by $\delta$ in Rubinstein's model (p. 327)
- [[rubinstein-bargaining]] (new) — alternating offers, no end date, responder gets $\delta/(1+\delta)$ (pp. 326–329)
- [[virtual-strike]] (new) — work and production go on, but neither side is paid (p. 321)

## Canonical instances
- [[hotel-wage-bargaining]] — 101-day season, alternating offers, $505 vs $495 (pp. 310–312)
- [[airfare-triangle-route]] — pie of $1,000 gives $832 and $1,986 (pp. 314–315)
- [[mlb-1980-strike]] — players timed strikes to hurt owners more (pp. 316–317)
- [[meridiana-virtual-strike]] — Italian virtual strike, receipts to charity (p. 322)
- [[nhl-2004-lockout]] — whole season lost (p. 322)
- [[dock-lockout-2002]] — more than $10 billion damage over a $20 million dispute (p. 321)

## Bridges (candidates)
- [structural-analogy] Rubinstein split $\delta/(1+\delta)$ ↔ repeated games: the weight on the future ($\delta$) plays the same role as in cooperation models.
- [structural-analogy] Strike as signaling ↔ signaling: a costly action proves private information about waiting costs.
- [structural-analogy] Virtual strike ↔ mechanism design: change the rules to keep incentives while removing waste.
- [metaphor] Handicap in golf ↔ BATNA: starting advantages offset in a split.

## Questions this raises
- If the receiver might act irrationally on purpose, how should the proposer learn whether it is a bluff?
- How can each side prove a low waiting cost without causing the strike losses?
- What are the real BATNAs in a virtual strike, and does the public relations benefit change them?
- Does the 2:1 result for $\delta=1/2$ still hold when sides differ in patience, and by how much?

## Reading notes
- Printed page numbers equal pdf page numbers (310–330).
- The tables on pp. 311, 312, 323 and 325, the airfare one-way fare table, and some equations are not in the text layer. I did not reconstruct them beyond what the prose states. Images were supplied only for pp. 327–329.
- On p. 328 the first bound is printed as "L > δ(1–δ(1–L))" (text layer and image agree). The simplified result "L ≥ δ(1−δ)/(1−δ²) = δ/(1+δ)" appears only in the image; it is missing from the text layer. The algebra between them is my added step.
- The page 330 formula for $\delta=1/2$ is not in the text layer. The 2:1 split is stated in prose. I computed 2/3 vs 1/3 as an added step.
- The case study says management offers labour "$101" on day one. The units are as printed. Labour's $1 on the last day and $2 the day before (p. 324) is consistent with $101 on day one of 101 days (my inference).
- The airfare case (p. 314) first says one company is in Dallas, then calls it Houston; I followed Houston, as the rest of the text does.
