---
id: osborne-2004-introduction/ch04-mixed-p2
work: osborne-2004-introduction
unit: "4 Mixed Strategy Equilibrium (part 2/2): §§4.7–4.12 and Notes"
pages: 125-149
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Mixed equilibrium in a single population, crime reporting, belief formation, finding all equilibria, continuum actions, and expected payoffs

## L0 — One line
In a mixed strategy equilibrium each player is indifferent among the actions she uses, and the author uses this characterization to derive the "larger group, less help" result, to search for all equilibria, and to restate the equilibrium test for continuum games; mixed equilibria also model stochastic steady states.

## L1 — The gist (≤ 120 words)
This part of Chapter 4 applies mixed equilibrium in new settings. Every game in which players share one finite action set has a symmetric mixed equilibrium. In the symmetric mixed equilibrium of the crime-reporting game, a larger group is less likely to produce any call, because indifference fixes the chance that no one else calls. Best-response dynamics and fictitious play are simple learning models of how players may reach equilibrium. In principle, all mixed equilibria can be found by checking every choice of action subsets. With a continuum of actions, strategies become cumulative distributions, as in the all-pay auction. An appendix states that Bernoulli payoffs (numbers whose expected value ranks lotteries) are fixed only up to increasing linear transformations.

**Prerequisites:** Nash equilibrium and best response in two-player tables; probability of independent events; the characterization of mixed equilibrium from earlier in the chapter (Prop. 113.2, restated on p. 139); cumulative distribution functions.

## L2 — Key ideas (5–10 bullets)
- A symmetric mixed equilibrium (every player uses the same mixed strategy) models a stochastic steady state in one population. Every game with expected-payoff (vNM) preferences and one common finite action set has one (Prop. 127.1, stated without proof). (pp. 126–127)
- In the crime-reporting game there is no symmetric pure equilibrium but a unique symmetric mixed one, $p = 1-(c/v)^{1/(n-1)}$. (pp. 128–129)
- In that equilibrium the probability that anyone calls falls as the group grows, even though each person's cost and benefit are fixed. The author argues that the equilibrium (indifference) condition together with the laws of probability produces this, so the socio-psychological factors are not needed to explain it. (pp. 129–131)
- Players may reach equilibrium by eliminating dominated actions, by best-response dynamics (can cycle, e.g. in BoS) or by fictitious play (converges in some classes of games). (pp. 131–134)
- To find all mixed equilibria, check each combination of action subsets against the equality and no-better-action conditions. The number of cases grows fast. (pp. 135–138)
- The equilibrium test is restated as Prop. 140.1 so that it fits continuum games; in games with interval action sets a mixed strategy is a cumulative distribution. The all-pay auction has a uniform-bidding equilibrium with payoff 0. (pp. 139–143)
- Lemma 145.1 (at least three outcomes; only the "if" half is proved) says two Bernoulli payoff functions represent the same preferences over lotteries iff one equals $\eta+\theta$ times the other plus a constant with $\theta>0$. A merely increasing transformation (e.g. $\sqrt u$) need not preserve them. (pp. 144–147)

## L3 — Walkthrough

### End of §4.6 (p. 125)
The first lines finish the comparative-statics discussion of the expert-diagnosis model of §4.6 (defined before these pages). A change that makes it harder for an expert to claim fraudulently that she did a major repair raises $q^*$. Consumers then become less wary, and experts have less to gain from dishonesty. (p. 125)

Two exercises (125.1 incompetent experts; 125.2 choosing a seller) are listed below.

### 4.7 Equilibrium in a single population (pp. 125–128)
§2.10 treated deterministic steady states; this section treats *stochastic* steady states in a single population. (p. 125)

**Definition 126.1 (symmetric two-player game with vNM preferences).** A game with vNM preferences (preferences given by expected values of payoffs) is symmetric if both players have the same action set and their payoff functions satisfy
$u_1(a_1,a_2)=u_2(a_2,a_1)$ for every action pair $(a_1,a_2)$. (p. 126)

**Definition 126.2 (symmetric mixed strategy Nash equilibrium).** In a game with vNM preferences where every player has the same action set, a profile $\alpha^*$ is a symmetric mixed strategy Nash equilibrium if it is a mixed strategy Nash equilibrium and $\alpha_i^*$ is the same for every player $i$. It is defined for any number of players. (p. 126)

**Approaching pedestrians (Fig. 126.1).** Payoffs: $(Left,Left)=(1,1)$, $(Right,Right)=(1,1)$, mismatches $(0,0)$. Besides the two pure symmetric equilibria (two deterministic steady states), there is a symmetric mixed equilibrium with probability $\tfrac12$ on each action. It corresponds to a steady state in which half of all encounters are collisions: probability $\tfrac14$ for (Left, Right) and $\tfrac14$ for (Right, Left). (p. 126)

