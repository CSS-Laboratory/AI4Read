---
id: transpose
type: concept
fields: [linear-algebra]
n_sources: 3
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p2, deisenroth-2020-mml/ch02-linear-p1, strang-2023-introduction/ch02-solving-p2]
generated_by: build_kg.py
---

# transpose

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p2]] (p. 77): $A^t$ with $(A^t)_{k,j}=A_{j,k}$ [new]
- [[deisenroth-2020-mml/ch02-linear-p1]] (p. 25): $b_{ij}=a_{ji}$; $(AB)^\top=B^\top A^\top$ [new]
- [[strang-2023-introduction/ch02-solving-p2]] (pp. 67–68): (Aᵀ)ᵢⱼ = Aⱼᵢ; defined better by (Ax)ᵀy = xᵀ(Aᵀy) [new]

## Instances that use it

- [[difference-matrix-transpose-example]] — A = [[−1,1,0],[0,−1,1]] with (Ax)ᵀy = xᵀ(Aᵀy) — from [[strang-2023-introduction/ch02-solving-p2]]
- [[d-dt-antisymmetric]] — transpose of d/dt is −d/dt by integration by parts — from [[strang-2023-introduction/ch02-solving-p2]]

## Candidate bridges

- [same-math] ℳ(T′)=ℳ(T)ᵗ ↔ linear-algebra: transpose matrix Aᵗ acting on row vectors. The dual map is the coordinate-free transpose. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [same-math] adjoint $T^*$ with real entries = transpose ↔ the transpose in $\operatorname{null}(A^{\mathrm t})=(\operatorname{col}A)^\perp$ (four fundamental subspaces): 7.6 over $\mathbf R$ with orthonormal bases. — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → other)
- [same-math] Jacobian ∂y/∂x = Aᵀ for y = Ax ↔ backpropagation through a linear layer: the same transpose-of-weights rule. — from [[prince-2023-udl/ch22-mathematics]] (llm → other)
- [same-math] AᵀA with A a ±1 difference matrix (Example 3, p. 70; B₃ = AᵀA) ↔ graph theory: Laplacian L = BᵀB of an incidence matrix — same product of a ±1 edge-difference matrix with its transpose. — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other)
- [structural-analogy] transpose of d/dt is −d/dt ↔ functional analysis: adjoint operator defined by ⟨Ax,y⟩ = ⟨x,A*y⟩ — same defining inner-product identity, on functions. — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other)
- [structural-analogy] Kirchhoff's law $A^{\mathsf T}y=0$ ↔ graph Laplacian and network flow: nullspace of the incidence transpose. — from [[strang-2023-introduction/ch04-orthogonality-p2]] (linear-algebra → other)
