---
id: power-iteration
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 5
n_works: 4
tiers: [deep, core]
grounding: digests
sources: [bryan-2006-eigenvector/main, deisenroth-2020-mml/ch10-dimensionality, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch35-conjugate, vonluxburg-2007-spectralclustering/main]
raw_ids: [power iteration]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# power-iteration

## Canon spine entry

- **power iteration** (linear-algebra): repeatedly applying A to find the dominant eigenvector; how PageRank is computed (UG)

## Definitions in the sources

### linear-algebra

- [[bryan-2006-eigenvector/main]] (p. 8–9): $x_k=Mx_{k-1}$ (rescaled) converges to the dominant eigenvector; here $\|M^kv\|_1\le c^k\|v\|_1$ on $V$
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 335): $x_{k+1}=Sx_k/\|Sx_k\|$ converges to the top eigenvector [as `power iteration`]
- [[spielman-2025-sagt/ch10-random]] (p. 101): repeated multiplication by W̃
- [[spielman-2025-sagt/ch35-conjugate]] (p. 281): applied to an approximate inverse for the smallest eigenvalue
- [[vonluxburg-2007-spectralclustering/main]] (p. 22): power method mentioned for eigenvectors of sparse Laplacians

## Instances that use it

- [[google-pagerank-power-iteration]] — the original PageRank algorithm uses power iteration on hyperlinks — from [[deisenroth-2020-mml/ch10-dimensionality]]

## Candidate bridges

- [structural-analogy] $T^kv=\lambda^kv$ for eigenvectors (5.59) ↔ Markov matrices / power iteration: steady-state and long-run behaviour from eigen-decomposition — same mechanism, not developed here. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] iteration $x^{(k+1)}=Cx^{(k)}+d$ ↔ power iteration: repeated application of a matrix — both repeat a matrix map until convergence, though the update rules differ. — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] PageRank vector $Ax^*=x^*$ via repeated multiplication $x,Ax,A^2x,\dots$ ↔ power iteration / Markov steady state — same eigenvector equation, with the iteration as described on p. 114. — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → unspecified)
- [same-math] Power iteration for the top eigenvector ↔ network analysis: PageRank / eigenvector centrality — the same iteration on a different matrix. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → complex-systems)
- [same-math] $\|D^{-1/2}p_t\|^2$ decay under $I-\tfrac12N$ ↔ power iteration: components shrink by $\omega_i^t$. — from [[spielman-2025-sagt/ch22-local]] (linear-algebra → linear-algebra)
- [structural-analogy] square the graph to boost the gap ↔ power iteration: squaring a matrix squares the eigenvalues — from [[spielman-2025-sagt/ch30-simple]] (linear-algebra → linear-algebra)
- [metaphor] QR algorithm's repeated "factor, then reverse the factors" ↔ power iteration: both repeatedly apply a matrix until eigen-structure appears. — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → linear-algebra)
