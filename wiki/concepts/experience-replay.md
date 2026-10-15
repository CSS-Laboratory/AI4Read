---
id: experience-replay
type: concept
fields: [control-theory, llm]
fields_strong: [control-theory, llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch19-reinforcement, sutton-2018-rl/ch16-applications]
generated_by: build_kg.py
---

# experience-replay

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch16-applications]] (p. 440): store transitions and update from random samples; allowed by off-policy learning [new]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (pp. 387–388): sampling stored past tuples at random to form batches [new]

## Instances that use it

- [[dqn-experience-replay]] — buffer of past samples reused for training — from [[bertsekas-2026-rlcourse/ch03-learning-p2]]
