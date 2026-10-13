---
id: axler-2024-ladr/ch07-operators-p3
work: axler-2024-ladr
unit: "7 Operators on Inner Product Spaces (part 3/3): 7E Singular Value Decomposition and 7F Consequences of Singular Value Decomposition"
pages: 270–296
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
# Singular Value Decomposition and Its Consequences (Axler, §7E–7F)

## L0 — One line
Every linear map between inner product spaces acts by stretching along one orthonormal list by the singular values $s_k$ and landing on another orthonormal list (the SVD); this leads to norms, best approximations by maps of lower-dimensional range, the polar decomposition (for operators), and volume change (for invertible operators on real spaces).

## L1 — The gist (≤ 120 words)
Eigenvalues are defined only for maps from a space to itself, and (as in Example 7.66) can miss part of how a map stretches. This unit defines singular values (square roots of eigenvalues of $T^*T$) for any linear map between inner product spaces. Main results: every such map has the form $Tv=\sum s_k\langle v,e_k\rangle f_k$ with two orthonormal lists (SVD). Consequences: the norm of $T$ is the largest singular value; truncating the SVD gives the best lower-rank approximation (in the operator norm), with error $s_{k+1}$; every operator is a unitary times $\sqrt{T^*T}$; an invertible operator maps the unit ball to an ellipsoid and (for real spaces) multiplies volume by the product of singular values.

**Prerequisites:** adjoint $T^*$; positive and self-adjoint operators; spectral theorem; orthonormal lists and Bessel's inequality; unitary operators and isometries; null space and range; pseudoinverse (as defined earlier in the book).

## L2 — Key ideas
- **Singular values** of $T\in\mathcal L(V,W)$ are the nonnegative square roots of the eigenvalues of the positive operator $T^*T$, listed in decreasing order with multiplicity. Unlike eigenvalues, they exist for maps between different spaces. Example 7.66 shows they can detect stretching that eigenvalues miss (p. 271).
- The number of positive singular values equals $\dim\operatorname{range}T$. $T$ is injective iff $0$ is not a singular value. $T$ is an isometry iff all singular values equal 1 (p. 272).
- **SVD (7.70):** there are orthonormal lists $e_1,\dots,e_m$ in $V$ and $f_1,\dots,f_m$ in $W$ with $Tv=\sum_k s_k\langle v,e_k\rangle f_k$. So every linear map has a (rectangular) diagonal matrix in suitable orthonormal bases (pp. 273–274).
- Swapping the roles of the $e$'s and $f$'s gives the adjoint. Swapping them and inverting each $s_k$ gives the pseudoinverse (p. 275). The matrix form is $A=BDC^*$, which can need far fewer stored entries than $A$ (p. 277).
- The norm of a linear map, $\|T\|=\max\{\|Tv\|:\|v\|\le1\}$, equals the largest singular value. It satisfies $\|Tv\|\le\|T\|\|v\|$ and $\|T^*\|=\|T\|$ (pp. 280–283).
- **Best approximation (7.92):** among maps with range of dimension $\le k$, a closest map to $T$ is the truncated SVD $T_k$, at distance exactly $s_{k+1}$ (for $1\le k<m$, where $m$ is the number of positive singular values) (p. 284).
- **Polar decomposition (7.93):** every operator is $T=S\sqrt{T^*T}$ with $S$ unitary (p. 286).
- An invertible operator maps the unit ball onto an ellipsoid (a stretched ball) whose principal axes $s_kf_k$ come from the SVD. It maps ellipsoids to ellipsoids and parallelepipeds to parallelepipeds, and some boxes to boxes (pp. 288–291).
- For $\mathbf F=\mathbf R$, an invertible $T$ multiplies volume by the product of its singular values, which the author says equals $|\det T|$ (a forward reference) (p. 293).

## L3 — Walkthrough

Throughout, $V,W$ are inner product spaces and $\mathbf F$ is $\mathbf R$ or $\mathbf C$.

### 7E. Singular Value Decomposition

#### Singular values

**7.64 (properties of $T^*T$).** Let $T\in\mathcal L(V,W)$. Then (a) $T^*T$ is a positive operator on $V$; (b) $\operatorname{null}T^*T=\operatorname{null}T$; (c) $\operatorname{range}T^*T=\operatorname{range}T^*$; (d) $\dim\operatorname{range}T=\dim\operatorname{range}T^*=\dim\operatorname{range}T^*T$ (p. 270).

Proof steps (p. 270):
- (a) $(T^*T)^*=T^*(T^*)^*=T^*T$, so it is self-adjoint. For $v\in V$: $\langle (T^*T)v,v\rangle=\langle T^*(Tv),v\rangle=\langle Tv,Tv\rangle=\|Tv\|^2\ge0$.
- (b) If $v\in\operatorname{null}T^*T$, then $\|Tv\|^2=\langle Tv,Tv\rangle=\langle T^*Tv,v\rangle=\langle0,v\rangle=0$, so $Tv=0$. Conversely $Tv=0$ gives $T^*Tv=0$.
- (c) Because $T^*T$ is self-adjoint, $\operatorname{range}T^*T=(\operatorname{null}T^*T)^\perp=(\operatorname{null}T)^\perp=\operatorname{range}T^*$, using 7.6 and (b).
- (d) $\dim\operatorname{range}T=\dim(\operatorname{null}T^*)^\perp=\dim W-\dim\operatorname{null}T^*=\dim\operatorname{range}T^*$, using 7.6(d), 6.51 and the fundamental theorem of linear maps (3.21). The last equality follows from (c).

*Intuition note.* $T^*T$ measures lengths of $Tv$ ($\langle T^*Tv,v\rangle=\|Tv\|^2$). So $\langle T^*Tv,v\rangle$ is never negative, and $T^*T$ kills exactly the vectors that $T$ kills.

