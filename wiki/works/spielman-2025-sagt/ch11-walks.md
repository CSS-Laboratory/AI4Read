---
id: spielman-2025-sagt/ch11-walks
work: spielman-2025-sagt
unit: "Chapter 11 — Walks, Springs, and Resistor Networks"
pages: 102-110
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
# Walks, Springs, and Resistor Networks

## L0 — One line
Absorbing random walks, spring networks and resistor networks all lead to the same object: a function that is harmonic away from the boundary, found by solving a linear system in the Laplacian matrix or one of its submatrices.

## L1 — The gist (≤ 120 words)
Question: how can one linear-algebra problem describe three different physical or probabilistic models on a weighted graph? Answer: in each model the values at non-boundary nodes (those not fixed in the boundary set $B$) equal the weighted average of the neighbours' values (a harmonic function). With boundary values fixed, this is the system $L(S,S)x(S)=r$. If the graph is connected and the boundary is nonempty, $L(S,S)$ (a submatrix of the Laplacian $L=D-M$) is positive definite, so the solution exists and is unique; its inverse has nonnegative entries. The same solution minimises spring energy. For resistor networks, $i_{ext}=U^TWUv=Lv$, and the Laplacian pseudo-inverse $L^+$ solves for voltages. These ideas recur in the rest of the book.

**Prerequisites:** weighted graphs, degree and Laplacian $L=D-M$; positive (semi)definite matrices; eigendecomposition of symmetric matrices; Neumann series; Perron–Frobenius theorem (used, not proved here); partial derivatives.

## L2 — Key ideas
- $x$ is harmonic at $a$ if $x(a)$ is the weighted average of its neighbours' values, eq. (11.1) (p. 102).
- Absorbing-walk probabilities, spring equilibria and resistor voltages are harmonic at non-boundary nodes (pp. 103–104, 109).
- Harmonic equations are Laplacian rows, so they reduce to $L(S,S)x(S)=r$ (pp. 104–105).
- $L(S,S)$ is positive definite when $G$ is connected and $\emptyset\ne B\subsetneq V$; the solution is therefore unique (pp. 105–106).
- For $L$ the Laplacian of a connected graph and $X$ diagonal, nonnegative and nonzero, the inverse of $L+X$ has all entries positive, via a convergent series (p. 106).
- The harmonic solution minimises the spring energy $\mathcal E(x)$ (p. 107).
- Resistor networks: $i=WUv$, $i_{ext}=U^TWUv=Lv$; voltages are harmonic exactly where $i_{ext}=0$ (pp. 108–109).
- $v=L^+i_{ext}$ solves the equations when the entries of $i_{ext}$ sum to zero (pp. 109–110).

## L3 — Walkthrough

### 11.2 Harmonic functions (p. 102)
Setting: weighted graph $G=(V,E,w)$, boundary $B\subseteq V$, $S=V-B$. $G$ is assumed connected and $B$ nonempty. $x:V\to\mathbb R$ is *harmonic at $a$* if
$$x(a)=\frac1{d_a}\sum_{b\sim a}w_{a,b}x(b).\tag{11.1}$$
It is harmonic on $S$ if it is harmonic at every $a\in S$.

### 11.3 Random walks with absorbing nodes (p. 103)
Take the standard (not lazy) walk, which moves $a\to b$ with probability $w_{a,b}/d_a$. Let $B=\{s,t\}$; the walk stops at $s$ or $t$ (absorbing nodes). Let $x(a)$ be the probability that a walk from $a$ stops at $s$. Then $x(s)=1$, $x(t)=0$, and for other $a$: $x(a)=\sum_{b\sim a}\frac{w_{a,b}}{d_a}x(b)$. So $x$ is harmonic on $V-B$.

