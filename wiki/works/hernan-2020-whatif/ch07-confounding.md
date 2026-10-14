---
id: hernan-2020-whatif/ch07-confounding
work: hernan-2020-whatif
unit: "7 Confounding"
pages: 91-108
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 6
---
# Confounding (Hernán & Robins, Ch. 7)

## L0 — One line
Confounding is the bias from common causes of treatment and outcome, shown as open backdoor paths in a causal diagram; if the causal diagram is known, whether adjusting for a set of variables L removes it can be decided by the backdoor criterion (or by a SWIG), rather than by the traditional, mostly association-based rules.

## L1 — The gist (≤ 120 words)
When is "association" not "causation" in observational data, and which variables must we adjust for? The chapter defines confounding structurally: a shared cause of treatment A and outcome Y opens a backdoor path. Conditional exchangeability given L holds when L blocks all backdoor paths and contains no descendants of A. Adjusting for a collider can create bias (M-bias), so the traditional "confounder" definition, based on associations, can give harmful advice. SWIGs (single-world intervention graphs) link graphs to counterfactual independence. Adjustment methods (g-methods, stratification) all rely on unverifiable assumptions. This matters because causal claims from observational data need explicit, criticizable causal assumptions.

**Prerequisites:** causal DAGs (paths, colliders, d-separation); counterfactual notation $Y^a$; exchangeability; standardization and IP weighting (Ch. 2, 4, 6). Quick glosses: a *backdoor path* is a noncausal path between treatment and outcome that has an arrow into treatment; a *collider* on a path is a node with two arrows pointing into it; a *SWIG* is a graph that includes counterfactual variables; *g-methods* are standardization, IP weighting and g-estimation; *faithfulness* means no independencies hold beyond those the graph implies (no exact cancellations); *FFRCISTG* is Robins's causal model, which does not assume cross-world independencies; *NPSEM-IE* is a structural-equation causal model with independent errors, which does assume them; *cross-world independencies* are independencies between counterfactuals under different treatment values (see Technical Point 7.1).

## L2 — Key ideas
- **Confounding is structural.** Shared causes of A and Y create an open backdoor path, so the associational risk ratio need not equal the causal risk ratio (p. 91).
- **Backdoor criterion.** L must block all backdoor paths and contain no descendants of A. Given faithfulness (and an FFRCISTG model), conditional exchangeability $Y^a \perp\!\!\!\perp A \mid L$ holds if and only if this is satisfied (p. 93, 94).
- **Adjusting can hurt.** Conditioning on a collider (Figures 7.4, 7.7) opens a blocked path, giving selection bias. Unconditional effects can then be identified while conditional ones are not (pp. 97, 99).
- **Given a causal DAG, confounding is absolute and "confounder" is relative.** Traditional association-based confounder definitions mislead. The structural approach makes assumptions explicit and criticizable (p. 99, 100).
- **SWIGs** put counterfactual variables on the graph, so exchangeability is read off by d-separation (p. 101, 102).
- **Adjusting for a descendant of treatment** does not eliminate bias, even if that variable blocks all backdoor paths (Fine Point 7.4). What matters is graph topology, not time order (p. 103).
- **Adjustment methods** (g-methods; stratification-based) need conditional exchangeability. Alternatives (difference-in-differences, front door, proximal inference) need other unverifiable assumptions (p. 103, 104, 106, 107).
- **Criticism of observational studies** that only says the study 'may be confounded' is noninformative. It becomes informative when it cites contradicting evidence or names a specific common cause (e.g., smoking) through which a backdoor path may remain open, which gives a testable challenge. If data on that cause cannot be obtained, a sensitivity analysis is the suggested response (p. 104, 105).

## L3 — Walkthrough

### Opening (p. 91)
A pedestrian example: first pedestrian looks up, second looks up, but a thunderous noise also makes people look up, so the effect is confounded. In observational studies treatment may be determined by many factors. If those factors affect the outcome, their effects become entangled with the treatment effect. Confounding is "just a form of lack of exchangeability" between treated and untreated. Even in an arbitrarily large population, association is not causation under confounding (p. 91).

### 7.1 The structure of confounding (pp. 91–93)
- Figure 7.1: $L \to A$, $L \to Y$, $A \to Y$. There are two sources of association: the causal path $A \to Y$ and the path $A \leftarrow L \to Y$ (p. 91).
- A **backdoor path** is a noncausal path between treatment and outcome that remains even if arrows from treatment to its descendants are removed. It has an arrow pointing into treatment (margin note, p. 91).
- Without $L$, the associational risk ratio $\Pr[Y=1|A=1]/\Pr[Y=1|A=0]$ would equal the causal risk ratio $\Pr[Y^{a=1}=1]/\Pr[Y^{a=0}=1]$. With $L$ it does not (p. 91).
- Examples (pp. 91–92). All share one structure: a cause ($L$ or $U$) shared by $A$ and $Y$ opens a backdoor path (p. 92).

