---
id: spielman-2025-sagt/ch04-adjacency
work: spielman-2025-sagt
unit: "Chapter 4 — Adjacency matrices, Eigenvalue Interlacing, and the Perron-Frobenius Theorem"
pages: 34-42
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
# Adjacency matrices, Eigenvalue Interlacing, and the Perron-Frobenius Theorem

## L0 — One line
The largest adjacency eigenvalue $\mu_1$ is squeezed between average and maximum degree, never increases when vertices are deleted, bounds the chromatic number and (for connected graphs) has a positive eigenvector and satisfies $|\mu_n|\le\mu_1$, with equality exactly for bipartite graphs.

## L1 — The gist (≤ 120 words)
The chapter asks what the extreme eigenvalues of an adjacency matrix $M$ say about a graph. Degrees bound $\mu_1$: $d_{ave}\le\mu_1\le d_{max}$. Cauchy interlacing shows $\mu_1$ is at least the average degree of every induced subgraph. This gives Wilf's theorem, $\chi(G)\le\lfloor\mu_1\rfloor+1$. For connected graphs, Perron-Frobenius (symmetric case) gives a strictly positive top eigenvector, $\mu_1\ge-\mu_n$ and $\mu_1>\mu_2$. For a connected graph, $\mu_n=-\mu_1$ holds exactly when the graph is bipartite. These are features Laplacians lack.

**Prerequisites:** symmetric matrices and the spectral theorem; Rayleigh quotients and Courant–Fischer; graph colouring basics (chromatic number $\chi(G)$ = fewest colours so that adjacent vertices get different colours); induced subgraph (a vertex subset with all edges inside it); bipartite (vertices split into two sets, every edge between them); singular values.

## L2 — Key ideas
- Eigenvalues are ordered $\mu_1\ge\dots\ge\mu_n$, so $\mu_i$ matches Laplacian $\lambda_i$ for regular graphs, $\lambda_i=d-\mu_i$ (p. 35).
- $d_{ave}\le\mu_1\le d_{max}$; for connected $G$, $\mu_1=d_{max}$ forces $G$ to be regular (pp. 35–36).
- For trees of maximum degree $d$, all eigenvalues have absolute value $\le 2\sqrt{d-1}$, proved by rescaling with a diagonal matrix (p. 36).
- Cauchy interlacing implies $\mu_1\ge d_{ave}(S)$ for every induced subgraph (pp. 37–38).
- Wilf: $\chi(G)\le\lfloor\mu_1\rfloor+1$, by induction removing a minimum-degree vertex (pp. 38–39).
- Perron-Frobenius (symmetric, proved for $H=0$): positive top eigenvector, $\mu_1\ge-\mu_n$, $\mu_1>\mu_2$ (pp. 39–40).
- Connected $G$ is bipartite if and only if $\mu_n=-\mu_1$; bipartite spectra are symmetric about 0 (p. 41).
- A bipartite $M$ is the "dilation" of $B$, so its spectrum comes from the singular values of $B$ (pp. 41–42).

## L3 — Walkthrough

**Intro (p. 34).** The author says the top adjacency eigenvalue corresponds to the smallest Laplacian eigenvalue. The Perron vector (top adjacency eigenvector) need not be constant.

