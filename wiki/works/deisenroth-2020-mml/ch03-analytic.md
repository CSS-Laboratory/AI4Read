---
id: deisenroth-2020-mml/ch03-analytic
work: deisenroth-2020-mml
unit: "3 Analytic Geometry"
pages: 70-97
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Analytic Geometry (MML, Chapter 3)

## L0 — One line
An inner product on a vector space defines lengths, distances, angles and orthogonality, and orthogonal projection onto a subspace (via the normal equation) is a central application built on them.

## L1 — The gist (≤ 120 words)
Chapter 2 treated vector spaces abstractly. This chapter asks how to add geometry: lengths, distances, angles. The answer is to choose an inner product, a symmetric, positive definite bilinear map (linear in each argument; $\langle x,x\rangle>0$ for $x\ne0$). It induces a norm, a distance and an angle. Different inner products give different geometry, so orthogonality depends on the choice. Orthogonal matrices preserve lengths and angles (for the dot product); rotations are examples. Orthogonal projection finds the point of a subspace closest to a vector. It is computed through the normal equation (a linear system for the coordinates), and Gram–Schmidt (orthogonalising a basis) is built from it. The chapter says projections underlie PCA (principal component analysis), regression and classification.

**Prerequisites:** vectors and matrices (transpose, inverse), basis and linear independence, null space, basic trigonometry, a definite integral.

## L2 — Key ideas
- A norm satisfies absolute homogeneity, the triangle inequality and positive definiteness; ℓ1 and ℓ2 are examples (p. 71–72).
- Inner product = symmetric, positive definite bilinear map. In a basis it equals $\hat x^\top A\hat y$ with $A$ symmetric positive definite, and this is an "if and only if" (Theorem 3.5) (p. 73–74).
- Every inner product induces a norm, a distance and an angle. Not every norm comes from an inner product; ℓ1 does not (p. 75–76).
- Orthogonality is relative to the chosen inner product. Orthogonal matrices ($A^{-1}=A^\top$) preserve lengths and angles for the dot product (p. 77–78).
- Orthonormal bases, orthogonal complements and the inner product of functions extend these ideas (p. 79–81).
- Projection onto a subspace spanned by the columns of $B$ is $P_\pi = B(B^\top B)^{-1}B^\top$, from the normal equation $B^\top B\lambda = B^\top x$ (p. 86–87).
- Projection solves unsolvable $Ax=b$ approximately (least squares). With an orthonormal basis (ONB) it simplifies to $BB^\top x$ (p. 88).
- Gram–Schmidt turns any basis into an orthogonal one by subtracting projections. Affine projection (onto a shifted subspace) works by subtracting and re-adding a support point, the shift vector (p. 89–90).
- Rotations are orthogonal matrices; Givens rotations (rotations in one coordinate plane, fixing the other coordinates) generalise them to $n$ dimensions. Rotations commute in 2D, but generally not in 3D or higher (p. 91–94).

## L3 — Walkthrough

### Introduction (p. 70)
Inner products induce norms and metrics, which capture similarity and distance; the book uses this for the support vector machine (Ch. 12). Lengths and angles lead to orthogonal projections, used in PCA (Ch. 10) and maximum-likelihood regression (Ch. 9) (p. 70).

### 3.1 Norms (p. 71–72)
**Definition 3.1.** A norm on $V$ is a function $\|\cdot\|: V\to\mathbb R$, $x\mapsto\|x\|$ (the "length"), such that for all $\lambda\in\mathbb R$, $x,y\in V$:
- Absolutely homogeneous: $\|\lambda x\| = |\lambda|\,\|x\|$.
- Triangle inequality: $\|x+y\|\le\|x\|+\|y\|$ (any side of a triangle is at most the sum of the other two).
- Positive definite: $\|x\|\ge 0$ and $\|x\|=0 \iff x=0$ (p. 71).

The book only considers finite-dimensional $\mathbb R^n$ (p. 71).

- **Manhattan norm ($\ell_1$), Example 3.1:** $\|x\|_1 := \sum_{i=1}^n |x_i|$ (3.3). In $\mathbb R^2$ the vectors with $\|x\|_1=1$ form a diamond (p. 71).
- **Euclidean norm ($\ell_2$), Example 3.2:** $\|x\|_2 := \sqrt{\sum_i x_i^2} = \sqrt{x^\top x}$ (3.4). Its unit set in $\mathbb R^2$ is a circle. It is the book's default norm (p. 72).

### 3.2 Inner products (p. 72–74)
Inner products give length, angle and distance. A major purpose is to decide whether vectors are orthogonal (p. 72).

**3.2.1 Dot product.** $x^\top y = \sum_{i=1}^n x_i y_i$ (3.5). It is one particular inner product (p. 72).