**7.65 Definition (singular values).** The singular values of $T\in\mathcal L(V,W)$ are the nonnegative square roots of the eigenvalues of $T^*T$, listed in decreasing order, each repeated as often as the dimension of the corresponding eigenspace of $T^*T$ (p. 271).

**7.66 Example (p. 271).** $T(z_1,z_2,z_3,z_4)=(0,3z_1,2z_2,-3z_4)$ on $\mathbf F^4$. Then
$$T^*T(z_1,z_2,z_3,z_4)=(9z_1,4z_2,0,9z_4).$$
The eigenvalues of $T^*T$ are 9, 4, 0, with eigenspace dimensions $2,1,1$. So the singular values are $3,3,2,0$. The only eigenvalues of $T$ are $-3$ and $0$; the number 2 appears only among the singular values.

**7.67 Example (p. 271).** $T\in\mathcal L(\mathbf F^4,\mathbf F^3)$ has matrix $\begin{pmatrix}0&0&0&-5\\0&0&0&0\\1&1&0&0\end{pmatrix}$. The matrix of $T^*T$ is $\begin{pmatrix}1&1&0&0\\1&1&0&0\\0&0&0&0\\0&0&0&25\end{pmatrix}$. Its eigenvalues are $25,2,0$ with eigenspace dimensions $1,1,2$. The singular values are $5,\sqrt2,0,0$.

**7.68 (role of positive singular values).** For $T\in\mathcal L(V,W)$ (p. 272):
- (a) $T$ injective $\iff$ $0$ is not a singular value.
- (b) The number of positive singular values equals $\dim\operatorname{range}T$.
- (c) $T$ surjective $\iff$ the number of positive singular values equals $\dim W$.

Proof (p. 272). (a) $T$ injective $\iff\operatorname{null}T=\{0\}\iff\operatorname{null}T^*T=\{0\}$ [7.64(b)] $\iff0$ is not an eigenvalue of $T^*T\iff0$ is not a singular value. (b) By the spectral theorem, $\dim\operatorname{range}T^*T$ equals the number of positive eigenvalues of $T^*T$ (with repetition). By 7.64(d) this is $\dim\operatorname{range}T$. (c) The author says to use (b) and 2.39.

The author's comparison table (p. 272): eigenvalues are defined only for maps from a vector space to itself. Singular values are defined for maps between possibly different inner product spaces and are nonnegative. The list of singular values has length $\dim V$, and it includes 0 iff the map is not injective. Singular values are always sorted in decreasing order. Eigenvalues need not be nonnegative, can form an empty list when $\mathbf F=\mathbf R$, include 0 iff the operator is not invertible, and have no standard order.

**7.69 (isometries).** $S\in\mathcal L(V,W)$ is an isometry $\iff$ all singular values of $S$ equal 1. Proof: $S$ isometry $\iff S^*S=I$ (7.49) $\iff$ all eigenvalues of the self-adjoint $S^*S$ equal 1 (spectral theorem) $\iff$ all singular values equal 1 (p. 272).

#### SVD for linear maps and for matrices

**7.70 (singular value decomposition).** Suppose $T\in\mathcal L(V,W)$ has positive singular values $s_1,\dots,s_m$. Then there exist orthonormal lists $e_1,\dots,e_m$ in $V$ and $f_1,\dots,f_m$ in $W$ such that
$$Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m\tag{7.71}$$
for every $v\in V$ (p. 273).

Proof (p. 273). Let $s_1,\dots,s_n$ be all singular values ($n=\dim V$).
1. $T^*T$ is positive (7.64(a)), so the spectral theorem gives an orthonormal basis $e_1,\dots,e_n$ of $V$ with $T^*Te_k=s_k^2e_k$ (7.72).
2. For $k=1,\dots,m$ put $f_k=Te_k/s_k$ (7.73).
3. For $j,k\le m$: $\langle f_j,f_k\rangle=\frac1{s_js_k}\langle Te_j,Te_k\rangle=\frac1{s_js_k}\langle e_j,T^*Te_k\rangle=\frac{s_k}{s_j}\langle e_j,e_k\rangle$. This is 0 if $j\ne k$ and 1 if $j=k$, so $f_1,\dots,f_m$ is orthonormal.
4. If $k>m$ then $s_k=0$, so $T^*Te_k=0$, so $Te_k=0$ by 7.64(b).
5. For $v\in V$: $Tv=T(\sum_{k\le n}\langle v,e_k\rangle e_k)=\sum_{k\le m}\langle v,e_k\rangle Te_k=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$. The sum stops at $m$ by step 4, and the last equality uses 7.73.

*Intuition note.* $V$ has special perpendicular directions $e_k$. $T$ sends them to perpendicular directions $f_k$ in $W$ and stretches by $s_k$. Directions with $s_k=0$ are sent to 0.

**Matrix form (pp. 273–274).** Extend $e_1,\dots,e_m$ to an orthonormal basis $e_1,\dots,e_{\dim V}$ of $V$, and $f_1,\dots,f_m$ to one of $W$. Then $Te_k=s_kf_k$ for $1\le k\le m$ and $Te_k=0$ for $m<k\le\dim V$. So the matrix has entries
$$\mathcal M\big(T,(e_1,\dots,e_{\dim V}),(f_1,\dots,f_{\dim W})\big)_{j,k}=\begin{cases}s_k&1\le j=k\le m\\0&\text{otherwise.}\end{cases}$$

**7.74 Definition (diagonal matrix).** An $M$-by-$N$ matrix $A$ is diagonal if all entries are 0 except possibly $A_{k,k}$ for $k=1,\dots,\min\{M,N\}$ (p. 274). So every linear map $V\to W$ has a diagonal matrix in suitable orthonormal bases.

