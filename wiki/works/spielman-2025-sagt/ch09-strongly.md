---
id: spielman-2025-sagt/ch09-strongly
work: spielman-2025-sagt
unit: Chapter 9 — Strongly Regular Graphs
pages: 83-90
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Strongly Regular Graphs

## L0 — One line
A connected regular graph is strongly regular exactly when its adjacency matrix has at most three distinct eigenvalues, and then the eigenvalues other than $k$ are the two roots of one quadratic; the eigenspaces give a two-distance point set whose dimension is at least $\sqrt{2n}-2$.

## L1 — The gist (≤ 120 words)
Which graphs have very few adjacency eigenvalues, and what does that force? A graph is strongly regular if it is $k$-regular and every adjacent pair has $\lambda$ common neighbours and every non-adjacent pair has $\mu$. Writing $A^2$ in terms of $A$, $I$, $J$ shows that the eigenvalues other than $k$ solve a quadratic; conversely, a connected regular graph with at most three eigenvalues is strongly regular. Unless the multiplicities $f,g$ of the two roots are equal, the two roots are integers. An eigenspace gives a two-distance point set, and a polynomial-counting argument bounds its dimension from below. This matters because strongly regular graphs are extremal in several ways, and the author says they have supplied a reasonable answer to requests for a "random-looking" 0/1 matrix.

**Prerequisites:** adjacency matrix and $A^2$ as common-neighbour counts; eigenvalues of symmetric matrices; orthogonal projections; Gram matrix; linear independence.

## L2 — Key ideas (5–10 bullets)
- Strongly regular means regular plus constant common-neighbour counts $\lambda$ (adjacent pairs) and $\mu$ (non-adjacent pairs) (p. 83).
- Examples: pentagon, lattice graphs, Latin square graphs, triangular graphs, each with explicit $(k,\lambda,\mu)$ (pp. 84–85, 88–89).
- $A^2=(\lambda-\mu)A+\mu J+(k-\mu)I$ forces the other eigenvalues $r>s$ to be roots of $\theta^2=(\lambda-\mu)\theta+k-\mu$ (p. 85).
- Converse: a connected regular graph with at most three eigenvalues is strongly regular (p. 86).
- If $f\neq g$, then $r,s$ are integers (rational, plus a root lemma) (pp. 86–87).
- With $U$ an orthonormal eigenbasis matrix for $r$, $UU^T=P(A)$ for a polynomial $P$; so the eigenspace points form a two-distance set (p. 88).
- Counting degree-2 polynomials gives $f\ge\sqrt{2n}-2$ (pp. 89–90).

## L3 — Walkthrough

### 9.1–9.2 Definition
Strongly regular graphs are described as extremal; their adjacency matrices have only three distinct eigenvalues (p. 83). The Paley graphs of Chapter 7 are strongly regular (p. 83). The author says strongly regular graphs can be thought of as high-degree analogues of expander graphs, but are much easier to construct, and that they have provided a reasonable answer to requests for a 0/1 matrix that "looked random" (p. 83). Here $\lambda,\mu$ are **not** eigenvalues (p. 83).

$G$ is *strongly regular* if (1) it is $k$-regular; (2) every adjacent pair has exactly $\lambda$ common neighbours; (3) every non-adjacent pair has exactly $\mu$ common neighbours (p. 83). Complete graphs and disjoint unions of complete graphs qualify. From now on: connected, not complete (p. 84).

### 9.3–9.5 Examples
- Pentagon: $n=5,k=2,\lambda=0,\mu=1$ (p. 84).
- Lattice graph $L_n$: vertices $\{1,\dots,n\}^2$, adjacent if same row or column (the line graph of $K_{n,n}$). $k=2(n-1)$, $\lambda=n-2$, $\mu=2$ (p. 84).
- Latin square graph: $n^2$ cells, adjacent if same row, same column or same symbol. $k=3(n-1)$. Two adjacent cells in a row share the other $n-2$ cells of the row plus two more (each one's symbol in the other's column), so $\lambda=n$. For non-adjacent $(1,1),(2,2)$ there are 2 common neighbours in the row, 2 in the column, 2 via the symbol of $(1,1)$, so $\mu=6$ (p. 85).

### 9.6 Eigenvalues
$(A^2)_{uv}$ counts common neighbours; $(A^2)_{uu}=k$. The complement has adjacency matrix $J-I-A$. So
$$A^2=\lambda A+\mu(J-I-A)+kI=(\lambda-\mu)A+\mu J+(k-\mu)I.$$
For $v\perp\mathbf 1$: $A^2v=(\lambda-\mu)Av+(k-\mu)v$. So every eigenvalue $\theta\ne k$ satisfies $\theta^2=(\lambda-\mu)\theta+k-\mu$, with roots
$$\frac{\lambda-\mu\pm\sqrt{(\lambda-\mu)^2+4(k-\mu)}}{2}.$$
These are called $r>s$, with multiplicities $f$ and $g$. $k$ has multiplicity 1 (p. 85).
Values: pentagon $r=\frac{\sqrt5-1}{2}$, $s=-\frac{\sqrt5+1}{2}$ (p. 85); $L_n$: $r=n-2,s=-2$; Latin square graphs: $r=n-3,s=-3$ (p. 86).

