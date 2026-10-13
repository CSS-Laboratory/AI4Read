---
id: argyle-2023-silicon/main-p1
work: argyle-2023-silicon
unit: "paper (part 1/2): Abstract, §§1–9, Appendix A, Appendix B (B.1–B.3)"
pages: 1–29
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Out of One, Many: Using Language Models to Simulate Human Samples (part 1/2)

## L0 — One line
The authors argue that GPT-3, conditioned on first-person demographic backstories from real survey respondents, produces "silicon samples" whose response patterns closely match those of matching human subgroups in U.S. politics (which they call *algorithmic fidelity*).

## L1 — The gist (≤ 120 words)
The paper asks whether a language model can serve as a proxy for human survey respondents. The authors treat GPT-3's "algorithmic bias" as many demographically specific response distributions, not one uniform bias. They call the accuracy of those distributions *algorithmic fidelity* and propose four criteria for it. They condition GPT-3 on backstories taken from real surveys ("silicon sampling"). In three studies on U.S. politics (partisan word lists, vote choice, associations among survey items), GPT-3 output matches human data closely, with exceptions such as pure independents. They suggest piloting studies cheaply on silicon samples before human data collection, and they warn about misuse.

**Prerequisites:** conditional probability and marginalisation; what a language model and its sampling temperature are; OLS regression, fixed effects, clustered standard errors; correlation measures for binary and categorical data.

## L2 — Key ideas (5–10 bullets)
- **Algorithmic fidelity:** the degree to which relationships among ideas, attitudes and socio-cultural contexts inside a model mirror those in human sub-populations. The core assumption is that outputs come from a mixture of many distributions, not one (p. 4).
- **Four minimal criteria:** Turing test, backward continuity, forward continuity, pattern correspondence. The authors give no numeric thresholds. They propose repeated support across data sources, measures and groups as the standard (pp. 4–5).
- **Silicon sampling:** take backstories from a representative human sample (e.g., the ANES, the American National Election Studies, a large U.S. survey) and let the model answer for each. This corrects the model's skewed backstory distribution, provided the model gets P(V|B) right (the probability of a vote given a backstory) (p. 5).
- **Study 1:** evaluators could not tell human from GPT-3 word lists (61.7% vs 61.2% judged human). They rated the content similarly, but guessed the writer's party less often for GPT-3 lists (52.8% vs 60.1%) (pp. 8–9).
- **Study 2:** GPT-3 vote choice correlates highly with ANES vote in 2012, 2016, 2020 (tetrachoric correlation, a correlation measure for two yes/no variables: 0.90, 0.92, 0.94). Pure independents (respondents with no party lean) are the weak spot (p. 11).
- **Study 3:** Cramér's V (a summary measure of association between survey items) shows the same pattern among items in GPT-3 data as in ANES data; mean difference −0.026. Correspondence is judged at the aggregate level, not the individual level (pp. 12–13).
- **Intended use:** generate hypotheses, pilot question wording, and plan analyses cheaply (Study 1 cost $29) before collecting human data (p. 15).
- **Caveats stated by the authors:** the evidence covers only U.S. politics, and the method could be used for misinformation, manipulation or fraud (pp. 15–16).

## L3 — Walkthrough

### Abstract and §1 Introduction (pp. 1–3)
- **Claim (authors):** language models can be studied as proxies for specific human sub-populations. "Algorithmic bias" is usually treated as one uniform property. The authors say it is instead "fine-grained and demographically correlated", so proper conditioning makes the model emulate response distributions of many subgroups (p. 1).
- Generative language models are "complex conditional distributions over natural language" (p. 2). The authors propose them as surrogates for human respondents (p. 2).
- **Reframing of bias:** the models "do not contain just one bias, but many". Conditioning on simulated individuals with targeted identity profiles selects one of many response distributions, each aligned with a real sub-population (p. 2). The degree to which a model reflects these distributions is its **algorithmic fidelity** (p. 3).
- It matters because one model could then show attitudes of single groups (women, millennials) and intersections (Black immigrants, female Republicans). The authors say the extent of fidelity in large models is "unexplored" (p. 3).
- **Data used:** ANES 2012, 2016, 2020 waves, and Rothschild et al.'s "Pigeonholing Partisans" data. One "silicon subject" is generated per human participant, and each does the same task as its human twin (p. 3).
- **Studies (p. 3):**
  - Study 1: list words describing outgroup partisans.
  - Studies 2 and 3: relationships among demographics, attitudes and reported behaviours.
