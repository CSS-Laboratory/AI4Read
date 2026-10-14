---
id: gelman-2013-bda3/ch14-introduction
work: gelman-2013-bda3
unit: "Chapter 14 — Introduction to regression models"
pages: 353–380
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Introduction to regression models (BDA3, Chapter 14)

## L0 — One line
Classical normal linear regression can be thought of as Bayesian posterior inference under a noninformative prior; simulation from that posterior gives predictions and model checks, and the same machinery extends to unequal variances and to prior information.

## L1 — The gist (≤ 120 words)
The chapter asks how to set up and use Bayesian normal linear models. With a uniform prior on (β, log σ), the posterior has closed forms (normal for β given σ, scaled inverse-χ² for σ²) matching classical estimates. Simulation then yields posterior predictive draws and checks, shown with an incumbency-advantage study of US House elections. The chapter also covers goals of regression (prediction vs causal inference), choosing predictors, regularization (lasso), unequal variances and correlated errors, and prior information coded as extra "data points". It matters because the later hierarchical models (Chapter 15) reuse these computations.

**Prerequisites:** matrix algebra (inverse, Cholesky, QR); multivariate normal; conditional expectation and variance; scaled inverse-χ² distribution (Ch. 3); posterior predictive checks (Ch. 6); ignorability (Ch. 8).

## L2 — Key ideas (5–10 bullets)
- A regression model analyzes p(y|X,θ) alone. This loses no information if the prior on the X-parameters ψ is independent of the prior on θ (p. 354).
- With the prior p(β,σ²) ∝ σ⁻², the posterior is β|σ,y ∼ N(β̂, V_βσ²) and σ²|y ∼ Inv-χ²(n−k, s²). It is proper if n>k and rank(X)=k (pp. 355–356).
- To predict, draw (β,σ) from the posterior, then ỹ from N(X̃β, σ²I). This includes both model noise and parameter uncertainty (p. 357).
- Posterior predictive checks of any summary statistic are easy by simulation. In the incumbency example, the outlier counts are far above model predictions, yet the main estimate is little affected (pp. 362–363).
- For causal estimation, condition on enough control variables to make assignment ignorable. Do not control for post-treatment variables such as campaign spending (pp. 360, 365).
- With collinear columns of X, coefficients cannot be uniquely estimated from the data alone (more data or prior information is needed). Regularization priors, such as the lasso's double-exponential prior, stabilize estimates (pp. 365–369).
- When the variance matrix Σ_y is known (or known up to a scalar factor), unequal variances or correlated errors reduce to ordinary regression after transforming y and X by Σ_y^{-1/2} (pp. 370–373).
- A normal prior on β can be coded as extra data rows in a weighted regression; a scaled inverse-χ² prior on σ² acts like n₀ extra data points with variance σ₀² (pp. 376–377).

## L3 — Walkthrough

### Introduction (p. 353)
The chapter treats normal linear models with uniform priors. Hierarchical versions come in Chapter 15, and the Chapter 5 education example is a special case (p. 353). The aim is to show how to set up Bayesian models and draw samples for parameters θ and future observables ỹ, building on least-squares computations (p. 353).

### 14.1 Conditional modeling (pp. 353–354)
- **Notation.** Outcome y is continuous. Explanatory variables x=(x₁…x_k) may be discrete or continuous. A "treatment variable" is one x_j of primary interest; the other components are "control variables". Units are indexed by i, components of x by j. y is the n-vector of outcomes and X the n×k predictor matrix (p. 353).
- **Model.** The normal linear model has $E(y_i|\beta,X)=\beta_1x_{i1}+\dots+\beta_kx_{ik}$, often with $x_{i1}=1$ (pp. 353–354).
- **Ordinary linear regression** (Sections 14.2–14.5) adds equal variances, $\mathrm{var}(y_i|\theta,X)=\sigma^2$, and conditional independence. Then θ=(β₁…β_k, σ) (p. 354).
- **Key issues.** (1) Define and transform variables so the conditional mean is roughly linear with approximately normal errors. (2) Choose a prior that is strong enough for estimation but does not dominate the data (p. 354).
- **Justification of conditioning on X.** A full model has p(X|ψ), a joint likelihood p(X,y|ψ,θ) and a prior p(ψ,θ). A "regression model" ignores what X says about (ψ,θ). If $p(\psi,\theta)=p(\psi)p(\theta)$, the posterior factors as $p(\psi,\theta|X,y)=p(\psi|X)\,p(\theta|X,y)$. We can then analyze $p(\theta|X,y)\propto p(\theta)p(y|X,\theta)$ with no loss of information (p. 354). For a designed experiment, p(X) is known and there is no ψ (p. 354). The practical gain: it is easier to specify y given k variables than a joint distribution of k+1 variables (p. 354).

*Intuition note:* If what we believe about how X is generated is unrelated to what we believe about how y depends on X, the X-part of the posterior never touches θ. So we can drop it.

### 14.2 Bayesian analysis of classical regression (pp. 354–358)
Classical regression can be seen as Bayesian inference under a noninformative prior. Posterior means and standard errors then coincide with classical results, but simulation still helps with prediction and checking (p. 355).

**Model.**
$$y|\beta,\sigma,X\sim \mathrm{N}(X\beta,\sigma^2 I)\tag{14.1}$$
Here I is the n×n identity (p. 355).

**Prior.** Uniform on (β, log σ), equivalently
$$p(\beta,\sigma^2|X)\propto\sigma^{-2}\tag{14.2}$$
It is useful with many data points and few parameters. For small samples or many parameters, priors and hierarchical models matter more (p. 355).

