---
id: hernan-2020-whatif/ch18-variable
work: hernan-2020-whatif
unit: "18 Variable selection and high-dimensional data"
pages: 241-252
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
# Variable selection and high-dimensional data

## L0 — One line
Choosing adjustment variables for a causal effect needs subject-matter knowledge, not just prediction algorithms; once a sound set is chosen, doubly robust estimators with sample splitting and cross-fitting let machine learning handle high-dimensional adjustment, and under stated conditions the confidence intervals stay valid.

## L1 — The gist (≤ 120 words)
Which variables should we adjust for? For pure prediction, the aim is to use variables that improve accuracy, and no confounder question arises. For causal effects, some variables (colliders, mediators, instruments) induce or amplify bias, and data alone cannot identify them. So expert knowledge must screen the variables first. Then the problem becomes estimating the effect when the covariates are high-dimensional. Flexible machine learning predicts well, but plugging it into IP weighting or the plug-in g-formula generally cannot give valid Wald confidence intervals. Doubly robust estimators combined with sample splitting and cross-fitting can give valid intervals under conditions. Even so, subject-knowledge gaps, computing costs and large variance may remain.

**Prerequisites:** g-formula and IP weighting; causal DAGs with colliders; conditional exchangeability; confidence intervals; conditional expectation.

## L2 — Key ideas
- Prediction needs no adjustment for confounding, because confounding is a causal concept. Causal analysis needs a thoughtful choice of confounders. (p. 241–242)
- Adjusting for a collider, or a descendant of one, can create selection bias, even under the null (Figures 18.1, 18.2). (p. 243)
- Adjusting for a mediator blocks part of the effect. A noncollider affected by treatment can also bias the estimate. Yet a post-treatment variable may be valid to adjust for, as in Figure 18.5. (p. 244–245)
- Data alone cannot distinguish a confounder from a collider, so subject-matter knowledge must guide the adjustment set. (p. 245)
- Adjusting for an instrument may amplify bias from an unmeasured confounder. Amplification is not guaranteed. (p. 246)
- With high-dimensional covariates, ML-based doubly robust estimators (built from two fitted functions: the outcome mean $b(X)$ and the treatment probability $\pi(X)$) have bias that depends on a product of two errors. IP weighting and the plug-in g-formula do not. (p. 247–248)
- Sample splitting (fit $b$ and $\pi$ on one random half, estimate the effect on the other half) makes these fitted functions (the "nuisance" estimates) independent of the estimation sample. Cross-fitting regains the lost efficiency. (p. 248–249)
- Under conditions (i) the fitted $b,\pi$ are consistent and (ii) the conditional bias divided by the standard error tends to 0, the cross-fit AIPW (augmented IP weighted) estimator is asymptotically normal and unbiased, and its Wald intervals (estimate $\pm1.96$ standard errors) are valid. (p. 250)
- The tension between bias and variance remains. Discarding covariates after seeing the data breaks the guarantee of valid intervals. (p. 250–251)

## L3 — Walkthrough

### Opening (p. 241)
All adjustment methods (stratification and outcome regression, standardization and g-formula, IP weighting, g-estimation) rely on one condition. The set $L$ must carry enough information for conditional exchangeability, or equivalently must block all backdoor paths without opening other biasing paths (p. 241). Variable-selection criteria for causal inference differ from those for prediction. Common predictive procedures may therefore not transfer to causal analyses (p. 241).

### 18.1 The different goals of variable selection (pp. 241–242)
- For a purely predictive goal, no adjustment for confounding is needed, because "confounding" does not apply when the estimand is an association (p. 241). To quantify the association of smoking cessation with weight gain, one compares average weight gain between quitters and non-quitters (p. 241).
- In a predictive model all covariates have the same status. There is no $A$ versus $L$, and parameters need not have causal meaning. Example: prior hospitalization may predict heart failure, but nobody would stop admitting patients to prevent it (p. 241).
- Prediction algorithms have tuning parameters. The lasso and ridge regression have a regularization parameter that shrinks coefficients toward zero. Neural nets have depth and width. These are often chosen by cross-validation, which also compares algorithms, because no single algorithm is best in all data sets (p. 242).
- Black-box procedures are not always easy to explain. Two views are reported:
  - **One view:** for pure prediction in a given setting, whatever improves prediction is fair game (p. 242).
  - **Other view:** interpretable algorithms are needed. Physicians will not feel comfortable with treatment decisions whose medical reasons they cannot articulate to themselves and the patient. Black-box algorithms may perform poorly in new settings because they rely on local, often noncausal features. They may also bake in discriminatory practices present in the training data (p. 242).
