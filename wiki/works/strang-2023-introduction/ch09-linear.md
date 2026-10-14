---
id: strang-2023-introduction/ch09-linear
work: strang-2023-introduction
unit: "9 Linear Algebra in Optimization"
pages: 335–369
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Linear Algebra in Optimization (Strang, Ch. 9)

## L0 — One line
At a smooth minimum the gradient is zero. This gives a linear system for quadratics, gradient-type iterations for other functions, and Lagrange multipliers or duality once constraints appear.

## L1 — The gist (≤ 120 words)
How do we minimize a function of many variables, with or without constraints? At a smooth minimum the gradient is zero. For a quadratic this is a linear system Sx = b. Otherwise follow −∇F downhill (gradient descent, with momentum or random samples). Backpropagation computes the gradients cheaply by ordering a chain-rule product from the output. With linear constraints on a quadratic cost, Lagrange multipliers give a saddle-point (KKT) linear system. In the quadratic examples each multiplier is the derivative of the minimum cost. Linear programs have dual programs with equal optimal value, and two-person zero-sum games reduce to them. The choice of norm changes the solution: ℓ¹ gives sparse ones.

**Prerequisites:** partial derivatives and gradients; symmetric positive definite matrices and eigenvalues; matrix products and shapes; block elimination; the norms ‖·‖₁, ‖·‖₂, ‖·‖∞.

## L2 — Key ideas
- At a smooth minimum ∇F = 0. For F = ½xᵀSx − bᵀx this is Sx = b, so Newton's method solves it in one step. Newton converges fast near x* but needs the whole Hessian, the matrix of all second derivatives (p. 335–337).
- Gradient descent x_{k+1} = x_k − s_k∇F(x_k) uses only first derivatives but, with exact line search, zig-zags in narrow valleys. For ½(x²+by²) the rate is ((1−b)/(1+b))² per step, which is near 1 when b is small (p. 337, 342).
- Momentum (z_k = ∇F(x_k)+βz_{k−1}) with optimal s, β replaces b by √b in that rate. The condition number λmax/λmin (largest over smallest eigenvalue of S; 1/b here) controls everything (p. 343–344).
- Backpropagation is the chain rule as a product of Jacobians (matrices of first partial derivatives), evaluated from the output end. Then every step is vector×matrix and work is reused across layers (p. 347–350). Stochastic gradient descent uses one sample or a small batch per step (p. 348).
- For a quadratic cost with linear constraints, Lagrange multipliers (one unknown per constraint) give the KKT (Karush–Kuhn–Tucker) saddle-point system. In those quadratic examples the multiplier equals the derivative of the minimum cost with respect to the constraint level b (p. 357–358).
- The KKT matrix is symmetric but indefinite; block elimination gives the Schur complement −AᵀS⁻¹A (the block left in the lower right corner). For that Lagrangian, maximin = minimax (p. 359–360). With inequality constraints the question is which ones are active; an active-set method (keep a working set of equalities) is one answer (p. 361).
- ℓ¹ minimization on a linear constraint gives sparse solutions, because the ℓ¹ diamond touches a line at a corner. ℓ² does not (p. 356).
- A linear program has a dual maximum program. Weak duality is yᵀb ≤ cᵀx and the duality theorem says the two optima are equal. Max flow = min cut and two-person zero-sum games are instances (p. 365–368).

## L3 — Walkthrough

### Chapter introduction (p. 335)
The overall problem is to minimize F(x) with x = (x₁,…,xₙ). The gradient ∇F = (∂F/∂x₁,…,∂F/∂xₙ) vanishes at a smooth minimum x*. So we must solve n equations in n unknowns (p. 335).

For the model Q(x) = ½xᵀSx − bᵀx the gradient is ∇Q = Sx − b, so ∇Q = 0 is Sx = b. If S is symmetric positive definite, the solution is the minimum point (p. 335). If the second-derivative matrix S(x) is everywhere positive definite, F is convex, "roughly a bowl" (p. 335).

Constraints such as Ax = b, x ≥ 0 chop the bowl. The key question is whether xᵢ > 0 or xᵢ = 0 at the minimum. A Lagrange multiplier deals with it (p. 335).

### 9.1 Minimizing a Multivariable Function (p. 336–345)

**Taylor approximations.** For one variable:
$$F(x+\Delta x)\approx F(x)+\Delta x\,\frac{dF}{dx}(x)+\frac12(\Delta x)^2\frac{d^2F}{dx^2}(x)\tag{1}$$
For n variables:
$$F(x+\Delta x)\approx F(x)+(\Delta x)^{T}\nabla F+\tfrac12(\Delta x)^{T}S\,(\Delta x)\tag{2}$$
Here ∇F is the column vector of partial derivatives. S is the symmetric Hessian matrix, S_ij = ∂²F/∂xᵢ∂xⱼ = ∂²F/∂xⱼ∂xᵢ (p. 336).

If S is positive definite, F is strictly convex: it stays above its tangents. A convex F has a minimum at x* if ∇F(x*) = 0 (p. 336).

**Newton's method.** Expanding the gradient, ∇F(x+Δx) ≈ ∇F(x) + S(x)Δx. Setting this to zero gives
$$\nabla F(x+\Delta x)\approx\nabla F(x)+S(x)\Delta x=0\ \Rightarrow\ \Delta x=-S^{-1}(x)\nabla F(x)\tag{3}$$
Then x_{k+1} = x_k + Δx. The iterates often converge quickly, but every step needs all second derivatives in S(x), which can be very costly (p. 336).

*Example 1.* For F = ½xᵀSx − xᵀb, ∇F = Sx − b. Newton gives x₁ − x₀ = −S⁻¹(Sx₀ − b) = −x₀ + S⁻¹b, so x₁ = S⁻¹b = x* in one step (p. 336).

*Example 2.* Solve ∇F = x² − 4 = 0, so S(x) = 2x. The step is x_{k+1} − x_k = (−1/2x_k)(x_k² − 4), i.e.
$$x_{k+1}=\tfrac12\Big(x_k+\frac{4}{x_k}\Big).\tag{4}$$
From x₀ = 4: x₁ = ½(4+1) = 2.5; x₂ = ½(2.5+1.6) = 2.05; x₃ = 2.0006; x₄ = 2.000000009. The number of correct zeros doubles each step (p. 337). The error is squared:
$$x_{k+1}-2=\tfrac12\Big(x_k+\tfrac4{x_k}\Big)-2=\frac1{2x_k}(x_k-2)^2,\qquad \|x_{k+1}-x^*\|\approx\tfrac14\|x_k-x^*\|^2 .$$
This holds *provided x_k is close to x\** (p. 337).

