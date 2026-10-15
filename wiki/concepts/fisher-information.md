---
id: fisher-information
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 16
n_works: 6
tiers: [reference, core, deep]
grounding: digests
sources: [cover-2006-elements/ch09-differential, cover-2006-elements/ch12-information-p3, cover-2006-elements/ch16-inequalities, gelman-2013-bda3/appb-outline, gelman-2013-bda3/ch04-asymptotics, jaynes-2003-probability/ch08-sufficiency, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch03-statistics-p1, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch08-f-p2, polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch36-strong-p1]
raw_ids: [Fisher information]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# fisher-information

## Canon spine entry

- **Fisher information** (information-theory): the curvature of log-likelihood; the local, second-order form of KL divergence (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch09-differential]] (p. 227): only mentioned: related to surface area of typical set
- [[cover-2006-elements/ch12-information-p3]] (p. 328): variance of the score, $J(\theta)=E_\theta[\partial_\theta\ln f]^2$; $J_n=nJ$ for i.i.d. data
- [[cover-2006-elements/ch16-inequalities]] (p. 494): here $J(X)=\int f(\partial_x\ln f)^2dx$ for a location family
- [[nielsen-2020-elementary/main-p1]] (pp. 18, 26): $E[\partial_il\,\partial_jl]$, equal to $-E[\partial_i\partial_jl]$ under regularity
- [[nielsen-2020-elementary/main-p2]] (pp. 36, 41): the metric used for Riemannian modelling; empirical FIM from scores in NES
- [[polyanskiy-2025-information/ch01-introduction]] (p. xix): gives classical variance bounds for estimation, re-examined
- [[polyanskiy-2025-information/ch03-divergence]] (pp. 38–39): $J_F(\theta)=\mathbb E_\theta[VV^\top]$, the local quadratic coefficient of $D$ [as `Fisher information`]
- [[polyanskiy-2025-information/ch08-f-p2]] (p. 141): $J_F(t)=4\int\mu\,\dot h_t^2$, with $J_F(0)=\int\mu\,\dot p_0^2/p_0$ in Theorem 7.22; coefficient of local quadratic behaviour
- [[polyanskiy-2025-information/ch15-universal]] (p. 251): Hessian of KL; enters via $\sqrt{\det J_F}$ and $\frac1{\log e}J_F$
- [[polyanskiy-2025-information/ch32-classical]] (p. 575; local $\chi^2$ expansion p. 576): curvature of log-likelihood; sets the $1/(nJ_F)$ variance floor for unbiased estimators (and the asymptotic minimax constant), with matrix form $J_F^{-1}$
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 645): $J_F(0)$ in the correlation lower bound

### bayesian

- [[gelman-2013-bda3/appb-outline]] (p. 589): $J(\theta_0)$, with $(nJ(\theta_0))^{-1}$ the limiting posterior variance; $-J$ is the mean of the second derivative of the log likelihood if the model is correct [new]
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 88): $J(\theta)$ from BDA (2.20); each likelihood term's second derivative has expected value about $-J(\theta_0)$, so the curvature is about $nJ$ [new]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 257): $I_{ij}$ defined in (8.54) as an average of second derivatives of $\log p$; a useful measure of the "resolving power" of an experiment [as `Fisher information`; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 41): equals $\nabla^2A=\mathrm{Cov}[\mathcal T]$ in this family (new)
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 76): covariance of the score; equals the expected NLL Hessian under regularity conditions [new]

## Instances that use it

- [[fim-binomial-gaussian-logistic]] — worked Fisher information calculations — from [[murphy-2023-pml2/ch03-statistics-p1]]
- [[multinomial-fisher-information]] — Example 2.6, (2.37)–(2.39) — from [[polyanskiy-2025-information/ch03-divergence]]
- [[location-family-fisher-information]] — Example 2.7, $J(p_0)$ — from [[polyanskiy-2025-information/ch03-divergence]]

## Candidate bridges

