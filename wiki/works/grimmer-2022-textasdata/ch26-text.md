---
id: grimmer-2022-textasdata/ch26-text
work: grimmer-2022-textasdata
unit: "Chapter 26. Text as Treatment"
pages: 436-446
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Text as Treatment

## L0 — One line
When the treatment is a text, we must learn which latent features of the text matter, and randomising texts identifies their effects only under extra assumptions about the features we did not measure.

## L1 — The gist (≤ 120 words)
Chapter 26 asks how to estimate the causal effect of a feature of a text (for example, a negative attack in an ad) when each text bundles many features. The answer follows Fong and Grimmer. Learn binary latent treatments from the text with a supervised model on a training set, then estimate effects on a held-out test set. Randomising texts is not enough. The authors give two sufficient conditions: the measured and unmeasured treatments are independent, or the unmeasured ones have no average effect. Two survey experiments illustrate this: Trump tweets and candidate biographies. They show that attacks and legal experience lower ratings, while military experience raises them.

**Prerequisites:** potential outcomes and ATE; randomisation; SUTVA, ignorability, positivity (Ch. 24–25); topic models; train/test split; regression.

## L2 — Key ideas (5–10 bullets)
- Text as treatment: the treatment is a latent feature of the text, mapped from the text by $g$. It is not the text itself, as in A/B testing, which compares two fixed texts (p. 436).
- Texts carry many features at once, so the treatment is multidimensional. The authors use $K$ binary indicators, giving $2^K$ treatment vectors, rather than topic proportions, which sum to 1 on a simplex (p. 437).
- A second function $h$ stands for unmeasured treatments $b_i$. The ATE averages over their distribution, under an exclusion restriction: the text affects responses only through the measured and unmeasured treatments (p. 437).
- Identification needs SUTVA, ignorability and positivity, plus a sufficiency condition: independence of measured and unmeasured treatments, or no average effect of the unmeasured ones (pp. 437–438).
- Randomising the texts alone is not enough; the extra assumption can be hard to meet even in vignette experiments, where analysts control the document contents (p. 438).
- Trump tweets: the supervised Indian Buffet Process (SIBP) found five treatments. Attacks on Clinton and the media, and the healthcare treatment, lowered ratings. Controlling for sentiment did not change the results (pp. 439–441).
- Biographies: ten treatments were found. Political and legal experience lowered thermometer ratings; advanced degrees and military experience raised them (pp. 444–445).
- Design choices: sample splitting, distinct texts per respondent to avoid aliasing (perfectly correlated treatments), and no-interaction assumptions (pp. 439, 443–444, 446).

## L3 — Walkthrough

### Setup (pp. 436–437)
**Running example.** The effect of a negative campaign ad, compared with an ad without an attack, on turnout. The treatment is the ad text $t_i$. The potential outcome $y_i(t_i)$ is respondent $i$'s turnout decision (p. 436).

**Why not A/B testing?** Comparing two ads is A/B testing. Social scientists usually want the effect of an underlying latent value of the text, here "contains an attack". An attack can appear in many forms. The alternative is to assign many different ads and map each text to the feature of interest, $\pi_i = g(t_i)$, following Egami et al. (2018) (p. 436).

The estimated ATE is a difference of means in the test set $O$ (the original prints this with garbled brackets; the indicator is written $\mathbb 1(\pi_i = g_I(t_i)=\cdot)$):
$$\widehat{ATE}=\frac{\sum_{i\in O}\mathbb 1(\pi_i=g_I(t_i)=1)\,y_i(1)}{\sum_{j\in O}\mathbb 1(\pi_j=g_I(t_j)=1)}-\frac{\sum_{i\in O}\mathbb 1(\pi_i=g_I(t_i)=0)\,y_i(0)}{\sum_{j\in O}\mathbb 1(\pi_j=g_I(t_j)=0)}\tag{26.0.1}$$
The subscript $I$ means $g$ was developed in the training set. $O$ means the ATE is estimated in the test set (pp. 436–437).

