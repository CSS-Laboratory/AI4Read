---
id: axelrod-1984-cooperation/ch06-choose
work: axelrod-1984-cooperation
unit: "Chapter 6 — How to Choose Effectively"
pages: 109-123
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# How to Choose Effectively

## L0 — One line
In a long-running Prisoner's Dilemma, do well by being nice, provocable, clear and not envious, with a level of forgiveness that suits the environment, because your own success depends on drawing cooperation out of the other player.

## L1 — The gist (≤ 120 words)
The chapter asks what advice a player in a durable iterated Prisoner's Dilemma should follow. Using the tournament results and the theory, Axelrod gives four suggestions: don't be envious, don't be the first to defect, reciprocate both cooperation and defection, and don't be too clever. The common thread is that the game is non-zero-sum (both sides can do well together), so the other player's success is not your loss, and the other player adapts to what you do. Two qualifications matter. Defecting first can pay if the future is unimportant or if no one will reciprocate. The best amount of forgiveness depends on the environment.

**Prerequisites:** Prisoner's Dilemma payoffs (T, R, P, S); the idea of a strategy in repeated play; the tournament and chapter 3 results as summarised here.

## L2 — Key ideas
- Judging yourself against the other player's score leads to envy, and envy leads to defection and mutual punishment. A better test is whether you do as well as anyone could with this partner (pp. 111–112).
- TIT FOR TAT (cooperate on move 1, then copy the partner's last move) won the tournament without ever outscoring its partner in a game. It elicited behaviour that let both do well (p. 112).
- Niceness (never defecting first) was the best single predictor of tournament success (p. 113).
- Being nice is not always best. Defecting first can pay if the future is too unimportant (the discount parameter $w$, which says how much future interaction counts, is too low) or if cooperation will not be reciprocated. Even so, a small share of interactions with responsive players like TIT FOR TAT can make cooperating worthwhile (pp. 115–116).
- Reciprocity means cooperating first and then copying the partner's last move. TIT FOR TAT is nice, provocable (it answers a defection with a defection) and maximally discriminating (it can invade a world of meanies in the smallest possible cluster), and it does not destroy the environment it needs (pp. 118–119).
- The right level of forgiveness depends on the environment. A roughly one-for-one response is likely to work in many settings (p. 120).
- Clever strategies that treat the other player as a fixed part of the environment fail, because the other player adapts to you (pp. 120–121).
- Being incomprehensible is dangerous: a strategy that looks random looks unresponsive, so the other player has no reason to cooperate. TIT FOR TAT's clarity is part of its success (pp. 122–123).

## L3 — Walkthrough

### Introduction (pp. 109–110)
Foresight is not needed for cooperation to evolve, but it can help (p. 109). This chapter advises participants; the next advises reformers. The goal is to score as well as possible over a series of interactions with another player who is also trying to score well. The player has a short-run incentive to defect but can do better in the long run through mutual cooperation (p. 109). Four suggestions follow for a *durable* iterated Prisoner's Dilemma (p. 110):
1. Don't be envious. 2. Don't be the first to defect. 3. Reciprocate both cooperation and defection. 4. Don't be too clever.

### 1. Don't be envious (pp. 110–113)
- **Zero-sum vs non-zero-sum.** In a zero-sum interaction (zero-sum: one side's gain is the other's loss), such as chess, you must beat the other player. Most of life is not like that: both sides can do well or both can do poorly (p. 110).
- **Classroom observation.** Axelrod told student pairs to score well for themselves and not to care about the other's score. This did not work (p. 111). Students use the comparison with the other player's score as a standard. Sooner or later one defects to get ahead, and the other defects so as not to fall behind. Recriminations follow. When one tries to restore cooperation, the other fears a ploy (p. 111).
- **Why envy is self-destructive.** Envy leads to attempts to remove the other's advantage. In this game that can only be done by defection, which leads to more defection and mutual punishment (p. 111). Comparing scores is a good standard only if your goal is to destroy the other player, which is usually impossible or very costly (p. 111). Axelrod proposes a better standard: "Given the strategy of the other player, are you doing as well as possible?" (pp. 111–112).
- **TIT FOR TAT as evidence.** It never once scored better than the other player in a game. It lets the other defect first and never defects more often than the other has. So it gets the same score as its partner or a little less. It won by eliciting mutually rewarding behaviour, and it did this so consistently that its total was higher than any other strategy's (p. 112).
- **Conclusion.** In a long iterated game the other's success is "virtually a prerequisite" of your own. Axelrod adds that you need not beat the other player to do well, especially when you meet many different players (p. 112).
- **Examples.** Legislators can cooperate without threatening each other's standing at home, because the main threat comes from challengers in the home district (pp. 112–113). A buyer should not envy a supplier's profit. Pressing it down, for example by paying late, invites retaliation. Retaliation could mean slower deliveries, lower quality control, worse discounts, or less timely market news (Macaulay 1963), often without being labelled as punishment (p. 113).

*Intuition note:* Your score is what you collect, not the gap between you and your partner. Trying to close the gap by defecting usually shrinks both scores.

### 2. Don't be the first to defect (pp. 113–117)
- **Tournament evidence.** Niceness (never being the first to defect) was the single best predictor of performance (p. 113). Round 1: all of the top eight rules were nice and none of the bottom seven were. Round 2: all but one of the top fifteen were nice (the exception ranked eighth), and all but one of the bottom fifteen were not nice (pp. 113–114).
- **Not-nice rules did badly.** TESTER defected at the start and backed off if punished. TRANQUILIZER waited a dozen or two moves, then added more frequent defections until the other player forced it to back off. Neither did well, because many players were not exploitable and the conflicts were costly (p. 114).
- **Experts.** Almost half of the game theorists' entries in round 1 were not nice. About a third were not nice in round 2 (p. 114).
- **Theory (ch. 3).** A population of nice rules is the hardest to invade, because nice rules do well with each other. A nice population that resists one mutant rule can resist any cluster of invaders (p. 114, citing p. 67).
- **Qualification 1: short futures.** TIT FOR TAT is stable only when the discount parameter $w$ is high enough relative to the payoffs $R, S, T, P$. By proposition 2, if $w$ is too low and the other uses TIT FOR TAT, you do better alternating defection and cooperation, or always defecting. So if you will probably not meet the other again, defecting at once beats being nice (p. 115).
  - *Gypsy example.* Axelrod says this fact has unfortunate implications for groups known to move from place to place. An anthropologist (as he reports) finds that Gypsies and non-Gypsies approach each other expecting trouble or double-dealing (p. 115). In a quoted account (Gropper 1975), Gypsies paid a doctor only part of his bill, "in revenge" (p. 115). In a California town, Gypsies did not pay all of a doctor's bill but paid municipal fines promptly (Sutherland 1975). Axelrod says "Presumably" this is because they returned to the same town each winter and could not shop around for another garbage service, while there were always enough doctors (pp. 115–116).
- **Qualification 2: no reciprocation.** If everyone else always defects, one individual can do no better than always defect. But from chapter 3, if even a small share of one's interactions are with TIT FOR TAT players, TIT FOR TAT can beat always-defect. In the chapter 3 example, 5 percent was enough for the small cluster to beat the typical defector (p. 116).
- **Will anyone reciprocate?** This may be hard to tell in advance. But if enough time has passed for many strategies to be tried and for successful ones to spread, one can be "fairly confident" that some will reciprocate. A small cluster of discriminating nice rules can invade a population of meanies, and once established they can protect themselves from reinvasion (p. 116).
- **"Playing it safe" is risky.** Defecting until the other cooperates invites retaliation, and you then must escape from exploitation or mutual defection. If you punish the other's retaliation, the problem echoes. If you forgive, you risk looking exploitable (p. 117).
- **Ecological analysis.** The only top-fifteen non-nice rule in round 2 was HARRINGTON (eighth). It scored well against low-ranking entries, but these shrank in hypothetical future rounds, and HARRINGTON eventually died out. Doing well with rules that do poorly themselves is self-defeating. Not being nice may look promising at first but can destroy the environment one needs (p. 117).

*Intuition note:* Starting with cooperation pays when the game is long, because it avoids costly fights. The chapter names two cases where defecting first can pay: the other player is unlikely to be met again, or cooperation will not be reciprocated.

### 3. Reciprocate both cooperation and defection (pp. 118–120)
- **Record.** TIT FOR TAT cooperates on move 1, then copies the other's previous move. It won round 1 with a higher average than any entry by professional game theorists. It won again in round 2 even though anyone could have submitted it after seeing round 1 (p. 118). It also did best in hypothetical future rounds, so it does not destroy the basis of its own success (p. 118).
- **Theory.** When the future is important enough relative to the present, TIT FOR TAT is collectively stable (if everyone uses it, no player does better by using anything else) (pp. 118–119). It is maximally discriminating (ch. 3, p. 66). By proposition 6, it can therefore invade a world of meanies in the smallest possible cluster. It is also *provocable* (it answers defection with defection), and proposition 4 shows provocability is required for a nice rule to resist invasion (p. 119).
- **Punishment vs forgiveness.** TIT FOR TAT defects exactly once after each defection. Axelrod says it is hard to know whether one-for-one is the best balance, since rules with other balances were not submitted. Extracting more than one-for-one risks escalation, and less risks exploitation (p. 119).
- **TIT FOR TWO TATS** defects only after two defections in a row. It would have won round 1 if submitted, because it avoided recriminations that troubled TIT FOR TAT. In round 2 it was submitted but did not score in the top third, because some rules exploited its forgiveness of isolated defections (pp. 119–120).
- **Moral.** The best level of forgiveness depends on the environment. If the main danger is unending recrimination, be generous. If it is strategies that exploit easygoing rules, too much forgiveness is costly. The evidence suggests something approaching one-for-one is "likely to be quite effective" in a wide range of settings (p. 120).

*Intuition note:* A rule has to balance two risks: answering defection with more than one defection risks escalation, and answering with less risks exploitation. The right mix depends on who else is around.

### 4. Don't be too clever (pp. 120–123)
- **Tournament result.** Sophisticated rules did not beat simple ones. The "maximizing" rules often did poorly and fell into mutual defection. They drew wrong inferences about the other player, for example reading one trial defection as proof the other could not be enticed to cooperate. The core flaw was ignoring that their own behaviour would make the other player change (pp. 120–121).
- **Why chess and umbrellas differ.** Clouds do not react to your umbrella, and in zero-sum chess you can assume the opponent picks the most dangerous move, so complex analysis pays. In a Prisoner's Dilemma the other player responds to your choices, should not be regarded as out to defeat you, and is likely to echo your behaviour back (p. 121). Modelling the other as fixed ignores the reverberating process of mutual adaptation, and none of the complex tournament rules handled it well (p. 121).
- **Permanent retaliation** (cooperate until the other defects once, then never cooperate again). It is nice, so it does well with nice rules and with unresponsive rules such as the random rule. With many others it does poorly, because it gives up on rules that try an occasional defection but back off when punished. It is "too harsh for its own good" (pp. 121–122).
- **Rules too complex to read.** Some probabilistic strategies were so complex they could not be told apart from random choice. A random-looking player looks unresponsive, so the other has no incentive to cooperate (p. 122). A person can explain complicated reasons, but the other may think they were invented for the occasion and judge you "unreformable", which leads to defection (p. 122).
- **Clarity of TIT FOR TAT.** The one-for-one pattern is easy to understand, so behaviour is predictable. The other player can see that cooperating is the best response. Provided the game is sufficiently likely to continue for at least one more interaction, nothing beats cooperating now to get cooperation next move (pp. 122–123).
- **Chess contrast.** In chess, keeping the opponent guessing helps, since the opponent's inefficiency benefits you. In the iterated Prisoner's Dilemma you benefit from the other's cooperation and should encourage it by making clear you will reciprocate. Words can help, but actions speak louder (p. 123).

*Intuition note:* Cleverness helps against things that do not react to you. Against a partner who reacts, being easy to read can help you more than being hard to predict.

## Toy example (ours, not from the text)
Assume payoffs $T=5,\ R=3,\ P=1,\ S=0$ and 10 rounds per pair. Compare TIT FOR TAT (TFT) with ALL-D (always defect).
- TFT vs TFT: both cooperate every round, so $10 \times 3 = 30$ each.
- ALL-D vs ALL-D: $10 \times 1 = 10$ each.
- TFT vs ALL-D: round 1 gives TFT $S=0$ and ALL-D $T=5$. In rounds 2–10 both defect: $9 \times 1 = 9$ each. TFT total $= 0 + 9 = 9$. ALL-D total $= 5 + 9 = 14$. TFT never beats its partner.
- Suppose each player meets one TFT and one ALL-D. TFT: $30 + 9 = 39$. ALL-D: $14 + 10 = 24$.

TFT loses its head-to-head game against ALL-D (9 vs 14) but has the higher total (39 vs 24), because it gets 30 from the cooperating partner. This shows suggestion 1: do not judge yourself against the other's score.

## Concepts
- [[iterated-prisoners-dilemma]] (new) — the Prisoner's Dilemma played repeatedly, so long-run cooperation can beat short-run defection (p. 109)
- [[zero-sum game & minimax]] — one side's gain is the other's loss; chess is the example. The chapter contrasts it with the Prisoner's Dilemma (p. 110)
- [[envy-as-standard]] (new) — judging success by comparing one's score with the other's; leads to defection and mutual punishment (p. 111)
- [[niceness]] (new) — a rule that is never the first to defect (p. 113)
- [[tit-for-tat]] (new) — cooperate first, then copy the other's last move (p. 118)
- [[provocability]] (new) — answering defection with defection; required for a nice rule to resist invasion (p. 119)
- [[forgiveness-level]] (new) — how much punishment follows a defection; the best level depends on the environment (p. 120)
- [[shadow of the future]] — here the discount parameter $w$: how much future interaction matters (p. 115)
- [[reciprocity (direct, indirect, network)]] — cooperation sustained by answering the partner's moves in kind (p. 118)
- [[permanent-retaliation]] (new) — cooperate until the first defection, then never again; too harsh (pp. 121–122)
- [[clarity-of-strategy]] (new) — being understandable to the partner, which makes responsiveness visible and cooperation worth offering (pp. 122–123)

## Canonical instances
- [[computer-tournament]] — source of evidence: niceness and TIT FOR TAT results (pp. 113, 118)
- [[classroom-pd-play]] — students told to ignore the other's score still compare scores and slide into defection (p. 111)
- [[tester-tranquilizer-harrington]] — non-nice rules that did poorly or died out in ecological analysis (pp. 114, 117)
- [[tit-for-two-tats]] — forgiving rule that would have won round 1 but did badly in round 2 (pp. 119–120)
- [[gypsy-doctor-example]] — short interactions can make defecting first pay (pp. 115–116)
- [[congress-and-supplier-examples]] — envy is pointless where cooperation helps both sides (pp. 112–113)

## Bridges (candidates)
- [structural-analogy] Don't-be-envious advice ↔ decision-game-theory: preferring absolute payoff to relative payoff (own score vs. score gap) — the advice swaps a relative standard for an absolute one.
- [structural-analogy] "Too clever" modelling of a partner as fixed ↔ decision-game-theory: best response against a static opponent model — fails when the partner adapts.
- [metaphor] Clarity of TIT FOR TAT ↔ signaling: making your intentions legible so others can respond.
- [structural-analogy] Qualification about low $w$ ↔ repeated game & folk theorem: patience thresholds for cooperation.

## Questions this raises
- How high must $w$ be, relative to $R, S, T, P$, for TIT FOR TAT to be stable? (The chapter refers to proposition 2 without stating it.)
- Which environments would reward more or less forgiveness than one-for-one?
- If the other player can misread your move or make an error, does one-for-one reciprocity still work?
- Can a player know in practice whether the future is long enough to make niceness pay?

## Reading notes
- Printed pages 109–123 correspond to pdf 113–127 (printed = pdf − 4).
- Footnote markers 1–4 appear in the text (pp. 111, 112, 116), but the notes are not in these pages. Chapter references (propositions 2, 4, 6; pp. 66–67) are to material outside this unit and are reported only as the chapter states them.
- The text layer's page footer on printed p. 121 reads "111", which looks like a misprint or OCR error for 121. The running header on p. 112 reads "Participants, and Reformers" (a comma), unlike the other pages.
- I worked from the extracted text layer. No page images were visible to me, so the numbers and names were checked only against the text layer.
