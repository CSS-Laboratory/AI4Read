---
id: hernan-2020-whatif/ch08-selection
work: hernan-2020-whatif
unit: "8 Selection bias"
pages: 109-124
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Selection bias

## L0 — One line
Selection bias is a treatment–outcome association that can appear when the analysis is restricted by conditioning on a common effect of two variables (one tied to treatment, one to outcome), and it can arise even in a randomized trial if the selection happens after randomization.

## L1 — The gist (≤ 120 words)
Confounding comes from common causes. Which other mechanism can make treated and untreated people non-comparable? The chapter's answer is selection bias: bias from conditioning on a common effect (collider) of two variables, one linked to treatment and one to outcome. Examples are loss to follow-up, volunteer bias, healthy-worker bias and case-control sampling. Randomization protects against confounding, but not against selection that occurs after randomization. If exchangeability, positivity and consistency hold for censoring, inverse-probability weighting can remove the bias, while stratification may fail. Conditioning on a collider does not always produce selection bias.

**Prerequisites:** causal DAGs and d-separation (conditioning on a collider opens a path; conditioning on a non-collider blocks it); counterfactual notation $Y^a$; risk ratio; conditional probability; the idea of weighting counts. Terms used in L1–L2: *exchangeability* (treated and untreated groups are comparable; not formally defined in this unit); *censoring* (loss to follow-up before the outcome is seen); *stratification* (estimating the effect within levels of a covariate $L$); *positivity* (a nonzero probability of being uncensored in every stratum); *consistency* (the intervention that removes censoring is well defined); *hazard ratio* (ratio of death rates among those still alive at a given time).

## L2 — Key ideas
- **Definition.** Selection bias is an association created by how individuals are selected into the analysis. Unlike confounding, it needs no common cause of treatment and outcome, and it can occur in randomized and observational studies (p. 109).
- **Structure.** Restricting the analysis (conditioning) on a common effect of two variables opens a non-causal path between them. One variable must be the treatment or a cause of it, the other the outcome or a cause of it (p. 111). Bias of this kind can arise even when treatment has no effect on the outcome ("under the null") (pp. 109–110).
- **Many names, one structure.** Informative censoring, missing data, healthy-worker bias, volunteer bias, pre-study treatment and case-control sampling all fit this structure (pp. 111–112).
- **Randomization.** It does not protect against selection after assignment, such as loss to follow-up. It does protect against selection into the study before assignment (p. 113).
- **Why classify.** Structural labels guide analysis, design, and understanding of why a variable is a "confounder" in one study but not another (p. 115).
- **Hazard ratios.** Time-specific hazard ratios condition on earlier survival, so they carry built-in selection bias (p. 114).
- **Censoring as a treatment.** Censoring can be treated as another treatment. Inverse-probability (IP) weighting then builds a pseudo-population with nobody censored. It needs exchangeability, positivity and consistency for censoring (pp. 117–120).
- **Stratification can fail.** It fails under some structures (Figures 8.4 and 8.6) where IP weighting still works (p. 120).
- **Selection without bias.** Collider conditioning always induces some association, but it may be absent in one level of the collider (p. 122).

## L3 — Walkthrough

### Introduction (p. 109)
**Example.** A randomized experiment asks whether an investigator's looking up at the sky makes pedestrians look up (p. 109). Only pedestrians who later consented to data use are analysed. Shy pedestrians, and pedestrians who felt tricked because the investigator looked up, were less likely to consent (p. 109). So among participants, those in front of whom she looked up are less likely to be shy, hence more likely to look up themselves (p. 109). The selection process then guarantees an association, whatever the true effect (p. 109).

**Definition.** Selection bias is an association created by the process that selects individuals into the analysis. It is not due to common causes of treatment and outcome, and it can arise in randomized experiments and observational studies. It is a form of lack of exchangeability between the treated and the untreated (p. 109). (Exchangeability is not formally defined in this unit.)

### 8.1 The structure of selection bias (pp. 109–111)
**Selection bias under the null** means bias that would arise even if treatment had a null effect (no effect) on the outcome (p. 109).

**Figure 8.1.** The arrows are $A\to Y$, $A\to C$ and $Y\to C$. $A$ is folic acid supplementation, $Y$ is cardiac malformation and $C$ is death before birth. Malformation raises mortality. Supplements lower mortality by preventing non-cardiac malformations. The study includes only survivors, $C=0$, which is the box around $C$ (p. 109).

