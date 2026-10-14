---
id: spielman-2025-sagt/ch20-graph
work: spielman-2025-sagt
unit: "Chapter 20 — Graph Partitioning"
pages: 171–175
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Graph Partitioning

## L0 — One line
The second-smallest eigenvalue of the Laplacian ($\lambda_2$), or of the normalized Laplacian ($\nu_2$), lower-bounds how cheaply any vertex set can be cut off, measured by isoperimetric ratio or conductance.

## L1 — The gist (≤ 120 words)
How can we measure whether a set of vertices is easy to separate from the rest of a graph? The chapter defines two measures: isoperimetric ratio (boundary edges per vertex in the set) and conductance (boundary weight per unit of weighted degree). Each is bounded below by an eigenvalue: $\theta_G \ge \lambda_2/2$ and $\phi_G \ge \nu_2/2$. Both proofs use the variational (min-quotient) characterisation of the eigenvalue, with a shifted indicator vector of $S$ as the test vector. A large $\lambda_2$ therefore means that every small set has a boundary that is large relative to its size. Chapter 21 gives an approximate converse (Cheeger's inequality).

**Prerequisites:** graph Laplacian $L=D-A$ and its quadratic form $\sum_{(a,b)\in E}(x_a-x_b)^2$; Rayleigh quotient and the min characterisation of eigenvalues; weighted degree; orthogonality.

## L2 — Key ideas
- The boundary $\partial(S)$ is the set of edges leaving $S$. The isoperimetric ratio $\theta(S)=|\partial(S)|/|S|$ compares it with the size of $S$ (p. 171).
- Theorem 20.1.1: $\theta(S)\ge\lambda_2(1-s)$ for every $S$, hence $\theta_G\ge\lambda_2/2$ (p. 172).
- The proof uses the indicator vector of $S$, shifted to be orthogonal to $\mathbf 1$, as a test vector in the Rayleigh quotient (p. 172).
- Conductance $\phi(S)$ handles weighted graphs and measures size by degree sum $d(S)$ (p. 173).
- The normalized Laplacian $N=D^{-1/2}LD^{-1/2}$ turns the generalized quotient $y^TLy/y^TDy$ into an ordinary Rayleigh quotient (p. 174).
- Lemma 20.3.1 and Corollary 20.3.2: $\nu_2\le d(V)\,w(\partial S)/(d(S)d(V-S))$, hence $\phi(S)\ge\nu_2/2$ (pp. 174–175).
- Definitions vary across authors, so check the formulas when reading (p. 175).

## L3 — Walkthrough

### 20.1 Isoperimetry and $\lambda_2$ (pp. 171–173)
Definitions, for an unweighted graph and vertex set $S$ (p. 171):
$$\partial(S)\overset{def}{=}\{(a,b)\in E: a\in S,\ b\notin S\},\qquad \theta(S)\overset{def}{=}\frac{|\partial(S)|}{|S|},\qquad \theta_G\overset{def}{=}\min_{|S|\le n/2}\theta(S).$$

The author says an approximate converse of the lower bound derived next, known as Cheeger's Inequality, will be presented in Chapter 21 (p. 171).

**Theorem 20.1.1.** For every $S\subset V$, $\theta(S)\ge\lambda_2(1-s)$ with $s=|S|/|V|$. In particular $\theta_G\ge\lambda_2/2$ (p. 172).

Proof steps (p. 172):
1. Since $\lambda_2=\min_{x:x^T\mathbf 1=0}\frac{x^TL_Gx}{x^Tx}$, every non-zero $x\perp\mathbf 1$ has $x^TL_Gx\ge\lambda_2x^Tx$.
2. Let $\mathbf 1_S$ be the indicator of $S$. Then $\mathbf 1_S^TL_G\mathbf 1_S=\sum_{(a,b)\in E}(\mathbf 1_S(a)-\mathbf 1_S(b))^2=|\partial(S)|$.
3. $\mathbf 1_S$ is not orthogonal to $\mathbf 1$, so take $x=\mathbf 1_S-s\mathbf 1$. Then $x(a)=1-s$ on $S$ and $-s$ elsewhere, and $x^T\mathbf 1=0$.
4. The shift cancels in differences: $x^TL_Gx=\sum_{(a,b)\in E}((\mathbf 1_S(a)-s)-(\mathbf 1_S(b)-s))^2=|\partial(S)|$.
5. By Claim 19.3.3 (not in this unit), $x^Tx=n(s-s^2)$.
6. Hence $\lambda_2\le \frac{x^TL_Gx}{x^Tx}=\frac{|\partial(S)|}{|S|(1-s)}$. (added step: $n(s-s^2)=ns(1-s)=|S|(1-s)$.) This gives $\theta(S)\ge\lambda_2(1-s)$.
7. (added step) If $|S|\le n/2$ then $1-s\ge 1/2$, which gives $\theta_G\ge\lambda_2/2$.

**Intuition note.** A set with few boundary edges (relative to its size) gives a test vector whose quotient is small. Every such quotient is at least $\lambda_2$, so a big $\lambda_2$ rules that out.

The author says: if $\lambda_2$ is big, $G$ is very well connected, because every small set has boundary at least $\lambda_2$ times slightly less than $|S|$ (p. 173). Rearranged (p. 173):
$$\frac{\theta(S)}{1-s}=|V|\frac{|\partial(S)|}{|S||V-S|}\ge\lambda_2 .$$
The author sometimes favors the middle quantity over the isoperimetric ratio because $|\partial(S)|/(|S||V-S|)$ removes the need to restrict $|S|\le|V|/2$ (p. 173).

### 20.2 Conductance (p. 173)
For weighted graphs: $d(S)$ is the sum of degrees in $S$, $d(V)$ is twice the total edge weight, and $w(F)$ is the total weight of an edge set $F$.
$$\phi(S)\overset{def}{=}\frac{w(\partial(S))}{\min(d(S),d(V-S))},\qquad \phi_G\overset{def}{=}\min_{S\subset V}\phi(S).$$
The author notes that other definitions exist, e.g. $d(V)\,w(\partial S)/(d(S)d(V-S))$, used in (20.3). In the author's experience, conductance is more useful when concerned about edges, and isoperimetric ratio when concerned about vertices. Conductance is particularly useful for random walks (p. 173).

### 20.3 The normalized Laplacian (pp. 173–175)
Since $\frac{\mathbf 1_S^TL\mathbf 1_S}{\mathbf 1_S^TD\mathbf 1_S}=\frac{w(\partial S)}{d(S)}$, the author considers the generalized Rayleigh quotient $\frac{y^TLy}{y^TDy}$ (20.1) (pp. 173–174).

Substituting $D^{1/2}y=x$ gives $\frac{x^TD^{-1/2}LD^{-1/2}x}{x^Tx}$, an ordinary Rayleigh quotient. Define $N\overset{def}{=}D^{-1/2}LD^{-1/2}$ with eigenvalues $0=\nu_1\le\nu_2\le\dots\le\nu_n$. From Section 10.5 (not in this unit): $\nu_2=\min_{y\perp d}\frac{y^TLy}{y^TDy}$, where $d$ is the degree vector. The author states $\nu_2/2\le\phi_G$ (20.2), saying the conductance is related to $\nu_2$ as the isoperimetric ratio is related to $\lambda_2$ (p. 174). Lemma 20.3.1 and Corollary 20.3.2 below give the set-wise bounds.

**Lemma 20.3.1.** For every $S\subset V$, $\nu_2\le d(V)\frac{w(\partial S)}{d(S)d(V-S)}$ (p. 174).

Proof (pp. 174–175):
1. Set $y=\mathbf 1_S-\sigma\mathbf 1$ with $\sigma=d(S)/d(V)$.
2. Check $y^Td=\mathbf 1_S^Td-\sigma\mathbf 1^Td=d(S)-(d(S)/d(V))\,d(V)=0$.
3. As before, $y^TLy=w(\partial S)$.
4. Denominator:
$$\begin{aligned}y^TDy&=\sum_{u\in S}d(u)(1-\sigma)^2+\sum_{u\notin S}d(u)\sigma^2\\&=d(S)(1-\sigma)^2+d(V-S)\sigma^2\\&=d(S)-2d(S)\sigma+d(V)\sigma^2\\&=d(S)-d(S)\sigma\quad(\text{as }d(S)=d(V)\sigma)\\&=d(S)d(V-S)/d(V).\end{aligned}$$
5. Therefore
$$\nu_2\le\frac{y^TLy}{y^TDy}=d(V)\frac{w(\partial S)}{d(S)d(V-S)}\tag{20.3}$$

**Corollary 20.3.2.** For every $S\subset V$, $\phi(S)\ge\nu_2/2$ (p. 175).
Proof: the larger of $d(S),d(V-S)$ is at least $d(V)/2$, so $\nu_2\le2\,w(\partial S)/\min(d(S),d(V-S))$. (added step: $d(S)d(V-S)=\min\cdot\max\ge\min\cdot d(V)/2$.)

**Intuition note.** The same trick works as in 20.1: shift the indicator so it is orthogonal to the constraint vector. Degree weights replace vertex counts, and $N$ rescales so the weighted problem becomes the ordinary one.

### 20.4 Notes (p. 175)
Definitions vary. Expansion often means boundary vertices over internal vertices. Cut ratio is sometimes used for isoperimetric ratio. Authors are inconsistent, so check the formulas.

## Toy example (ours)
4-cycle $C_4$, vertices 1–2–3–4–1, all weights 1. $L$ has eigenvalues $0,2,2,4$, so $\lambda_2=2$. Take $S=\{1,2\}$.
- $\partial(S)=\{(2,3),(1,4)\}$, so $|\partial S|=2$. $\theta(S)=2/2=1$. $s=1/2$, so $\lambda_2(1-s)=1$. The bound holds with equality.
- Test vector $x=\mathbf 1_S-\tfrac12\mathbf 1=(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12)$. Edge differences squared: $0,1,0,1$, so $x^TLx=2$. $x^Tx=1$. The quotient is $2=\lambda_2$.
- Conductance: $d(v)=2$, $d(S)=4=d(V-S)$, $d(V)=8$. $\phi(S)=2/4=0.5$. $N=L/2$, so $\nu_2=1$ and $\nu_2/2=0.5$. This is also equality.
- Check (20.3): $d(V)\,w/(d(S)d(V-S))=8\cdot2/16=1=\nu_2$.

## Concepts
- [[graph-laplacian]] — $x^TLx$ sums squared differences over edges (p. 172); $L=D-A$ is the standard definition, not restated on these pages
- [[rayleigh-quotient]] — $x^TLx/x^Tx$; its minimum over $x\perp\mathbf 1$ is $\lambda_2$ (p. 172)
- [[isoperimetric-ratio]] (new) — $\theta(S)=|\partial S|/|S|$; $\theta_G$ minimises over $|S|\le n/2$ (p. 171)
- [[conductance]] (new) — $\phi(S)=w(\partial S)/\min(d(S),d(V-S))$ (p. 173)
- [[normalized-laplacian]] (new) — $N=D^{-1/2}LD^{-1/2}$, eigenvalues $\nu_i$ (p. 174)
- [[cheeger-inequality]] (new) — approximate converse of the bound; only mentioned here (p. 171)

## Canonical instances
- [[shifted-indicator-test-vector]] (new) — $\mathbf 1_S$ minus a constant, used to bound an eigenvalue (pp. 172, 174)

## Bridges (candidates)
- [structural-analogy] $\lambda_2$ bounds cut quality ↔ community detection: spectral bisection with the Fiedler vector — both use the same eigenvalue to measure how separable a network is.
- [metaphor] Conductance ↔ random walks: a low-conductance set traps a walker for a long time. The text only says conductance is useful for random walks (p. 173).

## Questions this raises
- How close to $\theta_G$ is $\lambda_2$? (Chapter 21, Cheeger, is the stated answer, p. 171.)
- Which sets achieve equality in Theorem 20.1.1 beyond the toy $C_4$?
- When should one prefer $N$ over $L$ for networks with very uneven degrees (p. 174)?

## Reading notes
- Printed = pdf − 24.
- Page 172 proof, last display: the text and image print $\frac{\mathbf 1_S^TL_G\mathbf 1_S}{\mathbf 1_S^T\mathbf 1_S}$ as the middle term. The value $|\partial(S)|/(|S|(1-s))$ is the quotient for $x=\mathbf 1_S-s\mathbf 1$, i.e. $x^TL_Gx/x^Tx$. With $\mathbf 1_S$ itself the quotient would be $|\partial S|/|S|$. I wrote it with $x$.
- Page 172 also has one stray "$\chi_S$" for $\mathbf 1_S$.
- The proof of Corollary 20.3.2 gives the reason (the larger of $d(S),d(V-S)$ is at least $d(V)/2$) but not the algebra of the step $d(V)/(d(S)d(V-S))\le 2/\min(d(S),d(V-S))$. I added it as a marked step. (20.2) itself is stated on p. 174 without a separate proof.
- Claim 19.3.3 and Section 10.5 are cited but not included.
