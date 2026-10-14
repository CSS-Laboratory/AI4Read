---
id: mcgrayne-2011-theory/ch12-who
work: mcgrayne-2011-theory
unit: "12. Who Wrote The Federalist?"
pages: 154-162
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
# Who Wrote The Federalist?

## L0 — One line
Mosteller and Wallace used Bayes' rule, in odds form and with marker words, to attribute 12 disputed Federalist papers to Madison, and found that the prior mattered little.

## L1 — The gist (≤ 120 words)
After the 1948 polling and Kinsey scandals, Frederick Mosteller looked for a classification problem. He chose the 12 Federalist papers whose author, Madison or Hamilton, was disputed. With David Wallace he spent about ten years on a Bayesian analysis, using the frequencies of common "marker" words (words whose use differs by author), odds instead of probabilities, and early computers. In 1964 they reported odds "satisfyingly fat" that Madison wrote all 12. Their main surprise was that the choice of prior (starting belief) mattered little compared with the choice of data model. It was the biggest Bayesian application of its time, but nobody followed it up.

**Prerequisites:** probability vs odds; the idea of updating a belief with evidence; what a prior is.

## L2 — Key ideas (5–10 bullets)
- The project began as a classification (discrimination) problem, not as a Bayesian crusade. Mosteller was an eclectic who used whatever technique worked (pp. 155–156).
- Wallace pushed for Bayes because, with many unknowns, Bayesian and non-Bayesian answers differ greatly (p. 156).
- Topic-dependent words were ignored (p. 157). Context-free words such as "upon", and later marker words such as "whilst" and "enough", became evidence about authorship (pp. 157, 159–160).
- They started from 50–50 odds, updated word by word, and worked in odds language (pp. 157–158).
- Hand counting and early computers slowed the work. Mosteller used about 100 helpers (pp. 159–160).
- Surprise: the prior was not of major importance. The choice of data model deserved more attention (p. 161).
- Result: the odds were "satisfyingly fat" that Madison wrote all 12 papers; the weakest case was No. 55 at 240 to 1 (p. 161).
- It was admired but not followed up, and Mosteller never again devoted a whole project to Bayes (pp. 161–162).

## L3 — Walkthrough

### Origins: the two 1948 scandals (pp. 154–155)
- Pollsters failed to predict Truman's 1948 win. Mosteller, appointed to investigate, blamed pollsters for rejecting randomized sampling. Their outdated designs underrepresented blacks, women and the poor, who voted more heavily Democratic (p. 154).
- Kinsey's work lacked randomized sampling. Mosteller still judged it far better than anyone else's. It was quietly arranged (the text does not say by whom) that Jerome Cornfield would help with the statistics of the next study (p. 154).
- Both scandals were **discrimination (classification) problems**: assigning people or things to categories without being sure the assignments are accurate or the categories well defined (p. 155).

### Choosing the problem (p. 155)
- Mosteller wanted a large database for discriminating between two cases, and thought of the Federalist papers, not of Bayes' rule (p. 155).
- Hamilton, Jay and Madison wrote 85 anonymous articles in 1787–88. Historians could attribute most, but no one agreed whether Madison or Hamilton wrote 12 others (p. 155).
- In 1941 he had counted sentence lengths with Frederick Williams. Hamilton and Madison were stylistically "practically twins", so Mosteller agreed to "leave general style as a poor bet and pay attention to words" (p. 155).

### Why Bayes, and Mosteller's stance (pp. 156–157)
- By 1955 he recruited David Wallace. Wallace urged Bayes' rule, having been exposed to Savage's teaching (p. 156).
- **Wallace's view:** on simple textbook problems Bayesian and non-Bayesian answers are not appreciably different. With large numbers of unknowns the difference "grows immense" (p. 156).
- Mosteller was no fervent Bayesian. He accepted both degrees of belief and relative frequency. A unique event such as "Hamilton wrote paper No. 52" is hard to treat with sampling theory. Degrees of belief are harder to specify but more widely applicable (p. 156).
- He disliked the gap between many Bayesian theories and few practical applications (p. 157).
- Data: 94,000 words surely by Hamilton and 114,000 by Madison. Topic-dependent words ("war", "executive", "legislature") were ignored. Context-free words ("in", "an", "of", "upon") were kept (p. 157).
- They then decided to make the project a serious empirical comparison of Bayesian and frequentist methods (p. 157).

