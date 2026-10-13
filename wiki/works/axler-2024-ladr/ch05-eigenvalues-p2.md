---
id: axler-2024-ladr/ch05-eigenvalues-p2
work: axler-2024-ladr
unit: "5 Eigenvalues and Eigenvectors (part 2/2): 5C Upper-Triangular Matrices, 5D Diagonalizable Operators, 5E Commuting Operators"
pages: 154–180
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# Upper-Triangular, Diagonalizable and Commuting Operators (Axler, LADR 4e, §§5C–5E)

## L0 — One line
Whether an operator on a finite-dimensional space has a triangular or diagonal matrix in some basis is decided by its minimal polynomial (split into degree-1 factors, or into *distinct* degree-1 factors), and commuting operators over C can be made upper triangular together, and commuting diagonalizable operators can be diagonalized together.

## L1 — The gist (≤ 120 words)
This part of Chapter 5 asks when an operator on a finite-dimensional space has a simple matrix. Upper-triangular matrices exist in some basis exactly when the minimal polynomial splits into degree-1 factors, so always over C; their diagonal lists the eigenvalues. Diagonal matrices exist exactly when the minimal polynomial has distinct degree-1 factors, equivalently when there is a basis of eigenvectors; dim V distinct eigenvalues suffice. The Gershgorin theorem locates eigenvalues near diagonal entries. Commuting operators (over C) share an eigenvector, can be made upper triangular together, and if diagonalizable can be diagonalized together. Over C, each eigenvalue of a sum or product of commuting operators is a sum or product of eigenvalues.

**Prerequisites:** matrix of a linear map; invariant subspaces and eigenvectors; minimal polynomial and its basic properties (5.27, 5.29); direct sums, dimension formulas; induction.

## L2 — Key ideas (5–10 bullets)
- An operator has an upper-triangular matrix in basis $v_1,\dots,v_n$ iff each $\operatorname{span}(v_1,\dots,v_k)$ is invariant; this links matrix shape to invariant subspaces (5.39, p. 156).
- If the matrix is upper triangular, the eigenvalues of $T$ are exactly the diagonal entries, and $(T-\lambda_1 I)\cdots(T-\lambda_n I)=0$ (5.40, 5.41, pp. 156–157).
- Over a finite-dimensional space, an upper-triangular matrix exists iff the minimal polynomial is a product of degree-1 factors. Hence over $\mathbf C$ one always exists, but there is no method to compute it exactly (5.44, 5.47, pp. 159–160).
- Diagonalizable ⟺ basis of eigenvectors ⟺ $V$ is the direct sum of the eigenspaces ⟺ dimensions of eigenspaces add up to $\dim V$ (5.55, p. 165).
- Diagonalizable ⟺ minimal polynomial has *distinct* degree-1 factors (5.62, p. 169). Having $\dim V$ distinct eigenvalues is sufficient but not necessary (5.58, p. 166).
- Diagonalization turns powers of an operator into powers of scalars, e.g. $T^{100}$ in Example 5.59 (p. 167).
- Gershgorin: every eigenvalue lies in some disk centred at a diagonal entry with radius the sum of the other absolute entries in that row (5.67, p. 171).
- Commuting operators: each eigenspace of one is invariant under the other (5.75, p. 176). Diagonalizable operators are simultaneously diagonalizable iff they commute (5.76, p. 176).
- Over $\mathbf C$, commuting operators have a common eigenvector and a common upper-triangularizing basis, so each eigenvalue of $S+T$ and $ST$ is a sum or product of eigenvalues of $S$ and $T$ (5.78, 5.80, 5.81, pp. 177–179).

## L3 — Walkthrough

### 5C Upper-Triangular Matrices

**5.35 Matrix of an operator.** For $T\in\mathcal L(V)$ and basis $v_1,\dots,v_n$ of $V$, $\mathcal M(T)$ is the $n\times n$ matrix with entries $A_{j,k}$ defined by
$$Tv_k = A_{1,k}v_1+\cdots+A_{n,k}v_n .$$
The $k$th column holds the coefficients of $Tv_k$. Operators have square matrices. On $\mathbf F^n$ with no basis stated, use the standard basis (p. 154).

**Example 5.36.** $T(x,y,z)=(2x+y,\,5y+3z,\,8z)$ has standard-basis matrix $\begin{pmatrix}2&1&0\\0&5&3\\0&0&8\end{pmatrix}$ (p. 154).

The author's goal: find a basis in which $\mathcal M(T)$ has many 0's (p. 154). Over a finite-dimensional complex $V$, take an eigenvalue $\lambda$ (exists by 5.19), a corresponding eigenvector $v$, and extend $v$ to a basis. The first column of the matrix is then $(\lambda,0,\dots,0)^T$ (p. 155).

**5.37–5.38.** The *diagonal* is the line of entries from upper left to lower right. A square matrix is *upper triangular* if all entries below the diagonal are 0. In 5.36 the diagonal is 2, 5, 8 (p. 155). At least almost half the entries of a large upper-triangular matrix are 0 (p. 155).

