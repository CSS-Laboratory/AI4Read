---
id: pearl-2009-causality/main
work: pearl-2009-causality
unit: "Epilogue — The Art and Science of Cause and Effect (public lecture, 1996)"
pages: 401-428
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# The Art and Science of Cause and Effect

## L0 — One line
Pearl argues that causation can be made precise as the effect of surgery on one equation of a model, guided by a diagram, and that this gives causal questions their own calculus (the *do* operator).

## L1 — The gist (≤ 120 words)
Why has causation been troublesome in science, and can it be given a precise mathematical form? Pearl's lecture traces the history from Galileo and Hume through Pearson and Fisher. He argues that ordinary equations and probability theory cannot express interventions. He proposes treating an intervention as surgery on one equation of a causal model, guided by a diagram, with a *do* operator and rules for manipulating it. His examples are randomized trials, policy analysis, the smoking–cancer debate, and choosing covariates (variables to adjust for) in Simpson's paradox. It matters because, on his account, some causal questions become computable. Pearl says explicitly that this does not solve all problems of causality.

**Prerequisites:** conditional probability P(A | B); simple linear equations; what a directed graph (nodes and arrows) is; the idea of correlation.

## L2 — Key ideas (5–10 bullets)
- Causation was long tied to blame and purpose. It became physical when multistage machines appeared. Galileo then put "how" before "why" and demanded equations (pp. 402–405).
- On Pearl's reading, Hume reduced causation to constant conjunction. Spurious correlations (rooster, barometer) show this is insufficient. This gives two riddles: how causal knowledge is learned, and what difference it makes (pp. 406–407).
- Pearson removed causation from statistics, and Fisher's randomized experiment became its one accepted causal concept. Probability theory has no word for "cause" (pp. 410–412).
- Causation is summarised behaviour under intervention. An intervention is surgery on equations, and a diagram tells which equation to delete (pp. 414, 417).
- Pearl argues this resolves Russell's puzzle of symmetric equations versus directed causes: "A causes B" and "B causes A" compare two different models. Which is which depends on how we carve the "in" from the "out" (pp. 419–420).
- Equations, Boolean algebra and probability serve observation, not intervention. The new *do* calculus has three rules, licensed by diagram conditions (pp. 421–422).
- Applications: Fisher's randomization as surgery; policy analysis in economics; the smoking–cancer debate; and the covariate-selection problem behind Simpson's paradox (pp. 418–427).

## L3 — Walkthrough

### Introduction and plan (pp. 401–402)
Pearl says causality is basic to human thought, yet shrouded in mystery and caution. Scientists and philosophers have had difficulties defining when one event truly causes another. Even the fact that a rooster's crow does not cause the sun to rise cannot easily be written as an equation (p. 401). The lecture has three parts: a historical sketch of the difficulties; ideas that reduce them; practical tools for statistics and social science (pp. 401–402).

### Part 1: A historical sketch

**Ancient causality (pp. 402–403).**
- In the Bible story of Adam and Eve, God asks only for facts; Adam and Eve volunteer causal explanations. Pearl concludes that causal explanation is a man-made concept, used in the story exclusively for passing responsibility; for thousands of years explanations had no other function (p. 402).
- Therefore, Pearl says, only gods, people and animals could cause things to happen, not objects, events or physical processes. In the ancient world natural events were simply predetermined; a die roll was a divine message, as in the casting of lots in Jonah (p. 402).
- Problems began with engineering. In multistage machines, a broken rope or rusty pulley is a more useful explanation than blaming God or the operator. Physical objects became causal agents (p. 403).
- These objects inherited traits of gods and humans: force, will, purpose. Aristotle called explanation by purpose the "final cause" (pp. 403–404). Causality thus served a dual role: target of blame and carrier of physical control (p. 404).

**Galileo (pp. 404–405).** Pearl reads the title page of Recordes's 1575 book as showing the wheel of fortune turned by human ignorance, not God's wisdom. As human knowledge took over God's role as final cause, causal explanation as a whole came under attack (p. 404). Galileo's two maxims (1638):
1. Description first, explanation second. "How" precedes "why".
2. Description is done in mathematics, i.e. equations (p. 404).

- Equations let engineers ask "how to" questions as well as "what if". Algebra does not discriminate among variables, so we can solve for parameters given the desired behaviour (p. 405).
- Physics filled with empirical laws (Snell, Hooke, Ohm, Joule) used before they were explained (p. 405).

