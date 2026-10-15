---
id: diagonalization
type: concept
fields: [linear-algebra]
n_sources: 10
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p2, axler-2024-ladr/ch07-operators-p1, axler-2024-ladr/ch08-operators, deisenroth-2020-mml/ch04-matrix-p1, spielman-2025-sagt/ch39-testing, spielman-2025-sagt/ch42-quadrature, strang-2023-introduction/ch06-eigenvalues-p1, strang-2023-introduction/ch06-eigenvalues-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch08-linear]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# diagonalization

## Canon spine entry

- **diagonalization** (linear-algebra): A = XΛX⁻¹; in the eigenbasis the map is just independent scalings, so Aᵏ is easy (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p2]] (pp. 163, 165): operator has a diagonal matrix in some basis ⟺ basis of eigenvectors
- [[axler-2024-ladr/ch07-operators-p1]] (p. 243): here "diagonal matrix in an orthonormal basis"
- [[axler-2024-ladr/ch08-operators]] (p. 300): equals having an eigenvector basis; the failure of this motivates the chapter
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 116–118): $A=PDP^{-1}$ exists iff the eigenvectors form a basis of $\mathbb R^n$; $A^k=PD^kP^{-1}$
- [[spielman-2025-sagt/ch39-testing]] (p. 308): $A=\Psi\Lambda\Psi^T$; distinct eigenvalues fix eigenvectors up to sign
- [[spielman-2025-sagt/ch42-quadrature]] (p. 338): rotations diagonalized by a complex $U$ to expose $e^{\pm i\theta}$
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 222): previewed only: needs n independent eigenvectors
- [[strang-2023-introduction/ch06-eigenvalues-p2]] (p. 232–233): A = XΛX⁻¹ when A has n independent eigenvectors; Aᵏ = XΛᵏX⁻¹
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 277): A = XΛX⁻¹, used to get $e^{At}=Xe^{\Lambda t}X^{-1}$
- [[strang-2023-introduction/ch08-linear]] (p. 327): B⁻¹AB = Λ, which needs n independent eigenvectors

## Instances that use it

- [[example-551-diagonalization-by-new-basis]] — $\operatorname{diag}(69,46)$ in basis $(1,4),(7,5)$ — from [[axler-2024-ladr/ch05-eigenvalues-p2]]
- [[fibonacci-diagonalization]] — only as Exercise 21: $T(x,y)=(y,x+y)$ gives exact formula for $F_n$ — from [[axler-2024-ladr/ch05-eigenvalues-p2]]

## Candidate bridges

- [structural-analogy] splitting $V=V_1\oplus\cdots\oplus V_m$ into invariant pieces ↔ diagonalization: in an eigenbasis the map acts independently on each direction (canon link; not stated in this unit). — from [[axler-2024-ladr/ch05-eigenvalues-p1]] (linear-algebra → other)
- [structural-analogy] Fibonacci via diagonalization (Ex. 21) ↔ adjacency matrix: counting walks via $A^k$ by diagonalizing $A$. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Simultaneous diagonalization of commuting operators (5.76) ↔ spectral theorem: orthonormal eigenbasis for symmetric matrices (the text only points forward to 7.29, 7.31). — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
