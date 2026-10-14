---
id: gelman-2013-bda3/ch22-finite
work: gelman-2013-bda3
unit: "22 Finite mixture models"
pages: 519-544
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Finite mixture models (BDA3, Chapter 22)

## L0 — One line
A mixture model adds unobserved component indicators z to the model, so that standard hierarchical-model tools (EM/ECM, Gibbs sampling, posterior predictive checks) can fit populations made of subpopulations, with extra care needed for label switching and for the number of components.

## L1 — The gist (≤ 120 words)
Some data come from several subpopulations whose membership is not recorded. The chapter treats such data as a hierarchical model with hidden indicators z. It shows how to set priors, find modes with ECM, run a Gibbs sampler, and check and expand the fit. This is done in a schizophrenia reaction-time example. It then covers label switching, which makes component-specific parameters hard to summarise, and an overfitted-mixture way to handle an unknown number of components (small Dirichlet parameter a = n₀/H). Finally it applies mixtures to density estimation, classification and regression. Mixtures matter because they are flexible models, though the authors caution that, because the true model is never known, estimated clusters cannot be fully trusted.

**Prerequisites:** Bayes' rule; multinomial, Dirichlet, Beta and normal conjugate updating; EM and Gibbs sampling in outline; posterior predictive checks; hierarchical models.

## L2 — Key ideas (5–10 bullets)
- A finite mixture is a hierarchical model: hidden indicators $z_{ih}$ say which component produced each observation, and inference averages over them (pp. 519–520).
- Continuous mixtures (the t model, negative binomial, beta-binomial) use the same notation and computing approach. Their mixing distribution plays the role of the weights λ (p. 520).
- With indicators in the model, ECM (EM that maximises one block of parameters at a time) and Gibbs steps become simple. Gibbs steps are stochastic versions of the ECM steps. Hunt for all modes from many starting points (pp. 523–529).
- Model checking uses test quantities that are not sufficient statistics. In the example, the observed spread of within-person variances is atypical under the first model, and the expanded model improves but does not fully fix this (pp. 531–533).
- Mixture likelihoods are invariant to relabelling components. Component-specific posteriors are therefore not meaningful under exchangeable priors (priors that treat all components alike) unless each component is somehow defined as different from the others, but the mixed density $g(y)$ is unaffected (pp. 533–535).
- Order constraints on means only partly solve label ambiguity and may bias results (p. 536).
- An unknown number of components can be handled by an overfitted mixture with upper bound H and Dirichlet(n₀/H, …, n₀/H) weights. The number of occupied components (those holding at least one observation) then has a posterior (p. 536).
- Mixtures give flexible models for classification and regression, including semi-supervised cases and predictor-dependent mixtures of regressions (pp. 539–542).

## L3 — Walkthrough

### Chapter introduction (pp. 519)
Mixtures arise when measurements come from several conditions, such as male and female heights (p. 519). If the condition is known (sex), model it directly. If it is not known (which reaction-time trials were affected by an attentional delay), use a mixture (p. 519).

Basic principle: introduce unobserved **indicators** $z$ (vector or matrix) giving the component of each observation. Observed $y$ is modelled given $z$, and $z$ gets its own distribution. The indicators can be treated as missing data. Inference averages over $z$; in simulation this means drawing $(\theta, z)$ from the joint posterior (p. 519).

### 22.1 Setting up and interpreting mixture models

**Finite mixtures (pp. 519–520).** Model $y=(y_1,\dots,y_n)$ (or $y|x$) as a mixture of $H$ components. Component $h$ has density $f_h(y_i|\theta_h)$ and population proportion $\lambda_h$, with $\sum_h\lambda_h=1$. If all components share one family:
$$p(y_i|\theta,\lambda)=\lambda_1 f(y_i|\theta_1)+\dots+\lambda_H f(y_i|\theta_H).\tag{22.1}$$
The weights could be read as a discrete prior on $\theta_h$. The authors prefer to read them as describing variation in $\theta$ across the population, so the model resembles a hierarchical model (p. 520).

Indicators: $z_{ih}=1$ if unit $i$ is from component $h$, else $0$. Given $\lambda$, $z_i=(z_{i1},\dots,z_{iH})\sim\text{Multin}(1;\lambda_1,\dots,\lambda_H)$, so $\lambda$ is a hyperparameter for $z$ (p. 520). The joint distribution given the parameters is
$$p(y,z|\theta,\lambda)=p(z|\lambda)p(y|z,\theta)=\prod_{i=1}^n\prod_{h=1}^H\bigl(\lambda_h f(y_i|\theta_h)\bigr)^{z_{ih}},\tag{22.2}$$
with exactly one $z_{ih}=1$ per $i$. $H$ is for now assumed known. An observation with known component (e.g. adult of recorded sex) adds one factor with known $z_i$ (p. 520).

**Continuous mixtures (p. 520).** The finite mixture is a special case of $p(y_i)=\int p(y_i|\theta)\lambda(\theta)d\theta$. Chapter 5 hierarchical models are continuous mixtures, with $\lambda(\theta)$ the population distribution. The t distribution is a scale mixture of normals. Negative binomial and beta-binomial are continuous mixtures of Poisson and binomial respectively (p. 520).

The author's t example: $y_i|\mu,\sigma^2,z_i\sim N(\mu,\sigma^2 z_i)$, with $z_i$ a random sample from a scaled Inv-$\chi^2(\nu,1)$. After averaging over $z_i$, $y_i\sim t_\nu(\mu,\sigma^2)$. The degrees of freedom $\nu$ plays the role of the multinomial parameters $\lambda$. The posterior of the $z_i$ can show possible outliers (p. 520).

**Identifiability (p. 521).** All finite mixtures are nonidentifiable in one sense: permuting component labels leaves the distribution unchanged. When possible, define the parameter space to remove this, e.g. require means to be nondecreasing, or $\lambda_H$ nondecreasing. For many problems an informative prior ties components to subpopulations (p. 521).

**Prior (p. 521).** Usually independent priors on $\theta$ and $\lambda$. For multinomial indicators, the natural conjugate prior is $\lambda\sim\text{Dirichlet}(\alpha_1,\dots,\alpha_H)$. The relative sizes of the $\alpha_h$ give the prior mean of $\lambda$, and $\sum\alpha_h$ is a prior sample size. Some parameters can be shared across components (e.g. a common variance). Continuous mixtures need a hyperprior on their mixing parameters (p. 521).

