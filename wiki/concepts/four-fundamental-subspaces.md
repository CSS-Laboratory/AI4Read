---
id: four-fundamental-subspaces
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 7
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch07-operators-p1, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch04-orthogonality-p2, strang-2023-introduction/ch06-eigenvalues-p3, strang-2023-introduction/ch07-singular]
raw_ids: [four fundamental subspaces]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# four-fundamental-subspaces

## Canon spine entry

- **four fundamental subspaces** (linear-algebra): column space, null space, row space, and left null space, which come in orthogonal pairs (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch07-operators-p1]] (p. 231): here $\operatorname{null}T^*=(\operatorname{range}T)^\perp$ etc. (7.6)
- [[strang-2023-introduction/ch03-four-p1]] (p. 84): column space, row space, nullspace of A and of Aᵀ; only announced here [as `four fundamental subspaces`]
- [[strang-2023-introduction/ch03-four-p3]] (p. 129): C(Aᵀ) and N(A) in ℝⁿ, C(A) and N(Aᵀ) in ℝᵐ, with dimensions r, n − r, r, m − r [as `four fundamental subspaces`]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 144–146): here shown as two orthogonal pairs: C(Aᵀ) ⊥ N(A) and C(A) ⊥ N(Aᵀ)
- [[strang-2023-introduction/ch04-orthogonality-p2]] (p. 191): used to define $A^+$
- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 264): in the complex case C(Āᵀ) and N(Āᵀ) replace C(Aᵀ) and N(Aᵀ)
- [[strang-2023-introduction/ch07-singular]] (p. 286, p. 289): $v$'s span row space and nullspace; $u$'s span column space and left nullspace

## Candidate bridges

- [same-math] adjoint $T^*$ with real entries = transpose ↔ the transpose in $\operatorname{null}(A^{\mathrm t})=(\operatorname{col}A)^\perp$ (four fundamental subspaces): 7.6 over $\mathbf R$ with orthonormal bases. — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → other:the-transpose-in-operatornamenullamathrm)
