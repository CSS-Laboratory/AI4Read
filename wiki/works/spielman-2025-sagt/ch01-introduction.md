---
id: spielman-2025-sagt/ch01-introduction
work: spielman-2025-sagt
unit: Chapter 1 — Introduction
pages: 2–20
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Introduction (Spectral and Algebraic Graph Theory)

## L0 — One line
Eigenvalues and eigenvectors of a graph are meaningful mainly when taken from a natural operator (the diffusion/walk matrix) or a natural quadratic form (the Laplacian), and the chapter's examples are offered to suggest that they carry information about smoothness, connectivity and geometry.

## L1 — The gist (≤ 120 words)
The chapter asks why one should study graphs through matrix spectra, and which matrix to use. The author finds the adjacency matrix the most natural but the least useful. A graph gives a diffusion operator and a Laplacian quadratic form, which measures how smooth a vertex function is. The chapter recalls the spectral theorem for symmetric matrices and shows that the Laplacian is positive semidefinite (all eigenvalues nonnegative). Examples (paths, grids, dodecahedron) and a survey of later topics suggest that low-frequency eigenvectors encode connectivity and give drawings. The topics include isomorphism testing, the Fiedler value (second-smallest Laplacian eigenvalue), expanders (very well connected sparse graphs), graph approximation and Laplacian solvers. Eight linear-algebra exercises close the chapter.

**Prerequisites:** matrix–vector multiplication; eigenvalues and eigenvectors; transpose, orthogonal and permutation matrices; determinant; basic graph vocabulary (vertex, edge, degree).

## L2 — Key ideas (5–10 bullets)
- A matrix is used as an operator ($x \mapsto Mx$) and as a quadratic form ($x \mapsto x^TMx$), not as a spreadsheet (p. 3).
- The adjacency matrix is the most natural but, in the author's view, the least useful; the diffusion matrix $W_G=M_GD_G^{-1}$ and the Laplacian $L_G=D_G-M_G$ are, respectively, the probably most natural operator and the most natural quadratic form (pp. 4–5).
- $x^TL_Gx=\sum w_{a,b}(x(a)-x(b))^2$ measures smoothness, and this makes $L_G$ positive semidefinite (pp. 5–6).
- Symmetric real matrices have an orthonormal eigenbasis with real eigenvalues (Spectral Theorem). Eigenvalues are unique, eigenvectors are not (pp. 5–6).
- For paths, low-frequency eigenvectors resemble low-frequency vibration modes of a string; the highest-frequency one alternates in sign (pp. 7–9).
- Eigenvectors can serve as drawing coordinates; eigenvalues are permutation-invariant, which gives an isomorphism heuristic that does not always work, for example when vertices land on the same spot (pp. 9–15).
- $\lambda_2=0$ iff the graph is disconnected; $\lambda_2$ is proposed as a quantitative measure of connectivity (p. 16).
- The chapter previews expanders, graph approximation, random walks and fast Laplacian solvers (pp. 17–18).

## L3 — Walkthrough

### 1.1 Graphs (pp. 2–3)
A graph $G=(V,E)$ has a vertex set $V$ and edge set $E$. In an undirected graph, $(a,b)=(b,a)$. Unless said otherwise, graphs are undirected, simple (no loops or multiple edges) and finite (p. 2). Unspecified weights are taken as 1. The author calls this an arbitrary choice that has an impact (p. 2). "Vertex" and "node" are used interchangeably (p. 2).

Natural examples: friendship, network, circuit and protein–protein interaction graphs (pp. 2–3). Abstract examples (p. 3):
- Path on $n$ vertices: edges $(i,i+1)$, $1\le i<n$.
- Ring: the path edges plus $(1,n)$.
- Hypercube on $2^k$ vertices: vertices in $\{0,1\}^k$; edges join vertices differing in one coordinate.

### 1.2 Matrices for graphs (pp. 3–5)
The author uses a matrix in two ways: as an operator $x\mapsto Mx$ and as a quadratic form $x\mapsto x^TMx$ (p. 3).

**1.2.1 Spreadsheet.** The adjacency matrix has $M_G(a,b)=1$ if $(a,b)\in E$, else 0. For weighted graphs, $M_G(a,b)=w_{a,b}$ (p. 3). Rows and columns are indexed by vertices, and almost every statement survives renaming vertices (p. 3). The author finds this matrix the least useful, because it is neither a natural operator nor a natural quadratic form (p. 4).