- Causal analysis needs thoughtful confounder selection. Automatic selection may work for prediction but not generally for causal inference, because it may select variables that introduce bias (p. 242).

**Intuition note.** A predictor is useful if it helps guess $Y$, even if it is not a cause. A confounder is defined relative to a treatment–outcome question. The same algorithm can therefore work for one goal but not generally for the other.

#### Fine Point 18.1: selection in regression (p. 243)
When there are too many predictors, one can select a subset or shrink.
- **Best subset:** fix the number of variables, fit all combinations, and choose by a criterion such as Akaike's. This is computationally infeasible for many variables and, in a finite data set, not guaranteed to give the smallest prediction error.
- **Greedy methods:** forward selection, backward elimination and stepwise selection. They are easy but do not explore all subsets.
- **Shrinkage:** a penalty pushes estimates (other than the intercept) toward zero. This lowers variance and stabilizes prediction. Ridge regression and the lasso are the best known. Unlike ridge, the lasso can set some parameters exactly to zero, so it is both shrinkage and subset selection.

#### Fine Point 18.2: overfitting and cross-validation (p. 244)
- **Overfitting:** variables are chosen to predict the observed data well, including random variation. The model then predicts poorly for new individuals.
- **Training/validation split:** with sample size $n$, use $v$ individuals for validation and $n-v$ for training. The downside is higher variance, because only a subset is used for estimation.
- **Cross-validation:** repeat the split many times and average accuracy over the validation samples.
- **Leave-$v$-out:** use all partitions. This may become computationally infeasible for moderately large $n$ and $v$. Two possible fixes are to choose $v=1$ or to evaluate only a sample of partitions.
- **$k$-fold:** split into $k$ equal parts, and use each in turn as validation. A common choice is $k=10$.
- The text notes that deep networks with huge training data often seem nearly immune to overfitting even though they fit training data exactly. It calls explaining this an active research area.

### 18.2 Variables that induce or amplify bias (pp. 242–246)
**Setting.** Imagine unlimited computing power and a quasi-infinite sample, with $A$, $Y$ and a moderate number of discrete $X$. For pure prediction under least squares loss, the best predictor is the mean of $Y$ in each joint stratum of $A$ and $X$ (p. 242). For the causal effect $E[Y^{a=1}]-E[Y^{a=0}]$, the goal is to remove as much confounding as possible using $X$. Even here the authors say there are reasons to adjust for only a subset of $X$, namely that adjusting for some variables induces bias (p. 243).

**Colliders (Figure 18.1: $A\to L\leftarrow U\to Y$).**
- The causal effect is $0$, and $E[Y|A=1]-E[Y|A=0]$ is unbiased because there is no confounding by $L$ (p. 243).
- Adjusting for $L$ with the g-formula gives
$$\sum_l E[Y|A=1,L=l]\Pr(L=l)-\sum_l E[Y|A=0,L=l]\Pr(L=l).$$
- This differs from the unadjusted contrast, and so is biased. The reason is that $L$ is conditionally associated with $Y$ given $A$ and marginally associated with $A$, so $\Pr(L=l)\neq\Pr(L=l|A)$ (p. 243).
- The adjusted $A$–$Y$ association is expected to be non-null although the effect is null. This is **selection bias under the null** (p. 243).
- The same bias is expected when adjusting for a descendant of a collider (Figure 18.2: $A\to B\to L$, $U\to B$, $U\to Y$; $B$ is the collider, $L$ its descendant) (pp. 243–244).

**Noncollider affected by treatment (Figure 18.3: $A\to Y\to L$).**
- The effect $E[Y^{a=1}]-E[Y^{a=0}]\neq0$ is unbiasedly estimated by the unadjusted contrast. Adjusting for $L$ as if it were pre-treatment gives a contrast that differs from it, "for the same reasons" (p. 244).
- If the arrow $A\to Y$ were absent, $A$ and $Y$ would be independent marginally and given $L$, and the adjusted contrast would be $0$ and unbiased. Under the null $A$ no longer affects $L$.
- Hence, unlike Figures 18.1 and 18.2, adjusting for $L$ here causes bias only when $A$ has a non-null effect on $Y$. This is **selection bias under the alternative** (off the null) (p. 244).

