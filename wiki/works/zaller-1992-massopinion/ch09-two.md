---
id: zaller-1992-massopinion/ch09-two
work: zaller-1992-massopinion
unit: 9 Two-sided information flows
pages: 185-215
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Two-sided information flows

## L0 — One line
Zaller argues that public opinion on an issue responds to the relative intensity of competing (pro and con) message flows, filtered by each citizen's awareness and values, and a two-message extension of his Receive–Accept–Sample (RAS) model of opinion formation fits Vietnam War opinion in 1964–70.

## L1 — The gist (≤ 120 words)
Earlier chapters modelled opinion change as a response to a one-sided message flow. This chapter asks how opinion moves when a dominant message and a weaker, opposing ("countervalent") message compete. Zaller builds a "two-message" version of his Receive–Accept–Sample (RAS) model. Each message is received, accepted and recalled with probabilities that depend on awareness, values (acceptance only) and message intensity (reception only). He fits it to four Center for Political Studies (CPS) surveys on Vietnam (1964–70). The fitted intensities correspond closely to newsmagazine story counts, and the model fits how hawks and doves at different awareness levels changed. Zaller concludes that the results support the claim that attitudes respond to the relative intensity of competing communications.

**Prerequisites:** logistic function and multinomial logit; probability of independent events; the RAS axioms (reception, resistance, accessibility) and the mainstream/polarization patterns from earlier chapters; instrumental variables (basic idea).

## L2 — Key ideas (5–10 bullets)
- A two-message model lets a dominant and a countervalent message affect different parts of the public, depending on awareness, values and relative intensity (pp. 185, 189).
- Vietnam is the test case because elite positions and both message intensities changed quickly (pp. 186, 188). The magazine story counts, Hallin's TV study, the Times Index (volume only) and congressional actions are broadly consistent. For 1970, the magazine counts and the actions of officeholders point somewhat differently (pp. 188–189).
- Reception, acceptance and recall are each logistic functions (S-shaped curves that turn a linear score into a probability). Message intensity is the reception intercept $a_{0kt}$, which varies by message and time (Eqs. 9.1–9.8, pp. 191–195).
- The values (hawk–dove) variable is a proxy built with Franklin's two-sample instrumental-variables technique (using a 1988 survey that has direct hawk–dove items), with first-stage $r^2$ of only 0.14 (pp. 196–197).
- The effects of awareness and values on resistance appear only after elites divided (1966 on). Intensities inferred from opinion data alone match the story counts "remarkably" well (pp. 200–203).
- Vietnam shows countervalent resistance: highly aware doves turned against the war in 1964–66 while the national trend was prowar. Highly aware hawks largely held their ground; their war support never really declined (pp. 203–205, 207).
- Black opinion resembled white conservatives' until 1966 and white liberals' afterwards, which the author suggests reflects different leadership cues (pp. 206–207).
- The Chapter 8 typology (patterns derived assuming a one-sided flow) appears to be a good approximation when one message holds steady or fades while the other grows. It strictly holds only for one-sided flows (p. 208).
- The Vietnam case adds to Converse's account of belief systems (clusters of attitudes seen as "going together"): lags in adopting new belief elements may produce unexpected "constraint" (pp. 209–210).

## L3 — Walkthrough

### Introduction (pp. 185–186)
- Earlier chapters modelled change as a response to a one-sided stream. Real flows are rarely completely one-sided for long. Example: some Republican senators defended Reagan during Iran-Contra (p. 185).
- Goal: a model for a dominant message plus a less intense countervalent message that partly offsets it. This is possible because the two messages can affect different segments of the public (p. 185).
- Larger aim: show how the mainstream pattern (elite consensus; most aware follow it most strongly) and the polarization pattern (partisan elite split) form and change as message intensities change (p. 185).
- General claim: opinion responds to the relative intensity and stability of opposing liberal and conservative flows. The labels give only the direction of a message (pp. 185–186).
- Few issues offer a crisp change in relative intensity that good surveys captured. Vietnam is the one case the author knows of (p. 186). Plan: an illustration, a statistical model, then measures and results (p. 186).

### Ebb and flow of support for the Vietnam War (pp. 186–190)
**Why Vietnam (p. 186).**
- Liberal elites mostly supported the war in 1964 and mostly opposed it in 1970. Conservative elites supported it throughout.
- Johnson pushed harder after the 1965 ground-troop commitment than in the 1964 campaign.
- The antiwar message was almost absent in 1964 and "hardly more than a whisper" in 1966. By 1970 it was probably as intense as the prowar message, perhaps more.
- The issue moved from mainstream (1964) to polarization (1970).
- CPS election studies asked an almost identical question in four surveys and carried good awareness and values variables (pp. 186–187).

