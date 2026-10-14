---
id: spielman-2025-sagt/ch15-tutte
work: spielman-2025-sagt
unit: "Chapter 15 — Tutte's Theorem: How to draw a graph"
pages: 134–141
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Tutte's Theorem: How to draw a graph

## L0 — One line
In a 3-connected planar graph, fix one face as a strictly convex polygon and put every other vertex at a weighted average of its neighbours (the proof only needs it to lie inside the convex hull of its neighbours); drawing edges as straight lines then gives a planar drawing.

## L1 — The gist (≤ 120 words)
The question: can spring embeddings draw a planar graph without edge crossings? The answer is Tutte's theorem. Take a 3-connected planar graph. Nail one face to a strictly convex polygon. Let every other vertex sit at a weighted average of its neighbours. Then straight-line edges form a planar drawing. The proof is based on Geelen's. First, averaging (with 3-connectivity) gives geometric facts: no vertex is collinear with all its neighbours, and half-plane vertex sets are connected. Second, the two faces beside any non-boundary edge lie on opposite sides of that edge. Third, a "generic point" argument shows that no two edges cross. It matters because planarity of the drawing follows from algebraic harmonicity plus 3-connectivity.

**Prerequisites:** graph basics (paths, connectivity, induced subgraph); convex sets and half-planes in $\mathbb{R}^2$; weighted averages; proof by contradiction. Terms used in L0–L2: *3-connected* = no two vertices disconnect the graph; *strictly convex polygon* = convex with every corner angle below $\pi$; *harmonic* = a vertex sits at a weighted average of its neighbours; *collinear* = on one line; *half-plane* = everything on one side of a line; *generic point* = a point on no vertex and no edge drawing; *non-boundary edge* = an edge not on the outside face.

## L2 — Key ideas (5–10 bullets)
- A Tutte embedding fixes one face as a strictly convex polygon and makes every other vertex harmonic (a weighted average of its neighbours). (p. 137–138)
- Tutte's theorem: straight-line edges of a Tutte embedding of a 3-connected planar graph give a planar drawing. (p. 138)
- The proof uses only that each non-boundary vertex lies in the convex hull of its neighbours, which corresponds to allowing arbitrary spring constants. (p. 138)
- Harmonicity gives two facts. A vertex with a neighbour on one side of a line through it has a neighbour on the other side. Non-boundary vertices lie strictly inside the polygon. (p. 138–139)
- Half-plane vertex sets induce connected subgraphs. No vertex is collinear with all its neighbours; otherwise $G$ would have a $K_{3,3}$ minor. (p. 139)
- The proof relies on Kuratowski's theorem (quoted as a standard fact, not proved) and on Geelen's Lemma 15.1.3 (proved by a planar-drawing argument). (p. 136)
- Every non-boundary edge has its two neighbouring faces on strictly opposite sides. A generic-point argument then shows no two edges cross. (p. 140–141)

## L3 — Walkthrough

