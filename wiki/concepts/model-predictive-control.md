---
id: model-predictive-control
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 13
n_works: 4
tiers: [reference, core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch15-architecture-p1, astrom-2021-feedbacksystems/ch15-architecture-p2, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, bertsekas-2026-rlcourse/ch02-approximation-p7, murphy-2023-pml2/ch35-reinforcement, recht-2019-tour/main]
raw_ids: [model predictive control]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# model-predictive-control

## Canon spine entry

- **model predictive control** (control-theory): repeatedly solve a finite-horizon optimal control problem and apply only the first step (grad)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (p. 15-10, p. 15-11): receding horizon control: solve a finite-horizon problem, apply a short part, resolve; terminal cost matters for stability [as `model predictive control`]
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-40): originated at Shell as dynamic matrix control
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 8–9): approximation in value space used in control design; control interval and prediction interval defined here
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 50, 53–55): mentioned as on-line multistep optimization with a prediction interval; stability and target tubes noted
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 118–122): at each state solve an $\ell$-stage deterministic problem, apply only the first control, repeat; read here as rollout and as a Newton step [as `model predictive control`]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 147): on-line optimization over a truncated rolling horizon with terminal cost approximation [as `model predictive control`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 188): mentioned: the sequential improvement condition underlies MPC stability, but the classical MPC heuristic is not sequentially consistent
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 204): replanning each step; rollout and world models share this character
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 250): mentioned as the setting where longer lookahead is typical
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (p. 276): cited as a major paradigm of $\ell$-stage lookahead optimization [as `model predictive control`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (pp. 334, 341): the chess scheme is described as an application of it; "rolling/receding horizon" is the lookahead truncation idea
- [[recht-2019-tour/main]] (p. 20): receding horizon control: plan short-term, execute one step, replan

### bayesian

- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1164): plan $H$ steps with a model, act once, replan [new; work fields: bayesian, control-theory]

## Candidate bridges

- [structural-analogy] Approximation in value space with a control interval and prediction interval ↔ model predictive control: the book relates the two (pp. 8–9) — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] $\ell$-step lookahead applying only the first control ↔ model predictive control: receding-horizon re-optimization at every step (the text links them, pp. 50, 53). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → control-theory)
- [structural-analogy] first step precise, later steps only enhance the starting point ↔ model predictive control: apply only the first step of a finite-horizon solution (canon link; not stated in this unit). — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → control-theory)
- [structural-analogy] World-model rollout with replanning ↔ model predictive control (control-theory): act on the first step, then re-observe the state. — from [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (control-theory → control-theory)
- [structural-analogy] Rollout applies the first control and discards the rest of the ℓ-step plan ↔ control-theory: model predictive control (receding horizon) — both re-solve a finite lookahead each step. — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (control-theory → control-theory)
- [structural-analogy] Certainty-equivalent rollout ↔ control theory: optimizing with future disturbances fixed at nominal values, as in model predictive control (p. 276). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → control-theory)
- [structural-analogy] OLFC ↔ model predictive control: re-solve an open-loop optimization each step and apply only the first control (p. 338). — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (control-theory → control-theory)
- [structural-analogy] n-step return with bootstrapped tail ↔ model predictive control: a finite lookahead horizon plus an estimate of the remaining cost — both truncate the future and replace the tail by a value estimate. — from [[sutton-2018-rl/ch07-n]] (control-theory → control-theory)
- [structural-analogy] Decision-time planning (replan after every state, execute one action) ↔ control theory: model predictive control — repeated finite-horizon planning with only the first action applied. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
- [structural-analogy] MCTS re-run from the new current state at every step, applying only the first action ↔ control-theory: receding-horizon / model predictive control — plan ahead, act once, re-plan (p. 443). — from [[sutton-2018-rl/ch16-applications]] (control-theory → control-theory)
- [metaphor] "postponing decisions until the last possible moment" ↔ model predictive control: acting from the current state estimate and re-deciding as information arrives (p. 2) — from [[todorov-2002-ofc/main]] (control-theory → control-theory)
