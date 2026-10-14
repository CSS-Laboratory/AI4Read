---
id: lupia-1998-dilemma/ch07-laboratory-p2
work: lupia-1998-dilemma
unit: "7 Laboratory Experiments on Information, Persuasion, and Choice (part 2/2)"
pages: 112-148
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
# Laboratory Experiments on Information, Persuasion, and Choice (part 2/2)

## L0 — One line
In coin-toss prediction experiments, uninformed subjects followed a speaker when the speaker was believed knowledgeable and to share their interests, or when a penalty, verification or costly effort backed the speaker's message; they chose well when the speaker was in fact informative. In most conditions without these, behaviour was near random.

## L1 — The gist (≤ 120 words)
The authors test their theory of persuasion in a lab. Subjects ("principals") predict a coin toss they cannot see and are paid for correct predictions. One "speaker" sees the toss and sends advice. Benchmarks show choice with full information (97% correct) and with none (48%). Five experiments vary the speaker's knowledge and interests, and add a lying penalty, verification or costly effort. When the speaker was informative and credible, principals followed advice and made reasoned choices (the best option) 83–97% of the time. When principals had no reason to believe the speaker, they acted like random choosers. The authors conclude that limited information prevents reasoned choice when people cannot interact with such a speaker; otherwise it may imply nothing.

**Prerequisites:** binomial probability (fair coin, independent trials); expected value; the chapter's earlier hypotheses (Table 6.1) and the idea of principal and speaker; basic game-theoretic equilibrium.

## L2 — Key ideas (5–10 bullets)
- **Design with many principals.** One speaker faced seven to eleven principals. Payoffs and information were arranged so each principal could be treated as if alone with the speaker (p. 112).
- **Benchmarks define "reasoned choice".** With complete information, 97% of predictions were correct. With none, 48% were, so random behaviour is the baseline for "no persuasion" (p. 113).
- **Persuasion is measured as matches.** Persuasion means the principal's prediction matches the speaker's signal. Strings of matches are compared with what random guessing would produce, a binomial baseline (pp. 114–115).
- **Speaker characteristics.** Without external forces, knowledge and common interests were each needed in these data. Principals ignored an ignorant speaker with common interests and a knowledgeable speaker with conflicting interests. They followed a speaker with both (pp. 118–126).
- **Perception matters.** With a 70% chance of knowledge or of common interests, principals followed the advice. With a 25% chance of common interests, they did not (pp. 122, 132).
- **External forces work.** A $1.00 lying penalty, but not a 10-cent one, induced belief in a conflicting-interest speaker. A 70% verification threat (the true outcome is announced with 70% probability) and costly effort gave similar results (pp. 134–142).
- **Table 7.6 summary.** Here "enlightenment" refers to the conditions under which a speaker's message lets a principal choose correctly (inferred from usage), and "deception" is a prediction that matched the speaker but was wrong. Persuasion plus enlightenment gave about 83% reasoned choice. Persuasion without enlightenment: about 50% of persuasive messages deceived. Without persuasion, behaviour was near 50% (pp. 144–148).
- **Speaker behaviour was less predictable.** Speakers in the costly-effort treatments proposed more often than expected (p. 143).

## L3 — Walkthrough

### Design (continued from the first part of the chapter)
**Many principals per speaker (p. 112).** The theory has one speaker and one principal. The experiments used one speaker and seven to eleven principals. The aim was more data on how people choose whom to believe, at lower cost than one principal per speaker (p. 112). The authors give three safeguards:
- Principals were paid only for their own predictions.
- Principals could not see, hear, or learn of one another's actions.
- All principals faced identical incentives, and the speaker got no feedback on past principal actions. So the speaker had no basis to discriminate among principals.

If the speaker earned $1.00 per correct principal, ten principals gave $10.00. This is the same incentive as one principal with a $10.00 reward (n. 8, p. 112). Principals were called "predictors" and the speaker the "reporter" (n. 7, p. 112).

