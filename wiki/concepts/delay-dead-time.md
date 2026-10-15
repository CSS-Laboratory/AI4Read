---
id: delay-dead-time
type: concept
fields: [control-theory]
n_sources: 18
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch14-fundamental, astrom-2021-feedbacksystems/ch15-architecture-p1, bellman-1957-dp/ch05-v, bellman-1957-dp/ch07-vii, meadows-2008-thinking/app-untitled, meadows-2008-thinking/ch00-introduction, meadows-2008-thinking/ch03-systems, meadows-2008-thinking/ch04-systems, meadows-2008-thinking/ch06-leverage, meadows-2008-thinking/ch07-living, sutton-2018-rl/ch12-eligibility, todorov-2002-ofc/main]
raw_ids: [delay (dead time)]
canon_spine: control-theory
generated_by: build_kg.py
---

# delay-dead-time

## Canon spine entry

- **delay (dead time)** (control-theory): lag between action and effect, the main cause of overshoot and oscillation (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch12-error]] (p. 221): R cannot complete its action before T's outcome starts [as `delay (dead time)`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-10): varying time lags complicate stability in networks [as `delay (dead time)`]
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-15, p. 4-16): round-trip and forward/backward delays in the congestion model (4.17)–(4.19)
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-35): $e^{-s\tau}$: gain 1, phase $-180\omega\tau/\pi$ degrees; like a RHP zero in phase effect [as `delay (dead time)`]
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-4, 10-20): a pure delay $e^{-s\tau}$ leaves gain unchanged and adds phase lag $\omega\tau$
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-13): in the FOTD model, $\tau$; relative delay $\tau_n$ classifies lag, balanced or delay dominated [as `delay (dead time)`]
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-5, 14-14): adds phase lag, with effects similar to a RHP zero; approximated by Padé [as `delay (dead time)`]
- [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (p. 15-19, p. 15-22): handled by the Smith predictor; cascade control is particularly useful when significant delay lies between $u$ and the primary output but much less between $u$ and the secondary output [as `delay (dead time)`]
- [[bellman-1957-dp/ch05-v]] (pp. 156–157): the supply lag in sections D, E and §14: orders arrive later; a one-period lag keeps the single state $x$ (total available), while a two-period lag needs two state variables
- [[bellman-1957-dp/ch07-vii]] (p. 208): assumed absent: no lag between allocation and capacity [as `delay (dead time)`]
- [[meadows-2008-thinking/app-untitled]] (p. 189): in a balancing loop it makes oscillation likely [as `delay (dead time)`]
- [[meadows-2008-thinking/ch00-introduction]] (p. 3): feedback delays may make a problem unnecessarily hard to solve by the time it is apparent [as `delay (dead time)`]
- [[meadows-2008-thinking/ch03-systems]] (pp. 78, 83): feedback passing through many layers loses resilience; well-designed links minimize delays [as `delay (dead time)`]
- [[meadows-2008-thinking/ch04-systems]] (pp. 103–105): lag in a feedback loop; cause of overshoot, oscillation, collapse; every stock is a delay [as `delay (dead time)`]
- [[meadows-2008-thinking/ch06-leverage]] (p. 152): lag in a feedback loop, critical relative to the rate of change of the controlled stock [as `delay (dead time)`]
- [[meadows-2008-thinking/ch07-living]] (p. 179): slow central thermostat corrections led to overcorrection and oscillation [as `delay (dead time)`]
- [[sutton-2018-rl/ch12-eligibility]] (p. 317): delayed rewards are one case where traces help
- [[todorov-2002-ofc/main]] (p. 5): sensory delay is roughly equivalent to extra sensory noise because the forward model extrapolates delayed data

## Candidate bridges

- [metaphor] Rush-hour effect in queues ↔ delay (dead time): slow recovery after a short overload resembles slow response, though the mechanism here is saturated service rate. — from [[astrom-2021-feedbacksystems/ch03-system-p2]] (control-theory → other)
- [structural-analogy] backward-view credit assignment (TD error shouted back to prior states) ↔ control-theory: delay (dead time) — spreading a late signal back over earlier causes compensates for lag between action and effect. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
