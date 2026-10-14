---
id: gelman-2013-bda3/ch07-evaluating
work: gelman-2013-bda3
unit: "7 Evaluating, comparing, and expanding models"
pages: 165-196
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
# Evaluating, comparing, and expanding models

## L0 — One line
Bayesian models can be compared by estimated out-of-sample predictive accuracy (the log predictive density, corrected for overfitting), the authors prefer to improve them by continuous expansion rather than discrete choice, and a model that fits well can still give bad answers when the data cannot speak to what matters.

## L1 — The gist (≤ 120 words)
How can we compare Bayesian models, and improve them, when all of them are wrong? The chapter estimates out-of-sample predictive accuracy from the log predictive density, corrected for overfitting by AIC, DIC, WAIC or cross-validation. It applies these to an election regression and the eight-schools model. It argues that Bayes factors can work well for truly discrete model sets but work poorly for inherently continuous problems. The authors prefer continuous model expansion. A final example, estimating a population total, shows that a well-fitting model can still give terrible inferences when the data cannot address the crucial tail behaviour. Then prior information, or a more robust question, is needed.

**Prerequisites:** posterior simulation draws; log-likelihood and posterior predictive distribution; normal linear regression; hierarchical model (eight schools, Ch. 5); posterior predictive checks (Ch. 6); expectation and variance.

## L2 — Key ideas (5–10 bullets)
- Predictive accuracy is scored with the log predictive density (the log probability that the fitted model gives to data). The prior is not part of this score, because the aim is to summarise fit to data (p. 167).
- The within-sample lppd (the log pointwise predictive density of the data used for fitting) is in general an overestimate of out-of-sample accuracy. Every method (the information criteria AIC, DIC, WAIC, and cross-validation) is an approximate bias correction, correct at best in expectation (pp. 169–170).
- The corrections use an "effective number of parameters": $k$, $p_{\rm DIC}$, $p_{\rm WAIC}$. The authors prefer WAIC to AIC and DIC, and in the end prefer cross-validation (pp. 172–174, 182).
- In the eight-schools example, complete pooling gets the best predictive score, yet the authors still prefer the hierarchical model because they do not believe $\tau=0$ (pp. 179–181).
- Predictive comparisons need judgement: some asymptotic theory suggests statistical noise is of order 1 in log score (not necessarily for nonnested models), practical size can be calibrated with simple models, and selecting among very many models biases the estimate (p. 181–182).
- Bayes factors work for truly discrete hypotheses with proper marginal densities (genetics). They work poorly for the continuous no-pooling vs complete-pooling problem, where they depend on arbitrary prior variance and on the number of schools (pp. 183–184).
- Model expansion embeds the old model in a larger continuous family. This needs priors $p(\theta|\phi)$ and a hyperprior $p(\phi)$, and sensitivity analysis (pp. 185–187).
- In the NY-municipalities example a better-fitting model (power family) gave worse inferences for the population total. Crucial tail behaviour needs prior information, or a more robust question such as the median (pp. 188–192).

## L3 — Walkthrough

### Introduction and running example (pp. 165–166)
The chapter is about comparing models and exploring improvements, not checking fit. Even if all models mismatch the data, comparing predictive accuracy can be informative. The main challenge is estimating predictive accuracy while correcting the bias of evaluating predictions on the data used to fit the model (p. 165).

**Running example: forecasting presidential elections.** Hibbs's 'bread and peace' model predicts the incumbent party's vote share $y$ from economic growth $x$ (p. 165). The model is
$$y\sim \mathrm{N}(a+bx,\sigma^2),\qquad p(a,b,\log\sigma)\propto 1,$$
with $n=15$ elections treated as a simple regression (p. 165). The posterior is normal-inverse-$\chi^2$, factored as $p(a,b,\sigma^2|y)=p(\sigma^2|y)\,p(a,b|\sigma^2,y)$ (p. 165):
$$\sigma^2|y\sim \text{Inv-}\chi^2(n-J,s^2),\quad s^2=\tfrac{1}{n-J}(y-X\hat\beta)^T(y-X\hat\beta),$$
$$\beta|\sigma^2,y\sim \mathrm N(\hat\beta,V_\beta\sigma^2),\quad \hat\beta=(X^TX)^{-1}X^Ty,\quad V_\beta=(X^TX)^{-1}.$$
Shapes: $X$ is $n\times J=15\times 2$ (a column of ones and the vector $x$); $\beta=(a,b)$ has length 2; $V_\beta$ is $2\times2$ (p. 166). For these data $s=3.6$, $\hat\beta=(45.9,3.2)$, $V_\beta=\begin{pmatrix}0.21&-0.07\\-0.07&0.04\end{pmatrix}$ (p. 166).

### 7.1 Measures of predictive accuracy (pp. 166–169)
- The best measure is tailored to the application (classification accuracy, monetary cost). Otherwise generic scores are used (p. 167).
- **Point prediction** (one reported value) is scored by *scoring functions*, e.g. mean squared error $\frac1n\sum_i (y_i-\mathrm E(y_i|\theta))^2$, or a version weighted by $1/\mathrm{var}(y_i|\theta)$. It is easy to compute and interpret, but less appropriate for models far from normal (p. 167).
- **Probabilistic prediction** (reporting the full uncertainty about $\tilde y$) is scored by *scoring rules*: quadratic, logarithmic, zero-one. Good rules are *proper* (they motivate honest reporting of beliefs) and *local* (bad predictions at some $\tilde y$ may be judged more harshly than at others). The logarithmic score is the unique (up to an affine transformation) local and proper rule (p. 167).
- The **log predictive density** $\log p(y|\theta)$ is the log score. It is proportional to mean squared error if the model is normal with constant variance (p. 167). It is linked to Kullback–Leibler information: in the large-sample limit, the model with the lowest KL information, and so the highest expected log predictive density, will have the highest posterior probability (p. 167). The chapter uses it throughout.
- **Why not the log posterior?** The prior matters for estimating parameters but not for assessing a model's accuracy against data. The authors do not say the prior is irrelevant to model fit in general: it affects inference about $\theta$, and in sparse data a poor prior gives poor predictions (p. 167).