- The authors say the results suggest that, for U.S. politics, researchers can "confidently" use a silicon sample to explore hypotheses before costly human work (p. 3).
- **Five contributions (p. 3):**
  1. the concept and four criteria;
  2. silicon sampling, which corrects skewed marginals;
  3. first-person demographic backstory conditioning;
  4. evidence of fidelity in GPT-3 for U.S. politics;
  5. examples of research uses.

### §2 The GPT-3 language model (pp. 3–4)
- GPT-3 was released by OpenAI in 2020, with 175 billion parameters and more than 45 TB of training text (p. 3).
- Formally, a language model is a conditional distribution over tokens (units of text), with each $x_i$ drawn from a fixed vocabulary (p. 3):
$$p(x_n \mid x_1,\dots,x_{n-1})$$
- Sampling this repeatedly generates arbitrarily long text. The initial tokens $\{x_1,\dots,x_{n-1}\}$ are the **context**, or conditioning text (p. 4).
- **Example (authors):** for "Can you come" the model may give high probability to "home" and low to "bananas". Changing one word to "Can you eat" reverses that (p. 4).
- At each step the model estimates a distribution over the vocabulary, picks a candidate with a distribution function, appends it, and repeats until a token count or external stop. Because selection is probabilistic, many continuations exist for one context (p. 4).

> **Intuition note.** A language model is a machine for "what comes next, given this text". Changing the earlier text changes the odds of what follows. The whole paper uses this: write a person's background as the earlier text, and read the answer as what that person might say.

### §3 Algorithmic fidelity (pp. 4–5)
- **Definition:** the degree to which the complex patterns of relationships between ideas, attitudes and socio-cultural contexts within a model accurately mirror those within a range of human sub-populations (p. 4).
- **Core assumption:** generated text is drawn from a combination of many distributions, not one. Structured curation of the context can induce outputs that correlate with the attitudes, opinions and experiences of distinct sub-populations (p. 4).
- **Limits stated:** this does not imply the model can simulate a specific individual, or that every response is coherent. Known shortcomings of large models still apply (p. 4).
- **Beyond prior work:** the authors say fidelity goes beyond the observation that models reflect biases in their corpora. It suggests that human-like output "stems from human-like underlying concept associations" (p. 4). In social science terms it bears on *generalizability*, the degree to which what is learned from the models applies to the world beyond them (p. 4).
- **Four criteria**, the minimum a model must repeatedly meet (pp. 4–5):
  1. **Social Science Turing Test:** generated responses are indistinguishable from parallel human texts.
  2. **Backward Continuity:** responses are consistent with the attitudes and socio-demographic information in the conditioning context, so humans viewing them can infer key elements of that input.
  3. **Forward Continuity:** responses proceed naturally from the context, reflecting its form, tone and content.
  4. **Pattern Correspondence:** responses reflect underlying relationships between ideas, demographics and behaviour as observed in comparable human data.
- These are "four qualitatively different dimensions". Lack of fidelity in any one lowers confidence, and in more than one lowers it further (p. 5).
- **No thresholds:** the authors propose no specific metrics or cut-offs, since appropriate statistics depend on data structure and discipline. The best metric is "repeated support for each criteria across multiple data sources, different measures, and across many groups" (p. 5).
- Political science literature on expected relationships among political ideas provides the comparison basis (p. 5).

> **Intuition note.** The criteria ask different questions: does it look human, does it fit the backstory it was given, does it continue the context naturally, and does it reproduce the correlations seen in real data? The last is the one most directly about structure across many respondents.

