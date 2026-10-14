---
id: spielman-2025-sagt/ch26-planar
work: spielman-2025-sagt
unit: "Chapter 26 — Planar Graphs 2, the Colin de Verdière Number"
pages: 211-217
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Planar Graphs 2, the Colin de Verdière Number

## L0 — One line
For a three-connected planar graph, the Colin de Verdière number is 3 (sketched in the chapter, with one step only cited): a 3D polytope gives a generalized Laplacian whose second eigenvalue has multiplicity 3, and a multiplicity of 4 or more would force a forbidden $K_{3,3}$ minor.

## L1 — The gist (≤ 120 words)
How does planarity show up in the spectrum of Laplacian-like matrices? The Colin de Verdière number cdv(G) is the largest multiplicity of the second-smallest eigenvalue of a "generalized Laplacian" of G (with a technical extra condition). The chapter sketches why cdv(G) = 3 for three-connected planar graphs. Lower bound: build a matrix from a 3D convex polytope realising G, so that its three coordinate vectors lie in its null space. Upper bound: if the multiplicity were at least 4, a nodal-domain argument would produce a $K_{3,3}$ minor, impossible for a planar graph. The chapter links spectra, geometry and forbidden minors.

**Prerequisites:** graph Laplacian and eigenvalue multiplicity; null space; vector cross product in $\mathbb{R}^3$; graph contraction; $K_{3,3}$ (the complete bipartite graph on two sets of 3 vertices); Fiedler's nodal domain theorem (recalled, not proved).

## L2 — Key ideas (5–10 bullets)
- A generalized Laplacian has negative entries on edges, zeros on non-edges, and an arbitrary diagonal. cdv(G) is the maximum multiplicity of its second-smallest eigenvalue, subject to the Strong Arnold Property, a technical condition that the author says is not needed for this lecture's results (pp. 211–212).
- Cited results: cdv ≤ 2 iff outerplanar (planar with every vertex on one face); ≤ 3 iff planar; ≤ 4 iff linkless embeddable. This chapter sketches only two parts of this work, both for three-connected planar graphs (p. 212).
- Steinitz: a three-connected planar graph is the skeleton (vertices and edges) of a 3D convex polytope (p. 213).
- Lower bound: cross products of vertex vectors, together with the vectors $y$ that define the polytope's faces, define the off-diagonal entries. The diagonal is then chosen so the three coordinate vectors lie in the null space (pp. 213–214).
- That the matrix has exactly one negative eigenvalue is stated, not proved. It gives multiplicity 3 for the second-smallest eigenvalue (p. 214).
- Minors of planar graphs are planar, and planar graphs have no $K_{3,3}$ minor; a minor is what remains after removing and contracting edges (p. 214).
- Upper bound: take a minimal-support eigenvector (one whose zero set is not contained in the zero set of another eigenvector of the same eigenvalue) that vanishes on three vertices of a face. Connectivity of its positive and negative sets, plus three disjoint paths, yields a $K_{3,3}$ minor (pp. 215–217).

## L3 — Walkthrough

### 26.1 Introduction (p. 211)
The chapter introduces cdv(G) and sketches why it is 3 for planar graphs. It recalls two facts: three-connected planar graphs are skeletons of 3D convex polytopes, and planar graphs are those with no $K_5$ or $K_{3,3}$ minor (p. 211).