**Single data point and averaging over future data (pp. 167–168).** Let $f$ be the true model, $y$ the observed data, $\tilde y$ future or alternative data. Write $p_{\rm post}$ and $\mathrm E_{\rm post}$ for anything averaged over $p(\theta|y)$. For a new point:
$$\log p_{\rm post}(\tilde y_i)=\log \mathrm E_{\rm post}\,p(\tilde y_i|\theta)=\log\int p(\tilde y_i|\theta)p_{\rm post}(\theta)d\theta .$$
The expected log predictive density for a new point averages this over $f$:
$$\mathrm{elpd}=\mathrm E_f(\log p_{\rm post}(\tilde y_i))=\int(\log p_{\rm post}(\tilde y_i))f(\tilde y_i)d\tilde y \tag{7.1}$$
For a whole new dataset, pointwise (needs an agreed split of $y$ into points $y_i$; the pointwise form links to cross-validation):
$$\mathrm{elppd}=\sum_{i=1}^n \mathrm E_f(\log p_{\rm post}(\tilde y_i)) \tag{7.2}$$
Given a point estimate $\hat\theta(y)$:
$$\mathrm E_f(\log p(\tilde y|\hat\theta)) \tag{7.3}$$
For independent data given parameters, joint and pointwise prediction coincide here, since $p(\tilde y|\hat\theta)=\prod_i p(\tilde y_i|\hat\theta)$ (p. 168). We do not know $f$. Plugging in an estimate of $f$ tends to give too good a fit (p. 168).

**Fitted model (pp. 168–169).** The log pointwise predictive density of the observed data is
$$\mathrm{lppd}=\log\prod_{i=1}^n p_{\rm post}(y_i)=\sum_{i=1}^n\log\int p(y_i|\theta)p_{\rm post}(\theta)d\theta, \tag{7.4}$$
computed from posterior draws $\theta^s$, $s=1,\dots,S$, as
$$\text{computed lppd}=\sum_{i=1}^n\log\Big(\frac1S\sum_{s=1}^S p(y_i|\theta^s)\Big). \tag{7.5}$$
The lppd of observed data overestimates the elppd for future data. So the plan is to start from (7.5) and apply a bias correction (p. 169).

**Choices in defining the likelihood (p. 169).** The line between prior and likelihood is somewhat arbitrary. It depends on what is replicated.
- In a hierarchical model with parameters $\alpha_j$ and hyperparameters $\phi$ one can replicate new data in existing groups. Then compute $p(y|\alpha_j^s)$ for each draw and average as in (7.5).
- Or one can replicate new data in a new group. Then sample $\alpha^s_{J+1}$ from $p(\alpha_{J+1}|\phi^s)$ and compute $p(y|\alpha^s_{J+1})$.
- Similar choices arise with mixture indicators, and with whether sample size $n$ is fixed by design.

The authors are not bothered by this nonuniqueness: different predictive distributions correspond to different uses of the inference (p. 169).

*Intuition note.* The score asks: how much probability did the fitted model give to data? The prior is left out because we judge how well the model, once fitted, describes data. What counts as "new data" is a modelling choice that depends on the use you have in mind.

### 7.2 Information criteria and cross-validation (pp. 169–178)
(A footnote says that instead of this section the authors recommend Vehtari, Gelman and Gabry (2017), p. 169.)

*Information criteria* are measures of predictive accuracy, historically defined from the **deviance** $-2\log p(y|\hat\theta)$ (p. 169). Out-of-sample prediction will typically be less accurate than within-sample accuracy implies. This holds even if the model family contains the true process and the parameters really were drawn from the prior (pp. 169–170).

The goal is mainly to put models on a common scale, not necessarily to pick the lowest-error model. The authors prefer continuous expansion to discrete choice or averaging (Section 7.5) (p. 170). If models have the same number of parameters estimated in the same way, best-fit log densities can be compared directly. Otherwise, adjust for the natural ability of larger models to fit better, even by chance (p. 170).

**Three ways to estimate out-of-sample accuracy (p. 170).** The authors know of no approximation that works in general.
- *Within-sample* lppd: quick, but generally an overestimate of (7.2).
- *Adjusted within-sample* (AIC, DIC, WAIC): start from something like lppd and subtract a correction for the (effective) number of parameters. Correct at best in expectation, not in any given case.
- *Cross-validation*: fit on training data, evaluate on a holdout. It avoids overfitting but remains tied to the data at hand. It is expensive: leave-one-out (LOO-CV) needs $n$ fits unless a shortcut exists.

**Asymptotics (pp. 170–171).** Under the conditions of Chapter 4, $\theta|y\to \mathrm N(\theta_0,V_0/n)$ as $n\to\infty$. The likelihood approaches the same normal because the prior contributes one factor and the likelihood $n$ (p. 171). In this limit, with $k=\dim\theta$ and $c(y)$ a constant not depending on $\theta$:
$$\log p(y|\theta)=c(y)-\tfrac12\big(k\log(2\pi)+\log|V_0/n|+(\theta-\theta_0)^T(V_0/n)^{-1}(\theta-\theta_0)\big).$$
So the posterior distribution of the log predictive density is a constant minus $\tfrac12\chi^2_k$. Its maximum is at the MLE and its posterior mean is $k/2$ lower. For actual posteriors this is only an approximation, useful as a benchmark. For singular models (mixtures, overparameterised models) the Fisher information matrix is not positive definite, plug-in estimates are not representative, and the deviance does not converge to $\chi^2$ (p. 171).

*Election example.* Using $S=10{,}000$ draws, the posterior distribution of $\log p(y|\theta)$ looks roughly like a scaled, shifted $\chi^2_3$ (Fig. 7.2). Its maximum (at the MLE) is $-40.3$ and its mean is $-42.0$. The difference, 1.7, is close to the asymptotic $3/2$ for 3 parameters (two coefficients and a variance) (pp. 171–172).

**AIC (p. 172).** AIC is based on a point estimate $\hat\theta$, typically the MLE. The target is $\mathrm E_f(\log p(\tilde y|\hat\theta(y)))$, (7.3). In the asymptotic normal limit (or for a normal linear model with known variance and uniform prior), subtracting $k$ corrects for the chance gain from fitting $k$ parameters:
$$\widehat{\mathrm{elpd}}_{\rm AIC}=\log p(y|\hat\theta_{\rm mle})-k, \tag{7.6}$$
and $\mathrm{AIC}=-2\log p(y|\hat\theta_{\rm mle})+2k$. Beyond linear models with flat priors one cannot simply add $k$. Informative priors and hierarchical structure reduce overfitting, and the effective number of parameters then depends strongly on the group-level variance (p. 172). For eight schools it is expected to lie between 1 and 8 (p. 172).

