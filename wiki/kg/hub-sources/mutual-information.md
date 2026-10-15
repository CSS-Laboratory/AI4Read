---
id: mutual-information
type: concept
fields: [information-theory, bayesian, llm, political-science]
fields_strong: [information-theory, bayesian, llm, political-science]
n_sources: 58
n_works: 10
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch04-entropy, cover-2006-elements/ch06-gambling, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch09-differential, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch14-network-p3, cover-2006-elements/ch15-information, cover-2006-elements/ch16-inequalities, gibson-2019-efficiency/main, grimmer-2022-textasdata/ch11-discriminating, mackay-2003-information/ch08-dependent, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch11-error, mackay-2003-information/ch44-supervised, murphy-2023-pml2/ch05-information-p2, pierce-1980-introduction/ch08-noisy, polyanskiy-2025-information/ch02-entropy, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch08-f-p1, polyanskiy-2025-information/ch13-fixed, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch18-hypothesis, polyanskiy-2025-information/ch20-random, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch27-rate, polyanskiy-2025-information/ch28-rate, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch30-metric, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch35-entropic, polyanskiy-2025-information/ch36-strong-p1, polyanskiy-2025-information/ch36-strong-p2, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appf-rules, stone-2022-information/ch04-noisy, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel, stone-2022-information/ch08-rate, stone-2022-information/ch09-transfer, stone-2022-information/ch11-information, tishby-2000-bottleneck/main]
aliases: [mutual-information-ixy]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# mutual-information

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `mutual-information-ixy` — 13 digest(s)

## Canon spine entry

