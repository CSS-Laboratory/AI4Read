---
id: deisenroth-2020-mml/ch09-linear
work: deisenroth-2020-mml
unit: "9 Linear Regression"
pages: 289–316
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
# Linear Regression (Deisenroth, Faisal & Ong, ch. 9)

## L0 — One line
Linear regression with Gaussian noise is least squares seen as maximum likelihood, and adding a Gaussian prior gives regularization (MAP, which maximizes the posterior over the parameters) and then a full Bayesian treatment, all in closed form; geometrically, maximum likelihood is an orthogonal projection.

## L1 — The gist (≤ 120 words)
How do we fit a function to noisy data so that it also predicts well on new inputs? The chapter models the noise as Gaussian and the function as linear in its parameters (features may be nonlinear). Maximum likelihood gives the least-squares solution $(\Phi^\top\Phi)^{-1}\Phi^\top y$ but can overfit. A Gaussian prior adds $\frac{\sigma^2}{b^2}I$ (MAP, equal to regularized least squares). Bayesian linear regression keeps a whole Gaussian posterior over parameters and so gives predictions with uncertainty. Geometrically, maximum likelihood projects $y$ orthogonally onto the span of the feature columns. This matters because regression is a fundamental problem in machine learning, and the chapter solves it by applying mathematical concepts from earlier chapters (p. 289).

**Prerequisites:** gradients and matrix calculus; Gaussian distributions (marginals, linear maps); Bayes' theorem; rank and invertibility; positive definite matrices; orthogonal projection.

## L2 — Key ideas
- Linear regression means "linear in the parameters": $y=\phi^\top(x)\theta+\epsilon$ with Gaussian noise. Nonlinear features $\phi$, such as polynomials, still fit this framework (pp. 291, 295).
- Maximum likelihood minimizes a squared error. It has the closed form $\theta_{ML}=(\Phi^\top\Phi)^{-1}\Phi^\top y$, which needs $\mathrm{rk}(\Phi)=K$ (pp. 294, 296–297).
- The ML noise variance is the mean squared residual (p. 298).
- Overfitting: training error never increases with polynomial degree, but test error eventually rises. In the example, the best test error is at $M=4$ (pp. 298–300).
- A Gaussian prior gives the MAP estimate (the parameters that maximize the posterior) $(\Phi^\top\Phi+\frac{\sigma^2}{b^2}I)^{-1}\Phi^\top y$. This equals regularized least squares with $\lambda=\sigma^2/b^2$. It can push the boundaries of overfitting but is not a general solution to it (pp. 301–303).
- Bayesian linear regression has a closed-form Gaussian posterior $\mathcal N(m_N,S_N)$, found by completing the square (rewriting a quadratic as a perfect square plus a constant) (Thm 9.1, pp. 306–308).
- Posterior predictive variance is parameter uncertainty plus noise $\sigma^2$. Its mean equals the MAP prediction (pp. 308–309).
- The marginal likelihood (the likelihood averaged over the prior) is also Gaussian in $y$, with mean $Xm_0$ and covariance $XS_0X^\top+\sigma^2I$ (pp. 312–313).
- Maximum likelihood is an orthogonal projection of $y$ onto the column space of $\Phi$. With orthonormal features it becomes a sum of one-dimensional projections (pp. 313–314).
- Extensions: generalized linear models (a smooth function applied to a linear model), deep networks, Gaussian processes (distributions placed directly on functions), and sparsity-inducing priors (a Laplace prior is equivalent to L1-regularized regression, LASSO) (pp. 315–316).

## L3 — Walkthrough

### Chapter introduction (pp. 289–290)
- **Regression** means finding $f:\mathbb R^D\to\mathbb R$ from noisy observations $y_n=f(x_n)+\epsilon$. Here $\epsilon$ is i.i.d. zero-mean Gaussian noise. The goal is a function that also generalizes to new inputs (p. 289).
- The author lists five problems: choice of model and parametrization; finding good parameters (loss functions and optimization); overfitting and model selection; the link between loss functions and parameter priors; and uncertainty modeling (p. 290).
- Plan: maximum likelihood and MAP, then generalization error and overfitting, then Bayesian linear regression (p. 290).

### 9.1 Problem Formulation (pp. 291–292)
- Likelihood: $p(y\mid x)=\mathcal N(y\mid f(x),\sigma^2)$ (9.1), i.e. $y=f(x)+\epsilon$, $\epsilon\sim\mathcal N(0,\sigma^2)$ (9.2) (p. 291).
- The chapter studies *parametric* models: a parametrized function with parameters $\theta$ to be learned. $\sigma^2$ is assumed known for now (p. 291).
- Linear regression: $\theta$ enters linearly.
$$p(y\mid x,\theta)=\mathcal N(y\mid x^\top\theta,\sigma^2)\tag{9.3}$$
$$\iff y=x^\top\theta+\epsilon,\quad\epsilon\sim\mathcal N(0,\sigma^2)\tag{9.4}$$
with $\theta\in\mathbb R^D$. This class contains straight lines through the origin (p. 291).
- The only source of uncertainty in (9.3) is observation noise, since $x$ and $\theta$ are known. Without noise the relation would be deterministic (a Dirac delta) (p. 291).
- Example 9.1: for $x,\theta\in\mathbb R$, $\theta$ is the slope of the line (p. 291).
- "Linear regression" means linear in the parameters. A model $y=\phi^\top(x)\theta$ with nonlinear $\phi$ is still linear regression. A "feature" is a representation $\phi(x)$ of the input (pp. 291–292).

