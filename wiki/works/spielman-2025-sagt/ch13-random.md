---
id: spielman-2025-sagt/ch13-random
work: spielman-2025-sagt
unit: "Chapter 13 — Random Spanning Trees"
pages: 122-128
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Random Spanning Trees

## L0 — One line
For a connected weighted graph, $\sigma_{n-1}(L_G)$ equals $n$ times the sum over spanning trees of the product of their edge weights, and a spanning tree drawn with probability proportional to that product contains edge $e$ with probability equal to its leverage score $w_e R_{\rm eff}(e)$.

## L1 — The gist (≤ 120 words)
How can eigenvalues count spanning trees, and how likely is a given edge to lie in a random tree? Spielman first reviews determinants and the elementary symmetric functions $\sigma_k$ of the eigenvalues. He then proves the Matrix-Tree Theorem: $\sigma_{n-1}(L_G)=n\sum_T\prod_{e\in T}w_e$. First he handles a tree, using the factorisation $L_G=U^TWU$; the general case then sums over edge subsets. Next he shows that the matrix $\Gamma=BL_G^+B^T$ is a projection whose diagonal holds the leverage scores. A second determinant argument gives $\Pr[e\in T]=\ell_e$. Since $\Gamma$ has trace $n-1$, the leverage scores sum to $n-1$, the number of edges in a tree.

**Prerequisites:** determinants and the Leibniz formula; eigenvalues; orthogonal projections; Laplacian $L=U^TWU$; pseudoinverse; effective resistance.

## L2 — Key ideas
- $\sigma_k$, the $k$th elementary symmetric function of the eigenvalues, equals the sum of all $k\times k$ principal minors (13.3). The author turns to such functions to measure the volume spanned by $n-1$ vectors in $n$ dimensions (p. 123); for a rank-$k$ matrix, $\sigma_k$ acts as the determinant on its span (p. 124).
- When $A,B$ have rank $k$ and range$(A)\perp$ null$(B)$, $\sigma_k(BA)=\sigma_k(B)\sigma_k(A)$. This is used for symmetric matrices with the same nullspace (p. 124).
- Matrix-Tree Theorem: $\sigma_{n-1}(L_G)=n\sum_T\prod_{e\in T}w_e$. With unit weights the right side is $n$ times the number of spanning trees (p. 124).
- For a tree, every principal minor $\det L_G(S_a,S_a)$ equals $\prod_e w_e$, because the reduced factor $B(:,S_a)$ is triangular after renumbering (p. 125).
- The general proof expands $\sigma_{n-1}(BB^T)$ over edge subsets of size $n-1$. Disconnected subsets contribute 0 and trees contribute $n\prod w_e$ (pp. 125–126).
- $\Gamma=BL_G^+B^T$ is a symmetric projection with trace $n-1$, so $\sum_e\ell_e=n-1$ (pp. 126–127).
- $\Pr[e\in T]=\ell_e$ for weight-proportional random spanning trees (p. 126). The proof reduces to $\|\gamma_e\|^2=\Gamma(e,e)$ (pp. 127–128).

## L3 — Walkthrough

### 13.1–13.2 Determinants (pp. 122–123)
- Leibniz: $\det(A)=\sum_\pi \mathrm{sgn}(\pi)\prod_{i=1}^n A(i,\pi(i))$ (13.1). Also $\det(AB)=\det(A)\det(B)$ (13.2) (p. 122).
- Adding a multiple of one column to another leaves $\det$ unchanged (the text calls this an elementary row operation). Two uses (pp. 122–123):
  1. Reduce to an upper triangular matrix. By (13.1), its determinant is the product of the diagonal entries.
  2. The determinant is the volume of the parallelepiped with axes $a_1,\dots,a_n$. With $\Pi_{a_1}$ the symmetric projection orthogonal to $a_1$: $\det(a_1,\dots,a_n)=\det(a_1,\Pi_{a_1}a_2,\dots,\Pi_{a_1}a_n)$.
- This volume is $\|a_1\|$ times the volume spanned by $\Pi_{a_1}a_2,\dots,\Pi_{a_1}a_n$. Those are $n-1$ vectors in $n$ dimensions, so the volume cannot be written directly as a determinant. The author uses other elementary symmetric functions instead (p. 123).