### 26.2 Colin de Verdière invariant (pp. 211–212)
- $M$ is a **generalized Laplacian** of $G=(V,E)$ if $M=L+D$, with $L$ the Laplacian of a weighted version of $G$ and $D$ an arbitrary diagonal matrix. Equivalently: $M(i,j)<0$ if $(i,j)\in E$; $M(i,j)=0$ if $(i,j)\notin E$ and $i\ne j$; $M(i,i)$ arbitrary (p. 211).
- cdv(G) = maximum multiplicity of the second-smallest eigenvalue of such an $M$ satisfying the **Strong Arnold Property**: for every non-zero $n\times n$ matrix $X$ with $X(i,j)=0$ for $i=j$ and $(i,j)\in E$ (as printed), $MX\neq 0$. The author says this restriction is unnecessary for the results proved in this lecture (p. 212).
- Cited: Colin de Verdière proved cdv(G) ≤ 2 iff G is outerplanar (planar with every vertex on one face), and ≤ 3 iff G is planar. Lovász–Schrijver proved ≤ 4 iff G is linkless embeddable (p. 212).
- Two parts are sketched, for three-connected planar G: (1) cdv(G) ≥ 3, by constructing a matrix from the polytope; (2) cdv(G) ≤ 3, by showing no generalized Laplacian has a high-multiplicity second eigenvalue, using minors (p. 212).

### 26.3 Polytopes and planar graphs (pp. 212–213)
- Convex hull of $x_1,\dots,x_n\in\mathbb{R}^d$: $\{\sum_i a_ix_i:\sum_i a_i=1,\ a_i\ge 0\}$. Every convex polytope is the convex hull of its extreme vertices (p. 212).
- Face description: $\{x: y_i^Tx\le 1\ \forall i\}$ is a convex polytope. Every convex polytope with the origin in its interior can be written this way. Face $i$ is the set of polytope points with $y_i^Tx=1$ (p. 212).
- Vertices are points that are not a non-trivial convex combination of other points. Edges are boundary segments between two vertices whose points are not non-trivial combinations of other vertices (pp. 212–213).
- **Theorem 26.3.1 (Steinitz).** For every three-connected planar graph $G=(V,E)$ there are $x_1,\dots,x_n\in\mathbb{R}^3$ such that the segment $x_i x_j$ is an edge of their convex hull iff $(i,j)\in E$ (p. 213).

*Intuition note:* A three-connected planar graph can be drawn as the corners and edges of a solid. The matrix construction uses that solid's geometry.

### 26.4 The Colin de Verdière matrix (pp. 213–214)
Let $v_i\in\mathbb{R}^n$ with $v_i(j)=x_j(i)$ for $i=1,2,3$. The goal is a generalized Laplacian $M$ with $v_1,v_2,v_3$ in its null space (p. 213).

Cross-product facts used: $x\times y=-y\times x$; $(x_1+x_2)\times y=x_1\times y+x_2\times y$; $x\times y=0$ iff $x,y$ are parallel (p. 213).

**Off-diagonal entries.**
1. Edge $(i,j)$ lies on two faces with vectors $y_a,y_b$, so $y_a^Tx_i=y_a^Tx_j=y_b^Tx_i=y_b^Tx_j=1$ (p. 213).
2. Hence $(y_a-y_b)^Tx_i=(y_a-y_b)^Tx_j=0$, so $y_a-y_b$ is parallel to $x_i\times x_j$ (p. 213).
3. If $y_a$ precedes $y_b$ clockwise about $x_i$, then $y_b-y_a$ points the same way as $x_i\times x_j$. Set $M(i,j)$ by
$$M(i,j)\,x_i\times x_j=y_a-y_b,$$
which gives $M(i,j)<0$ (pp. 213–214).

**Diagonal entries.**
4. Define $\hat x_i=\sum_{j\sim i}M(i,j)x_j$. Then
$$x_i\times\hat x_i=x_i\times\sum_{j\sim i}M(i,j)x_j=\sum_{j\sim i}M(i,j)\,x_i\times x_j .$$
5. This sum is made of the differences $y_b-y_a$ for consecutive faces around $x_i$. Going around $x_i$ counter-clockwise, each such vector appears once positively and once negatively, so the sum is 0 (p. 214).
6. So $\hat x_i$ is parallel to $x_i$, and we may set $M(i,i)$ with $M(i,i)x_i+\hat x_i=0$ (p. 214).
7. Then row $i$ of $M$ applied to the stacked coordinates gives $M(i,i)x_i+\sum_{j\sim i}M(i,j)x_j=M(i,i)x_i+\hat x_i=0$. Each coordinate vector $v_k$ is therefore in the null space (p. 214).

