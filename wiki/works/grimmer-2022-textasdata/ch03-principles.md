---
id: grimmer-2022-textasdata/ch03-principles
work: grimmer-2022-textasdata
unit: Chapter 3. Principles of Selection and Representation
pages: 72-82
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Principles of Selection and Representation

## L0 — One line
The corpus and the numerical representation of text should both be chosen for the specific research question, ; there is no single "right" representation, and the representation should be checked by external validation.

## L1 — The gist (≤ 120 words)
How should a researcher choose which documents to collect (the corpus) and how to turn them into numbers (the representation)? The authors give four principles: build the corpus for the question; recognise that corpus construction is never values-free (representation, harmful language, privacy); no representation is right for all questions, so use the simplest one that carries enough information; and validate it against external evidence. The chapter ends by introducing two running examples: State of the Union addresses and the Mosteller–Wallace study of the Federalist Papers. The Federalist case shows how a question (who wrote the disputed papers?) can make ordinary "filler words" the most informative data.

**Prerequisites:** sampling from a population; the idea of measuring a social quantity with a number (e.g. GDP); basic classification by comparing rates.

## L2 — Key ideas (5–10 bullets)
- Collecting a corpus is like sampling from a population, and representing text is like using a metric such as GDP; both simplify a complex phenomenon into numbers (p. 72).
- Whether a corpus is useful depends on the question and population. When the question is well defined, state the quantity and population of interest first; incomplete corpora can still be used if the incompleteness is understood and reported (p. 74).
- Corpus construction is not values-free. It raises issues of who is represented, harmful language, and privacy (pp. 75–76).
- A corpus may not reflect the population equitably, and text represents language as its authors use it, not neutrally. Researchers often end up focusing on the people who produce documents (p. 75).
- There is no single right representation. Choose the simplest one that contains enough information; if unsure, use many features and let a model select (p. 77).
- Validate against hand-coded data and known facts (measurement), accuracy (prediction), or replication (causal inference) (p. 78).
- The authors do not require robustness across all representations when one clearly dominates (p. 78).
- Mosteller and Wallace's filler-word counts are a simple bag-of-words case (each document is represented by counts of chosen words): representation depends entirely on the question (p. 81).

## L3 — Walkthrough

**Introduction (pp. 72–73).** Text reflects social interactions, economic transactions and political processes. The researcher must curate a corpus and then represent it numerically (p. 72). Not all information in text is useful, so the task is to decide what to keep. Theory often cannot pick the best representation, so extensive validation is needed (p. 72). The goal is not one correct model of language. Social scientists study the processes reflected in the text, not the text itself (p. 72). The chapter builds four principles on Chapter 2's six principles (p. 72).

**3.1 Principle 1: Question-specific corpus construction (p. 74).**
- Usefulness depends on the question and population. Example: Twitter might not be the most accurate way to gauge US opinion on climate change, because only a minority use the platform and few of them tweet about climate. It may be useful for studying how officials interact with constituents or how activists try to shift the conversation (p. 74).
- When the question is well defined, state the quantities and population first. Then judge whether the corpus reflects that population and whether the quantities can be measured from the text (p. 74).
- Biased or incomplete corpora need not always be discarded, if the sources and consequences of incompleteness are understood and communicated (p. 74).
- If the question is not yet defined (exploration, treated in the Discovery part), explore with quantitative analysis plus close reading. Then revisit corpus selection and collect new data once the question is settled (p. 74).

*Intuition note:* Ask who the documents come from and whether they can tell you what you want to know. A corpus can be fine for one question and poor for another.