**Measuring the information flow (pp. 187–189).**
- A research assistant, unaware of the author's expectations, content-analysed *Time*, *Newsweek* and *Life* (1963–70). He took all issues with Vietnam-related cover stories and rated each story prowar, antiwar or balanced (p. 187).
- Prowar stories were moderately prominent in 1963–4 (about four per magazine per year with a cover). Antiwar stories averaged about 1.5. Early antiwar stories reported difficulties that could be read as reasons to strengthen the commitment, not partisan opposition (pp. 187–188).
- Prowar coverage rose from 1964 to 1966 and stayed high to about 1968. Then it fell almost to 1964 levels. Antiwar coverage rose every year and appears to have caught and even overtaken prowar by 1970 (p. 188, Fig. 9.1a).
- Total magazine coverage fell in 1970. A count of *New York Times Index* pages suggests total volume stayed high (Fig. 9.1b). The author reads this as war coverage losing novelty for the periodicals (p. 188).
- Hallin's TV study: administration spokesmen "heavily predominant" before spring 1968, then relative parity after Tet. TV volume rose to about 1966 and then stayed roughly steady (p. 188).
- Congressional actions. The Gulf of Tonkin resolution passed 414–0 (House) and 88–2 (Senate) in 1964. Fulbright hearings in 1966 brought the first hints of opposition. Early funding cut-offs in 1967 were soundly defeated, e.g. 372–18 (House, 1967) (pp. 188–189 and n. 2).
- In 1969–70, Vietnamization and defeated cut-off attempts (closer margins) kept a supportive stream among officeholders. This conflicts with the magazine data, which suggest an antiwar tilt by 1970 (p. 189, n. 3).
- Synthesis (the author: "it appears"): both messages grew from 1964 to 1966. The prowar message was far more intense at first but lost the advantage by 1970. They may have been roughly even by 1970, at high overall volume (p. 189).

**The two-message idea (p. 189).** Citizens are exposed to one flow on each side. Effects differ across segments by relative intensity. Expectation for 1964–66:
- The still-faint antiwar message should have its greatest impact on the most aware liberals, who receive it and are sympathetic.
- The rise in the prowar message should matter more for moderately and less aware people. The most aware had probably received it already in 1964.

**Figure 9.2 (p. 190).** Among liberals (doves), support for the war rose between 1964 and 1966 among the less aware, "presumably" because they were now heavily exposed to prowar arguments. The most aware doves became less supportive, "presumably" because they received and accepted an antiwar message inaudible to the less attentive. The author calls this rough but "the clearest illustration" of the chapter's main point (p. 190). The CPS item changed after 1970, so the analysis ends there (p. 190).

> *Intuition note.* Each message reaches the best-informed first. A message already loud at the top of the awareness scale mainly gains new audience lower down. A new faint message has its greatest impact at the top, among aware people who are also sympathetic to it. So the two messages move different groups at the same time.

### A two-message model of attitude change (pp. 190–195)
**Simplifying assumptions (p. 191).**
1. Within each two-year period, communications fall into a fixed, small number of "messages". There are $N$ prowar messages of one uniform intensity and $N$ antiwar messages of another uniform intensity.
2. A consideration stays active no more than two years unless reinforced by reception and acceptance of an identical argument. Each survey can then be modelled from the preceding two years. Longer lags are not identifiable with four surveys (n. 4 points to a lagged model in Ch. 10, App. B).
3. People answer using the first consideration that comes to mind, not whatever is accessible as axiom A4 allows.

**Reception (pp. 191–192).**
$$\text{Prob(Reception)}_{ikt}=1-\left[1+\exp(a_{0kt}+a_1\,\text{Awareness}_i)\right]^{-1}=RE_{ikt}\tag{9.1a}$$
This is logistic (the text layer may hide a floor term $f$; see Reading notes). $i$ indexes persons, $k$ the message (prowar/antiwar), and $t$ the survey (64, 66, 68, 70). The intercept $a_{0kt}$ is the message-intensity parameter. With 2 messages × 4 periods, there are eight $a_{0kt}$ (p. 192). The slope $a_1$ is kept time-invariant because the Vietnam data are not strong enough for credible tests of time variation (p. 192, n. 5).

**Acceptance (p. 192).** By the Resistance Axiom, people reject messages inconsistent with their predispositions, but only if they have contextual information. Reception and cue accessibility rise with awareness (axioms A1, A3). So acceptance given reception should fall jointly with awareness and ideological distance:
$$\text{Prob(Accept}\mid\text{Recept)}_{ikt}=\left[1+\exp(-b_{0k}-b_{1t}\,\text{Awareness}_i-b_{2t}\,\text{Distance}_i)\right]^{-1}=\text{Accept}_{ikt}\tag{9.2}$$
(form as extracted; see Reading notes). The intercept $b_{0k}$ varies by message, since some messages may meet more resistance. Example (the author: "one might suspect"): the liberal antiwar message may meet more resistance because it runs against an established policy, or may be inherently less attractive. The coefficients carry $t$ because elite cues changed once liberal elites began to oppose the war around 1966. This lets the model test whether awareness and distance became more strongly linked to resistance after that (pp. 192–193).

**Recall (p. 193).** It is assumed that a typical consideration, once formed, is accessible with a probability that varies with awareness and nothing else:
$$\text{Prob(Recall)}_i=1-\left[1+\exp(c_0+c_1\,\text{Awareness}_i)\right]^{-1}=R_i\tag{9.3}$$
No $kt$ subscripts: every consideration is equally likely to be sampled, whatever its date or side. Recall's decline with time since formation (axiom A3) is omitted because it has no observable implications here (n. 6).

