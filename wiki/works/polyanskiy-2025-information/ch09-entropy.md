---
id: polyanskiy-2025-information/ch09-entropy
work: polyanskiy-2025-information
unit: "Chapter 8 (file ch09), Entropy method in combinatorics and geometry"
pages: 158-165
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Entropy method in combinatorics and geometry

## L0 — One line
To bound the size of a set, draw a uniform random element: its entropy is $\log|C|$, so any upper bound on its joint entropy bounds $|C|$.

## L1 — The gist (≤ 120 words)
How can Shannon entropy bound how many objects of some kind exist? Draw one object uniformly at random from the set. Its entropy is the log of the set's size. Then bound that joint entropy in one of three ways: by the sum of marginals, by Shearer's lemma (pairwise bound), or by the chain rule. The chapter applies these to binary vectors with a given average weight (Massey), subgraph counts (triangles, general $H$), and Brégman's permanent bound. Differential-entropy analogues give the Bollobás–Thomason and Loomis–Whitney inequalities about projection volumes. It matters because one short entropy argument can give bounds that other methods reach by different routes; for example, a linear-algebra proof gives the same triangle bound (Remark 8.1, p. 160).

**Prerequisites:** entropy, conditional entropy, chain rule; Jensen's inequality; Han's/Shearer's inequality (Thm 1.8); differential entropy (Thm 2.7); basic graph theory and linear programming.

## L2 — Key ideas (5–10 bullets)
- Counting recipe: a uniform element of $C$ has entropy $\log|C|$. Upper-bound its joint entropy by the marginal bound, Shearer's lemma or the chain rule (p. 158).
- Marginal bound plus Jensen gives $|C|\le e^{nh(p)}$, and hence $\sum_{j\le k}\binom nj\le e^{nh(k/n)}$ for $k\le n/2$ (pp. 158–159).
- Shearer's lemma gives $N(K_3,G)\le\frac{\sqrt2}{3}m^{3/2}$ and, for general $H$, $N(H,m)\asymp m^{\rho^*(H)}$ with $\rho^*$ the fractional covering number (the value of a linear program defined on p. 160) (pp. 160–161).
- A naive marginal bound for perfect matchings is exponentially too weak. The proof of Brégman's bound applies the chain rule in a uniformly random vertex order (the 'key idea'; here $\mathrm{perm}(A)$, the permanent, is the number of perfect matchings of a bipartite graph) (pp. 162–163).
- Key lemma: in that random order the number of available choices $N_k$ is uniform on $[d_k]$, giving $\mathrm{perm}(A)\le\prod_i(d_i!)^{1/d_i}$ (pp. 163–164).
- With differential entropy, a box built from $\log a_i=h(X_i|X^{i-1})$ has the same volume as $K$ and coordinate projections that are no larger (Bollobás–Thomason). Loomis–Whitney follows (pp. 164–165).

## L3 — Walkthrough

**Chapter intro (p. 158).** To count $C$, draw $X=(X_1,\dots,X_n)$ uniformly from $C$. Then $\log|C|=H(X)$. Three bounds on $H(X_1,\dots,X_n)$ are used:
- marginal: $\le\sum_i H(X_i)$;
- pairwise (Shearer, Thm 1.8): $\le\frac1{n-1}\sum_{i<j}H(X_i,X_j)$;
- chain rule (exact): $=\sum_i H(X_i|X_1,\dots,X_{i-1})$.

### 8.1 Binary vectors of average weights
**Lemma 8.1 (Massey).** Let $C\subset\{0,1\}^n$ and $p=\frac1{|C|}\sum_{x\in C}\frac{w_H(x)}{n}$, where $w_H$ is the number of 1's. Then $|C|\le\exp\{nh(p)\}$, even if $p>1/2$ (p. 158). Here $h$ is the binary entropy function.

*Proof.* Let $p_i=P[X_i=1]$.
- $\log|C|=H(X)\le\sum_i H(X_i)=\sum_i h(p_i)$ (p. 158).
- Averaging over vectors first or over bits first gives $p=\frac1n\sum_i p_i$ (p. 159).
- $h$ is concave, so Jensen gives $\sum_i h(p_i)\le n\,h(\frac1n\sum_i p_i)=nh(p)$ (p. 159).

