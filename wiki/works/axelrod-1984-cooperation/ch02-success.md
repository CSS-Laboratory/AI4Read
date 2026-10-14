---
id: axelrod-1984-cooperation/ch02-success
work: axelrod-1984-cooperation
unit: "Chapter 2 — The Success of TIT FOR TAT in Computer Tournaments"
pages: 27-54
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 9
---
# The Success of TIT FOR TAT in Computer Tournaments

## L0 — One line
In two computer tournaments of the repeated Prisoner's Dilemma, the simple rule TIT FOR TAT won both, and Axelrod traces its robust success to being nice, retaliatory, forgiving and clear.

## L1 — The gist (≤ 120 words)
What is a good way to play the repeated Prisoner's Dilemma, given that no strategy is best against every opponent? Axelrod invited game theorists, and later a much wider public, to submit programs to two computer tournaments in which every program plays every other. The simple TIT FOR TAT won both. It also won five of six hypothetical tournaments and stayed first in a simulation of future rounds. Axelrod attributes its robust success to being nice (never defecting first), retaliatory (answering a defection at once), forgiving (returning to cooperation afterwards) and clear. Round-one entrants made systematic errors: too competitive, not forgiving enough, too pessimistic. The aim is practical advice on how to act in such settings.

**Prerequisites:** the Prisoner's Dilemma payoffs (3, 1, 5, 0) and the idea of a strategy that depends on history; Proposition 1 of chapter 1 (no best strategy independent of the other player's strategy); proportions and averages.

