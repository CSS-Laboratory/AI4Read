---
id: hernan-2020-whatif/ch22-target
work: hernan-2020-whatif
unit: "22 Target trial emulation"
pages: 305–322
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Target trial emulation

## L0 — One line
Causal questions about sustained treatment strategies are clarified by stating the protocol of a (hypothetical) target randomized trial; for per-protocol effects, the analysis, which generally needs g-methods, should then be the same whether the data come from a trial or from observational records.

## L1 — The gist (≤ 120 words)
How should we define and estimate effects of treatments that last over time? The chapter separates the intention-to-treat effect (effect of assignment) from the per-protocol effect (effect of following the strategy). It argues that the per-protocol effect is often the more natural target. Estimating it generally needs adjustment for time-varying confounding and selection bias, even inside a randomized trial. Observational analyses should emulate a target trial: fix eligibility, time zero, strategies, outcomes, contrast and analysis plan. Cloning, censoring and weighting handle unclear strategy assignment. The unifying message: trial and observational analyses differ less than usual practice suggests.

**Prerequisites:** counterfactual notation $Y^a$; exchangeability; confounding vs selection bias (backdoor paths, colliders); static vs dynamic strategies; IP weighting and g-methods (Chapters 19–21).

## L2 — Key ideas (5–10 bullets)
- Randomized assignment $Z$ can affect $Y$ through received treatment $A$ and also directly, so the intention-to-treat (ITT) effect is "the effect of assigning", not "the effect of treating" (p. 306).
- ITT is unconfounded, which largely explains why it is privileged in many trials (p. 307). Its usual justifications (null preservation, conservativeness, "effectiveness") hold only under conditions and can fail (pp. 307–309).
- The per-protocol effect compares strategies under full adherence. Because sensible protocols allow stopping for toxicity or contraindication, it generally compares dynamic strategies (pp. 310–311).
- Conventional "as-treated" and "per-protocol" analyses of trials are observational analyses. They need adjustment for confounding and selection bias (p. 308).
- A target trial protocol states eligibility, follow-up, strategies, outcomes, contrast and analysis plan. Its closest observational analog of ITT is a comparison of initiators, and the per-protocol analog is defined identically (pp. 313–314).
- Time zero should generally match the target trial. With multiple eligible times, one option is to emulate sequential trials. When data fit several strategies, clone individuals, censor clones when they deviate, and weight (pp. 315–317).
- Per-protocol analyses of randomized and observational data should be identical; both generally need g-methods (pp. 318–320).
- Fine Points 22.7–22.8 give an extreme constructed example and a generalization in which confounded observational data may, in extremely rare circumstances, point to a better policy than a trial alone (pp. 320–322).

## L3 — Walkthrough

### Introduction (p. 305)
Parts I and II used only simple target trials with time-fixed treatments. Now that tools for time-varying treatments exist, the target trial is generalized to sustained treatment strategies. The chapter also gives a taxonomy of effects, including observational analogs of ITT and per-protocol effects. Valid estimation generally needs data on time-varying prognostic factors and treatments, plus g-methods. The authors say g-methods make this more than a formal exercise (p. 305).

### 22.1 Intention-to-treat effect and per-protocol effect

**Setting (p. 305).** People at risk of a dangerous virus are randomized. $Z=1$ means immediate vaccination plus an experimental antiviral if infected. $Z=0$ means standard of care (no vaccine, no antiviral). Figure 22.1 has assigned treatment $Z$, received treatment $A$, outcome death $Y$, and unmeasured risk factors $U$ that influence the decision to get vaccinated. $Z$ and $A$ can differ (non-adherence). Arrows in Figure 22.1: $Z\to A$, $A\to Y$, $Z\to Y$, $U\to A$, $U\to Y$.

Two pathways link $Z$ to $Y$ (p. 305):
- $Z\to A\to Y$, through the treatment actually received.
- $Z\to Y$ directly, not through $A$. Example: people who know they got a promising treatment may become less careful.

**Fine Point 22.1: exclusion restriction (p. 306).** The arrow $Z\to Y$ means the exclusion restriction does not hold. Investigators try to remove that arrow (Figure 22.2) by hiding the assignment from participants and doctors (placebo, double-blind trial). Blinding is often unfeasible: no convincing placebo (e.g., open heart surgery), or side effects reveal who is treated. It is also not advised when one wants the effect in the real world, where there is no blinding (p. 306).

**Intention-to-treat effect (p. 306).** The effect of $Z$ depends on the strength of $A\to Y$, of $Z\to A$ (adherence) and of $Z\to Y$ (concurrent behaviour changes). It is the effect of assigning participants to treatment with $A$ (the intention of treating), hence the name intention-to-treat effect.
- Randomization implies exchangeability $Y^z \perp\!\!\!\perp Z$: no backdoor path from $Z$ to $Y$ in Figure 22.1.
- Association between $Z$ and $Y$ therefore implies a causal effect of $Z$ on $Y$, whether or not all adhered (p. 306).
- The associational risk ratio equals the causal ITT risk ratio:
$$\frac{\Pr[Y=1\mid Z=1]}{\Pr[Y=1\mid Z=0]}=\frac{\Pr[Y^{z=1}=1]}{\Pr[Y^{z=0}=1]}.$$
- An unadjusted comparison of $Z$ and $Y$ is an *intention-to-treat analysis* (p. 306).

