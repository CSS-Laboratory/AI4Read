---
id: kahneman-2011-thinking/ch17-regression
work: kahneman-2011-thinking
unit: "17 Regression to the Mean"
pages: pdf 172–181 (printed page numbers not given)
fields: [decision-game-theory]
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
# Regression to the Mean

## L0 — One line
When two measures are imperfectly correlated, extreme results tend to be followed by less extreme ones, and this needs a statistical explanation, not a causal story.

## L1 — The gist (≤ 120 words)
Why do praised flight cadets get worse and scolded cadets get better? Kahneman argues that performance is partly talent and partly luck. An extreme result probably had extreme luck, and luck is unlikely to repeat. So the next result is expected to be closer to the average. This is regression to the mean. It follows whenever the correlation between two scores is below perfect. Our minds look for causes, so we invent stories (praise, jinx, relaxation) or misread treatment effects. The same logic matters for forecasting and for judging treatments, which need a control group. Regression has an explanation but no cause.

**Prerequisites:** the idea of an average; ranking people on a measure; the everyday meaning of "correlation".

## L2 — Key ideas
- The flight instructor's observation was correct, but his inference was wrong. Extreme performances are followed by regression whether or not there is praise or punishment (pdf 172).
- Because we reward good results and punish bad ones, life's feedback is "perverse": we are statistically punished for being nice and rewarded for being nasty (pdf 173).
- Success = talent + luck. An extreme score suggests extreme luck, so the best prediction is more moderate than the score (pdf 173–174).
- Regression also appears when you predict the earlier event from the later one. Kahneman says this should help convince us that it has no causal explanation (pdf 175).
- Sir Francis Galton, a nineteenth-century British scientist, discovered and named regression. He took years to see that correlation and regression are the same concept seen from two sides (pdf 176, 178).
- Whenever the correlation between two scores is imperfect, there will be regression to the mean. The correlation coefficient measures the relative weight of the factors two measures share (pdf 177–178).
- Our mind is strongly biased toward causal explanations and handles "mere statistics" badly. Kahneman says the difficulty with regression comes from both System 1 and System 2 (the book's two modes of thinking), and that the insistent demand for causal interpretations is a feature of System 1 (pdf 179).
- Judging a treatment needs a control group (a group that gets no treatment, or a placebo), because extreme groups regress to the mean over time. Forecasts should be regressive, meaning pulled toward the average (pdf 180–181).

## L3 — Walkthrough

**The flight instructors (pdf 172–173).**
- Kahneman taught that rewarding improvement works better than punishing mistakes (pdf 172).
- **Instructor's objection:** after praise for a clean maneuver, cadets usually do worse next time. After shouting at a bad maneuver, they usually do better. So punishment works and reward does not (pdf 172).
- **Kahneman's reply:** the observations are right, but the inference is wrong. He praised only far-above-average attempts. Those cadets were probably lucky and likely to deteriorate anyway. Bad attempts were probably unlucky and likely to improve anyway (pdf 172).
- Demonstration: each officer threw two coins at a floor target with his back turned. The two distances were listed and sorted by first try. Most, but not all, of the best first-try throwers got worse. Poor ones generally improved. No praise or punishment was involved (pdf 172–173).
- Conclusion: instructors are trapped. They punish after poor performance and are "rewarded" by the improvement that follows. Kahneman adds that the instructors were not alone in this predicament, and calls the feedback life gives us "perverse" (pdf 173).

*Intuition note:* A very good or very bad try is probably partly luck. Luck is unlikely to repeat, so the next try tends to be less extreme.

**Talent and luck (pdf 173–175).**
- Kahneman's "favorite equations": success = talent + luck, and great success = a little more talent + a lot of luck (pdf 173).
- Golf example: assume the day-1 average is par 72. A golfer scores 66. We may infer he is more talented than average. We may equally infer he was lucky (pdf 173).
- The inferences are uncertain but will be right more often than wrong. Above-average day 1 = above-average talent + luck. Below-average day 1 = below-average talent + bad luck (pdf 174).
- For day 2, expect talent to stay the same. We have no way of predicting luck, so the best guess is that it will be average. The best guess is therefore not a repeat of day 1 (pdf 174).
- The day-1 leader will probably still do well, but less well. The day-1 laggard will probably still be below average, but will improve. The gap between them is expected to shrink, though the first player is still expected to do better (pdf 174).
- The predicted score is closer to the average than the evidence. The more extreme the score, the more regression we expect. A few 66-scorers will do even better, but most will do worse (pdf 174–175).
- Reversed in time, the same pattern appears: day-2 best players were probably less lucky and scored less well on day 1. Kahneman says this should help convince us that regression has no causal explanation (pdf 175).
- **Sports Illustrated jinx:** the cover athlete had an exceptional season, probably helped by luck. Overconfidence and pressure are offered as causes, but luck being fickle is simpler (pdf 175).
- **Ski jump:** a commentator said the leader "will be tense", and the man behind "will be relaxed". Kahneman says this is an invented causal story. The story could even be true. But the change "does not need a causal explanation"; he calls it a mathematically inevitable consequence of luck playing a role in the first jump (pdf 175).

*Intuition note:* Predict the second round by keeping the talent part and replacing the luck part with "average". That automatically pulls the forecast toward the middle.

**Understanding regression (pdf 176–179).**
- Galton published "Regression towards Mediocrity in Hereditary Stature" in 1886. For seeds, he reported that offspring were smaller than large parents and larger than very small ones. He found the filial regression "directly proportional to the parental deviation" (pdf 176).
- Kahneman finds it striking that Galton was surprised by something so common. It took Galton several years to see that regression occurs whenever correlation is less than perfect (pdf 176).
- Different scales are compared using the population as reference, via ranks or standard scores. Example: Jane is 3rd in piano and 27th in weight among 100 children, so the text says she is a better pianist than she is tall (the text says "tall", although the second measure is weight) (pdf 176).
- Simplifying assumptions, at any given age: piano playing depends only on weekly practice hours, and weight only on ice cream consumption. Practice and ice cream are unrelated. Then weight = age + ice cream, and piano = age + practice (pdf 177).
- Tom ranks 12th in weight. Statistically he is probably older and eats more ice cream. Barbara is 85th in piano, so she is probably young and practises less. Predicting one measure from the other therefore regresses (pdf 177).
- The correlation coefficient (varies between 0 and 1, per the text) measures the relative weight of shared factors. Examples (pdf 177–178):
  - Size in English vs metric units: 1.
  - Parent–child height (a trait with relatively little environmental influence; we share half our genes with each parent): not far from .50.
  - Self-reported height and weight, adult American males: .41.
  - SAT and college GPA: about .60. The correlation of aptitude tests with graduate-school success is much lower, largely because aptitude varies little in that selected group.
  - Income and education in the US: about .40.
  - Family income and the last four phone digits: 0.
- Correlation and regression are "different perspectives on the same concept". Whenever the correlation between two scores is imperfect, there will be regression to the mean (pdf 178).
- Example: the claim that highly intelligent women tend to marry less intelligent men invites causal explanations. The claim that the correlation between spouses' intelligence is less than perfect is trivial. The two are algebraically equivalent, assuming men and women do not differ on average (pdf 178–179).
- Why it is hard: the mind is biased toward causal explanations. Associative memory spreads activation to any stored cause (pdf 179).
- Regression "has an explanation but does not have a cause". A business commentator who correctly says a business did better this year because it did poorly last year is likely to have a short tenure on the air (pdf 179). The author says the difficulty comes from both System 1 and System 2 (pdf 179).

*Intuition note:* "Imperfect correlation" and "regression" say the same thing in two ways. An interesting-sounding fact may therefore be a dull one in disguise.

**Treatments and forecasts (pdf 179–181).**
- Invented headline: depressed children given an energy drink improve over three months. Headstands or cat hugging would also be followed by improvement (pdf 179).
- Depressed children are an extreme group, and depression scores on successive tests correlate imperfectly. So they improve with no treatment (pdf 179–180).
- To show a treatment works, compare with a control group, ideally given a placebo. The question is whether treated patients improve more than regression explains (pdf 180). Howard Wainer has listed eminent researchers who made this error (pdf 180).
- Store-sales forecast (adapted from Bazerman): 2011 sales are $11M, $23M, $18M and $29M, total $61M. The required 2012 total is $67.1M, +10% (pdf 180).
- Adding 10% to each store is wrong. Forecasts should be regressive: add more than 10% to low performers, and less (or even subtract) for the others (pdf 180–181). Many people will find this puzzling (pdf 181).
- Closing remarks (pdf 181): one speaker says experience taught her that criticism beats praise, and the reply is that it is all due to regression. A weaker second interview is said to be more likely due to an unusually good first one. Because a screening procedure is good but not perfect, we should anticipate regression and not be surprised when the very best candidates often fall short.

*Intuition note:* Store sales differ because of location, competition and random factors. Stores that sold little may have had some bad luck, and stores that sold a lot some good luck. So forecasts should be regressive: add more than 10% for low performers and less for the others.

## Toy example (ours, not from the text)
Four players have talent 0, 2, 4, 6 (higher is better). Each day, luck is +2 or −2 with equal chance. A day score is talent + luck. Mean talent is (0+2+4+6)/4 = 3.
- Day-1 score 8: only possible as talent 6 + luck +2. Day-2 expectation: 6 + 0 = 6. It falls from 8 to 6, closer to 3.
- Score 6: only talent 4 + luck +2. Expectation 4 + 0 = 4.
- Score 0: only talent 2 + luck −2. Expectation 2 + 0 = 2.
- Score −2: only talent 0 + luck −2. Expectation 0.

The top scores fall back and the bottom scores rise, with no praise or blame involved. (Only these four extreme cases are used. The middle scores in this tiny model do not behave so neatly.)

## Concepts
- [[regression-to-the-mean]] (new) — extreme results tend to be followed by less extreme ones when luck or imperfect correlation is involved (pdf 172, 178)
- [[talent-plus-luck]] (new) — success = talent + luck; extreme success suggests a lot of luck (pdf 173–174)
- [[correlation-coefficient]] (new) — 0 to 1 here; the relative weight of factors two measures share (pdf 177)
- [[causal-bias]] (new) — the mind's pull toward causal explanations rather than "mere statistics" (pdf 179)
- [[control-group]] (new) — an untreated or placebo group that shows how much change regression alone produces (pdf 180)
- [[regressive-prediction]] (new) — a forecast pulled toward the average, not a repeat of the evidence (pdf 174, 181)

## Canonical instances
- [[flight-instructor-praise-punishment]] — praise followed by decline, scolding by improvement, explained by regression (pdf 172)
- [[coin-throwing-demonstration]] — two throws at a target show regression without feedback (pdf 172–173)
- [[golf-day1-day2]] — day-1 leader expected to regress on day 2 (pdf 173–174)
- [[sports-illustrated-jinx]] — a cover-athlete's later decline, which Kahneman explains more simply by fickle luck than by a jinx (pdf 175)
- [[galton-seeds-and-heights]] — regression in seeds and in the heights of children and parents (pdf 176)
- [[intelligent-women-spouses]] — causal puzzle that is just imperfect correlation (pdf 178)
- [[depressed-children-energy-drink]] — improvement of an extreme group without any treatment effect (pdf 179–180)
- [[store-sales-forecast]] — regressive forecasting of sales (pdf 180–181)

## Bridges (candidates)
- [structural-analogy] Talent + luck regression ↔ decision-game-theory: bias–variance trade-off — shrinking noisy estimates toward the mean can predict better.
- [metaphor] Perverse feedback for praise and punishment ↔ decision-game-theory: repeated games — what looks like a response to our action may be noise.
- [metaphor] Control group ↔ mechanism design: comparing against a baseline to isolate an effect — only a loose likeness.

## Questions this raises
- How much should a forecast be pulled toward the mean? The chapter only says "more" for extreme cases.
- How can a manager separate real improvement from regression in everyday feedback?
- If regression is a mathematical inevitability, when is a causal story about relaxation after a bad jump worth testing?
- Does the same logic apply when selecting the "very best" candidates?

## Reading notes
- Printed page numbers are "?" in the labels and not visible in the text layer, so all references use pdf numbers.
- The digest was written from the text layer; the wording of garbled spots is a reconstruction and was not verified in a page image.
- The text says Jane is a better pianist than she is "tall" although the second measure is weight (pdf 176); the digest follows the source wording.
- OCR errors appear, for example a garbled phrase in the instructor's speech (pdf 172), "verye d" (pdf 173), "filess" (pdf 175), "ann wd" (pdf 177), "werecte" (pdf 179). Garbled words are reconstructed from context.
- The "equations" in this chapter are verbal (e.g. success = talent + luck), so there is no formal derivation.
- The text says the correlation coefficient varies between 0 and 1; this is reported as stated.
