---
id: axler-2024-ladr/ch03-linear-p3
work: axler-2024-ladr
unit: "3 Linear Maps (part 3/3): 3E Products and Quotients of Vector Spaces; 3F Duality"
pages: 96-118
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
# Products, Quotients and Duality (Axler, LADR 4e, §3E–3F)

## L0 — One line
Products, quotients V/U and the dual space V′ are new vector spaces built from old ones. Several of their dimensions are computed with the fundamental theorem of linear maps, and the dual map T′ has, in dual bases, the transpose of the matrix of T as its matrix.

## L1 — The gist (≤ 120 words)
How can we build new vector spaces from old ones, and how does a space relate to the linear maps from it into its scalar field? The unit defines products, quotients V/U (sets of translates of U), and the dual space V′ of linear functionals. Main results: dimensions add for products; dim V/U = dim V − dim U; dim U⁰ = dim V − dim U. The dual map T′ has null space (range T)⁰ and range (null T)⁰. Its matrix is the transpose of the matrix of T, which gives a second proof that column rank equals row rank.

**Prerequisites:** vector space, subspace, linear map, null space and range, fundamental theorem of linear maps (dim V = dim null T + dim range T), basis, isomorphism, matrix of a linear map, direct sum.

## L2 — Key ideas
- The product V₁×⋯×V_m is a vector space with slot-wise operations, and dim(V₁×⋯×V_m) = Σ dim V_k. (pp. 96–97)
- A sum V₁+⋯+V_m is direct iff the map Γ(v₁,…,v_m)=v₁+⋯+v_m is injective. For finite-dimensional V this holds iff dimensions add. (p. 98)
- The quotient space V/U is the set of translates v+U. Two translates are equal or disjoint, and the operations are well defined because of this. (pp. 99–101)
- dim V/U = dim V − dim U, via the quotient map π (null π = U, range π = V/U). (p. 102)
- T̃ : V/(null T) → W is injective and has the same range as T. So V/(null T) ≅ range T. (p. 102)
- V′ = ℒ(V,𝐅) has dim V′ = dim V when V is finite-dimensional. For finite-dimensional V, the dual basis φ₁,…,φ_n of a basis v₁,…,v_n is a basis of V′ and gives the coefficients of a vector. (pp. 105–107)
- The dual map T′(φ)=φ∘T is linear, and (ST)′ = T′S′ (order reverses). (pp. 107–108)
- The annihilator U⁰ ⊆ V′ is the set of functionals that vanish on every vector of U. It is a subspace, and for finite-dimensional V, dim U⁰ = dim V − dim U. For finite-dimensional V and W it gives null T′ = (range T)⁰ and range T′ = (null T)⁰. Hence, for finite-dimensional V and W, T surjective ⟺ T′ injective, and T injective ⟺ T′ surjective. (pp. 109–113)
- ℳ(T′) = (ℳ(T))ᵗ in dual bases, and this gives a duality proof that column rank = row rank. (pp. 113–114)

## L3 — Walkthrough

### 3E Products and Quotients of Vector Spaces

**Products of vector spaces.** All spaces are over the same field 𝐅 (p. 96).

**3.87 Definition (product).** For vector spaces V₁,…,V_m over 𝐅:
- $V_1\times\cdots\times V_m=\{(v_1,\dots,v_m): v_1\in V_1,\dots,v_m\in V_m\}$;
- $(u_1,\dots,u_m)+(v_1,\dots,v_m)=(u_1+v_1,\dots,u_m+v_m)$;
- $\lambda(v_1,\dots,v_m)=(\lambda v_1,\dots,\lambda v_m)$. (p. 96)

**3.88 Example.** In 𝒫₅(𝐑)×𝐑³: $(5-6x+4x^2,(3,8,7))+(x+9x^5,(2,2,2))=(5-5x+4x^2+9x^5,(5,10,9))$. Also $2(5-6x+4x^2,(3,8,7))=(10-12x+8x^2,(6,16,14))$. (p. 96)

