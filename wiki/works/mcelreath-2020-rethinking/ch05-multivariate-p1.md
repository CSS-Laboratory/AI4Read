---
id: mcelreath-2020-rethinking/ch05-multivariate-p1
work: mcelreath-2020-rethinking
unit: "Chapter 5. Multivariate Linear Models (part 1/2): Introduction, 5.1 Spurious association, start of 5.2 Masked relationship"
pages: 119-140
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Multivariate Linear Models (part 1/2): spurious association and masked relationship

## L0 — One line
A regression coefficient answers "what does this predictor add once the other predictors are known?", so adding a predictor can erase an association (spurious) or reveal one (masked).

## L1 — The gist (≤ 120 words)
Why can a predictor look important in a simple regression, then lose or gain importance when others are added? McElreath gives two cases. In US divorce data, marriage rate predicts divorce, but once median age at marriage is in the model, its coefficient is near zero: a spurious association. In primate milk data, neocortex percent and body mass each look weak alone, but both coefficients grow when entered together: a masked relationship. He shows three ways to display what a multivariate model says: predictor residual plots, counterfactual plots and posterior prediction plots. He stresses that the model alone cannot establish causation.

**Prerequisites:** Gaussian linear regression with priors (previous chapter); percentile intervals; posterior sampling (`link`, `sim`); standardizing a variable.

## L2 — Key ideas
- Correlation is very common, so a correlation alone (e.g. Waffle House and divorce) is weak evidence of cause. Multivariate regression helps with confounds (variables that may be correlated with another variable of interest), multiple causes and interactions (the importance of each variable depends on the other); this part mainly deals with confounds and multiple causes. (pp. 119–120)
- Multivariate model: add one parameter × variable term per predictor to the mean, $\mu_i=\alpha+\beta_R R_i+\beta_A A_i$. (pp. 123–124)
- Each coefficient answers: what is the predictive value of this variable once the others are already known? It is not an experimental "control" and not automatically causal. (p. 123)
- In the divorce data, $\beta_R$ moves to about 0 while $\beta_A$ stays near −1.1 once both are in. Marriage rate adds little once age at marriage is known. (pp. 125–126)
- Three displays: predictor residual plots (outcome against the part of a predictor not predicted by the others), counterfactual plots (model predictions with one predictor varied), posterior prediction plots (model predictions against raw data). Each has strengths and limits. (pp. 126–134)
- Counterfactual plots may show impossible predictor combinations and so mislead about interventions. (p. 131)
- Even after "controlling" for other predictors, a leftover correlation (Waffle Houses) need not be real. (p. 134)
- Masking: two predictors correlated with each other, one positively and one negatively with the outcome, can hide each other's effect until both are included. (pp. 135, 140)

## L3 — Walkthrough

### Introduction (pp. 119–120)
- **Waffle House example.** The density of Waffle House diners is associated with divorce rate across US states (Fig. 5.1). The author calls this a misleading correlation. His explanation: Waffle House began in Georgia in 1955 and stayed mostly in the South. Divorce is more common where people marry young, and he says "it's probably just an accident of history" that both occur in the South. (p. 119)
- In large data sets, every pair of variables has a statistically discernible non-zero correlation (p. 119). So we need tools to separate mere association from evidence of causation. One such tool is multivariate regression: using more than one predictor for an outcome. (p. 119)
- **Three reasons for multivariate models:**
  1. *Statistical "control" for confounds.* A confound is a variable that may be correlated with another variable of interest. It can create false importance (Southernness and waffles) or hide real importance. In Simpson's paradox, the direction of an apparent association is reversed by a confound. (p. 119)
  2. *Multiple causation.* An outcome may have several causes, and one cause can hide another. (p. 120)
  3. *Interactions.* The importance of each variable may depend on the other, e.g. light and water for plants. (p. 120)
- The author says the chapter will "begin to deal with the first of these two" (see Reading notes), using additive "main effects". It focuses on two things multivariate models can help with: (1) revealing spurious correlations and (2) revealing important correlations that may be masked by other variables. It warns that extra predictors can hurt (multicollinearity) and meets categorical variables. (p. 120)
- **Rethinking box:** There is no unified approach to causal inference yet. The author says there is general agreement on one thing: "Causal inference always depends upon unverifiable assumptions." (p. 120)

### 5.1 Spurious association (pp. 121–140)
**Setup.** Divorce rate $D_i$ is positively associated with marriage rate and negatively with median age at marriage $A_i$ (Fig. 5.2). A high marriage rate predicting high divorce is suspicious, because it could equally signal a culture that values marriage. (p. 121) Bivariate model for age (priors as printed, predictor standardized):