- [same-math] Fisher information $J(\theta)$ ↔ relative entropy: Problem 7 asks the reader to show $\lim_{\theta'\to\theta}\frac{D(p_\theta\|p_{\theta'})}{(\theta-\theta')^2}=\frac1{\ln4}J(\theta)$. Fisher information is the local, second-order form of KL. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → information-theory)
- [same-math] Cramér–Rao bound ↔ Statistics: variance lower bound by inverse Fisher information (p. 494). — from [[cover-2006-elements/ch16-inequalities]] (information-theory → other:statistics)
- [same-math] Fisher information $J(\theta)$ in Jeffreys' prior ↔ frequentist asymptotics: the same quantity as in (2.20). — from [[gelman-2013-bda3/ch02-single]] (bayesian → other:frequentist-asymptotics)
- [structural-analogy] $\partial^2\ln Z/\partial\lambda^2$ as variance ↔ Fisher information: curvature of log-likelihood — the same second-derivative-of-log-normalizer structure (relation not stated in the paper). — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [same-math] Denominator of (B.15) ↔ information-theory: Fisher information of $f(x|\theta)$ times $n$ (canon link; not stated in this unit). — from [[jaynes-2003-probability/appb-mathematical]] (bayesian → information-theory)
- [structural-analogy] $\sigma^{-2}=-L''(\hat f)$ in (4.70)–(4.71) ↔ Fisher information: curvature of log-likelihood sets the posterior width ($1/\sqrt N$ shrinkage), here with a flat prior. — from [[jaynes-2003-probability/ch04-elementary]] (bayesian → information-theory)
- [structural-analogy] Posterior becoming Gaussian with width about $1/\sqrt c$ ↔ information-theory: Fisher information as local curvature of log-likelihood — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → information-theory)
- [same-math] Fisher information matrix (8.54) ↔ information-theory: local curvature of KL divergence / Fisher–Rao metric (up to the sign issue in Reading notes). — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [same-math] χ² as the second-order expansion (9.97) ↔ information-theory: the local quadratic (Fisher-information) form of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → information-theory)
- [structural-analogy] Weight of evidence as sharpness of the A_p density ↔ information-theory: Fisher information as curvature of log-likelihood — narrower density means more information — from [[jaynes-2003-probability/ch18-p]] (bayesian → information-theory)
- [structural-analogy] curvature-based covariant step $\mathbf M=\mathbf A^{-1}$ ↔ information-theory: Fisher information as local curvature and Fisher–Rao metric — both turn curvature of a log-likelihood into a metric (not stated in this unit) — from [[mackay-2003-information/ch34-independent]] (information-theory → information-theory)
- [same-math] Fisher information F_η=Cov[T(x)] ↔ exponential families: variance of sufficient statistics is the curvature of log A(η) — same objects, as in (3.67)–(3.72). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → information-theory)
- [same-math] Fisher information of an exponential family $=\nabla^2F=\mathrm{Cov}[t]$ ↔ information-theory: exponential family / Gibbs distribution — $F$ is the log-normalizer — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] $I_f$ at nearby parameters $\approx\tfrac12g_{ij}\mathrm d\theta^i\mathrm d\theta^j$ ↔ information-theory: Fisher information as local second-order form of KL — eq. (116–117) — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] Fisher information as Hessian of $D$ ↔ statistics: curvature of log-likelihood — the chapter gives $J_F=-\mathbb E[\mathrm{Hess}\ln p_\theta]$ (p. 39). — from [[polyanskiy-2025-information/ch03-divergence]] (information-theory → other:statistics)
- [structural-analogy] Single-letterization of capacity ↔ Fisher information additivity for iid samples — both reduce an $n$-sample optimum or quantity to $n$ copies of a one-sample one. — from [[polyanskiy-2025-information/ch21-channel]] (information-theory → unspecified)
- [same-math] Local $\chi^2$/KL expansion with Fisher information ↔ information geometry: Fisher–Rao metric as local divergence curvature. — from [[polyanskiy-2025-information/ch32-classical]] (information-theory → information-theory)
