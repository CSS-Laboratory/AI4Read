---
id: osborne-2004-introduction/ch09-bayesian
work: osborne-2004-introduction
unit: 9 Bayesian Games
pages: 271–309
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Bayesian Games (Osborne, ch. 9)

## L0 — One line
A Bayesian game models imperfect information with states, signals and beliefs; each signal defines a "type", and an equilibrium is a Nash equilibrium of the ordinary game whose players are all the types.

## L1 — The gist (≤ 120 words)
Nash equilibrium assumes each player knows the game, including the others' preferences. In many situations she does not. The chapter defines a Bayesian game: a set of states, and for each player signals, beliefs about states, and payoffs. Each signal gives a "type". A Nash equilibrium is an equilibrium of the strategic game whose players are all types of all players. Applications: more information can hurt, small gaps in higher-order knowledge can "infect" equilibrium, Cournot with unknown cost, a public-good cutoff, auctions (bid shading, revenue equivalence, winner's curse), and unanimous juries, where voting by signal fails in large juries when jurors care about acquitting the guilty.

**Prerequisites:** strategic games and Nash equilibrium; best response; expected value and conditional probability (Bayes' rule); mixed strategies (some exercises); basic calculus (appendix only).

## L2 — Key ideas (5–10 bullets)
- A state describes everyone's preferences and information. Each player gets a signal from it, and her type is her signal. Treating each type as a separate player lets us reuse Nash equilibrium (pp. 277–280).
- A type's expected payoff depends only on the actions of the other players' types, not on other types of herself ((279.1), p. 279).
- More information can hurt a player in a game, because others know she has it and react (p. 281). Missing higher-order knowledge (not knowing that the other player knows) can force a unique equilibrium via "infection" (p. 282).
- In the public-good game, a symmetric equilibrium has a cutoff valuation $v^*$ with $v^*(F(v^*))^{n-1}=c$. The cutoff exceeds the cost $c$ (pp. 288–289).
- In second-price sealed-bid auctions, bidding one's valuation weakly dominates. In first-price auctions a symmetric equilibrium has bidders shade: $\tfrac12 v$ for two uniform bidders, $E[X\mid X<v]$ in general (pp. 292–294).
- Revenue equivalence: with risk-neutral bidders and the stated conditions, the second-price equilibrium with truthful bids and the symmetric first-price equilibrium give the same expected revenue. The appendix generalises this (pp. 294, 308).
- With common values, a bidder must condition on winning, or she suffers the winner's curse (p. 297).
- Under unanimity, a juror's vote matters only if all others vote to convict. So in a large jury, voting by signal is not an equilibrium when jurors care about acquitting the guilty (pp. 302–303).

## L3 — Walkthrough

### 9.1 Introduction (p. 271)
Nash equilibrium assumes each player holds correct beliefs about the others' actions, so she must know the game, including the others' preferences. Often she does not: bargainers' valuations, firms' costs, combatants' strengths, jurors' interpretations. A "Bayesian game" generalises the strategic game to any case where players are imperfectly informed about something relevant to their choice (p. 271).

### 9.2 Motivational examples (pp. 271–276)

**Example 271.1 (BoS variant).** Player 1 does not know whether player 2 wants to meet her or avoid her. She gives probability $\tfrac12$ to each. Player 2 knows. There are two states ("meet", "avoid"), with payoffs as in Figure 272.1. The numbers are Bernoulli payoffs, because probabilities are involved (p. 272).
- Player 2 has two types: one who wishes to meet, one who wishes to avoid.
- Player 1 needs a belief about what each type does. Example: if the "meet" type plays $B$ and the "avoid" type plays $S$, then $B$ gives player 1 $\tfrac12\cdot2+\tfrac12\cdot0=1$ and $S$ gives $\tfrac12\cdot0+\tfrac12\cdot1=\tfrac12$ (p. 272).
- Figure 273.1 lists player 1's expected payoffs. Columns are (action of "meet" type, action of "avoid" type):

| | (B,B) | (B,S) | (S,B) | (S,S) |
|---|---|---|---|---|
| B | 2 | 1 | 1 | 0 |
| S | 0 | ½ | ½ | 1 |

- Pure equilibrium: a triple of actions (player 1, "meet" type, "avoid" type) such that player 1's action is optimal against the pair of type actions given her belief, and each type's action is optimal against player 1's action. This is a three-player strategic game (p. 273).
- Player 2 need not plan for both cases. We, as analysts, do, because player 1's beliefs about each type's action should be correct (p. 273).
- $(B,(B,S))$ is an equilibrium: $B$ is optimal for player 1 against $(B,S)$ in Figure 273.1. Given $B$, $B$ is optimal for the "meet" type and $S$ for the "avoid" type (p. 273).
- Story for the model: a player is told the state by a signal and carries out a plan made for each possible signal. Player 1's signal is uninformative, the same in every state (p. 274).

**Example 274.2 (both players unsure).** Player 1 gives probability $\tfrac12$ to "2 wants to meet". Player 2 gives probability $\tfrac23$ to "1 wants to meet". Each knows her own preferences (p. 274).
- Four states: $yy, yn, ny, nn$. The first letter is player 1's wish, the second is player 2's.
- Player 1's signal is $y_1$ in $\{yy,yn\}$ and $n_1$ in $\{ny,nn\}$. Player 2's signal is $y_2$ in $\{yy,ny\}$ and $n_2$ in $\{yn,nn\}$ (p. 274).
- Beliefs: $y_1$ gives $\tfrac12,\tfrac12$ to $yy,yn$. $n_1$ gives $\tfrac12,\tfrac12$ to $ny,nn$. $y_2$ gives $\tfrac23$ to $yy$ and $\tfrac13$ to $ny$. $n_2$ gives $\tfrac23$ to $yn$ and $\tfrac13$ to $nn$ (p. 275).
- There are four "players" (two types each). Type $y_1$'s expected payoffs (Figure 276.1) equal the table above (p. 276).
- Claimed equilibria: $((B,B),(B,S))$ and $((S,B),(S,S))$. The first pair is the actions of types $y_1,n_1$, the second those of $y_2,n_2$ (pp. 275–276).

In both examples, an equilibrium is a list of actions, one per type, each a best response given the type's belief. The actions of other types of the same player are irrelevant to her, so we may treat all types as players of one strategic game (p. 276).

*Intuition note.* Unknown preferences are handled by splitting a player into versions, one per thing she might know. Player 1 then best-responds to a "population" of versions of player 2, weighted by her probabilities.

### 9.3 General definitions (pp. 276–280)

**9.3.1 Bayesian games.** A state is a complete description of the players' relevant characteristics, preferences and information. There must be a state for every collection some player thinks possible (p. 276). A state is realised but not observed. Player $i$ receives the signal $\tau_i(\omega)$, a deterministic function of the state (p. 277).
- States giving signal $t_i$ are *consistent* with it.
- If $\tau_i$ differs in every state, $i$ is perfectly informed. If constant, her signal says nothing. Otherwise it gives partial information (p. 277).
- Type $t_i$ is player $i$ having received $t_i$. Each type has a belief (probabilities over consistent states). Preferences over lotteries on pairs (action profile $a$, state $\omega$) are given by a Bernoulli payoff $u_i(a,\omega)$ (p. 277).

**Definition 277.1.** A Bayesian game consists of: a set of players; a set of states; and for each player a set of actions; a set of signals with a signal function (state → signal); for each signal, a belief (probability distribution over the states consistent with it); and a Bernoulli payoff function $u_i(a,\omega)$ (pp. 277–278).

Beliefs are taken as primitives. A variant gives each player a "prior" belief about the states, from which each type's belief is derived using Bayes' formula, but this chapter does not (p. 278).

Example 271.1 fits as follows (p. 278). States are {meet, avoid}. Player 1 has one signal $z$ with $\tau_1=z$ in both states and belief $\tfrac12$ each. Player 2 has signals $m,v$ and learns the state. Example 274.2 fits likewise with four states and signals $y_1,n_1,y_2,n_2$ (pp. 278–279).

**9.3.2 Nash equilibrium.** In a Bayesian game each type of each player chooses an action. In equilibrium each type's action is optimal given every type's action of every other player (p. 279).

Notation: $\Pr(\omega\mid t_i)$ is the belief of type $t_i$. $a(j,t_j)$ is the action of type $t_j$ of player $j$. $\hat a(\omega)$ is the profile in which each $j$ plays $a(j,\tau_j(\omega))$. Type $t_i$'s expected payoff from action $a_i$ is

$$\sum_{\omega\in\Omega}\Pr(\omega\mid t_i)\,u_i\big((a_i,\hat a_{-i}(\omega)),\omega\big),\tag{279.1}$$

and it does not depend on other types of player $i$ (pp. 279–280). Check with Example 271.1: player 1 plays $B$ against ("meet" type plays $B$, "avoid" type plays $S$), giving $\tfrac12u_1(B,B,\text{meet})+\tfrac12u_1(B,S,\text{avoid})$ (p. 279).

**Definition 280.1.** A Nash equilibrium of a Bayesian game is a Nash equilibrium of the strategic game with vNM preferences in which the players are all pairs $(i,t_i)$ ($t_i$ a signal $i$ may receive), the actions of $(i,t_i)$ are those of $i$, and the payoff of $(i,t_i)$ is (279.1) (p. 280).

*Intuition note.* An equilibrium needs each type to be best-responding. Pairing each type with her expected payoff over states is what turns uncertainty into an ordinary game that Nash analysis can handle.

Exercises on p. 280: 280.2 (fight with unknown strength), 280.3 (exchange game), 280.4 (adverse selection), plus 274.1 and 275.1 earlier.

### 9.4 Two examples concerning information (pp. 281–283)

**9.4.1 More information may hurt.** A single decision-maker cannot be worse off with more information, since she can ignore it. In a game, a player with more information, known to others to have it, may be worse off (p. 281).

Figure 281.1 has two states of probability $\tfrac12$ each, with $0<\epsilon<\tfrac12$. Player 1 chooses $T$ or $B$. Player 2 chooses $L,M,R$ (payoffs are as in the figure, and both states have the same $T/B$ payoffs on $L$, with $M,R$ swapped between states) (p. 281).
- Neither player knows the state. Let $p$ be the probability player 1 gives to $T$. Player 2's payoff from $L$ is $2-2(1-\epsilon)p$. From $M$ or $R$ it is $\tfrac32-\tfrac32(1-\epsilon)p$. So $L$ is her unique best response to every strategy of player 1. Player 1's unique best response to $L$ is $B$. The unique equilibrium is $(B,L)$, with payoff 2 for each (p. 281).
- If player 2 learns the state ($\tau_2(\omega_1)\ne\tau_2(\omega_2)$), the unique equilibrium is $(T,(R,M))$. Each type of player 2 has a strictly dominant action, and $T$ is player 1's unique best response (p. 281).
- Player 2 now gets $3\epsilon$ in each state, which is less than 2. She is worse off with the information (p. 281).
- Reason: uninformed, she chooses $L$, which induces $B$. Informed, she tailors her action to the state, which induces $T$. There is no steady state in which she ignores her information and plays $L$, because $L$ leads player 1 to $B$, making $R$ better in $\omega_1$ and $M$ better in $\omega_2$ (p. 282).

*Intuition note.* Information is a commitment device in reverse: because she will act on it, the other player reacts differently, and that reaction can cost her more than the information is worth.

**9.4.2 Infection.** Bayesian games can model uncertainty about others' *knowledge*, not only preferences (p. 282).

Figure 282.1 has three states $\alpha,\beta,\gamma$. Player 1 knows the state if it is $\alpha$, and otherwise knows only that it is $\beta$ or $\gamma$. Player 2 knows $\gamma$ is the state if it is $\gamma$, and otherwise knows only that it is $\alpha$ or $\beta$. The beliefs printed are $\tfrac34,\tfrac14$ in each pair (see figure) (p. 282). Player 2's preferences are the same in all states, and player 1's are the same in $\beta,\gamma$ but differ in $\alpha$ (player 1 gets 3 from $(R,L)$ in $\alpha$, but 0 in $\beta$ and $\gamma$) (p. 282).
- In state $\gamma$ each knows the other's preferences, and player 2 knows that player 1 knows hers. The shortcoming: player 1 does not know that player 2 knows hers, since player 1 can't rule out $\beta$, where player 2 doesn't know whether the state is $\alpha$ or $\beta$ (p. 282).
- Had information been perfect in $\gamma$, both $(L,L)$ and $(R,R)$ would be equilibria. The whole game has a *unique* equilibrium, with $(R,R)$ in $\gamma$ (and indeed every type playing $R$). The incentives of player 1 in $\alpha$ "infect" the rest. The text asks the reader to show this (Exercise 282.1), working through the chain of types in the order given there (p. 282).
- Extending the chain to four states (Figure 283.1) leaves the unique equilibrium unchanged. In state $\delta$ player 2 knows player 1's preferences, but does not know whether player 1 knows that she knows them. With many states, the information in the last state is only very slightly imperfect, yet the equilibrium is still unique, with every type playing $R$ (p. 283).
- In each case the equilibrium outcome is worse for both than $(L,L)$, which in every state but the first is a Nash equilibrium of the perfect-information game. For other payoffs in $\alpha$ and beliefs the "good" outcome $(L,L)$ may be selected in every state. The point is only that one of two equilibria is selected (p. 283).

*Intuition note.* A tiny uncertainty at one end of a chain of "who knows what" can propagate step by step and fix behaviour everywhere. The perfect-information game's multiplicity disappears.

### 9.5 Cournot's duopoly with imperfect information (pp. 283–287)

**9.5.1 Imperfect information about cost.** Both know firm 1's unit cost is $c$. Only firm 2 knows its own cost. Firm 1 believes $c_L$ with probability $\theta$ and $c_H$ with probability $1-\theta$, where $0<\theta<1$ and $c_L<c_H$ (p. 284).

Bayesian game: states $\{L,H\}$. Actions are outputs ($\ge0$). Firm 1 has one type (same signal in both states) and gives $\theta$ to $L$. Firm 2's signal reveals the state. Profits: firm 1 gets $q_1(P(q_1+q_2)-c)$. Firm 2 gets $q_2(P(q_1+q_2)-c_I)$ in state $I$ (p. 284).

Equilibrium is a triple $(q_1^*,q_L^*,q_H^*)$. Best responses (p. 285):
- Firm 1: $b_1(q_L,q_H)$ solves $\max_{q_1}\,[\theta(P(q_1+q_L)-c)q_1+(1-\theta)(P(q_1+q_H)-c)q_1]$.
- Firm 2, low cost: $b_L(q_1)$ solves $\max_{q_L}(P(q_1+q_L)-c_L)q_L$. High cost: $b_H(q_1)$ solves $\max_{q_H}(P(q_1+q_H)-c_H)q_H$.
- Equilibrium: $q_1^*=b_1(q_L^*,q_H^*)$, $q_L^*=b_L(q_1^*)$, $q_H^*=b_H(q_1^*)$ (p. 285).

Exercise 285.1 asks for the equilibrium with $P(Q)=\alpha-Q$ and comparison with the two perfect-information games (p. 285).

**9.5.2 Uncertainty about cost and about information.** Firm 2 now thinks firm 1 may know its cost. Four states: $L0,H0,L1,H1$. The letter gives firm 2's cost, and 1 means firm 1 knows it (p. 285).
- Firm 1's signals: $0$ in $L0,H0$; $L$ in $L1$; $H$ in $H1$. Firm 2's signals: $L$ in $L0,L1$; $H$ in $H0,H1$ (p. 286).
- Beliefs: firm 1's type 0 gives $\theta$ to $L0$ and $1-\theta$ to $H0$. Types $L$ and $H$ are certain. Firm 2's type $L$ gives $\pi$ to $L1$ and $1-\pi$ to $L0$. Type $H$ gives $\pi$ to $H1$ and $1-\pi$ to $H0$. ($\pi=0$ is the earlier case.) (p. 286)
- Exercise 286.1 asks the reader to write the best-response problems, solve for $P(Q)=\alpha-Q$ and check the limits $\pi=0$, $\pi=1$ and that for $0<\pi<1$ firm 2's outputs lie between them (pp. 286–287).

### 9.6 Providing a public good (pp. 287–290)

$n$ individuals, cost $c>0$, individual $i$'s value $v_i$ if the good is provided; payoff 0 otherwise. Each knows her own $v_i$. All values lie between $\underline v$ and $\bar v$, with $0\le\underline v<c<\bar v$. She believes any one valuation is at most $v$ with probability $F(v)$, independently, with $F$ continuous and increasing (p. 287).

Mechanism: each submits $c$ or $0$ simultaneously. If someone submits $c$, the good is provided. A contributor gets $v_i-c$, a non-contributor gets $v_i$. If all submit 0, everyone gets 0 (p. 287).

Bayesian game: states are valuation profiles; actions $\{0,c\}$; $\tau_i=v_i$; payoff $0$ if no one contributes, $v_i$ if $i$ doesn't but another does, $v_i-c$ if $i$ does (p. 288). Exercise 288.1 asks for conditions for equilibria in which only the types $v_i\ge c$ of one player contribute and no other type of any player does (p. 288).

**Symmetric cutoff equilibrium.** Suppose others contribute iff valuation $\ge v^*$. The probability that at least one other contributes is $1-(F(v^*))^{n-1}$. Player $i$'s expected payoff is $(1-(F(v^*))^{n-1})v_i$ if she does not contribute and $v_i-c$ if she does (p. 289). The cutoff is optimal iff

$$v_i(F(v^*))^{n-1}\le c\ \text{ if }v_i<v^*,\qquad v_i(F(v^*))^{n-1}\ge c\ \text{ if }v_i\ge v^*,\tag{289.1}$$

which implies

$$v^*(F(v^*))^{n-1}=c.\tag{289.2}$$

Conversely, if $v^*$ satisfies (289.2) then it satisfies (289.1). So the equilibrium exists iff $v^*$ solves (289.2) (p. 289).

- $v^*>c$. The author notes $F(v)=1$ only if $v\ge\bar v>c$. (Added step: (289.2) with $F\le1$ gives $v^*\ge c$, and $v^*=c$ would need $F(v^*)=1$.) So the good is provided only if some valuation exceeds $v^*>c$, even though all would gain if a player with $v_i>c$ contributed (p. 289).
- Dependence on $n$. The probability the good is provided is $1-(F(v^*))^n=1-cF(v^*)/v^*$. As $n$ rises, $v^*(F(v^*))^{n-1}$ falls at any given $v^*$, so $v^*$ must rise to keep (289.2). The probability rises with $n$ if $F(v^*)/v^*$ is decreasing in $v^*$, and falls if it is increasing. For $F$ uniform with $\underline v>0$ it is decreasing, so the probability rises with $n$ (p. 289).

*Intuition note.* Each player contributes only when she is sure enough that nobody else will. A high cutoff means waiting for someone else, and the free-riding is built into the cutoff.

Exercise 290.1 uses a Bayesian game with three states for uncertainty about the number of witnesses, with $\pi$ the probability of being the sole witness (p. 290).

### 9.7 Auctions (pp. 290–299)

**9.7.1 Introduction.** One object; each bidder gets a signal about its value. If the signal is her valuation, values are *private*. If valuation depends on others' signals too, they are *common* (p. 290). Sealed bids; the highest bidder wins. First-price: the winner pays her bid. Second-price: she pays the highest other bid. The identification of the second-price rule with an open ascending auction needs private values. With common values a bidder can learn from others' bids in an open auction (pp. 290–291).

**9.7.2 Independent private values.** Valuations lie in $[\underline v,\bar v]$ with $\underline v\ge0$; $F$ continuous and increasing; bidders risk neutral; a tie among $m$ bids gives $(v-p)/m$ (p. 291). $P(b)$ is the price paid. Payoff of $i$: $(v_i-P(b))/m$ if no bid exceeds $b_i$ and $m$ bids equal $b_i$, and $0$ if some bid exceeds $b_i$ (p. 292).

*Second-price.* A bid equal to her valuation weakly dominates all her other bids, for every type. For every profile of others' bids it does at least as well, and for some it does strictly better. The proof (Exercise 292.1) adapts Section 3.5.2, since player $i$ is now uncertain about the highest other bid. So there is an equilibrium in which every type bids her valuation. Other equilibria exist (Exercise 292.2) (p. 292).

*First-price.* Bidding $v_i$ weakly dominates any higher bid but does not weakly dominate lower bids, and is itself weakly dominated by any lower bid, since a lower bid may win with positive payoff while bidding $v_i$ gives payoff 0. So an equilibrium with bids below valuations is plausible (p. 292).

*Uniform example, $n=2$, $F(v)=v$ on $[0,1]$.* Claim: $\beta_i(v)=\tfrac12v$ for both is a symmetric equilibrium (p. 293).
- If player 2 bids $\tfrac12v_2$, her bids are uniform on $[0,\tfrac12]$. Player 1 wins surely if $b_1>\tfrac12$. If $b_1\le\tfrac12$ she wins when $v_2<2b_1$, with probability $2b_1$ (p. 293).
- Her payoff is $2b_1(v_1-b_1)$ for $0\le b_1\le\tfrac12$ and $v_1-b_1$ for $b_1>\tfrac12$ (Figure 293.1). Its maximiser is $\tfrac12v_1$ (the author cites Exercise 446.1) (p. 293).
- For $n>2$ a similar analysis gives a symmetric equilibrium $\beta_i(v)=(1-1/n)v$ (p. 293).

*General interpretation.* Let $X$ be the highest of $n-1$ independent valuations drawn from $F$. A symmetric equilibrium exists in which type $v$ bids $E[X\mid X<v]$. Each bidder asks: in the cases where my valuation is highest, what is the expected highest other valuation? In the uniform case with $n=2$, $E[X\mid X<v]=\tfrac12v$, matching (p. 294). The proof is in 9.9.

*Revenue equivalence.* In the second-price equilibrium with truthful bids, a winner with valuation $v$ pays in expectation $E[X\mid X<v]$. This equals the first-price equilibrium bid. In both, the highest valuation wins. So if each bidder is risk neutral and valuations satisfy the conditions of 9.7.2, the two equilibria give the same revenue (pp. 294–295).

**Exercise 295.1** (risk-averse bidders, payoff $x^{1/m}$, $m>1$; claims bids $(1-1/[m(n-1)+1])v_i$) uses the fact that $\max_b b^k(v-b)^\ell$ is solved by $kv/(k+\ell)$ (p. 295).

*Intuition note.* With the bid shaded to $E[X\mid X<v]$, the winner pays on average what a second-price winner would pay. Because the same type wins in both formats, auctioneer revenue is the same, as long as bidders are risk neutral.

**9.7.3 Common valuations.** Valuation of $i$ is $g_i(t_1,\dots,t_n)$, increasing in all signals. Signals are independent. Payoff: $(g_i(t)-P(b))/m$ under the same tie rule, and 0 if outbid (pp. 295–296).

*Second-price example.* $n=2$, signals uniform on $[0,1]$, $v_i=\alpha t_i+\gamma t_j$, $\alpha\ge\gamma\ge0$. $\alpha=1,\gamma=0$ is the private-value case. $\alpha=\gamma$ is "pure common values" (p. 296). Claim: each type $t_i$ bidding $(\alpha+\gamma)t_i$ is an equilibrium. Suppose player 2 bids $(\alpha+\gamma)t_2$ and type $t_1$ bids $b_1$ (p. 296):
- Win probability: $b_1\ge(\alpha+\gamma)t_2$ iff $t_2\le b_1/(\alpha+\gamma)$, probability $b_1/(\alpha+\gamma)$.
- Expected price if she wins: player 2's bid is uniform on $[0,b_1]$ given it is below $b_1$, so $\tfrac12b_1$.
- Expected $t_2$ if she wins: $\tfrac12b_1/(\alpha+\gamma)$.
- Expected payoff $=\big(\alpha t_1+\tfrac12\gamma b_1/(\alpha+\gamma)-\tfrac12b_1\big)\,b_1/(\alpha+\gamma)$, which equals $\dfrac{\alpha}{2(\alpha+\gamma)^2}\,(2(\alpha+\gamma)t_1-b_1)\,b_1$. It is maximised at $b_1=(\alpha+\gamma)t_1$ (p. 297). Symmetrically for player 2.

Exercise 297.1 asks for asymmetric equilibria ($\alpha=\gamma=1$, bids $(1+\lambda)t_1$ and $(1+1/\lambda)t_2$) (p. 297).

*Winner's curse.* Player 1 must use the expected value of player 2's signal *given that her bid wins*. If she wins, 2's signal must be low, so she should impute a low value. A bidder who instead uses the unconditional expectation of the other's signal more likely than not overvalues the object when she wins. This is the winner's curse. The author compares a contractor's quote for renovating a house (p. 297).

*First-price example.* Claim: bidding $\tfrac12(\alpha+\gamma)t_i$ is an equilibrium (Exercise 297.2). The symmetric equilibria again have the same expected price and win probability in both formats, so revenue equivalence holds here too (pp. 297–298). The text says the principle holds more generally for risk-neutral bidders with signals from the same distribution (p. 298).

**Box: auctions of the radio spectrum (pp. 298–299).** US licences were first allocated by hearings, then lotteries, then auctions after the early 1990s. The 1994 mechanism was an open ascending auction with simultaneous bidding on all licences each round. Experts argued openness and simultaneity helped efficiency, since bidders could see rivals' bids. No theory fitted well, so experts used existing theory, laboratory experiments and New Zealand/Australian experience. The first four auctions raised over US$18 billion (p. 299).

### 9.8 Juries (pp. 299–305)

**9.8.1 Model.** Conviction needs a unanimous verdict (p. 299). Each juror thinks the defendant is guilty with prior probability $\pi$. For each true status, each juror independently interprets the evidence as pointing to guilt or innocence with positive probability. With probability $p$ she reads "guilt" if guilty. With probability $q$ she reads "innocence" if innocent. Assume $p>\tfrac12$ and $q>\tfrac12$, so $p>1-q$ (pp. 299–300).

Bernoulli payoffs: $0$ if a guilty defendant is convicted or an innocent one acquitted; $-z$ if an innocent defendant is convicted; $-(1-z)$ if a guilty one is acquitted (300.1). With $r$ her probability of guilt, acquittal pays $-r(1-z)$ and conviction pays $-(1-r)z$, so she prefers acquittal iff $r<z$ (p. 300):

> acquittal is at least as good as conviction iff $\Pr(\text{guilty}\mid\text{juror's information})\le z$. (300.2)

So $z$ is the probability of guilt at which a juror wants conviction (p. 300).

Bayesian game: a state is $(X,s_1,\dots,s_n)$ with $X\in\{G,I\}$ and $s_i\in\{g,b\}$ ($b$ = "blameless"). Action $C$ or $Q$. Signal $\tau_j=s_j$. Given unanimity, only $(C,\dots,C)$ convicts, so payoffs are as in (301.1): $-z$ if $a=(C,\dots,C)$ and $\omega_1=I$; $-(1-z)$ if $a\ne(C,\dots,C)$ and $\omega_1=G$; $0$ otherwise (p. 301). Beliefs: type $g$ gives $\pi p^{k-1}(1-p)^{n-k}$ to $(G,s)$ and $(1-\pi)(1-q)^{k-1}q^{n-k}$ to $(I,s)$, with $k$ the number of $g$'s including herself. Type $b$ gives $\pi p^k(1-p)^{n-k-1}$ and $(1-\pi)(1-q)^{k}q^{n-k-1}$ to the same states, where $k$ counts the $g$'s (the printed exponent $k-1$ on $(1-q)$ looks like a misprint; see Reading notes) (p. 301).

**9.8.2 Nash equilibrium.**

*One juror.* Bayes' rule gives $\Pr(G\mid b)=\dfrac{(1-p)\pi}{(1-p)\pi+q(1-\pi)}$. Acquittal is at least as good iff $z\ge$ that. Similarly conviction after signal $g$ is at least as good iff $z\le\dfrac{p\pi}{p\pi+(1-q)(1-\pi)}$. So she votes by signal if

$$\frac{(1-p)\pi}{(1-p)\pi+q(1-\pi)}\le z\le\frac{p\pi}{p\pi+(1-q)(1-\pi)}\tag{302.1}$$

(the left term is below the right given $p>1-q$) (pp. 301–302).

*Two jurors.* Suppose juror 2 votes by signal. Juror 1's vote matters only if 2 votes $C$, i.e. her signal is $g$. So type $b$ of juror 1 conditions on $(b,g)$:
$$\Pr(G\mid b,g)=\frac{(1-p)p\pi}{(1-p)p\pi+q(1-q)(1-\pi)}.$$
Acquittal is at least as good iff $z$ is at least this (by (300.2)). For type $g$, conviction is at least as good iff $z\le p^2\pi/(p^2\pi+(1-q)^2(1-\pi))$. So voting by signal is an equilibrium if

$$\frac{(1-p)p\pi}{(1-p)p\pi+q(1-q)(1-\pi)}\le z\le\frac{p^2\pi}{p^2\pi+(1-q)^2(1-\pi)}.\tag{302.2}$$

Dividing numerator and denominator of the left sides by $1-p$ and by $(1-p)p$ respectively, and using $p>1-q$, the left side of (302.2) exceeds that of (302.1). So the lowest $z$ supporting voting by signal is higher with two jurors. Reason: a $b$-juror decides assuming the other's signal is $g$, so she worries less about convicting an innocent (pp. 302–303).

*Many jurors ($n$).* If all others vote by signal, juror 1 (type $b$) conditions on all others having signal $g$:
$$\Pr(G\mid b,g,\dots,g)=\frac{(1-p)p^{n-1}\pi}{(1-p)p^{n-1}\pi+q(1-q)^{n-1}(1-\pi)},$$
and acquittal is at least as good iff $z$ is at least this (by (300.2)), which equals
$$\frac{1}{1+\frac{q}{1-p}\left(\frac{1-q}{p}\right)^{n-1}\frac{1-\pi}{\pi}}.$$
Since $p>1-q$, the denominator falls to 1 as $n$ grows, so this lower bound tends to 1. Check: $p=q=0.8$, $\pi=0.5$, $n=12$ gives a bound above $0.999999$. So in a large jury, a juror who reads the evidence as pointing to innocence still votes to convict if she cares even slightly about acquitting the guilty, because her vote matters only when all others read guilt. The text concludes that the large-jury model with such jurors has no equilibrium in which every juror votes by signal (p. 303).

*Other equilibria.* Exercise 304.1 asks for conditions for equilibria in which all vote $Q$, or all vote $C$, regardless of signal (p. 304). Under some conditions on $z$ there is also a symmetric mixed equilibrium: type $g$ votes $C$, type $b$ plays $C$ with probability $\beta(C)$. Type $b$ must be indifferent, so $\Pr(G\mid b,\ n-1\text{ votes for }C)=z$. A juror votes $C$ with probability $p+(1-p)\beta(C)$ if guilty and $1-q+q\beta(C)$ if innocent. This yields

$$(1-p)(p+(1-p)\beta(C))^{n-1}\pi(1-z)=q(1-q+q\beta(C))^{n-1}(1-\pi)z\tag{304.2}$$

and hence $\beta(C)=\dfrac{pX-(1-q)}{q-(1-p)X}$, where $X=\big[\pi(1-p)(1-z)/((1-\pi)qz)\big]^{1/(n-1)}$. For a range of parameters $0\le\beta(C)\le1$. For large $n$, $X\approx1$ and $\beta(C)\approx1$. Type $g$ is willing to convict, since the needed inequality follows from (304.2) given $p,q>\tfrac12$ (p. 304). The text states, without proof ("not simple"), that in this equilibrium the probability an innocent defendant is convicted increases with $n$ (p. 305).

*Variants.* The results rest on a vote mattering only if everyone else votes to convict. With less than unanimity the equilibria differ. Feddersen and Pesendorfer (1998) show that the analogous mixed equilibria give a probability of convicting an innocent defendant that approaches zero as the jury grows (p. 305). Exercise 305.1 (swing voter's curse) is a related two-citizen voting game (p. 305).

*Intuition note.* A vote only counts in the world where everyone else already voted to convict. In a large jury, conditioning on that world makes guilt look very likely, so a signal of innocence can be overruled.

### 9.9 Appendix: arbitrary distribution (pp. 306–308)

**9.9.1 First-price auctions.** Uses calculus. Look for a symmetric equilibrium with an *increasing* bidding function $\beta$ (to be checked afterwards). Let $G_\beta(b)=\Pr\{\text{bid}\le b\}=F(\beta^{-1}(b))$ (p. 306). The expected payoff of valuation $v$ bidding $b$ against the others using $\beta$ is $(v-b)\Pr\{\text{highest bid is }b\}$, where the probability is $(G_\beta(b))^{n-1}$:

$$(v-b)(G_\beta(b))^{n-1}\tag{306.2}$$

Setting the derivative in $b$ to zero at the best response $B_v(\beta)$:

$$-(G_\beta(B_v(\beta)))^{n-1}+(v-B_v(\beta))(n-1)(G_\beta(B_v(\beta)))^{n-2}G_\beta'(B_v(\beta))=0.\tag{306.3}$$

Equilibrium requires $B_v(\beta^*)=\beta^*(v)$ for all $v$ (pp. 306–307). Then:
1. $G_{\beta^*}(B_v(\beta^*))=F(v)$.
2. $G'_\beta(b)=F'(\beta^{-1}(b))/\beta'(\beta^{-1}(b))$, so $G'_{\beta^*}(\beta^*(v))=F'(v)/\beta^{*\prime}(v)$.
3. (306.3) becomes $-(F(v))^{n-1}+(v-\beta^*(v))(n-1)(F(v))^{n-2}F'(v)/\beta^{*\prime}(v)=0$, i.e.
$\beta^{*\prime}(v)(F(v))^{n-1}+(n-1)\beta^*(v)(F(v))^{n-2}F'(v)=(n-1)v(F(v))^{n-2}F'(v)$.
4. The left side is the derivative of $\beta^*(v)(F(v))^{n-1}$. Integrating from $\underline v$:
$\beta^*(v)(F(v))^{n-1}=\int_{\underline v}^v(n-1)x(F(x))^{n-2}F'(x)\,dx=v(F(v))^{n-1}-\int_{\underline v}^v(F(x))^{n-1}dx$ (integration by parts).

$$\beta^*(v)=v-\frac{\int_{\underline v}^v(F(x))^{n-1}dx}{(F(v))^{n-1}}\tag{307.1}$$

*Skip path:* carry forward (307.1) and the identity $\beta^*(v)=E[X\mid X<v]$.

Exercises 307.2 (increasing; $\beta^*(\underline v)=\underline v$; $\beta^*(v)<v$ for $v>\underline v$, via L'Hôpital) and 307.3 (uniform gives $(1-1/n)v$) (p. 307).

*Equivalence with $E[X\mid X<v]$.* $X$ has distribution $H(x)=(F(x))^{n-1}$, so
$$E[X\mid X<v]=\frac{\int_{\underline v}^v xH'(x)dx}{H(v)}=\frac{\int_{\underline v}^v(n-1)x(F(x))^{n-2}F'(x)dx}{(F(v))^{n-1}},$$
which is $\beta^*(v)$ since the numerator is the first line of step 4 (evaluated by parts in its second line). So $\beta^*(v)=E[X\mid X<v]$ (pp. 307–308).

**9.9.2 Revenue equivalence.** Take risk-neutral bidders in a sealed-bid auction where the price is any function of the bids. A bid determines the winning probability $p$ and the expected payment $e(p)$. A bidder with valuation $v$ solves $\max_p\,(p\,v-e(p))$, with solution $p^*(v)$. If $e$ is differentiable, the first-order condition gives $v=e'(p^*(v))$ (p. 308). Integrating,

$$e(p^*(v))=e(p^*(\underline v))+\int_{\underline v}^v x\,dp^*(x).\tag{308.1}$$

In an equilibrium where the object goes to the highest valuation ($p^*(v)=\Pr\{X<v\}$) and the lowest type's expected payment $e(p^*(\underline v))$ is 0 (the text calls it the expected payoff), (308.1) says a bidder's expected payment is independent of the price rule. It equals $\Pr(X<v)E[X\mid X<v]$ (p. 308).

General principle (p. 308): suppose each bidder (i) is risk neutral, (ii) independently receives a signal from the same distribution, satisfying the 9.7.2 conditions, and (iii) has a valuation that may depend on all signals. Consider auction mechanisms whose symmetric equilibria sell to the highest signal and give zero expected payoff to the lowest possible type. Then in the symmetric equilibrium the expected payment of a bidder of any given type, and hence the auctioneer's expected revenue, is the same across such mechanisms.

*Intuition note.* Once the lowest type earns nothing and the highest type wins, the "price rule" cannot change what each type pays on average. What type $v$ pays is pinned down by the marginal-payment condition $v=e'(p)$.

## Toy example (ours, not from the text)
Player 1 chooses $A$ or $B$ and always gets 1 if her action equals player 2's, else 0. Player 2 knows her type. With probability 0.6 she is type $X$ (gets 1 if she matches player 1, else 0). With probability 0.4 she is type $Y$ (gets 1 if she *mismatches*, else 0). Player 1 knows only these probabilities.

Treat $X$ and $Y$ as separate players. Player 1's expected payoff for her action against (action of $X$, action of $Y$):

| player 1 plays | (A,A) | (A,B) | (B,A) | (B,B) |
|---|---|---|---|---|
| A | 0.6·1+0.4·1 = 1 | 0.6·1+0.4·0 = 0.6 | 0.6·0+0.4·1 = 0.4 | 0.6·0+0.4·0 = 0 |
| B | 0.6·0+0.4·0 = 0 | 0.6·0+0.4·1 = 0.4 | 0.6·1+0.4·0 = 0.6 | 0.6·1+0.4·1 = 1 |

Given player 1 plays $A$, $X$'s best response is $A$ (1 vs 0) and $Y$'s is $B$ (1 vs 0), so the pair is $(A,B)$. Against $(A,B)$, $A$ pays 0.6 and $B$ pays 0.4, so $A$ is best. Hence $(A;\,A,B)$ is an equilibrium. If player 1 plays $B$, the types' best responses are $(B,A)$, and against it $B$ pays 0.6 and $A$ pays 0.4. So $(B;\,B,A)$ is the second pure equilibrium. Because each type's response to player 1's action is unique, these are the only two pure equilibria. Note that $Y$ plays "against" player 1 even though player 1 never meets both types at once.

## Concepts
- [[bayesian-game-types]] — a game with states, signals, beliefs and payoffs over (action profile, state); each signal defines a type (pp. 277–278)
- [[bayesian-nash-equilibrium]] — Nash equilibrium of the strategic game whose players are all (player, signal) pairs, with payoff (279.1) (p. 280)
- [[state-of-the-world]] (new) — complete description of players' preferences and information; unobserved, realised at the start (p. 276)
- [[signal-function]] (new) — deterministic map from state to what a player observes; sets of consistent states measure her information (p. 277)
- [[strategic-normal-form-game]] — the base model that the Bayesian game generalises (p. 276)
- [[best-response]] — optimal action given others' actions; used type by type (p. 273)
- [[expected-utility]] — payoffs are Bernoulli payoffs whose expectation represents preferences over lotteries (p. 277)
- [[dominant-dominated-strategy]] — second-price bid equal to valuation weakly dominates (p. 292)
- [[mixed-strategy]] — used in the symmetric jury equilibrium (p. 304)
- [[risk-aversion]] — payoff $x^{1/m}$ in Exercise 295.1; revenue equivalence assumes risk neutrality (p. 295)
- [[private-vs-common-values]] (new) — valuation depends only on one's own signal vs also on others' signals (p. 290)
- [[first-second-price-auction]] (new) — sealed-bid rules: winner pays own bid vs highest other bid (p. 290)
- [[revenue-equivalence]] (new) — same expected revenue across auction formats under the stated conditions (pp. 294, 308)
- [[winners-curse]] (new) — overvaluation from ignoring that winning is informative about others' signals (p. 297)
- [[infection-higher-order-uncertainty]] (new) — a gap in knowing that others know, at one end of a chain of types, can force a unique equilibrium throughout (as in the examples, p. 282)
- [[adverse-selection]] (new) — named in Exercise 280.4; not developed in the text (p. 281)

## Canonical instances
- [[bos-with-uncertain-preferences]] — Examples 271.1 and 274.2: types as separate players (pp. 271–276)
- [[more-information-may-hurt]] — Figure 281.1: informed player 2 gets $3\epsilon<2$ (p. 281)
- [[infection-game]] — Figures 282.1, 283.1: unique equilibrium all $R$ (pp. 282–283)
- [[cournot-incomplete-information]] — duopoly with unknown cost (pp. 283–287)
- [[public-good-contribution-cutoff]] — $v^*(F(v^*))^{n-1}=c$ (pp. 287–290)
- [[first-price-auction-uniform]] — bids of $\tfrac12 v$ for two uniform bidders (p. 293)
- [[common-value-auction-oil-tract]] — $v_i=\alpha t_i+\gamma t_j$, winner's curse (pp. 296–297)
- [[jury-unanimity]] — voting by signal fails in large juries (pp. 299–305)
- [[spectrum-auctions]] — FCC design (pp. 298–299)

## Bridges (candidates)
- [structural-analogy] types of a player as separate players ↔ decision theory: choosing a contingent plan for each possible observation — each type's action is optimal given her information.
- [structural-analogy] winner's curse (condition on winning) ↔ statistics: selection effects/conditioning on being pivotal — the jury juror conditions on her vote mattering, the bidder conditions on her bid winning.
- [structural-analogy] infection via chains of who-knows-that-who-knows ↔ epistemic game theory: mutual vs. common knowledge — each added state raises the level at which the shortcoming in the players' knowledge occurs. (The text does not use these terms.)
- [metaphor] public-good cutoff $v^*>c$ ↔ collective action/free-riding: each waits for someone else.
- [same-math] first-price equilibrium bid $E[X\mid X<v]$ ↔ order statistics: expected value of the maximum of $n-1$ draws conditional on being below $v$.

## Questions this raises
- If beliefs are derived from each player's prior by Bayes' rule, instead of taken as primitives (p. 278), what restrictions do the beliefs of different types satisfy?
- Why does moving from unanimity to a less demanding voting rule change the pivotal-vote logic so much (p. 305)?
- How robust is revenue equivalence if bidders are risk averse (Exercise 295.1) or valuations are not independent?
- In the infection example, which payoffs and beliefs make the "good" outcome $(L,L)$ the unique equilibrium (p. 283)?

## Exercises worth doing
- Ex. 274.1 (p. 274) — equilibria of BoS with uncertainty, pure and mixed; practises the type-as-player method — difficulty: medium
- Ex. 280.4 (p. 280) — takeover bid with unknown target value; adverse selection — difficulty: medium
- Ex. 282.1 (p. 282) — prove uniqueness in the infection game by working along the chain of types — difficulty: medium
- Ex. 285.1 (p. 285) — linear-demand Cournot with unknown cost; compare with perfect-information cases — difficulty: medium
- Ex. 295.1 (p. 295) — risk-averse first-price bidding; compare revenue with second-price — difficulty: hard
- Ex. 305.1 (p. 305) — swing voter's curse: formulate, find the two pure equilibria, show a weakly dominated action — difficulty: medium

## Reading notes
- The source is the author's draft (a draft chapter, version 00/11/6, copyright 1995–2000, as printed on p. 271), not the published 2004 book. Cross-references to other chapters (e.g. "Figure 16.1", "Section 17.7.5", "Exercise 446.1", "(54.2)", "Exercise 31.1") point to material not in these pages.
- Page offset: printed = pdf − 5 (pdf 276–314 = printed 271–309). All citations use printed pages.
- The text layer dropped some symbols. Checked in the page images: in 9.4.1 the image shows $\tau_2(\omega_1)\neq\tau_2(\omega_2)$ (text layer shows "="); in (301.1) the first line is $a\neq(C,\dots,C)$ with $\omega_1=I$ (and the second line $a=(C,\dots,C)$, $\omega_1=G$), so the payoff is 0 in both. The "ε" symbols were also garbled in the text layer.
- Likely misprints in the source: 9.5.1 Signals: "$\tau_1(H)=\tau_2(L)$" should read $\tau_1(H)=\tau_1(L)$. 9.5.2 Payoffs: firm 2's profit in states $H0,H1$ uses $c_L$; it should be $c_H$. Type $b$ belief in 9.8.1 prints $(1-q)^{k-1}$ with $q^{n-k-1}$, whose exponents do not sum to $n-1$; $(1-q)^k$ is expected. 9.8.2 one-juror paragraph (p. 302): "too concerned" after "as long as she is" contradicts the preceding "z is not too small"; "not too concerned" is evidently meant. Page 273 writes "meet player 2" and "avoid player 2" where player 1 is meant (similar slip on p. 272). Ex. 292.1 title says "action" for "auction". In 9.9.1 the probability of the highest bid is described using "valuations" of the other bidders, although $G_\beta$ concerns their bids.
- The table of contents on p. 271 lists the parts of the chapter without section numbers; the numbers 9.1–9.9 used here come from the headings in the body. The beliefs printed in Figure 283.1 are not reproduced in this digest.
- Parts only summarised: box on spectrum auctions (pp. 298–299), the Notes (p. 309, bibliographic credits, not digested), and several exercises, whose solutions are left to the reader.
