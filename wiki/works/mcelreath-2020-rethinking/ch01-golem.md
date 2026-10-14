---
id: mcelreath-2020-rethinking/ch01-golem
work: mcelreath-2020-rethinking
unit: "Chapter 1. The Golem of Prague"
pages: 1-17
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Golem of Prague

## L0 — One line
Statistical models are powerful but unwise "golems", so researchers should learn to build and criticise several models (using Bayesian analysis, multilevel models and information criteria) instead of picking pre-made tests to falsify null hypotheses.

## L1 — The gist (≤ 120 words)
The chapter asks what statistical inference is for and why a menu of classical tests is not enough. McElreath argues that deductive falsification almost never works in science. Hypotheses do not map one-to-one onto models, measurement is error-prone, and most hypotheses are quantitative rather than all-or-nothing. McElreath describes statistics as a branch of engineering and urges us to build, compare and check explicit models. He introduces three tools: Bayesian data analysis, multilevel models, and model comparison with information criteria. The point is that readers who understand how their models work are better placed to interpret their output and have a good chance of noticing and diagnosing failures. The chapter ends with a roadmap of the book's four parts.

**Prerequisites:** basic idea of a hypothesis test (null hypothesis, p-value); what a regression is; basic probability as frequency.

## L2 — Key ideas (5–10 bullets)
- Scientific models are "golems": obedient, powerful, without wisdom. Classical tests tend to be inflexible and fragile in new contexts. Without understanding the machinery you cannot interpret the output (pp. 1–4).
- The author argues that the aim of inference is not just to test null hypotheses. The opposite belief is a kind of "folk Popperism", and deductive falsification is impossible in nearly every scientific context (p. 4).
- Hypotheses, process models and statistical models are related many-to-many. Rejecting or retaining a null model therefore says little about a hypothesis (pp. 5–7).
- Measurement error and continuous (quantitative) hypotheses further break the "black swan" logic. Falsification in practice is consensual, not logical (pp. 7–10).
- Bayesian inference counts the ways things can happen under stated assumptions. It treats randomness as a property of information, not of the world (pp. 11–12).
- In multilevel models a parameter can be regarded as a placeholder for a missing model. The author argues they deserve to be the default regression (pp. 13–14).
- Information criteria estimate predictive accuracy, help with overfitting, and allow comparison of several non-null models (pp. 15–16).

## L3 — Walkthrough

**Opening fable (p. 1).** In the learned Prague of Rudolph II, one version of the golem legend has Rabbi Judah Loew build a clay golem to defend the city's Jews. It was animated by *emet* ("truth") on its brow. It always does exactly what it is told. It is powerful, lacks wisdom, and eventually caused innocent deaths. Judah wiped one letter to make *met* ("death") and shut it down (p. 1).

### 1.1 Statistical golems
- Scientific models are the scientist's golems. They are, the author says, neither true nor false, but constructs engineered for a purpose. Their logic can reveal hidden implications or produce silly, dangerous behaviour (pp. 1–2).
- Even a t-test is a small golem that does an exact calculation the same way (nearly) every time. Some phenomena (selection strength, neutrino speed, species counts in the Amazon) can only be measured through models. The golem is a prosthesis but has no wisdom: it cannot tell when the context is inappropriate (p. 2).
- McElreath's view: statistics is "neither mathematics nor a science, but rather a branch of engineering", with common design principles producing many specialised applications (p. 3).
- Intro courses give a zoo of pre-made "tests", often organised as a decision tree (Fig. 1.1: data type, question type, parametric assumptions → procedure name). Students use these without knowing the models underneath. The author compares this to teaching engineering backwards, and says it is not the students' fault (pp. 2–3).
- For some people the pre-made toolbox is all they need: within well-tested contexts and a few appropriate procedures, a lot of good science can be done, as plumbers do useful work without knowing much fluid dynamics. Serious trouble begins in innovative research; the author compares this to getting hydraulic engineers by promoting plumbers (p. 3).
- Classical procedures are **inflexible** (few ways to adapt to a context) and **fragile** (fail unpredictably in new contexts). Examples: Fisher's exact test applies exactly to a very narrow context but is regularly used whenever cell counts are small; the author has never seen it used appropriately except by Fisher. Linear regression can fail "in spectacular ways" with substantial measurement error on predictors. Nearly always one can do better than ordinary regression, largely because of overfitting (Ch. 6) (p. 3).
- If we keep adding new tools there will soon be far too many to keep track of. Researchers need a unified theory of "golem engineering". Every major branch of statistical philosophy has one, but it is never taught in introductory courses and often not in advanced ones either (pp. 3–4).

