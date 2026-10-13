---
id: axler-2024-ladr/ch07-operators-p2
work: axler-2024-ladr
unit: "7 Operators on Inner Product Spaces (part 2/3): 7C Positive Operators; 7D Isometries, Unitary Operators, and Matrix Factorization"
pages: 251-269
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Positive operators, isometries, unitary operators, QR and Cholesky factorization

## L0 — One line
Positive operators (the analogue of nonnegative numbers) have a unique positive square root, and the norm-preserving maps (isometries, unitary operators) lead to the QR factorization and, from it, the Cholesky factorization $B=R^*R$.

## L1 — The gist (≤ 120 words)
Which operators behave like nonnegative numbers, and which like numbers of absolute value 1? Axler shows that an operator is positive exactly when it is self-adjoint with nonnegative eigenvalues, equivalently when it equals $R^*R$ for some $R$. Each positive operator has exactly one positive square root. Linear maps that preserve norms (isometries) are exactly those that preserve inner products, or send some orthonormal basis to an orthonormal list. Applying Gram–Schmidt to the columns of a matrix gives a unique QR factorization. QR then gives the unique Cholesky factorization of a positive definite matrix. Both factorizations matter in computational linear algebra.

**Prerequisites:** adjoint and self-adjoint operators; spectral theorem; orthonormal bases and Gram–Schmidt; matrix of an operator; injective ⇒ invertible in finite dimension.

## L2 — Key ideas (5–10 bullets)
- A positive operator is self-adjoint with $\langle Tv,v\rangle\ge 0$. It is equivalent to: nonnegative eigenvalues, an orthonormal basis giving a nonnegative diagonal matrix, a positive or self-adjoint square root, or $T=R^*R$ (7.38). Several tests are available. (p. 252)
- A positive operator has a unique positive square root $\sqrt T$; it acts as $\sqrt\lambda$ on each $\lambda$-eigenvector (7.39). (p. 253)
- If $T$ is positive and $\langle Tv,v\rangle=0$, then $Tv=0$ (7.43). A self-adjoint $T$ is positive and invertible iff $\langle Tv,v\rangle>0$ for all $v\neq 0$ (7.61). (pp. 254, 266)
- An isometry preserves norms. This is equivalent to $S^*S=I$, to preserving inner products, to mapping an orthonormal basis to an orthonormal list, and to the matrix having orthonormal columns (7.49). (p. 259)
- A unitary operator is an invertible isometry. Equivalent: $S^{-1}=S^*$, or orthonormal rows. Its eigenvalues have absolute value 1. Over $\mathbf C$ the unitary operators are those with an orthonormal eigenbasis whose eigenvalues all have $|\lambda|=1$ (7.53–7.55). (pp. 261–262)
- The analogy $\mathbf C \leftrightarrow \mathcal L(V)$ runs through the section: real ↔ self-adjoint, nonnegative ↔ positive, unit circle ↔ unitary. (p. 262)
- A square matrix with independent columns has a unique factorization $A=QR$ ($Q$ unitary, $R$ upper triangular with positive diagonal). It comes from Gram–Schmidt and lets one solve $Ax=b$ by back-substitution (7.58). (pp. 264, 266)
- A positive definite matrix $B$ (self-adjoint, with $\langle Bx,x\rangle>0$ for $x\ne0$, 7.62) has a unique upper-triangular $R$ with positive diagonal and $B=R^*R$ (Cholesky, 7.63). (p. 267)

## L3 — Walkthrough

### 7C Positive Operators

**7.34 Definition (positive operator).** $T\in\mathcal L(V)$ is *positive* if $T$ is self-adjoint and $\langle Tv,v\rangle\ge 0$ for all $v\in V$. If $V$ is complex, the self-adjointness requirement can be dropped (by 7.14). (p. 251)

**7.35 Examples.** (p. 251)
- (a) $T\in\mathcal L(\mathbf F^2)$ with matrix $\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$ is self-adjoint, and $\langle T(w,z),(w,z)\rangle = 2|w|^2-2\operatorname{Re}(w\bar z)+|z|^2=|w-z|^2+|w|^2\ge 0$. So $T$ is positive.
- (b) The orthogonal projection $P_U$ onto a subspace $U$ is positive (left to the reader).
- (c) If $T$ is self-adjoint and $b,c\in\mathbf R$ with $b^2<4c$, then $T^2+bT+cI$ is positive, as shown in the proof of 7.26.

