---
id: strang-2023-introduction/ch06-eigenvalues-p3
work: strang-2023-introduction
unit: "6 Eigenvalues and Eigenvectors (part 3/3): §6.4 Complex Numbers and Vectors and Matrices; §6.5 Solving Linear Differential Equations"
pages: 262–285
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Complex matrices, the Fourier matrix, and eigenvalue solutions of du/dt = Au

## L0 — One line
Allowing complex numbers makes Hermitian, unitary and circulant matrices fit eigenvalue theory (the Fourier matrix diagonalizes all circulants), and eigenvalues then solve du/dt = Au through e^{λt}x, with the real parts of λ deciding stability.

## L1 — The gist (≤ 120 words)
Section 6.4 extends eigenvalue theory to complex numbers. With the conjugate transpose, Hermitian matrices (S̄ᵀ = S) and unitary matrices (Q̄ᵀ = Q⁻¹) play the roles of symmetric and orthogonal ones. The cyclic permutation P and circulant matrices (combinations of powers of P) are diagonalized by the Fourier matrix. This leads to the fast Fourier transform (FFT) and the convolution rule. Section 6.5 solves du/dt = Au: write u(0) in eigenvectors and multiply each by e^{λt}. The matrix exponential e^{At} also covers missing eigenvectors, the real parts of λ decide stability, and the QR algorithm computes eigenvalues. Constant-coefficient linear equations become eigenvalue problems; the same tools serve signal processing and numerical computation.

**Prerequisites:** eigenvalues/eigenvectors, A = XΛX⁻¹, symmetric and orthogonal matrices, determinant and trace, Gram–Schmidt/QR, power series, derivative of e^{λt}.

## L2 — Key ideas (5–10 bullets)
- Complex vectors need v̄ᵀw, and complex matrices need Āᵀ in place of Aᵀ. Then Hermitian (S̄ᵀ = S) and unitary (Q̄ᵀ = Q⁻¹) matrices replace symmetric and orthogonal ones (pp. 263–264).
- Hermitian matrices have real eigenvalues, shown with the Rayleigh quotient x̄ᵀSx / x̄ᵀx; orthogonal eigenvectors need Schur's theorem (every square matrix is QTQ̄ᵀ with T triangular) (p. 264).
- The permutation P has eigenvalues equal to the N-th roots of 1. Its eigenvector matrix is the Fourier matrix F, which also diagonalizes every circulant matrix (a combination of powers of P) (pp. 265–266).
- Factoring F_N into half-size pieces gives the fast Fourier transform (FFT), with cost about N log₂N instead of N² (p. 267). Circulant multiplication is cyclic convolution, and F(c ⊛ d) = (Fc).*(Fd) (pp. 267–268).
- du/dt = Au is solved by u(t) = c₁e^{λ₁t}x₁ + ⋯ + cₙe^{λₙt}xₙ, where the cᵢ solve Xc = u(0) (pp. 270–272).
- A second-order equation becomes a first-order system with a companion matrix (the coefficient matrix of that system) whose eigenvalues solve the same quadratic. Difference methods are stable or unstable according to |λ| (pp. 273–275).
- A 2 by 2 system is stable when trace < 0 and det > 0. e^{At} = I + At + ⋯ always solves the equation and handles repeated eigenvalues (pp. 276–279).
- The QR algorithm computes eigenvalues by repeated A_k = Q_kR_k, A_{k+1} = R_kQ_k (pp. 284–285).

## L3 — Walkthrough

### 6.4 Complex numbers, vectors and matrices

**Complex numbers (p. 262).** The number i solves x² = −1. Every polynomial of degree n with complex coefficients has n complex roots (proved by Gauss). Quadratic formula: x = (−b ± √(b²−4ac))/2a, with two roots, real or complex, or one double root when b² = 4ac. Formulas for degree 3 and 4 are complicated; none is possible for n ≥ 5 (p. 262).

Rules, for $z = x+iy$:
- Sum: $z_1+z_2=(a+x)+i(b+y)$.
- Product: $(a+ib)(x+iy)=(ax-by)+i(bx+ay)$.
- Conjugate: $\bar z = x-iy$.
- Modulus: $|z|^2=z\bar z=x^2+y^2=r^2$.
- Division: multiply top and bottom by $\bar z$; in particular $1/z=\bar z/|z|^2$.

