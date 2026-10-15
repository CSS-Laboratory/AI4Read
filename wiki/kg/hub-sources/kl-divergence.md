---
id: kl-divergence
type: concept
fields: [information-theory, bayesian, llm, control-theory, analytic-philosophy, decision-game-theory]
fields_strong: [information-theory, bayesian, llm, control-theory, analytic-philosophy, decision-game-theory]
n_sources: 93
n_works: 13
tiers: [reference, core, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, blei-2017-variational/main-p2, cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch06-gambling, cover-2006-elements/ch09-differential, cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch12-information-p2, cover-2006-elements/ch13-rate, cover-2006-elements/ch15-information, cover-2006-elements/ch16-inequalities, gelman-2013-bda3/appb-outline, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch13-modal, gelman-2013-philosophy/main, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch13-decision, mackay-2003-information/ch02-probability, mackay-2003-information/ch05-symbol, mackay-2003-information/ch06-stream, mackay-2003-information/ch08-dependent, mackay-2003-information/ch23-useful, mackay-2003-information/ch33-variational, mackay-2003-information/ch39-single, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch09-big, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch06-optimization-p3, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch08-gaussian-p2, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch13-sequential, murphy-2023-pml2/ch14-predictive, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch20-generative, murphy-2023-pml2/ch21-variational, murphy-2023-pml2/ch23-normalizing, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch25-diffusion, murphy-2023-pml2/ch26-generative, murphy-2023-pml2/ch28-latent-p2, murphy-2023-pml2/ch29-state-p3, murphy-2023-pml2/ch34-decision, murphy-2023-pml2/ch35-reinforcement, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch08-f-p1, polyanskiy-2025-information/ch08-f-p2, polyanskiy-2025-information/ch12-variable, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch16-neyman, polyanskiy-2025-information/ch17-information, polyanskiy-2025-information/ch18-hypothesis, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch22-channels, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch28-rate, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch35-entropic, polyanskiy-2025-information/ch36-strong-p1, polyanskiy-2025-information/ch36-strong-p2, prince-2023-udl/ch05-loss, prince-2023-udl/ch17-variational, prince-2023-udl/ch23-probability, stone-2022-information/appa-glossary, stone-2022-information/ch06-mutual, tishby-2000-bottleneck/main]
aliases: [relative-entropy, relative-entropy-kl, relative-entropy-kl-divergence]
raw_ids: [KL divergence]
canon_spine: [bayesian, information-theory]
generated_by: build_kg.py
---

# kl-divergence

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `relative-entropy` — 2 digest(s)
- `relative-entropy-kl` — 7 digest(s)
- `relative-entropy-kl-divergence` — 42 digest(s)

## Canon spine entry

- **KL divergence** (bayesian): an asymmetric measure of how one distribution differs from another; the objective VI minimizes (grad)

## Canon spine entry

