---
id: liapunov-function
type: concept
fields: [complex-systems]
n_sources: 3
tiers: [core]
grounding: digests
sources: [strogatz-2024-nonlinear/ch07-limit-p1, strogatz-2024-nonlinear/ch09-lorenz-p1, strogatz-2024-nonlinear/ch09-lorenz-p2]
generated_by: build_kg.py
---

# liapunov-function

## Definitions in the sources

### complex-systems

- [[strogatz-2024-nonlinear/ch07-limit-p1]] (p. 203): positive definite $V$ with $\dot V<0$ away from $\mathbf x^*$ [new]
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (p. 323): positive definite function decreasing along trajectories; proves global stability of origin for r < 1 [new]
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 347): a positive-definite function that decreases along trajectories, proving global stability [new]

## Candidate bridges

- [structural-analogy] Liapunov function / gradient potential ↔ optimisation: a loss function that decreases along update steps rules out cycling — both use a strictly decreasing quantity to forbid loops. — from [[strogatz-2024-nonlinear/ch07-limit-p1]] (complex-systems → other)