**3.2.2 General inner products.** A *bilinear mapping* $\Omega$ takes two arguments and is linear in each (p. 72):
$$\Omega(\lambda x+\psi y, z) = \lambda\Omega(x,z)+\psi\Omega(y,z)\tag{3.6}$$
$$\Omega(x,\lambda y+\psi z) = \lambda\Omega(x,y)+\psi\Omega(x,z)\tag{3.7}$$

**Definition 3.2.** For a bilinear $\Omega: V\times V\to\mathbb R$:
- *symmetric* if $\Omega(x,y)=\Omega(y,x)$ for all $x,y$;
- *positive definite* if $\forall x\in V\setminus\{0\}: \Omega(x,x)>0$ and $\Omega(0,0)=0$ (3.8) (p. 73).

**Definition 3.3.** A positive definite, symmetric bilinear mapping is an *inner product*, written $\langle x,y\rangle$. The pair $(V,\langle\cdot,\cdot\rangle)$ is an inner product space. With the dot product it is a *Euclidean vector space* (p. 73).

**Example 3.3.** On $\mathbb R^2$, $\langle x,y\rangle := x_1y_1-(x_1y_2+x_2y_1)+2x_2y_2$ (3.9) is an inner product different from the dot product. The proof is left as an exercise (p. 73).

**3.2.3 Symmetric, positive definite matrices.** Let $V$ be $n$-dimensional with an inner product and ordered basis $B=(b_1,\dots,b_n)$. Write $x=\sum_i\psi_i b_i$, $y=\sum_j\lambda_j b_j$. By bilinearity (p. 73):
$$\langle x,y\rangle=\Big\langle\sum_i\psi_i b_i,\sum_j\lambda_j b_j\Big\rangle=\sum_{i=1}^n\sum_{j=1}^n\psi_i\langle b_i,b_j\rangle\lambda_j=\hat x^\top A\hat y\tag{3.10}$$
with $A_{ij}:=\langle b_i,b_j\rangle$ and $\hat x,\hat y$ the coordinate vectors. So the inner product is uniquely determined by $A$. Symmetry of the inner product makes $A$ symmetric. Positive definiteness gives (p. 73–74)
$$\forall x\in V\setminus\{0\}: x^\top Ax>0.\tag{3.11}$$

**Definition 3.4.** A symmetric $A\in\mathbb R^{n\times n}$ satisfying (3.11) is *symmetric, positive definite*. If only $\ge$ holds, it is *positive semidefinite* (p. 74).

**Example 3.4.** $A_1=\begin{bmatrix}9&6\\6&5\end{bmatrix}$, $A_2=\begin{bmatrix}9&6\\6&3\end{bmatrix}$ (3.12).
- $x^\top A_1x = 9x_1^2+12x_1x_2+5x_2^2=(3x_1+2x_2)^2+x_2^2>0$ for $x\neq0$, so $A_1$ is positive definite.
- $x^\top A_2x=9x_1^2+12x_1x_2+3x_2^2=(3x_1+2x_2)^2-x_2^2$ can be negative, e.g. at $x=[2,-3]^\top$. So $A_2$ is symmetric but not positive definite (p. 74).

If $A$ is symmetric positive definite, $\langle x,y\rangle=\hat x^\top A\hat y$ (3.14) defines an inner product with respect to $B$.

**Theorem 3.5.** For a real, finite-dimensional $V$ and ordered basis $B$: $\langle\cdot,\cdot\rangle$ is an inner product **if and only if** there is a symmetric, positive definite $A\in\mathbb R^{n\times n}$ with $\langle x,y\rangle=\hat x^\top A\hat y$ (3.15) (p. 74).

Properties of symmetric positive definite $A$ (p. 74):
- Its null space is $\{0\}$, since $x^\top Ax>0$ for $x\ne0$ implies $Ax\neq0$.
- Its diagonal entries are positive: $a_{ii}=e_i^\top Ae_i>0$.

*Intuition note.* Once a basis is fixed, choosing an inner product on $\mathbb R^n$ amounts to choosing a symmetric positive definite matrix. The matrix says how basis vectors relate to each other. Positive definiteness guarantees that every nonzero vector has positive squared length.

### 3.3 Lengths and distances (p. 75–76)
Every inner product induces a norm, $\|x\|:=\sqrt{\langle x,x\rangle}$ (3.16). Not every norm is induced by an inner product; the Manhattan norm is a norm without a corresponding inner product (p. 75).

**Cauchy–Schwarz inequality** (stated as a remark, no proof): $|\langle x,y\rangle|\le\|x\|\|y\|$ (3.17) (p. 75).

**Example 3.5.** Take $x=[1,1]^\top$.
- Dot product: $\|x\|=\sqrt{x^\top x}=\sqrt{1^2+1^2}=\sqrt2$ (3.18).
- With $\langle x,y\rangle:=x^\top\begin{bmatrix}1&-\tfrac12\\-\tfrac12&1\end{bmatrix}y=x_1y_1-\tfrac12(x_1y_2+x_2y_1)+x_2y_2$ (3.19): $\langle x,x\rangle=x_1^2-x_1x_2+x_2^2=1-1+1=1$, so $\|x\|=1$ (3.20).
- This inner product gives smaller values than the dot product when $x_1x_2>0$ and greater values otherwise. Here $x$ is "shorter" than under the dot product (p. 75).