**Fine Point 22.2: variations on ITT analysis (p. 307).** An ITT analysis is unbiased for the ITT effect because it includes all randomized individuals. Variants that use only a subset may be biased.
- *Pseudo-ITT analysis*: restricts to people with complete follow-up, $\Pr[Y=1\mid Z=1,C=0]/\Pr[Y=1\mid Z=0,C=0]$, where $C=0$ means uncensored until $Y$ is measured. Censoring may induce selection bias, in either direction. With loss to follow-up, a proper ITT analysis needs adjustment for selection bias (Section 21.5) (p. 307).
- *Modified ITT analysis*: for sustained strategies, restricts to people who at least initiated their assigned strategy (e.g., took one pill). It uses a subset and may be biased. It generally needs adjustment for risk factors that affect adherence (p. 307).

**Per-protocol effect (pp. 306–307).** This is the effect that would have been observed if everyone had adhered to the assigned treatment as the protocol specifies. The definition is the contrast
$$\Pr[Y^{z=1,a=1}=1]\ \text{vs.}\ \Pr[Y^{z=0,a=0}=1],$$
or, under the exclusion restriction,
$$\Pr[Y^{a=1}=1]\ \text{vs.}\ \Pr[Y^{a=0}=1].$$
The text uses the latter for simplicity (p. 306).
- Most of the book assumed perfect adherence, i.e., no $U$, so $Y^a\perp\!\!\!\perp A$ (p. 306).
- Suppose $U=1$ means high infection risk, and high-risk people in the $Z=0$ group seek vaccination outside the study. Then $A=1$ holds a higher share of high-risk people, so the groups are not exchangeable. The associational risk ratio $\Pr[Y=1\mid A=1]/\Pr[Y=1\mid A=0]$ does not equal the per-protocol risk ratio (p. 306).
- The backdoor path $A\leftarrow U\to Y$ means confounding. Estimating the per-protocol effect requires adjustment, i.e., treating the randomized experiment as an observational study (p. 307).

*Intuition note.* Randomization protects the effect of *assignment*, not the effect of what people then *do*. Once people choose whether to follow the assignment, the usual confounding problem returns.

**Fine Point 22.3: naïve per-protocol analyses (p. 308).**
- *As-treated analysis*: compares $A=1$ vs $A=0$ regardless of $Z$. It is confounded if reasons for taking treatment relate to unmeasured prognostic factors $U$ (Figures 22.1, 22.2). If measured $L$ blocks all backdoor paths (Figure 22.3: $Z\to A$, $L\to A$, $A\to Y$, $U\to L$, $U\to Y$), the analysis must adjust for $L$.
- *Conventional per-protocol (on-treatment) analysis*: keeps only the per-protocol population $A=Z$ and compares $Z=1$ vs $Z=0$ in it. It is an ITT analysis restricted to that population, and generally gives a biased estimate. In Figure 22.4, $S=1$ if $A=Z$ and $S=0$ otherwise, and $S$ is a common effect of $Z$ and $A$. Conditioning on $S=1$ opens the noncausal path $Z\to A\leftarrow L\leftarrow U\to Y$ unless $L$ is measured and adjusted for (p. 308).
- Both are observational analyses of a randomized experiment and need adjustment for confounding and selection bias (p. 308).

**Why ITT is privileged, and caveats (pp. 307–308).** The lack of confounding largely explains why ITT is privileged: it may not be the effect we want, but it is easier to compute, and the authors say we tend to invent arguments to justify an easier but less interesting quantity. They say several well-known justifications need to be taken with a grain of salt: two justifications and a further objection.

1. **Null preservation (common justification).** If $A$ has a null effect on $Y$, so does $Z$. More formally, under the sharp causal null and the exclusion restriction,
$$\frac{\Pr[Y=1\mid Z=1]}{\Pr[Y=1\mid Z=0]}=\frac{\Pr[Y^{a=1}=1]}{\Pr[Y^{a=0}=1]}=1 .$$
This fails when the exclusion restriction fails (Figure 22.1): $A$'s effect may be null while $Z$'s is not, because the arrow $Z\to Y$ remains (p. 307). The margin note says ITT then gives a valid, though perhaps underpowered, $\alpha$-level test of no average effect in double-blind placebo-controlled trials (p. 307).
2. **Conservativeness (common justification).** If imperfect adherence attenuates the effect, the ITT risk ratio lies between 1 and the per-protocol risk ratio, so ITT would be a lower bound. The authors answer that attenuation is not guaranteed (Fine Point 22.4) (p. 307–308).
3. **A further objection (not a justification).** Even when ITT is conservative, that may be bad. One could naïvely call $A$ safe because the ITT effect on an adverse outcome is near null, although $A$ harms many patients. Many assigned $Z=1$ may not have taken, or stopped taking, treatment before the outcome. The same objection applies to non-inferiority trials (p. 308).

