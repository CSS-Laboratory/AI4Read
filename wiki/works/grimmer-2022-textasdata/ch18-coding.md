---
id: grimmer-2022-textasdata/ch18-coding
work: grimmer-2022-textasdata
unit: Chapter 18. Coding a Training Set
pages: 303-317
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Coding a Training Set

## L0 — One line
A training set of labelled documents can come from trained human coders, a crowd, or found data; hand coding rests on a final codebook and reliability checks, crowd labels must be reconciled, and found data demands careful validation.

## L1 — The gist (≤ 120 words)
How should a researcher create the labelled documents that train and validate a classifier? The authors describe three routes. Hand coding uses a codebook, separate coders, a representative sample and intercoder reliability checks. Crowdsourcing scales fast but suits only simple, easily explained tasks and must reconcile conflicting labels. Supervision with found data reuses labels made by others, which can be cheap but can bias measures in unpredictable directions. For hand coding, the codebook should be finalised on a development set and applied to fresh documents. Intercoder reliability does not guarantee accuracy, and found-data labels demand careful validation. Examples: Boydstun's news coding and Nielsen's Jihad Score.

**Prerequisites:** supervised classification (labels → classifier); sampling and representativeness; the idea of a latent dimension.

## L2 — Key ideas (5–10 bullets)
- Human coding is a mapping from text to categories, made of codebook, training and coders' own judgment. It is slow but useful for small datasets and complex concepts (p. 303).
- Write a concise codebook, revise it in an exploratory phase, and apply the "final" version to separate documents to avoid overfitting the development set (pp. 303–304).
- Neuendorf's criteria for a good training set: objectivity/intersubjectivity, a priori design, reliability, validity, generalizability, replicability (p. 305).
- Hand-coding steps: choose codebook, coders other than the researcher (at least two), a representative sample, trained and independent coders, and a reliability check. Watch for coder drift and data drift (pp. 306–308).
- Boydstun hand-coded 31,034 front-page NYT articles with an adapted codebook and found coverage highly skewed toward international affairs and often driven by events (pp. 308–309).
- Crowdsourcing differs in three ways: lower fixed costs and so less feasible intensive training, fast scaling, and unavoidable annotation error. The key is splitting tasks into small pieces, such as pairwise comparisons (pp. 310–314).
- Supervision with found data (Nielsen) can be cheap and can use expert labels. But the labels come from an unknown process and the sample is non-random, so careful validation is required (pp. 315–316).

## L3 — Walkthrough

