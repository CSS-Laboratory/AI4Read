---
id: osborne-2004-introduction/ch04-mixed-p1
work: osborne-2004-introduction
unit: "4 Mixed Strategy Equilibrium (part 1/2)"
pages: 97–124
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Mixed Strategy Equilibrium (part 1/2): randomizing players, the indifference characterization, domination, and expert diagnosis

## L0 — One line
When players may randomize, a stable pattern of play (a mixed strategy Nash equilibrium) exists in every finite game, and in it each player is indifferent among all actions she uses with positive probability.

## L1 — The gist (≤ 120 words)
Some games, like Matching Pennies, have no Nash equilibrium in actions, yet a stable pattern of play exists if players randomize. This part of the chapter defines mixed strategies and mixed strategy Nash equilibrium for players whose preferences over lotteries are represented by expected payoffs. Key result: a profile is an equilibrium if and only if each player is indifferent among her actions used with positive probability and does no better with any other action. Every finite game has one. In equilibrium no strictly dominated action is used with positive probability. The expert-diagnosis game applies these tools; in its mixed equilibrium a change in one parameter ($r$) moves the expert's probability but not the consumer's.

**Prerequisites:** Nash equilibrium and best responses in strategic games (Chapter 2); expected value; independent events; straight-line (linear) functions; weighted averages.

## L2 — Key ideas
- A mixed strategy Nash equilibrium models a stochastic steady state (each player randomizes with fixed probabilities). It equally models a population in which fixed fractions always play each action (p. 97).
- Randomization needs preferences over lotteries (probability distributions over outcomes), not only over outcomes. The standard assumption is vNM preferences: lotteries are ranked by the expected value of a Bernoulli payoff function (a payoff function over certain outcomes). Two payoff tables that agree ordinally can be different games (pp. 100, 103–104).
- A significant fraction of subjects' stated (hypothetical) choices cannot be represented by any expected-payoff function; the author calls this evidence 'at a minimum, suggestive', yet keeps the assumption as standard, noting many ideas appear not to depend on it (pp. 102–103).
- A player's expected payoff is linear in her own mixing probabilities. So her best response is a single pure strategy or all mixed strategies (in two-action games), and a mixed strategy with $0<p<1$ is never the unique best response (pp. 107–108).
- Proposition 113.2: a profile is a mixed equilibrium iff, for each player, all actions used get the same expected payoff and unused actions get at most that. Hence non-degenerate mixed equilibria (those that are not also pure equilibria) are never strict, i.e. some player always lacks a positive incentive to keep her strategy (pp. 113–116).
- Every finite game has a mixed equilibrium, and one with no weakly dominated strategies (pp. 116, 119).
- A strictly dominated action (including by a mixed strategy) is never used in a mixed equilibrium; a weakly dominated one (another strategy is never worse and sometimes better) may be (pp. 117–118).
- Pure equilibria are exactly the pure-strategy mixed equilibria, whether randomization is allowed or not (pp. 119–120).
- In the expert-diagnosis game the equilibrium is mixed when $E > rE'+(1-r)I'$; $q^*$ is independent of $r$ (pp. 121–124).

## L3 — Walkthrough

### 4.1 Introduction (pp. 97–103)

**4.1.1 Stochastic steady states.** A Nash equilibrium corresponds to a steady state in which, for each player, a population exists and one individual is drawn from each at random for each play (p. 97). Two more general kinds of steady state keep the *pattern* of choices constant (p. 97):
1. Different members of a population choose different actions, each always the same one.
2. Each individual chooses probabilistically, with the same unchanging distribution, every time.

These are equivalent: a fraction $p$ of population $i$ playing $a$ corresponds to every member playing $a$ with probability $p$. In both, the chance that the player-$i$ individual chooses $a$ is $p$ (p. 97). Both are modelled by a *mixed strategy Nash equilibrium*. Mostly the chapter uses the second reading, called *stochastic* ("involving probability") (pp. 97–98).

**4.1.2 Matching Pennies.** Outcomes (Figure 98.1): matching gives player 1 $+\$1$ and player 2 $-\$1$; mismatching gives the reverse (p. 98). There is no Nash equilibrium in actions (p. 98).

*Claim 1: each player choosing each action with probability $\tfrac12$ is a stochastic steady state.* Let player 2 choose each action with probability $\tfrac12$ and player 1 choose Head with probability $p$. Player 1 gains \$1 with probability $\tfrac12 p+\tfrac12(1-p)=\tfrac12$ and loses \$1 with probability $\tfrac12$. The distribution over outcomes does not depend on $p$, so every $p$ is optimal, including $\tfrac12$. The argument for player 2 is similar (p. 98).

