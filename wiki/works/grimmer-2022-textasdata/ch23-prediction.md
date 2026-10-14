---
id: grimmer-2022-textasdata/ch23-prediction
work: grimmer-2022-textasdata
unit: "Chapter 23. Prediction"
pages: 381-406
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
# Prediction (Grimmer, Roberts & Stewart, ch. 23)

## L0 — One line
Text can be used to predict outcomes outside the text, but good prediction depends on how the model is evaluated, because the link between predictors and outcome can drift and prediction can change behaviour.

## L1 — The gist (≤ 120 words)
The chapter asks how text can predict outcomes, rather than measure concepts inside it, and what can go wrong. Prediction needs data, a model and an evaluation metric. It is closer to supervised learning than to causal inference. Five principles warn that predictors need not be causal, that cross-validation can mislead when the future differs from the past, that average accuracy can hide failure, that interpretability has practical value, and that prediction is hard to use in policy. Four tasks illustrate this: source prediction, linguistic prediction, social forecasting and nowcasting. The Trump-tweets model shows why good historical precision and recall need not carry over (its later validation is weak), and Google Flu Trends shows how drift may undermine a model that looked good on historical data.

**Prerequisites:** supervised classification, training/test split and cross-validation (Chs. 19–20); loss functions; precision and recall; basic regression.

## L2 — Key ideas
- Prediction has three parts: labeled data, a model fitted by minimizing a loss, and an evaluation metric tied to the analyst's purpose (p. 383–384).
- Prediction is closer to supervised learning than to causal inference. The new difficulty is time: labeled data may not resemble the data to be predicted, so drift can occur (p. 385).
- Predictors need not cause the outcome. They may even be effects of it, as in nowcasting (predicting a present value whose official figures come later) (p. 387).
- Cross-validation works best for estimating future error when the future is like a random sample of the past; if held-out historical data differ systematically from the future, it will in general not estimate error accurately. Successful predictions can themselves create drift, and real-time checking is the best test (p. 388–389).
- Average accuracy can mislead (the accuracy paradox). Precision, recall, F1 (one score combining the two) and cost-weighted $F_C$ help, and subgroup accuracy should be checked (p. 389–391).
- Using predictions in policy is not the same as evaluating policy impact. It can change incentives and create feedback loops, where model-guided action produces the data that confirm the model (p. 392).
- Four text-prediction tasks: source, linguistic, social forecasting, nowcasting (p. 394).
- Beauchamp's polling study and Google Flu Trends show out-of-sample and benchmark discipline, and the cost of drift (p. 401–404).

## L3 — Walkthrough

**Introduction (pp. 381–382).** The chapter turns from using text to measure a concept to using text "to tell us something about the future" (p. 381). Examples: spam filtering, legal-decision prediction (Aletras et al.), box-office prediction from tweets (Asur and Huberman), conflict onset from newspapers (Mueller and Rauh) (p. 381). Social scientists have been more hesitant than computer scientists to make prediction a goal. The authors suggest it may gain importance with real-time data, and that predictive models may help judge which theories explain events in advance (pp. 381–382). The chapter announces four tasks: source prediction, linguistic prediction, social prediction, nowcasting (p. 382).

### 23.1 The Basic Task of Prediction (pp. 383–384)
Three components: data, a model, an evaluation metric (p. 383). Running example: predicting state-level election polls from Twitter.
- Outcome $y_i$ for unit $i$; prediction $\hat y_i$. $X_i$ is a vector of $P$ non-text features. $W_{i,\cdot}$ is the text predictors, here the tweets (p. 383).
- *Labeled* data has predictors and $y_i$ known. It is split into training set and test set (p. 383).
- The model is chosen via a loss function $L(\cdot)$ comparing predicted and actual outcomes. Example, least squares on training set $I$:
$$\hat\mu = \arg\min_\mu \sum_{i\in I}\left(y_i - W_{i,\cdot}\mu\right)^2 \tag{23.1.1}$$
- Later, $\hat y_i = W_{i,\cdot}\hat\mu$ is computed for weeks without polls (p. 384). The authors expect more complex methods from the measurement chapters to do better than linear regression (p. 384).
- The metric should reflect the analyst's goal. A political scientist filling in past polls and a consultant who cares only about this week's support for one candidate need different evaluation (p. 384).
- Generally the metric is the generalization error, the error on unseen data from the population of interest. With a random sample, it is approximated on a held-out sample $O$:
$$\text{Error}_{\text{out}} = \mathbb{E}_{i\in O}\left[L\big(y_i, f(\hat\mu, W_{i,\cdot})\big)\,\middle|\, I\right]$$
- This is estimated with a hold-out set or cross-validation (Ch. 20) (p. 384).

