---
id: axler-2024-ladr/ch09-multilinear-p1
work: axler-2024-ladr
unit: "9 Multilinear Algebra and Determinants (part 1/2): 9A Bilinear Forms and Quadratic Forms; 9B Alternating Multilinear Forms"
pages: 332-353
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Bilinear forms, quadratic forms and alternating multilinear forms (Axler, Ch. 9, sections 9A–9B)

## L0 — One line
Alternating $n$-linear forms on an $n$-dimensional space form a one-dimensional space, given by an explicit sum over permutations; this is the groundwork for a basis-free determinant.

## L1 — The gist (≤ 120 words)
How can we study functions of two vectors that are linear in each slot, and then of $m$ vectors? Section 9A treats bilinear forms: their matrices, how those matrices change with the basis, and their symmetric and alternating parts. It also treats quadratic forms, which can be diagonalised. Section 9B treats $m$-linear forms. An alternating form gives 0 on any linearly dependent list and changes sign when two inputs are swapped. When $m=\dim V$, the alternating forms are all scalar multiples of one form, written as a sum over permutations. A nonzero such form is nonzero on a list exactly when the list is linearly independent. The chapter uses this to define the determinant.

**Prerequisites:** vector spaces over $\mathbf R$ or $\mathbf C$; linear functionals and dual space; matrix of an operator and change of basis; transpose; direct sum; linear dependence; the real spectral theorem.

## L2 — Key ideas (5–10 bullets)
- A bilinear form is a function $V\times V\to\mathbf F$ that is linear in each slot. With a basis it has an $n\times n$ matrix, and $\beta\mapsto\mathcal M(\beta)$ is an isomorphism, so $\dim V^{(2)}=(\dim V)^2$ (pp. 333–335).
- Under a change of basis the matrix transforms as $A=C^{\mathrm t}BC$, with a transpose where operators use an inverse (p. 336).
- A bilinear form has a symmetric matrix in every basis or in none. A symmetric form has a diagonal matrix in some basis, and in some orthonormal basis on a real inner product space (pp. 337–339).
- $V^{(2)}=V^{(2)}_{\rm sym}\oplus V^{(2)}_{\rm alt}$. A form is alternating iff swapping the inputs flips the sign (pp. 339–340).
- A quadratic form is $q(v)=\beta(v,v)$. It comes from a unique symmetric bilinear form, and in a suitable basis it is a weighted sum of squares with no cross terms (pp. 341–343).
- An alternating $m$-linear form is zero on linearly dependent lists, and is identically zero if $m>\dim V$. Swapping two inputs multiplies it by $-1$ (pp. 347–348).
- For an alternating $n$-linear form with $n=\dim V$: $\alpha(v_1,\dots,v_n)=\alpha(e_1,\dots,e_n)\sum_{\text{perm}}\operatorname{sign}(\cdot)\,b_{j_1,1}\cdots b_{j_n,n}$ (p. 350).
- Hence $\dim V^{(\dim V)}_{\rm alt}=1$. A nonzero such form is nonzero on a list iff the list is linearly independent (pp. 351–352).

## L3 — Walkthrough

### Chapter opening (p. 332)
The chapter studies bilinear and quadratic forms, then multilinear forms. It shows that alternating $n$-linear forms on an $n$-dimensional space have dimension one, which gives a basis-free determinant. The announced consequences are: $\det(ST)=(\det S)(\det T)$, and $T$ is invertible iff $\det T\neq 0$. The determinant of an operator on a complex space is the product of its eigenvalues, counted with multiplicity. The chapter ends with tensor products. These later results are only announced in these pages (p. 332).
Standing assumptions: $\mathbf F$ is $\mathbf R$ or $\mathbf C$; $V$ and $W$ are finite-dimensional nonzero vector spaces over $\mathbf F$ (p. 332).

### 9A Bilinear forms and quadratic forms

**Bilinear forms.**
- **9.1 Definition.** A *bilinear form* on $V$ is a function $\beta: V\times V\to\mathbf F$ such that $v\mapsto\beta(v,u)$ and $v\mapsto\beta(u,v)$ are linear functionals on $V$ for every $u\in V$ (p. 333). A *linear functional* is a linear map into $\mathbf F$ (p. 333).
- On a real inner product space, $(u,v)\mapsto\langle u,v\rangle$ is a bilinear form. On a nonzero complex inner product space it is not, because complex scalars leave the second slot conjugated (p. 333).
- For $\mathbf F=\mathbf R$, an inner product additionally needs symmetry ($\beta(v,w)=\beta(w,v)$) and positive definiteness ($\beta(v,v)>0$ for $v\ne0$). A bilinear form needs neither (p. 333).
- **9.2 Examples** (pp. 333–334):
  - $\beta((x_1,x_2,x_3),(y_1,y_2,y_3))=x_1y_2-5x_2y_3+2x_3y_1$ on $\mathbf F^3$.
  - For an $n\times n$ matrix $A$: $\beta_A((x_1,\dots,x_n),(y_1,\dots,y_n))=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jy_k$. The first example is $\beta_A$ with $n=3$ and $A=\begin{pmatrix}0&1&0\\0&0&-5\\2&0&0\end{pmatrix}$.
  - $\beta(u,v)=\langle u,Tv\rangle$ for $T\in\mathcal L(V)$, $V$ a real inner product space.
  - $\beta(p,q)=p(2)\cdot q'(3)$ on $\mathcal P_n(\mathbf R)$ ($n$ a positive integer).
  - $\beta(u,v)=\varphi(u)\tau(v)$ for $\varphi,\tau\in V'$, and more generally $\varphi_1(u)\tau_1(v)+\dots+\varphi_n(u)\tau_n(v)$.