**3.2 Principle 2: No values-free corpus construction (pp. 75–76).**
- *Representation.* Corpora may misrepresent the population because individuals differ in resources and incentives to write and publish. Institutions and governments may skew retention and availability; internet censorship is an extreme case (p. 75). Researchers then tend to focus on the document-producing population. Inequitable coverage can bias conclusions and make models less accurate for subgroups (p. 75).
- *Harmful language.* Corpora reflect authors' language, including stereotypes and hate speech. Sometimes finding such language is the task. In predictive language models, including it in training data can perpetuate the problem downstream. Data are not the only cause, but can be an important part of the process (p. 75).
- *Privacy, research-generated text* (e.g. open-ended survey answers): follow standard procedures for consent, removing obvious identifiers, and protecting subjects. This is especially pressing when text is merged with other sensitive data, because it is hard to know which details identify someone (p. 75). The authors cite Lundberg et al. (2019) for a privacy threat analysis (p. 75).
- *Privacy, public sources.* More frequently, documents come from public sources and were not written for research, often with no simple way to obtain informed consent. Many researchers argue that publishing implies permission, but the public/private split may oversimplify privacy in the social media age (p. 76). Nissenbaum's "contextual integrity" asks about the norms under which authors expected access. Semi-public settings (closed groups, sign-up mailing lists) are harder still (p. 76).

*Intuition note:* Choosing documents is choosing whose voices count and whose privacy is at risk. Both decisions have ethical consequences.

**3.3 Principle 3: No right way to represent text (p. 77).**
- Representation, like the corpus, depends on the question. Options include an indicator for a single word; indicators for most words minus common words such as *the* and *and*; only the common words; or information on how words relate to each other and their context (p. 77).
- Advice: choose the simplest representation that contains sufficient information about what is to be measured. Ask what quantity is measured and how the phenomenon might show up in text (p. 77).
- If the best representation is unknown, use many features and let a model extract the most important ones for the measure of interest (p. 77).

*Intuition note:* Start with the question, then ask what minimal numbers from the text would carry the answer. A more complicated representation may be needed when the simple one does not capture the quantity.

**3.4 Principle 4: Validation (p. 78).**
- In many cases there are too many representation choices to enumerate. The authors rely on validation (p. 78).
- A representation works in a **measurement model** if the measures align with validated hand-coded data and known facts. It works in a **prediction model** if accuracy is high. It works in **causal inference** if the experiment can be replicated with the same results (p. 78).
- If validation fails, revisit both representation and model (p. 78).
- The authors do not believe findings must be robust across many representations, as is common in other social science. Representations suit different tasks, and robustness checks are unnecessary if one representation clearly dominates. Instead, use external validation to find the best representation and ignore the less useful ones (p. 78).

*Intuition note:* A representation is judged by external checks: agreement with trusted hand-coded data and known facts, accuracy, or replication. The authors do not require results to survive every alternative representation.

**3.5 State of the Union addresses (p. 79).** The corpus has 236 addresses, 1790–2016, written or spoken, and gives a snapshot of executive-branch priorities (p. 79). Rule, Cointet and Bearman (2015) argue that discourse shifted after 1917: "Statecraft" and "Political Economy" morphed into "Foreign Affairs" and "Public Policy" (p. 79). Benoit, Munger and Spirling (2019) find that textual complexity decreased substantially over time. Written speeches are much more complex than spoken ones in the same year, so more spoken delivery might explain some of the decline (p. 79).

**3.6 Authorship of the Federalist Papers (pp. 80–81).**
- *Setting.* There are 85 papers by Hamilton, Jay and Madison supporting the Constitution; the first 77 were published anonymously in New York newspapers, 1787–88 (p. 80). The text gives 73 as uncontested, 12 as believed to be by Hamilton or Madison, and 3 as joint with disputed sections. Hamilton's list (given two days before his death in a duel, 1804) and Madison's list (1818) conflict (p. 80).
- *Method.* Mosteller and Wallace aimed to separate the authors by style, not content. The two authors use "filler words" (*upon*, *by*, *to*) at different rates in known documents (p. 80). They split texts into blocks of about 200 words, to allow for joint authorship, and counted filler words per block (p. 80). Counting in 1959–60 was manual, with words cut into paper slips ("slips of paper would fly about the room", p. 81).
- *Model.* Trained on known documents, the model asks whether a 200-word passage's filler-word rates look more like known Hamilton or known Madison text (p. 81). It attributed all 12 unknown-authorship documents to Madison, "quite decisively" (p. 81).
- *Lesson.* It is a simple bag of words: each document is represented by counts of words of interest. For many social science questions the rate of *upon* is useless, but here filler words matter most. Representation depends entirely on the question (p. 81).