**Sessions (p. 112).** A session had two experimenters, two to four assistants and eight to twelve subjects. It contained two sets of benchmark trials and one to four experimental conditions.

### Benchmarks (pp. 113–114)
- **Complete information.** The first two trials showed everyone the coin toss. Principals made 376 of 389 correct predictions (97%). The authors read this as strong support for the claim that principals who know consequences choose the highest-valued alternative. Such choices count as reasoned choices (p. 113).
- **Incomplete information.** In later trials (the text says trials three to six) principals did not see the toss and had no speaker. For a fair coin the expected payoffs of heads and tails are equal, so the authors expected random predictions (about 50% correct). They observed 377 of 780 (48%) correct (p. 113).
- When principals were paid a small fee for predicting heads regardless of outcome, they predicted heads 124 of 144 times (86%). This differs significantly from random (n. 10, p. 113).

> **Intuition note.** The benchmarks give two reference points: what good choice looks like (97% correct) and what ignorance looks like (about half correct). Everything later is judged against them.

### Experiments: how the data are used (p. 114–115)
There were five experiments: two on speaker characteristics (knowledge, interest) and three on external forces (penalty for lying, verification, costly effort). Each condition had four to ten trials under identical circumstances. Principals never saw the toss (p. 114).
- Each principal produces a string of predictions per condition.
- The **test statistic** is the number of times the principal's prediction matched the speaker's signal.
- A long string of matches is the strongest evidence of persuasion, because its probability under random behaviour approaches zero as trials increase.
- The null hypothesis is that the principal predicts randomly.
- Each figure has a bar graph of observed principals by number of matches. A line shows the binomial distribution expected if all chose randomly, assuming independent and identically distributed predictions (n. 11, p. 115). For example, with eleven random principals in Fig. 7.1a, about 31% would match two of five times (p. 115).
- Bars stacked to the right indicate persuasion.

### Knowledge experiment (pp. 115–125)
**Hypothesis:** if the principal believes speaker and principal share interests, a higher assessed probability that the speaker is knowledgeable increases persuasion. **Control:** the speaker has common interests but does not see the toss. **Treatment:** the speaker sees the toss (p. 115).

Common interests: both earned an equal amount for each correct principal prediction. Following the speaker was then an undominated strategy. Principals also got 10 cents for predicting heads regardless of outcome. This isolates knowledge: a principal was expected to pick heads in the control regardless of signal, and to follow the speaker in the treatment (pp. 115, 118).

**Control results (pp. 118–119).**
- For a tails signal, following earns $0.5 \times 1 + 0.5 \times 0 = 50$ cents. Ignoring and choosing heads earns $0.5 \times 1 + 0.5 \times 0 + 0.10 = 60$ cents (n. 13, p. 118).
- In the five-trial control (Fig. 7.1a), predictions matched the speaker two of five times for seven principals, three of five for two, once for one, and never for one (p. 118).
- For tails-signal trials (Fig. 7.1b), the text says seven of ten principals always picked heads. It also says seven of eleven never matched. The chance that one random string matches zero of three times is .13 (p. 118).
- Overall in the controls, predictions matched advice 63% (90/143). The speaker reported veraciously about 46% (6/13) and principals chose reasonably about 50% (71/143) (p. 118).
- On tails-signal trials only, matches were 11% (5/44), veracious reports 50% (2/4) and reasoned choices about 57% (25/44) (pp. 118–119).
- To ensure some tails signals, the speaker was covertly offered $5.00 to say tails 60% of the time in the five-trial treatment. This was announced afterwards (n. 15, p. 119).
- The authors say the results suggest principals ignored speakers lacking knowledge despite knowing their common interests (p. 119).

