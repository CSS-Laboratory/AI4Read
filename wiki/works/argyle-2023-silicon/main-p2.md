---
id: argyle-2023-silicon/main-p2
work: argyle-2023-silicon
unit: paper (part 2/2) — Appendices C–E, Acknowledgements, References
pages: 30–53
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Appendices C–E: Details on Studies 2 and 3, costs, references

## L0 — One line
The appendices document how GPT-3 "silicon samples" of respondents to the American National Election Studies (ANES, a US election survey) were built and scored in Studies 2 and 3, and add agreement tables, an ablation (dropping inputs to see the effect), a model comparison, Study 3 checks and costs.

## L1 — The gist (≤ 120 words)
This part is the appendix of a paper that prompts GPT-3 with survey-style "backstories" built from real ANES respondents. It documents how Study 2 (vote prediction for 2012, 2016, 2020) and Study 3 (virtual interviews, 2016) were built and scored. It adds full agreement tables, an ablation, a model comparison, Study 3 checks and costs. In Study 2, whole-sample tetrachoric correlations with human votes are 0.90–0.94, but agreement varies by subgroup; for 2020 independents it is near zero. Study 3 compares patterns of association between variables, not individual answers.

**Prerequisites:** 2×2 contingency tables; correlation; prompting a language model and reading next-token probabilities; sampling temperature.

## L2 — Key ideas
- **Study 2 setup.** GPT-3 gets a first-person backstory built from up to 10 ANES variables. The authors read the probability of one next token, with synonym tokens collapsed (e.g. "romney", "mitt", "republican"), and never sample text. Temperature is therefore irrelevant (p. 30).
- **Scoring.** The probability of voting Republican is cut at 0.50 into a binary variable. It is compared with the reported vote by four agreement statistics: tetrachoric correlation (correlation of two binary variables assumed to come from hidden normal scales), Cohen's κ (agreement corrected for chance), the intraclass correlation coefficient (ICC, a rater-agreement index) and raw proportion agreement (pp. 30–31).
- **Results by subgroup.** Whole-sample tetrachoric correlation is 0.90 (2012), 0.92 (2016) and 0.94 (2020). Agreement is near-perfect for strong partisans and weak for independents (2020: 0.02) (pp. 32–34).
- **Ablation** (systematically removing backstory elements). No single element accounted for all of the predictive power. Party was more predictive than ideology. State or political interest slightly hurt (p. 35).
- **Model comparison.** Larger models do very well. A smaller open model (reported as GPT-Neo, 6B) rivals GPT-3 (175B) (p. 36).
- **Study 3 setup.** Eleven interview answers are fed in as a mock interview. GPT-3 samples the twelfth, 5 tokens at temperature 0.7. The text is coded by exact string match (pp. 36–38).
- **Study 3 logic.** The comparison is of distributions, not of individuals. Cramér's V (0–1 association measure for categorical variables) is computed between all pairs of 22 variables. 1,782 of 4,270 cases are complete (p. 43).
- **Differences from humans.** Descriptive statistics differ a lot (e.g. GPT-3 age mean 35.5 vs. 50.1). Missing data from GPT-3 is up to 23.8% for some items (pp. 47–48).
- **Checks on Study 3.** A synthetic-only version of the Cramér's V comparison looks similar in pattern. Among three temperatures (0.001, 0.7, 1.0), 0.7 gave the smallest differences (pp. 47, 49–50).
- **Costs** are reported: $29, $75 and $1,428 for Studies 1–3 (p. 50).

## L3 — Walkthrough

### C. Details on Study 2

