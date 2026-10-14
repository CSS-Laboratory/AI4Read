---
id: mcelreath-2020-rethinking/ch13-adventures
work: mcelreath-2020-rethinking
unit: "Chapter 13. Adventures in Covariance"
pages: 387–421
fields: [bayesian]
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
# Adventures in Covariance (varying slopes, non-centered parameterization, Gaussian processes)

## L0 — One line
Give all varying effects of a unit (intercepts and slopes) one joint multivariate Gaussian prior whose covariance is learned from data, so the model pools information across units and across parameter types; Gaussian processes extend this to continuous "distances".

## L1 — The gist (≤ 120 words)
Chapter 12's varying intercepts pool information among units. This chapter asks how to pool slopes too, and how to let intercepts and slopes inform each other. The answer is a joint multivariate Gaussian prior for the varying effects. Its covariance matrix is built from standard deviations and a correlation matrix with an LKJcorr prior (a prior family for correlation matrices), and it is learned from the data. Examples: simulated cafés, UC Berkeley admissions, chimpanzees. A non-centered parameterization (an equivalent rewriting of the model) can make sampling more efficient. Gaussian processes then extend varying effects to continuous dimensions such as geographic distance, where covariance falls with distance. Every unit gets its own response, and estimates still borrow strength.

**Prerequisites:** partial pooling and varying intercepts (Ch. 12); multivariate Gaussian, covariance vs correlation; matrix multiplication; logit and Poisson GLMs; MCMC output (n_eff, divergences); WAIC.

## L2 — Key ideas (5–10 bullets)
- Any batch of parameters with exchangeable (arbitrarily labelled) indices can be pooled, slopes as well as intercepts. Pooling is done by estimating the population distribution along with the units (p. 387).
- Intercepts and slopes can covary in the population (as for the cafés), so a joint 2-D Gaussian prior lets what is learned about one improve the other (pp. 387–389).
- The covariance matrix S is factored as S = diag(σ) R diag(σ), with σ the standard deviations and R the correlation matrix. R gets an LKJcorr(η) prior (a one-parameter prior family for correlation matrices), which is skeptical of extreme correlations when η > 1 (pp. 393–394).
- Shrinkage in this model happens in two dimensions and is not straight toward the center. It follows the estimated correlation, and it carries over to the outcome scale (pp. 396–397).
- In the UCB data, the varying-slopes model wins on WAIC (an estimate of out-of-sample accuracy) although the average gender slope is near zero. Variation in slopes is what matters (pp. 400–403).
- The centered and non-centered parameterizations (the second moves the standard deviations and correlations out of the prior into the linear model) are the same model but sample differently. The non-centered form removed all divergent iterations (warnings that sampling is inefficient) and gave far larger n_eff (effective sample size) for the chimpanzee model (pp. 405–406, 408–410).
- A Gaussian process uses a kernel (a formula for the covariance between two units) $K_{ij}=\eta^2\exp(-\rho^2D_{ij}^2)+\delta_{ij}\sigma^2$ so that covariance falls with distance. It gives a varying intercept for each society while allowing for non-independence (pp. 411–416).
- The Gaussian process is descriptive. Its output is compatible with many causal explanations (p. 418).

## L3 — Walkthrough

### Introduction (pp. 387–389)
- **Coffee robot.** A robot visits cafés and records wait times. With $A_i$ a 0/1 indicator for afternoon, the model is $\mu_i=\alpha_{\text{café}[i]}+\beta_{\text{café}[i]}A_i$. Each slope is the expected afternoon-minus-morning difference for a café (p. 387).
- **Varying effects strategy.** The robot learns intercepts better by pooling, and it learns slopes better the same way: estimate the population distribution of slopes while estimating each slope. Any batch of parameters with *exchangeable* index values can and probably should be pooled. "Exchangeable" means the indices have no true ordering and are arbitrary labels (p. 387).
- **Covariation.** At a popular café the morning wait (intercept) is long and the afternoon is much shorter, so the slope is far from zero. At an unpopular café both are small. Across the population, intercepts and slopes covary (pp. 387–388, Fig. 13.1).
- **Why it helps.** If the robot arrives at a new café and sees a long morning wait, it can update its expectation for the afternoon before ordering. In this population a long morning wait goes with a shorter afternoon wait (p. 388).
- **Claims about the method.** Varying-slopes models are "massive interaction machines": each unit has its own response while pooling improves estimates. When slope variation is large, the average slope is of less interest. The pattern of slope variation sometimes hints at omitted variables (p. 388).
- **Preview.** The same machinery is later used for *Gaussian processes*, which handle continuous categories such as age or location. Ordinary varying effects work only with discrete, unordered categories (pp. 388–389).