### 9.2 Parameter Estimation (p. 292)
- Training set $\mathcal D=\{(x_1,y_1),\dots,(x_N,y_N)\}$. The $y_n$ are conditionally independent given their inputs, so the likelihood factorizes:
$$p(\mathcal Y\mid\mathcal X,\theta)=\prod_{n=1}^N p(y_n\mid x_n,\theta)=\prod_{n=1}^N\mathcal N(y_n\mid x_n^\top\theta,\sigma^2)\tag{9.5}$$
- Once an estimate $\theta^*$ is found, the prediction at a test input $x_*$ is $p(y_*\mid x_*,\theta^*)=\mathcal N(y_*\mid x_*^\top\theta^*,\sigma^2)$ (9.6) (p. 292).

#### 9.2.1 Maximum Likelihood Estimation (pp. 293–297)
- $\theta_{ML}\in\arg\max_\theta p(\mathcal Y\mid\mathcal X,\theta)$ (9.7). The likelihood is a normalized distribution in $y$, but it is not a probability distribution in $\theta$ (it does not integrate to 1 and may not even be integrable) (p. 293).
- In practice we minimize the negative log-likelihood. Reasons: the product of $N$ probabilities can underflow numerically, and the log turns the product into a sum, so the gradient is a sum of individual gradients (p. 293).
- By independence, $-\log p(\mathcal Y\mid\mathcal X,\theta)=-\sum_n\log p(y_n\mid x_n,\theta)$ (9.8). Each term is $\log p(y_n\mid x_n,\theta)=-\frac1{2\sigma^2}(y_n-x_n^\top\theta)^2+\text{const}$ (9.9) (p. 293).
- Dropping constants, with design matrix $X=[x_1,\dots,x_N]^\top\in\mathbb R^{N\times D}$ and $y\in\mathbb R^N$:
$$\mathcal L(\theta):=\frac1{2\sigma^2}\sum_{n=1}^N(y_n-x_n^\top\theta)^2\tag{9.10a}$$
$$=\frac1{2\sigma^2}(y-X\theta)^\top(y-X\theta)=\frac1{2\sigma^2}\|y-X\theta\|^2\tag{9.10b}$$
(p. 294). $\mathcal L$ is quadratic in $\theta$, so a unique global solution can be found by setting the gradient to zero (p. 294).
- Gradient (shapes: $\frac{d\mathcal L}{d\theta}\in\mathbb R^{1\times D}$):
$$\frac{d\mathcal L}{d\theta}=\frac{d}{d\theta}\Big(\frac1{2\sigma^2}(y-X\theta)^\top(y-X\theta)\Big)\tag{9.11a}$$
$$=\frac1{2\sigma^2}\frac{d}{d\theta}\big(y^\top y-2y^\top X\theta+\theta^\top X^\top X\theta\big)\tag{9.11b}$$
$$=\frac1{\sigma^2}(-y^\top X+\theta^\top X^\top X)\in\mathbb R^{1\times D}\tag{9.11c}$$
- Setting it to $0^\top$ (necessary optimality condition):
$$\tfrac{d\mathcal L}{d\theta}=0^\top\iff\theta_{ML}^\top X^\top X=y^\top X\tag{9.12a}$$
$$\iff\theta_{ML}^\top=y^\top X(X^\top X)^{-1}\tag{9.12b}$$
$$\iff\theta_{ML}=(X^\top X)^{-1}X^\top y\tag{9.12c}$$
We may right-multiply by $(X^\top X)^{-1}$ because $X^\top X$ is positive definite if $\mathrm{rk}(X)=D$. Ignoring duplicate data points, $\mathrm{rk}(X)=D$ if $N\ge D$ (p. 294).
- Remarks: the zero-gradient condition is necessary and sufficient, and the minimum is global because the Hessian is positive definite (the author prints it as $X^\top X\in\mathbb R^{D\times D}$). Also, (9.12c) amounts to solving $A\theta=b$ with $A=X^\top X$, $b=X^\top y$ (p. 294).
- *Intuition note:* For Gaussian noise, "most likely parameters" means "smallest sum of squared errors". The answer solves the linear system $X^\top X\theta=X^\top y$ (the transpose of (9.12a)).
- Example 9.2: fitting $f(x)=\theta x$ to the data of Fig. 9.2(b) with (9.12c) gives the line in Fig. 9.2(c) (p. 295).

**Maximum likelihood with features (pp. 295–297).**
- Replace $x$ by $\phi(x)\in\mathbb R^K$:
$$p(y\mid x,\theta)=\mathcal N(y\mid\phi^\top(x)\theta,\sigma^2)\iff y=\phi^\top(x)\theta+\epsilon=\sum_{k=0}^{K-1}\theta_k\phi_k(x)+\epsilon\tag{9.13}$$
Parameters still appear only linearly (p. 295).
- Example 9.3 (polynomial regression): $\phi(x)=[1,x,x^2,\dots,x^{K-1}]^\top$ (9.14). This lifts the 1-D input into $K$-dim feature space and models polynomials of degree $\le K-1$: $f(x)=\sum_{k=0}^{K-1}\theta_kx^k=\phi^\top(x)\theta$ (9.15) (pp. 295–296).
- Feature (design) matrix $\Phi\in\mathbb R^{N\times K}$, $\Phi_{ij}=\phi_j(x_i)$ (9.16), rows $\phi^\top(x_n)$. Example 9.4: for a second-order polynomial the rows are $[1,\;x_n,\;x_n^2]$ (9.17) (p. 296).
- The negative log-likelihood is $\frac1{2\sigma^2}(y-\Phi\theta)^\top(y-\Phi\theta)+\text{const}$ (9.18). This is (9.10b) with $X$ replaced by $\Phi$, so
$$\theta_{ML}=(\Phi^\top\Phi)^{-1}\Phi^\top y\tag{9.19}$$
(p. 296). $\Phi^\top\Phi\in\mathbb R^{K\times K}$ is invertible if and only if $\mathrm{rk}(\Phi)=K$ (p. 297).
- *Intuition note:* Replacing $x$ by $\phi(x)$ changes the columns of the matrix but not the algebra. The curve can bend, yet the problem stays a linear least-squares problem.
- Example 9.5: $N=10$ points, $x_n\sim\mathcal U[-5,5]$, $y_n=-\sin(x_n/5)+\cos(x_n)+\epsilon$, $\epsilon\sim\mathcal N(0,0.2^2)$. A degree-4 polynomial is fitted with (9.19) (Fig. 9.4) (p. 297).