**Theorem 8.2.** $\sum_{j=0}^k\binom nj\le\exp\{nh(k/n)\}$ for $k\le n/2$. Take $C=\{x:w_H(x)\le k\}$ (the Hamming ball). Lemma 8.1 gives $|C|\le e^{nh(p)}$. Then $h$ is increasing on $[0,1/2]$, so $e^{nh(p)}\le e^{nh(k/n)}$ (p. 159). (added step: this uses $p\le k/n\le1/2$.)
The text also notes that this follows from the Chernoff bound $P(\mathrm{Bin}(n,1/2)\le k)\le\exp\{-nd(\frac kn\|\frac12)\}$ (p. 159).

*Intuition note.* Few vectors can be "spread out" over many bit patterns if each bit is biased. Entropy per bit is at most $h(p)$, whatever the dependence between bits.

### 8.2 Shearer's lemma and counting subgraphs
The section first recalls the special case $H(X_1,X_2,X_3)\le\frac12[H(X_1,X_2)+H(X_2,X_3)+H(X_1,X_3)]$ of Shearer's lemma (Han's inequality), which is classically used to bound the size of a set in $\mathbb R^3$ by the sizes of its projections (p. 159). $N(H,G)$ is the number of subgraphs of $G$ isomorphic to $H$. Also $N(H,G)=\mathrm{inj}(H,G)/|\mathrm{Aut}(H)|$, where inj counts edge-preserving injective vertex maps (fn. 1, p. 160). $N(H,m)=\max_{G:|E(G)|\le m}N(H,G)$.

**Triangles: $N(K_3,m)\asymp m^{3/2}$ (8.1).**
- Lower bound: $G=K_n$ has $m=\binom n2\asymp n^2$ and $N=\binom n3\asymp n^3\asymp m^{3/2}$ (p. 160).
- Upper bound: draw a labeled triangle $(X_1,X_2,X_3)$ uniformly. There are $3!\,N(K_3,G)$ of them. Shearer gives
$$\log(3!N(K_3,G))=H(X_1,X_2,X_3)\le\tfrac12[H(X_1,X_2)+H(X_2,X_3)+H(X_1,X_3)]\le\tfrac32\log(2m).$$
Each pair is an ordered edge, so it takes at most $2m$ values. Hence
$$N(K_3,G)\le\frac{\sqrt2}{3}m^{3/2}.\tag{8.2}$$
(p. 160)
- Remark 8.1: the linear-algebra route gives the same bound. With adjacency eigenvalues $\lambda_i$, $2|E|=\mathrm{tr}(A^2)=\sum\lambda_i^2$ and $6N(K_3,G)=\mathrm{tr}(A^3)=\sum\lambda_i^3$. Minkowski's inequality gives $(6N)^{1/3}\le(2|E|)^{1/2}$ (p. 160).

**Fractional covering number**, a linear program:
$$\rho^*(H)=\min_w\Big\{\sum_{e\in E}w(e):\ \sum_{e\ni v}w(e)\ge1\ \forall v\in V,\ w(e)\in[0,1]\Big\}.\tag{8.3}$$
With $\{0,1\}$ constraints one gets the covering number $\rho(H)$ (fn. 2, p. 160). For $K_3$, $\rho^*=3/2$ (p. 161).

**Theorem 8.3 (Alon; Friedgut–Kahn).** $c_0(H)m^{\rho^*(H)}\le N(H,m)\le c_1(H)m^{\rho^*(H)}$ (8.4) (p. 160).

*Upper bound.* Let $V(H)=[n]$ and let $w^*$ solve (8.3). Draw a uniform random copy of $H$ in $G$. Let $X_i$ be the vertex of $G$ playing the role of vertex $i$ of $H$. Pick a random edge $e$ of $H$ with probability $w^*(e)/\rho^*(H)$, and let $S$ be its two endpoints. Then $P[i\in S]\ge1/\rho^*(H)$ for all $i$. Applying Thm 1.8:
$$\log N(H,G)=H(X)\le\rho^*(H)\,H(X_S|S)\le\rho^*(H)\log(2m),$$
since $X_S$ takes at most $2m$ values. So $N(H,G)\le(2m)^{\rho^*(H)}$ (p. 161). For $K_3$ this is weaker than (8.2). To recover (8.2), take $X$ uniform on injective homomorphisms $H\to G$ (fn. 3, p. 161).

