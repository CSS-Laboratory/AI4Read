---
id: relative-entropy-kl-divergence
type: concept
fields: [information-theory]
n_sources: 42
tiers: [reference, core, deep]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch06-gambling, cover-2006-elements/ch09-differential, cover-2006-elements/ch12-information-p2, cover-2006-elements/ch13-rate, cover-2006-elements/ch15-information, cover-2006-elements/ch16-inequalities, jaynes-2003-probability/ch05-queer, mackay-2003-information/ch02-probability, mackay-2003-information/ch05-symbol, mackay-2003-information/ch08-dependent, mackay-2003-information/ch33-variational, mackay-2003-information/ch39-single, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch08-f-p1, polyanskiy-2025-information/ch08-f-p2, polyanskiy-2025-information/ch12-variable, polyanskiy-2025-information/ch16-neyman, polyanskiy-2025-information/ch17-information, polyanskiy-2025-information/ch18-hypothesis, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch35-entropic, polyanskiy-2025-information/ch36-strong-p1, polyanskiy-2025-information/ch36-strong-p2, stone-2022-information/ch06-mutual, tishby-2000-bottleneck/main]
raw_ids: [relative entropy / KL divergence, relative-entropy-KL-divergence]
canon_spine: information-theory
generated_by: build_kg.py
---

# relative-entropy-kl-divergence

## Canon spine entry