- Since $V\times V$ is a vector space, one may ask whether a bilinear form can also be a linear map on $V\times V$. The examples are linear only in special cases where the form is zero. Exercise 3 states that a bilinear form that is a linear map on $V\times V$ must be $0$ (p. 334).
- **9.3.** $V^{(2)}$ denotes the set of bilinear forms. With the usual function operations it is a vector space (p. 334).
- **9.4 Definition (matrix of a bilinear form).** For a basis $e_1,\dots,e_n$, $\mathcal M(\beta)$ is the $n\times n$ matrix with
$$\mathcal M(\beta)_{j,k}=\beta(e_j,e_k).$$
 Notation $\mathcal M(\beta,(e_1,\dots,e_n))$ names the basis when needed (p. 334).

**9.5 $\dim V^{(2)}=(\dim V)^2$.** For a basis $e_1,\dots,e_n$, $\beta\mapsto\mathcal M(\beta)$ is an isomorphism of $V^{(2)}$ onto $\mathbf F^{n,n}$ (p. 335).
*Proof.*
1. The map is clearly linear.
2. For $A\in\mathbf F^{n,n}$ define $\beta_A(x_1e_1+\dots+x_ne_n,\ y_1e_1+\dots+y_ne_n)=\sum_{k=1}^n\sum_{j=1}^n A_{j,k}x_jy_k$.
3. The maps $\beta\mapsto\mathcal M(\beta)$ and $A\mapsto\beta_A$ are inverses, since $\beta_{\mathcal M(\beta)}=\beta$ and $\mathcal M(\beta_A)=A$. The author leaves this check to the reader.
4. So $\dim V^{(2)}=\dim\mathbf F^{n,n}=n^2$ (p. 335).

*Intuition note.* Once you fix a basis, a bilinear form is completely determined by the $n^2$ numbers $\beta(e_j,e_k)$. Any $n^2$ numbers can occur, which is why the space has dimension $n^2$.

**9.6 Composition with an operator.** Let $\beta\in V^{(2)}$, $T\in\mathcal L(V)$, $\alpha(u,v)=\beta(u,Tv)$, $\rho(u,v)=\beta(Tu,v)$. For a basis $e_1,\dots,e_n$ (p. 335):
$$\mathcal M(\alpha)=\mathcal M(\beta)\mathcal M(T),\qquad \mathcal M(\rho)=\mathcal M(T)^{\mathrm t}\mathcal M(\beta).$$
*Proof of the first (the second is "similar").*
$$\mathcal M(\alpha)_{j,k}=\alpha(e_j,e_k)=\beta(e_j,Te_k)=\beta\Big(e_j,\sum_{m=1}^n\mathcal M(T)_{m,k}e_m\Big)=\sum_{m=1}^n\beta(e_j,e_m)\mathcal M(T)_{m,k}=\big(\mathcal M(\beta)\mathcal M(T)\big)_{j,k}.$$
(p. 335)

**9.7 Change-of-basis formula.** Let $\beta\in V^{(2)}$ and let $e_1,\dots,e_n$ and $f_1,\dots,f_n$ be bases. Put $A=\mathcal M(\beta,(e_1,\dots,e_n))$, $B=\mathcal M(\beta,(f_1,\dots,f_n))$ and $C=\mathcal M(I,(e_1,\dots,e_n),(f_1,\dots,f_n))$. Then
$$A=C^{\mathrm t}BC.$$
The operator formula of 3.84 has $C^{-1}$ where this has $C^{\mathrm t}$ (p. 336).
*Proof.*
1. By the linear map lemma (3.4) there is $T\in\mathcal L(V)$ with $Tf_k=e_k$. Then $\mathcal M(T,(f_1,\dots,f_n))=C$.
2. Define $\alpha(u,v)=\beta(u,Tv)$ and $\rho(u,v)=\alpha(Tu,v)=\beta(Tu,Tv)$.
3. Then $\beta(e_j,e_k)=\beta(Tf_j,Tf_k)=\rho(f_j,f_k)$.
4. So $A=\mathcal M(\rho,(f))=C^{\mathrm t}\mathcal M(\alpha,(f))=C^{\mathrm t}BC$, with the last two equalities from 9.6 (p. 336).

