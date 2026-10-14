---
id: bryan-2006-eigenvector/main
work: bryan-2006-eigenvector
unit: paper
pages: 1-11
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# The $25,000,000,000 Eigenvector: The Linear Algebra Behind Google

## L0 — One line
PageRank scores are the unique positive, sum-one eigenvector (eigenvalue 1) of the column-stochastic matrix $M=(1-m)A+mS$ (for $0<m\le1$), and power iteration finds it.

## L1 — The gist (≤ 120 words)
How can a search engine rate the importance of every web page? The authors let each page split one vote among its outgoing links, weighted by its own score. This gives the eigenvector problem $Ax=x$. The problem can fail: if the web splits into disconnected parts, the eigenspace has dimension above 1 and the ranking is not unique. Mixing $A$ with the all-$1/n$ matrix $S$ gives a positive matrix $M$ (for $m>0$). For positive column-stochastic matrices, the eigenspace for eigenvalue 1 has dimension exactly one and its vectors are strictly positive or strictly negative. Power iteration converges to this eigenvector geometrically, and each step is cheap because $A$ is sparse.

**Prerequisites:** eigenvalues and eigenvectors; linear independence, dimension and subspaces; matrix–vector multiplication; triangle inequality; vector norms; proof by contradiction. Terms used above: *column-stochastic* = all entries $\ge0$ and every column sums to 1; *positive matrix* = all entries $>0$; *eigenspace* = all eigenvectors for one eigenvalue (with 0); *power iteration* = repeatedly multiplying a start vector by the matrix; *sparse* = mostly zero entries; *1-norm* = sum of absolute values of the entries; *zero-sum subspace* = vectors whose entries sum to 0.

## L2 — Key ideas (5–10 bullets)
- A page's score is the sum, over pages linking to it, of (their score ÷ their number of outgoing links). This gives $Ax=x$, so ranking becomes an eigenvector problem (p. 2–3).
- If no page is dangling (has no outgoing links), $A$ is column-stochastic and always has eigenvalue 1, because $A^Te=e$ (p. 3).
- Ranking can be non-unique: a web with $r$ disconnected subwebs gives $\dim V_1(A)\ge r$. Dangling nodes are a second problem, which the paper sets aside (p. 4–5).
- The remedy is $M=(1-m)A+mS$; Google reportedly used $m=0.15$. For $m\in(0,1]$ the matrix $M$ is positive and column-stochastic (p. 6).
- Positive and column-stochastic implies $\dim V_1(M)=1$ with strictly signed eigenvectors. This is proved by contradiction using a triangle-inequality argument (Props. 2–3, Lemma 3.2) (p. 7).
- On the zero-sum subspace, $M$ shrinks the 1-norm by a factor $c<1$, so $M^kx_0\to q$ for any positive start with $\|x_0\|_1=1$ (Props. 4–5) (p. 8–9).
- In the example the error ratio is $0.85=1-m$, the second-largest eigenvalue; in general $|\lambda_2|\le 1-m$ is cited, so convergence is much faster than the bound $c^k$. Using $(1-m)Ax+ms$ avoids dense $n^2$ multiplication (p. 9–10).
- Probabilistic reading: $q_j$ is the long-run fraction of time a random surfer spends on page $j$ (p. 10).

## L3 — Walkthrough

### 1. Introduction (p. 1)
A search engine crawls, indexes and rates pages. The paper focuses on step 3, rating importance. Its question: how can one define and quantify the "importance" of a page in a web of links? The authors say rated importance is a significant factor in how links are presented, but not the only one (p. 1).

### 2. Developing a formula to rank pages