*Intuition note.* Near the solution, the correct decimals double each step because the new error is about a quarter of the old error squared. The price is the Hessian. For large networks the author says it is too expensive, so gradient descent is the algorithm of choice in deep learning (p. 337).

**Gradient descent (= steepest descent).** Calculus says all ∂F/∂xᵢ vanish at a smooth minimum. The steepest direction at x_k is −∇F(x_k):
$$x_{k+1}=x_k-s_k\nabla F(x_k)\tag{5}$$
Here s_k is the stepsize or learning rate (p. 337). With n = 20 unknowns there are 20 first derivatives. The symmetric Hessian has ½(n²+n) = 210 second derivatives instead of n² = 400. Automatic differentiation, rediscovered as backpropagation, keeps the cost far below 20× or 210× (p. 338).

**Derivatives and differences (n = 1).** The derivative is a limit of the slope Δf/Δx:
$$\frac{df}{dx}=\lim\frac{\Delta f}{\Delta x}=\lim\Big[\frac{f(x+\Delta x)-f(x)}{\Delta x}\Big]\tag{6}$$
This is a forward difference if Δx > 0 and a backward difference if Δx < 0. ReLU(x) = max(0,x) has slope 1 on the right and 0 on the left of 0, so its derivative does not exist at 0 (p. 338). For f = x² at x = 0 the ratio equals Δx, which is only first-order accurate. Averaging forward and backward differences gives the centered difference:
$$\tfrac12\Big[\tfrac{f(x+\Delta x)-f(x)}{\Delta x}+\tfrac{f(x-\Delta x)-f(x)}{-\Delta x}\Big]=\frac{f(x+\Delta x)-f(x-\Delta x)}{2\Delta x}\tag{7}$$
It is exact for f = x². For all smooth functions its error is of size (Δx)², against Δx for uncentered differences (p. 338–339).

**The gradient vector, Examples 3–7 (p. 339–340).**
- Ex. 3: F = aᵀx has ∇F = a.
- Ex. 4: for symmetric S, F = ½xᵀSx has ∇F = Sx. For n = 2 with S = [a b; b c], F = ½ax₁² + ½cx₂² + bx₁x₂ and the gradient is (ax₁+bx₂, bx₁+cx₂) = Sx.
- Ex. 5: for S positive definite and F = ½xᵀSx − aᵀx, the gradient is Sx − a. The minimum is at
$$\nabla F=Sx-a=0\ \text{at}\ x^*=S^{-1}a=\arg\min F.\tag{8}$$
Then F_min = ½(S⁻¹a)ᵀS(S⁻¹a) − aᵀ(S⁻¹a) = ½aᵀS⁻¹a − aᵀS⁻¹a = −½aᵀS⁻¹a. The graph is a bowl through 0 at x = 0 that dips to F_min at x* (p. 339–340).
- Ex. 6: for F = det X, ∂(det X)/∂x_ij = C_ij, the cofactor.
- Ex. 7: for L = log det X, the chain rule gives ∂L/∂x_ij = C_ij/det X = the (j,i) entry of X⁻¹. The matrix of n⁴ second derivatives is negative definite when X = S is symmetric positive definite. Hence −log(det S) is a convex function of the entries of a positive definite S (p. 340).

**Geometry of the gradient (p. 340–342).** ‖∇F‖ = √((∂F/∂x)²+(∂F/∂y)²) is the steepest slope, and it points in the steepest direction. The steepest direction is perpendicular to the level direction (p. 340–341).
- Ex. 8: for F = ax+by, ∇F = (a,b) and ‖∇F‖ = √(a²+b²). In Figure 9.2, F = x+2y has steepest direction (1,2), slope √5, level direction (2,−1) (p. 341).
- Ex. 9: F = ax²+by² has ∇F = (2ax, 2by). The level curves are ellipses. The steepest direction changes as you go down, and it does not point to the bottom. From (x₀,y₀) the steepest line is (x₀,y₀) − s(2ax₀, 2by₀), and if a ≠ b the point (0,0) does not lie on it for any s (p. 341).

So one gradient step does not find the minimum unless the bowl is circular (b = a). In practice we keep going until F stops decreasing quickly, then recompute the gradient (p. 342).

**Zig-zag example.** Take F = ½(x²+by²), 0 < b ≤ 1, with ∇F = (x, by) and minimum 0 at (0,0). With exact line search, starting at (x₀,y₀) = (b,1):
$$x_k=b\Big(\frac{b-1}{b+1}\Big)^k,\quad y_k=\Big(\frac{1-b}{1+b}\Big)^k,\quad F(x_k,y_k)=\Big(\frac{1-b}{1+b}\Big)^{2k}F(x_0,y_0)\tag{9}$$
If b = 1 one step reaches (0,0). The crucial ratio is r = (1−b)/(1+b): for b = 1/10, r = 9/11; for b = 1/100, r = 99/101. For small b progress virtually stops. The bowl is a narrow valley and the iterates cross it instead of moving down it (p. 342; Figure 9.4, p. 343). Each new step is perpendicular to the level set where the previous step stopped, a 90° turn (p. 343).

*Intuition note.* The gradient only sees the steepest local slope, which in a stretched bowl points mostly across the valley. The ratio r tends to 1 as b = λmin/λmax shrinks, so the stretched bowl is the hard case.

**Momentum (heavy ball).** The model F has second-derivative matrix diag(1, b), and the problem is serious when b = λmin/λmax is small (p. 342). Polyak's idea: let the new direction remember the old one,
$$x_{k+1}=x_k-sz_k,\quad z_k=\nabla F(x_k)+\beta z_{k-1}\tag{10}$$
This is a two-step method. As a one-step method for (x, z):
$$x_{k+1}=x_k-sz_k,\qquad z_{k+1}-\nabla F(x_{k+1})=\beta z_k\tag{11}$$
This is like reducing one second-order differential equation to two first-order ones (p. 343).

