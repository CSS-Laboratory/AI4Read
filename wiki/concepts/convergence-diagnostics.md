---
id: convergence-diagnostics
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 23
n_works: 7
tiers: [core, deep, reference]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, betancourt-2017-hmc/main-p3, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch18-models, gelman-2013-bda3/ch19-parametric, gelman-2013-bda3/ch22-finite, gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p2, gelman-2020-workflow/main-p3, mackay-2003-information/ch29-monte, mackay-2003-information/ch32-exact, mcelreath-2020-rethinking/ch08-markov, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch12-markov-p2, robert-2011-mcmc/main]
aliases: [convergence-diagnostics-r-hat-ess-divergences, convergence-diagnostics-rhat-ess-divergences]
raw_ids: [Convergence diagnostics]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# convergence-diagnostics

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `convergence-diagnostics-r-hat-ess-divergences` — 1 digest(s)
- `convergence-diagnostics-rhat-ess-divergences` — 2 digest(s)

## Canon spine entry

- **Convergence diagnostics (R-hat, ESS, divergences)** (bayesian): checks that chains have mixed and that the sampler explored the posterior faithfully (grad)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 11): here: split $\hat R$ as the empirical diagnostic, with geometric ergodicity as the formal sufficient condition (p. 15); ESS measures estimator precision
- [[betancourt-2017-hmc/main-p3]] (pp. 44–46): divergences and E-BFMI as HMC-specific checks, with split $\hat R$ generic
- [[gelman-2013-bda3/appc-computation]] (pp. 593–594, 598): R̂ (below 1.1 in the Stan example, where the chains appeared well mixed) and n_eff, via `print` or `monitor`
- [[gelman-2013-bda3/ch10-introduction]] (p. 270): here, running parallel simulations from different starting points and checking they mix
- [[gelman-2013-bda3/ch11-basics]] (pp. 284–285, 287): here R̂ computed from B and W on split chains, with threshold about 1.1
- [[gelman-2013-bda3/ch12-computationally]] (p. 302): $\hat R$ near 1 and large effective sample size judge HMC convergence
- [[gelman-2013-bda3/ch14-introduction]] (p. 375): $\hat R<1.1$ for all parameters in the two-variance fit
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 388): $\hat R<1.1$ after 500 steps with ten sequences
- [[gelman-2013-bda3/ch16-generalized]] (p. 424): $\hat R$ below 1.2
- [[gelman-2013-bda3/ch18-models]] (p. 466): $\hat R<1.1$ used for data augmentation chains
- [[gelman-2013-bda3/ch19-parametric]] (pp. 475, 482): $\widehat R<1.1$ in the assay; within/between variance comparison for PERC
- [[gelman-2013-bda3/ch22-finite]] (p. 530): $\hat R<1.1$ on suitable scales (log for variances, logit for $\lambda$)
- [[gelman-2020-workflow/main-p1]] (pp. 13, 16): $\widehat R<1.01$, $R^*$, effective sample size, absence of divergent transitions; they cannot detect a model coded differently than intended [alias `convergence-diagnostics-r-hat-ess-divergences`]
- [[gelman-2020-workflow/main-p2]] (p. 28): divergent transitions signal difficult geometry and untrustworthy results
- [[gelman-2020-workflow/main-p3]] (p. 57): R̂, trace plots including warmup; R̂ < 1.01 desired, R̂ > 2 means poor mixing
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 250, 257): here `n_eff` (effective sample count) and Rhat (Gelman–Rubin). Rhat may be seen "perhaps as a signal of danger, but never of safety" [alias `convergence-diagnostics-rhat-ess-divergences`]
- [[mcelreath-2020-rethinking/ch10-counting]] (pp. 298, 321): n_eff and Rhat used to check MCMC fits [as `Convergence diagnostics`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 373–374): n_eff, Rhat and divergent iterations are checked for the more complex models
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 408): n_eff, Rhat and divergences as signs of the sampling problem
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 526–531): checks that chains mixed: trace plots, rank plots, $\hat R$, split-$\hat R$, $N_{\rm eff}$ [alias `convergence-diagnostics-rhat-ess-divergences`]
- [[robert-2011-mcmc/main]] (p. 9): here via the ergodic theorem (3) and CLT (4), needing a consistent variance estimate

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 366, 379): detecting convergence and independence of an MCMC run is hard; the author lists no perfect tool [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch32-exact]] (p. 413): here, an exact answer to "has the chain converged?" for suitable chains [work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Many repeated measurements sharing one unknown systematic error ↔ bayesian: Convergence diagnostics (ESS) — correlated draws carry less information than the nominal sample size. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
