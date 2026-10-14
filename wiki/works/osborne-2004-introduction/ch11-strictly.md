---
id: osborne-2004-introduction/ch11-strictly
work: osborne-2004-introduction
unit: "11 Strictly Competitive Games and Maxminimization"
pages: 335–348
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Strictly Competitive Games and Maxminimization

## L0 — One line
In a two-player game where the players' interests are exactly opposed, playing the cautious maxminimizing strategy is the same thing as playing a Nash equilibrium strategy (when an equilibrium exists).

## L1 — The gist (≤ 120 words)
Nash equilibrium assumes players know what the others do. This chapter instead asks what a player should do if she forms beliefs from her analysis of the game, not from experience. A cautious answer is maxminimization: choose the strategy whose worst-case payoff is highest. In any game, an equilibrium payoff is at least the maxminimized payoff. In strictly competitive games (two players with exactly opposed preferences, also called zero-sum) that have an equilibrium, the two coincide. Equilibria then have equal payoffs, can be mixed and matched, and each equilibrium strategy guarantees the value of the game (the common max-min and min-max payoff). Examples include the card game le Her. Laboratory evidence (O'Neill's experiment) tends not to support maxminimization.

**Prerequisites:** Nash equilibrium; mixed strategies and expected (vNM) payoffs; max/min notation; solving two linear equations; basic probability.

## L2 — Key ideas (5–10 bullets)
- **Maxminimization** picks the strategy with the highest worst-case payoff, assuming opponents act to hurt you. A mixed strategy can guarantee more than any pure one (pp. 335–337).
- In **any** game, a player's Nash equilibrium payoff is at least her maxminimized payoff (Lemma 338.1, p. 338).
- A game is **strictly competitive** if the two players' preferences are exactly reversed. Such games can be represented with payoffs summing to zero. Strictly competitive in pure strategies does not imply it with mixed strategies (pp. 338–340).
- **Proposition 341.1:** in a strictly competitive game, a pair is a Nash equilibrium if and only if both strategies are maxminimizers and max-min equals min-max (p. 341).
- Consequences: all equilibria give the same payoffs, equilibria are interchangeable, and equilibrium strategies guarantee the **value** of the game. BoS shows the first two can fail without strict competition, and the author says the third can fail too (Ex. 343.2) (pp. 342–343).
- Historically, in a letter dated 1713 Waldegrave found the mixed maxminimizers of a reduced 2×2 version of le Her (pp. 344–346).
- In a non-strictly-competitive game, a maxminimizer can guarantee the equilibrium payoff while the equilibrium strategy does not (Example 346.1, p. 346).
- In O'Neill's experiment, minmax behaviour is rejected statistically even though frequencies look close. Evidence so far tends not to support the theory (pp. 347–348).

## L3 — Walkthrough

### 11.1 Introduction (p. 335)
Nash equilibrium models a steady state. Each player knows from experience what the others will do (p. 335). This chapter instead studies players who form beliefs about others' actions from analysis of the game (p. 335). The focus is on two-player strictly competitive games, where interests are diametrically opposed. There a simple decision procedure leads each player to a Nash equilibrium action (p. 335).

### 11.2 Definitions and examples

**Maxminimization.** Assume the worst: whatever you do, opponents take the action worst for you. For each of your actions, find the lowest payoff over the others' actions. Then choose the action whose lowest payoff is largest (p. 335). The author works with vNM payoffs, though the idea does not need randomizing (p. 335). For a mixed strategy $\alpha_i$, the lowest payoff is $\min_{\alpha_{-i}} U_i(\alpha_i,\alpha_{-i})$ (pp. 335–336).

**Definition 336.1.** A *maxminimizing mixed strategy* for player $i$ is a mixed strategy $\alpha_i^*$ that solves
$$\max_{\alpha_i}\ \min_{\alpha_{-i}}\ U_i(\alpha_i,\alpha_{-i}).$$
This maximizes her payoff under the pessimistic assumption that others minimize it (p. 336).

