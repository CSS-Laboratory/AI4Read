---
id: murphy-2023-pml2/ch36-causality-p1
work: murphy-2023-pml2
unit: "36 Causality (part 1/2): 36.1–36.4.6"
pages: 1185–1207
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Causality (part 1/2): causal formalism, RCTs, and confounder adjustment

## L0 — One line
The average treatment effect is defined through interventions in a structural causal model, and if all common causes are observed and overlap holds, it equals a covariate-adjusted difference of means that can be estimated by outcome regression, propensity weighting, or a doubly robust "double ML" estimator.

## L1 — The gist (≤ 120 words)
How can data tell us what would happen under an intervention, not just what is associated? The chapter works in three steps: define a causal estimand (structural causal models, do-notation), identify it from observable distributions using assumptions, then estimate it. For the average treatment effect (ATE), if X contains all common causes and overlap holds (every covariate value has both treated and untreated units), the ATE equals an adjusted difference of means. Estimators: outcome regression, inverse propensity weighting, matching, and AIPTW (outcome model plus propensity correction) with cross-fitting. AIPTW gives valid confidence intervals even with slowly converging fitted models, e.g. each at $o(n^{-1/4})$ (plus technical conditions). Every identification strategy relies on assumptions with some content the data cannot verify.

**Prerequisites:** conditional expectation and the tower property; DAGs, conditional independence and colliders; regression as minimising squared loss; central limit theorem; asymptotic notation $o(\cdot)$.

## L2 — Key ideas
- Associations alone cannot answer interventional questions: the same observed data fit several causal stories, so causal knowledge must be added (p. 1185).
- A structural causal model (SCM) is an ordered set of assignments (cause + exogenous noise). It implies a probabilistic model, not conversely, and an intervention replaces one assignment. Its ordering is therefore "load-bearing" (p. 1188).
- Graph surgery: the intervention $\mathrm{do}(A=a)$ (set $A$ to $a$) deletes the edges into $A$ and conditions on $A=a$. This separates $P(\cdot\mid A=a)$ from $P(\cdot\mid \mathrm{do}(A=a))$ (pp. 1189–1190).
- Identification means the assumptions leave a unique value of the estimand. Every identification strategy relies on assumptions with some content that the observed data cannot validate (pp. 1191–1192).
- Queries form a hierarchy. Interventional queries (e.g. the ATE) need only marginal potential-outcome distributions. Counterfactual queries need the within-individual joint, hence functional-form assumptions (p. 1193).
- Theorem 2: with observed confounders and overlap, ATE $=\mathbb E[\mathbb E[Y\mid A=1,X]]-\mathbb E[\mathbb E[Y\mid A=0,X]]$ (p. 1196). A randomized controlled trial (RCT, random treatment assignment) is the special case with no confounders (p. 1194).
- Three estimation routes: outcome model $\hat Q$ (predicts $Y$ from $A,X$), propensity model $\hat g$ (predicts $A$ from $X$; inverse-propensity weighting, IPTW), or both (augmented IPTW, AIPTW). AIPTW's bias term is a product of the errors of the two fitted ("nuisance") models, so $o(n^{-1/4})$ rates for each suffice, given technical conditions, for a $\sqrt n$ central limit theorem (pp. 1198–1202).
- Practical pitfalls: conditioning on mediators (variables on a path from $A$ to $Y$) or colliders (variables caused by both), m-bias (adjusting for a collider of two hidden causes), conditioning on instruments (causes of treatment only) which can amplify bias, near-violations of overlap, and no empirical train/test validation of causal estimates (pp. 1204–1207).

## L3 — Walkthrough

### 36.1 Introduction (pp. 1185–1186)
- Most ML summarises associations among observed variables to predict on similar data. Causal inference asks how a system would change if observed under different conditions, e.g. whether a patient recovers if given a treatment (p. 1185).
- Figure 36.1: ice cream production vs drowning deaths, and smoking vs lung cancer. Both show strong positive association, yet "ban ice cream" and "ban cigarettes" intuitively have different answers (p. 1185).
- Three stories for ice cream and drowning: ice cream causes drowning; drownings raise ice cream demand; or warm weather is a common cause. All can produce exactly the same data, but they imply very different effects of a ban. So we need some causal knowledge (p. 1185).
- Three-step approach (p. 1186):
  1. **Causal estimand**: a summary of how the world would change under intervention.
  2. **Identification**: express the estimand through quantities estimable in principle from observational data. This tells us what we could answer with perfect knowledge of the observed distribution.
  3. **Estimation**: estimate that quantity from a finite sample. Non-parametric (ML) predictive models can be used.
- Focus: the **average treatment effect (ATE)**, the effect averaged over a population (p. 1186).

### 36.2 Causal formalism

**36.2.1 Structural causal models (pp. 1187–1188)**
- Setting: smoking $A_i$, lung cancer $Y_i$, health-consciousness index $H_i$, genetic predisposition $G_i$; data iid from $P^{\mathrm{obs}}$ (p. 1187).
- Many factorisations describe the same $P^{\mathrm{obs}}$, e.g.
$$A\sim P^{\mathrm{obs}}(A)\tag{36.1}$$
$$H\mid A\sim P^{\mathrm{obs}}(H\mid A)\tag{36.2}$$
$$Y\mid A,H\sim P^{\mathrm{obs}}(Y\mid H,A)\tag{36.3}$$
$$G\mid A,H,Y\sim P^{\mathrm{obs}}(G\mid A,H,Y)\tag{36.4}$$
  This is valid for sampling, but does not map onto a mechanistic story. It is perhaps more plausible that $H$ causally precedes $A$ (p. 1187).
- A **structural causal model (SCM)**: each variable is a deterministic function of its causes plus exogenous noise, written as ordered assignments (pp. 1187–1188):
$$G\leftarrow f_G(\xi_0),\quad H\leftarrow f_H(\xi_1),\quad A\leftarrow f_A(H,\xi_2),\quad Y\leftarrow f_Y(G,H,A,\xi_3)\tag{36.5–36.8}$$
  The $f$'s are unknown, fixed, physical relationships. The $\xi$'s are unmeasured causes modelled as independent noise, since units are drawn at random (p. 1188).
