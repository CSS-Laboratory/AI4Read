---
id: hernan-2020-whatif/ch16-instrumental
work: hernan-2020-whatif
unit: "16 Instrumental variable estimation"
pages: 209-226
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Instrumental variable estimation

## L0 — One line
A variable that affects the outcome only through the treatment can replace the need to measure all confounders, but only under extra untestable assumptions (a fourth condition such as homogeneity or monotonicity), and the method is fragile when the instrument is weak.

## L1 — The gist (≤ 120 words)
The methods so far need all confounders to be measured. This chapter asks when an instrument $Z$ (a variable that moves $A$ and reaches $Y$ only through $A$) lets us estimate the effect of treatment $A$ on outcome $Y$ without measuring them. Three instrumental conditions alone give only (usually wide) bounds. A fourth condition is needed. Under effect homogeneity (no effect variation), the ratio of the $Z$–$Y$ difference to the $Z$–$A$ difference is the population average effect. Under monotonicity (no one acts against $Z$) it is the effect in "compliers" (people whose treatment follows $Z$) only. Only the first condition can be checked in data. Weak instruments amplify bias and variance, and small violations can cause large bias.

**Prerequisites:** potential outcomes and counterfactual notation ($Y^a$); conditional exchangeability and confounding; causal diagrams (colliders); expectation and conditional expectation; linear regression.

## L2 — Key ideas (5–10 bullets)
- An instrument $Z$ must meet three conditions: associated with $A$, no effect on $Y$ except through $A$, and no shared causes with $Y$ (p. 209). IV methods may then be used to attempt to identify the effect without measuring the confounder $U$ (p. 209); the three conditions alone do not suffice (pp. 211–212).
- Only condition (i) can be checked empirically; (ii) and (iii) are assumptions, so a variable is only a *candidate* instrument in observational studies (p. 211).
- The three conditions alone give only bounds on the average causal effect, which are often too wide to be useful (pp. 211–212).
- The usual IV estimand for a binary instrument is $\frac{E[Y|Z=1]-E[Y|Z=0]}{E[A|Z=1]-E[A|Z=0]}$. In a randomized trial it is the intention-to-treat effect (effect of assignment $Z$ on $Y$) divided by the effect of $Z$ on $A$, a measure of adherence (p. 213). In the smoking example it is $0.1503/0.0627 = 2.4$ kg, with 95% CI −36.5 to 41.3 (p. 213).
- A fourth condition is needed. Under effect homogeneity (several versions) the estimand is the average causal effect (pp. 214–216). Under monotonicity (no defiers, i.e., nobody who would do the opposite of what $Z$ encourages) it is the average effect in compliers (people whose treatment follows $Z$), a local effect (pp. 218–219, 224).
- Monotonicity and the complier effect are criticized: the compliers are unidentified, defiers may not be negligible in some observational settings, and principal strata may be ill-defined (pp. 219–220).
- Weak instruments give wide intervals, amplify bias from violations of (ii) and (iii), and cause finite-sample bias even with a valid instrument (pp. 220–221).
- IV swaps conditional exchangeability for other assumptions. It is more sensitive to small violations than IP weighting or standardization and suits a narrower setting (p. 223).

## L3 — Walkthrough

### Opening (p. 209)
Methods so far assume that all confounders and selection-bias variables are identified and correctly measured. This is untestable, and residual bias will always exist to some extent (p. 209). IV estimation is a method that can validly estimate causal effects under an alternative set of assumptions that do not require measuring all adjustment factors (p. 209).

### 16.1 The three instrumental conditions
**Setting.** Figure 16.1 is a double-blind randomized trial: $Z$ is the randomization assignment (1 treatment, 0 placebo). $A$ is treatment received, since not everyone adheres. $Y$ is the outcome. $U$ stands for all (partly unmeasured) common causes of adherence and outcome. Arrows: $Z\to A\to Y$, $U\to A$, $U\to Y$ (p. 209).

Standard methods (IP weighting, standardization, g-estimation, stratification, matching) must block the back-door path $A\leftarrow U\to Y$ and are biased if the needed variables are unmeasured, mismeasured or misspecified. IV methods may be used to *attempt* to identify the average causal effect of $A$ on $Y$ even without measuring them (p. 209).

A variable $Z$ is an **instrument** if (p. 209):
- (i) $Z$ is associated with $A$.
- (ii) $Z$ does not affect $Y$ except through its potential effect on $A$.
- (iii) $Z$ and $Y$ do not share causes.

In the trial, (i) holds because people assigned to treatment are more likely to take it. (ii) is expected from the double-blind design (it would fail if side effects unblinded participants). (iii) is expected from random assignment (p. 209).

