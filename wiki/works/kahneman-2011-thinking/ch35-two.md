---
id: kahneman-2011-thinking/ch35-two
work: kahneman-2011-thinking
unit: "35 Two Selves"
pages: "pdf 368–376 (printed page numbers unknown)"
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Two Selves

## L0 — One line
Our memory of a painful episode tends to follow the peak and the end and to neglect duration, so choices guided by memory can conflict with what was actually experienced.

## L1 — The gist (≤ 120 words)
Kahneman separates experienced utility (pain and pleasure as lived) from decision utility (what people want, as economics uses the word). The idea of rational agents assumes the two coincide. In a colonoscopy study, patients' retrospective ratings followed the peak-end rule (worst and final moments) and neglected duration. In a cold-hand experiment, 80% of participants whose pain diminished at the end chose to repeat the longer episode; Kahneman explains this by their having the less aversive memory of it. Kahneman describes this as a conflict between an experiencing self and a remembering self, with the remembering self making the decisions. This is a challenge to the rational-agent assumption that people have consistent preferences and know how to maximize them.

**Prerequisites:** the idea of utility as a number for how good something is; System 1 as fast intuitive thinking; area under a curve as a total over time.

## L2 — Key ideas (5–10 bullets)
- "Utility" has two meanings: experienced utility (pain and pleasure, Bentham) and decision utility ("wantability", economics). Rationality assumes they coincide (pdf 368).
- Injections puzzle: paying more to cut 6→4 injections than 20→18 is absurd if each injection hurts equally. At least in some cases, experienced utility is the criterion for judging a decision wrong (pdf 368–369).
- Edgeworth's "hedonimeter" idea: total experienced utility is the area under the moment-by-moment curve, so duration matters (pdf 369–370).
- Retrospective ratings of the colonoscopy followed the peak-end rule and ignored duration, so they differ systematically from hedonimeter totals (pdf 370–371).
- Cold-hand experiment: 80% of those whose pain diminished in the last phase chose to repeat the longer episode, which was worse from the experiencing self's perspective (pdf 373).
- Cause: System 1 stores a set of moments as a prototype (average or norm), not a sum. The same feature explains less-is-more effects, and rats also show duration neglect (pdf 374).
- The remembering self "keeps score" and decides. Preferences can fail to serve our interests, which challenges the rational-agent model (pdf 372, 375).

## L3 — Walkthrough

### Two meanings of utility (pdf 368)
- Bentham: pain and pleasure are the two "sovereign masters" of mankind. Kahneman calls this **experienced utility**.
- For about 100 years economists have used "utility" to mean "wantability", which Kahneman calls **decision utility**. Expected utility theory is "entirely about" the rules of rationality for decision utilities. It says nothing about hedonic experience.
- The two coincide if people want what they will enjoy and enjoy what they chose. This is implicit in the idea of the rational agent, who knows present and future tastes and decides well.

### Experienced Utility: the injections puzzle (pdf 368–369)
- Setup: one painful injection per day, with no adaptation. Would people value cutting 20→18 injections the same as 6→4?
- Kahneman did not collect data because the outcome was evident. People pay more to cut a third (6→4) than a tenth (20→18). This is absurd, since the pain per injection is constant.
- Implications: experienced utility can be measured by counting injections. At least in some cases it is the criterion for judging a decision. Paying different amounts for the same gain in experienced utility is a mistake.
- In decision theory, the only basis for calling a decision wrong is inconsistency with other preferences. Here experienced utility is proposed as a criterion, at least in some cases, beyond consistency.

### Experience and Memory (pdf 369–372)
- **Edgeworth's hedonimeter:** an imagined instrument recording pleasure or pain at each moment. The total for an episode is the "area under the curve". Doubling the time at the same intensity doubles total utility (pdf 369).
- **Colonoscopy study** (Redelmeier and Kahneman; run in the early 1990s):
  - 154 patients rated pain every 60 seconds on a 0–10 scale. Procedures lasted from 4 to 69 minutes (pdf 369–370).
  - Patient A's procedure lasted 8 minutes and patient B's 24 minutes. B spent at least as long as A at every pain level, so B clearly suffered more by area. Measures from momentary reports are called **hedonimeter totals** (pdf 370).
  - Afterwards, patients rated the total amount of pain they had experienced. Two findings (pdf 370):
    - **Peak-end rule:** the global rating was well predicted by the average of the worst-moment pain and the pain at the end.
    - **Duration neglect:** duration had no effect "whatsoever" on the ratings.
  - Application (pdf 371): both patients had a peak of 8. The last rating was 7 for A and 1 for B. The peak-end averages are
    $$\tfrac{8+7}{2}=7.5 \ (A), \qquad \tfrac{8+1}{2}=4.5 \ (B).$$
    So A remembered the episode as much worse, although B suffered more by area.
