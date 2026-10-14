---
id: spielman-2025-sagt/ch06-comparing
work: spielman-2025-sagt
unit: "Chapter 6 — Comparing Graphs"
pages: 53–60
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
# Comparing Graphs

## L0 — One line
If one graph's Laplacian dominates a multiple of another's in the Loewner order, its eigenvalues dominate that multiple of the other's eigenvalues, so comparing a graph with the complete graph gives lower bounds on $\lambda_2$.

## L1 — The gist (≤ 120 words)
Eigenvalues of an abstractly defined graph can rarely be determined exactly. Test vectors usually make upper bounds on $\lambda_2$ easy, but lower bounds are harder. This chapter uses the Loewner order, extended from matrices to graphs through their Laplacians. If $c>0$ and $G \succcurlyeq c\cdot H$, then $\lambda_k(G)\ge c\lambda_k(H)$ for every $k$. To lower-bound $\lambda_2$ here, the chapter shows that a multiple of the graph dominates the complete graph $K_n$, whose $\lambda_2$ is $n$. The tool is a path inequality, proved with Cauchy–Schwarz and extended to weighted paths. It gives $\lambda_2(P_n)\ge 6/((n+1)(n-1))$ and $\lambda_2(T_n)\ge 1/2n$ for the complete binary tree $T_n$.

**Prerequisites:** Laplacian quadratic form; positive semidefinite matrices; Courant–Fischer theorem; Cauchy–Schwarz inequality; $\lambda_2(K_n)=n$.

## L2 — Key ideas
- Upper bounds on $\lambda_2$ usually need only a well-chosen test vector (with Courant–Fischer). Lower bounds are harder, which motivates graph comparison (p. 53).
- $A\succcurlyeq B$ means $v^TAv\ge v^TBv$ for all $v$. For graphs, $G\succcurlyeq H$ means $L_G\succcurlyeq L_H$ (pp. 53–54).
- Dropping edges or lowering weights lowers the Laplacian in this order (p. 54).
- If $c>0$ and $G\succcurlyeq c\cdot H$, then $\lambda_k(G)\ge c\lambda_k(H)$ for all $k$ (Lemma 6.2.1, pp. 54–55).
- $H$ is a $c$-approximation of $G$ if $cH\succcurlyeq G\succcurlyeq H/c$. Good approximations exist, for example expanders approximating complete graphs (p. 55).
- Basic path inequality: $(n-1)P_n\succcurlyeq G_{1,n}$, by Cauchy–Schwarz (p. 55–56).
- Sum this over all pairs, then apply Lemma 6.2.1: $\lambda_2(P_n)\ge 6/((n+1)(n-1))$ (p. 57).
- Weighted version: $G_{1,n}\preccurlyeq(\sum 1/w_a)(\sum w_aG_{a,a+1})$ (p. 59).
- Weighting edges by depth improves the binary-tree bound from $1/((n-1)\log_2 n)$ to $1/2n$ (p. 60).

## L3 — Walkthrough

### 6.1 Overview (p. 53)
Courant–Fischer plus a test vector usually gives lower bounds on the largest eigenvalues or upper bounds on the smallest. Bounds in the other direction are harder. The technique is called "Poincaré inequalities" or "graphic inequalities".

### 6.2 The Loewner order (pp. 53–55)
For symmetric $A$, $A\succcurlyeq 0$ means $A$ is positive semidefinite (all eigenvalues nonnegative), equivalently $v^TAv\ge0$ for all $v$. $A\succcurlyeq B$ means $A-B\succcurlyeq0$, equivalently $v^TAv\ge v^TBv$ for all $v$ (pp. 53–54).

It is a *partial* order: some pairs are incomparable. Where defined it is transitive, and $A\succcurlyeq B\Rightarrow A+C\succcurlyeq B+C$ (p. 54).

For graphs, $G\succcurlyeq H$ means $L_G\succcurlyeq L_H$. If $H=(V,F)$ is a subgraph of $G=(V,E)$ on the same vertices, then $L_G\succcurlyeq L_H$. This follows from
$$x^TL_Gx=\sum_{(u,v)\in E}w_{u,v}(x(u)-x(v))^2,$$
since dropping edges, or lowering weights, can only decrease the sum (p. 54). Here $c\cdot H$ is $H$ with every weight multiplied by $c$, so $L_{c\cdot H}=cL_H$ (p. 54).

