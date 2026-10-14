---
id: spielman-2025-sagt/ch12-effective
work: spielman-2025-sagt
unit: "Chapter 12 — Effective Resistance and Schur Complements"
pages: 111-121
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Effective Resistance and Schur Complements

## L0 — One line
Eliminating internal vertices from a weighted graph by Gaussian elimination leaves a smaller weighted graph (a Schur complement of the Laplacian) with the same voltages and currents on the kept vertices, and effective resistance, defined by $L^+$, is a squared Euclidean distance that also satisfies the triangle inequality.

## L1 — The gist (≤ 120 words)
How can a whole network act as one resistor between two vertices, or as a smaller network on a chosen vertex subset $B$? The chapter defines effective resistance as $(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)$ and shows that it is the reciprocal of the effective spring constant, which is twice the minimum spring energy. It proves reciprocity, Rayleigh monotonicity, and the series and parallel rules. Eliminating internal vertices (making them harmonic) gives the Schur complement $L_B$, which is again a Laplacian. For a symmetric matrix $M$ (with $M$ and $M(S,S)$ invertible), the restriction of $M^{-1}$ to $B$ equals the inverse of the Schur complement $M_B$. Finally, effective resistance is a distance (it satisfies the triangle inequality). The chapter's introduction also says it can serve as a measure of the importance of an edge.

**Prerequisites:** graph Laplacian $L=D-A$ and its pseudoinverse; spectral decomposition; harmonic vectors; Gaussian elimination; block matrices.

## L2 — Key ideas
- Effective resistance is $R_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)=\|L^{+/2}(\delta_a-\delta_b)\|^2$, a squared Euclidean distance (p. 112).
- Effective conductance $C_{\rm eff}=1/R_{\rm eff}$ equals $x^TLx$ for the minimum-energy $x$ with $x(t)-x(s)=1$, which is twice the minimum energy (p. 113).
- Voltage differences are reciprocal because $L$ is symmetric. Lowering weights cannot raise effective conductance (Rayleigh monotonicity), a property the author calls special to linear elements (pp. 113–114).
- Parallel edges add weights; series edges add resistances (p. 114).
- Eliminating one vertex by Gaussian elimination equals substituting its harmonic value. The result is a Laplacian (pp. 116–118).
- Eliminating a set $S$ gives the Schur complement $L_B=L(B,B)-L(B,S)L(S,S)^{-1}L(S,B)$, a Laplacian (pp. 118–119).
- For symmetric $M$ with $M$ and $M(S,S)$ invertible: $(M^{-1})(B,B)=(M_B)^{-1}$ (pp. 119–120).
- Effective resistance obeys the triangle inequality, shown on three vertices via elimination (pp. 120–121).

## L3 — Walkthrough

### 12.1 Electrical flows and effective resistance (pp. 111–112)
Voltages satisfy $v=L^+i_{\rm ext}$. For a unit flow from $a$ to $b$, $v=L^+(\delta_a-\delta_b)$ (p. 111). Ohm's law is $i(a,b)=(v(a)-v(b))/r_{a,b}$. The author applies it to the whole network: inject one unit at $a$, remove one unit at $b$, and measure the voltage difference (p. 112):
$$R_{\rm eff}(a,b)\overset{\rm def}{=}(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b).$$
For a symmetric PSD matrix $M=\sum_i\lambda_i\psi_i\psi_i^T$, the square root is $M^{1/2}=\sum_i\lambda_i^{1/2}\psi_i\psi_i^T$. Hence (p. 112)
$$(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)=\|L^{+/2}(\delta_a-\delta_b)\|^2=\mathrm{dist}(L^{+/2}\delta_a,L^{+/2}\delta_b)^2.$$
*Intuition note:* Map each vertex to the point $L^{+/2}\delta_a$. Effective resistance is then the squared straight-line distance between two points.

