---
id: centrality
type: concept
fields: [political-science, communication-theory]
fields_strong: [political-science, communication-theory]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [converse-1964-beliefsystems/ch01-introduction, converse-1964-beliefsystems/ch03-sections, katz-1955-personalinfluence/ch06-interpersonal]
generated_by: build_kg.py
---

# centrality

## Definitions in the sources

### political-science

- [[converse-1964-beliefsystems/ch01-introduction]] (p. 4): role of an element; the element more likely to change when elements clash is, by definition, the less central one [new]
- [[converse-1964-beliefsystems/ch03-sections]] (p. 45): how central a belief or object is within a person's belief system. Centrality and temporal stability are said to be "highly related" [new]

### communication-theory

- [[katz-1955-personalinfluence/ch06-interpersonal]] (pp. 111–112): Leavitt: degree of a member's access to all others; the major determinant of leadership where the structure gave one member high centrality [new]

## Instances that use it

- [[bavelas-leavitt-wheel]] — wheel, chain, circle and centrality — from [[katz-1955-personalinfluence/ch06-interpersonal]]

## Candidate bridges

- [same-math] $(I-T)^{-1}=I+T+\dots+T^{m-1}$ for nilpotent $T$ (Exercise 8A.17) ↔ linear-algebra: Katz–Bonacich centrality $(I-\beta A)^{-1}$ for an acyclic-graph adjacency matrix (finite walk count) — same Neumann series. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [structural-analogy] PageRank ↔ network science: eigenvector centrality — importance depends on importance of in-neighbours; the paper adds a constant term and a division by out-degree. — from [[brin-1998-anatomy/main]] (linear-algebra → complex-systems)
- [structural-analogy] PageRank scores ↔ network science: eigenvector centrality — a node's importance depends on the importance of its neighbours — from [[bryan-2006-eigenvector/main]] (linear-algebra → complex-systems)
- [same-math] Power iteration for the top eigenvector ↔ network analysis: PageRank / eigenvector centrality — the same iteration on a different matrix. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → complex-systems)
- [structural-analogy] Leavitt's "centrality" ↔ network analysis: node centrality — both ask how much access a position has to the rest of a network; this unit gives no formula. — from [[katz-1955-personalinfluence/ch06-interpersonal]] (communication-theory → complex-systems)
- [structural-analogy] Opinion leaders as central, norm-conforming nodes ↔ network analysis: high-centrality nodes relaying influence. — from [[rogers-2003-diffusion/ch01-elements-p2]] (communication-theory → complex-systems)
- [same-math] Perron vector (positive top eigenvector) ↔ network science: eigenvector centrality of a connected graph is the same top adjacency eigenvector. — from [[spielman-2025-sagt/ch04-adjacency]] (linear-algebra → complex-systems)
- [structural-analogy] $(I-B)^{-1}=I+\sum B^i$ ↔ Katz–Bonacich centrality: both are walk-counting series. — from [[spielman-2025-sagt/ch11-walks]] (linear-algebra → linear-algebra)
- [same-math] Perron's theorem for positive A ↔ network science: eigenvector centrality and PageRank use the dominant positive eigenvector of a nonnegative matrix. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → complex-systems)
