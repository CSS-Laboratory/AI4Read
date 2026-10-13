---
id: axler-2024-ladr/ch08-operators
work: axler-2024-ladr
unit: "8 Operators on Complex Vector Spaces"
pages: 297–331
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Operators on Complex Vector Spaces (Axler, LADR 4th ed., Chapter 8)

## L0 — One line
On a finite-dimensional complex vector space every operator has a basis of generalized eigenvectors, so the space splits into invariant pieces on which the operator is "scalar plus nilpotent", which gives multiplicity, the Cayley–Hamilton theorem, square roots of invertible operators, Jordan form and the trace.

## L1 — The gist (≤ 120 words)
Some operators lack enough eigenvectors to form a basis, even over the complex numbers. The chapter asks what can replace eigenvectors. The answer is generalized eigenvectors: vectors that some power of $T-\lambda I$ sends to 0. Over $\mathbf C$ they always span the space. Hence $V$ is the direct sum of the generalized eigenspaces. On each of these, $T$ is $\lambda I$ plus a nilpotent operator (some power of it is 0). From this the chapter derives multiplicities, the characteristic polynomial, the Cayley–Hamilton theorem, square roots of invertible operators and Jordan form. It ends with the trace (sum of diagonal entries of a matrix of the operator): basis-independent, linear, and over $\mathbf C$ equal to the sum of the eigenvalues counted with multiplicity.

**Prerequisites:** null space and range; rank–nullity; direct sums; invariant subspaces; eigenvalues; minimal polynomial; upper-triangular matrices; change of basis.

## L2 — Key ideas (5–10 bullets)
- Null spaces of $T^k$ grow with $k$ and have stopped growing by $k=\dim V$. Thus $V=\operatorname{null}T^{\dim V}\oplus\operatorname{range}T^{\dim V}$, although $V=\operatorname{null}T\oplus\operatorname{range}T$ can fail (pp. 298–299).
- A generalized eigenvector satisfies $(T-\lambda I)^k v=0$ for some $k$. Over $\mathbf C$ a basis of them exists, each belongs to only one eigenvalue, and those for distinct eigenvalues are independent (pp. 300–303).
- Nilpotent operators ($T^k=0$ for some $k$) have only the eigenvalue 0 and satisfy $T^{\dim V}=0$. They have a strictly upper-triangular matrix in some basis (pp. 303–305).
- Over $\mathbf C$, $V=G(\lambda_1,T)\oplus\dots\oplus G(\lambda_m,T)$, where the generalized eigenspace $G(\lambda,T)$ is the set of generalized eigenvectors for $\lambda$ together with 0. Each piece is $T$-invariant and $T-\lambda_k I$ is nilpotent on it (p. 309).
- Multiplicity is defined as $\dim G(\lambda,T)$. Over $\mathbf C$ the multiplicities $d_k$ sum to $\dim V$, and the characteristic polynomial $q=(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}$ built from them satisfies $q(T)=0$ (the Cayley–Hamilton theorem) (pp. 310–312).
- Over $\mathbf C$, multiplicity equals the number of times $\lambda$ appears on the diagonal of any upper-triangular matrix of $T$. Over $\mathbf C$ a basis exists in which $T$ has a block-diagonal matrix whose blocks are upper triangular, each with a single eigenvalue repeated on its diagonal (pp. 313–315).
- Invertible operators on complex spaces have square roots, because identity plus nilpotent has one (pp. 319–320).
- Every operator on a complex space has a Jordan basis: a basis in which the matrix is block diagonal, each block having one eigenvalue on its diagonal, 1's directly above it and 0 elsewhere, so entries can be nonzero only on the diagonal and the line above it (pp. 322–324).
- The trace (the sum of the diagonal entries of a matrix of the operator) is basis-independent and satisfies $\operatorname{tr}(ST)=\operatorname{tr}(TS)$. Over $\mathbf C$ it equals the sum of the eigenvalues with multiplicity, and no $S,T$ satisfy $ST-TS=I$ (pp. 326–330).

## L3 — Walkthrough

**Chapter set-up.** Standing assumptions: $\mathbf F$ is $\mathbf R$ or $\mathbf C$, and $V$ is finite-dimensional and nonzero. Some results hold for both fields. The author says an inner product does not help with this material (p. 297).

### 8A Generalized Eigenvectors and Nilpotent Operators

