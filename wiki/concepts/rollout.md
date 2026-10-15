---
id: rollout
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 15
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p3, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, bertsekas-2026-rlcourse/ch02-approximation-p6, bertsekas-2026-rlcourse/ch02-approximation-p7, bertsekas-2026-rlcourse/ch03-learning-p2, sutton-2018-rl/ch08-planning]
aliases: [rollout-algorithm]
generated_by: build_kg.py
---

# rollout

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `rollout-algorithm` — 4 digest(s)

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 24): getting $\tilde J_k$ on-line by running a base heuristic from each candidate next state [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 35–36, 49): one-step lookahead whose terminal cost is the cost of a base policy; truncated rollout adds a terminal approximation after $m$ steps [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 71): one-step lookahead with $\tilde J=J_\mu$ of a base policy; improves on it, so is stable if $\mu$ is [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (pp. 87, 102): one-step lookahead using a base policy's cost as $\tilde J$ [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 112, 122): one-step or multistep lookahead with cost-to-go approximated by a base policy; here used for replanning [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (pp. 143–144): apply a base policy's value as the cost approximation in one-step lookahead; equals one policy-iteration step [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 178): approximation in value space where $\tilde J_{k+1}$ is the cost of a base heuristic run from the next state [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 190): one-step lookahead whose tail cost is the cost of running a base heuristic or policy [alias `rollout-algorithm`; new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (pp. 216, 221): one-step or multistep lookahead whose leaves are evaluated by running a base policy or heuristic [alias `rollout-algorithm`; new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 243): one-step lookahead that scores controls by the cost of a base heuristic or policy; in this unit also constrained, continuous-time and stochastic [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (pp. 282, 292): one-step (or multistep) lookahead with a base policy's cost estimated by simulation or optimization; the resulting policy is no worse than the base for standard and multiagent rollout (p. 290), but not necessarily for truncated or certainty-equivalent variants (pp. 282, 292); see also pp. 275, 283 [alias `rollout-algorithm`; new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 305, 321): one-step lookahead whose tail cost is the simulated cost of a base policy; here applied to belief-state and minimax problems [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (pp. 322, 335): policy improvement from a base policy/heuristic evaluated by simulation or, here, by DP/maximization [new]
- [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 392): improve a base policy by lookahead plus simulation of that policy, possibly truncated with a terminal cost [new]
- [[sutton-2018-rl/ch08-planning]] (p. 183): Monte Carlo action-value estimates for the current state under a rollout policy [alias `rollout-algorithm`; new]

## Instances that use it

- [[td-gammon]] — approximate policy iteration trained with TD($\lambda$); on-line lookahead with truncated rollout — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[traveling-salesman-dp]] — exponential state growth makes exact DP intractable; rollout with nearest neighbor is polynomial — from [[bertsekas-2026-rlcourse/ch01-exact-p1]]
- [[td-gammon]] — truncated rollout with a base policy from a neural-network terminal cost — from [[bertsekas-2026-rlcourse/ch01-exact-p3]]
- [[spiders-and-flies]] — multiagent rollout with $5^m$ joint moves — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[lq-rollout-replanning]] — $b=2$, $r=0.5$ nominal; $K^*\le\tilde K_L\le K_L$ — from [[bertsekas-2026-rlcourse/ch01-exact-p5]]
- [[tsp-rollout]] — 5-city TSP: heuristic 48, one-step rollout 37, optimal 20 — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[option-exercise-rollout]] — stock-selling DP; base heuristic 2.268, rollout 2.269; Monte Carlo accuracy matters — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[backgammon-rollout]] — origin of the name; truncated rollout with a neural-net estimate — from [[bertsekas-2026-rlcourse/ch01-exact-p6]]
- [[multi-vehicle-routing-rollout]] — rollout improves a nearest-task heuristic from 10 to 6 moves — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[breakthrough-problem]] — greedy versus rollout versus exact DP on a binary tree — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[sequential-improvement-violation-example]] — rollout strictly worse than a heuristic that is optimal from $x_0$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]]
- [[rna-folding]] — rollout with partial-folding software and an expert comparing foldings — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]]
- [[traveling-salesman-k-opt]] — local search/rollout on tours, $k$-interchange neighborhoods — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]]
- [[constrained-tsp]] — TSP with a safety constraint; rollout with a non-consistent heuristic — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[td-gammon]] — uses scheme (b), one-step minimization plus truncated rollout, out of necessity — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]]
- [[facility-location]] — 0-1 decisions fixed by rollout with transportation problems — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[constrained-spanning-tree-rollout]] — one-arc-at-a-time rollout; iteration as policy iteration — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[min-length-curve-calculus-of-variations]] — poor base policy, optimal rollout in continuous time — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[optimal-stopping-always-stop-base]] — rollout optimal under absorbing stopping set — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[backgammon-rollout-tesauro-galperin]] — Monte Carlo rollout on top of TD-Gammon — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[traveling-salesman-constrained-rollout]] — sequential improvement and its violation when D→A costs 25 — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]]
- [[spiders-and-flies]] — poor base policy, excellent (here optimal) rollout via implicit coordination — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[multi-vehicle-routing]] — base cost 7 vs rollout cost 5; polynomial rather than exponential in $m$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[supply-chain-delay]] — rollout with continuous controls, delays and on-line replanning — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[agent-coordination-failure]] — Example 2.9.3: rollout cost 2 vs base cost 1 — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[alphago-alphazero]] — MCTS, with or without rollout, in games; MCTS tested as ineffective in backgammon — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[wordle]] — deterministic adaptive control / search problem; rollout near optimal — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]]
- [[tsp-rollout-exercise]] — traveling salesman with farthest/nearest neighbor heuristics — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[breakthrough-problem]] — greedy/random/truncated rollout — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]]
- [[pipeline-repair-pomdp]] — case study of approximate rollout and PI [BBW20] — from [[bertsekas-2026-rlcourse/ch03-learning-p2]]
- [[twitter-280-characters]] — partial-equilibrium novelty effect from a small randomized rollout — from [[grimmer-2022-textasdata/ch22-principles]]
- [[alphago]] — MCTS guided by SL policy, RL-trained value network and rollouts — from [[sutton-2018-rl/ch16-applications]]