**2.1 Basic idea (p. 2–3).**
- A page's *importance score* $x_k\ge 0$ comes from its *backlinks* (links to it from other pages). A larger $x_j$ means a more important page (p. 2).
- The web is a *directed graph*: vertices are pages, and edges are links with a direction (p. 2, footnote 1).
- Counting backlinks in Fig. 2.1 gives $x=(2,1,3,2)$. This ignores that a link from an important page should count more (p. 2).
- A first fix: a page's score is the sum of the scores of the pages linking to it. For page 1 this gives $x_1=x_3+x_4$, which is self-referential (p. 2).
- Second fix: a page with $n_j$ outgoing links gives each target $x_j/n_j$. Each page thus casts one vote, weighted by its score and split evenly. Self-links are not counted (p. 2–3). With $L_k$ the set of backlinks of page $k$:
$$x_k=\sum_{j\in L_k}\frac{x_j}{n_j}.\tag{2.1}$$
- For Fig. 2.1: $x_1=x_3/1+x_4/2$, $x_2=x_1/3$, $x_3=x_1/3+x_2/2+x_4/2$, $x_4=x_1/3+x_2/2$. In matrix form $Ax=x$ with $x=[x_1\,x_2\,x_3\,x_4]^T$ (shape $4\times1$) and $A$ $4\times4$ (p. 3):
$$A=\begin{bmatrix}0&0&1&\tfrac12\\ \tfrac13&0&0&0\\ \tfrac13&\tfrac12&0&\tfrac12\\ \tfrac13&\tfrac12&0&0\end{bmatrix}\tag{2.2}$$
- So we seek an eigenvector of the "link matrix" $A$ for eigenvalue 1. Here the eigenvectors are all multiples of $[12\ 4\ 9\ 6]^T$. Scaled to sum 1: $x_1=12/31\approx0.387$, $x_2=4/31\approx0.129$, $x_3=9/31\approx0.290$, $x_4=6/31\approx0.194$. Page 3 is not top even though all pages link to it: it links only to page 1, so its whole vote goes there (p. 3).
- In general $A_{ij}=1/n_j$ if page $j$ links to page $i$, else 0. Column $j$ has $n_j$ entries equal to $1/n_j$, so it sums to 1 (p. 3).
- **Definition 2.1.** A square matrix is *column-stochastic* if all entries are $\ge0$ and each column sums to 1. A web with no dangling nodes (pages with no outgoing links) has such an $A$ (p. 3).
- **Proposition 1.** Every column-stochastic matrix has 1 as an eigenvalue. *Proof.* With $e$ the all-ones vector, $A^Te=e$. So 1 is an eigenvalue of $A^T$, hence of $A$ (they share eigenvalues) (p. 3).
- $V_1(A)$ denotes the eigenspace for eigenvalue 1 (p. 3).

*Intuition note.* Each column of $A$ describes how one page hands out its single vote. Because every column sums to 1, the all-ones vector $e$ is fixed by $A^T$ (that is, $A^Te=e$). That is why eigenvalue 1 is guaranteed.

**2.2 Shortcomings (p. 3–5).**

*2.2.1 Non-unique rankings.*
- We want $\dim V_1(A)=1$, so that exactly one eigenvector has $\sum x_i=1$. This holds for Fig. 2.1, and always for a *strongly connected* web (you can get from any page to any other in finitely many steps); see Exercise 10 (p. 3–4).
- It fails for Fig. 2.2 (subwebs $W_1=\{1,2\}$, $W_2=\{3,4,5\}$). There $V_1(A)$ is two-dimensional, with basis $x=[\tfrac12,\tfrac12,0,0,0]^T$ and $y=[0,0,\tfrac12,\tfrac12,0]^T$. Every combination is also in $V_1(A)$; e.g. $\tfrac34x+\tfrac14y=[3/8,3/8,1/8,1/8,0]^T$. It is unclear which to use (p. 4).
- **Claim.** If the web, viewed as an undirected graph, has $r$ disconnected subwebs $W_1,\dots,W_r$, then $\dim V_1(A)\ge r$. So no unique score vector with $\sum x_i=1$ exists (p. 4).
- *Argument.* Let $n_i$ be the number of pages in $W_i$, $N_i=\sum_{j\le i}n_j$, $N_0=0$. Index $W_i$'s pages $N_{i-1}+1,\dots,N_i$. Then $A$ is block diagonal, $A=\mathrm{diag}(A_1,\dots,A_r)$ with zero blocks off the diagonal. Each $A_i$ ($n_i\times n_i$) is column-stochastic, so has an eigenvector $v^i\in\mathbb R^{n_i}$ for eigenvalue 1 (Prop. 1). Let $w^i\in\mathbb R^n$ equal $v^i$ in block $i$ and 0 elsewhere. Then $Aw^i=w^i$, and the $w^i$ are linearly independent. So $\dim V_1(A)\ge r$ (p. 4–5).

*Intuition note.* Disconnected subwebs never vote for each other, so nothing fixes the relative size of their scores. You can scale each subweb's scores freely.

*2.2.2 Dangling nodes (p. 5).* A dangling node gives a zero column, so $A$ is *column-substochastic* (column sums $\le1$). Its eigenvalues have magnitude $\le1$, but 1 need not be an eigenvalue. The paper says such a matrix must have a positive eigenvalue $\lambda\le1$ with a non-negative (Perron) eigenvector that can rank the pages (Exercise 4). It does not pursue this (p. 5).

