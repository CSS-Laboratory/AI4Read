---
id: water-filling
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 3
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [cover-2006-elements/ch10-gaussian, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch22-channels]
generated_by: build_kg.py
---

# water-filling

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch10-gaussian]] (pp. 252–256): optimal power $P_i=(\nu-N_i)^+$ over parallel channels; extends to eigenvalues and spectra [new]
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 114): optimal spectral allocation $f_X^*=|T-f_N|_+$, only quoted here [new]
- [[polyanskiy-2025-information/ch22-channels]] (p. 402): optimal power $P_k=|T-\sigma_k^2|^+$ across parallel or spectral branches [new]

## Instances that use it

- [[parallel-channel-water-filling]] — Figure 10.4: power poured into channels of different noise levels — from [[cover-2006-elements/ch10-gaussian]]
- [[spectral-water-filling]] — Figure 10.5: input spectrum large where the noise spectrum is small — from [[cover-2006-elements/ch10-gaussian]]
- [[parallel-gaussian-water-filling]] — Thm 13.3.3 — from [[cover-2006-elements/ch13-rate]]
- [[adsl-power-allocation]] — water-filling for cable modems and ADSL — from [[polyanskiy-2025-information/ch22-channels]]

## Candidate bridges

- [structural-analogy] Water-filling of power over noise levels ↔ rate–distortion: reverse water-filling — both allocate a budget over independent Gaussian components with a common level. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → information-theory)
- [structural-analogy] Reverse water-filling for parallel Gaussians ↔ information-theory: water-filling power allocation for parallel Gaussian channels — only structurally similar here; the text does not state the channel version, so confirm before using. — from [[cover-2006-elements/ch13-rate]] (information-theory → information-theory)
- [structural-analogy] Water-filling over $\sigma_j^2$ ↔ reverse water-filling in rate–distortion for parallel Gaussians (not in this unit; to be checked by the Knowledge Manager). — from [[polyanskiy-2025-information/ch22-channels]] (information-theory → unspecified)