*Claim 2: no other steady state exists, under an assumption on preferences.* **Assumption:** each player wants the probability of gaining \$1 to be as large as possible, i.e. if $p>q$ she prefers gaining with probability $p$ to gaining with probability $q$ (p. 98). Let player 2 choose Head with probability $q$ and player 1 choose Head with probability $p$. Then (p. 99):
- Probability of player 1 gaining \$1: $pq+(1-p)(1-q)=1-q+p(2q-1)$.
- Probability of losing \$1: $(1-p)q+p(1-q)=q+p(1-2q)$.

If $q<\tfrac12$, the first is decreasing and the second increasing in $p$. Player 1's unique best policy is then $p=0$ (Tail with certainty). If $q>\tfrac12$ it is Head with certainty. If player 1 plays a pure action, player 2's optimal policy is pure (Head against Tail, Tail against Head). So no steady state has $q\neq\tfrac12$; a symmetric argument rules out $p\neq\tfrac12$ (p. 99).

Population reading: half of the player-1 population always plays Head and half always Tail, and likewise for player 2. Each individual then meets Head with probability $\tfrac12$ (p. 99).

*Intuition note.* Against a 50–50 opponent, nothing you do changes your odds, so 50–50 is as good as anything. Against any other mix, the opponent can be exploited with a pure action. Then the opponent would switch to exploit that, so only 50–50 is stable.

**4.1.3 Expected payoffs.** With two outcomes per player (gain/lose), preferences over lotteries follow from preferences over outcomes under a weak assumption (p. 99). With three outcomes $a\succ b\succ c$, the ranking tells us nothing about whether she prefers $b$ for sure to the lottery giving $a$ or $c$ with probability $\tfrac12$ each; both preferences are consistent (p. 100).

*Standard assumption:* each player $i$ has a payoff function $u_i$ such that she prefers one lottery to another iff its expected $u_i$-value is larger (p. 100). For lotteries $P=(p_a,p_b,p_c)$, $Q=(q_a,q_b,q_c)$, she prefers $P$ to $Q$ iff
$$p_a u_i(a)+p_b u_i(b)+p_c u_i(c)>q_a u_i(a)+q_b u_i(b)+q_c u_i(c).$$
Such preferences are called **vNM preferences** (after von Neumann and Morgenstern); $u_i$ is a **Bernoulli payoff function** (p. 100). The restrictions needed for a payoff function over deterministic outcomes are relatively innocuous; those needed for the expected-value form are not. The author keeps the assumption anyway, as standard in game and economic theory (p. 100).

*Risk attitudes are not restricted* (p. 101). Take $a\succ b\succ c$.
- With $u(a)=10,\ u(b)=9,\ u(c)=0$, she prefers $b$ for sure to any $a$–$c$ lottery giving $a$ with probability below $\tfrac{9}{10}$.
- With $u(a)=10,\ u(b)=1,\ u(c)=0$, she prefers any lottery giving $a$ with probability above $\tfrac1{10}$ to $b$.

If the payoff equals the money amount, the person is **risk neutral**. Example: she is indifferent between \$100 for sure and \$0 w.p. $\tfrac9{10}$ / \$1000 w.p. $\tfrac1{10}$. Buying insurance suggests risk aversion in some circumstances; buying lottery tickets that pay less on average suggests risk preferring in others. In both cases preferences are not represented by expected *money*, but may still be by the expected value of a different payoff function (p. 101).

*Many payoff functions represent the same lottery preferences* (Section 4.12.2, not in this part). We may fix payoffs of the best and worst outcomes arbitrarily, provided best > worst. Example: if $a\succ b\succ c$ and she is indifferent between $b$ and the $\tfrac12$–$\tfrac12$ lottery over $a,c$, then $u(a)=3,u(c)=1\Rightarrow u(b)=2$; or $u(a)=10,u(c)=0\Rightarrow u(b)=5$ (p. 101).

**Box: evidence on expected payoff functions (pp. 102–103).** Lottery 1: \$2m for sure. Lottery 2: \$10m w.p. 0.1, \$2m w.p. 0.89, 0 w.p. 0.01. Lottery 3: \$2m w.p. 0.11, 0 w.p. 0.89. Lottery 4: \$10m w.p. 0.1, 0 w.p. 0.9. A significant fraction of experimental subjects say they prefer 1 to 2 *and* 4 to 3 (p. 102). No expected-payoff function represents this. If lottery 1 beat lottery 2 under some $u$ (amounts in millions):
$$u(2)>0.1u(10)+0.89u(2)+0.01u(0).$$
Subtract $0.89u(2)$ and add $0.89u(0)$ to each side:
$$0.11u(2)+0.89u(0)>0.1u(10)+0.9u(0),$$
which says lottery 3 beats lottery 4 (p. 102).

