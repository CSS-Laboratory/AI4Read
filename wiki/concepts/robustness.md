---
id: robustness
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 17
n_works: 5
tiers: [core, reference, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch13-robust, astrom-2021-feedbacksystems/ch14-fundamental, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p6, liberzon-2012-calculus/ch07-advanced, recht-2019-tour/main, sarkka-2023-bayesianfiltering/ch05-modeling]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# robustness

## Canon spine entry

- **robustness** (control-theory): feedback keeps performance good even when the plant model is wrong (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-14): feedback gives good performance despite disturbances and uncertain process dynamics
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-23): here: feedback around a nonlinear, variable amplifier gives a practically linear input–output relation
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): the inherent property of feedback systems that the text gives as the reason they can often be analyzed and designed using comparatively simple models
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-5, p. 4-10): closed-loop op-amp gain is insensitive to the open-loop gain $k$; an imperfect model can still be used for design
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-33): here: a good feedback law for $\tilde u$ can tolerate model uncertainty in the cancellation
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-17): only touched on: Theorem 7.3 assumes precise knowledge of the process; robustness is deferred to Chapter 13
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-17): here expressed by margins: how much the system may deviate from the nominal model and remain stable
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-12, 11-13): ZN tuning lacks it; in the AFM example the modified rule raises the stability margin
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-6): measured by margins and by $M_s=1/s_m$
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-1): closed loop stays stable and performs well despite model error
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-5, 14-23): here measured by $M_s$, $M_t$, phase and gain margin
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 108): here: robust controller design checks one fixed controller over a parameter range (e.g. $|1+bL|<1$)
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 115): here: the loss $K_L-K^*$ from keeping the nominal policy when parameters change
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 313): here, a base policy $\pi$ that works adequately for all $\theta^i$
- [[liberzon-2012-calculus/ch07-advanced]] (p. 174): $\mathcal H_\infty$ design keeps disturbance-to-output gain bounded
- [[recht-2019-tour/main]] (pp. 13–14): here, guaranteed stabilisation for every system in an estimated uncertainty set
- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 78): here: tolerance to outlier measurements via heavy-tailed or clutter noise [work fields: control-theory, bayesian]

## Instances that use it

- [[bahdanau-fig2-length-robustness]] — BLEU vs sentence length: RNNencdec falls, RNNsearch-50 does not — from [[bahdanau-2015-attention/main]]
- [[eight-schools]] — hypothetical $y_8=100$ motivates robustness; $t_4$ and varying-$\nu$ analyses show insensitivity for the real data — from [[gelman-2013-bda3/ch17-models]]
- [[chloride-concentration]] — 54 points, 21 B-spline coefficients; shrinkage toward a line, variable selection, robustness to outliers — from [[gelman-2013-bda3/ch20-basis]]

## Candidate bridges

- [structural-analogy] stability only against specified disturbances ↔ control-theory: robustness over a stated class of disturbances/models — the verdict depends on the set. — from [[ashby-1956-cybernetics/ch05-stability]] (control-theory → control-theory)
- [structural-analogy] Hubs dominating connectivity ↔ complex-systems: robustness and fragility — hubs matter for network tolerance (not discussed in this unit). — from [[barabasi-1999-scaling/main]] (complex-systems → complex-systems)
- [structural-analogy] Stability bound $\sum_nD(c^nx)$ ↔ control-theory: robustness of optimal value to model error — bounds how much a perturbed return changes the solution. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [structural-analogy] Stability Thm 3–4 ($u(c)/(1-a)$) ↔ robustness: error in the model data bounded by a geometric-series amplification. — from [[bellman-1957-dp/ch04-iv]] (control-theory → other:unnamed)
- [structural-analogy] Redundant gender marking ↔ error-correcting codes: parity bits add redundancy for robustness to noise. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [structural-analogy] Robustness–accuracy trade-off ↔ information-theory: minimax/universal coding — performance is traded across a model class. — from [[jaynes-2003-probability/ch21-outliers]] (bayesian → information-theory)
- [metaphor] "Closeness depends on the norm" ↔ robustness: which perturbations count as small depends on the chosen measure (not stated in this unit) — from [[liberzon-2012-calculus/ch01-introduction]] (control-theory → other:unnamed)
- [structural-analogy] Resilience from redundant loops on different time scales ↔ control-theory: robustness through multiple feedback paths — both keep performance when one mechanism fails. — from [[meadows-2008-thinking/ch03-systems]] (control-theory → control-theory)
- [structural-analogy] hub dependence ↔ robustness and fragility: the same structure gives resilience to random loss and vulnerability to targeted loss (p. 114) — from [[mitchell-2009-guidedtour/ch15-science]] (complex-systems → complex-systems)
- [structural-analogy] Equilibrium strategy that guarantees the value ↔ mechanism design / robustness: strategies that do not depend on correct beliefs about the other player. — from [[osborne-2004-introduction/ch11-strictly]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Noise added to cover linearization error ↔ robustness: model uncertainty treated as extra disturbance. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → other:unnamed)
- [structural-analogy] Random spanning tree marginals ↔ network robustness: an edge whose removal disconnects $G$ has $\ell_e=1$ (p. 126), so by Theorem 13.5.1 it lies in every spanning tree. — from [[spielman-2025-sagt/ch13-random]] (linear-algebra → other:network-robustness)
- [structural-analogy] Hyperbolic (robust) vs. marginal (fragile) fixed points ↔ complex-systems: robustness and fragility — some structures survive small perturbations and others do not. — from [[strogatz-2024-nonlinear/ch06-phase-p1]] (complex-systems → complex-systems)
- [structural-analogy] RL safety via modelling, testing and stability theory ↔ control theory: robustness and adaptive-control guarantees (p. 477). — from [[sutton-2018-rl/ch17-frontiers]] (control-theory → control-theory)
- [structural-analogy] Robustness to trivial alterations ↔ ML evaluation: out-of-distribution/adversarial testing of generalization — both probe whether a model learned the rule or surface correlations. — from [[ullman-2023-trivial-alterations/main]] (theory-of-mind → llm)
