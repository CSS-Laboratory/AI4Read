---
id: pearl-2018-bookofwhy/ch00-introduction
work: pearl-2018-bookofwhy
unit: "Introduction: Mind over Data"
pages: "pdf 9–26 (printed page numbers not given)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Introduction: Mind over Data

## L0 — One line
Statistics long lacked a language for causes; the "Causal Revolution" supplies one (diagrams plus the do-operator), and with it causal questions can be answered by combining a causal model with data, because data alone are "profoundly dumb" about causes.

## L1 — The gist (≤ 120 words)
Pearl asks why science lacked a mathematical language for cause and effect, and what such a language changes. His answer: in his opinion the main obstacle was a vocabulary gap, and after Galton and Pearson statistics put causal talk off limits and wrongly believed answers lie in the data. The Causal Revolution adds causal diagrams (what we know) and a query language (what we want to know). An "inference engine" turns assumptions and a query into an estimand (a recipe) if the query is answerable; data then turn the recipe into an estimate. This matters because data cannot tell seeing from doing, and counterfactual ("what if") questions need a causal model. His message: you are smarter than your data.

**Prerequisites:** conditional probability $P(A\mid B)$; the idea of a variable; "correlation is not causation."

## L2 — Key ideas
- Causal questions (does X cause Y? should I act?) were long unanswerable in science because, Pearl says, science gave no means even to state them; his main explanation is a gap between causal vocabulary and the vocabulary of scientific theories. An equation such as $B = kP$ gives no way to say that pressure causes the barometer reading (pdf 10–11).
- Pearl also blames early statistics: Galton and Pearson's causal questions about heredity failed, and they declared such questions off limits; causal vocabulary was then virtually prohibited for over half a century. Wright's path analysis was a shining exception, but it remained the only early step until the 1980s (pdf 12–13).
- The calculus of causation has two languages: causal diagrams for knowledge, and a query language with the do-operator, $P(L\mid do(D))$ (pdf 14).
- Seeing and doing differ: $P(L\mid D)$ may differ from $P(L\mid do(D))$, and confusing them produces paradoxes (pdf 15).
- Counterfactuals (retrospective what-ifs) can in many cases be handled by an algorithm; people agree about them because they reflect the structure of a shared causal model (pdf 16).
- The inference engine takes Assumptions, Queries and Data and outputs a yes/no (is the query answerable?), an Estimand, and an Estimate. Some queries cannot be answered under the current model, however much data we collect (pdf 18–20).
- Causal models are adaptable: the estimand depends on the model, not on the numbers in the data. In Pearl's example, a pure data-fitter must retrain for a new population, while a learner with a causal model can reuse the estimand (pdf 22–23).
- The chapter previews the book: Ladder of Causation, history, Bayesian networks, RCTs, smoking, paradoxes, back-door/front-door/instrumental-variable tools, counterfactuals, mediation, AI (pdf 23–26).

## L3 — Walkthrough

### Opening (untitled sections, pdf 9–17)

**What the "new science" is.** Pearl calls it "causal inference." It is not particularly high-tech. It tries to emulate the causal reasoning of the human mind, which he calls the most advanced tool for managing causes and effects. Humans store a great deal of causal knowledge, which data can supplement (pdf 9). A longer-term hope is an "artificial scientist" (pdf 9).

**Its questions.** Examples: How effective is a treatment? Did the tax law or advertising raise sales? What health cost is attributable to obesity? Can hiring records prove sex discrimination? Whether to quit a job. Words like "preventing," "cause," "policy" signal causal content. Until recently science gave no means even to articulate them (pdf 10). The key contribution is a simple mathematical language for causal relationships, which allows principled combination of knowledge with data (pdf 10).