**Estimating the noise variance (pp. 297–298).**
- Log-likelihood in $\sigma^2$, with $s:=\sum_n(y_n-\phi^\top(x_n)\theta)^2$:
$$\log p(\mathcal Y\mid\mathcal X,\theta,\sigma^2)=\sum_n\log\mathcal N(y_n\mid\phi^\top(x_n)\theta,\sigma^2)\tag{9.20a}$$
$$=\sum_n\Big(-\tfrac12\log(2\pi)-\tfrac12\log\sigma^2-\tfrac1{2\sigma^2}(y_n-\phi^\top(x_n)\theta)^2\Big)\tag{9.20b}$$
$$=-\tfrac N2\log\sigma^2-\tfrac1{2\sigma^2}s+\text{const}\tag{9.20c}$$
- Derivative set to 0:
$$\frac{\partial\log p}{\partial\sigma^2}=-\frac N{2\sigma^2}+\frac1{2\sigma^4}s=0\iff\frac N{2\sigma^2}=\frac s{2\sigma^4}\tag{9.21}$$
$$\sigma^2_{ML}=\frac sN=\frac1N\sum_{n=1}^N(y_n-\phi^\top(x_n)\theta)^2\tag{9.22}$$
So $\sigma^2_{ML}$ is the empirical mean of squared distances between noise-free values $\phi^\top(x_n)\theta$ and observations $y_n$ (p. 298).

#### 9.2.2 Overfitting in Linear Regression (pp. 298–300)
- Quality can be measured by the negative log-likelihood, or by the squared error $\|y-\Phi\theta\|^2$ (since $\sigma^2$ is not a free model parameter, $1/\sigma^2$ can be ignored). Often the root mean square error is used:
$$\mathrm{RMSE}=\sqrt{\tfrac1N\|y-\Phi\theta\|^2}=\sqrt{\tfrac1N\sum_n(y_n-\phi^\top(x_n)\theta)^2}\tag{9.23}$$
It (a) allows comparison across dataset sizes and (b) has the same units as $y$. Example: for house prices in EUR, RMSE is in EUR but squared error is in EUR² (p. 298).
- Model selection: choose the polynomial degree $M$ by brute-force search. For training size $N$, testing $0\le M\le N-1$ is sufficient. For $M<N$ the ML estimator is unique. For $M\ge N$ the system is underdetermined, $\Phi^\top\Phi$ is no longer invertible, and there are infinitely many ML estimators (pp. 298–299).
- Fig. 9.5 (same data as Fig. 9.4(a), $N=10$):
  - Low degrees ($M=0,1$) fit poorly.
  - $M=3,\dots,6$ look plausible.
  - At $M=N-1=9$ the polynomial passes through every point but oscillates wildly: overfitting (p. 299).
- A separate test set of 200 points (same generation procedure; test inputs on a linear grid of 200 points in $[-5,5]$) is used for the RMSE of Fig. 9.6. Test error first decreases. It is relatively low and roughly constant from degree 4 up to degree 5, and rises significantly from degree 6 onward. The training error never increases with degree. In this example the smallest test error is at $M=4$ (pp. 299–300).
- *Intuition note:* In the polynomial example, a higher degree never makes the training error worse, but the test error eventually rises, so a good fit to the training data does not guarantee good predictions on new points (p. 300).

#### 9.2.3 Maximum A Posteriori Estimation (pp. 300–302)
- Overfitting is often accompanied by large parameter magnitudes. A prior $p(\theta)$ encodes plausible parameter values before seeing data. Example: $\mathcal N(0,1)$ on one parameter expects values in $[-2,2]$ (two standard deviations) (p. 300).
- MAP maximizes the posterior, from Bayes' theorem:
$$p(\theta\mid\mathcal X,\mathcal Y)=\frac{p(\mathcal Y\mid\mathcal X,\theta)p(\theta)}{p(\mathcal Y\mid\mathcal X)}\tag{9.24}$$
$$\log p(\theta\mid\mathcal X,\mathcal Y)=\log p(\mathcal Y\mid\mathcal X,\theta)+\log p(\theta)+\text{const}\tag{9.25}$$
The MAP estimate is a "compromise" between the prior and the data-dependent likelihood (pp. 300–301).
- $\theta_{MAP}\in\arg\min_\theta\{-\log p(\mathcal Y\mid\mathcal X,\theta)-\log p(\theta)\}$ (9.26). The gradient (9.27) is the negative-log-likelihood gradient (9.11c) plus $-\frac{d\log p(\theta)}{d\theta}$ (p. 301).
- With conjugate prior $p(\theta)=\mathcal N(0,b^2I)$:
$$-\log p(\theta\mid\mathcal X,\mathcal Y)=\frac1{2\sigma^2}(y-\Phi\theta)^\top(y-\Phi\theta)+\frac1{2b^2}\theta^\top\theta+\text{const}\tag{9.28}$$
$$-\frac{d\log p(\theta\mid\mathcal X,\mathcal Y)}{d\theta}=\frac1{\sigma^2}(\theta^\top\Phi^\top\Phi-y^\top\Phi)+\frac1{b^2}\theta^\top\tag{9.29}$$
- Set to $0^\top$ and solve:
$$\tfrac1{\sigma^2}(\theta^\top\Phi^\top\Phi-y^\top\Phi)+\tfrac1{b^2}\theta^\top=0^\top\tag{9.30a}$$
$$\iff\theta^\top\big(\tfrac1{\sigma^2}\Phi^\top\Phi+\tfrac1{b^2}I\big)-\tfrac1{\sigma^2}y^\top\Phi=0^\top\tag{9.30b}$$
$$\iff\theta^\top\big(\Phi^\top\Phi+\tfrac{\sigma^2}{b^2}I\big)=y^\top\Phi\tag{9.30c}$$
$$\iff\theta^\top=y^\top\Phi\big(\Phi^\top\Phi+\tfrac{\sigma^2}{b^2}I\big)^{-1}\tag{9.30d}$$
Transposing both sides:
$$\theta_{MAP}=\big(\Phi^\top\Phi+\tfrac{\sigma^2}{b^2}I\big)^{-1}\Phi^\top y\tag{9.31}$$
(p. 301).
- Compared with (9.19), the only difference is the extra term $\frac{\sigma^2}{b^2}I$. $\Phi^\top\Phi$ is symmetric positive semidefinite, and adding this term makes the matrix symmetric and strictly positive definite. So its inverse exists and the MAP estimate is the unique solution of a linear system. The term also reflects the regularizer (pp. 301–302).
- *Intuition note:* (Our reading of (9.31).) The zero-mean prior discourages large parameter values. The added term $\frac{\sigma^2}{b^2}I$ is larger when $\sigma^2$ is larger or the prior is tighter (small $b^2$).
- Example 9.6: prior $\mathcal N(0,I)$ on the polynomial parameters, with MLE and MAP compared at degrees 6 and 8 (Fig. 9.7). The prior does not matter much for low degree but keeps the function relatively smooth for higher degree. MAP "can push the boundaries of overfitting" but is not a general solution, so a more principled approach is needed (p. 302).