### 12.2 Energy minimization (pp. 112–113)
The effective spring constant is defined as twice the minimum possible energy $\mathcal E$, where $2\mathcal E(x)=\sum_{(a,b)\in E}w_{a,b}(x(a)-x(b))^2$ with $x(s)$ and $x(t)$ differing by 1. The minimiser is harmonic off $\{s,t\}$, by Theorem 11.6.1 (p. 112). Take $x=L^+(\delta_t-\delta_s)/R_{\rm eff}(t,s)$. Then $x(t)-x(s)=(\delta_t-\delta_s)^TL^+(\delta_t-\delta_s)/R_{\rm eff}(s,t)=1$, and $x$ is harmonic off $\{s,t\}$. Its energy form is (p. 113)
$$C_{\rm eff}(s,t)=x^TLx=\frac{(\delta_t-\delta_s)^TL^+LL^+(\delta_t-\delta_s)}{R_{\rm eff}(s,t)^2}=\frac{(\delta_t-\delta_s)^TL^+(\delta_t-\delta_s)}{R_{\rm eff}(s,t)^2}=\frac1{R_{\rm eff}(s,t)}.$$
This is the effective conductance.

### 12.3 Reciprocity and monotonicity (pp. 113–114)
For a unit flow $a\to b$, $v(c)-v(d)=(\delta_c-\delta_d)^TL^+(\delta_a-\delta_b)$. As $L$ is symmetric, this equals $(\delta_a-\delta_b)^TL^+(\delta_c-\delta_d)$. So the voltage difference across $(c,d)$ for a unit flow $a\to b$ equals the one across $(a,b)$ for a unit flow $c\to d$ (p. 113).

**Theorem 12.3.1 (Rayleigh monotonicity).** If $G$ and $\widehat G$ have the same edges and $\widehat w_{a,b}\le w_{a,b}$ for all edges $(a,b)$, then the effective spring constants satisfy $\widehat c_{s,t}\le c_{s,t}$ for any vertices $s,t$ (p. 113).
*Proof:* Let $x$ be the minimum-energy vector in $G$ with $x(s)=0$, $x(t)=1$. Its energy in $\widehat G$ is no greater than in $G$. So the minimum in $\widehat G$ is at most $c_{s,t}$ (p. 114). In terms of resistances, this says that raising resistances cannot lower $R_{\rm eff}$. The author warns that this fails "in just slightly more complicated situations" (p. 114).
*Intuition note:* Weakening springs cannot make the network stiffer, because the old best stretch pattern is still available at no greater cost.

### 12.4 Series and parallel (pp. 114–115)
- **Parallel:** with resistances $r_i$, $R_{\rm eff}=1/(1/r_1+\dots+1/r_k)$. In weights, conductance is $w_1+\dots+w_k$: a unit voltage drives flow $w_i$ on edge $i$ (p. 114).
- **Series (path):** $R_{\rm eff}=r_{1,2}+\dots+r_{n-1,n}$. Set $v(i)=r_{i,i+1}+\dots+r_{n-1,n}$. Each edge then carries current 1, and the flow is harmonic at internal vertices. The unit-weight path gives $n-1$ (p. 114).
- This gives another proof of the weighted path inequality (Lemma 6.6.1), $(x(1)-x(n))^2\le\left(\sum_a 1/w_a\right)\sum_a w_a(x(a)-x(a+1))^2$. The minimum energy given the endpoints is $\frac12\left(\sum_a 1/w_a\right)^{-1}(x(1)-x(n))^2$, and any other configuration has at least this energy (p. 115).

### 12.5 Equivalent networks, elimination, Schur complements (pp. 115–118)
Keep $B$; call $S=V-B$ internal. Fix $v(B)$, make $v(S)$ harmonic, and seek $L_B$ with $i_B=L_Bv(B)$ (p. 115). Footnote: $L_B$ is not a submatrix of $L$.