Polar form: $z=|z|e^{i\theta}=re^{i\theta}$ with $e^{i\theta}=\cos\theta+i\sin\theta$, so $x=r\cos\theta$, $y=r\sin\theta$. Multiplying adds angles and multiplies r's: $z_1z_2=|z_1||z_2|e^{i(\theta_1+\theta_2)}$, $z^n=r^ne^{in\theta}$ (p. 262).

**Conjugate pairs (p. 263).** For a real matrix, det(A−λI) = P(λ) has real coefficients, and P(λ) = λ² − (trace)λ + det for 2 by 2. The complex roots of a real polynomial come in conjugate pairs a ± bi. Reason: if P(x+iy)=0 with real coefficients, then P(x−iy)=0. For real A, Av = λv gives Av̄ = λ̄v̄, so eigenvectors for λ and λ̄ are v and v̄ (p. 263).

**Complex vectors and matrices (p. 263).**
- Length: $\|v\|^2=\bar v^Tv=|v_1|^2+\dots+|v_n|^2\ge0$.
- Inner product: $\bar v^Tw=\bar v_1w_1+\dots+\bar v_nw_n$. Use $\bar v^T$, not $v^T$.
- Example: v = (1, i) and w = (1+i, 0) both have length √2.
- Rule: replace Aᵀ, AᵀA, AAᵀ by Āᵀ, ĀᵀA, AĀᵀ. The test QᵀQ = I becomes Q̄ᵀQ = I.

| Real | Complex | Facts |
|---|---|---|
| symmetric Sᵀ = S | Hermitian S̄ᵀ = S | real eigenvalues; orthogonal eigenvectors |
| orthogonal Qᵀ = Q⁻¹ | unitary Q̄ᵀ = Q⁻¹ | orthogonal eigenvectors; $|\lambda|=1$ |

If A has eigenvalue λ then Āᵀ has eigenvalue λ̄. ĀᵀA and AĀᵀ have real eigenvalues ≥ 0 (positive semidefinite). Example: $S=\begin{bmatrix}2&3-3i\\3+3i&5\end{bmatrix}$ is Hermitian with λ = 8 and −1, with eigenvectors x = (1, 1+i) and y = (1−i, −1), and x̄ᵀy = 0 (p. 263).

*Intuition note.* With complex entries, "length squared" must stay positive, so each entry is conjugated before multiplying. Conjugate-transposing is the change that lets the real-matrix theory carry over to complex matrices.

**Four subspaces (p. 264).** C(A) and N(A) are unchanged. The row space becomes C(Āᵀ) and the left nullspace becomes N(Āᵀ), so orthogonality (defined by x̄ᵀy = 0) still holds in pairs. Ranks and dimensions are unchanged. In function space the inner product is ∫x̄(t)y(t)dt. The functions $e^{inx}$ on $0\le x\le2\pi$ form the Fourier basis, a complete orthogonal basis: $\int_0^{2\pi}e^{ikx}e^{-inx}dx=\left[\frac{e^{i(k-n)x}}{i(k-n)}\right]_0^{2\pi}=0$ if k ≠ n (p. 264).

**Hermitian ⇒ real eigenvalues (p. 264).**
- If Sx = λx then x̄ᵀSx = λx̄ᵀx, and x̄ᵀx = ‖x‖² > 0.
- The number x̄ᵀSx is real because it equals its own conjugate x̄ᵀS̄ᵀx. Hence
$$\lambda=\frac{\bar x^TSx}{\bar x^Tx}=\text{real number}\tag{1}$$
- This ratio is the Rayleigh quotient. Maximizing it gives λ_max (best x is its eigenvector), minimizing gives λ_min. The in-between eigenvalues are "saddle points" of (1) (p. 264).
- Orthogonal eigenvectors, so that S = QΛQ⁻¹ = QΛQ̄ᵀ, take two steps:
  1. Schur's theorem: every square matrix is A = QTQ̄ᵀ with T triangular (proved on the book's website).
  2. If A = S = S̄ᵀ then T is the diagonal Λ (proved in the Problem Set).

**Permutation P (pp. 265–266).** For the 4 by 4 cyclic permutation, Px = λx reads (x₂, x₃, x₄, x₁) = λ(x₁, x₂, x₃, x₄) (2). Start with x₁ = 1; then x₂ = λ, x₃ = λ², x₄ = λ³, and the last equation gives 1 = λ⁴ (p. 265).
- det(P − λI) = λ⁴ − 1, so λ = 1, i, i² = −1, i³ = −i. They add to 0 = trace P.
- i and −i are a conjugate pair.
- The Fourier matrix F has the eigenvectors as columns, with $F^{-1}PF=\Lambda$, i.e. PF = FΛ (3).
- For N by N: $\lambda^N=1$ has solutions $w,w^2,\dots,w^{N-1},1$ with $w=e^{2\pi i/N}$ (4). They are equally spaced on the unit circle, at angles θ, 2θ, …, Nθ = 2π with θ = 2π/N (p. 265).
- With rows and columns counted from 0, $\lambda_k=w^k$, and $F_N$ has $w^{jk}$ in row j, column k (p. 266).

