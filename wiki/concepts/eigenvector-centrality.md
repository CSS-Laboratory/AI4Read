---
id: eigenvector-centrality
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 1
n_works: 1
tiers: [core]
grounding: digests
sources: [bonacich-1987-power/main]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# eigenvector-centrality

## Canon spine entry

- **eigenvector centrality** (linear-algebra): a node's importance is proportional to the sum of its neighbours' importance; the dominant eigenvector of A (grad)

## Definitions in the sources

### linear-algebra

- [[bonacich-1987-power/main]] (pp. 1172–1173): e: centrality equals summed ties weighted by neighbours' centralities, Re=λe; the limit of c as β→1/λ_max

## Candidate bridges

- [structural-analogy] PageRank ↔ network science: eigenvector centrality — importance depends on importance of in-neighbours; the paper adds a constant term and a division by out-degree. — from [[brin-1998-anatomy/main]] (linear-algebra → complex-systems)
- [structural-analogy] PageRank scores ↔ network science: eigenvector centrality — a node's importance depends on the importance of its neighbours — from [[bryan-2006-eigenvector/main]] (linear-algebra → complex-systems)
- [same-math] Power iteration for the top eigenvector ↔ network analysis: PageRank / eigenvector centrality — the same iteration on a different matrix. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → complex-systems)
- [same-math] Perron vector (positive top eigenvector) ↔ network science: eigenvector centrality of a connected graph is the same top adjacency eigenvector. — from [[spielman-2025-sagt/ch04-adjacency]] (linear-algebra → complex-systems)
- [same-math] Perron's theorem for positive A ↔ network science: eigenvector centrality and PageRank use the dominant positive eigenvector of a nonnegative matrix. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → complex-systems)
