---
id: mcgrayne-2011-theory/ch17-rosetta
work: mcgrayne-2011-theory
unit: "17. Rosetta Stones"
pages: 233–251
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Rosetta Stones

## L0 — One line
By the 2000s Bayes' rule had become a working tool across science, business, the web, translation and theories of the brain, with the chapter pointing to users who cared about results, cheap computing and vast data archives.

## L1 — The gist (≤ 120 words)
This closing chapter asks where Bayes' rule stands after two and a half centuries. McGrayne's answer is that the old Bayesian–frequentist war has cooled, and Bayesian methods now run through many fields. Examples include finance, astronomy, genetics, robot cars, the military, spam filters, Netflix, Google, machine translation, teaching software and theories of the brain. Some areas still resist, notably courts and the census. Some applications, such as the Netflix winner, use only a Bayesian "perspective" rather than a formal Bayesian model. The chapter matters because it shows the same idea, combining prior knowledge with new evidence, working in very different settings. It ends with open questions about whether data or priors will matter more.

**Prerequisites:** Bayes' rule as "prior knowledge updated by evidence"; the idea of probability as degree of belief; no mathematics beyond that.

## L2 — Key ideas (5–10 bullets)
- The Bayesian–frequentist battle has cooled. Researchers are said to adopt whichever approach fits their needs, and most modern Bayesians accept that frequentism (the school of Fisher, Neyman and Egon Pearson) is still effective for most statistical problems, such as simple standard analyses (pp. 233–234).
- The American census is still anti-Bayesian and Anglo-American courtrooms are largely closed to Bayes. British and continental European forensic labs use Bayes, tactfully called the "likelihood ratio" approach (a way of measuring the value of evidence), with success especially in DNA profiling (p. 235).
- In finance and economics, Bayes ranges from Nobel-level theory to the RenTech hedge fund. Whether Greenspan used it as statistics or only as a metaphor is disputed (pp. 236–238).
- Science problems with faint signals in noise (supernova neutrinos, genes, images) are tackled with Bayes, as are robot vision, military tracking and weapons testing (pp. 238–242).
- On the web, Bayesian ideas appear in spam filters, Microsoft products, the Netflix prize and Google. Some uses are loose: the Netflix winner had only a Bayesian "perspective" and drew on the idea of averaging complementary models, and Google often tries naïve Bayes (which assumes all variables are independent) first (pp. 242–245).
- IBM's speech-recognition team treated speech as a signal sent through a noisy channel and sought the most probable intended sentence (noisy-channel decoding), and it applied the same methods to translation. Google's 2005 results showed progress coming from more training data, not better algorithms (pp. 245–247).
- Bayes appears in education software and as a proposed model of how the brain combines prior beliefs with unreliable senses (pp. 247–250).
- The future debate is whether huge data alone will suffice or whether priors and structure stay fundamental (pp. 250–251).

## L3 — Walkthrough

The chapter has no numbered sections. I follow its topical order.

### Opening: a truce and a broader field (pp. 233–235)
- Today's Bayesians have large Internet archives, off-the-shelf software, MCMC and almost free computing (p. 233).
- The author says Bayesianism as an all-encompassing framework has been replaced by "utilitarian applications and computation". Computer scientists who joined cared about results, not philosophy (p. 233).
- Even theorists who once insisted on strict adherence to fundamental principles now accept Tukey's 1950s view that an approximate answer to the right question beats an exact answer to the wrong one (p. 233).
- Bayes' rule and Fisher's likelihood approach ended their "cold war" and supported a revolution in modeling (p. 233).
- "Bayes" still means probability as a measure of belief (de Finetti, Ramsey, Savage, Lindley). Most modern Bayesians accept that frequentism is still effective for simple, standard analyses, for checking how well a hypothesis fits data, and as the foundation of many modern technologies such as machine learning (pp. 233–234).
- Efron, who remained a committed frequentist while helping develop empirical Bayes, told the author that Bayesians are more tolerant and frequentists see the need for Bayesian reasoning, so the two may be heading for some kind of convergence (p. 234).
- **Kass's view:** Bayes and Laplace did not see that accumulating data makes open-minded observers agree and converge on the truth. Bayes was ultimately accepted not for superior logic but because probability models mimic real-world variation well (p. 234).
- Bayes now overlaps computer science, machine learning and AI. It can combine imperfect evidence and find hidden patterns (p. 234).
- "Bayes" has become a buzzword: Schneider, Unwin's "faith-belief factor", a Ludlum thriller (p. 235).

