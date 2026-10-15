---
id: gibbs-sampling
type: concept
fields: [bayesian, information-theory, control-theory, complex-systems, llm]
fields_strong: [bayesian, information-theory, control-theory, complex-systems, llm]
n_sources: 30
n_works: 7
tiers: [core, reference, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, blei-2017-variational/main-p2, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch18-models, gelman-2013-bda3/ch19-parametric, gelman-2013-bda3/ch20-basis, gelman-2013-bda3/ch22-finite, gelman-2013-bda3/ch23-dirichlet, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch31-ising, mackay-2003-information/ch32-exact, mackay-2003-information/ch43-boltzmann, mcelreath-2020-rethinking/ch08-markov, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch12-markov-p1, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch28-latent-p2, murphy-2023-pml2/ch29-state-p1, murphy-2023-pml2/ch29-state-p2, robert-2011-mcmc/main]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# gibbs-sampling

## Canon spine entry

- **Gibbs sampling** (bayesian): MCMC that updates one variable at a time from its full conditional distribution (grad)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (p. 10): sample each variable from its complete conditional; CAVI uses the same conditional via an expected log
- [[blei-2017-variational/main-p2]] (p. 22): classical sampler that CAVI is closely connected to
- [[gelman-2013-bda3/appc-computation]] (p. 598): cycle through exact conditionals θ | μ,τ; μ | θ,τ; τ | θ,μ
- [[gelman-2013-bda3/ch10-introduction]] (pp. 262, 269): mentioned only as the engines of Bugs and Stan, developed in later chapters
- [[gelman-2013-bda3/ch11-basics]] (pp. 276–277, 281): cycle through subvectors, drawing each from its full conditional given the latest values of the rest; a special case of MH with every jump accepted
- [[gelman-2013-bda3/ch12-computationally]] (p. 293): cycle through conditional draws; most efficient with independent components
- [[gelman-2013-bda3/ch14-introduction]] (p. 375): used for several unknown variances after EM and normal approximation
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 392–393): batch-wise and all-at-once versions for hierarchical regressions
- [[gelman-2013-bda3/ch16-generalized]] (pp. 408, 431): truncated-normal latent data; Bayesian IPF
- [[gelman-2013-bda3/ch17-models]] (p. 440): Gibbs with mixture variables; Metropolis step for $\nu$
- [[gelman-2013-bda3/ch18-models]] (p. 455): used as data augmentation on $(y_{\rm mis},\theta)$
- [[gelman-2013-bda3/ch19-parametric]] (p. 482): here with Metropolis steps for the non-closed-form $\psi_k$ conditionals
- [[gelman-2013-bda3/ch20-basis]] (pp. 492, 494): used to update inclusion indicators γ_h and, in the gdP model, block updates of β
- [[gelman-2013-bda3/ch22-finite]] (pp. 524, 529, 534): alternate draws of indicators given parameters and parameters given indicators
- [[gelman-2013-bda3/ch23-dirichlet]] (p. 551): used for allocations, weights and cluster parameters
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 245–246): Metropolis–Hastings variant with adaptive proposals; relies on conjugate pairs; inefficient with very many parameters
- [[mcgrayne-2011-theory/ch16-eureka]] (pp. 218–219): the Geman brothers' variant of Monte Carlo for imaging problems with many pixels
- [[murphy-2023-pml2/ch04-graphical-p2]] (pp. 168, 171): mentioned as the sampler used for Ising samples; ICM is its deterministic analogue
- [[murphy-2023-pml2/ch07-inference]] (p. 355): sample each variable from its full conditional
- [[murphy-2023-pml2/ch12-markov-p1]] (pp. 505–506): resample each variable from its full conditional; MH with acceptance 1
- [[murphy-2023-pml2/ch15-generalized]] (p. 624): alternate truncated-normal $z$ and Gaussian $w$ draws
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 966, 970): collapsed Gibbs for LDA and LDA-HMM
- [[murphy-2023-pml2/ch29-state-p1]] (p. 996): blocked Gibbs alternates $z_{1:T}$ and $\theta$ [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch29-state-p2]] (p. 1014): blocked Gibbs alternating $\mathbf z_{1:T}$ and $\boldsymbol\theta$ [work fields: bayesian, control-theory]
- [[robert-2011-mcmc/main]] (p. 5): update components from conditionals; named after Gibbs random fields by Geman and Geman (1984)

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 370–371): update one variable (or group) at a time from its conditional; a Metropolis method with all proposals accepted [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch30-efficient]] (p. 391): draw each variable from its conditional; slow random walk when variables are strongly correlated [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch31-ising]] (p. 402): update one spin from its conditional (31.17), local field $b_n$ [work fields: information-theory, bayesian, complex-systems]
- [[mackay-2003-information/ch32-exact]] (p. 418): update one spin at a time from its conditional. Here it is coupled via shared $u$ and the same spin $i$ (Algorithm 32.4) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch43-boltzmann]] (p. 522): rule (43.3) is Gibbs sampling for (43.2) [work fields: information-theory, bayesian, llm]

