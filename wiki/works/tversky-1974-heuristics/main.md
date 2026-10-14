---
id: tversky-1974-heuristics/main
work: tversky-1974-heuristics
unit: paper
pages: 1124-1131
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Judgment under Uncertainty: Heuristics and Biases

## L0 — One line
People judge probabilities and predict values with three simple heuristics (representativeness, availability, anchoring), which are usually useful but cause systematic, predictable errors.

## L1 — The gist (≤ 120 words)
How do people judge the likelihood of uncertain events? The authors argue that they use a few heuristics, meaning shortcuts that simplify the task. Representativeness judges by similarity. Availability judges by ease of recall or construction. Anchoring starts from a number and adjusts too little. Each heuristic is often useful, but each produces systematic errors. Examples are neglecting base rates, ignoring sample size, the gambler's fallacy, misreading regression, biased frequency estimates, and overly narrow confidence intervals. Experts show the same biases when they think intuitively. The authors say that internal consistency of probability judgments is not enough for rationality. Understanding the biases could improve judgments and decisions.

**Prerequisites:** basic probability (odds, Bayes' rule in words, independent events); averages; binomial coefficients (counting combinations).

## L2 — Key ideas
- Judging probability by similarity (representativeness) ignores factors that should matter: base rates (how common each outcome is in the population), sample size, predictability, and regression (the tendency of extreme results to be followed by less extreme ones) (p. 1124–1127).
- Judging frequency by ease of recall or imagination (availability) is biased by familiarity, salience, search method and imaginability. It also offers a natural account of illusory correlation, an overestimate of how often two strongly associated events occur together (p. 1127–1128).
- Estimating by adjusting from a starting point (anchoring) leaves answers too close to the anchor. This affects compound events and confidence intervals (p. 1128–1130).
- People tend to overestimate the probability of conjunctive events (all of several events must occur) and to underestimate disjunctive events (at least one of several events occurs). This can lead to unwarranted optimism about plans and to underestimated failure risk in complex systems (p. 1129).
- Misunderstanding regression toward the mean leads instructors to wrongly conclude that punishment works better than reward (p. 1127).
- Biases are not motivational, and trained experts also show them when they judge intuitively (p. 1130).
- People do not learn statistical rules from experience because the relevant instances are not coded appropriately (p. 1130).
- Coherent (internally consistent) probabilities are not enough. A rational judge's probabilities must be compatible with his whole web of beliefs (p. 1130).

## L3 — Walkthrough

### Introduction (p. 1124)
Beliefs about uncertain events rest on a limited number of heuristic principles. These reduce complex probability and prediction tasks to simpler operations. They are "quite useful, but sometimes they lead to severe and systematic errors" (p. 1124). The authors compare this to distance perception. Apparent distance depends partly on clarity. The rule has some validity, but it leads to systematic errors: distances are often overestimated in poor visibility and often underestimated in good visibility (p. 1124). The article describes three heuristics and the biases they cause.

### Representativeness (p. 1124–1127)
**Definition.** For questions like "does A belong to class B?", people judge probability by how far A resembles B (p. 1124). In the Steve example ("shy… meek and tidy soul"), the probability that Steve is a librarian is assessed by his similarity to the librarian stereotype; research with problems of this type found that people order occupations by probability and by similarity in exactly the same way (p. 1124).

**Insensitivity to prior probability.** Similarity is not affected by base rates, so base rates are neglected (p. 1124).
- *Experiment.* Descriptions were said to be sampled from 100 engineers and lawyers. In one condition there were 70 engineers and 30 lawyers; in the other, 30 and 70 (p. 1124).
- *Normative benchmark.* By Bayes' rule the ratio of the two conditions' odds should be $(.7/.3)^2 = 5.44$ per description (p. 1124). (added step: posterior odds equal prior odds times the likelihood ratio, which is the same in both conditions. So the ratio of posterior odds is $\frac{7/3}{3/7}=\frac{49}{9}\approx 5.44$.)
- *Result.* Subjects gave essentially the same judgments in both conditions (p. 1124–1125).
- Without a description, they used the base rates correctly (.7 and .3) (p. 1125).
- With the worthless "Dick" description they said .5 in both conditions. The authors conclude that when no evidence is given, priors are used, and when worthless evidence is given, they are ignored (p. 1125).

**Insensitivity to sample size.** Similarity of a sample statistic to a population parameter does not depend on sample size (p. 1125).
- Subjects gave identical distributions of average height for samples of 1000, 100 and 10 men (p. 1125).
- *Hospital problem.* The larger hospital has about 45 births per day and the smaller about 15. Which recorded more days with over 60% boys? Answers: larger 21, smaller 21, about the same 53. Sampling theory says the smaller hospital has many more such days, because large samples stray less from 50% (p. 1125).
- *Urn problem.* The urn is 2/3 one colour and 1/3 the other. Sample 1 is 4 red and 1 white (n = 5). Sample 2 is 12 red and 8 white (n = 20). The correct posterior odds are 8 to 1 for sample 1 and 16 to 1 for sample 2, with equal priors (p. 1125). Most people feel sample 1 is stronger evidence because its proportion is higher (p. 1125). Intuitive odds are also far less extreme than the correct ones. This underestimation is called "conservatism" (p. 1125).

*Intuition note.* A big sample and a small one can show the same proportion. They are equally "similar" to the population, but they are not equally reliable. Similarity alone cannot capture reliability.

**Misconceptions of chance.** People expect even short random sequences to look like the process.
- H-T-H-T-T-H is judged more likely than H-H-H-T-T-T, and also more likely than H-H-H-H-T-H (p. 1125).
- Locally representative sequences contain too many alternations and too few runs (p. 1125).
- Gambler's fallacy: after a long run of red, people think black is "due". Deviations are not corrected as chance unfolds, they are "merely diluted" (p. 1125).
- Experienced research psychologists show a "law of small numbers", the belief that even small samples are highly representative. They overtrust small samples, overestimate replicability, and select samples that are too small (p. 1125–1126).

**Insensitivity to predictability.** Predictions are often made by representativeness. The favourableness of a description is unaffected by its reliability, so if people predict solely from favourableness, their predictions will be insensitive to reliability and to expected accuracy (p. 1126).
- Normatively, the extremeness and range of predictions should be controlled by predictability. If predictability is nil, the same prediction should be made in all cases. The higher the predictability, the wider the range of predictions (p. 1126).
- *Student-teacher study.* Predicting a teacher's standing 5 years later gave the same percentile judgments as evaluating the practice lesson. Subjects knew predictability was limited, yet their predictions were as extreme (p. 1126).

**The illusion of validity.** Confidence depends mainly on how well the chosen outcome matches the input, with little regard for factors that limit accuracy. The authors call this unwarranted confidence the "illusion of validity". It persists even when the judge knows these limits, for example in interviewers' confidence despite evidence that interviews are fallible (p. 1126).
- Consistent input patterns raise confidence. Such patterns are most often found when inputs are redundant or correlated.
- Given inputs of stated validity, independent inputs can give higher accuracy than redundant ones. So redundancy lowers accuracy while raising confidence (p. 1126).

**Misconceptions of regression.** For two variables $X$ and $Y$ with the same distribution, if one selects individuals whose average $X$ score deviates from the mean of $X$ by $k$ units, their average $Y$ score will usually deviate from the mean of $Y$ by less than $k$ units. This is regression toward the mean (p. 1126).
- People do not expect regression in many contexts where it must occur. When they recognize it, they often invent spurious causal explanations (p. 1126).
- The authors suggest regression stays elusive because it conflicts with the belief that the outcome should be as extreme as the input (p. 1126–1127).
- *Flight training.* **Instructors' view:** praise after a smooth landing is followed by a worse landing, and criticism after a rough one by improvement. They concluded that punishment works and reward harms. **Authors' reply:** this conclusion is unwarranted because regression alone predicts these changes, even if the instructor's response has no effect (p. 1127).
- Because rewards usually follow good performance and punishments poor performance, by chance alone one is most often rewarded for punishing and punished for rewarding (p. 1127).

*Intuition note.* An extreme result is partly luck, so the next result is likely to be less extreme. If you react to the first result, you may credit your reaction for what luck did.

### Availability (p. 1127–1128)
**Definition.** People assess frequency or probability by the ease with which instances come to mind. This is useful because large classes are usually recalled faster. But availability is also affected by factors other than frequency (p. 1127).

**Retrievability of instances.** Lists of famous and less famous names of both sexes: subjects judged the sex with the more famous names to be more numerous (p. 1127). Salience and recency also matter. The impact of seeing a house burning is probably greater than that of reading about a fire in the local paper, and an overturned car raises the felt accident risk for a while (p. 1127).

**Effectiveness of a search set.** Is a word more likely to start with r, or to have r as the third letter? People find words by first letter more easily, so they judge first-letter words more numerous. This holds even for r and k, which are more frequent in third position (p. 1127). Abstract words (love) are judged more frequent than concrete words (door) of equal objective frequency; the authors suggest this is because contexts for abstract words seem easier to think of (p. 1127).

**Imaginability.** For 10 people forming committees of $k$ members, the number of committees is the binomial coefficient $\binom{10}{k}$, with maximum 252 at $k=5$. It is the same for $k$ and $10-k$, because each committee defines a unique group of $10-k$ non-members (p. 1127–1128).
- Subjects construct committees mentally. Five disjoint 2-member committees are easy to form, but not even two disjoint 8-member ones. So small committees seem more numerous.
- Estimates fell as committee size rose. The median estimate was 70 for committees of 2 and 20 for committees of 8. The correct answer is 45 in both cases (p. 1128).
- The risk of an expedition may be judged by imagined dangers, which need not reflect actual likelihood (p. 1128).

**Illusory correlation.** Naive judges saw hypothetical patients' diagnoses and drawings (Chapman and Chapman). They overestimated how often natural associates co-occurred, such as suspiciousness and peculiar eyes. The effect persisted even when the true correlation was negative (p. 1128). **Authors' account:** availability gives a natural account. The judged frequency of co-occurrence could be based on the strength of the associative bond, so strong associates would be judged to have occurred together frequently (p. 1128).

*Intuition note.* What comes to mind easily feels common. Ease of recall depends on fame, vividness and how we search, not only on how often something happens.

### Adjustment and Anchoring (p. 1128–1130)
People start from an initial value and adjust. Adjustments are typically insufficient, so estimates stay biased toward the starting value. This is called anchoring (p. 1128).

**Insufficient adjustment.**
- A wheel-of-fortune number (0–100) was shown first. Median estimates of the percentage of African countries in the UN were 25 for the anchor 10 and 45 for the anchor 65. Payoffs for accuracy did not reduce the effect (p. 1128).
- Students estimated within 5 seconds either $8\times7\times6\times5\times4\times3\times2\times1$ or $1\times2\times\dots\times8$. The median estimates were 2,250 (descending) and 512 (ascending). The correct answer is 40,320. Both predictions held: underestimation, and a higher estimate for the descending order (p. 1128).

**Conjunctive and disjunctive events.** Bar-Hillel's bets (p. 1129):
- Simple event: red from a 50/50 bag, probability .50.
- Conjunctive: red seven times in a row with replacement, 90% red, probability .48.
- Disjunctive: at least one red in seven tries, 10% red, probability .52.
- A significant majority preferred the conjunctive event to the simple event; subjects also preferred the simple event to the disjunctive one. So most subjects bet on the less likely event in both comparisons (p. 1129).
- (added step: $.9^7\approx .478$ and $1-.9^7\approx .522$.)
- **Authors' explanation:** the probability of one stage is the anchor, and adjustment is insufficient. A conjunction is overestimated and a disjunction underestimated (p. 1129).
- Planning has a conjunctive character, so this leads to unwarranted optimism about completion. Risk in complex systems is disjunctive, so people will tend to underestimate the probability of failure (p. 1129).

**Subjective probability distributions.** A judge is calibrated if exactly $\Pi$ percent of true values fall below his stated $X_\Pi$. The true value should lie between $X_{01}$ and $X_{99}$ in 98 percent of problems (p. 1129).
- In most studies, true values fall outside $X_{01}$–$X_{99}$ for about 30 percent of problems, so the intervals are too narrow. Proper scoring rules do not remove this (p. 1129).
- The authors attribute it at least partly to anchoring on the best estimate (p. 1129).
- *Two elicitation procedures.* (i) Choose values for given percentiles. (ii) Give probabilities that the true value exceeds given values. They are formally equivalent, but should anchor differently. Procedure (ii) should give less extreme odds (p. 1129).
- *Experiment with 24 quantities.* Group 1 gave $X_{10}$ or $X_{90}$. Group 2 received the median of Group 1's values and assessed odds, which should have been 9:1 if unbiased. The median odds were 3:1 (p. 1130).
- Group 1's events given probability .10 occurred 24% of the time (too extreme). Group 2's events with average probability .34 occurred 26% of the time (too conservative). Calibration depends on the elicitation procedure (p. 1130).

### Discussion (p. 1130)
- The biases are not attributed to motivation such as wishful thinking. Several errors occurred despite rewards for accuracy (p. 1130).
- Experienced researchers, including statistically trained ones, are also prone to the same biases when they think intuitively; they avoid elementary errors but are liable to similar fallacies in more intricate, less transparent problems (p. 1130).
- People do not learn rules such as regression or sample-size effects from life, because the relevant instances are not coded appropriately. Example: people do not notice that lines differ more in average word length than pages do. People also seldom group events by judged probability, so they cannot learn that their calibration is poor (p. 1130).
- *Theory.* Modern decision theory defines subjective probability by the bets a person accepts, with coherence from axioms. Its contribution is a rigorous subjective interpretation of probability. The authors add that people normally do not form probabilities from betting preferences. Probabilities determine bets (p. 1130).
- Coherence alone is "not entirely satisfactory". Example: a gambler's-fallacy person can be internally consistent but conflicts with the belief that a coin has no memory. A rational judge must also be compatible with his entire web of beliefs, but there can be no simple formal procedure for checking this. The rational judge will nevertheless strive for compatibility with his knowledge of the subject matter, the laws of probability, and his own heuristics and biases (p. 1130).

### Summary (p. 1131)
The three heuristics are economical and usually effective, but they lead to systematic and predictable errors. Better understanding could improve judgments and decisions (p. 1131).

## Toy example (ours, not from the text)
Aim: show how the "same proportion looks equally representative" shortcut hides a sample-size effect.

A fair coin is flipped. A sample is "extreme" if at least 80% of flips are heads.
- n = 5: at least 4 heads. Count $\binom54+\binom55 = 5+1 = 6$ out of $2^5=32$. Probability $6/32 = .1875$.
- n = 10: at least 8 heads. Count $\binom{10}{8}+\binom{10}{9}+\binom{10}{10}=45+10+1=56$ out of $2^{10}=1024$. Probability $56/1024\approx .0547$.

Both samples "look equally like" an 80% result, so a representativeness judge says "equally likely". The true chance is about $.1875/.0547\approx 3.4$ times higher for the small sample.

## Concepts
- [[heuristic]] — a simple judgmental rule that cuts complex probability tasks to simpler operations; useful but leads to systematic errors (p. 1124)
- [[representativeness / availability / anchoring]] — judging by similarity to a class, by ease of retrieval or construction, and by adjustment from a starting value (p. 1124, 1127, 1128)
- [[base-rate-neglect]] (new) — ignoring prior frequency of outcomes when a description is available (p. 1124–1125)
- [[law-of-small-numbers]] (new) — belief that even small samples are highly representative of their population (p. 1125–1126)
- [[gamblers-fallacy]] (new) — expecting a chance process to self-correct after a run (p. 1125)
- [[regression-toward-the-mean]] (new) — extreme scores on one measure tend to be less extreme on a second equivalent measure (p. 1126)
- [[illusion-of-validity]] (new) — confidence from a good match between input and predicted outcome, with little or no regard for factors that limit accuracy (p. 1126)
- [[illusory-correlation]] (new) — overestimating co-occurrence of events that are strongly associated (p. 1128)
- [[calibration]] (new) — a judge is properly (externally) calibrated in a set of problems if exactly $\Pi$ percent of the true values fall below his stated $X_\Pi$ (p. 1129)
- [[subjective expected utility]] — here only the axiomatic subjective-probability side: probability defined by accepted bets, with coherence (p. 1130)

## Canonical instances
- [[steve-librarian]] — description "Steve" shows similarity-based occupation judgments (p. 1124)
- [[engineer-lawyer-experiment]] — base rates 70/30 vs 30/70 produce the same judgments (p. 1124–1125)
- [[two-hospitals-problem]] — sample-size insensitivity (p. 1125)
- [[flight-instructors-reward-punishment]] — regression mistaken for causal effect of praise and blame (p. 1127)
- [[r-words-letter-position]] — availability via search sets (p. 1127)
- [[committees-of-ten]] — imaginability misjudges $\binom{10}{k}$ (p. 1127–1128)
- [[anchoring-factorial-products]] — ascending vs descending multiplication (p. 1128)
- [[bar-hillel-bets]] — conjunctive/disjunctive misjudgment (p. 1129)
- [[dow-jones-confidence-intervals]] — overly tight subjective distributions (p. 1129)

## Bridges (candidates)
- [structural-analogy] Insensitivity to prior probability ↔ Bayesian updating: the judge acts as if the likelihood ratio alone fixed the posterior odds.
- [same-math] Regression toward the mean ↔ statistics of correlation: the regression of $Y$ on $X$ when $r<1$ gives the shrinkage the text describes.
- [metaphor] Overly narrow intervals ↔ bias–variance idea: sample-based intuitions overtrust small samples and are too confident (canon link; not stated in this unit).
- [metaphor] Anchoring and adjustment ↔ bounded rationality: limited effort stops adjustment early.
- [structural-analogy] Coherence vs compatibility ↔ subjective expected utility: consistency of bets does not guarantee sensible beliefs.

## Questions this raises
- Why do heuristics persist if they cause predictable errors, and when are they better than formal rules?
- Could training or better feedback (e.g., tallying calibration) fix these biases?
- How do the three heuristics interact in one judgment?
- If coherence is not enough for rationality, how can compatibility with one's whole belief system be tested?

## Reading notes
- Printed pages 1124–1131 contain the paper. Printed = pdf + 1123. Page 1131 also holds an unrelated article ("Rural Health Care in Mexico?"), ignored here. Page 1132 is only the Science download information sheet.
- The text layer is garbled in places. It prints "23" for the urn's "2/3". I read it as 2/3, consistent with the stated odds (8 to 1, 16 to 1). Percentile symbols such as "X1o", "XAT0", "X0l", "X19", "XIo", "Xgo" are OCR noise. Context shows $X_{10}$, $X_{90}$, $X_{01}$, $X_{99}$.
- The text layer reads "(.7/.3)2" for the squared odds ratio, so I wrote $(.7/.3)^2$. I only had a page image for p. 1131 and p. 1132, so the other pages rest on the text layer.
- The paper has no numbered sections. The headings follow the printed headings (Representativeness, Availability, Adjustment and Anchoring, Discussion, Summary).