**9.8 Example** (p. 336). $\beta(p,q)=p(2)\cdot q'(3)$ on $\mathcal P_2(\mathbf R)$. Take bases $(1,x-2,(x-3)^2)$ and $(1,x,x^2)$. Then
$$A=\begin{pmatrix}0&1&0\\0&0&0\\0&1&0\end{pmatrix},\quad B=\begin{pmatrix}0&1&6\\0&2&12\\0&4&24\end{pmatrix},\quad C=\begin{pmatrix}1&-2&9\\0&1&-6\\0&0&1\end{pmatrix},$$
and $A=C^{\mathrm t}BC$, which the reader can verify by multiplication (p. 336).

*Intuition note.* A bilinear form eats two vectors, so a basis change acts on both slots. That gives $C^{\mathrm t}\,\cdot\,C$ instead of $C^{-1}\,\cdot\,C$ for an operator, which eats one vector and returns one.

**Symmetric bilinear forms.**
- **9.9.** $\rho\in V^{(2)}$ is *symmetric* if $\rho(u,w)=\rho(w,u)$ for all $u,w$. The set is $V^{(2)}_{\rm sym}$ (p. 337).
- **9.10 Examples.** The inner product on a real inner product space. $\langle u,Tw\rangle$ is symmetric iff $T$ is self-adjoint. $\rho(S,T)=\operatorname{tr}(ST)$ on $\mathcal L(V)$ is symmetric because $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ (p. 337).
- **9.11.** A square matrix is *symmetric* if it equals its transpose. An operator may have a symmetric matrix in some bases but not others. A bilinear form has a symmetric matrix in all bases or in none (p. 337).

**9.12 Symmetric bilinear forms are diagonalizable.** For $\rho\in V^{(2)}$ the following are equivalent (p. 337):
(a) $\rho$ is symmetric.
(b) $\mathcal M(\rho,(e_1,\dots,e_n))$ is symmetric for every basis.
(c) It is symmetric for some basis.
(d) It is diagonal for some basis.

*Proof* (p. 338).
- (a)⇒(b): $\rho(e_j,e_k)=\rho(e_k,e_j)$. (b)⇒(c) is clear. (d)⇒(c) because diagonal matrices are symmetric.
- (c)⇒(a): write $u=\sum a_je_j$, $w=\sum b_ke_k$. Then
$$\rho(u,w)=\sum_{j,k}a_jb_k\rho(e_j,e_k)=\sum_{j,k}a_jb_k\rho(e_k,e_j)=\rho(w,u),$$
where the middle equality uses the symmetric matrix.
- (a)⇒(d) by induction on $n=\dim V$.
  1. If $n=1$, every $1\times1$ matrix is diagonal.
  2. Let $n>1$. If $\rho=0$, its matrix is zero in every basis. Otherwise some $\rho(u,w)\neq0$.
  3. From $2\rho(u,w)=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w)\neq 0$, the three terms on the right are not all zero. So there is $v$ with $\rho(v,v)\ne0$.
  4. Let $U=\{u\in V:\rho(u,v)=0\}$. This is the null space of the nonzero functional $u\mapsto\rho(u,v)$. The functional is nonzero because $v\notin U$, so $\dim U=n-1$.
  5. By the induction hypothesis, $U$ has a basis $e_1,\dots,e_{n-1}$ in which $\rho|_{U\times U}$ is diagonal.
  6. Since $v\notin U$, the list $e_1,\dots,e_{n-1},v$ is a basis of $V$. For $k<n$, $\rho(e_k,v)=0$ by construction of $U$, and $\rho(v,e_k)=0$ by symmetry. So the matrix is diagonal.

*Intuition note.* Picking a vector $v$ with $\rho(v,v)\neq0$ and splitting off everything "$\rho$-perpendicular" to it peels off one diagonal entry at a time.

**9.13 Orthonormal diagonalization.** If $V$ is a real inner product space and $\rho$ is symmetric, $\rho$ has a diagonal matrix in some orthonormal basis. The inner product is unrelated to $\rho$ (p. 339).
*Proof* (p. 339).
1. Take an orthonormal basis $f_1,\dots,f_n$ and $B=\mathcal M(\rho,(f))$. $B$ is symmetric by 9.12.
2. Let $T$ be the operator with $\mathcal M(T,(f))=B$. $T$ is self-adjoint.
3. By the real spectral theorem (7.29) there is an orthonormal basis $e_1,\dots,e_n$ in which $T$ is diagonal. Let $C=\mathcal M(I,(e),(f))$. Then $C^{-1}BC$ is diagonal (3.84).
4. $C$ is a real unitary matrix, so $C^{-1}=C^{\mathrm t}$ (7.57). By 9.7, $\mathcal M(\rho,(e))=C^{\mathrm t}BC=C^{-1}BC$.

