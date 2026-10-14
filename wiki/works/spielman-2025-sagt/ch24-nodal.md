---
id: spielman-2025-sagt/ch24-nodal
work: spielman-2025-sagt
unit: "Chapter 24 — Nodal Domains"
pages: 196-203
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Nodal Domains

## L0 — One line
The sign pattern of a Laplacian eigenvector is tied to its eigenvalue index: on a weighted path (stated for trees, proved only for paths), if the $k$th eigenvector has no zero entry it has $k-1$ sign changes, and on any weighted connected graph the set where it is non-negative induces at most $k-1$ connected components (proved for threshold $t=0$).

## L1 — The gist (≤ 120 words)
When graphs are drawn using Laplacian eigenvectors, the author says he will show that the subgraphs in the two halves of each drawing are connected; plots show path eigenvectors crossing zero more often as $k$ grows. The chapter proves related, precise results. It proves Sylvester's Law of Inertia, uses it to count negative eigenvalues of paths with signed weights, and derives Fiedler's theorem for weighted paths: if $\psi_k$ has no zero entries (and $\lambda_k$ is simple), exactly $k-1$ edges change sign. After a Perron–Frobenius corollary for matrices with non-positive off-diagonal entries, it proves Fiedler's nodal domain theorem for $t=0$: $\{i:\psi_k(i)\ge 0\}$ induces at most $k-1$ components. The strict version ($>0$) fails on stars. This is the rigorous explanation, promised in the overview, of some of the behaviour seen in eigenvector-based graph drawings.

**Prerequisites:** Laplacian of a weighted graph and $x^TLx=\sum w_{uv}(x(u)-x(v))^2$; Courant–Fischer; eigenvalue interlacing; Perron–Frobenius (Thm 4.5.1, cited here, not restated); block matrices.

## L2 — Key ideas (5–10 bullets)
- A nodal domain is a connected part of the graph on which an eigenvector is positive, or negative (p. 198).
- Sylvester's Law of Inertia: for symmetric $M$ and non-singular $B$, $BMB^T$ and $M$ have equal counts of positive, negative and zero eigenvalues. This is a change of variables, not a similarity (p. 199).
- A weighted path with non-zero, possibly negative weights has as many negative Laplacian eigenvalues as negative weights. A change of variables to edge differences shows this (p. 200).
- For a weighted path whose $\psi_k$ has no zero entry (and $\lambda_k$ simple), exactly $k-1$ edges have $\psi_k(a)\psi_k(b)<0$ (pp. 199–201).
- The key trick: $\Psi_k(L-\lambda_k I)\Psi_k$ is a Laplacian with edge weights $w_{ab}\psi_k(a)\psi_k(b)$ (p. 201).
- Perron–Frobenius transfers to matrices with non-positive off-diagonals (when the graph of non-zero entries is connected), via the smallest eigenvalue (p. 201).
- Fiedler: for $t=0$, $G(W_k)$ has at most $k-1$ components. The proof compares block eigenvalues with those of $L$ using interlacing (pp. 202–203).
- The strict set $\{\psi_k>0\}$ can violate the bound; stars are counterexamples (p. 203).

## L3 — Walkthrough

### 24.1 Overview (pp. 196–198)
- Drawings use $\psi_2$ as horizontal and $\psi_3$ as vertical coordinate. The chapter will show the left and right halves induce connected subgraphs (p. 196).
- Plots of path eigenvectors (unit and random weights in $[0,1]$) show the eigenvector crossing zero more often as its index grows. The author says the $k$th eigenvector 'still changes sign $k$ times' and that he will prove this always happens; he calls these results Fiedler's theorems on nodal domains (p. 198).
- Nodal domains are the connected parts of a graph on which an eigenvector is negative or positive (p. 198).

### 24.2 Sylvester's Law of Inertia (pp. 198–199)
**Claim 24.2.1.** $A$ PSD $\Rightarrow B^TAB$ PSD. Proof: $x^TB^TABx=(Bx)^TA(Bx)\ge0$ (p. 198).

**Theorem 24.2.2.** $M$ symmetric, $B$ non-singular $\Rightarrow$ $BMB^T$ has the same number of positive, negative and zero eigenvalues as $M$ (p. 199).
- Same rank, so same number of zero eigenvalues.
- Show $M$ has at least as many positive eigenvalues as $BMB^T$. Let $\gamma_1\ge\dots\ge\gamma_k>0$ be the positive eigenvalues of $BMB^T$, $Y_k$ the span of their eigenvectors, $S_k=\{B^Ty:y\in Y_k\}$, of dimension $k$ because $B$ is non-singular. With $\alpha_1\ge\dots\ge\alpha_n$ the eigenvalues of $M$, Courant–Fischer gives
$$\alpha_k=\max_{\dim S=k}\min_{x\in S}\frac{x^TMx}{x^Tx}\ge\min_{x\in S_k}\frac{x^TMx}{x^Tx}=\min_{y\in Y_k}\frac{y^TBMB^Ty}{y^TBB^Ty}\ge\frac{\gamma_k y^Ty}{y^TBB^Ty}>0 .$$
- Negative eigenvalues: symmetric argument, or reverse roles using $B^{-1}$ (p. 199).