*Lower bound.* Use the dual LP, the fractional packing number
$$\alpha^*(H)=\max_\psi\Big\{\sum_v\psi(v):\ \psi(v)+\psi(w)\le1\ \forall (vw)\in E,\ \psi(v)\in[0,1]\Big\}\tag{8.5}$$
By LP duality $\alpha^*=\rho^*$. Build $G$ as follows.
1. Replicate each vertex $v$ of $H$ $m(v)$ times.
2. Replace each edge $(vw)$ by the complete bipartite graph $K_{m(v),m(w)}$.
3. Then $|E(G)|=\sum_{(vw)\in E(H)}m(v)m(w)$ and $N(G,H)\ge\prod_v m(v)$.
4. Take $m(v)=\lceil M^{\psi(v)}\rceil$ with $\psi$ the maximizer of (8.5). Then $|E(G)|\le\sum 4M^{\psi(v)+\psi(w)}\le4M|E(H)|$ and $N(G,H)\ge\prod_vM^{\psi(v)}=M^{\alpha^*(H)}$ (p. 161).

*Intuition note.* Shearer's lemma says that if each coordinate is "covered" by the sampled edge with probability at least $1/\rho^*$, the joint entropy is at most $\rho^*$ times the conditional entropy of one edge's endpoints given which edge $S$ was drawn. Each edge has at most $2m$ possible endpoint pairs, so the count is at most $(2m)^{\rho^*}$.

### 8.3 Brégman's theorem
The **permanent** is $\mathrm{perm}(A)=\sum_{\pi\in S_n}\prod_{i=1}^na_{i\pi(i)}$. For a bipartite graph with $n$ vertices on each side, it equals the number of perfect matchings (p. 162).

**Theorem 8.4 (Brégman).** $\mathrm{perm}(A)\le\prod_{i=1}^n(d_i!)^{1/d_i}$, where $d_i$ is the degree of left vertex $i$ (p. 162).
- $K_{n,n}$: $\mathrm{perm}=n!=[(n!)^{1/n}]^n$.
- $n/d$ disjoint copies of $K_{d,d}$: the bound is tight, $\mathrm{perm}=(d!)^{n/d}$ (p. 162).

*Proof* (Radhakrishnan). Assume $\mathrm{perm}(A)>0$. Let $X_i$ be the right vertex matched to left vertex $i$ in a uniform random perfect matching.
- *Attempt 1 (marginals):* $\log\mathrm{perm}=H(X)\le\sum H(X_i)\le\sum\log d_i$. This gives $\mathrm{perm}\le\prod d_i$. It is exponentially worse than Brégman, because $\prod(d_i!)^{1/d_i}\sim(\prod d_i)e^{-n}$ by Stirling (p. 162).
- *Attempt 2 (chain rule):* $H(X)=\sum_iH(X_i|X_1,\dots,X_{i-1})\le\sum_i E[\log N_i]$. Here $N_i$ is the number of values $X_i$ can take given $X_1,\dots,X_{i-1}$. This is hard to continue, because only degrees are known, not the graph (p. 163).
- *Key idea:* label the vertices in a random order. Take $\pi$ uniform on $S_n$, independent of $X$:
$$\log\mathrm{perm}(A)=H(X)=H(X|\pi)=\sum_{k=1}^nH(X_k\mid\{X_j:\pi^{-1}(j)<\pi^{-1}(k)\},\pi)\le\sum_{k=1}^nE\log N_k.$$
Here $N_k$ is the number of choices for vertex $k$ given the earlier-revealed ones. The expectation is over $(X,\pi)$ (p. 163).

**Lemma 8.5.** $N_k$ is uniform on $[d_k]$. Then
$$E_{(X,\pi)}\log N_k=\frac1{d_k}\sum_{i=1}^{d_k}\log i=\log(d_k!)^{1/d_k},$$
so $\log\mathrm{perm}(A)\le\sum_k\log(d_k!)^{1/d_k}$, which is the theorem (p. 163).

