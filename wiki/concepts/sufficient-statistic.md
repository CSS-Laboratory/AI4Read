---
id: sufficient-statistic
type: concept
fields: [bayesian, information-theory, control-theory, linear-algebra]
fields_strong: [bayesian, information-theory, control-theory, linear-algebra]
n_sources: 17
n_works: 8
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch03-learning-p1, cover-2006-elements/ch02-entropy, deisenroth-2020-mml/ch06-probability-p2, gelman-2013-bda3/ch02-single, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, mackay-2003-information/ch22-maximum, mackay-2003-information/ch24-exact, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch05-information-p2, polyanskiy-2025-information/ch04-mutual]
aliases: [sufficient-statistics]
generated_by: build_kg.py
---

# sufficient-statistic

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `sufficient-statistics` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch02-single]] (p. 36): $t(y)$ such that the likelihood depends on data only through $t(y)$ [new]
- [[jaynes-2003-probability/ch07-central-p1]] (p. 213): data summaries that alone enter the likelihood; with Gaussian errors, $\bar y$ and $s^2$ [alias `sufficient-statistics`; new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch08-sufficiency]] (pp. 245–246): a function $r$ of the data such that $p(\mathbf x|\theta)=p(r|\theta)b(\mathbf x)$; the posterior then depends on the data only through $r$, for every prior [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch14-simple]] (pp. 429–430): here: $D$ with $p(Y|V)=p(Y|D)$, equivalently $p(V|D)=p(V|YD)$; equal to zero loss of expected entropy information [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 459): here $n$ and $y(n)$ in the tetrahedra problem [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 501): not defined here; $\bar y$ is called one in the Gaussian case [new; weak: not really used in this unit; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (pp. 510, 520): statistic after which position on the data manifold is irrelevant to $\theta$; exists iff the form (17.32) holds [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 537): a data summary carrying all information about the parameters; $(\overline{y^2},\overline{sy},\overline{ty})$ here [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 64): counts N₁,N₀ that are all we need from D to infer θ [alias `sufficient-statistics`; new]
- [[murphy-2023-pml2/ch05-information-p2]] (p. 240): $s(X)$ with $\mathbb I(\theta;s(X))=\mathbb I(\theta;X)$; minimal if a function of every other sufficient statistic [new; work fields: bayesian, information-theory]

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 37): $T$ with $\theta\to T(X)\to X$; equivalent to $I(\theta;T(X))=I(\theta;X)$ [new]
- [[mackay-2003-information/ch22-maximum]] (p. 300): functions of the data (here $\bar x$, $S$) through which the likelihood depends on the data [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch24-exact]] (p. 321): functions of the data (here $\bar x$, S) through which the likelihood depends on the data [new; work fields: information-theory, bayesian]
- [[polyanskiy-2025-information/ch04-mutual]] (p. 54): T such that $P_{X|T}$ does not depend on θ; equivalent to equality in the DPI [new]

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 81): quantity summarizing all essential content of the available information for control; $I_k$ or $b_k$ [new]
- [[bertsekas-2026-rlcourse/ch03-learning-p1]] (p. 360): a function $S_k(I_k)$ through which the optimal control depends on the information vector [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 210): statistics through which $p(x|\theta)$ depends on $\theta$ (Fisher–Neyman) [new]

## Instances that use it

- [[gaussian-sufficient-statistics]] — $\overline y,s^2$ jointly sufficient for $\mu,\sigma$ — from [[jaynes-2003-probability/ch08-sufficiency]]
- [[cauchy-no-sufficient-statistic]] — Cauchy sampling has no sufficient statistic; it appears that no part of the data is irrelevant — from [[jaynes-2003-probability/ch08-sufficiency]]
- [[bernoulli-sufficient-statistic]] — $N$ and the success count are a minimal sufficient statistic for $N$ Bernoulli trials — from [[murphy-2023-pml2/ch05-information-p2]]
- [[normal-mean-sufficient-statistic]] — the sample mean is sufficient for the mean of $\mathcal N(\theta,1)$ — from [[polyanskiy-2025-information/ch04-mutual]]

