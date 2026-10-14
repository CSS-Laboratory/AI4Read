---
id: grimmer-2022-textasdata/ch15-principles
work: grimmer-2022-textasdata
unit: Chapter 15. Principles of Measurement
pages: 275-282
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Principles of Measurement

## L0 — One line
A text measure is a deliberate compression of documents into a latent representation (a compressed quantity computed from each document) tied to a theoretical concept, and it should aim to meet five principles, which may not all be fully met in one project: clear goal, an identified (ideally public) source, explainable and reproducible coding, validation, and documented limitations.

## L1 — The gist (≤ 120 words)
The chapter asks what a good measurement from text looks like. The authors say the goal of measurement is to instantiate a concept from a theory so that it can be quantified. Measurement inevitably involves throwing away most of the information about an object such as a document. They describe most measurement as involving five steps (define, locate data, translate to a latent representation, label, validate). They give five principles for good measures: clear goals, identified and ideally public sources, explainable and reproducible coding, validation on data not used to build the measure, and honest documentation of limitations. They also advise separating discovery from measurement and developing a measure in a training sample but reporting results in a test sample. This matters because measurement links theory to evidence.

**Prerequisites:** the idea of a theory's observable implications; train/test split and overfitting; basic content analysis (human coders and codebooks).

## L2 — Key ideas (5–10 bullets)
- Measurement links a conceptual argument to the available data, and always carries testable and untestable assumptions (p. 275).
- Measurement is compression: most information about an object is discarded to keep a generalizable property. The document-to-representation map is a function (p. 276).
- Five steps: conceptualize, find data, build a latent representation, label it, validate it. This part of the book covers steps 3–5 (pp. 275–276).
- Five principles define a good measure, and the authors say they may not be fully met in any one project (pp. 278–280).
- The goal of measuring differs from the goal of prediction or retrieval. A good spam predictor need not be a good estimator of the proportion of spam (p. 278).
- The authors reject many off-the-shelf black-box measurement strategies, because in their view a measurement cannot properly be part of science if we don't know how it was generated (p. 279).
- Discovery and measurement should be separated, though the authors expect most broad research programs to iterate between them (p. 277).
- Develop the measure on training data and report results on test data, to protect against certain kinds of overfitting; the authors motivate this by the worry that analyst biases or expectations may creep into measurement (p. 281).

## L3 — Walkthrough

### Opening (pp. 275–276)
- Duncan (1984) observes that measurement grew up and was taken for granted before anyone asked how it works. The authors say text as data, being new, has renewed attention to assumptions and validation (p. 275).
- **Goal:** instantiate a concept from the hypothesis or theory so that it can be quantified. No measurement is fully divorced from theory. Measuring invokes testable and untestable assumptions about how observed data map to the concept (p. 275).
- No single approach works best everywhere (the Chapter 2 principles). Most measurement involves five steps (p. 275):
  1. Define the conceptualization.
  2. Locate data containing implications of the concept.
  3. Translate data into a latent representation.
  4. Label the representation and connect it to the concept.
  5. Validate the measure.
- Steps 1–2 were covered earlier (Discovery part; Chapter 4). This part treats steps 3–5. Measurement is needed whether the goal is description, causal inference or prediction (p. 276).
- **Compression:** measuring means discarding most information about an object to focus on a generalizable property. This is formalized as a function mapping a document to the latent representation (p. 276).

*Intuition note:* A measure is a summary on purpose. Which details you throw away decides what the measure can and cannot tell you.

### 15.1 From Concept to Measurement (p. 277)
- Discovery proposes an understanding, unsettles it with data and revises it. Measurement begins when this iteration settles down (p. 277).
- In practice the two are not always cleanly separated, often because discovery goes unreported. The authors separate them so each can use suited techniques. They expect that in most broad research programs there will be iteration between the two stages (p. 277).
- No universally best method exists. The following chapters describe approaches that use analyst information in different ways (p. 277).

### 15.2 What Makes a Good Measurement (pp. 278–280)
- A good measure simplifies the world so the analyst can describe a process or test a theory's observable implications. Its properties depend on the problem (p. 278).
- Computer and industrial data scientists have focused mainly on retrieval and prediction. Social scientists and digital humanists have almost exclusively used texts as a mechanism for measurement. Examples: culture, political agendas, support for violent jihad, international events (p. 278).
- The first computer-assisted content analysis the authors know of is Sebeok and Zeps (1958), on folktales (p. 278).
- A spam predictor will not necessarily measure well the proportion of email that is spam. In the haystack metaphor, some want to find the strand of hay and others to characterize the haystack (p. 278).
- The five criteria are demanding and may not be fully satisfied in any one paper (p. 278).

**Principle 1: clear goals.** A measure reduces the source, and no piece of information is universally right to keep. So the goal should be stated, giving clear scope and purpose. This guards against misuse, including by later scholars. Where possible the statement should be understandable to nonexperts (p. 278).

**Principle 2: identify the source, ideally make it public.** Meaning is sensitive to the context of production, so the source should always be clearly stated. Making the texts public may not always be possible, but it facilitates future work and allows independent validation (p. 279).

**Principle 3: explainable and reproducible coding.** Given the raw documents, a reader should be able to reconstruct the measure. For human coders this means a comprehensive codebook. For computer-assisted coding it means a complete description of the model or software. The "explainable" requirement means these materials should be understandable by the broadest possible audience. The authors write that a measurement "cannot properly be a part of science if we don't know how it was generated" (p. 279). This rejects many off-the-shelf black-box strategies (p. 279).

