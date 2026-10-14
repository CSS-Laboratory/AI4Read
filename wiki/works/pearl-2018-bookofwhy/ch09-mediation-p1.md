---
id: pearl-2018-bookofwhy/ch09-mediation-p1
work: pearl-2018-bookofwhy
unit: "Chapter 9 — Mediation: The Search for a Mechanism (part 1 of 2)"
pages: pdf 273–292 (printed page numbers not visible)
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 24
pipeline_version: 0.1
---
# Mediation: The Search for a Mechanism (part 1)

## L0 — One line
To ask *how* a cause works, we must separate direct from indirect effects, which means holding a mediator constant (or setting it counterfactually) rather than just conditioning on it, and indirect effects need rung-three counterfactuals.

## L1 — The gist (≤ 120 words)
The chapter asks the second kind of "Why?": by what mechanism does a known cause produce a known effect? A mediator is a variable on the path between cause and effect. Stories about scurvy, Barbara Burks and the Berkeley admissions case show that a wrong mediator, or conditioning on a mediator instead of holding it constant, can give wrong answers. Pearl calls the second error the Mediation Fallacy. He defines the controlled direct effect with the do-operator. The natural direct and indirect effects need counterfactuals. The Daisy-and-kittens example motivates the natural indirect effect. This matters because different mechanisms call for different actions.

**Prerequisites:** causal diagrams (arrows, colliders, confounders); the do-operator (intervening vs. seeing); the Ladder of Causation (association, intervention, counterfactual); Simpson's paradox.

## L2 — Key ideas
- A mediator is a variable through which a cause acts. Knowing it tells us what to do when circumstances change, for example when oranges run out (pdf 273–274).
- Scurvy shows the cost of a wrong mediator. Acidity was believed to be the mediator, but vitamin C is the true one. That error contributed, at least in part, to scurvy's return on polar expeditions (pdf 276–278).
- Barbara Burks drew a mediator diagram in 1926. She warned against conditioning on variables that are effects of either factor or effects of unmeasured causes of either. Her second criterion, (b), is an early example of collider bias (pdf 278–281).
- Bickel and Hammel's Berkeley analysis (stratifying by department) gives a valid estimate of the direct effect of Gender under the simple diagram of Figure 9.4. Kruskal's confounder State of Residence shows it can fail when that diagram does not hold (pdf 285–286).
- Mediation Fallacy: conditioning on a mediator is not the same as holding it constant. They give the same answer when mediator and outcome are unconfounded, but with confounding conditioning can reverse the analysis (pdf 287).
- The controlled direct effect (CDE) fixes the mediator by do(). It has one version per mediator value and can be overcontrolled and unnatural (pdf 289).
- The natural direct effect (NDE) and natural indirect effect (NIE) need counterfactual subscripts. The indirect effect has no controlled version (pdf 290).
- Pearl says a counterfactual-free "Mediation Formula" makes the NDE estimable from observational data. For the NIE, assuming no confounding between M and Y, a similar reduction to rung-one data is possible. The formulas are not given in these pages (pdf 290, 292).

## L3 — Walkthrough