Author's comparison with the spectral theorem (p. 274): the spectral theorem covers only self-adjoint ($\mathbf F=\mathbf R$) or normal ($\mathbf F=\mathbf C$) operators and gives one orthonormal basis. Its proof differs for $\mathbf R$ and $\mathbf C$. The SVD covers arbitrary linear maps between possibly different spaces and gives two orthonormal lists, not necessarily equal even when $W=V$. The same proof works for both fields.

**7.75 (adjoint and pseudoinverse from the SVD).** Suppose $Tv=s_1\langle v,e_1\rangle f_1+\cdots+s_m\langle v,e_m\rangle f_m$ (7.76) with orthonormal lists as in 7.70. Then for every $w\in W$ (p. 275):
$$T^*w=s_1\langle w,f_1\rangle e_1+\cdots+s_m\langle w,f_m\rangle e_m,\tag{7.77}$$
$$T^\dagger w=\frac{\langle w,f_1\rangle}{s_1}e_1+\cdots+\frac{\langle w,f_m\rangle}{s_m}e_m.\tag{7.78}$$

Proof (p. 275).
- *Adjoint.* $\langle Tv,w\rangle=\sum s_k\langle v,e_k\rangle\langle f_k,w\rangle=\langle v,\sum s_k\langle w,f_k\rangle e_k\rangle$. This gives 7.77.
- *Pseudoinverse.* Let $v=\sum\frac{\langle w,f_k\rangle}{s_k}e_k$. Since 7.76 gives $Te_k=s_kf_k$, we get $Tv=\sum\langle w,f_k\rangle f_k$. By 7.76, $f_1,\dots,f_m$ spans $\operatorname{range}T$, so it is an orthonormal basis of $\operatorname{range}T$, and 6.57(i) gives $Tv=P_{\operatorname{range}T}w$. Also $v\in(\operatorname{null}T)^\perp$ (Exercise 8(b)). The definition of $T^\dagger w$ (6.68, not restated here) then shows $v=T^\dagger w$.

The author recalls that $T^\dagger=T^{-1}$ when $T$ is invertible [6.69(a)] (p. 275).

**7.79 Example (p. 276).** Take $T(x_1,x_2,x_3,x_4)=(-5x_4,0,x_1+x_2)$. By Example 7.67, the positive eigenvalues of $T^*T$ are 25 and 2, each with a one-dimensional eigenspace, so $s_1=5$, $s_2=\sqrt2$. Orthonormal eigenvectors: $e_1=(0,0,0,1)$ for 25 and $e_2=(\tfrac1{\sqrt2},\tfrac1{\sqrt2},0,0)$ for 2. Then $f_1=Te_1/5=(-1,0,0)$ and $f_2=Te_2/\sqrt2=(0,0,1)$. So $Tv=5\langle v,e_1\rangle f_1+\sqrt2\langle v,e_2\rangle f_2$ for all $v\in\mathbf F^4$.

**7.80 (matrix version of SVD).** Suppose $A$ is a $p$-by-$n$ matrix of rank $m\ge1$. Then there exist a $p$-by-$m$ matrix $B$ with orthonormal columns, an $m$-by-$m$ diagonal matrix $D$ with positive diagonal entries, and an $n$-by-$m$ matrix $C$ with orthonormal columns such that
$$A=BDC^*.$$
("Orthonormal" means for the standard Euclidean inner product.) (pp. 276–277)

Proof (p. 277).
1. Let $T:\mathbf F^n\to\mathbf F^p$ have matrix $A$ in the standard bases. Then $\dim\operatorname{range}T=m$ (3.78). Take an SVD $Tv=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$ (7.81).
2. Let $B$ have columns $f_1,\dots,f_m$ ($p\times m$), $D=\operatorname{diag}(s_1,\dots,s_m)$ ($m\times m$), and $C$ have columns $e_1,\dots,e_m$ ($n\times m$).
3. With $u_1,\dots,u_m$ the standard basis of $\mathbf F^m$: $(AC-BD)u_k=Ae_k-B(s_ku_k)=s_kf_k-s_kf_k=0$. So $AC=BD$.
4. Multiply on the right by $C^*$: $ACC^*=BDC^*$.
5. The rows of $C^*$ are the conjugates of the $e_k$, so $C^*e_k=u_k$ and $CC^*e_k=e_k$. Hence $ACC^*v=Av$ for $v\in\operatorname{span}(e_1,\dots,e_m)$.
6. If $v\in(\operatorname{span}(e_1,\dots,e_m))^\perp$, then $Av=0$ (from 7.81) and $C^*v=0$. So $ACC^*v=Av$ there too.
7. $ACC^*$ and $A$ agree on the span and on its orthogonal complement, so $ACC^*=A$. Thus $A=BDC^*$.

Storage remark (p. 277): $A$ has $pn$ entries, while $B,D,C$ have $m(p+m+n)$ entries together. If $p,n$ are large and the rank $m$ is much smaller, storing $B,D,C$ takes far fewer numbers than storing $A$.

*Intuition note.* A matrix of rank $m$ is a sum of $m$ "one pattern in, one pattern out" pieces. Storing the pieces is cheaper than storing the whole table when $m$ is small.

**Exercises 7E (pp. 278–279).** Only the main themes are listed here. Characterise $T=0$ by singular values (1). Characterise singular values by Schmidt pairs $Tv=sw$, $T^*w=sv$ (2). Show $\{\|Tv\|:\|v\|=1\}=[s_n,s_1]$ (4). Compute singular values of concrete maps (5, 6). For self-adjoint or normal $T$ the singular values are $|\lambda_j|$ (7). Show $T,T^*$ have the same positive singular values (9) and that $T^{-1}$ has singular values $1/s_n,\dots,1/s_1$ (10). Further exercises concern $\sum\|Tv_k\|^2=\sum s_k^2$ (11), $T^2$ (12), and unitary equivalence $T_1=S_1T_2S_2$ (13). Others give $s_n\|v\|\le\|Tv\|$ (14), $s_1\ge|\lambda|\ge s_n$ (15), and $(T^*)^\dagger=(T^\dagger)^*$ (16). Exercise 8 proves that the data in 7.76 are the SVD data.

