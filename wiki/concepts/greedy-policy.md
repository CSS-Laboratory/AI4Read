---
id: greedy-policy
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p2, sutton-2018-rl/ch03-finite]
generated_by: build_kg.py
---

# greedy-policy

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 214): picks the next state with maximal transition probability [new]
- [[sutton-2018-rl/ch03-finite]] (p. 64): chooses by one-step consequences; greedy with respect to $v_*$ is optimal [new]

## Instances that use it

- [[gridworld-4x4]] — random policy's $v_\pi$ equals negative expected steps to termination; greedy policy is optimal after one improvement — from [[sutton-2018-rl/ch04-dynamic]]
