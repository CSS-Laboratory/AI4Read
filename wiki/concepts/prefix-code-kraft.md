---
id: prefix-code-kraft
type: concept
fields: [information-theory, bayesian, complex-systems, llm]
fields_strong: [information-theory, bayesian, complex-systems, llm]
n_sources: 13
n_works: 6
tiers: [core, deep, reference]
grounding: digests
sources: [cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch07-kolmogorov, mackay-2003-information/ch06-stream, mackay-2003-information/ch07-codes, mackay-2003-information/ch42-hopfield, pierce-1980-introduction/ch05-entropy, polyanskiy-2025-information/ch11-lossless, polyanskiy-2025-information/ch12-variable, rosvall-2008-maps/main-p1, rosvall-2008-maps/main-p2, stone-2022-information/appa-glossary, stone-2022-information/ch03-source]
aliases: [prefix-code-kraft-inequality]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# prefix-code-kraft

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `prefix-code-kraft-inequality` — 4 digest(s)

## Canon spine entry

- **prefix code & Kraft inequality** (information-theory): instantaneously decodable codes exist iff Σ 2^{−ℓ_i} ≤ 1; code lengths and probabilities are interchangeable (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch05-data-p1]] (pp. 81–83): prefix codes (no codeword is a prefix of another) exist for lengths $l_i$ iff $\sum D^{-l_i}\le1$ [alias `prefix-code-kraft-inequality`]
- [[cover-2006-elements/ch05-data-p2]] (pp. 102, 108, 117): prefix-freeness read as disjoint intervals; $\sum2^{-l}\le1$ used in all proofs [alias `prefix-code-kraft-inequality`]
- [[cover-2006-elements/ch07-kolmogorov]] (p. 154): halting programs form a prefix-free set, so $\sum2^{-l(p)}\le1$ (Lemma 7.3.1)
- [[mackay-2003-information/ch06-stream]] (pp. 126–127): Exercise 6.18 and 6.22 link codelengths to the Kraft inequality/equality [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch07-codes]] (pp. 134–135): complete code = Kraft equality; any complete code is optimal for the prior it implies [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch42-hopfield]] (p. 521): the conserved weight $2^{-l}$ in the southeast puzzle [alias `prefix-code-kraft-inequality`; work fields: information-theory, bayesian, llm]
- [[pierce-1980-introduction/ch05-entropy]] (pp. 100–101): prefix property: no code word begins another; allows decoding without a known start (pp. 100–101). Kraft's inequality is not stated here. [weak: not really used in this unit]
- [[polyanskiy-2025-information/ch11-lossless]] (p. 195): if one restricts to prefix-free or uniquely decodable codes, the optimal length is $H(X)+O(1)$
- [[polyanskiy-2025-information/ch12-variable]] (p. 208): prefix codes exist for lengths with $\sum2^{-l_a}\le1$, and uniquely decodable codes obey it [as `prefix code & Kraft inequality`; alias `prefix-code-kraft-inequality`]
- [[rosvall-2008-maps/main-p1]] (pdf 2): the Huffman code is prefix-free [work fields: information-theory, complex-systems]
- [[rosvall-2008-maps/main-p2]]: node codewords appear as binary strings of varying length (e.g. 0, 10, 0001). The pages do not state that the code is prefix-free. [work fields: information-theory, complex-systems]
- [[stone-2022-information/appa-glossary]] (p. 244): no codeword is a prefix of another
- [[stone-2022-information/ch03-source]] (p. 59): here only the prefix property (no codeword begins another) is stated, not the Kraft inequality