**C.1 Data generation (p. 30).**
- The silicon sample uses the 2012, 2016 and 2020 ANES Timeseries data. Each subject gets a first-person backstory built with a templating strategy "similar to" Study 1.
- Ten variables are used (names differ per year): (1) race/ethnicity, (2) gender, (3) age, (4) conservative–liberal self-placement, (5) party identification, (6) interest in politics, (7) church attendance, (8) discussing politics with family and friends, (9) patriotic feeling about the flag (not asked in 2020), (10) state of residence (not released in 2020 at time of writing).
- Self-reported vote is the outcome (presvote2012x, V162062x, V202110x).
- Template phrasing is close to the ANES wording, turned into first-person statements. Age and state are inserted directly. Other variables are mapped to a short string such as "attend church" or "extremely liberal". Fragments are concatenated. A missing variable means its fragment is omitted.
- Only the probability of a single successor token is used, so temperature and sampling strategy do not matter. Many equivalent phrases get probability, so they are collapsed (method in "Section A", not in this unit).
- Token sets per year: Romney: "romney", "mitt", "republican", "conservative". Obama: "obama", "barack", "democrat", "democratic", "liberal". Trump (2016 and 2020): "trump", "donald", "republican", "conservative". Clinton: "clinton", "hillary", "rodham", "senator", "democrat", "democratic", "liberal". Biden: "joe", "joseph", "biden", "democratic", "democrat", "liberal".
- Case and spacing variants count as distinct tokens and were included. Other tokens are ignored. Sets were meant to catch common cases and were "not tuned or optimized".

**C.2 Data analysis (pp. 31–34).**
- The Republican probability is dichotomized exactly at 0.50. More than .50 is coded as a Republican vote, less than 0.50 as Democrat. No probability was exactly 0.50. Human reported vote is the baseline (p. 31).
- Four statistics compare the two binary variables (p. 31):
  - *Tetrachoric correlation:* for two binary variables assumed to come from an underlying continuous normal distribution. Read like Pearson's r. R command `tetrachoric` (psych).
  - *Cohen's κ:* agreement of two "raters" (ANES and GPT-3), penalizing agreement expected by chance. Typically 0 to 1. A negative value means worse than chance.
  - *ICC:* an agreement measure usable across measurement types. Scores above 0.75 count as strong agreement. The authors use the averaged versions and report the lowest of ICC1, ICC2 and ICC3. They say the differences between them are negligible in nearly all cases. Using the underlying probability instead of the binary GPT-3 variable does not change ICC meaningfully.
  - *Proportion agreement:* the share of exact matches. It is descriptive and ignores chance. It is included because tetrachoric correlation and κ "do not perform well" when more than 95 percent of data fall in one quadrant. The authors give Strong Democrats as an example. There is almost no variation in either vote variable, which makes the correspondence measures unreliable (pp. 31–32).
- Main text Table 1 gave only tetrachoric correlation and proportion agreement (p. 31).

Whole-sample and selected subgroup results (Tables 8–10, pp. 32–34). Cells are tetrachoric / κ / ICC / proportion agreement:

| Group | 2012 (Romney) | 2016 (Trump) | 2020 (Trump) |
|---|---|---|---|
| Whole sample | .90/.69/.81/.85 | .92/.73/.84/.87 | .94/.77/.87/.89 |
| Strong partisans | .99/.93/.96/.97 | 1.00/.95/.97/.97 | 1.00/.95/.97/.97 |
| Weak partisans | .73/.45/.61/.74 | .71/.46/.62/.74 | .84/.63/.77/.82 |
| Independents | .31/.16/.22/.59 | .41/.25/.39/.62 | .02/.02/.03/.53 |
| Moderates | .65/.40/.57/.77 | .76/.52/.69/.78 | .71/.48/.65/.77 |

- Other rows, with proportion agreement high and κ lower: Liberals 2012 .43 / .95; 2016 .25 / .95; 2020 .51 / .97. Blacks 2012 .31 / .97; 2016 .51 / .96; 2020 .49 / .94 (κ / proportion agreement) (pp. 32–34).
- Age groups: κ is 0.65–0.71 (2012), 0.69–0.75 (2016) and 0.70–0.82 (2020) (pp. 32–34). Table 10 has no state rows (consistent with the state variable not being released for 2020).
- The authors explain the low correspondence measures only for the Strong Democrats case, by lack of variation (pp. 31–32). They give no explanation for independents in these pages.

*Intuition note:* The statistics answer "how often do the human and the silicon vote agree, beyond luck?". When almost everyone in a group votes the same way, κ and correlation can look poor even when the raw match rate is high, so the authors also report the raw match rate.

