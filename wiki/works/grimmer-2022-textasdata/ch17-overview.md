---
id: grimmer-2022-textasdata/ch17-overview
work: grimmer-2022-textasdata
unit: Chapter 17. An Overview of Supervised Classification
pages: 293-302
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# An Overview of Supervised Classification

## L0 — One line
Supervised classification turns measurement into prediction: humans label a sample of documents, a model learns to reproduce those labels, and the model's performance is checked on held-out labeled data before the measure is used.

## L1 — The gist (≤ 120 words)
How can a researcher measure a concept in far more documents than humans can code, when counting a single word or applying a dictionary may not capture it? The chapter's answer is a three-step recipe: build a human-labeled training set, train a classifier on text features, and validate on held-out labels. The recipe is illustrated with Gillion's (2016) classification of about 3.2 million political paragraphs as race-related or not. The authors stress that feature choice matters more than model class. They also warn that the resulting measure contains error, which should ideally be carried into later analysis. The authors present the recipe as a default for automating measurement.

**Prerequisites:** the idea of a document-term count vector; basic prediction vs. labels; proportions and sampling.

## L2 — Key ideas (5–10 bullets)
- Supervised classification learns the mapping from text features to categories from coded examples. Earlier chapters fixed this mapping by hand (one word, or a dictionary). (p. 293)
- The human supplies three things: the labels, the feature representation, and the model class. (p. 293)
- The authors say features matter substantially more than the model class. (p. 294)
- Model classes differ in how they share information across documents. Simple models are often easy to interpret and need relatively little data. Complex ones need more data and may be relatively opaque. (p. 294)
- Step 1, the training set: random sampling is the simplest safeguard (here stratified), and the authors recommend at least two coders. Assess intercoder reliability. (p. 297)
- Step 2, classification: choose a representation, in part using domain expertise, then a model or an ensemble of models. (p. 298)
- Step 3, validation: hold out labeled data; researchers often add cross-validation. Accuracy can mislead when categories are skewed. (p. 299)
- The measures contain measurement error; ideally it is passed on to later analysis and checked for whether it is systematic. (pp. 300–301)

## L3 — Walkthrough

**Introduction (pp. 293–294).**
- Supervised classification uses labeled documents to build a model, a "classifier". The model relates words to labels and gives labels to unlabeled documents. (p. 293)
- The prediction for document $i$ is $\hat y_i = f_\mu(W_{i,\cdot})$. Here $W_{i,\cdot}$ is the document representation (the vector of term counts, as on p. 294) and $\mu$ are the model parameters. (p. 293)
- The parameters are learned from random samples of input $W$ and output $y$ (training samples). The task becomes predicting the label the analyst would have assigned herself. Once learned, labeling more documents is "essentially costless". (p. 293)
- Three human inputs: labels, input representation, model class. For now the authors assume the training documents are a random sample and the labels are perfectly accurate. (pp. 293–294)
- On representation, the authors say they "will happily choose better features over better models every time" (p. 294). They use term counts for exposition, but embeddings, phrases or other features could be used. (p. 294)
- Model classes are ways of sharing information. With no assumptions about how features map to output, one can only classify documents exactly like training ones. (p. 294)
- Simple models: often easy to interpret, require relatively little data, but may not be flexible enough. Complex models: hungrier for data, may be relatively opaque, but can often handle complex problems. (p. 294)

*Intuition note:* A model class is a way of sharing information across documents. With no assumptions about how features map to labels, the classifier could only label documents exactly like training ones (p. 294). The authors add that the features matter substantially more than the model class.

**17.1 Example: Discursive Governance (p. 295).**
- Gillion (2016) argues that talking about race matters beyond elections. He calls the process "discursive governance": rhetoric shapes how the public and policymakers set agendas and design, discuss, implement and evaluate policy. In his view, not discussing race lowers the salience of racial inequality and removes information on policy impact from policymaking. (p. 295)
- Data: presidential and congressional statements, with the paragraph as unit. This gives 912,466 presidential paragraphs (1955–2012) and 2.3 million paragraphs from members of Congress (104th–112th Congress). (p. 295)
- Concept: "race-related discourse", defined as political rhetoric that "primarily relates to an underrepresented racial or ethnic minority group or explicitly uses terms that carry a racial connotation" (p. 33 of Gillion, cited on p. 295).
- Too many documents for hand coding. As Gillion notes, dictionaries are insufficient: paragraphs may discuss race without the word "race", and words like "busing" may be race-related only in certain contexts. So he combines human coding with supervised learning (race-related vs. not). (pp. 295–296)

**17.2 Create a Training Set (p. 297).**
- Two annotators labeled 12,300 paragraphs using Gillion's definition. (p. 297)
- Consideration 1, sampling: an unrepresentative training set can give a biased classifier. A random sample is the simplest assurance. Gillion used a stratified random sample so that time periods are represented. The authors note random sampling is not always possible (see Chapter 18). (p. 297)
- Consideration 2, coder accuracy: even simple schemes are read differently by different coders. The authors recommend at least two annotators and assessing intercoder reliability, the proportion of documents both coders put in the same category. (p. 297)
- Gillion reports 97% agreement (his p. 164). He decided disagreements himself. (p. 297)

**17.3 Classify Documents (p. 298).**
- Choose a representation, partly using domain expertise. Many classifiers also include feature selection, which drops features found irrelevant. (p. 298)
- Gillion uses bag of words, after removing punctuation, numbers, white space and stop words. (p. 298)
- Models can be combined into ensembles that "vote" on each document's label. Gillion uses this approach. (p. 298)

