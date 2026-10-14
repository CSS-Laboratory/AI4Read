---
id: pearl-2016-primer/ch03-effects
work: pearl-2016-primer
unit: "3 The Effects of Interventions"
pages: 53–88
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
---
# The Effects of Interventions

## L0 — One line
If a causal graph is valid, the effect of setting a variable, $P(y\mid do(x))$, can often be computed from purely observational data by removing the arrows into that variable and adjusting for the right covariates.

## L1 — The gist (≤ 120 words)
Conditioning on $X=x$ only narrows attention to a subgroup. Intervening, $do(X=x)$, changes the system. The chapter asks when the effect of an intervention can be computed from data gathered without intervention. Graph surgery gives the adjustment formula. The backdoor criterion says which covariates to adjust for. The front-door criterion works even when the confounder is unmeasured. The chapter then covers conditional interventions, inverse probability weighting, and direct effects (mediation). It ends with linear systems, where regression is the main tool for finding causal path coefficients. The point is that the data alone cannot settle causal questions, such as Simpson's paradox; a causal graph is also needed.

**Prerequisites:** conditional probability and the law of total probability; DAGs, d-separation, colliders (Part One of the book); linear regression and partial regression coefficients.

## L2 — Key ideas (5–10 bullets)
- Intervening ($do$) is not conditioning. $do(X=x)$ deletes all arrows into $X$ and changes the system. Conditioning only selects a subpopulation (p. 54–55).
- Adjustment formula: $P(y|do(x))=\sum_z P(y|x,z)P(z)$. It is derived from the invariance of $P(z)$ and $P(y|x,z)$ under surgery. Given the graph, adjusting for the parents of $X$ gives the right answer (Rule 1), but they are often unmeasured. This resolves Simpson's paradox, given a graph (pp. 56–59).
- Truncated product (g-formula): write the joint distribution as a product of factors, then delete the factors of the intervened variables. This also handles several interventions (p. 60).
- Backdoor criterion: use a set $Z$ with no descendants of $X$ that blocks every path between $X$ and $Y$ that contains an arrow into $X$. Then adjust for $Z$. Sometimes $Z$ must include a collider (Fig. 3.7), but conditioning on a collider that opens a spurious path creates bias (e.g. $W$ in Fig. 2.8) (pp. 61–63).
- Front-door criterion identifies the effect through a mediator (a variable on the causal path from $X$ to $Y$), even with an unmeasured confounder, by chaining two backdoor adjustments (pp. 66–69).
- Conditional policies $do(X=g(Z))$ (treatment follows a rule based on $Z$) reduce to $z$-specific effects, i.e. effects within the subgroup $Z=z$ (Rule 2). Inverse probability weighting estimates the effect by reweighting samples with $1/P(x|z)$. It is valid only if $Z$ satisfies the backdoor criterion (pp. 70–75).
- Direct effect is defined by intervening on the mediator (the controlled direct effect, CDE), not by conditioning on it. Conditioning on a mediator can open a collider path (pp. 76–78).
- In linear Gaussian systems, structural (path) coefficients are direct effects. Total effect is a sum of products over non-backdoor paths. Regression on a backdoor set, the $G_\alpha$ rule (delete the edge $X\to Y$, then find a set that d-separates $X$ and $Y$), or an instrument (a variable d-connected to $X$ and d-separated from $Y$ in $G_\alpha$) identifies them (pp. 81–86).

## L3 — Walkthrough

### 3.1 Interventions (pp. 53–55)
- Many studies aim to predict the effect of an intervention. Randomized controlled experiments are the "golden standard", but are often impractical (weather, TV viewing, drug-trial dropouts). Researchers then use observational studies, where data are only recorded (p. 53).
- Example: a study found heavy texting correlated with "shallowness". Texting might cause shallowness, shallowness might cause texting, or a common factor might cause both. The study did not show that intervening on texting would change shallowness (p. 54).
- **Intervening vs conditioning.** To intervene is to fix a variable's value. This changes the system, and other variables may change. To condition is to restrict attention to the cases with that value. Only our perception changes, not the world (p. 54).
- Ice-cream example (Fig. 3.1): $Z$ = temperature, $X$ = ice-cream sales, $Y$ = crime; $Z\to X$, $Z\to Y$. Fixing $X$ is graph surgery: remove all edges directed into $X$ (Fig. 3.2). Then $Y$ is independent of $X$, because $X$ no longer depends on $Z$. Conditioning gives a very different dependency pattern. Conditional quantities come directly from the data. Interventional ones depend on the graph, which tells us which arrow to remove (pp. 54–55).
- **Notation.** $P(y|x)$ is the distribution of $Y$ among individuals whose $X$ is $x$. $P(y|do(x))$ is the distribution of $Y$ if everyone had $X$ fixed at $x$. $P(y|do(x),z)$ is the conditional on $Z=z$ in the distribution created by $do(x)$ (p. 55).
- Tacit assumption: the intervention has no side effects, i.e. assigning $x$ does not directly alter later variables. "Assigned" a drug may differ from being forced to take it. Side effects must be put in the model explicitly (p. 55).

