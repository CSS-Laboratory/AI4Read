---
id: spielman-2025-sagt/ch08-eigenvalues
work: spielman-2025-sagt
unit: "Chapter 8 — Eigenvalues of Random Graphs"
pages: 69-82
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
# Eigenvalues of Random Graphs

## L0 — One line
Write a random graph's adjacency matrix as the mean matrix $p(J-I)$ (the rank-one matrix $pJ$ minus $pI$) plus a zero-mean random matrix $R$, then show $\|R\|$ is, with high probability, about at most $2\sqrt{np(1-p)}$, by bounding $\mathbb E\,\mathrm{Tr}\,R^l$ through counting closed walks.

## L1 — The gist (≤ 120 words)
What do the adjacency eigenvalues of an Erdős–Rényi random graph (each edge present independently with probability $p$) look like? The chapter says that typically one eigenvalue is near $pn$, and that the rest probably have absolute value at most $(1+o(1))\,2\sqrt{p(1-p)n}$, spread in a semicircle. Only the upper bound is proved. The proof splits the adjacency matrix $M$ into $p(J-I)$ plus a zero-mean noise matrix $R$. A first attempt (for $p=1/2$) uses Hoeffding's inequality for each fixed unit vector, plus a random-vector cap argument, and gives about $(5/3)\sqrt n$. The main proof uses the trace method: for even $l$, $\|R\|^l\le \mathrm{Tr}\,R^l$. It bounds $\mathbb E\,\mathrm{Tr}\,R^l$ by counting closed walks, then applies Markov's inequality.

**Prerequisites:** spectral norm and Rayleigh quotient; trace $=$ sum of eigenvalues; expectation of independent products; Markov's inequality; counting (binomial coefficients); rank-one matrices.

## L2 — Key ideas
- Write $M=p(J-I)+R$ with $\mathbb E R=0$. $p(J-I)$ has eigenvalues $p(n-1)$ and $-p$ ($n-1$ times). So the bulk of $M$'s spectrum is very close to that of $R$, minus $p$ (p. 70–71).
- Adding the rank-one matrix $pJ$ moves the largest eigenvalue a lot and every other eigenvalue by at most to the next one (interlacing, Exercise 1) (p. 71).
- For a fixed unit $x$, $x^TRx$ is concentrated (Hoeffding): $\Pr[|x^TRx|\ge t]\le 2e^{-t^2}$ (p. 72). Passing to all $x$ via a random-vector cap argument gives $\|R\|\lesssim(5/3)\sqrt n$ for $p=1/2$ (p. 72–73).
- Trace method: for even $l$, $\|R\|\le(\mathrm{Tr}\,R^l)^{1/l}$. Expanding $\mathbb E\,\mathrm{Tr}\,R^l$ leaves only "significant" closed walks, in which every pair occurs at least twice (p. 75–76).
- Counting significant walks by their number $k$ of new vertices gives $W_{n,l,k}\le n^{k+1}2^l l^{4(l-2k)}$. This yields $\mathbb E\,\mathrm{Tr}\,R^l\le 2n(4np(1-p))^{l/2}$ for $np(1-p)\ge 2l^8$ (p. 76–80).
- The key counting trick: the first-visit edges form a tree. A vertex-minus-edge counter on once-used tree edges shows that ambiguous steps are at most as many as extra steps (p. 78–80).

## L3 — Walkthrough

**Introduction (p. 69–70).** The chapter studies adjacency eigenvalues of Erdős–Rényi graphs: each edge appears with probability $p$, independently (p. 69). The author states that such graphs typically have one large eigenvalue around $pn$. All the others probably have absolute value at most $(1+o(1))\,2\sqrt{p(1-p)n}$. Their histogram follows Wigner's semicircle law (p. 69). Histograms for $p=1/2$ are shown: all but the largest eigenvalue for $n=4000$; the 99 smallest eigenvalues of 10,000 graphs with $n=100$, almost never outside $[-10,10]$ (p. 69–70). (added step: for $n=100$, $p=1/2$, $2\sqrt{np(1-p)}=2\sqrt{25}=10$.) A histogram of the second-largest eigenvalues of 10,000 matrices with $n=1000$ is shown; $\sqrt{1000}\approx 31.62$ is at the very right end of it (p. 70). Only an upper bound on the bulk is proved; the semicircle shape is not proved.

