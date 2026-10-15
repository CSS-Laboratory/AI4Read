---
id: expected-utility
type: concept
curated: 2026-10-15
fields: [decision-game-theory, bayesian, economics-finance, information-theory, political-science]
level: UG
grounding: digests
aliases: [expected-utility-maximization, maximum-expected-utility, expected-utility-principle, expected-utility-theory]
sources: [gelman-2013-bda3/ch09-decision, mcgrayne-2011-theory/ch03-many, murphy-2023-pml2/ch34-decision, kahneman-1979-prospect/main, kahneman-2011-thinking/ch25-bernoulli, kahneman-2011-thinking/ch26-prospect, kahneman-2011-thinking/ch31-risk, kahneman-2011-thinking/appb-choices, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch04-mixed-p2, schelling-1960-conflict/ch07-randomization, simon-1955-behavioral/main, thaler-2015-misbehaving/ch04-value, mackay-2003-information/ch36-decision, shepsle-2010-analyzing/ch02-rationality, shepsle-2010-analyzing/ch09-collective-p2, grossman-1980-impossibility/main, kahneman-2011-thinking/ch19-illusion]
links: [utility-function, loss-function, prospect-theory, bounded-rationality, risk-aversion, mixed-strategy, value-of-information]
generated_version: wiki/kg/hub-sources/expected-utility.md
---

# Expected utility

**Gist.** Expected utility values a risky option as the probability-weighted average of the utilities of its outcomes; the rational-choice rule is to pick the option with the highest expected utility.

Four variant ids are merged here (see `aliases`). 18 digests in five fields.

## How each field uses it

### Decision & game theory (home field)
- “value of a gamble as the probability-weighted average of the utilities of outcomes (Bernoulli's "moral expectation")” — [[kahneman-2011-thinking/ch25-bernoulli]] (pdf 265–266)
- “vNM preferences: lotteries ranked by the expected value of a Bernoulli payoff function” — [[osborne-2004-introduction/ch04-mixed-p1]] (p. 100)
- “the expected-payoff evaluation $\sum p_k u(a_k)$ of lotteries, (144.1)” — [[osborne-2004-introduction/ch04-mixed-p2]] (p. 144)
- “the probability-weighted value used to compare threats” — [[schelling-1960-conflict/ch07-randomization]] (p. 207)
- “the probabilistic rule: maximize $\sum V(s)P_a(s)$” — [[simon-1955-behavioral/main]] (p. 103)

### Bayesian theory & modeling (decision analysis)
- “E(U(x)|d), computed at each decision point given the information then available” — [[gelman-2013-bda3/ch09-decision]] (p. 238)
- “pick the action maximising expected utility $U=-\ell$” — [[murphy-2023-pml2/ch34-decision]] (p. 1107)
- “Ramsey's tool for acting under uncertainty” — [[mcgrayne-2011-theory/ch03-many]] (p. 52)

### Information theory (MacKay)
- “choose $a$ maximizing $\int U(x,a)P(x\mid a)\,d^Kx$” — [[mackay-2003-information/ch36-decision]] (p. 451)

### Economics & finance
- “axiom-based theory of choice under risk, von Neumann–Morgenstern” — [[thaler-2015-misbehaving/ch04-value]] (pdf 39–40)
- “$U=\sum p_iu(x_i)$, tenet (i) of the theory under attack” — [[kahneman-1979-prospect/main]] (p. 263)

### Political science
- “choose the action whose outcome utilities, weighted by probabilities, sum highest” — [[shepsle-2010-analyzing/ch02-rationality]] (p. 33)

## Bridges between fields

- **same-math** (political science → decision theory): “Voting condition $p_2+p_3>2C$ ↔ decision theory: expected-utility comparison of two actions under state uncertainty.” — [[shepsle-2010-analyzing/ch09-collective-p2]]. Justification: the paradox-of-voting calculus is an expected-utility comparison.
- **same-math** (economics, within the field): “CARA-normal demand $X=(E[u]-RP)/(a\,Var[u])$ ↔ economics-finance: mean-variance optimization — expected utility is a mean-variance expression with risk-aversion weight $a$ (the paper does not itself name mean-variance).” — [[grossman-1980-impossibility/main]]. Justification: under these assumptions the two objectives coincide.
- **same-math** (Bayesian ↔ ML): Murphy writes the utility as a negative loss, “$U=-\ell$” — [[murphy-2023-pml2/ch34-decision]]; see [[loss-function]]. Justification: maximising expected utility and minimising expected loss are one rule.
- **structural-analogy** (decision theory, behavioural side): “Outcome bias ↔ decision theory: judging a gamble by its draw, not by its expected utility.” — [[kahneman-2011-thinking/ch19-illusion]]. Justification: the bias is defined against the expected-utility benchmark.

## Where definitions disagree

- **Normative rule vs. descriptive theory under attack.** Osborne, Gelman, Murphy and MacKay use it as the rule to follow. Prospect theory names it as “tenet (i) of the theory under attack” — [[kahneman-1979-prospect/main]]. Kahneman also reports a stronger critique: “the rational-model benchmark Samuelson used; Rabin and Thaler's point, reported by Kahneman, is that if it can be consistent with such a foolish rejection, something is wrong with it” — [[kahneman-2011-thinking/ch31-risk]] (pdf 328).
- **Utility of wealth vs. of changes.** Kahneman's chapter on prospect theory treats it as “the utility-of-wealth account that Rabin's theorem attacks” — [[kahneman-2011-thinking/ch26-prospect]] (pdf 277); prospect theory values gains and losses instead.
- **Linear in probabilities?** The standard form weights utilities by probabilities; “the authors question it via nonlinear weights” — [[kahneman-2011-thinking/appb-choices]] (pdf 438).
- **Maximise or satisfice?** Simon states the maximising rule (quote above) in order to replace it with simpler rules for limited agents (see [[bounded-rationality]]).
- **Origins.** Kahneman ties it to Bernoulli's moral expectation; Thaler to the von Neumann–Morgenstern axioms; McGrayne to Ramsey (quotes above).

## Digests

Decision & game theory: [[kahneman-2011-thinking/ch25-bernoulli]], [[kahneman-2011-thinking/ch26-prospect]], [[kahneman-2011-thinking/ch31-risk]], [[kahneman-2011-thinking/appb-choices]], [[kahneman-2011-thinking/ch19-illusion]], [[osborne-2004-introduction/ch04-mixed-p1]], [[osborne-2004-introduction/ch04-mixed-p2]], [[schelling-1960-conflict/ch07-randomization]], [[simon-1955-behavioral/main]] ·
Bayesian: [[gelman-2013-bda3/ch09-decision]], [[murphy-2023-pml2/ch34-decision]], [[mcgrayne-2011-theory/ch03-many]] ·
Information theory: [[mackay-2003-information/ch36-decision]] ·
Economics & finance: [[thaler-2015-misbehaving/ch04-value]], [[kahneman-1979-prospect/main]], [[grossman-1980-impossibility/main]] ·
Political science: [[shepsle-2010-analyzing/ch02-rationality]], [[shepsle-2010-analyzing/ch09-collective-p2]]
