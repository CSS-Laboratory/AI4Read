---
id: spielman-2025-sagt/ch30-simple
work: spielman-2025-sagt
unit: "Chapter 30 — A simple construction of expander graphs"
pages: 243–250
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A simple construction of expander graphs

## L0 — One line
Take the line graph of a graph (its vertices are the edges of the original), replace each of its cliques (groups of mutually adjacent vertices) by a small expander (a sparse, well-connected graph), then square twice; the spectral gap (a measure of how well connected the graph is) stays above a fixed bound while the degree stays fixed, so repeating this builds an infinite family of constant-degree expanders.

## L1 — The gist (≤ 120 words)
Question: can we build, for fixed ε, an infinite family of d-regular ε-expanders with d independent of the number of vertices? Random generalized hypercubes fail, because their degree grows like log n. Answer: start from small expanders. Take a line graph, which makes the graph bigger but keeps λ₂ and raises the degree. Replace each clique by a small expander, which cuts the degree back to 2k and loses a little more than a factor 2 of spectral gap. Then square twice, which restores the gap and returns the degree to exactly d. Every step is an exact spectral identity or a simple inequality. This matters because it gives an explicit, easy-to-analyse construction.

**Prerequisites:** Laplacian and adjacency eigenvalues of regular graphs; L = UᵀU; the Loewner order ≼ (quadratic-form comparison); eigenvalues of AB versus BA.

## L2 — Key ideas
- Squaring a graph maps adjacency eigenvalues μ ↦ μ² − d. A d-regular β-expander with β ≥ 1/√(d−1) becomes a β²-expander, at the cost of a higher degree d(d−1) (p. 244).
- The relative spectral gap r(G) = min(λ₂/d, (2d−λₙ)/d) measures expansion; an ε-expander has r ≥ 1−ε and vice versa (p. 245).
- The Laplacian spectrum of a line graph H equals that of G, plus dn/2 − n extra eigenvalues 2d. This follows from |U|ᵀ|U| and |U||U|ᵀ sharing eigenvalues (pp. 246–247).
- Line graphs enlarge a graph and keep λ₂, but raise the degree to 2(d−1) (pp. 245–247).
- Replacing each d-clique of the line graph by a k-regular α-expander gives a spectral approximation of the line graph, with degree 2k and r(G ⓛ Z) ≥ ((1−α)/2)·r(G) (pp. 248–249).
- Squaring twice fixes the degree. The degree 2k of Gᵢ ⓛ Z becomes exactly d = (2k(2k−1))² − 2k(2k−1), which is the number of vertices the small expander Z must have (pp. 249–250).
- With Z a 1/6-expander and r(Gᵢ) ≥ 4/5, the induction gives r(Gᵢ₊₁) ≥ 65/81 > 4/5 (p. 250).

## L3 — Walkthrough

### 30.1 Overview (pp. 243–244)
Goal: for every ε>0 there is a d for which we can efficiently construct an infinite family of d-regular ε-expanders (p. 243). Here an ε-expander has |μᵢ| ≤ εd for adjacency eigenvalues and |d−λᵢ| ≤ εd for Laplacian eigenvalues, for i>1 (p. 243). The d obtained is large but constant.

Random generalized hypercubes have degree f(ε) log n, which depends on n, so they fail. The construction requires some small expanders; random generalized ring graphs (Claim 30.1.1) can supply them. **Claim 30.1.1:** for every ε>0 and sufficiently large n, the Cayley graph on Z/n with at least f(ε) log n random generators is an ε-expander with high probability (p. 243).

Quick recipe: start with an expander; take its line graph (a union of cliques); replace each clique by a small expander; square; square again; repeat (p. 243). The construction is explicit: if a vertex name has b bits, its neighbours can be computed in time polynomial in b (p. 244).

### 30.2 Squaring graphs (p. 244)
G² joins u,v when they are at distance 2. Strictly it is weighted by the number of such paths; treat these weights as multiedges. With M the adjacency matrix of G, M²(u,v) counts length-2 paths, and M²(v,v) = d. Remove these self-loops:
$$M_{G^2} = M_G^2 - dI_n.$$
**Claim 30.2.1:** the adjacency eigenvalues of G² are precisely $\mu_i^2 - d$.

