---
id: adjacency-matrix
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 24
n_works: 6
tiers: [deep, core, reference]
grounding: digests
sources: [bonacich-1987-power/main, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch10-matrix, deisenroth-2020-mml/ch04-matrix-p1, prince-2023-udl/ch13-graph, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch04-adjacency, spielman-2025-sagt/ch07-cayley, spielman-2025-sagt/ch08-eigenvalues, spielman-2025-sagt/ch09-strongly, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch19-independent, spielman-2025-sagt/ch23-spectral, spielman-2025-sagt/ch29-expander, spielman-2025-sagt/ch30-simple, spielman-2025-sagt/ch38-fast, spielman-2025-sagt/ch39-testing, spielman-2025-sagt/ch40-testing, spielman-2025-sagt/ch43-ramanujan, spielman-2025-sagt/ch44-bipartite, spielman-2025-sagt/ch45-matching, vonluxburg-2007-spectralclustering/main]
raw_ids: [adjacency matrix]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# adjacency-matrix

## Canon spine entry

- **adjacency matrix** (linear-algebra): Aᵢⱼ = 1 if i links to j; (Aᵏ)ᵢⱼ counts walks of length k (UG)

## Definitions in the sources

### linear-algebra

- [[bonacich-1987-power/main]] (pp. 1172, 1174, 1178): R, with R_ij=1 if a relation exists and zero diagonal; powers Rᵏ count paths
- [[boyd-2018-vmls/ch06-matrices]] (p. 112): $A_{ij}=1$ if $(i,j)\in\mathcal R$, else 0; the reverse convention also exists [as `adjacency matrix`]
- [[boyd-2018-vmls/ch07-matrix]] (p. 133): related but different from incidence; does not explicitly label edges [as `adjacency matrix`]
- [[boyd-2018-vmls/ch10-matrix]] (pp. 186–187): here $A_{ij}=1$ if there is an edge from j to i; $(A^\ell)_{ij}$ counts paths of length ℓ from j to i [as `adjacency matrix`]
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 110): $a_{ij}=1$ if neuron $i$ synapses onto $j$; symmetrised as $A+A^\top$ [as `adjacency matrix`]
- [[spielman-2025-sagt/ch01-introduction]] (pp. 3–4): $M_G(a,b)=1$ if $(a,b)\in E$ (weight if weighted); author calls it least useful
- [[spielman-2025-sagt/ch03-laplacian]] (p. 30): $A_G$ in $L=D-A$ [as `adjacency matrix`]
- [[spielman-2025-sagt/ch04-adjacency]] (p. 34): acts by $(Mx)(a)=\sum_{b\sim a}w_{a,b}x(b)$, eigenvalues ordered decreasingly here
- [[spielman-2025-sagt/ch07-cayley]] (p. 68): used in 7.8; Laplacian shares eigenvectors since graphs are regular
- [[spielman-2025-sagt/ch08-eigenvalues]] (p. 70): $M$; here split as $p(J-I)+R$
- [[spielman-2025-sagt/ch09-strongly]] (p. 85): $(A^2)_{uv}$ counts common neighbours
- [[spielman-2025-sagt/ch10-random]] (p. 93): M, the (weighted) adjacency matrix
- [[spielman-2025-sagt/ch19-independent]] (p. 164): eigenvalues indexed $\mu_1\ge\dots\ge\mu_n$, reversed from the Laplacian
- [[spielman-2025-sagt/ch23-spectral]] (p. 190): here $M$, random, with entries 1 on edges
- [[spielman-2025-sagt/ch29-expander]] (p. 237): here $A$ of $G$; the double cover has $\begin{pmatrix}0&A\\A&0\end{pmatrix}$
- [[spielman-2025-sagt/ch30-simple]] (p. 244): M_G; M² counts length-2 paths
- [[spielman-2025-sagt/ch38-fast]] (p. 305): $A-C$ is the adjacency matrix of the graph whose Laplacian is $L$ [as `adjacency matrix`]
- [[spielman-2025-sagt/ch39-testing]] (p. 307): the matrix used here to encode graphs [as `adjacency matrix`]
- [[spielman-2025-sagt/ch40-testing]] (p. 319): $(A^2)_{ab}$ counts common neighbours; used to get $A^2=(\alpha-\beta)A+\beta J+(d-\beta)I$
- [[spielman-2025-sagt/ch43-ramanujan]] (p. 342): $M$ for a perfect matching; sums $\sum\Pi_iM\Pi_i^T$ give $d$-regular multigraphs
- [[spielman-2025-sagt/ch44-bipartite]] (p. 350): A of G; its spectrum is related to that of S through the 2-lift [as `adjacency matrix`]
- [[spielman-2025-sagt/ch45-matching]] (p. 359): $A_G$ of the graph, used in $\chi_x(A_G)$
- [[vonluxburg-2007-spectralclustering/main]] (p. 2): here a weighted symmetric $W$ with $w_{ij}\ge0$

### llm

- [[prince-2023-udl/ch13-graph]] (pp. 244–245): $N\times N$ binary matrix of edges; $\mathbf{A}^L$ counts walks of length $L$ [new]

## Candidate bridges

- [structural-analogy] Fibonacci via diagonalization (Ex. 21) ↔ adjacency matrix: counting walks via $A^k$ by diagonalizing $A$. — from [[axler-2024-ladr/ch05-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [same-math] $(I-T)^{-1}=I+T+\dots+T^{m-1}$ for nilpotent $T$ (Exercise 8A.17) ↔ linear-algebra: Katz–Bonacich centrality $(I-\beta A)^{-1}$ for an acyclic-graph adjacency matrix (finite walk count) — same Neumann series. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [same-math] Adjacency matrix $A_{ij}$ ↔ network analysis: the graph as a table of 0/1 ties, where $A=A^T$ means an undirected network. — from [[boyd-2018-vmls/ch06-matrices]] (linear-algebra → complex-systems)
- [same-math] Matrix powers of the adjacency matrix ↔ graph theory/network science: counting walks of length ℓ — the same entries $(A^\ell)_{ij}$. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → complex-systems)
- [structural-analogy] Trace method: $\mathrm{Tr}\,R^l$ as a sum over closed walks ↔ adjacency matrix: $(A^k)_{ij}$ counts walks of length $k$ — same expansion, but weighted by random entries here. — from [[spielman-2025-sagt/ch08-eigenvalues]] (linear-algebra → linear-algebra)
- [structural-analogy] $B=D^{-1/2}AD^{-1/2}$ ↔ graph theory: normalized adjacency matrix — similar form, but here $D$ need not be the degree matrix and $A$ may have diagonal entries. — from [[spielman-2025-sagt/ch38-fast]] (linear-algebra → other:graph-theory)