Two sources of $A$–$Y$ association are open (p. 109):
1. the path $A\to Y$, the causal effect;
2. the path $A\to C\leftarrow Y$, open because $C$ (a common effect, or collider) is conditioned on.

Hence the associational risk ratio does not equal the causal risk ratio (pp. 109–110):
$$\frac{\Pr[Y=1\mid A=1,C=0]}{\Pr[Y=1\mid A=0,C=0]}\neq\frac{\Pr[Y^{a=1}=1]}{\Pr[Y^{a=0}=1]}.$$
Without conditioning on $C$, the only open path is $A\to Y$, and the associational and causal risk ratios would be equal (p. 110).

**Figure 8.2** adds $S$, parental grief, affected by $C$. Restricting to non-grieving parents, $S=0$, conditions on a variable affected by the collider and also opens $A\to C\leftarrow Y$ (p. 110).

In both figures the bias arises whether or not there is an arrow $A\to Y$. Structures that give bias under the null also give bias when the effect is non-null (p. 110). Selection bias under the null is defined more generally by Figures 8.3–8.6 (p. 110).

**Figure 8.3.** The study follows HIV patients to estimate the effect of treatment $A$ on 3-year death $Y$; there is no arrow $A\to Y$ (p. 110).
- $U$ is unmeasured immunosuppression and raises the risk of death.
- $L$ (symptoms, CD4 count, viral load) mediates the effect of $U$ on censoring $C$.
- Treatment causes side effects that may lead to dropout, which is the arrow $A\to C$.
- The analysis is restricted to the uncensored, $C=0$ (p. 110).

By d-separation, conditioning on $C$ opens $A\to C\leftarrow L\leftarrow U\to Y$. So the associational risk ratio is not 1 although the causal risk ratio is 1 (p. 110).

*Intuition for the bias (p. 110):* a treated person with side effects who did not drop out probably lacked a second cause of dropout such as $U=1$. So $A$ and $U$ are inversely associated among the uncensored. Because $U$ is positively associated with $Y$, an inverse $A$–$Y$ association is induced (pp. 110–111).

Figure 8.3 is a transformation of Figure 8.1. The $Y$–$C$ association now arises from $U$, a common cause of $Y$ and $C$ (p. 110). The conditioned collider is a common effect of $A$ and a cause $U$ of $Y$ (p. 111).

**Figures 8.4–8.6** (p. 111):
- In Figure 8.4, $A$ has a direct effect on symptoms $L$. Restricting to the uncensored conditions on the common effect $C$ of $A$ and $U$.
- Figures 8.5 and 8.6 are variants of 8.3 and 8.4 with a common cause $W$ of $A$ and another variable. $W$ is unmeasured lifestyle, personality or education. It affects attendance at visits ($W\to C$, Fig. 8.5) or the threshold for reporting symptoms ($W\to L$, Fig. 8.6). These are examples of M-bias.

**Working definition.** The book uses "selection bias" for all biases from conditioning on a common effect of two variables. One of them is the treatment or a cause of treatment; the other is the outcome or a cause of the outcome (p. 111).

> **Intuition note.** Looking only at people who passed a filter can link two things that were unrelated before the filter, if both influence passing it. The link needs no real effect of treatment on outcome.

### 8.2 Examples of selection bias (pp. 111–113)
All follow the structure above (p. 111):
- **Differential loss to follow-up** (informative censoring): the bias of Figures 8.3–8.6.
- **Missing data / nonresponse bias**: $C$ can mean missing outcome data for any reason. Restricting to complete data ($C=0$) may cause bias.
- **Healthy worker bias**: $A$ is occupational exposure, $Y$ is death, $U$ is unmeasured true health, and $C$ is not being at work ($C=1$: no). The study is restricted to those at work. Exposure reduces the chance of being at work, directly (Figs. 8.3, 8.4) or via a common cause $W$, such as exposed jobs being eliminated (Figs. 8.5, 8.6) (pp. 111–112).
- **Self-selection / volunteer bias**: $C$ is agreement to participate, $A$ is smoking, $Y$ is coronary heart disease, $U$ is family history, $W$ is healthy lifestyle, and $L$ is a mediator such as awareness (p. 112). Bias may be present if the study is restricted to volunteers.
- **Selection affected by treatment received before study entry**: if pre-study treatment affects selection into the study, bias is expected. It is a generalization of self-selection. Unmeasured confounding of the pre-study part of treatment may also exist if confounders were measured only during the study (p. 112).