*Intuition note.* A change of variables $x\mapsto B^Tx$ changes the eigenvalues but not how many are positive, negative or zero. The signs count the directions in which the quadratic form is positive, negative or flat.

### 24.3 Weighted trees (pp. 199–201)
**Theorem 24.3.1 (Fiedler, simplified).** $T$ weighted tree, $0=\lambda_1<\lambda_2\le\dots\le\lambda_n$. If $\psi_k$ has no zero entry, exactly $k-1$ edges $(a,b)$ have $\psi_k(a)\psi_k(b)<0$ (p. 199). Proved only for weighted paths, and only when $\lambda_k$ has multiplicity 1 (pp. 199–200).

**Lemma 24.3.2.** Let $M=\sum_{1\le a<n}w_{a,a+1}L_{a,a+1}$ with all $w_{a,a+1}\neq0$ (negative allowed). Then the number of negative eigenvalues of $M$ equals the number of negative weights (p. 200).
- $x^TMx=\sum_{(u,v)\in E}w_{u,v}(x(u)-x(v))^2$.
- Put $\delta(1)=x(1)$ and $\delta(a)=x(a)-x(a-1)$ for $a>1$. Then $x(a)=\delta(1)+\dots+\delta(a)$, so $x=B\delta$ with $B$ square, full rank.
- By Sylvester, $B^TMB$ has the same inertia as $M$, and $\delta^TB^TMB\delta=\sum_{1\le a<n}w_{a,a+1}\,\delta(a+1)^2$. This matrix has one zero eigenvalue and as many negative eigenvalues as negative weights (p. 200).
- The author notes this also holds for trees.

**Proof of 24.3.1** (assumes $\lambda_k$ has multiplicity 1; the author skips the general case) (p. 200).
- Let $\Psi_k=\mathrm{diag}(\psi_k)$ and $X=\Psi_k(L_P-\lambda_kI)\Psi_k$. $L_P-\lambda_kI$ has one zero and $k-1$ negative eigenvalues. $\Psi_k$ is non-singular, so by Sylvester $X$ has the same counts (p. 200).
- Claim: $X=\sum_{(a,b)\in E}w_{a,b}\psi_k(a)\psi_k(b)L_{a,b}$. Off-diagonal entries agree. Row sums of both are zero: $\Psi_k(L_P-\lambda_kI)\Psi_k\mathbf 1=\Psi_k(\lambda_k\psi_k-\lambda_k\psi_k)=0$ and $L_{u,v}\mathbf1=0$. So diagonals agree (p. 201).
- By Lemma 24.3.2, $X$, and hence $L_P-\lambda_kI$, has as many negative eigenvalues as edges with $\psi_k(a)\psi_k(b)<0$. That number is $k-1$ (p. 201).

*Intuition note.* Rescaling $L-\lambda_kI$ by $\Psi_k$ turns it into a Laplacian whose edge weights are negative exactly where $\psi_k$ changes sign. Counting negative eigenvalues is then counting sign-change edges.

### 24.4 Perron–Frobenius for Laplacians (p. 201)
**Corollary 24.4.1.** $M$ has non-positive off-diagonal entries, and the graph of its non-zero off-diagonal entries is connected. Then its smallest eigenvalue $\lambda_1$ has multiplicity 1 and $v_1$ may be taken strictly positive.
Proof: for large $\sigma$, $B=\sigma I-M$ is non-negative with connected graph. Apply Perron–Frobenius: $\alpha_1$ simple, $v_1>0$; $\lambda_1=\sigma-\alpha_1$.
The author says this also applies to Laplacians and their principal submatrices.

### 24.5 Fiedler's nodal domain theorem (pp. 201–203)
$G(W)$ is the subgraph induced on $W$ (edges with both ends in $W$).

**Theorem 24.5.1.** $G$ weighted, connected; $0=\lambda_1<\lambda_2\le\dots$; $k\ge2$, $t\le0$; $W_k=\{i:\psi_k(i)\ge t\}$. Then $G(W_k)$ has at most $k-1$ connected components (p. 202).

Proof for $t=0$ (the general case needs "additional work", not given) (pp. 202–203):
- $W_k\ne\emptyset$ because $\psi_k\perp\psi_1=\mathbf1$, so $\psi_k$ has positive and negative entries.
- Suppose $c$ components. Order vertices so
$L=\begin{bmatrix}B_1&&&C_1\\&\ddots&&\vdots\\&&B_c&C_c\\C_1^T&\cdots&C_c^T&D\end{bmatrix}$, $\psi_k=(x_1,\dots,x_c,y)$, with $x_i\ge0$ and $y<0$ entrywise. Each $B_i$ has a connected graph; each $C_i\le0$ with at least one negative entry (else $G$ is disconnected).
- $B_ix_i+C_iy=\lambda_kx_i$. $C_iy\ge0$ with some positive entry, so $x_i\ne0$. Then $B_ix_i=\lambda_kx_i-C_iy\le\lambda_kx_i$, hence $x_i^TB_ix_i\le\lambda_kx_i^Tx_i$.
- If $x_i>0$ strictly, $x_i^TC_iy>0$, so the inequality is strict and the smallest eigenvalue of $B_i$ is below $\lambda_k$.
- If $x_i$ has a zero entry, Perron–Frobenius says $x_i$ is not the smallest-eigenvalue eigenvector of $B_i$, so again the smallest eigenvalue of $B_i$ is below $\lambda_k$. (added step: the inequality gives "$\le$"; equality would make $x_i$ a minimal eigenvector.)
- So $\mathrm{diag}(B_1,\dots,B_c)$ has at least $c$ eigenvalues below $\lambda_k$. By eigenvalue interlacing, $L$ has at least $c$ such eigenvalues. Hence $c\le k-1$ (p. 203).

