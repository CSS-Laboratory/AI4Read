---
id: spielman-2025-sagt/ch19-independent
work: spielman-2025-sagt
unit: "Chapter 19 — Independent Sets and Coloring"
pages: 164-170
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
# Independent Sets and Coloring

## L0 — One line
The extreme (largest) Laplacian eigenvalue $\lambda_n$ and the extreme adjacency eigenvalues $\mu_1,\mu_n$ give provable bounds on how big an independent set can be and on how many colors a graph needs.

## L1 — The gist (≤ 120 words)
Finding large independent sets (vertex sets with no edge inside) and optimal colorings (using the fewest colors, $\chi(G)$, so that adjacent vertices differ) is computationally hard in general. The chapter asks what the spectrum can still say. Using the Courant–Fischer formula $\lambda_n=\max_x x^TLx/x^Tx$, it shows that an independent set $S$ satisfies $|S|\le n(1-d_{ave}(S)/\lambda_n)$ (Godsil–Newman, generalizing Hoffman). For Paley graphs this gives $|S|\le\sqrt p$. A different argument, based on a block-matrix eigenvalue inequality, gives Hoffman's lower bound $\chi(G)\ge 1+\mu_1/(-\mu_n)$, valid for non-regular and weighted graphs. The bounds are useful for carefully chosen graphs (e.g. Paley graphs). They are not always tight.

**Prerequisites:** symmetric matrices and eigenvalues; Courant–Fischer / Rayleigh quotient; graph Laplacian; block matrices; basic induction.

## L2 — Key ideas (5–10 bullets)
- Adjacency eigenvalues are indexed in decreasing order, $\mu_1\ge\dots\ge\mu_n$. For $d$-regular graphs $\mu_i=d-\lambda_i$, and $\mu_n<0$ for a non-empty graph (p. 164).
- A color class is an independent set, so $\alpha(G)\ge n/\chi(G)$. Finding large independent sets is NP-complete and very hard to even approximate (pp. 164–165).
- Godsil–Newman: for independent $S$, $|S|\le n(1-d_{ave}(S)/\lambda_n)$. The proof tests the Rayleigh quotient on $\mathbf 1_S-s\mathbf 1$ (pp. 165–166).
- For regular graphs this reduces to Hoffman's bound $\alpha\le n\,(-\mu_n)/(d-\mu_n)$. The theorem also holds for weighted graphs (pp. 165–166).
- Paley graphs on $p$ vertices have $\alpha\le\sqrt p$. The text says Paley graphs were among the best known explicit Ramsey graphs until "a decade ago" (p. 167).
- An independence bound gives a lower bound on $\chi$, but it can be poor: a clique with pendant vertices has $\chi=n$ but the bound gives only 2 (p. 167).
- Hoffman: $\chi(G)\ge 1+\mu_1/(-\mu_n)$. It is proved by writing the adjacency matrix in $k$ zero-diagonal color blocks and using $(k-1)\lambda_{min}(M)+\lambda_{max}(M)\le\sum_i\lambda_{max}(M_{i,i})$ (pp. 167–168).
- That block inequality is proved for $k=2$ by building a second test vector from a top eigenvector, then extended by induction (pp. 169–170).

## L3 — Walkthrough

### 19.1–19.2 Setup
Laplacian eigenvalues: $0=\lambda_1\le\dots\le\lambda_n$. Adjacency eigenvalues are numbered in reverse: $\mu_1\ge\dots\ge\mu_n$ (p. 164).

A *$k$-coloring* is $c:V\to\{1,\dots,k\}$ with $c(u)\ne c(v)$ for every edge $(u,v)$. $\chi(G)$ is the least such $k$. $G$ is 2-colorable iff bipartite. Deciding 3-colorability is NP-complete; every planar graph is 4-colorable (p. 164).

A set $S$ is *independent* if no edges join its vertices. $\alpha(G)$ is the size of the largest one. Some color class has size $\ge n/k$, so $\alpha(G)\ge n/\chi(G)$ (p. 164). Finding large independent sets is NP-complete and very hard to approximate, but spectral analysis gives good bounds for some carefully chosen graphs (p. 165).

### 19.3 Hoffman's bound
**Theorem 19.3.1 (Hoffman).** $G$ $d$-regular: $\alpha(G)\le n\dfrac{-\mu_n}{d-\mu_n}$ (p. 165).

**Theorem 19.3.2 (Godsil–Newman).** For any graph and independent $S$:
$$|S|\le n\Bigl(1-\frac{d_{ave}(S)}{\lambda_n}\Bigr).$$
For $d$-regular graphs, $d_{ave}=d$ and $\lambda_n=d-\mu_n$, so $1-\frac{d_{ave}}{\lambda_n}=\frac{\lambda_n-d}{\lambda_n}=\frac{-\mu_n}{d-\mu_n}$ (p. 165).

