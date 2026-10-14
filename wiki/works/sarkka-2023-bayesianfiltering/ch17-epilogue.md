---
id: sarkka-2023-bayesianfiltering/ch17-epilogue
work: sarkka-2023-bayesianfiltering
unit: 17 Epilogue
pages: 349–354
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Epilogue: choosing a method, and what the book left out

## L0 — One line
For non-linear state estimation, start with the extended Kalman filter and its smoother (EKF/ERTSS), move to sigma-point methods if these work badly, or to particle methods if Gaussian approximations fail, and use Monte Carlo sampling as a last resort.

## L1 — The gist (≤ 120 words)
The chapter asks which filtering, smoothing or parameter-estimation method to use for a given state-space problem. If the problem is linear, the Kalman filter and RTS smoother are the natural choice. For non-linear models with Gaussian noise, start with the extended Kalman filter (EKF) and its smoother (ERTSS), then try iterated or sigma-point versions. Use particle methods when Gaussian approximations fail or when exactness is needed. If a state or parameter can be marginalized out, prefer that to sampling it. In parameter estimation, generally use the same approximations as the final application. The chapter ends with pointers to topics the book omitted, such as continuous-time filters, multiple-model methods, target tracking, bounds and parallel methods.

**Prerequisites:** state-space models; Kalman filter and RTS smoother; the book's EKF, sigma-point, particle and MCMC methods (earlier chapters).

## L2 — Key ideas
- Linear problems: Kalman filter and RTS smoother are the natural choice, also for evaluating the quantities needed in parameter estimation (p. 349).
- For non-linear Gaussian models, Gaussian-approximation filters are the first choice in applications. If theoretical exactness is needed, particle (or grid-based) methods are the only option (p. 349).
- It is always a good idea to start with the extended Kalman filter (EKF) and its smoother (ERTSS). Iterated versions can improve the results; the iterated ERTSS often does well because it converges to the MAP (maximum a posteriori) estimate (p. 349).
- Sigma-point methods trade off cost, accuracy and consistency of error estimates. More complicated methods are not guaranteed to be better (p. 350).
- Particle methods: test the bootstrap filter first, check whether states or parameters can be marginalized out (Rao–Blackwellization), and consider a better importance distribution (pp. 350–351).
- Parameter estimation: use the same approximations as the final application. Real models are more or less wrong anyway, so one should be careful not to make them worse with bad approximations (p. 351).
- Omitted topics are listed with references (pp. 351–354).

## L3 — Walkthrough

### 17.1 Which method should I choose? (pp. 349–351)

**Linear case.** The Kalman filter and RTS smoother are natural choices, also for evaluating the quantities needed in parameter estimation (p. 349). The non-linear/non-Gaussian case is harder (p. 349).

**Non-linear, Gaussian noise.** The model is (p. 349)
$$x_k = f(x_{k-1}) + q_{k-1}, \qquad y_k = h(x_k) + r_k, \tag{17.1}$$
where $f$ and $h$ are "somewhat well-behaved". Here $x_k$ is the state, $y_k$ the measurement, and $q_{k-1}$, $r_k$ the Gaussian noises.
- For applications, where the goal is good state and parameter estimates and exactness is not important in itself, the first choice is a Gaussian approximation-based filter/smoother (p. 349).
- If theoretical exactness is needed, the only option is particle filters and smoothers (or grid-based solutions) (p. 349).

