---
id: strang-2023-introduction/ch08-linear
work: strang-2023-introduction
unit: "8 Linear Transformations"
pages: 308-334
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Linear Transformations (Strang, Ch. 8)

## L0 — One line
A linear transformation is fully determined by what it does to a basis, so each choice of input and output bases turns it into a matrix, and a good choice of bases (eigenvectors, singular vectors, and so on) makes that matrix simple.

## L1 — The gist (≤ 120 words)
The chapter asks how a linear transformation T (a rule respecting sums and scalings) relates to a matrix, and which basis gives the simplest matrix. Once an input basis and an output basis are chosen, column j of the matrix holds T(v_j) written in the output basis. Matrix multiplication AB then matches composition TS (when the middle basis is shared). Changing bases changes A to B_out⁻¹ A B_in. Eigenvector bases give Λ, singular-vector bases give Σ, generalized eigenvectors give the Jordan form J, and Fourier, Legendre and Chebyshev bases suit function space. It matters because it explains why matrices multiply as they do and why diagonalizing is a change of basis.

**Prerequisites:** vector spaces, basis, and matrix–vector products as combinations of columns. Λ and Σ stand for the diagonal matrices of eigenvalues and of singular values. A circulant matrix has constant diagonals that wrap around. Also column space and nullspace, eigenvectors, the SVD, Gram–Schmidt, and inner products. For 8.3 you also need the derivative and integral of polynomials.

## L2 — Key ideas
- Linearity means T(cv + dw) = cT(v) + dT(w). Shifts, lengths and squares fail it. (p. 309–310)
- If T(v₁),…,T(vₙ) are known for a basis, T(u) is known for every u. This is why one matrix per pair of bases can copy T. (p. 310, 318)
- Derivative and integral are linear transformations on polynomial spaces. Their matrices show a kernel (the inputs sent to 0; here the constants) and a pseudoinverse relation (an inverse that works on one side only: A⁺A ≠ I, AA⁺ = I). (p. 312–313, 320)
- Key rule: column j of A is T(v_j) written in the output basis w. Then Ac gives the coefficients of T(v). (p. 320)
- The reason for the rule for multiplying matrices: AB represents the composition TS when the middle basis is shared. Rotation by θ twice gives rotation by 2θ. (p. 321)
- Changing bases turns A into B_out⁻¹ A B_in. When A has n independent eigenvectors, they give Λ; singular vectors give Σ, so "diagonalize" means "choose a good basis". (p. 322–323)
- The Jordan form J is the nearly diagonal matrix for matrices lacking n eigenvectors (it uses extra "generalized" eigenvectors). Strang says it is unstable to compute. (p. 328–329)
- The Fourier matrix diagonalizes every circulant matrix. For function space, the powers 1, x, x², … form an ill-conditioned (barely independent) basis, while Fourier, Legendre and Chebyshev bases are good. (p. 330–333)

## L3 — Walkthrough

### Preface (p. 308)
Strang chose to start with matrices, not transformations. Section 8.3 turns to bases for function space. There the length and inner product are ‖f‖² = ∫f(x)² dx and (f,g) = ∫f(x)g(x) dx. (p. 308)

### 8.1 The Idea of a Linear Transformation
**Definition.** A transformation T assigns an output T(v) to each input v in V. It is *linear* if, for all v, w and all c, (p. 309)
(a) T(v + w) = T(v) + T(w), and (b) T(cv) = cT(v).
Together: T(cv + dw) = cT(v) + dT(w). It follows that T(0) = 0. Matrix multiplication T(v) = Av is linear. (p. 309)

**Shift is not linear.** If T(v) = v + u₀ then T(v + w) = v + w + u₀ ≠ T(v) + T(w) = v + w + 2u₀, unless u₀ = 0. For u₀ = 0, T is the identity. Linear plus shift, T(v) = Av + u₀, is called *affine*. Straight lines stay straight, and computer graphics uses it. (p. 309–310)