**Multidimensional treatment.** We will rarely be able to design texts so that the only relevant feature is the treatment of interest. Ads also carry candidate information, economic emphasis, tone and format. A topic model is hard to use here because topic proportions lie on a simplex (each $\pi_i$ sums to 1). So $g$ maps $t$ to a length-$K$ binary vector, $\pi_{ik}=1$ if unit $i$ contains treatment $k$, giving $2^K$ possible vectors (p. 437).

**Unmeasured treatments.** Fong and Grimmer (2021) add a function $h$ with $h(t_i)=b_i\in\mathcal B$, a vector of binary treatments not explicitly represented. $g$ and $h$ are deterministic (the page says "functions of the treatments"). Random assignment of documents still creates a joint distribution $p(\pi_i,b_i)$ (p. 437).

**Exclusion restriction.** Text affects responses only through the observed and unobserved treatments:
$$y_i(t_i)=y_i(g(t_i),h(t_i),t_i)=y_i(g(t_i),h(t_i)).$$
With one binary treatment of interest $\pi_i\in\{0,1\}$, the ATE is (the page prints the brackets loosely; the sum is over the difference):
$$ATE=\sum_{b\in\mathcal B}\big(E[y_i(\pi_i=1,b_i=b)]-E[y_i(\pi_i=0,b_i=b)]\big)\Pr(b_i=b).$$
(p. 437)

**Identification.** Beyond SUTVA, Ignorability and Positivity (Ch. 24–25), Fong and Grimmer give two sufficient assumptions (p. 437). Positivity here means $f(\pi_i)>0$ for all $\pi_i\in\text{Range}\,g(\cdot)$ (fn. 1, p. 446).