### 7F. Consequences of Singular Value Decomposition

#### Norms of linear maps

**7.82 (upper bound).** If $s_1$ is the largest singular value of $T\in\mathcal L(V,W)$, then $\|Tv\|\le s_1\|v\|$ for all $v\in V$ (p. 280).

Proof (p. 280). With the SVD 7.83:
$$\|Tv\|^2=s_1^2|\langle v,e_1\rangle|^2+\cdots+s_m^2|\langle v,e_m\rangle|^2\le s_1^2\big(|\langle v,e_1\rangle|^2+\cdots+|\langle v,e_m\rangle|^2\big)\le s_1^2\|v\|^2,$$
where the last step is Bessel's inequality (6.26). Take square roots. (The author points to Exercise 14 of §7E for a lower bound.)

Consequences (p. 280). So $\|Tv\|\le s_1$ whenever $\|v\|\le1$ (7.84). Taking $v=e_1$ in 7.83 gives $Te_1=s_1f_1$, hence $\|Te_1\|=s_1$. Therefore
$$\max\{\|Tv\|:v\in V,\ \|v\|\le1\}=s_1.\tag{7.85}$$

**7.86 Definition (norm of a linear map).** $\|T\|=\max\{\|Tv\|:v\in V\text{ and }\|v\|\le1\}$ (p. 280). The maximum exists here because it equals $s_1$ (p. 281). The author notes two uses of "norm": $\|v\|=\sqrt{\langle v,v\rangle}$ for vectors, and $\|T\|$ for maps. The latter does not usually come from an inner product (Exercise 21) (p. 281).

**7.87 (basic properties).** For $T\in\mathcal L(V,W)$ (p. 281): (a) $\|T\|\ge0$; (b) $\|T\|=0\iff T=0$; (c) $\|\lambda T\|=|\lambda|\|T\|$ for $\lambda\in\mathbf F$; (d) $\|S+T\|\le\|S\|+\|T\|$ for $S\in\mathcal L(V,W)$.

Proof highlights (p. 281).
- (b) If $\|T\|=0$ and $u\ne0$, then $Tu=\|u\|\,T(u/\|u\|)=0$.
- (c) Pull $|\lambda|$ out of the maximum.
- (d) Pick $v$ with $\|v\|\le1$ and $\|S+T\|=\|(S+T)v\|$. Then $\|S+T\|=\|Sv+Tv\|\le\|Sv\|+\|Tv\|\le\|S\|+\|T\|$.

The author calls $\|S-T\|$ the distance between $S$ and $T$ (p. 282).

**7.88 (alternative formulas).** For $T\in\mathcal L(V,W)$ (p. 282): (a) $\|T\|$ is the largest singular value; (b) $\|T\|=\max\{\|Tv\|:\|v\|=1\}$; (c) $\|T\|$ is the smallest $c$ with $\|Tv\|\le c\|v\|$ for all $v$.

Proof (p. 282). (a) is 7.85. (b) For $0<\|v\|\le1$, put $u=v/\|v\|$. Then $\|u\|=1$ and $\|Tu\|=\|Tv\|/\|v\|\ge\|Tv\|$, so it suffices to look at unit vectors. (c) For $v\ne0$, $\|T(v/\|v\|)\|\le\|T\|$, giving
$$\|Tv\|\le\|T\|\|v\|.\tag{7.89}$$
Conversely, if $c\ge0$ and $\|Tv\|\le c\|v\|$ for all $v$, then $\|Tv\|\le c$ for $\|v\|\le1$. Taking the maximum gives $\|T\|\le c$.

Computing (p. 282): given the matrix of $T$ in orthonormal bases, form $T^*T$ by matrix multiplication. Ask a computer for an approximation to its largest eigenvalue, then take the square root. By 7.88(a) this approximates $\|T\|$.

**7.90 Examples (norms), p. 283.**
- $\|I\|=1$.
- If $T\in\mathcal L(\mathbf F^n)$ has a matrix of all 1's, then $\|T\|=n$.
- If $V$ has an orthonormal eigenbasis of $T$ with eigenvalues $\lambda_1,\dots,\lambda_n$, then $\|T\|=\max|\lambda_k|$.
- For $T\in\mathcal L(\mathbf R^5)$ with entry $1/(j^2+k)$ in row $j$, column $k$, standard software gives largest singular value $\approx0.8$ and smallest $\approx10^{-6}$. So $\|T\|\approx0.8$ and (by Exercise 10 of §7E) $\|T^{-1}\|\approx10^6$. The author says exact formulas are not possible. The author tells the reader to verify all assertions in the example.

**7.91 (norm of adjoint).** $\|T^*\|=\|T\|$ (p. 283).

Proof. For $w\in W$:
$$\|T^*w\|^2=\langle T^*w,T^*w\rangle=\langle TT^*w,w\rangle\le\|TT^*w\|\|w\|\le\|T\|\|T^*w\|\|w\|.$$
This implies $\|T^*w\|\le\|T\|\|w\|$, and with 7.88(c), $\|T^*\|\le\|T\|$. Replacing $T$ by $T^*$ and using $(T^*)^*=T$ gives $\|T\|\le\|T^*\|$. (The author also suggests a proof via Exercise 9 of §7E.)

#### Approximation by linear maps with lower-dimensional range

