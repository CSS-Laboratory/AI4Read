---
id: spielman-2025-sagt/ch40-testing
work: spielman-2025-sagt
unit: "Chapter 40 — Testing Isomorphism of Strongly Regular Graphs"
pages: 317-324
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
# Testing Isomorphism of Strongly Regular Graphs

## L0 — One line
A strongly regular graph has only three distinct adjacency eigenvalues, and every such graph has a "distinguishing set" of $O(\sqrt n\log n)$ vertices, which gives isomorphism testing in time $n^{O(\sqrt n\log n)}$.

## L1 — The gist (≤ 120 words)
The previous lecture handled graphs whose eigenvalues are all distinct. This chapter takes the opposite case: strongly regular graphs, where every adjacent pair has $\alpha$ common neighbours and every non-adjacent pair has $\beta$. Writing $A^2$ in terms of $A$, $I$, $J$ shows that $A$ has only two eigenvalues besides $d$. Isomorphism is tested by individualizing a small set of vertices and refining labels. The key lemma (used for Babai's result) says that if $d<n/2$, then for any two vertices $a,b$, $a$ has at least $d/3$ neighbours that $b$ lacks. So a random set of $O(\sqrt n\log n)$ vertices separates all pairs, with probability at least 1/2. Brute-force search over such sets is much faster than trying all $n!$ permutations.

**Prerequisites:** adjacency matrix; $(A^2)_{ab}$ counts common neighbours; eigenvalues; simple counting and probability (union bound, $(1-1/x)^x\le 1/e$).

## L2 — Key ideas
- Strongly regular means $d$-regular, with $\alpha$ common neighbours for adjacent pairs and $\beta$ for non-adjacent pairs. Examples are the pentagon, lattice graphs and Latin square graphs (pp. 318–319).
- $A^2=(\alpha-\beta)A+\beta J+(d-\beta)I$. On vectors orthogonal to $\mathbf 1$, every eigenvalue other than $d$ satisfies $\lambda^2=(\alpha-\beta)\lambda+d-\beta$, so there are two such eigenvalues, $r>s$ (p. 319).
- Isomorphism testing can be reduced to giving vertices unique names. Refinement relabels vertices by their neighbours' labels. Individualization breaks symmetry by naming chosen vertices arbitrarily (pp. 320–321).
- A distinguishing set $S$ gives every vertex a unique name after individualization and refinement. Testing isomorphism with it means checking $\binom{n}{|S|}$ sets and $|S|!$ labelings, so $S$ must be small (p. 321).
- Lemma 40.8.1: if $G$ is connected strongly regular with $d<n/2$, then for any two vertices $a,b$ at least $d/3$ vertices are neighbours of $a$ but not of $b$. The proof uses three relations among $\alpha,\beta,d,n$ (pp. 321–323).
- A random $S$ of size $3\sqrt{n+2}\,\ln n^2$ separates all pairs with probability at least 1/2 (p. 322).
- Later work improved the running time and was then subsumed by Babai's general algorithm (p. 324).

## L3 — Walkthrough

### 40.1 Introduction (p. 317)
The previous lecture treated graphs with all eigenvalues distinct. Here the graphs have 3 distinct eigenvalues. The algorithm is not polynomial. It takes time $n^{O(\sqrt n\log n)}$, which is much faster than checking all $n!$ permutations (p. 317). The author says this was the best known general isomorphism bound until three years before the lecture.

### 40.2 Definitions (pp. 317–318)
$G$ is *strongly regular* if (1) it is $d$-regular, (2) every adjacent pair has exactly $\alpha$ common neighbours, and (3) every non-adjacent pair has exactly $\beta$ common neighbours (p. 317). The literature writes $k,\lambda,\mu$ for $d,\alpha,\beta$. From here on, graphs are connected and not complete (p. 318).

### 40.3–40.5 Examples (pp. 318–319)
- **Pentagon (a Paley graph):** $n=5,\ d=2,\ \alpha=0,\ \beta=1$ (p. 318).
- **Lattice graph $L_n$:** vertices $\{1,\dots,n\}^2$. $(a,b)\sim(c,d)$ if $a=c$ or $b=d$. It is the product of two complete graphs on $n$ vertices. $d=2(n-1),\ \alpha=n-2,\ \beta=2$ (p. 318).
- **Latin square graph:** an $n\times n$ Latin square has entries in $1..n$, with no repeat in any row or column. The number of Latin squares is at least $n!(n-1)!\cdots2!$. Isomorphism (renumbering rows, columns, entries, or permuting these) gives only $6(n!)^3$ maps. So many non-isomorphic Latin squares exist (p. 318).
- Its graph has $n^2$ nodes, one per cell. Two nodes are adjacent if they share a row, a column or a number. Then $d=3(n-1)$ (p. 319).
- Adjacent nodes in the same row have the other $n-2$ row nodes as common neighbours (our reading of a garbled sentence), plus two more (the nodes in their columns holding the other's number). So $\alpha=n$. The text says the same holds for columns and for equal numbers (p. 319).
- For non-adjacent $(1,1)$ and $(2,2)$ there are 2 common neighbours in the row, 2 in the column, and 2 more holding the number of $(1,1)$ in the row or column of $(2,2)$. So $\beta=6$ (p. 319).

### 40.6 Eigenvalues (pp. 319–320)
$d$ is an eigenvalue of multiplicity 1. $(A^2)_{ab}$ is the number of common neighbours of $a,b$, and equals the degree when $a=b$. The complement has adjacency matrix $J-I-A$. Hence
$$A^2=\alpha A+\beta(J-I-A)+dI=(\alpha-\beta)A+\beta J+(d-\beta)I .$$
For $v\perp\mathbf 1$: $A^2v=(\alpha-\beta)Av+(d-\beta)v$. So every eigenvalue $\lambda\ne d$ satisfies $\lambda^2=(\alpha-\beta)\lambda+d-\beta$, giving
$$\lambda=\frac{\alpha-\beta\pm\sqrt{(\alpha-\beta)^2+4(d-\beta)}}{2}.$$
These are called $r>s$, with multiplicities $f$ and $g$ (p. 319).
- Pentagon: $r=\frac{\sqrt5-1}{2},\ s=-\frac{\sqrt5+1}{2}$.
- $L_n$: $r=n-2,\ s=-2$.
- Latin square graphs: $r=n-3,\ s=-3$ (p. 320).
The author states "one can prove" that every connected regular graph with just three distinct adjacency (or Laplacian) eigenvalues is strongly regular (p. 320).

*Intuition note:* $A^2$ counts common neighbours. In a strongly regular graph that count depends only on whether the pair is equal, adjacent or non-adjacent. That is why $A^2$ is a combination of $I,A,J$ and the spectrum is so small.

### 40.7 Individualization and refinement (pp. 320–321)
The author says isomorphism testing is often reduced to naming each vertex uniquely. If the naming does not depend on the initial vertex order, the names can be compared across two graphs to test isomorphism. *Refinement* repeatedly appends the neighbours' labels to each vertex's label, starting from degrees. In the author's example this gives every vertex a unique label (pp. 320–321). Refinement fails on regular graphs and on graphs with automorphisms. *Individualization* then gives chosen vertices unique names arbitrarily, after which refinement continues. A set $S$ is *distinguishing* if individualizing it and refining gives every vertex a unique name. Assume $S$ distinguishes $G$. To test whether $H$ is isomorphic to $G$, enumerate all $|S|$-subsets of $H$'s vertices and check whether they distinguish $H$; if $G\cong H$, then $H$ has an isomorphic distinguishing set that gives an isomorphism. This costs $\binom{n}{|S|}$ sets and $|S|!$ labelings each, "so we had better hope that $S$ is small" (p. 321).

### 40.8 Distinguishing sets (pp. 321–323)
**Babai's result:** every strongly regular graph has a distinguishing set of size $O(\sqrt n\log n)$. The result needs no refinement beyond naming each vertex by the set of individualized nodes that are its neighbours. So $S$ works if for every pair $a\ne b$ some $s\in S$ is adjacent to exactly one of them (p. 321). The complement of a strongly regular graph is strongly regular, so assume $d<n/2$. The graph has diameter 2, so $d\ge\sqrt{n-1}$ (p. 321).

**Lemma 40.8.1.** If $G$ is connected strongly regular with $d<n/2$, then for all $a,b$ at least $d/3$ vertices are neighbours of $a$ but not $b$ (p. 321).

*Use of the lemma (random set).* Let $T$ be the set of neighbours of $a$ that are not neighbours of $b$. Then, since $d\ge\sqrt{n-1}$, $|T|\ge\sqrt{n-1}/3$, so for a random vertex
$$\frac{|T|}{n}\ge\frac{\sqrt{n-1}}{3n}\ge\frac{1}{3\sqrt{n+2}}.$$
Choose $S$ of $3\sqrt{n+2}\,\ln n^2$ random vertices. The probability that none lies in $T$ is $\left(1-\frac{1}{3\sqrt{n+2}}\right)^{3\sqrt{n+2}\ln n^2}\le 1/n^2$ (using $(1-1/x)^x\le 1/e$, added step). Over all $\binom n2$ pairs, the failure probability is at most 1/2 (p. 322).

*Proof of the lemma.* Write $a\sim b$ for adjacent. If $a\sim b$, the number of neighbours of $a$ not of $b$ is $d-1-\alpha$. If $a\not\sim b$, it is $d-\beta$. So we must show neither $\alpha$ nor $\beta$ is too close to $d$ (p. 322).

1. *Case $a\sim b$.* Take $z$ with $a\not\sim z$ and $b\not\sim z$. Let $Z_0=\{w:w\sim a,\ w\not\sim z\}$ and $Z_1=\{w:w\not\sim b,\ w\sim z\}$. Every neighbour of $a$ that is not a neighbour of $b$ lies in $Z_0\cup Z_1$. Since $z$ is adjacent to neither $a$ nor $b$, $|Z_0|=|Z_1|=d-\beta$. Hence
$$d-\alpha-1\le 2(d-\beta)\ \Rightarrow\ 2\beta\le d+\alpha+1.\tag{40.1}$$
2. *Case $a\not\sim b$.* Take $z\sim a$ and $z\sim b$. Any $w\sim a$, $w\not\sim b$ satisfies ($w\not\sim z$) or ($w\sim z$, $w\not\sim b$). (added step) The set $\{w:w\sim a,\ w\not\sim z\}$ has $d-\alpha$ elements, since $z\sim a$ gives $\alpha$ common neighbours. It contains $z$ itself, which cannot be a valid $w$ because $z\sim b$. The set $\{w:w\sim z,\ w\not\sim b\}$ has $d-\alpha$ elements, since $z\sim b$. It contains $a$, which is not a valid $w$ because $a\not\sim a$. So each set contributes at most $d-\alpha-1$ vertices $w$. So
$$d-\beta\le 2(d-\alpha-1)\ \Rightarrow\ 2(\alpha+1)\le d+\beta.\tag{40.2}$$
3. *Third relation.* Fix $a$ and count pairs $(b,z)$ with $b\sim z,\ a\sim b,\ a\not\sim z$. Each of the $d$ neighbours $b$ of $a$ has $d-\alpha-1$ neighbours outside $a$'s neighbourhood. Each of the $n-d-1$ non-neighbours $z$ has $\beta$ common neighbours with $a$. So
$$(n-d-1)\beta=d(d-\alpha-1).\tag{40.3}$$
As $d<n/2$, $n-d-1\ge d$ (added step: $n-d>d$ and the numbers are integers), so $d(d-\alpha-1)\ge d\beta$, i.e.
$$d-\alpha-1\ge\beta.\tag{40.4}$$
4. Adding (40.1) and (40.4) gives $2d\ge3\beta$, so $\beta\le\frac23 d$. Adding (40.2) and (40.4) gives $\alpha+1\le\frac23 d$. Therefore $\min(d-\alpha-1,\,d-\beta)\ge d/3$ (p. 323). ∎

*Intuition note:* Strong regularity forces any two vertices to see quite different neighbourhoods. When $d<n/2$, a random vertex then separates them with probability at least $1/(3\sqrt{n+2})$, so about $\sqrt n\log n$ random vertices suffice to separate all pairs with probability at least 1/2.

*Running time (added step, not computed in the text):* $|S|=O(\sqrt n\log n)$ and at most $\binom{n}{|S|}|S|!\le n^{|S|}$ labelings, consistent with $n^{O(\sqrt n\log n)}$ (p. 317).

### 40.9 Notes (p. 324)
Analysing two refinement phases gave $2^{O(n^{1/3}\log n)}$ [Spi96b]. That algorithm handled Latin square graphs and Steiner graphs separately. Babai, Chen, Sun, Teng and Wilmes improved on this later. All these bounds are subsumed by Babai's general algorithm [Bab16] (p. 324).

## Toy example (ours)
Pentagon, vertices $0..4$ in a cycle: $n=5,d=2,\alpha=0,\beta=1$.
- $A^2=(\alpha-\beta)A+\beta J+(d-\beta)I=-A+J+I$. Diagonal: $0+1+1=2=d$ ✓. Adjacent pair: $-1+1+0=0=\alpha$ ✓. Non-adjacent pair: $0+1+0=1=\beta$ ✓.
- $\lambda^2=-\lambda+1$, so $\lambda=\frac{-1\pm\sqrt5}{2}$, as in the text.
- Lemma check ($d=2<2.5$): vertices 2,3 are adjacent. $N(2)=\{1,3\}$, $N(3)=\{2,4\}$. Neighbours of 2 not of 3, apart from 3 itself: $\{1\}$, size $1=d-1-\alpha$ ✓. Vertices 0,2 are non-adjacent. $N(0)=\{1,4\}$, $N(2)=\{1,3\}$. Neighbours of 0 not of 2: $\{4\}$, size $1=d-\beta$ ✓. Both are at least $d/3\approx0.67$.
- Distinguishing set $S=\{0,1\}$: vertex 2 is adjacent to (0? no, 1? yes) → $(0,1)$. Vertex 3 → $(0,0)$. Vertex 4 → $(1,0)$. All three are distinct, and 0 and 1 are named individually.

## Concepts
- [[strongly-regular-graph]] (new) — $d$-regular graph (the chapter then takes it connected and not complete) with constant common-neighbour counts $\alpha$ (adjacent) and $\beta$ (non-adjacent) (p. 317)
- [[adjacency-matrix]] — $(A^2)_{ab}$ counts common neighbours; used to get $A^2=(\alpha-\beta)A+\beta J+(d-\beta)I$ (p. 319)
- [[eigenvector-eigenvalue]] — $d$ (multiplicity 1) plus two roots $r>s$ of $\lambda^2=(\alpha-\beta)\lambda+d-\beta$ (p. 319)
- [[individualization-refinement]] (new) — naming chosen vertices arbitrarily, then relabeling by neighbour labels (p. 321)
- [[distinguishing-set]] (new) — vertex set whose individualization plus refinement names every vertex uniquely (p. 321)
- [[graph-isomorphism]] (new) — here, testing by finding order-independent unique vertex names (p. 320)

## Canonical instances
- [[pentagon-paley-graph]] — $n=5,d=2,\alpha=0,\beta=1$ (p. 318)
- [[lattice-graph]] — $d=2(n-1),\alpha=n-2,\beta=2$; $r=n-2,s=-2$ (pp. 318, 320)
- [[latin-square-graph]] — $d=3(n-1),\alpha=n,\beta=6$; $r=n-3,s=-3$ (pp. 319–320)

## Bridges (candidates)
- [same-math] $A^2$ entries as common-neighbour counts ↔ walk counting: $(A^k)_{ij}$ counts walks of length $k$ — here $k=2$.
- [structural-analogy] Random set separates all pairs with a union bound ↔ probabilistic method in combinatorics: show existence by random choice.

## Questions this raises
- Why must a connected regular graph with exactly three distinct eigenvalues be strongly regular (the "one can prove" on p. 320)?
- How much does analysing further refinement phases reduce the bound (p. 324)?
- Does the diameter-2 claim (p. 321) follow directly from the definition?
- Can the $d/3$ constant in Lemma 40.8.1 be improved?

## Reading notes
- Printed = pdf − 24. The chapter opens with the red note "This Chapter Needs Editing"; the work citation (not these pages) gives a draft dated April 2, 2025.
- Page 322: the image shows $3\sqrt{n+2}$ with the root over $n+2$. The text layer is ambiguous.
- Page 319: "will both be neighbors with every other pair of nodes in their row" is a garbled phrase in the source. The count $\alpha=n$ is consistent with the argument.
- The text does not show that the vertex $z$ in the proof (cases 1 and 2) exists. The "three years ago" in 40.1 is relative to the original lecture, whose date these pages do not give.
- The example graph labels on page 320 are in figures. I did not reproduce them.
