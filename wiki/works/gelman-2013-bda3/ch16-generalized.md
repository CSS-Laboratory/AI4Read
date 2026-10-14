---
id: gelman-2013-bda3/ch16-generalized
work: gelman-2013-bda3
unit: "16 Generalized linear models"
pages: 405-434
fields: [bayesian]
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
# Generalized linear models (BDA3, Chapter 16)

## L0 — One line
A generalized linear model (linear predictor + link + non-normal random component) can be handled in Bayesian fashion by repeated normal "pseudodata" regressions, stabilised by weakly informative priors, and applied, including in hierarchical models, to Poisson, logistic, multinomial and loglinear data.

## L1 — The gist (≤ 120 words)
How do we extend Bayesian linear regression to counts, binary, categorical and multivariate outcomes? The chapter defines generalized linear models, shows how to approximate their likelihood by a weighted normal regression on pseudodata, and proposes a default Cauchy prior that stabilises logistic regression when separation occurs. Worked examples cover hierarchical Poisson regression (police stops), multilevel logistic regression (state opinion), a bivariate meta-analysis, a Bradley–Terry chess model fitted as a Poisson regression, and loglinear tables fitted by iterative proportional fitting. It matters because linear models with normal errors do not suit many outcomes, such as counts or binary data.

**Prerequisites:** linear regression in matrix form; Bayes' theorem; Taylor expansion; Poisson, binomial, multinomial, Dirichlet distributions; hierarchical models; Gibbs and Metropolis sampling; EM algorithm.

