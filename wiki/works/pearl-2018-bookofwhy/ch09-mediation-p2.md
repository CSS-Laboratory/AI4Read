---
id: pearl-2018-bookofwhy/ch09-mediation-p2
work: pearl-2018-bookofwhy
unit: "Chapter 9, part 2/2: Mediation in Linear Wonderland; Embrace the 'Would-Haves'; Case Studies of Mediation"
pages: pdf 293–313 (printed page numbers not available)
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Mediation beyond linear models: natural effects, the Mediation Formula, and three case studies

## L0 — One line
In nonlinear models "direct" and "indirect" effects can be defined as counterfactual quantities (natural direct and indirect effects), and the Mediation Formula lets us estimate them from data under explicit graph assumptions.

## L1 — The gist (≤ 120 words)
Linear path analysis treats the indirect effect as a product of path coefficients and the total effect as direct plus indirect. Pearl argues that these rules are procedures, not meanings, and fail once the model has interactions or thresholds. He redefines the effects with counterfactuals: the natural direct effect lets each person's mediator (a variable on the causal path from treatment to outcome) keep its no-treatment value, and the natural indirect effect changes the mediator only. Under explicit assumptions shown in the causal graph, the Mediation Formula estimates them without assuming a functional form. Three cases follow: the "Algebra for All" policy, the smoking gene, and tourniquets. They show opposing effects, interaction, and the bias of conditioning on a mediator.

**Prerequisites:** causal diagrams (arrows as direct causes); the do-operator; counterfactuals as "what would have happened"; conditional probability; the idea of a confounder.

## L2 — Key ideas
- In linear models the indirect effect is a product of path coefficients, and total = direct + indirect. This holds automatically in linear models, which allow no interactions; with interactions, total = direct + indirect fails (pdf 293–294).
- Baron–Kenny regression mediation (a linear method) was hugely popular. The sum-of-products rule gives wrong answers when practitioners extend it to nonlinear systems, because it assumes that effects along distinct paths add and that coefficients along one path multiply (pdf 294–295).
- In a threshold example, the controlled direct effect (CDE) depends on the value at which the mediator is fixed. Additivity fails, but a "subtractivity" identity holds, with TE the total effect, NDE the natural direct effect and NIE the natural indirect effect: TE(0→1) = NDE(0→1) − NIE(1→0) (pdf 296).
- "Product of coefficients" and "difference in coefficients" confuse a procedure with a meaning. The indirect effect is defined by a counterfactual: hold X fixed and set M to the value it would take under treatment (pdf 297–298, 301).
- Natural direct and indirect effects are defined by letting the mediator take its natural value for each individual. The Mediation Formula consists of two formulas, one for each effect. Eq. 9.5, the NIE formula, can be estimated from rung-one data (purely observational, with no do-operators) when the assumptions hold (pdf 301–302).
- Robins and Greenland stated that natural effects cannot be estimated from experiments and certainly not from observational studies. Pearl suggests a possible further reason, the "cross-worlds" condition, and disagrees: he believes there may be other routes based on rung-three (counterfactual) assumptions (pdf 302–303).
- Algebra for All: a positive direct effect (+2.7) was almost cancelled by a negative indirect effect through classroom environment (−2.3). Baron–Kenny missed the indirect effect (pdf 306–307).
- Smoking gene: the gene's effect is mostly not via smoking amount. It matters mainly for people who smoke, so this is interaction (pdf 309–310).
- Tourniquets: a study that included only patients who reached hospital conditioned on the mediator and could measure only the direct effect (pdf 312–313).

## L3 — Walkthrough

### Mediation in Linear Wonderland (pdf 293–295)

**An objection.** The reader may ask whether counterfactuals are needed at all. Surely the indirect effect is what remains after removing the direct effect, i.e. Total Effect = Direct Effect + Indirect Effect \tag{9.4} (pdf 293).

**Pearl replies:** this fails in models with interactions (also called moderation). Example: a drug works only by combining with an enzyme the body secretes. The total effect is positive. The direct effect is zero, because with the enzyme disabled the drug does not work. The indirect effect is zero, because the enzyme alone does not cure the disease. So 9.4 fails (pdf 293).

Eq. 9.4 does hold automatically in linear causal models, which allow no interactions. That makes mediation easy but limits what real processes can be described (pdf 293).

