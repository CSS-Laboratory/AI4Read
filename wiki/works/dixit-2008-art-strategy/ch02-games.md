---
id: dixit-2008-art-strategy/ch02-games
work: dixit-2008-art-strategy
unit: "2. Games Solvable by Backward Reasoning"
pages: 45-73
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Games Solvable by Backward Reasoning

## L0 — One line
In sequential-move games (players move in turn), work out the other players' future responses and use them to choose your best current move: "look forward and reason backward".

## L1 — The gist (≤ 120 words)
How should you play a game where players move in turn? Dixit and Nalebuff give Rule 1: anticipate where your choices lead, then reason back from the end of a game tree. They apply it to Lucy and Charlie Brown, a risky investment, the line-item veto, the 21-flags game on *Survivor*, and a football decision. Experiments (such as the ultimatum game, a take-it-or-leave-it split) show that people also care about fairness and altruism, so the method needs richer assumptions about motives. For huge games like chess, full backward reasoning is infeasible; it must be combined with judgment of positions. Taking unavoidable risks early often keeps options open.

**Prerequisites:** Reading a branching diagram (tree); simple percentages; the idea of a payoff ranking.

## L2 — Key ideas (5–10 bullets)
- **Rule 1:** look ahead to others' future responses and reason backward to choose your present move (p. 47).
- A **game tree** (several players) differs from a **decision tree** (one player). In games you must predict others' choices by thinking as they would (p. 49).
- More freedom can hurt in games, because it changes what others do. The president may be worse off with a line-item veto (the power to cancel single items in a bill). Tying your hands can help (pp. 53–55).
- The 21-flags game (tribes take 1–3 flags in turn; whoever takes the last flag wins) is fully solved by working back from the end; actual players erred almost everywhere (pp. 56–58).
- The 21-flags game was fully solvable because it had no uncertainty about chance, others' motives, or others' actions (pp. 59–60).
- Ultimatum experiments (one player proposes a split; the other accepts, or refuses and both get nothing) and dictator experiments (the other player has no say) differ from the prediction for purely selfish, perfectly calculating players. The authors conclude that fairness and altruism should be included in players' objectives (pp. 61–67).
- For huge trees such as chess, combine look-ahead with a judgment of positions. Predict what others will actually do, not what you would do (pp. 68–70).
- Case study: if you must take a risk, take it early (pp. 71–73).

## L3 — Walkthrough

### Charlie Brown and Lucy (pp. 45–46)
Lucy holds the football and Charlie may kick. Lucy prefers seeing him fall to letting him kick. So Charlie should forecast that she will pull the ball away, and decline (p. 45). Her move lies in the future, but that does not make it uncertain (p. 45).

Two kinds of strategic interaction (p. 46):
- **Sequential:** players alternate moves.
- **Simultaneous:** players act at once, ignorant of each other's current actions. Chapter 3 covers these.

Some games, such as football, mix both (p. 46).

### The First Rule of Strategy (p. 47)
**RULE 1: Look forward and reason backward.** Anticipate where your initial decisions will lead and use this to calculate your best choice (p. 47).

> **Intuition note.** Do not pick the first step that looks best. First ask what happens at the end, then what each person would do at each step on the way, and only then choose your first move.

### Decision trees and game trees (pp. 48–50)
- A tree shows the options at each junction. The Princeton-to-New York example: do not take the route whose first branch looks best; anticipate later choices. For a downtown destination, PATH from Newark beats driving (pp. 48–49).
- A tree of a game with several players is a **game tree**. Decision tree is reserved for one-person situations (p. 49).
- **Charlie's tree** (p. 50): Charlie accepts or refuses. If he accepts, Lucy chooses between letting him kick and pulling the ball away. Charlie "prunes" the branch Lucy will not choose. What remains, accepting, leads to a fall, so he refuses (p. 50).

### Business version: Fredo (pp. 50–52)
- Fredo asks Charlie to invest $100,000 and promises to turn it into $500,000, shared equally. If Fredo honors the contract he pays Charlie $250,000, a profit of $150,000 (pp. 50–51).
- Without a clear reason to believe him, Charlie should predict that Fredo absconds. The tree is identical in essentials to Lucy's (p. 51).
- A reputation or an ongoing relationship (for example, Fredo needs US financing or exports goods there) could make Fredo honest. That would make this a larger game (p. 51).