**DIC (pp. 172–173).** DIC replaces the MLE by the posterior mean $\hat\theta_{\rm Bayes}=\mathrm E(\theta|y)$ and $k$ by a data-based correction:
$$\widehat{\mathrm{elpd}}_{\rm DIC}=\log p(y|\hat\theta_{\rm Bayes})-p_{\rm DIC} \tag{7.7}$$
$$p_{\rm DIC}=2\big(\log p(y|\hat\theta_{\rm Bayes})-\mathrm E_{\rm post}(\log p(y|\theta))\big) \tag{7.8}$$
$$\text{computed }p_{\rm DIC}=2\Big(\log p(y|\hat\theta_{\rm Bayes})-\frac1S\sum_{s=1}^S\log p(y|\theta^s)\Big) \tag{7.9}$$
Negative $p_{\rm DIC}$ can arise if the posterior mean is far from the mode (p. 173). An alternative:
$$p_{\rm DIC\,alt}=2\,\mathrm{var}_{\rm post}(\log p(y|\theta)) \tag{7.10}$$
Both are correct in the limit of fixed model and large $n$ (derivable from the shifted, scaled $\chi^2$). For linear models with uniform priors both reduce to $k$. $p_{\rm DIC}$ is more numerically stable; $p_{\rm DIC\,alt}$ is always positive (p. 173). DIC itself is $-2\log p(y|\hat\theta_{\rm Bayes})+2p_{\rm DIC}$ (p. 173).

**WAIC (pp. 173–174).** WAIC starts from the computed lppd (7.5) and adds a pointwise correction; both versions can be viewed as approximations to cross-validation (derivations not shown) (p. 173).
$$p_{\rm WAIC1}=2\sum_{i=1}^n\big(\log(\mathrm E_{\rm post}p(y_i|\theta))-\mathrm E_{\rm post}(\log p(y_i|\theta))\big),$$
computed by replacing expectations with averages over the $S$ draws. The second version uses variances:
$$p_{\rm WAIC2}=\sum_{i=1}^n\mathrm{var}_{\rm post}(\log p(y_i|\theta)) \tag{7.11}$$
$$\text{computed }p_{\rm WAIC2}=\sum_{i=1}^n V_{s=1}^S\big(\log p(y_i|\theta^s)\big) \tag{7.12}$$
where $V_{s=1}^S a_s=\frac1{S-1}\sum_s(a_s-\bar a)^2$ is the sample variance (p. 173). It resembles (7.10) (without the factor 2) but is more stable, because variances are computed per data point and summed (p. 173). With either $p_{\rm WAIC}$:
$$\widehat{\mathrm{elppd}}_{\rm WAIC}=\mathrm{lppd}-p_{\rm WAIC} \tag{7.13}$$
The authors recommend $p_{\rm WAIC2}$ for practice. Its series expansion resembles that of LOO-CV, and in practice it seems to give results closer to LOO-CV. $\mathrm{WAIC}=-2\,\mathrm{lppd}+2p_{\rm WAIC2}$ (deviance scale). Watanabe's original definition is the negative average, divided by $n$, without the factor 2 (p. 174).

For a normal linear model with large $n$, known variance and uniform priors, both $p_{\rm WAIC}$ versions are approximately the number of parameters. More generally, a parameter counts about 1 if unconstrained, about 0 if all information is from the prior, and in between if both data and prior are informative (p. 174).

WAIC averages over the posterior instead of conditioning on a point estimate. It evaluates the predictions actually used in Bayesian practice. It works for singular models (hierarchical, mixture). Its cost: it needs a partition of the data into $n$ pieces, which is hard for time-series, spatial and network data. AIC and DIC derivations assume residuals independent given $\hat\theta$ (p. 174). The authors find WAIC more appealing than AIC and DIC (p. 174).

**Effective number of parameters is data-dependent (pp. 174–175).** Take $y_i\sim \mathrm N(\theta,1)$, $n$ large, $\theta\sim U(0,\infty)$. If the measurement $y$ is near zero, $p\approx\frac12$, because roughly half the information comes from the prior constraint. If $y$ is large and positive, $p\approx1$. So even for a fixed model and fixed true parameters, $p$ may depend on the data (pp. 174–175).

**BIC (p. 175).** $\mathrm{BIC}=-2\log p(y|\hat\theta)+k\log n$. For large datasets this penalises each parameter more than AIC does and favours simpler models. Its aim is to approximate the marginal density $p(y)$, not predictive fit. A complicated model can have low AIC, DIC and WAIC but high (poor) BIC. The authors do not consider BIC further (p. 175).

**Leave-one-out cross-validation (pp. 175–176).** Fit to $y_{\rm train}$, giving $p_{\rm train}(\theta)=p(\theta|y_{\rm train})$. Evaluate $\log p_{\rm train}(y_{\rm holdout})=\log\int p_{\rm pred}(y_{\rm holdout}|\theta)p_{\rm train}(\theta)d\theta$, estimated with draws $\theta^s$ as $\log(\frac1S\sum_s p(y_{\rm holdout}|\theta^s))$. For LOO-CV each holdout is one point, giving $n$ posteriors $p_{\mathrm{post}(-i)}$ with draws $\theta^{is}$:
$$\mathrm{lppd}_{\rm loo\text{-}cv}=\sum_{i=1}^n\log p_{\mathrm{post}(-i)}(y_i),\ \text{calculated as}\ \sum_i\log\Big(\frac1S\sum_s p(y_i|\theta^{is})\Big) \tag{7.14}$$
Each prediction uses $n-1$ points, which underestimates predictive fit. This is negligible for large $n$. For small $n$ or $k$-fold, use a first-order bias correction $b=\mathrm{lppd}-\overline{\mathrm{lppd}}_{-i}$, where $\overline{\mathrm{lppd}}_{-i}=\frac1n\sum_{i}\sum_j\log p_{\mathrm{post}(-i)}(y_j)$. The corrected value is $\mathrm{lppd}^{c}_{\rm loo\text{-}cv}=\mathrm{lppd}_{\rm loo\text{-}cv}+b$ (rarely used since $b$ is usually small) (pp. 175–176). The effective number of parameters from CV:
$$p_{\rm loo\text{-}cv}=\mathrm{lppd}-\mathrm{lppd}_{\rm loo\text{-}cv} \tag{7.15}$$
(with bias correction, $p^c_{\rm loo\text{-}cv}=\overline{\mathrm{lppd}}_{-i}-\mathrm{lppd}_{\rm loo}$) (p. 176).

