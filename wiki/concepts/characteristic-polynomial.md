---
id: characteristic-polynomial
type: concept
fields: [linear-algebra]
n_sources: 13
tiers: [deep, core]
grounding: digests
sources: [axler-2024-ladr/ch08-operators, axler-2024-ladr/ch09-multilinear-p2, deisenroth-2020-mml/ch04-matrix-p1, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch41-expected, spielman-2025-sagt/ch42-quadrature, spielman-2025-sagt/ch43-ramanujan, spielman-2025-sagt/ch44-bipartite, spielman-2025-sagt/ch45-matching, strang-2023-introduction/ch06-eigenvalues-p1, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3]
raw_ids: [characteristic polynomial]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# characteristic-polynomial

## Canon spine entry

- **characteristic polynomial** (linear-algebra): det(A − λI); its roots are the eigenvalues (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch08-operators]] (p. 311): here $\prod(z-\lambda_k)^{d_k}$ over $\mathbf C$, defined by multiplicities, not determinants
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 363): here defined for any $V$ as $z\mapsto\det(zI-T)$ [as `characteristic polynomial`]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 104–106): $p_A(\lambda)=\det(A-\lambda I)$; roots are the eigenvalues; $c_0=\det A$, $c_{n-1}=(-1)^{n-1}\operatorname{tr}A$ [as `characteristic polynomial`]
- [[spielman-2025-sagt/ch01-introduction]] (p. 5): $\det(xI-M)$; roots are the eigenvalues
- [[spielman-2025-sagt/ch13-random]] (p. 123): $\det(xI-A)=\sum x^{n-k}(-1)^k\sigma_k(A)$
- [[spielman-2025-sagt/ch41-expected]] (p. 327): $\chi_x(M)=\det(xI-M)$
- [[spielman-2025-sagt/ch42-quadrature]] (p. 333): $\chi_x(M)$; here averaged over random matrices
- [[spielman-2025-sagt/ch43-ramanujan]] (p. 342): $\chi_x(\cdot)$, whose roots are eigenvalues; here averaged over random permutations
- [[spielman-2025-sagt/ch44-bipartite]] (p. 350): $\chi_x(M)=\det(xI-M)$; the chapter works with it instead of eigenvalues directly [as `characteristic polynomial`]
- [[spielman-2025-sagt/ch45-matching]] (p. 359): $\det(xI-A_G)$; equals $\mu_x$ for trees
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 220): det(A − λI), degree n; roots are the eigenvalues [as `characteristic polynomial`]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 237): det(A − λI) = 0 gives eigenvalues; for Fibonacci λ² − λ − 1
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 263): det(A − λI); for real A it has real coefficients, so complex roots come in conjugate pairs

## Instances that use it

- [[ex-upper-triangular-6-7]] — matrix with eigenvalues 6 (multiplicity 2) and 7: multiplicity, characteristic polynomial, block form — from [[axler-2024-ladr/ch08-operators]]

## Candidate bridges

- [structural-analogy] Matching closed-loop characteristic polynomial coefficients (2.26)–(2.28) ↔ control theory: pole placement by state feedback — both choose gains to put closed-loop roots where wanted (the chapter only points to later chapters, p. 2-28). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → control-theory)
- [same-math] Poles as eigenvalues of $A$ ↔ linear algebra: roots of $\det(sI-A)$ — the same characteristic polynomial. — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (control-theory → linear-algebra)
- [structural-analogy] Root locus asymptotes and the closed-loop polynomial $a+kb$ ↔ eigenvalue assignment: both study roots of the closed-loop characteristic polynomial. — from [[astrom-2021-feedbacksystems/ch12-frequency]] (control-theory → linear-algebra)
- [structural-analogy] zeros of a polynomial ↔ linear algebra: eigenvalues as zeros of the characteristic polynomial — the unit only says polynomials will be used for maps from a space to itself (p. 119); the link itself is not stated here — from [[axler-2024-ladr/ch04-polynomials]] (linear-algebra → linear-algebra)
- [structural-analogy] eigenvalues as zeros of the minimal polynomial ↔ linear-algebra canon: roots of the characteristic polynomial $\det(A-\lambda I)$ — both are polynomials annihilating $T$ whose roots are the eigenvalues; the characteristic polynomial is not in this unit. — from [[axler-2024-ladr/ch05-eigenvalues-p1]] (linear-algebra → linear-algebra)
- [same-math] Over $\mathbf C$, $\det T$ is the product of eigenvalues ↔ characteristic polynomial and the trace as sum of eigenvalues, since the coefficients are $\operatorname{tr}T$ and $\det T$. — from [[axler-2024-ladr/ch09-multilinear-p2]] (linear-algebra → unspecified)
- [structural-analogy] Haar-averaged characteristic polynomial ↔ free probability: operations independent of eigenvectors, in the finite-$n$ setting — from [[spielman-2025-sagt/ch42-quadrature]] (linear-algebra → other)
- [same-math] det(A − λI) = 0 (p. 205) ↔ linear-algebra: characteristic polynomial, whose roots are eigenvalues. — from [[strang-2023-introduction/ch05-determinants]] (linear-algebra → linear-algebra)
