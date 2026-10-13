---
id: axler-2024-ladr/ch03-linear-p2
work: axler-2024-ladr
unit: "3 Linear Maps (part 2/3): 3C Matrices and 3D Invertibility and Isomorphisms"
pages: 69-95
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
# Matrices, Invertibility and Isomorphisms (Axler, Ch. 3, Sections 3C–3D)

## L0 — One line
Once bases are fixed, a linear map is a matrix, composition of maps is matrix multiplication, invertible maps are isomorphisms, and the dimension alone decides whether two finite-dimensional spaces are isomorphic.

## L1 — The gist (≤ 120 words)
How can linear maps be recorded as arrays of numbers, and what do the algebra of those arrays and the idea of "undoing" a map tell us? Axler defines the matrix of a map by writing each image vector in the target basis. He then defines matrix operations so that sums, scalar multiples and products of maps match those of matrices. He proves column rank = row rank. He shows a map is invertible iff it is injective and surjective, and that injective ⇔ surjective when the two spaces have equal finite dimension. Finite-dimensional spaces over F are isomorphic iff their dimensions agree. Finally he shows M(Tv) = M(T)M(v) and derives the change-of-basis formula A = C⁻¹BC.

**Prerequisites:** vector spaces, subspaces, bases, dimension; linear maps, null space, range, injective/surjective; the fundamental theorem of linear maps (dim V = dim null T + dim range T); the linear map lemma.

## L2 — Key ideas (5–10 bullets)
- The matrix M(T) has as its k-th column the coordinates of Tv_k in the target basis; it depends on both chosen bases. (p. 69–70)
- Matrix addition and scalar multiplication are defined entrywise so that M(S+T)=M(S)+M(T) and M(λT)=λM(T). F^{m,n} is a vector space of dimension mn. (pp. 71–72)
- Matrix multiplication is defined *so that* M(ST)=M(S)M(T). Equivalent views: entry = row × column; column of AB = A × column; Ab = linear combination of columns of A. (pp. 72–76)
- Column–row factorization A=CR gives column rank = row rank (column rank: dimension of the span of the columns; row rank: the same for the rows), hence a single "rank" of a matrix. (pp. 78–79)
- A linear map is invertible (it has a linear inverse map that undoes it) iff injective and surjective. If dim V = dim W < ∞, injective, surjective and invertible are all equivalent; on infinite-dimensional spaces, Example 3.64 shows that neither injectivity nor surjectivity alone implies invertibility. (pp. 83–84)
- Finite-dimensional spaces over F are isomorphic (joined by an invertible linear map) iff same dimension; M is an isomorphism L(V,W) → F^{m,n}, so dim L(V,W)=(dim V)(dim W). (pp. 86–87)
- M(Tv)=M(T)M(v): every linear map between finite-dimensional spaces acts as matrix multiplication after relabeling by coordinates. dim range T = column rank of M(T). (pp. 88–90)
- Change of basis: if A, B are matrices of T in bases (u), (v) and C=M(I,(u),(v)), then A=C⁻¹BC. (p. 93)

## L3 — Walkthrough

### 3C Matrices

**Representing a linear map by a matrix (pp. 69–70).** By the linear map lemma, the values Tv_1,…,Tv_n on a basis determine T. Matrices record these values efficiently (p. 69).

- **3.29 Matrix.** An m-by-n matrix A is a rectangular array of elements of F with m rows and n columns. A_{j,k} is the entry in row j, column k. First index = row, second = column. Example 3.30: for A = (8 4 5−3i; 1 9 7), A_{2,3}=7 (p. 69).
- **3.31 Matrix of a linear map.** Let T∈L(V,W), v_1,…,v_n a basis of V, w_1,…,w_m a basis of W. M(T) is the m-by-n matrix with entries A_{j,k} defined by
$$Tv_k = A_{1,k}w_1+\cdots+A_{m,k}w_m .$$
If the bases are unclear, write M(T,(v_1,…,v_n),(w_1,…,w_m)). M(T) depends on the two bases as well as on T (p. 69).
- The k-th column of M(T) holds the scalars needed to write Tv_k as a combination of the w_j: $Tv_k=\sum_{j=1}^m A_{j,k}w_j$. If T is a map from an n-dimensional space to an m-dimensional one, M(T) is m-by-n (p. 70).
- For maps F^n → F^m the bases are standard unless stated otherwise. Then column k of M(T) is T applied to the k-th standard basis vector. For P_m(F), use the basis 1, x, …, x^m (p. 70).
- **Example 3.32.** T(x,y)=(x+3y, 2x+5y, 7x+9y). T(1,0)=(1,2,7), T(0,1)=(3,5,9), so M(T) is the 3-by-2 matrix with rows (1 3), (2 5), (7 9) (p. 70).
- **Example 3.33.** D: P_3(R)→P_2(R), Dp=p′. Since (x^k)′=kx^{k−1}, M(D) is the 3-by-4 matrix with rows (0 1 0 0), (0 0 2 0), (0 0 0 3) (p. 70).

