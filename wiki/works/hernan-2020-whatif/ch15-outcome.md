---
id: hernan-2020-whatif/ch15-outcome
work: hernan-2020-whatif
unit: "15 Outcome regression and propensity scores"
pages: 199–208
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
# Outcome regression and propensity scores

## L0 — One line
Outcome regression and propensity-score methods can estimate causal effects under exchangeability and positivity given covariates $L$, but each depends on a correctly specified model, and variable selection built for prediction can harm causal estimates.

## L1 — The gist (≤ 120 words)
The chapter asks how to estimate a causal effect by modelling the outcome or the treatment, and what each choice costs. Outcome regression estimates the effect within levels of covariates $L$. The propensity score $\pi(L)=\Pr[A=1\mid L]$ can replace $L$ in stratification, standardization or matching, because conditional exchangeability and positivity given $L$ carry over to $\pi(L)$. Outcome regression needs the outcome model to be right; g-estimation needs the treatment model to be right. Matching may restrict the analysis to a hard-to-describe subpopulation. Prediction-oriented variable selection can inflate variance and bias, because a propensity model needs the variables that guarantee exchangeability, not good prediction of treatment. The examples use the smoking-cessation and weight-gain data.

**Prerequisites:** conditional exchangeability, positivity and consistency; linear and logistic regression; standardization, IP weighting and g-estimation of structural nested models (Chapters 12–14); basic causal diagrams. A nuisance parameter is a parameter that is not of primary interest (p. 200). Colliders and instruments are not defined in this chapter (the text points to Chapter 18 and the next chapter).

## L2 — Key ideas
- Simple outcome regression and propensity-score methods work fine in simpler settings but are not designed for time-varying treatments (p. 199).
- In outcome regression the nuisance parameters are those of the $L$–$Y$ model. In g-estimation of structural nested models they are those of the treatment model. For fixed treatments, choosing a method means choosing which nuisance model we trust more (p. 200).
- The propensity score $\pi(L)$ balances measured covariates, $A \perp\!\!\!\perp L \mid \pi(L)$. If $L$ is sufficient for exchangeability, so is $\pi(L)$ (pp. 201–202).
- Stratifying on deciles of $\pi(L)$ can leave residual imbalance within strata. Using $\pi(L)$ as a continuous covariate avoids this but needs a correct outcome-model form (p. 203).
- Matching defines a matched population, which may be hard to describe. Closeness criteria trade bias against variance, and matching hides the difference between random and structural nonpositivity (pp. 204–205).
- Restricting by real-world variables characterizes the target population better than restricting by $\pi(L)$ (p. 205).
- Effect modification by $\pi(L)$ is hard to turn into policy statements, and matched estimates may differ from overall ones for several reasons (p. 206).
- Predictive and causal uses of regression differ. Predictive variable selection applied to causal models can add superfluous or harmful covariates, such as strong predictors of $A$, colliders or instruments (p. 207).

## L3 — Walkthrough

### Introduction (p. 199)
The authors say outcome regression and propensity score methods are the most commonly used parametric methods for causal inference. They put them after the g-methods because these simpler methods "do not work in general": they work fine in simpler settings but are not designed to handle the complexities of time-varying treatments (p. 199).

### 15.1 Outcome regression (pp. 199–201)
**Setting.** Treatment $A$ is smoking cessation, outcome $Y$ is weight gain. Exchangeability is assumed conditional on the vector $L$ (sex, age, race, education, smoking intensity and duration, physical activity, exercise, weight) (p. 199).

**Contrast with structural nested models.** These have product terms between $A$ and $L$ but no parameters for $L$ itself. Their g-estimation is agnostic about the form of the $L$–$Y$ relation and so protected from misspecifying it (p. 199).