### 13.1 Varying slopes by construction (pp. 389–398)
**Main idea.** To pool across intercepts and slopes, model their joint population, that is, their covariance. The device is a joint multivariate Gaussian for all varying effects (p. 389).

**Rethinking: Why Gaussian?** The multivariate distribution need not be Gaussian. Practically, few multivariate distributions are easy to use (the common ones are multivariate Gaussian and Student t). Epistemologically, if all we want to say is the means, variances and covariances, the maximum entropy distribution is multivariate Gaussian (p. 389).

**13.1.1 Simulate the population (pp. 389–391).**
- Population values: average morning wait `a = 3.5`; average afternoon difference `b = -1`; `sigma_a = 1`; `sigma_b = 0.5`; `rho = -0.7` (R code 13.1). Mean vector `Mu <- c(a, b)` (p. 390).
- Covariance matrix (p. 390):
$$\begin{pmatrix}\sigma_\alpha^2 & \sigma_\alpha\sigma_\beta\rho\\ \sigma_\alpha\sigma_\beta\rho & \sigma_\beta^2\end{pmatrix}$$
  Variances lie on the diagonal. The off-diagonal covariance is the product of the two standard deviations and the correlation. An ordinary variance can be imagined as the covariance of a variable with itself (p. 390).
- Two ways to build it in R. First, directly with `matrix(c(sigma_a^2,cov_ab,cov_ab,sigma_b^2), ncol=2)`; R fills matrices column by column. Second, with the standard deviations and correlations separate, then multiplied: `Sigma <- diag(sigmas) %*% Rho %*% diag(sigmas)` (R code 13.3–13.5). The author will use the second form for priors (p. 390).
- `N_cafes <- 20`. `vary_effects <- mvrnorm(N_cafes, Mu, Sigma)` (seed 5) is a 20×2 matrix. Column 1 holds intercepts and column 2 slopes (p. 391). Fig. 13.2 plots them with ellipse contours of the population. On average the sample correlation is −0.7, though a single simulation may not show it clearly (pp. 391–392).

**13.1.2 Simulate observations (pp. 391–392).**
- 10 visits per café, 5 morning and 5 afternoon. `mu <- a_cafe[cafe_id] + b_cafe[cafe_id]*afternoon`, within-café `sigma <- 0.5`, `wait <- rnorm(N_visits*N_cafes, mu, sigma)` (p. 392).
- The data are balanced here, but need not be. Lack of balance can favor varying effects, because partial pooling uses population information where it is most needed (p. 392).
- **Rethinking: Simulation and misspecification.** Real models are always misspecified. Simulation can explore how models that do not match the generating process perform. In a Bayesian model the likelihood is "merely a prior for the data", and inference can be insensitive to its details (p. 392).