**Which Gaussian method.**
- Start with the EKF and ERTSS. They are the only algorithms used in practice for over half a century: "they simply work" (p. 349).
- Iterated EKF/ERTSS can improve results. The iterated ERTSS often does well because it converges to the MAP estimate (p. 349).
- If the EKF/ERTSS work badly or not at all, move to sigma-point methods. Spherical cubature and unscented methods are computationally light and tend to give very good results. Their error estimates may not always be consistent with the actual errors, and the EKF/ERTSS tend to share this problem (p. 350).
- The unscented transform has more tuning parameters than spherical cubature. This can be an advantage or a disadvantage. Spherical cubature is an unscented transform with a particular parameter choice (p. 350).
- Gauss–Hermite methods tend to have more consistent errors, so they are more robust. Their computational complexity is high (p. 350).
- Higher-order cubature/unscented rules have moderate cost and high accuracy, but can give negative weights. Other integration rules not covered in the book may avoid these problems (p. 350).
- Iterated sigma-point methods can improve the non-iterated ones. Monte Carlo integration can sometimes replace sigma-point integration inside Gaussian approximations (p. 350).
- There is no guarantee that more complicated algorithms improve results, so test the EKF/ERTSS first (p. 350).
- The bootstrap filter is easy to implement. It can sometimes serve as a reference solution when debugging and testing Gaussian filters (p. 350).

*Intuition note.* The authors put the EKF/ERTSS first because they simply work, and because more complicated algorithms are not guaranteed to give better results, so the EKF/ERTSS are tested first. The text moves from EKF/ERTSS to sigma-point methods when the EKF/ERTSS work badly, and to particle methods when Gaussian approximations do not work or the problem does not fit.

**Particle-based solutions.**
- Use them when the problem does not fit the non-linear Gaussian framework, or when Gaussian approximations fail for other reasons (p. 350).
- The bootstrap filter, and probably a particle smoother, should be tried first, with enough particles (p. 350).
- The clear disadvantage is high computational load. Check early whether any states or parameters can be marginalized out ("Rao–Blackwellized"), exactly or approximately. If so, one should always prefer marginalization to sampling (p. 350).
- Footnote rule of thumb: use Monte Carlo sampling only as a last resort when all other options have failed (p. 350).
- Also check whether the optimal or almost optimal importance distribution can be used. Non-linear Gaussian filters can in principle build such distributions. This may be computationally heavy and cause convergence problems (p. 351).
- If they are used, it might be advisable to inflate the filter covariances somewhat or to use Student's t-distributions instead of the Gaussians as they are (p. 351).

**Parameter estimation (p. 351).**
- Generally use the same approximations as in the final application, if the estimates will later be used in filters and smoothers.
- If a single point estimate is needed, ML and MAP are "not bad choices". Checking the posterior spread with MCMC may be useful.
- If the true parameter values matter, particle filtering combined with MCMC is "probably the safest bet".
- Estimating true parameters is possible only in simulated scenarios. In real applications the models are more or less wrong anyway. One should be careful not to ruin already probably inaccurate models with bad filter/smoother approximations.

*Intuition note.* The estimator and the model should be judged together. Real models are probably already imperfect, so a poor filter or smoother approximation risks making them worse.