## L2 — Key ideas (5–10 bullets)
- A GLM has three parts: linear predictor $\eta = X\beta$, link function $g$ with $\mu = g^{-1}(\eta)$, and a random component for $y$ with mean $\mu$ (p. 405). It covers cases where linearity or normal variation fails.
- Discrete-data models can be rewritten with latent continuous data (probit: $u_i\sim N(X_i\beta,1)$). This helps interpretation and gives a Gibbs sampler for probit (p. 408).
- The likelihood can be approximated by a normal regression on pseudodata $z_i$ with pseudovariances $\sigma_i^2$ (eq. 16.4). Iterating gives the posterior mode (Newton's method) and a normal posterior approximation (pp. 410–411).
- Separation can make the logistic MLE undefined or unreasonable (−∞ in the 1964 voting example), and flat-prior Bayes can also fail. A weakly informative Cauchy(0, 2.5) prior on standardized inputs stabilises it (pp. 412–416).
- A t prior can be fitted by alternating weighted least squares with an approximate EM step for the scale (eqs. 16.8–16.11) (pp. 414–415).
- Hierarchical Poisson regression with an offset and per-observation normal errors handles overdispersion. In the police-stop data, for the most frequent stops (violent and weapons offenses), blacks and hispanics were stopped more than whites relative to arrests in all three precinct categories; for property and drug crimes whites were stopped slightly more or more often (pp. 420–422).
- Multinomial data can be fitted as Poisson regression by conditioning on totals; the Bradley–Terry chess model with ties uses this trick (pp. 426–428).
- Loglinear models for contingency tables use a Dirichlet-like conjugate prior. Iterative proportional fitting finds the mode and Bayesian IPF (a Gibbs sampler) draws from the posterior (pp. 429–431).

## L3 — Walkthrough

### Introduction (pp. 405–406)
A linear model $X\beta$ with normal errors is easy to interpret, but may not suit the data. Transformation sometimes helps, e.g. $y_i = x_{i1}^{b_1}\cdots x_{ik}^{b_k}\cdot$variation gives $\log y_i = b_1\log x_{i1}+\dots+b_k\log x_{ik}+$variation (p. 405). It does not help when $y\ge 0$ can equal zero, or when $y$ is discrete (e.g. counts of a rare disease by county) (p. 405). In the election example the vote share is bounded, but the bounds are not a serious problem because observations lie almost all in 0.2–0.8 and the residual sd is about 0.06 (p. 405).

A GLM is specified in three stages (p. 405):
1. linear predictor $\eta = X\beta$;
2. link function $g(\cdot)$: $\mu = g^{-1}(\eta) = g^{-1}(X\beta)$;
3. random component: distribution of $y$ with mean $E(y|X)=\mu$, possibly with a dispersion parameter $\phi$.

$X$ is $n\times p$; $\eta$ is the vector of $n$ linear predictors (p. 406). The data distribution is
$$p(y|X,\beta,\phi)=\prod_{i=1}^n p(y_i|X_i\beta,\phi).\tag{16.1}$$
Poisson and binomial models fix $\phi=1$, but the authors say excess dispersion is "the rule rather than the exception" in practice (p. 406).

### 16.1 Standard GLM likelihoods (pp. 406–407)
- **Continuous.** Linear regression is the identity link, $g(\mu)=\mu$. For positive data, use the normal model on the log scale; gamma and Weibull are sometimes alternatives (p. 406).
- **Poisson.** $y$ is Poisson with mean $\mu$ (variance $\mu$), usually with log link, $\log\mu = X\beta$:
$$p(y|\beta)=\prod_{i=1}^n \frac{1}{y_i!}e^{-\exp(\eta_i)}(\exp(\eta_i))^{y_i}.\tag{16.2}$$
The factors $1/y_i!$ are absorbed into a constant in the posterior (p. 406).
- **Binomial.** $y_i\sim\mathrm{Bin}(n_i,\mu_i)$, $n_i$ known. The logit link $g(\mu_i)=\log(\mu_i/(1-\mu_i))$ gives logistic regression:
$$p(y|\beta)=\prod_{i=1}^n\binom{n_i}{y_i}\left(\frac{e^{\eta_i}}{1+e^{\eta_i}}\right)^{y_i}\left(\frac{1}{1+e^{\eta_i}}\right)^{n_i-y_i}.$$
The probit link $g(\mu)=\Phi^{-1}(\mu)$ gives $\prod\binom{n_i}{y_i}\Phi(\eta_i)^{y_i}(1-\Phi(\eta_i))^{n_i-y_i}$ (p. 406). Probit and logit are similar, differing mainly in the tails (p. 407). The complementary log-log link $g(\mu)=\log(-\log\mu)$ is asymmetric (p. 407).
- **Overdispersion** is variation beyond the assumed sampling distribution. Example: litter of mice, proportion born alive. A hierarchical model can add an indicator per mother, drawn from a normal (easy to interpret) or beta (conjugate to the binomial) distribution (p. 407). Section 16.4 uses a normal error for each data point (p. 407).

### 16.2 Working with GLMs (pp. 407–412)
**Canonical link.** The function of the mean parameter that appears in the exponent of the exponential-family density. The discussion does not depend on this choice; the probit link is not canonical (p. 407).

**Offsets.** A predictor with known coefficient. With exposure $T$, the expected count is $\mu T$. Add a column $\log T$ to $X$ with coefficient fixed at 1 (p. 407). Police-stop example: previous crime is the offset (p. 407).

**Interpretation.** Because the linear predictor predicts $g(\mu)$, the effect of changing $x_j$ depends on the current $x$ (p. 408). Compare with a standard case $x_0$, $y_0=g^{-1}(x_0\beta)$: adding or subtracting $\Delta x$ moves the outcome to $g^{-1}(g(y_0)\pm(\Delta x)\beta)$ (p. 408). The authors consider changes not necessarily close to zero more useful than the differential form (p. 408).

**Latent continuous data.** The probit model $\Pr(y_i=1)=\Phi(X_i\beta)$ is equivalent to
$$u_i\sim N(X_i\beta,1),\qquad y_i=\begin{cases}1&u_i>0\\0&u_i<0.\end{cases}\tag{16.3}$$
$u$ may have an interpretation, e.g. partisan preference (p. 408). A Gibbs sampler follows: given the $u_i$, the model is a linear regression; given parameters and data, each $u_i$ is a normal truncated to be positive or negative according to $y_i$ (p. 408). For logit, $u_i\sim\mathrm{logistic}(X_i\beta,1)$, which is less convenient computationally but useful for understanding (p. 408). Ordered multinomials use cutpoints: with $y\in\{0,1,2,3\}$ and cutpoints $c_0,c_1,c_2$, $y_i=0$ if $u_i<c_0$, 1 if $u_i\in(c_0,c_1)$, 2 if $u_i\in(c_1,c_2)$, 3 if $u_i>c_2$ (p. 408). Adding a constant to all cutpoints leaves the likelihood unchanged, so the model is potentially nonidentifiable. The usual fix is to fix one cutpoint, e.g. $c_0=0$ (p. 408).

> *Intuition note.* In the probit model a binary outcome is treated as a hidden normal score that was cut at zero. Once the score is "known", the model is ordinary regression, which is why Gibbs sampling is easy.

**Priors.** With a dispersion parameter, write $p(\beta,\phi)=p(\phi)p(\beta|\phi)$ (p. 409).
- *Noninformative (flat) prior on $\beta$:* gives the classical analysis. The posterior mode equals the MLE, found by iterative weighted linear regression (R, Glim). Approximate inference comes from a normal approximation to the likelihood (p. 409).
- *Conjugate prior:* specify hypothetical data $y_0$ ($n_0$ points) with an $n_0\times k$ matrix $X_0$. The posterior equals that from the stacked data $(y;y_0)$ with design $(X;X_0)$ and a flat prior (as in Section 14.8). The same iterative methods apply (p. 409).
- *Nonconjugate prior:* e.g. $\beta\sim N(\beta_0,\Sigma_\beta)$, convenient with normal-approximation computation (p. 409).
- *Hierarchical:* a natural way to fit complex structures and include more explanatory variables without overfitting. A normal distribution for $\beta$ lets us reuse the hierarchical normal-model methods (p. 409).

Example: the rat tumor example of Section 5.1 could be computed on a grid only because of the conjugate beta prior. With linear predictors for the 70 experiments, a hierarchical logistic regression would be more appealing and exact computation is impossible (p. 409).

**Normal approximation: pseudodata and pseudovariances.** For each $y_i$ construct $z_i$ and $\sigma_i^2$ so that $p(y_i|X_i\beta,\phi)\approx N(z_i|X_i\beta,\sigma_i^2)$. Then regress $z$ on $X$ with known variance matrix $\mathrm{diag}(\sigma_1^2,\dots,\sigma_n^2)$ using ordinary linear-regression algorithms (p. 410). The approximation is centered at $(\hat\beta,\hat\phi)$, with $\hat\eta=X\hat\beta$. During mode finding the center is updated iteratively; after approximate convergence it is fixed (p. 410).

Write the log-likelihood as $\prod_i\exp(L(y_i|\eta_i,\phi))$ and approximate each $L$ by a quadratic in $\eta_i$:
$$L(y_i|\eta_i,\phi)\approx-\frac{1}{2\sigma_i^2}(z_i-\eta_i)^2+\text{constant}.$$
Matching first- and second-order Taylor terms about $\hat\eta_i$, with $L'=dL/d\eta$, $L''=d^2L/d\eta^2$ (p. 410):
$$z_i=\hat\eta_i-\frac{L'(y_i|\hat\eta_i,\hat\phi)}{L''(y_i|\hat\eta_i,\hat\phi)},\qquad \sigma_i^2=-\frac{1}{L''(y_i|\hat\eta_i,\hat\phi)}.\tag{16.4}$$

*Example: binomial-logistic (pp. 410–411).* $L(y_i|\eta_i)=y_i\log\frac{e^{\eta_i}}{1+e^{\eta_i}}+(n_i-y_i)\log\frac{1}{1+e^{\eta_i}}=y_i\eta_i-n_i\log(1+e^{\eta_i})$. No dispersion parameter. Derivatives:
$$\frac{dL}{d\eta_i}=y_i-n_i\frac{e^{\eta_i}}{1+e^{\eta_i}},\qquad\frac{d^2L}{d\eta_i^2}=-n_i\frac{e^{\eta_i}}{(1+e^{\eta_i})^2}.$$
Hence
$$z_i=\hat\eta_i+\frac{(1+e^{\hat\eta_i})^2}{e^{\hat\eta_i}}\left(\frac{y_i}{n_i}-\frac{e^{\hat\eta_i}}{1+e^{\hat\eta_i}}\right),\qquad\sigma_i^2=\frac1{n_i}\frac{(1+e^{\hat\eta_i})^2}{e^{\hat\eta_i}}.$$
The approximation depends on $\hat\beta$ through $\hat\eta$ (p. 411).

**Finding the mode (p. 411).** At each step compute the normal approximation at the current $(\beta,\phi)$ and take the mode of the resulting approximate posterior by weighted linear regression. Prior information enters as extra rows (Section 14.8; Chapter 15 for hierarchical). Iterating is equivalent to Newton's method on $dp(\beta|y)/d\beta=0$ and converges rapidly for standard GLMs. A possible difficulty is $\beta$ tending to infinity, e.g. in logistic regression when $\mu$ is nearly 0 or 1 for some predictor combinations; substantive prior information tends to eliminate this. A dispersion parameter $\phi$ can be updated each step by maximizing its one-dimensional conditional posterior; hierarchical variances likewise (p. 411).

**Approximate normal posterior (p. 411).** At the mode, $p(\beta|\hat\phi,y)\approx N(\beta|\hat\beta,V_\beta)$ with $V_\beta=(X^T\mathrm{diag}(-L''(y_i,\hat\eta_i,\hat\phi))X)^{-1}$. For large $n$ and no $\phi$ (binomial, Poisson) one may stop here. With $\phi$, use the Section 13.5 method at the conditional mode $\hat\beta(\phi)$:
$$p_{\text{approx}}(\phi|y)=\frac{p(\beta,\phi|y)}{p_{\text{approx}}(\beta|\phi,y)}\propto p(\hat\beta(\phi),\phi|y)\,|V_\beta(\phi)|^{1/2}.$$

> *Intuition note.* Each observation is replaced by one "fake normal observation" whose mean and noise level come from the local slope and curvature of the log-likelihood. Solving the fake regression, re-centering, and repeating climbs to the posterior mode.

**More advanced methods (p. 412).** Full Bayes, variational Bayes (Section 13.7, needing a series of somewhat different normal approximations) or expectation propagation (logistic example in Section 13.8) can do much better than the normal approximation.

### 16.3 Weakly informative priors for logistic regression (pp. 412–419)
**Problem.** Besides collinearity, logistic regression can be unstable from *separation*: a linear combination of predictors perfectly predicts the outcome. It is "surprisingly common", especially with binary predictors, and is often handled inappropriately, e.g. by removing predictors, which typically removes the strongest ones (p. 412). When a model separates, the MLE can be undefined or unreasonable, and Bayes with a uniform prior can fail (p. 412).

**Proposal.** Independent Student-$t$ priors (mean 0, degrees of freedom $\nu$, scale $s$) for the coefficients, chosen to give minimal information that constrains coefficients to a reasonable range. Flat-tailed distributions allow robust inference (Chapter 17) (p. 412). Full MCMC is possible; an approximate EM gives point estimates and standard errors; the prior regularizes the estimates (p. 412).

**Example: Republican vote on sex, ethnicity, income (income coded $-2..2$).** Separate logistic regressions with uniform priors for 1960–1972 (Table 16.1, p. 413). Estimates are reasonable except in 1964, where none of the 87 African American respondents preferred the Republican candidate. R gave coefficient of black $-16.83$ with s.e. 420.40 (1960: $-1.03$, s.e. 0.36; 1968: $-3.64$, 0.59; 1972: $-2.58$, 0.26). The 1964 numbers are meaningless, depending on when the iteration stops; the MLE is $-\infty$ (pp. 412–413). Figure 16.1 shows the profile likelihood for this coefficient, maximal as $\beta\to-\infty$ (p. 413).

**Computation with a specified normal prior.** Model $\Pr(y_i=1)=\mathrm{logit}^{-1}(X_i\beta)$ (16.5). The classical algorithm linearizes the derivative of the log-likelihood, solves by weighted least squares, and iterates (p. 414). Normal priors
$$\beta_j\sim N(\mu_j,\sigma_j^2),\ j=1,\dots,J\tag{16.6}$$
enter by adding $J$ pseudo-data points to the weighted regression:
$$z_*=\begin{pmatrix}z\\\mu\end{pmatrix},\quad X_*=\begin{pmatrix}X\\I_J\end{pmatrix},\quad w_*=((\sigma^z)^{-2},\sigma^{-2}).\tag{16.7}$$
Here $z,\sigma^z$ are the pseudodata and pseudo-sds from the likelihood (defined in (14.7), outside this unit); $z_*,w_*$ have length $n+J$ and $X_*$ is $(n+J)\times J$ (p. 414). With $X_*$ the regression is identified, so $\hat\beta$ is well defined with finite variance even under collinearity or separation (p. 414). $V_\beta$ is the inverse second-derivative matrix of the log posterior at $\hat\beta$ (p. 414).

**Approximate EM with a $t$ prior.** Express each $t$ prior as a normal mixture with unknown scale:
$$\beta_j\sim N(\mu_j,\sigma_j^2),\qquad\sigma_j^2\sim\text{Inv-}\chi^2(\nu_j,s_j^2).\tag{16.8}$$
Treat $\beta_j$ as missing data and alternate one weighted-least-squares step with one EM step. Initialize $\sigma_j=s_j$ and $\beta$ at a crude guess or 0 (pp. 414–415). The target is, as printed,
$$\log p(\beta,\sigma|y)\approx-\frac12\sum_{i=1}^n\frac{1}{(\sigma_i^z)^2}(z_i-X_i\beta)^2-\frac12\sum_{j=1}^J\left(\frac1{\sigma_j^2}(\beta_j-\mu_j)^2+\log(\sigma_j^2)\right)-p(\sigma_j|\nu_j,s_j)+\text{constant}.\tag{16.9}$$
Each iteration (p. 415):
1. At the current $\beta$, compute $z,\sigma^z$.
2. *Approximate E-step:* run weighted least squares on (16.7) to get $\hat\beta$ and $V_\beta$; replace $(\beta_j-\mu_j)^2$ in (16.9) by
$$E\big((\beta_j-\mu_j)^2|\sigma,y\big)\approx(\hat\beta_j-\mu_j)^2+(V_\beta)_{jj}.\tag{16.10}$$
It is approximate because the averaging normal is itself only an approximation to the GLM likelihood.
3. *M-step:*
$$\hat\sigma_j^2=\frac{(\hat\beta_j-\mu_j)^2+(V_\beta)_{jj}+\nu_js_j^2}{1+\nu_j},\tag{16.11}$$
the approximate posterior mode of $\sigma_j^2$ given one measurement with value (16.10) and an Inv-$\chi^2(\nu_j,s_j^2)$ prior.
4. Recompute derivatives at $\hat\beta$, rebuild (16.7) with $\hat\sigma$, repeat. At convergence report $\hat\beta$ and $V_\beta$.

**Default prior.** Flat prior (scale $\to\infty$) fails under separation. The scale must be right (age in years vs months), but discrete predictors have a natural scale. Step one is standardizing *inputs* (not predictors; e.g. age, sex, age×sex has 4 predictors but 2 inputs) (pp. 415–416):
- binary inputs: shifted to mean 0 and to differ by 1 between conditions (10% black: values 0.9 and $-0.1$);
- other inputs: shifted to mean 0, scaled to sd 0.5, matching symmetric binary inputs ($\pm0.5$, sd 0.5).

A prior on standardized variables depends on the data; the authors say this is not necessarily bad and approximates a hierarchical model with the scale estimated from the data (p. 416). Priors are centered at zero because without problem-specific information the sign is unknown (p. 416). A single binomial trial with half a success and half a failure has likelihood $e^{\theta/2}/(1+e^\theta)$, close to a $t_7$ with scale 2.5. The authors choose the slightly more conservative Cauchy ($t_1$), scale 2.5 (Figure 16.2, p. 416).

*Default:* independent Cauchy(0, 2.5) for all coefficients except the constant. With standardization this implies the logit difference should be less than 5 in absolute value between one sd below and one sd above the mean. A shift of 5 on the logit scale moves probability 0.01 to 0.5 or 0.5 to 0.99, larger than expected in most applications (lung cancer: about 1% lifetime death risk for a nonsmoking US man vs less than 50% for a heavy smoker) (p. 416). For the constant, Cauchy(0, 10), implying an average-case success probability between $10^{-9}$ and $1-10^{-9}$; the authors typically have more information about the intercept than about any coefficient, "so we can get by with a weaker prior" (pp. 416–417).

> *Intuition note.* Together with the standardization, the Cauchy(0, 2.5) prior implies that moving from one sd below to one sd above the mean of an input should change the logit probability by less than 5 in absolute value, a shift larger than most applications expect, while its heavy tails still allow an occasional larger effect.

**Other models (p. 417).** *Linear regression:* same algorithm; weighted least squares is exact, a step estimates the data variance, and $y$ is rescaled to mean 0, sd 0.5 (or multiply the prior scale by the data sd). Separation is not a concern, but collinearity can arise in routine use. *Other GLMs:* pseudodata change via (16.4); for log-link models effects larger than 5 are rarely expected, so the same priors may be a reasonable default; dispersion parameters (e.g. negative binomial) get an extra step. Multinomial logit and probit have no simple iteratively reweighted least-squares algorithm to adapt (p. 417).

**Bioassay example (pp. 417–418).** Twenty animals, four doses (data in Table 3.1). Cauchy 10 (constant) and 2.5 (dose, after rescaling $x$ to mean 0, sd 0.5). The coefficient of standardized dose moves from $10.2\pm6.4$ (glm) to $5.4\pm2.2$ (bayesglm); the intercept from $-0.1\pm0.7$ to $-0.2\pm0.6$ (Figure 16.3, p. 417). On the rescaled parameterization the slope goes $7.7\pm4.9\to4.4\pm1.9$ (p. 418). The authors doubt an effect as large as 10.2 and say the shrinkage shows how weak the information was. Footnote: the second data point has empirical rate $1/5=0.20$ and Bayes-fit probability 0.27; $\sqrt{0.27\cdot0.73/5}=0.20$, so a 0.07 difference "should be of no concern" (p. 418).

**Voting example (continued, pp. 418–419).** Cauchy, $t_7$ and normal priors (center 0, scale 10 constant, 2.5 others) all do a reasonable job at stabilizing the 1964 coefficient of black while leaving other years (1952–2000) essentially unchanged (Figure 16.4, p. 419).

**Default vs actual prior knowledge (pp. 418–419).** Cauchy(0, 2.5) is not their real prior: they knew blacks were less likely to vote Republican (negative coefficient), data from other years would inform a given year (they would guess the 2004 coefficient is probably between $-2$ and $-5$), and the 1964 Republican candidate's racial stance would predict very poor polling among African Americans. They are comfortable with a default that omits this, and one could add it, e.g. via a hierarchical model across years (p. 419).

### 16.4 Overdispersed Poisson regression for police stops (pp. 420–422)
**Data.** The NY State Attorney General's Office studied "stop and frisk" in 1999. About 175,000 stop records for 15 months in 1998–1999. Analysis focuses on blacks, hispanics and whites; "other" (about 4% of stops) is excluded because small misclassification rates could distort it (p. 420).

**Aggregate.** Blacks and hispanics were 51% and 33% of stops but 26% and 24% of the population. Using 1997 DCJS arrests as a proxy for crime, stops-to-arrests ratios were 1.24 (whites), 1.54 (blacks), 1.72 (hispanics): blacks stopped 23% and hispanics 39% more often than whites (p. 420).

**Regression controlling for precincts.** Citywide ratios could differ even if stops depended only on location. The authors fit hierarchical models over 75 precincts, separately for precincts $<10\%$ black, 10–40%, $>40\%$ (about a third each) (p. 420). For ethnic group $e=1,2,3$ and precinct $p$, with $n_{ep}$ = DCJS arrests (times 15/12) as offset:
$$y_{ep}\sim\text{Poisson}\big(n_{ep}e^{\alpha_e+\beta_p+\epsilon_{ep}}\big),\quad\beta_p\sim N(0,\sigma_\beta^2),\quad\epsilon_{ep}\sim N(0,\sigma_\epsilon^2).\tag{16.12}$$
$\alpha_e$: ethnic groups; $\beta_p$: precinct variation; $\epsilon_{ep}$: overdispersion. Of interest: $\exp(\alpha_e)$, the relative rate of stops to arrests after controlling for precinct (p. 421). The model was fit for four crime types (violent, weapons, property, drug; baseline previous year's arrests of that type) $\times$ three precinct categories = 12 subsets, using Bugs (p. 421). The ordering of groups is the same in all precinct categories for each crime type. Adding the month of arrest added nothing informative (p. 421).

**Results (Figure 16.5).** For violent crimes (25% of stops) and weapons offenses (44%): blacks and hispanics stopped 2.5 and 1.9 times as often as whites (violent), and 1.8 and 1.6 times (weapons), in all precinct categories (p. 422). Whites are slightly more often stopped for property crimes and more often for drug crimes, relative to previous-year arrests (p. 422).

**Interpretation.** Asked whether this implies the NYPD acted unfairly or racist, the authors answer "Not at all": effective policing may require many stops to gather information. The quantitative pattern is still relevant, and the police can explain their policies to affected communities (p. 422).

> *Intuition note.* The offset turns a count model into a rate-per-arrest model. $\exp(\alpha_e)$ is then a stop rate per arrest, with precinct effects removed and extra-Poisson noise absorbed by $\epsilon_{ep}$.

### 16.5 State-level opinions from national polls (pp. 422–423)
Illustrates the analysis of variance (Section 15.6) for hierarchical GLMs. Two steps (p. 422):
1. Fit a regression for individual response $y$ given demographics and state, giving an average response $\theta_j$ for each of $2\times2\times4\times4\times50=3200$ categories (sex, ethnicity, age, education, state).
2. Weight by census adult populations: $\theta_s=\sum_{j\in s}N_j\theta_j/\sum_{j\in s}N_j$, summing over the 64 demographic categories in state $s$.

Many categories are needed (state-level output and nonresponse adjustment), so many cells have little or no data; a multilevel model handles this, and each batch of coefficients gets a variance component (p. 422). Outcome: probability of preferring the Republican candidate in seven CBS polls in the week before the 1988 election, $\Pr(y_i=1)=\mathrm{logit}^{-1}(X_i\beta)$, undecideds excluded. $X$ has 0/1 indicators for sex, ethnicity, age, education, sex×ethnicity, age×education, 50 states, 4 regions (states nested in regions, so no state main effects needed). Each batch of coefficients gets an independent normal prior centered at zero with sd estimated hierarchically under a uniform prior (pp. 422–423).

Results (Figure 16.6): ethnicity is by far the most important demographic factor, state also explains much; adding interactions shows surprisingly large ethnicity×state×region effects, i.e. differences between African Americans and others vary dramatically by state (p. 423).

### 16.6 Multivariate and multinomial responses (pp. 423–428)
**Meta-analysis with binomial outcomes (22 trials, pp. 423–425).** Each trial gives a 2×2 table of death/survival by treatment. Section 5.6 used a normal approximation to the log-odds ratio and ignored average death rates; this can matter if average rates correlate with treatment effects (pp. 423–424).

*Data model:* $y_{ij}|n_{ij},p_{ij}\sim\mathrm{Bin}(n_{ij},p_{ij})$, $i=0,1$ (1 = treated), $j=1..22$. Negative log-odds ratios mean fewer deaths under treatment (p. 424). The 44 parameters $p_{ij}$ come in 22 pairs and are put on the logit scale, then transformed:
$$\beta_{1j}=(\mathrm{logit}(p_{0j})+\mathrm{logit}(p_{1j}))/2,\qquad\beta_{2j}=\mathrm{logit}(p_{1j})-\mathrm{logit}(p_{0j}).\tag{16.13}$$
$\beta_{2j}$ corresponds to $\theta_j$ of Section 5.6. The 22 exchangeable pairs follow a bivariate normal with unknown parameters:
$$p(\beta|\alpha,\Lambda)=\prod_{j=1}^{22}N\!\left(\begin{pmatrix}\beta_{1j}\\\beta_{2j}\end{pmatrix}\Big|\begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix},\Lambda\right).$$
This is equivalent to a normal model on $(\mathrm{logit}\,p_{0j},\mathrm{logit}\,p_{1j})$, but the linear transformation should leave the $\beta$'s roughly independent, making inference less sensitive to the prior on their correlation (p. 424).

*Hyperprior:* uniform on $\alpha_1,\alpha_2$; independent uniform priors on the variances $\Lambda_{11},\Lambda_{22}$ and on the correlation $\rho_{12}=\Lambda_{12}/(\Lambda_{11}\Lambda_{22})^{1/2}$. The posterior is proper (Exercise 16.9) (p. 424).

*Computation:* parameterized by $\beta,\alpha,\log\Lambda_{11},\log\Lambda_{22}$ and Fisher's $z$, $\frac12\log\frac{1+\rho_{12}}{1-\rho_{12}}$. Starting points from conditional-mode approximation plus importance resampling; ten parallel Metropolis runs with a normal jumping kernel (covariance from curvature at the mode) scaled by $2.4/\sqrt{49}$ (49-dimensional); 40,000 iterations; $\hat R<1.2$ for all parameters and $<1.1$ for most. 200,000 draws from the second halves summarise Table 16.2 (pp. 424–425). The authors note Stan could fit this easily and that their method is almost certainly not the most efficient (p. 424).

*Results:* $\rho_{12}$ posterior median 0.21 (2.5%–97.5%: $-0.61$ to $0.91$), "considerable variability". Other medians: $\alpha_1=-2.34$ (mean of average logits), $\sqrt{\Lambda_{11}}=0.55$, $\alpha_2=-0.24$ (mean effect), $\sqrt{\Lambda_{22}}=0.16$. So, the authors say, the multivariate model would have only a small effect on inferences; the exact analysis fixes deficiencies of the normal approximation but does not markedly change the essential inferences (Table 16.2, p. 425).

**Multinomial logistic extension (p. 426).** $y_i\sim\mathrm{Multin}(n_i;\alpha_{i1},\dots,\alpha_{ik})$, $\sum_j\alpha_{ij}=1$. With baseline category 1:
$$\log(\alpha_{ij}/\alpha_{i1})=\eta_{ij}=X_i\beta^{(j)},\qquad p(y|\beta)\propto\prod_{i=1}^n\prod_{j=1}^k\left(\frac{e^{\eta_{ij}}}{\sum_{l=1}^ke^{\eta_{il}}}\right)^{y_{ij}},$$
with $\beta^{(1)}=0$ so $\eta_{i1}=0$. With category indicators: $\eta_{ij}=\delta_j+X_i\beta^{(j)}$, $\delta_1,\beta^{(1)}$ typically 0 (p. 426).

**Ordered categories.** For ordinal data (grades) rather than nominal (diseases), use cumulative probabilities $\pi_{ij}=\sum_{l\le j}\alpha_{il}$: $\log\frac{\pi_{ij}}{1-\pi_{ij}}=\delta_j+X_i\beta^{(j)}$, $\delta_1=\beta^{(1)}=0$ typically. A common $\beta^{(j)}=\beta$ "may be reasonable". The multinomial probit is another common choice; both have latent-variable forms (p. 426).

**Poisson for multinomial.** If $y_1..y_k$ are independent Poisson with means $\lambda_j$, then given $n=\sum y_j$,
$$p(y|n,\alpha)=\mathrm{Multin}(y|n;\alpha_1,\dots,\alpha_k),\quad\alpha_j=\lambda_j/\textstyle\sum_i\lambda_i.\tag{16.14}$$
Multinomial data can be fitted by Poisson GLMs by adding covariates with uniform-prior coefficients that impose the sum constraint (p. 426).

> *Intuition note.* Independent counts, once you fix their total, are exactly a multinomial. So software for Poisson regression can be reused for categorical outcomes, if the total is enforced.

**World Cup chess (pp. 427–428).** 1988–89: six round-robin tournaments, 29 players, 16–18 players each, 789 games; recorded: players, outcome (win/lose/draw), who moved first (Table 16.3 gives a subset aggregated over tournaments) (p. 427). The Bradley–Terry model has $p_{ij}=\exp(\alpha_i-\alpha_j)/(1+\exp(\alpha_i-\alpha_j))$. With draws and first-move effect (i moves first):
$$p_{ij1}=\frac{e^{\alpha_i}}{D_{ij}},\quad p_{ij2}=\frac{e^{\alpha_j+\gamma}}{D_{ij}},\quad p_{ij3}=\frac{e^{\delta+\frac12(\alpha_i+\alpha_j+\gamma)}}{D_{ij}},\tag{16.15}$$
$D_{ij}=e^{\alpha_i}+e^{\alpha_j+\gamma}+e^{\delta+\frac12(\alpha_i+\alpha_j+\gamma)}$; $\gamma$ is the first-move advantage or disadvantage, $\delta$ governs draws (p. 427). (added step) In (16.15), $\gamma$ enters the numerator for $j$'s win, so a positive $\gamma$ favours the player not moving first.

*Poisson form.* $y_{ijk}$ ($k=1,2,3$: wins, losses, draws for $i$ with first move) are independent Poisson with mean $\mu_{ijk}=n_{ij}p_{ijk}$ ($n_{ij}$ games with $i$ first). With $A_{ij}=\log D_{ij}$ (p. 428):
$$\log\mu_{ij1}=\log n_{ij}+\alpha_i-A_{ij},\quad\log\mu_{ij2}=\log n_{ij}+\alpha_j+\gamma-A_{ij},\quad\log\mu_{ij3}=\log n_{ij}+\delta+\tfrac12\alpha_i+\tfrac12\alpha_j+\tfrac12\gamma-A_{ij}.\tag{16.16}$$
*Setup:* $y$ has length $3\times29\times28$. $\beta$ contains the 29 $\alpha_i$, $\gamma$, $\delta$ and $29\times28$ nuisance $A_{ij}$. As the author describes it, the $\alpha_1$ column of $X$ is 1 in rows for a win by player 1 and 0.5 for a draw; the $\delta$ column is 1 for draws. Each $A_{ij}$ column is 1 for the three rows of games with $i$ first. The $A_{ij}$ are not sampled; they enforce $y_{ij1}+y_{ij2}+y_{ij3}=n_{ij}$. $\log n_{ij}$ is an offset with coefficient 1. With noninformative priors the model is overparameterized (adding a constant to every $\alpha_i$ changes nothing); require $\alpha_1=0$ and set one $A_{ij}$ to zero. With varying (hierarchical) abilities, $\alpha_1=0$ is no longer needed (p. 428).

### 16.7 Loglinear models for multivariate discrete data (pp. 428–431)
Loglinear models describe association among categorical variables. Counts in a contingency table are Poisson (or multinomial if the total or some margins are fixed by design), and $\log$ means follow a linear model in indicators. They are a GLM special case, treated separately because they are common (especially for multiple imputation, Chapter 18) and because an alternative computing strategy exists for expected counts with a conjugate prior (p. 428).

**Likelihood.** For $y=(y_1..y_n)$ cells, expected counts $\mu$: $p(y|\mu)=\prod_i\frac1{y_i!}\mu_i^{y_i}e^{-\mu_i}$. If the total is fixed use a multinomial (16.14); fixed margins can give products of multinomials (e.g. exactly 500 respondents in each of four regions) (p. 429).

**Design matrix.** $\log\mu=X\beta$ with known 0/1 incidence matrix $X$; no structural zeros. For a noninformative prior, a $k$-category variable gets $k-1$ indicators; interactions are products of main-effect columns (p. 429). *Saturated* model: all effects and interactions (as many parameters as cells under a noninformative prior; more under informative or hierarchical priors since all $k$ categories are included). *Null*: equal cell probabilities (constant only). *Independence*: one-way effects only. With $z_1,z_2,z_3$, a model with $z_1z_3$ and $z_2z_3$ interactions only makes $z_1,z_2$ conditionally independent given $z_3$ (p. 429).

**Priors.** Conjugate, Dirichlet-like:
$$p(\mu)\propto\prod_{i=1}^n\mu_i^{k_i-1},\tag{16.17}$$
with $p(\mu)=0$ unless some $\beta$ gives $\log\mu=X\beta$. For Poisson sampling there is no constraint $\sum\mu_i=1$. Values $k_i\in(0,1)$ are commonly used as noninformative priors (pp. 429–430). Nonconjugate priors (e.g. exchangeable high-order interactions) do not fit the special methods below (p. 430).

**Finding the mode (pp. 430).** Start from crude estimates, e.g. standard loglinear software on the data supplemented by prior counts $k_i$. Closed forms: saturated model, expected = observed counts; null model, all equal $\sum y_i/n$; independence model, from marginal totals. Otherwise use *iterative proportional fitting* (IPF): refine expected counts $\mu$ by scale factors. Use $\gamma_j=\exp(\beta_j)$, $y_{j+}=\sum_ix_{ij}(y_i+k_i)$, start at $\beta=0$ ($\mu=1$). One parameter is updated at a time:
$$\gamma_j^{\text{new}}=\frac{y_{j+}}{\sum_{i=1}^nx_{ij}\mu_i^{\text{old}}}\gamma_j^{\text{old}},\qquad\mu_i^{\text{new}}=\mu_i^{\text{old}}\left(\frac{\gamma_j^{\text{new}}}{\gamma_j^{\text{old}}}\right)^{x_{ij}}.\tag{16.18}$$
Cycle through $j$; the tables converge to the posterior mode. Each step matches a margin (sufficient statistic). Random zeros are generally not a problem unless the saturated model is fitted or all cells needed for a parameter are zero (p. 430).

**Bayesian IPF (p. 431).** A Gibbs sampler on $\gamma$. Start at $\gamma_j=1$ (always safe; the initial choice must not carry structure for interactions absent from the model). Update
$$\gamma_j^{\text{new}}=\frac{A}{2y_{j+}}\,\frac{y_{j+}}{\sum_{i=1}^nx_{ij}\mu_i^{\text{old}}}\,\gamma_j^{\text{old}},\qquad A\sim\chi^2_{2y_{j+}},$$
then update $\mu$ by (16.18). The tables converge to draws from the posterior of $\mu$. For multinomial data, rescale $\mu$ to the right total after each step (the intercept $\gamma_j$ need not be sampled); product multinomials have several parameters fixed by margins. The method applies only to categorical measurements; with mixed data use a normal linear model (continuous outcome) or a GLM (categorical outcome) (p. 431).

> *Intuition note.* IPF repeatedly rescales the table so one margin matches its target, cycling through margins. The Bayesian version multiplies each rescaling by a random factor $A/(2y_{j+})$ with mean 1, which turns the optimiser into a sampler.

### 16.8 Bibliographic note (pp. 431–432)
Cites Nelder and Wedderburn (1972) for the term GLM; McCullagh and Nelder (1989); Gelman, Jakulin et al. (2008) for the Cauchy prior; Gelman and Rubin (1991) for Bayesian IPF; Bradley and Terry (1952) and Davidson and Beaver (1977) for paired comparisons; Deming and Stephan (1940) for IPF (pp. 431–432).

## Toy example (ours, not from the text)
**Goal:** one pseudodata step for a logistic regression with only an intercept, then the effect of a normal prior row.

Data: one binomial unit, $n=10$, $y=3$. Start at $\hat\eta=0$.
- $e^{0}/(1+e^{0})=0.5$. $L'=y-n\cdot0.5=3-5=-2$. $L''=-n\cdot e^{0}/(1+e^{0})^2=-10\cdot0.25=-2.5$.
- (16.4): $z=0-(-2)/(-2.5)=-0.8$; $\sigma^2=-1/(-2.5)=0.4$. The binomial formulas agree: $z=0+\frac{4}{1}(0.3-0.5)=-0.8$, $\sigma^2=\frac1{10}\cdot4=0.4$.
- With no prior, the weighted regression of one point on a constant gives $\hat\beta=z=-0.8$.
- Second iteration at $\hat\eta=-0.8$: $e^{-0.8}\approx0.4493$, $p=0.4493/1.4493\approx0.310$. $L'=3-3.10=-0.10$, $L''=-10\cdot0.310\cdot0.690\approx-2.139$. $z=-0.8-(-0.10)/(-2.139)=-0.8-0.047\approx-0.847$.
- True MLE: $\log(0.3/0.7)=-0.847$. Newton converged in two steps.

Now add a normal prior $\beta\sim N(0,1)$ as one extra row in (16.7), from the start $\hat\eta=0$: $z_*=(-0.8,\,0)$, $X_*=(1,1)^T$, weights $w_*=(1/0.4,\,1/1)=(2.5,\,1)$.
- Weighted least squares: $\hat\beta=\frac{2.5(-0.8)+1(0)}{2.5+1}=\frac{-2}{3.5}\approx-0.571$ after this step. This is shrunk toward the prior mean 0. With more steps it would settle on the posterior mode, which we did not compute.

## Concepts
- [[generalized-linear-model]] (new) — linear predictor, link function and random component with mean $\mu=g^{-1}(X\beta)$ (p. 405)
- [[link-function]] (new) — maps the mean to the linear predictor scale; canonical link = the one in the exponential-family exponent (pp. 405, 407)
- [[offset]] (new) — predictor with known coefficient 1, e.g. $\log T$ for exposure (p. 407)
- [[latent-data-representation]] (new) — discrete outcome as a thresholded unobserved continuous variable; gives Gibbs for probit (p. 408)
- [[normal-approximation-pseudodata]] (new) — replace each GLM observation by $z_i,\sigma_i^2$ from the local slope and curvature of the log-likelihood; iterate to the mode (pp. 410–411)
- [[separation]] (new) — a linear combination of predictors predicts the outcome perfectly; the MLE can be undefined or unreasonable (−∞ in the 1964 voting example) (p. 412)
- [[weakly-informative-prior]] (new) — default prior (Cauchy on standardized inputs) giving minimal information that constrains coefficients away from unrealistic extremes (pp. 412, 416)
- [[overdispersion]] (new) — variation beyond the sampling distribution; handled by hierarchical or per-observation error terms (p. 407)
- [[multinomial-logit-and-poisson-trick]] (new) — categorical data via baseline-category logits or conditional-Poisson equivalence (pp. 426–428)
- [[loglinear-model]] (new) — Poisson model with $\log\mu=X\beta$ for cross-classified counts (pp. 428–429)
- [[iterative-proportional-fitting]] (new) — cyclic margin-matching algorithm for the mode; Bayesian IPF is Gibbs (pp. 430–431)
- [[bayesian-anova-display]] (new) — standard deviations of batches of coefficients to show factor importance (pp. 422–423)
- [[conjugate-prior]] — hypothetical data $(y_0,X_0)$ for GLM; Dirichlet-like prior for loglinear counts (pp. 409, 429)
- [[hierarchical-multilevel-model]] — normal prior on coefficients with hyperparameters estimated from data (p. 409)
- [[partial-pooling-shrinkage]] — the weak prior shrinks the bioassay slope from 10.2 to 5.4 (p. 418)
- [[gibbs-sampling]] — truncated-normal latent data; Bayesian IPF (pp. 408, 431)
- [[metropolis-hastings]] — Metropolis runs for the meta-analysis (p. 424)
- [[convergence-diagnostics]] — $\hat R$ below 1.2 (p. 424)

## Canonical instances
- [[bioassay-logistic]] — default prior changes the slope $10.2\pm6.4\to5.4\pm2.2$ (pp. 417–418)
- [[vote-1964-separation]] — complete separation, MLE $-\infty$, stabilised by weak priors (pp. 412–413, 418–419)
- [[nyc-stop-and-frisk]] — overdispersed hierarchical Poisson with offset (pp. 420–422)
- [[cbs-1988-state-opinion]] — multilevel logistic regression with Anova display (pp. 422–423)
- [[beta-blocker-meta-analysis]] — bivariate normal hierarchical model on logits (pp. 423–425)
- [[world-cup-chess]] — Bradley–Terry with draws as a Poisson regression (pp. 427–428)

## Bridges (candidates)
- [same-math] pseudodata weighted regression (16.4) ↔ optimization: Newton/Fisher-scoring step (iteratively reweighted least squares) — the text says iterating equals Newton's method on the log posterior (p. 411)
- [same-math] adding $J$ prior rows to the regression (16.7) ↔ ridge-type penalized regression: normal prior as data augmentation — same weighted least-squares algebra
- [structural-analogy] Cauchy(0, 2.5) default prior ↔ regularization in machine learning: shrinking coefficients away from extremes
- [same-math] Poisson conditional on total = multinomial (16.14) ↔ probability: standard distribution relation
- [structural-analogy] Bayesian IPF ↔ Gibbs sampling: cycling over one parameter at a time with a random rescaling

## Questions this raises
- How should a default prior's scale be chosen for other link functions, or when inputs are not standardizable (e.g. rare binary predictors)?
- When does the normal approximation to a GLM likelihood fail badly (e.g. small counts), and how much does variational Bayes or expectation propagation improve on it?
- In the police-stop analysis, what does "arrests as a baseline" assume about the link between crime and arrests, and how sensitive are the ratios to that proxy?
- How do the choices of cutpoint parameterization and identification restrictions interact with a hierarchical prior?

## Exercises worth doing
- Ex. 1 (p. 432) — derive the pseudodata formulas (16.4) from the Taylor expansion — difficulty: easy
- Ex. 3 (p. 433) — bioassay with an extra normal error on the logit scale; effect of overdispersion on conclusions — difficulty: medium
- Ex. 6 (p. 433) — fake-data simulation: Metropolis for Poisson regression with Cauchy priors, then negative binomial extension — difficulty: medium
- Ex. 7 (p. 433) — paired comparisons on the chess subset, up to fitting the Section 16.6 model — difficulty: medium
- Ex. 8 (p. 434) — prove IPF increases the posterior and that Bayesian IPF is a Gibbs sampler — difficulty: hard
- Ex. 9 (p. 434) — show the meta-analysis posterior is proper — difficulty: hard
- Ex. 10–11 (p. 434) — variational Bayes and HMC for probit regression (arsenic data) — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 415 = printed 405). Page labels gave printed numbers directly.
- p. 408: the logistic density is printed as $1/(e^{x/2}+e^{-x/2})$, described as the derivative of the inverse logit. That derivative has a squared denominator, so the square seems to be missing in the print. I copied the logic, not the formula.
- p. 415, (16.9): the last term appears in the image as "$-p(\sigma_j|\nu_j,s_j)$", without a log. It is likely meant as a log prior density, but I reproduced it as printed.
- p. 420: the text says blacks are stopped "23% more" than whites, but $1.54/1.24\approx1.24$ from the printed ratios; probably rounding of unrounded ratios. The hispanic figure (39%) matches.
- The text layer shows $\omega$ in several places (pp. 416, 422, 424, 427, 433) where the page images show $\theta$; I followed the images.
- Equations (14.7) and Sections 13.5, 14.8 are referred to but not part of this unit.
- Section heading 16.5 is printed "opinons" (typo). The text layer was garbled in places (equations, Greek letters); all equations were checked against the page images.
