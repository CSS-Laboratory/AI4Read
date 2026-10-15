---
id: cholesky-sampling
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, gelman-2013-bda3/appa-standard]
generated_by: build_kg.py
---

# cholesky-sampling

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appa-standard]] (p. 582): draw $\mu+Az$ with $AA^T=\Sigma$ to get a multivariate normal [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 204): sample $y=Ax+\mu$ with $AA^\top=\Sigma$, $A$ triangular [new]

## Candidate bridges

- [same-math] Cholesky sampling of a Gaussian with covariance $\Sigma=LL^\top$ ↔ probability (Chapter 6): linear transformation of random variables (as sketched on p. 115). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other:probability)
- [same-math] Cholesky sampling $\Sigma=AA^\top$ ↔ linear-algebra: Cholesky factorization of a symmetric positive definite matrix. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
