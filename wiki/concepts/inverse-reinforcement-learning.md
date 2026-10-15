---
id: inverse-reinforcement-learning
type: concept
fields: [control-theory, theory-of-mind]
fields_strong: [control-theory, theory-of-mind]
n_sources: 5
n_works: 5
tiers: [core, deep, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p2, ng-2000-irl/main, rabinowitz-2018-machine-tom/main, recht-2019-tour/main, sutton-2018-rl/ch17-frontiers]
aliases: [inverse-reinforcement-learning-inverse-optimal-control]
raw_ids: [inverse reinforcement learning]
canon_spine: [control-theory, theory-of-mind]
generated_by: build_kg.py
---

# inverse-reinforcement-learning

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `inverse-reinforcement-learning-inverse-optimal-control` — 2 digest(s)

## Canon spine entry

- **inverse reinforcement learning** (theory-of-mind): recovering a reward function from observed behaviour; the ML twin of inverse planning (grad)

## Canon spine entry

- **inverse reinforcement learning (inverse optimal control)** (control-theory): infer the reward that makes observed behavior optimal (grad)

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 202): learning an expert's cost from its choices; mentioned [alias `inverse-reinforcement-learning-inverse-optimal-control`]
- [[ng-2000-irl/main]] (p. 0): find the reward function that an observed (optimal) behaviour is optimizing
- [[recht-2019-tour/main]] (p. 23): estimate a human's reward function from behaviour
- [[sutton-2018-rl/ch17-frontiers]] (p. 470): recover a reward that makes an expert's behavior optimal. This is not exactly possible, since many rewards fit one policy [as `inverse reinforcement learning (inverse optimal control)`; alias `inverse-reinforcement-learning-inverse-optimal-control`]

### theory-of-mind

- [[rabinowitz-2018-machine-tom/main]] (pdf 4): recovering rewards from behaviour; BIRL used as a baseline [as `inverse reinforcement learning`]

## Candidate bridges

- [structural-analogy] Inverse problem ↔ inverse planning / inverse reinforcement learning (not in this unit): inferring goals from actions is under-determined in both — similar problem, not shown here to be the same mathematics — from [[apperly-2011-mindreaders/ch01-introduction]] (theory-of-mind → control-theory)
- [structural-analogy] shrinking class of "indistinguishably satisfactory models" as connections are enriched (p. 30) ↔ statistics/machine learning: identifiability in inverse reinforcement learning, where more varied behaviour narrows the set of consistent reward functions. — from [[dennett-1987-intentional-stance/ch02-true]] (theory-of-mind → llm)
- [structural-analogy] The disjunction problem (a state may "mean" any broader disjunction) ↔ inverse planning / inverse reinforcement learning: many goal or reward descriptions fit the same behaviour, so extra constraints are needed to choose one. — from [[dennett-1987-intentional-stance/ch08-evolution]] (theory-of-mind → control-theory)
