---
id: text-as-data-validation
type: concept
fields: [political-science]
n_sources: 29
tiers: [core, deep]
grounding: digests
sources: [chong-2007-framing/main, grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch01-introduction, grimmer-2022-textasdata/ch02-social, grimmer-2022-textasdata/ch03-principles, grimmer-2022-textasdata/ch05-bag, grimmer-2022-textasdata/ch06-multinomial, grimmer-2022-textasdata/ch07-vector, grimmer-2022-textasdata/ch08-distributed, grimmer-2022-textasdata/ch09-representations, grimmer-2022-textasdata/ch10-principles, grimmer-2022-textasdata/ch11-discriminating, grimmer-2022-textasdata/ch12-clustering, grimmer-2022-textasdata/ch13-topic, grimmer-2022-textasdata/ch14-low, grimmer-2022-textasdata/ch15-principles, grimmer-2022-textasdata/ch16-word, grimmer-2022-textasdata/ch17-overview, grimmer-2022-textasdata/ch18-coding, grimmer-2022-textasdata/ch20-checking, grimmer-2022-textasdata/ch21-repurposing, grimmer-2022-textasdata/ch22-principles, grimmer-2022-textasdata/ch23-prediction, grimmer-2022-textasdata/ch24-causal, grimmer-2022-textasdata/ch25-text, grimmer-2022-textasdata/ch26-text, grimmer-2022-textasdata/ch27-text, grimmer-2022-textasdata/ch28-conclusion, zaller-1992-massopinion/ch13-measures]
raw_ids: [text as data / validation]
canon_spine: political-science
generated_by: build_kg.py
---

# text-as-data-validation

## Canon spine entry

- **text as data / validation** (political-science): treating documents as quantitative measurements whose validity has to be shown against human judgment and task-specific checks (grad)

## Definitions in the sources

### political-science

- [[chong-2007-framing/main]] (pp. 107–108): frame content analysis with dictionaries or human coders; intercoder reliability needed for manual coding
- [[grimmer-2013-textasdata/main]] (pp. 2, 5): treating text as quantitative data, with outputs checked against human judgment or substantive evidence
- [[grimmer-2022-textasdata/ch01-introduction]] (pp. 28–29): validation judged by whether measures capture concepts and meet task assumptions, not by predicting unseen words (pp. 28–29). Canon id: text as data / validation.
- [[grimmer-2022-textasdata/ch02-social]] (pp. 66–68): treating text as measurements whose validity must be shown by task-specific checks; here validation is multi-layered (task, aggregation, face, hypothesis, label fidelity)
- [[grimmer-2022-textasdata/ch03-principles]] (p. 78): check a text representation against hand-coded data, known facts, accuracy or replication
- [[grimmer-2022-textasdata/ch05-bag]] (p. 104): here: checking that preprocessing kept the information relevant to the question
- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 119): only loosely related here: authorship probabilities are compared with Mosteller–Wallace's conclusion
- [[grimmer-2022-textasdata/ch07-vector]] (p. 129): here: no metric is correct in general; fit to task decides
- [[grimmer-2022-textasdata/ch08-distributed]] (p. 153): intrinsic vs extrinsic evaluation; the researcher's own task comes first
- [[grimmer-2022-textasdata/ch09-representations]] (p. 169): the authors stress that representation choices depend on the question (p. 169); validation itself is not discussed here
- [[grimmer-2022-textasdata/ch10-principles]] (p. 177): after a concept is fixed, one can check how accurately a method measures it
- [[grimmer-2022-textasdata/ch11-discriminating]] (p. 196): here validation is indirect and needs subject expertise; predictive accuracy alone is insufficient
- [[grimmer-2022-textasdata/ch12-clustering]] (pp. 211–212, 231): here: label by distinctive words, reading 10–30 documents, and replicate with hand coding or supervised learning; validate in new data [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch13-topic]] (pp. 239, 242–243): here: reading exemplar documents and checking labels against real-world referents [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch14-low]] (p. 263): here: regress component scores on external measures such as DW-Nominate, noting that measurement error lowers correlations
- [[grimmer-2022-textasdata/ch15-principles]] (p. 279): checking on independent data that the measure maps to the intended concept
- [[grimmer-2022-textasdata/ch16-word]] (p. 289): compare dictionary measures to hand labels on fresh data; revised dictionaries need new data
- [[grimmer-2022-textasdata/ch17-overview]] (p. 299): validating a measure against human labels
- [[grimmer-2022-textasdata/ch18-coding]] (p. 316): downstream validation can help reveal whether enough documents were coded (p. 307); found-data labels demand careful validation [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch20-checking]] (p. 337): checking that a text measure reflects the concept and works out of sample; it rests on being exposed to failure [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch21-repurposing]] (pp. 351, 360): measure from unsupervised output is justified by validation, not by the model
- [[grimmer-2022-textasdata/ch22-principles]] (pp. 374–375): here contrasted: predictions validated against outcomes, causal effects only indirectly
- [[grimmer-2022-textasdata/ch23-prediction]] (pp. 384, 389): here, held-out testing and, for prediction, continuous real-time checking [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch24-causal]] (pp. 425–426): here, validation of g is needed in training and again in the test set
- [[grimmer-2022-textasdata/ch25-text]] (p. 431, 435): here, the authors report similar results across analyses with slightly different $g$'s and 'relative stability' (p. 431, 435); the text does not call this validation
- [[grimmer-2022-textasdata/ch26-text]] (p. 439): here shown as a train/test split: discover on training, estimate on test
- [[grimmer-2022-textasdata/ch27-text]] (p. 456): here, reading matched document pairs to judge whether they are plausible counterfactuals [as `text as data / validation`]
- [[grimmer-2022-textasdata/ch28-conclusion]] (pp. 465–466): here: validation tied to the task, with humans in the loop, not to model fit or an assumed correct model
- [[zaller-1992-massopinion/ch13-measures]] (p. 335): loosely related: choosing a measure by testing it against criterion variables