### 13.3 Characteristic polynomials (pp. 123–124)
- $\det(xI-A)=\sum_{k=0}^n x^{n-k}(-1)^k\sigma_k(A)$, where $\sigma_k(A)=\sum_{|S|=k}\prod_{i\in S}\lambda_i$, with algebraic multiplicity. So $\sigma_1$ is the trace, $\sigma_n$ the determinant, and all are similarity-invariant (p. 123).
- $\sigma_k(A)=\sum_{|S|=k}\det(A(S,S))$ (13.3). The author says this follows from applying Leibniz to $\det(xI-A)$ (p. 123).
- The volume of the parallelepiped of $\Pi_{a_1}a_2,\dots,\Pi_{a_1}a_n$ is written $\sigma_{n-1}(0_n,\Pi_{a_1}a_2,\dots,\Pi_{a_1}a_n)$, the product of the $n-1$ nonzero eigenvalues of this matrix (p. 123).
- $BB^T$ and $B^TB$ share their nonzero eigenvalues, so $\sigma_k(BB^T)=\sigma_k(B^TB)$. Hence the square of that product is the determinant of the square Gram-type matrix $(\Pi a_2;\dots;\Pi a_n)(\Pi a_2,\dots,\Pi a_n)$ (p. 124).
- For $B$ of rank $k$, $\sigma_k(B)$ acts as the determinant of $B$ restricted to its span. If $A,B$ both have rank $k$ and range$(A)\perp$ null$(B)$, then $\sigma_k(BA)=\sigma_k(B)\sigma_k(A)$ (13.4). It will be used for symmetric $A,B$ with the same nullspace (p. 124).

*Intuition note.* For a rank-$k$ matrix, $\sigma_k$ plays the role of a determinant on its span (p. 124). It lets us talk about the volume of a flat object inside a bigger space. (13.4) says the product rule $\sigma_k(BA)=\sigma_k(B)\sigma_k(A)$ holds when $A,B$ have rank $k$ and range$(A)\perp$ null$(B)$.

### 13.4 The Matrix-Tree Theorem (pp. 124–126)
**Theorem 13.4.1.** For connected weighted $G=(V,E,w)$: $\sigma_{n-1}(L_G)=n\sum_{\text{spanning trees }T}\prod_{e\in T}w_e$ (p. 124).

**Lemma 13.4.2.** For a weighted tree, $\sigma_{n-1}(L_G)=n\prod_{e\in E}w_e$ (p. 124).
- With $S_a=V-\{a\}$, (13.3) gives $\sigma_{n-1}(L_G)=\sum_{a\in V}\det L_G(S_a,S_a)$ (p. 124). It suffices to show $\det L_G(S_a,S_a)=\prod_e w_e$ for each $a$ (p. 125).
- Write $L_G=U^TWU$ ($U$ the signed edge-vertex matrix, $W$ the diagonal weights) and $B=W^{1/2}U$. Then $L_G(S_a,S_a)=B(:,S_a)^TB(:,S_a)$ and $\det L_G(S_a,S_a)=\det(B(:,S_a))^2$. $B(:,S_a)$ is square because a tree has $n-1$ edges (p. 125).
- Path example with $a$ the first vertex: $B(:,S_1)$ is lower triangular with diagonal entries $-\sqrt{w_i}$ (p. 125).
- General tree: renumber so $a$ is first and the other vertices are ordered by distance from $a$. Each $c\ne1$ then has exactly one edge $(b,c)$ with $b<c$. Put it in position $c-1$, with weight $w_c$. $B(:,S_a)$ is lower triangular with $-\sqrt{w_c}$ on diagonal $c$, so $\det(B(:,S_a))^2=\prod_{c=2}^n w_c$ (p. 125). Sign changes from renumbering vanish on squaring.
- Summing the $n$ equal terms gives the lemma (added step).

**Proof of 13.4.1** (pp. 125–126):
$$\sigma_{n-1}(L_G)=\sigma_{n-1}(B^TB)=\sigma_{n-1}(BB^T)=\sum_{|S|=n-1,\,S\subseteq E}\sigma_{n-1}(B(S,:)B(S,:)^T)$$
$$=\sum_{|S|=n-1}\sigma_{n-1}(B(S,:)^TB(S,:))=\sum_{|S|=n-1}\sigma_{n-1}(L_{G_S}),$$
using (13.3) at the third equality. $G_S$ has $n-1$ edges, so it is a tree or disconnected. If disconnected, $L_{G_S}$ has at least two zero eigenvalues and $\sigma_{n-1}=0$. If a tree, the lemma gives $n\prod_{e\in T}w_e$. Summing over trees proves the theorem (p. 126).

*Intuition note.* Choosing $n-1$ of the $|E|$ edges either gives a spanning tree or leaves some part cut off. Only trees survive in the sum, each contributing $n\times$ its weight product.