**Technical Point 16.1 (formal conditions, p. 210).**
- (i) *Relevance*: $Z \not\perp\!\!\!\perp A$.
- (ii) *Exclusion restriction* ("no direct effect of $Z$ on $Y$"). Individual level: $Y_i^{z,a}=Y_i^{z',a}=Y_i^{a}$ for all $z,z'$, all $a$, all individuals $i$. Some results need only the population level: $E[Y^{z,a}]=E[Y^{z',a}]$. It is trivially true for surrogate instruments (defined below).
- (iii) *Marginal exchangeability*: $Y^{a,z}\perp\!\!\!\perp Z$ for all $a,z$. This holds in the SWIGs (single-world intervention graphs) of Figures 16.1–16.3. Together with individual-level (ii) it implies $Y^a\perp\!\!\!\perp Z$. A stronger version is *joint exchangeability*: $\{Y^{z,a}; a\in\{0,1\}, z\in\{0,1\}\}\perp\!\!\!\perp Z$ for dichotomous $A$ and $Z$. Technical Point 16.2 says which results need which version.

**Causal vs surrogate instruments (p. 210).** In Figure 16.1, $Z$ has a causal effect on $A$ (a *causal instrument*). Sometimes the causal instrument $U_Z$ is unmeasured and we use a measured proxy $Z$ associated with it (Figure 16.2: $U_Z\to Z$, $U_Z\to A$). This *surrogate instrument* has no effect on $A$. The $Z$–$A$ association comes from the shared cause $U_Z$, and (iii) becomes "$Z$ and $Y$ do not share causes except for $U_Z$". Both types can be used with caveats (Section 16.4). Figure 16.3 shows an unusual case: $Z$–$A$ association arising from conditioning on a common effect $S$ of $U_Z$ and $Z$, in a selected population (p. 210).

> **Intuition note.** An instrument is a lever that moves treatment but touches the outcome by no other route and is itself unconfounded. Randomization assignment is the model case.

**Smoking example (p. 210).** Effect of smoking cessation $A$ on weight change $Y$. Candidate instrument: cigarette price, with $Z=1$ if the average pack price in the person's U.S. state of birth was above \$1.50, else 0. The case for it: (i) price affects quitting, (ii) price affects weight only through cessation, (iii) no common causes of price and weight change. A margin note says condition (i) is met if the state-of-birth price is associated with cessation through the unmeasured $U_Z$, the price in the place of residence (p. 210).

**Which conditions can be checked (pp. 210–211).** Only (i). $\Pr[A=1|Z=1]=25.8\%$ and $\Pr[A=1|Z=0]=19.5\%$, a risk difference of 6%, so $Z$ is a *weak instrument* (Section 16.5). Conditions (ii) and (iii) cannot be verified. Conditioning on $A$ cannot check (ii), because $A$ is a collider on $Z\leftarrow U_Z\to A\leftarrow U\to Y$ and conditioning would induce a $Z$–$Y$ association even if (ii) held. Condition (iii) cannot be proven because confounding can never be ruled out. Falsification tests can sometimes reject (ii) or (iii), but only for a small subset of violations; for most violations they have no power even with arbitrarily large samples (margin note, p. 211). So in observational studies $Z$ is a *candidate* instrument, justified by subject-matter knowledge (p. 211).

**Fine Point 16.1 (p. 211): candidate instruments.** Three categories:
- *Genetic factors* (Mendelian randomization). Example: ALDH2 variant for alcohol intake and coronary heart disease.
- *Preference* of the physician. Unmeasured $U_Z$ is replaced by a measured surrogate such as the physician's last prescription.
- *Access*: distance or travel time to a facility, calendar period, or price of treatment.

**Technical Point 16.2: bounds (p. 212).**
- For a dichotomous $Y$, $\Pr[Y^{a=1}=1]-\Pr[Y^{a=0}=1]$ lies in $(-1,1)$. Using data (each person's observed outcome fixes one counterfactual, the other set to its extremes) halves the width. The bounds still include 0.
- With a variable meeting population-level (ii) and marginal exchangeability (iii), the *natural bounds* have width $\Pr[A=1|Z=0]+\Pr[A=0|Z=1]$, narrower than data alone. *Sharp bounds* are sometimes narrower, under joint exchangeability.
- All such partial identification methods are often relatively uninformative. Sufficiently strong parametric assumptions about the effect of $A$ on $Y$ can shrink the bounds to a single number (point identification; Section 16.2).

**Conclusion of 16.1 (p. 212).** An instrument by itself does not identify the average effect of cessation on weight change, only bounds. They are typically very wide and often include the null. In the example they would only confirm that cessation can cause gain, loss or no change. Sections 16.3–16.4 give additional unverifiable conditions (p. 212).

### 16.2 The usual IV estimand (pp. 212–214)
When a dichotomous $Z$ meets (i)–(iii) *and* condition (iv) (next section: homogeneity), the average effect $E[Y^{a=1}]-E[Y^{a=0}]$ is identified and equals

$$\frac{E[Y|Z=1]-E[Y|Z=0]}{E[A|Z=1]-E[A|Z=0]}$$

the *usual IV estimand* for a dichotomous instrument (p. 213). For a continuous $Z$ the usual estimand is $\mathrm{Cov}(Y,Z)/\mathrm{Cov}(A,Z)$ (margin note, p. 213).

**Reading it in a randomized trial (p. 213).** The numerator is the effect of assignment $Z$ on $Y$ (the intention-to-treat effect). The denominator is the effect of $Z$ on $A$ (adherence). With perfect adherence the denominator is 1 and the effect of $A$ equals the effect of $Z$. As adherence worsens the denominator moves toward 0 and the effect of $A$ becomes larger than the effect of $Z$. IV bypasses adjustment for confounders by inflating the effect of assignment, and the inflation grows as the $Z$–$A$ risk difference shrinks. Both effects can be estimated without adjustment because $Z$ is randomized. In observational studies the denominator is either the effect of a causal instrument on $A$ or a non-causal association for a surrogate instrument (p. 213).

> **Intuition note.** The ratio uses only how $Y$ and $A$ both change when $Z$ is switched, so adjustment for the $A$–$Y$ confounding by $U$ is bypassed, provided the instrumental conditions and a fourth condition hold. Dividing "how much $Y$ moved" by "how much $A$ moved" scales the effect of $Z$ up to the effect of $A$.

**Estimates in the example (p. 213)** (individuals with missing outcome or instrument excluded):
- Numerator estimate: $\widehat E[Y|Z=1]-\widehat E[Y|Z=0]=2.686-2.536=0.1503$.
- Denominator estimate: $\widehat E[A|Z=1]-\widehat E[A|Z=0]=0.2578-0.1951=0.0627$.
- Ratio: $0.1503/0.0627=2.4$ kg. (This is the "Wald estimator".)

**Equivalent computations (p. 213).** Fit saturated linear models $E[A|Z]=\alpha_0+\alpha_1Z$ and $E[Y|Z]=\beta_0+\beta_1Z$. Or use two-stage least squares: (1) fit $E[A|Z]=\alpha_0+\alpha_1Z$ and predict $\widehat E[A|Z]$ for each person; (2) fit $E[Y|Z]=\beta_0+\beta_1\widehat E[A|Z]$. Then $\hat\beta_1$ is always numerically equal to the standard IV estimate (here again 2.4 kg).

**Uncertainty (pp. 213–214).** The 95% CI is −36.5 to 41.3, expected because the $Z$–$A$ association is weak. A common rule of thumb calls an instrument weak if the first-stage F-statistic is below 10; here it was 0.8.

**Structural mean models (p. 214).** Additive or multiplicative structural mean models (Technical Points 16.3, 16.4) make the assumptions behind 2SLS explicit. Their parameters are estimated by g-estimation. With measured common causes $L$ of instrument and outcome, the choice between 2SLS and structural mean models resembles that between outcome regression and structural nested models (Ch. 14–15). These estimators are valid only when the usual IV estimand can be read as the average causal effect, which needs a fourth condition (p. 214).

### 16.3 A fourth identifying condition: homogeneity (pp. 214–216)
Conditions (i)–(iii) are insufficient to make the IV estimand the average causal effect of $A$ on $Y$; *effect homogeneity* (iv) is needed (p. 214). Four versions are listed in historical order:

1. **Constant effect** across individuals (e.g., everyone gains exactly 2.4 kg after quitting). This is equivalent to additive rank preservation (Section 14.4), which is scientifically implausible for most treatments and outcomes, and impossible for dichotomous outcomes except under the sharp null or universal harm/benefit. Many early 2SLS analyses assumed it implicitly (p. 214).
2. **Additive homogeneity** for dichotomous $Z,A$: $E[Y^{a=1}-Y^{a=0}|Z=1,A=a]=E[Y^{a=1}-Y^{a=0}|Z=0,A=a]$ for $a=0,1$. This is used in Technical Point 16.3. Even when $Y^a\perp\!\!\!\perp Z$ holds, $Y^a\perp\!\!\!\perp Z|A$ does not generally hold, so the effect may depend on $Z$ (margin note, p. 214).
3. **$U$ is not an additive effect modifier**: $E[Y^{a=1}|U]-E[Y^{a=0}|U]=E[Y^{a=1}]-E[Y^{a=0}]$. This is stated in terms of unmeasured confounders $U$, which is more natural, but often implausible: weight gain after quitting may vary with prior smoking intensity, which may itself be an unmeasured confounder (p. 215). Hernán and Robins (2006b) showed that if $U$ is an additive effect modifier, it is not reasonable to believe version 2 holds (margin note, p. 215).
4. **$Z$–$A$ association constant across $U$**: $E[A|Z=1,U]-E[A|Z=0,U]=E[A|Z=1]-E[A|Z=0]$ (p. 215).

Versions 3 and 4 are special cases of a general condition. Define $e(U)\equiv E[Y^{a=1}-Y^{a=0}|U]$ and $t(U)\equiv E[A|Z=1,U]-E[A|Z=0,U]$. The condition is $\mathrm{Cov}[e(U),t(U)]=0$ (p. 215). Versions 3 and 4 are "$e(U)$ is a constant" and "$t(U)$ is a constant", and the covariance of any variable with a constant is 0 (p. 216).

**Technical Point 16.3: additive structural mean model (p. 215).** Saturated model:
$$E[Y^{a=1}-Y^{a=0}|A=1,Z]=\beta_0+\beta_1Z .$$
Equivalently $E[Y-Y^{a=0}|A,Z]=A(\beta_0+\beta_1Z)$. $\beta_0$ is the average effect among the treated with $Z=0$. $\beta_0+\beta_1$ is the effect among the treated with $Z=1$. So $\beta_1$ is additive effect modification by $Z$.

*Proof that $\beta_1=0$ gives the usual estimand.*
- Condition (ii) implies $E[Y^{a=0}|Z=1]=E[Y^{a=0}|Z=0]$ (p. 215).
- Under the model this becomes $E[Y-A(\beta_0+\beta_1)|Z=1]=E[Y-A\beta_0|Z=0]$ (p. 215).
- With $\beta_1=0$: $E[Y|Z=1]-\beta_0E[A|Z=1]=E[Y|Z=0]-\beta_0E[A|Z=0]$ (added step). Solving gives
$$\beta_0=\frac{E[Y|Z=1]-E[Y|Z=0]}{E[A|Z=1]-E[A|Z=0]}.$$

*Why $\beta_1=0$ is assumed.* There are two unknowns ($\beta_0,\beta_1$) and one equation, which exhausts the constraints the three instrumental conditions put on the data distribution. An extra untestable constraint is needed, and $\beta_1=0$ is chosen rather than, say, $\beta_1=2$. This is what "an instrument is insufficient to identify the average effect" means (p. 215).

*Scope.* Under $\beta_1=0$, $\beta_0$ is the average effect in the *treated*. To conclude it is the average effect in the whole study population, one must also assume that the effects of treatment in the treated and in the untreated are identical, i.e., the parameter for $Z$ is also 0 in the structural model for $A=0$. This is another untestable assumption (p. 215).

**Technical Point 16.4: multiplicative structural mean model (p. 216).** Saturated model:
$$\frac{E[Y^{a=1}|A=1,Z]}{E[Y^{a=0}|A=1,Z]}=\exp(\beta_0+\beta_1Z),$$
equivalently $E[Y|A,Z]=E[Y^{a=0}|A,Z]\exp[A(\beta_0+\beta_1Z)]$. For dichotomous $Y$, $\exp(\beta_0)$ is the causal risk ratio in the treated with $Z=0$, and $\beta_1$ is multiplicative effect modification by $Z$. If we assume $\beta_1=0$ and also no multiplicative modification by $Z$ in the untreated, then $E[Y^{a=1}]/E[Y^{a=0}]=\exp(\beta_0)$ and
$$E[Y^{a=1}]-E[Y^{a=0}]=E[Y|A=0](1-E[A])[\exp(\beta_0)-1]+E[Y|A=1]E[A][1-\exp(-\beta_0)].$$
The proof relies on the instrumental conditions (Robins 1989; Hernán and Robins 2006b). The average effect is still identified but no longer equals the usual IV estimand. The estimate therefore depends on whether we assume no additive or no multiplicative modification by $Z$. Even with infinite data we cannot tell which, if either, is true, because saturated models have more unknown parameters than equations (p. 216).

**Technical Point 16.5: proof of the general homogeneity condition (p. 217).** Claim: under Figure 16.1 and $\mathrm{Cov}(e(U),t(U))=0$,
$$E[Y^{a=1}-Y^{a=0}]=\frac{E[Y|Z=1]-E[Y|Z=0]}{E[A|Z=1]-E[A|Z=0]}.$$
Steps:
1. $E[e(U)]=E[Y^{a=1}-Y^{a=0}]$, and $E[t(U)]=E[A|Z=1]-E[A|Z=0]$ because $U\perp\!\!\!\perp Z$.
2. Zero covariance gives $E[e(U)t(U)]=E[e(U)]E[t(U)]$ (added step). Hence $E[e(U)t(U)]/\{E[A|Z=1]-E[A|Z=0]\}=E[Y^{a=1}-Y^{a=0}]$.
3. It remains to show $E[Y|Z=1]-E[Y|Z=0]=E[e(U)t(U)]$. Write $Y=A(Y^{a=1}-Y^{a=0})+Y^{a=0}$.
4. Because $Y^a\perp\!\!\!\perp(A,Z)|U$ and $U\perp\!\!\!\perp Z$ in Figure 16.1:
$$E[Y|Z]=\sum_u\sum_{a\in\{0,1\}}E[Y|A=a,Z,U=u]\Pr(A=a|Z,U=u)f(u|Z)=\sum_u\big\{E[Y^{a=1}-Y^{a=0}|U=u]\Pr(A=1|Z,U=u)+E[Y^{a=0}|U=u]\big\}f(u).$$
5. Therefore $E[Y|Z=1]-E[Y|Z=0]=E\big[E[Y^{a=1}-Y^{a=0}|U]\{\Pr(A=1|Z=1,U)-\Pr(A=1|Z=0,U)\}\big]$, as required.

> **Intuition note.** The usual estimand averages the treatment effect with weights given by how strongly $Z$ moves treatment in each stratum of $U$. It equals the plain average effect if the effect and the strength of $Z$ do not vary together across $U$ (zero covariance).

**Two ways to bypass homogeneity (p. 216).** Because homogeneity is often seen as implausible, the author notes two approaches. (a) Add baseline covariates to the IV models. Structural mean models are safer than 2SLS for this, because they impose fewer parametric assumptions. They allow the effect in the treated to vary with $Z$ by constraining how it varies within covariate levels (Technical Point 16.6). (b) Use a different condition (iv) that does not require homogeneity: monotonicity (next section). It gives the usual estimand a causal interpretation without identifying the population average effect (p. 216).

**Technical Point 16.6: general structural mean models (p. 218).** For continuous or multivariate $A$, instruments $Z$ and pre-instrument covariates $V$, the additive model is
$$E[Y-Y^{a=0}|Z,A,V]=\gamma(Z,A,V;\beta),\quad \gamma(Z,A=0,V;\beta)=0,$$
with $\gamma$ a known function. It is identified by g-estimation under $E[Y^{a=0}|Z=1,V]=E[Y^{a=0}|Z=0,V]$. The multiplicative version is $E[Y|Z,A,V]=E[Y^{a=0}|Z,A,V]\exp[\gamma(Z,A,V;\beta)]$, under analogous conditions. Nested versions can extend IV methods to time-varying treatments and confounders (p. 218).

### 16.4 An alternative fourth condition: monotonicity (pp. 217–220)
Take the double-blind trial. $A^{z=1}$ is the treatment a person would take if assigned $z=1$, and $A^{z=0}$ if assigned $z=0$. If both were known, people fall into four *compliance types* (principal strata) (p. 217):
1. *Always-takers*: $A^{z=1}=1, A^{z=0}=1$.
2. *Never-takers*: $A^{z=1}=0, A^{z=0}=0$.
3. *Compliers* (cooperative): $A^{z=1}=1, A^{z=0}=0$.
4. *Defiers* (contrarians): $A^{z=1}=0, A^{z=0}=1$.

These are not generally identified. A person with $Z=1,A=1$ may be a complier or an always-taker. A person with $Z=1,A=0$ may be a defier or a never-taker (p. 217). **Monotonicity** holds when no defiers exist, i.e., $A^{z=1}\ge A^{z=0}$ for all individuals. Then $Z$ either leaves $A$ unchanged (Figures 16.4, 16.5) or raises it (compliers, Figure 16.6). For defiers, $Z$ would lower $A$ (Figure 16.7) (pp. 217–218).

**Result.** If monotonicity replaces any homogeneity condition as (iv), the usual IV estimand no longer equals the population average effect. It equals the average effect in the compliers, $E[Y^{a=1}-Y^{a=0}|A^{z=1}=1,A^{z=0}=0]$ (p. 218). This is the complier average causal effect (CACE), a local average treatment effect (LATE) (margin note, p. 219).

*Sketch (p. 218).* The effect of $Z$ on $Y$ (the numerator) is a weighted average of the effects of $Z$ in the four strata. It is exactly zero in always-takers and never-takers, because their $A$ is fixed and $Z$ acts only through $A$. No defiers exist. So the numerator is the effect in compliers times the proportion of compliers, and that proportion is the denominator. The full proof is in Technical Point 16.7.

**Technical Point 16.7: proof (p. 224).** (Imbens and Angrist 1994; Baker and Lindeman 1994 for binary outcomes.)
1. Intention-to-treat effect as a weighted average over strata: $E[Y^{z=1}-Y^{z=0}]=\sum_{\text{strata}}E[Y^{z=1}-Y^{z=0}|A^{z=1}=a_1,A^{z=0}=a_0]\Pr[A^{z=1}=a_1,A^{z=0}=a_0]$ over always-takers, never-takers, compliers and defiers.
2. In always-takers and never-takers the effect is zero: $Z$ does not affect $A$ and, by individual-level (ii), has no independent effect on $Y$.
3. With no defiers: $E[Y^{z=1}-Y^{z=0}]=E[Y^{z=1}-Y^{z=0}|A^{z=1}=1,A^{z=0}=0]\Pr[A^{z=1}=1,A^{z=0}=0]$.
4. In compliers $Z=A$, so the effect of $Z$ equals the effect of $A$. Thus
$$E[Y^{a=1}-Y^{a=0}|A^{z=1}=1,A^{z=0}=0]=\frac{E[Y^{z=1}-Y^{z=0}]}{\Pr[A^{z=1}=1,A^{z=0}=0]}.$$
5. Random assignment implies $Z\perp\!\!\!\perp\{Y^{a,z},A^z;z=0,1;a=0,1\}$. With consistency, $E[Y^{z=1}-Y^{z=0}]=E[Y|Z=1]-E[Y|Z=0]$.
6. For the denominator: always-takers are $\Pr[A^{z=0}=1]=\Pr[A=1|Z=0]$; never-takers are $\Pr[A^{z=1}=0]=\Pr[A=0|Z=1]$. With no defiers, compliers are the remainder: $1-\Pr[A=1|Z=0]-(1-\Pr[A=1|Z=1])=\Pr[A=1|Z=1]-\Pr[A=1|Z=0]$.

*Surrogate instruments.* Hernán and Robins (2006b) proved the usual estimator also identifies the complier effect (compliers defined by $U_Z$) when only a surrogate $Z$ is observed. This needs two assumptions: $Z$ independent of $A$ and $Y$ given $U_Z$, and binary $U_Z$. The independence assumption often has little substantive plausibility unless $U_Z$ is continuous, so the complier interpretation is questionable for many observational applications (p. 224).

> **Intuition note.** With no defiers (monotonicity), switching $Z$ only changes the treatment of compliers. So all of the difference in $Y$ between the $Z$ arms comes from them, and dividing by the share of compliers recovers their per-person effect. It does not by itself tell us about always-takers or never-takers.

**Observational studies (pp. 218–219).** There is no assignment, but "compliers" are those with $(A^{z=1}=1,A^{z=0}=0)$. In the example, compliers would quit in a high-price state and not quit in a low-price state. Defiers would do the opposite. If there are no defiers and the causal instrument is dichotomous, 2.4 kg is the IV estimate in compliers (p. 219).

**Criticisms of the complier effect (pp. 219–220).** Monotonicity was welcomed in the mid-1990s as the salvation of IV methods, because homogeneity is often implausible, but the author gives three grounds for criticism:
1. *Relevance.* Compliers are not identified. Their proportion (the denominator; about 6% in the example) varies across instruments and studies, so decision makers cannot easily use the estimate. The author asks what if treatment is not as beneficial in the always-takers and never-takers (the majority). The author suggests interest in this estimand may come from the (often erroneous) perception that it is easy to identify, not from practical relevance (p. 219).
2. *Monotonicity is not always plausible.* In randomized trials the absence of defiers seems a safe assumption (we do not expect anyone to consent in order to do the opposite). It is ensured by design when the control arm is prevented from receiving treatment (no always-takers or defiers), and then the complier effect is the effect in the treated. For "physician preference" it is harder to justify. Example (Swanson and Hernán): physician 1 usually prescribes but not for diabetics; physician 2 usually does not prescribe but does for physically active patients. A patient who is both diabetic and active is treated against both preferences, so is a defier (p. 219). With a dichotomous surrogate $Z$ and continuous causal $U_Z$, the usual estimand is a weighted average of effects over all individuals, not the effect in a particular complier group, even if monotonicity held for $U_Z$ (pp. 219–220; Technical Point 16.7).
3. *Strata may be ill-defined.* A stable partition into the four types needs, among other things, deterministic counterfactuals, no interference, and several forms of heterogeneity. For physician preference it would require physicians with the same preference level to treat a patient identically (p. 220).

**Summary (p. 220).** If the effect in the compliers is of interest, relying on monotonicity seems promising in double-blind two-arm trials with all-or-nothing compliance, especially when one arm has full adherence by design. Caution is needed in more complex settings and observational studies, even if the instrument were truly an instrument (p. 220).

### 16.5 The three instrumental conditions revisited (pp. 220–222)
In observational studies a proposed instrument may violate (ii) or (iii), or be weak, and IV estimation may then be substantially biased even if (iv) held perfectly (p. 220).

**Condition (i) and weak instruments.** Three problems (pp. 220–221):
1. *Wide confidence intervals*, as in Section 16.2.
2. *Bias amplification.* A weak instrument gives a small denominator, so any violation of (ii) or (iii) that affects the numerator is greatly exaggerated. In the example bias is multiplied by about $1/0.0627\approx15.9$ (p. 221).
3. *Finite-sample bias even with a valid instrument.* A randomly generated $Z$ has a zero denominator in an infinite population (estimate undefined). In a finite sample, chance associates it weakly with $U$ and hence with $A$, so the denominator is tiny and the numerator is inflated. The proposed "price > \$1.50" behaves like a random variable: thresholds \$1.60, \$1.70, \$1.80, \$1.90 would give estimates of 41.3, −40.9, −21.1 and −12.8 kg, each with a huge CI (p. 221).

A strong proposed instrument that slightly violates (ii) and (iii) may be preferable to a less invalid but weaker one (p. 221). Martens et al. (2006): in linear models, instruments are guaranteed to be weak under strong confounding, since a strong $A$–$U$ association leaves little residual variation for a strong $A$–$U_Z$ or $A$–$Z$ association (margin note, p. 220).

**Fine Point 16.2: two definitions of weak (p. 221).** *Substantively weak*: the true $Z$–$A$ association (the denominator) is small. *Statistically weak*: the F-statistic is small, typically below 10. The example meets both (risk difference 6%, F = 0.8). The first reminds us that even with an infinite sample the estimator amplifies numerator bias. The second reminds us that even with a perfect instrument the IV estimator can be biased in finite samples.

**Condition (ii) (pp. 221–222).** A direct arrow $Z\to Y$ (Figure 16.8) adds to the numerator and is wrongly inflated as if it were treatment effect. Coarsening a continuous or multi-valued treatment $A$ into a dichotomous $A^*$ can violate (ii) even when it holds for $A$ (Figure 16.9: path $Z\to A\to Y$ is then not mediated by $A^*$). This is a problem for IV but not necessarily for earlier methods.

**Condition (iii) (p. 222).**
- Confounding of $Z$ and $Y$ (Figure 16.10: $U_1$, a cause of $Z$, $A$ and $Y$; $U_2$, a cause of $Z$ and $Y$ only) is inflated by the denominator.
- Plausibility may improve within levels of measured pre-instrument covariates $V$. One can run IV in each stratum and pool, assuming constant effect within $V$ levels (population effect under homogeneity, complier effect under monotonicity), or include $V$ in two-stage models. In the example this reduced the estimate and widened the CI.
- Checking balance of measured confounders across $Z$ may give false security, because even small imbalances can cause large bias through amplification.
- Selection bias can also violate (iii): excluding people with some values of $A$ (e.g., restricting to $A=1$ or $A=2$ when $A\in\{0,1,2\}$) may give a non-null estimate even if the true effect is null. This does not bias non-IV analyses of $A=1$ versus $A=2$.
- Using multiple instruments to offset weakness makes it more likely that some violate a condition.

### 16.6 Instrumental variable estimation versus other methods (p. 223)
IV differs from earlier methods in three ways:
1. It *replaces conditional exchangeability* with other assumptions, so IV can give valid estimates when conditional exchangeability fails if (i)–(iv) hold. The choice depends on whether it is easier to measure the confounders or to find an instrument with monotonicity or no relevant heterogeneity. Regression discontinuity and difference-in-differences also ignore conditional exchangeability (margin note).
2. *Minor violations can cause large bias*, because the denominator blows up the numerator. An IV estimate may sometimes be more biased than an unadjusted estimate. IP weighting and standardization tend to give slightly biased results under slight violations. Hence sensitivity analyses are important.
3. The *ideal setting is narrower*: lots of unmeasured confounding, a truly dichotomous time-fixed treatment, a strong causal proposed instrument, and homogeneity (or monotonicity, if the complier effect is of interest). So IV mostly addresses point interventions and will not be prominent in Part III (time-varying treatments).

IV is attractive for triangulation because its assumptions differ from other methods'. Its wide CIs often limit the value added, and its bias can go in counterintuitive directions and magnitudes (p. 223).

**Fine Point 16.3: regression discontinuity (p. 225).** Example: antiviral treatment $A$ for COVID-19, outcome $Y$ oxygen level after one week, treatment given only if age $L\ge65$, so $\Pr[A=1|L<65]=0$ and $\Pr[A=1|L\ge65]=1$. There is no positivity. Identification assumes (a) $E[Y^{a=1}|L]$ and $E[Y^{a=0}|L]$ are continuous in $L$ (strictly, around the threshold), and (b) people just on either side are exchangeable. A jump in $E[Y|L]$ at 65 is then attributed to the abrupt change in treatment probability, and can be inspected by plotting. The estimate is the difference in mean $Y$ just above versus just below 65, using linear models on each side within a chosen bandwidth. The bandwidth is critical because wide bands compare non-exchangeable people, and cross-validation can help choose it. The estimand is the effect near the threshold, which may differ from the population effect if $L$ is an effect modifier. It is biased if other treatments also change at the threshold or if people manipulate their age. This is the *sharp* design. A *fuzzy* design (treatment probability jumps from above 0 to below 1) relies on monotonicity and estimates the effect in compliers near the threshold (p. 225).

## Toy example (ours, not from the text)
Randomized trial, 1000 people, 500 in each arm ($Z=1$ or $Z=0$), no defiers. Compliance types in the population: 10% always-takers, 30% never-takers, 60% compliers. By randomization each arm has the same mix: 50 always-takers, 150 never-takers, 300 compliers. Assume potential outcomes (unmeasured baseline differences create confounding):

| type | $Y^{a=0}$ | effect of $A$ | $Y^{a=1}$ |
|---|---|---|---|
| always-takers | 10 | +1 | 11 |
| never-takers | 4 | +9 | 13 |
| compliers | 6 | +5 | 11 |

*Numerator.* $E[Y|Z=1]$: always-takers treated $0.1\times11=1.1$; never-takers untreated $0.3\times4=1.2$; compliers treated $0.6\times11=6.6$. Sum $=8.9$. $E[Y|Z=0]$: always-takers treated $1.1$; never-takers $1.2$; compliers untreated $0.6\times6=3.6$. Sum $=5.9$. Difference $=3.0$.

*Denominator.* $E[A|Z=1]=0.1+0.6=0.7$; $E[A|Z=0]=0.1$. Difference $=0.6$ (the complier share).

*IV estimate:* $3.0/0.6=5$, the complier effect, as under monotonicity.
*Population average effect:* $0.1(1)+0.3(9)+0.6(5)=0.1+2.7+3.0=5.8$. The IV estimate is 5, not 5.8, so it is a local effect.
*Naive comparison* by treatment received: treated are 50 + 300 in arm 1 and 50 in arm 0, 400 people, all with $Y=11$ (mean 11). Untreated are $150+150$ never-takers ($Y=4$) and 300 compliers ($Y=6$): $(300\times4+300\times6)/600=3000/600=5$ (300 never-takers in total). Naive difference $=11-5=6$, confounded.
*Amplification.* If assignment had a direct effect of +0.3 on everyone's $Y$ (violating (ii)), the numerator would be 3.3 and the estimate $3.3/0.6=5.5$. If the denominator were 0.06 instead, the same 0.3 would add $0.3/0.06=5$.

## Concepts
- [[instrumental-variable]] (new) — variable $Z$ meeting three conditions that lets $A$'s effect on $Y$ be estimated without measuring all confounders, given a fourth condition (p. 209)
- [[instrumental-conditions]] (new) — (i) relevance, (ii) no effect on $Y$ except through $A$, (iii) no shared causes with $Y$ (pp. 209–210)
- [[exclusion-restriction]] (new) — condition (ii), "no direct effect of $Z$ on $Y$"; individual or population level (p. 210)
- [[surrogate-instrument]] (new) — measured proxy associated with an unmeasured causal instrument $U_Z$; no effect on $A$ itself (p. 210)
- [[weak-instrument]] (new) — small true $Z$–$A$ association, or first-stage F below about 10; inflates bias and variance (pp. 211, 214, 221)
- [[partial-identification-bounds]] (new) — instrument alone gives only upper and lower bounds on the average effect, often wide (p. 212)
- [[usual-iv-estimand]] (new) — $\frac{E[Y|Z=1]-E[Y|Z=0]}{E[A|Z=1]-E[A|Z=0]}$ for binary $Z$ (p. 213)
- [[two-stage-least-squares]] (new) — regress $A$ on $Z$, then $Y$ on predicted $A$; numerically equals the usual estimator here (p. 213)
- [[effect-homogeneity]] (new) — fourth-condition family (several versions) under which the IV estimand is the average effect; a multiplicative version gives a different estimand (pp. 214–216)
- [[structural-mean-model]] (new) — model for mean effect among those with observed treatment $A$ and instrument level $Z$, fit by g-estimation (pp. 215–216, 218)
- [[monotonicity]] (new) — no defiers, $A^{z=1}\ge A^{z=0}$ for all individuals (pp. 217–218)
- [[compliance-types-principal-strata]] (new) — always-takers, never-takers, compliers, defiers; defined by $(A^{z=1},A^{z=0})$, not identified (p. 217)
- [[complier-average-causal-effect]] (new) — effect in compliers; what the usual estimand equals under monotonicity; a local effect (pp. 218–219)
- [[bias-amplification]] (new) — dividing by a small denominator magnifies violations of (ii)/(iii) (p. 221)
- [[regression-discontinuity]] (new) — effect estimated at a threshold of a covariate that assigns treatment (p. 225)
- [[potential-outcomes]] — counterfactual notation $Y^{z,a}$, $A^z$ used throughout (pp. 210, 217)
- [[assignment-mechanism-ignorability]] — IV replaces conditional exchangeability by other assumptions (p. 223)
- [[fork-chain-collider]] — conditioning on $A$ (a collider) cannot check condition (ii) (p. 211)
- [[confounding-vs-selection-bias]] — (iii) can fail by confounding or by selection, e.g., excluding some values of $A$ (p. 222)

## Canonical instances
- [[smoking-cessation-weight-iv]] — price-in-state-of-birth instrument, estimate 2.4 kg, CI −36.5 to 41.3, F = 0.8 (pp. 210, 213–214)
- [[double-blind-randomized-trial-iv]] — randomization assignment as instrument with non-adherence (p. 209)
- [[physician-preference-defiers]] — diabetic and physically active patient as a defier (p. 219)
- [[weak-instrument-price-thresholds]] — thresholds \$1.60–\$1.90 giving 41.3, −40.9, −21.1, −12.8 kg (p. 221)
- [[covid-age-65-regression-discontinuity]] — antiviral given only at age ≥ 65 (p. 225)

## Bridges (candidates)
- [structural-analogy] Non-identified parameter needs an extra untestable assumption ($\beta_1=0$) ↔ Bayesian inference: when data cannot identify a parameter, the posterior depends on the prior — both fill a gap the data cannot.
- [structural-analogy] Weak instrument and small denominator blow up the ratio estimate ↔ Bayesian inference: weakly identified parameters give unstable, highly variable estimates.
- [structural-analogy] Compliance types (latent strata, not observed) ↔ Bayesian latent-class mixtures: each person belongs to an unobserved class that only partly shows in data.
- [metaphor] Bounds from partial identification ↔ Bayesian credible intervals: both express an honest range, but the bounds carry no probability.

## Questions this raises
- How should a sensitivity analysis quantify how large a violation of (ii) or (iii) would turn the estimate to the null, given the amplification factor $1/\text{denominator}$?
- If compliers are unidentified, how can their observed characteristics be described (the text mentions this is possible under strong assumptions; Angrist and Pischke 2009, Baiocchi et al. 2014)?
- When two methods with different assumptions (IV and adjustment) disagree, how should triangulation decide which assumption to doubt?
- Could a Bayesian treatment of IV with priors on violation sizes yield more useful intervals than the wide bounds? (The text does not address this.)

## Reading notes
- Printed page = pdf page − 9 (pdf 218 = printed 209). The last page (printed 226) has only a running header and is otherwise blank.
- This is an online revision dated 2026-08-19, not the 2020 print version (per source note); chapter numbering may differ in older citations.
- Misprint in the source: the text on p. 218 says "Technical Point 16.6 shows a proof" of the complier result, but the proof is in Technical Point 16.7 (p. 224); Technical Point 16.6 (p. 218) is on general structural mean models.
- Page 216 sends the reader to "Section 16.5 and Technical Point 16.6" for structural mean models with covariates. Section 16.5 only briefly mentions covariates (p. 222).
- Technical Points 16.3–16.5 text layers are garbled in places (displayed equations broken); I checked the equations against the page images.
- The example numbers are printed as rounded in the text: $2.686-2.536$ shown as 0.1503; the text does not explain the rounding. The estimate for the \$1.60 threshold (41.3) equals the upper CI limit printed for the \$1.50 threshold (p. 213 vs p. 221); both are as printed.
- No exercises appear in this unit.
- Technical Point 16.1 prints the joint-exchangeability index sets as $[0,1]$; the digest writes $\{0,1\}$ for dichotomous $A$ and $Z$.
