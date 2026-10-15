---
id: inverse-reinforcement-learning
type: concept
fields: [control-theory, theory-of-mind]
n_sources: 3
tiers: [deep, core]
grounding: digests
sources: [ng-2000-irl/main, rabinowitz-2018-machine-tom/main, recht-2019-tour/main]
raw_ids: [inverse reinforcement learning]
canon_spine: theory-of-mind
generated_by: build_kg.py
---

# inverse-reinforcement-learning

## Canon spine entry

- **inverse reinforcement learning** (theory-of-mind): recovering a reward function from observed behaviour; the ML twin of inverse planning (grad)

## Definitions in the sources

### control-theory

- [[ng-2000-irl/main]] (p. 0): find the reward function that an observed (optimal) behaviour is optimizing
- [[recht-2019-tour/main]] (p. 23): estimate a human's reward function from behaviour

### theory-of-mind

- [[rabinowitz-2018-machine-tom/main]] (pdf 4): recovering rewards from behaviour; BIRL used as a baseline [as `inverse reinforcement learning`]

## Candidate bridges

- [structural-analogy] Inverse problem ↔ inverse planning / inverse reinforcement learning (not in this unit): inferring goals from actions is under-determined in both — similar problem, not shown here to be the same mathematics — from [[apperly-2011-mindreaders/ch01-introduction]] (theory-of-mind → control-theory)
- [structural-analogy] shrinking class of "indistinguishably satisfactory models" as connections are enriched (p. 30) ↔ statistics/machine learning: identifiability in inverse reinforcement learning, where more varied behaviour narrows the set of consistent reward functions. — from [[dennett-1987-intentional-stance/ch02-true]] (theory-of-mind → other)
- [structural-analogy] The disjunction problem (a state may "mean" any broader disjunction) ↔ inverse planning / inverse reinforcement learning: many goal or reward descriptions fit the same behaviour, so extra constraints are needed to choose one. — from [[dennett-1987-intentional-stance/ch08-evolution]] (theory-of-mind → control-theory)
