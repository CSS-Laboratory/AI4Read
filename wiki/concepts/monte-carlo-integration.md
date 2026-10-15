---
id: monte-carlo-integration
type: concept
fields: [bayesian, information-theory, llm, control-theory, decision-game-theory]
fields_strong: [bayesian, information-theory, llm, control-theory, decision-game-theory]
n_sources: 28
n_works: 10
tiers: [core, reference, deep]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, gelman-2013-bda3/ch03-introduction, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch09-decision, gelman-2013-bda3/ch10-introduction, jaynes-2003-probability/ch17-principles-p2, mackay-2003-information/ch29-monte, mackay-2003-information/ch32-exact, mackay-2003-information/ch41-learning, mackay-2003-information/ch43-boltzmann, mackay-2003-information/ch45-gaussian, mcelreath-2020-rethinking/ch03-sampling, mcgrayne-2011-theory/ch15-navy, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch08-gaussian-p2, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch11-monte, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch26-generative, murphy-2023-pml2/ch34-decision, robert-2011-mcmc/main, sarkka-2023-bayesianfiltering/ch02-bayesian, tenenbaum-2011-grow/main]
raw_ids: [Monte Carlo integration]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# monte-carlo-integration

## Canon spine entry

- **Monte Carlo integration** (bayesian): approximating expectations by averaging over random samples (UG)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 10): averaging $f$ over the chain history to estimate $\mathbb E_\pi[f]$
- [[gelman-2013-bda3/ch03-introduction]] (pp. 70, 77): summaries (e.g. $\theta_1-\theta_2$, LD50) computed from posterior draws
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 109): posterior simulation by drawing hyperparameters, then parameters, then predictions
- [[gelman-2013-bda3/ch09-decision]] (p. 253): 5000 simulated measurements to estimate $L_3$
- [[gelman-2013-bda3/ch10-introduction]] (p. 262): approximate $\mathrm E(h(\theta)|y)$ by $\frac1S\sum h(\theta^s)$ using posterior draws
- [[jaynes-2003-probability/ch17-principles-p2]] (pp. 531–532): estimating an integral by random points; here shown beaten by a grid [work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 51): replacing integrals by counts over samples; the author does not use this name here
- [[mcgrayne-2011-theory/ch15-navy]] (pp. 199–200): here Monte Carlo simulation of random submarine paths to build a prior, not an integral
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 221): learning about a distribution by sampling instead of exact calculation
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 45): here: approximate $p_y$ by pushing samples through $f$ and using an empirical pdf
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 110): posterior of $f(\boldsymbol\theta)$ estimated from samples
- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 273): averaging samples to approximate gradient expectations
- [[murphy-2023-pml2/ch06-optimization-p2]] (pp. 296, 301, 313): used in MCEM, the EI estimate (6.178) and ES gradients [as `Monte Carlo integration`]
- [[murphy-2023-pml2/ch07-inference]] (p. 354): approximate the posterior by $S$ samples
- [[murphy-2023-pml2/ch08-gaussian-p2]] (p. 385): one way to compute GGF moments [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 446): single-sample estimates of ELBO expectations/gradients
- [[murphy-2023-pml2/ch11-monte]] (p. 483): approximate $\mathbb E[f(x)]$ by the sample average of $f$ at draws from $p$; the error is dimension-independent in principle
- [[murphy-2023-pml2/ch24-energy]] (p. 851): unbiased estimate of $\nabla\log Z$ from model samples (p. 851) (reuse) [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch26-generative]] (p. 896): reused id; the GAN objectives discussed are estimated by sample averages (26.7) [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch34-decision]] (pp. 1111, 1126, 1143): single posterior sample in Thompson sampling; samples in MBR and BatchBALD [work fields: bayesian, decision-game-theory]
- [[robert-2011-mcmc/main]] (p. 2): average random draws to approximate integrals; here born at Los Alamos
- [[tenenbaum-2011-grow/main]] (p. 1284): sampling-based approximation proposed as a unifying account of practical Bayesian inference

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 357): approximate ⟨φ⟩ by averaging φ over samples; error variance σ²/R, independent of dimension [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch32-exact]] (p. 419): estimator (32.1); the coupling idea can improve it [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 496): posterior averages by sample means, eq. 41.19 [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch43-boltzmann]] (p. 523): model correlations estimated by averaging along simulation [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch45-gaussian]] (pp. 537, 546): averaging over posterior samples, (45.8), or over $\boldsymbol\theta$ [work fields: information-theory, bayesian]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 23): approximate expectations by sample averages [new; work fields: control-theory, bayesian]

## Candidate bridges

- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [structural-analogy] averaging the conditional prediction over the posterior (1.4) ↔ Monte Carlo integration: with posterior draws it becomes an average over rows of Table 1.1. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [same-math] LOO-CV approximation by importance weights ↔ importance sampling in Monte Carlo integration: weights correct draws from the full posterior toward a leave-out posterior (p. 31). — from [[gelman-2020-workflow/main-p2]] (bayesian → other:importance-sampling-in-monte)
- [structural-analogy] Averaging predictions over the observed $L_i$ ↔ Monte Carlo integration: replacing an expectation over $L$ by a sample average. — from [[hernan-2020-whatif/ch13-standardization]] (bayesian → bayesian)
- [structural-analogy] Density evolution with resampled message populations ↔ bayesian: Monte Carlo integration, approximating a distribution by a sample. — from [[mackay-2003-information/ch47-low]] (information-theory → bayesian)
- [same-math] the posterior of $\gamma=\beta_R+\beta_{AR}$ from per-sample arithmetic (p. 221) ↔ Monte Carlo integration: transform draws, then summarise. — from [[mcelreath-2020-rethinking/ch07-interactions]] (bayesian → bayesian)
- [structural-analogy] inverse-cdf sampling via PIT ↔ Monte Carlo integration — turning uniform draws into draws from a target. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
- [same-math] Reparameterized gradient $\mathbb E_{p(\epsilon)}[\nabla_\phi f(g(\phi,\epsilon))]$ ↔ Monte Carlo integration: a single-sample Monte Carlo estimate of an expectation of a gradient. — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → bayesian)
- [same-math] Importance weighting $w=q(x)/p(x)$ for target risk (19.12–19.16) ↔ Monte Carlo integration: importance sampling re-expresses an expectation under $q$ as one under $p$ times a density ratio. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [same-math] Thompson sampling's one-sample estimate of $p_a$ ↔ Monte Carlo integration: the integral of an indicator under the posterior is estimated by a sample. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → bayesian)