#### 9.2.4 MAP Estimation as Regularization (pp. 302–303)
- Regularized least squares:
$$\|y-\Phi\theta\|^2+\lambda\|\theta\|_2^2\tag{9.32}$$
The first term is the data-fit (misfit) term, proportional to the negative log-likelihood (9.10b). The second is the regularizer, and $\lambda\ge0$ is the regularization parameter (p. 302).
- Remark: any $p$-norm may replace the Euclidean norm. In practice smaller $p$ leads to sparser solutions (many $\theta_d=0$), which is useful for variable selection. For $p=1$ this is LASSO (p. 303).
- With $p(\theta)=\mathcal N(0,b^2I)$: $-\log p(\theta)=\frac1{2b^2}\|\theta\|_2^2+\text{const}$ (9.33). For $\lambda=\frac1{2b^2}$ the regularization term and the negative log prior are identical (p. 303).
- Minimizing (9.32) gives
$$\theta_{RLS}=(\Phi^\top\Phi+\lambda I)^{-1}\Phi^\top y\tag{9.34}$$
which is identical to the MAP estimate (9.31) for $\lambda=\sigma^2/b^2$ (p. 303).
- (added step) Multiplying (9.28) by $2\sigma^2$ gives $\|y-\Phi\theta\|^2+\frac{\sigma^2}{b^2}\|\theta\|^2$ plus a constant. This is (9.32) with $\lambda=\sigma^2/b^2$; the two values of $\lambda$ above differ because the data term in (9.32) is not divided by $2\sigma^2$.
- Both ML and MAP give *point estimates* (single parameter values) and can overfit. The next section keeps a distribution over parameters instead (p. 303).

### 9.3 Bayesian Linear Regression (p. 303 onward)
Bayesian linear regression does not compute a point estimate. It uses the full posterior over parameters when predicting, i.e. it averages over all plausible parameter settings (p. 303).

#### 9.3.1 Model (p. 304)
$$\text{prior: }p(\theta)=\mathcal N(m_0,S_0),\qquad\text{likelihood: }p(y\mid x,\theta)=\mathcal N(y\mid\phi^\top(x)\theta,\sigma^2)\tag{9.35}$$
$\theta$ is now a random variable. The joint model is $p(y,\theta\mid x)=p(y\mid x,\theta)p(\theta)$ (9.36) (p. 304).

#### 9.3.2 Prior Predictions (pp. 304–305)
- Prediction at $x_*$ integrates out $\theta$ (no training data needed):
$$p(y_*\mid x_*)=\int p(y_*\mid x_*,\theta)p(\theta)\,d\theta=\mathbb E_\theta[p(y_*\mid x_*,\theta)]\tag{9.37}$$
- With the Gaussian prior, the predictive distribution is Gaussian:
$$p(y_*\mid x_*)=\mathcal N\big(\phi^\top(x_*)m_0,\;\phi^\top(x_*)S_0\phi(x_*)+\sigma^2\big)\tag{9.38}$$
The author gives three reasons. (i) Conjugacy and the marginalization property of Gaussians give a Gaussian. (ii) The noise is independent, so $\mathbb V[y_*]=\mathbb V_\theta[\phi^\top(x_*)\theta]+\mathbb V_\epsilon[\epsilon]$ (9.39). (iii) $y_*$ is a linear transformation of $\theta$, so rules (6.50), (6.51) apply. The term $\phi^\top S_0\phi$ is parameter uncertainty; $\sigma^2$ is measurement noise (pp. 304–305).
- For noise-free $f(x_*)=\phi^\top(x_*)\theta$: $p(f(x_*))=\mathcal N(\phi^\top(x_*)m_0,\phi^\top(x_*)S_0\phi(x_*))$ (9.40), which omits $\sigma^2$ (p. 305).
- The parameter distribution induces a distribution over functions: each sample $\theta_i$ gives a function $f_i(\cdot)=\theta_i^\top\phi(\cdot)$ (p. 305).
- Example 9.7: degree-5 polynomials, prior $\mathcal N(0,\frac14I)$, 200 input locations in $[-5,5]$. Fig. 9.9 shows the induced prior over functions with 67% and 95% bounds and sample functions. The uncertainty there is solely parameter uncertainty (noise-free predictive (9.40)) (p. 305).