### Opening: two kinds of "Why?" (pdf 273–275)
- Version 1 of "Why?" asks for the cause of a known effect. Version 2 asks for the mechanism linking a known cause and effect. This chapter treats version 2 (pdf 273).
- Mechanisms matter because different mechanisms call for different actions. Without oranges, knowing that vitamin C is the mechanism lets us use another source. Without that knowledge we might try bananas (pdf 274).
- **Mediation** is the scientists' word for this question. A statement that the effect of Drug B on heart attacks is mediated by blood pressure encodes Drug → Blood Pressure → Heart Attack. Typical questions: does the mediator account for the entire effect? Does the drug work exclusively through it? (pdf 274).
- The placebo effect is a common type of mediator: if a drug acts only through the patient's belief in its benefit, most doctors will consider it ineffective. In law, asking whether a company discriminated when it paid women less is a mediation question: is the salary gap produced directly in response to sex, or indirectly through a mediator such as qualification, over which the employer has no control? (pdf 274).
- Terms: **total effect**, **direct effect** (does not pass through a mediator), **indirect effect** (does). Defining them was a major challenge. Some tried to avoid causal vocabulary. Others dismissed the concepts as more deceptive than helpful to clear statistical thinking (pdf 274).
- Pearl once thought indirect effects have no operational implications because, unlike direct effects, they cannot be defined in the language of interventions. He then realised that counterfactuals can define them, and that they can have policy implications. They can be quantified only at the third rung, which is why he placed them at the end of the book (pdf 274–275).
- Pearl says they "could" perhaps be compared to irrational and imaginary numbers: uncomfortable at first, but usefulness eventually transformed the discomfort. He believes their usefulness will overcome doubts about counterfactuals (pdf 275).
- Later examples promised: "Algebra for All" and tourniquet use. They do not appear in these pages (pdf 275).

### Scurvy: the wrong mediator (pdf 275–278)
- Lind's 1747 experiment showed citrus fruit prevented scurvy. By the early 1800s it was a problem of the past for the British navy (pdf 275–276).
- Scurvy returned on polar expeditions (1875, 1894, Scott in 1903 and 1911). Dr. Koettlitz blamed tainted meat and called antiscorbutics a delusion. Scott's 1911 stores had inspected dried meat but no citrus (pdf 276).
- Doctors had believed, without proof, in the diagram Citrus → Acidity → Scurvy, so on this view any acid would work (pdf 277).
- Sailors switched to West Indian limes. They were as acidic as Spanish lemons but had a quarter of the vitamin C. The juice was also cooked, which may have broken down remaining vitamin C. Pearl says they were disabling the mediator (pdf 277).
- Confusion followed: sailors eating fresh meat avoided scurvy and those eating tinned meat did not. Wright proposed that bacteria in tainted meat caused ptomaine poisoning, which led to scurvy. The citrus theory was discarded (pdf 277–278).
- Funk proposed "vitamines" in 1912. By 1930 Szent-Gyorgyi had isolated the specific acid, vitamin C. True path: Citrus → Vitamin C → Scurvy (pdf 278).

*Intuition note:* If you believe in the wrong mediator, you may choose a substitute that matches the wrong mechanism and possibly lose the right one. Knowing the real mechanism tells you what you can change and what you cannot.

### Nature versus nurture: Barbara Burks (pdf 278–282)
- Pearl says Burks (1926) was, to his knowledge, the first to represent a mediator explicitly in a diagram. He says there is reason to believe, and that she "may" have, invented path diagrams independently of Wright (pdf 278, 281).
- Figure 9.2: Parental Intelligence → Child's Intelligence directly (nature), and via Social Status (nurture). X stands for other unmeasured remote causes. Burks used some double-headed arrows. Pearl assumes, for simplicity, that the main effect goes left to right so that Social Status is a mediator (pdf 278–279).
- Data: 204 families with foster children and a control group of 105 families without, IQ tests and environment questionnaires. Her path analysis gave a direct effect of parental IQ on children's IQ of 35 percent, about one-third, of IQ variation inherited. Parents 15 IQ points above average would typically have children 5 points above average (pdf 279).
- The accepted method at the time was to control for Social Status. Burks wrote that the true measure of a cause's contribution is "mutilated" if we hold constant variables that may be caused, in part or whole, by either of the two factors, or by other unmeasured remote causes that affect either of them. Pearl's gloss: for the total effect of Parental on Child's Intelligence, do not adjust for any variable on the pathway between them (pdf 280).
- Pearl translates her criterion into modern terms: bias will be introduced if we condition on variables that are (a) effects of either Parental or Child's Intelligence, or (b) effects of unmeasured causes of either (pdf 280).
- Pearl calls criterion (b) one of the earliest examples of collider bias. Social Status is a collider on the path with X. Controlling for it opens the back-door path Parental Intelligence → Social Status ← X → Child's Intelligence. Estimates of direct and indirect effects are then biased (pdf 281).
- Pearl: hers is the first warning against conditioning on a pretreatment factor, and it fits Chapter 4's M-bias examples. She was not the first to discover the collider effect, but one can argue she was the first to characterise it generally in graphical terms (pdf 281).
- Her first paper attacked partial and multiple correlation techniques. Terman wrote that she was more aggressive in standing up for her ideas than many teachers and male graduate students liked (pdf 281).
- After her doctorate she never managed to get a university professorship and had less secure research positions. In 1943, at age forty, she jumped to her death from the George Washington Bridge (pdf 282).
- Pearl says her paper served as the inspiration for Blalock and Duncan's revival of path analysis in the 1960s, through Wright's response, Ogburn's lecture and Duncan (pdf 282).