**3.89.** The product is a vector space over 𝐅 (proof left to reader). Its additive identity is (0,…,0), with the 0 in slot k the zero of V_k. The additive inverse of (v₁,…,v_m) is (−v₁,…,−v_m). (p. 96)

**3.90 Example.** 𝐑²×𝐑³ ≠ 𝐑⁵: elements of 𝐑²×𝐑³ are lists of length two, ((x₁,x₂),(x₃,x₄,x₅)), but elements of 𝐑⁵ are lists of length five. The map ((x₁,x₂),(x₃,x₄,x₅)) ↦ (x₁,…,x₅) is an isomorphism, so the spaces are isomorphic. The author calls this a "relabeling". (p. 97)

**3.91 Example.** In 𝒫₂(𝐑)×𝐑², the list (1,(0,0)), (x,(0,0)), (x²,(0,0)), (0,(1,0)), (0,(0,1)) is linearly independent and spans, so it is a basis. (p. 97)

**3.92 Dimension of a product.** If V₁,…,V_m are finite-dimensional, then V₁×⋯×V_m is finite-dimensional and
$$\dim(V_1\times\cdots\times V_m)=\dim V_1+\cdots+\dim V_m.$$
*Proof.* Choose a basis of each V_k. For each basis vector of V_k, take the element of the product equal to that vector in slot k and 0 elsewhere. This list is independent and spans, so it is a basis. Its length is Σ dim V_k. (p. 97)

*Intuition note.* A product just stacks independent copies of the spaces side by side. So the "degrees of freedom" add.

**3.93 Products and direct sums.** Let V₁,…,V_m be subspaces of V. Define the linear map $\Gamma: V_1\times\cdots\times V_m\to V_1+\cdots+V_m$ by $\Gamma(v_1,\dots,v_m)=v_1+\cdots+v_m$. Then V₁+⋯+V_m is a direct sum iff Γ is injective.
*Proof.* By 3.15, Γ is injective iff the only way to write 0 = v₁+⋯+v_m with v_k ∈ V_k is with every v_k = 0. By 1.45 that is exactly the direct-sum condition. Γ is surjective by the definition of the sum, so "injective" could be replaced by "invertible". (p. 98)

**3.94 Direct sum iff dimensions add.** If V is finite-dimensional and V₁,…,V_m are subspaces, then V₁+⋯+V_m is a direct sum iff $\dim(V_1+\cdots+V_m)=\dim V_1+\cdots+\dim V_m$.
*Proof.* Γ is surjective. By the fundamental theorem (3.21), Γ is injective iff $\dim(V_1+\cdots+V_m)=\dim(V_1\times\cdots\times V_m)$. Combine with 3.93 and 3.92. For m = 2, the author notes an alternative proof via 1.46 and 2.43. (p. 98)

*Intuition note.* Γ adds up the pieces. It loses no information (is injective) exactly when no dimension is wasted by overlap.

**Quotient spaces.**

**3.95 Notation.** For v ∈ V and U ⊆ V: $v+U=\{v+u: u\in U\}$. (p. 98)

**3.96 Example.** Let U = {(x,2x): x ∈ 𝐑}, the line of slope 2 through the origin. Then (17,20)+U is the line of slope 2 through (17,20). Since (10,20) ∈ U and (17,20) ∈ (17,20)+U, it is U moved 7 units to the right. (p. 99)

**3.97 Definition.** For v ∈ V and U a subset of V, v+U is a *translate* of U. (p. 99)

**3.98 Examples.** For the slope-2 line U in 𝐑², its translates are all lines of slope 2. For any line U in 𝐑², its translates are all lines parallel to U. If U={(x,y,0)}, its translates are the planes parallel to the xy-plane. For any plane U in 𝐑³, its translates are all planes parallel to U. (p. 99)

**3.99 Definition (quotient space).** For U a subspace of V, $V/U=\{v+U: v\in V\}$, the set of all translates of U. (p. 99)

**3.100 Examples.** For U the slope-2 line, 𝐑²/U is the set of all lines of slope 2. If U is a line through the origin in 𝐑³, 𝐑³/U is the set of lines parallel to U. If U is a plane through the origin in 𝐑³, 𝐑³/U is the set of planes parallel to U. (p. 100)

