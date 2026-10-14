---
id: mcgrayne-2011-theory/ch11-business
work: mcgrayne-2011-theory
unit: "11. Business Decisions"
pages: 139-153
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
# Business Decisions (McGrayne, ch. 11)

## L0 — One line
In the 1960s Robert Schlaifer and Howard Raiffa turned Bayes' rule into practical tools for business decisions under uncertainty, but McGrayne says their attempt to make Bayes standard in business teaching and statistics ultimately failed.

## L1 — The gist (≤ 120 words)
Bayesians of the 1960s had elegant theory but few real applications. At Harvard Business School, Schlaifer and Raiffa asked how a manager should decide when there is little or no repeatable data. Their answer: combine a subjective prior with sample data, and weigh the cost of getting more data. They made this usable with decision trees, "tree-flipping", conjugate priors and the questioning of experts. Schlaifer wrote the first fully Bayesian textbook; Raiffa's program taught future business-school deans. Yet Bayesian decision analysis later shrank to a few weeks of study, and many statisticians ignored them. The chapter shows both what it took to make Bayes practical and why that effort fell short.

**Prerequisites:** conditional probability, i.e. P(x | y) versus P(y | x); the frequentist/Bayesian split; the idea of a prior.

## L2 — Key ideas (5–10 bullets)
- Bayesians seemed unwilling to apply their theories to real problems: one Bayesian called Savage's examples "dumb", and even diehard Bayesians preferred frequency methods for large data sets. Practical use was also held back by heavy calculation and a method seen as professionally almost taboo (pp. 139–140).
- McGrayne says frequentism offered businesses no help with issues like launching a product or changing a price (p. 141). Schlaifer saw that Bayes' rule could combine a subjective prior with objective data (p. 142).
- Raiffa moved from Neyman–Pearson statistics (a frequentist school built on error rates and accept/reject tests) to Bayesianism because he wanted probability statements about unknowns tied to decisions, not accept/reject tests (pp. 145–146).
- Their tools were decision trees (diagrams of sequential choices), tree-flipping (reordering a tree so test-result probabilities come first), conjugate priors (priors whose posterior keeps the same curve shape), and elicitation (interviewing experts for their judgment) (pp. 148–150).
- Raiffa said of tree-flipping, "We didn't call it Bayes"; McGrayne adds that it amounted to using Bayes' rule (p. 149).
- Raiffa and Schlaifer's advanced book (1961) set the direction of Bayesian statistics for two decades, and Raiffa's Ford Foundation program gave the next generation of business-school deans a heavy dose of Bayesian subjectivism (pp. 150–151).
- They ultimately failed to make Bayes standard in business curricula or statistics. McGrayne ties this partly to Schlaifer's theoretical style and lack of consulting (pp. 151–152).

## L3 — Walkthrough
(The chapter has no numbered sections; headings below are ours, following its order.)

**Opening: a professional embarrassment (pp. 139–140).**
- John Pratt complained that both Bayesians and frequentists published "too many minor advances" from sanitised, real or mythical problems (p. 139).
- Savage's textbook examples (rabbit ears, 20-pound chairs) were called "dumb" by a Harvard Business School Bayesian. With large data sets even diehard Bayesians used frequency methods. Lindley's 1961 exam-grading paper to Harvard did not mention Bayes (p. 139).
- Pratt: you cannot have an opinion afterwards without having had one before and updated it. The difficulty was making belief quantitative and precise (p. 139).
- Obstacles: laborious calculation, few computers, no packaged software, and a method seen as "almost taboo". "Brawn" had to substitute for computer time (p. 140).

**Schlaifer's path (pp. 140–143).**
- Schlaifer (born 1914) trained in classics and ancient history, took one math course, and worked on sonar in the war. He then wrote a 600-page book on aircraft engines for Harvard Business School (p. 141).
- Assigned to teach statistical quality control, he read Fisher, Neyman and Egon Pearson. Wartime operations research had mathematised inventory control and transport scheduling. Frequentism did not help with launching a product or changing a price (p. 141).
- His examples: a newsstand owner unsure how many *Daily Racing Form* copies to stock, and a wholesaler allocating ten trucks between two warehouses. Would extra data be worth its cost? (pp. 141–142)
- **McGrayne on the frequentist view:** objective statistics meant long-run relative frequency, and probabilities were invalid without repeatable observations. This suited grain crops, genetics, gambling, insurance and statistical mechanics (p. 142).
- Business executives often decide under extreme uncertainty without sample data; Schlaifer said they are forced to gamble (p. 142).
- His reasoning: whatever prior information executives have beats none. Then comes how to use sample data and how much to pay for it. Bayes' rule could combine subjectively assessed priors with objectively obtained data (p. 142).
- He threw away his books and reinvented Bayesian decision theory without knowing the objectivist–subjectivist dispute (p. 142). He judged his own math "of order of magnitude epsilon", so he recruited Raiffa from Columbia (p. 143).

*Intuition note:* Executives often had to decide without sample data. Schlaifer's step was to treat whatever prior information they had as better than none, then ask how to use sample data and how much to pay for it (p. 142).

