---
id: risk-aversion
type: concept
fields: [decision-game-theory]
n_sources: 10
tiers: [core]
grounding: digests
sources: [kahneman-1979-prospect/main, kahneman-2011-thinking/appb-choices, kahneman-2011-thinking/ch19-illusion, kahneman-2011-thinking/ch25-bernoulli, kahneman-2011-thinking/ch26-prospect, kahneman-2011-thinking/ch29-fourfold, kahneman-2011-thinking/ch31-risk, kahneman-2011-thinking/ch34-frames, osborne-2004-introduction/ch04-mixed-p1, osborne-2004-introduction/ch09-bayesian]
raw_ids: [risk aversion]
canon_spine: decision-game-theory
generated_by: build_kg.py
---

# risk-aversion

## Canon spine entry

- **risk aversion** (decision-game-theory): preferring a sure amount to a gamble with the same expected value; concave utility (UG)

## Definitions in the sources

### decision-game-theory

- [[kahneman-1979-prospect/main]] (p. 264): preferring a sure $x$ to any risky prospect with expected value $x$; in expected utility equivalent to concave $u$ [as `risk aversion`]
- [[kahneman-2011-thinking/appb-choices]] (pdf 432): preferring a sure outcome to a gamble of higher or equal expectation; here explained by concave value of gains [as `risk aversion`]
- [[kahneman-2011-thinking/ch19-illusion]] (pdf 199): here, bureaucratic caution of agents fearing hindsight scrutiny
- [[kahneman-2011-thinking/ch25-bernoulli]] (pdf 265): preferring a sure thing to a gamble of equal or slightly higher expected value, which Bernoulli proposed is explained by diminishing marginal utility [as `risk aversion`]
- [[kahneman-2011-thinking/ch26-prospect]] (pdf 271, 277): preferring a sure gain; here also strong in mixed gambles because of loss aversion
- [[kahneman-2011-thinking/ch29-fourfold]] (pdf 309): preferring a sure amount to a gamble of equal expected value, as used in Figure 13 [as `risk aversion`]
- [[kahneman-2011-thinking/ch31-risk]] (pdf 326): here, the preference for a sure gain; paired with risk seeking in the loss domain
- [[kahneman-2011-thinking/ch34-frames]] (pdf 359): tending to prefer the sure thing when outcomes are good; Kahneman adds that people tend to be risk seeking when both outcomes are negative
- [[osborne-2004-introduction/ch04-mixed-p1]] (p. 101): here: preferring $z$ for sure to a lottery averaging $z$; risk neutral = payoff equals money; both compatible with expected-payoff preferences
- [[osborne-2004-introduction/ch09-bayesian]] (p. 295): payoff $x^{1/m}$ in Exercise 295.1; revenue equivalence assumes risk neutrality

## Instances that use it

- [[rich-democracies-live-longer]] — risk-aversion explanation and its testable implication — from [[clark-2017-principles/ch02-science]]
- [[anthony-and-betty]] — same final-wealth options, a gain frame versus a loss frame; risk aversion versus risk seeking — from [[kahneman-2011-thinking/ch25-bernoulli]]

## Candidate bridges

- [same-math] CARA-normal demand $X=(E[u]-RP)/(a\,Var[u])$ ↔ economics-finance: mean-variance optimization — expected utility is a mean-variance expression with risk-aversion weight $a$ (the paper does not itself name mean-variance). — from [[grossman-1980-impossibility/main]] (economics-finance → economics-finance)
- [same-math] concave value for gains ↔ decision-game-theory: concave utility gives risk aversion — the same curve-shape argument, here applied to gains and losses separately. — from [[kahneman-2011-thinking/appb-choices]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Bernoulli's concave utility ↔ risk aversion in finance (canon: mean-variance optimization) — concavity makes a sure amount preferred to a gamble with the same mean. — from [[thaler-2015-misbehaving/ch04-value]] (economics-finance → economics-finance)