**Fig. 127.1** is symmetric, but players prefer *different* actions: $(X,X)=(0,0)$, $(X,Y)=(1,1)$, $(Y,X)=(1,1)$, $(Y,Y)=(0,0)$. It has no symmetric pure equilibrium but has a symmetric mixed one with probability $\tfrac12$ on each action. (pp. 126–127)

**Proposition 127.1 (existence).** Every strategic game with vNM preferences in which each player has the same finite set of actions has a symmetric mixed strategy Nash equilibrium. The proof needs relatively advanced tools and is not given. (p. 127)

*Intuition note.* A symmetric game can lack a symmetric equilibrium in pure strategies, but in the two examples (and, by Prop. 127.1, in any finite game with a common action set) a symmetric mixed equilibrium exists. In the pedestrian example it is read as a steady state in which half of all encounters are collisions. For the game of Exercise 127.2 the author remarks that its equilibrium may attractively be read as some members always choosing one action and others always the other. (pp. 126–127)

### 4.8 Illustration: reporting a crime (pp. 128–131)
**Model.** $n$ people see a crime. Each gets $v$ if the police are informed and pays $c$ if she herself calls, with $v>c>0$. Payoffs: $0$ if no one calls; $v-c$ if she calls; $v$ if at least one other person calls and she does not. Actions: Call, Don't call. (p. 128)

**Pure equilibria.** There are $n$ asymmetric pure equilibria, each with exactly one caller. If the caller stops, her payoff falls from $v-c$ to $0$. If a non-caller starts, her payoff falls from $v$ to $v-c$. If the group differs in some way, such an equilibrium can be a steady state (e.g. "the oldest person calls"). (p. 128)

If people are drawn from a single homogeneous population and cannot coordinate, a symmetric equilibrium is more compelling (author's view). There is no symmetric pure equilibrium: if everyone calls, each prefers not to call; if no one calls, each prefers to call. (p. 128)

**Symmetric mixed equilibrium.** Suppose each person calls with probability in $(0,1)$. Then calling and not calling must have equal expected payoff. Calling pays $v-c$. Not calling pays $0$ if no one else calls and $v$ otherwise:
$$v-c = 0\cdot\Pr\{\text{no one else calls}\}+v\cdot\Pr\{\text{at least one other calls}\} = v\,(1-\Pr\{\text{no one else calls}\}),$$
$$\frac{c}{v}=\Pr\{\text{no one else calls}\}. \tag{129.1}$$
With $p$ the common probability of calling, $\Pr\{\text{no one else calls}\}=(1-p)^{n-1}$, so $c/v=(1-p)^{n-1}$ and
$$p = 1-(c/v)^{1/(n-1)}.$$
This lies between 0 and 1, so the game has a *unique* symmetric mixed equilibrium. (p. 129)

**Comparative statics in $n$.**
- As $n$ rises, $1/(n-1)$ falls, so $(c/v)^{1/(n-1)}$ rises and $p$ falls. (p. 129)
- "No one calls" equals "$i$ does not call and no one other than $i$ calls", so
$$\Pr\{\text{no one calls}\}=\Pr\{i\text{ does not call}\}\cdot\Pr\{\text{no one else calls}\}. \tag{129.2}$$
- The first factor rises with $n$. By (129.1) the second equals $c/v$, independent of $n$. So $\Pr\{\text{no one calls}\}$ rises with $n$: the larger the group, the *less* likely the police are informed. (p. 129)

The result that each person calls less is unsurprising. That *at least one* person calls is less likely is a subtler implication of equilibrium. Individuals care no less in a larger group, yet the steady-state behavior lowers the chance of notification. (p. 129)

*Intuition note.* Each person must be indifferent, which pins "nobody else calls" at $c/v$ whatever $n$ is. By (129.2), Pr{no one calls} = Pr{i does not call} × c/v; the second factor stays at c/v while the first rises with $n$, so everyone-silent becomes likelier. (p. 129)

**Box: social psychology and game theory (p. 130–131).** Thirty-eight people witnessed the murder of Kitty Genovese in March 1964 and none significantly responded; some commentators blamed big-city apathy. Experiments suggest people are not generally apathetic. A lone witness is very likely to help, but as the group grows both the probability that a given person helps and the probability that at least one helps decline. (p. 130)

*Social psychologists' hypotheses* (three factors): "diffusion of responsibility" (lower psychological cost of not helping in a large group); "audience inhibition" (more embarrassment if help turns out inappropriate); "social influence" (others' inaction suggests help is inappropriate). In the model these raise the expected cost and/or reduce the expected benefit. (p. 130)

