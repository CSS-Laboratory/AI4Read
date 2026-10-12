---
id: akerlof-1970-lemons/main
work: akerlof-1970-lemons
unit: paper
pages: 488–500
fields: [economics-finance, decision-game-theory, information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-12
---

# The Market for "Lemons": Quality Uncertainty and the Market Mechanism (Akerlof, 1970)

## L0 — One line
When sellers know a product's quality and buyers do not, bad goods can push good goods out of the market, and the market can shrink or even disappear.

## L1 — The gist (≤ 120 words)
Akerlof asks what happens in a market where buyers cannot judge quality before buying, but sellers can. Buyers will only pay a price that reflects *average* quality. At that price, owners of above-average goods hold back, so average quality falls, so the price falls, and so on. In his used-car example with uniform quality, no trade happens at any price, even though every car is worth more to buyers than to its owner. The same logic explains why people over 65 cannot buy medical insurance, why dishonesty is so costly, and why credit is expensive in poor countries. It also explains institutions such as guarantees, brand names, chains and licences, which exist to counter quality uncertainty.

## L2 — Key ideas (5–10 bullets)
- **Sellers know more than buyers.** After using a car, the owner knows its quality better than any buyer can, so good and bad cars must sell at one price (p. 489). This is the "asymmetry in available information" that drives everything else.
- **Bad drives out good.** Because price cannot depend on a car's true quality, owners of good cars cannot get what their cars are worth, and mostly lemons are traded. Akerlof calls this a modified Gresham's law (pp. 489–490).
- **The unraveling can be complete.** With many grades, the bad can drive out the not-so-bad, and so on down the line, until "no market exists at all" (p. 490).
- **A worked model shows total collapse.** With uniform quality on $[0,2]$ and buyers valuing cars at $3/2$ of their quality, the average quality offered at price $p$ is $p/2$, buyers will pay at most $3p/4 < p$, and no trade occurs at any price (pp. 490–491).
- **Information has a measurable welfare cost.** Under symmetric information, trade gains are $N/2$ (or $Y_2/2$ if buyers' income is short); under asymmetry they are zero (p. 492).
- **The same principle explains insurance.** Higher premiums attract only the people most sure they will claim, so cover for the over-65s may not exist at any price; this is the argument Akerlof gives for Medicare (pp. 492–494).
- **Dishonesty costs more than the cheat.** The main cost is the honest trade that is driven out, which in the model is $1/2$ unit of utility per car and a used-car market that shrinks from $N$ to $0$ (pp. 495–496).
- **Reputation, kinship and credit.** In poor-country credit markets, lenders lend only where they can enforce contracts or know the borrower, which favors communal groups and local moneylenders (pp. 497–499).
- **Institutions fight back.** Guarantees, brand names, chains and licences/certificates all reduce quality uncertainty, but they are "nonatomistic" and can create concentrations of power (pp. 488, 499–500).
- **Private and social returns differ.** A seller's honesty or training raises the group's average, not only his own return, so the market underinvests in quality and government action may help (pp. 488, 495).

## L3 — Walkthrough

### I. Introduction (p. 488)
Akerlof starts from a simple fact: goods come in many grades, and the buyer often cannot tell which grade he is getting. He lists what the idea will be used for: labor-market institutions, the costs of dishonesty (which he says is "a struggling attempt" to give structure to the claim that business in underdeveloped countries is difficult), money markets, insurability, the liquidity of durables, and brand names (p. 488).

The central mechanism is stated in advance. Buyers often judge quality from a *market statistic* (for example the average quality of the group). A seller's good quality raises the group's statistic, so most of the return goes to the whole group and not to him. Each seller therefore has an incentive to sell poor quality. The result is lower average quality and a smaller market (p. 488).

Two consequences follow. First, social and private returns differ, so government intervention may help everyone. Second, private institutions may arise to capture the gains, but these are "nonatomistic" (not made up of many small independent actors) and so can become concentrations of power with their own harms (p. 488). The automobile market is used only as a "finger exercise", chosen for being concrete and easy to follow, not because it is important or realistic (p. 489).

> **Intuition note.** A good seller is paid as if he were average. If you are above average you subsidize the others, so you leave. That departure makes the average worse for those who remain.

### II. The model with automobiles as an example

**A. The automobiles market (pp. 489–490).**
Suppose there are four kinds of cars: new or used, good or lemon. A buyer of a new car does not know which he gets, but knows that it is good with probability $q$ and a lemon with probability $1-q$, where $q$ is the share of good cars produced (p. 489).

After owning the car for a while, the owner forms a better estimate of its quality. Now the sellers know more than the buyers do. Because buyers cannot tell good from bad, all used cars of the same type must sell at one price (p. 489).

That price cannot equal the price of a new car. If it did, an owner of a lemon would swap it for a new car, which has a higher chance $q$ of being good and a lower chance of being bad. So the used-car price is lower than the new-car price. Therefore the owner of a good used car is "locked in": he cannot get the true value of his car, and he cannot even get the expected value of a new car (p. 489).

This revives Gresham's law (bad money drives out good). Most cars traded will be lemons, and good cars may not be traded at all (pp. 489–490). Akerlof notes that the analogy is only partial. In Gresham's law both sides can tell good money from bad, and the exchange rate is fixed. In the car market, only the seller can tell, and that hidden knowledge is the whole problem (p. 490).

> **Intuition note.** The new-car/used-car price gap is explained here without any "joy of a new car". It is the price of the buyer's ignorance (p. 489).

**B. Asymmetrical information (pp. 490–491).**
With many grades of quality the problem can be worse. The bad may drive out the not-so-bad, which drive out the medium, and so on, until no market exists (p. 490).

Let $p$ be the price of a used car and $\mu$ the average quality of used cars traded. Demand depends on both, $Q^d = D(p,\mu)$. Supply depends on price, $S = S(p)$, and so does average quality, $\mu = \mu(p)$. In equilibrium supply equals demand at the average quality that the price itself produces:
$$S(p) = D\big(p,\mu(p)\big).$$
Normally, as price falls, quality falls too, and it is quite possible that nothing is traded at any price (p. 490).

*The utility example (pp. 490–491).* There are two groups of traders. Group one has utility
$$U_1 = M + \sum_{i=1}^{n} x_i,$$
and group two has
$$U_2 = M + \sum_{i=1}^{n} \tfrac{3}{2}\,x_i,$$
where $M$ is consumption of goods other than cars, $x_i$ is the quality of the $i$-th car, and $n$ is the number of cars (p. 490). So group two values any car at $3/2$ times its quality; it values cars more than group one does, and trade would be efficient.

Akerlof makes three comments on these functions (pp. 490–491). (1) Linear utility avoids needless algebra, for example with log utility. (2) Linear utility lets him isolate the effect of asymmetric information; with concave utility the usual risk effects would be mixed in. (3) A $k$-th car adds as much utility as the first, which is unrealistic but keeps the focus.

Assumptions (p. 491): both groups maximize expected utility (von Neumann–Morgenstern); group one owns $N$ cars with quality $x$ uniformly distributed on $0 \le x \le 2$; group two owns no cars; the price of "other goods" $M$ is $1$. Let $Y_1$ and $Y_2$ be the incomes (including sales proceeds) of the two groups.

*Demand of group one.* A group-one trader buys a car only if the average quality is worth more than its price:
$$D_1 = Y_1/p \ \text{ if } \mu/p > 1, \qquad D_1 = 0 \ \text{ if } \mu/p < 1.$$

*Supply of group one.* A car of quality $x$ is worth $x$ to its owner, so he sells if the price is at least $x$ (added step). With $x$ uniform on $[0,2]$, the share of cars with $x \le p$ is $p/2$ (for $p \le 2$), so
$$S = pN/2 \quad (p \le 2), \tag{1}$$
and the average quality of cars offered is the mean of a uniform variable on $[0,p]$ (added step):
$$\mu = p/2. \tag{2}$$
(The paper labels the supply in (1) as $S_2$; it is group one's supply, see Reading notes.)

*Demand and supply of group two.* Group two values a car of average quality $\mu$ at $3\mu/2$, so
$$D_2 = Y_2/p \ \text{ if } 3\mu/2 > p, \qquad D_2 = 0 \ \text{ if } 3\mu/2 < p, \qquad S_2 = 0.$$

*Total demand* (p. 491):
$$D(p,\mu) = \begin{cases} (Y_2+Y_1)/p & p < \mu \\ Y_2/p & \mu < p < 3\mu/2 \\ 0 & p > 3\mu/2. \end{cases}$$

*The collapse.* Substitute $\mu = p/2$ from (2). Group one never buys, since $\mu/p = 1/2 < 1$ (added step). Group two buys only if $3\mu/2 = 3p/4 > p$, which is never true for $p>0$ (added step). So demand is zero at every price and "at no price will any trade take place at all", although at any price there are type-one traders willing to sell at a price that type-two traders would pay (p. 491).

> **Intuition note.** Each possible price tells buyers who will sell. A high price brings in more good cars but also more bad ones, and the average at price $p$ is only $p/2$. Group two's premium of $3/2$ is not big enough to cover this fall in quality (it would need to reach $2$; see Questions). So buyers will not pay the price that would bring out the cars they want.

**C. Symmetric information (p. 492).**
Compare the case where both sides know only that quality is uniform on $[0,2]$. A group-one owner now values any car at the expected quality $1$, so he sells at any price above $1$:
$$S(p) = N \ (p>1), \qquad S(p) = 0 \ (p<1).$$
Demand (group two values the average car at $3/2$):
$$D(p) = (Y_2+Y_1)/p \ (p<1), \quad D(p) = Y_2/p \ (1<p<3/2), \quad D(p) = 0 \ (p>3/2).$$
Equilibrium (p. 492):
$$p = 1 \ \text{ if } Y_2 < N, \tag{3}$$
$$p = Y_2/N \ \text{ if } 2Y_2/3 < N < Y_2, \tag{4}$$
$$p = 3/2 \ \text{ if } N < 2Y_2/3. \tag{5}$$
(Added step for (4): when $1<p<3/2$ all $N$ cars are supplied, so $Y_2/p = N$ gives $p = Y_2/N$, which lies in $(1, 3/2)$ exactly when $2Y_2/3 < N < Y_2$.)

*Welfare comparison.* If $N < Y_2$, there is a gain in utility of $N/2$ over the asymmetric case. (Added step: every car moves from a holder who values it at $1$ to one who values it at $3/2$, a gain of $1/2$ each.) If $N > Y_2$, group two's income cannot buy all the cars, and the gain is $Y_2/2$ (p. 492).

Finally, if both groups share the same probabilistic estimates of each car's quality, even though estimates differ from car to car, then (3)–(5) still hold with $p$ read as the expected price of one quality unit (p. 492).

> **Intuition note.** The only difference between the two cases is who knows what. Quality, tastes and incomes are identical, yet the market is full under symmetry and empty under asymmetry. The gap $N/2$ is the dollar value of hidden information in this model.

### III. Examples and applications

**A. Insurance (pp. 492–494).**
People over 65 have great difficulty buying medical insurance. Why doesn't the price rise to match the risk? Akerlof's answer is that as the price rises, those who insure are increasingly the people who are sure they will need it, because applicants can judge their own risk better than the insurer can. The average health of applicants gets worse as the price rises, "with the result that no insurance sales may take place at any price". This is "strictly analogous" to the car case (pp. 492–493).

He cites insurance textbooks, which describe "adverse selection" at these ages, and survey data from 1956 (2,809 families, 8,898 persons). Hospital insurance coverage falls from 63% for ages 45–54 to 31% for those over 65. Average medical expenses are \$88 for men aged 55–64 and \$77 for men over 65. Uninsured spending rises from \$66 to \$80 across these age groups, while insured spending falls from \$105 to \$70. He reads this as evidence that insurers are wary of the old (p. 493).

Adverse selection is potentially present in all insurance, for example when healthy policyholders drop their cover as premiums mount with age (p. 493). Group insurance, the most common type in the United States, picks out the healthy because good health is needed for employment; so insurers do their own "adverse selection", and cover is least available to those who need it most (pp. 493–494).

The result is an argument for Medicare. It is quite possible that every individual would pay the expected cost of his own cover, yet no insurer can sell him a policy, because at any price it would attract too many "lemons". Akerlof compares the welfare logic to the usual classroom argument for public spending on roads (p. 494). In a footnote he adds that Arrow (1963) stressed "moral hazard" rather than adverse selection; in the strict sense moral hazard hurts government and private programs equally, but in the broad sense that includes adverse selection it favors government programs (p. 493, n. 1).

**B. The employment of minorities (pp. 494–495).**
Akerlof applies the "Lemons Principle" to hiring. An employer may refuse to hire members of a minority group for certain jobs, and this need not come from irrationality or prejudice, but may be profit-maximizing: race may act as a statistic for social background, quality of schooling and general job ability (p. 494).

Good schooling could replace such a statistic, because schools grade students and so give a better indicator. But the certifying body must be credible. The unreliability of slum schools lowers the economic prospects of their students (p. 494). Employers may rationally decline to hire any member of such groups for responsible jobs because it is hard to tell good from bad candidates (p. 495).

The rewards of working in slum schools accrue to the group, by raising its average quality, and not to the individual, so only if information beyond race is used is there an incentive to train. Akerlof also worries that cost-benefit analysis of anti-poverty programs (the Office of Economic Opportunity) would miss these external benefits (p. 495).

**C. The costs of dishonesty (pp. 495–496).**
Consider a market where quality may be honestly or dishonestly represented. The presence of dishonest sellers tends to drive honest dealing out of the market, as lemons do. The cost of dishonesty is therefore not only the amount the buyer is cheated out of, but also the loss from legitimate business being driven out (p. 495). In the model economy, misrepresenting car quality costs $1/2$ unit of utility per car and cuts the used-car market from $N$ to $0$, so the cost can be evaluated directly "at least in theory" (pp. 495–496).

*Evidence on quality variation in poor countries* (p. 496): about 85% of Indian exports are covered by some quality control under the Export Quality Control and Inspection Act of 1963; Indian housewives must pick stones, of the same colour and shape, out of bazaar rice; and street markets are compared with the canned uniformity of the American supermarket.

*Merchants and entrepreneurs* (p. 496): the key merchant skill in this picture is identifying quality. Someone who can identify and guarantee the quality of used cars can earn up to the gap between type-two buyers' price and type-one sellers' price. Such skills are equally needed in production, to judge inputs and certify outputs, which is "one (added) reason" why merchants often become the first entrepreneurs (Japan is the best-documented case). If entrepreneurship is scarce, quality variation impedes development in two ways: the payoff to trade diverts would-be entrepreneurs from production, and more entrepreneurial time is needed per unit of output when quality varies more (p. 496).

**D. Credit markets in underdeveloped countries (pp. 497–499).**
*(1) Managing agencies.* In India, "managing agencies" controlled 65.7% of the net worth of public limited companies and 66% of total assets. Promoters turned to an established agency because of its reputation, which encouraged confidence and investment (p. 497). These agencies are dominated by caste or communal groups. A footnote table counts firms by community: British 281, 416 and 382 firms in 1911, 1931 and 1951; Marwaris rise from 6 in 1931 to 96 in 1951; totals are 341, 510 and 619 (p. 497, n. 5). In an environment where outside investors are likely to be cheated, either firms build a reputation for honesty that earns monopoly rent, or finance stays within communal groups that can use communal or family ties to enforce honesty (pp. 497–498). Akerlof says it is very hard to tell whether rich landlords' savings stayed out of industry because of fear of other communities, high consumption, or low returns (p. 498). British-owned agencies had more mixed equity holders than Indian-controlled ones (p. 498).

*(2) Moneylenders.* Local moneylenders charge 15, 25 or even 50 per cent, while big central-city banks have prime rates of 6, 8 and 10 per cent (p. 498). Akerlof's explanation is that credit is given only where the lender has (1) an easy way to enforce the contract or (2) personal knowledge of the borrower. A middleman who tries to arbitrage between the moneylender's rate and the central bank's rate "is apt to attract all the lemons" and lose money (p. 499). He supports this with Darling's account of the village moneylender's intimate knowledge of clients, a Hong Kong fishing-village shopkeeper who gives credit only to people he knows, and Iranian cotton ginners who expect large losses on loans in their first years because they know the local scene poorly (p. 499).

> **Intuition note.** In credit markets the "good car" is a reliable borrower. A lender who cannot tell reliable from unreliable must price for the average, and then reliable borrowers drop out. Local lenders who can tell borrowers apart escape the problem, which is why they hold their market even at very high rates.

### IV. Counteracting institutions (pp. 499–500)
Several institutions arise to reduce quality uncertainty:
- **Guarantees.** Most consumer durables carry guarantees, and the model implies that the risk is borne by the seller and not the buyer (p. 499).
- **Brand names.** They indicate quality and also give the buyer a way to retaliate, by cutting future purchases. New products are often given old brand names, which reassures buyers (pp. 499–500).
- **Chains.** Chain restaurants appear mostly on interurban highways, where customers are seldom local. Well-known chains offer a better hamburger than the average local restaurant, but a local customer knows his area and can usually choose a place he prefers (p. 500).
- **Licensing and certification.** Licensing of doctors, lawyers and barbers, and diplomas up to the Ph.D. (even, to some degree, the Nobel Prize), certify proficiency. Education and labor markets "have their own brand names" (p. 500).

### V. Conclusion (p. 500)
These are models in which "trust" matters: informal unwritten guarantees are preconditions for trade and production, and where they are weak, business suffers, as shown by the generalized Gresham's law. Game theorists have studied this aspect of uncertainty (for example in the Prisoner's Dilemma), but it has usually not been part of the traditional Arrow–Debreu approach to uncertainty. The difficulty of telling good from bad quality is inherent in business and may explain many economic institutions (p. 500).

## Toy example
*(Ours, not from the text.)* Four used cars have qualities $x = 1, 2, 3, 4$ (thousand dollars of value to the owner). Buyers value a car at $1.4x$, so every car is worth more to a buyer than to its owner, and full trade would be efficient. Buyers cannot see $x$.

- **Symmetric information.** Everyone knows each car's own quality. All four cars trade at prices between $x$ and $1.4x$. Total gain from trade is $0.4 \times (1+2+3+4) = 4$.
- **Asymmetric information.** Try price $p = 4$: all four owners sell (each has $x \le 4$), average quality is $2.5$, buyers value that at $1.4 \times 2.5 = 3.5 < 4$. No buyer pays 4. Try $p = 3$: owners of cars 1, 2, 3 sell, average $2$, buyers value $2.8 < 3$. Still no. Try $p = 2.05$: only cars 1 and 2 sell (average $1.5$), buyers value $2.1 > 2.05$. So trade occurs at a price in about $(2, 2.1]$, but only for cars 1 and 2.
- **Result.** Cars 3 and 4, the good cars, never trade, although buyers value them at $4.2$ and $5.6$. The gain from trade falls from $4$ to $1.4(1+2) - (1+2) = 1.2$. The difference, $2.8$, is the cost of the hidden information. With a continuum of qualities (as in the paper) the unraveling is complete and nothing trades.

## Concepts
- [[asymmetric-information]] — one side (the seller) knows the quality, the other (the buyer) does not (p. 489)
- [[adverse-selection]] — at a given price, the sellers who stay in the market are those with the worst quality, so average quality falls as price falls and the market can unravel (pp. 490, 493)
- [[market-failure-externality]] — private and social returns differ, because one seller's quality or honesty affects the group's statistic (pp. 488, 495)
- [[equilibrium]] — price at which supply equals demand, with demand depending on the average quality that the price itself produces, $S(p) = D(p,\mu(p))$ (p. 490)
- [[moral-hazard]] — mentioned as the different problem stressed by Arrow, in contrast to adverse selection (p. 493, n. 1)
- [[screening]] — insurers and employers sort applicants themselves (insurers "screen"), as a response to hidden quality (pp. 493–494)
- [[signaling]] — guarantees, brand names, licences and diplomas as ways to reveal or certify quality (pp. 499–500); Akerlof does not model the cost of signals
- [[incomplete-contracts]] — informal, unwritten guarantees ("trust") are preconditions of trade where contracts cannot specify quality (p. 500)
- [[market-unraveling]] (new) — the chain "bad drives out not-so-bad drives out medium…" that ends in no market (p. 490)
- [[statistical-discrimination]] (new) — judging an individual by a group statistic when individual quality cannot be observed (pp. 494–495)
- [[quality-certification]] (new) — a credible third party (school, licence, brand) that makes quality visible (pp. 494, 500)
- [[cost-of-dishonesty]] (new) — the loss from honest trade driven out, beyond the amount of cheating itself (p. 495)

## Canonical instances
- [[market-for-lemons-used-cars]] — hidden quality drives good cars out; with uniform quality on $[0,2]$ and a buyer premium of $3/2$, no trade at any price (pp. 489–491)
- [[insurance-over-65]] (new) — as price rises, only the sure-to-claim buy cover, so no policy may be sold at any price; the argument for Medicare (pp. 492–494)
- [[india-moneylender-vs-bank]] (new) — local lenders charge 15–50% while city banks' prime is 6–10%, because an arbitrageur would attract "all the lemons" (pp. 498–499)
- [[chain-restaurants-on-highways]] (new) — chains on interurban roads, where customers are non-local, as a brand-name response to quality uncertainty (p. 500)

## Bridges (candidates)
- [same-math] Akerlof's adverse selection and Spence-style signaling ↔ decision-game-theory: Bayesian games with incomplete information — the seller's type (quality) is private, and the buyer's belief must match the distribution of types who choose to trade.
- [same-math] Average quality of sellers at price $p$, $E[x \mid x \le p] = p/2$ ↔ information-theory / Bayesian updating: conditioning on a selection event — the act of selling is a signal about quality, and the price changes who selects in; the same truncated-expectation calculation appears in the winner's curse in auctions.
- [structural-analogy] Pooling at one price ↔ information-theory: a lossy channel from quality to price — many quality levels map to one price, so the price carries no information about an individual car; separation (guarantees, certificates) restores a channel.
- [structural-analogy] Quality externality on the group statistic (p. 488) ↔ decision-game-theory: social dilemma / tragedy of the commons — each seller gains by cutting quality, and the group's reputation is the shared resource that is depleted.
- [structural-analogy] Generalized Gresham's law ↔ evolutionary dynamics / selection: replicator-style dynamics where the worse type's share rises because the environment rewards it.
- [metaphor] Lemons ↔ online information and content markets (misinformation research): if readers cannot judge quality before use, low-quality content may crowd out high-quality content; no model in the paper supports this, it is a candidate analogy only.

## Questions this raises
1. In the model, group two's premium is $3/2$. What premium $k$ is needed for the market not to collapse? (Added step: with $\mu = p/2$, group two buys iff $k\,p/2 \ge p$, so $k \ge 2$; below that, unraveling is complete.)
2. If sellers can take a costly action to reveal quality (education, a warranty), when does a separating outcome appear, and who pays? (Spence, 1973, takes this up.)
3. Which of the "counteracting institutions" actually restore trade, and which just move the problem to the certifier? Akerlof himself warns that these institutions can concentrate power (p. 488).
4. Does the unraveling story fit markets where quality is revealed only after use but can be repeated (reviews, ratings, repeat purchase)? Brand names give buyers a way to retaliate (p. 500), which hints at a role for repeated play.

## Reading notes
- **Source text is OCR with missing word spaces** (for example "goodsposes interestingand importantproblemsfor"). I checked the equations against the PDF images of printed pages 489–492; all equations above follow the printed page.
- **Garbled symbols in the OCR** on p. 490: $\mu$ appears as "A", "u" or "y", and "$\mu = \mu(p)$" appears as "p=j (p)". The PDF shows $\mu = \mu(p)$. The utility sums on p. 490 are rendered as "$\sum_{i=1}^{n}$" in the PDF.
- **Printing errors in the source.** Eq. (1) on p. 491 labels group one's supply $S_2$; the context ($S_2 = 0$ for group two a few lines below) shows it should be $S_1$. The closing sentence of II.B on p. 491 says "any given price between 0 and 3"; this presumably refers to group two's maximum willingness to pay ($3/2 \times 2 = 3$), but eq. (1) limits supply to $p \le 2$, so the range is loose.
- **Promised but not developed.** The introduction (p. 488) lists "the liquidity of durables" as an application; no section covers it. The "structure of money markets" is covered only through the credit-market section III.D.
- **Tables garbled.** The interest-rate table in n. 7 (p. 498) has OCR fractions such as "37 Y2" (read as $37\tfrac12$), "184" and "18 8/4" (read as $18\tfrac34$). I did not use the table's values beyond the rate ranges Akerlof gives in the text. Footnote 5 on p. 494 and footnote 2 on p. 500 have small OCR errors.
- **Tone of section III.B.** It is a 1970 theoretical argument about hiring decisions when applicant quality is hidden; this digest reports it as the author's model and does not endorse its empirical claims. The paper gives no data for it.
- **Sections and terms.** The paper uses the term "adverse selection" only through insurance textbooks and in III.A; the car model itself is introduced under "asymmetrical information" (pp. 490, 493).
- Footnote 1 on p. 493 (Arrow, moral hazard) is summarized; other footnotes are used only for numbers and quotations of the cited sources.
