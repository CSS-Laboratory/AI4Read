---
id: path-graph
type: instance
fields: [linear-algebra]
n_sources: 4
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch05-fundamental, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch24-nodal]
raw_ids: [path graph]
generated_by: build_kg.py
---

# path-graph

## Descriptions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch01-introduction]] (pp. 6–9): $L$ eigenvectors resemble string vibration modes
- [[spielman-2025-sagt/ch05-fundamental]] (p. 49, 51): λ₂ ≤ 12/(n(n+1)); (5.1) is loose [as `path graph`]
- [[spielman-2025-sagt/ch10-random]] (p. 99): mixing ~n² steps
- [[spielman-2025-sagt/ch24-nodal]] (pp. 197–200): plots with and without random weights; $\psi_k$ has $k-1$ sign changes when it has no zero entry (proved for $\lambda_k$ simple)

## Candidate bridges

- [same-math] Matrix in the heat-equation example (Figure 6.8) ↔ graph Laplacian: A = [−1 1 0; 1 −2 1; 0 1 −1] is minus the Laplacian of a 3-node path graph, so du/dt = Au smooths a signal on a network. — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → other)
