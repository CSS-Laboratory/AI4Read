---
id: axler-2024-ladr/ch03-linear-p1
work: axler-2024-ladr
unit: "3 Linear Maps (part 1/3): 3A Vector Space of Linear Maps; 3B Null Spaces and Ranges"
pages: 51-68
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
# Linear Maps, part 1: the space of linear maps, null spaces and ranges

## L0 — One line
For a linear map $T$ on a finite-dimensional space, $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$, and this forces maps to smaller spaces to be non-injective, maps to bigger spaces to be non-surjective, and gives results on linear systems.

## L1 — The gist (≤ 120 words)
This part defines linear maps (functions preserving addition and scaling) and shows that a linear map is fixed by its values on a basis. Linear maps from $V$ to $W$ form a vector space, and can be composed (multiplied). Each map has a null space (vectors sent to 0) and a range (all outputs), both subspaces. A map is injective (distinct inputs, distinct outputs) exactly when its null space is $\{0\}$. The fundamental theorem of linear maps adds the dimensions of null space and range to get the dimension of the domain. Consequences: homogeneous systems with more variables than equations have nonzero solutions, and systems with more equations than variables are unsolvable for some right-hand sides.

**Prerequisites:** vector spaces over $\mathbf R$ or $\mathbf C$, subspaces, span, linear independence, basis, dimension; extending an independent list to a basis (2.32); the inequality $\dim\operatorname{range}T\le\dim W$, which the source cites as 2.37 (p. 63).

## L2 — Key ideas
- A linear map satisfies additivity and homogeneity. A linear map sends 0 to 0, so $x\mapsto mx+b$ is linear only if $b=0$ (3.1, 3.10; p. 52, 56).
- Linear map lemma: values on a basis can be chosen freely and then determine a unique linear map (3.4; p. 54).
- $\mathcal L(V,W)$ is a vector space. The product $ST$ is composition. It is associative and distributive but not commutative (3.6–3.9; p. 55–56).
- $\operatorname{null}T$ and $\operatorname{range}T$ are subspaces (of $V$ and $W$) (3.13, 3.18; p. 59–61).
- $T$ is injective iff $\operatorname{null}T=\{0\}$ (3.15; p. 60). Surjectivity depends on the chosen target space (3.20; p. 62).
- Fundamental theorem of linear maps: $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ (3.21; p. 62–63).
- Dimension comparisons: $\dim V>\dim W$ rules out injectivity, $\dim V<\dim W$ rules out surjectivity (3.22, 3.24; p. 63–64).
- Systems of linear equations are recast as questions about injectivity and surjectivity of a map $\mathbf F^n\to\mathbf F^m$ (3.25–3.28; p. 64–65).

## L3 — Walkthrough

### Chapter 3 introduction (p. 51)
The chapter announces the fundamental theorem of linear maps, the matrix of a linear map, and product, quotient and dual spaces (the matrix part is outside these pages). The author says it implies that a linear map from a finite-dimensional space to itself is one-to-one iff its range is the whole space. Standing assumptions: $\mathbf F$ denotes $\mathbf R$ or $\mathbf C$; $U,V,W$ are vector spaces over $\mathbf F$ (p. 51).

### 3A Vector Space of Linear Maps

**Definition and examples.**
- **3.1 Linear map.** $T:V\to W$ is linear if (p. 52)
  - additivity: $T(u+v)=Tu+Tv$ for all $u,v\in V$;
  - homogeneity: $T(\lambda v)=\lambda(Tv)$ for all $\lambda\in\mathbf F$, $v\in V$.
- **3.2 Notation.** $\mathcal L(V,W)$ is the set of linear maps $V\to W$. $\mathcal L(V)=\mathcal L(V,V)$ (p. 52).
- **3.3 Examples** (p. 52–53):
  - zero map: $0v=0$.
  - identity operator: $Iv=v$.
  - differentiation: $D\in\mathcal L(\mathcal P(\mathbf R))$, $Dp=p'$.
  - integration: $T\in\mathcal L(\mathcal P(\mathbf R),\mathbf R)$, $Tp=\int_0^1p$.
  - multiplication by $x^2$: $(Tp)(x)=x^2p(x)$.
  - backward shift on $\mathbf F^\infty$: $T(x_1,x_2,x_3,\dots)=(x_2,x_3,\dots)$.
  - from $\mathbf R^3$ to $\mathbf R^2$: $T(x,y,z)=(2x-y+3z,\,7x+5y-6z)$.
  - from $\mathbf F^n$ to $\mathbf F^m$: with $A_{j,k}\in\mathbf F$,
  $$T(x_1,\dots,x_n)=(A_{1,1}x_1+\dots+A_{1,n}x_n,\dots,A_{m,1}x_1+\dots+A_{m,n}x_n).$$
  The author states that every linear map $\mathbf F^n\to\mathbf F^m$ has this form (Exercise 3A.3 asks the reader to show this, p. 57).
  - composition with a fixed polynomial: $(Tp)(x)=p(q(x))$.

