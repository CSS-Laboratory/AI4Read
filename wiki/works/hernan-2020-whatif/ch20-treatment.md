---
id: hernan-2020-whatif/ch20-treatment
work: hernan-2020-whatif
unit: "Chapter 20 — Treatment-confounder feedback"
pages: 267-276
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Treatment-confounder feedback

## L0 — One line
When a time-varying confounder is itself affected by earlier treatment, ordinary adjustment (stratification, regression, matching) can create bias even though all the needed data are measured.

## L1 — The gist (≤ 120 words)
Chapter 19 gave conditions (sequential exchangeability) for identifying effects of treatment strategies. This chapter asks which adjustment method then works. If a confounder $L_1$ affects later treatment and is also affected by earlier treatment $A_0$ (feedback), conditioning on $L_1$ opens a path through a collider. A hypothetical HIV trial with a true null effect gives −13.3 unadjusted and −8 after stratifying on $L_1$. Regression is itself stratification-based, and a similar argument applies to matching, so these methods fail too. The chapter also shows that adjusting for past treatment is generally needed, and that mismeasured past treatment can bias results under the null. The cure, g-methods, comes later.

**Prerequisites:** potential outcomes; causal diagrams and colliders; stratification and regression as adjustment; conditional expectation and weighted averages.

## L2 — Key ideas
- Treatment-confounder feedback: a time-varying confounder affects later treatment and is affected by earlier treatment (or shares a cause with it). Time-varying confounding can exist without it. (pp. 267, 269)
- Even with sequential exchangeability, positivity and consistency, traditional methods "will not generally" give a valid estimate under feedback. (pp. 268–269)
- Mechanism: stratifying on $L_1$ conditions on a collider. It opens $A_0 \to L_1 \leftarrow U_1 \to Y$, so it removes confounding for $A_1$ and adds selection bias for $A_0$. (pp. 271–272)
- Worked numbers: the true effect is 0. The unadjusted contrast is −13.3 and the $L_1$-stratified contrast is −8 in both strata. (pp. 270–271)
- Regression cannot repair this, because regression is itself a stratification-based method. (p. 273)
- The bias also arises when $L_1$ and $A_0$ share a cause $W_0$, and with non-null effects and many time points. (p. 272)
- Sequential exchangeability generally requires conditioning on past treatment. Omitting it, or mismeasuring it, can bias even effects of a time-fixed treatment. (pp. 274–275)

## L3 — Walkthrough

### Introduction (p. 267)
Assume the strongest sequential exchangeability holds. The measured time-varying confounders then suffice to validly estimate the effect of any strategy. The question is which adjustment method to use. When treatment-confounder feedback exists, traditional methods may introduce bias (p. 267).