**C.3 Ablation analysis (p. 35, Fig. 8).**
- Setting: ANES 2016, ten template elements. The authors removed one or two elements at a time and also tested one-element backstories. Metric: proportion agreement.
- Reported findings:
  1. No single element accounted for all of the predictive power. The authors suggest GPT-3 fuses several elements.
  2. GPT-3 can use either Party or Ideology, but Party is more predictive.
  3. Adding some elements (State, Political Interest) "mildly hurt" performance.
  4. With both Party and Ideology removed, the authors report that the remaining 8 elements together give better accuracy than any single element (see Reading notes: the figure seems to disagree).
- Figure 8, approximate values read from the bars: full backstory ≈0.87; no backstory ≈0.52 (caption: essentially random chance). Removing one element gives ≈0.80 to ≈0.89, lowest when Party is removed. Removing Party and Ideology gives ≈0.68. Single elements: +Party ≈0.82, +Ideology ≈0.79, +Patriotism ≈0.67, down to +Churchgoer ≈0.42.
- The template was not optimized; it was "our first try". The authors say future work can likely improve results by optimizing it.

*Intuition note:* Ablation asks which pieces of the prompt matter. Here party and ideology are the most useful single elements, but no single piece does everything.

**C.4 Model comparison (p. 36, Fig. 9).**
- Five model families are tested: GPT-3, Jurassic, GPT-J, GPT-Neo, GPT-2. GPT-3 and Jurassic are paid-API models; the others are public. Metric: proportion agreement against parameter count (log scale) for ANES 2012, 2016 and 2020.
- Performance also "depends strongly" on each model's training corpus. The authors note only that, as in many NLP tasks, the very largest models perform very well.
- They also note that the largest GPT-Neo model, at 6B parameters, rivals GPT-3 at 175B.

### D. Details on Study 3

**D.1 Data generation (pp. 36–42).**
- Study 3 builds a complete virtual interview. Twelve variables from the 2016 ANES are used: demographic (gender, race/ethnicity, age, education, religiosity), attitudinal (political interest, patriotic feeling about the flag, party identification, ideology) and behavioral (talking about politics, voting, vote choice). Because vote choice depends on turnout, these two are merged in the analysis, giving 11 unique items (footnote 1, p. 36).
- The conditioning text is a mock interview with 11 of the 12 questions answered. The twelfth is left for GPT-3. Each backstory comes from one real ANES respondent. A missing ANES answer removes that question (footnote 2, p. 36).
- Study 2 measured one token's probability. Here answers have many tokens, which complicates raw probabilities, so completions are sampled and analyzed (p. 36).
- Phrasing matches the ANES interview wording as closely as possible. Fragments are concatenated. Variables, in order: gender (V161342), race (V161310x), age (V161267), education (V161270), church attendance (V161244), patriotism (V162125x), discusses politics (V162174), political interest (V162256), 7-point ideology (V161126), 7-point partisanship (V161158x), voted in 2016 (V162031x), vote choice (V162062x) (pp. 36–38).
- Fig. 10 (p. 37) shows an example context. It is a dialogue of "Interviewer:" questions and "Me:" answers. Answer words are inserted dynamically. The target question is last; in the example the sampled completion for church attendance is "yes".
- Table 11 (pp. 39–42) compares ANES wording with the template. Examples of difference: the ANES race question has five categories, the template four ("White", "Black", "Asian", "Hispanic"). The template drops "apart from occasional weddings, baptisms or funerals" from the church question. Age is a derived ANES variable with no question text. The vote-choice question is shown only if the respondent voted.
- Procedure (p. 38): the *target factor* is predicted from all the others. Its fragment is placed last. GPT-3 samples 5 tokens at temperature 0.7. The output is lower-cased and stripped, then exactly matched to the allowed answers. Race codes are white 1, black 2, asian 3, hispanic 5. A non-match is coded as missing. The result is "structurally equivalent" to the ANES dataset.
- 12 variables × 4,270 respondents give more than 50,000 conditioning texts. Only the 1,782 observations complete in both ANES and GPT-3 are kept, to avoid noise from a changing set of cases (p. 38).