**Fine Point 8.1 — case-control studies (p. 112).** Figure 8.1 is used.
- $A$ is postmenopausal estrogen, $Y$ is coronary heart disease, and $C$ is selection into the study (1: no, 0: yes).
- $Y\to C$: cases are more likely selected than non-cases, the defining feature of case-control studies.
- Here controls are chosen preferentially among women with hip fracture. Estrogen protects against hip fracture, so $A$ now affects $C$.
- The odds ratio is by definition conditional on $C=0$. Among the selected, controls are more likely than cases to have had a hip fracture. A control is therefore less likely than a case to be on estrogen, so the $A$–$Y$ odds ratio given $C=0$ would be greater than the causal odds ratio.

**Where selection bias occurs (p. 113).** It may occur in retrospective studies (treatment data collected after the outcome) and prospective studies (before the outcome). It may occur in observational studies and randomized experiments (p. 113).

**Randomized experiments (p. 113).** Figures 8.3 and 8.4 can depict a randomized experiment, since there are no common causes of $A$ and any other variable. If people are lost before the outcome is ascertained, $\Pr[Y=1\mid A=a]$ cannot be computed. Only $\Pr[Y=1\mid A=a,C=0]$ can, and the uncensored may not be exchangeable with the lost.
- **Key difference:** randomization protects against confounding, but not against selection bias when selection occurs after randomization.
- Selection into the study before treatment is assigned causes no bias. Trials enrol volunteers but are not affected by volunteer bias, because assignment occurs after agreement.
- Figures 8.3 and 8.4 cannot represent this, since treatment cannot cause agreement to participate. Figures 8.5 and 8.6 cannot, since randomization means no common cause of treatment and anything else.

### 8.3 Selection bias and confounding (pp. 113–115)
Two reasons treated and untreated may not be exchangeable (p. 113):
1. common causes of treatment and outcome, called **confounding**;
2. conditioning on common effects of treatment and outcome (or causes of them), called **selection bias**.

This structural classification may not match the terminology of some disciplines. Statisticians and econometricians often call both "selection bias" (selection into the analysis, or into a treatment). The authors say they do not aim to be normative about terms (p. 113).

**Firefighters example (Figure 8.7; pp. 113–114).** The study is restricted to firefighters ($C=0$) to estimate the effect of physical activity $A$ on heart disease $Y$. Suppose $A$ does not cause $Y$.
- $L$ is parental socioeconomic status. It affects becoming a firefighter $C$ and, via childhood diet, $Y$.
- $U$ is unmeasured attraction to physical activity. It affects $C$ and $A$.
- $U$ does not affect $Y$, and $L$ does not affect $A$.

There are no common causes of $A$ and $Y$, so there is no confounding. In the whole population the associational risk ratio is expected to equal the causal risk ratio, which is 1. Within firefighters, conditioning on the common effect $C$ of a cause of treatment and a cause of outcome induces selection bias, and the two ratios differ (p. 114). Investigators must adjust for $L$ whatever the name. A structural classification does not always change the analysis (pp. 114–115). Many epidemiologists therefore call any variable needing adjustment a "confounder" (p. 115).

**Advantages of the structural view (p. 115):**
1. Structure guides the methods. In longitudinal studies with time-varying treatments, it detects cases where stratification for confounding would introduce selection bias. g-methods are then a better alternative (Part III).
2. It helps design. Firefighter studies should collect joint risk factors for $Y$ and $C$.
3. Selection on a pre-treatment variable (being a firefighter) could explain why a variable behaves as a confounder in some studies but not others. $L$ would not necessarily need adjustment in studies not restricted to firefighters.
4. It improves communication.

**Healthy worker bias, two meanings (p. 115).** One is the selection bias above (Figs. 8.3–8.6). The other compares workers with the general population. It is drawn as Figure 7.1 with $L$ (health) $\to A$ (worker group) and $L\to Y$. That is a common cause, so it is confounding.

Margin note: the so-called Simpson's paradox resulted from ignoring the difference between common causes and common effects. Blyth (1972) misrepresented it as an extreme case of confounding (p. 115).

Some paths opened by a collider may be weak and induce little bias. Selection bias is not "all or nothing", so direction and magnitude matter (Fine Point 8.2) (p. 115).