**Structural model if we are willing to specify the $L$–$Y$ association:**
$$\mathrm{E}[Y^{a,c=0}\mid L]=\beta_0+\beta_1 a+\beta_2 aL+\beta_3 L$$
Here $\beta_2,\beta_3$ are vector parameters (p. 199).
- The causal effects in each stratum of $L$ are functions of $\beta_1,\beta_2$.
- The mean counterfactual outcomes under no treatment are functions of $\beta_0,\beta_3$.
- $\beta_3$ is usually called the "main effect" of $L$, but it may not be the causal effect of $L$, since there may be confounding for $L$. It only quantifies how the mean of $Y^{a=0,c=0}$ varies with $L$ (pp. 199–200).
- In Chapter 12's terms this is a faux marginal structural model. The stabilized weights $SW^A(L)$ all equal 1 because the model conditions on all of $L$ (p. 199, margin).

**Fine Point 15.1 (nuisance parameters, p. 200).**
- Fitting the outcome regression, estimates of $\beta_1,\beta_2$ will in general be consistent only if $\beta_0+\beta_3L$ correctly models $\mathrm{E}[Y^{a=0,c=0}\mid L]$. So $\beta_0,\beta_3$ are nuisance parameters.
- Using g-estimation of $\mathrm{E}[Y^{a,c=0}-Y^{a=0,c=0}\mid L]=\beta_1 a+\beta_2 aL$, estimates will in general be consistent only if $\Pr[A=1\mid L]$ is correct. The nuisance parameters are then those of the treatment model, e.g. $\operatorname{logit}\Pr[A=1\mid L]=\alpha_0+\alpha_1L$.
- Example of bias: modelling $L$ with a linear term $\beta_3 L$ when it should be linear plus quadratic $\beta_3L+\beta_4L^2$.
- Symmetrically, outcome regression is not subject to misspecification of a treatment model. For fixed treatments, the choice "boils down to" which nuisance parameters we believe can be estimated more accurately. When possible, doubly robust methods are a better alternative (see Fine Point 13.2).

**Estimation.** Under exchangeability, positivity and well-defined interventions, $\mathrm{E}[Y^{a=1,c=0}\mid L=l]=\mathrm{E}[Y\mid A=1,C=0,L=l]$, and analogously for the untreated (p. 200). So the structural parameters can be estimated by ordinary least squares fitting
$$\mathrm{E}[Y\mid A,C=0,L]=\alpha_0+\alpha_1A+\alpha_2AL+\alpha_3L$$
Like stratification in Chapter 3, this adjusts for confounding by estimating the effect in each stratum of $L$. If $L$ suffices to adjust for confounding (and selection bias) and the model is correctly specified, the $\alpha$ equal the $\beta$ (p. 200).

**Difference from Section 13.2.** There, regression was an intermediate step before standardizing. Here it is the end of the procedure: we compare conditional means directly (p. 200).

**Numbers.** The model has one product term (between $A$ and smoking intensity). Estimates: $\hat\beta_1=2.6$, $\hat\beta_2=0.05$ (p. 200).
- Effect estimate $\hat{\mathrm E}[Y\mid A=1,C=0,L]-\hat{\mathrm E}[Y\mid A=0,C=0,L]$ is 2.8 kg (95% CI 1.5, 4.1) at 5 cigarettes/day and 4.4 kg (2.8, 6.1) at 40 cigarettes/day (p. 200).
- If we assume no effect modification by any variable in $L$, the model has no product terms. Then $\hat\beta_1$ estimates both the conditional and the marginal average causal effect. Here it gave 3.5 kg (2.6, 4.3) (pp. 200–201).
- For a dichotomous $Y$ one could fit a logistic model for $\Pr[Y=1\mid A=a,C=0,L]$ (p. 201).

*Intuition note.* Outcome regression adjusts by modelling how the outcome depends on $A$ and $L$. In general it gives consistent estimates only if that model is right. Methods built on the treatment model instead need the treatment model to be right.