**13.1.3 The varying slopes model (pp. 392–398).**
$$\begin{aligned}
W_i &\sim \text{Normal}(\mu_i,\sigma)\\
\mu_i &= \alpha_{\text{café}[i]}+\beta_{\text{café}[i]}A_i\\
\begin{bmatrix}\alpha_{\text{café}}\\ \beta_{\text{café}}\end{bmatrix} &\sim \text{MVNormal}\left(\begin{bmatrix}\alpha\\ \beta\end{bmatrix},\mathbf S\right)\\
\mathbf S &= \begin{pmatrix}\sigma_\alpha&0\\0&\sigma_\beta\end{pmatrix}\mathbf R\begin{pmatrix}\sigma_\alpha&0\\0&\sigma_\beta\end{pmatrix}\\
\alpha &\sim \text{Normal}(0,10),\quad \beta\sim\text{Normal}(0,10)\\
\sigma,\sigma_\alpha,\sigma_\beta &\sim \text{HalfCauchy}(0,1)\\
\mathbf R &\sim \text{LKJcorr}(2)
\end{aligned}$$
- The MVNormal line gives each café an intercept and slope drawn from a 2-D Gaussian. This prior "adaptively regularizes" the intercepts, the slopes and their correlation (p. 393). Factoring $\mathbf S$ into standard deviations and $\mathbf R$ makes the inferred structure easier to understand later (p. 393).
- For the 2×2 case, $\mathbf R=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix}$, so there is one parameter to give a prior. The same LKJcorr prior works for larger matrices (p. 393).
- (added step) Multiplying out $\text{diag}(\sigma)\,\mathbf R\,\text{diag}(\sigma)$ gives entry $(i,j)$ equal to $\sigma_i R_{ij}\sigma_j$. This reproduces the matrix on p. 390.
- **LKJcorr(η).** LKJcorr(2) is a weakly informative prior on ρ, skeptical of extreme correlations near −1 or 1. It is a regularizing prior for correlations. η = 1 is flat over all valid correlation matrices. η > 1 makes extreme correlations less likely (p. 394, Fig. 13.3, shown for η = 1, 2, 4). For larger matrices the nature of the distribution stays the same (p. 394).
- **Fit.** `m13.1` uses `dmvnorm2(c(a,b), sigma_cafe, Rho)`, 5000 iterations, 2000 warmup, 2 chains (R code 13.12). Initial "ill-conditioned" and "non-linear transform" warnings are harmless here (p. 395).
- **Posterior correlation.** The posterior of ρ is concentrated on negative values (Fig. 13.4). The model never saw the true intercepts and slopes, only wait times (p. 395). The author suggests trying LKJcorr(1) and LKJcorr(4) or (5) to see the prior's effect (p. 395).
- **Shrinkage.** Compared with unpooled estimates (`a1` = mean morning wait; `b1` = mean afternoon wait minus `a1`), the posterior means are pulled toward the center of the inferred population contours (R code 13.14–13.15; Fig. 13.5 left). Points farther from the center shrink more, because they are less plausible given the inferred population (p. 396).
- **Shrinkage is not straight to the center.** A café with an average intercept but an unusually high slope has its slope shrunk down. Because intercepts and slopes are correlated, this also shrinks its intercept. The angled lines reflect the negative correlation (p. 397).
- **Outcome scale.** Morning wait = `a`, afternoon wait = `a + b` (R code 13.16, Fig. 13.5 right). Shrinkage on the parameter scale produces shrinkage on the outcome scale, and it implies a population of wait times (p. 397).

*Intuition note.* The prior learns that high-intercept cafés tend to have low slopes. So an extreme slope is doubted, and the doubt also moves the intercept. The correlation tilts the pull toward the center.

**Overthinking: Jacobians and transforms (p. 398).** Stan warns about a "non-linear transform of a parameter" because the multivariate prior builds a vector from the named parameters. A parameter transform requires multiplying by the absolute determinant of the Jacobian (the matrix of partial derivatives). Here each parameter is inserted one-to-one in a fixed position, so the absolute Jacobian is exactly 1 and no adjustment is needed (p. 398).

### 13.2 Example: Admission decisions and gender (pp. 398–403)
UCBadmit data from Ch. 10, with `male` as a 0/1 dummy and `dept_id` as an index (R code 13.17, p. 398). Earlier, not modelling department means led to the opposite of the true inference (p. 398).

**13.2.1 Varying intercepts (p. 399).**
$$A_i\sim\text{Binomial}(n_i,p_i),\quad \text{logit}(p_i)=\alpha_{\text{dept}[i]}+\beta m_i,\quad \alpha_{\text{dept}}\sim\text{Normal}(\alpha,\sigma)$$
with $\alpha\sim\text{Normal}(0,10)$, $\beta\sim\text{Normal}(0,1)$, $\sigma\sim\text{HalfCauchy}(0,2)$. Putting $\alpha$ in the linear model is equivalent to putting it in the prior, but then $\alpha_{\text{dept}}$ are displacements from the average department (p. 399). Result (`m13.2`): `bm` mean −0.09 (sd 0.08), similar to Ch. 10. Department intercepts run from 0.67 (A) to −2.61 (F), as deviations from the global mean α (p. 399).

