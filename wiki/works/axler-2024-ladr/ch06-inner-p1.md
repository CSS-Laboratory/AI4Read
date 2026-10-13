---
id: axler-2024-ladr/ch06-inner-p1
work: axler-2024-ladr
unit: "6 Inner Product Spaces (part 1/2): chapter opening and 6A Inner Products and Norms"
pages: 181–196
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Inner Products and Norms (Axler, Ch. 6, opening and §6A)

## L0 — One line
An inner product is an abstract "dot product" on any real or complex vector space. It gives every vector a length (norm) and a notion of perpendicularity (orthogonality), and from its axioms the Pythagorean theorem, Cauchy–Schwarz, the triangle inequality and the parallelogram equality all follow.

## L1 — The gist (≤ 120 words)
Plain vector spaces have addition and scaling but no length or angle. This unit asks how to add these features in a way that works over both $\mathbf R$ and $\mathbf C$. The answer is the inner product $\langle u,v\rangle$, defined by five axioms (positivity, definiteness, additivity and homogeneity in the first slot, conjugate symmetry). The norm is $\|v\|=\sqrt{\langle v,v\rangle}$. Two vectors are orthogonal when $\langle u,v\rangle=0$. Orthogonal vectors satisfy the Pythagorean theorem. Splitting $u$ into a multiple of $v$ plus a vector orthogonal to $v$ gives the Cauchy–Schwarz inequality, which gives the triangle inequality; the parallelogram equality comes from expanding inner products. All hold in any inner product space. The unit's exercises (6A) are listed but not solved.

**Prerequisites:** vector spaces over $\mathbf F$; linear maps; complex conjugate and absolute value; the real dot product; basic integrals.

## L2 — Key ideas
- The dot product on $\mathbf R^n$ has four properties ($x\cdot x\ge0$; $x\cdot x=0$ iff $x=0$; linear in $x$ for fixed $y$; symmetric). Axler abstracts these into the inner product, with a complex conjugate so the same definition works over $\mathbf C$ (pp. 182–183).
- Inner products exist on many spaces, not only $\mathbf F^n$. Examples are weighted sums, integrals of products of functions, and polynomial spaces (6.3, p. 184).
- Every inner product determines a norm $\|v\|=\sqrt{\langle v,v\rangle}$. It satisfies $\|\lambda v\|=|\lambda|\,\|v\|$, and $\|v\|=0$ if and only if $v=0$ (6.7, 6.9, p. 186).
- Orthogonal means $\langle u,v\rangle=0$. For nonzero vectors in $\mathbf R^2$ this is the usual perpendicularity, via a cosine formula that Axler leaves to Exercise 15 (p. 187).
- Orthogonal vectors satisfy the Pythagorean theorem in any inner product space (6.12, p. 187).
- A vector $u$ can be written as a multiple of $v\neq0$ plus a part orthogonal to $v$ (6.13, p. 188). This decomposition, together with the Pythagorean theorem, proves Cauchy–Schwarz, including its equality case (6.14, p. 189).
- Cauchy–Schwarz gives the triangle inequality, with equality exactly when one vector is a nonnegative real multiple of the other (6.17, p. 190).
- The parallelogram equality $\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$ follows by expanding inner products (6.21, p. 191).

## L3 — Walkthrough

### Chapter opening (p. 181)
Vector spaces generalize the addition and scaling of $\mathbf R^2,\mathbf R^3$ but ignore length and angle. Inner products bring these back (p. 181). The chapter also promises orthonormal bases, Gram–Schmidt and minimization problems. These lie beyond the pages of this part. Standing assumption: $\mathbf F$ is $\mathbf R$ or $\mathbf C$; $V,W$ are vector spaces over $\mathbf F$ (p. 181).

### 6A. Inner Products

**Motivation in $\mathbf R^n$ (p. 182).**
- The norm of $x=(x_1,\dots,x_n)\in\mathbf R^n$ is $\|x\|=\sqrt{x_1^2+\cdots+x_n^2}$ (length of an arrow from the origin, or distance from the origin to the point). It is not linear (p. 182).
- **6.1 Dot product.** $x\cdot y=x_1y_1+\cdots+x_ny_n$ (a number, not a vector). Then $x\cdot x=\|x\|^2$ (p. 182).
- Properties:
  - $x\cdot x\ge0$.
  - $x\cdot x=0$ iff $x=0$.
  - For fixed $y$, $x\mapsto x\cdot y$ is linear.
  - $x\cdot y=y\cdot x$.
