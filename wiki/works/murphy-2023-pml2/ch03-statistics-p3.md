---
id: murphy-2023-pml2/ch03-statistics-p3
work: murphy-2023-pml2
unit: "Chapter 3 Statistics, part 3/3 (§3.6.2 end – §3.11: empirical Bayes, model selection, model checking, hypothesis testing, missing data)"
pages: 114-142
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Empirical Bayes, model selection and checking, hypothesis testing, missing data

## L0 — One line
In this part, the marginal likelihood (evidence) is used to set hyperparameters and compare models, predictive checks to find misfit, Bayes factors or posteriors over effect sizes to test hypotheses, and an explicit model of the missingness mechanism to handle incomplete data.

## L1 — The gist (≤ 120 words)
This part asks how to set hyperparameters, compare models, check models and test hypotheses in a Bayesian way. Empirical Bayes plugs a point estimate of the hyperparameters into a hierarchical model. Model selection uses the marginal likelihood (evidence), which penalizes flexibility automatically. It is hard to compute, so cross-validation, PSIS-LOO and information criteria (BIC, AIC, WAIC) serve as alternatives or approximations. Posterior predictive checks ask whether a model captures the features we care about. Many classical tests are inference in linear models, and Bayesian versions use posteriors rather than p-values. Finally, the missing-data mechanism (MCAR, MAR, MNAR) decides whether missing labels can be ignored.

**Prerequisites:** Bayes' rule; conjugate Beta–Binomial and Gaussian updating; marginal likelihood; Monte Carlo and importance sampling; Hessian and Gaussian (Laplace) approximation; linear regression/GLMs.

## L2 — Key ideas (5–10 bullets)
- Empirical Bayes (type II ML) estimates hyperparameters by maximizing the marginal likelihood, then conditions on them. It is cheap and less prone to overfit than ML, but it violates the principle that the prior is chosen independently of the data (p. 114).
- For equal group variances, EB for the hierarchical Gaussian model is closed-form and gives shrinkage with weight $\lambda=\sigma^2/(\sigma^2+\tau^2)$ (p. 116).
- The marginal likelihood implements a Bayesian Occam's razor. It is used for Bayesian model selection and Bayes model averaging, and it can be estimated analytically or by Monte Carlo and variational methods. The harmonic mean estimator is a bad choice (pp. 119–122).
- Log marginal likelihood is a sum of sequential predictive terms, which links it to cross-validation. The conditional marginal likelihood is much more predictive of generalization than the LML, and PSIS-LOO is a fast approximation to the LOO estimate of predictive performance (pp. 123–125).
- BIC, AIC, MDL and WAIC score a model by fit plus a complexity penalty. BIC comes from a Gaussian approximation to the evidence, and WAIC also works for singular models (pp. 126–127).
- Posterior predictive checks and Bayesian p-values test whether the model reproduces chosen features of the data. The aim is not to ask whether the data "come from" the model (pp. 128–131).
- Bayesian hypothesis testing can use Bayes factors (sensitive to priors; improper priors give the marginalization paradox) or posterior estimation of effect sizes (ROPE, credible intervals) (pp. 132–135).
- Many common tests, parametric and (via rank transforms) nonparametric ones, can be written exactly or approximately as inference in linear models and GLMs (pp. 136–140).
- MCAR, MAR and MNAR missingness decide whether unlabeled outputs can be ignored in discriminative models. A generative model can use unlabeled data even under MCAR and MAR (pp. 141–142).

## L3 — Walkthrough

### 3.6.2 (end) and 3.6.3 Reparameterization; hierarchical conditional models
Writing $\theta_j$ as a function of its parents plus a local noise term reduces dependence between $\theta_j$ and $\tau$, and hence among the other $\theta_k$. This can make inference algorithms more efficient (Section 12.6.5) and is widely used in hierarchical Bayes (p. 114).

3.6.3 only points ahead: hierarchical GLMs learn $p(y|x,\theta_j)$ per group with prior $p(\theta_j|\xi)$ (Section 15.5), and hierarchical Bayesian neural networks do the same nonlinearly (Section 17.6) (p. 114).

### 3.7 Empirical Bayes (EB)
Full posterior inference in hierarchical models can be hard. EB first computes a point estimate $\hat\xi$ of the hyperparameters, then the conditional posterior $p(\theta|\hat\xi,\mathcal D)$ instead of the joint $p(\theta,\xi|\mathcal D)$ (p. 114). The estimate maximizes the marginal likelihood:
$$\hat\xi_{\rm mml}(\mathcal D)=\arg\max_\xi p(\mathcal D|\xi)=\arg\max_\xi\int p(\mathcal D|\theta)p(\theta|\xi)d\theta \tag{3.260}$$
This is **type II maximum likelihood** (ML-II), also called the "evidence procedure" for neural nets (p. 114). EB violates the principle that the prior is chosen independently of the data. The author views it as a cheap approximation to full hierarchical inference, as MAP is to the one-level model (p. 114). The hierarchy of methods (p. 114):

| Method | Definition |
|---|---|
| Maximum likelihood | $\hat\theta=\arg\max_\theta p(\mathcal D|\theta)$ |
| MAP | $\hat\theta=\arg\max_\theta p(\mathcal D|\theta)p(\theta|\xi)$ |
| ML-II (EB) | $\hat\xi=\arg\max_\xi\int p(\mathcal D|\theta)p(\theta|\xi)d\theta$ |
| MAP-II | $\hat\xi=\arg\max_\xi\int p(\mathcal D|\theta)p(\theta|\xi)p(\xi)d\theta$ |
| Full Bayes | $p(\theta,\xi|\mathcal D)\propto p(\mathcal D|\theta)p(\theta|\xi)p(\xi)$ |

ML-II is less likely to overfit than ML, because there are typically fewer hyperparameters $\xi$ than parameters $\theta$ (p. 114).

*Intuition note.* Each extra integral treats one more unknown as uncertain instead of fixing it at its best value. EB integrates out $\theta$ but still fixes $\xi$, so it sits between MAP and full Bayes.

**3.7.1 Hierarchical binomial model.** The $\theta_j$ integrate out analytically (p. 115):
$$p(\mathcal D|\xi)=\prod_j\int \mathrm{Bin}(y_j|N_j,\theta_j)\mathrm{Beta}(\theta_j|a,b)d\theta_j\tag{3.261}$$
$$\propto\prod_j\frac{B(a+y_j,\,b+N_j-y_j)}{B(a,b)}\tag{3.262}$$
$$=\prod_j\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\frac{\Gamma(a+y_j)\Gamma(b+N_j-y_j)}{\Gamma(a+b+N_j)}\tag{3.263}$$
Maximize over $a,b$ (methods in [Min00c]), plug in $\hat a,\hat b$, and use conjugate analysis per group. Figure 3.20 (rat tumors) is very similar to the full Bayesian Figure 3.15, but EB is much faster (p. 115).