*Quadratic model.* Let F = ½xᵀSx with S symmetric positive definite, so ∇F = Sx. Track an eigenvector q with Sq = λq, and write x_k = c_kq, z_k = d_kq, ∇F_k = λc_kq. Equation (11) becomes
$$c_{k+1}=c_k-sd_k,\quad -\lambda c_{k+1}+d_{k+1}=\beta d_k,\ \text{i.e.}\ \begin{bmatrix}1&0\\-\lambda&1\end{bmatrix}\begin{bmatrix}c_{k+1}\\d_{k+1}\end{bmatrix}=\begin{bmatrix}1&-s\\0&\beta\end{bmatrix}\begin{bmatrix}c_k\\d_k\end{bmatrix}\tag{12}$$
Inverting the first matrix (−λ becomes +λ):
$$\begin{bmatrix}c_{k+1}\\d_{k+1}\end{bmatrix}=\begin{bmatrix}1&0\\\lambda&1\end{bmatrix}\begin{bmatrix}1&-s\\0&\beta\end{bmatrix}\begin{bmatrix}c_k\\d_k\end{bmatrix}=\begin{bmatrix}1&-s\\\lambda&\beta-\lambda s\end{bmatrix}\begin{bmatrix}c_k\\d_k\end{bmatrix}=R\begin{bmatrix}c_k\\d_k\end{bmatrix}\tag{13}$$
After k steps the start is multiplied by Rᵏ. We want both eigenvalues e₁, e₂ of R small. They depend on λ, which can be anywhere in [λmin(S), λmax(S)]. So choose s and β to minimize max(|e₁(λ)|, |e₂(λ)|) over that interval. The author writes that it "seems a miracle" that this problem has a beautiful solution (p. 344):
$$s=\Big(\frac{2}{\sqrt{\lambda_{\max}}+\sqrt{\lambda_{\min}}}\Big)^2,\qquad \beta=\Big(\frac{\sqrt{\lambda_{\max}}-\sqrt{\lambda_{\min}}}{\sqrt{\lambda_{\max}}+\sqrt{\lambda_{\min}}}\Big)^2\tag{14}$$
For λmax = 1, λmin = b:
$$s=\Big(\frac{2}{1+\sqrt b}\Big)^2,\qquad \beta=\Big(\frac{1-\sqrt b}{1+\sqrt b}\Big)^2\tag{15}$$
Compare the factors:
$$\text{ordinary }\Big(\frac{1-b}{1+b}\Big)^2\qquad\text{accelerated }\Big(\frac{1-\sqrt b}{1+\sqrt b}\Big)^2\tag{16}$$
So b in (9) is replaced by √b. For small b the ordinary factor is essentially 1 − 4b and the accelerated one essentially 1 − 4√b (p. 344).

*Numbers (b = 1/100, √b = 1/10).* Ordinary: (.99/1.01)² ≈ .96. Accelerated: (.9/1.1)² ≈ .67. Ten ordinary steps multiply the starting error by 0.67, matched by one momentum step. Ten momentum steps multiply it by 0.018. The condition number λmax/λmin = 1/b controls everything (p. 344).

*Reader's shortcut (our suggestion, not the author's):* the formulas to carry forward are (14) and (16); (13) is the step that leads to them.

*Intuition note.* With the right s and β, the number b in the ordinary rate is replaced by √b, as in the rate formulas (15)–(16). The author says the 2×2 case contains "the essence" of the general quadratic problem because only the extreme eigenvalues matter (p. 343).

**Notes (p. 345).** Nesterov also created an improvement on gradient descent, different from momentum. "Adaptive" methods use all earlier directions: D_k = δD_{k−1} + (1−δ)∇L_k. The batch size B in SGD can increase at later steps.

### 9.2 Backpropagation and Stochastic Gradient Descent (p. 346–354)

**Setting.** We have training data: inputs v₁,…,v_N with known outputs w_i. We choose weights x so that the errors e_i = F(x,v_i) − w_i are small by minimizing the total loss:
$$L(x)=\frac1N\sum_{i=1}^N\ell(e_i)=\frac1N\sum_{i=1}^N\ell\big(F(x,v_i)-w_i\big)\tag{1}$$
The best x depends on the form of F and on the loss ℓ. With square loss ℓ(e) = ‖e‖² this is a least-squares fit (p. 346). The goal is to predict the output W for new test data V by F(V). A very high-degree polynomial for F is "one of the worst approaches": a small change in V makes a large change in W (p. 346).

Three steps: (1) choose the form of F, including a nonlinearity such as ReLU; (2) compute the weights that fit the training data; (3) evaluate W = F(x,V) on test data. F is a chain of simpler functions, each with its own weights x_k (p. 346):
$$F(x,v)=F_L\big(F_{L-1}(\cdots F_2(F_1(v)))\big)\tag{2}$$
Backpropagation finds the derivatives of F (and ℓ) with respect to the weights efficiently. Then gradient descent or SGD optimizes. The author credits A. Craig and A. Griewank (automatic differentiation) (p. 347).

**Multivariable chain rule.** Let h(x) = f(g(x)) with x ∈ ℝᵐ, g with n components, h with p components. The Jacobians ∂f/∂g (p×n) and ∂g/∂x (n×m) hold the partial derivatives (p. 347). Then
$$\frac{\partial h_i}{\partial x_k}=\frac{\partial h_i}{\partial g_1}\frac{\partial g_1}{\partial x_k}+\dots+\frac{\partial h_i}{\partial g_n}\frac{\partial g_n}{\partial x_k},\ \text{i.e.}\ \frac{\partial h}{\partial x}=\frac{\partial f}{\partial g}\frac{\partial g}{\partial x}\tag{3–4}$$
Each entry is (row i of ∂f/∂g) · (a column of ∂g/∂x). The matrix is p×m. For the chain F_L(…F₁) this is a product of L matrices (p. 347):
$$\frac{\partial F}{\partial x}=\frac{\partial F_L}{\partial F_{L-1}}\frac{\partial F_{L-1}}{\partial F_{L-2}}\cdots\frac{\partial F_1}{\partial x}\tag{5}$$

**Stochastic gradient descent.** L(x) is a sum over all samples, and computing every derivative at every step is enormous. SGD randomly selects one sample or a small batch of B samples to update x_k → x_{k+1}. It "works surprisingly well". Early steps give big improvements. Near the optimum the iterations become erratic and high precision is not expected, so we can often stop early (p. 348).

*SGD for least squares.* Minimize ‖Ax − b‖². At each step pick one row a_i at random and update so that equation i holds:
$$x_{k+1}=x_k+\frac{b_i-a_ix_k}{\|a_i\|^2}\,a_i^{T}\quad\text{solves}\quad a_ix_{k+1}=b_i\tag{6}$$
Kaczmarz proposed this with rows taken cyclically. Strohmer and Vershynin chose rows randomly and proved a form of exponential convergence to the solution of AᵀAx̂ = Aᵀb. Figure 9.5 shows a fast start and an oscillating finish, "So stop early" (p. 348).

