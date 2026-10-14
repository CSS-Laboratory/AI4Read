---
id: kahan-2013-motivatedreasoning/main
work: kahan-2013-motivatedreasoning
unit: paper
pages: 407–424
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Ideology, motivated reasoning, and cognitive reflection (Kahan 2013)

## L0 — One line
In a national sample, motivated reasoning about a test of "open-mindedness" showed up on both left and right, and it was not reduced (in one condition it was increased) among people who scored high on the Cognitive Reflection Test, which fits an "expressive utility" account better than a "System 1 bias" or "conservative cognitive style" account.

## L1 — The gist (≤ 120 words)
Why do Americans split along ideological lines over empirical facts like climate change? Kahan tests three accounts: one blaming heuristic (System 1) thinking, one blaming conservative cognitive style, and one treating motivated reasoning as identity-protective and amplified by reasoning skill. In a 1,750-person national sample, ideology was not meaningfully related to Cognitive Reflection Test scores, and liberals and conservatives showed similar motivated reasoning when judging a test's validity. Higher reflection scores went with more polarization in one of two experimental conditions. The data fit the expressive-utility account better than the other two. Kahan infers that, if the study's implication holds, debiasing System 1 should not be expected to abate polarization.

**Prerequisites:** regression and interaction terms; ordered logit (regression for ordered rating scales); p-values and statistical power; Type II error; basic dual-process ideas (fast intuitive vs slow effortful thinking).

## L2 — Key ideas (5–10 bullets)
- Three influences on polarization over facts are heuristic-driven (System 1) processing, identity-protective motivated reasoning, and cognitive-style correlates of conservatism. Kahan turns their combinations into three rival positions, BRP, IAP and EUP, with different predictions. (pp. 408–410)
- Observational result: in a representative sample (N = 1750), conservatism/Republican orientation was not negatively related to CRT. The combined party-plus-ideology scale (Conserv_Repub) gave b = 0.05, p = 0.33 with controls; party identification alone correlated slightly but significantly positively with CRT (r_s = 0.08, p < 0.01). IAP's prediction was not confirmed, and the result is at odds with the nonrepresentative-sample findings. (pp. 413–414, 417)
- Experimental design: subjects judged the CRT's validity as a measure of open-mindedness after being told that climate-change skeptics, or believers, scored higher. Both sides rated the test as valid when it flattered their side. (pp. 412, 414)
- The motivated reasoning was symmetric: the shifts between conditions for liberal Democrats (0.86) and conservative Republicans (0.75) did not differ significantly, and quadratic terms added nothing. Kahan takes this as inconsistent with IAP, while footnote 5 notes a caveat. (p. 414 and n. 4)
- Higher CRT scores amplified polarization in the "believer-is-biased" condition (three-way interaction b = 0.30, p < 0.01) but not in the "skeptic-is-biased" condition. This is the opposite of BRP's prediction that polarization abates. (pp. 415–416)
- Kahan reads the results as more consistent with EUP: identity-protective cognition is individually rational, and reflective people do it better. For the weaker effect in one condition, which was not hypothesized, he offers a conditional explanation (wording familiarity and density) that he calls not incompatible with EUP. (pp. 417–418)
- Kahan stresses the limits: one study, with contested CRT and numeracy measures, so the question is not closed. He urges convergent measures such as an AOT scale. (pp. 418–419)
- Practical upshot: if, as the study implies, motivated cognition is not a consequence of over-reliance on heuristics, System 1 debiasing should not be expected to abate this polarization. Kahan says what is needed instead are interventions that remove the expressive incentives, and he points to work on regulating the social meanings that make beliefs badges of group loyalty. (p. 419)
- Expressively rational belief formation, individually rational but collectively harmful, is described as intrinsic to a collective action problem, the "tragedy of the science communications commons". (p. 420)

## L3 — Walkthrough

### Abstract and 1. Introduction (pp. 407–408)
- **Question.** Americans fight over empirical facts with striking "ubiquity and ferocity" (global warming, nuclear waste disposal, HPV vaccination, concealed-carry and crime), not only over values. The contending beliefs have no logical link to the values of those who hold them, and the polarization persists despite an apparent scientific consensus on many of the questions. (p. 407)
- Decision science offers three explanations (pp. 407–408):
  - Members of the public use heuristics that bias risk perception.
  - They seek and assess evidence in ways that reinforce prior positions.
  - Some psychologists say dogmatism and aversion to complexity correlate with conservatism and make conservatives distinctively resistant to evidence.
