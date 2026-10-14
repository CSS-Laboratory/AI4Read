---
id: gelman-2013-bda3/ch15-hierarchical
work: gelman-2013-bda3
unit: "15 Hierarchical linear models"
pages: 381–404
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Hierarchical linear models (BDA3, Chapter 15)

## L0 — One line
When predictors or groupings sit at several levels, give each batch of regression coefficients its own normal population distribution with its own estimated variance; this partial pooling sits between "no pooling" and "complete pooling" and can be run as one big augmented regression.

## L1 — The gist (≤ 120 words)
The chapter asks how to fit regressions when data are grouped (states within regions within years, students within schools, factors in an Anova). Its answer is to group the coefficients into batches. Each batch gets a normal population distribution with its own variance, estimated from the data. A normal prior can be written as extra "observations", so a hierarchical model is one large regression and the usual computing tools apply (Gibbs sampling, EM, Hamiltonian Monte Carlo (HMC), parameter expansion). Examples: election forecasting, business-school grade prediction, web connect times, a latin square. It matters because, in the election example, ignoring grouping gave falsely precise forecasts, and in the business-school example, groups with very sparse data could not be estimated separately by classical regression.

**Prerequisites:** linear regression with normal likelihood and conjugate normal prior (Ch. 14); multivariate normal; scaled inverse-χ² distribution; Gibbs sampling and R̂; posterior predictive checks; the eight-schools model of Section 5.5.

## L2 — Key ideas
- **Batches of exchangeable coefficients.** Each batch of coefficients gets a population distribution $\beta\sim N(1\alpha,\sigma_\beta^2 I)$. This contains "unrelated" ($\sigma_\beta=\infty$) and "all equal" ($\sigma_\beta=0$) as special cases (p. 382).
- **Groupings induce correlation.** Averaging over group indicator coefficients gives within-group correlation. For $\rho\ge0$ this equals the intraclass-correlation model (p. 382–383).
- **Ignoring the grouping can make forecasts falsely precise.** The nonhierarchical election model failed a posterior predictive check on nationwide residuals. Adding year and region × year varying coefficients fixed it (p. 386–388).
- **A normal prior is extra data.** The three-level model is a single regression on $n+J+K$ "observations" (15.3). Rows with noninformative priors can be dropped (p. 389).
- **Varying intercepts and slopes need a prior on a covariance matrix.** A scaled inverse-Wishart (redundant parameterization) separates variances from correlations. Hierarchical pooling made the business-school analysis possible with only about 4% of students in the subgroup (p. 390–392).
- **Computation.** Options are batch-wise Gibbs, all-at-once Gibbs (costly: cost ∝ $nk^2$), parameter expansion (for variances near 0), and decoupling reparameterizations for HMC (p. 392–394).
- **Anova as batching.** Rows of an Anova table are batches with their own $\sigma_m$. The finite-population $s_m$ (variation among the existing coefficients) can be estimated more precisely than the superpopulation $\sigma_m$ (the population they come from), especially when degrees of freedom are low. In the authors' framework, fixed vs. random is a difference in how inferences are used, not in inference or computation (p. 395–400).
- **Hierarchical priors on variance parameters.** A half-Cauchy prior with an estimated scale shrinks the upper ends of the intervals of many weakly identified $\sigma_k$ (p. 399–400).

## L3 — Walkthrough

### Chapter introduction (p. 381–382)
- Hierarchical regression is useful when predictors exist at different levels of variation (student, class, school). It also arises with stratified or cluster sampling. With cluster sampling, hierarchical modeling is necessary to generalize to unsampled clusters (p. 381).
- With predictors at several levels, exchangeability of lowest-level units breaks down. The simplest extension is to add indicator variables for the higher-level units. That multiplies the number of parameters, so sensible estimation needs a population distribution on them. This distribution may be simple i.i.d., or itself a regression on second-level predictors (p. 381).
- The eight-schools problem is a special case. In the notation of Section 5.5: data $y_j$, $j=1..J$; regression coefficients are the school parameters $\theta_j$; $n=J$; $X$ is the $J\times J$ identity; known variances $\sigma_j^2$ (p. 381).
- In regression language, **no pooling** = noninformative uniform prior on the coefficients. **Complete pooling** = common prior with zero variance. The favored hierarchical model is $\beta\sim N(\mu,\tau^2 I)$ (p. 381).
- Throughout the chapter the likelihood is $y\sim N(X\beta,\Sigma_y)$ (p. 381–382).

### 15.1 Regression coefficients exchangeable in batches (p. 382–383)
A **batch** of random effects (or varying coefficients) is a group of coefficients that are exchangeable and have a normal population distribution (p. 382).

**Simple varying-coefficients model.** All of $\beta$ ($J\times1$) is exchangeable:
$$\beta\sim N(1\alpha,\ \sigma_\beta^2 I)\tag{15.1}$$
$\alpha,\sigma_\beta$ are unknown scalars and $1$ is the $J\times1$ vector of ones. It is the eight-schools model with $(\beta,\alpha,\sigma_\beta)$ for $(\theta,\mu,\tau)$. Special cases: unrelated $\beta_j$ ($\sigma_\beta=\infty$) and all equal ($\sigma_\beta=0$) (p. 382).

**Priors.** A uniform prior on $\alpha,\sigma_\beta$ can be reasonable. A uniform prior on $\log\sigma_\beta$ cannot be used, because it gives an improper posterior with its mass near $\sigma_\beta=0$ (Section 5.4). Another fairly noninformative choice is a scaled inverse-χ² prior on $\sigma_\beta^2$ with low degrees of freedom such as 2. Check that inferences are not sensitive to these choices. With little replication at the level of a variance parameter, that parameter is generally poorly estimated and inferences may be sensitive to the prior (p. 382).