**3.101 Two translates are equal or disjoint.** For U a subspace of V and v, w ∈ V:
$$v-w\in U\iff v+U=w+U\iff (v+U)\cap(w+U)\neq\emptyset.$$
*Proof.*
1. Suppose v − w ∈ U. For u ∈ U, $v+u=w+((v-w)+u)\in w+U$, so v+U ⊆ w+U. Similarly w+U ⊆ v+U. Hence v+U = w+U.
2. Equality of the translates implies a nonempty intersection.
3. Suppose the intersection is nonempty. Then there are u₁,u₂ ∈ U with $v+u_1=w+u_2$. So $v-w=u_2-u_1\in U$. (p. 100)

**3.102 Definition (operations on V/U).** $(v+U)+(w+U)=(v+w)+U$ and $\lambda(v+U)=(\lambda v)+U$ for all v, w ∈ V and λ ∈ 𝐅. (p. 100)

**3.103 V/U is a vector space.**
*Proof (well-definedness).* The issue is that a translate has many representations. Suppose $v_1+U=v_2+U$ and $w_1+U=w_2+U$.
1. By 3.101, $v_1-v_2\in U$ and $w_1-w_2\in U$.
2. U is closed under addition, so $(v_1-v_2)+(w_1-w_2)\in U$, i.e. $(v_1+w_1)-(v_2+w_2)\in U$.
3. By 3.101, $(v_1+w_1)+U=(v_2+w_2)+U$. So addition makes sense.
4. For λ ∈ 𝐅, $\lambda(v_1-v_2)\in U$ since U is closed under scalar multiplication, i.e. $\lambda v_1-\lambda v_2\in U$. By 3.101, $(\lambda v_1)+U=(\lambda v_2)+U$.
The vector-space axioms are left to the reader. The additive identity is 0+U (which equals U), and the additive inverse of v+U is (−v)+U. (p. 101)

**3.104 Definition (quotient map).** $\pi:V\to V/U$, $\pi(v)=v+U$. It is linear (reader verifies). (p. 101)

**3.105 Dimension of quotient space.** If V is finite-dimensional and U is a subspace, $\dim V/U=\dim V-\dim U$.
*Proof.* For v ∈ V, v+U = 0+U iff v ∈ U (by 3.101), so null π = U. Also range π = V/U. The fundamental theorem gives dim V = dim U + dim V/U. (p. 102)

*Intuition note.* V/U "collapses" U to a point. Each U-direction disappears, so dim U dimensions are removed.

**3.106 Notation T̃.** For T ∈ ℒ(V,W), define $\tilde T: V/(\operatorname{null}T)\to W$ by $\tilde T(v+\operatorname{null}T)=Tv$. It is well defined: if u + null T = v + null T, then u − v ∈ null T by 3.101. So T(u−v)=0 and Tu = Tv. Linearity is left to the reader. (p. 102)

**3.107 Null space and range of T̃.** For T ∈ ℒ(V,W):
- (a) T̃∘π = T, where π is the quotient map onto V/(null T). Check: (T̃∘π)(v) = T̃(v+null T) = Tv.
- (b) T̃ is injective. If T̃(v+null T)=0, then Tv=0, so v ∈ null T, so v+null T = 0+null T by 3.101. Hence null T̃ = {0+null T}.
- (c) range T̃ = range T, by the definition of T̃.
- (d) V/(null T) and range T are isomorphic: by (b) and (c), T̃ is an isomorphism onto range T. (p. 102)

*Intuition note.* T cannot tell apart inputs that differ by an element of null T. T̃ is T after identifying such inputs, and then nothing is lost.

**Exercises 3E** (pp. 103–104) are listed under "Exercises worth doing".

### 3F Duality

**Dual space and dual map.**

**3.108 Definition.** A *linear functional* on V is a linear map from V to 𝐅, i.e. an element of ℒ(V,𝐅). (p. 105)