## Candidate bridges

- [structural-analogy] MPC "apply the first control, then replan" ↔ rollout/approximation in value space: both are one Newton step on the Bellman equation (pp. 119–122). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other:rollout-approximation-in-value)
- [structural-analogy] MPC (rolling horizon plus terminal cost) ↔ rollout and approximation in value space — author links them (pp. 147–148). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → unspecified)
- [structural-analogy] Rollout with a consistent base heuristic ↔ control-theory: one policy-improvement (Newton) step on the base policy — the author states this link to Chapter 1's Newton interpretation (p. 184, p. 188). — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → control-theory)
- [metaphor] Fortified rollout's "keep the best trajectory so far" ↔ incumbent solution in search heuristics. — from [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (control-theory → unspecified)
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ keeping an incumbent best solution in iterative search; the next step is accepted only on strict improvement. — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (control-theory → unspecified)
- [structural-analogy] World-model rollout with replanning ↔ model predictive control (control-theory): act on the first step, then re-observe the state. — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (control-theory → control-theory)
- [structural-analogy] Rollout applies the first control and discards the rest of the ℓ-step plan ↔ control-theory: model predictive control (receding horizon) — both re-solve a finite lookahead each step. — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (control-theory → control-theory)
- [structural-analogy] Rollout or lookahead with $\tilde J$ as one Newton step ↔ Newton's method for fixed-point equations — the page states the Newton-step view for Bellman's equation. — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (control-theory → unspecified)
- [structural-analogy] Rollout improvement via the continuous-time inequality (2.63) ↔ control theory: Lyapunov-style decreasing functions — the heuristic's cost-to-go must not rise along the controlled path. — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → control-theory)
- [structural-analogy] Fortified rollout's tentative best trajectory ↔ anytime/incumbent solutions in branch-and-bound — the author notes rollout traverses the branch-and-bound tree. — from [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (control-theory → unspecified)
- [structural-analogy] Agent-by-agent rollout ↔ optimization: coordinate descent on a function of $m$ components — the author's own footnote (p. 290). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → other:optimization)
- [structural-analogy] Certainty-equivalent rollout ↔ control theory: optimizing with future disturbances fixed at nominal values, as in model predictive control (p. 276). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → control-theory)
- [structural-analogy] Minimax rollout/worst-case lookahead ↔ robust (worst-case) control: the text contrasts engineering worst-case design with zero-sum theory (p. 340). — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (control-theory → control-theory)
- [structural-analogy] rollout or one-step lookahead as a Newton step ↔ optimization: Newton iteration on the Bellman equation (pp. 378, 386) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other:optimization)
- [metaphor] Latent overshooting ↔ model-based RL planning horizons: training for multi-step rollouts. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → other:model-based-rl-planning)
