---
id: exponential-family
type: concept
fields: [information-theory, bayesian, complex-systems, linear-algebra, llm]
fields_strong: [information-theory, bayesian, complex-systems, linear-algebra, llm]
n_sources: 24
n_works: 11
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch12-information-p2, deisenroth-2020-mml/ch06-probability-p2, gelman-2013-bda3/ch02-single, jaynes-1957-information/main, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch22-maximum, mackay-2003-information/ch31-ising, mackay-2003-information/ch43-boltzmann, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch02-probability-p2, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch36-strong-p1, tishby-2000-bottleneck/main]
aliases: [exponential-family-gibbs, exponential-family-gibbs-distribution]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# exponential-family

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `exponential-family-gibbs` — 6 digest(s)
- `exponential-family-gibbs-distribution` — 10 digest(s)

## Canon spine entry

- **exponential family / Gibbs distribution** (information-theory): the form of every MaxEnt solution under expectation constraints: p ∝ exp(Σ λ_i f_i) (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch11-maximum]] (p. 267): the max-entropy solution has the form $e^{\lambda_0+\sum\lambda_ir_i}$ [alias `exponential-family-gibbs`]
- [[cover-2006-elements/ch12-information-p1]] (p. 294): the tilted form (12.110) of $P^*$ under expectation constraints [alias `exponential-family-gibbs`]
- [[cover-2006-elements/ch12-information-p2]] (pp. 301, 309): P*(a) ∝ Q(a)e^{λa²} and P_λ ∝ P₁^λP₂^{1−λ} are exponential tilts
- [[jaynes-1957-information/main]] (p. 623): max-entropy solution $p_i=\exp\{-[\lambda_0+\sum\lambda_kf_k(x_i)]\}$ [alias `exponential-family-gibbs-distribution`]
- [[mackay-2003-information/ch22-maximum]] (p. 307): $P\propto\exp(\sum w_kf_k)$; ML matches model averages to data averages [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch31-ising]] (p. 400): Boltzmann law $P\propto\exp[-\beta E]$ over spin states (31.2) [alias `exponential-family-gibbs-distribution`; work fields: information-theory, bayesian, complex-systems]
- [[mackay-2003-information/ch43-boltzmann]] (p. 522): $P\propto\exp(\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x)$ as an energy-based distribution [alias `exponential-family-gibbs-distribution`; work fields: information-theory, bayesian, llm]
- [[nielsen-2020-elementary/main-p1]] (pp. 21–22): canonical density (89), Fisher matrix $=\nabla^2F$; dually flat with mixture connection
- [[nielsen-2020-elementary/main-p2]] (p. 29): $p_\theta=\exp(\theta^\top t-F(\theta))$, log-normalizer $F$ as Bregman generator [alias `exponential-family-gibbs`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 74): the tilted measure $Q^f\propto e^fQ$ is of this exponential-tilting form (canon link; the unit does not call it that) [alias `exponential-family-gibbs-distribution`]
- [[polyanskiy-2025-information/ch06-extremization]] (p. 100): $Q_X(n)=Z(\lambda)^{-1}e^{-\lambda f(n)}$; solves max-entropy bounds [alias `exponential-family-gibbs-distribution`]
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 642): the tree law (33.20) [alias `exponential-family-gibbs-distribution`]
- [[tishby-2000-bottleneck/main]] (p. 6): form $p(\tilde x|x)\propto p(\tilde x)e^{-\beta d}$ of the optimal encoder [alias `exponential-family-gibbs-distribution`]

### bayesian

