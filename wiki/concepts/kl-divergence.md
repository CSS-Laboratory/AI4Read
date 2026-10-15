---
id: kl-divergence
type: concept
fields: [bayesian, information-theory, llm]
n_sources: 42
tiers: [reference, core, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, blei-2017-variational/main-p2, gelman-2013-bda3/appb-outline, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch13-modal, gelman-2013-philosophy/main, jaynes-2003-probability/ch13-decision, mackay-2003-information/ch06-stream, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch06-optimization-p3, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch08-gaussian-p2, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch13-sequential, murphy-2023-pml2/ch14-predictive, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch20-generative, murphy-2023-pml2/ch21-variational, murphy-2023-pml2/ch23-normalizing, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch25-diffusion, murphy-2023-pml2/ch26-generative, murphy-2023-pml2/ch28-latent-p2, murphy-2023-pml2/ch29-state-p3, murphy-2023-pml2/ch34-decision, murphy-2023-pml2/ch35-reinforcement, polyanskiy-2025-information/ch28-rate, prince-2023-udl/ch05-loss, prince-2023-udl/ch17-variational, prince-2023-udl/ch23-probability]
raw_ids: [KL divergence]
canon_spine: bayesian
generated_by: build_kg.py
---

# kl-divergence

## Canon spine entry

- **KL divergence** (bayesian): an asymmetric measure of how one distribution differs from another; the objective VI minimizes (grad)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 3, 6): asymmetric, nonnegative measure of proximity between densities; VI minimizes KL(q‖p), here with q first
- [[blei-2017-variational/main-p2]] (pp. 22, 26): the objective here is $\mathrm{KL}(q(z)\|p(z\mid x))$; EP uses the reverse direction
- [[gelman-2013-bda3/appb-outline]] (p. 587): here $\mathrm{KL}(\theta)=\mathrm E_f\log[f/p(\cdot|\theta)]$, a model–truth discrepancy; $\theta_0$ is its minimizer, assumed unique
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 88): when the truth is outside the family, $\theta_0$ is the value making the model closest to the truth in a sense involving KL divergence
- [[gelman-2013-bda3/ch07-evaluating]] (p. 167): the log predictive density is linked to Kullback–Leibler information; highest expected log predictive density corresponds to lowest KL (large-sample statement)
- [[gelman-2013-bda3/ch13-modal]] (p. 331): here $\mathrm{KL}(g\|p)=-\mathrm E_g\log(p/g)$, minimum 0, attained when $g\equiv p$
- [[gelman-2013-philosophy/main]] (p. 10): the divergence rate d(θ) governs where the misspecified posterior concentrates
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 179): extra uncertainty from using $q$ to describe $p$; $\sum p_i\log(p_i/q_i)$; asymmetric
- [[mcelreath-2020-rethinking/ch09-big]] (pp. 272, 274): used to prove maximum entropy results (Gaussian, binomial) and as the quantity minimized when the prior is not flat
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 43): closeness measure used in the max-entropy derivation
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 56): the f-divergence with $f(r)=r\log r$
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 107): the reference prior maximizes expected KL between posterior and prior
- [[murphy-2023-pml2/ch05-information-p1]] (p. 221): expected log ratio $\sum p\log(p/q)$; size of an update from $q$ to $p$; unique under the five desiderata
- [[murphy-2023-pml2/ch05-information-p2]] (pp. 238, 247): used here as the base quantity for MI, rate, and excess code length $D_{KL}(p\|q)$
- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 280): the distance used by NGD, approximated by $\frac12\delta^\top F\delta$
- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 291): $D_{\mathrm{KL}}(q\|p)\ge0$, zero iff $q=p$; the E step sets it to zero [as `KL divergence`]
- [[murphy-2023-pml2/ch06-optimization-p3]] (p. 322): used here as the regularizer of the coupling
- [[murphy-2023-pml2/ch07-inference]] (pp. 352, 356): discrepancy used by VI, $D_{\mathrm{KL}}(q\|p)$; the evaluation measure is $D_{\mathrm{KL}}(p\|q_t)$
- [[murphy-2023-pml2/ch08-gaussian-p2]] (p. 392): the projection objective; direction decides moment-matching vs mode-seeking
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 439): $D_{KL}(q\|p)$ is the loss; the gap between log p(x) and the ELBO
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 478): $D_{\mathbb{KL}}(q\|p)$ is zero-forcing, $D_{\mathbb{KL}}(p\|q)$ zero-avoiding
- [[murphy-2023-pml2/ch13-sequential]] (p. 570): defines the locally optimal proposal (p. 554) and bounds SMC quality
- [[murphy-2023-pml2/ch14-predictive]] (pp. 577, 583): regularizer to prior and evaluation metric between predictives
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 653–654, 664, 669): VI minimizes $D_{KL}(q\|p)$, EP $D_{KL}(p\|q)$; also used in distillation and PAC-Bayes
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 711): the objective $D_{\rm KL}(q(f)\|p(f|y))$ minimised in VFE
- [[murphy-2023-pml2/ch19-beyond]] (p. 756): forward KL on the predictive posterior is the meta-learning objective
- [[murphy-2023-pml2/ch20-generative]] (p. 783): KL divergence; equals $-\mathbb H(p)+\mathbb H_{ce}(p,q)$
- [[murphy-2023-pml2/ch21-variational]] (p. 796): divergence between distributions; appears as rate term, and the ELBO equals a negative joint KL up to constants
- [[murphy-2023-pml2/ch23-normalizing]] (p. 841): $D_{\mathbb{KL}}(p_s\|p_t)$ used to distill WaveNet into an IAF
- [[murphy-2023-pml2/ch24-energy]] (p. 851): MLE equals minimising $D_{KL}(p_D\|p_\theta)$ (p. 851) (reuse: KL divergence)
- [[murphy-2023-pml2/ch25-diffusion]] (p. 870): each $L_{t-1}$ is a KL between Gaussians, analytic
- [[murphy-2023-pml2/ch26-generative]] (p. 903): reused id; here infinite for non-overlapping supports
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 976): appears in the total-correlation formula
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1038): penalizes mismatch of $q(\mathbf z_t)$ and the predicted prior
- [[murphy-2023-pml2/ch34-decision]] (pp. 1128, 1141): appears in the expected posterior change (34.96) and the regret lower bound (34.73)
- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1182): policy proximity and the MERL objective (pp. 1161, 1179); [[variational-inference-elbo]] — PlaNet/Dreamer and the free energy principle (pp. 1170, 1181); [[conjugate-prior]] — Dirichlet for Thompson sampling (p. 1149); [[posterior-predictive-distribution]] — $\mathbb E_{b_t}[T]$ in the BAMDP (p. 1149); [[principle-of-indifference-maximum-entropy]] — the max-ent IRL model

