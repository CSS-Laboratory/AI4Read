---
id: quadratic-approximation
type: concept
fields: [bayesian]
n_sources: 3
tiers: [core]
grounding: digests
sources: [mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch05-multivariate-p1]
generated_by: build_kg.py
---

# quadratic-approximation

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch02-small]] (pp. 41, 43): Gaussian approximation at the posterior mode, using the curvature there; improves with more data [new]
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (p. 86): Gaussian approximation to the posterior at its MAP peak, fit with `map` [new]
- [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (p. 137): the text calls the `precis` output of a `map` fit the "quadratic approximate posterior" [new]

## Instances that use it

- [[globe-tossing]] — W L W W W L W L W (6 W, 3 L); binomial likelihood; grid and quadratic approximation — from [[mcelreath-2020-rethinking/ch02-small]]

## Candidate bridges

- [same-math] Quadratic approximation ↔ Gaussian (Laplace-type) approximation of a density at its mode using the second derivative of the log density (the chapter gives only the mode-plus-Hessian procedure). — from [[mcelreath-2020-rethinking/ch02-small]] (bayesian → unspecified)
- [structural-analogy] Multivariate Gaussian prior on varying effects ↔ bayesian: the vcov of a quadratic approximation, the same kind of distribution (the text says this, p. 389) — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → bayesian)