*Proof.* Courant–Fischer: $\lambda_n=\max_x \frac{x^TLx}{x^Tx}$. Let $s=|S|/n$ and $x=\mathbf 1_S-s\mathbf 1$ (the projection of $\mathbf 1_S$ orthogonal to $\mathbf 1$). Since $L\mathbf 1=0$ and $S$ is independent,
$$x^TLx=\mathbf 1_S^TL\mathbf 1_S=\sum_{a\sim b}(\mathbf 1_S(a)-\mathbf 1_S(b))^2=d(S)=d_{ave}(S)|S|,$$
where $d(S)$ is the sum of degrees in $S$. The equality $\sum_{a\sim b}(\cdot)^2=d(S)$ is the one that uses independence (pp. 165–166). Next,
$$x^Tx=|S|(1-s)^2+(|V|-|S|)s^2=|S|(1-2s+s^2)+|S|s-|S|s^2=|S|(1-s)=n(s-s^2).$$
Thus
$$\lambda_n\ge\frac{x^TLx}{x^Tx}=\frac{d_{ave}(S)|S|}{n(s-s^2)}=\frac{d_{ave}(S)\,sn}{n(s-s^2)}=\frac{d_{ave}(S)}{1-s}.$$
Rearranging gives $1-d_{ave}(S)/\lambda_n\ge s$, which is the claim (p. 166).

*Intuition note.* An independent set has no internal edges, so its indicator vector is "rough" on the edges leaving it. $\lambda_n$ caps how rough any vector can be. That limits how large a fraction of the graph $S$ can be.

The theorem also holds for weighted graphs, though weights play no role in independence (p. 166).

**Claim 19.3.3.** If $|S|=s|V|$, then $\|\mathbf 1_S-s\mathbf 1\|^2=s(1-s)|V|$ (the computation above) (p. 166).

**Claim 19.3.4.** For $x$ of length $n$, $t=\mathbf 1^Tx/n$ minimizes $\|x-t\mathbf 1\|$. *Proof:* $\frac{d}{dt}\sum_a(x(a)-t)^2=2\sum_a(x(a)-t)$. Setting this to 0 gives $nt=\sum_a x(a)=\mathbf 1^Tx$ (p. 166). This is why subtracting $s\mathbf 1$ is natural (p. 166).

### 19.4 Paley graphs
By Corollary 7.3.2 (cited, not stated here), a Paley graph on $n=p$ vertices has $d=(p-1)/2$ and $\lambda_n=(p+\sqrt p)/2$. Hence for independent $S$ (p. 167):
$$|S|\le p\Bigl(1-\frac{p-1}{p+\sqrt p}\Bigr)=p\,\frac{\sqrt p+1}{p+\sqrt p}=\sqrt p.$$
The text says one can also show every clique has size at most $\sqrt p$ (p. 167).

A *$k$-Ramsey graph* has no clique and no independent set of size $k$. Erdős showed that a random graph (each edge with probability 1/2) is probably $2\log_2 n$-Ramsey. Explicit constructions are much harder. The text says Paley graphs were among the best known until "a decade ago". Chattopadhyay–Zuckerman give explicit graphs with no clique or independent set of size $2^{(\log\log n)^{O(1)}}$ (p. 167).

