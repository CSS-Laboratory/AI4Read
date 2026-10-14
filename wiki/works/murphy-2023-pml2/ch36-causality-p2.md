---
id: murphy-2023-pml2/ch36-causality-p2
work: murphy-2023-pml2
unit: "36 Causality (part 2/2): end of 36.4, 36.5 Instrumental variables, 36.6 Difference in differences, 36.7 Credibility checks, 36.8 The do-calculus (to the start of 36.8.3)"
pages: 1208–1231
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Causality (part 2/2): instruments, difference in differences, sensitivity analysis, do-calculus

## L0 — One line
When we cannot adjust for all confounders, we can sometimes still identify causal effects from observational data by adding a design assumption (instrument, parallel trends, or a causal graph via the do-calculus), and we should then stress-test the assumptions that data cannot check.

## L1 — The gist (≤ 120 words)
Adjustment needs every confounder to be observed. This unit asks what else can identify a causal effect. Answers: an instrument plus an extra assumption (additive confounding, monotonicity giving the LATE, or linearity giving two-stage least squares); difference in differences under parallel trends; or the do-calculus applied to a causal graph (back-door, front-door). It gives a double machine learning estimator for the LATE. It then covers credibility checks: placebo treatments and outcomes, and Austen plots, which ask how strong an unobserved confounder would need to be to produce a given bias. These matter because some identification assumptions cannot be tested from data.

**Prerequisites:** potential outcomes and the ATE; back-door adjustment, propensity score and AIPTW (Section 36.4, not in this unit); do-operator and d-separation; conditional expectation; Beta and Bernoulli distributions.

## L2 — Key ideas
- Before trusting an adjustment estimate, compare several estimators, inspect propensity scores (treatment probabilities given covariates) for overlap (treated and control units at similar covariate values), and quantify the variance (bootstrap or analytic). Unobserved-confounding bias can be substantial, often overwhelming estimation error (p. 1208).
- An instrument must satisfy relevance (it affects the treatment), unconfoundedness (no open back-door path from it to $Y$ given covariates) and exclusion (it affects $Y$ only through the treatment). These are necessary but not sufficient for identification; an extra assumption is also needed (p. 1209).
- With additive unobserved confounding, the effect contrast equals a contrast of a function $\tilde f$ that solves an integral equation linking $\mathbb{E}[Y|z,x]$ and $p(a|z,x)$; if the solution is unique, the effect is identified. Relevance is not used in the proof; its role is to limit how many solutions exist (pp. 1210–1211).
- With a binary instrument and treatment, the IV assumptions and monotonicity (no defiers), the LATE (local average treatment effect: the effect among compliers, who take the treatment only if assigned) equals a ratio of two observational contrasts (the effect of $Z$ on $Y$ over the effect of $Z$ on $A$). Double machine learning estimates it with $\sqrt n$-rate asymptotics under conditions on the errors of the nuisance models (pp. 1212–1215).
- Two stage least squares, which assumes linear models, can give far-too-small standard errors under misspecification and weak relevance (pp. 1215–1216).
- Difference in differences identifies the effect on the treated under (conditional) parallel trends (without treatment, both groups would follow the same time trend), together with a causal graph and overlap. Its estimation task is the same statistical task as adjustment (pp. 1216–1219).
- Placebo treatments or outcomes and Austen plots probe untestable assumptions. Austen plots work for any model of the observed data but rest on an assumed model for the confounder, so they only guide experts informally (pp. 1220–1228).
- The do-calculus has three rewrite rules. Back-door adjustment follows from rules 2 and 3, and front-door adjustment handles confounding via an observed mediator (pp. 1228–1231).

## L3 — Walkthrough

### End of 36.4: practical checks on adjustment estimates (p. 1208)
- Small datasets may force simple models for the nuisance functions $g$ (propensity) and $Q$ (outcome regression). If overlap is poor in some regions, flexible $Q$ may be highly variable and inverse propensity weights may be large, so IPTW/AIPTW estimates may fluctuate wildly. Outcome regression is then sensitive to how $Q$ is specified (p. 1208).
- Checks the author lists (p. 1208):
  - Compute several ATE estimators (outcome regression, IPTW, doubly robust) with comparably complex $Q$ and $g$ models. Agreement gives some comfort but no guarantee. Disagreement calls for caution.
  - Inspect the estimated, ideally cross-fitted, propensity scores $\hat g(x_i)$ for overlap failures. If overlap is poor, consider the ATE on the treated or a "trimmed" estimand that drops units with extreme propensities.
  - Quantify uncertainty by bootstrapping the whole procedure (refitting models each time) or by the AIPTW analytical variance. Large variance estimates may indicate problems with the analysis; poor overlap will often (though not always) show up as extremely large variance. Small variance estimates call for caution unless other checks (overlap, stability across $Q$ and $g$ models) also pass.
- These checks address only the statistical problem. Whether $\tau$ is an ATE depends on "no unobserved confounders", and sensitivity analysis (Section 36.7) addresses that. The author adds that bias from unobserved confounding can be substantial in practice, often overwhelming bias due to estimation error (p. 1208).

### 36.5 Instrumental variable strategies (pp. 1208–1210)
- Setting: unobserved confounder $U$ affects $A$ and $Y$. An **instrumental variable** $Z$ affects $Y$ only through $A$ (Figure 36.5; observed covariates $X$ allowed). Informally: find the effect of $Z$ on $Y$ and of $Z$ on $A$, then combine them (p. 1209).
- Three conditions, for observed $X$ (p. 1209):
  1. **Relevance:** $Z \not\perp A \mid X$.
  2. **Unconfoundedness:** every back-door path between $Z$ and $Y$ is blocked by $X$, even conditional on $A$.
  3. **Exclusion restriction:** all directed paths from $Z$ to $Y$ pass through $A$.
- These are necessary but "not quite sufficient". An extra assumption is needed. Historically it was linearity of both the instrument–treatment and treatment–outcome relations (p. 1209).
- Examples (pp. 1209–1210):
  - *Random assignment with non-compliance.* Random assignment of a drug is the instrument.
    - Relevance holds if assignment changes the probability of taking the drug.
    - Unconfoundedness holds because assignment is randomized.
    - Exclusion is plausible, but may fail if unassigned patients seek other treatment.
  - *Judge fixed effects.* The judge assigned to a case is the instrument for incarceration.
    - Relevance requires judges to differ in severity.
    - Unconfoundedness follows from random assignment of judges.
    - Exclusion may fail if judges add unrecorded punishments.
