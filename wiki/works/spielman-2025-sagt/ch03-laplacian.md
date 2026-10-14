---
id: spielman-2025-sagt/ch03-laplacian
work: spielman-2025-sagt
unit: "Chapter 3 — The Laplacian and Graph Drawing"
pages: 29-33
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# The Laplacian and Graph Drawing

## L0 — One line
The Laplacian matrix is built so that $x^TLx$ sums squared differences across edges. Hall's method draws a graph using the eigenvectors $\psi_2,\dots,\psi_{k+1}$ for the smallest eigenvalues after 0, which minimize total squared edge length under scale, centring and orthogonality constraints.

## L1 — The gist (≤ 120 words)
The chapter asks how to turn the edge-wise "smoothness" sum $\sum w_{a,b}(x(a)-x(b))^2$ into a matrix. It shows $L=\sum_{(a,b)} w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T$, which equals $D-A$. It proves that the second-smallest eigenvalue $\lambda_2$ is positive exactly when the graph is connected. It then explains Hall's drawing: place each vertex at its entries in $\psi_2,\dots,\psi_{k+1}$. Theorem 3.2.1 proves this choice minimizes total squared edge length among orthonormal, centred coordinate vectors. The author warns that some graphs, such as expanders, do not draw nicely, and that many other drawing methods come without guarantees.

**Prerequisites:** quadratic forms; eigenvectors of symmetric matrices (orthonormal eigenbasis); outer products $uv^T$; Lemma 2.1.1 and Theorem 2.0.1 (cited here, not restated).

## L2 — Key ideas (5–10 bullets)
- The Laplacian is defined by its quadratic form $x^TL_Gx=\sum w_{a,b}(x(a)-x(b))^2$; the matrix is derived from this form (p. 29).
- $L_G$ is a weighted sum of one rank-one matrix per edge, $L_G=\sum w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T$. It agrees with $D_G-A_G$ (pp. 29–30).
- $L\mathbf 1=0$. Constant vectors have eigenvalue 0 and form the whole 0-eigenspace if the graph is connected (p. 30).
- Lemma 3.1.1: $\lambda_2>0$ if and only if $G$ is connected (pp. 30–31).
- Hall's drawing minimizes total squared edge length under scale, centring and orthogonality constraints. These constraints remove degenerate solutions (pp. 31–32).
- Theorem 3.2.1: $\sum_i x_i^TLx_i\ge\sum_{i=2}^{k+1}\lambda_i$, so $\psi_2,\dots,\psi_{k+1}$ are optimal. The proof uses a doubly-stochastic weight matrix (pp. 32–33).
- Hall's drawings are not always nice (expanders). Other drawing methods often lack guarantees, so images should not be over-read (p. 33).

## L3 — Walkthrough

### 3.1 The Laplacian matrix
- **Definition by quadratic form.** For a weighted graph $G=(V,E,w)$ with $w:E\to\mathbb R^+$, the Laplacian is designed so that
$$x^TL_Gx=\sum_{(a,b)\in E}w_{a,b}\,(x(a)-x(b))^2.\tag{3.1}$$
(p. 29)
- **Two-vertex graph $G_{1,2}$ (one edge, weight 1).** $x^TL_{G_{1,2}}x=(x(1)-x(2))^2$ (3.2). Since $x(1)-x(2)=\delta_1^Tx-\delta_2^Tx=(\delta_1-\delta_2)^Tx$,
$$(x(1)-x(2))^2=x^T(\delta_1-\delta_2)(\delta_1-\delta_2)^Tx=x^T\begin{bmatrix}1\\-1\end{bmatrix}\begin{bmatrix}1&-1\end{bmatrix}x=x^T\begin{bmatrix}1&-1\\-1&1\end{bmatrix}x .$$
Hence $L_{G_{1,2}}=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ (p. 29).
- **One edge $(a,b)$ in a larger graph.** $L_{G_{a,b}}=(\delta_a-\delta_b)(\delta_a-\delta_b)^T$. It is zero except in rows and columns $a,b$, where it is the same $2\times2$ block (pp. 29–30).
- **Sum over edges.**
$$L_G=\sum_{(a,b)\in E}w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T=\sum_{(a,b)\in E}w_{a,b}L_{G_{a,b}}.\tag{3.3}$$
The reader is asked to check that this equals $L_G=D_G-A_G$ with $D_G(a,a)=\sum_b w_{a,b}$ (p. 30).
- **Operator view.** With $d(a)=\sum_{(a,b)\in E}w_{a,b}$,
$$(L_Gx)(a)=d(a)x(a)-\sum_{(a,b)\in E}w_{a,b}x(b)=\sum_{(a,b)\in E}w_{a,b}(x(a)-x(b)).\tag{3.4}$$
(p. 30)
- From (3.1), $x^TLx=0$ for constant $x$. From (3.4), $L\mathbf 1=0$. So constant vectors are eigenvectors with eigenvalue 0; if the graph is connected they are the only ones (p. 30).