| Domain | Treatment → outcome; confounder | Name / diagram |
|---|---|---|
| Occupational | firefighting → death; physical fitness $L$ | healthy worker bias (Fig 7.1) |
| Clinical | aspirin → stroke; heart disease $L$ (indication) | confounding by indication / channeling; Fig 7.1 or 7.2 (unmeasured atherosclerosis $U$) |
| Lifestyle | exercise → death; smoking $L$; $U$ = personality/social factors | Fig 7.3. Subclinical disease $U$ gives "reverse causation" when $L$ is unknown |
| Genetic | DNA sequence $A$ → trait; sequence $L$ | linkage disequilibrium / population stratification (Fig 7.3) |
| Social | income at 65 → disability at 75; disability at 55 $L$ | Fig 7.1 |
| Environmental | particulates → coronary heart disease; other pollutants $L$; $U$ = weather | Fig 7.3 |

- Yule and Pearson et al. called such association "fictitious", "illusory", "apparent" or "spurious". The authors reply that there is nothing fictitious, illusory, apparent or spurious about it: it is a real association but cannot be read as a treatment effect. Yule's words: such associations are those "to which the most obvious physical meaning must not be assigned" (margin, p. 92).
- Throughout the chapter they assume positivity and consistency, perfectly measured nodes, no selection nodes (data are a random sample of the population of interest), and no random variability (pp. 92–93).

### 7.2 Confounding and exchangeability (pp. 93–95)
- If $Y^a \perp\!\!\!\perp A$ holds (marginally randomized experiment), $\mathrm{E}[Y^{a=1}]-\mathrm{E}[Y^{a=0}] = \mathrm{E}[Y|A=1]-\mathrm{E}[Y|A=0]$ without adjustment (p. 93).
- If marginal exchangeability fails but $Y^a \perp\!\!\!\perp A \mid L$ holds (conditionally randomized experiment), the population effect is identified by standardization or IP weighting. Conditional effects are identified by stratification (p. 93). Under conditional exchangeability:
$$\mathrm{E}[Y^{a=1}]-\mathrm{E}[Y^{a=0}] = \sum_l \mathrm{E}[Y|L=l,A=1]\Pr[L=l] - \sum_l \mathrm{E}[Y|L=l,A=0]\Pr[L=l].$$
- Key question: can we tell whether some measured $L$ gives conditional exchangeability? This is hard to judge directly. It becomes answerable if the true causal DAG is known (however we came to know it). Two approaches: the backdoor criterion and the SWIG (deferred to 7.5) (p. 93).
- **Backdoor criterion** (Pearl): $L$ satisfies it if all backdoor paths between $A$ and $Y$ are blocked by conditioning on $L$, and $L$ contains no descendants of $A$. Under faithfulness and a further condition (Technical Point 7.1), $Y^a\perp\!\!\!\perp A|L$ holds if and only if $L$ satisfies the criterion. By trying every subset of measured non-descendants of $A$, one can check any subset (p. 93).
- **Technical Point 7.1** (p. 94): $L$ satisfying the backdoor criterion always implies conditional exchangeability, even without faithfulness. The converse, given faithfulness, holds under an FFRCISTG model. Under an NPSEM-IE model, conditional exchangeability can hold without the criterion, for example in a DAG with $A\to L$, $A\to Y$. The difference arises because NPSEM-IE assumes cross-world independencies, which no randomized experiment can verify. The book always assumes FFRCISTG and faithfulness, unless stated otherwise (p. 94).
- The criterion is satisfied in two settings (p. 94):
  1. *No common causes.* The empty set satisfies it: no confounding. This is the marginally randomized experiment, where marginal exchangeability is equivalent to no common causes of treatment and outcome.
  2. *Common causes, but a subset $L$ of measured non-descendants of $A$ suffices to block all backdoor paths* (Fig 7.1). There is confounding but "no unmeasured confounding". This is the conditionally randomized experiment, where $L\to A$ by design.
