---
id: huffman-arithmetic-coding
type: concept
fields: [information-theory, bayesian, complex-systems]
fields_strong: [information-theory, bayesian, complex-systems]
n_sources: 14
n_works: 7
tiers: [core, reference, deep]
grounding: digests
sources: [cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch06-gambling, mackay-2003-information/ch05-symbol, mackay-2003-information/ch06-stream, mackay-2003-information/ch17-communication, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch07-efficient, polyanskiy-2025-information/ch12-variable, polyanskiy-2025-information/ch15-universal, rosvall-2008-maps/main-p1, shannon-1948-mathematical/main-p1, stone-2022-information/ch03-source, stone-2022-information/ch11-information]
raw_ids: [Huffman / arithmetic coding]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# huffman-arithmetic-coding

## Canon spine entry

- **Huffman / arithmetic coding** (information-theory): practical codes that approach the entropy bound (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch05-data-p1]] (pp. 92–94): Huffman: repeatedly merge the two least probable symbols; optimal prefix code
- [[cover-2006-elements/ch05-data-p2]] (pp. 101, 104–106): Huffman: greedy optimal code (Theorem 5.8.1); arithmetic: sequential block coding via $p(x^n)$, $F(x^n)$
- [[cover-2006-elements/ch06-gambling]] (p. 138): gambler's bets used as the distribution for arithmetic coding
- [[mackay-2003-information/ch05-symbol]] (pp. 99, 101): Huffman: optimal symbol code by merging the two least probable symbols; arithmetic coding is announced as the fix for its defects [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (p. 112): here, arithmetic coding: a string is identified with a sub-interval of [0,1) of width equal to its model probability [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch17-communication]] (p. 255): arithmetic-code decoders serve as "sparsifiers" [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch05-entropy]] (pp. 94–97): Huffman code: always less than one digit per symbol above $H$
- [[pierce-1980-introduction/ch07-efficient]] (pp. 127–128): Huffman coding of long blocks brings digits per character near entropy, but Pierce shows a case where it is pointless
- [[polyanskiy-2025-information/ch12-variable]] (p. 210–211): Huffman is optimal among prefix/UD codes with $L^*\in[H,H+1]$; arithmetic coding and Lempel–Ziv are deferred [as `Huffman / arithmetic coding`]
- [[polyanskiy-2025-information/ch15-universal]] (pp. 245–246): arithmetic coding: sequential encoding of $x^n$ as the largest dyadic interval inside its $Q$-interval, length at most $\lceil\log\frac1Q\rceil+1$
- [[rosvall-2008-maps/main-p1]] (pdf 2): Huffman code gives short words to frequent nodes; used to illustrate codes [work fields: information-theory, complex-systems]
- [[shannon-1948-mathematical/main-p1]] (p. 18): (canon link; not stated in this unit: Huffman coding is not named; this is a Shannon–Fano-type code) here the cumulative-probability binary code and Fano's method, substantially the same apart from minor differences (p. 17); the 0/10/110/111 code [weak: not really used in this unit]
- [[stone-2022-information/ch03-source]] (pp. 57–59): Huffman coding built by repeatedly merging the two least probable symbols; Huffman codes are prefix codes
- [[stone-2022-information/ch11-information]] (p. 218): Huffman coding is the text's example of recoding so that symbols occur equally often