*Intuition note:* To measure the total effect of A on B, do not adjust for anything on the path from A to B. Do not adjust for effects of unmeasured causes of A or B either, because that can create false links.

### In search of a language: the Berkeley admissions paradox (pdf 282–288)
- 1973: 44 percent of male applicants and 35 percent of female applicants to Berkeley graduate school were admitted. Department by department, decisions were consistently more favourable to women. Bickel recognised Simpson's paradox (pdf 283).
- The right resolution depends on the question: is the university, or someone in it, discriminating against women? (pdf 283).
- Pearl's wife objected that if each department discriminates one way, the school cannot discriminate the other way. Pearl agrees and later says she was right (pdf 283, 288).
- Bickel and Hammel (Science, 1975) explained that women were rejected more because they applied in greater proportion to harder departments, such as humanities and social sciences, and less to easier ones such as mechanical engineering. They concluded that the campus as a whole did not discriminate against women applicants (pdf 283–284).
- Pearl speculates ("Perhaps…") that women were discouraged from technical fields or discriminated against earlier in their education. He notes that such circumstances were not under Berkeley's control, so would not be discrimination by the university (pdf 284).
- Bickel defined bias as a pattern of association between a decision and the applicant's sex, and discrimination as the exercise of a decision influenced by sex when that is immaterial to qualifications. Pearl reads the first as rung one of the Ladder and the second as rung two or three (pdf 284).
- Pearl cites *Carson v. Bethlehem Steel* (Seventh Circuit, 1996): the central question is whether the employer would have taken the same action had the employee been of a different race, age, sex and so on, with everything else the same. Pearl reads this as saying we should disable ("freeze") all causal pathways from gender to admission that pass through other variables, so discrimination equals the direct effect of gender on the admission outcome (pdf 284–285).
- Figure 9.4: Gender → Department → Outcome and Gender → Outcome. Conditioning on a mediator is incorrect for the total effect. But for discrimination, the direct effect matters, so under the assumptions of Figure 9.4 stratifying by department gives a valid estimate of the direct effect of Gender on Outcome (pdf 285).
- **Kruskal's objection:** he wrote that Bickel and Hammel's explanation did not really exonerate Berkeley, and queried whether any purely observational study could (pdf 285). Department and Outcome might share an unmeasured confounder, State of Residence (pdf 285).
  - His hypothetical: two sex-discriminating departments accept all in-state males and out-of-state females and reject all out-of-state males and in-state females, this being their only decision criterion. This is blatant discrimination. Yet it produces exactly the same data as Bickel's example, so Bickel would have to conclude there was no discrimination (pdf 285–286).
  - Pearl: Kruskal found the weak spot (no justified criterion for which variables to control) and his letter despairs of a solution (pdf 286).
