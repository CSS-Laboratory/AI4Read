---
id: base-heuristic
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1]
generated_by: build_kg.py
---

# base-heuristic

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 24): a suboptimal control scheme whose cost approximates cost-to-go in rollout [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (pp. 152, 155, 157): a fixed heuristic whose value defines the rollout cost approximation [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 178): any method that, from a state, produces controls, states and a cost $H_k(x_k)$ to the end [new]

## Instances that use it

- [[option-exercise-rollout]] — stock-selling DP; base heuristic 2.268, rollout 2.269; Monte Carlo accuracy matters — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]

## Candidate bridges

- [structural-analogy] Rollout with a consistent base heuristic ↔ control-theory: one policy-improvement (Newton) step on the base policy — the author states this link to Chapter 1's Newton interpretation (p. 184, p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → control-theory)