*Osborne's view:* these factors are plausible but not needed, since the equilibrium analysis implies the decline even with cost and benefit independent of group size. The game analysis derives it from the same principles as other models (oligopoly, auctions, voting). He says the missing element in the socio-psychological analysis is the notion of equilibrium. (pp. 130–131)

Exercise 130.1 extends the model to $k\ge2$ (listed below). It uses $Q_{n-1,m}(p)$, the probability that exactly $m$ of $n-1$ players contribute. (p. 130)

### 4.9 The formation of players' beliefs (pp. 131–134)
**Population story.** Nash equilibrium assumes players know others' strategies. The analysis so far reads this as learned from experience: each role has a large population, and one member of each is drawn for each play. A newcomer to a steady-state population can learn others' strategies by observation, provided turnover is small enough that newcomers' non-equilibrium play is rare. The open question is what happens if many newcomers join several populations at once. (p. 131)

**4.9.1 Eliminating dominated actions.** In some games players may reach equilibrium actions by introspection.
- In the Prisoner's Dilemma each player's best action does not depend on the others' (p. 131).
- In **Fig. 132.1** (rows T, B; columns L, R; payoffs T: $(1,2),(0,3)$; B: $(0,0),(1,1)$), R strictly dominates L for player 2. Player 1, deducing that player 2 plays R, chooses B. This gives the unique equilibrium $(B,R)$. (pp. 131–132)
- In **Fig. 132.2** (T: $(0,2),(0,0)$; M: $(2,1),(1,2)$; B: $(1,1),(2,2)$), T is strictly dominated for player 1. Player 1 reasons that player 2 will deduce this and play R, so she chooses B rather than M. (p. 132)

The profiles surviving such reasoning include all Nash equilibria. Often many others also survive, and in many games none is eliminated because no action is strictly dominated. In some classes of games the process is powerful (Chapter 12). (p. 132)

**4.9.2 Learning.** Players start with an unexplained "prior" belief and revise it from observation, discussion, or own experience. Two theories are given, in which the same participants repeatedly play. (p. 132)

*Best response dynamics.* In period 1 each player best-responds to an arbitrary deterministic belief. In each later period each best-responds to the others' actions in the previous period. An action profile that stays the same from period to period is a pure Nash equilibrium. A pure equilibrium in which each player's action is her *only* best response to the others' actions does stay the same. (pp. 132–133)
- It converges from any initial beliefs in Cournot's duopoly (§3.1.3); the best-response functions of Fig. 56.2 let you see this. (p. 133)
- In BoS, if player 1 initially believes player 2 chooses Stravinsky and player 2 believes player 1 chooses Bach, play alternates forever between (Bach, Stravinsky) and (Stravinsky, Bach). This example highlights the limited reasoning the model assumes: it does not consider the possibility that a player notices that her opponent's action is always a best response to her own previous action. (p. 133)

*Fictitious play.* Under best-response dynamics beliefs are continually revealed to be wrong unless the starting point is a Nash equilibrium, and each player believes the others use pure strategies. In fictitious play each player starts with an arbitrary probabilistic belief and best-responds to it. Afterwards she believes the opponent mixes with probabilities proportional to the frequencies of its past actions. Example: if in six periods player 2 chose A twice, B three times, C once, player 1's period-7 belief is $\tfrac13,\tfrac12,\tfrac16$. (pp. 133–134)

*Matching Pennies (Fig. 134.1): Head/Head $=(1,-1)$, Head/Tail $=(-1,1)$, Tail/Head $=(-1,1)$, Tail/Tail $=(1,-1)$.* Start: player 1 believes Tail, player 2 believes Head. Period 1: both choose Tail. Period 2: both believe Tail, so player 1 chooses Tail and player 2 chooses Head. Period 3: player 1 believes Head and Tail each with probability $\tfrac12$, so both her actions are best responses. Player 2 believes Tail for sure and chooses Head. (p. 134)

*Convergence.* In two-player games with directly opposed interests, and in any two-player game with two actions per player, the process converges to a mixed equilibrium from any initial beliefs. That is, the frequencies of play approach the equilibrium frequencies. For other games some initial beliefs give no convergence, and the simplest example is "too complicated to present compactly." (p. 134)

The models explore two ways of drawing inferences from opponents' actions. More sophisticated models may say more about when equilibrium is attained, an active research area. (p. 134)

