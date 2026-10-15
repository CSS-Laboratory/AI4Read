---
id: fiedler-vector-algebraic-connectivity
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 8
n_works: 2
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch05-fundamental, spielman-2025-sagt/ch06-comparing, spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch25-second, spielman-2025-sagt/ch35-conjugate, vonluxburg-2007-spectralclustering/main]
aliases: [fiedler-vector]
raw_ids: [Fiedler vector / algebraic connectivity]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# fiedler-vector-algebraic-connectivity

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `fiedler-vector` — 3 digest(s)

## Canon spine entry

- **Fiedler vector / algebraic connectivity** (linear-algebra): the eigenvector of the second-smallest Laplacian eigenvalue; splits a graph into communities (grad)

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch01-introduction]] (p. 16): $\lambda_2$ of the Laplacian, proposed by Fiedler as a measure of connectivity; zero iff the graph is disconnected
- [[spielman-2025-sagt/ch03-laplacian]] (p. 30): $\psi_2$ and $\lambda_2$; $\lambda_2>0$ iff connected [as `Fiedler vector / algebraic connectivity`]
- [[spielman-2025-sagt/ch05-fundamental]] (p. 44, 48–49): λ₂, second-smallest Laplacian eigenvalue; bounded here [as `Fiedler vector / algebraic connectivity`]
- [[spielman-2025-sagt/ch06-comparing]] (p. 53): $\lambda_2$ is the quantity being bounded
- [[spielman-2025-sagt/ch24-nodal]] (p. 196): $\psi_2$ and its sign split, as in the drawings [alias `fiedler-vector`]
- [[spielman-2025-sagt/ch25-second]] (p. 204): λ₂ and its eigenvector, used to cut planar graphs and meshes
- [[spielman-2025-sagt/ch35-conjugate]] (p. 281): approximated via $Z$ [alias `fiedler-vector`]
- [[vonluxburg-2007-spectralclustering/main]] (pp. 11, 27): second Laplacian eigenvector; Fiedler (1973) proposed it for bipartition; the author's own derivation is the $k=2$ relaxations [alias `fiedler-vector`]

## Candidate bridges

- [structural-analogy] φ(S) ≤ √(8λ) ↔ linear-algebra: Cheeger-type relation between the spectral gap and a graph cut (Fiedler-vector partitioning) — an eigenvector yields a good cut. — from [[spielman-2025-sagt/ch16-lov]] (linear-algebra → linear-algebra)
- [structural-analogy] $\lambda_2$ bounds cut quality ↔ community detection: spectral bisection with the Fiedler vector — both use the same eigenvalue to measure how separable a network is. — from [[spielman-2025-sagt/ch20-graph]] (linear-algebra → complex-systems)
- [structural-analogy] Rounding $y$ to $x$ and sweeping thresholds ↔ spectral clustering: Fiedler-vector sweep cut. — from [[spielman-2025-sagt/ch22-local]] (linear-algebra → linear-algebra)
- [structural-analogy] signal-plus-noise recovery by the second eigenvector ↔ linear-algebra: Fiedler vector splitting a graph into communities — both read a partition from signs of an eigenvector. — from [[spielman-2025-sagt/ch23-spectral]] (linear-algebra → linear-algebra)
- [structural-analogy] Tanner neighbour growth ↔ community structure: a large λ₂ means no sparse cuts, the opposite of Fiedler-vector clustering. — from [[spielman-2025-sagt/ch27-properties]] (linear-algebra → complex-systems)
