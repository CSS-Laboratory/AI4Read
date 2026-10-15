---
id: map-estimate
type: concept
fields: [bayesian, information-theory, control-theory]
n_sources: 5
tiers: [core, reference, deep]
grounding: digests
sources: [mackay-2003-information/ch22-maximum, mackay-2003-information/ch41-learning, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch07-inference, sarkka-2023-bayesianfiltering/ch07-extended]
generated_by: build_kg.py
---

# map-estimate

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 65): posterior mode; equals the MLE under a uniform prior [new]
- [[murphy-2023-pml2/ch07-inference]] (p. 349): posterior mode, treated as a delta distribution [new]

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 306): maximizing the posterior density; it often shares ML's problems, and its answer usually changes with the parametrization [new]
- [[mackay-2003-information/ch41-learning]] (p. 493): $\mathbf w_{\rm MP}$, the (locally) most probable weights found by minimizing $M$ [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 121): state maximising the posterior; here the minimiser of $L$ [new]

## Candidate bridges

- [structural-analogy] Min–sum (Viterbi) most-probable path ↔ bayesian: MAP estimate versus full posterior — path cost is a negative log-likelihood under the binary symmetric channel. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
- [same-math] `lm` with flat priors ↔ Bayesian inference: under flat priors and a Gaussian likelihood the OLS estimates equal the MAP estimates (p. 159). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → bayesian)
