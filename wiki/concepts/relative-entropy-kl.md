---
id: relative-entropy-kl
type: concept
fields: [information-theory]
n_sources: 7
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, mackay-2003-information/ch23-useful, polyanskiy-2025-information/ch14-entropy, stone-2022-information/appa-glossary]
generated_by: build_kg.py
---

# relative-entropy-kl

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch11-maximum]] (p. 267): $D(g\|f^*)\ge0$ drives the proof of the theorem
- [[cover-2006-elements/ch12-information-p1]] (pp. 285, 288): controls type-class probability $2^{-nD(P\|Q)}$ and the cost of a mismatched Huffman code
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 291): Gibbs inequality (9.72) is the non-negativity of KL divergence (canon link; not stated in this unit)
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 298): ψ_B/(10n)=Σ f log₁₀(f/p); Jaynes calls −ψ_B/n an "entropy per symbol" relative to the expected distribution
- [[mackay-2003-information/ch23-useful]] (p. 318): $D_{\rm KL}(\mathbf p\|\mathbf m)$ in the entropic distribution
- [[polyanskiy-2025-information/ch14-entropy]] (p. 236): used to bound term $A$ in the proof
- [[stone-2022-information/appa-glossary]] (pp. 243, 246): measure of difference between two distributions

## Candidate bridges

- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