*Intuition note.* Each non-negative piece, taken alone as its block $B_i$, has smallest eigenvalue below $\lambda_k$. $L$ has at most $k-1$ eigenvalues below $\lambda_k$, which limits the number of pieces.

**Strict version fails** (p. 203). Fig. 24.1: star on 5 vertices, eigenvector of $\lambda_2=1$ with values $1,1,1$ on three leaves, $0$ at the centre, $-3$ on the fourth leaf. (added step: $\{\psi_2>0\}$ is three isolated leaves, 3 components $>k-1=1$.)

## Toy example (ours)
Unit-weight path on 3 vertices: $L=\begin{bmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{bmatrix}$, eigenvalues $0,1,3$. Take $k=3$, $\psi_3=(1,-2,1)$: $L\psi_3=(1+2,\,-1-4-1,\,2+1)=(3,-6,3)=3\psi_3$. No zero entries; edge products $1\cdot(-2)=-2<0$ and $(-2)\cdot1=-2<0$, so 2 sign changes $=k-1$.
Check the proof: $\Psi=\mathrm{diag}(1,-2,1)$, $X=\Psi(L-3I)\Psi$ has $X_{11}=-2$, $X_{12}=(1)(-2)(-1)=2$, $X_{22}=4(-1)=-4$, $X_{23}=2$, $X_{33}=-2$, $X_{13}=0$. So $X=-2L=-2L_{12}-2L_{23}$ (the weights are the edge products). Its eigenvalues are $0,-2,-6$: two negative, as many as negative weights.

## Concepts
- [[nodal-domain]] (new) — connected part of the graph on which an eigenvector is positive, or negative (p. 198)
- [[sylvester-law-of-inertia]] (new) — $BMB^T$ has the same counts of $+,-,0$ eigenvalues as $M$ for non-singular $B$ (p. 199)
- [[rayleigh-quotient]] — $x^TMx/x^Tx$; used via Courant–Fischer in the Sylvester proof (p. 199)
- [[graph-laplacian]] — here also with negative edge weights; $x^TMx=\sum w_{uv}(x(u)-x(v))^2$ (p. 200)
- [[perron-frobenius-theorem]] — applied to $\sigma I-M$, giving a simple smallest eigenvalue with positive eigenvector (p. 201)
- [[eigenvalue-interlacing]] (new) — used in Thm 24.5.1 to pass from 'the block-diagonal matrix of the $B_i$ has at least $c$ eigenvalues below $\lambda_k$' to the same for $L$ (p. 203)
- [[positive-semidefinite-matrix]] — $x^TAx\ge0$; preserved by $B^TAB$ (p. 198)
- [[fiedler-vector]] — $\psi_2$ and its sign split, as in the drawings (p. 196)

## Canonical instances
- [[path-graph]] — plots with and without random weights; $\psi_k$ has $k-1$ sign changes when it has no zero entry (proved for $\lambda_k$ simple) (pp. 197–200)
- [[star-graph]] — counterexample for $\{\psi_k>0\}$ (p. 203)

## Bridges (candidates)
- [structural-analogy] Sign split of $\psi_2$ ↔ spectral partitioning/communities: halves are connected pieces (p. 196)
- [metaphor] Counting negative eigenvalues of a signed-weight Laplacian ↔ counting "unstable directions" of a quadratic form

## Questions this raises
- What happens when $\lambda_k$ has multiplicity above 1, or $\psi_k$ has zero entries?
- Does the $k-1$ sign-change count hold for general graphs, or only the component bound?
- How does the general $t\le0$ case differ from $t=0$?

## Reading notes
- Printed = pdf − 24. Source is an incomplete draft (April 2, 2025).
- Overview text says "$k$th eigenvector changes sign $k$ times" (p. 196), but Thm 24.3.1 gives $k-1$ for $\lambda_k$ (with $\lambda_1$ constant); the plots show $v_2,v_3,v_4$ and $v_{10}$ for the unweighted path and $v_2,v_3,v_4$ and $v_{11}$ for a weighted path (p. 197).
- The proof of 24.3.1 switches from $T$ to $P$ ($L_P$). Typos: "Intertia" (p. 200); "non-singluar", "that that" and "We will now a slight simplification" with a missing verb (p. 199).
- Theorem 24.5.1 states "any $t\le0$" but the proof covers $t=0$ only.
- Fig. 24.1 caption says "$\lambda_2=1$" (as printed).