*Intuition note:* $A^2$ counts two-step walks. Strong regularity makes that count depend only on "equal / adjacent / non-adjacent", so $A^2$ lives in the span of $I,A,J$.

### 9.7 Converse
Let $G$ be connected, $k$-regular, with eigenvalues other than $k$ equal to $r,s$. For $v\perp\mathbf 1$, $(A-rI)(A-sI)v=0$; hence $(A-rI)(A-sI)=\beta J$ for some $\beta$. Then
$$A^2=(r+s)A-rsI+\beta J=(r+s+\beta)A+\beta(J-A-I)+(\beta-rs)I .$$
(The source prints $(rs+\beta)I$; see Reading notes.) Common-neighbour counts depend only on adjacency, so $G$ is strongly regular (p. 86).

### 9.8 Integrality
From the quadratic: $r+s=\lambda-\mu$ (9.1), $rs=\mu-k$ (9.2). Trace of $A$ is 0:
$$k+fr+gs=0\tag{9.3}$$
The author concludes $s<0$ and $r>0$ (p. 86). If $f\ne g$, (9.3) and (9.1) are independent constraints on $r,s$ (added step: the coefficient matrix $\begin{pmatrix}1&1\\f&g\end{pmatrix}$ has determinant $g-f\neq0$). Integer coefficients make $r,s$ rational (pp. 86–87).

**Lemma 9.8.1.** A rational root $\theta$ of $\theta^2+b\theta+c=0$ ($b,c\in\mathbb Z$) is an integer. *Proof:* $\theta=x/y$ in lowest terms gives $x^2+bxy+cy^2=0$, so $y\mid x^2$; with $\gcd(x,y)=1$, $y=1$ (p. 87).
So unless $f=g$, $r$ and $s$ are integers (p. 87).

### 9.9 Eigenspaces
Let $U$ ($n\times f$) have orthonormal $r$-eigenvectors as columns; $U$ is determined only up to $UQ$, $Q$ orthogonal. Vertex $i$ gets $\boldsymbol x_i=(u_1(i),\dots,u_f(i))$. Distances depend on $\|\boldsymbol x_i\|^2+\|\boldsymbol x_j\|^2-2\boldsymbol x_i\boldsymbol x_j^T$ and $QQ^T=I$ leaves this unchanged (p. 87). All geometry is in the Gram matrix $UU^T$ (p. 87).
With $W$ the analogue for $s$:
$$A=rUU^T+sWW^T+\tfrac kn J,\qquad A^2=r^2UU^T+s^2WW^T+k^2\tfrac1nJ,$$
because $UU^T$, $WW^T$, $\frac1nJ$ are mutually orthogonal projections (p. 88). Take
$$P(X)=\frac{(X-s)(X-k)}{(r-s)(r-k)},\quad P(r)=1,\ P(s)=P(k)=0 .$$
Then $P(A)=UU^T$. So the Gram matrix is a combination of $I$, $A$, $A^2$, and distances depend only on adjacency. The points form a *two-distance point set* (p. 88).

*Intuition note:* The author says the eigenspaces tell us nothing we do not already know about the graph (p. 87). The Gram matrix is a fixed polynomial in $A$, so the embedding's geometry is determined by $A$ (p. 88).

### 9.10 Triangular graphs
$T_n$ is the line graph of $K_n$: vertices are 2-subsets of $\{1,\dots,n\}$, adjacent if they meet in one element. $T_3$ is the triangle, $T_4$ the octahedron skeleton, $T_5$ the complement of the Petersen graph (p. 88). For $\{1,2\}$: neighbours $\{1,i\},\{2,i\}$, so $k=2(n-2)$. For neighbour $\{1,3\}$: common neighbours $\{1,i\}$ ($i\ge4$) and $\{2,3\}$, so $\lambda=(n-3)+1=n-2$ (p. 88). For non-neighbour $\{3,4\}$: $\{1,3\},\{1,4\},\{2,3\},\{2,4\}$, so $\mu=4$ (p. 89).

### 9.11 Two-distance sets and a dimension bound
Author states (without proof here) that for connected non-complete graphs distinct vertices map to distinct unit vectors, and that two strongly regular graphs with the same parameters are isomorphic iff an orthogonal map carries one point set to the other. Checking all maps fixed by $f$ independent vectors needs $\binom nf f!$ trials, which would be helpful if $f$ were small; but, the author says, it is not small: $f,g\ge\sqrt{2n}-2$ (p. 89).

