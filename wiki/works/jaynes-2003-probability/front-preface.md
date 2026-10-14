---
id: jaynes-2003-probability/front-preface
work: jaynes-2003-probability
unit: Preface
pages: pdf 20–30 (printed pages xix–xxix; see Reading notes)
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Preface (Jaynes, *Probability Theory: The Logic of Science*)

## L0 — One line
Jaynes argues that the rules of probability are the unique consistent rules for plausible reasoning under incomplete information, not just rules for frequencies of "random variables".

## L1 — The gist (≤ 120 words)
The Preface says what the book is for and how it is written. The question is how to reason when information is incomplete. Jaynes answers that Pólya's desiderata (qualitative requirements of common sense) plus Cox's consistency theorems give the sum and product rules as the unique quantitative rules of inference, if plausibilities are real numbers. He therefore treats probability as extended logic. He argues that frequentist devices are narrow special cases with ad hoc add-ons, that Bayesian methods and maximum entropy cover more, and that prior information matters greatly. He also favours a finite-sets policy and puts clarity before rigor. Part 1 covers principles and elementary applications; Part 2 covers more advanced applications, including maximum-entropy ones.

**Prerequisites:** basic probability (sum and product rules), the idea of a sampling distribution, a rough sense of "frequentist vs Bayesian"; no deep mathematics.