**13.2.2 Varying effects of being male (pp. 399–401).**
$$\text{logit}(p_i)=\alpha_{\text{dept}[i]}+\beta_{\text{dept}[i]}m_i,\quad \begin{bmatrix}\alpha_{\text{dept}}\\ \beta_{\text{dept}}\end{bmatrix}\sim\text{MVNormal}\left(\begin{bmatrix}\alpha\\ \beta\end{bmatrix},\mathbf S\right)$$
with the same factoring of $\mathbf S$, $(\sigma_\alpha,\sigma_\beta)\sim\text{HalfCauchy}(0,2)$ and $\mathbf R\sim\text{LKJcorr}(2)$ (p. 400). The total male slope in department $i$ is $\beta+\beta_{\text{dept}[i]}$ (p. 400).
- Pooling is stronger for cases with fewer applications (p. 400). Department B had only 25 female applications, so its male–female difference shrinks toward the population average. Department F had hundreds of both, so pooling does little (p. 400).
- Fit as `m13.3`. A few divergent iterations may be reported; the next section covers them (p. 400).
- **Result.** Intercepts "range all over the place" while slopes cling near zero. Departments varied a lot in admission rates but neither discriminated much nor varied much in discrimination (p. 401). Departments 1 and 2 are exceptions. Department 1's slope is centered almost 1 log-odds below the mean with no mass on the other side of zero. Department 2's slope is highly uncertain, so it includes plausibly large effects. A marginal posterior that overlaps zero should not be treated as zero (p. 401). These two departments have the largest intercepts (p. 401).

**13.2.3 Shrinkage (pp. 401–402).**
- The posterior correlation between intercepts and slopes has most mass below zero (Fig. 13.6 left). Departments with the highest admission rates have the smallest slopes (p. 401).
- Shrinkage again follows a negative correlation, a weaker one here. A shrinks most because it is most extreme. Department F has an average raw slope but an unusually low intercept. Its intercept moves slightly toward the mean, and its slope moves down because of the negative population correlation (pp. 401–402).
- Overall little shrinkage occurs, because each row has many applications (p. 402).

**13.2.4 Model comparison (p. 402).** `m13.4` ignores gender (R code 13.21). WAIC:

| model | WAIC | pWAIC | dWAIC | weight |
|---|---|---|---|---|
| m13.3 (varying slopes) | 5191.4 | 11.3 | 0.0 | 0.99 |
| m13.4 (no gender) | 5201.2 | 6.0 | 9.8 | 0.01 |
| m13.2 (constant gender effect) | 5201.9 | 7.2 | 10.5 | 0.01 |

`m13.4` and `m13.2` perform alike, and `m13.3` dominates both although its average slope is nearly zero. The individual department slopes matter, not the average. To generalize to new departments, gender is worth attention even if the average slope is near zero (pp. 402–403).

*Intuition note.* A slope that averages to about zero can still be large and positive in some units and negative in others. A model that allows it predicts better than one forcing every unit to share the average.

**13.2.5 More slopes (p. 403).** Each additional predictor with varying slopes adds one dimension to the covariance matrix, that is, one more standard deviation and one more dimension of the correlation matrix (p. 403).

### 13.3 Cross-classified chimpanzees with varying slopes (pp. 403–410)
Chimpanzee data from Ch. 10. There are two cluster types (actors and blocks). Slopes: prosocial option $P$ and the interaction of $P$ with the presence of another chimpanzee $C$ (p. 403). Parameterization is introduced here: "how you fit the model is part of the model", meaning mathematically equivalent forms behave differently in MCMC (p. 403).

**Model (as printed, p. 403).**
$$\begin{aligned}
L_i&\sim\text{Binomial}(1,p_i),\quad \text{logit}(p_i)=\mathcal A_i+(\mathcal B_{P,i}+\mathcal B_{PC,i}C_i)P_i\\
\mathcal A_i&=\alpha+\alpha_{\text{actor}[i]}+\alpha_{\text{block}[i]}\\
\mathcal B_{P,i}&=\beta_P+\beta_{P,\text{actor}[i]}+\beta_{P,\text{block}[i]}\\
\mathcal B_{PC,i}&=\beta_P+\beta_{PC,\text{actor}[i]}+\beta_{PC,\text{block}[i]}
\end{aligned}$$
(The third line shows $\beta_P$ rather than $\beta_{PC}$ in the printed page; see Reading notes.) The sub-models decompose intercepts and slopes into a mean plus offsets for actor and block (p. 404).
- Two priors, one per cluster type, each 3-D with mean zero: $[\alpha_{\text{actor}},\beta_{P,\text{actor}},\beta_{PC,\text{actor}}]^\top\sim\text{MVNormal}(\mathbf 0,\mathbf S_{\text{actor}})$ and likewise for block. Actors and blocks come from different populations. The means $\alpha,\beta_P,\beta_{PC}$ sit in the linear models (p. 404).
- Fixed priors in `m13.6`: `c(a,bp,bpc) ~ dnorm(0,1)`, `dcauchy(0,2)` for the σ's, `dlkjcorr(4)` for both Rho (p. 405).

