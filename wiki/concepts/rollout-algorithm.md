---
id: rollout-algorithm
type: concept
fields: [control-theory]
n_sources: 4
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p2, bertsekas-2026-rlcourse/ch02-approximation-p3, bertsekas-2026-rlcourse/ch02-approximation-p5, sutton-2018-rl/ch08-planning]
generated_by: build_kg.py
---

# rollout-algorithm

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p2]] (p. 190): one-step lookahead whose tail cost is the cost of running a base heuristic or policy [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (pp. 216, 221): one-step or multistep lookahead whose leaves are evaluated by running a base policy or heuristic [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (pp. 282, 292): one-step (or multistep) lookahead with a base policy's cost estimated by simulation or optimization; the resulting policy is no worse than the base for standard and multiagent rollout (p. 290), but not necessarily for truncated or certainty-equivalent variants (pp. 282, 292); see also pp. 275, 283 [new]
- [[sutton-2018-rl/ch08-planning]] (p. 183): Monte Carlo action-value estimates for the current state under a rollout policy [new]
