---
id: gram-schmidt-and-qr
type: concept
fields: [linear-algebra]
n_sources: 17
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p2, axler-2024-ladr/ch07-operators-p2, axler-2024-ladr/ch09-multilinear-p2, boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch05-linear, boyd-2018-vmls/ch10-matrix, boyd-2018-vmls/ch11-matrix, boyd-2018-vmls/ch14-least, boyd-2018-vmls/ch16-constrained, boyd-2018-vmls/ch18-nonlinear, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch04-matrix-p1, strang-2023-introduction/ch04-orthogonality-p2, strang-2023-introduction/ch05-determinants, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch08-linear]
raw_ids: [Gram–Schmidt and QR]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# gram-schmidt-and-qr

## Canon spine entry

- **Gram–Schmidt and QR** (linear-algebra): turning any basis into an orthonormal one; A = QR (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p2]] (p. 201): procedure 6.32 turning an independent list into an orthonormal one with the same nested spans; QR itself is not in these pages
- [[axler-2024-ladr/ch07-operators-p2]] (p. 264): $A=QR$ for square $A$ with independent columns, $Q$ unitary, $R$ upper triangular with positive diagonal; unique [as `Gram–Schmidt and QR`]
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 365): used in the proof of Hadamard's inequality [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/app-appendices]] (p. 442): QR factorization costs $2mn^2$ flops [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/ch05-linear]] (p. 97): only the Gram–Schmidt algorithm appears; QR is not mentioned [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/ch10-matrix]] (p. 190): A = QR with $Q^TQ=I$ and R upper triangular with positive diagonal, from Gram–Schmidt [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/ch11-matrix]] (pp. 206, 208–209): $A^{-1}=R^{-1}Q^T$, used to solve systems and compute inverses [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/ch14-least]] (p. 300): one QR factorization reused for all $K$ least squares problems
- [[boyd-2018-vmls/ch16-constrained]] (p. 348): QR of $[A;C]$ and of $Q_2^T$ yields Algorithm 16.2 [as `Gram–Schmidt and QR`]
- [[boyd-2018-vmls/ch18-nonlinear]] (p. 393): used to cost an LM step at $2(m+n)n^2$ flops
- [[deisenroth-2020-mml/ch03-analytic]] (p. 89): iterative orthogonalisation; here only the Gram–Schmidt part, no QR [as `Gram–Schmidt and QR`]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 112): used here to orthogonalise eigenvectors within one eigenspace [as `Gram–Schmidt and QR`]
- [[strang-2023-introduction/ch04-orthogonality-p2]] (pp. 180, 182): subtract earlier projections from each new vector, then normalize; gives $A=QR$, $R=Q^{\mathsf T}A$ upper triangular
- [[strang-2023-introduction/ch05-determinants]] (p. 213): E = QR; |det E| = |det R| = product of heights [as `Gram–Schmidt and QR`]
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 256): used to turn X into QR in Schur's argument
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 284): A = QR used in each QR-algorithm step
- [[strang-2023-introduction/ch08-linear]] (p. 333): orthogonalizing 1, x, x², … gives the Legendre polynomials

## Candidate bridges

- [same-math] QR factorization ↔ Gram–Schmidt and QR (canon): $Q$ is the Gram–Schmidt output and $R_{j,k}=\langle v_k,e_j\rangle$. — from [[axler-2024-ladr/ch07-operators-p2]] (linear-algebra → other)