**Null spaces of powers.**
- **8.1.** For $T\in\mathcal L(V)$: $\{0\}=\operatorname{null}T^0\subseteq\operatorname{null}T^1\subseteq\cdots\subseteq\operatorname{null}T^k\subseteq\operatorname{null}T^{k+1}\subseteq\cdots$. Proof: if $T^kv=0$ then $T^{k+1}v=T(T^kv)=T(0)=0$ (p. 298).
- **8.2.** If $\operatorname{null}T^m=\operatorname{null}T^{m+1}$, then all later null spaces equal it. Proof, for $k\ge1$: "$\subseteq$" is 8.1. For the reverse, let $v\in\operatorname{null}T^{m+k+1}$. Then $T^{m+1}(T^kv)=0$, so $T^kv\in\operatorname{null}T^{m+1}=\operatorname{null}T^m$. Hence $T^{m+k}v=T^m(T^kv)=0$ (p. 298).
- **8.3.** $\operatorname{null}T^{\dim V}=\operatorname{null}T^{\dim V+1}=\cdots$. Proof: if not, 8.1 and 8.2 give a chain of strict inclusions $\{0\}\subsetneq\operatorname{null}T^1\subsetneq\cdots\subsetneq\operatorname{null}T^{\dim V+1}$. Each strict step raises the dimension by at least 1, so $\dim\operatorname{null}T^{\dim V+1}\ge\dim V+1$. This is impossible for a subspace of $V$ (p. 299).
- **8.4.** $V=\operatorname{null}T^{\dim V}\oplus\operatorname{range}T^{\dim V}$. Let $n=\dim V$.
  - First, $(\operatorname{null}T^n)\cap(\operatorname{range}T^n)=\{0\}$ (8.5). Take $v$ in both, so $T^nv=0$ and $v=T^nu$. Applying $T^n$ gives $T^{2n}u=0$. By 8.3, $T^nu=0$, so $v=0$.
  - So the sum is direct (1.46). Then $\dim(\operatorname{null}T^n\oplus\operatorname{range}T^n)=\dim\operatorname{null}T^n+\dim\operatorname{range}T^n=\dim V$ (3.94, 3.21). By 2.39 the sum is $V$ (p. 299).
- The author notes that $V=\operatorname{null}T\oplus\operatorname{range}T$ is *not* true for every $T$ (p. 299). Exercise 19 improves 8.4 for non-nilpotent $T$ (p. 299).
- **Example 8.6.** $T(z_1,z_2,z_3)=(4z_2,0,5z_3)$ on $\mathbf F^3$. $\operatorname{null}T=\{(z_1,0,0)\}$ and $\operatorname{range}T=\{(z_1,0,z_3)\}$, so they intersect nontrivially. But $T^3(z_1,z_2,z_3)=(0,0,125z_3)$, so $\operatorname{null}T^3=\{(z_1,z_2,0)\}$ and $\operatorname{range}T^3=\{(0,0,z_3)\}$. These give $\mathbf F^3$ as a direct sum (pp. 299–300).

*Intuition note.* Repeatedly applying $T$ can only destroy more vectors. After $\dim V$ steps nothing new is destroyed. By then the "dying part" and the "surviving part" no longer overlap.

**Generalized eigenvectors.**
- Motivation: a decomposition $V=V_1\oplus\dots\oplus V_n$ into one-dimensional invariant subspaces exists iff $V$ has a basis of eigenvectors, iff $V=E(\lambda_1,T)\oplus\cdots\oplus E(\lambda_m,T)$ (8.7, citing 5.55). On an inner product space, the spectral theorem gives this for self-adjoint operators when $\mathbf F=\mathbf R$ and normal operators when $\mathbf F=\mathbf C$. It can fail for more general operators, even over $\mathbf C$ (the operator in 5.57) (p. 300).
- **8.8 Definition.** Let $\lambda$ be an eigenvalue of $T$. A vector $v$ is a *generalized eigenvector* for $\lambda$ if $v\ne0$ and $(T-\lambda I)^kv=0$ for some positive integer $k$ (p. 300). By 8.1 and 8.3 one may take $k=\dim V$ (p. 301). Generalized eigenvalues are not defined: if $(T-\lambda I)^k$ is not injective then $T-\lambda I$ is not, so $\lambda$ is already an eigenvalue (p. 301).
- **8.9.** If $\mathbf F=\mathbf C$, $V$ has a basis of generalized eigenvectors of $T$. Proof by induction on $n=\dim V$.
  - $n=1$: every nonzero vector is an eigenvector.
  - $n>1$: take an eigenvalue $\lambda$. 8.4 for $T-\lambda I$ gives $V=\operatorname{null}(T-\lambda I)^n\oplus\operatorname{range}(T-\lambda I)^n$.
  - If the null space is $V$, we are done. Otherwise $0<\dim\operatorname{range}(T-\lambda I)^n<n$, since $\lambda$ is an eigenvalue.
  - The range is $T$-invariant (5.18). Apply the induction hypothesis to $T$ restricted to it, and adjoin a basis of the null space.
  - $\mathbf F=\mathbf C$ is used to guarantee an eigenvalue exists (p. 301).
  - For $\mathbf F=\mathbf R$ and $\dim V>1$, some operators have such a basis and others do not. Exercise 11 gives a necessary and sufficient condition (p. 301).
- **Example 8.10.** $T$ as in 8.6, on $\mathbf C^3$. Eigenvalues are 0 and 5. Eigenvectors for 0 are $(z_1,0,0)$ and for 5 are $(0,0,z_3)$, which cannot span $\mathbf C^3$. Since $T^3(z)=(0,0,125z_3)$, the generalized eigenvectors for 0 are the nonzero $(z_1,z_2,0)$. Since $(T-5I)^3(z)=(-125z_1+300z_2,-125z_2,0)$, those for 5 are the nonzero $(0,0,z_3)$. The standard basis therefore consists of generalized eigenvectors (p. 302).
- **8.11.** Each generalized eigenvector corresponds to only one eigenvalue. Proof: suppose $v$ is one for $\alpha$ and $\lambda$. Let $m$ be the least positive integer with $(T-\alpha I)^mv=0$, and $n=\dim V$. Then
$$0=(T-\lambda I)^nv=\big((T-\alpha I)+(\alpha-\lambda)I\big)^nv=\sum_{k=0}^n b_k(\alpha-\lambda)^{n-k}(T-\alpha I)^kv,$$
  with $b_0=1$. Apply $(T-\alpha I)^{m-1}$. The terms with $k\ge1$ vanish because $(T-\alpha I)^{m-1+k}v=0$ (added step). This leaves $0=(\alpha-\lambda)^n(T-\alpha I)^{m-1}v$. Since $(T-\alpha I)^{m-1}v\ne0$, $\alpha=\lambda$ (p. 302).