- Hedonimeter totals are duration-weighted: all moments get equal weight. Retrospective ratings ignore duration and weight the peak and the end heavily (pdf 371).
- **Practical implications** (pdf 371):
  - If the aim is to reduce the memory of pain, lowering the peak intensity could be more important than minimizing duration, and gradual relief may be preferable to abrupt relief if the pain at the end is relatively mild.
  - If the aim is to reduce pain actually experienced, a swift procedure may be better, even with a higher peak and an awful memory.
  - Kahneman's impression (not a survey) is that a strong majority favour reducing the memory of pain.
- **Two selves** (not the same as the two systems): the experiencing self answers "Does it hurt now?" and the remembering self answers "How was it, on the whole?" (pdf 371). Memories are all we keep, so we think about our lives from the remembering self's perspective (pdf 371).
- **Symphony anecdote** (pdf 372): a listener said a scratch at the end "ruined the whole experience". Kahneman says only the memory was ruined. The experience was almost entirely good, and the grade ignored 40 minutes of bliss.
- Confusing experience with memory is a "compelling cognitive illusion". The experiencing self has no voice. The remembering self is sometimes wrong, but it keeps score and makes decisions. Kahneman calls this the "tyranny of the remembering self" (pdf 372).

*Intuition note:* Memory does not add up moments. It keeps a snapshot strongly influenced by the worst point and the final point. So an episode that ends mildly can feel better afterwards even if it contained more total pain.

### Which Self Should Count? The cold-hand experiment (pdf 372–374)
- **Method** (pdf 372–373):
  - Participants held a hand in painfully cold water, with tolerable pain, and recorded pain continuously with the free hand. Nobody withdrew.
  - Short episode: 60 s at 14 °C, then the hand is removed and a warm towel is offered.
  - Long episode: the same 60 s, then 30 s more while the water warmed by about 1°, enough for most to notice slightly less pain.
  - Each person did both, one per hand. Order and hand were counterbalanced. Trials were 7 minutes apart.
  - Seven minutes after the second trial, they chose which experience to repeat in a "third trial".
- **Prediction:** the experiencing self finds the long trial worse. Peak-end plus duration neglect predicts a better memory of the long one (pdf 373).
- **Result:** 80% of those who reported that pain diminished in the final phase chose to repeat the long episode. They accepted 30 seconds of needless pain (pdf 373).
- **Interpretation:**
  - They were not masochists. Kahneman says that if they had been asked whether they preferred the 90-second immersion or only its first part, they would certainly have chosen the short one. They knew which was longer but did not use that knowledge.
  - Their decision rule was intuitive: pick the option you like most or dislike least. Memory determined the dislike (pdf 373–374).
  - This is a discrepancy between decision utility and experienced utility, like the injections puzzle (pdf 374).
- **Less-is-more link:** the same System 1 feature appears in Hsee's dishes and in Linda. System 1 represents sets by averages, norms and prototypes, not by sums. Each episode is stored as a prototypical moment. The observer's area under the curve is a sum (pdf 374).
- **Evolution:** memory could store integrals, as with a squirrel's food store, but the integral of pain or pleasure may be less biologically significant. Rats show duration neglect. In a shock experiment, fear depended on intensity, and shock duration had little or no effect. For pleasurable brain stimulation, only intensity appears to matter: up to a point, longer bursts did not seem to raise the animal's eagerness. The rules of the remembering self have a long evolutionary history (pdf 374).

*Intuition note:* The subjects knew which episode was longer but did not use that knowledge. They chose the one they disliked least, and the rules of memory set how much they disliked each.

### Biology vs. Rationality (pdf 375)
- The injections error came from diminishing sensitivity (18 vs 20 looks less different than 4 vs 6). The cold-hand error came from duration neglect and the peak-end rule. The mechanisms differ, but both give a decision that is not correctly attuned to the experience.
- Choosing to endure the longer pain means something is wrong with the decision.
- Preferences from personal experience, even laid down within the last quarter of an hour, cannot be fully trusted to reflect our interests. This is a "profound challenge" to the cornerstone of the rational-agent model, consistent preferences that people know how to maximize.
- We want pain brief and pleasure long. Memory, a function of System 1, represents the peak and the end, so a memory that neglects duration will not serve that preference.
- Kahneman adds that decisions that do not produce the best experience, and erroneous forecasts of future feelings, are bad news for believers in rational choice, and that an inconsistency is built into the design of our minds.