**5.39 Conditions for upper-triangular matrix.** Let $T\in\mathcal L(V)$ and $v_1,\dots,v_n$ a basis. These are equivalent (p. 156):
(a) $\mathcal M(T)$ is upper triangular;
(b) $\operatorname{span}(v_1,\dots,v_k)$ is invariant under $T$ for each $k$;
(c) $Tv_k\in\operatorname{span}(v_1,\dots,v_k)$ for each $k$.

*Proof (key steps, p. 156).* (a)⇒(b): upper triangular gives $Tv_j\in\operatorname{span}(v_1,\dots,v_j)\subseteq\operatorname{span}(v_1,\dots,v_k)$ for $j\le k$. (b)⇒(c): take the case $j=k$. (c)⇒(a): writing $Tv_k$ uses only $v_1,\dots,v_k$, so entries below the diagonal are 0.

*Intuition note.* Column $k$ of the matrix says where $v_k$ goes. "Upper triangular" means $v_k$ never lands outside the earlier basis vectors, so the span of the first $k$ vectors is carried into itself.

**5.40 Equation satisfied.** If $T$ has an upper-triangular matrix with diagonal $\lambda_1,\dots,\lambda_n$, then $(T-\lambda_1I)\cdots(T-\lambda_nI)=0$ (p. 156).

*Proof (p. 157).* Let $v_1,\dots,v_n$ be the basis. $Tv_1=\lambda_1v_1$, so $(T-\lambda_1I)v_1=0$. Since the factors $T-\lambda_jI$ commute, $(T-\lambda_1I)\cdots(T-\lambda_mI)v_1=0$ for all $m$. Next, $(T-\lambda_2I)v_2\in\operatorname{span}(v_1)$, so $(T-\lambda_1I)(T-\lambda_2I)v_2=0$, and hence $(T-\lambda_1I)\cdots(T-\lambda_mI)v_2=0$ for $m\ge2$. Likewise $(T-\lambda_3I)v_3\in\operatorname{span}(v_1,v_2)$, and so on. Thus the full product is 0 on every $v_k$, hence is the 0 operator.

**5.41 Eigenvalues from the diagonal.** If $T$ has an upper-triangular matrix with respect to some basis, the eigenvalues of $T$ are precisely the diagonal entries (p. 157).

*Proof (p. 157).*
- Every diagonal entry is an eigenvalue. $Tv_1=\lambda_1v_1$ gives $\lambda_1$. For $k\ge2$, $(T-\lambda_kI)v_k\in\operatorname{span}(v_1,\dots,v_{k-1})$, so $T-\lambda_kI$ maps the $k$-dimensional $\operatorname{span}(v_1,\dots,v_k)$ into a $(k-1)$-dimensional space. By 3.22 it is not injective on it, so some $v\ne0$ has $(T-\lambda_kI)v=0$.
- No other eigenvalues. Let $q(z)=(z-\lambda_1)\cdots(z-\lambda_n)$. Then $q(T)=0$ (5.40), so $q$ is a polynomial multiple of the minimal polynomial (5.29). The zeros of the minimal polynomial are the eigenvalues (5.27), so every eigenvalue is a zero of $q$.

**Example 5.42.** For the matrix of 5.36, the eigenvalues are 2, 5, 8 (p. 158).

*Intuition note.* Eigenvalues cannot in general be computed exactly from a matrix (p. 157). But if you happen to have a basis giving a triangular matrix, you can just read them off the diagonal.

**Example 5.43 (p. 158).** $T(z_1,z_2,z_3,z_4)=(-z_2,\,z_1,\,2z_1+3z_3,\,z_3+3z_4)$ on $\mathbf F^4$, with standard matrix
$$\begin{pmatrix}0&-1&0&0\\1&0&0&0\\2&0&3&0\\0&0&1&3\end{pmatrix}.$$
Its minimal polynomial (the author says a computer can verify it) is $p(z)=9-6z+10z^2-6z^3+z^4$.
- If $\mathbf F=\mathbf R$: $p(z)=(z^2+1)(z-3)(z-3)$, and $z^2+1$ has no real degree-1 factors. By 5.44 no basis of $\mathbf R^4$ gives an upper-triangular matrix.
- If $\mathbf F=\mathbf C$: $p(z)=(z-i)(z+i)(z-3)(z-3)$, so by 5.44 such a basis exists. Indeed, with basis $(4-3i,-3-4i,-3+i,1)$, $(4+3i,-3+4i,-3-i,1)$, $(0,0,0,1)$, $(0,0,1,0)$ the matrix is $\begin{pmatrix}i&0&0&0\\0&-i&0&0\\0&0&3&1\\0&0&0&3\end{pmatrix}$.

**5.44 Necessary and sufficient condition.** Let $V$ be finite-dimensional, $T\in\mathcal L(V)$. Then $T$ has an upper-triangular matrix with respect to some basis iff the minimal polynomial of $T$ equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some $\lambda_1,\dots,\lambda_m\in\mathbf F$ (p. 159).

