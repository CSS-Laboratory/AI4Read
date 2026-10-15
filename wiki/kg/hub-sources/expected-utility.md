---
id: expected-utility
type: concept
fields: [decision-game-theory, bayesian, economics-finance, information-theory, political-science]
fields_strong: [decision-game-theory, bayesian, economics-finance, information-theory, political-science]
n_sources: 18
n_works: 11
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch09-decision, kahneman-1979-prospect/main, kahneman-2011-thinking/appb-choices, kahneman-2011-thinking/ch25-bernoulli, kahneman-2011-thinking/ch26-prospect, kahneman-2011-thinking/ch29-fourfold, kahneman-2011-thinking/ch31-risk, mackay-2003-information/ch36-decision, mcgrayne-2011-theory/ch03-many, murphy-2023-pml2/ch34-decision, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch04-mixed-p2, osborne-2004-introduction/ch07-extensive, osborne-2004-introduction/ch09-bayesian, schelling-1960-conflict/ch07-randomization, shepsle-2010-analyzing/ch02-rationality, simon-1955-behavioral/main, thaler-2015-misbehaving/ch04-value]
aliases: [expected-utility-maximization, expected-utility-principle, expected-utility-theory, maximum-expected-utility]
raw_ids: [expected utility]
canon_spine: [decision-game-theory]
generated_by: build_kg.py
---

# expected-utility

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `expected-utility-maximization` — 1 digest(s)
- `expected-utility-principle` — 1 digest(s)
- `expected-utility-theory` — 1 digest(s)
- `maximum-expected-utility` — 1 digest(s)

## Canon spine entry

- **expected utility** (decision-game-theory): valuing a gamble as the probability-weighted average of the utilities of its outcomes (UG)

## Definitions in the sources

### decision-game-theory

- [[kahneman-1979-prospect/main]] (p. 263): $U=\sum p_iu(x_i)$, tenet (i) of the theory under attack [as `expected utility`; work fields: decision-game-theory, economics-finance]
- [[kahneman-2011-thinking/appb-choices]] (pdf 438): probability-weighted sum of outcome utilities (Bernoullian rule); the authors question it via nonlinear weights [as `expected utility`]
- [[kahneman-2011-thinking/ch25-bernoulli]] (pdf 265–266): value of a gamble as the probability-weighted average of the utilities of outcomes (Bernoulli's "moral expectation") [as `expected utility`]
- [[kahneman-2011-thinking/ch26-prospect]] (pdf 277): the utility-of-wealth account that Rabin's theorem attacks
- [[kahneman-2011-thinking/ch29-fourfold]] (pdf 302): a gamble's utility is the probability-weighted average of its outcomes' utilities (the "expectation principle") [as `expected utility`]
- [[kahneman-2011-thinking/ch31-risk]] (pdf 328): the rational-model benchmark Samuelson used; Rabin and Thaler's point, reported by Kahneman, is that if it can be consistent with such a foolish rejection, something is wrong with it
- [[osborne-2004-introduction/ch04-mixed-p1]] (p. 100): vNM preferences: lotteries ranked by the expected value of a Bernoulli payoff function
- [[osborne-2004-introduction/ch04-mixed-p2]] (p. 144): the expected-payoff evaluation $\sum p_k u(a_k)$ of lotteries, (144.1)
- [[osborne-2004-introduction/ch07-extensive]] (pp. 222, 225): payoffs in chance games are expected values of Bernoulli payoffs [as `expected utility`]
- [[osborne-2004-introduction/ch09-bayesian]] (p. 277): payoffs are Bernoulli payoffs whose expectation represents preferences over lotteries
- [[schelling-1960-conflict/ch07-randomization]] (p. 207): the probability-weighted value used to compare threats
- [[simon-1955-behavioral/main]] (p. 103): the probabilistic rule: maximize $\sum V(s)P_a(s)$ [work fields: decision-game-theory, economics-finance]

### bayesian

- [[gelman-2013-bda3/ch09-decision]] (p. 238): E(U(x)|d), computed at each decision point given the information then available [new]
- [[mcgrayne-2011-theory/ch03-many]] (p. 52): Ramsey's tool for acting under uncertainty [new]
- [[murphy-2023-pml2/ch34-decision]] (p. 1107): pick the action maximising expected utility $U=-\ell$ [alias `maximum-expected-utility`; new; work fields: bayesian, decision-game-theory]

### economics-finance

- [[thaler-2015-misbehaving/ch04-value]] (pdf 39–40): axiom-based theory of choice under risk, von Neumann–Morgenstern [alias `expected-utility-theory`; new]

### information-theory

- [[mackay-2003-information/ch36-decision]] (p. 451): choose $a$ maximizing $\int U(x,a)P(x\mid a)\,d^Kx$ [alias `expected-utility-maximization`; new; work fields: information-theory, bayesian, decision-game-theory]

### political-science

- [[shepsle-2010-analyzing/ch02-rationality]] (p. 33): choose the action whose outcome utilities, weighted by probabilities, sum highest [alias `expected-utility-principle`; new]

## Instances that use it

- [[problem-9-probabilistic-insurance]] — 80% reject it, although concave-$u$ expected utility predicts it beats regular insurance — from [[kahneman-1979-prospect/main]]

## Candidate bridges

- [same-math] CARA-normal demand $X=(E[u]-RP)/(a\,Var[u])$ ↔ economics-finance: mean-variance optimization — expected utility is a mean-variance expression with risk-aversion weight $a$ (the paper does not itself name mean-variance). — from [[grossman-1980-impossibility/main]] (economics-finance → economics-finance)
- [structural-analogy] Scope insensitivity to quantity (bird nets) ↔ decision-game-theory: expected-utility valuation that should scale with outcome size — the observed answers do not scale. — from [[kahneman-2011-thinking/ch08-judgments]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Outcome bias ↔ decision theory: judging a gamble by its draw, not by its expected utility. — from [[kahneman-2011-thinking/ch19-illusion]] (decision-game-theory → decision-game-theory)
- [metaphor] Optimism-driven risk taking ↔ expected utility: the chapter contrasts it with "favourable odds" as the cause of risk taking. — from [[kahneman-2011-thinking/ch23-outside]] (decision-game-theory → decision-game-theory)
- [same-math] Weighted-average payoff $U_i(\alpha)=\sum\alpha_i(a_i)U_i(a_i,\alpha_{-i})$ ↔ decision theory: expected utility is linear in probabilities — literally the same formula. — from [[osborne-2004-introduction/ch04-mixed-p1]] (decision-game-theory → decision-game-theory)
- [same-math] Lemma 145.1 (payoffs unique up to positive affine maps) ↔ decision theory: positive affine invariance of expected utility — the same representation result. — from [[osborne-2004-introduction/ch04-mixed-p2]] (decision-game-theory → decision-game-theory)
- [same-math] Expected value $\sum p_ix_i$ ↔ decision-game-theory: expected utility — the same weighted average, with utilities as the numbers. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → decision-game-theory)
- [same-math] Voting condition $p_2+p_3>2C$ ↔ decision theory: expected-utility comparison of two actions under state uncertainty. — from [[shepsle-2010-analyzing/ch09-collective-p2]] (political-science → decision-game-theory)
- [structural-analogy] Coherence vs compatibility ↔ subjective expected utility: consistency of bets does not guarantee sensible beliefs. — from [[tversky-1974-heuristics/main]] (decision-game-theory → decision-game-theory)