- Indifference between 1 and 2 and between 3 and 4 is compatible with expected payoffs. If people "make mistakes" when almost indifferent, the observed pattern is not directly inconsistent with the theory (p. 102).
- If mistakes are symmetric, the frequency of expressing 2-over-1 and 4-over-3 should be similar to that of 1-over-2 and 3-over-4. The text then says 'the second pattern is significantly more common than the first' (Conlisk 1989), so a more significant modification of the theory is needed (pp. 102–103).
- Limits of the evidence: the choices are hypothetical. Experiments with normal research budgets show few inconsistent choices, which does not contradict the large-stakes evidence (p. 103).
- Verdict: the evidence is "at a minimum, suggestive". The vast majority of models still assume expected-payoff preferences, and the author keeps the assumption, noting many ideas appear not to depend on it (p. 103).

*Intuition note.* The algebra shows that "1 over 2" and "3 over 4" are the same comparison once the common 0.89 chance of \$2m (or 0) is cancelled. Yet many subjects say they prefer 1 to 2 and 4 to 3, which no expected-payoff function can produce.

### 4.2 Strategic games in which players may randomize (pp. 103–105)

**Definition 103.1.** A strategic game (with vNM preferences) consists of a set of players; for each player a set of actions; and for each player preferences over lotteries over action profiles that are represented by the expected value of a Bernoulli payoff function over action profiles (p. 103).

The table looks the same as in Chapter 2, but the numbers are now Bernoulli payoffs whose expected values represent preferences over lotteries. So two tables that represent the same *ordinal* game may be different vNM games (p. 103).

*Example (Figure 104.1).* Both Prisoner's Dilemma tables rank outcomes identically. Left table, $(Q,Q)=2,\ (F,Q)=3,\ (F,F)=1$ for player 1: $2=\tfrac12\cdot3+\tfrac12\cdot1$, so she is indifferent between $(Q,Q)$ and the $\tfrac12$–$\tfrac12$ lottery over $(F,Q),(F,F)$. Right table, with entries $3$, $4$, $1$: $3>\tfrac12\cdot4+\tfrac12\cdot1$, so she prefers $(Q,Q)$ to that lottery (p. 104). To show two tables differ, one pair of lotteries ordered differently suffices; to show they are the same is harder (Section 4.12.2) (p. 104).

A reasonably safe assumption when reading the literature: if players cannot randomize, table numbers represent ordinal preferences; if they can, the numbers are payoffs whose expected values represent lottery preferences (pp. 104–105).

### 4.3 Mixed strategy Nash equilibrium (pp. 105–116)

**4.3.1 Mixed strategies.** A **mixed strategy** is a probability distribution over a player's actions. $\alpha_i(a_i)$ is the probability that $\alpha_i$ gives to action $a_i$. Shorthand: list probabilities in table order, e.g. $(\tfrac13,\tfrac23)$ gives $Q$ probability $\tfrac13$ and $F$ probability $\tfrac23$. A mixed strategy giving probability 1 to one action is a **pure strategy**, written $a_i$ (p. 105).

**4.3.2 Equilibrium.** **Definition 105.1.** A mixed strategy profile $\alpha^*$ is a mixed strategy Nash equilibrium if, for each player $i$ and every mixed strategy $\alpha_i$ of $i$, her expected payoff to $\alpha^*$ is at least that to $(\alpha_i,\alpha^*_{-i})$. Equivalently (pp. 105–106):
$$U_i(\alpha^*)\ge U_i(\alpha_i,\alpha^*_{-i})\ \text{ for every mixed strategy }\alpha_i\text{ of player }i, \tag{106.1}$$
where $U_i(\alpha)$ is $i$'s expected payoff to profile $\alpha$.

**4.3.3 Best response functions.** $B_i(\alpha_{-i})$ is the set of $i$'s best mixed strategies given the others' mixed strategies. Then $\alpha^*$ is a mixed strategy Nash equilibrium iff $\alpha^*_i\in B_i(\alpha^*_{-i})$ for every player $i$ (p. 106).

**4.3.4 Two players, two actions.** Player 1 has $T,B$; player 2 has $L,R$. Let $p=\alpha_1(T)$ and $q=\alpha_2(L)$. Players' choices are taken to be independent, so each action pair has the product probability (Figure 107.1): $(T,L)$: $pq$; $(T,R)$: $p(1-q)$; $(B,L)$: $(1-p)q$; $(B,R)$: $(1-p)(1-q)$ (p. 107). Player 1's expected payoff is
$$pq\,u_1(T,L)+p(1-q)\,u_1(T,R)+(1-p)q\,u_1(B,L)+(1-p)(1-q)\,u_1(B,R),$$
which regroups as
$$p[q\,u_1(T,L)+(1-q)u_1(T,R)]+(1-p)[q\,u_1(B,L)+(1-q)u_1(B,R)]=pE_1(T,\alpha_2)+(1-p)E_1(B,\alpha_2),$$
where $E_1(T,\alpha_2)$ and $E_1(B,\alpha_2)$ are her expected payoffs to the pure strategies $T$ and $B$ against $\alpha_2$. So it is a weighted average of the two pure-strategy expected payoffs and is linear in $p$ (a straight line, Figure 108.1) (p. 107).