**Guarantee.** A mixed strategy $\alpha_i$ *guarantees* player $i$ the payoff $\underline u_i$ if $u_i(\alpha_i,\alpha_{-i})\ge \underline u_i$ for every list $\alpha_{-i}$ of the others' mixed strategies (p. 336). (The source's page image prints this payoff with an overline; I write $\underline u_i$ for "the guaranteed level".) A maxminimizer $\alpha_i^*$ maximizes the payoff one can guarantee:
$$\min_{\alpha_{-i}} u_i(\alpha_i^*,\alpha_{-i}) \ge \min_{\alpha_{-i}} u_i(\alpha_i,\alpha_{-i})\quad\text{for every }\alpha_i.$$

**Example 336.2 (bargaining game, pure strategies; game of Exercise 36.2, not in these pages).** Demanding $x\le 5$ gives exactly $x$. Demanding $6$ gives $6$ or at worst $5$. Demanding $x\ge7$ gives $x$ or at worst $11-x$ (p. 336). Figure 337.1 lists the smallest amount obtained (p. 337):

| Demand | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Worst case | 0 | 1 | 2 | 3 | 4 | 5 | 5 | 4 | 3 | 2 | 1 |

Maxminimization leads each player to demand $5 or $6 (worst case $5) (p. 336).

**Why assume the opponent minimizes your payoff?** In some games that is not sensible. With one opponent whose interests are diametrically opposed (a strictly competitive game) it may be reasonable. In such games the maxminimizing outcome is closely related to the Nash equilibrium outcome. A maxminimizing action also maximizes the payoff you can guarantee (pp. 336–337).

**Example 337.1.** Game of Figure 337.2 (player 1 chooses the row, payoffs listed as player 1, player 2) (p. 337):

| | L | R |
|---|---|---|
| T | 2, −2 | −1, 1 |
| B | −1, 1 | 1, −1 |

With pure strategies, T's worst case is $-1$ (player 2 plays R). B's worst case is $-1$ (player 2 plays L). So both guarantee $-1$ (p. 337). Let $p$ be the probability of T. Player 1's expected payoff against L is $2p-(1-p)=3p-1$. Against R it is $-p+(1-p)=1-2p$ (added step: computed from the matrix). Her payoff against any mixed strategy of player 2 lies above the lower of these two lines. The lowest payoff for each $p$ is the "heavy inverted V" in Figure 338.1. Its peak is where the lines cross: $3p-1=1-2p$ gives $p=\tfrac25$ (added step), with payoff $\tfrac15$ (pp. 337–338). This maxminimizer gives player 1 the same payoff whether player 2 plays L or R. That is different from Nash equilibrium indifference, where player 1's mixed strategy makes *player 2* indifferent (p. 337).

*Intuition note.* Randomizing can lift the worst case. In this example the best mix is the one where the opponent's two replies hurt you equally.

**Lemma 338.1.** In any strategic game, each player's payoff in any Nash equilibrium is at least her maxminimized payoff (p. 338).
*Proof (player 1).* Let $(\alpha_1^*,\alpha_2^*)$ be a Nash equilibrium. Then $U_1(\alpha_1^*,\alpha_2^*)\ge U_1(\alpha_1,\alpha_2^*)$ for every $\alpha_1$. Hence $U_1(\alpha_1^*,\alpha_2^*)\ge \min_{\alpha_2}U_1(\alpha_1,\alpha_2)$ for every $\alpha_1$. Since this holds for every $\alpha_1$, $U_1(\alpha_1^*,\alpha_2^*)\ge\max_{\alpha_1}\min_{\alpha_2}U_1(\alpha_1,\alpha_2)$ (p. 338).

*Intuition note.* An equilibrium strategy is a best reply to the other's equilibrium strategy. Its payoff there is at least what any strategy of hers gets in the worst case, hence at least the maxmin payoff.

### 11.3 Strictly competitive games