*Eliminating vertex 1* ($B=\{2,\dots,n\}$, $N$ = neighbours of 1). Harmonicity gives
$$v(1)=\frac1{d(1)}\sum_{a\in N}w_{1,a}v(a).\tag{12.1}$$
For $b\in N$, substitute into $i_{ext}(b)=d(b)v(b)-w_{b,1}v(1)-\sum_{c\sim b,c\ne1}w_{b,c}v(c)$ (p. 116). Since $b\in N$, the term $a=b$ moves to the diagonal:
$$i_{ext}(b)=\Big(d(b)-\frac{w_{b,1}^2}{d(1)}\Big)v(b)-\sum_{a\in N,a\ne b}\frac{w_{b,1}w_{1,a}}{d(1)}v(a)-\sum_{c\sim b,c\ne1}w_{b,c}v(c).$$
In row $b$ the column-1 entry vanishes. The diagonal drops by $w_{b,1}^2/d(1)$, and each off-diagonal entry $a\in N$, $a\ne b$, drops by $w_{b,1}w_{a,1}/d(1)$. The total change in the row is $w_{b,1}-\sum_{a\in N}w_{b,1}w_{a,1}/d(1)=w_{b,1}-w_{b,1}\sum_{a\in N} w_{a,1}/d(1)=0$, so row sums stay 0 (p. 116). The changes are symmetric and only decrease off-diagonal entries; together with the zero row sums, this is what the author uses to conclude that the system is a Laplacian, since a Laplacian needs symmetry, non-positive off-diagonal entries and zero row sums (pp. 116–117).

This is Gaussian elimination: subtract $L(b,1)/L(1,1)=-w_{b,1}/d(1)$ times row 1 from row $b$. This changes the diagonal by $L(b,1)L(1,b)/L(1,1)=w_{b,1}^2/d(1)$ and the entry in column $a$ by $w_{b,1}w_{a,1}/d(1)$ (p. 117).

**12.5.1 By energy.** Require $v(B)^TL_Bv(B)=v^TLv$ for $v$ harmonic at 1. Here $d(1)=L(1,1)$, $\sum_{b\sim1}w_{1,b}v(b)=-L(1,B)v(B)$ (the off-diagonal entries of $L$ are $-w$; the page writes $+L(1,B)v(B)$, but its next line has $v(1)=-(1/L(1,1))L(1,B)v(B)$), so $v(1)=-L(1,B)v(B)/L(1,1)$ (p. 117). Expanding $v^TLv$:
$$v(B)^TL(B,B)v(B)+L(1,1)v(1)^2+2v(1)L(1,B)v(B)=v(B)^TL(B,B)v(B)+\frac{(L(1,B)v(B))^2}{L(1,1)}-\frac{2(L(1,B)v(B))^2}{L(1,1)}.$$
This equals $v(B)^TL(B,B)v(B)-(L(1,B)v(B))^2/L(1,1)$. Hence (p. 117)
$$L_B=L(B,B)-\frac{L(B,1)L(1,B)}{L(1,1)}.$$
It is symmetric. Its off-diagonal entries are non-positive because $L(1,B)\le0$ and $L(1,1)>0$. From $L\mathbf 1=0$: $L(1,B)\mathbf 1_B=-L(1,1)$ and $L(B,B)\mathbf 1_B=-L(B,1)$. So $L_B\mathbf 1_B=-L(B,1)+L(B,1)=0_B$ (p. 118).
*Intuition note:* Removing a vertex replaces its star of edges by a clique among its neighbours. The edge between neighbours $a$ and $b$ gets extra weight $w_{b,1}w_{a,1}/d(1)$.

### 12.6 Eliminating many vertices (pp. 118–119)
To clear the entries of a row $a\in B$ in the columns $S$ by adding multiples of the rows $L(S,:)$, the coefficients must satisfy $L(a,S)+cL(S,S)=0$, so $c=-L(a,S)L(S,S)^{-1}$. Restricting to $B$ gives the **Schur complement**
$$L_B=L(B,B)-L(B,S)L(S,S)^{-1}L(S,B).$$
Intermediate matrices do not depend on elimination order, so $L_B$ is uniquely defined (p. 118). Equivalently, harmonicity $L(S,S)v(S)+L(S,B)v(B)=0$ gives $v(S)=-L(S,S)^{-1}L(S,B)v(B)$. Then $i_{ext}(B)=L(B,S)v(S)+L(B,B)v(B)=L_Bv(B)$ (p. 119). $L_B$ is a Laplacian:
- Symmetric by the formula.
- $L_B\mathbf 1_B=-L(B,S)\mathbf 1_S-L(B,S)L(S,S)^{-1}(-L(S,S)\mathbf 1_S)=0_B$, using $L(B,B)\mathbf 1_B=-L(B,S)\mathbf 1_S$ and $L(S,B)\mathbf 1_B=-L(S,S)\mathbf 1_S$.
- Off-diagonals are non-positive, because $L(B,S)L(S,S)^{-1}L(S,B)$ is non-negative. This uses that $L(S,S)^{-1}$ is positive (Theorem 11.5.4) and $L(S,B)\le 0$ (p. 119).