*Intuition note.* A matrix is a table of where the basis vectors of the domain go, written in the coordinates of the target. Change the bases and the table changes, though the map does not.

**Addition and scalar multiplication (pp. 71–72).** Assume U, V, W finite-dimensional with chosen bases.

- **3.34 Matrix addition:** add corresponding entries (same size required). **3.36 Scalar multiplication:** multiply every entry by the scalar. Example 3.37: $2\begin{pmatrix}3&1\\-1&5\end{pmatrix}+\begin{pmatrix}4&2\\1&6\end{pmatrix}=\begin{pmatrix}6&2\\-2&10\end{pmatrix}+\begin{pmatrix}4&2\\1&6\end{pmatrix}=\begin{pmatrix}10&4\\-1&16\end{pmatrix}$ (p. 72).
- **3.35:** M(S+T)=M(S)+M(T) for S,T∈L(V,W) (same bases). **3.38:** M(λT)=λM(T). Both are left to the reader (Exercise 3) (pp. 71–72).
- **3.39–3.40.** F^{m,n} denotes the set of all m-by-n matrices over F. With these operations it is a vector space of dimension mn. Proof sketch: the additive identity is the zero matrix; the mn matrices with a single 1 and zeros elsewhere form a basis (p. 72).

**Matrix multiplication (pp. 72–74).** Let T∈L(U,V), S∈L(V,W), with bases u_1,…,u_p of U, v_1,…,v_n of V, w_1,…,w_m of W. Let M(S)=A (m-by-n) and M(T)=B (n-by-p). The author wants M(ST)=M(S)M(T), and derives the needed formula for 1 ≤ k ≤ p (p. 73):
$$
\begin{aligned}
(ST)u_k &= S\Big(\sum_{r=1}^{n}B_{r,k}v_r\Big)=\sum_{r=1}^{n}B_{r,k}\,Sv_r\\
&=\sum_{r=1}^{n}B_{r,k}\sum_{j=1}^{m}A_{j,r}w_j=\sum_{j=1}^{m}\Big(\sum_{r=1}^{n}A_{j,r}B_{r,k}\Big)w_j .
\end{aligned}
$$
So M(ST) is the m-by-p matrix whose row j, column k entry is $\sum_{r}A_{j,r}B_{r,k}$.