**Lemma 3.1.1.** Let $0=\lambda_1\le\lambda_2\le\dots\le\lambda_n$ be the eigenvalues of $L$. Then $\lambda_2>0$ iff $G$ is connected (p. 30).
- *Disconnected ⇒ $\lambda_2=0$.* Write $G$ as a disjoint union of $G_1,G_2$ with no edges between them. After reordering vertices, $L=\begin{bmatrix}L_{G_1}&0\\0&L_{G_2}\end{bmatrix}$. Then $L$ has at least two orthogonal eigenvectors of eigenvalue 0: $\begin{bmatrix}\mathbf 0\\\mathbf 1\end{bmatrix}$ and $\begin{bmatrix}\mathbf 1\\\mathbf 0\end{bmatrix}$ (p. 30).
- *Connected ⇒ $\lambda_2>0$.* Let $L\psi=0$. Then $\psi^TL\psi=\sum w_{a,b}(\psi(a)-\psi(b))^2=0$. Weights are positive, so $\psi(a)=\psi(b)$ on every edge. Every pair of vertices is joined by a path, so induction along the path gives $\psi(a)=\psi(b)$ for all $a,b$. Thus $\psi$ is constant and the 0-eigenspace has dimension 1 (pp. 30–31).

*Intuition note.* $x^TLx=0$ means (with positive weights) no edge has a difference across it. On a connected graph, "no difference anywhere" forces a constant vector. If the graph splits, each piece can take its own constant value, so there are more zero modes.

### 3.2 Drawing with Laplacian eigenvalues
- **Line drawing.** Map each vertex to a real number, $x\in\mathbb R^V$. For an unweighted graph, Hall suggested minimizing $x^TLx=\sum_{(a,b)\in E}(x(a)-x(b))^2$ (3.5). Edges would overlap on a line, so the author suggests drawing them as curves or wrapping the line around a circle (p. 31).
- **Constraints.** Unless restrictions are placed on $x$, the solution is degenerate; for example, all vertices could map to 0. So require $\|x\|^2=\sum_a x(a)^2=1$ (3.6). Even with that restriction, another degenerate solution is possible: every vertex could map to $1/\sqrt n$. So also require $\mathbf 1^Tx=\sum_ax(a)=0$ (3.7). (3.7) fixes the shift; together with (3.6) it ensures something interesting (p. 31).
- Since $\mathbf 1$ is the eigenvector of the smallest eigenvalue, Theorem 2.0.1 (cited) implies a unit eigenvector of $\lambda_2$ minimizes $x^TLx$ under (3.6) and (3.7) (p. 31).
- **Two dimensions.** Use coordinates $x,y$. The sum of squared edge lengths is
$$\sum_{(a,b)\in E}\Big\|\binom{x(a)}{y(a)}-\binom{x(b)}{y(b)}\Big\|^2=\sum_{(a,b)\in E}(x(a)-x(b))^2+(y(a)-y(b))^2=x^TLx+y^TLy.$$
Impose $\|x\|^2=\|y\|^2=1$, $\mathbf 1^Tx=\mathbf 1^Ty=0$. This still allows $x=y=\psi_2$, so Hall added the requirement that $x\perp y$. Figs. 1.1, 1.4 and 1.5 were drawn this way (p. 32).
- **$k$ dimensions.** Choose orthonormal $x_1,\dots,x_k\perp\mathbf 1$ minimizing $\sum_ix_i^TLx_i$. A natural choice is $\psi_2,\dots,\psi_{k+1}$, with value $\sum_{i=2}^{k+1}\lambda_i$ (p. 32).

