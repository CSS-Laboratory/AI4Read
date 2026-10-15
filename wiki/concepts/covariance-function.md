---
id: covariance-function
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch21-gaussian, mackay-2003-information/ch45-gaussian]
generated_by: build_kg.py
---

# covariance-function

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch21-gaussian]] (pp. 501–502): $k(x,x')$, controls smoothness and shrinkage; sums and products are again covariance functions [new]

### information-theory

- [[mackay-2003-information/ch45-gaussian]] (pp. 535, 543): $C(x,x')$, the expected covariance of $y$ at two points; its only constraint is non-negative-definiteness [new; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] GP covariance function ↔ kernel methods: the kernel in SVMs, which MacKay says is another name for it (p. 548). — from [[mackay-2003-information/ch45-gaussian]] (information-theory → llm)