**Divergent iterations.** `m13.6` gave 559 divergent iterations. Brute force (very long sampling) may give eventual convergence, but sometimes chains never converge. Even when they do, "divergent" iterations signal inefficiency (p. 405).

**Non-centered fix.** `m13.6NC` uses `dmvnormNC`, with no zero mean in the prior. All prior parameters, including Rho, are moved out into the linear model (pp. 405–406). Result: no divergent iterations, faster sampling, same inferences, much larger n_eff (Fig. 13.7; p. 406). For larger data sets the savings can mean hours (p. 406).

*Intuition note.* The two forms describe the same model. The non-centered form samples a standardized version of the effects and rescales them afterwards. In this example the non-centered version sampled much more efficiently (p. 406).

**Parameter count (p. 406).** 54 parameters: 3 average effects, $3\times7$ actor effects, $3\times6$ block effects, 6 standard deviations, 6 free correlations. The model has only about 18 effective parameters by WAIC, because the two populations regularize the varying effects (p. 406). The text later says "56 actual" parameters (p. 407).

**Standard deviations (R code 13.25, p. 407).** Posterior means: actor [1] (intercept) 2.33, [2] 0.46, [3] 0.52; block 0.22, 0.57, 0.51. The small values (several with 89% intervals starting at 0.00) show aggressive shrinkage (p. 407). Overfitting risk is milder than with fixed effects. Variation in slopes may go unnoticed if not checked, even if the average slope is near zero (p. 407).

**`link`.** With several linear models, `link` returns a list of matrices (`p`, `A`, `BP`, `BPC`; each 1000×504). Only `p` is the probability to use for predictions (R code 13.26, p. 407).

**Comparison with `m12.5` (p. 407).** WAIC 532.7 (pWAIC 10.4, weight 0.73) vs `m13.6NC` 534.7 (pWAIC 18.3, dWAIC 2, weight 0.27, dSE 4.1). There is hardly any predictive difference, because slope variation across actors and blocks is small (p. 407). The author suggests one may simplify by varying only the slopes with important variation. "There are no 'correct' models"; understanding data through several models is more useful than finding one true model. Actors vary a lot in baseline left-lever preference. Everything else is much less important. The complex model "tells the correct story" and has not overfit much (p. 408).

**Overthinking: Non-centered parameterization (pp. 408–410).**
- Problem signs for MCMC: low n_eff, high Rhat, divergences. "Non-centered" is the standard but unhelpful name; "standardized adaptive prior" is better (p. 408).
- For a Gaussian, $y\sim\text{Normal}(\mu,\sigma)$ is equivalent to
$$y=\mu+z\sigma,\qquad z\sim\text{Normal}(0,1).$$
- Applied to the model, each varying effect is multiplied by its σ in the linear model, e.g. $\mathcal A_i=\alpha+\alpha_{\text{actor}[i]}\sigma_{\text{actor},1}+\alpha_{\text{block}[i]}\sigma_{\text{block},1}$ (analogously for the two slopes, with $\sigma_{\cdot,2}$ and $\sigma_{\cdot,3}$). The priors then contain only correlation matrices, so they are distributions of correlated z-scores (p. 408). Code `m13.6nc1` needs `start`, `constraints` and `types` lists (p. 409).
- The correlation matrix can also be removed with a **Cholesky decomposition** $\mathbf R=\mathbf L\mathbf L^{\top}$. Multiplying $\mathbf L$ by a vector of uncorrelated samples gives correlated samples. `dmvnormNC` automates this (p. 409).
- **Costs:** the code is harder to read and share, and the effects come out as z-scores needing further processing. Not every model and data combination benefits. Sometimes the centered form is better. The advice is to try the form most natural to you, and if it gives trouble, try another (pp. 409–410).

### 13.4 Continuous categories and the Gaussian process (pp. 410–419)
**Motivation (p. 410).** Discrete categories (cafés, ponds, departments) have no ordering. For continuous dimensions such as age, similar individuals share more exposures, and covariation falls off with dissimilarity. A separate intercept per age ignores this, and every individual may have a unique age. **Gaussian process regression** applies varying effects here. The idea is to define a dimension of difference, measure distances between all pairs of cases, and estimate a *covariance function* of distance (p. 410).

