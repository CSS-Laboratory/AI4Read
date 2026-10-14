---
id: hernan-2020-whatif/ch03-observational
work: hernan-2020-whatif
unit: "3 Observational studies"
pages: 27-46
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
# Observational studies (Hernán & Robins, ch. 3)

## L0 — One line
An observational study can be treated as a conditionally randomized experiment, so that causal effects can be identified, if three conditions hold (exchangeability, positivity and consistency), conditions the authors call "often heroic" and of which exchangeability can never be tested.

## L1 — The gist (≤ 120 words)
Without randomization, can we still estimate causal effects from observed data? The chapter says yes, if we can treat the data as a conditionally randomized experiment. That requires three identifiability conditions (assumptions that let the observed data pin down one causal effect): conditional exchangeability given measured covariates L, positivity, and consistency. Exchangeability can never be verified from the data. Positivity can sometimes be checked. Consistency requires well-defined interventions and a link from them to the recorded variables. The chapter ends by proposing to specify a hypothetical "target trial" and emulate it. This makes the causal question precise and shows when a question about a non-intervention variable (such as blood pressure) is ill-defined.

**Prerequisites:** counterfactual (potential) outcomes $Y^a$; marginal vs. conditional independence; standardization and IP weighting from Chapter 2 (the previous chapter).

## L2 — Key ideas
- Causal inference from observational data needs two things: data and identifiability conditions. In ideal randomized experiments the conditions hold by design (p. 28).
- The three conditions are consistency, conditional exchangeability $Y^a \perp\!\!\!\perp A \mid L$, and positivity. If they hold, standardization or IP weighting identify the effect (p. 28).
- Conditional exchangeability is an assumption external to the data and cannot be tested. Unmeasured predictors $U$ of the outcome that influence treatment within strata of $L$ can break it (pp. 29–31).
- Positivity ($\Pr[A=a\mid L=l]>0$ for the relevant $l$) is needed for standardized and IP-weighted means to be meaningful. Unlike exchangeability, it can sometimes be checked empirically (pp. 32–34).
- Consistency ($Y=Y^A$) has two parts: well-defined counterfactuals, which need well-defined interventions, and a link between those interventions and the recorded variable (pp. 33–39).
- For non-intervention variables, in the book's framework, a causal effect is well defined only if one believes in "effective no-direct-effect" (ENDE) interventions. Whether to accept this belief is a matter of expert judgement (pp. 38, 42).
- A target trial specifies the hypothetical experiment to be emulated. This makes the causal contrast precise and reveals extreme or impossible interventions (pp. 41–44).

## L3 — Walkthrough

### Introduction (p. 27)
- Question: does one pedestrian's looking up make other pedestrians look up? A randomized experiment is too burdensome, so an *observational study* is proposed. The investigator only observes and records (p. 27).
- Critics could say both pedestrians looked up because of a common event (a thunderous noise, rain drops). Such criticisms do not apply to randomized experiments, which is one reason they are central to causal theory (p. 27).
- Much human knowledge still comes from observational studies (evolution, tectonic plates, global warming). The chapter reviews conditions under which they give valid causal inferences (p. 27).

### 3.1 Identifiability conditions (pp. 27–29)
- Ideal randomized experiments identify average causal effects because randomization gives exchangeability. Example: an associational risk ratio of 0.7 from a marginally randomized heart transplant trial is expected to equal the causal risk ratio (p. 27). This chapter considers only experiments with full follow-up and full adherence (p. 27, margin note).
- In an observational study where transplant recipients were more likely to have a severe heart condition, an associational risk ratio of 1.1 would be a compromise. The beneficial effect pushes it under 1. The higher underlying mortality of recipients pushes it over 1 (pp. 27–28).
- Therefore the best explanation for an observational association is not necessarily a causal effect (p. 28).
- Common strategy: analyze the data *as if* treatment were randomly assigned conditional on measured covariates $L$, though this is at best an approximation (p. 28).
- Informally, an observational study can be conceptualized as a conditionally randomized experiment if (p. 28):
  1. the observed outcome equals the counterfactual outcome under the observed treatment (**consistency**);
  2. the counterfactual outcomes are independent of the observed treatment conditional only on known measured covariates $L$ (**exchangeability**);
  3. the probability of receiving every value of treatment conditional on $L$ is greater than zero (**positivity**).
- The authors call these conditions "often heroic", which explains the suspicion toward observational causal inference (p. 28).
- If the analogy is correct, the methods of the previous chapter (IP weighting, standardization) identify causal effects. The conditions are therefore called *identifiability conditions*. For example, the data of Table 3.1 gave a causal risk ratio of 1 in the conditionally randomized experiment. If the same data came from an observational study and the three conditions held, the causal risk ratio would also be 1 (p. 28).
- In ideal randomized experiments the conditions hold by design. For an observational study we must assume them, and the assumptions may be false. Causal inference needs data plus identifiability conditions (p. 28).
- Terminology (margin): Rosenbaum and Rubin called exchangeability plus positivity *weak ignorability*. Full exchangeability plus positivity is *strong ignorability* (p. 28).
- If a condition fails, other approaches exist. One uses an *instrumental variable*, a predictor of treatment that is hoped to behave as if randomly assigned given measured covariates (Chapter 16) (p. 28).