**Why so late? (the language gap).** In his opinion, the most serious impediment is the gap between the vocabulary of causal questions and the traditional vocabulary of scientific theories (pdf 11).
- Example: barometer $B = kP$ can be rewritten as $P = B/k$, $k = B/P$, or $B - kP = 0$. All say that any two quantities fix the third, and no letter is privileged. Pearl asks how one could express, in such equations, that pressure causes the barometer to change rather than the reverse; the implication is that algebra cannot (pdf 11).
- Part of the answer: tools arise from needs. We handle switches and ice cream well intuitively, so no machinery seemed needed until causal questions arose in law, business, medicine and policy (pdf 11–12).
- Analogies: probability theory arose from gamblers' games (Pascal, Fermat, Huygens); mortality tables from insurers (Halley, de Moivre); error theory from astronomy (Bernoulli, Laplace, Gauss) (pdf 12).

**The missed moment.** Modern statistics itself arose from Galton's and Pearson's causal questions about heredity. They failed, declared such questions off limits, and built a "causality-free" statistics (pdf 12). Causal vocabulary was virtually prohibited for over half a century, despite Sewall Wright (pdf 12). Pearl's verdict: when you prohibit speech, you prohibit thought (pdf 12).
- "Correlation is not causation" is correct (rooster's crow and sunrise), but statistics "fetishized" it. It says what causation is not, not what it is. Textbooks allow only "related" or "associated" (pdf 12–13).
- Path analysis (Wright, 1920s) was the only early step until the 1980s (pdf 13).
- Today's Big Data enthusiasm continues the data-centric belief that answers reside in data. Pearl's claim: data are "profoundly dumb." Example: people who took a medicine recovered faster, but perhaps they could afford it and would have recovered anyway (pdf 13).

**The Causal Revolution** (pdf 13–14). Causal models now let scientists tackle questions once judged unscientific (e.g. whether smoking harms health, or whether it was the aspirin that stopped a headache). Epidemiologists, social scientists, computer scientists and "at least some" economists and statisticians now ask these routinely (pdf 13–14).

**Two languages** (pdf 14).
- *Causal diagrams* express knowledge. Dots are variables; arrows are known or suspected causal relationships (which variable "listens" to which others). Pearl says that if you can read a map of one-way streets, you can read them.
- Other model forms exist (structural equations; lists of assumptions). Whatever the form, a model should depict, at least qualitatively, the process that generates the data.
- A *query language* expresses what we want to know, e.g. $P(L\mid do(D))$: the probability that a typical patient survives $L$ years if made to take drug $D$. This corresponds to a clinical trial. It is often compared with $P(L\mid do(\text{not-}D))$, the control (pdf 14–15).

**Seeing vs doing** (pdf 15).
- $do(D)$ signals intervention, not passive observation. Without it, differences might be confounded (mixed up with other factors). Example: if only the terminally ill took the drug, comparing groups would reflect differences in disease severity rather than the drug's effect. Forcing treatment regardless of preconditions "washes away" preexisting differences (pdf 15).
- $P(L\mid D)$ is the ordinary conditional probability: lifespan among those who voluntarily take $D$. It may be totally different from $P(L\mid do(D))$ (pdf 15).
- Barometer: seeing it fall raises the probability of a storm, while forcing it to fall does not (pdf 15).
- A world with only $P(L\mid D)$ would be strange: people would avoid doctors to lower their chance of being ill; cities would fire firefighters to reduce fires; doctors would recommend a drug to men and women but not to patients of undisclosed gender (pdf 15).
- Achievement: predicting an intervention's effect without carrying it out. This needed a definition of $do$ and a noninvasive way to emulate it (pdf 16).

> *Intuition note.* "Seeing" asks what we find among people who happened to take the drug. "Doing" asks what happens if we make people take it. They may differ when something else (like illness) influences who takes the drug.

**Counterfactuals** (pdf 16). Example: Joe took Drug D and died a month later. Might the drug have caused his death? We must imagine Joe changing his mind. Classical statistics only summarizes data and has no language for this. Causal inference provides notation and, in many cases, an algorithm ("algorithmization of counterfactuals") from the observed world to the counterfactual world.
- Empirical observation can never confirm or refute such answers. Yet people judge them reliably (had the rooster been silent, the sun would still have risen). Pearl's explanation: counterfactuals reflect the structure of our world model, and two people sharing a causal model share all counterfactual judgments (pdf 16).
- Pearl adds that counterfactual thinking underlies moral behavior, free will and social responsibility (pdf 16).

**Pearl's AI viewpoint** (pdf 16–17). Pearl says his AI background gives him points of departure from most colleagues; the first is that in AI you do not really understand a topic until you can teach it to a robot, hence his stress on notation and grammar. He holds that language shapes thought: one cannot answer a question one cannot ask, and cannot ask one with no words for it (pdf 16–17). Separately, he gives another incentive for studying causation: in the late 1980s he realized that machines' lack of causal understanding was perhaps the biggest roadblock to human-level intelligence; he believes strong AI is achievable (pdf 17).

### A Blueprint of Reality (pdf 17–23)

**The inference engine** (Figure I.1; caption says it combines data with causal knowledge to answer queries; the dashed box is needed for building the engine but is not part of it) (pdf 17–18).
- *Inputs:* Assumptions, Queries, Data.
- *Outputs, in order:* (a) a Yes/No on whether the query can in theory be answered under the model, assuming perfect, unlimited data; (b) if Yes, an **Estimand**, a formula serving as a recipe for the answer from any hypothetical data; (c) once Data arrive, an **Estimate** with statistical uncertainty. That uncertainty reflects finite sample size, measurement error and missing data (pdf 18).

Pearl annotates nine boxes using the query "effect of Drug D on Lifespan L":
1. **Knowledge:** the agent's past experience, education and cultural mores that are relevant. It stays implicit (dotted box) (pdf 18).
2. **Assumptions:** the simplifying statements the researcher makes explicit. Some logicians say a model is just a list of assumptions. Computer scientists object that how assumptions are represented matters for specifying, using and revising them (pdf 18–19).
3. **Causal model:** options include diagrams, structural equations, logical statements. Pearl favors diagrams for transparency. Definition for diagrams: $X$ is a cause of $Y$ if $Y$ "listens" to $X$ and determines its value in response. So draw an arrow $D \to L$. Other relevant variables are denoted collectively $Z$ (pdf 19).
4. **Testable implications:** listening patterns usually leave patterns in data. Example: the statement that no path connects $D$ and $L$ translates into the statistical statement that $D$ and $L$ are independent. If data contradict this implication, the model needs revision. A second engine (not drawn) computes the "degree of fitness" between data and assumptions (pdf 19–20).
5. **Query:** must be in causal vocabulary, e.g. $P(L\mid do(D))$ (pdf 20).
6. **Estimand:** Latin for what is to be estimated, written like a probability formula, e.g. $P(L\mid D,Z)\times P(Z)$, but really a recipe certified by the engine (pdf 20).
   - Unlike ordinary estimation, some queries cannot be answered under the current model *even with any amount of data*. Example: if both $D$ and $L$ depend on $Z$ (disease stage) and $Z$ cannot be measured, $P(L\mid do(D))$ cannot be answered. Collecting data is then a waste; refine the model, by new knowledge about $Z$ or by simplifying assumptions (risking error), e.g. that $Z$'s effect on $D$ is negligible (pdf 20).
7. **Data:** the ingredients. They give quantities like $P(L\mid D)$ or $P(L\mid D,Z)$. The estimand says how to combine them into an expression that, given the model, is logically equivalent to the causal query (pdf 20).
   - In traditional statistics the estimand and the query coincide (e.g. query $P(D\mid L)$ is itself the estimand), so no causal knowledge is needed. Hence some statisticians find it hard to see why data cannot replace scientific knowledge (pdf 20–21).
8. **Estimate:** approximate, since data are a finite sample. Statistics and machine learning supply tools for this uncertainty (maximum likelihood, propensity scores, confidence intervals, significance tests) (pdf 21).
9. **Answer:** if the model is correct and data sufficient, we get an answer such as: the drug increases the lifespan $L$ of diabetic patients $Z$ by 30 percent, plus or minus 20 percent. It adds to Knowledge (box 1) and, if things did not go as expected, might suggest improvements to the causal model (box 3) (pdf 21).

> *Intuition note.* The engine splits the work: the model decides *what formula* answers the question; the data only supply *the numbers* for that formula. Without a model, no formula can be justified.

**Why the process matters** (pdf 21–23).
- Everyday causal judgment works without such machinery, but teaching a robot, or working where intuition fails, requires a structured procedure (pdf 21–22).
- Data are collected only *after* the model, query and estimand are fixed, unlike the traditional approach with no causal model (pdf 22).
- Pearl is an "outspoken skeptic" of AI researchers who want to skip model-building and rely on data alone. Information on effects of interventions is not in raw data unless collected by controlled experimental manipulation. With a causal model, one can often predict an intervention's result from intervention-free data (pdf 22).
- Counterfactuals are the hardest queries for AI. Pearl says any query about the mechanism by which causes transmit effects, the prototypical "Why?" question, is a counterfactual question in disguise (pdf 22).
- *Adaptability:* the estimand is computed from the model alone, so it is good for any data compatible with the qualitative model, whatever the numerical relationships (pdf 22–23). Example: a learner predicting survival from patients' data moves to a hospital with different diet, hygiene and work habits. A pure data-fitter must retrain. A learner with a causal model of the drug, whose structure stays intact, can reuse the estimand with new data to get a new prediction function (pdf 23).

### Preview of chapters (pdf 23–26)
- **Ch. 1:** observation, intervention, counterfactuals form the Ladder of Causation; basics of causal diagrams (pdf 23).
- **Ch. 2:** how statistics "inflicted causal blindness" on itself; Sewall Wright, who drew the first causal diagrams in the 1920s (pdf 23).
- **Ch. 3:** Pearl's route from AI and Bayesian networks (tools letting computers think in "shades of gray") to causality. Includes an introduction to Bayes's rule; Bayesian networks still hold much of the mathematical foundation of causal diagrams (pdf 23–24).
- **Ch. 4:** the randomized controlled trial as a man-made tool for uncovering $P(L\mid do(D))$, a property of nature. It disassociates $D$ and $L$ from other variables $Z$ affecting both (confounding). A simple diagram-based solution to confounding is promised (pdf 24).
- **Ch. 5:** the smoking–lung cancer debate, where RCTs were unavailable (pdf 24).
- **Ch. 6:** paradoxes (Monty Hall, Simpson, Berkson). Pearl says almost all reflect clashes with causal intuition, and that intuition is grounded in causal, not statistical, logic (pdf 24).
- **Ch. 7:** automating answers to do-questions; the engine's yes/no and estimand; back-door adjustment, front-door adjustment, instrumental variables (pdf 24–25).
- **Ch. 8:** counterfactuals. Hume's 1748 definition of cause, which Lewis read as two definitions: regularity, and counterfactual (if the first object had not been, the second never had existed). Lewis argued the counterfactual one fits intuition better. Includes necessary and sufficient causes, with legal and climate examples (pdf 25).
- **Ch. 9:** mediation: is $D$'s effect on $L$ direct or via a mediator such as blood pressure? (pdf 25–26).
- **Ch. 10:** strong AI; Pearl believes causal reasoning is essential for machines to communicate with us about policies, experiments, explanations, theories, regret, responsibility, free will and obligations, and eventually to make moral decisions (pdf 26).

**Pearl's closing message:** "you are smarter than your data." Data do not understand causes and effects; humans do (pdf 26).

## Toy example (ours, not from the text)
100 patients; severity $Z$ affects both who takes drug $D$ and survival $L$. The drug has *no* effect in this made-up world.
- 50 severe: 40 take $D$, 10 do not. 50 mild: 10 take $D$, 40 do not.
- Survival rate: severe 0.2, mild 0.8, with or without $D$.
- **Seeing.** Takers: 50 people; survivors $40(0.2)+10(0.8)=8+8=16$, so $P(L\mid D)=16/50=0.32$. Non-takers: 50 people; survivors $10(0.2)+40(0.8)=2+32=34$, so $P(L\mid \text{not-}D)=0.68$. It looks as if the drug harms.
- **Doing.** Force everyone to take $D$: $50(0.2)+50(0.8)=10+40=50$ survivors, so $P(L\mid do(D))=0.5$. Force no one: also $0.5$. No effect.
- **Estimand-style recipe** (added step): $\sum_z P(L\mid D,z)P(z)=0.2(0.5)+0.8(0.5)=0.5$. This matches the forced result, using only observational data and the assumption that $Z$ is the only confounder, which is the role the text gives the estimand (pdf 20).

## Concepts
- [[do-operator]] — $P(L\mid do(D))$: distribution under forced intervention, unlike seeing $P(L\mid D)$ (pdf 14–15)
- [[causal-dag]] — Pearl's causal diagram: dots = variables, arrows = known or suspected "listens to" links (pdf 14, 19)
- [[ladder-of-causation]] — observation, intervention, counterfactuals as steps; only named here, developed in Ch. 1 (pdf 23)
- [[confounding-vs-selection-bias]] — here only confounding: other factors affecting both treatment and outcome distort comparisons (pdf 15, 24)
- [[propensity-score]] — listed among tools for managing sampling uncertainty (pdf 21)
- [[simpsons-paradox]] — named as a paradox revealing causal intuition (pdf 24)
- [[frequentist-vs-bayesian]] — not treated here; Bayesian networks are previewed only (pdf 23–24)
- [[causal-inference-engine]] (new) — Assumptions + Query + Data → yes/no, estimand, estimate (pdf 18)
- [[estimand]] (new) — formula from data quantities equivalent to the causal query, given the model (pdf 20)
- [[counterfactual]] (new) — retrospective "what if" about a changed past; judgments follow from a shared causal model (pdf 16)
- [[testable-implications]] (new) — statistical patterns, e.g. independence, that follow from the diagram and can be used to test it (pdf 19)
- [[randomized-controlled-trial]] (new) — man-made tool for obtaining $P(L\mid do(D))$ by breaking confounding (pdf 24)
- [[mediation]] (new) — splitting an effect into direct and indirect parts via a mediator (pdf 25)

## Canonical instances
- [[barometer-and-pressure]] — $B=kP$ cannot show direction; a falling barometer predicts but does not cause storms (pdf 11, 15)
- [[rooster-and-sunrise]] — correlation without causation; a counterfactual judgment shared by all (pdf 12, 16)
- [[drug-lifespan-example]] — running $D$, $L$, $Z$ example for do, estimand, confounding (pdf 14–20)
- [[joe-took-the-drug]] — counterfactual question about a patient's death (pdf 16)
- [[hume-lewis-two-definitions]] — regularity vs counterfactual definitions of cause (pdf 25)
- [[sewall-wright-path-analysis]] — 1920s precursor of causal diagrams (pdf 13)

## Bridges (candidates)
- [structural-analogy] estimand as a recipe fixed before data ↔ bayesian: model specified before fitting; the likelihood and prior are chosen before data arrive.
- [metaphor] "listens to" ↔ bayesian: conditional dependence in a directed graphical model, as in Bayesian networks, which Pearl says underlie causal diagrams (pdf 24).
- [structural-analogy] $P(L\mid D)$ vs $P(L\mid do(D))$ ↔ bayesian: conditioning on data vs setting a variable by intervention.
- [metaphor] adaptability of estimands ↔ bayesian: reusing structure across populations resembles hierarchical sharing, but the text does not say this.

## Questions this raises
- How exactly does the engine decide that $P(L\mid do(D))$ is answerable, and what formula comes out (Ch. 7 promises back-door, front-door, instruments)?
- If counterfactuals can never be confirmed by observation, how are the models behind them justified?
- When data contradict a testable implication, how do we decide which assumption to revise?
- How do Bayesian networks differ from causal diagrams (Ch. 3)?

## Reading notes
- Printed page numbers were not provided ("?"), so all references use the pdf page. The unit is pdf 9–26.
- The text refers to the figure both as "Figure I" and as "Figure I.1". I used only its caption and the box annotations in the text.
- Pearl presents his account of history (e.g. that causal vocabulary was virtually prohibited for more than half a century) as his own view; he introduces the language-gap explanation with "in my opinion" (pdf 11).
- The Toy example and the "added step" are ours, not from the source.