Therefore exactly three cases for her best response (p. 108):
- $E_1(T,\alpha_2)>E_1(B,\alpha_2)$: unique best response $T$.
- $E_1(B,\alpha_2)>E_1(T,\alpha_2)$: unique best response $B$.
- Equal: the line is horizontal and all mixed strategies are best responses.

So a strategy with $0<p<1$ is never the *unique* best response (p. 108).

*Intuition note.* Mixing gives an average of two numbers, so it can never beat the better of them. At best it ties the better one, and a mix with $0<p<1$ does so exactly when the two are equal.

**4.3.5 Matching Pennies via best responses.** Use payoffs $1$ (gain) and $-1$ (loss). With $p,q$ the probabilities of Head, player 1's expected payoffs are $2q-1$ to Head and $1-2q$ to Tail. Her best-response set (of probabilities on Head) is (p. 109)
$$B_1(q)=\begin{cases}\{0\}&q<\tfrac12\\ \{p:0\le p\le1\}&q=\tfrac12\\ \{1\}&q>\tfrac12.\end{cases}$$
Player 2's is $B_2(p)=\{1\}$ if $p<\tfrac12$, $\{q:0\le q\le1\}$ if $p=\tfrac12$, $\{0\}$ if $p>\tfrac12$. Equilibria are the intersections of the two functions' graphs (Figure 110.1). There is one, $(\tfrac12,\tfrac12)$ (p. 109).

**4.3.6 BoS.** Payoffs (Figure 110.2): $(B,B)=(2,1)$, $(S,S)=(1,2)$, mismatches $(0,0)$. Let player 2 play $B$ with probability $q$. Player 1's expected payoffs: $2q$ to $B$, $1-q$ to $S$. So $B$ is best if $q>\tfrac13$, $S$ if $q<\tfrac13$, and all mixed strategies tie at $q=\tfrac13$. Hence $B_1(q)=\{0\}$ if $q<\tfrac13$, $[0,1]$ if $q=\tfrac13$, $\{1\}$ if $q>\tfrac13$ (here $p$ is the probability on $B$) (p. 110). Player 2's function is found "similarly" (p. 110); (added step) her payoffs given $p$ are $p$ to $B$ and $2(1-p)$ to $S$, so her switch point is $p=\tfrac23$, as Figure 111.1 shows. The graphs meet in three points, $(p,q)=(0,0),(\tfrac23,\tfrac13),(1,1)$. The first and third are the equilibria of the ordinal game. The second is new: both players mix and all four outcomes occur with positive probability (p. 110). So randomization can add equilibria to a game that already had some (p. 109).

Exercises 111.1, 111.2, 112.1, 112.2 apply these methods (Hawk–Dove with vNM payoffs, two 2×2 games, an effort-cost coordination game, a "swimming with sharks" game) (pp. 111–112).

**4.3.7 A useful characterization.** For any finite game, a player's expected payoff is a weighted average of her expected payoffs to her pure strategies, with weights given by her own mixed strategy (113.1) (p. 113):
$$U_i(\alpha)=\sum_{a_i\in A_i}\alpha_i(a_i)\,U_i(a_i,\alpha_{-i}).$$
*Argument for the proposition* (p. 113). Let $E_i^*=U_i(\alpha^*)$ in an equilibrium.
- Each pure strategy earns at most $E_i^*$, since $\alpha^*$ is an equilibrium.
- $E_i^*$ is a weighted average of the payoffs to the pure strategies used with positive probability. If any were smaller than $E_i^*$, the average would be smaller, so all equal $E_i^*$.
- Conversely, if these conditions hold for each $i$, any other mixed strategy is by (113.1) a weighted average of $E_i^*$ and numbers at most $E_i^*$, so it does no better.

**Proposition 113.2.** A mixed strategy profile $\alpha^*$ in a finite strategic game with vNM preferences is a mixed strategy Nash equilibrium **if and only if**, for each player $i$ (pp. 113–114):
- the expected payoff, given $\alpha^*_{-i}$, to every action to which $\alpha^*_i$ assigns positive probability is the same; and
- the expected payoff, given $\alpha^*_{-i}$, to every action with zero probability is at most that to any action with positive probability.

Each player's equilibrium expected payoff is her expected payoff to any action she uses with positive probability (p. 114).

*Intuition note.* You only need to check pure actions, not all mixtures. Used actions must tie for best; unused actions must not be better.

*Checks.* BoS: against $(\tfrac13,\tfrac23)$ player 1 gets $\tfrac23$ from both $B$ and $S$. Against $(\tfrac23,\tfrac13)$ player 2 gets $\tfrac23$ from both. So $((\tfrac23,\tfrac13),(\tfrac13,\tfrac23))$ is an equilibrium (p. 114).

