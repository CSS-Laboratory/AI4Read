---
id: slice-sampling
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch12-computationally, mackay-2003-information/ch29-monte, murphy-2023-pml2/ch12-markov-p1]
generated_by: build_kg.py
---

# slice-sampling

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch12-computationally]] (p. 297): iterative sampling from the uniform distribution under the density curve [new]
- [[murphy-2023-pml2/ch12-markov-p1]] (pp. 514–515): uniform height variable $v$; sample $x$ from $\{x:\tilde p(x)\ge v\}$ [new]

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 374–375): sample uniformly under the curve P* via interval stepping-out and shrinking; self-tuning step size [new; work fields: information-theory, bayesian]

## Instances that use it

- [[binomial-logistic-regression-slice]] — slice sampling vs grid posterior — from [[murphy-2023-pml2/ch12-markov-p1]]

## Candidate bridges

- [structural-analogy] Sampling under a curve (rejection and slice sampling) ↔ geometry: x-marginal of a uniform distribution under P* is P (p. 364–365, 375). — from [[mackay-2003-information/ch29-monte]] (information-theory → other:mathematics)