**Mediators (Figure 18.4: $A\to L\to Y$ and $A\to Y$).**
- Adjusting for a mediator or its descendants blocks the part of the effect that goes through $L$. The adjusted association then differs from the effect of $A$. This is **overadjustment for mediators** when the average causal effect is the contrast of interest (p. 245).
- Margin note: this adjusted association is biased for the total effect but unbiased for the direct effect not mediated through $L$ (p. 245).

**Post-treatment variables.**
- The bias-inducing variables above are all affected by treatment. One might think we should never adjust for post-treatment variables. That rule would be easy to follow, but it may exclude useful variables (p. 245).
- In Figure 18.5 ($U\to A$, $U\to L$, $L\to Y$), $L$ is post-treatment but blocks the backdoor path. Adjusting for it gives an unbiased estimate, and the unadjusted association is biased (p. 245).
- The authors say "causal graphs do not care about temporal order". When $A$ does not affect $L$, the correct analysis is the same whether $L$ is before or after $A$ (p. 245).
- Even with known temporal order, data cannot show whether $A$ affects $L$. For order $A, L, Y$, any joint distribution without independencies fits several causal graphs. So the decision cannot come from automated procedures based only on statistical associations. As in Chapter 7, collider and confounder cannot be told apart from data alone. Subject-matter knowledge must guide exclusion (p. 245).

**Pre-treatment variables (order $L, A, Y$).**
- Take a very large sample, so variance is negligible and only bias matters. It is commonly believed that adjusting for all pre-treatment covariates minimizes bias. The authors say this is wrong for two separate reasons (p. 245).
- *Reason 1: M-bias.* In Figure 18.6 ($U_1\to L$, $U_1\to Y$, $U_2\to L$, $U_2\to A$, $A\to Y$), $L$ is a collider on a path from $A$ to $Y$. Adjusting for it introduces selection bias (M-bias, Chapter 7). If there were also an arrow $L\to A$, $L$ would be both confounder and collider. Then the effect cannot be identified, whether or not one adjusts for $L$ (p. 245).
- *Reason 2: bias amplification.* In Figure 18.7 ($Z\to A\to Y$, $U\to A$, $U\to Y$), $U$ is unmeasured. $Z$ is not on any backdoor path, so it is an instrument and useless for g-formula adjustment (p. 246).
- Adjusting for $Z$ may nonetheless amplify the confounding bias from $U$. The adjusted $A$–$Y$ association may be further from the effect than the unadjusted one. This is **Z-bias**, a reason to avoid adjusting for instruments (p. 246).
- Margin note: amplification is guaranteed if all structural equations are linear (Wooldridge 2010, Pearl 2011), but may also occur in more realistic settings (Ding et al. 2017) (p. 246).
- Amplification is not guaranteed. Adjusting for $Z$ could also reduce the bias. Generally one cannot know which (p. 246).

**Summary.** Even with unlimited computing and sample size, it is not advisable to adjust for all of $X$. Bias-inducing variables cannot be identified by purely statistical algorithms, so expert knowledge is needed (p. 246).

**Intuition note.** Adding a variable to the adjustment set is not free. Conditioning on a common effect of $A$ and $Y$-related causes creates a spurious link. Conditioning on a variable that only drives treatment (an instrument) may make the leftover unmeasured confounding matter more, though this is not guaranteed.