**Lemma 6.2.1.** If $c>0$ and $G\succcurlyeq c\cdot H$, then $\lambda_k(G)\ge c\lambda_k(H)$ for all $k$.
*Proof.* By Courant–Fischer (p. 55):
$$\lambda_k(G)=\min_{\substack{S\subseteq\mathbb R^n\\ \dim S=k}}\max_{x\in S}\frac{x^TL_Gx}{x^Tx}\ \ge\ \min_{\substack{S\subseteq\mathbb R^n\\ \dim S=k}}\max_{x\in S}c\,\frac{x^TL_Hx}{x^Tx}=c\lambda_k(H).$$

**Corollary 6.2.2.** Removing an edge, or lowering an edge weight, does not increase any $\lambda_k$ (p. 55).

*Intuition note:* If a graph's energy $x^TLx$ is at least $c$ times another's for every $x$, the same holds for the min–max values that define the eigenvalues. Adding edges (or raising weights) cannot lower any eigenvalue (Corollary 6.2.2).

### 6.3 Approximations of graphs (p. 55)
$H$ is a **$c$-approximation** of $G$ if $cH\succcurlyeq G\succcurlyeq H/c$. It is good when $c$ is slightly above 1. The text says random regular and Erdős–Rényi graphs approximate complete graphs (Chapter 8). For every $\epsilon>0$ there is a $d$ such that for all $n$ there is a $d$-regular $G_n$ that is a $(1+\epsilon)$-approximation of $K_n$. Chapters 32–33 will show that every graph has a good sparse approximation (p. 55).

### 6.4 The path inequality (pp. 55–57)
**Lemma 6.4.1 (Daitch).** $(n-1)\cdot P_n\succcurlyeq G_{1,n}$, where $G_{1,n}$ has only the edge $(1,n)$ (all unweighted).
*Proof.* One must show, for every $x\in\mathbb R^n$,
$$(n-1)\sum_{a=1}^{n-1}(x(a+1)-x(a))^2\ge(x(n)-x(1))^2.$$
Set $\Delta(a)=x(a+1)-x(a)$, so $\sum_a\Delta(a)=x(n)-x(1)$. By Cauchy–Schwarz with the all-ones vector (p. 56):
$$\Big(\sum_a\Delta(a)\Big)^2=(\mathbf 1^T_{n-1}\Delta)^2\le(\|\mathbf 1_{n-1}\|\|\Delta\|)^2=(n-1)\sum_i\Delta(i)^2.$$

*Intuition note:* A single jump from $x(1)$ to $x(n)$ is cheapest, in squared differences, when it is spread evenly over the $n-1$ steps. The factor $n-1$ is the price of spreading.

**6.4.1 Lower bound on $\lambda_2(P_n)$ (pp. 56–57).** Theorem 5.6.1 gives $\lambda_2(P_n)=2(1-\cos(\pi/n))\approx\pi^2/n^2$ for large $n$ (p. 56). We use $\lambda_2(K_n)=n$ (Lemma 5.1.1) and $L_{K_n}=\sum_{a<b}L_{G_{a,b}}$. For each $a<b$, $P_{a,b}$ is the subpath on indices $a..b$ (length $b-a$), and
$$G_{a,b}\preccurlyeq(b-a)P_{a,b}\preccurlyeq(b-a)P_n.\tag{6.2}$$
Summing over pairs: $K_n\preccurlyeq\sum_{a<b}(b-a)P_n$. Moreover (p. 57)
$$\sum_{1\le a<b\le n}(b-a)=\sum_{c=1}^{n-1}c(n-c)=n(n+1)(n-1)/6.$$
So $L_{K_n}\preccurlyeq\frac{n(n+1)(n-1)}6L_{P_n}$, i.e. $L_{P_n}\succcurlyeq\frac{6}{n(n+1)(n-1)}L_{K_n}$. Lemma 6.2.1 with $\lambda_2(K_n)=n$ gives
$$\lambda_2(P_n)\ge\frac6{(n+1)(n-1)}.$$