**3.109 Examples.** φ(x,y,z)=4x−5y+2z on 𝐑³. φ(x₁,…,x_n)=c₁x₁+⋯+c_nx_n on 𝐅ⁿ for fixed c's. φ(p)=3p″(5)+7p(4) on 𝒫(𝐑). φ(p)=∫₀¹ p on 𝒫(𝐑). (p. 105)

**3.110 Definition (dual space).** $V'=\mathcal L(V,\mathbf F)$, the vector space of all linear functionals on V. (p. 105)

**3.111.** If V is finite-dimensional, so is V′, and $\dim V'=\dim V$.
*Proof.* By 3.72, $\dim V'=\dim\mathcal L(V,\mathbf F)=(\dim V)(\dim\mathbf F)=\dim V$. (p. 105)

**3.112 Definition (dual basis).** For a basis v₁,…,v_n of V, the dual basis is φ₁,…,φ_n in V′, where φ_j is the linear functional with
$$\varphi_j(v_k)=\begin{cases}1 & k=j,\\ 0 & k\ne j.\end{cases}$$
Each φ_j is well defined by the linear map lemma (3.4). (p. 106)

**3.113 Example.** On 𝐅ⁿ let φ_j(x₁,…,x_n)=x_j, the j-th coordinate. For the standard basis e₁,…,e_n, φ_j(e_k)=1 if k=j and 0 otherwise. So φ₁,…,φ_n is the dual basis of the standard basis. (p. 106)

**3.114 Dual basis gives coefficients.** If v₁,…,v_n is a basis of V and φ₁,…,φ_n its dual basis, then for each v ∈ V:
$$v=\varphi_1(v)v_1+\cdots+\varphi_n(v)v_n.$$
*Proof.* Write $v=c_1v_1+\cdots+c_nv_n$ (3.115). Applying φ_j gives φ_j(v)=c_j. Substitute into 3.115. (p. 106)

**3.116 The dual basis is a basis of V′** (V finite-dimensional).
*Proof.* Suppose $a_1\varphi_1+\cdots+a_n\varphi_n=0$ (3.117). Evaluating at v_k gives $(a_1\varphi_1+\cdots+a_n\varphi_n)(v_k)=a_k$, so every a_k = 0. Thus the list is independent. It has length n = dim V′ (3.111), so it is a basis (2.38). (p. 107)

*Intuition note.* φ_j reads off the j-th coordinate of a vector in the basis v₁,…,v_n. Reading off all n coordinates is enough to describe every linear functional.

**3.118 Definition (dual map).** For T ∈ ℒ(V,W), the dual map is $T'\in\mathcal L(W',V')$, defined for φ ∈ W′ by $T'(\varphi)=\varphi\circ T$. This lies in V′ because it is a linear map V → 𝐅. T′ is linear:
- $T'(\varphi+\psi)=(\varphi+\psi)\circ T=\varphi\circ T+\psi\circ T=T'(\varphi)+T'(\psi)$;
- $T'(\lambda\varphi)=(\lambda\varphi)\circ T=\lambda(\varphi\circ T)=\lambda T'(\varphi)$. (p. 107)

The prime has two unrelated meanings in the next example: D′ is a dual map, p′ is a derivative (p. 107).

**3.119 Example.** Let D: 𝒫(𝐑)→𝒫(𝐑), Dp = p′.
- If φ(p)=p(3), then $(D'(\varphi))(p)=\varphi(Dp)=\varphi(p')=p'(3)$.
- If φ(p)=∫₀¹ p, then $(D'(\varphi))(p)=\varphi(p')=\int_0^1p'=p(1)-p(0)$. (p. 108)

**3.120 Algebraic properties of dual maps.** For T ∈ ℒ(V,W):
- (a) (S+T)′ = S′+T′ for S ∈ ℒ(V,W);
- (b) (λT)′ = λT′ for λ ∈ 𝐅;
- (c) (ST)′ = T′S′ for S ∈ ℒ(W,U).
(a), (b) are left to the reader. For (c), take φ ∈ U′:
$$(ST)'(\varphi)=\varphi\circ(ST)=(\varphi\circ S)\circ T=T'(\varphi\circ S)=T'(S'(\varphi))=(T'S')(\varphi).$$
The 1st, 3rd and 4th equalities use the definition of the dual map, and the 2nd uses associativity of composition. (p. 108) The order reverses in (c). The author reserves T* for the adjoint (Chapter 7) rather than for duality (p. 108).