Cross-validation, like WAIC, needs disjoint, ideally conditionally independent, pieces. It is expensive without shortcuts. LOO-CV can be approximated from the full-posterior draws with Pareto-smoothed importance sampling. Otherwise use $k$-fold CV (e.g. $k=10$). The chapter uses brute-force LOO for clarity (p. 176).

**Relations among methods (p. 176).** Under some conditions the criteria are asymptotically equal to LOO-CV (the bias correction is ignored in the proofs). AIC is asymptotically equal to LOO-CV computed with the MLE. DIC is a variant of regularised criteria that are asymptotically equal to LOO-CV with plug-in predictive densities. WAIC is asymptotically equal to Bayesian LOO-CV. For finite $n$ they differ, since LOO conditions on $n-1$ points. Further, LOO-CV assumes the prediction task $p(\tilde y_i|\tilde x_i,y_{-i},x_{-i})$, while WAIC estimates $p(\tilde y_i|y,x)$, so WAIC predicts only at already-observed $x$-locations (or subgroups). This can matter in flexible regressions or hierarchical models (p. 176). Cross-validation resembles the jackknife. The goal is an expectation over $y^{\rm rep}$ under the true $f$, so we study frequency properties of a Bayesian procedure (p. 176). AIC starts from the MLE, DIC from the posterior mean, WAIC from the posterior-averaged density; only WAIC is fully Bayesian, which is the authors' preference among bias-correction formulas. Cross-validation applies to any fit measure (pp. 176–177).

*Intuition note.* All these tools do the same job. They take the in-sample score, which is too optimistic, and subtract a penalty for how much the model could bend to the noise. The penalty is a "number of parameters" that shrinks when priors or hierarchies constrain the model.

**Worked example: election model (pp. 177–178).**
- *AIC.* MLE $(\hat a,\hat b,\hat\sigma)=(45.9,3.2,3.6)$, 3 parameters: $\widehat{\mathrm{elpd}}_{\rm AIC}=\sum_{i=1}^{15}\log \mathrm N(y_i|45.9+3.2x_i,3.6^2)-3=-43.3$; $\mathrm{AIC}=86.6$.
- *DIC.* $\mathrm E_{\rm post}\log p(y|\theta)=-42.0$ (invariant to reparameterisation). The first term is not invariant. Posterior means: $a,b$ as the MLE; $\mathrm E(\sigma|y)=4.1$, $\mathrm E(\sigma^2|y)=17.2$, $\mathrm E(\log\sigma|y)=1.4$. Parameterising by $\sigma$: $\log p(y|\mathrm E_{\rm post}\theta)=-40.5$. So $p_{\rm DIC}=2(-40.5+42.0)=3.0$, $\widehat{\mathrm{elpd}}_{\rm DIC}=-40.5-3.0=-43.5$, $\mathrm{DIC}=87.0$.
- *WAIC.* $\mathrm{lppd}=-40.9$. $p_{\rm WAIC1}=2(-40.9-(-42.0))=2.2$ (the text writes the expectation term loosely as $\mathrm E_{\rm post}(y|\theta)$). $p_{\rm WAIC2}=2.7$. So $\widehat{\mathrm{elppd}}_{\rm WAIC1}=-43.1$, $\widehat{\mathrm{elppd}}_{\rm WAIC2}=-43.6$; WAIC is 86.2 or 87.2.
- *LOO-CV.* 15 fits. $\mathrm{lppd}_{\rm loo\text{-}cv}=-43.8$, times $-2$ is 87.6. $p_{\rm loo\text{-}cv}=-40.9-(-43.8)=2.9$.
- All give reasonable effective parameter counts (3 parameters). *External validation*: the 2012 election is just one data point, which shows the difficulty of external validation here (pp. 177–178).

### 7.3 Model comparison based on predictive performance (pp. 178–182)
(A footnote again recommends Vehtari et al. 2017.) The usual workflow is to start simple, check fit (Sections 6.3, 6.4), then expand (Section 7.5) (p. 178). Two scenarios (p. 178):
- *Nested models*: the larger one fits better and makes more sense but is harder to understand and compute. The key questions are whether the fit gain justifies the difficulty, and whether the prior on the extra parameters is reasonable.
- *Nonnested models* (e.g. different predictor sets): usually one would rather build a larger model containing both, possibly with an informative prior. Comparing can still show how each set performs alone.

Adjusting for overfitting matters most when complexity differs greatly (p. 178).

**Example: eight schools (pp. 178–181).** Three models for the SAT-coaching data (Section 5.5): *no pooling* ($\tau=\infty$; 8 parameters), *complete pooling* ($\tau=0$; 1 parameter), *hierarchical* ($\tau$ estimated; 8 constrained parameters, effective number below 8). Data points and CV are defined at the school level, since only group-level data exist (pp. 178–179).

Table 7.1 (deviance scale, lower is better for AIC/DIC/WAIC; blank = undefined) (p. 179):

| | No pooling | Complete pooling | Hierarchical |
|---|---|---|---|
| AIC: $-2\,$lpd (at MLE) | 54.6 | 59.4 | – |
| AIC: $k$ | 8.0 | 1.0 | – |
| AIC | 70.6 | 61.4 | – |
| DIC: $-2\,$lpd (at posterior mean) | 54.6 | 59.4 | 57.4 |
| $p_{\rm DIC}$ | 8.0 | 1.0 | 2.8 |
| DIC | 70.6 | 61.4 | 63.0 |
| WAIC: $-2\,$lppd | 60.2 | 59.8 | 59.2 |
| $p_{\rm WAIC1}$ | 2.5 | 0.6 | 1.0 |
| $p_{\rm WAIC2}$ | 4.0 | 0.7 | 1.3 |
| WAIC (with $p_{\rm WAIC2}$) | 68.2 | 61.2 | 61.8 |
| LOO-CV: $-2\,$lppd | – | 59.8 | 59.2 |
| $p_{\rm loo\text{-}cv}$ | – | 0.5 | 1.8 |
| $-2\,$lppd$_{\rm loo\text{-}cv}$ | – | 60.8 | 62.8 |