$$D_i\sim\text{Normal}(\mu_i,\sigma),\quad \mu_i=\alpha+\beta_A A_i,\quad \alpha\sim\text{Normal}(10,10),\ \beta_A\sim\text{Normal}(0,1),\ \sigma\sim\text{Uniform}(0,10)$$

Result (`m5.1`): each additional SD of marriage age (1.24 years) predicts about one fewer divorce per 1000 adults. The 89% interval is about −1.4 to −0.7, so the sign is reliable but the size is uncertain. (p. 122) The analogous model for marriage rate (`m5.2`) gives +0.6 divorces per SD of marriage rate (3.8), a weaker relation. (p. 123)

Comparing coefficients across bivariate models cannot say which predictor is better: they may be independent, redundant, or one may cancel the other's value. The question for a multivariate model is: "What is the predictive value of a variable, once I already know all of the other predictor variables?" (p. 123)

**Rethinking box ("control"):** Calling this "statistical control" implies a causal "effect" and an experimental separation of predictors. These assumptions are not part of the model. The author uses this to separate small-world from large-world interpretation. (p. 123)

**5.1.1 Multivariate notation.** Recipe: (1) choose predictors; (2) give each a parameter; (3) multiply parameter by variable and add the term to the linear model. (p. 123) The model with both predictors:

$$D_i\sim\text{Normal}(\mu_i,\sigma),\quad \mu_i=\alpha+\beta_R R_i+\beta_A A_i$$
$$\alpha\sim\text{Normal}(10,10),\ \beta_R\sim\text{Normal}(0,1),\ \beta_A\sim\text{Normal}(0,1),\ \sigma\sim\text{Uniform}(0,10)$$

The expected divorce rate is the sum of three independent terms: a constant, a marriage-rate term, an age term. Reading "+" as "or" suggests independent associations, "which may be purely statistical or rather causal". (p. 124)

*Overthinking (design matrix).* General form $\mu_i=\alpha+\sum_{j=1}^{n}\beta_j x_{ji}$, or $\mu_i=\alpha+\beta_1x_{1i}+\dots+\beta_nx_{ni}$. In matrix form $\mathbf m=\mathbf X\mathbf b$. Here $\mathbf m$ is the vector of predicted means (one per data row), $\mathbf b$ the column vector of parameters, and $\mathbf X$ the design matrix. $\mathbf X$ has as many rows as data and predictors + 1 columns; the extra first column is all 1s, which multiplies the intercept. In R this is `X %*% b`. The book does not use this approach. Software uses it for the matrix formula for least-squares (maximum likelihood) estimates in linear regression. (p. 124)

**5.1.2 Fitting the model (`m5.3`).** Same priors, `mu <- a + bR*Marriage.s + bA*MedianAgeMarriage.s`. (p. 125) `precis` output (columns: mean, SD, 5.5%, 94.5%, i.e. an 89% interval):

| | Mean | SD | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 9.69 | 0.20 | 9.36 | 10.01 |
| bR | −0.13 | 0.28 | −0.58 | 0.31 |
| bA | −1.13 | 0.28 | −1.58 | −0.69 |
| sigma | 1.44 | 0.14 | 1.21 | 1.67 |

`bR` is now close to zero with plenty of probability on both sides; `bA` is slightly farther from zero but essentially unchanged. (p. 125) Reading: once we know a State's median age at marriage, there is little or no additional predictive power in knowing its marriage rate. This does not mean marriage rate is useless if age data are missing. (p. 126)

*Intuition note.* The bivariate slope for marriage rate ignores age at marriage. The multivariate coefficient instead reports the association that remains once age at marriage is known; in the residual plot this is the part of marriage rate not expected from age, and it shows little relation to divorce.

**5.1.3 Plotting multivariate posteriors.** One scatterplot is not enough with several predictors. The author offers three displays, each with advantages and deficiencies (p. 126):