- [[gelman-2013-bda3/ch02-single]] (pp. 36–37): densities $f(y)g(\theta)e^{\phi(\theta)^Tu(y)}$; these have natural conjugate priors [new]
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 291): form $u_j=e^{-\lambda g_j}/Z(\lambda)$ of the comparison distribution; the bound (9.76)–(9.77) is attained iff $f_j=u_j$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 292): "Gibbs canonical ensemble"; the function Z (from (9.75), not shown here) and $\overline G=-\partial\log Z/\partial\lambda$ [alias `exponential-family-gibbs`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch11-discrete]] (p. 356): maximum-entropy solution under expectation constraints is $p_i=\exp(-\lambda_0-\sum\lambda_jf_j(x_i))$ [alias `exponential-family-gibbs`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch12-ignorance]] (p. 376): the solution form (12.11) with partition function $Z$ [alias `exponential-family-gibbs`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch14-simple]] (pp. 443–447): the geometric/exponential priors (14.59) and the Bose–Einstein form (14.77) [as `exponential family / Gibbs distribution`; alias `exponential-family-gibbs-distribution`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 519): form (17.33), $m(x)e^{-l\beta(x)}/Z$ [alias `exponential-family-gibbs-distribution`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch22-introduction]] (p. 639): the form (22.30), with partition function $Z$ giving the multipliers [alias `exponential-family-gibbs-distribution`; work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch09-big]] (p. 282): family of common GLM distributions, each maximum entropy under some constraints [new]
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 34): densities $h(\mathbf x)\exp[\boldsymbol\eta^\top\mathcal T(\mathbf x)-A(\boldsymbol\eta)]$ (new)

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 211): $h(x)\exp(\langle\theta,\phi(x)\rangle-A(\theta))$ [new]

## Instances that use it

- [[bayesian-logistic-regression-nonconjugate]] — simple model whose posterior is not exponential-family — from [[blei-2017-variational/main-p2]]
- [[gaussian-as-exponential-family]] — $\phi(x)=(x,x^2)$, $\theta=(\mu/\sigma^2,-1/2\sigma^2)$ — from [[deisenroth-2020-mml/ch06-probability-p2]]
- [[bernoulli-as-exponential-family]] — $\theta=\log\frac\mu{1-\mu}$, giving the sigmoid — from [[deisenroth-2020-mml/ch06-probability-p2]]
- [[bernoulli-as-exponential-family]] — logit natural parameter, sigmoid mean, $A=\log(1+e^\eta)$ — from [[murphy-2023-pml2/ch02-probability-p2]]
- [[categorical-softmax]] — softmax from the exponential-family form of the categorical — from [[murphy-2023-pml2/ch02-probability-p2]]
- [[kl-as-bregman-exponential-family]] — reverse KL from the log-normalizer — from [[nielsen-2020-elementary/main-p2]]

## Candidate bridges

