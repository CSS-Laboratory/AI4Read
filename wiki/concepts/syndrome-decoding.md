---
id: syndrome-decoding
type: concept
fields: [information-theory]
n_sources: 3
tiers: [core]
grounding: digests
sources: [mackay-2003-information/ch01-introduction, mackay-2003-information/ch14-very, mackay-2003-information/ch47-low]
generated_by: build_kg.py
---

# syndrome-decoding

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch01-introduction]] (pp. 10–12): compute the pattern of violated parity checks, **z** = **H r**, and map it to the most probable noise pattern [new]
- [[mackay-2003-information/ch14-very]] (p. 229): compute $\mathbf z=\mathbf{Hr}$, which depends only on the noise, and solve $\mathbf{Hx}=\mathbf z$ [new]
- [[mackay-2003-information/ch47-low]] (p. 558): decode by inferring the noise $\mathbf n$ from the syndrome $\mathbf z=\mathbf H\mathbf r$ [new]

## Instances that use it

- [[syndrome-decoding-gibbs-failure]] — Gibbs sampling gets stuck on codeword-constrained posteriors — from [[mackay-2003-information/ch29-monte]]
- [[bsc-syndrome-decoding]] — on BSC the syndrome decoder finds the minimum-weight noise; $D_0$ is the set of coset leaders — from [[polyanskiy-2025-information/ch20-random]]

## Candidate bridges

- [structural-analogy] linear compression $w=Hx$ with a decoder choosing the likeliest $x$ ↔ coding theory: syndrome decoding of linear error-correcting codes — the text says efficient decoders of such codes can make the decompressor practical (p. 218). — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → information-theory)