**Hume and the two riddles (pp. 405–407).**
- Descartes and Leibniz still sought a justification of cause. Hume went to an extreme: the "why" is superfluous, subsumed by the "how" (pp. 405–406).
- **Hume's view:** we remember flame and heat in constant conjunction, and "without any farther ceremony" call one cause and the other effect (p. 406). Pearl's reading: causal connection is a product of observation, a learnable habit of mind (p. 406).
- Pearl says Hume knew of counterexamples. The rooster crow and the barometer reading stand in constant conjunction with sunrise and rain but do not cause them. Today these are "spurious correlations" (p. 406).
- **Riddle 1 (learning):** If knowledge comes from correlation, and correlation does not imply causation, how do people acquire causal knowledge? Regularity of succession is not sufficient, so what patterns of experience would justify calling a connection causal? (pp. 406–407)
- **Riddle 2 (usage):** What difference does it make to say a connection is causal? Pearl's obvious answer is that it changes how we act (wake the rooster early to shorten the night). But if causal information has empirical content beyond regularity, it should appear in the laws of physics, and it does not (p. 407).

**Russell and the symmetry of physics (pp. 407–408).**
- **Russell (1913):** in advanced sciences the word "cause" never occurs; the law of causality is a relic of a bygone age, "surviving, like the monarchy" (p. 407).
- **Suppes:** nearly every issue of *Physical Review* has an article with "cause" or "causality" in its title (p. 407). Pearl's conclusion: physicists write physics in one language and talk it in another (p. 407).
- **Russell's reply to "causality is just shorthand" (as Pearl imagines it):** causality could not possibly be an abbreviation, because the laws of physics are all symmetric while causal relations are unidirectional (p. 408).
- Example: $f = ma$ can be rearranged freely, so any two quantities determine the third. We still say force causes acceleration, not the reverse, and the equations do not support this (p. 408).
- Few physicists cared. The tension was noticed in statistics, where distinguishing causal from other relations is explicitly demanded (p. 408).

**Statistics (pp. 408–412).**
- Galton (1888) plotted forearm length against head size. He found that the slope of the best-fit line is 1 only when one quantity predicts the other precisely, and is zero whenever prediction is no better than a random guess. It is the same whether X is plotted against Y or Y against X (p. 409). Pearl calls this the first objective, data-only measure of how two variables are related (p. 409).
- **Galton:** correlation must come from the two variations being partly due to common causes (p. 409).
- **Pearson:** he read Galton as showing a category broader than causation, correlation, with causation as its limit (p. 409). In the 1911 *Grammar of Science* he called cause and effect a "fetish". He replaced it with contingency tables (p. 410).
- Pearl: Pearson denied the need for any causal concept beyond correlation and, in Pearl's words, wiped causation out of statistics before it could take root. Fisher's randomized experiment, formulated about 25 years later, is the only causal concept permitted in mainstream statistics (p. 410).
- Pearl cites the current state: the *Encyclopedia of Statistical Science* gives 12 pages to correlation and 2 to causation, one of them showing that correlation does not imply causation. Dawid calls causal inference important but most neglected; Speed says causality should preferably not be considered at all, or else with great care; Cox and Wermuth avoid the words causal and causality out of caution (p. 411).
- Pearl's explanation: causation is harder to measure than correlation, but he calls this too simplistic. The answer, he believes, lies deeper: the word *cause* is not in the vocabulary of probability theory. The sentence that mud does not cause rain cannot be expressed; we can only say the two are dependent (p. 412). Scientific development needs knowledge to be transferred reliably between studies, and this requires a formal language (p. 412).

**Computer science (pp. 412–413).**
- A robot (like an economist or epidemiologist) needs to track down cause–effect relations from limited actions and noisy observations (Riddle 1), and the question is how it should process causal information received from its programmer (Riddle 2) (p. 413).
- A bug illustrates Russell's warning that causal relations and physical equations are incompatible. Given the rule that wet grass means it rained and the rule that breaking the bottle makes the grass wet, the computer concludes that breaking the bottle means it rained (p. 413).

*Intuition note.* Regularity of succession alone is not enough to make a connection causal (the rooster). The wet-grass bug arises because the rule that wet grass means rain is chained with an action (making the grass wet), although the rule describes what we see, not what we do.

### Part 2: The ideas

**Three ideas (p. 414).** (1) Causation as a summary of behaviour under interventions. (2) Equations and graphs as a language in which causal thoughts can be represented and manipulated. (3) Interventions as surgery over equations (p. 414).

