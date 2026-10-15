---
id: incidence-matrix
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 10
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch08-linear, boyd-2018-vmls/ch09-linear, boyd-2018-vmls/ch15-multi, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch14-approximating, spielman-2025-sagt/ch30-simple, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch09-linear]
raw_ids: [incidence matrix]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# incidence-matrix

## Canon spine entry

- **incidence matrix** (linear-algebra): edges × nodes with ±1 entries; a graph as a difference operator (UG)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch07-matrix]] (p. 133): $n\times m$ matrix of a directed graph, $\pm1$ entries per edge; flows to net node flows [as `incidence matrix`]
- [[boyd-2018-vmls/ch08-linear]] (p. 156): here used for flow conservation $Af+s=0$
- [[boyd-2018-vmls/ch09-linear]] (p. 171): $A^{\rm sc}$, $n\times m$; converts link flows into net inflow at nodes [as `incidence matrix`]
- [[boyd-2018-vmls/ch15-multi]] (p. 317): reused; defines the Dirichlet energy
- [[spielman-2025-sagt/ch11-walks]] (p. 108): signed edge–vertex matrix $U$ with rows $\delta_a^T-\delta_b^T$
- [[spielman-2025-sagt/ch13-random]] (p. 125): $U$, the signed edge-vertex matrix
- [[spielman-2025-sagt/ch14-approximating]] (p. 131): the author's $U$ (signed edge–vertex adjacency matrix), $m\times n$ [as `incidence matrix`]
- [[spielman-2025-sagt/ch30-simple]] (p. 246): signed edge–vertex U with L=UᵀU
- [[strang-2023-introduction/ch03-four-p3]] (p. 134): rows with −1 and 1 for the nodes at each edge's ends [as `incidence matrix`]
- [[strang-2023-introduction/ch09-linear]] (p. 366): A for the flow network; Aᵀy = 0 is Kirchhoff's current law

## Instances that use it

- [[figure-7-2-graph]] — 4 nodes, 5 edges; its incidence matrix, circulation and source-flow examples — from [[boyd-2018-vmls/ch07-matrix]]
- [[supply-chain-dynamics]] — warehouse level deviations driven by flows (via incidence matrix), purchases and sales — from [[boyd-2018-vmls/ch09-linear]]
- [[incidence-matrix-5-edges-4-nodes]] — Figure 3.4 graph; dimensions 1, 3, 3, 2; loops and trees — from [[strang-2023-introduction/ch03-four-p3]]
- [[incidence-matrix]] — graph example with $m=5,n=4,r=3$; $A^+$ computed exactly via $CR$; $A^{\mathsf T}y=0$ is Kirchhoff's law — from [[strang-2023-introduction/ch04-orthogonality-p2]]

## Candidate bridges

- [structural-analogy] Incidence matrix of a chain graph ↔ difference matrix $D$ ↔ first-order differences as convolution with $(1,-1)$. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → unspecified)
- [same-math] diffusion system with incidence matrix $A$ ↔ network analysis: flow conservation on a graph uses the incidence matrix — the same $A$ as in §7.3. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → complex-systems)
- [structural-analogy] Supply chain incidence matrix ↔ graph models: $A^{\rm sc}f$ converts edge flows into node changes. — from [[boyd-2018-vmls/ch09-linear]] (linear-algebra → other:graph-models)
- [structural-analogy] diffusion on a grid (heat) ↔ graph Laplacian (canon): incidence matrix $A$ and a resistance matrix $R$ appear in the system — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [same-math] Dirichlet energy $\|A^Tx\|^2$ (incidence matrix) ↔ linear-algebra canon: graph Laplacian quadratic form $\sum(x_i-x_j)^2$ — both are $x^T(AA^T)x$ for the incidence matrix $A$. — from [[boyd-2018-vmls/ch15-multi]] (linear-algebra → linear-algebra)
- [same-math] AᵀA with A a ±1 difference matrix (Example 3, p. 70; B₃ = AᵀA) ↔ graph theory: Laplacian L = BᵀB of an incidence matrix — same product of a ±1 edge-difference matrix with its transpose. — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → other:graph-theory)
- [structural-analogy] Left nullspace of an incidence matrix ↔ network science: loop currents / cycle space — independent loops count m − n + 1. — from [[strang-2023-introduction/ch03-four-p3]] (linear-algebra → complex-systems)
- [same-math] Incidence matrix constraint Aᵀy = 0 in max flow ↔ graph theory: incidence matrix and conservation of flow at nodes. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → other:graph-theory)
