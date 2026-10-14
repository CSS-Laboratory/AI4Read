---
id: hernan-2020-whatif/ch05-interaction
work: hernan-2020-whatif
unit: "5 Interaction"
pages: 61-74
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
# Interaction (Hernán & Robins, Chapter 5)

## L0 — One line
Two treatments interact when the effect of one differs depending on the level the other is set to by a joint intervention; this is a counterfactual contrast, and it is a different concept from sufficient-cause "mechanistic" interaction.

## L1 — The gist (≤ 120 words)
The chapter asks what it means for two treatments, A and E, to "interact", and how to identify interaction from data. The counterfactual definition compares the effect of A when E is set to 1 with its effect when E is set to 0. Identifying interaction requires exchangeability, positivity and consistency for both treatments (a sufficient condition for the joint treatment, not a necessary one). If E is randomly and unconditionally assigned, interaction coincides with effect modification by E. The chapter then links interaction to 16 counterfactual response types, introduces sufficient-component causes ("causal pies"), and defines sufficient-cause interaction (synergism, antagonism). It ends by comparing the two frameworks. This matters because, when joint interventions are feasible, identifying interaction helps one choose the most effective one.

**Prerequisites:** potential outcomes $Y^a$; risk difference and risk ratio; exchangeability, positivity, consistency; effect modification (Ch. 4); standardization and IP weighting (earlier chapters).

## L2 — Key ideas (5–10 bullets)
- Interaction between A and E is defined with joint counterfactuals $Y^{a,e}$: the effect of A under $e=1$ differs from its effect under $e=0$. A and E have equal status (pp. 61–62).
- Effect modification concerns only the effect of A across levels of V, and V is not intervened on. Interaction treats both variables as interventions (p. 62).
- Identifying interaction requires exchangeability, positivity and consistency for both treatments; this is a sufficient condition for the joint treatment, not a necessary one. If E is randomly and unconditionally assigned, interaction coincides with effect modification by E (pp. 62–64).
- Interaction can be on the additive or multiplicative scale, and can be super- or sub-additive (or multiplicative) (p. 63).
- With two binary treatments there are 16 response types. Additive interaction implies that some individuals belong to at least one of three classes covering 10 specific types; absence of additive interaction implies no individual in these classes, or a perfect cancellation of equal deviations of opposite sign (pp. 64–66).
- Sufficient-component causes ("causal pies") show 9 ways to die for two treatments. A sufficient-cause interaction (synergism or antagonism) exists when A and E sit in the same pie (pp. 66–70).
- Under stated inequalities, synergism can be shown without any mechanism knowledge. The inequalities are sufficient, not necessary (pp. 67, 70–71).
- The frameworks answer different questions ("what happens?" vs "how does it happen?"). Excess fractions of two treatments may sum to over 100% (pp. 71–72).

## L3 — Walkthrough

### Introduction (p. 61)
Many causal questions involve two or more simultaneous treatments. The authors' example: randomly assign both looking up at the sky and being dressed or naked. If the effect of looking up differs between dressed and naked, the two treatments interact (p. 61). Identifying interaction lets one choose the most effective joint intervention (p. 61).

### 5.1 Interaction requires a joint intervention (pp. 61–62)
- Setting: heart transplant $A$ and multivitamins $E$, both binary. Each person has four counterfactual outcomes $Y^{a=1,e=1}, Y^{a=1,e=0}, Y^{a=0,e=1}, Y^{a=0,e=0}$ (p. 61).
- $Y^{a,e}$ is the outcome if A and E had been set to $a$ and $e$. Interventions on two or more treatments are *joint interventions* (p. 61).
- Margin note: $Y^a = Y^{a,E}$, i.e. $Y^a$ equals $Y^{a,e}$ when the observed $E$ is $e$. Consistency, $Y = Y^A = Y^{A,E}$, is a special case of this substitution (p. 61).
- **Definition.** There is interaction if the effect of A after a joint intervention setting $E=1$ differs from the effect after setting $E=0$ (p. 61). On the additive scale (risk difference):

$$\Pr[Y^{a=1,e=1}=1]-\Pr[Y^{a=0,e=1}=1] \neq \Pr[Y^{a=1,e=0}=1]-\Pr[Y^{a=0,e=0}=1].$$