**1.2.2 Operator.** Diffusion: each vertex's "stuff" is spread uniformly over its neighbours, and none stays (p. 4). Degrees are $d=M_G\mathbf 1$. For weighted graphs, "degree" means weighted degree, the sum of incident weights (p. 4). With $D_G$ diagonal and $D_G(a,a)=d(a)$,
$$W_G=M_GD_G^{-1}.$$
If $G$ is regular, $W_G$ is only a rescaling of $M_G$ (p. 4). If $d(a)=0$, set $W_G(a,a)=0$ (p. 4). For $p\in\mathbb R^V$, one step gives $W_Gp$. Check on the unit vector $\delta_a$: $D_G^{-1}\delta_a$ has value $1/d(a)$ at $a$ and 0 elsewhere. So $M_GD_G^{-1}\delta_a$ has value $1/d(a)$ at every neighbour of $a$ and 0 elsewhere (p. 4). The lazy walk, which stays put with probability ½, is
$$\widetilde W_G=I/2+W_G/2.$$
One purpose of spectral theory is to understand repeated application of such an operator (p. 5).

**1.2.3 Quadratic form.** The Laplacian is $L_G=D_G-M_G$. For $x\in\mathbb R^V$ and weights $w_{a,b}>0$:
$$x^TL_Gx=\sum_{(a,b)\in E}w_{a,b}\,(x(a)-x(b))^2.\tag{1.1}$$
It is small when $x$ varies little across edges, so it measures smoothness (p. 5). Laplacians with negative weights are defined only when needed (p. 5).

*Intuition note:* $x^TLx$ adds up squared differences across edges. A function that is nearly constant on connected vertices gets a small value.

### 1.3 Spectral theory (pp. 5–6)
$\psi\neq0$ is an eigenvector with eigenvalue $\lambda$ if
$$M\psi=\lambda\psi.\tag{1.2}$$
Equivalently, $\lambda$ is an eigenvalue iff $\lambda I-M$ is singular. Eigenvalues are the roots of $\det(xI-M)$ (p. 5). Matrices are *similar* if $X^{-1}MX=B$ for a non-singular $X$. Similar matrices have the same eigenvalues (the author leaves this as an exercise) (p. 5).

**Theorem 1.3.1 (Spectral Theorem).** For every real symmetric $n\times n$ matrix $M$, there exist real $\lambda_1,\dots,\lambda_n$ and mutually orthogonal unit vectors $\psi_1,\dots,\psi_n$ with $M\psi_i=\lambda_i\psi_i$ (p. 5).

The author says a non-symmetric matrix might not have $n$ eigenvalues. Even when it has $n$, their eigenvectors will not be orthogonal (p. 5).

Eigenvalues are unique, but eigenvectors are not. $-\psi$ also works. If $\lambda_i=\lambda_{i+1}$, then $\psi_i+\psi_{i+1}$ is also an eigenvector. Eigenvectors of a given eigenvalue are determined only up to an orthogonal transformation (p. 6).

**Definition 1.3.2.** $M\succ0$ (positive definite): symmetric with all eigenvalues positive. $M\succeq0$ (positive semidefinite): symmetric with all eigenvalues nonnegative (p. 6).

**Fact 1.3.3.** $L_G$ is positive semidefinite. *Proof.* For a unit eigenvector $\psi$ of eigenvalue $\lambda$:
$$\psi^TL\psi=\psi^T\lambda\psi=\lambda(\psi^T\psi)=\lambda=\sum_{(a,b)\in E}w_{a,b}(\psi(a)-\psi(b))^2\ge0.$$
(p. 6)

Laplacian eigenvalues are numbered smallest to largest, so $\lambda_1=0$. Small-index ones such as $\lambda_2$ are *low-frequency*; $\lambda_n$ is *high-frequency* (p. 6).

*Intuition note:* Every eigenvalue equals the "roughness" of its unit eigenvector, a sum of squares, so it cannot be negative.