**Intraclass correlation.** Suppose $y_1..y_n$ fall into $J$ batches and $y\sim N(\alpha 1,\Sigma_y)$ with $\operatorname{var}(y_i)=\eta^2$. Let $\operatorname{cov}(y_{i_1},y_{i_2})=\rho\eta^2$ if the two are in the same batch, and 0 otherwise. If $\rho\ge0$ this is equivalent to $y\sim N(X\beta,\sigma^2 I)$. Here $X$ is an $n\times J$ indicator matrix ($X_{ij}=1$ if unit $i$ is in batch $j$) and $\beta$ has distribution (15.1). The equivalence holds when
$$\eta^2=\sigma^2+\sigma_\beta^2,\qquad \rho=\sigma_\beta^2/(\sigma^2+\sigma_\beta^2),$$
as seen by deriving the marginal distribution of $y$, averaging over $\beta$. Positive intraclass correlation in a regression can thus be absorbed by adding $J$ indicator variables with coefficient distribution (15.1) (p. 382).

**Mixed-effects model.** The first $J_1$ components of $\beta$ get independent improper priors ("fixed effects", implicitly infinite prior variance). The remaining $J_2=J-J_1$ are exchangeable with common mean $\alpha$ and sd $\sigma_\beta$ (p. 382–383). Footnote 1: "fixed" and "random" come from the non-Bayesian tradition and are somewhat confusing in Bayesian work, where all unknown parameters are treated as random (or, equivalently, as fixed but unknown) (p. 383). Example: eight schools with a uniform prior on the mean $\alpha$ is a mixed-effects model with one constant fixed effect and random effects with mean 0 (p. 383).

**Several sets of varying coefficients.** Split $\beta$ into $K$ clusters, cluster $k$ with mean $\alpha_k$ and sd $\sigma_{\beta k}$. A mixed-effects model sets one cluster's variance to $\infty$ (p. 383).

**Exchangeability.** Exchangeability of units is achieved by conditioning on indicator variables for groupings. Averaging over the varying coefficients induces correlation among outcomes in the same subgroup (p. 383).

*Intuition note.* Each group gets its own offset. The offsets are drawn from one common normal distribution. If you do not know the offsets, then units in the same group look correlated. That is the same as the intraclass-correlation story.

### 15.2 Example: forecasting U.S. presidential elections (p. 383–388)
Plan: fit a nonhierarchical regression, find it inadequate, expand hierarchically (p. 383).

**Data.** Units: results in each state in each of 11 presidential elections 1948–1988. Outcome: Democratic share of the two-party vote. The District of Columbia and states with third-party victories were dropped, leaving 511 units. The model was estimated on elections through 1988 and used to forecast 1992 (p. 383).