**Summary (p. 308).** Exclusive reliance on ITT is hard to justify with substantial non-adherence, or when harms are studied. The per-protocol effect is often a more natural estimand for researchers and decision makers. It needs adjustment under conditional exchangeability given measured covariates, or under alternative assumptions such as those for instrumental variables (Chapter 16). With sustained strategies non-adherence grows, ITT becomes increasingly noninformative compared with the per-protocol effect, and estimating the per-protocol effect generally requires g-methods (p. 308).

**Fine Point 22.4: more misunderstandings (p. 309).**
- *The commonly heard argument that ITT measures real-world effectiveness and per-protocol measures efficacy.* The authors list problems:
  - ITT reflects adherence in that one experiment. Real-life adherence may differ, e.g., closer monitoring in studies, or more adherence once people learn a treatment works.
  - If effectiveness were the goal, double-blind placebo trials should be avoided, since real patients and doctors know the treatment.
  - People planning to adhere care more about the per-protocol effect.
- *The argument that ITT is guaranteed to be conservative.* The authors say this is not true in all settings:
  - If the per-protocol effect is not monotonic (not in the same direction for all individuals) and non-adherence is high, the per-protocol effect may be closer to the null than the ITT effect.
  - Even for monotonic effects, ITT is not necessarily conservative in head-to-head trials of two active treatments.
  - Example: expensive drug ($Z=1$) vs ibuprofen ($Z=0$), outcome severe pain at 1 year. Both are truly equally effective (per-protocol risk ratio 1). Adherence to ibuprofen happened to be lower, because of an easily palliated mild side effect. The ITT risk ratio was above 1, and investigators wrongly concluded ibuprofen was less effective (p. 309).

### 22.2 A target trial with sustained treatment strategies