**3.4 Linear map lemma.** Suppose $v_1,\dots,v_n$ is a basis of $V$ and $w_1,\dots,w_n\in W$. Then there exists a unique linear map $T:V\to W$ with $Tv_k=w_k$ for each $k$ (p. 54).
- *Existence.* Define $T(c_1v_1+\dots+c_nv_n)=c_1w_1+\dots+c_nw_n$. This is a well-defined function because every vector of $V$ has a unique expression in the basis. Taking $c_k=1$ and the other $c$'s 0 gives $Tv_k=w_k$ (p. 54).
- *Additivity.* For $u=\sum a_kv_k$ and $v=\sum c_kv_k$: $T(u+v)=T(\sum(a_k+c_k)v_k)=\sum(a_k+c_k)w_k=\sum a_kw_k+\sum c_kw_k=Tu+Tv$ (p. 54).
- *Homogeneity.* $T(\lambda v)=T(\sum\lambda c_kv_k)=\sum\lambda c_kw_k=\lambda\sum c_kw_k=\lambda Tv$ (p. 54).
- *Uniqueness.* If $T$ is linear with $Tv_k=w_k$, homogeneity gives $T(c_kv_k)=c_kw_k$. Additivity then gives $T(\sum c_kv_k)=\sum c_kw_k$. So $T$ is determined on the span, which is $V$ (p. 54).

*Intuition note.* A linear map has no hidden freedom. Once you decide where the basis vectors go, every other vector's image is forced. Any choice of images for basis vectors is allowed.

