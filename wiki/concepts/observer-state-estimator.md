---
id: observer-state-estimator
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 11
n_works: 7
tiers: [core, deep, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch11-pid, bertsekas-2026-rlcourse/ch01-exact-p5, kalman-1960-filtering/main, liberzon-2012-calculus/ch07-advanced, sarkka-2023-bayesianfiltering/ch06-bayesian, sarkka-2023-bayesianfiltering/ch14-general, sarkka-2023-bayesianfiltering/ch16-parameter, todorov-2002-ofc/main, welch-2004-kalmanintro/main]
aliases: [observer]
raw_ids: [observer (state estimator)]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# observer-state-estimator

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `observer` — 4 digest(s)

## Canon spine entry

- **observer (state estimator)** (control-theory): a model run in parallel and corrected by measurements to reconstruct hidden state (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-7): model copy plus output-error correction $L(y-C\hat x)$ so that $\hat x\to x$ [as `observer (state estimator)`]
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-20): state estimator (9.33), combined into a controller transfer function [alias `observer`]
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-1): observer-based control predicts the state with a model, unlike PID's linear extrapolation [as `observer (state estimator)`]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 129, 131): with Kalman filter, used to reconstruct the state for MPC when it is not measured [as `observer (state estimator)`]
- [[kalman-1960-filtering/main]]: the filter (21) is a model run in feedback with measurements; the author describes it as a feedback system (Remark (m), p. 42)
- [[liberzon-2012-calculus/ch07-advanced]] (p. 175): the output-feedback $\mathcal H_\infty$ controller can be interpreted as state feedback combined with an estimator (observer) [as `observer (state estimator)`]
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]]: canon concept (state estimator); this unit does not mention observers (canon link only, not stated in this unit) [alias `observer`; weak: not really used in this unit; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch14-general]] (p. 279): Smoothers likewise reconstruct hidden state from measurements, here using all of $\mathbf y_{1:T}$ [alias `observer`; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 320): filters/smoothers are the engines used to score parameters [work fields: control-theory, bayesian]
- [[todorov-2002-ofc/main]] (p. 2): forward model combining delayed noisy feedback, plant dynamics and efference copy
- [[welch-2004-kalmanintro/main]] (p. 4): the filter estimates the state, using measurements as feedback [alias `observer`]

## Candidate bridges