- **relative entropy / KL divergence** (information-theory): the expected extra bits paid for coding data from p with a code built for q; non-negative and asymmetric (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 8): $D(p\|q)$, non-negative, zero iff $p=q$, not a metric [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch02-entropy]] (p. 49): $D(p\|q)=E_p\log\frac{p}{q}$; $\ge0$; not symmetric; no triangle inequality (p. 18). The author also lists "cross entropy" as another name for it (p. 49), unlike the canon's $H(p)+D(p\|q)$. [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch05-data-p1]] (pp. 89–90): $D(p\|q)$, the extra expected length when coding $p$ with a code for $q$ [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch05-data-p2]] (p. 117): cost of a wrong code, $H(p)+D(p\|q)$, only in the summary [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch06-gambling]] (p. 128): the loss from betting $\mathbf b$ instead of $\mathbf p$ is $D(\mathbf p\|\mathbf b)$ [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch09-differential]] (p. 231): $D(f\|g)=\int f\log(f/g)\ge0$ [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch11-maximum]] (p. 267): $D(g\|f^*)\ge0$ drives the proof of the theorem [alias `relative-entropy-kl`]
- [[cover-2006-elements/ch12-information-p1]] (pp. 285, 288): controls type-class probability $2^{-nD(P\|Q)}$ and the cost of a mismatched Huffman code [alias `relative-entropy-kl`]
- [[cover-2006-elements/ch12-information-p2]] (p. 297): D(P‖Q); here used as a "squared-distance-like" quantity on the simplex of types [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch13-rate]] (p. 365–366): distance minimized in Lemma 13.8.1 and the algorithm [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch15-information]] (p. 467): upper bound on doubling-rate loss from wrong beliefs [alias `relative-entropy-kl-divergence`]
- [[cover-2006-elements/ch16-inequalities]] (pp. 484, 489): $D(p\|q)\ge0$ with equality iff $p=q$; stronger than $\mathcal L_1$ distance [as `relative-entropy-KL-divergence`; alias `relative-entropy-kl-divergence`]
- [[mackay-2003-information/ch02-probability]] (p. 34): $D_{\rm KL}(P\|Q)$; not symmetric, so not strictly a distance [alias `relative-entropy-kl-divergence`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch05-symbol]] (p. 98): the excess of expected length over $H$ when a complete code with implicit $\mathbf q$ is used for true $\mathbf p$ [alias `relative-entropy-kl-divergence`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (p. 123): mismatch between source and a symbol code's implicit distribution adds $D_{\mathrm{KL}}$ to the expected length [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch08-dependent]] (pp. 140, 143): $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$; Gibbs' inequality gives non-negativity [alias `relative-entropy-kl-divergence`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch23-useful]] (p. 318): $D_{\rm KL}(\mathbf p\|\mathbf m)$ in the entropic distribution [alias `relative-entropy-kl`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch33-variational]] (p. 422): D_KL(Q‖P) = Σ Q ln(Q/P) in nats; ≥ 0, zero only if Q = P, asymmetric [alias `relative-entropy-kl-divergence`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch39-single]] (p. 475): each term of $G$ is also described as relative entropy between the empirical $(t,1-t)$ and $(y,1-y)$ [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`; work fields: information-theory, bayesian, llm]
- [[nielsen-2020-elementary/main-p1]] (p. 24): the $\alpha\to1$ member of the $\alpha$-divergences [alias `relative-entropy-kl-divergence`]
- [[nielsen-2020-elementary/main-p2]] (pp. 29–31): in this unit: $D_{\mathrm{KL}}[p_1:p_2]=E_{p_1}\log(p_1/p_2)$; equals a Bregman divergence on exponential (reverse order) and mixture (same order) families [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): $D(Q\|P)$, the dissimilarity between posterior $Q$ and prior $P$ in Shannon's case [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch03-divergence]] (pp. 21–22, 25): $D(P\|Q)=\mathbb E_Q[\frac{dP}{dQ}\log\frac{dP}{dQ}]$ if $P\ll Q$, else $\infty$; equals $\mathbb E_P\log\frac{dP}{dQ}$; asymmetric [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch04-mutual]] (pp. 42, 52): the base object; its DPI and chain rule are used to prove Thms 3.2 and 3.7 [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 70–72, 78): defined via densities, and equivalently as a sup over partitions or functions; convex, lower semicontinuous, not continuous in general [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch06-extremization]] (pp. 91–92, 96): jointly convex, not strictly; not a metric [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch08-f-p1]] (p. 116): the f-divergence with $f=x\log x$ [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch08-f-p2]] (p. 141–142, 150): $D$ is the case $f=x\log x$; locally $\frac{\log e}2J_F t^2$ [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch12-variable]] (p. 209): used to show $\mathbb El-H=D(P\|Q)-\log\sum2^{-l_a}\ge0$ [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch14-entropy]] (p. 236): used to bound term $A$ in the proof [alias `relative-entropy-kl`]
- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list [alias `relative-entropy`]
- [[polyanskiy-2025-information/ch16-neyman]] (p. 287): $D(P\|Q)$; here, the optimal Stein exponent [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch17-information]] (p. 299): D(Q‖P); here it is the cost of making a rare event typical under Q [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch18-hypothesis]] (p. 314, 317): D(P‖Q); appears as Stein/slope quantities and as the exponents themselves [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch19-error]] (p. 349): $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$ [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch22-channels]] (p. 401): $D(P_Z\|\mathcal N)$ measures non-Gaussianness and bounds the capacity gain [alias `relative-entropy`]
- [[polyanskiy-2025-information/ch23-capacity]] (p. 414): equals the cost-normalized rate: $C_{puc}=\sup D/\mathsf c$ [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch24-strong]] (p. 425): $D(\mathrm{Ber}(\delta)\|\mathrm{Ber}(1/2))=C$ for the BSC; Stein's exponent [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch25-channel]] (p. 447): $D(\mathbb P\|\mathbb Q)$ minimised over $\mathcal Q$ gives information flow [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch28-rate]] (p. 493): used as $D(P_{\hat S|S}\|Q_{\hat S}|P_S)$, the random-coding exponent
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 508): used to prove converses via a reference backward channel [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch32-classical]] (pp. 581–582): gives the intuition for MLE consistency ($-nD<0$) and the KL-projection view of the MLE [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch33-mutual]] (pp. 587, 592): used for the information-radius bound and tensorization [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 600): in the Gaussian model D = (n/2)‖θ−θ′‖² [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch35-entropic]] (p. 603): loss $D(P_\theta\|\hat P)$; asymmetric, and the reverse loss is typically infinite nonparametrically [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 631): $\eta_{KL}$ is the main coefficient [alias `relative-entropy-kl-divergence`]
- [[polyanskiy-2025-information/ch36-strong-p2]] (p. 650): the divergence whose contraction defines $\eta_{\rm KL}$ [alias `relative-entropy-kl-divergence`]
- [[stone-2022-information/appa-glossary]] (pp. 243, 246): measure of difference between two distributions [alias `relative-entropy-kl`]
- [[stone-2022-information/ch06-mutual]] (p. 151): D_KL(p‖q) is positive unless p = q, and usually asymmetric; MI is D_KL(joint ‖ product of marginals) [as `relative entropy / KL divergence`; alias `relative-entropy-kl-divergence`]
- [[tishby-2000-bottleneck/main]] (p. 12): emerges as the effective distortion $d(x,\tilde x)$ [alias `relative-entropy-kl-divergence`]

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 3, 6): asymmetric, nonnegative measure of proximity between densities; VI minimizes KL(q‖p), here with q first
- [[blei-2017-variational/main-p2]] (pp. 22, 26): the objective here is $\mathrm{KL}(q(z)\|p(z\mid x))$; EP uses the reverse direction
- [[gelman-2013-bda3/appb-outline]] (p. 587): here $\mathrm{KL}(\theta)=\mathrm E_f\log[f/p(\cdot|\theta)]$, a model–truth discrepancy; $\theta_0$ is its minimizer, assumed unique
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 88): when the truth is outside the family, $\theta_0$ is the value making the model closest to the truth in a sense involving KL divergence
- [[gelman-2013-bda3/ch07-evaluating]] (p. 167): the log predictive density is linked to Kullback–Leibler information; highest expected log predictive density corresponds to lowest KL (large-sample statement)
- [[gelman-2013-bda3/ch13-modal]] (p. 331): here $\mathrm{KL}(g\|p)=-\mathrm E_g\log(p/g)$, minimum 0, attained when $g\equiv p$
- [[gelman-2013-philosophy/main]] (p. 10): the divergence rate d(θ) governs where the misspecified posterior concentrates [work fields: bayesian, analytic-philosophy]
- [[jaynes-2003-probability/ch05-queer]] (p. 121): Jaynes's $H(f,p)$, the entropy of the observed distribution relative to the expected one, in the likelihood $e^{nH}$ (p. 121). Under the canon, $-H$ is KL. [alias `relative-entropy-kl-divergence`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 291): Gibbs inequality (9.72) is the non-negativity of KL divergence (canon link; not stated in this unit) [alias `relative-entropy-kl`; weak: not really used in this unit; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 298): ψ_B/(10n)=Σ f log₁₀(f/p); Jaynes calls −ψ_B/n an "entropy per symbol" relative to the expected distribution [alias `relative-entropy-kl`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch13-decision]] (p. 403): Jaynes's I(q;p) in the weatherman pay scheme [work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 179): extra uncertainty from using $q$ to describe $p$; $\sum p_i\log(p_i/q_i)$; asymmetric
- [[mcelreath-2020-rethinking/ch09-big]] (pp. 272, 274): used to prove maximum entropy results (Gaussian, binomial) and as the quantity minimized when the prior is not flat
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 43): closeness measure used in the max-entropy derivation
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 56): the f-divergence with $f(r)=r\log r$
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 107): the reference prior maximizes expected KL between posterior and prior
- [[murphy-2023-pml2/ch05-information-p1]] (p. 221): expected log ratio $\sum p\log(p/q)$; size of an update from $q$ to $p$; unique under the five desiderata [work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch05-information-p2]] (pp. 238, 247): used here as the base quantity for MI, rate, and excess code length $D_{KL}(p\|q)$ [work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 280): the distance used by NGD, approximated by $\frac12\delta^\top F\delta$
- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 291): $D_{\mathrm{KL}}(q\|p)\ge0$, zero iff $q=p$; the E step sets it to zero [as `KL divergence`]
- [[murphy-2023-pml2/ch06-optimization-p3]] (p. 322): used here as the regularizer of the coupling
- [[murphy-2023-pml2/ch07-inference]] (pp. 352, 356): discrepancy used by VI, $D_{\mathrm{KL}}(q\|p)$; the evaluation measure is $D_{\mathrm{KL}}(p\|q_t)$
- [[murphy-2023-pml2/ch08-gaussian-p2]] (p. 392): the projection objective; direction decides moment-matching vs mode-seeking [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 439): $D_{KL}(q\|p)$ is the loss; the gap between log p(x) and the ELBO
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 478): $D_{\mathbb{KL}}(q\|p)$ is zero-forcing, $D_{\mathbb{KL}}(p\|q)$ zero-avoiding
- [[murphy-2023-pml2/ch13-sequential]] (p. 570): defines the locally optimal proposal (p. 554) and bounds SMC quality
- [[murphy-2023-pml2/ch14-predictive]] (pp. 577, 583): regularizer to prior and evaluation metric between predictives
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 653–654, 664, 669): VI minimizes $D_{KL}(q\|p)$, EP $D_{KL}(p\|q)$; also used in distillation and PAC-Bayes [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 711): the objective $D_{\rm KL}(q(f)\|p(f|y))$ minimised in VFE
- [[murphy-2023-pml2/ch19-beyond]] (p. 756): forward KL on the predictive posterior is the meta-learning objective
- [[murphy-2023-pml2/ch20-generative]] (p. 783): KL divergence; equals $-\mathbb H(p)+\mathbb H_{ce}(p,q)$ [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch21-variational]] (p. 796): divergence between distributions; appears as rate term, and the ELBO equals a negative joint KL up to constants [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch23-normalizing]] (p. 841): $D_{\mathbb{KL}}(p_s\|p_t)$ used to distill WaveNet into an IAF [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch24-energy]] (p. 851): MLE equals minimising $D_{KL}(p_D\|p_\theta)$ (p. 851) (reuse: KL divergence) [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch25-diffusion]] (p. 870): each $L_{t-1}$ is a KL between Gaussians, analytic [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch26-generative]] (p. 903): reused id; here infinite for non-overlapping supports [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 976): appears in the total-correlation formula
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1038): penalizes mismatch of $q(\mathbf z_t)$ and the predicted prior [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch34-decision]] (pp. 1128, 1141): appears in the expected posterior change (34.96) and the regret lower bound (34.73) [work fields: bayesian, decision-game-theory]
- [[murphy-2023-pml2/ch35-reinforcement]] (pp. 1161, 1179): policy proximity and the MERL objective [work fields: bayesian, control-theory]

### llm

- [[prince-2023-udl/ch05-loss]] (p. 71): measure of distance between two distributions, eq. 5.27 [new]
- [[prince-2023-udl/ch17-variational]] (p. 334): non-negative "distance" between distributions; zero when they match [new]
- [[prince-2023-udl/ch23-probability]] (p. 461): $\int p\log(p/q)$; $\ge0$, asymmetric (p. 461). Not the same as the canon's "KL penalty". [new]

## Candidate bridges

- [structural-analogy] Mean-field underestimating variance ↔ bayesian: asymmetry of KL divergence — the KL(q‖p) direction penalizes q-mass outside p's support — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [same-math] relative entropy $D(p\|q)$ ↔ statistics: error exponent in hypothesis testing between $p$ and $q$ (pp. 8–9) — from [[cover-2006-elements/ch01-introduction]] (information-theory → other:statistics)
- [structural-analogy] Decision boundary D(P‖P₂)−D(P‖P₁)=const ↔ classification: a nearest-prototype rule with relative entropy as distance. — from [[cover-2006-elements/ch12-information-p2]] (information-theory → llm)
- [same-math] Fisher information $J(\theta)$ ↔ relative entropy: Problem 7 asks the reader to show $\lim_{\theta'\to\theta}\frac{D(p_\theta\|p_{\theta'})}{(\theta-\theta')^2}=\frac1{\ln4}J(\theta)$. Fisher information is the local, second-order form of KL. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → information-theory)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [same-math] Integral in (8.51) ↔ information-theory: minus the KL divergence $D(p_{\theta_0}\|p_\theta)$; non-positivity is Gibbs' inequality. The unit does not name KL. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [same-math] Fisher information matrix (8.54) ↔ information-theory: local curvature of KL divergence / Fisher–Rao metric (up to the sign issue in Reading notes). — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [same-math] Gibbs inequality (9.72) ↔ information-theory: non-negativity of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (bayesian → information-theory)
- [same-math] ψ_B = 10n Σ f_k log₁₀(f_k/p_k) ↔ information-theory: n × KL divergence D(f‖p) in log₁₀ units, scaled by 10 — literally the same sum. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → information-theory)
- [same-math] χ² as the second-order expansion (9.97) ↔ information-theory: the local quadratic (Fisher-information) form of KL divergence. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → information-theory)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → information-theory)
- [same-math] $H^c=-\int p\log(p/m)$ ↔ information-theory: negative KL divergence $-D(p\|m)$ — same functional form; this identification is ours, not stated in the unit. — from [[jaynes-2003-probability/ch12-ignorance]] (bayesian → information-theory)
- [same-math] $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$ ↔ information-theory: relative entropy and Gibbs' inequality. — from [[mackay-2003-information/ch08-dependent]] (information-theory → information-theory)
- [structural-analogy] choosing a Q with KL(Q‖P) (compact) vs KL(P‖Q) (G, spread out) ↔ information-theory: asymmetry of relative entropy. — from [[mackay-2003-information/ch33-variational]] (information-theory → information-theory)
- [structural-analogy] Entropic prior ↔ KL divergence: $S(\mathbf f,\mathbf m)$ resembles a relative-entropy term against a default $\mathbf m$. — from [[mackay-2003-information/ch46-deconvolution]] (information-theory → information-theory)
- [structural-analogy] Shannon's "learning" as posterior far from prior ↔ KL divergence (canon link; not stated in this unit). — from [[mcgrayne-2011-theory/ch04-bayes]] (bayesian → unspecified)
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$. — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] Entropic OT regularization with $D_{\mathrm{KL}}(\pi\|\mu\otimes\nu)$ ↔ bayesian: KL divergence as a regularizer or objective in variational inference — both use KL to turn a hard problem into a smooth one. — from [[murphy-2023-pml2/ch06-optimization-p3]] (bayesian → bayesian)
- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → information-theory)
- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] KL between exponential-family members = Bregman divergence of the log-normalizer ↔ information theory: coding-cost excess (relative entropy) — same quantity (p. 29). — from [[nielsen-2020-elementary/main-p2]] (information-theory → information-theory)
- [structural-analogy] Marginal-bound proof of Thm 8.2 ↔ large deviations: the same inequality follows from a Chernoff bound with KL divergence (p. 159). — from [[polyanskiy-2025-information/ch09-entropy]] (information-theory → information-theory)
- [structural-analogy] IS exponentiates an average KL divergence ↔ llm: perplexity exponentiates an average log-loss — both turn an information measure into an "effective number". — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [same-math] KL divergence inside $D_{JS}$ (eq. 15.9) ↔ llm: KL penalty — same divergence $D_{KL}$, here used between a distribution and a mixture — from [[prince-2023-udl/ch15-generative]] (llm → llm)
- [same-math] KL term in ELBO ↔ llm (KL penalty): the same KL divergence between two distributions, though used for a different purpose. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] KL divergence ↔ language models: cross-entropy equals entropy plus KL, so minimizing log-loss minimizes KL to the data distribution (canon link; not stated in this unit). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [structural-analogy] Coordinate-free capacity (difference of two entropies) ↔ KL divergence / mutual information as invariant under reparametrisation. — from [[shannon-1948-mathematical/main-p2]] (information-theory → unspecified)
- [same-math] $I(X,Y)=H(X)+H(Y)-H(X,Y)$ ↔ KL divergence: $I$ equals the KL divergence of $p(X,Y)$ from $p(X)p(Y)$ — this follows from (4.29–4.30) read as an expected log ratio, but the chapter does not name it. — from [[stone-2022-information/ch04-noisy]] (information-theory → information-theory)
- [same-math] MI as D_KL(joint ‖ product of marginals) ↔ information-theory canon: relative entropy — the same integral (Eq. 6.47). — from [[stone-2022-information/ch06-mutual]] (information-theory → information-theory)