- **8.12.** Every list of generalized eigenvectors for distinct eigenvalues is linearly independent. Proof by contradiction. Take a shortest dependent list $v_1,\dots,v_m$ ($m\ge2$) with $a_1v_1+\dots+a_mv_m=0$, all $a_k\ne0$. Apply $(T-\lambda_mI)^n$ with $n=\dim V$, which gives 8.13: $a_1(T-\lambda_mI)^nv_1+\dots+a_{m-1}(T-\lambda_mI)^nv_{m-1}=0$.
  - For $k<m$, $(T-\lambda_mI)^nv_k\ne0$, else $v_k$ would belong to two eigenvalues, contradicting 8.11.
  - Also $(T-\lambda_kI)^n\big((T-\lambda_mI)^nv_k\big)=(T-\lambda_mI)^n\big((T-\lambda_kI)^nv_k\big)=0$, so each $(T-\lambda_mI)^nv_k$ is a generalized eigenvector for $\lambda_k$.
  - Thus $m-1$ generalized eigenvectors for distinct eigenvalues are dependent, contradicting minimality (p. 303).

*Intuition note.* When a matrix is "defective", the missing directions are found one step deeper: apply $T-\lambda I$ several times instead of once. The uniqueness and independence facts say that these deeper vectors still behave like eigenvectors with respect to which $\lambda$ they belong to.

**Nilpotent operators.**
- **8.14.** $T$ is *nilpotent* if some power of it is 0. Equivalently, every nonzero vector is a generalized eigenvector for 0 (p. 303).
- **Example 8.15.** (a) $T(z_1,\dots,z_4)=(0,0,z_1,z_2)$ on $\mathbf F^4$ has $T^2=0$. (b) The operator on $\mathbf F^3$ with matrix $\begin{pmatrix}-3&9&0\\-7&9&6\\4&0&-6\end{pmatrix}$ is nilpotent; cubing the matrix gives 0. (c) Differentiation on $\mathcal P_m(\mathbf R)$ is nilpotent, and one needs power $m+1=\dim$ to get 0 (p. 304).
- **8.16.** If $T$ is nilpotent then $T^{\dim V}=0$. If $T^k=0$ then $\operatorname{null}T^k=V$, and 8.1 and 8.3 give $\operatorname{null}T^{\dim V}=V$ (p. 304).
- **8.17.** (a) If $T$ is nilpotent, 0 is an eigenvalue and the only one. If $T^m=0$ then $T$ is not injective. If $Tv=\lambda v$ with $v\neq0$, then $\lambda^mv=T^mv=0$, so $\lambda=0$. (b) If $\mathbf F=\mathbf C$ and 0 is the only eigenvalue, then $T$ is nilpotent: by 5.27(b) the minimal polynomial is $z^m$ (pp. 304–305). Exercise 23 shows that $\mathbf F=\mathbf C$ cannot be dropped in (b) (p. 305).
- **8.18.** For $T\in\mathcal L(V)$ these are equivalent: (a) $T$ is nilpotent; (b) the minimal polynomial is $z^m$ for some positive $m$; (c) some basis gives an upper-triangular matrix with all entries on and below the diagonal equal to 0. Proof: (a)⇒(b) because $z^n$ is a multiple of the minimal polynomial (5.29). (b)⇒(c) by 5.27(a), 5.44 and 5.41. (c)⇒(a) by 5.40 (p. 305).

*Intuition note.* A nilpotent operator is a map that eventually sends everything to zero. Its matrix can be made strictly upper triangular, so more than half its entries are zero. Section 8C does better.

**Exercises 8A** are listed at the end (pp. 306–307).

### 8B Generalized Eigenspace Decomposition

**Generalized eigenspaces.**
- **8.19.** $G(\lambda,T)=\{v\in V:(T-\lambda I)^kv=0\text{ for some positive integer }k\}$. It is the generalized eigenvectors for $\lambda$ plus 0. Always $E(\lambda,T)\subseteq G(\lambda,T)$ (p. 308).
- **8.20.** $G(\lambda,T)=\operatorname{null}(T-\lambda I)^{\dim V}$, by 8.1 and 8.3 for $T-\lambda I$. So it is a subspace (p. 308).
- **Example 8.21.** For $T(z)=(4z_2,0,5z_3)$: $G(0,T)=\{(z_1,z_2,0)\}$ and $G(5,T)=\{(0,0,z_3)\}$, and $\mathbf C^3=G(0,T)\oplus G(5,T)$ (p. 308).
- **8.22 Generalized eigenspace decomposition.** Suppose $\mathbf F=\mathbf C$ and $\lambda_1,\dots,\lambda_m$ are the distinct eigenvalues. Then (a) each $G(\lambda_k,T)$ is $T$-invariant; (b) $(T-\lambda_kI)|_{G(\lambda_k,T)}$ is nilpotent; (c) $V=G(\lambda_1,T)\oplus\cdots\oplus G(\lambda_m,T)$.
  - (a): $G(\lambda_k,T)=\operatorname{null}(T-\lambda_kI)^{\dim V}$ is invariant by 5.18.
  - (b): by 8.20, $\big((T-\lambda_kI)|_G\big)^{\dim V}=0$.
  - (c): if $v_1+\dots+v_m=0$ with $v_k\in G(\lambda_k,T)$, then 8.12 gives each $v_k=0$, so the sum is direct (1.45). Every vector is a sum of generalized eigenvectors by 8.9 (p. 309).
  - Exercise 8 gives the analogue for $\mathbf F=\mathbf R$ (p. 309).