**3.7.2 Hierarchical Gaussian model.** Assume $\sigma_j^2=\sigma^2$ for all groups. Then the EB estimate is closed-form (p. 116):
$$p(y_j|\mu,\tau^2,\sigma^2)=\int\mathcal N(y_j|\theta_j,\sigma^2)\mathcal N(\theta_j|\mu,\tau^2)d\theta_j=\mathcal N(y_j|\mu,\tau^2+\sigma^2)\tag{3.264}$$
$$p(\mathcal D|\mu,\tau^2,\sigma^2)=\prod_{j=1}^J\mathcal N(y_j|\mu,\tau^2+\sigma^2)\tag{3.265}$$
So the usual Gaussian MLEs apply:
$$\hat\mu=\frac1J\sum_j y_j=\overline y\tag{3.266}$$
Moment matching (equivalent to the Gaussian MLE) equates model variance and empirical variance:
$$\hat\tau^2+\sigma^2=\frac1J\sum_j(y_j-\overline y)^2\triangleq v\tag{3.267}$$
so $\hat\tau^2=v-\sigma^2$. Since $\tau^2$ must be positive, the common revision is
$$\hat\tau^2=\max\{0,v-\sigma^2\}=(v-\sigma^2)_+\tag{3.268}$$
The posterior mean is
$$\hat\theta_j=\lambda\mu+(1-\lambda)y_j=\mu+(1-\lambda)(y_j-\mu),\quad \lambda=\sigma^2/(\sigma^2+\tau^2)\tag{3.269}$$
(μ is the estimate $\hat\mu$ in practice; added step.) The method cannot be used on the 8-schools data, which has unequal $\sigma_j$. EM or other optimization methods can still be used there (p. 116).

*Intuition note.* $\lambda$ is the share of the total variance that is noise. Large noise relative to between-group spread pulls each group's estimate strongly toward the overall mean, and $\tau^2$ is read off the spread of the group means.

**3.7.3 EB for Markov models (n-gram smoothing).** Add-one smoothing assumes all n-grams are equally likely. **Deleted interpolation** mixes bigram frequencies $f_{jk}=N_{jk}/N_j$ with unigram frequencies $f_k=N_k/N$ (pp. 116–117):
$$A_{jk}=(1-\lambda)f_{jk}+\lambda f_k=(1-\lambda)\frac{N_{jk}}{N_j}+\lambda\frac{N_k}{N}\tag{3.270}$$
$\lambda$ is usually set by cross validation. **Backoff smoothing** falls back to $f_k$ when $f_{jk}$ is too small (p. 117). The heuristic can be read as EB in a hierarchical model (following [MP95]). Each row $A_j$ gets an independent Dirichlet prior with shared hyperparameters (Fig. 3.21), where $m$ is the prior mean ($\sum_k m_k=1$), $\alpha_0$ the prior strength, $\theta_j=A_j$ and $\xi=(\alpha,m)$:
$$A_j\sim\mathrm{Dir}(\alpha_0m_1,\dots,\alpha_0m_K)=\mathrm{Dir}(\alpha_0 m)=\mathrm{Dir}(\alpha)\tag{3.271}$$
The posterior is $A_j\sim\mathrm{Dir}(\alpha+N_j)$, and the posterior predictive is (as printed; see Reading notes)
$$p(X_{t+1}=k|X_t=j,\mathcal D)=\frac{N_{jk}+\alpha_jm_k}{N_j+\alpha_0}=\frac{f_{jk}N_j+\alpha_jm_k}{N_j+\alpha_0}\tag{3.272}$$
$$=(1-\lambda_j)f_{jk}+\lambda_jm_k\tag{3.273}$$
$$\lambda_j=\frac{\alpha_j}{N_j+\alpha_0}\tag{3.274}$$
This resembles (3.270) but the weight $\lambda_j$ depends on context ("adaptive deleted interpolation"). It also backs off to the model parameter $m_k$, not to $f_k$ (p. 117).

For $\alpha,m$ use EB. Rows are independent a priori given $\alpha$, so
$$p(\mathcal D|\alpha)=\prod_j\frac{B(\mathbf N_j+\alpha)}{B(\alpha)}\tag{3.275}$$
with $B$ the generalized beta function. It can be fitted as in [Min00c], or approximated ([MP95]) by
$$m_k\propto|\{j:N_{jk}>0\}|\tag{3.276}$$
So the prior probability of word $k$ reflects the number of different contexts it occurs in, not its count (p. 118).

MacKay and Peto's example: if the couplet "you see" is very frequent, "you" and "see" have equal marginal frequency (11 each). Formula (3.270) then gives $P(\text{you}|\text{novel})=P(\text{see}|\text{novel})$ for an unseen context word. That seems unreasonable, because "you" occurs in many contexts and "see" only after "you". Backing off to $m_k$ gives large $m_{\rm you}$ and small $m_{\rm see}$ by (3.276) (p. 118).

The Bayesian model does not beat interpolated Kneser–Ney. Nonparametric Bayes can outperform such heuristics, and recurrent neural nets do better still, because they learn distributed embeddings rather than treating symbols "atomically" (p. 118).

**3.7.4 Non-conjugate models.** For more complex models, the EB estimate cannot be computed exactly. Variational EM gives an approximate EB estimate (Section 10.1.3.2) (p. 118).

### 3.8 Model selection
"All models are wrong, but some are useful" (Box, p. 118). We have a set of models $\mathcal M$ and either pick one or average over all of them. The **M-complete** assumption says the "true" model is in $\mathcal M$. The **M-open** scenario says none may be adequate. Fit can be checked as in §3.9. If no model fits, the hypothesis space must be expanded (p. 119).

**3.8.1 Bayesian model selection.** Pick the most probable model:
$$\hat m=\arg\max_{m\in\mathcal M}p(m|\mathcal D),\qquad p(m|\mathcal D)=\frac{p(\mathcal D|m)p(m)}{\sum_{m\in\mathcal M}p(\mathcal D|m)p(m)}\tag{3.277, 3.278}$$
With uniform prior $p(m)=1/|\mathcal M|$ this becomes $\hat m=\arg\max_m p(\mathcal D|m)$ (3.279), where
$$p(\mathcal D|m)=\int p(\mathcal D|\theta,m)p(\theta|m)d\theta\tag{3.280}$$
is the marginal likelihood or evidence. A model that assigns high prior predictive density to the observed data is good. A model with too much flexibility has prior settings that do not match the data. This probability mass is "wasted" and lowers the expected likelihood. This implicit regularization is the **Bayesian Occam's razor** (Fig. 3.22: broad curve = complex model, narrow = simple, middle = "just right") (p. 119).

*Intuition note.* A model must spread one unit of probability over all datasets it can generate. A very flexible model spreads thinly, so any particular dataset gets low probability.

*Example: is the coin fair?* $M_0$: $\theta=0.5$. $M_1$: $\theta$ unknown in $[0,1]$ with a Beta prior (pp. 119–120).
$$p(\mathcal D|M_0)=\left(\tfrac12\right)^N\tag{3.281}$$
$$p(\mathcal D|M_1)=\int p(\mathcal D|\theta)p(\theta)d\theta=\frac{B(\alpha_1+N_1,\alpha_0+N_0)}{B(\alpha_1,\alpha_0)}\tag{3.282}$$
Figure 3.23(a) plots $\log p(\mathcal D|M_1)$ against heads $N_1$ for $N=5$ and $\alpha_1=\alpha_0=1$. The shape is not very sensitive to $\alpha_0,\alpha_1$ if the prior is symmetric. For 2 or 3 heads, $M_0$ is more likely than $M_1$, since it would be a suspicious coincidence for a biased coin to give almost exactly 50/50. With more extreme counts $M_1$ is favored. Figure 3.23(b) shows the BIC approximation giving a similar picture (p. 120).