**7.36 Definition.** $R$ is a *square root* of $T$ if $R^2=T$. **7.37 Example:** $T(z_1,z_2,z_3)=(z_3,0,0)$ has the square root $R(z_1,z_2,z_3)=(z_2,z_3,0)$, since $R^2=T$. (p. 251)

Axler notes the analogy with $\mathbf C$. A number is nonnegative iff it has a nonnegative square root (condition (d)), iff it has a real square root (condition (e)), and iff $z=\bar w w$ for some $w$ (condition (f)). He admits "positive" is a misnomer for "nonnegative"; "positive semidefinite operator" means the same. (p. 251)

**7.38 Characterizations of positive operators.** For $T\in\mathcal L(V)$ the following are equivalent. (p. 252)
- (a) $T$ is positive.
- (b) $T$ is self-adjoint and all eigenvalues are nonnegative.
- (c) For some orthonormal basis, the matrix of $T$ is diagonal with only nonnegative diagonal entries.
- (d) $T$ has a positive square root.
- (e) $T$ has a self-adjoint square root.
- (f) $T=R^*R$ for some $R\in\mathcal L(V)$.

*Proof* (cycle (a)⇒(b)⇒…⇒(f)⇒(a)). (p. 252)
- (a)⇒(b): $T$ is self-adjoint by definition. If $Tv=\lambda v$ with $v\ne0$, then $0\le\langle Tv,v\rangle=\lambda\langle v,v\rangle$, so $\lambda\ge0$.
- (b)⇒(c): the spectral theorem (7.29, 7.31) gives an orthonormal eigenbasis $e_1,\dots,e_n$. The matrix is diagonal with the nonnegative eigenvalues $\lambda_k$.
- (c)⇒(d): by the linear map lemma (3.4) define $Re_k=\sqrt{\lambda_k}\,e_k$. $R$ is positive (to verify), and $R^2e_k=\lambda_ke_k=Te_k$, so $R^2=T$.
- (d)⇒(e): positive operators are self-adjoint.
- (e)⇒(f): if $T=R^2$ with $R=R^*$, then $T=R^*R$.
- (f)⇒(a): $T^*=(R^*R)^*=R^*R=T$, and $\langle Tv,v\rangle=\langle R^*Rv,v\rangle=\langle Rv,Rv\rangle\ge0$.

*Intuition note.* Positivity can be tested on eigenvalues, on a diagonal matrix, or by writing $T$ as $R^*R$. Conditions (d), (e), (f) mirror ways to say that a number is nonnegative (p. 251). Condition (f) gives $\langle Tv,v\rangle=\|Rv\|^2$.

**7.39 Each positive operator has only one positive square root.** (p. 253)

*Proof.* Let $T$ be positive and $R$ a positive square root of $T$. Let $v$ be an eigenvector of $T$, so $Tv=\lambda v$ with $\lambda\ge0$. The claim is $Rv=\sqrt\lambda\,v$.
- The spectral theorem gives an orthonormal eigenbasis $e_1,\dots,e_n$ of $R$ with $Re_k=\sqrt{\lambda_k}\,e_k$, where $\lambda_k\ge0$ (eigenvalues of a positive operator are nonnegative).
- Write $v=a_1e_1+\dots+a_ne_n$. Then $Rv=a_1\sqrt{\lambda_1}e_1+\dots+a_n\sqrt{\lambda_n}e_n$.
- Also $\lambda v=Tv=R^2v=a_1\lambda_1e_1+\dots+a_n\lambda_ne_n$.
- Hence $a_1\lambda e_1+\dots+a_n\lambda e_n=a_1\lambda_1e_1+\dots+a_n\lambda_ne_n$, so $a_k(\lambda-\lambda_k)=0$ for each $k$.
- Thus $v=\sum_{\{k:\lambda_k=\lambda\}}a_ke_k$, and so
$$Rv=\sum_{\{k:\lambda_k=\lambda\}}a_k\sqrt{\lambda_k}\,e_k=\sqrt\lambda\,v .$$
- So $R$ is determined on every eigenvector of $T$. $T$ has an eigenbasis (spectral theorem), so $R$ is unique.