*Intuition note.* Over $\mathbf C$ the space cuts into independent blocks, one per eigenvalue. On the block for $\lambda$, $T$ is just $\lambda I$ plus a map that eventually dies.

**Multiplicity of an eigenvalue.**
- **8.23.** The *multiplicity* of $\lambda$ is $\dim G(\lambda,T)=\dim\operatorname{null}(T-\lambda I)^{\dim V}$ (p. 310).
- **Example 8.24.** $T(z)=(6z_1+3z_2+4z_3,\,6z_2+2z_3,\,7z_3)$ has matrix $\begin{pmatrix}6&3&4\\0&6&2\\0&0&7\end{pmatrix}$. Eigenvalues are 6 and 7. $G(6,T)=\operatorname{span}((1,0,0),(0,1,0))$ and $G(7,T)=\operatorname{span}((10,2,1))$. So 6 has multiplicity 2 and 7 has multiplicity 1. A basis of generalized eigenvectors is $(1,0,0),(0,1,0),(10,2,1)$. There is no basis of eigenvectors (p. 310).
- **8.25.** If $\mathbf F=\mathbf C$, the multiplicities sum to $\dim V$ (from 8.22 and 3.94) (p. 311).
- Terminology as printed: algebraic multiplicity $=\dim\operatorname{null}(T-\lambda I)^{\dim V}=\dim G(\lambda,T)$, which is this book's multiplicity. Geometric multiplicity $=\dim\operatorname{null}(T-\lambda I)=\dim E(\lambda,T)$. The author says his definition is cleaner than the determinant one, and that 9.62 shows they agree. For normal $T$ on an inner product space the two multiplicities are equal, as seen from Exercise 27 in 7A applied to $T-\lambda I$ (p. 311).
- **8.26 Characteristic polynomial.** For $\mathbf F=\mathbf C$, with distinct eigenvalues $\lambda_1,\dots,\lambda_m$ and multiplicities $d_1,\dots,d_m$: $(z-\lambda_1)^{d_1}\cdots(z-\lambda_m)^{d_m}$. **Example 8.27:** for $T$ of 8.24 it is $(z-6)^2(z-7)$ (p. 311).
- **8.28.** The characteristic polynomial has degree $\dim V$ (by 8.25), and its zeros are the eigenvalues (by definition) (p. 312).
- **8.29 Cayley–Hamilton.** If $\mathbf F=\mathbf C$ and $q$ is the characteristic polynomial, then $q(T)=0$. Proof: let $d_k=\dim G(\lambda_k,T)$. By 8.16, $(T-\lambda_kI)^{d_k}|_{G(\lambda_k,T)}=0$. Since $V$ is the sum of the $G$'s (8.22), it suffices to show $q(T)|_{G(\lambda_k,T)}=0$ for each $k$. In $q(T)=(T-\lambda_1I)^{d_1}\cdots(T-\lambda_mI)^{d_m}$ the factors commute. Move $(T-\lambda_kI)^{d_k}$ to the end, and it kills $G(\lambda_k,T)$ (p. 312).
- **8.30.** The characteristic polynomial is a polynomial multiple of the minimal polynomial (8.29 and 5.29). So if the minimal polynomial has degree $\dim V$, the two are equal (p. 312).
- **8.31.** Suppose $\mathbf F=\mathbf C$ and $v_1,\dots,v_n$ is a basis giving an upper-triangular matrix $A$. Then the number of times $\lambda$ appears on the diagonal of $A$ equals the multiplicity of $\lambda$. Proof:
  - Let $\lambda_1,\dots,\lambda_n$ be the diagonal entries. Then $Tv_k=u_k+\lambda_kv_k$ with $u_k\in\operatorname{span}(v_1,\dots,v_{k-1})$. If $\lambda_k\ne0$, $Tv_k$ is not a combination of $Tv_1,\dots,Tv_{k-1}$. By the linear dependence lemma (2.19), the $Tv_k$ with $\lambda_k\ne0$ are independent.
  - With $d$ = number of $k$ with $\lambda_k=0$: $\dim\operatorname{range}T\ge n-d$, hence $\dim\operatorname{null}T\le d$ (8.32).
  - $T^n$ has matrix $A^n$ with diagonal entries $\lambda_k^n$ (Exercise 2(b) of 5C), and $\lambda_k^n=0$ iff $\lambda_k=0$. So $\dim\operatorname{null}T^n\le d$ (8.33).
  - Replace $T$ by $T-\lambda I$. With $m_\lambda$ the multiplicity and $d_\lambda$ the diagonal count, $m_\lambda\le d_\lambda$ (8.34).
  - Both $\sum m_\lambda$ (by 8.25) and $\sum d_\lambda$ equal $n$. So every inequality is an equality (p. 313).

*Intuition note.* Counting an eigenvalue by the dimension of its generalized eigenspace is the same as counting how often it sits on the diagonal. That count is the same for every upper-triangular form of $T$.