Example: path $P_n$ with $s=n$, $t=1$. Then $x(a)=\frac{a-1}{n-1}$ solves (11.1). The author says it 'essentially follows from the definitions' that only one solution can exist, and promises an algebraic proof. The lazy walk gives the same equations, since $x(a)=\tfrac12x(a)+\tfrac12\sum\cdots$ is equivalent to $x(a)=\sum\cdots$.

*Intuition note:* The chance of ending at $s$ is a weighted average over the first step. That is the same averaging rule as harmonicity.

### 11.4 Spring networks (p. 104)
Each edge is an ideal spring with constant $w_{a,b}$. Vertices in $B$ are nailed down. By Hooke's law the force of edge $(a,b)$ on $a$ is $w_{a,b}(x(b)-x(a))$; the unweighted case takes constant 1. Positions $x(a)$ may lie in $\mathbb R$, $\mathbb R^2$ or $\mathbb R^k$. At a stable configuration, each $a\notin B$ has zero net force; in the unweighted case: $\sum_{b\sim a}(x(b)-x(a))=0\iff\frac1{d_a}\sum_{b\sim a}x(b)=x(a)$. The weighted version is (11.1), so $x$ is harmonic on $V-B$.

Existence and uniqueness are claimed for connected $G$ and nonempty $B$. Uniqueness can fail only if some connected component contains no vertex of $B$ (footnote 1). Example: $P_n$ with $x(1)=1$, $x(n)=n$ has the unique solution $x(i)=i$.

### 11.5 Laplacian linear equations (pp. 104–106)
Rewrite (11.1) as $d_ax(a)-\sum_{b\sim a}w_{a,b}x(b)=0$ (11.2). This is row $a$ of the Laplacian. Fix $x(a)=f(a)$ for $a\in B$ and move boundary terms to the right:
$$L(S,S)\,x(S)=r,\qquad r=M(S,B)f(B),\tag{11.3}$$
with $x(B)=f(B)$. Here $L(S,S)$ is the submatrix on rows and columns in $S$, and $M(S,B)$ is described in the text as the submatrix of $L$ on rows $S$, columns $B$ (p. 105; see Reading notes).

**Claim 11.5.1.** $L(S,S)=L_{G(S)}+X_S$. Here $G(S)$ is the induced subgraph, and $X_S$ is diagonal with $X_S(a,a)=\sum_{b\sim a,\,b\in B}w_{a,b}$ (p. 105). The off-diagonals agree with those of $L_{G(S)}$; the diagonals are larger because they also count edges to $B$.

**Lemma 11.5.2.** If $L$ is the Laplacian of a connected graph and $X$ is nonnegative, diagonal, with at least one nonzero entry, then $L+X$ is positive definite.
*Proof (p. 105).* Both $L$ and $X$ are positive semidefinite, so $x^T(L+X)x\ge\min(x^TLx,\,x^TXx)$. Since the graph is connected, $x^TLx>0$ unless $x$ is constant. For $x=c\mathbf 1$, $c\ne0$: $c^2\mathbf 1^T(L+X)\mathbf 1=c^2\mathbf 1^TX\mathbf 1=c^2\sum_iX(i,i)>0$.

**Lemma 11.5.3.** If $G$ is connected and $B$ is a nonempty proper subset of $V$, then $L(S,S)$ is positive definite.
*Proof (p. 106).* Let $S_1,\dots,S_k$ be the components of $G(S)$; $L(S,S)$ is block diagonal with blocks $L(S_i,S_i)=L_{G_{S_i}}+X_{S_i}$. Since $G$ is connected, some vertex of $S_i$ has an edge leaving $S_i$, so $X_{S_i}\ne0$. By Lemma 11.5.2 each block is invertible, so $L(S,S)$ has no zero eigenvalue. Being positive semidefinite, it is positive definite.

Hence (11.3) has a unique solution (p. 106).