### 12.7 The Schur complement (pp. 119–120)
For symmetric $M$ with $M(S,S)$ invertible: $M_B\overset{\rm def}{=}M(B,B)-M(B,S)M(S,S)^{-1}M(S,B)$ (p. 119).

**Theorem 12.7.1.** If $M$ and $M(S,S)$ are invertible, then $(M^{-1})(B,B)=(M_B)^{-1}$ (p. 119).
*Proof (as given):* Write the block inverse
$$\begin{pmatrix}(M_B)^{-1}&-(M_B)^{-1}M(B,S)M(S,S)^{-1}\\-M(S,S)^{-1}M(S,B)(M_B)^{-1}&M(S,S)^{-1}+M(S,S)^{-1}M(S,B)M_B^{-1}M(B,S)M(S,S)^{-1}\end{pmatrix}$$
and multiply by $\begin{pmatrix}M(B,B)&M(B,S)\\M(S,B)&M(S,S)\end{pmatrix}$ to confirm the identity (p. 120). The author does not carry out the multiplication.

### 12.8 Interpreting Gaussian elimination (p. 120)
Elimination builds graphs $G_2,\dots,G_n$, where $G_i$ is the effective network on vertices $i,\dots,n$. It then solves for $v$ backwards. If $i_{ext}(i)=0$, $v(i)$ is the weighted average of its neighbours. If not, $i_{ext}(i)$ has to be taken into account here and in the elimination as well. When some vertices are fixed and the rest are harmonic, there is no such complication (p. 120).

### 12.9 Effective resistance is a distance (pp. 120–121)
A distance needs $\delta(a,a)=0$, $\delta\ge0$, symmetry and the triangle inequality. Only the triangle inequality is non-trivial. By elimination, any graph can be reduced to $a,b,c$ without changing the effective resistances among them (p. 120).

**Lemma 12.9.1.** $R_{\rm eff}(a,b)+R_{\rm eff}(b,c)\ge R_{\rm eff}(a,c)$.
*Proof:* Let $z=w_{a,b}$, $y=w_{a,c}$, $x=w_{b,c}$. Eliminating $c$ adds weight $\frac{xy}{x+y}$ to edge $(a,b)$. So
$$R_{\rm eff}(a,b)=\frac1{z+\frac{xy}{x+y}}=\frac{x+y}{zx+zy+xy}.$$
By symmetry the claim becomes, for positive $x,y,z$,
$$\frac{x+y}{zx+zy+xy}+\frac{y+z}{zx+zy+xy}\ge\frac{x+z}{zx+zy+xy}.$$
(added step) After multiplying by the common denominator, the left side minus the right side is $2y\ge0$ (p. 121).

## Toy example (ours)
Triangle on $a,b,c$ with $w_{ab}=1$, $w_{ac}=2$, $w_{bc}=2$. Order $(a,b,c)$:
$$L=\begin{pmatrix}3&-1&-2\\-1&3&-2\\-2&-2&4\end{pmatrix}.$$
Take $B=\{a,b\}$, $S=\{c\}$. Then $L(B,S)L(S,S)^{-1}L(S,B)=\frac14\begin{pmatrix}-2\\-2\end{pmatrix}\begin{pmatrix}-2&-2\end{pmatrix}=\begin{pmatrix}1&1\\1&1\end{pmatrix}$. So
$$L_B=\begin{pmatrix}3&-1\\-1&3\end{pmatrix}-\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}2&-2\\-2&2\end{pmatrix}.$$
This is a single edge of weight 2. It matches $1+\frac{2\cdot2}{2+2}=2$, and $R_{\rm eff}(a,b)=1/2$. The Lemma 12.9.1 formula gives $\frac{x+y}{zx+zy+xy}=\frac4{2+2+4}=\frac12$, which agrees.