**8.1 Transformation (p. 70–71).** Let $M$ be the adjacency matrix. Write
$$M=p(J-I)+R,$$
where $J$ is the all-ones matrix and $R$ is symmetric with zero diagonal. Off-diagonal entries are $R(a,b)=1-p$ with probability $p$ and $-p$ with probability $1-p$, so $\mathbb E R=0$ (p. 70). The goal is to show all eigenvalues of $R$ are small w.h.p., so $M\approx p(J-I)$.

$p(J-I)$ has one eigenvalue $p(n-1)$ and $n-1$ eigenvalues $-p$ (p. 71). Subtracting $pI$ from $R$ shifts its eigenvalues down by $p$. Adding $pJ$ (rank one) interlaces: the eigenvalues of $pJ+(R-pI)$ interlace those of $R-pI$ (Exercise 1). The top eigenvalue moves up a lot; the other $n-1$ move up at most to the next eigenvalue (p. 71).

*Intuition note.* Subtracting the mean leaves a zero-mean random matrix $R$. Adding the rank-one term $pJ$ can move the top eigenvalue a lot, but each of the other eigenvalues moves up by at most to the next one.

**8.2 The extreme eigenvalues (p. 71–73).** Assume $p=1/2$, so entries $R(i,j)$ are independent, uniform on $\pm1/2$. Recall $\|R\|=\max_x|x^TRx/x^Tx|$. For a unit $x$, $x^TRx=\sum_{i<j}2R(i,j)x(i)x(j)$, a sum of independent terms with mean 0 (p. 71).

**Theorem 8.2.1 (Hoeffding).** Let $X_i$ be independent with values in $[a_i,b_i]$, $\mu=\mathbb E\sum_iX_i$. For every $t>0$,
$$\Pr\Big[\sum_iX_i\ge\mu+t\Big]\le\exp\Big(-\frac{2t^2}{\sum_i(b_i-a_i)^2}\Big).$$
Take $X_{i,j}=2r_{i,j}x(i)x(j)$ with $a_{i,j}=-x(i)x(j)$, $b_{i,j}=x(i)x(j)$. Then
$$\sum_{i<j}(b_{ij}-a_{ij})^2=\sum_{i<j}4x(i)^2x(j)^2=2\sum_{i\ne j}x(i)^2x(j)^2\le 2\Big(\sum_ix(i)^2\Big)\Big(\sum_jx(j)^2\Big)=2.$$
(p. 71–72).

**Lemma 8.2.2.** For every unit $x$, $\Pr_R[|x^TRx|\ge t]\le 2e^{-t^2}$. Proof: split into the two tails; $R$ and $-R$ have the same distribution; apply Hoeffding to each tail (p. 72).

**8.2.1 Vectors near $v_1$ (p. 72–74).** Lemma 8.2.2 handles one $x$, but $\|R\|$ involves all $x$. Instead of an $\epsilon$-net, the author uses Bayes' rule and:

**Lemma 8.2.3.** For symmetric $R$ and uniform random unit $u$: $\Pr_u\big[|u^TRu|\ge\|R\|/2\big]\ge \dfrac{1}{\sqrt\pi\,n2^{n-1}}$ (p. 72).

