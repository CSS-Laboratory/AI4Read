---
id: spielman-2025-sagt/ch37-augmented
work: spielman-2025-sagt
unit: "Chapter 37 — Augmented Spanning Tree Preconditioners"
pages: 295-299
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Augmented Spanning Tree Preconditioners

## L0 — One line
Scale up a low-stretch spanning tree, sample the other edges, and eliminate degree 1 and 2 vertices; recursing on the smaller graph gives a Laplacian solver for constant accuracy in time $\widetilde O(m\log^2 n)$.

## L1 — The gist (≤ 120 words)
The question is how to solve Laplacian systems $L_Gx=b$ in nearly linear time. A good preconditioner $H$ has far fewer edges than $G$, and solves in $H$ can be done recursively. Koutis–Miller–Peng multiply the weights of a low-stretch spanning tree $T$ by $s$, getting $\widetilde G$. They then sample off-tree edges with probability based on stretch, which bounds effective resistance. The condition number grows by a factor of at most about $s$. Taking $s\ge c(\sigma\ln n)^2$ makes the number of off-tree edges shrink by a factor of at least $c\sigma\ln n$ per level. The total time is $\widetilde O(m\log^2 n)$ for constant accuracy. The section "Saving a log" is empty in this draft.

**Prerequisites:** Laplacian $L_G$ and the order $\preceq$; relative condition number $\kappa(A,B)$; effective resistance and Rayleigh monotonicity; spanning-tree stretch; Schur complement (elimination of vertices); preconditioned iteration and iterative refinement.

## L2 — Key ideas
- Eliminating degree 1 and 2 vertices gives $U^T\mathrm{diag}(I,L_{\widetilde H})U=L_H$. $U$ has at most $2n$ nonzeros, so solves in $U$ and $U^T$ cost $O(n)$ (p. 296).
- A recursive approximate solver is a linear operator $Z$ with $(1-\epsilon)Z^+\preceq L_{\widetilde H}\preceq(1+\epsilon)Z^+$. Using it costs only a factor $(1+\epsilon)/(1-\epsilon)$ in condition number (p. 296).
- A tree has more than half its vertices of degree 1 or 2. If a tree plus $k$ edges has its degree 1 and 2 tree vertices that avoid the extra edges eliminated until none remain, at most $4k$ vertices and $5k$ edges are left (pp. 296–297).
- Stretch bounds effective resistance, $\mathrm{Reff}_G\le\mathrm{Stretch}_T$, by Rayleigh monotonicity. Sampling by stretch is cheap, but it keeps too many edges (p. 297).
- Fix: multiply the tree weights by $s$. This divides the resistance bound by $s$, so sampling keeps about $1/s$ as many off-tree edges. The price is $\kappa(L_G,L_{\widetilde G})\le s$ (p. 298).
- Balancing $s^{1/2}$ solves in $H$ against the cost of one multiply by $G$ requires $s\ge c(\sigma\ln n)^2$ (p. 298).
- Recursion keeps $o_{i+1}\le o_i/(c\sigma\ln n)$, where $o_i$ counts off-tree edges. Induction gives solve time $O(o_i\sigma\ln n)$ (p. 299).

## L3 — Walkthrough

**Intro (p. 295).** Augmented spanning tree preconditioners are spanning trees with edges of $G$ added back. Vaidya suggested maximum spanning trees. Spielman–Teng augmented low-stretch trees. This chapter presents the Koutis–Miller–Peng algorithm, which the intro says solves to accuracy $\epsilon$ in time $\widetilde O(m\log n\log\epsilon^{-1})$. By Iterative Refinement (previous chapter), any constant $\epsilon<1$ suffices. $\widetilde O$ hides low-order logarithmic factors. Constants $c$ change from line to line.

