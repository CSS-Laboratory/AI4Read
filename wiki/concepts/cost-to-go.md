---
id: cost-to-go
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch02-approximation-p1]
generated_by: build_kg.py
---

# cost-to-go

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 14, 19): cost of the remaining stages from $x_k$; its optimum is $J_k^*(x_k)$ [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 168): $J^*_k(x_k)$, the optimal cost of the $(N-k)$-stage tail subproblem starting at $x_k$ [new]

## Candidate bridges

- [structural-analogy] Rollout improvement via the continuous-time inequality (2.63) ↔ control theory: Lyapunov-style decreasing functions — the heuristic's cost-to-go must not rise along the controlled path. — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → control-theory)
