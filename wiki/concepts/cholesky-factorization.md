---
id: cholesky-factorization
type: concept
fields: [linear-algebra, bayesian]
fields_strong: [linear-algebra, bayesian]
n_sources: 5
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p2, deisenroth-2020-mml/ch04-matrix-p1, mcelreath-2020-rethinking/ch13-adventures, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch06-eigenvalues-p2]
aliases: [cholesky-decomposition]
generated_by: build_kg.py
---

# cholesky-factorization

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `cholesky-decomposition` — 2 digest(s)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p2]] (p. 267): $B=R^*R$ with $R$ upper triangular, positive diagonal, for positive definite $B$ [new]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 114): $A=LL^\top$, $L$ lower-triangular with positive diagonal, unique, for symmetric PD $A$ [alias `cholesky-decomposition`; new]
- [[strang-2023-introduction/app1-ranks]] (p. 401): S = CᵀC for symmetric positive definite S [new]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 250): S = AᵀA with A = √D Lᵀ upper triangular from elimination [new]

### bayesian

- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 409): $\mathbf R=\mathbf L\mathbf L^\top$; $\mathbf L$ times uncorrelated samples gives correlated samples [alias `cholesky-decomposition`; new]

## Candidate bridges

- [same-math] Cholesky sampling $\Sigma=AA^\top$ ↔ linear-algebra: Cholesky factorization of a symmetric positive definite matrix. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