> **Intuition note.** The two biases are different causal structures (common cause versus common effect), yet both leave the treated and untreated non-comparable. The name matters less for the adjustment than for choosing methods and designs.

### Technical Point 8.1 — built-in selection bias of hazard ratios (p. 114)
**Setup (Figure 8.8).** A randomized experiment studies heart transplant $A$ and death at time 1 ($Y_1$) and time 2 ($Y_2$). Arrows: $A\to Y_1$, $U\to Y_1$, $U\to Y_2$, $Y_1\to Y_2$. There is no arrow $A\to Y_2$. $U$ is an unmeasured haplotype that lowers the risk of death at all times. $Y_1$ is boxed (conditioned on) (p. 114).

**Risk ratios.** With no confounding, these are unbiased measures of the effect of $A$ on death by times 1 and 2:
$$aRR_{AY_1}=\frac{\Pr[Y_1=1\mid A=1]}{\Pr[Y_1=1\mid A=0]},\qquad aRR_{AY_2}=\frac{\Pr[Y_2=1\mid A=1]}{\Pr[Y_2=1\mid A=0]}.$$
$aRR_{AY_2}$ is below 1, although $A$ has no direct effect on $Y_2$, because it measures the effect on total mortality through time 2 (p. 114).

**Hazard ratios.** The hazard at time 2 is the probability of dying at time 2 among those who survived past time 1. In discrete time the time-1 hazard ratio equals $aRR_{AY_1}$, and the time-2 hazard ratio is
$$aRR_{AY_2\mid Y_1=0}=\frac{\Pr[Y_2=1\mid A=1,Y_1=0]}{\Pr[Y_2=1\mid A=0,Y_1=0]}.$$
Treated survivors of time 1 are less likely than untreated survivors to have the protective $U$ (treatment can explain their survival). They are therefore more likely to die at time 2. So the hazard ratio is below 1 at time 1 and above 1 at time 2: the hazards have crossed (p. 114).

The time-2 hazard ratio is a biased estimate of the direct effect. The cause is selection bias from conditioning on the common effect $Y_1$ of $A$ and $U$, which opens $A\to Y_1\leftarrow U\to Y_2$. An unmeasured cause of death marginally unassociated with treatment, like $U$, is often called a frailty (p. 114).

Within each stratum of $U$, the conditional hazard ratio $aRR_{AY_2\mid Y_1=0,U}$ is 1, because conditioning on the non-collider $U$ blocks the path. That it differs from the unconditional ratio although $U$ is independent of $A$ shows noncollapsibility of the hazard ratio (p. 114). The conditional ratio cannot be computed because $U$ is unobserved. The data cannot say whether the true DAG is Figure 8.8 or Figure 8.9 (which has an arrow $A\to Y_2$). All this applies to observational studies and randomized experiments (p. 114).

> **Intuition note.** At time 2 only time-1 survivors are compared. Treated survivors owe part of their survival to treatment, so fewer of them needed the protective trait, and they die more often later. This pushes the time-2 hazard ratio above 1, so the hazards cross although there is no direct effect.

### 8.4 Selection bias and censoring (pp. 115–117)
**Wasabi trial (pp. 115–116).** The 60 participants are marginally randomized, half to wasabi ($A=1$), half not. In each group 17 died within a year, so the associational risk ratio is 1, and the causal risk ratio is expected to be 1 by randomization. (Imagine 60 million patients if random variability bothers you.) Many patients were censored (lost to follow-up). Censoring was more frequent among those with heart disease ($L=1$) and those on wasabi.
- Uncensored: 9 in the wasabi group, 22 in the other.
- Observed deaths: 4 and 11.
- Risk ratio among the uncensored: $(4/9)/(11/22)=0.89\neq 1$. This is selection bias from conditioning on the common effect $C$ (p. 116).

**Diagram.** Figure 8.3 depicts the trial, with $U$ now atherosclerosis, which affects heart disease $L$ and death $Y$ (p. 116). There is no common cause of $A$ and $Y$, so no adjustment for confounding is needed for the effect of $A$. There is a backdoor path $C\leftarrow L\leftarrow U\to Y$. To estimate the (null) effect of censoring $C$ on $Y$, one would have to adjust for confounding, which the measured $L$ can do by blocking that path (p. 116).

