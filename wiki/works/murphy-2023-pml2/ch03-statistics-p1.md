---
id: murphy-2023-pml2/ch03-statistics-p1
work: murphy-2023-pml2
unit: "3 Statistics (part 1/3): 3.1 Introduction, 3.2 Bayesian statistics, 3.3 Frequentist statistics (to the start of 3.3.6)"
pages: 63–82
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Statistics, part 1: Bayesian inference, frequentist sampling distributions, Fisher information

## L0 — One line
Statistics infers parameters from data; the Bayesian way conditions on the observed data and integrates over parameter uncertainty, while the frequentist way studies how estimators vary across hypothetical repeated datasets, which produces counterintuitive quantities such as confidence intervals and p-values.

## L1 — The gist (≤ 120 words)
The unit asks how to infer unknown parameters θ from data D, i.e. compute p(θ|D). It works the Bayesian answer through the beta–Bernoulli coin model: posterior, MAP (posterior mode), mean, variance, credible intervals, predictive distribution and marginal likelihood. It then explains why integrating over parameters gives a fuller account of predictive uncertainty than plugging in a point estimate does. De Finetti's theorem ties priors to exchangeability. The frequentist side covers sampling distributions, the bootstrap, asymptotic normality of the MLE and the Fisher information matrix. Murphy argues that confidence intervals and p-values behave counterintuitively, since they do not condition on the observed data.

**Prerequisites:** Bayes' rule; beta and binomial distributions; expectation and variance; partial derivatives and Hessians; basic matrix notation; the exponential family (Chapter 2).