### 15.2 Propensity scores (pp. 201–202)
**Definition.** $\pi(L)=\Pr[A=1\mid L]$ is the propensity score. It is near 0 for people unlikely to be treated and near 1 for those likely to be (p. 201).
- In an ideal randomized trial with half assigned to $A=1$, $\pi(L)=0.5$ for everyone and for any choice of $L$.
- In observational studies the true $\pi(L)$ is unknown and must be estimated (p. 201).

**Example.** A logistic model for quitting given $L$ (the same model as for IP weighting and g-estimation) gave the lowest estimated score 0.053 (individual 22941) and the highest 0.793 (individual 24949). Mean estimated score: 0.312 in quitters and 0.245 in nonquitters (Figure 15.1) (p. 201).
- If the distribution of $\pi(L)$ were the same in treated and untreated, there would be no confounding due to $L$, i.e. no open path from $L$ to $A$ (p. 201).

**Balance.** People with the same $\pi(L)$ generally differ in some covariates, yet they are equally likely to be treated given $L$. Among all people with a given $\pi(L)$ in the super-population, the distribution of $L$ is the same in treated and untreated:
$$A\perp\!\!\!\perp L\mid \pi(L)$$
This is "balance" (p. 201).
- Margin notes: because of sampling variability the true $\pi(L)$ only approximately balances $L$ in a study. An estimated score from a correct model gives better balance in general. In a randomized experiment the estimated $\pi(L)$ adjusts for random as well as systematic imbalance, so it does better than the true $\pi(L)$ (pp. 201–202).
- Balance holds only for measured $L$, so residual confounding by unmeasured factors remains possible. Randomization balances measured and unmeasured covariates and is the preferred method (pp. 201–202).

**Key result.** Propensity methods need exchangeability, positivity and consistency. Conditional exchangeability $Y^a\perp\!\!\!\perp A\mid L$ implies $Y^a\perp\!\!\!\perp A\mid\pi(L)$. Positivity within levels of $\pi(L)$ (no individual has a score of exactly 0 or 1) holds if and only if positivity within levels of $L$ holds (p. 202).
- Under these conditions $\pi(L)$ can be used for stratification (including outcome regression), standardization and matching. First estimate $\pi(L)$ from the data, then use it in place of $L$ (p. 202).

**Technical Point 15.1 (p. 202).**
- A *balancing score* $b(L)$ is any function of $L$ with $A\perp\!\!\!\perp L\mid b(L)$. The propensity score is the simplest example.
- Rosenbaum and Rubin (1983) proved that exchangeability and positivity based on $L$ imply exchangeability and positivity based on $b(L)$. So if adjusting for $L$ is sufficient, adjusting for any $b(L)$, including $\pi(L)$, is sufficient.
- Figure 15.2 treats $\pi(L)$ as an intermediate node on the path $L\to\pi(L)\to A$, with a deterministic arrow from $L$ to $\pi(L)$. The text says $\pi(L)$ "blocks all backdoor paths from $A$ to $L$" (as printed), which gives a proof of sufficiency.
- A *prognostic score* $s(L)$ satisfies $Y^{a=0}\perp\!\!\!\perp L\mid s(L)$. Methods using it need stronger assumptions and cannot readily be extended to time-varying treatments.

*Intuition note.* $\pi(L)$ compresses many covariates into one number, and within a level of that number treated and untreated look alike on $L$. If $L$ was enough to remove confounding, the one number is enough too.

### 15.3 Propensity stratification and standardization (pp. 202–203)
Under the identifying conditions, $\mathrm{E}[Y^{a=1,c=0}\mid\pi(L)=s]-\mathrm{E}[Y^{a=0,c=0}\mid\pi(L)=s]=\mathrm{E}[Y\mid A=1,C=0,\pi(L)=s]-\mathrm{E}[Y\mid A=0,C=0,\pi(L)=s]$ (p. 202).

