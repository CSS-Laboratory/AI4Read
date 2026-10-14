---
id: lupia-1998-dilemma/ch09-survey
work: lupia-1998-dilemma
unit: "9 A Survey Experiment on the Conditions for Persuasion"
pages: 184-201
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A Survey Experiment on the Conditions for Persuasion

## L0 — One line
In a phone survey experiment (1,464 respondents), the more a respondent saw a talk-show host as knowledgeable and trustworthy, the more the respondent's opinion matched the host's endorsement, and this beat liking and ideology as a predictor.

## L1 — The gist (≤ 120 words)
The authors ask whether people are selective about whom they believe, as their Chapter 3 theorems predict. Respondents were randomly told that Rush Limbaugh or Phil Donahue supported or opposed more prison spending, or were told nothing. They then rated how often they agree with the speaker and how much he knows. Overall opinions barely moved. But the gap between "supports" and "opposes" groups rose with perceived trust and knowledge, and turned negative for distrusted speakers. Feeling thermometers and ideology predicted worse. The authors reject their null hypothesis and conclude that people choose whom to believe selectively.

**Prerequisites:** randomized experiments and difference in proportions; binomial test; the Chapter 3 "conditions for persuasion" (perceived common interests, perceived knowledge, external forces).

## L2 — Key ideas (5–10 bullets)
- The chapter tests Chapter 3's persuasion theorems against a null hypothesis: perceived trustworthiness and knowledge do not affect persuasion (p. 185).
- Design: random endorsement (Limbaugh/Donahue, supports/opposes, or none) on prison spending, followed by two perception questions, Agrees and Knows (pp. 187–188).
- The authors argue the setting matches the model's premises "good, though not perfect"; noisy respondent goals are said to stack the deck against the theory (pp. 189–190).
- Overall endorsement effects look tiny (Table 9.1), but splitting by Agrees and Knows reveals large, systematic differences (pp. 191–193).
- Negative Supports–Opposes values for distrusted speakers are read as people doing the opposite of the advice, contrary to the cheap-talk claim (p. 194).
- Agrees and Knows have distinct, complementary effects: within each Agrees level, the effect rises with Knows (p. 194).
- Feeling thermometers (likability) and ideology predict persuasion worse than Agrees and Knows, but the authors see likability as complementary, not refuted (pp. 196–201).

## L3 — Walkthrough

### Introduction (pp. 184–186)
- Claim: people are selective about whom to believe. The best predictors of reactions to a speaker are the Chapter 3 conditions for persuasion (p. 184).
- Design in brief: each respondent makes a binary choice so complex that they were unlikely to know which option was better. Most can learn from a speaker whose knowledge and trustworthiness may be unknown to them (p. 184).
- Phone surveys give little control over the setting. The authors ran this one alongside the lab experiments of Chapters 7–8. Rejecting the null in two very different environments suggests robustness (fn. 1, p. 184).
- Persuasion = successful attempt to change another's beliefs. It is necessary, not sufficient, for enlightenment (p. 185).
- Theorems, compact form (p. 185):
  - **3.1:** absent external forces, perceived common interests are necessary for persuasion.
  - **3.2:** absent external forces, perceived speaker knowledge is necessary for persuasion.
  - **3.3:** external forces can substitute for common interests (and for each other).
- **Null hypothesis:** the speaker's ability to persuade is not affected by the respondent's perception of the speaker's trustworthiness or knowledge (p. 185).
- No "reasoned choice" statistics are reported, because reasoned choice for these subjects cannot be known (fn. 2, p. 185).
- The authors say the survey lets them reject the null. If the theory had predicted badly, their later claims on enlightenment and delegation might be flawed (pp. 185–186).

### Description of the experiment (pp. 186–190)
**The survey (p. 186).** This was one of twelve components of the 1992 Multi-Investigator Study on Political Persuasion and Attitude Change (seventeen scholars, thirteen universities). Fieldwork: Berkeley Survey Research Center, CATI telephone interviews, 15 June–4 Nov 1994. Sample: 1,464 randomly selected English-speaking adults in telephone households in the 48 contiguous states (pp. 186–187). Of 2,234 contacted households, 686 refused, 68 were never home and 16 were unable to take part (fn. 3, p. 187).