A strictly competitive game has two players whose preferences are diametrically opposed: whenever one prefers an outcome $a$ to $b$, the other prefers $b$ to $a$ (p. 338). For pure strategies:

**Definition 339.1 (ordinal).** A strategic game with ordinal preferences is *strictly competitive* if it has two players and $(a_1,a_2)\succsim_1(b_1,b_2)$ if and only if $(b_1,b_2)\succsim_2(a_1,a_2)$ (p. 339). It follows that indifference is shared, and that strict preference of one player is reversed for the other (p. 339). Payoffs can be chosen to sum to zero at every profile: give 0 to both for player 1's worst outcome, 1 and $-1$ for the next worst, and so on. For this reason such a game is sometimes called *zerosum* (p. 339).

**Examples (p. 339).** The Prisoner's Dilemma is not strictly competitive, because both prefer (Quiet, Quiet) to (Fink, Fink). BoS is not, because both prefer $(B,B)$ to $(S,B)$. Matching Pennies is. The game of Figure 339.1 is strictly competitive in pure strategies:

| | L | R |
|---|---|---|
| T | 2, 1 | 0, 5 |
| B | 1, 3 | 5, 0 |

Player 1 ranks $(B,R)\succ(T,L)\succ(B,L)\succ(T,R)$, and player 2 ranks them in exactly the reverse order (p. 339).

**Definition 339.2 (vNM).** A strategic game with vNM preferences is strictly competitive if it has two players and $U_1(\alpha_1,\alpha_2)\ge U_1(\beta_1,\beta_2)$ if and only if $U_2(\beta_1,\beta_2)\ge U_2(\alpha_1,\alpha_2)$, for pairs of mixed strategies (p. 339).

**Zero-sum representation with mixed strategies (p. 340).** Let $\overline a$ and $\underline a$ be player 1's best and worst outcomes. Choose representations with $v_1(\overline a)=1$, $v_1(\underline a)=0$, $v_2(\overline a)=-1$, $v_2(\underline a)=0$. The author asks why this is possible, and leaves it as a question. For any outcome $a$, let $p=u_1(a)$. Then $u_1(a)=p\,u_1(\overline a)+(1-p)\,u_1(\underline a)$. Since the game is strictly competitive, $u_2(a)=p\,u_2(\underline a)+(1-p)\,u_2(\overline a)=-p$. So $u_1(a)+u_2(a)=0$. Hence, if player 2's preferences are not represented by $-u_1$, the game is not strictly competitive (p. 340).

A game strictly competitive with mixed strategies is clearly strictly competitive in pure strategies, but not conversely (p. 340). In Figure 339.1 read as vNM payoffs, player 1 is indifferent between $(T,L)$ and the lottery with $(T,R)$ at probability $\tfrac35$ and $(B,R)$ at $\tfrac25$, since $\tfrac35\cdot0+\tfrac25\cdot5=2$. Player 2 is not indifferent: she gets 1 from $(T,L)$ and $\tfrac35\cdot5+\tfrac25\cdot0=3$ from the lottery (p. 340).

**A tool.** Since $\max_x f(x)=-\min_x(-f(x))$, with $U_2=-U_1$ (assumed without loss of generality):
$$\max_{\alpha_2}\min_{\alpha_1}U_2(\alpha_1,\alpha_2)=\max_{\alpha_2}\min_{\alpha_1}(-U_1(\alpha_1,\alpha_2))=\max_{\alpha_2}\bigl(-\max_{\alpha_1}U_1(\alpha_1,\alpha_2)\bigr)$$
$$\max_{\alpha_2}\min_{\alpha_1}U_2(\alpha_1,\alpha_2)=-\min_{\alpha_2}\max_{\alpha_1}U_1(\alpha_1,\alpha_2).\tag{340.2}$$
The last step again uses $\max_x(-g)=-\min_x g$ (added step) (p. 340).