**Fine Point 3.1 — Identifiability (p. 29).**
- An average causal effect is (nonparametrically) *identifiable* under a set of assumptions if they imply that the distribution of the observed data is compatible with a single value of the effect measure. It is *nonidentifiable* if the data are compatible with several values (p. 29).
- Table 3.1 from a conditionally randomized experiment: effect identifiable, risk ratio 1, no further assumptions. The same data from an observational study give risk ratio 1 only if we add conditional exchangeability $Y^a\perp\!\!\!\perp A\mid L$, an *identifying assumption* external to the data (p. 29).
- Without that assumption the data are consistent with (p. 29):
  - a risk ratio below 1, if risk factors other than $L$ are more frequent among the treated;
  - a risk ratio above 1, if they are more frequent among the untreated;
  - a risk ratio of 1, if all risk factors except $L$ are equally distributed (equivalently, $Y^a\perp\!\!\!\perp A\mid L$).

Observational methods based on the conditional-randomization analogy are traditionally privileged in fields where it is often reasonable (e.g., epidemiology). Instrumental variable methods are traditionally privileged where it is not (e.g., economics) (p. 29).

*Intuition note.* Identifiability asks whether the data alone pin down one answer. In observational data they do not, until you add an assumption about who got treated and why. Randomization supplies that assumption for free.

### 3.2 Exchangeability (pp. 29–31)
- In marginally randomized experiments the treated and untreated are exchangeable because randomization equally distributes the independent predictors of the outcome (an *independent predictor* is a covariate associated with $Y$ within levels of treatment) (p. 29).
- In Table 3.1, 69% of the treated versus 43% of the untreated were in critical condition $L=1$, so marginal exchangeability fails (pp. 29–30).
- In a conditionally randomized experiment, imbalance in $L$ is expected by design. The treated and untreated are not exchangeable but are conditionally exchangeable within levels of $L$. Equivalently, within levels of $L$ all other outcome predictors are equally distributed (p. 30).
- In an observational study, reasons for treatment are likely associated with outcome predictors (later called *confounders*, Chapter 7). If doctors direct scarce hearts to those in critical condition, and $L$ is the only unequally distributed outcome predictor, the study in Table 3.1 can be described in two logically equivalent ways. Either it is (i) an observational study with $\Pr[A=1\mid L=1]=0.75$ and $\Pr[A=1\mid L=0]=0.50$, or (ii) a (nonblinded) conditionally randomized experiment with those assignment probabilities. Under either, $Y^a\perp\!\!\!\perp A\mid L$ holds and standardization or IP weighting can identify the effect (p. 30).
- Whether $L$ is the only unequally distributed predictor "must remain unanswered", so investigators must work under the assumption (p. 30).
- Not every variable unequally distributed between treatment groups needs to be in $L$. Example: HLA gene compatibility guides allocation. HLA genes are not predictors of mortality conditional on $L$ and $A$, so assignment is essentially random within levels of $L$ and HLA need not be considered (p. 30).
- Failure example: unknown to investigators, doctors prefer nonsmokers. Within $L=1$, smokers ($U=1$) have a lower probability of $A=1$. Smoking is an important outcome predictor, so conditional exchangeability given $L$ fails. Collecting smoking data would not rule out other unmeasured imbalanced predictors (pp. 30–31).
- Specifically, conditional exchangeability will not hold if there exist unmeasured independent outcome predictors $U$ such that the probability of treatment depends on $U$ within strata of $L$. Unmeasured variables $U$ cannot be used for standardization or IP weighting (p. 31).
- Even if it holds, investigators cannot empirically verify it. One would need $\Pr[Y^a=1\mid A=a,L=l]=\Pr[Y^a=1\mid A\neq a,L=l]$, but for those with $A\neq a$ the value of $Y^a$ is unknown (margin note, p. 31).
- Investigators can raise plausibility by measuring many relevant $L$ (e.g., determinants of treatment that also predict the outcome). But however many variables are included, the assumption cannot be tested. Validity depends on the investigators' expert knowledge being correct (p. 31).

**Fine Point 3.2 — Crossover randomized experiments (p. 31).**
- Without randomization, individual effects are identified in a crossover experiment under three strong conditions (from Fine Point 2.1), for $t=0,1$: (i) no carryover, $Y_{it=1}^{a_0,a_1}=Y_{it=1}^{a_1}$; (ii) the individual effect does not depend on time, $Y_{it}^{a_t=1}-Y_{it}^{a_t=0}=\alpha_i$; (iii) the no-treatment outcome does not depend on time, $Y_{it}^{a_t=0}=\beta_i$ (p. 31).
- Now randomize the order: each individual gets $(A_{i1}=1,A_{i0}=0)$ or $(A_{i1}=0,A_{i0}=1)$ with probability 0.5. This matters when (iii) is not assumed. Let $Y_{i1}^{a_1=0}-Y_{i0}^{a_0=0}=r_i$. Under (i), (ii) and consistency (p. 31):
  - if $A_{i0}=0, A_{i1}=1$: $Y_{i1}-Y_{i0}=\alpha_i+r_i$;
  - if $A_{i1}=0, A_{i0}=1$: $Y_{i0}-Y_{i1}=\alpha_i-r_i$.
