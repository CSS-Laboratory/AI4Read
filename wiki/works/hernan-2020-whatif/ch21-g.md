---
id: hernan-2020-whatif/ch21-g
work: hernan-2020-whatif
unit: "21 G-methods for time-varying treatments"
pages: 277–304
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# G-methods for time-varying treatments

## L0 — One line
With treatment-confounder feedback, the g-formula, IP weighting and g-estimation (and their doubly robust versions) can give correct effects for sustained treatment strategies under sequential exchangeability, positivity and consistency, where traditional adjustment fails.

## L1 — The gist (≤ 120 words)
The previous chapter showed that traditional methods of confounding adjustment gave estimates different from the null even though treatment had zero effect, in a dataset with treatment-confounder feedback (confounders affected by past treatment). This chapter applies the three g-methods to the same two-time-point dataset. The g-formula (standardization conditional on history), IP weighting (weights built from the probability of the observed treatment history) and g-estimation (structural nested models) all give the correct null answer (both means equal 60). The chapter then covers estimation with many time points, model misspecification, doubly robust estimators, censoring as a time-varying treatment, and the "big g-formula" that links other identification formulas, such as the front door formula, to the g-formula.

**Prerequisites:** conditional expectation; standardization and IP weighting for time-fixed treatment (Ch. 12–15); sequential exchangeability, positivity, consistency (Ch. 19–20); logistic and linear regression; d-separation.

## L2 — Key ideas (5–10 bullets)
- For a time-varying treatment, the g-formula standardizes over confounders, with every factor conditioned on past treatment and covariate history. In Table 21.1 it gives 60 for both "always" and "never" treat (p. 278).
- IP weights multiply one factor per time point. IP weighting and the g-formula give identical numbers in the nonparametric example, even when identifiability fails, so the equality is not causal (p. 282–283).
- Parametric g-formula and parametric IP weighting rely on different models. A difference beyond sampling variability shows that at least one set of models is misspecified, so both should be run (p. 284). If treatment has no effect on anyone (the sharp null) and there is treatment-confounder feedback, standard non-saturated parametric g-formula models cannot all be correct (the "g-null paradox"), so the null might theoretically be falsely rejected; IP weighting of marginal structural mean models and g-estimation of structural nested mean models do not suffer this (p. 286).
- A marginal structural mean model (a model for mean counterfactual outcomes under many strategies) such as $E[Y^{\bar a}]=\beta_0+\beta_1 cum(\bar a)$ pools information across strategies and is fit by weighted least squares. Stabilized weights (numerator $f(A_k|\bar A_{k-1})$ instead of 1) are preferred for non-saturated models, but cannot be used for dynamic strategies (pp. 284–285).
- Doubly robust estimators (iterated conditional expectation, ICE, i.e. sequential regressions from the last time backwards, with the IP weight as a covariate) are consistent if all the treatment models or all the outcome models are right. They are in fact $K+2$ robust (also unbiased if the treatment models are right up to some time $m$ and the outcome models after it), and variants reach $2^{K+1}$ robustness (pp. 286–289).
- G-estimation of structural nested mean models (models for the effect of a last blip of treatment given history) searches for the parameter value that makes the "blipped-down" outcome $H_k(\psi^\dagger)$ (the observed outcome with the modelled effect of treatment from time $k$ onward removed) unassociated with treatment given history. These models can allow effect modification by past covariates. If one instead assumes none and that is wrong, g-estimates are biased while IP weighted marginal structural model estimates stay unbiased; g-estimation is more efficient when the assumption holds (pp. 289–295).
- Censoring is a time-varying treatment, handled by extra IP weights (pp. 297–299).
- The "big g-formula" uses all variables, measured or not. Other identifying formulas are mathematically linked to it; for example, under the front door criterion it reduces to the front door formula, which uses observed variables only (pp. 300–301).

## L3 — Walkthrough

### Introduction (p. 277)
- The chapter uses the dataset of Table 21.1 (from Table 20.1; sequentially randomized experiment). It shows that the three g-methods give the correct null effect (p. 277).
- Static strategies are compared under sequential exchangeability, positivity and consistency from Chapter 19 (p. 277).

**Table 21.1** (columns $A_0, L_1, A_1$, N, mean Y) (p. 277):

| $A_0$ | $L_1$ | $A_1$ | N | Mean Y |
|---|---|---|---|---|
| 0 | 0 | 0 | 2400 | 84 |
| 0 | 0 | 1 | 1600 | 84 |
| 0 | 1 | 0 | 2400 | 52 |
| 0 | 1 | 1 | 9600 | 52 |
| 1 | 0 | 0 | 4800 | 76 |
| 1 | 0 | 1 | 3200 | 76 |
| 1 | 1 | 0 | 1600 | 44 |
| 1 | 1 | 1 | 6400 | 44 |

### 21.1 The g-formula for time-varying treatments (pp. 277–281)

**Time-fixed case.** For only $A_1$, $E[Y^{a_1}]=\sum_{l_1}E[Y|A_1=a_1,L_1=l_1]f(l_1)$, with $f(l_1)=\Pr[L_1=l_1]$. This is the mean outcome standardized to the confounder distribution (p. 277).

**Time-varying case, two time points.** Under static sequential exchangeability for $Y^{a_0,a_1}$ (p. 278):
$$E[Y^{a_0,a_1}]=\sum_{l_1}E[Y|A_0=a_0,A_1=a_1,L_1=l_1]\,f(l_1|a_0).$$
- The weights are the distribution of $L_1$ given the past, here past treatment $a_0$ as set by the intervention. Every factor is conditional on past treatment and covariate history. This conditioning is not needed in the time-fixed case (p. 278).
- Computable only if, for any $l_1$ with $f(l_1|a_0)\neq0$, there are individuals with $(A_0=a_0,A_1=a_1,L_1=l_1)$. This is positivity (Technical Point 19.2) (p. 278).
- Table 21.1: never treat, $84\times0.25+52\times0.75=60$. Always treat, $76\times0.50+44\times0.50=60$. The causal effect estimate is 0, as expected (p. 278).
- The probabilities come from Figure 21.1: $\Pr[A_0=1]=0.5$; $\Pr[L_1=1|A_0=0]=0.75$; $\Pr[L_1=1|A_0=1]=0.5$. Also $\Pr[A_1=1|L_1=0]=0.4$ and $\Pr[A_1=1|L_1=1]=0.8$ (p. 278).

*Intuition note:* The g-formula does not compare treated and untreated people directly. Under the identifiability conditions, it rebuilds the population in which everybody follows the strategy. The $L_1$ distribution is the one that treatment $a_0$ would produce.

**Simulation view.** Under sequential exchangeability for $Y$ and $\bar L$ jointly, the g-formula simulates (identifies) the joint distribution of $(Y^{\bar a},\bar L^{\bar a})$. It builds a new tree (Figure 21.2) in which (i) the strategy's treatment gets probability 1 at each time, and (ii) $\Pr[L_1=l_1|A_0=a_0]$ and $E[Y|A_0,A_1,L_1]$ are kept as in the original population. For "always treat", 32,000 individuals are in the $A_0=1$ branch, 16,000 in each of the two final branches, with means 76 and 44 (pp. 278–279).

Under sequential exchangeability, $\Pr[L_1=l_1|A_0=a_0]=\Pr[L_1^{a_0}=l_1]$ and $E[Y|A_0=a_0,A_1=a_1,L_1=l_1]=E[Y^{a_0,a_1}|L_1^{a_0}=l_1]$ (p. 279).

**Two cautions** (p. 279):
1. The g-formula's value depends on what is included in $L$. If $L_1$ is not collected, on the mistaken belief that it is not a confounder, the formula becomes $E[Y|A_0=a_0,A_1=a_1]$. Because $A_1$ is in fact affected by $L_1$ (Figure 20.8), it then has no causal interpretation.
2. Even when the g-formula is causal, its components may not be. Under the diagram of Figure 20.9, where only static sequential exchangeability holds, $\Pr[L_1=l_1|A_0=a_0]\neq\Pr[L_1^{a_0}=l_1]$ and $E[Y|A_0,A_1,L_1]\neq E[Y^{a_0,a_1}|L_1^{a_0}]$. The formula still equals $E[Y^{\bar a}]$, also if arrows from $A_0,A_1$ to $Y$ are added. In a sequentially randomized trial these inequalities become equalities.