**Proposition 341.1.** Consider a strictly competitive strategic game with vNM preferences (p. 341).
- **(a)** If $(\alpha_1^*,\alpha_2^*)$ is a Nash equilibrium, then $\alpha_1^*$ is a maxminimizer for player 1 and $\alpha_2^*$ is one for player 2. Moreover $\max_{\alpha_1}\min_{\alpha_2}U_1=\min_{\alpha_2}\max_{\alpha_1}U_1=U_1(\alpha_1^*,\alpha_2^*)$.
- **(b)** If $\alpha_1^*$ and $\alpha_2^*$ are maxminimizers for players 1 and 2, and $\max_{\alpha_1}\min_{\alpha_2}U_1=\min_{\alpha_2}\max_{\alpha_1}U_1$ (in particular if a Nash equilibrium exists, by (a)), then $(\alpha_1^*,\alpha_2^*)$ is a Nash equilibrium.

*Proof of (a)* (p. 341). Equilibrium gives $U_2(\alpha_1^*,\alpha_2^*)\ge U_2(\alpha_1^*,\alpha_2)$ for all $\alpha_2$. Since $U_2=-U_1$, $U_1(\alpha_1^*,\alpha_2^*)\le U_1(\alpha_1^*,\alpha_2)$ for all $\alpha_2$. So $U_1(\alpha_1^*,\alpha_2^*)=\min_{\alpha_2}U_1(\alpha_1^*,\alpha_2)$. The right side is evaluated at one particular $\alpha_1^*$, so it is at most the maximum over $\alpha_1$:
$$U_1(\alpha_1^*,\alpha_2^*)\le\max_{\alpha_1}\min_{\alpha_2}U_1(\alpha_1,\alpha_2).$$
Lemma 338.1 gives the opposite inequality, so equality holds and $\alpha_1^*$ is a maxminimizer. The same argument for player 2 gives $U_2(\alpha_1^*,\alpha_2^*)=\max_{\alpha_2}\min_{\alpha_1}U_2$. By (340.2), $U_1(\alpha_1^*,\alpha_2^*)=\min_{\alpha_2}\max_{\alpha_1}U_1$.

*Proof of (b)* (pp. 341–342). Let $v^*=\max_{\alpha_1}\min_{\alpha_2}U_1=\min_{\alpha_2}\max_{\alpha_1}U_1$. By (340.2), $\max_{\alpha_2}\min_{\alpha_1}U_2=-v^*$. Because $\alpha_1^*$ is a maxminimizer, $U_1(\alpha_1^*,\alpha_2)\ge v^*$ for all $\alpha_2$. Because $\alpha_2^*$ is one, $U_2(\alpha_1,\alpha_2^*)\ge -v^*$ for all $\alpha_1$. Setting $\alpha_2=\alpha_2^*$ and $\alpha_1=\alpha_1^*$ gives $U_1(\alpha_1^*,\alpha_2^*)\ge v^*$ and $U_2(\alpha_1^*,\alpha_2^*)\ge -v^*$, i.e. $U_1(\alpha_1^*,\alpha_2^*)\le v^*$. So $U_1(\alpha_1^*,\alpha_2^*)=v^*$. Then:
- $U_1(\alpha_1^*,\alpha_2)\ge U_1(\alpha_1^*,\alpha_2^*)$ for all $\alpha_2$, i.e. $U_2(\alpha_1^*,\alpha_2)\le U_2(\alpha_1^*,\alpha_2^*)$.
- $U_2(\alpha_1,\alpha_2^*)\ge U_2(\alpha_1^*,\alpha_2^*)$ for all $\alpha_1$, i.e. $U_1(\alpha_1,\alpha_2^*)\le U_1(\alpha_1^*,\alpha_2^*)$.

Neither player gains by deviating, so $(\alpha_1^*,\alpha_2^*)$ is a Nash equilibrium.

*Intuition note.* In a zero-sum game, what hurts one player helps the other. So "guaranteeing the most" and "best-responding to the opponent's best guarantee" turn out to be the same condition, provided max-min equals min-max (Prop. 341.1b).