**Intro and 15.1: 3-connected planar graphs.**
- Setup: nail the vertices of one face to a strictly convex polygon, with face edges along polygon edges. Every other vertex goes to the centre of gravity of its neighbours. Tutte proved the result is a planar embedding. The proof is based on one constructed by Geelen. (p. 134)
- $G$ is $k$-connected if for every $S\subset V$ with $|S|<k$, $G(V-S)$ is connected. (p. 134)
- A planar drawing maps vertices to distinct points $z:V\to\mathbb{R}^2$ and gives interior-disjoint curves for edges. The curve for edge $(a,b)$ runs from $z(a)$ to $z(b)$, never crosses itself, and meets no other edge curve or vertex in its interior. Faces are the connected regions left after removing the curves. (p. 135)
- In a 3-connected planar graph the vertex and edge sets bordering each face are the same in every planar drawing. There are planar graphs that are not 3-connected (Figures 15.1, 15.2) for which different planar drawings give combinatorially different faces. Only 3-connected graphs are considered. (p. 135)
- **Claim 15.1.1** (stated without proof): a 3-connected planar graph has a set of faces, each a simple cycle, with every edge in exactly two faces. (p. 135)
- Contracting an edge merges its endpoints into one vertex. This preserves planarity and 3-connectivity. (p. 136)
- A minor of $G$ is obtained by contracting some edges and possibly deleting edges and vertices. (p. 136)
- **Theorem 15.1.2 (Kuratowski).** $G$ is planar iff it has no minor isomorphic to $K_5$ or $K_{3,3}$. (p. 136)
- **Lemma 15.1.3 (Geelen).** Let $(a,b)$ be an edge of a 3-connected planar graph. Let $S_1,S_2$ be the vertex sets of its two faces. Let $P$ be a path from a vertex of $S_1-\{a,b\}$ to a vertex of $S_2-\{a,b\}$ that avoids $a,b$. Then every path from $a$ to $b$ either meets a vertex of $P$ or is the edge $(a,b)$. (p. 136)
  - Proof: in a planar drawing, follow $P$ and close the curve through the interiors of the two faces. The closing part of the curve crosses only the curve for $(a,b)$. This closed curve separates $a$ from $b$. (p. 136)
- *Intuition note:* $P$ together with a closing curve forms a fence that cuts $a$ from $b$. The only gap is the edge $(a,b)$ itself.

**15.2: Strictly convex polygons; the theorem.**
- A set is convex if the segment between any two of its points lies in it. A convex polygon is strictly convex if every corner angle is less than $\pi$. Equivalently, for each polygon edge, all other corners lie strictly on one side of its line. Corners are assumed distinct. (p. 137)
- **Definition 15.2.1 (Tutte embedding).** $z:V\to\mathbb{R}^2$ for 3-connected planar $G$, such that (a) some face $F$ is mapped to the corners of a strictly convex polygon, with face edges joining consecutive corners; (b) $z$ is harmonic at every vertex not in $F$, i.e. each lies at the weighted average of its neighbours. (p. 137–138)
- For 3-connected $G$, one can show these conditions put every vertex outside $F$ strictly inside the polygon. (p. 138)
- The proof does not use exact averaging. It uses only that each non-boundary vertex is inside the convex hull of its neighbours, which allows arbitrary spring constants. (p. 138)
- **Theorem 15.2.2.** If $z$ is a Tutte embedding of 3-connected planar $G$ and edges are drawn as straight segments, the result is a planar drawing. (p. 138)
- Without 3-connectivity the embedding can degenerate. If removing two vertices $a,b$ disconnects $G$, all vertices of one component land on the segment from $a$ to $b$. (p. 138)

**15.3: Consequences of harmonicity.**
- **Claim 15.3.1.** For a vertex $a$ and any line $\ell$ through $z(a)$: if $a$ has a neighbour strictly on one side of $\ell$, it has one on the other side. (p. 138)
- **Claim 15.3.2.** All vertices not in $F$ lie strictly inside the convex hull of the polygon. (p. 138)
  - Proof: eliminate every vertex outside $F\cup\{a\}$ (Lecture 13). Then all neighbours of $a$ are in $F$, so $z(a)$ is a weighted average of positions of $F$-vertices. By 3-connectivity, at least 3 of these weights are nonzero ("we can show"; not proved here). (p. 139)
  - The author notes that Claim 15.3.2 can also be proved by showing that moving vertices inside the polygon reduces the potential energy, citing Claim 8.8.1 of his 2015 lecture notes (not reproduced here). (p. 139)