**Modified contrast.** The usual contrast does not involve $C$. Because selection bias would not exist if everybody were uncensored, the authors use counterfactuals $Y^{a,c=0}$, the outcome under treatment $a$ and no censoring. The contrast is
$$\Pr[Y^{a=1,c=0}=1]\ \text{versus}\ \Pr[Y^{a=0,c=0}=1].$$
Using $Y^{a,c=0}$ implies a belief in no-direct-effect interventions that can set $C$ to 0 (margin note) (p. 116).

Often it is reasonable to assume that censoring has no causal effect on the outcome, but omitting the superscript $c=0$ would hide that confounding for $C$ becomes central. With $Y^{a,c=0}$, censoring is just another treatment, and the goal is the effect of a joint intervention on $A$ and $C$. To eliminate selection bias for $A$, we need to adjust for confounding for the effect of $C$ (p. 117).

So we need (i) exchangeability, positivity and consistency to hold for $C$ as well as $A$, and (ii) the same analytic methods as for estimating the effect of $C$. Under these conditions and methods, selection bias can be eliminated. In the absence of measurement error and confounding, the effect of $A$ on $Y$ can be identified (p. 117).

### 8.5 How to adjust for selection bias (pp. 117–120)
Selection bias can sometimes be avoided by design, but often it cannot (loss to follow-up, self-selection, missing data) (p. 117). Correction can sometimes be done by IP weighting (or standardization). Each selected individual ($C=0$) gets weight
$$W^C=\frac{1}{\Pr[C=0\mid L,A]},$$
so she stands for herself and for those with the same $L$ and $A$ who were not selected (p. 117). Margin note: with both confounding and selection bias, the product $W^AW^C$ can adjust for both under assumptions given in Chapter 12 and Part III, with $W^A=1/f(A|L)$ (p. 117).

**Tree for the wasabi trial (Figure 8.10, p. 118).** Numbers read from the figure (pp. 117–118):

| $L$ | $A$ | $n$ | uncensored $C=0$ ($n$, prob.) | deaths among $C=0$ | censored $C=1$ | deaths among $C=1$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 10 | 10 (1) | 2 | 0 | 0 |
| 0 | 1 | 10 | 5 (.5) | 1 | 5 | 1 |
| 1 | 0 | 20 | 12 (.6) | 9 | 8 | 6 |
| 1 | 1 | 20 | 4 (.2) | 3 | 16 | 12 |

- 40 had heart disease and 20 did not. Everyone had a 50/50 chance of $A=1$, so there is no arrow $L\to A$ (p. 117).
- The deaths among the censored are shown only to document Figure 8.3's independencies: $A$ is marginally independent of $Y$, and $C$ is independent of $Y$ within levels of $L$. In real life they are unknown (p. 117).
- The risk ratio in the whole population is 1; in the uncensored it is 0.89 (p. 117).

**Weighting (p. 118).** Take the $L=1,A=1$ branch: 4 of 20 uncensored, $\Pr[C=0\mid L=1,A=1]=4/20=0.2$. The 16 censored get weight 0. The 4 uncensored get weight $1/0.2=5$, so the 20 individuals are replaced by 5 copies of each of the 4. Repeating this for all branches builds a **pseudo-population**: a reweighted copy of the study population of the same size, in which nobody is lost to follow-up (Figure 8.11, p. 119). Its associational risk ratio is 1, the same as $\Pr[Y^{a=1,c=0}=1]/\Pr[Y^{a=0,c=0}=1]$ (p. 118).

*(added step)* Weights for the other branches follow from the table: $1/1=1$ for $L=0,A=0$; $1/0.5=2$ for $L=0,A=1$; $1/0.6=5/3$ for $L=1,A=0$. Weighted death counts are 2, 2, $9\times5/3=15$ and $3\times5=15$ out of 10, 10, 20 and 20. Risk with $A=1$ is $(2+15)/30=17/30$, and with $A=0$ it is $(2+15)/30=17/30$, so the ratio is 1. Figure 8.11 shows these counts.