**Block diagonal matrices.**
- **8.35.** A *block diagonal matrix* is a square matrix with square matrices $A_1,\dots,A_m$ along the diagonal and 0 elsewhere. **Example 8.36:** a 5×5 matrix with blocks $A_1=(4)$, $A_2=\begin{pmatrix}2&-3\\0&2\end{pmatrix}$, $A_3=\begin{pmatrix}1&7\\0&1\end{pmatrix}$ (p. 314).
- **8.37.** If $\mathbf F=\mathbf C$, some basis gives a block diagonal matrix with each $A_k$ a $d_k$-by-$d_k$ upper-triangular matrix with $\lambda_k$ on its whole diagonal. Proof: on each $G(\lambda_k,T)$ pick a basis such that $(T-\lambda_kI)|_G$ has the form in 8.18(c). Then $T|_G=(T-\lambda_kI)|_G+\lambda_kI|_G$ has the form $A_k$. Concatenate the bases using 8.22 (p. 315).
- **Example 8.38.** For $T$ of 8.24 the standard-basis matrix is upper triangular but not of block form. In the basis $(1,0,0),(0,1,0),(10,2,1)$ the matrix is $\begin{pmatrix}6&3&0\\0&6&0\\0&0&7\end{pmatrix}$, which has the form promised by 8.37 (p. 315).

### 8C Consequences of Generalized Eigenspace Decomposition

**Square roots.** A *square root* of $T$ is an $R$ with $R^2=T$. Not every operator on a complex space has one: $T(z_1,z_2,z_3)=(z_2,z_3,0)$ has none (Exercise 1). The author says this operator's non-invertibility "is no accident" (p. 319).
- **8.39.** If $T$ is nilpotent, $I+T$ has a square root (valid over $\mathbf R$ and $\mathbf C$). Proof idea:
  - Use the Taylor series $\sqrt{1+x}=1+a_1x+a_2x^2+\cdots$ (8.40) only as motivation, without worrying about convergence.
  - If $T^m=0$, guess a root of the form $I+a_1T+\dots+a_{m-1}T^{m-1}$. Its square is
$$I+2a_1T+(2a_2+a_1^2)T^2+(2a_3+2a_1a_2)T^3+\cdots+(2a_{m-1}+\text{terms in }a_1,\dots,a_{m-2})T^{m-1}.$$
  - Choose $a_1$ with $2a_1=1$ ($a_1=1/2$). Then $2a_2+a_1^2=0$ ($a_2=-1/8$). Then the coefficient of $T^3$ is 0 ($a_3=1/16$). Continue so each coefficient of $T^k$, $k=4,\dots,m-1$, is 0. Only existence of suitable $a_k$ matters (p. 319).
- The next result needs $\mathbf C$. The multiplication-by-$-1$ operator on the real line $\mathbf R$ has no square root. Every $z=r(\cos\theta+i\sin\theta)$ has the square root $\sqrt r(\cos\frac\theta2+i\sin\frac\theta2)$ (p. 320).
- **8.41.** If $V$ is complex and $T$ invertible, $T$ has a square root. Proof:
  - On each $G(\lambda_k,T)$, $T=\lambda_kI+T_k$ with $T_k$ nilpotent (8.22(b)). Since $T$ is invertible, $\lambda_k\ne0$, so $T|_G=\lambda_k\big(I+T_k/\lambda_k\big)$.
  - $T_k/\lambda_k$ is nilpotent, so $I+T_k/\lambda_k$ has a square root (8.39). Multiply it by a square root of $\lambda_k$ to get a square root $R_k$ of $T|_{G(\lambda_k,T)}$.
  - For $v=u_1+\dots+u_m$ (unique, 8.22) define $Rv=R_1u_1+\dots+R_mu_m$. The reader is asked to verify $R^2=T$ (p. 320).
  - The author says that imitating these techniques should prove that invertible operators on complex spaces have $k$th roots (p. 320). Exercise 3 asks this for cube roots.

*Intuition note.* On each block, $T$ is a nonzero scalar times (identity plus a "small" nilpotent part). That form behaves like $1+x$ with $x$ small, which has a root.