**Definition 3.6.** In an inner product space, $d(x,y):=\|x-y\|=\sqrt{\langle x-y,x-y\rangle}$ (3.21) is the *distance*; with the dot product it is the *Euclidean distance*. The map $d:V\times V\to\mathbb R$ is a *metric* (3.22–3.23) (p. 75–76).

A norm alone suffices to define distance. For an inner-product-induced norm, the distance may vary with the choice of inner product (p. 76). A metric satisfies (p. 76):
1. positive definite: $d(x,y)\ge0$, and $d(x,y)=0\iff x=y$;
2. symmetric: $d(x,y)=d(y,x)$;
3. triangle inequality: $d(x,z)\le d(x,y)+d(y,z)$.

Inner product and metric "behave in opposite directions": very similar $x,y$ give a large inner product and a small metric (p. 76).

### 3.4 Angles and orthogonality (p. 76–78)
For $x,y\ne0$, Cauchy–Schwarz gives
$$-1\le\frac{\langle x,y\rangle}{\|x\|\|y\|}\le1\tag{3.24}$$
so there is a unique $\omega\in[0,\pi]$ with
$$\cos\omega=\frac{\langle x,y\rangle}{\|x\|\|y\|}\tag{3.25}$$
(Fig. 3.4: on $[0,\pi]$, cosine returns a unique value in $[-1,1]$). This is the *angle* between $x$ and $y$; it says how similar their orientations are. With the dot product, the angle between $x$ and $y=4x$ is 0 (p. 76).

**Example 3.6.** Dot product, $x=[1,1]^\top$, $y=[1,2]^\top$:
$$\cos\omega=\frac{x^\top y}{\sqrt{x^\top x\,y^\top y}}=\frac{3}{\sqrt{10}}$$
(3.26), so $\omega=\arccos(3/\sqrt{10})\approx0.32$ rad $\approx18^\circ$ (p. 77).

**Definition 3.7.** $x,y$ are *orthogonal* if and only if $\langle x,y\rangle=0$, written $x\perp y$. If also $\|x\|=\|y\|=1$, they are *orthonormal*. Hence $0$ is orthogonal to every vector (p. 77). Orthogonality generalises perpendicularity to inner products other than the dot product (p. 77).

**Example 3.7.** $x=[1,1]^\top$, $y=[-1,1]^\top$.
- Dot product: angle $90^\circ$, so $x\perp y$.
- With $\langle x,y\rangle=x^\top\begin{bmatrix}2&0\\0&1\end{bmatrix}y$ (3.27): $\cos\omega=-\tfrac13$, $\omega\approx1.91$ rad $\approx109.5^\circ$ (3.28). (added step: $\langle x,y\rangle=2(1)(-1)+1(1)(1)=-1$ and $\|x\|=\|y\|=\sqrt{2+1}=\sqrt3$, so $\cos\omega=-1/3$.)
- Vectors orthogonal for one inner product need not be orthogonal for another (p. 77–78).

**Definition 3.8.** A square $A\in\mathbb R^{n\times n}$ is *orthogonal* if and only if its columns are orthonormal, so that $AA^\top=I=A^\top A$ (3.29), which implies $A^{-1}=A^\top$ (3.30). (The book notes "orthonormal" would be more precise.) (p. 78)

For the dot product, orthogonal $A$ preserves length and angle (p. 78):
$$\|Ax\|^2=(Ax)^\top(Ax)=x^\top A^\top Ax=x^\top Ix=x^\top x=\|x\|^2\tag{3.31}$$
$$\cos\omega=\frac{(Ax)^\top(Ay)}{\|Ax\|\|Ay\|}=\frac{x^\top A^\top Ay}{\sqrt{x^\top A^\top Ax\;y^\top A^\top Ay}}=\frac{x^\top y}{\|x\|\|y\|}\tag{3.32}$$
Such matrices define rotations (with possible flips); Section 3.9 gives details (p. 78).

*Intuition note.* Angles and right angles are not built into the space; they come from the inner product you pick. An orthogonal matrix moves vectors without stretching or bending anything, with respect to the dot product.

### 3.5 Orthonormal basis (p. 78–79)
**Definition 3.9.** A basis $\{b_1,\dots,b_n\}$ of an $n$-dimensional $V$ is an *orthonormal basis (ONB)* if $\langle b_i,b_j\rangle=0$ for $i\ne j$ (3.33) and $\langle b_i,b_i\rangle=1$ (3.34). If only (3.33) holds it is an *orthogonal basis* (p. 79).

The text says a non-orthogonal, unnormalised basis $\{\tilde b_i\}$ can be turned into an orthonormal one by Gaussian elimination on the augmented matrix $[\tilde B\tilde B^\top|\tilde B]$, calling this the Gram–Schmidt process. It gives no example of this route (p. 79). The explicit iterative method comes in 3.8.3.

