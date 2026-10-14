---
id: grimmer-2022-textasdata/ch11-discriminating
work: grimmer-2022-textasdata
unit: Chapter 11. Discriminating Words
pages: 188-202
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
# Discriminating Words

## L0 — One line
Words that characterize a known group of documents can be found with several measures (mutual information, Fightin' Words, prediction-based scores), but all must trade off distinctiveness against prevalence, so there is no single best method.

## L1 — The gist (≤ 120 words)
Given documents already sorted into categories (party, gender, organization), which words best characterize each category? The chapter presents three families of answer: mutual information, the Fightin' Words standardized log odds, and "fictitious prediction" methods (standardized regression and χ² statistics, multinomial inverse regression). Each is run on Nelson's feminist-organization corpus. They give related but different word lists. The core tension is distinctive-between-groups versus prevalent-within-group; chance-rare words can look distinctive, so measures use regularization (shrinking toward a common value) or standardization. Because prediction is only a device, accuracy alone cannot validate the lists; subject-matter judgment is needed. The lists are tools for discovery and for interpreting clusters found later.

**Prerequisites:** multinomial and Dirichlet-prior word model (Ch. 6); entropy and conditional probability; OLS regression and test statistics; log odds; idea of shrinkage/Lasso.

## L2 — Key ideas
- Discriminating-word methods take existing categories (observed or learned) and find words that convey each category's distinct content; they help interpret newly found organizations of text (p. 188).
- Core tension: words distinctive between groups versus words prevalent within a group. Each way of trading these off defines "discriminating" differently (pp. 188–189).
- Mutual information measures how much knowing a word reduces uncertainty about the category. It is unsigned, ignores estimation uncertainty and uses only presence/absence (pp. 190–191).
- Fightin' Words smooths the multinomial word probabilities and divides the log odds ratio by an approximate variance-based scale. Rare words are shrunk toward the average (pp. 193–195).
- Fictitious prediction: the label is already known, but prediction methods are reused because they can more easily handle continuous labels and other complex settings. Good predictive accuracy is insufficient to show that the word list is accurate (p. 196).
- Without regularization, rare words that fall in one group by chance look discriminating. Correlated traits can also be mistaken for the category (Taddy's public-lands example) (pp. 196–197).
- Standardized regression test statistics and χ² statistics scale by variance but are not explicitly regularized, so the authors turn to MNIR (with a Gamma-Laplace prior), which regularizes; on Nelson's data MNIR returns much rarer words (pp. 197–201).
- There is no optimal prevalence–distinctiveness trade-off and no single best method (p. 202).

## L3 — Walkthrough

### Introduction (pp. 188–189)
- The methods find words that convey the distinct content of an observed category (gender, partisanship, ideology) or a learned category (clusters, next chapter). Unlike the later methods in this part, a set of categories is assumed to exist already (p. 188).
- Typical use: how Republican and Democratic rhetoric in Congress differ (Monroe et al. 2008; Gentzkow, Shapiro, Taddy 2019). Other applications: ideology, gender, geography (p. 188).
- Appeal: group-specific language is thought to indicate the group's arguments or frames. Results can validate intuition and also surprise (p. 188).
- Tension: distinctive between groups versus prevalent within the group. Approaches focus on distinctiveness but need some attention to prevalence so words still represent the group. Different trade-offs give different definitions and results (pp. 188–189).
- Plan: mutual information, then Fightin' Words (multinomial model of Ch. 6), then predictive models of group labels. These are *fictitious prediction problems*: the label is known by construction, and the goal is to find the words that predict it best (p. 189).
- Running example (Nelson 2020): documents from four women's organizations: Hull House (first wave, Chicago), Heterodoxy (first wave, New York), CWLU (second wave, Chicago), Redstockings (second wave, New York). Nelson infers that both Chicago groups focused on concrete policies (education, medicine, abortion access) and both New York groups on abstract, general ideas. She validates with topic models and close reading (p. 189).
- Features may be n-grams or phrases rather than single words. Phrases are rarer but can be substantially more informative (p. 189).

### 11.1 Mutual information (pp. 190–191)
- Setup: $y_i \in \{1,\dots,K\}$. Mutual information (MI) is an unsigned measure of how strongly a word relates to a category. It asks how much the presence or absence of word $j$ helps in guessing a random document's category (p. 190).
- $\pi_k$ = proportion of documents in category $k$; $\pi_{-k}=1-\pi_k$. Entropy (uncertainty about the guess):
$$H(k) = -\pi_k \log_2 \pi_k - \pi_{-k}\log_2 \pi_{-k} \tag{11.1.1}$$
It is 0 if every document is in $k$, and maximal when $\pi_k=\pi_{-k}$ (p. 190).
- $\pi_{k,j}$ = proportion of documents that are both in category $k$ and have word $j$; $\pi_{k|j}$ = proportion in category $k$ among documents containing $j$. Conditional entropy (as printed):
$$H(k\mid j) = -\sum_{k,-k}\sum_{j,-j} \pi_{k,j}\log_2 \pi_{k|j}$$
The source explains that $\sum_{k,-k}$ sums over documents in $k$ and not in $k$; the second sum over $j,-j$ is not explained on the page (presumably word present/absent; my reading) (p. 190).
- If a word perfectly predicts the category, $H(k|j)$ goes to zero. If a word is orthogonal to the category, $H(k|j)$ just returns $H(k)$ (pp. 190–191). Hence
$$MI_{kj} = H(k) - H(k\mid j).$$
It is maximal when the word perfectly predicts the category and zero when the word has no predictive power. Repeating over all categories and words gives a top-MI list per category (p. 191).
- Comparison with Nelson: she ranks words by the difference in the proportion of use between organizations (left half of Table 11.1, replicated with slightly different preprocessing). The difference-in-proportions columns show Chicago groups with *work, classes, school, medical* and New York groups, especially Redstockings, with *consciousness, theory, revolution, political*. MI shows a similar pattern, which "perhaps even" centers more clearly the abstract words of Heterodoxy, such as *suffrage* and *liberty* (pp. 191–192).
- Limits: MI ignores uncertainty in estimating the probabilities and counts only whether a word appears, discarding repeated use. A fully probabilistic model addresses both (p. 191).

*Intuition note.* MI asks: if I tell you a word is in the document, how much less unsure are you about its group? It does not tell you which direction the word points, and it does not know whether the probabilities rest on few or many observations.

### 11.2 Fightin' Words (pp. 193–195)
- Monroe, Colaresi and Quinn (2008) start from Nelson's difference in proportions and add pieces one at a time. By modeling word use probabilistically they can account for the different uncertainty of words with different frequencies. They also add explicit *regularization*, meaning shrinking estimates toward a common value. Common words can move away from it if truly distinctive. Rare words used occasionally are shrunk toward the average (p. 193). The chapter's authors say regularization is essential and will recur in later methods (p. 193).
- Notation: $n_k=\sum_{j=1}^J\sum_{i=1}^N I(y_i=k)W_{ij}$ (tokens in category $k$); $W^*_{jk}=\sum_{i=1}^N I(y_i=k)W_{ij}$ (uses of word $j$ in category $k$). Regularized estimate:
$$\hat\mu_{jk} = \frac{W^*_{jk}+\alpha_j}{n_k+\sum_{j=1}^J \alpha_j} \tag{11.2.1}$$
$\alpha_j$ is a small smoothing value. This equals the posterior mean of a Dirichlet–multinomial model: $\mu\sim\text{Dirichlet}(\alpha)$, $W^*_{k\cdot}\sim\text{Multinomial}(n_k,\mu_k)$ (p. 193).
- Log odds ratio of word $j$ in group $k$ versus the other groups (p. 194):
$$\text{log odds ratio}_{kj}=\log\frac{\hat\mu_{kj}}{1-\hat\mu_{kj}}-\log\frac{\hat\mu_{-kj}}{1-\hat\mu_{-kj}}$$
- Approximate variance (p. 194):
$$\mathrm{Var}(\text{log odds ratio}_{kj}) \approx \frac{1}{W^*_{kj}+\alpha_j}+\frac{1}{W^*_{-kj}+\alpha_j}$$
- Standardized measure, their suggested separation score (p. 194):
$$\text{Std. Log Odds}_j=\frac{\text{log odds ratio}_{kj}}{\sqrt{\mathrm{Var}(\text{log odds ratio}_{kj})}} \tag{11.2.2}$$
(The square root is my reading; see Reading notes.)
- Result (Table 11.2): the Chicago/New York contrast reappears. Hull House gets *club, school, classes*. CWLU gets *center, children, union, health, medical*. Redstockings gets *radical, feminist, oppression, consciousness, theory* (p. 194). This formulation both regularizes and standardizes for estimation uncertainty (p. 195).
- Limit: it is hard to apply to a continuous category such as speaker ideology. This motivates fictitious prediction problems (p. 195).

*Intuition note.* A word seen twice in one group and never in the other has a big raw ratio but a huge variance. Dividing by the variance-based scale downweights it. A frequent word with a moderate ratio gets a precise estimate and can rank higher.

### 11.3 Fictitious prediction problems (pp. 196–197)
- Distinctiveness is measured within a prediction problem that is never of direct interest (e.g., predicting party of members of Congress, who self-identify). The fiction lets researchers reuse prediction methods that handle continuous labels or complex settings. The premise is that a word useful for predicting the outcome is also discriminating in a way useful for discovery (p. 196).
- Consequence: good predictive performance is insufficient to show that the words accurately distil a group's rhetoric. Cross-validation is less useful here, because one might prefer a less predictive model that better identifies category-indicative words. Validation is indirect and needs subject-matter expertise (p. 196).
- Risk: other document characteristics correlated with the category can be picked up. Taddy (2013) found that national-park words came out as "Republican" words because many Republicans represent states with large public lands, though these debates are not particularly partisan. The authors connect this to the role of theory: a rigorous conception of partisanship is needed to contextualize what is found (pp. 196–197).
- The tension again: words that distinguish categories may differ from words indicative of a category. Taddy recommends including covariates but raises the question of which covariates to include and why (p. 197).
- Regularization as protection against overfitting: any word spoken once perfectly classifies its speaker's party, regardless of content. The problem persists after removing once-only words, since rare words may fall in one group solely by chance. Then the list contains words that merely align with the categories (p. 197).

#### 11.3.1 Standardized test statistics (pp. 197–198)
- $y_i$ may be continuous or categorical (for a category, use a dummy for membership in $k$). Regress one word at a time:
$$y_i=\mu_0+\mu_{1j}W_{ij}+\varepsilon_i$$
Test $H_0:\mu_{1j}=0$ and use the statistic as the separation score:
$$\text{Standard}_j=\frac{\hat\mu_{1j}}{\widehat{SE}(\hat\mu_{1j})}$$
- Larger (more positive) means more discriminating, scaled by the coefficient's variance. Under the null, a larger statistic corresponds to a lower p-value (p. 198).
- Table 11.3: Chicago groups get event-related words (*attendance, music, entertainment*). Redstockings gets words like *analyzing, thinking, evaluating* (p. 198).

#### 11.3.2 χ² statistics (p. 198, continued p. 200)
- Gentzkow and Shapiro (2010) use a χ² statistic testing equal distribution across categories. Two-category case: $W^*_{j1}$ = times group 1 uttered word $j$; $W^*_{-j1}=\sum_{m\ne j}\sum_i W_{im}I(y_i=1)$ = words other than $j$ uttered by group 1; $W^*_{j0}$, $W^*_{-j0}$ analogously (p. 198). As printed:
$$\chi^2_j=\frac{W^*_{j1}W^*_{-j1}-W^*_{j0}W^*_{-j0}}{(W^*_{j1}+W^*_{j0})(W^*_{j0}+W^*_{-j0})(W^*_{j1}+W^*_{-j1})(W^*_{-j1}+W^*_{-j0})}$$
(see Reading notes on the layout and numerator.)
- It finds words used disproportionately by group 1 or 2, consistent with a lower p-value under equal use (p. 200).
- Worry for both z-type and χ² scores: a rare word that happens to separate groups may be confused with a regularly used word that systematically differs. Manual frequency thresholds are hard to set. Instead use regularizing models whose shrinkage depends on the information in the data: rare coincidental words are smoothed toward the common value; regularly used, distinguishing words are shrunk only a little (p. 200).

#### 11.3.3 Multinomial Inverse Regression (pp. 200–201)
- Regressing the label on all $J$ words at once is problematic: coefficients are not identified if $J>N$, and estimates may be noisy even if computable. Section 11.3.1 avoided this by adding one word at a time (pp. 200–201).
- Taddy (2013) *inverts* the regression: features are regressed on $y_i$, which allows continuous $y_i$ and does a regularization job like Fightin' Words (p. 201):
$$W_{i\cdot}\sim\text{Multinomial}(n_i,\theta_i),\qquad \theta_{ij}=\frac{\exp(\mu_{0j}+\mu_{1j}y_i)}{\sum_{l=1}^J\exp(\mu_{0l}+\mu_{1l}y_i)} \tag{11.3.1}$$
- Chance differences from rare words are handled with a Gamma-Laplace prior, whose regularization is related to Lasso. The estimated coefficients $\mu_{1j}$ serve as word separation measures (p. 201).
- Table 11.4: the lists differ dramatically. The words are substantially rarer (many names and rare terms, e.g., *addams, gymnasium, sanger, hanisch, belmont*) but still reflect robust group differences and Nelson's theory. Heterodoxy's abstract concerns are clearer than in prior lists (pp. 199–201).

*Intuition note.* Flipping the regression means the word counts are the outcome and the label $y_i$ is the predictor, which also allows continuous $y_i$. The Gamma-Laplace prior regularizes (related to Lasso) so that rare, chance differences in word use are not over-read; the text does not say how MNIR handles $J>N$.

### 11.4 Conclusion (p. 202)
- Discriminating-word lists can spark ideas about how communities use language, to be confirmed by deeper reading (p. 202).
- There is no optimal trade-off between prevalence and distinctiveness, so no single best method. The chapter's methods gave different views of Nelson's corpus (p. 202).
- Essentially any supervised learning method can generate such labels, and techniques exist for simple summaries of complex predictive models (Ribeiro et al. 2016). The tools will help to label and interpret clusters, topic models and embeddings in the next three chapters (p. 202).

## Toy example (ours, not from the text)
Two groups A and B, 1,000 tokens each. Vocabulary: "rare", "common", "other" ($J=3$). Counts: A: rare 2, common 60, other 938; B: rare 0, common 40, other 960. Use $\alpha_j=1$, so $\sum\alpha_j=3$ and denominators are 1003.

**Rare.** $\hat\mu_A=3/1003$, odds $=3/1000=0.0030$. $\hat\mu_B=1/1003$, odds $=1/1002=0.000998$. Log odds ratio $=\ln(0.003\times1002)=\ln 3.006=1.101$. Variance $=1/(2+1)+1/(0+1)=1.333$, so sd $=1.155$. Standardized $=1.101/1.155=0.95$.

**Common.** $\hat\mu_A=61/1003$, odds $=61/942$. $\hat\mu_B=41/1003$, odds $=41/962$. Ratio $=(61\times962)/(942\times41)=58682/38622=1.519$, so log $=0.418$. Variance $=1/61+1/41=0.0164+0.0244=0.0408$, so sd $=0.202$. Standardized $=0.418/0.202=2.07$.

Raw log odds ranks "rare" first (1.10 vs 0.42). Standardizing reverses this (0.95 vs 2.07). Without smoothing, "rare" would have B-odds 0 and an infinite ratio, the perfect-classifier trap of p. 197.

## Concepts
- [[discriminating-words]] (new) — words that convey the distinct content of a category of documents (p. 188)
- [[distinctiveness-prevalence-tension]] (new) — words distinctive between groups versus frequent within a group; defines the choice of measure (pp. 188–189)
- [[mutual-information]] (new) — $H(k)-H(k|j)$: how much a word's presence reduces category uncertainty; unsigned (pp. 190–191)
- [[fightin-words]] (new) — Monroe–Colaresi–Quinn standardized log odds from a smoothed multinomial model (pp. 193–194)
- [[regularization]] (new) — shrinking estimates toward a common value so rare words are not over-read (p. 193)
- [[fictitious-prediction-problem]] (new) — predicting an already known label only to find the best-predicting words (pp. 189, 196)
- [[multinomial-inverse-regression]] (new) — regress word counts on the label with a Gamma-Laplace prior; handles continuous $y_i$ (p. 201)
- [[text-as-data-validation]] — here validation is indirect and needs subject expertise; predictive accuracy alone is insufficient (p. 196)

## Canonical instances
- [[nelson-feminist-organizations]] (new) — four organizations in Chicago and New York; concrete versus abstract language (pp. 189–202)
- [[taddy-public-lands-words]] (new) — national-park words labelled Republican because of correlated state characteristics (pp. 196–197)
- [[congress-partisan-language]] (new) — Republican/Democrat rhetoric as the standard application (pp. 188, 196)

## Bridges (candidates)
- [structural-analogy] Shrinkage of rare-word scores ↔ statistics: Lasso-type regularization — the chapter links MNIR's Gamma-Laplace prior to Lasso.
- [same-math] Smoothed word probability (11.2.1) ↔ Bayesian estimation: Dirichlet–multinomial posterior mean — the text states the equality.
- [structural-analogy] Confounded discriminating words (national parks) ↔ causal inference: omitted correlated covariates — both concern a correlate being mistaken for the target.
- [metaphor] Fictitious prediction ↔ any "proxy task" used only for its by-product (the word weights).

## Questions this raises
- How should one choose the covariates to include so that "partisan" words are not just "state-characteristic" words?
- How much smoothing ($\alpha_j$) or shrinkage is appropriate, and how sensitive are the word lists to it?
- What counts as validating a word list when predictive accuracy is not the criterion?
- Would n-gram features sharpen the Nelson contrasts, as suggested on p. 189?

## Reading notes
- Printed = pdf page numbers (188–202).
- The text layer of the equations is garbled. I checked the images: equations are rendered in flat text with no visible fraction bars or roots.
- (11.2.2): the image shows the numerator and "Var(...)" side by side in flat text, with no visible fraction bar or square root. I wrote $\sqrt{\mathrm{Var}}$ because the text says "standardize" using the variance; flagged as my reading.
- χ² formula (p. 198): the image shows numerator $W^*_{j1}W^*_{-j1}-W^*_{j0}W^*_{-j0}$, with no visible square. I copied it as printed and did not check it against any other source. In the definition of $W^*_{-j1}$ the source has no star, while the formula uses stars. Also, $W^*_{j1}$ is defined with $W^*_{ij}$ (a starred term inside the sum), probably meant as $W_{ij}$.
- $H(k|j)$ has no equation number in the source.
- Table bodies (11.1–11.4) are summarized by representative words only. Footnote 1 (p. 202) says the replication uses slightly different preprocessing from Nelson, with unchanged substantive results. The source uses both "Hullhouse" and "Hull House".