### 20.1 The elements of treatment-confounder feedback (pp. 267–269)
- Setting: the sequentially randomized HIV trial of Chapter 19. At month $k=0,\dots,K$ we have treatment $A_k$ (1 treated, 0 untreated) and covariates $L_k$. The outcome $Y$ is health status at month $K+1$. There is no censoring (p. 267).
- In Figure 20.1, CD4 count $L_k$ affects treatment $A_k$, and treatment $A_{k-1}$ raises later CD4 count $L_k$. The confounder affects treatment and treatment affects the confounder. This is **treatment-confounder feedback** (p. 267).
- Figure 20.2 deletes the arrows from $A_{k-1}$ to $L_k$ and $U_k$. There is still time-varying confounding but no feedback (p. 267).
- **Fine Point 20.1.** An acyclic graph can show a feedback loop by unrolling it in time: $A_{k-1}\to L_k\to A_k\to L_{k+1}$. This needs time to be discrete: changes happen within intervals $[k,k+1)$, and the exact moment is unspecified. Interval length can be chosen to fit the data (p. 268).
- Figure 20.3 is the smallest diagram showing feedback with two time points. It makes four simplifications (p. 268):
  - no baseline $L_0$; $A_0$ is marginally randomized and $A_1$ is randomized given $L_1$;
  - no $U_0$;
  - no arrow $A_0\to A_1$, so treatment is assigned using $L_1$ only;
  - no arrows from $A_0, L_1, A_1$ to $Y$ (the sharp null: treatment has no effect on any individual's $Y$).
- The target is $\mathrm{E}[Y^{a_0=1,a_1=1}]-\mathrm{E}[Y^{a_0=0,a_1=0}]$ ("always treat" vs "never treat"). In Figure 20.3 it is 0, because no forward path leads from $A_0$ or $A_1$ to $Y$. The investigators do not know this (p. 268).
- No arrows run from $U$ into treatment, so the diagram can depict a sequentially randomized trial and the effect is identifiable. Yet adjusting for $L_1$ by stratification, outcome regression or matching will generally give a non-zero, invalid estimate (p. 268).
- Figure 20.4 replaces the arrow $A_0\to L_1$ by a shared cause $W_0$ of $A_0$ and $L_1$. This is an observational-study version. Both figures count as feedback examples. G-methods, unlike traditional methods, adjust appropriately (p. 269).

*Intuition note:* Feedback means $L_1$ is both a cause of later treatment (so we want to adjust for it) and an effect of earlier treatment (so adjusting is risky). Simple diagrams already show the problem.

### 20.2 The bias of traditional methods (pp. 269–271)
**Trial.** There are 32,000 people, $k=0,1$, and an ideal trial (full adherence, no loss to follow-up). $A_0=1$ has probability 0.5. $A_1$ is given with probability 0.4 if $L_1=0$ (high CD4) and 0.8 if $L_1=1$ (low CD4). Higher $Y$ means better health (p. 269).

Table 20.1 (p. 269):

| N | $A_0$ | $L_1$ | $A_1$ | Mean $Y$ |
|---|---|---|---|---|
| 2400 | 0 | 0 | 0 | 84 |
| 1600 | 0 | 0 | 1 | 84 |
| 2400 | 0 | 1 | 0 | 52 |
| 9600 | 0 | 1 | 1 | 52 |
| 4800 | 1 | 0 | 0 | 76 |
| 3200 | 1 | 0 | 1 | 76 |
| 1600 | 1 | 1 | 0 | 44 |
| 6400 | 1 | 1 | 1 | 44 |

Sequential exchangeability, positivity and consistency hold. Positivity holds because no row is empty (p. 269).

**Checking the null (ignoring random variability).**
- Effect of $A_1$ within each stratum of $(A_0,L_1)$ is zero. Example: $\mathrm{E}[Y|A_0=0,L_1=0,A_1=1]-\mathrm{E}[Y|A_0=0,L_1=0,A_1=0]=84-84=0$. Rows 3–4, 5–6 and 7–8 give the same (pp. 269–270).
- Effect of $A_0$: randomization makes $\mathrm{E}[Y|A_0=1]-\mathrm{E}[Y|A_0=0]$ valid. Using the weighted averages (the text's "treated at time 0" for the first group is a slip; see Reading notes):
$$\mathrm{E}[Y|A_0=0]=\tfrac{2400}{16000}84+\tfrac{1600}{16000}84+\tfrac{2400}{16000}52+\tfrac{9600}{16000}52=60,$$
and $\mathrm{E}[Y|A_0=1]=60$ analogously. The effect is zero (p. 270).
- **Technical Point 20.1 (g-null test).** Under the sharp null, $Y^g=Y$. Sequential exchangeability then reads $Y\perp\!\!\!\perp A_0|L_0$ and $Y\perp\!\!\!\perp A_1|A_0,L_0,L_1$. Under sequential exchangeability, testing these is a test of the sharp null. The **g-null theorem** (Robins 1986) says: under sequential randomization for all $g$, these independencies hold if and only if the distribution (hence mean) of $Y^g$ is the same for all $g$ and equal to that of observed $Y$ (p. 270).
- So the "always treat" vs "never treat" effect should be 0 (p. 270).

**Two analyses (p. 270–271).**
1. No adjustment for $L_1$: compare those treated at both times (rows 6, 8) with untreated at both (rows 1, 3).
$$\mathrm{E}[Y|A_0=1,A_1=1]=\tfrac{3200}{9600}76+\tfrac{6400}{9600}44=54.7,\qquad \mathrm{E}[Y|A_0=0,A_1=0]=\tfrac{2400}{4800}84+\tfrac{2400}{4800}52=68.0.$$
The difference is $54.7-68=-13.3$, not 0. Adjustment for $L_1$ is needed.
2. Stratify on $L_1$. For $L_1=0$: $\mathrm{E}[Y|A_0=1,L_1=0,A_1=1]-\mathrm{E}[Y|A_0=0,L_1=0,A_1=0]=76-84=-8$ (rows 6 and 1). For $L_1=1$ the difference is also $-8$. Since both strata give $-8$, no weighted average of them can equal 0 (p. 271).

*Intuition note:* The data come from a valid trial and the true effect is 0. Yet the unadjusted contrast is −13.3, and the "properly adjusted" contrast is −8 in every stratum. Stratifying on $L_1$ is not a cure here.

### 20.3 Why traditional methods fail (pp. 271–273)
- All three identifiability conditions hold, so $U_1$ is not needed given $L_1$. The method, not the data, is the problem (p. 271).
- Stratification means estimating the association within strata of $L_1$. When $L_1$ is caused by $A_0$, it is a collider. Conditioning on it opens $A_0\to L_1\leftarrow U_1\to Y$ (Figure 20.5). This induces an association between $A_0$ and $U_1$, hence between $A_0$ and $Y$ (p. 271).
- Among $L_1=1$ (low CD4), being treated at time 0 becomes a marker of severe immunosuppression (high $U_1$). Among $L_1=0$, being untreated becomes a marker of milder immunosuppression (low $U_1$) (pp. 271–272).
- So stratification eliminates confounding for $A_1$ at the cost of selection bias for $A_0$. The contrasts $\mathrm{E}[Y|A_0=1,L_1=l,A_1=1]-\mathrm{E}[Y|A_0=0,L_1=l,A_1=0]$ can be non-zero under the null. The net bias depends on the relative size of the confounding removed and the selection bias created (p. 272).
- Same problem with a shared cause $W_0$ (Figure 20.6): conditioning on $L_1$ opens $A_0\leftarrow W_0\to L_1\leftarrow U_1\to Y$. Figures 20.3 and 20.4 cannot be told apart from observed data (p. 272).
- Non-null effects (Figure 20.7) do not remove the problem: conditioning on $L_1$ still creates a non-causal $A_0$–$Y$ association. More time points and variables do not help; time-varying confounders affected by past treatment at many times increase the possibility of a large bias (p. 272).
- **Fine Point 20.2.** Selection bias can occur even when $L_1$ is not on a causal path from treatment to outcome (Figures 20.5, 20.6). In Figure 20.7, $L_1$ is on the path $A_0\to L_1\to Y$. Without $U_1$ as a common cause of $L_1$ and $Y$, $A$–$Y$ associations within $L_1$ strata would estimate the direct effect of $A_0$ not through $L_1$, not the overall effect. The author calls the claim that a variable on a causal pathway cannot be a confounder "inaccurate" for time-varying treatments. Whether adjusting for such confounders induces bias depends on the method: stratification does, g-methods do not (p. 272).
- Valid estimation of strategy effects requires estimating the joint effect of the components $A_k$ simultaneously and without bias. Stratification may fail at this even with all confounders measured (p. 273).

*Intuition note:* Stratifying on a variable that treatment helps to cause selects people in a treatment-dependent way. Within a stratum, treatment status then carries information about the hidden cause $U_1$ and so about $Y$.

### 20.4 Why traditional methods cannot be fixed (pp. 273–274)
- Stratified tables become impossible in high dimensions. With $K$ about 100 there are $2^{100}$ static strategies, far more than any sample size. Dynamic strategies add more (p. 273).
- Modeling is then needed, with a dose-response function. Example: effect increases linearly with cumulative treatment, so, under this assumption, all strategies with exactly three months of treatment have the same effect, whichever months those are. The price is possible misspecification (p. 273).
- Modeling gives no protection from the feedback problem, because regression is itself a stratification-based method (p. 273).
- Example under Figure 20.5: $cum(\bar A)=A_0+A_1\in\{0,1,2\}$. Assuming the mean outcome depends linearly on $cum(\bar A)$, fit
$$\mathrm{E}[Y|\bar A,L_1]=\theta_0+\theta_1\,cum(\bar A)+\theta_2L_1 .$$
Then $\mathrm{E}[Y|cum(\bar A)=2,L_1]-\mathrm{E}[Y|cum(\bar A)=0,L_1]=\theta_1\times 2$. Reading this as a causal effect is unwarranted: conditioning on $L_1$ induces an $A_0$–$Y$ association, so $\theta_1$ is non-zero even if the true effect is zero and the regression model is correct (p. 274).
- A similar argument applies to matching. G-methods are needed (p. 274).

### 20.5 Adjusting for past treatment (pp. 274–275)
- Add an arrow $A_0\to A_1$ (doctors use treatment history). In Figures 20.8 and 20.9, conditioning on $L_1$ is then insufficient to block all back-door paths from $A_1$ to $Y$. It opens $A_1\leftarrow A_0\to L_1\leftarrow U_1\to Y$ (Figure 20.8) and $A_1\leftarrow A_0\leftarrow W_0\to L_1\leftarrow U_1\to Y$ (Figure 20.9) (p. 274).
- Regardless of feedback, conditioning on past treatment is required when past treatment affects $Y$ (Figure 20.10: $A_0$ confounds $A_1$'s effect). Hence sequential exchangeability at $k$ generally requires conditioning on $\bar A_{k-1}$, not only on $L$ (p. 274).
- For a time-fixed treatment $A_1$ (the "short-term effect"), not adjusting for $A_0$ generally gives selection bias under feedback, and confounding if $A_0$ affects $Y$. $\mathrm{E}[Y|A_1=1,L_1]-\mathrm{E}[Y|A_1=0,L_1]$ can be non-zero when $A_1$ has no effect (pp. 274–275).
- Remedy: adjust for prior treatment or restrict to individuals with a given history. This is the idea of "new-user designs" (restrict to those who had not used treatment) (p. 275).
- Mismeasured past treatment: with only $A_0^*$ (an arrow $A_0\to A_0^*$), conditioning on $A_0^*$ cannot block the biasing paths through $A_0$. The investigators then find an $A_1$–$Y$ association after adjusting for $A_0^*$ and $L_1$ despite no effect (p. 275).
- So, contrary to a widespread belief, independent non-differential mismeasurement of treatment may cause bias under the null. Past treatment is a confounder for subsequent treatment even if it has no effect on $Y$. Under the alternative, imperfect adjustment may exaggerate the effect. Robins (1987) showed randomly mismeasured treatment may lead to bias away from the null (p. 275).

*Intuition note:* In a time-varying setting, past treatment generally has to be controlled for. If it is recorded with error, the control is incomplete, and leftover bias can look like an effect.

## Toy example (ours, not from the text)
Show the collider mechanism with the smallest numbers. Each of four types is 100 of 400 people:
- $A_0\in\{0,1\}$ is a fair coin, and $U\in\{0,1\}$ is an independent fair coin.
- $L_1=1$ if $A_0=1$ or $U=1$, else 0 (treatment raises $L_1$, as $U$ does).
- $Y=10\,U$. Treatment has no effect on $Y$. We ignore $A_1$.

| $A_0$ | $U$ | $L_1$ | $Y$ | N |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 100 |
| 0 | 1 | 1 | 10 | 100 |
| 1 | 0 | 1 | 0 | 100 |
| 1 | 1 | 1 | 10 | 100 |

- Unadjusted: $\mathrm{E}[Y|A_0=1]=(0+10)/2=5$ and $\mathrm{E}[Y|A_0=0]=(0+10)/2=5$. The difference is 0, which is correct.
- Stratify on $L_1=1$ (300 people): $\mathrm{E}[Y|A_0=1,L_1=1]=(100\cdot0+100\cdot10)/200=5$, and $\mathrm{E}[Y|A_0=0,L_1=1]=10$ (only the $U=1$ type). The difference is $5-10=-5$, although the true effect is 0.
- Among $L_1=1$, being untreated implies $U=1$. This is the "marker" effect of conditioning on the collider.

## Concepts
- [[treatment-confounder-feedback]] (new) — a time-varying confounder is affected by earlier treatment (or shares a cause with it) and affects later treatment (p. 267, p. 269)
- [[time-varying-confounder]] (new) — covariate $L_k$ that predicts later treatment and outcome; can exist without feedback (p. 267)
- [[sequential-exchangeability]] (new) — conditional exchangeability at each time given past treatment and covariates; generally needs $\bar A_{k-1}$ (p. 274)
- [[g-methods]] (new) — methods that adjust for time-varying confounders even with feedback; named here, not described (p. 269)
- [[g-null-theorem]] (new) — under sequential randomization, the independencies hold iff all $Y^g$ share one distribution, equal to that of observed $Y$ (p. 270)
- [[fork-chain-collider]] — $L_1$ is a collider on $A_0\to L_1\leftarrow U_1$; conditioning opens a path (p. 271)
- [[confounding-vs-selection-bias]] — stratification removes confounding for $A_1$ but creates selection bias for $A_0$ (p. 272)
- [[causal-dag]] — acyclic graphs can show feedback by unrolling in discrete time (p. 268)
- [[potential-outcomes]] — strategy effects defined as $\mathrm{E}[Y^{\bar a}]$ contrasts (p. 268)
- [[new-user-design]] (new) — restrict to people with no prior treatment to avoid past-treatment bias (p. 275)

## Canonical instances
- [[hiv-cd4-trial-table-20-1]] — hypothetical trial: true effect 0, estimates −13.3 (unadjusted) and −8 (stratified) (pp. 269–271)
- [[cum-treatment-regression]] — regression on $cum(\bar A)$ and $L_1$ gives non-zero $\theta_1$ under the null (pp. 273–274)
- [[mismeasured-past-treatment]] — questionnaire-based $A_0^*$ leaves bias under the null (p. 275)

## Bridges (candidates)
- [structural-analogy] Collider stratification here ↔ selection bias in sampling: restricting to a stratum chosen by an outcome of treatment creates spurious associations.
- [structural-analogy] Conditioning on $L_1$ in a regression ↔ Bayesian posterior conditioning: conditioning on a collider changes beliefs about its causes (e.g., $U_1$) in the same way.
- [metaphor] "More covariates is safer" ↔ model-building habits: adding a variable to the model can hurt when it is downstream of treatment.

## Questions this raises
- Which g-methods remove the bias, and what do they do differently from conditioning on $L_1$?
- How large can the net bias be, given it balances removed confounding against created selection bias?
- How can one defend identifiability when feedback and unmeasured $W_0$ cannot be distinguished by the data (Figures 20.3 vs 20.4)?
- How should past treatment be measured, or the analysis restricted, so that adjustment for it is valid?

## Reading notes
- Printed pages 267–276. The page offset is printed = pdf − 9. Printed page 276 is blank except for the running header.
- The source is the online revision dated 2026-08-19, not the 2020 version, so chapter numbers may differ from older citations.
- Misprint on p. 270: the text describes the 16,000 with $A_0=0$ as "treated at time 0". The table and the weighted-average margin note (rows 1–4) show they are untreated at time 0.
- Fine Point 20.2 says "Ā" for treatment history; I wrote $\bar A$. All figures were checked against the page images; the arrows described match them.
- Toy example, intuition notes and the bridges are my additions. The $-8$ in the $L_1=1$ stratum is stated by the text (p. 271) and not recomputed from the table here.
