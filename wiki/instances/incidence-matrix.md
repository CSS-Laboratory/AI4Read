---
id: incidence-matrix
type: instance
fields: [linear-algebra]
n_sources: 1
tiers: [core]
grounding: digests
sources: [strang-2023-introduction/ch04-orthogonality-p2]
canon_instance: [incidence-matrices-and-kirchhoffs-laws]
canon_match_rule: confirmed
generated_by: build_kg.py
---

# incidence-matrix

## Canon entry

- **Incidence matrices and Kirchhoff's laws** (linear-algebra): a network's incidence matrix encodes conservation laws, and BᵀB is the graph Laplacian — strang-2010-mit1806, strang-2018-matrixmethods

## Descriptions in the sources

### linear-algebra

- [[strang-2023-introduction/ch04-orthogonality-p2]] (pp. 194–195): graph example with $m=5,n=4,r=3$; $A^+$ computed exactly via $CR$; $A^{\mathsf T}y=0$ is Kirchhoff's law

## Candidate bridges

- [structural-analogy] Incidence matrix of a chain graph ↔ difference matrix $D$ ↔ first-order differences as convolution with $(1,-1)$. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → unspecified)
- [same-math] diffusion system with incidence matrix $A$ ↔ network analysis: flow conservation on a graph uses the incidence matrix — the same $A$ as in §7.3. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → complex-systems)
- [structural-analogy] Supply chain incidence matrix ↔ graph models: $A^{\rm sc}f$ converts edge flows into node changes. — from [[boyd-2018-vmls/ch09-linear]] (linear-algebra → other:graph-models)
- [structural-analogy] diffusion on a grid (heat) ↔ graph Laplacian (canon): incidence matrix $A$ and a resistance matrix $R$ appear in the system — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [same-math] Dirichlet energy $\|A^Tx\|^2$ (incidence matrix) ↔ linear-algebra canon: graph Laplacian quadratic form $\sum(x_i-x_j)^2$ — both are $x^T(AA^T)x$ for the incidence matrix $A$. — from [[boyd-2018-vmls/ch15-multi]] (linear-algebra → linear-algebra)
- [same-math] AᵀA with A a ±1 difference matrix (Example 3, p. 70; B₃ = AᵀA) ↔ graph theory: Laplacian L = BᵀB of an incidence matrix — same product of a ±1 edge-difference matrix with its transpose. — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other:graph-theory)
- [structural-analogy] Left nullspace of an incidence matrix ↔ network science: loop currents / cycle space — independent loops count m − n + 1. — from [[strang-2023-introduction/ch03-four-p3]] (linear-algebra → complex-systems)
- [same-math] Incidence matrix constraint Aᵀy = 0 in max flow ↔ graph theory: incidence matrix and conservation of flow at nodes. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → other:graph-theory)