#### 9.3.3 Posterior Distribution (pp. 306–308)
- Posterior (9.41) $=\frac{p(\mathcal Y\mid\mathcal X,\theta)p(\theta)}{p(\mathcal Y\mid\mathcal X)}$. The denominator is the marginal likelihood (evidence)
$$p(\mathcal Y\mid\mathcal X)=\int p(\mathcal Y\mid\mathcal X,\theta)p(\theta)d\theta=\mathbb E_\theta[p(\mathcal Y\mid\mathcal X,\theta)]\tag{9.42}$$
It does not depend on $\theta$ and normalizes the posterior (p. 306).
- **Theorem 9.1 (Parameter posterior).** In model (9.35) the posterior is Gaussian:
$$p(\theta\mid\mathcal X,\mathcal Y)=\mathcal N(\theta\mid m_N,S_N)\tag{9.43a}$$
$$S_N=(S_0^{-1}+\sigma^{-2}\Phi^\top\Phi)^{-1}\tag{9.43b}$$
$$m_N=S_N(S_0^{-1}m_0+\sigma^{-2}\Phi^\top y)\tag{9.43c}$$
(added step) Shapes: $S_N\in\mathbb R^{K\times K}$, $m_N\in\mathbb R^K$, following from $\Phi\in\mathbb R^{N\times K}$.
- *Proof.* Likelihood $p(\mathcal Y\mid\mathcal X,\theta)=\mathcal N(y\mid\Phi\theta,\sigma^2I)$ (9.44b), prior $\mathcal N(\theta\mid m_0,S_0)$ (9.44c). The posterior is proportional to their product, so work in log-space and complete the square (p. 306).
  - Sum of log-likelihood and log-prior:
$$-\tfrac12\big(\sigma^{-2}(y-\Phi\theta)^\top(y-\Phi\theta)+(\theta-m_0)^\top S_0^{-1}(\theta-m_0)\big)+\text{const}\tag{9.45}$$
  - Expand (9.46a): $-\frac12\big(\sigma^{-2}y^\top y-2\sigma^{-2}y^\top\Phi\theta+\theta^\top\sigma^{-2}\Phi^\top\Phi\theta+\theta^\top S_0^{-1}\theta-2m_0^\top S_0^{-1}\theta+m_0^\top S_0^{-1}m_0\big)$. Collect terms:
$$=-\tfrac12\Big(\theta^\top(\sigma^{-2}\Phi^\top\Phi+S_0^{-1})\theta-2(\sigma^{-2}\Phi^\top y+S_0^{-1}m_0)^\top\theta\Big)+\text{const}\tag{9.46b}$$
  - This is quadratic in $\theta$, so $p(\theta\mid\mathcal X,\mathcal Y)\propto\exp\big(-\frac12(\theta^\top(\sigma^{-2}\Phi^\top\Phi+S_0^{-1})\theta-2(\sigma^{-2}\Phi^\top y+S_0^{-1}m_0)^\top\theta)\big)$ (9.47) is Gaussian.
  - The desired log-density is
$$\log\mathcal N(\theta\mid m_N,S_N)=-\tfrac12(\theta-m_N)^\top S_N^{-1}(\theta-m_N)+\text{const}=-\tfrac12\big(\theta^\top S_N^{-1}\theta-2m_N^\top S_N^{-1}\theta+m_N^\top S_N^{-1}m_N\big)\tag{9.48}$$
  - Matching the quadratic terms gives $S_N^{-1}=\Phi^\top\sigma^{-2}I\Phi+S_0^{-1}$ (9.49a), i.e. (9.43b). Matching the linear terms gives $m_N^\top S_N^{-1}=(\sigma^{-2}\Phi^\top y+S_0^{-1}m_0)^\top$ (9.50a), i.e. (9.43c). $\square$
- Since the posterior is Gaussian, $\theta_{MAP}=m_N$ (margin note, p. 307).
- *Intuition note:* The posterior precision $S_N^{-1}$ is the prior precision plus data precision $\sigma^{-2}\Phi^\top\Phi$. Its mean $m_N$ is the MAP estimate (margin note, p. 307).
- **Remark (completing the squares, p. 308).** Given $x^\top Ax-2a^\top x+\text{const}_1$ (9.51) with $A$ symmetric positive definite, the form $(x-\mu)^\top\Sigma(x-\mu)+\text{const}_2$ (9.52) is obtained by
$$\Sigma:=A,\quad\mu:=\Sigma^{-1}a,\quad\text{const}_2=\text{const}_1-\mu^\top\Sigma\mu\tag{9.53–9.54}$$
Here $A=\sigma^{-2}\Phi^\top\Phi+S_0^{-1}$ (9.55) and $a=\sigma^{-2}\Phi^\top y+S_0^{-1}m_0$ (9.56) (p. 308).