## L2 — Key ideas
- **No best strategy, so test strategies against each other.** Proposition 1 says what is best depends on the other player. Existing literatures say little about how to play well, so Axelrod uses computer tournaments of informed entrants (pp. 27–30).
- **The simplest entry won both rounds.** TIT FOR TAT (cooperate first, then copy the other's last move) won round one among 14 entries and round two among 62. No entrant who knew this beat it (pp. 31–32, 42).
- **Niceness (never defecting first) went with success.** In round one all eight top entries were nice (relaxed definition) and no other entry was. In round two the correlation of niceness with score was .58, with exceptions (pp. 33, 43–44).
- **Echoes and too little forgiveness are costly.** In round one JOSS's occasional defections set off mutual retaliation with TIT FOR TAT that, in the illustrative game, lasted to the end. In the round-one environment, TIT FOR TWO TATS (which defects only after two defections in a row) would have won (pp. 36–39).
- **Round-one entrants made systematic errors.** They were too competitive, not forgiving enough, and too pessimistic about the other side's responsiveness (p. 40).
- **Exploiting easygoing rules did not pay in round two.** TESTER and TRANQUILIZER exploited easygoing rules but ranked 46th and 27th. It also paid to be retaliatory, not only nice (pp. 44–47).
- **TIT FOR TAT was robust.** It won five of six hypothetical tournaments, and in a simulation of future generations it never lost first place. Success based on exploiting others eroded as the exploited rules died out; HARRINGTON is the example (pp. 48–53).
- **Robustness comes from the combination of properties.** Nice, retaliatory, forgiving, and clear. Clarity helps because others can recognise TIT FOR TAT and see that it cannot be exploited (pp. 53–54).

## L3 — Walkthrough

### Why a tournament (pp. 27–30)
- Proposition 1 of chapter 1 shows there is no one best strategy. What is best depends in part on what the other player is likely to do, and that may well depend on what the other expects you to do (p. 27).
- Three literatures use the Prisoner's Dilemma. (1) Psychology experiments: hundreds of articles; the iterated game has become "the E. coli of social psychology" (p. 28). (2) Models of social processes, such as the arms race (Richardson), oligopoly, collective action and vote trading (p. 28). (3) Abstract analysis of rationality, effects of choices on others, and cooperation without enforcement (p. 29).
- None of them says much about how to play well. Virtually all experimental players meet the formal game for the first time. Natural-setting evidence is slow and covers no more than a few dozen choices. Abstract work often changes the game to remove the dilemma (p. 29).
- A new approach needs people with a rich understanding of **non-zero-sum** settings (interests partly coincide, partly conflict). It must use two facts: effectiveness depends on the other strategies present, and an effective strategy must use the history so far (p. 30).
- A **computer tournament** meets these needs. Each entrant writes a program that picks cooperate or defect each move using the history. If entrants are recruited mainly from people familiar with the game, they can be assured that their rules face other informed rules, and the state of the art is represented (p. 30).

### Round one: set-up (pp. 30–32)
- Professional game theorists were invited. It was a **round robin**: every entry plays every other, its own twin, and RANDOM (cooperates or defects with equal probability). Each game had exactly 200 moves (p. 30).
- Payoffs per move: 3 each for mutual cooperation, 1 each for mutual defection; a lone defector gets 5, the lone cooperator 0 (pp. 30–31).
- The whole round robin was run five times for stabler scores: 120,000 moves, 240,000 choices. There were 14 entries from five disciplines (psychology, economics, political science, mathematics, sociology) (p. 31).
- TIT FOR TAT (Anatol Rapoport) won. It was the simplest program. It starts with cooperation and then does what the other did on the previous move (p. 31).
- Known properties: it elicits a good degree of cooperation from humans, is not very exploitable, and does well with its twin. Its disadvantage is being too generous to RANDOM (pp. 31–32).
- It was a known strong competitor: second in a preliminary tournament and first in a variant of it. Entrants had a description of that tournament, and many tried to improve on TIT FOR TAT. None of the more complex programs did as well (p. 32).
- Contrast: in computer chess, complexity is needed. Johann Joss's least complex program came last in a chess championship. His Prisoner's Dilemma entry was a small modification of TIT FOR TAT and lowered performance (p. 32).
- Neither the author's discipline, nor program brevity, nor length accounts for success (p. 32).

### Round one: scores and niceness (pp. 32–34)
- Benchmarks for 200 moves: 600 points for constant mutual cooperation, 200 for constant mutual defection; scores of 0–1000 are possible. TIT FOR TAT averaged 504 (pp. 32–33). *(added step: 200×3 = 600, 200×1 = 200, 200×5 = 1000.)*
- **Nice** = never the first to defect. For this tournament the definition was relaxed to include rules that do not defect first before the last few moves, say before move 199 (p. 33).
- Each of the eight top-ranking entries was nice. None of the other entries was. Nice entries averaged 472–504; the best non-nice entry got 401 (p. 33).
- Nice rules got about 600 with each other and with their own twins. End-game variations did not account for much of the score variation (p. 33).
- So the ranking among nice rules depended on their scores against non-nice rules. It was largely determined by two of those rules, the **kingmakers**: they do not do well themselves but largely fix the order among top contenders (p. 34).
- **DOWNING**, the main kingmaker, was based on "outcome maximization". It estimates two probabilities: that the other cooperates after DOWNING cooperates, and that it cooperates after DOWNING defects. It updates them every move and picks the choice that maximises its long-term payoff, assuming this model is right (p. 34).
  - If the two probabilities are similar, the other seems unresponsive, so DOWNING defects. If the other cooperates after cooperation but not after defection, it seems responsive, so DOWNING cooperates. Under some circumstances DOWNING alternates cooperation and defection (pp. 34–35).
  - It starts by assuming both probabilities are .5 but gives that estimate no weight once data come in. By initially assuming that the other player is unresponsive, it is doomed to defect on the first two moves (p. 35).
  - Many rules punished those defections. TIT FOR TAT and TIDEMAN AND CHIERUZZI reacted so that DOWNING learned that defection does not pay and cooperation does. All other nice rules "went downhill" with DOWNING (p. 35).
- **Axelrod's explanation of niceness paying:** the nice rules did well largely because they did so well with each other, and because there were enough of them to raise each other's average score substantially (p. 35).

> *Intuition note.* Nice rules scored about 600 with one another, so differences among them came from how they handled the few non-nice rules. The result is for round one and uses the relaxed definition of "nice".

### Forgiveness and the echo (pp. 35–38)
- **Forgiveness**: a rule's propensity to cooperate after the other has defected (p. 36).
- FRIEDMAN was the least forgiving nice rule and scored lowest of the nice rules. It retaliates permanently after any defection. TIT FOR TAT is unforgiving for one move, then forgives (p. 36).
- One reason the non-nice rules did badly: most rules were not very forgiving (p. 36).
- **JOSS** is TIT FOR TAT, except that 10 percent of the time it defects after the other cooperates (p. 36).
- Table 1 (JOSS vs TIT FOR TAT, 200 moves; p. 37):
  - Both cooperate on moves 1–5. JOSS defects on move 6. TIT FOR TAT defects on 7, and JOSS answers on 8 (p. 37).
  - This "echo" has JOSS defecting on later even moves and TIT FOR TAT on later odd moves (p. 37).
  - On move 25 JOSS defects again, TIT FOR TAT answers on move 26, and a second echo starts. After move 25 both defect every move, one point each per turn (p. 37).
  - Final score: TIT FOR TAT 236, JOSS 241. JOSS did slightly better, but both did poorly (p. 37).
  - *(added step: 15 + 9·5 + 1 + 175 = 236 for TIT FOR TAT; 15 + 10·5 + 1 + 175 = 241 for JOSS.)*
- Moral: if both sides retaliate like this, it does not pay to be as greedy as JOSS (p. 38).
- A major lesson is to minimise **echo effects** where a single defection can set off long mutual recriminations (p. 38). A sophisticated analysis must go at least three levels deep (p. 38):
  1. Direct effect: a defection always earns more than a cooperation.
  2. Indirect effect: the other side may or may not punish.
  3. Tertiary effect: answering the other's defection may repeat or amplify one's own earlier exploitative choice.
- A defection can look good at levels 1 and 2 while the real cost lies at level 3. Many rules wound up punishing themselves, with the other player delaying the punishment by a few moves (p. 38).

> *Intuition note.* In Table 1 each side copies the other's last move, so one defection bounces back and forth. Both ended with about one point per move, far below cooperation.

### Rules that would have won (pp. 38–40)
- Several rules would have beaten TIT FOR TAT in the round-one environment. This warns against the facile belief that an eye for an eye is necessarily the best strategy (pp. 38–39).
- **TIT FOR TWO TATS** (the sample program sent to entrants) defects only if the other defected on the previous two moves. It would have won if mailed in. A common error of contestants was to expect gains from being less forgiving than TIT FOR TAT, whereas there were big gains from being more forgiving (p. 39).
- **LOOK AHEAD**, inspired by AI chess techniques, won the preliminary tournament and would have won this one (p. 39).
- A modification of DOWNING that started by assuming the others are responsive would have won by a large margin: first place rather than tenth (pp. 39–40).
- Axelrod's summary: entries were too competitive for their own good. Many defected early without provocation. The optimal forgiveness was considerably greater than that of any entry (except possibly DOWNING). DOWNING floundered on its misplaced pessimism (p. 40).
- Even expert strategists from several disciplines made these systematic errors (p. 40). Results of one tournament are not definitive, since effectiveness depends on the other strategies present, so a second round was run (p. 40).

### Round two (pp. 40–48)
- Entrants received the detailed round-one analysis, including the supplementary rules that would have done well. Each knew the others knew it, so the round presumably began at a higher level of sophistication (p. 41).
- There were 62 entries from six countries, recruited largely through small-computer journals plus the earlier game theorists. Contestants ranged from a ten-year-old hobbyist to professors in many fields (p. 41).
- TIT FOR TAT was again the simplest entry and won again. Only one person (Rapoport) submitted it, although anyone could submit any program (p. 42).
- Games ended probabilistically, with chance 0.00346 of ending after each move, equivalent to $w = .99654$, the weight of the next move relative to the current one (a parameter from ch. 1; not defined in this unit) *(added step: $1 - 0.00346 = 0.99654$)*. Since nobody knew when the last move would come, end-game effects were avoided (pp. 42–43).
- No personal attribute correlated significantly with performance: not professor status, being American, or FORTRAN vs BASIC. Short programs did not do significantly better than long ones, nor long than short (p. 43).
- There were 3969 pairings of the 63 rules (including RANDOM) and over a million moves (p. 43).
- Niceness again paid. More than half the entries were nice. Of the top fifteen, all but one were nice (that one ranked eighth). Of the bottom fifteen, all but one were not nice. The overall correlation of niceness with score was .58 (pp. 43–44).
- A rule is **retaliatory** if it immediately defects after an "uncalled for" defection. The author says exactly what is "uncalled for" is not precisely determined. Without such a response, the other may take more and more advantage (p. 44).
- Among nice rules, rankings depended largely on how they coped with challengers that used controlled numbers of defections (p. 44).
  - **TESTER** (46th) defects on move 1 to test the other. If the other ever defects, it apologises by cooperating and plays tit-for-tat for the rest of the game. Otherwise it cooperates on moves 2 and 3 and defects every other move afterwards (p. 44).
    - It never defects twice in a row, so TIT FOR TWO TATS always cooperates with it and is badly exploited (p. 45).
    - Three variants of Downing's outcome-maximization principle (two REVISED DOWNING submissions and one slightly modified version) were also exploited, because they judged that a program cooperating just over half the time after their cooperation should be answered with cooperation. They would have done better to defect on move 2, as TIT FOR TAT and other high-ranking rules did, which would have drawn TESTER's apology (p. 45).
  - **TRANQUILIZER** (27th) first builds mutual cooperation, then cautiously tries unprovoked defections. It cooperates for the first dozen or two dozen moves. While its average payoff is at least 2.25 points per move, it does not defect twice in succession or more than one-quarter of the time (pp. 45–46).
- Conclusion: it pays to be nice and also retaliatory. TIT FOR TAT is never first to defect, forgives an isolated defection after one response, and is always incited by a defection however good the interaction has been (p. 46).
- Two lessons were drawn from round one (p. 47):
  - Lesson One: "Be nice and forgiving."
  - Lesson Two: "If others are going to be nice and forgiving, it pays to try to take advantage of them."
- Of 62 entries, 39 were nice, nearly all at least somewhat forgiving. TIT FOR TWO TATS (John Maynard Smith) came 24th. REVISED DOWNING, submitted twice, was in the bottom half (p. 47).
- Those who drew Lesson One suffered from those who drew Lesson Two. But the Lesson Two users did not do well either: they often eventually got punished enough to make the game less rewarding than mutual cooperation. TRANQUILIZER and TESTER each beat TIT FOR TAT's score with fewer than one-third of the rules (p. 47).
- No entrant benefited more than it was hurt by trying to exploit easygoing rules. The most successful entries tended to be relatively small variations on TIT FOR TAT designed to give up on seemingly random or very uncooperative players. They did not beat pure TIT FOR TAT, which "got along with almost everyone" (pp. 47–48).

> *Intuition note.* Being too easygoing invites exploiters, and exploiting provokes punishment that costs both sides. In round two nobody gained more than they lost from exploiting.

### Robustness checks (pp. 48–53)
- **Hypothetical tournaments**: modified distributions of entry types (method in Appendix A). TIT FOR TAT won five of six and was second in the sixth (p. 48).
- **Future rounds**: if successful rules became a larger share of each rule's environment and unsuccessful ones a smaller share, continued success would require doing well with other successful rules (p. 48).
- Evolutionary analogy (pp. 49–50): a round is one generation of animals that interact as in the Prisoner's Dilemma and remember past encounters. Each animal's decision rule is used by many individuals. A rule's number of offspring is proportional to its tournament score. A rule with twice another's score is twice as well represented next time (p. 49).
- For humans, the same effect could come from trying strategies and sticking with what works, imitation, or removal from key roles (p. 50).
- The simulation uses the score matrix and the starting proportions to compute the next generation's proportions (p. 50). Results (p. 50):
  - By the fifth generation the lowest eleven entries have fallen to half their initial size. The middle entries hold their own and the top entries slowly grow.
  - By the fiftieth generation the bottom third have virtually disappeared, most of the middle third have begun to shrink, and the top third keep growing.
- Figure 2 plots proportion of population against generations (0–1000). The TIT FOR TAT curve is at the top (p. 51).
- This is an **ecological** perspective: no new rules are introduced. An evolutionary perspective would allow mutations to introduce new strategies (p. 51).
- Early, a rule that does well with all sorts of rules proliferates. Later, success requires good performance with other successful rules (p. 51).
- Success breeds success, provided it derives from interactions with other successful rules. If success comes from exploiting other rules, then as the exploited die out, the exploiter's base erodes (p. 52).
- **HARRINGTON**, the only non-nice rule among the top fifteen, grew for roughly the first two hundred generations alongside TIT FOR TAT. After that there were fewer and fewer prey, it fell behind, and by generation 1000 it was extinct (p. 52).
- Author's conclusion: doing well with rules that do not score well themselves is eventually self-defeating. Not being nice may look promising at first, but in the long run it can destroy the environment it needs (p. 52).
- TIT FOR TAT had a very slight lead in the original tournament and never lost it in simulated generations. By generation 1000 it was the most successful rule and still growing faster than any other (pp. 52–53).

> *Intuition note.* A rule that lives off weak victims loses its food supply as they vanish. A rule that does well with other successful rules keeps its support.

### Why TIT FOR TAT is robust (pp. 53–54)
- Record: highest average of 62 entries in round two; highest in five of six hypothetical tournaments and second in the sixth; first in the simulated future generations; also won round one and did fairly well with human subjects (p. 53).
- Proposition 1 still holds: no rule is best independent of the environment. What can be said for TIT FOR TAT's empirical successes is that it is very robust, doing well over a wide range of environments (p. 53).
- Part of its success might be that other rules anticipate it. Doing well with it requires cooperating with it, which helps it. Even TESTER quickly apologises. Any rule that tries to exploit it simply hurts itself (p. 53).
- It benefits from its nonexploitability because three conditions hold. The possibility of meeting it is salient; once met, it is easy to recognise; once recognised, its nonexploitability is easy to appreciate. So it "benefits from its own clarity" (pp. 53–54).
- It gives up the possibility of exploiting others. Such exploitation is occasionally fruitful, but over a wide range of environments it has three problems (p. 54):
  1. defecting to test risks retaliation from provocable rules;
  2. once mutual recriminations set in, it is hard to escape;
  3. attempts to give up on unresponsive rules (RANDOM or very uncooperative ones) often wrongly gave up on rules that a more patient rule could have salvaged.
- No round-two entry managed to exploit the exploitable without paying too high a cost with others (p. 54).
- Conclusion: its robust success comes from being nice, retaliatory, forgiving and clear. Niceness avoids unnecessary trouble, retaliation discourages persistence in defection, forgiveness helps restore cooperation, and clarity makes it intelligible and so elicits long-term cooperation (p. 54).

> *Intuition note.* The author assigns each property a job: avoid trouble, discourage defection, restore cooperation, and be understood. These are the author's own statements of what each property does (p. 54).

## Toy example (ours, not from the text)
Two TIT FOR TAT players, A and B, play 8 moves with the chapter's payoffs. Suppose A defects once on move 3 (by accident, say); JOSS's deliberate probabilistic defection had a similar echo effect in Table 1. C = cooperate, D = defect.

| Move | A | B | A pts | B pts |
|---|---|---|---|---|
| 1 | C | C | 3 | 3 |
| 2 | C | C | 3 | 3 |
| 3 | D | C | 5 | 0 |
| 4 | C (copies B's C) | D (copies A's D) | 0 | 5 |
| 5 | D | C | 5 | 0 |
| 6 | C | D | 0 | 5 |
| 7 | D | C | 5 | 0 |
| 8 | C | D | 0 | 5 |

A: 3+3+5+0+5+0+5+0 = 21. B: 3+3+0+5+0+5+0+5 = 21. Steady cooperation would give 8×3 = 24 each. The echo gives an average of (5+0)/2 = 2.5 per move from move 3 on.

Now let both players use TIT FOR TWO TATS, with the same accident by A on move 3. On move 4, B sees A's last two moves as C, D, which is not two defections, so B cooperates. A sees B's C, C and cooperates. Everyone cooperates from move 4 on. A: 3+3+5+5×3 = 26. B: 3+3+0+5×3 = 21. Joint total 47, against 42 in the echo case. This illustrates why one isolated defection is costly when both punish at once, in the spirit of pp. 37–39. It is a toy, and says nothing about the real tournament scores.

## Concepts
- [[iterated-prisoner-dilemma]] (new) — the Prisoner's Dilemma played over many moves, with each move's choice able to depend on history (pp. 28, 30)
- [[non-zero-sum-setting]] (new) — interests of participants partly coincide and partly conflict (p. 30)
- [[round-robin-tournament]] (new) — each entry is paired with each other entry; this tournament also paired each with its own twin and with RANDOM (p. 30)
- [[tit-for-tat]] (new) — cooperate on move 1, then copy the other player's previous move (p. 31)
- [[niceness]] (new) — never being the first to defect (relaxed in round one to not before about move 199) (p. 33)
- [[forgiveness]] (new) — propensity to cooperate in moves after the other player has defected (p. 36)
- [[retaliation]] (new) — immediate defection after an "uncalled for" defection by the other (p. 44)
- [[kingmaker-rule]] (new) — a rule that scores poorly itself but largely determines the ranking among the top contenders (p. 34)
- [[echo-effect]] (new) — one defection triggering a long back-and-forth of mutual defections (pp. 37–38)
- [[ecological-simulation]] (new) — future generations in which each rule's number of copies is proportional to its tournament score and no new rules appear (pp. 49–51)
- [[robustness-of-strategy]] (new) — doing well over a wide range of environments (pp. 48, 53)
- [[clarity-of-strategy]] (new) — being easy to recognise and understand, so others see it cannot be exploited (pp. 53–54)
- [[shadow-of-the-future]] — the weight on future moves is $w = .99654$ in round two, via the end-of-game probability 0.00346 (p. 42); the chapter does not use the term itself (canon link; not stated in this unit)

## Canonical instances
- [[tft-wins-tournament-1]] — TIT FOR TAT wins round one among 14 entries, averaging 504 (pp. 31, 33)
- [[joss-tft-echo]] — JOSS vs TIT FOR TAT, Table 1: a single defection leads to mutual defection, 236 vs 241 (p. 37)
- [[downing-kingmaker]] — DOWNING, which estimates the other's responsiveness and starts pessimistic (pp. 34–35, 39–40)
- [[tit-for-two-tats]] — the forgiving sample rule that would have won round one but placed 24th in round two (pp. 39, 47)
- [[tester-and-tranquilizer]] — round-two exploiters that placed 46th and 27th (pp. 44–47)
- [[harrington-extinction]] — non-nice rule that grows, then goes extinct in the ecological simulation (p. 52)
- [[friedman-permanent-retaliation]] — the lowest-scoring nice rule, never forgiving (p. 36)

## Bridges (candidates)
- [structural-analogy] The ecological simulation (share proportional to score) ↔ replicator dynamics: strategies grow in proportion to their payoff. The chapter's footnote on the exact calculation is not in these pages, so same-math is not claimed.
- [structural-analogy] The echo effect ↔ arms-race spirals (Richardson's model is cited on p. 28): mutual retaliation raises costs for both.
- [structural-analogy] Clarity of TIT FOR TAT ↔ credible commitment: a rule that others can easily recognise changes their incentives.
- [metaphor] DOWNING's updating of conditional probabilities ↔ Bayesian learning about types: the chapter describes only an updated estimate.

## Questions this raises
- Would the order of rules change under different payoff numbers? All results here use 3, 1, 5, 0.
- What if a rule makes noisy mistakes? JOSS's deliberate occasional defection shows how costly an isolated defection can be when both sides retaliate.
- Does the success of TIT FOR TAT depend on other entrants having read the round-one report?
- What happens when new strategies can appear (mutation), not only the given rules?

## Reading notes
- Printed page = pdf − 8. All citations use printed pages.
- Footnote markers 1–7 appear in the text, but the footnote texts are not on these pages. I do not report their contents. Appendix A (names, scores, the 63×63 score matrix, method for hypothetical tournaments) is not part of this unit.
- p. 34 says the ranking of the eight top rules was largely determined by two of "the other seven rules". My own arithmetic: fourteen entries minus eight nice rules gives six; adding RANDOM would give seven, but the page does not say this. My own check: 14 entries plus RANDOM is 15 programs. 15×16/2 = 120 games, including twins, × 200 moves × 5 runs = 120,000 moves, matching p. 31. The text does not explain the count.
- p. 44 text layer has a misprint: "I shall called" (should be "call").
- Figure 2 (p. 51) is a line chart. Curves carry labels 1, 3, 2, 6, 7,9, 10, 4, 11, 5, 8, 18, 14,12,15, 13 and "Others". The page does not say what these numbers mean. p. 44 says the one non-nice rule among the top fifteen ranked eighth without naming it, and p. 52 names HARRINGTON as the only non-nice rule in the top fifteen. The curve labelled 8 rises then falls, but the page does not link the label to HARRINGTON. I give no values read from the figure.
- Table 1 (p. 37) was read from the page image. The digits match the text layer and the move-by-move description.
