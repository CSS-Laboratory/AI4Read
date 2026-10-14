---
id: zaller-1992-massopinion/ch10-information-p1
work: zaller-1992-massopinion
unit: "10 Information flow and electoral choice (part 1/2): House elections"
pages: 216-247
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
# Information flow and electoral choice (part 1/2): resistance to incumbent-dominated House campaigns

## L0 — One line
In 1978 House elections, highly aware outpartisans (voters of the party opposing the incumbent) resist the incumbent's dominant campaign mainly because they alone pick up the faint challenger campaign (countervalent resistance), more than because awareness itself makes them reject incoming messages (awareness-driven partisan resistance played a role, but not a large one).

## L1 — The gist (≤ 120 words)
Zaller asks whether the reception–acceptance model, built for opinion surveys (people must receive, then accept, a message), also explains how voters respond to election campaigns. Using the 1978 NES House study (77 contested incumbent races), he finds that more aware outpartisans (opposite-party voters) resist incumbent-dominated campaigns largely because only they notice the faint challenger campaign (countervalent resistance). Stored partisan considerations (inertia) matter somewhat. Awareness adds little extra partisan resistance when candidate information is first encountered, probably because party cues are widespread in elections. In intense races, less aware voters move toward the incumbent and highly aware outpartisans move away. Competing messages thus produce cross-cutting change.

**Prerequisites:** logistic function and logistic regression; interaction terms; the RAS model of Chapters 7–9 (reception, acceptance, inertial/countervalent/partisan resistance); reading simulated curves.

## L2 — Key ideas
- Election campaigns are another case of partisan elites competing to persuade. The chapter tests whether the same awareness-and-predisposition dynamics (the RAS, or reception–acceptance, model) hold, using 77 House races with strong measures of every RAS variable (p. 216–217).
- Converse explained awareness-induced resistance by stored information. Zaller treats this as inertial resistance and adds countervalent and partisan resistance (p. 218–219).
- A one-message reception × acceptance model is applied to outpartisans' votes for the incumbent, and all its individual-level variables are significant. Awareness keeps a significant resistance effect even with inertia controlled (p. 220–223).
- Seniority raises reception of proincumbent messages among less aware voters. It helps incumbents in low-intensity races and probably hurts in high-intensity ones (p. 224–228, 240).
- Because incumbent and challenger messages differ in intensity, high-intensity races move less aware outpartisans toward the incumbent and highly aware ones away: differential information flow (p. 228).
- Candidate considerations matter more for the vote than party considerations. Highly aware outpartisans resist because they receive challenger likes and incumbent dislikes (p. 231–234).
- Awareness has strong effects on reception but only inconsistent effects on acceptance of candidate information. The author infers that partisan cues are widely available in elections (p. 241–243).
- Simulations show the likes/dislikes counts track campaign intensity, not just talkativeness. Small cognitive effects of seniority may still make a big difference in the voting booth (p. 243–246).

## L3 — Walkthrough

### Chapter introduction (pp. 216–217)
- Campaigns are attempts by competing partisan elites to reach citizens and persuade them. One may therefore suspect that citizens differ in susceptibility according to awareness and predispositions, as in earlier chapters. The chapter tests this suspicion (p. 216).
- Four election types are examined: House, Senate, general presidential, and presidential primary. The aim is not a full account of electoral behaviour. It is to learn how attitudes respond to competing information flows, especially how citizens resist dominant messages in incumbent-dominated races (p. 216).
- The 1978 NES congressional study has identical measures of awareness, ideology and candidate attitudes across 77 contested elections. Vietnam attitudes offered only four surveys, so here there are, in effect, 77. The NES covered 108 districts, but only those where an incumbent sought re-election against an opponent from the other party are used (p. 216–217, fn. 1).
- Vote decisions serve as the "considerations" the model needs. Variation in campaign intensity is readily measured (p. 216).