### 3.2 The Adjustment Formula (pp. 55–58)
- Setting: Fig. 3.3, with $Z$ (gender) $\to X$ (drug), $Z\to Y$ (recovery), $X\to Y$. The target is the average causal effect (ACE) (pp. 55–56):
$$P(Y=1|do(X=1))-P(Y=1|do(X=0)) \tag{3.1}$$
- Causal effects cannot be computed from data without a causal story; this was the lesson of Simpson's paradox. With the graph they can be. Simulate the intervention by surgery (Fig. 3.4). Then $P(y|do(x))=P_m(y|x)$, where $P_m$ is the manipulated model. Only one table is left, so the "aggregate vs $Z$-specific" question disappears (p. 56).
- Two invariances between $P_m$ and the original $P$ (p. 56):
  1. $P_m(Z=z)=P(Z=z)$, because the process that determines $Z$ is untouched.
  2. $P_m(Y=y|Z=z,X=x)=P(Y=y|Z=z,X=x)$, because $Y=f(x,z,u_Y)$ is the same whether $X$ varies spontaneously or by manipulation.
- Also, $Z$ and $X$ are d-separated in the modified model, so $P_m(z|x)=P_m(z)=P(z)$ (p. 56).
- Derivation (pp. 56–57):
$$P(y|do(x)) = P_m(y|x)\quad\text{(by definition)}\tag{3.2}$$
$$=\sum_z P_m(y|x,z)P_m(z|x)\tag{3.3}$$
$$=\sum_z P_m(y|x,z)P_m(z)\tag{3.4}$$
$$P(y|do(x))=\sum_z P(y|x,z)P(z)\tag{3.5}$$
 (3.3) is the law of total probability. (3.4) uses the independence of $Z$ and $X$ in the modified model. (3.5) uses the two invariances. (3.5) is the **adjustment formula**, also called "adjusting for $Z$" or "controlling for $Z$". It can be estimated by filtering the data (p. 57).