**3.8.2 Bayes model averaging (BMA).** For prediction, average over models (p. 121):
$$p(y|\mathcal D)=\sum_{m\in\mathcal M}p(y|m)p(m|\mathcal D)\tag{3.283}$$
This resembles ensembling, but ensemble weights need not sum to 1. In BMA, if there is a single best model $m^*$, then in the large-sample limit $p(m|\mathcal D)$ becomes degenerate on $m^*$ and the other models are ignored. This does not happen with an ensemble (p. 121).

**3.8.3 Estimating the marginal likelihood.** (p. 121–122)
- *3.8.3.1 Conjugate models:* analytic (Section 3.4.5.4); see the coin example.
- *3.8.3.2 Harmonic mean estimator* [NR94]:
$$p(\mathcal D)\approx\left(\frac1S\sum_{s=1}^S\frac1{p(\mathcal D|\theta_s)}\right)^{-1}\tag{3.284}$$
with $\theta_s$ posterior samples (the source writes $\theta_s\sim p(\theta)$; see Reading notes). It follows from
$$\mathbb E\!\left[\frac1{p(\mathcal D|\theta)}\right]=\int\frac1{p(\mathcal D|\theta)}p(\theta|\mathcal D)d\theta\tag{3.285}$$
$$=\int\frac1{p(\mathcal D|\theta)}\frac{p(\mathcal D|\theta)p(\theta)}{p(\mathcal D)}d\theta\tag{3.286}$$
$$=\frac1{p(\mathcal D)}\int p(\theta)d\theta=\frac1{p(\mathcal D)}\tag{3.287}$$
Radford Neal called it "The Worst Monte Carlo Method Ever" (2008 blog). His argument: the posterior is often much narrower than the prior and insensitive to it, so the estimate is likely nearly the same for two different priors, and is hopelessly inaccurate (p. 121–122).
- *3.8.3.3 Other Monte Carlo:* annealed importance sampling (Section 11.5.4.1), sequential Monte Carlo (13.2.3.3), nested sampling (p. 122).
- *3.8.3.4 Variational Bayes:* an efficient approximation of the evidence via the ELBO (Section 10.3.3) (p. 122).

**3.8.4 Cross validation and marginal likelihood.** In $K$-fold cross validation (Fig. 3.24), train on $K-1$ folds and test on the $K$th, $K$ times. $K=N$ is leave-one-out (LOO-CV) (pp. 122–123):
$$L_{\rm LOO}(m)\triangleq\sum_{n=1}^N\log p(\mathcal D_n|\hat\theta(\mathcal D_{-n}),m)\tag{3.288}$$
The log marginal likelihood (LML) has a sequential form:
$$\mathrm{LML}(m)\triangleq\log p(\mathcal D|m)=\log\prod_{n=1}^N p(\mathcal D_n|\mathcal D_{1:n-1},m)=\sum_{n=1}^N\log p(\mathcal D_n|\mathcal D_{1:n-1},m)\tag{3.289}$$
$$p(\mathcal D_n|\mathcal D_{1:n-1},m)=\int p(\mathcal D_n|\theta)p(\theta|\mathcal D_{1:n-1},m)d\theta\tag{3.290}$$
This is "prequential analysis". With a plug-in point estimate (delta-function posterior),
$$p(\mathcal D_n|\mathcal D_{1:n-1},m)\approx p(\mathcal D_n|\hat\theta_m(\mathcal D_{1:n-1}))\tag{3.291}$$
$$\log p(\mathcal D|m)\approx\sum_{n=1}^N\log p(\mathcal D_n|\hat\theta(\mathcal D_{1:n-1}),m)\tag{3.292}$$
This is very similar to (3.288) but evaluated sequentially. A complex model overfits the early examples, predicts the rest poorly, and gets both a low marginal likelihood and a low cross-validation score (p. 123).

**3.8.5 Conditional marginal likelihood (CLML).** The marginal likelihood asks how likely the training data are under the prior. This suits comparing fixed priors but is less useful for selecting by posteriors. [Lot+22] showed it can sometimes be negatively correlated with generalization. The reason is that early LML terms can be large and negative for a model with a poor (weak) prior that adapts quickly (p. 123). The alternative is
$$\mathrm{CLML}(m)=\sum_{n=K}^N\log p(\mathcal D_n|\mathcal D_{1:n-1},m)\tag{3.293}$$
with $K\in\{1,\dots,N\}$. It scores the last $N-K$ points under the posterior of the first $K$. Averaging over orders reduces order dependence, and $K=N-1$ averaged over all orders gives the LOO estimate. CLML is much more predictive of generalization than LML and much less sensitive to prior hyperparameters. It is also easier to compute, since it samples from the posterior $p(\theta|\mathcal D_{<n})$, unlike the harmonic mean estimator (p. 124).

**3.8.6 Bayesian LOO.** Focus on conditional models $p(y|x,\theta)$ (p. 124). The log pointwise predictive density, and its Monte Carlo version with $\theta_s\sim p(\theta|\mathcal D,m)$:
$$\mathrm{LPPD}(m)\triangleq\sum_n\log\int p(y_n|x_n,\theta,m)p(\theta|\mathcal D,m)d\theta\approx\sum_n\log\Big(\frac1S\sum_s p(y_n|x_n,\theta_s,m)\Big)\tag{3.294, 3.295}$$
LPPD predicts $y_n$ using data that include $y_n$. What we want is the expected LPPD on future data,
$$\mathrm{ELPD}(m)\triangleq\mathbb E_{x_*,y_*}\log p(y_*|x_*,\mathcal D,m)\tag{3.296}$$
approximated by LOO:
$$\mathrm{ELPD}_{\rm LOO}(m)\triangleq\sum_n\log\int p(y_n|x_n,\theta,m)p(\theta|\mathcal D_{-n},m)d\theta\approx\sum_n\log\Big(\frac1S\sum_s p(y_n|x_n,\theta_{s,-n},m)\Big)\tag{3.297, 3.298}$$
where $\theta_{s,-n}\sim p(\theta|\mathcal D_{-n},m)$ (pp. 124–125).

This needs $N$ posteriors. Instead compute $p(\theta|\mathcal D,m)$ once and use importance sampling, with target $f=p(\theta|\mathcal D_{-n},m)$ and proposal $g=p(\theta|\mathcal D,m)$ (p. 125):
$$w_{s,-n}=\frac{f(\theta_s)}{g(\theta_s)}=\frac{p(\theta_s|\mathcal D_{-n})}{p(\theta_s|\mathcal D)}=\frac{p(\mathcal D_{-n}|\theta_s)p(\theta_s)}{p(\mathcal D_{-n})}\frac{p(\mathcal D)}{p(\mathcal D|\theta_s)p(\theta_s)}\tag{3.299}$$
$$\propto\frac{p(\mathcal D_{-n}|\theta_s)}{p(\mathcal D|\theta_s)}=\frac{p(\mathcal D_{-n}|\theta_s)}{p(\mathcal D_{-n}|\theta_s)p(\mathcal D_n|\theta_s)}=\frac1{p(\mathcal D_n|\theta_s)}\tag{3.300}$$
(The printed denominator in the middle expression of (3.300) omits the subscript $s$ on $\theta$; I wrote $\theta_s$.) Normalize and estimate:
$$\hat w_{s,-n}=\frac{w_{s,-n}}{\sum_{s'=1}^S w_{s',-n}}\tag{3.301}$$
$$\mathrm{ELPD}_{\rm IS\text{-}LOO}(m)=\sum_n\log\Big(\sum_s\hat w_{s,-n}\,p(y_n|x_n,\theta_s,m)\Big)\tag{3.302}$$
The weights may have high variance, so a Pareto distribution is fitted to the weights and used to smooth them. This is **Pareto smoothed importance sampling (PSIS)**:
$$p(r|u,\sigma,k)=\sigma^{-1}(1+k(r-u)\sigma^{-1})^{-1/k-1}\tag{3.303}$$
with location $u$, scale $\sigma$, shape $k$. The fitted $k_n$ assess the approximation. If $k_n>0.5$ for a point, it is likely an outlier and the LOO estimate is likely quite poor (p. 125).

