---
id: kahneman-2011-thinking/ch16-causes
work: kahneman-2011-thinking
unit: 16 Causes Trump Statistics
pages: pdf 163–171 (printed page numbers not visible)
fields: [decision-game-theory]
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
# Causes Trump Statistics

## L0 — One line
People readily use base rates that fit a causal story about the individual case, and tend to underweight or neglect purely statistical facts about a group; but even compelling causal statistics do not change long-held beliefs.

## L1 — The gist (≤ 120 words)
Why do people ignore base rates (how common something is in a population) in Bayesian problems? Kahneman reports that the same numbers count for more when framed causally than as plain statistics, which are often underweighted (the cab problem, Ajzen's exam study). In the cab case the causal base rate works like a stereotype. That improves accuracy there, but in hiring or profiling a strong social norm opposes stereotyping. The Nisbett–Borgida helping-experiment study shows that students given surprising statistics learned nothing, while surprising individual cases led them to generalize. The practical lesson: System 1 (fast, automatic thinking) handles causal stories but is weak at statistics. To teach, surprising individual cases work better than surprising statistics.

**Prerequisites:** percentages; the idea of conditional probability (updating a probability after new evidence); the idea of a "base rate".

## L2 — Key ideas
- Two mathematically equivalent versions of the cab problem get different treatment. In the statistical version (85% of cabs are Green) readers often ignore the base rate; in the causal version (Green cabs are involved in 85% of accidents) they give it considerable weight (pdf 163–164).
- Statistical base rates are generally underweighted, and sometimes neglected, when case-specific information exists. Causal base rates are treated as information about the individual case (pdf 164).
- Stereotypes are statements about a group that are accepted, at least tentatively, as facts about every member. Kahneman uses the word neutrally: System 1 represents categories by prototypes (pdf 165).
- Using a valid stereotype can improve judgment. Kahneman holds that the strong social norm, also embedded in law, against stereotyping in hiring or profiling is as it should be. Kahneman says the cost of that norm is real, though worth paying (pdf 165–166).
- Ajzen's exam study: a causal base rate (class pass rate) moved judgments much more than a statistically equivalent selected-sample base rate (pdf 166–167).
- Nisbett–Borgida: students told the results of the helping experiment predicted individuals' behavior no differently from students not told. People resist base-rate conclusions that conflict with their beliefs about themselves and human nature (pdf 167–170).
- Told only that two nice people had not helped, students guessed the overall results very accurately. Surprising cases teach; surprising statistics do not (pdf 170).

## L3 — Walkthrough

### Causal Stereotypes: the cab problem (pdf 163–165)
- **Version 1.** 85% of the city's cabs are Green and 15% are Blue. A witness says the hit-and-run cab was Blue. The witness is right 80% and wrong 20% of the time. What is the probability that the cab was Blue? (pdf 163)
- This is standard Bayesian inference: it combines a base rate with imperfect testimony. Without the witness, the probability of Blue is the base rate, 15%. With equal-sized companies, the base rate would be uninformative (pdf 163).
- **Version 2.** The companies run the same number of cabs, but Green cabs are involved in 85% of accidents. The witness information is unchanged (pdf 163–164).
- The versions are mathematically indistinguishable but psychologically different. Version 1 readers often ignore the base rate. Version 2 readers give it considerable weight, and their average answer is not too far from the Bayesian one (pdf 164).
- **Why.** In version 1 the number of cabs is a statistical fact. A mind "hungry for causal stories" finds nothing to chew on (pdf 164). In version 2 the Green drivers are seen as reckless, which is a stereotype that fits a causal story (pdf 164).
- The two causal stories (a reckless Green driver; a witness who says Blue) point in opposite directions and approximately cancel. The Bayesian answer is 41%, because the Green base rate is slightly more extreme than the witness's reliability (pdf 164).
- (added step) Calculation: $P(\text{Blue}\mid\text{says Blue})=\dfrac{0.15\cdot 0.80}{0.15\cdot 0.80+0.85\cdot 0.20}=\dfrac{0.12}{0.29}\approx 0.41$.
- **Two types of base rate** (pdf 164):
  - *Statistical* base rates are facts about a population to which the case belongs, not relevant to the individual case.
  - *Causal* base rates change your view of how the case came to be.
- Statistical base rates are generally underweighted, and sometimes neglected altogether, when case-specific information is available. Causal base rates are treated as information about the individual case and combined easily with other case-specific information (pdf 164).

*Intuition note:* The mind asks "what caused this?" A number with a cause attached becomes a fact about the driver, so people use it. A bare count has no cause attached, so it tends to be underweighted or dropped.

### Stereotypes and their social cost (pdf 165–166)
- Stereotypes are statements about a group accepted, at least tentatively, as facts about every member. Examples: "Most graduates of this inner-city school go to college"; "Interest in cycling is widespread in France" (pdf 165).
- Kahneman uses "stereotype" neutrally. System 1 represents categories as norms and prototypical exemplars, which are called stereotypes when the categories are social. Some stereotypes are perniciously wrong, but "stereotypes, both correct and false, are how we think of categories" (pdf 165).
- The irony: in the cab problem, neglecting base rates is a flaw, and stereotyping Green drivers improves accuracy (pdf 165).
- In hiring or profiling there is a strong social norm, embedded in law, against stereotyping. Kahneman says this is as it should be: we want base rates treated as group facts, not as presumed facts about individuals (pdf 165).
- The norm has been highly beneficial. Still, neglecting valid stereotypes inevitably results in suboptimal judgments. Saying resistance is costless is "not scientifically defensible", though the costs are worth paying (pdf 166).
- Kahneman links the claim "our positions have no cost" to the affect heuristic in politically charged arguments (pdf 166).

### Causal Situations: Ajzen's study (pdf 166–167)
- Kahneman and his colleague Amos built the cab variants but borrowed causal base rates from Icek Ajzen (pdf 166).
- Participants judged whether students shown in vignettes had passed a Yale exam. *Causal condition:* the students came from a class in which 75% passed, or one in which 25% passed. A 25% pass rate suggests a brutally difficult test, a causal factor for every student (pdf 166).
- Result: every student was judged more likely to pass in the high-success condition than in the high-failure condition (pdf 166).
- *Noncausal condition:* the students came from a sample built by selecting students who had passed or failed, for example "75% had failed" because the investigator was interested in the causes of failure. This is a purely statistical fact about the ensemble and has no bearing on whether an individual passed (pdf 166).
- Result: the explicit base rates had some effect, but much less than the statistically equivalent causal ones. System 1 handles causally linked stories but is weak at statistical reasoning. For a Bayesian the versions are equivalent (pdf 167). Kahneman says it is tempting to conclude that causal base rates are used and merely statistical facts are more or less neglected, but the next study shows the situation is rather more complex (pdf 167).

### Can Psychology be Taught? (pdf 167–171)
- Causal base rates support two kinds of inference: a trait attributed to an individual (reckless drivers) and a feature of the situation (a hard exam). People drew these correctly. The next study shows they will not draw an inference that conflicts with other beliefs (pdf 167). Kahneman says it also supports the uncomfortable conclusion that teaching psychology is mostly a waste of time (pdf 167).
- **The helping experiment** (New York University). Participants sat in booths and took turns speaking over an intercom. There were six per group, one a stooge. The stooge described a tendency to seizures, then appeared to have one and asked for help. Only 4 of 15 participants responded immediately; six never left the booth; five came out only well after the apparent choking (pdf 167–168).
- The result shows that individuals feel relieved of responsibility when they know others also heard the request (pdf 168).
- Kahneman says readers will very probably be surprised, because we expect ourselves and other decent people to help. The teacher wants students to treat the low rate as causal, like the hard exam: a feature of the situation, diffusion of responsibility, makes normal, decent people unhelpful (pdf 168).
- **Nisbett and Borgida's study** (University of Michigan). Students watched short, bland interviews with two supposed participants who seemed nice, normal and conventional. They then guessed how fast each had helped (pdf 168–169).
- *Bayesian benchmark:* the base rate is 4/15, about 27%. The videos were designed to be uninformative, so the Bayesian answer is to stay with the base rate: the person probably did not rush to help (pdf 169).
- *Group 1* (procedure only) predicted that both would rush to help. *Group 2* (procedure and results) predicted no differently: "they learned nothing at all". They knew the base rate but stayed convinced the people on video helped (pdf 169).
- The same held for a second study, in which mild social pressure led people to accept painful shocks. Students "quietly exempt themselves" and their friends from surprising conclusions (pdf 170).
- *Group 3* learned the procedure but not the results. They were told that the two people on video had not helped, then guessed the overall results. Their guesses were extremely accurate (pdf 170).
- Nisbett and Borgida's summary: "Subjects' unwillingness to deduce the particular from the general was matched only by their willingness to infer the general from the particular." (pdf 170)
- Kahneman's conclusions:
  - Learning psychology means your understanding of situations has changed, not that you can repeat a fact (pdf 170).
  - Causal statistics have a stronger effect than noncausal ones, but even compelling causal statistics will not change long-held beliefs or beliefs rooted in personal experience (pdf 170).
  - There is a deep gap between our thinking about statistics and our thinking about individual cases (pdf 170).
  - Surprising individual cases are a more effective teaching tool because the incongruity must be resolved and embedded in a causal story. This is why the book asks questions addressed to the reader (pdf 170–171).

*Intuition note:* A fact about "people in general" can be admired and passed on without touching how you judge the person in front of you. A single case that breaks your expectation can force you to build a new story, which can change your beliefs.

### Speaking of Causes and Statistics (pdf 171)
- The chapter closes with two sample remarks. One says we cannot assume people will learn from mere statistics, so we should show them a few individual cases to influence their System 1. The other says there is no need to worry that statistical information will be ignored, because it will immediately be used to feed a stereotype (pdf 171).

## Toy example (ours)
A city has 1000 accidents. Blue cabs cause 10% (100) and Green cabs 90% (900). A witness is right 90% of the time.
- Of the 100 Blue accidents, the witness says "Blue" in 0.9 × 100 = 90.
- Of the 900 Green accidents, the witness wrongly says "Blue" in 0.1 × 900 = 90.
- Total "Blue" reports: 90 + 90 = 180. Real Blue among them: 90/180 = 50%.

The witness is 90% reliable, yet the answer is only 50%, because the base rate pulls it down. If the 10%/90% split were stated as "cab numbers in the city", intuition would tend to ignore it and say about 90%. If it were stated as "Green drivers cause 90% of accidents", people would likely use it.

## Concepts
- [[base-rate-neglect]] (new) — ignoring how common a category is when judging a case (pdf 164)
- [[statistical-base-rate]] (new) — population fact not tied to the individual case; underweighted (pdf 164)
- [[causal-base-rate]] (new) — base rate that changes the story of how the case arose; used easily (pdf 164)
- [[bayesian-inference]] (new) — combine a prior (base rate) with case evidence to get a posterior (pdf 163)
- [[stereotype]] (new) — group statement accepted, at least tentatively, as fact about every member; used neutrally by Kahneman (pdf 165)
- [[system-1-causal-thinking]] (new) — System 1 handles causal stories, weak at statistics (pdf 167)
- [[diffusion-of-responsibility]] (new) — people feel less responsible when others could also help (pdf 168)
- [[affect-heuristic]] (new) — Kahneman says reliance on it is common in politically charged arguments: favored positions seem to have no costs, opposed ones no benefits (pdf 166)

## Canonical instances
- [[cab-problem]] — same numbers, statistical vs causal framing; Bayesian answer 41% (pdf 163–164)
- [[ajzen-yale-exam-study]] — causal vs selected-sample base rates (pdf 166–167)
- [[helping-experiment]] — 4 of 15 helped immediately; the seizure stooge (pdf 167–168)
- [[nisbett-borgida-study]] — students learn from cases, not statistics (pdf 168–170)

## Bridges (candidates)
- [same-math] Base rate plus witness reliability ↔ probability: Bayes' rule with prior 0.15 and likelihood ratio 4:1 gives 0.12/0.29.
- [structural-analogy] Ajzen's "selected sample" base rate ↔ statistics: a sample built by selecting on the outcome distorts the apparent outcome rate.
- [structural-analogy] Neglect of a prior when vivid case evidence is present ↔ machine learning: ignoring class priors when a classifier sees case features.
- [metaphor] "Quietly exempt themselves" ↔ social science: people accept group findings but treat themselves as exceptions.

## Questions this raises
- Why does a causal framing make a base rate feel relevant, and can we train people to build the causal story for statistical facts?
- When should stereotype-like base rates be used, and when should social norms forbid them even at the cost of accuracy?
- If surprising cases teach better than statistics, how can teaching avoid over-generalizing from a single vivid case?
- How well does the Nisbett–Borgida result hold up? These pages give no sample sizes for it.

## Reading notes
- No printed page numbers are visible in the text layer, so all citations use (pdf N).
- The text layer has OCR noise. On pdf 163 a broken fragment follows "reliability of the witness,"; the rest of that sentence is not readable in the text layer. Other garbled bits are "Hely re" (pdf 165), "bs oase" (pdf 166), "andpeo" (pdf 167) and "statisticis al" (pdf 170).
- The 41% figure is Kahneman's. The calculation shown is my added check.
- The "27%" figure is 4/15, as stated on pdf 169.
