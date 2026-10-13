---
id: akerlof-1970-lemons/main
work: akerlof-1970-lemons
unit: paper
pages: 488-500
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
---

# The Market for "Lemons": Quality Uncertainty and the Market Mechanism

## L0 — One line
When sellers know a good's quality but buyers do not, bad goods can drive good goods out of the market, and the market may shrink or disappear entirely.

## L1 — The gist (≤ 120 words)
Akerlof asks what happens when goods differ in quality, sellers know the quality, and buyers see only an average. A buyer will pay only for average quality. That price is too low for owners of good goods, so they withdraw. Average quality falls, the price falls again, and the process can end with no trade at all (pp. 489–491). In his used-car example, trade stops even though every car is worth more to some buyer than to its owner (p. 491). He applies the idea to health insurance for the old, to minority employment, to the costs of dishonesty, and to credit markets in poor countries (pp. 492–499). Guarantees, brands, chains and licences are institutions that offset the problem (pp. 499–500).

## L2 — Key ideas (5–10 bullets)
- **Quality uncertainty with asymmetric information.** After owning a car for a while, the owner knows its quality better than any buyer. Good and bad cars must still sell at one price (p. 489). This asymmetry is the source of the problem.
- **Bad drives out good.** Akerlof calls this a modified Gresham's law. Used cars cannot be valued like new ones, and owners of good cars are "locked in" (pp. 489–490). The analogy is not exact: in Gresham's law both sides can tell good money from bad (p. 490).
- **The market can vanish.** Price lowers average quality, which lowers demand, and so on. With many quality grades the sequence runs "bad driving out the not-so-bad", until "no market exists at all" (p. 490).
- **Worked model.** With two trader groups and uniform quality, average quality at price $p$ is $\mu=p/2$. Buyers value quality at most $3\mu/2=3p/4<p$, so no trade happens at any price (p. 491). Under symmetric information, trade happens and gains $N/2$ in utility (p. 492).
- **Private and social returns differ.** Returns to quality accrue to the whole group behind the market statistic, not to the individual seller. This is an externality, and government or private institutions may raise everyone's welfare (p. 488).
- **Applications.**
  - Health insurance for those over 65 (p. 492).
  - Statistical hiring decisions about minorities (p. 494).
  - Costs of dishonesty (p. 495).
  - Credit markets in India and elsewhere, where moneylenders charge far more than central banks (p. 498).
- **Dishonesty is costly beyond the cheating itself.** It costs $1/2$ unit of utility per car and shrinks the used-car market from $N$ to $0$ (p. 496).
- **Counteracting institutions.** Guarantees, brand names, chains and licensing or certification reduce quality uncertainty. Such institutions are non-atomistic and can concentrate power (pp. 488, 499–500).

## L3 — Walkthrough

### I. Introduction (p. 488)
- The paper links quality and uncertainty. Quality differences plus uncertainty may explain labour-market institutions. They also give a structure to the claim that "business in underdeveloped countries is difficult", including the economic cost of dishonesty (p. 488).
- Other applications are listed: money markets, "insurability", liquidity of durables and brand-name goods (p. 488).
- The core mechanism is that buyers judge quality by a market statistic. Sellers then have an incentive to sell poor quality, because returns to good quality "accrue mainly to the entire group whose statistic is affected" and not to the individual seller (p. 488).
- Result: average quality falls and the market shrinks. Social and private returns differ, so intervention may help everyone (p. 488).
- Private institutions that arise to fix this are non-atomistic. They can lead to concentrations of power with ill consequences (p. 488).
- The car market is chosen for concreteness, not for realism or importance (p. 489).

### II. The model with automobiles as an example

**A. The automobiles market (pp. 489–490)**
- There are four kinds of cars: new or used, good or bad. Bad cars are "lemons" (p. 489).
- Buyers of a new car know only that it is good with probability $q$ and a lemon with probability $1-q$. Here $q$ is the proportion of good cars produced (p. 489).
- After some time, the owner learns the car's quality much better. Information is now asymmetric: sellers know more than buyers (p. 489).
- Good and bad used cars must sell at the same price, because buyers cannot tell them apart (p. 489).
- A used car cannot be valued like a new one. If it were, an owner of a lemon could trade it for a new car at the same price and get a higher chance $q$ of a good car. So the owner of a good car is locked in. He cannot get his car's true value, and he cannot even get the expected value of a new car (p. 489).
- Gresham's law reappears. Most traded cars will be lemons, and good cars may not be traded at all (pp. 489–490).
- The analogy is incomplete. In Gresham's law, bad money drives out good because the exchange rate is fixed, but both parties can tell the two apart. Here only the seller knows (p. 490).