**37.1 Recursion (pp. 295–297).**
- Let $H$ be a spanning tree $T$ of $G$ plus a few edges. Many of its vertices have degree 1 or 2. Eliminating them gives a Schur complement $\widetilde H$ and an upper triangular $U$ (p. 296):
$$U^T\begin{pmatrix}I&0\\0&L_{\widetilde H}\end{pmatrix}U=L_H.$$
- Eliminating a degree 1 vertex only lowers its neighbour's degree. Eliminating a degree 2 vertex changes no neighbour's degree. So $U$ has at most $2n$ nonzeros and triangular solves take $O(n)$ (p. 296).
- The recursive solver is not exact. It acts as multiplication by a matrix $Z$ that is never built, with $(1-\epsilon)Z^+\preceq L_{\widetilde H}\preceq(1+\epsilon)Z^+$ (p. 296). Conjugating by $U$:
$$(1-\epsilon)U^T\begin{pmatrix}I&0\\0&Z^+\end{pmatrix}U\preceq U^T\begin{pmatrix}I&0\\0&L_{\widetilde H}\end{pmatrix}U\preceq(1+\epsilon)U^T\begin{pmatrix}I&0\\0&Z^+\end{pmatrix}U.$$
- So an $\epsilon$-approximate solve in $L_H$ uses a solve in $U$, an application of $Z$, and a solve in $U^T$ (p. 296). With $M=U^T\mathrm{diag}(I,Z^+)U$, the text says $\kappa(L_G,M)\le\frac{1+\epsilon}{1-\epsilon}\kappa(L_G,L_H)$ (p. 296).
- **Lemma 37.1.1.** In a tree on $n$ vertices, more than half the vertices have degree 1 or 2. Proof: the average degree is below 2, so there is at least one degree 1 vertex per vertex of degree $\ge3$. The rest have degree 2 (p. 296).
- **Lemma 37.1.2.** Let $H$ be a tree plus $k$ edges. Eliminate degree 1 or 2 tree vertices not touching the extra edges until none remain. Then at most $4k$ vertices and $5k$ edges are left (p. 297). Proof: each such elimination leaves a tree on one fewer vertex plus the same $k$ edges. A tree on $4k$ vertices has at least $2k+1$ vertices of degree 1 or 2. At least one of them does not touch an extra edge (added step: $k$ edges have at most $2k$ endpoints), so elimination can continue (p. 297).

*Intuition note.* Trees are almost "free" to solve, because leaves and path vertices can be peeled off cheaply. Few extra edges leave only a small core, and the recursion works on that core.

**37.2 Heavy Trees (pp. 297–299).**
- $H$ does not necessarily have to look like a tree plus a few edges; all that is really needed is that it has many fewer edges than $G$. The approach is the random sampling of Chapter 32, with effective resistances replaced by stretches. This gives a worse approximation but is cheaper (p. 297).
- **Theorem 37.2.1.** Let $p_{a,b}\in(0,1]$ satisfy $p_{a,b}\ge\min\!\big(1,\tfrac{4\ln n}{\epsilon^2}w_{a,b}\mathrm{Reff}_G(a,b)\big)$. Keep each edge independently with probability $p_{a,b}$ and weight $w_{a,b}/p_{a,b}$. Then, for some constant $c$ and with probability at least $1-n^{-c}$, $H$ is an $\epsilon$-approximation of $G$ and has at most $2\sum p_{a,b}$ edges (p. 297).
- **Lemma 37.2.2.** $\mathrm{Reff}_G(a,b)\le\mathrm{Stretch}_T(a,b)$. Proof: $\mathrm{Reff}_G\le\mathrm{Reff}_T$ by Rayleigh monotonicity, and $\mathrm{Reff}_T=\mathrm{Stretch}_T$ (p. 297).
- Sampling by stretch keeps too many edges. Define $\widetilde G=G+(s-1)T$, so tree edges have weight multiplied by $s$. For off-tree $(a,b)$ (p. 298):
$$\mathrm{Reff}_{\widetilde G}(a,b)\le\mathrm{Reff}_{sT}(a,b)\le(1/s)\mathrm{Stretch}_T(a,b).$$
- Set $p_{a,b}=1$ on $T$. Off $T$, set $p_{a,b}\ge\min\!\big(1,\tfrac{4\ln n}{s\epsilon^2}w_{a,b}\mathrm{Stretch}_T(a,b)\big)$ (p. 298).
- Let $\sigma=(1/m)\sum_{(a,b)\in E}w_{a,b}\mathrm{Stretch}_T(a,b)$, with $\sigma\le\widetilde O(\log n)$ for a low-stretch tree (p. 298). Whp $H$ is an $\epsilon$-approximation of $\widetilde G$. Its off-tree edges number at most
$$\sum_{(a,b)\notin T}p_{a,b}\le\frac{4m\sigma\ln n}{s\epsilon^2}.$$
- So taking $s$ a little more than a constant times $\sigma\ln n$ makes $H$ have fewer off-tree edges than $G$ (p. 298).
- **Claim 37.2.3.** $\kappa(L_G,L_H)\le\kappa(L_G,L_{\widetilde G})\,\kappa(L_{\widetilde G},L_H)$. Also $\kappa(L_G,L_{\widetilde G})\le s$. Hence $\kappa(L_G,L_H)\le s(1+\epsilon)/(1-\epsilon)$. A constant times $\kappa^{1/2}$ solves in $L_H$ give $\epsilon$-accurate solves in $L_G$, so about $s^{1/2}$ solves for constant $\epsilon$ (p. 298).
- To make a solve in $H$ cost less than a multiply by $G$, require $s^{1/2}\frac{4m\sigma\ln n}{s\epsilon^2}\le m$. This needs $s\ge c(\sigma\ln n)^2$. The text then claims time $\widetilde O(m\log^2 n)$ for constant accuracy (p. 298).