### 4.10 Extension: finding all mixed strategy Nash equilibria (pp. 135–138)
For two players with two actions each, best-response functions suffice; in larger games this is usually impractical. The systematic method is suggested by the characterization in Prop. 113.2 (as restated on p. 139: (a) every action with positive probability gives the same expected payoff; (b) no action gives more):
1. For each player $i$ choose a subset $S_i\subseteq A_i$.
2. Look for a profile $\alpha$ where the actions with positive probability in $\alpha_i$ are exactly $S_i$, and where $\alpha$ satisfies the conditions of Prop. 113.2.
3. Repeat for every collection of subsets. (p. 135)

**Example 135.1 (2×2 game, payoffs $u_{ij},v_{ij}$ as in Fig. 136.1).** Each player has three nonempty subsets, so $3\times3=9$ pairs. (p. 135)
- The four single-action pairs amount to checking the four pure profiles. (p. 135)
- For $\{T,B\}$ and $\{L\}$, with $p=\Pr(T)$: need $u_{11}=u_{21}$ (player 1's two payoffs equal) and $pv_{11}+(1-p)v_{21}\ge pv_{12}+(1-p)v_{22}$ (L at least as good as R). If $u_{11}\ne u_{21}$, or no $p$ satisfies the inequality, there is no equilibrium of this type. The other three "one mixes, one pure" pairs are similar. (pp. 135–136)
- For $\{T,B\}$ and $\{L,R\}$, with $p=\Pr(T)$ and $q=\Pr(L)$, we need
$$qu_{11}+(1-q)u_{12}=qu_{21}+(1-q)u_{22}\quad\text{and}\quad pv_{11}+(1-p)v_{21}=pv_{12}+(1-p)v_{22}.$$
(p. 136)
- In BoS: the single-action pairs give the two pure equilibria; mixed/single pairs give none; $(\{B,S\},\{B,S\})$ gives the mixed equilibrium. (p. 136)

With two actions per player, at most one condition matters per subset (equality if the subset has both actions, no-better-action if it has one). With three or more actions and a two-action subset, both matter. (p. 136)

**Example 136.2 (variant of BoS, Fig. 137.1).** Player 1 chooses row B or S; player 2 chooses column B, S or X. Payoffs: (B,B) $=(4,2)$, (B,S) $=(0,0)$, (B,X) $=(0,1)$, (S,B) $=(0,0)$, (S,S) $=(2,4)$, (S,X) $=(1,3)$. (p. 137)
- Pure equilibria by inspection: $(B,B)$ and $(S,S)$. (p. 136)
- *Player 1 pure, player 2 using two or more actions.* If player 1 plays B, player 2's payoffs to her three actions (2, 0, 1) all differ, so no equality is possible. Similar reasoning rules out player 1 playing S and the case with player 2 pure and player 1 mixing. (pp. 136–137)
- *Both of player 1's actions used; player 2 uses two of three.* Let $p=\Pr(B)$.
  - *B and S:* need $2p=4(1-p)\ge p+3(1-p)$. The equation gives $p=\tfrac23$, which violates the inequality (X pays more). No equilibrium. (p. 137)
  - *B and X:* need $2p=p+3(1-p)\ge4(1-p)$. The equation gives $p=\tfrac34$, which satisfies the inequality. Player 1 must be indifferent: $4q=1-q$, where $q=\Pr$(player 2 plays B), so $q=\tfrac15$. Equilibrium: $\big((\tfrac34,\tfrac14),(\tfrac15,0,\tfrac45)\big)$. (p. 137)
  - *S and X:* for every strategy of player 2 on S and X only, player 1's payoff to S exceeds that to B. No equilibrium. (p. 137)
- *All three of player 2's actions used.* Need $2p=4(1-p)=p+3(1-p)$. The first equality needs $p=\tfrac23$, which violates the second. No equilibrium. (pp. 137–138)
- **Conclusion:** three equilibria: $((1,0),(1,0,0))$, $((0,1),(0,1,0))$ and $\big((\tfrac34,\tfrac14),(\tfrac15,0,\tfrac45)\big)$. (p. 138)

*Intuition note.* Guess which actions are used, impose equal payoffs on them, then check that unused actions are not better. Wrong guesses fail at the inequality or at the equality, as with B-and-S above. (pp. 135–138)

**Cost of the method.** With three actions each there are 7 nonempty subsets per player, so $7\times7=49$ collections. In symmetric games many cases repeat the same argument. (p. 138)

Exercises 136.1, 138.1, 138.2 (Rock, paper, scissors), 139.1 (Election campaigns), 139.2 (three-player game, one table per action of player 3) ask for mixed equilibria of further games; only 136.1 and 138.1 explicitly say to use the method above. (pp. 136–139)

### 4.11 Extension: continuum of actions (pp. 139–143)
Prop. 113.2 (a) does not fit here, since a mixed strategy is given by probabilities of *sets* of actions, which may all be zero for single actions. (pp. 139–140)

**Proposition 140.1 (characterization).** A mixed strategy profile $\alpha^*$ in a strategic game with vNM preferences is a mixed strategy Nash equilibrium if and only if, for each player $i$:
- $\alpha_i^*$ assigns probability zero to the set of actions $a_i$ for which $(a_i,\alpha^*_{-i})$ gives $i$ an expected payoff less than her expected payoff to $\alpha^*$; and
- no action $a_i$ gives $(a_i,\alpha^*_{-i})$ an expected payoff greater than her expected payoff to $\alpha^*$. (p. 140)

This restatement is equivalent to Prop. 113.2 when action sets are finite. (p. 140)

**Interval games.** Player $i$'s action set is an interval; a mixed strategy is a cumulative distribution $F_i$ (nondecreasing, $0\le F_i\le1$, $F_i(a_i)=\Pr$(action $\le a_i$)). Suppose, for $i=1,2$:
- there are $x_i,y_i$ with $F_i(z)=0$ for $z<x_i$ and $F_i(z)=1$ for $z\ge y_i$;
- $i$'s expected payoff from $a_i$ against $F_j$ equals a constant $c_i$ for $x_i\le a_i\le y_i$, and is $\le c_i$ for $a_i<x_i$ or $a_i>y_i$ (Fig. 141.1).

By Prop. 140.1, such a pair is a mixed equilibrium with payoff $c_i$ for each $i$. (p. 140) The author warns that this example is simple, that in most such games the analysis of equilibria is at a minimum somewhat more complex, and that he finds one equilibrium without studying all. (pp. 140–141)

**Example 141.1 (all-pay auction).** Two bidders value an object at $\$K$. Bids are numbers in $[0,K]$. The higher bid wins; a tie gives each half the object (worth $K/2$). Both pay their bids. Payoff to $i$:
$$u_i(a_1,a_2)=\begin{cases}-a_i & a_i<a_j\\ K/2-a_i & a_i=a_j\\ K-a_i & a_i>a_j.\end{cases}$$
Uses: lobbying, or two firms racing to develop a product. (p. 141)

*No pure equilibrium.* (a) $(x,x)$ with $x<K$: either player gains by slightly raising her bid. (b) $(K,K)$: either can raise her payoff from $-K/2$ to $0$ by bidding 0. (c) $a_1\ne a_2$: the higher bidder can lower her bid; the lower bidder, if her bid is positive, can lower it to 0. (p. 142)

*Mixed equilibrium.* Look for $F_1,F_2$ with no positive probability on any single bid (so $F_i(a_i)$ is both $\Pr(\le a_i)$ and $\Pr(<a_i)$), and with $F_i$ positive only on $[x_i,y_i]$. Player 1's expected payoff from $a_1$ against $F_2$: (p. 142)
- $-a_1$ if $a_1<x_2$;
- $K-a_1$ if $a_1>y_2$;
- for $x_2\le a_1\le y_2$:
$$(K-a_1)F_2(a_1)+(-a_1)(1-F_2(a_1))=KF_2(a_1)-a_1$$
(added step: the $a_1F_2$ terms cancel).

Need $KF_2(a_1)-a_1=c_1$ on $[x_1,y_1]$, with $F_2(x_2)=0$, $F_2(y_2)=1$, $F_2$ nondecreasing, and analogous conditions for player 2. All hold for $x_i=0$, $y_i=K$, $F_i(z)=z/K$ on $[0,K]$. Each player's expected payoff is $0$ for every action. (p. 142)

*Conclusion:* both randomize "uniformly" over all bids, with expected payoff $0$ (on average a player spends exactly the object's value). A more involved argument, not given, shows this is the only mixed equilibrium. (p. 143)

*Intuition note.* Because $F_2(a_1)=a_1/K$ is exactly the chance that a bid of $a_1$ wins, expected winnings $K\cdot a_1/K=a_1$ cancel the bid, so every bid yields 0. (p. 142–143)

In these examples, payoff depends on the other's action only via greater than, equal to or less than, which makes expected payoff easy to compute. Games with stronger dependence need more sophisticated tools. (p. 143) Exercises 143.1 (many bidders) and 143.2 (Bertrand duopoly) follow. (p. 143)

### 4.12 Appendix: representing preferences by expected payoffs (pp. 143–148)
**4.12.1 Expected payoffs.** Given preferences over lotteries (probability distributions over $K$ outcomes), under fairly weak assumptions a payoff function $U(p_1,\dots,p_K)$ represents them. (pp. 143–144) The standard approach of von Neumann and Morgenstern adds the "independence axiom" (not described here), which implies that there is a payoff function $u$ over *deterministic* outcomes with
$$\sum_{k=1}^K p_k u(a_k) > \sum_{k=1}^K p'_k u(a_k) \tag{144.1}$$
if and only if the lottery $(p_1,\dots,p_K)$ is preferred to $(p'_1,\dots,p'_K)$. The function $u$ is the **Bernoulli payoff function**. (p. 144)

*Example (outcomes $\$0,\$1,\$5$; lottery entries are probabilities of $0,1,5$).* Prefer $(\tfrac12,0,\tfrac12)$ to $(0,\tfrac34,\tfrac14)$. This is consistent with $u(0)=0$, $u(1)=1$, $u(5)=4$, since $\tfrac12\cdot0+\tfrac12\cdot4>\tfrac34\cdot1+\tfrac14\cdot4$. Among functions with $u(0)=0$, $u(5)=4$, any with $u(1)<\tfrac43$ works. The opposite preference is consistent with $u(1)=3$: $\tfrac12\cdot0+\tfrac12\cdot4<\tfrac34\cdot3+\tfrac14\cdot4$. (p. 144)

*Bernoulli vs. ordinal payoffs.* Preferences by expected Bernoulli payoff are fully specified by $u$. If lottery preferences are represented by the expected value of $u$, then $u$ also represents the ranking of deterministic outcomes (they are lotteries with probability 1). The converse fails. With $\$5\succ\$1\succ\$0$ and $(\tfrac12,0,\tfrac12)\succ(0,\tfrac34,\tfrac14)$, the function $u(0)=0$, $u(1)=3$, $u(5)=4$ fits the deterministic ranking but gives $\tfrac12\cdot0+\tfrac12\cdot4<\tfrac34\cdot3+\tfrac14\cdot4$, the wrong lottery ranking. Moral: know which type of payoff function you have. (p. 145)

Exercise 144.2 tests consistency of lottery rankings with expected payoff. (pp. 144–145)

**4.12.2 Equivalent Bernoulli payoff functions.** Any increasing transformation of an ordinal payoff function still represents the same deterministic preferences, but the analogous property fails for Bernoulli payoff functions. With $u(0)=0$, $u(1)=1$, $u(5)=4$, the function $\sqrt u$ has values $0,1,2$ and gives $\tfrac12\cdot0+\tfrac12\cdot2<\tfrac34\cdot1+\tfrac14\cdot2$, contradicting the preference for $(\tfrac12,0,\tfrac12)$. (p. 145)

**Lemma 145.1.** Suppose there are at least three possible outcomes. The expected values of Bernoulli payoff functions $u$ and $v$ represent the same preferences over lotteries if and only if there are numbers $\eta$ and $\theta>0$ with $u(x)=\eta+\theta v(x)$ for all $x$. (p. 145)

So $2u$, $1+u$, $-1+4u$ work; $u^2$ and $\sqrt u$ do not. (p. 146)

*Proof of the "if" part (given).* Let $v=\eta+\theta u$, $\theta>0$. Suppose $(p_k)$ is preferred to $(p'_k)$, i.e.
$$\sum_k p_k u(a_k) > \sum_k p'_k u(a_k). \tag{146.1}$$
Since $\sum_k p_k=1$,
$$\sum_k p_kv(a_k)=\sum_k p_k\eta+\sum_k p_k\theta u(a_k)=\eta+\theta\sum_k p_ku(a_k),$$
and likewise for $p'_k$. Substituting for $u$ in (146.1) gives
$$\Big(\sum_k p_kv(a_k)-\eta\Big)/\theta>\Big(\sum_k p'_kv(a_k)-\eta\Big)/\theta,$$
which, as $\theta>0$, is equivalent to $\sum_k p_kv(a_k)>\sum_k p'_kv(a_k)$. So $v$ represents the same preferences. The harder "only if" argument is omitted. (p. 146)

*Intuition note.* Adding a constant or rescaling by a positive number changes only the unit and zero point of the payoff scale. A curved transformation can flip rankings of gambles, as the square-root example on p. 145 shows. (pp. 145–146)

Exercise 146.2 asks for the normalization to payoff 1 (best) and 0 (worst). (p. 146)

**4.12.3 Equivalent strategic games with vNM preferences.** Fig. 147.1 gives three BoS-type tables (rows and columns B, S):
- left: $(2,1),(0,0),(0,0),(1,2)$;
- middle: $(4,0),(0,-3),(0,-3),(2,3)$;
- right: $(3,2),(0,1),(0,1),(1,4)$.

All three represent the same game with ordinal preferences. Only left and middle represent the same game with vNM preferences, because $v_1=2u_1$ and $v_2=-3+3u_2$. For the right table, $w_1=\eta+\theta u_1$ would require $0=\eta+\theta\cdot0$, $1=\eta+\theta\cdot1$, $3=\eta+\theta\cdot2$, which have no solution. One player's preferences differing is enough for non-equivalence. Another check: in the left table player 1 is indifferent between the sure outcome $(S,S)$ and the lottery giving $(B,B)$ or $(S,B)$ with probability $\tfrac12$ each (both worth 1), but in the right table she prefers the lottery (1.5 vs 1). (p. 147)

Exercise 147.1 uses Fig. 148.1 (Prisoner's Dilemma equivalence). (pp. 147–148)

### Notes (pp. 148–149)
The author attributes: the modern formulation of mixed strategies to Borel; expected-payoff representation to von Neumann and Morgenstern (1944); mixed Nash equilibrium and the finite-game existence result (Prop. 116.1) to Nash; Prop. 119.2 as an implication of Selten's trembling-hand perfect equilibrium; the §4.8 model to Palfrey and Rosenthal (1984) with the interpretation from an unpublished 1984 Samuelson paper; best response dynamics first studied by Cournot (1838); fictitious play suggested by Brown (1951). Robinson (1951) shows that fictitious play converges to a mixed equilibrium in any two-player game with opposed interests; Shapley (1964, Section 5) exhibits a game outside this class where it does not converge. The all-pay-auction exercise rests on Baye, Kovenock and de Vries (1996). The author says the §4.10 method is computationally intense in all but the simplest games and mentions the program GAMBIT. (pp. 148–149)

## Toy example (ours)
Crime game with $v=8$, $c=2$, so $c/v=\tfrac14$. Equilibrium $p=1-(1/4)^{1/(n-1)}$ (p. 129).

| $n$ | $(1/4)^{1/(n-1)}$ | $p$ | $\Pr\{\text{no one calls}\}=(1-p)\cdot\tfrac14$ |
|---|---|---|---|
| 2 | $1/4$ | $3/4$ | $\tfrac14\cdot\tfrac14=0.0625$ |
| 3 | $1/2$ | $1/2$ | $\tfrac12\cdot\tfrac14=0.125$ |
| 5 | $(1/4)^{1/4}\approx0.7071$ | $\approx0.2929$ | $0.7071\cdot\tfrac14\approx0.177$ |

Check indifference for $n=3$: each other person fails to call with probability $\tfrac12$, so $\Pr\{\text{no one else}\}=\tfrac14=c/v$ and $\Pr\{\text{at least one}\}=\tfrac34$. Not calling pays $8\cdot\tfrac34=6$, calling pays $8-2=6$. ✓. As $n$ grows, each person calls less and the chance that nobody calls rises ($0.0625\to0.125\to0.177$).

## Concepts
- [[mixed-strategy]] — a probability distribution over a player's actions; payoffs are expected values (used throughout; p. 126)
- [[nash-equilibrium]] — in this unit, a mixed profile where no player has an action with higher expected payoff, and only best actions get positive probability (Prop. 140.1; p. 140)
- [[symmetric-game-equilibrium]] (new) — equilibrium in a symmetric game in which all players use the same (possibly mixed) strategy; models a one-population steady state (Defs. 126.1–126.2; p. 126)
- [[best-response]] — action maximizing expected payoff given beliefs about others' actions; the basis of the dynamics in §4.9 (p. 132)
- [[dominant-dominated-strategy]] — strictly dominated actions can be dismissed by introspection (p. 131–132)
- [[iterated-elimination-of-dominated-strategies]] — repeated removal of strictly dominated actions; surviving profiles include all Nash equilibria (p. 132)
- [[best-response-dynamics]] (new) — each player best-responds to others' previous-period actions; may converge or cycle (p. 132–133)
- [[fictitious-play]] (new) — each player best-responds to the empirical frequencies of the opponent's past actions (p. 133–134)
- [[support-enumeration]] (new) — author's method: try every combination of action subsets and test the equality and no-better-action conditions (p. 135)
- [[bernoulli-payoff-function]] (new) — payoff function over outcomes whose expected value represents preferences over lotteries; unique up to $\eta+\theta u$, $\theta>0$, when there are at least three outcomes (Lemma 145.1; pp. 144–145)
- [[expected-utility]] — the expected-payoff evaluation $\sum p_k u(a_k)$ of lotteries, (144.1) (p. 144)
- [[independence-axiom]] — assumption (named, not described here) that yields the expected-payoff representation (p. 144)
- [[utility-function]] — ordinal payoff function for deterministic outcomes; distinct from the Bernoulli function (p. 145)
- [[all-pay-auction]] (new) — auction where all bidders pay their bids; winner takes the object (p. 141)

## Canonical instances
- [[approaching-pedestrians]] — symmetric game with two pure and one mixed symmetric equilibrium; half of encounters collide in the mixed one (p. 126)
- [[crime-reporting-game]] — $n$ bystanders; unique symmetric mixed equilibrium; bigger group, lower chance anyone calls (pp. 128–129)
- [[kitty-genovese-bystander-effect]] — empirical puzzle for which social psychologists propose three factors, while the author argues the equilibrium analysis implies the decline without them (pp. 130–131)
- [[matching-pennies]] — fictitious play converges to the mixed equilibrium (p. 134)
- [[battle-of-the-sexes]] — best-response dynamics can cycle; used to illustrate the support method (pp. 133, 136)
- [[cournot-duopoly]] — best-response dynamics converge (p. 133)
- [[all-pay-auction-uniform-equilibrium]] — both players bid uniformly on $[0,K]$, payoff 0 (pp. 141–143)

## Bridges (candidates)
- [structural-analogy] Fictitious play beliefs ↔ statistics: using the empirical frequency of past observations as the probability estimate — same counting rule, but used here as a belief about a strategic opponent.
- [metaphor] Best-response dynamics cycling in BoS ↔ dynamics: a system oscillating without reaching a fixed point, since the equilibrium here is only a fixed point of the map.
- [structural-analogy] Crime-reporting equilibrium ↔ social psychology: the bystander effect; the game gives an equilibrium account of a result the psychologists explain by cost/benefit shifts.
- [same-math] Lemma 145.1 (payoffs unique up to positive affine maps) ↔ decision theory: positive affine invariance of expected utility — the same representation result.
- [structural-analogy] Uniform bidding in the all-pay auction ↔ mechanism design / contests: bids spent equal the prize value on average.

## Questions this raises
- Why does Prop. 127.1 need advanced tools, and does it fail for infinite action sets?
- When does fictitious play converge outside the two classes named (opposed interests; two actions each)?
- If players in the crime game could coordinate or differ in cost $c$, which equilibrium would a society settle on?
- How does the support-checking method scale, and which computational methods improve on it (the author mentions GAMBIT)?

## Exercises worth doing
- Ex. 127.2 (p. 127) — symmetric equilibrium of "approaching cars"; effect of guilt on payoffs, a steady state with mixed behavior — difficulty: medium
- Ex. 130.1 (p. 130) — extends the crime game to $k\ge2$ contributors; the condition on $Q_{n-1,k-1}(p)$ — difficulty: hard
- Ex. 133.1 (p. 133) — best-response dynamics in Cournot's duopoly from output 0 — difficulty: easy
- Ex. 138.2 (p. 138) — Rock, paper, scissors: all mixed equilibria, then with Scissors forbidden for player 1 — difficulty: medium
- Ex. 143.1 (p. 143) — all-pay auction with $n$ bidders, symmetric mixed equilibrium — difficulty: hard
- Ex. 144.2 (p. 144) — is a set of lottery rankings consistent with expected payoff? — difficulty: medium

## Reading notes
- **Where this part starts and ends:** it starts on printed p. 125 (the end of the §4.6 discussion plus Exercises 125.1–125.2, then §4.7) and ends at the end of the chapter Notes on printed p. 149. §§4.1–4.6 are in part 1. Printed page = pdf page − 11.
- **Source edition:** per the unit metadata, this is an author's draft of selected chapters (copyright 1995–2000), not the published 2004 book. I could not check that against the pages themselves. Cross-references to e.g. Props. 113.2, 116.1, 119.2, Exercises 115.2–115.4, Fig. 104.1 and Fig. 111.2 point to material outside this part.
- **Prop. 113.2** is not printed in this part; I used its restatement on p. 139 and the use on pp. 135–138 for the two conditions (equal payoff on used actions; no better action).
- **Text-layer issues:** primes on $E'$, $I'$ (p. 125), $\epsilon$ (p. 127) and bars on $\underline a_i,\overline a_i$ (p. 140) are damaged in the text layer; I read them from the images. The URL on p. 149 is garbled in the text layer. Overbars/underbars in Exercise 143.2 are lost in the text layer, so I did not reproduce its details.
- **Small slips in the source:** p. 140 writes "$F(z)=1$" without the subscript $i$; p. 133 has "generated best response dynamics" (missing "by") and "Does the sequences".
- **Not in these pages:** the model of §4.6 itself (including the definition of $q^*$; Exercise 125.1 only recalls $r$, $E'$, $I'$, $\pi$), and the proofs of Prop. 127.1 and the "only if" part of Lemma 145.1.
