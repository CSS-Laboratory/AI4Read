---
id: grimmer-2022-textasdata/ch22-principles
work: grimmer-2022-textasdata
unit: Chapter 22. Principles of Inference
pages: 369-380
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Principles of Inference

## L0 — One line
Prediction and causal inference are distinct inferential tasks with different assumptions, goals, validation and use of features, and researchers must say which one they are doing.

## L1 — The gist (≤ 120 words)
The chapter opens the book's inference section. It defines inference as using a sample to estimate a quantity in a well-defined, possibly counterfactual, population. It asks how two inferential tasks differ: predicting outcomes that will happen, and estimating outcomes under interventions. Prediction relies on the past relationship continuing, and its answers are eventually observed. Causal inference puts identification first, and the counterfactual is never observed. The two differ in goals, validation and treatment of features. Partial-equilibrium experiments may not tell us about general-equilibrium effects. Forecasts can be undone by strategic responses (Lucas critique). The distinction matters because the right assumptions and checks depend on the task.

**Prerequisites:** sampling and supervised learning; regression; treatment/control and confounding; the idea of a counterfactual outcome. Quick glosses for L0–L2: *identification* = what the data could reveal in principle with infinite data; *counterfactual* = the outcome if only the intervention had been different; *partial vs general equilibrium* = treating one unit vs treating the whole group; *Lucas critique* = actors who know the past response change behaviour in anticipation; *pre-treatment covariate* = a variable not caused by the intervention.

## L2 — Key ideas (5–10 bullets)
- Inference here means estimating a quantity in a population beyond the sample, so it needs stronger assumptions than discovery or measurement (p. 369).
- Forecasting needs an assumption that is unverifiable before the outcome is seen: past feature–outcome relationships continue into the future (p. 370).
- Prediction and causal inference differ on four points: identification vs estimation, goals, validation, and features (p. 372).
- Causal inference puts identification first and builds research designs for it. Prediction often puts estimation first, because outcomes will eventually be seen (pp. 372–373).
- Predictions are checked against realized outcomes. Causal effects can never be checked directly, so validation is indirect: identification checks, sensitivity analysis, alternative estimators (pp. 374–375).
- Features are tools in prediction. In causal inference they split into treatments and covariates, and only pre-treatment covariates can be included, and variables that induce bias, such as colliders (variables with a dependence structure that can make bias worse), should be avoided (p. 376).
- Partial-equilibrium RCT results may not carry over to general equilibrium (pp. 378–379).
- Predictions can be invalidated when actors strategically respond to the forecast (Lucas critique) (p. 379).

## L3 — Walkthrough

**Chapter introduction (p. 369).** The authors define inference narrowly: using a sample to estimate a quantity in a well-defined, possibly counterfactual, population. In discovery and measurement the goal was a useful function of high-dimensional data for the documents in hand. Inference makes claims about a broader population and therefore needs stronger assumptions (p. 369).

### 22.1 Prediction (pp. 370–371)
- **Prediction** asks what outcome we expect for units from a distinct population (p. 370).
- It looks like supervised learning but differs. In supervised learning we had assumed we could randomly sample from the population of interest, because we had already observed all units. In expectation, sample relationships then reflect population relationships (p. 370).
- In prediction to a new population, we cannot yet sample from it. The most common case is **forecasting**, and we cannot sample from the future (p. 370).
- So forecasting needs an extra assumption: the past relationship between outcome and features continues into the future. It is unverifiable before the outcome is observed. We can creatively approximate the assumption with our data, but cannot test it until we observe the actual units (p. 370).
- A random split of already-observed units justifies treating training and test relationships as the same on average. Forecasting has no such justification (p. 370).
- Forecasting therefore requires that prior predictive performance indicate future success. In social science data this is a strong assumption, particularly for rare events and for processes that may change rapidly (p. 370).
- **Example: presidential election forecasts.** Forecasters model the relationship between polls and past election results. They apply it to the current polls. The strong assumption is that the polls–outcome relationship found before also holds now. Accuracy in past elections does not guarantee accuracy later (pp. 370–371).
- Good predictive features must be predictive, available at prediction time, and likely to keep the same relationship out of population (p. 371).
- **Example: the 2020 economy.** Economic conditions relate to incumbents' reelection chances. Forecasters were unsure how to treat the COVID-19 downturn. The public might excuse Trump, because part of the contraction was deliberate. It might instead blame him for the response. At the time, no data were available to directly test which relationship would hold (p. 371).