- Each is well supported, but "relatively little testing" has been done on how they relate. Plausible accounts of their interaction compete, and testing them matters for practical action. (p. 408)
- The study uses observational and experimental methods to test the three dynamics: dual-process reasoning, conservative cognitive style, motivated cognition. (p. 408)

### 2. Empirical and theoretical background (pp. 408–410)
- **Heuristic-driven processing.** Dual-process theories posit a "fast, associative" mode and a "slow, rule based" mode. Many scholars blame public risk controversy on over-reliance on System 1. Visceral, emotion-guided perception can lead laypeople to overestimate sensational risks (terrorism, gun accidents) relative to remote ones (climate change, swimming pools). Expert opinion does not reliably correct this because the public too often lacks the time or ability for System 2 reasoning. (p. 408)
- **Motivated reasoning** means conforming assessments of information to a goal other than accuracy. Protecting one's standing in an affinity group is one such goal ("identity self-defense"). If a factual proposition becomes associated with a group, forming a contrary view threatens one's standing, so people are unconsciously motivated to resist contrary assertions. (p. 408)
- **Cognitive-style correlates.** A body of work refining the "authoritarian personality" idea has revived the hypothesis that right-wing ideology is a manifestation of dogmatism, aversion to complexity and a craving for closure. It is surmised that this style generates reflexive closed-mindedness toward evidence hostile to conservative policy premises. (p. 408)
- **Three positions** (all described as plausible; how they interact has "not been systematically explored") (pp. 408–410):
  - **BRP (Bounded Rationality Position).**
    - On this view, System 1 predominance would be the most decisive factor. Group-based emotional associations drive System 1 risk perceptions, so risk perceptions differ across ideologically uniform groups. (pp. 408–409)
  - **IAP (Ideological Asymmetry Position).**
    - The reasoning-style correlates of right-wing ideology are most consequential. Motivated cognition is treated as heuristic-driven, and conservative traits indicate reliance on System 1. Motivated reasoning would therefore be disproportionately associated with conservatives, because open-mindedness and reflection that would check it correlate negatively with conservatism. (p. 409)
    - Experimental evidence is "mixed": Nam et al. report greater conservative resistance, while others find symmetry across groups. (p. 409)
  - **EUP (Expressive Utility Position).**
    - Identity-protective processing guides people to group-congruent beliefs rather than the best evidence. It often benefits ordinary individuals, since one person's error about, e.g., climate science will not change the risk (Downs), whereas deviating from the group's belief could mark her as untrustworthy or stupid. (p. 409)
    - Hence System 2 should magnify, not mitigate, ideological differences. System 1 users fit in via conformity and elite cues. System 2 users are better at fighting off counterarguments, choosing stances on technical issues, and understanding what evidence means for their group's status, so they feel more unconscious pressure to form identity-congruent assessments. (pp. 409–410)
    - EUP inverts BRP's relation between motivated cognition and System 2. It is "agonistic" (agnostic) on whether System 1 dispositions correlate with ideology, but it does not imply that motivated reasoning is concentrated in conservatives. (p. 410)

*Intuition note:* The three positions differ on two questions. Is motivated reasoning mainly a lazy-thinking problem (BRP, IAP) or a skilled social strategy (EUP)? Is it concentrated on the right (IAP) or found across ideologies (EUP)?

### 3. Study: sample, design, hypotheses (pp. 410–413)
**3.1 Sample.** 1,750 U.S. adults recruited by YouGov (online, stratified to the U.S. population), July 2012. The sample was 54% female, mean age 52, 76% white and 11% African-American. By party, 28% were Republican, 36% Democrat and 30% independent. By ideology, 25% were liberal/very liberal, 37% conservative/very conservative and 29% moderate. Mean education was "some college" and mean income $40,000–49,000. (p. 410)