- $L$ is a **sufficient set for confounding adjustment** if it consists of measured non-descendants of $A$ and blocks all backdoor paths. The treated and untreated are then exchangeable within levels of $L$ (p. 94).
- Heart transplant study: the treated had more severe heart disease $L$, a common cause of $A$ and $Y$. So they are not marginally exchangeable but are conditionally exchangeable given $L$. This is what one hopes for in observational studies (p. 95).
- The criterion says nothing about the magnitude or direction of confounding. Some open paths may be weak, or strong paths may bias in opposite directions. Unmeasured confounding is not all-or-nothing (p. 95).

*Intuition note:* Exchangeability is a statement about counterfactuals, which is often not intuitive to judge directly in complex systems. The backdoor criterion turns it into a path-checking task on a DAG, provided the DAG is believed. The answer is only as good as the DAG.

### 7.3 Confounding and the backdoor criterion (pp. 95–98)
- **Fig 7.1:** confounded, but blocking $L$ suffices, so no unmeasured confounding given $L$ (p. 95).
- **Fig 7.2** ($L\leftarrow U\to Y$ with $L\to A$) and **Fig 7.3** ($L\leftarrow U\to A$ with $L\to Y$): the common cause $U$ is unmeasured. The path can be blocked by $U$ (if measured) and also by $L$. So no unmeasured confounding given $L$ (p. 95).
- **Fig 7.4** (A ← U₂ → L ← U₁ → Y, plus A → Y): there are no common causes of $A$ and $Y$, so no confounding. $L$ is a collider on $A\leftarrow U_2\to L\leftarrow U_1\to Y$, which is blocked. Association is causation. Example: $A$ physical activity, $Y$ cervical cancer, $U_1$ pre-cancer lesion, $L$ Pap smear, $U_2$ health-conscious personality. There is no need to adjust for $L$ to compute $\Pr[Y^{a}=1]$ (p. 95).
- **Fine Point 7.1: direction and strength of bias** (p. 96).
  - *Example:* the study's risk ratio is 0.6 (a 40% mortality reduction), and smoking $L$ is a common cause. Smokers are less likely to get a transplant and more likely to die. There are fewer smokers among the treated, so lower mortality is expected even under the null. Adjustment would move the estimate up (say, 0.6 to 0.7). So lack of adjustment exaggerated the benefit (p. 96).
  - *Signed causal diagrams* (Fig 7.1, dichotomous variables): sign each arrow $L\to A$ and $L\to Y$. Both positive or both negative means positive confounding bias: the unadjusted estimate is biased upwards. Opposite signs mean negative bias: biased downwards. The rule may fail in more complex diagrams or with non-dichotomous variables (p. 96).
  - *Magnitude:* a large bias requires a strong confounder–treatment and a strong confounder–outcome association (conditional on treatment). For discrete confounders it also depends on prevalence. Unknown confounders require guesses, organized by sensitivity analyses (p. 96).
- **Definition of confounder** (p. 96). Suppose data on $L,A,Y$ suffice to identify the effect. $L$ is a *confounder* if data on $A,Y$ alone do not suffice (structural confounding). $L$ is a *non-confounder* if $A,Y$ alone suffice. Equivalently: a confounder if there is conditional but not unconditional exchangeability, a non-confounder if there is unconditional exchangeability. Informally, a confounder is any variable that can be used to adjust for confounding; this is not circular because confounding was defined first (margin, p. 96).
  - In Figs 7.1–7.3, $L$ is a confounder, since $\Pr[Y^a=1]$ is identified by $\sum_l \Pr[Y=1|A=a,L=l]\Pr[L=l]$. In 7.2 and 7.3, $L$ is not a common cause but is needed to block the path through $U$ (pp. 96–97).
  - In Fig 7.4, $L$ is a non-confounder, and $\Pr[Y^a=1]$ is just $\Pr[Y=1|A=a]$ (pp. 96–97).