### §4 Silicon sampling: correcting skewed marginals (p. 5)
- **Problem:** internet users (the training population) are neither representative nor balanced, and the corpus is a snapshot from a fixed time (p. 5).
- GPT-3 models votes $V$ and demographic backstories $B_{GPT3}$ jointly (p. 5):
$$P(V, B_{GPT3}) = P(V \mid B_{GPT3})\,P(B_{GPT3})$$
- The distribution of backstories $P(B_{GPT3})$ does not match the true one $P(B_{True})$. So the marginal over votes, as printed on p. 5,
$$P(V)=\int_B P(V,B_{GPT3}),$$
is skewed by this difference (p. 5).
- **Fix:** sample backstories from a known, nationally representative sample (e.g., ANES) and estimate $P(V)$ from those. This computes $P(V\mid B_{ANES})\,P(B_{ANES})$. "As long as GPT-3 models the conditional distribution $P(V\mid B)$ well", one can explore patterns in any designated population (p. 5).
- **Simpson's paradox analogy (authors):** trends in a combined group may not reflect those of its components. Silicon sampling lets researchers see sub-population patterns that can differ drastically from generic, unconditioned GPT-3 completions (p. 5).
- **Caveat (authors):** being able to sample component distributions does not by itself guarantee they faithfully reflect human subgroups. Fidelity must be examined for the domain and groups of interest (p. 5).

> **Intuition note.** The model's conditional answers can be good even when its picture of "who is out there" is off. So the method takes the "who" from a real survey and only the "what do they say" from the model. The assumption doing the work is that $P(V\mid B)$ is well modelled.

### §5 Study 1: Free-form partisan text (pp. 6–10)
**Design (pp. 6–8)**
- Source data: Rothschild et al.'s "Pigeonholing Partisans" survey, where respondents listed four words describing Republicans and four describing Democrats. Rothschild et al. found people describe partisans through traits, issues, social groups or a mix, and often describe their own party more positively (p. 6).
- One first-person backstory is built per human subject (Figure 1; template details in B.1). GPT-3 then samples the four words. It "almost always" gives neat four-word sets but occasionally gives phrases, mini-essays or nothing. Regular expressions extracted the four words (p. 6).
- **Evaluation:** 2873 Lucid evaluators judged 7675 lists (human and GPT-3 mixed, source unlabelled). Each evaluated 8 random lists, and each list was evaluated by three people (p. 6).
- **Six prompts per list (pp. 6–8):**
  1. guess writer partisanship (Republican, Democrat, Independent);
  2. five ratings: positive/negative tone, extremity, and mentions of traits, policy issues, social groups.
- **Turing task:** evaluators then saw 8 more lists, were told some were computer-generated, and guessed human or computer (pp. 7–8).
- The authors say these tests speak to Criterion 1 and Criterion 2 (p. 8).
- **Figure 2 (qualitative):** most frequent words by source and writer ideology look as political scientists might expect. For example, a common set of words describes Democrats and is rarely used for Republicans (p. 6).