**3.2 Observational component.**
- *Measures.* Party identification (dem_repub, 7 points) and ideology (libcon, 5 points) were standardized and summed into Conserv_Repub (α = 0.82). The components were centered at their ordinal midpoints (4 and 3), not their means, so 0 is a "neutral" orientation. Negative values mean Democrat/liberal, positive Republican/conservative. (p. 410)
- *CRT.* A three-item performance test of disposition to effortful System 2 processing (Frederick 2005). It predicts heuristic-related biases strongly, more than several self-report measures. Mean score was 0.65 (SD = 0.95). (p. 410)
- Table 1 gives the items and the % correct: widgets (5 machines, 5 minutes, 5 widgets → 100 machines, 100 widgets) 26%; bat and ball ($1.10 total, bat costs $1.00 more) 13%; lilypad (doubles daily, 48 days to cover the lake → half) 25%. (p. 411)
- *Hypothesis.* IAP predicts a right-wing outlook goes with a lower CRT score. The reasoning: CRT is routinely used as a performance-based corroborator of self-report measures such as need for closure. CRT is also reported to correlate negatively with religiosity. (p. 411)
- *Prior work.* Iyer et al. (2012) and Pennycook et al. (2012) found slightly lower CRT in conservatives. Kahan questions their samples. (p. 411)
  - **Iyer et al.:** visitors to a website about political outlooks and cognitive styles, with a self-profile offered as incentive. Mean CRT scores of all ideologies matched or exceeded those of elite-university students, so the sample may overrepresent highly reflective people.
  - **Pennycook et al.:** Mechanical Turk workers. Their sample was 53% liberal and 25% conservative, against about 20% and 40% in national surveys (Gallup, footnote 1). Further concerns raised: repeat exposure to performance measures, and some workers misrepresenting their nationality.
- A finding in a representative sample would matter. Absence of the negative correlation "would be surprising" and would complicate the finding that conservatism is negatively associated with subjective measures of heuristic processing. A finding that CRT correlates with conservative ideology in the general population would be inconclusive for BRP and EUP: BRP does not suggest asymmetry but does not rule it out, while EUP asserts symmetry without blaming System 1. (p. 412)

**3.3 Experimental component.**
- *Measure.* After finishing the CRT, subjects rated agreement (six points) with: "I think the word-problem test I just took supplies good evidence of how reflective and open-minded someone is" (CRT_valid). (p. 412)
- *Conditions* (random assignment; wording in Appendix, p. 424):
  - **Control:** psychologists believe the questions measure reflectiveness and open-mindedness.
  - **Skeptic-is-biased:** additionally, a study found that people who accept climate-change evidence score higher on the test. This would imply believers are more open-minded.
  - **Believer-is-biased:** additionally, a study found that people who reject climate-change evidence score higher. This would imply skeptics are more open-minded.
- *Logic.* Open-mindedness is a positive trait, so people have a stake in believing their own ideological group is at least not less open-minded. Subjects had only sparse information on CRT validity (the "psychologists believe" statement plus their own experience of the test). Kahan expects motivated reasoning to make them credit the test's validity conditional on whether that gratifies their stake. The design models how ordinary people process second-hand reports of studies on the ideological correlates of cognitive style, and more generally evidence on climate change, guns, the death penalty, etc. If validity assessments depend on fit with predispositions, citizens polarize rather than converge. (p. 412–413)
- *Predictions* (all three positions predict motivated reasoning here; they differ on its form) (p. 413):

| Position | Prediction |
|---|---|
| IAP | Stronger in conservatives. Right-wing subjects see CRT as more valid in believer-is-biased than skeptic-is-biased; left-wing subjects' assessments comparable across the two. |
| BRP | Higher among low-CRT subjects; any polarization should dissipate as CRT increases. |
| EUP | Symmetric across ideology, and ideologically congruent assessments increase with CRT. |

- EUP's reasoning: high-CRT subjects process more methodically, so they misunderstand the question less often and escape the unconscious pressure less often. (p. 413)

**3.4 Power and missing data.** The large sample gave power "well over 0.80" at p ≤ .05 to detect even r = 0.10. Kahan therefore equates nonsignificance with lack of effect at low risk of Type II error. Missing data were handled by multiple imputation. An earlier analysis with listwise deletion gave no materially different results (footnote 3). (p. 413)

### 4. Results (pp. 413–416)
**4.1 Observational.**
- Ordered logit of CRT on Conserv_Repub and controls (Table 2, N = 1750): (p. 413)

| Predictor | Model 1 | Model 2 |
|---|---|---|
| Conserv_Repub | 0.07 (1.45) | 0.05 (0.97) |
| male | | **0.68** (6.60) |
| white | | **0.72** (5.41) |
| education | | **0.31** (8.39) |
| income | | **0.06** (3.32) |
| religiosity | | **−0.15** (−3.63) |
| LRχ² | 2.1 (1 df) | 261.9 (6 df) |
| ΔLRχ² | | 259.8 (5 df) |