**4.1 The adjacency matrix (pp. 34–35).** For a possibly weighted graph, $M$ acts by
$$(Mx)(a)=\sum_{(a,b)\in E}w_{a,b}\,x(b)=\sum_{b\sim a}w_{a,b}x(b).\tag{4.1}$$
The ordering is $\mu_1\ge\dots\ge\mu_n$ (opposite to the Laplacian's), so that $\mu_i$ corresponds to $\lambda_i$. If $G$ is $d$-regular, $D=Id$, $L=dI-M$, so $\lambda_i=d-\mu_i$. Hence $\mu_1=d$ with constant eigenvector. Directly: if $x\equiv1$, then $(Mx)(b)=d$ (p. 35).

**4.2 The largest eigenvalue (pp. 35–36).**
*Lemma 4.2.1.* With $d_{ave}=\frac1n\sum_a d(a)$ and $d_{max}=\max_a d(a)$: $d_{ave}\le\mu_1\le d_{max}$ (p. 35).
- Lower bound: $\mu_1=\max_x\frac{x^TMx}{x^Tx}\ge\frac{1^TM1}{1^T1}=\frac{1^Td}{n}=\frac{\sum_a d(a)}{n}=d_{ave}$.
- Upper bound: take eigenvector $\phi_1$, positive somewhere (replace by $-\phi_1$ if needed). Let $a$ maximise $\phi_1$. Then
$$\mu_1=\tfrac{1}{\phi_1(a)}(M\phi_1)(a)=\tfrac1{\phi_1(a)}\sum_{b\sim a}w_{a,b}\phi_1(b)\le\tfrac1{\phi_1(a)}\sum_{b\sim a}w_{a,b}\phi_1(a)=d(a)\le d_{max}.\tag{4.2}$$
The step "$\le$" uses $\phi_1(b)\le\phi_1(a)$ and non-negative weights (added step).

*Lemma 4.2.2.* If $G$ is connected and $\mu_1=d_{max}$, then $G$ is $d_{max}$-regular. Equality in (4.2) forces $d(a)=d_{max}$ and $\phi_1(b)=\phi_1(a)$ for all neighbours $b$. Repeating along paths reaches every vertex (p. 36).

*Theorem 4.2.3.* For any complex $n\times n$ matrix $M$ and eigenvalue $\lambda$: $|\lambda|\le\max_a\sum_b|M(a,b)|=\|M\|_\infty$. Proof: take $a$ where $|\phi|$ is largest. Then
$$|\lambda||\phi(a)|=|(M\phi)(a)|=\Big|\sum_bM(a,b)\phi(b)\Big|\le\sum_b|M(a,b)||\phi(b)|\le|\phi(a)|\sum_b|M(a,b)|.$$
Divide by $|\phi(a)|$ (p. 36).

Lemma 4.2.1's bounds can be very loose. A large complete $d$-ary tree has maximum degree $d$, average degree just under 2, and $\mu_1$ close to $2\sqrt{d-1}$ (p. 36).

*Theorem 4.2.4.* If $d\ge2$ and every vertex of tree $T$ has degree $\le d$, all adjacency eigenvalues have absolute value $\le2\sqrt{d-1}$ (p. 36). Proof:
- Root the tree; $h(a)$ is the distance to the root. Let $D(a,a)=(\sqrt{d-1})^{h(a)}$.
- $DMD^{-1}$ has the same eigenvalues as $M$. Theorem 4.2.3 bounds them by the largest row sum of $DMD^{-1}$.
- Root row: up to $d$ entries, each $1/\sqrt{d-1}$. $d/\sqrt{d-1}\le2\sqrt{d-1}$ for $d\ge2$.
- Leaf row: one nonzero entry, $\sqrt{d-1}$.
- Other rows: one entry $\sqrt{d-1}$ and up to $d-1$ entries $1/\sqrt{d-1}$; total $2\sqrt{d-1}$.

The lower bound is left as an exercise.

*Intuition note.* Rescaling by $\sqrt{d-1}$ per level averages out the low- and high-degree vertices (p. 36). This gives a tight bound on a tree where the degree bounds of Lemma 4.2.1 are very loose.

**4.3 Eigenvalue interlacing (pp. 37–38).** The induced subgraph $G(S)$ has vertex set $S$ and all edges of $E$ inside $S$. $M(S)$ is the principal submatrix on $S$ (p. 37).

*Theorem 4.3.1 (Cauchy).* If $B$ is $A$ (symmetric, $n\times n$) with one row and the same column deleted, then
$$\alpha_1\ge\beta_1\ge\alpha_2\ge\beta_2\ge\dots\ge\alpha_{n-1}\ge\beta_{n-1}\ge\alpha_n,$$
where $\alpha_i$, $\beta_i$ are the eigenvalues of $A$, $B$ (p. 37). Proof: assume the first row and column are removed. Courant–Fischer gives $\alpha_k=\max_{S\subseteq\mathbb R^n,\dim S=k}\min_{x\in S}\frac{x^TAx}{x^Tx}$. For $B$,
$$\beta_k=\max_{S\subseteq\mathbb R^{n-1},\ \dim S=k}\min_{x\in S}\frac{\binom0x^TA\binom0x}{x^Tx}.$$
This is a maximum over only those $k$-dimensional subspaces of $\mathbb R^n$ whose vectors have first coordinate 0. A maximum over all subspaces is no smaller, so $\alpha_k\ge\beta_k$. The other inequalities follow by using $-A,-B$, or the min–max form of Courant–Fischer (p. 37).

*Lemma 4.3.2.* For $S\subseteq V$, $d_{ave}(S)\le\mu_1$. Proof: $M(S)$ is the adjacency matrix of $G(S)$. Lemma 4.2.1 bounds $d_{ave}(S)$ by its top eigenvalue, and interlacing bounds that by $\mu_1$ (p. 38). Direct proof: the Rayleigh quotient of $1_S$ is $\frac{1_S^TM1_S}{1_S^T1_S}=\frac{\sum_{a,b\in S,(a,b)\in E}w_{a,b}}{|S|}=d_{ave}(S)$ (p. 38). The author calls interlacing "overkill" here (p. 38).

*Intuition note.* Deleting a vertex can raise the average degree, yet $\mu_1$ can only fall. So $\mu_1$ is at least the average degree of every induced piece.

**4.4 Wilf's theorem (pp. 38–39).** A colouring gives adjacent vertices distinct colours; $\chi(G)$ is the least $k$ for which $G$ is $k$-colourable. Greedy colouring gives $\chi\le d_{max}+1$ (p. 38).

*Theorem 4.4.1.* $\chi(G)\le\lfloor\mu_1\rfloor+1$. Induction on $n$. Base: one vertex has $\chi=1$ and $\mu_1=0$. Step:
- Let $a$ have minimum degree. Then $d(a)\le d_{ave}\le\mu_1$ (Lemma 4.2.1). Degrees are integers, so $d(a)\le\lfloor\mu_1\rfloor$.
- For $S=V\setminus\{a\}$, Lemma 4.3.2 gives $\mu_1(G(S))\le\mu_1$. Induction colours $G(S)$ with $\le\lfloor\mu_1\rfloor+1$ colours.
- $a$ has at most $\lfloor\mu_1\rfloor$ neighbours, so a free colour remains (p. 39).

Examples: the 3-vertex path has $d_{max}=2$ but $\mu_1<2$, so Wilf gives 2 colours (tight). A star on $n$ vertices has $d_{max}=n-1$ and $\mu_1=\sqrt{n-1}$. Wilf is then much better than $d_{max}+1$ but far from the true $\chi=2$ (p. 39).

**4.5 Perron-Frobenius, symmetric case (pp. 39–41).**
*Theorem 4.5.1.* Let $G$ be connected and weighted with adjacency matrix $A$. Let $H$ be a non-negative diagonal matrix and $M=A+H$. Then (a) $\mu_1$ has a strictly positive eigenvector; (b) $\mu_1\ge-\mu_n$; (c) $\mu_1>\mu_2$. Only the case $H=0$ is proved (p. 39).

*Lemma 4.5.2.* A non-negative eigenvector $\phi$ of $M$ is strictly positive. If $\phi$ is not strictly positive, some entry is 0; as $G$ is connected and $\phi\ne0$, there is an edge $(b,c)$ with $\phi(b)=0$ and $\phi(c)>0$. Then $0=\mu\phi(b)=(M\phi)(b)=\sum_{(b,z)\in E}w_{b,z}\phi(z)\ge w_{b,c}\phi(c)>0$, a contradiction (p. 40).

Proof of the theorem (p. 40):
- (a) Let $\phi_1$ be a unit eigenvector of $\mu_1$ and $x(u)=|\phi_1(u)|$. Then $x^Tx=\phi_1^T\phi_1$ and $\mu_1=\phi_1^TM\phi_1=\sum_{a,b}M(a,b)\phi_1(a)\phi_1(b)\le\sum_{a,b}M(a,b)|\phi_1(a)||\phi_1(b)|=x^TMx$. So $x$'s Rayleigh quotient is at least $\mu_1$, hence exactly $\mu_1$, so $x$ is an eigenvector (Theorem 2.2.1, cited). By Lemma 4.5.2 it is strictly positive.
- (b) With $y(u)=|\phi_n(u)|$: $|\mu_n|=|\phi_nM\phi_n|\le\sum_{a,b}M(a,b)y(a)y(b)=y^TMy\le\mu_1y^Ty=\mu_1$ (4.3).
- (c) $\phi_2$ is orthogonal to the positive $\phi_1$, so it has both signs. With $y=|\phi_2|$: $\mu_2=\phi_2^TM\phi_2\le y^TMy\le\mu_1$. If $\mu_2=\mu_1$, then $y$ is a non-negative eigenvector of $\mu_1$, hence strictly positive. So $\phi_2$ has no zero entries, and connectivity gives an edge $(a,b)$ with $\phi_2(a)<0<\phi_2(b)$. That edge contributes negatively to $\phi_2^TM\phi_2$ and positively to $y^TMy$, so the first inequality is strict, a contradiction.

*Intuition note.* Taking absolute values of an eigenvector can only raise the quadratic form because all matrix entries are non-negative. So the absolute-value vector $x$ is again a top eigenvector. Connectivity then spreads positivity to every vertex.

*Proposition 4.5.3.* If $G$ is connected and $\mu_n=-\mu_1$, then $G$ is bipartite. Equality in (4.3) needs $y$ to be an eigenvector for $\mu_1$, hence strictly positive. So $\phi_n$ has no zeros, and some edge $(a,b)$ has $\phi_n(a)<0<\phi_n(b)$. All terms $M(a,b)\phi_n(a)\phi_n(b)$ must share one sign, and that sign is negative (that edge gives a negative term; added step, for positive weights). So the endpoints of every edge have opposite signs in $\phi_n$, and these signs give the bipartition (p. 41).

*Proposition 4.5.4.* If $G$ is bipartite with sides $S,T$, its spectrum is symmetric about 0. Given eigenpair $(\mu,\phi)$, let $x=\phi$ on $S$ and $-\phi$ on $T$. For $a\in S$, $(Mx)(a)=\sum M(a,b)(-\phi(b))=-\mu\phi(a)=-\mu x(a)$. The case $a\in T$ is similar (p. 41). The author also states, for connected $G$, that if $\mu_n=-\mu_1$ then $\mu_{n-i}=-\mu_{i+1}$ for every $i$ (p. 41); no separate proof is given on these pages.

**4.6 Singular values and directed graphs (pp. 41–42).** A bipartite graph has $M=\begin{pmatrix}0&B\\B^T&0\end{pmatrix}$, with rows and columns indexed by $S$ then $T$. $B$ need not be square. With $s=|S|\le t=|T|$, "one can show" (no proof given) that the singular values of $B$ are the square roots of the eigenvalues of $BB^T$. The eigenvalues of $M$ are $t-s$ zeros and $\pm\sigma_1,\dots,\pm\sigma_s$. $M$ is called the dilation of $B$ (p. 42). The author recommends Seneta and Bapat–Raghavan for general Perron-Frobenius theory (p. 42).

## Toy example (ours)
Path on 3 vertices, vertices 1–2–3: $M=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}$.
- $\det(M-\lambda I)=-\lambda^3+2\lambda=-\lambda(\lambda^2-2)$, so $\mu_1=\sqrt2,\ \mu_2=0,\ \mu_3=-\sqrt2$. Symmetric about 0, as for a bipartite graph.
- Perron vector: $x=(1,\sqrt2,1)$ gives $Mx=(\sqrt2,2,\sqrt2)=\sqrt2\,x$, strictly positive.
- Degree bounds: $d_{ave}=4/3\approx1.333\le1.414\le d_{max}=2$.
- Wilf: $\lfloor\sqrt2\rfloor+1=2$ colours.
- Prop. 4.5.4: take $S=\{2\}$, $T=\{1,3\}$. Flipping the sign on $T$ gives $x'=(-1,\sqrt2,-1)$ and $Mx'=(\sqrt2,-2,\sqrt2)=-\sqrt2\,x'$.
- Dilation: $B=(1\ 1)$ is $1\times2$, with $s=1,t=2$ and singular value $\sqrt2$. So $M$ has $t-s=1$ zero and $\pm\sqrt2$.