- **relative entropy / KL divergence** (information-theory): the expected extra bits paid for coding data from p with a code built for q; non-negative and asymmetric (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 8): $D(p\|q)$, non-negative, zero iff $p=q$, not a metric [as `relative entropy / KL divergence`]
- [[cover-2006-elements/ch02-entropy]] (p. 49): $D(p\|q)=E_p\log\frac{p}{q}$; $\ge0$; not symmetric; no triangle inequality (p. 18). The author also lists "cross entropy" as another name for it (p. 49), unlike the canon's $H(p)+D(p\|q)$.
- [[cover-2006-elements/ch05-data-p1]] (pp. 89–90): $D(p\|q)$, the extra expected length when coding $p$ with a code for $q$
- [[cover-2006-elements/ch05-data-p2]] (p. 117): cost of a wrong code, $H(p)+D(p\|q)$, only in the summary
- [[cover-2006-elements/ch06-gambling]] (p. 128): the loss from betting $\mathbf b$ instead of $\mathbf p$ is $D(\mathbf p\|\mathbf b)$
- [[cover-2006-elements/ch09-differential]] (p. 231): $D(f\|g)=\int f\log(f/g)\ge0$
- [[cover-2006-elements/ch12-information-p2]] (p. 297): D(P‖Q); here used as a "squared-distance-like" quantity on the simplex of types
- [[cover-2006-elements/ch13-rate]] (p. 365–366): distance minimized in Lemma 13.8.1 and the algorithm
- [[cover-2006-elements/ch15-information]] (p. 467): upper bound on doubling-rate loss from wrong beliefs
- [[cover-2006-elements/ch16-inequalities]] (pp. 484, 489): $D(p\|q)\ge0$ with equality iff $p=q$; stronger than $\mathcal L_1$ distance [as `relative-entropy-KL-divergence`]
- [[jaynes-2003-probability/ch05-queer]] (p. 121): Jaynes's $H(f,p)$, the entropy of the observed distribution relative to the expected one, in the likelihood $e^{nH}$ (p. 121). Under the canon, $-H$ is KL.
- [[mackay-2003-information/ch02-probability]] (p. 34): $D_{\rm KL}(P\|Q)$; not symmetric, so not strictly a distance
- [[mackay-2003-information/ch05-symbol]] (p. 98): the excess of expected length over $H$ when a complete code with implicit $\mathbf q$ is used for true $\mathbf p$
- [[mackay-2003-information/ch08-dependent]] (pp. 140, 143): $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$; Gibbs' inequality gives non-negativity
- [[mackay-2003-information/ch33-variational]] (p. 422): D_KL(Q‖P) = Σ Q ln(Q/P) in nats; ≥ 0, zero only if Q = P, asymmetric
- [[mackay-2003-information/ch39-single]] (p. 475): each term of $G$ is also described as relative entropy between the empirical $(t,1-t)$ and $(y,1-y)$ [as `relative entropy / KL divergence`]
- [[nielsen-2020-elementary/main-p1]] (p. 24): the $\alpha\to1$ member of the $\alpha$-divergences
- [[nielsen-2020-elementary/main-p2]] (pp. 29–31): in this unit: $D_{\mathrm{KL}}[p_1:p_2]=E_{p_1}\log(p_1/p_2)$; equals a Bregman divergence on exponential (reverse order) and mixture (same order) families
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): $D(Q\|P)$, the dissimilarity between posterior $Q$ and prior $P$ in Shannon's case
- [[polyanskiy-2025-information/ch03-divergence]] (pp. 21–22, 25): $D(P\|Q)=\mathbb E_Q[\frac{dP}{dQ}\log\frac{dP}{dQ}]$ if $P\ll Q$, else $\infty$; equals $\mathbb E_P\log\frac{dP}{dQ}$; asymmetric [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch04-mutual]] (pp. 42, 52): the base object; its DPI and chain rule are used to prove Thms 3.2 and 3.7 [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 70–72, 78): defined via densities, and equivalently as a sup over partitions or functions; convex, lower semicontinuous, not continuous in general
- [[polyanskiy-2025-information/ch06-extremization]] (pp. 91–92, 96): jointly convex, not strictly; not a metric
- [[polyanskiy-2025-information/ch08-f-p1]] (p. 116): the f-divergence with $f=x\log x$
- [[polyanskiy-2025-information/ch08-f-p2]] (p. 141–142, 150): $D$ is the case $f=x\log x$; locally $\frac{\log e}2J_F t^2$
- [[polyanskiy-2025-information/ch12-variable]] (p. 209): used to show $\mathbb El-H=D(P\|Q)-\log\sum2^{-l_a}\ge0$ [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch16-neyman]] (p. 287): $D(P\|Q)$; here, the optimal Stein exponent [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch17-information]] (p. 299): D(Q‖P); here it is the cost of making a rare event typical under Q
- [[polyanskiy-2025-information/ch18-hypothesis]] (p. 314, 317): D(P‖Q); appears as Stein/slope quantities and as the exponents themselves
- [[polyanskiy-2025-information/ch19-error]] (p. 349): $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$
- [[polyanskiy-2025-information/ch23-capacity]] (p. 414): equals the cost-normalized rate: $C_{puc}=\sup D/\mathsf c$
- [[polyanskiy-2025-information/ch24-strong]] (p. 425): $D(\mathrm{Ber}(\delta)\|\mathrm{Ber}(1/2))=C$ for the BSC; Stein's exponent
- [[polyanskiy-2025-information/ch25-channel]] (p. 447): $D(\mathbb P\|\mathbb Q)$ minimised over $\mathcal Q$ gives information flow
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 508): used to prove converses via a reference backward channel
- [[polyanskiy-2025-information/ch32-classical]] (pp. 581–582): gives the intuition for MLE consistency ($-nD<0$) and the KL-projection view of the MLE
- [[polyanskiy-2025-information/ch33-mutual]] (pp. 587, 592): used for the information-radius bound and tensorization [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 600): in the Gaussian model D = (n/2)‖θ−θ′‖² [as `relative entropy / KL divergence`]
- [[polyanskiy-2025-information/ch35-entropic]] (p. 603): loss $D(P_\theta\|\hat P)$; asymmetric, and the reverse loss is typically infinite nonparametrically
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 631): $\eta_{KL}$ is the main coefficient
- [[polyanskiy-2025-information/ch36-strong-p2]] (p. 650): the divergence whose contraction defines $\eta_{\rm KL}$
- [[stone-2022-information/ch06-mutual]] (p. 151): D_KL(p‖q) is positive unless p = q, and usually asymmetric; MI is D_KL(joint ‖ product of marginals) [as `relative entropy / KL divergence`]
- [[tishby-2000-bottleneck/main]] (p. 12): emerges as the effective distortion $d(x,\tilde x)$

## Candidate bridges

- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