**Theorem 11.5.4.** For $L$, $X$ as in Lemma 11.5.2, all entries of $(L+X)^{-1}$ are positive.
*Proof (p. 106).*
1. Write $L=D-M$ ($D$ degree matrix, $M$ adjacency matrix) and $H=D+X$.
2. $H^{-1/2}(L+X)H^{-1/2}=H^{-1/2}(D+X-M)H^{-1/2}=I-H^{-1/2}MH^{-1/2}$, which is positive definite by Lemma 11.5.2.
3. Let $B=H^{-1/2}MH^{-1/2}$. Its largest eigenvalue is below 1. $B$ has nonnegative entries, so Perron–Frobenius gives $\|B\|<1$.
4. So $(I-B)^{-1}=I+\sum_{i\ge1}B^i$ converges, and every term has nonnegative entries.
5. Since $G$ is connected, for each $a,b$ some $i$ has $B^i(a,b)>0$, so every entry of the sum is positive.
6. Finally, $H^{1/2}$ is diagonal with positive entries, so multiplying by it on both sides keeps entries positive (see Reading notes for the printed formula).

*Intuition note:* Adding boundary weights to the diagonal makes the Laplacian invertible. The inverse is a series of powers of $B$; $B^i(a,b)>0$ when a length-$i$ walk joins $a$ and $b$ (my gloss), so a connected graph gives every pair of vertices a positive entry.

### 11.6 Energy (p. 107)
A spring with constant $w$ stretched to length $l$ has energy $\tfrac12wl^2$. So
$$\mathcal E(x)=\tfrac12\sum_{(a,b)\in E}w_{a,b}(x(a)-x(b))^2.\tag{11.4}$$
At a minimiser, $\partial\mathcal E/\partial x(a)=0$ for $a\in S$. The derivative is $\tfrac12\sum_{b\sim a}w_{a,b}\,2(x(a)-x(b))=\sum_{b\sim a}w_{a,b}(x(a)-x(b))$. Setting it to zero gives (11.1).

**Theorem 11.6.1.** For connected weighted $G$, $B\subset V$, $S=V-B$, and given $x(B)$, $\mathcal E(x)$ is minimised by choosing $x(S)$ so that $x$ is harmonic on $S$. If $x(B)=f$, then $x(S)=-L(S,S)^{-1}L(S,B)f$.

### 11.7 Resistor networks (pp. 107–109)
Resistance is $r_e=1/w_e$; a missing edge means infinite resistance. Ohm's law is $V=IR$. Current from $a$ to $b$ is $i(a,b)=\frac1{r_{a,b}}(v(a)-v(b))=w_{a,b}(v(a)-v(b))$, with $i(b,a)=-i(a,b)$. Current flows from high to low voltage.

Orient each edge once. The signed edge–vertex matrix $U$ has rows indexed by edges and columns by vertices: $U((a,b),c)=1$ if $a=c$, $-1$ if $b=c$, $0$ otherwise. So row $(a,b)$ is $\delta_a^T-\delta_b^T$ (p. 108). With $W$ the diagonal matrix of edge weights, $i=WUv$. The network holds no current, so $i_{ext}(a)=\sum_{b\sim a}i(a,b)$, i.e.
$$i_{ext}=U^Ti=U^TWUv.\tag{11.5}$$

Worked example (p. 108): vertices 1, 2, 3; edge (1,2) with weight 1; edge (2,3) with weight 2. Then $U=\begin{pmatrix}1&-1&0\\0&1&-1\end{pmatrix}$ and $W=\mathrm{diag}(1,2)$. For $v=(1,2,4)^T$: $Uv=(-1,-2)^T$, $i=WUv=(-1,-4)^T$, and $i_{ext}=(-1,-3,4)^T$. So one unit leaves the network at vertex 1, coming from vertex 2 because $i(2,1)=1$ (p. 109).