#### 9.3.4 Posterior Predictions (pp. 308–311)
- Same reasoning as in 9.3.2 with the posterior in place of the prior:
$$p(y_*\mid\mathcal X,\mathcal Y,x_*)=\int\mathcal N(y_*\mid\phi^\top(x_*)\theta,\sigma^2)\,\mathcal N(\theta\mid m_N,S_N)\,d\theta=\mathcal N\big(y_*\mid\phi^\top(x_*)m_N,\;\phi^\top(x_*)S_N\phi(x_*)+\sigma^2\big)\tag{9.57}$$
The term $\phi^\top S_N\phi$ is posterior parameter uncertainty. $S_N$ depends on the training inputs through $\Phi$. The predictive mean coincides with predictions from $\theta_{MAP}$ (p. 308).
- Remark: (9.57a) can be written as $\mathbb E_{\theta\mid\mathcal X,\mathcal Y}[p(y_*\mid x_*,\theta)]$. This resembles the marginal likelihood, but the marginal likelihood (i) concerns the training targets $y$ and (ii) averages over the prior, not the posterior (p. 309).
- Remark (noise-free values): $\mathbb E[f(x_*)\mid\mathcal X,\mathcal Y]=\phi^\top(x_*)m_N$ (9.58) and $\mathbb V_\theta[f(x_*)\mid\mathcal X,\mathcal Y]=\phi^\top(x_*)S_N\phi(x_*)$ (9.59). The mean equals the noisy-prediction mean (noise has mean 0), and the variance differs by $\sigma^2$ (p. 309).
- Remark (distribution over functions): the mean function is $m_N^\top\phi(\cdot)$ and the marginal variance is $\phi^\top(\cdot)S_N\phi(\cdot)$ (p. 309).
- Example 9.8 (degree 5, prior $\mathcal N(0,\frac14I)$): Fig. 9.10 shows the posterior over functions with MLE, MAP (identical to the posterior mean function) and samples (p. 310). Fig. 9.11 shows degrees $M=3,5,7$ (p. 311). For low-order polynomials the sampled functions are nearly identical. For higher order the parameters are not sufficiently constrained and the samples separate visually, with uncertainty growing especially at the boundaries (p. 310).
- For $M=7$ the MAP fit looks reasonable, but Bayesian linear regression additionally shows that the posterior uncertainty is huge. This can be critical in decision-making systems (e.g. reinforcement learning, robotics) (pp. 310–311).

#### 9.3.5 Computing the Marginal Likelihood (pp. 312–313)
- Generative process: $\theta\sim\mathcal N(m_0,S_0)$, $y_n\mid x_n,\theta\sim\mathcal N(x_n^\top\theta,\sigma^2)$ (9.60). Then
$$p(\mathcal Y\mid\mathcal X)=\int p(\mathcal Y\mid\mathcal X,\theta)p(\theta)d\theta=\int\mathcal N(y\mid X\theta,\sigma^2I)\,\mathcal N(\theta\mid m_0,S_0)\,d\theta\tag{9.61}$$
- Step 1 (Gaussian): the author argues from Section 6.5.2 that a product of Gaussians is an unnormalized Gaussian and a linear transformation of a Gaussian is Gaussian. After a linear transformation the integral is the normalizing constant of the product, which is Gaussian in shape (p. 312).
- Step 2 (moments):
$$\mathbb E[\mathcal Y\mid\mathcal X]=\mathbb E_{\theta,\epsilon}[X\theta+\epsilon]=X\mathbb E_\theta[\theta]=Xm_0\tag{9.62}$$
$$\mathrm{Cov}[\mathcal Y\mid\mathcal X]=\mathrm{Cov}_\theta[X\theta]+\sigma^2I=X\,\mathrm{Cov}_\theta[\theta]X^\top+\sigma^2I=XS_0X^\top+\sigma^2I\tag{9.63}$$
Hence
$$p(\mathcal Y\mid\mathcal X)=(2\pi)^{-N/2}\det(XS_0X^\top+\sigma^2I)^{-1/2}\exp\big(-\tfrac12(y-Xm_0)^\top(XS_0X^\top+\sigma^2I)^{-1}(y-Xm_0)\big)\tag{9.64a}$$
$$=\mathcal N(y\mid Xm_0,\;XS_0X^\top+\sigma^2I)\tag{9.64b}$$
(pp. 312–313). The author notes this form is unsurprising given its link to the posterior predictive (p. 313).

### 9.4 Maximum Likelihood as Orthogonal Projection (pp. 313–314)
- Simple setting: $y=x\theta+\epsilon$, $\epsilon\sim\mathcal N(0,\sigma^2)$ (9.65), lines through the origin. With $X=[x_1,\dots,x_N]^\top\in\mathbb R^N$ and $y\in\mathbb R^N$:
$$\theta_{ML}=(X^\top X)^{-1}X^\top y=\frac{X^\top y}{X^\top X}\in\mathbb R\tag{9.66}$$
$$X\theta_{ML}=X\frac{X^\top y}{X^\top X}=\frac{XX^\top}{X^\top X}y\tag{9.67}$$
This is the approximation of $y$ with minimum least-squares error (pp. 313–314).
- Reading of (9.67): $\frac{XX^\top}{X^\top X}$ is the projection matrix onto the 1-D subspace of $\mathbb R^N$ spanned by $X$. $\theta_{ML}$ gives the coordinates of the projection, and $X\theta_{ML}$ is the orthogonal projection of $y$ onto this subspace (Section 3.8) (p. 314).
- General case, features $\phi(x)\in\mathbb R^K$: $y\approx\Phi\theta_{ML}$ (9.69), $\theta_{ML}=(\Phi^\top\Phi)^{-1}\Phi^\top y$ (9.70). This is a projection onto the $K$-dim subspace of $\mathbb R^N$ spanned by the columns of $\Phi$ (p. 314).
- If the feature functions are orthonormal, the columns of $\Phi$ form an orthonormal basis, $\Phi^\top\Phi=I$, and
$$\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y=\Phi\Phi^\top y=\Big(\sum_{k=1}^K\phi_k\phi_k^\top\Big)y\tag{9.71}$$
The ML projection is then the sum of projections onto the individual $\phi_k$, and the coupling between features disappears. The author notes that wavelets and Fourier bases are orthogonal basis functions (signal processing). For non-orthogonal but linearly independent features, Gram–Schmidt (Section 3.8.3) can convert them (pp. 314–315).
- *Intuition note:* The fitted values $\Phi\theta_{ML}$ are the point in the column space of $\Phi$ closest to $y$. Because the projection is orthogonal, the residual $y-\Phi\theta_{ML}$ is perpendicular to the column space (our reading; checked numerically in the toy example for $D=1$).