**Example 3.8.** The standard basis of $\mathbb R^n$ is an ONB for the dot product. In $\mathbb R^2$, $b_1=\tfrac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}$, $b_2=\tfrac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}$ (3.35) form an ONB, since $b_1^\top b_2=0$ and $\|b_1\|=\|b_2\|=1$ (p. 79).

### 3.6 Orthogonal complement (p. 79–80)
Let $V$ be $D$-dimensional and $U\subseteq V$ an $M$-dimensional subspace. Its *orthogonal complement* $U^\perp$ is a $(D-M)$-dimensional subspace containing all vectors orthogonal to every vector in $U$. Also $U\cap U^\perp=\{0\}$, so every $x\in V$ decomposes uniquely as
$$x=\sum_{m=1}^M\lambda_mb_m+\sum_{j=1}^{D-M}\psi_jb_j^\perp,\quad\lambda_m,\psi_j\in\mathbb R\tag{3.36}$$
with $(b_m)$ a basis of $U$ and $(b_j^\perp)$ a basis of $U^\perp$ (p. 79–80).

A plane $U$ in $\mathbb R^3$ can be described by a unit vector $w$ orthogonal to it, the basis of $U^\perp$, called the *normal vector*. All vectors orthogonal to $w$ lie in $U$. In general, orthogonal complements describe hyperplanes in $n$-dimensional vector and affine spaces (p. 80).

### 3.7 Inner product of functions (p. 80–81)
A vector in $\mathbb R^n$ can be seen as a function with $n$ values. For infinitely many entries or continuous functions the sum in (3.5) becomes an integral. For $u,v:\mathbb R\to\mathbb R$,
$$\langle u,v\rangle:=\int_a^bu(x)v(x)\,dx\tag{3.37}$$
with $a,b<\infty$. If it is 0, $u$ and $v$ are orthogonal. Making this precise needs measures and Hilbert spaces, which the book does not cover. Unlike finite-dimensional cases, such inner products may diverge (p. 80–81).

**Example 3.9.** $u=\sin x$, $v=\cos x$: the integrand $\sin x\cos x$ is odd, $f(-x)=-f(x)$, so the integral over $[-\pi,\pi]$ is 0. Hence $\sin$ and $\cos$ are orthogonal (p. 81).

Remark: $\{1,\cos x,\cos 2x,\cos 3x,\dots\}$ is pairwise orthogonal on $[-\pi,\pi]$. It spans a large subspace of the even, periodic functions on $[-\pi,\pi)$, and projecting onto it is the fundamental idea behind Fourier series (p. 81). Section 6.4.6 treats inner products of random variables (p. 81).

### 3.8 Orthogonal projections (p. 81–90)
Motivation: high-dimensional data often has only a few informative dimensions. Projecting onto a lower-dimensional subspace compresses data; orthogonal projections retain as much information as possible and minimise the error between data and projection, for a given subspace (p. 81–82).

**Definition 3.10.** For a subspace $U\subseteq V$, a linear map $\pi:V\to U$ is a *projection* if $\pi^2=\pi\circ\pi=\pi$. For matrices: $P_\pi^2=P_\pi$ (p. 82).

The book assumes the dot product from here unless stated (p. 82).

**3.8.1 Projection onto lines.** Let $U$ be spanned by $b\in\mathbb R^n$. Two properties of $\pi_U(x)$ (p. 83):
- It is closest to $x$, so $\pi_U(x)-x$ is orthogonal to $b$: $\langle\pi_U(x)-x,b\rangle=0$.
- It lies in $U$, so $\pi_U(x)=\lambda b$ for some $\lambda\in\mathbb R$ ($\lambda$ is its coordinate with respect to $b$).

Step 1, the coordinate (p. 83):
$$\langle x-\pi_U(x),b\rangle=0\overset{\pi_U(x)=\lambda b}{\iff}\langle x-\lambda b,b\rangle=0\tag{3.39}$$
$$\langle x,b\rangle-\lambda\langle b,b\rangle=0\iff\lambda=\frac{\langle x,b\rangle}{\langle b,b\rangle}=\frac{\langle b,x\rangle}{\|b\|^2}\tag{3.40}$$
For the dot product, $\lambda=\dfrac{b^\top x}{b^\top b}=\dfrac{b^\top x}{\|b\|^2}$ (3.41); if $\|b\|=1$, $\lambda=b^\top x$.

Step 2, the point (p. 84):
$$\pi_U(x)=\lambda b=\frac{\langle x,b\rangle}{\|b\|^2}b=\frac{b^\top x}{\|b\|^2}b\tag{3.42}$$
(last equality for the dot product only). Its length is $\|\pi_U(x)\|=\|\lambda b\|=|\lambda|\|b\|$ (3.43). With the dot product and $\omega$ the angle between $x$ and $b$:
$$\|\pi_U(x)\|\overset{(3.42)}{=}\frac{|b^\top x|}{\|b\|^2}\|b\|\overset{(3.25)}{=}|\cos\omega|\,\|x\|\|b\|\frac{\|b\|}{\|b\|^2}=|\cos\omega|\,\|x\|\tag{3.44}$$
For $\|x\|=1$ this is the familiar trigonometric picture (Fig. 3.10b) (p. 84).