**Key ideas of backpropagation (p. 349–350).** Simplification: each weight enters only one F_j, with F_j = ReLU(A_jF_{j−1} + b_j), weights x_j = (A_j, b_j). The chain rule for the loss ℓ is
$$\frac{\partial\ell}{\partial x_j}=\frac{\partial\ell}{\partial F_L}\frac{\partial F_L}{\partial F_{L-1}}\frac{\partial F_{L-1}}{\partial F_{L-2}}\cdots\frac{\partial F_{j+1}}{\partial F_j}\frac{\partial F_j}{\partial x_j}\tag{7}$$
This involves only the weights x_j,…,x_L, not earlier ones. So start from the last layer and go backward (p. 349).

For square loss, with w the true output and F(x,v) the computed output:
$$\ell(x)=(w-F)^T(w-F),\qquad \frac{\partial\ell}{\partial F}=-2(w-F(x,v))\tag{8}$$
(the sign is garbled in the extracted text; see Reading notes). The key point is that ∂ℓ/∂F is a *vector*. With M_k = ∂F_k/∂F_{k−1}, the chain is
$$\frac{\partial\ell}{\partial x_j}=\Big(\big((\tfrac{\partial\ell}{\partial F_L}M_L)M_{L-1}\big)\cdots M_{j+1}\Big)\frac{\partial F_j}{\partial x_j}\tag{9}$$
Every step is vector × matrix. For n×n matrices that costs n² multiplications per step, against n³ for matrix × matrix in the opposite order (p. 349).

*Summary (reverse mode vs forward mode).* Reverse mode is more efficient for two reasons: (1) most operations are vector–matrix (or vector–tensor); (2) work is reused, because the derivatives at layers j < k share the prefix ∂ℓ/∂F_k. When the parentheses are grouped from the left (p. 349–350):
$$\frac{\partial\ell}{\partial x_j}=\Big(\big((\tfrac{\partial\ell}{\partial F_L}\tfrac{\partial F_L}{\partial F_{L-1}})\tfrac{\partial F_{L-1}}{\partial F_{L-2}}\big)\cdots\tfrac{\partial F_{j+1}}{\partial F_j}\Big)\tfrac{\partial F_j}{\partial x_j}\tag{10}$$
Only the last step, for A_j, is a vector–tensor contraction because A_j is a matrix (p. 350).

*The algorithm.* Do a forward pass with input v and store all F_j. Compute ∂ℓ/∂F_L. Then for j = L down to 1: compute and store ∂ℓ/∂b_j = (∂ℓ/∂F_j)(∂F_j/∂b_j) and ∂ℓ/∂A_j = (∂ℓ/∂F_j)(∂F_j/∂A_j). If j ≠ 1, compute ∂ℓ/∂F_{j−1} = (∂ℓ/∂F_j)(∂F_j/∂F_{j−1}) for the next iteration (p. 350).

The author says one backward pass needs only 2L vector–matrix multiplies and L vector–tensor contractions. Forward mode would need O(L²) matrix–tensor contractions and matrix–matrix multiplies, so backpropagation is "more efficient by multiple orders of magnitude" (p. 350).

*Intuition note.* The chain-rule product can be evaluated in either order, and the answer is the same. Starting from the scalar loss at the output keeps every intermediate object a vector, and the shared prefix is computed once. Keras uses TensorFlow, which builds a computational graph and inserts derivative operations, usually working backward. For the layered structure above it would produce the same operations as the pseudocode (p. 350–351).

**Derivatives of Av + b (p. 351–352).** For a layer, w_j = A_jv_{j−1} + b_j and v_j = ReLU(w_j). Drop the index j and write w = Av + b. Then
$$\frac{\partial w_i}{\partial b_j}=\delta_{ij}\ (=1\text{ if }i=j,\ 0\text{ if }i\ne j)\tag{11}$$
$$T_{ijk}=\frac{\partial w_i}{\partial A_{jk}}=v_k\,\delta_{ij},\quad\text{e.g. }T_{111}=v_1,\ T_{122}=0\tag{12}$$
This derivative is a 3-way tensor (a "box of numbers"). Row j of A affects w_i only if j = i, and then A_jk multiplies v_k. Tensors are not trivial extensions of matrices: their rank is hard to define and the SVD fails. A rank-one tensor has entries a_ib_jc_k (p. 351–352).

*Example (2×2).* With w₁ = b₁ + a₁₁v₁ + a₁₂v₂: ∂w₁/∂b₁ = 1, ∂w₁/∂b₂ = 0, ∂w₁/∂a₁₁ = v₁, ∂w₁/∂a₁₂ = v₂, ∂w₁/∂a₂₁ = ∂w₁/∂a₂₂ = 0 (p. 352).

**Hidden layers (L = 2).** v₁ = ReLU(b₁ + A₁v₀) and w = b₂ + A₂v₁ = b₂ + A₂ReLU(b₁ + A₁v₀). Equations (11)–(12) give the derivatives for b₂, A₂ directly. For A₁ the chain rule has three factors:
$$\frac{\partial w}{\partial A_1}=A_2\,\mathrm{ReLU}'(b_1+A_1v_0)\,\frac{\partial(b_1+A_1v_0)}{\partial A_1}\tag{13}$$
The formulas go backward from w to v, and automatic backpropagation does the same ("reverse mode") (p. 352).

**Details of ∂w/∂A (p. 352–353).** ReLU(x) = (x)₊. Its derivative is 0 for x < 0 and 1 for x > 0 ("Don't ask about … 0"). Write A, b for A_{L−1}, b_{L−1}. Then
$$w=A_L\,\mathrm{ReLU}(Av+b)+b_L,\qquad\frac{\partial w}{\partial A}=A_L\,J\,\frac{\partial(Av+b)}{\partial A},\quad J=\mathrm{ReLU}'(Av+b)\tag{14–15}$$
J is a diagonal matrix with 1's for positive components and 0's for negative components. The third factor is known from (11)–(12). If a smooth sigmoid replaces ReLU, J holds the derivative values instead of 1's and 0's. Figure 9.6 shows ReLU and Leaky ReLU (slope 1/100 on the left) as two activation options (p. 353).

### 9.3 Constraints, Lagrange Multipliers, Minimum Norms (p. 355–362)

