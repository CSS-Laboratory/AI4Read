---
id: axler-2024-ladr/ch05-eigenvalues-p1
work: axler-2024-ladr
unit: "5 Eigenvalues and Eigenvectors (part 1/2): intro, 5A Invariant Subspaces, 5B The Minimal Polynomial"
pages: 132-153
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
audited: 2026-10-14
audit_fixes: 4
---
# Eigenvalues, Invariant Subspaces and the Minimal Polynomial (Axler, Ch. 5, Sections 5A–5B)

## L0 — One line
Studying an operator through subspaces it maps into themselves leads to eigenvectors, and polynomials applied to the operator show that every operator on a finite-dimensional nonzero complex space has an eigenvalue, and that on a finite-dimensional space the eigenvalues are exactly the zeros of a unique "minimal polynomial".

## L1 — The gist (≤ 120 words)
How can we understand an operator, a linear map from a space to itself? The chapter looks for subspaces the operator maps into themselves (invariant subspaces). The one-dimensional ones correspond to eigenvectors and eigenvalues. Powers and polynomials of an operator are then defined. With them the text proves that every operator on a finite-dimensional nonzero complex space has an eigenvalue. It also proves that every operator on a finite-dimensional space has a unique monic (leading coefficient 1) polynomial of least degree that kills it, the minimal polynomial. Its zeros are exactly the eigenvalues. Over the reals, odd dimension is enough to guarantee an eigenvalue. Finding exact eigenvalues is as hard as finding polynomial zeros.

**Prerequisites:** vector spaces over $\mathbf R$ or $\mathbf C$; linear maps, null space, range, injective/surjective; rank–nullity; linear independence and the linear dependence lemma; polynomials (division algorithm, fundamental theorem of algebra, factoring); direct sums.

## L2 — Key ideas (5–10 bullets)
- An operator is a linear map $V\to V$. A subspace $U$ is invariant if $T$ maps $U$ into $U$. Then $T|_U$ is itself an operator, so decomposing $V$ into invariant pieces reduces the problem (p. 133).
- One-dimensional invariant subspaces correspond exactly to eigenvectors, which satisfy $Tv=\lambda v$ with $v\ne 0$. So $V$ has such a subspace iff $T$ has an eigenvalue (pp. 134–135).
- In finite dimension, $\lambda$ is an eigenvalue iff $T-\lambda I$ is not injective, not surjective, not invertible. Eigenvectors for distinct eigenvalues are linearly independent. So there are at most $\dim V$ eigenvalues (pp. 135–136).
- Operators can be raised to powers, and a polynomial $p$ can be applied to $T$. Polynomials of the same $T$ commute and multiply as polynomials do (pp. 137–138). Null space and range of $p(T)$ are invariant under $T$ (p. 139).
- Every operator on a finite-dimensional nonzero complex space has an eigenvalue. The proof uses a minimal-degree polynomial killing a vector plus the fundamental theorem of algebra. It fails over $\mathbf R$ and in infinite dimension (p. 143).
- In finite dimension, a unique monic polynomial of least degree annihilates $T$ (the minimal polynomial), with degree $\le \dim V$. It can be computed by solving linear systems (pp. 144–146).
- The zeros of the minimal polynomial are exactly the eigenvalues. $q(T)=0$ iff $q$ is a polynomial multiple of the minimal polynomial. $T$ is invertible iff the constant term is nonzero (pp. 146–149).
- Exact eigenvalues cannot always be found by formula. Example 5.28 has minimal polynomial $3-6z+z^5$ (p. 147).
- On a real odd-dimensional space, every operator has an eigenvalue. Key lemma: $\dim\operatorname{null}(T^2+bT+cI)$ is even when $b^2<4c$ (pp. 149–150).

## L3 — Walkthrough

### Chapter introduction (p. 132)
Operators are linear maps from a space to itself. The chapter restricts operators to subspaces, which leads to invariant subspaces, then to eigenvectors and eigenvalues. It promises to prove that every operator on a finite-dimensional nonzero complex space has an eigenvalue. Standing assumptions: $\mathbf F$ is $\mathbf R$ or $\mathbf C$; $V$ is a vector space over $\mathbf F$ (p. 132).

### 5A Invariant Subspaces

