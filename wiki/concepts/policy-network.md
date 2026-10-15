---
id: policy-network
type: concept
fields: [control-theory, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p3, prince-2023-udl/ch01-introduction]
generated_by: build_kg.py
---

# policy-network

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p3]] (p. 404): neural approximators of cost functions / policies [new]

### llm

- [[prince-2023-udl/ch01-introduction]] (p. 12): deep network mapping the observed state to an action [new]

## Instances that use it

- [[chess-policy-network]] — board state → move; extreme credit assignment — from [[prince-2023-udl/ch01-introduction]]

## Candidate bridges

- [structural-analogy] Policy network (p. 12–13) ↔ llm: RLHF policy optimized for reward — both map a state/context to actions under a reward signal (canon link; not stated in this unit). — from [[prince-2023-udl/ch01-introduction]] (llm → llm)
