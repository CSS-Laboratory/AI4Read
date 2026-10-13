---
id: axelrod-1984-cooperation/appb-proofs
work: axelrod-1984-cooperation
unit: Appendix B — Proofs of the Theoretical Propositions
pages: 206-215
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Appendix B — Proofs of the Theoretical Propositions

## L0 — One line
In the repeated Prisoner's Dilemma, whether a strategy resists invasion depends on how much the future matters and on whether newcomers arrive alone or in groups.

## L1 — The gist (≤ 120 words)
This appendix gives the mathematics behind Axelrod's claims about the repeated Prisoner's Dilemma, a game where each round tempts players to defect. It states eight propositions and a theorem. The strategy that cooperates first and then copies the other player's last move is stable against every invader exactly when future payoffs weigh enough. A strategy that always defects is stable whatever the payoffs. In a world of always-defectors, cooperation can start if newcomers arrive in groups that meet each other often enough. Nice strategies (those that never defect first) resist such groups better than other strategies do. Stability against single invaders also gives stability in neighbour-based territories, if they are not too highly interconnected.

**Prerequisites:** geometric series; solving linear inequalities; weighted averages; the Prisoner's Dilemma payoffs T > R > P > S.

## L2 — Key ideas
- **Setup.** Payoffs satisfy T > R > P > S and R > (T+S)/2. Each later move is worth a factor w less (0 < w < 1). A strategy "invades" B if V(A|B) > V(B|B). B is "collectively stable" if nothing can invade it. TIT FOR TAT (TFT) cooperates first, then copies the other's previous move. ALL D always defects (setup pp. 206–207; ALL D is defined on p. 211).
- **Prop. 2.** TFT is collectively stable if and only if w ≥ max{(T−R)/(T−P), (T−R)/(R−S)}. It suffices to check two invaders: ALL D and strict alternation of D and C (pp. 207–209).
- **Characterization Theorem.** B is collectively stable iff B defects whenever the other player's score so far is too high. Hence there are typically many collectively stable strategies, and nice rules have the most flexibility (pp. 209–210).
- **Props. 3–4.** Any strategy that may cooperate first can be collectively stable only if w is large enough. A nice strategy can be collectively stable only if it is provoked by the other's very first defection (pp. 210–211).
- **Prop. 5 and clusters.** ALL D is always collectively stable, so single newcomers cannot dislodge it. A "p-cluster" (newcomers who share a proportion p of their interactions) can invade. With T=5, R=3, P=1, S=0 and w=.9, a TFT cluster invades ALL D with 5% in-cluster interaction (pp. 211–212).
- **Random mixing.** With completely random mixing, TFT invading ALL D at the standard payoffs needs a newcomer share q > 1/17 (p. 213).
- **Prop. 6.** The strategies that invade ALL D with the smallest p are "maximally discriminating": they eventually cooperate first, cooperate with ALL D only once, and always cooperate with their own kind. TFT is one (pp. 213–214).
- **Prop. 7.** A nice strategy that no single individual can invade cannot be invaded by any cluster (p. 214).
- **Prop. 8.** Collectively stable implies territorially stable (stable on a map where players meet only neighbours). The proof is for a rectangular grid and generalizes to systems that are not too highly interconnected (p. 215).

## L3 — Walkthrough

### Definitions (pp. 206–207)
- Prisoner's Dilemma: each player chooses C or D. Both C: each gets R. Both D: each gets P. One C, one D: the cooperator gets S (sucker), the defector gets T (temptation). T > R > P > S and R > (T+S)/2 (pp. 206–207).
- In the iterated game each move is worth a factor w less than the one before. Two players who always cooperate with each other get
$$R + wR + w^2R + \dots = \frac{R}{1-w}. $$ (p. 207)
- A strategy maps the whole history so far to a probability of cooperating now. TFT is certain to cooperate on move 1, then does what the other did on the previous move (p. 207).
- V(A|B) is the score of A against B. A invades a population of B if V(A|B) > V(B|B). B is collectively stable if no strategy can invade it (p. 207).

### Proposition 1 (p. 207)
If w is sufficiently high, there is no best strategy independent of the other player's strategy. The proof is in chapter 1, not in this appendix (p. 207).

### Proposition 2 (pp. 207–209)
**Claim.** TFT is collectively stable iff $w \ge \max\{(T-R)/(T-P),\ (T-R)/(R-S)\}$ (p. 207).