- **mutual information I(X;Y)** (information-theory): how much knowing Y reduces uncertainty about X; symmetric, and zero iff X and Y are independent (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): reduction in uncertainty, $H(X)-H(X|Y)$; symmetric, non-negative [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[cover-2006-elements/ch02-entropy]] (pp. 18–20, 27): $D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric; $\ge0$, $=0$ iff independent
- [[cover-2006-elements/ch04-entropy]] (p. 70): used to show the bound gap equals $I(X_1;Y_n|Y_{n-1},\dots,Y_1)$
- [[cover-2006-elements/ch06-gambling]] (p. 131): in a horse race equals the doubling-rate gain from side information
- [[cover-2006-elements/ch08-channel-p1]] (pp. 184, 191): $I(X;Y)=H(Y)-H(Y|X)$, concave in $p(x)$, the quantity maximized
- [[cover-2006-elements/ch08-channel-p2]] (p. 205): $I(X;Y)$, additive bound over uses of a DMC
- [[cover-2006-elements/ch09-differential]] (p. 231): $I(X;Y)=D(f(x,y)\|f(x)f(y))$; limit of quantized versions
- [[cover-2006-elements/ch12-information-p1]] (p. 296): appears as the exponent $2^{-nI(X;Y)}$ in Example 12.5.3
- [[cover-2006-elements/ch13-rate]] (p. 350): objective of the minimization; convex in $p(\hat x|x)$
- [[cover-2006-elements/ch14-network-p1]] (p. 387): conditional mutual information sets the joint-typicality probability
- [[cover-2006-elements/ch14-network-p2]] (p. 389–390): conditional mutual informations bound the rates
- [[cover-2006-elements/ch14-network-p3]] (p. 422): rate constraints $I(U;Y_2)$, $I(X;Y_1|U)$, etc.
- [[cover-2006-elements/ch15-information]] (p. 468): upper bound on doubling-rate gain from side information
- [[cover-2006-elements/ch16-inequalities]] (p. 484): $D(p(x,y)\|p(x)p(y))\ge0$, zero iff independent [as `mutual-information-I(X;Y)`; alias `mutual-information-ixy`]
- [[gibson-2019-efficiency/main]] (p. 4): $I[X:C]=H[X]-H[X\mid C]$, symmetric and non-negative
- [[mackay-2003-information/ch08-dependent]] (pp. 139, 143): $H(X)-H(X|Y)$; symmetric, $\ge0$, zero iff independent [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 149): I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X); input-to-output information, depends on P_X [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch10-noisy]] (p. 163): $I(X;Y)$; sets the chance $2^{-NI}$ that independent sequences look jointly typical [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch11-error]] (p. 180): the one information measure with a well-behaved continuous limit, eq. (11.24) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch44-supervised]] (p. 533): proposed classifier score $I(T;Y)$ [as `mutual information I(X;Y)`; alias `mutual-information-ixy`; work fields: information-theory, bayesian, llm]
- [[pierce-1980-introduction/ch08-noisy]] (p. 155; canon link, not stated in this unit): Pierce does not use this name. His rate $R$ in 8.8–8.10 is the same quantity [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 17, 19): within these pages appears only in the non-Shannon inequality and Example 1.5, with its definition deferred
- [[polyanskiy-2025-information/ch04-mutual]] (p. 42, 44): here defined as D(P_{X,Y}‖P_X P_Y), the general definition; equals H(X)−H(X|Y) for discrete X when H(X|Y)<∞ [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 67–70, 83): here $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$, with inf forms over $Q_Y$, $Q_XQ_Y$ and sup forms over kernels and partitions
- [[polyanskiy-2025-information/ch06-extremization]] (p. 92): concave in $P_X$, convex in $P_{Y|X}$
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 106): I(X;Y), here optimised over high-dimensional inputs and channels
- [[polyanskiy-2025-information/ch08-f-p1]] (p. 135): ordinary case $f=x\log x$ of $I_f$; has subadditivity (7.47)
- [[polyanskiy-2025-information/ch13-fixed]] (pp. 225, 227): $H(T)-H(T|S)=H(S)-H(S|T)=I(S;T)$ is why the sloped boundary of the Slepian-Wolf region has slope $-1$; $I(Y;U)$ is the helper's rate
- [[polyanskiy-2025-information/ch14-entropy]] (pp. 240–241): semicontinuity and σ-algebra continuity used in Sinai's proof
- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list
- [[polyanskiy-2025-information/ch18-hypothesis]] (p. 327): I(W;Y^n) controls the communication-constrained exponent
- [[polyanskiy-2025-information/ch20-random]] (p. 351): $I(X;Y)=\mathbb E[i(X;Y)]$
- [[polyanskiy-2025-information/ch21-channel]] (p. 376): the quantity maximized to get capacity; its information density is a sum of iid terms in the proof [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch24-strong]] (p. 426): $I(X;Y)\le C$ bounds the mean of the information density
- [[polyanskiy-2025-information/ch25-channel]] (p. 444): $I(\tilde\pi,P_{Y|X})$ is the drift of the log-posterior
- [[polyanskiy-2025-information/ch27-rate]] (p. 486, 488): the quantity minimized in $\phi_X(D)$; convex in $P_{Y|X}$, super-additive for independent inputs [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch28-rate]] (p. 490): $I(S;\hat S)$ minimised over test channels with $\mathbb E d\le D$ gives $\phi_S(D)$
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 508): the quantity minimized in $R(D)$; rewritten as $D(P_{S|\hat S}\|P_S|P_{\hat S})$
- [[polyanskiy-2025-information/ch30-metric]] (pp. 532, 542): used in $|\mathbb E Z_T|\le\sqrt{2I(Z^n;T)}$ and in rate–distortion
- [[polyanskiy-2025-information/ch33-mutual]] (p. 585): information the data give about $\theta$; capped by channel capacity [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 599): bounded via the chain rule and the Jensen–Shannon form [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[polyanskiy-2025-information/ch35-entropic]] (p. 605): the Bayes KL risk is the conditional mutual information $I(\theta;X_{n+1}|X^n)$
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 626): $I(U;Y)$ in all SDPI statements
- [[polyanskiy-2025-information/ch36-strong-p2]] (p. 650): conditional MI bounded by percolation, $I(X_{S_1};X_{S_2}|Y)$
- [[shannon-1948-mathematical/main-p1]] (p. 22): not named here; the rate $R=H(x)-H_y(x)=H(y)-H_x(y)=H(x)+H(y)-H(x,y)$ is, in a sense, the bits per second common to input and output [weak: not really used in this unit]
- [[shannon-1948-mathematical/main-p2]] (pp. 42, 54): appears as the integrand $\log\frac{P(x,y)}{P(x)P(y)}$ defining $R$; Appendix 7 defines it as a supremum over partitions
- [[stone-2022-information/appa-glossary]] (p. 244): symmetric reduction in uncertainty
- [[stone-2022-information/appb-mathematical]] (p. 249): $I(X,Y)$, the average bits each $Y$ value gives about $X$, and vice versa
- [[stone-2022-information/appf-rules]] (p. 266): H.13–H.18 [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[stone-2022-information/ch04-noisy]] (p. 79, p. 90): average reduction in uncertainty about one variable from knowing the other; $H(X)+H(Y)-H(X,Y)$
- [[stone-2022-information/ch06-mutual]] (pp. 135, 148): here I(X,Y) = H(X)+H(Y)−H(X,Y) = H(X)−H(X|Y) = H(Y)−H(Y|X); symmetric, zero if X, Y are independent [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[stone-2022-information/ch07-channel]] (pp. 153, 165): $H(Y)-H(Y|X)$; for Gaussians, $\tfrac12\log\frac1{1-\rho^2}$ [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[stone-2022-information/ch08-rate]] (p. 180): the quantity minimised in $R^I(D)$ [as `mutual information I(X;Y)`; alias `mutual-information-ixy`]
- [[stone-2022-information/ch09-transfer]] (pp. 198, 199): $I(y_t;y_{t-1})=H(y_t)-H(y_t|y_{t-1})$; symmetric, unlike transfer entropy
- [[stone-2022-information/ch11-information]] (p. 230): information the neuron's output carries about its input, bounded by output entropy
- [[tishby-2000-bottleneck/main]] (pp. 4, 9): $I(X;\tilde X)$ is the rate bound; $I(\tilde X;Y)$ is the relevant information

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (p. 238): KL divergence between joint and product of marginals; reduction in uncertainty about one variable from observing the other [new; work fields: bayesian, information-theory]

### political-science

