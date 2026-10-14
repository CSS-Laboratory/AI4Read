---
id: deisenroth-2020-mml/ch06-probability-p2
work: deisenroth-2020-mml
unit: "6 Probability and Distributions (part 2/2): §6.5 Gaussian Distribution to §6.8 Further Reading, and Exercises"
pages: 197-224
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Probability and Distributions, part 2: Gaussians, Conjugacy, Exponential Families, Change of Variables

## L0 — One line
Gaussians stay Gaussian under marginalizing, conditioning, summing independent variables and linear maps; exponential families have conjugate priors, so Bayesian updating stays inside the family; and change of variables (with a Jacobian determinant) gives the density of a differentiable invertible transform.

## L1 — The gist (≤ 120 words)
How can we compute with probability distributions in closed form? The chapter answers in three steps. First, Gaussians stay Gaussian under marginalization, conditioning, sums of independent variables and linear maps, with simple matrix formulas for the parameters. Second, conjugate priors (whose posterior has the same form as the prior) turn Bayesian updating into a parameter update (Beta–Bernoulli, Beta–Binomial); the exponential family unifies such distributions and has finite-dimensional sufficient statistics (summaries carrying all information about the parameter). Third, for a transformed random variable, the cdf (cumulative distribution function) technique and the change-of-variables formula give its density, using $|dU^{-1}/dy|$ or the Jacobian determinant. This matters because linear regression, Gaussian processes and Kalman filters use these closure properties.

**Prerequisites:** matrix inverse, transpose and determinant; covariance matrix; Bayes' theorem (posterior ∝ likelihood × prior); basic integration and the chain rule; the Jacobian as a matrix of partial derivatives.

## L2 — Key ideas
- A multivariate Gaussian $\mathcal N(\mu,\Sigma)$ is fixed by its mean vector and covariance matrix. Its marginals and conditionals are Gaussian with closed-form parameters, (6.65)–(6.68) (pp. 198–199).
- The product of two Gaussian densities is a scaled Gaussian with $C=(A^{-1}+B^{-1})^{-1}$. This is the multiplication that arises when Bayes' theorem combines a Gaussian prior with a Gaussian likelihood (p. 201).
- Independent Gaussians add by adding means and covariances. A linear map $y=Ax$ of $x\sim\mathcal N(\mu,\Sigma)$ gives $\mathcal N(A\mu, A\Sigma A^\top)$. A Cholesky factor $A$ with $AA^\top=\Sigma$ turns standard-normal samples $x$ into samples $y=Ax+\mu$ from $\mathcal N(\mu,\Sigma)$ (pp. 201–204).
- A mixture of Gaussian densities (a weighted sum of densities) is different from a weighted sum of Gaussian random variables. Its mean is the weighted mean, and its variance is the weighted variances plus the variance of the component means, an instance of the law of total variance (pp. 202–203).
- A prior is conjugate if the posterior has the same form. Beta is conjugate to Bernoulli and Binomial, and the update is $\alpha\to\alpha+h$, $\beta\to\beta+N-h$ (pp. 208–209).
- Exponential family: $p(x|\theta)=h(x)\exp(\langle\theta,\phi(x)\rangle-A(\theta))$. It has finite-dimensional sufficient statistics and an explicit conjugate prior, and it contains Gaussian, Bernoulli, Binomial and Beta (pp. 210–214).
- Change of variables: for differentiable invertible $y=U(x)$, $f(y)=f_x(U^{-1}(y))\,|\det\partial U^{-1}/\partial y|$. The cdf technique and the probability integral transform (cdf of $X$ applied to $X$ is uniform) are used to derive sampling by transforming uniform samples with the inverse cdf (pp. 215–219).

## L3 — Walkthrough

### End of §6.4 (start of this part), p. 197
The part opens inside a remark. Comparing probability distributions with a distance built from inner products is "unfortunately not the best way" to get distances (p. 197). Probability mass or density is positive and sums to 1, so distributions live on a *statistical manifold*; its study is *information geometry*. Distances between distributions are often computed with the Kullback–Leibler divergence. The book says it is a special case of Bregman divergences and of $f$-divergences, and calls divergences beyond its scope (p. 197).

### 6.5 Gaussian Distribution (pp. 197–204)
The Gaussian (normal) distribution is the best-studied distribution for continuous variables. The book says its importance comes from many computationally convenient properties. It arises naturally for sums of independent identically distributed variables (central limit theorem, margin note). It is used for the likelihood and prior in linear regression (Chapter 9) and for mixtures in density estimation (Chapter 11) (p. 197).

**Densities.** Univariate:
$$p(x\mid\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)\tag{6.62}$$
Multivariate, $x\in\mathbb R^D$, with mean vector $\mu$ and covariance matrix $\Sigma$:
$$p(x\mid\mu,\Sigma)=(2\pi)^{-D/2}|\Sigma|^{-1/2}\exp\!\big(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\big)\tag{6.63}$$
We write $p(x)=\mathcal N(x\mid\mu,\Sigma)$ or $X\sim\mathcal N(\mu,\Sigma)$. The case $\mu=0,\ \Sigma=I$ is the *standard normal* (p. 198).

Gaussians have closed-form marginals and conditionals, which Chapter 9 uses. Since a Gaussian is fully specified by mean and covariance, one can often get the transformed distribution by transforming the mean and covariance, so variable transformations (§6.7) are "often not needed" (p. 198).

