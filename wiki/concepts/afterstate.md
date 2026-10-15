---
id: afterstate
type: concept
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch16-applications]
generated_by: build_kg.py
---

# afterstate

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch06-temporal]] (p. 137): position after the agent's move, before the environment's response [new]
- [[sutton-2018-rl/ch16-applications]] (p. 424): the position right after the agent's move, before the opponent or chance acts; valued instead of states in TD-Gammon and Watson [new]

## Instances that use it

- [[tic-tac-toe-afterstates]] — different position–move pairs, same afterposition — from [[sutton-2018-rl/ch06-temporal]]
- [[watson-daily-double]] — action values from learned afterstate values and confidence, with risk control — from [[sutton-2018-rl/ch16-applications]]