### information-theory

- [[jaynes-2003-probability/ch13-decision]] (p. 403): Jaynes's I(q;p) in the weatherman pay scheme
- [[mackay-2003-information/ch06-stream]] (p. 123): mismatch between source and a symbol code's implicit distribution adds $D_{\mathrm{KL}}$ to the expected length
- [[polyanskiy-2025-information/ch28-rate]] (p. 493): used as $D(P_{\hat S|S}\|Q_{\hat S}|P_S)$, the random-coding exponent

### llm

- [[prince-2023-udl/ch05-loss]] (p. 71): measure of distance between two distributions, eq. 5.27 [new]
- [[prince-2023-udl/ch17-variational]] (p. 334): non-negative "distance" between distributions; zero when they match [new]
- [[prince-2023-udl/ch23-probability]] (p. 461): $\int p\log(p/q)$; $\ge0$, asymmetric (p. 461). Not the same as the canon's "KL penalty". [new]

## Candidate bridges

- [structural-analogy] Mean-field underestimating variance ↔ bayesian: asymmetry of KL divergence — the KL(q‖p) direction penalizes q-mass outside p's support — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → other)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$. — from [[jaynes-2003-probability/ch05-queer]] (information-theory → information-theory)
- [same-math] Integral in (8.51) ↔ information-theory: minus the KL divergence $D(p_{\theta_0}\|p_\theta)$; non-positivity is Gibbs' inequality. The unit does not name KL. — from [[jaynes-2003-probability/ch08-sufficiency]] (information-theory → information-theory)
- [same-math] Fisher information matrix (8.54) ↔ information-theory: local curvature of KL divergence / Fisher–Rao metric (up to the sign issue in Reading notes). — from [[jaynes-2003-probability/ch08-sufficiency]] (information-theory → information-theory)
- [same-math] Gibbs inequality (9.72) ↔ information-theory: non-negativity of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → information-theory)
- [same-math] ψ_B = 10n Σ f_k log₁₀(f_k/p_k) ↔ information-theory: n × KL divergence D(f‖p) in log₁₀ units, scaled by 10 — literally the same sum. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (information-theory → information-theory)
- [same-math] χ² as the second-order expansion (9.97) ↔ information-theory: the local quadratic (Fisher-information) form of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (information-theory → information-theory)
- [same-math] $H^c=-\int p\log(p/m)$ ↔ information-theory: negative KL divergence $-D(p\|m)$ — same functional form; this identification is ours, not stated in the unit. — from [[jaynes-2003-probability/ch12-ignorance]] (information-theory → information-theory)
- [structural-analogy] Entropic prior ↔ KL divergence: $S(\mathbf f,\mathbf m)$ resembles a relative-entropy term against a default $\mathbf m$. — from [[mackay-2003-information/ch46-deconvolution]] (information-theory → other)
- [structural-analogy] Shannon's "learning" as posterior far from prior ↔ KL divergence (canon link; not stated in this unit). — from [[mcgrayne-2011-theory/ch04-bayes]] (bayesian → unspecified)
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$. — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] Entropic OT regularization with $D_{\mathrm{KL}}(\pi\|\mu\otimes\nu)$ ↔ bayesian: KL divergence as a regularizer or objective in variational inference — both use KL to turn a hard problem into a smooth one. — from [[murphy-2023-pml2/ch06-optimization-p3]] (bayesian → bayesian)
- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → information-theory)
- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [structural-analogy] Marginal-bound proof of Thm 8.2 ↔ large deviations: the same inequality follows from a Chernoff bound with KL divergence (p. 159). — from [[polyanskiy-2025-information/ch09-entropy]] (information-theory → other)
- [structural-analogy] IS exponentiates an average KL divergence ↔ llm: perplexity exponentiates an average log-loss — both turn an information measure into an "effective number". — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [same-math] KL divergence inside $D_{JS}$ (eq. 15.9) ↔ llm: KL penalty — same divergence $D_{KL}$, here used between a distribution and a mixture — from [[prince-2023-udl/ch15-generative]] (llm → llm)
- [same-math] KL term in ELBO ↔ llm (KL penalty): the same KL divergence between two distributions, though used for a different purpose. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [structural-analogy] Coordinate-free capacity (difference of two entropies) ↔ KL divergence / mutual information as invariant under reparametrisation. — from [[shannon-1948-mathematical/main-p2]] (information-theory → unspecified)
- [same-math] $I(X,Y)=H(X)+H(Y)-H(X,Y)$ ↔ KL divergence: $I$ equals the KL divergence of $p(X,Y)$ from $p(X)p(Y)$ — this follows from (4.29–4.30) read as an expected log ratio, but the chapter does not name it. — from [[stone-2022-information/ch04-noisy]] (information-theory → other)
