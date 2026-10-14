---
id: zaller-1992-massopinion/ch08-tests
work: zaller-1992-massopinion
unit: "8 Tests of the one-message model"
pages: 151-184
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Tests of the one-message model

## L0 — One line
Zaller's reception–acceptance model, applied to a one-sided message, predicts different shapes of opinion change for different message intensities, issue familiarities and ages, and the available data roughly bear this out.

## L1 — The gist (≤ 120 words)
Chapter 7's RAS model fitted some attitude-change data. Was that luck? Zaller derives further implications. Opinion-change curves should differ with message intensity (how far a message reaches inattentive people) and issue familiarity (stored considerations dilute new messages). He finds roughly the expected shapes on Reagan's approval, on new issues, and on Korea, Vietnam and race. The same logic appears to hold in how individual considerations form. Age, a predisposition that is not manifestly political, appears to interact with awareness as party or ideology does. The evidence is cumulative and supportive, not conclusive. The typology rests on weak measurement, and no case has a strictly one-sided message flow, as the model assumes.

**Prerequisites:** logistic functions; the RAS model and Equations 7.3/7.5 from Chapter 7 (reception rises with awareness, acceptance falls with awareness when a message conflicts with predispositions); the idea of a nonmonotonic (rise-then-fall) curve.

## L2 — Key ideas (5–10 bullets)
- **Intensity is partly a property of the audience.** How many people receive a story depends on public interest and prior knowledge, not only on media volume. North's one-day sentencing reached more people than months of Wright coverage (pp. 152–153).
- **Two message-level parameters.** Intensity is $a_0$ in the reception function; familiarity is $b_0$ in the acceptance function. Varying them produces a typology of six change curves (Figs. 8.2–8.3). Its general shape holds over all plausible values of $a_0$, $b_0$, provided awareness stays positively linked to reception and negatively linked to acceptance to a similar degree (pp. 154–158).
- **Predictions.** Low intensity concentrates change among the highly aware. High familiarity lowers total change and pushes the peak toward less-aware people. A moderately intense message reaching a group opposed to it produces nonmonotonic change, peaking among the moderately aware (p. 165).
- **Tests on cases.** Reagan's approval after Iran–Contra (judged a louder and more familiar message than Central America), plus school desegregation, the nuclear freeze and economic news, fit reasonably. Zaller says the evidence for the first two deductions seems quite strong and that the typology is less strongly supported (pp. 159–166).
- **Resistance at the level of considerations.** Highly aware people hold more non-Contra considerations, and the data are consistent with these diluting scandal news (inertial resistance). They also form fewer inconsistent considerations than moderately aware people (partisan resistance). Zaller calls this support helpful but not conclusive (pp. 168–172).
- **Age works like any predisposition.** Older highly aware Republicans (Korea), older liberals (Vietnam, desegregation) show nonmonotonic patterns, which Zaller attributes to older partisan lessons they learned (pp. 174–179).
- **Age is not generally linked to resistance.** Zaller sees no reason to expect age to be generally tied to greater resistance; he argues the RAS model can specify the effect of age, whatever its direction (p. 180).
- **Caveat.** No case has strictly one-sided information; a two-message model is promised for Chapter 9 (p. 166).

## L3 — Walkthrough

### Introduction (p. 151)
The chapter tests deductions from the Chapter 7 model, including nonintuitive ones. The aim is to show that the model's early success was not "merely fortuitous" (p. 151). Three parts: message-level determinants of change (intensity, familiarity); resistance at the level of considerations (the RAS model's primitive term); and generational differences in receptivity. Zaller warns that the chapter skips from one empirical example to another without building a comprehensive picture of any one domain, which he admits makes it somewhat disjointed to read (p. 151).

### Characteristic patterns of attitude change (pp. 151–158)