> **Intuition note.** The price must be one number for all cars. That number reflects average quality. Owners of better-than-average cars lose by selling, so they leave, and the average falls.

**B. Asymmetrical information (pp. 490–491)**
- With a continuum of grades, the sequence of exit can run all the way down: the good, then the not-so-good, then the medium, and so on, until no market exists (p. 490).
- General setup: demand depends on price $p$ and average quality $\mu$ of used cars traded:
$$Q^d = D(p,\mu).$$
Average quality and supply depend on price: $\mu=\mu(p)$ and $S=S(p)$. Equilibrium is
$$S(p)=D(p,\mu(p)).$$
As the price falls, quality normally falls too. It is possible that no goods are traded at any price (p. 490).

*Utility example (pp. 490–491).* There are two groups of traders. Their utilities are
$$U_1 = M + \sum_{i=1}^{n} x_i, \qquad U_2 = M + \sum_{i=1}^{n} \tfrac{3}{2}\, x_i .$$
Here $M$ is consumption of goods other than cars, $x_i$ is the quality of the $i$-th car, and $n$ is the number of cars (p. 490).

Three comments on these functions (pp. 490–491):
1. Linear utility avoids needless algebra, for example with logarithmic utility.
2. Linearity isolates the effect of information asymmetry. With concave utility, the usual risk-variance effects would mix in.
3. Each extra car adds the same utility as the first. This is unrealistic, and it is accepted to keep the focus.

Assumptions (p. 491):
1. Both groups maximise von Neumann–Morgenstern expected utility.
2. Group one has $N$ cars, with quality $x$ uniformly distributed on $0\le x\le 2$. Group two has no cars.
3. The price of "other goods" $M$ is 1.

