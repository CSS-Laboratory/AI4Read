---
id: blei-2017-variational/index
work: blei-2017-variational
type: work-map
units: [blei-2017-variational/main-p1, blei-2017-variational/main-p2]
---

# Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). *Variational Inference: A Review for Statisticians*. Journal of the American Statistical Association, 112(518), 859–877. DOI: 10.1080/01621459.2017.1285773

## In one paragraph
Bayesian inference needs the posterior, but its normalizing constant (the evidence) is often too hard to compute. This review presents variational inference (VI) as an alternative to sampling. You pick a simple family of densities and find the member closest in KL divergence to the posterior. Since that KL cannot be computed directly, you maximize the ELBO instead. For the mean-field family, coordinate ascent (CAVI) gives explicit updates. In exponential-family models these updates have a neat form, and stochastic natural-gradient steps scale them to very large data sets. VI is usually faster than MCMC, but it has no exactness guarantee and tends to underestimate posterior variance. The review also covers applications, thin theory, models that are not conditionally conjugate, and open problems.

## The path through the work
- [[blei-2017-variational/main-p1]] — Variational inference turns posterior approximation into optimization: choose a simple family of densities and maximize the ELBO, which minimizes the KL divergence to the exact posterior.
- [[blei-2017-variational/main-p2]] — Variational inference (VI) turns posterior computation into optimization. It is already used widely, has only partial theory, has been extended beyond conditional conjugacy (including by Monte Carlo gradients), and the appendices give a CAVI derivation for ARD regression, a Gaussian mixture specification with Stan code, and CAVI updates for LDA.

## Big ideas across units
- **Inference as optimization.** VI replaces sampling with finding the closest member of a family Q to the posterior. Part 1 sets this up and compares it with MCMC. Part 2 lists open problems such as other divergences and combining VI with MCMC. Units: main-p1, main-p2.
- **The ELBO as the working objective.** The KL to the posterior depends on the evidence, so one maximizes the ELBO, which lower-bounds the log evidence. Units: main-p1, main-p2.
- **Mean-field family and coordinate ascent (CAVI).** Independent factors are optimized one at a time, each set from the expected log joint. Part 1 derives this and works through a Gaussian mixture. Part 2's appendices apply it to ARD regression and LDA. Units: main-p1, main-p2.
- **Conjugacy and exponential families give closed-form updates.** Each optimal factor lies in the same family as its complete conditional. Part 2 then asks what happens when conditional conjugacy fails. Units: main-p1, main-p2.
- **Scaling up with stochastic VI.** Natural-gradient steps on single data points make CAVI work for big data. Part 2 shows the payoff: topics from 1.8M New York Times articles. Units: main-p1, main-p2.
- **Beyond conditional conjugacy.** Non-exponential-family complete conditionals break the standard updates. The remedies are tailored bounds, delta/Laplace methods, message passing, and "black box" Monte Carlo gradients of the ELBO. Unit: main-p2.
- **Mean-field underestimates variance.** This is seen in the 2-D Gaussian example, explained by the direction of the KL, and raised again in the theory results and open problems. Units: main-p1, main-p2.
- **The Gaussian mixture as a running example.** It appears as a full CAVI derivation with a comparison against Hamiltonian MC (Stan), and again as a specification with Stan code. Units: main-p1, main-p2.

## How to read it
- **Essential:** main-p1. It holds the whole conceptual core: the ELBO, mean-field, CAVI, exponential-family updates and stochastic VI. Part 2 builds on it throughout.
- **Next, on a first pass:** the main-text portion of main-p2 (NYT application, applications survey, theory, non-conjugate models, open problems). It depends on the ELBO, mean-field/CAVI and conjugacy ideas from main-p1.
- **Can be skipped at first:** the appendices in main-p2. A (ARD regression), B (Gaussian mixture spec and Stan code) and C (LDA updates) are worked details. A and C depend on CAVI and complete conditionals, and B depends on the Gaussian mixture example in main-p1.

## Concepts introduced
Several ids look like near-duplicates across units. They are kept as written in the digests.
- [[variational-inference-elbo]] — main-p1
- [[kl-divergence]] — main-p1
- [[marginal-likelihood-evidence]] — main-p1
- [[elbo-evidence-lower-bound]] — main-p1
- [[mean-field-family]] — main-p1
- [[cavi-coordinate-ascent-vi]] — main-p1 (main-p2 uses [[coordinate-ascent-vi]])
- [[coordinate-ascent-vi]] — main-p2
- [[markov-chain-monte-carlo-mcmc]] — main-p1
- [[gibbs-sampling]] — main-p1
- [[hamiltonian-monte-carlo]] — main-p1
- [[complete-conditional]] — main-p1
- [[conjugate-prior]] — main-p1
- [[conditionally-conjugate-model]] — main-p1 (main-p2 uses [[conditional-conjugacy]])
- [[conditional-conjugacy]] — main-p2
- [[natural-gradient]] — main-p1
- [[stochastic-variational-inference]] — main-p1
- [[em-algorithm]] — main-p1
- [[label-switching]] — main-p1
- [[log-sum-exp-trick]] — main-p1
- [[black-box-vi]] — main-p2
- [[automatic-relevance-determination]] — main-p2
- [[latent-dirichlet-allocation]] — main-p2
- [[gaussian-mixture-model]] — main-p2
- [[variance-underestimation-mean-field]] — main-p2
- [[hierarchical-model]] — main-p2
- [[posterior-distribution]] — main-p2