## Candidate bridges

- [structural-analogy] Sufficient statistic for control (Ex. 3.1.6) ↔ statistics: sufficient statistic in inference; the text says the concept originated there (p. 360). — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → other:statistics)
- [same-math] Sufficient statistic ↔ statistics: equality condition of the data processing inequality $I(\theta;T(X))=I(\theta;X)$ is the sufficiency condition (p. 37). — from [[cover-2006-elements/ch02-entropy]] (information-theory → other:statistics)
- [structural-analogy] Kolmogorov sufficient statistic ↔ statistics: sufficient statistics, $\theta\to T(X)\to X$ — the text draws the parallel via a Markov chain. — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → other:statistics)
- [structural-analogy] Kolmogorov structure function / minimal sufficient statistic ↔ MDL: model plus data cost — the Historical Notes call MDL close in spirit. — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → information-theory)
- [same-math] Max-entropy form $e^{\lambda_0+\sum\lambda_ir_i}$ ↔ statistics: exponential family with sufficient statistics $r_i$ — same functional form. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other:statistics)
- [structural-analogy] $A\perp\!\!\!\perp L\mid\pi(L)$ ↔ sufficient statistics: given one summary, the rest of $L$ carries no further information about treatment. — from [[hernan-2020-whatif/ch15-outcome]] (bayesian → bayesian)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity. — from [[mackay-2003-information/ch31-ising]] (information-theory → information-theory)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Fisher information F_η=Cov[T(x)] ↔ exponential families: variance of sufficient statistics is the curvature of log A(η) — same objects, as in (3.67)–(3.72). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → information-theory)
- [same-math] CRF/MRF log-likelihood gradient (features minus expected features) ↔ exponential-family MLE: derivative of log-partition is expected sufficient statistics (Sec. 2.4.3, cited p. 183). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → other:exponential-family-mle)
- [same-math] marginals as $\nabla_\eta\log Z$ ↔ exponential families: mean of sufficient statistics equals gradient of the log partition (p. 435). — from [[murphy-2023-pml2/ch09-message]] (bayesian → information-theory)
- [structural-analogy] VMP ↔ belief propagation: message passing, but messages are expected sufficient statistics (p. 470) — from [[murphy-2023-pml2/ch10-variational-p2]] (bayesian → bayesian)
- [structural-analogy] $f_Z$ as sufficient statistic, $f_*\perp f_X|f_Z$ ↔ graphical models: a hub variable that screens off training from test. — from [[murphy-2023-pml2/ch18-gaussian-p2]] (bayesian → bayesian)
- [structural-analogy] hidden state $z_t$ compressing the past ↔ sufficient statistic in sequential updating: both summarize history for predicting the next item. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → other:statistics)
- [same-math] $\nabla_\theta\log Z_\theta=\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]$ ↔ exponential families: gradient of the log-normaliser equals the expected sufficient statistic — same identity for $E_\theta=-\theta^T\phi(x)$ (added link; not stated here). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → information-theory)
- [structural-analogy] Sufficient statistic ↔ statistics: Fisher's sufficiency — equality in the DPI is the information-theoretic form (p. 54). — from [[polyanskiy-2025-information/ch04-mutual]] (information-theory → other:statistics)
- [same-math] Tilted family P_λ with sufficient statistic φ ↔ statistics: standard exponential family with natural parameter λ and mean parameter μ=∇ψ(λ) (p. 310). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other:statistics)
- [structural-analogy] Information bottleneck ↔ statistical inference: sufficient statistics — the paper says that in cases with sufficient statistics, almost all information can be kept at finite β (p. 9) — from [[tishby-2000-bottleneck/main]] (information-theory → other:statistics)
