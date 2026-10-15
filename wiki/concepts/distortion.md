---
id: distortion
type: concept
fields: [control-theory, information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch09-incessant, stone-2022-information/appb-mathematical]
generated_by: build_kg.py
---

# distortion

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch09-incessant]] (p. 188): a received signal that is a definite function of the sent signal; correctable, at least in principle, if the function has an inverse [new]

### information-theory

- [[stone-2022-information/appb-mathematical]] (p. 248): $d$ per element, $D$ mean, between $\mathbf x$ and $\hat{\mathbf x}$ [new]

## Instances that use it

- [[binary-source-rate-distortion]] — $R(D)=H(p)-H(D)$ with a BSC test channel — from [[cover-2006-elements/ch13-rate]]
- [[gaussian-source-rate-distortion]] — $R(D)=\frac12\log\sigma^2/D$; $D(R)=\sigma^22^{-2R}$ — from [[cover-2006-elements/ch13-rate]]
- [[one-bit-gaussian-quantizer]] — points $\pm\sqrt{2/\pi}\sigma$, distortion $0.3633\sigma^2$ versus the block bound $\sigma^2/4$ — from [[cover-2006-elements/ch13-rate]]
- [[cauchy-quadratic-distortion]] — $D_{\max}=\infty$ so fixed-length $R(D)=\infty$, but $R^{(I)}(D)<\infty$ — from [[polyanskiy-2025-information/ch28-rate]]
- [[uncoded-vs-separated-bsc]] — Ber(1/2) over BSC$_\delta$ with $\rho=1$: separated vs uncoded distortion — from [[polyanskiy-2025-information/ch29-evaluating]]
- [[sphere-rate-distortion]] — uniform on $S^{d-1}$: rate–distortion $\approx(d-1)\log\frac1\epsilon$ — from [[polyanskiy-2025-information/ch30-metric]]
- [[buy-and-hold-distortion]] — a popular distortion of a professional narrative — from [[shiller-2019-narrative/front-preface]]
- [[binary-rate-distortion]] — $R(D)=H(p)-H(D)$ with Hamming distortion — from [[stone-2022-information/ch08-rate]]
- [[gaussian-rate-distortion]] — $R(D)=\tfrac12\log(\sigma^2/D)$; one extra bit divides D by 4 — from [[stone-2022-information/ch08-rate]]

## Candidate bridges

- [structural-analogy] Water-filling of power over noise levels ↔ rate–distortion: reverse water-filling — both allocate a budget over independent Gaussian components with a common level. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → other)
- [structural-analogy] rate distortion $\min I(X;\hat X)$ s.t. distortion ↔ information-theory: channel capacity $\max I(X;Y)$ s.t. cost — dual optimizations with a random-coding proof and a shared alternating algorithm. — from [[cover-2006-elements/ch13-rate]] (information-theory → information-theory)
- [structural-analogy] Informativeness–complexity trade-off in lexica ↔ rate–distortion theory: bits spent against loss of useful distinctions. — from [[gibson-2019-efficiency/main]] (information-theory → other)
- [same-math] Rate–distortion via reversed code (10.20) ↔ lossy compression theory (information-theory canon). — from [[mackay-2003-information/ch10-noisy]] (information-theory → unspecified)
- [structural-analogy] vector quantization ↔ information-theory: lossy compression with distortion (rate–distortion) — the chapter gives distortion (20.1) but no rate analysis — from [[mackay-2003-information/ch20-example]] (information-theory → information-theory)
- [metaphor] Wald's "inference as decision" (§1.1) ↔ information-theory: rate–distortion, choosing a representation under a dissimilarity — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [structural-analogy] Quantizing to ~1% accuracy ↔ information-theory: rate–distortion — accept small error to save digits. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
- [structural-analogy] Fidelity criterion over long stretches ↔ rate–distortion theory: required bits depend on the allowed distortion measure. — from [[pierce-1980-introduction/ch07-efficient]] (information-theory → other)
- [structural-analogy] fidelity criterion with penalties ↔ rate–distortion function — both ask how many bits suffice for a given tolerated damage (Pierce gives no formula). — from [[pierce-1980-introduction/ch14-back]] (information-theory → unspecified)
- [structural-analogy] Water-filling over $\sigma_j^2$ ↔ reverse water-filling in rate–distortion for parallel Gaussians (not in this unit; to be checked by the Knowledge Manager). — from [[polyanskiy-2025-information/ch22-channels]] (information-theory → unspecified)
- [structural-analogy] rate-distortion for the worst-case distribution ↔ minimax thinking: metric entropy as the hardest-distribution case (p. 476) — from [[polyanskiy-2025-information/ch26-rate]] (information-theory → other)
- [structural-analogy] Average vs. excess distortion ↔ statistics/ML: average vs. high-probability risk bounds (p. 485). — from [[polyanskiy-2025-information/ch27-rate]] (information-theory → other)
- [structural-analogy] Shannon lower bound for estimation (§30.1 preview) ↔ statistics: lower bounds on estimation error via rate-distortion. — from [[polyanskiy-2025-information/ch29-evaluating]] (information-theory → other)
- [structural-analogy] Metric entropy $\log N(\epsilon)$ ↔ rate–distortion: Thm 27.16 compares worst-case rate–distortion at distortion cε (plus $\log2$, factor $1/(1-2c)$) with $\log N$; it is a comparison, not an equality. — from [[polyanskiy-2025-information/ch30-metric]] (information-theory → other)
- [structural-analogy] Randomized estimators as Markov kernels ↔ channels and rate–distortion: action space $\hat{\mathcal Y}$ vs $\mathcal Y$ (p. 558). — from [[polyanskiy-2025-information/ch31-basics]] (information-theory → other)
- [structural-analogy] MIM ↔ information-theory: converse of joint source–channel coding — same "rate-distortion ≤ capacity" chain (p. 585) — from [[polyanskiy-2025-information/ch33-mutual]] (information-theory → information-theory)
- [same-math] SLB for $\phi$ ↔ rate-distortion theory: Shannon lower bound (Section 26.1) — from [[polyanskiy-2025-information/ch33-mutual]] (information-theory → other)
- [structural-analogy] Volume bound for metric entropy ↔ SLB for rate-distortion (Remark 30.2) — from [[polyanskiy-2025-information/ch33-mutual]] (information-theory → unspecified)
- [same-math] Bernoulli rate–distortion in (31.6) ↔ lossy source coding: the Hamming distortion bound is the one from Section 26.1.1 (p. 598). — from [[polyanskiy-2025-information/ch34-lower]] (information-theory → other)
- [same-math] $R_1=\min$ of mutual information at fixed average distortion ↔ rate–distortion function $R(D)$: same optimisation; the exponential solution $P_y(x)=B(x)e^{-\lambda\rho}$ is its first-order condition. — from [[shannon-1948-mathematical/main-p2]] (information-theory → other)
- [metaphor] Speed–accuracy trade-off ↔ rate–distortion trade-off — fast, low-bit responses are less accurate. — from [[stone-2022-information/ch08-rate]] (information-theory → unspecified)
- [structural-analogy] Rate distortion with chosen d ↔ IB with data-derived d — the same exponential-form solution with a different distortion (pp. 6, 12) — from [[tishby-2000-bottleneck/main]] (information-theory → unspecified)