### 1.4 Examples: paths (pp. 6–9)
The 4-vertex path has Laplacian rows $(1,-1,0,0),(-1,2,-1,0),(0,-1,2,-1),(0,0,-1,1)$ (pp. 6–7). For the 10-vertex path, the Laplacian eigenvalues are 0, 0.097887, 0.381966, 0.824429, 1.38197, 2.0, 2.61803, 3.17557, 3.61803, 3.90211 (p. 7).
- The $\lambda_1=0$ eigenvector is constant (every entry ≈ 0.3162) (p. 7).
- The $\lambda_2$ eigenvector is monotone along the path, from 0.4417 down to −0.4417 (p. 7).
- Eigenvectors 2–4 resemble low-frequency vibration modes of a string. The path is a discretization of a string, and its Laplacian discretizes the Laplace operator (pp. 8–9).
- The highest-frequency eigenvector alternates sign at every vertex (p. 9).
- The author says low frequencies will be related to connectivity. High-frequency eigenvectors "may be related" to graph colouring and independent sets (p. 9).

### 1.5 Highlights (pp. 9–18)
**1.5.1 Spectral drawing.** Plot vertex $a$ at $(\psi_2(a),\psi_3(a))$ and draw straight edges. For the 3-by-4 grid this gives a rectangular grid (Fig. 1.1, p. 10). For a Delaunay-triangulation graph on points sampled from the Yale logo, the coordinates are discarded and the graph is redrawn from $\psi_2,\psi_3$ (Figs. 1.2–1.4, pp. 10–12). The middle of the result is almost planar, though edges cross near the boundary (p. 12). The author says this is a great way to draw a graph you know nothing about (p. 12).

**1.5.2 Graph isomorphism.** For a permutation matrix $P$ (with $P^TP=I$):
$$L\psi=\lambda\psi\iff(PLP^T)(P\psi)=PL\psi=\lambda(P\psi).$$
Eigenvalues do not change, and eigenvector entries are permuted (p. 12). A randomly permuted graph drew a picture slightly different from the previous one, flipped vertically, because eigenvectors are determined only up to sign, and only when the multiplicity is 1 (p. 13).

*Heuristic:* (1) If the eigenvalue sets differ, the graphs are not isomorphic. (2) If they match and all multiplicities are 1, draw both. If the pictures agree up to flips and no two vertices land on one spot, aligning them recovers the permutation (p. 13). Since vertices can coincide, this does not always work (p. 13). Chapter 39 will show that if every eigenvalue of $G$ and $H$ has multiplicity 1, isomorphism can be tested efficiently. The method extends to constant-bounded multiplicity [BGM82] (p. 13).

Counter-example (the author notes that some graphs have every non-trivial eigenvalue of large multiplicity, and that Chapter 9 will construct and analyze some, p. 13): the Latin Square Graph on 25 vertices (a Strongly Regular Graph) has Laplacian eigenvalues 0, then 10 (12 times) and 15 (12 times). All Latin Square Graphs of the same size have the same eigenvalues, isomorphic or not (pp. 13–14).

**1.5.3 Platonic solids.** Drawing the dodecahedron skeleton with $\psi_2,\psi_3$ looks squashed, because its smallest nonzero eigenvalue has multiplicity three: 0, 0.763932 (×3), 2 (×5), 3 (×4), 5 (×4), 5.23607 (×3) (p. 14). Three eigenvectors spanning that eigenspace give a canonical 3-D picture (p. 15). The author says this happens for all Platonic solids. With proper re-weighting it happens for every one-skeleton of a convex polytope [Lov01] (p. 15). High-frequency eigenvectors place vertices approximately opposite their neighbours (p. 15).

**1.5.4 The Fiedler value.** Lemma 3.1.1 (proved later): $\lambda_2=0$ iff $G$ is disconnected (p. 16). If $G$ splits into $G_1,G_2$, then $L_G=\begin{pmatrix}L_{G_1}&0\\0&L_{G_2}\end{pmatrix}$. Its eigenvalues are the union, with multiplicity, of those of the blocks, so each block contributes a zero (p. 16). If $G$ is connected and $x$ is non-constant, some edge has $x(a)\ne x(b)$. That edge adds a positive term to (1.1), so only constant vectors give $x^TL_Gx=0$ (p. 16). Fiedler suggested making this quantitative by taking $\lambda_2$ as a measure of how well connected the graph is; it is called the "algebraic connectivity" or Fiedler value. He proved that the further $\lambda_2$ is from 0, the better connected the graph (p. 16). Cheeger's inequality (Chapter 21) is "the ultimate extension". It ties $\lambda_2$ tightly to the ratio (almost) of vertices cut off versus edges removed (p. 16). If $\lambda_2$ is small, then for some threshold $t$ the set $\{i:\psi_2(i)<t\}$ may be removed by cutting many fewer than $|S|$ edges. This spectral partitioning heuristic "has proved very successful in practice" (pp. 16–17). Similarly, the smallest eigenvalue of the diffusion matrix is zero iff the graph is bipartite, and Trevisan [Tre09] related its magnitude to distance from bipartiteness (p. 17).