**Problem.** $\pi(L)$ is continuous, so two people rarely share a value. Example: only individual 22005 had estimated $\pi(L)=0.6563$ (pp. 202–203).

**Deciles.** Classify people into 10 strata of about equal size (here about 162 each) and estimate the effect in each. Effects ranged from 0.0 to 6.6 kg across deciles, with wide 95% CIs (p. 203).
- Equivalent: an outcome model for $\mathrm{E}[Y\mid A,C=0,\pi(L)]$ with $A$, 9 decile indicators and 9 product terms between $A$ and the indicators.
- Most applications omit the product terms, assuming no effect modification by $\pi(L)$. Without them: 3.5 kg (2.6, 4.4) (p. 203).

**Caution.** Within some deciles the distribution of $\pi(L)$ may differ between treated and untreated. Then the two groups might not be exchangeable in those strata (p. 203).
- IP weighting and g-estimation avoided this because they used the numerical value of the estimated probability, not a categorical version like deciles.
- Outcome regression with $\pi(L)$ as a continuous covariate also avoids it. That gave 3.6 kg (2.7, 4.5).
- Margin note: the IP-weight denominator is $\pi(L)$ for the treated and $1-\pi(L)$ for the untreated.

**Model form.** Validity depends on correctly specifying the relation between $\pi(L)$ and the mean outcome (assumed linear here). Because $\pi(L)$ is one-dimensional, it is easy to guard against misspecification with flexible models such as cubic splines. IP weighting and g-estimation were agnostic about this relation (p. 203).
- $\pi(L)$ itself must still be estimated from a model regressing $A$ on high-dimensional $L$ (margin, p. 203).

**Standardization.** If the parametric assumptions, exchangeability and positivity hold, the model estimates effects within all levels $s$ of $\pi(L)$. For the effect in the whole study population, standardize $\mathrm{E}[Y\mid A,C=0,\pi(L)]$ over the distribution of the propensity score. The procedure is as in Chapter 13, with $\pi(L)$ replacing $L$, and it can include an $A\times\pi(L)$ product term. Standardized estimate: 3.6 kg (2.7, 4.6) (p. 203).

*Intuition note.* Once the score is the only adjustment variable, the outcome model has just one covariate to get right, so flexible shapes are cheap. Coarse bins, however, can leave imbalance inside each bin.

### 15.4 Propensity matching (pp. 204–205)
**Idea.** Matching on $\pi(L)$ is analogous to matching on one continuous variable (Chapter 4). All forms aim for a matched population in which treated and untreated are exchangeable because they have the same $\pi(L)$ distribution. For example, pair each treated individual with one or more untreated individuals with the same score (p. 204).
- Under exchangeability and positivity given $\pi(L)$, association measures in the matched population are consistent estimates of effect measures. The associational risk ratio consistently estimates the causal risk ratio in the matched population.
- The matched population can have the $\pi(L)$ distribution of the treated, of the untreated, or any other arbitrary one (margin).
- Margin: computing the variance of matched estimates used to be a drawback. It is no longer, thanks to Abadie and Imbens (2006).

**Closeness.** Exact equality is unlikely, so a common rule matches a treated individual with score $s$ to untreated individuals with $s\pm0.05$ (or another small difference). Example: treated individual 1089 ($\pi(L)=0.6563$) might be matched with untreated individual 1088 (0.6579) (p. 204).

**Bias–variance trade-off.**
- Criteria too loose: $\pi(L)$ distributions differ in the matched population and exchangeability fails.
- Criteria too tight: many people are excluded, so exchangeability is approximate but 95% CIs may be wider (p. 204).

**Positivity.** The estimated $\pi(L)$ distributions in treated and untreated overlapped over most of the range (Figure 15.1). Only 2 treated individuals (reported as 0.01% of the study population) had scores above all untreated individuals (p. 204).
- Outcome regression on $\pi(L)$ effectively treated this as chance (random nonpositivity) and kept everyone.
- Most matched analyses would exclude those two. Matching does not distinguish random from structural nonpositivity (p. 204).