**7.92 (best approximation by a map whose range has dimension $\le k$).** Let $s_1\ge\cdots\ge s_m$ be the positive singular values of $T\in\mathcal L(V,W)$ and $1\le k<m$. Then
$$\min\{\|T-S\|:S\in\mathcal L(V,W),\ \dim\operatorname{range}S\le k\}=s_{k+1}.$$
Moreover, if $Tv=\sum_{j\le m}s_j\langle v,e_j\rangle f_j$ is an SVD and $T_kv=s_1\langle v,e_1\rangle f_1+\cdots+s_k\langle v,e_k\rangle f_k$, then $\dim\operatorname{range}T_k=k$ and $\|T-T_k\|=s_{k+1}$ (p. 284).

Proof (p. 284).
- *$T_k$ attains $s_{k+1}$.* $\|(T-T_k)v\|^2=\sum_{j=k+1}^m s_j^2|\langle v,e_j\rangle|^2\le s_{k+1}^2\sum_{j=k+1}^m|\langle v,e_j\rangle|^2\le s_{k+1}^2\|v\|^2$. So $\|T-T_k\|\le s_{k+1}$. Since $(T-T_k)e_{k+1}=s_{k+1}f_{k+1}$, equality holds.
- *No $S$ does better.* Let $\dim\operatorname{range}S\le k$. The $k+1$ vectors $Se_1,\dots,Se_{k+1}$ are linearly dependent, so $a_1Se_1+\cdots+a_{k+1}Se_{k+1}=0$ with the $a_j$ not all 0. Then $a_1e_1+\cdots+a_{k+1}e_{k+1}\ne0$, and
$$\|(T-S)(\textstyle\sum a_je_j)\|^2=\|T(\sum a_je_j)\|^2=\|\textstyle\sum s_ja_jf_j\|^2=\sum_{j=1}^{k+1}s_j^2|a_j|^2\ge s_{k+1}^2\sum|a_j|^2=s_{k+1}^2\|\textstyle\sum a_je_j\|^2.$$
Hence $\|T-S\|\ge s_{k+1}$.

*Skip path:* carry forward "truncate after $k$ terms; error is exactly $s_{k+1}$".

*Intuition note.* Dropping the weakest stretches leaves the best simplified copy of the map. The size of the biggest dropped stretch, $s_{k+1}$, is the error. The author says this leads to algorithms for compressing huge matrices (p. 283). Exercise 22 and Exercise 27 give other approximation results (p. 284).

#### Polar decomposition

Motivation (p. 285): every complex $z\ne0$ is $z=\frac{z}{|z|}|z|=\frac{z}{|z|}\sqrt{\bar zz}$, a factor of absolute value 1 times a nonnegative factor. By analogy the author guesses that every operator is a unitary times $\sqrt{T^*T}$ ($T^*T$ is positive by 7.64(a), so its square root is a well-defined positive operator).

**7.93 (polar decomposition).** For $T\in\mathcal L(V)$ (real or complex space) there is a unitary $S\in\mathcal L(V)$ with $T=S\sqrt{T^*T}$ (p. 286).

Proof (p. 286).
1. Take an SVD $Tv=\sum_{k\le m}s_k\langle v,e_k\rangle f_k$ (7.94) with $e_1,\dots,e_m$ and $f_1,\dots,f_m$ orthonormal lists in $V$. Extend both to orthonormal bases $e_1,\dots,e_n$ and $f_1,\dots,f_n$ of $V$.
2. Define $Sv=\langle v,e_1\rangle f_1+\cdots+\langle v,e_n\rangle f_n$. Then $\|Sv\|^2=\sum|\langle v,e_k\rangle|^2=\|v\|^2$, so $S$ is unitary.
3. Applying $T^*$ to 7.94 and using 7.77: $T^*Tv=\sum_{k\le m}s_k^2\langle v,e_k\rangle e_k$.
4. Hence $\sqrt{T^*T}\,v=\sum_{k\le m}s_k\langle v,e_k\rangle e_k$. The operator sending $v$ to this right side is positive and its square is $T^*T$.
5. Then $S\sqrt{T^*T}\,v=\sum_{k\le m}s_k\langle v,e_k\rangle f_k=Tv$ by 7.94.

Remarks (pp. 285–286).
- Exercise 27 shows this $S$ is as close to $T$ as any unitary operator can be.
- Take $\mathbf F=\mathbf C$ and $T=S\sqrt{T^*T}$. There is an orthonormal basis in which $S$ is diagonal, and one in which $\sqrt{T^*T}$ is diagonal. **Warning (author):** there may be no single orthonormal basis that diagonalises both.
- If $T$ is normal, an orthonormal basis making both diagonal exists (Exercise 31). Conversely, if $T=S\sqrt{T^*T}$ with $S$ unitary and both diagonal in the same orthonormal basis, then $T$ has a diagonal matrix there, so $T$ is normal [7.31, (c)⇔(a)].
- The author says alternative proofs via the spectral theorem exist, but this one "seems cleaner" (p. 286).

*Intuition note.* "Unitary times positive" means "rotate or reflect, after stretching along perpendicular axes". It parallels writing a complex number as an angle part times a size part.

#### Operators applied to ellipsoids and parallelepipeds

**7.95 Definition (ball).** $B=\{v\in V:\|v\|<1\}$ (p. 287).

**7.96 Definition (ellipsoid).** For an orthonormal basis $f_1,\dots,f_n$ of $V$ and positive numbers $s_1,\dots,s_n$, the ellipsoid with principal axes $s_1f_1,\dots,s_nf_n$ is
$$E(s_1f_1,\dots,s_nf_n)=\Big\{v\in V:\frac{|\langle v,f_1\rangle|^2}{s_1^2}+\cdots+\frac{|\langle v,f_n\rangle|^2}{s_n^2}<1\Big\}.$$
Think of it as the ball stretched by $s_k$ along each $f_k$-axis (p. 287).