### 17.2 Further topics (pp. 351–354)
The book covers mainly non-linear Kalman-type and particle methods. The authors list pointers to other areas, not an exhaustive list (p. 351).
- **Continuous-time filters and smoothers.** The state, and sometimes the measurements, are modeled with stochastic differential equations (SDEs). Full filtering theory is in Jazwinski (1970), smoothing theory is credited to Striebel (1965) and Leondes et al. (1970). The text points to continuous-time extensions of EKF, unscented, Gaussian and particle methods (pp. 351–352).
- **Other Gaussian integration methods.** Various other integration rules not presented in the book could be used to build new Gaussian filters and smoothers. One particularly interesting approach fits a Gaussian-process non-parametric model to the non-linear functions at sample points (Deisenroth et al.). It is related to kernel/Gaussian-process quadratures, which are numerical integration methods based on Gaussian process regression (p. 352).
- **Multiple-model methods** (GPB1, GPB2, IMM). They approximate Bayesian solutions for a fixed number of modes. The active mode is a discrete latent variable modeled as a Markov chain, and given its value the system is (approximately) Gaussian. The methods use a mixture of Gaussians (a bank of Kalman/extended Kalman filters), obtained by moment matching (p. 352).
- **Related methods for switching linear dynamic systems (SLDS):** expectation correction (EC), expectation propagation (EP). SLDS is another name for multiple-mode problems, and these models are special cases of conditionally Gaussian models (pp. 352–353).
- **Non-Gaussian measurements** (e.g. Student's t). Variational Bayes can sometimes give tractable inference. EP can serve for non-linear, non-Gaussian systems. Both are closely related to the Gaussian filters of the book. Variational Bayes can also estimate unknown time-varying parameters (p. 353).
- **Multiple target tracking.** Specific methods exist for data association and an unknown number of targets (p. 353).
- **Omitted topics:** the Cramér–Rao lower bounds (CRLB), which are lower bounds on the mean-squared error achievable by any non-linear filter in a given problem; observability and controllability, related to whether the state can be determined from the measurements at all; conditions for particle filter convergence; square-root versions of filters for numerical stability (p. 353).
- **Parallel computation** on GPUs, with special parallel filtering and smoothing methods (pp. 353–354).

## Toy example (ours, not from the text)
Linear scalar case, where the Kalman filter applies. Model: $x_k = 0.5\,x_{k-1} + q_{k-1}$ with $Q=1$, and $y_k = x_k + r_k$ with $R=1$. Prior: $m=2$, $P=4$.
- Predict: $m^- = 0.5\cdot 2 = 1$. $P^- = 0.5^2\cdot 4 + 1 = 2$.
- Update with $y=2$: $S = P^- + R = 3$. $K = P^-/S = 2/3$. $m = 1 + \tfrac23(2-1) = 1.667$. $P = P^- - K S K = 2 - \tfrac49\cdot 3 = 0.667$.

The result is exact here. For non-linear $f$ or $h$, the EKF replaces them by their local slopes, and the same formulas become an approximation. That is why the chapter says to try the EKF first.

## Concepts
- [[kalman-filter]] — natural choice for linear problems, with the RTS smoother (p. 349)
- [[state-space-model]] — model (17.1): state transition $f$ plus noise, measurement $h$ plus noise (p. 349)
- [[extended-kalman-filter]] (new) — Gaussian-approximation filter; first method to try; has an iterated version and smoother (ERTSS) (p. 349)
- [[sigma-point-methods]] (new) — unscented, spherical cubature, Gauss–Hermite and higher-order rules for Gaussian filters (p. 350)
- [[particle-filter]] (new) — Monte Carlo filter for models outside the Gaussian framework; the bootstrap filter is the easiest (p. 350)
- [[rao-blackwellization]] (new) — marginalizing out states or parameters exactly or approximately, preferred to sampling (p. 350)
- [[multiple-model-methods]] (new) — GPB1, GPB2, IMM: Gaussian mixtures for systems with discrete modes (p. 352)
- [[observability]] — whether the state can be determined from measurements; mentioned as omitted (p. 353)
- [[controllability]] — mentioned together with observability as omitted (p. 353)

## Canonical instances
- [[nonlinear-gaussian-ssm]] (new) — model (17.1), the setting for the main recommendations (p. 349)

## Bridges (candidates)
- [structural-analogy] Kalman filter choice for linear systems ↔ control-theory observer: both reconstruct hidden state from measurements with a model corrected by data
- [structural-analogy] observability/controllability omitted here ↔ control-theory observability/controllability: same questions, asked for estimation
- [metaphor] "test the simple EKF first as a baseline" ↔ control practice of testing simple (e.g. PID) control before complex designs

## Questions this raises
- When do EKF error estimates become inconsistent, and how can this be detected in practice?
- How much does Rao–Blackwellization reduce the number of particles needed for a given accuracy?
- How do the CRLB and the observability conditions tell us what any filter can achieve?
- How do multiple-model methods compare with particle filters for mode-switching systems?

## Reading notes
- Printed = pdf − 30 (pdf 379 = printed 349).
- Equation (17.1) is garbled in the text layer (symbols such as "D", "C", and a missing minus sign). I reconstructed it as $x_k=f(x_{k-1})+q_{k-1}$, $y_k=h(x_k)+r_k$ from the text layer and context, not from a page image.
- No other equations appear. The unit is prose advice and a reference list; citations are named only as the text names them.
- Each page carries a pre-publication copyright header (Cambridge University Press, 2nd edition, 2023).