**Graphics.** Fig. 15.1a (1984 vs 1988 state votes) is close to linear. Fig. 15.1b (1972 vs 1976) is not. Its outliers are Georgia (Carter's home state) and other Southern states. This suggests adding indicators for candidates' home states and regions (p. 384).

**Preliminary regression.** There are three levels of variation (national, regional, state), so three kinds of predictors (Table 15.1, p. 385):
- *Nationwide*: Sept. poll support; July presidential approval × Inc; approval × Presinc; 2nd-quarter GNP growth × Inc. ("Inc" = +1/−1 for a Democratic/Republican incumbent; "Presinc" = Inc if the incumbent runs, else 0.)
- *Statewide*: Democratic share in the last two elections (as deviations from the national vote), home states of presidential and vice-presidential candidates, legislature majority, state economic growth × Inc, state ideology, ideological compatibility, proportion Catholic in 1960.
- *Regional/subregional*: South, and year-specific South/Deep South/New England/North Central/West indicators.

With 511 observations many state and regional variables can be fitted. Fewer relationships with national variables can be estimated (than with state and regional variables), since for this purpose there are essentially only 11 data points (p. 384). The classical fit could be used to simulate the 1992 vector of 50 state outcomes from posterior draws (p. 385).

**Model check.** The classical model treats the data as 511 independent observations. But if the Democrat does better than expected in Massachusetts in one year, he is expected to do so in Utah too. So exchangeability does not make sense even after controlling for the predictors (p. 385–386). The test quantity is $T(y,\beta)$, the square root of the average of the 11 squared nationwide residuals. Each nationwide residual is the average of $(y_i-X_i\beta)$ over the roughly 50 states in a year. It is compared with $T(y^{rep},\beta)$ (Fig. 15.2). The 200 simulated points lie far below the 45° line. Observed variation in national results is larger than the model implies, so its national forecasts are falsely precise (p. 386).

**Varying-coefficients model.** Add 11 year indicators, exchangeable with mean 0 (a constant is already in the model). The classical model is the special case where their variance is fixed at 0 (p. 386). Add 44 region × year indicators, exchangeable within region, with mean 0. The 11 Southern ones get their own variance and the 33 others share another. In total: 55 new $\beta$ parameters and three new variance components. The year-specific regional corrections of Table 15.1 are dropped (p. 387). For state $s$, region $r(s)$, year $t$:
$$y_{st}\sim N(X_{st}\beta+\gamma_{r(s)t}+\delta_t,\ \sigma^2),\quad
\gamma_{rt}\sim\begin{cases}N(0,\tau_{\gamma1}^2)& r=1,2,3\ (\text{non-South})\\ N(0,\tau_{\gamma2}^2)& r=4\ (\text{South})\end{cases},\quad \delta_t\sim N(0,\tau_\delta^2)\tag{15.2}$$
The hyperprior is uniform on $\beta,\sigma,\tau_{\gamma1},\tau_{\gamma2},\tau_\delta$. A uniform prior on the variances instead gave essentially identical inferences (p. 387). In Section 15.1's notation the augmented coefficient vector is $(\beta,\gamma,\delta)$ with prior mean 0 and $\Sigma_\beta=\operatorname{diag}(\infty,\dots,\infty,\tau_{\gamma1}^2,\dots,\tau_{\gamma2}^2,\dots,\tau_\delta^2,\dots)$. The first 14 elements have $\sigma_{\beta j}=\infty$, the next 33 have $\tau_{\gamma1}$, the 11 Southern have $\tau_{\gamma2}$, and the last 11 have $\tau_\delta$ (p. 387).

**Forecasting 1992.** Predictive inference is subtler because new varying coefficients may be needed for the predicted data. The $50\times20$ matrix of 1992 predictors is padded with 55 columns of zeros (previous-year indicators set to zero). Five new predictors are needed: one year indicator and four region × year indicators. They are not in the estimated $\beta$, so their coefficients are simulated from their population distribution: $N(0,\tau_\delta^2)$, $N(0,\tau_{\gamma1}^2)$ (non-South), $N(0,\tau_{\gamma2}^2)$ (South), using $\tau$ values drawn from the posterior (p. 387).

**Posterior inference.** Fitted with EM and the vector Gibbs sampler (Section 15.5). Ten parallel sequences; after 500 steps, $\hat R<1.1$ for all parameters (p. 387–388). Coefficient estimates are similar to the nonhierarchical fit, and posterior medians all have the expected positive sign. The $\tau$'s are not determined with great precision. This is an advantage of the full Bayesian approach: point estimates of the variance components would ignore a wide range of plausible values (p. 388). For 1992 the model gave an 85% forecast probability that the Democrats would win the national electoral vote. State forecasts had predictive standard errors between 5% and 6% (state-by-state results are in Fig. 6.1, not on these pages) (p. 388). The same posterior predictive check now fits (Fig. 15.3: points scattered evenly about the 45° line) (p. 388).

**Three advantages of the hierarchical model** (p. 388):
1. It models correlation within election years and regions.
2. Including year and region × year terms without a hierarchical model, or omitting them, are the special cases $\tau=\infty$ or $0$. The general model compromises between these extremes.
3. Predictions have additional variability components for region and year, and should therefore be more reliable.

*Intuition note.* The 511 rows are really 11 "experiments" of about 50 related rows. A shared year-level shock widens the forecast uncertainty about the national result. The hierarchical model puts that shock in explicitly, and the data decide how large it is.

### 15.3 Interpreting a normal prior distribution as extra data (p. 388–389)
Further levels can be added. Example: class effects depending on district or state features. For elections, one could model year errors as time trends, though there is probably limited information for that. No serious conceptual or computational difficulties arise from more levels (p. 388–389).

**Three-level model** (p. 389):
- likelihood: $y\mid X,\beta,\Sigma_y\sim N(X\beta,\Sigma_y)$ — $n$ data points
- population distribution: $\beta\mid X_\beta,\alpha,\Sigma_\beta\sim N(X_\beta\alpha,\Sigma_\beta)$ — $J$ parameters
- hyperprior: $\alpha\mid\alpha_0,\Sigma_\alpha\sim N(\alpha_0,\Sigma_\alpha)$ — $K$ parameters

**Single regression.** By conjugacy (Section 14.8), write $y_*\mid X_*,\gamma,\Sigma_*\sim N(X_*\gamma,\Sigma_*)$ with $\gamma=(\beta,\alpha)$ of length $J+K$. The likelihood, population and hyperprior act as $n+J+K$ "observations" about $\gamma$:
$$y_*=\begin{pmatrix}y\\0\\\alpha_0\end{pmatrix},\quad X_*=\begin{pmatrix}X&0\\I_J&-X_\beta\\0&I_K\end{pmatrix},\quad \Sigma_*^{-1}=\begin{pmatrix}\Sigma_y^{-1}&0&0\\0&\Sigma_\beta^{-1}&0\\0&0&\Sigma_\alpha^{-1}\end{pmatrix}\tag{15.3}$$
(added step) Shapes: $y_*$ is $(n+J+K)\times1$; $X_*$ is $(n+J+K)\times(J+K)$; $\Sigma_*^{-1}$ is $(n+J+K)\times(n+J+K)$ (p. 389).

Components of $\beta$ or $\alpha$ with noninformative priors correspond to "observations" with infinite variance. Their rows in $y_*,X_*$ and rows/columns of $\Sigma_*^{-1}$ can be dropped. The regression then has $n+J_*+K_*$ observations ($J_*,K_*$ = numbers of components with informative priors) (p. 389).

**Election example.** $\beta$ has 75 components: 20 predictors (including the constant, excluding the five year-specific regional variables of Table 15.1), 11 year errors, 44 region × year errors. $J_*=55$ because only the year and region × year errors have informative priors. All means are fixed at zero, so $K_*=0$ (p. 389).

**Equivalent set-ups.** Eight schools: $y_j\sim N(\theta_j,\sigma_j^2),\ \theta_j\sim N(\mu,\tau^2)$, or $y_j\sim N(\beta_0+\beta_j,\sigma_j^2),\ \beta_j\sim N(0,\tau^2)$. Election model: a regression with "70 predictors" and normal priors on coefficients, or a regression with 20 predictors and three independent error terms (year, region × year, state × year). Group-level predictors can enter the likelihood or the population distribution, and the constant can sit in any of the three levels (p. 389). (The count 70 differs from 75 above; see Reading notes.)

*Intuition note.* A prior of the form "coefficient ~ N(mean, variance)" acts like an extra data row saying "this coefficient was measured as the mean, with that variance". Stack the rows and an ordinary weighted regression gives the posterior mean.

### 15.4 Varying intercepts and slopes (p. 390–392)
When several parameters vary by group, a multivariate prior is needed. Generic set-up: $J$ groups, likelihood $p(y^{(j)}\mid\theta^{(j)})$, prior $p(\theta_j\mid\phi)$ with hyperparameters $\phi$ (p. 390).

**Varying-intercept, varying-slope model:**
$$y_{ij}\sim N(\alpha_j+x_{ij}\beta_j,\sigma_y^2),\quad \begin{pmatrix}\alpha\\\beta\end{pmatrix}\sim N\!\left(\begin{pmatrix}\mu_\alpha\\\mu_\beta\end{pmatrix},\begin{pmatrix}\sigma_\alpha^2&\rho\sigma_\alpha\sigma_\beta\\\rho\sigma_\alpha\sigma_\beta&\sigma_\beta^2\end{pmatrix}\right)\tag{15.4}$$
The hyperprior on $(\mu_\alpha,\mu_\beta,\sigma_\alpha,\sigma_\beta,\rho)$ probably starts uniform (scales positive, $-1<\rho<1$), with more information added if needed, e.g. when there are few groups (p. 390).

**More than two coefficients:**
$$y_{ij}\sim N(X_j\beta^{(j)},\sigma_y^2),\qquad \beta^{(j)}\sim N(\mu_\beta,\Sigma_\beta)\tag{15.5}$$
Extensions are possible (group-varying data variance, structure in the mean, more levels). The key is the prior on $\Sigma_\beta$. $\sigma_y$ and $\mu_\beta$ can typically be estimated well from the data, so their priors matter less (p. 390).

**Inverse-Wishart.** With $K$ coefficients, $\beta$ is $J\times K$ and $\Sigma_\beta$ is $K\times K$. The conditionally conjugate prior for $\Sigma_\beta$ in (15.5) is the inverse-Wishart (Section 3.6) (p. 390).

**Scaled inverse-Wishart.** The Inv-Wishart$_{K+1}(I)$ model strongly constrains the variances (the diagonal). The aim is a model noninformative on correlations but allowing wider uncertainty on variances. Use a redundant parameterization:
$$y_{ij}\sim N\big(X_j(\mu_\beta+\xi\otimes\eta^{(j)}),\sigma_y^2\big),\qquad \eta^{(j)}\sim N(0,\Sigma_\eta)\tag{15.6}$$
$\xi$ has length $K$; $\otimes$ is component-wise multiplication; $\beta^{(j)}=\mu_\beta+\xi\otimes\eta^{(j)}$; $\Sigma_\beta=\operatorname{Diag}(\xi)\Sigma_\eta\operatorname{Diag}(\xi)$ (p. 390). Separate priors on $\xi$ and $\Sigma_\eta$ give a richer uncertainty structure. This is the scaled inverse-Wishart of Section 3.6. A noninformative choice: $\Sigma_\eta\sim$ Inv-Wishart$_{K+1}(I)$ with independent uniform priors on the $\xi$'s. Informative priors on $\xi$ can be added if necessary (p. 391).

**Example: business-school grade prediction** (p. 391–392).
- Schools use regressions of first-year GPA on GMAT-V, GMAT-Q and UGPA. A study of 59 business schools over two years (about 8500 students, about 4% black) raised a concern about biased predictions for subgroups. Separate regressions per school (constant, GMAT-V, GMAT-Q, UGPA) found that the regressions tended to overpredict the first-year grades of black students (p. 391).
- Adding a single indicator was considered too restrictive; it was desired to allow different regression models for the two groups. Each school's model then has eight explanatory variables: the four above plus the same four times the black-student indicator. Likelihood: $p(y\mid\beta,\sigma^2)\sim\prod_{j=1}^{59}\prod_{i=1}^{n_j}N(y_{ij}\mid X_{ij}\beta_j,\sigma_j^2)$. Geometrically this is two regression planes; all eight terms predict black students' scores and only the first four predict non-black students' (p. 391). Nine parameters per school: $\beta_{1j},\dots,\beta_{8j},\sigma_j$ (p. 391).
- Separate least squares per school is impossible: many schools have no black students or too few. A hierarchical model fits all $8\times59$ coefficients: the 59 vectors $\beta_j$ are independent draws from $N(\alpha,\Lambda_\beta)$ ($\alpha$ unknown 8-vector, $\Lambda_\beta$ an $8\times8$ matrix) (p. 391).
- Prior: uniform on $\alpha,\Lambda_\beta,\log\sigma_1..\log\sigma_{59}$. The authors call this not ideal (one would want to embed the $\sigma_j$ in a hierarchical model) but a reasonable start. A pooled regression on all data gave crude starting values. The posterior mode was found with EM, and the conclusions rest on this modal approximation (p. 392).
- Conclusions: the multivariate hierarchical model is a substantial improvement over the standard model, with relatively accurate predictions for both groups. With test scores fixed at the mean scores for black students, in about 85% of schools non-blacks were predicted to have higher first-year GPA. Over 60% of the differences were more than one posterior sd above zero, and about 20% were more than two. A nonhierarchical model could not reasonably estimate this comparison here, given so few black students per school (p. 392).

*Intuition note.* When a group has too little data to pin down its own slopes, its slopes borrow strength from the other groups through the shared $N(\alpha,\Lambda_\beta)$. The scaled version lets the variances be vague while keeping the correlation prior mild.

### 15.5 Computation: batching and transformation (p. 392–394)
The authors generally prefer HMC to simple Gibbs. Gibbs ideas still help in parameterizing the problem for HMC, and in splitting big models into pieces (p. 392). The discussion assumes independent variances per level (p. 392).

**Gibbs, one batch at a time.** Update each batch of coefficients given the others (an augmented linear regression, Section 14.8), then update the variances. In the election example the batch updates reduce to simple averages. For scalar variance parameters (one per batch plus data-level ones) the conditionals are scaled inverse-χ². For more complex models, use Metropolis jumps. Cycling through batches (including any noninformative or fixed-prior batch) mimics the natural way to combine levels: guess the upper-level parameters, run the lower-level regression, use the draws to improve the upper-level estimates, and so on (p. 392–393).

**All-at-once Gibbs.** Use the augmented regression (15.3). Alternate: variances from independent inverse-χ² given the data and coefficients; coefficients by a weighted regression whose weights depend on the current variances. Advantage: it works efficiently even when coefficients at different levels are correlated in the posterior (e.g. $\theta_j$ and $\mu$ in eight schools). Disadvantage: each step is a regression on a large augmented dataset. For elections $n=511,k=20$, but $n_*=511+55$, $k_*=20+55$. Regression time is proportional to $nk^2$, so steps are slow when parameters are many. In practice HMC would be used (p. 393).

**Parameter expansion.** All the algorithms above can converge slowly when a hierarchical variance is near zero. A near-zero variance draw shrinks the batch $\gamma_j$ toward the population mean. Those $\gamma_j$ then give a near-zero variance update, and so on. The sampler can eventually escape, but possibly after many iterations (p. 393). The fix (parameter-expanded Gibbs and EM, Sections 12.1, 13.4): attach a multiplicative factor to each batch, which breaks the dependence between the coefficients and their variance parameter (p. 393).

*Election example, expanded version of (15.2):*
$$y_{st}\sim N\big(X_{st}\beta+\zeta_1^{region}\gamma_{r(s)t}+\zeta^{year}\delta_t,\sigma^2\big)\ (r=1,2,3),\qquad \text{with }\zeta_2^{region}\text{ in place of }\zeta_1^{region}\ (r=4)$$
Priors as before. The $\zeta$'s get uniform priors and are not identified. The products $\zeta_1^{region}\gamma_{rt}$, $\zeta_2^{region}\gamma_{rt}$, $\zeta^{year}\delta_t$ correspond to the old $\gamma_{rt},\delta_t$. The products $|\zeta_1^{region}|\tau_{\gamma1}$, $|\zeta_2^{region}|\tau_{\gamma2}$, $|\zeta^{year}|\tau_\delta$ correspond to the old variance components (p. 393–394). The plain Gibbs sampler is already reasonably efficient here because the variances are estimated precisely. The example just illustrates the steps (p. 394).
- Update the coefficients $(\beta,\gamma,\delta)$ by any Gibbs scheme (batch, all at once, element-wise). Update the variances by independent inverse-χ². The $\zeta$'s do not change the fact that $\beta,\gamma,\delta$ are linear-regression parameters (p. 394).
- Update $\zeta$: regress the "data" $z_{st}=y_{st}-X_{st}\beta$ on the three "predictors" built from $\gamma$ (non-South), $\gamma$ (South) and $\delta_t$, with variance $\sigma^2I$ (p. 394).
- Monitor $\sigma$ and the original-parameterization quantities: multiply each $\gamma_{rt},\delta_t$ by its $\zeta$, and each $\tau$ by $|\zeta|$ (p. 394).

**Transformations for HMC.** HMC can be slow when parameters have very short or long tails, as variances or log variances can. A decoupling can help. For eight schools, $y_j\sim N(\theta_j,\sigma_j^2),\ \theta_j\sim N(\mu,\tau^2)$ with prior $p(\mu,\tau)$: EM or Gibbs can get stuck near $\tau=0$. In HMC the joint posterior of $\theta,\mu,\tau$ forms a "whirlpool": no single step size suits the whole distribution, and trajectories rarely enter or leave the region near $\tau=0$. A better parameterization:
$$y_j\sim N(\mu+\tau\eta_j,\sigma_j^2),\qquad \eta_j\sim N(0,1),\qquad \theta_j=\mu+\tau\eta_j$$
(p. 394).

*Intuition note.* Near $\tau=0$ the group offsets shrink towards nothing, which is where the "whirlpool" (p. 394) forms (our gloss). Writing the offset as $\tau$ times a standard normal makes the sampled quantity $\eta_j$ independent of the scale $\tau$.

### 15.6 Analysis of variance and the batching of coefficients (p. 395–398)
The largest gains in estimating regression coefficients often come from specifying structure. In the election model it is crucial that national and regional indicators are clustered and modeled separately from the quantitative predictors. Predictors should be set up so they can be structured hierarchically (p. 395). Anova here is the grouping of coefficients into batches (each row of an Anova table is a source of variation). We care about individual coefficients and also the variance of each batch. Anova is "a way of making sense of hierarchical regression models" with exchangeable batches (p. 395).

**Notation.** Rows $m=1..M$; batch $m$ has $J_m$ coefficients $\beta^{(m)}_j$, subvector $\beta^{(m)}$, classical least-squares estimate $\hat\beta^{(m)}$. There are $c_m$ linear constraints: $C^{(m)}$ is $c_m\times J_m$ of rank $c_m$, $C^{(m)}\hat\beta^{(m)}=0$, and $(df)_m=J_m-c_m$. The grand mean is $\beta^{(0)}_1$ (row 0, no constraints) (p. 395).
$$y_i=\sum_{m=0}^{M}\beta^{(m)}_{j_i^m}\tag{15.7}$$
$j_i^m$ picks the coefficient in batch $m$ for data point $i$, so each data point pulls one coefficient from each row. The last row corresponds to residuals. With a general design matrix (regression or GLM):
$$y_i=\sum_{m=0}^{M}\sum_{j=1}^{J_m}x^{(m)}_{ij}\beta^{(m)}_j\tag{15.8}$$
(p. 395).

**Hierarchical formulation.** $\beta^{(m)}_j\sim N(0,\sigma_m^2)$ for $j=1..J_m$. Centering at 0 loses no generality (if the mean were elsewhere, include the mean of the $x^{(m)}_j$ as a separate predictor). As in classical Anova, interactions are usually included only if the main effects are (p. 396). Conjugate prior: $\sigma_m^2\sim\text{Inv-}\chi^2(\nu_m,\sigma_{0m}^2)$. A natural noninformative prior is uniform on $\sigma_m$, which corresponds to $\nu_m=-1,\sigma_{0m}=0$. If $J_m$ is large, $\sigma_m$ is essentially estimated from data. If $J_m$ is small, the flat prior allows large $\sigma$, which minimizes shrinkage (p. 396).

**Computation.** Gibbs: update $\beta$ given $\sigma$ by linear regression; update $\sigma$ from independent inverse-χ² conditionals. It can stick near $\sigma_m\approx0$, so use parameter expansion (p. 396):
$$\beta^{(m)}_j=\zeta_m\gamma^{(m)}_j,\qquad \sigma_m=|\zeta_m|\tau_m\tag{15.9}$$
Model: $y=X\zeta\gamma$, $\gamma^{(m)}_j\sim N(0,\tau_m^2)$, $\tau_m^2\sim\text{Inv-}\chi^2(\nu_m,\sigma_{0m}^2)$, uniform prior on $\zeta$ (so it reduces to the original model). The sampler updates $\gamma$ (regression with $n$ data points and $\sum_m J_m$ predictors), $\zeta$ (regression with $n$ points and $M$ predictors) and $\tau$ (independent inverse-χ²). $\beta,\sigma$ are recomputed from (15.9) and stored (p. 396).

**Finite-population vs superpopulation sd.** The importance of source $m$ is measured by the sd of its constrained coefficients:
$$s_m=\sqrt{\frac{1}{(df)_m}\,\beta^{(m)T}\Big[I-C^{(m)T}\big(C^{(m)}C^{(m)T}\big)^{-1}C^{(m)}\Big]\beta^{(m)}}\tag{15.10}$$
Divide by $(df)_m=J_m-c_m$ because $C^{(m)}$ induces $c_m$ constraints. The underlying $\beta$ are modeled unconstrained (p. 396–397).
- The **superpopulation** sd $\sigma_m$ characterizes uncertainty in predicting a *new* coefficient from batch $m$. The **finite-population** sd $s_m$ describes variation among the existing $J_m$ coefficients (p. 397).
- Anova summaries focus on $s_m$. The $\sigma_m$ are useful computational intermediates. Procedure: draw joint posterior simulations of $(\beta,\sigma)$, then compute $s_m$ from $\beta$ by (15.10) (p. 397).
- *Extreme case:* $J_m=2$, $\beta_1+\beta_2=0$, lots of data in both groups. Then $\beta_1,\beta_2$ are estimated accurately, and so is $s_m^2=\tfrac12(\beta_1^{(m)}-\beta_2^{(m)})^2$. But $\sigma_m^2$ is estimated from something proportional to a χ² with 1 degree of freedom. We know much about these two parameters and little about others from their batch (p. 397).
- **Fixed vs random.** Which of $s_m$, $\sigma_m$ matters depends on context. The 50 U.S. states suggest the finite population; subject-level effects in a psychology experiment suggest the superpopulation. Example: five treatments considered "fixed" (4 df) are then found to be part of a larger family and so "random". Inference on the five $\beta$'s, $s_m$ and $\sigma_m$ does not change. The superpopulation variance gains a new role in characterizing the distribution of treatment effects. So the difference is "not a difference in inference or computation but in the ways that these inferences will be used" (p. 397).

**Example: Web connect times** (p. 397–398). Messages were sent by an internet infrastructure provider every hour for 25 hours, from each of 45 locations to 4 destinations, through two companies, and the study was repeated a week later. The analysis is of log connect times with five factors: to, from, company, hour, week. It is a full factorial with no replication, so the five-way interaction is the "error". Fig. 15.4 shows each source's finite-population $s_m$ with 50% and 95% intervals. Read from the figure: the "to" source has 3 df, "from" 44, "company" 1, "hour" 24, "week" 1.
- The lowest-level variation is more important in variance than any factor except the main effect of destination. Company matters on its own, and in interaction with to, from, and in the three-way interaction (p. 397–398).
- Caption: on the log scale, $s_m=0.20$ corresponds to a coefficient of variation $\exp(0.2)-1\approx0.2$, so exponentiated coefficients vary multiplicatively by about 20% (p. 398).
- This is a default model for exploration, not the final analysis. It can guide more focused models or future data collection (p. 398).

*Intuition note.* Each Anova row is a batch of effects with its own spread. $s_m$ asks "how spread out are the effects we actually have?", while $\sigma_m$ asks "how spread out is the population they came from?". With few effects in a batch, the first is much better pinned down.

### 15.7 Hierarchical models for batches of variance components (p. 398–400)
Example: a $5\times5\times2$ split-plot latin square with five full-plot treatments (A–E), each plot split into two subplots. Nine sources/variance components (df): row 4, column 4, (A,B,C,D,E) 4, plot 12; (1,2) 1, row×(1,2) 4, column×(1,2) 4, (A–E)×(1,2) 4, plot×(1,2) 12 (p. 398–399).
- A simple noninformative analysis uses $p(\sigma_1..\sigma_9)\propto1$. A hierarchical alternative gives the $\sigma$'s a common half-Cauchy prior with peak 0 and scale $A$, with a uniform prior on $A$. This lets most variance parameters be small but occasionally one large, which seems reasonable in typical Anova settings where most sources are small and some large (p. 399).
- **Superpopulation fits (Fig. 15.5).** Under uniform priors, extremely high values of the $\sigma_k$ are not ruled out: degrees of freedom are low and the interlocking of linear parameters makes any single variance hard to estimate. The half-Cauchy model shrinks heavily, especially the high ends of intervals. For most parameters the posterior medians are similar under both models; the 75th and 97.5th percentiles are shrunk. This is an ideal setting for hierarchical modeling of variance parameters, since it combines separately imprecise estimates (p. 399).
- **Finite-population fits (Fig. 15.6).** The $\sigma_k$ are superpopulation parameters: each is the sd of a whole population of groups, of which only a few were sampled. With few df it can help to look at the finite-population $s_\alpha$. For the simple form (5.21), $s_\alpha$ is the sd of the $J$ values $\alpha_j$. More generally, $s_\alpha$ is the root mean square of the coefficients' residuals after projection to their constraint space. It is calculated from posterior simulations and, especially with low df, is more precisely estimated than $\sigma$ (p. 400).
- The half-Cauchy prior does slightly better than the uniform for $s_\alpha$, with the largest shrinkage for the one-df component. The scale $A$ was estimated at 1.8 with 95% posterior interval [0.5, 5.1] (p. 400).

*Intuition note.* Nine variance estimates, each weak, are partly pooled just as group means are. The half-Cauchy hyperprior learns from the data how big "typical" sources are, and this reins in the implausibly large values that a flat prior leaves open.

### 15.8 Bibliographic note (p. 400–402)
Pointers given: Gelman & Hill (2007) for an elementary introduction; Lindley & Smith (1972) for the general normal linear form; Braun et al. (1983) as the source of the business-school example; Gelman & King (1993) and Boscardin & Gelman (1996) for the election model. Parameter-expanded Gibbs: Liu & Wu (1999), Gelman et al. (2008). The Anova perspective is from Gelman (2005). Further points stated: ridge regression is equivalent to an exchangeable normal prior on coefficients (p. 401). The Bayesian approach differs from non-Bayesian random-effects methods by averaging over uncertainty in the hierarchical parameters (p. 401). Footnote 1: posterior means from hierarchical models are biased as "estimates" but can be unbiased or approximately unbiased as "predictions", since frequency evaluations condition on unknown parameters but not on unknown predictive quantities (p. 401).

### 15.9 Exercises (p. 402–404)
Six exercise sets are listed; see "Exercises worth doing".

## Toy example (ours, not from the text)
Show a normal prior as extra data (15.3), and partial pooling. Simplify: two groups, $\alpha=0$ known (so no $\alpha$ columns, $K=0$), data variance $\sigma^2=1$.

Model: $y_j\sim N(\beta_j,1)$, $\beta_j\sim N(0,\tau^2)$, $j=1,2$, observed $y=(4,2)$.

Augmented regression: $y_*=(4,2,0,0)^T$ (a $4\times1$ vector), $X_*=\begin{pmatrix}I_2\\I_2\end{pmatrix}$ ($4\times2$), $\Sigma_*^{-1}=\operatorname{diag}(1,1,1/\tau^2,1/\tau^2)$. Posterior mean $=(X_*^T\Sigma_*^{-1}X_*)^{-1}X_*^T\Sigma_*^{-1}y_*$.

- $\tau^2=1$: $X_*^T\Sigma_*^{-1}X_*=(1+1)I=2I$ and $X_*^T\Sigma_*^{-1}y_*=(4\cdot1+0\cdot1,\ 2\cdot1+0\cdot1)=(4,2)$. Mean $=(4,2)/2=(2,1)$. Posterior variance of each $\beta_j$ is $1/2$.
- $\tau^2=1/3$: $\Sigma_*^{-1}=\operatorname{diag}(1,1,3,3)$, so $X_*^T\Sigma_*^{-1}X_*=(1+3)I=4I$ and the right side is again $(4,2)$. Mean $=(1,\ 0.5)$. Posterior variance $1/4$.
- $\tau^2\to\infty$: the prior rows have zero precision and drop out, so mean $=(4,2)=y$ (no pooling). $\tau^2\to0$: mean $=(0,0)$, all $\beta_j$ equal to $\alpha=0$.

So each estimate is a precision-weighted average of $y_j$ and the prior mean $0$. The smaller $\tau^2$, the stronger the shrinkage.

Intraclass check with $\sigma=1,\sigma_\beta=1$ (from p. 382): $\eta^2=1+1=2$, $\rho=1/(1+1)=0.5$.

## Concepts
- [[hierarchical-model]] — parameters for groups drawn from a population distribution learned from data; here, regression coefficients in batches (p. 382)
- [[partial-pooling]] — compromise between no pooling ($\sigma_\beta=\infty$) and complete pooling ($\sigma_\beta=0$) (p. 381–382, 388)
- [[exchangeability]] — here: exchangeability among units is obtained by conditioning on group indicators; coefficients within a batch are exchangeable (p. 383)
- [[varying-coefficients-batch]] (new) — a batch of regression coefficients with a common normal population distribution (random effects) (p. 382)
- [[intraclass-correlation]] (new) — within-batch correlation $\rho=\sigma_\beta^2/(\sigma^2+\sigma_\beta^2)$, equivalent for $\rho\ge0$ to varying intercepts (p. 382)
- [[mixed-effects-model]] (new) — some coefficients with improper priors ("fixed"), others exchangeable ("random") (p. 382–383)
- [[prior-as-extra-data]] (new) — population and hyperprior distributions written as extra rows of one augmented regression (15.3) (p. 389)
- [[posterior-predictive-check]] — used with the test quantity $T(y,\beta)$ on nationwide residuals (p. 386)
- [[posterior-predictive-distribution]] — forecasting requires simulating new varying coefficients from their population distribution (p. 387)
- [[scaled-inverse-wishart]] (new) — redundant parameterization $\Sigma_\beta=\operatorname{Diag}(\xi)\Sigma_\eta\operatorname{Diag}(\xi)$ for a covariance-matrix prior (p. 390)
- [[gibbs-sampling]] — batch-wise and all-at-once versions for hierarchical regressions (p. 392–393)
- [[parameter-expansion]] (new) — multiplicative auxiliary parameters that decouple coefficients from their variance, avoiding stickiness near $\sigma=0$ (p. 393, 396)
- [[hamiltonian-monte-carlo]] — preferred sampler here; parameterization $\theta_j=\mu+\tau\eta_j$ helps (p. 392, 394)
- [[convergence-diagnostics]] — $\hat R<1.1$ after 500 steps with ten sequences (p. 388)
- [[anova-as-batching]] (new) — Anova rows as batches of exchangeable coefficients, each with its own variance (p. 395)
- [[finite-vs-superpopulation-sd]] (new) — $s_m$ (existing coefficients, eq. 15.10) vs $\sigma_m$ (population they come from) (p. 396–397)
- [[half-cauchy-prior-for-variances]] (new) — common half-Cauchy prior with scale $A$ on the $\sigma_k$'s (p. 399)
- [[conjugate-prior]] — conjugacy of normal prior and regression likelihood allows the augmented-regression form (p. 389)

## Canonical instances
- [[election-forecasting-1992]] — nonhierarchical model fails a check, varying year and region × year effects fix it; 85% forecast (p. 383–388)
- [[eight-schools]] — hierarchical regression with $X=I_J$; used to explain special cases and HMC reparameterization (p. 381, 394)
- [[business-school-grade-prediction]] — varying intercepts and slopes for 59 schools with a sparse subgroup (p. 391–392)
- [[web-connect-times-anova]] — five-way factorial Bayesian Anova display (p. 397–398)
- [[split-plot-latin-square]] — half-Cauchy hierarchical prior on nine variance components (p. 398–400)
- [[marquardt-snee-chemical-data]] — dataset for an exercise on many regression coefficients (p. 403)

## Bridges (candidates)
- [same-math] Exchangeable normal prior on regression coefficients ↔ ridge regression (stated on p. 401) — same quadratic penalty on coefficients.
- [same-math] Normal prior as extra "observation" rows ↔ weighted least squares on stacked data — (15.3) is literally one weighted regression.
- [structural-analogy] Finite-population vs superpopulation sd ↔ causal inference (sample vs population estimand) — whether you care about the units at hand or the population they represent.
- [structural-analogy] Partial pooling ↔ shrinkage in group-level estimates: noisier groups are pulled more toward the mean (same logic as in Ch. 5).
- [metaphor] HMC "whirlpool" near $\tau=0$ ↔ funnel geometry: trajectories cannot easily enter or leave a narrow region.

## Questions this raises
- How should the hyperprior on a variance be chosen when there are very few groups, and how sensitive are conclusions to it?
- What changes when the likelihood is not normal (generalized linear models, as in Exercise 6)?
- When should year- or region-level effects be modeled as exchangeable rather than as depending on predictors such as time trends (p. 389)?
- How can a modal (EM) approximation, as in the business-school analysis, misstate uncertainty compared with full posterior simulation?

## Exercises worth doing
- Ex. 1 (p. 402) — express eight schools as a hierarchical linear model with eight observations and known variances, and simulate — difficulty: easy
- Ex. 2(c) (p. 402) — set up varying coefficients for blocks and treatments; explain why their means are fixed at zero — difficulty: medium
- Ex. 3 (p. 402–403) — compare an ordinary regression with a mixed-effects model with a shared prior on nine coefficients, using the data of Table 15.2; interpret the differences via the hierarchical variance — difficulty: medium
- Ex. 4 (p. 403) — build an Anova plot for the educational testing example and discuss finite-population vs superpopulation sd — difficulty: medium
- Ex. 5(a),(c) (p. 403) — show the determinant of a correlation matrix is quadratic in any element; show equicorrelation $R$ is positive definite iff $-1/(d-1)<r<1$ — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 10 (pdf 391 = printed 381). All citations use printed numbers.
- The text layer renders $\theta$ as "ω" and "∼" as "→" in many places. The images show $\theta$ and $\sim$. I followed the images.
- Count inconsistencies as printed (not resolved here): p. 387 says the first 14 elements of $\beta$ cover the constant and Table 15.1 predictors, but the same page (p. 387) also speaks of a $50\times20$ matrix of predictors, and p. 389 and p. 393 say 20 predictors ($n_*=511+55$, $k_*=20+55$). Table 15.1 lists 19 variables, 5 of them year-specific regional ones. p. 389 says "75 components" but also "70 predictors" in the equivalent regression.
- p. 383 points to Anova "in Section 15.7", but Anova is developed in 15.6. p. 394 promises more on parameter-expanded Gibbs "at the end of Section 15.7", but 15.7 on these pages has none; the Anova version is in 15.6.
- The 1992 state-by-state forecasts are in Fig. 6.1, which is not in this unit. The 15.8 note cites "Pinheiro and Bates" without a year, as printed. A typo "forecasating" appears on p. 401.
- Exercise sets 2 and 6 refer to material from other chapters (Exercise 8.5, Exercise 11.7, Section 8.3), not available here. Table 15.2 (p. 403) is data for Exercise 3 and is not reproduced.