**Fine Point 21.1 (history).** The factor for $L_2$ is conditioned on $A_0,A_1,L_0,L_1$, and so on. "History" need not be chronological. Confounders can lie in the temporal future of treatment, and adjusting for some earlier variables can cause M-bias. Here "history" at $k$ means the treatments and confounders needed for conditional exchangeability for $A_k$. Usually this is the chronological history (p. 280).

**General formula** (times $k=0..K$) (p. 280):
$$\sum_{\bar l}E[Y|\bar A=\bar a,\bar L=\bar l]\prod_{k=0}^{K}f(l_k|\bar a_{k-1},\bar l_{k-1})$$
- The sum $\sum_{\bar l}$ is $\sum_{l_K}\dots\sum_{l_1}\sum_{l_0}$. It equals $E[Y^{\bar a}]$ under sequential exchangeability for $Y^{\bar a}$ given $(\bar L_k,\bar A_k)$ at each $k$ (p. 280).
- With high-dimensional data the components must be estimated. For example, linear regression for $E[Y|\bar A,\bar L]$ and logistic models for discrete $L_k$ ($k\neq0$). The estimates are plugged in: the plug-in g-formula, or parametric g-formula if the models are parametric (p. 280).

**Random strategies.** For a random strategy $f^{int}$ (example: treat independently with probability 0.3 at each $k$), under sequential exchangeability (pp. 280–281):
$$\sum_{\bar a,\bar l}E[Y|\bar A=\bar a,\bar L=\bar l]\prod_{k=0}^{K}f(l_k|\bar a_{k-1},\bar l_{k-1})\prod_{k=0}^{K}f^{int}(a_k|\bar a_{k-1},\bar l_k).$$
Replacing $f^{int}$ by the observed $f(a_k|\bar a_{k-1},\bar l_k)$ gives the observed mean of $Y$. For a deterministic strategy $f^{int}$ is 1 for the mandated treatment and 0 otherwise, so the $f^{int}$ factors and the sum over $\bar a$ can be dropped. Software: the *gfoRmula* R package and the GFORMULA SAS macro (p. 281).

**Technical Point 21.1 (g-formula density)** (p. 281).
- Static strategy $\bar a$: the g-formula density of $(Y,\bar L)$ at $(y,\bar l)$ is $f(y|\bar a_K,\bar l_K)\prod_{k=0}^K f(l_k|\bar a_{k-1},\bar l_{k-1})$.
- The density for $Y$ is its marginal: $\int\!\dots\!\int f(y|\bar a_K,\bar l_K)\prod_{k=0}^K dF(l_k|\bar a_{k-1},\bar l_{k-1})$.
- A dynamic deterministic strategy $g=(g_0,\dots,g_K)$ replaces $a_k$ by $a_k^g$, defined recursively: $\bar a_k^g\equiv\bar g_k(\bar a^g_{k-1},\bar l_k)$, with $\bar a^g_{-1}=0$. A static strategy is the special case of constant $g_k$.
- Inputs: (i) a deterministic strategy $g$, (ii) a causal DAG for the observed data and unmeasured common causes, (iii) a subset $L$ of measured variables to adjust for, (iv) a total ordering of $L$, $\bar A$, $Y$ consistent with the DAG.
- With sequential exchangeability for $Y^g$ and positivity, the density for $Y$ equals $f_{Y^g}(y)$. Otherwise it can be computed but is not causal. With exchangeability and positivity for $(Y^g,\bar L^g)$, the density for $(Y,\bar L)$ equals $f_{Y^g,\bar L^g}$.

### 21.2 IP weighting for time-varying treatments (pp. 282–286)

**Time-fixed reminder.** $W^{A_1}=1/f(A_1|L_1)$; $SW^{A_1}=f(A_1)/f(A_1|L_1)$ (p. 282).

**Time-varying weights** (two time points; $A_{-1}=0$) (p. 282):
$$W^{\bar A}=\prod_{k=0}^{1}\frac{1}{f(A_k|\bar A_{k-1},\bar L_k)},\qquad SW^{\bar A}=\prod_{k=0}^{1}\frac{f(A_k|\bar A_{k-1})}{f(A_k|\bar A_{k-1},\bar L_k)}.$$
- The denominator is, informally, the probability of the treatment history received, given the covariate and treatment history (p. 282).
- Under the identifiability assumptions for static strategies, $E[Y^{a_0,a_1}]=E_{ps}[Y|A_0=a_0,A_1=a_1]$ in the pseudo-population (population reweighted by the weights). This holds for both weight types, and the estimate is the average of $Y$ among those with $\bar A=(a_0,a_1)$ there (p. 282).
- Margin note: $E_{ps}[Y|\bar A=\bar a]=E[W^{\bar A}Y\,I(\bar A=\bar a)]=E[SW^{\bar A}YI(\cdot)]/E[SW^{\bar A}I(\cdot)]$, whether or not sequential exchangeability holds (p. 282).

**Table 21.1 application (Figure 21.3).** With no $L_0$, the denominator is $f(A_0)f(A_1|A_0,L_1)$. Pseudo-population size: $32{,}000\times4=128{,}000$ (4 = number of static strategies). Row pseudo-counts $N_W$ are 8000, 8000, 24,000, 24,000, 16,000 (four rows) (pp. 282–283).
- Never treat: $84\times\frac{8000}{32000}+52\times\frac{24000}{32000}=60$. Always treat also gives 60, so the effect estimate is 0 (p. 282).
- The same 0 results with stabilized weights. In the nonstabilized pseudo-population $\Pr_{ps}[A_k=1|\bar A_{k-1},\bar L_k]=1/2$. In the stabilized one, $\Pr_{ps}[A_k=1|\bar A_{k-1}]=1/2$ (p. 283).
- The nonparametric g-formula and IP weighting estimates are equal. This has nothing to do with causal inference: they would be equal even if identifiability failed (p. 283).

