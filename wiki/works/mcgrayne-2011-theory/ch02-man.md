---
id: mcgrayne-2011-theory/ch02-man
work: mcgrayne-2011-theory
unit: "2. The Man Who Did Everything"
pages: 13–33
fields: [bayesian]
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
# The Man Who Did Everything (Laplace and the "probability of causes")

## L0 — One line
Pierre Simon Laplace, independently of Bayes, built the "probability of causes" into the general rule we now call Bayes' rule, and the author says the rule was really his achievement, even though usage keeps Bayes' name.

## L1 — The gist (≤ 120 words)
Who turned Bayes' idea into a working method? The chapter follows Laplace (1749–1827). He wanted to handle error-filled astronomical observations, so he worked out a "probability of causes" in 1774, with equal starting probabilities for all causes. In 1781 he learned of Bayes' starting guess. Between 1810 and 1814 he reached the general formula with unequal priors. He applied it to births, population counts, court verdicts and astronomy. After 1810 he relied mainly on frequency-based methods, because with large amounts of reliable data the two approaches generally give much the same results. The author says that, if advancing knowledge is what counts, the rule should be called Laplace's rule or Bayes-Price-Laplace, though usage keeps Bayes' name.

**Prerequisites:** basic probability (conditional probability, odds, sums of probabilities equal 1); ratios and percentages. No calculus needed.

## L2 — Key ideas (5–10 bullets)
- Laplace's problem was uncertain data, not wrong theory: he decided Newton's theory was fine and that astronomers' observations were the issue (p. 17).
- His 1774 principle moves backward from an effect to its most likely cause. It is stated in words, and in this form it assumes all causes start equally likely (pp. 20–21, 23).
- He found the idea independently of Bayes. Learning of Bayes' starting guess in 1781 confirmed that his 1774 principle was right for equal priors (pp. 22–23).
- The method was applied to real data: boy/girl birth ratios, the French population, jury verdicts, and the masses of Jupiter and Saturn (pp. 24–28, 32).
- Big-number arithmetic was a major obstacle, and he invented approximations and generating functions to get around it (pp. 24–25).
- The central limit theorem (1810) justified averaging. Laplace then switched mainly to frequency methods, since both approaches usually agree on large reliable data (pp. 30–31).
- The general rule with an explicit prior and a sum over all hypotheses came between 1810 and 1814 (p. 31).
- Laplace kept religion out of the method. He resolved the stability of the solar system by other means (pp. 28, 30).

## L3 — Walkthrough

### Boyhood and education (pp. 13–15)
- Born March 23, 1749, in Normandy, son of the village mayor and inn-keeper. His father enrolled him in a Benedictine school with a Latin, memorization-heavy curriculum. It gave him a fabulous memory and great perseverance (pp. 13–14).
- Halley's comet returned on schedule in 1759, as French astronomers had predicted. Later Laplace said this made his generation see that comets and droughts came from natural laws, not divine anger (p. 14).
- He studied at the University of Caen from 1766. There he learned Leibniz-style algebraic calculus and became a religious skeptic (p. 14).

### Choosing mathematics; Paris and the Academy (pp. 15–18)
- He refused the clerical path his father wanted. In 1769 he went to Paris with a letter to d'Alembert. Within days d'Alembert got him a teaching post at the Royal Military School (pp. 15–16). He did not return home for 20 years (p. 15).
- To do full-time research he needed election to the Royal Academy of Sciences, so he needed a spectacular impact (p. 16). D'Alembert urged astronomy (p. 16).
- The burning question was whether the solar system is stable. Jupiter seemed to accelerate and Saturn to slow down. Newton had concluded that God's intervention kept equilibrium (p. 17).
- Laplace briefly considered modifying Newton's theory, then decided the problem was the data. Observations came from Chinese, Chaldean, Greek, Roman and Arab astronomers, and not all were equally valuable (pp. 17–18).
- Astronomers typically averaged their three best observations. No one had justified this by theory or by test (p. 18).
- He sent 13 papers in five years. He was considered six times and rejected, and was elected March 31, 1773. His mémoire on the probability of causes was published in 1774 (pp. 18, 22).

> **Intuition note:** Laplace's starting question was practical: when measurements disagree, which should you trust? That question led him to probability.

### Probability as a way to handle ignorance (pp. 19–20)
- In the Military School library he found de Moivre's *Doctrine of Chances*, a gambling-probability book (p. 19).
- **D'Alembert's view:** probability is too subjective for science. **Laplace disagreed:** probability would not give absolute answers, but could show which data were more likely correct (p. 19).
- He called his idea "the probability of causes" because Continental mathematicians did not yet know of Bayes (p. 19).
- In 1773 he wrote that probability is the mathematical expression of our ignorance, since humans can never know everything with certainty (p. 19).