#### 6.5.1 Marginals and conditionals of Gaussians are Gaussians (pp. 198–200)
Write the joint distribution of $x$ and $y$ (possibly different dimensions) via the concatenated vector:
$$p(x,y)=\mathcal N\!\Big(\begin{bmatrix}\mu_x\\ \mu_y\end{bmatrix},\begin{bmatrix}\Sigma_{xx}&\Sigma_{xy}\\ \Sigma_{yx}&\Sigma_{yy}\end{bmatrix}\Big)\tag{6.64}$$
Here $\Sigma_{xx}=\mathrm{Cov}[x,x]$ and $\Sigma_{yy}=\mathrm{Cov}[y,y]$ are the marginal covariance matrices, and $\Sigma_{xy}=\mathrm{Cov}[x,y]$ is the cross-covariance matrix (p. 199).

**Conditional** (derivation cited to Bishop 2006, not given here):
$$p(x\mid y)=\mathcal N(\mu_{x|y},\Sigma_{x|y})\tag{6.65}$$
$$\mu_{x|y}=\mu_x+\Sigma_{xy}\Sigma_{yy}^{-1}(y-\mu_y)\tag{6.66}$$
$$\Sigma_{x|y}=\Sigma_{xx}-\Sigma_{xy}\Sigma_{yy}^{-1}\Sigma_{yx}\tag{6.67}$$
In (6.66), $y$ is an observed value, no longer random (p. 199).

*Remark (p. 199).* Gaussian conditionals appear in the Kalman filter (the book says it "does nothing but" compute them), in Gaussian processes (conditioning on data gives a posterior over functions), and in latent linear Gaussian models such as probabilistic PCA (Section 10.7).

**Marginal** (sum rule (6.20)):
$$p(x)=\int p(x,y)\,dy=\mathcal N(x\mid\mu_x,\Sigma_{xx})\tag{6.68}$$
The same holds for $p(y)$. Intuitively, we integrate out everything we are not interested in (p. 199).

**Example 6.6 (p. 200).** $p(x_1,x_2)=\mathcal N\big(\begin{bmatrix}0\\2\end{bmatrix},\begin{bmatrix}0.3&-1\\-1&5\end{bmatrix}\big)$ (6.69). Condition on $x_2=-1$:
$\mu_{x_1|x_2=-1}=0+(-1)\cdot0.2\cdot(-1-2)=0.6$ (6.70),
$\sigma^2_{x_1|x_2=-1}=0.3-(-1)\cdot0.2\cdot(-1)=0.1$ (6.71),
so $p(x_1\mid x_2=-1)=\mathcal N(0.6,0.1)$ (6.72). The marginal is $p(x_1)=\mathcal N(0,0.3)$ (6.73).

*Intuition note.* Marginalizing just reads off the matching blocks of $\mu$ and $\Sigma$. Conditioning shifts the mean in proportion to how far the observation is from its mean (6.66). In Example 6.6 it also lowers the variance, from 0.3 to 0.1.

#### 6.5.2 Product of Gaussian densities (p. 201)
In linear regression (Chapter 9) we need a Gaussian likelihood and may assume a Gaussian prior; Bayes' theorem then multiplies the two. The product of two Gaussian densities is a Gaussian scaled by $c\in\mathbb R$:
$$\mathcal N(x\mid a,A)\,\mathcal N(x\mid b,B)=c\,\mathcal N(x\mid c,C)$$
$$C=(A^{-1}+B^{-1})^{-1}\tag{6.74}$$
$$c=C(A^{-1}a+B^{-1}b)\tag{6.75}$$
$$c=(2\pi)^{-D/2}|A+B|^{-1/2}\exp\!\big(-\tfrac12(a-b)^\top(A+B)^{-1}(a-b)\big)\tag{6.76}$$
(The book uses the symbol $c$ both for the mean vector and for the scalar constant; the derivation is Exercise 6.10.) The constant is itself a Gaussian density with "inflated" covariance: $c=\mathcal N(a\mid b,A+B)=\mathcal N(b\mid a,A+B)$ (6.77). The notation $\mathcal N(x\mid m,S)$ is used for the functional form even when $x$ is not random (p. 201).

*Intuition note.* Adding the precisions (inverse covariances) $A^{-1}+B^{-1}$ gives the new precision $C^{-1}$. The new mean is a precision-weighted average of $a$ and $b$.

#### 6.5.3 Sums and linear transformations (pp. 201–204)
If $X,Y$ are independent Gaussians, $p(x)=\mathcal N(\mu_x,\Sigma_x)$ and $p(y)=\mathcal N(\mu_y,\Sigma_y)$, then
$$p(x+y)=\mathcal N(\mu_x+\mu_y,\ \Sigma_x+\Sigma_y)\tag{6.78}$$
Given that the sum is Gaussian, mean and covariance follow from (6.46)–(6.49). This matters for i.i.d. Gaussian noise in regression (p. 201). Example 6.7: for independent Gaussians, $p(ax+by)=\mathcal N(a\mu_x+b\mu_y,\ a^2\Sigma_x+b^2\Sigma_y)$ (6.79) (p. 201).

**Mixtures are different** (p. 202). A weighted sum of *densities* is not a weighted sum of *random variables*.

