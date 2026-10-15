---
id: prefix-code-kraft
type: concept
fields: [information-theory]
n_sources: 9
tiers: [core, deep, reference]
grounding: digests
sources: [cover-2006-elements/ch07-kolmogorov, mackay-2003-information/ch06-stream, mackay-2003-information/ch07-codes, pierce-1980-introduction/ch05-entropy, polyanskiy-2025-information/ch11-lossless, rosvall-2008-maps/main-p1, rosvall-2008-maps/main-p2, stone-2022-information/appa-glossary, stone-2022-information/ch03-source]
generated_by: build_kg.py
---

# prefix-code-kraft

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch07-kolmogorov]] (p. 154): halting programs form a prefix-free set, so $\sum2^{-l(p)}\le1$ (Lemma 7.3.1)
- [[mackay-2003-information/ch06-stream]] (pp. 126–127): Exercise 6.18 and 6.22 link codelengths to the Kraft inequality/equality
- [[mackay-2003-information/ch07-codes]] (pp. 134–135): complete code = Kraft equality; any complete code is optimal for the prior it implies
- [[pierce-1980-introduction/ch05-entropy]] (pp. 100–101): prefix property: no code word begins another; allows decoding without a known start (pp. 100–101). Kraft's inequality is not stated here.
- [[polyanskiy-2025-information/ch11-lossless]] (p. 195): if one restricts to prefix-free or uniquely decodable codes, the optimal length is $H(X)+O(1)$
- [[rosvall-2008-maps/main-p1]] (pdf 2): the Huffman code is prefix-free
- [[rosvall-2008-maps/main-p2]]: node codewords appear as binary strings of varying length (e.g. 0, 10, 0001). The pages do not state that the code is prefix-free.
- [[stone-2022-information/appa-glossary]] (p. 244): no codeword is a prefix of another
- [[stone-2022-information/ch03-source]] (p. 59): here only the prefix property (no codeword begins another) is stated, not the Kraft inequality