- Religiosity is a composite of church attendance, prayer frequency and perceived importance of God (α = 0.82). (p. 413)
- Conserv_Repub was positive but nonsignificant: b = 0.07, p = 0.15 alone; b = 0.05, p = 0.33 with controls. The other characteristics all had significant independent effects. (p. 414)
- Components separately (for comparability with single-measure studies): (p. 414)
  - libcon correlation: r_s = −0.02, p = 0.45. Liberals (M = 0.75, SEM 0.05) vs conservatives (M = 0.67, SEM 0.04), moderates excluded: ΔM = 0.09, t = 1.41, p = 0.16.
  - dem_repub correlation: r_s = 0.08, p < 0.01, positive and significant, so CRT rose with Republican identification.
  - Republicans (M = 0.66) vs Democrats (M = 0.52), leaners excluded: ΔM = 0.14, t = 2.48, p < 0.05.
  - With leaners treated as partisans: 0.71 vs 0.59, ΔM = 0.13, t = 2.54, p < 0.05.
- IAP's prediction of a negative CRT–right-wing correlation "was not confirmed". (p. 414)

*Intuition note:* In a sample built to resemble the U.S., conservatives scored no lower on the reflection test, and Republicans scored slightly higher. Kahan argues the earlier negative results may come from unrepresentative samples.

**4.2 Experimental.**
- *a. Motivated reasoning in general* (Figure 1A). All three positions expected it, and it appeared. (p. 414)
  - **Control:** right and left subjects judged CRT validity comparably (M = 3.0, SEM = 0.2 each; ΔM = 0.08, t = 0.59, p = 0.56).
  - **Skeptic-is-biased:** right-wing M = 2.4, left-wing M = 3.5.
  - **Believer-is-biased:** right-wing M = 3.1, left-wing M = 2.6.
- *b. Symmetry.* Figure 1 uses a locally weighted regression smoother (it traces the data without distributional assumptions). The motivated-reasoning effect did not appear to grow toward the right. (p. 414)
  - Liberal Democrats discounted CRT validity in believer-is-biased relative to skeptic-is-biased by ΔM = 0.86 (t = 6.37, p < 0.01). Conservative Republicans discounted it in skeptic-is-biased relative to believer-is-biased by ΔM = 0.75 (t = 5.39, p < 0.01). The first amount was slightly but nonsignificantly larger (ΔM = 0.11, t = 0.57, p = 0.57).
  - Footnote 4: a quadratic model, adding squared Conserv_Repub to Table 3 Model 1, gave trivially small, nonsignificant added terms and no significant improvement in fit.

*Intuition note:* Both sides moved their ratings by about the same amount, in opposite directions, depending on whether the news flattered their side. Nothing in these data shows one side doing this more.

- *c. Interaction with CRT.* Figure 1 panels B–D (CRT = 0, 1, and 2 or 3) show congenial assessments becoming "progressively more pronounced" as CRT increases, most dramatically in believer-is-biased. (p. 415)
- Regression (Table 3; outcome CRT_valid; skeptic/believer are 0/1 dummies; zCRT and Conserv_Repub centered at 0): (p. 416)

| Term | Model 1 | Model 2 |
|---|---|---|
| Conserv_Repub | −0.12 (−1.60) | −0.12 (−1.58) |
| Skeptic-is-biased | −0.02 (−0.29) | −0.03 (−0.27) |
| Believer-is-biased | −0.18 (−1.74) | −0.17 (−1.63) |
| Con_Rep_x_skeptic | **−0.50** (−4.63) | **−0.50** (−4.62) |
| Con_Rep_x_believer | **0.38** (3.59) | **0.37** (3.47) |
| zCRT | | 0.04 (0.53) |
| C_R_x_zcrt | | −0.05 (−0.76) |
| zCRT_x_skeptic | | −0.01 (−0.12) |
| zCRT_x_believer | | −0.07 (−0.65) |
| Con_Rep_x_zCRT_x_skeptic | | −0.03 (−0.31) |
| Con_Rep_x_zCRT_x_believer | | **0.30** (2.95) |
| LRχ² | 89.96 (5 df) | 102.60 (11 df) |
| ΔLRχ² | | 12.64 (6 df) |