The author draws three consequences, which hold independently of maxminimization (p. 342).
1. **Corollary 342.1.** Every Nash equilibrium of a strictly competitive game yields the same pair of payoffs. This can fail in games that are not strictly competitive, e.g. BoS (p. 342).
2. A Nash equilibrium can be found by solving $\max_{\alpha_1}\min_{\alpha_2}U_1$. If player 1's equilibrium payoff is known, any mixed strategy that yields this payoff against any pure strategy of player 2 solves the maxminimization problem. It is then an equilibrium strategy of player 1. This helps when payoffs are known before strategies (Exercise 344.2) (p. 342).
3. **Corollary 342.2 (interchangeability).** If $(\alpha_1,\alpha_2)$ and $(\alpha_1',\alpha_2')$ are Nash equilibria, so are $(\alpha_1,\alpha_2')$ and $(\alpha_1',\alpha_2)$. *Proof:* by (a), $\alpha_1,\alpha_1'$ are maxminimizers of player 1 and $\alpha_2,\alpha_2'$ of player 2. Also $\max\min U_1=\min\max U_1=U_1(\alpha_1,\alpha_2)=U_1(\alpha_1',\alpha_2')$. Then (b) applies to the mixed pairs (p. 342). BoS shows equilibria need not be interchangeable without strict competition (p. 343).

**Value of the game.** In any game, $\max_{\alpha_1}\min_{\alpha_2}U_1\le\min_{\alpha_2}\max_{\alpha_1}U_1$. For any $\alpha_1'$ and all $\alpha_2$, $U_1(\alpha_1',\alpha_2)\le\max_{\alpha_1}U_1(\alpha_1,\alpha_2)$. Taking minima over $\alpha_2$: $\min_{\alpha_2}U_1(\alpha_1',\alpha_2)\le\min_{\alpha_2}\max_{\alpha_1}U_1$. So the payoff player 1 can guarantee is at most what player 2 can hold her to (p. 343). If the two sides are equal, this payoff $v^*$ (player 1's equilibrium payoff) is the *value* of the game (p. 343).

**Corollary 343.1.** In a strictly competitive game, any Nash equilibrium strategy of player 1 guarantees her at least the value, and any equilibrium strategy of player 2 guarantees that player 1 gets at most the value. *Proof:* by 341.1a, $\alpha_1^*$ is a maxminimizer, so $U_1(\alpha_1^*,\alpha_2)\ge\min_{\alpha_2}U_1(\alpha_1^*,\alpha_2)=\max_{\alpha_1}\min_{\alpha_2}U_1=v^*$. Likewise player 2's equilibrium strategy guarantees her at least $-v^*$, which is the same as holding player 1 to at most $v^*$ (p. 343).

*Intuition note.* In a strictly competitive game, playing your equilibrium strategy is a safe choice. Whatever the opponent does, you get at least the equilibrium value.

Exercises 343.2, 343.3, 344.1–344.3 follow here (pp. 343–344); see "Exercises worth doing".

### Box: Maxminimization — some history (pp. 344–346)
The author says von Neumann developed the theory for general strictly competitive games in the late 1920s. An earlier appearance in a specific game is in Montmort's *Essay d'analyse sur les jeux de hazard* (1713 or 1714). It reports correspondence with Nikolaus Bernoulli and a letter (13 Nov 1713) from "M. de Waldegrave" about the card game *le Her* (pp. 344–345).

**Rules of le Her** (p. 345). Each player gets one card; values run ace = 1 up to king = 13. Player 1 may swap her card with player 2's. Player 2 must accept unless she holds a king, in which case she automatically wins. Then player 2 may swap her card for a random card from the rest of the deck. If it is a king, she automatically loses. Otherwise she makes the swap. The higher card wins, and player 2 wins ties.