### Inertial resistance to incumbent-dominated House campaigns (pp. 217–219)
- Background: scholars have tried to explain "vanishing marginals" (districts won by five points or less), often via the incumbent's constituency service and "personal vote" (p. 217).
- **Reception.** Case work reaches people regardless of awareness. Most other incumbent publicity (newsletters, district benefits, endorsements, speeches) likely reaches mainly the chronically attentive. Most House races are low-key, so what aware people see is strongly proincumbent (p. 217–218).
- **Acceptance.** Aware people may better resist a dominant message if predisposed by party or ideology. They hold prior information that dilutes new ideas, are likelier to get countervalent messages (the challenger's), and can better recognise inconsistent messages. Hence a **nonmonotonic** pattern is expected: moderately aware people defect most to the incumbent (p. 218).
- **Converse's view (1962, 1952 election):** highly aware people are heavily exposed but hard to move because of strong prior attitudes. Unaware people are stable because they rarely encounter messages. Moderately aware people are the most volatile (p. 218). Defection probability "varies inversely" with the mass of stored political information (Converse, p. 219).
- Zaller reads "mass of stored information" as "preexisting considerations", which corresponds almost exactly to his inertial resistance. Converse does not mention countervalent or partisan resistance (p. 219).
- Converse found no nonmonotonicity in the 1958 House elections. His explanation was that news was so weak that only avid readers heeded it. Zaller suggests 1978 campaigns may be intense enough to reach moderately attentive voters. This is the difference between cell A (low-intensity message) and cell B (medium-intensity) of Figure 8.2 (p. 219).

*Intuition note.* People who already hold many partisan considerations are hard to move because new items are diluted among old ones. Zaller suggests that 1978 House campaigns may now reach moderately attentive voters, so the most volatile group might be moderately aware people.

### Defection patterns in House elections (pp. 219–228)
**Set-up.** Almost all defections go to the incumbent's party, so only outpartisans' votes for the incumbent are analysed (p. 219–220). These defectors are the voters most responsible for the "personal vote" and show persuasion against predispositions (p. 220). Defection is modelled as reception × acceptance, adapted from Eq. (7.5):

$$\text{Prob(Defection)} = \Big[1-\big(1+\exp[a_0+a_1\text{Awareness}+\dots\text{others}]\big)^{-1}\Big]\times\big(1+\exp[-b_0-b_1\text{Awareness}\dots\text{others}]\big)^{-1}\tag{10.1}$$

(Text layer garbled; bracket placement is my reconstruction, see Reading notes.)

Variables (p. 220):
- Reception function: political awareness; media coverage intensity; incumbent's spending; challenger's spending; years in office; seniority × challenger's spending.
- Acceptance function: awareness; strength of party attachment; inertia; challenger's spending.
- Only awareness is individual-level in reception. The rest are aggregate-level. The logistic form makes them interact with awareness (p. 220).

Measures (p. 221):
- Media coverage: district mean of "how many newspaper articles did you read about the House campaign", purged of district differences in awareness. It ranged from 0.6 to 1.9.
- Seniority proxies interelection communication. Its expected positive effect holds only in lightly contested races. In heavy races service seems to hurt, hence the interaction term. This is an ad hoc fix because Eq. 10.1 is essentially a one-message model; a two-message model as in Chapter 9 would be needed (p. 221, fn. 4).
- Inertia comes from NES party likes/dislikes (up to five responses each):
$$\text{Inertia}=+\textstyle\sum(\text{Outparty likes})+\sum(\text{Incumbent party dislikes})-\sum(\text{Outparty dislikes})-\sum(\text{Incumbent party likes})$$
- Higher inertia means more difficulty deflecting an outpartisan's vote (p. 221–222). This is the first direct test of inertial resistance (p. 221).

**Estimates (Table 10.1, N = 277, maximum likelihood; standard errors in brackets; p. 222).**

| Reception | coef. (SE) | Acceptance | coef. (SE) |
|---|---|---|---|
| Intercept | −1.71 | Intercept | 3.39 |
| Awareness (std.) | 2.24 (1.20) | Awareness | −1.01 (.41) |
| Incumbent spending ($10,000s) | −0.11 (.09) | Party strength | −1.32 (.48) |
| Challenger spending | 0.28 (.18) | Partisan inertia (high = challenger's party) | −0.22 (.12) |
| Media coverage | 3.51 (2.72) | Challenger spending | −0.05 (.02) |
| Seniority (logged) | 2.84 (2.13) | | |
| Seniority × challenger spending | −0.41 (.26) | | |

Findings (pp. 223–224):
- All individual-level variables are significant, supporting the RAS model's applicability.
- The negative awareness coefficient in acceptance is noteworthy. With preexisting considerations controlled, awareness might have been expected to have little direct effect. It remains, which the author will trace to partisan and especially countervalent resistance.
- Inertia is significant but only moderately large. A net score of 6 (very high) equals the effect of party strength, since $6\times0.22=1.32$. Dropping inertia raises residual variation by 2 percent, dropping party strength by 4 percent.
- Only one aggregate coefficient is individually significant, but the block F-test on all six is significant (F[6,265] = 2.62, p < .05). The author does not interpret individual spending coefficients because of probable endogeneity (fn. 6).
- Seniority has a positive main effect and negative interaction with challenger spending. The joint F-test on the two terms is close to significance (F[2,265] = 2.96, p < .06). Zaller accepts the cross-cutting effects "as probably real" (p. 223–224).
- The negative sign on awareness in acceptance differs from his 1989 paper because the acceptance function changed form (fn. 5).

**Figure 10.1 (p. 224–226).** It decomposes persuasion into reception, acceptance and defection for three constructed outpartisans: strong partisan (inertia +3), disaffected partisan (−3), and modal outpartisan (inertia +0.7, party strength 1.30). The low-intensity race has an incumbent spending $25,000, no challenger spending report, and media coverage 0.75. About 10 percent of contested House races are of this type (p. 224).
- Worked case: a strong partisan at the 50th percentile of awareness, low-seniority incumbent (two years): reception .72, acceptance .56, so defection $=.72\times.56=.40$. With a ten-year (five-term) incumbent, reception rises to .97, so defection $=.97\times.56=.54$ (p. 224).
- A voter of moderately low awareness has roughly a 25 percent chance of receiving a proincumbent message under a one-term incumbent and roughly 65 percent under a five-term incumbent. The most aware are already saturated after the first term, so seniority adds no comparable defection among them (p. 224–226).
- Acceptance falls with both awareness and partisanship. Without this independent awareness effect there would be no nonmonotonicity once partisanship and inertia are controlled. Partisanship matters mainly at middle and high awareness, so awareness and partisanship interact (p. 226).
- The patterns resemble Figure 8.2, top half: a two-year incumbent acts like cell B (moderate intensity), a ten-year one like cell C (high intensity). Because the figure covers only voters, the whole-population pattern would roughly resemble cell B in both cases. So a typical incumbent campaign is a "moderately intense message on an unfamiliar topic" (p. 226).
- The seniority effect in high-intensity races is not graphed (too few cases), but its direction is clear: high seniority plus high intensity reduces defections (p. 226–227).

**Figure 10.2 (pp. 227–228).** The baseline is a modal outpartisan facing a two-year incumbent in a low-intensity race. The left panel shows ten years' seniority. The right panel shows a high-intensity campaign: incumbent $200,000, challenger $150,000, coverage 1.25, about the 90th percentile of intensity.
- High intensity gives above-baseline defection among less aware voters and below-baseline defection among the most aware.
- A one-message model expects all change toward the dominant message. This pattern needs two messages. The incumbent's intense campaign reaches less aware voters. The challenger's weaker one does not. It does reach the attentive, who as outpartisans are more likely to accept it (p. 228).
- Seniority, a mainly one-sided message, produces only one-directional change in low-intensity races (p. 228).
- This is another case of **differential information flow**, as in the early Vietnam War (p. 228).

*Intuition note.* An intense incumbent campaign reaches people who are normally out of reach. A modest challenger campaign reaches only the attentive. So the same race pushes unaware outpartisans toward the incumbent and aware ones away.

### Countervalent and partisan resistance to incumbent-dominated campaigns (pp. 228–243)
**Data and measures (pp. 229–230).**
- This section uses all respondents in contested-incumbent districts. It analyses candidate likes/dislikes (up to four remarks per probe) as the considerations received and accepted (p. 229).
- Challenger information mostly arrives during the campaign. Incumbent information mixes interelection and campaign effects. Cross-district differences in remarks are read as campaign effects (p. 229).
- Zaller concedes the data are not a complete map of considerations. He argues the data are well suited because remarks vary strongly by campaign context, from about 2.5 per respondent in heavy races to under 0.5 in low-intensity ones (simulated), and loquacity can be controlled (p. 229–230).

**Table 10.2 (p. 230).** Mean summed likes/dislikes by awareness (five groups, low to high):
- Two House candidates (1978): 0.50, 0.86, 1.13, 1.50, 2.06.
- Two parties (1978): 0.67, 1.01, 1.61, 2.41, 4.06.
- 1984 presidential candidates: 2.35, 4.11, 6.26, 6.62, 7.81.
- Voters have many more party than House-candidate considerations. This raises the question of which matter more for the vote (p. 230).

**Table 10.3 (p. 231).** Logistic regression of outpartisans' vote for the incumbent, N = 277. The text layer prints N = 111; the image shows 277.
- Net candidate likes/dislikes: −1.14 (.19). Net party likes/dislikes: −0.29 (.11). "Strongly" identified: 1.11 (.41). Issues scale: 0.06 (.06). Intercept −.36.
- Net candidate consideration is scored toward the incumbent (Eq. 10.2):
$$\text{Net candidate consideration}=+\textstyle\sum(\text{Incumbent likes})+\sum(\text{Challenger dislikes})-\sum(\text{Incumbent dislikes})-\sum(\text{Challenger likes})\tag{10.2}$$
- One extra candidate like or dislike has the same effect as strong identification with the outparty and about four times that of a party like or dislike. Issue distance from the incumbent has virtually no direct effect (p. 231).
- Inertial considerations still help prevent defection, especially among the highly aware. But "the main action" is in candidate considerations (p. 232).

**Figures 10.3 and 10.4 (pp. 232–234).** Races are split at $40,000 into low- and higher-intensity.
- Inpartisans: net considerations rise steadily with awareness, with no nonmonotonicity. Highly aware inpartisans have no reason to resist (p. 232).
- Outpartisans: a strong nonmonotonic relation. The highly aware outpartisans' curve sits lower in higher-intensity races, matching their lower defection (p. 233).
- Disaggregated (Figure 10.4): little sign of nonmonotonicity. Higher awareness means more remarks about both candidates, even against partisan grain. The puzzle is how this fits with nonmonotonic defection (p. 233).
- Answer: incumbent likes overwhelm other types. Among outpartisans, incumbent likes are four times as numerous as challenger likes. Many challengers are almost invisible, but visible to the highly aware (p. 234).
- Incumbent dislikes also rise sharply with awareness, especially among outpartisans. Highly aware outpartisans are the only group for which proincumbent considerations do not overwhelm others (p. 234).
- This is **countervalent resistance** shown directly at the level of considerations. It parallels sophisticated liberals' resistance to the prowar message in the early Vietnam War (p. 234).

*Intuition note.* Highly aware outpartisans do not simply reject the incumbent. They hear the weak challenger signal that others miss, and they are predisposed to accept it.

**Partisan resistance (pp. 234–243).**
- Partisan resistance is visible in Figure 10.3, where inpartisans hold more proincumbent considerations. Whether awareness enhances it needs a stricter test (p. 234–235).
- Each of the four candidate consideration counts gets its own reception-acceptance model of the form of Eq. 10.1:
$$\text{Net candidate considerations}_{ij}=\textstyle\sum_n f(\text{Like/Dislike})_n=\sum_n\big((\text{Recept}_{ij})(\text{Accept}_{ij}\mid\text{Recept}_{ij})\big)_n\tag{10.3}$$
- Here $i$ indexes individuals, $j$ districts, $n$ the four measures. Both functions are logistic. The expectation: campaign intensity and attentiveness drive reception, while habitual awareness has little effect on acceptance (p. 235).
- Reception measures: awareness; campaign interest; voted in 1978. The last two are added because the 1978 survey had few knowledge items. Both are purged of correlation with district media coverage so they measure habitual, not campaign-stimulated, awareness (p. 235–236).
- District-level reception variables: incumbent and challenger spending, media coverage, years served. The spending variables are entangled with challenger quality, previous margin and coverage. The author cannot disentangle them, so he draws no conclusions from single coefficients and uses simulations (p. 236).
- Acceptance variables (p. 236–238):
  - party identification, five points, scored toward the challenger's party. A strong coefficient would indicate partisan bias;
  - policy distance from the incumbent (individual's issue position vs. ADA/ACA roll-call ratings; fn. 8) and, for challengers, a left-right issue scale;
  - inertia. The RAS model expects preexisting considerations only to dilute new ones, not to affect their acquisition;
  - awareness. Any remaining effect after inertia and countervalent reception are controlled can be attributed to enhanced partisan resistance via cueing messages;
  - loquacity (total party likes/dislikes) as a nuisance control.

**Table 10.4 (p. 239; NLS, N = 1545), selected coefficients (inc. likes / inc. dislikes / chall. likes / chall. dislikes).**
- Reception awareness: 0.58 / 1.11 / 0.71 / 0.71 (SEs .08 / .29 / .18 / .34).
- Reception seniority: 0.42 (.16) / 2.02 (.51) for incumbent remarks.
- Reception intercepts: −4.43 / −8.92 / −7.90 / −8.21.
- Acceptance awareness: −1.43 (.32) / −0.25 (.30) / −0.89 (.39) / −0.04 (.55).
- Party attachment: −0.45 / 0.20 / 0.19 / −0.14.
- Inertia: −0.00 / 0.07 / 0.27 / 0.20.
- Issue distance from incumbent: −0.47 / 0.52.
- Challenger issue scale: 0.13 / −0.47.

Findings (pp. 240–243):
- **Seniority** is significant in both incumbent-likes and incumbent-dislikes models, so its effects are cross-cutting. They are not mutually cancelling. The dislikes intercept is low, so seniority matters there only when other reception variables are high (high-intensity races). The likes intercept is the highest of the four, so positive effects act even in low-intensity races. Net: positive in low-intensity races, negative in high-spending ones, confirming Table 10.1 (p. 240).
- The Kennedy illustration (Senator Kennedy "may exemplify" such a politician): in a low-intensity race his glamour and family background are selling points, while in a high-intensity race a skilled challenger might find ammunition in his long liberal record, so the negative effects might become important only against a potent challenge (p. 240).
- Zaller says this analysis is more solidly founded than the earlier one (highly significant coefficients; all respondents, not only outpartisan voters) and more informative, since it shows why seniority cross-cuts (p. 240, fn. 11).
- Three attentiveness measures are correctly signed in all models and significant in 10 of 12 trials. Attentiveness is a major determinant of acquisition (p. 240–241).
- **Inertia** performs weakly in acceptance (coefficients from moderately large expected-direction to moderately large unexpected-direction). Inertia counters fresh information at the vote decision but has no consistent effect on accepting new candidate information (p. 241).
- **Party attachment and issue distance** have correct signs in all equations and are significant in five of eight cases, a partisan bias in processing candidate information (p. 241).
- **Awareness** is mixed. It appears to promote partisan resistance to positive information (incumbent and challenger likes) but not to negative information. Parallel checks on Senate and 1984 presidential likes/dislikes found no important association (p. 241).
- So awareness has relatively little effect on partisan resistance at the level of incoming candidate information. Yet awareness is strongly associated with resistance at the vote level, because partisan resistance is only one of three awareness-mediated mechanisms. Inertial and especially countervalent resistance have large effects (p. 241–242).
- **Author's inference** (not demonstrable from these data): partisan discrimination is present (Table 10.4), but the least aware show nearly as much as the most aware. If the RAS model is right, cueing information must be so widely available in election campaigns that even the least aware acquire it. News and advertising routinely identify candidates' party. The author's impression is that issue news rarely carries clear partisan cues (p. 242).
- Conclusion: attentiveness works on candidate information mainly via reception (p. 242–243).

### Simulating the effects of campaign intensity (pp. 243–246)
- **Methodological check.** The modal outpartisan is expected to make 0.27 remarks in a low-intensity race (two-year incumbent) and 2.51 in a high-intensity one (ten-year incumbent). A no-campaign race gives 0.20. So remark counts do not mainly reflect willingness to talk (p. 243).
- **Figure 10.5.** Seniority (two to ten years) slightly raises net proincumbent considerations, mainly among middle- and low-aware outpartisans. High campaign intensity raises support among less aware outpartisans and lowers it among highly aware ones. Both match Figure 10.2 (p. 243–244; fn. 14 gives the simulation settings).
- The seniority effect on considerations looks small relative to its effect on defections. Zaller cites Mann and Wolfinger (1980): the personal vote has not come with better recall of incumbents' names, and incumbency advantage may need only name recognition at the ballot box (p. 244–245).
- Conclusion: the small seniority effect is probably accurate, but not so small that it cannot matter in the booth against an almost invisible challenger. The seniority effect is small only in the sense of net considerations; the separate positive and negative coefficients are not small (p. 245, fn. 15).
- **Table 10.5 (p. 246).** Simulated mean considerations for modal outpartisans:

| | High-aware pro-inc | High-aware pro-chal | Low-aware pro-inc | Low-aware pro-chal |
|---|---|---|---|---|
| Low intensity | 0.24 | 0.07 | 0.16 | 0.01 |
| High intensity | 1.09 | 1.43 | 0.92 | 0.26 |
| Gain | +0.85 | +1.36 | +0.76 | +0.25 |

- Net to incumbent: printed −0.41 (high-aware) and +0.51 (low-aware). Highly aware outpartisans are heavily exposed to both campaigns but accept mainly countervalent considerations. Low-aware outpartisans receive mostly dominant-campaign information (p. 246).
- This parallels Vietnam 1964–66, where less aware liberals became more supportive of the war and more aware liberals less. Here the two-sided flow is seen both in votes and in considerations (p. 246).

### Summary on House elections (pp. 246–247)
- **Inertial resistance:** Converse's mechanism is supported. Aware people hold more preexisting partisan considerations (Table 10.2), and these go with resistance (Tables 10.1, 10.3; Figure 10.1) (p. 247).
- **Partisan resistance:** awareness remains associated with resistance after inertia is controlled. One reason is partisan resistance at the point of encountering messages (Table 10.4). Its effects were neither large nor consistent (p. 247).
- **Countervalent resistance:** highly aware persons, but not most others, receive substantial challenger information, so highly aware outpartisans develop reasons to oppose the incumbent (Figure 10.4). What drives this is not resistance per se but the ability to pick up low-intensity communications. It appears to be the most important source of resistance (p. 247).
- **Objection (an imagined critic):** this is not resistance but susceptibility to another persuader. **Zaller replies:** the objection may perhaps be reasonable when the countervalent message is nearly as intense as the dominant one. But countervalent resistance means being exposed to two streams and choosing the one congenial to one's values, not simply the louder one. Such autonomous choice justifies saying one message was chosen and the other resisted (p. 247).

## Toy example (ours, not from the text)
Treat each message's reception probability as the expected number of considerations it yields. Assume outpartisans accept incumbent messages with probability 0.3 and challenger messages with probability 0.8, the same at every awareness level (as the book finds, awareness has little effect on acceptance).

Weak campaign: reception probabilities (incumbent, challenger): low-aware (0.2, 0.0); high-aware (0.7, 0.1).
Strong campaign: low-aware (0.8, 0.1); high-aware (0.95, 0.7).

Net proincumbent considerations = pro-incumbent − pro-challenger.
- Low-aware, weak: $0.2\times0.3=0.06$; $0.0\times0.8=0$; net $+0.06$. Strong: $0.8\times0.3=0.24$; $0.1\times0.8=0.08$; net $+0.16$. Change $+0.10$.
- High-aware, weak: $0.7\times0.3=0.21$; $0.1\times0.8=0.08$; net $+0.13$. Strong: $0.95\times0.3=0.285$; $0.7\times0.8=0.56$; net $-0.275$. Change $-0.405$.

The stronger campaign moves low-aware voters toward the incumbent and high-aware outpartisans away, with acceptance unchanged. Differential reception alone produces the cross-cutting pattern.

## Concepts
- [[RAS model]] — reception–acceptance model; here applied to vote choice as reception × acceptance (Eq. 10.1) (p. 220)
- [[political awareness / sophistication]] — habitual, chronic attention to politics; in this chapter it strongly raises reception but only inconsistently affects acceptance of candidate information (p. 235–236, 242–243)
- [[inertial-resistance]] (new) — preexisting considerations dilute new messages; measured by net party likes/dislikes ("inertia") (p. 219–221)
- [[countervalent-resistance]] (new) — resisting a dominant message by receiving and accepting a competing message; appears to be the most important source of resistance in House races (p. 234, 247)
- [[partisan-resistance]] (new) — accepting congenial and rejecting uncongenial messages, measured by party ID and issue distance (p. 234, 241)
- [[differential-information-flow]] (new) — two messages of unequal intensity have opposite effects at different awareness levels (p. 228)
- [[nonmonotonic-persuasion]] (new) — relation expected (and found by Converse for 1952) in which moderately aware people are the most influenced (p. 218)
- [[incumbent-personal-vote]] (new) — defection of outpartisans to the incumbent; seniority serves as its proxy (p. 217, 221)
- [[heuristics / cues]] — partisan cueing information; inferred (not directly shown) to be widely available in election campaigns (p. 242)
- [[likes-dislikes-considerations]] (new) — NES open-ended likes/dislikes counted as received-and-accepted considerations (p. 229–230)

## Canonical instances
- [[house-elections-1978]] — NES study of 77 contested incumbent races, used to test the RAS model (p. 216–217)
- [[converse-1962-information-flow]] — Converse's nonmonotonic stability explanation, reread as inertial resistance (p. 218–219)
- [[vietnam-differential-flow]] — compared with House results as a parallel two-sided flow (p. 228, 246)
- [[mann-wolfinger-name-recognition]] — personal vote may rest on name recognition, not recall (p. 244–245)

## Bridges (candidates)
- [structural-analogy] Countervalent resistance ↔ political science: Lupia–McCubbins conditions for persuasion — whose message is believed and accepted shapes who is persuaded.
- [structural-analogy] Differential reception under an intensity threshold ↔ revolutionary threshold/cascade — different people cross a "reached by the message" threshold at different intensities.
- [metaphor] Seniority as slowly accumulated name recognition ↔ path dependence — early investments build a lasting advantage.

## Questions this raises
- Would a genuine two-message model (separate reception and acceptance functions per message), as footnote 4 requests, reproduce the seniority × challenger-spending interaction without an ad hoc term?
- Does the claim that cues are widely available hold for Senate and presidential races? Only brief checks are reported here.
- How far do results depend on likes/dislikes as a measure of considerations, and on endogenous spending variables?
- What happens in open-seat or non-incumbent races? (Part 2 may address Senate, presidential and primary elections; not covered here.)

## Reading notes
- **Part boundaries:** this part starts at the chapter opening (printed p. 216) and ends at the end of "Summary on House elections" (p. 247). The remaining chapter sections are not covered. Per the source note, the split falls at a section boundary.
- **Offset:** printed = pdf − 16.
- **Garbled equations:** Eq. 10.1 and Eq. 10.3 and the Inertia formula (p. 220–221, 235) have garbled text layers, and no page images were supplied for pdf 236, 237 or 251 (printed 220, 221, 235). I reconstructed the factors from the structure described on pp. 220 and 224 and from Table 10.1 signs. Verify against the printed page.
- **Table 10.3 (p. 231):** the text layer gives N = 111, but the image shows N = 277. The signs of the candidate-information and strong-identification coefficients are as printed; this part does not explain the sign convention of the dependent variable.
- **Table 10.5 (p. 246):** printed high-awareness net is −0.41, but the gains printed give $+0.85-1.36=-0.51$. Low-awareness net $+0.51$ matches. Possible misprint, as shown on the image.
- **Figure 10.1 (p. 225)** is rotated. I read curves only qualitatively, plus the numbers labelled on them (.72, .56, .40, .97, .54).
- **Terminology:** the text uses "ten-year" and "five-term" incumbents interchangeably, and "two-year" and "one-term".