Step 3, the matrix. A projection is linear, so $\pi_U(x)=P_\pi x$. From
$$\pi_U(x)=\lambda b=b\lambda=b\frac{b^\top x}{\|b\|^2}=\frac{bb^\top}{\|b\|^2}x\tag{3.45}$$
we get
$$P_\pi=\frac{bb^\top}{\|b\|^2}\tag{3.46}$$
$bb^\top$ (hence $P_\pi$) is symmetric of rank 1, and $\|b\|^2$ is a scalar (p. 84). The projection $\pi_U(x)$ is still an $n$-vector but needs only one coordinate $\lambda$ in the basis $b$ (p. 84).

**Example 3.10.** $b=[1,2,2]^\top$, $b^\top b=9$:
$$P_\pi=\frac{bb^\top}{b^\top b}=\frac19\begin{bmatrix}1&2&2\\2&4&4\\2&4&4\end{bmatrix}\tag{3.47}$$
For $x=[1,1,1]^\top$: $\pi_U(x)=P_\pi x=\tfrac19[5,10,10]^\top\in\mathrm{span}[[1,2,2]^\top]$ (3.48). Applying $P_\pi$ again changes nothing, as $P_\pi^2=P_\pi$ requires (p. 85). Remark: with Chapter 4 one can show $\pi_U(x)$ is an eigenvector of $P_\pi$ with eigenvalue 1 (p. 85).

*Intuition note.* Projecting onto a line means dropping a perpendicular and keeping the foot. Its position is $\lambda$ times $b$, where $\lambda=\langle x,b\rangle/\langle b,b\rangle$ measures how much of $x$ points along $b$.

**3.8.2 Projection onto general subspaces.** Let $(b_1,\dots,b_m)$ be an ordered basis of $U\subseteq\mathbb R^n$, $\dim U=m\ge1$. If $U$ is given by spanning vectors that are not a basis, first find a basis (margin note, p. 85). Then $\pi_U(x)=\sum_i\lambda_ib_i=B\lambda$, with $B=[b_1,\dots,b_m]\in\mathbb R^{n\times m}$ and $\lambda\in\mathbb R^m$ (3.49–3.50) (p. 86).

Step 1, the coordinates. "Closest" means $x-\pi_U(x)$ is orthogonal to every basis vector, giving $m$ conditions $b_i^\top(x-B\lambda)=0$ (3.51–3.54), i.e. a homogeneous system (p. 86):
$$\begin{bmatrix}b_1^\top\\\vdots\\b_m^\top\end{bmatrix}(x-B\lambda)=0\iff B^\top(x-B\lambda)=0\tag{3.55}$$
$$\iff B^\top B\lambda=B^\top x\tag{3.56}$$
This is the *normal equation*. Since the $b_i$ are linearly independent, $B^\top B\in\mathbb R^{m\times m}$ is regular (invertible), so
$$\lambda=(B^\top B)^{-1}B^\top x\tag{3.57}$$
$(B^\top B)^{-1}B^\top$ is the *pseudo-inverse* of $B$, computable for non-square $B$; it requires $B^\top B$ to be positive definite, which holds if $B$ is full rank. In practice (e.g. linear regression) one often adds a "jitter term" $\epsilon I$ to $B^\top B$ for numerical stability and positive definiteness; the text says this "ridge" can be derived by Bayesian inference (Ch. 9) (p. 86–87).

Step 2: $\pi_U(x)=B(B^\top B)^{-1}B^\top x$ (3.58). Step 3:
$$P_\pi=B(B^\top B)^{-1}B^\top\tag{3.59}$$
Shapes: $B$ is $n\times m$, $B^\top B$ is $m\times m$, $P_\pi$ is $n\times n$. For $\dim U=1$, $B^\top B$ is a scalar and (3.59) reduces to (3.46) (p. 87).

**Example 3.11.** $U=\mathrm{span}\big[[1,1,1]^\top,[0,1,2]^\top\big]\subseteq\mathbb R^3$, $x=[6,0,0]^\top$ (p. 87–88).
1. The generating set is linearly independent, so $B=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}$.
2. $B^\top B=\begin{bmatrix}3&3\\3&5\end{bmatrix}$, $B^\top x=\begin{bmatrix}6\\0\end{bmatrix}$ (3.60).
3. Normal equation $\begin{bmatrix}3&3\\3&5\end{bmatrix}\lambda=\begin{bmatrix}6\\0\end{bmatrix}$ gives $\lambda=[5,-3]^\top$ (3.61).
4. $\pi_U(x)=B\lambda=[5,2,-1]^\top$ (3.62).
5. Projection error: $\|x-\pi_U(x)\|=\|[1,-2,1]^\top\|=\sqrt6$ (3.63). It is also called the reconstruction error.
6. $P_\pi=\tfrac16\begin{bmatrix}5&2&-1\\2&2&2\\-1&2&5\end{bmatrix}$ (3.64).