**Circuit diagram and autonomy (pp. 414–415).**
- A circuit diagram of AND/OR gates predicts the output not only under normal operation but under millions of abnormal conditions. Examples: set Y to 0, tie Y to X, replace an AND gate by an OR gate (p. 414).
- Source of this power: *autonomy*, a term used by early economists. Gates are independent mechanisms, so one can be changed without changing the others (p. 414). The diagram describes normal functioning with exactly those building blocks that stay unaltered under intervention (p. 415).
- Pearl's three reasons for the example. First, engineers' practice holds unexploited wisdom. Second, economists have used structural equation modeling and path diagrams on and off for over 75 years but in recent years let algebraic convenience suppress the diagrams. Third, diagrams capture, in his opinion, the very essence of causation: the ability to predict consequences of abnormal eventualities and new manipulations (p. 415). S. Wright's guinea-pig diagram predicts coat patterns under changed environmental or genetic factors, which correlational analysis cannot do (p. 415).
- Pearl links this to "deep understanding" and "being in control". Understanding means knowing how things behave under new hypothetical circumstances. Gravitation gives a feeling of control over tides without practical means of control (pp. 415–416). Causal models are viewed as the litmus test separating deliberate reasoning from reactive or instinctive response (p. 416).

**Surgery on equations (pp. 416–417).**
- Take two components: a multiplier (output $Y = 2X$) and an adder (output $Z = Y + 1$). The slide equations are given in the lecture's figures (p. 416).
- These equations are not equivalent to the diagram. Rewriting them with variables switched gives equations for a different circuit, in which manipulating Y affects X and has no effect on Z, while in the original manipulating Y affects Z. Further algebra gives two constraints on three variables with no structure at all (p. 416).
- Setting Y to 0 replaces the equation $Y = 2X$ by $Y = 0$. Solving the new system gives $Z = 1$. In the lower model, the second equation is replaced; this yields $X = 0$ and leaves Z unconstrained (p. 417).
- **Definition (Pearl, p. 417):** Y is a cause of Z if, after surgically removing the equation for Y, the solution for Z depends on the new value substituted for Y.
- The diagram tells which equation to delete. Once the equations are algebraically rearranged this information is lost, and, Pearl says, in the rearranged equations there is no single equation that is the equation for Y (p. 417).
- Pearl credits the idea of modelling interventions by wiping out equations to Herman Wold (1960). He suggests early econometricians, who wanted clean algebra, rejected diagrams, and the surgery makes no sense without a diagram (p. 417).

*Intuition note.* An equation set says what holds together; a causal model also says which equations would stay intact if you forced one variable. The diagram supplies that extra information.

**Randomized experiments as surgery (p. 418).** Uncontrolled study: patients choose treatment, perhaps depending on socioeconomic background, so we cannot tell treatment from background effects. Fisher's experiment has two parts, *intervention* and *randomization*. Intervention severs the link from background to treatment and replaces it with the experimenter's assignment. Linking the new link to a coin flip guarantees the old link is broken, because the coin is assumed unaffected by anything measurable at the macroscopic level (p. 418).

**Policy analysis in economics (pp. 418–419).**
- A decision to change taxes is a surgery on the economic model. The model was built from data in which taxes responded to economic conditions (endogenous). To evaluate a policy we want to compare alternatives under the same conditions, i.e. sever that link. We should infer the behaviour of the mutilated model from data governed by the non-mutilated model (pp. 418–419).
- Pearl says you will not find this analysis in any economics textbook; all discussions he could find assume the mutilated model holds throughout, treating taxation as exogenous because the government controls it at evaluation time (p. 419).

**Resolving Russell's enigma (pp. 419–420).**
- "A causes B" versus "B causes A" compares two world models: the equation for A removed in one, the equation for B in the other (p. 419).
- **Russell's objection (as Pearl imagines it):** there is only one world model. **Pearl:** yes, but if the whole universe is in the model, causality disappears because interventions disappear. Scientists carve out an "in" piece and treat the rest as background boundary conditions. This asymmetry permits talk of outside intervention and directionality (pp. 419–420).
- Descartes' hand–eye drawing: carving out the object part makes the hand cause the light ray to change; carving out the brain part makes the light ray cause the hand to move. Directionality depends on the carving (p. 420). In AI this is McCarthy's "circumscription"; in economics it is the endogenous/exogenous choice (p. 420).
- **Causal vs. equational model (p. 420–421):** both use symmetric equations for normal conditions. A causal model adds (i) an in/out distinction, (ii) each equation as an independent mechanism, kept as a separate sentence, and (iii) interventions as surgeries over mechanisms.