### 6.5 The complete binary tree (pp. 57–58)
$T_n$ has $n=2^{d+1}-1$ nodes (depth $d+1$), with edges $(i,2i)$ and $(i,2i+1)$ for $i<n$ (p. 57).

*Upper bound.* Test vector: $x(1)=0$, $x(2)=1$, $x(3)=-1$. Every node reachable from node 2 without passing node 1 gets $1$; all the other nodes (apart from node 1, which keeps $0$) get $-1$. Then $\mathbf 1^Tx=0$, and Courant–Fischer gives
$$\lambda_2\le\frac{x^TLx}{x^Tx}=\frac{(x(1)-x(2))^2+(x(1)-x(3))^2}{n-1}=\frac2{n-1}.$$

*Lower bound.* The tree path $T^{a,b}$ has length at most $2d\le2\log_2n$. So
$$K_n=\sum_{a<b}G_{a,b}\preccurlyeq\sum_{a<b}(2d)T^{a,b}\preccurlyeq\sum_{a<b}(2\log_2n)T_n=\binom n2(2\log_2n)T_n.$$
Hence $\binom n2(2\log_2n)\lambda_2(T_n)\ge\lambda_2(K_n)=n$, so $\lambda_2(T_n)\ge\frac1{(n-1)\log_2n}$ (p. 58).

The author's Julia experiment ($d=12$) prints $0.000245342$ for the first entry of `fiedler(...)` (presumably $\lambda_2$) against $1/n\approx0.000244200$. So the truth seems close to $1/n$ (p. 58).

### 6.6 The weighted path (p. 59)
**Lemma 6.6.1.** For positive $w_1,\dots,w_{n-1}$:
$$G_{1,n}\preccurlyeq\Big(\sum_{a=1}^{n-1}\frac1{w_a}\Big)\sum_{a=1}^{n-1}w_aG_{a,a+1}.$$
*Proof.* With $\Delta$ as before, set $\gamma(a)=\Delta(a)\sqrt{w_a}$ and $w^{-1/2}(a)=1/\sqrt{w_a}$. Then $\sum_a\Delta(a)=\gamma^Tw^{-1/2}$, $\|w^{-1/2}\|^2=\sum_a1/w_a$, and $\|\gamma\|^2=\sum_a\Delta(a)^2w_a$. By Cauchy–Schwarz,
$$x^TL_{G_{1,n}}x=\Big(\sum_a\Delta(a)\Big)^2=(\gamma^Tw^{-1/2})^2\le\|\gamma\|^2\|w^{-1/2}\|^2=\Big(\sum_a\tfrac1{w_a}\Big)x^T\Big(\sum_aw_aL_{G_{a,a+1}}\Big)x.$$

*Intuition note:* Cheaper (lower-weight) steps may carry more of the jump. Weighting trades off how much each step is charged. All weights equal to 1 recovers Lemma 6.4.1.

### 6.7 A better lower bound on $\lambda_2(T_n)$ (p. 60)
**Theorem 6.7.1.** $\lambda_2(T_n)\ge1/2n$.
*Proof.* Let $n=2^{d+1}-1$. Edge depth is the larger of its endpoints' depths, so it ranges over $1..d$. Let $T^{a,b}$ be the tree path from $a$ to $b$, with weight $2^i$ on each depth-$i$ edge. Such a path has at most two edges at each depth, so Lemma 6.6.1 gives
$$G_{a,b}\preccurlyeq2(2^{-1}+2^{-2}+\dots+2^{-(d-1)})\,T^{a,b}\preccurlyeq2\,T^{a,b}.$$
So $K_n\preccurlyeq2\sum_{a<b}T^{a,b}$.