The text states, without proof (details in [Lov01]), that $M$ has precisely one negative eigenvalue. Hence the second-smallest eigenvalue (here 0) has multiplicity 3 (p. 214).

*Intuition note:* Around each vertex the cross-product terms cancel, so the weighted sum $\hat x_i$ of its neighbours' vectors is parallel to $x_i$. Choosing the diagonal entry to cancel it puts each coordinate vector in the null space.

### 26.5 Minors of planar graphs (p. 214)
A minor of $G$ is any graph obtained by removing and contracting edges (contracting merges the two endpoints). Every minor of a planar graph is planar (called easy). Kuratowski: $G$ is planar iff it has no $K_5$ or $K_{3,3}$ minor. Only "planar ⇒ no $K_{3,3}$ minor" is used (p. 214).

### 26.6 cdv(G) ≤ 3 (pp. 214–217)
**Setup.** Let $G$ be three-connected. Assume, for contradiction, that a generalized Laplacian $M$ has $\lambda_2$ of multiplicity ≥ 4. The aim is a $K_{3,3}$ minor. Adding a diagonal matrix lets us take $\lambda_2=0$ without loss of generality (p. 215).

**Tool.** Fiedler's nodal domain theorem says that for any $\lambda_2$-eigenvector the non-negative vertices are connected. Van der Holst's variant concerns a $\lambda_2$-eigenvector $v$ of **minimal support**: no other $\lambda_2$-eigenvector $w$ has zero set containing the zero set of $v$. For such $v$, the positive vertices form a connected set, and so do the negative ones (p. 215).

**Argument.**
1. Take a face $F$ and vertices $a,b,c\in F$. Multiplicity ≥ 4 gives a $\lambda_2$-eigenvector vanishing at $a,b,c$. Take one, $v$, of minimal support. Pick $d$ with $v(d)>0$ (p. 215).
2. Three-connectivity gives three vertex-disjoint paths from $d$ to $a$, $b$, $c$ (Menger's Theorem, not covered in the text) (p. 215).
3. Since $v(d)>0$ and $v(a)=0$, some $a'$ on the $d$–$a$ path has $v(a')=0$ and a neighbour $a^+$ with $v(a^+)>0$. As $\lambda_2=0$, $a'$ also has a neighbour $a^-$ with $v(a^-)<0$. Do the same for $b'$ and $c'$ (p. 215; Fig. 26.1).
4. Contract the paths $a$–$a'$, $b$–$b'$, $c$–$c'$. Contract the positive set and the negative set, each to one vertex. Contract every edge of $F$ not involving $a,b,c$. The result has a triangular face $abc$, with each of $a,b,c$ joined to the positive and to the negative supervertex (pp. 215–216).
5. Add a vertex $f$ inside $F$, joined to $a,b,c$. This keeps planarity because $a,b,c$ lie on one face, and $f$ can be added before contracting. Discard all other edges (p. 216; Figs 26.2–26.3).
6. (added step) The remaining graph has $\{a,b,c\}$ each adjacent to each of $\{+,-,f\}$, which is $K_{3,3}$. The text says only "we have constructed a $K_{3,3}$ minor".
7. A planar graph has no such minor, so $G$ is not planar, a contradiction. Therefore cdv(G) ≤ 3 for three-connected planar $G$ (p. 216).

*Intuition note:* Extra freedom in the eigenspace lets us force zeros at three chosen vertices of one face. The sign pattern of the eigenvector then gives a connected positive set, a connected negative set and three paths from $a,b,c$. After contracting these and adding a vertex $f$ in the face, the result is a $K_{3,3}$ minor.