Row-by-row reading (pp. 179–180):
- *AIC*: no pooling has the best raw fit (MLE sits at the data), but after the correction (8 vs 1) complete pooling has the lowest AIC. AIC is undefined for the hierarchical model.
- *DIC*: identical to AIC for the two flat-prior models. The hierarchical model has fit between the two and $p_{\rm DIC}=2.8$, closer to 1 than 8, because school effects are pooled almost all the way to the common mean. Complete pooling wins, consistent with data compatible with zero between-group variance.
- *WAIC*: fit slightly worse than lpd (the posterior predictive is wider). The corrections are lower: for no pooling and hierarchical, $p_{\rm WAIC}$ is about half of $p_{\rm DIC}$. All $p_{\rm WAIC}$ are much below $p_{\rm DIC}$, because lppd already accounts for much of the parameter uncertainty.
- *CV*: the no-pooling model cannot be cross-validated (it cannot predict a held-out school from the other seven). This is a main difference from information criteria, which assume new data for the same schools. CV's local prediction uses only the other schools; WAIC's also uses the local observation. The two differ more as the hierarchical prior becomes vague (the difference goes to infinity as it becomes uninformative, giving no pooling) (p. 180).

*Comparing.* Complete pooling wins on expected out-of-sample prediction in this dataset. Typically one should estimate the hierarchical variance, but here $\tau=0$ happens to fit best. The authors still prefer the hierarchical model, because they do not believe $\tau=0$. Example: school A estimate 28 (s.e. 15), school C $-3$ (s.e. 16); not significant, and compatible with zero variation, but the authors would be uncomfortable stating a posterior probability of 0.5 that C's effect exceeds A's. A more informative prior on $\tau$ might help, since very large $\tau$ values are implausible and add predictive uncertainty (pp. 180–181).

Predictive measures are best used alongside posterior predictive checks. For hierarchical models the log score can be computed for existing groups (as done here) or for new groups (p. 181).

**Evaluating predictive error comparisons (p. 181).**
- *Statistical significance*: some asymptotic theory suggests the sampling variance of an estimate of average prediction error is of order 1, so differences of less than 1 could typically be attributed to chance. This need not hold for nonnested models. A practical estimate comes from the variation in the pointwise $\widehat{\mathrm{elpd}}_i$ (parametric or nonparametric).
- *Practical significance*: an application-specific scoring function (e.g. AUC in epidemiology) can help. Otherwise calibrate with simple models. Take $n$ voters; model 1 predicts $p=0.5$ for each voter; model 2 assigns 0.4/0.6 correctly. Expected log predictive probability per respondent is $\log0.5=-0.693$ vs $0.6\log0.6+0.4\log0.4=-0.673$. The expected gain is $0.02n$: 20 for $n=1000$, only 2 for $n=10$.
- A larger, better model may not dominate predictive comparisons if its gains are small on an absolute scale and concentrated in a few subsets. Average prediction error "does not tell the whole story of model fit" (p. 181).

**Bias induced by model selection (p. 182).** CV and information criteria correct the double use of data for a given model. But when used to choose a model, the performance estimate of the selected model is biased by the selection. The bias is small for few models. It can be strong if candidates are very many (e.g. number of predictors $p\gg\log n$). The bias can be estimated (e.g. another CV level), but this does not prevent the selection procedure overfitting. This is one reason the authors use CV and information criteria for understanding fitted models, not for choosing among them (p. 182).

**Challenges (p. 182).** AIC fails with strong prior information; DIC gives nonsense when the posterior is not summarised by its mean; WAIC needs a data partition (hard for spatial or network data); CV is costly and not always well defined for dependent data. Predictive comparisons can still make sense for highly dissimilar models, and effective parameter counts help understand splines and Gaussian processes. The authors' current preferred choice is cross-validation. Bayesian CV is asymptotically equal to WAIC; Pareto-smoothed importance sampling LOO-CV is as efficient as WAIC but more robust in finite samples with weak priors or influential observations (p. 182).

### 7.4 Model comparison using Bayes factors (pp. 182–184)
The fully Bayesian alternative gives each model a prior probability and multiplies by its marginal likelihood. The authors generally do not recommend it, because the marginal likelihood is highly sensitive to aspects of the model that are arbitrary and untestable from data (p. 182). For two models $H_1,H_2$:
$$\frac{p(H_2|y)}{p(H_1|y)}=\frac{p(H_2)}{p(H_1)}\times \text{Bayes factor}(H_2;H_1),$$
$$\text{Bayes factor}(H_2;H_1)=\frac{p(y|H_2)}{p(y|H_1)}=\frac{\int p(\theta_2|H_2)p(y|\theta_2,H_2)d\theta_2}{\int p(\theta_1|H_1)p(y|\theta_1,H_1)d\theta_1}\tag{7.16}$$
The Bayes factor is defined only when the marginal density of $y$ under each model is proper (p. 183). Using it means choosing one model or averaging with $p(H_i|y)$; the authors generally prefer an expanded continuous family (p. 183).

**Discrete example (genetics, Section 1.4).** $H_1$: the woman is affected; $H_2$: unaffected. Prior odds $p(H_2)/p(H_1)=1$. Data: two unaffected sons. Bayes factor $=1.0/0.25$, so posterior odds $=4$. Multiplying odds makes accumulation of evidence clear. Bayes factors help here because each alternative makes scientific sense with nothing in between, and each $p(y|H_i)$ is proper (p. 183).

**Continuous example: eight schools.** $H_1$ (no pooling): $y_j\sim \mathrm N(\theta_j,\sigma_j^2)$ with $p(\theta_1,\dots,\theta_J)\propto1$. $H_2$ (complete pooling): $\theta_1=\dots=\theta_J=\theta$, $p(\theta)\propto 1$ (pp. 183–184). With these improper priors, the Bayes factor is $0/0$, undefined. Replace them with independent $\mathrm N(0,A^2)$ priors (large $A$). Then
$$p(\theta_j|y)=(1-\lambda)p(\theta_j|y,H_1)+\lambda p(\theta_j|y,H_2),$$
with the two components normal, centred near $y_j$ and $\bar y$. Here $\lambda$ is proportional to prior odds times the Bayes factor (see Exercise 7.4) (p. 184). Two problems: (1) as $A$ increases with fixed data and prior odds, the posterior concentrates ever more on complete pooling, so the Bayes factor cannot be applied even to noninformative priors defined as limits; (2) results are sensitive to the number of schools (e.g. 80 instead of 8), a scientifically incidental feature (p. 184). The discrepancy with substantive knowledge would send us to a continuous family, $y_j\sim \mathrm N(\theta_j,\sigma_j^2)$, $\theta_j\sim \mathrm N(\mu,\tau^2)$, flat prior on $\mu$, $\tau\in[0,\infty)$ (the Section 5.5 model). Then there is no reason to give discrete positive probability to $\tau=0$ or $\tau=\infty$ (p. 184).

