---
id: spielman-2025-sagt/ch27-properties
work: spielman-2025-sagt
unit: "Chapter 27 — Properties of Expander Graphs"
pages: 219-227
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
# Properties of Expander Graphs

## L0 — One line
A d-regular graph whose nontrivial adjacency eigenvalues are all at most εd in absolute value approximates the complete graph; this forces random-like edge counts and strong neighbour growth, and, for fixed d and large n, ε cannot be much below 2√(d−1)/d.

## L1 — The gist (≤ 120 words)
The chapter asks what it means for a regular graph to be a good expander (all non-trivial adjacency eigenvalues small), what that implies, and how good it can be. It shows that this condition is the same as approximating the complete graph in the Laplacian order. It derives two consequences: edge counts between any two vertex sets are close to those of a random graph, and small sets have many neighbours (Tanner's theorem). A test-vector argument bounds λ₂ from above, so, for fixed d and growing n, ε cannot be much smaller than the value achieved by Ramanujan graphs. It matters because it links eigenvalues to combinatorial behaviour. Open problems are listed at the end.

**Prerequisites:** graph Laplacian and its quadratic form; Rayleigh quotient; operator norm; the order H ≼ G on Laplacians; characteristic vectors of vertex sets.

## L2 — Key ideas
- ε-expander: d-regular (μᵢ = adjacency eigenvalues; the eigenvalue d is excluded) with |μᵢ| ≤ εd for i ≥ 2, equivalently ‖L_G − (d/n)L_{K_n}‖ ≤ εd (p. 220).
- ε-approximation means (1−ε)H ≼ G ≼ (1+ε)H. This definition is not symmetric (p. 220).
- Quasi-randomness (α=|S|/n, β=|T|/n): for all S, T, |E⃗(S,T)| is within εdn√((α−α²)(β−β²)) of the random-graph value αβdn (Thm 27.3.1, p. 221).
- Tanner's theorem (N(S) = set of neighbours of S) follows from this: |N(S)| ≥ |S|/(ε²(1−α)+α) (p. 223).
- A single vertex already forces ε to be roughly at least 1/√d (p. 223).
- Nilli's test vector (neighbourhood layers around two edges at distance ≥ 2k+2) gives, for the second Laplacian eigenvalue, λ₂ ≤ d − 2√(d−1) + (2√(d−1)−1)/(k+1) (Thm 27.5.1, p. 224).
- Ramanujan graphs (constructed by Margulis and by Lubotzky–Phillips–Sarnak) achieve ε ≤ 2√(d−1)/d; for fixed d, ε cannot be asymptotically smaller than this (pp. 219, 224).
- The analogous bound for λₙ was asserted falsely earlier, and irregular graphs are open (p. 227).

## L3 — Walkthrough

### 27.1 Overview (p. 219)
A d-regular graph is a good expander if all adjacency eigenvalues other than d are small, with absolute value at most εd. The chapter shows four things: equivalence to approximating $K_n$; random-like edge counts; Tanner's theorem; and the Alon–Boppana bound, which makes Ramanujan graphs asymptotically best.

### 27.2 Expanders as approximations of the complete graph (pp. 219–220)
- The operator norm (the default here) is $\|M\|=\max_x \|Mx\|/\|x\|$, the largest singular value. For symmetric $M$ it is the largest absolute eigenvalue (p. 220).
- **ε-expander:** d-regular with $|\mu_i|\le\epsilon d$ for $i\ge2$. Since $\lambda_i=d-\mu_i$, this is equivalent to $|d-\lambda_i|\le\epsilon d$, and to $\|L_G-(d/n)L_{K_n}\|\le\epsilon d$ (p. 220).
- **ε-approximation:** $(1-\epsilon)H\preceq G\preceq(1+\epsilon)H$, where $H\preceq G$ means $x^TL_Hx\le x^TL_Gx$ for all $x$. The author warns it is not symmetric. For a symmetric version he usually uses $(1+\epsilon)^{-1}H\preceq G$ (p. 220).
- For an ε-expander and $x\perp\mathbf 1$: $(1-\epsilon)d\,x^Tx\le x^TL_Gx\le(1+\epsilon)d\,x^Tx$. For $K_n$, $x^TL_{K_n}x=n\,x^Tx$. With $H=\frac dnK_n$ we get $x^TL_Hx=d\,x^Tx$, so $G$ ε-approximates $H$ (p. 220).
- From $(1-\epsilon)L_H\preceq L_G\preceq(1+\epsilon)L_H$ we get $-\epsilon L_H\preceq L_G-L_H\preceq\epsilon L_H$. Both matrices are symmetric and $L_H$ has eigenvalues 0 or $d$, so
$$\|L_G-L_H\|\le\epsilon d.\tag{27.1}$$

*Intuition note:* "All non-trivial eigenvalues near d" says the Laplacian of G looks like a scaled complete graph on every direction except the constant one. The three definitions are the same condition in different language.

### 27.3 Quasi-random properties (pp. 221–222)
- Random sets: put each vertex in S with probability α and in T with probability β. A fraction αβ of ordered edge pairs is expected to have u∈S, v∈T. Define $\vec E(S,T)=\{(u,v):u\in S,v\in T,(u,v)\in E\}$. For disjoint S, T, $|\vec E(S,T)|$ is the number of edges between them. $|\vec E(S,S)|$ counts each inside edge twice (p. 221).
- **Theorem 27.3.1** (Alon–Chung bound, slightly extended by Beigel–Margulis–Spielman). If $G$ is d-regular and ε-approximates $\frac dnK_n$, then for all $S,T$ with $|S|=\alpha n$, $|T|=\beta n$:
$$\Big|\,|\vec E(S,T)|-\alpha\beta dn\Big|\le\epsilon dn\sqrt{(\alpha-\alpha^2)(\beta-\beta^2)}.$$
When α, β > ε the right side is less than αβdn (p. 221).
- **Proof** (p. 222):
  1. $\chi_S^TL_G\chi_T=d|S\cap T|-|\vec E(S,T)|$ (p. 221).
  2. With $H=\frac dnK_n$: $\chi_S^TL_H\chi_T=\chi_S^T(dI-\frac dnJ)\chi_T=d|S\cap T|-\frac dn|S||T|=d|S\cap T|-\alpha\beta dn$.
  3. Hence $\big||\vec E(S,T)|-\alpha\beta dn\big|=|\chi_S^TL_G\chi_T-\chi_S^TL_H\chi_T|$.
  4. $\chi_S^T(L_H-L_G)\chi_T\le\|\chi_S\|\,\|L_H-L_G\|\,\|\chi_T\|\le\epsilon d\|\chi_S\|\|\chi_T\|=\epsilon dn\sqrt{\alpha\beta}$.
  5. Improvement: $L_Hx=L_H(x+c\mathbf 1)$. Let $x_S,x_T$ be $\chi_S,\chi_T$ orthogonalized against constants. Then $x_S^T(L_H-L_G)x_T=\chi_S^T(L_H-L_G)\chi_T$, and $\|x_S\|\|x_T\|=n\sqrt{(\alpha-\alpha^2)(\beta-\beta^2)}$ (Claim 2.4.2). This gives the theorem.
- For disjoint S, T the same proof works for irregular weighted graphs that ε-approximate $\frac dnK_n$, using $w(S,T)=\sum_{(u,v)\in E,u\in S,v\in T}w(u,v)$ (p. 222).

*Intuition note:* The quadratic form of $L_G-L_H$ is small on every pair of vectors. Set indicator vectors are such vectors, so no pair of sets can have an edge count far from the random value.

### 27.4 Vertex expansion (pp. 222–223)
- **Theorem 27.4.1 (Tanner).** Under the same hypothesis, $|N(S)|\ge\dfrac{|S|}{\epsilon^2(1-\alpha)+\alpha}$ where $|S|=\alpha n$. For α much less than ε², the right side is about $|S|/\epsilon^2$ (p. 223).
- **Proof:**
  1. Let $R=N(S)$, $T=V-R$, $|T|=\beta n$, $|R|=\gamma n$, $\gamma=1-\beta$. No edges join S and T, so Thm 27.3.1 gives $\alpha\beta dn\le\epsilon dn\sqrt{(\alpha-\alpha^2)(\beta-\beta^2)}$.
  2. Divide by $dn$ and square: $\alpha^2\beta^2\le\epsilon^2(\alpha-\alpha^2)(\beta-\beta^2)$.
  3. This is equivalent to $\alpha\beta\le\epsilon^2(1-\alpha)(1-\beta)$.
  4. Then $\frac\beta{1-\beta}\le\frac{\epsilon^2(1-\alpha)}\alpha$, i.e. $\frac{1-\gamma}\gamma\le\frac{\epsilon^2(1-\alpha)}\alpha$.
  5. Then $\frac1\gamma\le\frac{\epsilon^2(1-\alpha)+\alpha}\alpha$, so $\gamma\ge\frac\alpha{\epsilon^2(1-\alpha)+\alpha}$.
- Using $N(S)-S$ instead gives disjoint S, T, so the argument works for weighted irregular graphs (p. 223).

*Intuition note:* If a set had few neighbours, the complement of its neighbourhood would be a large set with zero edges to S. Theorem 27.3.1 limits how large such a zero-edge pair of sets can be, which gives the bound on $|N(S)|$.

### 27.5 How well can a graph approximate $K_n$? (pp. 223–226)
- Tanner with $S=\{v\}$ (v has exactly d neighbours) gives $\epsilon^2(1-1/n)+1/n\ge1/d$. The author concludes ε is at least $1/\sqrt{d(n-1)/n}$, "essentially" $1/\sqrt d$ (p. 223).
- Ramanujan graphs (Margulis; Lubotzky–Phillips–Sarnak) achieve $\epsilon\le 2\sqrt{d-1}/d$. The author writes that for fixed $d$ and growing $n$, ε "cannot exceed this bound in the limit" (as printed; the overview on p. 219 says ε cannot be asymptotically smaller, which is the reading used here). The proof builds a test function (p. 224).
- **First test vector** (u, v with non-overlapping neighbourhoods): $x(u)=1$, $x=1/\sqrt d$ on $N(u)$, $x(v)=-1$, $x=-1/\sqrt d$ on $N(v)$, else 0.
  - Numerator, summed over edges of squared differences: $2d(1-1/\sqrt d)^2+2d(d-1)/d=2(d-2\sqrt d+1+(d-1))=2(2d-2\sqrt d)$.
  - Denominator is 4, so $x^TLx/x^Tx=d-\sqrt d$.
  - The sign-flipped $y$ (negating the neighbourhood values) gives $d+\sqrt d$. This only recovers $\epsilon\ge1/\sqrt d$ (p. 224).
- Improvements: extend to neighbourhoods of neighbourhoods, and base the construction at two edges so each vertex has $d-1$ edges going farther out (p. 224).
- **Theorem 27.5.1 (Nilli).** If a d-regular $G$ has edges $(u_0,u_1)$, $(v_0,v_1)$ at distance at least $2k+2$, then
$$\lambda_2\le d-2\sqrt{d-1}+\frac{2\sqrt{d-1}-1}{k+1}.$$
- **Proof** (pp. 225–226):
  - $U_0=\{u_0,u_1\}$, $U_i=N(U_{i-1})-\cup_{j<i}U_j$ for $0<i\le k$; similarly $V_i$. No edges join any $U_i$ to any $V_j$.
  - Test vector: $x(a)=(d-1)^{-i/2}$ on $U_i$, $-\beta(d-1)^{-i/2}$ on $V_i$, else 0, with β chosen so $x\perp\mathbf1$.
  - The Rayleigh quotient is at most $\frac{X_0+\beta^2Y_0}{X_1+\beta^2Y_1}$, where $X_0=\sum_{i=0}^{k-1}|U_i|(d-1)\big(\frac{1-1/\sqrt{d-1}}{(d-1)^{i/2}}\big)^2+|U_k|(d-1)^{-k+1}$ and $X_1=\sum_{i=0}^{k}|U_i|(d-1)^{-i}$. $Y_0,Y_1$ are the same with $V_i$. The source gives these without derivation.
  - By "my favorite inequality" (p. 226) it suffices to bound $X_0/X_1$ and $Y_0/Y_1$. *(added step: this is $\frac{a+b}{c+e}\le\max(\frac ac,\frac be)$ for positive terms.)*
  - Since $(d-1)(1-1/\sqrt{d-1})^2=d-2\sqrt{d-1}$, the numerator of $X_0/X_1$ equals
    $\sum_{i=0}^{k-1}\frac{|U_i|}{(d-1)^i}(d-2\sqrt{d-1})+\frac{|U_k|}{(d-1)^k}(d-1)$.
    Writing $d-1=(d-2\sqrt{d-1})+(2\sqrt{d-1}-1)$ gives
    $\sum_{i=0}^{k}\frac{|U_i|}{(d-1)^i}(d-2\sqrt{d-1})+\frac{|U_k|}{(d-1)^k}(2\sqrt{d-1}-1)$.
  - The first sum, divided by $X_1$, gives exactly $d-2\sqrt{d-1}$.
  - Since $|U_k|\le(d-1)^{k-i}|U_i|$, we get $\frac{|U_k|}{(d-1)^k}\le\frac1{k+1}\sum_{i=0}^k\frac{|U_i|}{(d-1)^i}$. The last term then contributes at most $\frac{2\sqrt{d-1}-1}{k+1}$.

*Skip path:* a reader may skip the proof and keep the theorem statement.

*Intuition note:* The test vector decays by $(d-1)^{-1/2}$ per layer. The construction is based at two edges so that each vertex has $d-1$ edges going farther out (p. 224). When the two edges can be taken at large distance (large k), the bound on λ₂ approaches $d-2\sqrt{d-1}$.

### 27.6 Open problems (p. 227)
- The author earlier asserted that the same proof gives $\lambda_n\ge d+2\sqrt{d-1}-\frac{2\sqrt{d-1}-1}{k+1}$; "the proof did not work."
- Open: how well can an irregular graph of average degree d approximate $K_n$? The author doubts irregularity helps but cannot prove it.
- **Conjecture (author):** for every d and β>0 there is $n_0$ such that every weighted graph with $dn/2$ edges, average degree d and $n\ge n_0$ vertices satisfies $\frac{\lambda_2}{\lambda_n}\le\frac{d-2\sqrt{d-1}}{d+2\sqrt{d-1}}+\beta$.

## Toy example (ours)
$G=K_4$: $d=3$, $n=4$, adjacency eigenvalues $3,-1,-1,-1$, so $\epsilon=1/3$.
- Check: $L_G=4I-J$, $H=\frac34K_4$, so $L_H=\frac34(4I-J)$. On $x\perp\mathbf1$, $x^TL_Gx=4x^Tx$ and $x^TL_Hx=3x^Tx$. Here $(1-\frac13)3=2\le4\le4=(1+\frac13)3$. Also $\|L_G-L_H\|=1=\epsilon d$.
- Theorem 27.3.1 with $S=\{1\}$, $T=\{2\}$: $\alpha=\beta=1/4$, $dn=12$. $|\vec E(S,T)|=1$ and $\alpha\beta dn=12/16=0.75$, so the left side is $0.25$. Right side: $\frac13\cdot12\cdot\sqrt{(3/16)(3/16)}=4\cdot\frac3{16}=0.75$. So $0.25\le0.75$.
- Tanner with $S=\{1\}$: $|S|/(\epsilon^2(1-\alpha)+\alpha)=1/(\frac19\cdot\frac34+\frac14)=1/(\frac1{12}+\frac3{12})=3$. Indeed $|N(S)|=3$, so the bound is tight here.

## Concepts
- [[epsilon-expander]] (new) — d-regular graph with $|\mu_i|\le\epsilon d$ for $i\ge2$; equivalent to $\|L_G-\frac dnL_{K_n}\|\le\epsilon d$ (p. 220)
- [[epsilon-approximation]] (new) — $(1-\epsilon)H\preceq G\preceq(1+\epsilon)H$ in the Laplacian order; not symmetric (p. 220)
- [[norm]] — operator norm = largest singular value (p. 220)
- [[graph Laplacian]] — $L_G$; eigenvalues $\lambda_i=d-\mu_i$ for d-regular graphs (p. 220)
- [[Rayleigh quotient]] — $x^TLx/x^Tx$; used with test vectors to upper-bound $\lambda_2$ (p. 224)
- [[expander-mixing-bound]] (new) — edge count between any two sets is within $\epsilon dn\sqrt{(\alpha-\alpha^2)(\beta-\beta^2)}$ of random (p. 221)
- [[tanner-theorem]] (new) — lower bound on $|N(S)|$ for ε-approximations of $\frac dnK_n$ (p. 223)
- [[alon-boppana-bound]] (new) — Nilli's upper bound on $\lambda_2$ via test vectors on layered neighbourhoods (p. 224)
- [[ramanujan-graph]] (new) — graphs achieving $\epsilon\le2\sqrt{d-1}/d$ (p. 224)

## Canonical instances
- [[complete-graph-Kn]] — reference graph: $x^TL_{K_n}x=n\,x^Tx$ for $x\perp\mathbf1$ (p. 220)
- [[ramanujan-graph]] — Margulis and Lubotzky–Phillips–Sarnak constructions (p. 224)
- [[random-regular-graph]] — an expander with reasonably high probability [Fri08] (p. 221)

## Bridges (candidates)
- [structural-analogy] Quasi-random edge counts ↔ probability: concentration of edge counts in random sets — a spectral bound replaces a probabilistic one.
- [same-math] Test-vector upper bound on λ₂ ↔ linear-algebra: Rayleigh quotient of a trial vector orthogonal to $\mathbf 1$ upper-bounds $\lambda_2$ (the variational idea; not developed on these pages).
- [structural-analogy] Tanner neighbour growth ↔ community structure: a large λ₂ means no sparse cuts, the opposite of Fiedler-vector clustering.

## Questions this raises
- Why does the (d−1)-ary tree structure give exactly $2\sqrt{d-1}$, and why must large-distance edges exist when n grows?
- Why does the same test-vector argument fail for $\lambda_n$?
- Can irregular or weighted graphs of average degree d beat Ramanujan graphs?
- Are the quasi-random bounds tight for sets of size comparable to ε?

## Reading notes
- Printed page = pdf − 24. The unit opens with "This Chapter Needs Editing" (draft notice, p. 219).
- p. 222: the image prints "$\|x_S\|=n(\alpha-\alpha^2)$". The next line, $\|x_S\|\|x_T\|=n\sqrt{(\alpha-\alpha^2)(\beta-\beta^2)}$, requires $\|x_S\|^2=n(\alpha-\alpha^2)$. This looks like a misprint (missing square or root).
- p. 223: from $\epsilon^2(1-1/n)+1/n\ge1/d$ I get $\epsilon^2\ge\frac{n-d}{d(n-1)}$, not the printed $\epsilon\ge1/\sqrt{d(n-1)/n}$. Both are about $1/\sqrt d$ for large $n$.
- p. 224: the text says ε "cannot exceed" the Ramanujan value in the limit. The overview (p. 219) and the logic of Thm 27.5.1 say ε cannot be asymptotically smaller. I follow the overview.
- p. 224: "whose neighborhoods to do not overlap" is a typo as printed.
- p. 220: the ε-expander definition prints "for $\mu_i\ge2$"; I read it as $i\ge2$, as the equivalent statement in the same sentence uses.
- p. 224: the source attributes Thm 27.5.1 to A. Nilli but says it was probably written by N. Alon.
- p. 221: the text says only the disjoint case is proved "in class". The printed proof is written for general S, T.
- The proof of Thm 27.5.1 states the bounds on $X_0$, $X_1$, $Y_0$, $Y_1$ without derivation.