**Theorem 6.12.** Let $p(x)=\alpha p_1(x)+(1-\alpha)p_2(x)$ (6.80), with $0<\alpha<1$ and $p_1,p_2$ univariate Gaussians with $(\mu_1,\sigma_1^2)\ne(\mu_2,\sigma_2^2)$. Then
$$\mathbb E[x]=\alpha\mu_1+(1-\alpha)\mu_2\tag{6.81}$$
$$\mathbb V[x]=\big[\alpha\sigma_1^2+(1-\alpha)\sigma_2^2\big]+\Big(\big[\alpha\mu_1^2+(1-\alpha)\mu_2^2\big]-\big[\alpha\mu_1+(1-\alpha)\mu_2\big]^2\Big)\tag{6.82}$$
*Proof (pp. 202–203).*
$$\mathbb E[x]=\int_{-\infty}^\infty xp(x)dx=\int(\alpha xp_1+(1-\alpha)xp_2)dx=\alpha\!\int xp_1dx+(1-\alpha)\!\int xp_2dx=\alpha\mu_1+(1-\alpha)\mu_2\tag{6.83a–d}$$
Using the raw-score variance (6.44), $\sigma^2=\mathbb E[x^2]-\mu^2$:
$$\mathbb E[x^2]=\int x^2p(x)dx=\alpha\!\int x^2p_1dx+(1-\alpha)\!\int x^2p_2dx=\alpha(\mu_1^2+\sigma_1^2)+(1-\alpha)(\mu_2^2+\sigma_2^2)\tag{6.84a–d}$$
$$\mathbb V[x]=\mathbb E[x^2]-(\mathbb E[x])^2=\alpha(\mu_1^2+\sigma_1^2)+(1-\alpha)(\mu_2^2+\sigma_2^2)-(\alpha\mu_1+(1-\alpha)\mu_2)^2\tag{6.85a,b}$$
Regrouping gives (6.82), the form (6.85c). $\square$

The derivation holds for any density. Because a Gaussian is fixed by mean and variance, the mixture density can be determined in closed form (p. 203). The theorem extends to multivariate variables if the square is replaced by $xx^\top$ (p. 202).

*Law of total variance (p. 203).* Components can be viewed as conditionals given the component identity. (6.85c) is an instance of $\mathbb V_X[x]=\mathbb E_Y[\mathbb V_X[x|y]]+\mathbb V_Y[\mathbb E_X[x|y]]$: expected conditional variance plus variance of the conditional mean.

*Intuition note.* A mixture's spread has two sources: the spread inside each component, and the spread between component means. Only the first appears if both means are equal.

**Linear/affine maps (p. 203).** The book recalls Example 6.17 (below): a linear map $Ax$ of a standard bivariate Gaussian gives mean 0 and covariance $AA^\top$, and adding a constant shifts the mean only. It concludes that any linear/affine transformation of a Gaussian is Gaussian. For $X\sim\mathcal N(\mu,\Sigma)$ and $y=Ax$:
$$\mathbb E[y]=A\mathbb E[x]=A\mu\tag{6.86}$$
$$\mathbb V[y]=A\mathbb V[x]A^\top=A\Sigma A^\top\tag{6.87}$$
$$p(y)=\mathcal N(y\mid A\mu,\ A\Sigma A^\top)\tag{6.88}$$

**Reverse direction (p. 204).** For full-rank $A\in\mathbb R^{M\times N}$, $M\ge N$, let $p(y)=\mathcal N(y\mid Ax,\Sigma)$ (6.89), $y\in\mathbb R^M$. What is $p(x)$? If $A$ is invertible, use $x=A^{-1}y$ and (6.88). Otherwise, pre-multiply by $A^\top$ and invert $A^\top A$ (symmetric, positive definite), in an approach similar to the pseudo-inverse (3.57):
$$y=Ax\iff (A^\top A)^{-1}A^\top y=x\tag{6.90}$$
$$p(x)=\mathcal N\big(x\mid (A^\top A)^{-1}A^\top y,\ (A^\top A)^{-1}A^\top\Sigma A(A^\top A)^{-1}\big)\tag{6.91}$$

#### 6.5.4 Sampling from multivariate Gaussians (p. 204)
Subtleties of computer random sampling are left to Gentle (2004). Three stages for a standard normal $\mathcal N(0,I)$: (1) pseudo-random uniform numbers in $[0,1]$; (2) a non-linear transform such as Box–Müller to get univariate Gaussian samples; (3) stack these into a vector. For general $\mathcal N(\mu,\Sigma)$: if $x\sim\mathcal N(0,I)$ and $AA^\top=\Sigma$, then $y=Ax+\mu\sim\mathcal N(\mu,\Sigma)$. A convenient $A$ is the Cholesky factor of $\Sigma=AA^\top$ (Section 4.3). It is triangular, so computation is efficient. Cholesky needs a symmetric positive definite matrix, which covariance matrices are (margin note).

### 6.6 Conjugacy and the Exponential Family (pp. 205–214)
Many named distributions were found to model particular phenomena, in the era of pencil-and-paper computation. The book lists three desiderata for ML (p. 205):
1. A "closure property" under the rules of probability (e.g., Bayes' theorem): the operation returns an object of the same type.
2. More data should not require more parameters.
3. Parameter estimation should behave nicely.

The exponential family is said to give the right balance of generality and good computation and inference properties. Three named distributions are introduced first (pp. 205–207).

**Example 6.8 (Bernoulli, p. 205).** One binary variable $x\in\{0,1\}$, parameter $\mu\in[0,1]$ is $P(X=1)$:
$$p(x\mid\mu)=\mu^x(1-\mu)^{1-x}\ (6.92),\quad \mathbb E[x]=\mu\ (6.93),\quad \mathbb V[x]=\mu(1-\mu)\ (6.94)$$
The remark on p. 206 notes that writing Booleans as 0/1 exponents is a common ML-textbook trick (also used for the Multinomial).

**Example 6.9 (Binomial, p. 206).** Number $m$ of $X=1$ outcomes in $N$ Bernoulli samples with $p(X=1)=\mu$:
$$p(m\mid N,\mu)=\binom Nm\mu^m(1-\mu)^{N-m}\ (6.95),\quad \mathbb E[m]=N\mu\ (6.96),\quad \mathbb V[m]=N\mu(1-\mu)\ (6.97)$$

**Example 6.10 (Beta, pp. 206–207).** A distribution over $\mu\in[0,1]$, with parameters $\alpha>0,\beta>0$:
$$p(\mu\mid\alpha,\beta)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\mu^{\alpha-1}(1-\mu)^{\beta-1}\tag{6.98}$$
$$\mathbb E[\mu]=\frac{\alpha}{\alpha+\beta},\quad \mathbb V[\mu]=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}\tag{6.99}$$
with the Gamma function $\Gamma(t):=\int_0^\infty x^{t-1}e^{-x}dx$, $t>0$ (6.100), and $\Gamma(t+1)=t\Gamma(t)$ (6.101). The ratio of Gamma functions normalizes the density. Intuitively $\alpha$ moves mass toward 1 and $\beta$ toward 0. Special cases (Murphy 2012): $\alpha=\beta=1$ gives uniform $\mathcal U[0,1]$; $\alpha,\beta<1$ gives a bimodal density with spikes at 0 and 1; $\alpha,\beta>1$ gives a unimodal density; $\alpha,\beta>1$ with $\alpha=\beta$ gives a unimodal symmetric density with mode and mean at $\tfrac12$ (p. 207).