**Step 1: equivalent form.** The claim is equivalent to: TFT is invadable neither by ALL D nor by the strategy that alternates D and C (p. 208).
- ALL D gets T on move 1 and P afterwards: $V(\text{ALL D}|\text{TFT}) = T + wP/(1-w)$. TFT with its twin gets $V(\text{TFT}|\text{TFT}) = R/(1-w)$ (p. 208).
- ALL D cannot invade iff
$$T + \frac{wP}{1-w} \le \frac{R}{1-w} \iff T(1-w)+wP \le R \iff T-R \le w(T-P) \iff w \ge \frac{T-R}{T-P}.$$ (p. 208)
- Alternation cannot invade iff $(T+wS)/(1-w^2) \le R/(1-w)$, i.e. $(T-R)/(R-S) \le w$ (p. 208). (added step) Multiply by $1-w^2$: $T+wS \le R(1+w)$, so $T-R \le w(R-S)$.
- So the two conditions together are the same as the two invasion-proofs, which shows the two formulations are equivalent (p. 208).

**Step 2: both implications of the second form.**
- If TFT is collectively stable, no rule can invade, so neither can these two (p. 208).
- Conversely, TFT has only two states, set by the other player's previous move (on move 1 it acts as if the other had just cooperated). So against TFT, A's best continuation after each of its own choices is C or D. That leaves four possibilities for A's best play: repeated sequences CC, CD, DC, or DD (pp. 208–209).
- The first does what TFT does with another TFT. The second cannot do better than both the first and the third. The third and fourth are equivalent to alternation and to ALL D. So if those two cannot invade, no rule can (p. 209).

*Intuition note.* TFT retaliates after a defection, but this deters an invader only when w is at or above the thresholds, i.e. when the future is worth enough that a one-time gain T does not pay (our reading of the thresholds). Two simple deviations (always defect; defect every other move) are the only ones that need checking.

### Secure position and the Characterization Theorem (pp. 209–210)
- Idea: invasion is prevented if the common rule makes the invader worse off than following the common strategy (p. 209).
- **Definition.** B has a *secure position* over A on move n if, no matter what A does from move n on, V(A|B) < V(B|B), assuming B defects from move n on (p. 209).
- With $V_n(A|B)$ = A's discounted cumulative score before move n, this is equivalent to
$$V_n(A|B) + \frac{w^{n-1}P}{1-w} < V(B|B),$$
since the best A can do from move n on, if B defects, is P each time (p. 209).
- **Characterization Theorem.** B is collectively stable iff B defects on move n whenever the other player's cumulative score is too great, i.e. when
$$V_n(A|B) > V(B|B) - w^{n-1}\Big[T + \frac{wP}{1-w}\Big].$$
The proof is in Axelrod (1981), not in these pages (pp. 209–210).
- (added step) The bracket is the most A could get from move n on if B cooperates on move n and defects afterwards.
- The condition is both necessary and sufficient, so it is a complete characterization (p. 210).
- Two consequences. (1) While the other's score is not too high, B may cooperate or defect and stay collectively stable. This flexibility explains why there are typically many collectively stable strategies. (2) A nice rule (never defects first) has the most flexibility, because it scores the highest possible against an identical rule. Nice rules can be more generous because they do so well with each other (p. 210).

*Intuition note.* The advice is to cooperate only when you can afford being exploited and still keep your secure position (p. 209). A nice rule has a big score "cushion" against its own kind, so it can afford to be generous.

### Proposition 3 (pp. 210–211)
**Claim.** Any strategy B that may be the first to cooperate can be collectively stable only when w is sufficiently large (p. 210).

**Proof.**
- If B cooperates on move 1, $V(\text{ALL D}|B) \ge T + wP/(1-w)$. For any B, $R/(1-w) \ge V(B|B)$, because R is the best B can get with another B (since R > P and R > (S+T)/2) (pp. 210–211).
- So $V(\text{ALL D}|B) > V(B|B)$ whenever $T + wP/(1-w) > R/(1-w)$. That means ALL D invades a B that cooperates on move 1 whenever $w < (T-R)/(T-P)$ (p. 211).
- If B has a positive chance of cooperating on move 1, ALL D's gain over $V_1(B|B)$ can be cancelled only if w is sufficiently large (p. 211).
- Likewise, if B will not be the first to cooperate until move n, then $V_n(\text{ALL D}|B) = V_n(B|B)$, and the gain of $V_{n+1}(\text{ALL D}|B)$ over $V_{n+1}(B|B)$ can be cancelled only if w is sufficiently large (p. 211).

### Proposition 4 (p. 211)
**Claim.** A nice strategy can be collectively stable only if it is provoked by the other's very first defection. So on some later move it must have a finite chance of defecting back (p. 211).
**Proof.** If it were not provoked by a defection on move n, a rule that defected only on move n could invade it (p. 211).

### Proposition 5 (pp. 211–212)
**Claim.** ALL D is always collectively stable, whatever w, T, R, P, S. **Proof:** it always defects, so it meets the Characterization Theorem's requirement of defecting whenever required (pp. 211–212).

*Intuition note.* A world of "meanies" resists invaders who arrive one at a time. For cooperation to get going, newcomers must arrive in clusters (p. 212).