### Method (pp. 157–158)
- Probabilities express degrees of belief about propositions like "Hamilton wrote paper No. 52". Bayes' theorem adjusts them with more evidence (p. 157).
- They began with 50–50 odds per paper and used the frequencies of 30 words, one at a time, to improve the estimate (p. 157).
- Two stages: first the 57 papers of known authorship, then the 12 disputed ones. Wallace developed asymptotic approximations for hard integrals (p. 157).
- They worked in **odds** because it was easier computationally and intuitively (pp. 157–158).

*Intuition note:* Odds say "how many times more likely one author than the other". Each marker word can push the odds one way or the other. The authors say single words would not suffice, so they accumulated many marker words (p. 159).

### Mosteller beside the project (pp. 157–159)
- With Savage's encouragement they set out to "apply a 200-year-old mathematical theorem to a 175-year-old historical problem". It would be the largest civilian application of Bayes' rule since Laplace and Jeffreys, and they would turn to "high-speed computers" (p. 157).
- During the decade of the analysis Mosteller was the person to call when something went wrong. Over the years Harvard asked him to chair four departments, and he persuaded Harvard to set up a statistics department (p. 158).
- He wrote two textbooks on frequentism and Bayes' rule for high school students and taught probability on NBC's Continental Classroom in 1961 (p. 158).
- He worked in small groups of collaborators and wrote or cowrote 57 books, 36 reports and more than 360 papers. Cleo Youtz was his statistical assistant for more than 50 years (p. 159).

### Marker words and labour (pp. 159–160)
- Historian Douglass Adair pointed to a 1916 study: Hamilton used "while", Madison "whilst" (p. 159).
- One word was not enough. Printer errors or editing could taint it, so many marker words had to be counted in every paper (p. 159).
- Harvard had no computer of its own, and Fortran was new and awkward for words. Mosteller used about 100 helpers (80 students, 20 others) to punch cards. Youtz organized a hand-made concordance (word index) from typed tape strips (p. 160).
- Hamilton used "upon" about twice per paper and Madison seldom. "Enough" was used by Hamilton, never by Madison. Four words pointed to Madison (p. 160).
- Authors may have edited each other's papers, so Mosteller and Wallace said they would offer no "absolutely conclusive settlement", only strong confidence (p. 160).
- They tackled 25 technical problems and published four parallel studies comparing Bayes, frequentism and two simplified Bayesian approaches. "Upon" was the best discriminator by a factor of four. "Whilst", "there" and "on" were also good (p. 160).

### Findings (pp. 160–161)
- **Mosteller:** the prior was less important than expected. Statisticians should pay less attention to the prior and more to the model for the data (p. 161).
- They included prior odds only because Bayes' theorem called for them, and arbitrarily assigned equal odds to Madison and Hamilton. The prior odds were so unimportant that readers could have been let to name them (p. 161).
- Analogy: one astronaut's measurement of lunar dust would overwhelm any expert's prior opinion. Asked why include a prior at all, Mosteller's answer was: because with controversial or scanty data, enormous amounts of observational material might be needed to decide the issue (p. 161).
- 1964 report: odds "satisfyingly fat" for Madison on all 12; the weakest case, No. 55, was 240 to 1 (p. 161).

*Intuition note:* With enough strong evidence, different starting beliefs lead to nearly the same conclusion. The authors say this holds for their data. For still including a prior they give this reason: with controversial or scanty data, enormous amounts of observational material might be needed to decide the issue (p. 161).