*Intuition note.* A test is a fixed machine that cannot check its own fit to your problem. If you do not know how it is built, you cannot interpret its output.

### 1.2 Statistical rethinking
- The book works through the computational details of each procedure because you cannot interpret a golem's output without knowing how it processes information. It also needs some "statistical epistemology": how models relate to hypotheses and mechanisms (p. 4).
- **The tacit belief (author's target):** the proper objective of inference is to test null hypotheses, because Popper said science advances by falsification. The author calls this "folk Popperism". He grants that seeking evidence that could embarrass our ideas is a normative standard most scholars accept. He also says Popper himself recognised that science is not described by the falsification standard (p. 4).
- The author's claim: deductive falsification is impossible in nearly every scientific context, for two reasons: (1) hypotheses are not models; (2) measurement matters (p. 4). Hence, the author says, the scientific method cannot be reduced to a statistical procedure (p. 4).
- *Rethinking box:* NHST usually falsifies a null hypothesis, not the research hypothesis. This seems the reverse of Popper's philosophy (p. 5).

**1.2.1 Hypotheses are not models (pp. 5–7).**
- Any attempt to falsify a hypothesis uses a model, at least a tacit measurement model. All models are false. So rejecting a model derived from a hypothesis does not let you deduce that the hypothesis is false (p. 5).
- *Example: neutral evolution (Fig. 1.2).* Two verbal hypotheses: H0 "evolution is neutral", H1 "selection matters". Each corresponds to several detailed process models (p. 5):
  - P0A: neutral, equilibrium. P0B: neutral, non-equilibrium (population size fluctuates).
  - P1A: constant selection. P1B: fluctuating selection (p. 5).
- A process model becomes a statistical model by deriving the expected distribution of some statistic, such as the histogram of allele frequencies (p. 5). P0A yields a power law, giving M_II. P1A predicts something quite different, M_III. But P1B also implies M_II, and in Fig. 1.2 P0B links to M_I (pp. 5–6).
- Three lessons (p. 6): (1) a statistical model M may correspond to more than one process model P; (2) a hypothesis H may correspond to more than one P; (3) an M may correspond to more than one H.
- Consequences if P0A is the null, with data from M_II (pp. 6–7):
  - Rejecting the null does not show selection matters, since other neutral models predict different distributions.
  - Failing to reject does not show evolution is neutral, since some selection models expect the same distribution.
- The author says the same worry applies to routine models. A "null" of zero average group difference can be consistent with data in many ways. This motivates considering unobserved variables and sampling bias (p. 7).
- **Remedy:** compare predictions of more than one process model. P0A and P1B give similar power-law allele distributions but very different predictions for changes in allele frequency over time (p. 7).
- *Rethinking box (entropy):* normal, binomial, Poisson and other exponential-family distributions are maximum-entropy distributions (Ch. 9). So one can no more infer evolutionary process from a power law than developmental process from normally distributed height. These distributions still allow useful statistical work without identifying the process (p. 7).

*Intuition note.* Many different mechanisms can produce the same pattern in data. So a match (or mismatch) between the data and my null cannot, by itself, tell you which mechanism or hypothesis is right.

**1.2.2 Measurement matters (pp. 7–9).**
- Falsification logic is *modus tollens*: if H entails observation D and D is not found, H is false. Finding D tells nothing certain about H, since other hypotheses may predict D (p. 7).
- *Swan fable.* H0: "All swans are white." No number of white swans proves it, but one black swan refutes it (pp. 7–8). The author calls this "seductive" but misleading for two reasons: observations are error-prone, and most hypotheses are quantitative (p. 8).
- **1.2.2.1 Observation error.** Swan colour is easy to judge, but in most science we are unsure whether a disconfirming result has been detected (p. 8).
  - *Ivory-billed Woodpecker.* In 2005 Cornell ornithologists claimed evidence of a bird thought extinct (H0: it is extinct). Many doubted the evidence. Despite searches and a $50,000 reward, no evidence satisfying all parties had emerged by 2015. There are false positives and false negatives. Those who already believe it extinct will always be suspicious of a claimed falsification; those who believe it alive tend to count even the vaguest evidence as falsification (p. 8).
  - *FTL neutrinos.* In September 2011 a large team reported neutrinos travelling from Switzerland to Italy slightly faster than light. The dominant reaction was not that Einstein was wrong but a question about how the team had mis-measured, and the team itself asked others to check. Reasons for suspicion: measuring a neutrino's start consumes it; the detected difference was tiny relative to signal latencies; the "measurement" was a statistical-model estimate. By 2013 the community was unanimous that it was error (a poorly attached cable, among other things). Supernova neutrinos agree with Einstein (pp. 8–9).
  - Key dilemma in both: is the falsification real or spurious? Popper himself knew measurement limits. The author's reading of history is that such measurement problems are the norm, not the exception (p. 9).
- **1.2.2.2 Continuous hypotheses.** Typical hypotheses say, for example, that 80% of swans are white, or that black swans are rare. A black swan then does not refute them. The task is to estimate and explain the distribution, not to disprove (p. 9).
  - **Objection (imagined):** such hypotheses are not good scientific hypotheses because they are hard to disprove. **Author's reply:** then most important questions are not good hypotheses, so the definition of "good hypothesis" is not useful. Comparisons between hypotheses are often probabilistic, of degree and not kind (p. 9).

**1.2.3 Falsification is consensual (pp. 9–10).** Communities do come to regard some hypotheses as false (caloric theory, geocentrism), and evidence often, not always, plays a role. But falsification is "always consensual, not logical". Textbooks sometimes rewrite history to look like logical falsification. The author says this may hurt scientists, make science an easy target, and exaggerate how definitive knowledge is (p. 10).

### 1.3 Three tools for golem engineering (p. 10)
- Instead of mimicking falsification: model. Models can serve as tests but also to measure, forecast and argue. The author says you will eventually "wreck Prague", but a good golem engineer will at least notice and has a good chance of working out what went wrong (p. 10).
- Three tools, deeply related: (1) Bayesian data analysis, (2) multilevel models, (3) model comparison using information criteria. Understanding comes only with implementation, so the book focuses mostly on code (p. 10).

**1.3.1 Bayesian data analysis (pp. 10–13).**
- Probability theory lets us use chance (Fortuna) as a servant of wisdom (Minerva). Bayesian analysis does so most fully (p. 11).
- "In modest terms", Bayesian inference is counting the ways things can happen under our assumptions. Things that can happen more ways are more plausible. Because probability is a calculus for counting, it can represent plausibility for events and for parameters. Once assumptions are set, the processing is purely logical (p. 11).
- **Frequentist** approach (author's description): probabilities are defined by frequencies of countable events in very large samples. Uncertainty comes from imagined resampling. Parameters and models cannot have probability distributions, only measurements can. The distribution of measurements is the **sampling distribution**. Resampling is never done and often makes no sense (e.g. song-bird diversification in the Andes). **Fisher:** populations in significance tests have "no objective reality", being the statistician's imagination (p. 11). The author adds that imagined resampling, though a useful device in some contexts such as controlled greenhouse experiments, is just an assumption of the model and is "just as fantastical" as the Bayesian gambit of using probability for all uncertainty (p. 11). He says Bayesian probability includes frequentist probability as a special case (p. 11).
- *Galileo and Saturn (Fig. 1.3).* The blurred image has uncertainty about shape but no sampling variation: looking again gives the same image. The sampling distribution is constant, so frequentist inference has trouble starting. Bayesian inference proceeds because deterministic "noise" can be modelled with probability if probability is not identified with frequency. Image reconstruction is dominated by Bayesian algorithms (pp. 11–12).
- Even when Bayesian and frequentist answers coincide, Bayesian golems do not justify inferences by imagined repeat sampling. Randomness is "a property of information, not of the world". The coin toss is random from the golem's perspective (p. 12).
- This description invokes no one's "beliefs". The tradition of using it as a normative account of rational belief is called Bayesianism; the author says the book neither describes nor advocates it (p. 12).
- *Rethinking: probability is not unitary.* Axioms are shared, but interpretations differ (de Finetti, Cox, Savage). The book mainly follows the "logical" Cox (Laplace-Jeffreys-Cox-Jaynes) interpretation, fully developed in Ch. 9 (pp. 12–13).
- **Pedagogical advantage:** many people find Bayesian reasoning more intuitive. Many scientists, even instructors, read p-values as posterior probabilities and confidence intervals as Bayesian ones; the reverse mistake seems rare. This does not make Bayesian models more correct (p. 13).
- *Rethinking: history.* Bayesian methods were used in the late 1700s and 19th century. After World War I, anti-Bayesians such as Fisher marginalised them. Fisher wrote that the theory of inverse probability (the old name for Bayesian analysis) is founded upon an error and must be wholly rejected (p. 13). Acceptance grew in the later 20th century, and computational advances from the 1990s drove rapid uptake. Bayesian methods remain computationally expensive, so approximations stay important (p. 13).

*Intuition note.* Bayesian probability scores how many ways each possibility can happen given your assumptions. This works even when there is no sampling variation to imagine, as with Saturn's blurred image, which looks the same every time.

**1.3.2 Multilevel models (pp. 13–15).**
- "Turtles all the way down": a parameter can be regarded as a placeholder for a missing model. Embedding a model of how the parameter gets its value gives several levels of uncertainty, a multilevel model (also hierarchical, random/varying/mixed effects) (pp. 13–14).
- Four complementary reasons to use them (p. 14): (1) adjust for repeat sampling; (2) adjust for imbalance in sampling; (3) study variation among groups; (4) avoid averaging, since pre-averaging removes variation and "manufactures false confidence".
- Scope is broad: imputation, measurement error, factor analysis, some time-series, spatial and network regressions, and phylogenetic regressions are special cases. Single-level models then look like components (p. 14).
- **Author's claim:** multilevel regression deserves to be the default; papers not using it should justify that. Perhaps the most important reason, in his view, is that even well-controlled treatments interact with unmeasured aspects of the units, giving variation in treatment effects (pp. 14–15).
- Costs: fitting and interpreting are harder, and many researchers treat the software as a black box. The author expects this to change, as it did for multiple regression (p. 15).
- *Rethinking:* from the early 1960s John Tukey built multilevel real-time election-forecasting models for NBC, used through 1978 (p. 15).

**1.3.3 Model comparison and information criteria (pp. 15–16).**
- Information criteria (from the 1960s–70s) compare structurally different models by *future predictive accuracy*. AIC is the most famous; DIC and WAIC are also discussed. They build a model of the prediction task, so they depend on assumptions and "are still golems". They draw on information theory (crash course in Ch. 6) (p. 15).
- They address two difficulties (pp. 15–16):
  1. **Overfitting.** Mantra: "fitting is easy; prediction is hard." Future data will not be exactly like past data, so models cannot be judged only on fit (pp. 15–16).
  2. They allow comparing multiple **non-null** models on the same data. Some contexts (social networks, phylogenies, neutral evolution) have no unique null, so explicit comparison is mandatory (p. 16).
- Information criteria are comparatively young. There is no consensus on which metric is best, but they are already used in prominent debates (p. 16).
- *Rethinking: Neanderthals.* A 2010 draft Neanderthal genome shared more DNA sequences with non-African than with African humans. This fits interbreeding, but also fits ancient population structure in Africa. More than one process explanation exists, so model comparison is needed (p. 16).

### 1.4 Summary (pp. 16–17)
Instead of black-box null-hypothesis tests, build and analyse several non-null models. Book plan:
1. Ch. 2–3: Bayesian inference and its calculation tools, with a purely logical view of probability.
2. Ch. 4–7: multiple linear regression as a Bayesian tool, with plotting, interactions, overfitting, and information theory in Ch. 6.
3. Ch. 8–11: generalised linear models. Ch. 8 introduces MCMC, Ch. 9 maximum entropy, Ch. 10–11 the models.
4. Ch. 12–14: multilevel models, linear and generalised, including measurement error, missing data and spatial correlation via Gaussian processes.
Ch. 15 returns to issues of this chapter. Practice problems appear at the end of chapters, with solutions online (p. 17).

## Toy example (ours, not from the text)
Idea: two process models can give the same statistic, but a different statistic separates them (cf. P0A vs P1B, p. 7).
- Process A: a fair coin, independent tosses. Process B: a coin that strictly alternates H, T, H, T, …
- Observe 10 tosses and take the statistic "proportion of heads". Both models predict 0.5. Process B gives exactly 5 heads (HTHTHTHTHT), and Process A's expected proportion is 0.5. So the match cannot separate them.
- Take a different statistic: the number of runs (maximal blocks of equal outcomes). Process B gives 10 runs.
- Process A: runs = 1 + (number of adjacent pairs that differ). There are 9 adjacent pairs, each differing with probability 0.5. Expected runs = 1 + 9 × 0.5 = 5.5.
- So 5 heads "fails to reject" a fair-coin null yet cannot show the coin is fair. A run count of 10 tells the models apart. Comparing two models' predictions across statistics is the remedy the chapter recommends.

## Concepts
- [[statistical-golem]] (new) — a model or procedure that does exactly what it is programmed to do, powerful and without wisdom (p. 1).
- [[modus-tollens-falsification]] (new) — if H entails D and D is absent, H is false; the logic of deductive falsification (p. 7).
- [[null-hypothesis-significance-testing]] (new) — testing a null hypothesis; the author notes that this usually falsifies a null rather than the research hypothesis, which seems the reverse of Popper's philosophy (p. 5).
- [[hypotheses-vs-models]] (new) — hypotheses, process models and statistical models are linked many-to-many (p. 6).
- [[frequentist-vs-bayesian]] — frequentist: probability as frequency, uncertainty via imagined resampling; Bayesian: probability as plausibility, for any uncertainty (p. 11).
- [[probability-as-extended-logic]] — the "logical" Cox (Laplace-Jeffreys-Cox-Jaynes) interpretation the book mainly follows (p. 12).
- [[sampling-distribution]] (new) — distribution of a measurement under imagined repeated sampling (p. 11).
- [[hierarchical-model]] — multilevel model; a parameter is a placeholder for a missing model (p. 14).
- [[information-criteria]] (new) — AIC, DIC, WAIC: estimate predictive accuracy, not just fit (p. 15).
- [[overfitting]] (new) — a model unaware that future data will differ from past data tends to predict worse than it could, so fit to the data alone is not a good guide (pp. 15–16).
- [[principle-of-indifference-maximum-entropy]] — exponential-family distributions are maximum-entropy; only mentioned here (p. 7).

## Canonical instances
- [[neutral-evolution-debate]] — shows many-to-many hypothesis–model relations (pp. 5–7).
- [[black-swan]] — modus tollens ideal and its limits (pp. 7–9).
- [[ivory-billed-woodpecker]] — falsification under observation error (p. 8).
- [[ftl-neutrinos]] — apparent falsification of relativity attributed to measurement error (pp. 8–9).
- [[galileo-saturn]] — uncertainty without sampling variation (pp. 11–12).
- [[fishers-exact-test]] — a narrowly valid test used outside its context (p. 3).
- [[tukey-election-forecasting]] — early multilevel application (p. 15).
- [[neanderthal-interbreeding]] — same data fit rival process explanations (p. 16).

## Bridges (candidates)
- [same-math] Multilevel model: parameter as placeholder for a model ↔ bayesian: hierarchical model — parameters drawn from a higher-level distribution.
- [structural-analogy] Many process models per statistical model (p. 6) ↔ causal inference: non-identifiability — different mechanisms yield the same observed distribution.
- [structural-analogy] Overfitting versus predictive accuracy (p. 15) ↔ bayesian: cross-validation/LOO/WAIC — judge on out-of-sample prediction.
- [metaphor] Randomness is a feature of the golem's information, not of the coin (p. 12) ↔ bayesian: probability as extended logic — probability describes information.

## Questions this raises
- If deductive falsification is rarely possible, what concrete rules let a community decide that a model is adequate or wrong?
- How should one choose which candidate process models to compare, and which statistics to compare them on?
- When Bayesian and frequentist procedures give the same numbers, what practical difference does the interpretation make?
- How do information criteria build a model of the prediction task, and what assumptions do they depend on?

## Reading notes
- Printed page = pdf page − 14. The unit is printed pp. 1–17. Printed p. 18 (pdf 32) is blank.
- The text layer is clean. Footnote markers (e.g. 1–34) appear in the text but the footnote texts were not in these pages, so nothing in the digest relies on them.
- Fig. 1.1 (flowchart) and Fig. 1.2 were checked in the images. In Fig. 1.2 the lines run P0A→M_II, P0B→M_I, P1A→M_III, P1B→M_II, which matches the text on p. 6 for P0A, P1A and P1B (the text does not mention M_I).
- These pages contain no exercises, so there is no Exercises section. The text says practice problems appear at the end of each chapter (p. 17), but they are not reproduced in these pages.
