---
id: spielman-2025-sagt/ch25-second
work: spielman-2025-sagt
unit: "Chapter 25 — The Second Eigenvalue of Planar Graphs"
pages: 204-210
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
# The Second Eigenvalue of Planar Graphs

## L0 — One line
For a planar graph with n vertices and maximum degree d, λ₂ ≤ 8d/n, proved by embedding the graph on a sphere as touching disks and using disjointness of the disks' areas.

## L1 — The gist (≤ 120 words)
Why does the second Laplacian eigenvector partition planar graphs and meshes well? The chapter proves that λ₂ of a planar graph is small, λ₂ ≤ 8d/n ([ST07]). Cheeger's inequality then gives a good cut. The proof writes λ₂ as a minimum over vector-valued embeddings. Koebe's theorem draws any planar graph as touching disks. Stereographic projection (which maps circles to circles) moves the disks to a sphere, where their areas sum to at most 4π and so bound the numerator. A topological argument (Brouwer's fixed-point theorem) is used to re-centre the sphere so that the embedding sums to zero; the text proves only a simplified version of this step.

**Prerequisites:** Laplacian quadratic form and λ₂ as a Rayleigh-quotient minimum; Cheeger's inequality (used, not proved); planar graphs; continuity; spheres in ℝ³.

## L2 — Key ideas (5–10 bullets)
- Main theorem: planar G, n vertices, max degree d ⇒ λ₂ ≤ 8d/n (p. 204). Cheeger's inequality then makes the λ₂ eigenvector give a good cut (p. 204).
- λ₂ is a minimum over mean-zero vector embeddings $v_i\in\mathbb R^d$. So any such embedding upper-bounds λ₂ (Lemma 25.2.1, p. 205).
- Koebe: every planar graph is the touching graph of interior-disjoint disks (p. 205). The disk centres give a natural embedding.
- Plain-plane disk embeddings can fail: nested triangles give ratio Θ(1) (p. 206). Lifting to the sphere by stereographic projection, which maps circles to circles, repairs this (p. 206).
- On the unit sphere every centre has norm 1, so the denominator is n. The numerator is at most $2d\sum r_i^2\le 8d$, because the caps are disjoint and have area $\pi r_i^2$ (p. 207).
- The remaining task is $\sum_i v_i=0$. Circle-preserving maps $f_\omega$, indexed by ω in the ball, give the freedom to achieve it (pp. 208–209).
- Brouwer's theorem gives Lemma 25.3.2. A continuous map of the ball that is the identity on the sphere hits 0 (p. 209).
- The text argues only for the simplified Theorem 25.3.1 (zero sum of the mapped points $f_\omega(v_i)$ for points $v_i$ on the sphere), and the step removing ε is only sketched. The version for cap centres is deferred to [ST07, Thm 4.2] (p. 210).

## L3 — Walkthrough

### 25.1 Overview
- Spectral partitioning of planar graphs and meshes was historically successful. The chapter explains this by showing λ₂ is small for planar graphs (p. 204).
- Model case: a √n-by-√n grid has λ₂ ≈ c/n. Cheeger then gives a cut of conductance c/√n. This is the cut across the middle of an axis, which has minimum conductance (p. 204).
- **Theorem 25.1.1 [ST07].** G planar, n vertices, maximum degree d: $\lambda_2\le 8d/n$ (p. 204). The proof uses almost no calculation, and it has been generalized to planar-like graphs, including well-shaped 3D meshes (p. 204).

### 25.2 Geometric embeddings
**Lemma 25.2.1.** For any $d\ge1$ (here d is the embedding dimension),
$$\lambda_2=\min_{v_1,\dots,v_n\in\mathbb R^d:\ \sum v_i=0}\frac{\sum_{(i,j)\in E}\|v_i-v_j\|^2}{\sum_i\|v_i\|^2}.\tag{25.1}$$
*Proof* (p. 205). Write $v_i=(x_i,y_i,\dots,z_i)$. Then numerator and denominator split by coordinate: $\sum_E\|v_i-v_j\|^2=\sum_E(x_i-x_j)^2+\sum_E(y_i-y_j)^2+\dots$ and $\sum_i\|v_i\|^2=\sum x_i^2+\sum y_i^2+\dots$.
- λ₂ ≥ RHS: take every coordinate equal to a λ₂-eigenvector.
- λ₂ ≤ RHS: use $\frac{A+B+\cdots+C}{A'+B'+\cdots+C'}\ge\min\left(\frac AA',\dots,\frac CC'\right)$. Each coordinate has $\sum x_i=0$, so its ratio is $\ge\lambda_2$.

*Intuition note.* Each coordinate of an embedding is a test vector. The ratio of sums is a weighted average of the per-coordinate ratios, so it cannot beat the best one. To prove λ₂ small, find one good embedding. Example given: the square with corners (±1,±1) (p. 205).

**Koebe (Thm 25.2.2).** For planar G=(V,E) there are interior-disjoint circles $C_1,\dots,C_n$ in ℝ² with $C_i$ touching $C_j$ iff $(i,j)\in E$ (p. 205). This is a *kissing disk embedding*. It is stated without proof (see Agarwal–Pach). Choose $v_i$ = centre of disk $C_i$, with radius $r_i$ (p. 205).
- Numerator: $\|v_i-v_j\|^2=(r_i+r_j)^2\le 2r_i^2+2r_j^2$ (p. 206).
- Bounding the denominator below is trickier. Some graphs, built from triangles inside triangles, give (25.1) = Θ(1) (p. 206).

**Fix: stereographic projection** (p. 206). Let a sphere S touch the plane at s, with n the opposite point. $\Pi(x)$ is where the line from x to n meets S. Π maps circles to circles. So $D_i=\Pi(C_i)$ gives a kissing disk embedding on the sphere. Let $v_i$ be the centre of $D_i$.

**Bound, assuming $\sum_i v_i=0$** (p. 207).
- $\|v_i\|=1$, so the denominator is n.
- Let $r_i$ be the straight-line distance from $v_i$ to the boundary of $D_i$. Then $\|v_i-v_j\|^2\le(r_i+r_j)^2\le2r_i^2+2r_j^2$.
- Archimedes: the cap bounded by $D_i$ has area exactly $\pi r_i^2$. The text does not prove it. It only argues that the claim must be true because it holds for small $r_i$, for the hemisphere ($r_i=\sqrt2$), and for the whole sphere ($r_i=2$).
- The caps are disjoint, so $\sum_i\pi r_i^2\le4\pi$.
- Each vertex lies in at most d edges (added step). Hence
$$\sum_{(a,b)\in E}\|v_a-v_b\|^2\le\sum_{(a,b)\in E}(2r_a^2+2r_b^2)\le2d\sum_a r_a^2\le 8d.$$
- So the min in (25.1) is at most $8d/n$ (p. 208).

*Intuition note.* The sphere has total area 4π, so the disks cannot all be large. Small disks mean short edges, which makes the numerator small. On the sphere every $v_i$ has norm 1, so the denominator is simply n, which avoids the plane's difficulty with the denominator (pp. 206–207).

It remains to ensure $\sum_i v_i=\mathbf 0$ (25.2). There is freedom to place the sphere anywhere on the plane and to scale the image first. This lets one put the centre of gravity close to any boundary point of the sphere. The author says this is enough to place it at the origin (p. 208).

### 25.3 The center of gravity
**Maps $f_\omega$** (p. 208). For ω in the open ball and α on the unit sphere, $\Pi_\alpha$ is the stereographic projection from the plane tangent at α. Set $\Pi_\alpha^{-1}(-\alpha)=\infty$ and $\Pi_\alpha(\infty)=-\alpha$. $D_\alpha^a$ dilates that tangent plane by a factor a. Define
$$f_\omega(x)\overset{\text{def}}{=}\Pi_{\omega/\|\omega\|}\Big(D_{\omega/\|\omega\|}^{\,1-\|\omega\|}\big(\Pi^{-1}_{\omega/\|\omega\|}(x)\big)\Big).$$
For ω = aα, this pushes the sphere towards α, and more strongly as a → 1 (p. 208).

**Theorem 25.3.1.** For points $v_1,\dots,v_n$ on the unit sphere, there is an ω with $\sum_i f_\omega(v_i)=\mathbf 0$ (p. 209). This is simpler than what is needed. A circle-preserving map need not send a circle's centre to the image circle's centre (p. 209).

**Lemma 25.3.2.** If $\phi:B\to B$ is continuous and the identity on S, then $\phi(\omega)=\mathbf 0$ for some ω ∈ B (p. 209). It follows from:

**Theorem 25.3.3 (Brouwer).** A continuous $g:B\to B$ has a fixed point (p. 209).

*Proof of the lemma* (p. 209). Let $b(z)=z/\|z\|$, continuous except at 0. Suppose 0 is not in the image of φ. Then $g=-b\circ\phi$ is continuous and maps B to B. The text says g has no fixed point, contradicting Brouwer. (Added step: g takes values on S, so a fixed point α would lie on S, where φ(α)=α. But then g(α)=−α≠α.)

**Applying it** (pp. 209–210). Set $\phi(\omega)=\frac1n\sum_i f_\omega(v_i)$. It is undefined on S. For α ∈ S, define $f_\alpha(z)=\alpha$ if z≠−α, and $-\alpha$ otherwise. This is discontinuous at $\alpha=-v_i$. The author says this should not be a problem because the ω with φ(ω)=0 won't be on or near the boundary; the following argument makes this formal. Introduce a cutoff, with $\epsilon>0$:
$$h_\omega(z)=\begin{cases}1&\text{if }\operatorname{dist}(\omega,z)<2-\epsilon,\\(2-\operatorname{dist}(\omega,z))/\epsilon&\text{otherwise.}\end{cases}$$
$f_\alpha(z)h_\alpha(z)$ is continuous on B. So
$$\phi(\omega)\overset{\text{def}}{=}\frac{\sum_if_\omega(v_i)h_\omega(v_i)}{\sum_ih_\omega(v_i)}$$
is continuous and the identity on S. For each ε, Lemma 25.3.2 gives ω with φ(ω)=0 (p. 210).

**Removing ε** (p. 210). The aim is to show that ω stays bounded away from S, by some μ, for all sufficiently small ε. If so, the text says dist(ω, $v_i$) ≥ μ > 0 for all sufficiently small ε, so for ε < μ and sufficiently small, $h_\omega(v_i)=1$ for all i, which recovers the ε=0 case. The text says one can verify the bounded-away claim provided the $v_i$ are distinct and there are at least 3 of them (see Reading notes on the step to $h=1$).

**Cap centres** (p. 210). The actual need is cap centres, not the points $v_i$. Centres move with ω, but they stay inside the caps and move continuously with ω. The full proof is in [ST07, Thm 4.2].

### 25.4 Further progress (p. 210)
Kelner extended the result to bounded-genus graphs. Kelner–Lee–Price–Teng gave analogous bounds for λ_k, k ≥ 2. Biswal–Lee–Rao used new techniques that improve the bounds and cover graphs with no $K_h$ minor, for any constant h.

## Toy example (ours)
The 4-cycle C₄ (planar, n=4, d=2). Its Laplacian eigenvalues are 0, 2, 2, 4, so λ₂=2.
- Embed $v_1=(1,1),v_2=(-1,1),v_3=(-1,-1),v_4=(1,-1)$. The sum is (0,0).
- Each of the 4 edges has $\|v_i-v_j\|^2=2^2+0=4$. Numerator = 16.
- Each $\|v_i\|^2=2$. Denominator = 8.
- Ratio = 16/8 = 2. By the lemma, λ₂ ≤ 2, and here equality holds.
- Coordinate check: x = (1,−1,−1,1) gives numerator 4+0+4+0=8 and $\sum x^2=4$, ratio 2. Same for y.
- Theorem bound: 8d/n = 16/4 = 4 ≥ 2.

## Concepts
- [[graph-laplacian]] — the Laplacian matrix of a graph (not defined on these pages); λ₂ is its second-smallest eigenvalue (p. 204)
- [[fiedler-vector-algebraic-connectivity]] — λ₂ and its eigenvector, used to cut planar graphs and meshes (p. 204)
- [[rayleigh-quotient]] — here in vector-valued form (25.1), the ratio of edge energy to norm for a mean-zero embedding (p. 205)
- [[cheeger-inequality]] (new) — used to turn small λ₂ into a low-conductance cut; not stated in this unit (p. 204)
- [[kissing-disk-embedding]] (new) — interior-disjoint disks whose touching graph is G (p. 205)
- [[koebe-embedding-theorem]] (new) — every planar graph has a kissing disk embedding (p. 205)
- [[stereographic-projection]] (new) — plane-to-sphere map via the line to the opposite point; maps circles to circles (p. 206)
- [[brouwer-fixed-point-theorem]] (new) — a continuous map of the ball into itself has a fixed point (p. 209)

## Canonical instances
- [[grid-graph]] — √n×√n grid with λ₂ ≈ c/n (p. 204)
- [[nested-triangles-graph]] — kissing disk embedding in the plane with ratio Θ(1) (p. 206)
- [[square-embedding]] — corners (±1,±1) as example embedding (p. 205)

## Bridges (candidates)
- [same-math] vector-valued Rayleigh quotient (25.1) ↔ Rayleigh quotient: coordinate-wise application of the λ₂ characterization.
- [structural-analogy] choosing ω so that $\sum f_\omega(v_i)=0$ ↔ PCA: centring data before optimising a variance-type ratio.
- [metaphor] disjoint caps share the sphere's total area 4π ↔ budget constraints: limited total "room" forces most elements to be small.

## Questions this raises
- Why does a sum-to-zero embedding of the cap centres exist, not just of the points $v_i$ (p. 210)?
- Why is ω bounded away from S when the $v_i$ are distinct and n ≥ 3 (p. 210)?
- Which parts of the argument (Koebe, area bound, re-centring) survive for bounded-genus or $K_h$-minor-free graphs (p. 210)?
- How tight is $8d/n$ compared with the grid's c/n?

## Reading notes
- Printed = pdf − 24. The chapter header reads "This Chapter Needs Editing". The work citation (not these pages) describes the book as an incomplete draft.
- The letter d means two things: embedding dimension in Lemma 25.2.1, maximum degree in Theorem 25.1.1 and in the bound.
- B is defined as points of norm less than 1, yet Lemma 25.3.2 says "identity on S". So B must include S there.
- On p. 210 the text says dist(ω, v_i) ≥ μ gives $h_\omega(v_i)=1$. By the definition of h, this needs dist(ω, v_i) < 2 − ε. This follows if ‖ω‖ ≤ 1 − μ (triangle inequality: dist ≤ 2 − μ). The printed inequality looks like a slip.
- Archimedes' cap-area fact and the removal of ε are sketched, not proved. Koebe's theorem is cited without proof.
