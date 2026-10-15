---
id: integral-action
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 11
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch15-architecture-p1, astrom-2021-feedbacksystems/ch15-architecture-p2, bertsekas-2026-rlcourse/ch01-exact-p5]
raw_ids: [integral action]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# integral-action

## Canon spine entry

- **integral action** (control-theory): accumulating past error so that steady-state error goes to zero (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-19): control proportional to the integral of the error; zero steady-state error if a steady state is reached [as `integral action`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-15, 2-17): gives zero steady-state error to a constant disturbance, and $G_{yr}(0)=1$ if stable
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-4): the integrator drives steady-state error to zero despite disturbances and model errors
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-25): augment state with $\int(y-r)dt$; forces $y=r$ in steady state if the closed loop is stable
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-27): obtained here by estimating a constant disturbance state [as `integral action`]
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-24): integral control gives a zero at the origin from disturbance to error [as `integral action`]
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-4): forces zero steady-state error if a steady state exists; no linearity assumed [as `integral action`]
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-10): makes $S\to0$ at low frequency; $G_{yv}\approx s/k_i$
- [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (p. 15-19, p. 15-21): anti-windup is needed in cascade and selector structures [as `integral action`]
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-28): drives steady-state error to zero ($G_{v\theta}(0)=0$)
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 131): in PID, the integral term acts as a dynamic estimator of an unknown average disturbance [as `integral action`]

## Instances that use it

- [[cruise-control]] — integral action rejects hill disturbance — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[integral-action-by-augmentation]] — constant disturbance estimated as a state — from [[astrom-2021-feedbacksystems/ch08-output]]

## Candidate bridges

- [structural-analogy] Integral action u = k_i∫e ↔ accumulator or error-correction terms in learning rules — only if both are the same running sum of errors (not stated in this unit). — from [[astrom-2021-feedbacksystems/ch01-introduction]] (control-theory → unspecified)
- [structural-analogy] Integral action ($\dot z=y-r$ forces $y=r$) ↔ perceptual control: behavior keeps a perceived variable at a reference by acting on the error. — from [[astrom-2021-feedbacksystems/ch07-state]] (control-theory → control-theory)
- [structural-analogy] Integral action / perfect adaptation ↔ biology: adaptation in sensory systems such as the pupillary reflex — the text links both to feedback with integral action (p. 11-6). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → other:biology)
- [structural-analogy] Piece $B$ accumulating the speed error, so final speed is exactly $V$ (eq. 5) ↔ control-theory: integral action removes steady-state error. — from [[maxwell-1868-governors/main]] (control-theory → control-theory)
- [structural-analogy] Thermostat settling below its setting ↔ proportional-only control leaving a steady offset; the integral-action fix is not in this unit (canon link; not stated in this unit). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → unspecified)
- [metaphor] "Never forgets" in LSTD ↔ control theory: integral action accumulating past error — both accumulate history, with no built-in forgetting. — from [[sutton-2018-rl/ch09-policy-p2]] (control-theory → control-theory)
- [metaphor] "Signal stops once adjusted" ↔ steady-state error going to zero (integral action) — the text does not model integral action. — from [[wlezien-1995-thermostat/main]] (control-theory → unspecified)
