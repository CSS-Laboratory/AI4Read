---
id: kolmogorov-complexity
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 5
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch07-kolmogorov, murphy-2023-pml2/ch05-information-p2, stone-2022-information/appa-glossary, stone-2022-information/ch03-source]
aliases: [kolmogorov-complexity-kx]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# kolmogorov-complexity

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `kolmogorov-complexity-kx` — 1 digest(s)

## Canon spine entry

- **Kolmogorov complexity K(x)** (information-theory): the length of the shortest program that outputs x; information content of an individual object (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 3): length of shortest program printing the string [as `Kolmogorov complexity K(x)`; alias `kolmogorov-complexity-kx`]
- [[cover-2006-elements/ch07-kolmogorov]] (p. 147): K(x): length of the shortest program printing x (and halting) on a universal computer; the shortest-program definition (7.1)
- [[stone-2022-information/appa-glossary]] (p. 243): fewest binary digits to represent an entity
- [[stone-2022-information/ch03-source]] (pp. 76–78): length of the shortest program that generates an object; non-computable

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (p. 256): length of the shortest program producing a string on a universal Turing machine; uncomputable [new; work fields: bayesian, information-theory]

## Candidate bridges

- [structural-analogy] Lempel–Ziv universality (no source model needed) ↔ Kolmogorov complexity / universal coding: both compress without knowing the source. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → information-theory)
- [structural-analogy] Complexity as description length in a meta-language ↔ Kolmogorov complexity / MDL: the paper cites [46,129] and notes the dependence on the meta-language. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
