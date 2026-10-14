---
id: grimmer-2022-textasdata/ch27-text
work: grimmer-2022-textasdata
unit: "Chapter 27. Text as Confounder"
pages: 447-460
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Text as Confounder

## L0 — One line
When the text of a document may be related to both treatment and outcome and we do not know which parts matter, we must estimate a low-dimensional summary of the text and adjust for it by regression or matching.

## L1 — The gist (≤ 120 words)
Observational causal analyses must control for confounders, and sometimes the confounder is the text itself. The chapter asks how to adjust for many word counts when we do not know which words matter. It shows three routes: a Lasso (penalized regression) on the document-term matrix (word counts), controls for topic proportions, and matching on a low-dimensional text summary (TIRM, Topical Inverse Regression Matching). In the gender-and-citation example, the Lasso and topic controls give a negative female coefficient, and TIRM matching gives an average of 6.5 fewer citations for women's articles. Each method has weaknesses. Using text does not remove the core difficulties of causal inference and may add new ones.

**Prerequisites:** potential outcomes and conditional ignorability; linear regression; Lasso/penalized regression; topic models; matching and propensity scores; document-term matrix.

## L2 — Key ideas (5–10 bullets)
- Text can confound a treatment–outcome link. Women and men write on different IR topics, and topic may affect citations (p. 447).
- Conditioning on raw words fails because the vocabulary $J$ can exceed $N$. Exact matches on word frequencies almost never exist. We want to adjust only for the confounding parts of the text (pp. 448–449).
- The strategy is to estimate a low-dimensional summary $g(W_i,\cdot)$ and assume SUTVA (each unit's outcome depends only on its own treatment), conditional ignorability given $g$ (treatment is independent of the potential outcomes), and positivity (each treatment value has positive probability) (p. 449).
- The Lasso regression approach selects predictive words, but predictive words need not be the best confounders. The two-Lasso fix of Belloni et al. is one remedy (p. 452).
- Controlling for topic proportions is more efficient if topics capture the confounding. Unsupervised reductions can miss key words such as *minerva* (pp. 452, 455).
- Matching lets the analyst read matched documents and judge whether they are plausible counterfactuals (p. 456).
- TIRM matches on topics from a Structural Topic Model (STM) plus a treatment-projection score. Its matched sample shows a larger gender gap, 6.5 fewer citations on average (pp. 457–458).
- Text does not solve causal inference. Use train/test splits and replication (p. 459).

## L3 — Walkthrough

### Introduction: why text can confound (pp. 447–449)
- Text can be an outcome or a treatment, and it can also be a control variable in observational work (p. 447).
- **Running example:** Maliniak, Powers and Walter (2013) find that IR articles by women are cited less, which they attribute to perceived gender. They control for credentials and article-level covariates (venue, topic, perspective, age). Treatment is gender and the outcome is citations (p. 447).
- Gender is not randomly assigned, so a raw mean difference is not causal. Women write on different topics, so article text may relate to both treatment and outcome and so confounds the relationship. The original authors used hand-coded content categories as controls (p. 447).
- Other cases listed: bill content and veto threats, admissions files and race or gender, treaty content and trade (p. 447).
- Numeric confounders can be handled by regression or matching. Text is harder: there are probably more words than observations, and we want to adjust only for the words or word clusters that confound. This is the "curse of dimensionality" (p. 448). Researchers often do not know which text aspects relate to both treatment and outcome, so they must *estimate* them (p. 448).
- **Setup (as in Ch. 24):** $N$ units, treatment $t_i\in\{0,1\}$, potential outcomes $y_i(1)$, $y_i(0)$ (p. 448).
  - Matching on $P$ pre-treatment covariates in the $N\times P$ matrix $X$ aims at *balance*, similar covariate distributions in treated and control groups (p. 448).
  - If $X$ includes all sources of confounding, matching can achieve balance ($X_i \perp t_i$). This allows unbiased estimation of the average treatment effect on the treated (p. 448).
  - Usually $P\ll N$. With selection on observables we assume conditional ignorability: $t_i \perp (y_i(0),y_i(1)) \mid X_i$ (p. 448).
- With the document-term matrix $W$ added (shape $N\times J$ by implication, $J$ = vocabulary), the dimension $P+J$ is large and may exceed $N$. We do not know which words matter. Matching on all words finds matches only if two texts have identical word frequencies, which is vanishingly unlikely as dimension grows (p. 449).
- **Approach:** estimate a low-dimensional summary $g$ of $W$ for the confounders. Text matching needs three assumptions (p. 449):
  - **SUTVA:** for all individuals $i$, $y_i(t)=y_i(t_i)$ (as printed).
  - **Conditional ignorability:** $t_i \perp (y_i(0),y_i(1)) \mid g(W_i,\cdot)$.
  - **Positivity:** for all individuals $i$, $\Pr(t_i=t)>0$ for all $t\in\mathcal T$.
- Footnote 2: D'Amour et al. (2021) show positivity can often fail with high-dimensional data (p. 459).
- Related work named: Mozer et al. (2020) compare hundreds of text-matching methods. Veitch, Wang and Blei (2019) use word embeddings. Keith, Jensen and O'Connor (2020) is a review (p. 449).
- **Why the example is hard:** evidence of bias is strongest if women wrote identical articles and were cited less. Men and women differ in topics, methods and epistemology, so lower citations might reflect bias against topics rather than against women (p. 449). Maliniak et al. used TRIP database codes (subfield, issue areas, methodology, paradigm, epistemology). The chapter tries automated methods instead (pp. 449–450).
- **Data:** Roberts, Stewart and Nielsen (2020) obtained 3,201 IR articles since 1980 via JSTOR Data for Research, 333 written solely by women (p. 450).
- *Intuition note:* We cannot control for every word, because exact matches vanish and we would also over-control. The task is to find a small summary of the text that captures what links treatment and outcome.

### 27.1 Regression adjustments (pp. 451–455)
- **Lasso procedure:** regress citations on the term-document matrix, the Maliniak et al. covariates (age, tenure, journal) and an all-female-authors indicator. The treatment coefficient is *unpenalized*. The penalty on the other coefficients is chosen by cross-validation. The Lasso-selected words are then put into a linear regression for citations (p. 451).
- **Result:** the selected terms include funding words (Minerva), method words (cause-effect, zscore), substantive words (surgenc, democ) and author names (weingast, shepsl). *APSR* publication and a positivist framework predict higher citations. The female coefficient is negative (p. 451).
- **Drawbacks (p. 452):**
  - Adjustment is limited by the representation (word counts) plus the linear model. This rules out interactions, for example *minerva* with democracy versus with autocracy.
  - The Lasso selects good predictors, which may not be the best confounders (Belloni, Chernozhukov and Hansen 2014). Their alternative: one Lasso predicting the outcome, one predicting the treatment, then a regression adjusting for the union of selected variables.
  - Footnote 7: with two highly correlated predictors, one is likely zeroed out. This may drop variables correlated with treatment, which could be the key confounders. Also, the $\lambda$ that minimizes prediction error need not minimize error on the causal effect (pp. 459–460).
- **Lower-dimensional representation:** use topic proportions as controls. If topics capture the confounding, this is much more efficient, similar to the gains of Naive Bayes when its assumptions hold (p. 452).
- **Fig. 27.2 (topic proportions as controls):** topics range from war to development to foreign policy. Topic 13 (quantitative models) has higher citations than Topic 7 (Soviet Union and military). The female coefficient is similar to the Lasso's: controlling for topic, women still receive fewer citations (p. 454).
- PCA or SVD could replace topics. But these, and basic topic models, ignore treatment and outcome. The top words of the topics did not include *minerva*, though it strongly predicts citations. Using outcome or treatment information when selecting covariates may help (pp. 454–455).
- *Intuition note:* A method that is good at predicting citations may still choose the wrong controls. A method that ignores citations altogether may miss important words.

### 27.2 Matching adjustments (pp. 456–458)
- **Advantage of matching** (Roberts et al.): the analyst can read matched documents and judge whether they are good counterfactuals and whether treatment is plausibly "as-if random". This manual validation complements formal balance checks (p. 456).
- **Table 27.1** pairs all-female-authored articles with matched controls:
  - Choi (2004, democracies and war victory) ↔ Regan (2002, third-party interventions and civil conflict duration).
  - Kelleher (1981, NATO theater nuclear modernization) ↔ Trofimenko (1981, counterforce).
  - Cutler (1999, authority in the global political economy) ↔ Kang (1995, East Asian development) (pp. 456–457).
- **TIRM (Topical Inverse Regression Matching)** combines modeling of treatment assignment with coarsening. The Structural Topic Model (STM), with treatment as a topical-content covariate, jointly estimates topics and document-level scores of how likely each document was treated. Matching is on both (p. 457).
- **Treatment-assignment part:** this is analogous to propensity-score matching. Following Taddy (2013), they derive a projection that is a sufficient reduction of the word counts' information about treatment. Estimated within the topic model, it captures treatment information *not* carried in the topics (p. 457).
- **Coarsening part:** with treatment as a content covariate, the same topic can have different word distributions under treatment and control. A final STM step re-estimates all controls' topic proportions as though treated. This is consistent with a (local) average-treatment-effect-on-the-treated estimand. Matching on projection and topic proportions yields matches that are topically similar and have similar within-topic probabilities of treatment (pp. 457–458).
- **Application:** 15 topics. They also built matched samples using only the projection and only the topics. Re-estimating the Maliniak et al. models on the TIRM sample, they find gender differences are *even more pronounced* than originally reported. Women's articles receive an average of 6.5 fewer citations than as-identical-as-possible articles by men or mixed-gender groups (p. 458).
- *Intuition note:* Instead of adding controls, we pair each women-authored article with similar articles by men or mixed-gender teams. Because we can read the pairs, we can check whether the text model did its job.

### 27.3 Conclusion (p. 459)
- Text measures many social phenomena but is rarely used for causal inference. Using it as treatment, outcome or control brings pitfalls. It does not solve the core problems of causal identification and may add complications (p. 459).
- Advice: consult the causal inference literature (Morgan and Winship; Imbens and Rubin; Hernán and Robins). Use train/test splits to simulate replication, and repeat experiments in new populations and periods (p. 459).
- Footnote 3: the quantity of interest is the effect of *perceived* gender, so the ideal comparison is the same text with two different names (p. 459).

## Toy example (ours, not from the text)
Eight articles, two topics. A = quantitative (high citations), B = other. Women write mostly B.
- Women: A: 20; B: 8, 10, 12. Mean $=(20+8+10+12)/4=12.5$.
- Men: A: 24, 26, 28 (mean 26); B: 14. Mean $=(24+26+28+14)/4=23$.
- Naive gap: $12.5-23=-10.5$.
- Within-topic gaps: A: $20-26=-6$; B: $10-14=-4$.
- Weight by the women's topic mix (A 1/4, B 3/4), the ATT-style adjustment: $0.25(-6)+0.75(-4)=-1.5-3=-4.5$.
- Check: men reweighted to women's mix average $0.25(26)+0.75(14)=17$, and $12.5-17=-4.5$ ✓.
- Topic confounds, so the naive gap overstates the within-topic gap. In real text, "topic" must be estimated, as in TIRM.

## Concepts
- [[text-as-confounder]] (new) — text content related to both treatment and outcome, so it must be adjusted for (p. 447)
- [[curse-of-dimensionality]] (new) — too many text features to condition on directly, since words outnumber observations (p. 448)
- [[balance]] (new) — similar covariate distributions across treatment and control groups (p. 448)
- [[conditional-ignorability]] (new) — treatment independent of potential outcomes given covariates, here given $g(W_i,\cdot)$ (pp. 448–449)
- [[positivity]] (new) — every unit has a positive probability of each treatment value (p. 449)
- [[lasso-text-adjustment]] (new) — Lasso on words with unpenalized treatment, then regression on selected words (p. 451)
- [[double-selection-lasso]] (new) — Lasso for outcome and for treatment, then adjust for the union of selected variables (p. 452)
- [[topic-proportion-controls]] (new) — topic shares per document used as low-dimensional controls (p. 452)
- [[tirm]] (new) — STM-based matching on topics plus a sufficient-reduction treatment score (p. 457)
- [[text as data / validation]] — here, reading matched document pairs to judge whether they are plausible counterfactuals (p. 456)

## Canonical instances
- [[maliniak-gender-citation]] — gendered citation bias in IR, with text confounding via topic and method (p. 447)
- [[tirm-ir-application]] — 3,201 articles, 15 topics, 6.5 fewer citations for women's articles (pp. 450, 458)
- [[matched-pairs-table-27-1]] — three treated/control pairs of abstract or introduction excerpts for manual validation (pp. 456–457)

## Bridges (candidates)
- [structural-analogy] TIRM's treatment projection ↔ causal inference: propensity score — a low-dimensional score for treatment likelihood used for matching
- [structural-analogy] Lasso selecting predictive words that are not necessarily confounders ↔ regression: omitted-variable bias — selecting controls by outcome fit alone can miss treatment-related confounders
- [metaphor] Reading matched pairs ↔ text as data: validation — human judgment checks the automated measure

## Questions this raises
- When topics or projections are estimated from the same data, how much does that estimation error affect the causal estimate?
- How could positivity be checked or restored when text is high-dimensional?
- Could the Lasso and TIRM approaches be compared on data where hand-coded controls provide a benchmark?

## Reading notes
- Printed page = pdf page.
- Page 453 has only the page number in the text layer, and no image was supplied. Figure 27.1 (Lasso output) is therefore unseen, and the Lasso results are reported from the prose. The pdf 454 image shows the topic-control figure (Fig. 27.2). Its female coefficient reads by eye as roughly −10, but the text only says it is "similar" to the Lasso's.
- Assumption 2 prints $g(W_i,\ )$ with a blank symbol after the comma, in both the text layer and the image.
- Misprint: the text on p. 458 says "Figure 27.1 comprises example matched pairs". It should be Table 27.1, which is on pp. 456–457.
- Typo on p. 459: "casual inference" for "causal inference".
- The unit has no exercises.
