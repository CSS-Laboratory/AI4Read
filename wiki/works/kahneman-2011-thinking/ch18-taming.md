---
id: kahneman-2011-thinking/ch18-taming
work: kahneman-2011-thinking
unit: "18 Taming Intuitive Predictions"
pages: pdf 182–192 (printed page numbers unknown)
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Taming Intuitive Predictions

## L0 — One line
Intuitive predictions match the extremeness of the evidence and ignore regression to the mean, so they should be pulled back toward the average in proportion to how weak the evidence is.

## L1 — The gist (≤ 120 words)
How should we turn weak evidence into a numerical forecast? Kahneman argues that System 1 swaps the hard question (what will happen?) for an easy one (how impressive is the evidence?). The forecast then ends up as extreme as the evidence, which makes it biased. The fix is a four-step correction. Start from the average, find the value your intuition suggests, estimate the correlation between evidence and outcome, and move only that fraction of the distance. The correction is hard work and costs the thrill of calling extreme cases. It can be worth skipping when one kind of error is much worse than the other. Small samples of evidence deserve more regression.

**Prerequisites:** averages; correlation as a 0-to-1 strength of link; regression to the mean (previous chapter); the System 1 / System 2 distinction.

## L2 — Key ideas
- Forecasts come from calculation, from skilled intuition built by repeated experience, or from heuristics that substitute an easy question. The last two can sometimes feel the same, and heuristic judgments can be held with high confidence. (pdf 182)
- Intuitive prediction can be described as steps: find a causal link, compare to a norm, substitute, and match intensity (give the forecast the same rank as the evidence). Because System 1 either accepts or rejects evidence, it is almost completely insensitive to how predictive the evidence really is. (pdf 183)
- In the freshman-description study, the "evaluate the evidence" and "predict the outcome" percentile judgments were identical. Kahneman calls this perhaps the best evidence for substitution (answering an easier question than the one asked). (pdf 185)
- Israeli army officers' predicted grades had almost the same spread of A's and B's as the real final grades. Their predictions were therefore non-regressive. (pdf 185–186)
- Correction: baseline, intuition, correlation, then move that share of the distance. Unbiased predictions are about equally likely to be too high or too low. (pdf 187)
- Discrete (probability) and numerical predictions share one corrective logic: a point between the baseline and the intuition. (pdf 188)
- Unbiased predictions cannot call rare events from weak evidence. Extreme language may have some justification (for the comfort it gives) when one error type is far costlier, but a rational person need not delude herself. (pdf 189–190)
- Less information means more regression. This can favour Jane over the more impressive Kim. (pdf 190)
- Both systems resist regression, and we do not learn it from experience. (pdf 191)

## L3 — Walkthrough