### 23.2 Similarities and Differences between Prediction and Measurement (p. 385)
- The setup is almost identical to supervised learning in Part 3, where $y_i$ is the category and $W_{i,\cdot}$ the words. It is also close to causal inference (next chapter), with treatment $t_i$ and confounders $X_i$ (variables correlated with both treatment and outcome). The authors advocate some type of split-sample validation in all three cases (p. 385).
- Prediction is closer to supervised learning than to causal inference. Supervised learning is one example of prediction, namely predicting hand codes. The chapter's $y_i$ is broader: Supreme Court outcomes, stock markets, future documents (p. 385).
- Difference: prediction "invariably deals with the complication of time." Labeled data may not reflect the data to be predicted, which "could generate drift." People or contexts may change behaviour and strategies so that predictions stop being useful (p. 385).

### 23.3 Five Principles of Prediction (pp. 387–393)

**23.3.1 Predictive features need not cause the outcome (p. 387).**
- Ice-cream mentions on social media can predict swimsuit sales. Both are plausibly caused by hotter weather and summer vacation, and the mentions can be used if they improve predictive power (p. 387).
- Causal factors (weather, weekends, vacations) may help, and can matter for stability over time and space. But a causal effect that is small in magnitude, even if significantly nonzero, will not necessarily improve accuracy (Lo et al.) (p. 387).
- Predictors can even be results of the outcome. Flu data from health officials lags by weeks, while flu raises Google searches for remedies, so searches were used to predict flu incidence (Ginsberg et al.) (p. 387).

**23.3.2 Cross-validation is not always a good measure of predictive power (pp. 387–389).**
- Cross-validation estimates generalization error if the test data are a random sample of the target population. Historical data are typically not a random sample of future data. If held-out historical data differ systematically from the future, cross-validation "will not accurately estimate the error rate" (p. 388).
- Ice-cream example: if the platform downweights ice cream in the news feed, mentions might fall, the mentions–sales relationship would change, and prediction error would rise (p. 388). "Obama" mentions might have predicted the 2008 Democratic win but probably not as strongly in 2016, when he was not a candidate (p. 388).
- The best case for cross-validation is when the future is like a random sample of past data (p. 388).
- Successful predictions can themselves create drift. If it becomes known that words in financial reports predict stock value, firms may change their wording and investors their trading, which undermines the relationship (pp. 388–389).
- Checking predictions against real-time data is "the best measure of accuracy." This is feasible when outcomes come quickly (spam, clicks), but infeasible for slow outcomes like war or elections (p. 389).

*Intuition note.* A held-out test set is a good stand-in for the future when the future is like a random sample of the past. If the predictor–outcome relationship changes, or if publishing a prediction changes people's behaviour, cross-validation will in general not estimate the error accurately.

**23.3.3 It's not always better to be more accurate on average (pp. 389–391).**
- Average accuracy is $\frac{\sum_{i=1}^N \mathbb{I}(y_i=\hat y_i)}{N}$ (p. 389).
- Accuracy paradox: with 2 spam emails among 1,000, predicting "no spam" gives $998/1000=.998$ accuracy but never finds spam (p. 389).
- Confusion matrix (columns = actual class, rows = predicted class): True Positive and False Positive in the "predicted positive" row, False Negative and True Negative in the "predicted negative" row (p. 390).
$$\text{Recall}=\frac{TP}{TP+FN},\qquad \text{Precision}=\frac{TP}{TP+FP}$$
- Recall: how many actual positives were predicted positive. Precision: how many predicted positives were actually positive (p. 390).
- F1 trades them off. The authors say it reflects their product, so it falls if either is too low (p. 390):
$$F_1 = \frac{2\times \text{Recall}\times\text{Precision}}{\text{Recall}+\text{Precision}}$$
- F1 may not match real costs. Wrongly flagging a real email as spam may cost more than missing spam (precision matters more). In diagnosing a rare disease, recall may matter more. With $C$ the number of times recall is more important than precision (p. 390):
$$F_C = \frac{(1+C^2)\times \text{Recall}\times\text{Precision}}{\text{Recall} + (C^2\times \text{Precision})}$$
- Overall accuracy can hide subgroup differences. Facial recognition has been shown to be more accurate for white males than for darker-skinned females (Buolamwini and Gebru), which could create racial and gender bias downstream (p. 391).