- **Fig 7.4 and M-bias** (p. 97). Conditional exchangeability given $L$ does not hold. So $\Pr[Y^a=1|L=l]\ne\Pr[Y=1|A=a,L=l]$, and conditional effects within strata of $L$ are not identified. Standardizing over $L$ gives a biased estimate of $\Pr[Y^a]$. The reason is that conditioning on collider $L$ opens $A\leftarrow U_2\to L\leftarrow U_1\to Y$. This is the first example where unconditional exchangeability holds but conditional does not: the average effect is identified but generally not conditional effects. The authors call this **selection bias** (conditioning on a common effect of two marginally independent variables, see Ch. 8). It is also called M-bias, since $U_2, L, U_1$ resemble a letter M on its side (margin, p. 97).
- If $U_1$ causes $U_2$, $U_2$ causes $U_1$, or an unmeasured $U_3$ causes both, a common cause of $A$ and $Y$ exists and neither unconditional nor conditional exchangeability given $L$ holds (margin, p. 97). "Collider" is path-specific (margin, p. 97).
- **Fig 7.5** (Fig 7.4 plus $L\to A$): $A\leftarrow L\leftarrow U_1\to Y$ is open, so there is confounding. Conditioning on $L$ blocks it but opens the collider path $A\leftarrow U_2\to L\leftarrow U_1\to Y$. The bias is intractable: neither unconditional nor conditional exchangeability given $L$ (p. 97). Remedies: measure (i) $L_1$ between $U_1$ and either $A$ or $Y$, giving conditional exchangeability given $L_1$; or (ii) $L_2$ between $U_2$ and either $A$ or $L$, giving it given both $L_2$ and $L$. Fig 7.6 has both $L_1$ (between $U_1$ and $Y$) and $L_2$ (between $U_2$ and $A$) (p. 97).
- **Fine Point 7.2** (Fig 7.6; p. 98). Measure only $L_2$: no effects identified. Measure $L_2$ and $L$: conditional exchangeability given $(L_2, L)$ holds but not given either alone. Identified are:
  - Effects within joint strata of $L,L_2$: $\mathrm{E}[Y|A=a,L=l,L_2=l_2]$.
  - The unconditional effect: $\sum_{l,l_2}\mathrm{E}[Y|A=a,L=l,L_2=l_2]\Pr[L=l,L_2=l_2]$.
  - Effects within strata of $L$: $\sum_{l_2}\mathrm{E}[Y|A=a,L=l,L_2=l_2]\Pr[L_2=l_2|L=l]$.
  - Effects within strata of $L_2$: $\sum_{l}\mathrm{E}[Y|A=a,L=l,L_2=l_2]\Pr[L=l|L_2=l_2]$.
  
  Measuring only $L_1$ identifies effects within strata of $L_1$ and the unconditional effect. Measuring $L_1$ and $L$ adds effects within joint strata of $L_1,L$ and within strata of $L$. Measuring all three adds effects within joint strata of all three (p. 98).
- **Two definitions of confounding** (pp. 97–98). Here *confounding* = bias from shared causes, and *selection bias* = bias from conditioning on a common effect, which may open a blocked backdoor path (p. 97). The alternative: "bias due to an open backdoor path", or "any systematic bias that would be eliminated by randomized assignment of $A$". This labels the bias from conditioning on $L$ in Fig 7.4 as confounding, because randomization removes $U_2$ (p. 97). Under the first (structural) definition, confounding is a fact about the world independent of the analysis. Under the alternative, it depends on the analysis (Fig 7.4: none unless we adjust for $L$). The choice is "a matter of taste": identifiability conclusions rest only on whether conditional or unconditional exchangeability holds (p. 98).

*Intuition note:* Adding a variable to the adjustment set can open a path as well as close one. A collider "connects" its two parents once you condition on it, so a variable that predicts both $A$ and $Y$ may still be the wrong one to adjust for.

### 7.4 Confounding and confounders (pp. 98–100)
- The structural approach needs a priori knowledge of the DAG including all shared causes (measured or not). Then the backdoor criterion says what to adjust for (p. 98).
- **Traditional approach** (mostly associational): label variables as confounders, then adjust. Confounding is said to exist when adjusted and unadjusted estimates differ (p. 99). A traditional confounder: (1) associated with treatment, (2) associated with the outcome conditional on treatment (often "in the untreated"), (3) not on a causal pathway between treatment and outcome (p. 99).
- In Figs 7.1–7.3, $L$ meets all three, agreeing with the backdoor criterion (p. 99).
- In **Fig 7.4**, $L$ also meets all three conditions (shares $U_2$ with $A$, $U_1$ with $Y$). So the traditional approach says adjust, though there is no confounding and adjustment induces selection bias. **Fig 7.7** (A → L ← U → Y, as drawn in the image) is another example. Statistical criteria alone cannot characterize confounding (p. 99).
- Replacing (2) by "it is a cause of the outcome" avoids the error in Fig 7.4. But it then fails to call $L$ a confounder in Fig 7.2, where it should be adjusted for (Fig 7.8 is shown; see Technical Point 7.2) (p. 99).
- **Technical Point 7.2** (p. 101). To "fix" the traditional definition:
  1. Replace (3) by: there exist $L$ and $U$ with $Y^a\perp\!\!\!\perp A|L,U$. This is stronger; it effectively implies $L$ is not on a causal pathway and $\mathrm{E}[Y^a|L=l,U=u]$ is identified by $\mathrm{E}[Y|L=l,U=u,A=a]$.
  2. Replace (1) and (2) by: $U=U_1\cup U_2$ (disjoint) such that (i) $U_1$ and $A$ are not associated within strata of $L$, and (ii) $U_2$ and $Y$ are not associated within joint strata of $A,L,U_1$.
  
  If both hold, $U$ is a non-confounder given data on $L$. These conditions (Robins 1997a) let one dismiss variables as non-confounders; Greenland, Pearl and Robins applied them to Fig 7.4 (p. 101).