### 9.5 Further Reading (pp. 315–316)
- Non-Gaussian likelihoods: a Bernoulli likelihood for binary classification; Binomial or Poisson for count data. These fall under *generalized linear models* (GLMs): $y=\sigma(f(x))$ with $f(x)=\theta^\top\phi(x)$ and $\sigma$ smooth and invertible, possibly nonlinear. So the output is no longer linear in $\theta$. Logistic regression uses $\sigma(f)=\frac1{1+\exp(-f)}\in[0,1]$. $\sigma$ is the transfer or activation function, and its inverse is the canonical link function (p. 315).
- GLM $y=\sigma(Ax+b)$ is a single-layer network. Composition $x_{k+1}=f_k(x_k)$, $f_k(x_k)=\sigma_k(A_kx_k+b_k)$ (9.72), $k=0,\dots,K-1$, gives a $K$-layer deep network. Networks are much more expressive, but maximum likelihood is then non-convex and full Bayesian marginalization is analytically intractable (pp. 315–316).
- Gaussian processes place a distribution directly on functions, using the kernel trick. The author says they are closely related to Bayesian linear regression and support vector regression and can be interpreted as a Bayesian neural network with one hidden layer with infinitely many units (p. 316).
- Sparsity: if $N\ll D$ the problem is underdetermined. A sparsity-inducing prior such as the Laplace prior is a stronger regularizer than the Gaussian and can improve accuracy and interpretability. Linear regression with a Laplace prior is equivalent to L1-regularized regression (LASSO). The Laplace distribution is sharply peaked at zero and puts more mass near zero than the Gaussian (p. 316).

## Toy example (our own; not from the text)
Model $y=\theta x+\epsilon$ (no features, $D=1$), $\sigma^2=1$. Data: $x=(1,2)$, $y=(1,3)$, so $X=\begin{bmatrix}1\\2\end{bmatrix}\in\mathbb R^{2\times1}$.

1. **ML.** $X^\top X=1+4=5$, $X^\top y=1\cdot1+2\cdot3=7$, so $\theta_{ML}=7/5=1.4$ by (9.12c).
2. **Projection check.** $X\theta_{ML}=(1.4,\,2.8)$. The residual is $y-X\theta_{ML}=(-0.4,\,0.2)$. Its dot product with $X$ is $-0.4\cdot1+0.2\cdot2=0$, so the residual is orthogonal to $X$, as in Section 9.4.
3. **MAP / ridge.** Prior $\mathcal N(0,b^2)$ with $b^2=1$, so $\sigma^2/b^2=1$. By (9.31), $\theta_{MAP}=(5+1)^{-1}\cdot7=7/6\approx1.167$, shrunk toward 0. Regularized LS (9.34) with $\lambda=1$ gives the same value.
4. **Posterior.** With $m_0=0$, $S_0=1$: $S_N=(1+5)^{-1}=1/6$ by (9.43b), and $m_N=\frac16(0+7)=7/6$ by (9.43c). So $m_N=\theta_{MAP}$.
5. **Predictions at $x_*=3$.**
   - Posterior predictive (9.57): mean $3\cdot7/6=3.5$; variance $3^2\cdot\frac16+1=1.5+1=2.5$. Noise-free variance (9.59) is $1.5$.
   - Prior predictive (9.38): mean $0$, variance $9\cdot1+1=10$. The data shrink the variance from 10 to 2.5.
6. **Marginal likelihood (9.64).** Mean $Xm_0=(0,0)$. Covariance $XS_0X^\top+\sigma^2I=\begin{bmatrix}1&2\\2&4\end{bmatrix}+I=\begin{bmatrix}2&2\\2&5\end{bmatrix}$, with determinant $10-4=6$. Its inverse is $\frac16\begin{bmatrix}5&-2\\-2&2\end{bmatrix}$. Then $C^{-1}y=\frac16(5-6,\,-2+6)=\frac16(-1,4)$ and $y^\top C^{-1}y=\frac16(-1+12)=11/6$. So $p(\mathcal Y\mid\mathcal X)=(2\pi)^{-1}\,6^{-1/2}\,e^{-11/12}$.