*Proof (p. 159).*
- (⇒) Let $\alpha_1,\dots,\alpha_n$ be the diagonal entries and $q(z)=(z-\alpha_1)\cdots(z-\alpha_n)$. Then $q(T)=0$ (5.40), so $q$ is a multiple of the minimal polynomial (5.29). Hence the minimal polynomial is $(z-\lambda_1)\cdots(z-\lambda_m)$ with $\{\lambda_1,\dots,\lambda_m\}\subseteq\{\alpha_1,\dots,\alpha_n\}$.
- (⇐) Induction on $m$. If $m=1$, $T=\lambda_1I$, so every matrix is upper triangular. For $m>1$, let $U=\operatorname{range}(T-\lambda_mI)$, which is invariant under $T$ (special case of 5.18). For $u=(T-\lambda_mI)v\in U$, $(T-\lambda_1I)\cdots(T-\lambda_{m-1}I)u=(T-\lambda_1I)\cdots(T-\lambda_mI)v=0$. So $(z-\lambda_1)\cdots(z-\lambda_{m-1})$ is a multiple of the minimal polynomial of $T|_U$ (5.29), which is then a product of at most $m-1$ terms $z-\lambda_k$. By induction there is a basis $u_1,\dots,u_M$ of $U$ in which $T|_U$ is upper triangular, so by 5.39
$$Tu_k=(T|_U)(u_k)\in\operatorname{span}(u_1,\dots,u_k).\tag{5.45}$$
Extend to a basis $u_1,\dots,u_M,v_1,\dots,v_N$ of $V$. Then $Tv_k=(T-\lambda_mI)v_k+\lambda_mv_k$ with $(T-\lambda_mI)v_k\in U=\operatorname{span}(u_1,\dots,u_M)$, so
$$Tv_k\in\operatorname{span}(u_1,\dots,u_M,v_1,\dots,v_k).\tag{5.46}$$
By 5.45, 5.46 and 5.39, $T$ is upper triangular in this basis.

The set $\{\lambda_1,\dots,\lambda_m\}$ equals the set of eigenvalues of $T$ (5.27); the list may contain repetitions (p. 160).

**5.47 Over $\mathbf C$.** If $V$ is a finite-dimensional complex vector space and $T\in\mathcal L(V)$, then $T$ has an upper-triangular matrix with respect to some basis. *Proof:* 5.44 plus the second version of the fundamental theorem of algebra (4.13) (p. 160). The author says this is improved in Chapter 8 (8.37, 8.46) (p. 160).

*Intuition note.* Over $\mathbf C$ every polynomial splits into degree-1 factors, so the condition in 5.44 always holds. Over $\mathbf R$ an irreducible quadratic factor like $z^2+1$ blocks it.

**Caution and remarks (p. 160).** With an upper-triangular matrix in basis $v_1,\dots,v_n$: the eigenvalues are exactly the diagonal entries, and $v_1$ is an eigenvector, but $v_2,\dots,v_n$ need not be. $v_k$ is an eigenvector iff all entries of column $k$ are 0 except possibly the $k$th. The upper-triangular matrix from row echelon form has no connection with the one in 5.47, and row echelon form does not list the eigenvalues. There is no method for computing exactly a basis as in 5.47, although it exists over $\mathbf C$ (p. 160).

### 5D Diagonalizable Operators

**5.48–5.51.** A *diagonal matrix* is 0 except possibly on the diagonal (e.g. $\operatorname{diag}(8,5,5)$, Example 5.49). An operator is *diagonalizable* if it has a diagonal matrix with respect to some basis. If so, the diagonal entries are precisely the eigenvalues (from 5.41) (p. 163).

*Example 5.51.* $T(x,y)=(41x+7y,\,-20x+74y)$ has standard matrix $\begin{pmatrix}41&7\\-20&74\end{pmatrix}$, not diagonal. In basis $(1,4),(7,5)$ it is $\operatorname{diag}(69,46)$, since $T(1,4)=(69,276)=69(1,4)$ and $T(7,5)=(322,230)=46(7,5)$ (p. 163).

**5.52 Eigenspace.** For $T\in\mathcal L(V)$, $\lambda\in\mathbf F$:
$$E(\lambda,T)=\operatorname{null}(T-\lambda I)=\{v\in V: Tv=\lambda v\}.$$
It is the set of eigenvectors for $\lambda$ together with 0. It is a subspace, and $\lambda$ is an eigenvalue iff $E(\lambda,T)\ne\{0\}$. On $E(\lambda,T)$, $T$ is multiplication by $\lambda$ (p. 164).
*Example 5.53.* If $\mathcal M(T)=\operatorname{diag}(8,5,5)$ in basis $v_1,v_2,v_3$: $E(8,T)=\operatorname{span}(v_1)$, $E(5,T)=\operatorname{span}(v_2,v_3)$ (p. 164).

**5.54 Sum of eigenspaces is direct.** If $\lambda_1,\dots,\lambda_m$ are distinct eigenvalues, then $E(\lambda_1,T)+\cdots+E(\lambda_m,T)$ is a direct sum. If $V$ is finite-dimensional, $\dim E(\lambda_1,T)+\cdots+\dim E(\lambda_m,T)\le\dim V$ (p. 164).
*Proof.* If $v_1+\cdots+v_m=0$ with $v_k\in E(\lambda_k,T)$, linear independence of eigenvectors for distinct eigenvalues (5.11) gives each $v_k=0$; so the sum is direct (1.45). The dimension of a direct sum is the sum of dimensions (3.94) and is at most $\dim V$ (2.37).