- **3.41 Definition.** For A m-by-n and B n-by-p, AB is the m-by-p matrix with
$$(AB)_{j,k}=\sum_{r=1}^{n}A_{j,r}B_{r,k}.$$
It is defined only when the number of columns of A equals the number of rows of B (p. 73).
- **Example 3.42.** $\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}6&5&4&3\\2&1&0&-1\end{pmatrix}=\begin{pmatrix}10&7&4&1\\26&19&12&5\\42&31&20&9\end{pmatrix}$ (p. 73).
- Matrix multiplication is not commutative, even when both products are defined (Exercise 10). It is distributive and associative (Exercises 11, 12) (p. 73).
- **3.43:** M(ST)=M(S)M(T) for T∈L(U,V), S∈L(V,W), with the same basis used for each space throughout. The proof is the calculation above (p. 74).
- **3.44 Notation.** For an m-by-n matrix A: $A_{j,\cdot}$ is row j (a 1-by-n matrix); $A_{\cdot,k}$ is column k (an m-by-1 matrix). Example 3.45 gives $A_{2,\cdot}=(1\ 9\ 7)$ and $A_{\cdot,2}=\binom{4}{9}$ for A=(8 4 5; 1 9 7). A 1-by-1 matrix is often identified with its entry, e.g. $(3\ 4)\binom{6}{2}=26$ (p. 74).
- **3.46 Row times column.** $(AB)_{j,k}=A_{j,\cdot}B_{\cdot,k}$. Proof: the right side is the 1-by-1 matrix whose entry is the sum in 3.47, $A_{j,1}B_{1,k}+\cdots+A_{j,n}B_{n,k}$ (p. 75).
- **3.48 Column of a product.** $(AB)_{\cdot,k}=AB_{\cdot,k}$. Proof: both are m-by-1, and their row-j entries both equal the sum in 3.47 (p. 75).
- **Example 3.49.** $\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\binom{5}{1}=\begin{pmatrix}7\\19\\31\end{pmatrix}=5\begin{pmatrix}1\\3\\5\end{pmatrix}+1\begin{pmatrix}2\\4\\6\end{pmatrix}$ (p. 75).
- **3.50 Linear combination of columns.** For A m-by-n and $b=(b_1,\dots,b_n)^{t}$ an n-by-1 matrix,
$$Ab=b_1A_{\cdot,1}+\cdots+b_nA_{\cdot,n}.$$
Proof: row k of Ab is $A_{k,1}b_1+\cdots+A_{k,n}b_n$, which is also row k of the right side (p. 76).
- Row versions are Exercises 8 and 9: $(AB)_{j,\cdot}=A_{j,\cdot}B$ and $aB=a_1B_{1,\cdot}+\cdots+a_nB_{n,\cdot}$ (pp. 76, 80).
- **3.51.** Let C be m-by-c and R be c-by-n. (a) Column k of CR is a linear combination of the columns of C, with coefficients from column k of R. (b) Row j of CR is a linear combination of the rows of R, with coefficients from row j of C. Proof of (a): column k of CR equals $CR_{\cdot,k}$ (3.48), which by 3.50 is that combination. (b) is the same pattern using Exercises 8 and 9 (p. 76).

*Intuition note.* The product AB is defined to be "do B, then A" in coordinates. Because each column of AB is A applied to a column of B, A always acts by mixing its own columns.

**Column–row factorization and rank (pp. 77–79).**

- **3.52.** The *column rank* of A∈F^{m,n} is the dimension of the span of its columns in F^{m,1}. The *row rank* is the dimension of the span of its rows in F^{1,n}. Both are at most min{m,n} (p. 77).
- **Example 3.53.** For A=(4 7 1 8; 3 5 2 9): the first two columns are not scalar multiples of each other, so the span has dimension ≥ 2. Also dim F^{2,1}=2, so the column rank is 2. The two rows are not multiples of each other, so the row rank is 2 (p. 77).
- **3.54 Transpose.** For A m-by-n, $A^{t}$ is the n-by-m matrix with $(A^{t})_{k,j}=A_{j,k}$. Example 3.55: A=(5 −7; 3 8; −4 2) gives $A^t=(5\ 3\ -4;\ -7\ 8\ 2)$. Stated properties: $(A+B)^t=A^t+B^t$, $(\lambda A)^t=\lambda A^t$, $(AC)^t=C^tA^t$ (Exercises 14, 15) (pp. 77–78).
- **3.56 Column–row factorization.** If A is m-by-n with column rank c ≥ 1, there are an m-by-c matrix C and a c-by-n matrix R with A=CR.
 - Proof. Reduce the list of columns of A to a basis of their span (by 2.30). It has length c. Put these c columns together to form C (m-by-c).
 - Each column k of A is a combination of the columns of C. Use the coefficients as column k of R (c-by-n). Then A=CR by 3.51(a) (p. 78).
- **3.57 Column rank = row rank** for A∈F^{m,n}.
 - Proof. Let c be the column rank. If c=0, then A=0 and the row rank is 0. Otherwise take A=CR as in 3.56.
 - By 3.51(b), every row of A is a combination of the c rows of R. So row rank ≤ c.
 - Apply this to $A^t$: column rank of A = row rank of $A^t$ ≤ column rank of $A^t$ = row rank of A. Hence equality (p. 78).
- **3.58 Rank.** The rank of A is its column rank. The author points to 3.133 and Exercise 8 in Section 7A for other proofs (p. 79).

*Intuition note.* A=CR says every column of A is built from only c "ingredient" columns. Reading the same product by rows shows every row is built from c ingredient rows, so rows cannot give more independent directions than columns.

### 3D Invertibility and Isomorphisms

**Invertible linear maps (pp. 82–85).**

