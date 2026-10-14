---
id: osborne-2004-introduction/ch06-extensive
work: osborne-2004-introduction
unit: "6 Extensive Games with Perfect Information: Illustrations"
pages: 179-200
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Extensive Games with Perfect Information: Illustrations

## L0 — One line
Solving sequential games from the end backwards (subgame perfect equilibrium) gives sharp predictions in the ultimatum, holdup, Stackelberg, vote-buying and race games, and the results illustrate how moving first, moving second and committing matter.

## L1 — The gist (≤ 120 words)
The chapter applies subgame perfect equilibrium (SPE), found by backward induction, to five sequential games. In the ultimatum game the SPE gives the proposer the whole pie, but experiments do not match this, and two explanations are discussed. In the holdup game the SPE has the second player under-invest. In Stackelberg's duopoly the first mover does at least as well as in Cournot's game. In vote-buying (VX, VY: groups' values; k: legislators; μ: a bare majority), bill Y passes if VX < kVY/μ, and bill X passes if VX > kVY/μ. In the race, in SPE only one player moves. It matters because it shows how to turn a story into a game tree and solve it from the end.

**Prerequisites:** extensive games with perfect information, histories, strategies, backward induction and SPE (Chapter 5); best responses and Cournot's duopoly; maximizing a quadratic.

## L2 — Key ideas (5–10 bullets)
- **Ultimatum game:** the only SPE has person 1 offer 0 and person 2 accept every offer. Person 1 gets all of $c. (p. 180)
- **Why not "reject 0":** if person 2 rejected the offer 0, person 1 would have no optimal offer. The same "no optimum" argument is reused in Stackelberg and vote-buying. (pp. 180, 188, 192)
- **Experiments:** ultimatum experiments do not accord well with SPE. Equity-conscious preferences or "rules of thumb" are offered as explanations, and the evidence is broadly consistent with both. (pp. 181–182)
- **Holdup game:** person 2 chooses little effort in the unique SPE whatever the pie sizes, and in the author's example (great-effort pie much larger, extra effort only slightly larger) both could be much better off with great effort. (p. 184)
- **Stackelberg:** if firm 2 has a unique best response to each output, the first mover is at least as well off as in Cournot's Nash equilibrium. In the constant-cost, linear-demand example it produces more, and the follower produces less. Being committed to an output is valuable. (pp. 186–189)
- **Vote-buying:** the second mover (Y) is favoured and never pays. X wins only if VX > kVY/μ, and then pays every legislator VY/μ. (pp. 191–193)
- **Race:** in every Gi(k1, k2) only one player moves and the other gives up. A threat to speed up is part of equilibrium. Sunk costs are ignored. (pp. 194–200)
- **Method:** solve small subgames first and use their results to solve bigger ones. (p. 195)

## L3 — Walkthrough

### 6.1 Introduction (p. 179)
The first three sections use games whose longest history has length two or three. The last section studies a game with an arbitrary finite horizon (the maximum length of any history). Infinite-horizon games come in Chapters 16 and 14 (p. 179).

### 6.2 The ultimatum game and the holdup game

**6.2.1 The ultimatum game.** Two people split $c. Person 1 offers person 2 an amount up to $c. If 2 accepts, 1 gets the remainder. If 2 rejects, both get nothing. Each cares only about her own money and wants as much as possible. The offer may be any real number (p. 179).

Formal game (pp. 179–180):
- Players: the two people.
- Terminal histories: sequences $(x, Z)$ with $0 \le x \le c$ and $Z \in \{Y, N\}$ (yes or no).
- Player function: $P(\emptyset)=1$, $P(x)=2$ for all $x$.
- Payoffs: at $(x,Y)$ person 1 gets $c-x$ and person 2 gets $x$. At $(x,N)$ both get 0.

*Backward induction* (p. 180):
1. In the subgame after an offer $x>0$, person 2's optimal action is to accept.
2. After $x=0$ she is indifferent. So in an SPE her strategy either accepts all offers (including 0), or accepts all $x>0$ and rejects $x=0$.
3. If 2 accepts everything, person 1's optimal offer is 0, which yields her $c$.
4. If 2 accepts all offers except 0, no offer of person 1 is optimal. Any $x>0$ is beaten by $x/2$. The offer 0 is rejected and gives 1 a payoff of 0, so any positive offer below $c$ is better.
5. Conclusion: the only SPE is person 1 offering 0 and person 2 accepting all offers. Payoffs are $c$ and 0.

The author says this one-sided outcome follows from the one-sided structure of the game. If person 2 may counteroffer, the outcome is, under some circumstances, less one-sided (explored in Chapter 16) (p. 180).

*Intuition note.* The proposer has all the power: the responder's only alternative is nothing, so any positive amount is better than rejecting. The case "accept everything except 0" fails because the proposer could always offer slightly more than nothing.

Exercises 180.1–180.3 and 181.1 are posed in the text (pp. 180–181). In 181.1, person $i$'s payoff is $u_i(x_1,x_2)=x_i-\beta_i|x_1-x_2|$ with $\beta_i>0$ (p. 181).

**Experiments on the ultimatum game (box, pp. 181–182).**
- First test: late 1970s, graduate economics students in Cologne. The pie $c$ ranged from 4 DM to 10 DM. 42 students were split into two groups. Each "player 1" wrote a demand, and a randomly chosen "player 2" accepted or rejected. Each had 10 minutes. It was repeated a week later (Güth, Schmittberger and Schwarze 1982) (p. 181).
- Results: average demands were $0.65c$ and $0.69c$ in the two runs, much less than the SPE prediction of $c$ or $c-0.01$. Almost 20% of offers were rejected. These included one of 3 DM out of 7 DM and five of about 1 DM out of pies of 4–6 DM (p. 181).
- Many other experiments, including one with much larger sums, give similar results. The author's summary: the results "do not accord well" with SPE (p. 181).

The author then asks "Or do they?" (a rhetorical question; the text answers that they may, under other assumptions about preferences) (p. 182).
- **Equity-conscious preferences.** Subjects may care about the opponent's money. The author says an equity-conscious variant has SPE with significant offers (as Exercise 181.1 shows). But such an explanation should also apply to related games (p. 182).
- **Related games.** In SPE of the dictator and impunity games, player 1 offers 0. In the equity-conscious variants, player 1's offers are no higher than in the analogous ultimatum variant, and for moderate equity-consciousness they are lower. The author calls this broadly consistent with experiments on the three games (p. 182).
- **What it cannot explain.** Positive offers are sometimes rejected, which is inconsistent with SPE even for equity-conscious players, given the payoff form of Exercise 181.1. An equity-conscious player 2 rejects inequitable offers, but then player 1 does not make them. To get rejections in equilibrium one must assume that people differ in equity-consciousness and that player 1 does not know player 2's degree (Exercise 222.2) (p. 182).
- **Alternative: rules of thumb.** Significant offers may be driven by a rational fear that small offers get rejected. Player 2 may reject because in daily life we use rules of thumb suited to repeated interactions, where punishing paltry offers and building a reputation pays. Subjects may then reject low offers in the ultimatum game but accept them in the impunity game. The evidence so far is "broadly consistent with both" explanations (p. 182).

Exercises 183.1 and 183.2 follow (p. 183).

**6.2.2 The holdup game.** Before an ultimatum game, person 2 chooses effort. Little effort gives a small pie $c_L$. Great effort gives a large pie $c_H$. Her payoff is $x-E$ if her share is $x$, where $E=L$ for little effort and $E=H>L$ for great effort (p. 183). Formulating the game precisely is Exercise 183.3.

*Solution* (p. 184):
1. Each subgame after person 2's effort choice is an ultimatum game. It has a unique SPE: person 1 offers 0, and person 2 accepts all offers.
2. So if person 2 chooses $L$ her payoff is $-L$, and if she chooses $H$ it is $-H$. She chooses $L$.
3. The unique SPE: person 2 exerts little effort, and person 1 obtains all of the small pie.

This result does not depend on $c_L, c_H, L, H$ (given $H>L$). Even if $c_H$ is much larger than $c_L$ and $H$ is only slightly larger than $L$, person 2 exerts little effort. Both could be much better off with great effort, but no such outcome is sustainable, because person 2 may be "held up" for the entire pie. The result does not depend sensitively on the extreme ultimatum outcome. Section 16.3 analyses a model where bargaining gives a more equal split and a similar result may emerge (p. 184).

*Intuition note.* Person 2 pays the cost of effort but expects to receive nothing of the extra pie. So she saves the effort even when the gain to the pair is large.

### 6.3 Stackelberg's model of duopoly

**6.3.1 General model.** Two firms sell the same good. Firm $i$ has cost $C_i(q_i)$, and the price at total output $Q$ is $P_d(Q)$ (the subscript $d$ avoids a clash with the player function $P$). They choose outputs sequentially: firm 1, then firm 2, who sees firm 1's output (p. 184).

Game (pp. 184–185):
- Players: the two firms.
- Terminal histories: all $(q_1,q_2)$ with $q_i \ge 0$.
- Player function: $P(\emptyset)=1$, $P(q_1)=2$ for all $q_1$.
- Payoff of firm $i$: $q_iP_d(q_1+q_2)-C_i(q_i)$.

A strategy of firm 1 is an output. A strategy of firm 2 is a function from firm 1's outputs to outputs (p. 185).

*Backward induction* (p. 185):
1. For each $q_1$, find firm 2's profit-maximizing output. Suppose it is unique and call it $b_2(q_1)$. Then in any SPE firm 2's strategy is $b_2$.
2. Firm 1 then chooses $q_1$ to maximize
$$q_1 P_d\big(q_1+b_2(q_1)\big)-C_1(q_1). \tag{185.1}$$
Suppose the maximizer is unique and call it $q_1^*$.
3. If firm 2 has a unique best response to each $q_1$ and firm 1 has a unique best action, the SPE is $(q_1^*, b_2)$. Firm 2's equilibrium output is $q_2^*=b_2(q_1^*)$.
4. As firm 1 varies $q_1$, the outcome moves along firm 2's best response function. So the SPE outcome $(q_1^*,q_2^*)$ is the point on $b_2$ that maximizes firm 1's profit.

**6.3.2 Example.** Take $C_i(q_i)=cq_i$ and
$$P_d(Q)=\begin{cases}\alpha-Q & \text{if } Q\le\alpha\\ 0 & \text{if } Q>\alpha,\end{cases}\tag{185.2}$$
with $0<c<\alpha$. Firm 2's unique best response is $b_2(q_1)=\tfrac12(\alpha-c-q_1)$ if $q_1\le\alpha-c$, and $0$ otherwise (pp. 185–186).

Firm 1 maximizes (p. 186)
$$q_1\big(\alpha-c-(q_1+\tfrac12(\alpha-c-q_1))\big)=\tfrac12 q_1(\alpha-c-q_1).$$
This quadratic is zero at $q_1=0$ and $q_1=\alpha-c$, so its maximizer is $q_1=\tfrac12(\alpha-c)$.

Results (p. 186):
- There is a unique SPE. Firm 1 produces $q_1^*=\tfrac12(\alpha-c)$, and firm 2's strategy is $b_2$.
- Firm 2's output: $q_2^*=b_2(q_1^*)=\tfrac12\big(\alpha-c-\tfrac12(\alpha-c)\big)=\tfrac14(\alpha-c)$.
- Profits: firm 1 gets $\tfrac18(\alpha-c)^2$ and firm 2 gets $\tfrac1{16}(\alpha-c)^2$.
- In Cournot's simultaneous game, each firm produces $\tfrac13(\alpha-c)$ and earns $\tfrac19(\alpha-c)^2$.
- So the first mover produces more and earns more than in the Cournot equilibrium, and the second mover produces less and earns less.

*Intuition note.* In the example, firm 1 knows firm 2 will cut output when firm 1 raises its own. So firm 1 can "push" firm 2 down its reaction curve and take a larger share. Exercise 186.1 repeats the analysis with quadratic costs.

**6.3.3 Properties of SPE** (pp. 186–189).

*First-mover's equilibrium profit.* Whenever firm 2 has a unique best response to each output of firm 1, firm 1 is at least as well off in any SPE of Stackelberg's game as in any Nash equilibrium of Cournot's game. The author says this follows from the general result in Exercise 175.2a. Argument: firm 1 can choose its Cournot-equilibrium output. Firm 2's best action is then its Cournot output, so firm 1 gets its Cournot profit. A different output may give more (p. 186).

*Equilibrium outputs* (p. 187). A weak form of "firm 1 produces more and firm 2 less" holds whenever firm 2's best response function is decreasing where it is positive.
- Figure 187.1 shows the best responses $b_1$ (dashed) and $b_2$, with the Cournot equilibrium $(\bar q_1,\bar q_2)$ at their intersection.
- Along each gray curve firm 1's profit is constant, and lower curves mean higher profit. A reduction in firm 2's output raises the price and so raises firm 1's profit.
- Each curve is horizontal where it crosses $b_1$, since $b_1$ maximizes firm 1's profit given $q_2$.
- So the SPE outcome $(q_1^*,q_2^*)$ is the point on $b_2$ giving firm 1 the highest profit. With $b_2$ downward-sloping, firm 1 produces at least as much, and firm 2 at most as much, as in the Cournot equilibrium.

*Zero output for firm 2* (pp. 187–188). For some cost and demand functions, firm 2's SPE output is zero (Figure 188.1).
- The best response function jumps at $q_1^*$. One possible cause is a fixed cost for firm 2 (Exercise 57.3).
- When firm 1 produces $q_1^*$, firm 2's maximal profit is zero. It obtains this both with no output and with the output $\hat q_2$.
- Below $q_1^*$ firm 2 earns positive profit and produces a positive output. Above $q_1^*$ it produces nothing.
- Given the figure's shapes, firm 1's best point on $b_2$ is $(q_1^*,0)$.

The author claims a unique SPE: firm 1 produces $q_1^*$, and firm 2 plays its best response except at $q_1^*$, where it produces 0. Reason: if firm 2 answered $q_1^*$ with $\hat q_2$, firm 1 would have no optimal output. It would want slightly more than $q_1^*$ (to induce zero output), but the closer to $q_1^*$ the better, and there is no smallest output above $q_1^*$. This is like the ultimatum game with rejection of 0 (p. 188).

If firm 2 were absent, firm 1 would produce $\hat q_1<q_1^*$. So firm 2 affects the outcome even though it produces nothing (p. 188). Exercise 188.1 gives numbers: $c=0$, $\alpha=12$, $f=4$ (output 8 and 0) (pp. 188–189).

*The value of commitment* (p. 189). Firm 1's SPE output is generally not a best response to firm 2's output. If it could adjust after firm 2 moves, it would (in Figure 187.1 it would reduce output). But add a third stage in which firm 1 chooses again. Then the first stage is irrelevant and firm 2 is effectively the first mover. In the SPE firm 1 is worse off than in the simultaneous-move Nash equilibrium. In the linear example, firm 2 chooses $(\alpha-c)/2$ and firm 1 chooses $(\alpha-c)/4$. So firm 1 prefers to be committed not to change its mind.

*Intuition note.* More options can hurt. If firm 2 knows firm 1 can change its mind, firm 2 will not back down. Binding itself to its first output is what gives firm 1 its advantage.

Exercise 189.1 is the sequential Bertrand game.

### 6.4 Buying votes

*Setup* (pp. 189–190). A legislature has $k$ members, $k$ odd. Bills $X$ and $Y$ compete, and the bill with a majority passes. Interest group $X$ first gives each legislator an amount (possibly zero), then group $Y$ does. Group $X$ values bill $X$ at $V_X>0$ and bill $Y$ at zero. Group $Y$ values bill $Y$ at $V_Y>0$ and bill $X$ at zero. Each legislator votes for the group offering her most, and for $Y$ in a tie (an arbitrary assumption that, the author says, does not qualitatively change the outcome).
- Example: with $k=3$, $x=(100,50,0)$ and $y=(100,0,50)$, legislators 1 and 3 vote $Y$ and 2 votes $X$, so $Y$ passes.

Game (p. 190):
- Players: groups $X$ and $Y$.
- Terminal histories: $(x,y)$, each a list of $k$ nonnegative integers.
- Player function: $P(\emptyset)=X$, $P(x)=Y$.
- Payoff of $X$: $V_X-(x_1+\dots+x_k)$ if bill $X$ passes, and $-(x_1+\dots+x_k)$ if bill $Y$ passes.
- Bill $Y$ passes after $(x,y)$ if and only if at least $\tfrac12(k+1)$ components of $y$ are at least equal to the corresponding components of $x$.
- Group $Y$'s payoff is the analogue.

*Two examples* (pp. 190–191), both with $k=3$:
- $V_X=V_Y=300$. Any payments by $X$ summing to at most 300 include two that sum to at most 200. $Y$ can match those two for less than 300 and win. So in any SPE neither pays, and $Y$ passes (tie-break).
- $V_X=300$, $V_Y=100$. If $X$ pays each legislator more than 50, matching costs $Y$ more than 100, so $Y$ cannot profitably match. But no SPE has $X$ paying more than 50 each, since $X$ could pay a little less. In the only SPE $X$ pays each legislator exactly 50, and $Y$ pays nothing. $Y$ is then indifferent between matching and not. But no SPE has $Y$ matching, because $X$ could then raise payments slightly and make matching unprofitable.

The author says that in general the outcome takes one of these two forms (p. 191).

*General solution by backward induction* (pp. 191–192). Let $\mu=\tfrac12(k+1)$ (a bare majority). Let $m_x$ be the sum of the $\mu$ smallest components of $x$, the cost to $Y$ of buying a bare majority.

*Group Y's best response* (p. 191):
- If $m_x<V_Y$: match $X$'s payments to the $\mu$ legislators with the smallest payments, and $Y$ passes.
- If $m_x>V_Y$: pay nothing, and $X$ passes.
- If $m_x=V_Y$: either action is a best response.

*Group X's choice* (pp. 191–192):
1. If $m_x<V_Y$, then $Y$ matches and bill $Y$ passes. Reducing all payments leaves the same bill passing. So the only possibly optimal such list is $(0,\dots,0)$.
2. If $m_x>V_Y$, then $Y$ pays nothing and $X$ passes. Reducing all payments a little (keeping every bare majority above $V_Y$) gives the same outcome. So no list with $m_x>V_Y$ is optimal.
3. Hence in any SPE either $x=(0,\dots,0)$ or $m_x=V_Y$.

*Which case?* (p. 192)
- To deter $Y$, $X$ must pay more than $V_Y$ to every bare majority. So it must pay each legislator more than $V_Y/\mu$, which costs more than $kV_Y/\mu$ in total.
- If $V_X<kV_Y/\mu$, $X$ is better off paying nothing.
- If $V_X>kV_Y/\mu$, $X$ pays each legislator $V_Y/\mu$, so every bare majority gets exactly $V_Y$.
- Then $Y$ is indifferent. But no SPE has $Y$ matching, since $X$ could raise payments slightly (keeping the total below $V_X$) to deter it and make $X$ pass. This is the same argument as in the ultimatum game.

*Conclusion.* For $V_X\neq kV_Y/\mu$ the SPE is unique (p. 192):
- $Y$ matches the $\mu$ smallest payments after any $x$ with $m_x<V_Y$, and pays nothing after any $x$ with $m_x\ge V_Y$.
- $X$ pays nothing if $V_X<kV_Y/\mu$, and pays each legislator $V_Y/\mu$ if $V_X>kV_Y/\mu$.
- Outcomes: for $V_X<kV_Y/\mu$, no payments are made and bill $Y$ passes. For $V_X>kV_Y/\mu$, $X$ pays $V_Y/\mu$ to each legislator, $Y$ pays nothing, and bill $X$ passes. If $V_X=kV_Y/\mu$ the analysis is more complex.
- Check against the examples (added step): $k=3$ gives $\mu=2$, so $kV_Y/\mu=450$ when $V_Y=300$ and $150$ when $V_Y=100$.

*Three features* (p. 193):
1. The outcome favours the second mover, $Y$. $X$ wins only if $V_X>kV_Y/\mu$, which is close to $2V_Y$ for large $k$. (Added step: $kV_Y/\mu=2kV_Y/(k+1)$.)
2. $Y$ never pays anything. It is ready to pay in response to some strategies of $X$, but not given $X$'s equilibrium strategy.
3. If $X$ pays anyone, it pays every legislator. If no competing group existed and each legislator needed some minimum payment, $X$ would pay only a bare majority. With $Y$ present, that would give $Y$ almost a majority that could be bought at no cost.

*Intuition note.* Because $Y$ moves last, it only has to beat $X$'s cheapest majority. To stop that, $X$ must overpay all legislators, which is expensive. So when $V_X<kV_Y/\mu$, $X$ prefers to pay nothing and give up.

Exercises 193.1–193.4 (three groups, supermajority, sequential Hotelling) follow (p. 193).

### 6.5 A race

**6.5.1 General model** (p. 194). Players alternately choose how many "steps" to take. Player $i$ starts $k_i>0$ steps from the finish line. On each turn a player takes 0 steps (cost 0), 1 step (cost $c(1)$) or 2 steps (cost $c(2)$). The first to reach the finish wins a prize worth $v_i>0$ to player $i$. The loser gets 0 (apart from costs). If neither player moves on successive turns, the game ends with no prize. $G_i(k_1,k_2)$ denotes the game where player $i$ moves first.

Formal $G_1(k_1,k_2)$ (p. 194):
- Terminal histories: sequences $(x^1,y^1,x^2,y^2,\dots,x^T)$ or $(x^1,y^1,\dots,y^T)$ with each $x^t,y^t\in\{0,1,2\}$ and no two successive 0s except possibly at the end. Either $x^1+\dots+x^T=k_1$ and $y^1+\dots+y^T<k_2$ (player 1 first), or $x^1+\dots+x^T<k_1$ and $y^1+\dots+y^T=k_2$ (player 2 first).
- Players move alternately, player 1 first.
- A loser's payoff is minus the sum of her move costs. A winner's payoff is $v_i$ minus her costs.

**6.5.2 SPE of an example** (pp. 194–199). Take $v_1,v_2$ between 6 and 7 (the exact values do not affect the equilibria), $c(1)=1$, $c(2)=4$. Since $c(2)>2c(1)$, a lone player would move one step at a time (p. 195). Subgames are games $G_i(m_1,m_2)$, or the variant that ends if the mover takes no step because the previous mover took none (p. 195).

*Small cases* (p. 195):
- $G_1(1,1)$: if player 1 steps, she wins. If she does not, player 2 steps and wins. Unique SPE: player 1 steps and wins.
- $G_1(1,2)$: if 1 does not move, 2 steps one (reaching $G_1(1,1)$, which 1 wins) or two. So 2 takes two steps and wins. Hence 1 steps once and wins.
- $G_1(2,1)$: two steps win with payoff of at least $6-4=2$. One step leads to $G_2(1,1)$, which player 2 wins. No move leads to a subgame where 2 steps and wins. So 1 takes two steps and wins.
- The author uses these cases to show how a result for small games is used for larger ones. The equilibria of $G_i(k_1,k_2)$ for all values up to $\bar k$ give the consequences of player 1's moves in $G_1(\bar k+1,\bar k)$ (p. 195).
- Exercise 195.1: $G_1(2,2)$ (first mover takes two steps and wins).

*One player far behind* (p. 196):
- When each player is at most two steps away, the first mover takes enough steps to reach the finish and wins.
- Player 1 at most two steps away and player 2 three away: player 1 takes one step. Any move by 2 leads to a subgame that player 1 (first mover) wins, so 2 does not move. Player 1 then steps again and wins. One step at a time costs her 2, versus 4 for two steps at once. For $G_1(2,3)$: 1 steps, 2 does not move, 1 steps again and wins.
- By similar arguments: if player 1 is at most two steps away and player 2 is three or more away, player 1 moves one step at a time, player 2 does not move, and 1 wins. Symmetrically for player 2.
- Figure 197.1 labels: "1" (player 1 wins, stepping one at a time, whoever moves first), "2" (likewise for player 2), "f" (the first mover takes enough steps to finish, and wins).

*Larger cases* (pp. 196–198):
- $G_1(3,3)$: one step by 1 leads to $G_2(2,3)$, labelled "1" (player 1 wins). Two steps lead to $G_2(1,3)$, also won by player 1. She prefers not to take two steps unless she must. So she steps one at a time and wins, and 2 does not move. Symmetrically in $G_2(3,3)$ player 2 wins.
- $G_i(3,4)$, $G_i(4,3)$, $G_i(4,4)$: similar. A first mover four steps away initially takes two steps. If she takes only one, the other player wins.
- $G_i(3,5)$: player 1 steps one at a time. Taking three steps costs less than $v_1$, so she is willing to run. In $G_2(3,5)$ any move by player 2 reaches a game player 1 wins, so 2 does not move. The same holds when one player is 3 or 4 steps away and the other is 5 or more.
- Figure 198.1 relabels "f" as: the first mover takes enough steps to reach the finish or the closest point labelled with her name, whichever is closer.
- *Sunk cost in $G_1(4,4)$* (p. 197). Suppose player 1 takes two steps, then player 2 deviates by taking two steps. Player 1 should still take two steps to finish. Her payoff is less than $7-4-4=-1$, but if she does not, it is $-4$, since 2 wins. Her first move's cost is sunk, so the decision depends only on options from then on.
- *Five or six steps away* (p. 198). A player initially 6 steps away is better off not moving (payoff 0) than moving two steps on any turn (negative payoff). So in $G_1(6,5)$ player 1 does not move. If she steps once, player 2 becomes first mover and steps once, moving to a game she wins. Hence the first mover wins in $G_i(5,5)$ and $G_i(6,6)$. Player 2 wins in $G_i(6,5)$, and player 1 wins in $G_i(5,6)$.
- *More than six steps away*. A player more than six steps away gets a negative payoff if she moves, even if she wins. So she does not move in any SPE, and the analysis is complete (p. 198).

Final outcomes, Figure 199.1 (rows $k_2$, columns $k_1$; labels as above) (p. 199):

| $k_2\backslash k_1$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 6 | 1 | 1 | 1 | 1 | 1 | f |
| 5 | 1 | 1 | 1 | 1 | f | 2 |
| 4 | 1 | 1 | f | f | 2 | 2 |
| 3 | 1 | 1 | f | f | 2 | 2 |
| 2 | f | f | 2 | 2 | 2 | 2 |
| 1 | f | f | 2 | 2 | 2 | 2 |

The figure also shows the steps taken when player 1 moves first (p. 198).

*Intuition note.* Backward induction works along a grid of positions. A player close enough to win can scare the other into quitting, because any pursuit just means losing and paying costs. Only when the two are close does the first mover need to rush.

Exercises 198.1 (different valuations), 198.2 (removing stones), 199.1 (hungry lions) are posed in the text (pp. 198–199).

**6.5.3 General lessons** (pp. 199–200).
- *Threats.* Each player's equilibrium strategy involves a "threat" to speed up if the other deviates. In $G_1(3,3)$, player 1's equilibrium debt reaches 3 (three single steps). If after her first step player 2 deviates and steps, player 1's strategy has her take two steps, and her debt reaches 5. If her debt could never exceed 3, her strategy could not embody such threats. A limit on debt may affect the outcome even if it exceeds the debt along the equilibrium path (pp. 199–200). Exercise 200.1 gives a debt limit of 3.
- *Only one player moves.* In SPE of every $G_i(k_1,k_2)$ only one player moves and her opponent "gives up". The author says this holds in more general games. An added ingredient that might make both active is a player's uncertainty about the other's characteristics, for instance the cost of the opponent's moves. This requires imperfect information, treated in Chapter 10 (p. 200).
- *Competitor's effect on speed.* A lone player would move one step at a time. With two players, for most starting points the moving player keeps that leisurely pace. Only for a small number of starting points, with similar initial distances, does the competitor induce a faster pace, and only in the first period (p. 200).

**Notes** (p. 200). The author attributes: the first ultimatum experiment to Güth, Schmittberger and Schwarze (1982); an early holdup analysis to Grout (1984); the model of 6.3 to von Stackelberg (1934); the vote-buying game to Groseclose and Snyder (1996); and the race (a simplification suggested by Vijay Krishna) to Harris and Vickers (1985). He also lists further reading on experiments (Roth 1995), equity-consciousness (Bolton and Ockenfels 2000), rules of thumb (Aumann 1997), and fair division (Brams and Taylor 1996).

## Toy example (ours, not from the text)
Stackelberg duopoly with $\alpha=9$, $c=1$ (so $\alpha-c=8$), using the linear model of (185.2).
1. Firm 2's best response: $b_2(q_1)=\tfrac12(8-q_1)$.
2. Firm 1 maximizes $\tfrac12 q_1(8-q_1)$. It is zero at 0 and 8, so the maximizer is $q_1^*=4$. Then $q_2^*=\tfrac12(8-4)=2$.
3. Price: $P=9-(4+2)=3$. Profit of firm 1: $4(3-1)=8=\tfrac18\cdot 64$. Profit of firm 2: $2(3-1)=4=\tfrac1{16}\cdot 64$.
4. Cournot: each produces $\tfrac13\cdot 8=\tfrac83$. The price is $9-\tfrac{16}{3}=\tfrac{11}{3}$. Each profit is $\tfrac83(\tfrac{11}{3}-1)=\tfrac{64}{9}\approx 7.11$. So the leader earns $8>7.11$, and the follower earns $4<7.11$.
5. Check a deviation. If $q_1=3$, then $b_2=2.5$, $P=9-5.5=3.5$, and profit is $3(3.5-1)=7.5<8$. If $q_1=5$, then $b_2=1.5$, $P=9-6.5=2.5$, and profit is $5(2.5-1)=7.5<8$.
6. Commitment: if firm 1 could re-choose after firm 2, the first stage would be irrelevant. Firm 2 would play $(\alpha-c)/2=4$ and firm 1 $(\alpha-c)/4=2$ (p. 189). Then $P=9-6=3$ and firm 1 earns $2(3-1)=4<\tfrac{64}{9}$. Firm 1 is worse off than in the Cournot equilibrium.

## Concepts
- [[subgame-perfect-equilibrium]] — a strategy profile that is optimal in every subgame; here found by backward induction in finite-horizon games (pp. 180, 185, 194)
- [[backward-induction]] — solve the last decisions first, then earlier ones given those answers; used in all the applications (pp. 180, 185, 191, 195)
- [[extensive-form-game]] — here specified by players, terminal histories, player function and preferences (p. 179)
- [[nash-equilibrium]] — used as the benchmark: Cournot's simultaneous-move outcome vs. Stackelberg SPE (p. 186)
- [[best-response]] — firm 2's $b_2(q_1)$ and group $Y$'s reply to $x$ are best responses in subgames (pp. 185, 191)
- [[credible-commitment]] — Osborne's wording: firm 1 "prefers to be committed not to change its mind"; the value of commitment is shown by adding a third stage (p. 189)
- [[social-preferences]] — equity-conscious payoffs $x_i-\beta_i|x_1-x_2|$ as one explanation for ultimatum-game data (pp. 181–182)
- [[heuristic]] — "rules of thumb" that work in repeated interactions, offered as another explanation (p. 182)
- [[repeated-interaction-reputation]] (new) — the claim that daily-life repeated play makes it advantageous to punish paltry offers and build a reputation (p. 182)
- [[ultimatum-game]] (new) — proposer offers a split, responder accepts or rejects; rejection gives both nothing (p. 179)
- [[holdup-problem]] (new) — a player exerts costly effort before bargaining and may be "held up" for the whole surplus, so under-invests (pp. 183–184)
- [[stackelberg-duopoly]] (new) — sequential quantity competition: leader chooses an output, follower observes it (p. 184)
- [[sunk-cost-in-equilibrium]] (new) — past move costs are ignored; a player's decision depends only on options from then on (p. 197)

## Canonical instances
- [[ultimatum-game]] — unique SPE: offer 0, accept all; experiments differ (pp. 179–182)
- [[dictator-game-impunity-game]] — variants where player 2 cannot reject or player 1 is paid $c-x$ on rejection (pp. 180–181, Exercise 180.3)
- [[holdup-game]] — under-investment in SPE regardless of pie sizes (pp. 183–184)
- [[stackelberg-duopoly-game]] — leader produces $\tfrac12(\alpha-c)$, follower $\tfrac14(\alpha-c)$ in the linear example (pp. 184–186)
- [[vote-buying-game]] — outcome depends on $V_X$ vs. $kV_Y/\mu$ (pp. 189–193)
- [[race-game]] — one active player; threats to speed up; sunk costs (pp. 194–200)
- [[divide-and-choose]] — cake-cutting exercise (p. 183, Exercise 183.2)

## Bridges (candidates)
- [structural-analogy] Stackelberg first mover choosing the best point on the follower's reaction curve ↔ credible commitment: limiting one's own options changes the other's expectations — firm 1 gains by being unable to change its output.
- [structural-analogy] The "no optimal offer" argument (ultimatum rejection of 0; Stackelberg with fixed cost; vote-buying) ↔ open-set best-response problems — no smallest output or amount above a threshold.
- [metaphor] Holdup problem ↔ under-investment when the benefits of effort will be shared away; the text states only the specific game.
- [structural-analogy] Rejections of low offers explained by rules of thumb ↔ heuristic / bounded rationality: behaviour tuned to repeated environments is applied to one-shot games.

## Questions this raises
- If person 2 can make counteroffers (Chapter 16), how does the equilibrium split move away from the one-sided ultimatum outcome?
- How does uncertainty about a rival's costs or equity concern (imperfect information, Chapter 10) produce a race in which both players are active, or rejections of positive offers?
- What happens in the vote-buying game exactly at $V_X=kV_Y/\mu$, which the author calls "more complex"?
- Which of the two ultimatum explanations (preferences vs. rules of thumb) does new evidence favour? The text says current evidence fits both.

## Exercises worth doing
- Ex. 180.2 (p. 180) — SPE of the ultimatum game when money comes in cents; shows how discreteness gives "best" offers — difficulty: easy
- Ex. 181.1 (p. 181) — equity-conscious players in the ultimatum and impunity games; tests whether offers get rejected in equilibrium — difficulty: hard
- Ex. 186.1 (p. 186) — Stackelberg with quadratic costs; practice with the leader's maximization — difficulty: medium
- Ex. 198.2 (p. 198) — removing stones; backward induction on the pile size — difficulty: medium
- Ex. 199.1 (p. 199) — hungry lions; backward induction over $n$ players — difficulty: hard
- Ex. 200.1 (p. 200) — the race $G_1(3,3)$ with a debt limit; shows how threats depend on the ability to borrow — difficulty: medium

## Reading notes
- Source is a draft chapter (version 00/11/6, copyright 1995–2000 Osborne, as printed on pdf 188), not the published book. Printed page = pdf page − 9.
- The chapter refers to material outside this unit: Chapters 10, 14, 16; Exercises 57.2, 57.3, 175.2a, 222.2; Sections 3.1–3.3.
- Misprint, p. 186 (image): firm 2's profit is written as $q_1^*(P(q_1^*+q_2^*)-c)=\tfrac1{16}(\alpha-c)^2$. It should read $q_2^*$ (firm 1's version equals $\tfrac18$).
- Text-layer error, p. 192: the layer reads "if $V_X = kV_Y/\mu$ then the game has a unique SPE". The image shows $\neq$ (the equality case is "more complex").
- Page images were not provided for pdf 188 and 191–193 and 209. For those pages the text layer alone was used. On p. 183, the primes and subset symbols in Exercise 183.2b were not recoverable, so that exercise is not summarized in detail.
- Statements about the results of Exercise 181.1 (equity-conscious equilibria) are the author's remarks on p. 182; they were not re-derived here.