Exercises 1–6 are on p. 5 (see below).

### 3. A remedy for $\dim V_1(A)>1$ (p. 5–8)
The real web, as an undirected graph, has many disjoint components. The analysis is "basically a special case of the Perron-Frobenius theorem", and the authors prove only what they need (p. 5–6).

**3.1 Modification (p. 6).**
- Let $S$ be the $n\times n$ matrix with all entries $1/n$. It is column-stochastic and $V_1(S)$ is one-dimensional. Define
$$M=(1-m)A+mS,\qquad 0\le m\le1.\tag{3.1}$$
- $M$ is column-stochastic for every $m\in[0,1]$. Google reportedly used $m=0.15$. If $m=0$ then $M=A$. If $m=1$ then $M=S$, and all pages get score $1/n$ (p. 6).
- The authors show below that $V_1(M)$ is one-dimensional for $m\in(0,1]$ (p. 6).
- For dangling nodes: $M$ gives a page with no backlinks the score $m/n$ (Exercise 9). With dangling nodes $M$ stays substochastic for $m<1$, so the problem is not resolved. From here on, only webs without dangling nodes are considered (p. 6).
- Equivalent form, with $s$ the column vector of all $1/n$ (note $Sx=s$ when $\sum x_i=1$):
$$x=Mx=(1-m)Ax+ms.\tag{3.2}$$
- **Example 1** (Fig. 2.1, $m=0.15$). Entries: $0.15/4=0.0375$ where $A_{ij}=0$; e.g. $0.8875=0.85+0.0375$. Scores: $x_1\approx0.368$, $x_2\approx0.142$, $x_3\approx0.288$, $x_4\approx0.202$. Same ranking as before, slightly different scores (p. 6).
- **Example 2** (Fig. 2.2, $m=0.15$). $M$ is $5\times5$ with entries $0.03$ (from $0.15/5$), $0.88$ and $0.455$ (eq. 3.3). $V_1(M)$ is one-dimensional, with $x=(0.2,\,0.2,\,0.285,\,0.285,\,0.03)$. Pages in different subwebs can now be compared (p. 6).
- **Definition 3.1.** A matrix $M$ is *positive* if $M_{ij}>0$ for all $i,j$. Every $M$ from (3.1) is positive (for $m>0$). This is the key property behind $\dim V_1(M)=1$ (p. 6).

**3.2 Analysis of $M$ (p. 7).** $V_1(M)$ is non-empty by Prop. 1.

- **Proposition 2.** If $M$ is positive and column-stochastic, every eigenvector in $V_1(M)$ has all positive or all negative components.
  *Proof* (contradiction). Suppose $x\in V_1(M)$ has mixed signs. Then $x_i=\sum_jM_{ij}x_j$ has mixed-sign summands, and the triangle inequality is strict:
$$|x_i|=\Big|\sum_{j=1}^nM_{ij}x_j\Big|<\sum_{j=1}^nM_{ij}|x_j|.\tag{3.4}$$
  Sum over $i$, swap the sums, and use $\sum_iM_{ij}=1$:
$$\sum_i|x_i|<\sum_{i}\sum_jM_{ij}|x_j|=\sum_j\Big(\sum_iM_{ij}\Big)|x_j|=\sum_j|x_j|,$$
  a contradiction. If all $x_i\ge0$ (not all zero), then $x_i=\sum_jM_{ij}x_j>0$ because $M_{ij}>0$. The all-$\le0$ case is symmetric (p. 7).
- **Proposition 3.** If $v,w\in\mathbb R^m$ ($m\ge2$) are linearly independent, then for some $s,t$ not both zero, $x=sv+tw$ has both positive and negative components.
  *Proof.* Neither vector is zero. Let $d=\sum_iv_i$. If $d=0$, $v$ has mixed signs; take $s=1,t=0$. If $d\ne0$, take $s=-\sum_iw_i/d$, $t=1$. Then $x\ne0$ (independence) but $\sum_ix_i=0$, so $x$ has mixed signs (p. 7).
- **Lemma 3.2.** If $M$ is positive and column-stochastic, $\dim V_1(M)=1$.
  *Proof.* Suppose $v,w\in V_1(M)$ are independent. Every nonzero $sv+tw$ is in $V_1(M)$, so by Prop. 2 has constant sign. This contradicts Prop. 3 (p. 7).