**Theorem 8.2.4.** If $R$ is symmetric with zero diagonal and independent off-diagonal entries uniform on $\pm1/2$, then $\Pr[\|R\|\ge t]\le\sqrt\pi\,n2^n e^{-t^2/4}$.
Proof (p. 72–73). The events $|u^TRu|\ge\|R\|/2$ and $\|R\|\ge t$ together imply $|u^TRu|\ge t/2$. Hence
$$\Pr_{R,u}[|u^TRu|\ge t/2]\ge\Pr_R[\|R\|\ge t]\,\Pr_{u,R}\big[|u^TRu|\ge\|R\|/2\;\big|\;\|R\|\ge t\big]\ge\frac{\Pr_R[\|R\|\ge t]}{\sqrt\pi n2^{n-1}},$$
by Bayes' rule and Lemma 8.2.3. By Lemma 8.2.2 and total probability, the left side is at most $2e^{-(t/2)^2}$. Rearranging gives the theorem.

The bound is small once $e^{t^2/4}$ exceeds $\sqrt\pi n2^n$. For large $n$ this holds for $t>2\sqrt{\ln2}\sqrt n\sim(5/3)\sqrt n$ (p. 73). The author notes that $\|R\|$ is known to be unlikely to exceed much more than $\sqrt n$ (Füredi–Komlós, Vu), via the method of the next section (p. 73).

Lemma 8.2.3 follows from two lemmas (p. 73):
- **Lemma 8.2.5.** Let $\psi$ be a unit eigenvector of $R$ whose eigenvalue has absolute value $\|R\|$. If $x$ is a unit vector with $\psi^Tx\ge\sqrt3/2$, then $|x^TRx|\ge\frac12\|R\|$. Proof: take eigenvalues $\lambda_1\ge\dots\ge\lambda_n$, WLOG $\lambda_1\ge|\lambda_n|$, $\psi=\psi_1$. Write $x=\sum_ic_i\psi_i$, so $c_1\ge\sqrt3/2$, $\sum c_i^2=1$. Then
$$x^TRx=\sum_ic_i^2\lambda_i\ge c_1^2\lambda_1-\sum_{i\ge2}c_i^2|\lambda_1|=\lambda_1\Big(c_1^2-\sum_{i\ge2}c_i^2\Big)=\lambda_1(2c_1^2-1)\ge\lambda_1/2.$$
- **Lemma 8.2.6.** For any unit $\psi$ and random unit $x$: $\Pr[\psi^Tx\ge\sqrt3/2]\ge\frac1{\sqrt\pi n2^{n-1}}$. Proof: this is the surface-area ratio of the cap $C=\{x:\psi^Tx\ge\sqrt3/2\}$ to the unit ball $B^n$. Surface area of $B^n$ is $\frac{n\pi^{n/2}}{\Gamma(n/2+1)}$, with $\Gamma(n)=(n-1)!$ and $\Gamma$ increasing for $x\ge1$. The $(n-1)$-dimensional volume spanned by the cap's boundary lower-bounds the cap's area. Its radius is $r=\sin(\mathrm{acos}\sqrt3/2)=1/2$. The ratio is at least
$$\frac{r^{n-1}\pi^{(n-1)/2}/\Gamma(\frac{n-1}2+1)}{n\pi^{n/2}/\Gamma(\frac n2+1)}=\frac{r^{n-1}}{\sqrt\pi n}\frac{\Gamma(\frac n2+1)}{\Gamma(\frac{n-1}2+1)}\ge\frac1{\sqrt\pi n2^{n-1}}.$$
(p. 74).

*Intuition note.* A random direction has a tiny but explicitly bounded chance of lying close to the top eigenvector. A union over "all directions" is replaced by this one small chance, at the price of the factor $2^n$, which costs only a constant in $t/\sqrt n$.

**8.3 The trace method (p. 74–75).** Let $\rho_1,\dots,\rho_n$ be the eigenvalues of $R$. The $k$-th moment is $\sum_i\rho_i^k=\mathrm{Tr}(R^k)$; the first is $\mathrm{Tr}\,R=0$ (p. 74). Power formula: $(A^l)(a,b)=\sum_{c_1,\dots,c_{l-1}\in V}A(a,c_1)A(c_1,c_2)\cdots A(c_{l-1},b)$ (p. 74).