*Intuition note.* A forecast depends on the assumption that tomorrow works like yesterday. You cannot test that assumption until the outcome is observed.

### 22.2 Causal inference (pp. 372–376)
Causal inference asks how outcomes differ if we intervene, that is, how the outcome would differ if only the intervention changed (p. 372). It may look like prediction of a response outside the data. The authors say conflating the two has caused confusion in computational social science. They list four differences (p. 372).

**22.2.1 Identification first (pp. 372–373).**
- Heuristically, parameters are **identified** if datasets map uniquely to parameter values. Identification concerns what could be learned with infinite data (p. 372).
- Identification assumption for prediction: the data in hand are useful for out-of-sample data. For causal inference: no background confounders associated with treatment assignment, so the observed association represents the unobserved counterfactual population (p. 372).
- **Estimation** concerns how we characterize the observed data: functional forms and model fitting, e.g. linear regression, Lasso, Ridge (p. 372).
- Causal scholars prioritize identification. Its assumptions are often unverifiable, and without identification no estimator can reliably recover the right parameters (p. 373).
- Prediction scholars often put estimation first, because they will eventually see whether they were right. Predictions are often made even if identification assumptions are violated (p. 373).
- Causal scholars construct designs to make identification more likely. Randomized experiments are the gold standard because they identify effects under weaker assumptions (p. 373).
- Design still matters in prediction. Deciding which data to include, e.g. whether the 1932 US election helps forecast 2020 (probably not), is an identification assumption (p. 373).

**22.2.2 Goals (pp. 373–374).**
- Prediction estimates the outcome for a unit outside the forecasting population. Causal inference estimates how an intervention affects an outcome. Doing well at one does not imply doing well at the other (p. 373).
- In prediction no theory is needed to include a feature. A feature is useful if it improves the out-of-sample estimate. Accurate predictive models can still suggest misleading explanations, since "why" and "what if" questions are causal (pp. 373–374).
- An **intervention** is a feature of the world that could plausibly be changed. A causal effect occurs when changing only it changes the unit's outcome. The counterfactual is never observed, so designs and models aim to make observed comparisons plausible estimates of it. Hence feature choice must be more selective (p. 374).

**22.2.3 Validation (pp. 374–375).**
- Predictions are compared with the realized truth. Two properties are named. **Accuracy** is the proportion guessed correctly. **Calibration** asks whether predicted probabilities match true probabilities (p. 374).
- Counterfactuals are never seen, so causal effects can never be validated directly, for groups or individuals. Holland (1986) calls this the fundamental problem of causal inference (p. 374).
- Indirect checks are: assessing identification conditions; **sensitivity analysis** (assume plausible confounding, ask how large it must be to change the finding); and using different estimation strategies to test robustness to assumptions (pp. 374–375).
- The computer-science **shared task** (new methods beat old ones on the same dataset) is much less useful for causal inference. Analysts must generate the whole dataset to know the true answer. The confounding built in may not match real confounding, so methods that win may do poorly in practice. Identification conditions are held fixed within a task, so shared tasks favour estimation over identification (p. 375).
- Simulations remain useful. Recovering correct estimates on data generated under a method's own assumptions is necessary but not sufficient. Simulations can also show how a method behaves when identification conditions are slightly perturbed. They cannot replace application-specific analysis of identification assumptions (p. 375).