**Examples (p. 310).**
- Ex. 1: T(v) = a·v with a = (1,3,4) is linear from R³ to R¹. It is multiplication by the row matrix [1 3 4].
- Output with squares, products or lengths (v₁², v₁v₂, ‖v‖) is not linear.
- Ex. 2: the length ‖v‖ is not linear. (a) fails because of the triangle inequality ‖v+w‖ ≤ ‖v‖+‖w‖. (b) fails because ‖−v‖ = ‖v‖, not −‖v‖.
- Ex. 3: rotation of the plane by 30° is linear. Rotating then adding equals adding then rotating.

**Combinations (1).** u = c₁v₁ + ⋯ + cₙvₙ must go to
$$T(u) = c_1T(v_1) + c_2T(v_2) + \cdots + c_nT(v_n) \tag{1}$$
The 3-vector case is proved from the 2-vector rule: T(cu + dv + ew) = T(cu) + T(dv + ew), then apply linearity again. (p. 310)

**Basis tells all.** If T(v) is known for every vector of a basis v₁,…,vₙ, then T(u) is known for every u in the space. Every u is a combination of the v_j, and T(u) is the same combination of the T(v_j). (p. 310)

*Intuition note:* A linear map has no freedom beyond what it does to a basis. Fix the images of the basis vectors and every other image is forced.

**Lines to lines, triangles to triangles (Fig. 8.1).** Points on the line from v to w go onto the line from T(v) to T(w), and equally spaced points stay equally spaced. The midpoint ½v + ½w goes to ½T(v) + ½T(w). For three corners, the input triangle goes onto the output triangle, and u = ⅓(v₁+v₂+v₃) goes to ⅓(T(v₁)+T(v₂)+T(v₃)). (p. 311)

**Houses (Fig. 8.2).** The 2 by 12 matrix H holds the house corners as columns. The corners of the new house are the columns of AH. The matrices shown are I, a 35° rotation, [[0,1],[1,0]] and [[.7,.3],[.3,.7]]. (p. 311)

**Calculus (p. 312–313).**
- Ex. 4: T(u) = du/dx is linear. The derivatives of the basis 1, x, x² are 0, 1, 2x. For u = 6 − 4x + 3x², du/dx = 6(0) − 4(1) + 3(2x) = −4 + 6x.
- Nullspace of d/dx: the constants, a line in function space, spanned by u = 1.
- Column space of d/dx on quadratics a + bx + cx²: all b + 2cx. Then 2 + 1 = 3 = dim(input space), so r + (n − r) = n still holds. (p. 312)
- On the basis: dv₁/dx = 0, dv₂/dx = 1 = v₁, dv₃/dx = 2x = 2v₂. (2)
- The matrix, from input basis 1, x, x² and output basis 1, x, is
$$A = \begin{bmatrix}0&1&0\\0&0&2\end{bmatrix} \tag{3}$$
- Check: A(a,b,c)ᵀ = (b, 2c)ᵀ, which is the coefficient vector of b + 2cx. (p. 312)
- Ex. 5: the integral T⁺(D + Ex) = Dx + ½Ex² has input basis 1, x and output basis 1, x, x². Its matrix is
$$A^+=\begin{bmatrix}0&0\\1&0\\0&\tfrac12\end{bmatrix}.$$
- Product of the two matrices:
$$A^+A=\begin{bmatrix}0&0&0\\0&1&0\\0&0&1\end{bmatrix},\qquad AA^+=\begin{bmatrix}1&0\\0&1\end{bmatrix} \tag{4}$$
- The zero in the corner of A⁺A reflects the 1-dimensional nullspace of d/dx. Strang calls integration the pseudoinverse of differentiation. (p. 313)

**More examples (p. 313).**
- Ex. 6: sending (x,y,z) to (x,y,1) is not linear, since it does not send 0 to 0.
- Ex. 7: for invertible A, T⁻¹ (multiplication by A⁻¹) is linear, with T⁻¹(T(v)) = v matching A⁻¹(Av) = v. If T(v) = Av and S(u) = Bu, then T(S(u)) matches ABu.
- Strang asks whether every linear T from Rⁿ to Rᵐ comes from a matrix. His answer is yes, once an input basis and output basis are chosen.
- *Range of T* = all outputs (the column space when T(v) = Av). *Kernel of T* = all inputs with T(v) = 0 (the nullspace).

