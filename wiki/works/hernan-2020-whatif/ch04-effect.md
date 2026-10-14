---
id: hernan-2020-whatif/ch04-effect
work: hernan-2020-whatif
unit: "4 Effect modification"
pages: 47-60
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Effect modification

## L0 — One line
There is no single "the causal effect" of a treatment: the average effect depends on the population's mix of effect modifiers, and whether modification exists depends on the effect measure, so you must say which population and which measure you mean.

## L1 — The gist (≤ 120 words)
The chapter asks what happens when the average causal effect differs across subgroups. A variable V is an effect modifier when the average effect varies across its levels. Whether modification exists depends on the effect measure (difference or ratio). Stratifying by V identifies it, and standardization or IP weighting can deal with confounding separately. The population effect depends on how the modifiers are distributed, which limits transporting results to other populations. Standardization, IP weighting, stratification/restriction and matching all adjust for confounding, but they target different effects: marginal, conditional, or effect in the treated or untreated. Different numbers from different methods can therefore be all correct.

**Prerequisites:** potential outcomes $Y^a$; conditional exchangeability, positivity; risk difference and risk ratio; standardization and IP weighting (Chapters 1–3).

## L2 — Key ideas (5–10 bullets)
- A null average effect in a population does not imply a null effect in subsets. In Table 4.1 the effects in women and men cancel exactly (p. 48).
- Effect modification by V means the average causal effect varies across levels of V. It is scale-dependent: it can exist on the ratio scale but not on the difference scale unless it is qualitative, i.e. the stratum effects point in opposite directions (p. 48).
- Stratification identifies effect modification by measured V. Under conditional randomization it requires stratifying by V and also standardizing or IP weighting on L, a step that can be skipped when V equals the L needed for exchangeability (pp. 49–50).
- Effect modification by V need not mean V is causal. V may be only a surrogate for the true causal modifier, e.g. quality of surgery (pp. 50–51).
- Why care: the average effect changes with the population mix, transportability (extrapolating an effect to another population) is hard, the groups that benefit most can be found, and mechanisms can be explored (pp. 51–53).
- Additive modification matters most for deciding whom to treat. Multiplicative modification can arise just from different baseline risks, so report absolute risks (p. 53).
- Stratification as a form of adjustment forces conditioning on all L needed for exchangeability, and needs positivity. Matching builds a subset where L has the same distribution in treated and untreated (pp. 54–56).
- The four adjustment methods answer different questions, so their results can differ, e.g. 0.8, 2.0, 0.5, 1.0 (pp. 56–58).
- The odds ratio is noncollapsible (the population measure is not a weighted average of the stratum measures): the population odds ratio can lie outside the stratum-specific range even in a randomized experiment (p. 60).

## L3 — Walkthrough

### Introduction (p. 47)
Many causal questions concern subsets of the population (e.g. city dwellers vs visitors). Whether to compute the effect in the whole population or in a subset depends on the inferential goal (p. 47). For a nationwide fluoridation programme reaching all households, the policy maker mainly needs the average effect in the whole population (p. 47). Subset effects matter when the intervention can be targeted or when findings must be applied to other populations (p. 47). Main message: there is not such a thing as *the* causal effect of treatment; the effect depends on the population studied (p. 47).