A depth-$i$ edge has $2^{d+1-i}-1$ vertices beneath it. It lies on
$$(2^{d+1-i}-1)(n-2^{d+1-i}+1)\le(2^{d+1-i}-1)\,n$$
paths. Each appearance has weight $2^i$, so its total weight is at most $(2^{d+1}-2^i)n\le n^2$. Hence $\sum_{a<b}T^{a,b}\preccurlyeq n^2T_n$ and $K_n\preccurlyeq2n^2T_n$. With $\lambda_2(K_n)=n$ and Lemma 6.2.1, $\lambda_2(T_n)\ge n/2n^2=1/2n$.

*Intuition note:* A path has at most two edges at each depth, so with weights $2^i$ its factor $\sum 1/w_a$ stays below a constant instead of growing with the path length. Shallow edges lie on many paths but have small weight $2^i$; deep edges lie on few paths but have large weight. At every depth the total weight is at most $n^2$. This removes the $\log n$ factor.

## Toy example (ours)
Take $n=3$ and $x=(0,1,3)$.
- $x^TL_{P_3}x=(1-0)^2+(3-1)^2=5$, so $(n-1)\cdot5=10$.
- $x^TL_{G_{1,3}}x=(3-0)^2=9\le10$, consistent with Lemma 6.4.1.
- $\sum_{a<b}(b-a)=1+1+2=4=3\cdot4\cdot2/6$. So $K_3\preccurlyeq4P_3$.
- Lemma 6.2.1 gives $\lambda_2(P_3)\ge3/4$. The formula gives $6/(4\cdot2)=0.75$.
- True value: $2(1-\cos(\pi/3))=1\ge0.75$.

## Concepts
- [[loewner-order]] (new) — $A\succcurlyeq B$ iff $A-B$ is PSD; partial order on symmetric matrices, extended to graphs via Laplacians (p. 53–54)
- [[positive-semidefinite-matrix]] — symmetric, with $v^TAv\ge0$ for all $v$, equivalently nonnegative eigenvalues (p. 53)
- [[graph-laplacian]] — $x^TL_Gx=\sum w_{u,v}(x(u)-x(v))^2$ (p. 54)
- [[rayleigh-quotient]] — $x^TLx/x^Tx$, used via Courant–Fischer min–max (p. 55)
- [[fiedler-vector-algebraic-connectivity]] — $\lambda_2$ is the quantity being bounded (p. 53)
- [[graph-approximation]] (new) — $H$ is a $c$-approximation of $G$ if $cH\succcurlyeq G\succcurlyeq H/c$ (p. 55)
- [[cauchy-schwarz-inequality]] (new) — inner product at most product of norms; engine of the path lemmas (p. 56)

## Canonical instances
- [[path-graph-lambda2-bound]] (new) — $\lambda_2(P_n)\ge 6/((n+1)(n-1))$ (p. 57)
- [[complete-binary-tree-lambda2]] (new) — $2/(n-1)$ upper bound; $1/2n$ lower bound (pp. 57, 60)
- [[complete-graph-kn]] (new) — $\lambda_2(K_n)=n$, the reference graph (p. 56)

## Bridges (candidates)
- [structural-analogy] Dominating a multiple of $K_n$ ↔ condition numbers: $c$-approximation bounds the ratio of quadratic forms, as relative bounds on a matrix pair.
- [same-math] Lemma 6.2.1 ↔ Courant–Fischer / Rayleigh quotient: $\succcurlyeq$ on matrices passes to ordered eigenvalues.

## Questions this raises
- How tight is $6/((n+1)(n-1))$ against $\pi^2/n^2$ for large $n$?
- Which graphs $H$ give the best reference for comparison, apart from $K_n$?
- Can one find the optimal edge weights $w_a$ automatically in Lemma 6.6.1?

## Reading notes
- Printed = pdf − 24.
- The text layer shows $\succcurlyeq$ and $\preccurlyeq$ as garbled "<" and "4". I used the page images.
- On p. 60 the sum is printed as $2^{-1}+\dots+2^{-(d-1)}$. Depths run $1..d$, so I would expect the last term $2^{-d}$. The conclusion (at most $2$) holds either way. This is my observation, not the author's.
- The Julia snippet (p. 58) sets $n=2^d-1$ with $d=12$, whereas the text uses $n=2^{d+1}-1$.
- The draft contains typos, such as "It is rare than" (p. 53).
