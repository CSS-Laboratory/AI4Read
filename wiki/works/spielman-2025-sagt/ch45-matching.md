---
id: spielman-2025-sagt/ch45-matching
work: spielman-2025-sagt
unit: Chapter 45 — The Matching Polynomial (§§45.1–45.4; the pages end inside the proof of Theorem 45.4.2)
pages: 357–361
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# The Matching Polynomial

## L0 — One line
The matching polynomial of a graph counts matchings in its coefficients, equals the adjacency characteristic polynomial for trees, and (Godsil's route) is linked to a tree through the path tree.

## L1 — The gist (≤ 120 words)
The chapter asks why the matching polynomial $\mu_x[G]$, whose coefficients count matchings, has only real roots. The overview says Heilmann and Lieb proved this. Godsil's approach is to show that $\mu_x[G]$ divides $\mu_x[T_a(G)]$, where $T_a(G)$ is the path tree of $G$. For a tree, $\mu_x$ is the characteristic polynomial of the adjacency matrix, whose roots are real. The pages give the recurrence, the tree theorem, the path tree and a ratio identity (Theorem 45.4.1). The proof of divisibility (Theorem 45.4.2) begins but is cut off. The overview says the next lecture will use the $2\sqrt{d-1}$ root bound to derive Ramanujan graphs.

**Prerequisites:** determinant as a signed sum over permutations; characteristic polynomial; adjacency matrix; induction; polynomial divisibility.

## L2 — Key ideas (5–10 bullets)
- $\mu_x[G]=\sum_k x^{n-2k}(-1)^k m_k(G)$ encodes matching counts as coefficients (p. 358).
- It is multiplicative over disjoint unions (p. 358) and satisfies the vertex-deletion recurrence $\mu_x[G]=x\mu_x[G-a]-\sum_{b\sim a}\mu_x[G-a-b]$ (p. 359).
- For a tree, $\mu_x[G]=\chi_x(A_G)$, because only involution terms survive in the determinant expansion (p. 359).
- Godsil's plan: $\mu_x[G]$ divides $\mu_x[T_a(G)]$, and a tree's polynomial is real rooted, so $\mu_x[G]$ is real rooted (p. 359).
- Path tree $T_a(G)$: vertices are simple paths from $a$; adjacent when one extends the other by one vertex (p. 359).
- Theorem 45.4.1 is a ratio identity between $G$ and $T_a(G)$, proved by induction using the recurrence (pp. 360–361).
- Theorem 45.4.2 (divisibility) is proved by induction; the given pages stop mid-proof (p. 361).

## L3 — Walkthrough

### 45.1 Overview (p. 357)
- **Author's statement:** Heilmann and Lieb defined the matching polynomial and proved it is real rooted. They also proved that, for maximum degree $d$, all roots are at most $2\sqrt{d-1}$. The next lecture uses this for Ramanujan graphs.
- The proofs here follow Godsil. The author hopes Godsil's approach can connect this bound to the one from the previous lecture.
- Here $2\sqrt{d-1}$ appears as an upper bound on the spectral radius of a $d$-ary tree. Infinite $d$-ary trees appear as the graphs of free groups in free probability. The author feels there must be a formal relation between these that he is missing.

### 45.2 The matching polynomial (pp. 357–358)
- A matching is a subgraph where every vertex has degree 1. It has size $k$ if it has $k$ edges. $m_k(G)$ counts matchings of size $k$, with $|V|=n$.
- $m_1$ = number of edges. $m_{n/2}$ = number of perfect matchings. $m_0=1$ (empty matching).
- The author says counting perfect matchings is #P-hard, "much harder" than NP-hard problems (p. 357).
$$\mu_x[G]\overset{\text{def}}{=}\sum_{k=0}^{n/2}x^{n-2k}(-1)^k m_k(G).$$
- Since $m_0=1$, this is a polynomial of degree $n$ (p. 358).

### 45.3 Properties (pp. 358–359)
**Lemma 45.3.1.** For graphs $G,H$ on different vertex sets, $\mu_x[G\cup H]=\mu_x[G]\mu_x[H]$.
- Proof idea: each matching of $G\cup H$ is a matching of $G$ plus one of $H$. So $m_k(G\cup H)=\sum_{j=0}^k m_j(G)m_{k-j}(H)$, and the lemma follows (p. 358). (The source prints $\mu_j,\mu_{k-j}$ here; see Reading notes.)

**Recurrence.** Fix a vertex $a$. Split matchings into those avoiding $a$ and those using an edge $(a,b)$ (p. 358).
- Avoiding $a$: $m_k(G-a)$.
- Using $(a,b)$: the rest is a size-$(k-1)$ matching of $G-a-b$.
$$m_k(G)=m_k(G-a)+\sum_{b\sim a}m_{k-1}(G-a-b).$$
- Rewriting each term with the signs and powers of $x$ gives:

**Lemma 45.3.2.**
$$\mu_x[G]=x\,\mu_x[G-a]-\sum_{b\sim a}\mu_x[G-a-b].$$
*Intuition note:* either $a$ is unmatched (factor $x$ times the rest) or matched to a neighbour $b$ (sign flip, two vertices removed). The next theorem's induction (Theorem 45.4.1) uses it.

**Theorem 45.3.3.** If $G$ is a tree, $\mu_x[G]=\chi_x(A_G)$ (p. 359).
- Expand $\chi_x(A_G)=\det(xI-A_G)$ over permutations:
$$\sum_{\pi\in S_n}(-1)^{\mathrm{sgn}(\pi)}x^{|\{a:\pi(a)=a\}|}\prod_{a:\pi(a)\ne a}(-A_G(a,\pi(a))).$$
- If some $a$ has $\pi(\pi(a))\ne a$, then $\pi$ has a cycle $a_1,\dots,a_k$ with $k>2$. For a nonzero term, all $A_G(a_i,a_{i+1})=1$ and $A_G(a_k,a_1)=1$, which is a cycle of length $k$ in $G$. A tree has none.
- So only involutions (permutations that are their own inverse) contribute. They have fixed points and 2-cycles. Each nonzero 2-cycle is an edge. So permutations with $k$ 2-cycles correspond to matchings with $k$ edges. Their sign is $(-1)^k$, so the coefficient of $x^{n-2k}$ is $(-1)^km_k(G)$.

*Intuition note:* in a tree, the only way to get a nonzero determinant term from a non-fixed vertex is to swap two adjacent vertices. That is exactly choosing an edge of a matching.

### 45.4 The path tree (pp. 359–361)
- **Godsil's strategy:** show $\mu_x[G]$ divides the matching polynomial of a tree. That tree's polynomial equals the characteristic polynomial of its adjacency matrix, so it is real rooted, and so is $\mu_x[G]$ (p. 359).
- **Path tree $T_a(G)$:** vertices are paths in $G$ starting at $a$ with no repeated vertex. Two paths are joined if one extends the other by one vertex (p. 359).
- **Example (p. 360):** $G$ has edges $ab,ac,bd,cd,ce$. $T_a(G)$ has vertices $a$; $ab,abd,abdc,abdce$; $ac,acd,acdb$; $ace$. If $G$ is a tree, $T_a(G)\cong G$.
- Also $T_a(G)-a=\bigcup_{b\sim a}T_b(G-a)$ (p. 360).

**Theorem 45.4.1.** For every graph $G$ and vertex $a$:
$$\frac{\mu_x[G-a]}{\mu_x[G]}=\frac{\mu_x[T_a(G)-a]}{\mu_x[T_a(G)]}.$$
Proof by induction on $n$ (pp. 360–361):
1. Trees satisfy it trivially. Graphs with at most 2 vertices are trees, so this is the base case.
2. Lemma 45.3.2 gives $\dfrac{\mu_x[G]}{\mu_x[G-a]}=x-\sum_{b\sim a}\dfrac{\mu_x[G-a-b]}{\mu_x[G-a]}$.
3. The induction hypothesis on $G-a$ (vertex $b$) turns this into
$$x-\sum_{b\sim a}\frac{\mu_x[T_b(G-a)-b]}{\mu_x[T_b(G-a)]}.\tag{45.1}$$
4. Structure: $T_b(G-a)-b=\bigcup_{c\sim b,c\ne a}T_c(G-a-b)$, and $T_a(G)-a=\bigcup_{c\sim a}T_c(G-a)$. So $\mu_x[T_a(G)-a]=\prod_{c\sim a}\mu_x[T_c(G-a)]$.
5. With $ab$ the path vertex $a\to b$:
$$T_a(G)-a-ab=\Big(\bigcup_{c\sim a,c\ne b}T_c(G-a)\Big)\cup\big(T_b(G-a)-b\big),$$
so $\mu_x[T_a(G)-a-ab]=\Big(\prod_{c\sim a,c\ne b}\mu_x[T_c(G-a)]\Big)\mu_x[T_b(G-a)-b]$.
6. Dividing by $\mu_x[T_a(G)-a]$, the common factors cancel:
$$\frac{\mu_x[T_a(G)-a-ab]}{\mu_x[T_a(G)-a]}=\frac{\mu_x[T_b(G-a)-b]}{\mu_x[T_b(G-a)]}.$$
7. Substituting into (45.1):
$$\frac{\mu_x[G]}{\mu_x[G-a]}=x-\sum_{b\sim a}\frac{\mu_x[T_a(G)-a-ab]}{\mu_x[T_a(G)-a]}=\frac{x\mu_x[T_a(G)-a]-\sum_{b\sim a}\mu_x[T_a(G)-a-ab]}{\mu_x[T_a(G)-a]}=\frac{\mu_x[T_a(G)]}{\mu_x[T_a(G)-a]}.$$
   The last equality is Lemma 45.3.2 applied to $T_a(G)$ at its root (added step: the neighbours of the root are the vertices $ab$). Taking reciprocals gives the theorem.

*Intuition note:* the path tree "unrolls" $G$ so that, seen from $a$, it has the same deletion-ratio as $G$. Because the ratio is the same, the polynomials of $G$ and $T_a(G)$ are tied together.

**Theorem 45.4.2.** For every vertex $a$, $\mu_x[G]$ divides $\mu_x[T_a(G)]$ (p. 361).
- Proof begins by induction, base case at most 2 vertices. By induction, $\mu_x[G-a]$ divides $\mu_x[T_b(G-a)]$ for $b\sim a$. Since $T_a(G)-a=\bigcup_{b\sim a}T_b(G-a)$, $\mu_x[T_b(G-a)]$ divides $\mu_x[T_a(G)-a]$. Hence $\mu_x[G-a]$ divides $\mu_x[T_a(G)-a]$.
- The given pages end here; the rest of the proof is not in this unit.

## Toy example (ours)
Triangle $G$ on $a,b,c$: $n=3$, $m_0=1$, $m_1=3$, so $\mu_x[G]=x^3-3x$. It is not a tree: $\chi_x(A_G)=(x-2)(x+1)^2=x^3-3x-2\ne\mu_x[G]$.
- Path tree $T_a(G)$: path $abc - ab - a - ac - acb$, a path on 5 vertices with 4 edges. $m_1=4$. Size-2 matchings are non-adjacent edge pairs: (1,3),(1,4),(2,4), so $m_2=3$. Thus $\mu_x[T_a(G)]=x^5-4x^3+3x=x(x^2-1)(x^2-3)$.
- Divisibility: $(x^3-3x)(x^2-1)=x^5-x^3-3x^3+3x=x^5-4x^3+3x$ ✓.
- Theorem 45.4.1: $G-a$ is one edge, $\mu=x^2-1$. $T_a(G)-a$ is two disjoint edges, $\mu=(x^2-1)^2$. Left: $\frac{x^2-1}{x(x^2-3)}$. Right: $\frac{(x^2-1)^2}{x(x^2-1)(x^2-3)}=\frac{x^2-1}{x(x^2-3)}$ ✓.

## Concepts
- [[matching-polynomial]] (new) — $\mu_x[G]=\sum x^{n-2k}(-1)^km_k(G)$; coefficients count matchings (p. 358)
- [[matching]] (new) — subgraph with every vertex of degree 1; size = number of edges (p. 357)
- [[path-tree]] (new) — tree of simple paths from $a$, each joined to its one-vertex extension (p. 359)
- [[characteristic-polynomial]] — $\det(xI-A_G)$; equals $\mu_x$ for trees (p. 359)
- [[adjacency-matrix]] — $A_G$ of the graph, used in $\chi_x(A_G)$ (p. 359)

## Canonical instances
- [[path-tree-example-abcde]] — the 5-vertex graph and its path tree from $a$ (p. 360)

## Bridges (candidates)
- [same-math] $\mu_x[T]=\chi_x(A_T)$ for trees ↔ linear-algebra: determinant expansion over permutations — only involutions survive when there are no cycles.
- [structural-analogy] Path tree unrolling $G$ ↔ graph covers/walks on trees: universal-cover-like view of $G$ from $a$ (the source does not state this).
- [metaphor] $2\sqrt{d-1}$ as spectral radius of $d$-ary tree ↔ free probability, as the author suspects (p. 357).

## Questions this raises
- How does divisibility plus real-rootedness give roots at most $2\sqrt{d-1}$ for maximum degree $d$?
- What formal relation joins the $2\sqrt{d-1}$ here with the previous lecture's bound (author's open hope, p. 357)?
- Why is the ratio identity of Theorem 45.4.1 true "naturally", and is there a proof avoiding it (p. 360)?

## Reading notes
- Printed page = pdf − 24. The unit ends mid-proof (Theorem 45.4.2); page 361 stops at "Thus, $\mu_x[G-a]$ divides $\mu_x[T_a(G)-a]$,".
- Misprints (checked in images): Lemma 45.3.1 proof writes $\mu_j(G)\mu_{k-j}(H)$ where $m_j,m_{k-j}$ is meant. In Theorem 45.4.1's proof "inequality" should read "equality". Also "forrest", "Be obtain".
- The recurrence display on p. 358 omits the $\sum_{b\sim a}$ in the second term; it is implied by the preceding line.
- The author's definition of matching ("every vertex has degree 1") is read as covering only the vertices touched by the matching, since $m_k$ is used for $k<n/2$.