**The do calculus (pp. 421–422).**
- Science has observations and interventions; a laboratory combines both. Standard algebras (equations, Boolean, probability) serve the observational part (p. 421).
- $P(\text{Rain} \mid \text{Wet})$ asks for the chance of rain given that we see the grass wet. The question of the chance it rained if we make the grass wet cannot be written, since the bar already means seeing. Inventing a symbol *do* is not enough, because probability rules do not apply to that reading. The intuitive answer is $P(\text{Rain})$ (pp. 421–422).
- The recipe, analogous to how multiplication's rules were deduced from its meaning: assign a symbol, then derive the rules from the operator's meaning, here given by the surgery procedure (p. 422).
- Three rules result. Rule 1 ignores an irrelevant observation. Rule 3 ignores an irrelevant action. Rule 2 exchanges an action with an observation of the same fact. Each transformation is licensed by a condition on the diagram (p. 422). The formulas themselves appear only on the slide and are not printed in this text.

### Part 3: Applications

**Smoking and lung cancer (pp. 423–425).**
- The 1964 Surgeon General's report rested on non-experimental studies with a strong smoking–cancer correlation, and claimed it was causal (p. 423).
- **Tobacco industry side, backed by prominent statisticians including Fisher:** an unobserved genotype may cause both cancer and a craving for nicotine. In the lecture's notation, $P(\text{Cancer} \mid do(\text{Smoke})) = P(\text{Cancer})$, meaning no effect (p. 423).
- In a hypothetical meeting the tobacco side concedes a possible weak causal link from smoking to cancer and the health side concedes possible weak links to genetic factors, giving a combined model. The statistician says the strengths cannot be estimated, since any data fit either extreme model (p. 423).
- With an auxiliary measurement of tar deposits (smoking acts through tar), the effect is computable in closed form. The task is to eliminate the *do* symbol from $P(\text{Cancer})$ under the hypothetical action. Each stage applies a rule licensed by a subgraph, ending with an expression computable from non-experimental data (p. 424).
- Pearl says this does not settle the debate. The model assumes, for example, no direct smoking-to-cancer link unmediated by tar, which the parties may not accept. Refining the model could produce graphs of twenty or more variables, and the graph "welcomes" new factors. Simple tests let one glance at the graph and decide whether an effect is computable (pp. 424–425).

**Simpson's paradox and the adjustment problem (pp. 425–427).**
- Simpson's paradox, first noticed by Pearson in 1899 per Pearl, says every statistical relationship between two variables may be reversed by including additional factors. Pearl's example: smokers have higher grades; adjusting for age reverses this in every age group; further adjusting for parent income reverses it again (p. 425). No one could say which factors to include; Pearl says these can now be identified graphically (p. 425).
- Berkeley, 1975: overall admission was higher for men; by department there was a slight bias favouring women. Women applied to more competitive departments, where admission rates were low for both sexes (p. 426).
- Fishing-net analogy: females try the small-mesh net, males the large mesh. Only females are caught, so the catch seems to favour females, yet each net by itself traps males more easily (p. 426).
- "Reverse regression": comparing salaries of equally qualified men and women, or qualifications of equally paid men and women. Men earned more than equally qualified women, and men were also more qualified than equally paid women. Conclusions are very sensitive to which variables are held constant (p. 426).
- Adjustment problem: given treatment X and response Y, choose measured factors so that comparing subjects with equal values and averaging gives the right result. Some factors are affected by treatment, some affect it, some affect both, some are unmeasurable (p. 427).
- Pearl walks through testing whether two candidates Z1 and Z2 suffice, using steps shown on slides 52–56 (not in the text). Result: "If X is disconnected from Y, then Z1 and Z2 are appropriate measurements" (p. 427).

**Conclusion (pp. 427–428).** Testing for cause and effect is difficult and discovering causes of effects more so. But causality is not mystical or metaphysical; it can be expressed in a mathematical language ready for computer analysis. Pearl calls what he has presented a sort of pocket calculator, an abacus, and says it does not solve all the problems of causality. He believes many discoveries were delayed for lack of such a language, and says Pearson could have conceived randomized experiments in 1901 had he allowed causal diagrams (pp. 427–428).

## Toy example (ours, not from the text)
Take the model $Y = 2X$, $Z = Y + 1$, as in the lecture.
- Observed state: $X = 3$ gives $Y = 6$, $Z = 7$.
- Algebraically equivalent rewriting: $X = Y/2$, $Y = Z - 1$. Check: $6/2 = 3$ and $7 - 1 = 6$, so the same observed state fits.
- **do(Y = 0) in model 1:** delete $Y = 2X$, insert $Y = 0$. Then $Z = 0 + 1 = 1$. X is no longer constrained.
- **do(Y = 0) in model 2:** delete the equation whose left side is Y, i.e. $Y = Z - 1$, insert $Y = 0$. Then $X = 0/2 = 0$, and Z has no equation.
- Both models agree on all observations, but Z becomes 1 in one and is unconstrained in the other. Only the diagram says which equation is "the equation for Y".