- Individual effects are no longer identified since $r_i$ is unknown. But $A_{i1},A_{i0}$ are randomized and so independent of $r_i$. The mean of $(Y_{i1}-Y_{i0})A_{i1}+(Y_{i0}-Y_{i1})A_{i0}$ estimates $\mathrm E[\alpha_i]$ (p. 31).
- Under (i) only, this mean estimates $(\mathrm E[\alpha_{i1}]+\mathrm E[\alpha_{i0}])/2$, with $\alpha_{it}=Y_{it}^{a_t=1}-Y_{it}^{a_t=0}$ (p. 31).
- The authors call no carryover "implausible" for the treatments and outcomes studied in the book (p. 31).

*Intuition note.* Conditional exchangeability says: among people with the same $L$, who got treated is "as good as random" with respect to the outcomes they would have had. Since half of each comparison (the counterfactual) is never seen, no dataset can prove it. It rests on subject-matter knowledge.

### 3.3 Positivity (pp. 32–34)
- Idea: a study must have some individuals at each treatment level to compute an average effect. In randomized experiments $\Pr[A=1]$ and $\Pr[A=0]$ are positive by design. In conditionally randomized experiments $\Pr[A=a\mid L=l]>0$ holds by design for all $l$ (p. 32). The condition is sometimes called the *experimental treatment assumption* (margin note, p. 32).
- Example: in Table 3.1, $\Pr[A=1\mid L=1]=0.75$ and $\Pr[A=1\mid L=0]=0.50$, so neither probability is 0 or 1 and positivity holds (p. 32).
- Definition: positivity holds if $\Pr[A=a\mid L=l]>0$ for all $a$ involved in the causal contrast and for all values $l$ with $\Pr[L=l]\neq 0$ in the population of interest. It is needed only for the $l$ present in that population (p. 32).
- It is required only for variables $L$ needed for exchangeability. "Having blue eyes" was not used to assign treatment and is not an independent outcome predictor given $L$ and $A$. So positivity is not needed for it (p. 32).
- In observational studies neither exchangeability nor positivity is guaranteed. Positivity fails if doctors always transplant to those with $L=1$, i.e., $\Pr[A=0\mid L=1]=0$ (Figure 3.1) (p. 32).
- A difference from exchangeability: positivity can sometimes be empirically verified (Chapter 12). In Table 3.1 treated and untreated both occur at each level of $L$, so positivity holds for $L$ (p. 32).
- The previous chapter's standardized and IP weighted risks are only meaningful when positivity holds. In Figure 3.1 with no untreated at $L=1$, the data contain no untreated individuals with $L=1$ who could be exchangeable with the treated, so nothing says what would have happened had they been untreated (p. 33).
- Figure 3.1 numbers (p. 33): $\Pr[L=0]=0.4$, $\Pr[L=1]=0.6$. Within $L=0$: $A=0$ (0.5, count 4) and $A=1$ (0.5, count 4), each with $\Pr[Y=1]=0.25$. Within $L=1$: $A=0$ (probability 0, count 0) and $A=1$ (probability 1, count 12), with $\Pr[Y=1]=2/3$ among the treated.

**Technical Point 3.1 — Positivity for standardization and IP weighting (p. 34).**
- The standardized mean is
$$\sum_l \mathrm E[Y\mid A=a,L=l]\Pr[L=l]\quad\text{if }\Pr[A=a\mid L=l]>0\text{ for all }l\text{ with }\Pr[L=l]\neq0,$$
and is undefined otherwise. The condition is effectively equivalent to $f[a\mid L]>0$ with probability 1 (p. 34).
- The IP weighted mean $\mathrm E\!\left[\frac{I(A=a)Y}{f[a\mid L]}\right]$ is undefined when positivity fails, because a $0/0$ ratio occurs (p. 34).
- The version $\mathrm E\!\left[\frac{I(A=a)Y}{f[A\mid L]}\right]$ is always defined, because $f[A\mid L]$ is never zero. But when positivity fails it is a biased estimate of the counterfactual mean even under exchangeability (p. 34). With $Q(a)=\{l:\Pr(A=a\mid L=l)>0\}$:
$$\mathrm E\!\left[\frac{I(A=a)Y}{f[A\mid L]}\right]=\Pr[L\in Q(a)]\sum_l \mathrm E[Y\mid A=a,L=l,L\in Q(a)]\Pr[L=l\mid L\in Q(a)],$$
which under exchangeability equals $\mathrm E[Y^a\mid L\in Q(a)]\Pr[L\in Q(a)]$ (p. 34).
- With binary $A$ and no positivity, $Q(0)\neq Q(1)$. Then the contrast of the two IP-weighted means has no causal interpretation even under exchangeability, because it compares two different groups. Under positivity $Q(1)=Q(0)$ and the contrast is the average causal effect if exchangeability holds (p. 34).