**Theorem 3.2.1** (a variant of [Fan49, Thm 1]). Let $0=\lambda_1<\lambda_2\le\dots\le\lambda_n$ be the eigenvalues of $L$ with orthonormal eigenvectors $\psi_1,\dots,\psi_n$. Let $x_1,\dots,x_k$ be any orthonormal vectors orthogonal to $\mathbf 1$. Then
$$\sum_{i=1}^kx_i^TLx_i\ \ge\ \sum_{i=2}^{k+1}\lambda_i,$$
and this inequality is tight only when $x_i^T\psi_j=0$ for all $j$ with $\lambda_j>\lambda_{k+1}$ (p. 32).
The author notes that "only when $x_i^T\psi_j=0$ for all $j>k+1$" could be wrong if eigenvalues repeat (p. 32).

*Proof* (pp. 32–33):
1. Extend $x_1,\dots,x_k$ to an orthonormal basis $x_1,\dots,x_n$, using an orthonormal basis of the space orthogonal to them. Then $\sum_j(\psi_j^Tx_i)^2=1$ and $\sum_j(x_j^T\psi_i)^2=1$. So the matrix with entries $(\psi_j^Tx_i)^2$ is doubly stochastic (rows and columns sum to 1). The author's footnote says the theorem is really about majorization (p. 32).
2. Take $\psi_1=\mathbf 1/\sqrt n$. For $i\le k$, $\psi_1^Tx_i=0$. By Lemma 2.1.1 (cited),
$$x_i^TLx_i=\sum_{j=2}^n\lambda_j(\psi_j^Tx_i)^2=\lambda_{k+1}+\sum_{j=2}^n(\lambda_j-\lambda_{k+1})(\psi_j^Tx_i)^2\ \ge\ \lambda_{k+1}+\sum_{j=2}^{k+1}(\lambda_j-\lambda_{k+1})(\psi_j^Tx_i)^2 .$$
The middle step uses $\sum_{j=2}^n(\psi_j^Tx_i)^2=1$. The last step drops the terms with $j>k+1$, which are $\ge0$. It is tight only if $(\psi_j^Tx_i)^2=0$ whenever $\lambda_j>\lambda_{k+1}$ (p. 33).
3. Sum over $i$:
$$\sum_{i=1}^kx_i^TLx_i\ge k\lambda_{k+1}+\sum_{j=2}^{k+1}(\lambda_j-\lambda_{k+1})\sum_{i=1}^k(\psi_j^Tx_i)^2\ \ge\ k\lambda_{k+1}+\sum_{j=2}^{k+1}(\lambda_j-\lambda_{k+1})=\sum_{j=2}^{k+1}\lambda_j .$$
The second inequality uses $\lambda_j-\lambda_{k+1}\le0$ and $\sum_{i=1}^k(\psi_j^Tx_i)^2\le1$. The last equality holds because the $k$ terms $-\lambda_{k+1}$ cancel $k\lambda_{k+1}$ (added step). Tightness is under the same conditions as before (p. 33).

*Intuition note.* Each $x_i$ can put weight on the eigenvectors only in total amounts that add up to 1. The cheapest way to spend it is on the smallest nonzero eigenvalues. Orthogonality between the $x_i$ prevents all of them from piling onto $\psi_2$.

**Closing remarks** (p. 33). The author says Hall's pictures suggest that Laplacian eigenvectors reveal much about graph structure. But many graphs do not give nice images with this method, and some cannot be nicely drawn at all; expander graphs are examples. Many other approaches try to minimize some function of edge distances under constraints that keep vertices well separated. Few have compactly describable solutions or provably polynomial-time solutions. The algorithms typically use gradient-based methods that cannot guarantee they actually minimize the function; for many of these methods, relabeling the vertices could produce very different drawings. So one must be careful before inferring truths about a graph from such images.