**Posterior.** Factor $p(\beta,\sigma^2|y)=p(\beta|\sigma^2,y)\,p(\sigma^2|y)$, suppressing X (p. 355).

- Given σ, the posterior is an exponential of a quadratic in β, hence normal (derived by completing the square, Exercise 14.3):
$$\beta|\sigma,y\sim \mathrm{N}(\hat\beta,V_\beta\sigma^2)\tag{14.3}$$
$$\hat\beta=(X^TX)^{-1}X^Ty\tag{14.4}$$
$$V_\beta=(X^TX)^{-1}\tag{14.5}$$
(p. 355). Shapes: $\hat\beta$ is k×1, $V_\beta$ is k×k.
- The marginal of σ² is obtained as $p(\sigma^2|y)=p(\beta,\sigma^2|y)/p(\beta|\sigma^2,y)$ and has scaled inverse-χ² form (Exercise 14.4):
$$\sigma^2|y\sim\text{Inv-}\chi^2(n-k,s^2)\tag{14.6}$$
$$s^2=\frac1{n-k}(y-X\hat\beta)^T(y-X\hat\beta)\tag{14.7}$$
(pp. 355–356).
- Averaging over σ, β|y is multivariate t with n−k degrees of freedom. In practice we simulate σ, then β|σ (p. 356).
- **Comparison with classical results.** The classical estimates are β̂ and s. The classical standard error is obtained by setting σ=s in (14.3) (p. 356).
- **Properness.** Because the prior is improper, check that the posterior has a finite integral. $p(\beta,\sigma^2|y)$ is proper as long as (1) n>k and (2) rank(X)=k (Exercise 14.6). That means at least as many data points as parameters and linearly independent columns (p. 356).

*Intuition note:* With flat priors, the Bayesian answer is the least-squares fit. The only extra ingredient is honest uncertainty: σ² is scaled inverse-χ² around s², and β is normal around β̂ with spread proportional to σ.

**Sampling** (p. 356). Compute β̂ and V_β, then s²; draw σ² from (14.6), then β from (14.3). For efficiency:
1. QR factorization X=QR, with Q n×k with orthonormal columns and R k×k upper triangular.
2. Compute R⁻¹ (easy since R is upper triangular). It is a Cholesky factor of V_β, since $R^{-1}(R^{-1})^T=(X^TX)^{-1}=V_\beta$.
3. Solve $R\hat\beta=Q^Ty$ for β̂.

The random β draw uses R⁻¹ and independent standard normals. For very large problems (thousands of points, hundreds of predictors), conjugate gradient, stepwise ascent or iterative simulation can be better than QR (p. 356).

**Posterior predictive distribution** for new data with observed X̃ (p. 357).
- Two sources of uncertainty: (1) the variance σ² not accounted for by Xβ; (2) posterior uncertainty in (β,σ) from finite n. As n→∞, the second goes to zero but the first remains (p. 357).
- *Simulation:* draw (β,σ) from the joint posterior, then $\tilde y\sim\mathrm{N}(\tilde X\beta,\sigma^2I)$ (p. 357).
- *Analytic form.* Given σ, ỹ is normal (Exercise 14.7). Its mean, using (2.7), is
$$E(\tilde y|\sigma,y)=E\big(E(\tilde y|\beta,\sigma,y)\,\big|\,\sigma,y\big)=E(\tilde X\beta|\sigma,y)=\tilde X\hat\beta .$$
Its variance, using (2.8), is
$$\mathrm{var}(\tilde y|\sigma,y)=E[\mathrm{var}(\tilde y|\beta,\sigma,y)|\sigma,y]+\mathrm{var}[E(\tilde y|\beta,\sigma,y)|\sigma,y]\tag{14.8}$$
$$=E[\sigma^2I|\sigma,y]+\mathrm{var}[\tilde X\beta|\sigma,y]=(I+\tilde XV_\beta\tilde X^T)\sigma^2.\tag{14.9}$$
The first term, σ²I, is sampling variation. The second, X̃V_βX̃ᵀσ², is uncertainty about β (p. 357).
- Averaging over σ² using (14.6) gives a multivariate t for p(ỹ|y): center X̃β̂, squared scale matrix $s^2(I+\tilde XV_\beta\tilde X^T)$, and n−k degrees of freedom (p. 357).
- If X̃ is not completely observed, the explanatory variables must themselves be modeled. This is deferred to Chapter 18 (p. 357).

*Intuition note:* A prediction is uncertain for two reasons. Individuals scatter around the line (σ²I), and we do not know exactly where the line is (X̃V_βX̃ᵀσ²). More data shrinks only the second.

**Model checking** (p. 358). Standard residual plots can be read as posterior predictive checks. Because the posterior predictive distribution of any summary can be simulated, there is no need to derive sampling distributions of test statistics. Example: the correlation between squared residuals and fitted values (p. 358).

### 14.3 Regression for causal inference: incumbency and voting (pp. 358–364)
**Setup** (p. 358). Question: how much is incumbency worth in US House elections, and how has it changed over the past century? A separate regression is run for each election year. The results serve as summary statistics that are examined informally over time (a hierarchical time-series model could do this formally). There are 435 single-member districts, with typically about 100–150 uncontested. Units are contested district elections. The outcome $y_i$ is the incumbent party's vote proportion. The treatment is $R_i=1$ if the incumbent runs and 0 otherwise (an "open seat"). Third-party votes and uncontested elections are excluded (p. 358).