**Treatment results (p. 119).**
- Predictions consistently matched advice, even for tails.
- In Fig. 7.2b, seven of eleven principals predicted tails every time the speaker advised it. One random string matches six of six with probability under 2%. Seven of eleven such strings is nearly zero under randomness.
- Overall, matches were 92% (174/190), veracious reports about 94% (17/18) and reasoned choices about 86% (164/190). The last figure mimics the complete-information benchmark.
- Conclusion: when speaker and principal have common interests, increasing the speaker's knowledge induces persuasion and lets people lacking information choose reasonably (pp. 119–120).

**Variation 1: perceived knowledge (pp. 120–122).** The authors expect perceived, not actual, knowledge to be a necessary condition for persuasion. A ten-sided die (1–7) decided per trial whether the speaker saw the toss. The speaker knew the outcome of the die. Principals knew only a 70% chance of knowledge. The authors expected following if the perceived probability exceeded 50% (p. 122).
- Seven of eleven principals matched the speaker every time. The chance of this for one random string is .001. Matches were 90% (99/110) (p. 122).
- Persuasion was expected in all trials. Reasoned choice was not expected in all of them: it was expected when the speaker really knew, and not as often when he did not (p. 122).
- Speaker had knowledge (trials counted as "fourteen" in the text, but the counts 7/7 and 67/77 imply seven): veracious 100% (7/7), reasoned about 87% (67/77).
- Speaker lacked knowledge (three trials): unknowingly veracious in two of three; matches 97% (32/33), reasoned about 70% (23/33). This figure would have been lower had the speaker unknowingly sent more false reports.
- Together with the original treatment, this supports the expectation that perceived knowledge with common interests induces persuasion and facilitates reasoned choice (p. 122).

**Variation 2: no knowledge and conflicting interests (pp. 122–124).** The speaker did not see the toss and was paid 50 cents per incorrect prediction. Principals were not expected to follow. Matches were 33% (18/55), veracious 60% (3/5) and reasoned 58% (32/55). This resembles the benchmark and the control (p. 124; n. 17).

> **Intuition note.** Principals ignored a speaker who could not know the answer, even though he was friendly. A speaker who knows but is not friendly is also ignored. In these data, knowledge together with common interests moved principals.

### Interest experiment (pp. 124–133)
**Hypothesis:** if the principal believes the speaker is knowledgeable, a higher assessed probability of common interests increases persuasion. **Control:** a knowledgeable speaker with conflicting interests (paid for each incorrect principal prediction). **Treatment:** common interests (p. 124). The 10-cent heads fee was dropped here and in later experiments (n. 18, p. 124).

**Control (pp. 124–126).**
- Fig. 7.5 distributions resemble random behaviour. The modal principal followed about half the time.
- Overall, matches were 59% (452/771), veracious reports about 58% (46/79) and reasoned choices about 54% (413/771). The authors say these results suggest principals ignored knowledgeable speakers lacking common interests (p. 126).
- In variations where the speaker could stay silent, principals were correct four of nine times (44%) when no signal came (n. 19, p. 124).

**Treatment (pp. 126–130).**
- Distributions skew right. In Fig. 7.6a, over half the principals matched every time, whereas the chance for one random string is .03.
- Overall matches were 88% (372/422), veracious reports about 98% (48/49) and reasoned choices about 87% (366/422).
- Conclusion: when the speaker was knowledgeable, greater commonality of interests induced persuasion and reasoned choice (p. 130).
- With no signal, principals were correct 11 of 18 times (61%) (n. 20, p. 130).

**Variation 1: 70% common interests (pp. 130–132).** A ten-sided die set the speaker's payoff direction per trial. Principals knew only the 70% chance of common interests and were expected to follow because this exceeded 50%.
- A majority of principals matched every time. Matches were 87% (183/210).
- Speaker had common interests (14 trials): veracious about 79% (11/14), reasoned about 69% (102/147).
- Speaker had conflicting interests (6 trials): veracious about 33% (2/6), reasoned about 49% (31/63).
- The authors can reject random behaviour (p. 132).