- **3.59.** T∈L(V,W) is *invertible* if there is S∈L(W,V) with ST=I (identity on V) and TS=I (identity on W). Such an S is called an inverse of T (p. 82).
- **3.60 Inverse is unique.** If S_1, S_2 are inverses: $S_1=S_1I=S_1(TS_2)=(S_1T)S_2=IS_2=S_2$. **3.61:** the inverse is written T⁻¹ (p. 82).
- **Example 3.62.** T(x,y,z)=(−y,x,4z) is a 90° counterclockwise rotation in the xy-plane plus a stretch by 4 along the z-axis. Its inverse is T⁻¹(x,y,z)=(y,−x,z/4) (p. 82).
- **3.63 Invertible ⇔ injective and surjective.** Proof (p. 83):
 - (⇒) Assume T invertible. If Tu=Tv, then u=T⁻¹(Tu)=T⁻¹(Tv)=v, so T is injective. For w∈W, w=T(T⁻¹w), so T is surjective.
 - (⇐) Assume T injective and surjective. For w∈W define S(w) as the unique element of V with T(S(w))=w. Then T∘S=I on W.
 - For v∈V: T((S∘T)v)=(T∘S)(Tv)=Tv. By injectivity, (S∘T)v=v.
 - Linearity of S: T(S(w_1)+S(w_2))=w_1+w_2, so by definition of S, S(w_1+w_2)=S(w_1)+S(w_2). Likewise T(λS(w))=λw gives S(λw)=λS(w).
- **Example 3.64** (infinite-dimensional spaces). Multiplication by x² on P(R) is injective but not surjective (1 is not in the range), so not invertible. The backward shift on F^∞ is surjective but not injective ((1,0,0,…) is in the null space), so not invertible (p. 84).
- **3.65 (dim V = dim W < ∞).** For T∈L(V,W): T invertible ⇔ T injective ⇔ T surjective. Proof: by 3.21, $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ (3.66).
 - If T is injective, dim null T=0 (3.15), so dim range T=dim V=dim W, hence T is surjective (2.39).
 - If T is surjective, dim null T=dim V−dim W=0, so T is injective.
 - So injective ⇔ surjective, and either one gives both, hence invertibility by 3.63 (p. 84).
- **Example 3.67.** Claim: for every polynomial q there is a polynomial p with $((x^2+5x+7)p)''=q$.
 - 3.65 does not apply directly to P(R), because of 3.64. So pick m with q∈P_m(R) and define $T:P_m(R)\to P_m(R)$ by $Tp=((x^2+5x+7)p)''$.
 - Multiplying by x²+5x+7 raises the degree by 2 and differentiating twice lowers it by 2, so T maps P_m(R) to itself.
 - If Tp=0, the second derivative of (x²+5x+7)p is 0, so it has the form ax+b. So null T={0}, and T is injective, hence surjective by 3.65. This gives the p (p. 85).
- **3.68 (dim V = dim W < ∞).** For S∈L(W,V), T∈L(V,W): ST=I ⇔ TS=I.
 - Proof of ⇒: if Tv=0 then v=Iv=(ST)v=S(Tv)=S(0)=0, so T is injective, hence invertible (3.65). Multiply ST=I on the right by T⁻¹ to get S=T⁻¹, so TS=TT⁻¹=I. The other direction swaps the roles of S and T.
 - The author notes that for V=W this gives ST=I ⇒ ST=TS, although arbitrary linear maps on V do not commute (p. 85).

*Intuition note.* In finite dimension, a map between equal-sized spaces cannot lose information without also missing some targets. So one condition forces the other. In infinite dimension, Example 3.64 shows this can fail.

**Isomorphic vector spaces (pp. 86–87).**

- **3.69.** An *isomorphism* is an invertible linear map. Two vector spaces are *isomorphic* if some isomorphism goes from one onto the other. The author's picture: relabel v∈V as Tv∈W (p. 86).
- **3.70.** Two finite-dimensional vector spaces over F are isomorphic iff they have the same dimension. Proof (p. 86):
 - (⇒) An isomorphism T has null T={0} and range T=W, so 3.21 becomes dim V=dim W.
 - (⇐) With bases v_1,…,v_n and w_1,…,w_n, define $T(c_1v_1+\cdots+c_nv_n)=c_1w_1+\cdots+c_nw_n$. T is well defined and linear, surjective because the w's span, and injective (null T={0}) because the w's are linearly independent. By 3.63 it is an isomorphism.
