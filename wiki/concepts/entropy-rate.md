---
id: entropy-rate
type: concept
fields: [information-theory]
n_sources: 25
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch04-entropy, cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch06-gambling, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p3, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch15-information, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch06-language, pierce-1980-introduction/ch07-efficient, pierce-1980-introduction/ch13-information, pierce-1980-introduction/ch14-back, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch11-lossless, polyanskiy-2025-information/ch12-variable, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch16-neyman, polyanskiy-2025-information/ch27-rate, rosvall-2008-maps/main-p1, shannon-1948-mathematical/main-p1, shannon-1951-prediction/main, stone-2022-information/ch03-source]
raw_ids: [entropy rate]
canon_spine: information-theory
generated_by: build_kg.py
---

# entropy-rate

## Canon spine entry

- **entropy rate** (information-theory): entropy per symbol of a process with memory, such as English text (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch04-entropy]] (p. 63): $\lim\frac1nH(X_1,\dots,X_n)$, entropy growth per symbol, for a process with memory
- [[cover-2006-elements/ch05-data-p1]] (p. 89): limit of $H(X_1,\dots,X_n)/n$ for a stationary process; the achievable bits per symbol
- [[cover-2006-elements/ch05-data-p2]] (pp. 104, 117): block coding's per-symbol length tends to it; summary
- [[cover-2006-elements/ch06-gambling]] (p. 132): $H(\mathcal X)=\lim\frac1nH(X_1,\dots,X_n)$ for dependent races or English
- [[cover-2006-elements/ch08-channel-p2]] (p. 218): $H(\mathcal V)$ of a stationary source; compared with $C$
- [[cover-2006-elements/ch11-maximum]] (p. 273): here $\lim h(X^n)/n$ for real-valued processes
- [[cover-2006-elements/ch12-information-p3]] (p. 322): here $H(\mathcal X)$ of a stationary ergodic process; limit of $H(X_j|X_{j-k}^{j-1})$ as $k\to\infty$
- [[cover-2006-elements/ch14-network-p2]] (p. 415): replaces entropies when the source is jointly ergodic
- [[cover-2006-elements/ch15-information]] (p. 475): $H=\lim H^k$, also $\lim\frac1nH(X_1,\dots,X_n)$
- [[pierce-1980-introduction/ch05-entropy]] (pp. 91–94): entropy per symbol of a source with memory, as limit of (5.3), $H_N$ of (5.4), or (5.5)
- [[pierce-1980-introduction/ch06-language]] (pp. 110–111): Pierce says that, if Shannon is right, English text involves a choice of about 1 bit per symbol; a grammar could yield a new estimate
- [[pierce-1980-introduction/ch07-efficient]] (pp. 129–130): for English, estimated by letter, word and prediction experiments: 4.7, 4.14, 2.5 bits per character and 0.6–1.3 bits per letter
- [[pierce-1980-introduction/ch13-information]] (p. 254, 259): Pierce quotes Shannon's 3.3–7.2 bits per word and Pinkerton's 2.8 bits per note, which Pierce thinks is too high
- [[pierce-1980-introduction/ch14-back]] (p. 269): "information rate or entropy of an ergodic message source", part of the core
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 109): $\lim\frac1nH(X^n)$, when the limit exists
- [[polyanskiy-2025-information/ch11-lossless]] (p. 195): entropy per symbol of the process; the limit of normalized optimal length
- [[polyanskiy-2025-information/ch12-variable]] (p. 202): the limit of the optimal compression rate of an i.i.d. process, equal to $H(S)$ here [as `entropy rate`]
- [[polyanskiy-2025-information/ch14-entropy]] (pp. 233, 236): $\mathcal H(\mathbb S)$, per-symbol entropy of a stationary process; limit of $H(S_{m+1}|S_1^m)$ from above
- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list
- [[polyanskiy-2025-information/ch16-neyman]] (p. 288): here the relative entropy rate is the Stein exponent for stationary ergodic data (under both $P$ and $Q$) [as `entropy rate`]
- [[polyanskiy-2025-information/ch27-rate]] (p. 487): equals $R^{(I)}(D)$ in the discrete case for a stationary ergodic source, under the distortion assumption of Thm 24.4(c) [as `entropy rate`]
- [[rosvall-2008-maps/main-p1]] (pdf 1–2): rate at which a Markov process can be encoded at best; the authors choose not to use it as the aim
- [[shannon-1948-mathematical/main-p1]] (pp. 13–14): $H$ per symbol and $H'=mH$ per second; $F_N,G_N\to H$
- [[shannon-1951-prediction/main]] (p. 51): here $H=\lim_{N\to\infty}F_N$, entropy per letter of English with ever longer context
- [[stone-2022-information/ch03-source]] (pp. 64–68): here the block estimates $G_N$ that converge to H of English at $N_C$

## Instances that use it

- [[non-converging-entropy-average]] — independent source with $p_i$ from (4.13); no entropy rate — from [[cover-2006-elements/ch04-entropy]]
- [[toeplitz-determinant-monotonicity]] — stationary-process entropy rate analogue for $|K_k|^{1/k}$ — from [[cover-2006-elements/ch16-inequalities]]
- [[cesaro-limit-entropy-rate]] — $\lim h(X^n)/n=\lim h(X_n|X^{n-1})$ used for determinants — from [[cover-2006-elements/ch16-inequalities]]
- [[gilbert-elliott-hmm]] — binary-state HMM with BSC emissions; entropy rate via a Blackwell measure that can be fractal-like — from [[polyanskiy-2025-information/ch07-tensorization]]
- [[gaussian-mixture-bounded-centers]] — a model with $H^2\asymp D$, where the local-entropy rate is exact — from [[polyanskiy-2025-information/ch35-entropic]]

## Candidate bridges

- [structural-analogy] Capacity must at least match source entropy rate (p. 183) ↔ control-theory: law of requisite variety (canon link; not stated in this unit). — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] doubling rate $W$ ↔ entropy rate: the authors call $W$ a "dual" of the entropy rate (p. 4) — from [[cover-2006-elements/ch01-introduction]] (information-theory → other)
- [same-math] Entropy rate ↔ prediction: (11.40) links entropy rate to minimum mean squared prediction error for Gaussian processes. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other)
- [structural-analogy] Cesàro-mean proof of $W^*_\infty$ ↔ entropy rate of stationary processes: parallel limit structure, since the chain rule for $W$ is formally that of $H$ (p. 470). — from [[cover-2006-elements/ch15-information]] (information-theory → other)
- [same-math] $H_N$ in (5.4) ↔ conditional entropy / entropy rate: next-symbol entropy given the preceding block, averaged over blocks. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → other)
- [same-math] Szegő limit of $\frac1n\sum\log\sigma_j^2$ to the spectral integral ↔ entropy rate of a Gaussian process (the chapter points to (6.12)). — from [[polyanskiy-2025-information/ch22-channels]] (information-theory → unspecified)
- [same-math] block estimates $G_N\to H$ ↔ information-theory: entropy rate of a process with memory — per-letter block entropy converging to the limit — from [[stone-2022-information/ch03-source]] (information-theory → information-theory)