### Speaking of Two Selves (pdf 375–376)
Two sample remarks: judging a failed marriage only from the remembering self's view, like a symphony with a screech at the end; and calling it "duration neglect" to weigh the good and bad parts equally when the good part lasted ten times as long.

## Toy example (ours, not from the text)
Two episodes, pain rated each minute (0–10):
- X: 6, 6, 6, 6 (4 minutes).
- Y: 6, 6, 6, 6, 3, 3 (6 minutes).

Hedonimeter totals (area, one minute per reading): X = 6+6+6+6 = 24; Y = 24+3+3 = 30. So Y has more total pain.
Peak-end (average of peak and last reading): X = (6+6)/2 = 6; Y = (6+3)/2 = 4.5.
Y is remembered as milder (4.5 < 6) although it contains 6 more pain units. If asked which to repeat, a person choosing by memory picks Y, the same pattern as the cold-hand long episode.

## Concepts
- [[experienced-utility]] (new) — pain and pleasure as lived moment by moment; Bentham's sense (pdf 368)
- [[decision-utility]] (new) — "wantability"; the sense in which economics uses utility (pdf 368)
- [[hedonimeter-total]] (new) — area under the curve of momentary pain or pleasure reports, with all moments weighted equally (pdf 370–371)
- [[peak-end-rule]] (new) — retrospective rating ≈ average of worst-moment and end-moment levels (pdf 370)
- [[duration-neglect]] (new) — episode length has no effect on retrospective ratings (pdf 370)
- [[experiencing-self-vs-remembering-self]] (new) — the self that answers whether it hurts now versus the self that judges how the episode was on the whole; the remembering self decides (pdf 371–372)
- [[less-is-more-effect]] (new) — a set with more elements is judged in a way a sum would not predict (e.g. adding broken dishes lowers a set's value), because System 1 represents sets by averages, norms and prototypes (pdf 374)
- [[diminishing-sensitivity]] (new) — equal changes matter less at higher levels; explains the injections error (pdf 375)

## Canonical instances
- [[injections-puzzle]] — equal pain per injection, yet 6→4 is valued above 20→18 (pdf 368)
- [[colonoscopy-study]] — peak-end rule and duration neglect in 154 patients (pdf 369–371)
- [[cold-hand-experiment]] — 80% chose to repeat the longer, worse episode (pdf 372–373)
- [[scratched-symphony]] — a bad end "ruins" the memory, not the experience (pdf 372)
- [[rat-duration-neglect]] — rats' fear and eagerness depend on intensity, not duration (pdf 374)
- [[hsee-dishes-and-linda]] — earlier less-is-more cases (pdf 374)

## Bridges (candidates)
- [structural-analogy] decision utility vs. experienced utility ↔ decision-game-theory: preference relation / utility function — the standard theory judges choices only by internal consistency; here an external standard is added.
- [structural-analogy] peak-end rule ↔ heuristic / bounded rationality — a cheap summary of an episode saves memory and costs accuracy.
- [structural-analogy] "set represented by a prototype, not a sum" ↔ representativeness (Linda) — the same System 1 feature.
- [metaphor] remembering self "keeping score" ↔ an agent whose objective is a proxy of the true payoff.

## Questions this raises
- If remembered utility is a poor guide, should doctors or policy makers optimize for memory or for experience? Kahneman only sketches both goals (pdf 371).
- How far does the remembering self's rule hold for long episodes such as a whole life or a marriage?
- If preferences can be wrong even after recent personal experience, what is the standard for "good" decisions beyond consistency?

## Reading notes
- Printed page numbers are unknown in the supplied metadata (none is visible in the pdf 370 image), so all references use (pdf N).
- The text layer has garbled fragments (e.g., "T Jon e t8221; T Jhe", "worst rati Jon er soever on ng") in the text layer. The fragment on pdf 370 also appears in the page image, so it is damage in the source file itself. The meaning can be guessed from context, but only pdf 370 was checked against an image. Only pdf 370 was checked against its image: Figure 15 shows patient A ending at about 8 minutes and patient B at about 24 minutes, with peaks of about 8 for both.
- Figure 15 data are not given in text beyond the numbers cited above.
