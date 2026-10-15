---
id: principal-component-analysis
type: concept
fields: [linear-algebra, political-science]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, grimmer-2022-textasdata/ch14-low, strang-2023-introduction/ch07-singular, vonluxburg-2007-spectralclustering/main]
raw_ids: [principal component analysis]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# principal-component-analysis

## Canon spine entry

- **principal component analysis** (linear-algebra): the SVD of centred data; directions of maximal variance and best-fitting subspaces (UG)

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch04-matrix-p2]] (pp. 132, 136): named as an application of low-rank approximation (Chapter 10) [as `principal component analysis`]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 317): linear dimensionality reduction by projecting centered data onto the top-$M$ eigenvectors of $S$ [as `principal component analysis`]
- [[strang-2023-introduction/ch07-singular]] (p. 302, p. 304): SVD of centred data; $u_1$ gives the closest line, $u_1,u_2$ the closest plane
- [[vonluxburg-2007-spectralclustering/main]] (p. 27): only mentioned as related via kernel matrices

### political-science

- [[grimmer-2022-textasdata/ch14-low]] (p. 261): approximate centered document vectors by $K$ eigenvector components with scores; minimises squared error [new]

## Candidate bridges

- [structural-analogy] SVD directions $e_k$ ↔ statistics: principal component analysis (not stated in this unit) — a possible link, to be confirmed later. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → other)
- [metaphor] representatives as archetypes ↔ principal component analysis: both summarise data by a few prototype vectors, but via different constructions. — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [structural-analogy] Truncated SVD of term-document counts ↔ principal component analysis: keep the dominant directions, treat the rest as noise. The matrix here is not centred. — from [[deerwester-1990-lsa/main]] (linear-algebra → other)
- [same-math] Eckart–Young best rank-$r$ approximation ↔ principal component analysis: truncated canonic form of the data matrix, keep largest components — same decomposition and truncation. — from [[eckart-1936-lowrank/main]] (linear-algebra → other)
- [same-math] sum–difference recoding ↔ statistics: principal component analysis — the source says the recoding is also obtained by PCA. — from [[stone-2022-information/ch11-information]] (information-theory → other)
- [structural-analogy] Choosing a basis that diagonalizes A (U⁻¹AV = Σ) ↔ principal component analysis: finding axes in which a data matrix is simple. — from [[strang-2023-introduction/ch08-linear]] (linear-algebra → other)
