---
id: fortified-rollout
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p4]
generated_by: build_kg.py
---

# fortified-rollout

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 189): rollout that keeps the best trajectory found so far to enforce improvement [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 190): rollout that follows a stored best-so-far trajectory unless a cheaper one is found [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 243): rollout that keeps a tentative best feasible complete trajectory [new]

## Candidate bridges

- [metaphor] Fortified rollout's "keep the best trajectory so far" ↔ incumbent solution in search heuristics. — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → unspecified)
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ keeping an incumbent best solution in iterative search; the next step is accepted only on strict improvement. — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (control-theory → unspecified)
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ anytime/incumbent solutions in branch-and-bound — the author notes rollout traverses the branch-and-bound tree. — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → unspecified)
