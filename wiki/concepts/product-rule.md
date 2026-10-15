---
id: product-rule
type: concept
fields: [information-theory, linear-algebra]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, jaynes-2003-probability/ch02-quantitative, stone-2022-information/appf-rules]
generated_by: build_kg.py
---

# product-rule

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch02-quantitative]] (pp. 27–29, 33): $w(AB|C)=w(A|BC)w(B|C)$ forced by associativity and commutativity of the logical product; becomes (2.63) after rescaling [new]
- [[stone-2022-information/appf-rules]] (p. 261): $p(x,y)=p(x|y)p(y)$ [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 184): $p(x,y)=p(y\mid x)p(x)$ [new]

## Instances that use it

- [[weather-chain-product-rule]] — clouds→rain→wet→slippery, product rule estimate 0.0169 — from [[pearl-2016-primer/ch01-preliminaries]]

## Candidate bridges

- [same-math] Prop. 3 and Cor. ↔ probability: product rule $P(A\cap B)=P(A)P(B\mid A)$ — Bayes derives the same rule from expectations. — from [[bayes-1763-essay/main]] (bayesian → other)
- [structural-analogy] multiplicative $w$ (2.26) ↔ information-theory: surprisal $-\log p$ is additive for independent events. Taking $\log w$ turns the product rule into addition, but this unit does not make that move. — from [[jaynes-2003-probability/ch02-quantitative]] (information-theory → information-theory)
- [structural-analogy] Cox-style derivation of the rules ↔ Dutch book argument: two different routes to the same sum and product rules from consistency. — from [[jaynes-2003-probability/ch02-quantitative]] (information-theory → other)
- [same-math] special multiplication theorem $(1_s)$ ↔ probability: product rule for independent events — the same counting identity in frequency form. — from [[popper-1959-logic/appii-following]] (analytic-philosophy → other)