**Variation 2: 25% common interests (pp. 132–133).** An eight-sided die (1 or 2 means common) gave a 25% chance of common interests. The authors expected no persuasion regardless of the speaker's actual interests, because 25% is below 50%.
- Distributions did not differ significantly from random.
- Matches were 56% (63/112), veracious 50% (7/14) and reasoned 46% (51/112), like the incomplete-information benchmark.
- In these trials the speaker could stay silent. In the one silent trial, principals were correct three of eight times (n. 21, p. 133).

### Penalty-for-lying experiments (pp. 133–135)
**Hypothesis:** if the principal believes the speaker is knowledgeable, a larger penalty for lying increases persuasion. The control is the interest-experiment control (59% matches, about 54% reasoned) (p. 133).

In the treatments, interests stayed in conflict (speaker $1.00 per incorrect principal prediction). A false statement cost the speaker a fee paid to the experimenters, whatever the principals then did. With a 10-cent penalty (p. 133):
- False statement and correct prediction: net $-0.10$ (nothing minus 10 cents).
- False statement and incorrect prediction: $1.00 - 0.10 = 0.90$.
- True statement: $1.00$ for an incorrect prediction and nothing for a correct one.

**Results.** The small penalty was expected to be too low to induce persuasion, and the data fit.
- 10-cent penalty: the speaker told the truth about 70% (7/10), but principals matched only 56% (45/80) and chose reasonably about 41% (33/80). Compared with the control, the penalty induced truth-telling, but principals apparently chose not to believe many of the statements (pp. 134–135).
- $1.00 penalty: eleven of seventeen principals matched every time. The speaker was truthful about 80% (16/20), matches were 89% (152/170) and reasoned choices about 74% (126/170) (p. 135).
- Penalties for lying can induce principals lacking information to believe speakers with conflicting interests, and so facilitate reasoned choice (p. 135).
- At 90 or 91 cents, results were a mixture: veracious 74% (28/38), matches 81% (263/324), reasoned two-thirds (218/324) (n. 22, p. 135).

> **Intuition note.** A penalty works through belief. The 10-cent penalty raised truth-telling to about 70%, yet principals apparently mostly did not believe the speaker and matched him only 56% of the time. With the $1.00 penalty, principals followed a speaker they knew had conflicting interests.

### Verification experiments (pp. 135–139)
**Hypothesis:** if the principal believes the speaker is knowledgeable, a higher probability of verification increases persuasion (p. 135). Interests were uncertain to principals (25% common, 75% conflicting, via an eight-sided die). The authors suspected this would produce nontrivial interactions. If principals knew the speaker to be knowledgeable with common interests, the experiment would have been trivial (verification irrelevant). If they knew his interests conflicted, the authors expected them to ignore him, so any reaction to verification would have had nothing to do with principals' assessments of speaker incentives (p. 136).

**Control.** No verification. It is the 25% case (Figs. 7.7b–c): matches 56% (63/112), veracious 50% (7/14), reasoned 46% (51/112) (p. 136).

**Design of the treatment (pp. 136–137).**
- Verification has two effects: it reduces the value of lying, and it gives principals a stronger reason to believe the speaker.
- The speaker chose either to pay $2.00 to make a statement or to stay silent (no cost, no payment, no statement). This gauges the value of communicating.
- A ten-sided die (1–7) decided verification, so the true outcome was announced with probability 70% regardless of the speaker's action.
- The speaker did not know in advance whether verification would occur. Principals heard only "heads" or "tails" and could not tell its source.

**Expectations (p. 137 and n. 23).** Speakers with common interests would be truthful. Speakers with conflicting interests would be silent, and principals would follow any statement. For a speaker with conflicting interests (50 cents per incorrect prediction), the statement fee equals 20 cents per principal if there are ten principals. His expected payoff from speaking is:

$$(.7)(-20\text{ cents}) + (.3)(50\text{ cents} - 20\text{ cents}) = -\$.05,$$

which is less than the $0.00 from silence.