**Example 114.1** (Figure 114.1, dots are irrelevant payoffs). Claim: $(\tfrac34,0,\tfrac14)$ for player 1 and $(0,\tfrac13,\tfrac23)$ for player 2 is an equilibrium. Player 1's expected payoffs (p. 114):
- $T$: $\tfrac13\cdot3+\tfrac23\cdot1=\tfrac53$
- $M$: $\tfrac13\cdot0+\tfrac23\cdot2=\tfrac43$
- $B$: $\tfrac13\cdot5+\tfrac23\cdot0=\tfrac53$

$T$ and $B$ (used) tie at the maximum and $M$ (unused) is lower. Player 2 gets $\tfrac52$ from each of $L,C,R$ (e.g. $\tfrac34\cdot2+\tfrac14\cdot4=\tfrac52$). Both conditions hold (p. 114). Player 2's unused action $L$ ties with the used ones. This is allowed (the second condition says "at most") but does not by itself imply an equilibrium using $L$; that depends on unspecified payoffs (pp. 114–115).

Exercises 115.1–115.4 (choosing numbers, Silverman's game, voter participation, defending territory) practise this (pp. 115–116).

*Consequences* (p. 116):
- A *non-degenerate* mixed equilibrium (not also a pure equilibrium) is never a strict Nash equilibrium: a player mixing over several actions is indifferent between them.
- Non-strict equilibria have less appeal, because players lack a positive incentive to choose their equilibrium strategies. Among mixed equilibria the problem is pervasive.
- What fixes the mixing probabilities? In two-player games a player's mixed strategy keeps the *other* player indifferent. In BoS, player 1 plays $B$ with probability $\tfrac23$ so player 2 is indifferent. The author stresses that the theory is *not* that players consciously aim at this. The author says the equilibrium conditions are designed to ensure consistency with a steady state. How a steady state arises is left to Section 4.9 (p. 116).

**4.3.8 Existence.** **Proposition 116.1.** Every strategic game with vNM preferences in which each player has finitely many actions has a mixed strategy Nash equilibrium (p. 116). It does not help to find equilibria. Finiteness is sufficient, not necessary: many games with infinitely many actions also have equilibria. An equilibrium may have every player pure, in which case it is a pure equilibrium of the ordinal game. The proof needs advanced tools (Osborne and Rubinstein 1994) (p. 117).

### 4.4 Dominated actions (pp. 117–119)

**Definition 117.1 (strict domination).** Player $i$'s mixed strategy $\alpha_i$ strictly dominates her action $a_i'$ if
$$U_i(\alpha_i,a_{-i})>u_i(a_i',a_{-i})\ \text{ for every list }a_{-i}\text{ of the others' actions}.$$
Here $u_i$ is a Bernoulli payoff function and $U_i(\alpha_i,a_{-i})$ is her expected payoff under $u_i$ when she mixes and the others play $a_{-i}$ (p. 117).

*Example (Figure 117.1, player 1's payoffs):* $T$: $(1,1)$; $M$: $(4,0)$; $B$: $(0,3)$ against $(L,R)$. $T$ is dominated by neither $M$ nor $B$ alone, but by the $\tfrac12$–$\tfrac12$ mix of $M$ and $B$. That mix gives $2$ against $L$ and $\tfrac32$ against $R$, versus $1$ and $1$ for $T$ (p. 117). Exercise 118.1 asks for all dominating mixes.

*A strictly dominated action is never a best response to any mixed strategies of the others.* Reason: against $\alpha_{-i}$, the expected payoffs of $\alpha_i$ and of $a_i'$ are weighted averages with the *same* weights over $a_{-i}$. Every term for $\alpha_i$ is larger, so its average is larger (p. 118). Hence a strictly dominated action is not used with positive probability in any mixed strategy equilibrium, and can be deleted when looking for equilibria (p. 118).

**Definition 118.2 (weak domination).** $\alpha_i$ weakly dominates $a_i'$ if $U_i(\alpha_i,a_{-i})\ge u_i(a_i',a_{-i})$ for every $a_{-i}$ and $>$ for some $a_{-i}$ (p. 118). A weakly dominated action may be used in a Nash equilibrium (Figure 46.1, earlier chapter), so it may have positive probability in a mixed equilibrium. Weakly dominated actions therefore *cannot* be eliminated when searching for mixed equilibria (p. 118). Exercise 119.1 combines elimination with best-response functions.

**Proposition 119.2.** Every finite strategic game with vNM preferences has a mixed strategy Nash equilibrium in which no player's strategy is weakly dominated (the author notes this is not easy to prove) (p. 119).

### 4.5 Pure equilibria when randomization is allowed (pp. 119–120)

Let $G$ be the ordinal game with payoff functions $u_i$, and $G'$ the vNM game with the same players and actions in which preferences are represented by the expected value of $u_i$ (p. 119).

**Proposition 120.1.** If $a^*$ is a Nash equilibrium of $G$ and $\alpha_i^*$ puts probability 1 on $a_i^*$, then $\alpha^*$ is a mixed strategy Nash equilibrium of $G'$. Proof: no action beats $a_i^*$ against $\alpha^*_{-i}$, so both conditions of Proposition 113.2 hold (pp. 119–120).

**Proposition 120.2.** If $\alpha^*$ is a mixed strategy Nash equilibrium of $G'$ in which each $\alpha_i^*$ puts probability 1 on a single action $a_i^*$, then $a^*$ is a Nash equilibrium of $G$. Proof: no mixed strategy beats $\alpha_i^*$, so in particular no pure one does (p. 120). More generally, banning a non-optimal action does not change the set of optimal actions (p. 120).

### 4.6 Illustration: expert diagnosis (pp. 120–124)

**4.6.1 Model (p. 120–121).** A fraction $r$ of problems are major ($0<r<1$). The expert knows the type; the consumer knows only $r$. Diagnosis is costless to both.
- The consumer always accepts advice to get a minor repair, and may accept or reject advice to get a major repair.
- A major repair fixes both kinds of problem.
- The expert always recommends a major repair for a major problem, and may recommend either for a minor problem.
- Expert profit is $\pi>0$ for a minor repair of a minor problem and for a major repair of a major problem. It is $\pi'>\pi$ for a major repair "sold" for a minor problem.
- The consumer pays $E$ for a major repair and $I<E$ for a minor one. Another remedy costs her $E'>E$ if the problem is major and $I'>I$ if minor. Assumed throughout: $E>I'$.

Actions: expert *Honest* (H: minor repair for minor, major for major) or *Dishonest* (D: major for both); consumer *Accept* (A) or *Reject* (R: buy a minor repair, but seek another remedy if a major one is recommended). Payoffs are expected money (p. 121). The four cells are computed as follows.
- (H,A): consumer $-rE-(1-r)I$; expert $\pi$.
- (D,A): consumer $-E$; expert $r\pi+(1-r)\pi'$.
- (H,R): consumer $-rE'-(1-r)I$; expert $(1-r)\pi$ (paid only for minor problems).
- (D,R): consumer $-rE'-(1-r)I'$; expert $0$.

These form Figure 122.1 (pp. 121–122).

**4.6.2 Nash equilibrium (pp. 122–123).** Let $p$ be the probability on H and $q$ the probability on A.

*Expert's best response.*
- If $q=0$, $p=1$ (since $(1-r)\pi>0$).
- If $q=1$, $p=0$ (since $\pi'>\pi$ gives $r\pi+(1-r)\pi'>\pi$).
- Indifference requires $q\pi+(1-q)(1-r)\pi=q[r\pi+(1-r)\pi']$, which simplifies to $q=\pi/\pi'$ (p. 122).
- (added step) Left side $=qr\pi+(1-r)\pi$ after combining $q\pi-q(1-r)\pi=qr\pi$. Cancelling $qr\pi$ leaves $(1-r)\pi=q(1-r)\pi'$.

*Consumer's best response.*
- If $p=0$: she compares $E$ with $rE'+(1-r)I'$. If $E<rE'+(1-r)I'$, $q=1$. If $E>rE'+(1-r)I'$, $q=0$. If equal, she is indifferent.
- If $p=1$: $q=1$ (given $E<E'$).
- Hence if $E<rE'+(1-r)I'$, $q=1$ for every $p$ (left panel of Figure 123.1).
- If $E>rE'+(1-r)I'$, she is indifferent when
$$p[rE+(1-r)I]+(1-p)E=p[rE'+(1-r)I]+(1-p)[rE'+(1-r)I'],$$
which reduces to
$$p=\frac{E-[rE'+(1-r)I']}{(1-r)(E-I')}.$$
(added step) Moving terms gives $pr(E'-E)=(1-p)\{E-rE'-(1-r)I'\}$, and $r(E'-E)+E-rE'-(1-r)I'=(1-r)(E-I')$.
She plays $q=1$ for larger $p$ and $q=0$ for smaller $p$ (right panel of Figure 123.1) (p. 123).

*Equilibrium* (p. 123).
- If $E<rE'+(1-r)I'$ (an expert's major repair costs less than the *expected* cost of the alternative), $(D,A)$ is the unique equilibrium. The expert is always dishonest and the consumer always accepts: "the dismal outcome for the consumer".
- If $E>rE'+(1-r)I'$, the unique equilibrium is mixed, $(p,q)=(p^*,q^*)$ with
$$p^*=\frac{E-[rE'+(1-r)I']}{(1-r)(E-I')},\qquad q^*=\frac{\pi}{\pi'}.$$

*Population interpretation* (pp. 123–124). Here the author finds this reading fits well. A fraction $p^*$ of experts are honest and $1-p^*$ dishonest. A fraction $q^*$ of consumers are *credulous* (accept any advice) and $1-q^*$ are *wary* (accept only minor-repair advice). Honest and dishonest experts earn the same expected payoff, as do credulous and wary consumers (p. 124). Exercise 124.1 asks for the equilibria when $E=rE'+(1-r)I'$.

**4.6.3 Properties of the equilibrium (p. 124; section continues in part 2).** Rewrite
$$p^*=1-\frac{r(E'-E)}{(1-r)(E-I')}.$$
- *Fewer major problems ($r$ falls).* The numerator falls and the denominator rises, so $p^*$ rises: experts are more honest. Intuition given: a consumer has less to lose from ignoring advice, so honesty must rise for advice to be heeded. $q^*=\pi/\pi'$ does not depend on $r$. The author notes the partial analysis (a lower $r$ makes rejecting more attractive to the consumer given the experts' behaviour) is misleading: in the new equilibrium she accepts with the same probability as before (p. 124).
- *Cheaper major repairs ($E$ falls, with $E'$ and $I'$ constant).* $p^*$ falls: experts are less honest. The consumer has more to lose from ignoring advice, so she heeds it even if experts are less likely to be honest (p. 124).
- The third change ($\pi'$ falls) is cut off at the end of the pages given (p. 124).

*Intuition note.* In a mixed equilibrium each side's probability is set to make the *other* side indifferent. Here $p^*$ is determined by the consumer's costs and $r$ (it is the point where she is indifferent), and $q^*$ by the expert's profits (the point where she is indifferent). (added step: this reading is from the formulas for $p^*$ and $q^*$.) So an exogenous change in the consumer's costs moves the experts' behaviour, not the consumers'.

## Toy example (ours, not from the text)
Game: player 1 chooses $T$ or $B$; player 2 chooses $L$ or $R$. Payoffs (player 1, player 2): $(T,L)=(3,0)$, $(T,R)=(0,2)$, $(B,L)=(1,1)$, $(B,R)=(2,0)$.

*No pure equilibrium.* At $(T,L)$ player 2 gets 0 and gets 2 by switching to $R$. At $(T,R)$ player 1 gets 0 and gets 2 by switching to $B$. At $(B,R)$ player 2 gets 0 and gets 1 by switching to $L$. At $(B,L)$ player 1 gets 1 and gets 3 by switching to $T$.

*Mixed equilibrium via Proposition 113.2.* Let $p=$ prob. of $T$, $q=$ prob. of $L$.
- Player 1: $E_1(T)=3q+0(1-q)=3q$; $E_1(B)=1\cdot q+2(1-q)=2-q$. Indifference: $3q=2-q\Rightarrow q=\tfrac12$.
- Player 2: $E_2(L)=0\cdot p+1(1-p)=1-p$; $E_2(R)=2p+0(1-p)=2p$. Indifference: $1-p=2p\Rightarrow p=\tfrac13$.

Check: at $q=\tfrac12$, $E_1(T)=\tfrac32=E_1(B)=2-\tfrac12$, so every mix of player 1's gets $\tfrac32$ (a weighted average of two equal numbers). At $p=\tfrac13$, $E_2(L)=\tfrac23=E_2(R)=\tfrac23$. Both used actions tie, so the profile $((\tfrac13,\tfrac23),(\tfrac12,\tfrac12))$ is an equilibrium with expected payoffs $\tfrac32$ and $\tfrac23$. If $q>\tfrac12$, then $3q>2-q$ and $T$ is the unique best response, as in 4.3.4. Note that player 1's mix ($\tfrac13$) is fixed by *player 2's* payoffs.

## Concepts
- [[mixed-strategy]] — a probability distribution over a player's actions; pure strategy = probability 1 on one action (p. 105)
- [[nash-equilibrium]] — here, mixed strategy Nash equilibrium: no player has a mixed strategy with higher expected payoff given the others' (Def. 105.1) (p. 105)
- [[stochastic-steady-state]] (new) — steady state in which each individual randomizes with fixed probabilities; equivalent to fixed population fractions playing each action (p. 97)
- [[expected-utility]] — vNM preferences: lotteries ranked by the expected value of a Bernoulli payoff function (p. 100)
- [[utility-function]] — Bernoulli payoff function over deterministic outcomes whose expectation represents lottery preferences; not unique (p. 100–101)
- [[risk-aversion]] — here: preferring $z$ for sure to a lottery averaging $z$; risk neutral = payoff equals money; both compatible with expected-payoff preferences (p. 101)
- [[best-response]] — $B_i(\alpha_{-i})$, the set of $i$'s best mixed strategies; equilibrium iff each strategy lies in it (p. 106)
- [[indifference-characterization]] (new) — Prop. 113.2: used actions tie for best, unused actions get at most that (p. 113)
- [[dominated-strategy]] — strict domination may be by a mixed strategy; strictly dominated actions never used in equilibrium, weakly dominated ones may be (pp. 117–118)
- [[strategic-game]] — here with vNM preferences; same table, different interpretation of numbers (p. 103)

## Canonical instances
- [[matching-pennies]] — no pure equilibrium; unique mixed equilibrium $(\tfrac12,\tfrac12)$ (pp. 98–99, 109)
- [[bach-or-stravinsky]] — a mixed equilibrium (player 1 plays $(\tfrac23,\tfrac13)$, player 2 plays $(\tfrac13,\tfrac23)$) added to the two pure ones (pp. 110, 114)
- [[prisoners-dilemma]] — same ordinal game, different vNM games (Fig. 104.1) (p. 104)
- [[lottery-choice-evidence]] (new) — four lotteries; the stated choices of a significant fraction of subjects (1 over 2, 4 over 3) are not representable by expected payoffs (pp. 102–103)
- [[expert-diagnosis-game]] (new) — honest/dishonest expert vs accept/reject consumer; mixed equilibrium $(p^*,q^*)$ (pp. 120–124)
- [[silvermans-game]] (new) — exercise: no pure equilibrium; mix on 1, 2, 5 (p. 115)

## Bridges (candidates)
- [same-math] Weighted-average payoff $U_i(\alpha)=\sum\alpha_i(a_i)U_i(a_i,\alpha_{-i})$ ↔ decision theory: expected utility is linear in probabilities — literally the same formula.
- [same-math] Box algebra (cancel the common 0.89 component) ↔ decision theory: the independence axiom (canon link; not stated in this unit) — the derivation is that axiom at work.
- [structural-analogy] Fixed population fractions playing each action (p. 97) ↔ evolutionary game theory: population shares at a polymorphic rest point (canon link; not stated in this unit).
- [structural-analogy] Expert's honesty/consumer's credulity with mixed equilibrium ↔ signaling: informed party's action partly reveals information (canon link; not developed here).

## Questions this raises
- If players have no positive incentive to follow a non-degenerate mixed strategy, how can a steady state arise? (Author defers to Section 4.9, p. 116.)
- Which preference assumptions beyond expected payoffs would change mixed equilibria? The author says many ideas "appear not to depend" on the assumption (p. 103).
- In the expert game, why does a lower $r$ leave consumers' acceptance probability $q^*$ unchanged (p. 124)?
- What does the third comparative static ($\pi'$ falls) do to $p^*$ and $q^*$? (Cut off at p. 124.)

## Exercises worth doing
- Ex. 99.1 (p. 99) — Matching Pennies variant with unequal payoffs; tests the steady-state argument — difficulty: easy
- Ex. 107.1 (p. 107) — plot expected payoff as a line in $p$ for BoS (and the game of Figure 19.1, not reproduced here) for $q=0,\tfrac12,1$ — difficulty: easy
- Ex. 111.2 (p. 111) — find all mixed equilibria in two 2×2 games (one with a continuum) — difficulty: medium
- Ex. 112.1 (p. 112) — effort game: equilibria and their dependence on $c$ — difficulty: medium
- Ex. 118.1 (p. 118) — all mixed strategies that strictly dominate $T$ in Fig. 117.1 — difficulty: medium
- Ex. 124.1 (p. 124) — expert game at the knife-edge $E=rE'+(1-r)I'$ — difficulty: medium

(Difficulty is our rating, guided by the source's ?/?? marks where present.)

## Reading notes
- **Unit span:** this part starts at the opening of Chapter 4 (printed p. 97) and ends mid-section 4.6.3 on printed p. 124. The third comparative-statics change (a fall in $\pi'$) is cut off and continues in part 2. Sections 4.7 onward are not in this part.
- **Edition:** pdf pages are a "Selected chapters from draft" of the book, not the published 2004 OUP text. Header text printed at the top of p. 97 (not seen on the later pages): "Draft chapter … Version: 00/11/6. Copyright © 1995–2000". Cross-references (Definition 21.1, Section 4.9, 4.10, 4.12, Exercise 29.1, etc.) refer to this draft's numbering and, when outside Chapter 4, are not available here.
- **Page offset:** printed = pdf − 11.
- **OCR:** the text layer drops primes and some Greek letters on pp. 121–124 ($E'$, $I'$, $\pi'$). I restored them from the page images of pp. 121–123 (Figure 122.1, the best-response formulas, $p^*$, $q^*$). Page 124 had no image, so the primes in $p^*=1-\frac{r(E'-E)}{(1-r)(E-I')}$ and in the later text were restored by consistency with the p. 123 formula.
- **Equations without images:** no page images were supplied for pp. 99, 100, 103, 115, 116 and 124, so the equations on pp. 99, 100, 103 and 124 were read from the text layer only; page images were supplied for pp. 98, 101, 102, 104–114 and 117–123.
- **Voice:** the author writes in the first person; no interlocutor appears in this part.