**Message intensity (pp. 151–154).** Earlier chapters used two individual-level factors, awareness and predispositions. Now two message-level factors are added (p. 151).
- *Intensity* = a message's capacity to penetrate the consciousness of a public that differs in attention to politics. A few messages reach nearly everyone (e.g. wartime opposition to Germany and Japan). Many reach only the attentive, such as most congressional actions and Supreme Court decisions (p. 152).
- Intensity depends on more than media volume. It also depends on how much people already know and care about the issue (p. 152).
- **Evidence: 1989 NES pilot.** Three stories were tracked. North's suspended sentence was a one-day lead story. Wright's resignation was a months-long controversy. The Supreme Court ruling allowed executing juveniles and mentally retarded persons. "Reception" meant giving a minimally correct answer to a follow-up on why Wright resigned, or the equivalent. Estimated reception: about 75% (North), 45% (Wright), 25% (death penalty) (p. 152).
- Reagan's fall from a horse was learned about by more people than learned why Wright resigned, despite minimal weekend coverage (p. 153).
- Conclusion: Zaller says penetrating power may be as much a property of the audience, which does or does not find a story interesting, as of the amount of coverage. Intensity therefore describes both the message and an audience that is or is not interested (p. 153). Zaller notes that separate measures of coverage and public familiarity are unavailable (fn. 2, p. 153).
- These data measure reception independently of attitude change. Fig. 8.1 shows reception curves from logistic regressions of the Equation 7.3 form (coefficients in Table 8.6). Reception rises strongly with awareness, though stories differ in level. Highly aware people learn about virtually all important political news, while others learn almost none of it (p. 153).
- Comparison case (a nonpolitical story): a DC-10 airliner crash was shown repeatedly on television for several days and was prominently featured in all the news media. A large number of people were still unaware of it (p. 154).
- Consequence: attitude-change curves take markedly different shapes depending on whether the message has the penetrating power of the DC-10 crash, the North story or the death-penalty ruling (p. 154).

*Intuition note.* Whether news "gets through" depends on who is listening as well as on how loudly it is broadcast. Less-aware people miss even loud stories, so how many people the message reaches is part of the explanation for who can change.

**Message familiarity (p. 154).** Messages on issues where the public has a large store of considerations meet inertial resistance (stored considerations dilute any new message). They are expected to produce less change, all else equal, than messages on novel topics. They also change the expected shape of the curve. Fn. 4 notes that intensity and familiarity are not wholly independent, since both depend on prior public information (p. 154).

**The model (Eq. 7.5, repeated on p. 154).** The text layer for this page is garbled, and no page image was supplied. The following is my reconstruction of the equation from that text layer plus fn. 5 (p. 155), where "/" is the floor parameter $f$ and "$-b_2$ Predispositions" is a predisposition term:
$$\text{Prob(Change)}=\Big(1-\big(1+f+\exp[a_0+a_1\,\text{Awareness}]\big)^{-1}\Big)\times\big(1+\exp[-b_0-b_1\,\text{Awareness}-b_2\,\text{Predispositions}]\big)^{-1}\tag{7.5}$$
First factor = reception; second = acceptance. Intensity is captured by $a_0$: higher $a_0$ means more reception at a given awareness. Familiarity is captured by $b_0$: lower $b_0$ means lower acceptance (p. 154). The model is highly interactive, so shifts in $a_0$ and $b_0$ ramify (p. 155).

**The typology (Fig. 8.2, p. 155–157).** Parameter values (fn. 5, p. 155):
- $a_1=1.25$ and $b_1=-1.25$;
- $a_0=-2.5, 0, 2.5$ for low, medium and high intensity;
- $b_0=+3$ for low familiarity and $0$ for high familiarity;
- resistance effects of $+1.5, 0, -1.5$ for liberal, centrist and conservative persons;
- $f=0$, and awareness runs from $-2$ to $+2$.

A liberal message is assumed to diffuse through liberal, centrist and conservative subpopulations (p. 155).
- *Top row (less familiar), panels A, B, C = low, medium, high intensity, roughly like the death-penalty, Wright and DC-10 stories of Fig. 8.1.* Low intensity: change is concentrated among the most aware, because they are the only ones who meet the reception requirement. As intensity rises, change becomes common among moderately and then modestly aware persons. Lower intensity means a smaller share of change among the less aware, and higher intensity a larger share (p. 155).
- Central America (Fig. 7.5) roughly matches panel B (p. 155).
- *Bottom row (more familiar), panels D, E, F.* Higher familiarity has two effects. Total change is smaller. And a higher proportion of the change is concentrated among less-aware persons, so peaks move toward the low-awareness end (pp. 155, 157). Fn. 6 gives the reason: awareness has both reception and acceptance effects.
- Figure 8.2 does not exhaust the possible patterns. Even more intense messages would raise change among the least aware, and even less familiar issues would raise change especially among the highly aware (p. 157).

**Fig. 8.3 (pp. 157–158).** A three-dimensional version is meant to show that the typology does not depend on the chosen parameters. The surface keeps the same general shape for $a_0$, $b_0$ between $\pm 10$ (fn. 7), provided awareness remains positively associated with reception and negatively associated with acceptance to roughly the same degree (p. 158).