**7.97 Examples (pp. 287–288).** $E(2f_1,f_2)$ in $\mathbf R^2$ with the standard basis; the same ellipsoid with $f_1=(\tfrac1{\sqrt2},\tfrac1{\sqrt2})$, $f_2=(-\tfrac1{\sqrt2},\tfrac1{\sqrt2})$; and $E(4f_1,3f_2,2f_3)$ in $\mathbf R^3$. Also $E(f_1,\dots,f_n)=B$ for every orthonormal basis, by Parseval's identity 6.30(b) (p. 288).

**7.98 Notation.** For $\Omega\subseteq V$, $T(\Omega)=\{Tv:v\in\Omega\}$. So $T(V)=\operatorname{range}T$ (p. 288).

**7.99 (invertible operator takes ball to ellipsoid).** If $T\in\mathcal L(V)$ is invertible, then $T(B)=E(s_1f_1,\dots,s_nf_n)$ for an SVD $Tv=\sum_{k\le n}s_k\langle v,e_k\rangle f_k$ with $e$'s and $f$'s orthonormal bases (p. 288).

Proof (p. 288). Since $T$ is invertible, no $s_k$ is 0 (7.68).
- $\subseteq$: for $v\in B$, $\sum_k\frac{|\langle Tv,f_k\rangle|^2}{s_k^2}=\sum_k|\langle v,e_k\rangle|^2<1$. (This uses $\langle Tv,f_k\rangle=s_k\langle v,e_k\rangle$.) So $Tv\in E$.
- $\supseteq$: for $w\in E$, let $v=\sum\frac{\langle w,f_k\rangle}{s_k}e_k$. Then $\|v\|<1$ and $Tv=\sum\langle w,f_k\rangle f_k=w$.

**7.101 (ellipsoids to ellipsoids).** If $T\in\mathcal L(V)$ is invertible and $E$ is an ellipsoid in $V$, then $T(E)$ is an ellipsoid (p. 289). Proof: write $E=E(s_1f_1,\dots,s_nf_n)$ and define $S(\sum a_kf_k)=\sum a_ks_kf_k$. Then $S(B)=E$ ("as you can verify"). So $T(E)=(TS)(B)$, an ellipsoid by 7.99 applied to $TS$.

**7.102 Definition (parallelepiped).** For a basis $v_1,\dots,v_n$ of $V$, $P(v_1,\dots,v_n)=\{a_1v_1+\cdots+a_nv_n:a_1,\dots,a_n\in(0,1)\}$. A parallelepiped is $u+P(v_1,\dots,v_n)$ with $u\in V$; the $v_k$ are its edges (p. 289). Example 7.103: $(0.3,0.5)+P((1,0),(1,1))$ in $\mathbf R^2$.

**7.104.** For invertible $T\in\mathcal L(V)$, $T(u+P(v_1,\dots,v_n))=Tu+P(Tv_1,\dots,Tv_n)$. Proof: $Tv_1,\dots,Tv_n$ is a basis, and by linearity $T(u+\sum a_kv_k)=Tu+\sum a_kTv_k$ (p. 290).

**7.105 Definition (box).** A box is $u+P(r_1e_1,\dots,r_ne_n)$ with $r_k>0$ and $e_1,\dots,e_n$ an orthonormal basis (p. 290). In $\mathbf R^2$ a box is a rectangle. Examples 7.106: $(1,0)+P(\sqrt2e_1,\sqrt2e_2)$ with $e_1=(\tfrac1{\sqrt2},\tfrac1{\sqrt2})$, $e_2=(-\tfrac1{\sqrt2},\tfrac1{\sqrt2})$; and $P(e_1,2e_2,e_3)$ in $\mathbf R^3$.

**7.107 (invertible operator takes some boxes to boxes).** With the SVD of 7.100 (both lists orthonormal bases), $T$ maps the box $u+P(r_1e_1,\dots,r_ne_n)$ onto the box $Tu+P(r_1s_1f_1,\dots,r_ns_nf_n)$, for all positive $r_k$ and all $u\in V$. Proof: $T(u+\sum a_kr_ke_k)=Tu+\sum a_kr_ks_kf_k$ (p. 291). In general $T$ maps boxes to parallelepipeds that need not be boxes.

*Intuition note.* An invertible map sends a box with sides along the $e_k$ to a box with sides along the $f_k$, stretching each side by $s_k$. So boxes along those directions stay boxes, and the unit ball becomes an ellipsoid whose axes are the SVD directions.

#### Volume via singular values

The author works with an intuitive notion of volume (true definitions belong to analysis) and assumes $\mathbf F=\mathbf R$ (p. 291).

**7.108 Definition (volume of a box).** $\operatorname{volume}(u+P(r_1e_1,\dots,r_ne_n))=r_1\times\cdots\times r_n$. For the boxes of 7.106 this gives area $\sqrt2\cdot\sqrt2=2$ and volume $1\cdot2\cdot1=2$ (p. 291).

**7.109 Definition (volume, intuitive).** For $\Omega\subseteq V$, $\operatorname{volume}\Omega$ is approximately the sum of the volumes of disjoint boxes approximating $\Omega$, as in the Riemann integral. The author notes that for reasonably nice subsets, analysis answers affirmatively the questions of basis-independence and additivity over disjoint sets (p. 292).

**7.110 Example (p. 292).** $Tv=2\langle v,e_1\rangle e_1+\langle v,e_2\rangle e_2$ on $\mathbf R^2$ doubles the width and keeps the height of each approximating box. So it doubles the volume (area) of each box, and so changes the volume of the ball by a factor 2.

