---
id: mcgrayne-2011-theory/ch03-many
work: mcgrayne-2011-theory
unit: "3. Many Doubts, Few Defenders"
pages: 34-58
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Many Doubts, Few Defenders

## L0 — One line
After Laplace, theorists attacked Bayes' rule as subjective and frequentists almost wiped it out, yet practitioners (artillery, telephone and insurance men, a geophysicist) kept using it.

## L1 — The gist (≤ 120 words)
How did Bayes' rule fare after Laplace's death? McGrayne tells a story of theory against practice. A craze for "objective" statistics, then Fisher, Neyman and Egon Pearson, pushed the rule out of respectable theory. Away from the theorists, French officers, Bell engineers and workers' compensation actuaries used it because they had to decide with thin data. A few outsiders (Borel, Ramsey, de Finetti, Jeffreys) kept its ideas alive. Practically speaking, Jeffreys lost his public debate with Fisher, and frequentism almost totally eclipsed the rule for the next decade. The chapter also reports how personalities, convenience and differing aims shaped the quarrel.

**Prerequisites:** Bayes' rule as prior + data → updated belief; the difference between "probability of data given hypothesis" and "probability of hypothesis given data"; what a mean is; frequentists (people who judge the probability of an event by how often it occurs among many observations).

## L2 — Key ideas (5–10 bullets)
- Laplace's reputation was attacked with unsubstantiated charges, and a craze for "pure facts" statistics made probability of causes unfashionable (pp. 34–36).
- Critics treated subjective belief and objective frequency as opposites, although Laplace had thought them basically equivalent. They identified Bayes' rule with its equal-prior shortcut (starting from 50–50 odds) and condemned the whole rule because of it (pp. 36–37).
- Practical users kept Bayes: French artillery (Bertrand, Estienne), the Dreyfus trial, and Bell's Molina (pp. 38–42).
- US actuaries built "Credibility" (1918), a simple Bayesian-style premium formula that shrinks a business's data toward its class. It was relied on for the next 30 years, and some 50 years later statisticians and actuaries were surprised to find its Bayesian roots (pp. 43–45).
- Fisher, Neyman and Egon Pearson built frequentist tools (randomization, significance tests, hypothesis tests) and made Bayes nearly taboo. They also fought one another bitterly (pp. 46–51).
- Borel, Ramsey and de Finetti independently proposed measuring subjective belief by betting. Not even probability experts noticed (pp. 51–52).
- Small Bayesian niches survived: paternity law and Reed's X-ray dose study (pp. 52–53).
- Jeffreys defended Bayes with objective priors and attacked p-values (probability statements about data, given a hypothesis). Practically speaking he lost the debate to Fisher, for several reasons, and was left isolated (pp. 53–58).

## L3 — Walkthrough
(The chapter has no numbered sections. Headings below follow its order of topics. Printed page = pdf − 15.)

### Laplace's reputation and the statistics craze (pp. 34–36)
- After Laplace, theorists scorned, reformed, tolerated and nearly destroyed Bayes' rule, yet it kept helping with practical problems (p. 34).
- Charges against Laplace: de Morgan (1839) said he failed to credit others. Stigler later found this groundless. Maximilien Marie (1880s) painted him a reactionary. The 1912 Britannica and E. T. Bell's 1937 book also painted unflattering portraits. Karl Pearson called the Britannica author one of the most superficial writers and his statements deplorable. Modern historians show many disparaging comments were false (pp. 34–35).
- Laplace also launched a craze for statistics by publicizing (1827) that Paris dead letters stayed roughly constant yearly. Thefts, murders and suicides looked constant too. By 1830 stable ratios were separated from divine providence, and "objective numbers" became fashionable (p. 35).
- Statistics needed no mathematics. Gone was using probability to quantify lack of knowledge, and gone was the search for causes. A correspondent told Florence Nightingale that "the statistician has nothing to do with causation" (p. 35).
- "Subjective" became a naughty word. After the French Revolution, people no longer assumed all rational people share the same beliefs (pp. 35–36).

