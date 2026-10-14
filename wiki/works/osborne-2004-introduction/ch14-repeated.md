---
id: osborne-2004-introduction/ch14-repeated
work: osborne-2004-introduction
unit: "14 Repeated games: The Prisoner's Dilemma"
pages: 389–409
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Repeated games: The Prisoner's Dilemma

## L0 — One line
If players are patient enough, the threat of future punishment can make cooperation an equilibrium of the infinitely repeated Prisoner's Dilemma, and for patient players every feasible payoff pair that gives both more than 1 can be approximately sustained, even with subgame perfection.

## L1 — The gist (≤ 120 words)
Can mutual cooperation survive when a Prisoner's Dilemma is repeated with no known end? Players value a payoff stream by its discounted average (discount factor δ). With Figure 389.1's payoffs, two grim trigger strategies (defect forever once the other defects), or two tit-for-tat strategies (copy the other's last move), form a Nash equilibrium when δ ≥ 1/2. Punishing for k periods works only if k ≥ 2 and δ is large enough. For δ near 1, every feasible payoff pair with both payoffs above 1 is close to a Nash equilibrium payoff pair. Grim trigger is not subgame perfect; tit-for-tat is only if δ = 1/2. Punishing when either player defects fixes this; subgame perfect and Nash payoff sets coincide.

**Prerequisites:** Nash equilibrium; extensive games and subgame perfect equilibrium; strategies as plans for every history; geometric series; weighted averages.

## L2 — Key ideas (5–10 bullets)
- In repeated play a player may be deterred from a short-term gain by the threat of a long-term loss. The author offers this as a framework for studying why people often do not exploit co-players in ongoing relationships (p. 389).
- Players evaluate payoff streams by a discounted sum or discounted average. Payoffs are then cardinal: only increasing affine transformations preserve preferences, so one speaks of *a* repeated Prisoner's Dilemma (pp. 391–393).
- A strategy is a plan for every history and can be drawn as a state machine (grim trigger, limited punishment, tit-for-tat) (pp. 394–396).
- With the Figure 389.1 payoffs, both players using grim trigger or tit-for-tat is a Nash equilibrium if δ ≥ 1/2. Punishment of k periods needs k ≥ 2 and δ large enough; short punishment needs very patient players (pp. 396–398).
- For δ near 1, the feasible discounted-average payoffs are approximately the weighted averages of the stage-game payoffs. Nash equilibrium payoffs are at least 1 for each player, and any feasible pair with both payoffs above 1 is close to a Nash equilibrium payoff pair when δ is close enough to 1 (pp. 399–402).
- A strategy profile in an infinitely repeated game is subgame perfect iff no player can gain by deviating once after any history (p. 403).
- Grim trigger and limited punishment are not subgame perfect as stated. Tit-for-tat is subgame perfect only if δ = 1/2 (for the Figure 389.1 payoffs) (pp. 404–407).
- Punishing on *any* player's defection repairs grim trigger. With a similar path-following strategy, the subgame perfect and Nash equilibrium payoff sets coincide (pp. 405, 407–409).

## L3 — Walkthrough

### 14.1 The main idea (pp. 389–391)
- Many interactions are ongoing, and people often do not "take advantage" of their co-players. The theory of repeated games studies this (p. 389).
- Basic idea: a player may be deterred from exploiting a short-term gain by a "threat" of "punishment" that lowers her long-term payoff (p. 389).
- Stage game: the Prisoner's Dilemma of Figure 389.1, with C = cooperation, D = defection (p. 389).

| | C | D |
|---|---|---|
| C | 2, 2 | 0, 3 |
| D | 3, 0 | 1, 1 |

- The one-shot game has a unique Nash equilibrium, (D, D) (p. 389).
- Suppose one player plays C as long as the other plays C, and plays D in every period after any D by the other. If the other player cooperates always, she gets 2 per period. If she switches to D in some period, she gets 3 in that period and 1 in every later period; switching in the first period gives the stream (3, 1, 1, …) (p. 390).
- If she is not too impatient, (3, 1, 1, …) is worse than (2, 2, 2, …). So always playing C is a best response when the player is sufficiently patient (p. 390).
- Using the punishment strategy herself is also a best response, because the outcome is (C, C) every period either way. So both players using this strategy is a Nash equilibrium (p. 390).
- Always playing D after every history is also a Nash equilibrium, for any valuation of the future. Nothing a player does affects the other's behaviour (p. 390).
- Open questions the author lists (pp. 390–391):
  - How patient must players be?
  - Which other outcomes can be supported?
  - Is the punishment pair subgame perfect (is punishing optimal)? If not, is some other pair subgame perfect?
  - Are there equilibria with milder punishment?
  - To which other games do the arguments apply?

### 14.2 Preferences (pp. 391–393)
**14.2.1 Discounting.** Each player $i$ has a stage-game payoff function $u_i$ and a **discount factor** $\delta\in(0,1)$ (weight on next period's payoff relative to this period's). She evaluates outcomes $(a^1,\dots,a^T)$ by the **discounted sum**:
$$u_i(a^1)+\delta u_i(a^2)+\delta^2u_i(a^3)+\cdots+\delta^{T-1}u_i(a^T)=\sum_{t=1}^{T}\delta^{t-1}u_i(a^t).$$
Superscripts mean two things: $a^t$ is the action profile in period $t$, and $\delta^t$ is a power (p. 391). All players share the same δ. A δ near 0 means very impatient; near 1 means very patient (p. 391).

Reasons to discount (p. 391–392):
- plain impatience;
- a positive probability of dying in any period;
- borrowing and lending at a positive interest rate $r$.

The interest-rate case: with preferences that show no impatience, a player is indifferent between $(\$100,\$100,0,0,\dots)$ and $(\$100+\$100/(1+r),0,0,\dots)$, since lending $100/(1+r)$ yields $100 next period. Her preferences are then exactly represented by a discounted sum with $\delta=1/(1+r)$ (p. 392). Lottery example: 20 yearly payments of $50,000 at 7% are equivalent to about $567,000 as a lump sum (p. 392).

The author admits that discounted-sum preferences are restrictive. He says they capture the idea that people may value the present more highly than the future and appear not to obscure other relevant features (p. 392).

**14.2.2 Equivalent payoff functions.**
- Over deterministic atemporal outcomes, any increasing function of $u$ represents the same preferences. Over lotteries, any increasing affine function of a Bernoulli payoff function does (p. 392).
- Over streams: suppose $\sum\delta^{t-1}u(x^t)=\sum\delta^{t-1}u(y^t)$ and $v=\alpha+\beta u$ with $\beta>0$. Then
$$\sum\delta^{t-1}v(x^t)=\sum\delta^{t-1}\alpha+\beta\sum\delta^{t-1}u(x^t),$$
and likewise for $y$. So the two streams are also indifferent under $v$ (p. 392).
- **Lemma 393.1** (Equivalence of payoff functions under discounting). Suppose there are at least three possible outcomes. The discounted sum with $u$ and δ represents the same preferences over streams as the discounted sum with $v$ and δ if and only if there exist $\alpha$ and $\beta>0$ such that $u(x)=\alpha+\beta v(x)$ for all $x$ (p. 393).
- Consequence: stage-game payoffs are no longer merely ordinal. Example: replace (0, 3) and (3, 0) in Figure 389.1 by (0, 5) and (5, 0). For δ close enough to 1, each player prefers $((C,C),(C,C))$ to $((D,C),(C,D))$ in the first game but not in the second. So there is *a* repeated Prisoner's Dilemma, not *the* one. From now on, strategic games are defined by payoff functions (p. 393).
- **Discounted average** $=(1-\delta)\sum_{t=1}^\infty\delta^{t-1}w^t$. It represents the same preferences as the discounted sum (a constant multiple) when $\delta<1$. A constant stream $(c,c,\dots)$ has discounted average $c$, so values are comparable to one-period payoffs. The chapter uses the discounted average (p. 393).

> **Intuition note.** The discounted average is a "per-period equivalent" of a whole stream. Because only affine changes of payoffs keep preferences intact, the size of the temptation payoff (3 versus 5) matters for the repeated game.

### 14.3 Infinitely repeated games (pp. 393–394)
- Play may continue indefinitely. This may capture players' perceptions well even if play cannot literally go on forever, especially if the end is far away. A finite-horizon model is deferred to Section 15.3 (pp. 393–394).
- A repeated game is an extensive game with perfect information and simultaneous moves. A history is a sequence of action profiles (p. 394).
- **Definition 394.1.** Let $G$ be a strategic game with players $N$, actions $A_i$, payoffs $u_i$. The infinitely repeated game of $G$ for discount factor δ is the extensive game with perfect information and simultaneous moves in which (p. 394):
  - players are $N$;
  - terminal histories are all infinite sequences $(a^1,a^2,\dots)$ of action profiles of $G$;
  - the player function assigns all players to every proper subhistory of every terminal history;
  - the actions available to $i$ after any history are $A_i$;
  - $i$ evaluates $(a^1,a^2,\dots)$ by $(1-\delta)\sum_{t=1}^\infty\delta^{t-1}u_i(a^t)$.

### 14.4 Strategies (pp. 394–396)
A strategy specifies an action after every history, including histories the strategy itself would never produce (p. 394).

**Grim trigger.** $s_i(\varnothing)=C$ and
$$s_i(a^1,\dots,a^t)=\begin{cases}C&\text{if }a_j^\tau=C\text{ for }\tau=1,\dots,t\\ D&\text{otherwise.}\end{cases}\tag{394.2}$$
It is "grim" because a defection by the other player triggers relentless punishment (p. 394).

State diagrams (pp. 394–395):
- A strategy can be drawn with states, each labelled by the action chosen there. The initial state has a bold box. A state stays the same unless an event labelled on an outgoing arrow occurs.
- Grim trigger has state $\mathcal C$ (play C) and state $\mathcal D$ (play D). The arrow $(\cdot,D)$ means "other player chose D". Once in $\mathcal D$ it never leaves (Figure 395.1).
- A diagram must give, for every state, a transition for every possible outcome, including the player's own deviations. Figure 395.1 hides the null transitions (p. 395).
- **Limited punishment** (Figure 395.2): states $P_0:C$, $P_1:D$, $P_2:D$, $P_3:D$. After $(\cdot,D)$ in $P_0$ it moves $P_1\to P_2\to P_3$ after any outcome, then back to $P_0$. It plays D for three periods whatever the other does (p. 395).
- **Tit-for-tat**: do what the other player did last period. Two states $\mathcal C$, $\mathcal D$, with $(\cdot,D)$ leading $\mathcal C\to\mathcal D$ and $(\cdot,C)$ leading $\mathcal D\to\mathcal C$ (Figure 396.1). Punishment length depends on the other's behaviour (pp. 395–396).

Exercise 395.1 asks for diagrams of three strategies (a delayed grim, b grim that forgives one lapse, c Pavlov) (p. 396).

### 14.5 Some Nash equilibria of the infinitely repeated Prisoner's Dilemma (pp. 396–398)
Throughout: payoffs of Figure 389.1, common discount factor δ. If one player always plays D, the other's best response is to do the same, because (D, D) is a one-shot Nash equilibrium (p. 396).

**14.5.1 Grim trigger** (pp. 396–397).
- Suppose player 1 uses grim trigger. If player 2 does too, she gets (2, 2, …), discounted average 2 (p. 396).
- Any deviation includes a first D. After that player 1 plays D forever, so the best deviation plays D forever (D is her unique best response to D). If any deviation pays, deviating to D in period 1 pays (p. 396).
- That deviation gives (3, 1, 1, …) with discounted average
$$(1-\delta)[3+\delta+\delta^2+\cdots]=3(1-\delta)+\delta .$$
- She cannot gain iff $2\ge 3(1-\delta)+\delta$, i.e. $\delta\ge\tfrac12$. So **if $\delta\ge\frac12$, (grim trigger, grim trigger) is a Nash equilibrium** (p. 397).

**14.5.2 Limited punishment** (p. 397).
- Punish for $k$ periods ($k=3$ in Figure 395.2; grim is $k=\infty$). Suppose player 1 uses it. A profitable deviation for player 2 can be taken in period 1 (p. 397).
- After that deviation player 1 plays D for $k$ periods, so player 2 should play D too. In period $k+1$ after the deviation, player 1 returns to C and player 2 faces the same situation as at the start. So it suffices to compare the first $k+1$ periods (p. 397).
- Adhering gives $(1-\delta)[2+2\delta+\cdots+2\delta^k]=2(1-\delta^{k+1})$. Deviating gives $(1-\delta)[3+\delta+\cdots+\delta^k]=3(1-\delta)+\delta(1-\delta^k)$ (p. 397).
- No gain iff $2(1-\delta^{k+1})\ge3(1-\delta)+\delta(1-\delta^k)$, i.e. $\delta^{k+1}-2\delta+1\le0$ (p. 397). (Added step: expanding, the right side is $3-2\delta-\delta^{k+1}$, so the inequality becomes $-1+2\delta-\delta^{k+1}\ge0$.)
- Results: $k=1$ gives no $\delta<1$ that works. $k=2$ needs $\delta\ge0.62$. $k=3$ needs $\delta\ge0.55$. As $k$ grows the bound approaches $\tfrac12$ (p. 397).
- Conclusion: the $k$-period punishment pair is a Nash equilibrium so long as $k\ge2$ and δ is large enough; larger $k$ lowers the bound. Short punishment sustains (C, C) "only if the players are very patient" (p. 398).

**14.5.3 Tit-for-tat** (p. 398).
- Suppose player 1 uses tit-for-tat. If player 2 gains by deviating, she gains by playing D in period 1. Then player 1 plays D until she reverts to C. So she either alternates D, C (payoffs (3, 0, 3, 0, …)) or plays D forever (payoffs (3, 1, 1, …)) (p. 398).
- Alternating gives $(1-\delta)\cdot3/(1-\delta^2)=3/(1+\delta)$. Always D gives $3(1-\delta)+\delta=3-2\delta$. Adhering gives 2 (p. 398).
- Tit-for-tat is a best response to tit-for-tat iff $2\ge\frac{3}{1+\delta}$ and $2\ge3-2\delta$. Both are equivalent to $\delta\ge\tfrac12$. So **for $\delta\ge\frac12$, (tit-for-tat, tit-for-tat) is a Nash equilibrium** (p. 398).

> **Intuition note.** Cooperation holds when one period's gain from cheating (here 1 extra unit) is outweighed by the discounted losses afterwards. For these payoffs the threshold is δ = 1/2 for both grim trigger and tit-for-tat. Limited punishment with smaller $k$ needs a higher δ.

Exercise 398.1 asks for the δ-values at which each strategy of Exercise 395.1 gives a Nash equilibrium (p. 398).

### 14.6 Nash equilibrium payoffs when players are patient (pp. 398–402)
The equilibria so far give each player 2 (always (C, C)) or 1 (always (D, D)) (pp. 398–399). The general question is hard for arbitrary δ but tractable for δ close to 1 (p. 399).

**14.6.1 Feasible discounted average payoffs** (p. 399).
- Constant outcome $(X,Y)$ gives $(u_1(X,Y),u_2(X,Y))$. So (2, 2), (3, 0), (0, 3), (1, 1) are achievable (p. 399).
- Path alternating $(C,C)$ and $(C,D)$: player 1's payoffs alternate 2 and 0 (average 1), player 2's alternate 2 and 3 (average 5/2). Player 1's discounted average exceeds 1 for any δ, because more weight falls on the good first period of each cycle. It is close to 1 when δ is close to 1. Player 2's is below 5/2 but close to it when δ is near 1. So $(1,\tfrac52)$ is approximately achieved (p. 399).
- Repetition of $((C,C),(D,C),(D,C))$: player 1 gets close to $\tfrac13(2+3+3)=\tfrac83$ and player 2 close to $\tfrac13(2+0+0)=\tfrac23$ (p. 399).
- In general, for δ near 1 a repeated sequence's discounted average is close to its plain average, and only such payoffs can be achieved. So the feasible set is approximately the set of weighted averages of the stage payoffs (p. 399).
- **Definition 399.1.** The set of **feasible payoff profiles** of a strategic game is the set of all weighted averages of payoff profiles in the game (p. 399). The name is somewhat misleading: such profiles are not generally achievable in the one-shot game, only approximately as discounted averages in the repeated game (p. 400).
- Geometry: if $(x_1,x_2)$ and $(y_1,y_2)$ are feasible, take $k<m$ and a path with $k$ repetitions of the cycle yielding $(x_1,x_2)$ followed by $m-k$ repetitions of the cycle yielding $(y_1,y_2)$. Its average is $(k/m)(x_1,x_2)+(1-k/m)(y_1,y_2)$, a point on the line segment joining them. Varying $k$, $m$ gives all points with rational weights. So the feasible set is the parallelogram with vertices (0,3), (2,2), (3,0), (1,1) (Figure 400.1, p. 400).

**14.6.2 Nash equilibrium discounted average payoffs** (pp. 400–402).
- A player who plays D every period gets at least 1 per period. So no Nash equilibrium gives any player a discounted average below 1 (p. 400).
- Claim: every feasible pair in which both payoffs exceed 1 is close to a Nash equilibrium payoff pair when δ is close enough to 1 (pp. 400–401).
- Construction (p. 401):
  - For feasible $(x_1,x_2)$ take a finite sequence $(a^1,\dots,a^k)$ whose average payoff to each $i$ is $x_i$. Then $i$'s discounted average can be made as close to $x_i$ as wanted by δ near 1.
  - Let $(b^1,b^2,\dots)$ repeat this sequence ($b^1=b^{k+1}=\dots=a^1$, etc.).
  - Player $i$'s strategy: play $b_i^1$ first; after history $(h^1,\dots,h^{t-1})$ play
$$s_i(h^1,\dots,h^{t-1})=\begin{cases}b_i^t&\text{if }h_j^r=b_j^r\text{ for }r=1,\dots,t-1\\ D&\text{otherwise,}\end{cases}$$
where $j$ is the other player. Here only the *other* player's earlier actions are checked.
- Why it is a Nash equilibrium if $x_i>1$ for both $i$ (p. 401):
  - Since $x_i>1$, there is a period $t_i$ with $u_i(a^{t_i})>1$.
  - After a deviation by $i$, the other player plays D forever, so $i$ gets at most 1 per period. In every period where $a^{t_i}$ was due she gets 1 instead of $u_i(a^{t_i})>1$.
  - For δ close enough to 1, the discounted value of these losses outweighs any one-period gain from deviating.
- **Result** (for the Figure 389.1 game) (pp. 401–402):
  - For any δ, each player's payoff in every Nash equilibrium discounted average pair is at least 1.
  - For every feasible $(x_1,x_2)$ with $x_i>1$ for each $i$, there is $(y_1,y_2)$ close to $(x_1,x_2)$ such that, for δ close enough to 1, some Nash equilibrium has discounted averages $(y_1,y_2)$.
  - This is a special case of Proposition 413.1, stated later (p. 402).
- Why not "any path with discounted averages above 1"? That claim is false. Take $((C,C),(D,D),(D,D),\dots)$: each player's discounted average exceeds 1, but a player who deviates to D in period 1 gets more in period 1 and at least the same afterwards, however the opponent behaves. So no Nash equilibrium generates it (p. 402).
- Figure 402.1 shows the approximate Nash equilibrium payoff set. As drawn, it is the part of the parallelogram where both payoffs are at least 1: vertices about (1, 1), (1, 2.5), (2, 2), (2.5, 1). Although the one-shot game has a unique equilibrium, the repeated game's equilibrium payoffs range "from dismal to jointly maximal" (p. 402).

> **Intuition note.** Any feasible pair of long-run averages that beats the "always defect" floor of 1 for both players is approximately achieved by repeating a cycle of outcomes, enforced by the threat of permanent D. When δ is close enough to 1, the future loss from the threat outweighs the gain from one cheat. This explains why the set of equilibrium payoffs is so large.

### 14.7 Subgame perfect equilibria and the one-deviation property (pp. 402–404)
- Recalled from an earlier section (cross-reference unresolved in the draft): in a finite-horizon extensive game, a strategy profile is a subgame perfect equilibrium (SPE) iff it has the **one-deviation property**: no player can gain by changing her action at the start of any subgame in which she moves first, given the others' strategies and the rest of her own strategy (pp. 402–403). The question is whether this carries over to infinite horizons.
- An SPE trivially satisfies it, since no change of strategy can help. The converse needs proof (p. 403).
- Sketch: suppose $s$ is not an SPE, and in the subgame after $h$, player $i$ gains with $s_i'$ instead of $s_i$. Because far-future payoffs are worth little, there is a period $T$ such that any strategy agreeing with $s_i'$ through $T$ beats any strategy agreeing with $s_i$ through $T$. This holds even if the first gets the best outcome and the second the worst after $T$. So the strategy that follows $s_i'$ through $T$ and $s_i$ afterwards beats $s_i$. Then the finite-horizon argument gives a one-period deviation (p. 403).
- **Proposition 403.1** (One-deviation property of SPE of infinitely repeated games). A strategy profile in an infinitely repeated game is a subgame perfect equilibrium iff no player can gain by changing her action after any history, given the others' strategies and the remainder of her own strategy (p. 403).
- Proof (pp. 403–404):
  - If $s$ is an SPE, no deviation gains.
  - Conversely, if $s$ is not an SPE, assume WLOG (without loss of generality) the failing subgame starts at the initial history, with player $i$ and a better $s_i'$.
  - Choose $T$ so large that following $s_i'$ through $T$ exceeds following $s_i$ through $T$, even if the first strategy gets the best outcome and the second the worst after $T$. Let $s_i''$ follow $s_i'$ through $T$ and $s_i$ afterwards; it is better than $s_i$.
  - $s_i''$ and $s_i$ differ after only finitely many histories. So the finite-horizon argument (reference unresolved in the draft) yields a history and a strategy differing from $s_i$ only in its first action there that beats $s_i$. So some player gains by a one-period deviation.

> **Intuition note.** To check subgame perfection you need only test single-period deviations in every subgame. Discounting makes the far future negligible, so a long profitable deviation can always be cut into a finite one, and then into a one-period one.

### 14.8 Some SPE of the infinitely repeated Prisoner's Dilemma (pp. 404–409)
- Nash equilibrium requires only that each player's strategy be optimal in the whole game; after histories that do not occur, the prescribed actions may not be optimal. They may be "threats" that need not be optimal to carry out. SPE requires optimality after every history (p. 404).
- (Always D, always D) is an SPE: D is optimal whatever happens (p. 404).

**14.8.1 Grim trigger** (pp. 404–405).
- After outcome (C, D) in period 1, adherence to grim trigger gives outcomes $((D,C),(D,D),(D,D),\dots)$ in the subgame. Player 1 then gets $3(1-\delta)+\delta=3-2\delta$ (p. 405).
- If player 1 instead does not punish and plays C forever, the outcome is (C, C) from period 2 on, and she gets 2. If $\delta>\tfrac12$ then $2>3-2\delta$, so she does not want to punish (p. 405).
- For *any* δ the pair fails. After (C, D), player 2 (who deviated) prefers D from period 2 on, giving (D, D) forever, to C in period 2 and then D (giving (D, C) then (D, D)). So grim trigger vs grim trigger is not an SPE for any δ (p. 405).
- Fix: a player plays D after any history in which *either* player chose D (Figure 405.1: arrow from $\mathcal C$ to $\mathcal D$ on "all outcomes except (C, C)"). After a deviation the deviator plays D forever, so punishing by D is optimal for the opponent. The deviator's own D is optimal because (D, D) is a stage-game Nash equilibrium. Effectively, a player "punishes" the opponent who fails to punish her (p. 405).

**14.8.2 Limited punishment** (p. 406).
- The pair is not an SPE, for the same reason as grim trigger. The fix is to make the $P_0\to P_1$ transition occur whenever *either* player chooses D. A player plays D in her own punishment (optimal for her, and it makes her opponent's punishing optimal), and both revert to C afterwards (p. 406).
- Exercise 406.1 asks whether an SPE exists in which the two players have different punishment lengths (p. 406).

**14.8.3 Tit-for-tat** (pp. 406–407).
- Behaviour after a history depends only on its last outcome, so there are four subgame types: last outcome (C, C), (C, D), (D, C), (D, D). By Proposition 403.1 we check one-period deviations (p. 406).
- After (C, C): covered by the Nash analysis, needs $\delta\ge\tfrac12$ (p. 406).
- After (C, D) (player 2 adheres to tit-for-tat):
  - Adhering, player 1 gets outcomes alternating (D, C), (C, D), …, with $(1-\delta)(3+3\delta^2+\cdots)=3/(1+\delta)$.
  - Deviating to C first gives (C, C) forever, so 2.
  - Optimality needs $3/(1+\delta)\ge2$, i.e. $\delta\le\tfrac12$ (p. 406).
- After (D, C): adhering gives alternation starting with (C, D): $3\delta/(1+\delta)$. Deviating to D gives (D, D) forever, so 1. Optimality needs $3\delta/(1+\delta)\ge1$, i.e. $\delta\ge\tfrac12$ (p. 407).
- After (D, D): adhering gives 1. Deviating to C gives alternation starting with (C, D): $3\delta/(1+\delta)$. Optimality needs $\delta\le\tfrac12$ (p. 407).
- Conclusion: (tit-for-tat, tit-for-tat) is an SPE iff $\delta=\tfrac12$. For other payoffs it can fail for every δ: the pair is an SPE of a repeated Prisoner's Dilemma "only if the payoffs of the component game are rather special" (p. 407).
- Exercise 407.1 (Figure 407.1: payoffs $x,x$; $0,y$; $y,0$; $1,1$) asks to show that the pair is an SPE iff $y-x=1$ and $\delta=1/x$ (p. 407).

**14.8.4 SPE payoffs when players are patient** (pp. 407–409).
- Every SPE is a Nash equilibrium, so SPE payoff pairs are a subset of Nash equilibrium payoff pairs. The author argues the two sets are the same, by modifying the 14.6 strategy (p. 408).
- Let $(x_1,x_2)$ be feasible with $x_i>1$, with sequence $(a^1,\dots,a^k)$ and repeated path $(b^1,b^2,\dots)$ as in 14.6. Strategy $s_i$: play $b_i^1$ first, then
$$s_i(h^1,\dots,h^{t-1})=\begin{cases}b_i^t&\text{if }h^r=b^r\text{ for }r=1,\dots,t-1\\ D&\text{otherwise.}\end{cases}$$
Here the whole outcome (both players' actions) is compared with the path, unlike in 14.6 (p. 408).
- Claim: $(s,s)$ is an SPE, with two types of subgame (p. 408):
  1. *History equals $b^r$ in every period.* The argument is the same as for the Nash equilibrium in 14.6. Adherence gives each player close to $x_i$ for δ near 1. A deviation may gain in one period, but then the opponent plays D forever. Since $x_i>1$, the deviation makes the deviator worse off for δ close enough to 1.
  2. *Some earlier outcome differed from $b^r$.* Both players then play D whatever happens. Always-D is a Nash equilibrium of the repeated game, so this is a Nash equilibrium of the subgame.
- Point: after any deviation, the strategies prescribe Nash equilibrium actions of the stage game in every later period, so neither player has an incentive to deviate (p. 408).
- Since Nash equilibrium payoffs are at least 1, the SPE payoff set is exactly the Nash equilibrium payoff set, in the sense of two statements (p. 409):
  - for any δ, each player's payoff in every SPE discounted-average pair is at least 1;
  - for every feasible $(x_1,x_2)$ with $x_i>1$, there is $(y_1,y_2)$ close to $(x_1,x_2)$ such that, for δ close enough to 1, some SPE has discounted averages $(y_1,y_2)$.

> **Intuition note.** Subgame perfection fails for simple strategies because punishing may cost the punisher. Making the strategy punish *both* the deviator and anyone who does not punish turns the punishment phase into a (D, D) equilibrium that no one wants to leave. The set of equilibrium payoffs is unchanged (p. 409).

## Toy example (ours, not from the text)
Stage game: C/C gives (4, 4), D vs C gives 5 to the defector and 0 to the cooperator, D/D gives (1, 1). Both players use grim trigger.
- Adhering: stream (4, 4, 4, …), discounted average 4.
- Best deviation (D in period 1): stream (5, 1, 1, …), discounted average $(1-\delta)[5+\delta+\delta^2+\cdots]=5(1-\delta)+\delta=5-4\delta$.
- No gain iff $4\ge5-4\delta$, i.e. $\delta\ge\tfrac14$.
- Check at $\delta=0.5$: $\delta+\delta^2+\cdots=0.5/0.5=1$, so the average is $0.5\cdot(5+1)=3<4$: adhering is better. At $\delta=0.2$: $5-0.8=4.2>4$: deviating pays.
- The threshold fell from 1/2 to 1/4 because the one-period temptation gain (1 unit) is smaller relative to the per-period loss after punishment (3 units). In the book's game the gain is 1 and the loss is 1, giving 1/2.

## Concepts
- [[repeated-game-and-folk-theorem]] — a stage game played over many periods. Here: for patient players, feasible payoffs above 1 each are (approximately) equilibrium payoffs (pp. 394, 401–402, 409).
- [[infinitely-repeated-game]] (new) — extensive game with simultaneous moves whose terminal histories are infinite sequences of stage action profiles (p. 394).
- [[discount-factor]] (new) — weight δ ∈ (0, 1) per period of delay. With borrowing and lending at rate $r$, δ = 1/(1+r) (pp. 391–392).
- [[discounted-average-payoff]] (new) — $(1-\delta)\sum\delta^{t-1}w^t$; a constant stream $c$ has value $c$ (p. 393).
- [[shadow-of-the-future]] — the weight on future payoffs, here δ. The future loss from punishment must outweigh the immediate gain (pp. 390, 397).
- [[nash-equilibrium]] — each strategy is optimal in the whole game; off-path actions may be non-optimal "threats" (pp. 390, 404).
- [[subgame-perfect-equilibrium]] — strategies optimal after every history, including off-path ones (p. 404).
- [[one-deviation-property]] (new) — no player can gain by changing her action after any single history. In infinitely repeated games it is equivalent to subgame perfection (Prop. 403.1) (pp. 402–403).
- [[grim-trigger-strategy]] (new) — play C until anyone (or the other player, in the basic version) plays D, then D forever (pp. 394, 405).
- [[tit-for-tat]] (new) — copy the other player's action from the previous period (p. 395).
- [[limited-punishment-strategy]] (new) — after a defection, play D for $k$ periods, then return to C (pp. 395, 397).
- [[feasible-payoff-profile]] (new) — a weighted average of stage-game payoff profiles; only approximately achievable, via discounted averages for δ near 1 (pp. 399–400).
- [[strategic-normal-form-game]] — here defined by players, actions and payoff functions, not by preferences (p. 393).

## Canonical instances
- [[repeated-prisoners-dilemma]] (new) — payoffs (2, 2), (0, 3), (3, 0), (1, 1); cooperation sustained by grim trigger, limited punishment or tit-for-tat when δ is large enough (pp. 389, 396–398).
- [[lottery-annuity-discounting]] (new) — 20 payments of $50,000 at 7% are worth about $567,000 now (p. 392).

## Bridges (candidates)
- [same-math] discount factor δ = 1/(1+r) ↔ finance: present value of a payment stream at interest rate $r$ — the text derives δ from borrowing and lending (p. 392).
- [same-math] Nash equilibrium payoffs above 1 for patient players (Prop. 413.1 special case) ↔ canon concept "repeated game & folk theorem" — the unit proves a special case of the general result it calls Proposition 413.1 (p. 402).
- [structural-analogy] tit-for-tat and grim trigger ↔ reciprocity (direct, indirect, network): cooperation held in place by the other's conditional response.
- [structural-analogy] one-deviation property ↔ dynamic programming: checking single-step deviations in every state — proposal only; the unit does not mention dynamic programming.
- [metaphor] grim trigger as a "threat" ↔ credible commitment: the unit shows that the threat is not credible without the modification (pp. 404–405).

## Questions this raises
- How does the picture change when the horizon is finite? The author defers this to Section 15.3 (p. 394).
- How do the results extend beyond the Prisoner's Dilemma? The author mentions Proposition 413.1 as the general version (p. 402).
- What happens at intermediate δ, where the set of equilibrium payoffs is hard to characterise (p. 399)?
- Are there SPE with milder punishments than the modified grim strategy, and do they support the same payoffs (pp. 391, 406)?

## Exercises worth doing
- Ex. 395.1 (p. 395–396) — draw state diagrams for delayed grim, one-lapse-forgiving grim, and Pavlov; builds fluency with strategies as machines — difficulty: easy
- Ex. 398.1 (p. 398) — find the δ for which each strategy pair is a Nash equilibrium; if none exists, ask for which stage payoffs one would — difficulty: medium
- Ex. 406.1 (p. 406) — SPE with different punishment lengths for the two players — difficulty: hard
- Ex. 407.1 (p. 407) — show that tit-for-tat is an SPE iff $y-x=1$ and $\delta=1/x$, using the one-deviation property — difficulty: medium

## Reading notes
- Source is an author's draft chapter ("Draft chapter from *An introduction to game theory*", version 00/11/6, copyright 1995–2000), not the published book.
- **Page numbers.** The page labels give "printed 305–314" for pdf 368–377 and "?" for pdf 378–388. The images show the chapter's own numbers 389–409. I cite those: printed (image) = pdf + 21. The last page (p. 409) ends with an empty "Notes" heading.
- Unresolved cross-references appear as "Section ?????", "Proposition ????", "Proposition ???" (pp. 402, 403, 404, 406). References to "Lemma 145.1", "(449.1)", "(449.2)", "Section 15.3" and "Proposition 413.1" point outside this unit.
- Misprint in the image: the sums in Section 14.2.2 (p. 392) run from $t=0$ while using $\delta^{t-1}$. The definition on p. 391 starts at $t=1$.
- In 14.6 (p. 401) the strategy checks only the *other* player's earlier actions ($h_j^r=b_j^r$). In 14.8.4 (p. 408) it checks the whole outcome ($h^r=b^r$).
- Figure 402.1 vertices are my reading of the drawing. The text gives no coordinates.
