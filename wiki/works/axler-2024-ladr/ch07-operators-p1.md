---
id: axler-2024-ladr/ch07-operators-p1
work: axler-2024-ladr
unit: "7 Operators on Inner Product Spaces (part 1/3): 7A Self-Adjoint and Normal Operators, 7B Spectral Theorem"
pages: 227-250
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Adjoints, self-adjoint and normal operators, and the spectral theorems

## L0 — One line
On a finite-dimensional inner product space, an operator has an orthonormal basis of eigenvectors exactly when it is self-adjoint (real case) or normal (complex case).

## L1 — The gist (≤ 120 words)
Which operators can be diagonalized using an orthonormal basis? The chapter defines the adjoint $T^*$, the operator satisfying $\langle Tv,w\rangle=\langle v,T^*w\rangle$. It then studies two classes: self-adjoint operators ($T=T^*$) and normal operators ($TT^*=T^*T$). The spectral theorems answer the question. Over $\mathbf R$, the operators with such a basis are exactly the self-adjoint ones. Over $\mathbf C$, they are exactly the normal ones. Along the way: self-adjoint operators have real eigenvalues, and normal operators share eigenvectors with their adjoints. Eigenvectors for distinct eigenvalues of a normal operator are orthogonal. These operators are completely understood, and later results on positive operators and the SVD build on them.

**Prerequisites:** inner products, orthonormal bases, Riesz representation theorem, orthogonal complements, matrix of a linear map, eigenvalues, minimal polynomial, Schur's theorem (upper-triangular matrix in an orthonormal basis).

## L2 — Key ideas (5–10 bullets)
- The adjoint $T^*$ is defined through the Riesz representation theorem. It is automatically linear and basis-free. With orthonormal bases, its matrix is the conjugate transpose of the matrix of $T$ (pp. 228–232).
- $\operatorname{null}T^*=(\operatorname{range}T)^\perp$ and $\operatorname{range}T^*=(\operatorname{null}T)^\perp$, so orthogonal complements link a map to its adjoint (p. 231).
- Self-adjoint operators behave like real numbers: they have real eigenvalues (p. 233). On a complex space, $\langle Tv,v\rangle$ is real for all $v$ iff $T$ is self-adjoint (p. 234).
- Normal operators satisfy $\|Tv\|=\|T^*v\|$ for all $v$. Hence $\operatorname{null}T=\operatorname{null}T^*$, $T$ and $T^*$ share eigenvectors (with conjugate eigenvalues), and eigenvectors for distinct eigenvalues are orthogonal (pp. 236–238).
- On a complex space, $T$ is normal iff $T=A+iB$ with $A,B$ commuting self-adjoint operators ("real and imaginary parts") (p. 238).
- For self-adjoint $T$ and $b^2<4c$, $T^2+bT+cI$ is invertible. Hence the minimal polynomial of a self-adjoint operator is a product of real linear factors (pp. 243–244).
- Real spectral theorem: for $\mathbf F=\mathbf R$, self-adjoint ⟺ diagonal matrix in some orthonormal basis ⟺ orthonormal basis of eigenvectors (p. 245).
- Complex spectral theorem: the same equivalences for $\mathbf F=\mathbf C$ with "normal" in place of "self-adjoint". The proof uses Schur's theorem plus $\|Te_k\|=\|T^*e_k\|$ row by row (p. 246).

## L3 — Walkthrough

### Chapter 7 opening (p. 227)
The chapter studies linear maps and operators on inner product spaces. The author says the adjoint gives good theorems. The spectral theorem describes self-adjoint operators on real spaces and normal operators on complex spaces. It leads to positive operators, unitary operators, matrix factorizations, the singular value decomposition and the polar decomposition (those later topics are not in these pages). From now on, spaces are finite-dimensional. Standing assumptions: $\mathbf F$ is $\mathbf R$ or $\mathbf C$; $V$ and $W$ are nonzero finite-dimensional inner product spaces over $\mathbf F$ (p. 227).

### 7A Self-Adjoint and Normal Operators

#### Adjoints
**7.1 Definition.** For $T\in\mathcal L(V,W)$, the *adjoint* is the function $T^*:W\to V$ with
$$\langle Tv,w\rangle=\langle v,T^*w\rangle\quad\text{for every }v\in V,\ w\in W.$$
Why it is well defined: fix $w$. The map $v\mapsto\langle Tv,w\rangle$ is a linear functional on $V$. By the Riesz representation theorem (6.42) it is $v\mapsto\langle v,\text{one unique vector}\rangle$, and that vector is called $T^*w$. The left inner product is in $W$, the right one in $V$ (p. 228). The word "adjoint" has an unrelated second meaning elsewhere in linear algebra (p. 228).