- Example: the risk difference for transplant is 0.1 when everybody gets vitamins and 0.2 when nobody does. So there is additive interaction (p. 62).
- The authors say simple algebra shows this inequality implies the vitamin effect also differs by transplant level. Equivalent definition (p. 62):

$$\Pr[Y^{a=1,e=1}=1]-\Pr[Y^{a=1,e=0}=1] \neq \Pr[Y^{a=0,e=1}=1]-\Pr[Y^{a=0,e=0}=1].$$

- (added step) Both inequalities are equivalent to $\Pr[Y^{1,1}=1]+\Pr[Y^{0,0}=1] \neq \Pr[Y^{1,0}=1]+\Pr[Y^{0,1}=1]$, writing $Y^{a,e}$ for $Y^{a=a,e=e}$. So A and E have equal status.
- **Interaction vs effect modification.** V modifies the effect of A if the average causal effect of A varies across levels of V. The definition uses $Y^a$, not $Y^{a,v}$, because only A is considered a variable we could intervene on. The example is sex in Table 4.1, where the effect of sex on death was never discussed (p. 62).

*Intuition note.* Interaction asks "does the effect of one treatment change when I also set the other?". It needs both treatments to be things you could set. Effect modification only asks whether the effect of A is different in subgroups.

### 5.2 Identifying interaction (pp. 62–64)
- Identifying interaction requires exchangeability, positivity and consistency for both treatments (p. 62).
- **If E is randomly and unconditionally assigned,** positivity and consistency hold and the E=1 and E=0 groups are expected to be exchangeable. Then $\Pr[Y^{a=1,e=1}=1]=\Pr[Y^{a=1}=1\mid E=1]$ (p. 62). The definition becomes

$$\Pr[Y^{a=1}=1|E=1]-\Pr[Y^{a=0}=1|E=1]\neq \Pr[Y^{a=1}=1|E=0]-\Pr[Y^{a=0}=1|E=0],$$

which is exactly effect modification of A by E on the additive scale. So when E is randomized, interaction and effect modification coincide, and Chapter 4 methods apply with V replaced by E (pp. 62–63).
- **If E is not assigned by investigators,** one still needs the four marginal risks $\Pr[Y^{a,e}=1]$. Under the usual assumptions they can be computed by standardization or IP weighting conditional on measured covariates (p. 63). Equivalently, view $AE$ as one combined treatment with four levels (11, 01, 10, 00). Then the methods and conditions for one treatment apply, with more counterfactuals (p. 63).
- **Exchangeability only for A.** Example: effect of A in strata of E in a randomized experiment. One cannot generally assess interaction, but can assess effect modification by E, since no assumptions about E are needed to compute A's effect in each E stratum (p. 64).
- For V (nationality in Ch. 4) no identifying assumptions were made. V is a *surrogate effect modifier*: it does not act on the outcome, so it does not interact with A ("no action, no interaction"). It modifies the effect of A because it is correlated with (e.g. a proxy for) an unidentified variable that acts on Y and interacts with A (p. 64). Hence modification of A's effect by one variable can occur without interaction with that variable (p. 64).
- Margin note: interaction between A and E without modification of A's effect by E is logically possible but probably rare. It requires dual effects of A and exact cancellations (p. 64).
- **Conclusion.** A *sufficient* condition for identifying interaction is exchangeability, positivity and consistency for the joint treatment $(A,E)$ with its four values. Part III shows this is not necessary when treatments occur at different times (p. 64).
- None of the results so far require deterministic counterfactuals. Section 5.3 applies only to deterministic counterfactuals and dichotomous treatments and outcomes (p. 64).

*Intuition note.* With two treatments you simply have four "arms". If you can estimate the risk in all four arms, you can check interaction. Randomizing E makes the comparison of effects of A across E groups fair.

### Technical Point 5.1: additive and multiplicative scales (p. 63)
No additive interaction means $\Pr[Y^{1,1}=1]-\Pr[Y^{0,1}=1]=\Pr[Y^{1,0}=1]-\Pr[Y^{0,0}=1]$. This can be rewritten as

$$\Pr[Y^{1,1}=1]=\{\Pr[Y^{1,0}=1]-\Pr[Y^{0,0}=1]\}+\Pr[Y^{0,1}=1].$$