- [same-math] Max-entropy form $e^{\lambda_0+\sum\lambda_ir_i}$ ↔ statistics: exponential family with sufficient statistics $r_i$ — same functional form. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other:statistics)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [same-math] P*(a) ∝ Q(a)e^{λf(a)} (Example 12.6.1) ↔ statistical mechanics/exponential families: the same Gibbs-type tilt of a base measure. — from [[cover-2006-elements/ch12-information-p2]] (information-theory → complex-systems)
- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → information-theory)
- [structural-analogy] Gaussian as maximum entropy under fixed mean and variance ↔ information-theory: the maximum-entropy principle and exponential families (pp. 216–217) — from [[jaynes-2003-probability/ch07-central-p1]] (bayesian → information-theory)
- [same-math] Partition function $Z(\lambda)$ and $u_j\propto e^{-\lambda g_j}$ ↔ statistical mechanics / exponential families: Gibbs distribution with normaliser $Z$. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (bayesian → complex-systems)
- [same-math] §9.9 Gibbs distribution with $\overline G=-\partial\log Z/\partial\lambda$ ↔ information-theory: exponential family from MaxEnt under an expectation constraint. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → information-theory)
- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → other:exponential-family-theory)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (bayesian → information-theory)
- [same-math] Cramér–Rao equality condition ↔ information-theory: exponential family from MaxEnt — Jaynes shows (17.33) is the Chapter 11 form. — from [[jaynes-2003-probability/ch17-principles-p1]] (bayesian → information-theory)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [same-math] ML for exponential families (22.32) ↔ information theory: maxent solution (22.36) — both give the same exponential form, as shown on p. 308. — from [[mackay-2003-information/ch22-maximum]] (information-theory → information-theory)
- [structural-analogy] entropic distribution $\exp[-\alpha D_{\rm KL}]$ ↔ information-theory: Gibbs / exponential-family form. — from [[mackay-2003-information/ch23-useful]] (information-theory → information-theory)
- [same-math] HMC target $e^{-H}$ with separable $K(\mathbf p)$ ↔ information-theory: Gibbs/exponential-family distribution — the $\mathbf x$-marginal is exactly $e^{-E}/Z$. — from [[mackay-2003-information/ch30-efficient]] (information-theory → information-theory)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity. — from [[mackay-2003-information/ch31-ising]] (information-theory → information-theory)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → information-theory)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Fisher information F_η=Cov[T(x)] ↔ exponential families: variance of sufficient statistics is the curvature of log A(η) — same objects, as in (3.67)–(3.72). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → information-theory)
- [same-math] CRF/MRF log-likelihood gradient (features minus expected features) ↔ exponential-family MLE: derivative of log-partition is expected sufficient statistics (Sec. 2.4.3, cited p. 183). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → other:exponential-family-mle)
- [same-math] MLN joint $\exp(\sum_i w_in_i)/Z$ ↔ log-linear (exponential-family) MRF: it is an MRF with feature counts $n_i$. — from [[murphy-2023-pml2/ch04-graphical-p3]] (bayesian → other:log-linear-exponential-family)
- [structural-analogy] NGD with Fisher preconditioner ↔ Bayesian inference: the text says it is equivalent to EKF sequential inference in the online exponential-family case (p. 281) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → bayesian)
- [structural-analogy] Natural parameters vs moment parameters ↔ exponential-family duality: ordinary gradient in $\mu$ equals natural gradient in $\lambda$ (p. 284) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other:exponential-family-duality)
- [same-math] marginals as $\nabla_\eta\log Z$ ↔ exponential families: mean of sufficient statistics equals gradient of the log partition (p. 435). — from [[murphy-2023-pml2/ch09-message]] (bayesian → information-theory)
- [same-math] $\nabla_\theta\log Z_\theta=\mathbb E_{p_\theta}[-\nabla_\theta E_\theta]$ ↔ exponential families: gradient of the log-normaliser equals the expected sufficient statistic — same identity for $E_\theta=-\theta^T\phi(x)$ (added link; not stated here). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → information-theory)
- [same-math] Fisher information of an exponential family $=\nabla^2F=\mathrm{Cov}[t]$ ↔ information-theory: exponential family / Gibbs distribution — $F$ is the log-normalizer — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] KL between exponential-family members = Bregman divergence of the log-normalizer ↔ information theory: coding-cost excess (relative entropy) — same quantity (p. 29). — from [[nielsen-2020-elementary/main-p2]] (information-theory → information-theory)
- [same-math] $\mathcal H(\Lambda)\le\inf_\lambda\lambda\Lambda+\log_2Z(\lambda)$ ↔ statistical physics/MaxEnt: partition function and Gibbs (exponential-family) form $P_\lambda\propto2^{-\lambda\,\text{cost}}$ (p. 205) — from [[polyanskiy-2025-information/ch12-variable]] (information-theory → complex-systems)
- [same-math] Tilted family P_λ with sufficient statistic φ ↔ statistics: standard exponential family with natural parameter λ and mean parameter μ=∇ψ(λ) (p. 310). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other:statistics)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [same-math] Max-entropy under fixed variance gives Gaussian ↔ exponential-family / Gibbs form of MaxEnt solutions (canon link; not stated in this unit). — from [[stone-2022-information/ch05-entropy]] (information-theory → unspecified)