Let $Y_1$ and $Y_2$ be the incomes of all type-one and type-two traders. Income includes car-sale proceeds. Ignoring indivisibilities (p. 491):
$$D_1 = Y_1/p \quad (\mu/p>1), \qquad D_1 = 0 \quad (\mu/p<1).$$
The supply from type one is
$$S_2 = pN/2 \quad (p\le 2), \tag{1}$$
with average quality
$$\mu = p/2. \tag{2}$$
Equations (1) and (2) use the uniform distribution of quality (p. 491). (The source labels the supply in (1) as $S_2$. The context shows it is type one's supply. See Reading notes.)

For type two (p. 491):
$$D_2 = Y_2/p \quad (3\mu/2>p), \qquad D_2 = 0 \quad (3\mu/2<p), \qquad S_2 = 0.$$
Total demand (p. 491):
$$D(p,\mu) = (Y_2+Y_1)/p \ \text{ if } p<\mu,$$
$$D(p,\mu) = Y_2/p \ \text{ if } \mu<p<3\mu/2,$$
$$D(p,\mu) = 0 \ \text{ if } p>3\mu/2.$$
*Conclusion (p. 491).* With price $p$, average quality is $p/2$. So at no price does any trade take place. This holds even though at any price between 0 and 3 some type-one traders would sell at a price type-two traders would pay (p. 491).

*Added step (not in the source).* Type-one owners sell a car of quality $x$ only if $p\ge x$, because they value it at $x$. The fraction with $x\le p$ is $p/2$, which gives (1) and (2). Since $\mu=p/2$, we get $3\mu/2=3p/4<p$. Type-two buyers' demand is therefore zero at every price. For $p>2$ all $N$ cars are offered, with $\mu=1$, and $3\mu/2=1.5<p$, so demand is still zero.

> **Intuition note.** Buyers value cars 50% above sellers, so there are real gains from trade. But a buyer who sees price $p$ expects average quality $p/2$. He then values the car at only $0.75p$, below $p$. The price needed to attract any seller is always too high for buyers.

**C. Symmetric information (p. 492)**
- Now suppose quality is uniformly distributed on $0\le x\le 2$ and everyone knows each car's quality. Supply and demand are (p. 492):
$$S(p)=N \ (p>1), \qquad S(p)=0 \ (p<1).$$
$$D(p)=(Y_2+Y_1)/p \ (p<1), \quad D(p)=Y_2/p \ (1<p<3/2), \quad D(p)=0 \ (p>3/2).$$
- Equilibrium (p. 492):
$$p=1 \quad \text{if } Y_2<N, \tag{3}$$
$$p=Y_2/N \quad \text{if } 2Y_2/3<N<Y_2, \tag{4}$$
$$p=3/2 \quad \text{if } N<2Y_2/3. \tag{5}$$
- If $N<Y_2$, utility is higher than under asymmetric information by $N/2$. If $N>Y_2$, type-two income cannot buy all $N$ cars, and the gain is $Y_2/2$ (p. 492).
- If both groups share the same probabilistic estimates about each car's quality, (3)–(5) still hold. These estimates may vary from car to car. The only change is that $p$ then means the expected price of one quality unit (p. 492).

*Added step.* Under asymmetric information no car trades. Under symmetric information $N$ cars (average quality 1) move to buyers who value quality at $3/2$ instead of 1. The gain is $N\cdot(3/2-1)=N/2$.

> **Intuition note.** The loss from asymmetric information is the whole gain from trade. Everything the buyers value above the owners' value is lost.

### III. Examples and applications

**A. Insurance (pp. 492–494)**
- People over 65 find it very hard to buy medical insurance. Why does the price not rise to match the risk? (p. 492)
- Akerlof's answer: as the price rises, those who buy are increasingly certain they will need insurance. Applicants can judge their risks better than the insurer can. So average applicant health worsens as price rises, and no insurance may be sold at any price. This is "strictly analogous" to the cars case (pp. 492–493).
- Two insurance textbooks are cited as agreeing: "adverse selection" at ages above 65 (p. 493, citing Dickerson) and possible adverse selection in term life insurance when healthy holders leave as premiums rise (p. 493, citing Denenberg et al.).
- A 1956 survey of 2,809 families (8,898 persons) is cited (p. 493):
  - Hospital insurance coverage falls from 63% for ages 45–54 to 31% for those over 65.
  - Average medical expenses for males 55–64 are \$88. For males over 65 they are \$77.
  - Non-insured expenditure rises from \$66 to \$80. Insured expenditure falls from \$105 to \$70.
  - Akerlof finds it tempting to conclude that insurers are wary of insuring older people.
- Group insurance picks out the healthy, because adequate health is a precondition of employment. So insurance is least available to those who need it most (pp. 493–494).
- Footnote 1 says Arrow's article stresses "moral hazard" and not "adverse selection". In the strict sense, moral hazard hurts government and private programmes equally. In the broader sense, which includes adverse selection, it favours government programmes (p. 493).
- Footnote 5 quotes an insurance textbook: companies "give a second look" to people who seek accident and health insurance voluntarily (p. 494).
- Argument for Medicare: every individual might be willing to pay the expected cost of his coverage, yet no company can sell him a policy, because at any price it attracts too many lemons. The welfare logic is like the classroom argument for public roads (p. 494).

**B. The employment of minorities (pp. 494–495)**
- Refusing to hire minority members for some jobs may reflect profit maximisation and not irrationality or prejudice. Race can serve as a statistic for social background, schooling quality and job capabilities (p. 494).
- Good schooling could replace this statistic, since grading gives a better indicator. Talents must be certified by the educational establishment, and the certifier must be credible. Unreliable slum schools reduce their students' economic chances (p. 494).
- An employer may rationally refuse to hire any members of a disadvantaged group for responsible posts, because good and bad qualifications cannot be told apart. Akerlof links this to Stigler's remark that in a "regime of ignorance" Fermi would have been a gardener (p. 495).
- Rewards for work in slum schools accrue to the group, by raising its average quality, and not to the individual. There is incentive for training only if information beyond race is used (p. 495).
- He warns that cost-benefit analysis of anti-poverty programmes may miss external benefits. Training benefits arise partly from raising the group's average quality and are spread over the whole group (p. 495).

**C. The costs of dishonesty (pp. 495–496)**
- In a market where quality may be misrepresented, the presence of dishonest sellers tends to drive the market out of existence, as with lemons. Dishonest dealings drive honest ones out (p. 495).
- The cost of dishonesty is therefore not only what buyers lose by being cheated. It also includes the loss from driving legitimate business out of existence (p. 495).
- In the model economy, misrepresenting car quality costs $1/2$ unit of utility per car and shrinks the used-car market from $N$ to $0$. So the cost of dishonesty can be evaluated, "at least in theory" (pp. 495–496).
- Evidence that quality variation is larger in underdeveloped areas (p. 496):
  - Quality control of exports is needed. Under India's Export Quality Control and Inspection Act of 1963, about 85% of Indian exports are covered by some quality control.
  - Indian housewives must sort stones from rice.
- Merchants and entrepreneurs (p. 496):
  - In one traditional pattern, merchants of the pre-industrial generation become the first entrepreneurs of the next. Japan is the best-documented case. Britain and America may also fit.
  - In the model, the merchant's skill is identifying quality. Those who can identify and guarantee used cars may profit by up to the gap between type-two buyers' buying price and type-one sellers' selling price.
  - The same skills are needed in production, to judge input quality and certify output quality.
- Entrepreneurship is scarce. Product variation then impedes development in two ways (p. 496):
  1. The pay-off to trade is great, which diverts would-be entrepreneurs from production.
  2. The entrepreneurial time needed per unit of output is greater when quality varies more.

**D. Credit markets in underdeveloped countries (pp. 497–499)**
- *(1) Managing agencies in India* (pp. 497–498):
  - Managing agencies control 65.7% of the net worth of public limited companies and 66% of total assets (p. 497).
  - Promoters of new ventures approach an established agency for its reputation, which inspires confidence and attracts investment (p. 497).
  - A second feature is the domination of these agencies by caste or communal groups (p. 497).
  - Footnote 5 gives counts of firms by community of control. For 1911, 1931 and 1951, British-controlled firms number 281, 416 and 382. Marwari-controlled firms number "-", 6 and 96. Totals are 341, 510 and 619 (p. 497).
  - In an environment where outside investors are likely to be cheated, Akerlof says either (p. 498):
    1. Firms establish a reputation for honesty, which earns monopoly rent because such services are scarce, or
    2. Finance is limited to local communal groups, who can use communal or family ties to encourage honest dealing.
  - It is hard to tell why rich landlords' savings failed to enter industry. The causes may be fear of other communities' ventures, inflated propensities to consume, or low returns. British-owned agencies had a more heterogeneous equity holding than Indian-controlled agencies (p. 498).
- *(2) Moneylenders* (pp. 498–499):
  - Local moneylenders charge 15%, 25% and even 50%, while large city banks have prime rates of 6%, 8% and 10%. In India high rates have been a leading factor in landlessness, and the Cooperative Movement tried to counter this (p. 498).
  - Footnote 7 reproduces Darling's table of rates by province. Secured loans are around 6–12%, unsecured loans are higher, and grain loans are 25–50% (p. 498).
  - Akerlof's answer to the paradox: credit is granted only where the lender has (1) easy means of enforcing the contract or (2) personal knowledge of the borrower's character (p. 499).
  - A middleman who tries to arbitrage between moneylender and central-bank rates is apt to attract all the lemons and lose money (p. 499).
  - Supporting quotations: Darling on the village moneylender's intimate knowledge, a Hong Kong shopkeeper who gives credit only to those he knows, and Iranian cotton ginners who expect large early losses from poor local knowledge (p. 499).

> **Intuition note.** In all these cases an outsider cannot tell good from bad, so the market price is too low or no deal is made. Local insiders, such as moneylenders, communal firms and merchants, can profit because they see quality.

### IV. Counteracting institutions (pp. 499–500)
- Institutions arise to counteract quality uncertainty (p. 499).
- **Guarantees.** Most consumer durables carry them. A natural result of the model is that the risk is borne by the seller, not the buyer (p. 499).
- **Brand names** (pp. 499–500):
  - They indicate quality.
  - They also give the consumer a means of retaliation, since he will curtail future purchases.
  - New products are often tied to old brand names.
- **Chains** (hotels, restaurants) work like brand names. Chain restaurants in the US most often appear on interurban highways, where customers are seldom local. A local customer who knows his area can choose a place he prefers (p. 500).
- **Licensing and certification.** Examples are the licensing of doctors, lawyers and barbers, and the high school diploma, baccalaureate, Ph.D. and even the Nobel Prize. Education and labour markets have their own "brand names" (p. 500).

### V. Conclusion (p. 500)
- The paper discusses models in which "trust" matters. Informal unwritten guarantees are preconditions for trade and production. Where they are indefinite, business suffers, as the "generalized Gresham's law" shows (p. 500).
- Game theorists have explored this, as in the Prisoner's Dilemma. It has usually not been included in the Arrow–Debreu approach to uncertainty (p. 500).
- Distinguishing good from bad quality is inherent in business. It may explain many institutions and may be one of the more important aspects of uncertainty (p. 500).

## Toy example
*Our own numbers; not from the paper. It copies the paper's logic with a discrete quality distribution.*

Setup. There are four used cars, with qualities 1, 2, 3 and 4 (in thousands of dollars). Each owner values his car at its quality $x$. A buyer values a car of quality $x$ at $1.2x$. The buyer cannot see quality, but he knows the cars traded at price $p$ are those with $x\le p$. Cash is the numeraire.

At each price, owners sell if $x\le p$. The buyer's value is $1.2\times$ the average quality of the cars offered. Trade requires that value $\ge p$.

| Price band | Cars offered | Average quality | Buyer's value | Trade? |
|---|---|---|---|---|
| $p\ge 4$ | 1, 2, 3, 4 | $(1+2+3+4)/4=2.5$ | $1.2\times2.5=3.0$ | $3.0<4$: no |
| $3\le p<4$ | 1, 2, 3 | $(1+2+3)/3=2$ | $1.2\times2=2.4$ | $2.4<3$: no |
| $2\le p<3$ | 1, 2 | $(1+2)/2=1.5$ | $1.2\times1.5=1.8$ | $1.8<2$: no |
| $1\le p<2$ | 1 | 1 | $1.2\times1=1.2$ | Yes for $1\le p\le 1.2$ |

So only the worst car trades, at a price between 1 and 1.2.

Welfare. With full information, all four cars would trade at their own values. The gain is $0.2\times(1+2+3+4)=0.2\times10=2.0$. With hidden quality, only car 1 trades. The gain is $0.2\times1=0.2$. The loss is $2.0-0.2=1.8$, which is 90% of the possible gain. This is the same type of loss as the paper's "$N/2$" (p. 492): every car is worth more to a buyer, yet nearly all trade is lost.

## Concepts
- [[asymmetric-information]] — sellers know car quality, buyers do not (p. 489)
- [[adverse-selection]] — as price falls, the cars or insureds that stay in the market are the worse ones; Akerlof uses the term for insurance (pp. 489, 493)
- [[market-failure-externality]] — returns to quality accrue to the group, so private and social returns differ and the market shrinks (pp. 488, 495)
- [[price-as-signal]] — here price also drives average quality, as the price affects who sells (p. 490)
- [[equilibrium]] — supply equals demand at the given average quality, $S(p)=D(p,\mu(p))$; in the example, no trade is the outcome (pp. 490–491)
- [[incomplete-contracts]] — informal unwritten guarantees and trust are preconditions of trade (p. 500). The match is loose, since the source does not use this term.
- [[signaling]] — guarantees, brand names, licensing and certification credibly indicate quality (pp. 499–500). The match is loose, since the source does not use this term.
- [[screening]] — insurers screen applicants (p. 494, footnote 5). Used loosely.
- [[moral-hazard]] — mentioned in footnote 1 on Arrow's emphasis (p. 493)
- [[social-dilemma]] — Prisoner's Dilemma mentioned as a related trust problem (p. 500)
- `lemons-principle` (new) — bad-quality goods driven into markets where buyers cannot tell quality, so average quality and market size fall (pp. 489–491)
- `statistical-discrimination` (new) — using a group trait (race) as a statistic for individual quality (p. 494)
- `reputation-and-certification` (new) — brands, chains, licences and credible schools as quality guarantees (pp. 494, 499–500)

## Canonical instances
- [[used-car-market-lemons]] — the four-type car model with uniform quality and no trade at any price (pp. 489–491)
- [[over-65-health-insurance]] — adverse selection explains why the old cannot buy insurance; survey data (pp. 492–493)
- [[minority-employment-statistic]] — employer uses race as a quality statistic; incentives to train are weak (pp. 494–495)
- [[cost-of-dishonesty]] — $1/2$ unit of utility per car and the market falls from $N$ to $0$ (pp. 495–496)
- [[india-managing-agencies]] — communal groups and reputation as a response to quality uncertainty in finance (pp. 497–498)
- [[moneylender-interest-rates]] — high local rates versus low bank rates; arbitrage attracts lemons (pp. 498–499)
- [[chain-restaurants-highways]] — brand/chain example where customers are not local (p. 500)

## Bridges (candidates)
- [structural-analogy] Unraveling from adverse selection ↔ economics-finance: bank-run equilibrium — in both, one agent's exit makes staying worse for the others and the market or deposit base can collapse. The mechanisms differ: information versus a withdrawal coordination game.
- [structural-analogy] Group returns to quality (p. 488) ↔ economics-finance: social dilemma / externality — each seller bears the full cost of quality but gets only a share of the group's benefit, as in a public-goods game.
- [structural-analogy] Price lowers average quality (p. 490) ↔ economics-finance: price as signal — the price carries information, but here it also changes who participates.
- [metaphor] Gresham's law "bad drives out good" (p. 489) ↔ computational social science: low-quality content crowding out high-quality content on platforms — both describe the average falling when quality is hard to observe.
- [structural-analogy] Using race as a quality statistic (p. 494) ↔ computational social science: group-level features in predictive algorithms — both infer individual quality from group averages.
- [structural-analogy] Guarantees, brands, licences (pp. 499–500) ↔ economics-finance: signaling — a credible, costly commitment lets high types separate from low types.

## Questions this raises
- The paper's linear model makes trade vanish completely. How would the result change with risk-averse buyers, or with some sellers who value quality lower than buyers do (p. 491)?
- Can sellers in a lemons market take a costly action that only good types can afford? What does it take for the action to be credible (pp. 499–500)?
- Akerlof says rational employers may avoid minority hires (p. 494). How can policy change that without inviting mistakes or other adverse selection?
- When an institution fixes the quality problem, who controls it, and what market power might they gain (p. 488)?

## Reading notes
- **Page 1 (pdf)** is the JSTOR cover sheet. The paper begins at printed page 488 (pdf 2). The printed number is unknown for pdf 1.
- **OCR on pdf 2–3, 6–14** is poor in places. Words are run together, for example "gradesposes" and "CritiCreditMarketsin". I corrected spacing only where the meaning was clear. Page images were provided only for pdf 4–6 (printed 490–492). The equations on pp. 490–492 were checked against the images. Pages 488–489 and 493–500 were read from the text layer only.
- **Equation (1) label.** The printed text labels the supply from type one as $S_2$ (p. 491). From context it is type one's supply. Type-two supply is separately $S_2=0$. This looks like a misprint for $S_1$.
- **Section II.B notation.** Average quality is written $\mu$ in the image, but the text layer sometimes shows other symbols. Equation (3) and (5) also read $Y_2<N$ and $N<2Y_2/3$ in the images, which I used.
- **Price range "0 and 3".** On p. 491 the author writes "between 0 and 3". This is the highest value a type-two buyer could put on a car of quality 2 (3/2 × 2). This is my reading, not the author's explicit statement.
- **Table on p. 497 (text layer).** The 1911 column sums to 340, but the printed total is 341. The two dash cells (Muslims and Marwaris) may be a rendering issue. 1931 and 1951 sum correctly.
- **Footnote 7 table (p. 498).** The Darling table is only partly legible in the text layer. I did not copy it fully.
- **Term "adverse selection."** Akerlof's own wording is "adverse selection" in quotation marks, taken from insurance textbooks. He uses it as a known term for the insurance case and does not give a formal definition (p. 493).
- The paper has no formal theorem or proof. The only derivation is the car example in Section II.