- [[grimmer-2022-textasdata/ch11-discriminating]] (pp. 190–191): $H(k)-H(k|j)$: how much a word's presence reduces category uncertainty; unsigned [new]

## Candidate bridges

- [same-math] Doubling rate with side information, $\Delta W=I(X;Y)$ ↔ Kelly criterion: side information raises growth by its mutual information — same quantity. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] cut-set bound ↔ graph theory: max-flow–min-cut — the text itself offers this reading, with mutual information in place of edge capacity. — from [[cover-2006-elements/ch14-network-p4]] (information-theory → other:graph-theory)
- [same-math] Surprisal, entropy, conditional entropy, mutual information in Box 2 ↔ information theory: the standard definitions (I)–(V). — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [structural-analogy] Prior making data irrelevant ($AA=A$) ↔ information-theory: conditional mutual information is zero when the prior already contains the information. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [metaphor] A good measurement carrying no information once others are fixed ↔ information-theory: conditional independence or zero mutual information (p. 600) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [same-math] Mutual information I(X;Y) = H(X) − H(X|Y) ↔ bayesian: expected reduction in uncertainty about an unknown (the input) after an observation (the output) — the same quantity, computed from the Bayes posterior P(x|y). — from [[mackay-2003-information/ch09-communication]] (information-theory → bayesian)
- [structural-analogy] Value of prospecting data ↔ information-theory: mutual information — both measure what a signal is worth, though here in utility units rather than bits. — from [[mackay-2003-information/ch36-decision]] (information-theory → information-theory)
- [same-math] Reference-prior objective (mutual information $\mathbb I(\theta,\mathcal D)$) ↔ information theory: expected KL between posterior and prior (p. 107). — from [[murphy-2023-pml2/ch03-statistics-p2]] (bayesian → information-theory)
- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → information-theory)
- [same-math] BALD's $\alpha(x)=\mathbb I(w;y|\mathcal D,x)$ ↔ information theory: mutual information, with the KL form (34.96). — from [[murphy-2023-pml2/ch34-decision]] (bayesian → information-theory)
- [same-math] equivocation and rate (8.6–8.10) ↔ information-theory: conditional entropy and mutual information identities — same quantities under other names. — from [[pierce-1980-introduction/ch08-noisy]] (information-theory → information-theory)
- [structural-analogy] one-molecule engine's bit-for-work trade ↔ Kelly criterion: side information has a measurable, bounded value (it raises growth by its mutual information). — from [[pierce-1980-introduction/ch10-information]] (information-theory → information-theory)
- [structural-analogy] prediction ↔ universal compression: optimal online prediction linked to maximal mutual information (p. xx) — from [[polyanskiy-2025-information/ch01-introduction]] (information-theory → other:universal-compression)
- [structural-analogy] directed information $\vec I(X^n;Y^n)$ ↔ information-theory: transfer entropy — both are sums of conditional mutual informations measuring causally directed flow, though the conditioning sets differ. — from [[polyanskiy-2025-information/ch25-channel]] (information-theory → information-theory)
- [same-math] Soft-covering bound via Rényi mutual information ↔ information-theory: Rényi divergence bounds of Chapter 7 (Prop. 7.17 is the $\lambda=2$ case, p. 504). — from [[polyanskiy-2025-information/ch28-rate]] (information-theory → information-theory)
- [same-math] Gaussian $R(D)=\frac12\log\sigma^2/D$ ↔ Shannon–Hartley formula $C=\frac12\log(1+\mathrm{SNR})$ — both are a Gaussian mutual information with a noise-ratio inside the log. — from [[polyanskiy-2025-information/ch29-evaluating]] (information-theory → unspecified)
- [structural-analogy] Data-processing proof of estimation bounds ↔ Fano/converse arguments in channel coding: both bound error through a divergence or mutual-information inequality. — from [[polyanskiy-2025-information/ch32-classical]] (information-theory → information-theory)
- [structural-analogy] Le Cam / Assouad / Fano as reduction to testing ↔ information theory: converse proofs of channel coding via Fano — in both, decoding error is bounded by mutual information (canon link; not stated in this unit). — from [[polyanskiy-2025-information/ch34-lower]] (information-theory → information-theory)
- [same-math] Hamblin's $C(x,y)=\log_2\frac{P(xy)}{P(x)P(y)}$ ↔ information theory: pointwise mutual information. Popper says it is related to the fundamental idea of information theory (p. 421); the formula itself is the standard log-ratio. — from [[popper-1959-logic/appix-untitled]] (analytic-philosophy → information-theory)
- [same-math] $R_1=\min$ of mutual information at fixed average distortion ↔ rate–distortion function $R(D)$: same optimisation; the exponential solution $P_y(x)=B(x)e^{-\lambda\rho}$ is its first-order condition. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [structural-analogy] Coordinate-free capacity (difference of two entropies) ↔ KL divergence / mutual information as invariant under reparametrisation. — from [[shannon-1948-mathematical/main-p2]] (information-theory → unspecified)
- [structural-analogy] Conditioning on $y_{\text{past}}$ ↔ information theory: chain rule / conditional mutual information — only information not already supplied by $y$'s own history counts. — from [[stone-2022-information/ch09-transfer]] (information-theory → information-theory)