- Consequently every finite-dimensional V is isomorphic to F^n with n=dim V; e.g. P_m(F) ≅ F^{m+1}. The author answers "why not study only F^n?": studying F^n would lead to null spaces and ranges of maps, which are again vector spaces. Viewing each as some F^m "often adds complexity but no new insight" (p. 87).
- **3.71.** For bases of V and W, M is an isomorphism between L(V,W) and F^{m,n}. M is linear by 3.35 and 3.38.
 - Injective: if M(T)=0, then Tv_k=0 for all k, so T=0.
 - Surjective: given A∈F^{m,n}, the linear map lemma (3.4) gives T with $Tv_k=\sum_jA_{j,k}w_j$, and then M(T)=A (p. 87).
- **3.72.** dim L(V,W)=(dim V)(dim W) for finite-dimensional V, W. It follows from 3.71, 3.70 and 3.40 (p. 87).

**Linear maps thought of as matrix multiplication (pp. 88–90).**

- **3.73 Matrix of a vector.** For v∈V and a basis v_1,…,v_n, M(v) is the n-by-1 matrix $(b_1,\dots,b_n)^t$ where $v=b_1v_1+\cdots+b_nv_n$. Example 3.74: for 2−7x+5x³+x⁴ in the standard basis of P_4(R), M is the column (2, −7, 0, 5, 1). For x∈F^n in the standard basis, M(x) is x written as a column. The map v ↦ M(v) is an isomorphism of V onto F^{n,1} (p. 88).
- **3.75.** The k-th column of M(T) equals M(Tv_k) (computed in the basis of W). It follows directly from the definitions (p. 89).
- **3.76 Linear maps act like matrix multiplication.** M(Tv)=M(T)M(v). Proof: write v=b_1v_1+⋯+b_nv_n, so Tv=b_1Tv_1+⋯+b_nTv_n (3.77). Then
$$\mathcal M(Tv)=b_1\mathcal M(Tv_1)+\cdots+b_n\mathcal M(Tv_n)=b_1\mathcal M(T)_{\cdot,1}+\cdots+b_n\mathcal M(T)_{\cdot,n}=\mathcal M(T)\mathcal M(v).$$
The first equality uses 3.77 and linearity of M, the second uses 3.75, the third uses 3.50 (p. 89).
- The author concludes that, after relabeling by these isomorphisms, every linear map between finite-dimensional spaces is multiplication by a matrix. That matrix depends on the bases; many later results are about choosing a basis that makes the matrix as simple as possible (p. 89).
- **3.78.** dim range T = column rank of M(T). The column rank is therefore the same for all choices of bases, since range T does not depend on a basis. Proof: v ↦ M(v) is an isomorphism W → F^{m,1}. Its restriction to range T = span(Tv_1,…,Tv_n) (Exercise 10, Section 3B) is an isomorphism onto span(M(Tv_1),…,M(Tv_n)), which is the span of the columns of M(T) (p. 90).

**Change of basis (pp. 90–93).**

- For T∈L(V) with one basis used for both domain and target, write M(T,(v_1,…,v_n)) for M(T,(v_1,…,v_n),(v_1,…,v_n)), or just M(T) (p. 90).
- **3.79 Identity matrix I:** n-by-n, with 1's on the diagonal and 0's elsewhere. M(I) is I in every basis. The same symbol I denotes both the operator and the matrix. For a square matrix A of the same size, AI=IA=A (p. 91).
- **3.80.** A square matrix A is *invertible* if some square B of the same size has AB=BA=I; then B=A⁻¹. The proof of 3.60 shows uniqueness. "Nonsingular/singular" mean invertible/noninvertible. Also (A⁻¹)⁻¹=A. If A, C are invertible of the same size, then AC is invertible and (AC)⁻¹=C⁻¹A⁻¹, because (AC)(C⁻¹A⁻¹)=A(CC⁻¹)A⁻¹=AIA⁻¹=AA⁻¹=I, and similarly on the other side (p. 91).
- **3.81.** For T∈L(U,V), S∈L(V,W) with bases (u_1,…,u_m), (v_1,…,v_n), (w_1,…,w_p):
$$\mathcal M(ST,(u),(w))=\mathcal M(S,(v),(w))\,\mathcal M(T,(u),(v)).$$
This is 3.43 with the bases written out (p. 91).
- **3.82.** For two bases (u), (v) of V, the matrices M(I,(u),(v)) and M(I,(v),(u)) are invertible, and each is the inverse of the other. Proof: put S=T=I and w_k=u_k in 3.81 to get $I=\mathcal M(I,(v),(u))\,\mathcal M(I,(u),(v))$. Swap the roles of u and v for the other order (p. 92). Column k of M(I,(u),(v)) holds the scalars writing u_k in the basis (v) (p. 92).
- **Example 3.83.** For the bases (4,2),(5,3) and the standard basis of F²: since I(4,2)=4(1,0)+2(0,1) and I(5,3)=5(1,0)+3(0,1), M(I,((4,2),(5,3)),((1,0),(0,1))) = $\begin{pmatrix}4&5\\2&3\end{pmatrix}$. Its inverse is $\begin{pmatrix}3/2&-5/2\\-1&2\end{pmatrix}$, which by 3.82 is M(I,((1,0),(0,1)),((4,2),(5,3))) (p. 92).
- **3.84 Change-of-basis formula.** Let T∈L(V) and (u), (v) be bases of V. Let A=M(T,(u)), B=M(T,(v)), C=M(I,(u),(v)). Then
$$A=C^{-1}BC .$$
Proof: 3.81 with S=I (and w_k=u_k) and 3.82 give $A=C^{-1}\mathcal M(T,(u),(v))$ (3.85). 3.81 with the roles S→T, T→I gives $\mathcal M(T,(u),(v))=BC$. Substitute (p. 93).
- **3.86.** If T∈L(V) is invertible, M(T⁻¹)=(M(T))⁻¹ (same basis for both). The proof is left as an exercise (p. 93).