$L\overset{def}{=}U^TWU$ is the Laplacian, equal to $\sum_{a\sim b}w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T$ (eq. 3.3 of Chapter 3). Call nodes with $i_{ext}(a)\ne0$ boundary nodes and the rest internal. Row $a$ of $i_{ext}=Lv$ reads $0=\sum_{b\sim a}w_{a,b}(v(a)-v(b))=d_av(a)-\sum_{b\sim a}w_{a,b}v(b)$, i.e. $v$ is harmonic at $a$. A flow $i=WUv$ is a *potential flow*. The voltages are harmonic at precisely the vertices with $i_{ext}(a)=0$ (p. 109).

### 11.8 Solving for currents (pp. 109–110)
We want $v=L^{-1}i_{ext}$, but $L$ has no inverse. For connected $G$, $Lv=i_{ext}$ has a solution if the entries of $i_{ext}$ sum to zero (current in equals current out). These vectors are exactly those in the span of $L$ (p. 109). We solve with the Moore–Penrose pseudo-inverse.

**Definition 11.8.1.** For symmetric $L$, $L^+$ has the same span as $L$ and satisfies $L^+LL^+=L^+$, $LL^+L=L$, $L^+L=LL^+=\Pi$, where $\Pi$ is the symmetric projection onto the span of $L$ (p. 110). A symmetric projection is symmetric with $\Pi^2=\Pi$, equivalently all eigenvalues are 0 or 1. For a connected graph, $\Pi=(1/n)L_{K_n}$.

**Claim 11.8.2.** If $\psi_1,\dots,\psi_n$ is an orthonormal eigenbasis of $L$ with eigenvalues $\lambda_i$, then $L^+=\sum_{i:\lambda_i\ne0}(1/\lambda_i)\psi_i\psi_i^T$. If $v=L^+i_{ext}$, then $v$ is "the unique solution" of $Lv=i_{ext}$ and is harmonic wherever $i_{ext}$ is zero (p. 110).

*Intuition note:* $L$ cannot be inverted on directions where it is zero. $L^+$ inverts only the nonzero eigen-directions, which is enough when $i_{ext}$ sums to zero.

### 11.9 Exercise (p. 110)
Prove $L^p=\Psi\Lambda^p\Psi^T=\sum_i\lambda_i^p\psi_i\psi_i^T$ for every $p>0$; it holds for any symmetric matrix.

## Toy example (ours)
Use the weighted path 1–2–3 from p. 108: $w_{1,2}=1$, $w_{2,3}=2$. Let $B=\{1,3\}$, $f(1)=0$, $f(3)=3$, $S=\{2\}$.
- $d_2=1+2=3$, so $L(S,S)=[3]$.
- $r=w_{1,2}f(1)+w_{2,3}f(3)=1\cdot0+2\cdot3=6$.
- (11.3): $3x(2)=6$, so $x(2)=2$.
- Check harmonic: $(1\cdot0+2\cdot3)/3=2$. ✓
- Energy as a function of $x(2)=y$: $\mathcal E=\tfrac12(1\cdot y^2+2(3-y)^2)$. At $y=2$: $\tfrac12(4+2)=3$. At $y=0$: $9$. At $y=3$: $4.5$. The derivative $y+2(y-3)=3y-6$ vanishes at $y=2$.
- $L(S,S)^{-1}=1/3>0$, as Theorem 11.5.4 requires.

## Concepts
- [[harmonic-function]] (new) — $x(a)$ equals the weighted neighbour average on $S$ (p. 102)
- [[absorbing-random-walk]] (new) — walk stopped at boundary nodes; stopping probabilities are harmonic (p. 103)
- [[graph-laplacian]] — $L=D-M=U^TWU$; its rows encode harmonic equations (pp. 104, 109)
- [[positive-semidefinite-matrix]] — here $L(S,S)$, $L+X$ are positive definite under stated conditions (pp. 105–106)
- [[perron-frobenius-theorem]] — used for nonnegative $B$: largest eigenvalue below 1 gives $\|B\|<1$ (p. 106)
- [[incidence-matrix]] — signed edge–vertex matrix $U$ with rows $\delta_a^T-\delta_b^T$ (p. 108)
- [[spring-energy]] (new) — $\mathcal E(x)=\tfrac12\sum w_{a,b}(x(a)-x(b))^2$ (p. 107)
- [[potential-flow]] (new) — edge flow $i=WUv$ induced by voltages (p. 109)
- [[pseudoinverse]] — $L^+=\sum_{\lambda_i\ne0}\lambda_i^{-1}\psi_i\psi_i^T$ (p. 110)
- [[spectral-theorem]] — orthonormal eigenbasis used in Claim 11.8.2 (p. 110)

