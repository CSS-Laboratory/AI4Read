---
id: pearl-2018-bookofwhy/ch10-big
work: pearl-2018-bookofwhy
unit: "Chapter 10 — Big Data, Artificial Intelligence, and the Big Questions"
pages: "pdf 314–332 (printed page numbers not visible)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Big Data, Artificial Intelligence, and the Big Questions

## L0 — One line
Pearl argues that Big Data and AI cannot answer "Why?" without causal models, and that machines given causal models, counterfactual reasoning and a model of themselves could acquire agency and morality.

## L1 — The gist (≤ 120 words)
The final chapter asks what Big Data and AI need in order to deliver on causal questions. Pearl's answer: data mining only finds patterns, and interpretation needs a causal model. Causal diagrams plus Big Data also make it possible to transport results between populations and to correct selection bias. He dislikes opaque deep-learning systems and notes that they stay on the first rung of the Ladder of Causation. Strong AI, he says, needs causal and counterfactual reasoning, a model of itself, and memory of its intents. He treats free will as a possibly useful illusion that machines will need to emulate. He believes the answer is yes to whether we can, will and should build thinking, moral machines.

**Prerequisites:** the Ladder of Causation; causal diagrams and confounders; the do-operator and do-calculus (Ch. 7); counterfactuals (Ch. 8); Bayesian networks (Ch. 3).