- **Change-in-estimate** is unreliable: estimates may differ because of selection bias or noncollapsible effect measures (e.g. odds ratios: the overall value can differ from all stratum values without confounding). The idea has long been abandoned (p. 100).
- **Structural approach:** first identify the sources of confounding (common causes), then find a sufficient adjustment set. Whether a variable is needed depends on what is already in the set. In Figs 7.2 and 7.3, $L$ is needed because $U$ is unmeasured. If $U$ were measured, $L$ would not be a confounder given $U$. So "given a causal DAG, confounding is an absolute concept whereas confounder is a relative one" (p. 100).
- The researchers' DAG may be wrong. But the structural approach (a) prevents inconsistency between beliefs and actions (believe Fig 7.4 and you won't adjust for $L$), and (b) makes assumptions explicit and open to criticism (p. 100).
- **Fine Point 7.3: surrogate confounders** (Fig 7.8, $L\leftarrow U\to A$, $U\to Y$, $A\to Y$; p. 100). $L$ (e.g., income) is a proxy of unmeasured $U$ (socioeconomic status). On one hand, it can be said that $L$ is not a confounder because it is not on a backdoor path. Adjusting for $L$ may indirectly adjust for part of the confounding by $U$. If $L$ is a binary, nondifferentially misclassified version of $U$ (measured with errors that do not depend on treatment or outcome), conditioning on $L$ partially blocks $A\leftarrow U\to Y$ under some weak conditions. So one typically prefers to adjust. Such variables are *surrogate confounders*; they can never completely eliminate confounding. A possible strategy is to measure and adjust for as many as possible (Chapter 18) (p. 100).

### 7.5 Single-world intervention graphs (pp. 101–102)
- In graph language, exchangeability means no open paths between $A$ and $Y$ other than those starting with $A$. The equivalence of $Y^a\perp\!\!\!\perp A$ with the backdoor criterion seems "magical" because counterfactuals are not on ordinary DAGs. SWIGs add counterfactuals as nodes so exchangeability can be read off by d-separation (p. 101).
- A SWIG depicts the variables that would be observed in a hypothetical world where everyone received treatment level $a$. It transforms a DAG under a given intervention (p. 101).
- **Construction** (Fig 7.9, from Fig 7.2; p. 102): the node $A$ is split in two.
  - The right side is the fixed value $a$, which inherits all arrows that were out of $A$.
  - The left side is the natural value of treatment $A$, which inherits all arrows into $A$.
  - There is no arrow from $A$ to $a$, because $a$ is a constant.
  - The outcome becomes $Y^a$. Non-descendants of $A$ need not be labelled as counterfactual (under faithfulness, treatment has no causal effect on them for any individual).
  - The natural value of treatment is assumed well defined, though usually not measurable under intervention $a$ (p. 102).
- **Fig 7.9:** $Y^a$ and $A$ are d-separated given $L$, so $Y^a\perp\!\!\!\perp A|L$ holds (p. 102).
- **Fig 7.10 (from Fig 7.4):** $Y^a\perp\!\!\!\perp A$ holds, since all paths are blocked. But $Y^a\perp\!\!\!\perp A|L$ does not, since $Y^a\leftarrow U_1\to L\leftarrow U_2\to A$ opens when the collider $L$ is conditioned on (p. 102).
- On the SWIG, $Y^a$ is d-separated from $A$ given $L$ if and only if $L$ is a non-descendant of $A$ that blocks all backdoor paths from $A$ to $Y$ (p. 102). Under an FFRCISTG, d-separation on the SWIG implies statistical independence (margin, p. 102).

*Intuition note:* A SWIG is the DAG redrawn for the "everyone gets $a$" world. Exchangeability then becomes an ordinary d-separation question between $Y^a$ and $A$. That is why the backdoor criterion works.