**Results (pp. 137–139).**
- Eleven of nineteen principals matched the announced statement every time. Overall matches were 88% (260/294).
- Verified trials: matches and reasoned choices about 86% (187/217).
- Not verified, common interests: speakers truthful in 6 of 6 trials. Matches and reasoned choices were about 97% (55/57). Speakers with common interests made a statement 100% (9/9) of the time.
- Not verified, conflicting interests, speaker silent: reasoned choices two-thirds (24/36).
- Two unexpected statements from conflicting-interest speakers: one of two was truthful. Matches were 90% (18/20) and reasoned choices 40% (8/20). Speaker behaviour was not as expected, but principal responses were.
- Conclusion: the experiments strongly support the hypothesis that verification makes principals lacking information more likely to choose reasonably (p. 139).
- Variant with always-conflicting interests: the speaker never made an unverified statement. Matches and reasoned choices were 98% (62/63). In two silent unverified trials, 15 of 21 chose reasonably (71%) (n. 24, p. 138).

### Costly effort experiments (pp. 139–144)
**Hypothesis:** if the principal believes the speaker is knowledgeable, more observable costly effort by the speaker increases persuasion (p. 139). In the theory, a costly proposal lets the principal infer the change is worth at least the cost to the speaker, which narrows the possible alternatives (p. 139).

**Design (pp. 139–140).**
- The speaker no longer says "better" or "worse." He may pay a fixed amount to propose a fixed alternative to a known status quo.
- If he does not pay, the trial ends and the status quo fixes payoffs. If he pays, principals choose between the proposal and the status quo.
- Principals knew the status quo value but not the proposal's value, which depended on the coin toss. Example: status quo 40 cents, proposal 10 cents on heads or 60 cents on tails.
- The speaker's payoff was a fixed amount (60 cents) per principal choosing the proposal, and nothing otherwise. A speaker who paid and was rejected lost the fee.
- The authors expected a proposal only if his payoff exceeded the cost and he expected acceptance (p. 140).

**Benchmark.** Principals saw the toss. They chose the higher-paying alternative more than 85% (152/178) of the time (p. 141).

**Control.** Principals did not see the toss, and the speaker did. Only 135 of 371 (36%) choices were reasoned. But 72% (266/371) were consistent with maximizing expected value, because the proposal and status quo typically had unequal expected values. Example: a proposal paying 80 or 40 cents has expected value 60 cents, so with a status quo of 50 cents, choosing the proposal is consistent (p. 141).

**Treatments (pp. 141–142).**
- The speaker paid 20 cents per principal to propose (a 40-cent version was also run). Payoffs made proposing profitable for one coin outcome only.
- Example: 60 cents per principal on heads and 10 cents on tails. Proposing is worthwhile only on heads, so a proposal reveals heads.
- Reasoned choices: 142/165 (86%) at 20 cents and 198/220 (90%) at 40 cents. These figures count only trials where a proposal was expected (n. 26–27, p. 142).
- Principals when the speaker proposed unexpectedly: at 20 cents, 108/121 (89%) chose consistent with expected value and 40/121 (33%) made reasoned choices. At 40 cents, 59/66 (89%) and 34/66 (51.5%) (n. 26–27, p. 142).
- Costly effort apparently gave many principals the knowledge that reasoned choice required.

**Speaker behaviour (pp. 142–144).** The expected speaker behaviour comes from a game-theoretic equilibrium. The authors expected a proposal only if his payoff exceeded the cost and he expected acceptance. Otherwise indifference at best.

| Table | Condition | Expected proposal: proposed / not | Other expectation: proposed / not |
|---|---|---|---|
| 7.3 | Benchmark | 8 / 0 | indifferent: 9 / 3 |
| 7.4 | Control | 11 / 1 | indifferent: 26 / 2 |
| 7.5 | 20 cents | 15 / 5 | expected no proposal: 11 / 9 |
| 7.5 | 40 cents | 20 / 0 | expected no proposal: 6 / 14 |