As a strategic game, an action is a keep/exchange rule for each possible card, so each player has $2^{13}$ actions (p. 345). If player 1 exchanged, player 2 knows both cards and should draw if and only if her card would otherwise lose. If player 1 did not exchange, player 2's choice is less clear (p. 345). The three scholars argued that only these actions could be optimal:
- Player 1: "exchange up to 6" or "exchange up to 7".
- Player 2: "exchange up to 7" or "exchange up to 8".

Restricted to these, the game is equivalent to the matrix below (the source gives no row or column labels). Its payoffs are $(0,0),(5,-5)$ in the first row and $(3,-3),(0,0)$ in the second (p. 345). The game has no pure Nash equilibrium (p. 346).

Waldegrave considered randomizing. Player 1 mixing $(\tfrac38,\tfrac58)$ gets the same payoff whatever player 2 does, and is guaranteed $\tfrac{15}{8}$. Player 2 mixing $(\tfrac58,\tfrac38)$ ensures player 1 gets at most $\tfrac{15}{8}$ (p. 346). Check (added step): $\tfrac38\cdot0+\tfrac58\cdot3=\tfrac{15}8$ and $\tfrac38\cdot5+\tfrac58\cdot0=\tfrac{15}8$. The author says Waldegrave found each player's maxminimizer and understood its significance. Montmort wrote that "it seems to me" the letter "exhausts everything that one can say" about le Her (p. 346).

### Example 346.1: maxminimizer vs. equilibrium strategy (pp. 346–347)
The text says maxminimization seems to be conservative. It notes that in some non-strictly-competitive games the two payoffs also coincide, yet the predictions differ and a maxminimizer looks preferable (p. 346). The game of Figure 346.1:

| | L | R |
|---|---|---|
| T | 6, 0 | 0, 6 |
| B | 3, 2 | 6, 0 |

It has a unique Nash equilibrium: player 1 plays $(\tfrac14,\tfrac34)$ and player 2 plays $(\tfrac23,\tfrac13)$. Player 1's equilibrium payoff is 4 (p. 346). Player 1's maxminimizer is $(\tfrac13,\tfrac23)$ and guarantees 4 (Figure 347.1, p. 346–347). Check (added step): against L, player 1 gets $3+3p$. Against R she gets $6-6p$. These are equal at $p=\tfrac13$, giving 4. Her equilibrium strategy yields 4 if player 2 sticks to equilibrium, but if player 2 chooses a different strategy her payoff may be less than 4 (it may also be greater than 4) (p. 346). Her maxminimizer guarantees 4 regardless (p. 346).

*Intuition note.* Equilibrium play gives the equilibrium payoff if the opponent also plays equilibrium, but may give less if she does not. The maxminimizer guarantees its payoff whatever the opponent does.

### Box: Testing the theory (pp. 347–348)
Maxminimization makes a sharp prediction (p. 347). To avoid having to induce preferences, one can work with games with only two outcomes. Then monetary payoffs represent preferences and risk attitudes do not matter (p. 347). O'Neill (1987) used the game of Exercise 344.3, whose equilibrium strategy for each player is $(0.2,0.2,0.2,0.4)$. Each of 25 pairs played it 105 times (p. 347). Two issues arise (p. 347):
- Repetition could allow strategies conditioned on past play. The author says an analysis of these options concludes that players will eschew them in this game.
- Each subject faces more than two outcomes overall. Under the hypothesis that preferences are separable across trials, expected monetary payoffs still represent preferences in each trial.

Each subject got US$2.50, won US$0.05 per win, and paid US$0.05 per loss. Average observed frequencies were $(0.221,0.215,0.203,0.362)$ for player 1 and $(0.226,0.179,0.169,0.426)$ for player 2. These look fairly close to the prediction (p. 347). The $\chi^2$ test asks how probable a deviation at least this large would be if each player used exactly her equilibrium strategy. On the 16 outcome frequencies it rejects minmax behaviour decisively: the probability is less than 1 in 1,000 (pp. 347–348). Other tests on the data also reject it (Brown and Rosenthal (1990)) (p. 348). A higher-stakes, somewhat more complicated game (Rapoport and Boebel (1992)) also does not support maxminimization, though it explains the data better than two alternative theories. The author notes that a theory should work across a large class of games, not just one. Summary: evidence so far tends not to support maxminimization, though no other theory is systematically superior (p. 348).