- For real spaces, the inner product simply abstracts these four properties (p. 182).

**Complex case (p. 183).**
- For $\lambda=a+bi$: $|\lambda|=\sqrt{a^2+b^2}$, $\bar\lambda=a-bi$, and $|\lambda|^2=\lambda\bar\lambda$.
- For $z\in\mathbf C^n$, $\|z\|=\sqrt{|z_1|^2+\cdots+|z_n|^2}$. The absolute values keep the norm nonnegative. Also $\|z\|^2=z_1\bar z_1+\cdots+z_n\bar z_n$.
- So the inner product of $w$ with $z$ should be $w_1\bar z_1+\cdots+w_n\bar z_n$. Swapping the roles of $w,z$ gives the complex conjugate of this expression (p. 183).
- For $\lambda\in\mathbf C$, "$\lambda\ge0$" means $\lambda$ is real and nonnegative (p. 183).

**6.2 Definition (inner product).** A function taking each ordered pair $(u,v)\in V\times V$ to a number $\langle u,v\rangle\in\mathbf F$, with (p. 183):
- positivity: $\langle v,v\rangle\ge0$;
- definiteness: $\langle v,v\rangle=0$ iff $v=0$;
- additivity in first slot: $\langle u+v,w\rangle=\langle u,w\rangle+\langle v,w\rangle$;
- homogeneity in first slot: $\langle\lambda u,v\rangle=\lambda\langle u,v\rangle$;
- conjugate symmetry: $\langle u,v\rangle=\overline{\langle v,u\rangle}$.

In real spaces the conjugate can be dropped (p. 184). Margin note: many physicists require homogeneity in the second slot instead of the first (p. 184).

**6.3 Examples (p. 184).**
- (a) Euclidean inner product on $\mathbf F^n$: $\langle(w_1,\dots,w_n),(z_1,\dots,z_n)\rangle=w_1\bar z_1+\cdots+w_n\bar z_n$.
- (b) With positive $c_1,\dots,c_n$: $\langle w,z\rangle=c_1w_1\bar z_1+\cdots+c_nw_n\bar z_n$.
- (c) On continuous real-valued functions on $[-1,1]$: $\langle f,g\rangle=\int_{-1}^1 fg$.
- (d) On $\mathcal P(\mathbf R)$: $\langle p,q\rangle=p(0)q(0)+\int_{-1}^1p'q'$.
- (e) On $\mathcal P(\mathbf R)$: $\langle p,q\rangle=\int_0^\infty p(x)q(x)e^{-x}\,dx$.

**6.4 Inner product space:** a vector space $V$ together with an inner product on $V$. $\mathbf F^n$ is assumed to carry the Euclidean inner product unless stated otherwise (p. 184).

**6.5 Notation:** for the rest of this chapter and the next, $V,W$ denote inner product spaces over $\mathbf F$ (p. 185).

**6.6 Basic properties (p. 185).**
- (a) For fixed $v$, $u\mapsto\langle u,v\rangle$ is a linear map $V\to\mathbf F$.
- (b) $\langle0,v\rangle=0$.
- (c) $\langle v,0\rangle=0$.
- (d) $\langle u,v+w\rangle=\langle u,v\rangle+\langle u,w\rangle$.
- (e) $\langle u,\lambda v\rangle=\bar\lambda\langle u,v\rangle$.

Proofs:
- (a) is first-slot additivity and homogeneity.
- (b) holds because linear maps send $0$ to $0$.
- (c) $\langle v,0\rangle=\overline{\langle0,v\rangle}=\bar0=0$.
- (d) $\langle u,v+w\rangle=\overline{\langle v+w,u\rangle}=\overline{\langle v,u\rangle}+\overline{\langle w,u\rangle}=\langle u,v\rangle+\langle u,w\rangle$.
- (e) $\langle u,\lambda v\rangle=\overline{\langle\lambda v,u\rangle}=\overline{\lambda\langle v,u\rangle}=\bar\lambda\,\overline{\langle v,u\rangle}=\bar\lambda\langle u,v\rangle$.