**Norms.** On the line 3x + 4y = 1 find the point with minimum norm. The answer depends on the norm (p. 355).
- ℓ¹: ‖v‖₁ = |x|+|y|.
- ℓ²: ‖v‖₂ = √(x²+y²).
- ℓ^∞: ‖v‖_∞ = max(|x|,|y|).
- ℓᵖ: (|x|ᵖ+|y|ᵖ)^{1/p} for p ≥ 1.

All norms obey ‖cv‖ = |c|‖v‖ and the triangle inequality. For v = (1,1) the three norms are 2, √2, 1. The unit regions are a diamond, a circle and a square. For p = ½, v = (1,0) and w = (0,1) have norm 1 but v+w has norm (1+1)² = 4, which violates the triangle inequality. So p = ½ is not a norm and its region is not convex (p. 355).

Scaling the unit shape until it touches the line gives the minimizers (Figure 9.8, p. 356):
- ℓ¹: (0, ¼) with norm ¼.
- ℓ²: (3/25, 4/25) with norm 1/5.
- ℓ^∞: (1/7, 1/7) with norm 1/7.

The ℓ¹ solution is **sparse** (one nonzero component) because a diamond touches a line at a sharp corner. For the plane 3x+4y+5z = 1 the corner is (0,0,1/5), with two zeros. The ℓ² (least-squares) solution has many small, uninteresting components (p. 356).

The "ℓ⁰ norm" counts nonzeros. It is not a norm and not convex, since ‖2v‖₀ = ‖v‖₀. The ℓ¹ diamond "convexifies" the ℓ⁰ skeleton along the axes, which is why ℓ¹ finds sparse solutions of Av = b. For matrices, convexity will again be tied to the triangle inequality for a matrix norm (p. 356).

**Lagrange multipliers (2 variables).** Minimize F = x₁²+x₂² on the line a₁x₁+a₂x₂ = b. Build the constraint into the Lagrangian:
$$L(x,\lambda)=x_1^2+x_2^2-\lambda(a_1x_1+a_2x_2-b)\tag{1}$$
Set the derivatives to zero:
$$\partial L/\partial x_1=2x_1-\lambda a_1=0,\quad \partial L/\partial x_2=2x_2-\lambda a_2=0,\quad \partial L/\partial\lambda=-(a_1x_1+a_2x_2-b)=0\tag{2}$$
Then x₁ = ½λa₁ and x₂ = ½λa₂. Substituting in the constraint gives
$$\tfrac12\lambda a_1^2+\tfrac12\lambda a_2^2=b,\quad\lambda=\frac{2b}{a_1^2+a_2^2}\tag{3}$$
So x₁* = a₁b/(a₁²+a₂²), x₂* = a₂b/(a₁²+a₂²), and the minimum cost is b²/(a₁²+a₂²). The derivative of the minimum cost with respect to the constraint level b is the multiplier:
$$\frac{d}{db}\Big(\frac{b^2}{a_1^2+a_2^2}\Big)=\frac{2b}{a_1^2+a_2^2}=\lambda\tag{4}$$
At x* the line is tangent to the cost circle (Figure 9.9) (p. 357–358). The author warns that discarding the multipliers after using them is "a big mistake" (p. 357).

*Intuition note.* λ tells how much the minimum cost changes if the constraint level b is nudged. For this example it equals 2b/(a₁²+a₂²).

**Quadratic programming with S positive definite.** Aᵀ is m×n and there are m multipliers λ = (λ₁,…,λ_m):
$$\text{Minimize }F=\tfrac12x^TSx\ \text{ subject to }A^Tx=b\tag{5}$$
The Lagrangian is L = ½xᵀSx − λᵀ(Aᵀx − b). Its n+m derivative equations are
$$Sx-A\lambda=0,\qquad A^Tx=b\tag{6}$$
The first gives x = S⁻¹Aλ, then AᵀS⁻¹Aλ = b. So
$$\lambda^*=(A^TS^{-1}A)^{-1}b,\qquad x^*=S^{-1}A(A^TS^{-1}A)^{-1}b\tag{7}$$
The minimum cost is F* = ½(x*)ᵀSx* = ½bᵀ(AᵀS⁻¹A)⁻¹AᵀS⁻¹SS⁻¹A(AᵀS⁻¹A)⁻¹b, which simplifies to
$$F^*=\tfrac12b^T(A^TS^{-1}A)^{-1}b,\qquad \frac{\partial F^*}{\partial b}=(A^TS^{-1}A)^{-1}b=\lambda^*\tag{8}$$
(p. 358). With inequality constraints Aᵀx ≤ b, the multipliers must satisfy λᵢ ≥ 0 and the problem is "distinctly harder". A component λᵢ* = 0 signals that constraint i is not active: the minimum would be the same without it (p. 359).

**KKT (saddle point) matrix.**
$$K\begin{bmatrix}x\\-\lambda\end{bmatrix}=\begin{bmatrix}S&A\\A^T&0\end{bmatrix}\begin{bmatrix}x\\-\lambda\end{bmatrix}=\begin{bmatrix}0\\b\end{bmatrix}\tag{9}$$
K is symmetric but neither positive nor negative definite. Multiply the first block row by AᵀS⁻¹ and subtract from the second:
$$\begin{bmatrix}S&A\\0&-A^TS^{-1}A\end{bmatrix}\begin{bmatrix}x\\-\lambda\end{bmatrix}=\begin{bmatrix}0\\b\end{bmatrix}\tag{10}$$
The block −AᵀS⁻¹A is the Schur complement. The first n pivots are positive because S is positive definite. There are m negative pivots because −AᵀS⁻¹A is negative definite. This signals a saddle point: L is convex in x and concave in λ (p. 359).

**Minimax = Maximin (p. 359–360).** First minimize L over x for fixed λ: x* = S⁻¹Aλ. Then (added step: L = ½xᵀSx − λᵀAᵀx + λᵀb at x = S⁻¹Aλ gives ½λᵀAᵀS⁻¹Aλ − λᵀAᵀS⁻¹Aλ + λᵀb)
$$\min_xL=-\tfrac12\lambda^TA^TS^{-1}A\lambda+\lambda^Tb.$$
Maximizing over λ gives λ* = (AᵀS⁻¹A)⁻¹b and L = ½bᵀ(AᵀS⁻¹A)⁻¹b, so max_λ min_x L = ½bᵀ(AᵀS⁻¹A)⁻¹b. In the other order, max over λ of L is +∞ if Aᵀx ≠ b and ½xᵀSx if Aᵀx = b. Minimizing that over x gives the same value, min_x max_λ L = ½bᵀ(AᵀS⁻¹A)⁻¹b. At the saddle point ∂L/∂x = ∂L/∂λ = 0 and maximin = minimax (p. 360).

