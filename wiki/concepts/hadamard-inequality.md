---
id: hadamard-inequality
type: concept
fields: [information-theory, linear-algebra]
n_sources: 3
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch09-multilinear-p2, cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian]
generated_by: build_kg.py
---

# hadamard-inequality

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch09-differential]] (p. 233): $|K|\le\prod K_{ii}$, derived from $h$ subadditivity for normals [new]
- [[cover-2006-elements/ch10-gaussian]] (p. 255): $|K|\le\prod K_{ii}$ for positive definite $K$, equality iff diagonal [new]

### linear-algebra

- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 365): $|\det A|\le\prod\|v_k\|$ [new]

## Instances that use it

- [[hadamard-inequality]] — $|K|\le\prod K_{ii}$ via independence bound on entropy — from [[cover-2006-elements/ch16-inequalities]]

## Candidate bridges

- [same-math] Hadamard's inequality ↔ linear algebra: $|K|\le\prod K_{ii}$ for covariance matrices, from $h(X_1..X_n)\le\sum h(X_i)$ (p. 233). — from [[cover-2006-elements/ch09-differential]] (information-theory → linear-algebra)
