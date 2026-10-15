---
id: state-feedback
type: concept
fields: [control-theory, linear-algebra]
fields_strong: [control-theory, linear-algebra]
n_sources: 7
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch14-fundamental, boyd-2018-vmls/ch10-matrix, boyd-2018-vmls/ch17-constrained, liberzon-2012-calculus/ch04-maximum-p2, liberzon-2012-calculus/ch06-linear]
aliases: [state-feedback-closed-loop, state-feedback-control, state-feedback-pole-placement]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# state-feedback

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `state-feedback-closed-loop` — 1 digest(s)
- `state-feedback-control` — 1 digest(s)
- `state-feedback-pole-placement` — 4 digest(s)

## Canon spine entry

- **state feedback / pole placement** (control-theory): u = −Kx chosen to put the closed-loop eigenvalues where you want them (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch07-state]] (pp. 7-10, 7-11, 7-15): law $u=-Kx+k_fr$ chosen to give the closed loop a desired characteristic polynomial [alias `state-feedback-pole-placement`]
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-12): here applied to $\hat x$: $u=-K\hat x+k_fr$ [as `state feedback / pole placement`; alias `state-feedback-pole-placement`]
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-20, 14-25): choosing closed-loop poles; this unit adds rules for choosing them robustly [as `state feedback / pole placement`; alias `state-feedback-pole-placement`]
- [[liberzon-2012-calculus/ch04-maximum-p2]] (p. 109): here: $u^*$ expressed via Γ as a function of state
- [[liberzon-2012-calculus/ch06-linear]] (p. 147): here the linear feedback $u=-R^{-1}B^TPx$ is derived from the necessary conditions, with $P$ given by (6.10) or the RDE (6.14) [alias `state-feedback-pole-placement`]

### linear-algebra

- [[boyd-2018-vmls/ch10-matrix]] (pp. 185–186): with $u_t=Kx_t$, $x_{t+1}=(A+BK)x_t$ [alias `state-feedback-closed-loop`; new]
- [[boyd-2018-vmls/ch17-constrained]] (p. 371): $u_t=Kx_t$; $K$ found from $n$ solves of the LQ problem with $x^{\rm init}=e_i$ [alias `state-feedback-control`; new]

## Instances that use it

- [[predator-prey]] — linearised state feedback regulates lynx population — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[drug-administration-two-compartment]] — state-feedback dosing vs pulsed doses — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[state-feedback-control]] — closed-loop matrix A + BK — from [[boyd-2018-vmls/ch10-matrix]]

## Candidate bridges

- [structural-analogy] Matching closed-loop characteristic polynomial coefficients (2.26)–(2.28) ↔ control theory: pole placement by state feedback — both choose gains to put closed-loop roots where wanted (the chapter only points to later chapters, p. 2-28). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → control-theory)
- [same-math] Observer design by eigenvalue assignment ↔ state feedback pole placement (ch. 7): the same problem with $A,B,K$ replaced by $A^T,C^T,L^T$ (p. 8-7). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
- [structural-analogy] Cascade control with all states measured ↔ state feedback: the text calls state feedback the "ultimate case" of cascade (p. 15-19). — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → control-theory)
- [structural-analogy] Policy $v(c,T)$ as feedback on state ↔ control-theory: state feedback $u=-Kx$ — action as function of the current state (the toy example gives $y=-x$) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] State feedback $u=Kx$ giving $A+BK$ ↔ control and dynamical systems: changing the dynamics matrix by closing a loop. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → control-theory)
- [structural-analogy] Switching curve Γ as a state-feedback policy ↔ dynamic programming: optimal policy as a function of state. — from [[liberzon-2012-calculus/ch04-maximum-p2]] (control-theory → control-theory)
- [structural-analogy] parameterized policy $\pi_\theta$ updated by gradient ascent on $J$ ↔ control theory: state feedback $u=-Kx$ with gain tuned to optimize a cost — both tune a feedback law's parameters. — from [[sutton-2018-rl/ch13-policy]] (control-theory → control-theory)