*Intuition note.* The inner product is linear in the first slot, but conjugate-linear in the second slot (a scalar comes out conjugated). Over $\mathbf R$ the conjugate does nothing, so it is linear in both slots.

### Norms (p. 186)
**6.7 Definition.** $\|v\|=\sqrt{\langle v,v\rangle}$.
- **6.8 Examples.** In $\mathbf F^n$, $\|(z_1,\dots,z_n)\|=\sqrt{|z_1|^2+\cdots+|z_n|^2}$. For $f$ in 6.3(c), $\|f\|=\sqrt{\int_{-1}^1f^2}$.
- **6.9 Properties.** (a) $\|v\|=0$ iff $v=0$ (from definiteness). (b) $\|\lambda v\|=|\lambda|\,\|v\|$, because
$$\|\lambda v\|^2=\langle\lambda v,\lambda v\rangle=\lambda\langle v,\lambda v\rangle=\lambda\bar\lambda\langle v,v\rangle=|\lambda|^2\|v\|^2,$$
then take square roots.
- Principle: working with norms squared is usually easier than with norms (p. 186).

### Orthogonality (p. 187)
**6.10 Definition.** $u,v$ are *orthogonal* if $\langle u,v\rangle=0$. The order does not matter, since $\langle u,v\rangle=0$ iff $\langle v,u\rangle=0$.
- Exercise 15 (not proved here) asks to show that for nonzero $u,v\in\mathbf R^2$, $\langle u,v\rangle=\|u\|\|v\|\cos\theta$. Hence nonzero vectors in $\mathbf R^2$ are orthogonal iff they are perpendicular in the usual sense (p. 187).
- **6.11** (a) $0$ is orthogonal to every vector (by 6.6(b)). (b) $0$ is the only vector orthogonal to itself (by definiteness).

**6.12 Pythagorean theorem.** If $u,v$ are orthogonal, then $\|u+v\|^2=\|u\|^2+\|v\|^2$.

Proof, given $\langle u,v\rangle=0$ (and hence $\langle v,u\rangle=0$):
$$\|u+v\|^2=\langle u+v,u+v\rangle=\langle u,u\rangle+\langle u,v\rangle+\langle v,u\rangle+\langle v,v\rangle=\|u\|^2+\|v\|^2.$$

**6.13 Orthogonal decomposition (p. 188).** Let $u,v\in V$, $v\ne0$.
- Write $u=cv+(u-cv)$ and require $\langle u-cv,v\rangle=0$.
- This reads $0=\langle u,v\rangle-c\|v\|^2$, so $c=\langle u,v\rangle/\|v\|^2$.
- With $c=\dfrac{\langle u,v\rangle}{\|v\|^2}$ and $w=u-\dfrac{\langle u,v\rangle}{\|v\|^2}v$: $u=cv+w$ and $\langle w,v\rangle=0$.

*Intuition note.* Any $u$ splits into a piece along $v$ and a piece at "right angles" to $v$. The coefficient $c$ is forced by the orthogonality requirement.

### Cauchy–Schwarz (p. 189)
**6.14.** $|\langle u,v\rangle|\le\|u\|\|v\|$. Equality holds iff one of $u,v$ is a scalar multiple of the other.

Proof:
- If $v=0$, both sides are $0$. Otherwise use 6.13 and the Pythagorean theorem ($cv\perp w$):
$$\|u\|^2=\Big\|\tfrac{\langle u,v\rangle}{\|v\|^2}v\Big\|^2+\|w\|^2=\frac{|\langle u,v\rangle|^2}{\|v\|^2}+\|w\|^2\ \ge\ \frac{|\langle u,v\rangle|^2}{\|v\|^2}.\tag{6.15}$$
- Multiply by $\|v\|^2$ and take square roots.
- Equality in 6.14 holds iff equality holds in 6.15, i.e. iff $w=0$. By 6.13 that holds iff $u$ is a multiple of $v$. The phrasing "one is a multiple of the other" covers the cases where $u$ or $v$ is $0$ (p. 189).

