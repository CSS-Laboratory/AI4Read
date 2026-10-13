---
id: axler-2024-ladr/ch06-inner-p2
work: axler-2024-ladr
unit: "6 Inner Product Spaces (part 2/2): 6B Orthonormal Bases; 6C Orthogonal Complements and Minimization Problems"
pages: 197–226
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Orthonormal Bases, Orthogonal Complements, Best Approximation and the Pseudoinverse

## L0 — One line
In a finite-dimensional inner product space, orthonormal bases (built by Gram–Schmidt) turn inner products into coordinates, and orthogonal projection onto a subspace gives the unique closest point, which also yields the pseudoinverse.

## L1 — The gist (≤ 120 words)
Which bases make an inner product space easy to compute in, and how do we find the closest point of a subspace? Axler shows that an orthonormal basis (unit vectors, pairwise orthogonal) gives the coordinates ⟨v, e_k⟩ directly. Gram–Schmidt turns any independent list into an orthonormal list with the same spans, so finite-dimensional inner product spaces have orthonormal bases. For finite-dimensional U, the complement U^⊥ (vectors orthogonal to U) splits V as U ⊕ U^⊥ and defines the projection P_U, which gives the unique closest point of U. These tools prove Schur's theorem and the Riesz representation theorem. They also give a best polynomial approximation of sin x and the pseudoinverse, the best-fit, minimum-norm answer to Tv = w.

**Prerequisites:** inner product, norm, Pythagorean theorem (6.12); basis, dimension, direct sum; linear maps, null space, range; upper-triangular matrices and minimal polynomial (Ch. 5); definite integrals.

## L2 — Key ideas (5–10 bullets)
- An orthonormal list (unit vectors, pairwise orthogonal) has ‖Σaₖeₖ‖² = Σ|aₖ|², so it is automatically linearly independent. In dimension n, an orthonormal list of length n is a basis (pp. 198–199).
- In an orthonormal basis, coefficients are v = Σ⟨v,eₖ⟩eₖ, with ‖v‖² = Σ|⟨v,eₖ⟩|². No linear system needs solving (p. 200).
- Gram–Schmidt (subtract from each vector its components along the earlier ones, then rescale to length 1) turns an independent list into an orthonormal list with the same spans at each step. Hence, in finite-dimensional spaces, orthonormal bases exist, and every orthonormal list extends to one (pp. 201–203).
- Schur's theorem (upper-triangular = all entries below the diagonal are 0): for complex finite-dimensional V, every operator has an upper-triangular matrix in some orthonormal basis (pp. 203–204).
- Riesz representation theorem: on finite-dimensional V, every linear functional (linear map V → F) is u ↦ ⟨u,v⟩ for a unique v. The proof is given twice, using an orthonormal basis and then null-space complements (pp. 205, 216–217).
- For finite-dimensional U, V = U ⊕ U^⊥ (U^⊥ = all vectors orthogonal to every vector of U) and U = (U^⊥)^⊥. Orthogonal projection P_U (write v = u + w with u ∈ U, w ∈ U^⊥; then P_U v = u) is well defined and has a list of properties (pp. 212–216).
- P_U v is the unique point of U closest to v. With Gram–Schmidt this gives the best polynomial approximation of sin x on [−π, π] (pp. 217–219).
- The pseudoinverse T† (a linear map W → V built from T restricted to (null T)^⊥ and the projection onto range T) gives the best-fit solution of Tv = w, and among best fits, the one of smallest norm (pp. 220–222).

## L3 — Walkthrough

### 6B. Orthonormal Bases

#### Orthonormal lists and the Gram–Schmidt procedure

**6.22 Definition (orthonormal).** A list $e_1,\dots,e_m$ in $V$ is orthonormal if every vector has norm 1 and is orthogonal to all the others:
$$\langle e_j,e_k\rangle=\begin{cases}1&j=k\\0&j\ne k\end{cases}\qquad j,k\in\{1,\dots,m\}.$$
(p. 197)

**6.23 Examples.** (p. 197)
- (a) The standard basis of $\mathbf F^n$ is orthonormal.
- (b), (c) $(\tfrac1{\sqrt3},\tfrac1{\sqrt3},\tfrac1{\sqrt3}),(-\tfrac1{\sqrt2},\tfrac1{\sqrt2},0)$ is orthonormal in $\mathbf F^3$. Adding $(\tfrac1{\sqrt6},\tfrac1{\sqrt6},-\tfrac2{\sqrt6})$ keeps it orthonormal.
- (d) In $C[-\pi,\pi]$ (continuous real functions, $\langle f,g\rangle=\int_{-\pi}^{\pi}fg$) the list $\frac1{\sqrt{2\pi}},\frac{\cos x}{\sqrt\pi},\dots,\frac{\cos nx}{\sqrt\pi},\frac{\sin x}{\sqrt\pi},\dots,\frac{\sin nx}{\sqrt\pi}$ is orthonormal (Exercise 4). The author says it is often used to model periodic phenomena such as tides.
- (e) In $\mathcal P_2(\mathbf R)$ with $\langle p,q\rangle=\int_{-1}^1pq$, the standard basis $1,x,x^2$ is not orthonormal. Normalising gives $1/\sqrt2,\sqrt{3/2}\,x,\sqrt{5/2}\,x^2$. The second vector is orthogonal to the other two, but the first and third are not orthogonal, so the list is still not orthonormal.

**6.24 Norm of an orthonormal linear combination.** If $e_1,\dots,e_m$ is orthonormal, then
$$\|a_1e_1+\dots+a_me_m\|^2=|a_1|^2+\dots+|a_m|^2\quad\text{for all }a_k\in\mathbf F.$$
Proof: repeated Pythagorean theorem (6.12), using $\|e_k\|=1$. (p. 198)