**Orthogonal columns (p. 266).** $\bar F_N^TF_N=NI$.
- First proof: $P_N$ is orthogonal, so its eigenvectors are orthogonal.
- Second proof: the dot product of columns j and k is $1+a+a^2+\dots+a^{N-1}=\frac{a^N-1}{a-1}$ with $a=\bar w^jw^k$.
  - If j = k then a = 1 and the sum is N.
  - If j ≠ k then $a^N=\bar w^{Nj}w^{Nk}=1$, so the sum is 0/(a−1) = 0.

**Circulants (p. 266).** If Px = λx then Pⁿx = λⁿx. More than that, every combination $C=c_0I+c_1P+c_2P^2+c_3P^3$ has $Cx=(c_0+c_1\lambda+c_2\lambda^2+c_3\lambda^3)x$, with the same x as P. For the eigenvector x = (1, i, i², i³) of P: $Cx=(c_0+c_1i+c_2i^2+c_3i^3)x$ (5). A circulant has $c_0$ on the main diagonal, and the entries of each upper diagonal circle round to a lower diagonal. All circulants share the eigenvectors in F, so CF = FΛ. Their eigenvalues are $c_0+c_1\lambda+c_2\lambda^2+c_3\lambda^3$ for λ = 1, i, i², i³ (p. 266).

*Intuition note.* P just shifts entries around a cycle, so its eigenvectors are the pure "waves" in F. Every circulant is a polynomial in P, so it has the same eigenvectors and only its eigenvalues differ.

**FFT (p. 267).** The discrete Fourier transform (DFT) of a signal x is the vector F̄x (F with conjugated entries). The fast version (FFT) uses a factorization of $F_N$, whose middle factor holds two copies of $F_{N/2}$:
$$F_N=\begin{bmatrix}I&B\\I&-B\end{bmatrix}\begin{bmatrix}F_{N/2}&0\\0&F_{N/2}\end{bmatrix}\begin{bmatrix}\text{even }0,2,\dots\\ \text{odd }1,3,\dots\end{bmatrix}\tag{6}$$
The first factor has only diagonal blocks, and the third is a permutation. For N = 4 the displayed identity (7) has B = diag(1, i) and two copies of $F_2=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ (p. 267). For N = 1024, ordinary multiplication costs (1024)² steps (over a million). Recursion reduces the middle factor repeatedly; there are 10 layers of diagonal B's because 1024 = 2¹⁰. The cost is about $N\log_2N=10(1024)$ complex multiplications instead of N², a factor near 100. N should be a power of 2 (p. 267).

**Multiplying circulants (pp. 267–268).** Example: C = 2I + P + 3P³ and D = 3I + P + P² + 4P³, done like 3012 × 4113 without carrying. The product is
CD = 6I + 5P + 3P² + 18P³ + 7P⁴ + 3P⁵ + 12P⁶ = 13I + 8P + 15P² + 18P³, using P⁴ = I (p. 267).
- This is cyclic convolution: $c\circledast d=(2,1,0,3)\circledast(3,1,1,4)=(13,8,15,18)=d\circledast c$ (8).
- CD = DC has these as its top row (9). Ordinary convolution c ∗ d = (6,5,3,18,7,3,12) has 7 coefficients; P⁴ = I folds it to 4 (p. 268).

**Convolution Rule (p. 268).**
- The top row of C times each eigenvector $q_k$ gives $\lambda_k\cdot1$, so the eigenvalues are $\lambda=Fc$ (10). For N = 2, $F=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$ gives $(\lambda_0,\lambda_1)=(c_0+c_1,\,c_0-c_1)$ (11).
- C, D and CD share eigenvectors, so $CDq_i=\lambda_i(C)\lambda_i(D)q_i$. In vector form this is $\lambda(CD)=\lambda(C)\,.*\,\lambda(D)$ (12). The Hadamard product .* multiplies component by component.
- Substituting (10) gives the **Convolution Rule**:
$$F(c\circledast d)=(Fc)\,.*\,(Fd)\tag{13}$$
Convolving vectors is multiplying transforms.

