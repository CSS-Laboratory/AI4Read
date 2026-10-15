---
id: error-signal
type: concept
fields: [control-theory, economics-finance, political-science]
fields_strong: [control-theory, political-science]
n_sources: 8
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch11-pid, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch02-brief, taylor-1993-discretion/main, wlezien-1995-thermostat/main]
raw_ids: [error signal]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# error-signal

## Canon spine entry

- **error signal** (control-theory): the difference between the reference and the measured output (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch12-error]] (p. 222): information from the actual state of E, which R receives instead of information about D [as `error signal`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-18): control error $e=r-y$ [as `error signal`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-1): $e=r-y$, the controller input
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-2): $e=r-y$ [as `error signal`]
- [[meadows-2008-thinking/ch01-basics]] (pp. 27–28): the discrepancy between actual and desired stock level, which drives the correction
- [[meadows-2008-thinking/ch02-brief]] (pp. 36, 52): the "discrepancy" between goal and actual stock that drives corrections
- [[taylor-1993-discretion/main]] (p. 202): the deviations $y$ and $p-2$ in equation (1) (canon link; not named by the author) [as `error signal`; weak: not really used in this unit; work fields: control-theory, economics-finance]
- [[wlezien-1995-thermostat/main]] (pp. 982, 986, 998): the public's relative preference $R = P^* - P$ is the "signal" sent to policymakers [work fields: control-theory, political-science]

## Candidate bridges

- [structural-analogy] Adaptive law $\dot a=-\alpha we$, $\dot b=-\alpha ne$ ↔ machine learning: stochastic-gradient / LMS-style parameter updates driven by an error signal. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → llm)
- [structural-analogy] balancing loop with discrepancy ↔ control theory: negative feedback on error signal = reference − output. The thermostat's discrepancy is an error signal, but it is floored at 0 and the furnace heat is capped at 5 (p. 197). — from [[meadows-2008-thinking/app-untitled]] (control-theory → control-theory)
- [structural-analogy] Balancing loop with desired level and discrepancy ↔ control theory: negative feedback with reference and error signal — same loop structure, in plain-language diagrams rather than equations. — from [[meadows-2008-thinking/ch01-basics]] (control-theory → control-theory)
- [structural-analogy] TD error $\delta_t$ ↔ control theory: error signal — both are a difference between a current value and a better reference, used to correct the estimate. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → control-theory)
- [structural-analogy] TD error as dopamine burst ↔ control-theory: error signal driving a controller's adaptation — both use a deviation from expectation to correct future behaviour. — from [[sutton-2018-rl/ch15-neuroscience-p1]] (control-theory → control-theory)
- [structural-analogy] $R = P^* - P$ as public signal ↔ control theory: error signal = reference − output — same sign logic, but $P^*$ is unobserved here. — from [[wlezien-1995-thermostat/main]] (control-theory → control-theory)