### Clusters and mixing (pp. 212–213)
- Clustering: if new A's are rare relative to established B's, clustering lets the A's be a significant part of each other's environment but a negligible part of the B's. A **p-cluster of A invades B** if, as the text prints it, $pV(A|A) + (1-p)V(B|B) > V(B|B)$, where p is the proportion of an A-player's interactions that are with other A's. (Misprint? p. 214 uses $V(A|B)$ in the second term; see Reading notes.) Solving for p, invasion is possible if the newcomers interact enough with each other (p. 212).
- This assumes non-random pairing. With random pairing an A would rarely meet another A (p. 212).
- Example (chapter 3 numbers): T=5, R=3, P=1, S=0, w=.9. A cluster of TFTs can invade a population of meanies (ALL D) even if only 5 percent of their interactions are with other cluster members (p. 212).
- If newcomers grow in share, their need to avoid random mixing declines. With completely random mixing and newcomer share q, the newcomers do better than natives when
$$qV(A|A) + (1-q)V(A|B) > qV(B|A) + (1-q)V(B|B).$$
For TFT invading ALL D with the standard payoffs, this gives q > 1/17 (pp. 212–213).
- Story: a negligible cluster gets established if its members have even a small chance p of meeting. Once it thrives it depends less on non-random mixing. When it is a few percent of the population, it thrives even with completely random mixing (p. 213).

### Proposition 6 (pp. 213–214)
- **Maximally discriminating:** the strategy will eventually cooperate even if the other has never cooperated yet; once it cooperates it never cooperates again with ALL D; and it always cooperates with another player of the same strategy (p. 213).
- **Claim.** The strategies that can invade ALL D in a cluster with the smallest p are the maximally discriminating ones, such as TFT (p. 213).
- **Proof.**
  - To invade ALL D, a rule needs a positive chance of cooperating first. Stochastic cooperation with one's own kind is worse than deterministic cooperation, since it gives equal chances of S and T and (S+T)/2 < R. So the best invader must cooperate first on some move n even if the other has never cooperated (pp. 213–214).
  - With B = ALL D, the invaders with the lowest p are those with the lowest
$$p^* = \frac{V(B|B) - V(A|B)}{V(A|A) - V(A|B)}.$$
 (added step) This follows from $pV(A|A) + (1-p)V(A|B) > V(B|B)$ by rearranging, and the denominator is positive when $V(A|A) > V(B|B) > V(A|B)$.
  - $p^*$ is smallest when $V(A|A)$ and $V(A|B)$ are maximized (subject to A first cooperating on move n), since $V(A|A) > V(B|B) > V(A|B)$. They are maximized iff A is maximally discriminating. When A starts to cooperate does not matter for the minimal p (p. 214).
  - TFT qualifies: it cooperates on move 1, cooperates only once with ALL D, and always cooperates with another TFT (p. 214).

### Proposition 7 (p. 214)
**Claim.** If a nice strategy cannot be invaded by a single individual, it cannot be invaded by any cluster (p. 214).
**Proof.** A cluster of A invades B only if some $p \le 1$ gives $pV(A|A) + (1-p)V(A|B) > V(B|B)$. If B is nice, $V(A|A) \le V(B|B)$, because $V(B|B) = R/(1-w)$ is the largest value attainable against a same-strategy player, as R > (S+T)/2. So A can invade as a cluster only if $V(A|B) > V(B|B)$, which is the same as invading as an individual (p. 214). (added step) If both $V(A|A)$ and $V(A|B)$ were at most $V(B|B)$, the weighted average could not exceed it.

### Proposition 8 (p. 215)
- **Territorial system:** players interact only with neighbours. Each generation, a player's success score is the average of its performance with its neighbours. If one or more neighbours are more successful, the player converts to the strategy of the most successful (random choice among ties) (pp. 214–215).
- A single A placed in a population of B **territorially invades** B if every location eventually converts to A. B is **territorially stable** if no strategy can territorially invade it (p. 215).
- **Claim.** If a rule is collectively stable, it is territorially stable (p. 215).
- The proof is in chapter 8 for a rectangular grid. It generalizes to any system that is not too highly interconnected: for every point there is a neighbour of a neighbour that is not a neighbour of the original point (p. 215).
- Implication: protection from invasion is at least as easy in a territorial system as in a freely mixing one. Mutual cooperation can be sustained in a (not too highly connected) territorial system at least as easily as in a freely mixing one (p. 215).