**Estimand** (p. 359). This is an observational study; the target is the average incumbency effect. The theoretical advantage in district i is
$$\text{incumbency advantage}_i=y^I_{\text{complete}\,i}-y^O_{\text{complete}\,i}\tag{14.10}$$
- $y^I$ is the vote proportion for the incumbent legislator if he or she runs against major-party opposition. It is unobserved in open-seat elections.
- $y^O$ is the incumbent party's proportion if the incumbent does not run and the two major parties compete. It is unobserved if the incumbent runs.
- The aggregate advantage is the average over districts. The definition does not assume the two candidates are identical except for incumbency status (p. 359).
- Regression can estimate the average effect if we condition on enough controls to make assignment ignorable (Sections 8.4, 8.6) (p. 359).

**Controls** (pp. 359–360).
- Comparing incumbents and nonincumbents with only a constant and treatment would be flawed if incumbents run in "safe seats" (nonignorability) (p. 360).
- Partial solution: control for the incumbent party's previous-election vote. Figure 14.1 (1988 vs 1986) shows a strong, roughly linear relation (p. 360).
- A further control is $P_i=1$ if Democrats held the seat before the election and −1 if Republicans did, which allows for a nationwide partisan swing. A 5% swing toward Democrats adds 5% to y for Democratic-held districts and subtracts 5% for Republican-held ones (p. 360).
- More controls (earlier incumbency, results two elections back) would add little for predicting y and have essentially no influence on the treatment coefficient (p. 360).

**Implicit ignorability** (p. 360). The regression estimates the effect if, given the controls, the decision to run does not depend on other variables that affect the outcome. If incumbents who expected to lose declined to run, assignment would be nonignorable. In a separate analysis, the probability of running is approximately independent of the previous-election vote. If vulnerability mattered much, low-margin incumbents would run less. The authors therefore believe departures from ignorability are small and tentatively accept it, based on subject knowledge and additional analysis (p. 360).

**Transformations** (p. 361). A logit transform would seem advisable, but almost all vote proportions lie between 0.2 and 0.8, so the effect would be minor. The original scale is used (p. 361).

**Posterior inference** (pp. 361–362).
- Separate regressions are run for each twentieth-century election year, excluding years right after redistricting. Posterior intervals come analytically from t distributions (Figure 14.2).
- With 1000 simulation draws, the increase in average incumbency advantage from the 1950s to the 1980s has posterior mean 0.050 and central 95% interval [0.035, 0.065] (p. 361).
- More controls did not substantially change the treatment inference (p. 361).
- Table 14.1 (1988; uniform prior on (β, log σ)), posterior quantiles at 2.5% / 25% / median / 75% / 97.5%:

| Variable | 2.5% | 25% | median | 75% | 97.5% |
|---|---|---|---|---|---|
| Incumbency | 0.084 | 0.103 | 0.114 | 0.124 | 0.144 |
| Vote proportion in 1986 | 0.576 | 0.627 | 0.654 | 0.680 | 0.731 |
| Incumbent party | −0.014 | −0.009 | −0.007 | −0.004 | 0.001 |
| Constant term | 0.066 | 0.106 | 0.127 | 0.148 | 0.188 |
| σ (residual sd) | 0.061 | 0.064 | 0.066 | 0.068 | 0.071 |

(p. 362).

**Model checking** (pp. 362–364).
- *Outliers.* Standardized residuals $(y_i-X_i\hat\beta)/s$ should be approximately N(0,1) if the model is right. Figure 14.3 (1980s) shows some apparent outliers. Residual sd is about 0.07 and vote shares lie mostly in 0.2–0.8, so the 0–1 bound is essentially irrelevant (p. 362).
- *Posterior predictive check.* The test statistic is the proportion of elections with $|\text{residual}|>0.2$, roughly 3 estimated sds. It means "proportion of elections mispredicted by more than 20%" (p. 363). The simulation (p. 363):
  1. For l=1,…,1000, and for each election year: (i) draw (β,σ) from the posterior; (ii) draw $y^{rep}\sim\mathrm{N}(X\beta,\sigma^2I)$ with the year's X; (iii) regress $y^{rep}$ on X and save the residuals.
  2. Combine years to get the proportion of residuals above 0.2 in absolute value, separately for open seats and incumbents running. The 1000 values represent the posterior predictive distribution.
- Table 14.2:

| Category | Observed proportion | Predictive 2.5% | median | 97.5% |
|---|---|---|---|---|
| Open seats | 41/1596 = 0.0257 | 0.0013 | 0.0038 | 0.0069 |
| Incumbent running | 84/10303 = 0.0082 | 0.0028 | 0.0041 | 0.0054 |

The authors say the observed counts are "about ten times and twice" the expected values and cannot be explained by chance (p. 363).
- *Party switches.* Observed: 1498/11899 = 0.126. Predictive median 0.136, 95% interval [0.130, 0.143]. The model over-predicts switches by about one percentage point, a minor difference (p. 363).
- *Sensitivity.* The outliers do not strongly affect the average-advantage inference, so the authors ignore this failing. They would not use the model to predict extreme outcomes. Possible fix: unequal variances for incumbents and open seats, plus t errors, if there is good reason (pp. 363–364).

*Intuition note:* A model can fit the quantity of interest well and still misdescribe the tails. Posterior predictive checks let you design a test statistic with a clear meaning (here "mispredicted by 20%") and judge whether the failure matters for your question.

### 14.4 Goals of regression analysis (pp. 364–365)
At least three goals: (1) understand y given x; (2) predict y for new x; (3) causal inference, predicting how y changes if x is changed in a specified way (p. 364).

