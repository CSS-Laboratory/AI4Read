---
id: sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional
work: sarkka-2023-bayesianfiltering
unit: "Appendix A — Additional Material"
pages: 355-378
fields: [control-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Appendix A: Additional Material (Gaussian identities, SDE solutions, motion-model discretizations, SLR moments, parameter derivatives)

## L0 — One line
This appendix holds the supporting derivations (Gaussian conditioning, matrix identities, affine SDE solution, model discretizations, SLR moment formulas, and parameter derivatives of filter energy functions) that the main chapters use without proof.

## L1 — The gist (≤ 120 words)
The appendix collects tools that the main chapters cite. It gives Gaussian joint and conditional formulas, block-matrix inversion identities, the Cholesky factor and its derivative, the exact solution of affine stochastic differential equations (SDEs), and the derivation of the covariance ODE. It also gives closed-form discretizations of the bicycle and polar coordinated turn models, explicit moment formulas for statistical linear regression (SLR), and recursions for derivatives of the Kalman and Gaussian-filter energy functions (negative log unnormalized posteriors of the model parameters). These support Kalman equations, model discretizations and gradient-based maximum-likelihood or maximum a posteriori (MAP) parameter estimation.

**Prerequisites:** multivariate Gaussian density; block matrices and inverses; matrix exponential; matrix derivatives and trace; Kalman filter notation (innovation, gain); Jacobians.

## L2 — Key ideas (5–10 bullets)
- Joint Gaussians have closed-form marginals and conditionals; conditioning gives mean $a + CB^{-1}(y-b)$ and covariance $A - CB^{-1}C^\top$ (pp. 355–356).
- Block inversion yields the matrix inversion lemmas (A.8)–(A.9), which the text calls sometimes useful in deriving Gaussian conditioning and Kalman filtering and smoothing equations (pp. 356–357).
- The Cholesky factor's derivative is $A\,\Phi(A^{-1}(\partial P/\partial\theta)A^{-\top})$, with $\Phi$ keeping the strict lower part plus half the diagonal (p. 358).
- An affine SDE has solution $e^{F\tau}x(t)$ plus a deterministic integral plus a Gaussian integral, so $x(t+\tau)\mid x(t)$ is Gaussian with explicit moments (pp. 359–362).
- The covariance ODE of Theorem 4.13 follows from an $h$-step expansion in which the white-noise integral is kept intact (pp. 362–363).
- Bicycle and polar coordinated turn mean ODEs integrate in closed form; the constant-gradient approximation of the turn-model $Q_{k-1}$ integrates in closed form because $(A_x)^n=0$ for $n\ge3$ (pp. 363–367).
- Statistical linear regression (SLR) needs $\mu^-_k$, $P^{xx}_k$, $P^{x}_k$ (dynamics) or $\mu^+_k$, $P^{xy}_k$, $P^{y}_k$ (measurements); five different expressions are given (one for additive noise, two each for non-additive and conditional-distribution models) (pp. 367–371).
- Sensitivity recursions give exact gradients of the energy function (negative log unnormalized posterior of the parameters) for the Kalman filter; the Gaussian-filter version uses unit-Gaussian changes of variable (pp. 371–378).

## L3 — Walkthrough

### A.1 Properties of the Gaussian distribution (pp. 355–356)
**Definition A.1.** $x\in\mathbb R^n$ is Gaussian with mean $m$ and covariance $P$ if its density is
$$\mathrm N(x\mid m,P)=\frac{1}{(2\pi)^{n/2}|P|^{1/2}}\exp\!\Big(-\tfrac12 (x-m)^\top P^{-1}(x-m)\Big),\tag{A.1}$$
with $|P|$ the determinant (p. 355).

**Lemma A.2 (joint).** If $x\in\mathbb R^n$, $y\in\mathbb R^m$ with $x\sim\mathrm N(m,P)$ and $y\mid x\sim \mathrm N(Hx+u,R)$ (A.2), then
$$\begin{pmatrix}x\\y\end{pmatrix}\sim \mathrm N\!\left(\begin{pmatrix}m\\Hm+u\end{pmatrix},\begin{pmatrix}P & PH^\top\\ HP & HPH^\top+R\end{pmatrix}\right),\quad y\sim\mathrm N(Hm+u,\,HPH^\top+R).\tag{A.3}$$
(p. 355)

**Lemma A.3 (conditional).** If $\begin{pmatrix}x\\y\end{pmatrix}\sim\mathrm N\Big(\begin{pmatrix}a\\b\end{pmatrix},\begin{pmatrix}A&C\\C^\top&B\end{pmatrix}\Big)$ (A.4), then (p. 356)
$$\begin{aligned}x&\sim\mathrm N(a,A),\quad y\sim\mathrm N(b,B),\\ x\mid y&\sim \mathrm N\big(a+CB^{-1}(y-b),\,A-CB^{-1}C^\top\big),\\ y\mid x&\sim \mathrm N\big(b+C^\top A^{-1}(x-a),\,B-C^\top A^{-1}C\big).\end{aligned}\tag{A.5}$$

*Intuition note.* A linear-Gaussian measurement gives a joint Gaussian, and a joint Gaussian can be sliced. Conditioning shifts the mean by a gain times the surprise $y-b$ and shrinks the covariance.

### A.2 Block matrix inverses and matrix inversion formulas (pp. 356–357)
The block formulas are "easy to verify by direct calculation" (p. 356).

**Theorem A.4.** If $A$ and $D-CA^{-1}B$ are invertible,
$$\begin{pmatrix}A&B\\C&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}+A^{-1}B(D-CA^{-1}B)^{-1}CA^{-1} & -A^{-1}B(D-CA^{-1}B)^{-1}\\ -(D-CA^{-1}B)^{-1}CA^{-1} & (D-CA^{-1}B)^{-1}\end{pmatrix}.\tag{A.6}$$
If $D$ and $A-BD^{-1}C$ are invertible,
$$\begin{pmatrix}A&B\\C&D\end{pmatrix}^{-1}=\begin{pmatrix}(A-BD^{-1}C)^{-1} & -(A-BD^{-1}C)^{-1}BD^{-1}\\ -D^{-1}C(A-BD^{-1}C)^{-1} & D^{-1}+D^{-1}C(A-BD^{-1}C)^{-1}BD^{-1}\end{pmatrix}.\tag{A.7}$$