## Toy example (ours)
Path graph on vertices 1–2–3, unit weights. Using (3.3): $L=\begin{bmatrix}1&-1&0\\-1&1&0\\0&0&0\end{bmatrix}+\begin{bmatrix}0&0&0\\0&1&-1\\0&-1&1\end{bmatrix}=\begin{bmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{bmatrix}$.
- Check: $L(1,0,-1)^T=(1,0,-1)^T$ gives $\lambda_2=1$; $L(1,-2,1)^T=(3,-6,3)^T$ gives $\lambda_3=3$; $\lambda_1=0$.
- $k=1$: $x=(1,0,-1)/\sqrt2$ gives $x^TLx=[(1-0)^2+(0+1)^2]/2=1=\lambda_2$. Another unit vector $\perp\mathbf 1$, $(1,-1,0)/\sqrt2$, gives $[(2)^2+(1)^2]/2=2.5\ge1$, as the theorem says.
- $k=2$: bound is $\lambda_2+\lambda_3=4$. Take $x_1=(1,-1,0)/\sqrt2$ (value 2.5) and $x_2=(1,1,-2)/\sqrt6$ (value $[0^2+3^2]/6=1.5$). They are orthonormal and $\perp\mathbf 1$. The sum is $4$, equal to the bound. This is allowed: no $j$ has $\lambda_j>\lambda_3=3$, so the tightness condition is empty.

## Concepts
- [[graph Laplacian]] — $L_G=D_G-A_G=\sum w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T$, defined to realize (3.1) (p. 29)
- [[quadratic form]] — $x^TLx$ as a sum of weighted squared edge differences (p. 29)
- [[rank-one matrix / outer product]] — each edge contributes $(\delta_a-\delta_b)(\delta_a-\delta_b)^T$ (p. 29)
- [[adjacency matrix]] — $A_G$ in $L=D-A$ (p. 30)
- [[eigenvector / eigenvalue]] — $\mathbf 1$ has eigenvalue 0; $\psi_2,\dots$ give drawing coordinates (p. 30)
- [[Fiedler vector / algebraic connectivity]] — $\psi_2$ and $\lambda_2$; $\lambda_2>0$ iff connected (p. 30)
- [[orthogonality]] — constraints $\mathbf 1^Tx=0$, $x\perp y$ keep drawings non-degenerate (p. 32)
- [[Rayleigh quotient]] — Theorem 2.0.1 (cited) says a unit $\lambda_2$-eigenvector minimizes $x^TLx$ under (3.6)–(3.7) (p. 31)
- [[doubly-stochastic matrix]] (new) — non-negative matrix with all row and column sums 1; here entries $(\psi_j^Tx_i)^2$ (p. 32)
- [[Hall graph drawing]] (new) — coordinates from $\psi_2,\dots,\psi_{k+1}$ minimizing total squared edge length (p. 31)

## Canonical instances
- [[two-vertex-graph-Laplacian]] (new) — $L_{G_{1,2}}=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ derived from $(x(1)-x(2))^2$ (p. 29)
- [[disconnected-graph-block-Laplacian]] (new) — block diagonal $L$ with at least two orthogonal zero-eigenvectors (p. 30)
- [[expander-graphs]] (new) — graphs for which Hall's drawing gives no nice image (p. 33)

## Bridges (candidates)
- [same-math] $x^TLx=\sum_j\lambda_j(\psi_j^Tx)^2$ minimized over orthonormal frames ↔ linear-algebra: Rayleigh quotient / Courant–Fischer — Theorem 3.2.1 is the multi-vector (trace) version.
- [structural-analogy] Hall's constraints ($\|x\|=1$, $\mathbf 1^Tx=0$, $x\perp y$) ↔ PCA: centred, orthonormal directions — both choose orthonormal vectors extremizing a quadratic form.
- [structural-analogy] $\lambda_2>0$ iff connected ↔ network science: a disconnected network has several zero-modes, one per component.

## Questions this raises
- What does the theorem give for disconnected graphs, where $\lambda_2=0$ and the hypothesis $\lambda_1<\lambda_2$ fails?
- Why do expander graphs resist Hall's drawing, and what do their eigenvalues look like?
- What exactly does "majorization" add beyond the inequality proved here?
- Is the 0-eigenspace dimension equal to the number of components in general (the text proves only the two cases)?

## Reading notes
- Printed page = pdf page − 24 (pdf 53–57 = printed 29–33).
- Typo on p. 30: "where it looks looks like".
- Lemma 2.1.1 (the spectral expansion of $x^TLx$) and Theorem 2.0.1 are cited but not shown in these pages; I describe them only as the text uses them.
- Theorem 3.2.1 assumes $\lambda_1<\lambda_2$ (strict) in its statement; the unit does not comment on this.
- The unit contains no exercises.