**Figure 9.7 (linear path diagram).** Treatment→Mediator = 2, Mediator→Outcome = 3, Treatment→Outcome = 7. In a linear model the controlled direct effect CDE(m) is the same for every $m$, so one can speak of "the" direct effect (pdf 293–294).
- A one-unit rise in Treatment raises Outcome by 7 directly. It raises Mediator by 2, which adds $2 \times 3 = 6$ to Outcome. Net: 13, with 7 direct and 6 indirect (pdf 294).
- General rule (Wright's path analysis): the indirect effect along a path is the product of its coefficients. Total indirect effect is the sum over indirect paths, and total effect is direct plus indirect. Pearl says this follows formally from the do-operator definition of total effect (pdf 294).

**Baron–Kenny (1986).** Variables are linear in each other. Fit two equations, one with and one without the mediator. A significant change in coefficients is taken as evidence of mediation (pdf 294). The article ranked thirty-third among the most cited papers as of 2014, with 73,000 citations on Google Scholar as of 2017 (pdf 294). Pearl attributes its popularity to demand for mediation and to its cookbook form built on familiar statistics. He notes that a causal quantity was thereby defined by purely statistical means (pdf 294–295).

**Cracks.** From the early 2000s, practitioners tried to extend the sum-of-products rule to nonlinear systems. It rests on two assumptions, additive effects along distinct paths and multiplying coefficients along one path. Both give wrong answers in nonlinear models (pdf 295). Pearl quotes Rod McDonald (2001), who advised starting from scratch. Kenny added a "causal mediation analysis" section to his website in 2014 (pdf 295).

**Salary-threshold example (Figure 9.8).** Skill = 2 × Education; Salary = 7 × Education + 3 × Skill. The applicant accepts if Salary exceeds 10. Outcome is 0 or 1 (pdf 295–296).
- Total effect of Education 0→1: Salary goes from 0 to $7 + 3\cdot 2 = 13 > 10$, so Outcome goes 0→1; TE = 1 (pdf 295).
- NIE: keep Education at 0, set Skill to the value it takes under Education = 1 (namely 2). Salary goes from 0 to $2 \times 3 = 6 < 10$. NIE = 0 (pdf 295–296).
- CDE(0): hold Skill at 0. Salary goes 0→7, Outcome stays 0. CDE(0) = 0. CDE(2): hold Skill at 2. Salary goes 6→13, Outcome 0→1. CDE(2) = 1 (pdf 296).
- Dilemma: using CDE(2) keeps additivity but seems arbitrary. Using CDE(0), which matches the natural direct effect here, loses additivity, since TE ≠ DE + IE (pdf 296).
- Pearl's resolution: a modified law holds "in general". Compute NIE in reverse (X = 1 → 0): Salary falls from 13 to 7, Outcome 1→0, so NIE = −1. Then
$$\text{TE}(X{=}0\to X{=}1) = \text{NDE}(X{=}0\to X{=}1) - \text{NIE}(X{=}1\to X{=}0),$$
here $1 = 0 - (-1)$ (pdf 296).

*Intuition note.* When effects can interact, "how much is direct" depends on where the mediator is held, so simple adding breaks. Using one direction for the direct part and the reverse direction for the indirect part restores a clean identity.

### Procedure versus meaning (pdf 297–298)
Many papers tried to carry over linear definitions: indirect effect as a product of two quantities ("product of coefficients") or as total minus direct ("difference in coefficients"). Pearl says neither is right, because both confuse procedure with meaning. The procedure is mathematical and the meaning is causal. Outside linear models the indirect effect had no meaning for regression analysts beyond "multiply the path coefficients" (pdf 297).

**Melanie Wall's student.** Wall taught the product rule. A student asked what is being held constant when interpreting an indirect effect. She had no answer (pdf 297). Pearl, who had presented his causal mediation paper four months before Wall's question (October 2001), wrote back: the indirect effect is the increase in Y when X is held constant and M is raised to whatever value it would attain under a unit increase in X (pdf 298). Pearl compares the student to the boy in "The Emperor's New Clothes" (pdf 298).

### Embrace the "would-haves" (pdf 298–304)

**Pearl's own path.** Working with Jamie Robins (1993–95) on sequential treatments, he and Robins developed a sequential back-door criterion. Robins had been asked to testify about whether workplace chemical exposure caused a worker's death, and found statisticians lacked tools for such questions (pdf 298–300). Two lessons for Pearl: an action erases arrows and makes the graph sparser, and defining the controlled direct effect with do-operations freed direct effects from linear models (pdf 300).

**The blunder.** The action-based definition did not extend to the indirect effect: there is no variable to intervene on to disable the direct path while keeping the indirect path active. Pearl first called the indirect effect a "figment of the imagination", and says this in the first edition of *Causality* was one of his three greatest blunders. He had believed the only way to disable a path was to set a variable to one value. A model can be manipulated in other ways, for example fixing treatment at 0 while setting the mediator to the value it would have had under treatment = 1 (pdf 300).

**The breakthrough.** The legal definition of discrimination ("had the employee been of a different race… and everything else had been the same", pdf 301) suggested a make-believe game that keeps each individual's characteristics constant. Hence two new definitions (pdf 301):
- **Natural direct effect (NDE):** let each individual's mediator take the value it would have without treatment and fix it there. Then change the treatment and record the difference. This differs from the controlled direct effect, where the mediator is fixed at one value for everyone.
- **Natural indirect effect (NIE):** deny treatment to everyone, then let each individual's mediator take the value it would have under treatment, and record the difference.

Pearl realized that counterfactuals are quantities computed by operations on equations or diagrams, and that every direct and indirect effect can be translated into a counterfactual expression, from which a formula for estimating them can be derived. The formula assumes no functional form for X, M, Y (pdf 301).

**Mediation Formula.** Actually two formulas, one for NDE and one for NIE. They hold subject to transparent assumptions shown in the graph. Pearl gives the NIE case for Figure 9.4 (no confounding, M mediates between X and Y) (pdf 301–302):
$$\text{NIE} = \sum_m \big[P(M=m\mid X=1) - P(M=m\mid X=0)\big]\; P(Y=1\mid X=0, M=m) \tag{9.5}$$
The bracket is the effect of X on M. The last factor is the effect of M on Y (at $X=0$). So Eq. 9.5 is a product of two nonlinear effects, the origin of the product-of-coefficients idea. Unlike Eq. 9.3 (not in this unit), it has no subscripts or do-operators, so it can be estimated from rung-one data (pdf 302).

*Intuition note.* Eq. 9.5 asks: if everyone is untreated, how much does Y change when M is shifted from its untreated distribution to its treated distribution? Each value of M is weighted by how much more (or less) common it becomes under treatment.

Pearl says one formula covers linear, nonlinear, numerical and logical relationships. It can be used to judge discrimination, to split Burks's IQ data into nature and nurture, and to compute the percentage of the total effect explained by mediation versus owed to mediation (two concepts that coincide in linear models) (pdf 302).

**Priority and pessimism.** Robins and Greenland described natural effects in words in 1992 but did not give a formula. Pearl reports that they stated such effects cannot be estimated from experimental studies and certainly not from observational studies (pdf 302). Pearl guesses a further reason: the definition mixes two worlds ("cross-worlds"): treatment held at 0 and mediator set as if treatment were 1. No experiment can replicate this (pdf 303). **Pearl's view:** their school sees replicating a randomized experiment as the only route to truth, whereas other routes may rest on data plus established or assumed knowledge, via rung-three assumptions. Their "red light" kept the field at a standstill for nine years (pdf 303).

**Why a formula, and why framed.** Pearl calls a formula "a baked idea": it leaves no ambiguity and can be followed like a recipe, provided the causal model is accurate (pdf 303). Its second purpose is social. Through the story of an artist whose framed painting cost $5,000, he says a frame marks an idea as important and worth sharing (pdf 303–304). Papers with "mediation analysis" in the title were almost absent before 2004 and now exceed a hundred a year (pdf 304).

### Case studies of mediation (pdf 304–313)

**"Algebra for All" (pdf 304–307).**
- Chicago in 1997 ended remedial high-school courses and required all ninth graders to take college-prep courses (pdf 304–305).
- Math scores rose 7.8 points over three years, a statistically significant change that Pearl says is equivalent to about 75 percent of students scoring above the pre-policy mean (pdf 305). A confounder: incoming students were already better prepared because of earlier K–8 changes. Guanglei Hong found no significant improvement after accounting for this (pdf 305).
- Hong then postulated a mediator, classroom environment, measured as the median skill level of classmates (Figure 9.10). Pearl's explanation: weaker students in mixed classes may have been discouraged or received less attention, and teachers faced new demands (pdf 305–306).
- Result: a direct effect of about +2.7 points (statistically significant) and an indirect effect of −2.3 points, which almost completely cancelled it (pdf 306).
- Hong's conclusion: keeping the curriculum change but restoring the earlier classroom environment should give a modest gain. In 2003 "Double-Dose Algebra" (extra algebra class for students below the national median) did roughly that and was generally deemed a success (pdf 306). Pearl counts this as a success for mediation analysis because it explains both results (pdf 306).
- Hong also ran the Baron–Kenny analysis ("conventional procedures"). It failed to detect the indirect effect. Pearl says the most likely reason is that linear methods cannot spot treatment–mediator interactions (pdf 307).

**The smoking gene (pdf 307–310).**
- A 2008 genome-wide association study (GWAS) found a gene (rs16969968) on chromosome 15 that codes for nicotine receptors. GWAS finds genes associated with a disease; it does not prove causality (pdf 307).
- People with two copies of the less common variant (about one-ninth of the population) have about 77% greater lung-cancer risk. The variant also seems related to smoking behavior. Smoking is tied to more than a tenfold risk; a double dose of the gene less than doubles it (pdf 308).
- Fisher's confounder reading (Figure 9.11) cannot explain smoking's strong effect (Cornfield's 1959 argument). Redrawing with smoking as mediator (Figure 9.12) changes the question to how the gene works. The answer affects treatment: a direct effect suggests extra screening, an indirect effect suggests counseling against smoking or nicotine replacement (pdf 308–309).
- VanderWeele analysed Christiani's data (1,800 patients, 1,400 controls). The indirect effect raised risk by only 1 to 3 percent; carriers smoked about one extra cigarette a day. But the gene's effect was large only for smokers (pdf 309).
- So CDE(0) is essentially zero, while CDE(1) and CDE(2) (one or two packs a day) are strong. NDE averages these controlled effects and is positive, as VanderWeele reported (pdf 309).
- Pearl says the analysis shows three things: the gene does not significantly increase cigarette consumption, it does not cause cancer through a smoking-independent path, and it raises risk significantly for smokers (pdf 310). Bierut's caveat: only cigarettes per day was measured, so deeper inhalation could not be tested (pdf 310). Whether the gene changes behavior or interacts with behavior that would happen anyway remains unclear (pdf 310).

**Tourniquets (pdf 310–313).**
- Kragh, an army surgeon, collected data from 2006 in Baghdad. Tourniquets saw rising military use; he estimates 2,000 lives saved from 2002 to 2012 (pdf 310–311). The 2015 study found that pre-hospital tourniquets did not raise survival, even within injury-severity levels (Table 9.1 below) (pdf 311).

| Severity | No tourniquet | With tourniquet |
|---|---|---|
| 3 | 502/555 (90%) | 416/465 (89%) |
| 4 | 96/111 (86%) | 212/248 (85%) |
| 5 | 16/27 (59%) | 4/7 (57%) |
| Total | 614/693 (89%) | 632/720 (88%) |

- Not Simpson's paradox: in every stratum and in aggregate, survival was slightly higher without a tourniquet (difference not statistically significant) (pdf 312).
- Two explanations. Confirmation bias: successes are credited to the tourniquet, but survival without one is credited to nothing. Or a study-design bias noted by Kragh: only patients who survived to reach the hospital were recorded (pdf 312).
- Figure 9.13: Injury Severity confounds Tourniquet Use, Pre-Admission Survival (mediator) and Post-Admission Survival. Conditioning on severity is appropriate. But studying only hospital arrivals conditions on the mediator, blocking the indirect path and estimating the direct effect (dashed arrow), which was essentially zero (pdf 312).
- An indirect effect may still exist: if tourniquets get more soldiers to hospital alive, they could be very favorable. Nothing in Table 9.1 can confirm or refute this (pdf 312–313). Kragh had no data on soldiers who died before arrival. He wrote that he had no doubt tourniquets are desirable, and Pearl praises his scientific instincts (pdf 313).

*Intuition note.* Conditioning on a mediator cuts the path through it. If the data exclude people who never reach the mediator's "good" state, you can see only what the treatment does after that stage.

## Toy example (ours, not from the text)
Binary X (treatment), M, Y; no confounding, as in Figure 9.4. Suppose $P(M{=}1\mid X{=}0)=0.2$, $P(M{=}1\mid X{=}1)=0.7$, $P(Y{=}1\mid X{=}0,M{=}0)=0.1$, $P(Y{=}1\mid X{=}0,M{=}1)=0.5$.

Eq. 9.5, term by term:
- $m=0$: $[P(M{=}0\mid X{=}1)-P(M{=}0\mid X{=}0)] = 0.3-0.8=-0.5$; times $0.1$ gives $-0.05$.
- $m=1$: $[0.7-0.2]=0.5$; times $0.5$ gives $0.25$.
- NIE $= -0.05+0.25 = 0.20$.

Check against the definition: untreated people with their natural M (mean of Y): $0.8\cdot0.1+0.2\cdot0.5=0.18$. Untreated people with M drawn as under treatment: $0.3\cdot0.1+0.7\cdot0.5=0.38$. Difference $=0.20$, the same.

## Concepts
- [[mediator]] (new) — a variable lying on a causal path from treatment to outcome, transmitting part of the effect (pdf 293)
- [[natural-direct-effect]] (new) — change in Y when X changes but M stays at the value it would have under no treatment, individual by individual (pdf 301)
- [[natural-indirect-effect]] (new) — change in Y when X is held untreated but M moves to its treated value (pdf 295–296, 301)
- [[controlled-direct-effect]] (new) — change in Y when X changes and M is fixed at one value $m$ for everyone, CDE($m$) (pdf 293, 296)
- [[mediation-formula]] (new) — Eq. 9.5 and its NDE twin: estimates natural effects from observed data under graph assumptions (pdf 301–302)
- [[interaction-moderation]] (new) — effect of one variable depends on another's level; breaks Total = Direct + Indirect (pdf 293)
- [[sum-of-products-rule]] (new) — in linear models, multiply path coefficients along a path and add over paths (pdf 294)
- [[baron-kenny-method]] (new) — compare regressions with and without the mediator; linear, noncausal in form (pdf 294)
- [[do-operator]] — intervention operator; defines the total effect and the controlled direct effect (pdf 294, 300)
- [[causal-dag]] — diagram stating which variables directly affect which; assumptions for the Mediation Formula are read from it (pdf 301)
- [[ladder-of-causation]] — Pearl contrasts rung-one (observational) data with rung-three (counterfactual) assumptions (pdf 302–303)
- [[confounding-vs-selection-bias]] — here, conditioning on a mediator via sample selection (pdf 312)
- [[simpson-s-paradox]] — mentioned only to exclude it from the tourniquet data (pdf 312)

## Canonical instances
- [[enzyme-drug-example]] (new) — positive total effect with zero direct and zero indirect effect (pdf 293)
- [[salary-threshold-example]] (new) — nonlinear model where CDE depends on $m$ and TE = NDE − NIE(reverse) (pdf 295–296)
- [[algebra-for-all]] (new) — opposing direct (+2.7) and indirect (−2.3) effects (pdf 306)
- [[smoking-gene]] (new) — confounder vs mediator view; interaction between gene and smoking (pdf 308–310)
- [[tourniquet-study]] (new) — conditioning on a mediator via selection of survivors (pdf 311–313)

## Bridges (candidates)
- [structural-analogy] conditioning on the mediator in the tourniquet study ↔ Fork, chain, collider: conditioning on the middle of a chain blocks the path
- [structural-analogy] Eq. 9.5 as a sum over $m$ weighted by $P(M{=}m\mid X)$ ↔ Posterior predictive distribution: averaging over a distribution of an intermediate quantity
- [metaphor] "Linear Wonderland" estimates failing under interaction ↔ Hierarchical models: a single global coefficient hides group-level differences

## Questions this raises
- What exact assumptions let Eq. 9.5 be estimated from observational data when there is confounding between M and Y?
- When the treatment–mediator interaction is strong, which should be reported: NDE, or the CDE at specific mediator values?
- How can one estimate the effect through a mediator when the sample excludes units that never reach it (as in the tourniquet study)?
- Does the "subtractivity" identity TE = NDE − NIE(reverse) hold in general? How is it proved?

## Reading notes
- This part begins at the section "Mediation in Linear Wonderland" (pdf 293) and ends with the tourniquet section (pdf 313). It continues the chapter's earlier discussion of Eq. 9.3, Figure 9.4 and the Mediation Fallacy, which are not in this unit.
- No printed page numbers are given in the labels, so all references are pdf numbers.
- Page images were provided only for some pages. Eq. 9.5 (pdf 302) was read from the text layer, which has a stray "× ×" and a line break. I reconstructed it from the sentence that follows, which describes the bracket and the second factor.
- Figure 9.13's image labels the mediator "Pre-Administration Survival", while the text says "Pre-Admission Survival". This is a probable misprint, and I use "Admission".
- Table 9.1 was checked against the image. Row totals sum correctly.
- The sentences about 75% of students scoring above the old mean, and VanderWeele's finding that the "analysis proves three things", are the author's wording.