*Intuition note:* The Laplacian of a disconnected graph inherits a zero eigenvalue from each part, so zero repeats (p. 16). A small $\lambda_2$ points to a poorly connected graph: by Cheeger's inequality, some set can then be cut off by removing few edges (pp. 16–17).

**1.5.5–1.5.11 Previews (pp. 17–18).**
- Bounding eigenvalues: test vectors (§5.4) and comparison with simpler graphs (Ch. 6).
- Planar graphs: nicely drawable graphs have small Fiedler value (Ch. 25). Tutte [Tut63]: reasonably fix a face's vertices and let the others settle with the edges acting as springs, and the result is planar (Ch. 15).
- Random walks (Ch. 16) give a proof of Cheeger's inequality.
- Expanders: roughly, sparse graphs with $\lambda_2$ bounded away from 0 by a constant. Uses: pseudo-random generators and error-correcting codes. Simple construction in Ch. 30. Bipartite Ramanujan graphs in Chs. 43–44.
- Approximation: $G$ approximates $H$ if their Laplacian quadratic forms are close. Expanders are "precisely the sparse graphs" approximating the complete graph (Ch. 27). Sparsification: Chs. 32–33. Low-stretch spanning trees: Ch. 36.
- Motivation: fast solvers for Laplacian systems (finite elements, network flow, machine learning). The approximation notion is designed for Preconditioned Conjugate Gradient.
- Reading advice: assume the graph is connected, unit-weighted, with simple eigenvalues, when first understanding a proof (p. 18).

### 1.6 Exercises (pp. 19–20)
Eight linear-algebra exercises (orthogonal eigenvectors; invariance under permutations and rotations; similarity; spectral decomposition; trace; characteristic polynomial coefficients; reversing products).

## Toy example (ours)
Path on 3 vertices, edges $(1,2),(2,3)$. Degrees: $d=(1,2,1)$. Laplacian $L=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}$.
- Quadratic form for $x=(1,0,-1)$: $(1-0)^2+(0-(-1))^2=2$. Also $Lx=(1,0,-1)=1\cdot x$, so $\lambda=1$ and $x^Tx=2$, $x^TLx/x^Tx=1$.
- $x=(1,-2,1)$: $Lx=(1+2,\,-1-4-1,\,2+1)=(3,-6,3)=3x$, so $\lambda=3$.
- $x=\mathbf 1$: $L\mathbf1=0$, so $\lambda_1=0$. Eigenvalues are 0, 1, 3, all ≥ 0 as Fact 1.3.3 says.
- Low-frequency $(1,0,-1)$ is monotone along the path. High-frequency $(1,-2,1)$ alternates sign, as in §1.4.
- Walk matrix: $W=MD^{-1}$ has columns $(0,1,0)$, $(\tfrac12,0,\tfrac12)$, $(0,1,0)$. Then $W\delta_2=(\tfrac12,0,\tfrac12)$: vertex 2's stuff splits evenly to its two neighbours.