## Concepts
- [[do-operator]] — $P(\cdot \mid do(\cdot))$: probability after forcing a variable, as opposed to conditioning on having seen it (pp. 421–422)
- [[intervention-as-surgery]] (new) — an intervention deletes one equation and substitutes a fixed value (pp. 414, 417)
- [[autonomy-modularity]] (new) — each mechanism can be changed without changing the others (p. 414)
- [[structural-causal-model]] — equations plus a diagram, with an in/out split, independent mechanisms and surgery (pp. 420–421)
- [[causal-dag]] — the diagram saying which equation to delete and licensing transformations (pp. 417, 422)
- [[do-calculus]] (new) — three rules turning expressions with *do* into other expressions, licensed by graph conditions (p. 422)
- [[spurious-correlation]] (new) — correlation without causation (rooster, barometer) (p. 406)
- [[circumscription-endogenous-exogenous]] (new) — choosing which variables are in the model and which are background (p. 420)
- [[simpsons-paradox]] — a statistical relation may reverse when further factors are included (p. 425)
- [[adjustment-problem]] (new) — choosing which covariates to hold constant to get the right effect (p. 427)
- [[randomization-as-surgery]] (new) — a coin flip guarantees the link from background to treatment is cut (p. 418)

## Canonical instances
- [[rooster-and-barometer]] — constant conjunction without causation (p. 406)
- [[newtons-law-symmetry]] — $f = ma$ is symmetric, yet force causes acceleration (p. 408)
- [[circuit-diagram-interventions]] — one diagram predicts millions of abnormal conditions (p. 414)
- [[multiplier-adder-surgery]] — $Y = 2X$, $Z = Y+1$; setting Y to 0 gives $Z = 1$ (pp. 416–417)
- [[smoking-cancer-genotype]] — $P(\text{Cancer} \mid do(\text{Smoke}))$ versus $P(\text{Cancer})$; tar deposits as an intermediate (pp. 423–425)
- [[berkeley-admissions]] — Simpson's paradox with competitive departments (p. 426)
- [[fishing-net-analogy]] — the same reversal with two nets (p. 426)
- [[reverse-regression]] — opposite conclusions depending on which variable is held constant (p. 426)
- [[taxation-policy-surgery]] — policy as surgery; endogenous when modelled, exogenous when evaluated (pp. 418–419)

## Bridges (candidates)
- [structural-analogy] Equation deletion for do(Y=y) ↔ causal inference: the graph-surgery (truncated factorization) view of intervention — both cut the arrows into the manipulated variable.
- [structural-analogy] The lecture's tar-deposit example ↔ front-door adjustment; the lecture describes it only as a *do*-elimination, not by that name.
- [metaphor] Fisher's coin flip ↔ ignorability: randomization makes assignment independent of background factors.
- [structural-analogy] The adjustment steps (Z1, Z2 and "X disconnected from Y") ↔ back-door criterion and d-separation; the exact steps are on slides not in the text.

## Questions this raises
- The lecture claims a simple graph test decides if Z1, Z2 suffice. What exactly is the test, and what graph surgery precedes the check that "X is disconnected from Y"?
- The tar example needs the assumption of no direct smoking-to-cancer link. How sensitive is the conclusion if that assumption is false?
- Pearl's second riddle is answered by surgery. How much of the first riddle (learning causal structure from data) does the diagram actually reduce?
- If causal direction depends on how the "in" is carved out, can two scientists with different carvings both be right?

## Reading notes
- The source is a public lecture (UCLA, Nov. 1996), reprinted as the Epilogue of *Causality* (2009; printed pp. 401–428). It is written for a general audience with slides cited as [n].
- Printed page numbers equal pdf + 400.
- The text layer drops some symbols, so I restored them by context: "$f = ma$" (p. 408), "$Y = 2X$", "$Z = 1$", "$X = 0$" (p. 417); $Z = Y + 1$ is inferred from the description of the adder (p. 416) and the result $Z = 1$ when $Y = 0$, "$P(\text{Cancer} \mid do(\text{Smoke})) = P(\text{Cancer})$" (p. 423).
- Slide content is not in the text: the do-calculus formulas (slide 45), the lower pair of equations (pp. 416–417), the steps of the smoking derivation (slide 47), and the adjustment steps (slides 52–56). I did not reconstruct them.
- No exercises in this unit.
