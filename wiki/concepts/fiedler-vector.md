---
id: fiedler-vector
type: concept
fields: [linear-algebra]
n_sources: 3
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch35-conjugate, vonluxburg-2007-spectralclustering/main]
generated_by: build_kg.py
---

# fiedler-vector

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch24-nodal]] (p. 196): $\psi_2$ and its sign split, as in the drawings
- [[spielman-2025-sagt/ch35-conjugate]] (p. 281): approximated via $Z$
- [[vonluxburg-2007-spectralclustering/main]] (pp. 11, 27): second Laplacian eigenvector; Fiedler (1973) proposed it for bipartition; the author's own derivation is the $k=2$ relaxations

## Candidate bridges

- [structural-analogy] φ(S) ≤ √(8λ) ↔ linear-algebra: Cheeger-type relation between the spectral gap and a graph cut (Fiedler-vector partitioning) — an eigenvector yields a good cut. — from [[spielman-2025-sagt/ch16-lov]] (linear-algebra → linear-algebra)
- [structural-analogy] $\lambda_2$ bounds cut quality ↔ community detection: spectral bisection with the Fiedler vector — both use the same eigenvalue to measure how separable a network is. — from [[spielman-2025-sagt/ch20-graph]] (linear-algebra → other)
- [structural-analogy] Rounding $y$ to $x$ and sweeping thresholds ↔ spectral clustering: Fiedler-vector sweep cut. — from [[spielman-2025-sagt/ch22-local]] (linear-algebra → linear-algebra)
- [structural-analogy] signal-plus-noise recovery by the second eigenvector ↔ linear-algebra: Fiedler vector splitting a graph into communities — both read a partition from signs of an eigenvector. — from [[spielman-2025-sagt/ch23-spectral]] (linear-algebra → linear-algebra)
- [structural-analogy] Tanner neighbour growth ↔ community structure: a large λ₂ means no sparse cuts, the opposite of Fiedler-vector clustering. — from [[spielman-2025-sagt/ch27-properties]] (linear-algebra → other)
