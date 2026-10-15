---
id: source-coding-theorem
type: concept
fields: [information-theory, bayesian]
n_sources: 21
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch03-asymptotic, cover-2006-elements/ch05-data-p1, gibson-2019-efficiency/main, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch04-source, mackay-2003-information/ch05-symbol, mackay-2003-information/ch14-very, murphy-2023-pml2/ch05-information-p2, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch07-efficient, polyanskiy-2025-information/ch11-lossless, polyanskiy-2025-information/ch12-variable, polyanskiy-2025-information/ch13-fixed, polyanskiy-2025-information/ch14-entropy, polyanskiy-2025-information/ch26-rate, rosvall-2008-maps/main-p1, shannon-1948-mathematical/main-p1, stone-2022-information/ch01-information, stone-2022-information/ch03-source, stone-2022-information/ch08-rate]
raw_ids: [source coding theorem]
canon_spine: information-theory
generated_by: build_kg.py
---

# source-coding-theorem

## Canon spine entry

- **source coding theorem** (information-theory): data cannot be losslessly compressed below H bits per symbol on average, and H is achievable (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (pp. 6, 9): only previewed: $H$ lower-bounds average length, achievable within one bit [as `source coding theorem`]
- [[cover-2006-elements/ch03-asymptotic]] (pp. 53, 55): here only a consequence: typical-set code of ≈ nH bits per block (pp. 53, 55); the theorem is not stated in this unit
- [[cover-2006-elements/ch05-data-p1]] (pp. 87–89): here: $H\le L^*<H+1$, and $L_n\to H$ by block coding
- [[gibson-2019-efficiency/main]] (p. 3): here only the *task* of source coding (short signals on average) is defined, not the theorem
- [[jaynes-2003-probability/ch22-introduction]] (p. 640): expected Shannon–Fano code length per symbol equals $H_1$ bits (left as exercise) and $C\ge nH_1$
- [[mackay-2003-information/ch04-source]] (p. 74): (1/N)H_δ(X^N) is within ε of H for N large and 0<δ<1 (Thm 4.1) (p. 78). Here it is stated for lossy compression with failure probability δ, not the canon's lossless version [as `source coding theorem`]
- [[mackay-2003-information/ch05-symbol]] (p. 98): here, for symbol codes: a prefix code with $H(X)\le L<H(X)+1$ exists
- [[mackay-2003-information/ch14-very]] (p. 231): here: a linear compressor exists at any rate $R>H(X)$, virtually lossless
- [[pierce-1980-introduction/ch05-entropy]] (pp. 98, 105): encoding takes about $H$ digits per symbol; converse only asserted provable here
- [[pierce-1980-introduction/ch07-efficient]] (p. 128): entropy is a lower limit; it can be approached with block coding. This unit states only the approach by blocks
- [[polyanskiy-2025-information/ch11-lossless]] (p. 195): previewed: optimal lengths $H(X)-O(\log(1+H))$ or $H(X)+O(1)$
- [[polyanskiy-2025-information/ch12-variable]] (p. 199, 202): here Thm 10.3 for single-shot $f^*$, and the WLLN version $\frac1nl(f^*(S^n))\to H(S)$ in probability [as `source coding theorem`]
- [[polyanskiy-2025-information/ch13-fixed]] (p. 214): fixed-length version: $\epsilon^*(S^n,nR)\to0$ if $R>H(S)$, $\to1$ if $R<H(S)$
- [[polyanskiy-2025-information/ch14-entropy]] (p. 233): for ergodic sources, length per symbol $\to\mathcal H$; fixed-length error $\to0/1$
- [[polyanskiy-2025-information/ch26-rate]] (p. 475): lossless limit given by entropy; here only recalled from Part II
- [[rosvall-2008-maps/main-p1]] (pdf 2): average codeword length cannot be below $H(X)$
- [[shannon-1948-mathematical/main-p1]] (p. 16): Theorem 9 gives rate $C/H-\epsilon$, never above $C/H$
- [[stone-2022-information/ch01-information]] (p. 19): only hinted at here: the author says Shannon's work guarantees that if each pixel carries on average 5.92 bits, it can be represented with no more than 5.92 binary digits per pixel (p. 19); the theorem is not named or stated in general form [as `source coding theorem`]
- [[stone-2022-information/ch03-source]] (p. 49): rate $C/H-\epsilon$ symbols/s is achievable; more than $C/H$ is not
- [[stone-2022-information/ch08-rate]] (p. 180): the zero-distortion special case of the rate distortion theorem [as `source coding theorem`]

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (p. 247): expected lossless code length is at least $\mathbb H(p)$; excess is $D_{KL}(p\|q)$ [new]

## Candidate bridges

- [structural-analogy] Block coding saving ↔ information-theory: typical set / source coding theorem — long blocks let the code use only the likely sequences. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