**17.4 Check Performance (p. 299).**
- Hold out part of the labeled data from model fitting. Apply the fitted model to it and compare with the human labels. (p. 299)
- Cross-validation: repeatedly split the labeled data, fit, assess accuracy, then average. This guards against overfitting to one validation set. Gillion reports accuracy 0.77 (presidential) and 0.66 (Congress). (p. 299)
- Footnote: to raise accuracy above this, Gillion did another round of hand coding guided by the classifier. (p. 302)
- Accuracy is the number correctly classified divided by the number in the validation set. High accuracy can hide bad performance, especially with skewed categories. Precision and recall are treated in Chapter 20. (p. 299)

*Intuition note:* The researcher holds out labeled data from model fitting, applies the fitted model to it and compares with the human labels (p. 299). This tests the model on documents it was not fitted to.

**17.5 Using the Measure (pp. 300–301).**
- Gillion applies the classifier to all statements. (p. 300)
- Figure 17.1 (left): the proportion of presidential statements on race over time. Race-related statements are quite low for Obama relative to other presidents. Gillion argues Obama may have felt pressure to minimize race talk because he was a Black president. (p. 300)
- Figure 17.1 (right): the geography of House members' race statements. Gillion notes most are centered in the Southeastern US. (p. 300)
- The measures contain measurement error, from human coding or from the classifier. Ideally the error is passed on to the final analysis, and one checks whether it is systematic in ways that could affect the analysis. (pp. 300–301)

**17.6 Conclusion (p. 302).** The process is: code a training set, classify with a supervised classifier, evaluate. The next three chapters treat each step. (p. 302)

## Toy example (ours, not from the text)
Training set (6 paragraphs, label R = race-related, N = not):
1. "busing schools court" R
2. "civil rights voting" R
3. "tax budget deficit" N
4. "budget schools funding" N
5. "busing court order" R
6. "tax cut jobs" N

Learned rule (ours): a word is an "R-word" if it appears in more R paragraphs than N paragraphs. Counts: busing 2 vs 0, court 2 vs 0, civil 1 vs 0, rights 1 vs 0, voting 1 vs 0, order 1 vs 0 → R-words. "schools" is 1 vs 1 → not an R-word. Predict R if a paragraph has at least one R-word.

Held-out set (labels hidden from the rule):
- a. "court ruling voting" → predicts R, true R ✓
- b. "schools budget plan" → predicts N, true N ✓
- c. "busing tax" → predicts R, true N ✗ (word used in another context)
- d. "equality for minorities" → predicts N, true R ✗ (no learned words)

Accuracy = 2/4 = 0.5. Skew warning: suppose 100 held-out paragraphs, 95 N and 5 R. A classifier that always says N scores 95/100 = 0.95 yet finds 0 of the 5 R paragraphs.

## Concepts
- [[supervised-classification]] (new) — learn a text-to-label mapping from human-coded documents, then label the rest (p. 293)
- [[training-set]] (new) — the human-labeled sample used to fit the classifier (p. 297)
- [[feature-representation]] (new) — how text is turned into model input (here term counts); the authors rank it above model class (p. 294)
- [[intercoder-reliability]] (new) — proportion of documents two coders put in the same category (p. 297)
- [[ensemble-classifier]] (new) — many models "vote" on each document's label (p. 298)
- [[cross-validation]] (new) — repeated split, fit and assess on held-out data, then average (p. 299)
- [[accuracy-precision-recall]] (new) — accuracy is share correct; it can mislead with skewed classes; precision and recall come in Ch. 20 (p. 299)
- [[text-as-data-validation]] — validating a measure against human labels (p. 299)
- [[measurement-error]] (new) — error from coders or classifier that should be carried into later analysis (pp. 300–301)

## Canonical instances
- [[gillion-race-discourse]] (new) — classifying about 3.2 million presidential and congressional paragraphs as race-related, with 12,300 hand-coded for training (pp. 295–300)

## Bridges (candidates)
- [structural-analogy] Training and held-out validation ↔ statistics: fitting a model on one sample and testing on another to check generalization — the same logic, but the chapter gives no shared formalism.
- [structural-analogy] Intercoder reliability ↔ survey and measurement methods: agreement between independent raters as evidence of a clear concept definition.

## Questions this raises
- If coders disagree on 3% of paragraphs (97% agreement), how does that noise limit the best possible classifier accuracy?
- Why is Gillion's accuracy lower for Congress (0.66) than for the presidency (0.77), and is 0.66 good enough for his claims?
- How should classifier error be "passed on" into a downstream regression, and how can one tell if it is systematic?

## Reading notes
- Printed page = pdf page (offset 0).
- The inline formula on p. 293 is garbled in the text layer ("f μ ( W i , )"). I wrote it as $f_\mu(W_{i,\cdot})$, reading the subscript as a row index. No image of that page was provided, so this is unchecked against the page image.
- On p. 299 the text says the held-out set is excluded from the fitting "described in (2)", presumably a reference to step 2 of the list on p. 296 (17.3); the text does not say.
- On p. 300 the classifier is applied to "the test set", apparently the full set of statements; p. 297 also uses "test set" for where the classifier should generalize. This seems to differ from the held-out validation set of 17.4. The "about 3.2 million" paragraph total is my sum of 912,466 and 2.3 million (p. 295).
- Figure 17.1 (p. 300) is reproduced from Gillion; only its caption and the authors' description are summarised here.