## Canonical instances
- [[path-graph-harmonic]] — on $P_n$, $x(a)=(a-1)/(n-1)$ with ends 0 and 1; $x(i)=i$ with ends 1 and $n$ (pp. 103–104)
- [[three-vertex-resistor-example]] — $U$, $W$, $v=(1,2,4)^T$, $i_{ext}=(-1,-3,4)^T$ (p. 108)

## Bridges (candidates)
- [same-math] Spring energy $\mathcal E(x)$ ↔ Laplacian quadratic form: (11.4) is a sum over edges of $w_{a,b}(x(a)-x(b))^2$ (the identification with $x^TLx$ is not stated in this unit).
- [same-math] Absorbing-walk probabilities ↔ spring positions ↔ resistor voltages: all solve $L(S,S)x(S)=r$.
- [structural-analogy] $(I-B)^{-1}=I+\sum B^i$ ↔ Katz–Bonacich centrality: both are walk-counting series.
- [metaphor] Harmonic averaging ↔ opinion smoothing on a network with stubborn (fixed) agents.

## Questions this raises
- What do entries of $L(S,S)^{-1}$ mean as expected visits of random walks?
- How does $L^+$ define effective resistance between two vertices?
- Is the minimum-energy picture useful for drawing graphs when $x(a)\in\mathbb R^2$?
- When $B=\emptyset$ or the graph is disconnected, what exactly goes wrong?

## Exercises worth doing
- Ex. 11.9 (p. 110) — spectral formula for powers of a symmetric matrix (same form as Claim 11.8.2) — difficulty: easy

## Reading notes
- Printed page = pdf − 24. Per the work citation (not shown on these pages), the source is an incomplete draft dated April 2, 2025.
- Misprint (p. 106, last line of the proof): the image shows "$(I-B)^{-1}=H^{1/2}(I-B)^{-1}H^{1/2}$". The intended identity is presumably $(L+X)^{-1}=H^{-1/2}(I-B)^{-1}H^{-1/2}$ (my correction, from step 2).
- p. 106: just before Theorem 11.5.4 the text says "non-negative" inverse entries, while the theorem says "positive". The proof of Lemma 11.5.3 says "$L$ is invertible" where $L(S,S)$ is meant.
- p. 105: (11.3) uses $M(S,B)$ for the boundary block; Theorem 11.6.1 uses $-L(S,B)$. The text calls $M(S,B)$ a submatrix of $L$, but the right-hand side $\sum w_{a,b}f(b)$ above (11.3) equals $-L(S,B)f(B)$ (off-diagonal entries of $L=D-M$ are $-w_{a,b}$; my check), and on p. 106 $M$ is the adjacency matrix. So (11.3) and Theorem 11.6.1 agree if $M(S,B)$ means the adjacency block $=-L(S,B)$ (my reading; the text does not say so).
- p. 105: the proof of Lemma 11.5.2 uses "min" as printed; the bound by min alone would not give positivity if $x^TXx=0$; the case split (nonconstant $x$: $x^TLx>0$; constant $x$: direct computation) is what shows $x^T(L+X)x>0$ (my reading).
- p. 110: "unique solution" of $Lv=i_{ext}$ presumably means unique within the span of $L$. The text does not say this, and $L$ is not invertible.