### 18.3 Causal inference and machine learning (pp. 246–247)
- **Assumptions from here on:** $X$ contains no bias-inducing or amplifying variables, includes all confounders, and positivity holds. The remaining problem is estimating $E[Y^{a=1}]-E[Y^{a=0}]$ when $X$ is high-dimensional or has many continuous variables (p. 246). Good estimates of $E[Y^{a=1}]$ and $E[Y^{a=0}]$ give a good estimate of their difference, so the text focuses on $E[Y^{a=1}]$ (p. 246).
- **Two nuisance functions.** The plug-in g-formula needs $b(X)$, the mean of $Y$ given $X$ among $A=1$. IP weighting needs $\pi(X)$, the probability of treatment given $X$ (p. 246). Traditional parametric models with far fewer parameters than $n$ are certain to be misspecified when $X$ is high-dimensional. Then $\hat b(x)$ and $\hat\pi(x)$ are not consistent for $b(x)$ and $\pi(x)$ (pp. 246–247).
- **Richer models.** Use a linear predictor $\theta^Ts(x)=\sum_j\theta_js_j(x)$, where $s(X)$ is a very high-dimensional vector of transformations (e.g., cubic splines) and cross-products. With a logit link, $\hat b(x)=\mathrm{expit}(\hat\theta_b^Ts(x))$ and $\hat\pi(x)=\mathrm{expit}(\hat\theta_\pi^Ts(x))$. Even if consistent, finite-sample errors are much greater than for a correctly specified low-dimensional model. If $\dim s(X)>n$, the fit does not converge (p. 247).
- **Ways forward:** lasso or ridge penalties, stepwise selection, or ML such as random forests or neural nets. In most cases with large $n$ and many covariates, ML outperforms traditional parametric models for predicting conditional expectations (p. 247).
- **But** ML does not by itself suffice for confounding adjustment. It must be used with doubly robust estimators plus sample splitting and cross-fitting. This is necessary to build valid 95% Wald intervals, i.e., intervals that trap the parameter at least 95% of the time (p. 247).

### 18.4 Doubly robust machine learning estimators (pp. 247–250)
**Condition for valid Wald intervals for $\psi=E[Y^{a=1}]$ (p. 247).**
- The bias must be much less than the standard error. For most estimators the standard error scales as $1/\sqrt n$, so the bias must be much less than $1/\sqrt n$.
- The estimator must also generally be asymptotically normal, which is generally easier than small bias.

**Why doubly robust.**
- The bias of a doubly robust estimator depends on the product of the errors $\frac1{\pi(x)}-\frac1{\hat\pi(x)}$ and $b(x)-\hat b(x)$ (p. 247).
- The bias is less than $1/\sqrt n$ if both errors are much smaller than $1/\sqrt[4]{n}$. ML can often achieve this if $\pi(x)$ and $b(x)$ are quite smooth or very sparse, even if the relevant components are unknown (pp. 247–248).
- By contrast, IP weighted and plug-in g-formula estimators can have bias as large as $\frac1{\pi(x)}-\frac1{\hat\pi(x)}$ and $b(x)-\hat b(x)$, respectively. The text says that with high-dimensional $X$ the error of any estimator of $\pi$ or $b$ is known to exceed $1/\sqrt n$. So neither can generally center a valid Wald interval (p. 248).
- This is "second-order bias" (margin note, p. 248).

**Sample splitting (p. 248).**
1. Randomly split $n$ individuals into an estimation sample of size $n/2$ and an equal-sized training sample (the "nuisance sample").
2. Apply ML on the training sample to get $\hat b(x)$ and $\hat\pi(x)$, for $b(x)=E[Y|X=x,A=1]$ and $\pi(x)=E[A|X=x]$.
3. Compute the doubly robust estimator in the estimation sample, using those fitted functions.

**Why split.**
- The full-sample AIPW estimator is
$$\frac1n\sum_{i=1}^n\Big[\hat b(X_i)+\frac{A_i}{\hat\pi(X_i)}\{Y_i-\hat b(X_i)\}\Big],$$
with $\hat b,\hat\pi$ fitted on all $n$ individuals. They are then correlated with the estimator. If large, this correlation can affect bias, variance and normality in unpredictable ways. Its size is unknown and cannot be well estimated (p. 248).
- In the split-sample version the estimation sample is independent of $\hat b,\hat\pi$. Under weak conditions (Technical Point 18.2) the estimator is asymptotically normal with standard error scaling as $1/\sqrt n$. If the product bias is less than $1/\sqrt n$, Wald intervals centered on it are valid (p. 248).
- The split-sample estimator is therefore much preferred in high-dimensional settings. Its drawback is that its variance corresponds to a sample size of $n/2$, so the interval is wider (p. 248).