**3.7 Conclusion (p. 82).** The principles parallel Chapter 2: question-specific corpora, abandoning a single right representation, and focusing on validation. Chapter 4 covers selecting documents; Chapter 5 the first representation algorithm (p. 82).

## Toy example (ours, not from the text; numbers invented)
Suppose known author A uses *upon* at 6 per 1,000 words and known author B at 1 per 1,000. A 200-word block contains 1 *upon*.
- Block rate = 1 / 200 = 0.005 = 5 per 1,000.
- Distance to A = |5 − 6| = 1; distance to B = |5 − 1| = 4.
- The block looks more like A.

This is only a crude illustration of "compare filler-word rates to known authors". It is not Mosteller and Wallace's actual model. The point is that the bag-of-words representation (here, one count) is chosen because the question is authorship.

## Concepts
- [[text-as-data-validation]] — check a text representation against hand-coded data, known facts, accuracy or replication (p. 78)
- [[question-specific-corpus]] (new) — a corpus judged by whether it reflects the population and quantities of interest (p. 74)
- [[corpus-as-sample]] (new) — collecting a corpus is like sampling from a population of interest (p. 72)
- [[values-laden-corpus-construction]] (new) — document selection has ethical consequences: representation, harmful language, privacy (p. 75)
- [[contextual-integrity]] (new) — privacy judged by the norms under which authors expected their text to be accessed, not only public/private (p. 76)
- [[bag-of-words]] (new) — a document represented by counts of individual words of interest (p. 81)
- [[filler-words]] (new) — words like *upon*, *by*, *to* whose rates distinguish authors' style (p. 80)
- [[simplest-sufficient-representation]] (new) — choose the simplest representation with enough information for the quantity measured (p. 77)

## Canonical instances
- [[sotu-corpus]] (new) — 236 State of the Union addresses, 1790–2016; used for shifts in discourse and falling complexity (p. 79)
- [[federalist-papers-authorship]] (new) — Mosteller and Wallace's filler-word model attributing the 12 disputed papers to Madison (pp. 80–81)
- [[twitter-climate-opinion]] (new) — Twitter as possibly not the most accurate source for US climate opinion but a possibly useful one for studying officials' online interaction (p. 74)

## Bridges (candidates)
- [structural-analogy] Corpus choice ↔ survey sampling: a corpus is analogous to a sample from a population of interest (p. 72); the population should be defined before collecting (p. 74)
- [structural-analogy] Text representation ↔ measurement of GDP: a number standing in for a complex phenomenon (p. 72)
- [metaphor] Contextual integrity ↔ research ethics: expectations of the context in which information was shared

## Questions this raises
- How can a researcher tell when one representation "clearly dominates" the others, and is that judgment itself validated?
- When a corpus over-represents document producers, which corrections or disclosures make it usable?
- Is validating against hand-coded data always possible when no ground truth exists, as in exploratory work?
- What does the Federalist result imply about using style versus content features for measurement?

## Reading notes
- Printed page = pdf page (offset 0). pdf 73 holds only one continuing line of text plus a page number.
- Counts of Federalist papers as printed (73 uncontested + 12 + 3 = 88) exceed the stated total of 85. I did not resolve this; the digest repeats the author's figures.
- Footnote 2 (p. 82) gives Mosteller's recollection of the 1941 conversation that started the authorship question; the digest does not use its details.
- The chapter has no equations or exercises.
