---
id: hernan-2020-whatif/ch01-definition
work: hernan-2020-whatif
unit: "Introduction (Towards less casual causal inferences) and Chapter 1: A definition of causal effect"
pages: vii–viii, 3–12
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# A definition of causal effect

## L0 — One line
A causal effect is a contrast between outcomes in the same population under different treatments (counterfactual worlds), and this is a different quantity from an association between treatment and outcome among those who actually received each treatment.

## L1 — The gist (≤ 120 words)
The authors want causal questions and assumptions stated explicitly. Chapter 1 gives the notation for that. Each person has a potential outcome under each treatment value. An individual effect compares the two potential outcomes, but only one is ever observed, so individual effects cannot be identified (computed from observed data). Population effects compare average (marginal) risks if everyone were treated versus if no one were. Effect measures include the risk difference, risk ratio and odds ratio. Association compares conditional risks in the treated and the untreated. The two can disagree, for example if the treated are sicker (confounding). Random error comes from sampling and possibly from nondeterministic (random) counterfactuals; it is largely ignored until Chapter 10.

**Prerequisites:** proportions and averages; conditional probability; the idea of a random variable and expected value.

## L2 — Key ideas
- The book aims at causal inference that states its causal question and assumptions. It claims causal inference cannot be reduced to data-analysis recipes (p. vii).
- Potential (counterfactual) outcomes $Y^{a=1}, Y^{a=0}$ define an individual causal effect: $Y^{a=1}\neq Y^{a=0}$ for that person (p. 4).
- Consistency, $Y=Y^A$, links the observed outcome to the potential outcome for the treatment actually received. Only one potential outcome is observed per person, so the other is missing and individual effects are not identified (p. 4).
- The average causal effect is $E[Y^{a=1}]-E[Y^{a=0}]$. It equals the mean of individual effects. It can be null while many individuals are harmed and helped (p. 5–6).
- Risk difference, risk ratio, odds ratio and number needed to treat are different scales for one causal effect, and the risk ratio and risk difference may serve different purposes (p. 7–8).
- Random error has two sources: sampling variability and nondeterministic counterfactuals. Both are largely set aside until Chapter 10 (p. 8–9).
- Causation contrasts marginal risks in the whole population under two treatments. Association contrasts conditional risks in two disjoint subgroups (p. 11–12).

## L3 — Walkthrough

### Introduction (pp. vii–viii)
- The authors write for scientists, especially health and social scientists. They want analyses that state both the causal question and the assumptions behind the data analysis (p. vii).
- They criticise studies that leave the question unstated and the assumptions undeclared. With the foundations in place, causal inferences become "necessarily less casual" (p. vii).
- The book is "not a philosophy book": it stays agnostic about metaphysical notions of causality. It concerns identification and estimation of population causal effects, meaning numerical changes in the outcome distribution under different interventions (p. vii).
- Structure: Part I is causal inference without models (nonparametric identification). Part II is with parametric models. Part III covers time-varying treatments. Fine Points are designed to be accessible to all readers. Technical Points are designed for readers with intermediate training in statistics (p. vii).
- The book is a synthesis of the authors' teaching and research, not a systematic review (p. viii).

### Chapter intro (p. 3)
- The reader already has causal intuition. Examples are the toddler, the teenage skier and the parent with antibiotics: each is a case where acting on a raw association would have been harmful, and the text says the reader's causal intuition prevented this. The chapter only adds notation that formalises this intuition, and the notation is used throughout the book (p. 3).

