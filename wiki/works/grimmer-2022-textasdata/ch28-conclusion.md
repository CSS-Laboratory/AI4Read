---
id: grimmer-2022-textasdata/ch28-conclusion
work: grimmer-2022-textasdata
unit: Chapter 28. Conclusion
pages: 462-468
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Conclusion: Text as Data for Social Science Tasks

## L0 — One line
Text-as-data methods help social science most when they are organised around social-science tasks, used iteratively and sequentially, judged by task-specific validation rather than by faith in any one model, and sold with modesty.

## L1 — The gist (≤ 120 words)
The chapter asks how to use text-as-data tools well, and whether the book's principles reach beyond text. The authors argue for four things. Methods from computer science must be repurposed for social-science tasks: discovery, measurement, inference. Research should be iterative and sequential. We should stay skeptical about the true data-generating process and validate against the task, with humans in the loop. The same principles should apply to images, speech and video. They end with a warning against boom-and-bust cycles: no method removes the problems of concept formation, measurement and causal inference.

**Prerequisites:** the book's task vocabulary (discovery, measurement, causal inference, prediction); held-out model fit; pre-registration; basic ideas of validation.

## L2 — Key ideas (5–10 bullets)
- Methods built for computer-science goals (e.g. information retrieval) need repurposing, because social scientists want to characterise "the whole haystack", not find a needle (p. 464).
- Research tasks follow a project's trajectory: discovery, then measurement, then inference (causal or predictive). The authors say that, in their experience, this can make first serious projects more manageable and helps decompose existing ones (p. 464).
- Theory remains integral: it suggests conceptualisations, motivates measurement and helps interpret causal effects (p. 464).
- Iterative, sequential work tunes models to context, accumulates evidence, tests new hypotheses on new data, and may create incentives to replicate (p. 465).
- We should doubt that we ever have the correct model. Choose models by validation tied to their use, with humans in the loop, not by fit statistics alone (pp. 465–466).
- The framework is meant to apply to images, speech and video too, with the same basic principles (p. 467).
- New methods can improve work at each research stage but are not a panacea (pp. 463, 468). The authors call for humility, to avoid a boom-to-bust cycle (p. 468).

## L3 — Walkthrough

**Opening (pp. 462–463).** Text as data offers social scientists insight at a previously impossible scale, and new models make large datasets easier to analyse (p. 462). The authors restate three arguments:
1. Computer-science methods must be repurposed, and evaluated differently, for social-science problems.
2. Inference is best made iteratively and sequentially. Building the evidence base inductively from the datasets improves inferences, and working sequentially can improve the concepts, the measurements and the inferences.
3. We should keep a baseline skepticism ("agnosticism") about the true data-generating process. We therefore avoid validations that assume the correct model, and say that validations focused on the core task of interest are essential for judging whether models perform well for social-science tasks (p. 462).

They add that the principles extend to images, sound and video, where computer-science tasks differ from social-science tasks (p. 463). Text-as-data methods are "not a panacea". Challenges of causal inference, prediction and concept definition remain (p. 463).

**28.1.1 The focus on social science tasks (p. 464).**
- Unsupervised methods were developed for information retrieval, often evaluated by predictive accuracy on held-out data. Social scientists rarely care about prediction for unsupervised text. Models that predict better are sometimes worse at giving social-science insight, so the book is organised by task (p. 464).
- Tasks follow a project: *discovery* (new conceptualisations), *measurement* (assigning observations to categories), then *inference*. Inference is either causal (the effect of an intervention) or prediction (out-of-sample estimates) (p. 464).
- The authors say that, in their experience, deconstructing research into these stages can make daunting first research projects much more manageable, and that decomposing existing projects helps show what is driving inferences (p. 464).
- There is no theory chapter, but theory is integral: it can suggest conceptualisations, motivate measurement and aid the interpretation of causal effects. The authors reject the claim that big data ends theory. They argue the opposite: theory is essential for interpretation, and more data gives more stylised facts for building models (p. 464).

*Intuition note:* A model that is best at predicting held-out words may still give categories that mean little for your research question. So ask what you will use the model for, and judge it by that.

**28.1.2 Iterative and sequential nature (pp. 464–465).**
- *Iterative* building lets the analyst see how models apply in context and tune the feature representation and other model features. *Sequential* work accumulates evidence across studies. A hypothesis developed during one analysis can be tested on new data in the next design (p. 465).
- The authors say sequential work is more honest: papers are written as if deductive, but ideas are rarely created that way (p. 465).
- On "fishing" (analysis choices made to produce significance when the true difference is null): pre-registration can be useful, but does little about incentives to publish significant results. The authors think a sequential approach could create incentives to replicate, and to be replicated by others (p. 465).

*Intuition note:* Treat one study as a step. Hypotheses that come from the data can then be tested in the next study with fresh data.