## Toy example (ours, not from the text)
Use T=5, R=3, P=1, S=0.
- Prop. 2 threshold: (T−R)/(T−P) = 2/4 = 0.5; (T−R)/(R−S) = 2/3. The maximum is 2/3.
- Take w = 0.5 (below 2/3). V(TFT|TFT) = 3/(1−0.5) = 6. V(ALL D|TFT) = 5 + 0.5·1/0.5 = 6 (no gain). Alternation: (5 + 0.5·0)/(1 − 0.25) = 5/0.75 ≈ 6.67 > 6. So alternation invades; TFT is not collectively stable at w = 0.5.
- Take w = 2/3. V(TFT|TFT) = 3/(1/3) = 9. Alternation: 5/(1 − 4/9) = 5/(5/9) = 9, so it ties and does not invade. ALL D: 5 + (2/3)·1/(1/3) = 7 < 9. So TFT is collectively stable, exactly at the threshold.
- Random mixing check (with w = .9, which reproduces the text's 1/17; the text does not state w there): V(TFT|TFT) = 30, V(TFT|ALL D) = 0 + .9/.1 = 9, V(ALL D|TFT) = 5 + 9 = 14, V(ALL D|ALL D) = 10. Condition: 30q + 9(1−q) > 14q + 10(1−q), i.e. 9 + 21q > 10 + 4q, so q > 1/17.

## Concepts
- [[collectively-stable-strategy]] (new) — no strategy B′ has V(B′|B) > V(B|B); close to, but defined here by this inequality, not the canon's ESS (p. 207)
- [[evolutionarily-stable-strategy]] — nearest canon concept to collective stability; the text does not use the term (p. 207)
- [[shadow-of-the-future]] — here the discount parameter w; many results hold only if w is large enough (p. 207)
- [[tit-for-tat]] (new) — cooperate first, then copy the other's previous move (p. 207)
- [[all-d]] (new) — always defect (pp. 208, 211)
- [[nice-strategy]] (new) — never the first to defect (p. 210)
- [[secure-position]] (new) — B can hold A's total below V(B|B) by defecting from move n on (p. 209)
- [[characterization-theorem]] (new) — B is collectively stable iff it defects when the other's score is too high (pp. 209–210)
- [[cluster-invasion]] (new) — a p-cluster of A invades B; p is A's share of interactions with other A's (p. 212)
- [[maximally-discriminating-strategy]] (new) — cooperates eventually, once with ALL D, always with its own kind (p. 213)
- [[territorial-stability]] (new) — no strategy converts every location of a neighbour-based territory (p. 215)

## Canonical instances
- [[iterated-prisoners-dilemma]] (new) — the game with discount factor w (pp. 206–207)
- [[tft-vs-all-d-example]] (new) — T=5, R=3, P=1, S=0; w=.9 gives p about 5%; q > 1/17 (pp. 212–213)

## Bridges (candidates)
- [structural-analogy] collectively stable strategy ↔ evolutionary game theory: evolutionarily stable strategy — both ask whether a rare invader does better than the incumbent.
- [structural-analogy] p-cluster invasion ↔ non-random (assortative) interaction in evolutionary models — newcomers meet their own kind more than chance predicts.
- [structural-analogy] territorial stability (Prop. 8) ↔ network reciprocity — cooperation sustained by local interaction structure.
- [metaphor] w, the weight on later moves ↔ shadow of the future — the same idea in discounted form.

## Questions this raises
- What does the Characterization Theorem's proof (Axelrod 1981, not given here) look like?
- How does the 5% cluster size change for other values of w or other payoffs?
- Which graphs count as "too highly interconnected" for Prop. 8, and does the result fail for them?
- What happens when strategies can make errors or the other player's moves are misperceived? (This appendix does not discuss it.)

## Reading notes
- Printed page = pdf page − 2 (pdf 208 = printed 206).
- Page images were given only for printed pp. 206, 208, 211 and 214. Elsewhere only the text layer was available.
- On printed pp. 208, 211 and 214 the text layer shows "<" or ">" where the images show ≤ or ≥ (e.g. $V(\text{ALL D}|\text{TFT}) \le V(\text{TFT}|\text{TFT})$, $w \ge$ the thresholds, $p \le 1$, $V(A|A) \le V(B|B)$ in Prop. 7). I followed the images.
- p. 208: "the best which any strategy, A, can do after choosing D is to choose C or D. Similarly, the best A can do after choosing D…" prints D twice. The first D is presumably C, since the four cases are CC, CD, DC, DD (inference).
- p. 212 (text layer only): the definition of a p-cluster invasion prints $pV(A|A) + (1-p)V(B|B) > V(B|B)$. The proof of Prop. 6/7 (p. 214) uses $V(A|B)$ in the second term, which also fits the $p^*$ formula. The text layer's $V(B|B)$ is probably a misprint, but I could not check the image.
- p. 213 says "q percent newcomers" but the inequality treats q as a proportion (1/17).
- A footnote marker "1" appears on p. 210. The footnote text is not in these pages.
- The Prisoner's Dilemma figure is cited as "figure 1 of chapter 1 (see page 8)" and is not in this unit.