## L2 — Key ideas (5–10 bullets)
- Inference means deduction when information suffices and plausible reasoning when it does not. The book's topic is the optimal processing of incomplete information (pdf 20).
- Pólya's qualitative desiderata plus Cox's consistency theorems give a unique set of quantitative rules, if plausibilities are real numbers. These are the standard probability rules, now read as logic with no reference to "chance" (pdf 21).
- Jaynes claims frequentist methods are the most restricted special case. He says ad hoc devices (unbiased estimators, confidence intervals, tail-area tests) always generate inconsistencies or absurd results in extreme cases. He says Bayesian methods correct these defects in well-developed problems, and that his rules contain both Bayesian and frequentist calculations as particular cases but are broader than either (pdf 23–24).
- Maximum entropy (assigning probabilities directly from the data's constraints) suits problems with a sample space (the set of possible outcomes) but no model. Bayesian methods add a model, which may be speculative (pdf 24–25).
- The theory reproduces human reasoning phenomena, e.g. a truthful person not being believed, and divergence of opinions (pdf 26).
- Prior information strongly affects conclusions. In Jaynes's example, a model that does not allow a threshold effect prejudges the issue, and a false premise built into a model that is never questioned cannot be removed by any amount of new data (pdf 26–27).
- Jaynes says infinite-set paradoxes come from (1) jumping into an infinite set without specifying a limiting process and (2) asking questions whose answers depend on how the limit is approached. His basic rules admit only finite sets and infinite sets arising as well-defined limits of finite ones (pdf 23).
- Logic and clarity come before "rigor", which Jaynes says has no trustworthy standard once infinite sets are accepted (pdf 28).

## L3 — Walkthrough

**Audience and aim (pdf 20).** The readers are assumed to know advanced-undergraduate applied mathematics and a field where inference is needed. Prior probability or statistics training is not needed; a little "innocence" may help, since there is less to unlearn. Jaynes is concerned with probability theory and all of its conventional mathematics, viewed in a wider context. He expects that something like this theory will become the conventional probability theory of the future.

Footnote 1: "inference" means deduction when information permits it, and plausible reasoning otherwise. Problems solvable by deduction do not need probability theory, so the topic is the optimal processing of incomplete information (pdf 20).

**History (pdf 20–22).**
- Jaynes's interest began with Jeffreys (1939), followed by Cox (1946), Shannon (1948) and Pólya (1954). The writing began as Stanford lecture notes in 1956 on Pólya's *Mathematics and Plausible Reasoning* (pdf 20).
- Pólya broke common sense into elementary qualitative desiderata. Mathematicians had used these in the early, pre-proof stages of discovery. Pólya thought the resemblance to Bernoulli and Laplace was only qualitative (pdf 20–21).
- His agreement was so detailed that it suggested more. Cox's consistency theorems then settled it. Adding Pólya's conditions to Cox's gives the result: if degrees of plausibility are real numbers, there is a uniquely determined set of quantitative rules for inference. Any rules whose results conflict with them violate an elementary desideratum of rationality or consistency (pdf 21).
- These rules are the standard probability rules. What is new is that they are seen as principles of logic in general, with no reference to "chance" or "random variables". So the supposed distinction between "probability theory" and "statistical inference" disappears (pdf 21).
- Over 1957–1970 the lectures were repeated and grew. Old difficulties that led to rejection of Laplace's work are said to be misapplications. They arose from an ambiguously defined problem or from ignoring seemingly trivial side information (pdf 21).
- After about 1970 the material grew through research, and the book is meant to work as textbook or reference. Jaynes says the work of Jeffreys, Pólya and Cox is timeless, and predicts it will be crucially important in all areas 100 years hence (pdf 22).

*Intuition note.* On Jaynes's account, the rules of probability follow from consistency requirements (given real-number plausibilities), so they are not tied to frequencies. Any other rules whose results conflict with them violate an elementary, nearly inescapable desideratum of rationality or consistency.

**Foundations (pdf 22–23).**
- Jaynes's system differs greatly from Kolmogorov's in style, philosophy and purpose. In his view, about half of needed probability theory, assigning probabilities by logical analysis of incomplete information, is absent from Kolmogorov's system (pdf 22).
- Yet he finds himself in agreement with Kolmogorov, and in disagreement with Kolmogorov's critics, on nearly all technical issues. Each Kolmogorov axiom is, for practical purposes, derivable from the Pólya–Cox desiderata (Appendix A). He sees his system as extending Kolmogorov's, not contradicting it (pdf 22).
- With de Finetti he finds only a loose philosophical agreement. He disagrees strongly on many technical issues. It appears to him that de Finetti's way of treating infinite sets opened a "Pandora's box" of useless and unnecessary paradoxes. Nonconglomerability and finite additivity are examples (Chapter 15) (pdf 22).
- **Jaynes's remedy:** the basic rules admit only finite sets and infinite sets that are well-defined limits of finite ones. The paradoxes come from (1) jumping into an infinite set without a limiting process, and (2) asking questions whose answers depend on how the limit is approached (pdf 23).
- Example: "What is the probability that an integer is even?" can have any answer in $(0,1)$, depending on the limiting process defining "all integers". This is like a conditionally convergent series, which can sum to any number depending on term order (pdf 23).
- An infinite set has no "existence" or mathematical properties in probability theory until the limiting process is specified. He sails with Gauss, Kronecker and Poincaré, not Cantor, Hilbert and Bourbaki, and cites Kline (1980) (pdf 23).

*Intuition note.* "Fraction of integers that are even" is not defined by the set alone. It depends on how you build the infinite set from finite ones.

**Comparisons (pdf 23–25).**
- Jaynes has been an outspoken Bayesian partisan (earlier record: Jaynes 1983). He now claims arguments can cite proven theorems and worked numerical examples, not philosophy. He says the superiority of Bayesian methods is "a thoroughly demonstrated fact in a hundred different areas" (pdf 23). This is his claim.
- Yet neither Bayesian nor frequentist approach is universally applicable. The theme is probability theory as extended logic. The rules are not merely for calculating frequencies of random variables; they are the unique consistent rules for inference of any kind (pdf 23).
- All Bayesian and all frequentist calculations are particular cases, but the rules are broader than either (pdf 24).
- **Jaynes's critique of frequentist methods** (pdf 24):
  - Methods using only sampling distributions are useful in simple idealized problems. They presuppose independent repetitions with no relevant prior information, which is hardly ever met.
  - They offer no technical means to eliminate nuisance parameters or use prior information. They have no way even to use all the information in the data when sufficient or ancillary statistics do not exist.
  - They force one to "choose a statistic" by intuition, then to invent ad hoc devices. Jaynes says Cox's theorems guarantee that such devices give inconsistencies or absurd results in extreme cases.
- **Bayesian methods** (Jeffreys) handle these problems. They find optimal estimators automatically, use prior information, handle nuisance parameters, and, being exact, keep giving reasonable results in extreme cases. They arise from the sum and product rules, with no room for ad hoc devices (pdf 24).
- Bayesian methods need a developed problem: model, sample space, hypothesis space, priors, sampling distribution. Many problems stay in an "exploratory phase" where neither frequentist assumptions nor the Bayesian apparatus applies (pdf 24).
- For such problems the **Principle of maximum entropy** has, in Jaynes's view, the clearest justification and is the most developed computationally. It needs a sample space but no model or sampling distribution; in effect it builds a model from the data's constraints. Footnote 3 lists criteria of optimality (Chapters 11, 8, 7). For example, the model is the simplest one capturing all the information in the constraints (pdf 24–25).
- **Contrast:** Bayesian analysis may use a model, which expresses prior knowledge or a working hypothesis beyond the data. So it may be speculative. If the extra hypotheses are true, Bayesian results are expected to improve on maximum entropy; if false, they will likely be worse (pdf 25).
- Maximum entropy invokes nothing beyond the sample space and the data's evidence. It predicts observable facts, not parameters that may exist only in imagination. It is therefore the safest tool when little is known beyond raw data (pdf 25).
- Part 2 treats maximum-entropy applications, including statistical mechanics, spectrum analysis and image reconstruction. Jaynes expects the last two to evolve into the Bayesian phase (pdf 25).
- Numerical examples are supplied by three books: Bretthorst (1988), Buck and Macaulay (1991), Sivia (1996). MAXENT workshop proceedings also contain applications (pdf 25–26).

*Intuition note.* Maximum entropy is a "no extra assumptions" tool and Bayesian modelling is a "bet on a model" tool. If the model is right, Bayesian results are expected to improve on maximum entropy; if it is wrong, they will likely be worse.

**Mental activity (pdf 26).** Probability as extended logic reproduces features of human judgment. In Chapter 5 the equations show a person who tells the truth and is not believed, even though the disbelievers reason consistently. They also reproduce divergence of opinions, where two persons given the same information have their opinions driven in opposite directions. Jaynes says the theory shows what must be done to avoid this.

**What is "safe"? (pdf 26–27).**
- Main practical message: prior information greatly affects what conclusions a data set supports (pdf 26).
- Jaynes calls a linear no-threshold response model a common error. It is presumably right for cumulative poisons such as mercury and lead. For virtually every organic substance, a finite metabolic rate implies a finite threshold dose rate. Otherwise humanity could not have survived what it eats (pdf 26).
- Inference should estimate the slope and, more importantly, decide whether there is evidence for a threshold and estimate it. Effects seen only at "kilodoses" (1000 times normal) are, he argues, evidence of safety rather than danger. Sugar in overdose is far more dangerous, yet nobody proposes banning it (pdf 27).
- A model allowing no threshold prejudges the issue. In Jaynes's words, a false premise in an unquestioned model "cannot be removed by any amount of new data" (pdf 27).
- Likewise, new data analysed with old, unquestioned models cannot lead us out of old ideas. Coin-tossing data analysed with a stochastic model could never have led to Newtonian mechanics (pdf 27).
- Example: Bayesian spectrum analysis of nuclear magnetic resonance data gives accurate determinations not accessible by Fourier-transform analysis (pdf 27). Data "filtered" under false assumptions may lose information irreversibly. He says orthodox detrending and seasonal adjustment in econometrics do this. Preserved unmutilated data may be reusable later (pdf 28).

**Style of presentation (pdf 28–29).**
- In Part 1, chapters open with verbal discussion of the problem's logic and pitfalls, then mathematics. Part 2 goes straight to mathematics. Jaynes says students find the mathematics easy and the link from real problem to mathematics hard (pdf 28).
- He claims only that he does not knowingly give erroneous arguments (pdf 28).
- Two reasons for stressing logic over rigor (pdf 28):
  1. An argument is no stronger than its premises. Jeffreys noted that those who stress mathematical rigor most are the ones who, lacking a sure sense of the real world, tie their arguments to unrealistic premises and destroy their relevance; he likened this to anchoring steel beams in plaster.
  2. There are no trustworthy standards of rigor in mathematics that embraces infinite sets. Kline (1980, p. 351) is quoted asking whether a bridge designed with infinite sets or the axiom of choice might collapse. Jaynes says the only real rigor today is elementary arithmetic on finite sets of finite integers.
- The finite-sets policy is followed when it matters for results. After a result is derived from the rules, convenient approximations (e.g. sum to integral) are allowed (pdf 29).
- Strict use of the rules avoids paradoxes of orthodox statistics (Chapters 15, 17). It also simplifies computation (pdf 29):
  1. No sampling distribution of a "statistic" is needed; the data's evidence is in the likelihood function.
  2. Nuisance parameters can be eliminated at the start, reducing the search dimension. With several parameters, this can mean orders of magnitude less computation than least squares or maximum likelihood.
- Jaynes predicts that workers in all quantitative sciences will be obliged to use probability as extended logic. To progress, a "healthy disrespect" for tradition and authority is needed. The language is plain English, with no "meta-language" (pdf 29).

**Acknowledgments (pdf 30).** Jaynes thanks Jeffreys, Cox, Pólya, Shannon, about 300 former students and a long list of colleagues. The Preface is signed E. T. Jaynes, July 1996.

## Toy example (ours, not from the text)
Illustrates the "integers are even" point: the answer depends on the limiting process.
- **Process A:** take the first $N=12$ integers $1,\dots,12$ in natural order. Evens: 2, 4, 6, 8, 10, 12, so 6 of 12, and the fraction is $6/12 = 1/2$. This stays $1/2$ for every even $N$.
- **Process B:** list integers in blocks of two odds then one even: 1, 3, 2, 5, 7, 4, 9, 11, 6, 13, 15, 8. This is a reordering of the same integers. The first 12 terms hold evens 2, 4, 6, 8, so 4 of 12, and the fraction is $4/12 = 1/3$. At every block end it is $k/(3k)=1/3$.
- Same infinite set, different limits ($1/2$ vs $1/3$). So the question is not well posed until the limit process is specified, which is Jaynes's point.

## Concepts
- [[probability-as-extended-logic]] — probability rules as the unique consistent calculus of plausible reasoning, not only of frequencies (pdf 21, 23)
- [[cox-theorem]] — Cox's consistency theorems; with Pólya's desiderata they fix the quantitative rules if plausibilities are real numbers (pdf 21)
- [[maximum-entropy-principle]] — assign probabilities from a sample space and data constraints, with no model or sampling distribution; nonspeculative (pdf 24–25)
- [[frequentist-vs-bayesian-inference]] — Jaynes: frequentist methods are a restricted special case; Bayesian methods correct those defects in well-developed problems; both are contained in his rules, which are broader than either (pdf 23–24)
- [[prior-distribution]] — prior information as essential to correct inference; ignoring it can mislead (pdf 26–27)
- [[nuisance-parameter-elimination]] (new) — removing nuisance parameters at the start by the rules of probability; frequentist methods lack a principled way (pdf 24, 29)
- [[finite-sets-policy]] (new) — infinite sets allowed only as well-defined limits of finite ones (pdf 23, 29)
- [[exploratory-phase]] (new) — stage where model, priors and sampling distribution are not yet available (pdf 24)

## Canonical instances
- [[even-integer-probability]] — "probability that an integer is even" can be any value in $(0,1)$, depending on the limiting process (pdf 23)
- [[saccharin-threshold]] — no-threshold linear dose-response models prejudge the issue; kilodose effects are irrelevant (pdf 26–27)
- [[divergence-of-opinions]] — same information can drive two people to opposite views (pdf 26)
- [[nmr-bayesian-spectrum-analysis]] — Bayesian analysis recovers phenomena that Fourier-transform analysis could not (pdf 27)
- [[coin-tossing-newtonian-mechanics]] — stochastic coin-toss modelling could never find Newtonian mechanics (pdf 27)

## Bridges (candidates)
- [structural-analogy] Maximum-entropy assignment ↔ statistical mechanics: the Preface says all presently known statistical mechanics is included in the maximum-entropy approach (pdf 25).
- [structural-analogy] Model that cannot be corrected by data ↔ causal inference: a built-in false premise stays unchallenged, as with unmeasured-confounding assumptions.
- [metaphor] Jeffreys's "steel beams in plaster" ↔ model misspecification: rigorous mathematics resting on unrealistic premises (pdf 28).

## Questions this raises
- What exactly are Pólya's and Cox's desiderata, and which step forces the product and sum rules?
- How does maximum entropy "create a model" from constraints, and in what sense is it optimal by the criteria in footnote 3?
- Do the paradoxes (nonconglomerability, finite additivity) vanish with a limiting-process policy, as claimed?
- How do divergence of opinions and the "truthful but disbelieved" person arise from the equations (Chapter 5)?

## Reading notes
- Page labels: pdf 20–21 are labelled printed 17–18 but the text shows running numbers xix, xx. Pdf 22–30 have no printed label; the text shows xxi–xxix. Offset: roman printed number = pdf − 1. I cite pdf pages as instructed.
- No page images were provided; I worked from the text layer. It was clean, with no equations. No misprints found.
- The Preface has no exercises, so the Exercises section is omitted.
- Claims about the superiority of Bayesian methods and about frequentist failures are Jaynes's own claims, reported as his voice, not established facts here.
