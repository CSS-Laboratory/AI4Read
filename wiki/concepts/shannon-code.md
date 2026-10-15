---
id: shannon-code
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch05-data-p1, polyanskiy-2025-information/ch12-variable]
raw_ids: [Shannon code]
generated_by: build_kg.py
---

# shannon-code

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch05-data-p1]] (pp. 87, 96): lengths $\lceil\log_D 1/p_i\rceil$; within one symbol of $H$, but can be much worse for single symbols [new]
- [[polyanskiy-2025-information/ch12-variable]] (p. 209): lengths $\lceil\log_2 1/P_X(a)\rceil$ [as `Shannon code`; new]

## Instances that use it

- [[shannon-vs-huffman-09999]] — Shannon code gives 14 bits to a symbol of probability 0.0001 — from [[cover-2006-elements/ch05-data-p1]]

## Candidate bridges

- [same-math] Lemma 5.12.1 (expected depth $=H(Y)$ for leaf probabilities $2^{-k}$) ↔ information-theory canon, prefix codes: dyadic Shannon code reaches $L=H$ — the same identity read in two directions. — from [[cover-2006-elements/ch05-data-p2]] (information-theory → information-theory)
- [structural-analogy] $K(x)\approx\log\frac1{P_U(x)}$ ↔ Shannon code length $\log\frac1{p(x)}$ — the text itself draws this parallel (p. 170). — from [[cover-2006-elements/ch07-kolmogorov]] (information-theory → unspecified)
- [structural-analogy] Competitive optimality of $\mathbf b^*$ ↔ competitive optimality of Shannon codes (Chapter 5): the source calls the two results similar (p. 471); here the proof uses $E[S/S^*]\le1$ plus Markov. — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [same-math] MDL message length $L=-\log_2P$ ↔ information-theory: Shannon code length $-\log_2P(x)$ — the same relation, used to translate models into bits (p. 352) — from [[mackay-2003-information/ch28-model]] (information-theory → information-theory)