- [structural-analogy] Observer Two inferring hidden Z from past inputs (p. 115) ↔ control-theory: an observer / state estimator rebuilding hidden state from past inputs and outputs — both replace a hidden variable by a function of observed history. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [structural-analogy] inverter built from the coder's equations plus a delayer ↔ control theory: system inversion, observers reconstructing past inputs — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → control-theory)
- [same-math] Observer design by eigenvalue assignment ↔ state feedback pole placement (ch. 7): the same problem with $A,B,K$ replaced by $A^T,C^T,L^T$ (p. 8-7). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
- [structural-analogy] Observer's "prediction + correction by error" ↔ model-based learning: a model prediction is corrected by prediction error, as in reward prediction error updates. — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → other:model-based-learning)
- [structural-analogy] PID's linear extrapolation vs observer prediction ↔ state-space control: both predict, one from a model and one from the signal's slope (p. 11-1). — from [[astrom-2021-feedbacksystems/ch11-pid]] (control-theory → control-theory)
- [structural-analogy] IMC/Smith predictor internal model ↔ observer (state estimator): a model runs in parallel with the process, and its mismatch with the output is used for correction. — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]] (control-theory → control-theory)
- [structural-analogy] Integral term of PID ↔ control-theory: disturbance observer on an augmented state $(x,w)$ with $w_{k+1}=w_k$ — the author calls the integral term the simplest instance of the idea of inferring a constant disturbance, and calls the MPC version "a similar strategy" (pp. 130–131). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → control-theory)
- [structural-analogy] Posterior update $b_{k+1}=B_k(\cdot)$ ↔ control-theory: observer/state estimator — a recursive estimator of a hidden quantity, though here it is Bayesian and the state is a distribution (p. 302, 310). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → control-theory)
- [structural-analogy] feature state $y$ with estimator $F(y,u,z)$ ↔ control-theory: observer or Kalman filter state that is exactly updated from control and measurement (p. 391) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [metaphor] "Visible/operative public" ↔ selection bias in survey research: observers see only the self-selected tail (p. 29) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other:statistics)
- [structural-analogy] notional attitude + environment → propositional attitude ↔ theory-of-mind: belief ascription as a function of an agent's internal state plus what the observer knows of the setting — both factor a belief into agent-side and world-side contributions. — from [[dennett-1987-intentional-stance/ch05-beyond-p1]] (theory-of-mind → theory-of-mind)
- [metaphor] Random pattern: maximum entropy yet perceptually uniform ↔ typical set: the details are information-rich but irrelevant to the observer. — from [[pierce-1980-introduction/ch13-information]] (information-theory → information-theory)
- [structural-analogy] Bayesian filter (state from noisy outputs) ↔ control-theory: observer/state estimator — both reconstruct hidden state from measurements; the unit ties the Kalman filter to LQG control (p. 8). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → control-theory)
- [structural-analogy] Kalman correction $\mathbf m_k^-+\mathbf K_k[\,y_k-\mathbf H_k\mathbf m_k^-]$ ↔ control-theory: observer with output-error correction — a model run forward and corrected by the measurement residual. — from [[sarkka-2023-bayesianfiltering/ch03-batch]] (control-theory → control-theory)
- [same-math] Linear-in-parameters regression as $\mathbf{x}_k=\mathbf{x}_{k-1}$, $y_k=\mathbf{H}_k\mathbf{x}_k+\varepsilon_k$ ↔ control-theory: observer for a constant unknown parameter — the same linear Gaussian state space model. — from [[sarkka-2023-bayesianfiltering/ch05-modeling]] (control-theory → control-theory)
- [structural-analogy] Sensor bias as an extra state ↔ control-theory: disturbance estimation by augmenting the observer's state — both augment the state with the unknown quantity. — from [[sarkka-2023-bayesianfiltering/ch05-modeling]] (control-theory → control-theory)
- [structural-analogy] Kalman update $\mathbf m_k=\mathbf m_k^-+\mathbf K_k\mathbf v_k$ ↔ control theory: observer correcting a model prediction by a gain times output error — both run a model and correct it with measurement residuals. — from [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (control-theory → control-theory)
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → control-theory)
- [structural-analogy] IPLF measurement update ↔ control-theory observer: model corrected by measurement via gain $\mathbf K$ — a linear Kalman correction is run on a re-linearized model. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
- [structural-analogy] Linearize-at-the-estimate loop ↔ gain scheduling/extended observers in nonlinear control: the linearization point is itself estimated. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
- [structural-analogy] particle filter ↔ observer / state estimator: a model run forward and corrected by measurements, here for non-linear and non-Gaussian systems. — from [[sarkka-2023-bayesianfiltering/ch11-particle]] (control-theory → control-theory)
- [structural-analogy] Smoothing ↔ state estimation in control (observer using future data): offline refinement of filter estimates. — from [[sarkka-2023-bayesianfiltering/ch13-extended]] (control-theory → control-theory)
- [structural-analogy] Kalman filter choice for linear systems ↔ control-theory observer: both reconstruct hidden state from measurements with a model corrected by data — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → control-theory)
- [structural-analogy] Same test problem under many estimators ↔ control-theory: one plant tested with several observers. — from [[sarkka-2023-bayesianfiltering/ch20-list]] (control-theory → control-theory)
- [structural-analogy] Kalman filter (6.6) ↔ control theory: observer / state estimator — both correct a model prediction with measurements. — from [[sarkka-2023-bayesianfiltering/ch21-list]] (control-theory → control-theory)
- [structural-analogy] ELIZA effect and confirmation bias ↔ human judgment: observers read competence into fluent output. — from [[shapira-2024-clever-hans/main]] (theory-of-mind → other:human-judgment)
- [structural-analogy] Incremental update ↔ control-theory observers: estimate corrected by the error between measurement and prediction, scaled by a gain. — from [[sutton-2018-rl/ch02-multi]] (control-theory → control-theory)
- [structural-analogy] Dyna-Q's model-learning running beside acting ↔ observer/estimator: a model corrected by data and used for decisions. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
- [structural-analogy] state-update function $u$ and belief update (17.10) ↔ control theory: observer / Bayesian state estimator — both recursively fold new measurements into a compact state summary. — from [[sutton-2018-rl/ch17-frontiers]] (control-theory → control-theory)
- [same-math] forward model with efference copy ↔ control-theory: Kalman filter/observer (pp. 2, 9) — from [[todorov-2002-ofc/main]] (control-theory → control-theory)
- [structural-analogy] Residual correction $\hat x^-+K(z-H\hat x^-)$ ↔ observer design: a model run in parallel and corrected by measurement error. — from [[welch-2004-kalmanintro/main]] (control-theory → control-theory)