**28.1.3 Model skepticism (pp. 465–466).**
- Language is complex and its representation needs simplifying assumptions. The models are "obviously wrong, but some are useful" for measuring quantities, suggesting conceptualisations and facilitating causal inference (p. 465).
- So model choice should not rest only on fit statistics, which rarely optimise for how social scientists use the model. Use validations tied to the intended use, often with humans in the loop (pp. 465–466).
- Humans in the loop serve validity and meaning. They also bring context and substance so that research is practical and ethical, remembering that the authors of the texts are humans, not just data points (p. 466).

*Intuition note:* Because our models are simplifications of language, fit statistics alone say little about whether a model serves your task. Validation tied to that task, often with humans in the loop, is what the authors recommend.

**28.2 Beyond text (p. 467).** The authors argue that new data sources and imported methods should be assessed for how they will be used in political science. Examples cited:
- Images: Torres (2019) on how protesters are depicted in press photographs.
- Speech: Kaufman, Kraft and Sen (2019) show that how Supreme Court justices speak can predict how they rule. Knox and Lucas (2021) give a general method for decomposing speech content. The authors say how things are said matters, and mention Obama's and Reagan's delivery.
- Video: Dietrich and Sands (N.d.) use New York City traffic cameras to measure reactions to randomly placed people of different identities.

The authors conclude that the same basic principles hold and that similar models can often be used (p. 467).

**28.3 Avoiding the cycle of creation and destruction (p. 468).**
- The pattern: a new method is hailed as a breakthrough; researchers rush to re-evaluate past claims; it fails its unrealistic promises; critics point out the gap; the "too-pessimistic" conclusion is that it was not useful, and it is discarded although still useful for narrow tasks (p. 468).
- Text as data has largely avoided this fate so far. The authors think this is due in part to early papers not over-promising (p. 468). They add that text is hard to work with and the new methods are useful, but cannot necessarily give a unified, comprehensive approach to all text-as-data problems (p. 468).
- No computing power or "big data" solves the fundamental challenges. Researchers must still conceptualise and measure, and causal inference remains a problem even with many rows. New methods can nonetheless improve work at each stage (p. 468).

## Toy example (ours, not from the text)
Two topic models, A and B, are fitted to the same corpus. We want to know which is better for *measuring* whether press articles describe protests as "disorderly".
- Held-out log-likelihood per word: A = −7.0, B = −7.2. By fit alone, A wins, since −7.0 > −7.2.
- Task validation: humans code 20 articles as disorderly or not. Model A's topic assignments agree with the humans on 11 articles, 11/20 = 0.55. Model B's agree on 16, 16/20 = 0.80.
- On the task of interest B is better, 0.80 > 0.55, although A has the better fit. Following the chapter, we choose B for this task. Fit and task performance can disagree, so we validate against the use (pp. 464–466).

## Concepts
- [[text-as-data-validation]] — here: validation tied to the task, with humans in the loop, not to model fit or an assumed correct model (pp. 465–466)
- [[social-science-tasks]] (new) — discovery, measurement, causal inference, prediction; the organising frame of the book (p. 464)
- [[iterative-sequential-research]] (new) — build evidence inductively from the data; test new hypotheses on new data in later designs (pp. 462, 465)
- [[model-skepticism]] (new) — baseline "agnosticism" about the true data-generating process; models are simplifications that can still be useful (pp. 462, 465)
- [[humans-in-the-loop]] (new) — human assessment of models for validity, context and ethics (p. 466)
- [[boom-bust-method-cycle]] (new) — hype, over-promise, disappointment, then discarding a method that is useful for narrow tasks (p. 468)

## Canonical instances
- [[torres-2019-protest-images]] (new) — machine learning on press photographs of protesters (p. 467)
- [[kaufman-kraft-sen-2019-justices-speech]] (new) — justices' manner of speaking predicts case rulings (p. 467)
- [[knox-lucas-2021-speech-decomposition]] (new) — general method for decomposing the content of speech (p. 467)
- [[dietrich-sands-traffic-cameras]] (new) — traffic-camera video to measure reactions to randomly placed people (p. 467)

## Bridges (candidates)
- [structural-analogy] Testing hypotheses from one analysis on new data in the next study ↔ held-out evaluation: both separate discovery from confirmation.
- [structural-analogy] Task-based validation over model fit ↔ political-science measurement validity: judge a measure by what it is meant to capture.
- [metaphor] Boom-to-bust cycle in methods ↔ technology hype cycles in general.

## Questions this raises
- What concrete validation (e.g. human coding of a sample) would suit each of the four tasks?
- How would sequential replication be rewarded in journals, given that pre-registration "does little" about publication incentives (p. 465)?
- Which of the book's models transfer to image, sound and video data, and which need new validation (p. 467)?
- If theory is "essential" for interpreting models, how should theory enter the discovery stage without fixing the concepts in advance (p. 464)?

## Reading notes
- Printed page = pdf page (462–468). The unit contains no equations or exercises.
- Section 28.1.2's heading is split across pp. 464–465.
- Dietrich and Sands is cited "N.d." (no date) in the source (p. 467).
- The text layer looks clean. I saw no OCR problems or misprints.