## Concepts
- [[rayleigh-quotient]] — $x^TMx/x^Tx$; its maximum is $\mu_1$, and a test vector gives lower bounds (p. 35)
- [[adjacency-matrix]] — acts by $(Mx)(a)=\sum_{b\sim a}w_{a,b}x(b)$, eigenvalues ordered decreasingly here (p. 34)
- [[perron-frobenius-theorem]] — symmetric case: connected $G$ gives positive top eigenvector, $\mu_1\ge-\mu_n$, $\mu_1>\mu_2$ (p. 39)
- [[spectral-theorem]] — used (cited, not restated) to simplify the symmetric case (p. 39)
- [[singular-value-decomposition]] — singular values of $B$ give the spectrum of a bipartite $M$ (p. 41)
- [[graph-laplacian]] — compared; $L=dI-M$ for regular graphs (p. 35)
- [[cauchy-interlacing-theorem]] (new) — eigenvalues of a one-vertex-deleted principal submatrix interlace those of $A$ (p. 37)
- [[courant-fischer-theorem]] (new) — max–min over $k$-dimensional subspaces of Rayleigh quotients (p. 37)
- [[chromatic-number]] (new) — least $k$ for which a proper $k$-colouring exists (p. 38)
- [[wilf-theorem]] (new) — $\chi(G)\le\lfloor\mu_1\rfloor+1$ (p. 38)
- [[bipartite-graph]] (new) — vertices split into $S,T$ with all edges between them; here, connected $G$ is bipartite iff $\mu_n=-\mu_1$ (p. 41)
- [[dilation-matrix]] (new) — $\begin{pmatrix}0&B\\B^T&0\end{pmatrix}$ built from $B$ (p. 42)

