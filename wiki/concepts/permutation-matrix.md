---
id: permutation-matrix
type: concept
fields: [linear-algebra]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch07-matrix, spielman-2025-sagt/ch39-testing, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch02-solving-p2]
generated_by: build_kg.py
---

# permutation-matrix

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch07-matrix]] (p. 132): square matrix such that both $A$ and $A^T$ are selectors; reorders entries [new]
- [[spielman-2025-sagt/ch39-testing]] (p. 308): $\Pi(a,b)=1$ iff $\pi(a)=b$ [new]
- [[strang-2023-introduction/ch02-solving-p1]] (p. 45): P exchanges rows to avoid a zero pivot; there are n! of them [new]
- [[strang-2023-introduction/ch02-solving-p2]] (p. 64): matrix with the rows of I in some order; n! of them; Pᵀ = P⁻¹ [new]

## Instances that use it

- [[permutation-matrix-example]] — the 3×3 matrix sending (a,b,c) to (b,c,a) — from [[prince-2023-udl/ch22-mathematics]]
- [[permutation-matrix]] — every permutation matrix is orthogonal — from [[strang-2023-introduction/ch04-orthogonality-p2]]