**D.2 Data analysis (p. 43).**
- The synthetic responses are appended into one dataset with the ANES values and silicon responses for all eleven variables.
- **The authors do not compute individual-level correspondence** (such as percent correctly predicted). Their reason: GPT-3 draws from a distribution of words, and the population also has a distribution of outcomes. Even if both come from the same distribution, they need not match case by case. What matters is whether GPT-3 produces a distribution of responses comparable to the human data.
- Cramér's V is computed (R `DescTools::CramerV`) between every combination of the 22 variables. It suits categorical data and, like Pearson's chi-squared on which it is based, uses marginal values to account for base rates. Range 0–1. Higher means knowing one variable tells more about the other.
- Tables 12–14 (pp. 44–46) give the values behind main-text Figure 6. Columns: ANES V (ANES input with ANES output), GPT-3 V (ANES input with GPT-3 output), Difference = ANES V − GPT-3 V. Examples: age→discuss.politics 0.21 vs 0.21; ideology→church.goer 0.28 vs 0.07 (difference 0.21); political.interest→discuss.politics 0.40 vs 0.16 (0.24); church.goer→discuss.politics 0.01 vs 0.14 (−0.13); pid7→vote.2016 0.48 vs 0.37; ideology→pid7 0.37 vs 0.32.

*Intuition note:* The test is whether the same variables are linked in GPT-3's output as in human data, for example whether party goes with vote. Many pairs match closely, and a few differ by 0.2 or more.

**D.2.1 Missing data (pp. 43, 47).**
- Only complete cases are used: 1,782 of 4,270. Missing rates vary a lot for both sources.
- Table 15 (percent missing, ANES / GPT-3): Age 4.7/2.8; Attends church 0/0.4; Discusses politics 0.1/14.6; Race 0.1/5.6; Education 14.3/1; Gender 0/1.2; Ideology 4.2/22.6; Patriotism 0.7/14.6; Party ID 3.6/0.5; Political interest 1.1/14.8; 2016 vote and choice 0.5/23.8.
- The authors say GPT-3 gave a valid, compliant answer in more than three-quarters of cases for all items, and three items had compliance above 99 percent. They say non-compliance could "likely" be reduced with additional training for particular questions.

**D.2.2 Descriptive statistics (p. 48, Table 16).** Selected means, ANES vs GPT-3 (N = 1,782 each unless stated):
- Age 50.1 vs 35.5 (GPT-3 minimum 0; ANES minimum 18).
- White 0.803 vs 0.974; Hispanic 0.089 vs 0.001; Black 0.077 vs 0.023.
- Male 0.481 vs 0.759.
- Graduate degree 0.196 vs 0.002; some college 0.348 vs 0.642.
- Party ID 3.857 vs 4.429; ideology 4.095 vs 4.017; patriotism 1.963 vs 1.456.
- Among those with a vote-choice value (ANES 1,553; GPT-3 1,483): Trump 0.438 vs 0.245; Clinton 0.484 vs 0.233; Other 0.078 vs 0.523.
- The authors give no comment on these gaps in these pages. The analysis rests on pairwise associations (D.2), not on these marginal distributions.

**D.3 Alternative specifications (pp. 47–50).**

*D.3.1 Completely synthetic data (pp. 47, 49).* The main text computes V between the ANES "input" variable and the GPT-3 output. This is the most direct comparison, since both share one half of each pair. Alternatively, V can be computed between GPT-3 vectors only, with no ANES data in the GPT-3 relationship. Figure 11 (p. 49) shows the same "Human" points as before. It replaces the GPT-3 point (previously V between ANES and GPT-3) with V computed entirely on synthetic data. Using synthetic data on both sides adds noise, but the pattern of V comparisons is "highly similar" (p. 47).

*D.3.2 Temperature variation (pp. 47, 50).*
- Temperature controls random variation in sampling. At 0.001, virtually every completion is the highest-probability response; for a .49/.51 split, always the .51 token. At 1.0, selection probability equals the model probability (no adjustment). The main text uses 0.7.
- Table 17 (p. 49): summary of differences in V, computed as GPT-3 V minus human V (the opposite sign to Tables 12–14):

| | Temp 0.001 | Temp 0.7 | Temp 1.0 |
|---|---|---|---|
| Mean | 0.059 | −0.026 | −0.031 |
| Min | −0.123 | −0.241 | −0.250 |
| Max | 0.700 | 0.168 | 0.119 |
| SD | 0.141 | 0.068 | 0.070 |
| N | 2518 | 1782 | 1022 |