### 7.5 Continuous model expansion (pp. 184–187)
**Sensitivity analysis (pp. 184–185).** The posterior can overestimate uncertainty (not all substantive knowledge is included) and underestimate it (the model is almost certainly wrong; other reasonable models could fit equally well). Alternative models can differ in prior, likelihood, or both. Only models consistent with substantive knowledge and data need consideration. The basic method is to fit several models. Replacing improper priors by proper ones with real knowledge often avoids surprises. Medians are generally less sensitive than means or extreme quantiles; interpolation is less sensitive than extrapolation. 'Robust' models (e.g. $t$ in place of normal) cost more computation (Chapter 17) (p. 185).

**Adding parameters (p. 185).** Reasons to expand: (1) misfit to data or prior knowledge; (2) a questionable assumption (normal to $t$); (3) combining two models $p_1(y,\theta),p_2(y,\theta)$ in a continuous family (the SAT hierarchical model generalises complete pooling $\tau=0$ and no pooling $\tau=\infty$); (4) new data (inserting an experiment into a hierarchical population model; regression of $y|x$ to a model of $(x,y)$ for missing $x$). All have the same structure: the old model $p(y,\theta)$ is embedded in $p(y,\theta,\phi)$ or $p(y,y^*,\theta,\phi)$, with $y^*$ the added data:
$$p(\theta,\phi|y,y^*)\propto p(\phi)p(\theta|\phi)p(y,y^*|\theta,\phi),$$
$$p(\phi|y,y^*)\propto p(\phi)\int p(\theta|\phi)p(y,y^*|\theta,\phi)d\theta\tag{7.17}$$
One must specify $p(\theta|\phi)$ and a hyperprior $p(\phi)$; both typically need thought, especially with noninformative priors (p. 186).

**Other sub-sections (p. 186).**
- *Model choice in analysis*: final models arise after extensive analysis, which relates to multiple comparisons. Hierarchical modelling shrinks all comparisons (e.g. $\theta_j-\theta_k$ toward 0). Running many analyses to find the strongest conclusion remains a danger, only partly alleviated by Bayesian methods.
- *Predictors*: the authors prefer including many predictors and batching them in an analysis-of-variance structure, rather than 'in' or 'out'. Discrete model averaging may help, though they have not used it. For causal inference, estimands are in general not the regression coefficients.
- *Alternative formulations*: adding parameters (estimate variance; $t$ instead of normal) adds flexibility, but there are no general principles for basic model choices yet (pp. 186–187).

**Practical advice (p. 187).** Examine posterior distributions of substantively important parameters and predictions; compare with substantive knowledge, including observed data; use discrepancies to suggest expansions (real prior information, a nonlinear term, or substantive rethinking). A regression with many predictors and a flat prior will tend to overestimate variation among coefficients. An analysis is rarely, if ever, complete with simply rejecting a model. If sensitivity analysis reveals problems, include the other plausible models in the prior or report the sensitivity. Sometimes the data cannot answer a question (p. 187).

*Intuition note.* Instead of a hard choice between two models, add a dial (e.g. $\tau$) whose end settings are the two models, and let the data set the dial. Priors on the dial and on the parameters then do the work that "model probabilities" would do.

### 7.6 Implicit assumptions and model expansion: an example (pp. 187–192)
Inference is a way to explore the implications of a model so they can be compared with data and outside knowledge. Checks must reflect the use: the normal model for football scores predicts win probability well but gives poor predictions of exact ties (pp. 187–188).

**Example: population total of NY municipalities (pp. 188–192).** Estimate the 1960 total population of $N=804$ municipalities from a simple random sample of $n=100$. The data are in Table 7.2, from Rubin (1983a):

| | Population (N=804) | Sample 1 (n=100) | Sample 2 (n=100) |
|---|---|---|---|
| total | 13,776,663 | 1,966,745 | 3,850,502 |
| mean | 17,135 | 19,667 | 38,505 |
| sd | 139,147 | 142,218 | 228,625 |
| median | 1,668 | 2,081 | 1,740 |
| highest | 2,627,319 | 1,424,815 | 1,809,578 |

(The table also gives percentiles; see p. 188.) Sample 1 looks representative; sample 2 has a few too many large values (p. 188). The estimand is
$$y_{\rm total}=N\bar y=n\bar y_{\rm obs}+(N-n)\bar y_{\rm mis}\tag{7.18}$$

*Sample 1.*
- *Normal superpopulation* with uniform prior on $(\mu,\log\sigma)$: $\bar y\sim t_{n-1}(\bar y_{\rm obs},(\frac1n-\frac1N)s^2_{\rm obs})$ (Section 8.3). The 95% interval is $[-5.4\times10^6,\,37.0\times10^6]$. Replacing the lower limit by the sample total (the population total can be no less) gives $[2.0\times10^6,\,37.0\times10^6]$ (p. 188).
- *Lognormal* ($\log y_i\sim \mathrm N(\mu,\sigma^2)$, uniform prior): 100 draws, 95% interval $[5.4\times10^6,\,9.9\times10^6]$, narrower and at first sight better (p. 189).
- *Check*: posterior predictive test statistic $T(y_{\rm obs})=\sum_i y_{\mathrm{obs}\,i}$, the sample total. All 100 replicated totals are below the actual 1,966,745, so the lognormal model is unacceptable for this quantity (p. 189).
- *Power-transformed normal family* with extra parameter $\phi$: $\phi=1$ is normal, $\phi=0$ lognormal (defined in (7.19), Exercise 7.5). Fit by fitting the normal model to transformed data at several $\phi$ values and computing the marginal posterior of $\phi$. With a uniform prior on $\phi$, it peaks near $-\frac18$. The 95% interval is $[5.8\times10^6,\,31.8\times10^6]$, and 15 of 100 replicated totals exceed the observed total, so the check is adequate (p. 189).

The authors then test this "extended procedure" on sample 2 (p. 189).