- Model 2 fit significantly better than Model 1 (ΔLRχ² = 12.64 (6), p = 0.01). The believer-is-biased three-way term is positive and significant (b = 0.30, p < 0.01): opposing ideologies polarized more as CRT increased. The skeptic-is-biased term is trivial (b = −0.03, p = 0.76): polarization there did not meaningfully vary with CRT. (p. 415)
- Figure 2 (Monte Carlo predicted probabilities from Model 2, 95% CIs): "Liberal Democrat" = −0.95 and "Conservative Republican" = +0.95 on Conserv_Repub. "Low CRT" = 0 correct (bottom 60% of the sample). "High CRT" = 2 correct (matched or exceeded by 20%). (pp. 416–417)
  - In believer-is-biased, the difference in predicted probability of judging CRT "valid" is 28 percentage points (± 19%, CL = 0.95) greater for high-CRT partisans than for low-CRT partisans. Low-CRT partisans do not differ meaningfully there. My reading of Figure 2 is that this is the partisan gap, about 4 points at low CRT and about 32 at high CRT. (p. 416, Fig. 2)
  - In skeptic-is-biased, both low- and high-CRT partisans are highly likely to disagree. High-scorers disagree somewhat more, but the difference (8%, ± 11%) is not significant at 0.95. (p. 416)
- Conclusion of 4.2: the results are "more consistent with EUP than BRP". Intensification occurred but only in one condition. (p. 416; see Reading notes on a wording slip here)

*Intuition note:* In one condition, the more reflective a subject, the further apart left and right ended up. On Kahan's EUP reading, a better reasoner can see more clearly which answer protects the group. The effect is not general: it appeared in one of two conditions.

### 5. Discussion (pp. 416–420)
**5.1 Summary.** (pp. 416–418)
- **BRP not supported.** The CRT, a measure of System 2 disposition, "actually magnifies" the impact of motivated reasoning. (p. 416)
- **IAP faces two challenges.** (p. 417)
  - First, no meaningful correlation between right-wing ideology and CRT. CRT is treated as a stronger or behavioral corroborator of need for cognition, need for closure, etc. It has also been used to link religiosity with resistance to evidence. It is therefore "puzzling" that CRT did not correlate negatively with conservatism. This is at odds with the nonrepresentative-sample results.
  - Second, an experimental design built to test intensity across the spectrum found liberals and conservatives "uniformly" prone to motivated reasoning, as in other studies reporting symmetry.
  - Footnote 5: this inference assumes liberal Democrats and conservative Republicans have a comparable identity stake in their climate positions. If liberals were more committed to seeming open-minded, the design could not rule that out. That explanation would, however, not support the claim that conservatives are peculiarly vulnerable.
- **EUP largely fits.** EUP alone predicted both symmetry and amplification by CRT. It treats motivated cognition as a reasoning adaptation, not a deficiency. People use it to protect stakes in all kinds of groups, including non-political ones, so there is no reason to expect it to be stronger under any ideology. It guides individuals to serve personal (not collective) ends, so higher-reflection people should do it more accurately. (pp. 417–418)
- **The one discrepancy** is the limited scope of the CRT interaction (one condition). It was not hypothesized but is "not incompatible" with EUP. (p. 418)
  - "Skeptics are closed-minded" is likely more familiar than "believers are closed-minded". The instructions were fairly dense.
  - Low-CRT subjects, if they struggled or did not want to put in effort, would be more likely to misunderstand the unfamiliar claim. High-CRT subjects were more likely to grasp it and so to form an identity-congruent appraisal. (p. 418)

**5.2 Implications for dual-process and motivated-reasoning research.** (pp. 418–419)
- Many commentators have assumed, "not implausibly", that ideologically motivated cognition is unconscious, heuristic-driven and overridable by reflection. The results cast doubt on this. They are not in tension with dual-process theories generally. Some earlier dual-process theorists held that motivated reasoning should also characterize systematic cognition when it advances identity-maintaining ends. The study is more consistent with that view. (p. 418)
- The results also help corroborate the inference from an earlier observational study (Kahan, Peters et al. 2012). That study found climate and nuclear polarization greatest among people high in scientific literacy and numeracy, a measure of which CRT is a subcomponent. (p. 418)
- **Limits.** One study does not "conclusively demonstrate" that reflection invariably magnifies motivated reasoning. The key issue is the continuing debate over measures. (p. 418–419)
  - Self-report scales vs objective measures like CRT.
  - CRT is so demanding (over a third of a general sample may score zero; under 10% get all three) that it is of limited value in explaining variance among a large portion of the population. Numeracy is superior in this respect and also predicts greater polarization.
  - What CRT and numeracy measure is contested: critical reflection directly, or a general mathematical or intellectual proficiency. Whether CRT measures willingness to revise beliefs (Actively Open-minded Thinking, AOT) as well as an AOT scale is unresolved. So it is unresolved whether an AOT scale would amplify or reduce motivated reasoning.
  - Kahan recommends continued study with varied measures for convergent validity. If many measures converge, that program is best placed to show how the influence might be counteracted. (p. 419)