*Intuition note.* In our gloss, the typology can be read as a contest between two forces. Awareness raises the chance of hearing the message and, for opposed groups, raises the chance of rejecting it. Intensity and familiarity shift where each force wins.

### The case of presidential popularity (pp. 158–162)
**Measurement.** Independent measurement of intensity and familiarity is not possible. Media attention is easy to measure but intensity also includes public interest, and suitable knowledge data are unavailable. No-opinion rates are a possible indicator, but question formats differ (p. 158). Method: take U.S. involvement in Central America as the baseline (medium intensity, low familiarity) and judge other cases relative to it (p. 158).
- Central America got cover stories from Time and Newsweek in 1986–87, but did not grip the public. Only 38% knew in 1986 that the U.S. backed the Contras, not the Nicaraguan government (pp. 158–159).
- Reagan's disapproval rose from 32% to 48% between late Nov. 1986 and June 1987 after charges that he knew of the diversion of funds to the Contras (p. 159).
- Zaller classifies messages about Reagan's job performance as more intense (the Iran–Contra scandal was the major continuing story for months, and Reagan was the leading political figure) and as more familiar (his sixth year as president). So the Reagan pattern should differ from Central America roughly as cell B differs from cell F (p. 159).
- **Fig. 8.4** shows change toward disapproval among November approvers (Nov. 1986 NES postelection survey and 1987 NES pilot). Raw data (computed as in Tables 7.1 and 7.2) match cell F reasonably. Model estimates (Eq. 7.7, controlling party identification, egalitarianism and Central America attitudes; coefficients in Table 8.5) for centrist Republicans, Independents and Democrats closely resemble the raw data and cell F (p. 160).
- The curve for liberal Democrats (mean party ID 1.3; 1 SD above average on egalitarianism and dovishness) is not nonmonotonic. The apparent conflict is a compositional problem. The raw data cover only Democrats who did not yet disapprove of Reagan, and most liberal Democrats, especially the highly aware, already disapproved in fall 1986. So the liberal-Democrat curve does not describe the people available for conversion, while the centrist-Democrat curve does and generally agrees with the raw data (pp. 160–161, fn. 8).
- Fairness of the test requires controlling partisan composition. **Fig. 8.5** compares centrists on Reagan approval and Central America. The total change is about the same. The anti-Reagan message was "louder" because it penetrated the lower-awareness strata, and "more familiar" because it met greater resistance among the highly aware (p. 161).
- Among the most aware centrists, Iran–Contra had virtually no effect. Ideology is hard to invoke for centrists, and Zaller's alternative explanation is inertial resistance from a large store of information after six years of Reagan. The greatest impact fell on those with modest initial information (pp. 161–162).