**Cross-fitting (p. 249).** Swap the roles of the two halves, get a second estimate, and average the two. This average is the estimate for the whole population. A 95% interval comes from the bootstrap, either as estimate $\pm1.96\times$ bootstrap standard error or from the 2.5 and 97.5 percentiles (p. 249). Doubly robust estimation plus ML then yields estimates with known statistical properties that use all the data (p. 249).

**Intuition note.** Splitting stops the model from "grading its own homework". The nuisance fits never see the data used to evaluate the effect. Swapping halves recovers the data that splitting threw away.

#### Technical Point 18.1: AIPW split-sample and cross-fit estimator (p. 249)
(i) Randomly split into an estimation sample of size $q$ and a training sample of size $n_{tr}=n-q$, with $q/n\approx1/2$.
(ii) Estimate $\hat b(x)$ of $b(x)=E[Y|A=1,X=x]$ and $\hat\pi(x)$ of $\pi(x)=\Pr[A=1|X=x]$ from the training sample by ML.
(iii) Compute from the $q$ estimation subjects
$$\hat\psi=\frac1q\sum_{i=1}^q\Big[\hat b(X_i)+\frac{A_i}{\hat\pi(X_i)}\{Y_i-\hat b(X_i)\}\Big].$$
(iv) Compute
$$\hat\psi_{\text{cross-fit}}=\big(\hat\psi+\bar{\hat\psi}\big)/2,$$
where $\bar{\hat\psi}$ is $\hat\psi$ with training and estimation samples swapped.

Alternative with better finite-sample behavior: split into $M>2$ equal random samples. Compute $\hat\psi^{(m)}$ using sample $m$ as estimation sample and the other $M-1$ as training sample. Then $\hat\psi_{\text{cross-fit}}=\frac1M\sum_{m=1}^M\hat\psi^{(m)}$.

#### Technical Point 18.2: statistical properties (p. 250)
- Conditional on the training data $T_r$, $\hat b,\hat\pi$ are fixed functions. So $\hat\psi$ is a sum of i.i.d. terms and, by the central limit theorem, is asymptotically normal given $T_r$, with standard error proportional to $n^{-1/2}$.
- The exact conditional bias is
$$E[\hat\psi-\psi|T_r]=E\Big[\pi(X_i)\Big(\frac1{\hat\pi(X_i)}-\frac1{\pi(X_i)}\Big)\{b(X)-\hat b(X)\}\,\Big|\,T_r\Big].$$
- This bias is random through its dependence on the training data. **If** (i) $\hat b,\hat\pi$ are consistent (in mean square) for $b,\pi$, **and** (ii) $E[\hat\psi-\psi|T_r]/se(\hat\psi)\to0$ in probability, **then** $\hat\psi$ and $\hat\psi_{\text{cross-fit}}$ are asymptotically normal and unbiased.
- Then 95% Wald intervals $\hat\psi\pm1.96\,\widehat{se}(\hat\psi)$ and $\hat\psi_{\text{cross-fit}}\pm1.96\,\widehat{se}(\hat\psi_{\text{cross-fit}})$ are valid and calibrated. The standard errors can be computed by bootstrap.
- $n^{1/2}\widehat{se}(\hat\psi_{\text{cross-fit}})$ is semiparametric efficient, with standard error $\{\mathrm{var}\{b(X)+\frac{A}{\pi(X)}[Y-b(X)]\}\}^{1/2}$. This is smaller than that of $\hat\psi$ by a factor of $1/\sqrt2$.
- If $\frac1{\hat\pi}-\frac1\pi$ converges at rate $n^{-\alpha}$ and $b-\hat b$ at rate $n^{-\epsilon}$, the bias is $o(n^{-1/2})$ if $\alpha+\epsilon>1/2$. So $\hat b$ may converge more slowly than $n^{-1/4}$ if $\hat\pi$ converges fast enough, and the reverse also holds.

### 18.5 Variable selection is a difficult problem (pp. 250–251)
- The methods above contradict the widespread belief that any data-adaptive selection of adjustment variables inevitably gives incorrect confidence intervals. Combined with ML, causal methods can under certain conditions give correct inference (p. 250). But doubly robust ML does not solve everything, for at least three reasons (p. 250):
  1. Subject-matter knowledge may be insufficient to find all important confounders or to rule out bias-inducing variables, so a small bias is not guaranteed.
  2. Doubly robust estimators are difficult and expensive to implement with ML in high-dimensional settings with time-varying treatments, especially causal survival analysis. Most published longitudinal examples use single robust estimators. The methods of this chapter are quickly becoming routine in some fields.
  3. The variance can match what one would get if $b(X)$ and $\pi(X)$ were known, but nothing guarantees it is small enough to be useful.