**6.25 Orthonormal lists are linearly independent.** If $\sum a_ke_k=0$, then $\sum|a_k|^2=0$ by 6.24, so all $a_k=0$. (p. 198)

**6.26 Bessel's inequality.** If $e_1,\dots,e_m$ is orthonormal and $v\in V$, then $|\langle v,e_1\rangle|^2+\dots+|\langle v,e_m\rangle|^2\le\|v\|^2$. (p. 198)
Proof (p. 198):
1. Write $v=u+w$ with $u=\langle v,e_1\rangle e_1+\dots+\langle v,e_m\rangle e_m$ and $w=v-u$.
2. For each $k$: $\langle w,e_k\rangle=\langle v,e_k\rangle-\langle v,e_k\rangle\langle e_k,e_k\rangle=0$.
3. So $\langle w,u\rangle=0$, and the Pythagorean theorem gives $\|v\|^2=\|u\|^2+\|w\|^2\ge\|u\|^2$.
4. By 6.24, $\|u\|^2=\sum|\langle v,e_k\rangle|^2$.

> **Intuition note.** Orthonormal vectors do not interfere: the "length squared" of a combination is just the sum of squared coefficients. Bessel says that the squared sizes of the components along $e_1,\dots,e_m$ cannot add up to more than the whole vector's squared size.

**6.27 Definition.** An orthonormal basis of $V$ is an orthonormal list that is also a basis. (p. 199)

**6.28.** If $V$ is finite-dimensional, every orthonormal list of length $\dim V$ is an orthonormal basis. Reason: it is linearly independent (6.25), and an independent list of the right length is a basis (cited as 2.38). (p. 199)

**6.29 Example.** In $\mathbf F^4$, the list $(\tfrac12,\tfrac12,\tfrac12,\tfrac12),(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12),(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12),(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12)$ is an orthonormal basis. The first vector has norm $\sqrt{4\cdot\frac1{2^2}}=1$. The inner product of the first two vectors is $\tfrac14+\tfrac14-\tfrac14-\tfrac14=0$. The other norms and inner products are checked "similarly". Four orthonormal vectors in a 4-dimensional space form a basis by 6.28. (p. 199)

