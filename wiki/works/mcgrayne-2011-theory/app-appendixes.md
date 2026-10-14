---
id: mcgrayne-2011-theory/app-appendixes
work: mcgrayne-2011-theory
unit: "Appendixes (A: Dr Fisher's Casebook; B: Applying Bayes' Rule to Mammograms and Breast Cancer)"
pages: 253-258
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Appendixes: statistics as religion, and Bayes' rule on mammograms

## L0 — One line
Appendix A jokes that statisticians' camps resemble religions; Appendix B shows that a positive routine mammogram in a woman in her forties still means only about a 3% chance of cancer, because the disease is rare.

## L1 — The gist (≤ 120 words)
Appendix A, a humorous essay by Michael J. Campbell, compares frequentists and Bayesians (two schools of statistics) to religious groups. He calls himself an "Anglican" who steers a "middle way". Appendix B asks: a 40-year-old woman with no symptoms gets an abnormal mammogram; how likely is it that she has cancer? Bayes' rule combines the low background rate of the disease with the test's hit rate (share of sick women it finds) and false-positive rate (share of healthy women it flags). The answer is about 3%. The author says this calculation lay at the heart of the controversy over the 2009 screening advice. The appendix ends with the general rule $P(A|B)=P(A)P(B|A)/P(B)$.

**Prerequisites:** percentages and fractions; the idea of "probability of X given Y".

## L2 — Key ideas (5–10 bullets)
- Campbell (voice of Appendix A) casts frequentists as "Catholics": significant/non-significant replaces mortal/venial sin, the prayer begins "Our Fisher, who art in Heaven", and Pearson and Neyman are the saints (p. 253).
- He casts Bayesians as "born-again fundamentalists" who "believe", can often name the day Bayes entered their lives, and try to convert others (pp. 253–254).
- His own position is a "middle way": he uses p-values and confidence intervals (standard frequentist tools) but tempers them with prior beliefs (what one believes before seeing the data), and likes empirical Bayes (p. 254).
- Appendix B: a good screening test can still give mostly false alarms when the disease is rare. The test finds about 80% of cancers, gives a positive result to about 10% of healthy women (false positives), and the disease rate is about 0.4% (pp. 255–256).
- Bayes' rule counts the background disease rate as prior knowledge (p. 255).
- Worked result: 32 true positives among 1028 positives per 10,000 women, so about 3% (pp. 256–257).
- Policy reading: Bayes points to better tests and fewer false positives, and the calculation should be redone as new data arrive (p. 257).
- General form: $P(A|B)=\dfrac{P(A)P(B|A)}{P(B)}$, with A a hypothesis and B data (p. 257).

## L3 — Walkthrough