Side remark: a positive operator can have infinitely many square roots, but only one is positive. For example, the identity has infinitely many square roots when $\dim V>1$. (p. 253)

**7.40 Notation.** For positive $T$, $\sqrt T$ is its unique positive square root. (p. 253)

*Intuition note.* Like $\sqrt 4=2$ for nonnegative numbers, "the" square root of a positive operator is well defined once it is required to be positive. On each eigenspace it just takes $\sqrt\lambda$.

**7.41 Example.** On $\mathbf R^2$ let $S(x,y)=(x,2y)$ and $T(x,y)=(x+y,x+y)$. (p. 254)
- $\mathcal M(S)=\begin{pmatrix}1&0\\0&2\end{pmatrix}$ and $\mathcal M(T)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ (7.42). Both are symmetric, so $S,T$ are self-adjoint.
- $\langle S(x,y),(x,y)\rangle=x^2+2y^2\ge0$ and $\langle T(x,y),(x,y)\rangle=x^2+2xy+y^2=(x+y)^2\ge0$, so both are positive.
- The standard basis consists of eigenvectors of $S$. $\left(\tfrac1{\sqrt2},\tfrac1{\sqrt2}\right),\left(\tfrac1{\sqrt2},-\tfrac1{\sqrt2}\right)$ is an orthonormal eigenbasis of $T$ with eigenvalues $2$ and $0$. So $\sqrt T$ has the same eigenvectors with eigenvalues $\sqrt2$ and $0$.
- $\mathcal M(\sqrt S)=\begin{pmatrix}1&0\\0&\sqrt2\end{pmatrix}$ and $\mathcal M(\sqrt T)=\begin{pmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}\\ \frac1{\sqrt2}&\frac1{\sqrt2}\end{pmatrix}$. One checks that their squares are the matrices in 7.42 and that they are matrices of positive operators.

**7.43** If $T$ is positive and $\langle Tv,v\rangle=0$, then $Tv=0$. (p. 254)

*Proof.* $0=\langle Tv,v\rangle=\langle\sqrt T\sqrt Tv,v\rangle=\langle\sqrt Tv,\sqrt Tv\rangle=\|\sqrt Tv\|^2$. So $\sqrt Tv=0$, and $Tv=\sqrt T(\sqrt Tv)=0$.

### 7D Isometries, Unitary Operators, and Matrix Factorization

**Isometries.**

**7.44 Definition.** $S\in\mathcal L(V,W)$ is an *isometry* if $\|Sv\|=\|v\|$ for every $v\in V$ (it preserves norms). Every isometry is injective: if $Sv=0$ then $\|v\|=\|Sv\|=0$, so $v=0$. (p. 258)

**7.45 Example.** Let $e_1,\dots,e_n$ be an orthonormal basis of $V$, $g_1,\dots,g_n$ an orthonormal list in $W$, and $Se_k=g_k$. For $v\in V$ (p. 258):
$$v=\langle v,e_1\rangle e_1+\dots+\langle v,e_n\rangle e_n \tag{7.46}$$
$$\|v\|^2=|\langle v,e_1\rangle|^2+\dots+|\langle v,e_n\rangle|^2 \tag{7.47}$$
by 6.30(b). Applying $S$ to 7.46 gives $Sv=\langle v,e_1\rangle g_1+\dots+\langle v,e_n\rangle g_n$, so
$$\|Sv\|^2=|\langle v,e_1\rangle|^2+\dots+|\langle v,e_n\rangle|^2 \tag{7.48}$$
Comparing 7.47 and 7.48 gives $\|Sv\|=\|v\|$.

**7.49 Characterizations of isometries.** Let $S\in\mathcal L(V,W)$, with $e_1,\dots,e_n$ an orthonormal basis of $V$ and $f_1,\dots,f_m$ one of $W$. The following are equivalent. (p. 259)
- (a) $S$ is an isometry.
- (b) $S^*S=I$.
- (c) $\langle Su,Sv\rangle=\langle u,v\rangle$ for all $u,v\in V$.
- (d) $Se_1,\dots,Se_n$ is an orthonormal list in $W$.
- (e) The columns of $\mathcal M\big(S,(e_1,\dots,e_n),(f_1,\dots,f_m)\big)$ form an orthonormal list in $\mathbf F^m$ (Euclidean inner product).