**22.2.4 Features (pp. 375–376).**
- In prediction, features are tools. Lagged values are common, even when we do not know why they relate to future values (p. 376).
- In causal inference we separate **treatments** (the intervention) from **covariates** (used for more accurate, unbiased, precise estimation) (p. 376).
- In prediction we want any covariates that predict well, are available at prediction time and likely to be stable. In causal inference we must watch where covariates sit in the causal process (p. 376).
- Only **pre-treatment** covariates (not caused by the intervention) may be included (Montgomery, Nyhan, and Torres, 2018). Even among those, avoid variables that induce bias, such as **colliders** (Elwert and Winship, 2014) (p. 376).

*Intuition note.* In prediction, a feature that helps guess the outcome (and will be available and stable) is welcome. In causal work, a variable that helps guessing can still bias the effect estimate, so its causal position matters.

### 22.3 Comparing prediction and causal inference (p. 377)
- Both impute missing values. In prediction the missing value is eventually observed. In causal inference it never is (p. 377).
- **Ad campaign example.** "Who will buy?" is prediction. "Does our campaign induce purchase?" is causal, a question about counterfactual states (p. 377).
- "Will this individual buy if we show the ad?" is, at face value, a prediction question. The probability of purchase may be high even if the ad has little or no effect (p. 377).
- "Who is most responsive to the ad?" is a causal question about conditional average treatment effects, i.e. strata where the ad is very effective (p. 377).
- Prediction tools can help causal work. Machine learning is increasingly used to estimate **conditional average treatment effects**. These answer "what is the average effect for people with these characteristics?", which differs from "what is likely to happen to them?" (p. 377).

### 22.4 Partial and general equilibrium (pp. 378–379)
- **Partial vs general equilibrium** is the difference between an effect when treatment reaches one unit and when it reaches a whole group (p. 378).
- **Twitter 280 characters.** Twitter randomly gave a small set of accounts the 280-character ability (previously 140). Randomization made treated and untreated accounts comparable (p. 378).
- This does not make the experiment informative about a general rollout. Treated users tended to write series of high-engagement tweets highlighting their longer length. This is a partial effect that depends on only some users having the feature. Once all have it, novelty fades, and we would expect the effect to go away (p. 378; Jaidka, Zhou, and Lelkes, 2019).
- Analogies: job training gives a competitive advantage that vanishes if all workers are trained, so wages may not rise. A college degree's signalling value vanishes if everyone attends (p. 378).
- RCTs are almost exclusively designed to estimate partial-equilibrium effects, yet many important questions are general-equilibrium ones (p. 379).
- **Campaign message RCT** (Kalla and Broockman, 2018). Compare one message with none. A null effect suggests this message, given the rest of the campaign, is not very effective. Concluding that campaign messages in general do not work is a logical error. Reactions could differ substantially if a campaign stopped messaging altogether (p. 379).
- **Prediction analogue.** Historical relationships may fail if the forecast itself changes behaviour. Example: a platform predicts whether a political advertiser will follow campaign rules. Strategic actors may game the method, and it stops being predictive. This is the **Lucas critique** (Lucas, 1976): actors who know past responses alter behaviour in anticipation (p. 379).

*Intuition note.* An experiment on a few people can hide effects that appear only when everyone is treated. A forecast that people learn about can change the behaviour it was built on.

### 22.5 Conclusion (p. 380)
Understanding the specific inferential task determines how to infer. Computer scientists have emphasized prediction, social scientists causal inference. Both are essential. Researchers must be clear which task they undertake, because the assumptions and validations differ. The next chapter characterizes them for prediction (p. 380).

## Toy example
(Ours, not from the text.) An ad campaign, 100 people in each of two groups.

| Group | P(buy) without ad | P(buy) with ad | Effect of ad |
|---|---|---|---|
| A | 0.80 | 0.82 | 0.82 − 0.80 = 0.02 |
| B | 0.10 | 0.50 | 0.50 − 0.10 = 0.40 |