- **Lemma 15.3.3.** For any halfspace $H$, the subgraph induced on $\{a: z(a)\in H\}$ is connected. (p. 139)
  - Proof: write $H=\{x: t^Tx\ge\mu\}$ and define $t(c)=t^Tz(c)$. Take $a$ with $z(a)\in H$, and $b$ maximising $t(b)$. By Claim 15.3.2, $b\in F$. The goal is a path from $a$ to $b$ along which $t$ never decreases, so it stays in $H$. (p. 139)
  - Case $t(a)=t(b)$: then $a\in F$, and by strict convexity $(a,b)$ is a polygon edge, hence the path. (p. 139)
  - Case $t(a)<t(b)$: it suffices to reach some $c$ with $t(c)>t(a)$ without decreasing $t$, then continue from $c$. Let $U$ be the vertices reachable from $a$ with $t=t(a)$. By connectivity, some $u\in U$ has a neighbour $c\notin U$. By Claim 15.3.1, $u$ has a neighbour with $t>t(u)$. Go from $a$ through $U$ to that neighbour. (p. 139)
- **Lemma 15.3.4.** No vertex is collinear with all its neighbours. (p. 139)
  - Proof: for vertices in $F$ this is trivial, since no three of them are collinear. Otherwise suppose $a$ is collinear with all its neighbours, on a line $\ell$. Let $S^+,S^-$ be the vertices above and below $\ell$; both are connected by Lemma 15.3.3. (p. 139)
  - Let $U$ be the vertices reachable from $a$ all of whose neighbours lie on $\ell$. Let $W$ be the vertices on $\ell$ that neighbour $U$ but are not in $U$. By Claim 15.3.1 each $w\in W$ has neighbours in both $S^+$ and $S^-$. (p. 139)
  - Removing $W$ would disconnect $U$ from the rest, so 3-connectivity gives $|W|\ge3$. Take $w_1,w_2,w_3\in W$. Contracting $S^+$, $S^-$ and $U$ gives a $K_{3,3}$ minor with $\{w_1,w_2,w_3\}$ on one side. This contradicts planarity via Theorem 15.1.2. (p. 139)
- *Intuition note:* averaging means a vertex with a neighbour on one side of a line through it must also have one on the other side (Claim 15.3.1). Three "walls" ($S^+$, $S^-$, $U$) all joined to three vertices on the line would form $K_{3,3}$, which a planar graph cannot contain.

**15.4: All faces are convex.**
- **Lemma 15.4.1.** Let $(a,b)$ be a non-boundary edge and $\ell$ a line through $z(a),z(b)$. Let $S_0,S_1$ be the vertices of the two faces on $(a,b)$, other than $a,b$. Then $S_0$ and $S_1$ lie strictly on opposite sides of $\ell$. (p. 140)
  - If $z(a)=z(b)$, a line through them and a vertex of $S_0$ leads to a contradiction, so this degeneracy is excluded. (p. 140)
  - Proof by contradiction: assume $s_0\in S_0$ and $s_1\in S_1$ lie on or below $\ell$. By Lemma 15.3.4 and Claim 15.3.1, each has a neighbour strictly below $\ell$. By Lemma 15.3.3, a path $P$ joins $s_0$ to $s_1$ with all internal vertices strictly below $\ell$. (p. 140)
  - Similarly, $a$ and $b$ have neighbours above $\ell$ and are joined by a path strictly above $\ell$. This path is not the edge $(a,b)$ and is disjoint from $P$. That contradicts Lemma 15.1.3. (p. 140)
- Summary: no degeneracies; every face is a strictly convex polygon; the two faces on an edge lie on opposite sides of it. (p. 140)
- **Proof of Theorem 15.2.2.** A point is *generic* if it lies on no $z(a)$ and on no edge segment. First show every generic point lies in exactly one face. (p. 140)
  - A point outside the polygon of $F$ lies only in the outside face. For any other generic point, draw a curve from there that avoids all $z(a)$ and crosses edges only in their interiors. By Lemma 15.4.1, each crossing moves it from one face to another. So it is never in two faces. (p. 141)
  - If two edge drawings crossed, a generic point near the crossing would lie in at least two faces. This is a contradiction. (p. 141)
- *Intuition note:* by Lemma 15.4.1 the two faces at an edge lie on opposite sides of it, so a curve that crosses an edge in its interior moves from one face to the other. Hence the curve is never in two faces at once, and a crossing of two edges would put a generic point in two faces.