### Opinion formation on new issues (pp. 162–165)
Three cases of attitude *formation* are used as further tests of Fig. 8.2: federal school desegregation in the mid-1950s, judgments of the economy as the 1981–82 recession seemed to end, and the nuclear freeze in the early 1980s. Since no prior measurement exists, Zaller assumes that most support was formed in response to recent communications through the usual reception–acceptance process (p. 162).
- *School desegregation.* Before *Brown* (1954), federal action was a "nonissue." A 1956 agree–disagree item asked whether Washington should stay out of the question of whether white and colored children go to the same schools. Most non-black supporters of mandated desegregation are judged to be fairly new adherents (pp. 162–163; fn. 10 says opinion had been shifting left on race since the mid-1940s).
- *Nuclear freeze.* The NES asked in fall 1982 about a unilateral or joint freeze. The idea had been invented by activists only months before, so support must be new support (p. 163).
- *Economy.* In Nov.–Dec. 1982 the NES asked whether the economy had improved over the past year. After the deep 1982 recession, belief in improvement may be considered new support (p. 163).
- **Judgments (p. 164).** Intensity (from Zaller's casual look at the periodical literature): segregation and freeze seem to be of roughly middle intensity, like Central America. Economic news seems less intense, mostly second-level news. Familiarity: race is "by far" the most familiar; the freeze is at the other pole (a foreign-policy novelty); economic familiarity is hard to judge and left open. Expectations: freeze resembles cell B, segregation cell E, and economy a low-intensity cell (A or D).
- **Fig. 8.6**, derived from Eq. 7.5 (coefficients in Table 8.7), shows a "reasonable" fit with expectations. For the two liberal issues, awareness is positively related to support among liberals and nonmonotonically related among conservatives. For the economy, where the news had a conservative valence ("Reaganomics is working"), the pattern reverses: positive for conservatives, nonmonotonic for liberals (pp. 164–165).

### Evaluating the attitude-change typology (pp. 165–166)
Zaller lists four deductions that the data support (p. 165):
1. A liberal message diffusing through a very liberal group, or a conservative message through a very conservative group, yields monotonic change with the most aware most likely to change, at least when the issue is relatively unfamiliar.
2. A moderately intense liberal message through a conservative group (or the reverse) yields nonmonotonic change, with moderately aware persons most likely to change.
3. Low-intensity messages, compared to high-intensity ones, produce a higher proportion of change among the highly aware.
4. Change on less familiar issues, compared to more familiar ones, more often occurs among highly aware persons.

The evidence for the first two "seems quite strong." Deductions 3–4 are less strongly supported because of weak measurement of intensity and familiarity and a scarcity of cases. Still, the economy (low intensity) had a higher proportion of change among the highly aware than Central America. A larger proportion of change on the two more familiar issues (segregation, Reagan approval) occurred among moderately aware persons. "Confident confirmation" of the typology, especially for familiarity, "awaits stronger evidence" (p. 166; fn. 13 notes a confounding of intensity and familiarity in the race versus presidential comparison).

**Caveat (p. 166).** All cases model a single message, with all communication favoring one side. When opposing messages flow, especially of differing intensity, patterns can differ greatly. No case examined is strictly one-sided; a two-message model comes in Chapter 9. Meanwhile the one-message model "is robust" to fairly substantial departures from one-sidedness, according to Zaller (p. 166).

### Microfoundations of resistance to persuasion (pp. 166–172)
The model claims awareness adds resistance to value-inconsistent ideas, more so as value distance from the message grows. Chapter 7 proposed three mechanisms (p. 167):
- *partisan resistance* — aware people hold cueing messages that let them recognise value-inconsistent messages;
- *inertial resistance* — larger stores of considerations ("informational ballast") offset new ones;
- *countervalent resistance* — aware people are more exposed to esoteric counter-messages that offset dominant ones.

This section looks for evidence on the first two; countervalent resistance is deferred to Chapters 9–10 (p. 167).

**Preexisting considerations and inertial resistance (pp. 167–169).** Only one case of attitude change, Reagan/Iran–Contra, offers direct observation of stored considerations. In the June 1987 NES pilot, after rating Reagan's performance, respondents were asked in an open-ended question what ideas came to mind (up to three "Any others?" probes). Half the sample was primed with Iran–Contra information; that half is dropped. The priming experiment failed to shift approval, but those primed were slightly more likely to mention Iran–Contra (fn. 14, p. 167).
- New NES codes, three of which seem to refer directly or indirectly to Iran–Contra, covered remarks calling Reagan uninformed, remarks that he does not work hard, delegates too much or chose poor aides, and remarks about involvement in the diversion of money to the Contras. With hostage-release references, these form an index of Iran–Contra considerations (p. 168).
- The index is rough and almost certainly understates the scandal's influence. Reasons: scandal-inspired remarks such as "dishonest" would not be coded; highly aware Democrats may have had many other reasons and not mentioned it; and people may not recall all influences (Lodge, McGraw and Stroh) (p. 168).
- **Expectations:** the highly aware should (1) have large stores of non-Contra considerations and (2) these should offset scandal considerations (p. 168).
- **Table 8.1** (five awareness levels from low to high):

| | Low | | Mid | | High |
|---|---|---|---|---|---|
| Non-Contra remarks (mean) | 0.68 | 1.21 | 1.30 | 1.55 | 1.63 |
| Contra remarks (mean) | 0.09 | 0.23 | 0.41 | 0.42 | 0.28 |
| Contra ÷ all remarks | 0.08 | 0.15 | 0.23 | 0.21 | 0.13 |
| N | 44 | 52 | 54 | 38 | 46 |

(p. 169; the ratio row is the average of an individual-level measure, not the ratio of the two means above it.) Expectation 1 is strongly supported. Expectation 2 is supported: the ratio of Contra to all remarks is highest among those in the middle of awareness. Zaller says this nonmonotonicity is easily statistically significant (regression of the ratio on information and information-squared, both significant at .05 one-tailed; fn. 16). It arises "in part" because highly aware people's many non-Contra considerations dilute Contra ones. Also, spontaneous mention is only 9% among the least aware, consistent with their small change in ratings (p. 169).

*Intuition note.* A person who already has many reasons for judging Reagan counts one scandal as a small share of the total. A person with few reasons is swayed more, provided the news reached them.

**Partisan resistance at the level of considerations (pp. 169–172).** Rejecting a message at first contact is "more efficient" than diluting it later. Within the RAS model, people can reject ideas only if they have cueing information, which the aware more often have (Table 4.4) (pp. 169–170).
- **Expectation:** for partisan issues, awareness should be positively related to consistent considerations (exposure effect without resistance) and nonmonotonically related to inconsistent ones. The highly aware are heavily exposed but recognise and reject. The very unaware are exposed to little. Moderately aware people are exposed but often lack cues. This is the typology applied to considerations (p. 170).
- **Test:** the 1987 pilot measured considerations on job guarantees, government services and aid to blacks. Each was coded consistent or inconsistent with the person's liberal–conservative orientation, using remarks from both waves and the stop-and-think probes (p. 170).
- **Fig. 8.7** (aggregate; data in Table 8.2) is consistent with expectations: consistent considerations rise with awareness while inconsistent ones rise then fall (p. 171). By item, results are ragged, but Zaller reads them as still essentially consistent with expectations. Table 8.2 unweighted means, in six columns grouped under Low, Middle and High awareness (the pairing within each level is not labelled in the source): consistent 2.34, 3.36, 3.33, 3.74, 4.72, 4.96; inconsistent 2.37, 2.86, 3.35, 2.92, 2.94, 2.08 (p. 172). Fn. 17 says Table 8.2 folds the ideology scale, and that the expected relationships are much stronger for liberals alone than for liberals and conservatives together. Zaller's simulations suggest the pattern could arise if conservative messages on these issues were more intense and more credible (lower $b_0$) than liberal ones (p. 171).
- **Iran–Contra by party.** Zaller also reads the nonmonotonic pattern of Iran–Contra mentions in Table 8.1 as suggesting partisan resistance: the most informed were heavily exposed but apparently less likely to internalize the news (p. 171). Table 8.3 (mean negative references): Republicans 0.25, 0.33, 0.30, 0.23 (N = 20, 18, 20, 26), nonmonotonic; Democrats 0.07, 0.28, 0.41, 0.46 (N = 27, 32, 32, 26), rising. This matches the expectation that highly aware Republicans resist more (pp. 171, 173).
- Zaller counts four opportunities to observe the expected patterns of monotonicity and nonmonotonicity (taking Table 8.2's summary data and the results of Table 8.3), and expectations were upheld in all four (fn. 18). Chance probability is about $.5^4\approx .06$ (fn. 18), with small cells. Zaller concludes the evidence is "helpful but not clinching" and promises more in Chapter 10 (p. 172).

### Age and resistance to change (pp. 172–180)
Age is a predisposition that is not manifestly political. Generational differences in susceptibility to new ideas are well documented (p. 172). If the RAS model is general, awareness × age should interact like awareness × other predispositions. But this is "by no means obvious": age could simply retard change regardless of awareness (p. 173). Zaller's argument for interaction: if racial equality is a norm created by elites and transmitted by media, the aware of each cohort are more exposed. Older aware persons may also have more contextual information with which to reject it (p. 173).

**Resistance to liberal internationalism (pp. 174–176).**
- Background: in the 1930s–early 1940s Democrats were the party of internationalism and Republicans of isolationism. After WWII the Republican Party under Vandenberg largely supported Truman's initiatives (Europe's rebuilding, alliances, the UN, Korea). By the 1950s liberal internationalism was a "mainstream" norm with few cueing messages that it was inconsistent with conservatism (p. 174; fn. 19 notes Bricker and the press treating isolationism as "provincial").
- Expectation: the standard mainstream pattern (strong positive awareness–support relation) in most groups. Among *older* Republicans, the least aware would fail to receive the message and the most aware would resist (older contextual cues from the 1930s, and perhaps more isolationist ballast). Support would be greatest among moderately aware older Republicans (pp. 174–175).
- Data: a 1951 CPS survey with a political-information measure. Support for the Truman Korean policy was measured as disagreement with the statement that the U.S. "should get out of Korea now and stay out." The model is Eq. 7.5 plus an age variable (a 5-point cohort variable, because age in years was unavailable; Table 8.7) (p. 175).
- **Fig. 8.8, results.** Among all Democrats (data not shown) and younger Republicans, awareness and support are strongly positively related. Among older Republicans, but no other segment, the relation is strongly nonmonotonic, which Zaller presumes reflects resistance by highly aware Republicans who had not forgotten their party's old isolationist line. Some coefficients are not significant, but the critical age coefficient is significant at the .07 level (Table 8.7: $-1.60$, s.e. 1.09) (p. 175).

**Resistance to the anti-Vietnam War movement (pp. 175–177).** Here the roles are reversed: it is highly aware older *liberals* who were forced to accommodate themselves to a shift in partisan norms.
- Older liberals would have experienced the "lessons of Munich," communist takeovers, and apparent deterrence in Korea, Greece, Turkey and West Berlin. If they followed partisan interpretations of these events, they would have met many arguments to "stand up to communism" (p. 176). Liberal support for internationalism weakened and then reversed during the war. Zaller says "liberalism," not the Democratic Party, shifted, because the party had a large conservative wing (fn. 20).
- Expectation: among younger liberals, awareness is positively related to change toward the new liberal norm. Among older liberals, a nonmonotonic relation, with moderately aware ones most susceptible (pp. 176–177).
- Data: CPS election surveys 1964–1970, with an item offering three options: pull out entirely, keep soldiers there but try to end the fighting, or take a stronger stand even if that meant invading North Vietnam. The last two count as war support (p. 177).
- **Table 8.4** (liberals = upper 40% of dove measure; ages 21–35, 36–55, 56+ in 1966; change rate $=100\times(\text{Support}_{66}-\text{Support}_{70})/\text{Support}_{66}$; four awareness columns, Low to High; p. 178). Change rates from 1966 to 1970:

| Cohort | Low | | | High |
|---|---|---|---|---|
| Youngest | 17 | 25 | 37 | 53 |
| Middle | 2 | 14 | 41 | 31 |
| Oldest | −6 | 25 | 71 | 15 |

- Zaller reads the table as "clearly" supporting the expectation despite noise from small cells. The standard error for a difference between two cells with N = 25 and a true mean of .40 is .14 (95% CI ±.28; fn. 21). Younger liberals show a positive awareness relationship, and middle-aged and especially older liberals a nonmonotonic one (p. 177). Example, oldest cohort: support fell from 73% to 21% among the second-highest awareness group but only from 79% to 67% among the highest (p. 178).
- **Anomaly:** the $-6$ among the least aware older liberals means they became *more* supportive. Zaller says Chapter 9 will give evidence that this contrarian change is "probably quite real," and a more complicated model is needed to explain it (p. 177). Meanwhile, Zaller says Table 8.4 together with the Korean data indicates that the RAS model helps to specify the effect of age on susceptibility to change (p. 177).

**Generation and race (pp. 177–180).** Expected triple interaction: only among people who are both liberal and young should there be a positive linear awareness–racial liberalism relationship. As age and conservatism increase, the relationship should become increasingly nonmonotonic (p. 178). **Fig. 8.9** shows 1956 support for mandated desegregation by cohort (e.g. 20, 50, 75 years), ideology and awareness (same model as Fig. 8.6 but with age shown). The data "conform to expectation" (pp. 178–179; fn. 22 notes that the panel showed too little change to show a pattern).
- Why would aware older *liberals* resist federal desegregation? Zaller's answer: from the late 19th century until Roosevelt's attack on the Supreme Court in the late 1930s, judicial activism almost invariably served conservative interests, and states' rights and judicial self-restraint often protected liberal policies. Aware older liberals had learned the "dangers of judicial activism" too well to be entirely comfortable with *Brown*, just as they had learned Munich too well to oppose Vietnam (p. 179). Zaller adds a possible parallel in some contemporary liberals' opposition to affirmative action (pp. 179–180).

**General effects of age (p. 180).** If age is a predisposition like any other, no case-by-case justification is needed. Whatever its source (past learning, physiology, self-interest, circumstances or conservatism), the RAS logic applies. Zaller adds that he sees no reason to believe age will generally be associated with greater resistance. For a salient Medicare-benefits proposal, support among the elderly might rise with awareness without resistance, and resistance would be expected among the aware young. The claim is that the effects of age, "whatever their direction," can be specified by the RAS model (p. 180).

### Summary (p. 180)
The one-message model, though a simplification, generates different expectations for different circumstances, and these remain plausible after testing. Different patterns arise for different issues and communications. The formation of considerations behind closed-ended answers also appears to follow the model's logic. The model specifies the effect of age. Evidence is accumulating in support of the RAS model, though no single piece of it is conclusive (p. 180). The next two chapters take up Vietnam and candidate evaluation.

### Appendix: estimating the presidential popularity model (pp. 181–184)
- **Baseline and change periods.** Disapproval was 32% in the NES postelection sample before Nov. 28 (no time trend) and averaged 39% afterwards (highly significant). The break is dated to the day after Thanksgiving, three days after Meese announced an administration self-investigation. The pilot (which reinterviewed 457 respondents) showed 48%. Zaller used pre-Nov. 28 as the baseline and June 1987 as the postchange period (p. 181). Fn. 24: using the pilot's own fall interviews as baseline gave similar raw patterns, but the model could not be fitted reliably.
- **Estimation.** Eq. 7.7 was estimated first without constraints (Table 8.5, left). Coefficients had good magnitudes but large standard errors. Two constraints were added: remove the floor parameter, and force awareness to have the same effect on reception in baseline and change subfunctions. Fit did not worsen significantly ($F[2,1905]=1.6$, n.s.), and the two key coefficients (awareness effects on reception and acceptance in the change model) became more stable and into conventional significance ranges (p. 181).
- **Table 8.5 (two-constraint column).**
  - Baseline reception: intercept 2.12; awareness 0.79 (.43), constrained equal to the change-reception awareness.
  - Baseline acceptance: intercept $-0.92$; awareness 0.07 (.15); party 0.91 (.10); egalitarianism 0.36 (.08); Central America attitudes 0.23 (.09).
  - Change reception: intercept $-0.22$; awareness 0.79 (.43).
  - Change acceptance: intercept 0.68; awareness $-2.17$ (1.22); party 1.76 (.94); egalitarianism 1.64 (1.14); Central America 3.10 (1.74).
  - Residual sum of squares 421.91 ($N_1=1463$, $N_2=457$) (p. 182).
- Predispositions' effects appear to have increased over the period, but only the Central America increase survives an F-test. This confirms Krosnick and Kinder's finding that Iran–Contra "primed" Central America attitudes as determinants of approval (pp. 181–183).
- **Table 8.6** (Eq. 7.3 coefficients, intercept $a_0$ / awareness $a_1$): North 0.88 / 1.12; Wright $-0.42$ / 1.92; death penalty $-1.96$ / 1.03; DC-10 3.48 / 2.43 (p. 183).
- **Table 8.7** (Eq. 7.5). Acceptance-function age coefficients: school desegregation $-0.038$ (.017), freeze $-0.008$ (.008), economic news $-.033$ (.01), Korea $-1.60$ (1.09). Reception awareness coefficients: 0.72, 1.15, 1.21, 1.58 respectively (p. 184).

## Toy example (ours, not from the text)
Take three equal-size groups of conservatives (low, middle, high awareness) hearing a liberal message. Use made-up numbers for the two factors in the RAS product $P(\text{change})=P(\text{receive})\times P(\text{accept})$.

- Acceptance (falls with awareness for opposed people): 0.9, 0.5, 0.2.
- **Low-intensity message**, reception 0.05, 0.40, 0.90:
  - change = $0.05\times0.9=0.045$; $0.40\times0.5=0.200$; $0.90\times0.2=0.180$.
  - Total 0.425. Share among low-awareness group: $0.045/0.425\approx 10.6\%$. Peak at the middle group.
- **High-intensity message**, reception 0.60, 0.95, 0.99:
  - change = $0.60\times0.9=0.540$; $0.95\times0.5=0.475$; $0.99\times0.2=0.198$.
  - Total 1.213. Share among low-awareness group: $0.540/1.213\approx 44.5\%$. Peak moves to the low group.

Same acceptance pattern, higher reception: the proportion of change among the least aware rises from about 11% to about 45%. This is the chapter's deduction 3. Awareness helps reception but hurts acceptance, so the product can rise and then fall (deduction 2). (For the actual reception function with $f=0$, $a_0=0$, $a_1=1.25$ and awareness 0: $1-1/(1+e^0)=0.5$.)

## Concepts
- [[receive-accept-sample-ras-model]] — here the "reception–acceptance" part of RAS: opinion change needs reception of a message and then acceptance; both depend on awareness (pp. 151, 154).
- [[political-awareness-sophistication]] — habitual attention to and knowledge of politics. Raises reception and, for value-inconsistent messages, resistance (pp. 151, 166–167).
- [[message-intensity]] (new) — a message's penetrating power, set jointly by coverage and public interest; the $a_0$ parameter (pp. 152–154).
- [[issue-familiarity]] (new) — size of the public's store of existing considerations on an issue; is captured by $b_0$; more familiar issues have lower $b_0$ (e.g. $b_0=0$ versus $+3$ in the typology), which lowers acceptance and total change (pp. 154–155).
- [[inertial-resistance]] (new) — dilution of new messages by stored considerations ("informational ballast") (pp. 154, 167).
- [[partisan-resistance]] (new) — rejection of value-inconsistent messages on first encounter, possible only with cueing information (pp. 167, 169–170).
- [[countervalent-resistance]] (new) — offsetting by esoteric counter-messages the aware are exposed to; deferred to Chs. 9–10 (p. 167).
- [[nonmonotonic-opinion-change]] (new) — change that peaks among moderately aware people. In the model it arises, for a moderately intense message reaching a group opposed to it, when reception rises and acceptance falls with awareness (pp. 165, 175).
- [[one-message-model]] (new) — the model of a one-sided information flow, to be replaced by a two-message model in Ch. 9 (p. 166).
- [[consideration]] (new, or the RAS primitive) — a stored idea that can sway a response; measured here by open-ended remarks (pp. 151, 168).
- [[priming-agenda-setting]] — Krosnick and Kinder: Iran–Contra raised the weight of Central America attitudes in approval (p. 183). Canon-adjacent; used lightly here.

## Canonical instances
- [[news-diffusion-1989-pilot]] — North, Wright, death-penalty and DC-10 stories reached very different shares of the public (pp. 152–154).
- [[reagan-iran-contra-approval]] — disapproval rose from 32% to 48%; change concentrated among the moderately aware (pp. 159–162).
- [[central-america-baseline-case]] — medium-intensity, low-familiarity benchmark for the typology (pp. 158–159).
- [[school-desegregation-1956]] — high-familiarity, medium-intensity new issue; age-by-ideology pattern (pp. 162–164, 178–179).
- [[nuclear-freeze-1982]] — low-familiarity, medium-intensity new issue (pp. 163–165).
- [[korean-war-support-1951]] — nonmonotonic support among older Republicans (pp. 175–176).
- [[vietnam-war-liberal-cohorts]] — older liberals' resistance to the anti-war shift (pp. 176–178).

## Bridges (candidates)
- [structural-analogy] reception × acceptance product giving a hump-shaped response ↔ pharmacology/ecology: dose–response with a rising uptake term and a falling effectiveness term — both are products of opposing monotone factors.
- [structural-analogy] inertial resistance (many stored considerations dilute a new one) ↔ Bayesian updating: a strong prior moves little on one new observation. (Zaller does not use Bayesian language in this unit.)
- [structural-analogy] age-linked resistance from earlier partisan lessons ↔ path dependence: earlier commitments shape later openness to change.

## Questions this raises
- How does the typology change once opposing messages of different intensity are modelled (the promised two-message model, p. 166)? Does inertial resistance remain separable from countervalent resistance?
- Can intensity and familiarity be measured independently (public knowledge surveys, no-opinion rates) so the typology is tested without assigning cases informally?
- If the contrarian shift among the least-aware older liberals is "probably quite real" (p. 177), what mechanism produces change opposite to the elite message?
- Could the partisan-resistance pattern for considerations, sensitive to folding the ideology scale (fn. 17), differ when liberal and conservative messages differ in credibility?

## Reading notes
- Printed page = pdf − 16 (pdf 167 = printed 151).
- No page image was supplied for printed p. 154. Equation 7.5 is reconstructed from a garbled text layer ("1 -I- Exp", "/" for $f$, "^Predispositions") plus fn. 5 and the appendix mention of a floor parameter. The exact form of the predisposition term and the sign convention should be checked against the book.
- Table 8.2: the paired columns within each awareness level are not labelled in the source, so I did not assign meanings to them. Fn. 17 says the ideology scale was folded at the midpoint.
- Table 8.4 labels only "Low" and "High" over four columns.
- Misprints/oddities seen in the images: Table 8.7 reads "Domestic policy attiudes"; the subscripted "Time$_1$" in the Table 8.5 note comes through the text layer as "Timei"; the source varies between "egalitarianism" and "Equalitarianism"; the Fig. 8.8 raw-data N rows are not clearly tied to cells.
- Fn. 16 and fn. 18 describe significance tests only briefly; they are reported as stated. Fn. 17 (p. 171) equates "more credible" with lower $b_0$, whereas p. 154 says lower $b_0$ means lower acceptance; both are reported as printed. Equations 7.3 and 7.7 are referenced but not printed in this unit.
- The unit contains no exercises.