## Instances that use it

- [[syndrome-decoding-gibbs-failure]] — Gibbs sampling gets stuck on codeword-constrained posteriors — from [[mackay-2003-information/ch29-monte]]
- [[correlated-bivariate-gaussian-rho-0998]] — benchmark target ($\rho=0.998$): HMC is compared with random-walk Metropolis (Fig. 30.2) and overrelaxation with Gibbs sampling (Fig. 30.3) — from [[mackay-2003-information/ch30-efficient]]
- [[gelfand-smith-1990-random-effects]] — the model in (2) solved by Gibbs sampling — from [[robert-2011-mcmc/main]]

## Candidate bridges

- [structural-analogy] CAVI's coordinate updates ↔ bayesian: Gibbs sampling — both cycle through complete conditionals, one sampling and one setting a factor from the expected log — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [structural-analogy] CAVI ↔ Gibbs sampling: both update one block at a time given the others, but CAVI optimizes expected log complete-conditionals (p. 22). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [structural-analogy] Bayesian IPF ↔ Gibbs sampling: cycling over one parameter at a time with a random rescaling — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → bayesian)
- [same-math] data augmentation ↔ Gibbs sampling: alternately draw $y_{\rm mis}$ and parameters from full conditionals (the text calls it a special case of Gibbs) (p. 465). — from [[gelman-2013-bda3/ch18-models]] (bayesian → bayesian)
- [structural-analogy] Gibbs sampling for mixtures ↔ soft K-means: alternate sampling labels and updating parameters, as noted in Ex. 29.16 (p. 383). — from [[mackay-2003-information/ch29-monte]] (information-theory → information-theory)
- [same-math] Gibbs-sampling update (31.17) ↔ bayesian: Gibbs sampling from a full conditional. — from [[mackay-2003-information/ch31-ising]] (information-theory → bayesian)
- [structural-analogy] alternating Q_µ / Q_σ updates (p. 430) ↔ Gibbs sampling: both update one block given the others, but one passes averages, the other samples. — from [[mackay-2003-information/ch33-variational]] (information-theory → bayesian)
- [same-math] Gibbs sampling activity rule ↔ bayesian: Gibbs sampling MCMC, updating one variable from its conditional distribution. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [same-math] Full conditional via Markov blanket (4.32) ↔ Gibbs sampling: the conditional used in Gibbs updates (the text points to Eq. 12.19). — from [[murphy-2023-pml2/ch04-graphical-p1]] (bayesian → bayesian)
- [structural-analogy] Gibbs sampling ↔ optimisation: stochastic analogue of coordinate ascent (p. 355). — from [[murphy-2023-pml2/ch07-inference]] (bayesian → other:optimization)
- [structural-analogy] CAVI update $q_j\propto\exp\mathbb E[\log\tilde p]$ ↔ Gibbs sampling: sample from the full conditional instead of averaging its log (the author says "compare", p. 457) — from [[murphy-2023-pml2/ch10-variational-p2]] (bayesian → bayesian)
- [structural-analogy] Gibbs sampling ↔ optimization: coordinate descent (author's own comparison, p. 505). — from [[murphy-2023-pml2/ch12-markov-p1]] (bayesian → other:optimization)
- [structural-analogy] Blocked Gibbs for LDS ↔ Gibbs sampling in hierarchical models: alternate latent variables and parameters. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → bayesian)