**Proper posterior (p. 521).** Check before using an improper prior. An improper prior on $\lambda$ ($\alpha_i=0$) may cause trouble if the data do not show all $H$ components. Problems are more common with improper priors on component parameters. For two normals with separate variances there are "uninteresting" modes where one component is a single observation with zero variance. The posterior is proper if the ratio of the two variances is fixed or has a proper prior, but not if $(\log\sigma_1,\log\sigma_2)$ has a joint uniform density (p. 521).

**Number of components (pp. 521–522).** Computing with large $H$ can be costly, so start small, for computational and scientific reasons. Use the posterior predictive distribution of a test quantity that is not a sufficient statistic for the parameters to judge whether the current number describes the data. Alternatively treat $H$ as a hierarchical parameter and average over its posterior (pp. 521–522).

**More general formulation (p. 522).** Let $z_i\in\{1,\dots,H\}$ be the **latent class** of item $i$:
$$y_i|z_i\sim f(\theta_{z_i},\phi),\tag{22.3}$$
where $\phi$ is shared and $\theta_h$ is specific to subpopulation $h$. With $\Pr(z_i=h)=\pi_h$, marginalising $z_i$ gives
$$g(y|\pi,\theta,\phi)=\sum_{h=1}^H\pi_h f(y|\theta_h,\phi).$$
In general $g$ can approximate a much broader variety of true likelihoods than $f$. Example: $f=N(y|\theta,\phi^2)$ is unimodal and symmetric, but letting the mean vary across subpopulations gives a location mixture,
$$g(y|\pi,\theta,\phi)=\sum_{h=1}^H\pi_h N(y|\theta_h,\phi^2).\tag{22.4}$$
Any density can be accurately approximated by a mixture of sufficiently many normals (author's claim, p. 522). Letting $\phi$ also vary by component gives a location-scale mixture. Location-scale mixtures can often reach better accuracy with fewer components and may characterise variability more realistically (p. 522).

*Intuition note.* Mixing simple pieces (each component is simple) gives a flexible whole. Forms that are too rigid alone, such as a single normal (unimodal and symmetric), become able to approximate a much broader variety of shapes (p. 522).

**Mixtures as true models or approximations (pp. 522–523).** There are two schools.
- **First school:** latent subpopulations are real, and one can infer and cluster them (latent class models, model-based clustering) (p. 522).
- **Authors' take:** clustering can be a useful exploratory, hypothesis-generating tool. But such tasks are intrinsically sensitive to the parametric family $f$, so, to the extent that the true parametric model is never known, one can never fully trust estimated cluster-specific parameters or clusters. Changing $f$ from normal to $t$ can give very different clusters. In the multivariate case, diagonal covariances can inflate the number of clusters, splitting true elliptical subpopulations into several spherical groups (pp. 522–523).
- **Second school:** inferring latent subpopulations is intrinsically ill-defined, but mixtures are still a flexible model class. They give more realistic hierarchical models for random effects and error distributions, and serve density estimation, classification and nonparametric regression (p. 523). (The text does not say the authors fully adopt this view; it follows their own take.)

**Basics of computation (p. 523).** Fit as with hierarchical models, averaging over indicators, treated as nuisance parameters or missing data.

- **Crude estimates.** Graphical or clustering methods classify observations tentatively, after which component parameters are easy to estimate. This ignores uncertainty in the indicators and can overestimate differences between components. Crude indicator estimates are not usually needed, since EM averages over them and Gibbs draws them first (p. 523).
- **EM and variational Bayes.** The joint mode of parameters and indicators is not useful. EM estimates the parameters averaging over indicators. The E-step needs expected sufficient statistics of $(y,z)$ under the complete-data log likelihood (22.2), given the last guess of $(\theta,\lambda)$. In finite mixtures this is often the conditional expectation of the indicators by Bayes' rule. ECM or another EM variant may help. Find all modes and assess their posterior mass. Use a fairly large number (perhaps 50 or 100) of starting points, made by adding randomness to the crude estimate or by simplifying the model. One crude estimate is not enough (pp. 523–524). Variational Bayes gives approximate marginals in the same way (p. 524).
- **Gibbs sampler.** Starting values come from importance resampling from an approximation, a mixture of $t_4$ distributions at the modes. The sampler alternates (i) draws of indicators given parameters (multinomial draws in finite mixtures) and (ii) draws of parameters given indicators. Given the indicators the model is an ordinary, possibly hierarchical model, so conjugate priors help. Errors such as a wrong improper prior often show up here: a chain started near zero variance may never leave. Aliasing from label permutations can look like nonconvergence (p. 524).
- **Posterior inference.** After approximate convergence, ignore the drawn indicators for parameter inference. The posterior of the indicators says which component each observation likely came from. Use posterior predictive checks. If robustness matters, use the Chapter 17 methods (p. 524).

### 22.2 Example: reaction times and schizophrenia

**Data (pp. 524–525).** 17 people (11 non-schizophrenic, 6 schizophrenic), 30 reaction times each (Figure 22.1, log scale). Schizophrenics are slower on average, and some are much more variable. Psychological theory suggests that schizophrenics have an attentional deficit on some trials plus a general motor reflex retardation that affects all trials (p. 524).

**Model (pp. 525–526).** Non-schizophrenics ($j=1,\dots,11$): $N(\alpha_j,\sigma_y^2)$. Schizophrenics ($j=12,\dots,17$): a two-component mixture on log times. With probability $1-\lambda$ no delay, mean $\alpha_j$. With probability $\lambda$ delayed, mean $\alpha_j+\tau$. Same variance $\sigma_y^2$ (p. 525). The hierarchical part: $\alpha_j\sim N(\mu+\beta S_j,\sigma_\alpha^2)$, where $S_j=1$ for schizophrenics, so $\beta$ measures motor retardation. Parameters of primary interest: $\beta$, $\lambda$ (proportion of schizophrenic responses delayed), $\tau$ (size of delay) (p. 525). Hierarchical form with indicators $z_{ij}$ (1 = delayed), $\phi=(\sigma_\alpha^2,\beta,\lambda,\tau,\mu,\sigma_y^2)$:
$$y_{ij}|\alpha_j,z_{ij},\phi\sim N(\alpha_j+\tau z_{ij},\sigma_y^2),\quad \alpha_j|z,\phi\sim N(\mu+\beta S_j,\sigma_\alpha^2),\quad z_{ij}|\phi\sim\text{Bernoulli}(\lambda S_j).$$
In the general notation $H=2$, $\lambda_1=\lambda$, $\lambda_2=1-\lambda$, $z_{ij1}=z_{ij}$, $z_{ij2}=1-z_{ij}$. The indicators are not needed to state the model but simplify the conditionals, which allows ECM and Gibbs (p. 526).

**Hyperprior (p. 526).** Uniform on $\phi$. The model is unidentified because unaffected trials could be read as having a negative delay, so $\tau>0$ is imposed. Variances are positive. $\lambda$ is uniform on $[0.001,0.999]$ because 0 or 1 would not be a mixture. Science and prior analysis suggest that a no-mixture model is inadequate (p. 526).

**Crude estimates (p. 526).** $\alpha_j$ by person sample means; $\sigma_y^2$ by the average sample variance within non-schizophrenics; $\mu$ by the mean of non-schizophrenic $\alpha_j$; $\beta$ by the group difference; $\sigma_\alpha^2$ by the within-group variance of $\alpha_j$. From the histograms, $\hat\lambda=1/3$ and $\hat\tau=1.0$ (p. 526).

**ECM (pp. 526–528).** 100 starting points: crude estimates each divided by an independent $\chi^2_1$ variable (p. 526). E-step: average $z$ over $p(z|\theta^{\rm old},y)$. The expected complete-data log posterior is
$$E_{\rm old}\log p(z,\theta|y)=\text{const}+\sum_{j=1}^{17}\log N(\alpha_j|\mu+\beta S_j,\sigma_\alpha^2)+\sum_{j=1}^{17}\sum_{i=1}^{30}\Bigl[\log N(y_{ij}|\alpha_j,\sigma_y^2)(1-E_{\rm old}z_{ij})+\log N(y_{ij}|\alpha_j+\tau,\sigma_y^2)E_{\rm old}z_{ij}\Bigr]+\sum_{j}\sum_{i}S_j\bigl[\log(1-\lambda)(1-E_{\rm old}z_{ij})+\log(\lambda)E_{\rm old}z_{ij}\bigr].$$
The indicators are independent given $\theta^{\rm old}$ and $y$, with $\Pr(z_{ij}=1|\theta^{\rm old},y)=\zeta_{ij}$:
$$\zeta_{ij}=\frac{\lambda^{\rm old}N(y_{ij}|\alpha_j^{\rm old}+\tau^{\rm old},(\sigma_y^{\rm old})^2)}{(1-\lambda^{\rm old})N(y_{ij}|\alpha_j^{\rm old},(\sigma_y^{\rm old})^2)+\lambda^{\rm old}N(y_{ij}|\alpha_j^{\rm old}+\tau^{\rm old},(\sigma_y^{\rm old})^2)}.\tag{22.5}$$
(The printed (22.5) has no $S_j$; the Gibbs step on p. 529 fixes $z_{ij}=0$ for non-schizophrenics (p. 527).)

M-step (conditional maximisations, p. 527):
1. $\lambda^{\rm new}=\dfrac{1}{6\cdot30}\sum_{j=12}^{17}\sum_{i=1}^{30}\zeta_{ij}$ (fractional contributions).
2. For each $j$, combining the normal population distribution with the 30 data points:
$$\alpha_j^{\rm new}=\frac{\frac1{\sigma_\alpha^2}(\mu+\beta S_j)+\sum_{i=1}^{30}\frac1{\sigma_y^2}(y_{ij}-\zeta_{ij}\tau)}{\frac1{\sigma_\alpha^2}+\sum_{i=1}^{30}\frac1{\sigma_y^2}}.\tag{22.6}$$
3. $\tau^{\rm new}=\dfrac{\sum_{j=12}^{17}\sum_{i=1}^{30}\zeta_{ij}(y_{ij}-\alpha_j)}{\sum_{j=12}^{17}\sum_{i=1}^{30}\zeta_{ij}}$ and $(\sigma_y^{\rm new})^2=\dfrac1{17\cdot30}\sum_{j=1}^{17}\sum_{i=1}^{30}(y_{ij}-\alpha_j-\zeta_{ij}\tau^{\rm new})^2$.
4. Population parameters (uniform hyperprior), conditional modes (p. 528):
$$\mu^{\rm new}=\tfrac1{17}\sum_{j=1}^{17}(\alpha_j-\beta^{\rm new}S_j),\quad \beta^{\rm new}=\tfrac16\sum_{j=12}^{17}(\alpha_j-\mu^{\rm new}),\quad(\sigma_\alpha^{\rm new})^2=\tfrac1{17}\sum_{j=1}^{17}(\alpha_j-\mu^{\rm new}-\beta^{\rm new}S_j)^2.\tag{22.7}$$
These are equivalent to $\mu^{\rm new}=\frac1{11}\sum_{j=1}^{11}\alpha_j$ and $\beta^{\rm new}=\frac16\sum_{j=12}^{17}\alpha_j-\frac1{11}\sum_{j=1}^{11}\alpha_j$, with $(\sigma_\alpha^{\rm new})^2$ as in (22.7) (p. 528).

**Result of ECM (p. 528).** After 100 iterations from each of 100 starting points: three local maxima, one major and two minor. The minor modes are near-degenerate ($\lambda$ near zero), with posterior density ratios less than $e^{-20}$ relative to the major mode. The authors conclude that the target can be treated as unimodal for practical purposes (p. 528).

**Normal and t approximations (p. 528).** The marginal posterior averaging over indicators is
$$p(\theta|y)\propto\prod_{j=1}^{17}N(\alpha|\mu+\beta S_j,\sigma_\alpha^2)\times\prod_{j=1}^{17}\prod_{i=1}^{30}\bigl((1-\lambda S_j)N(y_{ij}|\alpha_j,\sigma_y^2)+\lambda S_jN(y_{ij}|\alpha_j+\tau,\sigma_y^2)\bigr).\tag{22.8}$$
It is monitored during ECM to check that it increases each step. A multivariate $t_4$ approximation is centred at the major mode with scale from the numerical second-derivative matrix. $S=2000$ draws from it start importance resampling. Minor-mode neighbourhoods would have minuscule importance weights (p. 528).

**Gibbs sampler (pp. 528–529).** Ten starting points by importance resampling from the $t_4$ approximation, intended to have means near the target and variances above target variances (pp. 528–529). One cycle (p. 529):
1. Draw $z_{ij}$ independent Bernoulli with probability $\zeta_{ij}$ from (22.5), for $i=1..30$, $j=12..17$. $z_{ij}=0$ for $j<12$.
2. Draw $\alpha_j$ normal, mean from (22.6) with $\zeta_{ij}\to z_{ij}$, variance the reciprocal of the denominator of (22.6).
3. $\lambda\sim\text{Beta}(h+1,180-h+1)$, $h=\sum_{j=12}^{17}\sum_i z_{ij}$ (delayed trials among 180), restricted to $[0.001,0.999]$.
4. The rest, as for the normal with unknown mean and variance: first the variances, then the others.
$$\sigma_y^2|\alpha,\lambda,z\sim\text{Inv-}\chi^2\Bigl(508,\tfrac1{508}\sum_{j=1}^{17}\sum_{i=1}^{30}(y_{ij}-\alpha_j-z_{ij}\tau)^2\Bigr),\quad \sigma_\alpha^2|\alpha,\lambda,z\sim\text{Inv-}\chi^2\Bigl(15,\tfrac1{15}\sum_{j=1}^{17}(\alpha_j-\mu-\beta S_j)^2\Bigr),$$
$$\tau|\cdots\sim N\Bigl(\tfrac{\sum_{j=12}^{17}\sum_i z_{ij}(y_{ij}-\alpha_j)}{\sum_{j=12}^{17}\sum_i z_{ij}},\tfrac{\sigma_y^2}{\sum_{j=12}^{17}\sum_i z_{ij}}\Bigr),\quad \mu|\cdots\sim N\Bigl(\tfrac1{17}\sum_{j=1}^{17}(\alpha_j-\beta S_j),\tfrac1{17}\sigma_\alpha^2\Bigr),$$
$$\beta|\alpha,\lambda,z,\mu,\sigma_y^2,\sigma_\alpha^2\sim N\Bigl(\tfrac16\sum_{j=12}^{17}(\alpha_j-\mu),\tfrac16\sigma_\alpha^2\Bigr).\tag{22.9}$$
The Gibbs steps are stochastic versions of the ECM steps: variances are drawn from scaled inverse-$\chi^2$ rather than set to the mode, and most centres use the ECM formulas with $\zeta_{ij}\to z_{ij}$ (p. 529).

*Intuition note.* ECM and Gibbs use the same two-step idea. Guess each trial's delay status, then update parameters as if that status were known. ECM uses fractional "soft" memberships $\zeta_{ij}$. Gibbs draws hard 0/1 memberships at random.

**Degenerate point (p. 530).** If all $z_{ij}=0$, the conditional of $\tau$ has no information (improper prior), so strictly the posterior is improper. For these data this point has extremely low posterior probability and was not reached. If $\sum z_{ij}=0$ were realistic, an informative prior on $\tau$ would be needed (p. 530).

**Inference from simulations (p. 530).** Ten sequences of 200 draws. $\hat R<1.1$ for all scalar estimands (scales: log for variances, logit for $\lambda$). Posterior intervals use 1000 draws from the second halves. Results, "old model" (Table 22.1; 2.5% / median / 97.5%):

| Parameter | 2.5% | median | 97.5% |
|---|---|---|---|
| $\lambda$ | 0.07 | 0.12 | 0.18 |
| $\tau$ | 0.74 | 0.85 | 0.96 |
| $\beta$ | 0.17 | 0.32 | 0.48 |

Interpretation: strong evidence of slower average times for schizophrenics ($\exp(\beta)$ in [1.18, 1.62]), with infrequent ($\lambda$ in [0.07, 0.18]) but large delays ($\exp(\tau)$ in [2.10, 2.61]) (p. 530).

**Posterior predictive distributions (p. 531).** Two kinds: (1) new measurements on an existing person $j$, conditional on that person's $\alpha_j$; (2) measurements on a new person, drawing $\tilde\alpha$ from $N(\mu+\beta S,\sigma_\alpha^2)$ first. For checking fit, use kind (1) (p. 531).

**Checking the model (p. 531).** Figure 22.1 suggests substantial variation in within-person variance among schizophrenics. Test quantities: $s_j$ is the standard deviation of the 30 log times for schizophrenic $j$; $T_{\min}$ and $T_{\max}$ are the smallest and largest of the six $s_j$. For each of 1000 posterior draws, simulate $y^{\rm rep}$ and compute $T_{\min}(y^{\rm rep})$, $T_{\max}(y^{\rm rep})$. A scatterplot (Figure 22.2) shows the observed point atypical: $T_{\min}$ too low, $T_{\max}$ too high, with estimated p-values 0.000 and 1.000. The average of $s_j$ would be a poor test quantity, because it is essentially the sufficient statistic for $\sigma_y^2$, so the model fits it automatically (p. 531).

**Expanding the model (pp. 531–532).** Add $\omega$ = probability that a schizophrenic is prone to attentional delays, and $\sigma_{y2}^2$ = variance of delayed observations (uniform priors). The old model is the special case $\omega=1$, $\sigma_{y2}^2=\sigma_y^2$. Add indicator $W_j$ (0 for non-schizophrenics, Bernoulli($\omega$) for schizophrenics):
$$y_{ij}|z_{ij},\theta\sim N\bigl(\alpha_j+\tau z_{ij},(1-z_{ij})\sigma_y^2+z_{ij}\sigma_{y2}^2\bigr),\quad \alpha_j|\cdot\sim N(\mu+\beta S_j,\sigma_\alpha^2),$$
$$z_{ij}|S,W,\theta\sim\text{Bernoulli}(\lambda S_jW_j),\quad W_j|S,\theta\sim\text{Bernoulli}(\omega S_j).$$
Three new Gibbs steps (for $\omega$, $\sigma_{y2}^2$, $W$); the old steps are altered to condition on them (details not given). Ten sequences of length 500, with $\hat R<1.1$; the first half is discarded, leaving 2500 draws (p. 532).

New-model results (Table 22.1; 2.5% / median / 97.5%): $\lambda$ 0.46/0.64/0.88; $\tau$ 0.21/0.42/0.60; $\beta$ 0.07/0.24/0.43; $\omega$ 0.24/0.56/0.84 ($\omega$ fixed at 1 in the old model). More schizophrenic observations are delayed but the average delay is shorter; because the old model is nested, the differences suggest a real improvement in fit (p. 532). Adding $\omega$ changes the interpretation of the other parameters (Table 22.1 caption, p. 530).

**Checking the new model (p. 533).** Same $T_{\min}$, $T_{\max}$ under the new posterior (Figure 22.3). The observed × is in the same place but the predictive distribution has moved closer. The p-values are 0.97 and 0.05, so fit is "by no means perfect", but lack of fit has greatly diminished in magnitude (p. 533).

*Intuition note.* A model check asks whether data simulated from the fitted model look like the real data in a feature the model was not tuned to. Here the feature is how much spread varies across people. The expanded model adds a further source of person-to-person variation; it reduced, but did not remove, the misfit.

### 22.3 Label switching and posterior computation

**Label ambiguity (p. 533).** Nothing in the likelihood distinguishes component $h$ from $h'$. Example: $(\pi_1,\theta_1,\pi_2,\theta_2)=(0.2,0,0.8,-1)$ is equivalent to $(0.8,-1,0.2,0)$. Under EM, any converged estimate has equivalent-likelihood estimates from permuting indexes. In a Bayesian model with a prior that is exchangeable over components, the marginal posterior of $\theta_h$ is identical for all $h$. So one cannot meaningfully estimate a posterior for component $h$ without defining it as different from the others (p. 533). A typical exchangeable prior:
$$(\pi_1,\dots,\pi_H)\sim\text{Dirichlet}(a,\dots,a),\quad\theta_h\sim P_0\text{ independently}.\tag{22.10}$$

**Data augmentation Gibbs algorithm (p. 534).** For a univariate location-scale Gaussian mixture,
$$y_i|z_i\sim N(\mu_{z_i},\tau_{z_i}^2),\quad\Pr(z_i=h)=\pi_h,\tag{22.11}$$
$$\mu_h,\tau_h^2\sim N(\mu_h|\mu_0,\kappa\tau^2)\,\text{Inv-gamma}(\tau^2|a_\tau,b_\tau).\tag{22.12}$$
There are no global parameters $\phi$. Steps:
1. $\Pr(z_i=h|-)=\dfrac{\pi_hN(y_i|\mu_h,\tau_h^{-1})}{\sum_l\pi_lN(y_i|\mu_l,\tau_l^{-1})}$.
2. $p(\mu_h,\tau_h^2|-)=N(\mu_h|\hat\mu_h,\hat\kappa\tau_h^2)\text{Inv-gamma}(\tau_h^2|\hat a_{\tau_h},\hat b_{\tau_h})$ with $\hat\kappa_h=(\kappa^{-1}+n_h)^{-1}$, $\hat\mu_h=\hat\kappa(\kappa^{-1}\mu_0+n_h\bar y_h)$, $\hat a_{\tau_h}=a_\tau+n_h/2$, $\hat b_{\tau_h}=b_\tau+\frac12\Bigl(\sum_{i:z_i=h}(y_i-\bar y_h)^2+\bigl(\frac{n_h}{1+\kappa n_h}\bigr)(\bar y_h-\mu_0)^2\Bigr)$. Here $n_h=\sum_i1_{z_i=h}$ and $\bar y_h$ is the mean within component $h$.
3. $\pi_1,\dots,\pi_H|-\sim\text{Dir}(a+n_1,\dots,a+n_H)$.

The density estimate is $\frac1S\sum_{s=1}^S\sum_{h=1}^H\pi_h^{(s)}N(y|\mu_h^{(s)},\tau_h^{(s)2})$ over a grid of $y$ (p. 534).

**Convergence and label switching (pp. 534–535).** The authors recommend not assessing convergence on component-specific $(\mu_h,\tau_h)$. By exchangeability each has the same multimodal target. With well-separated modes (e.g. 0 and −1) and a low-density region between them, the chain tends to stay in one labelling for long stretches. One can argue the sampler has failed, but in practice quantities that marginalise the labels, such as $g(y)$, often converge and mix well even if labels do not (p. 535).

**Density estimation claims (p. 535).** In the authors' experience, the Bayes density estimate with sufficiently large $H$ and $a=1/H$ has excellent frequency properties and lower mean integrated squared error than typical kernel density estimators. Component-specific bandwidths give locally adaptive smoothness, chosen automatically through the intrinsic Bayes penalty for complexity, without cross-validation. The penalty arises because the marginal likelihood tends to decrease as items spread over more components, since extra parameters mean marginalising over a larger space (p. 535).

**Choosing $P_0$ (p. 535).** Avoid an improper or very diffuse $P_0$, since results may be sensitive to the huge variance. Best results come when $P_0$ generates components close to the support of the data. One option is to normalise the data and use $\mu_0=0$, $\kappa=1$, $a_\tau=2$, $b_\tau=4$ as a default, then transform the samples back. Another is to elicit hyperparameters from knowledge of location and scale (p. 535).

**Component-specific inference (p. 535).** Raw posterior summaries of $(\mu_h,\tau_h)$ are inappropriate: with good mixing, $\mu_1$ and $\mu_2$ would get the same posterior mean. Post-processing: run MCMC ignoring the problem, then choose permutations $\sigma_1,\dots,\sigma_S$ to minimise a loss $L(a,\theta)$. Iterate between choosing action $a$ to minimise expected posterior loss given $\{\sigma_s\}$, and choosing each $\sigma_s$ to minimise loss given $a$ (p. 535).

**Order constraints (p. 536).** One can instead impose $\mu_1<\dots<\mu_H$ in the prior. Drawbacks: in multivariate cases it is unclear what restriction to use. Similar means with different variances may be needed, so label switching can still occur if means are close. Restrictions can cause mixing problems and bias, since the prior favours pushing parameters apart, which may greatly overestimate differences when posterior uncertainty is sizeable (p. 536).

### 22.4 Unspecified number of mixture components

**Options (p. 536).** A prior on $H$ (e.g. truncated Poisson) with reversible jump MCMC is computationally intensive. More common: fit several $H$ and choose by a penalised goodness-of-fit criterion. Marginal posterior probability can be sensitive to the prior; DIC is not well justified theoretically in mixture models; WAIC is theoretically justified, but inference conditional on the selected $H$ ignores uncertainty in $H$ (p. 536).

**Overfitted mixture (p. 536).** Use the Gibbs sampler of §22.3 with $H$ as an upper bound and a carefully chosen $a$. Let $H_n=\sum_{h=1}^H1_{n_h>0}$ be the number of occupied components; the sampler gives draws of $H_n$ after convergence. If $a=1$ (Dirichlet(1,…,1)), items tend to spread over many components, and as $H$ grows there is a high probability of each item in its own cluster, $H_n=n$. Instead set $a=n_0/H$, so the prior sample size $n_0=\sum_{h=1}^Ha$ does not depend on $H$; $n_0=1$ is a reasonable minimally informative default. This works well in favouring most weight on a few dominant locations (author's report). Equivalent construction: $\pi_h=\lambda_h/\sum_l\lambda_l$ with $\lambda_h\sim\text{Gamma}(n_0/H,1)$. With $n_0=1$ and large $H$ many $\lambda_h$ are near zero and a few lie in the right tail, giving a few high-probability components (p. 536).

For component-specific parameters, condition on an estimate $\hat H_n$: run an initial MCMC with upper bound $H$, set $\hat H_n$ to the posterior mode of $H_n$, run again with $H=\hat H_n$, and post-process as in §22.3 (p. 537). (The text writes this as "$H=\hat H_n$".)

*Intuition note.* With a tiny Dirichlet parameter, most weights are pushed near zero. The sampler therefore leaves surplus components empty, and the number of non-empty ones is learned from the data.

**Example: simple mixtures fit to small datasets (pp. 537–539).**
- Data: 82 galaxy speeds (1-D); acidity of 155 Wisconsin lakes (1-D); 150 iris observations (3 species, 4 measurements). Upper bound $H=5$ for the 1-D data. A larger bound for iris, though no more than 6 clusters were needed.
- Priors: data standardised; $a=1/H$; $\mu_0=0$, $\kappa=1$. A highly diffuse prior on cluster locations can lead the posterior to overly favour too few clusters. Precision prior: inverse-gamma with parameters 3 and 1. Iris: diagonal covariances. Post-processing with Kullback–Leibler loss; mixing of component-specific parameters was poor, as expected (p. 538).
- Redundant clusters can still get a few observations, which overestimates the number of clusters unless very small clusters are ignored (p. 537).
- **Galaxy (Table 22.2):** three non-overlapping clusters; the one near the origin is large, with $\pi_1=0.66$ (sd 0.15), $\mu_1=0.10$, $\sigma_1=0.22$. It might be two overlapping clusters but is well approximated by one normal (p. 538).
- **Acidity (Table 22.3):** two clusters are suggested. One looks skewed, so three components may be needed. Hence if the component form does not match well the form of the clusters, the number of components cannot be read as the number of clusters. The posterior favours two or three components. Fitted density has pointwise 95% credible intervals (p. 538).
- **Iris (Table 22.4):** six components with weights 0.30, 0.23, 0.16, 0.14, 0.11, 0.07. Posterior simulation automatically represents uncertainty in the number of clusters. With three true biological clusters one might expect three components, but the later masses are nontrivial, suggesting that the fitted normals do not fully capture variation within one or more species (pp. 538–539).

### 22.5 Mixture models for classification and regression (p. 539)
Mixtures can help when target and predictor values are partially observed.

**Classification (pp. 539–541).** Response $y\in\{1,\dots,C\}$, predictors $x\in\mathbb R^p$. Supervised: all $(y_i,x_i)$ observed. Semi-supervised: $y_i$ observed only for $n_0<n$ items. Model $\psi_c=\Pr(y_i=c)$ and $f_c(x_i)=f(x_i|y_i=c)$, then use Bayes' rule:
$$\Pr(y_i=c|x_i)=\frac{\Pr(y_i=c)f(x_i|y_i=c)}{\sum_{c'=1}^C\Pr(y_i=c')f(x_i|y_i=c')}.$$
With sufficiently flexible $\{f_c\}$ this can characterise any classification function. It is analogous to the cluster allocation formula of a $C$-component mixture (p. 539).

**Bayesian discriminant analysis (p. 540).** Prior $\psi\sim\text{Dirichlet}(a\psi_{01},\dots,a\psi_{0C})$ ($\psi_0=E\psi$, $a$ a prior sample size). In the supervised case the posterior is $\text{Dirichlet}\bigl(a\psi_{01}+\sum_i1_{y_i=1},\dots,a\psi_{0C}+\sum_i1_{y_i=C}\bigr)$. For $f_c$: either $N(x_i|\mu_c,\Sigma)$, which may be sensitive to normality, or a nonparametric-style mixture
$$f_c(x_i)=\sum_{h=1}^H\pi_{ch}N_p(x_i|\mu^*_{ch},\Sigma^*_{ch}),\quad(\mu^*_{ch},\Sigma^*_{ch})\sim P_0.$$
For simplicity they recommend sharing weights across classes ($\pi_c=\pi$) with a Dirichlet$(1/H,\dots,1/H)$ prior, and a normal-inverse Wishart $P_0$. With $z_i$ the within-class component index, the Gibbs steps are: (1) update $z_i$ from $\Pr(z_i=h|y_i=c,-)=\pi_hN_p(x_i|\mu^*_{ch},\Sigma^*_{ch})/\sum_{h'}\pi_{h'}N_p(x_i|\mu^*_{ch'},\Sigma^*_{ch'})$; (2) update $\psi$, $\pi$ and each $(\mu^*_{ch},\Sigma^*_{ch})$ from their conditionals. Semi-supervised: add a step imputing missing $y_i$. Missing predictors: add a step updating missing $x_i$ elements from their conditional normal (p. 540).

Prediction: record $\Pr(y_{n+1}=c)$ at each saved iteration and average to estimate $\Pr(y_{n+1}=c|x_{n+1},y,X)$. A single Bayes-optimal prediction minimises expected loss; under 0-1 loss it is the $c$ with the highest probability (pp. 540–541).

**Mixed predictor types and a joint model (p. 541).** Product kernel: $f(x_i|\theta_i)=\prod_{j=1}^p\mathcal K_j(x_{ij}|\theta_{ij})$, which assumes conditional independence given $\theta_i$. Induce dependence with $\theta_i\sim P=\sum_{h=1}^H\pi_h\delta_{\Theta_h}$, $\Theta_{hj}\sim P_{0j}$ independently (Gaussian kernels for continuous, Bernoulli for binary, Poisson for count predictors, with conjugate priors). This is a latent class model: elements of $x_i$ are conditionally independent given $z_i$ but marginally dependent. For classification, jointly: $\Pr(y_i=c|z_i=h)=\psi_{z_ic}$, $f(x_i|z_i=h)=N(x_i|\mu_{z_i},\Sigma_{z_i})$. This avoids modelling $x_i|y_i=c$ explicitly. Averaging over $z_i$:
$$\Pr(y_i=c|x_i)=\frac{\sum_{h=1}^H\pi_h\psi_{hc}N(x_i|\mu_h,\Sigma_h)}{\sum_{h=1}^H\pi_hN(x_i|\mu_h,\Sigma_h)},$$
which the authors say can be shown to be extremely flexible (p. 541).

**Regression (pp. 541–542).** For $y_i\in\mathbb R$, $x_i\in\mathbb R^p$, set $w_i=(y_i,x_i)$:
$$f(w_i)=\sum_{h=1}^H\pi_hN_{p+1}(w_i|\mu_h,\Sigma_h),\tag{22.13}$$
which induces
$$f(y_i|x_i)=\sum_{h=1}^H\pi_h(x_i)N(y_i|\beta_{0h}+x_i\beta_{1h},\sigma_h^2),\tag{22.14}$$
$$\pi_h(x_i)=\frac{\pi_hN_p(x_i|\mu_h^{(x)},\Sigma_h^{(x)})}{\sum_{h'}\pi_{h'}N_p(x_i|\mu_{h'}^{(x)},\Sigma_{h'}^{(x)})}.\tag{22.15}$$
This is a predictor-dependent mixture of linear regressions. The mean can change nonlinearly with $x$, and the variance and residual shape can change as well. It is fit by a Gibbs sampler for the joint model (22.13), and conditional draws follow automatically (p. 542).

Reasons for conditional-density models that avoid modelling the marginal of $x$ (p. 542): (1) predictors may be fixed by design; (2) predictors may not all be continuous; (3) computing $f(x_i)$ can be costly for many predictors; (4) a one-component conditional model could suffice while joint modelling needs many components, possibly degrading prediction of $y$ given $x$.

### 22.6 Bibliographic note (pp. 542–543)
Reports, among others: EM for mixtures (Dempster, Laird and Rubin 1977); variational Bayes (Bishop 2006); expectation propagation (Minka 2001); relabelling algorithms (Stephens 2000b; Jasra, Holmes and Stephens 2005); label-switching moves inside MCMC (Papaspiliopoulos and Roberts 2008); justification of the Dirichlet$(\alpha/H,\dots,\alpha/H)$ prior for overfitted mixtures (Ishwaran and Zarepour 2002) and asymptotic zeroing-out of redundant components (Rousseau and Mengersen 2011); product-kernel joint modelling (Dunson and Bhattacharya 2010) (pp. 542–543).

### 22.7 Exercises (pp. 543–544)
Eight exercises; see "Exercises worth doing".

## Toy example (ours, not from the text)
One schizophrenic-style person with three log reaction times $y=0,\,1,\,2$. Take the delay model of §22.2 with the current guess $\alpha=0$, $\tau=1$, $\sigma_y=1$, $\lambda=0.25$. Normal densities: $N(0|0,1)=0.3989$, $N(1|0,1)=0.2420$, $N(2|0,1)=0.0540$. By symmetry $N(y|1,1)$ at $y=0,1,2$ is $0.2420,\,0.3989,\,0.2420$.

E-step, using (22.5):
- $y=0$: $\zeta=\dfrac{0.25(0.2420)}{0.75(0.3989)+0.25(0.2420)}=\dfrac{0.0605}{0.29918+0.0605}=\dfrac{0.0605}{0.35968}=0.168$.
- $y=1$: $\zeta=\dfrac{0.25(0.3989)}{0.75(0.2420)+0.25(0.3989)}=\dfrac{0.09973}{0.18150+0.09973}=0.355$.
- $y=2$: $\zeta=\dfrac{0.25(0.2420)}{0.75(0.0540)+0.25(0.2420)}=\dfrac{0.0605}{0.0405+0.0605}=0.599$.

Larger observations are more probably "delayed", although the prior weight of 0.25 is small.

M-step for one person (with $\alpha$ held fixed): $\lambda^{\rm new}=(0.168+0.355+0.599)/3=1.122/3=0.374$. $\tau^{\rm new}=\dfrac{0.168(0)+0.355(1)+0.599(2)}{1.122}=\dfrac{1.553}{1.122}=1.38$. Repeating the two steps is ECM. A Gibbs sampler would instead draw each $z$ as Bernoulli($\zeta$) and draw $\lambda$ from Beta(#delayed + 1, 3 − #delayed + 1).

Label switching, same spirit: swapping the labels of $(\pi,\theta)=(0.2,0)$ and $(0.8,-1)$ gives the same mixture density (p. 533 example), so the likelihood cannot tell which is "component 1".

## Concepts
- [[finite-mixture-model]] (new) — $p(y_i)=\sum_h\lambda_hf(y_i|\theta_h)$, a hierarchical model with latent component indicators (p. 519).
- [[mixture-indicator-latent-class]] (new) — unobserved $z_{ih}$ (or $z_i\in\{1..H\}$) naming the component or latent class of unit $i$ (pp. 520, 522).
- [[continuous-mixture]] (new) — mixing distribution over a continuous parameter; the t, negative binomial and beta-binomial are examples (p. 520).
- [[hierarchical-multilevel-model]] — the authors read the mixing distribution as describing population variation in $\theta$, like a hierarchical model (p. 520).
- [[conjugate-prior]] — Dirichlet for $\lambda$ (multinomial indicators); normal-inverse-gamma for component parameters in the Gaussian mixture (pp. 521, 534).
- [[label-switching]] (new) — likelihood is invariant to permuting component labels, so under an exchangeable prior the marginal posterior is identical for every component (p. 533).
- [[em-ecm-algorithm]] (new) — E-step gives $\zeta_{ij}=E(z_{ij})$ by Bayes' rule; M-step uses conditional maximisations (pp. 523, 526–528).
- [[gibbs-sampling]] — alternate draws of indicators given parameters and parameters given indicators (pp. 524, 529, 534).
- [[posterior-predictive-check]] — use test quantities that are not sufficient statistics, e.g. $T_{\min}$, $T_{\max}$ of within-person SDs (p. 531).
- [[posterior-predictive-distribution]] — predictions for existing persons use $\alpha_j$; for new persons first draw $\tilde\alpha_j$ (p. 531).
- [[convergence-diagnostics]] — $\hat R<1.1$ on suitable scales (log for variances, logit for $\lambda$) (p. 530).
- [[overfitted-mixture-dirichlet-n0-over-H]] (new) — upper bound $H$ with Dirichlet$(n_0/H,\dots)$ weights; the number of occupied components $H_n$ is learned (p. 536).
- [[bayesian-occams-razor]] — the "intrinsic Bayes penalty": marginal likelihood tends to fall as items are spread across more components (p. 535).
- [[cross-validation-loo-waic]] — WAIC is theoretically justified for mixtures; DIC is not (p. 536).
- [[exchangeability]] — here: components are exchangeable in the prior (22.10) (p. 533).
- [[product-kernel-latent-class]] (new) — product of per-predictor kernels, with dependence induced by a mixture over parameters (p. 541).
- [[variational-inference-elbo]] — variational Bayes also approximates marginals while averaging over indicators (p. 524; ELBO not stated in this unit).

## Canonical instances
- [[schizophrenia-reaction-times]] — two-component mixture on log times for 6 schizophrenics; ECM + Gibbs, expanded model with $\omega$ (pp. 524–533).
- [[galaxy-acidity-iris-mixtures]] — overfitted Gaussian mixtures for density estimation and clustering (pp. 537–539).
- [[t-distribution-as-scale-mixture]] — $N(\mu,\sigma^2z_i)$ with $z_i\sim$ scaled Inv-$\chi^2(\nu,1)$ gives $t_\nu$ (p. 520).
- [[two-component-label-ambiguity]] — $(0.2,0;0.8,-1)$ vs $(0.8,-1;0.2,0)$ (p. 533).

## Bridges (candidates)
- [structural-analogy] Mixture indicators $z$ as missing data ↔ missing-data and potential-outcomes inference (canon): both treat unobserved quantities as unknowns to impute or average over.
- [same-math] Gibbs step for $z_{i}$ (22.5, p. 527; p. 534 step 1) ↔ Bayes' theorem: posterior component probability ∝ prior weight × component likelihood.
- [structural-analogy] Semi-supervised classification with imputed missing labels ↔ latent-class models: unlabeled items get their class by a Gibbs imputation step.
- [metaphor] Choosing $a=n_0/H$ so that unneeded components empty out ↔ Bayesian Occam's razor: complexity is penalised through the marginal likelihood rather than a selection rule.
- [structural-analogy] Predictor-dependent mixture weights (22.15) ↔ hierarchical models with group-varying parameters: the "group" membership probability varies smoothly with $x$.

## Questions this raises
- When data have a skewed component, how can one tell "a few components" from "a few real clusters"? The chapter says the count then cannot be read as the number of clusters (p. 538).
- When a Gibbs chain never label-switches, is relabelling post-processing still valid, and how sensitive are summaries to the loss function chosen (p. 535)?
- How sensitive is the number of occupied components to $n_0$ and the upper bound $H$? Tables 22.2–22.4 only report one setting.
- What prior would identify components in multivariate models, where an ordering of means is unclear (p. 536)?

## Exercises worth doing
- Ex. 1 (p. 543) — which pointwise posterior summary (mean, median or mode) to use to assign a component to each data point — difficulty: medium
- Ex. 2 (p. 543) — fit 2-, 3-, 4-component and unspecified-$H$ mixtures to data simulated from three normals; see when the model is too small or too big — difficulty: medium
- Ex. 6 (p. 544) — replace a gamma population distribution by a finite mixture for the kidney cancer example and compare — difficulty: hard
- Ex. 7 (p. 544) — consequences of a noninformative prior on component-specific parameters — difficulty: easy
- Ex. 8 (p. 544) — simulate sorted Dirichlet$(1/k,\dots)$ vs Dirichlet$(1,\dots)$ weights as $k$ grows, to see why $a=1/H$ empties components — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 529 = printed 519). Page labels give printed numbers, used throughout.
- The text layer replaces $\theta$ by $\omega$ in many places, renders $\sim$ as "→" (and minus signs in some exponents, e.g. $e^{-20}$, $\tau_h^{-1}$), renders $\mathbb R$ as "∈", and garbles some sums and products. I used the page images, which show $\theta$.
- Misprints and inconsistencies seen in the images:
  - p. 529 Gibbs step 1 reads "Bernoulli($z_{ij}$), with probabilities $\zeta_{ij}$". The probability should be $\zeta_{ij}$.
  - p. 538 refers to "Table 22.4" for galaxy and acidity results; those are Tables 22.2 and 22.3 (22.4 is iris).
  - p. 534 step 1 writes $N(y_i|\mu_h,\tau_h^{-1})$ while (22.11) uses $\tau_{z_i}^2$ as the variance.
  - p. 541 writes $\Pr(S_i=h)$ where $z_i$ is meant, and "$P_{ij}$" for $P_{0j}$.
  - pp. 533–536 and 540 use $k$ and $H$ interchangeably for the number of components.
  - The header row of Tables 22.2–22.4 reads "Mixure component" (sic).
  - p. 530 describes $\lambda$ in a slightly garbled sentence ("the probability that an observation will be delayed for a schizophrenic subject to attentional delays").
  - Figure 22.2/22.3 captions call $T_{\min},T_{\max}$ "within-schizophrenic variances", while the text (p. 531) defines them from standard deviations $s_j$.
- The figures (22.1–22.4)
- The model-fitting details of the expanded model's Gibbs steps are not given in the source (p. 532). The bibliographic note was summarised, not reproduced in full.
- Exercises have no printed solutions in this unit.
