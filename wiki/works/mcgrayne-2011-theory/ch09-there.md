---
id: mcgrayne-2011-theory/ch09-there
work: mcgrayne-2011-theory
unit: "9. There's Always a First Time"
pages: 119-128
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# There's Always a First Time

## L0 — One line
In 1957–58 Albert Madansky used a Bayesian prior that was not all at zero to argue that an accidental H-bomb explosion could not be ruled out, even though none had ever happened.

## L1 — The gist (≤ 120 words)
How can you estimate the chance of an event that has never occurred? RAND analyst Albert Madansky faced this question about accidental H-bomb explosions. SAC (the Strategic Air Command, which flew the bombers) and frequentist statistics treated zero past accidents as zero future risk. Madansky instead gave the accident probability a prior that was not all at zero, and counted future "accident opportunities". He concluded that it was highly probable that the planned expansion of armed flights would be accompanied by 19 "conspicuous" weapon accidents each year. LeMay, according to Iklé, then ordered safety measures such as the two-man rule and coded locks. The chapter shows Bayes' rule working on a problem where frequency counts gave no help.

**Prerequisites:** the idea of a prior probability; basic probability of repeated trials; the contrast between "probability as long-run frequency" and "probability as degree of belief".

## L2 — Key ideas
- Savage met Iklé at RAND in 1957 and handed the H-bomb accident problem to Madansky. Madansky found a Bayesian approach on his own (p. 120).
- The problem was hard because no nuclear weapon had ever exploded accidentally. Leaders reasoned that none could in future (p. 121).
- McGrayne says conventional statistics held that the impossible could not be calculated, and that Fisher's frequency view left only the observation of zero accidents and a future probability that was also zero (p. 121).
- Many accidents had occurred with unarmed weapons, and nuclear arsenals were growing. Madansky therefore doubted that the future probability was zero (pp. 121–123).
- Madansky's prior had some probability above zero on accidents, in the spirit of Cromwell's Rule. He used a deliberately weak, minimal prior (pp. 123–124).
- McGrayne calls the counting of "accident opportunities" an important innovation: a tiny per-operation risk can become significant over many operations. Madansky hoped to do the calculation by pencil and paper, using a tractable prior of the kind later called conjugate (p. 125).
- Result: it was highly probable that expanded airborne alert would be accompanied by 19 "conspicuous" weapon accidents per year. According to Iklé, LeMay then ordered safety measures such as the two-man rule and coded locks (pp. 125–127).

## L3 — Walkthrough

**Setting: RAND, 1957 (pp. 119–120).**
- RAND was a Cold War think tank funded by the U.S. Air Force. It used mathematics, statistics and computers on military problems and on decisions under uncertainty (p. 119).
- Savage visited in summer 1957. He talked with Fred Iklé, who studied catastrophes that deterrence would not prevent, namely accidents and mental derangement (p. 120).
- Savage handed the H-bomb study to Madansky, a 23-year-old graduate of his department. Madansky had earlier worked part-time for the Bayesian insurance theorist Arthur Bailey (p. 120).
- Savage had published *Foundations of Statistics* but had not yet embraced Bayes' rule. He did not frame the problem in Bayesian terms (p. 120).
- The report stayed classified, so Madansky could not discuss his work for 41 years (p. 120).

**The statistical problem (p. 121).**
- No atomic or hydrogen weapon had exploded accidentally. **Leaders' view:** barring accidents, nuclear stocks deterred war, and accidents could not occur in future because none had occurred in the past (p. 121).
- McGrayne lists "conventional" views that the impossible cannot be calculated: Bernoulli (1713: highly improbable events do not happen), Hume (the sun will rise), Cournot (a physically impossible event has infinitely small probability) and Kolmogorov (a very small probability means practical certainty of no event in the next trial) (p. 121). Price took the contrary view that the highly improbable can occur (p. 121).
- On McGrayne's account, Fisher's frequency view left only the "banal observation" of zero accidents and hence zero future probability (p. 121).
- **Madansky:** if you are set on zero, nothing will change your mind until the sun fails to rise (p. 121).

