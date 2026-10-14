---
id: mcelreath-2020-rethinking/ch06-overfitting-p2
work: mcelreath-2020-rethinking
unit: "Chapter 6. Overfitting, Regularization, and Information Criteria (part 2/2: §6.3–6.7)"
pages: 186-207
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 10
---
# Regularizing priors, information criteria (AIC, DIC, WAIC), model comparison and averaging

## L0 — One line
Skeptical (regularizing) priors reduce overfitting while you estimate, and information criteria such as WAIC estimate out-of-sample deviance from the training sample alone, so models can be compared and their predictions averaged rather than one model being "selected".

## L1 — The gist (≤ 120 words)
How can we build models that predict new data well, when fit to the training sample always improves with more parameters? This part gives two tools. Regularizing priors (skeptical priors on slopes) reduce overfitting during estimation. Information criteria (AIC, DIC, WAIC) estimate out-of-sample deviance from the sample alone. AIC adds 2 × the number of parameters to training deviance; WAIC works pointwise from posterior samples. A primate-milk example shows how to rank models, compute Akaike weights, compare estimates, and average predictions across models instead of picking one. The author stresses that all of this is heuristic and gives no guarantees.

**Prerequisites:** Gaussian likelihood and priors; posterior samples; overfitting (fitting the quirks of the training sample); deviance (a −2 × log-likelihood scale; lower is better); the train/test idea from part 1; averages and variances.

## L2 — Key ideas
- Flat priors let the model fit the training sample as fully as possible; a skeptical prior slows learning. Tuned well it cuts overfitting, but if too tight it causes underfitting (p. 186).
- In simulations, tighter priors worsen training deviance but improve test deviance. The effect is large at N = 20 and small at N = 100 (p. 187).
- With flat priors the gap between test and training deviance is about 2 × number of parameters, which gives AIC = D_train + 2p. AIC needs flat priors (or priors overwhelmed by the likelihood), a near-Gaussian posterior and N ≫ k (pp. 188–189).
- DIC uses the posterior of the deviance and the penalty p_D = D̄ − D̂. WAIC sums pointwise log average likelihood (lppd) minus a variance penalty p_WAIC, and needs no Gaussian posterior (pp. 190–192).
- Compare models only when all are fit to exactly the same observations. Use WAIC together with each model's estimates and posterior predictive checks (comparing data simulated from the fitted model with the observed data), because WAIC alone says little about why a model does better (p. 196). The ranking table adds dWAIC (each WAIC minus the lowest), the standard error (SE) of WAIC and the standard error of the difference (dSE), which show the uncertainty in WAIC and in differences (pp. 198–199).
- Akaike weights put dWAIC on a probability-like scale. They are heuristic and depend on the set of models compared (pp. 199–200).
- Model averaging means averaging predictions, not parameters, with weights. It is conservative; here it widened the 89% interval of the averaged predictions μ, which then includes a slope of zero (pp. 196, 203–204).
- Regularization and information criteria are complementary: regularization, as long as it is not too strong, reduces overfitting within a model, and information criteria measure it across models (p. 194). The author calls these tools heuristic with no guarantees (p. 205). After the poor-town/wealthy-town example he writes: "As always, statistics is no substitute for science." (p. 195)

## L3 — Walkthrough

### (End of §6.2 code, p. 186)
The page begins with the last lines of the plotting code for the train–test simulation of part 1. The author notes that `?sim.train.test` shows how to simulate other train–test scenarios (p. 186).