### 19.5 Lower bound on the chromatic number
An independence upper bound gives $\chi\ge n/\alpha$, but this can be weak. **Example (author's):** a clique on $n$ vertices plus $n$ degree-1 vertices, each attached to a different clique vertex ($2n$ vertices). $\chi=n$, since clique vertices need distinct colors. But $\alpha=n$ gives only $\chi\ge 2$ (p. 167).

**Theorem 19.5.1 (Hoffman).** $\chi(G)\ge\dfrac{\mu_1-\mu_n}{-\mu_n}=1+\dfrac{\mu_1}{-\mu_n}$. It needs no regularity and applies to weighted graphs. Numerically it is $n$ divided by the bound of Theorem 19.3.1, but the proof differs (p. 167).

**Lemma 19.5.2.** For a symmetric block-partitioned $M$ with blocks $M_{i,j}$, $k\ge2$ diagonal blocks, and $\lambda_{max},\lambda_{min}$ the largest and smallest eigenvalues:
$$(k-1)\lambda_{min}(M)+\lambda_{max}(M)\le\sum_i\lambda_{max}(M_{i,i}).$$
(p. 168)

*Proof of 19.5.1.* If $G$ is $k$-colorable, order vertices by color. The adjacency matrix has the form (19.1) with every diagonal block $\mathbf 0$, so $(k-1)\mu_n+\mu_1\le 0$. Since $\mu_n<0$, this gives $1+\mu_1/(-\mu_n)\le k$ (p. 168).

*Intuition note.* Edges only join different color blocks, so the matrix has no "mass" on its diagonal blocks. The lemma then ties the top and bottom eigenvalues together: $\mu_n$ cannot be too small in size relative to $\mu_1$ unless $k$ is large.

**Author's numerical example** ($n=6$, $2n=12$ vertices): $\mu_1=5.19$, $\mu_{12}=-1.62$. The bound is $4.2$, so $\chi\ge5$. Giving weight 2 to clique edges and 1 to the rest gives a bound of $5.18$, matching the true $\chi=6$ (p. 168).

### 19.6 Proofs of the lemma
**Lemma 19.6.1.** For symmetric $A=\begin{bmatrix}B&C\\C^T&D\end{bmatrix}$: $\lambda_{min}(A)+\lambda_{max}(A)\le\lambda_{max}(B)+\lambda_{max}(D)$ (p. 169).

*Proof.* Let $x=\binom{x_1}{x_2}$ be a unit eigenvector for $\lambda_{max}(A)$.

*Case $x_1\ne0\ne x_2$.* Set $y=\binom{\frac{\|x_2\|}{\|x_1\|}x_1}{-\frac{\|x_1\|}{\|x_2\|}x_2}$. It is a unit vector (the reader verifies; added step: $\|y\|^2=\|x_2\|^2+\|x_1\|^2=1$). So $y^TAy\ge\lambda_{min}(A)$ and
$$\begin{aligned}\lambda_{max}(A)+\lambda_{min}(A)&\le x^TAx+y^TAy\\
&=x_1^TBx_1+x_1^TCx_2+x_2^TC^Tx_1+x_2^TDx_2+\tfrac{\|x_2\|^2}{\|x_1\|^2}x_1^TBx_1-x_1^TCx_2-x_2^TC^Tx_1+\tfrac{\|x_1\|^2}{\|x_2\|^2}x_2^TDx_2\\
&=x_1^TBx_1+x_2^TDx_2+\tfrac{\|x_2\|^2}{\|x_1\|^2}x_1^TBx_1+\tfrac{\|x_1\|^2}{\|x_2\|^2}x_2^TDx_2\\
&\le\Bigl(1+\tfrac{\|x_2\|^2}{\|x_1\|^2}\Bigr)x_1^TBx_1+\Bigl(1+\tfrac{\|x_1\|^2}{\|x_2\|^2}\Bigr)x_2^TDx_2\\
&\le\lambda_{max}(B)(\|x_1\|^2+\|x_2\|^2)+\lambda_{max}(D)(\|x_1\|^2+\|x_2\|^2)\\
&=\lambda_{max}(B)+\lambda_{max}(D).\end{aligned}$$
The cross terms $C$ cancel. (Added step: the "$\le$" in the fourth line is just regrouping, so it is an equality.) (p. 169)

*Case $\|x_2\|=0$ (or $\|x_1\|=0$, the same case).* Theorem 4.3.1 (cited, not stated here) gives $\lambda_{max}(B)\le\lambda_{max}(A)$. So $x_1$ is an eigenvector of $B$ with eigenvalue $\lambda_{max}(A)$, hence $\lambda_{max}(B)=\lambda_{max}(A)$. Also $\lambda_{max}(D)\ge\lambda_{min}(D)\ge\lambda_{min}(A)$. Adding gives the claim (p. 169).

*Proof of Lemma 19.5.2.* $k=2$ is Lemma 19.6.1. For $k>2$, let $B$ be $M$ with the last block row and column removed. Theorem 4.3.1 gives $\lambda_{min}(B)\ge\lambda_{min}(M)$. Apply Lemma 19.6.1 to $B$ and block $M_{k,k}$, then the induction hypothesis to $B$:
$$\lambda_{min}(M)+\lambda_{max}(M)\le\lambda_{max}(M_{k,k})+\lambda_{max}(B)\le\sum_{i=1}^{k}\lambda_{max}(M_{i,i})-(k-2)\lambda_{min}(B)\le\sum_{i=1}^{k}\lambda_{max}(M_{i,i})-(k-2)\lambda_{min}(M).$$
Rearranging gives the lemma (p. 170).

*Skip path (our suggestion, if you skip the proofs in 19.6):* carry forward only Lemma 19.5.2 and the zero-diagonal-block argument for Theorem 19.5.1.

## Toy example (ours)
$C_4$ (4-cycle $1\text{–}2\text{–}3\text{–}4\text{–}1$), $d=2$, $n=4$. Laplacian eigenvalues: $0,2,2,4$, so $\lambda_n=4$. Adjacency eigenvalues: $\mu_i=d-\lambda_i=2,0,0,-2$.
- Take $S=\{1,3\}$, independent, $d_{ave}=2$, $s=1/2$. Theorem 19.3.2: $|S|\le 4(1-2/4)=2$. The bound is tight.
- Check the proof: $x=\mathbf 1_S-\tfrac12\mathbf 1=(\tfrac12,-\tfrac12,\tfrac12,-\tfrac12)$. $x^Tx=4\cdot\tfrac14=1=n(s-s^2)=4\cdot\tfrac14$. Each of the 4 edges has $(x(a)-x(b))^2=1$, so $x^TLx=4=d_{ave}|S|=2\cdot2$. The ratio is $4=\lambda_n$.
- Coloring: $\chi\ge1+\mu_1/(-\mu_n)=1+2/2=2$, tight, since $C_4$ is bipartite.

## Concepts
- [[graph-laplacian]] — Laplacian matrix $L$ with eigenvalues $0=\lambda_1\le\dots\le\lambda_n$ (p. 164)
- [[adjacency-matrix]] — eigenvalues indexed $\mu_1\ge\dots\ge\mu_n$, reversed from the Laplacian (p. 164)
- [[rayleigh-quotient]] — $x^TLx/x^Tx$; its maximum is $\lambda_n$ (Courant–Fischer) (p. 165)
- [[independent-set]] — (new) vertex set with no internal edge; $\alpha(G)$ is the largest size (p. 164)
- [[chromatic-number]] — (new) least $k$ with a proper $k$-coloring, $\chi(G)$ (p. 164)
- [[hoffman-bound]] — (new) $\alpha\le n(-\mu_n)/(d-\mu_n)$; generalized by Godsil–Newman with $d_{ave}(S)/\lambda_n$ (p. 165)
- [[hoffman-chromatic-bound]] — (new) $\chi\ge1+\mu_1/(-\mu_n)$, via zero-diagonal block matrices (p. 167)
- [[ramsey-graph]] — (new) $k$-Ramsey: no clique and no independent set of size $k$ (p. 167)
- [[projection]] — $\mathbf 1_S-s\mathbf 1$ is the projection of $\mathbf 1_S$ orthogonal to $\mathbf 1$ (p. 165)

## Canonical instances
- [[paley-graph]] — $\alpha\le\sqrt p$ from Hoffman's bound (p. 167)
- [[clique-with-pendants]] — $\chi=n$, but independence bound gives only 2; Hoffman gives 4.2 (unweighted) and 5.18 (reweighted) for $n=6$ (pp. 167–168)

## Bridges (candidates)
- [structural-analogy] Hoffman bound (test vector $\mathbf 1_S-s\mathbf 1$ in the Rayleigh quotient) ↔ spectral partitioning: both use indicator vectors orthogonalized against $\mathbf 1$ and Rayleigh quotients to bound combinatorial quantities.
- [structural-analogy] Lemma 19.6.1 ↔ Courant–Fischer / eigenvalue interlacing: both bound eigenvalues of $A$ by those of its sub-blocks (the unit uses Theorem 4.3.1 for this).

## Questions this raises
- When is Godsil–Newman's bound tight for non-regular graphs (it is tight for $C_4$ above)?
- Can edge reweighting be optimized to maximize the Hoffman chromatic bound? The unit shows reweighting helped once (5.18 vs 4.2).
- How close do Paley graphs come to explicit Ramsey optimality compared with the Chattopadhyay–Zuckerman graphs?

## Reading notes
- Printed = pdf − 24. The draft date (April 2, 2025) comes from the work citation; it is not printed on these pages.
- Typos in the source: "Recall the we" (p. 164); $\mathbf 1_S L\mathbf 1_S$ lacks the transpose (p. 165); the "$\le$" written in the fourth line of the chain on p. 169 is actually an equality. (Not a typo: "$\mu_{12}$" on p. 168 is correctly the smallest eigenvalue of the 12-vertex example; it only clashes with the use of $n$ for the clique size there.)
- On p. 168, "5.18 agrees with the chromatic number 6" presumably means that the bound rounds up to 6, since $\chi$ is an integer (the text does not say).
- Corollary 7.3.2, Proposition 4.5.4 and Theorem 4.3.1 are cited but not included in these pages. The claim that Paley cliques have size $\le\sqrt p$ is stated without proof.
- Numerical values (5.19, −1.62, 4.2, 5.18) are the author's and were not recomputed.
