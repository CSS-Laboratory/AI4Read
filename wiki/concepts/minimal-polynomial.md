---
id: minimal-polynomial
type: concept
fields: [linear-algebra]
n_sources: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch05-eigenvalues-p2, axler-2024-ladr/ch07-operators-p1, axler-2024-ladr/ch08-operators]
generated_by: build_kg.py
---

# minimal-polynomial

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p1]] (pp. 144–146): unique monic polynomial of least degree with $p(T)=0$; degree $\le\dim V$; its zeros are the eigenvalues [new]
- [[axler-2024-ladr/ch05-eigenvalues-p2]] (pp. 157, 159, 169): smallest-degree monic polynomial $p$ with $p(T)=0$; its zeros are the eigenvalues; here it decides triangularizability and diagonalizability [new]
- [[axler-2024-ladr/ch07-operators-p1]] (p. 244): used in 7.27 to show self-adjoint operators have real linear factors only [new]
- [[axler-2024-ladr/ch08-operators]] (pp. 305, 312): the minimal polynomial from Chapter 5 (not re-defined here); for nilpotent $T$ it is $z^m$, and over $\mathbf C$ it divides the characteristic polynomial [new]

## Instances that use it

- [[companion-style-matrix-5x5]] — minimal polynomial $3-6z+z^5$ (Examples 5.26, 5.28) — from [[axler-2024-ladr/ch05-eigenvalues-p1]]
- [[example-561-non-diagonalizable-via-minimal-polynomial]] — minimal polynomial $(z-6)^2(z-7)$ — from [[axler-2024-ladr/ch05-eigenvalues-p2]]

## Candidate bridges

- [structural-analogy] eigenvalues as zeros of the minimal polynomial ↔ linear-algebra canon: roots of the characteristic polynomial $\det(A-\lambda I)$ — both are polynomials annihilating $T$ whose roots are the eigenvalues; the characteristic polynomial is not in this unit. — from [[axler-2024-ladr/ch05-eigenvalues-p1]] (linear-algebra → linear-algebra)