**5.55 Conditions equivalent to diagonalizability.** $V$ finite-dimensional, $T\in\mathcal L(V)$, $\lambda_1,\dots,\lambda_m$ the distinct eigenvalues. Equivalent (p. 165):
(a) $T$ is diagonalizable;
(b) $V$ has a basis of eigenvectors of $T$;
(c) $V=E(\lambda_1,T)\oplus\cdots\oplus E(\lambda_m,T)$;
(d) $\dim V=\dim E(\lambda_1,T)+\cdots+\dim E(\lambda_m,T)$.

*Proof (p. 165).* (a)⇔(b): a diagonal matrix with entries $\lambda_k$ in basis $v_1,\dots,v_n$ means exactly $Tv_k=\lambda_kv_k$. (b)⇒(c): every vector is a combination of eigenvectors, so $V=\sum E(\lambda_k,T)$, and 5.54 makes it direct. (c)⇒(d): 3.94. (d)⇒(b): put together bases of the eigenspaces; by 5.56 this list has $n=\dim V$ eigenvectors. If $\sum a_jv_j=0$, group terms by eigenspace into $u_k\in E(\lambda_k,T)$ with $u_1+\cdots+u_m=0$. By 5.11 each $u_k=0$, and since each group is a basis of its eigenspace, all $a_j=0$. So the list is independent, hence a basis (2.38).

*Intuition note.* A diagonal matrix just says "each basis vector is merely stretched". So diagonalizable means the eigenvectors are numerous enough to fill the whole space.

**Example 5.57.** $T(a,b,c)=(b,c,0)$ on $\mathbf F^3$ has matrix $\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$, upper triangular but not diagonal. 0 is the only eigenvalue, $E(0,T)=\{(a,0,0):a\in\mathbf F\}$. So (b), (c), (d) of 5.55 fail, and $T$ is not diagonalizable for $\mathbf F=\mathbf R$ or $\mathbf C$ (p. 166).

**5.58 Enough eigenvalues.** If $V$ is finite-dimensional and $T$ has $\dim V$ distinct eigenvalues, then $T$ is diagonalizable (p. 166).
*Proof.* Pick eigenvectors $v_k$ for each eigenvalue. They are linearly independent (5.11); $\dim V$ independent vectors form a basis (2.38); in it $T$ is diagonal.
This condition is sufficient but not necessary: $T(x,y,z)=(6x,6y,7z)$ has only two eigenvalues but is diagonal in the standard basis of $\mathbf F^3$ (p. 166). Other sufficient conditions appear in the spectral theorems 7.29, 7.31 (named only, p. 166).

**Example 5.59: computing $T^{100}$ (p. 167).** $T(x,y,z)=(2x+y,5y+3z,8z)$, matrix as in 5.36. By 5.41 the eigenvalues are 2, 5, 8; three distinct eigenvalues on a 3-dimensional space, so 5.58 gives diagonalizability. Solving $T(x,y,z)=\lambda(x,y,z)$ gives eigenvectors $(1,0,0)$ for 2, $(1,3,0)$ for 5, $(1,6,6)$ for 8; in this basis the matrix is $\operatorname{diag}(2,5,8)$. Then
$$(0,0,1)=\tfrac16(1,0,0)-\tfrac13(1,3,0)+\tfrac16(1,6,6).$$
Using $T^kv=\lambda^kv$ for an eigenvector $v$:
$$T^{100}(0,0,1)=\tfrac16\big(2^{100}(1,0,0)-2\cdot5^{100}(1,3,0)+8^{100}(1,6,6)\big)=\tfrac16\big(2^{100}-2\cdot5^{100}+8^{100},\ 6\cdot8^{100}-6\cdot5^{100},\ 6\cdot8^{100}\big).$$
Exercise 21 uses the same technique for an exact Fibonacci formula (p. 167).

**Examples 5.60 and 5.61 (p. 168).** Preview: 5.62 says diagonalizable iff minimal polynomial is a product of *distinct* degree-1 factors.
- *5.60.* $T(z_1,\dots,z_5)=(-3z_5,\,z_1+6z_5,\,z_2,\,z_3,\,z_4)$ on $\mathbf C^5$ has minimal polynomial $3-6z+z^5$ (from Example 5.26). No exact expression is known for its zeros, but numerical zeros $\approx-1.67,\,0.51,\,1.40,\,-0.12\pm1.59i$ are accurate to more than three digits, hence good enough to show the five zeros are distinct. So $T$ is diagonalizable by 5.62.
- *5.61.* $T(z_1,z_2,z_3)=(6z_1+3z_2+4z_3,\,6z_2+2z_3,\,7z_3)$ has matrix $\begin{pmatrix}6&3&4\\0&6&2\\0&0&7\end{pmatrix}$. Eigenvalues are 6, 7 (5.41), so zeros of the minimal polynomial are 6, 7 (5.27(a)). By 5.40, $(T-6I)^2(T-7I)=0$. The degree is at most 3 (5.22). So the minimal polynomial is $(z-6)(z-7)$ or $(z-6)^2(z-7)$. A "simple computation" shows $(T-6I)(T-7I)\ne0$; so it is $(z-6)^2(z-7)$ and $T$ is not diagonalizable.