### Opening: kinds of forecasting (pdf 182)
- Forecasting is everywhere: economists, analysts, contractors, chefs, and private life (pdf 182).
- Some predictions use look-up tables and explicit analysis. Others use System 1 in two varieties (pdf 182):
  - Skilled intuition from repeated experience (Klein's chess masters, fireground commanders, physicians). The answer comes quickly because familiar cues are recognized.
  - Heuristic intuition, which substitutes an easy question for the harder one. It can be subjectively indistinguishable from skill and can be held with high confidence even though it rests on nonregressive assessments of weak evidence.
- Many real judgments mix analysis and intuition (pdf 182).

### Nonregressive Intuitions (pdf 182–186)
**Julie.** "Julie is a university senior who read fluently at age four. What is her GPA?" People familiar with US education quickly come up with a number, often near 3.7 or 3.8 (pdf 182). The steps, all System 1 (pdf 183–184):
1. *Find a causal link* between evidence and target. It can be indirect, since early reading and high GPA both signal academic talent. Irrelevant evidence (fly-fishing, weight lifting) would probably be rejected by System 2. The process is effectively dichotomous: System 1 can reject evidence but cannot adjust for smaller weaknesses. So intuitive predictions are almost completely insensitive to the evidence's real predictive quality. When a link is found, WYSIATI ("what you see is all there is") builds the best story from what is available (pdf 183).
2. *Compare to a norm*: how precocious is fluent reading at four? The reference group (the comparison group) is left unspecified, as in normal speech (pdf 183).
3. *Substitute and match intensity*: Julie gets the same percentile for GPA as for early reading. This is then translated onto the GPA scale (pdf 183).

Intensity matching makes predictions as extreme as the evidence. People give the same answer to "percentile for reading precocity?" and "percentile for GPA?" (pdf 183). The steps are listed in order only for clarity. In reality activation spreads, feeds back, and settles on the most coherent solution (pdf 184).

**Freshman descriptions study (Kahneman and Tversky).** Participants judged five-adjective descriptions of eight freshmen, such as "intelligent, self-confident, well-read, hardworking, inquisitive" (pdf 184).
- One group answered evidence questions: how impressive is this for academic ability, and what percentage of descriptions would impress you more? Judgments showed impressive consensus, at least within a culture, for example "top 15% but unlikely top 3%" (pdf 184).
- The other group answered prediction questions: the estimated GPA, and the percentage of freshmen with a higher GPA. These involve much uncertainty: a year passes, and it is doubtful how accurately five adjectives predict actual achievement (pdf 184–185).
- Result: the percentile judgments were identical. Kahneman calls this "perhaps the best evidence we have for the role of substitution" (pdf 185). Prediction matched evaluation. People did not notice they answered a different question, so their predictions ignore regression to the mean (pdf 185).

**Officer-selection unit.** Kahneman asked the unit's officers for their best guess of cadets' final officer-school grades, in addition to their usual ratings, and a few hundred forecasts were collected. The validity of the ratings was known to be rather poor. The predicted frequencies of A's and B's were almost identical to the school's actual grade frequencies (pdf 185). The officers did not distinguish evaluating candidates from predicting a future grade. They translated their own grades onto the school's scale by intensity matching (pdf 186).

*Intuition note:* Asked "what will happen?", the mind answers "how good does this look?" and reports it on the requested scale. A forecast built that way is as extreme as the evidence, however weak the evidence is.

### A Correction for Intuitive Predictions (pdf 186–187)
- Schematic formulas: reading age = shared factors + factors specific to reading age = 100%, and GPA = shared factors + factors specific to GPA = 100%. Shared factors include aptitude and family support for academics. Specific factors include pushy parents, a love affair, or a skiing accident (pdf 186).
- The correlation between two measures equals the proportion of shared factors among their determinants. Kahneman's "most optimistic guess" for Julie is about 30% (pdf 186).
- Four steps (pdf 187):
  1. Estimate the average GPA (the baseline you would predict knowing nothing about Julie).
  2. Find the GPA that matches your impression of the evidence (your intuitive prediction).
  3. Estimate the correlation between evidence and GPA.
  4. If it is .30, move 30% of the distance from the average to the matching GPA.
- As a formula (added step): $\text{prediction} = \text{baseline} + r\,(\text{intuitive} - \text{baseline})$, where $r$ is the correlation from step 3.
- The method works for any quantitative variable and keeps the intuition while regressing it toward the mean. When the correlation is strong, the adjustment is small (pdf 187).
- Why it is needed: predicting "day 2 golf score = day 1 score" is biased. Day-1 leaders will on average do worse and day-1 laggards mostly improve. Non-regressive predictions are too optimistic for the best and too pessimistic for the worst. Likewise early readers will more often disappoint than surprise (pdf 187).
- Corrected predictions are about equally likely to overestimate and underestimate. Errors remain but are smaller and do not favour high or low outcomes (pdf 187).

*Intuition note:* The farther your evidence is from guaranteeing the outcome, the less the forecast should leave the average. The correlation says how far.

### A Defense of Extreme Predictions? (pdf 188–191)
- The same corrective logic applies to Tom W-type probability predictions and to numerical ones (pdf 188). Both have:
  - a baseline (base rate, or average outcome in the relevant category);
  - an intuitive prediction;
  - a target between the two.
- With no useful evidence, stay at the baseline. Stay with the intuition only if you remain completely confident after critical review. Usually you land between (pdf 188).
- The procedure approximates an appropriate statistical analysis and addresses overconfident, overly extreme intuitions (pdf 188).
- Correcting is System 2 work: find the reference category, the baseline, and the evidence quality. It is justified only when the stakes are high and you are particularly keen not to make mistakes (pdf 189).
- Cost: unbiased predictions allow rare or extreme calls only when information is very good. If your predictions are unbiased, you will never get to say "I thought so!" about a future Supreme Court justice or a major start-up success (pdf 189).
- **Objection:** Kahneman says a preference for unbiased predictions is justified if all errors are treated alike, but in some situations one type of error is much worse. A venture capitalist fears missing the next Google more than a failed modest investment. A conservative banker may fear one default more than rejecting several good clients. Extreme language may then have some justification for its comfort (pdf 189).
- **Kahneman's reply:** a rational venture capitalist knows even promising start-ups have a moderate chance. She picks the best available bets, considers a range of outcomes, and may rationally invest heavily in a probable failure if the reward is large. Those who need distorted estimates to avoid paralysis should stay aware of the self-indulgence (pdf 189–190).
- **Kim vs. Jane.** Kim has a spectacular talk and recommendations but no track record. Jane has three productive postdoc years but a duller talk. Intuition favours Kim (WYSIATI), but there is much less information about her (pdf 190).
  - This is the law of small numbers: extreme outcomes are more likely in small samples, and there is more luck in them, so Kim's prediction should be regressed more deeply.
  - Allowing for this, you might pick Jane. Kahneman would vote for Jane but says it would be a struggle (pdf 190).
- A venture capitalist choosing between a well-estimated product and a more exciting but less certain one faces the same question. Whether the exciting one is still better after factoring in uncertainty deserves careful thought (pdf 190–191).

*Intuition note:* A vivid impression based on little information is a small sample. Regress it more deeply toward the mean than a duller impression based on a lot of information.

### A Two-Systems View of Regression (pdf 191)
- System 1 matches extremeness of prediction to extremeness of evidence, and its confidence comes from story coherence. Hence intuitions are too extreme and trusted too much (pdf 191).
- System 2 also struggles. Regression is alien and hard to teach (Galton had trouble), and it needs special training. We do not learn it from experience, and regressions we notice get a causal explanation that is "almost always wrong", as in the flight-instructor story (pdf 191).

### Speaking of Intuitive Predictions (pdf 191–192)
Kahneman gives sample sentences. They urge regression for an outstanding start-up proof of concept, an overly favourable intuitive prediction, and a single excellent review. They also say an investment may be a good idea even if the best guess is that it will fail (pdf 191–192).

## Toy example (ours, not from the text)
Predict a student's exam score. The class average is 60 (step 1). A glowing teacher letter feels like 90 (step 2). The letter correlates .30 with exam scores (step 3).
- Distance from average to intuition: 90 − 60 = 30.
- Move 30%: 0.30 × 30 = 9.
- Prediction: 60 + 9 = 69.

Edge cases:
- If $r = 0$: 60 + 0 × 30 = 60, the baseline.
- If $r = 1$: 60 + 1 × 30 = 90, the intuition.
- If the letter instead came from someone who met the student once and the correlation is .10: 60 + 0.10 × 30 = 63.

## Concepts
- [[heuristic]] — a shortcut that substitutes an easy question for a hard one; here, evaluation replaces prediction (pdf 182)
- [[regression-to-the-mean]] (new) — extreme outcomes tend to be followed by less extreme ones; intuitive predictions ignore this (pdf 185)
- [[substitution]] (new) — answering "how impressive is the evidence?" when asked "what will happen?" (pdf 183, 185)
- [[intensity-matching]] (new) — giving a prediction the same percentile or extremeness as the evidence (pdf 183)
- [[wysiati]] (new) — judging from the information at hand only, building the most coherent story (pdf 183)
- [[base-rate-baseline]] (new) — the prediction you would make knowing nothing about the case: base rate or category average (pdf 187–188)
- [[correlation-as-shared-factors]] (new) — correlation equals the proportion of shared determinants of two measures, as used here (pdf 186)
- [[law-of-small-numbers]] (new) — extreme outcomes are more likely to be observed in small samples of evidence, so regress more (pdf 190)
- [[bias-variance-trade-off]] — here only the idea that unbiased forecasts are smaller-error but less extreme (pdf 187, 189); the term itself is not used

## Canonical instances
- [[julie-gpa-prediction]] — early reading mapped to GPA by intensity matching (pdf 182–183)
- [[freshman-description-study]] — identical percentiles for evaluating and predicting (pdf 184–185)
- [[israeli-officer-grade-forecasts]] — predicted grade frequencies copied the school's (pdf 185–186)
- [[kim-vs-jane-hiring]] — less information, so more regression (pdf 190)
- [[golf-day-two-prediction]] — "same as day 1" forecasts are biased (pdf 187)

## Bridges (candidates)
- [same-math] Move $r$ of the way from average to intuition ↔ statistics: prediction by a regression line with standardized variables — same weighting by correlation (the author calls it only an approximation of statistical analysis, pdf 188)
- [structural-analogy] Regress toward the mean for a small sample ↔ bias–variance trade-off: shrinking noisy estimates helps forecasts
- [metaphor] Kim/Jane choice ↔ bounded rationality: vivid impressions fill gaps in thin information

## Questions this raises
- How do we estimate the correlation in step 3 when we have no data, and how wrong can that guess be?
- When are the costs of errors lopsided enough that biased, extreme forecasts are the better decision rule?
- How can organizations make people regress forecasts when the intuition feels right?
- If experience does not teach regression, what training works?

## Reading notes
- Printed page numbers are not given, so citations use pdf numbers (182–192).
- The text layer has stray garbled fragments inside words (e.g. "GDP" for GPA at pdf 183; "competitiowhired D=n" at pdf 183; "prediof рctions" at pdf 185). I read these as noise, not as the author's wording. No page images were supplied, so the text layer was my only source.
- "Tom W" and "law of small numbers" are referred to as earlier material and are not explained here.