For even $l$, $\|R\|^l\le\mathrm{Tr}(R^l)$, so $\|R\|\le(\mathrm{Tr}\,R^l)^{1/l}$ (p. 75). Theorem 8.4.2 (proved below): for even $l$ with $np(1-p)\ge2l^8$, $\mathbb E\,\mathrm{Tr}\,R^l\le2n(4np(1-p))^{l/2}$. Define
$$u\overset{\text{def}}=\big(2n(4np(1-p))^{l/2}\big)^{1/l}=(2n)^{1/l}\,2\sqrt{np(1-p)}.$$
For $\epsilon>0$, by Markov's inequality,
$$\Pr[\|R\|>(1+\epsilon)u]\le\Pr[\mathrm{Tr}\,R^l>(1+\epsilon)^lu^l]\le\Pr[\mathrm{Tr}\,R^l>(1+\epsilon)^l\,\mathbb E\,\mathrm{Tr}\,R^l]\le(1+\epsilon)^{-l}.$$
(p. 75). This is small when $l>1/\epsilon$. The author says that for $\epsilon<1/2$, $1+\epsilon<\exp(4\epsilon/5)$ (see Reading notes) and that one can take $\epsilon\approx(n/2)^{-1/8}$. The bound tends to 0 as $n\to\infty$ but is not useful for practical $n$ (p. 75). Also $(2n)^{1/l}=\exp(\ln(2n)/l)\le1+1.1\ln(2n)/l$ for $\ln(2n)/l<1/2$, so it is close to 1 when $l\gg\ln(2n)$ (p. 75).

**8.4 Expectation of the trace of a power (p. 75–77).** Expanding,
$$\mathbb E\,R^l(a_0,a_0)=\sum_{a_1,\dots,a_{l-1}\in V}\mathbb E\Big[R(a_0,a_{l-1})\prod_{i=1}^{l-1}R(a_{i-1},a_i)\Big].$$
Entries are independent except for symmetry, so only identical pairs are dependent. If pair $\{b_j,c_j\}$ occurs $d_j$ times in $\{a_0,a_1\},\dots,\{a_{l-1},a_0\}$ \tag{8.1}, the expectation factors as $\prod_j\mathbb E\,R(b_j,c_j)^{d_j}$. This is 0 if some $d_j=1$. For $d\ge2$,
$$\mathbb E\,R^d=p(1-p)\big[(1-p)^{d-1}-(-p)^{d-1}\big]\le p(1-p).\tag{8.2}$$
(p. 76).

Hence $\mathbb E\,R^l(a_0,a_0)$ is at most the sum over sequences in which every pair of (8.1) appears at least twice, times $p(1-p)$ for each distinct pair (p. 76). A *closed walk of length $l$ on $n$ vertices* is $a_0,\dots,a_l$ with $a_i\in[n]$, $a_l=a_0$. It is *significant* if every pair $\{b,c\}$ occurs for at least two indices $i$ as $\{a_i,a_{i+1}\}$. $W_{n,l,k}$ counts significant closed walks with exactly $k$ distinct elements in $a_1,\dots,a_{l-1}$. Since $k$ distinct elements give at least $k$ distinct pairs:

**Lemma 8.4.1.** $\mathbb E\,\mathrm{Tr}\,R^l\le\sum_{k=1}^{l/2}W_{n,l,k}\,(p(1-p))^k$ (p. 76).

Section 8.5 proves $W_{n,l,k}\le n^{k+1}2^ll^{4(l-2k)}$.