### 6.3 Regularization (pp. 186–188)
- **Root of overfitting.** The model gets "overexcited" by the training sample. With flat or nearly flat priors every parameter value looks equally plausible, so the posterior encodes as much of the sample, via the likelihood, as possible (p. 186).
- **Remedy.** Use a *skeptical* prior, one that slows the rate of learning from the sample. The common version is a **regularizing prior** on a slope coefficient. Tuned properly it reduces overfitting while still letting the model learn regular features. If it is too skeptical, regular features are missed and the model underfits. So the problem is one of tuning. Even mild skepticism can help, and "doing better is all we can really hope for" in the large world (p. 186).
- **Example model** (p. 186):
$$y_i \sim \text{Normal}(\mu_i,\sigma),\quad \mu_i = \alpha+\beta x_i,\quad \alpha\sim\text{Normal}(0,100),\quad \beta\sim\text{Normal}(0,1),\quad \sigma\sim\text{Uniform}(0,10)$$
- $x$ is standardized (mean 0, SD 1), so the prior on $\alpha$ is nearly flat and has no practical effect (p. 186).
- The prior $\beta\sim\text{Normal}(0,1)$ makes the model skeptical of values above 2 or below −2. A Gaussian with SD 1 puts only 5% of its plausibility beyond 2 SD. Reading with standardized $x$: a 1-SD change in $x$ is very unlikely to produce 2 units of change in the outcome (p. 186).
- Figure 6.8 shows three priors: Normal(0,1) (dashed), Normal(0,0.5) (thin) and Normal(0,0.2) (thick). Mass piles up near zero, so estimates are shrunk towards zero (pp. 186–187).
- **Simulation (Fig. 6.9).** Five models were simulated 10,000 times for each of the three priors. The points are the flat-prior deviances from part 1 (training in blue, test in black); the lines show each prior (p. 187).
  - At N = 20 the training deviance always gets worse with tighter priors. The test deviance improves (gets smaller). The 3-parameter model is still best out of sample, and the priors barely change it (p. 187).
  - With Normal(0,0.2), the 4- and 5-parameter models are "barely worse" than the 3-parameter one, so harm from complexity is greatly reduced if the prior is tuned right (p. 187).
  - At N = 100 the priors matter much less. The priors do help, but overfitting was less of a concern, and the data can overwhelm even Normal(0,0.2) (p. 187).
- **Tuning.** With enough data, split into train and test and choose the prior with the smallest test deviance. This is the essence of **cross-validation**. If all data are needed for training, tuning the prior may not be so easy. We would want to predict out-of-sample deviance from the sample at hand, which motivates §6.4 (pp. 187–188).
- *Box: multilevel models.* They learn the strength of the prior from the data, so they can be seen as adaptive regularization (Ch. 12) (p. 188).
- *Box: ridge regression.* Linear models with zero-centred Gaussian priors on slopes are sometimes called ridge regression. It takes a precision $\lambda$ describing the narrowness of the prior. $\lambda>0$ gives less overfitting; too large a $\lambda$ risks underfitting. It was not originally Bayesian. It computes no posterior; it modifies OLS (ordinary least squares: choose parameters minimising squared prediction errors) by putting $\lambda$ into the matrix-algebra formula. R's `lm.ridge` fits it (p. 188).

*Intuition note.* A regularizing prior is like a brake on learning from a small sample. It costs fit to the training data, but a model that fits less eagerly often predicts new data better.

### 6.4 Information criteria (pp. 188–195)
- **Train–test gap (Fig. 6.10, flat priors).** The average distance between training and test deviance is nearly twice the number of parameters, at both N = 20 and N = 100. The printed gaps at N = 20 are 2, 4.1, 5.3, 7.6, 9.7 for 1–5 parameters. At N = 100 they are 1.9, 4.1, 4.9, 7.1, 8.5 (pp. 188–189).
- The dashed lines in the figure are training deviance + 2 × parameters. They trace the average out-of-sample deviance closely (p. 189).
- **AIC** (Akaike information criterion), where $p$ is the number of free parameters (p. 189):
$$\text{AIC}=D_{\text{train}}+2p$$
- All information criteria target the same thing, out-of-sample deviance, under more or less general assumptions. AIC is the oldest and most restrictive and is reliable only when (p. 189):
  1. the priors are flat or overwhelmed by the likelihood;
  2. the posterior is approximately multivariate Gaussian;
  3. $N$ is much greater than the number of parameters $k$.