**Three identifiability conditions** (the pseudo-population association equals the effect in the original population if they hold; pp. 119–120):
1. **Exchangeability.** The average outcome among the uncensored must equal that among the censored with the same $A$ and $L$. This holds if the selection probability is conditioned on $A$ and on all further factors predicting both selection and outcome, that is, if $A$ and $L$ block all backdoor paths between $C$ and $Y$. This is untestable (p. 119).
2. **Positivity** (in the source's words, all conditional probabilities of being uncensored given $A$ and $L$ must be greater than zero). All $\Pr[C=0\mid A,L]$ must be greater than zero. It is required for being uncensored, not for being censored. Figure 8.10 has $\Pr[C=1\mid L=0,A=0]=0$, which does not matter (pp. 119–120).
3. **Consistency**, including sufficiently well-defined interventions. The pseudo-population has censoring abolished, so its effect measure is the one that would apply had nobody been censored. This may be well defined for loss to follow-up or nonresponse. It is not when censoring is a **competing event** (an event, such as death, that prevents the outcome of interest). For Alzheimer's disease, death from other causes is one. Treating it as censoring is problematic, since it is unclear what intervention would remove all other causes of death, and no feasible intervention removes just one cause without affecting others (p. 120).

**Stratification (p. 120).** One could stratify on $L$ instead of weighting. In Figure 8.3, conditioning on $L$ blocks the backdoor path $C$ to $Y$, so the conditional risk ratio $\Pr[Y=1|A=1,C=0,L=l]/\Pr[Y=1|A=0,C=0,L=l]$ can be read as the effect among the uncensored with $L=l$. Under the null, stratification would also work in Figure 8.5. It would not work in Figures 8.4 and 8.6: conditioning on $L$ opens $A\to L\leftarrow U\to Y$, since $L$ is a collider there. Even if the effect of $A$ is null, the conditional risk ratio would generally differ from 1 (p. 120). IP weighting adjusts appropriately in Figures 8.3–8.6, because it estimates unconditional effect measures after reweighting by treatment and $L$ (p. 120). This is the first time stratification cannot validly give the causal effect although exchangeability, positivity and consistency hold. Part III has similar cases for time-varying treatments (p. 120).

> **Intuition note.** Weighting lets each uncensored person count for the similar people who dropped out. The reweighted group looks as if no one had dropped out. This works only to the extent that $L$ and $A$ capture everything linking dropout to outcome, which cannot be tested.

### 8.6 Selection without bias (pp. 121–122)
**Figure 8.12.** $A$ (surgery) $\to Y\leftarrow E$ (genetic haplotype), $Y$ death. By d-separation, $A$ and $E$ are marginally independent but associated given $Y$ (p. 121). Conditioning on the common effect of two independent causes always induces a conditional association in at least one stratum of $Y$ (say $Y=1$). There is a special situation in which they stay independent in the other stratum (p. 121).

**Setup (Figure 8.13).** Suppose $A$ and $E$ affect survival through totally independent mechanisms, so that $E$ cannot modify the effect of $A$ on $Y$ and vice versa. For example, surgery acts by removing a tumor and the haplotype by raising cholesterol and heart-attack risk. Define cause-specific death $Y_A$ (tumor), $Y_E$ (heart attack) and $Y_O$ (other causes). $Y=1$ if any of them is 1, and $Y=0$ if all are 0. $Y_A,Y_E,Y_O$ are not recorded (p. 121).

**Result under this setup.**
- The arrows into $Y$ are deterministic. Conditioning on $Y=0$ is the same as conditioning on $Y_A=Y_E=Y_O=0$. These are non-colliders and block the path, so $A$ and $E$ are independent given $Y=0$ (p. 121).
- $Y=1$ is compatible with 7 combinations of $(Y_A,Y_E,Y_O)$ (listed on p. 121) and fixes none. The path stays open, so $A$ and $E$ are associated given $Y=1$ (p. 121).

**Cases that break this** (A and E dependent within both strata of $Y$; p. 121):
- a shared mechanism, with an arrow $A\to Y_E$ or $E\to Y_A$ (Fig. 8.14);
- a common cause $V$ of $Y_A$ and $Y_E$ (Fig. 8.15);
- common causes $W_1,W_2$ linking $Y_A$ with $Y_O$ and $Y_E$ with $Y_O$ (Fig. 8.16).

Data summarized by Figure 8.13 follow a **multiplicative survival model** (p. 121). The model is defined in the next paragraph.

**Technical Point 8.2 (p. 122).** A multiplicative survival model holds when
$$\Pr[Y=0\mid E=e,A=a]=g(e)h(a).$$
This is equivalent to the survival ratio $\Pr[Y=0|E=e,A=a]/\Pr[Y=0|E=e,A=0]$ not depending on $e$ and equalling $h(a)$. It means no interaction between $A$ and $E$ for $Y=0$ on the multiplicative scale. For Figure 8.13:
$$\Pr[Y=0\mid E=e,A=a]=\Pr[Y_O=0,Y_A=0,Y_E=0\mid E=e,A=a]=\Pr[Y_O=0]\Pr[Y_A=0\mid A=a]\Pr[Y_E=0\mid E=e].$$
The first equality is by determinism, the second by DAG factorization. Set $g(e)=\Pr[Y_E=0|E=e]$ and $h(a)=\Pr[Y_O=0]\Pr[Y_A=0|A=a]$. Then $\Pr[Y=1|E=e,A=a]=1-g(e)h(a)$ does not follow a multiplicative mortality model. Hence, when $A$ and $E$ are conditionally independent given $Y=0$, they are conditionally dependent given $Y=1$ (p. 122).

**Augmented causal DAG (p. 122).** Adding $Y_A,Y_E,Y_O$ yields a diagram that represents both the independence given $Y=0$ and the dependence given $Y=1$.

**Conclusion (p. 122).** Conditioning on a collider always induces an association between its causes, but it may be restricted to certain levels of the common effect. So it is theoretically possible that restricting to one level of a common effect causes no selection bias. "Collider stratification is not always a source of selection bias." (p. 122)

> **Intuition note.** In the independent-mechanisms setup of Figure 8.13, being alive means every possible cause of death failed to act, which leaves nothing to link $A$ and $E$. Death can come from several combinations of causes, so knowing death links $A$ and $E$.

### Fine Point 8.2 — strength and direction (p. 123)
- The direction of the association between independent causes $A$ and $E$ within strata of a common effect $Y$ depends on how they interact to cause $Y$.
- **"Or" mechanism.** With an undiscovered background factor $U$ unassociated with $A$ and $E$, either $A=1$ or $E=1$ is sufficient and necessary for death, and neither causes death without $U$. Then among those who died, $A$ and $E$ are negatively associated. $\log OR_{AE|Y=1}$ approaches $-\infty$ as the prevalence of $U$ approaches 1.
- **"And" mechanism.** If both $A=1$ and $E=1$ are required (with $U$), they are positively associated among the dead.
- A standard DAG like Figure 8.12 cannot tell "or" from "and". Causal DAGs with sufficient-cause structures can.
- Biases too small to affect conclusions may be ignored. Generally, a large selection bias requires strong associations between the collider and both treatment and outcome. Greenland (2003) studied the magnitude under the null ("collider-stratification bias").

## Toy example (ours, not from the text)
Let $A$ and $Y$ be independent, with no causal effect of $A$ on $Y$. In a population of 400, 100 people fall in each combination $(A,Y)$: (0,0), (0,1), (1,0), (1,1). Suppose only people with $A=1$ or $Y=1$ are selected, so $C=0$ means selected (as in the chapter) and $C=1$ means not selected. This is a common effect of $A$ and $Y$.
- Whole population: $\Pr[Y=1|A=1]=100/200=0.5$ and $\Pr[Y=1|A=0]=100/200=0.5$, so the risk ratio is 1.
- Selected only: $A=1$ gives $(1,0)$ and $(1,1)$, so 200 people with 100 having $Y=1$, risk 0.5. $A=0$ gives only $(0,1)$, so 100 people, all $Y=1$, risk 1.
- Risk ratio among the selected: $0.5/1=0.5\neq1$.

Selection created an inverse association from nothing. This matches the "or" mechanism of Fine Point 8.2.

## Concepts
- [[selection-bias]] (new) — association from conditioning on a common effect of two variables, one the treatment or its cause, the other the outcome or its cause (p. 111).
- [[selection-bias-under-the-null]] (new) — selection bias that would arise even if treatment had no effect on the outcome (p. 109).
- [[fork-chain-collider]] — a collider is a common effect; conditioning on it (or a descendant, Fig. 8.2) opens a path (pp. 109–110).
- [[d-separation]] — the rule used to read which paths conditioning opens or blocks (pp. 110, 121).
- [[confounding-vs-selection-bias]] — common causes versus common effects; both leave treated and untreated non-exchangeable (p. 113).
- [[exchangeability]] — property of treated and untreated groups whose lack results from confounding or selection bias; not formally defined in this unit (p. 113).
- [[censoring]] (new) — loss to follow-up before the outcome is observed ($C=1$); the analysis then uses the uncensored (p. 113).
- [[ip-weighting]] (new) — weight each selected person by $1/\Pr[C=0|L,A]$ so she stands for similar unselected people (p. 117).
- [[pseudo-population]] (new) — reweighted copy of the population in which nobody is censored (p. 118).
- [[positivity]] (new) — needed for being uncensored: $\Pr[C=0|A,L]>0$ in all strata (p. 119).
- [[consistency]] (new) — the intervention "abolish censoring" must be well defined; problematic for competing events (p. 120).
- [[competing-event]] (new) — event that prevents the outcome of interest, such as death (p. 120).
- [[hazard-ratio-selection-bias]] (new) — time-specific hazard ratios condition on earlier survival, a collider (p. 114).
- [[multiplicative-survival-model]] (new) — $\Pr[Y=0|E,A]=g(e)h(a)$; holds for Figure 8.13 (p. 122).
- [[augmented-causal-dag]] (new) — DAG with added deterministic cause-specific variables (p. 122).
- [[m-bias]] (new) — selection bias structures of Figures 8.5–8.6, as named in the margin (p. 111).
- [[simpsons-paradox]] — margin note: result of ignoring common cause versus common effect (p. 115).
- [[potential-outcomes]] — counterfactual $Y^{a,c=0}$ for the contrast with censoring removed (p. 116).

## Canonical instances
- [[pedestrians-looking-up]] — selection of consenting pedestrians after randomization (p. 109).
- [[folic-acid-fetal-death]] — conditioning on survival to birth (Fig. 8.1) (p. 109).
- [[hiv-censoring-study]] — informative censoring, Figures 8.3–8.6 (p. 110).
- [[estrogen-case-control-hip-fracture]] — inappropriate control selection (p. 112).
- [[firefighters-physical-activity]] — selection on a pre-treatment variable without confounding (p. 113).
- [[heart-transplant-hazard-ratio]] — crossing hazards through conditioning on survival (p. 114).
- [[wasabi-trial]] — worked IP-weighting example, risk ratio 0.89 versus 1 (pp. 116–119).
- [[surgery-haplotype-death]] — selection without bias in one stratum (p. 121).

## Bridges (candidates)
- [structural-analogy] Collider conditioning inducing association ↔ Bayesian inference: observing a shared effect makes independent causes dependent in the posterior.
- [structural-analogy] IP weighting by $1/\Pr[C=0|L,A]$ ↔ Monte Carlo: reweighting samples by inverse probability to mimic another distribution.
- [structural-analogy] Frailty $U$ and conditioning on survival ↔ hierarchical models: a latent trait shapes who remains in the sample.
- [structural-analogy] Missing outcome data in the censored ↔ Bayesian treatment of missing data: the unobserved outcomes must be modelled or reweighted.
- [metaphor] Selection as a filter on data ↔ Bayesian workflow: the analysis sample is itself an assumption to examine.

## Questions this raises
- How can IP weights be estimated when $\Pr[C=0|L,A]$ is unknown, and how sensitive is the result to a missed predictor of both censoring and outcome?
- When both confounding and censoring exist, how do the combined weights $W^AW^C$ work (Chapter 12, Part III)?
- How can the size of collider-stratification bias be bounded in practice (Greenland 2003)?
- What does a competing-event analysis look like, if censoring by death is conceptually ill-defined?

## Reading notes
- Source is the online revision dated 2026-08-19, not the 2020 print version. Chapter numbering may differ from older citations.
- Printed page = pdf − 9. PDF page 133 (printed 124) shows only the running head.
- The text layer was clean. I checked equations and figures against the images.
- Figures 8.14–8.16 are legible in the page image. In Figure 8.16 the arrows from $W_1$ and $W_2$ are drawn to $Y_O$ and, as far as I can see, to $A$ and $E$ respectively. The text on p. 121 describes common causes of $Y_A$ with $Y_O$ and of $Y_E$ with $Y_O$. I followed the text.
- Figure 8.3 is used for two examples: U = immunosuppression (p. 110) and U = atherosclerosis (p. 116).
- Margin note on p. 111 words the general definition slightly differently ("associated with") from the main text ("or a cause of"). I used the main text.
- Fine Point 8.2 (p. 123) says the "or" mechanism was the only explanation in the main text. The pages given do not show such an explanation explicitly. I recorded only what the Fine Point states.
- There are no exercises in this unit.