### Frequentists against Laplace (pp. 36–38)
- Revisionists such as John Stuart Mill denounced probability. They preferred to judge an event's probability by how frequently it occurred among many observations. These people became *frequentists* (or sampling theorists) (p. 36).
- Critics aimed at Laplace; Bayes barely registered. They treated frequency and degree of belief as opposites, although Laplace had considered them basically equivalent (p. 36).
- Targets: the sunrise question and the question whether one cause lay behind the solar system. McGrayne says Laplace did not actually use Bayes' rule for either, only simple gambling odds. He and followers sometimes began with 50–50 odds. This was hard to defend, since he knew these were results of celestial mechanics. He also started male/female birthrates at 50–50, though the male-birth likelihood was known to be about 0.52 (p. 36). Laplace agreed that reducing scientific questions to chance boosted the odds for his conviction that physical phenomena have natural causes, and he warned his readers; his followers sometimes weighted their initial odds heavily toward natural laws (pp. 36–37).
- Critics identified Bayes' rule with equal priors and damned the whole rule for them. Few tried to imagine other priors (p. 37).
- Keynes listed objections to the sunrise bet (Laplace: odds of 1,825,214 to 1). Boole called the hypotheses arbitrary, Venn said it conflicted with experience, Bertrand called it ridiculous. Others (de Morgan, Jevons, Pearson) accepted it (p. 37).
- Laplace's balance between subjective belief and objective frequency collapsed. No decisive experiment was available, and since Laplace had shown that both approaches often give roughly the same result, the small world of probability experts found the dispute hard to settle. Probability research petered out, and by 1850 Laplace's treatise was unavailable in Paris bookshops. Chrystal (1891) wrote an "obituary" for inverse probability (p. 37).
- Bayes' rule was "left for dead" a third time. The funeral was premature: it was still taught and used by astronomers, since frequentists had no systematic, practical substitute (p. 38).

*Intuition note:* Critics identified Bayes' rule with its equal-prior shortcut and condemned the whole rule because of that shortcut (p. 37).

### Bertrand, Dreyfus and the French army (pp. 38–40)
- Bertrand reformed Bayes for artillery officers, who faced uncertainties about enemy position, wind, cannon variation and so on. He taught that Laplace's probability of causes was the only valid way to verify a hypothesis with new observations. He told officers to stop using 50–50 odds indiscriminately (his example: Breton peasants who gave tides and dangerous northwest winds equal odds as causes of shipwrecks). Equal odds were for hypotheses truly equally likely, or when nothing was known (p. 38).
- Officers assigned equal probabilities only for cannons made in the same factory under identical conditions. French and Russian artillery used Bertrand's textbook for about 60 years, until the Second World War (p. 38).
- Dreyfus affair: almost the only evidence was a letter. The criminologist Bertillon testified that probability showed Dreyfus wrote it. At the 1899 trial Poincaré, who believed in frequency-based statistics, nevertheless invoked Bayes' rule. He thought it the only sensible way for a court to update a prior hypothesis with new evidence. His sarcastic letter said Bertillon's "colossal error" made all that followed suspect (pp. 38–39).
- The judges had studied Bayes in Bertrand's textbook. They gave a compromise verdict (guilty, five-year sentence). A pardon followed two weeks later. Many American lawyers, unaware that probability helped free Dreyfus, have seen the trial as mathematics run amok (p. 39).
- General Estienne made Bayesian firing tables. After 1914, when ammunition was scarce, mathematicians made Bayesian testing tables that destroyed only 20 cartridges per lot of 20,000. The army could stop testing once sure about the lot instead of using a predetermined number of tests. McGrayne says American and British mathematicians later found similar methods and called them operations research (pp. 39–40).

### Molina and the Bell System (pp. 40–42)
- Around the 1907 panic, state regulators demanded proof of Bell's service; its circuits were often overloaded at peaks and underused about 80% of the time. No company could afford to build for every possible peak call (p. 40).
- Molina, a self-taught engineer, said great confusion existed because many authorities failed to distinguish Bayes' original theorem from Laplace's generalization. The general one combines observation data with "collateral" information (indirect prior knowledge) (p. 41).
- He used Laplace's formula to combine prior information on the economics of automation with data on traffic, call length and waiting. He conceived the relay translator and analyzed switch/trunk combinations with Bayes. Bell chose a method that halved the operators. Operator employment fell from 15 to 7 per 1,000 telephones between the wars (p. 41).
- His Bayes use stayed controversial among some Bell mathematicians. AT&T often treated his articles as proprietary and published them years late; his enthusiasm did not spread to other American corporations (pp. 41–42).