> **Intuition note.** The chapter's first claim is a change in attitude. Researchers are described as adopting whichever approach fits their needs. The battle is said to have cooled; the chapter does not say it has ended.

### Resistance: census, courts, forensics (p. 235)
- Partisan politics keep the American census anti-Bayesian (p. 235).
- Anglo-American courts are largely closed to Bayes. A 1994 New Jersey case used it to show troopers singled out African American drivers. British judges in a 1990s rape trial said the method "plunges the jury into inappropriate and unneces­sary realms of theory and complexity" (p. 235).
- British forensic services employ Bayesian methods extensively, and continental European labs developed a quantitative measure for the value of evidence. Forensic circles tactfully call the approach the "logical" or "likelihood ratio" approach. It has worked where numbers exist, especially DNA profiling. Tiny DNA match probabilities may eventually open more courtroom doors (p. 235).

### Jefferson and Hemings (pp. 235–236)
- Fraser Neiman checked whether Hemings's conceptions fell during or near Jefferson's visits to Monticello. He combined prior historical testimony, DNA evidence and hypotheses based on Jefferson's calendar (p. 236).
- Assuming a 50–50 probability that the prior evidence was true, he concluded it was 99% probable that Jefferson fathered all six children (p. 236).

### Economics and finance (pp. 236–238)
- Bayes figured in three Nobel prizes for theoretical economics (1990, 1994, 2004). De Finetti anticipated Markowitz's work. Harsanyi and Nash shared the 1994 prize. Harsanyi showed that Nash's equilibrium for games with incomplete or imperfect information was a form of Bayes' rule (p. 236).
- In 2002 Tversky and Kahneman showed that people do not decide according to rational Bayesian procedures. Answers depend on phrasing, as in mortality versus survival framing of cancer treatments (p. 236).
- Tversky, regarded as a philosophical Bayesian, reported frequentist results. Tversky told Berger it was simply expedience; the text adds that Bayesian research was harder to publish in the 1970s, and Berger remarked that he took the easy way out (p. 236).
- Greenspan told the American Economic Association in 2004 that the risk-management approach to monetary policy is an application of Bayesian decision-making (p. 236). Feldstein explained that Bayes lets the Fed weigh a low-probability risk of disaster more heavily than a higher-probability risk that would cause little damage. His umbrella analogy: a good Bayesian carries an umbrella on many dry days (p. 237).
- After the 2008 crash Greenspan blamed his data, which covered only two decades of "euphoria", not the theory. **Blinder's view:** Greenspan used Bayesian ideas only as a metaphor. Greenspan, in the audience when Blinder said so in a talk, did not object (p. 237).
- RenTech hired Brown and Mercer from IBM in 1993. For several years its Medallion Fund, limited to employees, averaged about 35% annual returns. It starts from prior price knowledge and keeps updating, searching for nonrandom patterns in noisy data (p. 237). Mercer calls it close to a needle-in-a-haystack problem (p. 238).

### Faint signals in science (pp. 238–240)
- When Supernova 1987A exploded, astronomers detected precisely 18 neutrinos. Because the event was one of a kind, frequency-based methods did not apply, and Loredo found that Bayes let him compare hypotheses and choose the most probable one. His 1990 thesis introduced modern Bayesian methods to astronomy (p. 238).
- Susan Holmes works on rare amino acids. Frequentist counts would give zero, so she assigns missing species a small possibility, as Turing and Good did (p. 239).
- Because prior information is needed to assemble gene networks from noisy microarray data, many microarrays are analyzed with Bayesian methods (p. 239).
- Koller studies what regulates genes. **Purists (Jordan, Dawid):** "Bayesian networks" is a misnomer when a network has no priors, since Bayes without priors is not Bayes. **Koller's reply:** her networks qualify because she carefully builds priors (pp. 239–240).