*Proof of Lemma 8.5.* The claim holds even conditioned on the whole matching $X$. Fix a perfect matching and let $d=d_k$. Let $J_1,\dots,J_d$ be the nodes matched to the neighbours of $k$, with $J_1=k$. The random $\pi$ orders the $J_i$ uniformly among $d!$ orders. If $J_1$ lands in position $\ell$, then $N_k=d-\ell+1$. So $\ell$ and $N_k$ are uniform (pp. 163–164).

Example 8.1 (p. 163): in a 3-vertex example with $d_1=2$, $N_1$ is 2 or 1 depending on the order. The text finds the two values equally likely.

*Intuition note.* In a fixed order we cannot control $N_i$, because only the degrees are known, not the graph. In a random order, for a vertex of degree $d$, $N_k$ is equally likely to be any of $1,\dots,d$ (Lemma 8.5). Averaging $\log N_k$ over these values gives $\frac1d\log d!$, which is the $(d!)^{1/d}$ in the bound.

### 8.4 Euclidean geometry
$K_S$ is the projection of compact $K\subset\mathbb R^n$ onto the coordinates in $S$ (compactness makes projections measurable, fn. 4).

**Theorem 8.6 (Bollobás–Thomason box theorem).** There is a rectangle $A$ with $\mathrm{Leb}(A)=\mathrm{Leb}(K)$ and $\mathrm{Leb}(A_S)\le\mathrm{Leb}(K_S)$ for all $S\subset[n]$ (p. 164).

*Proof.* Let $X^n$ be uniform on $K$, so $h(X^n)=\log\mathrm{Leb}(K)$. Let $A$ have sides $a_1\times\dots\times a_n$ with $\log a_i=h(X_i|X^{i-1})$.
- By Thm 2.7(a), $h(X_S)\le\log\mathrm{Leb}(K_S)$.
- By the chain rule and "conditioning reduces differential entropy" (Thm 2.7(a),(c)):
$$h(X_S)=\sum_{i=1}^n\mathbf 1\{i\in S\}h(X_i|X_{[i-1]\cap S})\ge\sum_{i\in S}h(X_i|X^{i-1})=\log\prod_{i\in S}a_i=\log\mathrm{Leb}(A_S).$$
- (added step) For $S=[n]$ the chain rule gives $\sum_i\log a_i=h(X^n)=\log\mathrm{Leb}(K)$, so $\mathrm{Leb}(A)=\mathrm{Leb}(K)$ (p. 164).

**Corollary 8.7 (Loomis–Whitney).** With $K_{j^c}$ the projection onto $[n]\setminus j$,
$$\mathrm{Leb}(K)\le\prod_{j=1}^n\mathrm{Leb}(K_{j^c})^{\frac1{n-1}}.\tag{8.6}$$
*Proof.* Take a rectangle $A$ with $\mathrm{Leb}(A)=\mathrm{Leb}(K)$. Then $\mathrm{Leb}(K)=\mathrm{Leb}(A)=\prod_j\mathrm{Leb}(A_{j^c})^{1/(n-1)}$ (each side $a_i$ occurs in $n-1$ factors; added step). Then use $\mathrm{Leb}(A_{j^c})\le\mathrm{Leb}(K_{j^c})$ from Thm 8.6 (p. 165).

Reading (p. 165): with average width $w_j=\mathrm{Leb}(K)/\mathrm{Leb}(K_{j^c})$, (8.6) is equivalent to $\mathrm{Leb}(K)\ge\prod_jw_j$. The volume of $K$ is at least that of the rectangle of average widths.

*Intuition note.* For a given volume, there is a box whose coordinate projections are no larger than those of $K$ (Thm 8.6). So the volume of $K$ is controlled by its projections.

## Toy example (ours)
Let $n=3$, $C=\{110,101,011\}$. Then $p=\frac23$ and $|C|=3$.
- Uniform $X$ on $C$: $H(X)=\log_23=1.585$ bits.
- Each coordinate has $P[X_i=1]=\frac23$. So $h(2/3)=\frac23\log_2\frac32+\frac13\log_23=0.390+0.528=0.918$ bits.
- Marginal bound: $\sum H(X_i)=3(0.918)=2.755\ge1.585$.
- Lemma 8.1: $|C|=3\le2^{2.755}\approx6.75$.