**Design (pp. 187–188).**
- Question 1 asks whether spending money to build prisons is a good or bad idea. In the endorsement version it first says a talk-show host [SPEAKER] [POSITION] spending money to build more prisons (p. 187).
- Random generators decide:
  - with or without endorsement: about 10% without;
  - speaker: Limbaugh or Donahue;
  - position: "supports" or "opposes".
  - Each of the four endorsements has about a 22.5% chance (p. 188).
- This is a "post-test only" design. Random assignment to only 5 conditions should make initial attitudes comparable. "Very good/bad idea" answers were collapsed. Three respondents were dropped for "don't know" even after a follow-up (fn. 4, p. 187).
- Question 2 (agreement): on most political issues, do you and [SPEAKER] agree all, most, some of the time, or never? Question 3 (knowledge): how much does [SPEAKER] know about what happens if the country builds more prisons — a lot, some, a little, nothing? The order of Q2 and Q3 was randomized. Demographic and partisanship questions followed (p. 188).

**Why these questions (pp. 188–189).**
- Prison spending was chosen because it was salient, ideologically ambiguous (law-and-order vs. interventionist), and uncertain in its consequences. If consequences were transparent, the theory would predict no speaker effect (pp. 188–189).
- The speakers were chosen because they were familiar (only 3 of 1,340 respondents who heard an endorsement did not know the speaker) and unlikely to be universally trusted or reviled. They were talk-show hosts rather than experts so that perceived knowledge would vary (p. 189).
- None of the predictions evaluated depend on which speaker spoke. Only two speakers were used because of survey time and cell sizes (fn. 5, p. 189).

**Match with the theory (pp. 189–190).** The authors assert good but imperfect analogies:
- Respondent = principal and host = speaker. Support or oppose = binary choice. "Supports"/"opposes" = the model's "better"/"worse" (pp. 189–190).
- The principal's goals are unknown, and some respondents may want to end the call quickly. The authors say this stacks the deck against them, so rejecting the null is stronger. Respondents are unlikely to know what "we wanted to hear" (p. 190, fn. 6).
- The conditions for persuasion depend only on the principal's beliefs about speaker goals, not the actual goals. Q2 is a coarse measure of these beliefs and Q3 a coarse measure of perceived knowledge (p. 190).
- The sequence matches the model: beliefs set, speaker speaks, principal chooses, end (p. 190).

### Analysis (pp. 191–195)
**Table 9.1 (p. 191).** Percent saying "good idea": all respondents 59.7 (N = 1,247). Supports 59.8 (639), opposes 59.3 (666), no endorsement 61.4 (122). Limbaugh supports 60.7 (300) and opposes 57.4 (322). Donahue supports 59.0 (339) and opposes 61.0 (344). Democrat 56.1, Republican 64.7, Independent 53.1. Conservative 67.0, liberal 49.0.
- Partisanship and ideology had some effect but were far from deterministic.
- Endorsements seem to do little: Limbaugh supports was only 3.3 points above Limbaugh opposes, and "Donahue supports" was lower than "Donahue opposes" (p. 191).
- The authors say a closer look shows endorsements were used "in systematic and predictable ways" (p. 191).