### Images, robots, military (pp. 240–242)
- People can instantly recognize a blurry, noisy car or sheep, whereas a state-of-the-art computer trained to recognize cars and sheep may picture only nonsensical rectangles. The author says the difference is that the human brain has prior knowledge to integrate with new images. Koller says the problem is software, not hardware (p. 240).
- Thrun's car Stanley won the 2005 DARPA race (132 miles in seven hours). It estimated, for example, 90% probability of a nearby wall and 10% of an adjacent ditch, and slowed to avoid unlikely catastrophes (p. 240).
- Thrun credited Kalman filters. A Carnegie Mellon–GM team won the 2006 city-traffic contest (pp. 240–241).
- Military uses: Automatic Target Recognition, missile tracking, weapons testing and terrorism threats (p. 241).
  - Some ATR programs start with 50–50 odds, which can strongly affect rare events (p. 241).
  - **Anonymous ATR analyst:** Bayes is "wrong … except for the fact that it works" (p. 241).
  - Missile tracking let sensors pass on only their latest data once a missile was sufficiently probable (p. 241).
  - Many military systems cannot be tested in the large samples frequentist methods require, so a Bayesian approach combines test data with information from similar systems, components and earlier tests (p. 241).
  - Digital Sandbox used Bayesian networks, even before 9/11, to identify the Pentagon as a possible target, combining expert and subjective opinions about events that had never occurred (p. 241).
- When Britain considered a national data bank to detect potential terrorists, Bayes raised the same alarm it had against mass HIV screening. Terrorists are so rare that the definition must be extremely accurate, or many innocent people will be flagged (pp. 241–242).

> **Intuition note.** Many examples share one pattern: little data, a rare event, or a unique event. In several of them, prior or related information is combined with the little data available. The terrorism case shows why rarity matters: the definition of a terrorist must be extremely accurate.

### Microsoft, spam, Clippy (pp. 242–243)
- Heckerman: being a Bayesian means that all probability represents uncertainty and any uncertainty is represented with probability, and he says that is "a lot bigger than Bayes' theorem" (p. 242).
- At Stanford he built nets with expert-based priors. At Microsoft there was lots of data and few experts, so he combined the two (p. 242).
- Bayesian antispam methods score a message from its words and phrases. Scores near 0.9999 arise for phrases like "our price" and for !!! or $$$. Users refine filters by sorting low-scoring messages (p. 242). The author compares this to Mosteller and Wallace's Federalist work (pp. 242–243).
- Heckerman and Horwitz say Clippy was unfairly blamed on Bayes. The original used belief networks with a threshold. Non-Bayesians substituted a cruder algorithm that made it appear too often (p. 243).

### Recommenders and Netflix (pp. 243–244)
- Recommender (collaborative) filters assume that people who agreed on one product will probably agree on another. Machine-learning updating does not necessarily follow Bayes' theorem formally but "shares its perspective" (p. 243).
- The Netflix prize ran from 2006 and was won in September 2009 by the AT&T Labs team (p. 243).
- No contestant questioned Bayes as legitimate, yet almost none wrote a formal Bayesian model. The winner relied on empirical Bayes, estimating the initial priors from frequencies. The data set was too big for anyone to build a model, assign priors, update repeatedly and recommend films almost instantaneously, so the winning algorithm had a Bayesian "perspective" and "flavors" (pp. 243–244).
- The most important lesson of the contest originated as a Bayesian idea: sharing. Volinsky had used Bayesian model averaging in his 1997 thesis, though his team did not use the method directly for Netflix. He says Bayesian model averaging studies show that when two models that are not highly correlated are combined smartly, the combination often does better than either alone (p. 244).

### Search and Google (pp. 244–245)
- Before keyword search can work, each document must be profiled and categorized and its probable interconnectedness with other documents calculated. Hoff calls these inferential problems (p. 244).
- Google often tries naïve Bayes first. Naïve Bayes assumes every variable is independent of the others. Norvig says vast data often made a more complex method unnecessary (p. 244).
- Google's spelling checker learned spelling variants from a full-text search of the Internet, so it could correct "shaorn" to "Sharon" (p. 245).