**Jordan form.**
- **8.42.** $T(z_1,\dots,z_4)=(0,z_1,z_2,z_3)$ on $\mathbf C^4$ has $T^4=0$. With $v=(1,0,0,0)$, $T^3v,T^2v,Tv,v$ is a basis, and the matrix has 1's on the line above the diagonal and 0 elsewhere (p. 321).
- **8.43.** $T(z_1,\dots,z_6)=(0,z_1,z_2,0,z_4,0)$ has $T^3=0$. No single $v$ gives a basis $T^5v,\dots,v$. But with $v_1=(1,0,0,0,0,0)$, $v_2=(0,0,0,1,0,0)$, $v_3=(0,0,0,0,0,1)$, the list $T^2v_1,Tv_1,v_1,Tv_2,v_2,v_3$ is a basis. The matrix is block diagonal with a 3×3 block (1's above the diagonal), a 2×2 block (1 above) and a 1×1 block $(0)$ (p. 321).
- **8.44 Jordan basis.** A basis of $V$ is a *Jordan basis* for $T$ if $T$ has a block diagonal matrix $A_1,\dots,A_p$ where each $A_k$ has $\lambda_k$ on the diagonal, 1's on the line directly above the diagonal, and 0 elsewhere. The $\lambda_k$ need not be distinct, and a block may be $1\times1$ (p. 322).
- **8.45.** Every nilpotent operator has a Jordan basis (valid for real and complex spaces). Proof by induction on $\dim V$:
  - $\dim V=1$: $T=0$.
  - Let $m$ be the least positive integer with $T^m=0$, and $u$ with $T^{m-1}u\ne0$. Put $U=\operatorname{span}(u,Tu,\dots,T^{m-1}u)$. This list is independent (Exercise 2 of 8A). If $U=V$, reversing it gives a Jordan basis.
  - Otherwise $U$ is $T$-invariant. By induction $T|_U$ has a Jordan basis. The plan is to find a $T$-invariant $W$ with $V=U\oplus W$ and use induction on $W$.
  - Choose $\varphi\in V'$ with $\varphi(T^{m-1}u)\ne0$. Let $W=\{v\in V:\varphi(T^kv)=0,\ k=0,\dots,m-1\}$. It is invariant: if $v\in W$ then $\varphi(T^k(Tv))=0$ for $k=0,\dots,m-1$, using $T^m=0$ for $k=m-1$.
  - $U\cap W=\{0\}$: let $0\ne v\in U\cap W$ and $v=c_0u+\dots+c_{m-1}T^{m-1}u$. Let $j$ be the least index with $c_j\ne0$. Applying $T^{m-j-1}$ gives $T^{m-j-1}v=c_jT^{m-1}u$. Then $\varphi(T^{m-j-1}v)=c_j\varphi(T^{m-1}u)\ne0$, so $v\notin W$.
  - Dimension: define $S:V\to\mathbf F^m$, $Sv=(\varphi(v),\varphi(Tv),\dots,\varphi(T^{m-1}v))$. Then $\operatorname{null}S=W$, and $\dim W=\dim V-\dim\operatorname{range}S\ge\dim V-m$. So $\dim(U\oplus W)\ge m+(\dim V-m)=\dim V$, hence $U\oplus W=V$ (2.39) (pp. 322–323).
- **8.46 Jordan form.** If $\mathbf F=\mathbf C$, some basis of $V$ is a Jordan basis for $T$. Proof: by 8.22, $V=\bigoplus G(\lambda_k,T)$ with $(T-\lambda_kI)|_G$ nilpotent. By 8.45 pick a Jordan basis of each; concatenate (p. 324).

*Intuition note.* A nilpotent operator is a set of "chains" $v\mapsto Tv\mapsto T^2v\mapsto\dots\mapsto0$. Each chain becomes one Jordan block. Adding the eigenvalue back on each generalized eigenspace gives the general Jordan form.

**Exercises 8C** are listed at the end (pp. 324–325).

### 8D Trace: A Connection Between Matrices and Operators

- **8.47.** The *trace* $\operatorname{tr}A$ of a square matrix is the sum of its diagonal entries. **Example 8.48:** $A=\begin{pmatrix}3&-1&-2\\5&2&-3\\1&6&0\end{pmatrix}$ has $\operatorname{tr}A=3+2+0=5$ (p. 326).
- **8.49.** If $A$ is $m\times n$ and $B$ is $n\times m$, then $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. Proof: the $j$th diagonal entry of $AB$ is $\sum_{k=1}^nA_{j,k}B_{k,j}$. So
$$\operatorname{tr}(AB)=\sum_{j=1}^m\sum_{k=1}^nA_{j,k}B_{k,j}=\sum_{k=1}^n\sum_{j=1}^mB_{k,j}A_{j,k}=\sum_{k=1}^n(k\text{th diagonal entry of }BA)=\operatorname{tr}(BA)$$
  (p. 326).
- **8.50.** $\operatorname{tr}\mathcal M(T,(u_1,\dots,u_n))=\operatorname{tr}\mathcal M(T,(v_1,\dots,v_n))$ for two bases. Proof: with $A$, $B$ the two matrices, 3.84 gives an invertible $C$ with $A=C^{-1}BC$. Then $\operatorname{tr}A=\operatorname{tr}((C^{-1}B)C)=\operatorname{tr}(C(C^{-1}B))=\operatorname{tr}((CC^{-1})B)=\operatorname{tr}B$, the second step by 8.49 (p. 327).
- **8.51.** So $\operatorname{tr}T:=\operatorname{tr}\mathcal M(T,(v_1,\dots,v_n))$ for any basis is well defined (p. 327).
- **8.52.** If $\mathbf F=\mathbf C$, $\operatorname{tr}T$ equals the sum of the eigenvalues, each counted as many times as its multiplicity ($d_1\lambda_1+\dots+d_m\lambda_m$). Proof: use the upper-triangular basis of 8.37, whose diagonal lists the eigenvalues with multiplicity, and 8.50 (pp. 327–328).
- **Example 8.53.** $T(z)=(3z_1-z_2-2z_3,\,3z_1+2z_2-3z_3,\,z_1+2z_2)$ has matrix $\begin{pmatrix}3&-1&-2\\3&2&-3\\1&2&0\end{pmatrix}$ and trace 5. Its eigenvalues are $1$, $2+3i$, $2-3i$, each with multiplicity 1, and $1+(2+3i)+(2-3i)=5$ (p. 328).
- **8.54.** If $\mathbf F=\mathbf C$ and $n=\dim V$, $\operatorname{tr}T$ is the negative of the coefficient of $z^{n-1}$ in the characteristic polynomial. This follows from the expansion $z^n-(\lambda_1+\dots+\lambda_n)z^{n-1}+\dots+(-1)^n(\lambda_1\cdots\lambda_n)$. See 9.65 for the case without $\mathbf F=\mathbf C$ (p. 328).
- **8.55.** If $V$ is an inner product space and $e_1,\dots,e_n$ is an orthonormal basis, $\operatorname{tr}T=\langle Te_1,e_1\rangle+\dots+\langle Te_n,e_n\rangle$, since the $(k,k)$ entry of the matrix is $\langle Te_k,e_k\rangle$ (p. 329).
- **8.56.** $\operatorname{tr}:\mathcal L(V)\to\mathbf F$ is a linear functional and $\operatorname{tr}(ST)=\operatorname{tr}(TS)$. Proof: fix a basis. Then $\operatorname{tr}(\lambda T)=\lambda\operatorname{tr}T$ via 3.38. Also $\operatorname{tr}(S+T)=\operatorname{tr}S+\operatorname{tr}T$ via 3.35. Finally $\operatorname{tr}(ST)=\operatorname{tr}(\mathcal M(S)\mathcal M(T))=\operatorname{tr}(\mathcal M(T)\mathcal M(S))=\operatorname{tr}(TS)$ via 3.43 and 8.49. The equations $\operatorname{tr}(ST)=\operatorname{tr}(TS)$ and $\operatorname{tr}I=\dim V$ characterise the trace among linear functionals (Exercise 10) (p. 329).
- **8.57.** There are no $S,T\in\mathcal L(V)$ with $ST-TS=I$. Proof: $\operatorname{tr}(ST-TS)=\operatorname{tr}(ST)-\operatorname{tr}(TS)=0$, but $\operatorname{tr}I=\dim V\ne0$. The result fails in infinite dimensions (Exercise 13) (p. 330).

*Intuition note.* The trace ignores the choice of basis, because changing basis conjugates the matrix and conjugation does not change the trace. Over $\mathbf C$, this means the diagonal sum equals the sum of eigenvalues. A further consequence (8.56) is that $ST-TS$ always has trace 0, while $\operatorname{tr}I=\dim V\ne0$, so $ST-TS=I$ is impossible.

## Toy example (ours, not from the text)
Let $T$ on $\mathbf C^2$ be $T(z_1,z_2)=(2z_1+z_2,\,2z_2)$, with matrix $\begin{pmatrix}2&1\\0&2\end{pmatrix}$.
- **Eigenvectors:** $(T-2I)(z_1,z_2)=(z_2,0)$, so $E(2,T)=\{(z_1,0)\}$ has dimension 1. Eigenvectors do not span $\mathbf C^2$.
- **Generalized eigenspace:** let $N=T-2I$. Then $N^2(z_1,z_2)=N(z_2,0)=(0,0)$, so $N^2=0$ and $G(2,T)=\operatorname{null}N^2=\mathbf C^2$. Multiplicity 2 equals $\dim V$ (8.25).
- **Characteristic polynomial and Cayley–Hamilton:** $q=(z-2)^2$ and $q(T)=N^2=0$. The minimal polynomial is also $(z-2)^2$, since $N\neq0$.
- **Jordan basis:** take $v=(0,1)$. Then $Nv=(1,0)$ and $N^2v=0$. In the basis $Nv,v=(1,0),(0,1)$: $T(1,0)=(2,0)=2(1,0)$ and $T(0,1)=(1,2)=1\cdot(1,0)+2\cdot(0,1)$. The matrix is $\begin{pmatrix}2&1\\0&2\end{pmatrix}$, one Jordan block.
- **Square root (8.39, 8.41):** $T=2(I+N/2)$. Take $I+\tfrac12\cdot\frac N2=I+\frac N4$ as a root of $I+N/2$. Its square is $I+\frac N2+\frac{N^2}{16}=I+\frac N2$. So $R=\sqrt2\,(I+N/4)=\sqrt2\begin{pmatrix}1&1/4\\0&1\end{pmatrix}$ and $R^2=2\begin{pmatrix}1&1/2\\0&1\end{pmatrix}=\begin{pmatrix}2&1\\0&2\end{pmatrix}=T$.
- **Trace:** $\operatorname{tr}T=2+2=4=2+2$, the sum of eigenvalues with multiplicity (8.52).

## Concepts
- [[generalized-eigenvector]] (new) — nonzero $v$ with $(T-\lambda I)^kv=0$ for some $k\ge1$; $k=\dim V$ suffices (pp. 300–301)
- [[generalized-eigenspace]] (new) — $G(\lambda,T)=\operatorname{null}(T-\lambda I)^{\dim V}$, containing $E(\lambda,T)$ (p. 308)
- [[nilpotent-operator]] (new) — some power of $T$ is 0; then $T^{\dim V}=0$ and 0 is the only eigenvalue (pp. 303–304)
- [[generalized-eigenspace-decomposition]] (new) — over $\mathbf C$, $V=\bigoplus_kG(\lambda_k,T)$ with invariant pieces (p. 309)
- [[multiplicity]] (new) — $\dim G(\lambda,T)$, the book's "algebraic multiplicity" (pp. 310–311)
- [[characteristic-polynomial]] — here $\prod(z-\lambda_k)^{d_k}$ over $\mathbf C$, defined by multiplicities, not determinants (p. 311)
- [[cayley-hamilton-theorem]] (new) — $q(T)=0$ for the characteristic polynomial $q$ (p. 312)
- [[minimal-polynomial]] (new) — the minimal polynomial from Chapter 5 (not re-defined here); for nilpotent $T$ it is $z^m$, and over $\mathbf C$ it divides the characteristic polynomial (pp. 305, 312)
- [[block-diagonal-matrix]] (new) — square blocks on the diagonal, 0 elsewhere (p. 314)
- [[jordan-form]] (new) — a basis in which blocks have $\lambda_k$ on the diagonal and 1's directly above (pp. 322–324)
- [[operator-square-root]] (new) — $R$ with $R^2=T$; invertible operators on complex spaces have them (pp. 319–320)
- [[trace]] (new) — sum of diagonal entries; basis-independent; equals the sum of eigenvalues with multiplicity over $\mathbf C$ (pp. 326–328)
- [[eigenvector-eigenvalue]] — $Tv=\lambda v$; generalized to powers of $T-\lambda I$ (p. 301)
- [[rank-nullity]] — used in 8.4 and 8.45 (pp. 299, 323)
- [[change-of-basis]] — $A=C^{-1}BC$ used for trace invariance (p. 327)
- [[diagonalization]] — equals having an eigenvector basis; the failure of this motivates the chapter (p. 300)

## Canonical instances
- [[ex-T-4z2-0-5z3]] — $T(z)=(4z_2,0,5z_3)$: eigenvectors too few, but generalized eigenspaces give $\mathbf C^3=G(0,T)\oplus G(5,T)$ (pp. 299–302, 308)
- [[ex-upper-triangular-6-7]] — matrix with eigenvalues 6 (multiplicity 2) and 7: multiplicity, characteristic polynomial, block form (pp. 310–311, 315)
- [[ex-nilpotent-shift-C4-C6]] — shift-type nilpotent operators and their Jordan blocks (p. 321)
- [[ex-differentiation-nilpotent]] — differentiation on $\mathcal P_m(\mathbf R)$ is nilpotent of index $m+1$ (p. 304)
- [[ex-trace-3x3-complex-eigenvalues]] — trace 5 equals $1+(2+3i)+(2-3i)$ (p. 328)

## Bridges (candidates)
- [same-math] $(I-T)^{-1}=I+T+\dots+T^{m-1}$ for nilpotent $T$ (Exercise 8A.17) ↔ linear-algebra: Katz–Bonacich centrality $(I-\beta A)^{-1}$ for an acyclic-graph adjacency matrix (finite walk count) — same Neumann series.
- [same-math] trace $=$ sum of eigenvalues with multiplicity (8.52) ↔ linear-algebra: total variance in PCA equals the sum of covariance eigenvalues (covariance is symmetric, so it is a special case).
- [structural-analogy] chains $v\mapsto Tv\mapsto\dots\mapsto0$ forming Jordan blocks ↔ linear-algebra: $A^k$ for defective matrices (polynomial growth factors beyond $\lambda^k$) — Jordan blocks explain the non-diagonalizable behaviour.
- [structural-analogy] generalized eigenspace decomposition ↔ linear-algebra: spectral theorem — both split $V$ into $T$-invariant pieces, one per eigenvalue, without needing orthogonality in the first.

## Questions this raises
- Given a matrix, how can one actually compute the Jordan basis, and is Jordan form numerically stable?
- Is the Jordan form unique up to the order of the blocks? (For nilpotent $T$, Exercise 8C.13 (p. 325) shows that the number $n$ of chains equals $\dim\operatorname{null}T$, so it does not depend on the Jordan basis.)
- Over $\mathbf R$, what replaces Jordan form when the operator has non-real eigenvalues?
- What extra hypotheses extend 8.57 to infinite-dimensional spaces, as hinted for quantum theory (p. 330)?

## Exercises worth doing
- Ex. 8A.2 (p. 306) — a chain $v,Tv,\dots,T^{m-1}v$ with $T^{m-1}v\ne0$ is independent; used in 8.45 — difficulty: easy
- Ex. 8A.17 (p. 307) — $I-T$ is invertible for nilpotent $T$ and has the inverse $I+T+\dots+T^{m-1}$; explain how to guess it — difficulty: easy
- Ex. 8A.23 (p. 307) — an example over $\mathbf R$ with 0 the only eigenvalue but $T$ not nilpotent — difficulty: easy
- Ex. 8B.9 (p. 316) — $T=D+N$ with $D$ diagonalizable, $N$ nilpotent, $DN=ND$ — difficulty: medium
- Ex. 8C.4 (p. 324) — over $\mathbf R$, $-I$ has a square root iff $\dim V$ is even — difficulty: medium
- Ex. 8D.10 (p. 331) — trace is the only linear functional with $\tau(ST)=\tau(TS)$ and $\tau(I)=\dim V$ — difficulty: hard

## Reading notes
- Printed page = pdf page − 14; for example, pdf page 311 is printed page 297. The page labels give the printed numbers directly.
- The text layer shows math letters as garbled symbols. I read all equations from the page images.
- On the page between printed pages 313 and 315, the header image shows "≈ 100π" where the page number would be expected. I used 314 as its page number.
- Exercises are only listed, not solved. Exercise statements use $\mathbf F$ and $\mathbf C$ as printed.
- Several facts cited from earlier chapters (5.27, 5.29, 5.41, 5.44, 3.84, 9.62, 9.65, Exercise 27 of 7A) are stated here only as references, not proved in this unit.
- No errors in the mathematics were noticed while copying the statements and proofs.
