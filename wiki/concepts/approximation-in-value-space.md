---
id: approximation-in-value-space
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 8
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p7]
generated_by: build_kg.py
---

# approximation-in-value-space

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 22–23): using $\tilde J_k$ for $J_k^*$ in a forward lookahead minimization [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 34, 49): replace $J^*$ by $\tilde J$ in a lookahead minimization, giving a suboptimal policy [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 62): choose actions by minimizing stage cost plus an approximate terminal cost $\tilde J$ [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 87): replacing $J^*_{k+1}$ by some $\tilde J_{k+1}$ in the minimization [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 140): choose actions by lookahead with an approximate cost function; the workhorse of RL [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 173): run the forward construction (2.6) with an approximate cost-to-go $\tilde J_{k+1}$ in place of $J^*_{k+1}$ [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 250): choose controls by minimizing stage cost plus approximate cost-to-go [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (p. 327): apply the control from lookahead with an approximate cost-to-go $\tilde J$, as in (2.116) [new]

## Candidate bridges

- [structural-analogy] Approximation in value space with a control interval and prediction interval ↔ model predictive control: the book relates the two (pp. 8–9) — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] MPC "apply the first control, then replan" ↔ rollout/approximation in value space: both are one Newton step on the Bellman equation (pp. 119–122). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other:rollout-approximation-in-value)
- [structural-analogy] MPC (rolling horizon plus terminal cost) ↔ rollout and approximation in value space — author links them (pp. 147–148). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → unspecified)
