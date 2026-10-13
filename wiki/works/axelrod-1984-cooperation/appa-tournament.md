---
id: axelrod-1984-cooperation/appa-tournament
work: axelrod-1984-cooperation
unit: Appendix A — Tournament Results
pages: 192-205
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
# Appendix A: Tournament Results

## L0 — One line
Five "representative" rules explain 96% of the variance in round-two scores, and TIT FOR TAT still wins five of six hypothetical tournaments in which one kind of opponent is made five times more common (second in the sixth), so its victory is robust.

## L1 — The gist (≤ 120 words)
This appendix supports chapter 2. It lists the contestants, the scores and the match results of the two rounds of the Computer Prisoner's Dilemma Tournament. The 63-by-63 score matrix of round two is too large to read. Stepwise regression (adding predictors one at a time) shows that a rule's scores against five rules predict its overall score very well. These five are then used to build six "what if" tournaments. TIT FOR TAT wins five and comes second in the sixth, where another rule wins. This matters because TIT FOR TAT's win holds up under very wide changes in the mix of opponents.

**Prerequisites:** averages; correlation (r) and r² as "share of variance explained"; the idea of a repeated Prisoner's Dilemma match scored by points.

## L2 — Key ideas
- Round one had 14 entries plus RANDOM, with five games of 200 moves per pair. Round two had 62 entries plus RANDOM, with five games per pair averaging 151 moves (pp. 192–193).
- The round-two matrix is shown in compressed form. Each pair's average score becomes one digit from 1 to 9, and 453 is exactly total mutual cooperation (p. 193, p. 196).
- Five representative rules predict a rule's tournament score with r = .979 and r² = .96, using a linear formula (p. 199).
- TIT FOR TAT scored 453, 453, 453, 452 and 446 with the five representatives, so it scored at or near the 453 of full mutual cooperation against each of them (p. 199).
- The first three representatives are nice (a term from chapter 2, not defined on these pages). All nice rules got 453 against them. Rules that were not nice generally did worse than TIT FOR TAT against them (p. 202).
- The best rule that was not nice (rank 8) did worse than TIT FOR TAT against every representative. It suffered most against REVISED STATE TRANSITION, which stops cooperating once its tolerance limit is reached (pp. 202–203).
- Each representative stands for a "constituency" (a large group of rules it represents), and the residuals form a sixth. Making any one of the six constituencies five times larger gives six hypothetical tournaments. Their scores still correlate .82 to .96 with the real ones (p. 204).
- TIT FOR TAT would still have come first in five of the six hypothetical tournaments. In the one exception, it would have been second: this happens when the REVISED STATE TRANSITION constituency is five times larger (pp. 204–205).

## L3 — Walkthrough

### Purpose and round one (pp. 192–194)
- The appendix gives information on the entrants, the entries and how each entry did against each other entry. It also tests six major variations of the tournament (p. 192).
- **Round one.** There were 14 entries plus RANDOM. Each pair played five games of 200 moves. Table 2 lists contestants (discipline, program length, score) and table 3 gives the pairwise scores. Strategy descriptions are in Axelrod (1980a), the report given to round-two entrants (pp. 192–193).
- Table 2: rank 1 is Anatol Rapoport at 504.5 (his rule appears in table 3 as TIT FOR TAT). Rank 2 is Tideman & Chieruzzi at 500.4, rank 8 is Davis at 471.8, and rank 15 is RANDOM at 276.3 (p. 193). The table shows a visible gap between rank 8 (471.8) and rank 9 (400.7). The author does not comment on it in this appendix.

### Round two: contestants and the score matrix (pp. 193–199)
- There were 62 entries plus RANDOM. Table 4 lists name, country, discipline, language (FORTRAN or BASIC) and program length. Length counts internal FORTRAN statements, with a conditional counted as two (pp. 195–196).
- Each pair played five games of varying length, averaging 151 moves. The matrix is 63 × 63, so table 5 shows each average score as one digit (pp. 193, 196):

| Digit | Points |
|---|---|
| 1 | < 100 |
| 2 | 100–199.9 (151 = total mutual defection) |
| 3 | 200–299.9 |
| 4 | 300–399.9 |
| 5 | 400–452.9 |
| 6 | exactly 453 (total mutual cooperation) |
| 7 | 453.1–499.9 |
| 8 | 500–599.9 |
| 9 | ≥ 600 |

- (added step) 453 = 3 × 151 points and 151 = 1 × 151 points, so these values correspond to 3 and 1 points per move over 151 moves. The page does not state the payoffs itself.
- Table 5 has too much detail to explain why rules scored as they did. The author wants a more parsimonious method (p. 197).

### Stepwise regression: five representatives (pp. 197, 199)
- Stepwise regression finds that five rules account very well for how a rule did against all 63. They represent the full set because a rule's scores against them predict its average score over the full set (p. 197).
- Predicted score (p. 199):

$$T = 120.0 + (.202)S_{6} + (.198)S_{30} + (.110)S_{35} + (.072)S_{46} + (.086)S_{27}$$

