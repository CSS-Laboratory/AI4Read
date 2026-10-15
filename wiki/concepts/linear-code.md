---
id: linear-code
type: concept
fields: [linear-algebra, information-theory]
fields_strong: [linear-algebra, information-theory]
n_sources: 3
n_works: 2
tiers: [deep, reference]
grounding: digests
sources: [polyanskiy-2025-information/ch20-random, spielman-2025-sagt/ch28-brief, spielman-2025-sagt/ch29-expander]
generated_by: build_kg.py
---

# linear-code

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch28-brief]] (p. 232): code whose codewords form a vector space; defined by $M$ or $G$ [new]
- [[spielman-2025-sagt/ch29-expander]] (p. 238): codewords are solutions of linear equations; rate = dimension/length [new]

### information-theory

- [[polyanskiy-2025-information/ch20-random]] (pp. 362–363): a $k$-dimensional subspace of $\mathbb F_q^n$, given by $G$ or $H$; syndrome decoding is ML for additive noise [new]

## Instances that use it

- [[random-linear-code-ensemble]] — average over all binary $\mathbf H$ shows good codes exist — from [[mackay-2003-information/ch14-very]]
- [[hamming-code-7-4-3]] — $[7,4,3]_2$ linear code with explicit $G,H$, corrects 1 bit error — from [[polyanskiy-2025-information/ch20-random]]
- [[random-linear-code]] — good with the stated probability bound — from [[spielman-2025-sagt/ch28-brief]]

## Candidate bridges

- [structural-analogy] Typical-set decoding ↔ Chapter 10's random-code proof: the unit says both use typical sets (p. 228) and contrasts this linear-code proof with Chapter 10's random-code proof. — from [[mackay-2003-information/ch14-very]] (information-theory → other:chapter-10s-random-code)
- [structural-analogy] Random linear codes vs fully random codes ↔ compression: Theorems 11.5 vs 11.8, as the text states (p. 364). — from [[polyanskiy-2025-information/ch20-random]] (information-theory → information-theory)
- [same-math] linear code as column space or null space ↔ linear algebra: range and kernel, here over $\mathbb F_2$ (p. 232) — from [[spielman-2025-sagt/ch28-brief]] (linear-algebra → linear-algebra)