### Introduction (pp. 303–304)
- Human coding means putting documents into researcher-defined categories by hand. It is still useful alone for small datasets and complex concepts. It also often forms the basis of training and validation sets for statistical classifiers (p. 303).
- It provides a mapping from text to categories. The mapping is the codebook (the coders' instruction manual) plus coder training plus coders' internal thought processes. In comparison with statistical classification, humans can use substantive and background knowledge to fill gaps in the coding scheme from the context (p. 303).
- Coding is hard even for experts, because of ambiguous language, limited attention and nuanced concepts (p. 303). Schrodt (2006), describing the collection of events data, put the modal manual content-analysis project colorfully as "legions of bored students flipping through copies of The New York Times" (p. 303).
- Because language is contextual, a full codebook is hard to write ex ante. The authors recommend an exploratory phase. A preliminary concise codebook is applied to an initial set, ambiguities and overlooked categories surface, and the codebook is revised (pp. 303–304).
- Only after coders apply it without noticing substantial ambiguities is a "final" scheme ready for a separate analysis set. This addresses ambiguity without overfitting to the development documents (p. 304).
- The chapter covers codebooks, coders, coding, crowdsourcing and found data. It points to Krippendorff (2012), Neuendorf (2016), Riffe et al. (2019) and Barberá et al. (2021) for more detail (p. 304).

### 18.1 Characteristics of a good training set (p. 305)
Following Neuendorf (2016), the goal is a reliable human mapping that operationalizes concepts found earlier (p. 305).
- **Objectivity-intersubjectivity:** understanding of categories is not person-specific. If objectivity is unattainable, at least a shared understanding among researchers is needed.
- **A priori design:** categories may be refined during coding, but the final training set rests on a final codebook and fresh data.
- **Reliability:** independent coders produce the same mapping.
- **Validity:** the measure reflects the concept, and the label matches what is measured.
- **Generalizability:** the coded sample's mapping should carry over to the whole dataset and target population.
- **Replicability:** the measure can be reproduced on the same data, and ideally on other data and contexts.

### 18.2 Hand coding (pp. 306–309)
Hand coding can range from very straightforward to a process of weeks, months or even years (p. 306).

**18.2.1 Codebook.** The codebook defines the categories and must communicate them well, to secure reliability, validity and replicability. It may include example texts, edge cases and flowcharts for hierarchies. An existing codebook can be adapted, since it has often been refined through several rounds of testing. The Comparative Manifestos Project is an example (p. 306).

**18.2.2 Coders.** Coders other than the researcher should label the data. This tests whether the researcher can communicate the categories. Best practice is at least two coders, so agreement can be measured as reliability. Experienced coders may need only two. Less trained or less attentive pools may need many evaluations per document (pp. 306–307). Funding or access to experts may make separate coders impossible (fn. 3, p. 317).

**18.2.3 Documents.** For generalizability, the training set should represent the larger dataset and the target population. A simple random sample is one way to achieve this. Needed size rises with the number of categories and falls with coder reliability. Downstream validation can reveal whether enough was coded (p. 307).

**18.2.4 Managing coders.** Train coders: they read the codebook, ask questions, and label a sample so the researcher can check understanding or revise instructions. Final labelling happens after the last codebook revision, with no contact between coders and no outside resources, so reliability can be evaluated (p. 307).

**18.2.5 Reliability.** Compare labels on the same documents across coders, using for example Cohen's kappa or Krippendorff's alpha (formulas not given in this unit) (pp. 307–308). Intercoder reliability does not guarantee accuracy, because coders may share the same errors. Without "true" labels accuracy is hard to assess (fn. 4, p. 317).

**18.2.6 Drift.** Two kinds are distinguished (p. 308).
- *Coder drift:* coders change how they assign labels through fatigue or new insights. It might be useful to assess reliability at several points.
- *Data drift:* the content stream evolves, so categories may emerge, collapse or merge. If the codebook changes, new and old data may be labelled differently. One final coding round can help assess the new codebook's reliability.

**18.2.7 Example: Making the News (pp. 308–309).**
- Boydstun (2013) argues that media are neither pure watchdogs nor pure alarms. She proposes an alarm/patrol hybrid: many issue areas are monitored, but disproportionate resources go to a few "hot" ones (p. 308).
- Data: 31,034 *New York Times* articles, limited to the front page. Her codebook is the Policy Agendas Project codebook, annotated with more explicit instructions. It has 27 major topics and 225 subtopics (p. 308).
- Coders were trained on a sample and had to reach high reliability before coding the rest. Duplicate texts were coded throughout to monitor reliability over time. She reports alpha and kappa and posts the codebook online (pp. 308–309).
- Finding: issue coverage is highly skewed toward international affairs and often event-driven. After the September 2001 attacks, front-page coverage shifted drastically to defense, crowding out other areas (p. 309; Fig. 18.1, p. 313).

*Intuition note:* A codebook is a measuring instrument, and it must be tested before the real measurement. Revising on one set and coding on a fresh set keeps the instrument from being tuned to the data it will measure.

### 18.3 Crowdsourcing (pp. 310–314)
- Online labor markets such as Mechanical Turk give access to untrained or lightly trained workers at large scale. They suit tasks that are easy to explain, straightforward and quick (p. 310).
- The pool is smaller than it seems. One estimate is under 200,000 unique workers, with about 2,000–5,000 active at a time (Difallah et al., 2018). Workers are demographically and politically skewed, though less so than university students (Huff and Tingley, 2015) (p. 310).
- **Three differences from a small coder team** (p. 310):
  1. Fixed costs have to be lower, so intensive training is less feasible, which limits the work to comparatively simple tasks.
  2. Scaling up is fast: thousands of annotations in hours.
  3. Error must be accepted as inevitable, so conflicting labels need reconciling. The authors cite methods such as Dawid and Skene (1979) and return to them in Chapter 20 (pp. 310–311).
- **Cost (a view held by "some"):** a fourth difference is that crowdsourcing is cheaper. The authors say annotations *can* be cheaper but question whether they should be. Workers are often paid effectively below local minimum wage. They are humans, so ethical compensation concerns apply (p. 313).
- **Changing the task.** Crowdsourcing works by splitting coding into small "bite-sized" chunks (p. 313). Carlson and Montgomery (2017) place documents on a scale using thousands of quick pairwise comparisons (p. 313).
- Absolute ratings, such as how dark a grey is, are quite difficult without some reference point. A comparison between two items is easy to judge reliably. Fig. 18.2 contrasts absolute ratings of 65 and 70 on a 100-point scale with a direct comparison of the two (pp. 313–314).
- Pairwise judgments can recover an underlying latent dimension, an idea in psychometrics since at least Thurstone (1927) (p. 314).
- Carlson and Montgomery find the system highly reliable and favourable against other approaches. Coders seem to need considerably less training for pairwise judgments. The evaluations needed scale with the square of the number of texts, so the approach works best with a moderate number of documents. The largest case is under 2,000 (p. 314).
- The task is not fully supervised, because no unit is labelled with a "true" value. It is a middle ground between supervised and unsupervised measurement. The learned dimension needs checking that it has the intended meaning (p. 314).

*Intuition note:* Crowds suit many small, easily explained judgments; tasks that need expert background or intensive training fit them less well. Redesigning the task, for example from "rate this" to "which is more?", fits the work to the crowd.

### 18.4 Supervision with found data (pp. 315–316)
- This route uses existing categories made by people outside the research team as the training set (p. 315).
- **Example (Nielsen, 2017):** He studies why some Muslim clerics express support for violent jihad. He collects a census of clerics on the web and builds a "Jihad Score". The average cleric wrote 523 documents, so human coding even of a small random sample of clerics is very time consuming (p. 315).
- Instead he uses "The Jihadist's Bookbag", documents chosen by jihadists on web forums as an introduction to jihadist ideology, so he need not impose his own definition. He pairs it with a curated sample of known non-jihadist clerics' documents. This labelled set trains the classifier (p. 315).
- **Possible benefits:** it can be low-cost and can give labels from true experts (p. 315).
- **Risks:** measures can be biased in unpredictable directions, for at least two reasons (p. 315).
  1. The labels come from an unknown process. The analyst must ensure the documents reflect the intended categories.
  2. Even if the labels match what the analyst would assign, the documents were selected non-randomly. Estimated word probabilities given the latent category are then unlikely to be accurate. This is especially true when extreme cases are chosen, whose language may be distinct.
- Nielsen offers eight validations (reviewed in Chapter 20). The authors say this approach isn't a random sample but may work well in practice. It demands careful validation (pp. 315–316).

### 18.5 Conclusion (p. 317)
The chapter covers good training-set characteristics, the human-coding process, and the pros and cons of crowdsourcing and found data. Chapter 19 uses the training data for supervised learning (p. 317).

## Toy example
*(Ours, not from the text.)* Ten documents have true labels A (d1–d5) and B (d6–d10). Assume we could see the truth, which in practice we cannot.
- Coder 1 labels: d1=B, d2=A, d3=A, d4=A, d5=B, d6=A, d7–d10=B.
- Coder 2 labels: d1=A, d2=A, d3=A, d4=A, d5=B, d6=A, d7–d10=B.
- They differ only on d1, so agreement = 9/10 = 90%.
- Coder 1 is wrong on d1, d5 and d6, so accuracy = 7/10 = 70%. Coder 2 is wrong on d5 and d6, so accuracy = 8/10 = 80%.
- Both made the same mistakes on d5 and d6. High agreement therefore coexists with lower accuracy, which is the point of footnote 4 (p. 317).

## Concepts
- [[human-coding]] (new) — manual assignment of documents to categories via codebook, training and coder judgment (p. 303)
- [[codebook]] (new) — written instructions defining categories, with examples and edge cases (p. 306)
- [[training-set]] (new) — labelled documents used to train or validate a classifier (p. 303)
- [[intercoder-reliability]] (new) — agreement between independent coders on the same documents. It does not guarantee accuracy (pp. 307, 317)
- [[coder-and-data-drift]] (new) — coders' labelling changing over time, or the data stream evolving (p. 308)
- [[crowdsourcing-annotation]] (new) — labels from many lightly trained online workers; errors must be reconciled (p. 310)
- [[pairwise-comparison-scaling]] (new) — recovering a latent scale from many "which is more?" judgments (p. 314)
- [[supervision-with-found-data]] (new) — using labels made by others as the training set. Needs validation (p. 315)
- [[text as data / validation]] — downstream validation can help reveal whether enough documents were coded (p. 307); found-data labels demand careful validation (p. 316)

## Canonical instances
- [[boydstun-making-the-news]] — hand-coding 31,034 NYT front-page articles with an adapted Policy Agendas codebook (pp. 308–309)
- [[carlson-montgomery-pairwise]] — crowd pairwise comparisons used to scale documents (pp. 313–314)
- [[nielsen-jihad-score]] — found data ("Jihadist's Bookbag") used to train a classifier for cleric radicalization (p. 315)

## Bridges (candidates)
- [structural-analogy] Final codebook applied to fresh documents ↔ held-out test data: avoids tuning to the development set (the text names overfitting, p. 304).
- [structural-analogy] Non-random found-data labels ↔ sample selection bias: word probabilities estimated on selected cases are unlikely to be accurate (p. 315).
- [structural-analogy] Pairwise comparisons recovering a latent dimension ↔ psychometric scaling (Thurstone, p. 314).

## Questions this raises
- How does one reconcile conflicting crowd labels? (The text defers this to Chapter 20.)
- How can one judge whether a pairwise-derived dimension means what was intended?
- How many coded documents suffice for a given number of categories and coder reliability?
- How can bias from non-random found data be checked beyond Nielsen's eight validations?

## Reading notes
- Printed page = pdf page.
- pdf 311 has only text; pdf 312 shows only the number "312". The Figure 18.1 image was not in the pages provided; only its caption is on p. 313. Figure 18.2 (p. 313) was checked in the image.
- The unit gives no formulas for kappa or alpha.
- Misprint on p. 310: "Mechnical Turk".