**Lemma 30.2.2:** if {Gᵢ} are d-regular β-expanders with $\beta \ge 1/\sqrt{d-1}$, then {Gᵢ²} are d(d−1)-regular β²-expanders.
Proof. For an eigenvalue μ ≠ d of Gᵢ:
$$\frac{\mu^2-d}{d(d-1)}=\frac{\mu^2-d}{d^2-d}\le\frac{\mu^2}{d^2}\le\beta^2 .$$
Every adjacency eigenvalue of Gᵢ² is at least −d, which is at least $-\beta^2 d(d-1)$.
So repeated squaring turns β-expanders (any β<1) into ε-expanders.

*Intuition note:* Eigenvalues of M are squared, so those with |μ|/d < 1 shrink fast. The cost is a larger degree, because each vertex now has d(d−1) length-2 walks.

### 30.3 Relative spectral gap (p. 245)
For a d-regular graph:
$$r(G)\overset{\text{def}}{=}\min\left(\frac{\lambda_2(G)}{d},\frac{2d-\lambda_n}{d}\right).$$
Larger r means a better expander; an ε-expander has r ≥ 1−ε and vice versa. So it suffices to find an infinite family with r strictly above 0.
**Corollary 30.3.1:** if r(G)=β then r(G²) ≥ 2β − β². (The text gives no separate proof. *Added step:* G is a (1−β)-expander, so by Lemma 30.2.2 G² is a (1−β)²-expander, and 1−(1−β)² = 2β−β². This uses Lemma 30.2.2, so it needs 1−β ≥ 1/√(d−1); the text does not state this condition.) For small β this is about 2β.

### 30.4 Line graphs (pp. 245–246)
The line graph H of G has the edges of G as vertices; two are adjacent if they share an endpoint (p. 245). Figure: a 6-vertex graph on a–f and its line graph (p. 245).
If G is d-regular on n vertices, H has dn/2 vertices, each of degree 2(d−1). H contains a d-clique for each vertex of G, and each vertex of H lies in exactly two cliques (pp. 245–246).

The signed edge–vertex matrix U has rows indexed by edges, with U((a,b),c) = 1 if a=c, −1 if b=c, and 0 otherwise. It satisfies $L_G=U^TU$ (p. 246).

**Lemma 30.4.1:** the Laplacian spectrum of H equals that of G, plus dn/2 − n extra eigenvalues 2d (p. 246).

### 30.5 The spectrum of the line graph (pp. 246–247)
Let |U| have entrywise absolute values. Shapes: U and |U| are (nd/2)×n.
- $|U|^T|U| = D_G+M_G = dI+M_G$, an n×n matrix (p. 246).
- $|U||U|^T = 2I_{nd/2}+M_H$, an (nd/2)×(nd/2) matrix. Its (u,v),(w,z) entry is $(\delta_u+\delta_v)^T(\delta_w+\delta_z)$: 2 for the same edge, 1 if the edges share a vertex, 0 otherwise (p. 246).
- The two products have the same eigenvalues, except for nd/2 − n extra zeros (p. 246).

Proof of Lemma 30.4.1 (p. 247). If λᵢ is an eigenvalue of $L_G=D_G-M_G$, then:
d−λᵢ is an eigenvalue of $M_G$ ⟹ 2d−λᵢ is an eigenvalue of $D_G+M_G$ ⟹ 2d−λᵢ is an eigenvalue of $2I+M_H$ ⟹ 2(d−1)−λᵢ is an eigenvalue of $M_H$ ⟹ λᵢ is an eigenvalue of $D_H-M_H=L_H$.
The extra zeros of $2I+M_H$ become 2d in $L_H$. (*Added step:* a zero there means −2 for $M_H$, so $L_H$ gets 2(d−1)+2 = 2d.)

*Intuition note:* Edge-to-vertex and vertex-to-edge maps share nonzero spectrum. The line graph keeps G's Laplacian spectrum and adds only extra eigenvalues equal to 2d.

