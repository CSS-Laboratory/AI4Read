---
id: sufficient-statistics
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [jaynes-2003-probability/ch07-central-p1, murphy-2023-pml2/ch03-statistics-p1]
generated_by: build_kg.py
---

# sufficient-statistics

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 64): counts N₁,N₀ that are all we need from D to infer θ [new]

### information-theory

- [[jaynes-2003-probability/ch07-central-p1]] (p. 213): data summaries that alone enter the likelihood; with Gaussian errors, $\bar y$ and $s^2$ [new]

## Instances that use it

- [[gaussian-sufficient-statistics]] — $\overline y,s^2$ jointly sufficient for $\mu,\sigma$ — from [[jaynes-2003-probability/ch08-sufficiency]]
- [[cauchy-no-sufficient-statistic]] — Cauchy sampling has no sufficient statistic; it appears that no part of the data is irrelevant — from [[jaynes-2003-probability/ch08-sufficiency]]
- [[bernoulli-sufficient-statistic]] — $N$ and the success count are a minimal sufficient statistic for $N$ Bernoulli trials — from [[murphy-2023-pml2/ch05-information-p2]]
- [[normal-mean-sufficient-statistic]] — the sample mean is sufficient for the mean of $\mathcal N(\theta,1)$ — from [[polyanskiy-2025-information/ch04-mutual]]

## Candidate bridges

- [structural-analogy] Sufficient statistic for control (Ex. 3.1.6) ↔ statistics: sufficient statistic in inference; the text says the concept originated there (p. 360). — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → other)
- [same-math] Sufficient statistic ↔ statistics: equality condition of the data processing inequality $I(\theta;T(X))=I(\theta;X)$ is the sufficiency condition (p. 37). — from [[cover-2006-elements/ch02-entropy]] (information-theory → other)
- [structural-analogy] Kolmogorov sufficient statistic ↔ statistics: sufficient statistics, $\theta\to T(X)\to X$ — the text draws the parallel via a Markov chain. — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → other)
- [structural-analogy] Kolmogorov structure function / minimal sufficient statistic ↔ MDL: model plus data cost — the Historical Notes call MDL close in spirit. — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → other)
- [same-math] Max-entropy form $e^{\lambda_0+\sum\lambda_ir_i}$ ↔ statistics: exponential family with sufficient statistics $r_i$ — same functional form. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other)
- [structural-analogy] $A\perp\!\!\!\perp L\mid\pi(L)$ ↔ sufficient statistics: given one summary, the rest of $L$ carries no further information about treatment. — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → other)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity. — from [[mackay-2003-information/ch31-ising]] (information-theory → information-theory)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Fisher information F_η=Cov[T(x)] ↔ exponential families: variance of sufficient statistics is the curvature of log A(η) — same objects, as in (3.67)–(3.72). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → other)
- [same-math] CRF/MRF log-likelihood gradient (features minus expected features) ↔ exponential-family MLE: derivative of log-partition is expected sufficient statistics (Sec. 2.4.3, cited p. 183). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → other)
- [same-math] marginals as $\nabla_\eta\log Z$ ↔ exponential families: mean of sufficient statistics equals gradient of the log partition (p. 435). — from [[murphy-2023-pml2/ch09-message]] (bayesian → other)
- [structural-analogy] VMP ↔ belief propagation: message passing, but messages are expected sufficient statistics (p. 470) — from [[murphy-2023-pml2/ch10-variational-p2]] (bayesian → other)
- [structural-analogy] $f_Z$ as sufficient statistic, $f_*\perp f_X|f_Z$ ↔ graphical models: a hub variable that screens off training from test. — from [[murphy-2023-pml2/ch18-gaussian-p2]] (bayesian → other)
- [structural-analogy] hidden state $z_t$ compressing the past ↔ sufficient statistic in sequential updating: both summarize history for predicting the next item. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → other)
- [same-math] $\nabla_\theta\log Z_\theta=\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]$ ↔ exponential families: gradient of the log-normaliser equals the expected sufficient statistic — same identity for $E_\theta=-\theta^T\phi(x)$ (added link; not stated here). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → other)
- [structural-analogy] Sufficient statistic ↔ statistics: Fisher's sufficiency — equality in the DPI is the information-theoretic form (p. 54). — from [[polyanskiy-2025-information/ch04-mutual]] (information-theory → other)
- [same-math] Tilted family P_λ with sufficient statistic φ ↔ statistics: standard exponential family with natural parameter λ and mean parameter μ=∇ψ(λ) (p. 310). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other)
- [structural-analogy] Information bottleneck ↔ statistical inference: sufficient statistics — the paper says that in cases with sufficient statistics, almost all information can be kept at finite β (p. 9) — from [[tishby-2000-bottleneck/main]] (information-theory → other)