## L2 — Key ideas (5–10 bullets)
- Causal questions cannot be answered from data alone; they need a model of the data-generating process. A model-free study will merely summarise (and perhaps transform) the data, not interpret it. (pdf 316)
- Data mining may be an essential first step for finding associations and posing sharper causal questions. Big Data also helps with estimation in high dimensions and with personalised medicine. (pdf 316–317)
- Transportability (carrying a result over to a different population): a causal diagram with "difference-producing" variables S lets the do-calculus (the Ch. 7 rules for manipulating do-expressions) decide whether, and how, results from other populations apply to a target. (pdf 318–320)
- Selection bias (a study sample that differs from the target population) is treated like transportability, but with the arrow drawn toward S. Knowing how subjects were recruited can turn bias into something fixable. (pdf 320–321)
- Pearl contrasts rule-based AI, Bayesian networks and deep learning. Deep learning works for some tasks but is opaque and stuck at rung one of the Ladder. (pdf 322–325)
- Strong AI should reflect on its actions through counterfactuals such as $P(Y_{X=x'}=y'\mid X=x)$, using its own intent as evidence. (pdf 326)
- Pearl counts himself a compatibilist (someone who sees the clash between free will and determinism as only apparent). He suggests free will may be an illusion with computational benefits, such as compact "should have" instructions, and says strong AIs will need to emulate it to communicate naturally with humans. (pdf 327–329)
- Pearl believes the software that gives a machine agency would need at least three parts: a causal world model, a causal model of its own software, and a memory of intents. (pdf 329–330)
- Pearl believes the answer is yes to whether we can (almost certainly, if thinking means passing the Turing test), will and should build thinking machines, and yes to making machines that tell good from evil. He prefers equipping them with human-like abilities over Asimov-style rules. (pdf 330–332)

## L3 — Walkthrough

### Introduction (pdf 314–315)
Pearl began studying causation by following an anomaly: Bayesian networks let machines think in "shades of gray", but not about causes. Examples: why turning a barometer dial does not cause rain, or what happens if one firing-squad rifleman refuses to shoot (pdf 314). Without imagining alternate realities, a machine cannot pass the mini-Turing test (it cannot answer "Why?"). The same anomaly afflicted scientists, whose statistical culture forced them to recast causal questions as associational ones (pdf 314).

He names collaborators in many fields (Glymour, Scheines, Spirtes, Halpern, Robins, Greenland, Winship, Rubin, Dawid) and describes a "Causal Revolution". Its new paradigm: it is acceptable to base claims on assumptions if they are transparent, so others can judge their plausibility and how sensitive the claims are to violations (pdf 315). He calls this transformation the second gift of AI to humanity (his phrase). The chapter returns to the first gift: machines that understand causal conversation. He gives "no definitive conclusions" (pdf 315).

### Causal models and "Big Data" (pdf 315–321)
**Data growth.** Examples: Facebook reportedly stored 300 petabytes for 2 billion users in 2014 (150 MB per user); the 1000 Genomes Project, 200 terabytes; NASA's archive, 2.5 petabytes (pdf 315–316). The data are huge but the questions are simple and causal, for example "Is there a gene that causes lung cancer?" (pdf 316).

**Main claim.** Some circles have an "almost religious faith" that answers lie in the data if we mine cleverly. Pearl says this hype is likely misguided: causal questions can never be answered from data alone and need a model of the process that generates the data. A model-free study, he says, will merely summarise and perhaps transform the data but not interpret it (pdf 316).

**Roles for Big Data (pdf 316–317).**
- Data mining may be an essential first step. It finds associations (such as the "Mr. Big" gene) and lets us pose sharper causal questions. To go further, we need a model of affected variables, confounders and other pathways.
- Big Data and machine learning help at the last step of the inference engine (estimand → estimate). They can help overcome the curse of dimensionality (estimation is hard when there are very many variables).
- In personalised medicine, causal inference screens off irrelevant characteristics and recruits similar individuals from diverse studies. Big Data supplies enough information about them.
- Data mining tempts because it spares us from stating assumptions about the world. But the most important part of the answer must come from a model, sketched by us or hypothesised by machines.

*Intuition note:* More data alone does not supply a causal model. Patterns found by mining can suggest causal questions, but going further needs a model of how the data arose.

**Transportability (pdf 317–320).** Many studies exist under different conditions, and we want to translate results to new populations. Bareinboim and Pearl gave "a complete criterion" for when results are transportable, provided the researcher draws a causal diagram marked with locations of potential disparities. Transporting may require recalibration, not face-value use (pdf 317–318).

*Example (the surfboard ad).* $X$ = advertisement, $Y$ = purchase. Data come from five places and we want Arkansas (pdf 318; Fig. 10.1 on pdf 318).
- Los Angeles (survey): younger population.
- Boston (survey): lower car ownership.
- San Francisco (survey): higher click-through rate.
- Toronto (randomized trial): higher click-through rate.
- Honolulu (randomized trial): product more desirable.

In the diagram (Fig. 10.2, pdf 319), $Z$ = age (confounder), $W$ = click-through (mediator between seeing the ad and buying), $V$ = car ownership. $S$ is a "difference-producing" variable that points to the feature by which a population differs (pdf 318).

Findings, stated by Pearl (pdf 319–320):
- Boston differs from Arkansas only in $V$, which affects neither $X$ nor $Y$. The effect should be the same, with no work in Arkansas.
- Los Angeles needs reweighting for age structure.
- The Toronto trial is sufficient despite the disparity at $W$, if $X$, $W$ and $Y$ can be measured in Arkansas.
- In some examples no single study transports, yet the target is estimable from a combination.
- Honolulu is not transportable because of the arrow $S \to Y$. But the arrow $X \to W$ is not contaminated by $S$, so Honolulu data can estimate $P(W\mid X)$. Combined with other studies' estimates, this raises precision.

**The criterion (pdf 320).** If a valid sequence of do-operations (Chapter 7 rules) transforms the target quantity into an expression in which any factor involving $S$ is free of do-operators, then the estimate is transportable. Reason: such factors can be estimated from available data, uncontaminated by $S$. Bareinboim developed an algorithm that decides transportability from graphical criteria alone, as Shpitser did for interventions (pdf 320).

Pearl's claim: what was seen as a threat to "external validity" becomes an opportunity. Big Data supplies many studies and auxiliary variables like $Z$ and $W$ (pdf 320).

**Selection bias (pdf 320–321).** Same set-up, with one change: the arrow is drawn toward $S$, read as "selection into the study". Example: if only hospitalised patients are observed (Berkson bias), draw an arrow from Hospitalization to $S$. If we understand the recruitment mechanism, we can recover from bias by collecting data on the right deconfounders and using reweighting or an adjustment formula (pdf 321).

**Pearl's assessment (pdf 321).** He reports that dozens of experts on external validity could not solve any of the toy problems in Fig. 10.2. He says the field lists threats rather than fighting them. He admits no complex case studies exist yet because the techniques are new, but is confident that external validity will lose its mystical, terrifying power, as confounding did.

### Strong AI and free will (pdf 322–332)

**Why AI progress was slow (pdf 322–323).** Rule-based systems of the 1970s–80s were brittle, handled uncertainty and contradictions badly, and were not transparent. Pearl was a "neat" (wants guarantees), as opposed to a "scruffy" (wants what works). Bayesian networks coped with uncertainty, were modular and fast, and handled probability soundly. But information flows both ways, causal and diagnostic (smoke ↔ fire), and a network "can't even tell" the causal direction. This anomaly drew him to causation (pdf 322–323).

**Deep learning (pdf 323–325).** Pearl's view: deep networks (e.g., convolutional) do not follow probability rules, do not treat uncertainty transparently, and have no explicit representation of the environment. Their programmers do not know what they compute, or how to fix them. AlphaGo beat a professional 5–0 in late 2015, Lee Sedol 4–1 in March 2016, and Ke Jie in 2017. Understanding of deep learning is "completely empirical" with no guarantees (pdf 323–324).

**Objection (some people):** transparency is not needed; we do not understand brains either. **Pearl replies:** he cannot say they are wrong, and the scruffies currently lead, but he dislikes opaque systems. We communicate with humans in the language of cause and effect because our brains work alike. Opaque robots would not allow a meaningful conversation (pdf 324).

*Vacuum example (pdf 324).* The house robot vacuums while the owner sleeps. The owner says "You shouldn't have woken me up." The robot should see that the vacuuming was at fault, without reading this as an instruction never to vacuum upstairs again. It has to understand that vacuums make noise, noise wakes people, and that makes some people unhappy; Pearl says the phrase "You shouldn't have" encodes counterfactual relations. His conclusion: transparency enables effective communication.

**Limits (pdf 325–326).** Deep learning stays on rung one of the Ladder of Causation. This does not hurt AlphaGo, since the board plus rules is an adequate causal model of Go. It hinders learning systems that operate in environments governed by rich webs of causal forces while seeing only surface manifestations of those forces; medicine, economics, education, climatology and social affairs are typical examples. Pearl's analogy: like prisoners in Plato's cave watching shadows. Economists using machine learning have noted that their methods do not answer key questions such as the impact of untried policies (new price structures, subsidies, minimum wage). Machine learning goes from finite samples to distributions; we still need to get from distributions to cause–effect relations (pdf 326).

*Intuition note:* A learner that sees only data from a world can predict well inside that world. On its own it cannot answer questions about untried policies or actions, which lie beyond rung one.

**Counterfactuals for strong AI (pdf 326).** A strong AI should reflect on its actions and learn from mistakes. A statement that it should have acted differently means: I did $X=x$ and got $Y=y$, but with $X=x'$ the outcome would have been better, perhaps $Y=y'$. Estimating such probabilities has been "completely automated", given enough data and an adequately specified causal model. Pearl suggests a key machine-learning target:
$$P(Y_{X=x'} = y' \mid X = x),$$
where the machine observes $X=x$ but not $Y$ and asks about the outcome under $x'$. It treats its intended action as an observed event and asks what would happen if it changed its mind and did $x'$ instead. This is mathematically the effect of treatment on the treated (Chapter 8), with many known estimation results (pdf 326).

*Intuition note:* The machine treats its own intention as evidence about the situation. Then it asks what would have happened if it had acted otherwise.

**Intent and free will (pdf 326–329).** A former smoker tempted to smoke should examine his intent. Pearl says no machine he knows achieves this self-awareness; he would like a machine to be led into temptation and say "No" (pdf 326). A machine that notices its intent and chooses otherwise seems to need free will. Searle called the problem "a scandal in philosophy" (pdf 326). **Conventional dogma:** robotic free will must be a gimmick. **Compatibilists (Pearl counts himself one):** the clash is only apparent, arising between two levels of description: a neural level that looks deterministic and a cognitive level with a sense of options. He compares this to microscopic time-reversible physics versus macroscopic irreversibility (smoke never flows back into the chimney) (pdf 327).

Pearl thinks understanding the benefits of the illusion is "the key" to reconciling it with determinism; the problem will dissolve once a deterministic machine is endowed with those benefits (pdf 327). Two questions result, function and simulation, with function driving simulation. Voluntary actions often leave a trace in short-term memory reflecting a purpose. But rationalisation may be reconstructive and post-action; the soccer player rarely recalls the reasons that triggered his pass (pdf 327–328).

*Coach example (pdf 328).* The coach's remark that the player should have passed to Charlie transmits information swiftly. The "similar situations" are too many to list. The coach points at the player's action, which represents his intent at decision time, and asks him to reset the priorities of his own decision "software packages", which only he can identify. Thinking in terms of intents is a shorthand converting complicated causal instructions into simple ones (pdf 328). **Pearl's conjecture:** robots would play better soccer if they communicated as if they had free will. He is less uncertain that strong AIs will need to emulate the illusion to communicate with humans (pdf 328–329).

**Agency (pdf 329–330).** Algorithmized counterfactuals are a step toward making consciousness and agency computational. A machine can include itself in its environment model. It cannot hold a complete copy of its own software, but it can hold a blueprint summary that other components reason about, mimicking self-awareness. A memory of past activations lets it answer "Why did you do that?", with reasoned or evasive answers (pdf 329). Pearl's three parts for agency software, "at least": a causal model of the world; a causal model of its own software; and a memory linking intents to outside events (pdf 329–330). Speculatively, infants may learn like this: they defy an "intention generator" for fun, watch the results, and keep a record of how good it is. Taking moral responsibility begins when we adjust our own software (pdf 330).

**Should we worry? (pdf 330–332).** Pearl believes strong AI with causal understanding and agency is a realizable promise, which raises this question. Musk and Hawking have voiced worry; Musk called AIs "potentially more dangerous than nukes" (pdf 330). Edge.org's 2015 question gave 186 answers (pdf 330). Pearl splits it into five questions and answers (pdf 330–332):
1. Have we made machines that think? **No.** So far machines can only simulate thinking in narrow domains with primitive causal structure, where they win by computing.
2. Can we? **Almost certainly yes**, if thinking means passing the Turing test. The mini-Turing test's three-level query ability seeds agency, and the algorithms exist, awaiting implementation.
3. Will we? This depends on unpredictable human events. Humans have seldom refrained from building what they can. Counter-examples are the atomic-bomb debate and the 1975 Asilomar DNA conference. In 2017 a similar AI conference adopted 23 principles; Pearl highlights #6, #7 (transparency) and #10 (value alignment), which could be made operational if systems could declare intents and discuss causes (pdf 331–332).
4. Should we? **Yes**, based on the answer to question 5.
5. Can we make machines that tell good from evil? **Yes**, Pearl believes: at least as reliably as humans, and hopefully more so. A moral machine first needs self-reflection (counterfactual analysis). Pearl says empathy and fairness "follow", being based on the same principles with another agent added (pdf 332).

**Asimov's laws.** Pearl says science fiction has shown over and over that the laws always lead to contradictions; to AI scientists this is no surprise, since rule-based systems never turn out well. The approach should not be prescriptive: give machines human cognitive abilities (empathy, long-term prediction, self-restraint) and let them decide (pdf 332). Once a moral robot exists, many apocalyptic visions start to recede into irrelevance, and we could learn from it how our free-will software works. Pearl calls such a machine "AI's first and best gift to humanity" (pdf 332).

## Toy example (ours, not from the text)
Ad effect on buying, with age $Z$ the only difference between populations (like Los Angeles in Fig. 10.2b). Assume the age-specific causal effect is the same in both places. Assume it is known from the LA study and that $Z$ can be measured in Arkansas.

Age-specific purchase probabilities:

| Group | $P(Y{=}1\mid do(X{=}1),z)$ | $P(Y{=}1\mid do(X{=}0),z)$ |
|---|---|---|
| young | 0.40 | 0.30 |
| old | 0.10 | 0.05 |

Young share: LA 0.7, Arkansas 0.3.
- LA, with ad: $0.7(0.40)+0.3(0.10)=0.28+0.03=0.31$. Without: $0.7(0.30)+0.3(0.05)=0.21+0.015=0.225$. Effect $=0.085$.
- Arkansas (reweighted), with ad: $0.3(0.40)+0.7(0.10)=0.12+0.07=0.19$. Without: $0.3(0.30)+0.7(0.05)=0.09+0.035=0.125$. Effect $=0.065$.

Using LA's 0.085 directly would overstate the Arkansas effect (0.065). Reweighting by Arkansas's age mix corrects it. The reweighting formula $\sum_z P(y\mid do(x),z)P^*(z)$ is ours, not printed in the text (the text only says "reweight").

## Concepts
- [[ladder-of-causation]] — the hierarchy of levels of causal reasoning (this unit names rung one and mentions three levels); Pearl says deep learning cannot go beyond rung one (pdf 325, 331)
- [[do-operator]] — do-calculus rules used to test whether a target is transportable (pdf 320)
- [[confounding-vs-selection-bias]] — selection bias is drawn with an arrow toward $S$; confounder example is age $Z$ (pdf 318, 320–321)
- [[transportability]] (new) — translating a study's causal result to a different population, decided by a diagram with $S$ variables (pdf 317–318)
- [[external-validity]] (new) — whether results generalise beyond the study; here reframed as solvable, not just a threat (pdf 320–321)
- [[selection-variable-S]] (new) — "difference-producing" node for transportability; arrow-into-$S$ version for selection bias (pdf 318, 321)
- [[mini-turing-test]] (new) — a machine's ability to answer causal and counterfactual questions such as "Why?" (pdf 314, 331)
- [[effect-of-treatment-on-the-treated]] (new) — $P(Y_{X=x'}=y'\mid X=x)$ as the machine's question of what would happen if it changed its mind (pdf 326)
- [[curse-of-dimensionality]] (new) — estimation is hard with many variables; Big Data and machine learning help (pdf 317)
- [[strong-ai-agency]] (new) — Pearl's at-least-three parts: world model, self model, intent memory (pdf 329–330)
- [[compatibilism]] (new) — the clash between free will and determinism is only apparent, a clash between two levels of description (pdf 327)
- [[bayesian-network]] (new) — probabilistic, modular AI tool; cannot tell causal direction (pdf 322–323)
- [[rule-based-systems]] (new) — brittle, opaque; Pearl links their failure to Asimov's laws (pdf 322, 332)

## Canonical instances
- [[ad-transportability-example]] — five cities versus Arkansas, Figs. 10.1–10.2 (pdf 318–320)
- [[berkson-hospital-selection]] — hospitalisation → $S$ as a selection-bias example (pdf 321)
- [[mr-big-gene]] — data mining proposes candidates; a causal model is needed next (pdf 316)
- [[alphago]] — deep learning success in a world whose rules are a causal model (pdf 323–325)
- [[vacuum-robot]] — the owner's complaint that the robot should not have woken them, read as a counterfactual (pdf 324)
- [[soccer-coach-should-have]] — intent-based shorthand for causal instruction (pdf 328)
- [[platos-cave]] — deep learning as watching shadows (pdf 325)
- [[asimov-laws]] — rule-based morality said to lead to contradictions (pdf 332)

## Bridges (candidates)
- [structural-analogy] Transportability with $S$ nodes ↔ bayesian: hierarchical models, where populations differ in some parameters and share others — both decide what to borrow across groups.
- [structural-analogy] Reweighting by the target's age mix ↔ bayesian: post-stratification of survey estimates — same idea of recombining stratum-specific effects with new weights.
- [metaphor] Plato's cave and deep learning ↔ bayesian: prediction without a model of the generating process.

## Questions this raises
- What exactly must the diagram contain for the transportability algorithm to give a decisive answer, and what if the diagram is wrong?
- How would a machine estimate $P(Y_{X=x'}=y'\mid X=x)$ when its causal model is itself learned from data?
- Can claims about the benefits of the "illusion of free will" be tested, for example in robot teams?
- Do empathy and fairness really "follow" from self-awareness, as Pearl claims?

## Reading notes
- Printed page numbers are not visible in the page labels or images; all references use pdf numbers (pdf 314–332).
- In the text layer the formula on pdf 326 is garbled ("P(YX = x1 = y′ | X = x)"). In the page image the prime on the subscript $x$ is set oddly (it looks like a small mark after the subscript); I read it as $x'$ from the surrounding sentence, giving $P(Y_{X=x'}=y'\mid X=x)$. The arrows in "S → Y" and "X → W" on pdf 320 were also lost in the text layer; I restored them from the surrounding sentence.
- Fig. 10.2 panels (pdf 319) were read from the image. Panel (e) is labelled "Altered causal structure" (Toronto) and (f) "Altered structure, different in outcome variable" (Honolulu).
- Pearl's confident statements ("miracles", "algorithms already exist") are his own claims; no case studies are given in this unit.