- Relevance can be checked from data. Unconfoundedness is often true by design, or restricted to "obvious" cases (e.g. rainy days as an instrument for sun exposure). Exclusion needs domain expertise (p. 1210).

#### 36.5.1 Additive unobserved confounding (pp. 1210–1211)
- Assume the structural equation (unit-specific variables folded into $U$, footnote 7):
$$Y \leftarrow f(A,X) + f_U(U) \tag{36.48}$$
  Treatment and $U$ do not interact. Then $\mathbb{E}[Y|X,\mathrm{do}(A=a)]-\mathbb{E}[Y|X,\mathrm{do}(A=a')] = f(a,X)-f(a',X)$, which is the target (p. 1210).
- **Theorem 3.** If the IV assumptions and additive confounding hold, there is $\tilde f$ with
$$\mathbb{E}[Y|x,\mathrm{do}(A=a)]-\mathbb{E}[Y|x,\mathrm{do}(A=a')] = \tilde f(a,x)-\tilde f(a',x) \tag{36.49}$$
for all $x,a,a'$, and with
$$\mathbb{E}[Y|z,x] = \int \tilde f(a,x)\,p(a|z,x)\,\mathrm{d}a. \tag{36.50}$$
  If a unique $g$ satisfies $\mathbb{E}[Y|z,x]=\int g(a,x)p(a|z,x)\,\mathrm{d}a$ (36.51), then $g=\tilde f$ and this identifies the causal effect (pp. 1210–1211).
- Why useful: the left side and $p(a|z,x)$ are observational, so $\tilde f$ is identified implicitly as a solution of (36.51) (p. 1211).
- Proof (p. 1211). Additivity plus unconfoundedness gives $U \perp Z \mid X$. Then
$$\mathbb{E}[Y|Z,X] = \mathbb{E}[f(A,X)|Z,X]+\mathbb{E}[f_U(U)|Z,X] \tag{36.52}$$
$$= \mathbb{E}[f(A,X)|Z,X]+\mathbb{E}[f_U(U)|X] \tag{36.53}$$
$$= \mathbb{E}[\tilde f(A,X)|Z,X], \tag{36.54}$$
  with $\tilde f = f(A,X)+\mathbb{E}[f_U(U)|X]$. Contrasts of $\tilde f$ equal contrasts of $f$ because $\mathbb{E}[f_U(U)|x]$ cancels. Rewriting (36.54) as an integral gives (36.55), which is (36.50).
- Role of assumptions: exclusion is implied by the additive form. Unconfoundedness gives $U\perp Z|X$. Relevance is not used in the proof. It matters because different $z$ add non-trivial constraints on $g$ only if $p(a|z,x)$ varies with $z$ (p. 1211).
- Estimation: fit $\mathbb{E}[Y|z,x]$ and $p(a|z,x)$, then solve the implicit equation. Methods vary and are only cited. Even under relevance, several functions may solve (36.51). The ambiguity is removed by a structural assumption, e.g. a neural network with minimum $\ell_2$ parameter norm (p. 1211).

*Intuition note.* The instrument gives us many "experiments" (one per value of $z$), each telling us the average of the outcome function over a different treatment distribution. The more these differ, the fewer outcome functions fit all of them; if exactly one does, the effect is identified (even under relevance, several may fit). Relevance is what makes them differ.

#### 36.5.2 Instrument monotonicity and LATE (pp. 1212–1213)
- For binary instrument and treatment, think of $Z$ as assignment. The population has four types (p. 1212):
  1. Compliers take treatment if assigned, otherwise not.
  2. Always takers always take it.
  3. Never takers never take it.
  4. Defiers refuse if assigned and take it if not.
- The **local (complier) average treatment effect** is
$$\mathrm{LATE} = \mathbb{E}[Y|\mathrm{do}(A=1),\text{complier}]-\mathbb{E}[Y|\mathrm{do}(A=0),\text{complier}] \tag{36.56}$$
  (named LATE because "CATE" already means conditional ATE, footnote 8).
- **Instrument monotonicity:** assignment only increases the probability of taking treatment for each unit, equivalently $P(\text{defier})=0$ (p. 1212).
- **Theorem 4.** Under the IV assumptions and monotonicity, $\mathrm{LATE}=\tau^{\mathrm{LATE}}$, where
$$\tau^{\mathrm{LATE}}=\frac{\mathbb{E}\big[\mathbb{E}[Y|X,Z=1]-\mathbb{E}[Y|X,Z=0]\big]}{\mathbb{E}\big[P(A=1|X,Z=1)-P(A=1|X,Z=0)\big]} \tag{36.57}$$
- Proof (pp. 1212–1213).
  - Back-door adjustment (Theorem 2) on numerator and denominator separately gives
$$\tau^{\mathrm{LATE}}=\frac{\mathbb{E}[Y|\mathrm{do}(Z=1)]-\mathbb{E}[Y|\mathrm{do}(Z=0)]}{P(A=1|\mathrm{do}(Z=1))-P(A=1|\mathrm{do}(Z=0))} \tag{36.58}$$
  - Intervening on $Z$ does not change type proportions: $P(\text{complier}|\mathrm{do}(Z=z))=P(\text{complier})$, and likewise for the other types. So the numerator of (36.58) splits by type (the source prints the second term of (36.59) with $\mathrm{do}(Z=1)$ twice; it should be $\mathrm{do}(Z=0)$):
$$\mathbb{E}[Y|\mathrm{do}(Z=1)]-\mathbb{E}[Y|\mathrm{do}(Z=0)] \tag{36.59}$$
$$=\big(\mathbb{E}[Y|\text{complier},\mathrm{do}(Z=1)]-\mathbb{E}[Y|\text{complier},\mathrm{do}(Z=0)]\big)P(\text{complier}) \tag{36.60}$$
$$\;+\big(\mathbb{E}[Y|\text{always/never},\mathrm{do}(Z=1)]-\mathbb{E}[Y|\text{always/never},\mathrm{do}(Z=0)]\big)P(\text{always/never}) \tag{36.61}$$
$$\;+\big(\mathbb{E}[Y|\text{defier},\mathrm{do}(Z=1)]-\mathbb{E}[Y|\text{defier},\mathrm{do}(Z=0)]\big)P(\text{defier}) \tag{36.62}$$
  - For compliers, setting $Z=z$ sets $A=z$:
$$\mathbb{E}[Y|\text{complier},\mathrm{do}(Z=z)]=\mathbb{E}[Y|\text{complier},\mathrm{do}(A=z)] \tag{36.63}$$
  So $\mathrm{LATE}=\mathbb{E}[Y|\text{complier},\mathrm{do}(Z=1)]-\mathbb{E}[Y|\text{complier},\mathrm{do}(Z=0)]$ (36.64). The author calls this the core reason an instrument identifies the LATE.
  - By definition of the types, $P(A=1|\mathrm{do}(Z=1))=P(\text{complier})+P(\text{always taker})$ (36.65) and $P(A=1|\mathrm{do}(Z=0))=P(\text{always taker})$ (36.66). Hence $P(\text{complier})=P(A=1|\mathrm{do}(Z=1))-P(A=1|\mathrm{do}(Z=0))$.
  - So (36.60) $=\mathrm{LATE}\times\big(P(A=1|\mathrm{do}(Z=1))-P(A=1|\mathrm{do}(Z=0))\big)$ (36.67–36.68).
  - Term (36.61) is 0: always/never takers ignore the instrument. Term (36.62) is 0 because $P(\text{defier})=0$.
  - Therefore the left side of (36.59) equals $\mathrm{LATE}\times(P(A=1|\mathrm{do}(Z=1))-P(A=1|\mathrm{do}(Z=0)))+0+0$ (36.69–36.70). Rearranging and using (36.58) gives the result.

*Intuition note.* Given no defiers, only compliers change their treatment when the instrument changes. So the instrument's effect on $Y$, divided by the share of people it moves into treatment, is the treatment effect for those people. It says nothing about always or never takers.

##### 36.5.2.1 Estimation (pp. 1213–1215)
- Nuisance functions: $\mu(z,x)=\mathbb{E}[Y|z,x]$ (36.72), $m(z,x)=P(A=1|x,z)$ (36.73), $p(x)=P(Z=1|x)$ (36.74).
- Scores:
$$\phi_{Z\to Y}(\mathbf X;\mu,p)=\mu(1,X)-\mu(0,X)+\frac{Z(Y-\mu(1,X))}{p(X)}-\frac{(1-Z)(Y-\mu(0,X))}{1-p(X)} \tag{36.75}$$
$$\phi_{Z\to A}(\mathbf X;m,p)=m(1,X)-m(0,X)+\frac{Z(A-m(1,X))}{p(X)}-\frac{(1-Z)(A-m(0,X))}{1-p(X)} \tag{36.76}$$
$$\phi(\mathbf X;\mu,m,p,\tau)=\phi_{Z\to Y}-\phi_{Z\to A}\times\tau \tag{36.77}$$
- Two stages: (1) fit $\hat\mu,\hat m,\hat p$ by supervised learning ($\hat\mu$ by mean squared error; $\hat m$ and $\hat p$ by cross-entropy). (2) $\hat\tau^{\mathrm{LATE}}$ solves $\frac1n\sum_i\phi(\mathbf X_i;\hat\mu,\hat m,\hat p,\hat\tau)=0$, i.e.
$$\hat\tau^{\mathrm{LATE}}=\frac{\frac1n\sum_i\phi_{Z\to Y}(\mathbf X_i;\hat\mu,\hat p)}{\frac1n\sum_i\phi_{Z\to A}(\mathbf X_i;\hat m,\hat p)} \tag{36.78}$$
  This is the double machine learning (DML) estimate of the ATE of $Z$ on $Y$ divided by that of $Z$ on $A$ (p. 1214).
- Cross-fitting (Section 36.4.2.4): split into $K$ folds. For unit $i$ in fold $k$, use $\hat\mu^{-k},\hat m^{-k},\hat p^{-k}$ fit on the other folds (p. 1214).
- Result (p. 1214–1215). Use cross-fitting and suppose:
  1. $\mathbb{E}(\hat\mu-\mu)^2\to0$, $\mathbb{E}(\hat m-m)^2\to0$, $\mathbb{E}(\hat p-p)^2\to0$.
  2. $\sqrt{\mathbb{E}[(\hat p-p)^2]}\times\big(\sqrt{\mathbb{E}[(\hat\mu-\mu)^2]}+\sqrt{\mathbb{E}[(\hat m-m)^2]}\big)=o(\sqrt n)$ (as printed; see Reading notes).
  Then, with some omitted technical conditions,
$$\sqrt n(\hat\tau^{\mathrm{LATE\text{-}cf}}-\tau^{\mathrm{LATE}})\xrightarrow{d}\mathrm{Normal}\Big(0,\frac{\mathbb{E}[\phi(\mathbf X;\mu,m,p,\tau^{\mathrm{LATE}})^2]}{\mathbb{E}[m(1,X)-m(0,X)]^2}\Big) \tag{36.79}$$
- The product of the error in $p$ with the errors in $\mu,m$ matters. A very good model of instrument assignment ($p$) can compensate for errors in $m$ and $\mu$ (p. 1215).
- Variance:
$$\hat\tau_{Z\to A}=\frac1n\sum_i\phi_{Z\to A}(\mathbf X_i;\hat m,\hat p) \tag{36.80}$$
$$\hat{\mathbb V}[\hat\tau^{\mathrm{LATE}}]=\frac{1}{\hat\tau_{Z\to A}^2}\frac1n\sum_i\phi(\mathbf X_i;\hat\mu,\hat m,\hat p,\hat\tau^{\mathrm{LATE}})^2 \tag{36.81}$$
$$\sqrt n(\hat\tau^{\mathrm{LATE}}-\tau^{\mathrm{LATE}})\xrightarrow{d}\mathrm{Normal}(0,\hat{\mathbb V}[\hat\tau^{\mathrm{LATE}}]) \tag{36.82}$$
  The main extra condition for the variance estimate to be valid is that all nuisance parameters converge at rate $O(n^{-1/4})$, so an excellent estimator for one cannot fully compensate for terrible ones. The condition is unnecessary in special cases such as known $p$ (randomly assigned instrument) (p. 1215).

*Intuition note.* The LATE estimator is a ratio of two double machine learning estimators (effect of $Z$ on $Y$ over effect of $Z$ on $A$). The $\sqrt n$ rate needs only a relatively weak condition on the nuisance models: what matters is the product of the error in $p$ with the errors in $\mu$ and $m$, so a very good model of one can partly make up for errors in the others.

#### 36.5.3 Two stage least squares (pp. 1215–1216)
- Linear model assumptions (as printed):
$$A_i\leftarrow\alpha_0+\alpha Z_i+\delta_AX_i+\gamma_AX_i+\xi_i^A \tag{36.83}$$
$$Y_i\leftarrow\beta_0+\beta A_i+\delta_YX_i+\gamma_YX_i+\xi_i^Y \tag{36.84}$$
- Substituting (36.83) in (36.84): $Y_i\leftarrow\tilde\beta_0+\beta\alpha Z_i+\tilde\delta X_i+\tilde\gamma X_i+\tilde\xi_i$ (36.85).
- So $\beta$ equals the coefficient $\beta\alpha$ of $Z$ in the outcome model divided by the coefficient $\alpha$ of $Z$ in the treatment model. Fit both and divide: this is **two stage least squares** (p. 1215).
- Warning: linearity is hard to satisfy. Misspecification together with weak relevance can give standard errors far too small, and so large "significant" estimates when the truth is a weak or null effect (p. 1216).

### 36.6 Difference in differences (pp. 1216–1219)
- Panel data: each unit observed at several times. Simplest case: two periods. No unit is treated in period 0 (outcome $Y_{0i}$). A subset ($A_i=1$) is treated before period 1 (outcome $Y_{1i}$). The goal is the average effect on the treated (p. 1216).
- Example (Card and Krueger): New Jersey raised its minimum wage from \$4.25 to \$5.05 on 1 April 1992; Pennsylvania did not. $Y_{0i}$ and $Y_{1i}$ are full-time employees at fast-food restaurant $i$ in February and November 1992. $A_i=1$ if in New Jersey (p. 1216).
- Classical structural equation:
$$Y_{ti}\leftarrow W_i+S_t+\tau A_i\,\mathbb I(t=1)+\xi_{ti},\quad \mathbb{E}[\xi_{ti}|W_i,S_t,A_i]=0 \tag{36.86}$$
  $W_i$ is a unit effect constant in time; $S_t$ is a time effect common to all units; both are unobserved. Everything is additive. This is **parallel trends**: absent treatment, both groups would have the same trend (pp. 1216–1217).
- Under this assumption:
$$\tau=\mathbb{E}[Y_{1i}-Y_{0i}|A=1]-\mathbb{E}[Y_{1i}-Y_{0i}|A=0] \tag{36.87}$$
  (added step: from (36.86), $Y_1-Y_0=S_1-S_0+\tau A+\xi_1-\xi_0$, since $W_i$ cancels. The conditional expectation given $A$ then differs between groups only by $\tau$, if $\mathbb{E}[S_1-S_0|A]$ is the same for both groups, which is the assumption stated next.) The estimator (p. 1217):
$$\hat\tau=\frac1{n_A}\sum_{i:A_i=1}(Y_{1i}-Y_{0i})-\frac1{n-n_A}\sum_{i:A_i=0}(Y_{1i}-Y_{0i}) \tag{36.88}$$
- The root problem is $\mathbb{E}[W_i|A_i=1]\neq\mathbb{E}[W_i|A_i=0]$ (e.g. New Jersey and Pennsylvania restaurants differ in unobserved ways). Identification assumes the time effect has no such association: $\mathbb{E}[S_{1i}-S_{0i}|A_i=1]=\mathbb{E}[S_{1i}-S_{0i}|A_i=0]$. This may be too strong: employment in Pennsylvania fell relative to New Jersey in 1993–1996, which does not contradict parallel trends in 1992 but makes it less credible (p. 1217).
- Weaker version: parallel trends only after adjusting for covariates (e.g. restaurant chain type). Expensive chains may be hit harder by a recession, and may be commoner in New Jersey (p. 1217).
- Non-parametric target. Define (pp. 1217–1218)
$$\mathrm P^{A=1}(Y|\mathrm{do}(A=a))\triangleq\int P(Y|A=a,\text{parents of }Y)\,\mathrm dP(\text{parents of }Y|A=1) \tag{36.89}$$
$$\mathbb E^{A=1}[Y|\mathrm{do}(A=a)]\triangleq\mathbb E_{\mathrm P^{A=1}(Y|\mathrm{do}(A=a))}[Y] \tag{36.90}$$
  The usual do-operator replaces $P(\text{parents}|A=a)$ by $P(\text{parents})$. Here it is replaced by $P(\text{parents}|A=1)$, which still breaks back-door associations but targets the treated.
- Assume the graph in Figure 36.6 ($X$ and $U$ affect the difference $Y_1-Y_0$; $A$ affects it; $U$ is statistically dependent on $A$). The estimand and the assumption are:
$$\mathrm{ATT}^{\mathrm{DiD}}=\mathbb E^{A=1}[Y_1-Y_0|\mathrm{do}(A=1)]-\mathbb E^{A=1}[Y_1-Y_0|\mathrm{do}(A=0)] \tag{36.91}$$
$$\text{conditional parallel trends:}\quad\mathbb E^{A=1}[Y_1-Y_0|X,\mathrm{do}(A=0)]=\mathbb E[Y_1-Y_0|X,A=0] \tag{36.92}$$
  Meaning: had New Jersey not raised its wage, McDonald's in New Jersey would show the same expected employment change as McDonald's in Pennsylvania (p. 1218).
- **Theorem 5.** Observe $A,Y_0,Y_1,X\sim P$. Suppose (1) the data follow Figure 36.6; (2) conditional parallel trends (36.92); (3) overlap: $P(A=1)>0$ and $P(A=1|X=x)<1$ for all $x$. Then $\mathrm{ATT}^{\mathrm{DiD}}=\tau^{\mathrm{DiD}}$ with
$$\tau^{\mathrm{DiD}}=\mathbb E\big[\mathbb E[Y_1-Y_0|A=1,X]-\mathbb E[Y_1-Y_0|A=0,X]\,\big|\,A=1\big] \tag{36.93}$$
- Proof (p. 1219). $\mathbb E^{A=1}[Y_1-Y_0|\mathrm{do}(A=1),X]=\mathbb E[Y_1-Y_0|A=1,X]$ (36.94), a near-tautology. $\mathbb E^{A=1}[Y_1-Y_0|\mathrm{do}(A=0),X]=\mathbb E[Y_1-Y_0|A=0,X]$ (36.95) is conditional parallel trends. Overlap makes the conditional expectations well defined.

#### 36.6.1 Estimation (p. 1219)
- Let $\tilde Y=Y_1-Y_0$. The target is $\mathbb E[\mathbb E[\tilde Y|A=1,X]-\mathbb E[\tilde Y|A=0,X]\,|\,A=1]$. This is the observational estimand of adjustment for the ATT (Section 36.4.5.3). The causal argument differs, but the statistical task is the same, so outcome modelling, propensity methods and DML all apply.
- Recipe: fit $\hat Q(a,x)$ for $\tilde Y$ and/or $\hat g(x)$ for $A$; compute $\hat Q(0,x_i),\hat Q(1,x_i),\hat g(x_i)$; combine into an ATT estimate with any estimator valid for adjustment.

### 36.7 Credibility checks (pp. 1219–1228)
- Whether an estimate is right depends on identification assumptions, model quality and sampling variability. The last two are familiar (held-out performance, confidence intervals). Assumptions checkable from data (overlap, relevance) must be checked. Assumptions not checkable from data (no unobserved confounding, exclusion, conditional parallel trends) need substantive knowledge. Two supplementary tools follow (pp. 1219–1220).

#### 36.7.1 Placebo checks (p. 1220)
- *Null treatment:* find a "treatment" known to have no effect but confounded like the real one. Example: HPV vaccination as a placebo for COVID vaccination. If the identification strategy is valid, the same procedure on HPV should give $\hat\tau\approx0$ (the confidence interval should contain 0). If not, suspect leftover confounding.
- *Null outcome:* an outcome known to be unaffected by the treatment but sharing confounders with the true outcome. Example: symptomatic COVID within 7 days of vaccination. If the interval excludes 0, doubt the analysis.

#### 36.7.2 Sensitivity analysis to unobserved confounding (pp. 1221–1228)
- Setting: binary treatment, adjustment (Section 36.4). "No unobserved confounding" is untestable, and its violation may explain the association in whole or in part (p. 1221).
- Motivation: a large estimated effect should survive mild confounding. Cornfield et al. showed that, for a particular dataset, a hormone explaining the smoking–lung cancer association would need to increase the probability of smoking by at least a factor of nine, which is unreasonable, so they concluded the effect is unlikely to be explained away. We need a general procedure that translates judgments of confounding strength into judgments of bias (p. 1221).
- **Imbens' sensitivity model** (binary unobserved $U$; sig is the sigmoid) (p. 1221):
$$U_i\overset{\text{iid}}\sim\mathrm{Bern}(1/2) \tag{36.96}$$
$$A_i|X_i,U_i\overset{\text{ind}}\sim\mathrm{Bern}(\mathrm{sig}(\gamma X_i+\alpha U_i)) \tag{36.97}$$
$$Y_i|X_i,A_i,U_i\overset{\text{ind}}\sim\mathcal N(\tau A_i+\beta X_i+\delta U_i,\sigma^2) \tag{36.98}$$
  The analyst judges plausible $\alpha=\alpha^*$ (effect of $U$ on treatment) and $\delta=\delta^*$ (effect on outcome). Then the other parameters can be estimated, giving $\hat\tau(\alpha^*,\delta^*)$. Drawback: it is a parametric model of the full data, forbidding neural networks or random forests for the observed data (pp. 1221–1222).
- **Austen plots** (Veitch and Zaveri): a simple, interpretable model for the confounder's influence, with no constraints on the model for observed data. Two ideas borrowed from Imbens: sensitivity parameters on a standardized unitless scale, so they can be compared with observed covariates; and plotting the curve of all parameter values giving a fixed bias. This changes the question from "what values are plausible?" to "are values this extreme plausible?" (pp. 1222–1223).
- Figure 36.7 (p. 1222–1223): effect of combination blood-pressure medication on diastolic blood pressure, bias level 2 (equal to the nominal ATE), outcome by Bayesian Additive Regression Trees, treatment by logistic regression. An unobserved confounder as strong as age could induce bias about 2, but no other observed covariate or group has that much influence. If an expert thinks such a confounder is unlikely, the treatment is likely effective. If plausible, the study fails to establish efficacy.
- **Setup** (p. 1223). Data $(Y_i,A_i,X_i,U_i)\overset{\text{iid}}\sim P$, $U$ unobserved. Under no unobserved confounding the ATE equals
$$\tau=\mathbb E[\mathbb E[Y|X,A=1]-\mathbb E[Y|X,A=0]] \tag{36.99}$$
  With confounding, $\tau\neq$ ATE. The task splits into statistical estimation of $\tau$ and the causal task of assessing $\text{bias}=\text{ATE}-\tau$. This is bias from causal misidentification, not statistical bias of the estimator, and the analysis should not constrain $\hat Q,\hat g,\hat\tau$.
- **Sensitivity model** (pp. 1223–1224). Imbens' form: $\mathrm{logit}\,P(A=1|x,u)=h(x)+\alpha u$ (36.100), $\mathbb E[Y|a,x,u]=l(a,x)+\delta u$ (36.101). Solving (36.100) for $u$ and substituting shows this equals $\mathbb E[Y|t,x,u]=\tilde l(t,x)+\tilde\delta\,\mathrm{logit}P(A=1|x,u)$. So $u$ affects the outcome only through the propensity score, and we can posit a distribution for the propensity directly, avoiding $U$ and $h$.
  - Definition 36.7.1: $\tilde g(x,u)=P(A=1|x,u)$.
  - Austen model:
$$\tilde g(X,U)|X\sim\mathrm{Beta}\big(g(X)(1/\alpha-1),(1-g(X))(1/\alpha-1)\big) \tag{36.103}$$
$$A|X,U\sim\mathrm{Bern}(\tilde g(X,U)) \tag{36.104}$$
$$\mathbb E[Y|A,X,U]=Q(A,X)+\delta\big(\mathrm{logit}\,\tilde g(X,U)-\mathbb E[\mathrm{logit}\,\tilde g(X,U)|A,X]\big) \tag{36.105}$$
  - $\alpha$ near 0: $\tilde g$ concentrates near $g(X)$ and $U$ has little influence. $\alpha$ near 1: $\tilde g$ concentrates near 0 and 1, so $U$ would predict treatment well. Also $\alpha=\mathbb E[\tilde g(X,U)|A=1]-\mathbb E[\tilde g(X,U)|A=0]$ (36.102) (p. 1224).
  - By construction $P(A=1|X)=\mathbb E[\tilde g|X]=g(X)$ and $\mathbb E[Y|A,X]=Q(A,X)$, so the observed-data $g$ and $Q$ are unchanged. Sensitivity parameters: $\alpha$ (to treatment), $\delta$ (to outcome) (p. 1224).
- **Bias** (p. 1224). With $X,U$ identifying the ATE, plugging in the model gives
$$\mathrm{ATE}=\mathbb E[Q(1,X)-Q(0,X)]+\delta\big(\mathbb E[\mathrm{logit}\,\tilde g|X,A=1]-\mathbb E[\mathrm{logit}\,\tilde g|X,A=0]\big)$$
  The first term is $\tau$, so bias is $\delta$ times the bracket. Beta-Bernoulli conjugacy, standard Beta identities and $\psi(x+1)-\psi(x)=1/x$ ($\psi$ the digamma function) give:
- **Theorem 6.** Under (36.105),
$$\mathrm{bias}=\frac{\delta}{1/\alpha-1}\,\mathbb E\Big[\frac1{g(X)}+\frac1{1-g(X)}\Big]$$
  (the text layer garbles the closing bracket; in the page image the right side is $\mathbb E[\cdot]$ of the sum). More extreme propensity scores give more bias. Hence conditioning on a covariate that affects treatment but not the outcome directly (an instrument) increases bias from unobserved confounding: **z-bias** (p. 1225).
- **Sensitivity parameters** (p. 1225). Because the scale of $\delta$ is not fixed, outcome strength is re-expressed as a non-parametric partial $R^2$:
$$R^2_{Y,\mathrm{par}}(\alpha,\delta)=1-\frac{\mathbb E(Y-\mathbb E[Y|A,X,U])^2}{\mathbb E(Y-Q(A,X))^2}$$
  - **Theorem 7:**
$$R^2_{Y,\mathrm{par}}(\alpha,\delta)=\delta^2\sum_{a=0}^1\frac{\mathbb E\big[\psi_1\big(g(X)^a(1-g(X))^{1-a}(1/\alpha-1)+\mathbb 1[A=a]\big)\big]}{\mathbb E[(Y-Q(A,X))^2]}$$
  with $\psi_1$ the trigamma function (proof in Veitch and Zaveri).
  - **Theorem 8:** $\alpha=1-\dfrac{\mathbb E[\tilde g(X,U)(1-\tilde g(X,U))]}{\mathbb E[g(X)(1-g(X))]}$. So $\alpha$ measures how much more extreme propensity scores become when conditioning on $U$.
  - Equivalently $\alpha=R^2_{A,\mathrm{par}}=1-\mathbb E[(A-\tilde g(X,U))^2]/\mathbb E[(A-g(X))^2]$ (36.106), the partial coefficient of determination of $U$ on $A$ (pp. 1225–1226).
  - Theorems 6 and 7 together give bias in terms of $\alpha$ and $R^2_{Y,\mathrm{par}}$. In practice fit $\hat Q,\hat g$ and replace expectations by data means (p. 1226).
- **Calibration with observed data** (36.7.2.1, p. 1226). For an observed covariate $Z$ given $X\backslash Z$:
$$R^2_{Y\cdot Z|T,X\backslash Z}\triangleq1-\frac{\mathbb E(Y-Q(A,X))^2}{\mathbb E(Y-\mathbb E[Y|A,X\backslash Z])^2}$$
  estimated by also fitting $\hat Q_Z$ without $Z$ and replacing expectations by sample means. For treatment, fit $g_{X\backslash Z}(X\backslash Z)=P(A=1|X\backslash Z)$ and use
$$\hat\alpha_{Z|X\backslash Z}=1-\frac{\frac1n\sum_i\hat g(x_i)(1-\hat g(x_i))}{\frac1n\sum_i\hat g_{X\backslash Z}(x_i\backslash z_i)(1-\hat g_{X\backslash Z}(x_i\backslash z_i))}$$
  Group redundant or related covariates (e.g. income, location, race as "socioeconomic variables"), otherwise each looks unimportant.
- **Practical use** (36.7.2.2, p. 1227): (1) estimate $\hat\tau$ with any tools, plus $\hat g,\hat Q$; (2) choose a bias level that would change the conclusion (e.g. the lower end of a 95% interval); (3) plot the $(\alpha,R^2_{Y,\mathrm{par}})$ pairs giving that bias, using Theorems 6–7 (the black curve); (4) compute reference influence for (groups of) observed covariates using reduced models. Only the model fitting needs doing by hand.
- Limits (p. 1227): Equation (36.105) implicitly imposes a parametric assumption on the structural relation of $U$ to $A,Y$, not justified on substantive grounds. So Austen plots only informally guide experts and do not replace thorough adjustment. Other sensitivity models allow any machine-learning model but are not routine; Austen plots are chosen for ease of understanding. They are best when the conclusion is obvious to an expert (e.g. socioeconomic status too weak to change the conclusion in Figure 36.7). They should not support nuanced claims such as "latent confounder at most 90% as strong as age, so a small non-zero effect".
- **Caution on calibration** (p. 1228). The analysis conditions on $X$, but the dots condition on $X\backslash Z$ (the other covariates). **Cinelli and Hazlett's example:** $Z$ and $U$ identical in the true model, yet the influence of $U$ given $A,X$ is larger than that of $Z$ given $A,X\backslash Z$. So "$U$ is like $Z$, the dot is below the line, so $U$ cannot undo the conclusion" is not justified. If $U$ and $Z$ are independent and both strongly affect $A$ and $Y$, conditioning on $A$ (a collider) creates interaction between them. Be skeptical when a strong confounder is expected to be omitted. The practical importance is unclear. If $U$ and $Z$ are dependent (e.g. race and wealth), omitting $U$ should raise $Z$'s apparent importance, which is conservative.

*Intuition note.* We cannot test for a hidden confounder, but we can ask how strong it would have to be to erase the result, and compare that with strengths we can measure for real covariates. The answer is a guide for experts, not a proof.

### 36.8 The do-calculus (pp. 1228–1231)
- Confounder adjustment needs only the graph (plus overlap). IV and DiD also need functional-form assumptions. The question: when can the graph alone identify effects? The **do-calculus** [Pea09c] is three rewrite rules that turn interventional expressions like $P(Y|\mathrm{do}(A=a))$ into observational ones when identification is possible (p. 1228).

#### 36.8.1 The three rules (p. 1229)
Let $X,Y,Z,W$ be disjoint sets of variables in DAG $G$. $G_{\overline X}$ cuts edges into $X$; $G_{\underline Z}$ cuts edges out of $Z$.
- **Rule 1** (insert/delete observations):
$$p(y|\mathrm{do}(x),z,w)=p(y|\mathrm{do}(x),w)\ \text{ if }(Y\perp Z|X,W)_{G_{\overline X}} \tag{36.107}$$
  It follows from d-separation in the mutilated graph.
- **Rule 2** (replace $\mathrm{do}(z)$ by seeing $z$):
$$p(y|\mathrm{do}(x),\mathrm{do}(z),w)=p(y|\mathrm{do}(x),z,w)\ \text{ if }(Y\perp Z|X,W)_{G_{\overline X\underline Z}} \tag{36.108}$$
  Simplest case: if $Z$ is a root, $p(y|\mathrm{do}(z))=p(y|z)$. Intuitively, we can replace $\mathrm{do}(z)$ by $z$ when there are no back-door paths between $z$ and $y$.
- **Rule 3** (insert/delete actions):
$$p(y|\mathrm{do}(x),\mathrm{do}(z),w)=p(y|\mathrm{do}(x),w)\ \text{ if }(Y\perp Z|X,W)_{G_{\overline X\,\overline{Z^*}}} \tag{36.109}$$
  where $Z^*$ is the set of $Z$-nodes that are not ancestors of any $W$-node in $G_{\overline X}$.

#### 36.8.2 Revisiting backdoor adjustment (pp. 1229–1230)
- If $X$ are all parents of $A$ (discrete):
$$p(Y{=}y|\mathrm{do}(A{=}a))=\sum_xp(y|x,\mathrm{do}(A{=}a))\,p(x|\mathrm{do}(A{=}a)) \tag{36.110}$$
$$=\sum_xp(y|x,A{=}a)\,p(x) \tag{36.111}$$
  The first line is marginalization. In the second, $p(x|\mathrm{do}(A=a))=p(x)$ (rule 3: $A$ does not affect $X$), and $p(y|x,\mathrm{do}(A=a))=p(y|x,A=a)$ (rule 2: parents block all non-directed paths).
- **Back-door criterion:** a set $S$ with (1) no node a descendant of $A$ and (2) $S$ blocks every back-door path (paths between $A$ and $Y$ with an arrow into $A$). Then
$$p(Y{=}y|\mathrm{do}(A{=}a))=\mathbb E_S[p(Y{=}y|S,A{=}a)] \tag{36.112}$$
  proved by rules 3 and 2 as above. Excluding descendants avoids conditioning on mediators or colliders. Both the parents and the common causes of $A$ satisfy the criterion. With $\tau=\mathbb E_S[\mathbb E[Y|A=1,S]-\mathbb E[Y|A=0,S]]$, ATE $=\tau$ whenever $S$ satisfies the criterion, and Section 36.4 methods apply with $S$ in place of $X$ (p. 1230).

#### 36.8.3 Frontdoor adjustment (pp. 1230–1231; the unit ends mid-derivation)
- Figure 36.8: $U\to A$, $U\to Y$, $A\to M\to Y$; the effect of $A$ on $Y$ is entirely mediated by $M$ (p. 1230).
- If all **mediators** $M$ (variables on every directed path from $A$ to $Y$) are observed and have no unobserved common cause with $A$ or $Y$, identification is possible. The author says both the effect of $A$ on $M$ and the effect of $M$ on "A" are identified by back-door adjustment (the second is presumably $M$ on $Y$; see Reading notes). Combining (p. 1231):
$$p(Y|\mathrm{do}(A{=}a))=\sum_mp(Y|\mathrm{do}(M{=}m))\,p(M{=}m|\mathrm{do}(A{=}a)) \tag{36.113}$$
$$=\sum_m\sum_{a'}p(Y|a',m)\,p(a')\,p(m|a) \tag{36.114}$$
  The second line is back-door adjustment for each do-term ($A$ blocks the $M$–$Y$ back-door path through $U$). (36.114) is the **front-door formula**.
- **Front-door criterion** for $M$ relative to $(A,Y)$: (1) $M$ intercepts all directed paths from $A$ to $Y$; (2) no unblocked back-door path from $A$ to $M$; (3) all back-door paths from $M$ to $Y$ are blocked by $A$. If $M$ satisfies it and $p(A,M)>0$ for all values, the effect is identifiable via (36.114).
- Smoking example: condition 1 means smoking affects cancer only via tar and tissue damage; conditions 2–3 mean genotype $U$ affects $M$ only via smoking; $p(A,M)>0$ means high tar must also arise from other factors (e.g. pollutants), so $p(A=0,M=1)>0$. The do-calculus derivation of the criterion begins at the end of the unit and is not covered here.

## Toy example (ours, not from the text)
Randomized assignment $Z$ (half assigned), binary treatment $A$, binary type structure with no defiers. Population shares: compliers 0.5, always takers 0.2, never takers 0.3. Outcomes: compliers $Y=2$ untreated, $Y=6$ treated (true LATE $=4$); always takers $Y=8$; never takers $Y=1$ (they ignore the instrument, so exclusion holds).

1. $P(A=1|Z=1)=0.5+0.2=0.7$ and $P(A=1|Z=0)=0.2$. Denominator of (36.57): $0.7-0.2=0.5$.
2. $\mathbb E[Y|Z=1]=0.5\cdot6+0.2\cdot8+0.3\cdot1=3+1.6+0.3=4.9$. $\mathbb E[Y|Z=0]=0.5\cdot2+0.2\cdot8+0.3\cdot1=1+1.6+0.3=2.9$. Numerator: $2.0$.
3. $\tau^{\mathrm{LATE}}=2.0/0.5=4$, the complier effect.
4. Naive comparison of treated and untreated units, using joint masses (each $Z$ value has probability 0.5):
   - Treated: $Z{=}1$ compliers (mass 0.25, $Y=6$), $Z{=}1$ always takers (0.10, $Y=8$), $Z{=}0$ always takers (0.10, $Y=8$). Sum of $Y$ is $1.5+0.8+0.8=3.1$ over mass 0.45, mean $\approx6.89$.
   - Untreated: $Z{=}1$ never takers (0.15, $Y=1$), $Z{=}0$ compliers (0.25, $Y=2$), $Z{=}0$ never takers (0.15, $Y=1$). Sum is $0.15+0.5+0.15=0.8$ over mass 0.55, mean $\approx1.45$.
   - Naive difference $\approx5.43\ne4$: always takers have high $Y$ and self-select into treatment, i.e. confounding. The instrument ratio removes it.

## Concepts
- [[instrumental-variable]] (new) — variable $Z$ that affects $Y$ only via $A$; relevance, unconfoundedness, exclusion (p. 1209)
- [[exclusion-restriction]] (new) — all directed paths from $Z$ to $Y$ pass through $A$ (p. 1209)
- [[additive-unobserved-confounding]] (new) — $Y\leftarrow f(A,X)+f_U(U)$; no treatment–confounder interaction (p. 1210)
- [[late-complier-effect]] (new) — average effect among compliers; identified by the ratio (36.57) of observational contrasts under monotonicity (p. 1212)
- [[instrument-monotonicity]] (new) — no defiers, $P(\text{defier})=0$ (p. 1212)
- [[double-machine-learning]] (new) — score-based estimator whose $\sqrt n$ rate needs only a relatively weak condition on nuisance-model errors; used for the LATE (pp. 1214–1215)
- [[two-stage-least-squares]] (new) — fit linear $Y\sim Z$ and $A\sim Z$ models, divide the coefficients (p. 1215)
- [[difference-in-differences]] (new) — compare before/after changes between treated and untreated units (p. 1216)
- [[parallel-trends]] (new) — absent treatment, both groups would follow the same trend (conditional on $X$ in the weaker version) (pp. 1217–1218)
- [[placebo-check]] (new) — apply the method to a null treatment or null outcome; expect an effect near 0 (p. 1220)
- [[sensitivity-analysis-unobserved-confounding]] (new) — compute the bias a hypothetical confounder of given strength would cause (p. 1221)
- [[austen-plot]] (new) — curve of $(\alpha,R^2_{Y,\mathrm{par}})$ giving a fixed bias, with observed covariates as reference dots (p. 1222)
- [[z-bias]] (new) — adjusting for an instrument-like covariate amplifies unobserved-confounding bias (p. 1225)
- [[do-calculus]] (new) — three rewrite rules converting do-expressions to observational ones given a graph (p. 1228)
- [[back-door-front-door-criterion]] — graphical conditions for adjustment sets or mediators (pp. 1230–1231)
- [[do-operator]] — here also the variant $\mathbb E^{A=1}$ that uses $P(\text{parents}|A=1)$ (p. 1217)
- [[propensity-score]] — $g(x)=P(A=1|x)$; $\tilde g(x,u)$ adds the confounder (p. 1224)
- [[d-separation]] — basis of the rule conditions on mutilated graphs (p. 1229)
- [[fork-chain-collider]] — treatment as a collider when conditioning on $A$ (p. 1228)

## Canonical instances
- [[instance-random-assignment-noncompliance]] — randomized drug assignment as an instrument (pp. 1209–1210)
- [[instance-judge-fixed-effects]] — judge identity as an instrument for incarceration (p. 1210)
- [[instance-card-krueger-min-wage]] — New Jersey vs Pennsylvania fast food, DiD (p. 1216)
- [[instance-hpv-covid-placebo]] — HPV vaccine as null treatment; 7-day COVID as null outcome (p. 1220)
- [[instance-smoking-cornfield]] — hormone would need to raise smoking probability by at least a factor of nine (p. 1221)
- [[instance-blood-pressure-austen]] — Austen plot, age as reference confounder (p. 1222)
- [[instance-smoking-tar-frontdoor]] — front-door via tar and tissue damage (p. 1231)

## Bridges (candidates)
- [structural-analogy] Instrument ratio $\tau^{\mathrm{LATE}}$ ↔ econometrics: Wald estimator and 2SLS ratio of reduced-form to first-stage coefficients — the same ratio structure in linear and binary settings.
- [same-math] DiD estimation after taking $Y_1-Y_0$ ↔ adjustment-based ATT estimation (36.4.5.3) — the source says the statistical estimand is identical.
- [structural-analogy] Austen model's $\tilde g\sim\mathrm{Beta}$ with Bernoulli treatment ↔ Bayesian conjugacy: beta-Bernoulli updating gives the conditional logit expectations used in the bias formula.
- [metaphor] Placebo checks ↔ prior/posterior predictive checks: testing a model against something it should or should not predict.

## Questions this raises
- How restrictive is the additive-confounding assumption versus monotonicity, and what does LATE say about people who are not compliers?
- Can we test conditional parallel trends indirectly (e.g. with pre-period data) and what would pass or fail mean?
- How sensitive are Austen-plot conclusions to the Beta/logit form of (36.103)–(36.105) chosen for $U$?
- How does the do-calculus decide when an effect is not identifiable, rather than just finding identifying formulas?

## Reading notes
- This is part 2 of 2 of Chapter 36. It starts on printed p. 1208, in the middle of the end of Section 36.4 (the summary of practical checks), and ends on p. 1231 mid-sentence ("Assuming…") in Section 36.8.3, before the do-calculus derivation of the front-door formula. Page offset: printed = pdf − 34.
- Footer: "Probabilistic Machine Learning: Advanced Topics". Online version, December 10, 2025; MIT Press, CC-BY-NC-ND.
- Misprints seen in the images: (36.59) shows $\mathbb E[Y|\mathrm{do}(Z=1)]-\mathbb E[Y|\mathrm{do}(Z=1)]$ (same with 36.69); the context requires $Z=0$ in the second term. In 36.5.3, (36.83)–(36.84) print both $\delta X_i$ and $\gamma X_i$ terms as shown. On p. 1231 "effect of $M$ on $A$" is likely meant as $M$ on $Y$. In Theorem 6 the text layer garbles the bracket; I followed the image.
- On p. 1214, condition 2 for the DML result is printed with right side $o(\sqrt n)$. The following discussion speaks of the product of errors being small, and the printed form looks unusual. I report it as printed and do not assert a corrected form.
- Proofs of Theorems 7 and 8 are not given in the source (deferred to Veitch and Zaveri). The Theorem 6 derivation is only sketched (conjugacy and digamma identities).