**Target population.** In theory matching can target a well-characterized population. Matching each treated individual to untreated ones and excluding the unmatched untreated estimates the effect in the treated (Fine Point 15.2). In practice the estimate may refer to a hard-to-describe subset: those whose scores have successful matches (pp. 204–205).
- Restricting to overlap is often presented as a strength, but there is a price. If we can only estimate the effect for $\pi(L)<0.67$, it is unclear who those people are, so transportability to other populations is hard to assess (p. 205).
- Margin: the same score may mean different things in different settings.
- Restriction by real-world variables characterizes the population more naturally. The two treated individuals with $\pi(L)>0.67$ were the only ones over age 50 who had smoked less than 10 years. We could exclude them and say the estimate applies to smokers under 50 and to smokers 50 and over who smoked at least 10 years (p. 205).
- Using scores to detect overlap may be useful, but restricting only to that range is "a lazy way to ensure positivity" (p. 205).

**Fine Point 15.2 (effect modification and propensity score, p. 206).**
- When untreated individuals greatly outnumber treated ones, matching often matches almost all treated and excludes many untreated. The effect-modifier distribution in the matched population then resembles that of the treated, so the matched effect is closer to the effect in the treated than to the whole-population effect. Technical Point 4.1 gives IP weighting and standardization alternatives.
- Effect modification across propensity strata may be read as decision makers knowing what they do (doctors treating those likelier to benefit; Kurth et al. 2006). It can complicate interpretation. Statements such as "beneficial for scores between 0.11 and 0.93" are of little policy relevance because they are not expressed in terms of measured $L$.
- Matched and overall estimates may also differ because of positivity violations in the unmatched, or an unmeasured confounder that is more or less prevalent (or better or worse measured) in the matched population. Apparent effect modification might be explained by differing residual confounding across strata.

*Intuition note.* Matching can give a cleaner comparison by excluding people who cannot be matched, so the answer applies to the matched group. That group is defined by a score value, which is hard to explain.

### 15.5 Propensity models, structural models, predictive models (pp. 205–207)
**Propensity models** model $\Pr[A\mid L]$ for the $L$ needed for conditional exchangeability. Their parameters are nuisance parameters without causal interpretation, because $L$ and $A$ may be associated for many reasons. The $L$–$A$ association can be read as the effect of $L$ on $A$ under Figure 7.1 but not under Figures 7.2 and 7.3. They are still useful as a basis for estimating structural-model parameters (p. 205).

**Structural models** relate $A$ to some component (e.g. the mean) of $Y^a$, marginally or within levels of $L$. For continuous treatments they are often called dose-response models. Their treatment parameters are not nuisance parameters and have a direct causal interpretation (pp. 205–206).
- Marginal structural models contain treatment, effect modifiers $V$ and their products with treatment. The choice of $V$ reflects only the investigator's interest in effect modification.
- With no $V$ the model is truly marginal. With all of $L$ as $V$ it becomes a faux marginal structural model.
- Structural nested models contain treatment and product terms between $A$ and all effect modifiers in $L$ (p. 206).

**Predictive models.** Outcome regression is also used for pure prediction (online retailers predicting purchases; doctors identifying high-risk patients). There the aim is association, not causation, and the parameters need not have causal meaning. All covariates have the same status, with no $A$ and no $L$ (p. 206). Margin note: Kosinski et al. (2013) found that Facebook Likes predict traits, which is purely predictive.

**Variable selection.** For prediction, one may choose any variables that improve predictive ability, using forward, backward or stepwise selection or machine learning (p. 207).
- Courses have not always separated prediction from causal inference, so these procedures are often applied to causal models. This can bring superfluous or harmful covariates, inflated variances and greater bias.
- The mistaken belief is that propensity models should predict $A$ as well as possible. They only need to include the variables $L$ that guarantee exchangeability.
- Covariates strongly associated with treatment but not needed for exchangeability do not help reduce bias. Adjusting for them can give very large variances or even amplify existing bias (p. 207).
- Margin: predictive-power measures such as Mallows's $C_p$ are of questionable relevance for causal inference.

