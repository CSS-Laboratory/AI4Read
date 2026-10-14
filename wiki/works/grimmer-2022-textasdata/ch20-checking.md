---
id: grimmer-2022-textasdata/ch20-checking
work: grimmer-2022-textasdata
unit: Chapter 20. Checking Performance
pages: 337-349
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
# Checking Performance

## L0 — One line
A text measure earns trust by surviving, again and again, tests it would probably fail if it were wrong, using held-out gold-standard labels where they exist and varied external checks where they do not.

## L1 — The gist (≤ 120 words)
How can we know that a text-based measure captures the concept we care about, and does so outside the data used to build it? The chapter's answer is a single principle: expose the measure to tests it is likely to pass only if it works, and repeat the checks over time. With gold-standard labels, hold out a validation set, summarize a confusion matrix, and use cross-validation. Without them, use surrogate labels, partial category replication, nonexpert human judgments, and hypotheses about external information. Nielsen's (2017) eight-part validation of a jihad scale shows such a package in practice. No amount of validation gives complete assurance; the level of effort should fit the setting.

**Prerequisites:** supervised classification; train/test split; proportions and correlation; the idea of overfitting. Terms used above: gold-standard labels = trusted, correctly coded labels; validation set = labeled data held out from fitting; confusion matrix, precision/recall, cross-validation and surrogate labels are defined in L3.