- SCMs imply probabilistic models, but not conversely. Sampling: draw $\xi$, evaluate assignments in order (p. 1188).
- Beyond the probability model, an SCM encodes assumptions about interventions. An **intervention** replaces an assignment, e.g. $A\leftarrow 0$, written $P(Y\mid \mathrm{do}(A=0),H)$. Because the $f$'s are assumed invariant, the edited SCM is assumed to generate the data we would see if we really intervened (p. 1188).
- So the ordering of statements is "load-bearing". In ordinary probabilistic models, variables can be rearranged by Bayes' rule without changing substantive implications (p. 1188).
- Caveat: SCMs may not capture all notions of causality (e.g. conservation or equilibrium laws such as the ideal gas law). The chapter confines itself to SCMs (p. 1188).

**36.2.2 Causal DAGs (pp. 1188–1190)**
- A **causal graph** says which variables causally affect which, leaving the form of $f$ unspecified. Draw it by putting arrows from right-hand-side variables to the left-hand-side variable of each line (Figure 36.2a). Causal DAGs relate to SCMs as PGMs relate to probabilistic models (pp. 1188–1189).
- Causal DAGs imply a PGM: they give conditional independences via the Markov property (if $X\leftarrow Y\to Z$ then $X\perp\!\!\!\perp Z\mid Y$; d-separation). If $X\to Y\leftarrow Z$ then usually $X\not\perp\!\!\!\perp Z\mid Y$ even if $X,Z$ are marginally independent; $Y$ is a **collider** (p. 1189).
- PGMs encode statistical assumptions; causal graphs encode stronger, causal ones, from which one can derive how statistical relations change under intervention (p. 1189).
- Two sources of association between $A$ and $D$ (p. 1189):
  - A directed path from $A$ to $D$. Then $P(D\mid \mathrm{do}(A=a))\ne P(D\mid \mathrm{do}(A=a'))$.
  - A common cause $C$ with paths to both. If this is the only link, intervening on $A$ does not change $D$, but $P(D\mid A=a)\neq P(D\mid A=a')$ because $A$ carries information about $C$.
- Example: even if smoking had no effect on cancer, the path $A\leftarrow H\to Y$ (a "backdoor path") would create association. This is one core reason statistical and causal association differ (p. 1189).
- **Graph surgery**: after an intervention on $A$ nothing causes $A$. So an intervention setting $A=a$ deletes all incoming edges to $A$ and then conditions on $A=a$ in the post-surgery ("mutilated") graph (Figure 36.2b). $P(\mathbf X\mid \mathrm{do}(A=a))$ is the distribution under this graph; $\mathbb E[\mathbf X\mid \mathrm{do}(A=a)]\triangleq\mathbb E_{P(\mathbf X\mid \mathrm{do}(A=a))}[\mathbf X]$ (p. 1190).
- ATE as defined by the author:
$$\mathrm{ATE}=\mathbb E[Y\mid \mathrm{do}(A=1)]-\mathbb E[Y\mid \mathrm{do}(A=0)]\tag{36.9}$$
- Running example, conditioning vs intervening (p. 1190):
$$P(Y,H,G\mid A=a)=P(Y\mid H,G,A=a)P(G)P(H\mid A=a)\tag{36.10}$$
$$P(Y,H,G\mid \mathrm{do}(A=a))=P(Y\mid H,G,A=a)P(G)P(H)\tag{36.11}$$
  The conditional describes a population whose $H$ follows the distribution among those with $A=a$. The interventional one uses the marginal $P(H)$. E.g. $P(H\mid A=\text{smoker})$ would put more mass on low $H$ than $P(H)$ (p. 1190).

*Intuition note.* Conditioning on $A=a$ selects a different mix of people. Intervening keeps the same people and changes only $A$. The two formulas differ exactly in the factor for $H$.

**36.2.3 Identification (pp. 1190–1192)**
- Many different SCMs can give identical observed distributions, so the SCM cannot be uniquely identified from data, however large the sample (p. 1190).
- Example: treatment $A$ and outcome $Y$ share an unobserved binary common cause $U$. Then $\mathbb E[Y\mid \mathrm{do}(A=1)]$ generally cannot be learned. We cannot distinguish a strong treatment effect from no effect plus $U=1$ both causing treatment and raising the chance of a positive outcome. The same holds for $P(Y\mid \mathrm{do}(A=1))$ (p. 1190).
- An estimand is **identified** (identifiable) under assumptions if those assumptions provide a unique answer. Each set of sufficient conditions is an **identification strategy** (p. 1191).
- Usual proof by construction: if the causal estimand can be written entirely in observable distributions it is identified. Such a function is a **statistical estimand** (p. 1191). In the running SCM, the ATE equals
$$\mathrm{ATE}\overset{(*)}{=}\tau^{\mathrm{ATE}}\triangleq\mathbb E\big[\mathbb E[Y\mid H,A=1]-\mathbb E[Y\mid H,A=0]\big]\tag{36.12}$$
  where $(*)$ holds only because of specific properties of the SCM. The right side has no do-operators (p. 1191).
- Example assumptions, from strong to minimal (p. 1191): (1) additive on the logit scale in $A,G,H$; (2) smoking never decreases any individual's cancer probability; (3) $A$ is influenced by $H$ but not by $G$.
- Fully parametric assumptions are typically very strong. The goal is assumptions weak enough to be plausible but strong enough to identify (p. 1191).
- Minimal "which-affects-which" assumptions are exactly a (possibly incomplete) causal DAG. Section 36.8 is said to show that much progress is possible from such non-parametric assumptions (pp. 1191–1192).
- Some useful assumptions cannot be encoded in a graph but are weaker than full functional forms, e.g. outcome additive in treatment and confounders with no interactions. They can identify effects when the graph alone does not (p. 1192).
- Every identification strategy relies on assumptions that have some content that cannot be validated in observed data. If it could be validated, the estimand would be identifiable from data alone, yet many estimand values are compatible with the data (p. 1192).

**36.2.4 Counterfactuals and the causal hierarchy (pp. 1192–1194)**
- Three kinds of query (p. 1192):
  - **Observational**: associations ("Are smoking and cancer associated?").
  - **Interventional**: population-level causal effects ("How much does smoking raise cancer probability in a population?"). The rest of the chapter focuses on these.
  - **Counterfactual**: individual-level, "had something been different" ("Would Alice have developed cancer had she not smoked?"). The hierarchy was popularised by [Pea09a, Ch. 1].
- Interventional probabilities are uncertainty about the noise $\xi$ of a randomly selected individual, so they are statements about populations (p. 1192).
- Counterfactual outcomes for unit $i$ come from running the same $\xi_i$ through differently intervened SCMs. In potential-outcomes notation (p. 1192):
$$Y_i(a)\triangleq f_Y(G_i,H_i,a,\xi_{3,i})\tag{36.13}$$
  $Y_i(a)$ is the outcome had $A$ been set to $a$ with $G_i,H_i,\xi_{3,i}$ fixed (p. 1193).
- Being writable in potential outcomes does not make a query counterfactual. The ATE is interventional:
$$\mathrm{ATE}=\mathbb E[Y_i(1)-Y_i(0)]\tag{36.14}$$
- The dividing line is whether the query needs the joint distribution of potential outcomes within individuals, or marginals across individuals suffice. A signature of a counterfactual query is conditioning on one potential outcome, e.g. (p. 1193)
$$\mathbb E[Y_i(0)\mid Y_i(1)=1,A_i=1]\tag{36.15}$$
  This needs the link between individual outcomes across worlds (via $\xi_{3,i}$) and cannot be rewritten in do-notation (p. 1193).
- Counterfactual queries need categorically more assumptions. For interventional ones, knowing the DAG is often sufficient. For counterfactual ones, some functional-form assumptions are necessary, since only one potential outcome per individual is observed. Counterfactual quantities are "cross-world"; [SP07] is cited for when they are identifiable (p. 1193).
- Potential outcomes and graphs are, ultimately, mathematically equivalent. Potential outcomes map more directly to mechanistic understanding but do not automatically separate interventional from counterfactual queries. Graphs are easier with many variables (pp. 1193–1194).

### 36.3 Randomized control trials (pp. 1194–1195)
- In an RCT, assignment is random, so nothing causes treatment and there are no common causes of $A$ and $Y$ (p. 1194).
- Then $P(Y\mid \mathrm{do}(A=a))=P(Y\mid a)$, essentially by definition of graph surgery: $A$ has no parents, so the mutilated graph equals the original (p. 1194).
- ATE and its identification (p. 1194):
$$\mathrm{ATE}=\mathbb E[Y\mid \mathrm{do}(A=1)]-\mathbb E[Y\mid \mathrm{do}(A=0)]\tag{36.16}$$
$$\tau^{\mathrm{RCT}}=\mathbb E[Y\mid A=1]-\mathbb E[Y\mid A=0]$$
- Natural estimator, with $n_A$ the number of treated units:
$$\hat\tau^{\mathrm{RCT}}\triangleq\frac1{n_A}\sum_{i:A_i=1}Y_i-\frac1{n-n_A}\sum_{i:A_i=0}Y_i\tag{36.17}$$
- RCTs are the gold standard, since the no-unobserved-confounders assumption is enforced by design. Limits: they can be infeasible (expense, regulation, outcomes measured decades later), and participants may not represent the deployment population (pp. 1194–1195).

### 36.4 Confounder adjustment

**36.4.1 Causal estimand, statistical estimand, identification (pp. 1195–1198)**
- Setting: binary $A$, outcome $Y$, observed common causes $X$, iid from unknown $P$. The ATE, also called average causal effect (ACE), is
$$\mathrm{ATE}=\mathbb E[Y\mid \mathrm{do}(A=1)]-\mathbb E[Y\mid \mathrm{do}(A=0)]\tag{36.18}$$
- **Confounders** are common causes of treatment and outcome. Example: childhood horseback riding and adult health, both influenced by wealth $X$. Riders are wealthier, so they have better outcomes even with no causal benefit (p. 1196).
- Assumption: the triangle DAG (Figure 36.3: $X\to A$, $X\to Y$, $A\to Y$). The target is the distribution with the $X\to A$ edge removed. Two invariances make this tractable (p. 1196):
  1. The mechanism for $Y$ given $A,X$ is unchanged after removing $X\to A$.
  2. The distribution of $X$ is unchanged by the intervention.

**Theorem 2 (Adjustment with no unobserved confounders).** Observe $A,Y,X\sim P$. Suppose (1) *Confounders observed*: the data obey Figure 36.3; $X$ contains all common causes of $A$ and $Y$, and no variable in $X$ is caused by $A$ or $Y$. (2) *Overlap*: $0<P(A=1\mid X=x)<1$ for all $x$. Then ATE $=\tau$ with (p. 1196)
$$\tau=\mathbb E[\mathbb E[Y\mid A=1,X]]-\mathbb E[\mathbb E[Y\mid A=0,X]]\tag{36.19}$$

*Proof (as given).*
$$\mathrm{ATE}=\mathbb E[Y\mid \mathrm{do}(A=1)]-\mathbb E[Y\mid \mathrm{do}(A=0)]\tag{36.20}$$
$$=\mathbb E[\mathbb E[Y\mid \mathrm{do}(A=1),X]]-\mathbb E[\mathbb E[Y\mid \mathrm{do}(A=0),X]]\tag{36.21}$$
$$=\mathbb E[\mathbb E[Y\mid A=1,X]]-\mathbb E[\mathbb E[Y\mid A=0,X]]\tag{36.22}$$
- (36.21) is the tower property, conditioning on $X$. Overlap is needed for it to be well defined (p. 1197).
- (36.22) is the key step. From the graph, $P(Y\mid A,X)$ is the same in the original and mutilated graphs, and the mutilated graph defines $P(Y\mid \mathrm{do}(A=a),X)$ (pp. 1196–1197).
- Equation (36.19) has no do-operators, so characterising $P$ maps it to a unique ATE (p. 1197).

*Intuition note.* Within each stratum of $X$, treated and untreated people are comparable, so the observed difference is causal there. We then average over the one population distribution $P(X)$.

- Naive vs adjusted (p. 1197):
$$\tau=\int\mathbb E[Y\mid A=1,X]P(X)dX-\int\mathbb E[Y\mid A=0,X]P(X)dX\tag{36.23}$$
$$\mathbb E[Y\mid A=1]-\mathbb E[Y\mid A=0]=\int\mathbb E[Y\mid A=1,X]P(X\mid A=1)dX-\int\mathbb E[Y\mid A=0,X]P(X\mid A=0)dX\tag{36.24}$$
  The naive difference integrates over different confounder distributions per arm. $\tau$ uses the same $P(X)$ for both.
- **Definition 1 (overlap).** $P$ on $A,X$ satisfies overlap if $0<P(A=1\mid x)<1$ for all $x$; **strict overlap** if $\epsilon<P(A=1\mid x)<1-\epsilon$ for all $x$ and some $\epsilon>0$ (p. 1197).
- Why overlap is necessary: if a drug was prescribed only to males and sex is a confounder, there are no data on $\mathbb E[Y\mid A=1,X=\text{female}]$, so (36.19) is not identifiable without further assumptions. Strict overlap ensures conditional distributions at each stratum can be estimated in finite samples (p. 1197).
- With many covariates, combinations of traits can strongly predict treatment (e.g. men over 70 with BMI above 25 rarely get the drug). If such groups are a large share of the target population or have different effects, this is a problem. Strict overlap then forces most dimensions of $X$ to mimic RCT-like balance [D'A+21] (pp. 1197–1198).

**36.4.2 ATE estimation with observed confounders (pp. 1198–1202).** These techniques are called backdoor adjustment (footnote 2: Section 36.8 relates this to the do-calculus and to cases with unobserved common causes). A strategy can account for confounders' influence on outcome, on treatment, or both (p. 1198).

*36.4.2.1 Outcome model adjustment (g-computation).*
- **Definition 2.** The conditional expected outcome $Q(a,x)=\mathbb E[Y\mid A=a,X=x]$ (36.25). Then $\tau=\mathbb E[Q(1,x)-Q(0,x)]$. Fit $\hat Q$ and report
$$\hat\tau^Q\triangleq\frac1n\sum_i\hat Q(1,x_i)-\hat Q(0,x_i)\tag{36.26}$$
  (p. 1198).
- Fit $\hat Q$ by squared error, since $\mathbb E[Y\mid a,x]=\arg\min_Q\mathbb E[(Y-Q(A,X))^2]$ (footnote 4: for square-integrable variables, minimised over measurable functions). For treated units $\hat Q(0,x_i)$ is the guess about the counterfactual untreated outcome (justified by the same conditions as Theorem 2, footnote 5) (p. 1198).
- The outer expectation over $P(X)$ is replaced by the empirical distribution $\hat P(X)=\frac1n\sum_i\delta_{x_i}$ (p. 1199).
- *Linear regression special case.* Assume Theorem 2's conditions and a true $Q(A,X)=\beta_0+\beta_AA+\beta_XX$. Then $Q(1,X)-Q(0,X)=\beta_A=\tau$, so ATE estimation reduces to estimating the coefficient $\beta_A$. Outcome adjustment generalises this by dropping linearity (p. 1199).

*36.4.2.2 Propensity score adjustment (pp. 1199–1200).*
- Idea: confounding may be viewed as due to the difference between $P(X\mid A=1)$ and $P(X\mid A=0)$. With all confounders observed, reweight so $X$ has the same distribution in both groups (p. 1199).
- **Definition 3.** The propensity score is $g(x)=P(A=1\mid X=x)$ (p. 1199).
- Since $A\in\{0,1\}$:
$$\tau=\mathbb E\Big[\frac{YA}{g(X)}-\frac{Y(1-A)}{1-g(X)}\Big]\tag{36.27}$$
  Verification (as the author sketches): $\mathbb E[YA\mid X]=\mathbb E[Y\mid A=1,X]P(A=1\mid X)+0$. Rearrange for $\mathbb E[Y\mid A=1,X]$, do the same for $A=0$, substitute into (36.19). This is a mathematical fact about the statistical estimand and needs no causal assumptions (p. 1199).
- **IPTW estimator** (p. 1199):
$$\hat\tau^{\mathrm{IPTW}}\triangleq\frac1n\sum_i\frac{Y_iA_i}{\hat g(X_i)}-\frac{Y_i(1-A_i)}{1-\hat g(X_i)}\tag{36.28}$$
- $\hat g$ comes from predicting $A$ from $X$. A well-specified model with a proper scoring rule has risk minimiser $g^*(X)=P(A=1\mid X)$; cross-entropy and squared loss are proper (p. 1200).
- IPTW upweights units who were unlikely to be treated yet were treated (and vice versa). They are typical of the other group, so their outcomes tell what a typical untreated unit would do if treated (p. 1200).
- Warning: IPTW is asymptotically valid but can be unstable in finite samples. Propensities near 0 or 1 give huge weights and high variance. The **Hajek** (self-normalised) version may mitigate this in some cases (index of the denominator sums renamed $j$):
$$\hat\tau^{\mathrm{h\text{-}IPTW}}\triangleq\sum_iY_iA_i\frac{1/\hat g(X_i)}{\sum_jA_j/\hat g(X_j)}-\sum_iY_i(1-A_i)\frac{1/(1-\hat g(X_i))}{\sum_j(1-A_j)/(1-\hat g(X_j))}\tag{36.29}$$
  Extreme weights can persist (truly imbalanced strata, or an overfit propensity model). Heuristics such as weight clipping are common (p. 1200).

*36.4.2.3 Double machine learning (pp. 1200–1202).*
- Both routes above fit nuisance models ($Q$ or $g$) and plug them in. Estimate quality depends on theirs. Even though $\tau$ is one-dimensional, naive estimators can converge slowly, giving unreliable inference or wide intervals (p. 1200).
- **AIPTW** (augmented IPTW):
$$\hat\tau^{\mathrm{AIPTW}}\triangleq\frac1n\sum_i\hat Q(1,X_i)-\hat Q(0,X_i)+A_i\frac{Y_i-\hat Q(1,X_i)}{\hat g(X_i)}-(1-A_i)\frac{Y_i-\hat Q(0,X_i)}{1-\hat g(X_i)}\tag{36.30}$$
  This is the outcome-adjustment estimator plus a propensity-based stabilisation term. It belongs to a class called semi-parametrically efficient or double machine-learning estimators [Che+17e; Che+17d] (pp. 1200–1201).
- **Influence curve** of $\tau$, with $\mathbf X_i=(X_i,A_i,Y_i)$ (footnote 6: the general theory is omitted):
$$\phi(\mathbf X_i;Q,g,\tau)\triangleq Q(1,X_i)-Q(0,X_i)+A_i\frac{Y_i-Q(1,X_i)}{g(X_i)}-(1-A_i)\frac{Y_i-Q(0,X_i)}{1-g(X_i)}-\tau\tag{36.31}$$
  By design $\hat\tau^{\mathrm{AIPTW}}-\tau=\frac1n\sum_i\phi(\mathbf X_i;\hat Q,\hat g,\tau)$ (p. 1201).
- Ideal case (know $Q,g$): $\hat\tau^{\mathrm{ideal}}=\frac1n\sum_i\phi(\mathbf X_i;Q,g,\tau)+\tau$, and by the CLT
$$\sqrt n(\hat\tau^{\mathrm{ideal}}-\tau)\xrightarrow{d}\mathrm{Normal}(0,\mathbb E[\phi(\mathbf X_i;Q,g,\tau)^2])\tag{36.32}$$
- With estimated nuisances the $\sqrt n$ rate is not expected in general. For the outcome estimator, $\sqrt n(\hat\tau^Q-\tau)$ converges only if $\sqrt n\,\mathbb E[(\hat Q-Q)^2]^{1/2}\to0$ (as printed), i.e. $Q$ must itself be estimated at the $\sqrt n$ rate, "a much harder task" (p. 1201).
- Error decomposition:
$$\sqrt n(\hat\tau^{\mathrm{AIPTW}}-\tau)\tag{36.33}$$
$$=\frac1{\sqrt n}\sum_i\phi(\mathbf X_i;Q,g,\tau)\tag{36.34}$$
$$+\frac1{\sqrt n}\sum_i\Big[\phi(\mathbf X_i;\hat Q,\hat g,\tau)-\phi(\mathbf X_i;Q,g,\tau)-\mathbb E[\phi(\mathbf X;\hat Q,\hat g,\tau)-\phi(\mathbf X;Q,g,\tau)]\Big]\tag{36.35}$$
$$+\sqrt n\,\mathbb E[\phi(\mathbf X;\hat Q,\hat g,\tau)-\phi(\mathbf X;Q,g,\tau)]\tag{36.36}$$
  - (36.34) is the ideal-case error. We want AIPTW to match it asymptotically, which happens if the other two terms vanish (p. 1201).
  - (36.35) is the penalty for reusing the same data to fit $Q,g$ and compute $\tau$. For many model classes such "empirical process" terms go to 0; it is guaranteed by using separate data (p. 1201).
  - (36.36) is the penalty for misestimating nuisances. With "a little algebra" (p. 1202):
$$\mathbb E[\phi(\mathbf X;\hat Q,\hat g)-\phi(\mathbf X;Q,g)]=\mathbb E\Big[\frac1{g(X)}(\hat g(X)-g(X))(\hat Q(1,X)-Q(1,X))\tag{36.37}$$
$$+\frac1{1-g(X)}(\hat g(X)-g(X))(\hat Q(0,X)-Q(0,X))\Big]\tag{36.38}$$
- The errors of $Q$ and $g$ are multiplied. By Cauchy–Schwarz, (36.36) $\to0$ as long as $\sqrt n\max_a\mathbb E[(\hat Q(a,X)-Q(a,X))^2]^{1/2}\,\mathbb E[(\hat g(X)-g(X))^2]^{1/2}\to0$. So it suffices that the product of the errors is small enough (the text writes "$o(\sqrt n)$"; see Reading notes). Each error only needs to shrink as $o(n^{-1/4})$ (p. 1202).
- Under this weak condition (plus unstated technical conditions),
$$\sqrt n(\hat\tau^{\mathrm{AIPTW}}-\tau)\xrightarrow{d}\mathrm{Normal}(0,\mathbb E[\phi(\mathbf X_i;Q,g,\tau)^2])\tag{36.39}$$
  The earlier estimators require much faster nuisance convergence (p. 1202).
- Two more properties of AIPTW (p. 1202): it is **non-parametrically efficient** (smallest possible variance, $\mathbb E[\phi^2]$, among estimators making no parametric assumptions, hence smallest confidence intervals of such approaches), and **doubly robust** (consistent if at least one of $\hat Q$, $\hat g$ is consistent).

*Intuition note.* The correction term is built so that a mistake in $\hat Q$ only hurts if $\hat g$ is also wrong, and vice versa. The bias is a product of two small errors, which is much smaller than either.

*Skip path (36.33–36.39):* carry forward only that the leftover bias is a product of the two nuisance errors, so the CLT (36.39) holds with limiting variance $\mathbb E[\phi^2]$.

*36.4.2.4 Cross fitting (p. 1202).*
- Plain sample splitting (fit nuisances on one part, compute the estimator on the other) removes the reuse penalty but wastes data (p. 1202).
- **Cross fitting**: split into $K$ folds. For fold $j$, fit $\hat Q^{-j},\hat g^{-j}$ on the other $K-1$ folds. For each $i$ in fold $j$, set $\hat Q(a_i,x_i)=\hat Q^{-j}(a_i,x_i)$ and $\hat g(x_i)=\hat g^{-j}(x_i)$. Plug into (36.30). It "can be shown" this keeps the same $\sqrt n$ CLT guarantee (p. 1202).

**36.4.3 Uncertainty quantification (p. 1203).**
- Using (36.39), it suffices to estimate the asymptotic variance by plugging in fitted nuisances and $\hat\tau$ [Che+17e]:
$$\hat{\mathbb V}[\hat\tau]=\frac1n\sum_i\phi(\mathbf X_i;\hat Q,\hat g,\hat\tau)^2\tag{36.40}$$
  A 95% CI is $\hat\tau\pm1.96\sqrt{\hat{\mathbb V}[\hat\tau]/n}$ (p. 1203).
- Bootstrapping is an alternative, but it requires refitting nuisance functions for each resample and can be prohibitively costly (p. 1203).

**36.4.4 Matching (pp. 1203–1204).**
- For discrete $X$, let $\mathcal A_x$ be treated and $\mathcal C_x$ untreated units with covariate value $x$ (p. 1203):
$$\hat\tau^{\mathrm{matching}}=\sum_x\hat P(x)\Big(\frac1{|\mathcal A_x|}\sum_{i\in\mathcal A_x}Y_i-\frac1{|\mathcal C_x|}\sum_{j\in\mathcal C_x}Y_j\Big)\tag{36.41}$$
- Write $Y_i=Q(A_i,X_i)+\xi_i$ with $\mathbb E[\xi_i\mid A_i,X_i]=0$:
$$\hat\tau^{\mathrm{matching}}=\sum_x\hat P(x)\big(Q(1,x)-Q(0,x)\big)+\sum_x\hat P(x)\Big(\frac1{|\mathcal A_x|}\sum_{i\in\mathcal A_x}\xi_i-\frac1{|\mathcal C_x|}\sum_{j\in\mathcal C_x}\xi_j\Big)\tag{36.42}$$
  The first term estimates $\tau$ (equal to $\tau$ if $\hat P=P$). The second tends to 0 if $|\mathcal A_x|,|\mathcal C_x|\to\infty$ (p. 1203).
- Continuous covariates need a notion of "close" (p. 1204).
- Two emphasised points (p. 1204): (i) matching is an estimator of the observational parameter $\tau$ and says nothing about causal identification, which is set by Theorem 2's conditions; (ii) it amounts to the model $\hat Q(1,x)=\frac1{|\mathcal A_x|}\sum_{i\in\mathcal A_x}Y_i$ (and similarly for $\hat Q(0,x)$). A good ML outcome model may then give a more accurate estimate.
- Adjusting for a function $\phi(X)$ with $A\perp\!\!\!\perp X\mid\phi(X)$ suffices. Reason: $g(X)=P(A=1\mid\phi(X))$ depends only on $\phi(X)$, and $\tau$ depends on $X$ only through $g(X)$ via (36.27). The popular choice is $\phi(X)=g(X)$, giving **propensity score matching** (fit propensity, then match on it). Again this is an estimation procedure only (p. 1204).

**36.4.5 Practical considerations (pp. 1204–1206)**

*36.4.5.1 What to adjust for.*
- With the full causal graph the criterion is clear: adjust for the actual causal parents of $A$ and $Y$ (generalised in Section 36.8) (p. 1204).
- Without it, "condition on everything" is tempting but problematic (pp. 1204–1205):
  - A **mediator** $M$ (on a directed path from $A$ to $Y$): conditioning blocks part of the effect. This need not shrink the estimate, since a mediator's effect may oppose other paths; it can inflate or flip the sign.
  - A **collider** $C$ (caused by both $A$ and $Y$): conditioning induces an extra dependency between $A$ and $Y$.
- Both pitfalls involve post-treatment variables. Restricting to pre-treatment covariates is natural. If a valid adjustment set exists among $X$, one exists among the pre-treatment covariates, because any open backdoor path contains a parent of $A$ (p. 1205).
- But conditioning on all pre-treatment variables can open paths through colliders: **m-bias** (Figure 36.4). Here $U_1\to A$, $U_1\to X\leftarrow U_2$, $U_2\to Y$. $A$ and $Y$ are unconfounded, but adjusting for the collider $X$ opens a backdoor path, even though $X$ need not be pre-treatment (p. 1205). (The text calls the collider $D$ in the prose and $X$ in the figure.)
- VanderWeele–Shpitser [VS11] heuristic: condition on pre-treatment variables that are causes of treatment, outcome, or both. This avoids m-bias, needs more causal knowledge than the earlier heuristics, but not detailed knowledge of relations among covariates (p. 1205).
- If more structure is known, adjustment sets can be optimised to minimise variance [RS20]. An example is dropping **instruments** (parents of treatment but not of outcome; Section 36.5) (p. 1205).
- If no observed set blocks all backdoor paths, any adjusted estimate is biased, and the bias need not fall as more variables are added. Conditioning on an instrument often raises bias as well as variance ("bias amplification" or z-bias; Section 36.7.2). Rule of thumb: variables explaining much more variation in treatment than in outcome can amplify bias and need caution (pp. 1205–1206).

*36.4.5.2 Overlap (p. 1206).*
- With infinite data any amount of overlap suffices; in practice even near failures hurt. $\phi^2$ contains terms proportional to $1/g(X)$ and $1/(1-g(X))$, so variance balloons where $g\approx0$ or $1$ (unless such units are rare) (p. 1206).
- Practical check: fit $\hat g$ (needed anyway) and look for extreme values. The simplest fix, which the author calls "to cheat", is to exclude data with extreme $\hat g$. This is the ATE over the subpopulation where overlap holds. It changes the estimand and must be justified by knowledge of the real problem (p. 1206).

*36.4.5.3 Choice of estimand and the ATT (pp. 1206–1207).*
- The goal is usually qualitative (sign, size). The ATE is not sacrosanct. An alternative that is easier to estimate is the **average treatment effect on the treated**:
$$\mathrm{ATT}\triangleq\mathbb E_{X\mid A=1}\big[\mathbb E[Y\mid X,\mathrm{do}(A=1)]-\mathbb E[Y\mid X,\mathrm{do}(A=0)]\big]\tag{36.43}$$
- Useful when many population members are very unlikely to be treated but treated units had reasonably high chance of being control, e.g. controls from the general population while treated self-selected from a smaller subpopulation. The ATT omits controls with no similar treated unit (p. 1206).
- Under Figure 36.3 and $P(A=1\mid X=x)<1$ for all $x$ (weaker than ATE overlap; same proof as Theorem 2):
$$\tau^{\mathrm{ATT}}=\mathbb E_{X\mid A=1}\big[\mathbb E[Y\mid A=1,X]-\mathbb E[Y\mid A=0,X]\big]\tag{36.44}$$
- ATE strategies carry over: estimate nuisances the same way and average over treated points only. A double ML estimator that also uses untreated points (p. 1207):
$$\hat\tau^{\mathrm{ATT\text{-}AIPTW}}\triangleq\frac1n\sum_i\frac{A_i}{P(A=1)}(Y_i-\hat Q(0,X_i))-\frac{(1-A_i)\hat g(X_i)}{P(A=1)(1-\hat g(X_i))}(Y_i-\hat Q(0,X_i))\tag{36.45}$$
  Its variance is estimated via $\phi^{\mathrm{ATT}}$ (36.46) and $\hat{\mathbb V}[\hat\tau^{\mathrm{ATT\text{-}AIPTW}}]$ (36.47):
$$\phi^{\mathrm{ATT}}(\mathbf X_i;Q,g,\tau)\triangleq\frac1n\sum_i\Big[\frac{A_i}{P(A=1)}(Y_i-\hat Q(0,X_i))-\frac{(1-A_i)\hat g(X_i)}{P(A=1)(1-\hat g(X_i))}(Y_i-\hat Q(0,X_i))-\frac{A_i\tau}{P(A=1)}\Big]\tag{36.46}$$
$$\hat{\mathbb V}[\hat\tau^{\mathrm{ATT\text{-}AIPTW}}]\triangleq\frac1n\sum_i\phi^{\mathrm{ATT}}(\mathbf X_i;\hat Q,\hat g,\hat\tau^{\mathrm{ATT\text{-}AIPTW}})^2\tag{36.47}$$
- The ATT estimator does not need $Q(1,X)$, which can help when treated units are rare [Che+17e] (p. 1207).

**36.4.6 Summary and practical advice (p. 1207; the part ends mid-sentence).**
- Common recipe: (1) fit $\hat Q(a,x)$ and/or $\hat g(x)$; (2) compute $\hat Q(0,x_i),\hat Q(1,x_i),\hat g(x_i)$; (3) combine into an ATE estimate (p. 1207).
- No approach is a silver bullet. Double ML has efficiency guarantees and a variance recipe without bootstrapping the fitting, but its point estimates can sometimes underperform naive counterparts [KS07]. There are cases where each of outcome regression, propensity weighting or doubly robust methods outperforms the others (p. 1207).
- Fewer guardrails than in predictive modelling: causal estimands are functionals of a different data-generating process than the observed one. So many aspects cannot be validated empirically using standard techniques such as a train/test split (p. 1207).

## Toy example (ours, not from the text)
Population of 100 people. Confounder $X\in\{0,1\}$ (say wealth), 50 people each. Assume the true causal mean outcomes are $Q(0,0)=0.2$, $Q(1,0)=0.3$, $Q(0,1)=0.6$, $Q(1,1)=0.7$. So the true effect is $0.1$ in both strata. Treatment depends on $X$: $g(1)=0.8$, $g(0)=0.2$. Take the group means to be exactly these values.

Counts: $X=1$: 40 treated, 10 control. $X=0$: 10 treated, 40 control.

- **Naive** (36.24): treated mean $=(40\cdot0.7+10\cdot0.3)/50=(28+3)/50=0.62$. Control mean $=(10\cdot0.6+40\cdot0.2)/50=(6+8)/50=0.28$. Naive difference $=0.34$. This is confounded: treated people are mostly $X=1$.
- **Adjusted** (36.19/36.23), using $P(X=1)=P(X=0)=0.5$: $\tau=0.5(0.7-0.6)+0.5(0.3-0.2)=0.05+0.05=0.10$.
- **IPTW** (36.27), computed from the counts:
  - Treated term: $\frac1{100}\big[40\cdot0.7/0.8+10\cdot0.3/0.2\big]=\frac{35+15}{100}=0.5$.
  - Control term: $\frac1{100}\big[10\cdot0.6/0.2+40\cdot0.2/0.8\big]=\frac{30+10}{100}=0.4$.
  - Difference $=0.1$, matching the adjusted value.

The naive estimate is 3.4 times the true effect. Both adjustment routes recover $0.1$ because overlap holds ($0<g<1$) and $X$ is the only common cause.

## Concepts
- [[structural-causal-model]] — ordered assignments: each variable = function of its causes + independent exogenous noise; supports interventions by replacing assignments (p. 1187)
- [[causal-dag]] — graph of which variables are parents of which, leaving the functional forms unspecified; implies a PGM (p. 1188)
- [[fork-chain-collider]] — the chapter states the fork Markov property and collider ($X\to Y\leftarrow Z$) behaviour; conditioning on a collider usually creates dependence (p. 1189)
- [[d-separation]] — recalled (from Ch. 4) as the tool giving independences implied by the graph (p. 1189)
- [[do-operator]] — $P(\cdot\mid \mathrm{do}(A=a))$: distribution in the graph with edges into $A$ deleted, conditioned on $A=a$ (p. 1190)
- [[graph-surgery]] (new) — deleting the edges into the intervened variable and conditioning on its value (p. 1190)
- [[average-treatment-effect]] (new) — $\mathbb E[Y\mid \mathrm{do}(A=1)]-\mathbb E[Y\mid \mathrm{do}(A=0)]$ (p. 1190)
- [[identification]] (new) — an estimand is identified if the assumptions leave a unique value compatible with observed data (p. 1191)
- [[potential-outcomes]] — $Y_i(a)=f_Y(G_i,H_i,a,\xi_{3,i})$; equivalent to graphs, with different practical strengths (pp. 1192–1194)
- [[ladder-of-causation]] — observational, interventional, counterfactual queries, each needing more assumptions (p. 1192)
- [[counterfactual-query]] (new) — needs the within-individual joint of potential outcomes; cross-world; needs functional-form assumptions (p. 1193)
- [[fundamental-problem-of-causal-inference]] — used implicitly: only one potential outcome per individual is observed, so within-individual dependence is not observable (p. 1193)
- [[assignment-mechanism-ignorability]] — here via "all common causes observed" and RCT random assignment; the term "ignorability" is not used in this unit (pp. 1194, 1196)
- [[overlap]] (new) — $0<P(A=1\mid x)<1$ for all $x$; strict version bounds it by $\epsilon$ (p. 1197)
- [[back-door-front-door-criterion]] — backdoor adjustment as the family of estimation strategies here; details deferred to Section 36.8 (p. 1198)
- [[propensity-score]] — $g(x)=P(A=1\mid X=x)$ (p. 1199)
- [[outcome-regression-g-computation]] (new) — fit $\hat Q$, average $\hat Q(1,x_i)-\hat Q(0,x_i)$ (p. 1198)
- [[iptw-estimator]] (new) — inverse-propensity-weighted difference of means (p. 1199)
- [[double-machine-learning-aiptw]] (new) — $\hat Q$ plus propensity correction; doubly robust, efficient, product-of-errors bias (p. 1200)
- [[influence-curve]] (new) — function $\phi$ in (36.31) whose average gives the AIPTW error and whose second moment gives the asymptotic variance (p. 1201)
- [[cross-fitting]] (new) — fit nuisances on other folds for each datapoint (p. 1202)
- [[matching-estimator]] (new) — compare treated to controls with the same $x$; amounts to outcome adjustment with a sample-mean $\hat Q$ (pp. 1203–1204)
- [[confounding-vs-selection-bias]] — confounders (common causes) vs conditioning on colliders/mediators; m-bias as an example (pp. 1196, 1205)
- [[m-bias]] (new) — adjusting for a collider between two unobserved causes of $A$ and $Y$ creates bias (p. 1205)
- [[att]] (new) — average treatment effect on the treated; weaker overlap needed (p. 1206)
- [[randomized-controlled-trial]] (new) — random assignment, so $P(Y\mid \mathrm{do}(A=a))=P(Y\mid a)$ (p. 1194)

## Canonical instances
- [[ice-cream-drowning]] — association with three possible causal explanations (p. 1185)
- [[smoking-cancer-scm]] — running SCM with $A,Y,H,G$ and the DAG of Figure 36.2 (pp. 1187–1189)
- [[horseback-riding-wealth]] — wealth confounds childhood horseback riding and adult health (p. 1196)
- [[drug-sex-overlap]] — a drug given only to males makes the estimand non-identifiable (p. 1197)
- [[m-bias-graph]] — Figure 36.4: adjusting for a collider creates bias (p. 1205)

## Bridges (candidates)
- [structural-analogy] SCM/graph surgery ↔ bayesian: conditioning on an observed value vs overwriting a node — $P(Y\mid \mathrm{do}(A))$ differs from $P(Y\mid A)$ because the parents of $A$ are cut.
- [same-math] Outcome regression $\hat Q$ fitted by squared loss ↔ bayesian: posterior-mean/regression function as the minimiser of expected squared error — both use $\mathbb E[Y\mid\cdot]=\arg\min\mathbb E[(Y-f)^2]$.
- [structural-analogy] Cross-fitting ↔ bayesian: cross-validation — data folds so each prediction comes from a model that did not see that point.
- [structural-analogy] Propensity weighting ↔ bayesian: importance sampling — reweight a sample from $P(X\mid A)$ to look like $P(X)$.
- [structural-analogy] Collider conditioning (m-bias) ↔ bayesian: "explaining away" in Bayesian networks.

## Questions this raises
- How does the do-calculus (Section 36.8) decide which variables suffice for adjustment when the graph is only partly known?
- What can be done when no observed set blocks all backdoor paths (instruments, Section 36.5 is cited)?
- How reliable is the plug-in variance (36.40) in small samples compared with the bootstrap?
- In high dimensions, how can overlap be checked and the trimmed subpopulation justified?

## Reading notes
- **Part boundaries:** this part starts at 36.1 (printed p. 1185, pdf 1219) and ends mid-sentence in 36.4.6 on printed p. 1207 (pdf 1241), at "how well the treatment and". The chapter continues (Sections 36.5, 36.7, 36.8 are referred to but not included).
- **Page offset:** printed = pdf − 34. Running footer (bottom of the pages): "Probabilistic Machine Learning: Advanced Topics", online version, December 10, 2025. The chapter is attributed to Victor Veitch and Alex D'Amour (p. 1185).
- **Figure 36.1 vs text:** the text (p. 1185) says the ice-cream data are for the US in 1931 and the smoking data are "across various countries". The printed figure title reads "…USA, 2020", and panel (b) shows US cigarette sales and lung cancer mortality over time.
- **Possible misprints (as the image shows):**
  - p. 1188: the implied factorisation is printed $P(G)P(H)P(A\mid H)P(Y\mid A,H)$, but (36.8) has $Y$ depending on $G$ too. On p. 1187, "$(A_i,Y_i,H_i)\sim P^{\mathrm{obs}}$" omits $G_i$.
  - p. 1202: the condition is stated as the product of errors being "$o(\sqrt n)$". Taken with the preceding condition $\sqrt n\times(\text{product})\to0$, it should read $o(1/\sqrt n)$. The "weak condition" just before (36.39) is printed without square roots, unlike the earlier form.
  - p. 1207: the parentheses in (36.45) are unbalanced. In (36.46) $\phi^{\mathrm{ATT}}$ already contains $\frac1n\sum_i$ and (36.47) sums again, so one of the two sums seems redundant. I transcribed both, closing the unbalanced parentheses in the most natural way (so the grouping in my (36.45) and (36.46) is regrouped, not literally as printed).
  - p. 1205: m-bias prose calls the collider $D$; Figure 36.4 calls it $X$.
- **Numbering:** Theorem 2 and Definitions 1–3 are numbered as printed (no Theorem 1 appears in these pages).
- No exercises appear in this part.