**Simple hypothesis tests (pp. 192–194).**
- Agrees = coded Q2 answers (trustworthiness). The top two categories are collapsed because fewer than ten said "all the time". Knows = Q3 answers collapsed to binary (p. 192).
- Theorems 3.1–3.3 imply that higher Agrees or Knows should raise the chance that the answer matches the endorsement (p. 192).
- Measure: $\text{Supports–Opposes} = \%\text{good}\mid\text{heard supports} - \%\text{good}\mid\text{heard opposes}$ (added step: this definition is implied by the arithmetic of Table 9.2, e.g. $76-51=25$). It is 0 when equal numbers agree and disagree (p. 192).
- Table 9.2, either source: Agrees all/most 25 (76 vs 51), some 3 (62 vs 59), never −24 (41 vs 65). Knows a lot/some 14 (70 vs 56), little/nothing −20 (44 vs 64) (p. 193).
- Limbaugh: Agrees all/most 22, some 6, never −22; Knows lot/some 15, little/nothing −16. Donahue: 33, 0, −24; Knows 14, −22. The authors say Donahue's effects had the same direction and magnitude as Limbaugh's (pp. 192–193).
- Negative values mean respondents did not necessarily ignore advice from speakers whose trustworthiness or knowledge was suspect. The authors call these "stark counterexamples" to signaling models (Crawford–Sobel; Gilligan–Krehbiel) which, in their reading, say conflicting interests lead to uninformative cheap talk (p. 192). The authors say that if all talk between people with conflicting interests were cheap, we should never see a negative value; but we do (pp. 192, 194).
- Chapter 3's account: those who believe the speaker and audience have interests conflicting with their own should do the opposite of the advice. The negative values fit this (p. 194).
- **Table 9.3** (Agrees × Knows, pp. 194–195): Agrees all/most: Knows lot/some 31 (80 vs 49; N 80/70), little/nothing −80 (0 vs 80; N 4/5). Some: 12 (69 vs 57), −11 (51 vs 62). Never: −13 (56 vs 69), −28 (36 vs 64). At every Agrees level Supports–Opposes rises with Knows, so Agrees and Knows are not mere echoes of each other (p. 194).
- Test: each Table 9.2 entry is treated as an independent binomial $b(N,\%\text{Good})$. For each pair, the null of equal means is tested. Moving from a low to a higher Agrees or Knows category, the null is rejected at 90% or 95% confidence (p. 194).
- The speakers' actual knowledge, interests, incentives, personality and reputation were exogenous constants, so they cannot explain the variance (p. 194).

*Intuition note:* The overall average can hide different reactions. In the authors' reading, those who trust a speaker follow his advice and those who distrust him do the opposite (negative Supports–Opposes). This may help explain why the pooled comparison in Table 9.1 shows so little effect (this link is our gloss, not stated by the authors).

