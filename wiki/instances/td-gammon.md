---
id: td-gammon
type: instance
fields: [control-theory]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch02-approximation-p3, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch08-planning, sutton-2018-rl/ch16-applications]
generated_by: build_kg.py
---

# td-gammon

## Descriptions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 7, 9): approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 74): truncated rollout with a base policy from a neural-network terminal cost
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (p. 226): uses scheme (b), one-step minimization plus truncated rollout, out of necessity
- [[sutton-2018-rl/ch01-introduction]] (p. 11): TD plus a neural network for a game of about $10^{20}$ states
- [[sutton-2018-rl/ch08-planning]] (p. 182): deeper search gives better but slower moves
- [[sutton-2018-rl/ch16-applications]] (p. 421): nonlinear TD(λ) + ANN + self-play reaches near-grandmaster play; shows the role of representation and search