**7.111 (volume changes by the product of singular values).** For $\mathbf F=\mathbf R$, invertible $T\in\mathcal L(V)$ and $\Omega\subseteq V$:
$$\operatorname{volume}T(\Omega)=(\text{product of singular values of }T)\,(\operatorname{volume}\Omega).$$
Proof (p. 293). Approximate $\Omega$ by boxes $u+P(r_1e_1,\dots,r_ne_n)$, of volume $r_1\cdots r_n$, using the SVD bases. By 7.107, $T$ maps each to a box of volume $(s_1\cdots s_n)(r_1\cdots r_n)$. These boxes approximate $T(\Omega)$, so the volume changes by the factor $s_1\cdots s_n$.

The author adds that, as determinants will show, this product equals $|\det T|$ (see 9.60, 9.61; not covered here) (p. 293).

*Intuition note.* Each stretch $s_k$ multiplies one side length, so the volume is multiplied by all of them together.

#### Properties of an operator as determined by its eigenvalues (p. 293)

Context: finite-dimensional complex inner product space. For a normal operator, the property in column 1 holds iff all eigenvalues lie in the set in column 2. Only the first row does not need normality.

| property of a normal operator | eigenvalues contained in |
|---|---|
| invertible | $\mathbf C\setminus\{0\}$ |
| self-adjoint | $\mathbf R$ |
| skew | $\{\lambda:\operatorname{Re}\lambda=0\}$ |
| orthogonal projection | $\{0,1\}$ |
| positive | $[0,\infty)$ |
| unitary | $\{\lambda:|\lambda|=1\}$ |
| norm is less than 1 | $\{\lambda:|\lambda|<1\}$ |

The author asks the reader to explain each row. For the last row: $\|T\|$ is the largest singular value (7.85), and for normal $T$ with $\mathbf F=\mathbf C$ the singular values are the $|\lambda_j|$ (Exercise 7 of §7E).

**Exercises 7F (pp. 294–296).** Topics: reverse triangle inequality (1); $\|T\|=\max|\lambda|$ for self-adjoint or normal $T$ (2); $\|Tv\|=\|T\|\|v\|\iff T^*Tv=\|T\|^2v$ (3); $\|ST\|\le\|S\|\|T\|$ (5); metric and openness of invertibles and density of invertible or diagonalizable operators (7–11); $\|T^*T\|=\|T\|^2$ (19); the norm on $\mathcal L(V,W)$ is not from an inner product (21); the minimum of $\|T|_U\|$ over $k$-dimensional $U$ equals $s_{n-k+1}$ (22); polar decomposition exercises (15, 25–31), including that $S$ in 7.93 is the closest unitary (27); and the fact that a suitable ellipsoid in $(\operatorname{null}T)^\perp$ is mapped by $T$ onto the unit ball of $\operatorname{range}T$ (32).

## Toy example (ours, not from the text)

Let $T:\mathbf R^2\to\mathbf R^2$, $T(v_1,v_2)=(2v_2,v_1)$. Matrix $A=\begin{pmatrix}0&2\\1&0\end{pmatrix}$.