- **Variance problem.** If some covariates are strongly associated with $A$, $\pi(X)$ may be near $0$ or $1$ for some $X$ values. The estimate then has a very large variance and a very wide, often correct, interval (p. 251).
- **The temptation.** Throw out those covariates and repeat. Using the data to discard covariates associated with treatment but not much with outcome means the validity of the 95% interval can no longer be guaranteed. The tension between including all confounders (to remove bias) and excluding variables (to cut variance) is hard to resolve (p. 251).
- Margin question: if the interval is invalid after data-driven removal of 5 variables, why is it valid had we happened to receive a data set without them? Given that we always work with data sets in which some potential confounders are not recorded, how should we interpret confidence intervals in any observational analysis? (p. 251).
- Clear general guidelines may not be possible. The authors say the best scientific advice may be to carry out multiple sensitivity analyses (Section 13.5): run several methods. If estimates agree, confidence rises. If not, try to understand why (p. 251).

## Toy example (ours, not from the text)
Collider selection bias (Figure 18.1 structure). Let $U$ and $A$ be independent fair binary variables. Let $Y=U$, so $A$ has no effect on $Y$ and the true effect is $0$. Let $L$ depend on both: $\Pr(L=1|A,U)$ is $0.1$ for $(0,0)$, $0.5$ for $(0,1)$, $0.5$ for $(1,0)$ and $0.9$ for $(1,1)$.

Joint probabilities $\Pr(A,U,L)=0.25\cdot\Pr(L|A,U)$:

| $A$ | $U$ | $L=1$ | $L=0$ |
|---|---|---|---|
| 1 | 0 | .125 | .125 |
| 1 | 1 | .225 | .025 |
| 0 | 0 | .025 | .225 |
| 0 | 1 | .125 | .125 |

The eight cells sum to 1.

- Unadjusted: $E[Y|A=1]=(.225+.025)/.5=0.5$ and $E[Y|A=0]=(.125+.125)/.5=0.5$. The difference is $0$, which is correct.
- Stratum means:
  - $E[Y|A=1,L=1]=.225/.35=9/14$.
  - $E[Y|A=1,L=0]=.025/.15=1/6$.
  - $E[Y|A=0,L=1]=.125/.15=5/6$.
  - $E[Y|A=0,L=0]=.125/.35=5/14$.
- $\Pr(L=1)=.125+.225+.025+.125=.5$, so $\Pr(L=0)=.5$.
- g-formula for $A=1$: $.5\cdot\frac9{14}+.5\cdot\frac16=\frac{17}{42}\approx0.405$. For $A=0$: $.5\cdot\frac56+.5\cdot\frac5{14}=\frac{25}{42}\approx0.595$.
- Adjusted contrast $=-8/42\approx-0.19\neq0$, although the true effect is $0$. Adjusting for the collider $L$ created the bias.

Cross-fitting arithmetic (ours): if $\hat\psi=0.52$ on one half and $\bar{\hat\psi}=0.48$ on the swapped half, then $\hat\psi_{\text{cross-fit}}=(0.52+0.48)/2=0.50$.

