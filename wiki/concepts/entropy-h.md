---
id: entropy-h
type: concept
fields: [information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [pierce-1980-introduction/ch07-efficient, stone-2022-information/ch10-thermodynamic]
raw_ids: [entropy-H]
generated_by: build_kg.py
---

# entropy-h

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/ch07-efficient]] (p. 127): minimum average binary digits per symbol (or per second) needed to send a source's messages [as `entropy-H`]
- [[stone-2022-information/ch10-thermodynamic]] (pp. 207–208): Shannon entropy; equals $\log W$ for $W$ equally probable outcomes [as `entropy-H`]

## Instances that use it

- [[bernoulli-entropy]] — $h(p)$ is maximal at $\frac12$, zero at 0 and 1 — from [[polyanskiy-2025-information/ch02-entropy]]
- [[noisy-channel-conditional-entropy]] — $H(X|Y)=h(\delta)$ for XOR noise — from [[polyanskiy-2025-information/ch02-entropy]]

## Candidate bridges

- [same-math] $-\sum\mu_iP_{ij}\log P_{ij}$ ↔ conditional entropy $H(X_2|X_1)$ under the stationary law — literally the same quantity. — from [[cover-2006-elements/ch04-entropy]] (information-theory → unspecified)
- [same-math] $D_{\rm KL}(P\|Q)\ge0$ (Gibbs) ↔ information-theory: cross-entropy $=H+D_{\rm KL}$ is minimized by the true distribution — same quantity, as the concept list defines it (the unit does not state this). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [same-math] Shannon entropy H ↔ statistical mechanics: Gibbs entropy k_B Σp_i ln(1/p_i), equal to H up to the factor k_B (p. 87). — from [[mackay-2003-information/ch04-source]] (information-theory → complex-systems)
- [same-math] Min-entropy $H_\infty$ ↔ cryptography: the book names the same quantity (p. 14) — from [[polyanskiy-2025-information/ch02-entropy]] (information-theory → other)
