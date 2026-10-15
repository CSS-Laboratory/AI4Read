---
id: policy-iteration
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 5
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p6, sutton-2018-rl/ch04-dynamic]
generated_by: build_kg.py
---

# policy-iteration

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 6): alternating policy evaluation and policy improvement; the AlphaZero training structure [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 48): alternate policy evaluation and policy improvement; viewed as repeated rollout [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 72): repeated nontruncated rollout; converges quadratically from a stable linear policy [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 144): repeated rollout; evaluation plus improvement, needs off-line training [new]
- [[sutton-2018-rl/ch04-dynamic]] (p. 80): alternating evaluation and improvement until the policy is stable [new]

## Instances that use it

- [[alphazero]] — off-line policy-iteration training plus on-line lookahead with a trained evaluator — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[td-gammon]] — approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[constrained-spanning-tree-rollout]] — one-arc-at-a-time rollout; iteration as policy iteration — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[jacks-car-rental]] — policy iteration on a continuing MDP with Poisson demand; five successive policies — from [[sutton-2018-rl/ch04-dynamic]]
- [[alphago-zero]] — pure self-play policy iteration with MCTS as policy improvement — from [[sutton-2018-rl/ch16-applications]]

## Candidate bridges

- [structural-analogy] Procedure A (evaluate a policy, then maximize over $q$) ↔ policy iteration in RL — same alternating pattern (p. 89) — from [[bellman-1957-dp/ch03-iii]] (control-theory → unspecified)
- [structural-analogy] §5 monotone convergence from an initial policy's value ↔ policy iteration (improve a policy's value by one greedy step); the source only does the iteration, not full policy evaluation each round. — from [[bellman-1957-dp/ch04-iv]] (control-theory → unspecified)
- [structural-analogy] §22–23 policy iteration with monotone $f_n$ ↔ reinforcement learning: policy improvement — evaluate a policy, then improve greedily — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] approximation in policy space (§9) ↔ control-theory canon "policy": improve the policy against the current value, with monotone convergence — resembles policy iteration, but the text does not say so. — from [[bellman-1957-dp/ch11-xi]] (control-theory → control-theory)
- [structural-analogy] Policy iteration/GPI ↔ control theory: controller design alternating "estimate performance of the current law" and "improve the law" — two processes with a joint fixed point. — from [[sutton-2018-rl/ch04-dynamic]] (control-theory → control-theory)
