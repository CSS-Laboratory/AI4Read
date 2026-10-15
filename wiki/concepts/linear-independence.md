---
id: linear-independence
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 22
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch02-finite, axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch04-polynomials, axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch09-multilinear-p1, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch05-linear, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch11-matrix, boyd-2018-vmls/ch12-least, boyd-2018-vmls/ch13-least, boyd-2018-vmls/ch15-multi, boyd-2018-vmls/ch18-nonlinear, bryan-2006-eigenvector/main, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch02-linear-p2, spielman-2025-sagt/ch09-strongly, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch04-orthogonality-p1]
raw_ids: [linear independence]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# linear-independence

## Canon spine entry

- **linear independence** (linear-algebra): no vector in the set is a combination of the others; nothing is redundant (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch02-finite]] (p. 32): only the all-zero scalars give the zero combination; equivalently, representations in the span are unique [as `linear independence`]
- [[axler-2024-ladr/ch03-linear-p1]] (p. 54, 62–63): used throughout the proofs [as `linear independence`]
- [[axler-2024-ladr/ch04-polynomials]] (p. 124): the list (4.10) is independent because its members have distinct degrees
- [[axler-2024-ladr/ch05-eigenvalues-p1]] (pp. 136, 144): used to bound the number of eigenvalues and to build the minimal polynomial
- [[axler-2024-ladr/ch09-multilinear-p1]] (p. 352): the nonzero alternating $n$-linear form detects it when $n=\dim V$
- [[boyd-2018-vmls/ch02-linear]]: not used in this unit. [weak: not really used in this unit]
- [[boyd-2018-vmls/ch05-linear]] (pp. 89–91): only all-zero coefficients give the zero vector, (5.1); equivalent to unique coefficients [as `linear independence`]
- [[boyd-2018-vmls/ch06-matrices]] (p. 121): columns of $A$ independent if $Ax=0$ implies $x=0$ [as `linear independence`]
- [[boyd-2018-vmls/ch11-matrix]] (pp. 200–201): here linked to inverses: independent columns ⟺ left-invertible, independent rows ⟺ right-invertible [as `linear independence`]
- [[boyd-2018-vmls/ch12-least]] (p. 227): the assumption making the minimizer unique
- [[boyd-2018-vmls/ch13-least]] (pp. 248–249): needed for (13.2). Failure means a redundant basis function on this data [as `linear independence`]
- [[boyd-2018-vmls/ch15-multi]] (p. 310): reused; stacked columns are independent iff no nonzero $x$ has all $A_ix=0$
- [[boyd-2018-vmls/ch18-nonlinear]] (p. 391): needed for the Gauss–Newton step; always achieved in LM by the $\sqrt\lambda I$ block
- [[bryan-2006-eigenvector/main]] (p. 4, 7): used to build the $w^i$ and in Props. 3, Lemma 3.2
- [[deisenroth-2020-mml/ch02-linear-p1]] (pp. 40–42): only the trivial combination gives 0; tested by pivot columns in REF [as `linear independence`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 44, 47): used here via pivot columns of the row-echelon form
- [[spielman-2025-sagt/ch09-strongly]] (p. 89): used for the polynomials $p_i$
- [[strang-2023-introduction/ch01-vectors]] (p. 20): only the zero combination of the columns gives zero; no column is a combination of earlier ones
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 40–43): columns are independent when n nonzero pivots appear; dependent columns give nonzero X with AX = 0
- [[strang-2023-introduction/ch03-four-p1]] (pp. 85, 98): here used as: columns are independent when only x = 0 gives Ax = 0 [as `linear independence`]
- [[strang-2023-introduction/ch03-four-p2]] (p. 115): only $x=0$ gives $Ax=0$ (columns) or $\sum x_iv_i=0$
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 157): independent columns of A are exactly what makes AᵀA invertible

## Candidate bridges

- [structural-analogy] Direct sum (unique decomposition) ↔ linear independence (canon link; not stated in this unit): both say that "nothing is redundant", via uniqueness of the representation of $0$. — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → linear-algebra)
- [metaphor] linear independence ("no vector is redundant") ↔ statistics/data: redundant, collinear features — an informal way to think about dependent lists. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other:statistics)