- Because flat priors are "hardly ever the best", the section moves to DIC and WAIC. **DIC** accommodates informative priors but still assumes a Gaussian posterior and $N\gg k$. **WAIC** makes no assumption about posterior shape (p. 190).
- *Box: consistency.* AIC, DIC and WAIC do not always give the "true" model the best expected $D_{\text{test}}$, so they are not consistent for model identification. They aim at prediction, not at finding the true model. Consistency is judged as $N\to\infty$. In that limit the most complex model is chosen, but its predictions match the true model, since every parameter is precisely estimated. The 5-parameter model would show coefficients after the second as almost zero. Also, in the natural and social sciences the candidate models are almost never the data-generating ones (p. 190).

*Intuition note.* With flat priors, test deviance is on average about 2 points per parameter worse than training deviance (Fig. 6.10). Adding $2p$ to the training deviance is a simple way to correct for that optimism.

#### 6.4.1 DIC (pp. 190–191)
- DIC is built from the *posterior distribution of the deviance*. Since parameters have a posterior and deviance is computed from them, deviance has one too (p. 190).
- $D$ is the training deviance computed for each posterior sample (10,000 samples give 10,000 values). $\bar D$ is their average. $\hat D$ is the deviance at the posterior mean of each parameter (p. 190).
$$\text{DIC}=\bar D+(\bar D-\hat D)=\bar D+p_D$$
- $p_D=\bar D-\hat D$ is an "effective" number of parameters, a flexibility or penalty term. It is the expected distance between in-sample and out-of-sample deviance. With flat priors DIC reduces to AIC. In general $p_D$ is some fraction of the parameter count, because regularizing priors limit flexibility (p. 191).
- If a parameter is substantially skewed and matters for prediction, DIC (like AIC) can go "horribly wrong" (p. 190). In `rethinking`, `DIC` works on `map` and `map2stan` fits (p. 191).