The remark on pp. 207–208 says each named distribution was created for a reason but may have other uses. These three are introduced to illustrate conjugacy (§6.6.1) and exponential families (§6.6.3).

#### 6.6.1 Conjugacy (pp. 208–210)
The posterior is proportional to prior × likelihood (6.23). Specifying a prior is hard for two reasons: it should encode knowledge before seeing data, and the posterior often cannot be computed analytically (p. 208).

**Definition 6.13 (Conjugate prior).** A prior is conjugate for the likelihood function if the posterior is of the same form/type as the prior. Then the posterior is obtained algebraically by updating the prior's parameters (p. 208).

**Example 6.11 (Beta–Binomial, pp. 208–209).** Likelihood $x\sim\mathrm{Bin}(N,\mu)$ (6.102), prior $\mu\sim\mathrm{Beta}(\alpha,\beta)$ (6.103). Observe $x=h$ heads in $N$ flips:
$$p(\mu\mid x=h,N,\alpha,\beta)\propto p(x|N,\mu)\,p(\mu|\alpha,\beta)\propto\mu^h(1-\mu)^{N-h}\mu^{\alpha-1}(1-\mu)^{\beta-1}=\mu^{h+\alpha-1}(1-\mu)^{(N-h)+\beta-1}\tag{6.104a–c}$$
$$\propto\mathrm{Beta}(h+\alpha,\ N-h+\beta)\tag{6.104d}$$
So the Beta prior is conjugate for $\mu$ in the Binomial likelihood.

**Example 6.12 (Beta–Bernoulli, p. 209).** Likelihood $p(x|\theta)=\theta^x(1-\theta)^{1-x}$, prior $p(\theta|\alpha,\beta)\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}$:
$$p(\theta|x,\alpha,\beta)\propto\theta^x(1-\theta)^{1-x}\theta^{\alpha-1}(1-\theta)^{\beta-1}=\theta^{\alpha+x-1}(1-\theta)^{\beta+(1-x)-1}\propto p(\theta\mid\alpha+x,\ \beta+(1-x))\tag{6.105a–d}$$

**Table 6.2 (p. 209).** Likelihood → conjugate prior (posterior of same type): Bernoulli → Beta; Binomial → Beta; Gaussian → Gaussian/inverse Gamma; Gaussian → Gaussian/inverse Wishart; Multinomial → Dirichlet. The Gaussian appears twice for univariate versus multivariate. A Gaussian prior is conjugate on the mean. Inverse Gamma is conjugate for the univariate variance, inverse Wishart for the multivariate covariance (pp. 209–210). The margin note adds that Gamma is conjugate for the precision (inverse variance) and Wishart for the precision matrix.

*Intuition note.* With a Beta prior, the parameters $\alpha,\beta$ act like running counts of heads and tails. Observing data just adds to the counts, so the posterior needs no integration.

#### 6.6.2 Sufficient statistics (pp. 210–211)
A *statistic* is a deterministic function of a random variable, e.g. the sample mean $\hat\mu=\frac1N(x_1+\dots+x_N)$. Fisher's *sufficient statistics* carry all the information in the data about the distribution. Formally, a vector $\phi(x)$ is sufficient for $\theta_0$ if $p(x|\theta)$ factors into a part independent of $\theta$ and a part depending on $\theta$ only through $\phi(x)$ (p. 210).

**Theorem 6.14 (Fisher–Neyman; stated without proof).** The statistics $\phi(x)$ are sufficient for $\theta$ if and only if
$$p(x\mid\theta)=h(x)\,g_\theta(\phi(x))\tag{6.106}$$
where $h(x)$ is independent of $\theta$ and $g_\theta$ carries all dependence on $\theta$ through $\phi(x)$. If $p(x|\theta)$ does not depend on $\theta$, any $\phi$ is trivially sufficient. The interesting case is dependence on $\phi(x)$ only (p. 210).

Do we need more parameters as data grows? The book says "in general" yes (non-parametric statistics). A converse question is which classes have finite-dimensional sufficient statistics. The answer is exponential-family distributions (pp. 210–211).

#### 6.6.3 Exponential family (pp. 211–214)
Three levels of abstraction: (1) a named distribution with fixed parameters, e.g. $\mathcal N(0,1)$; (2) a fixed parametric form with parameters inferred from data, e.g. maximum likelihood for $(\mu,\sigma^2)$; (3) families of distributions, here the exponential family (p. 211). The univariate Gaussian and all named models in Table 6.2 belong to it (p. 211).

*Remark (p. 211).* In 1935–1936 Pitman, Darmois and Koopman independently showed that exponential families are the only families with finite-dimensional sufficient statistics under repeated independent sampling.