*Intuition note.* T′ takes a "measurement" φ on W and pulls it back to a measurement on V. Pulling back through ST means first through S, then through T, so the order flips.

**Null space and range of the dual map.**

**3.121 Definition (annihilator).** For U ⊆ V, $U^0=\{\varphi\in V': \varphi(u)=0 \text{ for all } u\in U\}$. (p. 109) U⁰ depends on the containing space V, which the author says is always clear from context (p. 109).

**3.122 Example.** If U is the set of polynomial multiples of x² and φ(p)=p′(0), then φ ∈ U⁰. (p. 109)

**3.123 Example.** In 𝐑⁵, with standard basis e₁,…,e₅ and dual basis φ₁,…,φ₅, let U = span(e₁,e₂). Claim: U⁰ = span(φ₃,φ₄,φ₅).
- (⊇) If φ = c₃φ₃+c₄φ₄+c₅φ₅ and (x₁,x₂,0,0,0) ∈ U, then φ(x₁,x₂,0,0,0)=0.
- (⊆) If φ ∈ U⁰, write φ = c₁φ₁+⋯+c₅φ₅ (the dual basis is a basis). Then 0=φ(e₁)=c₁ and 0=φ(e₂)=c₂. So φ ∈ span(φ₃,φ₄,φ₅). (p. 109)

**3.124 The annihilator is a subspace of V′.** The zero functional kills every u ∈ U. If φ, ψ ∈ U⁰ and u ∈ U, then (φ+ψ)(u)=0+0=0. Closure under scalar multiplication is similar. Apply 1.34. (p. 110)

**3.125 Dimension of the annihilator.** If V is finite-dimensional and U is a subspace, $\dim U^0=\dim V-\dim U$.
*Proof.*
1. Let $i\in\mathcal L(U,V)$ be the inclusion map, i(u)=u. Then $i'\in\mathcal L(V',U')$.
2. The fundamental theorem applied to i′ gives $\dim\operatorname{range}i'+\dim\operatorname{null}i'=\dim V'$.
3. null i′ = U⁰ ("by thinking about the definitions"), and dim V′ = dim V (3.111). So
$$\dim\operatorname{range}i'+\dim U^0=\dim V.\tag{3.126}$$
4. If φ ∈ U′, then φ extends to a linear functional ψ on V (the text cites Exercise 13 in Section 3A). By definition of i′, i′(ψ)=φ. So range i′ = U′.
5. Hence dim range i′ = dim U′ = dim U, and 3.126 becomes dim U + dim U⁰ = dim V. (p. 110)

The author also outlines an alternative proof: extend a basis of U to a basis of V, take the dual basis, and show that the last dual-basis vectors form a basis of U⁰. He says the reader should construct it (p. 110).

*Intuition note.* For a 2-dimensional U in 𝐑⁵, U⁰ is 3-dimensional (as in 3.123). The functionals that vanish on U are exactly the ones that depend only on the 3 remaining coordinates (3.123).

**3.127 When the annihilator is {0} or everything.** For V finite-dimensional and U a subspace:
- (a) U⁰ = {0} ⟺ U = V;
- (b) U⁰ = V′ ⟺ U = {0}.
*Proof of (a).* U⁰={0} ⟺ dim U⁰=0 ⟺ dim U = dim V (3.125) ⟺ U = V (2.39).
*Proof of (b).* U⁰=V′ ⟺ dim U⁰ = dim V′ (one direction by 2.39) ⟺ dim U⁰ = dim V (3.111) ⟺ dim U = 0 (3.125) ⟺ U={0}. (p. 111)

**3.128 Null space of T′.** For V, W finite-dimensional and T ∈ ℒ(V,W):
- (a) null T′ = (range T)⁰;
- (b) dim null T′ = dim null T + dim W − dim V.
*Proof of (a)* (this part does not use finite-dimensionality, as the author notes, p. 111). If φ ∈ null T′, then 0 = T′(φ) = φ∘T. So φ(Tv)=0 for every v ∈ V, so φ ∈ (range T)⁰. Conversely, if φ ∈ (range T)⁰, then φ(Tv)=0 for all v, so φ∘T=0=T′(φ). (p. 111)
*Proof of (b).*
$$\dim\operatorname{null}T'=\dim(\operatorname{range}T)^0=\dim W-\dim\operatorname{range}T=\dim W-(\dim V-\dim\operatorname{null}T)=\dim\operatorname{null}T+\dim W-\dim V.$$
The reasons, in order, are (a), 3.125, and the fundamental theorem 3.21. (p. 112)

**3.129 T surjective ⟺ T′ injective** (V, W finite-dimensional):
range T = W ⟺ (range T)⁰ = {0} (3.127(a)) ⟺ null T′ = {0} (3.128(a)) ⟺ T′ injective. (p. 112)

**3.130 Range of T′.** For V, W finite-dimensional:
- (a) dim range T′ = dim range T. Proof: $\dim\operatorname{range}T'=\dim W'-\dim\operatorname{null}T'=\dim W-\dim(\operatorname{range}T)^0=\dim\operatorname{range}T$, using 3.21, then 3.111 and 3.128(a), then 3.125. (p. 112)
- (b) range T′ = (null T)⁰. Proof: if φ = T′(ψ) and v ∈ null T, then $\varphi(v)=\psi(Tv)=\psi(0)=0$. So range T′ ⊆ (null T)⁰. Equal dimensions finish the proof: $\dim\operatorname{range}T'=\dim\operatorname{range}T=\dim V-\dim\operatorname{null}T=\dim(\operatorname{null}T)^0$, using (a), 3.21, 3.125. (p. 113)

**3.131 T injective ⟺ T′ surjective** (V, W finite-dimensional):
null T={0} ⟺ (null T)⁰=V′ (3.127(b)) ⟺ range T′=V′ (3.130(b)). (p. 113)

*Intuition note.* T and T′ mirror each other. T′ sends to zero exactly the functionals that vanish on range T, and the functionals that T′ produces are exactly those that vanish on null T. Surjective and injective swap roles.

**Matrix of the dual of a linear map.**

**3.132.** Take a basis v₁,…,v_n of V with dual basis φ₁,…,φ_n of V′, and a basis w₁,…,w_m of W with dual basis ψ₁,…,ψ_m of W′. Then ℳ(T) is taken in the first pair, and ℳ(T′) in the dual bases. For V, W finite-dimensional and T ∈ ℒ(V,W):
$$\mathcal M(T')=(\mathcal M(T))^{\mathrm t}.$$
*Shapes.* A = ℳ(T) is m×n, and C = ℳ(T′) is n×m.
*Proof.* Let A = ℳ(T), C = ℳ(T′), 1 ≤ j ≤ m, 1 ≤ k ≤ n.
1. By definition of ℳ(T′): $T'(\psi_j)=\sum_{r=1}^nC_{r,j}\varphi_r$. The left side is ψ_j∘T.
2. Apply both sides to v_k: $(\psi_j\circ T)(v_k)=\sum_rC_{r,j}\varphi_r(v_k)=C_{k,j}$.
3. Also $(\psi_j\circ T)(v_k)=\psi_j(Tv_k)=\psi_j\big(\sum_{r=1}^mA_{r,k}w_r\big)=\sum_rA_{r,k}\psi_j(w_r)=A_{j,k}$.
4. So $C_{k,j}=A_{j,k}$, i.e. C = Aᵗ. (pp. 113–114)

**3.133 Column rank equals row rank.** For A ∈ 𝐅^{m,n}, the column rank of A equals its row rank (alternative to 3.57).
*Proof.* Define T: 𝐅^{n,1}→𝐅^{m,1} by Tx = Ax, so ℳ(T)=A in the standard bases. Then
$$\text{col rank }A=\text{col rank }\mathcal M(T)=\dim\operatorname{range}T=\dim\operatorname{range}T'=\text{col rank }\mathcal M(T')=\text{col rank }A^{\mathrm t}=\text{row rank }A.$$
The reasons are, in order: 3.78 (twice, for steps 2 and 4), 3.130(a) (step 3), 3.132 (step 5), and the definitions of row and column rank (last step). Another proof is in Exercise 8 of Section 7A (p. 114). (p. 114)

*Intuition note.* The dual map has the same range dimension as T, and in coordinates it is the transpose. So the number of independent columns of A equals the number of independent columns of Aᵗ, which is the number of independent rows of A.

**Exercises 3F** (pp. 115–118) are listed under "Exercises worth doing".

## Toy example (ours, not from the text)
Let T: 𝐑²→𝐑², T(x,y) = (x+y, 2x+2y). Standard bases; ℳ(T) = A = [[1,1],[2,2]]. Let ψ₁,ψ₂ be the dual basis on the codomain and φ₁,φ₂ the dual basis on the domain.

- *Null space and range.* null T = {(x,y): x+y=0} = span((1,−1)) =: U. range T = span((1,2)).
- *Quotient.* dim 𝐑²/U = 2 − 1 = 1 (3.105). T̃((1,0)+U) = T(1,0) = (1,2). The translate (1,0)+U is the line x+y=1. T̃ sends every point of that line to (1,2): T(0,1)=(1,2) too, and (0,1)−(1,0)=(−1,1) ∈ U. T̃ is injective with image range T, so 𝐑²/U ≅ range T (3.107).
- *Dual map.* T′(ψ₁)=ψ₁∘T=(x,y)↦x+y, i.e. φ₁+φ₂. T′(ψ₂)=ψ₂∘T=(x,y)↦2x+2y, i.e. 2φ₁+2φ₂. Column j of ℳ(T′) holds the coefficients of T′(ψ_j): ℳ(T′)=[[1,2],[1,2]]. This equals Aᵗ = [[1,2],[1,2]] ✓ (3.132).
- *Range of T′.* range T′ = span(φ₁+φ₂), of dimension 1 = dim range T ✓ (3.130(a)). A functional aφ₁+bφ₂ kills (1,−1) iff a−b=0, i.e. a=b. So range T′ = (null T)⁰ ✓ (3.130(b)).
- *Null space of T′.* aψ₁+bψ₂ ∈ null T′ iff a(x+y)+b(2x+2y)=0 for all x,y, iff a+2b=0, so null T′ = span(2ψ₁−ψ₂). Also (range T)⁰ = {aψ₁+bψ₂ : a·1+b·2=0}, the same set ✓ (3.128(a)). The dimension is 1 = dim null T + dim W − dim V = 1+2−2 ✓.
- Neither T nor T′ is injective or surjective, consistent with 3.129 and 3.131.

## Concepts
- [[product-of-vector-spaces]] (new) — set of tuples with slot-wise addition and scaling; dim is the sum of dims (pp. 96–97)
- [[direct-sum]] (new) — V₁+⋯+V_m is direct iff Γ is injective, iff dims add (p. 98)
- [[translate]] (new) — a set v+U for a vector v and a subset U (p. 99)
- [[quotient-space]] (new) — V/U, the vector space of translates of U (pp. 99–101)
- [[quotient-map]] (new) — π(v)=v+U; linear, null π = U, range π = V/U (p. 101)
- [[rank–nullity (Fundamental Theorem of Linear Maps)]] — the repeated tool: dim V = dim null T + dim range T (p. 102, used throughout)
- [[null space (kernel)]] and [[column space (range)]] — null T′ = (range T)⁰ and range T′ = (null T)⁰ (pp. 111–113)
- [[linear-functional]] (new) — a linear map V → 𝐅 (p. 105)
- [[dual-space]] (new) — V′ = ℒ(V,𝐅), with dim V′ = dim V (p. 105)
- [[dual-basis]] (new) — φ_j(v_k)=1 if j=k and 0 otherwise; reads off coordinates (p. 106)
- [[dual-map]] (new) — T′(φ)=φ∘T, a map W′→V′; (ST)′=T′S′ (p. 107)
- [[annihilator]] (new) — U⁰, the functionals vanishing on U; dim U⁰ = dim V − dim U (pp. 109–110)
- [[matrix as transformation]] — here ℳ(T′) is ℳ(T)ᵗ in dual bases (p. 113)
- [[rank]] — column rank equals row rank, reproved by duality (p. 114)

## Canonical instances
- [[R2xR3-vs-R5]] (new) — isomorphic but not equal spaces; "relabeling" (p. 97)
- [[lines-parallel-to-U-quotient]] (new) — 𝐑²/U is the set of lines of slope 2 (pp. 99–100)
- [[derivative-dual-map]] (new) — D′ for D p = p′: evaluation at 3 goes to p′(3), and ∫₀¹ goes to p(1)−p(0) (p. 108)
- [[annihilator-of-span-e1-e2]] (new) — U⁰ = span(φ₃,φ₄,φ₅) in (𝐑⁵)′ (p. 109)

## Bridges (candidates)
- [structural-analogy] V/U (collapsing a subspace to zero) ↔ linear-algebra: null space of a map. T̃ identifies V/(null T) with range T, a "first isomorphism" pattern.
- [same-math] ℳ(T′)=ℳ(T)ᵗ ↔ linear-algebra: transpose matrix Aᵗ acting on row vectors. The dual map is the coordinate-free transpose.
- [structural-analogy] Dual basis as coordinate functionals ↔ statistics/data: a regression coefficient or weight vector as a linear readout of a feature vector.
- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product).