### 7.6 Confounding adjustment (pp. 102–107)
- Without randomization we assume that a sufficient set $L$ of non-descendants of $A$ is measured. This is uncheckable (p. 102).
- **Fine Point 7.4** (Figs 7.11, 7.12; p. 103). In Fig 7.11 ($A\to L\to Y$ with $U\to A$, $U\to L$), $L$ is a descendant of $A$ that blocks all backdoor paths. Conditioning on $L$ opens no collider path, but blocks the only causal pathway, since the effect of $A$ on $Y$ is solely through $L$. So adjusting does not eliminate bias. On the SWIG (Fig 7.12), $L$ is replaced by $L^a$. $Y^a\perp\!\!\!\perp A|L^a$ holds, but $Y^a\perp\!\!\!\perp A|L$ cannot be read off since $L$ is not on the graph (under an FFRCISTG, what cannot be read off cannot be assumed). So $\mathrm{E}[Y^{a=1}]-\mathrm{E}[Y^{a=0}]$ cannot be ensured to be identified from $(L,A,Y)$. The problem is that $L$ is a descendant of $A$, not that it is later in time. If the arrow $A\to L$ were absent, adjusting for $L$ would remove all bias even if $L$ were in the future of $A$. Topology matters, not time order (p. 103).
- **Two categories of methods** (pp. 103–104):
  - *G-methods* (standardization, IP weighting, g-estimation; "g" = generalized) use conditional exchangeability to estimate the effect in the entire population or any subset. Examples: Sections 2.4 and 2.5. Part II gives model-based extensions: parametric g-formula, marginal structural models, nested structural models.
  - *Conventional stratification-based methods* (stratification including restriction, matching) estimate the association within subsets defined by $L$. Examples: Sections 4.4 and 4.5. Part II extension: outcome regression. A common variation replaces $L$ by the propensity score $\Pr[A=1|L]$ (margin, Chapter 15).
  - Standardization and IP weighting simulate the $A$–$Y$ association as if backdoor paths through measured $L$ did not exist. IP weighting builds a pseudo-population (the population after reweighting each individual) where $A$ is independent of $L$, i.e., "deletes" $L\to A$. Stratification keeps the arrow and conditions on a subset (adds a selection box).
  - With time-varying treatments, g-methods are the methods of choice, because conventional stratification methods may result in selection bias (pp. 103–104).
- **Methods not requiring conditional exchangeability:** difference-in-differences and proximal inference (Technical Point 7.3), instrumental variables (Chapter 16), the front door criterion (Technical Point 7.4), and others. They require other unverifiable assumptions. The choice depends on which unverifiable assumptions seem more plausible (p. 104).
- **Practice:** investigators measure many non-descendants of treatment hoping to block all backdoor paths. There is no guarantee, so observational causal inference is risky. Investigators should at least generally avoid adjusting for variables affected by treatment or by the outcome. If several causal structures are plausible, run multiple analyses and state the assumptions of each. One can never be certain the true structure is among those considered (p. 104).
- **Technical Point 7.3: negative outcome controls and difference-in-differences** (Fig 7.13; p. 106).
  - *Setup:* effect of aspirin $A$ on blood pressure $Y$, with unmeasured common cause $U$ (e.g., heart disease history). Let $C$ be the outcome measured right before treatment. $U$ causes both $Y$ and $C$, and $A$ does not cause $C$.
  - *Confounding for $C$:* the causal effect of $A$ on $C$ is zero, yet $\mathrm{E}[C|A=1]-\mathrm{E}[C|A=0]\neq0$ because of $U$. This difference measures the additive confounding for $C$.
  - *Assumption:* additive equi-confounding, $\mathrm{E}[Y^0|A=1]-\mathrm{E}[Y^0|A=0]=\mathrm{E}[C|A=1]-\mathrm{E}[C|A=0]$. Then the effect in the treated is
$$\mathrm{E}[Y^1-Y^0|A=1]=(\mathrm{E}[Y|A=1]-\mathrm{E}[Y|A=0])-(\mathrm{E}[C|A=1]-\mathrm{E}[C|A=0]).$$
  - So the effect in the treated is the $A$–$Y$ association (causal effect mixed with confounding) minus the confounding measured by the $A$–$C$ association. The arrow $C\to Y$ in Fig 7.13 is not necessary.
  - This is difference-in-differences. It is somewhat restrictive: it needs $Y$ and $C$ on the same scale (e.g., pre- and post-treatment measurement) and additive equi-confounding. Sofer et al. (2016) give more general methods.
  - *Proximal inference:* with both a negative outcome control $C$ and a negative treatment control $Z$ (Fig 7.15), the effect can be nonparametrically identified despite unmeasured $U$, under additional assumptions. If $U,C,Z$ are discrete and $C$ and $Z$ each have at least as many levels as $U$, it will quite generally be identified (Miao et al. 2018) (p. 106).