### Appendix A — "Dr Fisher's Casebook: The Doctor Sees the Light" (Michael J. Campbell)
- **Frequentists as Catholics (Campbell's joke).**
  - "Significant"/"nonsignificant" results replace mortal/venial sins.
  - Randomisation is "the grace that saves the world".
  - A priest wants the frequency of sins, like a statistician wanting a bar chart.
  - Rejecting a null hypothesis at $p<0.05$ is like absolution: once published, one may use 0.05 as the limit again.
  - The prayer begins "Our Fisher, who art in Heaven". The saints are Pearson and Neyman, and the null and alternative hypotheses stand in for Heaven and Hell (p. 253).
- **Bayesians as born-again fundamentalists (Campbell's joke).**
  - One must be a "believer". Bayesians can often name the day Bayes came into their lives.
  - Reverend Thomas Bayes is their guide. Like the Christian God he did not publish in his lifetime.
  - Bayesians ask strangers "are you a Bayesian?", express amazement at non-Bayesians and try to convert them (pp. 253–254).
- **Sects.** Agnostics favour non-parametric statistics, bootstrappers do without "God", the "bell-curve" cult explains everything by the Normal distribution, and simulators think God is a human invention (p. 254).
- **Campbell's own stance.**
  - He is "Anglican": he steers a middle way and sees danger in extremism either way.
  - He still uses p-values and confidence intervals, tempered by prior beliefs.
  - He likes empirical Bayes (using earlier studies to inform priors).
  - He can see advantages of Bayesian methods for modelling complex systems and attaching uncertainty to parameters, and thinks that in many ways they reflect scientific inference better.
  - He prefers simply to call himself "a believer" without a label (p. 254).
- **Closing cartoon.** Monks stand for a vague prior (looking lost), a uniform prior (dressed as a soldier), an informative prior (holding a guide book) and an improper prior (tongue stuck out) (p. 254).

*Intuition note:* The essay is humorous. It treats loyalty to a statistical "camp" as resembling religious faith. Campbell says he is happy to use whatever means help him find the truth.

### Appendix B — Bayes' rule applied to mammograms
- **Setting.** In 2009 a U.S. government task force advised most women in their forties not to have annual mammograms. The public reaction was immediate and largely enraged. The appendix gives a simple version of the Bayesian calculation behind the controversy (p. 255).
- **Question.** A 40-year-old woman with no symptoms or family history gets an abnormal routine mammogram. What is the probability she has cancer? The author's answer: "Quite low" (p. 255).
- **Test properties.** The test identifies roughly 80% of 40-year-old women who have cancer at the time of the exam. It gives positive results to only about 10% of women without the disease (p. 255).
- **Why this surprises people.** Breast cancer is relatively rare, and Bayes' rule counts background rates as prior knowledge. Not everyone with a positive test has the disease. The probability of cancer is higher for a woman who finds a lump than for one screened routinely (p. 255).
- **Formula in words.** Probability of cancer given a positive mammogram = (probability of a positive mammogram among cancer patients) × (probability of having breast cancer), divided by the probability of a positive mammogram (p. 256; the text layer scrambles the fraction layout, but the final formula on p. 257 is clear).
- **Three inputs, per 10,000 women in their forties (p. 256):**
  1. Prior: about 0.4% have cancer, so 40 per 10,000, i.e. $40/10{,}000$.
  2. Hit rate: about 32 of those 40 test positive, i.e. $32/10{,}000$ of all women screened.
  3. All positives: 996 healthy women get an abnormal result (the 10% false-positive rate), plus the 32 cancer patients, giving $1028/10{,}000$, "a little more than 10%".
- **Result** (p. 257):
$$P(A|B)=\frac{P(A)\,P(B|A)}{P(B)}=\frac{\frac{40}{10{,}000}\times\ldots}{\frac{1028}{10{,}000}}\approx 0.03$$
  - The text layer garbles the printed arithmetic, so the middle factors are omitted rather than guessed.
  - (added step) The ratio of counts is $32/1028\approx0.0311$.
  - The author's result is 3%: a woman with a positive test has about 97 chances in 100 of being disease-free (p. 257).
- **Consequences (author's reading).** Universal screening for a disease affecting 0.4% of the population may cause needless worry and treatment, which can have their own medical problems. The money spent on universal screening could potentially be used for other worthwhile projects. Bayes highlights the need to improve screening and cut false positives. Negative results miss 1 in 5 cancers. Bayes' rule should be recalculated as new research data arrive (p. 257).
- **General rule** (p. 257): $P(A|B)=\dfrac{P(A)P(B|A)}{P(B)}$, "where A is a hypothesis and B is data."

*Intuition note:* Among 10,000 women, only 32 sick women test positive, but 996 healthy women do too. So most positives are false alarms, even though the test catches 80% of cancers.

## Toy example (ours, not from the text)
A disease affects 2% of people. A test detects 90% of sick people and wrongly flags 5% of healthy people. Take 1,000 people.
- Sick: $1000\times0.02=20$. Of these, $20\times0.90=18$ test positive.
- Healthy: $1000-20=980$. Of these, $980\times0.05=49$ test positive.
- All positives: $18+49=67$.
- Probability of disease given a positive: $18/67\approx0.269$, about 27%.

The 90% test still gives a positive result that is wrong nearly three times in four, because healthy people far outnumber sick ones.

## Concepts
- [[bayes-theorem]] — $P(A|B)=P(A)P(B|A)/P(B)$, with A a hypothesis and B data (p. 257)
- [[prior-distribution]] — here, the background disease rate (0.4%) used as prior knowledge (p. 255)
- [[base-rate-neglect]] — surprise that a positive test on an accurate screen means low risk; the text does not use the term (p. 255)
- [[frequentist-vs-bayesian]] — presented satirically as two "religions" (pp. 253–254)
- [[false-positive]] (new) — a positive test result in a person without the disease (p. 256)
- [[empirical-bayes]] (new) — using earlier studies to inform one's priors (p. 254)
- [[vague-uniform-informative-improper-prior]] (new) — four kinds of prior, named in the cartoon (p. 254)

## Canonical instances
- [[mammogram-screening-2009]] — a 3% chance of cancer after a positive routine mammogram at 40 (pp. 255–257)

## Bridges (candidates)
- [structural-analogy] Campbell's "religion" metaphor ↔ sociology of science: methodological camps as identity groups
- [same-math] Mammogram calculation ↔ Bayes' theorem (HS level): natural-frequency counts equal the formula
- [metaphor] "Born-again" Bayesian conversion ↔ paradigm shifts in science

## Questions this raises
- If the test is applied only to women who find a lump, which input changes, and by how much?
- How would the answer change if the false-positive rate fell from 10% to 5%?
- How does "empirical Bayes" choose a prior from earlier studies?
- Should one use p-values and Bayesian priors together, as Campbell suggests?

## Reading notes
- Printed page = pdf page − 15. Printed page 258 is blank.
- No page images were supplied, so the text layer alone was used. The fraction layouts on pp. 256–257 are garbled in it, and I could not check them against an image.
- In the text, $32/10{,}000$ is labelled "the probability of a breast cancer patient getting a positive mammogram". As a conditional probability this would be $32/40=80\%$, as stated on p. 255. The $32/10{,}000$ is the joint share of all women screened. The final 3% is consistent with $32/1028$.
- Appendix A is attributed to Michael J. Campbell; Appendix B is unsigned.
