---
id: sequential-improvement
type: concept
fields: [control-theory]
n_sources: 5
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p3, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p7]
generated_by: build_kg.py
---

# sequential-improvement

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 186): $\min_u\tilde Q_k(x_k,u)\le H_k(x_k)$ for all $x_k,k$; weaker than consistency, and still gives cost improvement [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 193): condition $\min_{u_k}\tilde Q_k\le H_k$; gives cost improvement of rollout [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (pp. 241–242): Eq. (2.48); with $R(\tilde y_0)\in C$ it gives feasibility and cost improvement [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (pp. 243, 255): condition ensuring rollout is feasible and no worse than the base heuristic; continuous-time form (2.63) [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (p. 322): condition that one-step lookahead on the heuristic's cost is no worse than the heuristic's cost; it implies cost improvement [new]

## Instances that use it

- [[sequential-improvement-violation-example]] — rollout strictly worse than a heuristic that is optimal from $x_0$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[traveling-salesman-constrained-rollout]] — sequential improvement and its violation when D→A costs 25 — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]

## Candidate bridges

- [structural-analogy] Sequential improvement ↔ MPC: the condition behind MPC's stability properties (p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → other)