*Intuition note.* Dropping point $n$ amounts to dividing its likelihood out of the posterior. So samples that fit $y_n$ well get small weight, and no refit is needed. Pareto smoothing tames the few huge weights.

**3.8.7 Information criteria.** Score a model by training NLL (or LPPD) plus a complexity penalty (pp. 125–126):
$$\mathcal L(m)=-\log p(\mathcal D|\hat\theta,m)+C(m)\tag{3.304}$$
Convention: $\mathrm{deviance}(m)=-2\log p(\mathcal D|\hat\theta,m)$ (3.305).

*3.8.7.1 MDL.* Choose the model that lets a sender transmit the data in the fewest bits. The author gives an approximate derivation. Parameters $\hat\theta\in\mathbb R^{D_m}$ can be reliably estimated only to accuracy $O(1/\sqrt N)$, so about $\tfrac12\log_2N$ bits per parameter suffice. (The source writes this as $\log_2(1/\sqrt N)=\tfrac12\log_2N$; see Reading notes.) Encoding the data costs $L(m)=-\log p(\mathcal D|\hat\theta,m)=-\sum_n\log p(y_n|\hat\theta,m)$ (3.306) bits. The total is
$$\mathcal L_{\rm MDL}(m)=-\log p(\mathcal D|\hat\theta,m)+\frac{D_m}2\log N\tag{3.307}$$
a two-part code with the same basic form as BIC (p. 126).

*3.8.7.2 BIC.*
$$\mathcal L_{\rm BIC}(m)=-2\log p(\mathcal D|\hat\theta,m)+D_m\log N\tag{3.308}$$
with $D_m$ the degrees of freedom. Derivation: with a Gaussian approximation to the posterior (Section 7.4.3, Eq. 7.28), and $\mathbf H$ the Hessian of the negative log joint at the MAP estimate,
$$\log p(\mathcal D|m)\approx\log p(\mathcal D|\hat\theta_{\rm map})+\log p(\hat\theta_{\rm map})-\tfrac12\log|\mathbf H|\tag{3.309}$$
With a uniform prior, drop the prior term and replace MAP by MLE:
$$\log p(\mathcal D|m)\approx\log p(\mathcal D|\hat\theta)-\tfrac12\log|\mathbf H|\tag{3.310}$$
$\log|\mathbf H|$ is the **Occam factor** (a measure of the posterior volume). With $\mathbf H=\sum_{i=1}^N\mathbf H_i$, $\mathbf H_i=\nabla\nabla\log p(\mathcal D_i|\theta)$, each $\mathbf H_i$ approximated by a fixed $\hat{\mathbf H}$, and $\mathbf H$ full rank (p. 127):
$$\log|\mathbf H|=\log|N\hat{\mathbf H}|=\log(N^{D_m}|\hat{\mathbf H}|)=D_m\log N+\log|\hat{\mathbf H}|\tag{3.311}$$
Drop $\log|\hat{\mathbf H}|$ because it does not depend on $N$ and is overwhelmed by the likelihood. Then
$$J_{\rm BIC}(m)=\log p(\mathcal D|\hat\theta,m)-\frac{D_m}2\log N\ \text{(to maximize)},\qquad \mathcal L_{\rm BIC}(m)=-2\log p(\mathcal D|\hat\theta,m)+D_m\log N\ \text{(to minimize)}\tag{3.312, 3.313}$$

*3.8.7.3 AIC.* $\mathcal L_{\rm AIC}(m)=-2\log p(\mathcal D|\hat\theta,m)+2D_m$ (3.314). It penalizes complexity less heavily than BIC, since the penalty is independent of $N$, and can be derived from a frequentist perspective (p. 127).

*3.8.7.4 WAIC.* MDL, BIC and AIC need the degrees of freedom, which is hard when parameters are correlated and not uniquely identifiable. If the parameter-to-likelihood map is not one-to-one, the model is a **singular statistical model**, and the Fisher information and $\mathbf H$ may be singular. WAIC (Watanabe–Akaike) works even then. It replaces the plug-in log likelihood with LPPD and uses the posterior variance of the log predictive as complexity (p. 127):
$$C(m)=\sum_n\mathbb V_{\theta|\mathcal D,m}[\log p(y_n|x_n,\theta,m)]\approx\sum_n\mathbb V\{\log p(y_n|x_n,\theta_s,m):s=1{:}S\}\tag{3.315}$$
$$\mathcal L_{\rm WAIC}(m)=-2\mathrm{LPPD}(m)+2C(m)\tag{3.316}$$
Intuition (author): if posterior samples make very different predictions for a point, the model is uncertain and likely too flexible. The PSIS-LOO estimate is asymptotically equivalent to WAIC [VGG17] (pp. 127–128).

*Intuition note.* Every criterion here pays for fit with a price for flexibility. on the log-likelihood scale BIC and MDL charge $\tfrac12\log N$ per parameter and AIC a constant that does not grow with $N$, and WAIC measures flexibility by how much predictions vary across the posterior.

### 3.9 Model checking
Bayesian inference is optimal only if the modeling assumptions are correct. Model checking asks whether the observed data are "typical" of what the model would generate, without a specific alternative model in mind (p. 128).

**3.9.1 Posterior predictive checks.** Coin example ([Kru15]): $M_1$: $\theta=0.99$, $M_2$: $\theta=0.01$. 30 heads in 40 flips gives $p(M_1|\mathcal D)\gg p(M_2|\mathcal D)$, yet $M_1$ is still a very bad model (p. 128). To check a model, draw synthetic datasets from the posterior predictive:
$$\tilde{\mathcal D}^s\sim p(\tilde{\mathcal D}|M,\mathcal D)=\{y^s_{1:N}\sim p(\cdot|M,\theta^s),\ \theta^s\sim p(\theta|\mathcal D,M)\}\tag{3.317}$$
Compare scalar test statistics $\mathrm{test}(\tilde{\mathcal D}^s)$ with $\mathrm{test}(\mathcal D)$. They should measure features of interest, since in general it is not possible to capture every aspect of the data with a given model. A large gap suggests a poor model. This is a **posterior predictive check** (p. 128).