**General form** ($k=0..K$) (p. 283):
$$W^{\bar A}=\prod_{k=0}^{K}\frac{1}{f(A_k|\bar A_{k-1},\bar L_k)},\qquad SW^{\bar A}=\prod_{k=0}^{K}\frac{f(A_k|\bar A_{k-1})}{f(A_k|\bar A_{k-1},\bar L_k)}.$$
When identifiability holds, the pseudo-population has (i) the same mean of $Y^{\bar a}$ as the actual population, and (ii) randomization probabilities constant at 1/2 (nonstabilized) or depending at most on past treatment (stabilized). So $E[Y^{\bar a}]-E[Y^{\bar a'}]=E_{ps}[Y|\bar A=\bar a]-E_{ps}[Y|\bar A=\bar a']$ (p. 283).

**Estimation.** In a true sequentially randomized trial the $f(A_k|\bar A_{k-1},\bar L_k)$ are known, so the estimates are guaranteed unbiased. In observational studies they are estimated, for example by logistic models. A misspecified model gives biased estimates. For stabilized weights, the numerator model $\hat f(A_k|\bar A_{k-1})$ can be misspecified without biasing $E[Y^{\bar a}]$, but then the stabilized pseudo-population no longer has the observed density $f(a_k|\bar a_{k-1})$ (pp. 283–284). In practice one often fits a single model with time-varying intercept terms (p. 284).

**Compare the two estimators** (p. 284). If the parametric g-formula and parametric IP weighting estimates of $E[Y^{\bar a}]$ differ by more than sampling variability (e.g., from the bootstrap), at least one set of models is misspecified. This holds whether or not the identifiability assumptions hold. So estimate with both methods and reexamine the models if they differ. The converse is not guaranteed: both could be biased in the same direction.

**Marginal structural mean model** (p. 284). With many strategies (the text counts $2^K$) and few parameters, one hypothesizes
$$E[Y^{\bar a}]=\beta_0+\beta_1\,cum(\bar a),\qquad cum(\bar a)=\sum_{k=0}^K a_k.$$
It is unsaturated. $\beta_1$ is the average causal effect of the time-varying treatment, and $E[Y^{\bar a}]-E[Y^{\bar a=\bar0}]=\beta_1\times cum(\bar a)$.
- Fit $E[Y|\bar A]=\theta_0+\theta_1cum(\bar A)$ by OLS in the pseudo-population. This is equivalent to weighted least squares (WLS) in the original population with weights $SW^{\bar A}$ or $W^{\bar A}$. Under identifiability, $\hat\theta_1$ is consistent for the causal $\beta_1$, not for the associational $\theta_1$ (p. 285).
- Margin note: the textbook proof that OLS/WLS are consistent for $\theta_1$ assumes weights depend only on $\bar A$. Here the weights depend on $\bar L$, which is correlated with $Y$ given $\bar A$ (p. 285).
- Variance: nonparametric bootstrap, analytic variance, or the robust variance estimator (conservative 95% CI). For a non-saturated model the intervals are typically narrower with $SW^{\bar A}$, so it is preferred (p. 285).
- The model is wrong if the effect depends on treatment through something other than cumulative treatment (e.g., only the last 5 months) or nonlinearly. To test this, fit $E[Y|\bar A]=\theta_0+\theta_1cum(\bar A)+\theta_2cum_{-5}(\bar A)+\theta_3cum(\bar A)^2$ with the weights. A Wald test of $\theta_2=\theta_3=0$ (2 d.f.) tests correct specification. So IP weighting of MSMs is not subject to the g-null paradox (Technical Point 21.3) (p. 285).
- Effect modification: for a dichotomous baseline $V$, $E[Y^{\bar a}|V]=\beta_0+\beta_1cum(\bar a)+\beta_2V+\beta_3cum(\bar a)V$. Fit by WLS with $W^{\bar A}$ or, better, $SW^{\bar A}(V)=\prod_{k=0}^K f(A_k|\bar A_{k-1},V)/f(A_k|\bar A_{k-1},\bar L_k)$. With treatment-confounder feedback, $V$ can only contain baseline variables. If $V$ had components of $L_k$, $k>0$, then $\theta_1$ and $\theta_3$ could differ from 0 even with no effect at any time (p. 285).

*Intuition note:* Each person is weighted by how unlikely their whole treatment path was, given their changing covariates. The reweighted population behaves as if treatment at each time were assigned without looking at $L$ (or only at past treatment, for stabilized weights).

**Technical Point 21.2 (dynamic strategies)** (p. 284). For deterministic dynamic $g$, the g-formula equals $E[Y\,I(\bar A_K=\bar A_K^g)W^{\bar A}]=E_{ps}[Y|\bar A_K=\bar A_K^g]$. The stabilized-weight ratio does not equal the g-formula, because the numerator of $SW^{\bar A}$ depends on $A$. So stabilized weights cannot be used with dynamic strategies. For a random dynamic strategy, the g-formula equals $E[Y\prod_{k}f^{int}(A_k|\bar A_{k-1},\bar L_k)W^{\bar A}]=E\big[Y\prod_k f^{int}(A_k|\cdot)/f(A_k|\cdot)\big]$.

**Technical Point 21.3 (g-null paradox)** (p. 286).
- Suppose treatment-confounder feedback and the sharp null: $Y^{\bar a}-Y^{\bar a'}=0$ with probability 1 for all $\bar a,\bar a'$. Then the g-formula for $E[Y^{\bar a}]$ is the same for every $\bar a$. Yet $E[Y|\bar A=\bar a,\bar L=\bar l]$ and $f(l_k|\bar a_{k-1},\bar l_{k-1})$ both depend on $\bar a$.
- Robins and Wasserman (1997): with standard non-saturated parametric models with variation-independent parameters $\theta,\phi$, and discrete components in $L_k$, the models cannot all be correct. The estimated g-formula will generally depend on $\bar a$. So inference might falsely reject the sharp null, even in a sequentially randomized experiment.
- In practice the paradox has not prevented null g-formula estimates, presumably because the induced bias is small relative to random variability.
- IP weighting of marginal structural mean models and g-estimation of structural nested mean models do not suffer it. Under the null, $\beta_1=0$ in the MSM, and any SNMM blip $\gamma_k(\bar a_{k-1},l_k,\beta)=0$ at $\beta=0$.

### 21.3 A doubly robust estimator for time-varying treatments (pp. 286–290)

Doubly robust methods need a correct model for the treatment or for the outcome. If at least one is correct (one need not know which), they are consistent. This gives "two chances" (p. 286).

**Time-fixed binary $A$, binary $Y$** (estimating $E[Y^a]$; three steps) (pp. 286–287):
1. Predicted $\hat f(a|L)=\widehat{\Pr}[A=a|L]$ from the treatment model.
2. Fit by maximum likelihood, restricted to individuals with $A=a$, a logistic outcome model $b(a,L;\theta)$ that includes $\hat W^a=1/\hat f(a|L)$ as a covariate, e.g. $\mathrm{expit}(\theta_{a,0}+\theta_{a,1}L+\theta_{a,2}\hat W^a)$.
3. Estimate $E[Y^{a=1}]$ and $E[Y^{a=0}]$ as $\hat E[b(1,L;\hat\theta)]$ and $\hat E[b(0,L;\hat\theta)]$, averaged over all individuals. Their difference is doubly robust for the average causal effect under identifiability.

**Time-varying, strategy "always treated"** $\bar a=\bar1=\bar1_K$ (a vector of $K+1$ ones) (p. 287):
- *Step 1.* Fit $\pi_k(\bar L_k;\alpha)$ for $\pi_k(\bar L_k)=\Pr[A_k=1|\bar A_{k-1}=\bar1_{k-1},\bar L_k]$, pooled over persons and times. A person contributes at time $k$ only if $\bar A_{k-1}=\bar1_{k-1}$. For individuals treated through $m$, weights $W^{\bar1_m}=\prod_{k=0}^m 1/\pi_k(\bar L_k)$, estimated with $\hat\pi_k$. So one weight per time $m$, not just one at the end. Example with $K=1$: $\hat\pi_1=\mathrm{expit}(\hat\alpha_{0,1}+\hat\alpha_2L_1)$, $\hat\pi_0=\mathrm{expit}(\hat\alpha_{0,0}+\hat\alpha_2L_0)$.
- *Step 2.* Fit separate outcome models $b_m(\bar L_m;\beta_m)$ for $m=K,K-1,\dots,0$, each only among those treated through $m$, each with $\hat W^{\bar1_m}$ as a covariate. The time-$K$ outcome is $Y$. The time-$m$ outcome ($m<K$) is the predicted $\hat B_{m+1}=b_{m+1}(\bar L_{m+1};\hat\beta_{m+1})$. The last prediction is $\hat B_0=b_0(\bar L_0;\hat\beta)$. Margin note: for binary $Y$, use $b_m=\mathrm{expit}[\gamma_mX_m+\varsigma_m\hat W^{\bar1_m}]$. $\hat B_K$ is not whole but lies in [0,1], so it can be an outcome of a logistic model. For continuous $Y$ use linear regression (p. 288).
- *Step 3.* $\hat E[Y^{\bar a=\bar1}]=$ sample average of $\hat B_0$ over all individuals (p. 288).
- If (i) all outcome models or (ii) all treatment models are correct, the estimate is (asymptotically) unbiased: doubly robust. It is also unbiased if, for some $m\in\{0,\dots,K-1\}$, the treatment models are correct for times $0..m$ and the outcome models for times $m+1..K$. This is $K+2$ robustness (p. 288).
- For "never treated" repeat with $\bar a=\bar0$. The difference of the two is a multiply robust estimator of the average effect (p. 289).
- It works only for static strategies. Technical Point 21.6 handles static or dynamic, deterministic or random (p. 289). Implementation has been hampered by computing limits and lack of software. The authors anticipate machine-learning, sample-split versions becoming common (p. 289).

*Skip path:* Carry forward: weights as covariate in sequential (ICE) regressions, then average the last prediction. It is consistent if either all treatment models or all outcome models are right (more precisely $K+2$ robust) (p. 288).

**Technical Point 21.4 ($K=1$)** (p. 288). Define $\hat b_1(L_0,L_1)=\hat E[Y|L_0,A_0=1,L_1,A_1=1]$ and $\hat b_0(L_0)=\hat E[\hat b_1(L_0,L_1)|A_0=1,L_0]$. The ICE plug-in estimator is $\hat\psi_{gfor}=P_n[\hat b_0(L_0)]$ ($P_n$ is the sample average). The IP weighted estimator is $\hat\psi_{IPW}=P_n[A_0A_1Y/(\hat\pi_0\hat\pi_1)]$. The augmented IP weighted estimator (Robins et al. 1994) is $\hat\psi_{TR}=P_n[\hat U_{TR}]$ with
$$\hat U_{TR}=\frac{A_0A_1Y}{\hat\pi_0\hat\pi_1}-\frac{A_0}{\hat\pi_0}\Big\{\frac{A_1}{\hat\pi_1}-1\Big\}\hat b_1(L_0,L_1)-\Big\{\frac{A_0}{\hat\pi_0}-1\Big\}\hat b_0(L_0).$$
- It is triply ($K+2$) robust. (1) Singly: consistent if $\hat\pi_0,\hat\pi_1$ are consistent, since the last two terms average to 0 and the first term is $\hat\psi_{IPW}$. (2) Doubly: consistent when $\hat E[Y|\cdot]$ and $\hat E[b_1|A_0=1,L_0]$ are consistent. Rearranging, $\hat U_{TR}=\hat b_0(L_0)+\frac{A_0A_1}{\hat\pi_0\hat\pi_1}(Y-\hat b_1)+\frac{A_0}{\hat\pi_0}(\hat b_1-\hat b_0)$. The last two terms average to 0 and the first gives $\hat\psi_{gfor}$. (3) Triply: consistent if $\hat b_1$ and $\hat\pi_0$ are consistent (Molina et al. 2017), using $\hat U_{TR}=A_0\hat b_1/\hat\pi_0+\frac{A_0A_1}{\hat\pi_0\hat\pi_1}(Y-\hat b_1)-(\frac{A_0}{\hat\pi_0}-1)\hat b_0$. It is not consistent when only $\hat\pi_1$ and $\hat E[b_1|A_0=a_0,L_0]$ are consistent.
- Replacing $\hat b_0(L_0)$ by $\tilde b_0(L_0)=\hat E\big[\frac{A_1Y}{\hat\pi_1}-(\frac{A_1}{\hat\pi_1}-1)\hat b_1(L_0,L_1)\,\big|\,A_0=1,L_0\big]$ gives $\hat\psi_{QR}$, quadruply ($2^{K+1}$) robust. It is consistent when only $\hat\pi_1$ and $\hat E[b_1|A_0=1,L_0]$ are consistent. $\tilde b_0$ is itself doubly robust (Tchetgen Tchetgen 2009).

**Technical Point 21.5** (p. 289). $\hat\psi_{TR}$ may fall outside $[0,1]$ for binary $Y$. The plug-in $\hat\psi_{gfor}$ always lies in $[0,1]$ with logistic models. A plug-in $\hat\psi_{TR,plug}=P_n[\hat b_0(L_0)]$ is also triply robust if $P_n[\frac{A_0A_1}{\hat\pi_0\hat\pi_1}(Y-\hat b_1)]$ and $P_n[\frac{A_0}{\hat\pi_0}(\hat b_1-\hat b_0)]$ are zero in every sample. This is achieved by adding the covariate $\theta_1\{A_0A_1/(\hat\pi_0\hat\pi_1)\}$ to the logistic model for $b_1$ (fit among $A_0=A_1=1$), and $\theta_0A_0/\hat\pi_0$ to the logistic model for $b_0$ (fit among $A_0=1$). The estimator in the main text is an instance. (The text refers to "Technical Point 21.12" for $\hat\psi_{TR}$; it is defined in 21.4.)

**Technical Point 21.6 (multiply robust, general $g$)** (p. 290). Let $f^g(a_m|\bar a_{m-1},\bar l_m)$ be the strategy's treatment density: $I(a_m=a^*_m)$ for static $\bar a^*$; $I(a_m=g_m(\bar a_{m-1},\bar l_m))$ for deterministic dynamic; $f^{int}$ for random. $C^g_k=I\big(\prod_{m=0}^k f^g(A_m|\bar A_{m-1},\bar L_m)=0\big)$ is 0 if the observed history is compatible with $g$, else 1. Algorithm (based on Rotnitzky et al. 2017):
1. Fit models $f_m(a_m|\bar a_{m-1},\bar l_m;\alpha_m)$ for $m=0..K$; weight $\hat W^{g,m}=\prod_{k=0}^m f^g(A_k|\cdot)/f_k(A_k|\cdot;\hat\alpha_k)$.
2. Set $\hat T_{K+1}=Y$.
3. For $m=K,\dots,0$: (a) fit a generalized linear model $b_m=\phi[\gamma_md_m(\bar A_m,\bar L_m)+\varsigma_m\hat W^{g,m}]$ ($\phi$ an inverse canonical link) for $E[\hat T_{m+1}|\bar A_m,\bar L_m,C^g_m=0]$ by IRLS among those with $C^g_m=0$, so that $\hat E\{I(C_m^g=0)\binom{d_m}{\hat W^{g,m}}(\hat T_{m+1}-b_m(\cdot;\hat\gamma_m,\hat\varsigma_m))\}=0$; (b) set $\hat T_m=\sum_{a_m}b_m(a_m,\bar A_{m-1},\bar L_m;\hat\gamma_m,\hat\varsigma_m)f^g(a_m|\bar A_{m-1},\bar L_m)$.
4. $\hat\psi_{dr,plug}=\hat E[\hat T_0]$.
- It is $K+2$ robust (Molina et al. 2017): unbiased if for some $p\in\{1..K\}$ the outcome models are correct for $m\in\{K..p\}$ and the treatment models for $m\in\{p-1..0\}$. Without $\hat W^{g,m}$ as a covariate, it is the ICE estimator, singly robust.

**Fine Point 21.2 (representations)** (p. 291). Nonparametrically equivalent representations of the g-formula: (i) standardization, a joint density modeling estimator; (ii) iterated conditional expectations (ICE), requiring sequential regressions; (iii) IP weighting, which requires estimating the conditional density of treatment given past treatment and covariate history. Plug-in estimators from these differ in practice. IP weighted estimators are called that, not g-formula estimators.

### 21.4 G-estimation for time-varying treatments (pp. 289–296)

**Saturated additive SNMM, $K=1$** (p. 290):
- $k=0$: $E[Y^{a_0,a_1=0}-Y^{a_0=0,a_1=0}|A_0=a_0]=\beta_0a_0$.
- $k=1$: $E[Y^{a_0,a_1}-Y^{a_0,a_1=0}|L_1^{a_0}=l_1,A_0=a_0,A_1^{a_0}=a_1]=a_1(\beta_{11}+\beta_{12}l_1+\beta_{13}a_0+\beta_{14}a_0l_1)$.
- By consistency the $k=1$ conditioning is $L_1=l_1,A_0=a_0,A_1=a_1$. Under sequential exchangeability, $A_0=a_0$ can be dropped from the $k=0$ conditioning and $A_1^{a_0}=a_1$ from the $k=1$ one (p. 290).
- Both equations are saturated: four $\beta_1$ parameters cover the four $(A_0,L_1)$ histories. $\beta_0$ covers the single history at $k=0$ (p. 291). Effect of $a_1$: $\beta_{11}$; $\beta_{11}+\beta_{12}$; $\beta_{11}+\beta_{13}$; $\beta_{11}+\beta_{12}+\beta_{13}+\beta_{14}$ for $(A_0,L_1)=(0,0),(0,1),(1,0),(1,1)$ (p. 291).
- The model is "nested" because eq. 1 is the effect of treatment at time 0 and never again, eq. 2 the effect at time 1 and never again, and so on (p. 291).

**Rank-preserving version** (p. 291):
$$Y_i^{a_0,0}=Y_i^{0,0}+\psi_0a_0,\qquad Y_i^{a_0,a_1}=Y_i^{a_0,0}+\psi_{11}a_1+\psi_{12}a_1L_{1,i}^{a_0}+\psi_{13}a_1a_0+\psi_{14}a_1a_0L^{a_0}_{1,i},$$
the second equation restricted to individuals with $A_0=a_0$.
- The first equation is rank preserving: $\psi_0$ is the same for everyone. The second is only conditionally ("locally") rank preserving: ranking is certain to be preserved only between people with the same $a_0$ and $l_1$ (p. 292).
- Rank preservation is biologically implausible, so the interest is in the SNMM, which is agnostic about effect heterogeneity. Given sequential exchangeability, g-estimators of $\psi$ for the rank-preserving model are consistent for $\beta$ of the mean model, even if rank preservation is wrong. Positivity is not required to fit an unsaturated SNMM by g-estimation (p. 292).

**Linking to data** (consistency) (p. 292):
$$Y^{A_0,0}=Y-(\psi_{11}A_1+\psi_{12}A_1L_1+\psi_{13}A_1A_0+\psi_{14}A_1A_0L_1),\qquad Y^{0,0}=Y^{A_0,0}-\psi_0A_0.$$
Candidate counterfactuals with $\psi^\dagger$ in place of $\psi$:
$$H_1(\psi^\dagger)=Y-(\psi^\dagger_{11}A_1+\psi^\dagger_{12}A_1L_1+\psi^\dagger_{13}A_1A_0+\psi^\dagger_{14}A_1A_0L_1),\qquad H_0(\psi^\dagger)=H_1(\psi^\dagger)-\psi^\dagger_0A_0.$$
When $\psi^\dagger=\psi$ and $\bar A_{k-1}=\bar a_{k-1}$, $H_k(\psi^\dagger)=Y^{\bar a_{k-1},\underline0_k}$ (treatment $\bar a_{k-1}$ through $k-1$, then 0) (p. 292).

**Fine Point 21.3 (worked g-estimation)** (p. 293, Tables 21.2–21.3). Sequential exchangeability at $k=1$ implies that within each $(A_0,L_1)$ stratum the mean of $Y^{A_0,0}$ is equal for $A_1=1$ and $A_1=0$, so the means of $H_1(\psi)$ must be equal.
- Stratum (0,0): $84=84-\psi_{11}\Rightarrow\psi_{11}=0$. Stratum (0,1): $52=52-\psi_{11}-\psi_{12}\Rightarrow\psi_{12}=0$. Stratum (1,0): $76=76-\psi_{11}-\psi_{13}\Rightarrow\psi_{13}=0$. Stratum (1,1): $44=44-\psi_{11}-\psi_{12}-\psi_{13}-\psi_{14}\Rightarrow\psi_{14}=0$.
- At $k=0$, $Y^{0,0}\perp A_0$ means that $H_0(\psi)$ has equal mean in $A_0=0$ and $A_0=1$ (16,000 each). For $A_0=0$: $84\times0.25+52\times0.75=60$. For $A_0=1$: $(76-\psi_0)\times0.5+(44-\psi_0)\times0.5=60-\psi_0$. So $\psi_0=0$.
- All parameters are 0, so every $E[Y^g]$, static or dynamic, equals 60, agreeing with the other two methods (p. 292).

**General SNMM** (p. 293). For $k=0..K$:
$$E\big[Y^{\bar a_{k-1},a_k,\underline0_{k+1}}-Y^{\bar a_{k-1},\underline0_k}\,\big|\,\bar L_k^{\bar a_{k-1}}=\bar l_k,\bar A_{k-1}=\bar a_{k-1},A_k=a_k\big]=a_k\gamma_k(\bar a_{k-1},\bar l_k,\beta).$$
- Here $(\bar a_{k-1},a_k,\underline0_{k+1})$ gives $\bar a_{k-1}$ to $k-1$, $a_k$ at $k$, then 0. It differs from $(\bar a_{k-1},\underline0_k)$ only by treatment $a_k$ at $k$ (a "last blip").
- $\gamma_k(\bar a_{k-1},\bar l_k,\psi^\dagger)$ is a known function with $\gamma_k(\cdot,\psi^\dagger=0)=0$; $\beta$ is the true value. With sequential exchangeability, $A_k=a_k$ can be dropped. For $K=1$: $\gamma_0=\beta_0$ and $\gamma_1=\beta_{11}+\beta_{12}l_1+\beta_{13}a_0+\beta_{14}a_0l_1$ (p. 293).

**Technical Point 21.7 (MSM vs SNMM)** (p. 294).
- An SNMM is a semiparametric marginal structural mean model if and only if $\gamma_k(\bar a_{k-1},\bar l_k,\beta)=\gamma_k(\bar a_{k-1},\beta)$ does not depend on $\bar l_k$. Then $E[Y^{\bar a}]=\alpha_0+\sum_{k=0}^K a_k\gamma_k(\bar a_{k-1},\beta)$, with $\alpha_0=E[Y^{\bar0_K}]$ (printed: "$a_0=E[Y^{\bar0_K}]$").
- Such an SNMM also assumes no effect modification by past covariates, which an MSM does not.
- Given such an SNMM, $\beta$ can be estimated by g-estimation or IP weighting. The most efficient g-estimator is more efficient than the most efficient IP weighted one when the SNMM (hence the MSM) is correct.
- If the MSM is correct but $\gamma_k$ truly depends on $\bar l_k$, g-estimates of $\beta$ and $E[Y^{\bar a}]$ are biased while IP weighted ones stay unbiased. This is a variance-bias trade-off.

**$H_k$ in general** (p. 294): $H_k(\psi^\dagger)=Y-\sum_{j=k}^K A_j\gamma_j(\bar A_{j-1},\bar L_j,\psi^\dagger)$. A correct locally rank-preserving model with true $\psi$ is equivalent to $H_k(\psi)=Y^{\bar A_{k-1},\underline0_k}$ exactly; $H_0(\psi)$ is $Y^{\bar0}$. If local rank preservation fails (which will "essentially always" happen if there is a treatment effect) but the SNMM is correct, then $E[H_k(\beta)|\bar A_k,\bar L_k]=E[Y^{\bar A_{k-1},\underline0_k}|\bar A_k,\bar L_k]$ and $E[H_0(\beta)]=E[Y^{\bar0}]$. So $E[Y^{\bar0}]$ is estimated by the sample average of $H_0(\hat\beta)$ for consistent $\hat\beta$.

**Unsaturated models** (p. 294). Options: $\gamma_k=\beta_1$ (same effect for all histories and times), $\beta_1+\beta_2k$ (linear in time), $\beta_1+\beta_2k+\beta_3a_{k-1}+\beta_4l_k+\beta_5l_ka_{k-1}$.

**G-estimation, $\gamma_k=\beta_1$** (p. 295). Then $H_k(\psi^\dagger)=Y-\sum_{j=k}^KA_j\psi^\dagger$.
- Choose $\psi_{low}$, $\psi_{up}$ far below and above plausible values, and a grid (e.g. steps of 0.1).
- For each $\psi^\dagger$ fit the pooled logistic model $\mathrm{logit}\Pr[A_k=1|H_k(\psi^\dagger),\bar L_k,\bar A_{k-1}]=\alpha_0+\alpha_1H_k(\psi^\dagger)+\alpha_2W_k$ with $W_k=w_k(\bar L_k,\bar A_{k-1})$; each person gives $K+1$ observations.
- $\hat\beta$ is the grid value where $\hat\alpha_1$ is closest to 0. Equivalently, the value at which the score test of $\alpha_1=0$ has p-value 1. That is, $\hat\beta$ solves
$$\sum_{i=1,k=0}^{N,K}\{A_i-\mathrm{expit}(\hat\alpha_0+\hat\alpha_2W_{i,k})\}H_{i,k}(\psi^\dagger)=0,$$
with $\hat\alpha_0,\hat\alpha_2$ from the model with $\alpha_1=0$. (The printed sum has $A_i$ without a $k$ subscript.) The 95% CI is the set of $\psi^\dagger$ with p-value $>0.05$ for $\alpha_1=0$ (margin note).
- $\hat\beta$ is consistent if (i) the SNMM is correct, (ii) sequential exchangeability for $Y$ holds, (iii) the treatment model is correct, (iv) $H_k(\psi^\dagger)$ enters the logistic model linearly, not squared or otherwise nonlinear (Technical Point 14.2).

**Vector $\beta$** (pp. 295–296). Example $\gamma_k=\beta_0+\beta_1k+\beta_2a_{k-1}+\beta_3l_k+\beta_4l_ka_{k-1}$ ($\beta$ 5-dimensional, $l$ 1-dimensional) needs 5 extra covariates, e.g.
$$\mathrm{logit}\Pr[A_k=1|\cdot]=\alpha_0+H_k(\psi^\dagger)(\alpha_1+\alpha_2k+\alpha_3A_{k-1}+\alpha_4L_k+\alpha_5L_kA_{k-1})+\alpha_6W_k.$$
- Covariate choice does not affect consistency but affects CI width. A grid search is 5-dimensional (20 points each gives $20^5$ values) and hard when $\dim\beta>2$. Instead take $\hat\beta$ as the $\psi^\dagger$ that makes the 5-d.f. score test p-value 1, i.e. solves $\sum_{i,k}\{A_i-\mathrm{expit}(\hat\alpha_0+\hat\alpha_6^TW_{i,k})\}H_{i,k}(\psi^\dagger)(1,k,A_{i,k-1},L_{i,k},L_{i,k}A_{i,k-1})^T=0$.
- Joint 95% CI: values not rejected by the 5-d.f. score test. Cheaper: univariate Wald $\hat\beta_j\pm1.96$ s.e. (margin notes).

**Technical Point 21.8 (closed form for linear SNMM)** (p. 296). If $\gamma_k=\beta^TR_k$ with $R_k=r_k(\bar L_k,\bar A_{k-1})$ known functions, and $\mathrm{logit}\Pr[A_k=1|\bar L_k,\bar A_{k-1}]=\alpha^TW_k$:
$$\hat\beta=\Big\{\sum_{i,k}A_{i,k}X_{i,k}(\hat\alpha)Q_{i,k}S_{i,k}^T\Big\}^{-1}\Big\{\sum_{i,k}Y_iX_{i,k}(\hat\alpha)Q_{i,k}\Big\},$$
with $X_{i,k}(\hat\alpha)=A_{i,k}-\mathrm{expit}(\hat\alpha^TW_{i,k})$, $S_{i,k}=\sum_{j=k}^KR_{i,j}$, and $Q_{i,k}=q_k(\bar L_{i,k},\bar A_{i,k-1})$, a $\dim\beta$-vector. (Added step: shapes: $Q$, $S$ are $\dim\beta\times1$, so the braces hold a $\dim\beta\times\dim\beta$ matrix and a $\dim\beta$-vector.) $Q$ affects efficiency, not consistency (optimal $Q$ in Robins 1994).
- With a working model $\varsigma^TD_k$ for $E[H_k(\beta)|\bar L_k,\bar A_{k-1}]=E[Y^{\bar A_{k-1},\underline0_k}|\bar L_k,\bar A_{k-1}]$, the estimator
$$\begin{pmatrix}\tilde\beta\\\tilde\varsigma\end{pmatrix}=\Big\{\sum_{i,k}\begin{pmatrix}A_{i,k}X_{i,k}Q_{i,k}\\D_{i,k}\end{pmatrix}(S_{i,k}^T,D_{i,k}^T)\Big\}^{-1}\Big\{\sum_{i,k}Y_i\begin{pmatrix}X_{i,k}Q_{i,k}\\D_{i,k}\end{pmatrix}\Big\}$$
is $2^{K+1}$ multiply robust. It is consistent and asymptotically normal if, for each $k$, either the $\varsigma^TD_k$ model or the treatment model is correct.

**Estimating $E[Y^g]$ after g-estimation** (p. 296). $E[Y^{\bar0}]$ is estimated by $\hat E[H_0(\hat\beta)]$. If there is no effect modification by past covariates ($\gamma_k=\gamma_k(\bar a_{k-1},\beta)$), $\hat E[Y^{\bar a}]=\hat E[Y^{\bar0_K}]+\sum_{k=0}^Ka_k\gamma_k(\bar a_{k-1},\tilde\beta)$. Otherwise, or for dynamic $g$, simulate $L_k$ (Technical Point 21.9).

**Technical Point 21.9 (Monte Carlo algorithm)** (p. 297). Given identifiability and a doubly robust $\tilde\beta$:
1. $\hat E[Y^{\bar0_K}]=$ average of $H_0(\tilde\beta)$ over $N$ subjects.
2. Fit a parametric model $\hat f(l_k|\bar a_{k-1},\bar l_{k-1})$, pooled over persons and times.
3. For $v=1..V$: (a) draw $l_{v,0}$ from $\hat f(l_0)$; (b) for $k=1..K$ draw $l_{v,k}$ from $\hat f(l_k|\bar a_{v,k-1},\bar l_{v,k-1})$ with $\bar a_{v,k-1}=\bar g_{k-1}(\bar l_{v,k-1})$; (c) $\hat\Delta_{g,v}=\sum_{j=0}^Ka_{v,j}\gamma_j(\bar a_{v,j-1},\bar l_{v,j},\tilde\beta)$, with $a_{v,j}=g_j(\bar l_{v,j-1})$ (the $v$th Monte Carlo estimate of $Y^g-Y^{\bar0_K}$).
4. $\hat E[Y^g]=\hat E[Y^{\bar0_K}]+\sum_v\hat\Delta_{g,v}/V$.
- Consistent if the $f(l_k|\cdot)$ model, the SNMM, and either the treatment model or the outcome model $E[Y^{\bar A_{k-1},\underline0_k}|\cdot]$ are correct. Bootstrap CIs.
- If $\tilde\beta$ is consistent for $\beta=0$, $\hat\Delta_{g,v}\to0$ even if the $f(l_k|\cdot)$ model is wrong. So the SNMM preserves the null if identifiability holds and either $\Pr[A_k=1|\cdot]$ is known (sequential randomization) or one of the two models is correct for each $k$.

*Intuition note:* G-estimation asks which "removal of treatment effect" makes outcomes look unrelated to the treatment actually received, once past history is accounted for. In Table 21.1 that value is 0 for every parameter.

### 21.5 Censoring is a time-varying treatment (pp. 297–299)

- Censoring $C_m$ ($m=1..K+1$) is 0 if uncensored at $m$, else 1. It is monotone missing data: $C_m=0$ implies all earlier $C=0$. $C_0=0$ by definition. After censoring, later data are unobserved, so analysis is restricted to $C_m=0$ person-times (p. 298).
- G-formula with censoring: $\sum_{\bar l}E[Y|\bar C=\bar0,\bar A=\bar a,\bar L=\bar l]\prod_{k=0}^Kf(l_k|c_k=0,\bar a_{k-1},\bar l_{k-1})$. If identifiability holds with $A_m$ replaced by $(A_m,C_{m+1})$, it is the g-formula for $E[Y^{\bar a,\bar c=\bar0}]$: the mean if all followed $\bar a$ and nobody was lost to follow-up (p. 298).
- **IP weighting.** Fit, e.g., $E[Y|\bar A,\bar C=\bar0]=\theta_0+\theta_1cum(\bar A)$ in the pseudo-population from $W^{\bar A}\times W^{\bar C}$, where
$$W^{\bar C}=\prod_{k=1}^{K+1}\frac{1}{\Pr(C_k=0|C_{k-1}=0,\bar A_{k-1},\bar L_{k-1})},$$
the denominator estimated by logistic regression. Nonstabilized weights replace censored individuals by copies of uncensored individuals with the same history. The pseudo-population has the size of the original population before censoring: censoring is abolished (p. 298).
- Stabilized: $SW^{\bar C}=\prod_{k=1}^{K+1}\Pr(C_k=0|C_{k-1}=0,\bar A_{k-1})/\Pr(C_k=0|C_{k-1}=0,\bar A_{k-1},\bar L_{k-1})$. Numerator and denominator are estimated by two separate models. The pseudo-population has the size of the original after censoring. Censoring occurs at random given measured $\bar L_k$: selection but no selection bias (pp. 298–299).
- In either pseudo-population there are no arrows from $L_k,A_k$ into later $C_m$. Under exchangeability for $(\bar A,\bar C)$, IP weighting is unbiased even if some $\bar L$ are affected by prior treatment (p. 299).
- For g-estimation of SNMMs, first estimate nonstabilized $W^{\bar C}$ to make a pseudo-population with no censoring, then g-estimate in it (p. 299).

**Technical Point 21.10 (survival)** (p. 299). For risk $\Pr[D^{\bar a,\bar c=\bar0}_{k+1}=1]$ (failure indicators $D_k$; Figure 21.4), the g-formula route identifies it as 1 minus
$$\sum_{\bar l_k}\Pr[D_{k+1}=0|\bar A_k=\bar a_k,\bar L_k=\bar l_k,D_k=C_{k+1}=0]\prod_{m=0}^kf(l_m|\bar a_{m-1},\bar l_{m-1},D_m=C_m=0)\Pr[D_m=0|\bar A_{m-1}=\bar a_{m-1},\bar L_{m-1}=\bar l_{m-1},D_{m-1}=C_m=0].$$
A plug-in estimate fits discrete-time hazard models (pooled logistic) and the density of $L$. Alternatively, fit a pooled logistic hazard model with time-varying weights $W_k^{\bar A}W_k^{\bar C}$ (or stabilized). Its parameters estimate those of a marginal structural pooled logistic model.

### 21.6 The big g-formula (pp. 300–303)

- Few realistic applications rely on identification other than sequential exchangeability plus the g-formula (for example, few for the front door formula). Yet the other identifying formulas are mathematically linked to the g-formula based on all variables (p. 300).
- For any causal DAG, the measured and unmeasured variables $\bar X=(\bar L,\bar U)$ ensure joint sequential exchangeability, because any parent of a treatment lies in $\bar A$ or $\bar X$. If every variable were measured and positivity held, the g-formula based on $\bar X$ would identify $E[Y^g]$ for any strategy $g$. This is the **big g-formula**; it depends only on the distribution of the factuals $(\bar A,\bar L,Y,\bar U)$ (p. 300). Margin note: factuals are variables that exist in the actual world, as opposed to counterfactuals.
- It cannot be used in practice because it contains unmeasured variables. The math question is whether it reduces to a functional of the observed $(\bar A,\bar L,Y)$ distribution. Under the front door criterion it does (Technical Point 21.11, Figure 7.14) (p. 300).
- General questions: can we always decide whether it reduces, assuming only that the joint distribution of $(\bar A,\bar L,Y,\bar U)$ obeys the d-separation relations of the DAG, and if so can we display the formula? Both answered affirmatively (Tian and Pearl 2002; Shpitser and Pearl 2006; Huang and Valtorta 2006) (p. 300).
- These are purely mathematical questions about distributions obeying the d-separation relations. The big g-formula has causal meaning only if the DAG is a causal DAG, which in observational analyses can never be known with certainty (p. 301).

**Technical Point 21.11 (front door via the big g-formula)** (p. 301). Under Figure 7.14, the big g-formula for $\Pr[Y^a=y]$ is $\sum_m\sum_u\Pr[Y=y|M=m,A=a,U=u]\Pr[M=m|A=a,U=u]\Pr[U=u]$. $\Pr[Y^a=y]$ is identified if and only if this depends only on the observed $(Y,M,A)$ distribution. Steps:
- Using $U\perp\!\!\!\perp M|A$ and $A\perp\!\!\!\perp Y|M,U$, rewrite as $\sum_m\Pr[M=m|A=a]\sum_u\Pr[Y=y|M=m,U=u]\{\sum_{a'}\Pr[U=u|A=a']\Pr[A=a']\}$.
- By the same independencies, this equals $\sum_m\Pr[M=m|A=a]\sum_{a'}\{\sum_u\Pr[Y=y|M=m,A=a',U=u]\Pr[U=u|M=m,A=a']\}\Pr[A=a']$.
- That equals $\sum_m\Pr[M=m|A=a]\sum_{a'}\Pr[Y=y|M=m,A=a']\Pr[A=a']$, the front door formula.
- This proof does not need the counterfactual $Y^m$ to exist. A coupling argument: any factual distribution Markov with respect to Figure 7.14 is compatible with an FFRCISTG model "as detailed as the data" (Robins and Richardson 2010), which formally includes $Y^m$. Under that model the big g-formula equals the front door formula (Technical Point 7.4). So no such factual distribution can violate the equality.

**Technical Point 21.12 (SWIG proof)** (p. 302). Only treatment counterfactuals are assumed well defined. SWIG property (Shpitser et al. 2022): if the fixed node $a_m$ is d-separated from $B^{\bar a}$ given $C^{\bar a}$, then $\Pr(B^{\bar a}=b|C^{\bar a}=c)$ does not depend on $a_m$. In the front door SWIG, take $B^a=Y^a$, $C^a=(M^{a'},A)$. Then $E[Y^a|M^a,A]=E[Y^{a'}|M^{a'},A]$ for any $a,a'$. The property is not cross-world. Proof step: $E[Y^a|M^a]=\sum_{a'}E[Y^a|M^a,A=a']\Pr(A=a'|M^a)=\sum_{a'}E[Y^a|M^a,A=a']\Pr(A=a')$ since $M^a$ is d-separated from $A$. By the SWIG property and consistency, $E[Y^a|M^a,A=a']=E[Y^{a'}|M^{a'},A=a']=E[Y|M,A=a']$. Hence $E[Y^a|M^a]=\sum_{a'}E[Y|M,A=a']\Pr(A=a')$. Also, $E[Y^a|M^a]\ne E[Y|M]$, since the observed $M$ is not independent of $A$.

**Technical Point 21.13 (general SNMM)** (p. 303). Blips can be defined relative to any strategy $g$, not only "never treat". The additive SNMM models
$$\gamma^g_t(\bar a_t,\bar l_t)=E[Y^{\bar a_{t-1},a_t,\underline g_{t+1}}-Y^{\bar a_{t-1},\underline g_t}|\bar A_{t-1}=\bar a_{t-1},A_t=a_t,\bar L_t=\bar l_t],$$
which is 0 when $a_t=g_t(\bar a_{t-1},\bar l_t)$. With $H_k(\gamma^g)=Y-\sum_{t=k}^K\gamma^g_t(\bar A_t,\bar L_t)$, consistency alone gives $E[H_k(\gamma^g)|\bar L_k,\bar A_k]=E[Y^{\bar A_{k-1},\underline g_k}|\bar L_k,\bar A_k]$ and $E[H_0(\gamma^g)]=E[Y^g]$. Under positivity and sequential exchangeability the $\gamma^g_t$ are nonparametrically identified. Robins (2004) defined an optimal-regime SNMM to estimate $g_{opt}=\arg\max_gE(Y^g)$. Sequential exchangeability is not the only identifying assumption. Zahn et al. (2022) showed identification under a time-varying parallel trends assumption. Then $E[Y^g]$ is identified for the $g$ that defines the SNMM but not for other strategies. Shahn et al. (2022) showed that adding "no additive effect modification by unmeasured $U$" identifies $E[Y^{g'}]$ for all $g'$, hence $g_{opt}$. (Citation names as printed.)

## Toy example
*Our own example, not from the text.* Two time points, no $L_0$. 160 people: $A_0=0$ for 80 and $A_0=1$ for 80. Counts and treatment probabilities:

| $A_0$ | $L_1$ | people | $\Pr(A_1=1)$ | mean Y |
|---|---|---|---|---|
| 0 | 0 | 40 | 0.25 | 8 |
| 0 | 1 | 40 | 0.75 | 4 |
| 1 | 0 | 20 | 0.25 | 7 |
| 1 | 1 | 60 | 0.75 | 3 |

Assume $Y$'s mean depends only on $(A_0,L_1)$. Assume sequential exchangeability and positivity.

*G-formula.* $f(L_1=1|A_0=0)=40/80=0.5$ and $f(L_1=1|A_0=1)=60/80=0.75$.
- Never treat: $8\times0.5+4\times0.5=6$.
- Always treat: $7\times0.25+3\times0.75=1.75+2.25=4$.
- Effect: $4-6=-2$.

*IP weighting* (weight $=1/[f(A_0)f(A_1|A_0,L_1)]$, $f(A_0)=0.5$).
- Never treat ($A_0=0,A_1=0$): the cell $L_1=0$ has $40\times0.75=30$ people, weight $1/(0.5\times0.75)=8/3$, pseudo-count 80. The cell $L_1=1$ has $40\times0.25=10$ people, weight $1/(0.5\times0.25)=8$, pseudo-count 80. Mean $=(8\times80+4\times80)/160=6$.
- Always treat: $L_1=0$ has $20\times0.25=5$ people, weight 8, pseudo-count 40. $L_1=1$ has $60\times0.75=45$ people, weight $8/3$, pseudo-count 120. Mean $=(7\times40+3\times120)/160=640/160=4$.

Both methods give 6 and 4, as in Section 21.2.

*Traditional comparison:* the crude means among people who followed each strategy are $E[Y|0,0]=(8\times30+4\times10)/40=7$ and $E[Y|1,1]=(7\times5+3\times45)/50=3.4$. The crude difference ($-3.6$) differs from the g-formula's $-2$, because the crude group of "always treated" has a different $L_1$ mix.

## Concepts
- [[g-formula]] — (new) outcome mean standardized to the confounder distribution, each factor conditioned on past treatment and covariate history (p. 278, 280)
- [[plug-in-g-formula]] — (new) g-formula with estimated components; parametric if the models are parametric (p. 280)
- [[treatment-confounder-feedback]] — (new) confounders affected by past treatment that also affect later treatment; why traditional adjustment fails (p. 277)
- [[sequential-exchangeability]] — (new) exchangeability at each time given measured past; identifies sustained-strategy effects (p. 277)
- [[positivity]] — (new) every relevant history value has individuals at each strategy-compatible treatment value, so the g-formula is computable (p. 278)
- [[treatment-strategy-static-dynamic]] — (new) static: fixed treatment sequence; dynamic: depends on history; random: treatment drawn with given probability (pp. 280–281, 284)
- [[ip-weighting-time-varying]] — (new) weights are products over time of $1/f(A_k|\text{history})$, stabilized or nonstabilized (p. 282–283)
- [[marginal-structural-model]] — (new) model for $E[Y^{\bar a}]$ across strategies, e.g. $\beta_0+\beta_1cum(\bar a)$, fit by weighted regression (p. 284)
- [[g-null-paradox]] — (new) under the sharp null with feedback, standard non-saturated parametric g-formula models (variation-independent parameters, discrete components in $L_k$) cannot all be correct (p. 286)
- [[doubly-robust-estimator]] — (new) consistent if either treatment or outcome models are correct; here $K+2$ robust for time-varying treatment (pp. 286–288)
- [[iterated-conditional-expectation]] — (new) g-formula as sequential regressions from the last time backwards (p. 291, 290)
- [[structural-nested-mean-model]] — (new) model for the effect of a last blip of treatment given history (p. 293)
- [[g-estimation]] — (new) find $\psi^\dagger$ making $H_k(\psi^\dagger)$ unassociated with $A_k$ given history (p. 292, 295)
- [[censoring-as-time-varying-treatment]] — (new) censoring indicators $C_k$ treated as part of the treatment, handled by IP weights (p. 297–298)
- [[big-g-formula]] — (new) g-formula using all variables, measured and unmeasured (p. 300)
- [[potential-outcomes]] — counterfactuals $Y^{\bar a}$ for strategies (p. 277)
- [[causal-dag]] — used to check which histories are needed and to define the big g-formula (p. 279, 300)
- [[d-separation]] — used to reduce the big g-formula (p. 301)
- [[back-door-front-door-criterion]] — front door formula as a reduction of the big g-formula (p. 300)
- [[confounding-vs-selection-bias]] — stabilized censoring weights give selection but no selection bias (p. 299)

## Canonical instances
- [[sequentially-randomized-experiment-table-21-1]] — two-time-point dataset where g-formula, IP weighting and g-estimation all give 60 for both strategies (p. 277–278, 282, 293)
- [[front-door-formula-big-g-proof]] — front door formula derived from the big g-formula (p. 301)
- [[g-null-paradox-example]] — parametric g-formula that, under feedback and the sharp null, might theoretically falsely reject the null (p. 286); a theoretical argument, not a numerical example

## Bridges (candidates)
- [structural-analogy] g-formula simulation of $(Y^{\bar a},\bar L^{\bar a})$ and Monte Carlo of Technical Point 21.9 ↔ Bayesian computation: ancestral sampling from a sequential generative model, drawing each $L_k$ given the history set by the strategy.
- [structural-analogy] Stabilized IP weights as ratios of densities ↔ Bayesian computation: importance weights (target density over sampling density).
- [structural-analogy] G-estimation confidence set from inverting score tests over a grid of $\psi^\dagger$ ↔ frequentist inference: confidence sets by test inversion.
- [metaphor] The g-null paradox (each model component is fine but together they cannot all be correct) ↔ Bayesian workflow: priors/likelihood that are individually reasonable but jointly incoherent.

## Questions this raises
- How large is the g-null paradox bias in realistic settings, given the author says only that it "presumably" is small relative to random variability (p. 286)?
- How can a prespecified criterion for "substantially different" g-formula and IP weighted estimates be chosen (p. 284)?
- When would the extra efficiency of g-estimation justify the bias risk from assuming no effect modification by past covariates (p. 294)?
- Which causal DAGs allow the big g-formula to be reduced to observed data, and how is that decided in practice (p. 300)?

## Reading notes
- Printed page = pdf − 9 (pdf 286 = p. 277). PDF is the online revision dated 2026-08-19, not the 2020 print; chapter numbering may differ in older citations. Printed p. 304 (pdf 313) shows only a running header.
- Several statements about the two-point example's numbers are read from Figures 21.1–21.3 images; pseudo-counts check as table counts multiplied by the weight.
- The text counts "$2^K$" strategies in the MSM discussion (p. 284). With times $k=0..K$ one would count $2^{K+1}$ static binary strategies. Reproduced as printed.
- The text calls the estimator $\hat\psi_{TR}$ "of Technical Point 21.12" (p. 289); it is defined in Technical Point 21.4. A condition on p. 295 reads "$\alpha_0+\alpha_0W_k$" (the second term presumably $\alpha_2W_k$). The p. 295 estimating-equation sum uses $A_i$ without a $k$ subscript.
- Margin notes were used where they carry content (e.g., weights depending on $\bar L$ in weighted regression; positivity not required for g-estimation of unsaturated SNMMs). Technical Points 21.4–21.6 are dense and compressed here to the main steps.