**General quadratic programming (p. 360–361).** Here S may be only semidefinite and constraints may be inequalities:
$$\min q(x)=\tfrac12x^TSx+x^Tc\ \text{ s.t. } a_i^Tx=b_i\ (i=1..m),\ \ a_j^Tx\ge c_j\ (j=1..p).$$
The problem is convex if S = Sᵀ is positive semidefinite (assumed). Nonconvex problems could have several local minima. Multipliers also obey inequalities, and normally either the constraint on x or the one on λ is tight. With 10 constraint pairs there would be 2¹⁰ = 1024 configurations, which we cannot try (p. 360).

With equality constraints only, the Lagrangian is L = ½xᵀSx + xᵀc − λᵀ(Ax − b). It gives Sx* + c − Aᵀλ* = 0 and Ax* = b, so (here A is m×n, K is (n+m)×(n+m)):
$$K\begin{bmatrix}x^*\\-\lambda^*\end{bmatrix}=\begin{bmatrix}S&A^T\\A&0\end{bmatrix}\begin{bmatrix}x^*\\-\lambda^*\end{bmatrix}=\begin{bmatrix}-c\\b\end{bmatrix}\tag{11}$$
Many authors put −Aᵀ in place of Aᵀ (p. 360).

*When is K invertible?* Assume A has full rank m. If S is positive definite, K is invertible. If S is only semidefinite, the author states: if the columns of N are a basis for the nullspace of A, then NᵀSN (size n−m) must be positive definite for K to be invertible. The proof: suppose K[w; v] = 0. Then Aw = 0, so w = Ny, and 0 = [w;v]ᵀK[w;v] = wᵀSw = yᵀNᵀSNy. So if K is not invertible, NᵀSN is not positive definite (some w ≠ 0 lies in the nullspace of both S and A). The contrapositive is that positive definite NᵀSN makes K invertible (p. 361).

Numerically, elimination with row exchanges to avoid small pivots ruins the symmetry of K. Wright and Nocedal develop stable algorithms (p. 361).

**Inequality constraints: active set method (p. 361).** The crucial question is which of the p inequalities are active at x*. If we knew the active set we could treat them as equations. The rough method keeps a working set of equality constraints. If x_k does not minimize the quadratic for it, solve that subproblem while ignoring other constraints. Move as far as possible toward its solution until a "blocking constraint" is hit. Add that constraint and solve again. The final working set is the correct active set. The simplex method will use a similar idea: each step moves in a cost-reducing direction until it hits a new constraint (p. 361).

**Dual problems in science and engineering (p. 362).** Minimizing ½xᵀSx subject to Aᵀx = b is central when linear differential equations are discretized.
- Electrical networks: unknowns are node voltages and edge currents; Kirchhoff's laws give the balance equations; Ohm's law is the constraint; AᵀS⁻¹A is the conductance matrix.
- Finite elements: unknowns are displacements and stresses; force balance gives the equations; Hooke's law is the stress–strain relation; AᵀS⁻¹A is the stiffness matrix.

For stable problems these matrices are symmetric positive definite. Three descriptions are possible: (i) linear equations with AᵀS⁻¹A, (ii) minimization with currents or stresses as unknowns x, (iii) maximization with voltages or displacements as unknowns λ. The linear equations (i) are the popular choice. Fluid flow often stays in saddle-point form, with velocities and pressures as unknowns. In statistics, AᵀΣ⁻¹A includes the covariance Σ, and dividing by variances "whitens the noise" (Σ = I). In nonlinear problems geometric nonlinearities appear in A and material nonlinearities appear in S (p. 362).

### 9.4 Linear Programming, Game Theory, and Duality (p. 364–369)

**Linear programming (p. 364).** The cost cᵀx is linear and the constraints are linear:
$$\text{Minimize }c^Tx\text{ subject to }Ax=b\text{ and }x\ge0\tag{1}$$
Each constraint x_k ≥ 0 is active or inactive. If x_k* > 0 the constraint was inactive and its multiplier λ_k* = 0. If it forces x_k* = 0 the multiplier has λ_k* > 0. So the optimality condition is x_k*λ_k* = 0 for each k.

For A of size 1×3, Ax = b is a plane such as x₁+x₂+2x₃ = 4. Cutting by x ≥ 0 leaves a triangle K with corners (4,0,0), (0,4,0), (0,0,2). Because the cost is linear, its minimum over K is reached at a corner. Checking all corners is exponentially impractical for large m, n. Dantzig's simplex method starts at one corner satisfying Ax = b, x ≥ 0 and moves along an edge to a lower-cost corner, with the cost dropping at each step. It stops when the corner has minimum cost (p. 364).

**Dual problem and weak duality (p. 365).** With y ∈ ℝᵐ (the Lagrange multipliers):
$$\text{Maximize }y^Tb\text{ subject to }A^Ty\le c\tag{2}$$
Since Aᵀ is n×m, this has n constraints. The author's "beautiful fact" is
$$y^Tb=y^T(Ax)=(A^Ty)^Tx\le c^Tx\tag{3}$$
(the last step uses x ≥ 0; see Problem 1 on p. 369, where the author doubts the inequality alone is enough). The **duality theorem** (the minimax theorem) says max yᵀb in (2) equals min cᵀx in (1). The simplex method solves both at once. Interior-point methods go through the feasible set instead of along its edges, and "either method could win" (p. 365).

Key points of LP: Ax = b is chopped by xᵢ ≥ 0; the minimum cost occurs at a corner of the feasible set K; simplex travels corner to corner on the boundary; it stops where all outgoing edges raise the cost (p. 365).

*Example online.* A Ph.D., a friend and a computer charge $5, $3, $8 per hour and solve 1, 1, 2 problems per hour. For 4 problems: minimize 5x₁+3x₂+8x₃ subject to x ≥ 0 and x₁+x₂+2x₃ = 4. The corners are (4,0,0), (0,4,0), (0,0,2), and one is optimal (p. 365).

**Max flow–min cut (p. 366).** A is the incidence matrix of a graph. Aᵀy = 0 says flow in equals flow out at every node. The flow on edge j is bounded by capacity: |y_j| ≤ M_j. The flow is sent from source s to sink t and returned on an extra edge of unlimited capacity. Figure 9.10 gives these bounds:
- The cut at the source has capacity 7+2+8 = 17.
- A cut through the three middle edges has capacity 6+4+5 = 15.
- A cut through five later edges has capacity 3+2+4+3+2 = 14.