### 13.5 Leverage scores and marginal probabilities (pp. 126–128)
- **Leverage score:** $\ell_e=w_eR_{\rm eff}(e)$, a measure of how important the edge is. If removing $e$ disconnects $G$, then $R_{\rm eff}(e)=1/w_e$ and $\ell_e=1$ (p. 126).
- **Theorem 13.5.1.** If $T$ is chosen with probability proportional to $\prod_{e\in T}w_e$, then $\Pr[e\in T]=\ell_e$ for every edge $e$ (p. 126).
- $\ell_{a,b}=w_{a,b}(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)$. Define $\Gamma=BL_G^+B^T$, indexed by edges, with $\Gamma(e,e)=\ell_e$ and $\Gamma((a,b),(c,d))=\sqrt{w_{a,b}}\sqrt{w_{c,d}}(\delta_a-\delta_b)^TL_G^+(\delta_c-\delta_d)$ (p. 126).
- **Claim 13.5.2.** $\Gamma$ is a symmetric projection with trace $n-1$. Proof: it is symmetric, and to show it is a projection it suffices to show that all its eigenvalues are 0 or 1. Apart from zero eigenvalues, it has the same eigenvalues as $L_G^+B^TB=L_G^+L_G=\Pi$, the projection orthogonal to the all-ones vector. $\Pi$ has $n-1$ eigenvalues equal to 1, so $\Gamma$ does too (p. 127).
- Hence $\sum_e\ell_e=n-1$. This is consistent with Theorem 13.5.1, since each spanning tree has $n-1$ edges (p. 127).
- Since $\Gamma=\Gamma^2$: $\Gamma(e,e)=\|\Gamma(e,:)\|^2$. If we flow 1 unit from $a$ to $b$, the potential difference between $c$ and $d$ is $(\delta_a-\delta_b)^TL_G^+(\delta_c-\delta_d)$; plugging these potentials into the Laplacian quadratic form gives the effective resistance. So the formula says $w_{a,b}R_{{\rm eff}\,a,b}=w_{a,b}\sum_{(c,d)\in E}w_{c,d}\big((\delta_a-\delta_b)^TL_G^+(\delta_c-\delta_d)\big)^2$ (p. 127).

**Proof of 13.5.1** (pp. 127–128):
$$\Pr_T[e\in T]=\sum_{T\ni e}\frac{\sigma_{n-1}(L_{G_T})}{\sigma_{n-1}(L_G)}=\sum_{T\ni e}\sigma_{n-1}(L_{G_T})\,\sigma_{n-1}(L_G^+)=\sum_{T\ni e}\sigma_{n-1}(L_{G_T}L_G^+),$$
the last step by (13.4). Non-tree edge sets of size $n-1$ contribute 0, so this equals $\sum_{|S|=n-1,\,e\in S}\sigma_{n-1}(L_{G_S}L_G^+)$ (p. 127). Each term is
$$\sigma_{n-1}(B(:,S)B(:,S)^TL_G^+)=\sigma_{n-1}(B(:,S)^TL_G^+B(:,S))=\sigma_{n-1}(\Gamma(S,S))=\sigma_{n-1}(\Gamma(S,:)\Gamma(:,S)).$$
Let $\gamma_e=\Gamma(e,:)$. Because $e\in S$,
$$\sigma_{n-1}(\Gamma(S,:)\Gamma(:,S))=\|\gamma_e\|^2\sigma_{n-2}(\Gamma(S,:)\Pi_{\gamma_e}\Gamma(:,S))=\|\gamma_e\|^2\sigma_{n-2}((\Gamma\Pi_{\gamma_e}\Gamma)(S,S)).$$
As $\gamma_e$ lies in the span of $\Gamma$, $\Gamma\Pi_{\gamma_e}\Gamma$ is a symmetric projection onto an $(n-2)$-dimensional space, so $\sigma_{n-2}(\Gamma\Pi_{\gamma_e}\Gamma)=1$. Then
$$\sum_{|S|=n-1,\,e\in S}\sigma_{n-1}(L_{G_S}L_G^+)=\|\gamma_e\|^2\sum_{|S|=n-1,\,e\in S}\sigma_{n-2}((\Gamma\Pi_{\gamma_e}\Gamma)(S,S))=\|\gamma_e\|^2\sigma_{n-2}(\Gamma\Pi_{\gamma_e}\Gamma)=\|\gamma_e\|^2=\ell_e.$$
The step from the sum of minors to $\sigma_{n-2}(\Gamma\Pi_{\gamma_e}\Gamma)$ (the third equality of the source's display) is stated without comment. (added step) Row $e$ of $\Gamma\Pi_{\gamma_e}\Gamma$ is zero, so any $(n-2)$-minor involving $e$ vanishes. Each remaining minor, indexed by $R\not\ni e$, appears once, for $S=R\cup\{e\}$ (p. 128).

*Intuition note.* The tree-probability becomes a ratio of volumes. After "removing the base" $\gamma_e$, what remains is a projection of rank $n-2$ with $\sigma_{n-2}=1$, and only the squared length $\|\gamma_e\|^2=\ell_e$ is left.

## Toy example (ours)
Triangle $K_3$, unit weights, $n=3$.
- $L=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}$ has eigenvalues $0,3,3$. So $\sigma_2=3\cdot3=9$.
- The triangle has 3 spanning trees (drop one edge), each with weight product 1. The theorem gives $n\cdot3=9$ ✓.
- Check with (13.3): deleting a vertex leaves $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, $\det=4-1=3$. Summing over 3 vertices gives 9 ✓.
- $R_{\rm eff}$ of an edge: resistance 1 in parallel with a path of resistance 2, so $\frac{1\cdot2}{1+2}=\frac23$. Hence $\ell_e=\frac23$.
- Each edge lies in 2 of the 3 trees, so $\Pr[e\in T]=\frac23$ ✓. The three leverage scores sum to $2=n-1$ ✓.

