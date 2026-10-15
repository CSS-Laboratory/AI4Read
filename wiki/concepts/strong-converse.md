---
id: strong-converse
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch24-strong]
raw_ids: [strong converse]
generated_by: build_kg.py
---

# strong-converse

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch21-channel]] (p. 374): $C_\epsilon$ constant for $0<\epsilon<1$ [as `strong converse`; new]
- [[polyanskiy-2025-information/ch24-strong]] (p. 422–423): above capacity the error probability tends to 1; $C_\epsilon=C$ for $0<\epsilon<1$ under finite $|\mathcal A|$ or $|\mathcal B|$ [new]

## Instances that use it

- [[bsc]] — special case of the strong converse; dispersion $\delta\bar\delta\log^2(\bar\delta/\delta)$; Figs. 22.1–22.3 — from [[polyanskiy-2025-information/ch24-strong]]
- [[awgn-channel]] — strong converse holds (Ex. IV.33); dispersion $\frac{P(P+2)}{2(P+1)^2}\log^2e$ — from [[polyanskiy-2025-information/ch24-strong]]

## Candidate bridges

- [structural-analogy] Weak vs strong converse (mean of LLR vs full CDF) ↔ channel coding: the same weak/strong converse pattern (p. 283) — from [[polyanskiy-2025-information/ch16-neyman]] (information-theory → information-theory)
- [same-math] Strong converse proof via $\beta_{1-\epsilon}$ ↔ hypothesis testing: Stein's lemma and Neyman–Pearson — the same $\beta$ exponent gives the code-size bound. — from [[polyanskiy-2025-information/ch24-strong]] (information-theory → other:statistics)
- [structural-analogy] Rényi divergence upgrading weak to strong converse ↔ large-deviation/Rényi methods: the exponent for $R>C$ uses order $1/(1+\rho)$. — from [[polyanskiy-2025-information/ch24-strong]] (information-theory → other:large-deviation-renyi-methods)