### Machine translation (pp. 245–247)
- Weaver suggested treating translation as cryptography. The idea lay fallow for lack of computing and text (p. 245).
- In the 1970s IBM had two speech-recognition teams. The linguists studied grammar rules. Mercer and Brown's team used Bayes' rule and was ignored for a decade (p. 245).
- Their framing: a signal passes through a noisy channel, and one seeks the most probable intended sentence. The prior is the likely word order in English, learned from large amounts of text (pp. 245–246).
- Ignoring grammar rules, they set out to estimate the probability that words and phrases in one language would end up as particular words or phrases in another, without needing to know any language (p. 245).
- They computed the probability of a word given the preceding words. After "the", "tree" is more likely than "cantaloupe", and "the" or "a" is highly unlikely (pp. 245–246).
- In the late 1980s they got about 100 million words of Canadian parliamentary debates in English and French. IBM extracted about three million sentence pairs, almost 99% true translations. Alignment used Bayes' theorem and hidden Markov models (p. 246).
- A 1990 paper applied Bayes to full sentences. "President Lincoln was a good lawyer" probably means "Le president Lincoln était un bon avocat", and probably not "Le matin je me brosse les dents" (p. 246).
- After 9/11 and the start of the Iraq war, military and intelligence communities poured money into machine translation. Mercer and Brown left IBM for RenTech in 1993, and critics complain the departures set machine translation back five years (p. 247).
- Google later used web texts, including 200 billion words from United Nations documents, and aligned sentences by the most probable fit (p. 247).
- Its 2005 contest wins showed progress came from more training data, not better algorithms. Computers do not "understand" but recognize patterns (p. 247).

### Learning and education (pp. 247–248)
- Cognitive Tutors, used by about 2,600 secondary schools, build on Anderson's idea that Bayes is a surrogate for natural gradual learning (pp. 247–248).
- Bayes' theorem computes each student's "skillometer", the probability of having mastered a topic. After ten years, students learned as much or more in a third of the time (p. 248).

### The brain (pp. 248–250)
- Emery Brown and Wilson, using Kalman filters, tracked a foraging rat's position from place-neuron firing. They needed only a fifth or a tenth of the neurons earlier methods required (pp. 248–249).
- Similar Bayesian filters applied to motor neurons let a monkey control a robotic arm to fetch a treat (p. 249).
- The author asks whether the brain itself performs Bayesian-like computations. The "Bayesian Brain" is a metaphor for a brain that mimics probability (p. 249).
- Hand location without sight can be off by up to 10 cm. The author says Bayes is a useful framework that helps explain how the brain may learn and demonstrates mathematically how we combine prior beliefs with error-fraught sensory evidence (p. 249). **Lindley:** if senses are certain we rely on them, otherwise we fall back on priors (pp. 249–250).
- **Wolpert's tennis experiment:** players unconsciously combine prior knowledge of bouncing balls with sensory data about one ball. Bayes gives a range of predictions, not one number (p. 250).
- Wolpert concluded that Bayesian thinking is basic to everything a human does, from speaking to acting. The author's summary is that "growing evidence suggests" we have Bayesian brains (p. 250).

> **Intuition note.** The brain story is a hypothesis, not a settled result. The text frames it as growing evidence and a metaphor. The core claim is that noisy senses are blended with prior expectation, with prior beliefs taking over when the senses are unreliable, as Lindley put it.

### The future (pp. 250–251)
- The author says brute computer force clusters and searches documents crudely by keywords, while only the brain examines documents and images by meaning and content. Open questions: will huge data alone teach everything, or will Bayesian organizing principles stay fundamental? (p. 250).
- **Geman:** the jumping-off point of the debate is Bayes and its priors, and the strongest argument for Bayes is its recognition of the brain's inner structures and prior expectations. He says old and new issues are similar, if not identical. The author says the old Bayesian-frequentist issues have been reframed as whether we use probabilities or not (p. 251).
- **Diaconis:** Bayes is still young, grew up in data-poor and computationally poor circumstances and has not settled down yet. He insists it will play a role (p. 251).

## Toy example (ours, not from the text)
A naïve Bayes spam score, with made-up numbers. Prior: 40% of mail is spam, so P(spam) = 0.4, P(ham) = 0.6.

- Word "price": appears in 30% of spam, 3% of ham.
- Message with "price" only:
  - spam numerator: 0.4 × 0.30 = 0.12
  - ham numerator: 0.6 × 0.03 = 0.018
  - posterior P(spam) = 0.12 / (0.12 + 0.018) = 0.12 / 0.138 ≈ 0.870
- Add "!!!": appears in 50% of spam, 5% of ham. Naïve Bayes treats it as independent of "price":
  - spam: 0.12 × 0.50 = 0.06
  - ham: 0.018 × 0.05 = 0.0009
  - P(spam) = 0.06 / 0.0609 ≈ 0.985

Each word updates the previous posterior, which acts as the new prior. Independence is the simplifying assumption the chapter describes (p. 244).