- **Technical Point 7.4: front door criterion** (Fig 7.14: $A\to M\to Y$, $U\to A$, $U\to Y$; p. 107). $M$ fully mediates $A\to Y$ and shares no unmeasured causes with $A$ or $Y$. $U$ is unmeasured, so standardization and IP weighting cannot be used. Pearl showed:
$$\Pr[Y^a=1]=\sum_m \Pr[M=m|A=a]\sum_{a'}\Pr[Y=1|M=m,A=a']\Pr[A=a'].$$
  Proof steps (p. 107):
  1. $\Pr[Y^a=1]=\sum_m \Pr[M^a=m]\Pr[Y^a=1|M^a=m]$.
  2. $\Pr[M^a=m]=\Pr[M=m|A=a]$, because there is no confounding of $A\to M$ ($A\perp\!\!\!\perp M^a$).
  3. $\Pr[Y^a=1|M^a=m]=\Pr[Y^m=1]$, because (i) $Y^a=Y^m$ when $M^a=m$ ($A$ affects $Y$ only through $M$), and (ii) $Y^m\perp\!\!\!\perp M^a$ by d-separation on a SWIG with $M$ set to $m$ and $A$ to $a$.
  4. By conditional exchangeability $Y^m\perp\!\!\!\perp M|A$ on the SWIG intervening on $M$ alone, $\Pr[Y^m=1]=\sum_{a'}\Pr[Y=1|M=m,A=a']\Pr[A=a']$.
  
  This proof needs well-defined $Y^m$; alternative proofs are in Technical Points 21.11 and 21.12 (p. 107).
- **The critic** (p. 104–105). Saying "the study may be incorrect because of potential confounding" is a logical statement, not a scientific one. Every observational study may be confounded, so the criticism is noninformative. An informative criticism cites contradicting evidence, or names a specific cause such as smoking through which a backdoor path may remain open. That is a testable challenge, and the burden of proof is again the investigator's: adjust for smoking, or do a sensitivity analysis if smoking data are unavailable (p. 105).
- Selection and measurement biases must also be absent. Unlike confounding, they may arise in both randomized experiments and observational studies. The next chapter treats selection (p. 105).

## Toy example (ours, not from the text)
Binary $L$, $A$, $Y$ with a true null effect: $Y$ depends only on $L$. $\Pr[L=1]=0.5$; $\Pr[A=1|L=1]=0.8$; $\Pr[A=1|L=0]=0.2$; $\Pr[Y=1|L=1]=0.6$; $\Pr[Y=1|L=0]=0.2$ for both $A=0,1$. This is the structure of Fig 7.1.

- $\Pr[A=1]=0.5\cdot0.8+0.5\cdot0.2=0.5$.
- $\Pr[L=1|A=1]=0.5\cdot0.8/0.5=0.8$; $\Pr[L=1|A=0]=0.5\cdot0.2/0.5=0.2$.
- Crude risks: $\Pr[Y=1|A=1]=0.8\cdot0.6+0.2\cdot0.2=0.48+0.04=0.52$; $\Pr[Y=1|A=0]=0.2\cdot0.6+0.8\cdot0.2=0.12+0.16=0.28$. Crude risk ratio $=0.52/0.28\approx1.86$.
- $L$ blocks the only backdoor path $A\leftarrow L\to Y$ and is a non-descendant of $A$, so standardization is valid. $\sum_l\Pr[Y=1|A=a,L=l]\Pr[L=l]=0.6\cdot0.5+0.2\cdot0.5=0.4$ for both $a=0,1$. Causal risk ratio $=0.4/0.4=1$.

The association (1.86) is real but is not the causal effect (1). Adjusting for $L$ gives the right answer.

## Concepts
- [[confounding-vs-selection-bias]] — here: confounding is bias from shared causes of $A$ and $Y$; selection bias is from conditioning on a common effect. An alternative definition lumps both as "open backdoor path" (p. 97)
- [[back-door-criterion]] — here: $L$ blocks all backdoor paths and has no descendants of $A$. With faithfulness (FFRCISTG), it holds iff conditional exchangeability holds (p. 93)
- [[fork-chain-collider]] — a collider on a path blocks it. Conditioning on it opens the path (pp. 95, 97)
- [[d-separation]] — read off exchangeability from the SWIG (p. 102)
- [[assignment-mechanism-ignorability]] — here: marginal and conditional exchangeability $Y^a\perp\!\!\!\perp A\,(|L)$ (p. 93)
- [[potential-outcomes]] — counterfactual $Y^a$ used throughout (p. 91)
- [[propensity-score]] — $\Pr[A=1|L]$, mentioned as a variation of stratification and matching (p. 103)
- [[front-door-criterion]] — identification via a fully mediating $M$, using $\sum_m\Pr[M=m|A=a]\sum_{a'}\Pr[Y=1|M=m,A=a']\Pr[A=a']$ (p. 107)
- [[sufficient-adjustment-set]] (new) — measured non-descendants of $A$ blocking all backdoor paths (p. 94)
- [[m-bias]] (new) — bias from adjusting for a collider $L$ in $A\leftarrow U_2\to L\leftarrow U_1\to Y$ (p. 97)
- [[confounder-vs-confounding]] (new) — confounding is absolute given a DAG; "confounder" is relative to the variables already in the adjustment set (p. 100)
- [[surrogate-confounder]] (new) — measured proxy of an unmeasured common cause. It can reduce bias but could never completely eliminate confounding (p. 100)
- [[swig]] (new) — single-world intervention graph, which splits $A$ into natural value and $a$, with counterfactual outcome nodes (p. 102)
- [[g-methods]] (new) — standardization, IP weighting, g-estimation (p. 103)
- [[negative-outcome-control]] (new) — pre-treatment outcome $C$ used to estimate confounding. Difference-in-differences assumes additive equi-confounding (p. 106)
- [[signed-causal-diagram]] (new) — signs on arrows predict the direction of confounding bias in simple cases (p. 96)

## Canonical instances
- [[pedestrians-looking-up]] — thunderous noise confounds one pedestrian's looking up and another's (p. 91)
- [[heart-transplant-study]] — severe heart disease $L$ confounds transplant and death. Fine Point 7.1 adds smoking as hypothetical confounder, with RR 0.6 vs 0.7 (pp. 95, 96)
- [[healthy-worker-bias]] — fitness confounds firefighting and mortality (p. 92)
- [[pap-smear-m-bias]] — physical activity, cervical cancer, Pap smear $L$, pre-cancer lesion $U_1$, health-conscious personality $U_2$ (p. 95)
- [[aspirin-blood-pressure-did]] — negative outcome control with pre-treatment blood pressure (p. 106)

## Bridges (candidates)
- [structural-analogy] Collider conditioning opens a path (M-bias) ↔ Bayesian networks: "explaining away", where conditioning on a common effect makes independent causes dependent — the same path logic.
- [structural-analogy] Standardization $\sum_l \mathrm{E}[Y|A,L=l]\Pr[L=l]$ ↔ Bayesian inference: marginalizing a nuisance variable by averaging over its distribution.
- [metaphor] Sensitivity analysis for unmeasured confounding ↔ prior sensitivity: rerunning an analysis under several assumptions about what cannot be checked.
- [structural-analogy] Explicit, criticizable DAG assumptions ↔ Bayesian priors: assumptions stated openly so others can challenge them.

## Questions this raises
- If the DAG is only believed, not known, how should one choose among several plausible DAGs, and how sensitive are identification results to a wrong arrow?
- How large must the confounder–treatment and confounder–outcome associations be to explain away an observed effect? (Sensitivity analyses are cited but not developed here.)
- When both selection and confounding occur, which variable sets work? (Ch. 8 is announced.)
- Why do conventional stratification methods produce selection bias with time-varying treatments, while g-methods do not? (Chapter 20 is cited but not developed here.)

## Reading notes
- Page offset: printed = pdf − 9 (pdf 100 = p. 91). pdf 117 (printed 108) contains only the running header.
- Source note given with the unit: the PDF is an online revision dated 2026-08-19, not the 2020 version. Chapter and technical-point cross-references (e.g., Chapter 23, Technical Points 21.11–21.12) follow this revision and may differ from older citations.
- Technical Points 7.1–7.4, Fine Points 7.1–7.4, Figures 7.1–7.15 are all inside this unit. Figures 7.13–7.15 sit on pp. 104–105 but are used in Technical Points 7.3 and 7.4 (pp. 106–107).
- Text-layer math (Technical Points 7.3, 7.4) was garbled in places; formulas here follow the page images.
- Misprint in the source: "because it it arises" (p. 97).
- Fig 7.7's structure (A → L ← U → Y) is read from the page image; the text gives no description.
- The chapter has no exercises.