*Intuition note.* If nobody in some stratum received a treatment level, no data say what that level would do there. The standardized mean is then undefined. The IP-weighted version that is still computable estimates something only about the strata where that level occurs, and a contrast of two such means compares different groups.

### 3.4 Consistency: first, define the counterfactual outcome (pp. 33–39)
- *Consistency*: the observed outcome $Y$ of every treated individual equals her $Y^{a=1}$, and of every untreated individual her $Y^{a=0}$. Formally $Y=Y^A$, i.e., $Y^a$ evaluated at the actual treatment (p. 33).
- It links counterfactuals to observed data. The book takes counterfactuals $Y^a$ as primitives and derives $Y$ from them. For binary $A$, $Y^A=AY^{a=1}+(1-A)Y^{a=0}$ (p. 33).
- It may seem obvious (aspirin, death) but cannot always be taken for granted. It has two components: (1) a precise definition of $Y^a$ via the superscript $a$; (2) linking counterfactual to observed outcomes. Section 3.4 treats (1) (p. 33).
- Well-defined counterfactuals are needed for the effect $Y^{a=1}-Y^{a=0}$. The average effect $\mathrm E[Y^{a=1}-Y^{a=0}]=\Pr[Y^{a=1}=1]-\Pr[Y^{a=0}=1]$ is well defined only if the individual effect is well defined for every individual in the population (p. 34). A natural sufficient condition: if $a$ corresponds to a well-defined intervention, then $Y^a$ is well defined as the outcome had that intervention been performed (p. 34). (Margin: Robins and Greenland argued that well-defined counterfactuals, or equivalent concepts, are necessary for meaningful causal inference.)
- **Two ideal randomized experiments** on the same population, heart transplant ($a=1$) vs. medical therapy ($a=0$), full adherence (pp. 34–35):
  - Experiment 1: the protocol details pre-operative procedures, anesthesia, surgical technique, post-operative care and immunosuppression. "Heart transplant" is the sequential implementation of components $(a_0,a_1,a_2,a_3)$, with $a_0=1$ meaning assignment to transplant (p. 35).
  - Experiment 2 (a *pragmatic trial*): only assignment ($a_0=1$) is specified. The remaining components take whatever values occur in the healthcare system, $a_j=A_j$ for $j=1,2,3$ (p. 35).
  - Both versions of $a=1$ are well defined in their protocols. So $Y^{a=1}$ is well defined in each. But the counterfactuals, and hence the causal effects, will likely differ between the experiments, so consumers must decide which they prefer (p. 35).
- The effect from experiment 1 may vary less across populations (precise components). So it may be less difficult to transport. This concerns transportability (Chapter 4), not whether effects are well defined (p. 35).
- Well-defined interventions need not be perfectly specified, and perfect specification is generally impossible. Example: surgeon experience is unspecified in experiment 1 and affects mortality. So the average effect may vary across populations even under the same protocol (pp. 35–36).
- More precise interventions give more precise questions and generally easier transport. Components with no effect on the outcome (e.g., scrub color) do not matter (p. 36).
- All this applies to both randomized and observational studies. In ideal experiments the interventions are specified and implemented, giving a common understanding. In observational studies investigators may have different views. Then "the effect of heart transplant" may be too vague. The vagueness can sometimes be removed by having experts focus on one specific intervention at a time (p. 36).
- An intervention is *sufficiently well defined* when, for all practical purposes, no meaningful vagueness remains. How do we know? "We don't." It is a matter of agreement among experts, based on available knowledge, and can change (pp. 36–37). Margin: "No causation without manipulation" (Holland 1986) captures the idea that meaningful causal inference requires sufficiently well-defined interventions. But such interventions may not be feasible at a given time. Genetic variants' effects were considered well defined before gene-editing technology existed (p. 36).

**Fine Point 3.3 — Possible worlds (p. 37).** In the philosophical counterfactual theories of Stalnaker and Lewis, $Y^a$ is the value of $Y$ in the closest possible world where the individual got $a$. Hence, under their definition of counterfactuals, $Y^a=Y$ if $A=a$, and consistency always holds. For $A\neq a$ the closest world is somewhat vague. Robins and Greenland argued that well-defined interventions should replace the closest-world concept, because counterfactuals are vague to the degree that interventions and contrasts are not made precise (p. 37).

