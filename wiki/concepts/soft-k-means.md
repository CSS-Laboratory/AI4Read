---
id: soft-k-means
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch20-example, mackay-2003-information/ch22-maximum]
generated_by: build_kg.py
---

# soft-k-means

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch20-example]] (p. 289): K-means with soft-min responsibilities and stiffness β [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch22-maximum]] (pp. 303–305): iterate responsibilities and weighted-mean updates; an ML algorithm for fitting a mixture of Gaussians [new; work fields: information-theory, bayesian]

## Instances that use it

- [[soft-k-means-as-em]] — delta-function Q_θ; "kaboom" problem — from [[mackay-2003-information/ch33-variational]]

## Candidate bridges

- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
- [structural-analogy] Gibbs sampling for mixtures ↔ soft K-means: alternate sampling labels and updating parameters, as noted in Ex. 29.16 (p. 383). — from [[mackay-2003-information/ch29-monte]] (information-theory → information-theory)
