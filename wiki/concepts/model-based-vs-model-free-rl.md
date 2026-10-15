---
id: model-based-vs-model-free-rl
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 17
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p6, bertsekas-2026-rlcourse/ch03-learning-p2, bertsekas-2026-rlcourse/ch03-learning-p4, recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch05-monte, sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch08-planning, sutton-2018-rl/ch14-psychology, sutton-2018-rl/ch15-neuroscience-p2, sutton-2018-rl/ch16-applications, sutton-2018-rl/ch17-frontiers]
raw_ids: [model-based vs model-free RL]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# model-based-vs-model-free-rl

## Canon spine entry

- **model-based vs model-free RL** (control-theory): learn a model and plan with it, versus learn values or policies directly (UG)

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 40): author's "model-free" means a simulator or real system replaces the equations; a model always exists
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 129, 133): "planning" vs "learning" in the AI/RL glossary; data-driven MPC replaces the model by data [as `model-based vs model-free RL`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 197, p. 203): rollout needing no explicit cost model, and the world-model alternative
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 309, footnote): system identification with policy reoptimization is contrasted here with the POMDP approach [as `model-based vs model-free RL`]
- [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 382): here "model-free" means a simulator replaces a mathematical model [as `model-based vs model-free RL`]
- [[bertsekas-2026-rlcourse/ch03-learning-p4]] (p. 414): the author calls (3.48) "model-free" because only simulated $F(z)$ is needed, not the form of $F$ [as `model-based vs model-free RL`]
- [[recht-2019-tour/main]] (pp. 4–7): fit dynamics then plan, versus map observations to actions without a dynamics model; the author says model-free still assumes structure
- [[sutton-2018-rl/ch01-introduction]] (p. 7): planning with a model of the environment versus explicit trial-and-error learning
- [[sutton-2018-rl/ch03-finite]] (p. 69): the unit contrasts complete knowledge (full $p$) with incomplete knowledge
- [[sutton-2018-rl/ch04-dynamic]] (pp. 73, 89): DP needs a perfect model; later methods drop that requirement
- [[sutton-2018-rl/ch05-monte]] (p. 91, 115): MC learns from sample experience or a sample model, with no explicit transition probabilities [as `model-based vs model-free RL`]
- [[sutton-2018-rl/ch06-temporal]] (p. 124): TD(0) needs no model of reward or transition probabilities
- [[sutton-2018-rl/ch08-planning]] (p. 159): model-based methods plan with a model; model-free learn directly; this chapter treats them as intermixable [as `model-based vs model-free RL`]
- [[sutton-2018-rl/ch14-psychology]] (pp. 364–366): corresponds to goal-directed vs habitual control [as `model-based vs model-free RL`]
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 407): mapped onto habitual vs goal-directed behaviour and onto DLS/DMS
- [[sutton-2018-rl/ch16-applications]] (pp. 437–438): DQN chose model-free Q-learning over learned models or emulator look-ahead for simplicity and speed
- [[sutton-2018-rl/ch17-frontiers]] (p. 461–463): used throughout, extended to options and GVFs [as `model-based vs model-free RL`]