**Definition.** An exponential family with parameter $\theta\in\mathbb R^D$:
$$p(x\mid\theta)=h(x)\exp\big(\langle\theta,\phi(x)\rangle-A(\theta)\big)\tag{6.107}$$
$\phi(x)$ is the vector of sufficient statistics; the standard dot product $\theta^\top\phi(x)$ is used. This is a particular form of $g_\theta(\phi(x))$ in Theorem 6.14. The factor $h(x)$ can be absorbed by appending $\log h(x)$ to $\phi$ with its parameter fixed to 1. $A(\theta)$ is the normalizer, called the *log-partition function* (p. 211). Ignoring $h$ and $A$ gives the intuition
$$p(x\mid\theta)\propto\exp(\theta^\top\phi(x))\tag{6.108}$$
and $\theta$ are then the *natural parameters* (p. 212).

**Example 6.13 (Gaussian, p. 212).** Take $\phi(x)=\begin{bmatrix}x\\x^2\end{bmatrix}$, so $p(x|\theta)\propto\exp(\theta_1x+\theta_2x^2)$ (6.109). With $\theta=\big[\tfrac{\mu}{\sigma^2},-\tfrac1{2\sigma^2}\big]^\top$ (6.110):
$$p(x|\theta)\propto\exp\!\Big(\frac{\mu x}{\sigma^2}-\frac{x^2}{2\sigma^2}\Big)\propto\exp\!\Big(-\frac1{2\sigma^2}(x-\mu)^2\Big)\tag{6.111}$$
The last "∝" holds because the dropped factor $\exp(-\mu^2/2\sigma^2)$ does not depend on $x$ (added step).

**Example 6.14 (Bernoulli, pp. 212–213).**
$$p(x|\mu)=\exp[\log(\mu^x(1-\mu)^{1-x})]=\exp[x\log\mu+(1-x)\log(1-\mu)]=\exp[x\log\mu-x\log(1-\mu)+\log(1-\mu)]=\exp\Big[x\log\tfrac{\mu}{1-\mu}+\log(1-\mu)\Big]\tag{6.113a–d}$$
Matching (6.107): $h(x)=1$ (6.114); $\theta=\log\frac\mu{1-\mu}$ (6.115); $\phi(x)=x$ (6.116); $A(\theta)=-\log(1-\mu)=\log(1+\exp\theta)$ (6.117). The map is invertible: $\mu=\frac1{1+\exp(-\theta)}$ (6.118), used for the right-hand equality in (6.117).

*Remark (p. 213).* The map from $\mu$ to $\theta$ is the sigmoid (logistic) function. $\mu\in(0,1)$ but $\theta\in\mathbb R$, so the sigmoid squeezes a real value into $(0,1)$. It is used in logistic regression and as a neural-network activation.

**Conjugate priors from the exponential family (p. 213).** For $p(x|\theta)=h(x)\exp(\langle\theta,\phi(x)\rangle-A(\theta))$ (6.119), the book states that every member has a conjugate prior (Brown 1986):
$$p(\theta\mid\gamma)=h_c(\theta)\exp\Big(\Big\langle\begin{bmatrix}\gamma_1\\\gamma_2\end{bmatrix},\begin{bmatrix}\theta\\-A(\theta)\end{bmatrix}\Big\rangle-A_c(\gamma)\Big)\tag{6.120}$$
with $\gamma=\begin{bmatrix}\gamma_1\\\gamma_2\end{bmatrix}$ of dimension $\dim(\theta)+1$. Its sufficient statistics are $\begin{bmatrix}\theta\\-A(\theta)\end{bmatrix}$.

**Example 6.15 (p. 214).** Start from the Bernoulli form (6.121). The canonical conjugate prior is written
$$p(\mu|\alpha,\beta)=\frac{\mu}{1-\mu}\exp\Big[\alpha\log\tfrac\mu{1-\mu}+(\beta+\alpha)\log(1-\mu)-A_c(\gamma)\Big]\tag{6.122}$$
with $\gamma:=[\alpha,\beta+\alpha]^\top$, $h_c(\mu):=\mu/(1-\mu)$. It is stated to simplify to $p(\mu|\alpha,\beta)=\exp[(\alpha-1)\log\mu+(\beta-1)\log(1-\mu)-A_c(\alpha,\beta)]$ (6.123), i.e. $\propto\mu^{\alpha-1}(1-\mu)^{\beta-1}$ (6.124), the Beta distribution (see Reading notes on this step). So the Beta form can be derived from the exponential-family conjugate-prior recipe, matching Example 6.12.

**Why exponential families (p. 214).** They have finite-dimensional sufficient statistics. Conjugate priors are easy to write down and come from an exponential family. In maximum likelihood, empirical estimates of sufficient statistics are optimal estimates of the population values. The log-likelihood is concave, so efficient optimization applies (Chapter 7).

*Intuition note.* In (6.108) the data enter only through $\phi(x)$. A finite-dimensional vector of statistics, such as $(x,x^2)$ for the Gaussian, captures the information about $\theta$ in the data (p. 212); the book's motivation is that the number of parameters needed does not increase arbitrarily (p. 211).

### 6.7 Change of Variables / Inverse Transform (pp. 214–220)
The set of named distributions is quite limited, so it is often useful to know how transformed variables are distributed. Examples: if $X\sim\mathcal N(0,1)$, what is the law of $X^2$? If $X_1,X_2$ are standard normal, what is the law of $\tfrac12(X_1+X_2)$? Means and variances of affine transforms are available (§6.4.4), but the functional form may not be, and non-linear maps may have no closed form (pp. 214–215). Notation: capital letters are random variables, small letters are values; pmf $P(X=x)$, pdf $f(x)$, cdf $F_X(x)$ (p. 215).

**Discrete case (p. 215).** For invertible $U$ and $Y:=U(X)$:
$$P(Y=y)=P(U(X)=y)=P(X=U^{-1}(y))\tag{6.125a,b}$$
So events are relabelled and their probabilities carried over.