*Proof.* (p. 259)
- (a)⇒(b): $\langle (I-S^*S)v,v\rangle=\langle v,v\rangle-\langle S^*Sv,v\rangle=\|v\|^2-\langle Sv,Sv\rangle=\|v\|^2-\|Sv\|^2=0$. The self-adjoint operator $I-S^*S$ is therefore $0$ (by 7.16).
- (b)⇒(c): $\langle Su,Sv\rangle=\langle S^*Su,v\rangle=\langle Iu,v\rangle=\langle u,v\rangle$.
- (c)⇒(d): take $u=e_j$, $v=e_k$.
- (d)⇒(e): let $A=\mathcal M(S,\dots)$. Then
$$\sum_{j=1}^m A_{j,k}\overline{A_{j,r}}=\Big\langle\sum_{j=1}^mA_{j,k}f_j,\ \sum_{j=1}^mA_{j,r}f_j\Big\rangle=\langle Se_k,Se_r\rangle=\begin{cases}1&k=r\\0&k\ne r\end{cases}\tag{7.50}$$
The left side is the inner product of columns $k$ and $r$ of $A$.
- (e)⇒(a): 7.50 shows $Se_1,\dots,Se_n$ is orthonormal, and Example 7.45 (with $Se_k$ as the $g_k$) gives an isometry.

Consequences stated by Axler: an isometry is exactly a map that preserves inner products. It is exactly a map that sends *some* orthonormal basis to an orthonormal list, and then every orthonormal basis does too. So Example 7.45 covers all isometries. (pp. 258–259) Exercises 1 and 11 give further equivalent conditions. (p. 259)

*Intuition note.* Preserving lengths is the same as preserving all inner products, and the same as sending some (equivalently, every) orthonormal basis to an orthonormal list (7.49). In matrix terms, the columns of $\mathcal M(S)$ are orthonormal.

**Unitary operators.**

**7.51 Definition.** $S\in\mathcal L(V)$ is *unitary* if it is an invertible isometry. Since isometries are injective and injective operators on a finite-dimensional space are invertible (3.65), "invertible" could be dropped without changing the meaning. "Unitary" and "isometry" agree for operators on finite-dimensional inner product spaces, but a unitary operator maps $V$ to itself. (p. 260)

**7.52 Example (rotation).** The operator with matrix $\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ has orthonormal columns. By 7.49 (a)⇔(e) it is an isometry, hence unitary. For $\mathbf F=\mathbf R$ it is counterclockwise rotation by $\theta$ about the origin. (p. 260)

**7.53 Characterizations of unitary operators.** Let $S\in\mathcal L(V)$ and let $e_1,\dots,e_n$ be an orthonormal basis. The following are equivalent. (p. 261)
- (a) $S$ is unitary.
- (b) $S^*S=SS^*=I$.
- (c) $S$ is invertible and $S^{-1}=S^*$.
- (d) $Se_1,\dots,Se_n$ is an orthonormal basis of $V$.
- (e) The rows of $\mathcal M(S,(e_1,\dots,e_n))$ form an orthonormal basis of $\mathbf F^n$.
- (f) $S^*$ is unitary.

All conditions of 7.49 can be added to this list. (p. 260)

*Proof* (cycle). (p. 261)
- (a)⇒(b): 7.49 gives $S^*S=I$. Multiplying on the right by $S^{-1}$ gives $S^*=S^{-1}$, so $SS^*=I$.
- (b)⇒(c): by definition of inverse.
- (c)⇒(d): $S^*S=I$, so $Se_1,\dots,Se_n$ is orthonormal (7.49 (b)⇔(d)). Its length is $\dim V$, so it is a basis.
- (d)⇒(e): by 7.49 $S$ is unitary, so $(S^*)^*S^*=SS^*=I$ and $S^*$ is an isometry. The columns of $\mathcal M(S^*)$ then form an orthonormal basis. The rows of $\mathcal M(S)$ are the complex conjugates of those columns.
- (e)⇒(f): the columns of $\mathcal M(S^*)$ are orthonormal, so $S^*$ is an isometry by 7.49 (a)⇔(e).
- (f)⇒(a): apply the chain (a)⇒(f) to $S^*$ and get that $(S^*)^*=S$ is unitary.

