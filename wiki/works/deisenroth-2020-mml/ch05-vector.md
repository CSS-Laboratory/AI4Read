---
id: deisenroth-2020-mml/ch05-vector
work: deisenroth-2020-mml
unit: 5 Vector Calculus
pages: 139-171
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Vector Calculus

## L0 — One line
Gradients, Jacobians and Hessians collect partial derivatives into arrays whose shapes make the multivariate chain rule a plain matrix product. This lets backpropagation compute gradients efficiently and lets Taylor expansions approximate functions locally.

## L1 — The gist (≤ 120 words)
Many ML algorithms tune parameters by optimizing an objective with gradient information. The chapter asks how to differentiate functions of vectors and matrices, and how to do it efficiently. Answer: partial derivatives are collected into a row-vector gradient or an m×n Jacobian, so the chain rule becomes matrix multiplication. Derivatives of matrices are tensors (multidimensional arrays), which can be flattened into vectors. Backpropagation is reverse-mode automatic differentiation on a computation graph. The Hessian holds second derivatives. Taylor series give local polynomial approximations. These tools underlie training, optimization, density estimation and probability transformations.

**Prerequisites:** limits and the high-school derivative; matrix multiplication and shapes; determinant as area scaling; dot product; trace; change of basis.

## L2 — Key ideas
- The derivative is the limit of the difference quotient (the slope of a secant line) as the step shrinks to 0; the secant becomes a tangent. The Taylor polynomial of degree n at x₀ is exact for polynomials of degree ≤ n. (pp. 141–143)
- The gradient of f: ℝⁿ→ℝ is a **row** vector (1×n) of partial derivatives. This convention lets it generalize to matrices and lets the chain rule be written as matrix multiplication. (pp. 146–149)
- For f: ℝⁿ→ℝᵐ the gradient is the m×n Jacobian, with J(i,j)=∂fᵢ/∂xⱼ. |det J| is the local area/volume scaling factor in a change of variables, exact when the map is linear. (pp. 150–152)
- Gradients of matrices with respect to vectors or matrices are tensors (multidimensional arrays). One can flatten matrices into vectors, work with a Jacobian matrix, and reshape back. (pp. 155–158)
- Backpropagation is reverse-mode automatic differentiation: the function is a computation graph of elementary operations, and gradients are propagated backward. In the worked example (Example 5.14), the derivative costs about as much as evaluating the function (p. 163). (pp. 159–164)
- The Hessian collects second-order partial derivatives and is symmetric when f is twice continuously differentiable. It measures local curvature. (pp. 164–165)
- The multivariate Taylor series uses k-fold outer products δᵏ of the difference vector δ=x−x₀ (δ⊗δ=δδᵀ is a matrix; δᵏ is a k-dimensional array). The first terms are f(x₀), the gradient term, and ½δᵀHδ. (pp. 165–169)
- Taylor expansions help approximate expectations (integrals) that cannot be solved analytically: the extended Kalman filter (a filter for state estimation in nonlinear dynamical systems) exploits first-order linearization, and the Laplace approximation (a local Gaussian approximation of a distribution around its mode) uses a second-order expansion. (p. 170)

## L3 — Walkthrough

### 5 Introduction (pp. 139–141)
Many ML algorithms optimize an objective with respect to parameters (p. 139). The examples are linear regression, neural-network auto-encoders, and Gaussian mixture models. These are typically solved with gradient-based optimization (p. 139).
A function f: ℝᴰ→ℝ assigns every input x exactly one value f(x). ℝᴰ is the *domain*; the values form the *image/codomain* (pp. 139–140).
Example 5.1 writes f(x)=xᵀx on ℝ² as x ↦ x₁²+x₂² (p. 140).
The author states that the gradient points in the direction of steepest ascent. Throughout the book, functions are assumed differentiable (pp. 140–141).

### 5.1 Univariate differentiation (pp. 141–145)
**Definition 5.1 (difference quotient)** (p. 141):
$$\frac{\delta y}{\delta x}:=\frac{f(x+\delta x)-f(x)}{\delta x}\tag{5.3}$$
This is the slope of the secant through two points of the graph.

**Definition 5.2 (derivative)** (p. 141):
$$\frac{df}{dx}:=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\tag{5.4}$$

**Example 5.2 (derivative of xⁿ, n∈ℕ)** (p. 142). Expand $(x+h)^n=\sum_{i=0}^n\binom{n}{i}x^{n-i}h^i$. The $i=0$ term equals $x^n$ and cancels, so
$$\frac{df}{dx}=\lim_{h\to0}\sum_{i=1}^{n}\binom{n}{i}x^{n-i}h^{i-1}=\lim_{h\to0}\Big[\binom{n}{1}x^{n-1}+\underbrace{\sum_{i=2}^{n}\binom{n}{i}x^{n-i}h^{i-1}}_{\to0\text{ as }h\to0}\Big]=\frac{n!}{1!(n-1)!}x^{n-1}=nx^{n-1}.$$
(5.5)–(5.6)