**6.30 Writing a vector in an orthonormal basis.** Let $e_1,\dots,e_n$ be an orthonormal basis of $V$ and $u,v\in V$. Then (p. 200)
- (a) $v=\langle v,e_1\rangle e_1+\dots+\langle v,e_n\rangle e_n$;
- (b) $\|v\|^2=|\langle v,e_1\rangle|^2+\dots+|\langle v,e_n\rangle|^2$ (Parseval's identity, published 1799 in the context of Fourier series);
- (c) $\langle u,v\rangle=\langle u,e_1\rangle\overline{\langle v,e_1\rangle}+\dots+\langle u,e_n\rangle\overline{\langle v,e_n\rangle}$.

Proof (p. 200):
1. Write $v=a_1e_1+\dots+a_ne_n$ (basis).
2. Take the inner product with $e_k$: orthonormality gives $\langle v,e_k\rangle=a_k$. This is (a).
3. (b) follows from (a) and 6.24.
4. For (c), take the inner product of $u$ with both sides of (a) and use conjugate linearity in the second slot.

The author remarks that this makes every $n$-dimensional inner product space behave like $\mathbf F^n$, with $\langle v,e_k\rangle$ as coordinates. (p. 200)

**6.31 Example.** $(1,2,4,7)$ in the basis of 6.29. The four inner products are $7,-4,1,2$. Hence $(1,2,4,7)=7(\tfrac12,\tfrac12,\tfrac12,\tfrac12)-4(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12)+(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12)+2(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12)$. A non-orthonormal basis would typically require solving four equations in four unknowns. (p. 200)

> **Intuition note.** With an orthonormal basis, "how much of $e_k$ is in $v$?" is answered by one inner product. This is the same job a dot product does for the standard basis.

**6.32 Gram–Schmidt procedure.** Let $v_1,\dots,v_m$ be linearly independent in $V$. Put $f_1=v_1$ and, for $k=2,\dots,m$,
$$f_k=v_k-\frac{\langle v_k,f_1\rangle}{\|f_1\|^2}f_1-\dots-\frac{\langle v_k,f_{k-1}\rangle}{\|f_{k-1}\|^2}f_{k-1}.$$
Let $e_k=f_k/\|f_k\|$. Then $e_1,\dots,e_m$ is orthonormal and $\operatorname{span}(v_1,\dots,v_k)=\operatorname{span}(e_1,\dots,e_k)$ for each $k$. (p. 201)

Proof, by induction on $k$ (p. 201):
1. *Base $k=1$.* $e_1=f_1/\|f_1\|$ has norm 1, and $e_1$ is a nonzero multiple of $v_1$, so the spans agree.
2. *Hypothesis.* Assume $e_1,\dots,e_{k-1}$ is orthonormal with $\operatorname{span}(v_1,\dots,v_{k-1})=\operatorname{span}(e_1,\dots,e_{k-1})$ (6.33).
3. *No division by zero.* Independence gives $v_k\notin\operatorname{span}(v_1,\dots,v_{k-1})=\operatorname{span}(f_1,\dots,f_{k-1})$. So $f_k\ne0$, and $\|e_k\|=1$.
4. *Orthogonality.* For $j<k$, $\langle e_k,e_j\rangle=\frac1{\|f_k\|\|f_j\|}\langle f_k,f_j\rangle$. In $\langle f_k,f_j\rangle$ only the $f_j$ term of the sum survives, giving $\langle v_k,f_j\rangle-\langle v_k,f_j\rangle=0$.
5. *Spans.* $v_k\in\operatorname{span}(e_1,\dots,e_k)$ by the definition of $f_k$, so $\operatorname{span}(v_1,\dots,v_k)\subseteq\operatorname{span}(e_1,\dots,e_k)$. Both lists are linearly independent (the $e$'s by 6.25), so both spans have dimension $k$ and are equal.

> **Intuition note.** At each step, subtract from $v_k$ everything that already lies along the earlier directions. What is left is perpendicular to them, and dividing by its length makes it a unit vector. Each step adds one new direction without changing the span.

**6.34 Example (an orthonormal basis of $\mathcal P_2(\mathbf R)$, $\langle p,q\rangle=\int_{-1}^1pq$).** Apply 6.32 to $1,x,x^2$. (p. 202)
- $f_1=1$, $\|f_1\|^2=\int_{-1}^11=2$.
- $f_2=x-\frac{\langle x,1\rangle}{\|f_1\|^2}\cdot1=x$, because $\langle x,1\rangle=\int_{-1}^1t\,dt=0$. Also $\|f_2\|^2=\int_{-1}^1t^2dt=\frac23$.
- $f_3=x^2-\frac12\langle x^2,1\rangle-\frac32\langle x^2,x\rangle x=x^2-\frac13$. Also $\|f_3\|^2=\int_{-1}^1(t^4-\frac23t^2+\frac19)dt=\frac8{45}$.
- Normalising gives the orthonormal list $\sqrt{\tfrac12},\ \sqrt{\tfrac32}\,x,\ \sqrt{\tfrac{45}8}\,(x^2-\tfrac13)$. It has length $3=\dim\mathcal P_2(\mathbf R)$, so it is a basis by 6.28.

**6.35 Existence.** Every finite-dimensional inner product space has an orthonormal basis: apply 6.32 to any basis, then use 6.28. (p. 202)

**6.36 Extension.** In finite-dimensional $V$, every orthonormal list $e_1,\dots,e_m$ extends to an orthonormal basis. Proof: the list is independent (6.25), so extend it to a basis $e_1,\dots,e_m,v_1,\dots,v_n$ (cited as 2.32). Apply 6.32. The formulas leave the first $m$ vectors unchanged because they are already orthonormal. The result is an orthonormal list of length $\dim V$, hence a basis by 6.28. (p. 203)

**6.37 Upper-triangular matrix in an orthonormal basis.** Let $V$ be finite-dimensional and $T\in\mathcal L(V)$. Then $T$ has an upper-triangular matrix with respect to some orthonormal basis if and only if the minimal polynomial of $T$ equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some $\lambda_1,\dots,\lambda_m\in\mathbf F$. (p. 203) This is the same condition as for an arbitrary basis (5.44).
Proof (p. 203):
1. If the matrix is upper triangular for some basis $v_1,\dots,v_n$, then $\operatorname{span}(v_1,\dots,v_k)$ is $T$-invariant for each $k$ (5.39).
2. Apply 6.32 to get an orthonormal basis $e_1,\dots,e_n$ with $\operatorname{span}(e_1,\dots,e_k)=\operatorname{span}(v_1,\dots,v_k)$. These spans are invariant, so the matrix in the $e$-basis is upper triangular (5.39).
3. Use 5.44 to finish the equivalence with the minimal polynomial condition.

**6.38 Schur's theorem.** Every operator on a finite-dimensional complex inner product space has an upper-triangular matrix with respect to some orthonormal basis. The text says this follows from the second version of the fundamental theorem of algebra (4.13, not restated here) and 6.37. Exercise 20 gives a version for several commuting operators. (p. 204)

> **Intuition note.** Gram–Schmidt keeps the nested spans $\operatorname{span}(e_1,\dots,e_k)$ the same, and "upper triangular" is exactly a statement about nested invariant spans. So switching to an orthonormal basis costs nothing.

#### Linear functionals on inner product spaces

**6.39 Definition.** A *linear functional* on $V$ is a linear map $V\to\mathbf F$. The *dual space* $V'=\mathcal L(V,\mathbf F)$ is the vector space of all linear functionals on $V$. (p. 204)

**6.40, 6.41 Examples.** $\varphi(z_1,z_2,z_3)=2z_1-5z_2+z_3$ on $\mathbf F^3$ equals $\langle z,w\rangle$ with $w=(2,-5,1)$. $\varphi(p)=\int_{-1}^1p(t)\cos(\pi t)\,dt$ is a linear functional on $\mathcal P_5(\mathbf R)$. (p. 204)

For fixed $v$, $u\mapsto\langle u,v\rangle$ is a linear functional. The next theorem says every functional has this form. (p. 205) For 6.41 it is not obvious that a polynomial $q\in\mathcal P_5(\mathbf R)$ represents $\varphi$, since $\cos(\pi t)$ itself is not a polynomial. (p. 205)

**6.42 Riesz representation theorem.** Let $V$ be finite-dimensional and $\varphi\in V'$. Then there is a unique $v\in V$ with $\varphi(u)=\langle u,v\rangle$ for every $u\in V$. (p. 205)
Proof (p. 205):
1. *Existence.* Take an orthonormal basis $e_1,\dots,e_n$. By 6.30(a) and linearity,
$$\varphi(u)=\varphi\big(\langle u,e_1\rangle e_1+\dots+\langle u,e_n\rangle e_n\big)=\langle u,e_1\rangle\varphi(e_1)+\dots+\langle u,e_n\rangle\varphi(e_n)=\big\langle u,\ \overline{\varphi(e_1)}e_1+\dots+\overline{\varphi(e_n)}e_n\big\rangle.$$
So $v=\overline{\varphi(e_1)}e_1+\dots+\overline{\varphi(e_n)}e_n$ (6.43) works.
2. *Uniqueness.* If $\langle u,v_1\rangle=\langle u,v_2\rangle$ for all $u$, then $\langle u,v_1-v_2\rangle=0$ for all $u$. Taking $u=v_1-v_2$ gives $v_1=v_2$.

**6.44 Example.** Find $q\in\mathcal P_2(\mathbf R)$ with $\int_{-1}^1p(t)\cos(\pi t)\,dt=\int_{-1}^1pq$ for all $p\in\mathcal P_2(\mathbf R)$. Here the inner product is the right-hand side (6.45), and $\varphi(p)=\int_{-1}^1p(t)\cos(\pi t)\,dt$. Using 6.43 with the orthonormal basis of 6.34, (p. 206)
$$q(x)=\Big(\int_{-1}^1\sqrt{\tfrac12}\cos(\pi t)dt\Big)\sqrt{\tfrac12}+\Big(\int_{-1}^1\sqrt{\tfrac32}\,t\cos(\pi t)dt\Big)\sqrt{\tfrac32}\,x+\Big(\int_{-1}^1\sqrt{\tfrac{45}8}(t^2-\tfrac13)\cos(\pi t)dt\Big)\sqrt{\tfrac{45}8}(x^2-\tfrac13).$$
"A bit of calculus" gives $q(x)=\frac{15}{2\pi^2}(1-3x^2)$. The same procedure for $\mathcal P_5(\mathbf R)$ gives $q(x)=\frac{105}{8\pi^4}\big((27-2\pi^2)+(24\pi^2-270)x^2+(315-30\pi^2)x^4\big)$. (p. 206)

The vector in 6.43 seems to depend on the chosen orthonormal basis, but by uniqueness (6.42) it does not. (p. 206)

> **Intuition note.** Any linear "measurement" of vectors is just "take the inner product with one special vector". The proof finds that vector by reading off what $\varphi$ does to an orthonormal basis.

Exercises 6B (pp. 207–209) are listed below.

### 6C. Orthogonal Complements and Minimization Problems

#### Orthogonal complements

**6.46 Definition.** For a subset $U\subseteq V$, $U^\perp=\{v\in V:\langle u,v\rangle=0\text{ for every }u\in U\}$. (p. 211)

**6.47 Examples.** (p. 211)
- In $\mathbf R^3$, if $U=\{(2,3,5)\}$, then $U^\perp$ is the plane $2x+3y+5z=0$. If $U$ is that plane, $U^\perp=\{(2t,3t,5t)\}$.
- A plane through the origin has a perpendicular line through the origin as complement, and conversely.
- In $\mathbf F^5$, if $U=\{(a,b,0,0,0)\}$, then $U^\perp=\{(0,0,x,y,z)\}$.
- If $e_1,\dots,e_m,f_1,\dots,f_n$ is an orthonormal basis of $V$, then $(\operatorname{span}(e_1,\dots,e_m))^\perp=\operatorname{span}(f_1,\dots,f_n)$.

**6.48 Properties.** (p. 211; proofs p. 212)
- (a) If $U\subseteq V$ is any subset, $U^\perp$ is a subspace. Proof: $0\in U^\perp$, and $U^\perp$ is closed under addition and under scalar multiplication, using $\langle u,\lambda v\rangle=\bar\lambda\langle u,v\rangle$.
- (b) $\{0\}^\perp=V$.
- (c) $V^\perp=\{0\}$. Reason: $v\in V^\perp$ gives $\langle v,v\rangle=0$.
- (d) $U\cap U^\perp\subseteq\{0\}$.
- (e) If $G\subseteq H$, then $H^\perp\subseteq G^\perp$.

**6.49 $V=U\oplus U^\perp$** if $U$ is a finite-dimensional subspace of $V$. (p. 212) Exercise 16 shows it can fail without finite dimension. (p. 212)
Proof (pp. 212–213):
1. *$V=U+U^\perp$.* Let $e_1,\dots,e_m$ be an orthonormal basis of $U$. Write $v=u+w$ with $u=\langle v,e_1\rangle e_1+\dots+\langle v,e_m\rangle e_m\in U$ and $w=v-u$ (6.50).
2. $\langle w,e_k\rangle=\langle v,e_k\rangle-\langle v,e_k\rangle=0$ for each $k$, so $w\in U^\perp$.
3. By 6.48(d), $U\cap U^\perp=\{0\}$. With step 1 this gives the direct sum (cited as 1.46).

**6.51 Dimension.** For finite-dimensional $V$ and subspace $U$: $\dim U^\perp=\dim V-\dim U$. It follows from 6.49 and 3.94 (cited, not restated). (p. 213)

**6.52 $U=(U^\perp)^\perp$** for finite-dimensional subspace $U$. (p. 213)
Proof (p. 213):
1. $U\subseteq(U^\perp)^\perp$ (6.53). If $u\in U$, then $\langle u,w\rangle=0$ for all $w\in U^\perp$, by the definition of $U^\perp$.
2. Conversely, let $v\in(U^\perp)^\perp$. Write $v=u+w$ with $u\in U$, $w\in U^\perp$ (6.49).
3. Then $v-u=w\in U^\perp$. Also $v-u\in(U^\perp)^\perp$, since $v$ and $u$ are (step 1).
4. So $v-u\in U^\perp\cap(U^\perp)^\perp=\{0\}$ by 6.48(d). Hence $v=u\in U$.

**6.54.** For a finite-dimensional subspace $U$: $U^\perp=\{0\}\iff U=V$. Proof: if $U^\perp=\{0\}$, then $U=(U^\perp)^\perp=\{0\}^\perp=V$. Conversely, $U=V$ gives $U^\perp=\{0\}$ by 6.48(c). The author notes that 6.54 can fail without the finite-dimensional hypothesis (Exercise 16(a)). (p. 214)

**6.55 Definition (orthogonal projection).** For a finite-dimensional subspace $U$, $P_U\in\mathcal L(V)$ is defined by: write $v=u+w$ with $u\in U$, $w\in U^\perp$, and set $P_Uv=u$. It is well defined by the uniqueness in the direct sum (6.49). (p. 214)

**6.56 Example (one-dimensional $U=\operatorname{span}(u)$, $u\neq0$).** $v=\frac{\langle v,u\rangle}{\|u\|^2}u+\Big(v-\frac{\langle v,u\rangle}{\|u\|^2}u\Big)$. The first term lies in $U$ and the second is orthogonal to $u$. So $P_Uv=\frac{\langle v,u\rangle}{\|u\|^2}u$. (p. 214)

**6.57 Properties of $P_U$** ($U$ finite-dimensional). (p. 215)
- (a) $P_U\in\mathcal L(V)$.
- (b) $P_Uu=u$ for $u\in U$.
- (c) $P_Uw=0$ for $w\in U^\perp$.
- (d) $\operatorname{range}P_U=U$.
- (e) $\operatorname{null}P_U=U^\perp$.
- (f) $v-P_Uv\in U^\perp$.
- (g) $P_U^2=P_U$.
- (h) $\|P_Uv\|\le\|v\|$.
- (i) If $e_1,\dots,e_m$ is an orthonormal basis of $U$, then $P_Uv=\langle v,e_1\rangle e_1+\dots+\langle v,e_m\rangle e_m$.

Key proof steps (pp. 215–216):
- (a): decompose $v_1=u_1+w_1$, $v_2=u_2+w_2$. Then $v_1+v_2=(u_1+u_2)+(w_1+w_2)$, and similarly $\lambda v=\lambda u+\lambda w$.
- (b), (c): write $u=u+0$ and $w=0+w$.
- (d): $\operatorname{range}P_U\subseteq U$ by definition and $U\subseteq\operatorname{range}P_U$ by (b).
- (e): $U^\perp\subseteq\operatorname{null}P_U$ by (c). If $P_Uv=0$, the decomposition must be $0+v$, so $v\in U^\perp$.
- (f): $v-P_Uv=w$.
- (g): $P_U(P_Uv)=P_Uu=u$.
- (h): $\|P_Uv\|^2=\|u\|^2\le\|u\|^2+\|w\|^2=\|v\|^2$ by the Pythagorean theorem.
- (i): this is equation 6.50.

> **Intuition note.** $P_U$ keeps the part of $v$ lying in $U$ and discards the part perpendicular to $U$. Applying it twice changes nothing more (g), and it never makes a vector longer (h).

**6.58 Riesz representation theorem, revisited.** For finite-dimensional $V$ and $v\in V$, define $\varphi_v(u)=\langle u,v\rangle$. Then $v\mapsto\varphi_v$ is a one-to-one function from $V$ onto $V'$. (p. 216)

The author proves only "onto" (one-to-one is as in 6.42). The idea: if $\varphi(u)=\langle u,v\rangle$ for all $u$, then $v\in(\operatorname{null}\varphi)^\perp$. This space is one-dimensional unless $\varphi=0$ (from 6.51 and 3.21). Pick a nonzero element and scale it. (p. 216)
Proof of surjectivity (pp. 216–217):
1. If $\varphi=0$, then $\varphi=\varphi_0$. Otherwise $\operatorname{null}\varphi\ne V$, so $(\operatorname{null}\varphi)^\perp\ne\{0\}$ (6.49 with $U=\operatorname{null}\varphi$).
2. Pick $w\in(\operatorname{null}\varphi)^\perp$, $w\ne0$. Set $v=\dfrac{\overline{\varphi(w)}}{\|w\|^2}w$ (6.59). Then $v\in(\operatorname{null}\varphi)^\perp$ and $v\neq0$.
3. Taking norms gives $\|v\|=\frac{|\varphi(w)|}{\|w\|}$ (6.60). Applying $\varphi$ to $v$ gives $\varphi(v)=\frac{|\varphi(w)|^2}{\|w\|^2}=\|v\|^2$.
4. For $u\in V$ write $u=\Big(u-\frac{\varphi(u)}{\varphi(v)}v\Big)+\frac{\varphi(u)}{\|v\|^2}v$. The first term is in $\operatorname{null}\varphi$, so it is orthogonal to $v$.
5. Taking the inner product with $v$: $\langle u,v\rangle=\frac{\varphi(u)}{\|v\|^2}\langle v,v\rangle=\varphi(u)$. So $\varphi=\varphi_v$.

Caution given by the author (p. 216): $v\mapsto\varphi_v$ is linear if $\mathbf F=\mathbf R$. If $\mathbf F=\mathbf C$ it is not linear, because $\varphi_{\lambda v}=\bar\lambda\varphi_v$. Exercise 13 gives yet another proof. (p. 217)

#### Minimization problems

**6.61 Minimizing distance to a subspace.** Let $U$ be a finite-dimensional subspace, $v\in V$, $u\in U$. Then $\|v-P_Uv\|\le\|v-u\|$, with equality if and only if $u=P_Uv$. (p. 217)
Proof (pp. 217–218):
$$\|v-P_Uv\|^2\le\|v-P_Uv\|^2+\|P_Uv-u\|^2=\|(v-P_Uv)+(P_Uv-u)\|^2=\|v-u\|^2\tag{6.62}$$
The first step holds because $0\le\|P_Uv-u\|^2$. The second step uses the Pythagorean theorem. It applies because $v-P_Uv\in U^\perp$ (6.57(f)) and $P_Uv-u\in U$. Equality holds if and only if $\|P_Uv-u\|=0$, i.e. $u=P_Uv$.

> **Intuition note.** The shortest segment from $v$ to a flat subspace $U$ meets $U$ at a right angle. $P_Uv$ is that foot point, and any other point of $U$ is farther by the Pythagorean theorem.

**6.63 Example (approximating sin on $[-\pi,\pi]$).** Find a polynomial $u$ of degree at most 5 minimizing $\int_{-\pi}^{\pi}|\sin x-u(x)|^2dx$. (pp. 218–219)
1. Use $C[-\pi,\pi]$ with $\langle f,g\rangle=\int_{-\pi}^\pi fg$ (6.64), $v(x)=\sin x$, and $U$ the polynomials of degree at most 5. The task is to minimize $\|v-u\|$.
2. Apply Gram–Schmidt to $1,x,\dots,x^5$ to get an orthonormal basis $e_1,\dots,e_6$ of $U$. Compute $P_Uv$ by 6.57(i) with $m=6$. The text says a computer that can integrate is useful.
3. The result is $u(x)=0.987862x-0.155271x^3+0.00564312x^5$ (6.65). The $\pi$'s in the exact answer are replaced by decimals.
4. By 6.61 this is the best approximation in the stated sense. The graph is almost indistinguishable from $\sin x$ on $[-\pi,\pi]$.
5. *Comparison.* The Taylor polynomial $p(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}$ (6.66) is excellent near 0 but poor for $|x|>2$. At $x=3$, 6.65 has error about $0.001$ and the Taylor polynomial about $0.4$.

#### Pseudoinverse

Setting: $T\in\mathcal L(V,W)$, $w\in W$, solve $Tv=w$. If $T$ is invertible, $v=T^{-1}w$. If not, there may be no solution or infinitely many. Two fallback goals: minimize $\|Tv-w\|$ if there is no solution, or minimize $\|v\|$ among solutions if there are many. (p. 220) The proofs below use that $\operatorname{null}T$, $(\operatorname{null}T)^\perp$ and $\operatorname{range}T$ are finite-dimensional when $V$ is. (p. 220)

**6.67.** For finite-dimensional $V$ and $T\in\mathcal L(V,W)$, $T|_{(\operatorname{null}T)^\perp}$ is an injective map of $(\operatorname{null}T)^\perp$ onto $\operatorname{range}T$. (p. 220)
Proof (p. 220):
1. *Injective.* If $v\in(\operatorname{null}T)^\perp$ and $Tv=0$, then $v\in\operatorname{null}T\cap(\operatorname{null}T)^\perp=\{0\}$.
2. *Onto.* Let $w=Tv\in\operatorname{range}T$. Write $v=u+x$ with $u\in\operatorname{null}T$, $x\in(\operatorname{null}T)^\perp$ (6.49).
3. Then $T|_{(\operatorname{null}T)^\perp}x=Tx=Tv-Tu=w-0=w$.

**6.68 Definition (pseudoinverse).** For finite-dimensional $V$ and $T\in\mathcal L(V,W)$, $T^\dagger\in\mathcal L(W,V)$ is
$$T^\dagger w=\big(T|_{(\operatorname{null}T)^\perp}\big)^{-1}P_{\operatorname{range}T}\,w.$$
So $T^\dagger w=0$ if $w\in(\operatorname{range}T)^\perp$. If $w\in\operatorname{range}T$, then $T^\dagger w$ is the unique element of $(\operatorname{null}T)^\perp$ with $T(T^\dagger w)=w$. It is also called the Moore–Penrose inverse. (p. 221)

**6.69 Algebraic properties.** (p. 221)
- (a) If $T$ is invertible, $T^\dagger=T^{-1}$.
- (b) $TT^\dagger=P_{\operatorname{range}T}$.
- (c) $T^\dagger T=P_{(\operatorname{null}T)^\perp}$.

Proof (p. 221):
- (a) Here $(\operatorname{null}T)^\perp=V$ and $\operatorname{range}T=W$. So $T|_{(\operatorname{null}T)^\perp}=T$ and $P_{\operatorname{range}T}=I$.
- (b) For $w\in\operatorname{range}T$: $TT^\dagger w=T(T|_{(\operatorname{null}T)^\perp})^{-1}w=w=P_{\operatorname{range}T}w$. For $w\in(\operatorname{range}T)^\perp$: both sides are 0. The two maps agree on $\operatorname{range}T$ and on its complement, so they are equal (by 6.49).
- (c) For $v\in(\operatorname{null}T)^\perp$: $T^\dagger(Tv)=(T|_{(\operatorname{null}T)^\perp})^{-1}(Tv)=v$. For $v\in\operatorname{null}T$: both sides are 0.

Consequences: if $T$ is surjective, $TT^\dagger=I_W$; if injective, $T^\dagger T=I_V$. (p. 221)

**6.70 Best approximate solution.** Let $V$ be finite-dimensional, $T\in\mathcal L(V,W)$, $w\in W$. (p. 222)
- (a) For $v\in V$, $\|T(T^\dagger w)-w\|\le\|Tv-w\|$, with equality if and only if $v\in T^\dagger w+\operatorname{null}T$.
- (b) If $v\in T^\dagger w+\operatorname{null}T$, then $\|T^\dagger w\|\le\|v\|$, with equality if and only if $v=T^\dagger w$.

Proof (p. 222):
- (a) Write $Tv-w=(Tv-TT^\dagger w)+(TT^\dagger w-w)$. The first term is in $\operatorname{range}T$. Since $TT^\dagger$ is the projection onto $\operatorname{range}T$ (6.69(b)), the second term is in $(\operatorname{range}T)^\perp$ (6.57(f)). Pythagoras gives the inequality, with equality iff the first term is 0, i.e. $v-T^\dagger w\in\operatorname{null}T$.
- (b) $v=(v-T^\dagger w)+T^\dagger w$ with $v-T^\dagger w\in\operatorname{null}T$ and $T^\dagger w\in(\operatorname{null}T)^\perp$. Apply Pythagoras.

A formula for $T^\dagger$ is promised in the next chapter (7.78). (p. 222)

> **Intuition note.** To solve $Tv=w$ when you cannot: first project $w$ onto the reachable set $\operatorname{range}T$, since that is the closest reachable target. Then solve exactly, but only inside $(\operatorname{null}T)^\perp$. The directions $T$ destroys are set to zero, so the answer is as short as possible.

**6.71 Example.** $T\in\mathcal L(\mathbf F^4,\mathbf F^3)$, $T(a,b,c,d)=(a+b+c,2c+d,0)$, neither injective nor surjective. (p. 223)
1. $\operatorname{range}T=\{(x,y,0)\}$, so $P_{\operatorname{range}T}(x,y,z)=(x,y,0)$.
2. $\operatorname{null}T=\{a+b+c=0,\ 2c+d=0\}$ has basis $(-1,1,0,0),(-1,0,1,-2)$, because $(a,b,c,d)=b(-1,1,0,0)+c(-1,0,1,-2)$.
3. $T^\dagger(x,y,z)=(T|_{(\operatorname{null}T)^\perp})^{-1}(x,y,0)$ (6.72). This is the $(a,b,c,d)$ with $T(a,b,c,d)=(x,y,0)$ that is orthogonal to both null-space basis vectors:
$$a+b+c=x,\quad 2c+d=y,\quad -a+b=0,\quad -a+c-2d=0.$$
4. Solving: $a=b=\frac1{11}(5x-2y)$, $c=\frac1{11}(x+4y)$, $d=\frac1{11}(-2x+3y)$. So $T^\dagger(x,y,z)=\frac1{11}(5x-2y,\,5x-2y,\,x+4y,\,-2x+3y)$.
5. Then $TT^\dagger(x,y,z)=(x,y,0)$, which illustrates $TT^\dagger=P_{\operatorname{range}T}$.

### Exercises
Exercises 6B (pp. 207–209) and 6C (pp. 224–226) are listed in "Exercises worth doing" below.

## Toy example (ours)
Find the point of $U=\operatorname{span}(v_1,v_2)\subset\mathbf R^3$, $v_1=(1,1,0)$, $v_2=(1,0,1)$, closest to $v=(1,2,3)$.

*Gram–Schmidt (6.32).*
- $f_1=(1,1,0)$, $\|f_1\|^2=2$.
- $\langle v_2,f_1\rangle=1$, so $f_2=(1,0,1)-\frac12(1,1,0)=(\frac12,-\frac12,1)$. Then $\|f_2\|^2=\frac14+\frac14+1=\frac32$.

*Projection (6.57(i), written with the $f$'s, since $\langle v,e_k\rangle e_k=\frac{\langle v,f_k\rangle}{\|f_k\|^2}f_k$).*
- $\langle v,f_1\rangle=3$, giving $\frac32(1,1,0)=(\frac32,\frac32,0)$.
- $\langle v,f_2\rangle=\frac12-1+3=\frac52$, and $\frac{5/2}{3/2}=\frac53$, giving $\frac53(\frac12,-\frac12,1)=(\frac56,-\frac56,\frac53)$.
- $P_Uv=(\frac32+\frac56,\ \frac32-\frac56,\ \frac53)=(\frac73,\frac23,\frac53)$.

*Checks.*
- $v-P_Uv=(-\frac43,\frac43,\frac43)$. Its inner product with $v_1$ is $-\frac43+\frac43=0$, and with $v_2$ is $-\frac43+\frac43=0$, so it lies in $U^\perp$.
- $\|v\|^2=14$, $\|P_Uv\|^2=\frac{49+4+25}9=\frac{26}3$, $\|v-P_Uv\|^2=\frac{16}3$. Indeed $\frac{26}3+\frac{16}3=14$.
- Another point of $U$: $u=v_1+v_2=(2,1,1)$ gives $\|v-u\|^2=\|(-1,1,2)\|^2=6>\frac{16}3$, as 6.61 predicts.

## Concepts
- [[orthogonality]] — inner product zero; here extended to sets via $U^\perp$ (p. 211)
- [[orthonormal-basis]] — orthonormal list that is a basis; gives coordinates $\langle v,e_k\rangle$ (pp. 197, 199, 200)
- [[gram-schmidt-and-qr]] — procedure 6.32 turning an independent list into an orthonormal one with the same nested spans; QR itself is not in these pages (p. 201)
- [[bessel-inequality]] (new) — $\sum|\langle v,e_k\rangle|^2\le\|v\|^2$ for an orthonormal list (p. 198)
- [[parseval-identity]] (new) — equality $\|v\|^2=\sum|\langle v,e_k\rangle|^2$ for an orthonormal basis (p. 200)
- [[orthogonal-complement]] (new) — $U^\perp$, all vectors orthogonal to every vector of $U$; $V=U\oplus U^\perp$ for finite-dimensional $U$ (pp. 211–213)
- [[projection]] — here $P_U$, defined via $V=U\oplus U^\perp$; $P_U v$ is the closest point of $U$ to $v$ (pp. 214–217)
- [[least-squares]] — only the minimization-in-norm idea appears (6.61, 6.70, sine approximation); normal equations are not stated here (pp. 217, 222)
- [[linear-functional-dual-space]] (new) — linear map $V\to\mathbf F$; $V'$ is the space of all of them (p. 204)
- [[riesz-representation-theorem]] (new) — every functional on finite-dimensional $V$ is $\langle\cdot,v\rangle$ for a unique $v$ (pp. 205, 216)
- [[schur-theorem]] (new) — complex operators are upper triangular in some orthonormal basis (p. 204)
- [[pseudoinverse]] — $T^\dagger=(T|_{(\operatorname{null}T)^\perp})^{-1}P_{\operatorname{range}T}$; best-fit, minimum-norm solution (pp. 221–222)
- [[null-space]] / [[column-space]] — appear as $\operatorname{null}T$ and $\operatorname{range}T$ and their complements (p. 220)

## Canonical instances
- [[fourier-orthonormal-list]] — sines and cosines are orthonormal in $C[-\pi,\pi]$ (p. 197)
- [[orthonormal-basis-of-P2]] — Gram–Schmidt on $1,x,x^2$ with $\int_{-1}^1$ (p. 202)
- [[sine-polynomial-approximation]] — best degree-5 approximation of $\sin$ via $P_U$, versus Taylor (pp. 218–219)
- [[riesz-polynomial-example]] — $q=\frac{15}{2\pi^2}(1-3x^2)$ represents the cosine integral on $\mathcal P_2$ (p. 206)
- [[pseudoinverse-F4-to-F3]] — worked $T^\dagger$ for $T(a,b,c,d)=(a+b+c,2c+d,0)$ (p. 223)
- [[orthonormal-coordinates-example-F4]] — expansion of $(1,2,4,7)$ in a $\pm\frac12$ orthonormal basis (p. 200)

## Bridges (candidates)
- [same-math] Gram–Schmidt (6.32) ↔ linear-algebra: QR factorization — orthonormalising the columns of an independent list gives the $Q$ factor (the text itself does not state QR).
- [same-math] Minimizing $\|v-u\|$ over $u\in U$ via $P_U$ ↔ statistics: least-squares fit — the same projection onto a subspace (normal equations are not in this unit).
- [same-math] Pseudoinverse $T^\dagger$ (6.68) ↔ linear-algebra: $A^+=V\Sigma^+U^\top$ of the concept list — same operator. The SVD formula is not in this unit; the author points to 7.78.
- [structural-analogy] Parseval/Bessel with Fourier orthonormal lists ↔ signal processing: energy splits across frequency components — an analogy only.
- [structural-analogy] Best polynomial approximation as projection ↔ machine learning: regression on basis functions.

## Questions this raises
- What does the formula for $T^\dagger$ promised in 7.78 look like, and how does it relate to singular values?
- Without finite dimension, which parts of $V=U\oplus U^\perp$ and Riesz survive? Exercises 16 and 22 show failures; what extra hypotheses repair them?
- Gram–Schmidt on a nearly dependent list divides by a tiny $\|f_k\|$. How reliable is it numerically? (Exercise 13 shows $f_k=0$ detects dependence, but numerical behaviour is not discussed here.)
- Why is the projection-based best polynomial so much better than the Taylor polynomial away from 0? The text states the numbers but gives no general explanation.

## Exercises worth doing
- Ex. 6B.1 (p. 207) — converse of 6.24: norm identity for all coefficients forces orthonormality — difficulty: medium
- Ex. 6B.13 (p. 209) — a list is dependent iff Gram–Schmidt gives some $f_k=0$; a dependence test without elimination — difficulty: medium
- Ex. 6B.22 (p. 210) — evaluation at 0 on $C[-1,1]$ has no Riesz vector, so finite dimension is needed — difficulty: hard
- Ex. 6C.8 (p. 224) — Riesz on the subspace $U$ gives $P_Uv$ — difficulty: medium
- Ex. 6C.15 (p. 225) — compute a closest point in $\mathbf R^4$ to $(1,2,3,4)$ — difficulty: easy
- Ex. 6C.21 (p. 226) — compute $T^\dagger$ for $T(a,b,c)=(a+b+c,2b+3c)$ and verify 6.69(b),(c) — difficulty: medium
- Ex. 6C.22 (p. 226) — prove $TT^\dagger T=T$ and $T^\dagger TT^\dagger=T^\dagger$ — difficulty: medium

## Reading notes
- This part starts at printed p. 197 (beginning of Section 6B, "Orthonormal Bases") and ends at printed p. 226 (last of Exercises 6C). The preceding part of Chapter 6 is not included. Split at a section boundary.
- Page offset: printed = pdf − 14 (the labels give printed numbers).
- The extracted text layer shows math letters as "��". All formulas were checked against the page images.
- On p. 197 the text layer garbles the square roots in 6.23(e). The image shows $\sqrt{3/2}\,x$ and $\sqrt{5/2}\,x^2$.
- Sidebars appear on pp. 200, 204, 205, 214, 216, 217, 218, 220 and 221 (Parseval 1799; Gram and Schmidt; Schur 1909; Riesz; a remark that Exercise 16(a) shows 6.54 fails without finite dimension; the caution on $v\mapsto\varphi_v$; a remark on applications; a figure caption and a remark about computers; the TeX note; the Moore–Penrose name). Page 210 ends with a boxed sidebar quoting a Supreme Court exchange about "orthogonal". The Supreme Court box is not mathematical content.
- 6.28, 6.36, 6.37, 6.38, 6.49, 6.51 and 6.58 rely on results from earlier chapters (2.38, 2.32, 5.39, 5.44, 4.13, 1.46, 3.94, 3.21) that are cited but not stated here. I did not restate them beyond what the text says.
- I found no misprints in these pages. Solutions to exercises are not printed.