**5.62 Necessary and sufficient condition for diagonalizability.** $V$ finite-dimensional, $T\in\mathcal L(V)$. $T$ is diagonalizable iff the minimal polynomial equals $(z-\lambda_1)\cdots(z-\lambda_m)$ for some list of *distinct* $\lambda_1,\dots,\lambda_m\in\mathbf F$ (p. 169).

*Proof (p. 169).*
- (⇒) Take a basis of eigenvectors $v_j$ and let $\lambda_1,\dots,\lambda_m$ be the distinct eigenvalues. Each $v_j$ satisfies $(T-\lambda_kI)v_j=0$ for some $k$, so $(T-\lambda_1I)\cdots(T-\lambda_mI)v_j=0$. This gives the minimal polynomial.
- (⇐) Assume $(T-\lambda_1I)\cdots(T-\lambda_mI)=0$ (5.63) with distinct $\lambda$'s. Induction on $m$. For $m=1$, $T=\lambda_1I$, diagonalizable. For $m>1$: $\operatorname{range}(T-\lambda_mI)$ is invariant under $T$ (5.18). For $u=(T-\lambda_mI)v$,
$$(T-\lambda_1I)\cdots(T-\lambda_{m-1}I)u=(T-\lambda_1I)\cdots(T-\lambda_mI)v=0.\tag{5.64}$$
So $(z-\lambda_1)\cdots(z-\lambda_{m-1})$ is a multiple of the minimal polynomial of $T$ restricted to that range (5.29). By induction, the range has a basis of eigenvectors of $T$. Next, if $u\in\operatorname{range}(T-\lambda_mI)\cap\operatorname{null}(T-\lambda_mI)$ then $Tu=\lambda_mu$, and 5.64 gives $0=(\lambda_m-\lambda_1)\cdots(\lambda_m-\lambda_{m-1})u$. Because the $\lambda$'s are distinct, $u=0$. So the intersection is $\{0\}$ (1.46), and by 3.94 and 3.21 the sum has dimension $\dim V$: $\operatorname{range}(T-\lambda_mI)\oplus\operatorname{null}(T-\lambda_mI)=V$. Nonzero vectors in the null space are eigenvectors for $\lambda_m$. Joining the two bases gives a basis of eigenvectors.

*Intuition note.* A repeated factor like $(z-6)^2$ means that $T-6I$ "does not finish the job" in one step. Distinct simple factors mean each eigenvalue is killed in one step, which is what a pure stretch does.

Remarks (p. 170): no formula exists for zeros of degree-5 or higher polynomials, yet 5.62 can decide diagonalizability without finding zeros (Exercise 15).

**5.65 Restriction to invariant subspace.** If $T$ is diagonalizable and $U$ is $T$-invariant, then $T|_U$ is diagonalizable (p. 170). *Proof:* the minimal polynomial of $T$ has distinct degree-1 factors (5.62) and is a polynomial multiple of the minimal polynomial of $T|_U$ (5.31); so the latter also has that form, and 5.62 applies.

**Gershgorin Disk Theorem.**
**5.66 Definition.** For $T\in\mathcal L(V)$, basis $v_1,\dots,v_n$ and $A=\mathcal M(T)$, a *Gershgorin disk* is
$$\Big\{z\in\mathbf F:\ |z-A_{j,j}|\le\sum_{\substack{k=1\\k\ne j}}^{n}|A_{j,k}|\Big\},\quad j\in\{1,\dots,n\}.$$
There are $n$ disks. For $\mathbf F=\mathbf C$ each is a closed disk centred at the diagonal entry $A_{j,j}$ with radius the sum of the absolute values of the other entries in row $j$. For $\mathbf F=\mathbf R$ they are closed intervals. If $A$ is diagonal, each disk is a single diagonal entry (p. 170).

**5.67 Theorem.** Each eigenvalue of $T$ lies in some Gershgorin disk with respect to the basis $v_1,\dots,v_n$ (p. 171).

*Proof (p. 171).* Let $\lambda$ be an eigenvalue with eigenvector $w=c_1v_1+\cdots+c_nv_n$ (5.68). Let $A=\mathcal M(T)$. Applying $T$:
$$\lambda w=\sum_{k=1}^n c_kTv_k=\sum_{k=1}^n c_k\sum_{j=1}^n A_{j,k}v_j=\sum_{j=1}^n\Big(\sum_{k=1}^n A_{j,k}c_k\Big)v_j.\tag{5.69, 5.70}$$
Choose $j$ with $|c_j|=\max\{|c_1|,\dots,|c_n|\}$ (so $c_j\neq0$ since $w\neq0$, *added step*). Comparing coefficients of $v_j$: $\lambda c_j=\sum_k A_{j,k}c_k$. Subtract $A_{j,j}c_j$ and divide by $c_j$:
$$|\lambda-A_{j,j}|=\Big|\sum_{k\ne j}A_{j,k}\frac{c_k}{c_j}\Big|\le\sum_{k\ne j}|A_{j,k}|,$$
because $|c_k/c_j|\le1$ (added step).