**Assumption 1 (Sufficiency).** Either:
1. Measured and unmeasured treatments are independent: $p(\pi,b)=p(\pi)p(b)$.
2. Unmeasured treatments are unrelated to the outcome on average: $E[y_i(\pi,b)]=E[y_i(\pi,b')]$ for all $b,b'\in\mathcal B$ (p. 438).

The authors liken (1) to assuming the effect is independent of unmeasured confounders. They liken (2) to a confounder unrelated to the outcome. An identification proof is in Fong and Grimmer (2021, 2016) (p. 438).

**Consequence.** Randomising the texts alone is insufficient to identify causal effects. For the ad example, other features (information, topics, even font) must be independent of the attack or have no effect on the outcome. This is hard to satisfy even in vignette experiments where the analyst controls the content (p. 438). (The source calls this "Assumption 4"; see Reading notes.)

*Intuition note:* A text is a bundle. If the bundle's other parts travel with the feature we study and also move the outcome, we may credit the feature with their effect. Randomising whole texts does not break this link.

### 26.1 An experiment using Trump's tweets (pp. 439–441)
**Data and method.** Fong and Grimmer (2021) use a 2017 YouGov survey in which respondents rate random Trump tweets as "Great", "Good", "OK", "Bad" or "Terrible" (p. 439). They apply the supervised Indian Buffet Process (SIBP) of Fong and Grimmer (2016). It is a supervised topic model that finds topics related to the outcome. Instead of LDA proportions, it gives a binary vector marking whether each topic is present in each document (p. 439).

**Split.** One-third of the data is the training set and two-thirds the test set. The split lets the authors search over models before settling on a treatment measure (p. 439).

**Treatments (Table 26.1, p. 440).** The authors read the top words as follows (p. 439):
- T1: attacks on Hillary Clinton and the media.
- T2: strong economic performance.
- T3: repealing and replacing the Affordable Care Act.
- T4: the First Lady and the NFL anthem controversy.
- T5: the stock market and North Korea.

**Estimates (Table 26.2, p. 440).** The authors regress favourability on the treatments separately for Democrats (columns 1–2), Independents (3–4) and Republicans (5–6) (N = 752 each). Odd columns omit and even columns include a positive-sentiment control. Attacks on Clinton and the media (T1) are rated negatively by all three groups, e.g. $-45.22$ (s.e. 5.18) for Democrats and $-18.91$ (3.27) for Republicans in the columns without the sentiment control (p. 440). The authors write that touting the economy (they say treatments 2 and 4) is evaluated positively in all groups (p. 439).

**Assumption checks.**
- SUTVA might fail because subjects probably saw other Trump tweets in 2017 (p. 440).
- Random assignment is more plausible, since YouGov controlled assignment (p. 440).
- For the unmeasured-treatment condition, a possible violation is sentiment: T1 and T3 may be more negative. A sentiment dictionary shows sentiment is related to the treatments. Adding it as a confounder in Table 26.2 does not change the results (p. 441).

*Intuition note:* The authors test the weak point directly. They name a plausible hidden feature (sentiment), measure it, and check whether adjusting for it moves the estimates. It does not.

### 26.2 A candidate biography experiment (pp. 442–445)
**Motivation.** A large literature asks how voters judge candidates' characteristics. In survey experiments, researchers manipulate some feature of the text, for example a biography that alters occupation, or run a conjoint study that varies several features (p. 442).

**Design (Fong and Grimmer 2016).**
- They collect 1,246 Congressional candidate biographies from Wikipedia and anonymise them, so only information in the text reaches respondents (p. 443).
- A condition for this experiment to uncover latent treatments is that every treatment vector has nonzero probability, which the authors say is equivalent to assuming no treatments are *aliased* (perfectly correlated). Aliasing is more likely with few distinct texts, so each respondent gets a distinct biography in each round (p. 443).
- Respondents rate up to four biographies, 2.8 on average, on a 0–100 feeling thermometer (cold to warm). Multiple evaluations are problematic if there is spillover across rounds; the authors see little reason to expect systematic spillover (p. 443; fn. 3, p. 446).
- The sample has 1,886 SSI participants, census-matched on sex, age, race and education, and 5,303 observations. There are 2,651 responses in the training set and 2,652 in the test set (p. 443).
- The thermometer is standardised to mean 0 and sd 1. $K=10$ was chosen after a quantitative and qualitative search over $K$, and the final model was chosen by varying parameters and evaluating the CE score (p. 443). The CE score is not defined in this unit.

**Treatments (Table 26.3, p. 442).** Ten were discovered. Examples: T6 and T10 are military experience; T5 and T7 previous political experience; T3 and T9 education (p. 443–444). The authors say many background features are missing but the dimensions are useful (p. 444).

**Estimation.** The model is applied to the test set to infer treatments. The authors assume no interactions between treatments. Interactions could be modelled, but this would need much stronger parametric assumptions (fn. 4, p. 446). The confidence intervals (Figure 26.1) account for uncertainty in inferring treatments from text and in their relation to the response. The mean thermometer is 62.3 (p. 444).

**Results (p. 445).**

| Treatment | Content | Effect | 95% CI |
|---|---|---|---|
| T5 | previous political experience | −2.26 | [−4.26, −0.24] |
| T9 | legal experience | −2.34 | [−4.28, −0.29] |
| T3 | advanced degrees | +2.43 | [0.49, 4.38] |
| T6 | military record | +3.21 | [1.34, 5.12] |
| T10 | military | +4.00 | [1.53, 6.45] |

The dislike of lawyers is not a dislike of education (T3 is positive). The authors say the military bonus is consistent with the intuition that the public supports veterans (p. 445).

*Intuition note:* The model proposes the features and the held-out data measures their effects. The effects are estimated on the test set, which is separate from the training set used to discover the features (pp. 437, 439, 444).

### 26.3 Conclusion (p. 446)
Unlike text as outcome, the goal is to identify latent treatments and estimate their impact. The next chapter uses text to measure and condition on confounding (p. 446).

## Toy example (ours)
Eight ads. $\pi$ = negative attack. $b$ = mentions the economy (unmeasured). Suppose the outcome is $y=50-4\pi+6b$. So the true effect of $\pi$ is $-4$ and $b$ also matters, which violates condition 2.

*Dependent case:* among the 4 ads with $\pi=1$, one has $b=1$. Among the 4 with $\pi=0$, three have $b=1$.
- Mean $y$, $\pi=1$: $50-4+6\cdot\tfrac14=47.5$.
- Mean $y$, $\pi=0$: $50+6\cdot\tfrac34=54.5$.
- Naive difference: $47.5-54.5=-7\neq-4$, because condition 1 fails.
- Adjusted as in the ATE formula: within each $b$ the effect is $-4$, and $\Pr(b=1)=4/8=0.5$, so $ATE=0.5(-4)+0.5(-4)=-4$. This needs $b$ observed, which is exactly what is not available in practice.

*Independent case:* two of the 4 ads have $b=1$ in each $\pi$ group. Means are $50-4+3=49$ and $50+3=53$, so the naive difference is $-4$, which is correct.

## Concepts
- [[text-as-treatment]] (new) — the treatment is a latent feature of a text, mapped by $g$; effects are estimated on held-out data (p. 436)
- [[latent-treatment]] (new) — an underlying feature (e.g. "negative attack") that can appear in many textual forms (p. 436)
- [[unmeasured-treatments-h]] (new) — features $b_i=h(t_i)$ not explicitly represented; they jointly vary with $\pi_i$ (p. 437)
- [[exclusion-restriction-text]] (new) — text affects outcomes only through $g(t)$ and $h(t)$ (p. 437)
- [[sufficiency-assumption]] (new) — either measured and unmeasured treatments are independent, or unmeasured ones have no average effect (p. 438)
- [[supervised-indian-buffet-process]] (new) — supervised topic model giving binary topic-presence vectors related to the outcome (p. 439)
- [[aliasing]] (new) — treatments perfectly correlated, violating positivity (p. 443)
- [[feeling-thermometer]] (new) — 0–100 warmth rating used as the outcome (p. 443)
- [[text-as-data-validation]] — here shown as a train/test split: discover on training, estimate on test (p. 439)

## Canonical instances
- [[negative-ad-turnout-example]] — running example of a text-defined treatment (p. 436)
- [[trump-tweets-experiment]] — attacks and healthcare tweets lower ratings across partisan groups (pp. 439–441)
- [[candidate-biography-experiment]] — legal and political experience penalised, military and advanced degrees rewarded (pp. 442–445)

## Bridges (candidates)
- [structural-analogy] Unmeasured treatments $b$ ↔ causal inference: omitted confounders. The author draws this analogy, but here $b$ is part of the same randomised text (p. 438).
- [structural-analogy] Aliasing ↔ experimental design: non-positivity in conjoint designs (Hainmueller et al.) (p. 443).
- [metaphor] Discovering latent treatments ↔ political-science measurement: first discover the dimensions, then test their effects (pp. 439, 443).

## Questions this raises
- How can a researcher tell whether the unmeasured treatments are independent of $\pi$ or irrelevant, beyond checking one named candidate such as sentiment?
- How sensitive are the estimates to the choice of $K$ and to the labels researchers give to topics from their top words?
- What would be needed to estimate interactions between discovered treatments?
- Does a distinct text per respondent solve aliasing, or just make it less likely?

## Reading notes
- Printed page numbers are visible and equal the pdf numbers (436–446).
- The text calls the sufficiency assumptions "Assumption 4" (pp. 438, 441), but the box is labelled "Assumption 1 (Sufficiency)". This looks like a numbering slip.
- The text layer garbles Eq. (26.0.1) and the ATE formula; the images show the notation (including an extra closing bracket after $y_i(1)$). I wrote the formulas in standard form from the visible structure.
- Page 439 says the SIBP seeks topics related to "the timeliness of the response", but the outcome is a favourability rating. This seems an error.
- Page 439 says treatments 2 and 4 are about the economy, but Table 26.1 and the same page describe T4 as the First Lady and NFL protests, and T5 as the stock market.
- In Table 26.2, T2 for Democrats is $10.59$ (s.e. $8.91$), so it is not clearly positive on its own.
- The CE score is used without definition on p. 443.