**Accessibility of a message as a consideration (p. 193).**
$$\text{Prob(Accessible)}_{ikt}=RE_{ikt}(\text{Accept}_{ikt})R_i=AC_{ikt}\tag{9.4}$$
Relative accessibility of prowar considerations, with $N$ messages each side:
$$\frac{\sum^N RE_{iPt}(\text{Accept}_{iPt})R_i}{\sum^N RE_{iPt}(\text{Accept}_{iPt})R_i+\sum^N RE_{iAt}(\text{Accept}_{iAt})R_i}\tag{9.5}$$

**Simplification (p. 194).** The $R_i$ cancel from numerator and denominator. Equal numbers of equally intense messages make the summation signs superfluous:
$$\frac{RE_{iPt}(\text{Accept}_{iPt})}{RE_{iPt}(\text{Accept}_{iPt})+RE_{iAt}(\text{Accept}_{iAt})}\tag{9.6}$$
Relative accessibility depends on the reception-acceptance ratios of the two messages. These vary with time, awareness and ideological distance (p. 194).

**"No opinion" (p. 194).** Presumably people say this when no consideration for either side comes to mind. The chance of none of the $2N$ considerations being accessible is $\prod(1-AC_{ikt_j})$ over the $2N$ messages. With equal numbers of prowar and antiwar messages, writing $\prod^N$ for the product of $N$ such factors:
$$\text{Prob(No opinion)}_{it}=\prod^N(1-AC_{iPt})\prod^N(1-AC_{iAt})=\prod^N(1-RE_{iPt}\text{Accept}_{iPt}R_i)\prod^N(1-RE_{iAt}\text{Accept}_{iAt}R_i)$$
$$\text{Prob(Opinion)}_{it}=1-\prod^N(1-AC_{iPt})\prod^N(1-AC_{iAt})\tag{9.7}$$

**Basic model (pp. 194–195).** Probability of a prowar response = (probability of recalling any consideration) × (relative accessibility of prowar considerations):
$$\text{Prob(prowar response)}_{iPt}=\Bigl(1-\prod^N(1-AC_{iPt})\prod^N(1-AC_{iAt})\Bigr)\frac{RE_{iPt}\text{Accept}_{iPt}}{RE_{iPt}\text{Accept}_{iPt}+RE_{iAt}\text{Accept}_{iAt}}\tag{9.8}$$
Antiwar and "No opinion" responses use correspondingly modified expressions (p. 195). The model is much more versatile than the Chapter 7 one-message model, though both capture many types of change. App. A gives a simpler alternative form without considerations (p. 195).

> *Intuition note.* Eq. 9.8 splits a survey answer into two steps. First, is anything on the person's mind at all (9.7)? Second, if so, which side is more likely to be on top (9.6)? Intense messages raise the first. The ratio of reception-times-acceptance sets the second.

### Data and results (pp. 195–207)
**Data problem: no panel (p. 195).** The CPS surveys are not reinterviews. Comparisons must be between similar types of people over time, e.g. "highly informed doves". Awareness scales (alpha ≥ .80) were built in each survey from information items. Items vary by year but should serve about equally well, like different random 20-word spelling tests (p. 195).

**Values measure (pp. 195–197).**
- Left–right "ideology" from the liberal–conservative feeling-thermometer difference may be partly caused by Vietnam opinion itself (endogeneity). Party has the same problem and predicts war attitudes more weakly (p. 196, n. 7).
- Hawk–dove predispositions are the more relevant dimension, but 1964–70 CPS surveys have no direct measure (p. 196).
- Solution: Franklin's (1989) two-sample instrumental-variables technique, whose estimates are asymptotically unbiased and efficient (p. 196). Steps:
  1. Use the 1988 NES, which has hawk–dove items (e.g. strong military versus bargaining table to keep peace).
  2. Pick auxiliary variables (gender, religion, racial attitudes) that relate to hawk–dove values there and appear identically in the Vietnam datasets.
  3. Regress hawk–dove values on the auxiliaries in 1988, assuming the relationship is time-invariant.
  4. Use those coefficients as weights to build an instrumental variable in the 1960s data (pp. 196–197).
- Limitation: the first-stage $r^2$ is only 0.14, yet the measure "performs extremely well" (p. 197). Details in App. B.

**Interest-filter discontinuity (p. 197).** In 1964 and 1966 only people "paying attention" to Vietnam were asked about the war. About 20% failed this in 1964 and 7% in 1966. The filter was dropped in 1968 and 1970. Volunteered "No opinion" fell from 13% (1964) to 9% (1966) to 7% (1968). So "No opinion" really kept declining, but the CPS data probably overestimate the 1966–68 decline (p. 197). Remedy: a floor parameter $f_t$, with different values in 1964–66 and 1968–70:
$$\text{Prob(RE)}_{ikt}=1-\left[1+f_t+\exp(a_{0kt}+a_1\,\text{Awareness}_i)\right]^{-1}=RE_{ikt}\tag{9.1b}$$