#### 6.4.2 WAIC (pp. 191–192)
- WAIC is also computed from averages over the posterior, and it estimates out-of-sample deviance. It does not need a Gaussian posterior, is often more accurate than DIC, and is hard to define for some models (p. 191).
- It is **pointwise**: prediction uncertainty is handled observation by observation, because some observations are harder to predict. It assesses flexibility for each observation and sums over observations (p. 191).
- Let $\Pr(y_i)$ be the average likelihood of observation $i$ over posterior samples. With $S$ samples $\theta_s$ this is $\Pr(y_i)=\frac1S\sum_s p(y_i\mid\theta_s)$ *(added step: explicit notation for the author's words)*. Then (p. 191):
$$\text{lppd}=\sum_{i=1}^N\log\Pr(y_i)$$
- In words: the log-pointwise-predictive-density is the total over observations of the log of each observation's average likelihood. Multiplied by −2 it resembles the deviance (p. 191).
- Let $V(y_i)$ be the variance, over posterior samples, of the log-likelihood of $y_i$ (p. 191):
$$p_{\text{WAIC}}=\sum_{i=1}^N V(y_i)$$
- Then (p. 192):
$$\text{WAIC}=-2\,(\text{lppd}-p_{\text{WAIC}})$$
- WAIC needs the data split into independent observations $i=1\dots N$. In a time series, where earlier observations are predictors of later ones, this is unclear. WAIC can be computed as if observations were independent, but it is not clear what it then means (p. 192).
- More generally, the validity of these criteria depends on the prediction task. Not all prediction fits the train–test form used here. The issue returns with multilevel models (p. 192).
- *Box: BIC.* Choosing between BIC and AIC is not a choice between Bayesian and non-Bayesian. BIC relates to the log of the average likelihood of a linear model (the denominator of Bayes' theorem). A ratio of average likelihoods is a **Bayes factor**. Averaging over the prior gives a natural complexity penalty, though not in general the same as with information criteria. Some Bayesians dislike Bayes factors. Even when priors are weak and do not affect estimates within models, they can have a huge impact on comparisons between models. The author treats them as beyond the book's scope and says we can use both approaches (p. 192).
- *Box: WAIC calculation for `cars`* (model with $a\sim\text{N}(0,100)$, $b\sim\text{N}(0,10)$, $\sigma\sim\text{U}(0,30)$; 1000 posterior samples) (pp. 192–193):
  1. Build the log-likelihood matrix `ll`, shape **50 × 1000** (observations × samples).
  2. lppd per observation = `log_sum_exp(ll[i,]) - log(n_samples)`, which is the log of the average, computed on the log scale for precision.
  3. $p_{\text{WAIC}}$ per observation = `var(ll[i,])`.
  4. `-2*(sum(lppd) - sum(pWAIC))` gave **421.0367**.
  5. Standard error = $\sqrt{N\cdot\text{var}(\text{WAIC}_i)}$, where $\text{WAIC}_i=-2(\text{lppd}_i-p_{\text{WAIC},i})$. This gave **14.43** (printed output: 14.42941). Simulation variance from sampling is much smaller than this standard error.
  6. Each observation has its own penalty term. `pointwise=TRUE` returns the pointwise values, which allows study of how observations contribute to overfitting.

#### 6.4.3 DIC and WAIC as estimates of deviance (p. 194)
- Fig. 6.11: 10,000 simulations at N = 20 for models with 1–5 parameters, with nearly flat Normal(0,100) priors (black) and Normal(0,0.5) priors (blue). DIC and WAIC are both within about 1 deviance point of the actual average in most cases. WAIC is more accurate in this context (p. 194).
- The regularizing prior still helps, and DIC and WAIC track that help. The author says this "suggests" that using both regularization and information criteria will always beat using only one. Regularization, as long as it is not too strong, reduces overfitting within a model; information criteria measure it across models fit to the same data (p. 194).
- *Box: diverse prediction frameworks.* Using a test sample of the same size is not required. A different size only rescales the deviance. AIC orders models like some forms of cross-validation, and WAIC is derived as an approximate Bayesian cross-validation. The distance between models is what matters, not the absolute deviance. Other frameworks exist, e.g. a prequential one judging accumulated learning error. With multilevel models "prediction" is no longer uniquely defined (pp. 194–195).
- The train–test setup assumes the test sample comes from the same process as the training sample (a uniformitarian assumption). **Example:** a height-on-weight regression fit in a poor town of thin people, used to predict in a wealthy town, would predict outrageously tall people, because at large weight the relationship disappears. WAIC will not automatically recognize this, nor will any isolated procedure. Repeated cycles of fitting, prediction and criticism can overcome it (p. 195).

### 6.5 Using information criteria (pp. 195–205)
- **Road so far.** Fit to the training sample always favors complexity. Information divergence is chosen as the accuracy measure, and a meta-model of forecasting yields AIC, DIC and WAIC as estimates of average new-sample deviance. Regularizing priors complement them (p. 195).
- **Model selection** (pick the lowest value, discard the rest) throws away the information in the *differences*. Sometimes differences are large and sometimes small. Relative model accuracy tells us how confident to be about models, conditional on the set compared, as relative posterior probability does for parameters (p. 195).
- **Model comparison:** use DIC/WAIC together with each model's estimates and posterior predictive checks. It is as important to understand *why* a model does better as to measure by how much (p. 196).
- **Model averaging:** use DIC/WAIC to build a posterior predictive distribution that reflects relative accuracy. It guards against overconfidence in model structure. It does *not* mean averaging parameter estimates, since parameters in different models have different meanings, except in special safe cases. So it is "prediction averaging" (p. 196).
- The details of later examples vary, so the author warns against overgeneralizing the example that follows (p. 196).

#### 6.5.1 Model comparison (pp. 196–202)
- **Data.** Primate milk data, complete cases only, with `neocortex = neocortex.perc/100`. This gives 17 rows and 9 columns (p. 196).
- **Key rule:** compared models must be fit to exactly the same observations. Automated routines like `lm` silently drop incomplete cases. A model fit to fewer observations will almost always have better deviance and AIC/DIC/WAIC because it is asked to predict less (p. 196).
- **Four models** for `kcal.per.g`, with flat priors (pp. 196–197): m6.11 intercept only; m6.12 neocortex; m6.13 log(mass); m6.14 both (code 6.22, p. 197).
- To keep $\sigma$ positive, estimate $\log\sigma$ and exponentiate it in the likelihood: `dnorm(mu, exp(log.sigma))`. Since $\exp(x)>0$ for any real $x$, this bounds $\sigma$ to positive reals (pp. 196–197).
- Flat priors are "clearly not the best idea". They show what the sample alone says and how WAIC measures overfitting; regularization is left to the problems (p. 197).

**6.5.1.1 Comparing WAIC values (pp. 197–200)**
- `WAIC(m6.14)` gave −14.96. Its lppd was 12.34, $p_{\text{WAIC}}$ was 4.86 and se was 7.58. Check *(added step)*: $-2(12.34-4.86)\approx-14.96$. Negative values are fine; smaller is better. The se is rough guidance when the sample is small (pp. 197–198).
- `compare()` output (p. 198):

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m6.14 | −15.0 | 4.8 | 0.0 | 0.93 | 7.54 | NA |
| m6.11 | −8.3 | 1.8 | 6.7 | 0.03 | 4.52 | 7.26 |
| m6.13 | −7.9 | 3.0 | 7.1 | 0.03 | 5.67 | 5.33 |
| m6.12 | −6.2 | 2.9 | 8.9 | 0.01 | 4.34 | 7.57 |

- dWAIC is each WAIC minus the lowest. SE is the standard error of each WAIC. dSE is the standard error of the *difference* from the top model. The SE column may not be very precise, but it provides a check against overconfidence in differences between WAIC values (p. 198).
- In `plot(milk.models, SE=TRUE, dSE=TRUE)`, filled points are in-sample deviance ($-2\times$lppd), open points are WAIC, and gray triangles with segments show dSE. Overlap of the individual SEs is *not* the SE of the difference, because WAIC uncertainty is correlated between models. A difference must be computed as a difference (p. 199).
- **Akaike weights** for model $i$ among $m$ models (p. 199):
$$w_i=\frac{\exp(-\tfrac12\,\text{dWAIC}_i)}{\sum_{j=1}^m\exp(-\tfrac12\,\text{dWAIC}_j)}$$
- This undoes the ×(−2), reverses the log by exponentiating, then divides by the total. Weights lie in 0–1 and sum to 1; larger is better. The same formula works for any criterion on the deviance scale (p. 199).
- **Akaike's interpretation (voice: Akaike, as reported by the author; there is no consensus on meaning):** a weight estimates the probability that the model gives the best predictions on new data, conditional on the models considered (p. 199).
- Heuristic reason: treat WAIC as an estimate of $E(D_{\text{test}})$. Converting to likelihoods and standardizing is like Bayes' theorem's denominator, so weights are analogous to posterior probabilities of models (p. 199). In simulation at least, the interpretation turns out appropriate, but it should not be taken too seriously because the future is unlikely to match the past (p. 200).
- Here the best model has over 90% of the weight. But with "only 12 cases" (as printed; see Reading notes) the WAIC error is substantial. Treating the difference m6.14 vs m6.11 as Gaussian with mean 6.7 and SD 7.26, simulation gives $P(\text{diff}<0)\approx 0.1773$. This is heuristic only (p. 200).
- Weights are conditional on the model set, so adding or removing a model changes them. This is a small-world analysis (reasoning only within the models considered, not about the real world) (p. 200).
- **Conclusions** (p. 200): among these four models there is a benefit to using both predictors, at least for describing this sample. The evidence is consistent with neocortex being positively associated with milk energy, controlling for body mass. Either predictor alone is expected to do slightly *worse* than the intercept-only model m6.11, because the penalty outweighs the small gain. The author calls this evidence of a masking effect (each predictor's association hidden unless the other is included).
- *Box: how big a difference is "significant"?* In general, no principled threshold exists, and the 5% convention is just a convention. The book encourages retaining and presenting all models. Averaging predictions often beats selecting one model, which avoids the significance question (pp. 200–201).
- *Box: metaphors.* Models are like race horses: WAIC values are race times, and the gaps are informative. A photo finish gives little confidence about which is best. Weights turn time differences into win probabilities, but they may mislead if conditions change. Models are also like skipping stones: relative average distance is informative, but any single throw is uncertain (p. 201).

**6.5.1.2 Comparing estimates (pp. 201–202)**
- Comparing parameter estimates across models helps in two ways. It explains why some models have lower WAIC. It also shows whether a parameter's posterior is stable when other predictors are added or removed (p. 201).
- `coeftab` output (MAP estimates, i.e. maximum a posteriori: the single most plausible parameter values; `nobs` = 17 for all) (p. 202):

| | m6.11 | m6.12 | m6.13 | m6.14 |
|---|---|---|---|---|
| a | 0.66 | 0.35 | 0.71 | −1.09 |
| log.sigma | −1.79 | −1.80 | −1.85 | −2.16 |
| bn | NA | 0.45 | NA | 2.79 |
| bm | NA | NA | −0.03 | −0.10 |

- Both `bn` and `bm` move farther from zero when both are in the model, as the previous chapter found (masking). Fig. 6.12 plots MAP estimates with 89% percentile intervals (the range between posterior percentiles holding the middle 89%) in a dotchart (pp. 201–203). *Box:* the author prefers dotcharts to barplots because bars clutter the display (p. 203).

#### 6.5.2 Model averaging (pp. 203–204)
- This preserves uncertainty about *models*, as earlier chapters preserved uncertainty about parameters, with weights treated as heuristic plausibilities of being best in testing (p. 203).
- **Ensemble procedure** (p. 203):
  1. compute WAIC (or another criterion) for each model;
  2. compute each model's weight;
  3. compute linear-model values and simulated outcomes for each model;
  4. combine them into an ensemble, using the weights as proportions.
- `ensemble()` calls `link` and `sim` for each model and combines results by Akaike weight (p. 204).
- Counterfactual predictions (predictions at chosen predictor values, whether or not observed) use neocortex from 0.5 to 0.8 (30 values) and mass 4.5 (p. 203).
- **Result (Fig. 6.13).** The averaged mean line barely moves, since m6.14 has about 90% of the weight. The averaged 89% interval is wider and includes a slope of zero. The other models, with about 10% of the weight, imply a near-zero or zero neocortex slope (p. 204).
- The author calls averaging "always a conservative procedure". It will never make a predictor look more influential than in any single model. Sometimes it has no practical impact and sometimes a massive one (p. 204).
- *Box: Curse of Tippecanoe.* From 1840 to 1960, every US president elected in a year ending in 0 died in office (seven in a row). Reagan, elected 1980, broke the pattern. With enough data such patterns can be found almost anywhere. Likewise, trying many combinations and transformations of predictors can find a model that fits a sample well by peculiar overfitting, and WAIC and similar metrics will be fooled. The author sees two defensible cases for fitting many models: exploring data when there are no clear hypotheses (admitted openly and used with averaging), and convincing an audience that no combination of predictors helps much (pp. 204–205).

### 6.6 Summary (p. 205)
- Overfitting is universal: models with more parameters fit a sample better even when the extra parameters are meaningless. Regularizing priors reduce overfitting during estimation; information criteria help estimate its degree. `compare` and `ensemble` handle model sets fit to the same data. The tools are heuristic and give no guarantees.

### 6.7 Practice (pp. 205–207)
- Easy (6E1–6E4) concern information entropy. Medium (6M1–6M6) ask for comparison of AIC/DIC/WAIC, selection vs averaging, the same-observations rule, how effective parameters change with prior concentration, and why informative priors reduce overfitting while overly informative ones underfit (pp. 205–206).
- Hard (6H1–6H6) split the Howell !Kung data into two halves of 272 rows each, with standardized age. They fit polynomial models M1–M6 (degree 1 to 6) to `d1`, compare by WAIC and weights, plot averaged predictions, compute test deviance on `d2`, and fit a degree-6 model with Normal(0,5) priors on the coefficients (pp. 206–207). The author notes that polynomials are not a good way to gain insight here (p. 207).

## Toy example (ours, not from the text)
Two observations, three posterior samples. Likelihoods $p(y_i\mid\theta_s)$:
- Obs 1: 0.2, 0.4, 0.6. Obs 2: 0.1, 0.3, 0.5.

**lppd.** Average likelihood, Obs 1 = (0.2+0.4+0.6)/3 = 0.4, so log = −0.9163. Obs 2 = (0.1+0.3+0.5)/3 = 0.3, so log = −1.2040. lppd = −0.9163 − 1.2040 = −2.1203.

**Penalty (variance of log-likelihoods, divisor $S-1=2$, as R's `var`).**
- Obs 1 logs: −1.6094, −0.9163, −0.5108. Mean = −1.0122. Deviations: −0.5973, 0.0959, 0.5014. Squares: 0.3568, 0.0092, 0.2514, sum 0.6174, so $V=0.3087$.
- Obs 2 logs: −2.3026, −1.2040, −0.6931. Mean = −1.3999. Deviations: −0.9027, 0.1959, 0.7068. Squares: 0.8149, 0.0384, 0.4996, sum 1.3529, so $V=0.6764$.
- $p_{\text{WAIC}}=0.3087+0.6764=0.9851$.

**WAIC** $=-2(-2.1203-0.9851)=-2(-3.1054)=6.21$.

**Akaike weights** for two models with dWAIC = 0 and 2: $e^{0}=1$ and $e^{-1}=0.3679$, total 1.3679. Weights are $1/1.3679=0.731$ and $0.3679/1.3679=0.269$. A 2-point gap gives the worse model about 27% of the weight, which shows why small differences need caution.

## Concepts
- [[regularizing-prior]] (new) — a skeptical prior, usually on slopes, that slows learning from the sample to reduce overfitting; too strong causes underfitting (p. 186)
- [[prior-distribution]] — here used as a tuning dial for how much to trust the sample; Normal(0,1)/(0,0.5)/(0,0.2) differ in strength (pp. 186–187)
- [[cross-validation-loo-waic]] — tune priors or compare models by test-sample deviance; WAIC is derived as an approximate Bayesian cross-validation (pp. 187, 194)
- [[aic]] (new) — $D_{\text{train}}+2p$; reliable only with flat priors (or priors overwhelmed by the likelihood), near-Gaussian posterior, $N\gg k$ (p. 189)
- [[dic]] (new) — $\bar D+p_D$; allows informative priors, assumes Gaussian posterior (pp. 190–191)
- [[waic]] (new) — $-2(\text{lppd}-p_{\text{WAIC}})$; pointwise, no Gaussian assumption (pp. 191–192)
- [[effective-number-of-parameters]] (new) — $p_D$ or $p_{\text{WAIC}}$; a measure of model flexibility that regularization lowers (pp. 191–192)
- [[akaike-weights]] (new) — exponentiated, normalized −½·dWAIC; heuristic chance of being best on new data, given the model set (p. 199)
- [[model-comparison]] (new) — using criteria plus estimates and checks, on the same observations (p. 196)
- [[model-averaging]] (new) — averaging predictions (not parameters) with Akaike weights (pp. 196, 203)
- [[marginal-likelihood-evidence]] — the average likelihood behind BIC and Bayes factors (p. 192)
- [[posterior-predictive-distribution]] — the ensemble is a weighted mix across models (p. 203)
- [[partial-pooling-shrinkage]] — multilevel models as adaptive regularization (p. 188, preview)

## Canonical instances
- [[train-test-regularization-simulation]] (new) — flat vs Normal(0,1/0.5/0.2) priors at N = 20 and 100 (pp. 187–188)
- [[primate-milk-model-comparison]] (new) — m6.11–m6.14; WAIC, weights, masking, averaged predictions (pp. 196–204)
- [[cars-waic-calculation]] (new) — step-by-step WAIC with 50 × 1000 log-likelihood matrix (pp. 192–193)
- [[curse-of-tippecanoe]] (new) — spurious pattern found by searching; analogy to trying many models (pp. 204–205)
- [[height-weight-town-extrapolation]] (new) — a model fit in a poor town predicts badly in a wealthy one (p. 195)

## Bridges (candidates)
- [same-math] Akaike weights ↔ machine learning: softmax of $-\tfrac12\text{dWAIC}$ — the same normalized-exponential formula.
- [structural-analogy] Regularizing Gaussian prior / ridge regression ↔ frequentist statistics: penalized least squares with penalty $\lambda$ — the author says both views exist (p. 188).
- [structural-analogy] Model averaging ↔ forecasting: ensemble forecasts — predictions are combined by weights to express uncertainty.
- [structural-analogy] Curse of Tippecanoe ↔ statistics: multiple comparisons / data dredging — searching many patterns finds coincidences.
- [metaphor] Models as race horses or skipping stones (p. 201) ↔ model uncertainty: confidence depends on the gaps between results.

## Questions this raises
- Why is the penalty close to $2p$ in the simulations, and under what conditions does this fail?
- How should one choose the strength of a regularizing prior when there is too little data to hold out a test sample?
- How should the uncertainty in WAIC (dSE) be passed on to the Akaike weights? The author says it should propagate (p. 200).
- When observations are not exchangeable (time series, multilevel data), what does "out-of-sample" mean, and what should replace WAIC?

## Exercises worth doing
- Ex. 6M3 (p. 206) — why models must use the same observations; try it with different numbers of rows — difficulty: easy
- Ex. 6M4 (p. 206) — how the effective number of parameters changes as a prior concentrates; experiment — difficulty: medium
- Ex. 6M5 and 6M6 (p. 206) — informal accounts of why informative priors reduce overfitting but over-informative priors underfit — difficulty: medium
- Ex. 6H1–6H3 (p. 207) — WAIC ranking, weights and averaged predictions for polynomial models — difficulty: medium
- Ex. 6H4–6H5 (p. 207) — compare test deviance with WAIC, i.e. check how well WAIC estimates out-of-sample deviance — difficulty: hard
- Ex. 6H6 (p. 207) — regularizing priors on the degree-6 model versus the best WAIC model — difficulty: hard

## Reading notes
- Edition: these pages are from the **1st edition** of *Statistical Rethinking*, not the 2nd (2020) that the work id names. No edition statement is printed on these pages; the evidence is the running header "6. OVERFITTING, REGULARIZATION, AND INFORMATION CRITERIA" and the `map`/`map2stan`/`ensemble` code and DIC/WAIC `compare` output. Chapter numbers here are 1st-edition numbers.
- This is part 2 of Chapter 6. It starts at printed p. 186, in the last lines of the part-1 simulation code, then §6.3 begins. It ends with §6.7 Practice on p. 207. Printed p. 208 (pdf 222) is blank. Page offset: printed = pdf − 14; the page labels give printed numbers.
- Source inconsistency: the text on p. 200 says "only 12 cases", but the data frame has 17 rows (p. 196) and `coeftab` shows `nobs` = 17 (p. 202). I kept "12" only as a quoted reading and flagged it here.
- On p. 199, the sentence "−2 × lppd, which is 2pWAIC from the corresponding WAIC value" is ambiguous. I read it as: the in-sample point sits $2p_{\text{WAIC}}$ below the WAIC point.
- Ex. 6M6 reads "information explanation" in the image; probably "informal". Ex. 6H2 says "97% confidence interval", while the rest of the chapter uses 89% intervals.
- Footnote numbers (94–105) appear in the text, but the notes themselves are not in these pages. The R output values (421.0367, 14.42941 shown here rounded as 14.43, table values) are copied from the printed output.
