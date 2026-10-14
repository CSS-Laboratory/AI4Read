---
id: hernan-2020-whatif/ch11-model
work: hernan-2020-whatif
unit: "11 Why model?"
pages: 153-162
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Why model?

## L0 — One line
When data are too thin to "speak for themselves", a model adds an a priori restriction that lets us borrow information, and the price is possible bias if the restriction is wrong (versus larger variance if we restrict less).

## L1 — The gist (≤ 120 words)
How can we estimate a mean outcome E[Y|A=a] when few or no sampled individuals have A=a? Averaging within treatment groups (a nonparametric estimator) breaks down when A has many levels. A parametric model, for example a straight line, borrows information from individuals with other values of A, which smooths the estimate. But the estimate is valid only if the model is correctly specified. Less smooth models (more parameters) protect against bias but give wider confidence intervals. Choosing a model means trading bias against variance. Part I of the book used only saturated models, which impose no restriction; Part II mostly uses parametric models.

**Prerequisites:** sample mean and confidence interval (Ch. 10); least-squares line fitting; the idea of a conditional mean E[Y|A]; for the optional notes, frequentist vs Bayesian probability.

## L2 — Key ideas (5–10 bullets)
- **Data cannot always speak for themselves.** With a treatment that has many levels and only 16 people, the group average is undefined at unobserved levels (p. 154).
- **A model is an a priori restriction** on the joint distribution of the data. It adds information to make up for what the data lack (pp. 155–156).
- **Parametric estimators** (e.g. least squares on a line) can estimate quantities that nonparametric estimators cannot. Their inferences are correct only if the model is correctly specified (p. 156).
- **Saturated "models"** have as many parameters as unknown conditional means and restrict nothing. They are equivalent to sample averages, and Part I used only these (p. 156).
- **Smoothing** means estimating E[Y|A=a] by borrowing information from individuals with A≠a. The fewer the parameters, the smoother the fitted curve (p. 158).
- **Bias–variance trade-off:** a less smooth model protects against misspecification bias but widens confidence intervals; if the smooth model is biased, its nominal 95% interval does not cover the truth 95% of the time (pp. 159–160).
- **Practical stance:** the book mostly assumes models are correct, but careful analysts check sensitivity to specification (p. 160).
- **Bayesian note:** in high-dimensional models, Bayesian credible intervals (the Bayesian analogue of confidence intervals) may trap the true value much less than 95% of the time, because the prior (the investigators' beliefs about the unknown parameters) is not swamped by the data (p. 159).

## L3 — Walkthrough

### Chapter introduction (p. 153)
Part I was conceptual, with hand calculations. Part II needs computers to fit regression models, such as linear and logistic models. The authors assume readers know these models at a basic level. The chapter contrasts the nonparametric estimators of Part I with the parametric (model-based) estimators of Part II. It also reviews smoothing and, briefly, the bias–variance trade-off in any modeling decision. The chapter motivates the need for models whether the goal is causal inference or, say, prediction (p. 153).

### 11.1 Data cannot speak for themselves (pp. 153–154)
**Setting.** 16 HIV-infected individuals are randomly sampled from a large, possibly hypothetical super-population, the target population. Treatment $A$ is antiretroviral therapy and the outcome $Y$ is CD4 cell count. The **estimand** (the unknown population quantity to estimate) is $\mathrm{E}[Y|A=a]$ (p. 153).

An **estimator** is a function of the data used to estimate the estimand. Informally, a **consistent** estimator gets closer to the population value as the sample grows. The sample average within $A=a$ is consistent. The value of the first observation with $A=a$ is not. In practice the authors require all estimators to be consistent (p. 153).

**Three versions of $A$** (Figures 11.1–11.3, p. 154):
- **Dichotomous** ($A\in\{0,1\}$, 8 per group). The sample averages are 146.25 for $A=1$ and 67.50 for $A=0$. Under exchangeability the difference would estimate the average causal effect. The chapter does not pursue causal interpretation (p. 154).
- **Four levels** ($A=1,\dots,4$: none, low, medium, high; 4 per group). The sample averages are 70.0, 80.0, 117.5 and 195.0 (p. 154).
- **Dose in mg/day**, integers 0–100. Many values of $A$ have no individual, e.g. nobody has $A=90$. The group average is undefined there, and for a truly continuous $A$ it would be undefined at nearly all levels (p. 154).

With fewer individuals per category, each category average is still exactly unbiased. But the probability that it is close to the population mean decreases. The 95% confidence intervals will be longer for Figure 11.2 than for Figure 11.1 (p. 154).

**Conclusion:** we cannot always let the data "speak for themselves"; we often must supplement them with a model (p. 154).

*Intuition note:* With 16 people spread over 101 dose levels, most levels are empty. An average of nothing is not a number, so some outside assumption is needed.

### 11.2 Parametric estimators of the conditional mean (pp. 155–156)
**Linear mean model.** Suppose we knew that the mean of $Y$ is a linear function of $A$ over the whole range (p. 155):
$$\mathrm{E}[Y|A]=\theta_0+\theta_1 A$$
- This restricts the shape of the conditional mean function. $\theta_0$ is the value at $A=0$ and $\theta_1$ is the change per unit of $A$.
- $\theta_0,\theta_1$ are the **parameters**. A model that describes the conditional mean with a finite number of parameters is a **parametric conditional mean model** (p. 155).
- Margin note: the authors call the shape restriction the "functional form". They avoid the term "dose-response curve" because it suggests a causal effect, which could be false under confounding (p. 155).

**Two steps** (p. 155):
1. Estimate $\hat\theta_0,\hat\theta_1$.
2. Predict $\widehat{\mathrm{E}}[Y|A=a]=\hat\theta_0+a\hat\theta_1$. The estimate for each individual is the **predicted value**.

**Ordinary least squares (OLS).** For each candidate line, take each dot's vertical distance to the line (the **residual**), square the 16 residuals and sum them. The line with the smallest sum gives the estimates. They are computable by linear algebra, and OLS is an exactly unbiased estimator of $\theta_0,\theta_1$ (p. 155).

**Result for Figure 11.3** (Figure 11.4):
- $\hat\theta_0=24.55$ and $\hat\theta_1=2.14$.
- $\widehat{\mathrm{E}}[Y|A=90]=24.55+90\times2.14=216.9$ (p. 155).
- Margin note: under homoscedasticity (residual variance not depending on $A$) the Wald 95% CIs are $(-21.2,70.3)$ for $\theta_0$, $(1.28,2.99)$ for $\theta_1$ and $(172.1,261.6)$ for $\mathrm{E}[Y|A=90]$ (p. 155).
- OLS uses all points, so $\mathrm{E}[Y|A=a]$ is estimated by borrowing information from individuals with $A\neq a$ (p. 155).

**What a model is.** A model is an a priori restriction on the joint distribution of the data (p. 155). The linear model, for example, forces the mean at $A=90$ to lie between the means at $A=80$ and $A=100$. Through such restrictions a model adds information to compensate for insufficient data (pp. 155–156).

**Not a free lunch.** Parametric estimators can estimate quantities that cannot otherwise be estimated, for example the mean at $A=90$ when no one in the study has it. But inferences are correct only if the model's restrictions are correct (correct specification). Model-based causal inference, which fills much of the rest of the book, therefore relies on (approximately) no model misspecification. Parametric models are rarely, if ever, perfectly specified, so some misspecification is almost always expected. Nonparametric estimators can at least partially rectify this (p. 156).

*Intuition note:* A model is extra information that comes from assumption, not from data. If the assumption is wrong, the answer is wrong, however precise it looks.

### 11.3 Nonparametric estimators of the conditional mean (pp. 156–157)
**Dichotomous $A$ (Figure 11.1).** Fit $\mathrm{E}[Y|A]=\theta_0+\theta_1A$ by least squares. Then $\mathrm{E}[Y|A=0]=\theta_0$ and $\mathrm{E}[Y|A=1]=\theta_0+\theta_1$. The estimates are $\hat\theta_0=67.5$ and $\hat\theta_1=78.75$. So $\widehat{\mathrm{E}}[Y|A=0]=67.5$ and $\widehat{\mathrm{E}}[Y|A=1]=146.25$. These are identical to the sample averages of 11.1, and the author says this is expected, not a coincidence (p. 156).

**Why.** Rewrite the model as $\mathrm{E}[Y|A=1]=\mathrm{E}[Y|A=0]+\theta_1$, with $\theta_1$ negative, positive or zero. This is always true, so the model restricts nothing. By the author's definition it is therefore "not a model" and lets the data speak (p. 156).
- Such "models" with no restriction on the data distribution are **saturated models**, and are ordinarily still called models (p. 156).
- A model is saturated whenever the number of parameters equals the number of unknown conditional means. Two parameters and two means, $\mathrm{E}[Y|A=1]$ and $\mathrm{E}[Y|A=0]$, make it saturated (p. 156).
- Part I ("Causal inference without models") described only saturated models (margin note, p. 156). The author defines "model" as an a priori mathematical restriction on the possible states of nature (Robins and Greenland 1986, cited in the margin).

**Contrast, Figure 11.3.** The same two-parameter linear model must estimate 101 quantities, $\mathrm{E}[Y|A=0],\dots,\mathrm{E}[Y|A=100]$. The only hope for unbiased estimation is to be fortunate enough that all 101 means lie on a straight line. A model with few parameters used for many quantities is **parsimonious** (pp. 156–157).

**Nonparametric estimators** (author's definition) produce estimates from the data with no a priori restriction on the conditional mean function. Examples are the sample average and, equivalently, the saturated model (p. 157).
- With 100 discrete levels and nobody at $A=90$, no nonparametric estimator of $\mathrm{E}[Y|A=90]$ exists (p. 157).
- Part I's methods (standardization, IP weighting, stratification, matching) rested on nonparametric estimators under a saturated model. Most Part II methods use parametric estimators for some part of the data distribution (p. 157).
- Margin: identifiability assumptions are those needed to compute the parameter even with infinite data. Modeling assumptions are the extra ones needed because data are finite (p. 157).

**Fine Point 11.1 (Fisher consistency, p. 157).** The author's "nonparametric estimator" coincides with a Fisher consistent estimator. Computed on the entire population, it gives the true parameter value. Such estimators lack model restrictions and may not exist for many quantities. When they exist, they are the nonparametric maximum likelihood estimators under a saturated model. In the wider literature, "nonparametric" sometimes means estimators with very weak restrictions that are not Fisher consistent, e.g. kernel regression (see Technical Point 11.1).

*Intuition note:* A "model" with as many free numbers as there are groups can always match every group mean, so it assumes nothing. Real modeling starts when there are more things to estimate than parameters.

### 11.4 Smoothing (pp. 157–158)
In the linear model $\theta_1$ is one number, so the difference in mean outcome per unit of $A$ is forced to be constant. That would be wrong if, say, higher doses have increasingly small effects. Linear models can be made more flexible (p. 157).

**Quadratic model:**
$$\mathrm{E}[Y|A]=\theta_0+\theta_1A+\theta_2A^2$$
- It is still a **linear model**, because the mean is a linear combination of covariates ($A$, $A^2$) times parameters, plus an intercept. Margin caution: "linear" means linear in parameters, even if the covariate functions are nonlinear (pp. 157–158).
- When $\theta_2\neq0$ it defines a parabola. $\theta_1$ is the parameter for the linear term and $\theta_2$ for the quadratic term (p. 158).
- OLS on Figure 11.3 (Figure 11.5) gives $\hat\theta_0=-7.41$, $\hat\theta_1=4.11$, $\hat\theta_2=-0.02$.
- $\widehat{\mathrm{E}}[Y|A=90]=\hat\theta_0+90\hat\theta_1+90\times90\,\hat\theta_2=197.1$ (margin: Wald 95% CI $(142.8,251.5)$) (p. 158).

**More terms.** We can add cubic, quartic, … up to a 15th-degree term. Then parameters equal data points (p. 158).
- More parameters generally mean more inflection points, so the curve is more "wiggly" (less smooth).
- A 2-parameter straight line is the smoothest. A model with as many parameters as data points is the least smooth and **interpolates** the data: every point lies on the fitted function (p. 158).

**Smoothing:** modeling can often be viewed as transforming noisy data into more or less smooth curves, because the model borrows information from many data points. All parametric estimators incorporate some smoothing (p. 158).
- The 2-parameter model borrows from all individuals. A model with as many parameters as individuals borrows nothing at observed values of $A$, though it borrows by interpolation at unobserved values (p. 158).
- Intermediate smoothing comes from an intermediate number of parameters, or from restricting which individuals contribute. For example, fit the line only to doses 80–100 (the source calls this a 10-unit window of $A=90$, i.e. within 10 units on either side). A wider window gives more smoothing (p. 158).
- The same reasoning applies to logistic models for dichotomous outcomes (margin note, p. 158) and to many covariates, where the curve becomes a hyperdimensional surface. In general, the fewer the parameters, the smoother the prediction surface (p. 158).

*Intuition note:* Smoothing is the other face of "borrowing information". A stiff curve uses every point to predict each value, so it is stable but may miss real bends. A wiggly curve follows each point and borrows less.

### Fine Point 11.2 (p. 159): model dimensionality and Bayesian vs frequentist intervals
- In frequentist inference probability is frequency. In Bayesian inference it is degree of belief. A Bayesian 95% credible interval means that, given the observed data, "there is a 95% probability that the estimand is in the interval" (p. 159).
- In part because the investigators' degree of belief must be specified, Bayesian inference is less commonly used than frequentist inference (author's statement, p. 159).
- In simple, low-dimensional parametric models with large samples, 95% credible intervals are also 95% confidence intervals. In high-dimensional or nonparametric models a 95% credible interval may trap the estimand much less than 95% of the time (p. 159).
- Underlying reason for these coverage results (author's statement): Bayesian inference needs a prior distribution for all unknown parameters. In low dimensions the data swamp reasonable priors, so inference is insensitive to the prior. In high dimensions this fails. If the true parameter values are unlikely under the prior, the interval's center is pulled away from them toward the values the prior favors most (p. 159).

### 11.5 The bias–variance trade-off (pp. 159–160)
For $\mathrm{E}[Y|A=90]$ the two models give different estimates:

| Model | Estimate | 95% CI |
|---|---|---|
| 2-parameter | 216.9 | (172.1, 261.6) |
| 3-parameter | 197.1 | (142.8, 251.5) |

Which is closer to the truth? (p. 159)
- If the relation is truly curvilinear, the 2-parameter estimate is biased because it assumes a straight line (p. 159).
- If the relation is truly a straight line, both estimates are valid. The 3-parameter model is correctly specified in both cases: $\theta_2=0$ for a line, $\theta_2\neq0$ for a parabola (p. 159).
- So a "safe strategy" is the 3-parameter model, which is less likely to be biased. In general, the more parameters, the fewer the restrictions, and the less smooth the model, the more protection against misspecification bias (p. 159).
- But less smooth models have larger variance, i.e. wider CIs. Here the 3-parameter interval is much wider (p. 159).
- If the 2-parameter estimate is biased, its nominal 95% CI is not calibrated: it does not cover the true $\mathrm{E}[Y|A=90]$ 95% of the time (pp. 159–160).

**Bias–variance trade-off:** investigators must decide whether protection against bias, e.g. via more parameters, is worth the variance cost (p. 160).
- Some formal procedures exist. In practice many decide by tradition, interpretability of parameters and software availability (p. 160).
- The book will usually assume parametric models are correct. The author calls this unrealistic, but it lets the book focus on problems specific to causal analysis (p. 160).
- Careful investigators question their models and run alternative analyses under different specifications compatible with expert knowledge, to assess sensitivity (p. 160).

*Intuition note:* A flexible model gives up precision to avoid being wrong about the shape. A rigid model is precise but may be precisely wrong. No model choice removes both risks.

### Technical Point 11.1: a taxonomy of commonly used models (p. 161)
- **Conditional mean models** have a linear predictor $\sum_{i=0}^{p}\theta_iX_i$ (with $X_0=1$) and a **link function** $g\{\cdot\}$ such that $g\{\mathrm{E}[Y|X]\}=\sum\theta_iX_i$. The text uses the identity link (p. 161).
- **Log link** (for strictly positive outcomes, e.g. counts): $\log\{\mathrm{E}[Y|X]\}=\sum_{i=0}^{p}\theta_iX_i$, so $\mathrm{E}[Y|X]=\exp(\sum\theta_iX_i)$. Predictions are then above zero (p. 161).
- **Logit link** (for 0/1 outcomes): $\log\left\{\frac{\mathrm{E}[Y|X]}{1-\mathrm{E}[Y|X]}\right\}=\sum\theta_iX_i$, so $\mathrm{E}[Y|X]=\operatorname{expit}(\sum\theta_iX_i)$. Predictions lie between 0 and 1. This is **logistic regression**, widely used in the book (p. 161).
- For these canonical links, $\theta$ can be estimated by maximum likelihood under a normal (identity), Poisson (log) or logistic (logit) working model. The estimates are consistent as long as the conditional mean model is correct. GEE models are a further example (p. 161).
- A conditional mean model restricts only $\mathrm{E}[Y|X]$. When $X$ or $Y$ is continuous it is a **semiparametric** model for the joint distribution, because the unrestricted parts cannot be written with a finite number of parameters (p. 161).
- **Generalizations:** *kernel regression* estimates $\mathrm{E}[Y|X=x]$ by $\sum_{i}w_h(x-X_i)Y_i\big/\sum_i w_h(x-X_i)$. Here $w_h$ is a positive kernel function, maximal at 0 and decreasing to 0 as $|z|$ grows, at a rate set by the *bandwidth* $h$. *Generalized additive models* replace $\sum\theta_iX_i$ by $\sum f_i(X_i)$, estimated by a backfitting algorithm (p. 161).
- **Terminology:** kernel regression borrows only from $X$ near $x$ and is called "nonparametric" in the wider literature. This differs from the chapter's usage, where nonparametric estimators use only individuals with $X=x$ exactly (p. 161).

The chapter ends: "We are now ready to describe the use of models for causal inference" (p. 160).

## Toy example (ours, not from the text)
**Part 1: no data at $A=3$.** Four people have $(A,Y)$: $(1,12),(2,18),(4,44),(5,46)$. Nobody has $A=3$, so the group average at $A=3$ is undefined.

Fit $\mathrm{E}[Y|A]=\theta_0+\theta_1A$ by OLS:
- $\bar A=(1+2+4+5)/4=3$ and $\bar Y=(12+18+44+46)/4=30$.
- $\sum(A-3)(Y-30)=(-2)(-18)+(-1)(-12)+(1)(14)+(2)(16)=36+12+14+32=94$.
- $\sum(A-3)^2=4+1+1+4=10$.
- $\hat\theta_1=94/10=9.4$ and $\hat\theta_0=30-9.4\times3=1.8$.
- $\widehat{\mathrm{E}}[Y|A=3]=1.8+3\times9.4=30$.

This number uses information from all four people. It is correct only if the true mean is linear in $A$.

**Part 2: saturated case.** Two groups: $A=0$ with $Y=10,20$ and $A=1$ with $Y=30,50$.
- Group means: 15 and 40.
- OLS: $\bar A=0.5$, $\bar Y=27.5$.
- $\sum(A-0.5)(Y-27.5)=(-0.5)(-17.5)+(-0.5)(-7.5)+(0.5)(2.5)+(0.5)(22.5)=8.75+3.75+1.25+11.25=25$.
- $\sum(A-0.5)^2=1$.
- $\hat\theta_1=25$ and $\hat\theta_0=27.5-25\times0.5=15$.
- Fitted means: $15$ and $15+25=40$, which equal the group averages.

So with two groups the line is saturated and assumes nothing. With a gap in $A$ it is a real restriction.

## Concepts
- [[estimand-estimator]] (new) — estimand is the unknown population quantity; an estimator is a data function used to estimate it (p. 153)
- [[consistent-estimator]] (new) — estimator whose estimates approach the population value as sample size grows (p. 153)
- [[parametric-model]] (new) — a priori restriction on the conditional mean written with finitely many parameters (p. 155)
- [[model-misspecification]] (new) — the model's restrictions are wrong; parametric inferences are then not guaranteed correct (p. 156)
- [[saturated-model]] (new) — as many parameters as unknown conditional means; imposes no restriction, equals sample averages (p. 156)
- [[nonparametric-estimator]] (new) — here: estimates with no a priori restriction on the conditional mean; elsewhere the term can mean weakly restricted estimators (p. 157, p. 161)
- [[ordinary-least-squares]] (new) — chooses the line minimizing the sum of squared residuals (p. 155)
- [[smoothing]] (new) — estimating at $A=a$ by borrowing from individuals with $A\neq a$ (p. 158)
- [[bias-variance-tradeoff]] (new) — protection against misspecification bias costs wider confidence intervals (p. 159)
- [[identifiability-vs-modeling-assumptions]] (new) — identifiability assumptions hold even with infinite data; modeling assumptions are needed because data are finite (p. 157)
- [[link-function]] (new) — $g$ with $g\{\mathrm{E}[Y|X]\}=\sum\theta_iX_i$ (p. 161)
- [[frequentist-vs-bayesian-inference]] — probability as frequency vs degree of belief (p. 159)
- [[credible-interval]] — Bayesian interval with stated posterior probability of containing the estimand (p. 159)
- [[prior-distribution]] — prior over all unknown parameters, required by Bayesian inference (p. 159)

## Canonical instances
- [[hiv-cd4-16-individuals]] — 16 people with dose $A$ and CD4 outcome $Y$; shows group averages failing as $A$ gains levels (p. 154)
- [[linear-vs-quadratic-fit-at-A90]] — estimates 216.9 vs 197.1 at $A=90$ with different CI widths; shows the bias–variance trade-off (p. 159)

## Bridges (candidates)
- [structural-analogy] Smoothing as borrowing information across values of $A$ ↔ bayesian: partial pooling/shrinkage, which also borrows information across units. The mechanisms differ.
- [structural-analogy] Bias–variance trade-off in choosing the number of parameters ↔ bayesian: Bayesian Occam's razor and cross-validation for model choice.
- [structural-analogy] Credible interval vs confidence interval in Fine Point 11.2 ↔ bayesian: credible intervals (probability as degree of belief) vs confidence intervals (probability as frequency). The definitions of probability differ, and coverage can differ in high dimensions.
- [structural-analogy] Model as a priori restriction adding information ↔ bayesian: the prior distribution adding information. Fine Point 11.2 links priors to high-dimensional sensitivity.

## Questions this raises
- How do formal procedures for choosing the number of parameters (p. 160) quantify the bias–variance trade-off?
- How large a bandwidth or model dimension is safe before a Bayesian credible interval stops matching confidence-interval coverage (p. 159)?
- If the difference between group means is given a causal reading under exchangeability (p. 154), how does model misspecification combine with confounding?
- How can sensitivity analysis over "compatible" model specifications (p. 160) be made systematic?

## Reading notes
- Printed page = pdf − 9 (pdf 162–171 = printed 153–162). Printed 162 has only the running header.
- Per the unit metadata, the source is the online revision dated 2026-08-19, not the 2020 print edition. Chapter numbering may differ from older citations.
- Arithmetic in the source rounds: $24.55+90\times2.14=217.15$ but the text prints 216.9. Likewise $-7.41+90\times4.11+8100\times(-0.02)\approx200.5$ but the text prints 197.1. The printed parameters are shown to few digits (e.g. $\hat\theta_2=-0.02$), which may explain the gap; I report the author's printed estimates.
- Technical Point 11.1: the first sentence writes the predictor with $i=0$ to $p$, but the link equation $g\{\mathrm{E}[Y|X]\}$ shows the sum from $i=1$. This looks like a misprint. The log and logit formulas use $i=0$.
- The scatter plots (Figures 11.1–11.5) show dots only; I did not read individual values from them.
- The chapter contains no exercises. The R/SAS/Stata/Python code is referenced only by margin notes (Programs 11.1–11.3).