**Worked examples (p. 314).**
- 8.1 A: the shear [[1,0],[1,1]] sends (x,y) to (x, x+y). It sends (1,0)→(1,1) and (2,0)→(2,2). Points (0,y) on the y axis do not move (eigenvectors with λ = 1). A square goes to a parallelogram.
- 8.1 B: a nonlinear T is invertible if T(x) = b has exactly one solution for every b. T₁ = x² is not invertible (x² = 1 has two solutions, x² = −1 none). T₄ = eˣ is not invertible (eˣ = −1 has no solution). T₂ = x³, T₃ = x + 9 and T₅ = 1/x are invertible, with inverses b^{1/3}, b − 9 and 1/b. (T₅² is the identity.)

### 8.2 The Matrix of a Linear Transformation
**Setting.** T goes from V (n-dimensional) to W (m-dimensional), with input basis v₁,…,vₙ and output basis w₁,…,wₘ. The matrix A is m by n. The standard bases (columns of I) give the standard matrix, and other bases give other matrices for the same T. (p. 318)

**Key idea.** Put the outputs T(v₁),…,T(vₙ) in the columns. Then Ac = c₁T(v₁) + ⋯ + cₙT(vₙ) = T(v). The reason is that every v is a unique combination Σcⱼvⱼ, and T is linear. (p. 318)

Ex. 1 (p. 318): T(v₁) = (2,3,4) and T(v₂) = (5,5,5) give
$$A=\begin{bmatrix}2&5\\3&5\\4&5\end{bmatrix},\quad T(v_1+v_2)=A\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}7\\8\\9\end{bmatrix}.$$

**Change of basis (Ex. 2, p. 319).** Take T = identity, V = W = R². Input basis V = [[3,6],[3,8]], output basis W = [[3,0],[1,2]]. Write each input vector in the output basis:
- v₁ = 1w₁ + 1w₂ and v₂ = 2w₁ + 3w₂.
- These coefficients are the columns of B = [[1,2],[1,3]], so WB = V.
$$B = W^{-1}V,\qquad \begin{bmatrix}3&0\\1&2\end{bmatrix}\begin{bmatrix}1&2\\1&3\end{bmatrix}=\begin{bmatrix}3&6\\3&8\end{bmatrix} \tag{1}$$
- Reason: the same u satisfies Vc = Wd, so d = W⁻¹Vc. (2)
- Strang calls it a "mystery" that for V = I the change-of-basis matrix is W⁻¹, not W. "Larger basis vectors have smaller coefficients." (p. 319)

**Construction (p. 320).** The first column of A is T(v₁) = a₁₁w₁ + ⋯ + aₘ₁wₘ, and similarly for each column. The key rule is
$$T(v_j)=a_{1j}w_1+\cdots+a_{mj}w_m \tag{3}$$
Then linearity gets all other vectors right, because multiplying A by c = (c₁,…,cₙ) is itself linear. Every linear T from V to W converts to a matrix using bases. (p. 320)
- Ex. 3: input basis 1, x, x², x³ and output basis 1, x, x² give the derivative matrix [[0,1,0,0],[0,0,2,0],[0,0,0,3]]. A(c₁,c₂,c₃,c₄)ᵀ = (c₂, 2c₃, 3c₄)ᵀ.
- Ex. 4: the integral matrix A⁺ has rows (0,0,0), (1,0,0), (0,½,0), (0,0,⅓). Applied to (d₁,d₂,d₃) it gives (0, d₁, ½d₂, ⅓d₃).
- Integrate then differentiate: AA⁺ = I. Differentiate then integrate: A⁺A ≠ I, because the constant is lost. T⁺T(1) = 0 matches A⁺A having a zero first column. (p. 320–321)