**Estimation (p. 198).**
- Multinomial maximum likelihood on three categories (support, oppose, no opinion), 5,002 respondents in four datasets. Whites are analysed in the main text; blacks separately. Hispanic and Asian-American cases are too few. "Support" combines two prowar options. A "three-message model" would be desirable (p. 198, n. 9).
- First estimates "underfit" trends visible in the raw data. Adding an awareness × values term to the acceptance function improved this. The author says no substantive conclusion depends on it (p. 198, n. 10).
- Unconstrained estimates (Table 9.1) have very high standard errors. The author gives two reasons. (i) The data do not reveal the actual intensities or the number of messages, which gives severe multicollinearity: few intense messages and many weak ones fit equally. (ii) Awareness plays three roles (memory search, reception, resistance) and enters several interactions (p. 198).

**Table 9.1, selected coefficients (standard errors in parentheses; pp. 199–200).**

| Function / term | Unconstrained | Constrained |
|---|---|---|
| Reception: message intercept / slope | eight $a_{0kt}$ (Fig. 9.3) | −5.68 (1.29) / 1.71 (0.64) |
| Reception: awareness | 0.51 (0.32) | 0.50 (0.17) |
| Floor 64–66 / 68–70 ($f_t$) | 0.008 (0.11) / 0.04 (0.53) | 0.01 (0.02) / 0.06 (0.03) |
| Acceptance: conservative-message intercept | 1.43 (2.36) | 2.31 (1.48) |
| Acceptance: liberal-message intercept | −1.06 (3.83) | −1.23 (0.43) |
| Acceptance: awareness / awareness × time | −0.08 (1.09) / −0.27 (0.78) | 0.06 (0.50) / −0.43 (0.51) |
| Acceptance: hawk–dove / × time | 0.11 (0.26) / 0.19 (0.33) | 0.19 (0.30) / 0.14 (0.30) |
| Acceptance: hawk–dove × awareness / × awareness × time | 0.01 (0.27) / 0.09 (0.27) | −0.07 (0.32) / 0.22 (0.35) |
| Acceptance: time / male | 0.29 (2.55) / −0.18 (0.21) | 0.47 (0.41) / −0.05 (0.16) |
| Recall: intercept $c_0$ / awareness $c_1$ | 3.19 (2.48) / 1.66 (0.94) | 3.47 (2.36) / 1.75 (0.94) |
| Number of messages $N$ | 35.2 (560) | 24 (fixed) |
| df / residual sum of squares | 9980 / 1643.67 | 9987 / 1650.77 |

Time = 0 in 1964 and 1 afterwards. The hawk–dove coefficient is negative in the conservative-message acceptance function and positive in the liberal one (Table 9.1 note, p. 200). The standard errors are approximate (p. 198).

**Unconstrained results: elite cues activate predispositions (p. 200).**
- In the acceptance function, the effects of ideology and awareness rise from 1964 (mainstream consensus) to 1966–70 (elite disagreement). The direct effect of values increased by a factor of 1.7, awareness by 3.4, and the awareness × values interaction by 9. (Added check: these match the time-interaction coefficient divided by the 1964 coefficient: 0.19/0.11, 0.27/0.08, 0.09/0.01.)
- The author reads this as supporting his point that the effects of values and awareness "are not automatic but depend on elite cues for activation" (p. 200). (Footnote 11: awareness was positive in the acceptance function in Zaller 1991, owing to a change of functional form.)

**Estimated message intensities (pp. 200–201, Fig. 9.3).**
- The $a_{0kt}$ values have little absolute meaning, but their changes do. The model estimates that the prowar message rose from 1964 to 1966, fell back moderately in 1968 and fell again in 1970. The antiwar message was initially very weak and rose steadily until 1970, when it was more intense than the prowar message (p. 200).
- These estimates are inferred from opinion data alone. They correspond "remarkably" well to the Figure 9.1a story counts, "a little too good". Other media indicators and the App. A model (Zaller 1991) give somewhat different results. The correlation between the Zaller (1991) $a_{0kt}$ and log story counts is 0.79, and 0.89 for this book's version (p. 201, n. 12).

**Constrained model (p. 201).**
- Constraint 1: $a_{0kt}$ is a linear function of the logged story counts of Fig. 9.1a (Table 9.1: intercept −5.68, slope 1.71).
- Constraint 2: $N$ is set to 24, the months between surveys. This raised residual variance only slightly. Any $N$ from about 8 to 60 fits almost equally well, and it greatly reduced standard errors. It also speeds convergence (nn. 12–13).

**Constrained results (pp. 202–203).**
- "All but one" reception and recall coefficients are said to be significant. The exception is the floor $f$ in 1964–66, which was expected to be zero (p. 202). (Table 9.1 shows the recall intercept with SE 2.36 on 3.47; see Reading notes.)
- Acceptance coefficients remain imprecise. On F-tests the block capturing increased effects after 1964 (Awareness × Time, Values × Time, Awareness × Values × Time, Time) is significant: $F[4,9987]=2.39$, $p<.05$. The interaction terms are also significant on an F-test (p. 202).
- In plain terms: awareness and values had significant effects on resistance, but only after elite divisions activated predispositions (pp. 202–203).
- Male gender is insignificant in the constrained model, although visible in raw data. The author guessed double entry, since gender is in the instrument. With the feeling-thermometer difference instead, gender is significant ($F[2,9987]=13.68$, $p<.01$). The modest gain in fit over the instrument suggests slight endogeneity of the thermometers and good performance of the instrument (p. 203, n. 14).