Three remarks (pp. 51–52):
1. Different situations can share one mathematical form, and theory transfers knowledge between them. Theory has limits but is a valuable starting point (pp. 51–52).
2. Fredo should see that a strategic Charlie will not invest, so Fredo needs a way to make his promise credible. Chapters 6 and 7 cover this (p. 52).
3. Games need not be **zero-sum**. Here "invest and honor" is better for both than "no investment". Most games mix common interest and conflict (p. 52).

### More complex trees: the line-item veto (pp. 52–55)
- Setup: Congress likes urban renewal (U); the president likes an antiballistic missile system (M). Both prefer the package to the status quo. Ratings run from 4 (best) to 1 (worst) (p. 53).
- **No veto:** The president signs a bill with U and M, or M alone, and vetoes U alone. Congress therefore passes the package. Both get their second-best outcome (rating 3) (p. 53).
- The president's choices must be shown even at nodes that are not reached. Congress's choice depends on what the president would have done after a different Congress choice (p. 53).
- **With a line-item veto:** Congress foresees that the package would be cut to M alone. So it passes U alone (to be vetoed) or nothing. The authors suppose Congress is indifferent between these. Each party then gets only its third-best outcome (rating 2). The president is worse off for his extra freedom (pp. 54–55).
- **General point:** in single-person decisions, greater freedom of action can never hurt. In games it can, because it influences other players' actions. Conversely, tying your own hands can help (the "advantage of commitment", chapters 6 and 7) (p. 55).

> **Intuition note.** A power you hold changes what the other side offers you. If you will use the power against them, they adjust in advance, and you may end up with less.

**Limits of drawing trees (p. 55).** In chess, White has 20 first moves and Black 20 replies, so 400 distinct paths after one move each. Solving chess by the tree method is beyond the most powerful computer expected in the next several decades (p. 55). Two approaches for moderately complex games: computer programs that build and solve trees, or tree logic without drawing the tree (p. 55).

### Strategies for "Survivors": the 21-flags game (pp. 55–58)
- **Rules:** 21 flags; tribes alternate; each takes 1, 2 or 3 flags (passing is not allowed); whoever takes the last flag wins (p. 56).
- **Actual play:** Sook Jai moved first and took 2, leaving 19 (p. 56).
- **Correct reasoning, working back** (pp. 56–57):
  - Leave the opponent with 4 flags. Whatever it takes (1, 2 or 3), you take the rest and win. Ted Rogers of Chuay Gahn said this (p. 56).
  - To leave 4 at its next turn, leave 8 at its previous turn. Likewise 12, 16, 20.
  - So the correct first move is to take 1, leaving 20. Then Sook Jai wins by leaving 16, 12, 8, 4 (p. 57).
- **Mistakes** (pp. 56–57):
  - Sook Jai took 3 of 9; the correct move was 1, leaving 8. Shii Ann realized this one move too late (pp. 56–57).
  - Chuay Gahn took 2 from 11; it should have taken 3, leaving 8 (p. 57).
  - Facing 19, Chuay Gahn should have taken 3, leaving 16 (p. 57).
  - Facing 6, Chuay Gahn took 2, which was correct (p. 56).
  - "No move" in the authors' table means all moves lose against correct play (p. 57).
  - Almost all choices were wrong. The exception was Chuay Gahn's move at 13, which the authors think was accidental (p. 57).
- Ivy League freshmen needed three or four plays to play correctly throughout. People seem to learn faster by watching than by playing (p. 58).
- **Trip to the Gym No. 1** (hot-potato version: forcing the other team to take the last flag is the win; 21 flags, your move; how many do you take?). Answer is in the book's Workouts section, not in this unit (p. 58).

> **Intuition note.** Start from the end position: "leave 4" wins. Then ask which positions let you reach "4", and repeat. In 21 flags the winning positions to hand over are 4, 8, 12, 16, 20.

### What makes a game fully solvable by backward reasoning? (pp. 59–60)
The authors say 21-flags was fully solvable because it had no uncertainty of any kind; they discuss three kinds:
1. **Natural chance** or hidden information about the position, as with cards. Many later examples include chance (p. 59).
2. **Others' motives and capabilities.** You can almost never know these for sure. You must not assume others share your preferences or those of a hypothetical "rational person" (p. 59). A strategic consultant may help (p. 60).
3. **Others' actions** ("strategic uncertainty"): present in simultaneous moves (penalty kicks, tennis serves, sealed-bid auctions). This needs different, in some respects harder, thinking. This chapter covers only sequential games (p. 60).