**Matrix products match transformations (p. 321).**
- (TS)(u) = T(S(u)) and (AB)(x) = A(Bx).
- S goes from U to V with matrix B (n by p), using bases u₁…u_p and v₁…vₙ. T goes from V to W with matrix A (m by n), which must use the *same* basis v₁…vₙ for V.
- Then AB, of shape (m by n)(n by p) = (m by p), represents TS.
- Ex. 5: S and T both rotate by θ, so T² is rotation by 2θ and A² = [[cos 2θ, −sin 2θ],[sin 2θ, cos 2θ]]. (4)
- Multiplying out gives A² = [[cos²θ − sin²θ, −2 sinθ cosθ],[2 sinθ cosθ, cos²θ − sin²θ]]. (5)
- Comparing (4) and (5) gives cos 2θ = cos²θ − sin²θ and sin 2θ = 2 sinθ cosθ.
- Ex. 6: rotating by θ then −θ gives AB = I, so the two rotation matrices are inverses. (p. 322)

*Intuition note:* "Do S, then T" becomes "multiply by B, then by A", so the rule for matrix products is just composition of maps written in coordinates. The middle basis must be shared.

**Choosing the best bases (p. 322–323).**
- *Eigenvectors:* if T maps Rⁿ to Rⁿ and A has n independent eigenvectors, use them as input and output basis. The matrix for T is then the diagonal matrix Λ.
- Ex. 7: T projects R² onto the line y = −x. In the standard basis, T(v₁) = (½,−½) and T(v₂) = (−½,½), so
$$A=\begin{bmatrix}\tfrac12&-\tfrac12\\-\tfrac12&\tfrac12\end{bmatrix},\quad A^{T}=A,\ A^2=A.$$
- With v₁ = w₁ = (1,−1), which projects to itself (λ₁ = 1), and v₂ = w₂ = (1,1), which projects to zero (λ₂ = 0), the new matrix is
$$\begin{bmatrix}1&0\\0&0\end{bmatrix}=\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix}=\Lambda \tag{6}$$
- For another basis b's with B_in = B and B_out = B⁻¹, the new matrix is similar to A:
$$A_{\text{new}}=B^{-1}AB. \tag{7}$$
- *Singular vectors:* with different spaces and bases, A = UΣVᵀ gives U⁻¹AV = Σ. The right singular vectors are the input basis and the left singular vectors the output basis. Then B_out⁻¹ A B_in = U⁻¹AV = Σ.
- Σ is not "similar" to A, since two bases are involved. Following David Vogan, Strang calls Σ *isometric* to A. **Definition:** C = Q₁⁻¹AQ₂ is isometric to A if Q₁ and Q₂ are orthogonal. (p. 323)
- Ex. 8: for T = d/dx, reverse both bases: input x³, x², x, 1 and output x², x, 1. The change-of-basis matrices are permutations, and
$$B_{\text{out}}^{-1}AB_{\text{in}}=\begin{bmatrix}3&0&0&0\\0&2&0&0\\0&0&1&0\end{bmatrix}=\Sigma,\ \sigma\text{'s}=3,2,1. \tag{8}$$
- Check: x³, x², x have derivatives 3x², 2x, 1. (p. 323)

*Intuition note:* The same T has many matrices. Eigenvector bases and singular-vector bases are the two choices the text singles out for making the matrix diagonal.

**Review (p. 323).** Linearity fixes T from basis values. Column j of A is a₁ⱼ…aₘⱼ exactly when T(v_j) = a₁ⱼw₁ + ⋯ + aₘⱼwₘ. The change-of-basis matrix is B = W⁻¹V = B_out⁻¹B_in. AB represents T(S(u)). The best bases give Λ or Σ.

### 8.3 The Search for a Good Basis
**Pure algebra.** If A is the matrix for T in the standard bases, then B_out⁻¹ A B_in is the matrix in the new bases (1). B_in and B_out are always invertible. When B_in = B_out = B, B⁻¹AB is similar to A (same eigenvalues). (p. 327)

Choices for vectors (p. 327):
1. B = eigenvector matrix X gives X⁻¹AX = Λ. This requires n independent eigenvectors ("A must be diagonalizable").
2. B_in = V, B_out = U (singular vectors) give U⁻¹AV = Σ. The columns are orthonormal eigenvectors of AᵀA and AAᵀ.
3. B_in = B_out = generalized eigenvectors give the Jordan form J = B⁻¹AB.

**Jordan form.**
- A (square) may have only s independent eigenvectors; in all cases Jordan constructed n − s extra "generalized" eigenvectors. J then has s square blocks, each with one eigenvalue λ, one eigenvector and 1's above the diagonal. The best J has n blocks of size 1×1, and then J = Λ. (p. 327)
- Ex. 1 (p. 328): J has blocks [2], [2] and [[3,1],[0,3]]. Its eigenvalues are 2, 2, 3, 3, with 3 independent eigenvectors.
  - Eigenvectors: x₁ = (1,0,0,0) and x₂ = (0,1,0,0) for λ = 2, and x₃ = (0,0,1,0) for λ = 3.
  - Generalized eigenvector: x₄ = (0,0,0,1), with (J − 3I)x₄ = x₃. A true eigenvector would give 0, but not here.
- Every C = BJB⁻¹ similar to this J has true eigenvectors b₁,b₂,b₃ in B's first three columns and a generalized b₄. Proof of (C − 3I)b₄ = b₃, using Bx₃ = b₃ and Bx₄ = b₄:
$$(BJB^{-1}-3I)b_4=BJx_4-3Bx_4=B(J-3I)x_4=Bx_3=b_3 \tag{2}$$
- Jordan's theorem: every square matrix has a complete set of eigenvectors and generalized eigenvectors. With these in B, B⁻¹AB = J.
- Theorem statement (p. 329): if A has s independent eigenvectors, it is similar to J with blocks J₁,…,J_s,
$$B^{-1}AB=\begin{bmatrix}J_1&&\\&\ddots&\\&&J_s\end{bmatrix}=J \tag{3}$$
$$J_i=\begin{bmatrix}\lambda_i&1&&\\&\ddots&\ddots&\\&&\ddots&1\\&&&\lambda_i\end{bmatrix} \tag{4}$$
- "Matrices are similar if they share the same Jordan form J—not otherwise." There is an off-diagonal 1 for each missing eigenvector. (p. 329)
- For any square A = BJB⁻¹, du/dt = Au has solution u(t) = Be^{Jt}B⁻¹u(0). e^{Jt} involves e^{λt} times powers 1, t,…, t^{s−1}. (p. 328)
- The proof is not given here. Strang says the Jordan form is not popular in computation, because its calculation is not stable. A slight change in A separates repeated eigenvalues and removes the 1's, switching J to a diagonal Λ. (p. 329)
- Question (p. 329): if A² = 0, all eigenvalues are 0 (Ax = λx gives A²x = λ²x = 0). J² = B⁻¹A²B = 0. Block sizes 1 and 2 satisfy J² = 0, but a 3×3 block has J² ≠ 0. So all blocks have size 1 or 2, and the maximum rank of J is n/2.

*Intuition note:* When eigenvectors are missing, no basis diagonalizes A. The Jordan form is the closest you can get: one 1 above the diagonal for each missing eigenvector.

**Fourier basis for vectors (p. 330–331).**
- Fx is a Discrete Fourier Transform of x. Strang says such fixed bases, chosen without knowing A, probably don't diagonalize A, but for many important matrices in applied mathematics B⁻¹AB is close to diagonal. (p. 330)
- Take P, the 4×4 cyclic permutation matrix with ones at (1,2), (2,3), (3,4), (4,1). Px = λx with x = (1, λ, λ², λ³) holds when λ⁴ = 1 (the fourth row gives 1 = λ⁴). (5)
- The four eigenvalues are 1, i, −1, −i. The eigenvector matrix is the Fourier matrix F, with columns (1, λ, λ², λ³) for those four λ. It diagonalizes P. (6)
- The columns of F are orthogonal. They are eigenvectors of P and of every circulant matrix C = c₀I + c₁P + c₂P² + c₂P³, as printed. The pattern of C below suggests the last coefficient is c₃. (p. 330)
- F is complex. Multiplications Fx are done fast by the Fast Fourier Transform.
- A circulant C has rows (c₀,c₁,c₂,c₃), (c₃,c₀,c₁,c₂), (c₂,c₃,c₀,c₁), (c₁,c₂,c₃,c₀). Its eigenvectors are the columns of F and its eigenvalues are in the vector Fc. λ = c₀ + c₁ + c₂ + c₃ has eigenvector (1,1,1,1). (p. 330)
- Circulants have constant diagonals that wrap around. This corresponds to constant coefficients in a differential equation, "exactly when Fourier works perfectly". (p. 331)
- d²u/dt² = −u is solved by u = c₀ cos t + c₁ sin t. d²u/dt² = tu (Airy's equation, variable coefficient) cannot be solved by elementary functions. Substituting e^{λt} into a constant-coefficient equation finds λ, which is "like an eigenvalue". (p. 331)

**Bases for function space (p. 331–332).**
- The powers 1, x, x², … are a terrible basis. They are "barely independent", and x¹⁰ is almost a combination of lower powers. The test for a basis is BᵀB: it is orthonormal when BᵀB = I.
- For the powers on [0,1], the inner product entries are
$$\int_0^1 x^ix^j\,dx=\frac{x^{i+j+1}}{i+j+1}\Big|_{0}^{1}=\frac1{i+j+1},$$
  the Hilbert matrix. It has an enormous ratio of largest to smallest eigenvalue, a large condition number, which signals an unhappy choice. (p. 331)
- Inner products of functions replace sums by integrals:
  - (f,g) = ∫ f(x)g(x) dx.
  - Complex: (f,g) = ∫ f̄(x)g(x) dx.
  - Weighted: (f,g)_w = ∫ w(x) f̄(x) g(x) dx. (p. 332)
- Three bases (p. 332): Fourier 1, sin x, cos x, sin 2x, cos 2x, …; Legendre 1, x, x² − ⅓, x³ − ⅗x, …; Chebyshev 1, x, 2x² − 1, 4x³ − 3x, ….
- Fourier functions are periodic and mutually orthogonal. A smooth periodic f needs only a few low-frequency terms. Jumps and noise show up in high frequencies. Function space is infinite-dimensional.
- Fourier series: f(x) = a₀ + b₁ sin x + a₁ cos x + b₂ sin 2x + a₂ cos 2x + ⋯
- Each coefficient is a projection, like bᵀa/aᵀa. For example,
$$a_3=\frac{(f(x),\cos 3x)}{(\cos 3x,\cos 3x)}=\frac{\int f(x)\cos 3x\,dx}{\int\cos 3x\cos 3x\,dx} \tag{7}$$
- Gibbs phenomenon: for a function with a jump, Fourier approximations overshoot, and adding more terms does not fix it. (p. 332)

**Legendre and Chebyshev (p. 333).**
- Legendre polynomials come from Gram–Schmidt applied to 1, x, x², … on the interval from −1 to 1. The function x is already orthogonal to 1.
- (x²,1)/(1,1) = ∫x²dx / ∫1dx = (2/3)/2 = ⅓, so Gram–Schmidt gives x² − ⅓.
- (x³,x)/(x,x) = (2/5)/(2/3) = ⅗, so Gram–Schmidt gives x³ − ⅗x. Continuing gives the rest.
- Chebyshev polynomials do not come from Gram–Schmidt. They connect to cos nθ by setting x = cos θ:
  - 2x² − 1 = 2(cos θ)² − 1 = cos 2θ.
  - 4x³ − 3x = 4(cos θ)³ − 3 cos θ = cos 3θ.
  - In general cos nθ = Tₙ(cos θ). The FFT then gives a computational advantage.
- "Chebfun" replaces each f(x) by a Chebyshev approximation, so one can integrate, solve f(x) = 0, find extrema and solve differential equations. (p. 333)

**Review (p. 333).** A basis is good if B is well-conditioned, and orthogonal bases are best. Λ = B⁻¹AB diagonal is also good, but the Jordan form is very unstable. Fourier diagonalizes constant-coefficient periodic equations. The powers give a Hilbert matrix, which is terrible. Legendre and Chebyshev are excellent for function space.

## Toy example (ours)
Let T(v) = Av with A = [[2,1],[1,2]] on R². Take input and output basis b₁ = (1,1), b₂ = (1,−1), so B = [[1,1],[1,−1]].

Build the matrix by the key rule (column j = T(b_j) in the b-basis):
- T(b₁) = A(1,1) = (3,3) = 3b₁ + 0b₂, so column 1 = (3,0).
- T(b₂) = A(1,−1) = (2−1, 1−2) = (1,−1) = 0b₁ + 1b₂, so column 2 = (0,1).
- The matrix is diag(3,1).

Check by formula. B⁻¹ = ½[[1,1],[1,−1]] and AB = [[3,1],[3,−1]]. Then B⁻¹AB = ½[[3+3, 1−1],[3−3, 1+1]] = [[3,0],[0,1]]. ✓.

Check by linearity. (2,0) = 1·b₁ + 1·b₂, so T(2,0) = 3b₁ + b₂ = (3,3) + (1,−1) = (4,2). Directly, A(2,0) = (4,2). ✓

## Concepts
- [[linear-map-transformation]] — a rule T with T(cv + dw) = cT(v) + dT(w); here V and W may be matrix or function spaces (p. 309)
- [[matrix-as-transformation]] — column j of the matrix is T(v_j) written in the output basis (p. 320)
- [[matrix-multiplication-as-composition]] — AB represents TS when A's input basis equals B's output basis (p. 321)
- [[change-of-basis]] — B = W⁻¹V for T = identity; A becomes B_out⁻¹AB_in (p. 319, 327)
- [[column-space-range]] — Strang's "range of T" is the set of all outputs T(v) (p. 313)
- [[null-space-kernel]] — Strang's "kernel of T" is the set of inputs with T(v) = 0 (p. 313)
- [[eigenvector-eigenvalue]] — used as a basis that makes the matrix Λ (p. 322)
- [[diagonalization]] — B⁻¹AB = Λ, which needs n independent eigenvectors (p. 327)
- [[singular-value-decomposition-svd]] — U⁻¹AV = Σ, with separate orthonormal input and output bases (p. 323)
- [[pseudoinverse]] — the integral is the pseudoinverse of the derivative, with A⁺A ≠ I and AA⁺ = I (p. 313, 320)
- [[orthonormal-basis-orthogonal-matrix]] — BᵀB = I is best possible for a basis (p. 331)
- [[condition-number]] — a large ratio of extreme eigenvalues of BᵀB (the Hilbert matrix) marks a bad basis (p. 331)
- [[gram-schmidt-and-qr]] — orthogonalizing 1, x, x², … gives the Legendre polynomials (p. 333)
- [[similar-matrices]] (new) — B⁻¹AB is similar to A; Strang says matrices are similar if they share the same Jordan form, and not otherwise (p. 322, 329)
- [[jordan-form]] (new) — J has Jordan blocks (λ on the diagonal, 1's above) and is nearly diagonal when eigenvectors are missing (p. 327–329)
- [[generalized-eigenvector]] (new) — an extra basis vector with (J − λI)x = a true eigenvector (p. 328)
- [[isometric-matrices]] (new) — C = Q₁⁻¹AQ₂ with Q₁, Q₂ orthogonal; Strang's term for Σ versus A (p. 323)
- [[affine-transformation]] (new) — linear plus shift; not linear, but lines stay straight (p. 310)
- [[fourier-matrix-and-circulant]] (new) — F diagonalizes P and every circulant matrix; Fx is a discrete Fourier transform (p. 330)
- [[inner-product-of-functions]] (new) — integrals replace sums in (f,g) (p. 332)
- [[hilbert-matrix]] (new) — BᵀB for the powers 1, x, x², …, with entries 1/(i+j+1) (p. 331)
- [[legendre-chebyshev-polynomials]] (new) — orthogonal polynomial bases for function space; Tₙ(cos θ) = cos nθ (p. 333)

## Canonical instances
- [[derivative-as-linear-map]] — d/dx on polynomials has matrix [[0,1,0],[0,0,2]], a kernel of constants, and the integral as pseudoinverse (p. 312–313, 320)
- [[rotation-composition]] — rotating by θ twice gives rotation by 2θ and the double-angle formulas (p. 321)
- [[projection-eigenbasis]] — projection onto y = −x becomes diag(1,0) in an eigenvector basis (p. 322)
- [[reversed-basis-svd]] — reversing the bases for d/dx gives Σ with σ = 3, 2, 1 (p. 323)
- [[house-transformations]] — AH draws images of a house under 2×2 matrices (p. 311)
- [[shear]] — [[1,0],[1,1]] turns squares into parallelograms (p. 314)
- [[gibbs-phenomenon]] — Fourier sums overshoot a jump, whatever the number of terms (p. 332)

## Bridges (candidates)
- [structural-analogy] Hilbert matrix BᵀB with large condition number ↔ regression: nearly collinear predictors give an ill-conditioned XᵀX — both are bad bases or near-dependent columns.
- [same-math] Fourier matrix diagonalizing circulants ↔ signal processing: circular convolution is diagonalized by the DFT — the same eigenvectors (1, λ, λ², λ³).
- [structural-analogy] Choosing a basis that diagonalizes A (U⁻¹AV = Σ) ↔ principal component analysis: finding axes in which a data matrix is simple.
- [structural-analogy] Jordan form's instability ↔ numerical analysis: tiny perturbations split repeated eigenvalues, so discontinuous structure is lost.

## Questions this raises
- If the Jordan form is unstable, what do numerical methods use instead when eigenvectors are missing? (p. 329)
- Why does a basis for which BᵀB has a huge eigenvalue ratio hurt computation? (p. 331)
- How do Legendre or Chebyshev approximations behave for functions with jumps, compared with the Gibbs overshoot? (p. 332–333)
- Which transformations on matrix spaces (e.g. transpose) have a matrix, and how big is it? (p. 316)

## Exercises worth doing
- Ex. 1 (p. 315) — prove T(0) = 0 from each linearity rule — difficulty: easy
- Ex. 16 (p. 316) — transposing 2×2 matrices is linear but no 2×2 A gives AM = Mᵀ; the matrix must be 4×4 — difficulty: medium
- Ex. 14 (p. 325) — find change-of-basis matrices between two bases of R² and see when none exists — difficulty: easy
- Ex. 27 (p. 326) — any invertible T has matrix I when w_i = T(v_i) — difficulty: medium
- Ex. 4 (p. 334) — Jordan forms with different block sizes are not similar — difficulty: medium
- Ex. 8–9 (p. 334) — build the 3×3 Fourier matrix and check circulant eigenvectors — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 318 = printed 308).
- The text layer is garbled in several equations (e.g. matrices in 8.1 Ex. 5, 8.2 (8), Jordan blocks); I checked the page images.
- Page 333: the text layer says "interval from 1 to 1" for Legendre. The page image shows "−1 to 1", so I wrote −1 to 1; the minus sign is lost only in the text layer (the values ∫1dx = 2 and ∫x²dx = 2/3 agree with that interval).
- Page 330: the circulant formula appears as "c₀I + c₁P + c₂P² + c₂P³", apparently a misprint for c₃P³; I flagged it in the walkthrough.
- Problem 33 on page 326 refers to "Worked Example 8.2 A", which is not among the pages supplied for this unit (printed 308–334).
- Unit pages end with Problem Set 8.3, problem 10 (the last problem on printed p. 334); anything after that is not included.