The bound holds but is not tight. For $C=\{0,1\}^2$, $p=\frac12$ and $2^{2h(1/2)}=4=|C|$, so it is tight.

## Concepts
- [[entropy-method]] (new) — count a set via the entropy $\log|C|$ of a uniform element (p. 158)
- [[entropy]] — joint entropy of $X$ equals $\log|C|$ for uniform $X$ on $C$ (p. 158)
- [[chain-rule]] — $H(X_1..X_n)=\sum H(X_i|X^{i-1})$, used in exact and random-order form (pp. 158, 163)
- [[shearers-lemma]] (new) — bounds joint entropy by entropy of projections to subsets covering each coordinate often enough (pp. 158, 160)
- [[joint-and-conditional-entropy]] — conditioning reduces entropy, used for $h(X_S)$ bounds (p. 164)
- [[differential-entropy]] — $h(X^n)=\log\mathrm{Leb}(K)$ for $X^n$ uniform on $K$ (p. 164)
- [[fractional-covering-number]] (new) — LP value $\rho^*(H)$; sets the exponent in $N(H,m)\asymp m^{\rho^*}$ (p. 160)
- [[permanent]] (new) — $\sum_\pi\prod a_{i\pi(i)}$; the number of perfect matchings of a bipartite graph (p. 162)

## Canonical instances
- [[massey-lemma]] — $|C|\le e^{nh(p)}$ from the marginal bound plus Jensen (p. 158)
- [[hamming-ball-volume-bound]] — $\sum_{j\le k}\binom nj\le e^{nh(k/n)}$ (p. 159)
- [[triangle-counting-shearer]] — $N(K_3,G)\le\frac{\sqrt2}{3}m^{3/2}$ (p. 160)
- [[bregman-theorem]] — permanent bound via random-order chain rule (p. 162)
- [[loomis-whitney]] — volume bounded by projection volumes (p. 165)

## Bridges (candidates)
- [structural-analogy] Shearer's lemma (discrete) ↔ Loomis–Whitney (geometry): the text calls the latter a continuous counterpart of the former.
- [structural-analogy] Marginal-bound proof of Thm 8.2 ↔ large deviations: the same inequality follows from a Chernoff bound with KL divergence (p. 159).
- [metaphor] Random-order averaging in Brégman's proof ↔ probability: symmetrization by a random permutation — averaging over orders removes dependence on unknown structure.

## Questions this raises
- Why does the random-order trick make the conditional entropies exactly computable, where a fixed order does not?
- When is the marginal bound (Lemma 8.1) tight, and what does it say about the Hamming-ball volume as $n\to\infty$?
- Footnote 3 says the proof as written is weaker for $K_3$ than (8.2). How much does a better choice of $X$ (injective homomorphisms) improve constants in general?
- Can the box theorem be extended beyond coordinate projections?

## Reading notes
- Printed chapter number is 8 ("8 Entropy method…"); the unit id says ch09. Printed pages 158–165 correspond to pdf 183–190 (printed = pdf − 25).
- Source text on p. 164 (just after Thm 8.6) states that rectangles are extremal for "maximizing volumes of coordinate projections". Thm 8.6 (and the sentence introducing it) give $\mathrm{Leb}(A_S)\le\mathrm{Leb}(K_S)$, i.e. minimizing.
- In Example 8.1 (p. 163), the cases 213 and 312 are each printed with probability 1/3, but each is one permutation of probability 1/6. The totals still give 1/2 for each value of $N_k$.
- Brégman's theorem uses $d_i$ for left-vertex degree. The proof of Lemma 8.5 speaks of the "$k$-th (right) node" (p. 163). The text also mixes indices $k$ and $i$ in the displayed averages.
- The notation $N(G,H)$ appears with arguments swapped in the lower-bound proof (p. 161).
- Graph pictures in the $N(H,G)$ examples (p. 160) are not described here; the numbers 4 and 8 are given there.
- Exercises I.1 and I.2 are referenced (p. 159) but not part of this unit.
