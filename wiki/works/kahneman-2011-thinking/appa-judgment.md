---
id: kahneman-2011-thinking/appa-judgment
work: kahneman-2011-thinking
unit: "Appendix A — Judgment Under Uncertainty: Heuristics and Biases (Tversky & Kahneman)"
pages: pdf 410–430 (printed page numbers not visible)
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Judgment Under Uncertainty: Heuristics and Biases

## L0 — One line
People judge probabilities and predict values with three shortcuts (representativeness, availability, anchoring) that are usually useful but sometimes cause systematic, predictable errors.

## L1 — The gist (≤ 120 words)
How do people judge the likelihood of uncertain events or predict uncertain quantities? The authors argue that they use a few heuristics: mental shortcuts that simplify the task. Representativeness judges by similarity. Availability judges by how easily instances come to mind. Anchoring starts from an initial number and adjusts too little. Each shortcut is often useful, but each produces systematic biases: ignoring base rates (how common each category is) and sample size, misreading chance and regression, misjudging frequencies, and giving overconfident estimates. The authors say the biases are not caused by wishful thinking or by payoffs and penalties, and experts show them too when they judge intuitively. Knowing them could improve judgments.

**Prerequisites:** probability and odds; averages and percentages; Bayes' rule at the level of "prior odds × evidence"; the idea of a random sample.

## L2 — Key ideas
- Beliefs about uncertain events rest on a few heuristics. They simplify hard tasks, are generally useful, and sometimes cause severe, systematic errors (pdf 410).
- **Representativeness:** probability is judged by similarity to a stereotype or to the parent population. This produces neglect of base rates (how common each category is), neglect of sample size, and false ideas about chance (pdf 411–414).
- Predictions made by representativeness ignore how predictable the outcome is. This gives the illusion of validity (unwarranted confidence from a good fit between input and outcome) and, the authors suggest, misunderstanding of regression toward the mean (extreme values tend to be followed by less extreme ones), for example the flight-instructor error about punishment (pdf 415–418).
- **Availability:** frequency is judged by ease of recall or construction. This biases judgments through retrievability, search sets, imaginability and illusory correlation (pdf 418–421).
- **Anchoring:** estimates stay too close to a starting value. This explains underestimated products, over-optimistic plans (conjunctive events: all steps must succeed), underestimated risks in complex systems (disjunctive events: failure if any part fails), and, at least in part, overly narrow confidence intervals (pdf 421–425).
- The biases are cognitive, not motivational. Experts show them in intuitive judgment, and people rarely learn the right statistical rules from experience because the relevant data are not coded appropriately (pdf 425–426).
- Coherence (internal consistency) is not enough for rational probability judgments; they must fit the person's whole web of beliefs (pdf 426–427).

## L3 — Walkthrough

**Introduction (pdf 410).** Beliefs about uncertain events (elections, guilt, the future dollar) are usually stated in words and only sometimes as numbers. The authors claim people use a limited number of heuristic principles that reduce hard probability and prediction tasks to simpler operations. Analogy: apparent distance depends partly on clarity. Sharper objects look closer. The rule has some validity, because in any given scene more distant objects are seen less sharply, but it leads to common biases; the text states that distance is underestimated when visibility is good because objects are seen sharply (this passage is partly garbled in the text layer). The paper describes three heuristics and the biases they cause.

### Representativeness (pdf 410–418)
Questions such as "does A belong to class B?" or "does process B generate event A?" are answered by how much A resembles B (pdf 410–411). Example: "Steve" is shy, tidy and detail-loving. People rank occupations by probability and by similarity in exactly the same order (pdf 411). Similarity ignores several factors that should affect probability.

**Insensitivity to prior probability (base rate).** The base rate (how common each category is) does not change similarity, so it gets neglected (pdf 411).
- Experiment: descriptions were said to be drawn from 100 professionals, either 70 engineers/30 lawyers or 30 engineers/70 lawyers. By Bayes' rule the odds ratio between the two conditions should be $(.7/.3)^2 = 5.44$ per description. Subjects gave essentially the same judgments in both conditions (pdf 412).
- With no description, subjects used the base rates correctly (.7 and .3).
- "Dick" (a description meant to be uninformative): subjects said .5 in both conditions. People use priors when given no evidence but ignore them when given worthless evidence (pdf 412).

*Intuition note:* Once a description is given, people judge by how well it matches a stereotype, so the plain count of how many engineers there are drops out of the judgment, even when the description tells us nothing.