*Intuition note.* A heavy tree lowers the resistance bound of every off-tree edge by a factor $s$, so fewer of them need to be kept. Heaviness costs at most a factor $s$ in condition number. Since the number of solves in $H$ is a constant times $\sqrt\kappa$, this is only about $s^{1/2}$ solves.

**The recursion (p. 299).**
- Let $G_0=G$ and $o_i=m_i-(n_i-1)$ (off-tree edges). Assume $G_0$ has no degree 1 or 2 vertices, so $o_0\ge n_0$ (p. 299).
- Form $\widetilde G_i$ and sample $H_i$. $H_i$ has at most a $1/(c\sigma\ln n)$ fraction of the off-tree edges of $G_i$ (p. 299).
- If $H_i$ has fewer than $n_i/4$ off-tree edges, eliminate degree 1 and 2 vertices and let $G_{i+1}$ be the result; the text states "at most $4n_i$ vertices and $5n_i$ edges" (see Reading notes). Otherwise $G_{i+1}=H_i$. Either way $o_{i+1}\le o_i/(c\sigma\ln n)$ (p. 299).
- Claim, by backwards induction: solving in $L_{G_i}$ takes time $O(o_i\sigma\ln n)$. A solve needs $O(s^{1/2})$ solves in $G_{i+1}$ and as many multiplies by $L_{G_i}$. The text writes the total as $O(s^{1/2}(o_i+o_{i-1}\sigma\ln n))\le O(s^{1/2}(2o_i))\le O(o_i\sigma\ln n)$ (p. 299). The last step needs $s^{1/2}=O(\sigma\ln n)$ (added step).

**37.3 Saving a log (p. 299).** Heading only; no text in this draft.

## Toy example (ours)
Take the 4-cycle $a\!-\!b\!-\!c\!-\!d\!-\!a$ with unit weights. Let $T$ be the path $a\!-\!b\!-\!c\!-\!d$, and the off-tree edge be $(d,a)$.
- $\mathrm{Reff}_T(d,a)=1+1+1=3$, so $\mathrm{Stretch}_T(d,a)=3$.
- $\mathrm{Reff}_G(d,a)$ is 1 in parallel with 3: $\frac{1\cdot3}{1+3}=\frac34\le3$. This is Lemma 37.2.2.
- Take $s=4$. Tree edges get weight 4, so the path has resistance $3/4$. Then $\mathrm{Reff}_{\widetilde G}(d,a)=\frac{(3/4)(1)}{3/4+1}=\frac37\approx0.43$. The bound is $\mathrm{Reff}_{sT}=3/4=(1/4)\cdot3$, and $\frac37\le\frac34$.
- The resistance bound for the off-tree edge shrank from 3 to $3/4$, so its sampling probability can be about 4 times smaller.
- Condition number (added step): $L_{\widetilde G}=L_G+3L_T\succeq L_G$. Since $L_T\preceq L_G$, also $L_{\widetilde G}\preceq4L_G$. So $\kappa(L_G,L_{\widetilde G})\le4=s$.