- Consequence: there is a unique eigenvector $x\in V_1(M)$ with positive components and $\sum x_i=1$ (p. 7).

*Intuition note.* Two independent eigenvectors could be combined to cancel their total sum. The result would have mixed signs, but positivity of $M$ forbids mixed-sign eigenvectors. So there can be only one direction.

Exercises 7–13 are on p. 7–8.

### 4. Computing the importance score eigenvector (p. 8–10)
- The web has at least eight billion pages. The proposed approach is the *power method*: $x_k=Mx_{k-1}$, so $x_k=M^kx_0$. In general one rescales, $x_k=Mx_{k-1}/\|Mx_{k-1}\|$. The method generally needs a one-dimensional eigenspace for the dominant eigenvalue, which holds here (p. 8).
- Normally one would need all other eigenvalues to satisfy $|\lambda|<1$. Prop. 4 avoids this (p. 8).
- **Definition 4.1.** $\|v\|_1=\sum_i|v_i|$.
- **Proposition 4.** Let $M$ be positive, column-stochastic, $n\times n$, and $V=\{v\in\mathbb R^n:\sum_jv_j=0\}$. Then $Mv\in V$ for $v\in V$, and
$$\|Mv\|_1\le c\|v\|_1,\quad c=\max_{1\le j\le n}\Big|1-2\min_{1\le i\le n}M_{ij}\Big|<1.$$
  *Proof.* With $w=Mv$: $\sum_iw_i=\sum_jv_j\sum_iM_{ij}=\sum_jv_j=0$, so $w\in V$ (p. 8). For the bound, let $e_i=\mathrm{sgn}(w_i)$. They are of mixed sign because $\sum w_i=0$ (if $w\equiv0$ the bound is clear). Then
$$\|w\|_1=\sum_ie_iw_i=\sum_jv_j\Big(\sum_ie_iM_{ij}\Big)=\sum_ja_jv_j,\quad a_j=\sum_ie_iM_{ij}.\tag{4.1}$$
  Since the $e_i$ have mixed sign, $\sum_iM_{ij}=1$ and $0<M_{ij}<1$: $-1<-1+2\min_iM_{ij}\le a_j\le1-2\min_iM_{ij}<1$. So $|a_j|\le|1-2\min_iM_{ij}|\le c<1$. Hence $\|w\|_1\le\sum|a_j||v_j|\le c\|v\|_1$ (p. 8–9).
- **Proposition 5.** A positive column-stochastic $M$ has a unique $q$ with positive components, $Mq=q$, $\|q\|_1=1$. Moreover $q=\lim_{k\to\infty}M^kx_0$ for any positive $x_0$ with $\|x_0\|_1=1$.
  *Proof.* Existence and uniqueness follow from Prop. 1, Lemma 3.2 and Prop. 2. Write $x_0=q+v$ with $v\in V$ (both vectors sum to 1). Then
$$M^kx_0-q=M^kv.\tag{4.2}$$
  By induction and Prop. 4, $\|M^kv\|_1\le c^k\|v\|_1\to0$ (p. 9).

*Intuition note.* On vectors whose entries sum to zero, one multiplication by $M$ strictly shrinks total size. Any positive start whose entries sum to 1 differs from $q$ by such a vector, so the difference dies out geometrically while the $q$ part never changes.

- **Numerical example** (matrix (3.3), $x_0=[0.24,0.31,0.08,0.18,0.19]^T$, $q=[0.2,0.2,0.285,0.285,0.03]^T$, $c=0.94$) (p. 9):

| $k$ | $\|M^kx_0-q\|_1$ | ratio to previous |
|---|---|---|
| 0 | 0.62 | |
| 1 | 0.255 | 0.411 |
| 5 | 0.133 | 0.85 |
| 10 | 0.0591 | 0.85 |
| 50 | $8.87\times10^{-5}$ | 0.85 |