## L2 — Key ideas (5–10 bullets)
- Validation means checking that a measure reflects the intended concept and that observations are correctly placed on it. It rests on vulnerability to being proven wrong, and it should be an ongoing loop (p. 337).
- A confusion matrix, built on a held-out validation set, is summarized by accuracy (share classified correctly), precision (share of documents put in a category that truly belong there) and recall (share of a category's true documents that are found) (pp. 338–339).
- The right metric depends on the task. Spam filtering favours precision. Estimating category proportions cares about bias in the proportion (p. 339).
- Cross-validation reduces overfitting to one validation set. It estimates error accurately only if the gold-standard documents are a random sample from the population of interest (p. 340).
- Gold-standard labels may themselves be flawed, so check intercoder reliability first. The authors strongly recommend re-checking performance regularly, because data can change (p. 340).
- Without gold-standard data, the burden of human effort shifts to validation. Surrogate labels help but can mislead: they may tell us only about extremes or be nonrandom (pp. 342–343).
- Other tools: partial category replication, nonexpert evaluations, and hypothesis validity from pre-specified external relationships (pp. 343–344).
- Nielsen's jihad scale shows a combined, case-specific validation, matched to how central the scores are to his argument (pp. 345–348).

## L3 — Walkthrough

### Introduction (p. 337)
- Measurement compresses data into categories or a continuous value. It is one operationalization of a concept (turning a concept into something measurable).
- Validation checks that the compression reflects the concept and that we understand what was kept and discarded. It also checks performance on data beyond the training data.
- There is no single organizing framework. The unifying principle is vulnerability to being proven wrong.
- No validation gives complete assurance. Different settings need different levels of validation. The authors stress an evaluation loop: validate and update at regular intervals, also after deployment.
- Measurement implicitly assumes concept homogeneity: two observations with the same value are equivalent on the conceptual dimension. Validation asks whether the dimension captures the theoretical concept and whether observations are placed correctly on it.

### 20.1 Validation with gold-standard data (p. 338)
- Canonical setting: mutually exclusive and exhaustive categories; randomly sampled gold-standard labeled documents; unlabeled documents to measure; and a classifier that extrapolates from labels. "Gold-standard" means labels are correct and perfectly reflect the concept.

**20.1.1 Validation set (pp. 338–339).**
- Do not fit on all labeled data. Split it into train and validation sets, and evaluate on the held-out validation set.
- Confusion matrix (Table 20.1): $K\times K$ cross-tabulation, rows = predictions, columns = gold-standard codes. $N_{12}$ counts documents the machine coded 1 and the gold standard labeled 2. Large diagonal cells indicate good performance (p. 339).
- Summaries (p. 339):
$$\text{Accuracy}=\frac{N_{11}+N_{22}+N_{33}+N_{44}}{N};\quad \text{Precision}_k=\frac{N_{kk}}{\sum_{k'=1}^{K}N_{kk'}};\quad \text{Recall}_k=\frac{N_{kk}}{\sum_{k'=1}^{K}N_{k'k}}$$
  Precision$_k$ divides by the number classified into $k$; recall$_k$ divides by the number of gold-standard documents in $k$.
- The choice depends on the quantity of interest. Spam filter: putting an important message in the spam folder costs more than letting spam into the inbox, so precision of the spam class should come before recall.
- Many social-science tasks "characterize the haystack": they estimate a category's proportion in a stratum (e.g., time period or author), with roughly equal weight on different errors. Then bias in the proportion matters more than document-level accuracy, precision or recall.

*Intuition note:* (our gloss, not stated in the text) A classifier can be wrong on many individual documents and still give a good proportion estimate if its errors roughly offset each other, as in the toy example below. The source's point is that which metric matters depends on the quantity of interest.

**20.1.2 Cross-validation (pp. 339–340).**
- Validation is iterative (fit, check, tune, refit). If we use only one validation set in these settings, the procedure will likely overfit to it.
- $V$-fold cross-validation: randomly partition the training set into $V$ groups. For each group $v$, train on the other $V-1$ groups and assess on group $v$. This gives $V$ performance measures, which are averaged.
- Benefits: it avoids overfitting by focusing on out-of-sample prediction, and it selects the best model from the candidates (the Oracle property). This holds only when all steps, including predictor selection, are done within the training folds, not on the full labeled data (fn. 2, p. 349).
- Caveat: the error estimate is accurate only if the gold-standard documents are a random sample from the population of interest. Example: classifying news posts today from 1993 posts. Under conceptual drift or other change in the data-generating process, error estimates fail even with good cross-validated performance.

**20.1.3 Importance of gold-standard data (p. 340).** Human coding is often treated as gold standard but can suffer from misinterpretation, complicated categories, or poorly trained coders. Check intercoder reliability (Chapter 18) before validating the classifier, which assumes correct labels.

**20.1.4 Ongoing evaluation (pp. 340–341).** For long-running projects, build habitual re-evaluation into maintenance. Example: a Twitter sentiment classifier, where both language and the user population change, which the original accuracy estimate does not account for.

*Intuition note:* A validation score describes the data it was computed on. If the world changes, the score may no longer apply.

### 20.2 Validation without gold-standard data (p. 342)
- Reasons for lacking gold-standard data: known coding errors, found data, or dictionary methods. This shifts the burden of human effort from labeling to validation. The approaches below are neither exclusive nor exhaustive and should be tailored.

**20.2.1 Surrogate labels (pp. 342–343).**
- Surrogate labels approximate gold standard; this often falls under convergent validity (the measure accords with other relevant measures). Example: compare article subject codes with the newspaper section or an online tag.
- Risk 1: they tend to inform us only about extreme cases. Goertz's (2008) "gray zone" is a range of intermediate scale points that are not really distinguished. Example (Polity, −10 to +10): keep only the extreme values (−10 and +10), which are 23% of the data, replace all others with random uniform draws, and the result correlates at .5 with the original measure. So we may think a measure discriminates along the whole dimension when it only separates two extremes.
- Risk 2: surrogate labels are often nonrandomly selected, as found data or because a rare category would need very many random samples. Evaluation designs exist for this purpose (King and Lowe, 2003).

**20.2.2 Partial category replication (p. 343).** With 100+ categories, often only a subset matters. Write a codebook for those categories, group the rest into "other", and do standard supervised learning and validation. Grimmer (2013a) used this to show ReadMe captures aggregate categories of legislative credit claiming.

**20.2.3 Nonexpert human evaluation (p. 343).** Examples: insert an intruder text from another category and ask evaluators to spot it (Chang et al., 2009); ask coders to label a category from its most distinctive words (semantic validity); cluster-quality evaluations (Grimmer and King, 2011); pairwise comparisons and ranking tasks.

**20.2.4 Correspondence to external information (p. 344).** If expected relationships are specified beforehand, we can test hypothesis validity. Examples: House floor speech should swing with major news events; Senate committee chairs should talk more about their committee's issues. Choose hypotheses so that failure to see the relationship is very unlikely unless the measure is poor. This creates a paradox: researchers show expected relationships, then report an unexpected one as the key finding.

### 20.3 Example: validating jihad scores (pp. 345–348)
Nielsen (2017, Ch. 5) uses eight validations. Scaling was partly motivated by the lack of gold-standard data. Many validations are paired with close reading (p. 345).
1. **Representativeness of the labeled documents.** The scale is anchored by "found data," The Jihadist's Bookbag, which was not annotated for this purpose. He runs LDA with $K=5$, shows the top five FREX words per topic and titles of the three documents most prominent in each topic, and clusters authors by topic use. He concludes the documents reflect his conception of jihadist ideology (p. 345).
2. **Alternate dataset.** A new scaling using the library "Pulpit of Monotheism and Jihad" (earlier rejected as ideologically too broad) gives qualitatively similar findings (p. 345).
3. **Word weights.** The scoring is transparent, so he checks the weights look reasonable on their face and visualizes the translated results (Figure 19.1) (p. 346).
4. **Known individuals.** He shows the score distribution and places key clerics on it (Figure 20.1), explaining why placements are reasonable. He checks all clerics at the extreme end and confirms they are extreme jihadists (p. 346).
5–8. **External sources:** cleric biographies; al-Zawahiri's list of al-Qaeda supporters; three jihadist websites listing allies and rejected clerics; counter-terrorism specialists' assessments (McCants et al., 2006). The scores predict the classifications in each. Errors are explained and judged unlikely to threaten validity (p. 347).
- Together these show the training data reflect the concept and the scores predict and agree with lists of jihadist clerics. The validation takes 20 pages, six figures and two tables, which the authors consider warranted because the scores are core to the argument (pp. 347–348).

### 20.4 Conclusion (p. 349)
Hold out a validation set, report accuracy, precision and recall, and use cross-validation. Without gold-standard data, using Nielsen (2017) as the example, surrogate labels, checking word weights for semantic validity, and close reading can also test the measure.

## Toy example (ours, not from the text)
Three categories, $N=100$ validation documents. Rows = machine, columns = human:

| | H1 | H2 | H3 | Row sum |
|---|---|---|---|---|
| M1 | 30 | 5 | 5 | 40 |
| M2 | 10 | 25 | 5 | 40 |
| M3 | 0 | 5 | 15 | 20 |
| Col sum | 40 | 35 | 25 | 100 |

- Accuracy $=(30+25+15)/100=0.70$.
- Precision$_1=30/40=0.75$; Recall$_1=30/40=0.75$.
- Precision$_2=25/40=0.625$; Recall$_2=25/35\approx0.714$.
- Precision$_3=15/20=0.75$; Recall$_3=15/25=0.60$.
- Proportions (machine vs gold): category 1, 40% vs 40% (no bias despite 20 document-level errors involving it); category 2, 40% vs 35% (+5 points); category 3, 20% vs 25% (−5 points).

This shows that document-level accuracy and bias in category proportions are different questions.

## Concepts
- [[text as data / validation]] — checking that a text measure reflects the concept and works out of sample; it rests on being exposed to failure (p. 337)
- [[concept-homogeneity]] (new) — observations with the same measured value are equivalent on the conceptual dimension (p. 337)
- [[confusion-matrix]] (new) — $K\times K$ table of predicted (rows) vs gold-standard (columns) classes (p. 338)
- [[precision-recall-accuracy]] (new) — summaries of the confusion matrix; the choice depends on the quantity of interest (p. 339)
- [[cross-validation]] (new) — $V$-fold out-of-sample assessment; accurate only if the labeled sample is random from the population (p. 340)
- [[conceptual-drift]] (new) — change in the data-generating process that makes old error estimates inaccurate (p. 340)
- [[surrogate-labels]] (new) — approximate external labels used for convergent validity (p. 342)
- [[gray-zone]] (new) — intermediate scale points not really distinguished (Goertz) (p. 342)
- [[hypothesis-validity]] (new) — a measure shows pre-specified relationships with external information (p. 344)

## Canonical instances
- [[spam-filter-precision]] — a case where precision outweighs recall (p. 339)
- [[polity-gray-zone]] — extremes plus random draws still correlate at .5 (pp. 342–343)
- [[nielsen-jihad-scale-validation]] — eight-part validation without gold-standard data (pp. 345–348)
- [[readme-credit-claiming]] — partial category replication (Grimmer 2013a) (p. 343)

## Bridges (candidates)
- [structural-analogy] Hypothesis validity ↔ observable implications: both test a measure or theory through varied, pre-specified consequences that would be unlikely if it were wrong.
- [structural-analogy] Conceptual drift ↔ machine learning: distribution shift — in both, a model fitted to old data is judged on data from a changed process (the text names only conceptual drift).
- [metaphor] Evaluation loop ↔ institutional feedback (exit/voice): ongoing checks as a feedback channel on a measurement system.

## Questions this raises
- How should one choose between document-level metrics and proportion bias when the target is a time series of category shares?
- How can researchers detect conceptual drift early, before error estimates fail?
- How many surrogate or external checks are enough, and who decides what level of validation a given application needs?
- How should rare categories be evaluated efficiently (King and Lowe, 2003)?

## Reading notes
- Printed pages equal pdf pages (337–349).
- The accuracy/precision/recall formula line is garbled in the text layer. The formulas above were reconstructed from the page image, which shows the same garbling, together with the author's verbal definitions.
- The Polity share "2 3 %" splits across pp. 342–343; read as 23%. The "−1 0 / +1 0" are −10 / +10.
- p. 341 contains only the last line of the 20.1.4 sentence ("the original accuracy estimate").
- Footnote 1 says parts of 20.1.2 draw on Grimmer, Roberts and Stewart (2021).