*Intuition note.* On a real inner product space, orthogonal change of basis makes "$C^{\mathrm t}$" and "$C^{-1}$" the same. So the spectral theorem for operators gives a diagonalisation of the form.

**Alternating bilinear forms.**
- **9.14.** $\alpha\in V^{(2)}$ is *alternating* if $\alpha(v,v)=0$ for all $v$. The set is $V^{(2)}_{\rm alt}$ (p. 339).
- **9.15 Examples.** $\alpha((x),(y))=x_1y_2-x_2y_1+x_1y_3-x_3y_1$ on $\mathbf F^n$ ($n\ge3$). $\alpha(u,w)=\varphi(u)\tau(w)-\varphi(w)\tau(u)$ for $\varphi,\tau\in V'$ (p. 339).
- **9.16.** $\alpha$ is alternating iff $\alpha(u,w)=-\alpha(w,u)$ for all $u,w$ (p. 340).
  *Proof.* ($\Rightarrow$) $0=\alpha(u+w,u+w)=\alpha(u,u)+\alpha(u,w)+\alpha(w,u)+\alpha(w,w)=\alpha(u,w)+\alpha(w,u)$. ($\Leftarrow$) Put $u=w=v$: $\alpha(v,v)=-\alpha(v,v)$, so $\alpha(v,v)=0$ (p. 340).
- **9.17.** $V^{(2)}_{\rm sym}$ and $V^{(2)}_{\rm alt}$ are subspaces, and $V^{(2)}=V^{(2)}_{\rm sym}\oplus V^{(2)}_{\rm alt}$ (p. 340).
  *Proof.* For $\beta\in V^{(2)}$ define $\rho(u,w)=\tfrac{\beta(u,w)+\beta(w,u)}2$ and $\alpha(u,w)=\tfrac{\beta(u,w)-\beta(w,u)}2$. Then $\rho$ is symmetric, $\alpha$ is alternating, and $\beta=\rho+\alpha$. If $\beta$ is in both subspaces, 9.16 gives $\beta(u,w)=-\beta(w,u)=-\beta(u,w)$, so $\beta=0$. Then 1.46 gives the direct sum (p. 340).

*Intuition note.* Every bilinear form splits uniquely into a "mirror-symmetric" part and a "sign-flipping" part (9.17).