*Intuition note.* If off-diagonal entries are small, each eigenvalue is near some diagonal entry (p. 170). Gershgorin published this in 1931 (p. 171). Exercise 23 says the radius may instead use column sums (p. 171).

### 5E Commuting Operators

**5.71.** Operators $S,T$ on the same space *commute* if $ST=TS$; square matrices $A,B$ commute if $AB=BA$. Examples: $\lambda I$ commutes with everything; $p(T)$ and $q(T)$ commute for polynomials $p,q$ (5.17(b)) (p. 175).

**Example 5.72 (p. 175).** Let $\mathcal P_m(\mathbf C^2,\mathbf C)$ be the polynomials $p(w,z)=\sum_{j+k\le m}a_{j,k}w^jz^k$ of degree at most $m$. Define
$$D_wp=\frac{\partial p}{\partial w}=\sum_{j+k\le m}ja_{j,k}w^{j-1}z^k,\qquad D_zp=\frac{\partial p}{\partial z}=\sum_{j+k\le m}ka_{j,k}w^jz^{k-1}.$$
They commute: $(D_wD_z)p=\sum jk\,a_{j,k}w^{j-1}z^{k-1}=(D_zD_w)p$.
The author notes that commuting matrices are unusual: of the $214{,}358{,}881=11^8$ ordered pairs of 2-by-2 matrices with integer entries in $[-5,5]$, a computer found only 674,609 commuting pairs, about 0.3% (p. 175).

**5.74.** With $v_1,\dots,v_n$ a basis, $S,T$ commute iff $\mathcal M(S)$ and $\mathcal M(T)$ commute. *Proof:* $ST=TS\iff\mathcal M(ST)=\mathcal M(TS)\iff\mathcal M(S)\mathcal M(T)=\mathcal M(T)\mathcal M(S)$ (p. 176).

**5.75 Eigenspace invariant under commuting operator.** If $S,T$ commute and $\lambda\in\mathbf F$, then $E(\lambda,S)$ is invariant under $T$ (p. 176).
*Proof.* For $v\in E(\lambda,S)$: $S(Tv)=(ST)v=(TS)v=T(Sv)=T(\lambda v)=\lambda Tv$. So $Tv\in E(\lambda,S)$.

**5.76 Simultaneous diagonalizability ⟺ commutativity.** Two diagonalizable operators on the same space have diagonal matrices with respect to the same basis iff they commute (p. 176).
*Proof (pp. 176–177).* (⇒) Diagonal matrices of the same size multiply entrywise on the diagonals, so they commute; use 5.74. (⇐) Let $\lambda_1,\dots,\lambda_m$ be the distinct eigenvalues of $S$. By 5.55(c), $V=E(\lambda_1,S)\oplus\cdots\oplus E(\lambda_m,S)$ (5.77). Each $E(\lambda_k,S)$ is $T$-invariant (5.75), so $T|_{E(\lambda_k,S)}$ is diagonalizable (5.65), giving a basis of $T$-eigenvectors of that eigenspace. Together these bases form a basis of $V$ (by 5.77) of vectors that are eigenvectors of both $S$ and $T$. Exercise 2 of 5E extends this to more than two operators (p. 177).

*Intuition note.* Each eigenspace of $S$ is a block that $T$ also respects. Inside each block $S$ is a scalar, so any eigenbasis of $T$ there also works for $S$.

**5.78 Common eigenvector.** Every pair of commuting operators on a finite-dimensional nonzero complex vector space has a common eigenvector (p. 177). *Proof:* let $\lambda$ be an eigenvalue of $S$ (5.19). $E(\lambda,S)\ne\{0\}$ and is $T$-invariant (5.75), so $T|_{E(\lambda,S)}$ has an eigenvector (5.19), which is an eigenvector of both. The two operators might not share an eigenvalue (p. 177).

**Example 5.79.** For $D_w,D_z$ of 5.72, 0 is the only eigenvalue of each. $E(0,D_w)=\{\sum_{k=0}^m a_kz^k\}$ and $E(0,D_z)=\{\sum_{j=0}^m c_jw^j\}$. Their intersection is the constant functions, which are the common eigenvectors (p. 177).

**5.80 Commuting operators are simultaneously upper triangularizable.** If $V$ is a finite-dimensional complex space and $S,T$ commute, there is a basis in which both have upper-triangular matrices (p. 178).