#### 6.7.1 Distribution function technique (pp. 215–217)
For $Y:=U(X)$: (1) find the cdf $F_Y(y)=P(Y\le y)$ (6.126); (2) differentiate, $f(y)=\frac{d}{dy}F_Y(y)$ (6.127). Keep in mind that the domain may change (p. 216).

**Example 6.16 (p. 216).** $f(x)=3x^2$ on $0\le x\le1$; find the pdf of $Y=X^2$. The map is increasing, so $y\in[0,1]$.
$$F_Y(y)=P(X^2\le y)=P(X\le y^{1/2})=F_X(y^{1/2})=\int_0^{y^{1/2}}3t^2dt=[t^3]_0^{y^{1/2}}=y^{3/2}\tag{6.129a–g}$$
So $F_Y(y)=y^{3/2}$ (6.130), and $f(y)=\frac d{dy}F_Y(y)=\tfrac32y^{1/2}$ on $0\le y\le1$ (6.131).

**Theorem 6.15 (probability integral transform).** If $X$ is continuous with strictly monotonic cdf $F_X$, then $Y:=F_X(X)$ is uniformly distributed (6.132) (p. 216; proof is Exercise 6.13). Uses named in the text (p. 217): sampling algorithms (draw uniform, apply the inverse cdf if available), hypothesis tests of whether a sample comes from a given distribution, and the basis of copulas.

*Intuition note.* Pushing a variable through its own cdf flattens it to uniform. Running that backwards, with the inverse cdf, turns uniform random numbers into samples from the desired distribution, assuming its inverse cdf is available (p. 217).

#### 6.7.2 Change of variables (pp. 217–220)
The cdf argument relies on (1) turning the cdf of $Y$ into a cdf of $X$ and (2) differentiating a cdf to get a pdf (p. 217). The name comes from substitution in integrals:
$$\int f(g(x))g'(x)dx=\int f(u)du,\quad u=g(x)\tag{6.133}$$
(based on the chain rule and the fundamental theorem of calculus; loosely, $du\approx\Delta u=g'(x)\Delta x$) (p. 217).

**Derivation, univariate** ($X$ has states $x\in[a,b]$; $U$ invertible, hence strictly monotone on an interval; first assume strictly increasing) (pp. 217–218):
- $F_Y(y)=P(Y\le y)$ (6.134) $=P(U(X)\le y)$ (6.135).
- Apply $U^{-1}$ (also increasing): $P(U(X)\le y)=P(U^{-1}(U(X))\le U^{-1}(y))=P(X\le U^{-1}(y))$ (6.136).
- This is a cdf of $X$: $P(X\le U^{-1}(y))=\int_a^{U^{-1}(y)}f(x)dx$ (6.137), so $F_Y(y)=\int_a^{U^{-1}(y)}f(x)dx$ (6.138).
- Differentiate: $f(y)=\frac d{dy}F_y(y)=\frac d{dy}\int_a^{U^{-1}(y)}f(x)dx$ (6.139).
- The integral is in $x$ but we differentiate in $y$, so substitute with (6.133): $\int f(U^{-1}(y))U^{-1\prime}(y)dy=\int f(x)dx$, $x=U^{-1}(y)$ (6.140). Hence $f(y)=\frac d{dy}\int_a^{U^{-1}(y)}f_x(U^{-1}(y))U^{-1\prime}(y)dy$ (6.141). The subscript $x$ reminds us that $f_x(U^{-1}(y))$ is a function of $x$.
- The fundamental theorem of calculus gives $f(y)=f_x(U^{-1}(y))\cdot\frac d{dy}U^{-1}(y)$ (6.142).
- For decreasing $U$ a negative sign appears; the absolute value covers both:
$$f(y)=f_x(U^{-1}(y))\cdot\Big|\frac d{dy}U^{-1}(y)\Big|\tag{6.143}$$

*Skip path:* carry forward (6.143); the factor $|dU^{-1}/dy|$ measures how much a unit volume changes under $U$ (p. 219).

*Remark (p. 219).* Compared with the discrete case (6.125b), the continuous case has the extra factor because $P(Y=y)=0$ for all $y$, and a density is not the probability of an event involving $y$.

**Theorem 6.16 (multivariate; Billingsley 1995).** Let $f(x)$ be the density of a multivariate continuous $X$. If $y=U(x)$ is differentiable and invertible for all $x$ in the domain, then $Y=U(X)$ has density
$$f(y)=f_x(U^{-1}(y))\cdot\Big|\det\Big(\frac\partial{\partial y}U^{-1}(y)\Big)\Big|\tag{6.144}$$
The absolute value is replaced by the determinant of the Jacobian matrix, since absolute value does not apply to multivariate functions. Recipe: find the inverse, substitute it into the density of $x$, then multiply by the Jacobian determinant (p. 219).

**Example 6.17 (pp. 219–220).** $X$ bivariate with $f(x)=\frac1{2\pi}\exp(-\tfrac12x^\top x)$ (6.145). Let $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$ (6.146) and $y=Ax$. The inverse is
$$x=A^{-1}y=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}y\tag{6.147}$$
where $ad-bc=\det A$. Then $f(x)=f(A^{-1}y)=\frac1{2\pi}\exp(-\tfrac12y^\top A^{-\top}A^{-1}y)$ (6.148). Since $\frac\partial{\partial y}A^{-1}y=A^{-1}$ (6.149) and $\det(A^{-1})=1/\det A$, we get $\det\big(\frac\partial{\partial y}A^{-1}y\big)=\frac1{ad-bc}$ (6.150). Therefore
$$f(y)=f(x)\Big|\det\Big(\frac\partial{\partial y}A^{-1}y\Big)\Big|=\frac1{2\pi}\exp\big(-\tfrac12y^\top A^{-\top}A^{-1}y\big)\,|ad-bc|^{-1}\tag{6.151a,b}$$
The relation holds in higher dimensions. By the remark on p. 220, (6.148) is the standard Gaussian and $f(y)$ is a bivariate Gaussian with covariance $\Sigma=AA^\top$.