**Quadratic forms.**
- **9.18.** For $\beta\in V^{(2)}$, $q_\beta(v)=\beta(v,v)$. A function $q:V\to\mathbf F$ is a *quadratic form* if $q=q_\beta$ for some bilinear form $\beta$. Also $q_\beta=0$ iff $\beta$ is alternating (p. 341).
- **9.19 Example.** $\beta((x),(y))=x_1y_1-4x_1y_2+8x_1y_3-3x_3y_3$ gives $q_\beta(x)=x_1^2-4x_1x_2+8x_1x_3-3x_3^2$ (p. 341).
- **9.20 Quadratic forms on $\mathbf F^n$.** $q$ is a quadratic form iff there are numbers $A_{j,k}$ with $q(x_1,\dots,x_n)=\sum_{k=1}^n\sum_{j=1}^nA_{j,k}x_jx_k$. The proof takes $A$ as the matrix of $\beta$ in the standard basis, and in the converse defines $\beta$ by the same coefficients (p. 341).
- **9.21 Characterizations.** For a function $q:V\to\mathbf F$ these are equivalent (p. 342):
(a) $q$ is a quadratic form.
(b) There is a *unique* symmetric bilinear form $\rho$ with $q=q_\rho$.
(c) $q(\lambda v)=\lambda^2q(v)$ for all $\lambda\in\mathbf F$, $v\in V$, and $(u,w)\mapsto q(u+w)-q(u)-q(w)$ is a symmetric bilinear form.
(d) $q(2v)=4q(v)$ for all $v$, and the same function $(u,w)\mapsto q(u+w)-q(u)-q(w)$ is a symmetric bilinear form.

  *Proof* (p. 342).
  - (a)⇒(b): $q=q_\beta$. By 9.17, $\beta=\rho+\alpha$ with $\rho$ symmetric, $\alpha$ alternating, so $q=q_\rho+q_\alpha=q_\rho$. If $\rho'$ is symmetric with $q_{\rho'}=q$, then $q_{\rho'-\rho}=0$, so $\rho'-\rho$ is symmetric and alternating. By 9.17, $\rho'=\rho$.
  - (b)⇒(c): $q(\lambda v)=\rho(\lambda v,\lambda v)=\lambda^2\rho(v,v)=\lambda^2q(v)$. Also $q(u+w)-q(u)-q(w)=\rho(u+w,u+w)-\rho(u,u)-\rho(w,w)=2\rho(u,w)$, which is a symmetric bilinear form.
  - (c)⇒(d) is clear.
  - (d)⇒(a): define $\rho(u,w)=\frac{q(u+w)-q(u)-q(w)}2$. Then $\rho(v,v)=\frac{q(2v)-2q(v)}2=\frac{4q(v)-2q(v)}2=q(v)$.
- **9.22 Example** (p. 343). For $q$ as in 9.19, the form $\beta$ of 9.19 is not symmetric. The symmetric form with $q=q_\rho$ is
$$\rho((x),(y))=x_1y_1-2x_1y_2-2x_2y_1+4x_1y_3+4x_3y_1-3x_3y_3.$$
- **9.23 Diagonalization of a quadratic form** (p. 343). Let $q$ be a quadratic form on $V$.
  (a) There are a basis $e_1,\dots,e_n$ and $\lambda_1,\dots,\lambda_n\in\mathbf F$ with $q(x_1e_1+\dots+x_ne_n)=\lambda_1x_1^2+\dots+\lambda_nx_n^2$ for all $x_j\in\mathbf F$.
  (b) If $\mathbf F=\mathbf R$ and $V$ is an inner product space, the basis can be chosen orthonormal.

  *Proof.* By 9.21 take symmetric $\rho$ with $q=q_\rho$. By 9.12, in some basis $\rho(e_j,e_k)=\lambda_j$ if $j=k$ and $0$ if $j\neq k$. Then $q(\sum x_je_j)=\sum_{j,k}x_jx_k\rho(e_j,e_k)=\lambda_1x_1^2+\dots+\lambda_nx_n^2$. Part (b) follows from 9.13 (p. 343).

*Intuition note.* "Cross terms" like $x_1x_2$ are artefacts of the coordinate system. Choosing a basis adapted to the symmetric form removes them, leaving a weighted sum of squares.

**Exercises 9A** (pp.

### 9B Alternating multilinear forms

**Multilinear forms.**
- **9.24.** $V^m=V\times\dots\times V$ ($m$ copies) (p. 346).
- **9.25.** An *$m$-linear form* on $V$ is a function $\beta:V^m\to\mathbf F$ that is linear in each slot with the others held fixed: for each $k$ and all $u_1,\dots,u_m$, the map $v\mapsto\beta(u_1,\dots,u_{k-1},v,u_{k+1},\dots,u_m)$ is linear. $V^{(m)}$ is the set of $m$-linear forms. A *multilinear form* is an $m$-linear form for some $m$. A 1-linear form is a linear functional and a 2-linear form is a bilinear form. $V^{(m)}$ is a vector space (p. 346).
- **9.26 Examples.** For $\alpha,\rho\in V^{(2)}$, $\beta(v_1,v_2,v_3,v_4)=\alpha(v_1,v_2)\rho(v_3,v_4)$ is in $V^{(4)}$. $\beta(T_1,\dots,T_m)=\operatorname{tr}(T_1\cdots T_m)$ is $m$-linear on $\mathcal L(V)$ (p. 346).

**Alternating forms.**
- **9.27.** An $m$-linear form $\alpha$ is *alternating* if $\alpha(v_1,\dots,v_m)=0$ whenever $v_j=v_k$ for some distinct $j,k$. $V^{(m)}_{\rm alt}$ is the set of such forms, a subspace of $V^{(m)}$ (p. 347).
- **9.28.** If $\alpha\in V^{(m)}_{\rm alt}$ and $v_1,\dots,v_m$ is linearly dependent, then $\alpha(v_1,\dots,v_m)=0$ (p. 347).
  *Proof.* By the linear dependence lemma (2.19), some $v_k=b_1v_1+\dots+b_{k-1}v_{k-1}$. Then
$$\alpha(v_1,\dots,v_m)=\sum_{j=1}^{k-1}b_j\,\alpha(v_1,\dots,v_{k-1},v_j,v_{k+1},\dots,v_m)=0,$$
  since each term repeats the vector $v_j$ (p. 347).
- **9.29.** If $m>\dim V$, the only alternating $m$-linear form is $0$. Proof: any $m$ vectors are linearly dependent (2.22), so 9.28 applies (p. 347).

*Intuition note.* An alternating form is blind to redundancy: if one input can be built from the others, the output is zero. In a space of dimension $n$ every list longer than $n$ is redundant.

**Permutations and swaps.**
- **9.30.** Swapping the vectors in any two slots multiplies $\alpha(v_1,\dots,v_m)$ by $-1$. Proof: put $v_1+v_2$ in the first two slots, get $0$, and expand as in 9.16 to get $\alpha(v_2,v_1,v_3,\dots)=-\alpha(v_1,v_2,v_3,\dots)$. Other slot pairs are the same (p. 348).
- Example (p. 348): for an alternating 3-linear form, $\alpha(v_3,v_1,v_2)=-\alpha(v_2,v_1,v_3)=\alpha(v_1,v_2,v_3)$. An odd number of swaps multiplies by $-1$, an even number leaves the value unchanged (p. 348).
- **9.31.** A *permutation* of $(1,\dots,m)$ is a list $(j_1,\dots,j_m)$ containing each of $1,\dots,m$ exactly once. $\operatorname{perm}m$ is the set of all of them. Example: $(2,3,4,5,1)\in\operatorname{perm}5$ (p. 348).
- **9.32.** $\operatorname{sign}(j_1,\dots,j_m)=(-1)^N$, where $N$ is the number of pairs $(k,\ell)$ with $1\le k<\ell\le m$ such that $k$ appears after $\ell$ in the list (p. 349). This gives a well-defined sign, whereas the number of swaps needed to reach $(1,\dots,m)$ depends on the choice of swaps (p. 348).
- **9.33 Examples.** $(1,\dots,m)$ has sign $1$. $(2,1,3,4)$ has only the pair $(1,2)$ out of order, so sign $-1$. $(2,3,\dots,m,1)$ has the $m-1$ pairs $(1,2),\dots,(1,m)$ out of order, so sign $(-1)^{m-1}$ (p. 349).
- **9.34.** Swapping two entries of a permutation multiplies its sign by $-1$ (p. 349).
  *Proof sketch.*
  1. The two swapped entries change between "in order" and "out of order", a net change of $\pm1$ in the count of out-of-order pairs.
  2. For each entry between them, the pairs it forms with the two swapped entries change the count by $2$, $-2$ or $0$.
  3. All other pairs are unchanged. So the total change is odd (p. 349).
- **9.35.** For $\alpha\in V^{(m)}_{\rm alt}$, all lists $v_1,\dots,v_m$ and all $(j_1,\dots,j_m)\in\operatorname{perm}m$:
$$\alpha(v_{j_1},\dots,v_{j_m})=\operatorname{sign}(j_1,\dots,j_m)\,\alpha(v_1,\dots,v_m).$$
  *Proof.* Reach $(1,\dots,m)$, which has sign $1$, by swaps. Each swap multiplies $\alpha$ by $-1$ (9.30) and the sign of the remaining permutation by $-1$ (9.34). So $\alpha$ changed sign an even number of times if the sign is $1$ and an odd number if it is $-1$ (p. 350).

**9.36 Formula for $(\dim V)$-linear alternating forms** (p. 350). Let $n=\dim V$, $e_1,\dots,e_n$ a basis, $v_1,\dots,v_n\in V$, and $v_k=\sum_{j=1}^nb_{j,k}e_j$. Then for every alternating $n$-linear form $\alpha$:
$$\alpha(v_1,\dots,v_n)=\alpha(e_1,\dots,e_n)\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\operatorname{sign}(j_1,\dots,j_n)\,b_{j_1,1}\cdots b_{j_n,n}.$$
*Proof.*
$$\alpha(v_1,\dots,v_n)=\alpha\Big(\sum_{j_1=1}^nb_{j_1,1}e_{j_1},\dots,\sum_{j_n=1}^nb_{j_n,n}e_{j_n}\Big)=\sum_{j_1=1}^n\cdots\sum_{j_n=1}^nb_{j_1,1}\cdots b_{j_n,n}\,\alpha(e_{j_1},\dots,e_{j_n}).$$
Terms where $j_1,\dots,j_n$ are not distinct vanish, so only permutations remain. Then 9.35 gives $\alpha(e_{j_1},\dots,e_{j_n})=\operatorname{sign}(j_1,\dots,j_n)\alpha(e_1,\dots,e_n)$ (p. 350).

*Intuition note.* Multilinearity expands the output into $n^n$ terms. The alternating property kills all but the $n!$ terms that use each basis vector once. The sign rule then reduces everything to the single number $\alpha(e_1,\dots,e_n)$.

**9.37 $\dim V^{(\dim V)}_{\rm alt}=1$.** (p. 351)
*Proof.* Let $n=\dim V$.
1. *Dimension $\le1$.* Let $\alpha\ne0$ and $\alpha'$ be alternating $n$-linear forms. Pick $e_1,\dots,e_n$ with $\alpha(e_1,\dots,e_n)\neq0$. There is $c$ with $\alpha'(e_1,\dots,e_n)=c\,\alpha(e_1,\dots,e_n)$. By 9.28 the list $e_1,\dots,e_n$ is linearly independent, hence a basis. By 9.36 applied to $\alpha'$ and then to $\alpha$,
$$\alpha'(v_1,\dots,v_n)=c\,\alpha(e_1,\dots,e_n)\sum(\cdots)=c\,\alpha(v_1,\dots,v_n).$$
So $\alpha'=c\alpha$ and $\alpha',\alpha$ is not linearly independent, giving $\dim\le1$.
2. *A nonzero form exists.* Let $e_1,\dots,e_n$ be any basis and $\varphi_1,\dots,\varphi_n\in V'$ the coordinate functionals, $v=\sum_j\varphi_j(v)e_j$ (3.114). Define
$$\alpha(v_1,\dots,v_n)=\sum_{(j_1,\dots,j_n)\in\operatorname{perm}n}\operatorname{sign}(j_1,\dots,j_n)\,\varphi_{j_1}(v_1)\cdots\varphi_{j_n}(v_n).\tag{9.38}$$
 It is clearly $n$-linear. If $v_1=v_2$, the terms for $(j_1,j_2,j_3,\dots,j_n)$ and $(j_2,j_1,j_3,\dots,j_n)$ have opposite signs and equal values, so they cancel. The same holds for any two equal vectors, so $\alpha$ is alternating. With $v_k=e_k$ only the permutation $(1,\dots,n)$ contributes, so $\alpha(e_1,\dots,e_n)=1\neq0$ (p. 351).

*Intuition note.* Up to a scalar multiple there is exactly one alternating $n$-linear form on an $n$-dimensional space. This single form is what the chapter will use to define the determinant (p. 351; the determinant itself is not defined in these pages).

**9.39 Linear independence test.** Let $n=\dim V$, $\alpha$ a *nonzero* alternating $n$-linear form, $e_1,\dots,e_n$ a list in $V$. Then $\alpha(e_1,\dots,e_n)\neq0$ iff the list is linearly independent (p. 352).
*Proof.* ($\Rightarrow$) 9.28. ($\Leftarrow$) $n$ independent vectors in an $n$-dimensional space form a basis (2.38). Since $\alpha\neq0$, some $\alpha(v_1,\dots,v_n)\neq0$, and then 9.36 forces $\alpha(e_1,\dots,e_n)\neq0$ (p. 352).
Exercise 7 (p. 353) says this can fail if $n=\dim V$ is dropped.

**Exercises 9B** (pp. 352–353) are listed at the end.

## Toy example (ours, not from the text)
Let $V=\mathbf R^2$ with basis $e_1=(1,0)$, $e_2=(0,1)$. Let $\alpha$ be any alternating 2-linear form. Take $v_1=3e_1+1e_2$, $v_2=2e_1+4e_2$, so $b_{1,1}=3$, $b_{2,1}=1$, $b_{1,2}=2$, $b_{2,2}=4$.

Formula 9.36 has two permutations of $(1,2)$:
- $(1,2)$ has sign $+1$ and contributes $b_{1,1}b_{2,2}=3\cdot4=12$.
- $(2,1)$ has sign $-1$ (the pair $(1,2)$ is out of order, $N=1$) and contributes $-b_{2,1}b_{1,2}=-1\cdot2=-2$.

So $\alpha(v_1,v_2)=\alpha(e_1,e_2)\,(12-2)=10\,\alpha(e_1,e_2)$.

Direct check by bilinearity: $\alpha(3e_1+e_2,\,2e_1+4e_2)=3\cdot2\,\alpha(e_1,e_1)+3\cdot4\,\alpha(e_1,e_2)+1\cdot2\,\alpha(e_2,e_1)+1\cdot4\,\alpha(e_2,e_2)=0+12\alpha(e_1,e_2)-2\alpha(e_1,e_2)+0=10\,\alpha(e_1,e_2)$. ✓.

Dependent case: $v_1=(1,2)$, $v_2=(2,4)=2v_1$. Then $b_{1,1}b_{2,2}-b_{2,1}b_{1,2}=1\cdot4-2\cdot2=0$, so $\alpha(v_1,v_2)=0$, as 9.28 predicts. For the first pair, if $\alpha(e_1,e_2)\ne0$, then $10\,\alpha(e_1,e_2)$ is nonzero, consistent with 9.39 because $(3,1),(2,4)$ are linearly independent.

## Concepts
- [[bilinear-form]] (new) — function $V\times V\to\mathbf F$ linear in each slot separately (p. 333)
- [[matrix-of-bilinear-form]] (new) — $\mathcal M(\beta)_{j,k}=\beta(e_j,e_k)$; changes by $A=C^{\mathrm t}BC$ (pp. 334, 336)
- [[symmetric-bilinear-form]] (new) — $\rho(u,w)=\rho(w,u)$; diagonalizable in some basis (pp. 337–338)
- [[alternating-form]] (new) — $m$-linear form that is zero when two inputs are equal; flips sign on swaps; zero on dependent lists (pp. 339, 347–348)
- [[multilinear-form]] (new) — $m$-linear function $V^m\to\mathbf F$, linear in each slot (p. 346)
- [[quadratic-form]] — here $q(v)=\beta(v,v)$ for some bilinear $\beta$, defined on any $V$ (the canon's $x^{\mathsf T}Sx$ is the $\mathbf F^n$ case via 9.20 and a symmetric matrix) (p. 341)
- [[change-of-basis]] — for bilinear forms $A=C^{\mathrm t}BC$, unlike the operator rule $C^{-1}BC$ (p. 336)
- [[spectral-theorem]] — real spectral theorem used to get an orthonormal diagonalisation in 9.13 (p. 339)
- [[permutation-sign]] (new) — $(-1)^N$, $N$ = number of out-of-order pairs; flips under a swap (pp. 348–349)
- [[linear-independence]] — the nonzero alternating $n$-linear form detects it when $n=\dim V$ (p. 352)

## Canonical instances
- [[bilinear-form-on-polynomials-p2-q3]] — $\beta(p,q)=p(2)q'(3)$ and its matrices in two bases (pp. 334, 336)
- [[trace-form-tr-ST]] — $\rho(S,T)=\operatorname{tr}(ST)$ is a symmetric bilinear form on $\mathcal L(V)$ (p. 337)
- [[quadratic-form-r3-example]] — $x_1^2-4x_1x_2+8x_1x_3-3x_3^2$ and its symmetric bilinear form (pp. 341, 343)
- [[trace-product-m-linear-form]] — $\operatorname{tr}(T_1\cdots T_m)$ is $m$-linear but is not claimed alternating (p. 346)
- [[permutation-sum-form-9.38]] — the explicit nonzero alternating $n$-linear form $\sum\operatorname{sign}\cdot\varphi_{j_1}(v_1)\cdots\varphi_{j_n}(v_n)$ (p. 351)

## Bridges (candidates)
- [same-math] $C^{\mathrm t}BC$ rule for the matrix of a bilinear form ↔ inner products: the Gram matrix $\langle e_j,e_k\rangle$ changes this way under a basis change — the inner product is a symmetric bilinear form here (9.10).
- [same-math] quadratic form $q(v)=\beta(v,v)$ on $\mathbf R^n$ with symmetric matrix ↔ canon "quadratic form $x^{\mathsf T}Sx$": the same function, shown diagonalisable by an orthonormal basis (9.23b).
- [same-math] Diagonalising a symmetric form in an orthonormal basis (9.13) ↔ spectral theorem: it follows from that theorem, using $C^{-1}=C^{\mathrm t}$.
- [same-math] Formula 9.36/9.38, a signed sum over permutations of products of entries ↔ determinant: the later chapter presumably identifies this expression with the determinant (not stated in these pages).
- [structural-analogy] Splitting $V^{(2)}=V^{(2)}_{\rm sym}\oplus V^{(2)}_{\rm alt}$ ↔ splitting a square matrix into symmetric and antisymmetric parts.

## Questions this raises
- How does the one-dimensional space $V^{(\dim V)}_{\rm alt}$ give a number $\det T$ for an operator, independent of basis? (The chapter says it will, p. 332.)
- Over $\mathbf C$, what replaces orthonormal diagonalisation of a quadratic form? Why does the proof of 9.13 depend on $\mathbf F=\mathbf R$ (Ex. 7, p. 344)?
- What are $\dim V^{(2)}_{\rm sym}$ and $\dim V^{(2)}_{\rm alt}$, and what does $\dim V^{(m)}_{\rm alt}$ become for $m<\dim V$?
- Can a symmetric form with all diagonal entries nonzero of mixed signs be put into a standard form? (The text only gives $\lambda_j\in\mathbf F$ with no further normalisation, p. 343.)

## Exercises worth doing
- Ex. 9A.4 (p. 344) — every bilinear form on a real inner product space is $\langle u,Tv\rangle$ for a unique $T$; links forms to operators — difficulty: medium
- Ex. 9A.7 (p. 344) — see exactly where the real-field hypothesis enters 9.13 — difficulty: medium
- Ex. 9A.8 (p. 344) — dimensions of the symmetric and alternating subspaces, using 9.17 and 9.5 — difficulty: medium
- Ex. 9B.3 (p. 352) — it suffices to test equal *adjacent* inputs for alternation — difficulty: medium
- Ex. 9B.5 (p. 353) — antisymmetrising any $m$-linear form produces an alternating one — difficulty: hard
- Ex. 9B.7 (p. 353) — 9.39 fails without $n=\dim V$ — difficulty: easy

## Reading notes
- This is part 1 of Chapter 9. It starts at the chapter opening (p. 332) and ends at the end of Exercises 9B (p. 353). The next section (the determinant, announced on p. 351) and later material are in the next part. The split is at a section boundary.
- Printed page = pdf page − 14. Page 345 is mostly blank after Exercise 10.
- The extracted text layer shows math symbols as unreadable placeholders. Formulas were read from the page images.
- Typographic points only: in the proof of 9.13 the displayed equation uses plain "M" where the definition uses script $\mathcal M$. In 9.2, $\beta_A$ is written with the outer sum over $k$ and the inner over $j$, which is harmless.
- The numerical matrices in Example 9.8 satisfy $A=C^{\mathrm t}BC$ as printed (direct multiplication confirms it).
- Proofs of 9.6 (second formula), 9.5 (inverse check) and the subspace claim for $V^{(2)}_{\rm alt}$ in 9.17 and the subspace claim in 9.27 are left to the reader in the source and are not expanded here.
