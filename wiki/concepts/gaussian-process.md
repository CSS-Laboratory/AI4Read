---
id: gaussian-process
type: concept
fields: [bayesian, information-theory, linear-algebra]
fields_strong: [bayesian, information-theory, linear-algebra]
n_sources: 4
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, gelman-2013-bda3/ch21-gaussian, mackay-2003-information/ch45-gaussian, murphy-2023-pml2/ch18-gaussian-p1]
generated_by: build_kg.py
---

# gaussian-process

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch21-gaussian]] (p. 501): random function whose values at any finite set of points are multivariate normal; defined by mean function $m$ and covariance function $k$ [new]
- [[murphy-2023-pml2/ch18-gaussian-p1]] (p. 681): prior over functions: any finite set of values is jointly Gaussian; set by mean and kernel [new]

### information-theory

- [[mackay-2003-information/ch45-gaussian]] (pp. 535, 540): a distribution over functions such that any finite set of function values is jointly Gaussian; given by mean and covariance function [new; work fields: information-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (p. 316): regression model with a distribution placed directly on functions [new]

## Instances that use it

- [[spline-prior-as-gp]] — cubic-spline smoothing is MAP under a Gaussian-process prior — from [[mackay-2003-information/ch45-gaussian]]
- [[neal-infinite-network-gp]] — one-hidden-layer network converges to a Gaussian process — from [[mackay-2003-information/ch45-gaussian]]
- [[kriging]] — identical, per MacKay, to Gaussian-process regression — from [[mackay-2003-information/ch45-gaussian]]
- [[oceanic-tools-gaussian-process]] — tool counts with geographic-distance covariance — from [[mcelreath-2020-rethinking/ch13-adventures]]
- [[gaussian-process]] — BNP prior over functions with jointly Gaussian finite marginals — from [[murphy-2023-pml2/ch32-representation]]
- [[gaussian-process-information-rate]] — Szegő-based formula, Example 6.4 — from [[polyanskiy-2025-information/ch07-tensorization]]
- [[gaussian-process-ergodicity]] — Cesàro decay of $c(n)$ gives ergodicity — from [[polyanskiy-2025-information/ch14-entropy]]

## Candidate bridges

- [same-math] Entropy rate ↔ prediction: (11.40) links entropy rate to minimum mean squared prediction error for Gaussian processes. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other:prediction)
- [structural-analogy] Distribution over functions induced by $p(\theta)$ ↔ Gaussian processes (author calls them closely related). — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → unspecified)
- [structural-analogy] Gaussian-process kernel (covariance falls with distance) ↔ spatial statistics: spatial autocorrelation — covariance as a function of separation — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → other:statistics)
- [same-math] Szegő limit of $\frac1n\sum\log\sigma_j^2$ to the spectral integral ↔ entropy rate of a Gaussian process (the chapter points to (6.12)). — from [[polyanskiy-2025-information/ch22-channels]] (information-theory → unspecified)
- [structural-analogy] Minimum norm brain imaging ↔ Gaussian process regression — the text says the Bayesian reading is equivalent to statistical inversion/GP regression (p. 5). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