*Intuition note.* C translates u-coordinates into v-coordinates. A=C⁻¹BC says: translate to the v-basis, apply the map there (B), and translate back.

## Toy example (ours, not from the text)
Take T, S ∈ L(R²) with T(x,y)=(2x, x+y) and S(x,y)=(y, x−y), standard bases.
- Columns of M(T): T(1,0)=(2,1), T(0,1)=(0,1), so $M(T)=\begin{pmatrix}2&0\\1&1\end{pmatrix}$.
- Columns of M(S): S(1,0)=(0,1), S(0,1)=(1,−1), so $M(S)=\begin{pmatrix}0&1\\1&-1\end{pmatrix}$.
- Composition: ST(x,y)=S(2x,x+y)=(x+y, 2x−(x+y))=(x+y, x−y). So ST(1,0)=(1,1) and ST(0,1)=(1,−1), giving $M(ST)=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.
- Product: row 1 of M(S)=(0,1) times columns of M(T): (0·2+1·1, 0·0+1·1)=(1,1). Row 2=(1,−1): (1·2+(−1)·1, 1·0+(−1)·1)=(1,−1). So M(S)M(T)=M(ST) ✓ (3.43).
- Action on a vector: v=(3,4). Tv=(6,7). M(T)M(v)=(2·3+0·4, 1·3+1·4)=(6,7) ✓ (3.76). Also M(T)M(v)=3·(2,1)+4·(0,1)=(6,7), a combination of columns (3.50).

## Concepts
- [[matrix as transformation]] — M(T): column k lists the target-basis coordinates of Tv_k; depends on both bases (p. 69)
- [[matrix multiplication as composition]] — product defined by $(AB)_{j,k}=\sum_rA_{j,r}B_{r,k}$ so that M(ST)=M(S)M(T) (pp. 72–74)
- [[linear combination]] — Ab is a combination of the columns of A with coefficients b; rows of CR are combinations of rows of R (p. 76)
- [[rank]] — column rank of a matrix (equal to row rank); also dim range T for T with matrix M(T) (pp. 77–79, 90)
- [[column space (range)]] — here only the span of columns; dim range T equals its dimension, i.e. the column rank of M(T) (p. 90)
- [[inverse matrix]] — square A with AB=BA=I for some square B; unique (p. 91). Author does not mention determinants in this unit.
- [[rank–nullity (Fundamental Theorem of Linear Maps)]] — used as 3.21/3.66 to prove 3.65 and 3.70 (pp. 84, 86)
- [[change of basis]] — A=C⁻¹BC with C=M(I,(u),(v)) (p. 93)
- [[dimension]] — the single number that decides whether two finite-dimensional spaces over F are isomorphic (p. 86)
- [[isomorphism]] (new) — an invertible linear map; "relabeling" of vectors (p. 86)
- [[invertible linear map]] (new) — T with S such that ST=I and TS=I; equivalent to injective and surjective (pp. 82–83)
- [[transpose]] (new) — $A^t$ with $(A^t)_{k,j}=A_{j,k}$ (p. 77)
- [[column–row factorization]] (new) — A=CR with C of size m-by-c, R of size c-by-n, c=column rank (p. 78)
- [[matrix of a vector]] (new) — n-by-1 column of coordinates M(v) in a chosen basis (p. 88)