**The analogy with $\mathbf C$.** Under the analogy $z\leftrightarrow S$, $\bar z\leftrightarrow S^*$: the real numbers ($z=\bar z$) correspond to self-adjoint operators, and nonnegative numbers to positive operators. The unit circle ($|z|=1$, equivalent to $\bar zz=1$) corresponds to $S^*S=I$, i.e. unitary operators. (p. 262)

**7.54 Eigenvalues of unitary operators have absolute value 1.** If $Sv=\lambda v$, $v\ne0$, then $|\lambda|\|v\|=\|\lambda v\|=\|Sv\|=\|v\|$, so $|\lambda|=1$. (p. 262)

**7.55 Unitary operators on complex spaces.** Let $\mathbf F=\mathbf C$. Then $S$ is unitary iff there is an orthonormal basis of $V$ consisting of eigenvectors of $S$ whose eigenvalues all have absolute value 1. (p. 262)
- (a)⇒(b): by 7.53 (a)⇔(b), $S$ is normal. The complex spectral theorem (7.31) gives an orthonormal eigenbasis, and 7.54 gives $|\lambda|=1$.
- (b)⇒(a): if $Se_j=\lambda_je_j$ with $|\lambda_j|=1$, then $\langle Se_j,Se_k\rangle=\lambda_j\overline{\lambda_k}\langle e_j,e_k\rangle$, which is $0$ for $j\ne k$ and $1$ for $j=k$. So $Se_1,\dots,Se_n$ is an orthonormal basis, and 7.53 (a)⇔(d) applies.

*Intuition note.* A unitary operator preserves norms, as rotations of $\mathbf R^2$ do (7.52). Over $\mathbf C$ it is in some orthonormal basis a diagonal map that only multiplies each coordinate by a number on the unit circle.

**QR Factorization.** Here matrices are $n$-by-$n$ and the operators live on $\mathbf F^n$ with the Euclidean inner product and standard basis. (p. 263)

**7.56 Definition.** An $n$-by-$n$ matrix is *unitary* if its columns form an orthonormal list in $\mathbf F^n$ (equivalently a basis, since the length is $n$). Rows could replace columns (by 7.53). $S$ is unitary iff $\mathcal M(S,(e_k),(f_k))$ is a unitary matrix for orthonormal bases $(e_k),(f_k)$. (p. 263)

**7.57 Characterizations of unitary matrices.** For an $n$-by-$n$ matrix $Q$ the following are equivalent. The proof is left to the reader (Exercise 17). (p. 263)
- (a) $Q$ is unitary.
- (b) The rows of $Q$ are an orthonormal list.
- (c) $\|Qv\|=\|v\|$ for every $v\in\mathbf F^n$.
- (d) $Q^*Q=QQ^*=I$, where $Q^*$ is the conjugate transpose.

**7.58 QR factorization.** If $A$ is a square matrix with linearly independent columns, then there exist unique matrices $Q,R$ with $Q$ unitary, $R$ upper triangular with only positive diagonal entries, and $A=QR$. If $A\in\mathbf F^{n,n}$, so are $Q,R$. (p. 264)