Checks suggested: $\pi_U(x)-x$ is orthogonal to all basis vectors, and $P_\pi=P_\pi^2$ (p. 88).

Remarks (p. 88):
- Projections remain $n$-vectors but need only $m$ coordinates.
- With general inner products, angles and distances must be computed with that inner product.
- **Least squares.** If $Ax=b$ has no solution ($b$ outside the column span of $A$), one can take the orthogonal projection of $b$ onto the column space of $A$. This is the least-squares solution of an overdetermined system (Sec. 9.4). Reconstruction errors give one derivation of PCA (Sec. 10.3).
- **ONB case.** If the basis is orthonormal, $B^\top B=I$ and $\pi_U(x)=BB^\top x$ (3.65), $\lambda=B^\top x$ (3.66). No inverse is needed.

*Intuition note.* The normal equation says the error vector is perpendicular to every basis vector of the subspace. Solving it gives the closest point in $U$. With an orthonormal basis the equations decouple, so each coordinate is just an inner product.

**3.8.3 Gram–Schmidt orthogonalization.** Projections let us turn any basis $(b_1,\dots,b_n)$ of $V$ into an orthogonal (or, after normalising, orthonormal) basis $(u_1,\dots,u_n)$ with $\mathrm{span}[b_1,\dots,b_n]=\mathrm{span}[u_1,\dots,u_n]$; the text says such a basis always exists (p. 89):
$$u_1:=b_1\tag{3.67}$$
$$u_k:=b_k-\pi_{\mathrm{span}[u_1,\dots,u_{k-1}]}(b_k),\quad k=2,\dots,n\tag{3.68}$$
Subtracting the projection leaves $u_k$ orthogonal to the span of $u_1,\dots,u_{k-1}$. Normalising each $u_k$ gives an ONB (p. 89).

**Example 3.12.** $b_1=\begin{bmatrix}2\\0\end{bmatrix}$, $b_2=\begin{bmatrix}1\\1\end{bmatrix}$ (3.69). Then $u_1=b_1=[2,0]^\top$ (3.70), and using (3.45)
$$u_2=b_2-\frac{u_1u_1^\top}{\|u_1\|^2}b_2=\begin{bmatrix}1\\1\end{bmatrix}-\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}0\\1\end{bmatrix}\tag{3.71}$$
and $u_1^\top u_2=0$ (p. 89–90).

**3.8.4 Projection onto affine subspaces.** Let $L=x_0+U$ with support point $x_0$ and direction space $U$. Subtract $x_0$ from $x$ and from $L$ (so $L-x_0=U$), project onto $U$, then add $x_0$ back (p. 90):
$$\pi_L(x)=x_0+\pi_U(x-x_0)\tag{3.72}$$
The distance of $x$ from $L$ equals the distance of $x-x_0$ from $U$ (p. 90):
$$d(x,L)=\|x-\pi_L(x)\|=\|x-(x_0+\pi_U(x-x_0))\|=d(x-x_0,\pi_U(x-x_0))=d(x-x_0,U)\tag{3.73}$$
This is used to derive the separating hyperplane in Section 12.1 (p. 90).

### 3.9 Rotations (p. 91–94)
Orthogonal matrices preserve length and angle (Sec. 3.4). A *rotation* is a linear map (an automorphism of a Euclidean vector space) that rotates a plane by an angle $\theta$ about the origin, which stays fixed. By convention $\theta>0$ is counterclockwise. Fig. 3.14 shows a rotation by 112.5° with matrix $R=\begin{bmatrix}-0.38&-0.92\\0.92&-0.38\end{bmatrix}$ (3.74). Applications named: computer graphics, robotics (p. 91).

**3.9.1 Rotations in $\mathbb R^2$.** Rotating $e_1,e_2$ by $\theta$ (trigonometry, Fig. 3.16) gives
$$\Phi(e_1)=\begin{bmatrix}\cos\theta\\\sin\theta\end{bmatrix},\ \Phi(e_2)=\begin{bmatrix}-\sin\theta\\\cos\theta\end{bmatrix}\tag{3.75}$$
$$R(\theta)=[\Phi(e_1)\ \Phi(e_2)]=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}\tag{3.76}$$
The rotated vectors are still linearly independent, so the rotation is a basis change (p. 92).