**Prediction** (pp. 364–365).
- Prediction assumes old and new observations are exchangeable given x. So x must contain all information that distinguishes the new unit (p. 364).
- Example: 100 second-graders with beginning-of-year score and a constant as x. Prediction for a 101st is most trustworthy if all 101 are randomly sampled from one population, less reliable if the new student comes from a different school (p. 364).
- Units need not be similar. More similarity lowers the variance, which is "an issue of precision, not validity" (p. 364).
- If units are not exchangeable, encode the difference in x. Replace the constant by two indicator columns $x_A$, $x_B$ for schools A and B. If all 100 students were in school A, the data give no evidence on the school B coefficient. The predictive distribution for a school B student then depends heavily on the prior. With a flat prior it is improper with infinite variance. A weak prior linking the schools would give a high-variance posterior (pp. 364–365).

**Causal inference** (p. 365).
- Treatment variables are manipulated or potentially manipulable. Controls (covariates; "confounding variables" in epidemiology) measure other characteristics (p. 365).
- **Do not control for post-treatment variables.** Campaign spending is useful for predicting vote shares. But much spending happens after the incumbent's decision to run. Controlling for total spending would estimate something different from the incumbency effect as defined. Controlling for "pre-decision" spending would be legitimate. If we control for one of the treatment's effects, the regression "will probably underestimate the true causal effect". To serve both goals, include spending and vote share as correlated outcomes (p. 365).

### 14.5 Assembling the matrix of explanatory variables (pp. 365–367)
- **Identifiability and collinearity.** From the data alone, β cannot be uniquely estimated if there are more parameters than data points, or if the columns of X are not linearly independent, however large n is. Nearly collinear data supply little information about some linear combinations of β (pp. 365–366).
  - Example: if all running incumbents had 70% previous vote and all open seats 60%, then previous vote = 0.6 + 0.1R_i, which is collinear with the constant and R (p. 366).
  - In a nearly collinear case (candidates with >65% always run, those with <65% never run), posterior variances are high and inferences are highly sensitive to linearity of E(y|x,θ) (p. 366).
- **Nonlinear relations.** Transform variables toward linearity. Transformations change the coefficient's interpretation to a change in transformed y per unit of transformed x. Including both x_j and x_j² allows an arbitrary quadratic. Nonparametric models are in Chapters 20–23, and generalized linear models for discrete y in Chapter 16 (p. 366).
- **Indicator variables.** For k categories, k−1 indicators are needed in addition to the constant. They can be put into hierarchical models (Chapter 15) (p. 366).
- **Categorical vs continuous.** Ordered categories can be coded numerically (grades A–D as 4–1; "trend analysis" in epidemiology). Continuous variables can be grouped to examine nonlinearity (p. 366).
- **Interactions.** If the response to x_i depends on the value of x_j, add a cross-product term $(x_i-\bar x_i)(x_j-\bar x_j)$ as a new column of X. It may be hard to interpret if both are continuous (p. 367).
- **Irrelevant variables.** Generally include only variables with some reasonable substantive link. Example: letters in the candidate's last name is set before the decision to run, so it does not harm causal inference. But if it predicts, find out why. It may proxy for ethnicity, which would be a better variable (p. 367).
- **Selecting variables.** Ideally include all covariates that might help predict y. The loss of precision from unimportant predictors is "a relatively small price". Classical regression with a noninformative prior needs k<n and leaves little information on the variance ("overfitting"). These problems matter much less with reasonable priors such as hierarchical ones (p. 367).

### 14.6 Regularization and dimension reduction (pp. 367–369)
- **Classical selection as a prior.** Leaving out a variable is equivalent to setting its coefficient to exactly zero. A classical estimate after stepwise or subset selection is equivalent to a posterior mode under a prior with nonzero probability on lower-dimensional hyperplanes of β-space ("room, floor, walls, edges, corners"). Selection depends heavily on the amount of data (pp. 367–368).
- **Continuous alternative.** Give each coefficient a prior peaked at zero with a long tail (for example a zero-centered t). This says each variable is probably unimportant but could be large if predictive (p. 368).
- **Scaling matters in Bayes.** Under least squares or a flat prior, linear transformations of predictors do not affect inferences. With a shared informative prior on coefficients they do matter, so predictors should first be put on a common scale (for example −1 to 1). A purely subjectivist would say such transformations are irrelevant because they map into the prior. In practice, convenience favors one common prior, or two or three classes of coefficients (essential / potentially important / doubtful) (p. 368).
- **Three choices in Bayesian regularization** (p. 368): (1) location and scale of the prior (more concentrated means more regularization); (2) its form: normal pulls estimates toward the prior mean by a constant proportion, double-exponential shifts them by a constant amount, and a long-tailed Cauchy regularizes more near the mean and less far from it; (3) how the posterior is summarized: the mode omits variation and can look more regularized than the full posterior.
- **Lasso.** It estimates coefficients by the posterior mode under a double-exponential prior centered at zero, $p(\beta)\propto\prod_j\exp(-\lambda|\beta_j|)$ (p. 368). With the normal regression likelihood, the posterior is partially pooled toward zero, with the amount set by hyperparameter λ. λ can come from external information or be estimated, for example by cross-validation (p. 369). The key is the sharp prior peak at zero combined with summarizing by the mode. Together these let coefficient estimates become exactly zero with many predictors, noisy data and small to moderate samples (p. 369).
- **Authors' view.** For the regressions they typically see, they do not believe any coefficients are truly zero and do not generally see a conceptual advantage in exact zeros. Still, regularized estimates can be much better than least squares with flat priors. "Regularization will always happen, one way or another" (p. 369). Lasso is clearly defined and algorithmic, and it uses data to decide which predictors to keep (p. 369). Possible improvements: allow uncertainty over which variables are selected; or do full Bayesian inference with the lasso prior (then there is no particular reason for the double-exponential over a t family); and allow different pooling for different coefficients (p. 369).