**Hospital example (p. 207).**
- Hospital Aceso gives $A=1$ to 99% of its patients. Hospital Panacea gives $A=0$ to 99%. Hospital has no effect on the outcome except through $A$, so it is not needed for exchangeability.
- Adding Hospital to the propensity model gives $\pi(L)\approx0.99$ in Aceso and $0.01$ in Panacea. By chance, some strata defined by $L$ may have everyone in Aceso treated or everyone in Panacea untreated.
- Then the estimate may have near-infinite variance with no reduction in confounding. That treatment is now well predicted is irrelevant for causal purposes.
- Margin: perfect prediction would give $\pi(L)=1$ for all treated and $0$ for all untreated, so there would be no overlap.

**Self-inflicted bias.** Including colliders may cause systematic bias even though colliders can be effective predictors. Including instruments (next chapter) may amplify bias due to unmeasured variables. Chapter 18 returns to this (p. 207).

**Closing.** Model-based causal methods (propensity and structural) require no misspecification of the covariates' functional form, hence flexible forms such as cubic splines. They also need exchangeability, positivity and well-defined interventions. The next chapter describes a different method that does not require exchangeability of treatment (p. 207).

## Toy example (ours, not from the text)
Aim: show that $A\perp\!\!\!\perp L\mid\pi(L)$ and that standardizing over $\pi(L)$ recovers the effect.

Two binary covariates $L=(L_1,L_2)$. There are 100 people in each of the 4 cells (400 in total). Assume $\pi(L)$ is known, the true effect is $+3$ for everyone, and $Y$ depends on $L$ only. Within each cell exchangeability holds, since every cell has a single value of $L$.

| $L$ cell | $\pi(L)$ | treated | untreated | $Y^{0}$ |
|---|---|---|---|---|
| (0,0) | 0.2 | 20 | 80 | 10 |
| (1,1) | 0.2 | 20 | 80 | 14 |
| (0,1) | 0.5 | 50 | 50 | 11 |
| (1,0) | 0.5 | 50 | 50 | 12 |

*Balance in the $\pi=0.2$ group.* It has 200 people: 40 treated and 160 untreated.
- Among the treated, the share in cell (0,0) is $20/40=0.5$ and in (1,1) is $20/40=0.5$.
- Among the untreated, the shares are $80/160=0.5$ and $80/160=0.5$.
- So $L$ has the same distribution in treated and untreated within this group. The same check works for $\pi=0.5$: $50/100=0.5$ in each cell, in both arms.

*Effect within the $\pi=0.2$ group.*
- Treated mean $=0.5(10+3)+0.5(14+3)=0.5(13)+0.5(17)=15$.
- Untreated mean $=0.5(10)+0.5(14)=12$.
- Difference $=3$.

*Effect within the $\pi=0.5$ group.*
- Treated mean $=0.5(14)+0.5(15)=14.5$.
- Untreated mean $=0.5(11)+0.5(12)=11.5$.
- Difference $=3$.

*Standardize over $\pi(L)$.* Each level has weight $200/400=0.5$, so the effect is $0.5(3)+0.5(3)=3$.

*Crude comparison, no adjustment.*
- Treated mean $=(20\cdot13+20\cdot17+50\cdot14+50\cdot15)/140=2050/140\approx14.643$.
- Untreated mean $=(80\cdot10+80\cdot14+50\cdot11+50\cdot12)/260=3070/260\approx11.808$.
- Difference $\approx2.835\ne3$.

Conditioning on the single number $\pi(L)$ removes the bias just as conditioning on both covariates would.