The author states that 14 is the min cut and, by duality, also the max flow (M = 14). If the capacities are integers, the optimal flows are integers. For a bipartite graph with capacities 0 or 1, max flow equals the maximum matching of people to jobs. The picture example allows a perfect matching M = 5. Removing the edge from 2 down to 1 leaves M = 4, because 2 and 5 are then qualified only for job 5. For bipartite graphs max flow = min cut is König's theorem and Hall's marriage theorem (p. 366).

**Two-person zero-sum games (p. 367–368).** R picks a row, C picks a column of the payoff matrix A, and R pays C the entry. R minimizes and C maximizes.

*Game 1:* A = [1 0 2; 3 −1 4]. Column 3 is C's favorite, and its smaller entry is 2 (row 1). The entry 2 is smallest in its column and largest in its row, so it is a saddle point. The optimal strategies are row 1 for R and column 3 for C, with payoff 2 (p. 367).

*Game 2 (changed column 3):* A = [1 0 4; 3 −1 2]. Now R needs a mixed strategy with probabilities x₁, x₂ (x₁+x₂ = 1). The mixed row is (x₁+3x₂, −x₂, 4x₁+2x₂). R equalizes the two largest payoffs:
$$x_1+3(1-x_1)=4x_1+2(1-x_1)\ \Rightarrow\ x_1^*=\tfrac14,\ x_2^*=\tfrac34,$$
and the mixed row is (2.5, −.75, 2.5). C mixes columns with y₁, y₂, y₃; the mixed column is (y₁+4y₃, 3y₁−y₂+2y₃). With y₂ = 0 and y₃ = 1−y₁: y₁+4(1−y₁) = 3y₁+2(1−y₁) gives y₁* = y₃* = ½. The value of the game is 2.5 both ways. R can guarantee to pay no more than 2.5 and C can guarantee to receive no less than 2.5 (p. 367–368).

Von Neumann's minimax theorem gives a solution for every payoff matrix and is equivalent to the LP duality theorem min cᵀx = max yᵀb. Games with three or more players are "much more difficult" (p. 367–368).

**Semidefinite programming (p. 368).** The cost is still cᵀx, but S(x) = S₀ + x₁S₁ + ⋯ + xₙSₙ must be positive semidefinite. The allowed set is convex, because the average of two semidefinite matrices is semidefinite (average the energies vᵀSv ≥ 0). Its sides can be curved: [x₁ 1; 1 x₂] is positive semidefinite when x₁ ≥ 0 and x₁x₂ ≥ 1. Minimizing the maximum eigenvalue of S(x) is included: minimize t so that tI − S(x) is positive semidefinite. Interior-point methods are best, essentially solving a least-squares problem per iteration (usually 5 to 50 iterations). There is a dual maximization whose value is never above cᵀx. We hope the two are equal, but "this might not happen" for matrix inequalities (p. 368).

## Toy example (ours)
Minimize F(x) = ½(x₁² + 2x₂²) subject to x₁ + x₂ = b. Here S = diag(1,2), Aᵀ = [1 1] (so A = (1,1)ᵀ), and the constraint is Aᵀx = b.

1. AᵀS⁻¹A = 1/1 + 1/2 = 3/2.
2. By (7), λ* = (3/2)⁻¹b = 2b/3.
3. x* = S⁻¹Aλ* = (λ*, λ*/2) = (2b/3, b/3). Check: 2b/3 + b/3 = b ✓.
4. Take b = 3: λ* = 2, x* = (2,1), F = ½(4+2) = 3. Formula (8): ½·3²·(2/3) = 3 ✓.
5. KKT check, Sx − Aλ = (2,2) − (2,2) = (0,0) ✓.
6. Multiplier as derivative: F*(b) = b²/3 (from (8): ½·b²·(2/3)). At b = 3.01, F* = 9.0601/3 = 3.020033. Then (3.020033 − 3)/0.01 ≈ 2.003 ≈ λ* = 2 ✓.

## Concepts
- [[gradient-descent]] (new) — step x_{k+1} = x_k − s_k∇F(x_k) in the steepest direction; s_k is the learning rate (p. 337).
- [[newton-method]] (new) — Δx = −S⁻¹∇F; converges fast near x*, needs the full Hessian (p. 336).
- [[hessian-matrix]] (new) — symmetric matrix S of second derivatives ∂²F/∂xᵢ∂xⱼ (p. 336).
- [[positive-definite-matrix]] — here S(x) positive definite everywhere makes F convex; the model bowl has S symmetric positive definite (p. 335–336).
- [[quadratic-form]] — F = ½xᵀSx − bᵀx; gradient Sx − b, minimizer S⁻¹b (p. 335, 339).
- [[convex-function]] (new) — graph stays above its tangents; positive definite Hessian gives (strict) convexity (p. 336).
- [[condition-number]] — λmax/λmin = 1/b of S; controls zig-zag and momentum rates (p. 344).
- [[momentum-descent]] (new) — z_k = ∇F(x_k) + βz_{k−1} makes descent a two-step method (p. 343).
- [[stochastic-gradient-descent]] (new) — each step uses one random sample (or batch B) instead of all N (p. 348).
- [[backpropagation]] (new) — reverse-mode chain rule: vector×matrix products from the loss back to layer j, with reuse (p. 349–350).
- [[jacobian-chain-rule]] (new) — ∂h/∂x = (∂f/∂g)(∂g/∂x), a matrix product (p. 347).
- [[matrix-multiplication-as-composition]] — the layered chain gives a product of L Jacobians (p. 347).
- [[tensor]] (new) — a derivative with three indices, e.g. T_ijk = v_kδ_ij; not a trivial extension of a matrix (p. 351).
- [[lagrange-multiplier]] (new) — λ attached to a constraint; for the quadratic examples it equals ∂F*/∂b (p. 357–358).
- [[kkt-matrix]] (new) — symmetric indefinite [S Aᵀ; A 0] ("saddle point matrix") for constrained quadratics (p. 359–360).
- [[schur-complement]] (new) — block −AᵀS⁻¹A that appears in the 2,2 position after block elimination (p. 359).
- [[norm]] — ℓ¹, ℓ², ℓ^∞, ℓᵖ (p ≥ 1); the "ℓ⁰ norm" counts nonzeros and is not a norm (p. 355–356).
- [[l1-sparsity]] (new) — ℓ¹ minimization on Av = b gives sparse solutions (p. 356).
- [[linear-programming]] (new) — minimize cᵀx s.t. Ax = b, x ≥ 0; optimum at a corner (p. 364).
- [[duality-lp]] (new) — dual max yᵀb s.t. Aᵀy ≤ c; weak duality yᵀb ≤ cᵀx; the optimal values are equal (p. 365).
- [[incidence-matrix]] — A for the flow network; Aᵀy = 0 is Kirchhoff's current law (p. 366).
- [[zero-sum-game-minimax]] (new) — payoff matrix, mixed strategies, minimax theorem equivalent to LP duality (p. 367–368).
- [[semidefinite-programming]] (new) — linear cost with S(x) = S₀ + Σxᵢ Sᵢ positive semidefinite (p. 368).