## Questions this raises
- The text notes that finding an isomorphism V → V′ generally requires choosing a basis (Exercise 32 note, p. 118). What extra structure (an inner product, Chapter 7) makes it natural?
- Is the quotient V/U always isomorphic to a complement of U (see Exercises 13–15, 18)? Does it need V to be finite-dimensional?
- How do the adjoint T* (Chapter 7) and the dual map T′ relate when V has an inner product?
- Can duality prove other rank facts, such as rank(ST) ≤ min(rank S, rank T), more quickly?

## Exercises worth doing
- Ex. 3E.1 (p. 103) — a function T is linear iff its graph is a subspace of V×W — difficulty: easy
- Ex. 3E.8 (p. 103) — solution sets of Tx=c are empty or translates of null T; applies to linear systems — difficulty: medium
- Ex. 3E.13 (p. 104) — V ≅ U×(V/U) when V/U is finite-dimensional — difficulty: hard

- Ex. 3F.14 (p. 116) — compute T′ on dual basis vectors for a concrete T: 𝐑³→𝐑² — difficulty: easy
- Ex. 3F.22 (p. 117) — (U+W)⁰ = U⁰∩W⁰ and (U∩W)⁰ = U⁰+W⁰ — difficulty: medium
- Ex. 3F.32 (p. 118) — the double dual V″ is naturally isomorphic to V when V is finite-dimensional — difficulty: hard

## Reading notes
- This unit starts at §3E (printed p. 96) and ends at the end of the exercises of §3F (printed p. 118); the split is at a section boundary. The earlier parts of Chapter 3 are not covered, and references such as 3.4, 3.15, 3.21, 3.57, 3.72, 3.78, 1.34, 1.45, 1.46, 2.38, 2.39, 2.43 point to material outside these pages.
- Page offset: printed page = PDF page − 14 (PDF page 110 = printed page 96).
- The extracted text layer garbles math letters, so all math was checked against the page images. The images are clear and I found no misprints.
- Every page carries the running footer "Linear Algebra Done Right, fourth edition, by Sheldon Axler".
- The statement in 3.125's proof that null i′ = U⁰ is left to the reader in the source ("as can be seen by thinking about the definitions"), and I did not add a proof. The same holds for the extension lemma, which the source cites as Exercise 13 in Section 3A.
- Exercises are only listed, not solved. The source prints no solutions on these pages.
