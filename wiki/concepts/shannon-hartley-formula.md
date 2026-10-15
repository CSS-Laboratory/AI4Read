---
id: shannon-hartley-formula
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 11
n_works: 6
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch10-gaussian, mackay-2003-information/ch11-error, pierce-1980-introduction/ch09-many, pierce-1980-introduction/ch10-information, polyanskiy-2025-information/ch22-channels, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch25-channel, shannon-1948-mathematical/main-p2, stone-2022-information/appb-mathematical, stone-2022-information/appf-rules, stone-2022-information/ch07-channel]
raw_ids: [Shannon–Hartley formula]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# shannon-hartley-formula

## Canon spine entry

- **Shannon–Hartley formula** (information-theory): C = W log2(1 + S/N) for a band-limited Gaussian channel (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch10-gaussian]] (p. 250): $C=W\log(1+P/N_0W)$ bits per second for the band-limited white-noise channel
- [[mackay-2003-information/ch11-error]] (p. 182): $C=W\log(1+P/N_0W)$ bits per second for the continuous band-limited channel [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch09-many]] (p. 175): eq. 9.3; here derived by sphere counting
- [[pierce-1980-introduction/ch10-information]] (p. 192): the formula 10.3/10.4; Pierce says it holds only for ideal encoding
- [[polyanskiy-2025-information/ch22-channels]] (p. 400): appears here only as the per-use AWGN formula; no bandwidth $W$ appears in this unit
- [[polyanskiy-2025-information/ch23-capacity]] (p. 419): the bandlimited result (21.13)
- [[polyanskiy-2025-information/ch25-channel]] (p. 458): per-use $C=\frac12\log(1+P)$ in the AWGN computation, with $\sigma^2=1$ implicit
- [[shannon-1948-mathematical/main-p2]] (p. 43): Theorem 17: $C=W\log\frac{P+N}N$ for white thermal noise, band $W$, average power $P$
- [[stone-2022-information/appb-mathematical]] (p. 249): the appendix gives only the form $C=\tfrac12\log(1+P/N)$, with $N$ the noise variance
- [[stone-2022-information/appf-rules]] (p. 266): here only the form $C=\frac12\log(1+P/N)$ with iid Gaussian input and noise; no bandwidth term appears on these pages [as `Shannon–Hartley formula`]
- [[stone-2022-information/ch07-channel]] (p. 156): close relative: $C=\tfrac12\log(1+P/N)$ per value, which the author calls Shannon's well-known equation. The bandwidth form $W\log_2(1+S/N)$ is not stated here [as `Shannon–Hartley formula`; weak: not really used in this unit]

## Candidate bridges

- [same-math] $C=W\log(1+S/N)$ here ↔ Shannon–Hartley formula in the canon list — the same formula, with $S/N=P/N_0W$. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → unspecified)
- [structural-analogy] Capacity $\tfrac12\log(1+\mathrm{SNR})$ ↔ information-theory: Shannon–Hartley formula, with one use of the channel as one sample. — from [[mackay-2003-information/ch11-error]] (information-theory → information-theory)
- [same-math] Sphere counting for $C=W\log(1+P/N)$ ↔ information-theory: the Shannon–Hartley formula in the canon list — the same formula. — from [[pierce-1980-introduction/ch09-many]] (information-theory → information-theory)
- [same-math] Gaussian $R(D)=\frac12\log\sigma^2/D$ ↔ Shannon–Hartley formula $C=\frac12\log(1+\mathrm{SNR})$ — both are a Gaussian mutual information with a noise-ratio inside the log. — from [[polyanskiy-2025-information/ch29-evaluating]] (information-theory → unspecified)
