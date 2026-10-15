---
id: orthonormal-basis
type: concept
fields: [linear-algebra]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p2, axler-2024-ladr/ch07-operators-p1, deerwester-1990-lsa/main, spielman-2025-sagt/ch02-eigenvalues]
generated_by: build_kg.py
---

# orthonormal-basis

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p2]] (pp. 197, 199, 200): orthonormal list that is a basis; gives coordinates $\langle v,e_k\rangle$
- [[axler-2024-ladr/ch07-operators-p1]] (p. 232): used to turn the adjoint into a conjugate transpose and to state the spectral theorems
- [[deerwester-1990-lsa/main]] (pdf 6): the factors are orthogonal axes; SVD factors are orthogonal axes (pdf 12); the authors note that Koll's hand-chosen dimensions were not truly orthogonal, unlike the axes of factor analysis
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 22): eigenbasis used to expand $x$ with $c_i=\psi_i^Tx$

## Instances that use it

- [[orthonormal-basis-of-p2]] — Gram–Schmidt on $1,x,x^2$ with $\int_{-1}^1$ — from [[axler-2024-ladr/ch06-inner-p2]]
- [[orthonormal-coordinates-example-f4]] — expansion of $(1,2,4,7)$ in a $\pm\frac12$ orthonormal basis — from [[axler-2024-ladr/ch06-inner-p2]]
- [[real-spectral-example-3x3]] — eigenvalues $27,9,-15$ with explicit orthonormal basis — from [[axler-2024-ladr/ch07-operators-p1]]
- [[orthonormal-basis-example-5-3]] — a 3-vector orthonormal basis used to expand $(1,2,3)$ — from [[boyd-2018-vmls/ch05-linear]]

## Candidate bridges

- [same-math] spectral theorem for real symmetric matrices ($S=Q\Lambda Q^{\mathrm t}$) ↔ linear-algebra canon "spectral theorem": 7.29 in matrix form (orthonormal basis ↔ columns of $Q$). — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → linear-algebra)
- [same-math] quadratic form $q(v)=\beta(v,v)$ on $\mathbf R^n$ with symmetric matrix ↔ canon "quadratic form $x^{\mathsf T}Sx$": the same function, shown diagonalisable by an orthonormal basis (9.23b). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other)
- [same-math] Diagonalising a symmetric form in an orthonormal basis (9.13) ↔ spectral theorem: it follows from that theorem, using $C^{-1}=C^{\mathrm t}$. — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → linear-algebra)
- [same-math] Orthonormal expansion $x=\sum(a_i^Tx)a_i$ ↔ linear-algebra: coordinates in an orthonormal basis (canon link; not stated in this unit). — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] Projection onto an orthonormal basis $\lambda=B^\top x$ ↔ Fourier series: coordinates are inner products with orthogonal functions (p. 81, 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