**5.3 Implications for counteracting motivated reasoning.** (pp. 419–420)
- Debiasing aimed at System 1 distortions is "unquestionably important", because such distortions are real. But if ideologically motivated cognition is not a consequence of over-reliance on heuristics, System 1 debiasing "should not be expected" to abate polarization over climate change, nuclear power, gun control or the HPV vaccine. (p. 419)
- What is needed are interventions removing the expressive incentives to form beliefs on grounds unconnected to their truth. The account presupposes that beliefs carry social meanings tied to group commitment. Few facts do: pasteurization, water fluoridation and air-traffic-control privatization do not show significant polarization. (p. 419)
- Meanings can plausibly be revised. Kahan reads the historical shift in public opinion on cigarette risks as mediated by campaigns that changed the positive meanings of dismissing the evidence in certain subcommunities. He cites ongoing work on forecasting polarizing technologies, protecting the "science communication environment", and framing strategies. (pp. 419–420)

**5.4 Conclusion: the tragedy of the science communications commons.** (p. 420)
- When risks become suffused with antagonistic meanings, it is "often if not always, and with respect to many if not all issues" individually rational to attend to information in a way that connects one to one's group's positions. If everyone does so, all are collectively worse off, because democratic institutions are less likely to converge, or to converge as rapidly, on policies reflecting the best evidence.
- One individual's policy belief makes no difference, so collective irrationality creates no reliable pressure to change. Overcoming polarization therefore needs collective action, and decision science is "uniquely poised" to supply the knowledge for it.

### Appendix (p. 424)
Gives the exact instructions for the three conditions and the CRT_valid item, six response options from "strongly disagree" to "strongly agree". The statements in skeptic- and believer-is-biased say "If the test is a valid way to measure open-mindedness, that finding would imply …".

## Toy example (ours, not from the paper)
Idea: test whether polarization grows with reflection (the three-way interaction in Table 3) by comparing partisan gaps.

Suppose 20 subjects in each of four cells, all in the believer-is-biased condition. We count how many rate the CRT "valid".

| Cell | Agree "valid" | Share |
|---|---|---|
| Low CRT, liberal Democrat | 7 of 20 | 35% |
| Low CRT, conservative Republican | 8 of 20 | 40% |
| High CRT, liberal Democrat | 4 of 20 | 20% |
| High CRT, conservative Republican | 11 of 20 | 55% |

- Partisan gap at low CRT: 40% − 35% = 5 points.
- Partisan gap at high CRT: 55% − 20% = 35 points.
- Difference in gaps: 35 − 5 = 30 points. A positive difference means polarization is larger among reflective subjects, the EUP pattern.
- BRP would instead predict a smaller gap at high CRT, for example 5 → 2, a difference of −3.
- In the paper, the corresponding quantity is estimated by a regression term: b = 0.30 for Con_Rep_x_zCRT_x_believer. The text gives a 28-point difference (± 19) from Model 2 (p. 416).

## Concepts
- [[motivated-reasoning]] — fitting assessments of information to a goal other than accuracy; here, protecting group standing (p. 408). Canon: motivated reasoning / motivated skepticism.
- [[identity-protective-cognition]] — "identity self-defense": unconsciously resisting facts contrary to one's group's dominant belief. Kahan adds that it often serves individual interest (pp. 408–409).
- [[heuristics-cues]] — System 1 low-effort shortcuts blamed by BRP for biased risk perception (p. 408). Here "heuristic" is tied to dual-process theory, not specifically to party cues.
- [[dual-process-theory]] (new) — fast, associative System 1 vs slow, rule-based System 2 (p. 408).
- [[cognitive-reflection-test]] (new) — three-item test measuring disposition toward System 2 over System 1 (pp. 410–411).
- [[bounded-rationality-position]] (new) — Kahan's label: System 1 dominates and motivates ideologically congruent assessment; polarization shrinks with System 2 use (pp. 409–413).
- [[ideological-asymmetry-position]] (new) — conservative cognitive style makes motivated reasoning stronger on the right; predicts lower CRT among conservatives (pp. 409, 411, 413).
- [[expressive-utility-position]] (new) — identity-protective reasoning is individually rational and magnified by System 2; symmetric across ideology (pp. 410, 413).
- [[expressive-rationality]] (new) — belief formation that is rational for conveying group loyalty, not for accuracy (pp. 409, 419–420).
- (No canon concept on belief-system constraint is used in this paper.)
- [[social-meaning-of-beliefs]] (new) — facts become badges of group membership. Only a few risk topics have this property (p. 419).
- [[collective-action-problem]] — individually rational belief strategies that leave everyone worse off. Kahan's "tragedy of the science communications commons" (p. 420).
- [[statistical-power-null-findings]] (new) — large N lets nonsignificance be read as no effect at low Type II risk (p. 413).