**Results**
- **Turing test (p. 8):** participants guessed 61.7% of human lists were human and 61.2% of GPT-3 lists were human (two-tailed difference p = 0.44). About 40% of both kinds were judged non-human, and this does not vary by source.
- **List characteristics (p. 8):**
  - OLS regressions of each of the 5 characteristics on a source dummy (0 = human, 1 = GPT-3) plus controls (writer's gender, ethnicity, income, age, partisan identity).
  - Evaluator fixed effects; standard errors clustered by evaluator and list.
  - Predicted shares (Figure 3B): lists mentioning traits were 72.3% (human) vs 66.5% (GPT-3); lists judged extreme were 39.8% vs 41.0%.
  - Per the authors, all characteristics hover around 50% except "traits", which is substantially higher in both sources. This matches Rothschild et al.'s original analysis.
  - The authors call the mirroring of that exception "strong evidence of the depth of algorithmic fidelity" (p. 8).
- **Pattern correspondence (p. 8, Fig. 3A):** broken out by writer ideology, positive-word and extreme-word usage is similar for humans and GPT-3. The authors call this Criterion 4 evidence ("striking" similarity).
- **Guessing partisanship (pp. 8–9):**
  - The model regresses a correct-guess indicator on source plus controls.
  - Both sources yield correct guesses significantly above chance (33%).
  - Human lists were guessed correctly 60.1% of the time vs 52.8% for GPT-3. The authors report this as "roughly 7.3% more often", a statistically significant difference (p < .001; this is 7.3 percentage points).
  - Even so, the authors say lists from both sources "clearly contain the sentiment cues" needed to guess the writer's party (pp. 9–10).
- **Summary (p. 10):** "repeated, consistent" support for Criteria 1 and 2, and "some initial evidence" for Criterion 4, across measures and population subsets.

> **Intuition note.** Raters could not detect which lists were machine-made, and they described both sets in nearly the same terms. The clearest gap the authors report is that evaluators identified the writer's party less often from GPT-3 lists (52.8% vs 60.1%). Table 2 (p. 24) also shows non-zero GPT-3 source coefficients for traits (−0.058) and groups (0.078).

### §6 Study 2: Vote prediction (pp. 10–12)
- **Design:** silicon samples built to match the demographics of ANES 2012, 2016 and 2020 participants. GPT-3 must produce a candidate name from a limited set, differently depending on the backstory. The authors say this assesses Criterion 3 (forward continuity) and Criterion 4 (p. 10).
- **Temporal test:** GPT-3's training corpus ended in 2019, so 2020 data probes fidelity outside the training period (p. 10).
- **Conditioning variables (p. 10):**
  1. race/ethnicity;
  2. gender;
  3. age;
  4. conservative–liberal ideology;
  5. party identification;
  6. political interest;
  7. church attendance;
  8. discusses politics with family/friends;
  9. patriotism about the American flag;
  10. state of residence.
  
  Variables 9 and 10 were not available for 2020 at the time of analysis.
- **Outcome:** the probability that "In [year], I voted for..." is completed with the Republican vs the Democratic candidate (see Appendix A for how probabilities are formed). Vote is coded 1 = Republican, 0 = Democrat. GPT-3 probabilities are dichotomized at 0.50 (p. 10).
- **Topline comparison (p. 10):**

| Year | GPT-3 prob. (Republican) | ANES |
|---|---|---|
| 2012 (Romney) | 0.391 | 0.404 |
| 2016 (Trump) | 0.432 | 0.477 |
| 2020 (Trump) | 0.472 | 0.412 |

  The authors read this as "a mild amount of overall bias": GPT-3 was a little predisposed against Romney, against Trump (2016) and against Biden (2020). They judge the differences "relatively small" (p. 10).
- **Subgroup agreement (Table 1, p. 11):** two correspondence measures between ANES vote and binarized GPT-3 vote. *Tetrachoric correlation* estimates the correlation of two binary variables; *proportion agreement* is the share of matching votes. Selected rows:

| Group | 2012 tetra. | 2016 tetra. | 2020 tetra. | 2012 / 2016 / 2020 prop. agree |
|---|---|---|---|---|
| Whole sample | 0.90 | 0.92 | 0.94 | 0.85 / 0.87 / 0.89 |
| Strong partisans | 0.99 | 1.00 | 1.00 | 0.97 / 0.97 / 0.97 |
| Weak partisans | 0.73 | 0.71 | 0.84 | 0.74 / 0.74 / 0.82 |
| Independents | 0.31 | 0.41 | 0.02 | 0.59 / 0.62 / 0.53 |
| Low interest | 0.71 | 0.75 | 0.83 | 0.74 / 0.75 / 0.81 |

- **Authors' reading (pp. 11–12):**
  - More than half of the tetrachoric correlations are 0.90 or higher in all three years.
  - The one exception is pure independents, especially in 2020. Other measures exceed 0.65 and are generally closer to 0.8 or 0.9.
  - They note that political-science research suggests independents should be hard to predict (conflicted, least likely to vote, least knowledgeable, least interested).
  - They conclude "strong, additional evidence" for Criteria 3 and 4.
- Additional results (an ablation of backstory elements and a comparison with other language models) are said to be in the appendix; they are not part of these pages (p. 12).
- **2020 result:** the authors say the ability is "not restricted to one moment in time", and that results indicate the *possibility* of understanding people and groups outside the original training corpus (p. 12).

> **Intuition note.** Strong partisans are nearly perfectly predicted (tetrachoric 0.99–1.00). Pure independents are the weak spot, a group the authors say political science expects to be especially hard to predict (p. 12). Party ID and ideology are among the conditioning variables, so high agreement overall may partly reflect how much those variables in the backstory carry (this is our reading; the authors' ablation is in the appendix, not in these pages).

### §7 Study 3: Closed-ended questions and complex correlations (pp. 12–13)
- **Aim:** replicate complex association patterns among many variables. Done for 2016 ANES only. The authors call it their "most rigorous evaluation" of Criterion 4 (p. 12).
- **Method:** an interview-style conditioning template (example in the appendix). Using the zero-shot property of language models, the format induces short answers drawn from options listed by the "Interviewer". The conditioning text also supplies each subject's background. Conditioning uses human answers to eleven 2016 ANES questions, and GPT-3 predicts the response to the twelfth (p. 12).
- **Measure:** Cramér's V is a summary association measure for categorical variables that accounts for base-rate differences (p. 12). It is computed:
  - for each pair of survey items in the ANES ("Human"), and
  - between ANES conditioning values and the GPT-3 answer ("GPT-3").
- **Result (Fig. 4, p. 12):** high correspondence, with a mean difference between Cramér's V values of −0.026. GPT-3 values are "not uniformly high or low" but mirror stronger and weaker human relationships. Pairs weakly associated in the human data are weakly associated in the GPT-3 data, and conversely. The authors note variation in how precisely the patterns match, but call the overall correspondence "stunning" in "the vast majority of cases" (p. 12).
- **Limits (p. 13):** no match is expected at the individual level, because sampling is stochastic. With a large enough sample the overall distribution should match. Variation across draws is expected, and variation by sampling parameters is reported in the appendix (not in these pages).
- **Conclusion (authors):** "compelling, consistent, repeated evidence" for Criterion 4, extending to inter-correlations among behaviours, demographics and attitudes (p. 13).

> **Intuition note.** Study 3 asks whether the whole web of correlations carries over, not only a topline. If so, a researcher could read relationships off GPT-3 data. The check is at the level of pair strengths, so it does not show that any single simulated person is right.

### §8 Where do we go from here? (p. 15; the section heading is on p. 14)
- The authors say their purpose is not just human–computer comparison. Fidelity matters because models can be used "prior to or in the absence of human data" (p. 14).
- **Study 1 alone** (authors' list of what GPT-3 data would show): people describe the parties with different stereotyped terms; affect and extremity are tied to beliefs and identity; stereotypes contain issue, group and trait content, with traits most common; others can guess partisanship from stereotypes. From this a researcher could design questions, treatments and codebooks. Study 1 cost $29 on GPT-3 (p. 15).
- **Studies 2 and 3:** the Study 2 ablation (appendix) suggests which variables to include. Study 3 can target connections worth exploring and flag potential confounds for pre-analysis plans (p. 15).
- After fidelity is established for a model and domain, silicon samples can be used to pilot question wording, triage measures, identify key relationships and draft analysis plans (p. 15).

### §9 Discussion (pp. 15–16)
- The authors summarise: GPT-3 contains "a striking degree of algorithmic fidelity" in U.S. public opinion. Study 1 supports Criteria 1, 2 and 4. Studies 2 and 3 support Criterion 3 and give more granular Criterion 4 evidence (p. 15).
- Careful conditioning addresses temporality and replicability, with support in the appendix. GPT-3 replicates viewpoints of demographically varied sub-populations (p. 15).
- **Strengths and weaknesses:** the authors expect the method to have both relative to traditional methods; cost is a strength (p. 15).
- **Dangers (authors):** models with such fidelity could be used to target groups for misinformation, manipulation or fraud. They endorse calls for ethical standards and argue transparent, community-accountable research is needed to recognise and prevent abuse by private actors (pp. 15–16).
- The study is restricted to one domain. The method is general, and they invite the wider community to test other fields (p. 16).

### Appendix A: General details on GPT-3 usage (p. 16)
- Accessed via OpenAI's remote API, using the **Davinci** model (175B parameters; not Ada, Curie or Babbage), temperature **0.7**. The API returns text completions and log-probabilities (p. 16).
- **Probability estimation (log-sum-exp conversion):** token sets are treated as equivalent. For the prompt "In 2016, I voted for", the set {Donald, donald, DONALD, Trump, trump, TRUMP} is summed to an un-normalized share for Donald Trump. After collapsing token sets and summing, probabilities are normalized across the remaining sets so they sum to 1 (p. 16).
- Studies 1 and 3 (text generation) use the Completion API with default settings except temperature 0.7, which "encourages more deterministic answers, at the expense of response diversity". The authors say this parameter was not tuned (p. 16).
- Figure 5 shows backstory contexts with sampled continuations. The figure pairs two contexts ("strong conservative" and "strong liberal", each ending "In 2016, I voted for") with five sampled continuations on each side, naming candidates such as Donald Trump, John Kasich, Hillary Clinton and Bernie Sanders. The caption says this yields plausible voting patterns and additional simulated beliefs (p. 17, Fig. 5).

### Appendix B: Details on Study 1

**B.1 Samples (pp. 17–19)**
- Human sample: Pigeonholing Partisans participants who gave partisan identification, ethnicity, gender, income and age, which Rothschild et al. identified as correlating with evaluations of outgroups. N = 2,107 (p. 17).
- A matching 2,107 silicon individuals were generated. Template fragments were concatenated in fixed order: ideology, 7-point partisanship, race, gender, income, age. Missing variables were omitted (p. 17).
- **Age mapping:** 18–24 "young", 25–39 "middle-aged", 40–60 "old", 61+ "very old".
- **Income mapping:** <$15k "very poor", $15k–50k "poor", $50k–150k "middle-class", $150k+ "upper-class" (p. 17).
- 128 tokens were generated per silicon respondent (Fig. 6 shows full outputs). Regular expressions plus light manual post-processing extracted the four words. If GPT-3 listed more than four, only the first four were used. If fewer, the rest were left blank (p. 17).
- **Compliance (pp. 17–19):**
  - Full compliance would give 2,107 × 2 = 4,214 texts per sample.
  - After culling non-compliant ones: 3,592 human texts (1.7 per respondent) and 4,083 GPT-3 texts (1.9 per respondent), 7,675 in total.
  - The most common "non-compliant" GPT-3 output was four descriptive phrases instead of four words (Fig. 6, panel B). Some humans did this too, and these were kept.
  - Mean text length: human 4.54 words (min 4, max 15); GPT-3 7.78 (min 4, max 97). The mode is 4 in both, and most longer responses were 2–3-word phrases (Fig. 7).

**B.2 Lucid survey design (pp. 19–22)**
- Built in Qualtrics; 2,873 Lucid evaluators. The authors say this was faster, cheaper, and gave a wider range of evaluators than training research assistants (p. 19).
- Each evaluator did a content part (8 lists) and then a Turing part (8 different lists). No text was seen in both parts. Answer-choice order was randomized across respondents and fixed within each (p. 19).
- Because of minimal non-response and a brief server issue, 120/7,675 (1.5%) texts were coded only twice and 7 were coded four times. The authors say results do not differ when these are excluded (p. 19).
- The instrument items (pp. 20–22): partisanship guess; positivity (5 levels); extremity (yes/no); mentions of traits, issues, groups (yes/no each); Turing question "person or computer program". A results screen showed evaluators their guesses and the true sources.

**B.3 Lucid results analysis (pp. 22–29)**
- OLS models; with binary outcomes these are linear probability models. Results "do not significantly differ" with logit. Models include evaluator fixed effects and standard errors clustered by evaluator and list; estimated with the R package *fixest* (p. 22).
- **Controls (p. 23):**
  - Gender: Male/Female/Other.
  - Ethnicity: Hispanic and White indicators.
  - Income: rescaled to 0–1 from an 11-point scale.
  - Age.
  - Party ID.
  - Word length (in the correct-guess model only).
- **Predicted values** are computed at: Female, Not Hispanic, White, mean income, mean age, Democrat (and mean word length where used) (p. 23).
- **Table 2 (p. 24)**, coefficient on Source:GPT-3 (SE), 18,903 observations:

| Outcome | Positive | Extreme | Traits | Issues | Groups |
|---|---|---|---|---|---|
| GPT-3 coefficient | −0.010 (0.006) | 0.013 (0.007) | −0.058 (0.007) | 0.033 (0.007) | 0.078 (0.007) |

- **Table 3 (p. 25),** correct partisanship guess: Source:GPT-3 −0.073 (0.008); PID:Indep. −0.285 (0.014); PID:Rep. −0.097 (0.011); Word length 0.0009 (0.0007). RMSE 0.43912.
- **Tables 4–7 (pp. 26–29)** repeat positivity and extremity models, subset by the 7-point ideology of the list writers: EC, C, SC, I, SL, L, EL (Extremely Conservative to Extremely Liberal). Source:GPT-3 coefficient (SE):

| Table | EC | C | SC | I | SL | L | EL |
|---|---|---|---|---|---|---|---|
| 4 Positive, describing Republicans | −0.085 (0.121) | 0.019 (0.046) | −0.041 (0.054) | 0.040 (0.028) | 0.018 (0.033) | 0.034 (0.019) | 0.019 (0.051) |
| 5 Positive, describing Democrats | −0.145 (0.172) | 0.044 (0.044) | 0.041 (0.045) | 0.089 (0.027) | −0.028 (0.032) | −0.099 (0.020) | −0.033 (0.053) |
| 6 Extreme, describing Republicans | 0.079 (0.070) | −0.025 (0.060) | 0.064 (0.069) | 0.035 (0.038) | −0.066 (0.051) | 0.016 (0.034) | 0.143 (0.080) |
| 7 Extreme, describing Democrats | −0.374 (0.277) | −0.089 (0.059) | −0.024 (0.057) | −0.062 (0.035) | 0.027 (0.044) | 0.015 (0.027) | −0.030 (0.084) |

  Subgroup n per table: Tables 4 and 6: 387, 1,122, 1,059, 2,072, 1,419, 2,374, 1,036; Tables 5 and 7: 393, 1,121, 1,048, 2,062, 1,423, 2,370, 1,029. The text does not discuss individual coefficients in these four tables.

## Toy example (ours, not from the paper)
**Silicon sampling correction.** Suppose backstory $B$ has two values, urban and rural. A model's conditional vote probabilities are assumed correct: $P(V{=}R\mid\text{urban})=0.2$, $P(V{=}R\mid\text{rural})=0.7$.
- The model's own backstory mix is 70% urban, 30% rural. The unconditioned estimate is $0.7\times0.2+0.3\times0.7=0.14+0.21=0.35$.
- A representative survey has 40% urban, 60% rural. Conditioning on survey backstories gives $0.4\times0.2+0.6\times0.7=0.08+0.42=0.50$.
- Same conditional model, different marginal: 0.35 vs 0.50. This is why the paper takes $B$ from ANES. It works only if $P(V\mid B)$ is right.

**Dichotomizing and agreement (as in Study 2).** Four respondents; ANES vote (1 = Republican): 0, 1, 1, 0. GPT-3 probabilities for their backstories: 0.3, 0.6, 0.4, 0.2.
- Dichotomized at 0.50 gives 0, 1, 0, 0. Matches: respondents 1, 2, 4. Proportion agreement = 3/4 = 0.75.
- Mean GPT-3 probability = (0.3 + 0.6 + 0.4 + 0.2)/4 = 0.375, vs ANES mean 2/4 = 0.50. This is a "mild bias" in the topline despite fairly high agreement.

## Concepts
- [[algorithmic-fidelity]] — degree to which a model's relationships among ideas, attitudes and contexts mirror those of human sub-populations (p. 4)
- [[silicon-sample]] — GPT-3 outputs conditioned on real respondents' backstories, one simulated subject per human participant (p. 3)
- [[silicon-sampling]] (new) — method that draws backstories from a representative human sample so the model's skewed backstory marginals do not distort estimates (p. 5)
- [[language-model]] — here, a conditional distribution $p(x_n\mid x_1,\dots,x_{n-1})$ over tokens, sampled iteratively (p. 3)
- [[conditioning-context]] (new) — the initial tokens given to the model, including first-person backstories (p. 4)
- [[zero-shot-few-shot-prompting]] — in Study 3, the format alone induces short survey-style answers without examples (p. 12)
- [[social-science-turing-test]] (new) — Criterion 1: generated texts are indistinguishable from parallel human texts (p. 4)
- [[backward-forward-continuity]] (new) — Criteria 2 and 3: output is consistent with the context, and proceeds naturally from it (pp. 4–5)
- [[pattern-correspondence]] (new) — Criterion 4: output reproduces relationships among ideas, demographics and behaviour seen in human data (p. 5)
- [[sampling-temperature]] (new) — API parameter set to 0.7; the authors say it favours more deterministic answers at the cost of diversity (p. 16)
- [[tetrachoric-correlation]] (new) — correlation measure for two binary variables, used with proportion agreement in Table 1 (p. 11)
- [[cramers-v]] (new) — association measure for categorical variables that accounts for base-rate differences (p. 12)

## Canonical instances
- [[pigeonholing-partisans-silicon-replication]] (new) — GPT-3 four-word lists about partisans vs Rothschild et al.'s human lists, judged by Lucid evaluators (pp. 6–9)
- [[anes-vote-choice-silicon-sample]] (new) — GPT-3 vote choice conditioned on ANES backstories for 2012, 2016, 2020 (pp. 10–11)
- [[anes-cramers-v-comparison]] (new) — interview-style conditioning, with Cramér's V compared between ANES and GPT-3 for 2016 (pp. 12–14)

## Bridges (candidates)
- [structural-analogy] Silicon sampling (replace $P(B_{GPT3})$ by $P(B_{ANES})$, keep $P(V\mid B)$) ↔ survey statistics: post-stratification / reweighting a conditional model to a target population — both fix the marginal while trusting the conditional
- [structural-analogy] Dichotomizing probabilities at 0.50 and comparing with binary survey vote ↔ classification evaluation: thresholded predictions scored by agreement
- [metaphor] "Many biases, not one" ↔ mixture models: a single model viewed as a mixture of subgroup distributions selected by conditioning (the authors say "combination of many distributions", p. 4)
- [structural-analogy] Simpson's paradox analogy (p. 5) ↔ statistics: aggregate trends can differ from subgroup trends

## Questions this raises
- Fidelity is tested against ANES vote and related items. How much of Study 2's agreement comes from variables like party ID and ideology that are closely tied to vote choice, rather than from subtler associations? (The authors point to an ablation in the appendix; that is not in this part.)
- Does fidelity hold for groups, topics or periods that are poorly represented in GPT-3's training text? The authors restrict their claim to U.S. politics (p. 16).
- The authors give no numeric thresholds (p. 5). What would a defensible standard for "enough fidelity" look like for a given research question?
- Agreement is judged in aggregate, not per individual (p. 13). What kinds of social-science inference does that still allow, and which does it rule out?

## Reading notes
- **Part boundaries:** this part covers printed pp. 1–29: abstract, §§1–9, Appendix A, Appendix B (B.1–B.3, ending with Table 7 on p. 29). The contents list on p. 2 also lists Appendices C (Study 2 details, incl. ablation and model comparison), D (Study 3 details, incl. temperature variation) and E (cost analysis), through p. 50. These pages were not provided and are not digested here. The split is at a section boundary.
- **Page numbers:** printed = pdf for all pages. Source is the arXiv version v1 (dated September 16, 2022); the unit header cites the 2023 *Political Analysis* version, whose pagination may differ.
- **Cross-reference errors visible in the pages:**
  - B.3 (p. 23) refers to "Panel B of Figure 4" and "panel A of Figure 4"; in this version these are Figure 3 panels. Figure 4 is the Cramér's V figure.
  - The Figure 6 caption says it is an expanded version of "Figure 2 in the main text" (the B.1 body says "Figure 2 in the text"); the matching example contexts are in Figure 1.
  - §6 (p. 12) and §8 (p. 15) cite "Appendix 3", and §9 (p. 15) cites "Appendix 5"; the appendix headings are lettered (C.3 ablation, E cost).
- **Typos:** p. 12 "The 2012 tetrachoric correlation across all respondents 0.90" (verb missing); p. 15 "these these".
- **Loose statements in the text:**
  - "7.3% more often" (p. 9) is a difference of 7.3 percentage points (60.1 − 52.8; Table 3: −0.073).
  - The claim that other measures "exceed 0.65" (p. 11) is loose: the Moderates 2012 tetrachoric value in Table 1 is exactly 0.65.
  - §7 says GPT-3 predicts the "twelfth" item after eleven conditioning questions, while Figure 4 shows 11 variables; I could not reconcile this from the pages.
  - The sign convention of the "−0.026" mean difference in Cramér's V is not stated.
  - Subgroup n in Tables 4–7 sum to 9,469 + 9,446 = 18,915, while Table 2 reports 18,903 observations; the pages do not explain the 12-observation difference.
  - Table 7 prints a "Signif. Codes" footnote, but no stars appear in the table.
- **Figures:** the bubble sizes in Fig. 2 and the line values in Fig. 3A are not readable numerically. Only percentages stated in the text are reported here.
- **Own inference flagged:** the comment on the Study 2 intuition note about party ID and ideology possibly carrying part of the signal is mine, not the authors'.