> *Intuition note.* Before 1966 the elites were nearly united, so knowing a person's values and awareness told little about who resisted what. Once elites split, informed people could tell which message belonged to their side, and resistance began to track values.

**Patterns of support, doves (pp. 203–204, Fig. 9.4).**
- Hawks and doves are persons at ±1.85 on the hawk–dove variable (n. 15).
- 1964: awareness related roughly linearly to support, the mainstream or "follower" pattern (p. 203).
- 1966: Johnson's "peace offensives" and similar efforts raised support mainly among the middle to low awareness groups. The antiwar message, barely audible to most, began to convert the most informed doves. They were the only segment to become less supportive between 1964 and 1966 (pp. 203–204).
- 1968: a small prowar trend remained among the least informed doves (statistically uncertain). A much larger antiwar movement occurred in the middle and upper ranges. The balance that favoured the war in 1966 now worked against it (p. 204).
- 1970: all segments of the dove group turned against the war. The biggest shift came after Nixon took office in 1969. The author notes Mueller's observation that doves found it easier to oppose a Republican-led war. The model picks up this acceleration without any term for presidential leadership; its only source of change is the media information pattern (p. 204).

**Hawks (p. 204).**
- Patterns parallel those of doves, except that war support among the most aware hawks never really declines.
- Support grew in all awareness groups in 1964–66. In 1968 gains among the less informed roughly balanced small losses among the most informed. In 1970 support fell only slightly, mainly among moderately aware hawks.
- Awareness remains positively associated with what is, among hawks, a strong partisan norm (p. 204).

**Comparing hawks and doves (pp. 204–205).**
- The least informed in each camp behave alike. They are late to support the war and late to respond to antiwar information. Moderately aware hawks and doves also behave alike. They rise with the prowar message and then abandon the war once the antiwar message becomes loud enough to reach them.
- The most aware ideologues differ. Highly aware doves turn against the war from 1966. Highly aware hawks largely hold their ground. The author's explanation is that hawks were sustained by congenial prowar messages and highly resistant to the antiwar message (pp. 204–205).

**"No opinion" (p. 205, Fig. 9.5).**
- "No opinion" falls with awareness. The relationship is much steeper early in the war than later. The model accommodates this because opinionation (Eq. 9.4, via $a_{0kt}$) carries message intensity, and more intense messages mean fewer "No opinion" answers (n. 16).
- The model predicts a small rise (about 2 points among the lowest awareness) from 1968 to 1970. It is invisible in the raw data. Pierce, Beatty and Hagner (1982) report "No opinion" creeping up in 1971, perhaps because communications on the war weakened (p. 205).

**Afro-Americans' support (pp. 206–207, Fig. 9.6).**
- Few black cases make confident assessment difficult. Figure 9.6 is smoothed by regression (p. 206).
- In 1964–66, black patterns resemble white conservatives', not liberals'. Awareness is positively related to support, and the rise in support is mainly among the less and moderately aware. There is no indication that blacks were initially reluctant to support the war. A tendency to lower support disappears with a control for awareness (p. 206, n. 17).
- After 1966 black patterns resemble white liberals': support fell, especially among highly and moderately informed blacks, as the antiwar message diffused (p. 206).
- The opinion data cannot by themselves explain the shift. The author offers an "obvious explanation". Johnson had won two civil rights bills and launched the War on Poverty, so blacks probably gave his war statements more credibility. By 1968 many black leaders, including the recently assassinated King, opposed the war (p. 207).
- Conclusion: blacks were as responsive as whites to the flow of information, but judged it by somewhat different leadership cues (p. 207).

### Implications (pp. 207–211)
1. **Countervalent resistance (p. 207).** The first clear evidence that highly aware doves resisted the dominant prowar message of 1964–66, in part because of exposure to the antiwar message. The latter, though less intense, neutralized the dominant message and moved some of the most aware doves against the national trend. The author gives as the reason that both messages were growing, so each could produce converts in a different part of the public. This pattern is "probably unusual", but weaker countervalent flows probably induce resistance in other cases too (p. 207).
2. **Forms of change and the Chapter 8 typology (p. 208).** Change under a two-sided message takes different forms, depending on relative intensities and the prior distribution of opinion. Some do not match the Chapter 8 typology, which assumed a one-sided flow. The author suggests the typology is nonetheless a good approximation when one message is steady or fading while the other grows. He says "perhaps" the most common stimulus, and all mass attitude changes he knows of, except 1964–66 Vietnam, appear to fit this. Late-war Vietnam (Fig. 9.7) is an example. The typology's patterns strictly hold only under one-sided flow. One-sidedness would seem most likely when the interval between measurements is short and the gain in one message's relative intensity is large (p. 208).
3. **Belief systems and Converse (pp. 208–210).**
   - **Converse's view as the author recounts it:** creative elites manufacture belief packages that diffuse imperfectly, so only the most aware absorb them fully (p. 209).
   - Here an antiwar element was gradually added to the liberal package. The most attuned liberals adopted it first and aware conservatives resisted, in the spirit of Converse.
   - Unexpected turns. Highly aware, older liberals continued to resist the antiwar element as late as 1970. As they presumably saw it, the constraints of liberal ideology ran toward support, as liberal internationalism. Moderately and less aware liberals moved prowar in 1964–66 and then back. They may have thought they were moving in a liberal direction, given Johnson and the internationalist tradition.
   - The author finds no contradiction with Converse. In a dynamic setting, various types of lags "may lead to unexpected forms of ideological constraint" (p. 210).