**Proposition 30.5.1:** for d-regular G with d ≥ 7 and H its line graph, $r(H)=\lambda_2(G)/(2(d-1))\ge r(G)/2$ (p. 247).
Proof sketch. λ₂(G) ≤ d+1 for G ≠ K_{d+1}. By Perron–Frobenius, λ_max(G) ≤ 2d. So λ_max(H)=2d and λ₂(H)=λ₂(G) ≤ d. H has degree 2d−2. The top-end term is
$$\frac{2(2d-2)-2d}{2d-2}=1-\frac2d\ge\frac57$$
as written by the author, using d ≥ 7. The other term satisfies $\lambda_2(H)/(2d-2)\le d/(2d-2)\le 2/3<5/7$. So r(H) is the λ₂ term, $\lambda_2(G)/(2d-2)$. (*Added step:* this is ≥ λ₂(G)/(2d) ≥ r(G)/2.)
The degree has grown and r has roughly halved (p. 247).

### 30.6 Approximations of line graphs (pp. 248–249)
Let Z be a k-regular graph on d vertices. Define G ⓛ Z: form H, then replace each d-clique by a copy of Z (any placement works). Every vertex has degree 2k (p. 248).

**Lemma 30.6.1:** if Z is a k-regular α-expander, then
$$(1-\alpha)\tfrac kd\,H\preccurlyeq G\,ⓛ\,Z\preccurlyeq(1+\alpha)\tfrac kd\,H$$
(as Laplacians). Proof: $L_H=\sum_{i=1}^n L_{H_i}$ over the d-cliques. With $Z_i$ the copy of Z placed on clique i (p. 248),
$$L_{G ⓛ Z}=\sum_i L_{Z_i}\succcurlyeq(1-\alpha)\tfrac kd\sum_i L_{H_i}=(1-\alpha)\tfrac kd L_H.$$
The upper bound is similar. The inequality per clique is used without separate statement.

**Corollary 30.6.2:** $r(G ⓛ Z)\ge\frac{1-\alpha}{2}r(G)$ (p. 248).
Proof. λ₂(G ⓛ Z) ≥ (1−α)kλ₂(G)/d and λ_max ≤ (1+α)2k (p. 248). Hence
$$\min\big(\lambda_2,\,2(2k)-\lambda_{\max}\big)\ge\min\Big((1-\alpha)\tfrac{k\lambda_2(G)}{d},\,(1-\alpha)2k\Big)=(1-\alpha)\tfrac{k\lambda_2(G)}{d},$$
since λ₂(G) ≤ d. Dividing by the degree 2k gives $\ge\frac{1}{2k}(1-\alpha)k\,r(G)=\frac{1-\alpha}2r(G)$ (p. 249).

*Intuition note:* A small expander is a cheap stand-in for a clique. It keeps the gap up to a factor (1−α), but the degree falls from about 2d to 2k.

### 30.7 The whole construction (pp. 249–250)
Choose k. Let Z be a k-regular ε-expander on
$$d\overset{\text{def}}{=}(2k(2k-1))^2-2k(2k-1)$$
vertices; the author believes ε=1/6 suffices. Let G₀ be a small d-regular expander with relative gap β>0 (both exist by Claim 30.1.1). The author "believes" β=1/5 works (p. 249). Set
$$G_{i+1}=\big((G_i\,ⓛ\,Z)^2\big)^2.$$
Degrees: Gᵢ ⓛ Z has degree 2k; one squaring gives 2k(2k−1) ≈ 4k²; the second gives d (approximately 16k⁴) (pp. 249–250). (*Added step:* with m=2k(2k−1), the second squaring gives m(m−1)=m²−m=d, so each Gᵢ₊₁ is d-regular and Z fits every clique.)

Careful computation (p. 250). Assume r(G₀) ≥ 4/5, assume r(Gᵢ) ≥ 4/5 by induction, and let Z be a 1/6-expander. Then
$$r(G_i ⓛ Z)\ge(1-\epsilon)\tfrac{4/5}2=\tfrac13,$$
so Gᵢ ⓛ Z is a 2/3-expander. Two squarings make Gᵢ₊₁ a (2/3)⁴-expander, so
$$r(G_{i+1})\ge1-(2/3)^4=65/81>4/5.$$
So every Gᵢ has r ≥ 4/5. Further squarings improve the gap.

*Intuition note:* One squaring is not quite enough to make up the loss of a factor (1−ε)/2 from the clique-replacement step, so the construction squares twice. The gap then stays above the threshold at every level while the degree is held at d.

### 30.8 Better constructions (p. 250)
The Zig-Zag product [RVW02] is trickier but gives better expansion. The author presents the line-graph method because its analysis closely resembles that of Zig-Zag.