### 1.1 Individual causal effects (pp. 3–4)
- Vignettes: Zeus is transplanted and dies five days later. By stipulated knowledge, he would have lived without the transplant. So the transplant caused his death. Hera is transplanted and lives, and would have lived anyway, so there is no effect (p. 3).
- Humans compare the outcome when an action is taken with the outcome when it is withheld. If they differ, the action has a causal effect, causative or preventive (p. 3).
- Notation: $A$ is a dichotomous treatment (1 treated, 0 untreated). $Y$ is a dichotomous outcome (1 death, 0 survival). Capitals are random variables, lower case are particular values (p. 3).
- $Y^{a=1}$ is the outcome that would be observed under $a=1$. $Y^{a=0}$ is the outcome under $a=0$. Zeus has $Y^{a=1}=1, Y^{a=0}=0$. Hera has $Y^{a=1}=0=Y^{a=0}$ (p. 4).
- **Definition (individual causal effect):** $A$ has a causal effect on an individual's $Y$ if $Y^{a=1}\neq Y^{a=0}$ for that individual. The individual effect is $Y_i^{a=1}-Y_i^{a=0}$ (p. 4).
- $Y^{a}$ are called potential or counterfactual outcomes. "Potential" stresses that either can potentially be observed. "Counterfactual" stresses that they describe situations that may not occur (p. 4).
- **Consistency:** an individual with observed treatment $A=a$ has observed outcome equal to the counterfactual $Y^a$. This is written $Y=Y^A$, i.e. if $A_i=a$ then $Y_i^a=Y_i^A=Y_i$ (p. 4).
- Only one counterfactual outcome is observed per individual. The rest is missing data, so individual effects cannot be identified, i.e. expressed as a function of observed data. Fine Point 2.1 is cited as a possible exception (p. 4).
- A margin note says that, for a specific individual such as Zeus, $Y_i^a$ is not random, because individual counterfactuals are assumed deterministic (see Technical Point 1.2) (p. 4).

*Intuition note.* To know whether the heart hurt Zeus, we need his outcome in two worlds, but we see only one. This is why individual effects cannot be identified (p. 4).