- Authors' reading: of the three options, 0.7 gives the lowest difference; 0.7 and 1.0 differ minimally. Each temperature was run once, with no selection of best fits. This "provides some evidence" of robustness to model specification (p. 47).
- Temperature 0.001 produces more error and systematically overstates the relationships. At 0.001, GPT-3 labelled all respondents white, so V for race was not computable and race is excluded there (pp. 47, 49).
- Different temperatures yield different numbers of valid completed cases. Lower temperature minimizes invalid tokens; higher temperature includes more invalid responses. Mid-range temperatures therefore appear to balance validity and completeness (p. 50).

*Intuition note:* At near-zero temperature the model almost always gives its single most likely answer (p. 47). The authors report that this overstated the relationships, and that GPT-3 labelled every respondent white. At 1.0 the model follows its raw distribution, and higher temperatures include more invalid responses (p. 50).

### E. Cost analysis (p. 50)
Costs are for final runs only; extra runs were made. The standard rate of $0.06 per 1,000 tokens is stated in the Study 1 paragraph.
- **Study 1:** queries printed as "1,1471" (one per human subject); backstories averaged 66 tokens; up to 128 tokens generated; total $29.
- **Study 2:** 15,626 queries (5,914 for 2012, 4,270 for 2016, 5,442 for 2020); backstories averaged 80 tokens; 1 token generated; total $75.
- **Study 3:** prompts averaged 458 tokens; up to 5 tokens generated; 4,270 queries per experiment, $119 per experiment. There were 12 experiments (one per predicted element), so the total was $1,428.
- The authors say the Jurassic model would have reduced costs for all experiments.

### Acknowledgements and references (pp. 50–53)
Thanks go to the BYU departments of Computer Science and Political Science and to five named colleagues for feedback. The references list 41 items. They include language-model papers (e.g. GPT-2, T5, GPT-3), political-science text-as-data work, algorithmic-bias literature, and ANES-related and voting-behavior literature. Cramér's *Mathematical Methods of Statistics* (1946) is listed as reference [39].

## Toy example (ours; not from the text)
100 imaginary respondents with a binary party and a binary vote.

**1. Cramér's V.** Human table (party × vote): R-R 40, R-D 10, D-R 10, D-D 40. For a 2×2 table, V = |φ| = |ad − bc| / √((a+b)(c+d)(a+c)(b+d)).
- φ = (40·40 − 10·10) / √(50·50·50·50) = 1500 / 2500 = 0.60.
- Silicon table: R-R 35, R-D 15, D-R 15, D-D 35. φ = (35·35 − 15·15) / 2500 = (1225 − 225) / 2500 = 0.40.
- Difference (human − silicon, the Tables 12–14 convention) = 0.20. The silicon sample shows the same direction of association, but weaker.
- Individual agreement was never needed. Only the strength of association in each dataset is compared.

**2. Why proportion agreement is also reported.** Human vote and silicon vote: both R 96, human R/silicon D 2, human D/silicon R 2, both D 0.
- Agreement = 0.96.
- Chance agreement = 0.98·0.98 + 0.02·0.02 = 0.9604 + 0.0004 = 0.9608.
- κ = (0.96 − 0.9608) / (1 − 0.9608) = −0.0008 / 0.0392 ≈ −0.02.
- So κ is about zero although 96% match. This is the low-variation problem described on pp. 31–32.

## Concepts
- [[silicon-sample]] — GPT-3 outputs conditioned on real respondents' backstories, compared with their human answers (pp. 30, 38)
- [[backstory-template]] (new) — first-person text fragments built from survey variables and concatenated into the prompt (p. 30)
- [[token-set-collapsing]] (new) — collapsing synonym tokens, including case and spacing variants, into one token set per candidate (p. 30)
- [[temperature-sampling]] (new) — a setting controlling randomness of sampling; 0.001 is near-greedy and 1.0 uses the model's raw probabilities (p. 47)
- [[tetrachoric-correlation]] (new) — correlation of two binary variables assumed to come from underlying normal variables (p. 31)
- [[cohens-kappa]] (new) — agreement between two raters, corrected for chance agreement (p. 31)
- [[intraclass-correlation]] (new) — a rater-agreement index; the authors report the lowest of ICC1–3, averaged versions (p. 31)
- [[proportion-agreement]] (new) — share of cases where the two binary variables match exactly; ignores chance (p. 31)
- [[ablation-study]] (new) — removing elements of the prompt template to measure their contribution (p. 35)
- [[target-factor]] (new) — the one interview variable GPT-3 must answer, always placed last (p. 38)
- [[cramers-v]] (new) — 0–1 association measure for categorical variables, based on chi-squared (p. 43)