*Sample 2.*
- Normal: $[-3.4\times10^6,\,65.3\times10^6]$, or $[3.9\times10^6,\,65.3\times10^6]$ after replacing the lower limit with the sample total.
- Lognormal: $[8.2\times10^6,\,19.6\times10^6]$ (tight), but none of 100 replicated totals reaches the observed total, so it is rejected.
- Power family: $\phi$ peaks at $-\frac14$; 48 of 100 replicated totals exceed the observed one (no apparent problem) (pp. 189–190).
- Knowing the truth (about 13.8 million), the power-family inference is "atrocious": median of the 100 generated $y_{\rm total}$ is $57\times10^7$, the 97th value $14\times10^{15}$, the largest $12\times10^{17}$ (p. 190).

*Why (p. 190).* The problem is not inability to fit but inability of the data to distinguish models with different implications for $y_{\rm total}$. The total depends on the extreme upper tail, beyond the largest observed value. For the power family, that tail (beyond the 99.5% quantile) is affected dramatically by how well the model fits the main body (0.5%–99.5%). Estimating a total or mean needs realistic extrapolation beyond the data, which must rely on prior assumptions such as the largest possible municipality size. The authors say they were warned by the simulated sample-2 totals: 10 of 100 exceeded 300 million.

*Fix.* Suppose no municipality exceeds $5\times10^6$. Truncate simulated municipality sizes at this bound. The 95% intervals are then $[6\times10^6,20\times10^6]$ (sample 1) and $[10\times10^6,34\times10^6]$ (sample 2). Both are tighter than the untruncated ones and both contain the true total $13.7\times10^6$ (p. 190).

*Why the plain normal works tolerably (pp. 190–191).* Its inference rests on the normal sampling distribution of $\bar y_{\rm obs}$ and the $\chi^2$ distribution of $s^2_{\rm obs}$. These need the central limit theorem to apply, which implicitly bounds the upper tail enough for $n=100$. The authors do not recommend it for clearly nonnormal data; it gives extremely poor inferences for estimands such as the median. A Bayesian analysis that limits large $y_i$ must do so explicitly (p. 191).

*Design and robust questions (p. 191).* A simple random sample is a poor design for the total of a highly skewed population. With stratification variables, one would oversample the large municipalities. For the **median**, the 95% intervals under (a) lognormal, (b) power family, (c) power family truncated at $5\times10^6$ are: sample 1 $[1800,3000]$, $[1600,2700]$, $[1600,2700]$; sample 2 $[1700,3600]$, $[1300,2400]$, $[1200,2400]$. For robust questions, better models matter little, and the sample-median checks look fine for all these models (but not for the untransformed normal) (p. 191).

**Lessons (pp. 191–192).**
1. The lognormal may give inaccurate inferences for the total even when it appears to fit fairly well.
2. Enlarging to a better-fitting family (power transformation) may give less realistic inferences for the total.
These are warnings about models not checked with posterior predictive checks (for variables relevant to the estimand) and reality checks. The authors say the "naive statement" that better fits mean better models and better real-world answers is "not necessarily true" (p. 191). Statistical answers depend on prior assumptions as well as data (pp. 191–192).
3. Inferences may be sensitive to features of the population distribution that the observed data cannot address. Good answers need (a) models flexible enough to specify realistic features not covered by the data (e.g. extreme tails), or (b) questions robust for the type of data collected. (a) is more general, since statisticians often must answer hard questions (e.g. total pollutant emitted, total medical expenses), which are inherently nonrobust. Switching to medians would not answer them. Robustness is a joint property of data, prior knowledge and question; when the important question is inescapably nonrobust, a good Bayesian analysis expresses this sensitivity (p. 192).

*Intuition note.* A tight, good-looking interval can come from a model that is silent about the part of the world that drives the answer. Checking fit to the observed sample is not enough. You must check the quantity you care about, and supply knowledge (like a size cap) where data cannot.

### 7.7 Bibliographic note (pp. 192–194)
Pointers only. The authors state that their treatment of information criteria and CV is taken from Gelman, Hwang and Vehtari (2014), and that the final section elaborates Rubin (1983a). They note that Bayes factors are rarely relevant in their approach (pp. 193–194).

### 7.8 Exercises (pp. 194–195)
Seven exercises: information criteria for the bioassay logistic regression (7.1) and for the meta-analysis (7.3); showing DIC is correct in expectation for normal models or large samples (7.2); Bayes factors with $\mathrm N(0,A^2)$ priors (7.4); Box–Cox priors (7.5); fitting a power-transformed normal model to radon data (7.6); a noninformative prior for the $t$ model (7.7).

## Toy example (ours, not from the text)
Aim: show how lppd and the WAIC penalty arise, with $n=2$ data points and $S=2$ posterior draws. Model: Bernoulli($\theta$), data $y_1=1,\ y_2=0$. Suppose (made up) the posterior draws are $\theta^1=0.8,\ \theta^2=0.4$.

Likelihoods: $p(y_1{=}1|\theta)=0.8,\ 0.4$. $p(y_2{=}0|\theta)=1-\theta=0.2,\ 0.6$.

- Point 1: mean likelihood $=(0.8+0.4)/2=0.6$, so $\log0.6=-0.5108$. Mean log-likelihood $=(\log0.8+\log0.4)/2=(-0.2231-0.9163)/2=-0.5697$.
- Point 2: mean likelihood $=(0.2+0.6)/2=0.4$, so $\log0.4=-0.9163$. Mean log-likelihood $=(-1.6094-0.5108)/2=-1.0601$.
- $\mathrm{lppd}=-0.5108-0.9163=-1.4271$ (7.5).
- $p_{\rm WAIC1}=2[(-0.5108+0.5697)+(-0.9163+1.0601)]=2(0.0589+0.1438)=0.405$.
- $p_{\rm WAIC2}$ (7.12), sample variance with $S-1=1$:
  - Point 1: logs $-0.2231,-0.9163$, mean $-0.5697$, deviations $\pm0.3466$, so $0.1201+0.1201=0.2402$.
  - Point 2: logs $-1.6094,-0.5108$, mean $-1.0601$, deviations $\mp0.5493$, so $0.3017+0.3017=0.6035$.
  - Sum: $p_{\rm WAIC2}=0.8437$.
- $\widehat{\mathrm{elppd}}_{\rm WAIC2}=-1.4271-0.8437=-2.271$, and $\mathrm{WAIC}=-2(-2.271)=4.54$.