### Workers' compensation and Credibility (pp. 42–45)
- In 1911–1920 no-fault laws in all but eight states began requiring employers to insure workers against occupational injury and illness. The accumulated data needed to price premiums did not exist in the US; even the most industrialized states could price only a few industries. Data from other places were seldom relevant (the example: Massachusetts shoe data versus Nevada metal mines) (pp. 42–43).
- Rubinow tabulated millions of claims by hand as a stopgap (he said all available information must be used). He helped found the Casualty Actuarial Society in 1914 (p. 43).
- In spring 1918 Whitney's committee stripped away complications. They assumed every business in an industrial class faced equal risk and every actuary was equally skilled at adding subjective judgments. This was Bayes' rule with industry-wide experience as the prior and the local business's history as new data (p. 44).
- Premiums were based almost exclusively on the broad class's experience, or on a large firm's own. Combining related businesses pulled numbers toward the mean, a "shrinking" effect that Stein would explain in the 1950s (p. 44).
- The committee named the result *Credibility*. An actuary later wrote that Z = P/(P+K) was not as great a discovery as E = mc² but had made life easier for insurance men (P and K are not defined in these pages). The system was relied on for the next 30 years; some 50 years later statisticians and actuaries were surprised to find its Bayesian roots (p. 44).
- Whitney worked out ways to weight each datum by its subjective believability. An actuary later reported that actuaries had gone beyond anything proven mathematically; their only demonstration was that it works in practice. An insurance commissioner asked where the experience supporting the Credibility factor was, and actuaries hastily changed the subject (pp. 44–45).
- From 1922 a large national data pool let actuaries check premiums against claims (p. 45).

*Intuition note:* Credibility mostly relies on what the whole industrial class shows; a firm big enough may rely on its own record. Pooling related businesses pulls the numbers toward the mean (p. 44).

### Karl Pearson, Fisher and the frequentist rise (pp. 45–51)
- Karl Pearson was uneasy about uniform priors and subjectivity but said practical men would accept Bayes-Laplace results until something better appeared. Keynes: "a smack of astrology, of alchemy"; Coolidge: "We use Bayes' formula with a sigh" (pp. 45–46).
- Fisher is portrayed as the near-lethal opponent. He feuded with Pearson but was a fellow eugenicist. At Rothamsted from 1919 he first used Bayes, then pioneered randomization, sampling theory, significance tests, maximum likelihood, analysis of variance and experimental design. His 1925 manual made frequency the de facto statistical method (pp. 46–47).
- McGrayne says Fisher's own work (small, repeatable experiments, few gaps in data) did not need hunches. He redefined uncertainty by relative frequencies, not relative probabilities (p. 48).
- Fisher called Bayes' rule "an impenetrable jungle", a "mistake", and said equal priors were "staggering falsity". McGrayne says his work had many Bayesian elements, yet he made Bayes virtually taboo. Frequentists enjoyed a golden age in the 1920s–30s (p. 48).
- Egon Pearson used Bayes in 1925, in the most extensive exploration between Laplace and the 1960s (taxicabs, pipe smokers, hounds), looking for "nature's prior" for binomial problems. No one followed up (p. 49).
- In 1933 Egon Pearson and Neyman developed hypothesis testing. Pearson's idea: the only correct reason to reject a hypothesis is to accept a more probable one (p. 49).
- Fisher and Neyman became anti-Bayesians who limited themselves to events repeatable many times and viewed each data set as a separate problem. They banned subjective priors, but did not dispute Bayes' theorem when priors were known. Difficulty arose when they were unknown (pp. 49–50).
- Philosophical divide: frequentists ask for the probability of data given known causes. Bayesians ask what the data tell about causes. Bayesians can also treat single events, and use subjective information and every datum (p. 50).
- Fisher and Neyman then feuded for 30 years (1934 Royal Society clash over the Latin square; separate tea rooms). George Box said both men could be very nasty and very generous. McGrayne adds that Neyman was decision-oriented and Fisher more interested in scientific inference, so each did what suited his own problems and neither tried to understand the other. Neyman moved to Berkeley, which became anti-Bayesian. Two warring frequentist camps were united in their abhorrence of Bayes (pp. 50–51).