## Canonical instances
- [[climate-change-believer-skeptic-experiment]] — believer-is-biased/skeptic-is-biased framing of CRT validity (pp. 412, 424).
- [[crt-items]] — widgets, bat-and-ball and lilypad items with % correct (p. 411).
- [[mechanical-turk-sample-critique]] — Kahan's argument that nonrepresentative samples may explain earlier CRT–conservatism correlations (pp. 411–412).
- [[cigarette-risk-opinion-shift]] — Kahan reads the shift in opinion on cigarette risks as showing that social meanings of risks may be changeable (pp. 419–420).
- [[pasteurization-fluoridation-nonpolarized]] — facts that carry no group meaning show little polarization (p. 419).

## Bridges (candidates)
- [structural-analogy] Individually rational belief-formation, collectively harmful ↔ collective action problem (tragedy of the commons): Kahan makes the analogy explicitly.
- [structural-analogy] One person's belief cannot change policy (Downs) ↔ paradox of voting / rational ignorance: the same logic of negligible individual influence removes pressure toward accuracy.
- [structural-analogy] EUP's reflective people better at identity-congruent processing ↔ identity-protective cognition among the more cognitively skilled (canon): the same claim stated for ideology.
- [structural-analogy] Three-way interaction (ideology × CRT × condition) ↔ difference-in-differences logic: compares partisan gaps across levels of a moderator.
- [metaphor] "Science communication environment" ↔ commons: pollution of shared information as common-pool degradation.

## Questions this raises
- Would the same symmetry and CRT amplification hold for issues beyond climate change, or for topics where one side has a stronger identity stake (as footnote 5 allows)?
- Why did high CRT amplify polarization only in believer-is-biased? Is the familiarity/density explanation testable by changing wording?
- Would an AOT scale, which measures willingness to revise beliefs, amplify or reduce motivated reasoning compared with CRT?
- Which practical interventions can change the social meaning of a contested fact, and how can we forecast which technologies become polarizing?

## Reading notes
- Printed page = pdf page + 406 (pdf 1 = p. 407). Pages 5, 7, 8, 9, 10, 11, 15, 16, 17 had images checked. Tables 1–3 and Figures 1–2 were read from the images; the Appendix (pdf 18) was read from the text layer only. The text layer was usable.
- **Probable slip in the source (p. 416):** "These results are more consistent with EUP than BRP. Whereas the former predicted that motivated reasoning would abate as CRT increases, the latter predicted that it would not". Earlier text (p. 413) says BRP predicts abatement and EUP predicts increase, so "former" and "latter" are swapped. I used the p. 413 assignment.
- The p. 414 libcon comparison reports ΔM = 0.09 although 0.75 − 0.67 = 0.08, presumably rounding.
- Typos in source: "Amzaon.com" (p. 411); "Sunstein, 20006b" (p. 418); "agonistic" for "agnostic" (p. 410); "property attributed" for "properly attributed" (p. 418); "Independents or Independents" (p. 414). Balcetis & Dunning is cited as 2008 in the text (p. 408) but 2006 in the references (p. 420).
- Both Conserv_Repub and religiosity scales are reported with α = 0.82 (pp. 410, 413); I did not treat this as an error.
- In the Table 3 text, interaction terms are named Con_Rep_x_zCRT_x_believer and similar. The table row "C_R_x_zcrt" is presumably the Conserv_Repub × zCRT term (the text does not say).
- Figure 2's numeric values were read approximately from the image. Only the "28 points (±19)" and "8% (±11)" figures are stated in the text.