## Toy example (ours)
Take G = K₄ (d=3, n=4). Its Laplacian eigenvalues are 0,4,4,4. Its line graph H has dn/2 = 6 vertices, one per edge of K₄. Two edges are non-adjacent only when disjoint, and each edge has exactly one disjoint partner. So each vertex of H has degree 4 = 2(d−1), and H is the complement of a perfect matching on 6 vertices (the octahedron).
Adjacency eigenvalues of H are 4 (all-ones vector), −2 twice, and 0 three times, because the matching has eigenvalues +1 (×3) and −1 (×3). The all-ones vector is excluded from the matching's remaining +1 eigenvalues, leaving two of them and three of −1. Check: J−I−P gives −1−1 = −2 twice and −1+1 = 0 three times.
Laplacian eigenvalues of H = 4 − μ: 0, 4, 4, 4, 6, 6. Lemma 30.4.1 predicts K₄'s 0,4,4,4 plus dn/2 − n = 2 extra copies of 2d = 6. ✓.

## Concepts
- [[expander-graph]] (new) — d-regular graph whose nontrivial adjacency eigenvalues are at most εd in absolute value (p. 243)
- [[relative-spectral-gap]] (new) — r(G)=min(λ₂/d,(2d−λₙ)/d); at least 1−ε iff ε-expander (p. 245)
- [[graph-squaring]] (new) — M_{G²}=M²−dI; eigenvalues μ²−d; degree d(d−1) (p. 244)
- [[line-graph]] (new) — edges of G as vertices; adjacent if they share an endpoint (p. 245)
- [[spectral-approximation]] (new) — comparing Laplacians by ≼ with multipliers (1±α)k/d (p. 248)
- [[graph-laplacian]] — L=D−A=UᵀU (p. 246)
- [[adjacency-matrix]] — M_G; M² counts length-2 paths (p. 244)
- [[incidence-matrix]] — signed edge–vertex U with L=UᵀU (p. 246)
- [[perron-frobenius-theorem]] — used to bound λ_max(G) ≤ 2d (p. 247)

## Canonical instances
- [[line-graph-six-vertex-example]] — the figure on p. 245 shows a 6-vertex graph and its line graph
- [[cayley-graph-random-generators]] — Z/n with random generators supplies the small expanders (p. 243)
- [[expander-recursion-numbers]] — ε=1/6, r ≥ 4/5, (2/3)⁴, 65/81 (p. 250)

## Bridges (candidates)
- [same-math] eigenvalues of AB and BA coincide up to zeros ↔ linear algebra: used with |U|ᵀ|U| and |U||U|ᵀ to get the line-graph spectrum
- [structural-analogy] replace a clique by a sparse expander ↔ spectral sparsification: both approximate a dense graph's Laplacian by a sparse one
- [structural-analogy] square the graph to boost the gap ↔ power iteration: squaring a matrix squares the eigenvalues

## Questions this raises
- Why does Claim 30.1.1 provide Z, whose degree k must grow with log d as d ≈ 16k⁴? Do suitable k exist?
- Lemma 30.2.2 needs β ≥ 1/√(d−1): is that satisfied at each squaring in the induction?
- How does the Zig-Zag product improve the spectral-gap/degree tradeoff?
- How far from Ramanujan is the final degree/expansion tradeoff?

## Reading notes
- Printed = pdf − 24. The page image for p. 243 was not supplied. There the text layer drops ε in "|μᵢ| ≤ εd" and similar, so I restored it from context.
- Lemma 30.4.1 text says "the later matrix has nd/2 − n extra zeros"; the larger matrix is |U||U|ᵀ, so it should be "former".
- Prop. 30.5.1 proof: "λ₂(G) ≤ d+1" is later used as "≤ d". The line "= 1 − 2/d" is really an inequality: the exact value is 1 − 1/(d−1) ≥ 1 − 2/d. The last display writes "r(G/2)", which should be r(G)/2.
- Section 30.7 says "β = 1/5 will work" but the calculation assumes β ≥ 4/5; also ρ(Gᵢ) stands for r(Gᵢ). Corollary 30.3.1 is stated without the lemma's condition on β. The text gives no proof of the "(1−α)(k/d)L_{H_i} ≼ L_{Z_i}" step.
- The source pages show no date; the draft date April 2, 2025 comes from the work citation supplied with the unit.