## Concepts
- [[effective-resistance]] (new) — $(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)$; the voltage drop for a unit current; a squared Euclidean distance (p. 112)
- [[effective-conductance]] (new) — $1/R_{\rm eff}$; equals $x^TLx$ for the minimum-energy $x$ with $x(t)-x(s)=1$, twice the minimum energy (p. 113)
- [[schur-complement]] (new) — $M(B,B)-M(B,S)M(S,S)^{-1}M(S,B)$; Gaussian elimination of $S$ (pp. 118–119)
- [[graph Laplacian]] — here also an operator from voltages to external currents (p. 115)
- [[quadratic form]] — energy $v^TLv$, preserved by the Schur complement on harmonic extensions (p. 117)
- [[positive (semi)definite matrix]] — used to define $M^{1/2}$ by the spectral decomposition (p. 112)
- [[rayleigh-monotonicity]] (new) — lowering weights cannot raise effective conductance (p. 113)
- [[harmonic-vector]] (new) — value at an internal vertex is the weighted average of its neighbours (p. 116)

## Canonical instances
- [[series-parallel-networks]] — weights add in parallel; resistances add in series (p. 114)
- [[path-graph-resistance]] — unit-weight path has $R_{\rm eff}=n-1$ between its ends (p. 114)
- [[three-vertex-reduction]] — eliminating $c$ gives edge $xy/(x+y)$, used for the triangle inequality (p. 121)

## Bridges (candidates)
- [same-math] Schur complement $M_B$ ↔ linear-algebra: block Gaussian elimination, with $(M^{-1})(B,B)=(M_B)^{-1}$ — the same block formulas.
- [structural-analogy] Effective resistance as squared distance between $L^{+/2}\delta_a$ points ↔ spectral embedding: vertices as vectors — both use the spectral decomposition of $L$.
- [metaphor] Rayleigh monotonicity ↔ stiffer springs give a stiffer whole — an intuition for "more edge weight, more conductance".

## Questions this raises
- Why can the effective resistance of an edge be the probability that it appears in a random spanning tree (Chapter 13, p. 111)?
- Why does sampling edges in proportion to weight times effective resistance give a good approximation (Chapter 32, p. 111)?
- In which "more complicated situations" does monotonicity fail (p. 114)?
- How does the elimination order affect the cost of Gaussian elimination, even though $L_B$ is order-independent (p. 118)?

## Reading notes
- Printed = pdf − 24.
- The factor 2 is inconsistent. Section 12.2 defines $C_{\rm eff}=x^TLx=\sum w(x(a)-x(b))^2=2\mathcal E_{\min}$. The proof of Thm 12.3.1 (p. 114) writes $\tfrac12\sum\widehat w(\dots)^2\le\tfrac12\sum w(\dots)^2=c_{s,t}$. The inequality argument is unaffected.
- The page 117 expansion prints $2v(1)L(1,B)\big(-L(1,B)v(B)/L(1,1)\big)$. Taken literally this substitutes $v(1)$ twice. The next line, $-2(L(1,B)v(B))^2/L(1,1)$, matches the correct cross term $2v(1)L(1,B)v(B)$.
- Typos: "this potential flow harmonic" (p. 115, missing "is"); "at upper bounded" (p. 119, should be "are"); "substition" (p. 117).
- On p. 117 the page prints $\sum_{b\sim1}w_{1,b}v(b)=L(1,B)v(B)$ without a minus sign. Its next line, $v(1)=-(1/L(1,1))L(1,B)v(B)$, uses the correct sign $-L(1,B)v(B)$.
- In 12.6 (p. 119), $M$ denotes the adjacency matrix; in 12.7 (also p. 119) it is a general symmetric matrix, so the letter is reused.
- The proof of Theorem 12.7.1 is only sketched. The reduction to three vertices in 12.9 cites "the previous section".