**6.16 Examples.**
- (a) For real $x_j,y_j$: $(x_1y_1+\cdots+x_ny_n)^2\le(x_1^2+\cdots+x_n^2)(y_1^2+\cdots+y_n^2)$.
- (b) For continuous real $f,g$ on $[-1,1]$: $\big|\int_{-1}^1fg\big|^2\le\big(\int_{-1}^1f^2\big)\big(\int_{-1}^1g^2\big)$.

*Intuition note.* The part of $u$ along $v$ is never longer than $u$ itself. Equality occurs only when nothing of $u$ is left over, i.e. $u$ lies along $v$.

### Triangle inequality (p. 190)
**6.17.** $\|u+v\|\le\|u\|+\|v\|$. Equality holds iff one of $u,v$ is a nonnegative real multiple of the other.

Proof:
$$\begin{aligned}\|u+v\|^2&=\langle u+v,u+v\rangle=\langle u,u\rangle+\langle v,v\rangle+\langle u,v\rangle+\langle v,u\rangle\\&=\langle u,u\rangle+\langle v,v\rangle+\langle u,v\rangle+\overline{\langle u,v\rangle}=\|u\|^2+\|v\|^2+2\,\mathrm{Re}\langle u,v\rangle\\&\le\|u\|^2+\|v\|^2+2|\langle u,v\rangle|\qquad(6.18)\\&\le\|u\|^2+\|v\|^2+2\|u\|\|v\|\qquad(6.19)\\&=(\|u\|+\|v\|)^2.\end{aligned}$$
Step 6.19 is Cauchy–Schwarz; then take square roots.

Equality case: equality needs equality in 6.18 and 6.19, i.e.
$$\langle u,v\rangle=\|u\|\|v\|.\tag{6.20}$$
- If one vector is a nonnegative real multiple of the other, 6.20 holds.
- Conversely, 6.20 gives equality in Cauchy–Schwarz, so one vector is a scalar multiple of the other. By 6.20 that scalar must be a nonnegative real number (p. 190).

The text notes that the triangle inequality implies the shortest polygonal path between two points is a single segment. The reverse triangle inequality is Exercise 20 (p. 190).

### Parallelogram equality (p. 191)
**6.21.** $\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$.

Proof: expand both inner products. The cross terms $\pm\langle u,v\rangle\pm\langle v,u\rangle$ cancel:
$$\|u\|^2+\|v\|^2+\langle u,v\rangle+\langle v,u\rangle+\|u\|^2+\|v\|^2-\langle u,v\rangle-\langle v,u\rangle=2(\|u\|^2+\|v\|^2).$$
Geometric meaning: the sum of the squared diagonal lengths equals the sum of the squared lengths of the four sides (p. 191).

### Exercises 6A (pp. 191–196)
Thirty-five exercises are printed; they are not solved here (see "Exercises worth doing").

## Toy example (ours)
In $\mathbf R^2$ with the dot product, take $u=(4,2)$, $v=(1,1)$.
- $\langle u,v\rangle=4\cdot1+2\cdot1=6$; $\|v\|^2=1+1=2$; so $c=6/2=3$.
- $cv=(3,3)$, $w=u-cv=(1,-1)$. Check: $\langle w,v\rangle=1-1=0$, so $w\perp v$.
- Pythagoras: $\|u\|^2=16+4=20$; $\|cv\|^2=9+9=18$; $\|w\|^2=1+1=2$; and $18+2=20$ ✓.
- 6.15: $|\langle u,v\rangle|^2/\|v\|^2=36/2=18\le20$ ✓.
- Cauchy–Schwarz: $6\le\sqrt{20}\sqrt2=\sqrt{40}\approx6.32$ ✓. Strict, because $w\ne0$.
- Parallelogram: $u+v=(5,3)$, $\|u+v\|^2=34$; $u-v=(3,1)$, $\|u-v\|^2=10$; sum $44$; and $2(20+2)=44$ ✓.

