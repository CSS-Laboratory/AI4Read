---
id: quantization
type: concept
fields: [information-theory]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [pierce-1980-introduction/ch04-encoding, pierce-1980-introduction/ch07-efficient, polyanskiy-2025-information/ch26-rate]
generated_by: build_kg.py
---

# quantization

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/ch04-encoding]] (p. 68): rounding each sample amplitude to the nearest of a limited set of whole numbers [new]
- [[pierce-1980-introduction/ch07-efficient]] (p. 132): allowing each sample only preassigned values [new]
- [[polyanskiy-2025-information/ch26-rate]] (p. 475): mapping continuous/analog signals into discrete/digital ones [new]

## Instances that use it

- [[sampling-and-quantization]] — analog-to-digital pipeline of Figure 23.7 — from [[polyanskiy-2025-information/ch26-rate]]
- [[k-means]] — optimal vector quantization of the empirical distribution — from [[polyanskiy-2025-information/ch27-rate]]

## Candidate bridges

- [structural-analogy] Quantization cost $-\log\Delta$ ↔ measurement resolution in applied statistics. — from [[cover-2006-elements/ch09-differential]] (information-theory → unspecified)
- [structural-analogy] vector quantization ↔ information-theory: lossy compression with distortion (rate–distortion) — the chapter gives distortion (20.1) but no rate analysis — from [[mackay-2003-information/ch20-example]] (information-theory → information-theory)
- [structural-analogy] Capacity $\approx\inf_\epsilon\{\epsilon^2+\log N\}$ ↔ model selection / description length: trade-off between a quantization error and the bits naming the cell. — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → political-science)