## Toy example (ours, not from the text)
Take $K_4$ (three-connected, planar) as a tetrahedron with $x_1=(1,1,1)$, $x_2=(1,-1,-1)$, $x_3=(-1,1,-1)$, $x_4=(-1,-1,1)$. Their sum is $0$. Pick $M(i,j)=-1$ for all $i\ne j$ (a symmetric choice; not computed from the cross-product recipe).
- $\hat x_1=-(x_2+x_3+x_4)=-(-x_1)=x_1$. So $M(1,1)x_1+\hat x_1=0$ forces $M(1,1)=-1$; the same holds for each $i$.
- Thus $M=-J$ ($J$ = all-ones $4\times4$ matrix).
- The coordinate vectors are $v_1=(1,1,-1,-1)$, $v_2=(1,-1,1,-1)$, $v_3=(1,-1,-1,1)$. Each sums to 0, so $Mv_k=-Jv_k=0$.
- Eigenvalues of $-J$: $-4$ (vector $\mathbf 1$) once, and $0$ three times. So there is exactly one negative eigenvalue, and the second-smallest eigenvalue $0$ has multiplicity 3, as in §26.4.

## Concepts
- [[graph Laplacian]] — here $L$ of a weighted graph; the base of a generalized Laplacian (p. 211)
- [[generalized-laplacian-matrix]] (new) — $M=L+D$: negative on edges, zero on non-edges, free diagonal (p. 211)
- [[colin-de-verdiere-number]] (new) — max multiplicity of the second-smallest eigenvalue of such an $M$ with Strong Arnold Property (p. 212)
- [[strong-arnold-property]] (new) — $MX\ne0$ for non-zero $X$ in the stated pattern; not needed in this lecture (p. 212)
- [[convex-polytope]] (new) — convex hull of finitely many points, or intersection of half-spaces (p. 212)
- [[steinitz-theorem]] (new) — three-connected planar graphs are skeletons of 3D polytopes (p. 213)
- [[graph-minor]] (new) — graph obtained by deleting and contracting edges (p. 214)
- [[eigenvector / eigenvalue]] — used with multiplicity; minimal-support eigenvectors (p. 215)
- [[null space (kernel)]] — contains the three coordinate vectors (p. 213)
- [[nodal-domain-theorem]] (new) — sign-set connectivity for $\lambda_2$-eigenvectors; van der Holst's minimal-support variant (p. 215)

## Canonical instances
- [[k33-minor-from-eigenvector]] — contracting paths and the sign sets of a minimal-support eigenvector gives $K_{3,3}$ (pp. 215–217)
- [[polytope-skeleton-laplacian]] — the matrix built from face vectors and cross products on a polytope (pp. 213–214)

## Bridges (candidates)
- [structural-analogy] Null-space coordinate vectors giving a 3D drawing ↔ spectral graph drawing: low-eigenspace vectors as vertex coordinates.
- [structural-analogy] Minimal-support eigenvector with connected sign sets ↔ Fiedler nodal domains: the same sign-connectivity idea, strengthened.

## Questions this raises
- Why does the construction give exactly one negative eigenvalue, and are $v_1,v_2,v_3$ independent?
- What does the Strong Arnold Property exclude, and why can it be dropped here?
- What happens without three-connectivity (Menger paths, Steinitz)?
- How does the "≤ 2 iff outerplanar" case differ in proof?

## Reading notes
- Printed page = pdf − 24. The chapter opens with a red "This Chapter Needs Editing" note (p. 211).
- The Strong Arnold Property is printed "for $i=j$ and $(i,j)\in E$". Literally "and" would be an odd condition; "or" is probably meant (my reading, not stated).
- Sign inconsistency in §26.4: $M(i,j)x_i\times x_j=y_a-y_b$ is defined first, but the sum is later described as "the difference $y_b-y_a$". This does not affect the zero-sum argument.
- Multiplicity exactly 3 relies on the unproved one-negative-eigenvalue claim and (unstated) independence of $v_1,v_2,v_3$.
- In Fig. 26.1 the label $b'$ is printed "b'" in the image.