*Intuition note:* Least squares with many predictors can be noisy, and informative priors regularize the estimates. The prior's shape and how the posterior is summarized decide how: lasso's sharp peak at zero plus mode-summary allows exact zeros, while full Bayesian inference with the lasso prior only partially pools (p. 369).

### 14.7 Unequal variances and correlations (pp. 369–376)
**Diagnosing violations** (pp. 369–370). The assumptions of (14.1) (linear mean, normal errors, independent equal-variance errors) are not exactly true in practice. Check fit and compare competing models (p. 369).
- *Nonlinearity:* residual plots; add transformed or quadratic terms (medical improvement vs age) (p. 369).
- *Nonnormality:* structural (discrete y) or visible in residual plots. First try transformation, or a generalized linear model (Chapter 16) (p. 370).
- *Unequal variances:* plots of absolute residuals against predictors. Often the fix is more predictors (for example, omitted precipitation in a yield study). Sometimes variance is natural: hospital averages have variance roughly proportional to 1/(sample size); different technicians differ (p. 370).
- *Correlations:* check residual autocorrelation for time-ordered data. Ignoring correlation typically gives falsely precise posteriors, because n correlated units carry less information than n independent ones, and gives inaccurate predictions. Example: siblings' heights remain correlated after controlling for age and sex. Adding parents' heights lowers the correlation but in general leaves it positive. Nonzero correlations are always required if y values are related by mechanisms other than the observed covariates (p. 370).

**General model** (p. 370):
$$y\sim\mathrm{N}(X\beta,\Sigma_y)\tag{14.11}$$
with Σ_y a symmetric positive definite n×n matrix that must be specified or given an informative prior (p. 370).

**Known Σ_y** (p. 371). Take a flat prior on β. Let $\Sigma_y^{1/2}$ be a Cholesky factor of Σ_y. Multiplying by $\Sigma_y^{-1/2}$ gives
$$\Sigma_y^{-1/2}y|\theta,X\sim\mathrm{N}(\Sigma_y^{-1/2}X\beta,I).$$
Apply Section 14.2 with σ=1 to the transformed data, giving
$$\hat\beta=(X^T\Sigma_y^{-1}X)^{-1}X^T\Sigma_y^{-1}y\tag{14.12}$$
$$V_\beta=(X^T\Sigma_y^{-1}X)^{-1}\tag{14.13}$$
with posterior (14.3). Explicit inverses are not needed; use the Cholesky decomposition (p. 371).

*Prediction with correlation* (p. 371). One must specify the joint covariance of old and new data:
$$\begin{pmatrix}y\\\tilde y\end{pmatrix}\Big|X,\tilde X,\theta\sim\mathrm{N}\left(\begin{pmatrix}X\beta\\\tilde X\beta\end{pmatrix},\begin{pmatrix}\Sigma_y&\Sigma_{y,\tilde y}\\\Sigma_{\tilde y,y}&\Sigma_{\tilde y}\end{pmatrix}\right)$$
which must be symmetric positive semidefinite. Then
$$E(\tilde y|y,\beta,\Sigma_y)=\tilde X\beta+\Sigma_{\tilde y,y}\Sigma_y^{-1}(y-X\beta),\qquad \mathrm{var}(\tilde y|y,\beta,\Sigma_y)=\Sigma_{\tilde y}-\Sigma_{\tilde y,y}\Sigma_y^{-1}\Sigma_{y,\tilde y},$$
from multivariate normal properties ((3.13), (A.1)). Example: predicting a child whose brother is in the data uses the within-family correlation (p. 371).

**Unknown Σ_y** (pp. 371–372). Assume $p(\beta|\Sigma_y)\propto1$. Then
$$p(\Sigma_y|y)=\frac{p(\beta,\Sigma_y|y)}{p(\beta|\Sigma_y,y)}\propto\frac{p(\Sigma_y)\mathrm{N}(y|\beta,\Sigma_y)}{\mathrm{N}(\beta|\hat\beta,V_\beta)}\tag{14.14}$$
This holds for any β, so set β=β̂:
$$p(\Sigma_y|y)\propto p(\Sigma_y)|\Sigma_y|^{-1/2}|V_\beta|^{1/2}\exp\!\Big(-\tfrac12(y-X\hat\beta)^T\Sigma_y^{-1}(y-X\hat\beta)\Big)\tag{14.15}$$
(Added step: the factor $|\Sigma_y|^{-1/2}$ comes from the likelihood at β̂, and $|V_\beta|^{1/2}$ from dividing by the normal density of β evaluated at its own mean, up to constants.) Density (14.15) is easy to evaluate but hard to sample, since β̂ and $|V_\beta|$ depend on Σ_y. A prior on a general Σ_y is also difficult to set (p. 372).