**Why zero was doubtful (pp. 121–123).**
- Nuclear weapons were spreading. The Soviets, Britain and France had tested bombs, and the USA supplied missiles to allies (pp. 121–122).
- A classified list gave 16 "dramatic incidents" from 1950 to 1958: drops, jettisons, crashes and testing errors (p. 122).
- A bomb explodes with a nuclear blast only if its conventional high explosives detonate simultaneously around the nuclear capsule. In a few cases the high explosives detonated, generally on impact in a plane crash; the nuclear capsule had not been installed, so there was no nuclear accident. That fact convinced SAC that its procedures were sound (p. 122).
- Examples: deaths in B-29 and B-50 crashes in 1950, and the 1958 Mars Bluff bomb, described as relatively harmless, which dug a crater but killed no people (pp. 122–123). Also the Sidi Slimane fire, which destroyed a weapon and its capsule (p. 123).
- Madansky then felt he could no longer assume an H-bomb accident could never occur, and wanted another kind of inference in which an accident's probability was not necessarily zero (p. 123).
- He turned to Bayes. **Madansky:** "if you're willing to admit a shred of disbelief, you can let Bayes' theorem work" (p. 123).
- Lindley's point: a prior of zero cannot be shifted by any evidence, as with the green-cheese moon. Cromwell's Rule says "think it possible you may be mistaken" (p. 123).
- Reliability engineers already used Bayesian methods on missile test data (pp. 123–124).

*Intuition note:* A prior of exactly zero cannot be changed by any amount of evidence. Allowing a small chance that accidents are possible keeps the question open, so data and counts of opportunities can then matter.

**Building the model (pp. 124–125).**
- Madansky assumed an a priori distribution of the per-opportunity accident probability "not all concentrated at zero" (p. 124).
- Once a Bayesian allowed that even one small accident might have occurred in the past 10,000 opportunities, the probability of an accident-free future dropped significantly (p. 124).
- He kept the prior minimally informative, "considerably weaker than 50–50", to avoid assumptions the military would reject (p. 124).
- The accident-free future depends on the length of the accident-free past and on the number of future opportunities (p. 124).
- He counted "accident opportunities" from the number of weapons, their longevity, and how often they were aboard planes or in storage. McGrayne calls this counting "an important innovation" (p. 125).
- **Madansky:** a one-in-a-million risk becomes significant if the operation occurs 10,000 times in five years (p. 125).
- Planned expansion: SAC planned 1,800 bombers capable of carrying nuclear weapons, about 15% of them in the air at all times, armed and ready. A B-52 carried up to four nuclear bombs, each with explosive power up to the equivalent of 1,850 Hiroshima bombs (pp. 124–125).
- Air force data: 5 major B-52 accidents per 100,000 flying hours, and roughly 3 bombs dropped or jettisoned per 1,000 flights carrying them (p. 125).
- Computation: he hoped to avoid RAND's computers. Many priors and posteriors share the same probability curves, which Raiffa and Schlaifer later called conjugate priors. Madansky had chosen his prior "ad hoc" (p. 125).
- The pages do not give his formula or the steps behind his figure (see Reading notes).
- Result: it was "highly probable" that the expanded alert would be accompanied by 19 "conspicuous" weapon accidents each year, using his tractable prior, classified military data and informed guesswork (p. 125).

*Intuition note:* A very small risk per operation adds up across thousands of operations. Counting operations, not only past accidents, turned "none so far" into a warning.

**Report and aftermath (pp. 126–128).**
- Report RM-2251, dated 15 October 1958, was classified and released 9 May 2000. Madansky wrote an elementary summary for decision makers (p. 126).
- Iklé and Madansky recommended safety features: a two-person arming rule, coded locks, and arming only over enemy territory, among others. The report also recommended placing reassuring articles in scientific journals about plutonium emissions, with the source of the research disguised (p. 126). Madansky could not predict when or where an accident would occur, but was sure the likelihood was rising and that it was in the military's interest to make the arsenal safer (p. 126). An appendix by Iklé and the psychiatrist Aronson dealt with mental illness among personnel in charge of the bombs (p. 126).
- RAND researchers assumed LeMay would scorn the report, but the day after it was presented he asked for a copy. Iklé said LeMay later issued a "blizzard" of orders, among others calling for the two-man rule and coded locks (p. 127).
- According to most reports, few coded locks were installed until Kennedy became president. Four days after his inauguration a B-52 disintegrated in midflight; one of its two 24-megaton bombs hit a swamp near Goldsboro, and analysis showed only one of the bomb's six safety devices had functioned properly (p. 127).
- McGrayne closes by saying the world can be thankful that Madansky's Bayesian statistics forced the military to tighten safety measures. Several false alerts were identified correctly before SAC could launch a counterattack (pp. 127–128).