### The first version of the rule, 1774 (pp. 20–22)
- About ten years after Bayes' essay, an astronomy journal made Laplace think others were on the same trail. He turned an old manuscript into the "Mémoire on the Probability of the Causes Given Events" (p. 20).
- Gamblers know the odds of an event given its cause (the dice). In science he often did not know such odds. His leap was to consider all possible causes and then choose among them (p. 20).
- He stated it only in words: the probability of a cause (given an event) is proportional to the probability of the event (given its cause). The author shows the modern form (p. 20):

$$P(C\mid E)=\frac{P(E\mid C)}{\sum P(E\mid C')}$$

Here $P(C|E)$ is the probability of a cause given the data. $P(E|C)$ is the probability of the datum given that cause. The sum in the denominator makes the probabilities of all possible causes add to one (p. 20).
- With this he could do everything Bayes could have done, provided all causes were equally likely (p. 21). Proportionality also made large calculations feasible with quill and ink (p. 21).
- Applications: an urn with an unknown ratio of black and white tickets (what is the probability the next ticket is white?). He needed 45 equations over four pages to prove an answer he already sensed. Another case: dividing the kitty in a stopped game of piquet by estimating players' skill. In a third, averaging three discrepant observations needed seven pages of equations (p. 21). He had no mathematical justification for averaging until 1810, when he invented the central limit theorem without using the probability of causes (p. 21).

> **Intuition note:** Instead of asking "what happens if the cause is X?", he asked "given what happened, how plausible is each X?". The 1774 form simply rescales the likelihoods of the causes so they sum to 1.

### Independence from Bayes (p. 22)
- The Bayes–Price essay appeared in an English journal and was apparently never mentioned again. French scientists thought Laplace was first (p. 22).
- The author says mathematics confirms independence. Bayes solved a special flat-table problem in two steps (prior guess plus new data). Laplace treated the problem generally but did not yet have the initial guess (p. 22).
- Bayes explained why uniform probabilities were permissible. Laplace assumed them instinctively (p. 22).
- Laplace wanted the probability that measured values were realistic, refining his opinion over and over with new information (p. 22). The author says his method was immensely influential, and scientists did not pay Bayes serious heed until the twentieth century (p. 22).

### 1781: Price's starting guess (p. 23)
- Price visited Paris in 1781 and told Condorcet of Bayes' discovery. Laplace incorporated the starting guess. Strictly speaking, this was not a new formula but a statement about the first formula assuming equal probabilities. It told him that, if all prior hypotheses were equally probable, his 1774 principle was correct (p. 23).
- He could then use each answer as the starting point for the next calculation (p. 23). He later credited Bayes publicly as first (p. 23).
- **Laplace's own complaint:** assigning equal probabilities was a limitation. Dice that look perfect are often skewed, and players' skills show up during play. The science of chances must be modified "when we pass from the mathematical case to the physical" (p. 23).

### The big-number problem (pp. 23–25)
- Repeated multiplication gave huge numbers, and he had no assistant until about 1785 (p. 24). His example was 20,000 × 19,999 × 19,998 × 19,997 … divided by 1 × 2 × 3 × 4 … up to 10,000 (p. 24).
- The author says Laplace's inventions included new generating functions, transforms and asymptotic expansions (p. 25). He used generating functions to trick a function he could handle into giving the one he wanted (p. 25).

### Counting babies (pp. 24–27)
- He needed large, trustworthy data. The author says parish records were the only such data in the 1700s. Paris data showed slightly more boys than girls, in a ratio that stayed constant (p. 24).
- Babies suited his purposes: they come as binomials (boy or girl), and the difference is small, so large numbers are needed (pp. 24–25). A Burgundy village with more girls for five years did not refute him, because a few facts cannot overrule a larger study (p. 25).
- A 52:48 start with 58,000 boys would mean multiplying .52 by itself 57,999 times (p. 25).
- He started provisionally with equal probabilities for his hunches (50–50, 33–33–33, 25–25–25–25), and his final hypotheses depended on all the data (p. 25).
- From christening and birth records he was willing to bet boys would outnumber girls for the next 179 years in Paris and 8,605 years in London (p. 25).
- He collected birth ratios from Naples to St. Petersburg over 30-odd years and concluded climate could not explain the disparity (p. 26). As evidence accumulated, his probabilities approached certainty "at a dramatically increasing rate" (p. 26).
- By 1786 he could handle future composite events, such as a year of births, even when the probability of a single birth was uncertain (p. 26). In 1812 he cautiously concluded that more boys than girls seemed to be "a general law for the human race" (p. 27).

> **Intuition note:** Each new birth record shrinks the range of uncertainty, as each coin toss makes "fair or rigged" clearer (p. 26). A few facts cannot overturn many.

### Population and courts (pp. 27–28)
- **Population:** an administrator advised multiplying annual French births by 26, giving about 25.3 million. Laplace combined the prior information from parish records with headcounts in eastern France (p. 27). In 1786 he gave odds of 1,000 to 1 that his estimate was off by less than half a million. In 1802 he advised Napoleon to add samples of about a million residents in 30 departments to a new census (p. 27).
- **Courts:** at Condorcet's urging, Laplace applied probability to testimony, juries and voting (p. 27). He set the prior odds of guilt at 50–50 and the probability that a juror was truthful somewhat higher. Even so, for a jury of eight voting by simple majority, the chance of a wrong verdict would be 65/256, more than one in four (p. 28). He cited this against capital punishment (p. 28).

### Solar-system stability and the Revolution (pp. 28–30)
- Between 1785 and 1788 he used other methods, not probability of causes, to show Jupiter and Saturn oscillate in an 877-year cycle. Hence the solar system was in equilibrium (p. 28).
- He married at 39. Some 16 months later the Bastille fell (pp. 28–29). During the Terror he was briefly arrested, then freed. He took no part in radical politics, unlike several friends who died (p. 29). He named the meter, centimeter and millimeter (p. 29).
- Napoleon favored him. **Napoleon** asked why Laplace's book never mentioned God. **Laplace replied:** "I have no need of that hypothesis" (p. 30). The author contrasts this with Price's idea that Bayes' rule could prove God's existence (p. 30).

### The central limit theorem and the switch (pp. 30–31)
- In 1810 he announced the central limit theorem. The author states it as: with some exceptions, any average of many similar terms has a normal, bell-shaped distribution (p. 30).
- It let him deal with almost any kind of data, whereas his probability of causes had limited him to binomial problems (p. 31).
- At 62 he switched mainly to a frequency-based approach he had also developed, and relied on it from 1811 until death. His reason: with large amounts of data both approaches generally give much the same results. The author adds that mathematicians learned only in the mid-twentieth century that even with great amounts of data the two can sometimes seriously disagree (p. 31).
- Probability of causes remained more powerful in particularly uncertain cases (p. 31).
- Looking back in 1813, Laplace described it as the primary method for researching unknown or complicated causes of natural phenomena, and as the inspiration behind his generating functions (p. 31).

> **Intuition note:** With plenty of reliable data, the author says both approaches generally give much the same results, and frequentism was easier to use on trustworthy data. This is the author's account of why Laplace switched. It is not a claim that the methods are equivalent, since the author adds that they can sometimes seriously disagree.

### The general rule, 1810–1814 (pp. 31–32)
- Between 1810 and 1814 Laplace saw what the general theorem had to be. In modern terms (p. 31):

$$P(C\mid E)=\frac{P(E\mid C)\,P_{\text{prior}}(C)}{\sum P(E\mid C')\,P_{\text{prior}}(C')}$$

The prior $P_{\text{prior}}(C)$ is the initial estimate of the hypothesis. $P(E|C)$ is the probability of the new information under the hypothesis. The denominator sums over all possible hypotheses (pp. 31–32).
- The first (discrete) version covers coin tosses and births. Later versions use calculus for continuous ranges (p. 32).
- The author says Laplace had owned Bayes' rule in all but name since 1781 and that the formula, the method and its masterful use all belong to him. She quotes Glenn Shafer: "Laplace did everything, and we just read stuff back into Thomas Bayes" (p. 32).
- The author adds that, if advancing the world's knowledge is important, the rule should be called Laplace's rule or BPL (Bayes-Price-Laplace). She says that, sadly, a half century of usage forces us to give Bayes' name to what was really Laplace's achievement (p. 32).

### Late applications, death (pp. 32–33)
- In 1815 he applied the rule to astronomy, using Bouvard's tables. He bet 11,000 to 1 that Bouvard's mass for Saturn was off by less than 1%, and a million to one for Jupiter. The author says space-age technology confirms he should have won both bets (p. 32).
- He used the rule in Earth science and a nonnumerical version for his nebular hypothesis. Comparing three hypotheses on 100 comets' orbits, he confirmed that comets most probably originate within the sun's sphere of influence (pp. 32–33).
- He died March 5, 1827, aged 78 (p. 33). The author says he built his probability theory on intuition. Laplace himself called probability "nothing but good common sense reduced to mathematics". Critics began complaining about his rule as soon as he was buried (p. 33).

## Toy example (ours, not from the text)
A coin is either cause C1 "fair" ($P(\text{heads})=0.5$) or C2 "biased" ($P(\text{heads})=0.8$). One toss gives heads (E).

1. **Equal priors, the 1774 form:** $P(C1|E)=0.5/(0.5+0.8)=0.5/1.3\approx0.385$, and $P(C2|E)=0.8/1.3\approx0.615$. These sum to 1.
2. **Unequal priors, the general form,** with $P_{\text{prior}}(C1)=0.9$ and $P_{\text{prior}}(C2)=0.1$:
   - Numerator for C1: $0.5\times0.9=0.45$. For C2: $0.8\times0.1=0.08$.
   - Denominator: $0.45+0.08=0.53$.
   - $P(C1|E)=0.45/0.53\approx0.849$, and $P(C2|E)=0.08/0.53\approx0.151$.

The same evidence gives different conclusions once the prior is included. That is what the 1810–1814 general rule added.

## Concepts
- [[bayes-theorem]] — Laplace's 1774 and 1810–14 formulas for moving from effect to probable cause (pp. 20, 31)
- [[prior-distribution]] — the initial estimate $P_{\text{prior}}(C)$; first assumed equal for all causes (pp. 23, 31)
- [[likelihood]] — $P(E|C)$, the probability of the event given the cause (p. 20)
- [[posterior-distribution]] — $P(C|E)$, the updated probability of a cause given the data (p. 20)
- [[sequential-updating]] — each answer becomes the starting point for the next calculation (p. 23)
- [[principle-of-indifference]] — equal prior probabilities as a provisional starting point (p. 25)
- [[frequentist-vs-bayesian]] — Laplace's switch, after 1810, to a frequency-based approach (p. 31)
- [[probability-of-causes]] (new) — Laplace's name for inference from known events back to probable causes (p. 19)
- [[central-limit-theorem]] (new) — with some exceptions, any average of a large number of similar terms has a normal, bell-shaped distribution (p. 30)
- [[generating-function]] (new) — Laplace's device to turn a function he could handle into one he needed (p. 25)

## Canonical instances
- [[laplace-birth-ratio]] (new) — boys outnumber girls; evidence accumulates until near-certainty (pp. 24–27)
- [[laplace-french-population]] (new) — combining prior parish data with eastern-France headcounts; odds of 1,000 to 1 (p. 27)
- [[laplace-jury-reliability]] (new) — 50–50 prior of guilt; eight-juror majority errs with probability 65/256 (p. 28)
- [[bouvard-planet-masses]] (new) — odds of 11,000 to 1 (Saturn) and a million to one (Jupiter) (p. 32)
- [[urn-of-tickets]] (new) — urn with unknown black/white ratio; probability the next ticket is white (p. 21)

## Bridges (candidates)
- [structural-analogy] Laplace's switch to frequentism with abundant data ↔ Bayesian inference: our gloss on the prior's role in the Bayesian method; the author says only that with large amounts of data both approaches generally give much the same results.
- [same-math] 1774 formula with equal priors ↔ Bayes' theorem with a uniform prior over a discrete set of hypotheses — it is the general formula with equal $P_{\text{prior}}$ cancelling.
- [metaphor] "Probability expresses our ignorance" ↔ subjective probability as degree of belief — Laplace ties probability to what we do not know.

## Questions this raises
- How do the "frequency-based approach" and the probability of causes sometimes disagree, even with large data (p. 31)?
- Why did early critics begin attacking the rule right after Laplace's death (p. 33)?
- How should a modern analyst choose priors, given Laplace's own doubt about assigning equal probabilities (p. 23)?
- How did the central limit theorem justify averaging, which Laplace had only intuited (pp. 21, 31)?

## Reading notes
- Printed = pdf − 15. Only pdf 39 was available as an image. The text layer for the other pages read cleanly, and the two formulas (pp. 20, 31) were taken from it. They agree with the surrounding prose.
- The chapter has no numbered sections or equation numbers. The headings in L3 are ours, and the page ranges are printed pages.
- Endnote markers were dropped. Dates are as the author gives them.