## Canonical instances
- [[newton-sqrt-example]] — x² − 4 = 0; error squared each step, 4 → 2.5 → 2.05 → 2.0006 (p. 337).
- [[zigzag-quadratic-bowl]] — F = ½(x²+by²) with exact line search; rate ((1−b)/(1+b))² per step (p. 342).
- [[kaczmarz-random-row]] — SGD for least squares via row projections; fast start, oscillating finish (p. 348).
- [[l1-l2-linf-minimizers]] — on 3x+4y = 1: (0,¼), (3/25,4/25), (1/7,1/7) (p. 356).
- [[min-distance-lagrange]] — min x₁²+x₂² on a₁x₁+a₂x₂ = b; λ = 2b/(a₁²+a₂²) (p. 357).
- [[max-flow-14]] — Figure 9.10: cuts 17, 15, 14; max flow = min cut = 14 (p. 366).
- [[game-mixed-strategy-2.5]] — payoff [1 0 4; 3 −1 2]; x* = (¼,¾), y* = (½,0,½), value 2.5 (p. 367–368).
- [[homework-help-lp]] — costs 5, 3, 8; x₁+x₂+2x₃ = 4 (p. 365).

## Bridges (candidates)
- [same-math] Chain-rule product of Jacobians ↔ linear-algebra: matrix multiplication as composition — each ∂F_k/∂F_{k−1} is a matrix and the whole is their product.
- [same-math] Zig-zag rate in 1/b ↔ linear-algebra: condition number λmax/λmin — b = λmin/λmax is exactly the author's setting.
- [same-math] Block elimination on K giving −AᵀS⁻¹A ↔ linear-algebra: Schur complement and pivots — elimination on a 2×2 block matrix.
- [structural-analogy] Lagrange multiplier = ∂(min cost)/∂b ↔ economics: shadow price of a resource — a price of relaxing a constraint (outside this unit).
- [same-math] Incidence matrix constraint Aᵀy = 0 in max flow ↔ graph theory: incidence matrix and conservation of flow at nodes.
- [structural-analogy] ℓ¹ minimization giving sparse solutions ↔ statistics: sparse regression — the same geometry of a diamond touching a flat set (outside this unit).

## Questions this raises
- Why does the extreme-eigenvalue pair (λmin, λmax) determine the best s and β for any symmetric positive definite S, not only for the 2×2 case?
- In reverse mode, how much memory is needed to store all forward-pass values F_j, and what does the cost trade-off look like?
- How does the simplex method pick the "steepest edge" as a linear algebra step, and why does the duality theorem hold with equality for LP but possibly not for SDP?
- When is a sparse ℓ¹ solution of Av = b guaranteed to be the sparsest, given that ℓ¹ only "convexifies" ℓ⁰?

## Exercises worth doing
- Ex. 9.1.1 (p. 345) — which functions make the Taylor formulas (1), (2) exact; checks what "quadratic" means — easy
- Ex. 9.1.5 (p. 345) — write the gradient-descent step for least squares ½‖Ax − b‖²; links Ch. 9 to normal equations — medium
- Ex. 9.1.6–7 (p. 345) — compute zig-zag steps with a given b and add one momentum step; makes (9)–(11) concrete — medium
- Ex. 9.1.4 (p. 345) — show −log(ac − b²) is convex from the Hessian; hard application of the det/log example — hard
- Ex. 9.2.1 (p. 353) — test Kaczmarz (6) in cyclic vs random order on a 2×2 system — easy
- Ex. 9.2.4 (p. 354) — gradient with respect to b of the vector tanh(Ax + b); practices the layer-derivative formulas — medium
- Ex. 9.3.3 (p. 363) — full Lagrange problem with checks of F*/∂b = λ*; practises (1)–(8) — medium
- Ex. 9.3.6 (p. 363) — Law of Inertia for 2×2 symmetric matrices; links pivot signs to eigenvalue signs (for K) — hard
- Ex. 9.4.1 (p. 369) — is x ≥ 0 needed in weak duality? — easy
- Ex. 9.4.5 (p. 369) — optimal mixed strategies for two payoff matrices — medium
- Ex. 9.4.10 (p. 369) — midpoint argument showing the LP feasible set is convex — easy

## Reading notes
- Printed page = pdf page − 10 (pdf 345 = printed 335). The unit covers printed 335–369. Equation numbers restart in each section; I tag them with the section in L3 headings.
- The extracted text is garbled in many equations; I checked each against the page images. Eq. (4) of 9.2 prints "column j of ∂g/∂x" where the surrounding formula uses column k. This looks like a misprint.
- In (8) of 9.2, the minus sign of ∂ℓ/∂F is lost in the extracted text; I wrote −2(w − F), which is the derivative of the squared length (w − F)ᵀ(w − F).
- Page 357 says the tangent line and circle are shown in "Figure 9.7", while the norm-minimization pictures are in Figure 9.8 and the tangent picture is Figure 9.9 (p. 358). Problem 3(c) on p. 363 has the same reference.
- On p. 353 the sigmoid is written "ReLU_a" and then "R_a"; this seems a typographical inconsistency.
- The author's statement about NᵀSN (p. 361) is phrased as "must be positive definite for K to be invertible", but the proof given shows the contrapositive: positive definite NᵀSN ⇒ K invertible. I report both.
- The letter A is used for different shapes: n×m in the first quadratic-programming section (Aᵀx = b) and m×n in the general QP section (Ax = b).
- The statement on p. 341 that (0,0) "does not lie on that line for any s" is stated for a general start (x₀,y₀); no further condition is printed.
- Problem 6 of Set 9.1 (p. 345) appears to use a specific b (printed ¼); I did not rely on it.