**Algebraic operations.**
- **3.5** For $S,T\in\mathcal L(V,W)$ and $\lambda\in\mathbf F$: $(S+T)(v)=Sv+Tv$ and $(\lambda T)(v)=\lambda(Tv)$. These are again linear maps (p. 55).
- **3.6** With these operations $\mathcal L(V,W)$ is a vector space; the proof is left to the reader. Its additive identity is the zero map (p. 55).
- **3.7 Product.** For $T\in\mathcal L(U,V)$ and $S\in\mathcal L(V,W)$, $ST\in\mathcal L(U,W)$ is $(ST)(u)=S(Tu)$. It is the composition $S\circ T$ and is defined only when $T$ maps into the domain of $S$ (p. 55).
- **3.8 Algebraic properties** (proof left to reader; p. 56):
  - associativity: $(T_1T_2)T_3=T_1(T_2T_3)$ whenever the products make sense;
  - identity: $TI=IT=T$ for $T\in\mathcal L(V,W)$ (the two $I$'s are the identity operators on $V$ and on $W$);
  - distributivity: $(S_1+S_2)T=S_1T+S_2T$ and $S(T_1+T_2)=ST_1+ST_2$.
- Multiplication is not commutative: $ST=TS$ need not hold even when both sides make sense (p. 56).
- **3.9 Example.** Let $D$ be differentiation and $T$ multiplication by $x^2$ on $\mathcal P(\mathbf R)$. Then
$$((TD)p)(x)=x^2p'(x),\qquad ((DT)p)(x)=x^2p'(x)+2xp(x).$$
So $TD\ne DT$ (p. 56).
- **3.10** $T(0)=0$ for linear $T$. Proof: $T(0)=T(0+0)=T(0)+T(0)$; add the additive inverse of $T(0)$ to both sides (p. 56).
- Consequence: $f(x)=mx+b$ on $\mathbf R$ is linear iff $b=0$. High-school "linear functions" are not in general linear maps (p. 56).

*Intuition note.* Composing maps behaves like multiplication of numbers, except that order matters. In 3.9, differentiating after multiplying also differentiates the factor $x^2$, which creates the extra term $2xp(x)$.

**Exercises 3A** are listed under "Exercises worth doing" below (p. 57–58).

### 3B Null Spaces and Ranges

**Null space and injectivity.**
- **3.11** For $T\in\mathcal L(V,W)$: $\operatorname{null}T=\{v\in V: Tv=0\}$ (p. 59). "Kernel" is another name (p. 59).
- **3.12 Examples** (p. 59):
  - zero map: $\operatorname{null}T=V$.
  - $\varphi(z_1,z_2,z_3)=z_1+2z_2+3z_3$ on $\mathbf C^3$: the null space is $\{z: z_1+2z_2+3z_3=0\}$.
  - differentiation: the null space is the set of constant functions.
  - multiplication by $x^2$: $\operatorname{null}T=\{0\}$.
  - backward shift: $\operatorname{null}T=\{(a,0,0,\dots):a\in\mathbf F\}$.
- **3.13** $\operatorname{null}T$ is a subspace of $V$. Proof: $T(0)=0$ by 3.10. If $u,v\in\operatorname{null}T$ then $T(u+v)=Tu+Tv=0+0=0$. If $u\in\operatorname{null}T$ then $T(\lambda u)=\lambda Tu=\lambda0=0$. Then 1.34 (subspace test) applies (p. 60).
- **3.14 Injective:** $Tu=Tv$ implies $u=v$. Equivalently, distinct inputs give distinct outputs. "One-to-one" means the same (p. 60).
- **3.15** $T$ is injective iff $\operatorname{null}T=\{0\}$ (p. 60).
  - ($\Rightarrow$) $\{0\}\subseteq\operatorname{null}T$ by 3.10. If $v\in\operatorname{null}T$ then $T(v)=0=T(0)$, so $v=0$ by injectivity.
  - ($\Leftarrow$) If $Tu=Tv$ then $0=Tu-Tv=T(u-v)$. So $u-v\in\operatorname{null}T=\{0\}$ and $u=v$.
- Of the maps in 3.12, only multiplication by $x^2$ is injective (the zero map is injective in the special case $V=\{0\}$) (p. 60).

*Intuition note.* For a linear map, collisions are controlled by one vector set. If two inputs collide, their difference is sent to 0. So checking that only 0 is sent to 0 is enough.

**Range and surjectivity.**
- **3.16** $\operatorname{range}T=\{Tv: v\in V\}\subseteq W$ (p. 61).
- **3.17 Examples** (p. 61):
  - zero map: $\operatorname{range}T=\{0\}$.
  - $T(x,y)=(2x,5y,x+y)$ on $\mathbf R^2\to\mathbf R^3$: $\operatorname{range}T=\{(2x,5y,x+y):x,y\in\mathbf R\}$.
  - differentiation on $\mathcal P(\mathbf R)$: every $q$ is $p'$ for some $p$, so $\operatorname{range}D=\mathcal P(\mathbf R)$.
- **3.18** $\operatorname{range}T$ is a subspace of $W$. Proof: $0=T(0)$. If $Tv_1=w_1$ and $Tv_2=w_2$ then $T(v_1+v_2)=w_1+w_2$. If $Tv=w$ then $T(\lambda v)=\lambda w$ (p. 61).
- **3.19 Surjective:** $\operatorname{range}T=W$. "Onto" means the same (p. 62). Of the maps in 3.17, only differentiation is surjective (the zero map in the special case $W=\{0\}$) (p. 62).
- **3.20 Example.** $D\in\mathcal L(\mathcal P_5(\mathbf R))$, $Dp=p'$, is not surjective because $x^5$ is not in its range. But $S\in\mathcal L(\mathcal P_5(\mathbf R),\mathcal P_4(\mathbf R))$, $Sp=p'$, is surjective, since its range is $\mathcal P_4(\mathbf R)$ (p. 62).

**3.21 Fundamental theorem of linear maps.** If $V$ is finite-dimensional and $T\in\mathcal L(V,W)$, then $\operatorname{range}T$ is finite-dimensional and
$$\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T.\tag{3.21}$$
*Proof* (p. 62–63):
1. Let $u_1,\dots,u_m$ be a basis of $\operatorname{null}T$. Extend it (by 2.32) to a basis $u_1,\dots,u_m,v_1,\dots,v_n$ of $V$. So $\dim V=m+n$. It remains to show $Tv_1,\dots,Tv_n$ is a basis of $\operatorname{range}T$.
2. *Spanning.* For $v\in V$ write $v=a_1u_1+\dots+a_mu_m+b_1v_1+\dots+b_nv_n$. Applying $T$ kills the $Tu_k$ terms because each $u_k\in\operatorname{null}T$. Hence $Tv=b_1Tv_1+\dots+b_nTv_n$. So the list spans $\operatorname{range}T$, which is therefore finite-dimensional.
3. *Independence.* Suppose $c_1Tv_1+\dots+c_nTv_n=0$. Then $T(c_1v_1+\dots+c_nv_n)=0$, so $c_1v_1+\dots+c_nv_n\in\operatorname{null}T$. Write it as $d_1u_1+\dots+d_mu_m$. By independence of $u_1,\dots,u_m,v_1,\dots,v_n$, all $c$'s and $d$'s are 0.

*Intuition note.* The domain splits into a part that $T$ destroys (null space) and a part that survives (copied one-to-one into the range). The dimensions of the two parts add up to $\dim V$.

**3.22** If $\dim V>\dim W$ (both finite-dimensional), no linear map $V\to W$ is injective. Proof: $\dim\operatorname{null}T=\dim V-\dim\operatorname{range}T\ge\dim V-\dim W>0$ (using 2.37). So $\operatorname{null}T\ne\{0\}$, and $T$ is not injective by 3.15 (p. 63).
- **3.23 Example.** $T:\mathbf F^4\to\mathbf F^3$, $T(z_1,\dots,z_4)=(\sqrt7z_1+\pi z_2+z_4,\ 97z_1+3z_2+2z_3,\ z_2+6z_3+7z_4)$ is not injective, since $4>3$, with no calculation needed (p. 63).

**3.24** If $\dim V<\dim W$ (both finite-dimensional), no linear map $V\to W$ is surjective. Proof: $\dim\operatorname{range}T=\dim V-\dim\operatorname{null}T\le\dim V<\dim W$, so $\operatorname{range}T\ne W$ (p. 64).

**Linear equations.**
- *Homogeneous system* (all right-hand sides 0). Given $A_{j,k}\in\mathbf F$, the system $\sum_{k=1}^nA_{j,k}x_k=0$ for $j=1,\dots,m$ always has the solution $x=0$. Define
$$T(x_1,\dots,x_n)=\Big(\sum_{k=1}^nA_{1,k}x_k,\dots,\sum_{k=1}^nA_{m,k}x_k\Big)\tag{3.25}$$
with $T:\mathbf F^n\to\mathbf F^m$ (shapes: $n$ unknowns in, $m$ equations out). Then $T(x)=0$ is the system. Nonzero solutions exist iff $\operatorname{null}T\supsetneq\{0\}$, i.e. iff $T$ is not injective (3.15) (p. 64).
- **3.26** A homogeneous system with more variables than equations has nonzero solutions. Proof: $n>m$, so $T$ is not injective by 3.22 (p. 65). Example: four equations, five variables (p. 65).
- *Inhomogeneous system* $\sum_kA_{j,k}x_k=c_j$ for $j=1,\dots,m$ (3.27). With the same $T$, it reads $T(x)=(c_1,\dots,c_m)$. Some choice of constants gives no solution iff $\operatorname{range}T\ne\mathbf F^m$, i.e. iff $T$ is not surjective (p. 65).
- **3.28** A system with more equations than variables has no solution for some choice of the constant terms. Proof: $n<m$, so $T$ is not surjective by 3.24 (p. 65). Example: five equations, four variables (p. 65).
- The author notes that 3.26 and 3.28 can also be proved by Gaussian elimination, and that the abstract approach "seems to provide cleaner proofs" (p. 65, margin).

*Intuition note.* Counting dimensions replaces solving. With more unknowns than equations, some direction of input must be crushed to 0. With more equations than unknowns, the outputs cannot fill the whole target.

**Exercises 3B** (p. 66–68) are listed below.

## Toy example (ours, not from the text)
Take $T:\mathbf R^3\to\mathbf R^2$, $T(x,y,z)=(x+y,\ y+z)$.
- Null space: $x+y=0$ and $y+z=0$ give $x=-y$, $z=-y$. So $\operatorname{null}T=\{y(-1,1,-1)\}$ and $\dim\operatorname{null}T=1$. Check: $T(-1,1,-1)=(-1+1,\,1-1)=(0,0)$.
- Basis $u_1=(-1,1,-1)$ of the null space. Extend with $v_1=(1,0,0)$, $v_2=(0,1,0)$. These are independent: $a u_1+bv_1+cv_2=(-a+b,\ a+c,\ -a)=0$ forces $a=0$, then $b=0$, $c=0$. So this is a basis of $\mathbf R^3$.
- As in the proof of 3.21: $Tv_1=(1,0)$ and $Tv_2=(1,1)$. They are independent and span $\mathbf R^2$ (e.g. $(0,1)=Tv_2-Tv_1$). So $\dim\operatorname{range}T=2$.
- Check: $\dim V=3=1+2$. Since $3>2$, $T$ cannot be injective (3.22), as seen from the nonzero null vector. As a system, $x+y=0,\ y+z=0$ (2 equations, 3 variables) has nonzero solutions (3.26).

## Concepts
- [[linear map / transformation]] — function $T:V\to W$ with additivity and homogeneity; Axler writes $Tv$ and calls $\mathcal L(V,W)$ the set of them (p. 52)
- [[linear map lemma]] (new) — prescribe images of a basis; exactly one linear map has them (p. 54)
- [[vector space of linear maps]] (new) — $\mathcal L(V,W)$ with pointwise sum and scalar multiple (p. 55)
- [[matrix multiplication as composition]] — here the product $ST$ of linear maps means "do $T$, then $S$"; no matrices yet (p. 55)
- [[null space (kernel)]] — $\{v: Tv=0\}$, a subspace of the domain (p. 59)
- [[column space (range)]] — here the range of any linear map $T$: all outputs $Tv$, a subspace of the target (p. 61); no matrices yet
- [[injective]] (new) — distinct inputs give distinct outputs; for linear maps iff null space is $\{0\}$ (p. 60)
- [[surjective]] (new) — range equals the target space $W$; depends on the chosen $W$ (p. 62)
- [[rank–nullity (Fundamental Theorem of Linear Maps)]] — $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ for finite-dimensional $V$ (p. 62)
- [[homogeneous system of linear equations]] (new) — all constant terms 0; recast as $\operatorname{null}T$ for $T$ in 3.25 (p. 64)
- [[basis]], [[dimension]], [[span]], [[linear independence]] — used throughout the proofs (p. 54, 62–63)

## Canonical instances
- [[differentiation-map]] — linear; null space = constants; surjective on $\mathcal P(\mathbf R)$; not surjective on $\mathcal P_5$ to itself (p. 53, 59, 61–62)
- [[multiplication-by-x-squared]] — injective, null space $\{0\}$; does not commute with differentiation (p. 56, 59)
- [[backward-shift]] — null space $\{(a,0,0,\dots)\}$ (p. 59)
- [[noncommuting-linear-maps-TD-DT]] — $TD\neq DT$ (p. 56)
- [[underdetermined-linear-system]] — 4 equations, 5 variables: nonzero solutions (p. 65)
- [[overdetermined-linear-system]] — 5 equations, 4 variables: unsolvable for some constants (p. 65)

## Bridges (candidates)
- [same-math] Fundamental theorem of linear maps ↔ linear-algebra spine: rank–nullity $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ — same statement, stated without matrices.
- [same-math] 3.25 map $\mathbf F^n\to\mathbf F^m$ ↔ matrix–vector product $Ax$ — the coefficient array $A_{j,k}$ is the matrix (matrix introduced later in the chapter).
- [structural-analogy] Null space of $T$ ↔ lost information: inputs that look identical after the map.
- [metaphor] Gaussian elimination vs. dimension counting — the author offers the abstract proof as a cleaner alternative to elimination (p. 65).

## Questions this raises
- When $\dim V=\dim W$, does injectivity imply surjectivity? (The chapter intro hints at this for maps from a space to itself, p. 51.)
- Is every linear map between finite-dimensional spaces captured by an array of numbers, as $\mathbf F^n\to\mathbf F^m$ suggests (p. 53)?
- What happens to 3.21 when $V$ is infinite-dimensional, e.g. differentiation on $\mathcal P(\mathbf R)$?
- For which maps does a left or right inverse exist? (Exercises 3B.19–20 point at this.)

## Exercises worth doing
- Ex. 3A.1 (p. 57) — shows how a constant term or nonlinear term breaks linearity ($b=c=0$) — difficulty: easy
- Ex. 3A.3 (p. 57) — proves every $T\in\mathcal L(\mathbf F^n,\mathbf F^m)$ has the coefficient form in 3.3 — difficulty: medium
- Ex. 3A.8 and 3A.9 (p. 57) — homogeneity alone, or additivity alone, does not give linearity — difficulty: medium
- Ex. 3B.2 (p. 66) — range inside null space implies $(ST)^2=0$ — difficulty: easy
- Ex. 3B.12–14 (p. 66) — use the fundamental theorem to prove surjectivity or non-existence from a prescribed null space — difficulty: medium
- Ex. 3B.19–20 (p. 67) — injective iff left inverse $ST=I$; surjective iff right inverse $TS=I$ — difficulty: hard

## Reading notes
- This part starts at the Chapter 3 opening (printed p. 51) and ends with Exercises 3B (printed p. 68). Sections 3A and 3B are complete; later sections of Chapter 3 are in other parts.
- Page offset: printed = pdf − 14.
- The text layer shows math letters as unreadable glyphs; all formulas were checked against the page images.
- Exercises 3B.22 and 3B.23 as printed state only that $U$ and $V$ are finite-dimensional (with $S\in\mathcal L(V,W)$); the finite-dimensionality of $W$ is not mentioned there.
- Proofs of 3.6, 3.8 and Exercises are not given in the source (left to the reader); none is solved here.