**Pragmatic design (p. 309).** Since the goal is to emulate trials with real-world data, only pragmatic trials are considered: assignment not blinded, no placebo (both strategies $g$ and $g'$ are active treatments or no treatment), and monitoring as frequent as for regular patients.

**Example (p. 309–310).** Randomized trial of antiretroviral therapy and 5-year risk of death in HIV. Eligible: 18 years or older, no AIDS, no previous antiretroviral therapy. They are randomized at baseline $k=0$. Follow-up ends at death, loss to follow-up, or 60 months, whichever is first.
- $A_k=1$ if therapy is received at time $k$, for $k=0,\dots,K$, $K=59$.
- Strategy $g_1$: receive treatment ($A_k=1$) continuously during follow-up unless a contraindication or toxicity arises. Strategy $g_0$: stay untreated ($A_k=0$) throughout follow-up.
- $Z=1$ if assigned to $g_1$, $Z=0$ if assigned to $g_0$. $D_k$ is the death indicator and $C_k$ the censoring indicator, for $k=1,\dots,K+1$. The outcome is a failure time (margin note) (p. 310).

**ITT effect (p. 310).** The contrast of the static strategies $(z=1,\bar c_K=\bar 0)$ and $(z=0,\bar c_K=\bar 0)$: be assigned at baseline and remain under study to the end. At time $k$:
$$\Pr\!\left[D_k^{z=1,\bar c_k=\bar 0}=1\right]-\Pr\!\left[D_k^{z=0,\bar c_k=\bar 0}=1\right].$$
If assignment and initiation happen together (all $g_1$ start at time 0 whether or not they continue; no $g_0$ starts at time 0), the ITT effect is also the effect of initiation:
$$\Pr\!\left[D_k^{a_0=1,\bar c_k=\bar 0}=1\right]-\Pr\!\left[D_k^{a_0=0,\bar c_k=\bar 0}=1\right].$$
ITT is agnostic about deviations after baseline (stopping for no clinical reason, starting in $g_0$, non-approved co-treatments). Its size may depend heavily on the pattern of deviations in each trial: two studies with the same protocol in different settings can have different ITT estimates, and neither is biased. So ITT should be complemented by the per-protocol effect (p. 310).

**Per-protocol effect (pp. 310–311).** The contrast under the interventions of receiving $g_1$ continuously from baseline to end of follow-up versus receiving $g_0$ continuously:
$$\Pr\!\left[D_k^{g_1,\bar c_k=\bar 0}=1\right]-\Pr\!\left[D_k^{g_0,\bar c_k=\bar 0}=1\right].$$
- Sensible protocols do not mandate treatment no matter what. So the per-protocol effect generally compares *dynamic* strategies (do this, and if X happens do something else) rather than static ones (do this whatever happens) (p. 311).
- A protocol that only says "receive treatment continuously" may mislead. A person who stops because of toxicity is perfectly adhering to $g_1$ as it should have been stated. Stopping, or starting other medically indicated treatment, cannot be a protocol deviation if doing otherwise is not an option in the real world. Ideally the protocol fully specifies the strategies (p. 311).
- The per-protocol effect is often the implicit target. Complaints that interventions in the study did not follow the protocol, and are therefore "biased", indicate that investigators are really interested in the per-protocol effect, since post-baseline non-adherence cannot bias the effect of baseline assignment (pp. 311–312).

**Technical Point 22.1: controlled direct effects (p. 311).** For a mediator $M$ set to $m$, the additive-scale direct effects of $A$ on $Y$ not through $M$ are
$$E[Y^{a=1,m=1}]-E[Y^{a=0,m=1}]\quad\text{and}\quad E[Y^{a=1,m=0}]-E[Y^{a=0,m=0}].$$
- These are average controlled direct effects. They could be identified by an experiment with sequential randomization of $A$ (baseline) and $M$ (one month later), giving four groups, with $Y$ measured at 3 months. Then $E[Y^{a,m}]=\Pr[Y^{a,m}=1]$ is consistently estimated by $\Pr[Y=1\mid A=a,M=m]$.
- They are also identifiable in observational studies if consistency, positivity and exchangeability hold for both $A$ and $M$. This is a special case of contrasts of sustained strategies (Chapter 19): replace $A$ and $M$ by $A_0$ and $A_1$ (p. 311).

**Technical Point 22.2: other direct effects (p. 312).**
- *Pure (natural) direct effect*: $E[Y^{a=1,M^{a=0}}]-E[Y^{a=0,M^{a=0}}]$. It is a cross-world quantity, because $Y^{a=1,M^{a=0}}$ is indexed by both $a=1$ and $a=0$. It cannot be identified from randomized experiments on $A$, $M$ or both, nor from observational data under an FFRCISTG model. Pearl showed it can be identified for certain graphs under the NPSEM-IE model, which assumes untestable cross-world independencies. It matters because total effects decompose into pure direct and total indirect effects.
- *Principal stratum direct effect*: effect of $A$ in the subset with $M^{a=0}=M^{a=1}=m$:
$$E[Y^{a=1,m}\mid M^{a=0}=M^{a=1}=m]-E[Y^{a=0,m}\mid M^{a=0}=M^{a=1}=m],$$
which equals $E[Y^{a=1}\mid M^{a=0}=M^{a=1}=m]-E[Y^{a=0}\mid M^{a=0}=M^{a=1}=m]$. It involves no joint counterfactuals $Y^{a,m}$, so it is a total effect in a subset and does not need well-defined interventions on $M$. It has little policy relevance when $A$ affects $M$ in almost all individuals, because the stratum is then very small. Coarsening $M$ to enlarge the stratum may make the effect less scientifically relevant (p. 312).

**Other strategies from the same trial (pp. 312–313).** Suppose that during the trial a consensus emerges that $g_0$ is inferior. Physicians then recommend starting therapy when CD4 count $L_k$ first drops below 200 cells/µL. Many assigned $g_0$ follow $g_0'$: stay untreated ($A_k=0$) but switch to $A_k=1$ once $L_k<200$. The contrast $g_1$ vs $g_0'$ is neither the ITT effect nor the original per-protocol effect. It is the per-protocol effect in a hypothetical target trial randomizing to $g_1$ or $g_0'$ (p. 313).
- If the strategies of interest differ from those in the actual trial, full adherence is disadvantageous: nobody would follow the new protocol, so the data cannot emulate it. Non-compliance is what lets one trial's data emulate other trials (p. 313).
- Estimating per-protocol effects with sustained strategies raises the same issues as any observational comparison of strategies. It generally demands post-randomization data on adherence and on time-varying prognostic factors associated with adherence (p. 313).

*Intuition note.* ITT answers what happens if we assign a strategy, which depends on how messy adherence was in this trial. The per-protocol effect answers what happens if people follow a fully specified plan, including the sensible exceptions built into that plan.

### 22.3 Emulating a target trial with sustained strategies (pp. 313–315)
- If a randomized trial is not possible, we may emulate it with observational data. Specifying the protocol clarifies the causal question. At minimum: eligibility criteria, start and end of follow-up, treatment strategies, outcomes of interest, causal contrast, and data analysis plan. Specifying it may require exploring the data, e.g., only after finding that HIV diagnosis is recorded can one reasonably propose a trial in HIV (p. 313).
- **Emulating ITT.** It is rarely possible, because the actual assignment is unknown. The closest analog compares *initiation* of strategies (p. 313):
  - Contrast of initiating $A_0=1$ vs $A_0=0$ at baseline and remaining under study: $\Pr[D_k^{a_0=1,\bar c_k=\bar 0}=1]-\Pr[D_k^{a_0=0,\bar c_k=\bar 0}=1]$ (p. 314).
  - This defines groups by initiation, not assignment. In a trial it would pool everyone who took no dose at baseline, whatever their assignment. If initiation follows assignment shortly, the analog roughly preserves the ITT feature that the interventions occur shortly after baseline.
  - It is equivalent to the modified ITT analysis of Fine Point 22.2. With data on prescription rather than dispensing, a comparison by prescription would be somewhat more analogous (margin notes, p. 314).
- **Emulating per-protocol.** The analog is defined identically to the trial's. No original/alternative distinction is needed, because without a prespecified protocol each per-protocol effect corresponds to one target trial. In general, observational data can emulate only trials whose interventions are followed by at least some individuals. Modeling (e.g., dose-response structural models) may extrapolate beyond them (p. 314).
- **Benefits of explicitness.**
  - It makes obvious which analyses compare things that cannot be translated into hypothetical interventions. Those should be avoided when the goal is to help choose among actions (Sections 3.5, 3.6).
  - It adds clarity. The efficacy/effectiveness labels are ambiguous for sustained strategies over long periods. It is often difficult to argue that ITT with non-adherence, or a real-world per-protocol effect, measures the effect under perfect conditions (pp. 314–315).
  - The authors suggest accepting that all causal effects lie somewhere on an effectiveness continuum, and defining the strategies explicitly (p. 315).

### 22.4 Time zero (pp. 315–317)
Time zero (baseline) is the start of follow-up. Eligibility must be met at that point but not later, and outcomes are counted after it but not before (p. 315).
- **In trials**, time zero is when an eligible person is assigned a strategy. Starting follow-up before is not reasonable (strategies not yet assigned, eligibility not defined). Starting after (e.g., 2 years later) is potentially biased: early deaths and short-term effects are missed. If treatment has a short-term effect, more susceptible people will have died by year 2 in the treated arm. That differential proportion of susceptibles destroys baseline comparability and opens the door to selection bias (p. 315).
- **In observational analyses** the same rules apply, for the same reasons. Follow-up should start when it would have started in the target trial; otherwise estimates may be hard to interpret and biased because of selection affected by treatment. Errors are frequent, from two problems (p. 315). Example from the margin: part of the discrepancy between observational studies and a trial of postmenopausal hormone therapy was due to mishandled time zero.

**Problem 1: non-unique time zero (pp. 315–316).**
1. *Eligibility met at a single time.* Follow-up starts then. Example: immediate initiation when CD4 first drops below 500 cells/µL vs delayed initiation when it first drops below 350. Follow-up starts when CD4 first drops below 500 (pp. 315–316).
2. *Eligibility met at multiple times.* Example: initiation vs no initiation of hormone therapy in postmenopausal women with no chronic disease and no hormone use in the previous two years, eligible continuously from age 51 to 65. Options for time zero include (a) first eligible time, (b) a randomly chosen eligible time, (c) every eligible time, etc. Option (c) emulates multiple sequential target trials (p. 316):
   - With a fixed data collection schedule (e.g., every two years), emulate a new trial at each scheduled time.
   - With subject-specific schedules (e.g., electronic records), choose a fixed time unit (day, week, month) and emulate a trial at each unit.
   - Choosing the unit too coarsely can introduce bias. If treatment and confounders change more than once a week for many people, week or month introduces bias. Day could remove it, and if daily data are missing the bias could not be fully corrected (margin note).
   - Option (c) can be more statistically efficient because it uses more data. Individuals enter several trials, so the variance needs adjustment, e.g., by bootstrapping the entire analysis (p. 316).

**Problem 2: no unique strategy at time zero (pp. 316–317).** Target trial: people whose CD4 just dropped below 500 are assigned to (1) start therapy immediately, (2) start when CD4 drops below 350, or (3) start when it drops below 200. In observational data, those who started at time zero follow strategy (1). Those who did not are compatible with both (2) and (3). Options:
- Assign them at random to one strategy: statistically inefficient.
- *Clone* them: make two exact copies, one per strategy. Clones are *censored* when their data stop being consistent with their arm. For example, if the person does not start at CD4 350, the clone for strategy (2) is censored then.
- This censoring is likely informative and is corrected by adjusting for time-varying factors via IP weighting ("cloning + censoring + weighting"; Robins et al. 2008, Cain et al. 2010).
- If the person dies before either clone is censored, both clones die and the death is assigned to both strategies. This double allocation prevents the bias that would arise if events during the waiting period were systematically assigned to only one strategy.
- Variance needs bootstrapping. The procedure can be combined with sequential trial emulation (p. 317).

**Fine Point 22.5: grace periods (p. 317).** In the real world, therapy cannot be started exactly on the day it is assigned. Investigators define a grace period (say 3 months) during which initiation still counts as immediate. Otherwise the study estimates strategies that rarely occur or could not be implemented.
- During the grace period, observed data are consistent with more than one strategy. Handle this by cloning, censoring clones when they become incompatible, and IP weighting.
- When grace periods are used with cloning and censoring, almost everyone contributes a clone to each strategy, so the ITT effect cannot be estimated: a contrast by baseline assignment compares groups with essentially identical outcomes. Such analyses are geared towards some form of per-protocol effect and thus will generally need adequate adjustment.
- A well-defined initiation strategy with a grace period should also specify the timing of initiation within it (Cain et al. 2010) (p. 317).

*Intuition note.* Time zero is the moment when the "trial" starts for each person. Cloning is a bookkeeping device: when the data do not yet reveal which strategy a person follows, they are kept in all compatible strategies until they visibly deviate.

### 22.5 A unified approach to answer What If questions with data (pp. 317–320)
**Why target trials unify (pp. 317–318).**
- Target trial emulation recapitulates the counterfactual and causal-diagram frameworks and grounds them in an actionable question, organized around the familiar concept of an experiment.
- It applies across disciplines. Economists call confounding and conditional exchangeability "omitted variable bias" and "selection on observables". Traditional social scientists are unlikely to use g-methods because their questions are typically not about time-varying treatments. The authors call these disciplinary differences superficial compared with the task all health and social scientists interested in causal inference face: articulating questions as contrasts of well-defined counterfactuals.
- Aside from baseline randomization, there are no other *necessary* differences between analyses of observational data that emulate a target trial and analyses of true trials (Fine Point 22.6). A trial is a follow-up study with baseline randomization; observational longitudinal data are a follow-up study without it (p. 318).
- Trials of sustained strategies in real-world settings, with possible deviations (imperfect adherence, loss to follow-up), are subject to confounding and selection biases that we have learned to associate exclusively with observational studies. For per-protocol effects, both designs may need adjustment for time-varying prognostic factors that predict drop-out (selection bias) and treatment (confounding). Per-protocol estimates from trials may be biased too (p. 318).

**Fine Point 22.6: how the data differ (p. 319).** Only three things distinguish trial data from observational data: (i) no baseline confounding is expected, (ii) randomization probabilities are known, (iii) assignment to a strategy is known at baseline.
- An observational analysis can emulate (i) with a sufficient set of covariates measured and adjusted for, and (ii) if the treatment-assignment model given the past is correctly specified.
- (iii) is not necessary for a per-protocol effect, in trials or observational data, because efficient estimators (functions of the sufficient statistic) do not use it. In a trial, one could delete the assignment variable and still estimate a per-protocol effect if enough confounders were measured. In a trial of dynamic strategies with perfect adherence, a sufficient set is all time-fixed and time-varying covariates the strategies use to assign treatment (Robins 1986).

**Typical analyses of trials (pp. 318–320).**
- *Typical ITT analysis*: compares randomized groups with no adjustment. No adjustment for baseline confounding is needed because of randomization. No adjustment for post-randomization confounding is needed because there cannot be such confounding for the effect of baseline assignment (p. 319).
- But randomization does not ensure exchangeability between those who are and are not lost to follow-up. An ITT estimate among those not lost may suffer post-randomization selection bias if prognostic factors influence, or are associated with, differential loss. Valid ITT estimation may then require adjustment for time-varying prognostic factors with g-methods, e.g., if symptoms influence dropping out (p. 319).
- *Typical per-protocol analysis* for sustained strategies censors people at the first deviation and does no adjustment. Three reasons it is questionable (pp. 319–320):
  1. Selection bias due to differential loss to follow-up may need g-methods.
  2. It partly disregards the randomized groups, so those who stay on protocol under different strategies may not be exchangeable. It is akin to an observational analysis and needs g-methods for time-varying risk factors that affect staying on protocol. Instrumental variable estimation (Chapter 16) can sometimes work without explicit adjustment, but needs a valid instrument and strong modeling assumptions.
  3. It ignores that the strategies are dynamic. Censoring those who discontinue treatment as if that were by definition a deviation (why it is called on-treatment analysis) is a mistake: stopping for toxicity or contraindication is not a deviation.
- For failure-time outcomes, g-methods are always needed when treatment affects the outcome, since $A_k$ affects all later variables through $D_{k+1}$ (margin note, p. 320).

**Conclusions (p. 320).** For per-protocol effects (or their observational analog), the analyses of trials and observational studies should be identical. If we adjust for time-varying confounding and selection bias in observational studies, we should do so for post-randomization confounding and selection bias in trials. Trials are not always available (expensive, infeasible, unethical, untimely), so many decisions rest on observational evidence. Observational analyses meant to assist decisions should explicitly emulate a trial and be judged by how well they emulate it (p. 320).

*Intuition note.* Once treatment strategies last long enough for people to deviate or drop out, a trial's per-protocol analysis faces the same confounding and selection problems as observational data. Then the same methods apply to both.

**Fine Point 22.7: a counterintuitive comparison (p. 321).**
- Setup: an untested over-the-counter treatment $A$ is used by many people with lung cancer. A double-blind placebo-controlled trial runs in a random 20% of newly diagnosed patients. All adhered. 60-month mortality was 55% (treated) and 45% (placebo):

| | $A=0$ | $A=1$ |
|---|---|---|
| $Y=1$ | 450 | 550 |
| $Y=0$ | 550 | 450 |
| total | 1000 | 1000 |

- The regulator banned the treatment. Later, an observational study of the other 80% (8000 patients) found 0% mortality in both treated and untreated.
- Counterfactual types: "doomed" ($Y^{a=0}=Y^{a=1}=1$), "hurt" ($Y^{a=0}=0,Y^{a=1}=1$), "helped" ($Y^{a=0}=1,Y^{a=1}=0$), "immune" ($Y^{a=0}=Y^{a=1}=0$). By random sampling and randomization, the 1000 treated, the 1000 untreated, and the 8000 observational individuals have the same type distribution.
- 0% observed mortality implies: (i) no "doomed"; (ii) everyone with $Y^{a=1}=1$ is "hurt" and had $A=0$; (iii) everyone with $Y^{a=0}=1$ is "helped" and had $A=1$.
- Reconstruction: the 550 treated who died are "hurt"; by randomization there are 550 "hurt" with $A=0$ who survived. Likewise 450 "helped" in each arm:

| "Hurt" | $A=0$ | $A=1$ | "Helped" | $A=0$ | $A=1$ |
|---|---|---|---|---|---|
| $Y=1$ | 0 | 550 | $Y=1$ | 450 | 0 |
| $Y=0$ | 550 | 0 | $Y=0$ | 0 | 450 |
| total | 550 | 550 | total | 450 | 450 |

  Combined, the tables recover the trial data, so there are no "immune" individuals.
- The authors conclude the regulator should relicense $A$ and continue current practice, because, as they put it, the observational study demonstrated that somehow every individual had private knowledge of whether the treatment was personally harmful or beneficial.
- An extreme scenario to explain this: suppose there is a 55/45 ethnic split and, for genetic reasons, $A$ is harmful to all in group 1 and beneficial to all in group 2. Suppose group 1 avoided $A$ after seeing members die, and group 2 took it after seeing members survive. That means maximal qualitative effect modification and maximal confounding by ethnic group.
- Point: the trial compared "treat everybody" and "treat nobody", but the optimal strategy is to treat only group 2. Without data on the effect modifier, a trial cannot assign people to it. In the observational study everyone followed the optimal strategy and no one died. The authors say the confounded observational study, not the unconfounded trial, revealed the correct policy. They call the setting unrealistic but useful (p. 321).

**Fine Point 22.8: generalization (p. 322).** A design combining trial and observational data may be more informative than the trial alone, provided both are random samples of all individuals eligible for the trial.
- Suppose a trial of binary $A$ is run where $A$ is already in use (lower $Y$ preferable), and occasionally the observational mean $E[Y]$ is less than the mean in both trial arms, i.e., less than $E[Y^{a=0}]$ and $E[Y^{a=1}]$. Then we might leave current practice unchanged.
- $E[Y]=E[Y^g]$ for a strategy $g$ different from "treat all" and "treat nobody". Let $U$ be a sufficient set of unmeasured, possibly unknown, pre-treatment covariates with $Y^a\perp\!\!\!\perp A\mid U$, and $\Pr[A=1\mid U]$ the propensity score. The equality holds for the random strategy $g$ that assigns $A=1$ with probability $\Pr[A=1\mid U]$, since this is the strategy that generated the observational data.
- $g$ cannot be implemented without data on $U$. But this could motivate measuring pre-treatment covariates $V$ and using the trial data to find a deterministic dynamic strategy $g^*(x)$ with $E[Y^{g^*}]$, estimated from the unconfounded trial, below the observational $E[Y]$ (p. 322).

## Toy example (ours, not from the text)
**Question:** how can the ITT risk ratio differ from 1 when the per-protocol risk ratio is 1? This mirrors the ibuprofen example in Fine Point 22.4, with numbers we chose.

Assumptions: 1000 people per arm. The exclusion restriction holds and adherence is unrelated to prognosis, so no confounding. Anyone who does not take their assigned drug takes nothing.
- Severe-pain risk if a drug is taken: 0.20 for both drugs, so the per-protocol risk ratio is $0.20/0.20=1$.
- Risk if nothing is taken: 0.50.
- Adherence: 90% for the expensive drug ($Z=1$), 50% for ibuprofen ($Z=0$).

ITT risks:
- $Z=1$: $0.9\times0.20+0.1\times0.50=0.18+0.05=0.23$, i.e., 230 of 1000.
- $Z=0$: $0.5\times0.20+0.5\times0.50=0.10+0.25=0.35$, i.e., 350 of 1000.

ITT risk ratio (ibuprofen vs expensive) $=0.35/0.23\approx1.52$. The ITT effect is not "conservative": it suggests ibuprofen is worse although the drugs are equally effective when taken. The ITT result reflects the adherence differences of this particular trial.

## Concepts
- [[intention-to-treat-effect]] (new) — effect of being assigned to a strategy at baseline, whatever happens afterwards; unconfounded under randomization (p. 306, p. 310)
- [[per-protocol-effect]] (new) — effect if everyone followed the (fully specified, often dynamic) strategies throughout follow-up; needs adjustment (pp. 306, 310–311)
- [[exclusion-restriction]] (new) — assumption of no direct arrow $Z\to Y$, i.e., assignment affects the outcome only through received treatment (p. 306)
- [[target-trial-emulation]] — design an observational analysis by specifying the protocol of the randomized trial it mimics: eligibility, follow-up, strategies, outcomes, contrast, analysis plan (p. 313)
- [[sustained-treatment-strategy]] (new) — treatment rule followed over follow-up, often dynamic (depends on evolving covariates), not a one-time assignment (pp. 309–311)
- [[time-zero]] (new) — start of follow-up: eligibility met there, outcomes counted after; should match the target trial (p. 315)
- [[cloning-censoring-weighting]] (new) — copy people into every compatible strategy, censor copies on deviation, correct by IP weighting, bootstrap variance (p. 316–317)
- [[grace-period]] (new) — time after time zero during which initiation still counts as "immediate" (p. 317)
- [[confounding-vs-selection-bias]] — here: confounding from $U$ affecting adherence and outcome; selection bias from loss to follow-up or from conditioning on $S$ (pp. 307–308)
- [[fork-chain-collider]] — conditioning on $S$, a common effect of $Z$ and $A$, opens $Z\to A\leftarrow L\leftarrow U\to Y$ (p. 308)
- [[assignment-mechanism-ignorability]] — here, conditional exchangeability given measured covariates, needed for per-protocol effects (p. 308)
- [[potential-outcomes]] — counterfactual contrasts $D_k^{z,\bar c}$, $D_k^{g,\bar c}$ define each effect (pp. 310–311)
- [[controlled-direct-effect]] (new) — effect of $A$ when mediator $M$ is set to a value; a special case of sustained strategies (p. 311)
- [[propensity-score]] — $\Pr[A=1\mid U]$ used to define the random strategy $g$ in Fine Point 22.8 (p. 322)

## Canonical instances
- [[hiv-antiretroviral-target-trial]] — 5-year death risk, strategies $g_1$ vs $g_0$, CD4 thresholds 500/350/200 (pp. 309–316)
- [[ibuprofen-vs-expensive-drug]] — ITT risk ratio $>1$ although per-protocol risk ratio is 1 (p. 309)
- [[vaccine-plus-antiviral-trial]] — non-adherence, $U$ and the exclusion restriction (pp. 305–306)
- [[hormone-therapy-time-zero]] — multiple eligible times; time-zero mishandling in part explains an observational–trial discrepancy (p. 315–316)
- [[lung-cancer-trial-vs-observational]] — Fine Point 22.7: hurt/helped types, ethnic-group scenario (p. 321)

## Bridges (candidates)
- [same-math] conditioning on $S=1$ (being per-protocol) opens $Z\to A\leftarrow L\leftarrow U\to Y$ ↔ causal DAGs: collider conditioning opens a spurious path — the same graph rule.
- [structural-analogy] cloning + censoring + IP weighting ↔ survey sampling / missing data: reweighting retained cases to represent those lost to informative selection.
- [structural-analogy] trial of messy adherence emulating other protocols ↔ causal inference with positivity: a strategy can be emulated only if some people follow it (p. 314).
- [structural-analogy] Fine Point 22.8, combining trial data (unconfounded) with observational data (large, confounded) ↔ Bayesian evidence synthesis: two data sources with different biases combined for one decision.
- [metaphor] clones assigned to each compatible strategy ↔ keeping several hypotheses alive until data rule them out.

## Questions this raises
- With cloning and censoring, how does one build the censoring-weight model, and what happens if positivity fails for a strategy?
- When the protocol is not explicit, who decides which deviations (e.g., stopping for toxicity) count as adherence, and how sensitive are results to that choice?
- How large must the gap between $E[Y]$ in observational data and in both trial arms be before a combined design is trustworthy (Fine Point 22.8)?
- How can one check, in practice, how well an observational study emulated its target trial?

## Reading notes
- Printed page = pdf page − 9 (pdf 314 = printed 305). Printed numbers appear on the page images and in the page labels.
- The source note says this PDF is an online revision dated 2026-08-19, not the 2020 version. Chapter numbering may differ from older citations (e.g., chapters 22–23). Chapter 23 is mentioned on p. 312 as covering an interventionist theory of mediation.
- The unit has no exercises, so there is no Exercises section.
- Text-layer issues: garbled counterfactual superscripts on pp. 310, 312 and 314, checked against the images. A stray fragment "cells/µL" appears in Fine Point 22.5 (p. 317).
- Possible misprints in the source: Technical Point 22.2 writes the last term of the principal-stratum identity as $E[Y^{a=0}=1\mid\dots]$ (with a stray "$=1$"); Fine Point 22.7 has "observayion". In Section 22.1, a sentence in the per-protocol discussion begins with a lowercase "that is" after a full stop (p. 306). I corrected none of these in the maths above except to write the principal-stratum identity without "$=1$".
- This is causal-inference material filed under the field "bayesian" only because of the metadata provided. These pages contain no Bayesian methods.
- The ITT justifications labelled "common justification" (null preservation, conservativeness) and the argument in Fine Point 22.4 that ITT measures effectiveness are views the authors then criticise, not their own claims.
