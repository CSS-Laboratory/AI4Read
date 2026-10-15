---
id: relative-entropy
type: concept
fields: [information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch22-channels]
generated_by: build_kg.py
---

# relative-entropy

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list
- [[polyanskiy-2025-information/ch22-channels]] (p. 401): $D(P_Z\|\mathcal N)$ measures non-Gaussianness and bounds the capacity gain

## Candidate bridges

- [same-math] relative entropy $D(p\|q)$ ↔ statistics: error exponent in hypothesis testing between $p$ and $q$ (pp. 8–9) — from [[cover-2006-elements/ch01-introduction]] (information-theory → other)
- [structural-analogy] Decision boundary D(P‖P₂)−D(P‖P₁)=const ↔ classification: a nearest-prototype rule with relative entropy as distance. — from [[cover-2006-elements/ch12-information-p2]] (information-theory → other)
- [same-math] Fisher information $J(\theta)$ ↔ relative entropy: Problem 7 asks the reader to show $\lim_{\theta'\to\theta}\frac{D(p_\theta\|p_{\theta'})}{(\theta-\theta')^2}=\frac1{\ln4}J(\theta)$. Fisher information is the local, second-order form of KL. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → other)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → information-theory)
- [same-math] $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$ ↔ information-theory: relative entropy and Gibbs' inequality. — from [[mackay-2003-information/ch08-dependent]] (information-theory → information-theory)
- [structural-analogy] choosing a Q with KL(Q‖P) (compact) vs KL(P‖Q) (G, spread out) ↔ information-theory: asymmetry of relative entropy. — from [[mackay-2003-information/ch33-variational]] (information-theory → information-theory)
- [structural-analogy] Entropic prior ↔ KL divergence: $S(\mathbf f,\mathbf m)$ resembles a relative-entropy term against a default $\mathbf m$. — from [[mackay-2003-information/ch46-deconvolution]] (information-theory → other)
- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] KL between exponential-family members = Bregman divergence of the log-normalizer ↔ information theory: coding-cost excess (relative entropy) — same quantity (p. 29). — from [[nielsen-2020-elementary/main-p2]] (information-theory → information-theory)
- [same-math] MI as D_KL(joint ‖ product of marginals) ↔ information-theory canon: relative entropy — the same integral (Eq. 6.47). — from [[stone-2022-information/ch06-mutual]] (information-theory → information-theory)