**Insensitivity to sample size.** Similarity of a sample statistic to the population value does not depend on sample size. So people give identical distributions of average height for samples of 1,000, 100 and 10 men (pdf 412–413).
- Hospital problem: larger hospital about 45 births/day, smaller about 15. Which recorded more days with more than 60% boys? Answers: larger 21, smaller 21, about the same 53 (undergraduates). Sampling theory says the smaller hospital, because a large sample strays less from 50% (pdf 413).
- Urn problem (2/3 vs. 1/3 colors): a sample of 4 red, 1 white versus 12 red, 8 white. Correct posterior odds, with equal priors, are 8 to 1 and 16 to 1. Most people think the first sample is stronger evidence because its proportion is higher. Intuitive odds are also far less extreme than correct ones, which is called **conservatism** (pdf 413–414).

**Misconceptions of chance.** People expect even short random sequences to look random. They judge H-T-H-T-T-H more likely than H-H-H-T-T-T or H-H-H-H-T-H. Locally representative sequences have too many alternations and too few runs. This leads to the **gambler's fallacy** (black is "due" after a run of red). Deviations in chance processes are not corrected but diluted (pdf 414). Experienced research psychologists show a belief in the **law of small numbers** (small samples are highly representative). They trust small samples too much and overestimate replicability (pdf 414–415).

**Insensitivity to predictability.** If people predict by how favorable a description is, predictions ignore its reliability (pdf 415). In normative theory, predictions should be the same for all cases when predictability is nil. In general, higher predictability means a wider range of predicted values (pdf 415). In the student-teacher study, predicting standing after 5 years gave judgments identical to evaluating the practice lesson itself (pdf 415–416).