**Corollary A.5.** Put $A=P^{-1}$, $D=R$, $B=-H^\top$, $C=H$ and match top-left blocks of (A.6) and (A.7):
$$(P^{-1}+H^\top R^{-1}H)^{-1}=P-PH^\top(R+HPH^\top)^{-1}HP.\tag{A.8}$$
Matching top-right blocks:
$$(P^{-1}+H^\top R^{-1}H)^{-1}H^\top R^{-1}=PH^\top(R+HPH^\top)^{-1}.\tag{A.9}$$
(p. 357)

*Intuition note.* The same matrix can be inverted by eliminating either block first, so the two block forms must agree. Equating their blocks gives two ways to write a posterior covariance and a gain.

### A.3 Cholesky factorization and its derivative (pp. 357–359)
The Cholesky factor of a symmetric positive definite $P$ is the lower triangular $A$ with
$$P=AA^\top.\tag{A.10}$$
**Algorithm A.6 (CHOL).** For $i=1,\dots,n$: $A_{ii}=\sqrt{P_{ii}-\sum_{k<i}A_{ik}^2}$; then for $j=i+1,\dots,n$: $A_{ji}=\big(P_{ji}-\sum_{k<i}A_{jk}A_{ik}\big)/A_{ii}$ (p. 357).

**Algorithm A.7 (DCHOL).** Given $P$ and $\partial P/\partial\theta$, compute $D=\partial A/\partial\theta$ by formally differentiating Algorithm A.6. For $i=1..n$ (pp. 357–358):
- $A_{ii}\leftarrow\sqrt{P_{ii}-\sum_{k<i}A_{ik}^2}$;
- $D_{ii}\leftarrow\big(\partial P_{ii}/\partial\theta-\sum_{k<i}2D_{ik}A_{ik}\big)/A_{ii}/2$;
- for $j=i+1..n$: $A_{ji}\leftarrow(P_{ji}-\sum_{k<i}A_{jk}A_{ik})/A_{ii}$;
  $\mathrm{temp}\leftarrow\partial P_{ji}/\partial\theta-\sum_{k<i}(D_{jk}A_{ik}+A_{jk}D_{ik})$;
  $D_{ji}\leftarrow\mathrm{temp}/A_{ii}-(D_{ii}/A_{ii})A_{ji}$.

**Theorem A.8.** With $P=AA^\top$,
$$\frac{\partial A}{\partial\theta}=A\,\Phi\!\Big(A^{-1}\frac{\partial P}{\partial\theta}A^{-\top}\Big),\tag{A.11}$$
$$\Phi_{ij}(M)=\begin{cases}M_{ij}& i>j\\ \tfrac12M_{ij}& i=j\\ 0& i<j.\end{cases}\tag{A.12}$$
*Proof (key steps).* $P=AA^\top$ (A.13). Differentiate: $\partial P/\partial\theta=(\partial A/\partial\theta)A^\top+A\,\partial A^\top/\partial\theta$ (A.14). Multiply by $A^{-1}$ on the left and $A^{-\top}$ on the right:
$$A^{-1}\frac{\partial P}{\partial\theta}A^{-\top}=A^{-1}\frac{\partial A}{\partial\theta}+\frac{\partial A^\top}{\partial\theta}A^{-\top}.\tag{A.15}$$
The right side is a lower triangular matrix plus an upper triangular matrix with identical diagonals. So $A^{-1}\partial A/\partial\theta=\Phi\big(A^{-1}\frac{\partial P}{\partial\theta}A^{-\top}\big)$ (A.16); multiplying by $A$ gives (A.11) (pp. 358–359).

*Intuition note.* The sum of the lower triangular matrix $A^{-1}\partial A/\partial\theta$ and its transpose equals the whole symmetric matrix $A^{-1}(\partial P/\partial\theta)A^{-\top}$, with the diagonal counted twice. So the strictly lower part plus half the diagonal identifies it uniquely.

### A.4 Affine stochastic differential equations (pp. 359–362)
**Lemma A.9.** Let $\dfrac{dx(t)}{dt}=Fx(t)+b(t)+Lw(t)$ (A.17), with $F$ constant, $b(t)$ deterministic, and $w(t)$ white Gaussian noise with the moments (4.4). Then
$$x(t+\tau)=e^{F\tau}x(t)+\int_t^{t+\tau}e^{F(t+\tau-v)}b(v)\,dv+\int_t^{t+\tau}e^{F(t+\tau-v)}Lw(v)\,dv.\tag{A.18}$$
The last integral is zero-mean Gaussian with covariance
$$\int_0^\tau e^{Fv}LQ^{c}L^\top e^{F v\,\top}dv.\tag{A.19}$$
Hence $x(t+\tau)\mid x(t)$ is Gaussian with
$$\mathrm E[x(t+\tau)\mid x(t)]=e^{F\tau}x(t)+\int_t^{t+\tau}e^{F(t+\tau-v)}b(v)\,dv,\qquad \mathrm{Cov}[x(t+\tau)\mid x(t)]=\int_0^\tau e^{Fv}LQ^{c}L^\top e^{Fv\,\top}dv.\tag{A.20}$$
If $b(t)=b$ is constant,
$$\int_t^{t+\tau}e^{F(t+\tau-v)}b\,dv=\int_0^\tau e^{Fv}dv\;b=\Big(\sum_{i=1}^\infty\frac{\tau^iF^{i-1}}{i!}\Big)b.\tag{A.21}$$
(pp. 359–360)