*Proof.* (p. 264)
- Let $v_1,\dots,v_n$ be the columns of $A$. Gram–Schmidt (6.32) gives an orthonormal basis $e_1,\dots,e_n$ with $\operatorname{span}(v_1,\dots,v_k)=\operatorname{span}(e_1,\dots,e_k)$ for each $k$ (7.59).
- Define $R_{j,k}=\langle v_k,e_j\rangle$. If $j>k$, $e_j$ is orthogonal to $\operatorname{span}(e_1,\dots,e_k)\ni v_k$, so $R_{j,k}=0$. Thus $R$ is upper triangular.
- Let $Q$ have columns $e_1,\dots,e_n$. Column $k$ of $QR$ is a combination of the columns of $Q$ with coefficients from column $k$ of $R$ (3.51(a)), namely $\langle v_k,e_1\rangle e_1+\dots+\langle v_k,e_k\rangle e_k$. By 6.30(a) this equals $v_k$, so $A=QR$.
- By the Gram–Schmidt equations, $v_k$ is a positive multiple of $e_k$ plus a combination of $e_1,\dots,e_{k-1}$. So each $\langle v_k,e_k\rangle>0$: the diagonal of $R$ is positive.
- Uniqueness: suppose also $A=\widehat Q\widehat R$ with the same properties and columns $q_1,\dots,q_n$ of $\widehat Q$. Each $v_k$ is a combination of $q_1,\dots,q_k$ with coefficients from column $k$ of $\widehat R$. Hence $\operatorname{span}(v_1,\dots,v_k)=\operatorname{span}(q_1,\dots,q_k)$ and $\langle v_k,q_k\rangle>0$. By the uniqueness of such orthonormal lists (Exercise 10, Section 6B), $q_k=e_k$. So $\widehat Q=Q$, and then $\widehat R=R$.

*Intuition note.* QR is Gram–Schmidt written as a matrix product. $Q$ holds the orthonormalised columns, and $R$ records how each original column is built from them. The triangular shape arises because $v_k$ only involves $e_1,\dots,e_k$.

**7.60 Example.** $A=\begin{pmatrix}1&2&1\\0&1&-4\\0&3&2\end{pmatrix}$, with columns $v_1=(1,0,0)$, $v_2=(2,1,3)$, $v_3=(1,-4,2)$. Gram–Schmidt gives $e_1=(1,0,0)$, $e_2=\left(0,\tfrac1{\sqrt{10}},\tfrac3{\sqrt{10}}\right)$, $e_3=\left(0,-\tfrac3{\sqrt{10}},\tfrac1{\sqrt{10}}\right)$. Then (p. 265)
$$Q=\begin{pmatrix}1&0&0\\0&\frac1{\sqrt{10}}&-\frac3{\sqrt{10}}\\0&\frac3{\sqrt{10}}&\frac1{\sqrt{10}}\end{pmatrix},\qquad R=\begin{pmatrix}1&2&1\\0&\sqrt{10}&\frac{\sqrt{10}}5\\0&0&\frac{7\sqrt{10}}5\end{pmatrix},$$
and multiplying out confirms $QR=A$.

**Solving $Ax=b$ with QR.** With $A=QR$, the equation $Ax=b$ is $QRx=b$. Multiplying by $Q^*$ and using 7.57(d) gives $Rx=Q^*b$. $Q^*b$ is easy to compute. Since $R$ is upper triangular with positive diagonal, solve for $x_n$ first, then $x_{n-1}$, and so on. No Gaussian elimination is needed. (p. 266) Axler adds that QR is the main tool of the QR algorithm for approximating eigenvalues and eigenvectors (not discussed here). (p. 264)

**Cholesky Factorization.**

**7.61 Positive invertible operator.** A self-adjoint $T$ is a positive invertible operator iff $\langle Tv,v\rangle>0$ for every nonzero $v$. (p. 266)
- (⇒) $T$ invertible and $v\ne0$ give $Tv\ne0$. By 7.43, $\langle Tv,v\rangle\ne0$, hence $>0$.
- (⇐) $\langle Tv,v\rangle>0$ for $v\ne0$ forces $Tv\ne0$, so $T$ is injective, hence invertible.

**7.62 Definition (positive definite matrix).** $B\in\mathbf F^{n,n}$ is *positive definite* if $B^*=B$ and $\langle Bx,x\rangle>0$ for every nonzero $x\in\mathbf F^n$. (p. 266)

**7.63 Cholesky factorization.** If $B$ is positive definite, there is a unique upper-triangular matrix $R$ with only positive diagonal entries such that $B=R^*R$. (p. 267)

*Proof.* (p. 267)
- Existence: by 7.38 (a)⇔(f), $B=A^*A$ for some invertible $A$ of the same size. Let $A=QR$ (7.58). Then $A^*=R^*Q^*$, so $B=A^*A=R^*Q^*QR=R^*R$.
- Uniqueness: let $S$ be upper triangular with positive diagonal and $B=S^*S$. $S$ is invertible because $B$ is (Exercise 11, Section 3D). Then $BS^{-1}=S^*$, and
$$(AS^{-1})^*(AS^{-1})=(S^*)^{-1}A^*AS^{-1}=(S^*)^{-1}BS^{-1}=(S^*)^{-1}S^*=I .$$
So $AS^{-1}$ is unitary, and $A=(AS^{-1})S$ is a QR-type factorization of $A$. By uniqueness in 7.58, $S=R$.