**3.9.2 Rotations in $\mathbb R^3$.** Specify where $e_1,e_2,e_3$ go, making sure the images $Re_1,Re_2,Re_3$ are orthonormal. "Counterclockwise" means: look at the axis head-on, from its end toward the origin. Three planar rotations (p. 92–93):
$$R_1(\theta)=\begin{bmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{bmatrix}\tag{3.77}$$
$$R_2(\theta)=\begin{bmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{bmatrix}\tag{3.78}$$
$$R_3(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}\tag{3.79}$$
For $R_1$ the $e_1$ coordinate is fixed and the rotation happens in the $e_2e_3$ plane (p. 93).

**3.9.3 Rotations in $n$ dimensions.** Fix $n-2$ dimensions and rotate within one plane (p. 93).

**Definition 3.11 (Givens rotation).** For $1\le i<j\le n$, $R_{ij}(\theta)\in\mathbb R^{n\times n}$ is the identity $I_n$ except
$$r_{ii}=\cos\theta,\quad r_{ij}=-\sin\theta,\quad r_{ji}=\sin\theta,\quad r_{jj}=\cos\theta\tag{3.80–3.81}$$
For $n=2$ this is (3.76) (p. 94).

**3.9.4 Properties.** Since rotations are orthogonal matrices (p. 94):
- they preserve distances, $\|x-y\|=\|R_\theta(x)-R_\theta(y)\|$, and angles;
- in three or more dimensions they are generally not commutative, so the order matters even about the same point;
- only in 2D does $R(\phi)R(\theta)=R(\theta)R(\phi)$ hold for all $\phi,\theta\in[0,2\pi)$. The text says they form an Abelian group (under multiplication) only if they rotate about the same point, e.g. the origin.

### 3.10 Further reading (p. 94–95)
Gram–Schmidt orthogonal bases matter in numerical algorithms; Krylov methods such as conjugate gradients and GMRES minimise mutually orthogonal residual errors. Inner products are important for kernel methods: many linear algorithms can be expressed purely through inner product computations, and the "kernel trick" computes them implicitly in a possibly infinite-dimensional feature space (e.g. kernel-PCA, Gaussian processes; Ch. 12). Projections appear in graphics (shadows), optimisation, linear regression (residuals as lengths of orthogonal projections, Ch. 9) and PCA (Ch. 10) (p. 94–95).

## Toy example (ours, not from the text)
Project $x=[1,2,0]^\top$ onto $U=\mathrm{span}[b_1,b_2]$ with $b_1=[1,0,1]^\top$, $b_2=[0,1,1]^\top$, dot product.
- $B=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$ ($3\times2$), $B^\top B=\begin{bmatrix}1\cdot1+0+1\cdot1&0+0+1\cdot1\\1&0+1+1\end{bmatrix}=\begin{bmatrix}2&1\\1&2\end{bmatrix}$.
- $B^\top x=[1\cdot1+0\cdot2+1\cdot0,\ 0\cdot1+1\cdot2+1\cdot0]^\top=[1,2]^\top$.
- Normal equation: $2\lambda_1+\lambda_2=1$, $\lambda_1+2\lambda_2=2$. From the first, $\lambda_2=1-2\lambda_1$. The second gives $\lambda_1+2-4\lambda_1=2$, so $\lambda_1=0$, $\lambda_2=1$.
- $\pi_U(x)=0\cdot b_1+1\cdot b_2=[0,1,1]^\top$. Residual $x-\pi_U(x)=[1,1,-1]^\top$.
- Check: residual $\cdot\,b_1=1+0-1=0$; residual $\cdot\,b_2=0+1-1=0$. Orthogonal to both basis vectors, as required.
- Error $=\sqrt{1+1+1}=\sqrt3$.

## Concepts
- [[norm]] — function giving a vector's length; homogeneous, triangle inequality, positive definite (p. 71)
- [[dot (inner) product]] — $x^\top y=\sum x_iy_i$; general inner product is symmetric, positive definite, bilinear (p. 72–73)
- [[inner-product-space]] (new) — vector space with a chosen inner product; supplies length, distance, angle (p. 73)
- [[positive (semi)definite matrix]] — symmetric $A$ with $x^\top Ax>0$ ($\ge0$) for $x\ne0$; matches inner products in a basis (p. 74)
- [[metric-distance]] (new) — $d(x,y)=\|x-y\|$, with positivity, symmetry, triangle inequality (p. 75–76)
- [[cauchy-schwarz-inequality]] (new) — $|\langle x,y\rangle|\le\|x\|\|y\|$; makes the angle definition possible (p. 75–76)
- [[cosine similarity]] — here the angle via $\cos\omega=\langle x,y\rangle/(\|x\|\|y\|)$ (p. 76)
- [[orthogonality]] — $\langle x,y\rangle=0$; depends on the chosen inner product (p. 77)
- [[orthonormal basis / orthogonal matrix]] — orthonormal basis; matrix with $A^\top A=I$ preserves lengths and angles for the dot product (p. 78–79)
- [[orthogonal-complement]] (new) — all vectors orthogonal to a subspace; dimension $D-M$ (p. 79)
- [[projection]] — linear $\pi$ with $\pi^2=\pi$; orthogonal case $P=B(B^\top B)^{-1}B^\top$ (p. 82–87)
- [[least squares]] — approximate solution of unsolvable $Ax=b$ by projecting $b$ onto the column space (p. 88)
- [[pseudoinverse]] — here $(B^\top B)^{-1}B^\top$ for full-column-rank $B$ (p. 86)
- [[Gram–Schmidt and QR]] — iterative orthogonalisation; here only the Gram–Schmidt part, no QR (p. 89)
- [[rotation-matrix-givens]] (new) — orthogonal matrix rotating a plane; Givens rotation fixes all but two coordinates (p. 92–94)
- [[basis]] — here used for ONB and for coordinates of a projection (p. 79, 86)

## Canonical instances
- [[manhattan-vs-euclidean-norm]] — $\ell_1$ and $\ell_2$ unit sets differ; $\ell_1$ has no inner product (p. 71, 75)
- [[angle-depends-on-inner-product]] — $[1,1]$ and $[-1,1]$ are orthogonal under the dot product, 109.5° apart under diag(2,1) (p. 77–78)
- [[projection-onto-line-example]] — $b=[1,2,2]^\top$, $P_\pi=\tfrac19 bb^\top$-type matrix (p. 85)
- [[projection-onto-plane-example]] — $x=[6,0,0]^\top$ projected to $[5,2,-1]^\top$, error $\sqrt6$ (p. 87–88)
- [[sin-cos-orthogonal-functions]] — $\int_{-\pi}^{\pi}\sin x\cos x\,dx=0$ (p. 81)

## Bridges (candidates)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88).
- [structural-analogy] Projection onto an orthonormal basis $\lambda=B^\top x$ ↔ Fourier series: coordinates are inner products with orthogonal functions (p. 81, 88).
- [structural-analogy] Inner product matrix $A_{ij}=\langle b_i,b_j\rangle$ ↔ kernel/Gram matrices: many algorithms expressible through inner products alone can be "kernelised" (p. 73, 95).
- [structural-analogy] Projection onto a line ↔ cosine similarity: $\|\pi_U(x)\|=|\cos\omega|\|x\|$ links projection length to angle (p. 84).
- [metaphor] Different inner products ↔ different "rulers" for the same space: the same vectors get different lengths and angles (p. 75, 77).

## Questions this raises
- Which norms are induced by an inner product, and how can one test that? (The text only says $\ell_1$ is not.) (p. 75)
- What is the exact relation between the pseudo-inverse here and the SVD-based pseudo-inverse? (the unit defines it only as $(B^\top B)^{-1}B^\top$) (p. 86)
- Why are rotations in $\ge3$ dimensions non-commutative while 2D rotations commute? (p. 94)
- How does the "ridge" term $\epsilon I$ arise from Bayesian inference? (promised for Ch. 9) (p. 87)

## Exercises worth doing
- Ex. 3.1 (p. 96) — prove (3.9)-type bilinear form is an inner product; checks the three axioms — difficulty: easy
- Ex. 3.2 (p. 96) — decide whether a non-symmetric matrix $A$ gives an inner product — difficulty: easy
- Ex. 3.3–3.4 (p. 96) — distances and angles under dot product vs. a matrix inner product — difficulty: easy
- Ex. 3.5 (p. 96) — projection onto a span in $\mathbb R^5$ and distance $d(x,U)$; per the margin note, find a basis of the spanning set first — difficulty: medium
- Ex. 3.7 (p. 97) — $\pi$ is a projection iff $\mathrm{id}_V-\pi$ is; image and kernel of $\mathrm{id}_V-\pi$ — difficulty: hard
- Ex. 3.8 (p. 97) — Gram–Schmidt to an ONB in a plane of $\mathbb R^3$ — difficulty: medium
- Ex. 3.9 (p. 97) — use Cauchy–Schwarz to bound sums of squares and reciprocals — difficulty: medium

## Reading notes
- Printed page = pdf page − 6 (pdf 76 = printed 70); all printed numbers are visible on the pages.
- Page footer: "Draft (2024-01-15)" and "©2024 … Published by Cambridge University Press (2020)".
- The Cauchy–Schwarz inequality is stated without proof (p. 75). No full proofs of Theorem 3.5 or of Example 3.3 are given; the latter is an exercise.
- The claim that Gaussian elimination on $[\tilde B\tilde B^\top|\tilde B]$ yields an ONB (p. 79) is stated without example; I did not verify it.
- The margin note "Projection matrices are always symmetric" (p. 84) appears beside the orthogonal-projection derivation. Definition 3.10 itself only requires $P_\pi^2=P_\pi$.
- The caption of Fig. 3.3 says "Euclidean distance" for the right panel, which shows the unit set of the Euclidean norm.
- Section 3.8.2 remark (p. 88) writes the basis as $\{b_1,\dots,b_k\}$ where the section uses $m$ vectors.
- Exercise statements appear on pp. 96–97; the book prints no solutions in these pages.