**Non-intervention variables (pp. 37–38).**
- Investigators often want effects of variables that do not correspond to interventions someone implemented: biological states (blood pressure, LDL-cholesterol, weight), social factors (socioeconomic status). These can only be changed by intervening on their causes (p. 37).
- "The effect of becoming obese on myocardial infarction" has no meaningful interpretation, because the counterfactual is ill-defined. Specifying start, end and procedure of change would describe the effect of those interventions rather than of obesity (p. 37).
- Puzzle: experts agree that blood pressure causally affects stroke (evidence from physics, in vitro, animal clamps, autopsies, intervention studies), though $Y^a$ for blood pressure references no intervention (p. 37). Whether such effects are ill-defined depends on the outcome (margin: obesity and job discrimination as perceived by the employer) (p. 37).
- Proposed resolution: such statements imply a belief that some intervention $X$ (possibly yet to be discovered) changes $A$ to $a$ for that individual and has no direct effect on $Y$ except through $A$. This is an **effective no-direct-effect (ENDE) intervention**, $\mathrm{ENDE}(a)$. Its existence is logically equivalent to asserting that $Y^a$ and the joint counterfactuals $Y^{x,a}$ are well defined and equal (pp. 37–38).
- The belief may be more acceptable when the mechanisms are well understood. Antihypertensive drugs might be ENDE interventions for blood pressure. Diet and exercise are not, since they affect stroke through other pathways. It is harder to justify for socioeconomic status and myocardial infarction (p. 38).
- Hence for non-interventions the population average effect is well defined if $\mathrm{ENDE}(a)$ and $\mathrm{ENDE}(a')$ interventions exist for every individual. Otherwise one must restrict the population to individuals for whom they exist (p. 38).
- Considering small changes $\Delta$ near 0 (e.g., blood pressure by $\Delta$ mm Hg) makes ENDE interventions more credible. Direct effects, such as drug toxicity, may arise only for large changes. $Y^\Delta$ is $Y^a$ evaluated at $a=A-\Delta$ (p. 38).
- Where experts disagree, a study design might support the claim that the effect of $X$ on $Y$ is completely mediated by $A$ (Fine Point 6.4) (p. 38).

**Fine Point 3.4 — Interventionist approach (p. 39).** The book's framework is based on well-defined counterfactuals defined through well-defined interventions. The authors extend it to non-interventions by clarifying conditions for meaningful quantitative inference. They state that they do not claim it is the only valid philosophy of causality, but that "to our knowledge" no alternative framework yields practically interpretable effect estimates (p. 39). (Other authors, e.g., Pearl, Schwartz et al., Glymour and Spiegelman, treat the effect as well defined where many experts would not recognize ENDE interventions (p. 42, margin).)

*Intuition note.* "The effect of treatment $a$" is a question about doing something specific. If different people mean different things by "heart transplant", there are several different causal effects under one name. The wording of the intervention fixes which one is being estimated.

### 3.5 Consistency: second, link counterfactuals to the observed data (pp. 38–40)
- Second component: the "equal" sign in $Y^a=Y$ for those with $A=a$ (p. 38).
- When the intervention was actually implemented per an experiment's protocol, the link is uncontroversial. By definition $Y=Y^A=Y^a$ for $A=a$ (p. 38).
- The same reasoning applies if the intervention was implemented in the real world, even not by investigators. Example: transplant-eligible patients offered heart transplant ($A=1$) or medical therapy ($A=0$). Then "heart transplant" $a=1$ means whatever followed the offer at that time and place, and $Y^{a=1}=Y$ for those with $A=1$ (p. 39). The effect may be of questionable relevance elsewhere if investigators cannot approximately characterize what $a=1$ means (p. 39).
- The choice of interventions depends on available data. Suppose investigators define $a=1$ precisely (exact procedures, anesthesia, technique, care, immunosuppression), but the data hold only an indicator $B$ of whether a transplant occurred. Then $Y^{a=1}$ for someone with $B=1$ is not necessarily equal to the observed $Y$ (p. 39). The same letter for the variable and the intervention is reserved for cases where the observed value corresponds to the well-defined intervention. So describing a well-defined $a$ is not sufficient for consistency (p. 39).
- Conversely, a recorded variable $A$ does not guarantee that "the causal effect of $A$" is meaningful if the corresponding interventions are ill-defined. A well-defined $a$ with nobody in the data having $A=a$ is an extreme form of non-positivity (p. 40).
- Good practice: make reasoning transparent so others can challenge the consistency argument (p. 40).

**Fine Point 3.5 — Attributable fraction (p. 40).**
- Ambrosia ($A=1$) or nectar ($A=0$) at a dinner, 20 people, 10 per group. Next day 7 of 10 with $A=1$ and 1 of 10 with $A=0$ were sick. Assuming exchangeability, causal risk ratio $=0.7/0.1=7$ and causal risk difference $=0.7-0.1=0.6$ (p. 40).
- Observed cases: 8, so $\Pr[Y=1]=8/20=0.4$. If everyone had $a=0$, $\Pr[Y^{a=0}=1]=0.1$. Excess $=0.4-0.1=0.3$, and $0.3/0.4=0.75$. So 75% of cases are attributable to treatment: of the 8 observed cases only 2 would have occurred under $a=0$ for all (p. 40).
- The *excess (attributable) fraction* is
$$\frac{\Pr[Y=1]-\Pr[Y^{a=0}=1]}{\Pr[Y=1]}.$$
- It generally differs from the *etiologic fraction*, the proportion of cases mechanically caused by exposure. Example: treatment produces 7 cases among the untreated-if-treated but prevents the 1 actual untreated case, and the treated would have had 1 different case if untreated. Then the excess fraction is a lower bound on the etiologic fraction. The etiologic fraction can be computed only in randomized experiments under strong assumptions (p. 40).

### 3.6 The target trial (pp. 41–44)
- When the three conditions are assumed, an observational analysis can be viewed as an attempt to emulate a hypothetical randomized experiment, the *target trial* (p. 41). For each effect we may (i) specify the protocol of the target trial we cannot conduct, and (ii) describe how the observational data emulate it. If emulation were successful, results would not differ from the target trial's (p. 41).
- Key protocol components: eligibility criteria, interventions (treatment strategies), assignment, outcomes, start and end of follow-up, causal contrasts. Eligibility must allow all individuals to receive all treatments of interest, otherwise some individual effects are undefined. In Parts I–II each individual meets eligibility once, which marks time zero (p. 41). PICO is sometimes used to summarize some components (margin, p. 41).
- Specifying the target trial defines $Y^a$ and the effect of interest (p. 41).
  - In experiments, $A$ values are actions applied by the investigators, so $Y^a$ is well defined. The target trial is the actual trial (aspirin and stroke example) (p. 41).
  - In observational studies, $Y^a$ is well defined if each value of $A$ corresponds to a well-defined action some agent could have applied. Example: aspirin prescription among people with no absolute indications or contraindications. Experts tend to agree a target trial could have been conducted (p. 41).
- **Non-intervention variables** (pp. 42–43):
  - *Genotype*: $Y^a$ is well defined if ENDE interventions $X$ exist that could change every individual's genotype to $a$ at conception without affecting $Y$ except via $A$. The target trial randomizes to $X$ rather than $A$. $X$ need not be known (decades ago, experts regarded the effect as well defined; gene editing was developed later) (p. 42).
  - *Systolic blood pressure*: well defined if ENDE interventions exist. Many experts believe some pharmacological interventions qualify in some populations, perhaps for a limited range of changes. So effects of modest differences can be defined via a target trial randomizing to $X$ (p. 42).
  - *Socioeconomic status*: most experts doubt that ENDE interventions exist (and may disagree on what it means). Then the effect is not well defined and no target trial can be specified (p. 42).
  - Summary: if $A$ is an intervention, the target trial randomizes to $a$. If $A$ is a non-intervention and ENDE interventions $X$ are believed to exist, it randomizes to $X$. Quantitative causal inference for non-interventions requires this assumption, even if $X$ cannot be specified (p. 42). Whether a variable is an intervention is often debatable, and there is a gradient (margin, p. 42).
- Valid emulation needs enough information to map protocol elements to the data (eligibility, groups, outcomes), and, when using IP weighting or standardization, adjustment variables $L$ sufficient for conditional exchangeability (pp. 42–43). For blood pressure and stroke, diet and exercise are believed to affect both exposure and stroke, so they should be adjusted for (p. 43). The text writes "weight A" here although the example concerns blood pressure; see Reading notes. Chapter 16 gives alternative identifying conditions (p. 43).

**Fine Point 3.6 — When causal inference for non-interventions goes unquestioned (p. 43).**
- In a randomized trial with assignment $Z$ and received treatment $A$: the effect of $Z$ (intention-to-treat) is well defined because $Z$ is an intervention. With perfect adherence $Z=A$ and, if $Z$ has no direct effect, $Z$ is an ENDE intervention for $A$ (p. 43).
- With imperfect adherence, $Z$ is not an ENDE intervention for everyone. The effect of $A$ is then well defined only if ENDE interventions $X$ on $A$ exist. Most experts would agree (e.g., adding aspirin to food without people's knowledge) (p. 43).
- In the subset who would have $A=1$ if $Z=1$ and $A=0$ if $Z=0$ (the "compliers", Chapter 16), $Z$ is an ENDE intervention, so the effect of $A$ there is well defined and equals that of $Z$. If $Z$ has direct effects on $Y$ not through $A$, the effect of $Z$ differs from that of $X$ even under full adherence (p. 43).

**Why the target trial helps, and its limits (pp. 43–44).**
- Anchoring an analysis to a target trial helps decision makers recognize analyses that imply extreme or impossible interventions (pp. 43–44).
- Example: comparing mortality at body mass index 25 vs. 30 at start of follow-up implies an instantaneous, possibly very large weight change. No ENDE interventions are known for that. A modified target trial could assign some individuals to lose 5% of BMI every year from age 40 while BMI stays over 25. Experts may still disagree, but such interventions are more likely to exist than instantaneous weight loss (p. 44).
- One may then proceed as if these interventions existed, adjusting for prognostic factors $L$. The authors state that results are then not causally interpretable and may not be adequate to guide decisions. They may still carry some information about ENDE interventions if they existed, or inspire their development (p. 44).

**Fine Point 3.7 — Limits of target trial emulation (p. 44).** The mean counterfactual under "heart transplant" can be read as the average outcome under (i) all $n$ eligible individuals treated concurrently, or (ii) each individual $i$ treated while the other $n-1$ receive their actual treatment. Interpretation (ii) is an average of $n$ interventions and is relevant to a physician/patient pair. It is the one used implicitly in the book. (i) is not well defined, because it does not say how the health system would be redesigned to supply hearts. If redesign were specified, current data (generated under the existing system) would be inadequate. Observational data may be insufficient to characterize system-wide scale-up. This relates to, but differs from, interference (Fine Point 1.1), where counterfactuals under (i) are generally assumed well defined (p. 44).

**Technical Point 3.2 — Recursive substitution (p. 45).**
- With variables ordered chronologically, the *one-step-ahead counterfactuals* are the counterfactual values of a variable when all earlier variables that could be intervened on have been intervened on. For $L,A,M,Y$ with interventions on $L,A,M$ well defined they are $L, A^l, M^{l,a}, Y^{l,a,m}$. If interventions on $L$ were not well defined: $L, A, M^a, Y^{a,m}$ (p. 45).
- Other factuals and well-defined counterfactuals follow by recursive substitution (p. 45):
$$A=A^{L},\quad M^a=M^{L,a},\quad M=M^{L,A}=M^{L,A^L},\quad M^l=M^{l,A^l},$$
$$Y^a=Y^{L,a,M^a}=Y^{L,a,M^{L,a}},\quad Y^m=Y^{L,A,m}=Y^{L,A^L,m},$$
$$Y^l=Y^{l,A^l,M^l}=Y^{l,A^l,M^{l,A^l}},\quad Y^{l,m}=Y^{l,A^l,m},\quad Y=Y^{L,A,M}=Y^{L,A^L,M^{L,A^L}}.$$
- The one-step-ahead counterfactuals also encode no-direct-effect assumptions. If $a$ has no direct effect on $Y$ (relative to $L$ and $M$), then $Y^{l,a,m}=Y^{l,m}=Y^{l,A^l,m}$ (p. 45).
- Heart transplant experiments: experiment 1 has one-step-ahead counterfactuals $A_1^{a_0=1}$, $A_2^{a_0=1,a_1}$, $A_3^{a_0=1,a_1,a_2}$ and $Y^{a_0=1,a_1,a_2,a_3}$. In experiment 2, $Y^{a=1}=Y^{a_0=1,A_1^{a_0=1},A_2^{a_0=1},A_3^{a_0=1}}$, with $A_2^{a_0=1}=A_2^{a_0=1,A_1^{a_0=1}}$ and $A_3^{a_0=1}=A_3^{a_0=1,A_1^{a_0=1},A_2^{a_0=1}}$. These $A_j^{a_0=1}$ are random (differing between individuals) counterfactuals (p. 45).
- This shows why transporting the outcome distribution of experiment 2 can be harder than for experiment 1. The distribution of $Y^{a_0=1,a_1,a_2,a_3}$ will generally differ between populations if the distribution of one or more of $A_1^{a_0=1}, A_2^{a_0=1}, A_3^{a_0=1}$ differs (p. 45).
- If one-step-ahead counterfactuals are well defined, recursive substitution applies equally to observational and randomized studies, since it concerns only logical relations between counterfactuals and factuals (p. 45).

## Toy example (ours, not from the text)
**Setting.** Within one stratum $L=1$, 200 people: 100 treated, 100 untreated. Observed deaths: 30 of 100 treated and 30 of 100 untreated. The observed risk ratio is $0.30/0.30=1$. Assume consistency and positivity hold (both groups are present).

**Three stories compatible with these same observed data**, differing in the unmeasured $U$ (as in Fine Point 3.1). In each, $\Pr[Y^{a=1}=1]$ for the treated is the observed 0.30 and for the untreated is assumed to be 0.30. Also, for the untreated, $\Pr[Y^{a=0}=1]$ is the observed 0.30.

| Story | Risk the *treated* would have had if untreated | $\Pr[Y^{a=0}=1]$ over all 200 | $\Pr[Y^{a=1}=1]$ | Causal risk ratio |
|---|---|---|---|---|
| A: exchangeable | 0.30 | $(100\cdot0.30+100\cdot0.30)/200=60/200=0.30$ | $0.30$ | $0.30/0.30=1$ |
| B: treated sicker on unmeasured $U$ | 0.50 | $(100\cdot0.50+100\cdot0.30)/200=80/200=0.40$ | $0.30$ | $0.30/0.40=0.75$ |
| C: treated healthier on unmeasured $U$ | 0.10 | $(100\cdot0.10+100\cdot0.30)/200=40/200=0.20$ | $0.30$ | $0.30/0.20=1.5$ |

**Reading.** The observed table is identical, yet the causal risk ratio is 1, 0.75 or 1.5. Only Story A gives conditional exchangeability. Choosing it is an assumption external to the data. The direction of the bias mirrors Fine Point 3.1: risk factors more frequent among the treated give a causal RR below 1 relative to the association, and more frequent among the untreated give above 1 (pp. 29–31).

**Positivity check.** If the stratum had 0 untreated people, the untreated risk would be $0/0$ and no counterfactual $Y^{a=0}$ could be estimated for the treated (pp. 33–34).

## Concepts
- [[consistency]] (new) — $Y=Y^A$: observed outcome equals the counterfactual under the treatment actually received; needs well-defined interventions plus a link to recorded data (p. 33; p. 38)
- [[positivity]] (new) — $\Pr[A=a\mid L=l]>0$ for all contrast values $a$ and all $l$ present in the population of interest, for the $L$ needed for exchangeability (p. 32)
- [[conditional-exchangeability]] (new) — $Y^a\perp\!\!\!\perp A\mid L$; within levels of $L$ the treated and untreated would have had the same average outcome; untestable (pp. 28–31). Related canon: Assignment mechanism / ignorability.
- [[identifiability]] (new) — an effect is identifiable if the assumptions imply the observed-data distribution fits a single effect value (p. 29)
- [[identifiability-conditions]] (new) — the three conditions (consistency, exchangeability, positivity) that let an observational study be treated as conditionally randomized (p. 28)
- [[potential-outcomes]] — counterfactuals $Y^a$ taken as primitives; observed $Y=AY^{a=1}+(1-A)Y^{a=0}$ for binary $A$ (p. 33)
- [[fundamental-problem-of-causal-inference]] — $Y^a$ is unknown for those with $A\neq a$, so conditional exchangeability cannot be verified (margin, p. 31)
- [[well-defined-intervention]] (new) — an action describable in a protocol so no meaningful vagueness remains in $Y^a$; "sufficiently well-defined" is an expert agreement (pp. 34–37)
- [[ende-intervention]] (new) — intervention $X$ that sets $A$ to $a$ with no direct effect on $Y$ except through $A$; its existence makes effects of non-interventions well defined (p. 37)
- [[target-trial-emulation]] — specify the hypothetical randomized trial and emulate it with observational data (p. 41)
- [[attributable-fraction]] (new) — $\frac{\Pr[Y=1]-\Pr[Y^{a=0}=1]}{\Pr[Y=1]}$; excess fraction, a lower bound on the etiologic fraction in the text's example (p. 40)
- [[transportability]] (new) — whether a causal effect from one population carries to another; affected by how precisely the intervention is specified (p. 35)
- [[instrumental-variable]] (new) — a treatment predictor assumed to be as-if randomized given measured covariates; deferred to Chapter 16 (p. 28)
- [[recursive-substitution]] (new) — building factuals and counterfactuals from one-step-ahead counterfactuals (p. 45)

## Canonical instances
- [[heart-transplant-table-3-1]] — the 20-person data set: $L$ imbalance 69% vs 43%, $\Pr[A=1\mid L]=0.75/0.50$, causal risk ratio 1 (pp. 28–30)
- [[figure-3-1-positivity-violation]] — tree with $\Pr[A=0\mid L=1]=0$ (p. 33)
- [[smoking-unmeasured-confounder]] — doctors prefer nonsmokers, so exchangeability given $L$ fails (pp. 30–31)
- [[two-heart-transplant-trials]] — fully specified vs. pragmatic trial; the same label, different $Y^{a=1}$ (pp. 34–35)
- [[blood-pressure-stroke-ende]] — effect of a non-intervention made meaningful by ENDE interventions (pp. 37–38, 42)
- [[ambrosia-attributable-fraction]] — 7/10 vs 1/10 sick; 75% of cases attributable (p. 40)
- [[bmi-weight-loss-target-trial]] — instantaneous BMI 25 vs 30 versus gradual 5% yearly loss (p. 44)

## Bridges (candidates)
- [structural-analogy] conditional exchangeability / ignorable assignment ↔ missing data: $Y^a$ is missing for those with $A\neq a$; ignorability plays the role of "missing at random" given $L$.
- [structural-analogy] identifying assumption external to the data ↔ Bayesian inference: where data fit many effect values, a prior or assumption must supply the rest (here the prior is a point-mass-like assumption of exchangeability).
- [structural-analogy] positivity and the IP-weighted mean $\mathrm E[I(A=a)Y/f[A\mid L]]$ ↔ Monte Carlo: importance sampling needs the proposal's support to cover the target's.
- [structural-analogy] sequential refinement of $Y^{a_0,a_1,a_2,a_3}$ (Technical Point 3.2) ↔ hierarchical models: unspecified components $A_j^{a_0=1}$ are random quantities whose population distribution drives transportability.

## Questions this raises
- If exchangeability can never be tested, how can sensitivity analyses or priors express how wrong it might be?
- How is positivity checked in practice, and what should be done when only some strata lack treated or untreated people (Chapter 12)?
- How do the differences between the two heart transplant trials show up in a Bayesian hierarchical model of effects across populations?
- Which alternative identifying conditions (Chapter 16) replace conditional exchangeability, and what do they cost?

## Reading notes
- Printed pages 27–46 = pdf 36–55 (printed = pdf − 9). Page labels give printed numbers; citations use them. Printed p. 46 contains only a running header.
- Source PDF is the online revision dated 2026-08-19, not the 2020 print edition. It cites works up to 2025 (e.g., Hernán et al. 2025, Madenci et al. 2024), so chapter references (e.g., Chapter 22 on target trial) may differ from older editions.
- The text layer for Technical Points 3.1 and 3.2 was garbled; formulas were checked against the page images.
- Section 3.6 (p. 43) says "variables that make individuals at different levels of blood pressure conditionally exchangeable", then "affect both weight A and the risk of stroke". "Weight" does not match the blood-pressure example. I reported it as the text prints it, noting the mismatch.
- Chapter 3 has no exercises, so there is no Exercises section.
- Text and image agree on the Figure 3.1 numbers. Counts beside the branches are 4, 4, 0, 12 for the treatment arms and 3/1, 3/1, 0/0, 4/8 for outcomes.
