---
id: observer-state-estimator
type: concept
fields: [control-theory]
n_sources: 7
tiers: [core, deep, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch11-pid, bertsekas-2026-rlcourse/ch01-exact-p5, kalman-1960-filtering/main, liberzon-2012-calculus/ch07-advanced, sarkka-2023-bayesianfiltering/ch16-parameter, todorov-2002-ofc/main]
raw_ids: [observer (state estimator)]
canon_spine: control-theory
generated_by: build_kg.py
---

# observer-state-estimator

## Canon spine entry

- **observer (state estimator)** (control-theory): a model run in parallel and corrected by measurements to reconstruct hidden state (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-7): model copy plus output-error correction $L(y-C\hat x)$ so that $\hat x\to x$ [as `observer (state estimator)`]
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-1): observer-based control predicts the state with a model, unlike PID's linear extrapolation [as `observer (state estimator)`]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 129, 131): with Kalman filter, used to reconstruct the state for MPC when it is not measured [as `observer (state estimator)`]
- [[kalman-1960-filtering/main]]: the filter (21) is a model run in feedback with measurements; the author describes it as a feedback system (Remark (m), p. 42)
- [[liberzon-2012-calculus/ch07-advanced]] (p. 175): the output-feedback $\mathcal H_\infty$ controller can be interpreted as state feedback combined with an estimator (observer) [as `observer (state estimator)`]
- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 320): filters/smoothers are the engines used to score parameters
- [[todorov-2002-ofc/main]] (p. 2): forward model combining delayed noisy feedback, plant dynamics and efference copy

## Candidate bridges

- [structural-analogy] Observer Two inferring hidden Z from past inputs (p. 115) ↔ control-theory: an observer / state estimator rebuilding hidden state from past inputs and outputs — both replace a hidden variable by a function of observed history. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [structural-analogy] IMC/Smith predictor internal model ↔ observer (state estimator): a model runs in parallel with the process, and its mismatch with the output is used for correction. — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → other)
- [structural-analogy] Posterior update $b_{k+1}=B_k(\cdot)$ ↔ control-theory: observer/state estimator — a recursive estimator of a hidden quantity, though here it is Bayesian and the state is a distribution (p. 302, 310). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → control-theory)
- [structural-analogy] Bayesian filter (state from noisy outputs) ↔ control-theory: observer/state estimator — both reconstruct hidden state from measurements; the unit ties the Kalman filter to LQG control (p. 8). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → control-theory)
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → other)
- [structural-analogy] particle filter ↔ observer / state estimator: a model run forward and corrected by measurements, here for non-linear and non-Gaussian systems. — from [[sarkka-2023-bayesianfiltering/ch11-particle]] (control-theory → other)
- [structural-analogy] Kalman filter (6.6) ↔ control theory: observer / state estimator — both correct a model prediction with measurements. — from [[sarkka-2023-bayesianfiltering/ch21-list]] (control-theory → control-theory)