- The bound $c^k$ is pessimistic. 0.85 equals $1-m$ and "turns out" to be the second-largest eigenvalue of $M$. In general the error shrinks asymptotically by about $|\lambda_2|$ per step. For $M=(1-m)A+mS$ with $A$ column-stochastic, $|\lambda_2|\le1-m$ (cited from [1], Thm 5.10, not proved here). Since all entries of $M$ are $\ge m/n$, $c\le1-2m/n$ (p. 9–10).
- Cost: $M$ has no zero entries, so $Mv$ typically costs $O(n^2)$ operations. By (3.2), for positive $x$ with $\|x\|_1=1$, $Mx=(1-m)Ax+ms$. This is far cheaper because $A$ is mostly zeros (p. 10).
- **Theorem 4.2.** For a web with no dangling nodes, $M$ from (3.1) is positive and column-stochastic. So there is a unique positive $q$ with $Mq=q$, $\sum q_i=1$. It is the limit of $x_k=(1-m)Ax_{k-1}+ms$ for any positive $x_0$ with $\|x_0\|_1=1$ (p. 10).
- **Random surfer.** At a page with $r$ outgoing links, the surfer follows each link with probability $\frac{1-m}{r}$, or jumps to each of the $n$ pages with probability $\frac mn$. (Total: $r\cdot\frac{1-m}{r}+n\cdot\frac mn=1$.) The authors state that $x_j$ is the long-run fraction of time spent on page $j$ (p. 10).

Exercises 14–17 are on p. 10.

## Toy example (ours, not from the text)
Web of 4 pages: $1\leftrightarrow2$ and $3\leftrightarrow4$ (two disconnected subwebs). Each page has one outlink, so $A$ swaps entries $(x_1,x_2)$ and $(x_3,x_4)$: $Ax=(x_2,x_1,x_4,x_3)$. Both $(\tfrac12,\tfrac12,0,0)$ and $(0,0,\tfrac12,\tfrac12)$ satisfy $Ax=x$, so $\dim V_1(A)\ge2$.

Take $m=0.2$, so $S$ has entries $0.25$ and $M=0.8A+0.2S$ has entries $0.8+0.05=0.85$ where $A_{ij}=1$ and $0.05$ elsewhere. All entries are positive. $M(\tfrac14,\tfrac14,\tfrac14,\tfrac14)^T$ has each entry $\tfrac14(0.85+3\cdot0.05)=\tfrac14$, so $q=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$ (symmetric web, equal scores).

Power iteration from $x_0=(0.4,0.1,0.3,0.2)$ (sum 1), using $(1-m)Ax+ms$:
- $Ax_0=(0.1,0.4,0.2,0.3)$, $0.8Ax_0=(0.08,0.32,0.16,0.24)$, add $0.2\cdot0.25=0.05$: $x_1=(0.13,0.37,0.21,0.29)$, sum 1.
- $\|x_0-q\|_1=0.15+0.15+0.05+0.05=0.40$. $\|x_1-q\|_1=0.12+0.12+0.04+0.04=0.32$. Ratio $0.8=1-m$.
- Here $c=|1-2(0.05)|=0.9$, and $0.8\le0.9$, consistent with Prop. 4.
- With $A$ alone, $A^2x_0=x_0$, so the iteration just swaps back and forth and never settles.

## Concepts
- [[pagerank]] (new) — importance score vector $q$ from the link structure; the positive, sum-one fixed point of $M$ (p. 2, 10)
- [[eigenvector-eigenvalue]] — here, scores solve $Ax=x$, an eigenvector for $\lambda=1$ (p. 3)
- [[markov-stochastic-matrix]] — column-stochastic: entries $\ge0$, columns sum to 1; always has eigenvalue 1 (p. 3)
- [[substochastic-matrix]] (new) — column sums $\le1$; arises with dangling nodes; 1 need not be an eigenvalue (p. 5)
- [[dangling-node]] (new) — a page with no outgoing links; gives a zero column of $A$ (p. 3, 5)
- [[strongly-connected-web]] (new) — any page reachable from any other; guarantees $\dim V_1(A)=1$ (p. 4, Ex. 10)
- [[eigenspace-V1]] (new) — $V_1(A)$, the eigenspace for eigenvalue 1; its dimension decides uniqueness of scores (p. 3)
- [[dimension]] — $\dim V_1\ge r$ for $r$ disconnected subwebs (p. 4)
- [[linear-independence]] — used to build the $w^i$ and in Props. 3, Lemma 3.2 (p. 4, 7)
- [[block-diagonal-link-matrix]] (new) — the form of $A$ for disconnected subwebs (p. 4)
- [[google-matrix-mixing]] (new) — $M=(1-m)A+mS$; weighted average of link matrix and uniform matrix, $m=0.15$ reportedly (p. 6)
- [[positive-matrix]] (new) — all entries $>0$; with column-stochastic, gives unique positive eigenvector (p. 6)
- [[norm]] — the 1-norm $\|v\|_1=\sum|v_i|$ (p. 8)
- [[power-iteration]] — $x_k=Mx_{k-1}$ (rescaled) converges to the dominant eigenvector; here $\|M^kv\|_1\le c^k\|v\|_1$ on $V$ (p. 8–9)
- [[perron-frobenius-theorem]] — the authors' analysis is a special case; Perron eigenvector for substochastic $A$ (p. 5, 6)
- [[random-surfer]] (new) — probabilistic reading of $q$ as long-run visiting frequency (p. 10)