**13.4.1 Spatial autocorrelation in Oceanic tools (pp. 410–418).**
- **Why space matters.** The Ch. 10 binary contact predictor ignores who has contact with whom. If tools were exchanged, tool counts are not independent even after conditioning on predictors, and close neighbors may share unmeasured features such as sources of stone or shell (pp. 410–411).
- **Distance matrix** (thousands of km, as-the-crow-flies; R code 13.29). Diagonal zeros; symmetric. Examples: Malekula–Tikopia 0.5, Hawaii–Yap 7.2 (p. 411).
- **Model (pp. 411–413).**
$$\begin{aligned}
T_i&\sim\text{Poisson}(\lambda_i),\quad \log\lambda_i=\alpha+\gamma_{\text{society}[i]}+\beta_P\log P_i\\
\gamma&\sim\text{MVNormal}\big((0,\dots,0),\mathbf K\big)\\
K_{ij}&=\eta^2\exp(-\rho^2D_{ij}^2)+\delta_{ij}\sigma^2
\end{aligned}$$
  The prior is 10-dimensional (10 societies) with zero means, since the grand mean $\alpha$ is in the linear model (p. 412).
- **Pieces of $K_{ij}$ (p. 412).** $\exp(-\rho^2D_{ij}^2)$: covariance declines exponentially with squared distance, and a large $\rho$ means rapid decline. Squared distance is the most common assumption, being easy to fit and often realistic in letting covariance fall faster as distance grows. Fig. 13.8 compares it with the linear-distance form $\exp(-\rho^2D_{ij})$ at $\rho^2=1$. The squared form is a half-Gaussian that is initially slower than exponential and then becomes faster (p. 412). $\eta^2$ is the maximum covariance between two societies. $\delta_{ij}$ equals 1 if $i=j$ and 0 otherwise, so $\delta_{ij}\sigma^2$ adds extra covariance on the diagonal. It does not matter here (one observation per society), so it is fixed at 0.01 (pp. 412–413).
- **Priors (p. 413).** $\alpha\sim\text{Normal}(0,10)$, $\beta_P\sim\text{Normal}(0,1)$, $\eta^2\sim\text{HalfCauchy}(0,1)$, $\rho^2\sim\text{HalfCauchy}(0,1)$. The priors are defined for the squares and estimated on that scale because it is computationally easier. Half-Cauchy priors are used because $\rho^2$ and $\eta^2$ must be positive. Nothing is special about the Cauchy. Navigation knowledge could give an informative prior on $\rho^2$ (p. 413).
- **Fit `m13.7`** with `g[society] ~ GPL2(Dmat, etasq, rhosq, 0.01)` (p. 414).
- **Estimates (R code 13.32).** `bp` 0.24 (sd 0.12; 89% interval 0.05–0.42), "very much as it was before", suggesting that it is hard to explain all the tools–population association as a side effect of contact. `etasq` mean 0.35, `rhosq` mean 2.67 (sd 51.60, interval 0.01–2.21). The `g` values are on the log-count scale and hard to interpret directly (p. 414).
- **Covariance functions (R code 13.33, Fig. 13.9).** The joint posterior of $\rho^2,\eta^2$ is a posterior over covariance functions. The median is used because the densities are skewed (the `rhosq` mean lies outside its 89% interval). There is a lot of uncertainty about the strength of the spatial effect: curves peaking at twice or half the median peak (about 0.2) are common. The majority of curves decline to zero before 4000 km (pp. 414–415).
- **Implied correlations (R code 13.34–13.35).** K is built from posterior medians, with `diag(K) <- median(etasq) + 0.01`, then converted to a correlation matrix. Malekula, Tikopia and Santa Cruz correlate above 0.8 with each other (0.87, 0.82, 0.92). Hawaii correlates about 0 with all others. Other pairs include Fiji–Tonga 0.76 and Trobriand–Manus 0.72 (p. 416).
- **Maps and plots (R code 13.36–13.37, Fig. 13.10).** Close societies have stronger correlations. The three-society cluster lies below the expected tools for its population, and being close, this is consistent with spatial covariance. The correlations "merely describe" this. Manus and the Trobriands are close, correlated and below expectation. Tonga has more tools than expected, and its proximity to Fiji counteracts some of the pull of Fiji's smaller neighbors. The model seems to think Fiji would have fewer tools if not for Tonga (pp. 417–418).
- **Caveat.** The correlations may reflect other unmeasured commonalities, for example tool stone. Gaussian process regression is "a grand and powerful descriptive model" and its output is always compatible with many different causal explanations (p. 418).

*Intuition note.* The model has no list of causes. It only says that nearby societies have more similar leftover tool counts than distant ones, after accounting for population. Why they are similar is a separate question.

