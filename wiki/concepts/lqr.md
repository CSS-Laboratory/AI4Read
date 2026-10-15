---
id: lqr
type: concept
fields: [control-theory]
n_sources: 7
tiers: [core, deep, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch13-robust, bertsekas-2026-rlcourse/ch01-exact-p2, kalman-1960-filtering/main, liberzon-2012-calculus/ch06-linear, recht-2019-tour/main]
raw_ids: [LQR]
canon_spine: control-theory
generated_by: build_kg.py
---

# lqr

## Canon spine entry

- **LQR** (control-theory): linear-quadratic regulator: the optimal state feedback for a quadratic cost on state and effort (grad)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-28): optimal linear state feedback for a quadratic cost (7.29)–(7.33)
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-22): optimal state feedback for quadratic cost, used with the filter in LQG [as `LQR`]
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-23): state feedback minimizing $\int(y^2+\rho u^2)dt$; phase margin ≥ 60°, infinite gain margin
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 31–33): scalar finite-horizon linear-quadratic problem with linear optimal policy and quadratic cost-to-go
- [[kalman-1960-filtering/main]] (p. 42): Problem II (noise-free regulator with quadratic index) with solution (34)–(37); not named LQR in the paper
- [[liberzon-2012-calculus/ch06-linear]] (p. 145): linear dynamics, quadratic cost on state and control; optimal control is linear state feedback
- [[recht-2019-tour/main]] (pp. 11–12): linear dynamics with quadratic cost; optimal policy is linear state feedback via the Riccati equation

## Instances that use it

- [[vectored-thrust-aircraft]] — LQR with weight $\rho$ on inputs — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[web-server-control]] — discrete-time LQR for load control — from [[astrom-2021-feedbacksystems/ch07-state]]
- [[scalar-integrator-lqr]] — $\dot x=u$; $P=\tanh(t_1-t)$ finite horizon, $P=1$ infinite horizon — from [[liberzon-2012-calculus/ch06-linear]]
- [[double-integrator-lqr]] — Exercise 6.4 — from [[liberzon-2012-calculus/ch06-linear]]
- [[double-integrator-lqr]] — position/velocity of a unit mass; nominal control works from 10 samples — from [[recht-2019-tour/main]]
- [[unstable-laplacian-data-center-lqr]] — three coupled heat sources with $A$ having 1.01 on its diagonal; shows the safety gap — from [[recht-2019-tour/main]]
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm — from [[recht-2019-tour/main]]

## Candidate bridges

- [structural-analogy] LQR cost weights $Q_x,Q_u$ ↔ economics/decision theory: a loss that trades off outcome error against effort or cost of action. — from [[astrom-2021-feedbacksystems/ch07-state]] (control-theory → economics-finance)
- [same-math] Kalman–Bucy Riccati equation ↔ LQR Riccati equation: equivalences (8.32) map one into the other (p. 8-20). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → other)
- [structural-analogy] Program synthesis ↔ LQR design: given a model and specification, produce a controller that by construction meets the specification — the authors draw this comparison (p. 15-16). — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → other)
- [structural-analogy] Quadratic closed forms of §17 ↔ LQR: value function quadratic in the state — here only on a restricted interval with constraint $0\le y\le x$. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → other)
- [structural-analogy] Riccati equation as $\min_w$ of linear equations (§8) ↔ LQR: a Riccati equation arising from minimizing over linear feedback-like choices. — from [[bellman-1957-dp/ch11-xi]] (control-theory → other)
- [same-math] Riccati operator fixed point $K=F(K)$ and its optimal gain $L^*$ ↔ control-theory LQR: the scalar LQR solution (the unit does not use the word LQR). — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → control-theory)
- [same-math] Theorem 4 duality (filter ↔ noise-free regulator) ↔ control-theory: the LQR design equations — the paper itself gives the substitution $X\to\hat X'(T-\tau)$ between (28–30) and (35–37). — from [[kalman-1960-filtering/main]] (control-theory → control-theory)
- [structural-analogy] Riccati equation (2.64) and its matrix form ↔ control theory: LQR Riccati equation (the author says matrix Riccati equations play a central role in Chapter 6, p. 54) — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
- [structural-analogy] Exercise 3.8 (linear system, quadratic cost) ↔ LQR: the text points to Chapter 6 for this class (p. 78) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → other)
- [structural-analogy] Output-feedback LQR and optimal state estimation (Kalman filter) ↔ estimation theory; the text only mentions this relation as not discussed (p. 160). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → unspecified)
- [structural-analogy] ARE (7.19) ↔ LQR ARE of Ch. 6 — similar matrix form with sign changes, but the author stresses that the meanings differ. — from [[liberzon-2012-calculus/ch07-advanced]] (control-theory → unspecified)