4. **The main claim (p. 210).** The results are "credible evidence" that attitudes respond to the relative intensity of competing communications. Under elite consensus the response is relatively nonideological, with the most aware following the consensus most strongly. Under partisan elite division the response becomes ideological, most among the most aware. Polarization reflects the relative intensity of the opposing flows. In 1966 the conservative message was much more intense, so polarization was modest and skewed conservative. As the flows balanced, support fell and polarization grew (Fig. 9.8).
   - Footnote 20: in 1970 the model puts the antiwar message ahead in intensity yet public support for the war exceeded opposition. The reason is greater resistance to the antiwar message at comparable reception, captured in the acceptance-intercept difference (Table 9.1) (p. 210).
5. **Limit (p. 211).** No measurements of opinion on Vietnam were made at the level of considerations, so the intrapsychic dynamics are not directly shown. The next chapter addresses this (p. 211).

### Appendix A: An alternative form of two-message model (pp. 211–213)
Setting: each period, on every issue, citizens face two messages (liberal and conservative), each the sum of all directionally valenced communications (p. 211).
- **Reception axiom.** The probabilities of receiving the liberal and conservative messages are independent increasing functions of awareness (Eq. 9.1b) (p. 211).
- **Acceptance axiom.** The probability of resisting, given reception, increases with value distance from the message and with the likelihood of knowing the elite "contextual information" (Eq. 9.2) (p. 211).
- **Change axiom.** "Supporting" messages are consistent with an existing opinion and "opposing" ones are not. (A) A person who accepts an opposing message and does not accept a supporting one converts. (B) A person who accepts no messages, or accepts both a supporting and an opposing one, decays toward "no opinion" with fixed probability $d$ (pp. 211–212).