- In a randomized experiment the data are already generated by a model of the Fig. 3.4 shape, so $P_m=P$ and no adjustment is needed. The derivation is thus a formal proof that randomization yields $P(y|do(x))$. In practice, adjustments are still used to reduce sampling variation (Cox 1958) (p. 57).
- **Numbers** (Simpson's drug example, Table 1.1; $X=1$ drug, $Z=1$ male, $Y=1$ recovery; population 700) (p. 57):
$$P(Y=1|do(X=1))=\tfrac{0.93(87+270)}{700}+\tfrac{0.73(263+80)}{700}=0.832$$
$$P(Y=1|do(X=0))=\tfrac{0.87(87+270)}{700}+\tfrac{0.69(263+80)}{700}=0.7818$$
$$ACE=0.832-0.7818=0.0502$$
 This is a clear advantage for drug-taking. It is the difference in the recovery fraction if everyone versus no one took the drug. The formula tells us to ignore the aggregate $P(Y=1|X=1)$ and $P(Y=1|X=0)$, which would falsely suggest a negative effect (pp. 57–58).
- **Blood-pressure version** (Fig. 3.5: $X\to Z$, $X\to Y$, $Z\to Y$, with $Z$ = blood pressure at the end of the study). The text asks how the formula copes with a case where the unconditioned table is right. $X$ has no parents, so no surgery is needed. Treatment is "as if randomized", and the formula reduces to $P(y|do(x))=P(y|x)$, adjusting for the empty set. Adjusting for blood pressure would give a wrong answer, corresponding to a model where blood pressure causes people to seek treatment (p. 58).

*Intuition note.* Surgery cuts the arrows into $X$, but the rest of the machine keeps running as before. So we average the within-group effects, weighting each group by its real share of the population, not by its share among the treated.

#### 3.2.1 To Adjust or not to Adjust? (pp. 58–59)
- Surgery neutralizes the influence of $X$'s parents, so the adjustment set should be the parents of $X$, $PA(X)$ (pp. 58–59).

**Rule 1 (Causal Effect Rule).** With $PA$ the parents of $X$:
$$P(Y=y|do(X=x))=\sum_z P(Y=y|X=x,PA=z)P(PA=z)\tag{3.6}$$
where $z$ ranges over all combinations of values of the variables in $PA$ (p. 59).

- Multiplying and dividing by $P(X=x|PA=z)$ gives
$$P(y|do(x))=\sum_z\frac{P(X=x,Y=y,PA=z)}{P(X=x|PA=z)}\tag{3.7}$$
 $P(X=x|PA=z)$ is the "propensity score" (discussed later, Sec. 3.6 here; p. 59 says Sec. 3.5) (p. 59).
- The graph is needed to identify the parents of $X$. **Interlocutor/reader temptation:** one may think that, once the parents are known, the rest of the graph can be discarded. The author says this is not so, because the parents are often unobserved. Other variables can substitute for them (p. 59).

#### 3.2.2 Multiple Interventions and the Truncated Product Rule (p. 60)
- Rule of Product Decomposition for Fig. 3.3, and the postintervention distribution for Fig. 3.4:
$$P(x,y,z)=P(z)P(x|z)P(y|x,z)\tag{3.8}$$
$$P(z,y|do(x))=P_m(z)P_m(y|x,z)=P(z)P(y|x,z)\tag{3.9}$$
 The factor $P(x|z)$ is removed because $X$ becomes parentless. Summing over $z$ returns (3.5) (p. 60).
- General rule: write the product decomposition and strike out the factors of the variables in the intervention set $\mathbf X$. This is the **truncated product formula** (g-formula):
$$P(x_1,\dots,x_n|do(\mathbf x))=\prod_i P(x_i|pa_i)\quad\text{for all }i\text{ with }X_i\text{ not in }\mathbf X.$$
- Example on the model of Fig. 2.9, setting $X=x$ and $Z_3=z_3$:
$$P(z_1,z_2,w,y|do(X=x,Z_3=z_3))=P(z_1)P(z_2)P(w|x)P(y|w,z_3,z_2)$$
 The factors $P(x|z_1,z_3)$ and $P(z_3|z_1,z_2)$ are deleted (p. 60).
- Combining (3.8) and (3.9) (p. 61):
$$P(z,y|do(x))=\frac{P(x,y,z)}{P(x|z)}\tag{3.10}$$
 So $P(x|z)$ is all we need beyond the observational distribution.

*Intuition note.* Each variable in the model has its own "rule" (its factor). An intervention overrides the rule for the intervened variable and leaves the other rules untouched.

### 3.3 The Backdoor Criterion (pp. 61–64)
- Question: when does the graph make a causal effect computable from passive observations, when $X$ has unmeasured parents? The backdoor criterion is the main tool (p. 61).

**Definition 3.3.1 (Backdoor).** For an ordered pair $(X,Y)$ in a DAG $G$, a set $Z$ satisfies the backdoor criterion if no node in $Z$ is a descendant of $X$, and $Z$ blocks every path between $X$ and $Y$ that contains an arrow into $X$ (p. 61).

- If $Z$ satisfies it, $P(y|do(x))=\sum_z P(y|x,z)P(z)$, just as for $PA(X)$. $PA(X)$ always satisfies the criterion (p. 61).
- Three aims: (1) block all spurious paths; (2) leave directed paths $X\to\cdots\to Y$ unperturbed; (3) create no new spurious paths. Backdoor paths are blocked for (1). Descendants of $X$ are excluded for (2), because they would be affected by an intervention on $X$ and might affect $Y$. Colliders that would unblock a new path are avoided for (3). The descendant rule also prevents conditioning on children of intermediate nodes (p. 62).
- **Example, Fig. 3.6:** $Z$ (socioeconomic status, unmeasured) $\to X$ and $Z\to W$; $W$ (weight) $\to Y$; $X\to Y$. $W$ is not a descendant of $X$ and blocks $X\leftarrow Z\to W\to Y$, so $W$ satisfies the criterion. Adjust: $P(y|do(x))=\sum_w P(y|x,w)P(w)$, estimable if $W$ is observed (p. 62).
- **Fig. 2.8:** there are no backdoor paths from $X$ to $Y$, so the empty set works and $P(y|do(x))=P(y|x)$. Adjusting for the collider $W$ would open the spurious path $X\to W\leftarrow Z\leftarrow T\to Y$, and bias the result (pp. 62–63).
- **W-specific effect in Fig. 2.8** (e.g. only patients without posttreatment pain). Conditioning on $W=w$ opens that path, but we can block it with $T$. As printed (p. 63):
$$P(Y=y|do(X=x),W=w)=\sum_t P(y|x,w,t)\,P(T=t|X=x,W=w)\tag{3.11}$$
- **Effect modification (moderation):** how much the effect of $X$ on $Y$ changes across values of $W$. It requires comparing $P(y|do(x),w)$ and $P(y|do(x),w')$. In Fig. 3.6, $W$ satisfies the criterion, so one compares $P(y|x,w)$ with $P(y|x,w')$ directly. If $W$ alone does not satisfy it but $T\cup W$ does, one adjusts for $T$ as in (3.11) (p. 63).
- **Colliders sometimes must be adjusted for (Fig. 3.7).** There are four backdoor paths, all through $Z$; $Z$ is a collider on $X\leftarrow E\to Z\leftarrow A\to Y$. To block all backdoor paths one needs $\{E,Z\}$, $\{A,Z\}$, or $\{E,Z,A\}$. All contain $Z$ (p. 63).
- Different valid adjustment sets must give the same $P(y|do(x))$. In Fig. 3.6: $\sum_w P(y|x,w)P(w)=\sum_z P(y|x,z)P(z)$. Uses: (1) we may choose the cheaper or more reliable set; (2) the equality is a testable constraint when all variables are observed. A model that implies it can be discarded if the data violate it (p. 64).
- Study questions 3.3.1–3.3.3 (pp. 64–66): see Exercises.

*Intuition note.* Think of three jobs: close all "back doors" through which confounding flows, keep the front door (the causal paths) open, and do not accidentally open a new window by conditioning on a collider or on something downstream of $X$.

### 3.4 The Front-Door Criterion (pp. 66–69)
- Smoking ($X$) and lung cancer ($Y$). In the years before 1970, the tobacco industry said an unobserved genotype $U$ could cause both. In Fig. 3.10(a), $U\to X$, $U\to Y$, $X\to Y$. With $U$ unobserved there is no backdoor set, and the effect is not identifiable (p. 66).
- Fig. 3.10(b) adds tar deposits $Z$: $X\to Z\to Y$, $U\to X$, $U\to Y$. Still no backdoor set, but the effect is identifiable by two consecutive backdoor applications (p. 66).
- **Data (Table 3.1, thousands; 800 subjects at high cancer risk).** Tar group (400): smokers 380, nonsmokers 20. No-tar group (400): smokers 20, nonsmokers 380. Cancer rates are: tar, smokers 15% (57/380), nonsmokers 95% (19/20); no tar, smokers 10% (2/20), nonsmokers 90% (342/380); overall, smokers 15% (59/400), nonsmokers 90.25% (361/400) (p. 67).
- **Tobacco industry's reading:** the table shows smoking is beneficial. Smokers have 15% cancer versus 90.25%, and smokers do better within both tar groups. The author says these numbers are obviously contrary to empirical observations and show that observations are not to be trusted (p. 67).
- **Antismoking lobby's reading:** smoking raises tar with probability 95% (380/400) versus 5% (20/400). Within smokers, tar raises cancer from 10% to 15%. Within nonsmokers, it raises cancer from 90% to 95% (Table 3.2). So avoiding smoking avoids tar's harm, whatever one's genotype (pp. 67–68).
- **The graph decides.** Steps (p. 68):
$$P(Z=z|do(X=x))=P(Z=z|X=x)\tag{3.12}$$
 (no backdoor path $X$ to $Z$).
$$P(Y=y|do(Z=z))=\sum_x P(Y=y|Z=z,X=x)P(X=x)\tag{3.13}$$
 (the backdoor path $Z\leftarrow X\leftarrow U\to Y$ is blocked by conditioning on $X$). Chain them: if nature sets $Z=z$, then $Y$ has probability $P(y|do(z))$. Given that we set $X=x$, nature does so with probability $P(z|do(x))$. Sum over $z$:
$$P(y|do(x))=\sum_z P(y|do(z))P(z|do(x))\tag{3.14}$$
 Substituting (3.12) and (3.13), with index $x'$ in the inner sum:
$$P(y|do(x))=\sum_z\sum_{x'}P(y|z,x')P(x')P(z|x)\tag{3.15}$$
 This is the **front-door formula**. Applied to Table 3.1, the author concludes that the tobacco industry was wrong: tar deposits make cancer more likely, and smoking increases tar. (Added step: taking $Y=1$ as cancer and $P(X=1)=0.5$, (3.15) gives $P(Y{=}1|do(X{=}1))=0.95\cdot0.55+0.05\cdot0.50=0.5475$ and $P(Y{=}1|do(X{=}0))=0.05\cdot0.55+0.95\cdot0.50=0.5025$, so smoking raises cancer risk by 0.045, using the Table 3.1 rates.) (p. 68)
- The author says real data would show a positive smoking–cancer correlation. The estimand (3.15) could then confirm and quantify the harm (p. 68).

**Definition 3.4.1 (Front-Door).** A set $Z$ satisfies the front-door criterion relative to $(X,Y)$ if (1) $Z$ intercepts all directed paths from $X$ to $Y$; (2) there is no backdoor path from $X$ to $Z$; (3) all backdoor paths from $Z$ to $Y$ are blocked by $X$ (p. 69).

**Theorem 3.4.1.** If $Z$ satisfies the front-door criterion relative to $(X,Y)$ and $P(x,z)>0$, then the causal effect is identifiable:
$$P(y|do(x))=\sum_z P(z|x)\sum_{x'}P(y|x',z)P(x')\tag{3.16}$$
- Conditions (2) and (3) are "overly conservative": some excluded paths can be allowed if blocked by other variables. The do-calculus, which finds all identifiable effects, is beyond the book's scope (p. 69).

*Intuition note.* We cannot measure the hidden confounder, but we can measure how smoking changes tar (clean, no confounding) and how tar changes cancer (confounding blocked by holding smoking fixed). Multiplying the two stages gives the total effect.

### 3.5 Conditional Interventions and Covariate-Specific Effects (pp. 70–71)
- Interventions can be dynamic policies: $X$ responds to $Z$ via $x=g(z)$ or stochastically via $P^*(x|z)$. Example: give the drug only if temperature exceeds a level. Written $do(X=g(Z))$ (p. 70).
- The **$z$-specific effect** $P(y|do(x),z)$ is the distribution of $Y$ in the subset where $Z$ takes the value $z$ after the intervention (p. 70).

**Rule 2.** $P(y|do(x),z)$ is identified whenever we can measure a set $S$ such that $S\cup Z$ satisfies the backdoor criterion. Then
$$P(y|do(x),z)=\sum_s P(y|x,s,z)P(s|z)$$
(pp. 70–71).

- Differences from (3.5): the adjustment set is $S\cup Z$, and the sum runs only over $S$. If $Z\subseteq S$, then $S\cup Z=S$. This criterion is somewhat stricter than for the nonspecific effect: adding $Z$ may open paths, e.g. if $Z$ is a collider (p. 71).
- Conditional policies: condition on $Z=z$:
$$P(y|do(X=g(Z)))=\sum_z P(y|do(X=g(Z)),z)P(z|do(X=g(Z)))=\sum_z P(y|do(X=g(z)),z)P(z)\tag{3.17}$$
 using $P(z|do(X=g(Z)))=P(z)$, since $Z$ occurs before $X$. Equivalently, substitute $g(z)$ for $x$ in the $z$-specific effect and average over the observed $P(z)$ (p. 71).

### 3.6 Inverse Probability Weighing (pp. 72–75)
- Problem: adjustment needs a sum over all strata of $Z$. With many variables and values, this is heavy, and cells may have too few samples (p. 72).
- Solution, given a reliable estimate of the propensity score $g(x,z)=P(X=x|Z=z)$ (e.g. by fitting a flexible function to data): generate artificial samples that act as if drawn from $P_m$, then count frequencies of $Y=y$ in each stratum $X=x$. "Nature does the summation" (p. 72).
- Conditioning, as filtering and renormalizing, multiplies each surviving case by $1/P(X=x)$ (Bayes' rule) (pp. 72–73). Under $do(x)$, multiply and divide the adjustment formula by the propensity score and use that $P(y|x,z)P(x|z)P(z)$ is the pre-intervention joint:
$$P(y|do(x))=\sum_z\frac{P(Y=y,X=x,Z=z)}{P(X=x|Z=z)}$$
 Each case $(y,x,z)$ has its probability boosted by $1/P(X=x|Z=z)$. This is inverse probability weighting. Weighting each sample by $1/P(X=x|Z=z)$ lets us treat it as if generated from $P_m$ (p. 73).
- **Worked example** (Table 3.3, joint probabilities $(x,y,z)$): Yes/Yes/Male 0.116; Yes/Yes/Female 0.274; Yes/No/Male 0.009; Yes/No/Female 0.101; No/Yes/Male 0.334; No/Yes/Female 0.079; No/No/Male 0.051; No/No/Female 0.036 (p. 73).
  - Conditioning on $X=$ yes: $P(X=yes)=0.116+0.274+0.01+0.101=0.501$, so weights are boosted by $1/0.501=2.00$ (Table 3.4: 0.231, 0.549, 0.017, 0.203) (p. 74).
  - Propensity scores: $P(X{=}yes|Male)=\frac{0.116+0.01}{0.116+0.01+0.334+0.051}=0.247$ and $P(X{=}yes|Female)=\frac{0.274+0.101}{0.274+0.101+0.079+0.036}=0.765$. Multiply gender-matching rows by $1/0.247$ and $1/0.765$ (Table 3.5: 0.475, 0.358, 0.035, 0.132). Then $P(Y=yes|do(X=yes))=0.476+0.357=0.833$ (p. 74).
- Three cautions (p. 75):
  1. The reweighting is discriminatory: Row 1 grows from 0.116 to 0.476 (factor 4.1), Row 2 from 0.274 to 0.357 (factor 1.3). This makes $X$ independent of $Z$, as in a randomized trial.
  2. This example saves no computation. The savings appear when $Z$ has thousands or millions of values and samples number in the hundreds, because then the cells met equal the number of samples.
  3. The method is valid only when the $Z$ in $1/P(x|z)$ satisfies the backdoor criterion. Otherwise it may introduce more bias than naive conditioning.
- Unbiasedness (convergence to the true effect with unlimited samples) is the chapter's focus, but precision also matters (variability with finite samples; shorter confidence intervals). Example: if $Z$ makes extreme values of a continuous $X$ most common, weighting down-weights those and focuses on middle values. A regression on the reweighted data (Sec. 3.8) would then be very imprecise, and other estimation strategies are sought (p. 75).

*Intuition note.* Reweighting makes rare combinations count more. People who got their treatment despite a low chance of it stand in for those who would have got it under a randomized rule. The reweighted population looks as if $X$ had been assigned independently of $Z$.

### 3.7 Mediation (pp. 75–78)
- Effects can be direct and mediated. In the blood-pressure example, treatment is a direct (negative) cause of recovery and an indirect (positive) cause via blood pressure. Separating them has been difficult (pp. 75–76).
- Example: gender ($X$) and hiring ($Y$) with qualifications $Z$ as mediator (Fig. 3.11: $X\to Z\to Y$, $X\to Y$). Traditionally one conditions on $Z$: if $P(\text{Hired}|\text{Female},\text{Highly Qualified})\ne P(\text{Hired}|\text{Male},\text{Highly Qualified})$, there is a direct effect. This is correct in Fig. 3.11 (p. 76).
- If income confounds qualification and hiring (Fig. 3.12: $I\to Z$, $I\to Y$), conditioning on $Z$ is conditioning on a collider. Conditioning opens $X\to Z\leftarrow I\to Y$. Not conditioning leaves $X\to Z\to Y$. Either way the direct effect is not obtained. Traditional statistics abandoned many such problems (p. 76).
- Fix: hold $Z$ constant by intervening, not conditioning. **Controlled direct effect** of changing $X$ from $x$ to $x'$ (p. 77):
$$CDE=P(y|do(x),do(z))-P(y|do(x'),do(z))\tag{3.18}$$
 It works even when $Z\to Y$, $X\to Z$, $X\to Y$ are confounded. It may differ across values of $z$ (e.g. discrimination against women in high-qualification jobs but against men in low-qualification jobs), so compute it for each relevant $z$. In linear models this is not necessary (Sec. 3.8) (p. 77).
- **Estimation in Fig. 3.12** (p. 77): no backdoor path from $X$ to $Y$, so replace $do(x)$ by conditioning on $x$: $P(y|x,do(z))-P(y|x',do(z))$. Backdoor paths from $Z$ to $Y$: via $X$ (blocked by conditioning on $X$) and via $I$ (blocked by adjusting for $I$):
$$\sum_i\big[P(y|x,z,i)-P(y|x',z,i)\big]P(i)$$
 This is do-free, so it can be estimated from nonexperimental data.
- **General identification.** The CDE is identifiable if (1) a set $S_1$ blocks all backdoor paths from $Z$ to $Y$; and (2) a set $S_2$ blocks all backdoor paths from $X$ to $Y$ after deleting all arrows entering $Z$. Condition 2 is not necessary in randomized trials or when $X$ is exogenous ("as if" randomized) (pp. 77–78).
- **Indirect effect** is harder, since the direct effect cannot be conditioned away. Total minus direct may work in linear systems. In nonlinear systems, differences mean little, e.g. when there is an interaction between $X$ and $Z$. A definition not based on total or direct effects is needed. Chapter 4 will supply one through counterfactuals (p. 78).

### 3.8 Causal Inference in Linear Systems (pp. 78–87)
- Earlier methods (d-separation, backdoor) make no assumption about functional form. This section looks at linear systems, the traditional arena in the social and behavioral sciences (p. 78). Assumptions: linear relations and Gaussian error terms (in some cases only symmetric distributions) (p. 78).
- Four properties from normality (p. 79): efficient representation; substitutability of expectations for probabilities; linearity of expectations; invariance of regression coefficients.
- **Efficient representation.** A bivariate normal is characterized by five parameters $\mu_X,\mu_Y,\sigma_X,\sigma_Y,\rho_{XY}$. For $N$ normal variables the joint is fixed by the pairwise distributions. That means at most $5\times N(N-1)/2$ parameters, or in fact $2N+N(N-1)/2$ (means, variances, and correlations) (p. 79).
- **Expectations.** Normal distributions are fully defined by expectations. Conditional independence $P(Y|X,Z)=P(Y|Z)$ can be written $E[Y|X,Z]=E[Y|Z]$. So regression, a predictive method, can be used for causal information (pp. 79–80).
- **Linearity and invariance.** Every conditional expectation is linear (p. 80):
$$E[Y|X_1=x_1,\dots,X_n=x_n]=r_0+r_1x_1+\dots+r_nx_n$$
 where each $r_i$ is a partial regression coefficient. The slopes depend only on which variables are regressors, not on their measured values (Figs. 1.1–1.2: the slope is constant at each age level, but differs if age is not regressed on) (p. 80).
- **Path (structural) coefficients.** Linearity lets us annotate each edge $X\to Y$ with a path coefficient $\beta$: the contribution of $X$ in the function defining $Y$. If $Y=3X+U$ the coefficient is 3. Path coefficients are structural and causal; regression coefficients are statistical (p. 80). Regression methods also apply beyond multivariate normal (binary, categorical, interaction terms such as $X_1X_2$) (p. 80).

#### 3.8.1 Structural versus Regression Coefficients (pp. 80–81)
- A regression equation is descriptive and assumes no causation. $y=r_1x+r_2z+\epsilon$ only asks for the best linear approximation of $E(y|x,z)$. The book writes structural coefficients as $\alpha,\beta,\dots$ and regression coefficients as $r_1,r_2,\dots$. Regression errors are $\epsilon_i$ (residuals of imperfect fitting, "human-made"). Structural errors are $U_i$ (latent factors not affected by $X$, "nature-made") (pp. 80–81).
- In linear systems, regression coefficients play the role of conditional probabilities. Testable implications are vanishing regression coefficients. In $y=r_0+r_1x_1+\dots+r_nx_n+\epsilon$, if $r_i=0$ then $Y$ is independent of $X_i$ given all the other regressors (p. 81).

#### 3.8.2 The Causal Interpretation of Structural Coefficients (pp. 81–83)
- Every path coefficient is the direct effect of the independent variable on the dependent one. Direct effect (3.18) means: change $X$ by one unit with all other parents of $Y$ held constant. In any linear system, whether or not disturbances are correlated, this gives the path coefficient (p. 81).
- **Fig. 3.13 model** (p. 81): $X=U_X$; $Z=aX+U_Z$; $W=bX+cZ+U_W$; $Y=dZ+eW+U_Y$. The direct effect of $Z$ on $Y$ (other parent: $W$):
$$DE=E[Y|do(Z=z+1),do(W=w)]-E[Y|do(Z=z),do(W=w)]=d(z+1)+ew-(dz+ew)=d$$
 Deleting the equations for $Z$ and $W$ removes $X,a,b,c$ from the computation. $DE=d$ holds even if $U_Y$ were correlated with $U_Z$, though $d$ would then be nonidentifiable (p. 82).
- **Total effect.** In a linear system it is the sum, over every nonbackdoor path from $X$ to $Y$, of the product of the coefficients on that path (p. 82). Check for $Z$ on $Y$: intervene on $Z$ (delete arrows into $Z$), then
$$Y=dZ+eW+U_Y=dZ+e(bX+cZ)+U_Y+eU_W=(d+ec)Z+ebX+U_Y+eU_W$$
 So $\tau=d+ec$, the sum over the two nonbackdoor paths $Z\to Y$ and $Z\to W\to Y$. The rule holds whatever the distribution or dependence of the $U$'s (pp. 82–83).

#### 3.8.3 Identifying Structural Coefficients and Causal Effect (pp. 83–86)
- Identifiability means expressing path coefficients through covariances or regression coefficients $R_{YX\cdot Z}$. We often need not identify every parameter (p. 83).
- **Total effect:** find a set $Z$ satisfying the backdoor criterion for $(X,Y)$, then regress $Y$ on $X$ and $Z$. The coefficient of $X$ is the true causal effect. Regressing on $Z$ blocks backdoor paths, so the coefficient of $X$ does not absorb their spurious information (p. 83).
- **Fig. 3.14** (labels $\alpha$ for $T$–$X$, $\beta$ for $T$–$Y$, $\gamma$ for $X$–$W$, $\delta$ for $W$–$Y$; caption: $X$ has no direct effect on $Y$ but a total effect): adjust for $T$. Regress $y=r_XX+r_TT+\epsilon$; $r_X$ is the total effect, with no parameter identified and $W$ not measured (pp. 83–84). The direct effect of $X$ on $Y$ is zero in this graph, because there is no arrow from $X$ to $Y$ (p. 84).
- **Direct effect (the "Regression Rule for Identification").** Remove the edge $X\to Y$ to get $G_\alpha$. If a set $Z$ d-separates $X$ and $Y$ in $G_\alpha$, regress $Y$ on $X$ and $Z$. The coefficient of $X$ equals $\alpha$ (p. 84). In Fig. 3.15 (edges $Z\to X$ with $\beta$, $X\to W$ with $\gamma$, $W\to Y$ with $\delta$, $X\to Y$ with $\alpha$), removing $X\to Y$ gives $G_\alpha$ (Fig. 3.16), where $W$ d-separates $X$ and $Y$. So regress $Y=r_XX+r_WW+\epsilon$; $r_X$ is the direct effect (p. 84).
- Takeaways: in linear systems regression is the major identification tool; one must choose the regressors and the coefficient of interest. If the $U$'s are independent and all variables are measured, every structural parameter can be identified by at least one regression equation. The structural equation itself is one, but others may be better. With unmeasured variables or correlated errors, the $G_\alpha$ procedure becomes indispensable. The author says this rule eluded investigators for almost a century (pp. 84–85).
- **Instrument (Fig. 3.17).** An unobserved common cause of $X$ and $Y$ (dashed double arrow) means there is no d-separating set in $G_\alpha$. A variable is an instrument if it is d-separated from $Y$ in $G_\alpha$ and d-connected to $X$. Here $Z\to X\to Y$, with $\beta$ on $Z\to X$. Regress $y=r_1z+\epsilon$ and $x=r_2z+\epsilon$. $Z$ emits no backdoors, so $r_2=\beta$ and $r_1=\beta\alpha$ (the total effect of $Z$ on $Y$). Hence $r_1/r_2=\alpha$ (p. 86). The author notes that direct effects can be identified from total effects, but not the other way around (p. 86).
- Study question 3.8.1 (Model 3.1, Fig. 3.18; pp. 86–87): see Exercises.

*Intuition note.* In a linear system every causal effect is a number built from the edge weights. Adding the products along each causal route gives the total effect. Regression recovers these numbers whenever the graph says the right variables have been included.

#### 3.8.4 Mediation in Linear Systems (p. 87)
- With linearity, the direct effect is the path coefficient, and estimating it reduces to estimating correlation coefficients with the Sec. 3.8.3 methods. The indirect effect is $IE=\tau-DE$, with $\tau$ estimated by regression as in Fig. 3.14 (p. 87).
- Nonlinear case: $DE=E[Y|do(x,z)]-E[Y|do(x',z)]$ depends on $x,x',z$. The indirect effect cannot be defined by do-expressions, since we cannot disable $Y$'s response to $X$ by holding variables constant. It also cannot be total minus direct, since differences do not faithfully reflect nonlinear systems. Chapter 4 introduces counterfactuals for this (p. 87).

### Bibliographical notes (pp. 87–88)
- They attribute simulating interventions by modifying equations to Haavelmo (1943). The truncated product formula and adjustment formula appear in Spirtes et al. (1993). The backdoor criterion is from Pearl (1993), the front-door criterion and do-calculus from Pearl (1995). Lord's paradox is Study question 3.3.2. DAGitty is mentioned for searching instruments (p. 88).

## Toy example (ours, not from the text)
Binary $Z$, $X$, $Y$, with $Z\to X$, $Z\to Y$, $X\to Y$. Let $P(Z{=}1)=0.5$ and $P(X{=}1|Z{=}1)=0.8$, $P(X{=}1|Z{=}0)=0.2$. Let $P(Y{=}1|X,Z)$ be 0.9 for $(1,1)$, 0.7 for $(0,1)$, 0.5 for $(1,0)$, 0.3 for $(0,0)$.

**Adjustment (3.5).**
- $P(Y{=}1|do(X{=}1))=0.5\cdot0.9+0.5\cdot0.5=0.70$.
- $P(Y{=}1|do(X{=}0))=0.5\cdot0.7+0.5\cdot0.3=0.50$.
- $ACE=0.20$.

**Naive conditioning.**
- $P(X{=}1)=0.5\cdot0.8+0.5\cdot0.2=0.5$, so $P(Z{=}1|X{=}1)=0.4/0.5=0.8$ and $P(Y{=}1|X{=}1)=0.8\cdot0.9+0.2\cdot0.5=0.82$.
- Also $P(Z{=}1|X{=}0)=0.1/0.5=0.2$, so $P(Y{=}1|X{=}0)=0.2\cdot0.7+0.8\cdot0.3=0.38$.
- The risk difference is $0.44$, more than twice the ACE. $Z$ pushes people toward treatment and also toward recovery.

**Inverse probability weighting (Sec. 3.6).** Weights for $X=1$ are $1/0.8$ for $Z=1$ and $1/0.2$ for $Z=0$.
- $P(Y{=}1,X{=}1,Z{=}1)=0.5\cdot0.8\cdot0.9=0.36$, so $0.36/0.8=0.45$.
- $P(Y{=}1,X{=}1,Z{=}0)=0.5\cdot0.2\cdot0.5=0.05$, so $0.05/0.2=0.25$.
- Sum $=0.70$, matching the adjustment formula.

## Concepts
- [[do-operator]] — $P(y|do(x))$: distribution of $Y$ when $X$ is fixed by intervention, not observed (p. 55)
- [[graph-surgery]] (new) — simulate an intervention by deleting all arrows into the manipulated variable (p. 54)
- [[adjustment-formula]] (new) — $P(y|do(x))=\sum_z P(y|x,z)P(z)$ for a valid adjustment set $Z$ (p. 57)
- [[average-causal-effect]] (new) — $P(y|do(x{=}1))-P(y|do(x{=}0))$ (ACE) (p. 56)
- [[truncated-product-formula]] (new) — delete factors of intervened variables from the product decomposition (g-formula) (p. 60)
- [[back-door-front-door-criterion]] — graph conditions for choosing an adjustment set (backdoor, p. 61) or identifying through a mediator (front door, p. 69)
- [[propensity-score]] — $P(X=x|PA=z)$ or $P(X=x|Z=z)$; the denominator in (3.7) and the IPW weight (pp. 59, 72)
- [[inverse-probability-weighting]] (new) — weight each case by $1/P(x|z)$ so the sample mimics $P_m$ (p. 73)
- [[z-specific-effect]] (new) — $P(y|do(x),z)$; identified by Rule 2 (p. 70)
- [[controlled-direct-effect]] (new) — effect of changing $X$ with the mediator fixed by $do(z)$, eq. (3.18) (p. 77)
- [[path-coefficient]] (new) — structural coefficient on an edge in a linear SCM; a direct effect, unlike a regression coefficient (p. 80)
- [[instrumental-variable]] (new) — variable d-connected to $X$ and d-separated from $Y$ in $G_\alpha$; gives $\alpha=r_1/r_2$ (p. 86)
- [[d-separation]] — used here to show $Z\perp X$ in $G_m$ (p. 56) and in the $G_\alpha$ rule (p. 84)
- [[fork-chain-collider]] — conditioning on a collider opens a path; this drives the backdoor rule and the mediation problem (pp. 62, 76)
- [[simpsons-paradox]] — the graph tells which table to use; the adjustment formula resolves it (p. 58)
- [[causal-dag]] / [[structural-causal-model]] — the graph and equations behind surgery and linear path analysis (pp. 54, 81)

## Canonical instances
- [[ice-cream-crime]] — temperature confounds ice cream and crime; $do(X)$ makes $X$ and $Y$ independent (p. 54)
- [[texting-shallowness]] — correlation does not show that reducing texting reduces shallowness (p. 54)
- [[simpson-drug-gender]] — ACE $=0.0502$ by adjustment for gender (p. 57)
- [[simpson-blood-pressure]] — treatment has no parents; adjusting for blood pressure would be wrong (p. 58)
- [[smoking-tar-genotype]] — front-door formula applied to the tobacco debate (pp. 66–68)
- [[gender-hiring-qualification-income]] — mediation; conditioning on the mediator opens a collider (p. 76)
- [[lords-paradox]] — boarding-school meal plans; Study question 3.3.2 (p. 65)

## Bridges (candidates)
- [structural-analogy] inverse probability weighting ($1/P(x|z)$) ↔ Bayesian computation: importance sampling — both reweight samples drawn from one distribution to mimic another.
- [same-math] adjustment formula $\sum_z P(y|x,z)P(z)$ ↔ probability: law of total probability with the marginal $P(z)$ instead of $P(z|x)$ — the only change is which distribution weights the strata.
- [structural-analogy] conditioning vs $do()$ ↔ Bayesian updating: updating on $X=x$ revises beliefs about the world; $do(x)$ changes the world's mechanism.
- [same-math] Gaussian conditional expectation is linear in the regressors ↔ Bayesian linear regression: both use the multivariate normal conditional $E[Y|X_1..X_n]=r_0+\sum r_ix_i$.
- [metaphor] choosing an adjustment set that does not open collider paths ↔ model checking: a testable equality between two valid adjustment sets (p. 64) resembles checking a model's implications against data.

## Questions this raises
- How can we know whether a graph is valid, given that all results hold "assuming the graph constitutes a valid representation of reality" (p. 55)?
- What does the do-calculus (p. 69) add beyond backdoor, front-door, and adjustment?
- If the front-door criterion identifies effects under confounding, how sensitive are the answers to small violations of conditions (2) and (3)?
- How does Chapter 4's counterfactual definition of the indirect effect avoid the problems of differences in nonlinear systems (pp. 78, 87)?

## Exercises worth doing
- Study question 3.2.1 (p. 59) — compute $P(y|do(x))$ by simulating surgery and by adjustment, then compare ACE and risk difference; builds the core intuition — difficulty: medium
- Study question 3.3.1 (p. 64) — list all backdoor sets and the minimal ones in Fig. 3.8 — difficulty: medium
- Study question 3.3.2, Lord's paradox (p. 65) — draw the causal graph and decide which statistician is right; link to Simpson's paradox — difficulty: hard
- Study question 3.4.2 (p. 69) — the pharmacy story: draw a causal graph, construct a compatible data set, and use the two stated assumptions to estimate the effect of the fresh versus the aged drug — difficulty: hard
- Study question 3.5.1 (p. 71) — $c$-specific effect and expected $Y$ under a $Z$-dependent policy — difficulty: medium
- Study question 3.8.1 (p. 86) — regression coefficients that identify parameters in Model 3.1, including an instrument construction — difficulty: hard

## Reading notes
- Printed page numbers are given in the page labels; printed = pdf − 20. Source pages are 53–88.
- Discrepancy, p. 57 vs p. 74: 0.832 for $P(Y{=}1|do(X{=}1))$ in the Sec. 3.2 computation and 0.833 in the Sec. 3.6 computation; the source does not explain the difference.
- Table 3.2 image, "All subjects", no-tar column: it prints 19%/81% (no cancer/cancer). From the counts, 56/400 = 14% and 344/400 = 86%. Treat the percentages as a misprint.
- Sec. 3.6 numbers: the text computes $0.476+0.357=0.833$, but Table 3.5 prints 0.475 and 0.358. Also 0.116/0.247 ≈ 0.470 by my arithmetic. The text uses 0.01 where Table 3.3 shows 0.009. I did not resolve these.
- Eq. (3.11) as printed has $P(T=t|X=x,W=w)$ in the weight. Rule 2 (p. 71) has only $P(S=s|Z=z)$ in the corresponding place. These look inconsistent; I kept the printed form.
- p. 59 says the propensity-score advantages are discussed in Sec. 3.5; the discussion is in Sec. 3.6.
- In Fig. 3.14 the labels $\alpha,\beta,\gamma,\delta$ sit on $T\to X$, $T\to Y$, $X\to W$, $W\to Y$, whereas the text on p. 84 uses $\alpha$ for a direct effect of $X$ on $Y$.
- p. 87, end of Sec. 3.8.4: "differences do not faithfully reflect operations in nonlinear systems to X" is garbled in the source. I gave the evident meaning.
- A few OCR spacing glitches ("re ality", "t hese c oefficients") are harmless.
