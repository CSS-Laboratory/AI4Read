---
id: kalman-gain
type: concept
fields: [control-theory, bayesian]
n_sources: 13
tiers: [deep, core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, kalman-1960-filtering/main, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch08-gaussian-p1, sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch03-batch, sarkka-2023-bayesianfiltering/ch06-bayesian, sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch09-gaussian, sarkka-2023-bayesianfiltering/ch10-posterior, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional, welch-2004-kalmanintro/main]
raw_ids: [Kalman gain]
canon_spine: control-theory
generated_by: build_kg.py
---

# kalman-gain

## Canon spine entry

- **Kalman gain** (control-theory): the weight on a new measurement, set by how uncertain the prediction is relative to the sensor (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-18, 8-20): $L[k]=AP[k]C^T(R_w+CP[k]C^T)^{-1}$ (discrete); $L=PC^TR_w^{-1}$ (continuous) [as `Kalman gain`]
- [[kalman-1960-filtering/main]] (p. 41): $\Delta^*(t)=\Phi P^*M'[MP^*M']^{-1}$, the weight on the innovation in (19); in (21) it multiplies $y(t)$
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (p. xxi): $\mathbf K_k$, "gain matrix of a Kalman/Gaussian filter"
- [[sarkka-2023-bayesianfiltering/ch03-batch]] (p. 35; same form with $\mathbf m_{k-1},\mathbf P_{k-1}$ on p. 30): $\mathbf K_k=\mathbf P_k^-\mathbf H_k^T\mathbf S_k^{-1}$, the weight on the prediction error $y_k-\mathbf H_k\mathbf m_k^-$
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (p. 97): $\mathbf K_k=\mathbf P_k^-\mathbf H_k^{\mathsf T}\mathbf S_k^{-1}$, weight on the measurement residual
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 114): $\mathbf K_k=\mathbf P_k^-\mathbf H_x^\top\mathbf S_k^{-1}$, the weight on the innovation $\mathbf v_k$
- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 134): $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$
- [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (p. 188): $\mathbf K_k=\mathbf C_k\mathbf S_k^{-1}$ in the SLR filters
- [[sarkka-2023-bayesianfiltering/ch10-posterior]] (p. 207): $\mathbf K=\mathbf P\mathbf A^{\mathsf T}\mathbf S^{-1}$
- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (p. 373): $K_k$; derivative given in (A.68)
- [[welch-2004-kalmanintro/main]] (p. 3): $K_k=P_k^-H^T(HP_k^-H^T+R)^{-1}$, the weight on the residual

### bayesian

- [[murphy-2023-pml2/ch02-probability-p2]] (p. 29): $\mathbf K=\mathbf C\mathbf S^{-1}$, which scales the correction to the mean (new)
- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 366): matrix weighting the innovation: $K_t=\Sigma_{t|t-1}H_t^\top S_t^{-1}$ [new]

## Candidate bridges

- [structural-analogy] Kalman gain update (2.123–2.124) ↔ filtering: the text says the gain's name comes from the Kalman filter (Section 8.2.2) — from [[murphy-2023-pml2/ch02-probability-p2]] (bayesian → other)
- [structural-analogy] Smoother gain $\mathbf G_k$ ↔ control: Kalman gain — both weight a correction by relative uncertainty. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → control-theory)
- [metaphor] choosing λ between MC and TD ↔ control-theory: trade-off between trusting a model prediction (bootstrap) and measured outcomes (Kalman-gain-like weighting). — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
- [structural-analogy] Kalman gain as trust weight ↔ statistics: inverse-variance weighted averaging — in the toy case with $Q=0$ the estimate is a weighted mean of prior and data. — from [[welch-2004-kalmanintro/main]] (control-theory → other)