## Concepts
- [[confounding-vs-selection-bias]] — confounding from common causes versus selection bias from adjusting for common effects. The chapter shows adjustment can create the second. (p. 243)
- [[fork-chain-collider]] — adjusting for a collider (Fig. 18.1), a descendant of one (Fig. 18.2), or a collider that is pre-treatment (Fig. 18.6, M-bias) induces bias. (p. 243, 245)
- [[causal-dag]] — graphs used to decide adjustment sets; the text says they ignore temporal order. (p. 245)
- [[assignment-mechanism-ignorability]] — here "conditional exchangeability", which $L$ must achieve. (p. 241)
- [[propensity-score]] — $\pi(X)=E[A|X]$, a nuisance function for IP weighting and AIPW; the text also calls it the propensity score. (p. 246, 251)
- [[cross-validation-loo-waic]] — repeated training/validation splitting to estimate out-of-sample prediction accuracy; the chapter covers leave-$v$-out and $k$-fold only. (p. 244)
- [[prediction-vs-causal-selection]] (new) — predictive selection keeps what improves accuracy; causal selection needs a confounder choice guided by structure. (p. 241–242)
- [[overfitting]] (new) — fitting random variation, so the model predicts well on training data and poorly on new individuals. (p. 244)
- [[lasso-ridge-shrinkage]] (new) — penalties pulling coefficients toward zero; the lasso can set some exactly to zero. This is not the hierarchical-model shrinkage of the canon. (p. 243)
- [[overadjustment-for-mediators]] (new) — adjusting for a mediator blocks part of the total effect. (p. 245)
- [[bias-amplification-z-bias]] (new) — adjusting for an instrument may increase confounding bias from an unmeasured $U$; not guaranteed. (p. 246)
- [[doubly-robust-aipw]] (new) — an estimator using $b(X)$ and $\pi(X)$ whose bias depends on the product of their errors. (p. 247–248)
- [[sample-splitting-cross-fitting]] (new) — fit nuisance functions on one half, estimate on the other, swap, and average. (p. 248–249)
- [[wald-interval]] (new) — estimate $\pm1.96$ standard errors; valid only if bias is much smaller than the standard error. (p. 247, 250)

## Canonical instances
- [[collider-selection-bias-fig-18-1]] — adjusting for $L$ with $A\to L\leftarrow U\to Y$ produces a non-null association under the null. (p. 243)
- [[m-bias-fig-18-6]] — a pre-treatment collider $L$; adjusting for it introduces bias. (p. 245)
- [[z-bias-instrument-fig-18-7]] — adjusting for instrument $Z$ may amplify confounding by $U$. (p. 246)
- [[post-treatment-adjustment-fig-18-5]] — a post-treatment $L$ that is valid to adjust for. (p. 245)
- [[k-fold-cross-validation]] — split into $k$ parts, each used once for validation; $k=10$ is common. (p. 244)

## Bridges (candidates)
- [structural-analogy] Lasso/ridge penalty (p. 243) ↔ Bayesian inference: priors that pull coefficients toward zero — both stabilize estimates by trading variance against bias.
- [same-math] Conditioning on a collider (p. 243) ↔ Causal DAG: collider path opening — the same phenomenon, discussed under d-separation and fork/chain/collider.
- [structural-analogy] $k$-fold cross-validation (p. 244) ↔ Bayesian model checking: LOO-type estimates of out-of-sample accuracy — both estimate predictive accuracy without overfitting.
- [metaphor] Discarding covariates after seeing the data (p. 251) ↔ Bayesian workflow: iterating model changes after looking at the data — both raise the question of what the final inference is conditional on.

## Questions this raises
- How can subject-matter knowledge be turned into a defensible adjustment set when the DAG is itself uncertain?
- The margin note asks why a confidence interval is valid for a data set lacking 5 variables but not after dropping them. What would a principled answer look like?
- When $\pi(X)$ is near 0 or 1, is the wide interval a problem with the method or an honest report that the data hold little information?
- How could one detect, in practice, whether the bias of a split-sample estimator is of the order of its standard error (an open research area per p. 249)?

## Reading notes
- Page offset: printed = pdf − 9 (pdf 250 = printed 241). Printed numbers are used throughout. Printed p. 252 is blank except for the running header.
- According to the unit metadata (not visible on the page images), the source is the online revision dated 2026-08-19, not the 2020 print version, so chapter numbering may differ from older citations.
- Page 242 refers to "Technical Point 18.1" for least squares loss, but Technical Point 18.1 on p. 249 concerns the AIPW estimator. This looks like a misreference.
- Section 18.3 cites "Fine Point 18.1" for lasso and ridge, which matches p. 243. The cross-validation reference to Fine Point 18.2 also matches p. 244.
- The text layer is garbled in places. Equations in the Technical Points, and the symbols $\hat b,\hat\pi$, were checked against the page images.
- Minor typos in the source: "ealier" (p. 248); the Fine Point 18.2 sentence ending "related techniques" has no full stop (p. 244).
- The chapter has no exercises.
- Several statements are given as the authors' claims without proof here (e.g., the lower bound of $1/\sqrt n$ on estimator error, p. 248). They are reported as stated.