## Toy example (ours, not from the text)
$G=K_4$ on vertices 1,2,3,4 (3-connected, planar). Take $F=\{1,2,3\}$ with $z(1)=(0,0)$, $z(2)=(1,0)$, $z(3)=(0,1)$, a strictly convex triangle. Vertex 4 has neighbours 1, 2, 3, so with equal weights
$z(4)=\tfrac13[(0,0)+(1,0)+(0,1)]=(\tfrac13,\tfrac13)$,
strictly inside the triangle (Claim 15.3.2).
Check Lemma 15.4.1 for the non-boundary edge $(4,1)$. Its faces are $\{1,2,4\}$ and $\{1,3,4\}$, so $S_0=\{2\}$, $S_1=\{3\}$. The line $\ell$ through $z(4),z(1)$ is $y=x$. Vertex 2: $y-x=0-1=-1<0$. Vertex 3: $y-x=1-0=1>0$. They lie strictly on opposite sides. ✓.

## Concepts
- [[tutte-embedding]] (new) — nailed strictly convex face, other vertices harmonic (p. 137–138)
- [[k-connected-graph]] (new) — no set of fewer than $k$ vertices disconnects it (p. 134)
- [[planar-drawing]] (new) — vertices to distinct points, interior-disjoint edge curves (p. 135)
- [[graph-minor]] (new) — obtained by contracting edges, deleting edges/vertices (p. 136)
- [[strictly-convex-polygon]] (new) — convex, all corner angles less than $\pi$, no corner on another edge's line (p. 137)
- [[harmonic-function-on-graph]] (new) — value at a vertex equals a weighted average of neighbours' values (p. 138)
- [[kuratowski-theorem]] (new) — planar iff no $K_5$ or $K_{3,3}$ minor (p. 136)

## Canonical instances
- [[petersen-graph-nonplanar]] — a minor isomorphic to $K_5$ shows it is not planar (Fig. 15.4, p. 137)
- [[non-3-connected-planar-graphs]] — 1- and 2-connected examples whose faces vary between drawings (Figs. 15.1, 15.2, p. 135)
- [[edge-contraction-example]] — contracting $(g,h)$ in a 3-connected planar graph (Fig. 15.3, p. 136)

## Bridges (candidates)
- [same-math] Harmonic condition at non-boundary vertices ↔ graph Laplacian: weighted-Laplacian equation $(Lz)(a)=0$ off the boundary — the averaging condition is the same linear equation.
- [structural-analogy] Convex hull / "nothing can be extreme inside" ↔ maximum principle for harmonic functions: the maximum of $t^Tz$ occurs on $F$ (p. 139).
- [metaphor] Spring embeddings ↔ physical networks of springs: equilibrium as minimum energy (p. 139 mentions potential energy).

## Questions this raises
- How exactly does eliminating vertices (Lecture 13) show the nonzero-weight claim for at least 3 vertices of $F$?
- Do the proofs of Lemmas 15.3.4 and 15.4.1 break down for graphs that are only 2-connected?
- Is the Tutte embedding unique given $F$ and the polygon, and how is it computed?

## Reading notes
- Printed page = pdf − 24.
- Misprints: after the contraction paragraph (p. 136), "Figure 15.1" should be Figure 15.3. At the end of the proof of Lemma 15.1.3, "See Figure 15.1" should be Figure 15.5. "Peterson" in Fig. 15.4's caption is spelled as printed.
- Definition 15.2.1(b) has a garbled sentence ("That is, if every vertex…").
- The draft's cited facts (Claim 15.1.1, Kuratowski, Lecture 13, 2015 notes) are not proved in this unit.
- Section 15.5 is a short note: the author calls this the simplest proof of Tutte's theorem he has seen, and mentions expositions by Lovász and Geelen and an alternative proof by Gortler, Gotsman and Thurston.