## Concepts
- [[graph-laplacian]] — $L_G=D_G-M_G$; its quadratic form is $\sum w_{a,b}(x(a)-x(b))^2$ (p. 5)
- [[quadratic-form]] — the function $x\mapsto x^TMx$, used here as the second way to use a matrix (p. 3)
- [[adjacency-matrix]] — $M_G(a,b)=1$ if $(a,b)\in E$ (weight if weighted); author calls it least useful (pp. 3–4)
- [[eigenvector-eigenvalue]] — $M\psi=\lambda\psi$, $\psi\ne0$ (p. 5)
- [[characteristic-polynomial]] — $\det(xI-M)$; roots are the eigenvalues (p. 5)
- [[spectral-theorem]] — real symmetric $M$ has real eigenvalues and an orthonormal eigenbasis (p. 5)
- [[positive-semidefinite-matrix]] — symmetric with nonnegative eigenvalues (p. 6)
- [[fiedler-vector-algebraic-connectivity]] — $\lambda_2$ of the Laplacian, proposed by Fiedler as a measure of connectivity; zero iff the graph is disconnected (p. 16)
- [[walk-matrix]] (new) — $W_G=M_GD_G^{-1}$, one diffusion step; lazy version $I/2+W_G/2$ (p. 4)
- [[low-frequency-eigenvector]] (new) — eigenvector for a small Laplacian eigenvalue; on a path its curve resembles a low-frequency vibration mode of a string (pp. 6, 8)
- [[spectral-graph-drawing]] (new) — plot vertex $a$ at $(\psi_2(a),\psi_3(a))$ (p. 10)
- [[eigenvalue-multiplicity]] (new) — repeated eigenvalue; makes eigenvectors non-unique; the drawing-based isomorphism heuristic is stated for multiplicity 1 (pp. 6, 13)
- [[expander-graph]] (new) — roughly, a sparse graph with $\lambda_2$ bounded away from 0 by a constant (p. 17)

## Canonical instances
- [[path-graph]] — $L$ eigenvectors resemble string vibration modes (pp. 6–9)
- [[grid-graph]] — 3-by-4 grid recovered by $\psi_2,\psi_3$ drawing (p. 10)
- [[dodecahedron-graph]] — $\lambda_2$ has multiplicity 3, so draw in 3-D (pp. 14–15)
- [[latin-square-graph]] — same spectrum whether or not the graphs are isomorphic (pp. 13–14)
- [[delaunay-yale-logo-graph]] — spectral drawing of a graph given without coordinates (pp. 10–12)

## Bridges (candidates)
- [same-math] Walk matrix $W_G=M_GD_G^{-1}$ ↔ probability/Markov chains: the author names "probability that a random walk is at that vertex"; each non-isolated vertex's column sums to 1.
- [structural-analogy] Laplacian eigenvectors on a path ↔ physics: vibration modes of a string; the Laplacian discretizes the Laplace operator.
- [structural-analogy] $\psi_2,\psi_3$ as coordinates ↔ PCA: low-dimensional coordinates from eigenvectors, though PCA uses a covariance matrix.
- [structural-analogy] Laplacian quadratic form ↔ smoothness penalty in machine learning (the author mentions ML classification only as a Laplacian-solver application).

## Questions this raises
- Why exactly does the eigenspace of the dodecahedron's smallest nonzero eigenvalue have dimension 3, and what does re-weighting do for general polytopes (Lov01)?
- How tightly does $\lambda_2$ control the best cut (Cheeger's inequality)?
- Which eigenvalue conditions make isomorphism testing efficient, and why do strongly regular graphs resist it?
- How do repeated applications of $W_G$ depend on the spectrum of $W_G$?

## Exercises worth doing
- Ex. 1 (p. 19) — eigenvectors of distinct eigenvalues of a symmetric matrix are orthogonal; needs symmetry — difficulty: easy
- Ex. 2 (p. 19) — permuting vertices permutes eigenvectors and keeps eigenvalues; basis of the isomorphism heuristic — difficulty: easy
- Ex. 5 (p. 19) — spectral decomposition $M=\Psi\Lambda\Psi^T=\sum\lambda_i\psi_i\psi_i^T$ — difficulty: medium
- Ex. 6 (p. 20) — $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ for rectangular matrices; trace equals the sum of eigenvalues — difficulty: medium
- Ex. 8 (p. 20) — $MM^T$ and $M^TM$ share nonzero eigenvalues — difficulty: medium

## Reading notes
- Printed page = pdf page − 24.
- Matrix symbols are bold in the source; they are plain here.
- The set in §1.5.4 is written $S_i=\{i:\psi_2(i)<t\}$ (p. 16): the subscript $i$ is also the bound variable, probably a notation slip.
- Figure 1.3's caption repeats Figure 1.2's ("Dots sampled from the Yale logo") although it shows a graph (p. 11).
- Typo on p. 16: "we will the prove".
- Code listings and numeric outputs are quoted from the page images.
- The dodecahedron's "zero" eigenvalue prints as 3.55271e-15, presumably numerical error (p. 14).
- The text says the $\lambda_2$ eigenvector "increases monotonically" along the path, but the printed values fall from 0.4417 to −0.4417 (p. 7).
- The source is an incomplete draft dated April 2, 2025 (as given in the unit metadata).
