---
id: multiagent-rollout
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 4
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, bertsekas-2026-rlcourse/ch02-approximation-p6, bertsekas-2026-rlcourse/ch02-approximation-p7]
generated_by: build_kg.py
---

# multiagent-rollout

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (pp. 103–104): one-agent-at-a-time lookahead giving $O(nm)$ instead of $O(n^m)$ Q-factors [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (pp. 283–285): agent-by-agent minimization of control components, cost $O(nm)$ per stage, keeps cost improvement [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 308): policy improvement one agent at a time, giving linear instead of exponential computation [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (p. 326): choose components of a joint control one agent at a time with the others on base policy [new]

## Instances that use it

- [[spiders-and-flies]] — multiagent rollout with $5^m$ joint moves — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