### Do people actually solve games by backward reasoning? (pp. 60–67)
- Backward reasoning is the correct (normative) way to analyze sequential games. Whether it also predicts actual outcomes (positive use) is a separate question. Experiments give mixed evidence (pp. 60–61).
- **Ultimatum game** (p. 61): proposer A offers a split of $100. Responder B accepts (split implemented) or refuses (both get nothing).
- **Reverse ultimatum "quick trip to the gym"** (p. 61): each further offer must be more generous. The source states the result: A keeps offering until 99 to B, 1 for himself; the authors advise B against holding out for 99:1.
- **Theoretical prediction** for two purely self-interested, perfect calculators: B accepts anything, so A offers the minimum, say one cent (pp. 61–62).
- **Experiments** (random pairs, played once, anonymous) (p. 62):
  - Offers below 10% of the total are very rare.
  - The median offer is 40–50%; 50:50 is often the single most frequent proposal.
  - Offers giving the responder less than 20% are rejected about half the time.
- **Three reasons for generous offers** (p. 62):
  1. Proposers may be unable to reason backward correctly.
  2. Proposers may have motives other than selfishness: they may act altruistically or care about fairness.
  3. Proposers may fear that responders will reject low offers.
- The first is unlikely because the game is simple. The explanation must be the second, the third, or both (pp. 62–63).
- **Evidence on reasons 2 and 3** (pp. 63–64):
  - Al Roth and coauthors found offers consistent with a balance of own share against the risk of rejection (p. 63).
  - **Dictator game** (the other player has no say): dictators give less than ultimatum proposers but substantially more than zero. So both generous and strategic aspects exist (p. 63).
  - Roles assigned by a contest (entitlement) lower offers by about 10% on average, but they stay well above zero (p. 63).
  - Dana, Cain and Dawes: dictators allocated $10, then were offered $9 for themselves, with the other party getting nothing and never knowing of the experiment. Most accepted. The authors read this as shame at others learning of their greed (p. 64).
- **Responders** (pp. 64–65):
  - The reason for rejecting cannot be reputation-building, since the pairs do not repeat. Any reputational motive would have to be an instinctive rule or an emotional response (p. 64).
  - In fMRI/PET studies, anterior insula activity (linked to anger, disgust) rises as offers become more unequal. Left prefrontal cortex is more active when an unequal offer is accepted (pp. 64–65).