Subtracting $\Pr[Y^{0,0}=1]$ from both sides:

$$\Pr[Y^{1,1}=1]-\Pr[Y^{0,0}=1]=\{\Pr[Y^{1,0}=1]-\Pr[Y^{0,0}=1]\}+\{\Pr[Y^{0,1}=1]-\Pr[Y^{0,0}=1]\}.$$

(Here $Y^{a,e}$ stands for $Y^{a=a,e=e}$.) The joint effect is then *additive*: the sum of the effect of A in the absence of E and of E in the absence of A. Interaction on the additive scale means "$\neq$"; it is *superadditive* if ">" and *subadditive* if "<" (p. 63).

**Multiplicative scale** (causal risk ratio): interaction if

$$\frac{\Pr[Y^{1,1}=1]}{\Pr[Y^{0,0}=1]}\neq\frac{\Pr[Y^{1,0}=1]}{\Pr[Y^{0,0}=1]}\times\frac{\Pr[Y^{0,1}=1]}{\Pr[Y^{0,0}=1]}.$$

With ">" it is *supermultiplicative*; with "<", *submultiplicative* (p. 63).

### 5.3 Counterfactual response types and interaction (pp. 64–66)
- With one binary treatment there are four response types (Table 5.1, with $(Y^{a=0},Y^{a=1})$): doomed (1,1), helped (1,0), hurt (0,1), immune (0,0) (p. 64).
- With two binary treatments there are 16 types, because each person has four counterfactual outcomes (Table 5.2, p. 65). Column order is $(1,1),(0,1),(1,0),(0,0)$ for $(a,e)$.
- Type 1 (all outcomes 1) and type 16 (all 0): neither treatment has any effect. If everyone were of types 1 and 16, the sharp causal null would hold for $(A,E)$ (p. 65).
- Types 4, 6, 11, 13: the outcome depends on only one treatment. Type 4 dies only if given vitamins, type 13 only if not given vitamins, type 6 only if given transplant, type 11 only if not given transplant (p. 65).
- These six types (1, 4, 6, 11, 13, 16) share this property. For each, the effect of A is the same whatever E is, and the effect of E is the same whatever A is. If *every* individual has one of them, there is no additive interaction (p. 65).
- **Converse.** Additive interaction implies that some individuals' outcomes under $A=a$ cannot be determined without knowing $E$ (and vice versa). So there must be individuals in at least one class (p. 65):
  1. Outcome under only one of the four combinations (types 8, 12, 14, 15).
  2. Outcome under two combinations, with each treatment's effect exactly opposite at each level of the other (types 7, 10).
  3. Outcome under three of four combinations (types 2, 3, 5, 9).
- Absence of additive interaction implies either no individual in these classes, or perfect cancellation of equal deviations from additivity of opposite sign. Example: equal proportions of types 7 and 10, or of types 8 and 12 (p. 66).
- Margin notes: Miettinen (1982) described the 16 types. Greenland and Poole (1988) noted these were not invariant to relabeling 0/1 and grouped them into three recoding-invariant classes (p. 65).

**Technical Point 5.2 (monotonicity).** With one treatment, $Y^{a=0}>Y^{a=1}$ only for the "helped" type. If there are no helped individuals, effects are monotonic: counterfactuals are nondecreasing in $a$. For two treatments, effects are monotonic if every $Y^{a,e}$ is nondecreasing in both $a$ and $e$. That means there are no individuals with $(Y^{1,1}=0,Y^{0,1}=1)$, $(Y^{1,1}=0,Y^{1,0}=1)$, $(Y^{1,0}=0,Y^{0,0}=1)$, or $(Y^{0,1}=0,Y^{0,0}=1)$ (p. 66).

*Intuition note.* Interaction is about people whose outcome depends jointly on both treatments. If everyone's outcome depends on at most one treatment (or neither), the effects add up. Additivity can also appear by accident when opposite deviations cancel.