Here $T$ is the predicted tournament score and $S_j$ is the score the rule gets with the $j$th rule. Shapes: one number $T$ per rule, from five scalar inputs.
- The prediction correlates with actual scores at $r=.979$, and $r^2=.96$. So 96% of the variance in tournament scores is explained by performance with just these five (p. 199).
- TIT FOR TAT got $S_6=453$, $S_{30}=453$, $S_{35}=453$, $S_{46}=452$ and $S_{27}=446$. Its victory is explained by good scores with all five. Other rules are compared by how many points they lost relative to these numbers (pp. 199–200).

*Intuition note:* A giant table can be replaced by five opponents. If you know how a rule does against these five, you can guess its overall score closely. They stand in for whole groups of opponent types.

### Table 6 and what worked (pp. 200–203)
- Table 6 gives each rule's tournament score, its points lost relative to TIT FOR TAT against each representative (negative means it did better), and the **residual**, the actual score minus the predicted score. The five representatives are Rule 6, REVISED STATE TRANSITION (30), Rule 35, Tester (46) and Tranquilizer (pp. 200–201).
- Scores span several hundred points, but residuals are usually smaller than 10 points. Top-ranking rules tend to have the largest positive residuals, so they do better than most rules on aspects the five do not capture (p. 202).
- **Nice rules.** The first three representatives are themselves nice. Every nice rule got 453 with each of them, so none lost points relative to TIT FOR TAT. Rules that were not nice generally did worse than TIT FOR TAT with these three, shown by more positive than negative numbers in those columns (p. 202).
- **Example: Harrington's rule (rank 8, best rule that was not nice).**
  - It is a variant of TIT FOR TAT with a check for RANDOM, a way out of alternating defections ("echo effects"), and a test of what it can get away with (p. 202).
  - It always defects on move 37, and with rising probability after that. It stops random defecting if the other player defects immediately after one of these defections (p. 202).
  - It did worse than TIT FOR TAT with all five representatives, losing 1.0, 37.2, 16.6, 1.0 and 1.6 points (table 6, p. 200). It suffered most from REVISED STATE TRANSITION (37.2 points) (p. 203).
- **REVISED STATE TRANSITION** (Jonathan Pinkley) models the other player as a one-step Markov process. It chooses to maximize its own long-term payoff if the model is correct. As Harrington's rule defected more, it updated its running estimate of the probability that the other cooperates after each of the four possible outcomes. It first decided cooperation did not pay after being exploited, and soon after that it decided cooperation did not pay even after mutual cooperation (p. 203).
- Lesson in the author's words: even if another rule accepts some defections, once its tolerance limit is reached it is hard to convince it that one's ways have been mended. Some not-nice rules beat TIT FOR TAT against REVISED STATE TRANSITION, but they tended to do much worse against other representatives (p. 203).

*Intuition note:* Being nice costs nothing against nice rules. Tricks that exploit a trusting rule can backfire later, because a rule that models you may stop cooperating and be hard to win back (p. 203).

### Hypothetical tournaments (pp. 203–205)
- Each representative has a large constituency, the group of rules it stands for. Together with the unrepresented constituency of the residuals, these six constituencies fully account for each rule's performance (p. 203).
- A hypothetical tournament makes one constituency five times as large as it actually was. This gives six tournaments, each magnifying a different aspect of a rule's environment (p. 204).
- **Stability of the overall results.** If the residuals were five times as large, scores would still correlate .82 with the actual ones. If any of the five representatives' constituencies were five times larger, correlations would be .90 to .96. The author concludes the round-two results are quite robust (p. 204).
- **Stability of the winner.** TIT FOR TAT would still come first in five of the six hypothetical tournaments. The author calls this a very strong result because it holds under very wide variation in the environment (p. 204).
- **The one exception.** If the REVISED STATE TRANSITION constituency were five times as large, TIT FOR TAT would be second. First place would go to the rule of Robert Leyland (Auckland, New Zealand), which actually ranked 49th (p. 205).
  - Leyland's rule starts cooperatively and then sees how much it can get away with, like TRANQUILIZER (p. 205).
  - It ranked 49th mainly because it did poorly with the third representative and with TRANQUILIZER. It did 90 points better than TIT FOR TAT with REVISED STATE TRANSITION, which was "quite well taken in" by early cooperation (p. 205; table 6, p. 201 shows −90.0).
- Conclusion: TIT FOR TAT won five of six variants and was second in the sixth, so its victory was "very robust indeed" (p. 205).

*Intuition note:* The "what if" tournaments test whether the win depended on the actual mix of opponents. It mostly did not. In the one exception, a rule that did better than TIT FOR TAT against REVISED STATE TRANSITION would have won when that constituency is five times larger (p. 205).

## Toy example (ours, not from the text)
Invented numbers. Four opponent types: A (nice), B (nice), C (easily exploited), D (tough). The environment has 4 A's, 3 B's, 2 C's and 1 D (10 opponents). Average scores per match:

| | vs A | vs B | vs C | vs D |
|---|---|---|---|---|
| Rule T (cooperative, retaliates) | 450 | 450 | 250 | 200 |
| Rule E (exploiter) | 350 | 400 | 500 | 150 |

Original environment (counts 4, 3, 2, 1; total 10):
- T = (4·450 + 3·450 + 2·250 + 1·200)/10 = (1800 + 1350 + 500 + 200)/10 = 3850/10 = 385.
- E = (4·350 + 3·400 + 2·500 + 1·150)/10 = (1400 + 1200 + 1000 + 150)/10 = 3750/10 = 375.
- T wins.

Make C five times as common (counts 4, 3, 10, 1; total 18):
- T = (1800 + 1350 + 2500 + 200)/18 = 5850/18 = 325.
- E = (1400 + 1200 + 5000 + 150)/18 = 7750/18 ≈ 430.6.
- E wins.

Make A five times as common (counts 20, 3, 2, 1; total 26):
- T = (9000 + 1350 + 500 + 200)/26 = 11050/26 = 425.
- E = (7000 + 1200 + 1000 + 150)/26 = 9350/26 ≈ 359.6.
- T wins.

Reading: this has the same shape as the appendix's argument. A rule is robust if it keeps winning when one constituency is magnified. Here T would win 1 original plus 1 of 2 magnified versions, so it is not fully robust. TIT FOR TAT, per the author, won five of six.

Check of the regression formula (added step): with TIT FOR TAT's five scores, 120.0 + .202·453 + .198·453 + .110·453 + .072·452 + .086·446 = 120.0 + 91.506 + 89.694 + 49.830 + 32.544 + 38.356 = 421.93. Table 6 shows an actual score of 434.73 and a residual of 13.3. The difference between 434.73 − 421.93 = 12.8 and 13.3 is small. It may come from rounding of the printed coefficients (our guess).

## Concepts
- [[tit-for-tat]] (new) — the rule that won both rounds; its robustness is the appendix's topic (p. 192, p. 205)
- [[nice-rule]] (new) — term from chapter 2, not defined on these pages; here all nice rules got exactly 453 with each of the first three representatives (p. 202)
- [[representative-rules]] (new) — five rules whose scores predict a rule's average over all 63 (p. 197, p. 199)
- [[robustness-of-tournament-result]] (new) — result holds when the mix of opponent types is changed (p. 204, p. 205)
- [[repeated game & folk theorem]] — only the setting (repeated Prisoner's Dilemma); the folk theorem is not stated in this unit (p. 192)
- [[ecological rationality]] — canon link; not stated in this unit. The appendix varies the environment mix (p. 204)

## Canonical instances
- [[axelrod-tournament-round-one]] — 14 entries plus RANDOM, 200-move games; TIT FOR TAT first (pp. 192–194)
- [[axelrod-tournament-round-two]] — 62 entries plus RANDOM, 63 × 63 matrix, average game length 151 (pp. 193–199)
- [[revised-state-transition]] — Markov-model rule that stopped cooperating after enough defections (p. 203)
- [[harrington-rule]] — best not-nice rule, rank 8 (p. 202)
- [[leyland-rule]] — rank 49 actually, but first in the hypothetical tournament with REVISED STATE TRANSITION times five (p. 205)

## Bridges (candidates)
- [structural-analogy] five representatives chosen by stepwise regression ↔ statistics: feature selection to reduce dimension — a few predictors summarize many opponents.
- [structural-analogy] reweighting opponent constituencies ↔ evolutionary game theory: changing population shares of strategies (replicator dynamics) — the same idea of an environment's composition, but the appendix does no dynamics.
- [metaphor] one rule's weakness exposed when its worst opponent type becomes common ↔ ecological rationality: fit to environment.

## Questions this raises
- The hypothetical tournaments only reweight rules that were actually submitted. Would TIT FOR TAT still win against rules nobody entered?
- Is a regression with five predictors fitted on the same data it explains a fair test? (The appendix does not discuss this.)
- Why did REVISED STATE TRANSITION's weakness lead to exploitation by Leyland's rule? Could TIT FOR TAT be changed to beat both?
- Do the "nice" results also hold when game length or noise changes?

## Reading notes
- Printed = pdf − 2.
- Footnote markers 1 and 2 appear on pp. 203–204. Their note texts are not on the pages supplied.
- Table 6 column header gives Tranquilizer as "(21)" on p. 200 and "(27)" on p. 201. The regression formula on p. 199 uses $S_{27}$ for the fifth rule.
- Table 6, rank 10 shows a score of 425.94, which is higher than rank 9 (425.07). Rank order and score disagree, probably a misprint (image checked).
- The text says "fourty-ninth" (p. 205). This is a typo.
- Table 3 is printed rotated (p. 194). Its average column matches table 2 (rounded), and no individual cell values from table 3 are quoted here. Table 5 digits were not decoded individually.
- Table 4's "Length of Program" note says length is counted in internal FORTRAN statements, and a conditional counts as two here but as one in the first-round report (p. 196).