*Intuition note.* When one class is rare, a model can score high accuracy by ignoring it. Precision and recall ask separately how clean and how complete the model's positive calls are.

**23.3.4 Practical value in interpreting models (p. 391).**
- Although how one arrives at a prediction matters less than in causal inference, decision makers in foreign policy or medicine may distrust opaque forecasts. People affected (credit scoring, legal AI) may demand reasons, which the EU has called a "right to explanation" (Goodman and Flaxman) (p. 391).
- The authors say this practical point differs from the ethical debate on algorithmic transparency. Explanations help because people view predictions with skepticism until they understand their essential components (p. 391).

**23.3.5 Applying prediction to policymaking is difficult (pp. 391–393).**
- Policy uses include policing, education, immigration and food inspection (p. 391).
- (i) Using a predictive model to implement a policy is not evaluating the policy's impact. Athey's example: buildings most likely to fail inspection may be the hardest to repair, so targeting them is not necessarily the most cost-effective. Buildings that fail and are easy to repair would not be revealed by the predictor (p. 392).
- (ii) Policy based on a model changes incentives and can undermine it. Actors may invest heavily in what affects their prediction without better outcomes (college ratings, O'Neil). Owners who expect a low inspection chance may skip upkeep (p. 392).
- (iii) Data collection can be a result of the policy. In predictive policing, patrols go where the model points, so more arrests occur there and the model's prediction is reconfirmed (Lum and Isaac). Steps can mitigate loops "under certain conditions" (Ensign et al.) (p. 392).
- Tools can be misused. Predicting mental health from posts could help people in need but raises privacy concerns and could serve advertisers or harassers (Chancellor et al.). Researchers should weigh benefits against harms beyond IRB consultation, including whether to release the tool (pp. 392–393).
- Summary: cross-validation may fail, accuracy may not be the right metric, and policy use needs validation and may have unintended consequences (p. 393).

### 23.4 Using Text as Data for Prediction: Examples (pp. 394–404)
Four categories, "neither exclusive nor exhaustive": source prediction, linguistic prediction, social forecasting, nowcasting (p. 394).

**23.4.1 Source prediction (pp. 394–398).**
- It predicts the source, or the source's characteristics, from text. It is prediction because information outside the text is estimated from the text (p. 394).
- Examples: Mosteller and Wallace used filler words to attribute the unknown-author Federalist Papers to Madison. Airoldi et al. studied Reagan's radio addresses. Other uses: malicious websites, bots, fake reviewers, online propagandists, personality, truthfulness, popularity of a text, depression (pp. 394–395).
- Illustration inspired by David Robinson's 2016 blog post. Trump tended to tweet from Android at early or late hours, his staff from iPhone at midday (Fig. 23.1). Android tweets tended to be more negative in tone (p. 395).
- In 2017 Trump switched to an iPhone, so the two could no longer be separated by device. Using content, the authors predict the source from the old labels (p. 396).
- Training data: 1,390 campaign tweets. Naive Bayes on words gave precision 0.82 and recall 0.75, estimated with cross-validation (p. 396). Table 23.1 shows the most predictive words. Android: *hillary, crooked, win, cruz*. iPhone: *thank, #trump2016, #makeamericagreatagain, join* (p. 396).
- They collected the 471 most recent tweets (footnote 5: 16 February 2018) and predicted their source. Good historical precision and recall need not carry over, as topics and the team's strategy had shifted (p. 397). They have no true labels, so they validate by plausibility only (p. 397).
- Table 23.2: top predicted staff tweets are announcements and news reports. The authors describe the predicted Trump tweets as about ISIS, votes in the House and news coverage, and say these conform to their expectations given the type of phone (p. 397).
- Timing check (Fig. 23.2): predicted Trump and staff tweets converge in hour pattern, unlike the historical pattern. The authors do not know whether the staff's schedule changed or the model errs; "without the true labels" they "might not ever know" (p. 398).

**23.4.2 Linguistic prediction (pp. 398–400).** It uses text to predict subsequent text. It is harder than source prediction because the outcome space is much larger (p. 398).
- Autocorrect, autocomplete (can be customized to the individual) and question answering. Question answering usually searches a database of answers and is an information-retrieval task (Watson, Siri) (p. 399).
- Machine translation. Direct translation (word-by-word lookup) lacks fluency and can be uninterpretable. Statistical approaches trade off fidelity against fluency and optimize both jointly (p. 399). Machine learning is increasingly the approach of choice. It learns from texts with several expert translations, or uses back-translation (A→B→A) to minimize the difference between the original and the round-trip text (pp. 399–400).

**23.4.3 Social forecasting (pp. 400–402).** Text is used to predict society. Examples (p. 400):
- Markets, company success (10-K reports, news), sales, box office, consumer confidence.
- European human-rights court decisions from case facts, ballot "roll-off" from Google searches (Reilly et al.), and bills becoming law from bill text (Nay).
- Public good: floods from Flickr tags, low restaurant hygiene scores from Yelp reviews.

*Beauchamp (2017) in detail* (pp. 400–402). Aim: predict state polls and state election outcomes, interpolate historical polls, cover states with few polls, and detect sharp local opinion changes (p. 401).
- Four lessons (p. 401): *Statistics*: enough reference data to validate. *Benchmarks*: compare with the best alternative, not naive or random predictions. *Training*: train on true values of the dependent variable (e.g. polls), not proxies. *Out of sample*: test data truly out of sample, ideally forward in time.
- Data: 120 million tweets in the two months before the 2012 election, containing political keywords. Location comes from geotags and profile text. The tweets are represented by the top 10,000 unigrams and aggregated to state-day (p. 401).
- Outcome: Obama's support share in 1,200 state polls. Training uses only states with at least 15 polls (24 of 50). Models: elastic net, SVM, random forest, plus an ensemble with time trends and fixed effects (p. 401).
- Three out-of-sample tests (pp. 401–402). (1) Election-day results in the 24 states, text-only model: "almost as well as" polls. (2) The other states, truly out of sample: "surprisingly good accuracy." (3) The text model with time trends and fixed effects, forecasting next-day polls recursively: text adds predictive power beyond the polling baseline for short-term changes and interpolation (p. 402).
- Predictive features: candidate mentions are not among the most predictive. *https* (read by Beauchamp as links to external information) predicts Obama support, *rt* predicts Romney (p. 402).
- Authors' lessons (p. 402): forecasting needs repeated measures, so rare events are hard, and elections are rare enough that polls are used as proxies. Only out-of-sample data show real performance, since the social media–outcome relationship keeps changing. The measure must be better at predicting than current approaches in order to be useful. Beauchamp's predictions beat random ones, but only some models beat polls.

**23.4.4 Nowcasting (pp. 402–404).**
- Longer gaps between data and event usually mean lower accuracy (for example, civil conflict one or two years ahead). Nowcasting sets the gap to zero: it "predicts" present events whose official data arrive days or months later (pp. 402–403).
- Text suits it as social media and news provide a constant stream. Examples: consumer confidence, unemployment, Google searches for sales of goods, houses and cars, hurricanes, food poisoning, migration after disasters (p. 403).
- Google Flu Trends (Ginsberg et al.), with the CDC: 45 searches most correlated with historical flu-related doctor visits were used to predict later visits (p. 403).
- GFT was initially very predictive but declined. It missed the 2009 swine flu. By 2013 its estimates were nearly double actual flu rates (Butler). Past flu data predicted almost as well (Goel et al.) (pp. 403–404).
- Reasons given: models need constant updating. Swine-flu media coverage may have changed search patterns. Google changed its search algorithms. With about 50 million candidate phrases and little outcome data, GFT could find terms only coincidentally related to flu season (Lazer et al.). Drift may overwhelm prediction "without constant supervision and tweaking" (p. 404). Footnote 7 notes that Twitter has been proposed, but is likely to suffer the same drift (p. 406).

*Intuition note.* Searching many candidate predictors against very little outcome data makes accidental matches likely. When the system behind the predictors changes, such matches stop working.

### 23.5 Conclusion (p. 405)
- Text allows prediction of source characteristics, future text, social outcomes and current measurements (p. 405).
- Predicting complex conversations is still very difficult. Forecasts of events far from the inputs are likely less accurate than closer ones. Drift can make once-accurate nowcasts inaccurate. Continuous real-time validation is the most accurate measure of accuracy, more accurate than cross-validation (p. 405).
- Policy use of prediction should be evaluated separately, with attention to feedback loops, strategy changes and discrimination (p. 405).
- Next chapter: causal inference asks what would have happened, which allows less flexibility in the information used but has more straightforward policy implications (p. 405).

## Toy example
*(Our own, not from the text.)* Past summer: weekly ice-cream mentions $x = 10, 20, 30, 40$; sales $y = 20, 40, 60, 80$. Fit through the origin: $\hat\mu=\sum xy/\sum x^2 = (200+800+1800+3200)/(100+400+900+1600) = 6000/3000 = 2$. Training and cross-validated error are 0, since the data are exactly linear.

Next summer the platform halves visible mentions. Two weeks truly drive sales of 50 and 70, which under the old relationship would show $x=25, 35$. Now the model sees $x = 12.5, 17.5$ and predicts $25$ and $35$. Errors are $25$ and $35$. Squared errors are $625$ and $1225$, mean $925$, root $\approx 30.4$. The historical error of 0 said nothing about this, which is drift as in §23.3.2.

## Concepts
- [[prediction-task]] (new) — predicting $y_i$ for unseen units from text $W$ and non-text $X$ features, using data, a model and an evaluation metric (p. 383)
- [[generalization-error]] (new) — expected loss on unseen data from the target population, estimated on held-out data (p. 384)
- [[text as data / validation]] — here, held-out testing and, for prediction, continuous real-time checking (pp. 384, 389)
- [[concept-drift]] (new) — the predictor–outcome relationship changes over time, so historical fit misleads; successful predictions can cause it (pp. 385, 388–389)
- [[accuracy-paradox]] (new) — higher accuracy need not mean a better model, as when predicting "no spam" (p. 389)
- [[precision-recall-f1]] (new) — precision, recall, F1 and cost-weighted $F_C$ as alternatives to accuracy (pp. 389–390)
- [[source-prediction]] (new) — estimating the author or author traits from text (p. 394)
- [[linguistic-prediction]] (new) — predicting subsequent or intended text (p. 398)
- [[social-forecasting]] (new) — using text to predict societal events (p. 400)
- [[nowcasting]] (new) — using alternate data to predict present measures released later (p. 403)
- [[feedback-loop]] (new) — model-guided action produces data that confirms the model (p. 392)

## Canonical instances
- [[trump-tweets-source-prediction]] — Naive Bayes on 1,390 tweets (precision 0.82, recall 0.75); weak validation after device change (pp. 396–398)
- [[federalist-papers-authorship]] — Mosteller and Wallace's filler-word authorship attribution, mentioned (p. 394)
- [[beauchamp-twitter-polls]] — text predicts state polls; four lessons and three out-of-sample tests (pp. 400–402)
- [[google-flu-trends]] — nowcast whose accuracy fell; the authors point to drift (and to coincidental search terms) as reasons (pp. 403–404)
- [[predictive-policing-feedback-loop]] — patrols → arrests → model reconfirmed (p. 392)
- [[swimsuit-ice-cream]] — non-causal predictor and its drift (pp. 387–388)

## Bridges (candidates)
- [same-math] Supervised misclassification error (Ch. 19–20 measurement) ↔ prediction error: the same held-out estimate of generalization error (pp. 384–385)
- [structural-analogy] Predictive models as tests of theories ↔ observable implications (KKV): both ask whether a theory yields checkable consequences (p. 382)
- [structural-analogy] Predictions changing actors' behaviour (§23.3.2) ↔ principal–agent problem: agents who know the monitoring rule can adapt to it
- [structural-analogy] Policing feedback loops ↔ path dependence: early choices shape the data that reinforce them

## Questions this raises
- How can analysts validate a source or nowcast model when no true labels arrive (as with Trump's tweets after 2017)?
- How often must a nowcasting model be retrained or recalibrated to keep up with drift?
- Can a policy-use predictor be designed so that actors cannot game it, or so that feedback loops are detected?
- How should an analyst choose the cost ratio $C$ in $F_C$ in practice?

## Reading notes
- Printed page = pdf page (381–406). Footnotes are on p. 406.
- Equations in the text layer are flattened. The page images show recall, precision, F1 and $F_C$ also printed flattened, with fraction bars lost. I wrote them as standard fractions, reading the printed order: numerator, then denominator. Eq. (23.1.1) was checked against the image.
- The text says F1 "multiplies" precision and recall. The printed formula is $2PR/(P+R)$, so it is a normalized product-over-sum.
- The Fig. 23.2 sentence "converge, shown in Figure 23.1" is ambiguous. I read it as: convergence relative to the pattern in Fig. 23.1.
- Table 23.1 lists 19 rows on p. 396 and row 20 (*today / people*) on p. 397. Table 23.2 shows "&amp;" artifacts in the printed tweets.
- "Jursfsky" is printed for the Jurafsky and Martin citation (p. 399).
- Source-prediction validation on the 471 tweets is plausibility-only, as the authors say (p. 397).
