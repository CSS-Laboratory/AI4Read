---
id: kalman-filter
type: concept
fields: [control-theory, bayesian]
n_sources: 28
tiers: [deep, core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch13-robust, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, kalman-1960-filtering/main, mcgrayne-2011-theory/ch15-navy, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch08-gaussian-p1, sarkka-2023-bayesianfiltering/ch01-are, sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch03-batch, sarkka-2023-bayesianfiltering/ch05-modeling, sarkka-2023-bayesianfiltering/ch06-bayesian, sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch09-gaussian, sarkka-2023-bayesianfiltering/ch10-posterior, sarkka-2023-bayesianfiltering/ch11-particle, sarkka-2023-bayesianfiltering/ch12-bayesian, sarkka-2023-bayesianfiltering/ch13-extended, sarkka-2023-bayesianfiltering/ch14-general, sarkka-2023-bayesianfiltering/ch16-parameter, sarkka-2023-bayesianfiltering/ch17-epilogue, sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional, sarkka-2023-bayesianfiltering/ch20-list, sarkka-2023-bayesianfiltering/ch21-list, todorov-2002-ofc/main, welch-2004-kalmanintro/main]
raw_ids: [Kalman filter]
canon_spine: control-theory
generated_by: build_kg.py
---

# kalman-filter

## Canon spine entry

- **Kalman filter** (control-theory): the optimal recursive estimator for linear systems with Gaussian noise: predict, then correct (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-18, 8-20): mean-square-optimal observer under Gaussian white noise [as `Kalman filter`]
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-23): observer with gains from an optimization, optimal for Gaussian noise
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 98): named as one belief-estimator algorithm based on Bayes' rule
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 131): updates state and disturbance estimates in MPC with mismatch [as `Kalman filter`]
- [[kalman-1960-filtering/main]] (p. 41): the recursive optimal linear estimator (21)+(28)–(30); the paper does not use this name
- [[sarkka-2023-bayesianfiltering/ch01-are]] (p. 13): closed-form solution of the linear Gaussian filtering problem [as `Kalman filter`]
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (pp. xxi–xxii): mean $\mathbf m_k$, covariance $\mathbf P_k$, gain $\mathbf K_k$
- [[sarkka-2023-bayesianfiltering/ch03-batch]] (p. 37): recursive posterior mean and covariance for linear-Gaussian models, as prediction then update
- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 78): estimator used for linear Gaussian models (p. 75); not applicable to the Student's t model
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (p. 97): closed-form Bayesian filter for linear Gaussian models, tracking mean and covariance
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 113): recursive predict–update estimator that the EKF reuses with linearisation
- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 134): here the gain/conditioning step $\mathbf K=\mathbf C\mathbf S^{-1}$ reused with integral-based $\boldsymbol\mu,\mathbf S,\mathbf C$
- [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (p. 169): closed-form prediction/update used as step 2 for all these filters, in affine form
- [[sarkka-2023-bayesianfiltering/ch10-posterior]] (p. 207): the update (10.7)/(10.15) is applied to the linearized model
- [[sarkka-2023-bayesianfiltering/ch11-particle]] (pp. 248–249): here run per particle, conditional on latent $u$
- [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (p. 256): supplies $\mathbf m_k,\mathbf P_k$ and the prediction equations used by the smoother
- [[sarkka-2023-bayesianfiltering/ch13-extended]] (p. 273–274): affine Kalman filter plus RTS smoother solves each linearized problem
- [[sarkka-2023-bayesianfiltering/ch14-general]] (p. 296): The affine filter run on the linearized model in the IPLS
- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 332): gives exact $v_k,S_k$, hence the exact energy in linear Gaussian models
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 349): natural choice for linear problems, with the RTS smoother
- [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (p. 372): predict/update recursions differentiated in A.10
- [[sarkka-2023-bayesianfiltering/ch20-list]] (p. 393–394): named only in 6.7, 6.8 (Kalman filter for random walk and car); no definition here
- [[sarkka-2023-bayesianfiltering/ch21-list]] (p. 397): named entries 6.6, 6.9 and many "Kalman filter" variants
- [[todorov-2002-ofc/main]] (p. 9): gives the internal state estimate $\hat x_t$ in the simulations
- [[welch-2004-kalmanintro/main]] (pp. 1–5): recursive estimator alternating prediction and correction; minimizes mean squared error

### bayesian

- [[mcgrayne-2011-theory/ch15-navy]] (p. 205): a procedure that adds new observations without full recalculation. The author says it can be derived from Bayes' rule [new]
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 240–241, 248): filtering tool the text credits for Stanley's win and uses with Bayes' rule in robot soccer and rat-brain tracking (the chapter does not define it) [new]
- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 365): exact Bayes filter for linear-Gaussian SSMs [new]

## Instances that use it

- [[vectored-thrust-aircraft]] — Kalman filter design, improved by adding a measurement — from [[astrom-2021-feedbacksystems/ch08-output]]
- [[recursive-least-squares]] — Kalman filter with latent state = regression weights — from [[murphy-2023-pml2/ch08-gaussian-p1]]
- [[drift-regression-sine-tracking]] — tracking a sine with random-walk parameters (Fig. 3.5) and with a locally linear Kalman filter (Fig. 3.6) — from [[sarkka-2023-bayesianfiltering/ch03-batch]]
- [[kalman-filter-66]] — Kalman filter, entry 6.6 — from [[sarkka-2023-bayesianfiltering/ch21-list]]
- [[extended-kalman-filter]] — entries 7.4, 7.5 — from [[sarkka-2023-bayesianfiltering/ch21-list]]
- [[kalman-filter-running-average]] — x̂_new = x̂_old + (1/1000)(b₁₀₀₀ − x̂_old) — from [[strang-2023-introduction/ch04-orthogonality-p1]]