## Canonical instances
- [[complete-d-ary-tree]] — degree bounds are loose; $\mu_1\approx2\sqrt{d-1}$ (p. 36)
- [[path-graph-3]] — Wilf's bound gives 2 colours, tight (p. 39)
- [[star-graph]] — $\mu_1=\sqrt{n-1}$; Wilf's bound is far above the true $\chi=2$ (p. 39)
- [[d-regular-graph]] — constant top eigenvector, $\mu_1=d$ (p. 35)

## Bridges (candidates)
- [structural-analogy] Rayleigh quotient with test vector $1$ or $1_S$ ↔ lower bounds in optimisation: any feasible test vector bounds the maximum from below.
- [same-math] Perron vector (positive top eigenvector) ↔ network science: eigenvector centrality of a connected graph is the same top adjacency eigenvector.
- [structural-analogy] Bipartite dilation $M$ ↔ SVD of a rectangular data matrix: spectrum of $M$ is $\pm$ singular values.

## Questions this raises
- Is Theorem 4.2.4 tight, i.e. do trees approach $2\sqrt{d-1}$? (Exercise 1.)
- How do the proofs change when $H\ne0$, and for directed strongly connected graphs, which need not be diagonalizable (p. 39)?
- Can Wilf's bound be sharpened further? (Chapter 19 is announced, p. 34.)
- Does the singular-value statement for $BB^T$ hold as claimed? The text gives no proof.

## Exercises worth doing
- Ex. 1 (p. 42) — formalise and prove that the $2\sqrt{d-1}$ tree bound of Theorem 4.2.4 is tight — difficulty: hard

## Reading notes
- Printed = pdf − 24.
- Footnote 1 (p. 38) writes a $k$-coloring as $c:\{1,\dots,k\}\to V$; the direction looks reversed (should be $V\to\{1,\dots,k\}$).
- Proof of Thm 4.4.1 (p. 39): "at most $a$ is at most $\mu_1$" is a garbled phrase (minimum degree $\le d_{ave}\le\mu_1$ is meant). Footnote 2 on p. 39 ends mid-sentence.
- Eq. (4.3) (p. 40) writes $|\phi_nM\phi_n|$ without a transpose.
- Proofs cite Theorem 2.2.1 and Section 2.3, which are not in these pages.
- Page 42 sentence "the bound prove in Theorem 4.2.4" has a typo.
- The title page of the work is not in these pages; the draft date is taken from the metadata, not seen here.