**Principle 4: validation.** Accuracy should be validated on data other than that used to develop the measure. Measures should be understandable to a broad audience. A conceptual gap between the method and the intended concept always exists, but it should be as small as possible. Validation is the process of establishing, to readers and to the researchers themselves, that the measure maps well to the concept it purports to measure (p. 279).

**Principle 5: explore, document and communicate limitations.** Some measurement error is inevitable. Its consequences depend on the intended use, so analysts should disclose when the measure performs well and when not (pp. 279–280). Measures may discriminate well across their whole range, or only at the extremes or the middle. Error rates may differ across groups, which matters for fairness (Jacobs and Wallach, 2021). Defining scope conditions supports correct use (p. 280).

*Intuition note:* The five principles let a reader check three things: what the measure is for, how it was made, and when to trust it.

- The authors draw on philosophy of science, psychometrics and other traditions. They note text as data is "in its infancy" with unique challenges. They say earlier measurement theory codified procedures found by trial and error. A full theory is beyond scope, and they offer guidance from their own trial and error (p. 280).

### 15.3 Balancing Discovery and Measurement with Sample Splits (p. 281)
- Doing conceptualization and measurement at once is difficult. Analyst bias or theoretical expectations may creep in. This is why interviewers may be blind to expectations and coders may not see outcomes. The aim is to minimize the influence of anything outside the text (p. 281).
- **King, Keohane and Verba (1994, p. 156) advise:**
  - first, use judgments made for other purposes by other researchers, since these were presumably not shaped by your hypotheses;
  - if you are the first to use the variables, let informed people code them without knowing your theory (p. 281).
- Often suitable measures do not exist. The authors then suggest a **train-test split**: develop the measure on training data and report results from the test data (p. 281).
- This protects against certain kinds of overfitting. Sample splits will also be central for causal inference (p. 281).

*Intuition note:* If you tune a measure on the same documents you report on, your expectations can shape the result. Reporting on held-out documents keeps part of the evidence untouched by your choices.

### Footnotes (pp. 281–282)
- **Stevens (1946):** measurement is assigning numbers to objects by rules. **Duncan's view:** this is incomplete, like defining piano playing as striking keys in a pattern, because it omits expressing the degree of a quality. The authors follow Duncan's purpose-driven view but endorse a slightly broader definition that includes classification (pp. 281–282).
- For documenting the purpose and limits of predictive models, including those used for measurement, see Mitchell et al. (2019) (p. 282).

## Toy example (ours, not from the text)
A mailbox has 1,000 emails, 100 of them spam (true share 10%). A classifier flags 90 of the 100 spam emails (10 missed). It also flags 90 of the 900 non-spam emails by mistake.
- Correct decisions: 90 + (900 − 90) = 90 + 810 = 900, so accuracy = 900/1000 = 90%. This looks good for prediction.
- Emails flagged: 90 + 90 = 180, so the estimated spam share is 180/1000 = 18%, against a true 10%.
- The measure is badly biased for the goal "proportion of spam" despite 90% accuracy. Each email is compressed to one 0/1 label, and the errors do not cancel.
- Following Principle 4, we would check the 18% on a test set not used to build the classifier. Following Principle 5, we would report that the share is overstated.

## Concepts
- [[text-as-data-validation]] — checking on independent data that the measure maps to the intended concept (p. 279)
- [[observable-implications]] — testable consequences of a theory that measures should be able to test (p. 278)
- [[measurement-as-compression]] (new) — measuring discards most information to keep a generalizable property, via a function from document to latent representation (p. 276)
- [[latent-representation]] (new) — the compressed quantity a document is mapped to, then labelled and linked to a concept (pp. 275–276)
- [[train-test-split]] (new) — build the measure on training data, report on test data, to guard against some overfitting (p. 281)
- [[scope-conditions]] (new) — documented conditions under which a measure performs well or badly (p. 280)

## Canonical instances
- [[spam-prediction-vs-proportion]] — good at predicting spam need not mean good at measuring its share (p. 278)
- [[haystack-metaphor]] — finding the strand versus characterizing the haystack (p. 278)
- [[stevens-duncan-measurement-definition]] — Stevens's definition, criticized by Duncan as incomplete, and the authors' broader version (pp. 281–282)
- [[kkv-blind-coding-advice]] — use others' judgments or blind coders to keep hypotheses out of measurement (p. 281)

## Bridges (candidates)
- [structural-analogy] Train-test split for measurement ↔ causal inference: both separate development from reporting (p. 281 says splits recur there).
- [structural-analogy] Blind coders and held-out test data ↔ blinding in experiments: both keep expectations from shaping the measurement.
- [metaphor] Compression ↔ lossy summarization: a measure keeps one property and discards the rest.

## Questions this raises
- What concrete validation checks show the "conceptual gap" is small enough for a given measure?
- When the goal is a proportion rather than a label, which error measures matter most?
- How can a measure be explainable and reproducible when it uses a complex model?
- How should scope conditions and group-specific error rates be documented?

## Reading notes
- Printed page = pdf page (275–282); text layer was clean, and no OCR problems were noticed.
- The supplied pages (275–282) contain no equations or exercises. Text was read from the text layer only. The title page and running headers are not in the supplied pages.
- Footnote 1 starts on p. 281 and ends on p. 282. The authors say the next several chapters cover methods (p. 276); those chapters are not covered here.