## Canonical instances
- [[four-page-web-fig-2-1]] — scores $(12,4,9,6)/31$ differ from backlink counts $(2,1,3,2)$ (p. 2–3)
- [[five-page-two-subweb-fig-2-2]] — $\dim V_1(A)=2$; with $M$ unique scores $(0.2,0.2,0.285,0.285,0.03)$ (p. 4, 6)
- [[power-method-convergence-table]] — error ratios approach $0.85=1-m$, versus bound $c=0.94$ (p. 9)

## Bridges (candidates)
- [same-math] Column-stochastic $A$, eigenvalue 1 ↔ Markov chains: stationary distribution — the paper mentions Markov chains and gives the surfer reading (p. 1, 3, 10)
- [same-math] Lemma 3.2 / Props. 2–5 ↔ Perron–Frobenius theorem for positive matrices — authors call their analysis a special case (p. 6)
- [structural-analogy] PageRank scores ↔ network science: eigenvector centrality — a node's importance depends on the importance of its neighbours
- [structural-analogy] Block-diagonal $A$ and non-unique scores ↔ graph theory: connected components giving multiple eigenvectors for one eigenvalue
- [metaphor] Mixing in $mS$ ↔ regularisation or smoothing — a small uniform term makes the problem well-posed

## Questions this raises
- How should $m$ be chosen, and how does it trade off faithfulness to the links against speed of convergence (Ex. 17)?
- How should dangling nodes be handled properly? The paper only says a Perron eigenvector can be used.
- Is the bound $|\lambda_2|\le1-m$ attained, and why does the ratio in the table settle at exactly $1-m$?
- Does a random-surfer proof that $x_j$ is a long-run visiting fraction follow from $Mq=q$? The paper only states it.

## Exercises worth doing
- Ex. 6 (p. 5) — page re-indexing leaves scores unchanged ($\tilde A=PAP$, $y=Px$) — medium
- Ex. 9 (p. 7) — a page with no backlinks gets score $m/n$ under (3.2) — easy
- Ex. 10 (p. 7–8) — strongly connected web implies $\dim V_1(A)=1$, via powers of $A$ and walk counting — hard
- Ex. 14 (p. 10) — compute error ratios, $c$ and $|\lambda_2|$ numerically for a 5-page web — medium
- Ex. 15 (p. 10) — role of the second eigenvalue in the convergence ratio, using diagonalisation — hard
- Ex. 16 (p. 10) — $M$ can fail to be diagonalizable for a specific $A$ — medium

## Reading notes
- Printed page numbers 1–11 equal pdf numbers (offset 0). The unit is the whole paper; pp. 10–11 hold exercises 14–17 and references. The metadata gives the journal pages 569–581, but the pages here are numbered 1–11.
- Exercise 1 refers to "Figure 1", and Exercise 3 and the text on p. 4 refer to "Figure 2"; these seem to mean Figs. 2.1 and 2.2.
- Sect. 3.1 states $V_1(M)$ is one-dimensional for $m\in(0,1]$, but later says the punchline holds "for $0<m<1$" (p. 7). Lemma 3.2 itself only assumes $M$ positive and column-stochastic, which also covers $m=1$.
- Sect. 3.1 equates a page "with no backlinks (a dangling node)". Elsewhere (p. 3, 5) a dangling node is a page with no outgoing links. These are different things.
- The asymptotic formula on pp. 9–10 is printed as $\|Mx_k-q\|_1\approx|\lambda_2|\|x-q\|_1$. It mixes $x_k$ and $x$; the intended meaning is presumably one-step shrinkage by about $|\lambda_2|$.
- The authors state, without proof here, that $V_1(A)$ is one-dimensional for strongly connected webs (Ex. 10), that $|\lambda_2|\le1-m$ (cited), and the random-surfer interpretation.
- In the printed proof of Prop. 3 the text layer is garbled in places; the page image shows $s=-\sum_iw_i/d$, $t=1$.