**The illusion of validity.** Confidence depends mainly on how well the predicted outcome matches the input, not on factors limiting accuracy. The illusion persists even when the judge knows of these limits, as with selection interviews (pdf 416). Consistent input patterns (all B's) raise confidence. But with inputs of stated validity, independent inputs can give higher accuracy than redundant ones. So redundancy raises confidence while lowering accuracy (pdf 416).

**Misconceptions of regression.** Take two variables $X$ and $Y$ with the same distribution. Individuals whose average $X$ score is $k$ units from the mean of $X$ will usually have an average $Y$ score less than $k$ units from the mean of $Y$. This is regression toward the mean (pdf 416–417). People do not expect it in many contexts where it is bound to occur, and when they recognize it they often invent spurious causal explanations. The authors suggest that regression stays elusive because it is incompatible with the belief that the outcome should be as extreme as the input (pdf 417).
- **Flight instructors' view:** praise after an exceptionally smooth landing is typically followed by a poorer one, and harsh criticism after a rough landing usually by improvement. They concluded that verbal rewards are detrimental and punishments beneficial. The authors say this is unwarranted, because regression toward the mean would produce improvement after poor performance and deterioration after outstanding performance even if the instructor did not respond to the first attempt (pdf 417).
- General consequence: people are most often rewarded for punishing and punished for rewarding, by chance alone (pdf 417–418).

*Intuition note:* After an extreme result, the next result is usually less extreme, so improvement after a poor performance (or decline after an outstanding one) is expected even if nobody reacts to the first result.

### Availability (pdf 418–421)
Frequency or probability is judged by how easily instances come to mind. This is useful because large classes are usually recalled better and faster, but ease of recall is affected by other factors (pdf 418).
- **Retrievability:** in lists of famous and less famous men and women, subjects judged the sex with more famous names to be more numerous. Salience and recency probably also matter (a burning house, an overturned car) (pdf 418–419).
- **Search set:** words starting with r vs. r in third position. Words are searched by first letter more easily, so first-position words seem more numerous, even for r and k, which are more frequent in the third position (pdf 419). Abstract words seemed more frequent than concrete ones of equal frequency, presumably because contexts are easier to find (pdf 419).
- **Imaginability:** committees of $k$ from 10 people, $2 \le k \le 8$. The count is the binomial coefficient $\binom{10}{k}$, maximal at 252 for $k=5$. It equals the count for $10-k$ (pdf 419). Small committees are easier to construct (five disjoint committees of 2, not even two of 8). Subjects' estimates decreased with committee size. Median estimates were 70 for size 2 and 20 for size 8; the correct value is 45 for both (pdf 420).
- **Illusory correlation (Chapman and Chapman):** judges overestimated how often natural associates (suspiciousness and peculiar eyes in drawings) co-occurred. The effect resisted contradictory data, persisted even when the true correlation was negative, and hid real relationships (pdf 420–421). The authors explain it by availability: strong associates seem to co-occur frequently (pdf 421).

*Intuition note:* What comes easily to mind often tracks real frequency, but not always. Where memory search is uneven, the estimate is wrong in a predictable direction.

### Adjustment and Anchoring (pdf 421–425)
Estimates start from an initial value and adjustments are typically insufficient, so estimates are biased toward the start. This is **anchoring** (pdf 421).
- **Wheel of fortune:** random numbers from a wheel were used as starting points. Median estimates of the percentage of African countries in the UN were 25 for the anchor 10 and 45 for the anchor 65. Payoffs for accuracy did not reduce the effect (pdf 421–422).
- **Incomplete computation:** high school students estimated $8\times7\times6\times5\times4\times3\times2\times1$ or the ascending version within 5 seconds. Medians were 2,250 (descending) and 512 (ascending); the correct answer is 40,320. Both predictions (underestimation; descending judged larger) were confirmed (pdf 422).
- **Conjunctive and disjunctive events (Bar-Hillel):** subjects preferred to bet on a seven-draw conjunctive event (probability .48) over a simple event (.50). They preferred the simple event over a disjunctive event (.52) (pdf 422). People tend to overestimate conjunctive and underestimate disjunctive probabilities. The authors explain this as anchoring: the elementary event's probability is the natural starting point, and adjustment is typically insufficient (pdf 423).
  - Planning typically has a conjunctive character (each of several events must occur), which leads to unwarranted optimism. Risks in complex systems are typically disjunctive (failure if any essential component fails), so people tend to underestimate failure. The chain-like structure of conjunctions leads to overestimation and the funnel-like structure of disjunctions to underestimation (pdf 423).
- **Subjective probability distributions and calibration:** $X_{90}$ is the value the judge is just willing to bet at 9:1 odds will not be exceeded by the true value. A judge is calibrated if exactly $i$% of the true values fall below the stated $X_i$. For example, 98% should fall between $X_{01}$ and $X_{99}$ (pdf 423–424). In most studies about 30% of true values fall outside that interval. This holds for naive and sophisticated subjects, and scoring rules do not remove it. The authors attribute it at least in part to anchoring on the best estimate with too little adjustment (pdf 424).
- **Two elicitation procedures** (percentiles vs. odds) are formally equivalent but suggest different anchors (pdf 424–425). With 24 quantities, one group gave $X_{10}$ or $X_{90}$. A second group assessed odds for the first group's median values, which should have been 9:1. Their median odds were 3:1. The first group was too extreme: events they gave probability .10 occurred in 24% of cases. The second group was too conservative: events given average probability .34 occurred in 26% (pdf 425).

### Discussion (pdf 425–427)
- The biases are not due to wishful thinking or payoff distortion. Several severe errors occurred even when accuracy was rewarded (pdf 425).
- Experienced researchers show the same biases when they think intuitively. Statistically sophisticated people avoid elementary errors but their intuitive judgments are liable to similar fallacies in more intricate and less transparent problems (pdf 425–426).
- Regression and the effect of sample size on variability are not learned from experience because relevant instances are not coded appropriately (for example, people do not attend to the average word length of individual lines or pages). Calibration is hard to learn because people do not group events by judged probability (pdf 426).
- **Modern decision theory** (note 24 cites Savage) defines subjective probability by the bets an idealized person would accept. Coherent probabilities can be derived if choices satisfy axioms. In reality probabilities determine bet preferences, not the reverse (pdf 426–427). The authors credit this approach with giving a rigorous subjective interpretation of probability that applies to unique events (pdf 426).
- Many students conclude from the subjective nature of probability that coherence is the only valid criterion; in the formal theory any coherent set of judgments is as good as any other. The authors say this is not entirely satisfactory. Coherence alone is not enough. A gambler's-fallacy believer could be internally consistent but conflicts with the belief that a coin has no memory. Rational judgments must fit the person's whole web of beliefs, though there can be no simple formal procedure for assessing this (pdf 427).

### Summary (pdf 427–428)
Representativeness is usually employed to judge whether an object or event belongs to a class or process. Availability is often employed to assess the frequency of a class or the plausibility of a development. Adjustment from an anchor is usually employed in numerical prediction when a relevant value is available. The heuristics are highly economical and usually effective but lead to systematic, predictable errors. Better understanding could improve judgment (pdf 427–428).

## Toy example (ours)
Base-rate neglect, using the engineers/lawyers setup. Suppose a description is 3 times as likely for an engineer as for a lawyer (likelihood ratio 3).
- Condition A (70 engineers, 30 lawyers): prior odds $7/3$. Posterior odds $= 7/3 \times 3 = 7$, so probability $7/8 = .875$.
- Condition B (30 engineers, 70 lawyers): prior odds $3/7$. Posterior odds $= 3/7 \times 3 = 9/7 \approx 1.29$, so probability $9/16 = .5625$.
- Ratio of posterior odds: $7 \div (9/7) = 49/9 = 5.44 = (7/3)^2$, the figure on pdf 412.

A judge using representativeness gives about the same answer in both conditions, as the subjects did, so the judge ignores the 5.44 factor.

## Concepts
- [[heuristic]] — a mental rule that simplifies probability judgment or value prediction; usually useful, sometimes severely wrong (pdf 410)
- [[representativeness / availability / anchoring]] — the paper's three heuristics: similarity, ease of recall or construction, and insufficient adjustment from a starting value (pdf 410, 418, 421)
- [[base-rate-neglect]] (new) — ignoring prior probabilities when a description is given, even a worthless one (pdf 411–412)
- [[insensitivity-to-sample-size]] (new) — judging sample results by resemblance to the population, not by sample size; includes the law of small numbers (pdf 412–415)
- [[gambler's-fallacy]] (new) — expecting chance to self-correct; deviations are actually diluted (pdf 414)
- [[conservatism]] (new) — intuitive posterior odds less extreme than correct ones (pdf 414)
- [[illusion-of-validity]] (new) — confidence from a good fit between input and predicted outcome, with little or no regard for the factors that limit accuracy (pdf 416)
- [[regression-toward-the-mean]] (new) — values selected for being extreme on one measure are usually less extreme on another (pdf 417)
- [[illusory-correlation]] (new) — overestimating co-occurrence of natural associates (pdf 420)
- [[conjunctive-disjunctive-bias]] (new) — overestimating conjunctive and underestimating disjunctive probabilities, via anchoring (pdf 422–423)
- [[calibration]] (new) — stated percentile values match actual frequencies; in most studies the intervals judges gave were too narrow (pdf 424)
- [[subjective expected utility]] — the decision-theory view of probability as coherent betting choices; the authors say coherence is not sufficient for rationality (pdf 426–427)

## Canonical instances
- [[steve-the-librarian]] — ranking occupations by similarity matches ranking by probability (pdf 411)
- [[engineers-and-lawyers]] — base rates ignored once a description is given (pdf 411–412)
- [[two-hospitals-problem]] — sample size neglected (pdf 413)
- [[flight-instructors]] — regression misread as the effect of punishment (pdf 417)
- [[committees-of-k]] — imaginability gives a decreasing estimate where the true count is bell-shaped (pdf 419–420)
- [[factorial-anchoring]] — 8×…×1 vs. 1×…×8 estimates (pdf 422)
- [[bar-hillel-bets]] — conjunctive/disjunctive betting (pdf 422)

## Bridges (candidates)
- [structural-analogy] Regression toward the mean ↔ statistics: shrinkage toward the mean under noisy measurement — extreme observations include noise that does not repeat.
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$.
- [structural-analogy] Overly narrow confidence intervals ↔ machine-learning model calibration: stated confidence exceeds hit rate.
- [metaphor] Heuristics as economical but biased ↔ bounded rationality: shortcuts used under limited effort.

## Questions this raises
- If heuristics are mostly accurate, in which environments do they fail, and can the failure direction be predicted as the authors do for conjunctive and disjunctive structures?
- Could people learn calibration or regression if feedback were organized in the appropriate "code" (pdf 426)?
- What practical procedure could check a probability judgment's fit with the whole web of beliefs, given that no simple formal procedure exists (pdf 427)?
- Do expert judges improve if trained on the specific biases listed here?

## Reading notes
- The unit is Appendix A of *Thinking, Fast and Slow*, by Amos Tversky and Daniel Kahneman (pdf 410); these pages give no publication year. No printed page numbers are visible, so all references are pdf pages. Only pdf 422 has a page image; the rest use the text layer.
- Footnotes appear as endnotes on pdf 429–430 (citations only).
- The text layer has garbled insertions (e.g. "[hanerser", "Vt pofreak"). I ignored these where the sense was clear. The coin sequence H-H-H-T-T-T on pdf 414 is a reconstruction of a garbled string ("H-H-H-T- [enc. IT-T"), and the distance analogy on pdf 410 is partly garbled.
- Misprint on pdf 422: the disjunctive bag is given as "10% red marbles and 9% white marbles". It should be 90% white; the stated probability .52 only works that way ($1-.9^7 \approx .52$). The conjunctive probability checks as $.9^7 \approx .48$.
- "(.7/.3)2, or 5.44" on pdf 412 means $(.7/.3)^2$. The text layer shows "2 = k= 8" for $2\le k\le 8$ and "(10/k)" for the binomial coefficient on pdf 419. Calibration notation $X_i$ on pdf 424 is garbled in the text layer; I reconstructed it from the examples given.