### Betting and the quiet niches (pp. 51–53)
- Borel (1924), Ramsey (1926) and de Finetti independently proposed that subjective belief could be quantified by betting. Ramsey added a utility function and maximizing expected utility, showing how to act under uncertainty; neither Bayes nor Laplace had treated decisions. They worked outside English-speaking statistical circles and were not noticed (pp. 51–52).
- Erik Essen-Möller's 1938 paternity index was mathematically equivalent to Bayes' theorem. US lawyers used it for 50 years, until DNA profiling. Lawyers started from 50–50 odds, which favored fathers (p. 53).
- Lowell Reed (1936) used Bayes to find X-ray doses for human tumors, sacrificing 27 cats. He had little influence on statistics (p. 53).

### Jeffreys against Fisher (pp. 53–58)
- Jeffreys, a geophysicist, nearly alone kept Bayes alive during the anti-Bayesian onslaught of the 1930s and 1940s, according to McGrayne. He and Fisher were friends. With large samples the prior did not matter and maximum likelihood gave about the same result as Bayes. They differed for small data (p. 53).
- Earthquake work (inferring that Earth's core is liquid, 1926) was inverse probability of causes from indirect, unrepeatable data. He said science moves from ignorance through partial knowledge to practical certainty (p. 54).
- He devised formal rules for choosing priors, an objective form of Bayes. He thought probability fit all uncertainty, even a scientific law, whereas frequentists usually restricted it to theoretically repeatable data (p. 55).
- p-value: a probability statement about data, given the hypothesis. Technically, p-values let laboratory workers call an outcome statistically significant evidence against a hypothesis if the outcome (or a more extreme one) had only a small probability, under the hypothesis, of occurring by chance alone (p. 55).
- Jeffreys's objections: he found it very strange that a frequentist considers possible outcomes that did not occur (a critic called the many repeated experiments "imaginary repetitions"); the p-value is about data, whereas he wanted the probability of his hypothesis given his data, so he proposed using only observed data with Bayes' rule. He argued that at no date in the history of the law of gravitation would a modern significance test have failed to reject all laws and left us with a law. He complained that frequentists seem to use observations only as grounds for possibly rejecting hypotheses, never for supporting them (pp. 55–56). McGrayne adds that odds are at least some hypotheses Fisher rejected were worth investigating or even true (p. 56).
- Bayesians say that even with a .01 p-value the odds in favor of a precisely tested hypothesis are still 1 to 9 or 10; Berger (Bayesian) calls this "not earth-shaking". **Goodman (1999):** "The p-value is almost nothing sensible you can think of." (p. 56).
- Jeffreys compared Bayes' rule to the Pythagorean theorem of probability theory, whereas Fisher used the word "Bayes" as an insult. McGrayne calls Jeffreys the founder of modern Bayesian statistics (p. 56).
- The two-year Royal Society debate ended inconclusively. Fisher said Jeffreys's book had a mistake on page one invalidating all 395 formulae. McGrayne comments that the supposed mistake was, of course, using Bayes' theorem (p. 57).
- Why Jeffreys lost, per McGrayne: Fisher was persuasive; social scientists needed objective methods; physicists using quantum mechanics used frequencies; Fisher's methods were easier to use (Jeffreys's five categories of evidence were in an appendix); Jeffreys cared about inference, not decisions (p. 57).
- Jeffreys was left almost totally isolated from statistical theorists. *Theory of Probability* was published in a physics series in the last year of peace (p. 58).