**Definitions 5.1, 5.2 (p. 133).** An *operator* is a linear map from a vector space to itself; $\mathcal L(V)$ means $\mathcal L(V,V)$. Suppose $V=V_1\oplus\cdots\oplus V_m$ with each $V_k$ nonzero and $m\ge2$. Then $T$ is understood through the restrictions $T|_{V_k}$. But $T|_{V_k}$ may not map $V_k$ into itself, so it may not be an operator on $V_k$. So we consider only decompositions where $T$ maps each $V_k$ into itself. A subspace $U$ is *invariant under $T$* if $Tu\in U$ for every $u\in U$. Equivalently, $T|_U$ is an operator on $U$ (p. 133).

**Examples (p. 133).**
- 5.3: for $Tp=p'$ on $\mathcal P(\mathbf R)$, the subspace $\mathcal P_4(\mathbf R)$ is invariant, since the derivative of a degree $\le4$ polynomial has degree $\le4$.
- 5.4: for any $T$, the subspaces $\{0\}$, $V$, $\operatorname{null}T$ and $\operatorname{range}T$ are invariant. For null $T$: $u\in\operatorname{null}T$ gives $Tu=0\in\operatorname{null}T$.

**Rhetorical question (author's voice, p. 134).** The author asks whether an operator must have any invariant subspaces other than $\{0\}$ and $V$. The text's answer is yes, if $V$ is finite-dimensional with $\dim V>1$ ($\mathbf F=\mathbf C$) or $\dim V>2$ ($\mathbf F=\mathbf R$). This is promised for later (5.19 and Exercise 29 of 5B). $\operatorname{null}T$ and $\operatorname{range}T$ do not settle it, since null $T$ may be $\{0\}$ and range $T$ may be $V$ (when $T$ is invertible) (p. 134).

**One-dimensional invariant subspaces (p. 134).** Take $v\ne0$ and $U=\{\lambda v:\lambda\in\mathbf F\}=\operatorname{span}(v)$. Every one-dimensional subspace has this form. If $U$ is invariant, then $Tv\in U$, so $Tv=\lambda v$ for some $\lambda\in\mathbf F$. Conversely, if $Tv=\lambda v$, then $\operatorname{span}(v)$ is a one-dimensional invariant subspace (p. 134).

**Definition 5.5 (eigenvalue, p. 134).** $\lambda\in\mathbf F$ is an eigenvalue of $T$ if there exists $v\in V$ with $v\ne0$ and $Tv=\lambda v$. We require $v\neq 0$ because $T0=\lambda0$ for every $\lambda$. Hence $V$ has a one-dimensional $T$-invariant subspace iff $T$ has an eigenvalue (p. 134).

**Example 5.6 (p. 134).** $T(x,y,z)=(7x+3z,\;3x+6y+9z,\;-6y)$ on $\mathbf F^3$. Then $T(3,1,-1)=(18,6,-6)=6(3,1,-1)$, so 6 is an eigenvalue.

**Theorem 5.7 (p. 135).** Suppose $V$ is finite-dimensional, $T\in\mathcal L(V)$, $\lambda\in\mathbf F$. These are equivalent: (a) $\lambda$ is an eigenvalue of $T$; (b) $T-\lambda I$ is not injective; (c) $T-\lambda I$ is not surjective; (d) $T-\lambda I$ is not invertible. Proof: (a)⇔(b) because $Tv=\lambda v \iff (T-\lambda I)v=0$. (b), (c), (d) are equivalent by 3.65, a result cited from earlier in the book (p. 135). The text says this kind of equivalence holds only in finite dimension (p. 135).

*Intuition note.* An eigenvalue is a number $\lambda$ for which $T-\lambda I$ squashes some nonzero vector to 0. In finite dimension, squashing a vector and failing to be invertible are the same thing.

**Definition 5.8 (eigenvector, p. 135).** If $\lambda$ is an eigenvalue, $v$ is an eigenvector for $\lambda$ if $v\ne0$ and $Tv=\lambda v$. So a nonzero $v$ is an eigenvector for $\lambda$ iff $v\in\operatorname{null}(T-\lambda I)$ (p. 135).

**Example 5.9 (pp. 135–136).** $T(w,z)=(-z,w)$ on $\mathbf F^2$.
- (a) $\mathbf F=\mathbf R$: $T$ is a 90° counterclockwise rotation. No nonzero vector is rotated to a scalar multiple of itself, so $T$ has no eigenvalues.
- (b) $\mathbf F=\mathbf C$: $T(w,z)=\lambda(w,z)$ is equivalent to
$$-z=\lambda w,\qquad w=\lambda z. \tag{5.10}$$
Substituting $w=\lambda z$ into the first equation gives $-z=\lambda^2 z$. Here $z\ne0$, since $z=0$ would force $w=0$ by 5.10. So $-1=\lambda^2$, giving $\lambda=i$ or $\lambda=-i$. Eigenvectors for $i$ are $(w,-wi)$ and eigenvectors for $-i$ are $(w,wi)$, with $w\in\mathbf C$, $w\ne0$ (p. 136).

**Theorem 5.11 (p. 136).** For $T\in\mathcal L(V)$, every list of eigenvectors of $T$ for distinct eigenvalues is linearly independent.
Proof (by minimal counterexample). Suppose false. Let $m$ be the smallest positive integer such that some linearly dependent list $v_1,\dots,v_m$ of eigenvectors has distinct eigenvalues $\lambda_1,\dots,\lambda_m$. Then $m\ge2$, since eigenvectors are nonzero. There are $a_1,\dots,a_m$, none zero (by minimality), with $a_1v_1+\cdots+a_mv_m=0$. Apply $T-\lambda_mI$:
$$a_1(\lambda_1-\lambda_m)v_1+\cdots+a_{m-1}(\lambda_{m-1}-\lambda_m)v_{m-1}=0.$$
Since the eigenvalues are distinct, no coefficient is 0. So $v_1,\dots,v_{m-1}$ is a dependent list of $m-1$ such eigenvectors. This contradicts the minimality of $m$ (p. 136).

**Theorem 5.12 (p. 136).** If $V$ is finite-dimensional, each operator on $V$ has at most $\dim V$ distinct eigenvalues. Proof: eigenvectors for $m$ distinct eigenvalues are independent by 5.11, so $m\le\dim V$ (by 2.22) (p. 136).

*Intuition note.* Eigenvectors for different eigenvalues point in genuinely different directions. The space has only $\dim V$ independent directions, so it limits the number of eigenvalues.

#### Polynomials applied to operators (pp. 137–139)
Operators can be raised to powers, which is why operators have a richer theory than general linear maps (p. 137).

**Notation 5.13 (p. 137).** $T^m=T\cdots T$ ($m$ factors); $T^0=I$; if $T$ is invertible, $T^{-m}=(T^{-1})^m$. The text says to verify $T^mT^n=T^{m+n}$ and $(T^m)^n=T^{mn}$. The integers $m,n$ are arbitrary if $T$ is invertible and nonnegative otherwise (p. 137).

**Notation 5.14 (p. 137).** For $p(z)=a_0+a_1z+\cdots+a_mz^m$, define $p(T)=a_0I+a_1T+a_2T^2+\cdots+a_mT^m$. The constant term becomes $a_0I$ because $a_0=a_0z^0$ and $T^0=I$ (p. 137).

**Example 5.15 (p. 138).** $D$ is differentiation and $p(x)=7-3x+5x^2$. Then $p(D)=7I-3D+5D^2$, so $(p(D))q=7q-3q'+5q''$. The map $p\mapsto p(T)$ from $\mathcal P(\mathbf F)$ to $\mathcal L(V)$ is linear (to be verified by the reader) (p. 138).

**Definition 5.16 and Theorem 5.17 (p. 138).** $(pq)(z)=p(z)q(z)$. For $p,q\in\mathcal P(\mathbf F)$ and $T\in\mathcal L(V)$: (a) $(pq)(T)=p(T)q(T)$; (b) $p(T)q(T)=q(T)p(T)$.
Proof of (a). Write $p(z)=\sum_{j=0}^m a_jz^j$ and $q(z)=\sum_{k=0}^n b_kz^k$. Then $(pq)(z)=\sum_{j=0}^m\sum_{k=0}^n a_jb_kz^{j+k}$. So
$$(pq)(T)=\sum_{j=0}^m\sum_{k=0}^n a_jb_kT^{j+k}=\Big(\sum_{j=0}^m a_jT^j\Big)\Big(\sum_{k=0}^n b_kT^k\Big)=p(T)q(T).$$
Proof of (b): $p(T)q(T)=(pq)(T)=(qp)(T)=q(T)p(T)$ (p. 138).

**Theorem 5.18 (p. 139).** For $T\in\mathcal L(V)$ and $p\in\mathcal P(\mathbf F)$, $\operatorname{null}p(T)$ and $\operatorname{range}p(T)$ are invariant under $T$.
Proof. If $u\in\operatorname{null}p(T)$, then $(p(T))(Tu)=(p(T)T)(u)=(Tp(T))(u)=T(p(T)u)=T(0)=0$, so $Tu\in\operatorname{null}p(T)$. If $u=p(T)v\in\operatorname{range}p(T)$, then $Tu=T(p(T)v)=p(T)(Tv)\in\operatorname{range}p(T)$ (p. 139).

*Intuition note.* Because $T$ commutes with every polynomial in itself, $T$ cannot move a vector out of the null space or range of $p(T)$.

**Exercises 5A (pp. 139–142).** There are 43 exercises. Topics include invariant subspaces, eigenvalues of concrete operators, shift operators, quotient operators and polynomial identities. A selection is listed under "Exercises worth doing".

### 5B The Minimal Polynomial

#### Existence of eigenvalues on complex spaces (p. 143)
**Theorem 5.19.** Every operator on a finite-dimensional nonzero complex vector space has an eigenvalue.
Proof. Let $\dim V=n>0$ and pick $v\ne0$. The $n+1$ vectors $v,Tv,T^2v,\dots,T^nv$ are linearly dependent. So some nontrivial combination equals 0, and there is a nonconstant polynomial $p$ of smallest degree with $p(T)v=0$. By the fundamental theorem of algebra (4.12) there is $\lambda\in\mathbf C$ with $p(\lambda)=0$. So $p(z)=(z-\lambda)q(z)$ for some $q$ (by 4.6). By 5.17,
$$0=p(T)v=(T-\lambda I)(q(T)v).$$
Since $\deg q<\deg p$, minimality gives $q(T)v\ne0$. Hence $\lambda$ is an eigenvalue with eigenvector $q(T)v$ (p. 143).

The hypothesis $\mathbf F=\mathbf C$ cannot be replaced by $\mathbf R$ (Example 5.9). The finite-dimensional hypothesis cannot be dropped either. **Example 5.20:** $(Tp)(z)=zp(z)$ on $\mathcal P(\mathbf C)$. For nonzero $p$, $\deg Tp=\deg p+1$, so $Tp$ is never a scalar multiple of $p$. $T$ has no eigenvalues, and $\mathcal P(\mathbf C)$ is infinite-dimensional (p. 143).

*Intuition note.* Over $\mathbf C$, any polynomial that kills a vector has a root, and a root gives a factor $(T-\lambda I)$ that kills something nonzero. Over $\mathbf R$ roots may be missing, and in infinite dimension the first step (a dependent list) fails.

#### Eigenvalues and the minimal polynomial (pp. 144–149)
**Definition 5.21 (p. 144).** A *monic polynomial* has highest-degree coefficient 1 (e.g. $2+9z^2+z^7$ has degree 7).

**Theorem 5.22 (pp. 144–145).** If $V$ is finite-dimensional and $T\in\mathcal L(V)$, there is a unique monic $p\in\mathcal P(\mathbf F)$ of smallest degree with $p(T)=0$, and $\deg p\le\dim V$.

Proof, existence. If $\dim V=0$, take $p=1$. Otherwise use induction on $\dim V$ (hypothesis: true for all smaller dimensions).
1. Take $u\ne0$. The list $u,Tu,\dots,T^{\dim V}u$ has length $1+\dim V$, so it is dependent. By the linear dependence lemma (2.19) there is a smallest positive $m\le\dim V$ with $T^mu$ a combination of $u,\dots,T^{m-1}u$:
$$c_0u+c_1Tu+\cdots+c_{m-1}T^{m-1}u+T^mu=0. \tag{5.23}$$
2. Let $q(z)=c_0+c_1z+\cdots+c_{m-1}z^{m-1}+z^m$. Then $q(T)u=0$. For $k\ge0$, $q(T)(T^ku)=T^k(q(T)u)=0$.
3. By 2.19, $u,\dots,T^{m-1}u$ are independent and lie in $\operatorname{null}q(T)$. So $\dim\operatorname{null}q(T)\ge m$ and
$$\dim\operatorname{range}q(T)=\dim V-\dim\operatorname{null}q(T)\le\dim V-m.$$
4. $\operatorname{range}q(T)$ is invariant under $T$ (5.18). The induction hypothesis applied to $T|_{\operatorname{range}q(T)}$ gives a monic $s$ with $\deg s\le\dim V-m$ and $s(T|_{\operatorname{range}q(T)})=0$.
5. For all $v\in V$: $((sq)(T))(v)=s(T)(q(T)v)=0$, because $q(T)v\in\operatorname{range}q(T)$. So $sq$ is monic, $\deg sq\le\dim V$, and $(sq)(T)=0$. Hence a monic polynomial of smallest degree killing $T$ exists, with degree $\le\dim V$.

Proof, uniqueness. Let $p$ be monic of smallest degree with $p(T)=0$, and let $r$ be another such polynomial of the same degree. Then $(p-r)(T)=0$ and $\deg(p-r)<\deg p$. If $p-r\ne0$, dividing by its leading coefficient gives a monic polynomial of smaller degree killing $T$, a contradiction. So $p=r$ (p. 145).

**Definition 5.24 (p. 145).** The *minimal polynomial* of $T$ is the unique monic polynomial of smallest degree with $p(T)=0$.

**Computing it (p. 145).** Find the smallest positive $m$ such that
$$c_0I+c_1T+\cdots+c_{m-1}T^{m-1}=-T^m$$
has a solution. In a basis, this is a system of $(\dim V)^2$ linear equations (each $T^k$ is a $\dim V\times\dim V$ matrix) in the $m$ unknowns $c_0,\dots,c_{m-1}$. Test $m=1,2,\dots$. By 5.22 a solution exists for some $m\le\dim V$. The faster method (usually) picks $v\ne0$ and solves
$$c_0v+c_1Tv+\cdots+c_{\dim V-1}T^{\dim V-1}v=-T^{\dim V}v, \tag{5.25}$$
a system of $\dim V$ equations in $\dim V$ unknowns. If the solution is unique (the usual case), then $c_0,\dots,c_{\dim V-1},1$ are the coefficients of the minimal polynomial. With $v=(1,0,0,0)$ on $\mathbf R^4$ this works on over 99.8% of 4×4 integer matrices with entries in $[-10,10]$, and over 99.999% with entries in $[-100,100]$. The text says these figures come from testing millions of random matrices (p. 145).

**Example 5.26 (p. 146).** $T\in\mathcal L(\mathbf F^5)$ with the $5\times5$ matrix (standard basis)
$$\mathcal M(T)=\begin{pmatrix}0&0&0&0&-3\\1&0&0&0&6\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\end{pmatrix}.$$
Take $v=e_1$. Then $Te_1=e_2$, $T^2e_1=e_3$, $T^3e_1=e_4$, $T^4e_1=e_5$, $T^5e_1=Te_5=-3e_1+6e_2$. So $3e_1-6Te_1=-T^5e_1$. The list $e_1,Te_1,\dots,T^4e_1$ equals $e_1,\dots,e_5$, which is independent, so no other combination works. The minimal polynomial is $3-6z+z^5$ (p. 146).

**Theorem 5.27 (pp. 146–147).** Let $V$ be finite-dimensional, $T\in\mathcal L(V)$, $p$ its minimal polynomial. (a) The zeros of $p$ are the eigenvalues of $T$ (zeros and eigenvalues taken in $\mathbf F$). (b) If $V$ is complex, $p(z)=(z-\lambda_1)\cdots(z-\lambda_m)$, where $\lambda_1,\dots,\lambda_m$ lists all eigenvalues, possibly with repetitions.
Proof of (a). (i) Let $\lambda\in\mathbf F$ with $p(\lambda)=0$. Then $p(z)=(z-\lambda)q(z)$ with $q$ monic (4.6), and $0=(T-\lambda I)(q(T)v)$ for all $v$. Since $\deg q=\deg p-1$, some $v$ has $q(T)v\ne0$, so $\lambda$ is an eigenvalue. (ii) Let $\lambda$ be an eigenvalue with $Tv=\lambda v$, $v\ne0$. Repeated application gives $T^kv=\lambda^kv$, so $p(T)v=p(\lambda)v$. Since $p(T)v=0$ and $v\ne0$, $p(\lambda)=0$.
(b) follows from (a) and the second version of the fundamental theorem of algebra (4.13) (pp. 146–147).

Consequences (p. 147). A nonzero polynomial has at most as many distinct zeros as its degree (4.8). With 5.27(a) and $\deg p\le\dim V$, this gives another proof of 5.12. By Exercise 16, every monic polynomial is the minimal polynomial of some operator. So finding exact eigenvalues is equivalent to finding exact zeros of polynomials, which is not possible in general (p. 147).

**Example 5.28 (p. 147).** The operator $T(z_1,\dots,z_5)=(-3z_5,\,z_1+6z_5,\,z_2,\,z_3,\,z_4)$ on $\mathbf C^5$ has the matrix of 5.26 and minimal polynomial $3-6z+z^5$. The text says no zero of it can be expressed with rational numbers, roots of rational numbers and the usual rules of arithmetic (the proof lies beyond linear algebra). By 5.27(a), the eigenvalues have no exact familiar expression. Numerically they are about $-1.67,\ 0.51,\ 1.40,\ -0.12\pm1.59i$. The two nonreal ones are conjugates, as expected for real coefficients (4.14) (p. 147).

**Theorem 5.29 (p. 148).** For finite-dimensional $V$, $T\in\mathcal L(V)$, $q\in\mathcal P(\mathbf F)$: $q(T)=0$ iff $q$ is a polynomial multiple of the minimal polynomial $p$.
Proof. (⇒) By the division algorithm (4.9), $q=ps+r$ with $\deg r<\deg p$. Then $0=q(T)=p(T)s(T)+r(T)=r(T)$. If $r\ne0$, dividing by its leading coefficient would give a monic polynomial of smaller degree than $p$ killing $T$, a contradiction. So $r=0$ and $q=ps$. (⇐) If $q=ps$, then $q(T)=p(T)s(T)=0\cdot s(T)=0$ (p. 148).

**Theorem 5.31 (p. 148).** Suppose $V$ is finite-dimensional. If $U$ is invariant under $T$, the minimal polynomial of $T$ is a polynomial multiple of the minimal polynomial of $T|_U$. Proof: with $p$ the minimal polynomial of $T$, $p(T)u=0$ for all $u\in U$, so $p(T|_U)=0$; apply 5.29 to $T|_U$ (p. 148). Exercise 25 gives an analogue for quotient operators (p. 148).

**Theorem 5.32 (p. 149).** Suppose $V$ is finite-dimensional. Then $T$ is not invertible iff the constant term of its minimal polynomial $p$ is 0. Proof: not invertible ⇔ 0 is an eigenvalue (5.7) ⇔ 0 is a zero of $p$ (5.27(a)) ⇔ $p(0)=0$, i.e. the constant term is 0 (p. 149).

*Intuition note.* The minimal polynomial is the shortest "recipe" in powers of $T$ that gives the zero map. Its roots are exactly the eigenvalues, so it packages all eigenvalue information, and its constant term tests invertibility.

#### Eigenvalues on odd-dimensional real vector spaces (pp. 149–150)
**Theorem 5.33 (p. 149).** Suppose $\mathbf F=\mathbf R$, $V$ is finite-dimensional, $T\in\mathcal L(V)$, $b,c\in\mathbf R$, $b^2<4c$. Then $\dim\operatorname{null}(T^2+bT+cI)$ is even.
Proof.
1. $\operatorname{null}(T^2+bT+cI)$ is invariant under $T$ (5.18). Replacing $V$ by it and $T$ by the restriction, assume $T^2+bT+cI=0$; we must show $\dim V$ is even.
2. $T$ has no eigenvector. If $Tv=\lambda v$ with $\lambda\in\mathbf R$, then
$$0=(T^2+bT+cI)v=(\lambda^2+b\lambda+c)v=\Big(\big(\lambda+\tfrac b2\big)^2+c-\tfrac{b^2}{4}\Big)v,$$
and the bracket is positive, so $v=0$.
3. Let $U$ be an invariant subspace of largest even dimension among invariant subspaces of even dimension. If $U=V$ we are done. Otherwise pick $w\notin U$ and set $W=\operatorname{span}(w,Tw)$. $W$ is invariant, since $T(Tw)=-bTw-cw$. $\dim W=2$, since otherwise $w$ would be an eigenvector.
4. $U\cap W=\{0\}$, since otherwise it would be a one-dimensional invariant subspace, impossible without eigenvectors. So $\dim(U+W)=\dim U+\dim W-\dim(U\cap W)=\dim U+2$. $U+W$ is invariant of larger even dimension, a contradiction. So $U=V$ and $\dim V$ is even (p. 149).

**Theorem 5.34 (p. 150).** Every operator on an odd-dimensional vector space has an eigenvalue.
Proof. The complex case is already known (5.19), so assume $\mathbf F=\mathbf R$, $n=\dim V$ odd. Use induction on $n$ in steps of two.
1. Base: if $\dim V=1$, every nonzero vector is an eigenvector.
2. Step: let $n\ge3$ and assume the result for smaller odd dimensions. Let $p$ be the minimal polynomial of $T$. If $p$ is a multiple of $x-\lambda$ for some real $\lambda$, then $\lambda$ is an eigenvalue by 5.27(a). Otherwise $p$ is a multiple of $x^2+bx+c$ with $b^2<4c$ (4.16).
3. Write $p(x)=q(x)(x^2+bx+c)$ with $q$ monic. Then $0=p(T)=q(T)(T^2+bT+cI)$, so $q(T)=0$ on $\operatorname{range}(T^2+bT+cI)$. Since $\deg q<\deg p$ and $p$ is minimal, $\operatorname{range}(T^2+bT+cI)\ne V$.
4. By the fundamental theorem of linear maps (3.21),
$$\dim V=\dim\operatorname{null}(T^2+bT+cI)+\dim\operatorname{range}(T^2+bT+cI).$$
$\dim V$ is odd and the null space dimension is even (5.33), so the range has odd dimension. The range is invariant under $T$ (5.18) and has odd dimension less than $\dim V$.
5. By the induction hypothesis, $T$ restricted to the range has an eigenvalue, hence so does $T$ (p. 150).

*Intuition note.* On the null space of $T^2+bT+cI$ (with $b^2<4c$) there are no eigenvectors, and the proof builds that space from 2-dimensional invariant pieces $\operatorname{span}(w,Tw)$, so its dimension is even. In an odd-dimensional space the range of $T^2+bT+cI$ therefore has odd dimension, which lets the induction go down.

**Exercises 5B (pp. 150–153).** There are 29 exercises. Topics include the eigenvalues of $p(T)$, $ST$ versus $TS$, the companion matrix (Ex. 16), the minimal polynomial of shifts and scalings of $T$, complexification, duals and quotient operators. A selection is listed below.

## Toy example (ours, not from the text)
Operator $T$ on $\mathbf R^2$ with $Te_1=e_2$ and $Te_2=-2e_1+3e_2$. Matrix with columns $(0,1)$ and $(-2,3)$, i.e. $\begin{pmatrix}0&-2\\1&3\end{pmatrix}$.
- Take $v=e_1$ in the style of 5.25. $Tv=e_2$ and $T^2v=Te_2=-2e_1+3e_2$. The list $v,Tv$ is independent, since $e_1,e_2$ is a basis, so no degree-1 polynomial kills $v$.
- Solve $c_0v+c_1Tv=-T^2v$: $c_0e_1+c_1e_2=2e_1-3e_2$, so $c_0=2$, $c_1=-3$. Minimal polynomial $p(z)=2-3z+z^2=(z-1)(z-2)$. It has degree $2=\dim V$ and is monic, as 5.22 allows.
- By 5.27(a), the eigenvalues are 1 and 2. Check: $T(x,y)=x\,e_2+y(-2e_1+3e_2)=(-2y,\;x+3y)$. For $(x,y)=(-2,1)$: $T=(-2,\,-2+3)=(-2,1)=1\cdot(-2,1)$ ✓. For $(-1,1)$: $T=(-2,\,-1+3)=(-2,2)=2\cdot(-1,1)$ ✓.
- The two eigenvectors are independent, as 5.11 predicts, and there are $2\le\dim V$ distinct eigenvalues, as 5.12 predicts.
- Constant term $2\ne0$, so $T$ is invertible (5.32).

## Concepts
- [[operator]] (new) — linear map from a vector space to itself, $\mathcal L(V)=\mathcal L(V,V)$ (p. 133)
- [[invariant-subspace]] (new) — subspace $U$ with $Tu\in U$ for all $u\in U$; then $T|_U$ is an operator (p. 133)
- [[eigenvector-eigenvalue]] — nonzero $v$ with $Tv=\lambda v$; $\lambda$ is the eigenvalue; same as the canon meaning, defined for operators on any $\mathbf F$ (pp. 134–135)
- [[null-space]] — the kernel; here eigenvectors for $\lambda$ are the nonzero elements of $\operatorname{null}(T-\lambda I)$ (p. 135)
- [[polynomial-of-an-operator]] (new) — $p(T)=a_0I+a_1T+\cdots+a_mT^m$; polynomials in one $T$ multiply and commute (pp. 137–138)
- [[monic-polynomial]] (new) — polynomial whose leading coefficient is 1 (p. 144)
- [[minimal-polynomial]] (new) — unique monic polynomial of least degree with $p(T)=0$; degree $\le\dim V$; its zeros are the eigenvalues (pp. 144–146)
- [[rank-nullity]] — used as the fundamental theorem of linear maps (3.21) in 5.34 (p. 150)
- [[linear-independence]] — used to bound the number of eigenvalues and to build the minimal polynomial (pp. 136, 144)

## Canonical instances
- [[rotation-90-eigenvalues]] — the map $(w,z)\mapsto(-z,w)$ has no eigenvalues over $\mathbf R$, and has $\pm i$ over $\mathbf C$ (pp. 135–136)
- [[differentiation-operator]] — $\mathcal P_4(\mathbf R)$ invariant; $p(D)q=7q-3q'+5q''$ (pp. 133, 138)
- [[multiplication-by-z-no-eigenvalues]] — $(Tp)(z)=zp(z)$ on $\mathcal P(\mathbf C)$, no eigenvalues, infinite-dimensional (p. 143)
- [[companion-style-matrix-5x5]] — minimal polynomial $3-6z+z^5$ (Examples 5.26, 5.28) (pp. 146–147)
- [[unsolvable-eigenvalues-example]] — eigenvalues with no exact familiar expression (p. 147)

## Bridges (candidates)
- [structural-analogy] eigenvalues as zeros of the minimal polynomial ↔ linear-algebra canon: roots of the characteristic polynomial $\det(A-\lambda I)$ — both are polynomials annihilating $T$ whose roots are the eigenvalues; the characteristic polynomial is not in this unit.
- [structural-analogy] splitting $V=V_1\oplus\cdots\oplus V_m$ into invariant pieces ↔ diagonalization: in an eigenbasis the map acts independently on each direction (canon link; not stated in this unit).
- [same-math] $v,Tv,T^2v,\dots$ dependent ⇒ polynomial kills $v$ ↔ Krylov subspaces: the span of $v,Tv,\dots,T^{k-1}v$ (Ex. 5B.23 says this span is invariant when $k=\dim V$).
- [metaphor] "exact eigenvalues are as hard as polynomial roots" ↔ numerical linear algebra: eigenvalues are found by iterative approximation, not formulas.

## Questions this raises
- How can a well-chosen basis make an operator's matrix simple? The chapter intro promises, for each operator on a finite-dimensional complex space, a basis in which at least almost half the matrix entries are 0 (p. 132).
- How does the minimal polynomial relate to the repeated eigenvalues and to the exponent of each factor $(z-\lambda_j)$?
- Why does every operator on a finite-dimensional space of dimension at least two have an invariant subspace of dimension two (Ex. 5B.29), and what does it say about real operators without eigenvalues?
- How do numerical methods actually approximate eigenvalues, given there is no general formula?

## Exercises worth doing
- Ex. 5A.8 (p. 139) — an operator with $P^2=P$ can only have eigenvalues 0 or 1; practice with polynomial identities and eigenvectors — difficulty: easy
- Ex. 5A.13 (p. 140) — similar operators $S^{-1}TS$ and $T$ have the same eigenvalues, and how their eigenvectors relate; change of basis idea — difficulty: medium
- Ex. 5A.23 (p. 141) — $ST$ and $TS$ have the same eigenvalues — difficulty: medium
- Ex. 5B.4 (p. 151) — eigenvalues of $p(T)$ over $\mathbf C$ are $p(\lambda)$; combines 5.27 and polynomial factoring — difficulty: medium
- Ex. 5B.8 (p. 151) — find the minimal polynomial of the 1° rotation of $\mathbf R^2$ (the book prints a hint); tests understanding of 5.22 — difficulty: medium
- Ex. 5B.16 (p. 152) — companion matrix: every monic polynomial is a minimal polynomial; ties to 5.26–5.28 — difficulty: hard

## Reading notes
- This part starts at the chapter opening (printed p. 132) and ends with Exercises 5B (printed p. 153). It covers Sections 5A and 5B. The chapter continues in the next part (these pages refer to Sections 5C and 5D).
- Page offset: printed = pdf − 14.
- The text layer shows math symbols as garbled characters. I read all equations from the page images.
- On printed p. 141 the page header in the image shows "≈ 100√2" where the page number would be. I cite it as p. 141, following the page label.
- Several proofs here (for example 5.7, 5.12, 5.19, 5.22, 5.34) cite earlier results (2.19, 2.22, 3.21, 3.65, 4.6, 4.8, 4.9, 4.12, 4.13, 4.14, 4.16). Those results are not in this unit; I name them only as cited by the author.
