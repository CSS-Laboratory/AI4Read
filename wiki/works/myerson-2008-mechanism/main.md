---
id: myerson-2008-mechanism/main
work: myerson-2008-mechanism
unit: paper
pages: 320–341
fields: [decision-game-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Perspectives on Mechanism Design in Economic Theory (Myerson, Nobel lecture 2007)

## L0 — One line
Economics should add incentive constraints to resource constraints, and the revelation principle lets us study every equilibrium of every institution through incentive-compatible plans.

## L1 — The gist (≤ 120 words)
Myerson asks what social arrangements are feasible when people hold private information and take hidden actions. Answer: by the revelation principle, any equilibrium of any institution is equivalent to an incentive-compatible plan, i.e. one where honesty and obedience are optimal; such plans are described by incentive constraints (inequalities). Three examples apply this: bilateral trade with private values (adverse selection), a project with a manager's hidden effort (moral hazard), and a ruler who may expropriate capital. The paper shows that incentive constraints can explain allocative inefficiency, that property-rights assignments can matter, and that efficiency should be judged for mechanisms, not just allocations.

**Prerequisites:** expected value (risk-neutral agents); Nash equilibrium; conditional probability; solving linear inequalities; present discounted value.

## L2 — Key ideas
- Economics moved from allocating goods to analysing incentives and institutions. Hayek asked for institutions to be compared as mechanisms of communication; Hurwicz added incentive compatibility (pp. 320–322).
- A social plan makes actions depend on information. Getting honest reports is *adverse selection*; getting obedient hidden actions is *moral hazard*. A plan is incentive compatible if honesty and obedience form an equilibrium (pp. 322–323).
- The revelation principle: any rational equilibrium of any mechanism is equivalent to an incentive-compatible plan. So one can search only among incentive-compatible plans (pp. 323–324, 330).
- In bilateral trade with private values, the best incentive-compatible plan still fails to realize a mutually beneficial trade (ex-post allocative inefficiency: the object does not go to the person who values it most) with probability 1/12 (p. 328). Efficiency must be judged with incentive constraints (p. 328).
- Incentive efficiency (efficiency of a mechanism among incentive-compatible ones) has an ex-ante version (welfare judged before anyone knows their type) and an interim version (judged after each person knows only his or her own type). Several mechanisms are interim efficient; some are better for strong types and others for weak types (pp. 328–329).
- Incentive constraints can be viewed as a source of Coasean transaction costs (the costs that Coase said stand between free trade and efficiency). Reversing initial ownership makes ex-post efficiency achievable in the trade example (p. 331).
- In the paper's example, moral hazard in management requires the manager to hold a stake (here at least 40% of the capital cost for positive profit). Adverse selection can instead favour collectivism (pp. 333–337).
- A ruler's inability to commit not to expropriate can block investment. Liberalization can help restore credibility, and natural-resource wealth can reduce the incentive to liberalize (pp. 337–339).

## L3 — Walkthrough

### 1. An historical perspective (pp. 320–322)
- Classical economics studied production and allocation of goods. Its classical result was that unrestricted free trade can achieve allocative efficiency: no reallocation can improve everyone's welfare (p. 320).
- Since Cournot (1838), theorists analysed rational individual decisions; game theory followed (p. 320).
- The socialism-versus-capitalism debate exposed a limit. Price theory could show (under some conditions) that free markets are efficient, but not that command economies could not do as well (p. 321).
- **Hayek's view:** institutions of all kinds communicate dispersed information, so they should be compared as mechanisms for communication (p. 321).
- Myerson's reading: Hayek's complaint was evidence of a need for new mathematical models, not against mathematics (p. 321).
- Hurwicz (1972) raised the question of incentives to communicate and introduced incentive compatibility (p. 321).
- With Harsanyi's Bayesian games, Hurwicz's mechanisms became a theory of designing Bayesian games. A *coordination mechanism* is a plan for how social decisions depend on reported information (p. 321).
- Many authors found the revelation principle independently. The feasible set essentially coincides with the incentive-compatible mechanisms, which satisfy *incentive constraints* (pp. 321–322).
- New concept: *incentive efficiency* evaluates the rules by which resources are allocated, not only specific allocations (p. 322).

### 2. Elements of mechanism design theory (pp. 322–324)
- A *social plan* describes how everyone's actions should depend on everyone's information. Feasibility is studied first with a trustworthy central mediator who receives confidential reports and recommends actions (p. 322).
- Adverse selection: giving people an incentive to share hard-to-observe information honestly. Moral hazard: giving incentives to obey recommendations on hidden actions or efforts (pp. 322–323).
- A plan is *incentive compatible* if honesty and obedience to the mediator form a rational equilibrium (p. 323). Such plans are characterised by inequalities (incentive constraints) (p. 323).
- **Revelation principle:** any rational equilibrium of individual behaviour in any institution is equivalent to an incentive-compatible plan (Figure 1, p. 323).
- **Proof sketch (p. 324):**
  1. Take any mechanism and equilibrium.
  2. The mediator computes the (dishonest) reports everyone would send in the equilibrium.
  3. It computes the mechanism's response to those reports.
  4. It computes the (disobedient) action each person would have chosen, and recommends it confidentially.
  5. A gain from lying or disobeying the mediator would also be a gain from lying or disobeying one's own equilibrium strategy, which is impossible in equilibrium.
- *Intuition note:* The mediator simulates the players' lies and disobedience for them. Honesty and obedience can then be made the best policy, so searching over honest plans loses no generality.
- Three examples follow: trade (adverse selection), management (moral hazard), government (moral hazard) (p. 324).

### 3. Bilateral trading with adverse selection (pp. 324–332)
**Setup.** One seller, one buyer, one object. Seller's value is $0 (*weak*) or $80 (*strong*). Buyer's value is $100 (weak) or $20 (strong). A "weak" type is one willing to trade at more prices. Each type has probability 0.5, independently. Agents are risk-neutral (pp. 324–325). A mediator receives reports and recommends trade at a price or no trade. Traders accept if neither is made worse off (p. 325). Figures give P(trade) and E(price | trade) in each type cell.

**3.1 Split-the-difference plan (Figure 2, p. 325).** Trade whenever buyer's value exceeds seller's, at the midpoint. Cells (seller, buyer): (80,20): 0; (80,100): 1, $90; (0,20): 1, $10; (0,100): 1, $50.
- A strong type never gains by claiming weakness (p. 326).
- Weak seller, buyer honest. Honest: $0.5(10-0)+0.5(50-0)=30$. Claiming strong: $0.5(90-0)=45>30$ (p. 326).
- So honesty is not an equilibrium: the plan is not incentive compatible (p. 326).

**3.2 Symmetric plans (Figure 3, p. 326).** Trade probability $q$ when exactly one is weak. The weak individual's expected profit margin in that case is $y$. Weak-weak trade has probability 1 at $50. No trade when both are strong. The cells are: weak seller with strong buyer: $q,\ y$; strong seller with weak buyer: $q,\ 100-y$ (p. 326). Incentive compatibility needs three constraints (pp. 326–327):
- Probability (resource) constraint: $0\le q\le 1$ (only one object) (p. 327).
- Participation constraint (a strong buyer pays $y$ in trades, which would be a loss if $y>20$):
$$y\le 20.$$
- Informational incentive constraint (weak seller, honest opponent). Honest: $0.5q(y-0)+0.5(1)(50-0)$. Lying: $0.5(0)+0.5q(100-y-0)$. Hence
$$0.5qy+0.5(50)\ge 0.5q(100-y),$$
equivalent to
$$q\le \frac{25}{50-y}.$$
(added step: expanding, $qy+50\ge q(100-y)$, i.e. $50\ge q(100-2y)$.) (p. 327)

**3.3 Incentive-efficient plans (pp. 327–329).**
- Since $25/(50-y)$ rises with $y$ and $y\le20$, the largest feasible $q$ is at $y=20$, $q=5/6$ (added step; the author states the result, p. 327). Figure 4: cells (80,100): 5/6, $80; (0,20): 5/6, $20; (0,100): 1, $50; (80,20): 0.
- The incentive constraint holds with equality: honesty gives $(0.5)(5/6)20+(0.5)50=33.33$; lying gives $(0.5)(5/6)80=33.33$ (p. 327).
- Footnote 3: this depends on separate communication with the mediator. If the seller learned a weak buyer report first, lying would pay, since $(5/6)80>50$ (p. 327).
- Ex-post failure probability in Figure 4 is $(2/4)(1/6)=1/12$. The author states that no incentive-compatible plan has lower ex-post inefficiency here, once participation and incentive constraints are included (p. 328).
- *Ex-ante* expected profit for each person: $[0+0+(5/6)20+(1)50]/4=16.67$. No incentive-compatible mechanism gives both a higher ex-ante expected profit, so Figure 4 is *ex-ante incentive efficient* (Holmström–Myerson) (p. 328).
- A strong seller never profits in Figure 4. Welfare judged after learning one's type gives *interim incentive efficiency*: no other incentive-compatible mechanism is preferred by every type of every individual (pp. 328–329).
- Figures 5 and 6 keep $q=25/(50-y)$ but with $y<20$ (p. 328):

| Figure | $y$ | $q$ | EU strong | EU weak |
|---|---|---|---|---|
| 4 | 20 | 5/6 | 0 | 33.33 |
| 5 | 10 | 5/8 | 3.125 | 28.125 |
| 6 | 0 | 1/2 | 5 | 25 |

 Figure 6 is the best for strong types among these. It is the solution of a generalized Nash bargaining solution (Myerson 1984) (p. 329).
- *Intuition note:* Information problems create a trade-off: more trade for weak types means a worse deal for strong ones. Which mechanism counts as "efficient" depends on the stage (before or after types are known) at which welfare is measured.

**3.4 Dishonest equilibria and the revelation principle (pp. 329–330).**
- In split-the-difference, if the buyer is honest, the seller prefers to always claim strong. If the seller always claims strong, the buyer prefers honesty (weak buyer gets at least $100-90=10$). So this is an equilibrium of the reporting game (p. 329).
- Its outcomes equal Figure 7: trade at $90 iff the buyer reports weak, ignoring the seller's report (p. 329).
- Two other equilibria: the buyer always claims strong (outcomes in Figure 8, the mirror image), and a mixed one where each weak type claims strong with probability 0.6 (outcomes in Figure 9: trade probabilities 0.4 (strong seller, weak buyer), 0.4 (weak seller, strong buyer), 0.64 (both weak)) (p. 330).
- General point: for any equilibrium under any mediation plan there is an incentive-compatible mechanism with the same outcomes for all types. So no equilibrium of any mediation plan, compatible or not, has lower ex-post inefficiency than the honest equilibrium of Figure 4 (p. 330).

**3.5 General nonsymmetric mechanisms (p. 331).** Variables $q_{j,k}$ and $y_{j,k}$ for seller value $j\in\{0,80\}$, buyer value $k\in\{20,100\}$ (eight variables). Constraints (p. 331):
- Probability: $0\le q_{j,k}\le 1$ for each pair.
- Participation (four): e.g. strong seller $0.5q_{80,20}(y_{80,20}-80)+0.5q_{80,100}(y_{80,100}-80)\ge0$; weak seller $0.5q_{0,20}y_{0,20}+0.5q_{0,100}y_{0,100}\ge0$; strong buyer $0.5q_{80,20}(20-y_{80,20})+0.5q_{0,20}(20-y_{0,20})\ge0$; weak buyer $0.5q_{80,100}(100-y_{80,100})+0.5q_{0,100}(100-y_{0,100})\ge0$.
- Informational incentive (four): each type's honest expected profit is at least what it gets by reporting the other type, e.g. strong seller: $0.5q_{80,20}(y_{80,20}-80)+0.5q_{80,100}(y_{80,100}-80)\ge0.5q_{0,20}(y_{0,20}-80)+0.5q_{0,100}(y_{0,100}-80)$ (analogous for the others; see Reading notes for a misprint).
- Substitution $x_{j,k}=q_{j,k}y_{j,k}$ linearizes these, so the optimum can be found by linear programming. Figures 4–6 remain incentive-efficient in this larger class (p. 331).

**3.6 Incentive constraints as a source of Coasean transaction costs (p. 331).**
- **Coase's argument:** with no transaction costs, free trade achieves allocative efficiency whatever the initial property rights. So we need a theory of where transaction costs come from (p. 331).
- Here, informational incentive constraints can be viewed as such a source. Participation constraints represent the initial property rights (Samuelson 1985) (p. 331).
- Ex-post efficiency cannot be guaranteed by any incentive-compatible mechanism when the initial owner is the person whose value may be 0 or 80. If ownership is given to the person whose value is 20 or 100, a mediator can guarantee it: propose $50$, and they trade if both accept (Figure 10) (p. 331).
- *Intuition note:* Who owns the object at the start can change which mechanisms are feasible, because participation constraints represent the initial property rights. In this example, this shows how initial property rights can affect efficiency, in contrast to Coase's no-transaction-cost case.

### 4. A risky project with moral hazard in management (pp. 332–336)
**Setup (p. 332).** Capital $K=100$ is needed. Revenue $R=240$ on success, 0 on failure. Good effort: success probability $p_G=1/2$. Abuse of power: $p_B=1/4$, with hidden private benefit $B=30$. Then $p_GR>K$ but $K>p_BR+B$, so the project is worth doing only under good effort. The manager has collateral $A<K$. Failure costs him at most $A$ (payoff $-A$). Pay may depend on success or failure, not on effort. $w$ is his net payoff on success (p. 332).

Constraints (p. 333):
- Moral hazard: $p_Gw-(1-p_G)A\ge B+p_Bw-(1-p_B)A$.
- Participation: $p_Gw-(1-p_G)A\ge0$.
- Limited liability: $w\ge -A$.
- Society's expected profit under obedience: $V=p_G(R-w)+(1-p_G)A-K$.

For $A<Bp_G/(p_G-p_B)$ (i.e. $A<60$) the optimum makes the moral-hazard constraint binding (p. 333):
$$w=\frac{B}{p_G-p_B}-A=120-A.$$
(added step: the constraint simplifies to $(p_G-p_B)(w+A)\ge B$.) The manager's moral-hazard rent is
$$p_Gw-(1-p_G)A=\frac{Bp_G}{p_G-p_B}-A=60-A,$$
so society's expected profit is at most
$$p_GR-K-(60-A)=A-40 .$$
(p. 333)
- This is negative for $A<40$. So, in this example, society cannot get any positive expected profit unless the manager contributes assets of at least 40 (the author's wording), i.e. at least 40% of the capital cost (strictly, the bound $A-40$ is positive only for $A>40$). If nobody has such wealth (as perhaps in an egalitarian socialist society), society cannot profitably undertake the investment (p. 334).
- **Author's reading:** industrial managers have large temptations $B$, so managers need large stakes. Moral hazard casts doubt on the ideal that all profits of industrial means of production belong to the public (p. 334).
- **Extension with punishment** (p. 334): add an unproductive punishment cost $z\ge0$ on failure. Maximize $V$ subject to $w\ge-A$, $z\ge0$,
 $p_Gw-(1-p_G)(A+z)\ge B+p_Bw-(1-p_B)(A+z)$ [moral hazard] and $p_Gw-(1-p_G)(A+z)\ge0$ [participation].
 For $A<60$ the optimum is $z=60-A$, $w=60$. This wipes out the manager's expected gain but leaves $V=0.5A-10$, positive only if $A>20$ (pp. 334–335).
- If the participation constraint is dropped and $A=0$: $w=0$, $z\ge120$ gives $V=20$. The author calls this a terrible solution (drafting an unwilling manager, motivated by threat of bodily harm) (p. 335).
- Author's conclusion: Soviet industrialization may have necessarily entailed either a privileged managerial elite or coerced labour (p. 335).
- *Intuition note:* To make hidden effort pay, the manager's reward for success must exceed his reward for failure by enough. If he cannot pay for failure from his own assets, society must pay him a rent, which eats the project's profit.

**4.1 An analogous adverse-selection problem (pp. 335–337).**
- Now $p_G$ and $p_B$ are the success probabilities of a good or bad manager *type*, known only to the manager (no hidden action). $p_GR>K>p_BR$. Probability of good type: $\alpha$ (p. 335).
- Plan: finance with probability $q_G$ (reported good) or $q_B$ (reported bad), with success wages $w_G$, $w_B$. Failure forfeits $A$. Investors' profit (p. 335):
$$V=\alpha q_G[p_G(R-w_G)+(1-p_G)A-K]+(1-\alpha)q_B[p_B(R-w_B)+(1-p_B)A-K].$$
- Constraints (p. 336): $w_G,w_B\ge-A$; $0\le q_G,q_B\le1$; participation $q_G[p_Gw_G-(1-p_G)A]\ge0$ and $q_B[p_Bw_B-(1-p_B)A]\ge0$; incentive:
$$q_G[p_Gw_G-(1-p_G)A]\ge q_B[p_Gw_B-(1-p_G)A],\qquad q_B[p_Bw_B-(1-p_B)A]\ge q_G[p_Bw_G-(1-p_B)A].$$
- **Under socialism:** with $A=0$, the ideal plan $q_G=1$, $q_B=0$ is feasible with $w_G=w_B=0$. The manager gains nothing from managing, so he has no reason to lie (p. 336).
- **Under capitalism:** competition among investors implies $V=0$. With $A=0$, the ideal $(q_G=1,q_B=0)$ is then not feasible in any incentive-compatible equilibrium (p. 336, author's statement; footnote 6 points to Tirole).
- **Conclusion:** moral hazard shows disadvantages of socialism, adverse selection shows potential advantages. Ownership rights can help with hidden effort but may create conflicting interests that make honest communication harder. Collectivism can ease adverse selection while worsening moral hazard (pp. 336–337).

### 5. Moral hazard in the central government (pp. 337–339)
**Setup (p. 337).** Output $Y(K)$ requires capital $K$ held by capitalists, who can take it abroad. Their discount rate is $r$, so to deter capital flight they must receive $rK$. The ruler taxes $Y(K)-rK$. His discount rate is $r+b$ ($b$ = rate of losing power exogenously). The ruler could expropriate and sell the capital abroad.
- If he never expropriates, his value is $(Y(K)-rK)/(r+b)$. If he expropriates, he gets $K$ plus $Y(0)/(r+b)$ thereafter. So without liberalization he is credible only if (p. 338)
$$\frac{Y(K)-rK}{r+b}\ge K+\frac{Y(0)}{r+b}.$$
- *Liberalization* $\lambda\in[0,1]$: the probability that the ruler loses power if he tries to expropriate (or to reduce liberalization). The expropriation payoff becomes $(1-\lambda)[K+Y(0)/(r+b)]$ (p. 338).
- Cost: false-alarm scandals arrive at rate $a$ and are treated like genuine expropriation. Power-losing scandals occur at rate $a\lambda$, so the ruler discounts at $r+b+a\lambda$:
$$V(K,\lambda)=\frac{Y(K)-rK}{r+b+a\lambda}.$$
- Constraint: $V(K,\lambda)\ge(1-\lambda)\,[K+Y(0)/(r+b)]$. The ruler maximizes $V(K,\lambda)$ subject to this, $K\ge0$, $0\le\lambda\le1$ (p. 338).
- **Numerical example (pp. 338–339):** $Y(K)=(K+n)^{0.5}$, $r=b=a=0.05$. Without the constraint the ideal has $K+n=100$.

| $n$ | Optimal $\lambda$ | Investment $K$ |
|---|---|---|
| 12 | 0.504 | 52.4 (with $\lambda=0$ only $K=0$ is feasible) |
| 0 | 0 | 44.4 |
| 25 | 0 | 0 |

- Author's explanation: with no natural resources, losing a reputation for protecting capital is costly, so investment is credible without liberalizing. With great natural wealth, the ruler refuses liberalization's political risk, so nobody invests. Natural resources can reduce the incentive to liberalize, and investment may fall by more than the resources' value ("cursed by too many natural resources") (p. 339).
- *Intuition note:* Liberalization works as a commitment device. It lowers the ruler's payoff from breaking his word, but it also exposes him to risk, and a ruler with great natural wealth is unwilling to accept that risk.

### 6. Conclusions (p. 339)
- Mechanism design adds incentive constraints to resource constraints. Failures of allocative efficiency may depend on the initial allocation of property rights. The object of analysis changes from allocations to mechanisms (p. 339).
- Cases for collectivism or private ownership may depend on the trade-off between moral hazard and adverse selection. Moral hazard is fundamental in every institution because leaders and officials who enforce rules must themselves be motivated by expected rewards (p. 339).

## Toy example (ours, not from the text)
Moral hazard with new numbers. Capital $K=50$, revenue $R=100$ on success. Manager's success probabilities: good effort $p_G=0.8$, abuse $p_B=0.4$, private benefit from abuse $B=5$. Collateral $A=0$.
- Check the project is worth doing only under good effort: $p_GR=80>50$; $p_BR+B=40+5=45<50$.
- Moral-hazard constraint: $0.8w\ge5+0.4w$, so $0.4w\ge5$ and $w\ge12.5$. Take $w=12.5$.
- Check: good effort gives $0.8\times12.5=10$; abuse gives $5+0.4\times12.5=10$. These are equal, so the constraint binds.
- Rent: $10$ (formula: $Bp_G/(p_G-p_B)-A=5\times0.8/0.4=10$).
- Society's profit: $V=0.8(100-12.5)-50=70-50=20$. Equivalently $80-50-10=20$.
- Take $A=0$ here, so the manager contributes nothing; the project is still profitable. Raising $A$ lowers the needed rent by the same amount. In the paper's example the project is unprofitable at low $A$ (below 40), so the threshold stake depends on parameters.

## Concepts
- [[mechanism design]] — choosing rules (a mapping from reports to outcomes) so that self-interested behaviour yields a target outcome (pp. 321–322)
- [[incentive compatibility & revelation principle]] — truth-telling and obedience form an equilibrium. Any equilibrium of any mechanism is equivalent to such a plan (p. 323)
- [[Bayesian game / types]] — Harsanyi's model of people with different private information, used as the basis for designing games (p. 321)
- [[Nash equilibrium]] — used here as the equilibrium notion for honest reporting (p. 326)
- [[credible commitment]] — here, a ruler's credible promise not to expropriate, supported by liberalization (p. 337)
- [[adverse-selection]] (new) — problem of eliciting honest reports of hidden information (p. 322)
- [[moral-hazard]] (new) — problem of inducing obedience in hidden actions or effort (p. 323)
- [[incentive-constraints]] (new) — inequalities (informational incentive, moral hazard) that characterise incentive-compatible plans. Participation and resource constraints are listed alongside them (pp. 323, 327)
- [[incentive-efficiency]] (new) — efficiency of a mechanism among incentive-compatible ones. Ex-ante: before types are known. Interim: after one's own type (pp. 322, 328)
- [[participation-constraint]] (new) — each type must expect no loss from joining the plan. It represents the initial property rights each can hold without trading (pp. 327, 331)
- [[coasean-transaction-costs-from-incentives]] (new) — informational incentive constraints viewed as the source of transaction costs (p. 331)

## Canonical instances
- [[bilateral-trade-adverse-selection]] — seller value 0/80, buyer value 100/20. Split-the-difference fails; best symmetric plan $y=20$, $q=5/6$ (pp. 324–330)
- [[manager-moral-hazard-project]] — $K=100$, $R=240$, $B=30$: society gets no positive expected profit unless the manager's stake is at least 40 (pp. 332–335)
- [[autocrat-credibility-problem]] — ruler, capital and liberalization; "curse" of natural resources (pp. 337–339)

## Bridges (candidates)
- [structural-analogy] Revelation principle ↔ decision-game-theory: Aumann's correlated equilibrium, where a mediator recommends actions and obeying is optimal — the paper credits Aumann (1974) as a building block (p. 322).
- [same-math] Linearization $x_{j,k}=q_{j,k}y_{j,k}$ and constraint set ↔ operations research: linear programming — the paper says the optimal mechanism can be found by linear programming (p. 331).
- [structural-analogy] Ruler's expropriation constraint ↔ repeated games: the shadow of the future (value of keeping a reputation vs one-time gain) — the constraint compares continuing revenue with a one-shot grab (p. 338).
- [metaphor] Mediator simulating lies ↔ simulation or compilation of a strategy into a program that tells the truth — suggests why truthful direct mechanisms lose no generality.

## Questions this raises
- The unit assumes risk-neutral agents and a mediator who is trusted. What changes if agents are risk-averse or the mediator is itself self-interested (compare the point on p. 339 that leaders and officials must themselves be motivated by rewards)?
- The $x=qy$ linearization makes the problem a linear program. How does the set of incentive-efficient mechanisms change when the type space is continuous (the Myerson–Satterthwaite case mentioned on p. 325)?
- The commitment story in section 5 relies on specific functional forms. How robust are the three outcomes to other choices of $Y(K)$ or to other values of $a$ and $b$?
- Which mechanism should a society pick among the incentive-efficient mechanisms (Figures 4–6), and who decides?

## Reading notes
- Printed page numbers are given on every page: printed = pdf + 319. Text is pp. 320–339; references pp. 340–341.
- Source is the Nobel Prize Lecture of 8 December 2007, published in AER 98(3) per the unit metadata. The first page prints "Prize Lecture, December 8, 2007".
- The text layer renders "≤" and "≥" as "<" and ">". The page images show the weak inequalities, e.g. $0\le q\le1$, $y\le20$, and $w\ge-A$. The constraint $A<Bp_G/(p_G-p_B)$ is strict in the image.
- Probable misprint (p. 331, image): the second informational incentive constraint has $0.5q_{0,20}(y_{80,20}-0)$ on the right-hand side, where $0.5q_{80,20}(y_{80,20}-0)$ would match the other constraints. I did not correct it above beyond describing the pattern.
- Figure 10 (p. 332): row and column labels are "Buyer's value $80, $0" and "Seller's value $20, $100". These follow the reversed-ownership story in the text.
- p. 334: "at least 40" is stated for positive profit, but $A-40$ is positive only for $A>40$; at $A=40$ the bound is exactly 0.
- Several statements are the author's without proof here: e.g. optimality of $z=60-A$, $w=60$, and the optimal values in section 5, and non-feasibility under capitalism in 4.1. I report them as claims.
- Footnotes 2–7 and the reference list are partly summarised only where used.