**Theorem 8.4.2.** If $l$ is even and $np(1-p)\ge2l^8$, then $\mathbb E\,\mathrm{Tr}\,R^l\le2n(4np(1-p))^{l/2}$.
Proof (p. 77). Let $t_k=n^{k+1}2^ll^{4(l-2k)}(p(1-p))^k$. Then
$$\frac{t_k}{t_{k-1}}=\frac{n\,p(1-p)}{l^8}\ge2.$$
So the $t_k$ grow geometrically and the sum is dominated by the last term:
$$\mathbb E\,\mathrm{Tr}\,R^l\le\sum_{k=1}^{l/2}W(n,l,k)(p(1-p))^k\le\sum_kt_k\le t_{l/2}\sum_{k=1}^{l/2}2^{1-k}\le2t_{l/2}\le2n2^l(np(1-p))^{l/2}.$$
(The printed sum $\sum 2^{1-k}$ is as in the source; the bound by 2 is what is used.) Vu proves the sharper $W_{n,l,k}\le n^{k+1}\binom l{2k}(k+1)^{2(l-2k)}2^{2k}$, which allows much higher powers (p. 77).

*Intuition note.* Because entries have mean zero, only walks that retrace every edge at least twice survive in $\mathbb E\,\mathrm{Tr}\,R^l$. Among these, walks using as many distinct vertices as possible ($k=l/2$) dominate.

**8.5 The number of walks (p. 77–80).** *Crude bound.* Let $S\subset\{1,\dots,l-1\}$ be the indices $i$ where $a_i$ has not appeared earlier. Record $S$ (at most $\binom{l-1}k$ choices), the map $\sigma:S\to[n]$ (at most $n^k$) and $a_0$ ($n$). For $i\notin S$, $a_i=a_j$ for some $j\in S\cup\{0\}$; record this by $\tau:[l-1]\setminus S\to S\cup\{0\}$ (at most $(k+1)^{l-1-k}$ choices). Figure 8.1 shows the walk $b,c,d,a,b,c,e,c,d,a,b$ with $k=4$, $S=\{1,2,3,6\}$, $\sigma(1)=c,\sigma(2)=d,\sigma(3)=a,\sigma(6)=e$, $\tau(4)=0,\tau(5)=1,\tau(7)=1,\tau(8)=2,\tau(9)=3$ (p. 78). Every significant walk arises from some such data, so
$$W_{n,l,k}\le\binom{l-1}kn^{k+1}(k+1)^{l-1-k}.\tag{8.3}$$
This is too loose; it only gives $\|R\|\le c\sqrt{np(1-p)}\log n$. It is loosest at $k=l/2$, which is both the easiest case to tighten and the dominant term in Theorem 8.4.2 (p. 78).

*The tree.* The edges $(a_{i-1},a_i)$, $i\in S$, form a tree: $k$ edges, $k+1$ vertices, connected by induction from $a_0$ (Figure 8.2) (p. 78).

*Case $l=2k$.* Each tree edge must be covered at least twice and the walk has only $l$ steps, so every pair appears exactly twice. Then $\tau$ is unnecessary: for $i\notin S$, the pair $\{a_{i-1},a_i\}$ appeared exactly once before, and $a_{i-1}$ touches exactly one such edge. Proof: track the subgraph of tree edges used exactly once, with $v$ vertices and $e$ edges, always counting the current vertex. Start and end: $v=1$, $e=0$. Steps in $S$ add 1 to both. A non-$S$ step with a unique once-used edge at $a_{i-1}$ lowers both by 1. If $a_{i-1}$ touched two once-used edges, $e$ would drop but $v$ would not; this is impossible since $v-e$ starts and ends at 1 (p. 78–79). Hence
$$W_{n,l,l/2}\le n^{l/2+1}\binom l{l/2}\quad\text{(p. 79)}.$$