## Candidate bridges

- [same-math] Recursive least squares (15.19) ↔ Kalman filter: the author states RLS is a special case of the Kalman filter (§8.2). — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other)
- [structural-analogy] Complementary filter ↔ Kalman filter: both fuse sensors; the former needs only a sensor model. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other)
- [structural-analogy] Belief state $b_k$ with update $F_k$ ↔ control-theory state estimation: Kalman filter output used as the state of a perfect-information problem (the text names Kalman filtering as one choice of $F_k$). — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → control-theory)
- [structural-analogy] Belief state $(x_k,b_k)$ ↔ Kalman filter state estimate: both summarize the information history in a recursively updated quantity (pp. 117, 131). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other)
- [structural-analogy] Gaussian posterior update with linear observations $z_u=a_u'\theta+w_u$ ↔ control-theory: Kalman-type estimation — the text says closed-form Gaussian estimation applies (p. 308); whether the formulas coincide with the Kalman filter is not stated here, so confirm. — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → control-theory)
- [structural-analogy] feature state $y$ with estimator $F(y,u,z)$ ↔ control-theory: observer or Kalman filter state that is exactly updated from control and measurement (p. 391) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [structural-analogy] Output-feedback LQR and optimal state estimation (Kalman filter) ↔ estimation theory; the text only mentions this relation as not discussed (p. 160). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → unspecified)
- [same-math] Kalman filter as derived from Bayes' rule (Aoki 1967) ↔ bayesian: sequential updating — the author says it can be derived directly from Bayes' rule (p. 205). — from [[mcgrayne-2011-theory/ch15-navy]] (bayesian → bayesian)
- [structural-analogy] Kalman gain update (2.123–2.124) ↔ filtering: the text says the gain's name comes from the Kalman filter (Section 8.2.2) — from [[murphy-2023-pml2/ch02-probability-p2]] (bayesian → other)
- [structural-analogy] Kalman filter ↔ hmm-inference (§9.2 as cited): the Gaussian analogue of the HMM forward filter; RTS ↔ HMM forwards-backwards smoothing (pp. 365, 370). — from [[murphy-2023-pml2/ch08-gaussian-p1]] (bayesian → other)
- [structural-analogy] Bayesian filter (state from noisy outputs) ↔ control-theory: observer/state estimator — both reconstruct hidden state from measurements; the unit ties the Kalman filter to LQG control (p. 8). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → control-theory)
- [structural-analogy] Gaussian posterior from linear model and Gaussian prior (Ex. 2.4) ↔ the measurement update of a Kalman filter — candidate only; the Kalman filter is not covered in these pages. — from [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (control-theory → unspecified)
- [same-math] Recursive regression update (3.8) ↔ control-theory: Kalman filter update step — the text states these are special cases of the Kalman filter update, and that only the update part is needed because the parameters are assumed constant (pp. 30–31). — from [[sarkka-2023-bayesianfiltering/ch03-batch]] (control-theory → control-theory)
- [structural-analogy] Lyapunov ODE (4.53) for $\mathbf P(t)$ ↔ control-theory: covariance propagation in the continuous-discrete extended Kalman filter (the text notes the same approximation is used there, p. 59). — from [[sarkka-2023-bayesianfiltering/ch04-discretization]] (control-theory → control-theory)
- [structural-analogy] Constant-gain stationary Kalman filter ↔ time-invariant linear (digital) filter (Ex. 6.3 asks which type). — from [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (control-theory → unspecified)
- [structural-analogy] Sigma-point propagation (UKF) ↔ control-theory: Kalman filter prediction/correction with non-linear dynamics; the Kalman filter is replaced by $\mathbf K=\mathbf C\mathbf S^{-1}$ built from integral-based moments. — from [[sarkka-2023-bayesianfiltering/ch08-general]] (control-theory → control-theory)
- [same-math] per-particle Kalman update in RBPF ↔ [[kalman-filter]]: literally the predict/update equations (11.55), (11.59). — from [[sarkka-2023-bayesianfiltering/ch11-particle]] (control-theory → other)
- [same-math] IERTSS iteration ↔ nonlinear least squares: Gauss–Newton on the cost (13.17), solved by Kalman filter and smoother. — from [[sarkka-2023-bayesianfiltering/ch13-extended]] (control-theory → other)
- [same-math] Kalman innovations $v_k,S_k$ in the energy (16.38) ↔ control-theory: Kalman filter innovation and its covariance — same quantities, here used to score θ. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → control-theory)
- [structural-analogy] Kalman filter choice for linear systems ↔ control-theory observer: both reconstruct hidden state from measurements with a model corrected by data — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → control-theory)
- [same-math] Matrix inversion lemma (A.9) ↔ control-theory: gain of the Kalman filter in two equivalent forms — the same algebraic identity. — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (control-theory → control-theory)
- [structural-analogy] Kalman filter (6.6) ↔ control theory: observer / state estimator — both correct a model prediction with measurements. — from [[sarkka-2023-bayesianfiltering/ch21-list]] (control-theory → control-theory)
- [same-math] recursive average update (4.2 C) ↔ signal processing: Kalman filter with gain 1/n — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other)
- [structural-analogy] TD(0) predict-then-correct from one-step data ↔ Kalman filter: predict, then correct — an estimate is corrected by a new observation. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → other)
- [same-math] forward model with efference copy ↔ control-theory: Kalman filter/observer (pp. 2, 9) — from [[todorov-2002-ofc/main]] (control-theory → control-theory)
