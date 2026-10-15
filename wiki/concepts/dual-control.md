---
id: dual-control
type: concept
fields: [control-theory]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch15-architecture-p2, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p6]
generated_by: build_kg.py
---

# dual-control

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-32): control that both investigates and directs; hyper state is a conditional distribution [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 147): Feldbaum's DP framework for adaptive control; estimation versus control [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 310): combined identification and control problem; optimal solution "notoriously difficult" [new]

## Candidate bridges

- [structural-analogy] Dual control ↔ exploration vs exploitation: both trade immediate performance against information gain; the author links dual control to reinforcement learning. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other)
- [structural-analogy] Dual control (estimation vs control) ↔ RL: exploration–exploitation tradeoff — the author identifies them (p. 147). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → other)
- [structural-analogy] Exploration vs exploitation ↔ control theory: identification (estimation) vs control, "dual control" — the text names this correspondence (p. 44). — from [[sutton-2018-rl/ch02-multi]] (control-theory → control-theory)