- **Larger stakes** (poorer countries, several months' income): rejection becomes somewhat less likely; offers do not become significantly less generous (p. 65).
- **Cultures** (p. 65):
  - What counts as a reasonable offer varies by up to 10% across cultures.
  - The Machiguenga offered much less (average 26%) and only one offer was rejected.
  - In two cultures with a custom of lavish giving after good luck, offers exceeded 50%.
- Hypotheses can be partly right; multiple causes can coexist (p. 64).

### What to learn from the experiments (pp. 66–68)
- The authors say backward reasoning should remain the starting point. Experiments use novices, as in 21-flags. Experienced players in business, politics and sports have learned more or use computers and consultants (p. 66).
- The more important lesson: people weigh many considerations besides their own reward. Game theory should include fairness and altruism, even a second-round concern to reward or punish others. The authors quote: "Behavioral game theory extends rationality rather than abandoning it." (pp. 66–67)
- **Evolutionary explanation** (the authors call it speculation, p. 67): groups with norms of fairness and altruism have less internal conflict and act collectively better, so such norms may have survival value (p. 67).
- **Burnham's experiment** (p. 67): $40 at stake, male Harvard graduate students. The divider's choices were offer $25 and keep $15, or offer $5 and keep $35. Of those offered $5, 20 accepted and 6 rejected. The rejecters had testosterone levels 50% higher than the acceptors.
- Norms are also passed on by education and socialization (p. 67).
- Fairness and altruism have limits. Innovation needs individualism, so society needs a balance of self-regarding and other-regarding behavior (pp. 67–68).

### Very complex trees: chess (pp. 68–70)
- In principle chess is ideal for backward reasoning: alternating moves, observable and irrevocable moves, no uncertainty about the position or motives. The repetition-draw rule ensures a finite game (p. 68).
- In practice there are about $10^{120}$ nodes. A computer 1,000 times as fast as a typical PC would need $10^{103}$ years to examine them all (p. 68).
- Experts can solve endgames with few pieces. Midgame is far harder; looking ahead five pairs of moves is about as much as experts can do in a reasonable amount of time (p. 68).
- **Practical solution:** look-ahead analysis (the "science") plus value judgments of positions ("knowledge", the "art"). Opening theory codifies knowledge from many games (p. 69).
- **Computers** (p. 69):
  - Early attempts to make computers think like humans failed for many years.
  - Number crunching brought Fritz and Deep Blue to compete with top humans by the late 1990s.
  - Later programs added midgame knowledge from top players.
  - Kasparov versus Fritz X3D (Nov 2003): one win each, two draws.
  - Hydra beat Michael Adams (July 2005): five wins, one draw.
- **Takeaway:** combine Rule 1 with experience for evaluating positions at the end of your forward calculation. Success comes from both together (p. 70).

> **Intuition note.** When the tree is too big, search as far as you can and then judge the position you reach, as a chess player would. This replaces the true end result with an educated estimate.

### Being of two minds (pp. 70–71)
- If both players could analyze all lines, they would agree in advance how the game ends. With partial analysis, the other side may see something you missed, or miss something you saw (p. 70).
- You must predict what others will actually do, not what you would do. It is hard to leave your own shoes behind. This is why people do not play chess or poker against themselves (p. 70).
- Put yourself in their shoes: know what they know, and no more, and use their objectives, not those you wish they had. Firms hire outsiders to play the other side in simulations, and learn from unanticipated moves (pp. 70–71).

### Case study: Tom Osborne and the '84 Orange Bowl (pp. 71–73)
- **Facts** (p. 71):
  - Nebraska (undefeated) needed only a tie to be ranked first. It trailed Miami 31–17, then scored a touchdown (31–23).
  - After a touchdown, a team may kick for 1 point or run/pass for 2.
  - Osborne kicked (31–24). A final touchdown made it 31–30. Nebraska went for 2 and failed, so Miami got the top ranking.
- **Authors' analysis** (p. 72):
  - They do not fault going for the win rather than the tie. Given that Osborne would take the risk, he did it in the wrong order: he should try the two-pointer first. If it succeeds, then kick for one; if it fails, try a second two-pointer.
  - Down 14, Nebraska needed two touchdowns and three extra points.
  - If both attempts succeed, the order does not matter; nor does it matter if the one-point kick is missed but the two-point attempt succeeds (the game is tied). The difference arises only if the two-point attempt fails.
  - Under Osborne's plan, a failed two-pointer lost the game.
  - With the two-pointer first, a failure leaves 31–23. The next touchdown makes it 31–29, and a successful two-pointer then ties and wins the ranking.
- **Counterargument** (heard by the authors; they reject it) (p. 72):
  - After an early miss the team would play for a tie, with less inspiration.
  - The counterargument adds that a final all-or-nothing play would make the team rise to the occasion.
  - **The authors' reply:** a miss at the end loses outright, while an early miss still leaves a chance of a tie. Miami's defense would also rise to the occasion. If momentum matters, an early success helps score again, and it would allow a tie with two field goals.
- **Moral:** if you must take some risks, it is often better to take them as early as possible (tennis first serve; careers, investments, dating) (p. 73).
- More practice is in chapter 14 cases (p. 73).

## Toy example
(Our own example, not from the text.) A pile of 10 tokens. Players alternate; each takes 1 or 2 tokens; whoever takes the last token wins. Work back from the end. "W" means the player to move can force a win; "L" means the mover loses against correct play.
- 1 token: take 1 → W. 2 tokens: take 2 → W.
- 3 tokens: moving to 2 or 1 hands the opponent a W position → L.
- 4: take 1, leaving 3 (L for the opponent) → W. 5: take 2, leaving 3 → W.
- 6: moves lead to 5 or 4, both W for the opponent → L.
- 7: take 1 → 6 → W. 8: take 2 → 6 → W. 9: moves lead to 8 or 7 → L.
- 10: take 1, leaving 9 → W.

So the first player takes 1 and then restores a multiple of 3 each turn (leaving 9, 6, 3, 0). A player who is not looking ahead and takes 2 at the start (leaving 8) hands the win to the opponent. This is the same logic as 21-flags, with multiples of 3 instead of multiples of 4.

## Concepts
- [[backward-induction]] — Rule 1: look forward and reason backward from the end of the tree to choose the current move (p. 47)
- [[extensive-form game]] — a "game tree": the sequence of decisions, with different players moving at different branch points (p. 49)
- [[decision-tree-vs-game-tree]] (new) — decision tree: one decision maker; game tree: two or more players (p. 49)
- [[sequential-vs-simultaneous-moves]] (new) — players move in turn and see earlier moves, or move at once without seeing them (p. 46)
- [[zero-sum game & minimax]] — here only the notion: one player's gain is the other's loss; the authors stress that many games are not zero-sum (p. 52)
- [[credible commitment]] — only foreshadowed: making a promise believable, and the advantage of tying one's hands (pp. 52, 55)
- [[strategic-uncertainty]] (new) — uncertainty about other players' choices, as distinct from natural chance (p. 60)
- [[social preferences]] — fairness and altruism in players' objectives, shown by ultimatum and dictator play (pp. 63, 66)
- [[ultimatum-game-and-dictator-game]] (new) — take-it-or-leave-it split with rejection (ultimatum); split with no veto (dictator) (pp. 61, 63)
- [[normative-vs-positive-use-of-theory]] (new) — theory as advice about what to do versus as an explanation of what is observed (p. 60)

## Canonical instances
- [[charlie-brown-lucy-football]] — simplest game tree; forecast the other's known preference and decline (pp. 45, 50)
- [[fredo-investment-game]] — the same tree in business: trust without enforcement (pp. 50–52)
- [[line-item-veto-game]] — extra freedom hurts the president (pp. 53–55)
- [[survivor-21-flags]] — leave multiples of 4; players erred nearly everywhere (pp. 55–58)
- [[ultimatum-game-experiments]] — median offer 40–50%, low offers often rejected (pp. 61–65)
- [[dictator-game-shame-experiment]] — $9 exit option (p. 64)
- [[chess-complexity]] — about $10^{120}$ nodes; science plus art (pp. 68–70)
- [[orange-bowl-1984-two-point-conversion]] — take the risk first (pp. 71–73)

## Bridges (candidates)
- [same-math] Rule 1, backward reasoning ↔ decision-game-theory: backward induction / subgame-perfect equilibrium — same procedure on a finite tree with perfect information.
- [structural-analogy] Look-ahead plus judgment of positions in chess ↔ bounded rationality: searching only part of the problem and approximating the rest.
- [structural-analogy] Authors' evolutionary account of fairness norms ↔ evolution: group-level selection of cooperative norms. The authors call it speculation.
- [metaphor] Pruning the branch Lucy won't pick ↔ everyday forecasting: ignoring a logically possible but "realistically irrelevant" outcome.

## Questions this raises
- If a promise is not credible (Fredo), what devices make it credible? (The authors point to chapters 6 and 7.)
- How should one predict others' moves when moves are simultaneous and cannot be observed (chapter 3)?
- How much of ultimatum-game rejection is emotion, learned culture, or evolved norm? The authors say several causes may coexist.
- When looking only some moves ahead, how can one judge the value of a position without solving the game?

## Exercises worth doing
- Trip to the Gym No. 1 (p. 58) — flip the 21-flags objective (take the last flag and lose); re-derive the winning positions — difficulty: easy
- Quick Trip to the Gym: Reverse ultimatum game (p. 61) — predict how the game ends when each further offer must be more generous; compare with the plain ultimatum game — difficulty: medium

## Reading notes
- Printed page = pdf page (45–73). No offset.
- Figures (trees, the veto payoff table, the 21-flags table of actual versus correct moves) are not in the extracted text. Their contents here come from the surrounding prose.
- Asterisk footnotes (pp. 57, 62, 69, 72) and numbered endnotes are not included in the pages given. The Workouts answer to Trip to the Gym No. 1 is not in this unit either.
- The heading "Evolution of Altruism and Fairness" appears at the bottom of p. 65; its text starts on p. 66.
- The exact table of rating numbers for the veto game is not in the extracted text; I report only the ratings that the prose states (3 without veto; 2 with veto).