## Concepts
- [[condition-number]] — here the relative $\kappa(L_G,L_H)$; it is submultiplicative across a chain of approximations, $\kappa(L_G,L_H)\le\kappa(L_G,L_{\widetilde G})\kappa(L_{\widetilde G},L_H)$ (p. 298)
- [[graph-laplacian]] — $L_G$; the matrix of the systems being solved (p. 295)
- [[spanning-tree-preconditioner]] (new) — a spanning tree plus added edges, used as the preconditioner $H$ (p. 295)
- [[stretch-of-tree-edge]] (new) — $\mathrm{Stretch}_T(a,b)=\mathrm{Reff}_T(a,b)$ as used here; it upper-bounds $\mathrm{Reff}_G$ (p. 297)
- [[effective-resistance]] (new) — resistance between $a$ and $b$ in $G$; controls sampling probabilities (p. 297)
- [[schur-complement-elimination]] (new) — eliminating degree 1 and 2 vertices to leave $L_{\widetilde H}$ (p. 296)
- [[sparsification-by-sampling]] (new) — keep edges with probability $p_{a,b}$ and reweight by $1/p_{a,b}$ (p. 297)
- [[heavy-tree-scaling]] (new) — $\widetilde G=G+(s-1)T$ (p. 297)

## Canonical instances
- [[kmp-recursive-solver]] (new) — the Koutis–Miller–Peng recursive solver, with the $o_i$ recursion (pp. 298–299)

## Bridges (candidates)
- [same-math] Elimination with Schur complement ↔ Gaussian elimination / sparse Cholesky: eliminating vertices leaves the Schur complement.
- [structural-analogy] Heavy tree $\widetilde G$ ↔ preconditioned iteration: trading a larger $\kappa$ (factor $s$) for a sparser system, with iterations scaling as $\sqrt\kappa$.
- [structural-analogy] Stretch bounds $\mathrm{Reff}$ ↔ electrical networks: adding resistors in parallel only lowers resistance (Rayleigh monotonicity).

## Questions this raises
- How does "Saving a log" reduce $\widetilde O(m\log^2n)$ toward the intro's $\widetilde O(m\log n\log\epsilon^{-1})$?
- Why does the recursion need $G_0$ to have no degree 1 or 2 vertices?
- Where does the $1/s^{1/2}$ balance come from, and could another trade-off between $s$ and the iteration count do better?

## Reading notes
- Printed = pdf − 24. The chapter opens with the note "This Chapter Needs Editing", and the draft is incomplete.
- §37.3 "Saving a log" has a heading and no text. The intro's bound $\widetilde O(m\log n\log\epsilon^{-1})$ is not derived here; the unit derives $\widetilde O(m\log^2n)$ (p. 298).
- Probable misprint (p. 299): the image reads "at most $4n_i$ vertices and $5n_i$ edges" for fewer than $n_i/4$ off-tree edges. Lemma 37.1.2 with $k<n_i/4$ would give at most $n_i$ vertices and $5n_i/4$ edges.
- Probable misprint (p. 299): the induction line shows $o_{i-1}$. The argument seems to need $o_{i+1}$, the next level.
- The text layer drops $\epsilon$ in several formulas (for example the $p_{a,b}$ bounds on pp. 297–298); the images show $\epsilon^2$ on p. 297 and $s\epsilon^2$ on p. 298.
- On p. 298 the page itself prints "(a, b)inT" (the symbol $\in$ is missing); it is read here as $(a,b)\in T$.
- Footnote 1 (p. 296): $U$ is upper triangular after suitable vertex ordering.
