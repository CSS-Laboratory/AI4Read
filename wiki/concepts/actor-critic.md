---
id: actor-critic
type: concept
fields: [control-theory, llm]
fields_strong: [control-theory, llm]
n_sources: 4
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch19-reinforcement, sutton-2018-rl/ch13-policy, sutton-2018-rl/ch15-neuroscience-p1, sutton-2018-rl/ch15-neuroscience-p2]
generated_by: build_kg.py
---

# actor-critic

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch13-policy]] (p. 331): policy (actor) plus a value function that assesses actions via a one-step return (critic); adds bias, often cuts variance [new]
- [[sutton-2018-rl/ch15-neuroscience-p1]] (p. 395): actor learns the policy, critic learns values by TD and sends $\delta$ to the actor [new]
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 398): actor adjusts the policy; critic learns values; both driven by the same δ [new]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (p. 394): policy network (actor) plus value network (critic), updated by TD [new]

## Instances that use it

- [[takahashi-neural-actor-critic]] — actor in dorsal, critic in ventral striatum, dopamine as $\delta$ — from [[sutton-2018-rl/ch15-neuroscience-p1]]

## Candidate bridges

- [structural-analogy] actor + critic ↔ control theory: controller plus an estimator that evaluates performance — both separate acting from assessing. — from [[sutton-2018-rl/ch13-policy]] (control-theory → control-theory)
- [structural-analogy] Actor–critic split ↔ control-theory: a controller plus a separate estimator of performance. Both act in one loop but have different learning roles. — from [[sutton-2018-rl/ch15-neuroscience-p1]] (control-theory → control-theory)