## Concepts
- [[characteristic-polynomial]] — $\det(xI-A)=\sum x^{n-k}(-1)^k\sigma_k(A)$ (p. 123)
- [[elementary-symmetric-eigenvalue-function]] (new) — $\sigma_k(A)=\sum_{|S|=k}\prod_{i\in S}\lambda_i=\sum_{|S|=k}\det A(S,S)$ (p. 123)
- [[determinant]] — volume of a parallelepiped; $\sigma_k$ acts as the determinant on a rank-$k$ span (pp. 123–124)
- [[projection]] — here $\Pi_{a}$ and $\Gamma$ are symmetric projections (pp. 123, 127)
- [[graph-laplacian]] — $L_G=U^TWU=B^TB$ (p. 125)
- [[incidence-matrix]] — $U$, the signed edge-vertex matrix (p. 125)
- [[pseudoinverse]] — $L_G^+$ with $L_G^+L_G=\Pi$ (p. 127)
- [[matrix-tree-theorem]] (new) — $\sigma_{n-1}(L_G)=n\sum_T\prod_{e\in T}w_e$ (p. 124)
- [[leverage-score]] (new) — $\ell_e=w_eR_{\rm eff}(e)=\Gamma(e,e)$ (p. 126)
- [[effective-resistance]] (new) — $(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)$ (p. 126)

## Canonical instances
- [[weighted-path-graph]] — $B(:,S_1)$ is lower triangular with diagonal $-\sqrt{w_i}$ (p. 125)
- [[bridge-edge]] — an edge whose removal disconnects $G$ has $\ell_e=1$ (p. 126)

## Bridges (candidates)
- [same-math] $\sigma_{n-1}(L_G)$ and principal minors of $L_G$ ↔ combinatorics: counting spanning trees by determinants, as in the Matrix-Tree Theorem.
- [structural-analogy] Edge leverage $\ell_e=\Gamma(e,e)$, diagonal of a projection ↔ statistics: hat-matrix leverage in regression. Both are diagonal entries of a projection matrix.
- [structural-analogy] Random spanning tree marginals ↔ network robustness: an edge whose removal disconnects $G$ has $\ell_e=1$ (p. 126), so by Theorem 13.5.1 it lies in every spanning tree.

## Questions this raises
- How can one sample a spanning tree with probability proportional to $\prod w_e$ efficiently?
- Are the events "$e\in T$" and "$f\in T$" correlated, and how do the off-diagonal entries of $\Gamma$ relate to that?
- Why is the sum $\sum_e\ell_e=n-1$ useful for sparsifying graphs? (The text does not say.)

## Reading notes
- Printed page = pdf − 24. The work citation describes the source as an incomplete draft dated April 2, 2025 (not stated on these pages).
- p. 127 contains an unresolved reference "Section ??".
- Text calls adding a multiple of a column an "elementary row operation" (p. 122).
- Notation shifts in the proof of 13.5.1. $L_{G_S}$ is written $B(:,S)B(:,S)^T$ although $B$ was defined with edges as rows, so the intended meaning is presumably $B(S,:)^TB(S,:)$, as on p. 125. I kept the source's notation.
- The proof of 13.5.1 cites (13.4) without discussing its hypotheses. On p. 124 the author says he will use (13.4) for symmetric matrices with the same nullspace.
- Exercise 3 of Lecture 2 is cited but is not in this unit. The unit has no exercises of its own.