### Fine Point 5.1: more on types and interaction (p. 67)
- Question: do individuals exist who develop the outcome with both $E=1$ and $A=1$ but not with only one? These have $Y^{1,1}=1$ and $Y^{0,1}=Y^{1,0}=0$ (types 7 and 8) (p. 67).
- A *sufficient* condition for their existence (VanderWeele and Robins' theory is cited for this) is

$$\Pr[Y^{1,1}=1]-(\Pr[Y^{0,1}=1]+\Pr[Y^{1,0}=1])>0,$$

equivalently $\Pr[Y^{1,1}=1]-\Pr[Y^{0,1}=1]>\Pr[Y^{1,0}=1]$. In a randomized experiment on A and E it can be checked empirically (p. 67).
- It is not necessary, and is so strong that it may miss most cases where types 7 and 8 exist (p. 67).
- A weaker sufficient condition, **if effects are monotonic**:

$$\Pr[Y^{1,1}=1]-\Pr[Y^{0,1}=1]>\Pr[Y^{1,0}=1]-\Pr[Y^{0,0}=1].$$

Then superadditive interaction implies type 8 is present (monotonicity rules out type 7) (p. 67).
- Type 8 interaction in genetics is called *compositional epistasis* (p. 67).

### 5.4 Sufficient causes (pp. 66–69)
- Single treatment A. The variety of response types indicates A is not the only determinant of Y (p. 66).
- Treated individuals: only some die, so treatment alone is insufficient. Oversimplified example: transplant kills only those allergic to anesthesia. $U_1$ is the smallest set of background factors that together with $A=1$ is sufficient to produce death. $\{A=1,U_1=1\}$ is a minimal *sufficient cause* (p. 66).
- Untreated individuals: $A=0$ kills only those with ejection fraction < 20%. $\{A=0,U_2=1\}$ is another sufficient cause (pp. 66–67).
- "Doomed" individuals lacking $U_1$ and $U_2$ imply further background factors sufficient regardless of treatment. Example: pancreatic cancer, $U_0=1$ (p. 67).
- Margin note: by definition the dichotomous $U$ variables cannot be intervened on and cannot be affected by A (p. 67).
- Three sufficient causes. Each has *components*; Figure 5.1 draws each as a circle ("pie") with sections for components. "Sufficient-component causes" names both (p. 67).
- **Link to effect modification.** The magnitude of A's effect depends on the distribution of modifiers. Two populations share the distributions of $U_2$ and $U_0$. In one 1% have $U_1=1$; in the other 10% do. In a randomized trial with half treated, the average effect of transplant on death is greater in the 10% population. The pie $\{A=1,U_1=1\}$ is 10 times more common there, while the other two pies are equally frequent (p. 68).
- **Two treatments.** Add 2 pies (E=1 alone, E=0 alone) and 4 pies for combinations. There are 9 possible ways to die (Greenland and Poole, 1988) (p. 68):
  1. by A (E irrelevant); 2. by absence of A (E irrelevant); 3. by E (A irrelevant); 4. by absence of E (A irrelevant); 5. by both A and E; 6. by A and absence of E; 7. by E and absence of A; 8. by absence of both; 9. other mechanisms (both irrelevant).
- Each pie includes background factors from $U_1,\dots,U_8$ and $U_0$ (Figure 5.2, "causal pies") (p. 68).
- Not all 9 exist in every setting. If vitamins $E=1$ kill nobody, the three pies with $E=1$ are absent (p. 69).

### 5.5 Sufficient cause interaction (pp. 69–70)
- The counterfactual definition needs no knowledge of mechanisms, nor even that treatments "work together". It is a contrast of counterfactual quantities, identifiable in an ideal randomized experiment (p. 69).
- **Sufficient cause interaction** between A and E exists in the population if A and E occur together in a sufficient cause. Example: individuals with $U_5=1$ get the outcome only with both vitamins and transplant. An individual with $Y^{1,1}=1$ and $Y^{0,1}=Y^{1,0}=0$ implies a sufficient cause interaction is present (pp. 69–70).
- **Synergism:** $A=1$ and $E=1$ in the same sufficient cause. **Antagonism:** $A=1$ and $E=0$ (or $A=0$ and $E=1$) in the same sufficient cause. Antagonism can be seen as synergism between A and "no E" (p. 70).
- This definition refers to mechanisms, but identifying it does not always require mechanism knowledge. If the inequalities of Fine Point 5.1 hold, synergism exists. The inequality is sufficient, not necessary (p. 71).

**Fine Point 5.2 (types ↔ pies).** One treatment, table (p. 70):

| Type | $Y^{a=0}$ | $Y^{a=1}$ | Component causes |
|---|---|---|---|
| Doomed | 1 | 1 | $U_0=1$ or $\{U_1=1$ and $U_2=1\}$ |
| Helped | 1 | 0 | $U_0=0$, $U_1=0$, $U_2=1$ |
| Hurt | 0 | 1 | $U_0=0$, $U_1=1$, $U_2=0$ |
| Immune | 0 | 0 | $U_0=0$, $U_1=0$, $U_2=0$ |

A combination of component causes gives exactly one type. A type may arise from several combinations (p. 70). Exchangeability can be written mechanistically: $\Pr[U_0=1\text{ or }U_1=1\mid A=1]=\Pr[U_0=1\text{ or }U_1=1\mid A=0]$ and $\Pr[U_0=1\text{ or }U_2=1\mid A=1]=\Pr[U_0=1\text{ or }U_2=1\mid A=0]$. These are the proportions of "doomed + hurt" and "doomed + helped" (p. 70).

**Fine Point 5.3 (biologic interaction).** Sufficient-cause interaction is often called biologic interaction. Example (VanderWeele and Robins): A and E are the two alleles of a gene for an essential protein. Death occurs only with a mutation in both ($A=1,E=1$). This is synergism, since a pie contains both. Yet one might argue the alleles do not physically act on each other (p. 71).

*Intuition note.* The counterfactual definition is purely about numbers across arms. The pie definition says "these two factors are parts of the same recipe for the outcome". Some data patterns reveal the second without knowing the recipe.

### 5.6 Counterfactuals or sufficient-component causes? (pp. 71–72)
- Sufficient-component model: sets of events that together inevitably produce the outcome. It asks "given an effect, what might have been its cause?" and needs mechanism detail (p. 71).
- Potential outcomes model: one cause, many effects. It asks what would have happened had a factor been set differently, and needs no mechanism detail (p. 71).
- "What happens?" vs "how does it happen?". For estimating average effects of hypothetical interventions the counterfactual framework is natural. Pies are useful for teaching: dependence of effects on background factors, and relations among effect modification, interaction and synergism (pp. 71–72).
- Limits of the pie framework in its classical form: deterministic, depends on coding of the outcome, limited to dichotomous variables. Stochastic and categorical or ordinal extensions might help, but one may rarely have enough data (p. 72).
- Causal diagrams and decision theory are said to be essentially equivalent to the counterfactual framework (next chapter) (p. 72).
- Margin: Hume hinted at counterfactual causation; Mackie (1965) developed the pie framework and the INUS condition (p. 71).

**Fine Point 5.4 (attributable fraction).** Excess fraction for A is 75% (Fine Point 3.5) and for E is 50%. Does that mean 125% of cases are preventable? No: no intervention, single or joint, can prevent more than 100% (p. 72). Example: Zeus has $U_5=1$ and gets $A=1,E=1$. Withholding either treatment prevents his case, so he is counted in both the 75% and the 50%. Some individuals are counted twice. Hence it makes little sense to apportion disease between A and E when both may be in one pie. Phenylketonuria: the excess fraction is 100% for the foods and 100% for the genes, so it can be called 100% genetic or 100% environmental (p. 72).

**Technical Point 5.3 (monotonicity and pies).** If smoking ($A=1$) and inactivity ($E=1$) never prevent heart disease, no sufficient cause containing $A=0$ or $E=0$ can exist. Otherwise some individuals (e.g. $U_2=1$) would develop the outcome if unexposed. Figure 5.3 crosses out the pies with $U_2$, $U_4$, $U_6$, $U_7$, $U_8$ (p. 73).

## Toy example (ours, not from the text)
Suppose a randomized trial of A and E gives these risks of death (hypothetical numbers):

| | $E=0$ | $E=1$ |
|---|---|---|
| $A=0$ | 0.1 | 0.2 |
| $A=1$ | 0.3 | 0.7 |

- Effect of A when $e=1$: $0.7-0.2=0.5$. When $e=0$: $0.3-0.1=0.2$. They differ, so there is additive interaction.
- Equal-status check: effect of E when $a=1$: $0.7-0.3=0.4$. When $a=0$: $0.2-0.1=0.1$. These also differ.
- Additivity: the joint effect is $0.7-0.1=0.6$. The sum of single effects is $0.2+0.1=0.3$. Since $0.6>0.3$, the interaction is superadditive.
- Multiplicative: joint RR $=0.7/0.1=7$. Product $=(0.3/0.1)\times(0.2/0.1)=3\times2=6$. Since $7>6$, it is supermultiplicative.
- Fine Point 5.1 sufficient condition: $0.7-0.2=0.5>\Pr[Y^{1,0}=1]=0.3$. So types 7 and/or 8 exist: synergism between A and E (a pie containing both $A=1$ and $E=1$).
- Under monotonicity, the weaker condition $0.5>0.2$ gives the same conclusion. Superadditivity then implies type 8.

## Concepts
- [[joint-intervention]] — setting two or more treatments at once, giving counterfactuals $Y^{a,e}$ (new) (p. 61)
- [[additive-interaction]] — effect of A (risk difference) differs by the level E is set to; symmetric in A and E (new) (p. 61)
- [[multiplicative-interaction]] — same, with risk ratios (new) (p. 63)
- [[effect-modification]] — the effect of A varies across levels of V, where V is not intervened on (new) (p. 62)
- [[potential-outcomes]] — counterfactual outcomes $Y^{a}$, $Y^{a,e}$; used with consistency $Y=Y^{A,E}$ (p. 61)
- [[response-types]] — each person's pattern of deterministic counterfactual outcomes; 4 for one binary treatment, 16 for two (new) (pp. 64–65)
- [[monotonicity]] — no treatment prevents any individual's outcome (new) (p. 66)
- [[sufficient-component-cause]] — set of components that together inevitably produce the outcome; "causal pies" (new) (p. 67)
- [[sufficient-cause-interaction]] — A and E are components of the same sufficient cause; synergism or antagonism (new) (p. 69)
- [[excess-fraction]] — proportion of cases attributable to a treatment; two single-treatment fractions can sum above 100% (new) (p. 72)

## Canonical instances
- [[heart-transplant-vitamins]] — transplant A and vitamins E, risk-difference example 0.1 vs 0.2 (pp. 61–62)
- [[anesthesia-allergy-pie]] — 1% vs 10% $U_1=1$; effect size depends on distribution of background factors (p. 68)
- [[two-alleles-protein]] — synergism without physical action between factors (p. 71)
- [[zeus-double-counting]] — excess fractions of 75% and 50% sum above 100% (p. 72)
- [[phenylketonuria]] — cause both 100% genetic and 100% environmental (p. 72)

## Bridges (candidates)
- [structural-analogy] Interaction on additive scale ↔ regression models: a product term in a linear model measures departure from additive effects. The source does not state this; it is our proposal.
- [structural-analogy] Effect modification by V ↔ hierarchical models: group-specific effects of A varying across levels of V.
- [metaphor] Sufficient-component pies ↔ noisy-OR-style models of how several causes jointly produce an outcome. The source only gives the deterministic pie framework.

## Questions this raises
- If the interaction is on the additive scale, can it be absent on the multiplicative scale (and the reverse), and which scale should guide decisions?
- How are interaction and sufficient-cause interaction handled with continuous treatments or stochastic outcomes (the stochastic extensions p. 72 mentions)?
- What changes when the two treatments occur at different times (Part III, p. 64)?
- Can one test for types 7 and 8 more cheaply when only monotonicity is plausible (p. 67)?

## Exercises worth doing
The unit prints no exercises.

## Reading notes
- Source is the online revision dated 2026-08-19, not the 2020 print version. Chapter numbering may differ from older citations.
- Page offset: printed = pdf − 9. Pdf 83 (printed 74) holds only the running header "74 Interaction"; it is otherwise blank.
- The text layer is garbled for the equations; they are transcribed from the page images.
- The sentence "The meaning of interaction is clarified by the classification of individuals according to counterfactual response types" appears at the end of 5.3 (p. 66) and again at the start of 5.4 (p. 66); this is repetition in the source.
- Both a Technical Point 5.3 (p. 73) and a Fine Point 5.3 (p. 71) exist; they are separate series.
- "Dyonisus" is printed as such on p. 64.
- Table 5.2 column order is $(a,e)=(1,1),(0,1),(1,0),(0,0)$.
- Several results rest on cited work (VanderWeele and Robins; Greenland and Poole; Greenland and Rothman).