*Intuition note.* Stretching space by $A$ spreads probability over a region $|\det A|$ times larger, so the density must be divided by $|\det A|$. This keeps the total probability equal to 1.

The chapter ends by pointing to probabilistic modelling in §8.4, the graphical language of §8.5, and applications in Chapters 9 and 11 (pp. 220–221).

### 6.8 Further Reading (p. 221)
The author calls the chapter "rather terse at times". The reading list covers: gentler texts (Grinstead and Snell; Walpole et al.), exponential families (Barndorff-Nielsen), normalizing flows (which rely on change of variables), and variational inference for neural networks (Goodfellow et al.). The chapter avoided measure-theoretic issues. These matter, for example, when conditioning on $X=x$ for continuous variables, which is a set of measure zero. A precise notation would use $\mathbb E_y[f(y)\mid\sigma(x)]$, with $\sigma(x)$ the $\sigma$-algebra of $x$. The text also names probabilistic ML books (MacKay; Bishop; Rasmussen and Williams; Barber; Murphy).

### Exercises (pp. 222–224)
Thirteen exercises are printed (6.1–6.13); see "Exercises worth doing". No solutions are given in these pages.

## Toy example (ours, not from the text)
**Beta–Binomial update.** Prior on a coin's heads probability: $\mu\sim\mathrm{Beta}(2,2)$. Prior mean (6.99): $2/(2+2)=0.5$. Observe $N=5$ flips with $h=4$ heads. By (6.104d) the posterior is $\mathrm{Beta}(h+\alpha,\ N-h+\beta)=\mathrm{Beta}(4+2,\ 5-4+2)=\mathrm{Beta}(6,3)$. Posterior mean (6.99): $6/(6+3)=2/3\approx0.667$. Posterior variance: $\dfrac{6\cdot3}{(9)^2(9+1)}=\dfrac{18}{810}\approx0.0222$. Prior variance: $\dfrac{2\cdot2}{4^2\cdot5}=\dfrac4{80}=0.05$. The data moved the mean from 0.5 toward the sample proportion $4/5=0.8$, and the variance fell from 0.05 to about 0.022. No integration was needed.

**Linear map of a standard Gaussian.** Let $x\sim\mathcal N(0,I_2)$ and $A=\begin{bmatrix}2&0\\1&1\end{bmatrix}$. By (6.88), $y=Ax$ has mean $0$ and covariance $AA^\top=\begin{bmatrix}2&0\\1&1\end{bmatrix}\begin{bmatrix}2&1\\0&1\end{bmatrix}=\begin{bmatrix}4&2\\2&2\end{bmatrix}$. Here $\det A=2\cdot1-0\cdot1=2$, so the density factor in (6.151b) is $|ad-bc|^{-1}=1/2$. Check: $\det\Sigma=4\cdot2-2\cdot2=4=(\det A)^2$. Also, $A$ is already triangular with $AA^\top=\Sigma$, so it serves as a Cholesky-type factor for sampling (§6.5.4).

## Concepts
- [[multivariate-gaussian]] (new) — density (6.63) fixed by mean vector and covariance matrix; closed under marginalizing, conditioning, sums and affine maps (p. 198)
- [[covariance-matrix]] — here $\Sigma$ in the Gaussian; blocks $\Sigma_{xx},\Sigma_{yy}$ are marginal covariances, $\Sigma_{xy}$ the cross-covariance (p. 199)
- [[gaussian-conditioning]] (new) — formulas (6.66)–(6.67) for $p(x|y)$ in a joint Gaussian (p. 199)
- [[gaussian-product]] (new) — product of two Gaussian densities is a scaled Gaussian with $C=(A^{-1}+B^{-1})^{-1}$ (p. 201)
- [[mixture-of-gaussians]] (new) — weighted sum of densities (not of variables); moments in Theorem 6.12 (p. 202)
- [[law-of-total-variance]] (new) — total variance = expected conditional variance + variance of conditional mean (p. 203)
- [[cholesky-sampling]] (new) — sample $y=Ax+\mu$ with $AA^\top=\Sigma$, $A$ triangular (p. 204)
- [[pseudoinverse]] — $(A^\top A)^{-1}A^\top$ used to invert $y=Ax$ when $A$ is not invertible (p. 204)
- [[positive-semidefinite-matrix]] — here: $A^\top A$ is symmetric positive definite for full-rank $A$; covariance matrices are symmetric positive definite (p. 204)
- [[conjugate-prior]] (new) — prior whose posterior has the same form (Def. 6.13) (p. 208)
- [[beta-distribution]] (new) — density on $[0,1]$ with parameters $\alpha,\beta$ (6.98) (p. 207)
- [[bernoulli-binomial]] (new) — binary variable and its count version (pp. 205–206)
- [[sufficient-statistic]] (new) — statistics through which $p(x|\theta)$ depends on $\theta$ (Fisher–Neyman) (p. 210)
- [[exponential-family]] (new) — $h(x)\exp(\langle\theta,\phi(x)\rangle-A(\theta))$ (p. 211)
- [[log-partition-function]] (new) — $A(\theta)$, the normalizer in the exponent (p. 211)
- [[sigmoid]] (new) — map $\theta\mapsto\mu=1/(1+e^{-\theta})$ from natural to Bernoulli parameter (p. 213)
- [[change-of-variables]] (new) — $f(y)=f_x(U^{-1}(y))\,|\det \partial U^{-1}/\partial y|$ (p. 219)
- [[probability-integral-transform]] (new) — $F_X(X)$ is uniform (p. 216)
- [[determinant]] — here the Jacobian determinant measures volume change of the inverse map (p. 219)