## Concepts
- [[inner-product]] — $\langle u,v\rangle$ obeying the five axioms of 6.2; first-slot linear, conjugate symmetric (p. 183). Generalizes the dot product (p. 182).
- [[inner-product-space]] (new) — vector space plus a chosen inner product (p. 184).
- [[norm]] — here $\|v\|=\sqrt{\langle v,v\rangle}$, the norm induced by an inner product (p. 186).
- [[orthogonality]] — $\langle u,v\rangle=0$ (p. 187).
- [[conjugate-symmetry]] (new) — $\langle u,v\rangle=\overline{\langle v,u\rangle}$; makes the definition work over $\mathbf C$ (p. 183).
- [[pythagorean-theorem-inner-product]] (new) — orthogonal $u,v$ give $\|u+v\|^2=\|u\|^2+\|v\|^2$ (p. 187).
- [[orthogonal-decomposition]] (new) — $u=cv+w$ with $c=\langle u,v\rangle/\|v\|^2$, $w\perp v$ (p. 188).
- [[cauchy-schwarz-inequality]] (new) — $|\langle u,v\rangle|\le\|u\|\|v\|$ (p. 189).
- [[triangle-inequality]] (new) — $\|u+v\|\le\|u\|+\|v\|$ (p. 190).
- [[parallelogram-equality]] (new) — $\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$ (p. 191).

## Canonical instances
- [[euclidean-inner-product]] — $\sum w_k\bar z_k$ on $\mathbf F^n$ (p. 184).
- [[function-space-inner-product]] — $\int_{-1}^1fg$ on continuous functions (p. 184).
- [[weighted-inner-product]] — positive weights $c_k$ on $\mathbf F^n$ (p. 184).

## Bridges (candidates)
- [structural-analogy] Cauchy–Schwarz on $\mathbf R^n$ and on $\int fg$ ↔ statistics: the same inequality bounds a correlation-like ratio — only the pairing differs.
- [same-math] Orthogonal decomposition 6.13 ↔ projection: the coefficient $c=\langle u,v\rangle/\|v\|^2$ is the projection of $u$ onto the line spanned by $v$.
- [structural-analogy] Cosine formula (Ex. 15) and the angle definition in Ex. 16 ↔ cosine similarity of embeddings: $\langle x,y\rangle/(\|x\|\|y\|)$.

## Questions this raises
- Which norms come from an inner product? (Exercises 24, 25 and 28 explore this via the parallelogram equality.)
- How do we recover the inner product from the norm (Exercises 26, 27)?
- What happens when we take several mutually orthogonal vectors rather than one (the chapter's orthonormal bases)?
- Why is the conjugate placed on the second slot, and what changes under the physicists' convention?

## Exercises worth doing
- Ex. 2 (p. 191) — when $\langle Su,Sv\rangle$ is an inner product, iff $S$ is injective — difficulty: easy
- Ex. 15 (p. 192) — dot product equals $\|u\|\|v\|\cos\theta$ in $\mathbf R^2$, via the law of cosines — difficulty: medium
- Ex. 16 (p. 193) — why Cauchy–Schwarz is needed for the angle in $\mathbf R^n$ to make sense — difficulty: easy
- Ex. 26–27 (p. 194) — recover the inner product from norms — difficulty: medium
- Ex. 25 (p. 194) — the $p$-norm on $\mathbf R^2$ comes from an inner product iff $p=2$ — difficulty: hard
- Ex. 28 (p. 194) — a norm satisfying the parallelogram equality comes from an inner product — difficulty: hard

## Reading notes
- This part covers the chapter opening (p. 181) through the end of Section 6A, including all of Exercises 6A (pp. 191–196).
- Printed page = pdf page − 14.
- Page 196 ends with an AI-written sonnet about Cauchy–Schwarz; it contains no mathematics.
- Page 181 shows an epigraph photo caption about the George Peabody Library and Sylvester; it is not mathematical content and is skipped.
- The historical remarks on pp. 187 and 189 (Greek origin of "orthogonal"; Babylonian/Greek history of the Pythagorean theorem; Cauchy/Bunyakovsky/Schwarz history) are not digested. The physicists' convention noted on p. 184 is mentioned in L3.