1. $A^\top A=\begin{pmatrix}0&1\\2&0\end{pmatrix}\begin{pmatrix}0&2\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&4\end{pmatrix}$. Eigenvalues are 4 and 1, so the singular values are $s_1=2,\ s_2=1$. The eigenvalues of $A$ are $\pm\sqrt2$ (from $\lambda^2=2$), so they do not show the numbers 2 and 1.
2. Orthonormal eigenvectors of $A^\top A$: $e_1=(0,1)$ for 4, $e_2=(1,0)$ for 1. Then $f_1=Te_1/2=(2,0)/2=(1,0)$ and $f_2=Te_2/1=(0,1)$.
3. Check 7.71 with $v=(3,5)$: $Tv=(10,3)$. Formula: $2\cdot\langle v,e_1\rangle f_1+1\cdot\langle v,e_2\rangle f_2=2\cdot5\,(1,0)+1\cdot3\,(0,1)=(10,3)$ ✓.
4. Matrix form (7.80): $B=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, $D=\begin{pmatrix}2&0\\0&1\end{pmatrix}$, $C=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ (columns $e_1,e_2$). $DC^*=\begin{pmatrix}0&2\\1&0\end{pmatrix}$, so $BDC^*=A$ ✓.
5. Norm: $\|T\|=s_1=2$. Check: $\|Te_1\|=\|(2,0)\|=2$.
6. Best rank-1 approximation: $T_1v=2\langle v,e_1\rangle f_1=(2v_2,0)$. Then $(T-T_1)v=(0,v_1)$, so $\|T-T_1\|=1=s_2$ (attained at $v=e_2$).
7. Polar decomposition: $Sv=\langle v,e_1\rangle f_1+\langle v,e_2\rangle f_2=(v_2,v_1)$ (a reflection, unitary). $\sqrt{T^*T}\,v=2\langle v,e_1\rangle e_1+\langle v,e_2\rangle e_2=(v_1,2v_2)$. Then $S\sqrt{T^*T}\,v=S(v_1,2v_2)=(2v_2,v_1)=Tv$ ✓.
8. Ball and volume: $T$ maps the unit disk onto $E(2f_1,1f_2)$, which has semi-axis 2 along $f_1=(1,0)$ and 1 along $f_2=(0,1)$. Areas are multiplied by $2\cdot1=2$. (Also $\det A=0\cdot0-2\cdot1=-2$, absolute value 2, as the text's remark predicts.)

## Concepts
- [[singular-values]] (new) — square roots of eigenvalues of $T^*T$, decreasing, with multiplicity; defined for maps between different inner product spaces (p. 271)
- [[singular-value-decomposition]] — $Tv=\sum s_k\langle v,e_k\rangle f_k$ with orthonormal lists in $V$ and $W$ (7.70); gives a diagonal matrix in suitable orthonormal bases (pp. 273–274)
- [[singular-value-decomposition]] (matrix form) — $A=BDC^*$ with $B,C$ having orthonormal columns and $D$ positive diagonal (7.80); the author's form uses $m$ = rank, not full size (p. 277)
- [[positive-semidefinite-matrix]] — here "positive operator" ($\langle Tv,v\rangle\ge0$, self-adjoint); $T^*T$ is always one (p. 270)
- [[spectral-theorem]] — used on $T^*T$ to build the SVD; the SVD is compared with it (pp. 273–274)
- [[pseudoinverse]] — $T^\dagger$, obtained from the SVD by swapping $e,f$ and inverting each $s_k$ (7.78) (p. 275)
- [[operator-norm]] (new) — $\|T\|=\max\{\|Tv\|:\|v\|\le1\}=s_1$; satisfies $\|Tv\|\le\|T\|\|v\|$ and $\|T^*\|=\|T\|$ (pp. 280–283)
- [[eckart-young-theorem]] — 7.92: the truncated SVD $T_k$ is the best approximation with range dimension $\le k$, error $s_{k+1}$ (in the operator norm; the book gives no name) (p. 284)
- [[polar-decomposition]] (new) — $T=S\sqrt{T^*T}$ with $S$ unitary (p. 286)
- [[ellipsoid-image-of-ball]] (new) — an invertible operator maps the unit ball to $E(s_1f_1,\dots,s_nf_n)$ (p. 288)
- [[determinant]] — only as a forward reference: product of singular values $=|\det T|$ (p. 293)
- [[rank]] — number of positive singular values (7.68(b)) (p. 272)

## Canonical instances
- [[svd-example-7-66]] — $T(z)=(0,3z_1,2z_2,-3z_4)$ has singular values $3,3,2,0$ but eigenvalues only $-3,0$ (p. 271)
- [[svd-example-7-79]] — full SVD of a map $\mathbf F^4\to\mathbf F^3$ with $s=5,\sqrt2$ (p. 276)
- [[norm-example-7-90]] — norms: $\|I\|=1$; all-ones matrix has norm $n$; the $1/(j^2+k)$ matrix has $\|T\|\approx0.8$ and $\|T^{-1}\|\approx10^6$ (p. 283)
- [[volume-example-7-110]] — a stretch by 2 along one axis doubles the area of the ball (p. 292)

## Bridges (candidates)
- [same-math] 7.80 $A=BDC^*$ ↔ linear-algebra canon "SVD" $A=U\Sigma V^\top$ — the same factorisation, written with only the $m$ positive singular values.
- [same-math] 7.92 ↔ Eckart–Young theorem (spectral-norm version) — same statement: truncated SVD is the best rank-$k$ approximation, error $s_{k+1}$.
- [same-math] $\|T\|\,\|T^{-1}\|=s_1/s_n$ (from 7.85 and Exercise 10 of §7E) ↔ condition number — Example 7.90 gives $0.8\times10^6$ for the $1/(j^2+k)$ matrix; the text does not use the term.
- [same-math] Product of singular values $=|\det T|$ (p. 293, forward reference) ↔ determinant as signed volume-scaling factor.
- [structural-analogy] Polar decomposition $T=S\sqrt{T^*T}$ ↔ complex numbers $z=\frac z{|z|}|z|$ — the author's own analogy (p. 285).
- [structural-analogy] SVD directions $e_k$ ↔ statistics: principal component analysis (not stated in this unit) — a possible link, to be confirmed later.

## Questions this raises
- Why does the product of the singular values equal $|\det T|$ (promised in 9.60–9.61), and what does that say about the sign of the determinant?
- If the $s_k$ decay slowly, how large is the error $s_{k+1}$, and how can one judge whether a low-rank approximation is acceptable?
- Is the SVD unique when singular values repeat, or when the $e_k$ for $s_k=0$ are free to choose? What is unique?
- How do the SVD and the polar decomposition fail to simultaneously diagonalise a non-normal operator (the warning on p. 285)?

## Exercises worth doing
- Ex. 7E.2 (p. 278) — characterises singular values through Schmidt pairs $Tv=sw$, $T^*w=sv$ — difficulty: medium
- Ex. 7E.7 (p. 278) — singular values of a normal or self-adjoint operator are $|\lambda_j|$; used in the table on p. 293 — difficulty: medium
- Ex. 7E.9 (p. 279) — $T$ and $T^*$ have the same positive singular values — difficulty: medium
- Ex. 7F.15 (p. 295) — find an explicit unitary $S$ with $T=S\sqrt{T^*T}$ — difficulty: medium
- Ex. 7F.19 (p. 295) — $\|T^*T\|=\|T\|^2$ — difficulty: medium
- Ex. 7F.27 (p. 296) — the unitary $S$ from the polar decomposition is the closest unitary to $T$ — difficulty: hard

## Reading notes
- This part starts at the beginning of §7E (printed p. 270) and ends with the exercises of §7F (printed p. 296). Offset: printed = pdf − 14.
- The running header on printed p. 272 shows "≈ 100 e" instead of the page number in the image. I used 272 from the page label.
- The extracted text had garbled math symbols (private-use characters). I checked the formulas against the page images.
- These pages never state that $V,W$ are finite-dimensional (p. 293 says "finite-dimensional" only for the table), although the proofs use $\dim V$ and $\dim W$; I treat it as an assumption carried over from earlier pages. Many proofs cite results from earlier parts (7.6, 7.29, 7.31, 7.49, 6.51, 6.57, 6.68, 3.21, 2.39), which I did not see.
- The table "properties of a normal operator" uses the term "skew" without defining it on these pages.
- The haiku on p. 279 is printed in the source as written by ChatGPT. I did not use it.
- The numerical values in Example 7.90 are given by the author as approximate software output.
- These pages do not name 7.92 "Eckart–Young". I only use that name as a canon label.