*Proof (p. 178).* Induction on $n=\dim V$; $n=1$ is trivial. For $n>1$, let $v_1$ be a common eigenvector (5.78), so $Sv_1,Tv_1\in\operatorname{span}(v_1)$. Choose a subspace $W$ with $V=\operatorname{span}(v_1)\oplus W$ (2.33). Define $P:V\to W$ by $P(av_1+w)=w$, and $\hat S,\hat T\in\mathcal L(W)$ by $\hat Sw=P(Sw)$, $\hat Tw=P(Tw)$. They commute: for $w\in W$ there is $a\in\mathbf C$ with
$$(\hat S\hat T)w=\hat S(P(Tw))=\hat S(Tw-av_1)=P\big(S(Tw-av_1)\big)=P\big((ST)w\big),$$
the last step because $Sv_1\in\operatorname{span}(v_1)$ and $Pv_1=0$. Similarly $(\hat T\hat S)w=P((TS)w)$. As $ST=TS$, $\hat S\hat T=\hat T\hat S$. By induction there is a basis $v_2,\dots,v_n$ of $W$ in which both are upper triangular, so $v_1,\dots,v_n$ is a basis of $V$. For $k\ge2$, $Sv_k=a_kv_1+\hat Sv_k$ and $Tv_k=b_kv_1+\hat Tv_k$ with $\hat Sv_k,\hat Tv_k\in\operatorname{span}(v_2,\dots,v_k)$. Hence $Sv_k,Tv_k\in\operatorname{span}(v_1,\dots,v_k)$, and 5.39 finishes. Exercise 9(b) extends this to more operators (p. 178).

**5.81 Eigenvalues of sum and product.** $V$ finite-dimensional complex, $S,T$ commuting. Then every eigenvalue of $S+T$ is an eigenvalue of $S$ plus an eigenvalue of $T$, and every eigenvalue of $ST$ is an eigenvalue of $S$ times an eigenvalue of $T$ (p. 179).
*Proof (p. 179).* Take a basis from 5.80. Then $\mathcal M(S+T)=\mathcal M(S)+\mathcal M(T)$ and $\mathcal M(ST)=\mathcal M(S)\mathcal M(T)$ (3.35, 3.43). Diagonal entries of the sum are sums of corresponding diagonal entries; for products of upper-triangular matrices the diagonal entries multiply. Both results are upper triangular (5C Exercise 2). By 5.41, eigenvalues of each operator are exactly the diagonal entries of its matrix. So every eigenvalue of $S+T$ (resp. $ST$) is a sum (resp. product) of a diagonal entry of $\mathcal M(S)$ and one of $\mathcal M(T)$ at the same position.
The author notes that in general one cannot determine eigenvalues of a sum or product from those of the two operators (p. 179). Exercise 10 shows 5.81 fails on real vector spaces (p. 180).

*Intuition note.* Commuting operators can be triangularized in one common basis, so their diagonals line up entry by entry. Sums and products then act entrywise on the diagonals.

## Toy example (ours, not from the text)
Let $T(x,y)=(3x+y,\,2y)$ on $\mathbf R^2$, matrix $\begin{pmatrix}3&1\\0&2\end{pmatrix}$ (upper triangular, standard basis).
1. By 5.41 the eigenvalues are the diagonal entries 3 and 2. Two distinct eigenvalues, $\dim\mathbf R^2=2$, so 5.58 gives diagonalizability.
2. Eigenvector for 3: $(1,0)$, since $T(1,0)=(3,0)$. For 2: $3x+y=2x$ gives $y=-x$; take $(1,-1)$: $T(1,-1)=(3-1,-2)=(2,-2)=2(1,-1)$.
3. Write $(0,1)=1\cdot(1,0)-1\cdot(1,-1)=(1-1,\,0+1)$. ✓
4. $T^5(0,1)=3^5(1,0)-2^5(1,-1)=243(1,0)-32(1,-1)=(211,\,32)$.
5. Check by iterating: $T(0,1)=(1,2)$; $T(1,2)=(5,4)$; $T(5,4)=(19,8)$; $T(19,8)=(65,16)$; $T(65,16)=(195+16,32)=(211,32)$. ✓
Minimal polynomial: $(z-3)(z-2)$, distinct degree-1 factors, matching 5.62.

## Concepts
- [[matrix as transformation]] — matrix of an operator $\mathcal M(T)$ w.r.t. one basis; column $k$ = coefficients of $Tv_k$ (p. 154)
- [[upper-triangular-matrix]] (new) — square matrix with zeros below the diagonal; ⟺ each $\operatorname{span}(v_1,\dots,v_k)$ is invariant (pp. 155–156)
- [[invariant-subspace]] (new) — subspace $U$ with $Tu\in U$ for all $u\in U$; used throughout (p. 156)
- [[minimal-polynomial]] (new) — smallest-degree monic polynomial $p$ with $p(T)=0$; its zeros are the eigenvalues; here it decides triangularizability and diagonalizability (pp. 157, 159, 169)
- [[eigenvector / eigenvalue]] — read off the diagonal of a triangular matrix (5.41) (p. 157)
- [[eigenspace]] (new) — $E(\lambda,T)=\operatorname{null}(T-\lambda I)$ (p. 164)
- [[diagonalization]] — operator has a diagonal matrix in some basis ⟺ basis of eigenvectors (pp. 163, 165)
- [[direct sum of eigenspaces]] (new) — sum of eigenspaces for distinct eigenvalues is direct; equals $V$ iff diagonalizable (pp. 164–165)
- [[gershgorin-disk-theorem]] (new) — eigenvalues lie in disks centred at diagonal entries with off-diagonal row-sum radius (pp. 170–171)
- [[commuting-operators]] (new) — $ST=TS$; equivalent to commuting matrices in any common basis (pp. 175–176)
- [[simultaneous-diagonalization]] (new) — diagonalizable operators share a diagonalizing basis iff they commute (p. 176)
- [[simultaneous-triangularization]] (new) — commuting complex operators share an upper-triangularizing basis (p. 178)