**Claim.** Let $\boldsymbol x_1,\dots,\boldsymbol x_n\in\mathbb R^f$ be unit vectors with $\langle\boldsymbol x_i,\boldsymbol x_j\rangle\in\{\alpha,\beta\}$, $\alpha,\beta<1$. Then $f\ge\sqrt{2n}-2$.
*Proof.* Set $p_i(\boldsymbol y)=(\boldsymbol y^T\boldsymbol x_i-\alpha)(\boldsymbol y^T\boldsymbol x_i-\beta)$, degree 2 in $f$ variables. Such polynomials form a space of dimension $1+2f+\binom f2$ (p. 89). Suppose the $p_i$ are dependent: $\sum_i\gamma_ip_i=0$ with $\gamma_1\ne0$. Plug in $\boldsymbol y=\boldsymbol x_1$: $\sum_i\gamma_ip_i(\boldsymbol x_1)=\gamma_1p_1(\boldsymbol x_1)\ne0$, a contradiction (p. 90). (Added step: $p_i(\boldsymbol x_j)=0$ for $i\ne j$, and $p_1(\boldsymbol x_1)=(1-\alpha)(1-\beta)\ne0$.) Hence $n\le1+2f+\binom f2$, so $f\ge\sqrt{2n}-2$ (p. 90). (Added step: $1+2f+\binom f2=\frac{(f+1)(f+2)}2$, so $2n\le(f+2)^2$.) The text states the same for $g$ (p. 89).

*Intuition note:* Unit vectors in $\mathbb R^f$ whose inner products take only two values below 1 cannot be more numerous than the dimension of the space of quadratics in $f$ variables. So many vertices force a large eigenspace.

## Toy example (ours): the pentagon
$n=5,k=2,\lambda=0,\mu=1$, so the identity reads $A^2=-A+J+I$. Vertex 0 has neighbours 1, 4.
- $(A^2)_{00}=2$; formula: $0+1+1=2$.
- Adjacent 0,1: neighbours of 1 are $\{0,2\}$, no overlap with $\{1,4\}$, so 0; formula $-1+1=0$.
- Non-adjacent 0,2: neighbours of 2 are $\{1,3\}$, overlap $\{1\}$, so 1; formula $0+1=1$.

Quadratic: $\theta^2=-\theta+1$, roots $\frac{-1\pm\sqrt5}2$; $r+s=-1=\lambda-\mu$ and $rs=\frac{1-5}4=-1=\mu-k$. The trace equation forces $f=g$ (added step: its irrational part is $(f-g)\sqrt5/2$), and then $2+f(r+s)=2-f=0$ gives $f=g=2$ (added step): $k+fr+gs=2+2(-1)=0$ ✓. Here $f=g$ and $r,s$ are irrational, which is allowed.

## Concepts
- [[strongly-regular-graph]] (new) — $k$-regular; $\lambda$ common neighbours for adjacent pairs, $\mu$ for non-adjacent (p. 83)
- [[adjacency-matrix]] — $(A^2)_{uv}$ counts common neighbours (p. 85)
- [[eigenvector-eigenvalue]] — here $k$ (multiplicity 1), $r>s$ with multiplicities $f,g$ (p. 85)
- [[projection]] — $UU^T$, $WW^T$, $\frac1nJ$ are orthogonal projections (p. 88)
- [[gram-matrix]] (new) — matrix of inner products $\boldsymbol x_i\boldsymbol x_j^T$; equals $UU^T$ (p. 87)
- [[two-distance-point-set]] (new) — points with only two distinct pairwise distances (p. 88)
- [[linear-independence]] — used for the polynomials $p_i$ (p. 89)

## Canonical instances
- [[pentagon]] — called the simplest strongly regular graph (p. 84)
- [[lattice-graph]] — $L_n$ (p. 84)
- [[latin-square-graph]] — $\lambda=n,\mu=6$ (p. 85)
- [[triangular-graph]] — $T_n$ (p. 88)
- [[paley-graph]] — only mentioned as strongly regular (p. 83)

## Bridges (candidates)
- [structural-analogy] Strongly regular graphs as high-degree analogues of expanders ↔ spectral graph theory: expander graphs — the author's own comparison; he adds that SRGs are much easier to construct (p. 83).
- [same-math] $P(A)=UU^T$ ↔ spectral decomposition: polynomial in $A$ as a spectral projector.
- [metaphor] Strongly regular 0/1 matrices as "random-looking" ↔ random-matrix modelling.

## Questions this raises
- Why must $\mu<k$, and does this give $r>0$ directly?
- Can every eigenvalue list satisfying (9.1)–(9.3) be realised by a graph?
- How strong is the claim that graphs are isomorphic iff their point sets are orthogonally equivalent?
- How tight is $\sqrt{2n}-2$ for known examples?

## Reading notes
- Printed = pdf − 24. Source is an incomplete draft headed "This Chapter Needs Editing" (p. 83).
- Misprint (p. 86): the final expansion shows $(rs+\beta)I$; consistent algebra requires $(\beta-rs)I$.
- p. 86: "Equation 9.1 then gives $r>0$" looks like it should cite (9.2) with $\mu<k$ (not stated here).
- p. 87: "$\|xx_j\|$" is a typo for $\|\boldsymbol x_j\|$. p. 89: sum index "$i\le k$" should be $i\le j$.
- p. 85: "just two other eigenvalues" is read as "at most two".
- p. 83 intro states $\lambda,\mu$ differ from eigenvalues.