- Benchmark and control behaviour fit expectations (p. 143).
- In the treatments, speakers proposed in 35 of 40 expected cases. Of 40 cases with no proposal expected, they proposed in 17 (p. 143).
- Post-experimental questionnaires suggested that some speakers had trouble with the mathematics and others were not motivated to maximize earnings (p. 144).

### Conclusion (pp. 144–148)
Table 7.6 summarizes veracious reporting, persuasion, enlightenment, deception and reasoned choice. The costly-effort trials are excluded because their format differs (p. 144). It has five sections:
1. **Complete-information benchmark:** 97% reasoned choice.
2. **Conditions for persuasion and enlightenment satisfied:** subjects who did not see the toss made correct predictions more than 83% of the time. In the verification trials with common interests and no verification, 97%. Many achieved this even though speakers were rewarded for incorrect predictions (p. 144).
3. **Incomplete-information benchmark:** 48%.
4. **Persuasion conditions satisfied, enlightenment conditions not:** the authors expected high persuasion and deception and low reasoned choice.
   - Here a principal is *deceived* when her prediction matched the statement and was incorrect.
   - Persuasion occurred about 90% of the time (104/116), and 50% (52/104) of persuasive communications deceived. In section 2 only 7% (79/1136) did (p. 148).
5. **Persuasion conditions not satisfied:** persuasion and reasoned choice dropped to near 50%, as expected under random choice (p. 148).

The authors' conclusions (p. 148):
- The table shows how much the conditions for persuasion and enlightenment determine who can choose reasonably.
- Subjects lacking a crucial piece of information could use another's statement as a substitute when those conditions held.
- The authors say the results give "impressive support" for their theory of persuasion and show that people facing a complex choice chose systematic adaptations to achieve their objectives.
- In these experiments reasoned choice required neither complete information nor statements from speakers whom principals knew well.
- If people lacking information cannot interact with speakers when the conditions for enlightenment are satisfied, limited information prevents reasoned choice. Otherwise it "may imply nothing" about reasoned choice, and the political consequences are far less dangerous (p. 148).

> **Intuition note.** Persuasion alone is not enough. Principals followed advice about 90% of the time in both section 2 and section 4 of Table 7.6. Whether following led to good choices depended on whether the speaker actually knew and had reason to be truthful. The same behaviour produced 7% deception in one case and 50% in the other.

## Toy example (ours, not from the text)
A principal wins $1 for a correct coin prediction and cannot see the toss. A speaker sees it. Suppose the speaker either has common interests with probability $p$ (then he always reports truthfully) or conflicting interests with probability $1-p$ (then he always reports falsely, and the principal naively takes it at face value). The speaker is knowledgeable in both cases.
- Following the advice pays an expected $p \times 1 + (1-p) \times 0 = p$ dollars.
- Ignoring the advice and guessing randomly pays $0.50.
- Follow if $p > 0.5$. At $p = 0.70$: $0.70 > 0.50$, so follow. At $p = 0.25$: $0.25 < 0.50$, so do not follow.

This mirrors the 70% and 25% interest variations (pp. 130–133).

Chance check: under random guessing, the chance that a principal matches the speaker in all 5 of 5 trials is $(1/2)^5 = 1/32 \approx .031$. With eleven random principals the expected number of all-match principals is $11/32 \approx 0.34$. Seeing seven of eleven with five of five matches would therefore be very surprising under randomness.