#### 5.1.1 Taylor series (pp. 142–145)
**Definition 5.3 (Taylor polynomial of degree n at x₀)**, with $t^0:=1$ (p. 142):
$$T_n(x):=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k\tag{5.7}$$
**Definition 5.4 (Taylor series)** for smooth $f\in\mathcal C^\infty$ (p. 142–143):
$$T_\infty(x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k\tag{5.8}$$
For $x_0=0$ this is the Maclaurin series. If $f=T_\infty$, then $f$ is called *analytic* (p. 143).
*Remark:* a Taylor polynomial of degree n approximates f near x₀. It is an exact representation of a polynomial of degree k ≤ n, because all derivatives of order above k vanish (p. 143).

**Example 5.3** ($f=x^4$, $T_6$ at $x_0=1$) (p. 143). The derivatives at 1 are $f=1$, $f'=4$, $f''=12$, $f^{(3)}=24$, $f^{(4)}=24$, $f^{(5)}=f^{(6)}=0$. Hence
$$T_6(x)=1+4(x-1)+6(x-1)^2+4(x-1)^3+(x-1)^4+0.$$
Multiplying out gives $(1-4+6-4+1)+x(4-12+12-4)+x^2(6-12+6)+x^3(4-4)+x^4=x^4$ (5.17)–(5.18).

**Example 5.4** ($f=\sin x+\cos x$ at $x_0=0$) (pp. 144–145). The derivatives at 0 are $1,1,-1,-1,1,\dots$, and $f^{(k+4)}(0)=f^{(k)}(0)$. Splitting even and odd terms:
$$T_\infty(x)=\sum_{k=0}^\infty(-1)^k\frac{x^{2k}}{(2k)!}+\sum_{k=0}^\infty(-1)^k\frac{x^{2k+1}}{(2k+1)!}=\cos x+\sin x\tag{5.25}$$
using the power series (5.26) and (5.27). Figure 5.4 shows $T_0,T_1,T_5,T_{10}$. Higher degree approximates better and more globally; $T_{10}$ is already similar to f on [−4,4] (p. 144).
*Remark:* a Taylor series is a power series $\sum a_k(x-c)^k$ of a special form (5.28) (p. 145).

*Intuition note:* A Taylor polynomial matches a function's value and first n derivatives at one point, so it is accurate near that point. If the function is itself a polynomial of low enough degree, the match is exact everywhere.

#### 5.1.2 Differentiation rules (pp. 145–146)
- Product: $(fg)'=f'g+fg'$ (5.29)
- Quotient: $(f/g)'=\dfrac{f'g-fg'}{g^2}$ (5.30)
- Sum: $(f+g)'=f'+g'$ (5.31)
- Chain: $(g(f(x)))'=(g\circ f)'(x)=g'(f(x))f'(x)$ (5.32)

**Example 5.5:** $h(x)=(2x+1)^4=g(f(x))$ with $f=2x+1$ and $g(f)=f^4$. Then $f'=2$, $g'=4f^3$, and $h'(x)=4(2x+1)^3\cdot2=8(2x+1)^3$ (pp. 145–146).

### 5.2 Partial differentiation and gradients (pp. 146–149)
The gradient is found by varying one variable at a time and keeping the others constant (p. 146).

**Definition 5.5 (partial derivative)** for $f:\mathbb R^n\to\mathbb R$:
$$\frac{\partial f}{\partial x_1}=\lim_{h\to0}\frac{f(x_1+h,x_2,\dots,x_n)-f(\mathbf x)}{h},\ \dots,\ \frac{\partial f}{\partial x_n}=\lim_{h\to0}\frac{f(x_1,\dots,x_{n-1},x_n+h)-f(\mathbf x)}{h}\tag{5.39}$$
The partials are collected in a **row vector**, called the gradient or Jacobian:
$$\nabla_{\mathbf x}f=\operatorname{grad}f=\frac{df}{d\mathbf x}=\Big[\tfrac{\partial f(\mathbf x)}{\partial x_1}\ \ \tfrac{\partial f(\mathbf x)}{\partial x_2}\ \cdots\ \tfrac{\partial f(\mathbf x)}{\partial x_n}\Big]\in\mathbb R^{1\times n}\tag{5.40}$$
(p. 146).

**Example 5.6:** for $f(x,y)=(x+2y^3)^2$, $\partial f/\partial x=2(x+2y^3)$ (5.41) and $\partial f/\partial y=2(x+2y^3)\cdot6y^2=12(x+2y^3)y^2$ (5.42) (pp. 146–147).

*Remark (row vector):* the row convention is chosen for two reasons (p. 147):
1. It generalizes consistently to $f:\mathbb R^n\to\mathbb R^m$, where the gradient becomes a matrix.
2. The multivariate chain rule can be applied without attending to gradient dimensions.

**Example 5.7:** $f=x_1^2x_2+x_1x_2^3$ has $\partial_{x_1}f=2x_1x_2+x_2^3$ and $\partial_{x_2}f=x_1^2+3x_1x_2^2$. So $\frac{df}{d\mathbf x}=[2x_1x_2+x_2^3\ \ x_1^2+3x_1x_2^2]\in\mathbb R^{1\times2}$ (5.43)–(5.45) (p. 147).

#### 5.2.1 Basic rules (pp. 147–148)
The sum, product and chain rules still apply, but order matters because matrix multiplication is not commutative (p. 147):
$$\frac{\partial}{\partial\mathbf x}(f g)=\frac{\partial f}{\partial\mathbf x}g+f\frac{\partial g}{\partial\mathbf x}\ (5.46),\quad \frac{\partial}{\partial\mathbf x}(f+g)=\frac{\partial f}{\partial\mathbf x}+\frac{\partial g}{\partial\mathbf x}\ (5.47),\quad \frac{\partial}{\partial\mathbf x}(g\circ f)=\frac{\partial g}{\partial f}\frac{\partial f}{\partial\mathbf x}\ (5.48)$$
The author gives an intuition for (5.48): the ∂f in the "denominator" of the first factor matches the one in the "numerator" of the second and "cancels". The author notes this is only an intuition, since a partial derivative is not a fraction (p. 148).

#### 5.2.2 Chain rule (pp. 148–149)
For $f(x_1(t),x_2(t))$ (p. 148):
$$\frac{df}{dt}=\Big[\tfrac{\partial f}{\partial x_1}\ \tfrac{\partial f}{\partial x_2}\Big]\begin{bmatrix}\partial x_1/\partial t\\ \partial x_2/\partial t\end{bmatrix}=\frac{\partial f}{\partial x_1}\frac{\partial x_1}{\partial t}+\frac{\partial f}{\partial x_2}\frac{\partial x_2}{\partial t}\tag{5.49}$$
**Example 5.8:** $f=x_1^2+2x_2$, $x_1=\sin t$, $x_2=\cos t$. Then $df/dt=2\sin t\cos t-2\sin t=2\sin t(\cos t-1)$ (5.50).
If $x_1(s,t),x_2(s,t)$ depend on two variables, then (5.51)–(5.52) hold and the result is the matrix product (p. 149)
$$\frac{df}{d(s,t)}=\frac{\partial f}{\partial\mathbf x}\frac{\partial\mathbf x}{\partial(s,t)}=\Big[\tfrac{\partial f}{\partial x_1}\ \tfrac{\partial f}{\partial x_2}\Big]\begin{bmatrix}\partial x_1/\partial s&\partial x_1/\partial t\\ \partial x_2/\partial s&\partial x_2/\partial t\end{bmatrix}\tag{5.53}$$
This compact form only works if the gradient is a row vector. Otherwise gradients must be transposed, which is no longer trivial when gradients become tensors (p. 149).

*Remark (gradient checking, p. 149):* use (5.39) with small $h$ (e.g. $10^{-4}$) to test an analytic gradient. "Small" error could mean $\sqrt{\sum_i(dh_i-df_i)^2/\sum_i(dh_i+df_i)^2}<10^{-6}$, where $dh_i$ is the finite-difference value and $df_i$ the analytic gradient. If the error is small, the implementation is *probably* correct.

*Intuition note:* Row-vector gradients have shape 1×n and Jacobians have shape m×n. The chain rule then multiplies neighbouring matrices whose inner dimensions match, similar to the dimension-matching rule of matrix multiplication (the author calls this resemblance only an intuition, p. 148).

### 5.3 Gradients of vector-valued functions (pp. 149–154)
For $\mathbf f:\mathbb R^n\to\mathbb R^m$ ($n\ge1$, $m>1$), $\mathbf f(\mathbf x)=[f_1(\mathbf x),\dots,f_m(\mathbf x)]^\top$ (5.54). Each $f_i$ follows the rules of Section 5.2 (p. 149).
The partial derivative with respect to $x_i$ is a column vector in $\mathbb R^m$, with entries $\lim_{h\to0}\frac{f_j(\dots,x_i+h,\dots)-f_j(\mathbf x)}{h}$ (5.55). Collecting these columns gives (5.56) (p. 150).

**Definition 5.6 (Jacobian)** (p. 150):
$$\mathbf J=\nabla_{\mathbf x}\mathbf f=\frac{d\mathbf f}{d\mathbf x}=\Big[\tfrac{\partial\mathbf f}{\partial x_1}\cdots\tfrac{\partial\mathbf f}{\partial x_n}\Big]\in\mathbb R^{m\times n},\qquad J(i,j)=\frac{\partial f_i}{\partial x_j}\tag{5.57–5.59}$$
For $f:\mathbb R^n\to\mathbb R^1$ the Jacobian is a $1\times n$ row vector.
*Remark:* the book uses the **numerator layout**, where the elements of $\mathbf f$ define the rows and the elements of $\mathbf x$ the columns. The denominator layout is its transpose (pp. 150–151).

**Jacobian determinant as scaling factor** (pp. 151–152). The author illustrates with two parallelograms:
- Unit square with sides $\mathbf b_1=[1,0]^\top$, $\mathbf b_2=[0,1]^\top$: $|\det\begin{bmatrix}1&0\\0&1\end{bmatrix}|=1$ (5.60).
- Parallelogram with sides $\mathbf c_1=[-2,1]^\top$, $\mathbf c_2=[1,1]^\top$: $|\det\begin{bmatrix}-2&1\\1&1\end{bmatrix}|=|-3|=3$ (5.61). Its area is three times the unit square's.

*Approach 1 (linear algebra, p. 151–152):* both pairs are bases of ℝ². The basis-change matrix $\mathbf J=\begin{bmatrix}-2&1\\1&1\end{bmatrix}$ (5.62) satisfies $\mathbf J\mathbf b_1=\mathbf c_1$ and $\mathbf J\mathbf b_2=\mathbf c_2$. Its $|\det\mathbf J|=3$ is the area scaling.

*Approach 2 (partial derivatives, p. 152):* this works for nonlinear maps too. Write $y_1=-2x_1+x_2$ and $y_2=x_1+x_2$ (5.63–5.64). The partials are $\partial y_1/\partial x_1=-2$, $\partial y_1/\partial x_2=1$, $\partial y_2/\partial x_1=1$, $\partial y_2/\partial x_2=1$ (5.65). So $\mathbf J=\begin{bmatrix}-2&1\\1&1\end{bmatrix}$ (5.66), the same as (5.62). The Jacobian is exact when the transformation is linear. If it is nonlinear, the Jacobian approximates it locally by a linear map. $|\det\mathbf J|$ is the factor by which areas or volumes are scaled (here 3). This is used for transforming probability distributions in Section 6.7 and in the reparametrization trick (p. 152).

Figure 5.6 summarizes derivative shapes (p. 152):

| $f$ | gradient shape |
|---|---|
| ℝ→ℝ | scalar |
| ℝᴰ→ℝ | 1×D row |
| ℝ→ℝᴱ | E×1 column |
| ℝᴰ→ℝᴱ | E×D matrix |

**Example 5.9:** $\mathbf f(\mathbf x)=\mathbf A\mathbf x$ with $\mathbf A\in\mathbb R^{M\times N}$. Since $f_i=\sum_jA_{ij}x_j$, $\partial f_i/\partial x_j=A_{ij}$ (5.67). So $d\mathbf f/d\mathbf x=\mathbf A\in\mathbb R^{M\times N}$ (5.68) (p. 153).

**Example 5.10:** $h=f\circ g$ with $f(\mathbf x)=\exp(x_1x_2^2)$ and $g(t)=[t\cos t,\ t\sin t]^\top$. Shapes: $\partial f/\partial\mathbf x\in\mathbb R^{1\times2}$, $\partial g/\partial t\in\mathbb R^{2\times1}$ (5.73). Then
$$\frac{dh}{dt}=\big[\exp(x_1x_2^2)x_2^2\ \ 2\exp(x_1x_2^2)x_1x_2\big]\begin{bmatrix}\cos t-t\sin t\\ \sin t+t\cos t\end{bmatrix}=\exp(x_1x_2^2)\big(x_2^2(\cos t-t\sin t)+2x_1x_2(\sin t+t\cos t)\big)$$
with $x_1=t\cos t$ and $x_2=t\sin t$ (5.74) (p. 153).

**Example 5.11 (least-squares loss)** (p. 154). Model $\mathbf y=\boldsymbol\Phi\boldsymbol\theta$ with $\boldsymbol\theta\in\mathbb R^D$, $\boldsymbol\Phi\in\mathbb R^{N\times D}$, $\mathbf y\in\mathbb R^N$. Define $L(\mathbf e):=\|\mathbf e\|^2$ (5.76) and $\mathbf e(\boldsymbol\theta):=\mathbf y-\boldsymbol\Phi\boldsymbol\theta$ (5.77). Then $\partial L/\partial\boldsymbol\theta\in\mathbb R^{1\times D}$ (5.78), and by the chain rule
$$\frac{\partial L}{\partial\boldsymbol\theta}=\frac{\partial L}{\partial\mathbf e}\frac{\partial\mathbf e}{\partial\boldsymbol\theta}\tag{5.79}$$
with $\partial L/\partial\mathbf e=2\mathbf e^\top\in\mathbb R^{1\times N}$ (since $\|\mathbf e\|^2=\mathbf e^\top\mathbf e$) (5.81) and $\partial\mathbf e/\partial\boldsymbol\theta=-\boldsymbol\Phi\in\mathbb R^{N\times D}$ (5.82). Therefore
$$\frac{\partial L}{\partial\boldsymbol\theta}=-2\mathbf e^\top\boldsymbol\Phi=-2(\mathbf y^\top-\boldsymbol\theta^\top\boldsymbol\Phi^\top)\boldsymbol\Phi\in\mathbb R^{1\times D}\tag{5.83}$$
Component form: $\frac{\partial L}{\partial\boldsymbol\theta}[1,d]=\sum_n\frac{\partial L}{\partial\mathbf e}[n]\frac{\partial\mathbf e}{\partial\boldsymbol\theta}[n,d]$ (5.80). The same result follows directly from $L_2(\boldsymbol\theta)=(\mathbf y-\boldsymbol\Phi\boldsymbol\theta)^\top(\mathbf y-\boldsymbol\Phi\boldsymbol\theta)$ (5.84). That route is still practical for simple functions like $L_2$ but becomes impractical for deep compositions (p. 154).

### 5.4 Gradients of matrices (pp. 155–158)
The gradient of an m×n matrix **A** with respect to a p×q matrix **B** is a four-dimensional tensor with entries $J_{ijkl}=\partial A_{ij}/\partial B_{kl}$, of shape $(m\times n)\times(p\times q)$ (p. 156).
Matrices and vectors are related by a vector-space isomorphism between $\mathbb R^{m\times n}$ and $\mathbb R^{mn}$. So one can flatten (stack columns), get an $mn\times pq$ Jacobian matrix, and reshape back (Figure 5.7, pp. 155–156). In practice it is often easier to flatten and continue with the Jacobian matrix, because the chain rule then reduces to matrix multiplication. With a tensor, one must track which dimensions to sum out (p. 156).

**Example 5.12 ($\mathbf f=\mathbf A\mathbf x$, gradient with respect to $\mathbf A$)** (pp. 156–157). Here $d\mathbf f/d\mathbf A\in\mathbb R^{M\times(M\times N)}$ (5.86). From $f_i=\sum_jA_{ij}x_j$ (5.88), $\partial f_i/\partial A_{iq}=x_q$ (5.89). Hence $\partial f_i/\partial A_{i,:}=\mathbf x^\top\in\mathbb R^{1\times1\times N}$ (5.90), and $\partial f_i/\partial A_{k\ne i,:}=\mathbf 0^\top$ (5.91). Stacking gives $\partial f_i/\partial\mathbf A\in\mathbb R^{1\times(M\times N)}$: rows of $\mathbf 0^\top$ except row $i$, which is $\mathbf x^\top$ (5.92).

**Example 5.13 ($\mathbf K=\mathbf R^\top\mathbf R$)** with $\mathbf R\in\mathbb R^{M\times N}$ (pp. 157–158). The gradient has shape $(N\times N)\times(M\times N)$ (5.94), and $dK_{pq}/d\mathbf R\in\mathbb R^{1\times M\times N}$ (5.95). Each entry is a dot product of columns: $K_{pq}=\mathbf r_p^\top\mathbf r_q=\sum_mR_{mp}R_{mq}$ (5.96). Then
$$\frac{\partial K_{pq}}{\partial R_{ij}}=\sum_{m=1}^M\frac{\partial}{\partial R_{ij}}R_{mp}R_{mq}=:\partial_{pqij}\tag{5.97}$$
$$\partial_{pqij}=\begin{cases}R_{iq}&j=p,\ p\ne q\\ R_{ip}&j=q,\ p\ne q\\ 2R_{iq}&j=p,\ p=q\\ 0&\text{otherwise}\end{cases}\tag{5.98}$$
with $p,q,j=1,\dots,N$ and $i=1,\dots,M$.

*Intuition note:* A "gradient of a matrix" is just a bookkeeping array of all partials $\partial(\text{entry})/\partial(\text{entry})$. Flattening turns that array into an ordinary Jacobian matrix.

### 5.5 Useful identities (pp. 158–159)
With $\operatorname{tr}$ the trace, det the determinant, and $f(\mathbf X)^{-1}$ assumed to exist (p. 158):
$$\tfrac{\partial}{\partial\mathbf X}f(\mathbf X)^\top=\big(\tfrac{\partial f(\mathbf X)}{\partial\mathbf X}\big)^\top\ (5.99),\qquad \tfrac{\partial}{\partial\mathbf X}\operatorname{tr}(f(\mathbf X))=\operatorname{tr}\big(\tfrac{\partial f(\mathbf X)}{\partial\mathbf X}\big)\ (5.100)$$
$$\tfrac{\partial}{\partial\mathbf X}\det f(\mathbf X)=\det f(\mathbf X)\operatorname{tr}\big(f(\mathbf X)^{-1}\tfrac{\partial f(\mathbf X)}{\partial\mathbf X}\big)\ (5.101),\qquad \tfrac{\partial}{\partial\mathbf X}f(\mathbf X)^{-1}=-f(\mathbf X)^{-1}\tfrac{\partial f(\mathbf X)}{\partial\mathbf X}f(\mathbf X)^{-1}\ (5.102)$$
$$\tfrac{\partial\mathbf a^\top\mathbf X^{-1}\mathbf b}{\partial\mathbf X}=-(\mathbf X^{-1})^\top\mathbf a\mathbf b^\top(\mathbf X^{-1})^\top\ (5.103),\quad \tfrac{\partial\mathbf x^\top\mathbf a}{\partial\mathbf x}=\mathbf a^\top\ (5.104),\quad \tfrac{\partial\mathbf a^\top\mathbf x}{\partial\mathbf x}=\mathbf a^\top\ (5.105)$$
$$\tfrac{\partial\mathbf a^\top\mathbf X\mathbf b}{\partial\mathbf X}=\mathbf a\mathbf b^\top\ (5.106),\quad \tfrac{\partial\mathbf x^\top\mathbf B\mathbf x}{\partial\mathbf x}=\mathbf x^\top(\mathbf B+\mathbf B^\top)\ (5.107)$$
$$\tfrac{\partial}{\partial\mathbf s}(\mathbf x-\mathbf A\mathbf s)^\top\mathbf W(\mathbf x-\mathbf A\mathbf s)=-2(\mathbf x-\mathbf A\mathbf s)^\top\mathbf W\mathbf A\quad\text{for symmetric }\mathbf W\ (5.108)$$
*Remark:* the book covers only traces and transposes of matrices. For tensors, the trace of a D×D×E×F tensor would be an E×F matrix (a tensor contraction), and "transpose" means swapping the first two dimensions. This is needed in (5.99)–(5.102) when one does not vectorize (pp. 158–159).

### 5.6 Backpropagation and automatic differentiation (pp. 159–164)
Gradient descent needs the gradient of the learning objective with respect to the model parameters. It is obtained with calculus and the chain rule (p. 159).
For $f(x)=\sqrt{x^2+\exp(x^2)}+\cos(x^2+\exp(x^2))$ (5.109), the explicit gradient is
$$\frac{df}{dx}=2x\Big(\frac{1}{2\sqrt{x^2+\exp(x^2)}}-\sin(x^2+\exp(x^2))\Big)(1+\exp(x^2))\tag{5.110}$$
Writing gradients out explicitly is often impractical. Implemented carelessly, the gradient could be significantly more expensive than the function (p. 159).

#### 5.6.1 Gradients in a deep network (pp. 159–161)
A deep network is a composition $\mathbf y=(f_K\circ\cdots\circ f_1)(\mathbf x)$ (5.111), where each $f_i$ has its own parameters. With layers $\mathbf f_0:=\mathbf x$ and $\mathbf f_i:=\sigma_i(\mathbf A_{i-1}\mathbf f_{i-1}+\mathbf b_{i-1})$, $i=1,\dots,K$ (5.112–5.113), the squared loss is
$$L(\boldsymbol\theta)=\|\mathbf y-\mathbf f_K(\boldsymbol\theta,\mathbf x)\|^2,\quad\boldsymbol\theta=\{\mathbf A_0,\mathbf b_0,\dots,\mathbf A_{K-1},\mathbf b_{K-1}\}\tag{5.114}$$
The chain rule gives, for $\boldsymbol\theta_j=\{\mathbf A_j,\mathbf b_j\}$ (p. 160):
$$\frac{\partial L}{\partial\boldsymbol\theta_{K-1}}=\frac{\partial L}{\partial\mathbf f_K}\frac{\partial\mathbf f_K}{\partial\boldsymbol\theta_{K-1}},\quad \frac{\partial L}{\partial\boldsymbol\theta_{K-2}}=\frac{\partial L}{\partial\mathbf f_K}\frac{\partial\mathbf f_K}{\partial\mathbf f_{K-1}}\frac{\partial\mathbf f_{K-1}}{\partial\boldsymbol\theta_{K-2}}\ (5.115\text{–}5.116)$$
$$\frac{\partial L}{\partial\boldsymbol\theta_{i}}=\frac{\partial L}{\partial\mathbf f_K}\frac{\partial\mathbf f_K}{\partial\mathbf f_{K-1}}\cdots\frac{\partial\mathbf f_{i+2}}{\partial\mathbf f_{i+1}}\frac{\partial\mathbf f_{i+1}}{\partial\boldsymbol\theta_i}\ (5.118)$$
Layer-output-with-respect-to-input factors are "orange"; layer-output-with-respect-to-parameter factors are "blue". If $\partial L/\partial\boldsymbol\theta_{i+1}$ is already computed, most of the computation is reused for $\partial L/\partial\boldsymbol\theta_i$. The additional terms to compute are indicated by boxes (Figure 5.9: gradients are passed backward through the network) (pp. 160–161).

#### 5.6.2 Automatic differentiation (pp. 161–164)
Backpropagation is a special case of *automatic differentiation*. This is a set of techniques that numerically (not symbolically) evaluate the exact (up to machine precision) gradient, using intermediate variables and the chain rule. It differs from symbolic differentiation and from finite-difference approximation (p. 161).
For a graph $x\to a\to b\to y$ (Figure 5.10), $\frac{dy}{dx}=\frac{dy}{db}\frac{db}{da}\frac{da}{dx}$ (5.119). Forward and reverse modes differ in the order of multiplication, by associativity of matrix multiplication (p. 161):
$$\frac{dy}{dx}=\Big(\frac{dy}{db}\frac{db}{da}\Big)\frac{da}{dx}\ \text{(reverse mode, 5.120)},\qquad \frac{dy}{dx}=\frac{dy}{db}\Big(\frac{db}{da}\frac{da}{dx}\Big)\ \text{(forward mode, 5.121)}$$
In neural networks the input dimension is often much higher than the label dimension, and the reverse mode is then computationally significantly cheaper than the forward mode (p. 162).

**Example 5.14** (p. 162–163). Intermediate variables for (5.122), the same function as (5.109):
$a=x^2$, $b=\exp(a)$, $c=a+b$, $d=\sqrt c$, $e=\cos c$, $f=d+e$ (5.123–5.128), with the computation graph of Figure 5.11. This needs fewer operations than the direct form. Elementary derivatives: $\partial a/\partial x=2x$; $\partial b/\partial a=\exp a$; $\partial c/\partial a=1=\partial c/\partial b$; $\partial d/\partial c=\frac1{2\sqrt c}$; $\partial e/\partial c=-\sin c$; $\partial f/\partial d=1=\partial f/\partial e$ (5.129–5.134). Working backward from the output:
$$\tfrac{\partial f}{\partial c}=\tfrac{\partial f}{\partial d}\tfrac{\partial d}{\partial c}+\tfrac{\partial f}{\partial e}\tfrac{\partial e}{\partial c},\ \ \tfrac{\partial f}{\partial b}=\tfrac{\partial f}{\partial c}\tfrac{\partial c}{\partial b},\ \ \tfrac{\partial f}{\partial a}=\tfrac{\partial f}{\partial b}\tfrac{\partial b}{\partial a}+\tfrac{\partial f}{\partial c}\tfrac{\partial c}{\partial a},\ \ \tfrac{\partial f}{\partial x}=\tfrac{\partial f}{\partial a}\tfrac{\partial a}{\partial x}$$
(5.135–5.138). Substituting: $\partial f/\partial c=1\cdot\frac1{2\sqrt c}+1\cdot(-\sin c)$; $\partial f/\partial b=\partial f/\partial c\cdot1$; $\partial f/\partial a=\partial f/\partial b\,\exp(a)+\partial f/\partial c\cdot1$; $\partial f/\partial x=\partial f/\partial a\cdot2x$ (5.139–5.142). The derivative costs about as much as the function, even though the closed-form (5.110) looks far more complicated (p. 163).

**General formulation** (pp. 163–164). Inputs are $x_1,\dots,x_d$, intermediates $x_{d+1},\dots,x_{D-1}$, and output $x_D$:
$$x_i=g_i(x_{\mathrm{Pa}(x_i)}),\quad i=d+1,\dots,D\tag{5.143}$$
where $g_i$ are elementary functions and Pa denotes parent nodes. Since $f=x_D$, $\partial f/\partial x_D=1$ (5.144). For the others,
$$\frac{\partial f}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial x_j}{\partial x_i}=\sum_{x_j:\,x_i\in\mathrm{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}\tag{5.145}$$
(5.143) is forward propagation of the function; (5.145) is backpropagation of the gradient. The approach works when the function can be expressed as a computation graph with differentiable elementary functions. It may even be a computer program, but not every program can be differentiated, and `for` loops and `if` statements need more care (p. 164).

*Intuition note:* Reverse mode starts from the output and multiplies Jacobians toward the inputs, reusing partial products. When the input dimension is much higher than the output (label) dimension, as the author says is often the case for neural networks, reverse mode is computationally much cheaper than forward mode (p. 162).

### 5.7 Higher-order derivatives (pp. 164–165)
Second derivatives are needed, e.g., by Newton's method (p. 164). Notation for $f(x,y)$: $\partial^2f/\partial x^2$ is the second partial in $x$; $\partial^nf/\partial x^n$ is the $n$th; $\partial^2f/\partial y\partial x=\partial_y(\partial_xf)$ differentiates first in $x$, then $y$ (p. 164). The Hessian is the collection of all second-order partials.
If $f(x,y)$ is twice (continuously) differentiable, $\frac{\partial^2f}{\partial x\partial y}=\frac{\partial^2f}{\partial y\partial x}$ (5.146). So the Hessian $\mathbf H=\begin{bmatrix}\partial^2f/\partial x^2&\partial^2f/\partial x\partial y\\ \partial^2f/\partial x\partial y&\partial^2f/\partial y^2\end{bmatrix}$ (5.147) is symmetric. It is denoted $\nabla^2_{x,y}f$. For $f:\mathbb R^n\to\mathbb R$ it is n×n and measures local curvature. For a vector field $f:\mathbb R^n\to\mathbb R^m$ it is an $(m\times n\times n)$-tensor (p. 165).

### 5.8 Linearization and multivariate Taylor series (pp. 165–169)
The local linear approximation is
$$f(\mathbf x)\approx f(\mathbf x_0)+(\nabla_{\mathbf x}f)(\mathbf x_0)(\mathbf x-\mathbf x_0)\tag{5.148}$$
It is accurate near $\mathbf x_0$ and worsens farther away (Figure 5.12). It is the first two terms of the multivariate Taylor series (p. 165).

**Definition 5.7 (multivariate Taylor series)** for $f:\mathbb R^D\to\mathbb R$ smooth at $\mathbf x_0$, with $\boldsymbol\delta:=\mathbf x-\mathbf x_0$ (p. 166):
$$f(\mathbf x)=\sum_{k=0}^\infty\frac{D^k_{\mathbf x}f(\mathbf x_0)}{k!}\boldsymbol\delta^k\tag{5.151}$$
$D^k_{\mathbf x}f(\mathbf x_0)$ is the $k$-th (total) derivative at $\mathbf x_0$. **Definition 5.8 (Taylor polynomial of degree n)** keeps the first $n+1$ terms: $T_n(\mathbf x)=\sum_{k=0}^n\frac{D^k_{\mathbf x}f(\mathbf x_0)}{k!}\boldsymbol\delta^k$ (5.152).
The notation $\boldsymbol\delta^k$ is "slightly sloppy". Both $D^k_{\mathbf x}f$ and $\boldsymbol\delta^k$ are $k$-th order tensors, and $\boldsymbol\delta^k\in\mathbb R^{D\times\cdots\times D}$ is the $k$-fold outer product ⊗ of $\boldsymbol\delta$ (p. 166):
$$\boldsymbol\delta^2:=\boldsymbol\delta\otimes\boldsymbol\delta=\boldsymbol\delta\boldsymbol\delta^\top,\ \boldsymbol\delta^2[i,j]=\delta[i]\delta[j]\ (5.153);\qquad \boldsymbol\delta^3[i,j,k]=\delta[i]\delta[j]\delta[k]\ (5.154)$$
In general the terms are $D^k_{\mathbf x}f(\mathbf x_0)\boldsymbol\delta^k=\sum_{i_1=1}^D\cdots\sum_{i_k=1}^D D^k_{\mathbf x}f(\mathbf x_0)[i_1,\dots,i_k]\,\delta[i_1]\cdots\delta[i_k]$ (5.155). These contain $k$-th order polynomials (p. 167).
First terms (with $\mathbf H(\mathbf x_0)$ the Hessian at $\mathbf x_0$) (p. 167):
- $k=0$: $f(\mathbf x_0)$ (5.156)
- $k=1$: $\nabla_{\mathbf x}f(\mathbf x_0)\boldsymbol\delta=\sum_i\nabla_{\mathbf x}f(\mathbf x_0)[i]\delta[i]$ (shapes 1×D, D×1) (5.157)
- $k=2$: $\operatorname{tr}(\mathbf H\boldsymbol\delta\boldsymbol\delta^\top)=\boldsymbol\delta^\top\mathbf H(\mathbf x_0)\boldsymbol\delta=\sum_{i,j}H[i,j]\delta[i]\delta[j]$ (5.158–5.159)
- $k=3$: $\sum_{i,j,k}D^3_{\mathbf x}f(\mathbf x_0)[i,j,k]\delta[i]\delta[j]\delta[k]$ (5.160)

**Example 5.15:** $f(x,y)=x^2+2xy+y^3$ at $(x_0,y_0)=(1,2)$ (pp. 167–169). It is a degree-3 polynomial, so the first four terms should give an exact representation.
- Order 0 and 1: $f(1,2)=13$ (5.162). $\partial_xf=2x+2y\Rightarrow6$; $\partial_yf=2x+3y^2\Rightarrow14$ (5.163–5.164). So $\nabla f(1,2)=[6\ 14]\in\mathbb R^{1\times2}$ and the term is $6(x-1)+14(y-2)$ (5.165–5.166).
- Order 2: $\partial^2_xf=2$, $\partial^2_yf=6y\Rightarrow12$, and both mixed partials equal 2 (5.167–5.170). So $\mathbf H=\begin{bmatrix}2&2\\2&6y\end{bmatrix}$, $\mathbf H(1,2)=\begin{bmatrix}2&2\\2&12\end{bmatrix}$ (5.171–5.172). The term is $\tfrac12\boldsymbol\delta^\top\mathbf H(1,2)\boldsymbol\delta=(x-1)^2+2(x-1)(y-2)+6(y-2)^2$ (5.173).
- Order 3: $D^3f=[\partial\mathbf H/\partial x\ \ \partial\mathbf H/\partial y]\in\mathbb R^{2\times2\times2}$ (5.174–5.176). The only nonzero third derivative is $\partial^3f/\partial y^3=6$ (5.177). So slice 1 is the zero matrix and slice 2 is $\begin{bmatrix}0&0\\0&6\end{bmatrix}$ (5.178), and the cubic term is $\frac{D^3f}{3!}\boldsymbol\delta^3=(y-2)^3$ (5.179).
- Total: $f=13+6(x-1)+14(y-2)+(x-1)^2+6(y-2)^2+2(x-1)(y-2)+(y-2)^3$ (5.180). This equals the original polynomial (p. 169).

*Intuition note:* The gradient term is the tilted plane that touches f at x₀. The Hessian term adds curvature (a quadratic bowl or saddle), and so on. Adding terms improves the local fit.

### 5.9 Further reading (p. 170)
Expectations $\mathbb E_{\mathbf x}[f(\mathbf x)]=\int f(\mathbf x)p(\mathbf x)d\mathbf x$ (5.181) generally cannot be solved analytically, even for Gaussian $p$. One approximation: if $p=\mathcal N(\boldsymbol\mu,\boldsymbol\Sigma)$, a first-order Taylor expansion around $\boldsymbol\mu$ locally linearizes $f$. For linear functions the mean and covariance are exact under a Gaussian. The extended Kalman filter exploits this. The unscented transform needs no gradients. The Laplace approximation uses a second-order Taylor expansion (Hessian) to build a local Gaussian approximation of $p$ around its mode (p. 170).

## Toy example (ours)
Let $g(t)=[t,\ t^2]^\top$ and $f(\mathbf x)=x_1x_2$, so $h(t)=f(g(t))=t^3$ and $dh/dt=3t^2$.

*Chain rule with shapes:*
- $\partial f/\partial\mathbf x=[x_2\ \ x_1]\in\mathbb R^{1\times2}$. At $t=2$, $\mathbf x=[2,4]^\top$, so it equals $[4\ \ 2]$.
- $\partial g/\partial t=[1;\ 2t]\in\mathbb R^{2\times1}$. At $t=2$ it equals $[1;\ 4]$.
- Product: $4\cdot1+2\cdot4=12$. Direct: $3t^2=3\cdot4=12$. ✓.

*Gradient check with $h=0.1$:* $(2.1^3-2^3)/0.1=(9.261-8)/0.1=12.61$, close to 12. It gets closer as $h\to0$.

*Reverse mode:* take $a=x^2$, $b=3a$, $c=a+b$, $f=c$, at $x=2$. Then $a=4$, $b=12$, $c=16$.
- $\partial f/\partial c=1$.
- $\partial f/\partial b=1\cdot\partial c/\partial b=1$.
- $\partial f/\partial a=\partial f/\partial b\cdot3+\partial f/\partial c\cdot1=3+1=4$.
- $\partial f/\partial x=4\cdot2x=4\cdot4=16$.

Direct check: $f=4x^2$, so $f'=8x=16$ ✓. Each node's derivative is computed once and reused, and the two paths through $a$ are summed as in (5.145).

## Concepts
- `derivative` (new) — limit of the difference quotient; slope of the tangent (p. 141)
- `partial derivative` (new) — derivative with respect to one variable, others held fixed (p. 146)
- `gradient` (new) — row vector (1×n) of partials of a scalar function; points in the direction of steepest ascent (pp. 140, 146)
- `jacobian` (new) — m×n matrix of first partials of $\mathbf f:\mathbb R^n\to\mathbb R^m$, numerator layout (p. 150)
- `determinant` — here, $|\det\mathbf J|$ gives the local area/volume scaling under a coordinate change (p. 152)
- `change of basis` — the matrix with $\mathbf J\mathbf b_i=\mathbf c_i$ implements the basis change and is the Jacobian of a linear map (p. 151)
- `chain rule (multivariate)` (new) — Jacobians multiply, $\partial g/\partial\mathbf x=(\partial g/\partial f)(\partial f/\partial\mathbf x)$ (p. 148)
- `hessian` (new) — symmetric matrix of second partials; local curvature (p. 165)
- `taylor series / polynomial` (new) — infinite/finite sum of derivative-determined terms around $x_0$; multivariate version uses $\boldsymbol\delta^k$ (pp. 142, 166)
- `rank-one matrix / outer product` — $\boldsymbol\delta\otimes\boldsymbol\delta=\boldsymbol\delta\boldsymbol\delta^\top$; $k$-fold outer products give $k$-th order tensors (p. 166)
- `backpropagation` (new) — efficient gradient of a loss through a layered composition, reusing partial products (p. 159)
- `automatic differentiation` (new) — exact (to machine precision) derivatives from a computation graph; forward and reverse modes (p. 161)
- `computation graph` (new) — graph of intermediate variables and elementary operations (p. 162)
- `tensor` (new) — multidimensional array; gradients of matrices are tensors (p. 155)
- `least squares` — squared-error loss $\|\mathbf y-\boldsymbol\Phi\boldsymbol\theta\|^2$, with gradient $-2\mathbf e^\top\boldsymbol\Phi$ (p. 154)

## Canonical instances
- `gradient-of-linear-map` — $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$ (p. 153)
- `least-squares-gradient` — $\partial L/\partial\boldsymbol\theta=-2\mathbf e^\top\boldsymbol\Phi$ for the linear model (p. 154)
- `jacobian-area-scaling` — the parallelogram example with $|\det\mathbf J|=3$ (pp. 151–152)
- `deep-network-backprop` — layered loss gradients reuse partial products (pp. 159–161)
- `taylor-poly-exact` — a degree-3 polynomial reproduced exactly at (1,2) (pp. 167–169)
- `gram-matrix-gradient` — $d(\mathbf R^\top\mathbf R)/d\mathbf R$ (pp. 157–158)

## Bridges (candidates)
- [same-math] Jacobian of a linear map ↔ linear-algebra: matrix of a linear map. $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$, and the basis-change matrix equals the Jacobian (pp. 151–153).
- [same-math] Jacobian determinant ↔ probability: change-of-variables density factor. The text defers this to Section 6.7 (p. 152).
- [structural-analogy] Chain rule as product of Jacobians ↔ matrix multiplication as composition: neighbouring dimensions must match (p. 148).
- [same-math] Hessian symmetry and $\boldsymbol\delta^\top\mathbf H\boldsymbol\delta$ ↔ quadratic forms and symmetric matrices (canon link; not stated in this unit).
- [structural-analogy] Reverse-mode vs forward-mode ordering ↔ associativity of matrix products: the same product evaluated in different orders has different cost (p. 161).

## Questions this raises
- Why is the reverse order cheaper when there is one scalar output and many inputs? What is the cost in terms of matrix shapes?
- When does the Taylor series of a smooth function actually converge to the function (analytic vs merely $\mathcal C^\infty$)?
- How is the Hessian used in Newton's method and in the Laplace approximation, and when is it positive definite?
- How does the Jacobian determinant enter the change-of-variables formula for densities (Section 6.7)?

## Exercises worth doing
- Ex. 5.4 (p. 170) — Taylor polynomials $T_0$–$T_5$ of $\sin x+\cos x$ at 0; check against Example 5.4 — difficulty: easy
- Ex. 5.5 (pp. 170–171) — dimensions and Jacobians of $\sin x_1\cos x_2$, $\mathbf x^\top\mathbf y$, $\mathbf x\mathbf x^\top$ — difficulty: medium
- Ex. 5.6 (p. 171) — gradients of $\sin(\log(\mathbf t^\top\mathbf t))$ with respect to $\mathbf t$ and of $\operatorname{tr}(\mathbf A\mathbf X\mathbf B)$ with respect to $\mathbf X$ — difficulty: medium
- Ex. 5.7 (p. 171) — chain rule with dimensions of every partial: $\log(1+\mathbf x^\top\mathbf x)$ and $\sin(\mathbf A\mathbf x+\mathbf b)$ — difficulty: medium
- Ex. 5.8c (p. 171) — Jacobian of $\tanh(\mathbf A\mathbf x+\mathbf b)$ via the chain rule — difficulty: medium
- Ex. 5.9 (p. 171) — gradient of $g=\log p(\mathbf x,\mathbf z)-\log q(\mathbf z,\boldsymbol\nu)$ with $\mathbf z=t(\boldsymbol\epsilon,\boldsymbol\nu)$ with respect to $\boldsymbol\nu$ — difficulty: hard

## Reading notes
- Printed page = pdf page − 6 (pdf 145 = printed 139). The page labels give printed numbers directly.
- Page footers: "Draft (2024-01-15)" and "©2024 … Published by Cambridge University Press (2020)".
- The text layer garbles many equations (e.g. (5.53), (5.56), (5.74), (5.98)). All equations here were checked against the page images.
- Inconsistency: p. 160 says parameters $\mathbf A_j,\mathbf b_j$ for $j=1,\dots,K$, but (5.114) and later text use $j=0,\dots,K-1$.
- Typo on p. 164: "differential elementary functions" presumably means differentiable ones.
- Definition 5.2 is printed as "for $h>0$" while the limit is $h\to0$.
- Exercise 5.5 refers to "∂fᵢ/∂x" in part a. Solutions are not printed in this unit.