### Aftermath (pp. 161–162)
- It was the fourth Bayes work in three years (after Jeffreys, Savage, Raiffa and Schlaifer), and the only one to treat real issues with modern computers. Mosteller thought about the problem for 23 years and worked on it for ten (p. 161).
- It was still admired, and as late as 1990 it was considered the greatest single Bayesian case study. But no one followed it up, and no one reanalyzed it with non-Bayesian methods (p. 161).
- Mosteller never again devoted an entire project to Bayes. He wrote to a student who had won a prize for a Bayesian thesis: "I think Bayesian methods are about to take off. But then I've been saying that for twenty-five years" (p. 162).

## Toy example (ours, not from the text)
Invented numbers. Odds are Madison : Hamilton, and the prior is 1:1.
- Word A, "upon": suppose 8 of 10 known Hamilton papers contain it, and 1 of 10 Madison papers. The disputed paper lacks it. Probability of absence: Hamilton 2/10, Madison 9/10. Ratio = 9/2 = 4.5. Odds → 1 × 4.5 = 4.5.
- Word B, "whilst": suppose 4 of 10 Madison papers contain it, and 1 of 10 Hamilton papers. The disputed paper has it. Ratio = 4/1 = 4. Odds → 4.5 × 4 = 18. (Multiplying assumes the words are independent given the author; added step.)
- 18:1 means probability 18/19 ≈ 0.947 for Madison.
- Prior check: prior odds 1:3 give 1/3 × 18 = 6; prior odds 3:1 give 3 × 18 = 54. Madison is favoured either way, which echoes the finding that the prior mattered little.

## Concepts
- [[prior-distribution]] — starting belief; here 50–50 odds, found to matter little (p. 161)
- [[bayes-theorem]] — adjusts the probability of "Hamilton wrote No. 52" as evidence arrives (p. 157)
- [[frequentist-vs-bayesian]] — Mosteller accepted both kinds of probability, and compared both methods empirically (pp. 156–157)
- [[subjective-probability]] — degrees of belief about unique events (p. 156)
- [[sequential-updating]] — each word's frequency improves the earlier estimate; the text says "one at a time" (p. 157)
- [[discrimination-classification-problem]] (new) — assigning cases to categories without certainty (p. 155)
- [[marker-words]] (new) — words such as "upon", "whilst" and "enough" whose use differs by author (pp. 157, 159–160)
- [[odds-form-of-bayes]] (new) — authors used odds instead of probabilities for ease (pp. 157–158)

## Canonical instances
- [[federalist-papers-authorship]] — Bayesian attribution of 12 disputed papers to Madison (pp. 155–161)
- [[1948-polling-failure]] — Truman election, blamed on non-random sampling (p. 154)
- [[kinsey-report-sampling]] — bestselling study lacking randomized sampling (p. 154)

## Bridges (candidates)
- [structural-analogy] word-by-word odds updating ↔ machine learning: naive Bayes text classifier — evidence from many features combined into one score; the text does not state independence.
- [structural-analogy] prior swamped by strong data ↔ Bayesian inference: posterior insensitive to prior with large samples (the astronaut's lunar-dust example, p. 161).
- [metaphor] Bayes as a way of "accommodating new ideas" ↔ learning theory, as Mosteller used it (p. 158).

## Questions this raises
- How large must the evidence be before the prior stops mattering, and when do scanty data keep it important?
- Why did no one reanalyze the papers non-Bayesianly, and what would a modern replication show?
- How sensitive are the odds to the choice of model for word counts, which the authors say deserves more attention?

## Reading notes
- Printed page = pdf − 15 (pdf 169 = p. 154). The text layer matched the printed numbers.
- The chapter contains no equations or exercises. Page 154 begins with the chapter title block.
- The odds figures (e.g., 240 to 1) are quoted without the underlying calculations. The prose gives no formulas.
- "Upon … by a factor of four" (p. 160) is the author's phrase and is left unexplained in the text.