**Σ_y known up to a scalar** (p. 372). Write $\Sigma_y=Q_y\sigma^2$ with Q_y known and prior $p(\beta,\sigma^2)\propto\sigma^{-2}$. Replace y by $Q_y^{-1/2}y$ and X by $Q_y^{-1/2}X$:
$$\hat\beta=(X^TQ_y^{-1}X)^{-1}X^TQ_y^{-1}y\tag{14.17}$$
$$V_\beta=(X^TQ_y^{-1}X)^{-1}\tag{14.18}$$
$$s^2=\frac1{n-k}(y-X\hat\beta)^TQ_y^{-1}(y-X\hat\beta)\tag{14.19}$$
with (14.3) and (14.6) as before. Ordinary regression is the case Q_y=I (p. 372).

**Weighted linear regression** (p. 372). Diagonal Σ with $\Sigma_{ii}=\sigma^2/w_i$ and known weights $w_i$. Then $Q_y^{-1}=\mathrm{diag}(w_1,\dots,w_n)$. The weight w acts like an X variable that affects variance but not the mean (p. 372).

**Parametric unequal variances** (pp. 372–373).
$$\Sigma_{ii}=\sigma^2v(w_i,\phi)\tag{14.20}$$
for example $v(w_i,\phi)=w_i^{-\phi}$, which moves continuously from equal variances (φ=0) to variances ∝ 1/w_i (φ=1). Another form with this feature is $(1-\phi)+\phi/w_i$. A reasonable noninformative prior on φ is uniform on [0,1]. Rescale the weights so their product is 1, so inference for φ does not depend on weight scale (p. 373).
$$p(\beta,\sigma^2,\phi|y)\propto p(\phi)\,p(\beta,\sigma^2|\phi)\prod_{i=1}^n\mathrm{N}(y_i|X_i\beta,\sigma^2v(w_i,\phi))\tag{14.21}$$
With $p(\beta,\log\sigma|\phi)\propto1$: given φ, this is weighted regression with $Q_y=\mathrm{diag}(v(w_1,\phi),\dots,v(w_n,\phi))$. The marginal of φ is $p(\phi|y)=p(\beta,\sigma^2,\phi|y)/p(\beta,\sigma^2|\phi,y)$. Evaluating at $(\hat\beta,s^2)$ and using product of weights = 1,
$$p(\phi|y)\propto p(\phi)|V_\beta|^{1/2}s^{-(n-k)}\tag{14.22}$$
with β̂, V_β, s depending on φ via (14.17)–(14.19). It is not a standard distribution but can be evaluated on a grid of φ in [0,1]. Then draw in the order φ, σ², β (p. 373).

**Several unknown variance parameters** (pp. 373–374). With more than one unknown variance, there is no general direct method to sample the marginal posterior of the variances, so iterative simulation is used. Such models arise when groups of observations have different variances and in hierarchical regression (Section 15.1) (p. 373).

*Incumbency example, continued* (pp. 374–375). The authors give two opposing stories for why incumbent and open-seat elections might differ in variability, and try two variance parameters.
- *Notation.* I batches with $n_i$ points each and variances σ₁²…σ_I², so Σ_y is diagonal with $n_i$ copies of $\sigma_i^2$. In the example I=2 (p. 374).
- *Prior.* Treat the data as I separate experiments, giving $p(\beta,\Sigma_y)\propto\prod_i\sigma_i^{-2}$. The posterior of σ_i² is proper only if n_i ≥ 2. A batch with one observation needs an informative prior (p. 374).
- *Posterior.*
$$p(\beta,\sigma_1^2,\dots,\sigma_I^2|y)\propto\Big(\prod_{i=1}^I\sigma_i^{-n_i-2}\Big)\exp\!\Big(-\tfrac12(y-X\beta)^T\Sigma_y^{-1}(y-X\beta)\Big)\tag{14.23}$$
Given the variances, β|· is weighted regression. The variances have marginal density as in (14.15) with prior $\prod\sigma_i^{-2}$ (p. 374).
- *Findings.* Post-1940, residual sds are on average higher for open seats. An equal-variance model therefore distorts β somewhat (pp. 374–375). The authors used EM to find a marginal posterior mode of (σ₁², σ₂²) and the normal approximation as starting point for the Gibbs sampler. Three chains of length 100 gave $\hat R<1.1$ for all parameters (p. 375). The incumbency coefficients over time are virtually unchanged. The main difference is in the predictive distribution, which realistically models uncertainty in open-seat and incumbent elections since 1940 (p. 375). The σ₂ series is spiky, driven by few open seats per year. A hierarchical time-series model (not covered) would be better (p. 375).

**General form** (p. 376). $E(y|X,\theta)=X\beta$ and $\log\mathrm{var}(y|X,\theta)=W\phi$, with W a specified matrix governing variance and φ the variance parameters. Iterative methods including Metropolis can be used for (β, φ) (p. 376).

### 14.8 Including numerical prior information (pp. 376–378)
Conjugate prior information is added to the classical regression model; this is of interest in itself and, more importantly, because the same ideas return in Chapter 15 (p. 376).

- **One coefficient.** Prior $\beta_j\sim\mathrm{N}(\beta_{j0},\sigma^2_{\beta_j})$ with both known. As a function of β_j, the density $p(\beta_j)\propto\frac1{\sigma_{\beta_j}}\exp\!\big(-\frac{(\beta_j-\beta_{j0})^2}{2\sigma_{\beta_j}^2}\big)$ is the density of an "observation" $\beta_{j0}$ with mean β_j and variance $\sigma^2_{\beta_j}$. To include it: append $\beta_{j0}$ to y, a row of zeros with a 1 in column j to X, and $\sigma^2_{\beta_j}$ to the diagonal of Σ_y (zeros elsewhere in the new row and column). Then do weighted regression (p. 376).
  - As $\sigma^2_{\beta_j}\to\infty$ the added point has no effect. At $\sigma^2_{\beta_j}=0$ it fixes β_j at β_{j0} (p. 376).