## L2 — Key ideas
- Bayesian inference treats θ as unknown and D as fixed, and computes the posterior p(θ|D) ∝ p(θ)p(D|θ) (p. 63).
- In the beta–Bernoulli model the Beta prior is conjugate (the posterior has the same functional form as the prior). Hyper-parameters (the prior's own parameters) act as pseudocounts, and the posterior mean is a convex combination of prior mean and the MLE (maximum-likelihood estimate) (pp. 64–66).
- Integrating over the posterior (the posterior predictive) reduces the chance of the overfitting that the plugin approximation (plugging in a point estimate such as the MLE) can suffer from. Laplace's rule of succession is an example (pp. 68–69).
- Predictive uncertainty has an aleatoric part (intrinsic noise) and an additional epistemic part (from not knowing the parameters). In Murphy's regression example the plugin approach captures only the first (pp. 70–71).
- De Finetti: if a sequence is infinitely exchangeable, there exist a parameter, a likelihood and a prior that make the data iid given θ (p. 72).
- Frequentist uncertainty is the sampling distribution of an estimator, approximated by the bootstrap or by asymptotic normality with the Fisher information as precision (pp. 73–75).
- The Fisher information is the covariance of the score. It equals the expected Hessian of the NLL (negative log-likelihood) under regularity conditions, and for exponential families, with respect to the natural parameters, it equals Cov[T(x)] (pp. 76–79).
- Frequentist confidence intervals and p-values do not give the probability statements people want. Murphy gives examples where they mislead (pp. 80–82).

## L3 — Walkthrough

### 3.1 Introduction (p. 63)
Probability theory models p(D|θ) for known θ. Statistics is the inverse problem: compute p(θ|D) (once called inverse probability theory). The two main approaches are frequentist and Bayesian. Most of the book is Bayesian (p. 63).

### 3.2 Bayesian statistics (p. 63)
θ is treated as unknown and D as fixed and known. Bayes' rule gives the posterior:
$$p(\theta|\mathcal D)=\frac{p(\theta)p(\mathcal D|\theta)}{p(\mathcal D)}=\frac{p(\theta)p(\mathcal D|\theta)}{\int p(\theta')p(\mathcal D|\theta')d\theta'}\tag{3.1}$$
- p(θ) is the prior (beliefs before data).
- p(D|θ) is the likelihood (what data we expect for each θ).
- p(θ|D) is the posterior (beliefs after data).
- p(D) is the marginal likelihood or evidence, a normalizing constant.

Computing the posterior is called Bayesian (or posterior) inference (p. 63).

#### 3.2.1 Tossing coins (p. 64)
Let θ∈[0,1] be the chance of heads (Y=1). Data: D={y_n∈{0,1}: n=1:N}. Goal: p(θ|D).

**3.2.1.1 Likelihood.** Assume iid (independent, identically distributed) tosses:
$$p(\mathcal D|\theta)=\prod_{n=1}^N\theta^{y_n}(1-\theta)^{1-y_n}=\theta^{N_1}(1-\theta)^{N_0}\tag{3.2}$$
with $N_1=\sum_n \mathbb I(y_n=1)$ and $N_0=\sum_n\mathbb I(y_n=0)$ (heads and tails). These counts are the sufficient statistics (all we need from D to infer θ). N=N₀+N₁ is the sample size. If we instead observe only the number of heads y in N trials, the likelihood is
$$p(\mathcal D|\theta)=\mathrm{Bin}(y|N,\theta)=\binom Ny\theta^y(1-\theta)^{N-y}\tag{3.3}$$
The factor $\binom Ny$ does not depend on θ, so inferences about θ are the same as for (3.2) (p. 64).

**3.2.1.2 Prior.** An uninformative prior (knowing only θ∈[0,1]) is uniform:
$$p(\theta)=\mathrm{Unif}(\theta|0,1)\tag{3.4}$$
More generally use a beta prior, with hyper-parameters $\breve\alpha,\breve\beta$ (parameters of the prior):
$$p(\theta)=\mathrm{Beta}(\theta|\breve\alpha,\breve\beta)\propto\theta^{\breve\alpha-1}(1-\theta)^{\breve\beta-1}\tag{3.5}$$
Setting $\breve\alpha=\breve\beta=1$ recovers the uniform prior (p. 64). The hyper-parameters can be seen as pseudocounts, analogous to $N_1,N_0$. The prior's strength is the equivalent sample size $\breve N=\breve\alpha+\breve\beta$ (p. 65).

**3.2.1.3 Posterior.** Multiply likelihood by prior:
$$p(\theta|\mathcal D)\propto\theta^{N_1}(1-\theta)^{N_0}\theta^{\breve\alpha-1}(1-\theta)^{\breve\beta-1}\propto\mathrm{Beta}(\theta|\breve\alpha+N_1,\breve\beta+N_0)=\mathrm{Beta}(\theta|\widehat\alpha,\widehat\beta)\tag{3.6}$$
with $\widehat\alpha\triangleq\breve\alpha+N_1$ and $\widehat\beta\triangleq\breve\beta+N_0$. Posterior and prior have the same functional form, so the prior is called conjugate (see Section 3.4) (p. 65).

Example (Fig. 3.1): $N_1=4,N_0=1$.
- Uniform prior: the posterior is Beta(5,2), with the same shape as the likelihood.
- Weak prior $\breve\alpha=\breve\beta=2$: the posterior is Beta(6,3), a "compromise" between prior and likelihood (p. 65).

**3.2.1.4 Posterior mode (MAP).**
$$\hat\theta_{\rm map}=\arg\max_\theta p(\theta|\mathcal D)=\arg\max_\theta\log p(\theta)+\log p(\mathcal D|\theta)\tag{3.7}$$
$$\hat\theta_{\rm map}=\frac{\breve\alpha+N_1-1}{\breve\alpha+N_1-1+\breve\beta+N_0-1}\tag{3.8}$$
(Murphy says "using calculus, one can show" this, with no derivation.) With a uniform prior, log p(θ)=0 and the MAP becomes the MLE:
$$\hat\theta_{\rm mle}=\arg\max_\theta\log p(\mathcal D|\theta)=\frac{N_1}{N_1+N_0}=\frac{N_1}{N}\tag{3.9}$$
The MLE can be very misleading with small samples. If N₁=0, it gives θ̂=0 and predicts no future heads. A MAP estimate with a stronger prior can fix this. With Beta(2,2):
$$\hat\theta_{\rm map}=\frac{N_1+1}{N_1+1+N_0+1}=\frac{N_1+1}{N+2}\tag{3.10}$$
This is called add-one smoothing (p. 66).

**3.2.1.5 Posterior mean.** The mode picks one point, so it can be a poor summary. The mean $\overline\theta=\int\theta p(\theta|\mathcal D)d\theta$ is, per Murphy, a "more robust" estimate. For the beta posterior:
$$\overline\theta\triangleq\mathbb E[\theta|\mathcal D]=\frac{\widehat\alpha}{\widehat\beta+\widehat\alpha}=\frac{\widehat\alpha}{\widehat N}\tag{3.11}$$
with $\widehat N=\widehat\alpha+\widehat\beta$ the posterior equivalent sample size. Writing the prior mean as $m=\breve\alpha/\breve N$:
$$\mathbb E[\theta|\mathcal D]=\frac{\breve\alpha+N_1}{\breve\alpha+N_1+\breve\beta+N_0}=\frac{\breve N m+N_1}{N+\breve N}\tag{3.12}$$
$$=\frac{\breve N}{N+\breve N}m+\frac{N}{N+\breve N}\frac{N_1}{N}=\lambda m+(1-\lambda)\hat\theta_{\rm mle}\tag{3.13}$$
Here $\lambda=\breve N/\widehat N$ is the ratio of prior to posterior equivalent sample size. The weaker the prior, the smaller λ, and the closer the posterior mean is to the MLE (p. 66).

*Intuition note:* The pseudocounts $\breve\alpha,\breve\beta$ behave like imaginary extra tosses added to the real ones. The posterior mean is then a weighted average of prior mean and observed frequency, weighted by how many (imaginary and real) tosses each represents.

**3.2.1.6 Posterior variance.** The standard error is the posterior standard deviation, $\mathrm{se}(\theta)=\sqrt{\mathbb V[\theta|\mathcal D]}$ (3.14). For the beta posterior (p. 67):
$$\mathbb V[\theta|\mathcal D]=\frac{\widehat\alpha\widehat\beta}{(\widehat\alpha+\widehat\beta)^2(\widehat\alpha+\widehat\beta+1)}=\frac{(\breve\alpha+N_1)(\breve\beta+N_0)}{(\breve\alpha+N_1+\breve\beta+N_0)^2(\breve\alpha+N_1+\breve\beta+N_0+1)}\tag{3.15}$$
If $N\gg\breve\alpha+\breve\beta$:
$$\mathbb V[\theta|\mathcal D]\approx\frac{N_1N_0}{(N_1+N_0)^2(N_1+N_0)}=\frac{N_1}{N}\frac{N_0}{N}\frac1N=\frac{\hat\theta(1-\hat\theta)}{N}\tag{3.16}$$
$$\sigma\approx\sqrt{\hat\theta(1-\hat\theta)/N}\tag{3.17}$$
with $\hat\theta=N_1/N$ the MLE. Uncertainty falls like $1/\sqrt N$. It is largest at θ̂=0.5 and smallest near 0 or 1, so it is easier to be sure a coin is biased than that it is fair (p. 67).

**3.2.1.7 Credible intervals.** A 100(1−α)% credible interval is a contiguous region C=(ℓ,u) holding 1−α of the posterior mass:
$$C_\alpha(\mathcal D)=(\ell,u):P(\ell\le\theta\le u|\mathcal D)=1-\alpha\tag{3.18}$$
Many intervals satisfy this. The central interval puts (1−α)/2 mass in each tail: ℓ=F⁻¹(α/2), u=F⁻¹(1−α/2), where F is the posterior cdf. For a N(0,1) posterior and α=0.05 this gives ±1.96, which justifies quoting μ±2σ (p. 67).

A central interval can exclude points with higher density than points inside it (Fig. 3.2a). The highest posterior density (HPD) region fixes this: find the density threshold p* with
$$1-\alpha=\int_{\theta:p(\theta|\mathcal D)>p^*}p(\theta|\mathcal D)d\theta\tag{3.19}$$
$$C_\alpha(\mathcal D)=\{\theta:p(\theta|\mathcal D)\ge p^*\}\tag{3.20}$$
In 1d it is called a highest density interval (HDI). For a Beta(3,9) posterior, the central interval is (0.06,0.52) and the 95% HDI is (0.04,0.48). The HDI is narrower, still holds 95% of the mass, and every point inside has higher density than every point outside (p. 68).

**3.2.1.8 Posterior predictive.** To predict future y, marginalize out the parameters:
$$p(\boldsymbol y|\mathcal D)=\int p(\boldsymbol y|\boldsymbol\theta)p(\boldsymbol\theta|\mathcal D)d\boldsymbol\theta\tag{3.21}$$
This can be hard, so a common approximation plugs in a point estimate $\hat{\boldsymbol\theta}=\delta(\mathcal D)$ (MLE or MAP):
$$p(\boldsymbol y|\mathcal D)\approx p(\boldsymbol y|\hat{\boldsymbol\theta})\tag{3.22}$$
This is the plugin approximation. It equals modelling the posterior as a Dirac delta, $p(\boldsymbol\theta|\mathcal D)\approx\delta(\boldsymbol\theta-\hat{\boldsymbol\theta})$ (3.23). This follows from the sifting property:
$$p(\boldsymbol y|\mathcal D)=\int p(\boldsymbol y|\boldsymbol\theta)\delta(\boldsymbol\theta-\hat{\boldsymbol\theta})d\boldsymbol\theta=p(\boldsymbol y|\hat{\boldsymbol\theta})\tag{3.24}$$
(p. 68). The plugin approximation can overfit. After N=3 heads in a row, the MLE θ̂=1 predicts tails are impossible (p. 69). The exact predictive for the beta posterior is
$$p(y=1|\mathcal D)=\int_0^1\theta\,\mathrm{Beta}(\theta|\widehat\alpha,\widehat\beta)d\theta=\mathbb E[\theta|\mathcal D]=\frac{\widehat\alpha}{\widehat\alpha+\widehat\beta}\tag{3.25–3.26}$$
With a uniform prior this gives Laplace's rule of succession:
$$p(y=1|\mathcal D)=\frac{N_1+1}{N_1+N_0+2}\tag{3.27}$$
This equals plugging in the add-one estimate (3.10), but that estimate came from the "rather unnatural" Beta(2,2) prior, whereas here the prior is uniform (p. 69).

**3.2.1.9 Marginal likelihood.**
$$p(\mathcal D|\mathcal M)=\int p(\boldsymbol\theta|\mathcal M)p(\mathcal D|\boldsymbol\theta,\mathcal M)d\boldsymbol\theta\tag{3.28}$$
It can be ignored when inferring θ within one model, since it is constant in θ. It matters for choosing between models (Section 3.8.1) and for estimating hyper-parameters (empirical Bayes, Section 3.7) (p. 69). For the beta–Bernoulli model, with $B$ the beta function:
$$p(\theta|\mathcal D)=\frac{p(\mathcal D|\theta)p(\theta)}{p(\mathcal D)}=\frac1{p(\mathcal D)}\big[\theta^{N_1}(1-\theta)^{N_0}\big]\Big[\frac1{B(\breve\alpha,\breve\beta)}\theta^{\breve\alpha-1}(1-\theta)^{\breve\beta-1}\Big]\tag{3.29}$$
$$=\frac1{p(\mathcal D)}\frac1{B(\breve\alpha,\breve\beta)}\big[\theta^{\breve\alpha+N_1-1}(1-\theta)^{\breve\beta+N_0-1}\big]=\frac1{B(\widehat\alpha,\widehat\beta)}\big[\theta^{\widehat\alpha}(1-\theta)^{\widehat\beta}\big]\tag{3.30}$$
(The printed last bracket omits the "−1" exponents, as in the source.) Equating the normalizing constants (added step): $\frac1{p(\mathcal D)B(\breve\alpha,\breve\beta)}=\frac1{B(\widehat\alpha,\widehat\beta)}$, so $p(\mathcal D)=B(\widehat\alpha,\widehat\beta)/B(\breve\alpha,\breve\beta)$ (p. 70). For the Jeffreys prior $\breve\alpha=\breve\beta=\tfrac12$ (Eq. 3.225, outside this part) this is the Krichevski–Trofimov (KT) estimator:
$$p(\mathcal D)=\frac{B(\widehat\alpha,\widehat\beta)}{B(\breve\alpha,\breve\beta)}=\frac{\Gamma(N_1+\frac12)\Gamma(N_0+\frac12)}{\Gamma(N_1+N_0+\frac12+\frac12)}\frac{\Gamma(\frac12+\frac12)}{\Gamma(\frac12)\Gamma(\frac12)}=\frac1\pi B\Big(N_1+\frac12,N_0+\frac12\Big)\tag{3.31}$$
using $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$, Γ(1)=1 and $\Gamma(\frac12)=\sqrt\pi$ (p. 70).

#### 3.2.2 Modeling more complex data (pp. 70–71)
For inputs x and outputs y, use p(y|x,θ) (a generalized linear model, a neural net, etc.). The main object is
$$p(\boldsymbol y|\boldsymbol x,\mathcal D)=\int p(\boldsymbol y|\boldsymbol x,\boldsymbol\theta)p(\boldsymbol\theta|\mathcal D)d\boldsymbol\theta\tag{3.32}$$
Integrating out parameters reduces the chance of overfitting, since it is a weighted average over an infinite number of models. Murphy notes that regularization methods also need a prior, so having a prior does not distinguish the Bayesian approach (p. 70). The plugin version is $p(\boldsymbol y|\boldsymbol x,\hat{\boldsymbol\theta})$ (3.33). It ignores parameter uncertainty and can underestimate predictive uncertainty. In linear regression with MLE-plugin, the predicted variance is the constant $\hat\sigma^2$ (Fig. 3.3a). That uncertainty is aleatoric (intrinsic) and would persist even if the true parameters were known. Not knowing the parameters adds an orthogonal epistemic uncertainty (from lack of knowledge). The Bayesian predictive (Fig. 3.3b) has error bars that widen away from the training data. Footnote 2 defines epistemic uncertainty as the mutual information I(θ;y)=H(y)−H(y|θ), i.e. total minus aleatoric uncertainty (p. 71).

*Intuition note:* A plugin predictor bets everything on one parameter value. The Bayesian predictor averages over all plausible values, so it becomes less sure where the data say little.

#### 3.2.3–3.2.4 Prior selection and computation (pp. 71–72)
Specifying a prior can be hard in large models. Later sections cover conjugate priors (3.4), uninformative priors (3.5), hierarchical priors (3.6) and empirical priors (3.7). Computing the posterior or predictive can be expensive. Approximate methods are in Section 7.4 and Part II (pp. 71–72).

#### 3.2.5 Exchangeability and de Finetti's theorem (p. 72)
Priors refer to abstract parameters, so where do they come from? A sequence $(\boldsymbol x_1,\boldsymbol x_2,\dots)$ is infinitely exchangeable if, for any n and permutation π,
$$p(\boldsymbol x_1,\dots,\boldsymbol x_n)=p(\boldsymbol x_{\pi_1},\dots,\boldsymbol x_{\pi_n})\tag{3.34}$$
Exchangeability is more general than iid. Murphy's example: images $x_i\sim p^*$ drawn independently are iid. With a shared background image $x_0$, the sequence $(x_0+x_1,\dots,x_0+x_n)$ is infinitely exchangeable but not iid, since all terms share the hidden factor $x_0$. The more examples we see, the better we can estimate $x_0$.

**Theorem 3.2.1 (de Finetti).** A sequence is infinitely exchangeable iff, for all n,
$$p(\boldsymbol x_1,\dots,\boldsymbol x_n)=\int\prod_{i=1}^np(\boldsymbol x_i|\boldsymbol\theta)p(\boldsymbol\theta)d\boldsymbol\theta\tag{3.35}$$
where θ is a hidden common random variable (possibly infinite-dimensional); the $x_i$ are iid given θ. So if data are exchangeable, a parameter, a likelihood and a prior must exist. Murphy concludes that the Bayesian approach "follows automatically from exchangeability" (citing [O'N09]). Partial exchangeability extends this to conditional models (p. 72).

*Intuition note:* An exchangeable sequence behaves as if a hidden cause were drawn first and the data then drawn independently given that cause. The prior is a belief about this hidden cause.

### 3.3 Frequentist statistics (pp. 72–73)
Frequentist (classical, orthodox) statistics tries to avoid treating parameters as random variables, and so avoids priors and Bayes' rule. Uncertainty is measured by how a data-derived quantity would change if the data changed, i.e. variation across repeated trials. The Bayesian view treats probability as information, which allows probabilities of one-off events (Murphy's example: the polar ice cap melting by 2030). Murphy says the Bayesian approach avoids certain paradoxes of the frequentist one (Section 3.3.5). Frequentist ideas such as cross validation, model checking and conformal prediction remain useful to Bayesians (p. 73).

#### 3.3.1 Sampling distributions (p. 73)
An estimator is a decision procedure from data to action; for parameters, $\hat{\boldsymbol\theta}=\hat\Theta(\mathcal D)$ (MLE, MAP, method of moments). Its sampling distribution is the distribution of $\hat{\boldsymbol\theta}$ over datasets drawn from a true model. Draw S datasets of size N:
$$\tilde{\mathcal D}^{(s)}=\{\boldsymbol x_n\sim p(\boldsymbol x_n|\boldsymbol\theta^*):n=1:N\}\tag{3.36}$$
(written $\tilde{\mathcal D}^{(s)}\sim\boldsymbol\theta^*$). Apply the estimator to each. As S→∞:
$$p(\hat\Theta(\tilde{\mathcal D})=\boldsymbol\theta|\tilde{\mathcal D}\sim\boldsymbol\theta^*)\approx\frac1S\sum_{s=1}^S\delta(\boldsymbol\theta-\hat\Theta(\tilde{\mathcal D}^{(s)}))\tag{3.37}$$
It can be approximated by Monte Carlo (3.3.2) or sometimes computed analytically (3.3.3) (p. 73).

#### 3.3.2 Bootstrap (pp. 73–75)
The bootstrap approximates the sampling distribution when the estimator is complex or N is small. Since θ* is unknown:
- **Parametric bootstrap:** generate datasets from $p(\boldsymbol x|\hat{\boldsymbol\theta})$ with $\hat{\boldsymbol\theta}=\hat\Theta(\mathcal D)$, instead of θ*. This is a plugin approximation to the sampling distribution (p. 74).
- **Non-parametric bootstrap:** resample N points from D with replacement. A bootstrap sample contains on average only 0.632N unique points, because the chance an item is picked at least once is $1-(1-1/N)^N\to1-e^{-1}\approx0.632$ (p. 74).

Fig. 3.4 (data from Ber(0.7), B=10,000 bootstrap samples). For N=10 the sampling distribution of the MLE is asymmetric and far from Gaussian. For N=100 it looks more Gaussian (p. 75). Posterior samples under a uniform prior look similar. Conceptually they differ, but when the estimator is the MLE and the prior is not strong they can be similar, so the bootstrap distribution is a "poor man's" posterior. The bootstrap can be slower than posterior sampling, since it fits a model to each of S datasets whereas posterior sampling fits once (p. 75).

#### 3.3.3 Asymptotic normality of the MLE (p. 75)
**Theorem 3.3.1.** Under various technical conditions,
$$\sqrt N(\hat{\boldsymbol\theta}-\boldsymbol\theta^*)\to\mathcal N(\mathbf 0,\mathbf F(\boldsymbol\theta^*)^{-1})\tag{3.38}$$
where F is the Fisher information matrix (3.40), θ* are the true data-generating parameters, and → is convergence in distribution. F measures the curvature of the log-likelihood at θ*. Murphy's reading: the sampling distribution of the MLE converges to a Gaussian centred on the true parameter, with precision given by the Fisher information. A peaked likelihood means the parameters are well determined and the estimates vary little across datasets (p. 75).

*Intuition note:* A sharply peaked log-likelihood means the data pin the parameter down. So the MLE moves little from dataset to dataset. The $\sqrt N$ scaling in (3.38) suggests that the spread of the MLE around $\theta^*$ shrinks at rate $1/\sqrt N$ (our reading of the formula).

#### 3.3.4 Fisher information matrix (pp. 75–79)
Uses: the MLE's sampling distribution, Jeffreys priors (3.5.2) and natural gradient descent (6.4) (p. 75).

**3.3.4.1 Definition.** The score function is the gradient of the log likelihood, $s(\boldsymbol\theta)\triangleq\nabla_{\boldsymbol\theta}\log p(\boldsymbol x|\boldsymbol\theta)$ (3.39). The Fisher information matrix is the covariance of the score:
$$\mathbf F(\boldsymbol\theta)\triangleq\mathbb E_{\boldsymbol x\sim p(\boldsymbol x|\boldsymbol\theta)}\big[\nabla\log p(\boldsymbol x|\boldsymbol\theta)\nabla\log p(\boldsymbol x|\boldsymbol\theta)^\top\big]\tag{3.40}$$
$$F_{ij}=\mathbb E_{\boldsymbol x\sim\boldsymbol\theta}\Big[\Big(\tfrac{\partial}{\partial\theta_i}\log p(\boldsymbol x|\boldsymbol\theta)\Big)\Big(\tfrac{\partial}{\partial\theta_j}\log p(\boldsymbol x|\boldsymbol\theta)\Big)\Big]\tag{3.41}$$
(p. 76).

**3.3.4.2 FIM equals the expected Hessian of the NLL.** With $\mathrm{NLL}(\boldsymbol\theta)=-\log p(\mathcal D|\boldsymbol\theta)$ (3.42), the Hessian measures curvature. A flat likelihood tells us nothing about the parameters; a delta-function likelihood determines them uniquely (p. 76).

**Theorem 3.3.2.** If log p(x|θ) is twice differentiable, and under certain regularity conditions,
$$\mathbf F(\boldsymbol\theta)_{ij}=\mathbb E\Big[\tfrac{\partial}{\partial\theta_i}\log p\,\tfrac{\partial}{\partial\theta_j}\log p\Big]=-\mathbb E\Big[\tfrac{\partial^2}{\partial\theta_i\partial\theta_j}\log p(\boldsymbol x|\boldsymbol\theta)\Big]\tag{3.43}$$
**Lemma 3.3.1.** $\mathbb E_{p(\boldsymbol x|\boldsymbol\theta)}[\nabla\log p(\boldsymbol x|\boldsymbol\theta)]=\mathbf 0$ (3.44).

*Proof (scalar case).* Since $\int p(x|\theta)dx=1$, we have $\frac{\partial}{\partial\theta}\int p(x|\theta)dx=0$ (3.45). Using the identity $\frac{\partial}{\partial\theta}p=\big[\frac{\partial}{\partial\theta}\log p\big]p$ (3.46):
$$0=\int\frac{\partial}{\partial\theta}p(x|\theta)dx=\int\Big[\frac{\partial}{\partial\theta}\log p(x|\theta)\Big]p(x|\theta)dx=\mathbb E[s(\theta)]\tag{3.47}$$
*Proof of Theorem (scalar).* Differentiate (3.47):
$$0=\frac\partial{\partial\theta}\int\Big[\frac\partial{\partial\theta}\log p\Big]p\,dx\tag{3.48}$$
$$=\int\Big[\frac{\partial^2}{\partial\theta^2}\log p\Big]p\,dx+\int\Big[\frac\partial{\partial\theta}\log p\Big]\frac\partial{\partial\theta}p\,dx\tag{3.49}$$
$$=\int\Big[\frac{\partial^2}{\partial\theta^2}\log p\Big]p\,dx+\int\Big[\frac\partial{\partial\theta}\log p\Big]^2p\,dx\tag{3.50}$$
Hence $-\mathbb E[\partial^2_\theta\log p]=\mathbb E[(\partial_\theta\log p)^2]$ (3.51). For N iid samples the NLL Hessian is
$$H_{ij}\triangleq-\frac{\partial^2}{\partial\theta_i\partial\theta_j}\log p(\mathcal D|\boldsymbol\theta)=-\sum_{n=1}^N\frac{\partial^2}{\partial\theta_i\partial\theta_j}\log p(\boldsymbol x_n|\boldsymbol\theta)\tag{3.52}$$
so $\mathbb E_{p(\mathcal D|\boldsymbol\theta)}[\mathbf H(\mathcal D)|_{\boldsymbol\theta}]=N\mathbf F(\boldsymbol\theta)$ (3.53), which is used for the MLE's sampling distribution (p. 77).

**3.3.4.3 Binomial.** For x∼Bin(n,θ), the log likelihood is $l(\theta|x)=x\log\theta+(n-x)\log(1-\theta)$ (3.54). The score is $s=\frac x\theta-\frac{n-x}{1-\theta}$ (3.55) and $s'=-\frac x{\theta^2}-\frac{n-x}{(1-\theta)^2}$ (3.56). Using $\mathbb E[x]=n\theta$ (added step, implicit in the source's first term $n\theta/\theta^2$):
$$F(\theta)=\mathbb E[-s'(\theta|x)]=\frac{n\theta}{\theta^2}+\frac{n-n\theta}{(1-\theta)^2}=\frac n\theta+\frac n{1-\theta}=\frac n{\theta(1-\theta)}\tag{3.57}$$
(pp. 77–78).

**3.3.4.4 Univariate Gaussian**, θ=(μ,v):
$$\ell=-\frac1{2v}(x-\mu)^2-\frac12\log v-\frac12\log(2\pi)\tag{3.58}$$
$$\frac{\partial\ell}{\partial\mu}=(x-\mu)v^{-1},\quad\frac{\partial^2\ell}{\partial\mu^2}=-v^{-1}\tag{3.59}$$
$$\frac{\partial\ell}{\partial v}=\frac12v^{-2}(x-\mu)^2-\frac12v^{-1},\quad\frac{\partial^2\ell}{\partial v^2}=-v^{-3}(x-\mu)^2+\frac12v^{-2}\tag{3.60}$$
$$\frac{\partial^2\ell}{\partial\mu\partial v}=-v^{-2}(x-\mu)\tag{3.61}$$
$$\mathbf F(\boldsymbol\theta)=\begin{pmatrix}\mathbb E[v^{-1}]&\mathbb E[v^{-2}(x-\mu)]\\\mathbb E[v^{-2}(x-\mu)]&\mathbb E[v^{-3}(x-\mu)^2-\tfrac12v^{-2}]\end{pmatrix}=\begin{pmatrix}\frac1v&0\\0&\frac1{2v^2}\end{pmatrix}\tag{3.62}$$
(p. 78).

**3.3.4.5 ℓ₂-regularized logistic regression.** (added step: shapes implied by the formulas, not stated on the page: X is N×D, y is N, w is D.) The negative log joint is
$$\mathcal L(\boldsymbol w)=-\log[p(\boldsymbol y|\mathbf X,\boldsymbol w)p(\boldsymbol w|\lambda)]=-\boldsymbol w^\top\mathbf X^\top\boldsymbol y+\sum_{n=1}^N\log(1+e^{\boldsymbol w^\top\boldsymbol x_n})+\frac\lambda2\boldsymbol w^\top\boldsymbol w\tag{3.63}$$
$$\nabla_{\boldsymbol w}\mathcal L=-\mathbf X^\top\boldsymbol y+\mathbf X^\top\boldsymbol s+\lambda\boldsymbol w,\ \ s_n=\sigma(\boldsymbol w^\top\boldsymbol x_n)\tag{3.64}$$
$$\mathbf F(\boldsymbol w)=\mathbb E_{p(\boldsymbol y|\mathbf X,\boldsymbol w,\lambda)}[\nabla^2\mathcal L(\boldsymbol w)]=\mathbf X^\top\boldsymbol\Lambda\mathbf X+\lambda\mathbf I\tag{3.65}$$
with Λ the N×N diagonal matrix $\Lambda_{nn}=\sigma(\boldsymbol w^\top\boldsymbol x_n)(1-\sigma(\boldsymbol w^\top\boldsymbol x_n))$ (3.66) (p. 78).

**3.3.4.6 Exponential family**, natural parameters η, sufficient statistics $\mathcal T(\boldsymbol x)$. From Chapter 2:
$$\nabla_\eta A(\eta)=\mathbb E[\mathcal T(\boldsymbol x)]=\boldsymbol m\tag{3.67}$$
$$\nabla_\eta\log p(\boldsymbol x|\eta)=\mathcal T(\boldsymbol x)-\mathbb E[\mathcal T(\boldsymbol x)]\tag{3.68}$$
Hence
$$(\mathbf F_\eta)_{ij}=\mathbb E\Big[\frac{\partial\log p}{\partial\eta_i}\frac{\partial\log p}{\partial\eta_j}\Big]=\mathbb E[(\mathcal T_i-m_i)(\mathcal T_j-m_j)]=\mathrm{Cov}[\mathcal T_i,\mathcal T_j]\tag{3.69–3.71}$$
so $\mathbf F_\eta=\mathrm{Cov}[\mathcal T(\boldsymbol x)]$ (3.72). For the moment parameters m, $(\mathbf F_m)_{ij}=\mathbb E\big[\frac{\partial\log p(\boldsymbol x|\eta)}{\partial m_i}\frac{\partial\log p(\boldsymbol x|\eta)}{\partial m_j}\big]$ (3.73). The chain rule $\frac{\partial\log p}{\partial\alpha}=\frac{\partial\log p}{\partial\beta}\frac{\partial\beta}{\partial\alpha}$ (3.74) gives
$$\mathbf F_\alpha=\Big(\frac{\partial\boldsymbol\beta}{\partial\boldsymbol\alpha}\Big)^\top\mathbf F_\beta\frac{\partial\boldsymbol\beta}{\partial\boldsymbol\alpha}\tag{3.75}$$
The log trick $\nabla\mathbb E_{p}[f]=\mathbb E_p[f\nabla\log p]$ (3.76) with (3.68) gives
$$\frac{\partial m_i}{\partial\eta_j}=\mathbb E\Big[\mathcal T_i\frac{\partial\log p}{\partial\eta_j}\Big]=\mathbb E[\mathcal T_i(\mathcal T_j-m_j)]\tag{3.77}$$
$$=\mathbb E[\mathcal T_i\mathcal T_j]-\mathbb E[\mathcal T_i]m_j=\mathrm{Cov}[\mathcal T_i,\mathcal T_j]=(\mathbf F_\eta)_{ij}\tag{3.78}$$
So $\partial\eta/\partial m=\mathbf F_\eta^{-1}$ (3.79), and
$$\mathbf F_m=\Big(\frac{\partial\eta}{\partial m}\Big)^\top\mathbf F_\eta\frac{\partial\eta}{\partial m}=\mathbf F_\eta^{-1}\mathbf F_\eta\mathbf F_\eta^{-1}=\mathbf F_\eta^{-1}=\mathrm{Cov}[\mathcal T(\boldsymbol x)]^{-1}\tag{3.80}$$
(p. 79).

#### 3.3.5 Counterintuitive properties of frequentist statistics (pp. 80–82)
Murphy says the approach has "pathological properties" that lead to misunderstanding and misuse (p. 80).

**3.3.5.1 Confidence intervals.** A 100(1−α)% confidence interval is any interval I(D̃) derived from a hypothetical dataset such that
$$\Pr(\theta\in I(\tilde{\mathcal D})|\tilde{\mathcal D}\sim\theta)=1-\alpha\tag{3.81}$$
If we repeatedly sample data, about 95% of the 95% intervals contain the true θ (95% coverage). This does not mean that for a particular dataset θ∈I(D) with 95% probability. That is what a credible interval gives and what people usually want. Frequentists treat θ as a fixed unknown constant and data as random; Bayesians treat data as fixed and θ as random (p. 80).

Berger's example [Ber85a]: draw two integers from
$$p(y|\theta)=\begin{cases}0.5&y=\theta\\0.5&y=\theta+1\\0&\text{otherwise}\end{cases}\tag{3.82}$$
For θ=39 the outcomes (39,39), (39,40), (40,39), (40,40) each have probability 0.25 (3.83). Let m=min(y₁,y₂) and take the interval [m,m] (3.84). It gives [39,39], [39,39], [39,39], [40,40] (3.85), so it is a 75% CI. But if D=(39,40) is observed, p(θ=39|D)=1.0, so we know θ=39, yet the CI only claims 75% "confidence". Coverage over repeated datasets can be very misleading for a single dataset (p. 80). Murphy cites studies showing that many people, including professional statisticians, misunderstand and misuse CIs, whereas credible intervals do not suffer from these problems (p. 81).

**3.3.5.2 p-values.** Null hypothesis significance testing (NHST) decides whether to reject the null H₀ based on whether a test statistic t(D) is likely under the null's sampling distribution (Section 3.10.1). The p-value is
$$\mathrm{pval}(t(\mathcal D))\triangleq\Pr(t(\tilde{\mathcal D})\ge t(\mathcal D)|\tilde{\mathcal D}\sim H_0)\tag{3.86}$$
a tail probability under the sampling distribution. **Common interpretation (as Murphy reports it):** small values mean H₀ is unlikely and H₁ likely, via the reasoning: if H₀ is true this test statistic would probably not occur; it did occur; so H₀ is probably false. Murphy says this reasoning is invalid. His illustration, taken from [Coh94], runs: if a person is an American, he is probably not a member of Congress; this person is a member of Congress; therefore he is probably not an American. Murphy calls this obviously fallacious. By contrast, the argument 'if a person is a Martian, then he is not a member of Congress; this person is a member; therefore he is not a Martian' is, per Murphy, valid deduction (modus tollens: P⇒Q and ¬Q give ¬P). The American case is induction (reasoning backwards from evidence to probable causes), which needs probabilistic inference, i.e. Bayes' rule:
$$p(H_0|\mathcal D)=\frac{p(\mathcal D|H_0)p(H_0)}{p(\mathcal D|H_0)p(H_0)+p(\mathcal D|H_1)p(H_1)}\tag{3.87}$$
(p. 81). With p(H₀)=p(H₁)=0.5 and likelihood ratio LR=p(D|H₀)/p(D|H₁):
$$p(H_0|\mathcal D)=\frac{LR}{LR+1}\tag{3.88}$$
In the Congress example, p(D|H₀) is low, but p(D|H₁)=0 since only Americans can be members. So LR=∞ and p(H₀|D)=1.0. NHST ignores p(D|H₁) and the prior p(H₀), so it gives wrong results in many problems, not just this one. Even most scientists misinterpret p-values; The American Statistician ran a special issue warning against them, and several journals have banned them (p. 82).

**3.3.5.3 Discussion.** Murphy's diagnosis: these problems arise because frequentist inference does not condition on the observed data but relies on the estimator's sampling distribution, while people want conditional probability statements. He quotes Jim Berger: users want the probability, after seeing the data, that a hypothesis is true or that θ lies in an interval, and classical statistics substitutes "artificial concepts" such as error probabilities and coverage (p. 82).

**3.3.6 Why isn't everyone a Bayesian?** This part of the chapter ends at the start of this section. It opens with a George Box epigraph (1962) and mentions Efron's paper of that title, then announces a quote from Efron's opening section, which the page does not reproduce (p. 82).

## Toy example (ours, not from the text)
Coin data: N₁=4 heads, N₀=1 tail (as in Fig. 3.1).

*Uniform prior Beta(1,1):* posterior Beta(5,2).
- Mean: 5/7 ≈ 0.714.
- MAP = MLE = 4/5 = 0.8 (by 3.8: (1+4−1)/(1+4−1+1+1−1) = 4/5).
- Predictive p(y=1|D) = (4+1)/(4+1+2) = 5/7 (Laplace).
- Marginal likelihood of this particular sequence = B(5,2)/B(1,1) = Γ(5)Γ(2)/Γ(7) = 24·1/720 = 1/30. Check: ∫₀¹θ⁴(1−θ)dθ = 1/5 − 1/6 = 1/30.

*Prior Beta(2,2):* posterior Beta(6,3), N̆=4, N̂=9.
- Mean = 6/9 = 2/3.
- MAP = (2+4−1)/(2+4−1+2+1−1) = 5/7.
- λ = 4/9. Prior mean m=0.5, MLE=0.8, so λm+(1−λ)θ̂ = (4/9)(0.5)+(5/9)(0.8) = 2/9+4/9 = 6/9 ✓ (3.13).
- Variance (3.15) = (6·3)/(9²·10) = 18/810 ≈ 0.0222, so se ≈ 0.149.
- Predictive p(y=1|D) = 2/3.

The plugin MLE would predict 0.8. The Bayesian answers are pulled toward 0.5 by the prior, and more strongly when N̆ is larger.

## Concepts
- [[bayes-theorem]] — posterior = prior × likelihood / evidence, eq. (3.1) (p. 63)
- [[prior-distribution]] — beliefs about θ before data; here Beta(ᾰ,β̆) with hyper-parameters (p. 64)
- [[likelihood]] — p(D|θ); here Bernoulli/Binomial, proportional in θ (p. 64)
- [[posterior-distribution]] — p(θ|D), the full Bayesian answer (p. 63)
- [[marginal-likelihood]] — p(D|M), ratio of posterior to prior normalizers in beta–Bernoulli; KT estimator for the Jeffreys prior (pp. 69–70)
- [[conjugate-prior]] — prior whose posterior has the same functional form (p. 65)
- [[posterior-predictive-distribution]] — ∫p(y|θ)p(θ|D)dθ (p. 68)
- [[credible-interval]] — contiguous region with posterior mass 1−α; central or HPD (p. 67)
- [[exchangeability]] — joint invariant to permutation; de Finetti's theorem gives iid given hidden θ (p. 72)
- [[frequentist-vs-bayesian-inference]] — data random, θ fixed vs data fixed, θ random (p. 80)
- [[sufficient-statistics]] (new) — counts N₁,N₀ that are all we need from D to infer θ (p. 64)
- [[pseudocounts-equivalent-sample-size]] (new) — hyper-parameters as imaginary counts; N̆=ᾰ+β̆ is prior strength (p. 65)
- [[map-estimate]] (new) — posterior mode; equals the MLE under a uniform prior (p. 65)
- [[plugin-approximation]] (new) — predictive with θ̂ plugged in; equals a delta-function posterior (p. 68)
- [[laplace-rule-of-succession]] (new) — (N₁+1)/(N+2) under a uniform prior (p. 69)
- [[aleatoric-vs-epistemic-uncertainty]] (new) — intrinsic noise vs uncertainty from not knowing parameters (p. 70)
- [[sampling-distribution]] (new) — distribution of an estimator across datasets from the true model (p. 73)
- [[bootstrap]] (new) — Monte Carlo approximation of the sampling distribution; parametric or non-parametric (p. 74)
- [[asymptotic-normality-mle]] (new) — √N(θ̂−θ*)→N(0,F⁻¹) under technical conditions (p. 75)
- [[fisher-information]] (new) — covariance of the score; equals the expected NLL Hessian under regularity conditions (p. 76)
- [[confidence-interval]] (new) — interval with (3.81) coverage over repeated datasets, not a probability for θ given D (p. 80)
- [[p-value]] (new) — tail probability of the test statistic under H₀, eq. (3.86) (p. 81)

## Canonical instances
- [[beta-bernoulli-coin-model]] — running example of the full Bayesian pipeline (pp. 64–70)
- [[plugin-vs-bayes-polynomial-regression]] — constant-variance plugin vs widening Bayesian error bars (Fig. 3.3, pp. 70–71)
- [[background-image-exchangeable-sequence]] — exchangeable but not iid (p. 72)
- [[bootstrap-vs-posterior-bernoulli]] — Fig. 3.4 with Ber(0.7) data (p. 74)
- [[fim-binomial-gaussian-logistic]] — worked Fisher information calculations (pp. 77–78)
- [[berger-integer-ci-example]] — 75% CI that, for the observed D=(39,40), still leaves θ known with certainty (p. 80)
- [[congress-p-value-example]] — p-value reasoning fallacy vs Bayes with LR=∞ (pp. 81–82)

## Bridges (candidates)
- [same-math] Fisher information F_η=Cov[T(x)] ↔ exponential families: variance of sufficient statistics is the curvature of log A(η) — same objects, as in (3.67)–(3.72).
- [structural-analogy] Bootstrap distribution ↔ Bayesian posterior sampling: both give a cloud of parameter values, from refitting vs from conditioning (p. 75).
- [same-math] Plugin approximation ↔ posterior replaced by a Dirac delta: eq. (3.23)–(3.24).
- [structural-analogy] de Finetti's hidden common cause ↔ hierarchical models: shared latent θ makes observations conditionally iid (p. 72).
- [metaphor] Marginalizing over parameters ↔ ensembling: the text calls it a weighted average over infinitely many models (p. 70).

## Questions this raises
- When does the bootstrap distribution fail to resemble the posterior, e.g. with a strong or informative prior?
- Which "regularity conditions" in Theorems 3.3.1–3.3.2 can fail, and what happens to the MLE's behavior then?
- How should one choose a prior for a large model such as a neural net, where the coin-style uniform prior is not obvious (Sections 3.4–3.7)?
- If CIs and p-values are misleading, what in frequentist practice (cross validation, conformal prediction) does remain useful?

## Reading notes
- This part starts at the chapter opening (printed p. 63, 3.1 Introduction) and ends on printed p. 82, at the start of 3.3.6, just before Efron's quoted opening section. The unit was split at a section boundary.
- Printed page = pdf page − 34. Footers: even printed pages show "Online version. December 10, 2025"; odd printed pages show the author/license line.
- Misprints seen in the images:
  - Fig. 3.1 caption labels both panels "(a)"; the second should be "(b)".
  - (3.60) writes the second derivative as ∂ℓ/∂v² and (3.61) writes ∂ℓ/∂µ∂v, both without the square on ℓ (I wrote ∂²ℓ/∂v² and ∂²ℓ/∂µ∂v).
  - (3.78) writes Cov[T_i T_j]; this means Cov[T_i, T_j].
  - In (3.30) the last bracket shows exponents α̂, β̂ without "−1", as printed.
- Equation (3.8) is stated without derivation ("using calculus").
- The verbal gloss of Theorem 3.3.1 ("precision equal to the Fisher information") refers loosely to the √N-scaled formula (3.38).
- Cross-references to Sections 3.4–3.10, 3.225, 6.4, 7.4 and Chapter 15 point outside this part.