## Canonical instances
- [[example-5.36-triangular-operator]] — $T(x,y,z)=(2x+y,5y+3z,8z)$: triangular matrix, eigenvalues 2, 5, 8, diagonalized and used for $T^{100}$ (pp. 154, 158, 167)
- [[example-5.43-real-vs-complex-triangularizability]] — same operator is triangularizable over $\mathbf C$ but not $\mathbf R$ (p. 158)
- [[example-5.57-nilpotent-shift]] — $T(a,b,c)=(b,c,0)$: triangular, not diagonalizable (p. 166)
- [[example-5.51-diagonalization-by-new-basis]] — $\operatorname{diag}(69,46)$ in basis $(1,4),(7,5)$ (p. 163)
- [[example-5.61-non-diagonalizable-via-minimal-polynomial]] — minimal polynomial $(z-6)^2(z-7)$ (p. 168)
- [[example-5.72-partial-differentiation-operators]] — commuting operators $D_w,D_z$ with common eigenvectors the constants (pp. 175, 177)
- [[fibonacci-diagonalization]] — only as Exercise 21: $T(x,y)=(y,x+y)$ gives exact formula for $F_n$ (p. 174)

## Bridges (candidates)
- [structural-analogy] $T^kv=\lambda^kv$ for eigenvectors (5.59) ↔ Markov matrices / power iteration: steady-state and long-run behaviour from eigen-decomposition — same mechanism, not developed here.
- [structural-analogy] Fibonacci via diagonalization (Ex. 21) ↔ adjacency matrix: counting walks via $A^k$ by diagonalizing $A$.
- [structural-analogy] Gershgorin disks (5.67) ↔ numerical stability / conditioning: small off-diagonal entries keep eigenvalues near the diagonal.
- [structural-analogy] Simultaneous diagonalization of commuting operators (5.76) ↔ spectral theorem: orthonormal eigenbasis for symmetric matrices (the text only points forward to 7.29, 7.31).
- [same-math] Matrix of $ST$ equals $\mathcal M(S)\mathcal M(T)$ (used in 5.74, 5.81) ↔ matrix multiplication as composition.

## Questions this raises
- If no exact method exists to compute the triangularizing basis of 5.47, how do numerical methods find eigenvalues in practice?
- Is a non-diagonalizable operator "almost" diagonalizable, i.e. what is the best simple form it has (the author points to Chapter 8)?
- Over $\mathbf R$, which operators are diagonalizable, and does the answer change when the space has an inner product (the author points to the real spectral theorem 7.29)?
- Can Gershgorin disks be sharpened (e.g. using columns, Ex. 23, or a better choice of basis) to tell when an operator is invertible (Ex. 22)?

## Exercises worth doing
- 5C Ex. 3 (p. 161) — inverse of an invertible upper-triangular operator is upper triangular with diagonal $1/\lambda_k$ — difficulty: medium
- 5C Ex. 4–5 (p. 161) — examples showing 5.41 fails without triangularity (zero diagonal but invertible; nonzero diagonal but not invertible) — difficulty: easy
- 5D Ex. 15 (p. 173) — diagonalizability ⟺ $p$ and $p'$ have no common zero ⟺ gcd 1; decide without finding zeros — difficulty: hard
- 5D Ex. 21 (p. 174) — exact Fibonacci formula through diagonalization; golden ratio — difficulty: medium
- 5D Ex. 22 (p. 174) — strict diagonal dominance implies invertible (via Gershgorin) — difficulty: medium
- 5E Ex. 10 (p. 180) — real commuting operators for which 5.81 fails — difficulty: medium

## Reading notes
- This part begins at §5C (printed p. 154, "Upper-Triangular Matrices") and ends at the end of Exercises 5E (printed p. 180). It starts exactly at a section boundary; earlier results cited (5.11, 5.17–5.19, 5.22, 5.26–5.31, 4.13, 2.33–2.38, 3.21–3.43, 3.94, 1.45–1.46) are cited from earlier in the book and are not stated in these pages. Their statements are used as the author cites them.
- Page offset: printed = pdf − 14.
- The text layer showed math italic letters as garbled glyphs; all formulas were checked against the page images. No misprints noticed.
- Exercises are listed only; no solutions are printed in these pages.
- The remarks "(added step)" in the Gershgorin proof mark my two small clarifications ($c_j\ne0$; $|c_k/c_j|\le1$). Example 5.43's minimal polynomial and 5.61's "simple computation" are asserted by the author without displayed verification.
