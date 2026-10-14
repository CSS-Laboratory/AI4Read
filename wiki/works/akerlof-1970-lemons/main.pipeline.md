---
id: akerlof-1970-lemons/main
work: akerlof-1970-lemons
unit: paper
pages: 488–500
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
# The Market for "Lemons": Quality Uncertainty and the Market Mechanism

## L0 — One line
When sellers know a good's quality but buyers see only the average, bad goods can drive good ones out, and the market may shrink or vanish.

## L1 — The gist (≤ 120 words)
Akerlof asks what happens in markets where goods differ in quality and sellers know more than buyers. In a used-car model buyers pay for average quality, so owners of good cars cannot get a fair price and good cars may not be traded. Average quality falls, and with the numbers chosen no trade occurs at any price, although trade would help both sides. The same logic is applied to insurance for the old, hiring of minorities, the cost of dishonesty, and credit markets in poor countries. Guarantees, brand names, chains and licensing are institutions that counteract the problem. Private and social returns differ, so intervention may sometimes help. Trust and quality uncertainty may explain many institutions.

**Prerequisites:** expected value; uniform distribution; linear utility; supply and demand curves.

## L2 — Key ideas (5–10 bullets)
- When buyers judge quality by a market statistic (such as average quality), sellers have an incentive to market poor quality, because the return to good quality goes mainly to the whole group whose statistic is affected. Average quality and market size tend to fall (p. 488).
- Used-car model: buyers cannot tell good cars from bad ones ("lemons"), so one price holds for all cars. Owners of good cars are locked in: they cannot get a good car's true value. Bad cars tend to drive out the good (pp. 489–490).
- In the linear-utility example (each extra car adds the same utility), average quality at price $p$ is $p/2$, and buyers value it at only $3p/4$. No trade occurs at any price, although gains from trade exist (p. 491).
- With symmetric information (everyone knows each car's quality), trade takes place, and utility is higher than under asymmetric information by $N/2$ if $N<Y_2$ (or by $Y_2/2$ if $N>Y_2$) (p. 492).
- Medical insurance for people over 65 follows a strictly analogous pattern, which insurance textbooks call adverse selection (as the price rises, the buyers are increasingly those sure they will need cover). This adds one argument in favor of medicare (pp. 492–494).
- Dishonesty costs more than the cheating itself: it can drive honest trade out. Quality variation and the need for trust may hold back development and shape credit markets (pp. 495–499).
- Guarantees, brand names, chains, licensing and certification counteract quality uncertainty (pp. 499–500).

## L3 — Walkthrough

### I. Introduction (p. 488)
- The paper links quality and uncertainty. Possible applications are the labor market, the costs of dishonesty, and "business in underdeveloped countries is difficult." It also touches money markets, insurability, durables' liquidity and brand names (p. 488).
- If buyers use a market statistic to judge quality, sellers gain by marketing poor quality. The return to good quality accrues mainly to the whole group whose statistic is affected, not to the individual seller. Average quality and market size tend to fall (p. 488).
- Social and private returns differ. So government intervention may, in some cases, raise everyone's welfare. Private institutions may arise too, but they are nonatomistic (not made of many small independent actors), so concentrations of power can develop (p. 488).
- The car market is chosen for concreteness and ease, not for realism (p. 489).

### II. The model with automobiles as an example

**A. The automobiles market (pp. 489–490)**
- Assume four kinds of cars: new or used, good or bad. A bad car is a "lemon." A buyer of a new car knows only that it is good with probability $q$ and a lemon with probability $1-q$; $q$ is the share of good cars produced (p. 489).
- After a time the owner can judge his car better than any buyer. This is asymmetric information (one side knows more than the other). Good and bad cars must still sell at one price, because buyers cannot tell them apart (p. 489).
- A used car cannot be valued like a new one. If it were, owners would trade a lemon for a new car, which has a higher chance of being good. So owners of good cars are locked in. They cannot get the car's true value, nor even the expected value of a new car (p. 489).
- Gresham's law has a modified reappearance. Most traded cars will be lemons, and good cars may not be traded at all (p. 489). The analogy is incomplete. In Gresham's law both parties presumably can tell good money from bad. Here only the seller knows (p. 490).

**B. Asymmetrical information (pp. 490–491)**
- With a continuum of grades, it is possible that the bad drives out the not-so-bad, and so on up to the good, until no market exists (p. 490).
- General form: demand $Q^d = D(p,\mu)$, where $\mu$ is average quality of used cars traded. Both $\mu=\mu(p)$ and supply $S=S(p)$ depend on price. Equilibrium: $S(p)=D(p,\mu(p))$. As price falls, quality normally falls too, and it is possible that nothing trades at any price (p. 490).
- Utility example. Two groups of traders. $M$ is consumption of other goods, $x_i$ is quality of car $i$, $n$ is number of cars (p. 490):
$$U_1 = M + \sum_{i=1}^{n} x_i, \qquad U_2 = M + \sum_{i=1}^{n} \tfrac{3}{2}x_i .$$
- Author's comments: linear utility avoids algebraic complication and isolates the effect of asymmetric information from the usual risk effects. A $k$th car adds as much utility as the first, which is unrealistic, but realism is traded for focus (pp. 490–491).
- Assumptions (p. 491): both groups maximize von Neumann–Morgenstern expected utility. Group one has $N$ cars, quality $x$ uniform on $0\le x\le 2$. Group two has no cars. The price of $M$ is 1. $Y_1,Y_2$ are group incomes, including car-sale income.
- Group one demand (ignoring indivisibilities): $D_1 = Y_1/p$ if $\mu/p>1$; $D_1=0$ if $\mu/p<1$. Supply by group one (the paper prints the label $S_2$) and its average quality, derived from the uniform distribution (p. 491):
$$S_2 = pN/2 \quad (p\le 2) \tag{1}$$
$$\mu = p/2 \tag{2}$$
- Group two: $D_2 = Y_2/p$ if $3\mu/2>p$; $D_2=0$ if $3\mu/2<p$; $S_2=0$ (p. 491).
- Total demand (p. 491): $D=(Y_2+Y_1)/p$ if $p<\mu$; $D=Y_2/p$ if $\mu<p<3\mu/2$; $D=0$ if $p>3\mu/2$.
- Result: at price $p$ average quality is $p/2$, so no trade occurs at any price. Yet at any price between 0 and 3 some group-one traders would sell at a price group two would pay (p. 491). (added step) With $\mu=p/2$, $3\mu/2 = 3p/4 < p$, so $D=0$ for every $p>0$.

*Intuition note:* A price that attracts good cars would have to be high. But a high price makes owners of mediocre cars sell too, so the average quality offered is only half the price. Buyers value that average at only three-quarters of the price.

**C. Symmetric information (p. 492)**
- Contrast: quality is uniform on $0\le x\le 2$ and known to all. Supply: $S(p)=N$ for $p>1$; $0$ for $p<1$. Demand: $(Y_2+Y_1)/p$ for $p<1$; $Y_2/p$ for $1<p<3/2$; $0$ for $p>3/2$.
- Equilibrium:
$$p=1 \ \text{ if } Y_2<N \tag{3}$$
$$p=Y_2/N \ \text{ if } 2Y_2/3<N<Y_2 \tag{4}$$
$$p=3/2 \ \text{ if } N<2Y_2/3 \tag{5}$$
- If $N<Y_2$, utility gain over asymmetric information is $N/2$. If $N>Y_2$, group two's income cannot buy all cars, and the gain is $Y_2/2$ (p. 492).
- If both groups share the same probabilistic estimates of each car's quality (these may vary by car), (3)–(5) still hold, but $p$ is then the expected price of one quality unit (p. 492).

### III. Examples and applications

**A. Insurance (pp. 492–494)**
- People over 65 find it hard to buy medical insurance. Author's answer: as price rises, buyers are those increasingly sure they need it, since applicants judge their risk better than the insurer. Average applicant health worsens as price rises, so no sales may occur at any price. This is strictly analogous to the car case (pp. 492–493).
- Insurance textbooks (quoted by the author) describe a "severe problem of adverse selection" at these ages. Adverse selection is the term for this effect (p. 493).
- Data from a 1956 survey (2,809 families, 8,898 persons): hospital insurance coverage falls from 63% (ages 45–54) to 31% (over 65). Males 55–64 have average medical expenses of \$88; males over 65, \$77. Non-insured spending rises from \$66 to \$80; insured spending falls from \$105 to \$70. The author finds it "tempting" to conclude that insurers are wary of older people (p. 493).
- Adverse selection is potentially present in all insurance lines. Group insurance picks out the healthy, since health is a precondition for employment. So insurance is least available to those who need it most (pp. 493–494).
- Argument for medicare: it is quite possible that every individual would pay the expected cost of his medicare, yet no insurer can sell at any price because it attracts too many lemons. The author says this is analogous to the classroom argument for public roads (p. 494).
- Footnote: Arrow emphasizes "moral hazard" rather than adverse selection. In its strict sense, moral hazard is equally disadvantageous for government and private programs; in its broader sense, which includes adverse selection, it gives a decided advantage to government insurance programs (p. 493, n. 1).

**B. Employment of minorities (pp. 494–495)**
- Refusing to hire minority members may reflect profit maximization, not irrationality or prejudice, because race may serve as a statistic for social background, schooling and job capability (p. 494).
- Good schooling could substitute for this statistic if the certifying school is credible. Unreliable slum schools reduce their students' economic possibilities (p. 494).
- An employer may rationally decline to hire any members of a disadvantaged group for responsible posts. The author connects this to Stigler's remark about Fermi and Von Neumann (p. 495).
- Rewards for work in slum schools tend to accrue to the group, by raising its average quality, rather than to the individual. Only insofar as information in addition to race is used is there any incentive for training. Cost-benefit analysis of training programs may miss these external benefits (p. 495).

**C. The costs of dishonesty (pp. 495–496)**
- Dishonest sellers tend to drive honest dealing out of the market. The cost of dishonesty is therefore not only the amount cheated but also the lost legitimate business (p. 495).
- In the model economy, misrepresenting car quality costs 1/2 unit of utility per car. It also reduces the used-car market from $N$ to 0. So the cost can be evaluated "at least in theory" (pp. 495–496).
- Evidence offered that quality variation is greater in underdeveloped areas: about 85% of Indian exports are under quality control; rice sellers may add stones (p. 496). The author speaks of "considerable evidence" and says that comparing street markets with supermarkets "suggests" quality variation is a greater problem in the East.
- The merchant's skill is identifying quality. People who can identify and guarantee quality may profit up to the gap between type-two buyers' price and type-one sellers' price. The same skill is needed in production, which may be one reason merchants become entrepreneurs (p. 496).
- If entrepreneurship is scarce, product variation impedes development in two ways. The trade pay-off diverts would-be entrepreneurs from production. And entrepreneurial time per unit of output rises with quality variation (p. 496).

**D. Credit markets in underdeveloped countries (pp. 497–499)**
- Indian managing agencies controlled 65.7% of net worth and 66% of total assets of public limited companies. Promoters turned to them for their reputation. Firms are largely classified by communal origin; the author gives a table of 1911, 1931 and 1951 counts (p. 497, n. 5).
- Where outside investors are likely to be bilked, either (1) firms with an honest reputation earn a monopoly rent, or (2) finance stays within communal groups that can use communal or familial ties to encourage honesty (pp. 497–498).
- Why landlords' savings did not go into industry is hard to say: fear of other communities' ventures, high consumption, or low returns (p. 498).
- Moneylenders charge 15, 25, even 50%, while big city banks have prime rates of 6, 8 and 10%. The author's answer: credit is granted only where the lender can enforce the contract easily or knows the borrower personally. A middleman who tries to arbitrage between the two rates is apt to attract all the lemons and thereby make a loss (pp. 498–499).
- Supporting accounts: Darling on the moneylender's intimate knowledge, a Hong Kong shopkeeper's caution with unknown borrowers, and losses of Iranian cotton ginners in early years from poor local knowledge (p. 499).

### IV. Counteracting institutions (pp. 499–500)
- Guarantees: the seller, not the buyer, bears the risk (p. 499).
- Brand names indicate quality and let the consumer retaliate by cutting future purchases. New products are often given old brand names (pp. 499–500).
- Chains: chain restaurants appear on interurban highways where customers are seldom local. The author's reason: chains offer a better hamburger than the average local restaurant, while a local customer who knows his area can usually choose a place he prefers (p. 500).
- Licensing and certification (doctors, lawyers, barbers, diplomas, degrees) reduce quality uncertainty. Education and labor markets have their own "brand names" (p. 500).

### V. Conclusion (p. 500)
- Models in which trust matters: informal, unwritten guarantees are preconditions for trade and production. When they are indefinite, business suffers, as in the "generalized Gresham's law." Game theorists have explored this (Prisoner's Dilemma), but it is usually not part of the Arrow–Debreu approach to uncertainty. Difficulty in telling good from bad quality may explain many institutions (p. 500).

## Toy example (ours, not from the text)
Five cars with qualities $x = 0,\,0.5,\,1,\,1.5,\,2$. A seller values his car at $x$; a buyer values it at $1.5x$. A seller offers his car if $p\ge x$. Buyers cannot see quality and will pay at most $1.5\times$ the average quality offered.

| price $p$ | cars offered | average quality | buyer's max price $1.5\times$avg | trade? |
|---|---|---|---|---|
| 2 | all 5, sum 5 | 5/5 = 1 | 1.5 < 2 | no |
| 1.5 | 4 cars, sum 3 | 0.75 | 1.125 < 1.5 | no |
| 1 | 3 cars, sum 1.5 | 0.5 | 0.75 < 1 | no |
| 0.5 | 2 cars, sum 0.5 | 0.25 | 0.375 < 0.5 | no |

Only the worthless car (price 0) could trade, which yields no gain. If quality were observable, each car could sell at a price between $x$ and $1.5x$, with gain $0.5x$. Total gain would be $0.5(0+0.5+1+1.5+2)=2.5$. With hidden quality the gain is 0.

## Concepts
- [[adverse selection]] — hidden quality means the worst types dominate offers; the term is taken from insurance textbooks (pp. 492–493)
- [[asymmetric information]] — sellers know a good's quality better than buyers (p. 489)
- [[market failure / externality]] — private and social returns differ, e.g. quality returns accrue to the group (pp. 488, 495)
- [[moral hazard]] — mentioned only in footnote 1, where Arrow is said to emphasize it; in its broader sense it includes adverse selection (p. 493)
- [[incomplete contracts]] — loosely: informal unwritten guarantees are preconditions for trade, and business suffers where they are indefinite (p. 500)
- [[quality unraveling / generalized Gresham's law]] (new) — bad goods drive out good, possibly to no market (pp. 489–490)
- [[statistic-based discrimination]] (new) — judging individuals by a group statistic such as race; the author does not use a name (p. 494)
- [[reputation and certification]] (new) — brand names, guarantees, licensing as counteracting institutions (pp. 499–500)

## Canonical instances
- [[used-car lemons market]] — hidden quality, no trade at any price with uniform quality (pp. 489–491)
- [[medical insurance over 65]] — as the price rises, applicants' average health worsens, so no insurance sales may take place at any price (pp. 492–494)
- [[Indian moneylenders and managing agencies]] — credit limited to those with personal knowledge or communal ties (pp. 497–499)

## Bridges (candidates)
- [structural-analogy] Lemons unraveling ↔ bank run equilibrium: both are self-reinforcing collapses of a market driven by participants' expectations.
- [structural-analogy] Group return to quality ↔ social dilemma: each seller gains from lowering quality while the group loses.
- [metaphor] Gresham's law ↔ quality unraveling: the author himself calls the analogy "instructive, but not complete" (p. 490).

## Questions this raises
- If quality is uniform on a different range, or sellers' and buyers' valuations are closer, does trade collapse completely or only partly?
- Do guarantees and brand names themselves cost something, and who bears those costs?
- How do we test that insurance or credit market failures stem from adverse selection rather than other causes?
- What happens when the market-statistic group is not fixed but gets chosen by agents?

## Reading notes
- Printed pages 488–500; pdf page 1 is a JSTOR cover sheet with no printed number. Printed = pdf + 486 for pdf 2–14.
- The text layer is garbled in places (words run together; $\mu$ appears as "p" on p. 490); I checked the images for pp. 490–492.
- The supply formula (1) on p. 491 is labeled $S_2$ in the image although it describes group one's supply, and group two's supply is also written $S_2=0$. This looks like a misprint (my inference).
- The page 492 conditions (3)–(5) are copied as printed.
- Footnote numbering restarts at 1 on p. 496. Page 497 gives a data table in a footnote, which I summarised only briefly. The p. 498 interest-rate table is not reproduced.