## Toy example (ours, not from the text)
Bertrand's Breton peasants, with invented numbers. Causes of a wreck: tides (T) or northwest wind (W). Evidence: a wreck occurred on a stormy night. Assume P(storm night | T) = 0.1 and P(storm night | W) = 0.6.
- Equal priors 0.5/0.5: T gets 0.5 × 0.1 = 0.05; W gets 0.5 × 0.6 = 0.30. Total 0.35, so P(T | data) = 0.05/0.35 ≈ 0.14.
- Informed prior 0.1/0.9 (winds more dangerous): T gets 0.1 × 0.1 = 0.01; W gets 0.9 × 0.6 = 0.54. Total 0.55, so P(T | data) = 0.01/0.55 ≈ 0.018.
The same data give different answers, so the prior must be chosen with care. That was Bertrand's point against indiscriminate 50–50 odds.

## Concepts
- [[bayes-theorem]] — rule combining prior information with new data; here used as practical tool by artillery, Bell, insurers (p. 38)
- [[prior-distribution]] — starting probabilities; critics fixed on the equal-prior shortcut (p. 37)
- [[principle-of-indifference]] — equal odds for causes; Bertrand allows it only for truly equal or unknown cases (p. 38)
- [[frequentist-vs-bayesian]] — frequency of events vs degree of belief; here treated as opposites, though Laplace saw them as equivalent (p. 36)
- [[subjective-probability]] — belief quantified by a wager (Borel, Ramsey, de Finetti) (p. 51)
- [[partial-pooling-shrinkage]] — Credibility's pull toward the class mean, later explained by Stein (p. 44)
- [[inverse-probability]] (new) — the chapter's term for reasoning back from data to causes; Chrystal's 1891 obituary names it (p. 37) and Jeffreys's earthquake problem is called a classic case (p. 54)
- [[collateral-information]] (new) — Molina's term: indirect prior knowledge beyond the observed data (p. 41)
- [[credibility-theory]] (new) — 1918 simplified Bayesian premium-setting method, Z = P/(P+K) (p. 44)
- [[p-value]] (new) — probability, under the hypothesis, of an outcome as extreme as observed (p. 55)
- [[neyman-pearson-testing]] (new) — hypothesis testing weighing a rival hypothesis; reject only to accept a more probable one (p. 49)
- [[expected-utility]] (new) — Ramsey's tool for acting under uncertainty (p. 52)

## Canonical instances
- [[dreyfus-affair]] — Poincaré invoked Bayes at the 1899 trial (p. 39)
- [[french-artillery-bertrand]] — textbook priors and cartridge-lot testing (pp. 38–40)
- [[bell-system-molina]] — Bayes for telephone traffic and automation (pp. 41–42)
- [[workers-compensation-credibility]] — Whitney's 1918 committee (p. 44)
- [[earth-core-jeffreys]] — liquid core inferred from seismic data (p. 54)
- [[essen-moller-paternity]] — Bayes-equivalent paternity index (p. 53)
- [[reed-xray-doses]] — tumor doses found with 27 cats (p. 53)
- [[sun-rising-laplace]] — sunrise bet, criticized and defended (p. 37)

## Bridges (candidates)
- [structural-analogy] Credibility's blend of class data and own data ↔ hierarchical modelling: partial pooling of group estimates — both pull noisy local estimates toward a wider mean
- [structural-analogy] Estienne's stop-when-sure ammunition testing ↔ sequential analysis in statistics — the sample size is not fixed beforehand
- [structural-analogy] Jeffreys on "imaginary repetitions" ↔ the likelihood principle (canon link; not stated in this unit) — inference from observed data only
- [metaphor] Fisher–Neyman tea-room split ↔ sociology of science: schools separated by aims, not only by logic

## Questions this raises
- How can a prior be chosen "objectively", as Jeffreys tried, if equal priors were so heavily criticized?
- Is the p-value versus posterior-odds gap Berger describes general or specific to precise hypotheses?
- What exactly are P and K in Credibility's Z = P/(P+K), and how does that formula match Stein's shrinkage?
- How much did decision-making needs (Neyman, Ramsey) rather than logic decide which school won?

## Reading notes
- Printed = pdf − 15 (pdf 49 = p. 34).
- The only formula is Z = P/(P+K), quoted from an actuary who compares it with E = mc² (p. 44). P and K are not defined in these pages.
- Statements about what Laplace did and did not do, and about Fisher's work (for example, that it had many Bayesian elements), are McGrayne's own statements, not mine.
- The chapter has no numbered subsections; the headings in L3 are mine.