## Candidate bridges

- [structural-analogy] agnostic vs structural view ↔ text-as-data validation: no single true model, so judge by validated task performance. — from [[grimmer-2022-textasdata/ch02-social]] (political-science → other)
- [structural-analogy] human-intruder test ↔ text as data / validation: human checks of whether discovered categories are coherent (p. 225). — from [[grimmer-2022-textasdata/ch12-clustering]] (political-science → other)
- [metaphor] Reading matched pairs ↔ text as data: validation — human judgment checks the automated measure — from [[grimmer-2022-textasdata/ch27-text]] (political-science → other)
- [structural-analogy] Faithful analogy between method and theory ↔ text as data / validation: measures must be validated against the concept they claim to capture. — from [[lupia-1998-dilemma/ch06-theory]] (political-science → other)
- [metaphor] Kepler's ellipse vs. perfect circles (p. 24) ↔ text-as-data/validation: do not fit a favourite model to data it does not match. — from [[ostrom-1990-commons/ch01-reflections]] (political-science → other)
- [structural-analogy] "Numbers do not speak for themselves" (fn. 3) ↔ text as data / validation: measurement needs analysis and checking to mean anything. — from [[shepsle-2010-analyzing/ch01-it]] (political-science → other)
- [structural-analogy] Counting media stories by direction as a simple measure of elite discourse ↔ [[text as data / validation]]: crude coded counts, justified by their relation to opinion. — from [[zaller-1992-massopinion/ch02-information]] (political-science → other)
- [structural-analogy] Coding error attenuating the consistency–stability slope (Fig. 4.2) ↔ text as data / validation: unreliable human codes weaken measured relationships. — from [[zaller-1992-massopinion/ch04-coming]] (political-science → other)
- [structural-analogy] Choosing the awareness measure by predictive performance against criteria ↔ text as data / validation: validating a measure against task-specific checks. — from [[zaller-1992-massopinion/ch13-measures]] (political-science → other)