Axler remarks: the transpose-conjugate $R^*$ is lower triangular, so $B$ is written as lower-triangular times its conjugate transpose (p. 267). $A$ could be taken as the positive square root of $B$ (7.39), but a more general $A$ is allowed because another choice may be easier to find for a specific $B$. (p. 267) Cholesky found the factorization; it was published posthumously in 1924. (p. 267)

*Intuition note.* A positive definite matrix can be written as $A^*A$ with $A$ invertible (as used on p. 267). QR on $A$ turns this into $R^*R$ with a triangular $R$, a square root that is cheap to use.

## Toy example (ours, not from the text)
Take $B=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ on $\mathbf R^2$.

1. *Positive:* $B$ is symmetric. $\langle B(x,y),(x,y)\rangle=2x^2+2xy+2y^2=x^2+y^2+(x+y)^2$. This is $>0$ unless $x=y=0$, so $B$ is positive definite (7.61/7.62).
2. *Square root via 7.38/7.39:* eigenvectors $\tfrac1{\sqrt2}(1,1)$ with eigenvalue $3$ and $\tfrac1{\sqrt2}(1,-1)$ with eigenvalue $1$ (check: $B(1,1)=(3,3)$, $B(1,-1)=(1,-1)$). So $\sqrt B=\sqrt3\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}+1\cdot\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}=\tfrac12\begin{pmatrix}\sqrt3+1&\sqrt3-1\\ \sqrt3-1&\sqrt3+1\end{pmatrix}$.
   Check $(\sqrt B)^2$: diagonal entry $\tfrac14[(\sqrt3+1)^2+(\sqrt3-1)^2]=\tfrac14(4+2\sqrt3+4-2\sqrt3)=2$. Off-diagonal entry $\tfrac14\cdot2(\sqrt3+1)(\sqrt3-1)=\tfrac14\cdot2\cdot2=1$.
3. *Cholesky (7.63):* seek $R=\begin{pmatrix}a&b\\0&c\end{pmatrix}$ with $a,c>0$ and $R^*R=\begin{pmatrix}a^2&ab\\ab&b^2+c^2\end{pmatrix}=B$. Then $a^2=2$, so $a=\sqrt2$. $ab=1$, so $b=\tfrac1{\sqrt2}$. $b^2+c^2=2$, so $c^2=2-\tfrac12=\tfrac32$ and $c=\sqrt{3/2}$. Verify: $R^*R$ has entries $\sqrt2\cdot\sqrt2=2$; $\sqrt2\cdot\tfrac1{\sqrt2}=1$; $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}+\tfrac32=\tfrac12+\tfrac32=2$. This is $B$, and the positive diagonal makes $R$ the unique such factor.

## Concepts
- [[positive (semi)definite matrix]] — Axler's "positive operator": self-adjoint with $\langle Tv,v\rangle\ge0$; "positive definite" (matrix) needs $>0$ for $x\neq0$ (pp. 251, 266)
- [[operator-square-root]] (new) — $R$ with $R^2=T$; a positive operator has exactly one positive square root $\sqrt T$ (pp. 251, 253)
- [[spectral theorem]] — used for the eigenbasis behind 7.38, 7.39, 7.55 (pp. 252–253, 262)
- [[orthonormal basis / orthogonal matrix]] — the unitary matrix/operator (conjugate-transpose version): $S^*S=SS^*=I$, columns and rows orthonormal (pp. 260–263)
- [[isometry]] (new) — linear map $S\in\mathcal L(V,W)$ with $\|Sv\|=\|v\|$; equivalent to $S^*S=I$ (pp. 258–259)
- [[Gram–Schmidt and QR]] — $A=QR$ for square $A$ with independent columns, $Q$ unitary, $R$ upper triangular with positive diagonal; unique (p. 264)
- [[cholesky-factorization]] (new) — $B=R^*R$ with $R$ upper triangular, positive diagonal, for positive definite $B$ (p. 267)
- [[norm]] — the quantity preserved by isometries (p. 258)

