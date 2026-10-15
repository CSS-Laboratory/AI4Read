---
id: explaining-away
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch21-exact, murphy-2023-pml2/ch04-graphical-p1, pearl-2018-bookofwhy/ch05-smoke]
generated_by: build_kg.py
---

# explaining-away

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 151–153): conditioning on a common effect couples its causes; also called Berkson's paradox, inter-causal reasoning [new]
- [[pearl-2018-bookofwhy/ch05-smoke]] (pdf 173): in the example, learning that a mother smokes explains away a baby's low weight and lowers the likelihood of a birth defect [new]

### information-theory

- [[mackay-2003-information/ch21-exact]] (p. 295): one cause becomes less probable when an alternative cause of the same data becomes more probable, though the causes were independent a priori [new; work fields: information-theory, bayesian]

## Instances that use it

- [[burglar-alarm]] — noisy-or network showing posterior enumeration and explaining away — from [[mackay-2003-information/ch21-exact]]
- [[student-network]] — five-variable Bayes net (D, I, G, S, L) used for factorization, explaining away, inference and counting-based learning — from [[murphy-2023-pml2/ch04-graphical-p1]]

## Candidate bridges

- [structural-analogy] Conditioning on a collider creates dependence between causes ↔ Bayesian: "explaining away" in posterior inference — learning the effect couples its independent causes. — from [[hernan-2020-whatif/ch06-graphical]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning opens a path (M-bias) ↔ Bayesian networks: "explaining away", where conditioning on a common effect makes independent causes dependent — the same path logic. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → bayesian)
- [structural-analogy] explaining away ↔ bayesian: conditioning on a common effect (collider, b→a←e) makes independent causes dependent (canon link; not stated in this unit) — from [[mackay-2003-information/ch21-exact]] (information-theory → bayesian)
- [structural-analogy] Collider/explaining away ↔ causal inference: conditioning on a common effect opens a spurious path, as in selection bias — the text itself calls the two-coin and Gaussian cases selection bias. — from [[murphy-2023-pml2/ch04-graphical-p1]] (bayesian → bayesian)
- [structural-analogy] RBM versus directed two-layer model ↔ explaining away in causal DAGs (p. 172). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → unspecified)
- [structural-analogy] Collider conditioning (m-bias) ↔ bayesian: "explaining away" in Bayesian networks. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning ↔ Bayesian inference: "explaining away" of one cause given the effect (named on p. 51) — the posterior over causes becomes dependent. — from [[pearl-2016-primer/ch02-graphical]] (bayesian → bayesian)
- [structural-analogy] Collider bias ↔ Bayes' theorem/explaining away: learning one cause lowers belief in another cause of the same effect. — from [[pearl-2018-bookofwhy/ch05-smoke]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning ↔ Bayesian explaining-away: both create dependence between independent causes once their common effect is observed (pdf 181, 184). — from [[pearl-2018-bookofwhy/ch06-paradoxes]] (bayesian → bayesian)