### 4.1 Heterogeneity of treatment effects (pp. 47–48)
Table 4.1 is Table 1.1 (20 members of Zeus's family) plus an indicator $V$: $V=1$ women (first 10 rows), $V=0$ men (last 10 rows) (p. 47). Whole population: $\Pr[Y^{a=1}=1]=10/20=0.5$ and $\Pr[Y^{a=0}=1]=10/20=0.5$. Causal risk ratio is 1 and causal risk difference is 0 (p. 47).

- Women ($V=1$): $\Pr[Y^{a=1}=1|V=1]=6/10=0.6$, $\Pr[Y^{a=0}=1|V=1]=4/10=0.4$. Risk ratio $0.6/0.4=1.5$, risk difference $0.2$. Transplant increases risk of death in women (pp. 47–48).
- Men ($V=0$): $\Pr[Y^{a=1}=1|V=0]=4/10=0.4$, $\Pr[Y^{a=0}=1|V=0]=6/10=0.6$. Risk ratio $0.4/0.6=2/3$, risk difference $-0.2$. Transplant decreases risk in men (p. 48).

So a null average effect in the population does not imply a null effect in a subset. Here the two effects have equal size and opposite direction, and with 50% of each sex they cancel exactly (p. 48). Exact cancellation is probably rare, but heterogeneity of individual effects is often expected because individuals differ in susceptibility (p. 48). The exception is the sharp null hypothesis (no effect for every individual). Then the effect is null in every subset (p. 48).

**Definition (effect modifier).** $V$ is a modifier of the effect of $A$ on $Y$ when the average causal effect of $A$ on $Y$ varies across levels of $V$ (p. 48). Only variables $V$ not affected by treatment are considered (p. 48). Because the effect can be measured on different scales, the presence of modification depends on the measure (p. 48):

- Additive modification: $\mathrm{E}[Y^{a=1}-Y^{a=0}|V=1]\neq \mathrm{E}[Y^{a=1}-Y^{a=0}|V=0]$ (p. 48).
- Multiplicative modification: $\dfrac{\mathrm{E}[Y^{a=1}|V=1]}{\mathrm{E}[Y^{a=0}|V=1]}\neq\dfrac{\mathrm{E}[Y^{a=1}|V=0]}{\mathrm{E}[Y^{a=0}|V=0]}$ (p. 48).
- The odds-ratio scale is not considered because the odds ratio is rarely, if ever, the parameter of interest for causal inference (p. 48).

In Table 4.1, sex modifies the effect on both scales. The effect is in opposite directions (ratio $>1$ vs $<1$; difference $>0$ vs $<0$), which is **qualitative effect modification** (p. 48). With qualitative modification, additive modification implies multiplicative modification, and vice versa. Without it, modification may exist on one scale but not the other (p. 48).

Second study (p. 48): $\Pr[Y^{a=0}=1|V=1]=0.8$, $\Pr[Y^{a=1}=1|V=1]=0.9$, $\Pr[Y^{a=0}=1|V=0]=0.1$, $\Pr[Y^{a=1}=1|V=0]=0.2$. No additive modification: $0.9-0.8=0.1=0.2-0.1$. Multiplicative modification: $0.9/0.8=1.1\neq 0.2/0.1=2$ (p. 48). Since one cannot generally speak of modification without naming the measure, some authors say "effect-measure modification" (p. 48).

*Intuition note:* "Modification" is a property of a subgroup comparison on a chosen scale. The same data can show modification on the ratio scale and none on the difference scale.

### 4.2 Stratification to identify effect modification (pp. 49–51)
To see whether $V$ modifies the effect, compute the effect of $A$ on $Y$ in each stratum of $V$ (p. 49). In Table 4.1 this was possible because both counterfactual outcomes were listed. Real data have only $A$ and observed $Y$, so what works depends on study design (p. 49).

*Marginally randomized experiment.* Leaving aside random variability, the causal risk difference equals the associational one. Unconditional randomization is expected to give exchangeability in every subset. So, e.g., $\Pr[Y^{a=1}=1|V=1]-\Pr[Y^{a=0}=1|V=1]=\Pr[Y=1|A=1,V=1]-\Pr[Y=1|A=0,V=1]$, and likewise for men (p. 49). Identifying modification just needs the association measure in each level of $V$. This gives average effects in subsets, not individual effects (p. 49).

*Conditional randomization.* 40 people: $A$ randomized with probability 0.75 if $L=1$ (severe) and 0.50 if $L=0$. 20 are Greek ($V=1$, Table 2.2) and 20 Roman ($V=0$, Table 4.2) (p. 49). Population: $\Pr[Y^{a=1}=1]=0.55$, $\Pr[Y^{a=0}=1]=0.40$ (computed by standardization or IP weighting). Risk difference $0.15$, risk ratio $0.55/0.40=1.375$ (p. 49). The same holds in an observational study if $Y^a\perp\!\!\!\perp A|L$ is believed (p. 49).

Procedure for $\Pr[Y^{a}=1|V=v]$: (1) stratify by $V$; (2) standardize by $L$ (or IP weight with weights depending on $L$). Step 2 can be ignored when $V$ equals the $L$ needed for conditional exchangeability (p. 50).

- Greeks: risk difference 0, risk ratio 1 (Chapter 2) (p. 50).
- Romans: $\Pr[Y^{a=1}=1|V=0]=0.6$, $\Pr[Y^{a=0}=1|V=0]=0.3$. Risk difference $0.3$, risk ratio $2$ (p. 50).

So there is additive and multiplicative modification by nationality. It is not qualitative, since the effect is harmful or null in both strata (p. 50).

*Surrogate vs causal modifier.* No claim is made about mechanism. If heart surgery is better in Greece than in Rome, nationality would show modification but be only a **surrogate effect modifier**; quality of care is the **causal effect modifier** (p. 50). Hence "effect modification by $V$" does not imply $V$ plays a causal role. Some authors prefer "effect heterogeneity across strata of $V$". The next chapter introduces "interaction", which does attribute a causal role (pp. 50–51).

**Fine Point 4.1 — Effect in the treated (p. 50, Fig. 4.1 p. 51).** The effect in the treated is not null if $\Pr[Y^{a=1}=1|A=1]\neq\Pr[Y^{a=0}=1|A=1]$, or by consistency if $\Pr[Y=1|A=1]\neq\Pr[Y^{a=0}=1|A=1]$. Causal risk difference in the treated: $\Pr[Y=1|A=1]-\Pr[Y^{a=0}=1|A=1]$. Causal risk ratio in the treated (standardized morbidity ratio, SMR): $\Pr[Y=1|A=1]/\Pr[Y^{a=0}=1|A=1]$. The untreated versions replace $A=1$ by $A=0$ (p. 50). Figure 4.1 compares E$[Y|A=1]$ with E$[Y^{a=0}|A=1]$ for the treated, and E$[Y^{a=1}|A=0]$ with E$[Y|A=0]$ for the untreated (p. 51). The effect in the treated differs from the population effect if the distribution of individual effects differs between treated and untreated. Treatment group is then a marker for the true modifiers; the author would not say "modification by treatment" (p. 50). The book focuses on the population effect because effects in the treated or untreated cannot be directly generalized to time-varying treatments (p. 50).

### 4.3 Why care about effect modification (pp. 51–53)
Reasons to measure pre-treatment descriptors $V$, even in randomized experiments (p. 51):

1. **Population dependence.** If $V$ modifies the effect, the average effect differs between populations with different prevalence of $V$. In Table 4.1 (50% women) the average effect is null. In a population with more women (e.g. graduating college students) it would be harmful (p. 51). With non-qualitative modification, the magnitude but not the direction of the average effect may vary across populations (examples: asbestos by smoking status, universal health care by income) (p. 51). So there is generally no "the average causal effect of $A$ on $Y$ (period)", only the effect "in a population with a particular mix of causal effect modifiers" (p. 51).

   *Transportability.* Extrapolating an effect from one population to another is **transportability** (lack of it is sometimes called lack of external validity) (p. 52). Here the effect differs by sex and nationality, so the population average may not transport to populations with other modifier distributions (p. 52). Conditional effects in strata of modifiers may be more transportable, but there is no guarantee. Other unmeasured modifiers may differ between populations, and these are not needed for exchangeability but are just outcome risk factors. So transportability is harder than identification within one population (p. 52). It is an unverifiable assumption relying on subject-matter knowledge. Most experts would agree that the health effect of +\$100 household income in Niger does not transport to the Netherlands, but that cholesterol-lowering drug effects in Europeans transport to Canadians (p. 52). Smith and Pell (2003) found no major modifiers of parachute effects, so restricted trials would not harm transportability (margin note, p. 52).

   **Fine Point 4.2 — Transportability (p. 54).** Transportability may be justified if these are similar between study and target populations: (a) the distribution of effect modifiers; (b) the definition of treatment; (c) interference patterns (treating one person affects others' outcomes). Restricting to stratum-specific effects, or reweighting the four stratum effects (Roman/Greek × women/men) by the second population's stratum proportions, may improve transportability. There is no guarantee, because of unmeasured modifiers, interference and treatment definition (p. 54).

   **Technical Point 4.1 — Computing the effect in the treated (p. 52).** The population effect used $Y^a\perp\!\!\!\perp A|L$ for $a=0,1$. The effect in the treated needs only partial exchangeability $Y^{a=0}\perp\!\!\!\perp A|L$; the effect in the untreated needs $Y^{a=1}\perp\!\!\!\perp A|L$ (p. 52). Counterfactual means $\mathrm{E}[Y^a|A=a']$ are then:
   - Standardization: $\sum_l \mathrm{E}[Y|A=a,L=l]\Pr[L=l|A=a']$ (p. 52).
   - IP weighting: the IP-weighted mean
   $$\frac{\mathrm{E}\!\left[\frac{I(A=a)\,Y}{f(A|L)}\Pr[A=a'|L]\right]}{\mathrm{E}\!\left[\frac{I(A=a)}{f(A|L)}\Pr[A=a'|L]\right]}$$
   with weights $\Pr[A=a'|L]/f(A|L)$ (p. 52).

2. **Finding who benefits most.** In Table 4.1, with qualitative modification by sex, physicians without other information would treat the next patient only if he is a man (p. 53). In the second example (risks 0.8→0.9 and 0.1→0.2) the risk difference is the same 0.1 in both strata. An intervention on everybody is equally effective in absolute terms in both strata despite multiplicative modification (p. 53). If there is a nonzero effect in at least one stratum and $\Pr[Y^{a=0}=1|V=v]$ varies with $v$, then modification is guaranteed on the additive or the multiplicative scale (p. 53). The author states that additive modification is the appropriate scale for identifying groups that benefit most. Without additive modification, learning of multiplicative modification may not help decisions (p. 53). In the second example, multiplicative modification is expected: risk under no treatment in $V=1$ is 0.8, so the maximum possible risk ratio there is $1/0.8=1.25$, guaranteed to differ from 2 in $V=0$. It arises from differing baseline risks. So, as a general rule, report the absolute counterfactual risks $\Pr[Y^{a=1}=1|V=v]$ and $\Pr[Y^{a=0}=1|V=v]$ in every stratum, not just their ratio or difference (p. 53).

3. **Mechanisms and interaction.** Modification can give clues to mechanisms (e.g. higher HIV risk in uncircumcised men) and may be a first step toward characterizing interactions between two treatments. "Effect modification" and "interaction" are sometimes used as synonyms. The next chapter treats interaction as a related but different causal concept (p. 53).

*Intuition note:* The average effect is a weighted mix of subgroup effects, so it changes when the mix changes. Also, a ratio can differ across groups simply because their untreated risks differ.

### 4.4 Stratification as a form of adjustment (pp. 53–55)
Until now the goal was the average effect in the whole population, which without marginal randomization requires adjusting for $L$ (conditional exchangeability) by standardization or IP weighting (p. 53). Identifying modification by $V$ requires stratifying by $V$ in addition to adjusting for $L$. In summary: standardization/IP weighting adjusts for $L$; stratification identifies modification by $V$ (pp. 53–54).

But in practice stratification is often used as an alternative to adjust for $L$, so many treat "stratification" and "adjustment" as synonyms (p. 54). An epidemiologist asked to adjust for $L$ would split Table 2.2 into $L=0$ and $L=1$ and report $\Pr[Y=1|A=1,L=l]/\Pr[Y=1|A=0,L=l]=1$ for $l=0,1$ (pp. 54–55). Under conditional exchangeability given $L$ these have a causal interpretation as effects in $L=l$, since $Y^a\perp\!\!\!\perp A|L$ gives $\Pr[Y=1|A=a,L=0]=\Pr[Y^a=1|L=0]$ (margin, p. 55). They are **conditional effect measures**; the Chapter 2 ratio was **marginal** (p. 55). Here all three equal 1 because there is no modification by $L$ (p. 55).

Drawbacks of stratification as adjustment (p. 55):
- It gives multiple stratum-specific measures, each for a nonoverlapping subset. In general none gives the effect in the whole population.
- It requires stratifying on a combination of *all* $L$ needed for conditional exchangeability. In the Greek/Roman data one must compute effects for Romans with $L=1$, Greeks with $L=1$, Romans with $L=0$, Greeks with $L=0$. One cannot get the effect in Romans from the association in $V=0$, because $V$ alone does not give conditional exchangeability.
- It forces evaluating modification by all such $L$ whether or not one cares. Stratifying by $V$ then standardizing/IP weighting for $L$ treats exchangeability and modification separately.
- Other problems: noncollapsibility of the odds ratio (Fine Point 4.3) and bias with time-varying treatments when $L$ is affected by prior treatment (Part III). With time-varying treatments, stratum-specific measures may lack a causal interpretation even under exchangeability, positivity and well-defined interventions (margin, p. 55).
- Stratification requires positivity: effects cannot be computed in $L=l$ with only treated or only untreated individuals (margin, p. 55).

**Restriction:** computing effects in only some strata. Stratification is restriction applied to several comprehensive, mutually exclusive subsets with exchangeability within each. When positivity fails in some strata, restriction limits inference to strata where positivity holds (p. 55).

### 4.5 Matching as another form of adjustment (pp. 55–56)
Matching builds a subset in which $L$ has the same distribution in treated and untreated (p. 55). In Table 2.2, for each untreated individual in noncritical condition ($A=0,L=0$) randomly select a treated one with $L=0$; likewise for $L=1$. Each untreated person and her match form a *matched pair*; $L$ is the *matching factor* (p. 56). The example has 7 pairs: Rheia–Hestia, Kronos–Poseidon, Demeter–Hera, Hades–Zeus ($L=0$); Artemis–Ares, Apollo–Aphrodite, Leto–Hermes ($L=1$). All untreated but only a sample of treated were selected. The proportion with $L=1$ is $3/7$ in both groups by design (p. 56).

Under conditional exchangeability given $L$, the matched population has unconditional exchangeability of treated and untreated. Outcomes can be compared directly: risk in treated $3/7$, in untreated $3/7$, risk ratio 1 (p. 56). Matching ensures positivity in the matched population because strata with only treated or only untreated are excluded (p. 56).

- Often one chooses the smaller group (here the untreated) and finds matches in the other. The chosen group defines the subpopulation. Here this gives the *effect in the untreated*. With fewer treated, one generally computes the *effect in the treated*. Matching can be one-to-many (p. 56).
- With vector $L$, match within strata of all variables in $L$. With more factors, exact matches become less likely (margin; Stuart 2010 cited for approximate matching) (p. 56).
- Any chosen distribution of $L$ can be created by individual matching or by frequency matching (e.g. select treated so that 70% have $L=1$, then repeat for the untreated) (p. 56).
- Margin: the discussion is for cohort studies. In case-control matching, even if the factors suffice for conditional exchangeability, unconditional exchangeability is not achieved. Stratification on the matching factors is required for conditional effects (p. 56).
- The matched population is a subset, so its distribution of causal effect modifiers generally differs from the original (p. 56).

### 4.6 Effect modification and adjustment methods (pp. 56–59)
Standardization and IP weighting can compute marginal or conditional effects. Stratification/restriction and matching only compute conditional effects in certain subsets (pp. 56–57). All four require exchangeability and positivity, but only in the subset relevant to the effect. For the effect in $L=l$, only in that subset; for the marginal effect, in all levels of $L$ (p. 57). Without effect modification, the four give equal measures (as in Chapter 2: ratio 1 for population, strata and untreated). In general they differ (p. 57).

**Technical Point 4.2 — Pooling (p. 57).** In samples one wants narrower confidence intervals. If there is no effect-measure modification, a pooled stratum-specific measure (Woolf, Mantel-Haenszel, maximum likelihood; weighted averages with variance-reducing weights) is more precise than each stratum estimate. Regression models with all product terms among $L$ but none between $A$ and $L$ also pool. The pooled measure is still conditional. In the heart-transplant example the Mantel-Haenszel risk ratio was 0.88 for outcome $Z$. This is meaningful only if the stratum ratios 2 and 0.5 estimate the same causal effect. If the true ratio is 0.9 in both strata and small samples gave 0.5 and 2.0, pooling is appropriate. If the true ratios are 0.5 and 2.0, pooling makes little sense. It is not always obvious whether heterogeneity is sampling variability or effect-measure modification, and finer stratification adds random variability (p. 57).

**Example (Table 4.3, outcome $Z$ = high blood pressure; assume $Z^a\perp\!\!\!\perp A|L$ and positivity; risk ratio scale)** (p. 57):

| Method | Effect computed | Risk ratio |
|---|---|---|
| Standardization / IP weighting | population | 0.8 |
| Stratification, $L=0$ | noncritical | 2.0 |
| Stratification, $L=1$ | critical | 0.5 |
| Matching (7 pairs of 4.5) | untreated | 1.0 |

All are correct (p. 58). The explanation is qualitative modification by $L$: treatment doubles risk in noncritical ($L=0$) and halves it in critical ($L=1$). The population effect (0.8) is beneficial because $\Pr[Z^{a=0}=1|L=1]/\Pr[Z^{a=0}=1|L=0]$ exceeds $2\Pr[L=0]/\Pr[L=1]$ (p. 58). The effect in the untreated is null, reflecting a larger proportion of noncritical individuals among the untreated than in the whole population (p. 58).

**Technical Point 4.3 — Marginal vs conditional risk ratios (p. 58).** The marginal risk ratio is a weighted average of the conditional ones:
$$\frac{\Pr[Y^{a=1}=1]}{\Pr[Y^{a=0}=1]}=\sum_l \frac{\Pr[Y^{a=1}=1|L=l]}{\Pr[Y^{a=0}=1|L=l]}\,w(l),$$
with $w(l)=\Pr[Y^{a=0}=1|L=l]\Pr[L=l]/\Pr[Y^{a=0}=1]$ and $\sum_l w(l)=1$. In the example the conditional ratios are 0.5 ($L=1$) and 2.0 ($L=0$). The marginal ratio is $<1$ if and only if $\Pr[Y^{a=0}=1|L=1]/\Pr[Y^{a=0}=1|L=0]>2\Pr[L=0]/\Pr[L=1]$ (p. 58).
(added step) Writing $r_l=\Pr[Y^{a=0}=1|L=l]$, $p_l=\Pr[L=l]$: marginal ratio $<1$ iff $0.5p_1r_1+2p_0r_0<p_1r_1+p_0r_0$, i.e. $p_0r_0<0.5p_1r_1$, i.e. $r_1/r_0>2p_0/p_1$. This matches the stated condition.

*Intuition note:* Different adjustment methods answer different questions about different groups, so different numbers are not a contradiction. The population ratio is a weighted average, and the weights depend on baseline risks and group sizes.

Closing lessons (pp. 58–59). The previous chapter argued a well-defined causal effect is a prerequisite for meaningful inference. This chapter adds a well-characterized target population. Both are automatic in experiments with a priori eligibility criteria, but not in observational studies, where investigators must define the effect and the subset (p. 58). An investigator using IP weighting (entire population) and one using matching (untreated) need not debate which method is superior. Their discrepancy comes from different questions, and the second could have used IP weighting for the untreated or treated (pp. 58–59). Stratification gives average effects in subsets, not individual effects, which are identifiable only under extreme assumptions (Fine Points 2.1, 3.2) (p. 59). Margin: standard regression models are a form of stratification (p. 58).

### Fine Point 4.3 — Collapsibility and the odds ratio (p. 60)
Without multiplicative modification by $V$, the population risk ratio equals the stratum-specific ratios. More generally it is a weighted average of them. If strata ratios are 2 and 3, the population ratio lies between them. This constraint is desirable for an effect measure; a measure violating it would be "odd" (p. 60).

Example (Table 4.4): effect of moving to high altitude $A$ on depression $Y$, 20 people, $V=1$ women; randomized, so $Y^a\perp\!\!\!\perp A$ (p. 60).

| | Risk ratio | Odds ratio |
|---|---|---|
| Population | 2.3 | 5.4 |
| Men ($V=0$) | 2 | 6 |
| Women ($V=1$) | 3 | 6 |

The population risk ratio lies between 2 and 3. The population odds ratio 5.4 is closer to the null than both stratum odds ratios (6). This can happen when $V$ is an independent risk factor for $Y$ and $A$ is independent of $V$ (p. 60). An effect measure is **collapsible** when the population measure is a weighted average of stratum measures. Risk ratio and risk difference are collapsible in follow-up studies, but the odds ratio (and odds difference) is not. This is a special case of Jensen's inequality (p. 60). The odds ratio is collapsible under the sharp null, and approximately collapsible (and close to the risk ratio) when the outcome is rare (say $<10\%$) in every stratum (p. 60). Consequence: one cannot equate "lack of exchangeability" with "change in the conditional odds ratio compared with the unconditional". Here the change was about 10% ($1-6/5.4$) although treated and untreated were exchangeable (p. 60).

## Toy example (ours, not from the text)
Take two strata, women ($V=1$) and men ($V=0$). Risks if everyone were treated / untreated: women 0.6 / 0.4, men 0.3 / 0.5. Stratum risk differences: women $0.6-0.4=+0.2$, men $0.3-0.5=-0.2$. This is qualitative modification.

- Population with 50% women: $\Pr[Y^{a=1}=1]=0.5(0.6)+0.5(0.3)=0.45$; $\Pr[Y^{a=0}=1]=0.5(0.4)+0.5(0.5)=0.45$. Risk difference $0$.
- Population with 80% women: $\Pr[Y^{a=1}=1]=0.8(0.6)+0.2(0.3)=0.48+0.06=0.54$; $\Pr[Y^{a=0}=1]=0.8(0.4)+0.2(0.5)=0.32+0.10=0.42$. Risk difference $0.12$, risk ratio $0.54/0.42\approx1.29$.

Same stratum effects, different population effects. The average effect depends on the mix of modifiers.

## Concepts
- [[effect-modification]] (new) — average causal effect varies across levels of a pre-treatment $V$; depends on the effect measure (p. 48)
- [[qualitative-effect-modification]] (new) — stratum effects in opposite directions; then additive and multiplicative modification imply each other (p. 48)
- [[surrogate-vs-causal-effect-modifier]] (new) — $V$ may only mark the true modifier (nationality vs quality of care) (p. 50)
- [[stratification]] (new) — computing the effect within each level of a variable; restriction is stratification applied to only some strata (pp. 49, 55)
- [[assignment-mechanism-ignorability]] — conditional exchangeability $Y^a\perp\!\!\!\perp A|L$ used to give causal meaning to stratum-specific and matched comparisons; partial exchangeability suffices for effects in the treated or untreated (pp. 52, 55)
- [[effect-in-the-treated]] (new) — causal contrast in $A=1$: $\Pr[Y=1|A=1]$ vs $\Pr[Y^{a=0}=1|A=1]$; ratio is the SMR (p. 50)
- [[transportability]] (new) — extrapolating effects to another population; depends on modifiers, treatment definition, interference (pp. 52, 54)
- [[matching-adjustment]] (new) — selecting treated and untreated with the same distribution of $L$; ensures positivity in the matched set (p. 56)
- [[positivity]] (new) — both treatment levels occur in each stratum used; needed by all four methods in the relevant subset (pp. 55, 57)
- [[collapsibility]] (new) — population measure is a weighted average of stratum measures; true for risk ratio and difference, not the odds ratio (p. 60)
- [[partial-pooling-shrinkage]] — here only pooled stratum-specific estimates (Mantel-Haenszel etc.) to reduce variance if there is no modification (p. 57)
- [[sutva]] — interference is mentioned as a reason effects differ across populations (p. 54)

## Canonical instances
- [[zeus-family-transplant-by-sex]] — Table 4.1: null population effect, opposite-sign effects in women and men (pp. 47–48)
- [[greek-roman-transplant-conditional-randomization]] — 40 people; Greek ratio 1, Roman ratio 2; nationality as surrogate modifier (pp. 49–50)
- [[transplant-high-blood-pressure-four-estimates]] — Table 4.3: 0.8, 2.0, 0.5, 1.0 from four methods (pp. 57–58)
- [[altitude-depression-odds-ratio-noncollapsibility]] — Table 4.4: risk ratio 2.3, odds ratio 5.4 vs 6 and 6 (p. 60)
- [[parachute-transportability]] — Smith and Pell: no major modifiers found (p. 52)

## Bridges (candidates)
- [structural-analogy] Pooling stratum-specific effects with variance-reducing weights ↔ bayesian: partial pooling/shrinkage in hierarchical models — both combine group estimates to reduce noise, but the text uses fixed-weight averages, not a prior.
- [structural-analogy] Marginal effect = weighted average of conditional effects with weights $w(l)$ ↔ bayesian: posterior predictive averaging over parameter uncertainty — both marginalize over a distribution.
- [structural-analogy] Reweighting four stratum effects to a new population's mix (Fine Point 4.2) ↔ bayesian: post-stratification in multilevel models — both rebuild a population quantity from group estimates and group sizes.
- [metaphor] "Transportability depends on unmeasured modifiers" ↔ bayesian: prior-sensitivity of out-of-sample prediction.

## Questions this raises
- How should one decide whether differing stratum estimates reflect true modification or sampling noise, especially under finer stratification (Technical Point 4.2)?
- The author says additive modification is the appropriate scale for identifying who benefits most (several cited authors call it the one of interest for public health). What changes if costs differ across strata?
- If $V$ is only a surrogate modifier, how can the true causal modifier be identified? (The next chapter promises "interaction".)
- How do transportability methods that reweight strata work when unmeasured modifiers differ (Fine Point 4.2 cites a "growing literature")?

## Reading notes
- Printed page = pdf page − 9 (labels give printed numbers; used throughout).
- Unit metadata says the PDF is an online revision dated 2026-08-19, not the 2020 print, and chapter numbering may differ. These pages show no edition line.
- Page 53 (second example) says treatment "reduces the risk of the outcome by 10%". The numbers on p. 48 (0.8→0.9, 0.1→0.2) show risk increases by 0.1 (ten percentage points). The words "reduces" and "10%" look inconsistent with the data; I followed the numbers.
- Page 57 contains a typo ("wish to obtaining"). The text layer of Technical Point 4.3 and some page-58 equations was garbled; I checked them against the page image.
- I checked the Table 4.3, 4.4 and Fine Point 4.3 numbers against the printed tables and they match.
- Page 59 has only a few lines (end of 4.6). The unit contains no exercises.