## Canonical instances
- [[anes-vote-prediction-2012-2016-2020]] — Study 2: GPT-3 vote probability vs reported vote in three elections (pp. 30–34)
- [[study3-virtual-interview]] — Study 3: mock ANES interview, one answer sampled; associations compared via Cramér's V (pp. 36–38, 43)
- [[template-ablation-anes-2016]] — Fig. 8 ablation of backstory elements (p. 35)
- [[model-size-comparison-vote-task]] — Fig. 9: five model families on the vote task (p. 36)

## Bridges (candidates)
- [same-math] Cramér's V ↔ statistics: chi-squared test of independence, rescaled to 0–1; for 2×2 tables it equals |φ|.
- [same-math] temperature in sampling ↔ language models: scaling next-token scores before the softmax (canon link; the source describes it only in words).
- [same-math] dichotomizing probability at 0.50 ↔ machine learning: a classification threshold on a predicted probability.
- [structural-analogy] prompt-element ablation ↔ interpretability: ablating model components to test their causal role.
- [structural-analogy] comparing association patterns, not individuals ↔ social-science simulation: validating a model by whether it reproduces population-level relationships.

## Questions this raises
- Why do the Study 3 marginal distributions (age, race, sex, vote-choice shares) differ so much from ANES while pairwise V values are often close? Could V hide these differences?
- If the ablation shows that State and Political Interest slightly hurt, would an optimized template change subgroup results, especially for independents?
- How much does the 0.50 cut-off matter? Would a different threshold change κ and ICC for weak partisans and moderates?
- Why does a smaller open model rival GPT-3 here, and does that hold for tasks beyond voting?

## Reading notes
- **Coverage:** this part starts at Appendix C ("Details on Study 2", p. 30) and ends with the last reference (p. 53). Printed page number = pdf page number. Appendices A and B are not in this unit; p. 30 only refers to "Section A" for token collapsing. Main-text Table 1 and Figure 6 are referred to but not shown.
- The authors give no numbers.
- **Possible source inconsistencies (what the pages show):**
  - C.3 item 4 says the 8 remaining elements (Party and Ideology removed) beat any single element. In Fig. 8, the "− Party and Ideology" bar (≈0.68) looks lower than "+ Party" (≈0.82) and "+ Ideology" (≈0.79).
  - Strong Democrats are said to have low κ and correlation (pp. 31–32), but Tables 8–10 list "Strong partisans" with very high values.
  - C.4 says GPT-Neo's largest model has 6B parameters. In Fig. 9 the points near 6×10⁹ are coloured as GPT-J, and the red GPT-Neo points appear to end near 3×10⁹.
  - The text under the κ bullet says values "in Table 1" were calculated with `cohen.kappa`, while the previous paragraph says Table 1 shows only tetrachoric correlation and proportion agreement.
  - In the C.1 variable list, V201452 appears for both church attendance (7) and discussing politics (8) in 2020.
  - Age is V161267 in the text (p. 36–38) but V161247 in Table 11.
  - Fig. 10 shows no ideology question, though ideology is in the variable list. The text does not say why; footnote 2 allows removal of missing answers.
  - Table 17 uses GPT-3 minus human (p. 47), the opposite sign to Tables 12–14 (ANES minus GPT-3). Its N row (2518, 1782, 1022) differs by temperature, which p. 50 attributes to different numbers of valid completed cases.
  - Section E says Jurassic was "not available at the time of writing", although C.4 reports it. Study 1's query count is printed as "1,1471" and Study 2's 2012 count as "20112"; the three Study 2 counts as printed sum to 15,626 (reading the 2012 count as 5,914).
  - Tables 8–9 print "Wisconsins". References [7] and [11] are the same Radford et al. 2019 entry. Reference [36] spells "Westyle" and [37] spells "Westlye".
- **Figure 11** is not an error: its "Human" points are unchanged, and only the GPT-3 points are replaced by synthetic-only V values (p. 47).