*General $k$.* A step $i$ is *extra* if $\{a_{i-1},a_i\}$ is not a tree edge or has already appeared at least twice. The number of extra steps $x$ is at most $l-2k$, as the tree edges use at least $2k$ steps (p. 79). Let $T$ be the steps where $a_{i-1}$ touches exactly one once-used tree edge and the walk follows it (so $a_i$ is inferred). A step is *ambiguous* if $a_{i-1}$ touches more than one once-used tree edge and the walk follows one. Every step outside $S\cup T$ is extra or ambiguous. So $\tau:[l-1]\setminus(S\cup T)\to S\cup\{0\}$, and $a_0,S,T,\sigma,\tau$ determine the walk (p. 79–80). If ambiguous steps number at most extra steps, then $|[l-1]\setminus(S\cup T)|\le2x$ (the source writes $V\setminus(S\cup T)$), so $\tau$ has at most $(k+1)^{2x}$ choices. The choices of $S,T$ number at most $\binom{l-1}k\binom{l-1-k}{2x}\le2^{l-1}(l-1-k)^{2x}$. Thus
$$W_{n,l,k}\le n^{k+1}2^{l-1}(l-k-1)^{2x}(k+1)^{2x}\le n^{k+1}2^{l-1}(lk)^{2(l-2k)}\le n^{k+1}2^ll^{4(l-2k)}.\tag{8.4}$$

*Ambiguous $\le$ extra.* Track $v$ and $e$ again (start and end $v-e=1$). Steps in $S$: both $+1$. Steps in $T$: $a_{i-1}$ has degree one, so both $-1$. Ambiguous steps: $e$ drops by 1 but $v$ does not, so $v-e$ increases. Extra steps do not change the edge count but can lower $v$ (when $a_{i-1}$ has no once-used edge but $a_i$ does), so they can decrease $v-e$. Since $v-e$ returns to its start value, extra steps are at least as many as ambiguous steps (p. 80).

*Intuition note.* Almost every step of a walk is determined by the past, so only the few "extra" and "ambiguous" steps (at most $2x\le 2(l-2k)$ in all) need a recorded choice. That is why the count of $\tau$ falls from $(k+1)^{l-1-k}$ to $(k+1)^{2(l-2k)}$.

**8.6 Notes (p. 80).** This proof is a slight simplification and weakening of a result of Vu. Füredi and Komlós first claimed the result, with a few mistakes in their paper. Vu also gives concentration results lower-bounding $\mu_2$, whereas this chapter gives only an upper bound (p. 80).

**8.7 Exercise (p. 81).** Interlacing: see Exercises.

## Toy example (ours)
Check the trace chain for $p=1/2$, $l=2$, $n=2$. Then $R=\begin{pmatrix}0&r\\r&0\end{pmatrix}$ with $r=\pm1/2$. Eigenvalues are $\pm r$, so $\|R\|=1/2$ and $\|R\|^2=1/4$. $\mathrm{Tr}\,R^2=r^2+r^2=1/2\ge1/4$. ✓.
Now expectation for general $n$: $\mathrm{Tr}\,R^2=\sum_{a,b}R(a,b)^2=n(n-1)\cdot\tfrac14$ (each off-diagonal entry squares to $1/4$). For $n=3$ this is $6/4=1.5$. Significant closed walks with $l=2$: $a_0,a_1,a_0$ with $k=1$, so $W_{3,2,1}\le9$, matching the crude bound $\binom{1}{1}n^2=9$ from (8.3). Lemma 8.4.1 gives $\mathbb E\,\mathrm{Tr}\,R^2\le9\cdot p(1-p)=9/4=2.25\ge1.5$ ✓. (The condition $np(1-p)\ge 2l^8$ of Thm 8.4.2 does not hold at this size; this only illustrates Lemma 8.4.1.)