## Concepts
- [[linear-regression]] (new) — model $y=\phi^\top(x)\theta+\epsilon$, linear in the parameters, Gaussian noise (pp. 291, 295)
- [[likelihood]] (new) — density of the targets given inputs and parameters. It is normalized in $y$, not in $\theta$ (pp. 291, 293)
- [[maximum-likelihood-estimation]] (new) — choose $\theta$ maximizing $p(\mathcal Y\mid\mathcal X,\theta)$; here it equals least squares (p. 293)
- [[least squares]] — minimizing $\|y-\Phi\theta\|^2$. Here it is the ML solution (9.12c)/(9.19), found by solving a linear system (pp. 294, 296)
- [[feature-matrix-design-matrix]] (new) — $\Phi\in\mathbb R^{N\times K}$ with $\Phi_{ij}=\phi_j(x_i)$ (p. 296)
- [[rank]] — $\Phi^\top\Phi$ is invertible iff $\mathrm{rk}(\Phi)=K$ (p. 297)
- [[positive (semi)definite matrix]] — $X^\top X$ is positive definite if $\mathrm{rk}(X)=D$. $\Phi^\top\Phi+\frac{\sigma^2}{b^2}I$ is strictly positive definite (pp. 294, 302)
- [[overfitting]] (new) — fits training data "too well" and generalizes badly. Typical when the model is overly flexible (pp. 290, 299)
- [[rmse]] (new) — $\sqrt{\frac1N\|y-\Phi\theta\|^2}$, same units as the targets (p. 298)
- [[map-estimation]] (new) — maximize the posterior $p(\theta\mid\mathcal X,\mathcal Y)$; a compromise between prior and likelihood (pp. 300–301)
- [[regularization]] (new) — adding $\lambda\|\theta\|^2$ to the loss. For the Gaussian prior it equals the MAP estimate with $\lambda=\sigma^2/b^2$ (pp. 302–303)
- [[lasso]] (new) — L1 regularization; equivalent to a Laplace prior; promotes sparsity (pp. 303, 316)
- [[bayesian-linear-regression]] (new) — Gaussian prior on $\theta$; predictions average over the closed-form Gaussian posterior (pp. 303–306)
- [[posterior-predictive]] (new) — $\mathcal N(\phi^\top m_N,\phi^\top S_N\phi+\sigma^2)$ (p. 308)
- [[marginal-likelihood]] (new) — $p(\mathcal Y\mid\mathcal X)=\mathbb E_\theta[p(\mathcal Y\mid\mathcal X,\theta)]$, here $\mathcal N(y\mid Xm_0,XS_0X^\top+\sigma^2I)$ (pp. 306, 312)
- [[completing-the-square]] (new) — rewrite $x^\top Ax-2a^\top x$ as $(x-A^{-1}a)^\top A(x-A^{-1}a)+\text{const}$ to identify a Gaussian's mean and covariance (p. 308)
- [[projection]] — $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y$ is the orthogonal projection of $y$ onto the column space of $\Phi$ (p. 314)
- [[orthonormal basis / orthogonal matrix]] — with $\Phi^\top\Phi=I$ the projection is $\sum_k\phi_k\phi_k^\top y$ (p. 314)
- [[Gram–Schmidt]] — converts a non-orthogonal basis of features to an orthogonal one (p. 315)
- [[generalized-linear-model]] (new) — $y=\sigma(\theta^\top\phi(x))$ with an activation $\sigma$; building block of feedforward networks (p. 315)
- [[gaussian-process]] (new) — regression model with a distribution placed directly on functions (p. 316)

## Canonical instances
- [[polynomial-regression]] — features $[1,x,\dots,x^{K-1}]$; degree $M=4$ fits best in the example, high degrees overfit (pp. 295–300)
- [[fitting-line-through-origin]] — $y=\theta x+\epsilon$; $\theta_{ML}=X^\top y/X^\top X$ as a 1-D projection (pp. 295, 313)
- [[prior-and-posterior-over-functions]] — degree-5 polynomials with prior $\mathcal N(0,\frac14I)$ (pp. 305, 310)
- [[logistic-regression]] — GLM with logistic sigmoid (p. 315)

## Bridges (candidates)
- [same-math] ML normal equations $\Phi^\top\Phi\theta=\Phi^\top y$ ↔ linear algebra: least-squares solution of an overdetermined $A x\approx b$ — identical equations.
- [same-math] MAP with Gaussian prior ↔ regularized (ridge) least squares: $(\Phi^\top\Phi+\lambda I)^{-1}\Phi^\top y$ with $\lambda=\sigma^2/b^2$.
- [same-math] ML fit $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y$ ↔ projection onto the column space; $\Phi\Phi^\top y$ for orthonormal columns.
- [structural-analogy] Posterior precision $S_N^{-1}=S_0^{-1}+\sigma^{-2}\Phi^\top\Phi$ ↔ Bayesian updating: precisions add like information.
- [structural-analogy] Distribution over functions induced by $p(\theta)$ ↔ Gaussian processes (author calls them closely related).
- [structural-analogy] GLM composition $\sigma_k(A_kx_k+b_k)$ ↔ layers of a feedforward neural network.
- [metaphor] Prior as "regularizer" ↔ a penalty on model complexity; MAP as a compromise between belief and data.

## Questions this raises
- How should $\sigma^2$ and the prior scale $b^2$ (hence $\lambda$) be chosen from data, e.g. via the marginal likelihood (9.64)?
- When $N<K$ and $\Phi^\top\Phi$ is singular, which of the infinitely many ML solutions is the "right" one, and how does the prior pick one?
- How does the posterior covariance $S_N$ behave as $N\to\infty$, and how do the choices of features $\phi$ change it?
- What changes in the closed-form results when the likelihood is non-Gaussian, as in logistic regression?

## Reading notes
- Page offset: printed = pdf − 6 (e.g. pdf 295 = printed 289). The unit has no exercises, so no exercise section.
- The source chapter intro cites "Chapters 2, 5, 6, and 7" (p. 289) and later "Chapters 3, 5, 6 and 7" (p. 290). This is a source inconsistency.
- The Hessian in the remark on p. 294 is printed as $X^\top X$. By (9.11c), differentiating once more gives $\frac1{\sigma^2}X^\top X$, so the factor $1/\sigma^2$ appears to be omitted. Positive definiteness is unaffected.
- The two values of $\lambda$ (pp. 303: $\frac1{2b^2}$ and $\sigma^2/b^2$) are both printed; see the (added step) in 9.2.4 for how they relate.
- The statement "$\mathrm{rk}(X)=D$ if $N\ge D$" (margin, p. 294) holds only ignoring duplicate data points, as the margin note says.
- In 9.3.3 the colors (blue quadratic, orange linear, black constant) in (9.46)–(9.48) are visible only in the page image. The text layer loses them.
- Typo in source: "qualitive" (p. 299). Fig. 9.6's test-error curve leaves the plotted range shortly after degree 7.
- Page footers show "Draft (2024-01-15)" and a 2020 Cambridge University Press copyright line.