**13.4.2 Other kinds of "distance" (pp. 418–419).**
- Patristic (phylogenetic) distance gives phylogenetic regression as a special case. Network distance can also be used. Periodic functions (sine and cosine) of time distance model cyclical covariation without hard season cutoffs (p. 418).
- The definition of $K$ differs across models, but modelling covariance as a function of distance is common to all. Several distance dimensions can be combined. A Gaussian process merges all influences into one covariance matrix and so one common intercept (p. 418). Moving population size into the process gives
$$K_{ij}=\eta^2\exp\!\Big(-\big(\rho_D^2D_{ij}^2+\rho_P^2(\log P_i-\log P_j)^2\big)\Big)+\delta_{ij}\sigma^2$$
  with separate relevance parameters $\rho_D,\rho_P$. This is called *automatic relevance determination*, which is "no more or less 'automatic'" than other coefficient estimation (p. 419).
- Fancier Gaussian process models are best built directly in Stan or in other tools such as GPstuff, rather than in `map2stan` (p. 419).

### 13.5 Summary (p. 419)
Partial pooling was extended to slopes by modelling covariation in the population of parameters. LKJcorr is a convenient prior family for correlation matrices. Gaussian processes extend varying effects to continuous similarity (spatial, network, phylogenetic or other abstract distance) (p. 419).

### 13.6 Practice (pp. 419–421)
Easy, medium and hard problems follow (see Exercises worth doing).

## Toy example (ours, not from the text)
Use the café population of §13.1.1: mean intercept 3.5, mean slope −1, $\sigma_\alpha=1$, $\sigma_\beta=0.5$, $\rho=-0.7$.

1. Covariance entry: $\sigma_\alpha\sigma_\beta\rho=1\times0.5\times(-0.7)=-0.35$. So $\mathbf S=\begin{pmatrix}1&-0.35\\-0.35&0.25\end{pmatrix}$.
2. Suppose the robot learns a new café has morning intercept 4.5, which is 1.0 above the mean. For a bivariate Gaussian (standard result, not in the text), the expected slope given the intercept is $E[\beta\mid\alpha]=-1+\rho\,\frac{\sigma_\beta}{\sigma_\alpha}(\alpha-3.5)$.
3. This gives $-1+(-0.7)(0.5/1)(1.0)=-1-0.35=-1.35$. The expected afternoon wait is $4.5+(-1.35)=3.15$ minutes. The population mean afternoon wait is $3.5-1=2.5$.
4. With $\rho=0$ the expected slope would stay at −1, and the afternoon wait would be $3.5$. The negative correlation shifts the afternoon expectation by 0.35 minutes. This is the covariation information the varying slopes model lets the robot use.

## Concepts
- [[hierarchical-multilevel-model]] — parameters for groups drawn from a population distribution; here extended to slopes and several cluster types (p. 387)
- [[partial-pooling-shrinkage]] — estimates pulled toward the population center; in 2-D the pull follows the intercept–slope correlation (pp. 396–397)
- [[exchangeability]] — here: index values with no true ordering, arbitrary labels, so a batch can be pooled (p. 387)
- [[varying-slopes-model]] (new) — each unit has its own slope, drawn with its intercept from a joint multivariate Gaussian (p. 393)
- [[covariance-matrix-factorization]] (new) — $\mathbf S=\text{diag}(\sigma)\,\mathbf R\,\text{diag}(\sigma)$: standard deviations and correlation matrix kept separate (p. 393)
- [[lkjcorr-prior]] (new) — one-parameter-η prior on correlation matrices; η = 1 flat, η > 1 skeptical of extreme correlations (p. 394)
- [[principle-of-indifference-maximum-entropy]] — cited as the epistemological reason for a Gaussian: it is the maximum entropy form given only means, variances and covariances (p. 389)
- [[non-centered-parameterization]] (new) — move means, standard deviations and (via Cholesky) correlations out of the prior into the linear model, leaving standardized z-scores (pp. 408–409)
- [[cholesky-decomposition]] (new) — $\mathbf R=\mathbf L\mathbf L^\top$; $\mathbf L$ times uncorrelated samples gives correlated samples (p. 409)
- [[divergent-iterations]] (new) — HMC warnings that signal inefficient sampling of a varying-effects model (p. 405)
- [[convergence-diagnostics]] — n_eff, Rhat and divergences as signs of the sampling problem (p. 408)
- [[cross-validation-loo-waic]] — WAIC used to compare varying slopes with simpler models and to estimate effective parameters (pp. 402, 406–407)
- [[cross-classified-model]] (new) — varying effects for more than one cluster type (actors and blocks) at once (p. 403)
- [[gaussian-process-regression]] (new) — varying intercepts across a continuous dimension, with covariance a function of distance (p. 410)
- [[squared-exponential-kernel]] (new) — $K_{ij}=\eta^2\exp(-\rho^2D_{ij}^2)+\delta_{ij}\sigma^2$ (p. 412)
- [[automatic-relevance-determination]] (new) — a separate relevance parameter for each distance dimension in the kernel (p. 419)
- [[model-misspecification]] (new) — the true generating process differs from the model; simulation can explore it (p. 392)