- Figure 9.5 (Kruskal's diagram) has the same structure as Burks's, with State of Residence in the role of X (pdf 286).
  - Stratifying by Department closes Gender → Department → Outcome. It opens Gender → Department ← State of Residence → Outcome, because Department is a collider (pdf 286).
  - Controlling also for State of Residence closes that path. What correlation remains is due to the direct path Gender → Outcome (pdf 286).
  - Kruskal's numbers: no adjustment gives females a lower admission rate; adjusting for Department gives females a higher rate; adjusting for both gives a lower rate again (pdf 286).
- **Bias vs. discrimination:** Bickel kept that conditioning on a decision-making unit differs from conditioning on a decision criterion but did not sound confident. Pearl says bias is a slippery statistical notion that may disappear when data are sliced differently. Discrimination, as a causal concept, reflects reality and must remain stable (pdf 287).
- The missing phrase was "hold constant". To disable the indirect path, hold Department constant and tweak Gender. Statisticians instead *condition* on Department (pdf 287).
  - Conditioning is valid when Department and Outcome are unconfounded, since then seeing is the same as doing (pdf 287).
- **Mediation Fallacy** (Pearl's name): conditioning on the mediator instead of holding it constant. It is harmless if the mediator and outcome are not confounded. With confounding it can completely reverse the analysis and suggest no discrimination when there is some (pdf 287).
- Pearl says R. A. Fisher made this blunder in 1936. Epidemiologists now know to watch for mediator–outcome confounders (pdf 287).
- Pearl says the problem Kruskal called "perhaps insoluble" was solved two decades ago, with do-calculus and counterfactuals (pdf 288).
- Outcome in the real case: nothing. No lawsuits or federal investigations followed. Bickel wrote that in most cases involving favoured status for women, admissions committees seemed to be seeking to overcome long-established shortages of women in their fields. A later Supreme Court case upheld affirmative action (pdf 288).
- Pearl says his wife's intuition is a theorem of causal calculus, similar to the sure-thing principle. Savage's version covers total effects; this one covers direct effects. A global direct effect is defined by aggregating direct effects in subpopulations. Pearl sums up: local fairness everywhere implies global fairness (pdf 288).

*Intuition note:* "Seeing" the outcome within a department is not "forcing" everyone into that department. Pearl says the two are the same when department and outcome are unconfounded; Kruskal's State of Residence example shows they can come apart when they are confounded.

### Daisy, the kittens and indirect effects (pdf 288–292)
Setting: treatment X, mediator M, outcome Y.

**Controlled direct effect.** Wiggle X while forcing M (pdf 289).
- Berkeley version: force everyone to apply to history, do(M=0). Randomly assign reported sex, male as do(X=1) or female as do(X=0), regardless of actual gender (pdf 289).

$$\mathrm{CDE}(0)=P(Y=1\mid do(X=1),do(M=0))-P(Y=1\mid do(X=0),do(M=0))\tag{9.1}$$

- The "0" is the forced mediator value. Forcing engineering gives CDE(1). So there are two versions, unlike the total effect. Reporting both is an option, since departments could discriminate in opposite ways (pdf 289).
- Pearl would not recommend running this experiment. Joe, who dreams of engineering, forced into history would submit a strange application. This would distort decisions regardless of the reported sex (pdf 289).

**Natural direct effect.** Applicants report a randomised gender but apply to the department they would have preferred (pdf 289).

$$\mathrm{NDE}=P(Y_{M=M_0}=1\mid do(X=1))-P(Y_{M=M_0}=1\mid do(X=0))\tag{9.2}$$

- $M=M_0$ stands for the department a female applicant would choose herself. In the Daisy example, the $M_0$ term is the "normal conditions" case (pdf 290, 292). In the first term, department is governed by actual sex and admission by reported sex. This cannot be written with do-operators, so counterfactual subscripts are needed (pdf 290).
- CDE is a do-expression, so the laws of do-calculus can reduce it to conditional probabilities estimable from observational data (pdf 290).
- NDE cannot be defined in do-terms, so it cannot be estimated with do-calculus. Pearl stripped its counterfactual subscripts, giving the **Mediation Formula**, so it can be estimated from observational data. The formula is not shown in these pages (pdf 290).

**Natural indirect effect.** There is no controlled version of the indirect effect, because no held-constant variable can disable the direct path. A natural version exists, defined with counterfactuals (pdf 290).
- Daisy, a poodle–Chihuahua mix, stopped having accidents while three foster kittens were present and relapsed a few days after they left. Dana's wife suggested the kittens gave Daisy a sense of "pack" (a direct effect). Dana suggested the kittens forced crating and close supervision, which are housebreaking methods (a mediated effect). Figure 9.6: Other Pets → Crating/Supervision → House Training, plus Other Pets → House Training (pdf 290–291).
- Their experiment: no kittens, but crate and supervise as if kittens were there. If accidents stopped, they could reasonably conclude the mediator was responsible. If not, the direct effect becomes more plausible (pdf 291).
- Pearl says the experiment (one dog) would be considered very shaky and not publishable. Our concern is the logic. It contains two "would haves": what would have happened had the kittens not been present, and, since without kittens Dana would not have supervised Daisy, what would have happened had he supervised. These are counterfactuals (pdf 291–292).
- Pearl says double-nested counterfactuals explain why statisticians struggled to define indirect effects, yet the definition fits natural intuition: Dana's wife readily understood the logic (pdf 292).

$$\mathrm{NIE}=P(Y_{M=M_1}=1\mid do(X=0))-P(Y_{M=M_0}=1\mid do(X=0))\tag{9.3}$$

- First term: no other pets (X=0), mediator set to the value it would take with pets, $M_1$. Second term: normal conditions with no other pets. $M_1$ is computed per animal, $M_1(u)$, which puts NIE outside do-calculus and may make the experiment infeasible (pdf 292).
- Assuming no confounding between M and Y, NIE can be reduced to a counterfactual-free Mediation Formula computable from rung-one data. This reduction is possible only because we assume no confounding, which, owing to the deterministic equations of a structural causal model, lives on rung three (pdf 292).
- Result: the experiment was inconclusive. It is questionable whether Dana and his wife monitored Daisy as carefully as they would have with kittens, so it is not clear that M was truly set to $M_1$. Daisy learned over several months. The lesson: attention to a possible mediator suggested another mechanism, so they did not need to keep a kitten pack forever (pdf 292).

*Intuition note:* The CDE asks what happens if everyone is forced into the same mediator value. The NDE and NIE ask about what people or animals would have done in their natural circumstances. The price is counterfactuals, which are per-individual "would have" statements.

## Toy example (ours, not from the text)
Four equally likely units. Each has a mediator value without treatment ($M_0$) and with treatment ($M_1$). Outcome rule (assumed): $Y=1$ if $X=1$ or $M=1$, else $Y=0$.

| Unit | $M_0$ | $M_1$ |
|---|---|---|
| u1 | 0 | 1 |
| u2 | 0 | 0 |
| u3 | 1 | 1 |
| u4 | 0 | 1 |

- CDE(0): force $M=0$. With $X=1$, $Y=1$ for all four units, so the probability is 4/4 = 1. With $X=0$, $Y=0$, so the probability is 0. CDE(0) = 1 − 0 = 1.
- CDE(1): force $M=1$. Both arms give $Y=1$, so CDE(1) = 1 − 1 = 0.
- NDE, using (9.2): with $X=1$, $Y=1$ for everyone, so the first term is 1. With $X=0$ and $M=M_0$, $Y=M_0$, which is 1 only for u3, so 1/4. NDE = 1 − 1/4 = 0.75.
- NIE, using (9.3): with $X=0$ and $M=M_1$, $Y=M_1$, which is 1 for u1, u3 and u4, so 3/4. Second term is 1/4. NIE = 3/4 − 1/4 = 0.5.

The two controlled effects differ (1 vs. 0), and the natural direct effect lies between them. The indirect effect needs each unit's own $M_1$, which no single do-experiment supplies.

## Concepts
- [[mediator]] (new) — variable on the path from cause to effect, through which the effect (partly) acts (pdf 274)
- [[direct-indirect-effect]] (new) — direct effect does not pass through the mediator, indirect effect does (pdf 274)
- [[mediation-fallacy]] (new) — conditioning on a mediator rather than holding it constant. Harmless without mediator–outcome confounding (pdf 287)
- [[controlled-direct-effect]] (new) — effect of X on Y with M forced by do(M=m), as in (9.1). One version per m (pdf 289)
- [[natural-direct-effect]] (new) — effect of X on Y with M left at the value it would naturally take (e.g. the applicant's own choice of department). Needs counterfactuals, as in (9.2) (pdf 289–290)
- [[natural-indirect-effect]] (new) — effect of M changing to its treated value $M_1$ while X stays at 0, as in (9.3). No controlled version (pdf 290, 292)
- [[mediation-formula]] (new) — counterfactual-free expression for NDE (p. 290) and, assuming no M–Y confounding, for NIE (p. 292), estimable from observational data. Named but not stated here (pdf 290, 292)
- [[bias-vs-discrimination]] (new) — in Bickel's definitions, bias is an association (rung one, per Pearl). Discrimination is a causal concept (rung two or three), and case law states it counterfactually (pdf 284, 287)
- Fork, chain, collider (canon) — Social Status in Burks's diagram and Department in Kruskal's are colliders. Conditioning on them opens a spurious path (pdf 281, 286)
- Do-operator (canon) — used to define CDE (pdf 289)
- Ladder of causation (canon) — indirect effects need rung three (pdf 275, 292)
- Simpson's paradox (canon) — Berkeley data (pdf 283)
- Confounding vs selection bias (canon) — State of Residence confounds Department and Outcome (pdf 285)

## Canonical instances
- [[scurvy-lind-vitamin-c]] — wrong assumed mediator (acidity) vs. true mediator (vitamin C) (pdf 277–278)
- [[barbara-burks-1926]] — first mediator diagram; early collider-bias criterion (pdf 278–281)
- [[berkeley-admissions-paradox]] — Simpson's paradox as a mediation question; Bickel vs. Kruskal (pdf 283–288)
- [[daisy-kittens]] — motivating example for the natural indirect effect (pdf 290–292)

## Bridges (candidates)
- [structural-analogy] Collider in Burks's diagram ↔ causal-inference canon (fork, chain, collider): conditioning on a common effect opens a spurious path.
- [structural-analogy] Mediation Fallacy ↔ Simpson's paradox: both show that stratifying can change the sign of an association, and only causal assumptions say which answer to trust.
- [metaphor] Natural indirect effect ↔ imaginary numbers: Pearl's comparison of initial discomfort turning into usefulness (pdf 275).

## Questions this raises
- How exactly does the Mediation Formula remove the counterfactual subscripts, and under what conditions? (Not shown in these pages.)
- If the CDE depends on the forced mediator value, when does it equal the NDE?
- How can the "no confounding between M and Y" assumption be checked, given that it lives on rung three?
- Do the effects add up, that is, do NDE and NIE combine to the total effect? The text does not say here.

## Reading notes
- The part starts at the chapter opening (pdf 273) and ends at the end of the section "Daisy, the Kittens and Indirect Effects" (pdf 292). The chapter continues in a second part not covered here. The examples "Algebra for All" and tourniquets are promised on pdf 275 but do not appear in these pages.
- No printed page numbers are visible, so all references use pdf numbers.
- The text layer drops arrow symbols in several places, for example in the Parental Intelligence–Social Status–X path on pdf 281. I reconstructed directions from the diagrams in Figures 9.2, 9.4–9.6 and the surrounding prose.
- Equations 9.1 and 9.3 were checked against page images. For pdf 290 (equation 9.2) no page image was supplied, so equation 9.2 follows the text layer, consistent with the explanation printed below it.
- "Dana" is the coauthor, Dana Mackenzie, who tells the Daisy story. Pearl refers to his own wife for the Berkeley intuition.
- Pearl's claim about Burks's priority in path diagrams and the circumstances of her death are his own account as written.
