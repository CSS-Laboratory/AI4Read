---
id: mcmc
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch13-modal, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch24-energy]
generated_by: build_kg.py
---

# mcmc

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch11-basics]] (pp. 275–276): Markov chain Monte Carlo: sequential draws whose distribution converges to p(θ|y); the Markov property helps prove this but is not the key
- [[gelman-2013-bda3/ch13-modal]] (pp. 311, 330): approximations serve as starting points and comparison points for Markov chain simulation
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 720): slice sampling, HMC and SMC are named options for kernel-parameter inference
- [[murphy-2023-pml2/ch24-energy]] (p. 852): sampling the EBM inside the training loop (p. 852) (reuse: Markov chain Monte Carlo)

## Instances that use it

- [[metropolis-1953-particle-system]] — first MCMC algorithm, for the Boltzmann integral of $N$ particles — from [[robert-2011-mcmc/main]]
- [[ohio-state-workshop-1991]] — three-day MCMC conference and program — from [[robert-2011-mcmc/main]]

## Candidate bridges

- [structural-analogy] n_eff for MCMC ↔ survey sampling: effective sample size under dependence, like cluster sampling (our link; the text compares only the var⁺ estimator to cluster sampling, p. 284). — from [[gelman-2013-bda3/ch11-basics]] (bayesian → other)
- [metaphor] "Premature optimization" in software engineering ↔ running MCMC to large effective sample size for an untested model — compute is wasted if bugs appear early (p. 14). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
- [same-math] Invariant distribution of an MCMC chain (eigenvalue 1 of T) ↔ linear algebra: Perron–Frobenius-style stationary vector of a column-stochastic matrix — the text states the eigenvector fact (p. 372). — from [[mackay-2003-information/ch29-monte]] (information-theory → linear-algebra)
- [structural-analogy] MCMC acceptance string as a bottleneck channel ↔ information-theory: noisy channel with capacity limit — a binary decision stream caps information per use. — from [[mackay-2003-information/ch30-efficient]] (information-theory → information-theory)
- [same-math] Gibbs sampling activity rule ↔ bayesian: Gibbs sampling MCMC, updating one variable from its conditional distribution. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [structural-analogy] Heavy-tailed decoding times ↔ information-theory/MCMC: convergence-time diagnostics. Only the heavy-tail idea is shared. — from [[mackay-2003-information/ch49-repeat]] (information-theory → information-theory)
- [same-math] Invariant distribution as principal right-eigenvector of $\mathbf{Q}$ ↔ bayesian: MCMC stationary distribution — the same linear-algebra fact about Markov chains. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [structural-analogy] Eigenvalue gap in (C.36)–(C.37) ↔ bayesian: MCMC mixing — a small gap amplifies perturbations in the first formula, and chain mixing is also governed by eigenvalue gaps. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [same-math] Gibbs/Metropolis–Hastings sampling ↔ the field's MCMC concepts: same algorithms as the Bayesian posterior-sampling toolkit. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → other)
- [same-math] stationary distribution of a chain ↔ Bayesian: MCMC — the target posterior is made the stationary distribution of a chain (the unit only says MCMC is an application, p. 51). — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → bayesian)
- [structural-analogy] Simulated annealing ↔ MCMC: Metropolis–Hastings sampling from $\exp(-\mathcal E)$ with decreasing entropy. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → other)
- [structural-analogy] ELBO maximisation ↔ MCMC: both avoid $p(\mathcal D)$, one by a constant offset and one by density ratios — they differ in mechanism. — from [[murphy-2023-pml2/ch07-inference]] (bayesian → other)
- [structural-analogy] SGD with fixed learning rate as approximate posterior sampler ↔ MCMC (SGLD): both generate approximate posterior samples, differing in explicit noise and learning-rate schedule. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → other)
- [structural-analogy] Noise-scale annealing in SGMs ↔ Bayesian: tempering/annealed sampling in MCMC; both move from a smoothed distribution to the target. — from [[murphy-2023-pml2/ch25-diffusion]] (bayesian → bayesian)
- [metaphor] Paradigm shift (Kuhn) ↔ philosophy of science: the authors' framing of MCMC replacing closed-form solutions. — from [[robert-2011-mcmc/main]] (bayesian → analytic-philosophy)