## Concepts
- [[outcome-regression]] (new) — regress $Y$ on $A$, $L$ (and products) and read effects from the conditional means, without standardizing (p. 200)
- [[propensity-score]] — $\pi(L)=\Pr[A=1\mid L]$, estimated from data in observational studies (p. 201)
- [[balancing-score]] (new) — a function $b(L)$ with $A\perp\!\!\!\perp L\mid b(L)$; $\pi(L)$ is the simplest example (p. 202)
- [[prognostic-score]] (new) — a function $s(L)$ with $Y^{a=0}\perp\!\!\!\perp L\mid s(L)$; needs stronger assumptions (p. 202)
- [[nuisance-parameters]] (new) — parameters not of primary interest, e.g. those of the outcome model or the treatment model (p. 200)
- [[structural-model-vs-propensity-model]] (new) — structural models have causal treatment parameters; propensity models have nuisance parameters without a causal interpretation (pp. 205–206)
- [[assignment-mechanism-ignorability]] — here, conditional exchangeability and positivity given $L$ or $\pi(L)$ (p. 202)
- [[propensity-matching]] (new) — pair treated and untreated with close $\pi(L)$; effect applies to the matched population (p. 204)
- [[causal-vs-predictive-modelling]] (new) — prediction wants any useful covariate; causal models need those ensuring exchangeability (p. 207)
- [[fork-chain-collider]] — colliders as covariates may cause bias even if they predict well (p. 207)

## Canonical instances
- [[smoking-cessation-weight-gain]] — running example (A = quitting, Y = weight gain): overall effect estimates of 3.5–3.6 kg by several methods; 2.8 and 4.4 kg at 5 and 40 cigarettes/day; 0.0–6.6 kg across propensity deciles (pp. 200–203)
- [[hospital-aceso-panacea]] — a strong predictor of treatment that is unnecessary for exchangeability inflates variance (p. 207)
- [[facebook-likes-prediction]] — purely predictive use of regression (p. 206, margin)

## Bridges (candidates)
- [structural-analogy] Nuisance parameters in outcome versus treatment models ↔ Bayesian inference: parameters not of interest are handled in a separate model component (the unit does not discuss this).
- [structural-analogy] $A\perp\!\!\!\perp L\mid\pi(L)$ ↔ sufficient statistics: given one summary, the rest of $L$ carries no further information about treatment.
- [structural-analogy] Predictive variable selection versus causal adjustment ↔ model comparison: criteria for predictive fit need not choose the right adjustment set.

## Questions this raises
- If both the outcome model and the treatment model might be wrong, how do doubly robust methods (Fine Point 13.2) combine them?
- How can we tell in practice that $L$ includes the variables guaranteeing exchangeability, when we cannot predict $A$ well as a check?
- Which causal diagrams make a covariate a collider or an instrument, and how does adjusting for it change bias (Chapter 18)?
- How do propensity methods behave when treatments vary over time, which this chapter says they are not designed for?

## Reading notes
- Printed page = pdf page − 9 (pdf 208 = p. 199). Printed p. 208 contains only a running header.
- Source is the online revision dated 2026-08-19, not the 2020 print version; chapter numbering may differ from older citations.
- Technical Point 15.1 says $\pi(L)$ "blocks all backdoor paths from A to L"; the image shows this wording. The intended path is probably from $A$ to $Y$ (my reading, not stated).
- The text says 2 treated individuals are "0.01% of the study population". Ten deciles of about 162 people imply roughly 1,620 people, so 2 would be about 0.12%. This may be a misprint (my arithmetic, not the book's).
- The sentence "See Fine Point 15.1 for a discussion of parameters that, like β0 and β3, do not have a causal interpretation" is split across the page break between pp. 199 and 200. Equation formatting in the text layer is lightly garbled, but the images were checked.
- The unit has no exercises. Program 15.1–15.4 code is referenced in margins but not shown.