*Intuition note.* In the Fourier basis a circulant only scales each wave, and scalings multiply component by component. Cyclic convolution becomes a component-by-component product.

**Problem Set 6.4 (p. 269):** 15 problems; see Exercises.

### 6.5 Solving linear differential equations

**Setting (pp. 270–271).** The box on p. 270 lists five facts: (1) if Ax = λx then u = e^{λt}x solves du/dt = Au; (2) if A = XΛX⁻¹ then u(t) = e^{At}u(0) = Xe^{Λt}X⁻¹u(0) = c₁e^{λ₁t}x₁ + ⋯ + cₙe^{λₙt}xₙ; (3) e^{At} = I + At + ⋯ = Xe^{Λt}X⁻¹; (4) A is stable when all eigenvalues have real part < 0; (5) a second-order equation becomes a first-order system. The only calculus fact needed is that the derivative of e^{λt} is λe^{λt}. Scalar case: du/dt = λu gives u = Ce^{λt}, and C = u(0) (1). The system du/dt = Au (2) is linear with constant coefficients, and these are the only equations the text converts directly to linear algebra. If u and v are solutions, so is Cu + Dv (p. 270).

**Pure exponential solutions (p. 271).** Substituting u = e^{λt}x gives du/dt = λe^{λt}x, which agrees with Au = Ae^{λt}x when Ax = λx (3); the factor e^{λt} cancels to leave Ax = λx. It grows if λ > 0 and decays if λ < 0. For complex λ, the real part decides growth or decay and the imaginary part ω gives oscillation e^{iωt} (p. 271).

**Example 1 (p. 271).** $du/dt=\begin{bmatrix}0&1\\1&0\end{bmatrix}u$, u(0) = (4, 2): dy/dt = z and dz/dt = y.
- Adding and subtracting: d(y+z)/dt = (y+z) and d(y−z)/dt = −(y−z). So y+z grows like eᵗ and y−z decays like e⁻ᵗ.
- A has λ = 1, −1 with x = (1,1) and (1,−1). The solution is $u(t)=Ce^t(1,1)+De^{-t}(1,-1)=(Ce^t+De^{-t},\,Ce^t-De^{-t})$ (4)–(5).
- At t = 0: C + D = 4 and C − D = 2, so C = 3, D = 1.

**Three steps (p. 272).** (1) Write u(0) = c₁x₁ + ⋯ + cₙxₙ (this needs n independent eigenvectors). (2) Multiply each xᵢ by $e^{\lambda_it}$. (3) Combine:
$$u(t)=c_1e^{\lambda_1t}x_1+\dots+c_ne^{\lambda_nt}x_n\tag{6}$$
Not included: if two λ's are equal with only one eigenvector, another solution is needed (it will be $te^{\lambda t}x$) (p. 272).

**Example 2 (p. 272).** $A=\begin{bmatrix}1&1&1\\0&2&1\\0&0&3\end{bmatrix}$, λ = 1, 2, 3, u(0) = (9, 7, 4). Eigenvectors: x₁ = (1,0,0), x₂ = (1,1,0), x₃ = (1,1,1). Solving Xc = u(0) (7) gives (c₁, c₂, c₃) = (2, 3, 4). Therefore u(t) = 2eᵗx₁ + 3e²ᵗx₂ + 4e³ᵗx₃ (p. 272).

*Intuition note.* Eigenvectors turn n coupled equations into n separate 1 by 1 equations. The cᵢ are just the coordinates of the starting vector in the eigenvector basis.