**Raiffa's path (pp. 143–146).**
- Raiffa came from City College of New York. Anti-Semitism he met in the army and in housing pushed him towards actuarial work, which was graded by objective exams. He studied at the University of Michigan and finished a mathematics doctorate in 1952 (pp. 143–144).
- His statistics teaching there was entirely Neyman–Pearson; he did not recall hearing "Bayes" (p. 144).
- Von Neumann and Morgenstern's *Game Theory* led him, as he recalled, to assess judgmental probability distributions "without realizing how radically I was behaving" (p. 144, paraphrase of his account).
- Wald's *Statistical Decision Functions* was full of Bayesian decision rules inside a frequentist framework. Wald also said that every good decision procedure is Bayesian, and confided to Hilda von Mises that he was a Bayesian but did not dare say so publicly (p. 144).
- Raiffa taught Wald's course at Columbia after Wald's death in 1950 (p. 144). By 1955 he no longer thought tests, confidence intervals and unbiased estimation central, but stayed a "closet Bayesian" (p. 145).
- **Columbia colleagues' objection:** was he introducing "squishy judgmental, psychological stuff" into science? (p. 145)
- **McGrayne's contrast:** Neyman and Pearson weighed error rates and accepted or rejected hypotheses, and could not decide on an observed sample without considering samples that did not occur. Raiffa wanted one-of-a-kind decisions such as how much to stock or what to price (p. 145).
- Raiffa's wanted-statement: given prior beliefs and the sample, "I now believe there is a .92 probability" that $\tilde p > .25$ (p. 145, text-layer symbol). Frequentists recognised only outcomes "significant at the .05 level". He saw hypothesis testing as steering students wrongly (pp. 145–146).
- **Coleman case:** a sociology student looked "fuzzy" in his oral exam. Raiffa argued the department's prior opinion was so positive that a one-hour exam should not substantially alter their views, and urged a pass. Coleman later became a prominent sociologist (p. 146).
- Harvard hired him in 1957 for statistics and the business school. Mosteller was tolerant but lukewarm; Cochran said "you'll grow up"; Schlaifer welcomed him (p. 146).

**The partnership (pp. 146–148).**
- Raiffa tutored Schlaifer daily in calculus and linear algebra; Schlaifer then conjectured theorems and applied them. They used no journals or books (p. 146).
- Schlaifer was better read in prewar theorists; Raiffa had not read Jeffreys, Fisher, Pearson or Ramsey (p. 147).
- Schlaifer insisted there was one right way and, as his student Schleifer recalled, attacked alternatives with paradoxes. He regarded Raiffa's plan to teach both schools as teaching falsehood (p. 147).
- By 1958 Raiffa was a committed subjectivist. Four businesses could reach four different conclusions from the same information. McGrayne notes this still bothers some, while others let large new data overwhelm initial priors (p. 147).
- Betting became the tangible expression of belief in Schlaifer's group, and critics called the school "a Bayesian hothouse" (p. 148).