## Canonical instances
- [[coffee-robot-cafes]] — simulated cafés with correlated morning waits and afternoon changes (pp. 387–397)
- [[ucb-admissions-varying-slopes]] — departments differ in intercepts; slopes near zero but WAIC favors varying slopes (pp. 398–403)
- [[chimpanzees-cross-classified]] — actor and block clusters; centered vs non-centered sampling (pp. 403–410)
- [[oceanic-tools-gaussian-process]] — tool counts with geographic-distance covariance (pp. 410–418)

## Bridges (candidates)
- [structural-analogy] Multivariate Gaussian prior on varying effects ↔ bayesian: the vcov of a quadratic approximation, the same kind of distribution (the text says this, p. 389)
- [same-math] Non-centered form $y=\mu+z\sigma$ and Cholesky-scaled z-scores ↔ sampling from a multivariate Gaussian via $\mathbf L z$ — literally the same algebra (pp. 408–409)
- [structural-analogy] Gaussian-process kernel (covariance falls with distance) ↔ spatial statistics: spatial autocorrelation — covariance as a function of separation
- [structural-analogy] Pooling across intercepts and slopes via correlation ↔ regression toward the mean in two dimensions
- [metaphor] "Massive interaction machines" ↔ interaction terms: every unit gets its own response to the predictor

## Questions this raises
- How sensitive are the pooled estimates to the LKJcorr η, and to the half-Cauchy priors on the σ's?
- When does the centered form sample better than the non-centered one (the text only says "sometimes", p. 410)?
- How can one separate geographic from other causes of the correlation among societies, if the Gaussian process is compatible with many causal stories?
- With many slopes, how large does the covariance matrix get, and when does it stop being practical ("within practical limits", p. 403)?

## Exercises worth doing
- Ex. 13E3 (p. 419) — when can a varying-slopes model have fewer effective parameters than the unpooled-slopes model — difficulty: medium
- Ex. 13M1 (p. 419) — rerun the café simulation with `rho = 0` and read the posterior of the correlation — difficulty: easy
- Ex. 13M2 (p. 420) — compare a model with independent slope and intercept priors to the multivariate prior using WAIC — difficulty: medium
- Ex. 13M3 (p. 420) — refit the UCBadmit varying-slopes model non-centered; compare n_eff and speed — difficulty: medium
- Ex. 13H1 (p. 420) — Bangladesh fertility: varying intercepts and urban slopes by district; interpret the correlation — difficulty: hard
- Ex. 13H4 (p. 421) — simulate new boys from the fitted varying-effects population and plot their trends — difficulty: hard

## Reading notes
- Printed page = pdf page − 14. Pdf 436 (printed 422) is blank. Footnote texts 161–164 are cited in the text but not shown on these pages.
- The model equations on p. 393 and p. 400 are garbled in the text layer; I checked them against the page images.
- **Misprint:** on p. 403 the $\mathcal B_{PC,i}$ sub-model shows $\beta_P$ in place of $\beta_{PC}$ in the first term, as the image shows. The same line on p. 408 also shows $\beta_P$ in the first term. The R code uses `bpc`.
- **Inconsistencies in the source:** the chimpanzee model has "54 parameters" (p. 406) but "56 actual parameters" (p. 407). The text gives the global mean α of `m13.2` as −0.58 (p. 399) while the table shows −0.59. The math on p. 393 uses HalfCauchy(0,1) priors for the σ's, while code 13.12 uses `dcauchy(0,2)`. The text on p. 405 writes `dvnormNC`, but the code uses `dmvnormNC`.
- All code is for the author's `rethinking`/`map2stan` setup as printed. I did not check it.
- Typos in the source: "indictor" (p. 387) and "determinate" for determinant (p. 398).
- The Cholesky factors `L_Rho_actor` and `L_Rho_block` are mentioned only in the Overthinking box (p. 409), as items in the `precis` output.