*Example: 1d Gaussian (Newcomb's speed of light).* $N=66$ measurements with two clear outliers in the left tail (Fig. 3.25a). Fit a Gaussian by MLE and use the plug-in predictive (p. 128):
$$p(\tilde y|\mathcal D)\approx\mathcal N(\tilde y|\hat\mu,\hat\sigma^2),\ \hat\mu=\tfrac1N\textstyle\sum_ny_n,\ \hat\sigma^2=\tfrac1N\sum_n(y_n-\hat\mu)^2\tag{3.318}$$
Sampling $s=1{:}1000$ datasets of size 66, the sampled datasets shown in Fig. 3.25b contain none of the large negative values. With $\mathrm{test}(\mathcal D)=\min\{y\in\mathcal D\}$ (3.319), the real value is $-44$, in the left tail of the predictive distribution (Fig. 3.25c). The author says this suggests the model cannot capture the long tails (assuming these extremes are scientifically interesting) (p. 129).

*Example: linear regression ("waffle divorce").* Data for 50 US states: divorce rate $D_n$, marriage rate $M_n$, age at first marriage $A_n$. Model: $p(y=d|x=(a,m))=\mathcal N(d|\alpha+\beta_aa+\beta_mm,\sigma^2)$, vague priors, Laplace approximation to the posterior. Plotting the posterior predictive against observed $y_n$ (Fig. 3.26) shows outliers. Idaho and Utah have much lower divorce than predicted, which the text attributes to their unusually large Mormon populations. The model is overconfident, caused by the incorrect use of a linear model. Ideally the predictive error bars would be wider where the model is wrong (pp. 129–130).

**3.9.2 Bayesian p-values.**
$$p_B=\Pr(\mathrm{test}(\tilde{\mathcal D})\ge\mathrm{test}(\mathcal D)|M,\mathcal D)\tag{3.320}$$
$$p_C=\Pr(\mathrm{test}(\tilde{\mathcal D})\ge\mathrm{test}(\mathcal D)|M)\ \text{(classical; }M\text{ is the null)}\tag{3.321}$$
The Bayesian compares to what one expects after conditioning the model on the data. The frequentist compares to the sampling distribution under the null, independent of the data (p. 130). Monte Carlo (the source writes $>$ here):
$$p_B=\int\mathbb I(\mathrm{test}(\tilde{\mathcal D})>\mathrm{test}(\mathcal D))p(\tilde{\mathcal D}|\theta)p(\theta|\mathcal D)d\theta\approx\frac1S\sum_{s=1}^S\mathbb I(\mathrm{test}(\tilde{\mathcal D}^s)>\mathrm{test}(\mathcal D))\tag{3.322}$$
Values near 0 or 1 mean the data are unlikely under the model for that statistic. If $\mathrm{test}(\mathcal D)$ is a sufficient statistic of the model, it is likely to be well estimated and $p_B$ near 0.5. For the variance statistic in the speed-of-light example, $p_B=0.48$ (Fig. 3.25d). So the Gaussian can represent the variance but not the support (range). Lesson: do not ask whether the data come from the model (nearly always "no"), but whether the model captures the features we care about (p. 131).

### 3.10 Hypothesis testing
**3.10.1 Frequentist (NHST).** Decision rule $\delta(\mathcal D)=\mathbb I(t(\mathcal D)\ge t^*)$ with test statistic $t$ and critical value $t^*$. Example, the t-statistic (p. 131):
$$t(\mathcal D)=\frac{\overline x-\mu}{\hat\sigma/\sqrt N}\tag{3.323}$$
Pick a significance level $\alpha$ (often 0.05), which controls the type I error rate (rejecting a true null). Find $t^*$ with
$$p(t(\tilde{\mathcal D})\ge t^*|H_0)=\alpha\tag{3.324}$$
which guarantees $p(\delta(\tilde{\mathcal D})=1|H_0)=\alpha$. Equivalently, reject if the p-value $<\alpha$ (p. 132). The author notes p-values and NHST have many problems (Section 3.3.5.2) and avoids them in the book (p. 132).

**3.10.2 Bayesian approach.** Two routes: Bayes factors and parameter estimation (p. 132).

*3.10.2.1 Model comparison.* Bayesian testing is model selection with two models, null $M_0$ and alternative $M_1$:
$$B_{1,0}\triangleq\frac{p(\mathcal D|M_1)}{p(\mathcal D|M_0)}=\frac{p(M_1|\mathcal D)}{p(M_0|\mathcal D)}\Big/\frac{p(M_1)}{p(M_0)}\tag{3.325}$$
It is like a likelihood ratio with parameters integrated out, so models of different complexity can be compared. If $B_{1,0}>1$ prefer $M_1$, else $M_0$. Jeffreys scale (Table 3.1): $BF<1/100$ decisive for $M_0$; $<1/10$ strong; $1/10$–$1/3$ moderate; $1/3$–$1$ weak for $M_0$; $1$–$3$ weak for $M_1$; $3$–$10$ moderate; $>10$ strong; $>100$ decisive for $M_1$ (p. 132).

*3.10.2.2 Improper priors.* Improper priors (not integrating to 1) can be fine for parameter inference but cause problems for model selection. With $L_i=\int_{\Theta_i}p(\mathcal D|\theta)p(\theta|M_i)d\theta$ (p. 133),
$$p(M_0|\mathcal D)=\frac{p(M_0)L_0}{p(M_0)L_0+p(M_1)L_1}\tag{3.326}$$
Take $p(M_0)=p(M_1)=0.5$, improper uniform priors $p(\theta|M_i)\propto c_i$, and $\ell_i=\int_{\Theta_i}p(\mathcal D|\theta)d\theta$, so $L_i=c_i\ell_i$:
$$p(M_0|\mathcal D)=\frac{c_0\ell_0}{c_0\ell_0+c_1\ell_1}=\frac{\ell_0}{\ell_0+(c_1/c_0)\ell_1}\tag{3.327}$$
The result depends on the arbitrary constants. This is the **marginalization paradox**, so improper priors should be avoided here. The paradox does not arise if the same improper prior is used for common parameters shared by both hypotheses. More generally, evidence results can be quite sensitive to the form of the prior (p. 133).

*3.10.2.3 Parameter estimation (Bayesian estimation).* To avoid the computational difficulty and prior sensitivity above, estimate parameters and check how much posterior mass falls near the null value. For a coin, compute $p(0.5-\epsilon<\theta<0.5+\epsilon|\mathcal D)$, where $(0.5-\epsilon,0.5+\epsilon)$ is the **region of practical equivalence (ROPE)**. This is simpler and also quantifies effect size (p. 133).

*3.10.2.4 Binomial test.* $N$ tosses, $y$ heads. Prior: Jeffreys is $\mathrm{Beta}(\tfrac12,\tfrac12)$, but [Lee04] argues the flat $\mathrm{Beta}(1,1)$ is least informative when both heads and tails are possible. The posterior is $\mathrm{Beta}(\theta|y+1,N-y+1)$. Credible interval $(\ell,u)=(P^{-1}(\alpha/2),P^{-1}(1-\alpha/2))$ with $P$ the posterior cdf (p. 133). Probability of exceeding the null:
$$p(\theta>0.5|\mathcal D)=\int_{0.5}^1p(\theta|\mathcal D)d\theta\tag{3.328}$$
(numerical or analytic [Coo05]) (p. 134).

*3.10.2.5 Two proportions ($\chi^2$ alternative).* $y_j\sim\mathrm{Bin}(\theta_j,N_j)$, $\theta_j\sim\mathrm{Beta}(1,1)$; for $J=2$:
$$p(\theta_1,\theta_2|\mathcal D)=\mathrm{Beta}(\theta_1|y_1+1,N_1-y_1+1)\mathrm{Beta}(\theta_2|y_2+1,N_2-y_2+1)\tag{3.329}$$
$$p(\delta|\mathcal D)=\int_0^1\!\!\int_0^1\mathbb I(\delta=\theta_1-\theta_2)p(\theta_1|\mathcal D_1)p(\theta_2|\mathcal D_2)\tag{3.330}$$
$$=\int_0^1\mathrm{Beta}(\theta_1|y_1+1,N_1-y_1+1)\mathrm{Beta}(\theta_1-\delta|y_2+1,N_2-y_2+1)d\theta_1\tag{3.331}$$
Use $p(\delta>0|\mathcal D)$ to judge whether the groups differ (p. 134).

*3.10.2.6 One-sample mean (t-test).* $y_n\sim\mathcal N(\mu,\sigma^2)$, test $\mu=0$. With a noninformative prior (limit of the conjugate Gaussian–gamma), the posterior of $\mu$ after marginalizing $\sigma^2$ is the same as the sampling distribution of the MLE $\hat\mu$ (both Student $t$). So the credible interval equals the confidence interval in this simple setting (p. 134). Flat priors $p(\mu)\propto1,p(\sigma)\propto1$ can give poor results. [GHV20a] suggest weakly informative, data-derived priors: $p(\mu)=\mathcal N(0,\sigma=2.5\,\mathrm{sd}(Y))$ (data centered) and $p(\sigma)=\text{Half-Student-t}(0,\mathrm{sd}(y),\nu=4)$. These priors are not conjugate, so approximate inference (MCMC or other algorithms) is used. This is "BTT" (p. 134–135). **Robust BTT** ([Kru13], "BEST") uses a Student likelihood $y_n\sim\mathcal T(\mu,\sigma,\nu)$ with $\mu\sim\mathcal N(M_\mu,S_\mu)$, $\sigma\sim\mathrm{Unif}(\sigma_{\rm low},\sigma_{\rm high})$, $\nu-1\sim\mathrm{Expon}(1/29)$ (p. 135; footnote 13 gives the settings).

*3.10.2.7 Paired t-test.* Define $y_n=y_{2n}-y_{1n}\sim\mathcal N(\mu,\sigma^2)$ and test $\mu=0$; pass the differences to BTT (p. 135).

*3.10.2.8 Two-sample t-test.* With $\sigma_1^2=\sigma_2^2$: two-sample (independent/unpaired) t-test. With variances varying by group: Welch's t-test. Bayesian version: $y_{jn}\sim\mathcal N(\mu_j,\sigma_j^2)$, then compute e.g. $p(\mu_1-\mu_2>0|\mathcal D)$ (Fig. 3.27) (p. 135).

*3.10.2.9 Correlation.* $(x_n,y_n)\sim\mathcal N(\boldsymbol\mu,\Sigma)$ with
$$\Sigma=\begin{pmatrix}\sigma_1^2&\rho\sigma_1\sigma_2\\\rho\sigma_1\sigma_2&\sigma_2^2\end{pmatrix}\tag{3.332, 3.333}$$
(the source prints $\sigma_a$ in one entry; see Reading notes). Same data-driven priors for $\mu_j,\sigma_j$ and $p(\rho)=\mathrm{Unif}(-1,1)$ [BMM00]. Compute e.g. $p(\rho>0|\mathcal D)$ (pp. 135–136).

**3.10.3 Common tests are inference in linear models.** [Lin19] points out that many common tests can be written exactly or approximately as (Bayesian or frequentist) inference about GLM parameters. This is easier to understand and more flexible (p. 136).

*3.10.3.1 Rank transform.* Nonparametric tests can be approximated by applying a parametric test to order statistics [CI81], with good accuracy for $N\ge10$. Rank transform: sort and replace by position. Signed rank: sort by absolute size, attach sign. For $\mathcal D=(3.6,3.4,-5.0,8.2)$: $R(\mathcal D)=(3,2,1,4)$ and $SR(\mathcal D)=(2,1,-3,4)$ (p. 136). Table 3.2 (p. 137), where "exact" gives the sample size above which the approximation is indistinguishable from the exact test (✓ = exact):

| Test | Model | Exact |
|---|---|---|
| One-sample t | $y\sim\mathcal N(\mu,\sigma^2)$ | ✓ |
| Wilcoxon signed-rank | $SR(y)\sim\mathcal N(\mu,\sigma^2)$ | $N>14$ |
| Paired t | $y_2-y_1\sim\mathcal N(\mu,\sigma^2)$ | ✓ |
| Wilcoxon matched pairs | $SR(y_2-y_1)\sim\mathcal N(\mu,\sigma^2)$ | ✓ |
| Pearson | $y\sim\mathcal N(\beta_0+\beta_1x,\sigma^2)$ | ✓ |
| Spearman | $R(y)\sim\mathcal N(\beta_0+\beta_1R(x),\sigma^2)$ | $N>10$ |
| Two-sample t | $y\sim\mathcal N(\beta_0+\beta_1x,\sigma^2)$, $x\in\{0,1\}$ | ✓ |
| Welch's t | same, variance $\sigma_x^2$ | ✓ |
| Mann–Whitney U | $SR(y)\sim\mathcal N(\beta_0+\beta_1x,\sigma_x^2)$ | $N>11$ |
| One-way ANOVA | $y\sim\mathcal N(f_{\rm aov}(x;\beta),\sigma^2)$ | ✓ |
| Kruskal–Wallis | $R(y)\sim\mathcal N(f_{\rm aov}(x;\beta),\sigma^2)$ | $N>11$ |
| Two-way ANOVA | $y\sim\mathcal N(f_{\rm aov2}(x_1,x_2;\beta),\sigma^2)$ | ✓ |

*3.10.3.2 One or two groups.* One-sample: regress on a constant, $p(y_n|\theta)=\mathcal N(y_n|\beta_0,\sigma^2)$, $\beta_0=\mu$. This is the one-sample t-test. With $SR(y_n)$ the results are very close to Wilcoxon signed-rank. Paired data: model differences (paired t-test), or $SR$ of the differences (Wilcoxon matched pairs). Unpaired two groups: $x_n\in\{0,1\}$ and $p(y_n|x_n)\sim\mathcal N(\beta_0+\beta_1x_n,\sigma^2)$ is the two-sample t-test. With the signed-rank transform of $y$ it is approximately Mann–Whitney U (p. 137).

*3.10.3.3 Correlation.* If $y_n\sim\mathcal N(\beta_0+\beta_1x,\sigma^2)$ and $Y$ is scaled to standard deviation 1, then $\beta_1=\rho$ ([Mur22, Sec 11.2.3.3]), so $p(\beta_1|\mathcal D)$ gives inference on $\rho$. Spearman correlation is Pearson correlation on rank-transformed data. Pearson assesses linear relationships, Spearman general monotonic ones (Fig. 3.28). With multiple predictors, multiple regression gives the posterior of partial correlations from the posterior of the weights (p. 138).

*3.10.3.4 One-way ANOVA.* $x_n\in\{1,\dots,J\}$ (a **factor**), $p(y_n|x_n=j)\sim\mathcal N(\mu_j,\sigma^2)$. Test whether all $\mu_j$ are equal. Applying a rank transform to $y$ is similar to Kruskal–Wallis. Classical ANOVA assumes normality and a common variance, so the sampling distribution of the $F$-statistic can be derived (p. 138). Use dummy encoding $x_{n[j]}=\mathbb I(x_n=j)$, dropping the first level (**reduced rank encoding**) to avoid unidentifiable posteriors (p. 139):
$$p(y_n|x_n;\theta)\sim\mathcal N(f_{\rm aov}(x_n,\beta),\sigma^2),\quad f_{\rm aov}(x,\beta)=\beta_0+\beta_2x_{[2]}+\dots+\beta_Jx_{[J]}\tag{3.334, 3.335}$$
$\beta_0$ is the level-1 value and the other $\beta_j$ are deviations from level 1. The null is $\beta_j=0$ for $j=2{:}J$ (Fig. 3.29). A symmetric form is
$$f_{\rm aov}(x;\beta)=\beta_0+\beta_1x_{[1]}+\dots+\beta_Jx_{[J]},\quad\textstyle\sum_{j=1}^J\beta_j=0\tag{3.336}$$
with $\beta_0$ the grand mean. The constraint is met by starting from unconstrained $\tilde\beta_j$ and $\bar\beta=\frac1J\sum_j\tilde\beta_j$:
$$f_{\rm aov}(x,\tilde\beta)=\tilde\beta_0+\sum_j\tilde\beta_jx_{[j]}=(\tilde\beta_0+\bar\beta)+\sum_j(\tilde\beta_j-\bar\beta)x_{[j]}\tag{3.337}$$
with $\beta_0=\tilde\beta_0+\bar\beta$, $\beta_j=\tilde\beta_j-\bar\beta$, and
$$\sum_{j=1}^J\beta_j=\sum_j\tilde\beta_j-\sum_j\bar\beta=J\bar\beta-J\bar\beta=0\tag{3.338}$$
In a Bayesian setting, normality and common variance can be relaxed: use a Student likelihood and per-group $\sigma_j^2$, estimated via a hierarchical model (p. 139).

*3.10.3.5 Multi-way ANOVA.* For two nominal predictors (p. 140):
$$f_{\rm aov2}(x)=\mu+\sum_j\alpha_jx_{1,[j]}+\sum_k\beta_kx_{2,[k]}+\sum_{jk}\gamma_{jk}x_{1,[j]}x_{2,[k]}\tag{3.339}$$
$$\textstyle\sum_j\alpha_j=\sum_k\beta_k=\sum_j\gamma_{jk}=\sum_k\gamma_{jk}=0\tag{3.340}$$
The test is $\gamma=\mathbf 0$ (no interaction). Bayesian: compute $p(\theta|\mathcal D)$.

*3.10.3.6 Counts ($\chi^2$ test).* Data are an $R\times C$ contingency table (Table 3.3: male 9 LH / 43 RH, $N_1=52$; female 4 LH / 44 RH, $N_2=48$; totals 13 / 87, 100). The null is independence. The classical statistic is
$$\chi^2=\sum_{r=1}^R\sum_{c=1}^C\frac{(O_{r,c}-E_{r,c})^2}{E_{r,c}}\tag{3.341}$$
with $E_{rc}=Np_{r\cdot}p_{\cdot c}$ from empirical marginals. The Bayesian version modifies two-way ANOVA with a Poisson likelihood and an exponential link, since the rate must be non-negative (p. 140):
$$p(y|x=(r,c),\theta)=\mathrm{Poi}(y|\lambda_{r,c}),\quad\lambda_{rc}=\exp(\beta_0+\beta_r+\beta_c+\beta_{r,c})\tag{3.342, 3.343}$$

*3.10.3.7 Non-metric outputs.* Categorical: logistic regression. Ordinal: ordinal regression. Counts: Poisson regression (Chapter 15) (p. 141).

*Intuition note.* Once a test is written as a regression coefficient being zero, the Bayesian version is just the coefficient's posterior. Rank transforms replace the raw values by their order, so a parametric model can approximate a nonparametric test. The author presents this as easier to understand and more flexible than choosing a named test from a menu.

### 3.11 Missing data
Parts of $\mathbf X_n\in\mathbb R^D$ may be unknown (labels are appended to features in supervised problems). $\mathbf X_{n,\rm mis}$ is the missing part and $\mathbf X_{n,\rm obs}$ the observed part. Because missingness may be informative (e.g., declining to answer "Do you have disease X?"), the **missing data mechanism** must be modeled with $\mathbf R_n$: $\mathbf R_{n,\rm obs}=1$ for observed components and $\mathbf R_{n,\rm mis}=0$ for the others (p. 141). Assumptions ([Rub76; LR87]):
- **MCAR**: $p(\mathbf R_n|\mathbf X_n)=p(\mathbf R_n)$, the strongest assumption.
- **MAR**: $p(\mathbf R_n|\mathbf X_n)=p(\mathbf R_n|\mathbf X_{n,\rm obs})$; missingness may depend on visible features only.
- **MNAR**: neither holds.

Discriminative models $p(y_n|x_n,\theta)$: $x_n$ is always observed and $y_n$ is observed depending on $r_n$ (e.g., semi-supervised learning with $\mathcal D^L$ and $\mathcal D^U$). In Fig. 3.30, in MCAR and MAR the hidden $y_n$ is a leaf node that does not affect $\theta$, so unlabeled data can be ignored. In MNAR, $y_n$ affects the always-observed $r_n$, so $\theta$ depends on $y_n$ even when hidden, and missing values must be imputed (Section 20.3.3) (p. 142). For a generative model $p(x,y)=p(y)p(x|y)$, unlabeled data can help even under MCAR and MAR, because $\theta$ depends on both $x$ and $y$ and information about $p(x)$ can inform $p(y|x)$ (p. 142).

## Toy example (ours, not from the text)
Fair coin $M_0$ ($\theta=0.5$) versus unknown-bias coin $M_1$ (uniform prior, $\mathrm{Beta}(1,1)$). Observe one specific sequence of $N=4$ tosses.

- $p(\mathcal D|M_0)=(1/2)^4=1/16=0.0625$ for any sequence.
- $p(\mathcal D|M_1)=B(1+N_1,1+N_0)/B(1,1)$, with $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$ and $B(1,1)=1$.
- Case $N_1=2,N_0=2$: $B(3,3)=2!\,2!/5!=4/120=1/30\approx0.0333$. So $B_{1,0}=(1/30)/(1/16)=16/30\approx0.53$. Table 3.1: weak evidence for $M_0$ ($1/3<BF<1$).
- Case $N_1=4,N_0=0$: $B(5,1)=4!\,0!/5!=1/5=0.2$. So $B_{1,0}=0.2/0.0625=3.2$. Table 3.1: moderate evidence for $M_1$ ($3<BF<10$).

Occam's razor shows here: $M_1$ spreads its probability over all 16 sequences and over all biases. For balanced data it loses to the simple $M_0$, and only strongly lopsided data favor it.

## Concepts
- [[empirical-bayes]] (new) — estimate hyperparameters from data (by maximizing marginal likelihood), then condition on them; approximation to full hierarchical Bayes (p. 114)
- [[type-ii-maximum-likelihood]] (new) — maximizing $p(\mathcal D|\xi)$ over hyperparameters, also called the evidence procedure in the neural-network context (p. 114)
- [[hierarchical-model]] — here, models whose group parameters share a prior with hyperparameters $\xi$; EB fits $\xi$ by a point estimate (p. 114)
- [[partial-pooling-shrinkage]] — posterior mean $\hat\theta_j=\lambda\mu+(1-\lambda)y_j$ with $\lambda=\sigma^2/(\sigma^2+\tau^2)$ (p. 116)
- [[marginal-likelihood]] — $p(\mathcal D|m)=\int p(\mathcal D|\theta,m)p(\theta|m)d\theta$, the evidence for model $m$ (p. 119)
- [[bayesian-occams-razor]] — a model with too much flexibility wastes prior predictive mass, lowering the expected likelihood (p. 119)
- [[bayesian-model-selection]] (new) — choose $\arg\max_m p(m|\mathcal D)$; with uniform prior $\arg\max p(\mathcal D|m)$ (p. 119)
- [[bayes-model-averaging]] (new) — $p(y|\mathcal D)=\sum_mp(y|m)p(m|\mathcal D)$; weights sum to 1, unlike general ensembles (p. 121)
- [[harmonic-mean-estimator]] (new) — evidence estimate from posterior samples; criticized as hopelessly inaccurate (p. 121)
- [[cross-validation-loo-waic]] — LOO-CV, PSIS-LOO, WAIC as predictive-accuracy estimates (pp. 122–127)
- [[conditional-marginal-likelihood]] (new) — LML of the last $N-K$ points under the posterior from the first $K$; better tied to generalization (p. 124)
- [[psis-loo]] (new) — importance-sampling LOO with Pareto-smoothed weights; $k_n>0.5$ flags trouble (p. 125)
- [[information-criteria-bic-aic-mdl]] (new) — fit plus complexity penalty; BIC from Gaussian approximation to evidence (pp. 125–127)
- [[posterior-predictive-check]] — compare test statistics on replicated and real data (p. 128)
- [[bayesian-p-value]] (new) — $\Pr(\mathrm{test}(\tilde{\mathcal D})\ge\mathrm{test}(\mathcal D)|M,\mathcal D)$ (p. 130)
- [[bayes-factor]] (new) — ratio of marginal likelihoods; Jeffreys scale (p. 132)
- [[marginalization-paradox]] (new) — improper priors make the posterior model probability depend on arbitrary constants (p. 133)
- [[rope-bayesian-estimation]] (new) — posterior mass in a region of practical equivalence around the null value (p. 133)
- [[tests-as-linear-models]] (new) — common tests as inference in GLMs, nonparametric ones via rank transforms (p. 136)
- [[missing-data-mechanisms]] (new) — MCAR, MAR, MNAR, defined via $p(\mathbf R_n|\mathbf X_n)$ (p. 141)
- [[frequentist-vs-bayesian-inference]] — $p_B$ conditions on data, $p_C$ uses the null's sampling distribution (p. 130)
- [[credible-interval]] — $(P^{-1}(\alpha/2),P^{-1}(1-\alpha/2))$ from the posterior cdf; equals the confidence interval in the t-test case with noninformative prior (pp. 133–134)

## Canonical instances
- [[rat-tumor-eb]] — EB for hierarchical binomial, close to full Bayes but much faster (p. 115)
- [[you-see-bigram]] — MacKay–Peto argument for context counts in smoothing (p. 118)
- [[coin-fair-bayes-factor]] — $M_0$ vs $M_1$, $N=5$, marginal likelihood vs heads (p. 119)
- [[newcomb-speed-of-light]] — Gaussian fit fails on min statistic, passes on variance ($p_B=0.48$) (pp. 128–131)
- [[waffle-divorce-ppc]] — linear model overconfident for Idaho and Utah (pp. 129–130)
- [[handedness-contingency-table]] — $2\times2$ table for the Poisson/$\chi^2$ test (p. 140)

## Bridges (candidates)
- [same-math] EB shrinkage weight $\lambda=\sigma^2/(\sigma^2+\tau^2)$ ↔ regularized regression: ridge-type shrinkage toward a common mean — a prior-variance-controlled weighted average
- [same-math] Sequential form of LML (3.289) ↔ online learning: cumulative log loss of a Bayesian predictor (prequential)
- [structural-analogy] BIC/MDL penalty $\tfrac{D_m}2\log N$ ↔ information theory: two-part code length
- [structural-analogy] MCAR/MAR/MNAR ↔ causal inference: ignorability of the assignment mechanism
- [same-math] Importance weights $1/p(\mathcal D_n|\theta_s)$ for LOO ↔ Monte Carlo: self-normalized importance sampling

## Questions this raises
- How much does plugging in a point estimate $\hat\xi$ understate uncertainty when there are few groups?
- When do Bayes factors and LOO/WAIC disagree, and which should guide a modeling decision?
- How does ROPE choice ($\epsilon$) change conclusions compared with a Bayes factor?
- For MNAR data, what extra modeling of $p(r_n|x_n,y_n)$ is needed, and how sensitive are results to it?

## Reading notes
- This is part 3/3 of Chapter 3. It starts mid-§3.6.2 (printed p. 114, the closing lines on reparameterization) and ends at the end of §3.11 (p. 142). The source note says the split is at a section boundary, but this part actually begins mid-§3.6.2 (the start of §3.6.2 is in the previous part).
- Printed = pdf − 34. Running footer: "Probabilistic Machine Learning: Advanced Topics", online version, December 10, 2025.
- Apparent misprints, as shown in the page images:
  - Eq. (3.284): $\theta_s\sim p(\theta)$ is written, but the derivation (3.285–3.287) uses posterior samples $p(\theta|\mathcal D)$.
  - §3.8.7.1: "$\log_2(1/\sqrt N)=\tfrac12\log_2N$" has a sign slip; the intended number of bits is $\tfrac12\log_2N$.
  - Eq. (3.333): $\rho\sigma_a\sigma_2$ should presumably be $\rho\sigma_1\sigma_2$.
  - Eqs. (3.272)–(3.274): $\alpha_j$ presumably stands for $\alpha_0$ in the numerator of $\lambda_j$ and in the term $\alpha_jm_k$ (since $\alpha_0m_k=\alpha_k$ in (3.271)); (3.273) only works out with $\alpha_0$.
  - §3.8.3.4: the ELBO is written "$\log q(\mathcal D|\theta)$", which looks garbled.
  - Eq. (3.320) uses $\ge$ and (3.322) uses $>$.
  - §3.10.1: "reject the null hypothesis is $p<\alpha$"; Eq. (3.341) text defines $p_{r\cdot}=O_{c\cdot}/N$, $p_{\cdot c}=O_{\cdot r}/N$ with swapped indices.
  - Table 3.2 lists two-way ANOVA as "N" (nonparametric), but the model has no rank transform.
  - §3.10.3.2 cites §3.10.2.6 for the paired t-test, which is §3.10.2.7.
- Cross-references to other chapters (Sections 3.3.5.2, 7.4.3, 10.x, 11.5, 15.x, 20.3.3) are not in this unit and were not checked.