**The tools (pp. 148–150).**
- Schlaifer's 1959 textbook was the first written entirely from the Bayesian view. Students could do inventory, marketing and queuing problems with arithmetic, slide rules or a desk calculator (p. 148).
- Bayesians had no "bookshelves of mathematical tools". Raiffa and Schlaifer set out in 1958 to make Bayes operational (p. 148).
- **Decision trees:** diagrams of sequential choices, e.g. act now or collect more information first. Raiffa did not claim to invent them but became "Mr. Decision Tree". McGrayne calls trees probably the best-known practical application of Bayes' rule (pp. 148–149).
- **Tree-flipping:** for a student studying wildcat oil drilling, Raiffa reversed the usual order, test then drill. He handled the probability of test results first and the decision to test afterwards. This put "y's first" instead of x's followed by y's. It amounts to Bayes' rule, since P(x | y) and P(y | x) are its two key elements (p. 149).
- Raiffa: "we didn't call it Bayes"; using the theorem directly was "too complicated" (p. 149).
- **Conjugate priors:** in many cases the prior and posterior have the same curve shape, e.g. Gaussian prior gives Gaussian posterior. This helps with repeated updating. McGrayne says MCMC later made it unnecessary (p. 149).
- Some business Bayesians dropped priors unless there was overwhelming prior evidence (Arthur Schleifer Jr.'s view) (p. 149).

*Intuition note:* Tree-flipping redraws the tree so the probabilities of the test results come first. Raiffa's point was that people could do this by common sense without invoking Bayes' theorem (p. 149). (Our reading: this gives the chance of oil after a given test result.)

**Expert opinion and spread (pp. 149–151).**
- No one knew whether executives would give opinions or whether those would be valid. John Pratt's wife Joy estimated theatre attendance; her estimates were at first too narrow, but after hundreds of comparisons with actual figures they became accurate (pp. 149–150).
- Bayesians objected that Pratt and Schlaifer analysed those data with frequentist techniques (p. 150).
- Executives liked having "managerial intuition" included early. DuPont (1962, size of a factory for artificial shoe leather) assessed prior odds of demand; Ford engineers' opinions let Ford use smaller samples (p. 150).
- Engineering example: of 20 sources of uncertainty, perhaps 12 handled by single guesses, 5 needing more testing, 2 needing expert interviews (p. 150).
- A weekly decision-making-under-uncertainty seminar ran 1961–65. *Applied Statistical Decision Theory* (1961) set Bayesian statistics' direction for two decades (p. 150).
- *Introduction to Statistical Decision Theory*: typescript in 1965, finished by Pratt and Raiffa as an 875-page MIT book thirty years later (p. 151).
- Raiffa's 1960–61 Ford Foundation program taught business professors; by 2000 Bayesian methods were often centred in business schools rather than statistics departments (p. 151).
- Raiffa then moved to societal issues: the Kennedy School, East–West think tank, negotiation teaching, advising McGeorge Bundy (p. 151).

**Why it fell short (pp. 151–153).**
- Bayesian decision analysis faded from the Harvard curriculum and became a few weeks' study. Students no longer do their own calculations (p. 152).
- Many theoretical statisticians ignored them as business-school outsiders; Lindley was astonished at this neglect (p. 152).
- **McGrayne's reasons:** Schlaifer set aside problems he could not solve, favoured short-term results, did little consulting, and stripped cases of real-world context. His text *MERC* was burned by students (p. 152).
- He died in 1994. Pratt and Raiffa dedicated the book to him (p. 153).

## Toy example (ours, not from the text)
Wildcatter's test, flipped. Assume P(oil) = 0.2. Assume the test is positive with probability 0.9 if oil and 0.3 if dry.
- Original tree (state first, then result) gives joint probabilities: P(oil and +) = 0.2 × 0.9 = 0.18; P(dry and +) = 0.8 × 0.3 = 0.24.
- Flip: P(+) = 0.18 + 0.24 = 0.42. P(oil | +) = 0.18 / 0.42 ≈ 0.43.
- P(oil and −) = 0.2 × 0.1 = 0.02; P(dry and −) = 0.8 × 0.7 = 0.56. P(−) = 0.58, so P(oil | −) = 0.02 / 0.58 ≈ 0.03.
- The flipped tree starts with the result (0.42 vs 0.58) and then gives the chance of oil, which is what the drilling decision needs.

## Concepts
- [[bayes-theorem]] — rule combining prior and sample data; here used by trees without being named (pp. 142, 149)
- [[prior-distribution]] — subjectively assessed starting belief, even from experts (pp. 142, 149–150)
- [[subjective-personal-probability]] — belief expressed in bets and judgment; Raiffa's .92 statement (pp. 145, 148)
- [[frequentist-vs-bayesian]] — McGrayne's contrast: error rates and accept/reject vs probabilities for unknowns (pp. 142, 145)
- [[conjugate-prior]] — prior whose posterior has the same curve shape (p. 149)
- [[decision-tree]] (new) — diagram of sequential choices and uncertainties, such as act now or collect more information (p. 148)
- [[tree-flipping]] (new) — reordering a tree so outcome probabilities come first; amounts to Bayes' rule (p. 149)
- [[decision-under-uncertainty]] (new) — choosing without repeatable data, weighing the value of extra information (p. 142)
- [[expert-elicitation]] (new) — interviewing and calibrating experts to build priors (p. 150)

## Canonical instances
- [[wildcatter-oil-drilling]] — test-then-drill decision that motivated tree-flipping (p. 149)
- [[coleman-oral-exam]] — Raiffa argued that a strongly positive prior opinion should not be substantially altered by a one-hour exam (p. 146)
- [[joy-pratt-attendance]] — feedback made an expert's estimates accurate (pp. 149–150)
- [[dupont-shoe-leather]] — prior odds of demand used for factory size (p. 150)
- [[newsstand-and-trucks]] — Schlaifer's small business decision problems (pp. 141–142)

## Bridges (candidates)
- [same-math] Tree-flipping ↔ Bayes' theorem: reversing P(result | state) into P(state | result)
- [same-math] Raiffa's conjugate priors ↔ Beta–Binomial conjugacy: both are closed-form updating within one family
- [structural-analogy] Coleman exam and strong department prior ↔ base-rate neglect: ignoring the prior would overweight a weak test
- [structural-analogy] Joy Pratt's calibration against data ↔ prior predictive checks: testing a prior against real data

## Questions this raises
- How should one measure and improve an expert's calibration before using the expert's prior?
- When data are plentiful, how much does the choice of prior matter?
- Is tree-flipping easier for novices than the formula, or does it hide the logic?
- Did computers and MCMC remove the need for the shortcuts Raiffa introduced?

## Reading notes
- Printed page = pdf − 15. Pages are 139–153.
- Spellings vary in the text: "Schlaiffer" (p. 143), "Schleifer" for Arthur Schleifer Jr. (pp. 140, 147–149), "mathema-tics" (p. 151, line-break hyphen).
- Raiffa's .92 quote uses a tilde on p (p̃) in the text layer (p. 145). I kept the symbol as extracted.
- The chapter has no equations or exercises. Almost all claims are McGrayne's narrative or quotations from participants.