### Comparison with alternative explanations (pp. 194–201)
**Affect (pp. 196–199).** The likability heuristic holds that liked sources are more persuasive (O'Keefe is cited for this). Feeling thermometers measure liking (p. 196).
- Table 9.4 ("supports" subsample) sorts respondents by thermometer (<50, 50, >50) and rows by Agrees or Knows. Likability predicts that support rises left to right. The theory predicts that, whatever the thermometer, support falls as Agrees goes from "all or most" to "never" or Knows from "a lot or some" to "a little or nothing" (pp. 196–197).
- Result: likability is false in every case with ≥10 respondents per cell. The theory is true in all of them. People can be persuaded by people they do not like (pp. 196–197).
- Table 9.5 ("opposes"): predictions reversed. Likability is true in four of nine cases and the theory in "seven of ten" (p. 197). The measures of perceived knowledge and incentives are "far better predictors" (p. 197).
- The authors do not call likability wrong. They see their account as complementary: "feelings" are the principal's beliefs about common interests, plus perceived knowledge and external forces. They call thermometers a "terrible" measure of what makes people follow advice, and say they should not be used to study persuasion (pp. 198–199).

**Ideology (pp. 199–201).** The claim here is that people believe speakers who share their ideology. The authors use the conservative/liberal split. They say this, if anything, overstates ideology's impact, since between-group effects far exceed within-group effects (p. 199, fn. 10).
- Ideology predicts conservatives support prisons more than liberals when Limbaugh endorses and less when Donahue does, with the reverse for "opposes". The theory predicts the same Agrees/Knows pattern as before (p. 199).
- Table 9.6 results: ideology is true in "only three of the twelve" cases. The theory is true in all fifteen (p. 201).
- Conservatives were more likely to support prison spending all else equal. But within conservatives and within liberals, perceived knowledge and trustworthiness were major determinants of whom people believed. So claims that Agrees and Knows are "mere restatements of the effect of ideology" is "plainly false" (p. 201). Partisanship fared much worse than ideology against Agrees and Knows (fn. 11, p. 201).

### Conclusion (p. 201)
Although Agrees and Knows are crude measures, they were strong and consistent predictors of how closely opinions matched speaker statements. The authors read this as "compelling support" that people are selective about whom they believe. Respondents tended to follow speakers seen as both knowledgeable and trustworthy, and to ignore those lacking these qualities (p. 201).

## Toy example (ours, not from the text)
Hypothetical: 200 respondents, 100 hear "supports" and 100 hear "opposes". In each arm, 50 trust the speaker (group A) and 50 distrust him (group B).
- Supports arm: A: 40/50 = 80% say good. B: 15/50 = 30%. Total 55/100 = 55%.
- Opposes arm: A: 25/50 = 50%. B: 28/50 = 56%. Total 53/100 = 53%.
- Pooled Supports–Opposes = 55 − 53 = 2 (looks like "no effect", like Table 9.1).
- A: 80 − 50 = +30. B: 30 − 56 = −26.
- Splitting by trust shows a large positive effect for A and a negative one for B, which the pooled gap hides.

## Concepts
- [[conditions-for-persuasion-lupia-mccubbins]] — absent external forces, perceived common interests and perceived speaker knowledge are each necessary for persuasion; external forces can substitute for common interests (and for each other) (p. 185)
- [[perceived-speaker-trustworthiness-and-knowledge]] (new) — measured by coarse survey items Agrees (Q2) and Knows (Q3) (p. 192)
- [[supports-opposes-measure]] (new) — %good after "supports" minus %good after "opposes"; positive means following, negative means doing the opposite (p. 192)
- [[heuristics-cues]] — here the likability heuristic: liked sources persuade more; tested with feeling thermometers (p. 196)
- [[cheap-talk]] (new) — in signaling models, talk between conflicting-interest parties is uninformative (as the authors read these models); contested by negative effects (p. 192)
- [[post-test-only-design]] (new) — random assignment to few conditions is likely to give roughly comparable initial attitudes, so persuasion can be inferred from a post-test alone (fn. 4, p. 187)

## Canonical instances
- [[limbaugh-donahue-prison-experiment]] — random endorsements by Limbaugh/Donahue on prison spending; effects split by perceived trust and knowledge (pp. 187–195)
- [[multi-investigator-persuasion-study-1994]] — the 12-component national phone survey in which this experiment was embedded (p. 186)

## Bridges (candidates)
- [structural-analogy] Pooled null effect hiding opposite subgroup effects ↔ causal inference: heterogeneous treatment effects across moderators — the average masks positive and negative responses.
- [structural-analogy] Perceived-trust moderation of endorsement ↔ heuristics / cues: party or source cues work only when the source is seen as credible.
- [metaphor] Doing the opposite of a distrusted speaker's advice ↔ identity-protective or motivated reasoning: rejection of uncongenial sources, but here from a rational-choice logic.

## Questions this raises
- Q2 asks about agreement on political issues. Does it capture beliefs about incentives on prisons specifically, or just general affinity (ideological closeness)?
- Do the strong patterns survive controlling for ideology and party jointly, rather than separately? Which variables did Lupia (n.d.) include?
- Does persuasion measured by an answer on the phone (a stated opinion) equal changed beliefs, or may it be shallow?
- The sparse cells (e.g., N = 4, 5) carry large effects: how much do they drive the rejection of the null?

## Reading notes
- Printed page = pdf − 16 (pdf 200 = p. 184); pdf 218 (p. 202) contains only a stray mark ("v.") in the extract.
- The text on p. 192 prints "Supports–Opposes = −100" for perfect matching, then also "−100" for no matches. The first is evidently a misprint; by the definition, perfect matching would give +100 (our inference).
- Table 9.2 first row (either source, Agrees all/most): the image shows 25, which matches 76 − 51 = 25.
- Table 9.1: the "All respondents" N is 1,247. The supports (639) + opposes (666) + no endorsement (122) = 1,427, and these differ from the 1,340 endorsement respondents (p. 189) and the 1,464 sample. The unit does not explain this.
- Counts in prose versus tables: p. 197 says the theory is true in "seven of ten" cases for Table 9.5, but the table shows 7 Yes and 2 No (9 entries). For Table 9.6 the text says ideology is true in "three of the twelve" cases, but I count four "Yes" in the image. The "fifteen" count for the theory matches the table.
- Table 9.3: in the Agrees = never rows, the label reads "a lot or never" in both the text layer and the image (apparently a misprint for "a lot or some"). Tables 9.2, 9.3 and 9.6 text layers are garbled, so numbers were read from the images.
