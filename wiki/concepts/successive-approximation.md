---
id: successive-approximation
type: concept
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [bellman-1957-dp/ch10-x, bellman-1957-dp/ch11-xi]
generated_by: build_kg.py
---

# successive-approximation

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch10-x]] (pp. 297, 300): $f_{n+1}=\max\min T(f_n)$; converges to the unique solution [new]
- [[bellman-1957-dp/ch11-xi]] (pp. 321–323): iterates (5.3) converging by factorial bounds [new]

## Candidate bridges

- [same-math] $f_{n+1}(x)=\min_z T(z,x,f_n)$ iterated from $f_0$ ↔ control-theory: value iteration for a discounted MDP with a continuous state — the same successive-approximation scheme. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