### 1.2 Average causal effects (pp. 4–6)
- An individual effect needs three things: an outcome, the two actions, and the individual. An average effect needs an outcome, the two actions, and a well-defined population (p. 4).
- **Table 1.1** lists $Y^{a=0}, Y^{a=1}$ for 20 members of Zeus's family. Ten of 20 would die if all were treated, so $\Pr[Y^{a=1}=1]=10/20=0.5$. Ten of 20 would die if none were treated, so $\Pr[Y^{a=0}=1]=10/20=0.5$ (pp. 4–5).
- For a dichotomous outcome, the risk equals the average of the counterfactual outcomes, i.e. deaths divided by 20 (p. 5).
- **Definition (average causal effect):** present if $\Pr[Y^{a=1}=1]\neq\Pr[Y^{a=0}=1]$ in the population of interest (p. 5). Here it is absent, since both risks are 0.5. When it is absent, the null hypothesis of no average causal effect is true (p. 5).
- Using $E$ for the population mean, a non-null effect is $E[Y^{a=1}]\neq E[Y^{a=0}]$. This covers dichotomous and nondichotomous outcomes (p. 5).
- **Fine Point 1.1 (interference).** The definition of $Y_i^a$ assumes that individual $i$'s counterfactual does not depend on others' treatment values. If Hera's transplant upset Zeus so that he would die, her treatment would interfere with his outcome. Then "the causal effect on Zeus" is not well defined without saying what Hera and others receive. This is common with contagious agents or educational programmes. No interference is "no interaction between units" (Cox 1958) and is part of SUTVA (Rubin 1980). The book assumes no interference unless stated (p. 5).
- **Technical Point 1.1.** For discrete outcomes $E[Y^a]=\sum_y y\,p_{Y^a}(y)$ with $p_{Y^a}(y)=\Pr[Y^a=y]$. For continuous outcomes $E[Y^a]=\int y f_{Y^a}(y)\,dy$. A general form is $E[Y^a]=\int y\,dF_{Y^a}(y)$, with $F$ the cdf (cumulative distribution function). A non-null effect exists if $E[Y^a]\neq E[Y^{a'}]$ for any two values $a,a'$ (p. 6).
  - A population effect may contrast other functionals, such as median, variance, hazard or cdf, of the marginal distributions of $Y^a$ (p. 6).
  - In Table 1.1 the distributions of $Y^{a=1}$ and $Y^{a=0}$ are identical (10 deaths of 20). So every such functional contrast is zero, e.g. $Var(Y^{a=1})-Var(Y^{a=0})=0$ (p. 6).
  - But $Var(Y^{a=1}-Y^{a=0})>0$, since $Y^{a=1}-Y^{a=0}$ is $-1$ for 6 individuals, $1$ for 6 and $0$ for 8. Unlike the mean, the difference of variances does not in general equal the variance of individual effects (p. 6).
  - A randomized trial can identify $Var(Y^{a=1})-Var(Y^{a=0})$ but not $Var(Y^{a=1}-Y^{a=0})$. The covariance of $Y^{a=1}$ and $Y^{a=0}$ is not identified, because both are never seen together. This holds for any nonlinear functional (p. 6).
- When treatment is not dichotomous, the contrast must be specified. "The causal effect of aspirin" is meaningless until stated, e.g. 150 mg by mouth daily for 5 years versus no aspirin. That effect is well defined even if other interventions are not (p. 6).
- A null average effect does not imply null individual effects. In Table 1.1 treatment has an individual effect on 12 members. Six are harmed ($Y^{a=1}-Y^{a=0}=1$, including Zeus) and 6 are helped ($-1$) (p. 6).
- This is not an accident: $E[Y^{a=1}]-E[Y^{a=0}]=E[Y^{a=1}-Y^{a=0}]$ always, since a difference of averages equals the average of differences (p. 6).
- **Sharp causal null hypothesis:** $Y^{a=1}=Y^{a=0}$ for all individuals. It implies the null of no average effect (p. 6). The converse is not true, as Table 1.1 shows (p. 6).
- Average effects can sometimes be identified even when individual effects cannot. From now on "causal effect" means average causal effect, and the "causal null hypothesis" is the null of no average effect (p. 6).

*Intuition note.* Positive and negative individual effects can cancel in the average. "No average effect" therefore does not mean "nobody was affected."

### 1.3 Measures of causal effect (p. 7)
- The causal null can be written in three equivalent ways. The left-hand sides are the causal risk difference, risk ratio and odds ratio (p. 7):

$$\text{(i)}\ \Pr[Y^{a=1}=1]-\Pr[Y^{a=0}=1]=0$$
$$\text{(ii)}\ \frac{\Pr[Y^{a=1}=1]}{\Pr[Y^{a=0}=1]}=1$$
$$\text{(iii)}\ \frac{\Pr[Y^{a=1}=1]/\Pr[Y^{a=1}=0]}{\Pr[Y^{a=0}=1]/\Pr[Y^{a=0}=0]}=1$$

- If the null fails, as in the example of smoking and lung cancer, these three are no longer 0, 1 and 1. They measure the strength of the same effect on different scales and are called effect measures (p. 7).
- A margin note: the causal risk difference is the average of the individual effects $Y^{a=1}-Y^{a=0}$. The causal risk ratio is not the average of any individual effects (p. 7).
- Example: 3 per million would develop the outcome if treated and 1 per million if untreated. The risk ratio is 3. The risk difference is 0.000002. The ratio (multiplicative scale) shows how many times treatment raises risk. The difference (additive scale) gives the absolute number of attributable cases. The choice depends on the goal (p. 7).
- **Fine Point 1.2 (number needed to treat).** Take 100 million patients, 20 million dying in five years if treated and 30 million if untreated. The risk difference is $0.2-0.3=-0.1$. That means 10 million fewer deaths if all are treated, so on average 10 patients must be treated to save 1 life. This is the NNT. When the risk difference is negative (p. 8):
$$NNT=\frac{-1}{\Pr[Y^{a=1}=1]-\Pr[Y^{a=0}=1]}$$
  Here $NNT=10$. When the risk difference is positive, one can define a number needed to harm. Like the risk difference, the NNT applies to the population and time interval it is based on (p. 8).

*Intuition note.* The same pair of risks can be reported as a difference, a ratio, an odds ratio or an NNT. The numbers differ, but they describe one underlying causal contrast.

### 1.4 Random variability (pp. 7–9)
- Real studies observe a sample, not the whole population. So $\Pr[Y^{a=0}=1]$ cannot be directly computed, only estimated (pp. 7–8).
- **1st source: sampling variability.** Treat the 20 people as a random sample of a near-infinite super-population. The sample proportion $\widehat{\Pr}[Y^{a=0}=1]=10/20=0.50$ need not equal the super-population probability. For example, the latter might be 0.57 (p. 8).
- $\widehat{\Pr}[Y^a=1]$ is a consistent estimator of $\Pr[Y^a=1]$: the difference is expected to shrink as the sample grows, because sampling error is random and obeys the law of large numbers (p. 8). A margin note says an estimator $\hat\theta$ is consistent if, with probability approaching 1, $\hat\theta-\theta$ approaches zero as the sample size goes to infinity. It also cautions that this "consistency" differs from consistency of counterfactuals (pp. 8–9).
- Since the probabilities are only estimated, one cannot be certain whether there is a causal effect. A statistical procedure must assess the evidence on $\Pr[Y^{a=1}=1]=\Pr[Y^{a=0}=1]$ (Chapter 10) (p. 9).
- **2nd source: nondeterministic counterfactuals.** Counterfactuals so far are fixed (Zeus: 100% death if treated, 0% if untreated). One could instead imagine 90% and 10%. Then Table 1.1 would show one realisation of "random flips of mortality coins," with probabilities varying across individuals. The text says quantum mechanics holds such uncertainty to be irreducible (p. 9).
- **Technical Point 1.2.** For nondeterministic outcomes, $E[Y^a]=\sum_y y\,p_{Y^a}(y)$, with $p_{Y^a}(\cdot)=E[Q_{Y^a}(\cdot)]$ and $Q_{Y^a}(y)$ a random probability of outcome $y$ under $a$. For Zeus $Q_{Y^{a=1}}(1)=0.9$ in the example. More generally each individual has a random cdf $\Theta_{Y^a}(\cdot)$ and
$$E[Y^a]=E\{E[Y^a\mid\Theta_{Y^a}(\cdot)]\}=E\!\left[\int y\,d\Theta_{Y^a}(y)\right]=\int y\,d\,E[\Theta_{Y^a}(y)]=\int y\,dF_{Y^a}(y),$$
  where $F_{Y^a}(\cdot)=E[\Theta_{Y_i^a}(\cdot)]$ (p. 10). For binary nondeterministic outcomes, the causal risk ratio $E[Q_{Y^{a=1}}(1)]/E[Q_{Y^{a=0}}(1)]$ equals the weighted average $E[W\{Q_{Y^{a=1}}(1)/Q_{Y^{a=0}}(1)\}]$ of individual ratio effects. The weights are $W=Q_{Y^{a=0}}(1)/E[Q_{Y^{a=0}}(1)]$. The text requires $Q_{Y^{a=0}}(1)$ never to equal 0 for anyone (p. 10).
- Until Chapter 10, the authors assume deterministic counterfactuals and data on everyone in a very large super-population. This is like 20 billion people, with 1 billion identical to Zeus, 1 billion identical to Hera, and so on. The computations are then "with Olympian certainty" (p. 9).
- Chapter 10 is said to show that estimates and confidence intervals for super-population effects are identical whether the world is stochastic or deterministic. Intervals for the effect in the actual sample differ between the two. Super-population effects are "in most cases" the effects of interest (p. 9).

### 1.5 Causation versus association (pp. 9–12)
- Real data show only one outcome per person: observed $A$ and $Y$ (Table 1.2) (pp. 9–10).
- **Conditional probability:** $\Pr[Y=1\mid A=a]$ is the proportion with the outcome among those who happened to receive $a$. In Table 1.2, 7 of the 13 treated died, so $\Pr[Y=1\mid A=1]=7/13$ (p. 10).
- **Independence** $Y\perp\!\!\!\perp A$ (symbol from Dawid 1979) means $\Pr[Y=1|A=1]=\Pr[Y=1|A=0]$, so $A$ is not associated with $Y$ and does not predict it. Equivalent forms are the associational risk difference $=0$, risk ratio $=1$, and odds ratio $=1$ (p. 10):
$$\text{(i)}\ \Pr[Y=1|A=1]-\Pr[Y=1|A=0]=0;\quad \text{(ii)}\ \frac{\Pr[Y=1|A=1]}{\Pr[Y=1|A=0]}=1;\quad \text{(iii)}\ \frac{\Pr[Y=1|A=1]/\Pr[Y=0|A=1]}{\Pr[Y=1|A=0]/\Pr[Y=0|A=0]}=1.$$
- Dependent (associated) means $\Pr[Y=1|A=1]\neq\Pr[Y=1|A=0]$. In the example $7/13\neq 3/7$ (p. 10). These measures are association measures and also suffer from random variability, which is ignored until Chapter 10 (p. 11).
- For a dichotomous outcome the risk equals the average, so association means $E[Y|A=1]\neq E[Y|A=0]$. For continuous $Y$, mean independence is $E[Y|A=1]=E[Y|A=0]$ (margin). For binary $A$, no association holds if and only if $A$ and $Y$ are not statistically correlated (p. 11).
- **Figure 1.1** (diamond): causation contrasts the whole population treated with the whole population untreated, $E[Y^{a=1}]$ versus $E[Y^{a=0}]$. Association contrasts the treated part with the untreated part, $E[Y|A=1]$ versus $E[Y|A=0]$ (p. 11). In the example, there is no causal effect (10/20 versus 10/20) but there is an association (13 treated versus 7 untreated) (p. 11).
- Causal questions are "what if" questions about counterfactual worlds. Associational questions are about the actual world (p. 11).
- Formally, $\Pr[Y=1|A=a]$ is a conditional probability, over the subset with actual treatment $a$. $\Pr[Y^a=1]$ is unconditional (marginal), over the entire population. Association is a different risk in two disjoint subsets. Causation is a different risk in the same population under two treatments (pp. 11–12).
- The term "causal effect" is used redundantly, to avoid the common use of "effect" for mere association (p. 12).
- This explains "association is not causation." Treated risk 7/13 exceeds untreated risk 3/7, but risk if all were treated (10/20) equals risk if none were (10/20). The discrepancy would not surprise if transplant recipients were on average sicker. Chapter 7 calls this confounding (p. 12).
- Margin example: the causal risk ratio of 5-year mortality for aspirin versus none is 0.5, but the associational risk ratio is 1.5, because high-risk patients are preferentially given aspirin. A physician who withholds aspirin because treated patients die more often would be sued for malpractice (p. 12).
- Causal inference needs data like Table 1.1, but we only get data like Table 1.2. The question is when real data can be used. The next chapter gives one answer: conduct a randomized experiment (p. 12).

*Intuition note.* Causation asks what happens if we change everyone's treatment. Association asks how treated and untreated people already differ. If the two groups differ in other ways, such as health, the two answers can differ.

## Toy example (ours, not from the text)
Eight people, with both potential outcomes shown (which we could not see in reality), actual treatment $A$ and observed $Y=Y^A$:

| Person | $Y^{a=0}$ | $Y^{a=1}$ | $A$ | $Y$ |
|---|---|---|---|---|
| P1 | 1 | 1 | 1 | 1 |
| P2 | 1 | 1 | 1 | 1 |
| P3 | 0 | 0 | 0 | 0 |
| P4 | 0 | 0 | 0 | 0 |
| P5 | 1 | 0 | 0 | 1 |
| P6 | 0 | 1 | 1 | 1 |
| P7 | 1 | 0 | 1 | 0 |
| P8 | 0 | 1 | 0 | 0 |

- Causal: $\Pr[Y^{a=1}=1]=4/8=0.5$ (P1, P2, P6, P8). $\Pr[Y^{a=0}=1]=4/8=0.5$ (P1, P2, P5, P7). Causal risk difference $=0$, risk ratio $=1$. The causal null holds.
- Individual effects $Y^{a=1}-Y^{a=0}$: P1–P4 give 0. P5 $=-1$, P6 $=+1$, P7 $=-1$, P8 $=+1$. The mean is $(0-1+1-1+1)/8=0$, matching $0.5-0.5$. Two are helped and two harmed, so the sharp null is false.
- Association: treated are P1, P2, P6, P7 with $Y=1,1,1,0$, so $\Pr[Y=1|A=1]=3/4$. Untreated are P3, P4, P5, P8 with $Y=0,0,1,0$, so $\Pr[Y=1|A=0]=1/4$. The associational risk difference is $0.5$ and the risk ratio is $3$.
- Treatment is associated with death without causing any change in the average. The two always-die people (P1, P2) were all treated.

## Concepts
- [[potential-outcomes]] — $Y^{a}$: the outcome that would be observed under treatment value $a$; called counterfactual when it may not occur (p. 4)
- [[fundamental-problem-of-causal-inference]] — only the outcome for the received treatment is observed, so individual effects are not identified (p. 4)
- [[consistency-counterfactual]] (new) — $Y=Y^A$: observed outcome equals the potential outcome for the received treatment (p. 4)
- [[individual-causal-effect]] (new) — $Y_i^{a=1}\neq Y_i^{a=0}$ (p. 4)
- [[average-causal-effect]] (new) — present if $E[Y^{a=1}]\neq E[Y^{a=0}]$; the contrast $E[Y^{a=1}]-E[Y^{a=0}]$ equals the mean of the individual effects (pp. 5–6)
- [[sharp-causal-null]] (new) — $Y^{a=1}=Y^{a=0}$ for every individual; implies no average effect (p. 6)
- [[effect-measures]] (new) — causal risk difference, ratio and odds ratio: scales of one causal effect (p. 7)
- [[number-needed-to-treat]] (new) — reciprocal of the absolute causal risk difference, for a harm-reducing treatment (p. 8)
- [[SUTVA]] — here "no interference": an individual's outcome does not depend on others' treatments. Fine Point 1.1 names it as a component of Rubin's SUTVA (p. 5)
- [[super-population-and-random-error]] (new) — sampling variability and nondeterministic counterfactuals; consistent estimators (pp. 8–9)
- [[association-vs-causation]] (new) — conditional risks in treated and untreated subsets versus marginal risks under two treatments (pp. 11–12)
- [[independence]] (new) — $Y\perp\!\!\!\perp A$: equal conditional risks; mean independence for continuous $Y$ (pp. 10–11)

## Canonical instances
- [[zeus-hera-transplant]] — individual effect present for Zeus, absent for Hera (pp. 3–4)
- [[table-1-1-zeus-family]] — null average effect with 12 individual effects, 6 harmed and 6 helped (pp. 5–6)
- [[table-1-2-association]] — association ($7/13$ versus $3/7$) without causation (pp. 10, 12)
- [[aspirin-malpractice]] — causal risk ratio 0.5 versus associational 1.5 (p. 12)
- [[nnt-100-million]] — 20 versus 30 million deaths gives NNT 10 (p. 8)

## Bridges (candidates)
- [structural-analogy] marginal $\Pr[Y^a=1]$ versus conditional $\Pr[Y=1|A=a]$ ↔ causal-DAG field: $P(Y|do(X=x))$ versus $P(Y|X=x)$ — same intervention-versus-observation distinction in a different notation.
- [structural-analogy] individual-specific random probability $Q_{Y^a}$ with population mean $E[Q]$ ↔ Bayesian: hierarchical model with per-unit parameters drawn from a population.
- [structural-analogy] individual effects unidentified because the other potential outcome is missing ↔ Bayesian: unobserved quantities treated as unknowns with a prior.
- [metaphor] super-population as 20 billion copies of 20 types ↔ Bayesian: a population distribution of types.

## Questions this raises
- Under what conditions does the conditional risk $\Pr[Y=1|A=a]$ equal the marginal risk $\Pr[Y^a=1]$? (The text points to randomisation in Chapter 2.)
- If individual effects cannot be identified, what is lost when we only report average effects?
- How do estimates and intervals change when the counterfactuals are stochastic rather than deterministic (Chapter 10)?
- What does a causal contrast mean when treatments interfere or when "the treatment" is poorly specified?

## Reading notes
- The source PDF is the online revision dated 2026-08-19, not the 2020 print version. Chapter numbering may differ from older citations.
- The unit includes the Introduction. Its page images are not shown. Its pdf pages have no printed label; the text layer shows "viii" on the second page, so I cite them as p. vii and p. viii. Chapter pages: printed = pdf − 9.
- Table 1.2 appears only as its first rows (Rheia 0,0; Kronos 0,1). The counts 7/13 and 3/7 are from the text, not recomputed from the table.
- I checked Table 1.1 against the image. 10 of 20 have $Y^{a=1}=1$, 10 of 20 have $Y^{a=0}=1$, 12 have differing outcomes, 6 harmed and 6 helped.
- In the independence list on p. 10 the text says "left-hand side of the inequalities (i), (ii), (iii)"; the context shows equalities are meant.
- Technical Point 1.2's condition "never equal to 0 (i.e., deterministic)" is reproduced as printed.
- Fine Point 2.1 and Chapters 7 and 10 are only referenced here, not covered.