**Second-order equations (p. 273).** For my″ + by′ + ky = 0 (Newton's law), substitute y = e^{λt}: (mλ² + bλ + k)e^{λt} = 0 (8). The two roots give y₁ = e^{λ₁t}, y₂ = e^{λ₂t}, and the complete solution is c₁y₁ + c₂y₂. This is not true if λ₁ = λ₂ (p. 273).
- Linear-algebra version with m = 1: u = (y, y′) and
$$\frac{d}{dt}\begin{bmatrix}y\\y'\end{bmatrix}=\begin{bmatrix}0&1\\-k&-b\end{bmatrix}\begin{bmatrix}y\\y'\end{bmatrix}=Au\tag{9}$$
- det(A − λI) = λ² + bλ + k, the same equation as (8). The eigenvectors are (1, λ₁) and (1, λ₂), and the first component of u(t) is the same y. A is called a companion matrix (p. 273).
- **Example 3:** y″ + y = 0 has λ = ±i, and half of e^{it} + e^{−it} gives y = cos t. With y(0) = 1, y′(0) = 0 the matrix is $\begin{bmatrix}0&1\\-1&0\end{bmatrix}$, antisymmetric, with eigenvectors (1, i), (1, −i), and u(0) = ½(x₁ + x₂) (10). The vector (cos t, −sin t) goes round a circle of radius 1, with period 2π (pp. 273–274).

**Difference equations (pp. 274–275).** To draw a circle, replace y″ = −y by a difference equation:
- (11F) forward: $\frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=-Y_{n-1}$
- (11C) centered: right side $-Y_n$
- (11B) backward: right side $-Y_{n+1}$

Forward in one-step form: $U_{n+1}=\begin{bmatrix}1&\Delta t\\-\Delta t&1\end{bmatrix}U_n=AU_n$ (12), with $U_n=(Y_n,Z_n)$. This time we take powers Aⁿ, not $e^{At}$, so the test is the magnitude |λ|. Here λ = 1 ± iΔt, so $|\lambda|=\sqrt{1+(\Delta t)^2}>1$ and the points spiral out (p. 275). Backward gives the matrix $\begin{bmatrix}1&-\Delta t\\ \Delta t&1\end{bmatrix}U_{n+1}=U_n$ (13); its eigenvalues are 1 ± iΔt, but it is inverted to go forward, so |λ| < 1 and the points spiral in. The centered (leapfrog) method stays close to the circle if Δt < 2 (the text cites Problem 28). The text says a fourth method (trapezoidal) completes the circle exactly (p. 275).

**Stability of 2 by 2 matrices (p. 276).** u(t) → 0 when all eigenvalues have negative real part. For λ = r + is, $|e^{ist}|^2=\cos^2st+\sin^2st=1$, so $|e^{\lambda t}|=e^{rt}$. For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, A is stable when both hold:
- (14T) trace $T=a+d=\lambda_1+\lambda_2<0$
- (14D) determinant $D=ad-bc=\lambda_1\lambda_2>0$

Reason: for real negative λ's the sum is negative and the product positive. Conversely, D > 0 means the λ's have the same sign, and T < 0 makes that sign negative. For complex λ = r ± is, D = r² + s² is automatically positive and T = 2r, so T < 0 means r < 0 (p. 276).

**Matrix exponential (pp. 276–277).**
$$e^{At}=I+At+\tfrac12(At)^2+\tfrac16(At)^3+\cdots\tag{15}$$
Its derivative is $A+A^2t+\tfrac12A^3t^2+\dots=Ae^{At}$, and its eigenvalues are $e^{\lambda t}$. So $u(t)=e^{At}u(0)$ solves du/dt = Au. The series always converges, so this works even with a shortage of eigenvectors (p. 277).
- If A = XΛX⁻¹, cancel X⁻¹X in each product of the series: $e^{At}=X[I+\Lambda t+\tfrac12(\Lambda t)^2+\cdots]X^{-1}=Xe^{\Lambda t}X^{-1}$. Hence $e^{At}u(0)=Xe^{\Lambda t}X^{-1}u(0)$ (16), which agrees with the three steps (17) (p. 277).

*Intuition note.* e^{At} is the matrix that carries u(0) forward to time t. In the eigenvector basis it just multiplies each coordinate by e^{λt}.

**Example 4 (p. 277).** $A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ has A⁴ = I. The powers repeat with period 4, and the series gives
$$e^{At}=\begin{bmatrix}\cos t&\sin t\\-\sin t&\cos t\end{bmatrix}\tag{18}$$
**Facts (p. 278):**
1. The inverse of e^{At} is always e^{−At}.
2. The eigenvalues of e^{At} are always e^{λt}.
3. When A is antisymmetric (Aᵀ = −A), e^{At} is orthogonal (inverse = transpose = e^{−At}).

Antisymmetric A has pure imaginary eigenvalues, so |e^{λt}| = 1: neutral stability, and ‖u(t)‖ = ‖u(0)‖ (p. 278).

**Examples 5–7 (pp. 278–279).**
- **Example 5:** A = [1 1; 0 2] is triangular, with λ = 1, 2 and eigenvectors (1,0), (1,1). Then $e^{At}=Xe^{\Lambda t}X^{-1}$ is triangular. (Added step: the product is $\begin{bmatrix}e^t&e^{2t}-e^t\\0&e^{2t}\end{bmatrix}$.)
- **Example 6:** y″ + 4y′ + 3y = 0 gives (λ+1)(λ+3) = 0, so λ = −1, −3 and y = c₁e⁻ᵗ + c₂e⁻³ᵗ → 0. The companion matrix $\begin{bmatrix}0&1\\-3&-4\end{bmatrix}$ has det(A − λI) = λ² + 4λ + 3, the same quadratic, with eigenvectors (1, λ₁), (1, λ₂) (p. 278).
- **Example 7:** y″ − 2y′ + y = 0 has the repeated root λ = 1, 1. The matrix $A=\begin{bmatrix}0&1\\-1&2\end{bmatrix}$ (20) has trace 2, det 1, and only multiples of (1,1) as eigenvectors, so it cannot be diagonalized. Use the series: $e^{At}=e^{It}e^{(A-I)t}=e^t[I+(A-I)t]$ (21), because (A−I)² = 0 (the series stops). This gives $y(t)=e^ty(0)-te^ty(0)+te^ty'(0)$, which contains the term teᵗ (p. 279).

**Heat and wave equations (p. 279).** These are partial differential equations: ∂u/∂t = ∂²u/∂x² and ∂²u/∂t² = ∂²u/∂x².
- Heat equation: temperatures in boxes follow du/dt = Au, with heat flowing at the rate of the temperature difference. The outer boxes are frozen at 0°, and the center starts at 2√2. The figure's 3 by 3 matrix is $A=\begin{bmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{bmatrix}$.
- Wave equation: d²u/dt² = Au has the same eigenvectors. For eigenvalues λ < 0, $e^{i\omega t}x$ and $e^{-i\omega t}x$ are solutions, with ω² = −λ. With three eigenvectors there are six solutions. If u′(0) = 0 they combine to 2 cos ωt · x (p. 279).

**Problem Set 6.5 (pp. 280–283):** 26 problems; see Exercises.

**QR algorithm (pp. 284–285).**
- Step 1 (details omitted): $A_0=B^{-1}AB$ is similar to A and almost triangular, a Hessenberg matrix (one nonzero subdiagonal). Every step $A_{k+1}=B_k^{-1}A_kB_k$ is a similarity, so eigenvalues never change. The goal is a smaller and smaller subdiagonal, so the diagonal entries approach the eigenvalues (p. 284).
- If $A^T=A$ and Q is orthogonal, then $A_0^T=(Q^{-1}AQ)^T=(Q^TAQ)^T=Q^TAQ=Q^{-1}AQ=A_0$ (22), so symmetry is preserved. A symmetric Hessenberg matrix has only three nonzero diagonals, so the computations are fast (p. 284).
- Step: Gram–Schmidt gives $A_k=Q_kR_k$ (Q orthogonal, R upper triangular). Reverse the factors:
$$A_{k+1}=R_kQ_k=Q_k^{-1}A_kQ_k\tag{23}$$
The magic, justified only by an example, is that the subdiagonals shrink (p. 284).
- **Example:** $A_0=\begin{bmatrix}\cos\theta&\sin\theta\\ \sin\theta&0\end{bmatrix}=QR$ with $Q=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$ and $R=\begin{bmatrix}1&\cos\theta\sin\theta\\0&-\sin^2\theta\end{bmatrix}$. Then
$A_1=RQ=\begin{bmatrix}\cos\theta(1+\sin^2\theta)&-\sin^3\theta\\-\sin^3\theta&-\sin^2\theta\cos\theta\end{bmatrix}$.
The trace is still cos θ, the determinant still −sin²θ, and the off-diagonal entry fell from sin θ to −sin³θ: cubic convergence (very rare). The last entry −sin²θ cos θ is very close to a true eigenvalue (p. 285).
- It helped that (A₀)₂₂ = 0. If not, shift A₀ by cI so that it is zero, and shift back at the end. The "QR algorithm with shifts" is a numerical success, unlike computing det(A − λI) and finding its roots, which is a failure. Two textbooks are named: Trefethen–Bau (SIAM, 1997) and Golub–van Loan (4th ed., 756 pages) (p. 285).

**Thoughts about differential equations (p. 285).**
1. For mu″ + bu′ + ku = 0, the exponents solve mλ² + bλ + k = 0. Underdamping b² < 4mk, critical damping b² = 4mk, overdamping b² > 4mk. This decides whether the roots are real, repeated or complex. For complex λ = a + iω, u oscillates from e^{iωt} while decaying from e^{at}.
2. With a forcing term f(t), add a particular solution to the nullspace solution: $u_{particular}=\int_0^te^{A(t-s)}f(s)\,ds$ (input at time s, growth factor $e^{A(t-s)}$, add outputs).

Nonlinear equations are solved numerically, e.g. by Runge–Kutta. Constant solutions of du/dt = f(u) are u = Y with f(Y) = 0 (p. 285).

## Toy example (ours)
**Part A: du/dt = Au.** Take $A=\begin{bmatrix}-2&1\\1&-2\end{bmatrix}$, u(0) = (4, 0).
1. Eigenvalues: trace = −4, det = 4 − 1 = 3. So λ² + 4λ + 3 = 0, giving λ = −1, −3. Eigenvectors: for −1, (1,1), since A(1,1) = (−1,−1); for −3, (1,−1), since A(1,−1) = (−3,3).
2. Stability tests: trace −4 < 0 and det 3 > 0, so the system is stable.
3. Step 1: (4,0) = 2(1,1) + 2(1,−1), so c = (2, 2).
4. Steps 2–3: u(t) = 2e⁻ᵗ(1,1) + 2e⁻³ᵗ(1,−1) = (2e⁻ᵗ + 2e⁻³ᵗ, 2e⁻ᵗ − 2e⁻³ᵗ).
5. Check: u(0) = (4, 0). u′(0) = (−2−6, −2+6) = (−8, 4), and Au(0) = (−8, 4). ✓. Both parts decay, as stability predicts.

**Part B: convolution rule, N = 2.** F₂ = [1 1; 1 −1], c = (1, 2), d = (3, 1).
- Cyclic convolution: (1·3 + 2·1, 1·1 + 2·3) = (5, 7).
- Fc = (3, −1), Fd = (4, 2), so (Fc).*(Fd) = (12, −2).
- F(c ⊛ d) = F(5, 7) = (12, −2). ✓

## Concepts
- [[eigenvector-eigenvalue]] — direction only scaled by A; here it gives pure solutions $e^{\lambda t}x$ (p. 271)
- [[diagonalization]] — A = XΛX⁻¹, used to get $e^{At}=Xe^{\Lambda t}X^{-1}$ (p. 277)
- [[spectral-theorem]] — symmetric/Hermitian S = QΛQ̄ᵀ via Schur's theorem (p. 264)
- [[rayleigh-quotient]] — x̄ᵀSx / x̄ᵀx; real; max and min give extreme eigenvalues (p. 264)
- [[four-fundamental-subspaces]] — in the complex case C(Āᵀ) and N(Āᵀ) replace C(Aᵀ) and N(Aᵀ) (p. 264)
- [[orthogonality]] — in the complex case x̄ᵀy = 0 (p. 264)
- [[orthonormal-basis-orthogonal-matrix]] — in the complex case the unitary Q̄ᵀ = Q⁻¹ (p. 263)
- [[positive-semidefinite-matrix]] — ĀᵀA and AĀᵀ have real eigenvalues ≥ 0 (p. 263)
- [[characteristic-polynomial]] — det(A − λI); for real A it has real coefficients, so complex roots come in conjugate pairs (p. 263)
- [[gram-schmidt-and-qr]] — A = QR used in each QR-algorithm step (p. 284)
- [[hermitian-matrix]] (new) — S̄ᵀ = S; real eigenvalues, orthogonal eigenvectors (p. 263)
- [[unitary-matrix]] (new) — Q̄ᵀ = Q⁻¹; eigenvalues with |λ| = 1 (p. 263)
- [[fourier-matrix]] (new) — $F_N$ with $w^{jk}$ in row j, column k; eigenvectors of P_N; $\bar F^TF=NI$ (p. 266)
- [[circulant-matrix]] (new) — a combination of powers of P; diagonalized by F (p. 266)
- [[fft]] (new) — factorization (6) giving cost about N log₂N (p. 267)
- [[cyclic-convolution]] (new) — c ⊛ d, the top row of CD; F(c ⊛ d) = (Fc).*(Fd) (pp. 267–268)
- [[matrix-exponential]] (new) — $e^{At}=\sum(At)^n/n!$; solves du/dt = Au (p. 276)
- [[ode-stability]] (new) — u → 0 when all Re λ < 0; for 2 by 2, trace < 0 and det > 0 (p. 276)
- [[companion-matrix]] (new) — turns a scalar higher-order equation into u′ = Au (p. 273)
- [[qr-algorithm]] (new) — iterate A_{k+1} = R_kQ_k to reveal eigenvalues (p. 284)
- [[hessenberg-matrix]] (new) — one nonzero subdiagonal; the near-triangular form from Step 1 (p. 284)

## Canonical instances
- [[spring-mass-oscillator]] — my″ + by′ + ky = 0 becomes a companion-matrix system; y″ + y = 0 gives a circle (p. 273)
- [[cyclic-permutation-eigenvalues]] — P₄ has eigenvalues the 4th roots of 1; $P_N$ the N-th roots (p. 265)
- [[rotation-matrix-exponential]] — $e^{At}$ for A = [0 1; −1 0] is a rotation by t (p. 277)
- [[heat-equation-boxes]] — du/dt = Au with a second-difference matrix (p. 279)
- [[repeated-eigenvalue-ode]] — y″ − 2y′ + y = 0, with teᵗ from the short series (p. 279)
- [[qr-algorithm-2x2-example]] — off-diagonal entry drops from sin θ to −sin³θ (p. 284)

## Bridges (candidates)
- [same-math] Convolution Rule F(c ⊛ d) = (Fc).*(Fd) ↔ signal processing: convolving signals is multiplying their transforms — the text itself says this simplifies signal processing (p. 268).
- [same-math] Matrix in the heat-equation example (Figure 6.8) ↔ graph Laplacian: A = [−1 1 0; 1 −2 1; 0 1 −1] is minus the Laplacian of a 3-node path graph, so du/dt = Au smooths a signal on a network.
- [structural-analogy] Stability test |λ| < 1 for Uₙ = AⁿU₀ vs Re λ < 0 for e^{At} ↔ iteration of Aᵏ: both ask whether eigenvalues make the evolution shrink, in discrete or continuous time.
- [structural-analogy] Problem 3's "continuous Markov equation" (columns of A sum to 0) ↔ Markov matrix: a steady state is the eigenvector for the zero eigenvalue, as for eigenvalue 1 in the discrete case.
- [metaphor] QR algorithm's repeated "factor, then reverse the factors" ↔ power iteration: both repeatedly apply a matrix until eigen-structure appears.

## Questions this raises
- Why does the QR algorithm drive the subdiagonal to zero? The text only justifies it by one example.
- What replaces the pure exponentials when eigenvectors are missing, beyond the repeated-root example, i.e. what does $e^{At}$ look like for larger Jordan-type blocks?
- How does the Fourier-matrix diagonalization of circulants relate to the Fourier basis $e^{inx}$ in function space (p. 264)?
- Which difference method (forward, backward, leapfrog, trapezoidal) is best for long simulations, and what does Δt < 2 mean for the leapfrog method in larger systems?

## Exercises worth doing
- Ex. 6.4-3 (p. 269) — unitary Q has |λ| = 1; checks the complex inner product — difficulty: easy
- Ex. 6.4-7 (p. 269) — verify the Convolution Rule for 3 by 3 F₃ with w³ = 1 — difficulty: medium
- Ex. 6.5-11 (p. 281) — non-diagonalizable A = [0 1; 0 0]; e^{At} gives a straight line y = y(0) + y′(0)t — difficulty: medium
- Ex. 6.5-14 (p. 282) — skew-symmetric A keeps ‖u‖ constant and e^{At} orthogonal — difficulty: medium
- Ex. 6.5-22 (p. 283) — why e^{At} is never singular (inverse and eigenvalues) — difficulty: easy
- Ex. 6.5-25 (p. 283) — trapezoidal method gives an orthogonal A, so points stay on the circle — difficulty: hard

## Reading notes
- This is part 3 of Chapter 6. It begins at §6.4 (printed p. 262, pdf 272) and ends at the end of §6.5 (printed p. 285, pdf 295). The split is at a section boundary, but §6.4 and §6.5 are both included. Page offset: printed = pdf − 10.
- The text layer is heavily garbled in equations (bars, subscripts, minus signs). I checked the page images for the equations used here.
- On p. 278, Example 5, the text layer for the top-right entry of e^{At} reads "e^{2t} + e^t". The product Xe^{Λt}X⁻¹ with the printed X and X⁻¹ gives e^{2t} − e^t, so I used the minus. The page image also shows this entry as e^{2t} + e^t, so it is not only an extraction artefact; I flag the printed plus as a likely misprint. The starting vector of that example is not used here.
- Cross-references in the text: the leapfrog stability claim cites "Problem 28" (p. 275), but Problem Set 6.5 on these pages ends at Problem 26. The text says "Problem 26 has a fourth (very good) method" (p. 275), but the trapezoidal method appears as Problem 25 (p. 283).
- Problems 1–15 of Set 6.4 and 1–26 of Set 6.5 are listed but solutions are not given in these pages.
- Schur's theorem is only stated (proof on the book's website). The justification of QR convergence is by example only (p. 284).