*Proof.*
- Multiply (A.17) by the integrating factor $e^{-Ft}$ (A.22). From $e^{Ft}=\sum_i F^it^i/i!$ (A.23), $\frac{d}{dt}e^{-Ft}=-Fe^{-Ft}$.
- The left side of (A.22) is then $\frac{d}{dt}(e^{-Ft}x(t))$, so $\frac{d}{dt}(e^{-Ft}x(t))=e^{-Ft}(b(t)+Lw(t))$ (A.24).
- Integrate from $t$ to $t+\tau$ (A.25) and multiply by $e^{F(t+\tau)}$ to get (A.18) (p. 360).
- For constant $b$: change variables and integrate the series termwise, $\int_0^\tau\sum_i F^iv^i/i!\,dv=\sum_i F^i\tau^{i+1}/(i+1)!=I\tau+F\tau^2/2+F^2\tau^3/3!+\cdots$ (A.27), confirming (A.21) (p. 361).
- Covariance: it is the expectation of the vector times its transpose, with $\mathrm E[w(v_1)w^\top(v_2)]=Q^c\delta(v_1-v_2)$ and the sifting property $\int\delta(v-v_0)f(v)dv=f(v_0)$. The double integral collapses to a single one (A.28), and the substitution $v\to t+\tau-v$ gives (A.19) (pp. 361–362).

*Intuition note.* The solution is the variation-of-constants formula: the old state decays or rotates by $e^{F\tau}$, deterministic inputs are carried forward the same way, and the noise integral adds a Gaussian term.

### A.5 Time derivative of covariance in Theorem 4.13 (pp. 362–363)
Let $P(t)=\mathrm E[(x-m)(x-m)^\top]$ and $dP/dt=\lim_{h\to0}(P(t+h)-P(t))/h$ (A.29; the source prints $h\to\infty$, see Reading notes). We seek $P(t+h)$ up to $o(h)$ terms (p. 362). The increments are
$$x(t+h)-x(t)=\int_t^{t+h}a(m(s))ds+\int_t^{t+h}A_x(m(s))(x(s)-m(s))ds+\int_t^{t+h}Lw(s)ds,\tag{A.30}$$
$$m(t+h)-m(t)=\int_t^{t+h}a(m(s))ds.\tag{A.31}$$
Subtracting,
$$x(t+h)-m(t+h)=[x(t)-m(t)]+A_x(m(t))(x(t)-m(t))h+o(h)+\int_t^{t+h}Lw(s)ds.\tag{A.32}$$
The white-noise integral is left intact because $\int_t^{t+h}Lw\,ds\neq Lw(t)h+o(h)$; Equation (4.4) is used instead. It is independent of the other terms and has zero mean, so cross terms vanish and
$$P(t+h)=P(t)+A_x(m(t))P(t)h+P(t)A_x^\top(m(t))h+LQ^cL^\top h+o(h).\tag{A.33}$$
(added step) Subtracting $P(t)$, dividing by $h$ and letting $h\to0$ gives $dP/dt=A_xP+PA_x^\top+LQ^cL^\top$ with $A_x=A_x(m(t))$. The text says this yields Equation (4.53) (p. 363).

*Intuition note.* Over a short step the covariance changes by the drift's linear part acting on both sides and by noise adding $LQ^cL^\top h$. The noise term is linear in $h$ (not $h^2$) because of the white-noise property.

### A.6 Derivation of mean for the bicycle model (pp. 363–364)
State $x=(x_1,x_2,s,\theta,\delta)$ with
$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\\s\\\theta\\\delta\end{pmatrix}=\begin{pmatrix}s\cos\theta\\ s\sin\theta\\0\\ s/r\\0\end{pmatrix},\quad r(t)=L/\tan\delta(t),\tag{A.34}$$
and initial condition $x(t_{k-1})=x_{k-1}$. Then $s(t)=s_{k-1}$, $\delta(t)=\delta_{k-1}$, so $r_{k-1}=L/\tan\delta_{k-1}$ and $\theta(t)=\theta_{k-1}+(t-t_{k-1})s_{k-1}/r_{k-1}$ (p. 363). Integrating,
$$x_1(t)=x_{1,k-1}+\int_0^{t-t_{k-1}}s_{k-1}\cos(\theta_{k-1}+v\,s_{k-1}/r_{k-1})dv=x_{1,k-1}+r_{k-1}\big(\sin(\theta_{k-1}+(t-t_{k-1})s_{k-1}/r_{k-1})-\sin\theta_{k-1}\big).\tag{A.35}$$
Similarly for $x_2$. With $\beta(t)=t\,s_{k-1}/r_{k-1}$ (evaluated at $t-t_{k-1}$):
$$x(t)=\Big(x_{1,k-1}+r_{k-1}[\sin(\theta_{k-1}+\beta(t-t_{k-1}))-\sin\theta_{k-1}],\; x_{2,k-1}+r_{k-1}[\cos\theta_{k-1}-\cos(\theta_{k-1}+\beta(t-t_{k-1}))],\; s_{k-1},\;\theta_{k-1}+\beta(t-t_{k-1}),\;\delta_{k-1}\Big).\tag{A.36}$$
At $t=t_k$ this is the discretized model, Equation (4.66) (p. 364).