## Canonical instances
- [[rotation-matrix-unitary]] (new) — rotation of $\mathbf R^2$ as a unitary operator (7.52) (p. 260)
- [[sqrt-of-2x2-positive-operators]] (new) — $\sqrt S,\sqrt T$ for $S(x,y)=(x,2y)$, $T(x,y)=(x+y,x+y)$ (7.41) (p. 254)
- [[qr-3x3-example]] (new) — QR factorization of a 3-by-3 matrix (7.60) (p. 265)
- [[nilpotent-square-root-example]] (new) — $R(z_1,z_2,z_3)=(z_2,z_3,0)$ squares to $(z_3,0,0)$ (7.37) (p. 251)

## Bridges (candidates)
- [structural-analogy] positive operators ↔ nonnegative real numbers; self-adjoint ↔ real; unitary ↔ unit circle — Axler states this analogy (p. 262).
- [same-math] QR factorization ↔ Gram–Schmidt and QR (canon): $Q$ is the Gram–Schmidt output and $R_{j,k}=\langle v_k,e_j\rangle$.
- [same-math] Cholesky $B=R^*R$ ↔ positive (semi)definite matrices (canon): "Gram matrix" form $A^*A$ (7.38 (f)), refined to a triangular factor.
- [same-math] unitary operator over $\mathbf R$ ↔ orthogonal matrix ($Q^TQ=I$) in the canon.
- [structural-analogy] $\|Sv\|=\|v\|$ and $S^*S=I$ ↔ condition-number intuition: unitary maps have no error amplification (canon link; not stated in this unit).

## Questions this raises
- 7.38 and 7.61 cover positive and positive invertible operators. Where does the dividing line between "positive" and "positive definite" matter in practice, e.g. when $\sqrt T$ is not invertible?
- Cholesky uses QR on an arbitrary $A$ with $B=A^*A$. How would one find such an $A$ cheaply for a given $B$ (Axler says another choice than $\sqrt B$ may be easier)?
- Axler says QR is the main tool of the QR algorithm for eigenvalue approximation. How does that iteration use repeated QR steps?
- For a non-square matrix with independent columns, what replaces $Q$ and $R$ (7.58 is stated only for square matrices)?

## Exercises worth doing
- Ex. 7C.5 (p. 255) — a self-adjoint $T$ is positive iff diagonal entries of its matrix are nonnegative in *every* orthonormal basis — difficulty: medium
- Ex. 7C.13 (p. 256) — $T-\alpha I$ is positive iff $\alpha$ is at most every eigenvalue of $T$ — difficulty: medium
- Ex. 7C.18 (p. 256) — the product of two positive operators is positive iff they commute — difficulty: hard
- Ex. 7C.23 (p. 257) — inner products on $V$ are exactly $\langle Tu,v\rangle$ for positive invertible $T$ — difficulty: hard
- Ex. 7D.1 (p. 268) — an isometry is detected by its action on orthonormal pairs — difficulty: medium
- Ex. 7D.3 (p. 268) — unitary operators form a group — difficulty: easy
- Ex. 7D.17 (p. 269) — prove the characterizations 7.57 of unitary matrices — difficulty: easy
- Ex. 7D.19 (p. 269) — the discrete Fourier transform is unitary and $\mathcal F^4=I$ — difficulty: hard

## Reading notes
- This unit is part 2/3 of Chapter 7. It starts at the beginning of Section 7C (printed p. 251) and ends after Exercises 7D (printed p. 269). The split is at a section boundary: the section after 7D is not covered.
- Printed page = pdf page − 14.
- The text layer garbles math letters; all formulas were read from the page images. No misprints noticed.
- The proof of 7.57 is left to the reader (Exercise 17, p. 269). In the Cholesky proof (p. 267), the text asserts that positive definite $B$ equals $A^*A$ for an invertible $A$, citing 7.38. That $A$ is invertible is not spelled out there; 7.61 gives that a positive definite matrix is invertible.
- The proofs of 7.26 and 7.14 and of the spectral theorem 7.29/7.31 are cited but lie outside this unit.