**7.2 Example.** $T:\mathbf R^3\to\mathbf R^2$, $T(x_1,x_2,x_3)=(x_2+3x_3,\,2x_1)$. Then
$$\langle T(x_1,x_2,x_3),(y_1,y_2)\rangle=x_2y_1+3x_3y_1+2x_1y_2=\langle(x_1,x_2,x_3),(2y_2,y_1,3y_1)\rangle,$$
so $T^*(y_1,y_2)=(2y_2,\,y_1,\,3y_1)$ (p. 228).

**7.3 Example.** Fix $u\in V$, $x\in W$ and set $Tv=\langle v,u\rangle x$. Then $\langle Tv,w\rangle=\langle v,u\rangle\langle x,w\rangle=\langle v,\langle w,x\rangle u\rangle$. So $T^*w=\langle w,x\rangle u$ (p. 229).

*Technique (author's margin note):* start from $\langle Tv,w\rangle$ and manipulate it until $v$ alone is in the first slot. The second slot is then $T^*w$ (p. 229).

**7.4 The adjoint is linear.** If $T\in\mathcal L(V,W)$ then $T^*\in\mathcal L(W,V)$. Proof:
- Additivity: $\langle Tv,w_1+w_2\rangle=\langle Tv,w_1\rangle+\langle Tv,w_2\rangle=\langle v,T^*w_1\rangle+\langle v,T^*w_2\rangle=\langle v,T^*w_1+T^*w_2\rangle$. So $T^*(w_1+w_2)=T^*w_1+T^*w_2$.
- Homogeneity: $\langle Tv,\lambda w\rangle=\bar\lambda\langle Tv,w\rangle=\bar\lambda\langle v,T^*w\rangle=\langle v,\lambda T^*w\rangle$. So $T^*(\lambda w)=\lambda T^*w$ (p. 229).

**7.5 Properties of the adjoint.** For $T\in\mathcal L(V,W)$ (p. 230):
- (a) $(S+T)^*=S^*+T^*$ for $S\in\mathcal L(V,W)$.
- (b) $(\lambda T)^*=\bar\lambda T^*$.
- (c) $(T^*)^*=T$.
- (d) $(ST)^*=T^*S^*$ for $S\in\mathcal L(W,U)$, with $U$ a finite-dimensional inner product space over $\mathbf F$.
- (e) $I^*=I$ for the identity $I$ on $V$.
- (f) If $T$ is invertible, then $T^*$ is invertible and $(T^*)^{-1}=(T^{-1})^*$.

Each part is proved by computing $\langle(\cdot)v,w\rangle$ and moving everything to the second slot. Example, (d): $\langle(ST)v,u\rangle=\langle Tv,S^*u\rangle=\langle v,T^*(S^*u)\rangle$. For (c): $\langle T^*w,v\rangle=\overline{\langle v,T^*w\rangle}=\overline{\langle Tv,w\rangle}=\langle w,Tv\rangle$. For (f): take adjoints of $T^{-1}T=I$ and $TT^{-1}=I$ and use (d) and (e). If $\mathbf F=\mathbf R$, then $T\mapsto T^*$ is linear. If $\mathbf F=\mathbf C$ it is not, because of the conjugate in (b) (p. 230).

**7.6 Null space and range of $T^*$.** For $T\in\mathcal L(V,W)$ (p. 231):
- (a) $\operatorname{null}T^*=(\operatorname{range}T)^\perp$
- (b) $\operatorname{range}T^*=(\operatorname{null}T)^\perp$
- (c) $\operatorname{null}T=(\operatorname{range}T^*)^\perp$
- (d) $\operatorname{range}T=(\operatorname{null}T^*)^\perp$

Proof of (a): $w\in\operatorname{null}T^*\iff T^*w=0\iff\langle v,T^*w\rangle=0\ \forall v\iff\langle Tv,w\rangle=0\ \forall v\iff w\in(\operatorname{range}T)^\perp$. Taking orthogonal complements of (a) gives (d), using 6.52. Applying (a) to $T^*$, with 7.5(c), gives (c). Applying (d) to $T^*$ gives (b) (p. 231).

*Intuition note:* $T^*$ kills exactly the vectors perpendicular to everything $T$ can output. So the four spaces (null and range of $T$ and $T^*$) come in orthogonal pairs.

**7.7 Definition.** The *conjugate transpose* of an $m$-by-$n$ matrix $A$ is the $n$-by-$m$ matrix $A^*$ with $(A^*)_{j,k}=\overline{A_{k,j}}$ (p. 231).

**7.8 Example.** The conjugate transpose of $\begin{pmatrix}2&3+4i&7\\6&5&8i\end{pmatrix}$ is $\begin{pmatrix}2&6\\3-4i&5\\7&-8i\end{pmatrix}$. For a real matrix, $A^*=A^{\mathrm t}$ (p. 231).

**7.9 Matrix of $T^*$.** Let $T\in\mathcal L(V,W)$, $e_1,\dots,e_n$ an orthonormal basis of $V$, $f_1,\dots,f_m$ an orthonormal basis of $W$. Then
$$\mathcal M(T^*)=(\mathcal M(T))^*,$$
with $\mathcal M(T)$ taken w.r.t. $(e),(f)$ and $\mathcal M(T^*)$ w.r.t. $(f),(e)$ (p. 232). So $\mathcal M(T)$ is $m\times n$ and $\mathcal M(T^*)$ is $n\times m$.
Proof: by 6.30(a), $Te_k=\langle Te_k,f_1\rangle f_1+\dots+\langle Te_k,f_m\rangle f_m$. So entry (row $j$, column $k$) of $\mathcal M(T)$ is $\langle Te_k,f_j\rangle$. Swapping roles, entry $(j,k)$ of $\mathcal M(T^*)$ is $\langle T^*f_k,e_j\rangle=\langle f_k,Te_j\rangle=\overline{\langle Te_j,f_k\rangle}$. That is the conjugate of entry $(k,j)$ of $\mathcal M(T)$ (p. 232).

**Caution:** for nonorthonormal bases the matrix of $T^*$ need not be the conjugate transpose. The adjoint itself does not depend on a basis, which is why the author emphasizes adjoints over transposes (p. 232). The author also remarks that, under the Riesz identification of $V$ with $V'$, $T^*$ corresponds to the dual map $T'$. Formulas 7.6(a), (b) then match those for $T'$, and 7.9 is analogous to 3.132. The author says no annihilators or dual maps are needed in inner product spaces (p. 232; Exercise 32).

#### Self-adjoint operators
**7.10 Definition.** $T\in\mathcal L(V)$ is *self-adjoint* if $T=T^*$. With an orthonormal basis, $T$ is self-adjoint iff $\mathcal M(T)=\mathcal M(T)^*$, by 7.9. Equivalently, $\langle Tv,w\rangle=\langle v,Tw\rangle$ for all $v,w$ (p. 233).

**7.11 Example.** On $\mathbf F^2$, $\mathcal M(T)=\begin{pmatrix}2&c\\3&7\end{pmatrix}$ and $\mathcal M(T^*)=\begin{pmatrix}2&3\\\bar c&7\end{pmatrix}$. So $T$ is self-adjoint iff $c=3$ (p. 233).

*Analogy (author):* the adjoint plays the role of complex conjugation. A complex number is real iff $z=\bar z$, so a self-adjoint operator is analogous to a real number (p. 233).

**7.12 Eigenvalues are real.** Every eigenvalue of a self-adjoint operator is real. Proof: if $Tv=\lambda v$, $v\ne0$, then $\lambda\|v\|^2=\langle Tv,v\rangle=\langle v,Tv\rangle=\bar\lambda\|v\|^2$, so $\lambda=\bar\lambda$. For $\mathbf F=\mathbf R$ this is true by definition, so it is interesting only for $\mathbf F=\mathbf C$ (p. 233).

**7.13** (complex only). Suppose $V$ is a complex inner product space and $T\in\mathcal L(V)$. Then $\langle Tv,v\rangle=0$ for every $v\iff T=0$. It is false for real spaces: the 90° rotation $T(x,y)=(-y,x)$ on $\mathbf R^2$ has $Tv\perp v$ for all $v$ but $T\neq0$ (p. 234). Proof uses the identity, checkable by expanding the right side:
$$\langle Tu,w\rangle=\frac{\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle}{4}+\frac{\langle T(u+iw),u+iw\rangle-\langle T(u-iw),u-iw\rangle}{4}\,i.$$
Each term has the form $\langle Tv,v\rangle$. If all vanish, then $\langle Tu,w\rangle=0$ for all $u,w$. Taking $w=Tu$ gives $Tu=0$ (p. 234).

**7.14** (complex only). $T$ is self-adjoint $\iff\langle Tv,v\rangle\in\mathbf R$ for every $v$. Proof: $\langle T^*v,v\rangle=\overline{\langle Tv,v\rangle}$ (7.15). Then $T=T^*\iff T-T^*=0\iff\langle(T-T^*)v,v\rangle=0\ \forall v$ (by 7.13 applied to $T-T^*$) $\iff\langle Tv,v\rangle-\overline{\langle Tv,v\rangle}=0\ \forall v\iff\langle Tv,v\rangle\in\mathbf R\ \forall v$. The author says it fails on real spaces as shown by considering any operator on a real inner product space that is not self-adjoint (p. 234).

**7.16.** If $T$ is self-adjoint on $V$ (either field), then $\langle Tv,v\rangle=0$ for every $v\iff T=0$. The complex case is 7.13. For real $V$: since $T$ is self-adjoint and the space is real, $\langle Tw,u\rangle=\langle w,Tu\rangle=\langle Tu,w\rangle$. Hence
$$\langle Tu,w\rangle=\frac{\langle T(u+w),u+w\rangle-\langle T(u-w),u-w\rangle}{4}\tag{7.17}$$
and then take $w=Tu$ as before (p. 235).

*Intuition note:* a real number $x$ with $x\cdot v^2=0$ for all $v$ must be $0$. Self-adjoint operators have the same property because their "quadratic form" $\langle Tv,v\rangle$ determines them. Non-self-adjoint real operators (rotation) can hide from it.

#### Normal operators
**7.18 Definition.** $T\in\mathcal L(V)$ is *normal* if it commutes with its adjoint: $TT^*=T^*T$. Every self-adjoint operator is normal (p. 235).

**7.19 Example.** $T(w,z)=(2w-3z,\,3w+2z)$, matrix $\begin{pmatrix}2&-3\\3&2\end{pmatrix}$. It is not self-adjoint, since the (2,1) entry $3$ is not the conjugate of the (1,2) entry $-3$. But
$$TT^*\leftrightarrow\begin{pmatrix}2&-3\\3&2\end{pmatrix}\begin{pmatrix}2&3\\-3&2\end{pmatrix}=\begin{pmatrix}13&0\\0&13\end{pmatrix},\qquad T^*T\leftrightarrow\begin{pmatrix}2&3\\-3&2\end{pmatrix}\begin{pmatrix}2&-3\\3&2\end{pmatrix}=\begin{pmatrix}13&0\\0&13\end{pmatrix}.$$
So $T$ is normal (pp. 235–236).

**7.20.** $T$ is normal $\iff\|Tv\|=\|T^*v\|$ for every $v\in V$. Proof chain: $T$ normal $\iff T^*T-TT^*=0\iff\langle(T^*T-TT^*)v,v\rangle=0\ \forall v\iff\langle Tv,Tv\rangle=\langle T^*v,T^*v\rangle\ \forall v\iff\|Tv\|=\|T^*v\|\ \forall v$. The second step uses 7.16, because $T^*T-TT^*$ is self-adjoint (p. 236).

**7.21 Normal operator facts.** For normal $T\in\mathcal L(V)$ (p. 237):
- (a) $\operatorname{null}T=\operatorname{null}T^*$. Proof: $v\in\operatorname{null}T\iff\|Tv\|=0\iff\|T^*v\|=0$ (by 7.20) $\iff v\in\operatorname{null}T^*$.
- (b) $\operatorname{range}T=\operatorname{range}T^*$. Proof: $\operatorname{range}T=(\operatorname{null}T^*)^\perp=(\operatorname{null}T)^\perp=\operatorname{range}T^*$, via 7.6(d), (a), 7.6(b).
- (c) $V=\operatorname{null}T\oplus\operatorname{range}T$. Proof: $V=\operatorname{null}T\oplus(\operatorname{null}T)^\perp=\operatorname{null}T\oplus\operatorname{range}T^*=\operatorname{null}T\oplus\operatorname{range}T$, via 6.49, 7.6(b), (b).
- (d) $T-\lambda I$ is normal for every $\lambda\in\mathbf F$. Proof: $(T-\lambda I)(T^*-\bar\lambda I)=TT^*-\bar\lambda T-\lambda T^*+|\lambda|^2I=T^*T-\bar\lambda T-\lambda T^*+|\lambda|^2I=(T^*-\bar\lambda I)(T-\lambda I)$. The middle step uses $TT^*=T^*T$.
- (e) $Tv=\lambda v\iff T^*v=\bar\lambda v$. Proof: by (d) and 7.20, $\|(T-\lambda I)v\|=\|(T^*-\bar\lambda I)v\|$, so one is $0$ iff the other is.

The author notes that Exercise 3 (eigenvalues of $T^*$ are conjugates of those of $T$) says nothing about eigenvectors. In general $T$ and $T^*$ may have different eigenvectors. For normal $T$, (e) says they have the same eigenvectors (p. 236).

**7.22 Orthogonal eigenvectors.** If $T$ is normal, eigenvectors for distinct eigenvalues are orthogonal. Proof: let $Tu=\alpha u$, $Tv=\beta v$, $\alpha\neq\beta$. By 7.21(e), $T^*v=\bar\beta v$. Then $(\alpha-\beta)\langle u,v\rangle=\langle\alpha u,v\rangle-\langle u,\bar\beta v\rangle=\langle Tu,v\rangle-\langle u,T^*v\rangle=0$. So $\langle u,v\rangle=0$. This applies to self-adjoint operators too (p. 238).

**7.23** ($\mathbf F=\mathbf C$). $T$ is normal iff there exist commuting self-adjoint operators $A,B$ with $T=A+iB$. If $T$ is normal, set
$$A=\frac{T+T^*}{2},\qquad B=\frac{T-T^*}{2i}\tag{7.24}$$
Then $A,B$ are self-adjoint, $T=A+iB$, and
$$AB-BA=\frac{T^*T-TT^*}{2i}\tag{7.25}$$
which is $0$ for normal $T$. Conversely, if $T=A+iB$ with $A,B$ commuting and self-adjoint, then $T^*=A-iB$. Adding and subtracting give 7.24, hence 7.25. Commuting $A,B$ then make the right side of 7.25 zero, so $T$ is normal (p. 238). The author says $A,B$ correspond to real and imaginary parts of $T$ under the adjoint/conjugate analogy. Exercise 12 gives a version that works over both fields (p. 238).

*Intuition note:* a normal operator is one whose "real part" and "imaginary part" do not interfere with each other (they commute). The matrix of $T^*T-TT^*$ measures that failure.

**Exercises 7A** (pp. 239–242) are listed below under Exercises. They include: formulas for adjoints (Ex. 1, 14, 31), rank and dimension results (Ex. 6–8), the 90° rotation (Ex. 11), and a basis-independent sum $\sum\|Te_k\|^2=\sum\|T^*f_j\|^2$ (Ex. 5).

### 7B Spectral Theorem

#### Setting (p. 243)
An operator is diagonalizable iff $V$ has a basis of eigenvectors (5.55). The "nicest" operators have an *orthonormal* basis of eigenvectors, equivalently a diagonal matrix in some orthonormal basis. The goal is to characterize them: self-adjoint operators when $\mathbf F=\mathbf R$, normal operators when $\mathbf F=\mathbf C$. The author calls the spectral theorem probably the most useful tool for operators on inner product spaces (p. 243).

#### Real Spectral Theorem
Two preliminary results are needed (valid over both fields, but not needed for the complex case) (p. 243).

*Motivation:* if $b,c\in\mathbf R$, $b^2<4c$, $x\in\mathbf R$, then $x^2+bx+c=(x+\tfrac b2)^2+(c-\tfrac{b^2}{4})>0$. Replace $x$ by a self-adjoint operator (p. 243).

**7.26 Invertible quadratic expressions.** If $T\in\mathcal L(V)$ is self-adjoint and $b,c\in\mathbf R$ with $b^2<4c$, then $T^2+bT+cI$ is invertible.
Proof: take $v\neq0$. Using $T=T^*$ (added step: this gives $\langle T^2v,v\rangle=\langle Tv,Tv\rangle$) and Cauchy–Schwarz (6.14),
$$\begin{aligned}\langle(T^2+bT+cI)v,v\rangle&=\langle Tv,Tv\rangle+b\langle Tv,v\rangle+c\|v\|^2\\&\ge\|Tv\|^2-|b|\,\|Tv\|\,\|v\|+c\|v\|^2\\&=\Big(\|Tv\|-\tfrac{|b|\,\|v\|}{2}\Big)^2+\Big(c-\tfrac{b^2}{4}\Big)\|v\|^2>0.\end{aligned}$$
So $(T^2+bT+cI)v\neq0$. Hence the operator is injective, hence invertible (3.65) (p. 244). Exercise 18 shows the self-adjoint hypothesis cannot be dropped even over $\mathbf R$ (p. 249).

**7.27 Minimal polynomial of a self-adjoint operator.** If $T$ is self-adjoint, its minimal polynomial is $(z-\lambda_1)\cdots(z-\lambda_m)$ for some $\lambda_1,\dots,\lambda_m\in\mathbf R$ (p. 244).
- $\mathbf F=\mathbf C$: the zeros of the minimal polynomial are the eigenvalues (5.27(a)). They are real (7.12). Then the fundamental theorem of algebra (4.13) gives the form.
- $\mathbf F=\mathbf R$: by 4.16 the minimal polynomial is
$$(z-\lambda_1)\cdots(z-\lambda_m)(z^2+b_1z+c_1)\cdots(z^2+b_Nz+c_N)\tag{7.28}$$
with $b_k^2<4c_k$ ($m$ or $N$ may be $0$). Then $(T-\lambda_1I)\cdots(T-\lambda_mI)(T^2+b_1T+c_1I)\cdots(T^2+b_NT+c_NI)=0$. If $N>0$, multiply on the right by the inverse of $T^2+b_NT+c_NI$ (invertible by 7.26). This gives a polynomial in $T$ of degree two less that equals $0$, contradicting minimality. So $N=0$.

The author adds that with 5.27(a), every self-adjoint operator has an eigenvalue (p. 244).

**7.29 Real spectral theorem.** Suppose $\mathbf F=\mathbf R$ and $T\in\mathcal L(V)$. The following are equivalent (p. 245):
- (a) $T$ is self-adjoint.
- (b) $T$ has a diagonal matrix w.r.t. some orthonormal basis of $V$.
- (c) $V$ has an orthonormal basis consisting of eigenvectors of $T$.

Proof, (a)⇒(b): by 6.37 and 7.27, $T$ has an upper-triangular matrix in some orthonormal basis. In that basis, $\mathcal M(T^*)$ is the transpose of $\mathcal M(T)$. Since $T^*=T$, the matrix equals its transpose. Being upper triangular, all entries above and below the diagonal are $0$. (b)⇒(a): a diagonal matrix equals its transpose, so $\mathcal M(T^*)=\mathcal M(T)$ in that basis. (b)⇔(c) follows from the definitions (see 5.55) (p. 245).

**7.30 Example.** On $\mathbf R^3$ the matrix $\begin{pmatrix}14&-13&8\\-13&14&8\\8&8&-7\end{pmatrix}$ equals its transpose, so $T$ is self-adjoint. An orthonormal basis of eigenvectors is $\frac{(1,-1,0)}{\sqrt2},\frac{(1,1,1)}{\sqrt3},\frac{(1,1,-2)}{\sqrt6}$, and the matrix in this basis is $\operatorname{diag}(27,9,-15)$ (p. 245). Exercise 17 extends this to a family of commuting self-adjoint operators (p. 249).

*Intuition note:* in the real case, a symmetric matrix can always be "rotated" into a diagonal one. The key step is 7.27: the minimal polynomial of a self-adjoint operator is a product of real linear factors, which (with 6.37) gives an upper-triangular matrix in an orthonormal basis (p. 245).

#### Complex Spectral Theorem
**7.31 Complex spectral theorem.** Suppose $\mathbf F=\mathbf C$ and $T\in\mathcal L(V)$. The following are equivalent (p. 246):
- (a) $T$ is normal.
- (b) $T$ has a diagonal matrix w.r.t. some orthonormal basis.
- (c) $V$ has an orthonormal basis of eigenvectors of $T$.

Proof, (a)⇒(b): by Schur's theorem (6.38) there is an orthonormal basis $e_1,\dots,e_n$ with
$$\mathcal M(T,(e_1,\dots,e_n))=\begin{pmatrix}a_{1,1}&\cdots&a_{1,n}\\&\ddots&\vdots\\0&&a_{n,n}\end{pmatrix}\tag{7.32}$$
Then $\|Te_1\|^2=|a_{1,1}|^2$ and $\|T^*e_1\|^2=|a_{1,1}|^2+|a_{1,2}|^2+\dots+|a_{1,n}|^2$. Normality gives $\|Te_1\|=\|T^*e_1\|$ (7.20), so the off-diagonal entries of row 1 are $0$. Next, $\|Te_2\|^2=|a_{2,2}|^2$ (because $a_{1,2}=0$) and $\|T^*e_2\|^2=|a_{2,2}|^2+\dots+|a_{2,n}|^2$. Equality of norms kills the off-diagonal entries of row 2. Continuing row by row, all off-diagonal entries are $0$.
(b)⇒(a): $\mathcal M(T^*)$ is the conjugate transpose, also diagonal. Diagonal matrices commute, so $TT^*=T^*T$. (b)⇔(c) follows from the definitions (p. 246).

The main conclusion: every normal operator on a finite-dimensional complex inner product space is diagonalizable by an orthonormal basis (p. 247). Exercises 13 and 20 give alternative proofs of (a)⇒(b). Exercises 14 and 15 restate the theorems as orthogonal direct sums of eigenspaces. Exercise 16 handles several commuting normal operators at once (p. 247).

**7.33 Example.** $T(w,z)=(2w-3z,\,3w+2z)$ is normal (7.19). An orthonormal basis of eigenvectors is $\frac1{\sqrt2}(i,1),\ \frac1{\sqrt2}(-i,1)$, and the matrix is $\begin{pmatrix}2+3i&0\\0&2-3i\end{pmatrix}$ (p. 247).

*Intuition note:* the matrix $\begin{pmatrix}2&-3\\3&2\end{pmatrix}$ has no real eigenvectors in the real plane, but over $\mathbf C$ it has an orthonormal eigenbasis. Its eigenvalues $2\pm3i$ are conjugates, consistent with 7.21(e).

**Exercises 7B** (pp. 247–250) include: a normal operator on a complex space is self-adjoint iff all its eigenvalues are real (Ex. 1), skew iff purely imaginary eigenvalues (Ex. 4), Fuglede's theorem (Ex. 12), eigenvalue approximation (Ex. 23), and the pseudoinverse on an eigenbasis (Ex. 25).

## Toy example (ours, not from the text)
Let $T$ on $\mathbf R^2$ have matrix $S=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ in the standard (orthonormal) basis.
1. **Self-adjoint:** $S^{\mathrm t}=S$, so by 7.9, $T^*=T$. Check with $v=(1,0)$, $w=(0,1)$: $Tv=(2,1)$ so $\langle Tv,w\rangle=1$; $Tw=(1,2)$ so $\langle v,Tw\rangle=1$.
2. **Eigenvectors:** $T(1,1)=(2+1,\,1+2)=(3,3)=3(1,1)$, and $T(1,-1)=(2-1,\,1-2)=(1,-1)=1\cdot(1,-1)$. Eigenvalues $3,1$ are real (7.12).
3. **Orthogonal:** $\langle(1,1),(1,-1)\rangle=1-1=0$ (7.22). Normalize: $e_1=(1,1)/\sqrt2$, $e_2=(1,-1)/\sqrt2$.
4. **Matrix in this basis** (entry $(j,k)$ is $\langle Te_k,e_j\rangle$): $\langle Te_1,e_1\rangle=3\langle e_1,e_1\rangle=3$, $\langle Te_1,e_2\rangle=3\langle e_1,e_2\rangle=0$, $\langle Te_2,e_1\rangle=0$, $\langle Te_2,e_2\rangle=1$. So $\mathcal M(T)=\operatorname{diag}(3,1)$, as the real spectral theorem predicts.
5. **Contrast:** the 90° rotation $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ has $RR^{\mathrm t}=I=R^{\mathrm t}R$, so it is normal. It is not symmetric, so it is not self-adjoint. It has no real eigenvector ($R(x,y)=(-y,x)=\lambda(x,y)$ forces $\lambda^2=-1$), which is why the real theorem needs self-adjointness.

## Concepts
- [[adjoint]] (new) — $T^*$, the unique map with $\langle Tv,w\rangle=\langle v,T^*w\rangle$; exists by Riesz representation (p. 228)
- [[conjugate-transpose]] (new) — swap rows and columns, conjugate entries; the matrix of $T^*$ in orthonormal bases (p. 231)
- [[self-adjoint-operator]] (new) — operator with $T=T^*$; analogue of a real number (p. 233)
- [[normal-operator]] (new) — operator with $TT^*=T^*T$; equivalently $\|Tv\|=\|T^*v\|$ for all $v$ (pp. 235–236)
- [[spectral-theorem]] — real: self-adjoint ⟺ orthonormal eigenbasis; complex: normal ⟺ orthonormal eigenbasis (pp. 245–246). Here stated for operators, not only symmetric matrices.
- [[four-fundamental-subspaces]] — here $\operatorname{null}T^*=(\operatorname{range}T)^\perp$ etc. (7.6) (p. 231)
- [[orthonormal-basis]] — used to turn the adjoint into a conjugate transpose and to state the spectral theorems (p. 232)
- [[diagonalization]] — here "diagonal matrix in an orthonormal basis" (p. 243)
- [[eigenvector-eigenvalue]] — real eigenvalues for self-adjoint operators; shared eigenvectors for normal ones (pp. 233, 237)
- [[minimal-polynomial]] (new) — used in 7.27 to show self-adjoint operators have real linear factors only (p. 244)

## Canonical instances
- [[adjoint-R3-to-R2-example]] — 7.2, $T^*(y_1,y_2)=(2y_2,y_1,3y_1)$ (p. 228)
- [[rank-one-adjoint-example]] — 7.3, $T^*w=\langle w,x\rangle u$ (p. 229)
- [[rotation-90-counterexample]] — $\langle Tv,v\rangle=0$ for all $v$ but $T\ne0$ on $\mathbf R^2$ (p. 234)
- [[normal-not-selfadjoint-example]] — $\begin{pmatrix}2&-3\\3&2\end{pmatrix}$, $TT^*=T^*T=13I$ (p. 236)
- [[real-spectral-example-3x3]] — eigenvalues $27,9,-15$ with explicit orthonormal basis (p. 245)
- [[complex-spectral-example-2x2]] — eigenvalues $2\pm3i$, basis $(\pm i,1)/\sqrt2$ (p. 247)

## Bridges (candidates)
- [same-math] spectral theorem for real symmetric matrices ($S=Q\Lambda Q^{\mathrm t}$) ↔ linear-algebra canon "spectral theorem": 7.29 in matrix form (orthonormal basis ↔ columns of $Q$).
- [same-math] adjoint $T^*$ with real entries = transpose ↔ the transpose in $\operatorname{null}(A^{\mathrm t})=(\operatorname{col}A)^\perp$ (four fundamental subspaces): 7.6 over $\mathbf R$ with orthonormal bases.
- [structural-analogy] self-adjoint operator ↔ real number, adjoint ↔ complex conjugate; normal operator ↔ complex number (real and imaginary parts commute) (pp. 233, 238).
- [metaphor] $\|Tv\|=\|T^*v\|$ for normal $T$ ↔ covariance/Gram matrices $X^{\mathrm t}X$ vs $XX^{\mathrm t}$ sharing structure (canon link; not stated in this unit).

## Questions this raises
- Which operators in applications (e.g. covariance matrices, graph Laplacians) are self-adjoint, so that the real spectral theorem applies?
- What if $T$ is not normal? Schur's theorem still gives an upper-triangular matrix in an orthonormal basis, but not a diagonal one. How far from diagonal can it be?
- Exercise 16 and 17 say commuting normal (or self-adjoint) families are simultaneously diagonalizable. Can this be used to understand several matrices (e.g. different powers of one graph adjacency matrix) at once?
- The author says the spectral theorem extends to certain infinite-dimensional spaces (p. 243). What changes there?

## Exercises worth doing
- Ex. 7A.7 (p. 239) — dimension formulas for $T^*$; gives rank of $T$ = rank of $T^*$ and the row rank = column rank proof of Ex. 8 — difficulty: medium
- Ex. 7A.9 (p. 239) — product of self-adjoint operators is self-adjoint iff they commute — difficulty: easy
- Ex. 7A.11 (p. 240) — the 90° rotation is normal, not self-adjoint; compute its eigenvalues — difficulty: easy
- Ex. 7B.1 (p. 247) — normal operator on a complex space is self-adjoint iff all eigenvalues are real — difficulty: medium
- Ex. 7B.8 (p. 248) — normal iff every eigenvector of $T$ is an eigenvector of $T^*$ (complex case) — difficulty: medium
- Ex. 7B.18 (p. 249) — shows self-adjointness is needed in 7.26 even over $\mathbf R$ — difficulty: easy

## Reading notes
- This part starts at the opening of Chapter 7 (printed p. 227) and ends with the Exercises 7B (printed p. 250). It covers 7A and 7B only; the chapter continues (not in these pages) after a section boundary.
- Printed page = pdf − 14.
- The text layer was garbled: math letters appeared as replacement characters. All formulas were checked against the page images. No misprints were found in the images.
- Chapter-intro photo (p. 227) is credited "Petar Milošević CC BY-SA".
- The proof of 7.26 uses $T=T^*$ in a step the page leaves implicit ($\langle T^2v,v\rangle=\langle Tv,Tv\rangle$); I marked it "(added step)".
- Cross-references such as 6.37, 6.38, 5.27(a), 4.13, 4.16, 3.65, 6.30(a), 6.49, 6.52 are cited in the proofs but their content is not in these pages. I used them only as the author does.