- **Whole vector.** Prior $\beta\sim\mathrm{N}(\beta_0,\Sigma_\beta)$ is treated as k prior data points:
$$y_*=\begin{pmatrix}y\\\beta_0\end{pmatrix},\quad X_*=\begin{pmatrix}X\\I_k\end{pmatrix},\quad\Sigma_*=\begin{pmatrix}\Sigma_y&0\\0&\Sigma_\beta\end{pmatrix}\tag{14.24}$$
Components with infinite prior variance should be left out of the added points to avoid infinities. Alternatively work with $\Sigma_*^{-1}$ and its Cholesky factors. The prior on β is proper if all k components are proper, that is, if $\Sigma_\beta^{-1}$ has rank k (p. 377). Computation given Σ_* uses Section 14.7. The marginal posterior of Σ_* can be found analytically and sampled by the inverse-cdf method. Hierarchical versions use the Gibbs sampler (p. 377).
- **Variance parameters.** Prior information on σ² matters less than that on β (σ² is of less substantive interest). The conjugate prior is $\sigma^2\sim\text{Inv-}\chi^2(n_0,\sigma_0^2)$, equivalent to n₀ prior data points (n₀ need not be an integer) with sample variance σ₀². The posterior is
$$\sigma^2|y\sim\text{Inv-}\chi^2\!\Big(n_0+n,\ \frac{n_0\sigma_0^2+ns^2}{n_0+n}\Big)$$
in place of (14.6). With a prior on β, s² comes from the regression of y_* on X_* with Σ_*, and n becomes the length of y_*. For several variances, use independent conjugate priors, or possibly a hierarchical model (p. 377).
- **Inequality constraints** (such as β₁≥0 or β₂≤β₃≤β₄; for example, positive slope in the bioassay example, or monotone coefficients for ordinal indicators). The simple method is to simulate from the unconstrained posterior and discard draws that violate the constraints. This is reasonably efficient unless the constraints remove a large part of the posterior, in which case "the data are tending to contradict the model" (pp. 377–378).

*Intuition note:* A normal prior on a coefficient acts like one more observation of that coefficient, with weight set by the inverse prior variance. A scaled inverse-χ² prior acts like n₀ extra observations of variance. So priors can be handled by the same least-squares machinery.

### 14.9 Bibliographic note (p. 378)
Points to textbooks and Bayesian treatments of linear regression, the incumbency example (Gelman and King 1990a) and Rubin's causal framework. It also cites lasso (Tibshirani 1996), Bayesian lasso and horseshoe priors, and work on unequal variances and correlation models (p. 378).

### 14.10 Exercises (pp. 378–380)
Fourteen exercises. They cover radon regression, finite- vs superpopulation inference, derivations of (14.4)–(14.7) and (14.24), properness, lasso, straight-line fitting with errors in both x and y (dog metabolic data, Table 14.3), and heaped age data (pp. 378–380).

## Toy example (ours, not from the text)
Data: n=3, k=2 (constant and slope). $x=(0,1,2)$, $y=(1,2,4)$.

- $X=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix}$, $X^TX=\begin{pmatrix}3&3\\3&5\end{pmatrix}$, det $=15-9=6$.
- $V_\beta=(X^TX)^{-1}=\tfrac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}$. $X^Ty=(1+2+4,\ 0\cdot1+1\cdot2+2\cdot4)=(7,10)$.
- $\hat\beta=\tfrac16(5\cdot7-3\cdot10,\ -3\cdot7+3\cdot10)=\tfrac16(5,9)=(5/6,\ 3/2)$ (14.4).
- Fitted values: $5/6,\ 14/6,\ 23/6$. Residuals: $1/6,\ -2/6,\ 1/6$. Sum of squares $=(1+4+1)/36=1/6$. $s^2=(1/6)/(3-2)=1/6$ (14.7).
- Posterior: $\sigma^2|y\sim\text{Inv-}\chi^2(1,1/6)$; $\beta|\sigma,y\sim\mathrm N(\hat\beta,V_\beta\sigma^2)$. Given σ, slope sd $=\sigma\sqrt{3/6}\approx0.707\sigma$.
- Prediction at $\tilde x=3$, $\tilde X=(1,3)$: mean $\tilde X\hat\beta=5/6+9/2=16/3\approx5.33$. Compute $V_\beta\tilde X^T=\tfrac16(5-9,\ -3+9)=\tfrac16(-4,6)$. Then $\tilde XV_\beta\tilde X^T=\tfrac16(-4+18)=7/3$.
- Given σ: $\mathrm{var}(\tilde y|\sigma,y)=(1+7/3)\sigma^2=\tfrac{10}{3}\sigma^2$ (14.9). Of this, $\sigma^2$ is sampling noise and $\tfrac73\sigma^2$ is parameter uncertainty. Extrapolation to x=3 makes the second term large.
- Unconditional on σ: t with n−k=1 df, center 16/3, squared scale $s^2(1+7/3)=\tfrac16\cdot\tfrac{10}3=5/9$.