## Canonical instances
- [[beta-binomial-conjugacy]] — Beta prior + Binomial data → Beta$(h+\alpha,N-h+\beta)$ (p. 208)
- [[beta-bernoulli-conjugacy]] — Beta prior + one Bernoulli observation (p. 209)
- [[gaussian-conditioning-example]] — Example 6.6: $p(x_1|x_2=-1)=\mathcal N(0.6,0.1)$ (p. 200)
- [[gaussian-as-exponential-family]] — $\phi(x)=(x,x^2)$, $\theta=(\mu/\sigma^2,-1/2\sigma^2)$ (p. 212)
- [[bernoulli-as-exponential-family]] — $\theta=\log\frac\mu{1-\mu}$, giving the sigmoid (p. 212)
- [[square-of-pdf-3x2]] — Example 6.16: $f(x)=3x^2$, $Y=X^2$ gives $f(y)=\tfrac32y^{1/2}$ (p. 216)
- [[linear-map-of-standard-gaussian]] — Example 6.17: density of $Y=AX$, covariance $AA^\top$ (p. 219)

## Bridges (candidates)
- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link).
- [same-math] $y=Ax$ gives covariance $A\Sigma A^\top$ ↔ linear-algebra: congruence/quadratic form $A\Sigma A^\top$ of a positive semi-definite matrix.
- [same-math] Cholesky sampling $\Sigma=AA^\top$ ↔ linear-algebra: Cholesky factorization of a symmetric positive definite matrix.
- [same-math] Jacobian determinant in (6.144) ↔ linear-algebra: determinant as signed volume scaling.
- [structural-analogy] Pseudo-inverse step (6.90) ↔ linear-algebra: least-squares normal equations $A^\top Ax=A^\top y$ — the same expression, used here to invert a Gaussian mean map.
- [structural-analogy] Conjugate update as parameter-counting (Beta$(\alpha+h,\beta+N-h)$) ↔ network science: updating link-probability beliefs from observed edges (our suggestion, not in the text).

## Questions this raises
- If conditioning only needs (6.66)–(6.67), how does the cost of computing $\Sigma_{yy}^{-1}$ scale in Gaussian processes with many observations?
- Which priors are conjugate for a Gaussian likelihood when both mean and variance are unknown, and what do Table 6.2's Gaussian/inverse-Gamma entries look like concretely?
- What is the relationship between concavity of the exponential-family log-likelihood and the convexity tools of Chapter 7?
- How does the change-of-variables formula extend to non-invertible maps, such as $y=x^2$ for $x\in\mathbb R$?

## Exercises worth doing
- Ex. 6.3 (p. 222) — choose a conjugate prior for a Bernoulli compile/no-compile model and compute $p(\mu|x_1,\dots,x_N)$; practises the Beta update — difficulty: easy
- Ex. 6.8 (p. 223) — write the Bernoulli in natural-parameter exponential-family form (compare Example 6.14) — difficulty: easy
- Ex. 6.10 (p. 223) — derive the product-of-Gaussians formulas (6.74)–(6.76) by completing the square and via the exponential-family form — difficulty: hard
- Ex. 6.12 (pp. 223–224) — linear-Gaussian model $y=Ax+b+w$, measurement $z=Cy+v$, then the posterior $p(x|\hat y)$ by Gaussian conditioning; combines §6.5.1 and §6.5.3 — difficulty: hard
- Ex. 6.13 (p. 224) — prove the probability integral transform (Theorem 6.15) — difficulty: medium
- Ex. 6.4 (p. 222) — Bayes' theorem with a biased coin choosing between two bags of fruit — difficulty: easy

## Reading notes
- **Where this part starts and ends:** it starts on printed p. 197, inside the closing remark of the previous section (distances between distributions, information geometry), then §6.5. It runs through §6.6, §6.7, §6.8 and the Exercises, ending on printed p. 224 (Exercise 6.13). The part begins in the middle of the last remark of the previous section, so the first page is a continuation; the unit metadata describes the split as a section boundary.
- **Page offset:** printed = pdf − 6. Printed numbers are visible on every page.
- **Edition as printed:** running footers read "Draft (2024-01-15) of 'Mathematics for Machine Learning'" and "©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020)".
- **Possible misprint, (6.122)→(6.123) (p. 214):** with $h_c(\mu)=\mu/(1-\mu)$ as printed, the product of $h_c$ and the exponential is $\mu^{\alpha+1}(1-\mu)^{\beta-1}$ (arithmetic check of ours), not (6.123). Obtaining (6.123)–(6.124) from the printed exponent would require $h_c(\mu)=1/(\mu(1-\mu))$. The conclusion (Beta form) agrees with Example 6.12 and (6.98).
- **Notation clash (p. 201):** the symbol $c$ denotes both the new mean vector and the scalar constant in "$c\,\mathcal N(x|c,C)$". The text distinguishes them only by context.
- **Forward reference:** p. 203 uses Example 6.17 (p. 219) to justify "any affine transformation of a Gaussian is Gaussian".
- **(6.139):** the printed text writes $F_y(y)$ with lowercase subscript; it means $F_Y$.
- **Exercise 6.1 table (p. 222):** the image shows a 3×5 grid with rows $y_1,y_2,y_3$ and columns $x_1,\dots,x_5$; the text layer matches it.
- **OCR:** the text layer was legible. All equations were checked against the page images.
- **Skipped or not derived in the source:** the Gaussian conditioning formulas (6.65)–(6.67) are cited to Bishop (2006) without derivation. Theorem 6.14 is stated without proof. Theorem 6.15 is left as Exercise 6.13, and Theorem 6.16 is not proved beyond the univariate derivation in §6.7.2.
- **Exercises:** 13 problems printed in these pages; solutions are not printed there.