## Canonical instances
- [[example-3-32-matrix-F2-to-F3]] — M of T(x,y)=(x+3y,2x+5y,7x+9y) (p. 70)
- [[example-3-33-differentiation-matrix]] — M(D), P_3(R)→P_2(R) (p. 70)
- [[example-3-42-matrix-product]] — 3×2 times 2×4 product (p. 73)
- [[example-3-53-column-row-rank]] — a 2×4 matrix with both ranks 2 (p. 77)
- [[example-3-62-inverse-rotation-stretch]] — T(x,y,z)=(−y,x,4z) and its inverse (p. 82)
- [[example-3-64-shift-and-x2]] — injective-not-surjective and surjective-not-injective maps (p. 84)
- [[example-3-67-second-derivative-polynomial]] — surjectivity via 3.65 on P_m(R) (p. 85)
- [[example-3-83-identity-two-bases]] — change-of-basis matrix for (4,2),(5,3) (p. 92)

## Bridges (candidates)
- [same-math] 3.50 "Ab is a combination of columns of A" ↔ linear-algebra spine: matrix–vector product as column space reachability
- [same-math] 3.84 A=C⁻¹BC ↔ linear-algebra spine: change of basis A ↦ P⁻¹AP
- [same-math] 3.78 dim range T = column rank ↔ linear-algebra spine: rank as dimension of column space
- [structural-analogy] 3.70 (dimension classifies vector spaces) ↔ other fields: classification of structures up to isomorphism by one invariant; the author notes this is hard for groups or topological spaces (p. 86)
- [metaphor] Isomorphism as "relabeling elements" ↔ data representation: choosing coordinates as an encoding that preserves all structure

## Questions this raises
- Which basis choice makes M(T) simplest for a map T∈L(V)? The author says this is a theme of later chapters (p. 89).
- How is the rank of a matrix connected to its row and column vectors beyond equality of the two ranks (e.g. the alternative proofs cited at 3.133)?
- When is a matrix invertible in practice? Exercise 22 relates invertibility of M(T) to that of T, and Exercise 21 compares two solvability conditions for n equations in n unknowns.
- What replaces 3.65 in infinite dimensions, given Example 3.64?

## Exercises worth doing
- Ex. 3C.5 (p. 79) — every T has bases in which M(T) is zeros plus 1's on the diagonal for rows 1 ≤ k ≤ dim range T — difficulty: medium
- Ex. 3C.12 (p. 80) — associativity of matrix multiplication; the exercise asks for a clean proof and quotes Emil Artin on throwing the matrices out — difficulty: medium
- Ex. 3C.16 (p. 81) — rank 1 ⇔ $A_{j,k}=c_jd_k$ (outer-product form) — difficulty: medium
- Ex. 3C.17 (p. 81) — five equivalent conditions for injectivity of T in terms of rows and columns of M(T) — difficulty: medium
- Ex. 3D.12 (p. 94) — STU=I implies T invertible and T⁻¹=US (finite-dimensional) — difficulty: medium
- Ex. 3D.24 (p. 95) — for square matrices, AB=I implies BA=I — difficulty: medium

## Reading notes
- **Part boundaries.** This unit starts at the beginning of Section 3C (printed p. 69) and ends at the end of the Exercises 3D (printed p. 95), covering all of 3C and 3D as printed. Earlier results (not part of this unit) are only cited, e.g. 3.4, 3.15, 3.21, 2.30, 2.39, Example 3.3.
- **Page offset:** printed = pdf − 14.
- **Edition:** running footer reads "Linear Algebra Done Right, fourth edition, by Sheldon Axler".
- **OCR:** the text layer renders math italics as placeholder glyphs and garbles matrices; all symbols were checked against the page images. I found no misprints.
- **Not proved in the text:** 3.35, 3.38 (Exercise 3), 3.86 (left as exercise), and the transpose properties (Exercises 14, 15).
- **Source cross-references** not in this unit: 3.133, Exercise 8 in 7A, Exercise 35 in 6A.
- **Toy example** is my own and is not in the source.