## Toy example (ours, not from the text)
Two hypotheses about the per-operation accident probability $p$: A: $p=0$. B: $p=1/10{,}000$. Assume prior $P(B)=0.01$ and $P(A)=0.99$. This is not Madansky's model.

- Observe 10,000 accident-free operations. Likelihood under A is 1. Under B it is $(1-10^{-4})^{10000}\approx e^{-1.00005}\approx 0.368$.
- Posterior of B: $\dfrac{0.01\times0.368}{0.01\times0.368+0.99\times1}=\dfrac{0.00368}{0.99368}\approx0.0037$.
- Chance of at least one accident in the next 10,000 operations: $0.0037\times(1-0.368)=0.0037\times0.632\approx0.0023$.
- Chance in the next 100,000 operations: $1-(1-10^{-4})^{100000}\approx1-e^{-10}\approx0.99995$, so the risk is $0.0037\times0.99995\approx0.0037$.
- With prior $P(B)=0$ the posterior stays 0 whatever the data. With any $P(B)>0$ the posterior stays above zero, and the more future operations, the larger the risk.

## Concepts
- [[prior-distribution]] — Madansky's prior on per-opportunity accident probability, deliberately not all concentrated at zero (p. 124)
- [[cromwells-rule]] (new) — Lindley liked to quote Cromwell's plea to allow that one may be mistaken, in connection with zero priors (p. 123)
- [[frequentist-vs-bayesian]] — on McGrayne's account, Fisher's relative-frequency view gave zero risk after zero accidents; Bayes allowed doubt (pp. 121, 123)
- [[minimally-informative-prior]] (new) — a weak prior chosen to avoid contestable assumptions (p. 124)
- [[accident-opportunities]] (new) — Madansky's count of occasions when an accident could happen, like coin flips (p. 125)
- [[conjugate-prior]] — priors and posteriors sharing the same curves, which Madansky hoped would allow pencil-and-paper calculation (p. 125)

## Canonical instances
- [[rand-h-bomb-accident-study]] — Bayesian estimate of risk for an event never yet observed (pp. 124–126)
- [[mars-bluff-1958]] — a bomb described as relatively harmless falls on a garden and its conventional explosives detonate (pp. 122–123)
- [[goldsboro-1961]] — B-52 crash where only one of six safety devices worked (p. 127)

## Bridges (candidates)
- [structural-analogy] Cromwell's Rule (no zero priors) ↔ smoothing of zero counts: avoiding a probability of exactly zero for unseen events.
- [structural-analogy] Counting accident opportunities ↔ per-trial risk compounding over many independent trials: a small rate times many exposures.
- [metaphor] Madansky's "alternate theology" ↔ choosing a modeling framework by what it permits you to doubt.

## Questions this raises
- How exactly did the prior and the flight data turn the accident-free record into 19 accidents per year?
- How sensitive is such a result to the choice of a "minimal" prior when there are no accidents in the data?
- Would the safety changes have happened without a quantitative argument, given LeMay's response?
- What does "conspicuous" accident mean here, and how does it differ from a nuclear explosion?

## Reading notes
- Printed page = pdf − 15 (pdf 134 = p. 119).
- The text layer was clean. The unit has no equations and no exercises.
- The pages do not give Madansky's prior, its parameters or the calculation behind "19 accidents". Nothing here can be checked mathematically.
- "In view of what would happen a few years later in Spain" (p. 126) refers to an event not explained in this unit.
- Descriptions of what frequentists or Fisher "could do" (pp. 121, 123) are McGrayne's characterizations. Some Madansky quotes are explicitly later recollections ("said later", p. 123); others come from his own writing ("Madansky wrote", p. 125).