## Concepts
- [[conditions-for-persuasion]] — the authors expect more persuasion as a speaker is believed knowledgeable and to share interests (pp. 115, 124), or as external forces (a larger lying penalty, verification, costly effort) are added for a speaker believed knowledgeable (pp. 133–139); perceived, not actual, knowledge and interests are expected to be necessary (pp. 120, 130).
- [[persuasion-operational]] (new) — operationalized as a principal's prediction matching the speaker's signal; evidence is a string of matches that random choice would rarely produce (p. 114).
- [[reasoned-choice]] (new) — choosing the alternative with the highest payoff given the true consequences; benchmarked at 97% in complete information (p. 113).
- [[enlightenment]] (new) — in this unit, the "conditions for enlightenment" are satisfied, for example, when the speaker actually has knowledge and common interests (pp. 122, 132), or when verification occurs regardless of the speaker's interests (p. 137); the term is not defined on these pages (inferred from usage).
- [[deception]] (new) — a prediction that matched the speaker's statement and was incorrect (p. 148).
- [[incomplete-information-benchmark]] (new) — trials with no coin-toss information and no speaker; behaviour is random (about 48% correct) (p. 113).
- [[verification]] (new) — a probability that the true outcome is announced regardless of the speaker's action; it lowers the value of lying and strengthens belief (p. 136).
- [[penalty-for-lying]] (new) — a fee paid by the speaker for a false statement; its effectiveness depends on whether it makes principals believe the speaker will tell the truth (p. 134).
- [[costly-effort-signal]] (new) — a cost paid to propose a change; the principal infers the change is worth at least that cost (p. 139).
- [[principal-agent-problem]] — related idea; the only mention here is the authors' note that the experiments apply to learning from either an agent or a speaker (n. 25, p. 139).

## Canonical instances
- [[coin-toss-prediction-game]] — principals predict an unseen coin toss; the speaker sees it (pp. 112–114).
- [[knowledge-experiment]] — speaker with or without knowledge and common interests (pp. 115–125).
- [[interest-experiment]] — knowledgeable speaker with conflicting or common interests (pp. 124–133).
- [[penalty-for-lying-experiment]] — 10-cent versus $1.00 penalty (pp. 133–135).
- [[verification-experiment]] — 70% verification and $2.00 fee for speaking (pp. 135–139).
- [[costly-effort-experiment]] — speaker pays to propose a change to a known status quo (pp. 139–144).

## Bridges (candidates)
- [structural-analogy] Verification and lying penalties ↔ principal–agent monitoring and sanctions: both make a message credible without trusting the sender's motives.
- [structural-analogy] Costly effort as a signal ↔ signalling models in economics: a costly proposal reveals the sender's private information.
- [metaphor] Reasoned choice via cues from a trusted speaker ↔ heuristics/cues in voting: uninformed people act as if informed by using an informative source.

## Questions this raises
- Do results from a one-speaker, binary coin-toss game hold when speakers are partisan or the issue is complex and multi-dimensional?
- Principals followed advice at 70% perceived common interests. How do real voters form such perceptions, and can the perception be manipulated?
- Why did speakers in the costly-effort treatments propose more than expected (p. 143), and how much does this limit the equilibrium predictions?
- How much do the results depend on payoff size (the authors report $1.00 versus 50 cents showed no impact, n. 12, p. 115)?

## Reading notes
- This part starts mid-chapter at p. 112 (the second design feature, before the "Experiments on Persuasion and Reasoned Choice" heading) and ends with the chapter's Conclusion on p. 148. Printed page = pdf − 16.
- Table 7.6 (pp. 145–147) is printed rotated and its text layer is garbled. I read it from the page images but cite only the figures the authors quote in the text (pp. 144, 148).
- Text inconsistencies: p. 113 says the first five trials are the benchmarks, but the incomplete-information trials are called "third through sixth." In Fig. 7.1b the text says "seven of ten principals" always picked heads and then "seven out of eleven" never matched (p. 118). The text says "fourteen trials" where the speaker had knowledge (p. 122), but 7/7 and 67/77 imply seven trials. The interest variation (p. 132) has 14 and 6 trials with 147 and 63 principal choices, and these counts are consistent.
- OCR errors: footnote 8 begins "Tor example" (misread "For example").
- Statements about the 5-dollar covert payment to speakers appear in notes 15 and 17 (pp. 119, 124).