Probability of switching to a conservative opinion (for someone liberal or with no opinion):
$$P_{i\to C,t+1}=[RE_{iCt}(1-RE_{iLt})]\text{Accept}_{iCt}+RE_{iCt}RE_{iLt}[\text{Accept}_{iCt}(1-\text{Accept}_{iLt})]\tag{9.9}$$
The first term is receiving only the conservative message and accepting it. The second is receiving both but accepting only the conservative one. $P_{i\to L,t+1}$ is defined similarly (p. 212). Decay to no opinion:
$$P_{i\to\text{Non},t+1}=d\,[(1-RE_{iCt})(1-RE_{iLt})+RE_{iCt}(1-RE_{iLt})(1-\text{Accept}_{iCt})+RE_{iLt}(1-RE_{iCt})(1-\text{Accept}_{iLt})+RE_{iCt}RE_{iLt}\text{Accept}_{iCt}\text{Accept}_{iLt}]=d\,(1-P_{i\to C,t+1}-P_{i\to L,t+1})\tag{9.10}$$
Let $\text{Lib}_{(t)},\text{Con}_{(t)},\text{Non}_{(t)}$ be the initial probabilities of each state. Then
$$\text{Lib}_{(t+1)}=\text{Lib}_{(t)}-[P_{\to C}\text{Lib}_{(t)}]-[P_{\to\text{Non}}\text{Lib}_{(t)}]+[P_{\to L}(\text{Con}_{(t)}+\text{Non}_{(t)})]\tag{9.11}$$
After algebraic manipulation (the author's words), this becomes a difference equation:
$$\text{Lib}_{(t+N)}=\text{Lib}_{(t)}X^N+P_{\to L}\frac{1-X^N}{1-X},\qquad X=1-P_{\to C}-P_{\to L}-d+d(P_{\to C}+P_{\to L})\tag{9.12}$$
(Added step: since $\text{Con}+\text{Non}=1-\text{Lib}$ and $P_{\to\text{Non}}=d(1-P_{\to C}-P_{\to L})$, Eq. 9.11 reduces to $\text{Lib}_{(t+1)}=X\,\text{Lib}_{(t)}+P_{\to L}$. Iterating gives 9.12.) With time as arbitrarily many tiny units, $N\to\infty$ and $X^N\to0$, leaving
$$\text{Lib}_{(t+N)}=P_{\to L}\frac{1-X^N}{1-X}=\frac{P_{\to L}}{P_{\to C}+P_{\to L}+d-d(P_{\to C}+P_{\to L})}\tag{9.13}$$
(The author's displayed steps assume $|X|<1$; this is not stated on the page.)
- Opinion at any time is an equilibrium independent of starting values. It depends on the intensities of the competing flows (aggregate level) and on attention and values (individual level). Opinion change is a difference between equilibria produced by changes in the flows (p. 213).
- Applied to Vietnam (Zaller 1991), it gives results highly similar to this chapter's. It estimates message intensities less well, in that they correspond less well with the story counts (p. 213).

> *Intuition note.* Each period a person is pushed toward the liberal state, the conservative state, or no opinion. With the same pushes every period, the share holding each opinion settles at a fixed value. That value depends on the strengths of the pushes (which reflect message intensities, attention and values), not on where it started.

### Appendix B: Measurement of hawk–dove attitudes (pp. 213–215)
- Franklin's technique estimates relationships between variables not measured in the same dataset (1989). One has $X$ in dataset A but not B, and the outcome $Y$ in B. Regress $X$ on auxiliaries carried in both datasets, build an instrument from the coefficients, and use it in B to predict $Y$. Here $X$ is hawk–dove attitude (1988 NES) and $Y$ is Vietnam opinion (CPS 1964–70) (p. 213).
- Main assumptions: both datasets sample the same population, and the auxiliary–$X$ relationships are the same in both. The second is the worrying one, with datasets 18–24 years apart. The author finds it "not implausible" that females, atheists and civil rights liberals were doves in the 1960s given appropriate cues, and all these variables correlate with Vietnam opinion in expected directions. He concludes the conditions are reasonably met (pp. 213–214).
- **Table 9.2 (first stage, 1988 NES, OLS; p. 214).** The dependent variable is a principal-components scale of five items, with high scores meaning dovish. N = 1441, adjusted $r^2$ = .14. The table lists twelve auxiliary variables:
  - Coefficients (T-ratio): agnostic/atheist 0.40 (4.04); Catholic 0.15 (2.51); fundamentalist −0.18 (2.54); Jehovah's Witness 0.98 (1.05); Jew 0.55 (2.99); pacifistic religion 0.43 (1.53); church attendance 0.08 (3.57).
  - Too slow on civil rights 0.50 (6.01); too fast on civil rights −0.38 (6.75).
  - Border state −0.01 (.16); southern state −0.13 (1.91); union member −0.11 (1.68).
- Age and education are excluded because they have "wrong-way" correlations (pp. 214–215). Age goes with more hawkishness in 1988 but less Vietnam support. The author sees no sign this reflects change over time, since older people were also less supportive in the Persian Gulf crisis. Education goes with less hawkishness but more Vietnam support, especially early. The author attributes this to Mueller's observation that the better educated are more exposed to elite cues, and says the same held in the latest war.

## Toy example (ours, not from the text)
Aim: show how Eq. 9.6–9.8 can make support fall among aware doves and rise among unaware doves. Take $N=1$ message per side. All probabilities below are invented for illustration and are not the author's estimates. Eq. 9.8 uses $AC=RE\cdot\text{Accept}\cdot R$ (9.4).

**Low-awareness dove ($R=0.5$), Accept$_P$ = Accept$_A$ = 0.8 in both years.**
- 1964: $RE_P=0.2$, $RE_A=0.02$. $AC_P=0.2\times0.8\times0.5=0.08$ and $AC_A=0.02\times0.8\times0.5=0.008$. Opinion prob. $=1-(0.92)(0.992)=1-0.91264=0.08736$. Relative prowar $=0.16/(0.16+0.016)=0.909$. Prowar response $=0.08736\times0.909=0.079$.
- 1966: $RE_P=0.6$, $RE_A=0.05$. $AC_P=0.24$, $AC_A=0.02$. Opinion $=1-(0.76)(0.98)=0.2552$. Relative prowar $=0.48/(0.48+0.04)=0.923$. Prowar response $=0.2552\times0.923=0.236$.
- Prowar support rises from about 8% to 24%, because the prowar message newly reaches this group.

**High-awareness dove ($R=0.9$).**
- 1964: $RE_P=0.9$, $RE_A=0.1$, Accept$_P$ = Accept$_A$ = 0.8. $AC_P=0.9\times0.8\times0.9=0.648$ and $AC_A=0.1\times0.8\times0.9=0.072$. Opinion $=1-(0.352)(0.928)=1-0.326656=0.673$. Relative prowar $=0.72/0.80=0.90$. Prowar response $=0.673\times0.90=0.606$.
- 1966: $RE_P=0.95$, $RE_A=0.5$, Accept$_P=0.3$ (elite cues now let this group resist the prowar message), Accept$_A=0.9$. $AC_P=0.95\times0.3\times0.9=0.2565$ and $AC_A=0.5\times0.9\times0.9=0.405$. Opinion $=1-(0.7435)(0.595)=1-0.4424=0.5576$. Relative prowar $=0.285/(0.285+0.45)=0.388$. Prowar response $=0.5576\times0.388=0.216$.
- Prowar support falls from about 61% to 22%.

Note that $R_i$ cancels in the ratio (9.6) but not in the opinionation term (9.7).

## Concepts
- [[receive-accept-sample-model]] — opinion as a response to considerations received, accepted and sampled. Here extended to two competing messages (p. 190)
- [[two-message-model]] (new) — model in which citizens face a prowar and an antiwar flow, with separate reception and acceptance probabilities (Eqs. 9.1–9.8) (p. 189)
- [[countervalent-message]] (new) — a weaker message partly counteracting a dominant one. It can create resistance, or even movement against the trend, in some segments (pp. 185, 207)
- [[message-intensity]] (new) — in the model, the reception-function intercept $a_{0kt}$, varying by message and time; its changes are interpretable (pp. 192, 200)
- [[political-awareness]] — habitual attention to politics. It raises reception and recall, and with distance from the message, resistance once elites supply cues (pp. 192–193)
- [[heuristics-cues]] — elite "contextual information" that lets people judge whether a message fits their values. Awareness and values matter for resistance only after elites divide (pp. 192, 200, 202–203)
- [[mainstream-and-polarization-patterns]] (new) — awareness-related support patterns under elite consensus versus partisan elite split. Their forms depend on relative message intensities (pp. 185, 210)
- [[belief-system-constraint]] — Converse's "what goes with what". The author adds that, in dynamic settings, lags can make older liberals' constraint point toward supporting the war (pp. 209–210)
- [[instrumental-variable-two-sample]] (new) — Franklin's method: build a proxy for a variable measured only in another dataset, using auxiliary variables (pp. 196–197, 213)
- [[non-attitudes]] — here "No opinion" is modelled as having no accessible consideration. The probability falls with message intensity (pp. 194, 205)

## Canonical instances
- [[vietnam-war-opinion-1964-1970]] (new) — four CPS surveys show change in hawk and dove support by awareness as the prowar and antiwar flows shifted (pp. 186–204)
- [[gulf-of-tonkin-resolution-vote]] (new) — 414–0 and 88–2 votes in 1964, used as an indicator of an early prowar elite consensus (p. 188)
- [[iran-contra-and-presidential-approval]] — mentioned as an example of a mostly one-sided flow with some Republican counter-messages (p. 185)

## Bridges (candidates)
- [same-math] Reception, acceptance and recall as logistic functions ↔ statistics: logistic regression for binary outcomes — each stage is a standard logistic of linear predictors.
- [same-math] Franklin's two-sample instrumental variables (Appendix B) ↔ econometrics: constructing a proxy from auxiliaries estimated in a second dataset — the same regress-then-predict construction.
- [structural-analogy] Appendix A's $\text{Lib}_{(t+1)}=X\,\text{Lib}_{(t)}+P_{\to L}$ with an equilibrium independent of starting values ↔ Markov chains: steady state of fixed transition probabilities — similar convergence logic, not stated as a Markov chain in the text.
- [structural-analogy] Relative accessibility as a ratio of reception-times-acceptance ↔ choice models: share of options proportional to "strength" — a ratio of two strengths.

## Questions this raises
- If the number of messages $N$ is arbitrary (any value from about 8 to 60 fits almost equally well, p. 201), how far can the model's substantive claims about intensities be trusted?
- Message intensities are inferred from opinion data alone, and the author calls the match with story counts "a little too good" (p. 201). What independent checks could separate the model's intensities from the media measure it was constrained to?
- Would the findings hold for issues where elite cues change less dramatically? The author calls the Vietnam pattern "probably unusual" (p. 207).
- Do the considerations-level dynamics hold? The author notes that no direct measurements were made at that level, and the next chapter takes this up (p. 211).

## Reading notes
- Printed page = pdf page − 16 (pdf 201 = printed 185). Printed numbers are shown in the page labels.
- The text layer is garbled for several equations. Page images were available only for some pages (e.g. pdf 203, 206, 209, 210, 215, 217, 218, 220–222, 224, 226, 228–230; none for pdf 216 or 219); no image was supplied for the pages carrying Eqs. 9.1a–9.2 (printed pp. 191–192) or Eq. 9.1b (p. 197). Those equations are reconstructed from the garbled text and the surrounding prose. In Eq. 9.1a the text layer reads "1 + / + Exp(...)"; the "/" may be an OCR'd floor term $f$ (p. 197 speaks of 'adding a time subscript to the floor parameter'). This cannot be confirmed without the page image, so 9.1a is given here without it; compare 9.1b.
- Eq. 9.2: subscripts and signs follow the extracted text. The text gives no sign convention for $b_{1t},b_{2t}$, and the sign pattern should be checked against the original.
- Table 9.1's source note reads "1964, 1966, 1978, and 1970 CPS surveys". "1978" is presumably a misprint for 1968, since the text uses 1968.
- p. 202 says all but one reception and recall coefficient are significant in the constrained model. As printed in Table 9.1, the recall intercept (3.47, SE 2.36) does not look significant on its face.
- The Figure 9.6 caption says "logistic regressions"; the text on p. 206 says "simple polynomial regression".
- Figure 9.1a values are read approximately from the figure. The text gives only about four prowar and 1.5 antiwar stories per magazine per year for 1963–64.
- The footnote 15 awareness z-score table has some garbled minus signs and the labels are as printed ("98th percentile"). It is not reproduced here.
- No exercises appear in this unit.