## Toy example (ours, not from the text)
Player 1 chooses U or D, player 2 chooses L or R. The payoffs below are to player 1, and player 2 gets the negative (zero-sum):

| | L | R |
|---|---|---|
| U | 3 | 0 |
| D | 1 | 2 |

**Pure maxmin.** Row minima: U gives $\min(3,0)=0$, D gives $\min(1,2)=1$. So $\max\min=1$ (pure).
**Pure minmax.** Column maxima: L gives $\max(3,1)=3$, R gives $\max(0,2)=2$. So $\min\max=2$ (pure). Here $1<2$, which illustrates the general inequality.
**Mixed maxmin.** Let $p$ be the probability of U. Against L, player 1 gets $3p+1(1-p)=1+2p$. Against R she gets $0\cdot p+2(1-p)=2-2p$. Setting $1+2p=2-2p$ gives $p=\tfrac14$, with payoff $1+\tfrac12=1.5$.
**Mixed minmax.** Let $q$ be the probability of L. If player 1 plays U she gets $3q$. If she plays D she gets $q+2(1-q)=2-q$. Setting $3q=2-q$ gives $q=\tfrac12$, with payoff $1.5$.
So mixed $\max\min=\min\max=1.5$, the value. Check equilibrium. Against $q=\tfrac12$, U gives $1.5$ and D gives $0.5+1=1.5$, so player 1 is indifferent. Against $p=\tfrac14$, L gives player 2 $-(1+0.5)=-1.5$ and R gives $-(2-0.5)=-1.5$, so player 2 is indifferent. Hence $(\tfrac14,\tfrac12)$ is a Nash equilibrium, as Proposition 341.1b predicts. Each equilibrium strategy guarantees the value (Corollary 343.1).

## Concepts
- [[maxminimization]] (new) — choose the strategy maximizing the worst-case payoff over the opponents' strategies (p. 335; Def. 336.1, p. 336).
- [[guarantee]] (new) — strategy $\alpha_i$ guarantees $\underline u_i$ if its payoff is at least $\underline u_i$ against every opposing strategy (p. 336).
- [[zero-sum game & minimax]] — here, a two-player game with exactly reversed preferences; payoffs can be chosen to sum to zero (pp. 339–340).
- [[strictly-competitive-game]] (new) — two players, preferences diametrically opposed. There are separate ordinal (Def. 339.1) and vNM (Def. 339.2) versions, and the vNM version is stronger (pp. 339–340).
- [[Nash equilibrium]] — in this chapter, compared with maxminimizers; its payoff is at least the maxmin payoff in any game (p. 338).
- [[mixed strategy]] — used to raise the guaranteed payoff (pp. 337–338).
- [[value-of-the-game]] (new) — the common value of $\max\min U_1$ and $\min\max U_1$ when they are equal (p. 343).
- [[interchangeability]] (new) — in a strictly competitive game, mixing and matching players' strategies from different equilibria gives equilibria (Cor. 342.2, p. 342).
- [[strategic (normal-form) game]] — the setting, with vNM payoffs (p. 335).

## Canonical instances
- [[bargaining-game-ex-36-2]] (new) — pure-strategy maxminimizers are demands of $5 or $6 (p. 336).
- [[matching-pennies]] — strictly competitive (p. 339).
- [[battle-of-the-sexes]] — not strictly competitive. Its equilibria have different payoffs and are not interchangeable (pp. 339, 342–343).
- [[prisoners-dilemma]] — not strictly competitive (p. 339).
- [[le-her]] (new) — card game; Waldegrave's mixed maxminimizers $(\tfrac38,\tfrac58)$ and $(\tfrac58,\tfrac38)$ in a reduced 2×2 version of the game; player 1 is guaranteed $\tfrac{15}8$ and player 2 holds her to at most $\tfrac{15}8$ (pp. 345–346).
- [[oneill-game]] (new) — 4-action zero-sum game tested experimentally (pp. 344, 347).
- [[guessing-morra]] (new) — an exercise game (p. 344).

