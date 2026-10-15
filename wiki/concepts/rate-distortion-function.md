---
id: rate-distortion-function
type: concept
fields: [information-theory]
n_sources: 21
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p4, gibson-2019-efficiency/main, mackay-2003-information/ch10-noisy, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch11-lossless, polyanskiy-2025-information/ch26-rate, polyanskiy-2025-information/ch27-rate, polyanskiy-2025-information/ch28-rate, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch30-metric, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch36-strong-p2, shannon-1948-mathematical/main-p2, stone-2022-information/appa-glossary, stone-2022-information/appf-rules, stone-2022-information/ch04-noisy, stone-2022-information/ch08-rate, tishby-2000-bottleneck/main]
raw_ids: [rate–distortion function]
canon_spine: information-theory
generated_by: build_kg.py
---

# rate-distortion-function

## Canon spine entry

- **rate–distortion function** (information-theory): the minimum bits needed to describe a source within a given average distortion; the theory of lossy compression (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 9): rates needed to describe the source up to distortion $D$ [as `rate–distortion function`]
- [[cover-2006-elements/ch13-rate]] (p. 341–342): $R(D)$: minimum rate of a code with expected distortion at most $D$; equals $\min I(X;\hat X)$ for i.i.d. sources
- [[cover-2006-elements/ch14-network-p4]] (p. 438): minimum bits to describe a source within average distortion D. Here it gets a side-information version
- [[gibson-2019-efficiency/main]] (p. 4): efficiency under approximate message reconstruction; only named
- [[mackay-2003-information/ch10-noisy]] (pp. 167–168): rate achievable at bit-error $p_b$ is $C/(1-H_2(p_b))$
- [[polyanskiy-2025-information/ch01-introduction]] (p. xxii): theory used to lower-bound statistical risk
- [[polyanskiy-2025-information/ch11-lossless]] (p. 196): lossy compression with $\mathbb{E}[d(X,\hat X)]\le\epsilon$, deferred to Part V
- [[polyanskiy-2025-information/ch26-rate]] (p. 475): named here as the quantity evaluated for Gaussian and Hamming sources in Chapter 26; the text calls the study of optimal quantization rate-distortion theory, and the function itself is not defined in this unit
- [[polyanskiy-2025-information/ch27-rate]] (p. 485, 487): here: operational $R(D)$ (24.10) lower-bounded by information version $R^{(I)}(D)$ (Def. 24.5) [as `rate–distortion function`]
- [[polyanskiy-2025-information/ch28-rate]] (p. 491): $R(D)$: operational minimal rate; equals $\phi_S(D)$ under Theorem 25.1's conditions
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 507): $R(D)=\inf_{P_{\hat S|S}:\mathbb E d\le D}I(S;\hat S)$; here evaluated in closed form
- [[polyanskiy-2025-information/ch30-metric]] (p. 542): here $\phi_X(\epsilon)=\inf I(X;\hat X)$ s.t. $\mathbb E\,d(X,\hat X)\le\epsilon$, and its worst case over $P_X$
- [[polyanskiy-2025-information/ch33-mutual]] (p. 585): here $\phi(D)$, the minimum $I(\theta;\hat\theta)$ at expected loss $\le D$ [as `rate–distortion function`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 598): Bernoulli rate–distortion gives (31.6) [as `rate–distortion function`]
- [[polyanskiy-2025-information/ch36-strong-p2]] (p. 658): used to force $I(X;\hat X)\ge cd$
- [[shannon-1948-mathematical/main-p2]] (pp. 49–50): $R_1$: minimum $R$ over systems with average distortion $v_1$; the author calls it the rate of a source "for a given quality"
- [[stone-2022-information/appa-glossary]] (p. 245): smallest rate for a given distortion $D$
- [[stone-2022-information/appf-rules]] (p. 266): H.23 [as `rate–distortion function`]
- [[stone-2022-information/ch04-noisy]] (p. 106): theory of the minimum error forced when $H(X)>C$; only introduced here
- [[stone-2022-information/ch08-rate]] (pp. 179–180): smallest rate R for each distortion D; equals $\min I(X;\hat X)$ over $p(\hat x|x)$ with $E[d]\le D$ [as `rate–distortion function`]
- [[tishby-2000-bottleneck/main]] (p. 5): R(D), the minimal $I(X;\tilde X)$ under a bound on expected distortion

## Candidate bridges

- [structural-analogy] fidelity criterion with penalties ↔ rate–distortion function — both ask how many bits suffice for a given tolerated damage (Pierce gives no formula). — from [[pierce-1980-introduction/ch14-back]] (information-theory → unspecified)
- [same-math] $R_1=\min$ of mutual information at fixed average distortion ↔ rate–distortion function $R(D)$: same optimisation; the exponential solution $P_y(x)=B(x)e^{-\lambda\rho}$ is its first-order condition. — from [[shannon-1948-mathematical/main-p2]] (information-theory → other)