## Concepts
- [[erdos-renyi-random-graph]] (new) — each edge present independently with probability $p$ (p. 69)
- [[adjacency-matrix]] — $M$; here split as $p(J-I)+R$ (p. 70)
- [[rank-one-matrix-outer-product]] — $J$ is rank one; adding it interlaces eigenvalues (p. 71)
- [[eigenvalue-interlacing]] (new) — adding a rank-one matrix interlaces the eigenvalues: the top one moves up a lot, the others at most to the next one; Exercise 1 states $\beta_i\ge\alpha_i\ge\beta_{i+1}$ for $B=A+xx^T$ (p. 71, 81)
- [[norm]] — spectral norm $\|R\|=\max_x|x^TRx/x^Tx|$ (p. 71)
- [[rayleigh-quotient]] — $x^TRx/x^Tx$, bounded for fixed $x$ by Hoeffding (p. 71–72)
- [[hoeffding-inequality]] (new) — tail bound for sums of independent bounded variables (p. 71)
- [[wigner-trace-method]] (new) — bound $\|R\|$ via $\mathbb E\,\mathrm{Tr}\,R^l$ for even $l$ (p. 74–75)
- [[significant-closed-walk]] (new) — closed walk with every pair traversed at least twice; counted by $W_{n,l,k}$ (p. 76)
- [[semicircle-law]] (new) — the eigenvalue histogram of $R$ looks like a semicircle; stated, not proved (p. 69)

## Canonical instances
- [[erdos-renyi-adjacency-spectrum]] (new) — $M=p(J-I)+R$ with the histograms of Section 8 intro (p. 69–70)
- [[example-walk-figure-8-1]] (new) — walk $b,c,d,a,b,c,e,c,d,a,b$ with its $S,\sigma,\tau$ and tree (p. 78–79)

## Bridges (candidates)
- [structural-analogy] Trace method: $\mathrm{Tr}\,R^l$ as a sum over closed walks ↔ adjacency matrix: $(A^k)_{ij}$ counts walks of length $k$ — same expansion, but weighted by random entries here.
- [same-math] Interlacing under $+pJ$ ↔ rank-one updates of a symmetric matrix: same eigenvalue-ordering statement (Exercise 1).
- [structural-analogy] Random-graph bulk edge $\approx2\sqrt{np(1-p)}$ ↔ network null models: a spectrum showing only noise would sit inside this bulk.

## Questions this raises
- What does the semicircle law say beyond the norm bound, and what extra work proves it?
- How much does the bound $\|R\|\lesssim 2\sqrt{np(1-p)}$ weaken for small $p$ (the sparse case, where $np(1-p)\ge2l^8$ fails)?
- Can the $\epsilon$-net route reach $\sqrt n$ without the trace method?
- How does the second-largest eigenvalue of $M$ relate to the largest of $R$ via interlacing, quantitatively?

## Exercises worth doing
- Ex. 1 (p. 81) — Interlacing: for symmetric $A$ and $B=A+xx^T$, prove $\beta_i\ge\alpha_i\ge\beta_{i+1}$; used in Section 8.1 — difficulty: medium

## Reading notes
- Printed page = pdf page − 24. Pages 93–106 pdf cover printed 69–82; p. 82 holds only the caption of Figure 8.3 ("An example walk along with v and e"); the figure itself is not visible and is never referenced in the text.
- Section 8.2 says the general-$p$ case is explained "at the end"; no such explanation appears in these pages, though Section 8.4 treats general $p$.
- p. 75: the text prints "for $\epsilon<1/2$, $1+\epsilon<\exp(4\epsilon/5)$". The inequality needed for the argument runs the other way, $1+\epsilon\ge\exp(4\epsilon/5)$ (added remark; e.g. $\ln1.5\approx0.405>0.4$).
- p. 73: the eigenbasis is named $\psi_i$ but the expansion is printed with $v_i$. p. 74: the radius of the sphere is written $R$ in a formula that uses $r$. In 8.5 the edge counter is called both $f$ and $e$; "$V\setminus(S\cup T)$" should be $[l-1]\setminus(S\cup T)$.
- In Figure 8.1, $a_1,\dots,a_9$ contain 5 distinct vertices but $k=4=|S|$, because $a_0=b$ reappears. So "$k$ distinct elements in $a_1,\dots,a_{l-1}$" is used loosely; the proof uses $k=|S|$ and a tree on $k+1$ vertices.
- Histograms are described only by the text and the images; their axis labels are small.