## Bridges (candidates)
- [same-math] Maxmin = minmax in a strictly competitive game ↔ decision-game-theory: the equality part of the minimax theorem for zero-sum games — here shown only under the assumption that an equilibrium exists (Prop. 341.1).
- [structural-analogy] Maxminimization as worst-case decision-making ↔ decision theory: pessimistic criteria under uncertainty — the opponent is treated as nature choosing the worst case.
- [structural-analogy] Equilibrium strategy that guarantees the value ↔ mechanism design / robustness: strategies that do not depend on correct beliefs about the other player.

## Questions this raises
- Without assuming a Nash equilibrium exists, does a strictly competitive game with finite actions always satisfy $\max\min=\min\max$ in mixed strategies? (Prop. 341.1b requires equality as a hypothesis.)
- If maxminimization is rejected in the lab, which theory should replace it? Does the answer depend on repeated play and incentives?
- How would one prove that preferences being strictly competitive for mixed strategies requires exactly a zero-sum vNM representation?
- In non-strictly-competitive games like Example 346.1, when is a maxminimizer more sensible than an equilibrium strategy?

## Exercises worth doing
- Ex. 338.2 (p. 338) — find a game with a unique Nash equilibrium where each player's equilibrium payoff strictly exceeds her maxmin payoff; shows Lemma 338.1 can be strict — difficulty: medium.
- Ex. 340.1 (p. 340) — test two games for strict competitiveness, with pure and with mixed strategies; shows the two definitions differ — difficulty: easy.
- Ex. 343.2 (p. 343) — find maxminimizers in BoS and show that no equilibrium strategy guarantees the equilibrium payoff — difficulty: medium.
- Ex. 344.1 (p. 344) — prove or refute: any profile giving player 1 the value is an equilibrium — difficulty: medium.
- Ex. 344.2 (p. 344) — Guessing Morra: use symmetry and the guarantee property to find all equilibria — difficulty: hard.
- Ex. 344.3 (p. 344) — O'Neill's game: find the symmetric mixed equilibrium and prove it is unique, using Cor. 342.1 and Cor. 343.1 — difficulty: hard.

## Reading notes
- The file is a draft chapter ("Version 00/11/6", copyright 1995–2000), not the published book. Its prerequisite line says Chapters 2 and 4.
- Page numbers: the labels give "printed" 310–319, then 9–12 for the last four pages. The page images, however, show running page numbers 335–348, and the chapter's own cross-references match them (e.g. "Proposition 341.1", "box on page 344"). I cite the **image numbers**. These equal pdf + 20 (pdf 315 = p. 335 … pdf 328 = p. 348).
- Misprint (p. 339): in the image, player 2's ordering in the Figure 339.1 discussion is written with subscript 1 ($\succ_1$) throughout. It should be $\succ_2$ for player 2.
- Misprint (p. 341, proof of b): "$a_2$" appears where $\alpha_2$ is meant.
- Page 340 prints $\overline a$, $\underline a$ for best and worst outcomes. The text layer lost the over- and underlines, but the image shows them.
- On p. 336, the guaranteed payoff is printed with an overline ($\overline u_i$).
- The matrix in the le Her box (p. 345) has no row or column labels in the source.
- The game of Exercise 36.2, Figures 13.1, 16.1 and 17.1, and the references cited are only mentioned; they are not in these pages.
- The history box (pp. 344–346) sits before the end of Section 11.3. The chapter's own Notes (p. 348) say the history box is based on Todhunter (1865) and Kuhn (1968), and that Guilbaud (1961) rediscovered Montmort's report of Waldegrave's work.