### A.7 Mean discretization for the polar coordinated turn model (pp. 364–365)
State $x=(x_1,x_2,s,\varphi,\omega)$, ODE (4.56), initial condition $x_{k-1}$. Because $\dot s=\dot\omega=0$: $s(t)=s_{k-1}$, $\omega(t)=\omega_{k-1}$ (A.37). Because $\omega=\dot\varphi$: $\varphi(t)=\varphi(t_{k-1})+(t-t_{k-1})\omega(t_{k-1})$ (A.38). Then
$$x_1(t)=x_{1,k-1}+\int_{t_{k-1}}^ts_{k-1}\cos(\varphi_{k-1}+(v-t_{k-1})\omega_{k-1})dv=x_{1,k-1}+\frac{s_{k-1}}{\omega_{k-1}}\big(\sin(\varphi_{k-1}+(t-t_{k-1})\omega_{k-1})-\sin\varphi_{k-1}\big)$$
$$=x_{1,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\Big(\frac{(t-t_{k-1})\omega_{k-1}}{2}\Big)\cos\!\Big(\varphi_{k-1}+\frac{(t-t_{k-1})\omega_{k-1}}{2}\Big).\tag{A.39}$$
By similar calculations
$$x_2(t)=x_{2,k-1}+\frac{2s_{k-1}}{\omega_{k-1}}\sin\!\Big(\frac{(t-t_{k-1})\omega_{k-1}}{2}\Big)\sin\!\Big(\varphi_{k-1}+\frac{(t-t_{k-1})\omega_{k-1}}{2}\Big).\tag{A.40}$$
The discretization is obtained at $t=t_k$ (p. 365).

### A.8 Approximating $Q_{k-1}$ in the polar coordinated turn model (pp. 365–367)
This derives the constant-gradient covariance approximation of Algorithm 4.19, using the mean from A.7:
$$Q_{k-1}=\int_0^{\Delta t_{k-1}}e^{A_x(x_{k-1})v}LQ^cL^\top e^{A_x(x_{k-1})v\,\top}dv.\tag{A.41}$$
With $x_{k-1}=(x_1,x_2,s,\varphi,\omega)^\top$ (A.42), (4.56) gives
$$A_x(x_{k-1})=\begin{pmatrix}0&0&\cos\varphi&-s\sin\varphi&0\\0&0&\sin\varphi&s\cos\varphi&0\\0&0&0&0&0\\0&0&0&0&1\\0&0&0&0&0\end{pmatrix},\tag{A.43}$$
$$(A_x)^2=\begin{pmatrix}0&0&0&0&-s\sin\varphi\\0&0&0&0&s\cos\varphi\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\end{pmatrix},\tag{A.44}$$
and $(A_x)^n=0$ for $n\ge3$. Hence the exponential series stops:
$$e^{A_xv}=I+vA_x+\tfrac{v^2}{2}A_x^2=\begin{pmatrix}1&0&v\cos\varphi&-vs\sin\varphi&-\frac{v^2}{2}s\sin\varphi\\0&1&v\sin\varphi&vs\cos\varphi&\frac{v^2}{2}s\cos\varphi\\0&0&1&0&0\\0&0&0&1&v\\0&0&0&0&1\end{pmatrix}.\tag{A.45}$$
With $L$ from (4.43) (not shown in this unit),
$$e^{A_xv}L=\begin{pmatrix}v\cos\varphi&-\frac{v^2}{2}s\sin\varphi\\ v\sin\varphi&\frac{v^2}{2}s\cos\varphi\\1&0\\0&v\\0&1\end{pmatrix}.\tag{A.46}$$
(added step) These two columns are columns 3 and 5 of (A.45).

Assume $Q^c=\mathrm{diag}(q_1,q_2)$. Write $\mathrm{si}=\sin\varphi$, $\mathrm{co}=\cos\varphi$, $\mathrm{cs}=\sin\varphi\cos\varphi$. The lower triangle of the symmetric integrand is
$$e^{A_xv}LQ^cL^\top e^{A_xv\,\top}=\begin{pmatrix}q_1v^2\mathrm{co}^2+q_2\frac{v^4}{4}s^2\mathrm{si}^2\\ q_1v^2\mathrm{cs}-q_2\frac{v^4}{4}s^2\mathrm{cs}& q_1v^2\mathrm{si}^2+q_2\frac{v^4}{4}s^2\mathrm{co}^2\\ q_1v\,\mathrm{co}&q_1v\,\mathrm{si}&q_1\\ -q_2s\frac{v^3}{2}\mathrm{si}&q_2s\frac{v^3}{2}\mathrm{co}&0&q_2v^2\\ -q_2s\frac{v^2}{2}\mathrm{si}&q_2s\frac{v^2}{2}\mathrm{co}&0&q_2v&q_2\end{pmatrix}.\tag{A.47}$$
Integrating over $v\in[0,\tau]$ gives (the source labels it $P(\tau+t_{k-1})$):
$$\begin{pmatrix}q_1\frac{\tau^3}{3}\mathrm{co}^2+q_2\frac{\tau^5}{20}s^2\mathrm{si}^2\\ q_1\frac{\tau^3}{3}\mathrm{cs}-q_2\frac{\tau^5}{20}s^2\mathrm{cs}& q_1\frac{\tau^3}{3}\mathrm{si}^2+q_2\frac{\tau^5}{20}s^2\mathrm{co}^2\\ q_1\frac{\tau^2}{2}\mathrm{co}&q_1\frac{\tau^2}{2}\mathrm{si}&q_1\tau\\ -q_2s\frac{\tau^4}{8}\mathrm{si}&q_2s\frac{\tau^4}{8}\mathrm{co}&0&q_2\frac{\tau^3}{3}\\ -q_2s\frac{\tau^3}{6}\mathrm{si}&q_2s\frac{\tau^3}{6}\mathrm{co}&0&q_2\frac{\tau^2}{2}&q_2\tau\end{pmatrix}.\tag{A.48}$$
Setting $\tau=\Delta t_{k-1}$ gives $Q_{k-1}$ (p. 367).

*Intuition note (A.6–A.8).* When the drift is "constant speed and turn rate," the ODE integrates exactly, which gives the sine/cosine updates. Because $A_x$ is nilpotent in the turn model, its exponential is a short polynomial, so the integral in the constant-gradient approximation of $Q_{k-1}$ reduces to integrating polynomials in $v$.

### A.9 Conditional moments used in SLR (pp. 367–371)
SLR (statistical linear regression) approximates dynamic and measurement models by linear ones with Gaussian error. Theorems 9.12 and 9.16 with Corollaries 9.14, 9.17, 9.18 give five expression types: one for additive noise (9.1), two each for non-additive noise (9.9) and conditional-distribution models (9.10) (p. 367).

**Dynamic model.** $x_k\simeq A_{k-1}x_{k-1}+a_{k-1}+e_{k-1}$, $e_{k-1}\sim\mathrm N(0,\Lambda_{k-1})$ (A.49). If $x_{k-1}\sim\mathrm N(\tilde m_{k-1},\tilde P_{k-1})$,
$$A_{k-1}=(P^{xx}_k)^\top\tilde P_{k-1}^{-1},\quad a_{k-1}=\mu^-_k-A_{k-1}\tilde m_{k-1},\quad \Lambda_{k-1}=P^x_k-A_{k-1}\tilde P_{k-1}A_{k-1}^\top,\tag{A.50}$$
with $\mu^-_k=\mathrm E[x_k]$, $P^{xx}_k=\mathrm{Cov}[x_{k-1},x_k]$, $P^x_k=\mathrm{Cov}[x_k]$. Tildes mark that the equations hold for any mean and covariance, but the choice influences the SLR approximation (footnote, p. 367). Write $\mathcal N=\mathrm N(x_{k-1}\mid\tilde m_{k-1},\tilde P_{k-1})$.
- Additive noise (A.51): $\mu_k^-=\int f(x_{k-1})\mathcal N dx_{k-1}$; $P^{xx}_k=\int(x_{k-1}-\tilde m_{k-1})(f(x_{k-1})-\mu^-_k)^\top\mathcal N dx_{k-1}$; $P^x_k=\int(f(x_{k-1})-\mu^-_k)(f(x_{k-1})-\mu^-_k)^\top\mathcal N dx_{k-1}+Q_{k-1}$.
- Non-additive noise (A.52): same integrands with $f(x_{k-1},q_{k-1})$, no $+Q_{k-1}$, and the extra weight $\mathrm N(q_{k-1}\mid0,Q_{k-1})$, integrated over $dx_{k-1}dq_{k-1}$.
- Conditional distribution (A.53): integrate over $x_k$ and $x_{k-1}$ with weight $p(x_k\mid x_{k-1})\mathcal N$; e.g. $\mu^-_k=\int x_k\,p(x_k\mid x_{k-1})\mathcal N\,dx_kdx_{k-1}$, and $P^x_k$ uses $(x_k-\mu_k^-)(x_k-\mu_k^-)^\top$.
- Conditional-moments forms (A.54): with $\mu^-_k(x_{k-1})=\mathrm E[x_k\mid x_{k-1}]$ and $P^x_k(x_{k-1})=\mathrm{Cov}[x_k\mid x_{k-1}]$,
$\mu_k^-=\int\mu^-_k(x_{k-1})\mathcal N dx_{k-1}$, $P^{xx}_k=\int(x_{k-1}-\tilde m_{k-1})(\mu_k^-(x_{k-1})-\mu^-_k)^\top\mathcal N dx_{k-1}$, $P^x_k=\int(\mu^-_k(x_{k-1})-\mu^-_k)(\cdot)^\top\mathcal Ndx_{k-1}+\int P^x_k(x_{k-1})\mathcal Ndx_{k-1}$. For additive noise $\mu_k^-(x_{k-1})=f(x_{k-1})$ and $P^x_k(x_{k-1})=Q_{k-1}$, so (A.54) reduces to (A.51) (p. 369).
- Conditional moments for non-additive noise (A.55): $\mu^-_k(x_{k-1})=\int f(x_{k-1},q_{k-1})\mathrm N(q_{k-1}\mid0,Q_{k-1})dq_{k-1}$ and $P^x_k(x_{k-1})$ is the covariance integral around it. For conditional-distribution models (A.56): $\mu_k^-(x_{k-1})=\int x_kp(x_k\mid x_{k-1})dx_k$ and $P^x_k(x_{k-1})=\int(x_k-\mu^-_k(x_{k-1}))(\cdot)^\top p(x_k\mid x_{k-1})dx_k$ (p. 369).

**Measurement model.** $y_k\simeq H_kx_k+b_k+v_k$, $v_k\sim\mathrm N(0,\Omega_k)$ (A.57). If $x_k\sim\mathrm N(\tilde m_k,\tilde P_k)$,
$$H_k=(P^{xy}_k)^\top\tilde P_k^{-1},\quad b_k=\mu^+_k-H_k\tilde m_k,\quad\Omega_k=P^y_k-H_k\tilde P_kH_k^\top,\tag{A.58}$$
with $\mu^+_k=\mathrm E[y_k]$, $P^{xy}_k=\mathrm{Cov}[x_k,y_k]$, $P^y_k=\mathrm{Cov}[y_k]$. Equations (A.59)–(A.64) are the same five forms as (A.51)–(A.56), with $f(x_{k-1})\to h(x_k)$, $x_{k-1}\to x_k$, $x_k\to y_k$, $Q\to R_k$, $q\to r_k$, $\mathrm N(\tilde m_{k-1},\tilde P_{k-1})\to\mathrm N(\tilde m_k,\tilde P_k)$. For example, additive noise (A.59):
$$\mu^+_k=\int h(x_k)\mathrm N(x_k\mid\tilde m_k,\tilde P_k)dx_k,\quad P^{y}_k=\int(h(x_k)-\mu^+_k)(h(x_k)-\mu^+_k)^\top\mathrm N(x_k\mid\tilde m_k,\tilde P_k)dx_k+R_k,$$
and $P^{xy}_k=\int(x_k-\tilde m_k)(h(x_k)-\mu_k^+)^\top\mathrm N(\cdot)dx_k$. In the conditional-moments form, $\mu_k^+(x_k)=h(x_k)$ and $P^y_k(x_k)=R_k$ for additive noise, reducing (A.62) to (A.59) (pp. 370–371). The text counts five alternatives for each of the two models (p. 371).

*Intuition note.* SLR needs only three moments of the pair (input, output) under the chosen Gaussian. How you compute them depends on how the noise enters, but all five expression types compute the same three moments.

### A.10 Parameter derivatives for the Kalman filter (pp. 371–374)
Model (A.65): $x_k=A(\theta)x_{k-1}+q_{k-1}$, $y_k=H(\theta)x_k+r_k$, with $q_{k-1}\sim\mathrm N(0,Q(\theta))$, $r_k\sim\mathrm N(0,R(\theta))$, $x_0\sim\mathrm N(m_0(\theta),P_0(\theta))$ (pp. 371–372). Theorem 16.9 gives the energy function $\varphi_k(\theta)$. The symbols $v_k$, $S_k$, $K_k$ are those of its Kalman filter (not defined in this unit; presumably innovation, its covariance, and gain). Derivatives are shaped like the matrix differentiated. The recursions (Gupta and Mehra, 1974) are used for gradient-based ML/MAP.

**Theorem A.10.** Run alongside the Kalman filter:
$$\frac{\partial\varphi_k}{\partial\theta_i}=\frac{\partial\varphi_{k-1}}{\partial\theta_i}+\frac12\mathrm{tr}\Big(S_k^{-1}\frac{\partial S_k}{\partial\theta_i}\Big)+v_k^\top S_k^{-1}\frac{\partial v_k}{\partial\theta_i}-\frac12v_k^\top S_k^{-1}\frac{\partial S_k}{\partial\theta_i}S_k^{-1}v_k.\tag{A.66}$$
Prediction step:
$$\frac{\partial m^-_k}{\partial\theta_i}=\frac{\partial A}{\partial\theta_i}m_{k-1}+A\frac{\partial m_{k-1}}{\partial\theta_i},$$
$$\frac{\partial P^-_k}{\partial\theta_i}=\frac{\partial A}{\partial\theta_i}P_{k-1}A^\top+A\frac{\partial P_{k-1}}{\partial\theta_i}A^\top+AP_{k-1}\frac{\partial A^\top}{\partial\theta_i}+\frac{\partial Q}{\partial\theta_i}.\tag{A.67}$$
Update step:
$$\begin{aligned}\frac{\partial v_k}{\partial\theta_i}&=-\frac{\partial H}{\partial\theta_i}m^-_k-H\frac{\partial m^-_k}{\partial\theta_i},\\
\frac{\partial S_k}{\partial\theta_i}&=\frac{\partial H}{\partial\theta_i}P^-_kH^\top+H\frac{\partial P^-_k}{\partial\theta_i}H^\top+HP^-_k\frac{\partial H^\top}{\partial\theta_i}+\frac{\partial R}{\partial\theta_i},\\
\frac{\partial K_k}{\partial\theta_i}&=\frac{\partial P_k^-}{\partial\theta_i}H^\top S_k^{-1}+P^-_k\frac{\partial H^\top}{\partial\theta_i}S_k^{-1}-P^-_kH^\top S_k^{-1}\frac{\partial S_k}{\partial\theta_i}S_k^{-1},\\
\frac{\partial m_k}{\partial\theta_i}&=\frac{\partial m_k^-}{\partial\theta_i}+\frac{\partial K_k}{\partial\theta_i}v_k+K_k\frac{\partial v_k}{\partial\theta_i},\\
\frac{\partial P_k}{\partial\theta_i}&=\frac{\partial P^-_k}{\partial\theta_i}-\frac{\partial K_k}{\partial\theta_i}S_kK_k^\top-K_k\frac{\partial S_k}{\partial\theta_i}K_k^\top-K_kS_k\frac{\partial K_k^\top}{\partial\theta_i}.\end{aligned}\tag{A.68}$$
The recursion starts from $\partial\varphi_0/\partial\theta=-\partial\log p(\theta)/\partial\theta$ (p. 373). (All arguments $\theta$ omitted above.)

**Theorem A.11.** By Fisher's identity (Eq. 16.32) and the expression for $\mathcal Q$ in Theorem 16.11,
$$\frac{\partial\varphi_T(\theta)}{\partial\theta}=-\frac{\partial\log p(\theta)}{\partial\theta}-\frac{\partial\mathcal Q(\theta,\theta^{(n)})}{\partial\theta}\Big|_{\theta^{(n)}=\theta},\tag{A.69}$$
where, with everything evaluated at $\theta$ and $\Sigma,\Phi,C,B,D,m_0^s,P_0^s$ the smoother-based quantities of Theorem 16.11 (not defined here),
$$\begin{aligned}\frac{\partial\mathcal Q}{\partial\theta_i}\Big|_{\theta^{(n)}=\theta}={}&-\tfrac12\mathrm{tr}\Big(P_0^{-1}\frac{\partial P_0}{\partial\theta_i}\Big)-\tfrac T2\mathrm{tr}\Big(Q^{-1}\frac{\partial Q}{\partial\theta_i}\Big)-\tfrac T2\mathrm{tr}\Big(R^{-1}\frac{\partial R}{\partial\theta_i}\Big)\\
&+\tfrac12\mathrm{tr}\Big\{P_0^{-1}\frac{\partial P_0}{\partial\theta_i}P_0^{-1}\big[P_0^s+(m_0^s-m_0)(m_0^s-m_0)^\top\big]\Big\}\\
&+\tfrac12\mathrm{tr}\Big\{P_0^{-1}\Big[\frac{\partial m_0}{\partial\theta_i}(m_0^s-m_0)^\top+(m_0^s-m_0)\frac{\partial m_0^\top}{\partial\theta_i}\Big]\Big\}\\
&+\tfrac T2\mathrm{tr}\Big\{Q^{-1}\frac{\partial Q}{\partial\theta_i}Q^{-1}\big[\Sigma-CA^\top-AC^\top+A\Phi A^\top\big]\Big\}\\
&-\tfrac T2\mathrm{tr}\Big\{Q^{-1}\Big[-C\frac{\partial A^\top}{\partial\theta_i}-\frac{\partial A}{\partial\theta_i}C^\top+\frac{\partial A}{\partial\theta_i}\Phi A^\top+A\Phi\frac{\partial A^\top}{\partial\theta_i}\Big]\Big\}\\
&+\tfrac T2\mathrm{tr}\Big\{R^{-1}\frac{\partial R}{\partial\theta_i}R^{-1}\big[D-BH^\top-HB^\top+H\Sigma H^\top\big]\Big\}\\
&-\tfrac T2\mathrm{tr}\Big\{R^{-1}\Big[-B\frac{\partial H^\top}{\partial\theta_i}-\frac{\partial H}{\partial\theta_i}B^\top+\frac{\partial H}{\partial\theta_i}\Sigma H^\top+H\Sigma\frac{\partial H^\top}{\partial\theta_i}\Big]\Big\}.\end{aligned}\tag{A.70}$$
(p. 374)

*Intuition note.* Theorem A.10 differentiates every step of the filter (a forward sensitivity recursion). Theorem A.11 instead uses Fisher's identity with the expression for $\mathcal Q$ from Theorem 16.11 (not defined here); the text presents it as another way to compute the same derivative (p. 373).

### A.11 Parameter derivatives for the Gaussian filter (pp. 374–378)
Models: $x_k=f(x_{k-1},\theta)+q_{k-1}$, $y_k=h(x_k,\theta)+r_k$ (A.71). Rewrite expectations over a unit Gaussian:
$$m^-_k(\theta)=\int f(x_{k-1},\theta)\mathrm N(x_{k-1}\mid m_{k-1},P_{k-1})dx_{k-1}=\int f\big(m_{k-1}+\sqrt{P_{k-1}}\,\xi,\theta\big)\mathrm N(\xi\mid0,I)d\xi.\tag{A.72}$$
Shorthand (added): $\hat x=m_{k-1}+\sqrt{P_{k-1}}\xi$, $\mathcal D=\partial m_{k-1}/\partial\theta_i+(\partial\sqrt{P_{k-1}}/\partial\theta_i)\xi$, and $J_f=F_x(\hat x,\theta)\mathcal D+\partial f/\partial\theta_i(\hat x,\theta)$, where $F_x$ is the Jacobian of $x\mapsto f(x,\theta)$. Then $\partial m^-_k/\partial\theta_i=\int J_f\,\mathrm N(\xi\mid0,I)d\xi$ (p. 375). With a Cholesky-based square root, $\partial\sqrt P/\partial\theta_i$ comes from Algorithm A.7 or Theorem A.8. For sigma points with weights $W_j$ and unit points $\xi^{(j)}$,
$$\frac{\partial m^-_k}{\partial\theta_i}\approx\sum_jW_j\Big[F_x(\cdot)\Big(\frac{\partial m_{k-1}}{\partial\theta_i}+\frac{\partial\sqrt{P_{k-1}}}{\partial\theta_i}\xi^{(j)}\Big)+\frac{\partial f}{\partial\theta_i}(\cdot)\Big],\tag{A.73}$$
with $(\cdot)=(m_{k-1}+\sqrt{P_{k-1}}\xi^{(j)},\theta)$. This is exactly the derivative of the sigma-point approximation to $m_k^-(\theta)$ (p. 375).

**Algorithm A.12.** The energy recursion has the same form as (A.66), with "$\simeq$":
$$\frac{\partial\varphi_k}{\partial\theta_i}\simeq\frac{\partial\varphi_{k-1}}{\partial\theta_i}+\tfrac12\mathrm{tr}\Big(S_k^{-1}\frac{\partial S_k}{\partial\theta_i}\Big)+v_k^\top S_k^{-1}\frac{\partial v_k}{\partial\theta_i}-\tfrac12v_k^\top S_k^{-1}\frac{\partial S_k}{\partial\theta_i}S_k^{-1}v_k.\tag{A.74}$$
Prediction derivatives (A.75), with $\mathrm d\xi$-integrals against $\mathrm N(\xi\mid0,I)$:
$$\frac{\partial m^-_k}{\partial\theta_i}=\int J_f\,d\xi,\qquad
\frac{\partial P^-_k}{\partial\theta_i}=\int\Big[J_f-\frac{\partial m^-_k}{\partial\theta_i}\Big]\big[f(\hat x,\theta)-m^-_k\big]^\top d\xi+\int\big[f(\hat x,\theta)-m^-_k\big]\Big[J_f-\frac{\partial m^-_k}{\partial\theta_i}\Big]^\top d\xi+\frac{\partial Q_{k-1}}{\partial\theta_i}.$$
Update derivatives (A.76): with $\hat x^-=m^-_k+\sqrt{P^-_k}\xi$, $J_h=H_x(\hat x^-,\theta)\big(\partial m^-_k/\partial\theta_i+(\partial\sqrt{P_k^-}/\partial\theta_i)\xi\big)+\partial h/\partial\theta_i(\hat x^-,\theta)$ ($H_x$ the Jacobian of $x\mapsto h(x,\theta)$):
$$\begin{aligned}\frac{\partial\mu_k}{\partial\theta_i}&=\int J_h\,d\xi,\qquad\frac{\partial v_k}{\partial\theta_i}=-\frac{\partial\mu_k}{\partial\theta_i},\\
\frac{\partial S_k}{\partial\theta_i}&=\int\Big[J_h-\frac{\partial\mu_k}{\partial\theta_i}\Big][h(\hat x^-,\theta)-\mu_k]^\top d\xi+\int[h(\hat x^-,\theta)-\mu_k]\Big[J_h-\frac{\partial\mu_k}{\partial\theta_i}\Big]^\top d\xi+\frac{\partial R_k}{\partial\theta_i},\\
\frac{\partial C_k}{\partial\theta_i}&=\int\Big\{\frac{\partial\sqrt{P^-_k}}{\partial\theta_i}\xi\,[h(\hat x^-,\theta)-\mu_k]^\top+\sqrt{P^-_k}\xi\Big[J_h-\frac{\partial\mu_k}{\partial\theta_i}\Big]^\top\Big\}d\xi,\\
\frac{\partial K_k}{\partial\theta_i}&=\frac{\partial C_k}{\partial\theta_i}S_k^{-1}-C_kS_k^{-1}\frac{\partial S_k}{\partial\theta_i}S_k^{-1},\end{aligned}$$
and $\partial m_k/\partial\theta_i$, $\partial P_k/\partial\theta_i$ as in (A.68) (with $\partial m_k^-,\partial P_k^-$ from (A.75)). Here $C_k$ is the cross-covariance of Algorithm 16.14 (not defined here). Sigma-point versions follow by approximating the integrals as in (A.73), and the result is the exact derivative of the sigma-point-based energy function (pp. 376–377).

In the original variable, the predicted-mean derivative is
$$\frac{\partial m^-_k}{\partial\theta_i}=\int\Big[F_x(x_{k-1},\theta)\,g(x_{k-1},\theta)+\frac{\partial f(x_{k-1},\theta)}{\partial\theta_i}\Big]\mathrm N(x_{k-1}\mid m_{k-1},P_{k-1})dx_{k-1},\tag{A.77}$$
$$g(x_{k-1},\theta)=\frac{\partial m_{k-1}}{\partial\theta_i}+\frac{\partial\sqrt{P_{k-1}}}{\partial\theta_i}\big(\sqrt{P_{k-1}}\big)^{-1}(x_{k-1}-m_{k-1}).\tag{A.78}$$
The full set is left to the reader (p. 378).

*Intuition note.* Writing the state as mean plus root-covariance times a fixed standard-normal $\xi$ moves all parameter dependence out of the integration weight into the integrand. Then you can differentiate under the integral and reuse the same quadrature rule.

## Toy example (ours)
Scalar case of A.1–A.2: $x\sim\mathrm N(1,4)$, $y\mid x\sim\mathrm N(2x,1)$ (so $m=1,P=4,H=2,u=0,R=1$).
- Lemma A.2: joint mean $(1,\;Hm=2)$; covariance entries $P=4$, $PH=8$, $HPH+R=2\cdot4\cdot2+1=17$. So $y\sim\mathrm N(2,17)$.
- Observe $y=4$. Lemma A.3 with $a=1,A=4,C=8,b=2,B=17$: mean $=1+\frac{8}{17}(4-2)=\frac{33}{17}$; variance $=4-\frac{8\cdot8}{17}=\frac{4}{17}$.
- Check (A.8): $(P^{-1}+HR^{-1}H)^{-1}=(\tfrac14+4)^{-1}=\tfrac{4}{17}$ ✓, and $P-PH(R+HPH)^{-1}HP=4-\tfrac{64}{17}=\tfrac{4}{17}$ ✓.
- Check (A.9): $\tfrac4{17}\cdot2\cdot1=\tfrac8{17}$ equals $PH(R+HPH)^{-1}=\tfrac8{17}$ ✓. This is the gain used in the mean: $\frac{8}{17}$.

## Concepts
- [[gaussian-conditioning]] (new) — closed-form conditional mean/covariance of a joint Gaussian, Lemma A.3 (p. 356)
- [[matrix-inversion-lemma]] (new) — identities (A.8)–(A.9) from block inversion; such formulas are sometimes useful in deriving Gaussian conditioning and Kalman filtering/smoothing equations (pp. 356–357)
- [[cholesky-factor]] (new) — lower triangular $A$ with $P=AA^\top$; derivative via $\Phi$ (p. 357)
- [[affine-sde-solution]] (new) — exact $x(t+\tau)\mid x(t)$ Gaussian for $\dot x=Fx+b+Lw$ (p. 359)
- [[state-space-model]] — linear dynamics $Fx+b+Lw$ and measurement $Hx+r$, as used here (pp. 359, 371)
- [[linearization]] — Jacobian $A_x(m)$ drives the covariance ODE (A.33) (p. 363)
- [[statistical-linear-regression]] (new) — linear-Gaussian approximation built from $\mu$, $P^{xx}$, $P^x$ (p. 367)
- [[energy-function]] (new) — negative log unnormalized posterior of parameters, $\varphi_k(\theta)$ (p. 371)
- [[sensitivity-equations]] (new) — recursions for $\partial/\partial\theta_i$ of filter quantities (p. 372)
- [[kalman-filter]] — predict/update recursions differentiated in A.10 (p. 372)
- [[kalman-gain]] — $K_k$; derivative given in (A.68) (p. 373)

## Canonical instances
- [[bicycle-model]] — mean ODE (A.34) with closed-form discretization (A.36) (p. 363)
- [[polar-coordinated-turn-model]] — mean discretization (A.39)–(A.40) and $Q_{k-1}$ in (A.48) (pp. 364–367)
- [[linear-gaussian-parametric-model]] — model (A.65) whose energy gradient is Theorem A.10 (p. 371)

## Bridges (candidates)
- [same-math] Lemma A.9 variation-of-constants solution ↔ control-theory: solution of $\dot x=Ax+Bu$ via the matrix exponential, with noise integral added — same formula with $b$ as input.
- [same-math] Matrix inversion lemma (A.9) ↔ control-theory: gain of the Kalman filter in two equivalent forms — the same algebraic identity.
- [same-math] Jacobian $A_x(m)$ in (A.33) ↔ control-theory: linearization about an equilibrium or trajectory — same Jacobian linearization.
- [structural-analogy] $\partial P/\partial t=A_xP+PA_x^\top+LQ^cL^\top$ ↔ control-theory: Lyapunov-type covariance propagation — same shape, different setting.

## Questions this raises
- When is the sigma-point derivative of A.11 also a good approximation to the derivative of the exact (non-Gaussian) filter's energy?
- How does the numerical cost of the sensitivity recursions (A.66–A.68) scale with the number of parameters compared with Fisher's identity (A.69–A.70)?
- What happens to (A.39)–(A.40) as $\omega_{k-1}\to0$, and how is that handled in practice?
- How accurate is the constant-gradient $Q_{k-1}$ of (A.48) when $A_x$ changes within a step?

## Reading notes
- Printed page = pdf page − 30 (labels give printed numbers directly).
- Text layer garbles all Greek and operator symbols; equations here were checked against the page images.
- (A.25): the source prints $b(t)$ inside the integrand ($b(t)+Lw(v)$); from context it should be $b(v)$, consistent with (A.18).
- (A.29): the source prints $\lim_{h\to\infty}$; the surrounding text ("terms that go to zero faster than $h$ as $h\to0$") requires $h\to0$.
- (A.48): entry (4,2) shows $v^4/8$ where $\tau^4/8$ is expected; the matrix is labelled $P(\tau+t_{k-1})$ but the text says it gives $Q_{k-1}$.
- (A.39) uses $\omega(t_{k-1})$ and $\omega_{k-1}$ interchangeably.
- Symbols from Theorems 16.9/16.11 and Algorithm 16.14 ($v_k,S_k,C_k,\Sigma,\Phi,B,D$, etc.) and $L$ from (4.43) are not defined in these pages.
- The closing remark on p. 378 leaves the full derivation as a reader exercise; no numbered exercises appear.
