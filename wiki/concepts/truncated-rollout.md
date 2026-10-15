---
id: truncated-rollout
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p3]
generated_by: build_kg.py
---

# truncated-rollout

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 144): simulate the base policy a few steps, then use a terminal cost estimate; "optimistic" single policy iteration [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 196): heuristic stopped after few steps plus terminal cost approximation [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (pp. 216, 222): the base heuristic is run only m steps; a terminal cost approximation $\tilde J$ may be added [new]

## Instances that use it

- [[td-gammon]] — approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[td-gammon]] — truncated rollout with a base policy from a neural-network terminal cost — from [[bertsekas-2026-rlcourse/ch01-exact-p3]]
- [[backgammon-rollout]] — origin of the name; truncated rollout with a neural-net estimate — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[td-gammon]] — uses scheme (b), one-step minimization plus truncated rollout, out of necessity — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[breakthrough-problem]] — greedy/random/truncated rollout — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