Reading: the within-sample score ($-1.43$) is optimistic; the penalty (about 0.84 "effective parameters" here) lowers it to about $-2.27$ as the estimate of out-of-sample accuracy. With only two draws, this illustrates the arithmetic, not a realistic posterior.

## Concepts
- [[elpd-lppd]] (new) — expected log (pointwise) predictive density for new data, (7.1)–(7.2), and its within-sample version lppd (7.4)–(7.5) (pp. 168–169)
- [[scoring-rules-proper-local]] (new) — scoring functions (point prediction) and rules (probabilistic); log score is the unique local proper rule up to an affine transformation (p. 167)
- [[kl-divergence]] — the log predictive density is linked to Kullback–Leibler information; highest expected log predictive density corresponds to lowest KL (large-sample statement) (p. 167)
- [[effective-number-of-parameters]] (new) — data-based penalty ($k$, $p_{\rm DIC}$, $p_{\rm WAIC}$, $p_{\rm loo\text{-}cv}$); about 1 per unconstrained, 0 per prior-determined parameter (pp. 172–174)
- [[aic-dic-waic]] (new) — deviance-based information criteria; AIC uses MLE and $k$, DIC posterior mean and $p_{\rm DIC}$, WAIC the posterior-averaged lppd and $p_{\rm WAIC}$ (pp. 172–174)
- [[cross-validation-loo-waic]] — Bayesian LOO-CV (7.14), with bias correction $b$, PSIS shortcut, $k$-fold alternative (pp. 175–176)
- [[bayes-factor]] (new) — ratio of marginal densities of the data under two models (7.16); needs proper marginals (p. 183)
- [[marginal-likelihood-evidence]] — $p(y|H)$; the authors say it is highly sensitive to arbitrary, untestable model aspects (p. 182)
- [[continuous-model-expansion]] (new) — embed the old model in a larger continuous family $p(y,\theta,\phi)$ with hyperprior $p(\phi)$ (pp. 185–186)
- [[sensitivity-analysis]] (new) — fit several reasonable models and see how inferences change (p. 185)
- [[posterior-predictive-check]] — used with a problem-relevant test statistic (sample total, sample median) (pp. 189–191)
- [[partial-pooling-shrinkage]] — hierarchical model sits between no pooling and complete pooling; shrinks comparisons toward 0 (pp. 179, 186)
- [[power-transformed-normal-family]] (new) — Box–Cox family (7.19); $\phi=1$ normal, $\phi=0$ lognormal (pp. 189, 194)
- [[hierarchical-multilevel-model]] — used for the eight schools; replication can be for existing or new groups (p. 169)

## Canonical instances
- [[election-forecasting-regression]] — Hibbs 'bread and peace' linear regression, $n=15$; running example for all criteria (pp. 165–178)
- [[eight-schools]] — no pooling vs complete pooling vs hierarchical compared by AIC/DIC/WAIC/CV (Table 7.1); Bayes factor failure (pp. 178–184)
- [[genetics-bayes-factor]] — Section 1.4 example with posterior odds 4 (p. 183)
- [[ny-municipalities-population-total]] — lognormal and power families, truncation, sample median (pp. 188–192)

## Bridges (candidates)
- [structural-analogy] WAIC/LOO penalty $p_{\rm WAIC}$ ↔ machine learning: held-out validation and degrees of freedom of regularised fits — both estimate the optimism of in-sample fit.
- [same-math] LOO-CV with the log score ↔ machine learning: cross-validated log-loss (negative log predictive probability on held-out points) — the same quantity, computed with a posterior predictive.
- [structural-analogy] Bayes factor sensitivity to prior variance $A^2$ ↔ Bayesian hypothesis testing (Lindley-type behaviour with diffuse priors) — a model's evidence depends on how much prior mass is wasted on unlikely data.
- [metaphor] Truncating tails by substantive upper bound ↔ regularisation by prior knowledge in extrapolation problems.

## Questions this raises
- If predictive scores cannot reliably choose among many models (selection bias, p. 182), what should guide the decision to expand a model?
- How should one define data "points" for WAIC and CV in structured data (time series, spatial, network), where the independence partition fails?
- How is the effective number of parameters in a hierarchical model related to $\tau$ (p. 172)? How would one derive the 1-to-8 range?
- Can a prior on tail behaviour be elicited in practice when the estimand (a total) depends on it, as in the municipality example?

## Exercises worth doing
- Ex. 7.1 (p. 194) — compute all four predictive measures for the bioassay logistic regression — difficulty: medium
- Ex. 7.2 (p. 194) — show DIC is correct in expectation for normal models or large $n$ — difficulty: hard
- Ex. 7.4 (p. 194) — derive the Bayes factor for the $\mathrm N(0,A^2)$ eight-schools models, its limit $A\to\infty$, and dependence on $J$ — difficulty: hard
- Ex. 7.5 (p. 194) — why a prior $p(\phi)$ alone fails for Box–Cox, and how $\dot y^{1-\phi}p(\phi)$ fixes it — difficulty: hard
- Ex. 7.6 (p. 195) — fit a power-transformed normal model to radon data and check it with posterior predictive simulation — difficulty: medium
- Ex. 7.7 (p. 195) — build a noninformative prior for the $t$ model's $(\mu,\log\sigma,\nu)$ — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 175 = printed 165). The last page (pdf 206, printed 196) is blank apart from the header line.
- The text layer garbles Greek letters (θ appears as ω, ∼ as →, and the minus sign in exponents as →); I used the page images. Equations were checked against the images.
- Footnotes on pp. 169 and 178 say that instead of Sections 7.2 and 7.3 the authors recommend Vehtari, Gelman and Gabry (2017).
- p. 177: the formula for $p_{\rm WAIC1}$ is written loosely as $2(\mathrm{lppd}-\mathrm E_{\rm post}(y|\theta))$; the number used (−42.0) is the posterior mean of the log density, as in (7.8).
- p. 180: the sentence on the "center column" of Table 7.1 says its measures are lower "than for no pooling or complete pooling". The center column is complete pooling, so this seems to be a slip; the table shows complete pooling lowest on the corrected measures (AIC, DIC, WAIC, CV).
- p. 190: the true total is called "13.8 million" and then $13.7\times10^6$; Table 7.2 gives 13,776,663.
- p. 174: "$y_i,\dots,y_n$" in the one-sided-constraint example is as printed (presumably $y_1,\dots,y_n$).
- The 7.7 bibliography is summarised only briefly; Exercises are listed without solutions.