## Concepts
- [[frequentist-vs-bayesian-inference]] — here a cooling rivalry. researchers adopt whichever approach fits their needs; most modern Bayesians accept frequentism as still effective for most statistical problems (pp. 233–234)
- [[subjective-probability]] — probability as a measure of belief, so that it can apply to unique events, as Lindley put it (pp. 233–234)
- [[prior-distribution]] — prior knowledge, such as word order in English, price history or expert opinion (pp. 237, 242, 246)
- [[bayes-theorem]] — combines prior knowledge with new evidence, from spam scoring to translation (pp. 242, 246)
- [[sequential-updating]] — continuous updating, as in RenTech's data stream and Bayesian filters (pp. 237, 249)
- [[base-rate-neglect]] — rare targets such as terrorists require an extremely accurate definition, or many innocent people are flagged (pp. 241–242)
- [[likelihood-ratio-forensics]] (new) — forensic "likelihood ratio" approach to the value of evidence (p. 235)
- [[naive-bayes]] (new) — assumes all variables are independent; a quick first method (p. 244)
- [[bayesian-model-averaging]] (new) — when two models that are not highly correlated are combined smartly, the result often beats either alone, per Volinsky (p. 244)
- [[empirical-bayes]] (new) — initial priors estimated from frequencies, as in the Netflix winner (pp. 243–244)
- [[kalman-filter]] (new) — filtering tool the text credits for Stanley's win and uses with Bayes' rule in robot soccer and rat-brain tracking (the chapter does not define it) (pp. 240–241, 248)
- [[bayesian-network]] (new) — network of variables with priors; purists dispute the name if priors are absent (pp. 239–240)
- [[noisy-channel-decoding]] (new) — find the most probable intended message given a corrupted signal (p. 245)
- [[bayesian-brain]] (new) — hypothesis that the brain blends priors with unreliable sensory data (pp. 249–250)

## Canonical instances
- [[jefferson-hemings-dna]] — Bayes with a 50–50 prior gives 99% for Jefferson's fatherhood of six children (p. 236)
- [[supernova-1987a]] — 18 neutrinos analysed by Bayes for a one-off event (p. 238)
- [[stanley-driverless-car]] — probabilistic obstacle estimates with caution toward rare disasters (p. 240)
- [[renaissance-medallion-fund]] — Bayesian data-driven trading (p. 237)
- [[netflix-prize]] — mostly informal Bayesian ideas; model combination mattered most (pp. 243–244)
- [[ibm-canadian-hansards-translation]] — a "Rosetta Stone" of English–French text for statistical translation (p. 246)
- [[wolpert-virtual-tennis]] — players combine priors with sensory data (p. 250)
- [[cognitive-tutors]] — skillometer based on Bayes (p. 248)
- [[clippy]] — Bayesian belief network replaced by a cruder algorithm (p. 243)

## Bridges (candidates)
- [structural-analogy] Feldstein's umbrella argument ↔ decision theory: act on loss-weighted probability, not on probability alone — the text links this to weighing rare disasters (p. 237)
- [structural-analogy] Spam scoring from words ↔ authorship attribution: both classify from word evidence (pp. 242–243)
- [metaphor] "Bayesian Brain" ↔ cognitive science: the brain as probability calculator (p. 249)
- [structural-analogy] Translation as noisy-channel decoding ↔ information theory: recover a message through a corrupted channel (p. 245)

## Questions this raises
- When does a "Bayesian perspective" (informal, as in Netflix) differ from a formal Bayesian model, and does it matter for results?
- If Google's translation gains came mainly from more data, what role are priors still playing?
- How would one test the claim that the brain acts like a Bayesian, beyond experiments like Wolpert's?
- Why do courts resist Bayes while forensic labs adopt it?

## Reading notes
- Printed pages 233–251 are the chapter. Printed 252 is blank. Printed = pdf − 15.
- The text gives "Fraser" and later "Fraiser" for Neiman (p. 236); I wrote "Fraser". "Horwitz" is spelled the same way on pp. 242 and 243.
- The Nobel list (1990, 1994, 2004) is explained only for 1990 and 1994 (p. 236). The 2002 prize is discussed separately.
- This is a popular narrative. Figures such as 35% returns, 99% and 90%/10% are as reported by the author and are not derived.
- The chapter has endnote numbers 1–6 but the notes are not in these pages.