- **Prediction question:** "Who will buy if shown the ad?" A: 0.82 × 100 = 82 buyers. B: 0.50 × 100 = 50 buyers. Group A looks best.
- **Causal question:** "Who is most responsive?" Extra buyers: A: 0.02 × 100 = 2. B: 0.40 × 100 = 40. Group B is far more responsive.
- Ranking by predicted purchase (A first) is the reverse of ranking by effect (B first). In real data the "without ad" column is the unobserved counterfactual for treated people, so the effect column can only be estimated through design.

## Concepts
- [[inference]] (new) — using a sample to estimate a quantity in a well-defined, possibly counterfactual, population (p. 369)
- [[prediction-forecasting]] (new) — estimating the outcome for units outside the sample population. Forecasting assumes past relationships continue (pp. 370, 373)
- [[causal-inference]] (new) — estimating how the outcome differs if only the intervention changed (p. 372)
- [[identification-vs-estimation]] (new) — identification: what infinite data could reveal. Estimation: how the observed data are characterized (p. 372)
- [[fundamental-problem-of-causal-inference]] (new) — counterfactual outcomes are never observed, so effects cannot be directly validated (p. 374)
- [[accuracy-calibration]] (new) — accuracy: share guessed correctly. Calibration: predicted probabilities match true ones (p. 374)
- [[sensitivity-analysis]] (new) — assume plausible confounding and assess how large it must be to change a finding (p. 375)
- [[shared-task]] (new) — evaluating methods by comparing performance on one dataset. Less useful for causal methods (p. 375)
- [[pre-treatment-covariate-collider]] (new) — covariates must not be consequences of treatment. Colliders can worsen bias (p. 376)
- [[conditional-average-treatment-effect]] (new) — average effect for individuals with a given set of characteristics (p. 377)
- [[partial-vs-general-equilibrium]] (new) — effect when one unit is treated vs when the whole group is treated (p. 378)
- [[lucas-critique]] (new) — actors who know past responses alter behaviour in anticipation of the forecast (p. 379)
- [[text-as-data-validation]] — here contrasted: predictions validated against outcomes, causal effects only indirectly (pp. 374–375)

## Canonical instances
- [[presidential-election-forecasting]] — polls–outcome relationship assumed to carry over to the new election (pp. 370–371)
- [[covid-2020-economy-forecast]] — unclear how the economic downturn would link to incumbent performance (p. 371)
- [[ad-campaign-predict-vs-cate]] — "who will buy?" vs "who responds?" (p. 377)
- [[twitter-280-characters]] — partial-equilibrium novelty effect from a small randomized rollout (p. 378)
- [[job-training-college-signaling]] — advantages that vanish when universal (p. 378)
- [[campaign-message-null-effect]] — a null effect of one message does not show campaigns are ineffective (p. 379)
- [[platform-ad-compliance-forecast]] — strategic gaming of a prediction method (p. 379)

## Bridges (candidates)
- [structural-analogy] Lucas critique (actors adapt to a known rule) ↔ political-science: strategic (sophisticated) voting — in both, behaviour responds to anticipated rules or outcomes.
- [structural-analogy] Economic conditions predicting incumbent reelection ↔ political-science: retrospective voting — the forecast feature mirrors the voter behaviour theory.
- [structural-analogy] Partial vs general equilibrium (value of an edge disappears when universal) ↔ political-science: selective incentives and free riding, where a benefit depends on who else has it.

## Questions this raises
- Which assumptions and validations does the next chapter give for prediction?
- How can we judge whether a past relationship will "continue" when the world changes, as in 2020?
- When can an RCT answer a general-equilibrium question, if ever?
- How should sensitivity analysis be reported so readers can judge plausible confounding?

## Reading notes
- Printed page numbers equal pdf numbers (offset 0). No equations or exercises in this unit.
- Footnote 1 (p. 369/380) says parts of the chapter are drawn from Grimmer, Roberts, and Stewart (2021).
- Probable misprint, p. 375: "show that our findings are not robust to particular assumptions". Context suggests "are robust". I reported it as robustness checks.
- Misprint p. 378: "equilbrium".
- The 1932/2020 election example and the Twitter example are used as the author gives them. The source gives no quantitative results for them (only the 140/280-character limits).