## Concepts
- [[normal-linear-model]] (new) — y given X is normal with mean linear in X; here with constant variance and independent errors (pp. 353–354)
- [[noninformative-prior-regression]] (new) — uniform prior on (β, log σ), i.e. $p(\beta,\sigma^2)\propto\sigma^{-2}$; gives classical estimates as posterior (p. 355)
- [[posterior-predictive-distribution]] — ỹ distribution averaging over posterior of (β,σ); adds parameter uncertainty to σ² (p. 357)
- [[posterior-predictive-check]] — compare a test statistic of observed data with its distribution under replicated data; here the proportion of outliers (p. 363)
- [[exchangeability]] — old and new units are exchangeable given x, so x must hold all distinguishing information (p. 364)
- [[assignment-mechanism-ignorability]] — treatment assignment independent of unobserved outcomes given controls; assumed tentatively for incumbency (p. 360)
- [[potential-outcomes]] — $y^I_{\text{complete}}$ and $y^O_{\text{complete}}$ define the incumbency advantage (p. 359)
- [[fundamental-problem-of-causal-inference]] — only one of $y^I$, $y^O$ is observed per district (p. 359)
- [[post-treatment-variable]] (new) — a variable affected by the treatment; should not be controlled for in causal regression (p. 365)
- [[collinearity-identifiability]] (new) — linearly dependent columns of X leave β not uniquely estimable from the data alone (p. 365)
- [[regularization]] — procedures giving more stable estimates; here informative priors (p. 368)
- [[lasso]] (new) — posterior mode under a double-exponential prior; can set coefficients exactly to zero (p. 368)
- [[weighted-linear-regression]] (new) — diagonal Σ_y with $\Sigma_{ii}=\sigma^2/w_i$; also the device for coding prior information (pp. 372, 376)
- [[conjugate-prior]] — normal prior on β and scaled inverse-χ² on σ² give the same families; coded as extra data (pp. 376–377)
- [[hierarchical-model]] — mentioned as the setting where these computations recur (Chapter 15) (p. 373)
- [[partial-pooling-shrinkage]] — lasso posterior is partially pooled toward zero (p. 369)
- [[gibbs-sampling]] — used for several unknown variances after EM and normal approximation (p. 375)
- [[convergence-diagnostics]] — $\hat R<1.1$ for all parameters in the two-variance fit (p. 375)

## Canonical instances
- [[incumbency-advantage-example]] — US House elections, separate regressions per year; effect, outlier check, two-variance model (pp. 358–364, 374–375)
- [[schoolchildren-prediction-example]] — second-grade reading scores; exchangeability and school indicators (p. 364)
- [[sibling-heights-example]] — sibling heights stay correlated after controlling for age and sex; adding parents' heights lowers the correlation but in general leaves it positive (pp. 370–371)
- [[campaign-spending-control]] — example of a post-treatment control that biases the causal estimate (p. 365)

## Bridges (candidates)
- [same-math] Ridge/least-squares-with-prior-as-extra-rows ↔ Bayesian conjugate updating: a normal prior on β is exactly extra rows $(I_k, \beta_0)$ in a weighted regression (14.24) — same algebra, different language.
- [same-math] Weighted regression with $\Sigma_{ii}=\sigma^2/w_i$ ↔ generalized least squares: $\Sigma_y^{-1/2}$ transformation gives (14.12)–(14.13).
- [structural-analogy] Lasso's exact zeros from prior peak plus mode summary ↔ sparsity-inducing penalties in machine learning: penalty = −log prior.
- [structural-analogy] Dropping post-treatment controls ↔ causal DAGs: conditioning on a mediator (ours; not stated in this unit). (canon link: fork, chain, collider)
- [metaphor] Regression ignoring the distribution of X ↔ treating covariates as fixed by design.

## Questions this raises
- How can t-family priors, which the authors suggest in place of exact zeros (p. 369), or the horseshoe priors cited in the bibliographic note, be set so that different coefficients are pooled differently?
- When the old and new units are not exchangeable, how weak can the linking prior in the school example be before predictions become useless?
- How should a hierarchical time-series model smooth the σ₂ series, and would it change the incumbency estimates themselves?
- How sensitive is the average-incumbency estimate to nonignorability of the decision to run, beyond the informal check against previous vote margin?

## Exercises worth doing
- Ex. 3 (p. 379) — derive β̂ and V_β by completing the square; the core of the chapter — difficulty: medium
- Ex. 4 (p. 379) — derive s² in (14.7) — difficulty: medium
- Ex. 6 (p. 379) — conditions for a proper posterior (n>k, rank k) — difficulty: medium
- Ex. 8 (p. 379) — algebraic proof that prior information is extra data (14.24) — difficulty: medium
- Ex. 9 (p. 379) — lasso posterior, one-dimensional mode, and why the multidimensional case is not coordinatewise shrinkage — difficulty: hard
- Ex. 13 (p. 380) — two correlated predictors (dogs data): effect of near-collinearity — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 363 = printed 353); printed numbers are visible and used throughout.
- The text layer garbles symbols: θ appears as "ω", ∼ as "→", and minus signs also as "→" (for example σ→2 for σ⁻²). I used the page images (θ, ∼) and wrote equations from them.
- Section 14.7 (p. 370) says models with more than one variance parameter are discussed "in Section 14.7"; this is a self-reference inside 14.7, as printed.
- The text on p. 363 says the observed outlier counts are "about ten times and twice" the model values; the Table 14.2 caption says only that both observed proportions are "far higher than expected". From the table medians, the ratios are about 7 (0.0257/0.0038) and 2 (0.0082/0.0041). Both rates lie outside the 95% predictive intervals either way.
- In 14.6 the sentence "it would be natural to first transforming each to…" (p. 368) contains a typo in the source; the meaning is clear.
- The bibliographic note and exercises are summarized briefly; Exercise 14's data file (reported_ages.png) is not in these pages.