**5.1.3.1 Predictor residual plots.** A predictor residual is the average prediction error when all other predictors are used to model the predictor of interest. Plotting the outcome against that residual gives a bivariate regression "of sorts" that has already "controlled" for the other predictor. For marriage rate, model it from age (`m5.4`; $\alpha$'s prior centered at 0 because both variables are standardized): (p. 126)

$$R_i\sim\text{Normal}(\mu_i,\sigma),\ \mu_i=\alpha+\beta A_i,\ \alpha\sim\text{Normal}(0,10),\ \beta\sim\text{Normal}(0,1),\ \sigma\sim\text{Uniform}(0,10)$$

Residual = observed − expected marriage rate, at the MAP values (code 5.7, p. 127). A positive residual means a State marries fast for its age at marriage; a negative one, slow (Fig. 5.3). (p. 127) Residuals are the variation left after removing the purely linear relation. (p. 128)

Fig. 5.4 (left): divorce vs marriage-rate residuals. Average divorce is about the same on both sides of zero, so there is little relation. The slope is −0.13, the same as in `m5.3`. (p. 128) Fig. 5.4 (right): divorce vs age-at-marriage residuals. States with older-than-expected age have lower divorce, slope −1.13, again the same as `m5.3`. (pp. 128–129)

Point: regression reports the remaining association of each predictor after the others are known. The residual plot does by hand what the multivariate model does automatically. For non-additive relations among predictors, the author says the basic logic of statistical control does not change but the details do, and these residual plots do not in general work the same way. (p. 129)

**5.1.3.2 Counterfactual plots.** These show the model's implied predictions for any predictor values, even unobserved or impossible combinations. The simplest use: hold all predictors at constant values except one. (p. 129) Code: build `pred.data` with `Marriage.s` over a sequence and `MedianAgeMarriage.s` fixed at its mean (zero, since it is centered). Use `link` for the mean and `sim` for outcomes. (pp. 129–130) The other plot swaps the roles (p. 131). Fig. 5.5: the plot varying marriage rate is nearly flat; the plot varying age falls steadily. Dark band: 89% interval of the mean; light band: 89% prediction interval. (p. 130) These plots have the same slopes as the residual plots but show no data and show intervals on the data scale. (p. 131)

*Tension.* In the model one can change age at marriage without changing marriage rate. In reality probably not: paying couples to marry at 35 would also lower the number who ever marry. Here this hardly matters because marriage rate has almost no effect on prediction once age is known. When several predictors matter, counterfactual plots "may also mislead" by showing impossible combinations. This is a serious obstacle if the goal is to intervene. (p. 131)

*Intuition note.* A counterfactual plot asks the fitted model "what if only this variable changed?". The model can answer even when the real world could not produce that case.

**5.1.3.3 Posterior prediction plots.** Two uses: (1) check whether the model fit correctly (software or user errors); (2) see how the model fails, by inspecting badly predicted cases. (pp. 131–132) Code 5.11 uses `link` and `sim` on the original data. (p. 132)
- Fig. 5.6(a), predicted vs observed with the line of perfect prediction: the model under-predicts at very high divorce rates and over-predicts at very low ones. Idaho (ID) and Utah (UT) have much lower divorce than predicted. (p. 132)
- Fig. 5.6(b), mean prediction error per State, sorted: the large failures are clearer, e.g. Idaho and Maine. Such plots take much space with many cases. (p. 134)
- Fig. 5.6(c): plot the divorce residuals against a new predictor, Waffle Houses per capita. A small positive correlation remains despite "controlling" for marriage rate and age. The author says this "does not mean that the correlation is real": spurious correlations can be found in the leftover variation however many predictors are included. (p. 134)

**Rethinking box:** Models quantify uncertainty only as the model understands the problem. Answers about truth and causation usually depend on information not in the model. A correlation could vanish or reverse when another predictor is added, and we may not notice if we cannot think of one. Rounds of model criticism and revision are the real tests of hypotheses; procedures called "tests" are small parts of that conversation. (p. 134)

**Overthinking: simulating spurious association.** A truly causal $x_{real}$ influences both $y$ and $x_{spur}$ (code 5.15, $N=100$):
`x_real <- rnorm(N)`; `x_spur <- rnorm(N, x_real)`; `y <- rnorm(N, x_real)`. Both $x$'s correlate with $y$. Regressing $y$ on both, the author says the posterior mean for $x_{spur}$ will be close to zero and that for $x_{real}$ closer to 1. (p. 135)

### 5.2 Masked relationship (pp. 135–140, part continues in the next part)
**Setup.** Another reason for multiple predictors is to measure direct influences of several factors when none is apparent in bivariate relationships. This tends to occur when two predictors are correlated with each other, but one is positively and the other negatively correlated with the outcome. (p. 135) Data: `milk`, primate milk composition, 29 rows and 8 variables. Hypothesis (popular): primates with larger brains produce more energetic milk. Variables used: `kcal.per.g` (energy per gram of milk), `mass` (average female body mass, kg), `neocortex.perc` (neocortex as % of brain mass). (p. 135)

**Missing values.** `map` with `neocortex.perc` fails with "initial value in 'vmmin' is not finite", because the column has `NA`s and `dnorm` returns `NaN`. Fix: keep complete cases, `dcc <- d[complete.cases(d),]`, giving 17 rows. Automated tools like `lm` and `glm` drop such cases for you, which is not always good if you are not aware of it (one reason is deferred to the next chapter). (p. 136)

**Bivariate neocortex model (`m5.5`):**
$$k_i\sim\text{Normal}(\mu_i,\sigma),\ \mu_i=\alpha+\beta_n n_i,\ \alpha\sim\text{Normal}(0,100),\ \beta_n\sim\text{Normal}(0,1),\ \sigma\sim\text{Uniform}(0,1)$$
(priors from the code, pp. 136–137). Result: $\alpha=0.353$ (SD 0.471), $\beta_n=0.005$ (SD 0.007; 89% interval −0.007 to 0.016), $\sigma=0.166$. (p. 137) Going from the smallest neocortex percent (55%) to the largest (76%) changes the expected value by $\hat\beta_n\times(76-55)\approx 0.09456654$ (printed output of code 5.22), below 0.1 kcal. The data range from under 0.5 to over 0.9. So the association is weak and imprecise: many mildly positive and mildly negative slopes are plausible (Fig. 5.7, top left). (p. 137)

**Why log mass.** Body mass often relates to other variables by magnitudes. Taking the log means we suspect that the magnitude of body mass is linearly related to milk energy. (pp. 137–138)

**Bivariate log-mass model (`m5.6`):** $\alpha=0.71$ (SD 0.05), $\beta_m=-0.03$ (SD 0.02; interval −0.06 to 0.00), $\sigma=0.16$. The association is negative and seems stronger than that of neocortex, but is quite uncertain (Fig. 5.7, top right). (p. 139)

**Joint model (`m5.7`):**
$$k_i\sim\text{Normal}(\mu_i,\sigma),\ \mu_i=\alpha+\beta_n n_i+\beta_m\log(m_i)$$
$$\alpha\sim\text{Normal}(0,100),\ \beta_n\sim\text{Normal}(0,1),\ \beta_m\sim\text{Normal}(0,1),\ \sigma\sim\text{Uniform}(0,10)$$
(the printed code uses `dunif(0,1)` for sigma). (p. 139) Result: $\alpha=-1.09$ (SD 0.47), $\beta_n=0.03$ (SD 0.01; 0.02 to 0.04), $\beta_m=-0.10$ (SD 0.02; −0.13 to −0.06), $\sigma=0.11$. Both associations increased: the neocortex mean rose more than sixfold with an 89% interval entirely above zero, and the log-mass mean is more strongly negative. (p. 140) Counterfactual plots hold log mass at its mean while neocortex varies (Fig. 5.7, bottom left); the log-mass plot is left to the reader. (p. 140)

**Why it happens.** Two variables correlate with the outcome, one positively and one negatively, and the two predictors correlate positively with each other. So they tend to cancel one another out. The model asks whether species with high neocortex *for their body mass* have richer milk, and whether species with high body mass *for their neocortex percent* do. Bigger species (apes) have less energetic milk; species with more neocortex tend to have richer milk. (p. 140) The pages given end mid-sentence here: "The fact that these two…". (p. 140)

*Intuition note.* Each predictor pulls the outcome in the opposite direction, but the two move together across species. Looked at alone, the pulls tend to cancel and each looks weak. Compared at the same level of the other, each effect shows up.

## Toy example (ours, not from the text)
Four states, standardized-like values with means 0: age $A=(-2,-1,1,2)$, marriage rate $R=(3,0,-2,-1)$, divorce $D=(12,11,9,8)$, i.e. $D=10-A$ exactly.
1. **Bivariate D on R.** $\bar R=0$, $\bar D=10$. $\sum R(D-10)=3(2)+0(1)+(-2)(-1)+(-1)(-2)=10$. $\sum R^2=9+0+4+1=14$. Slope $=10/14\approx0.71$. Marriage rate alone looks positively related to divorce.
2. **Residualize R on A.** $\sum AR=(-2)(3)+(-1)(0)+(1)(-2)+(2)(-1)=-10$; $\sum A^2=10$; slope $-1$, intercept 0. Residuals $R-(-A)=(3-2,\,0-1,\,-2+1,\,-1+2)=(1,-1,-1,1)$.
3. **D on the residuals.** $\sum \text{resid}\times(D-10)=1(2)+(-1)(1)+(-1)(-1)+1(-2)=0$. Slope 0: once age is known, the leftover marriage-rate variation does not predict divorce.
4. **Joint model.** $D=10+0\cdot R-1\cdot A$ fits every state exactly: $A=-2\to12$, $-1\to11$, $1\to9$, $2\to8$. So the best-fitting $\beta_R=0$ and $\beta_A=-1$. The bivariate 0.71 was borrowed from age.

## Concepts
- [[multiple-regression]] (new) — outcome mean modeled as intercept plus sum of parameter × predictor terms (pp. 119, 123–124)
- [[confound]] (new) — variable that may be correlated with another variable of interest, creating or hiding associations (p. 119)
- [[spurious-association]] (new) — a predictor's apparent importance that is near zero once another predictor is in the model, as for marriage rate once age at marriage is included (pp. 119, 125–126)
- [[masked-relationship]] (new) — two correlated predictors with opposite-signed relations to the outcome hide each other until both are included (pp. 135, 140)
- [[simpsons-paradox]] — a confound can reverse the direction of an apparent association; only mentioned here (p. 119)
- [[design-matrix]] (new) — matrix $\mathbf X$ with a column of 1s plus one column per predictor, so $\mathbf m=\mathbf X\mathbf b$ (p. 124)
- [[predictor-residual-plot]] (new) — outcome plotted against the part of one predictor not predicted by the others (pp. 126–129)
- [[counterfactual-plot]] (new) — model predictions as one predictor varies and others are held fixed, possibly at impossible combinations (pp. 129–131)
- [[posterior-predictive-check]] — compare model-implied predictions with observed data, to find fit errors and failures (pp. 131–134); the author calls these "posterior prediction plots"
- [[credible-interval]] — here an 89% percentile interval (5.5%–94.5%), sometimes called "confidence interval" in the text (pp. 122, 125; "confidence" wording also pp. 132, 139)
- [[quadratic-approximation]] (new) — the text calls the `precis` output of a `map` fit the "quadratic approximate posterior" (p. 137)

## Canonical instances
- [[waffle-house-divorce]] — a correlation the author considers misleading, tied to Southernness (pp. 119–120, 134)
- [[divorce-marriage-age]] — marriage rate's association with divorce vanishes once median age at marriage is included (pp. 121–129)
- [[simulated-spurious-predictor]] — code 5.15, $x_{real}$ drives both $y$ and $x_{spur}$ (p. 135)
- [[primate-milk-masking]] — neocortex percent and log body mass mask each other in predicting milk energy (pp. 135–140)

## Bridges (candidates)
- [structural-analogy] $x_{real}\to x_{spur}$ and $x_{real}\to y$ (p. 135) ↔ Causal DAG: a fork, where a common cause creates an association between its two effects — the text does not use DAG language.
- [metaphor] counterfactual plot (changing one predictor in the model) ↔ do-operator: both set a variable by hand, but the text makes no claim that the plot is an intervention estimate.
- [same-math] design matrix, $\mathbf m=\mathbf X\mathbf b$ and least-squares formula (p. 124) ↔ linear algebra / OLS: same matrix form.
- [structural-analogy] predictor residual plot ↔ partialling out one regressor: the plotted slopes equal the joint-model coefficients here (pp. 128–129).

## Questions this raises
- Do the residual-plot slopes always equal the multivariate coefficients, or only in additive linear models like these? (p. 129 hints at the latter.)
- If marriage rate and age at marriage are related causally, which causal story fits "marriage rate adds nothing once age is known"?
- How should one handle missing values (the 29 → 17 rows) beyond dropping cases? (The text defers this to the next chapter, p. 136.)
- When two predictors are highly correlated, when does masking become harmful multicollinearity? (Announced, p. 120.)

## Reading notes
- This part starts at the chapter opening (printed p. 119) and ends mid-sentence at the bottom of p. 140 in section 5.2; the source was split at a section boundary. Printed = pdf − 14.
- No exercises appear in these pages.
- Mismatches in the source: p. 120 says the chapter "begin[s] to deal with the first of these two", though three reasons are listed. The p. 139 math form gives $\sigma\sim\text{Uniform}(0,10)$ but code `m5.7` uses `dunif(0,1)`. Text on pp. 129–130 refers to `MAM.avg` and `MR.seq`, but the code uses `A.avg` and `R.seq`. The p. 125 text writes `ba` for `bA`. The p. 127 text says residuals are "predicted minus observed", but code 5.7 and the interpretation use observed − predicted.
- p. 122 says the association is "implausibly positive" in a sentence about the negative age coefficient; the wording is unclear, so I did not use it.
- The output column heads "5.5%" and "94.5%" span 89% (94.5 − 5.5); p. 122 mentions an 89% interval and p. 125 says only "percentile intervals".
- Fig. 5.6(c)'s x-axis is labelled "Waffles per capita"; the text says Waffle Houses per capita.
