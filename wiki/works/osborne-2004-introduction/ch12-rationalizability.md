---
id: osborne-2004-introduction/ch12-rationalizability
work: osborne-2004-introduction
unit: "12 Rationalizability"
pages: 349–361
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
# Rationalizability

## L0 — One line
An action is rationalizable if it survives unlimited rounds of "my opponent is rational, and knows that I am", which for finite games is the same as surviving iterated elimination of strictly dominated actions.

## L1 — The gist (≤ 120 words)
Nash equilibrium assumes each player already knows what the others do. This chapter asks what can be deduced from the players' rationality and their assumptions about each other's rationality. A rational player picks a best response to some belief about the others. Assuming the others are rational too restricts those beliefs, and the restriction can be repeated again and again. The actions that survive every round are rationalizable. For finite games, an action is never a best response exactly when it is strictly dominated. Rationalizability therefore equals iterated deletion of strictly dominated actions, and the order of deletion does not matter. Iterated deletion of weakly dominated actions is less compelling, because the result can depend on the order.

**Prerequisites:** strategic games; mixed strategies and expected payoff; best response; Nash equilibrium; strict dominance in pure strategies.

## L2 — Key ideas
- A rational player maximizes expected payoff given some belief about the others' actions. Nash equilibrium additionally requires the belief to be correct, which is unappealing for a player with little experience of the game (pp. 349–350).
- Rationality plus "the others are rational" plus "they think I am rational", and so on, removes actions step by step. In the bargaining example the demand $2 survives all steps (pp. 350–352).
- An action is rationalizable if it belongs to sets $Z_j$ in which every action is a best response to a belief on the others' sets (Def. 354.1, p. 354).
- Every action used with positive probability in some mixed Nash equilibrium is rationalizable. The converse fails: in Figure 355.1, T and B are rationalizable but not used in equilibrium (p. 354).
- Lemma 356.1: in a finite game, an action is a never best response if and only if it is strictly dominated (p. 356).
- Proposition 357.2: iterated elimination of strictly dominated actions leaves a unique set of profiles, independent of order, and it equals the rationalizable profiles (p. 357).
- Weakly but not strictly dominated actions are not clearly poor choices, and iterated elimination of weakly dominated actions can depend on the order. Dominance solvability is defined for the "eliminate all" version (pp. 359–361).

## L3 — Walkthrough

### 12.1 Introduction (pp. 349–355)

**Rationality.** Nash equilibrium models a steady state in which each player has learned the others' actions from long experience. It does not address what players can deduce from analysing each other's rationality (p. 349). Here each player $i$ has a Bernoulli payoff function $u_i$ (preferences are represented by its expected value). Her *belief* $\mu_i$ about the others' actions is a probability distribution over $A_{-i}$. $U_i(\alpha_i,a_{-i})$ is her expected payoff from mixed strategy $\alpha_i$ when the others play $a_{-i}$ (p. 349).

**Definition 349.1.** Player $i$ is *rational* if she chooses $\alpha_i$ to solve
$$\max_{\alpha_i}\sum_{a_{-i}}\mu_i(a_{-i})\,U_i(\alpha_i,a_{-i}),$$
where $\mu_i$ is her belief (p. 349).

If every belief is correct, a Nash equilibrium strategy solves this problem. Some nonequilibrium actions may be optimal too (pp. 349–350). Correct beliefs are not appealing for an inexperienced player. The most we may assume is that she knows, or assumes, that the others are rational (p. 350).

**Example 350.1 (bargaining over $4).** Each player names an integer amount of dollars.
- If $a_1+a_2\le 4$, each gets what she names.
- If the sum exceeds 4 and $a_i=a_j$, each gets 2.
- If the sum exceeds 4 and $a_i>a_j$, player $i$ gets $4-a_j-(a_i-a_j)\epsilon$.
- If the sum exceeds 4 and $a_i<a_j$, she gets $a_i+(a_j-a_i)\epsilon$.

Here $\epsilon>0$ is small (less than 30 cents). It is a small penalty for an excessive demand (p. 350; payoffs in Figure 350.1).

*Step 1 (rationality only).*
- Demanding \$0 is never optimal: it gives 0 whatever the other does, while demanding \$1 gives at least 1. So \$0 is a *never best response*. By a similar argument so is \$1 (pp. 350–351).
- \$2 is optimal if you are sure the other demands \$2.
- \$3 is optimal if you are sure the other demands \$1.
- \$4 is optimal if you are sure the other demands \$0 (p. 351).
- Hence only \$2, \$3, \$4 are consistent with your being rational (p. 351).

*Step 2 (you assume she is rational).*
- She will not demand less than \$2. Then \$4 is not optimal for you under any belief on her demands \$2, \$3, \$4, since \$2 or \$3 does better against each of them.
- \$2 and \$3 are each optimal for some belief on \{2,3,4\}. For example, if you are sure she demands \$4, then \$3 is optimal.
- So only \$2 and \$3 are consistent with rationality plus assuming she is rational (p. 351).

*Step 3 (you assume she assumes you are rational).*
- Her beliefs about you put weight only on demands of at least \$2. So your belief puts weight only on her demanding \$2 or \$3.
- Against \$2 or \$3, a demand of \$2 beats \$3 (Figure 350.1). So only \$2 remains (pp. 351–352).

Further levels remove nothing more. \$2 is optimal for a player sure that the opponent demands \$2, and (\$2, \$2) is a Nash equilibrium (p. 352).

> *Intuition note.* Each extra layer of "she knows that I know…" shrinks the set of sensible demands, until it stops shrinking. Here the survivor happens to be an equilibrium action.

**The general argument (two players; Figure 353.1).** Suppose $a_i^*$ is consistent with $i$'s rationality. Then some belief $\mu_i^1$ makes $a_i^*$ optimal. Let $X_j^1$ be the set of $j$'s actions that this belief gives positive probability (p. 352).

If $a_i^*$ is also consistent with $i$ assuming $j$ is rational, then for some such $\mu_i^1$ every action in $X_j^1$ must be optimal for $j$ under some belief $\mu_j^2(a_j)$. Let $X_i^2$ be the set of $i$-actions that these beliefs give positive probability (p. 352). Only the *existence* of one suitable belief $\mu_i^1$ is required, not that all beliefs making $a_i^*$ optimal work (pp. 352–353).

*Prisoner's Dilemma illustration.*
- Fink is optimal for player 1 under the belief "player 2 plays Fink with probability 1", and that belief can be continued.
- Fink is also optimal under a belief that gives positive probability to Quiet. But that belief gets stuck: no belief of player 2 makes Quiet optimal (p. 353).

The process continues: every action in $X_k^t$ must be optimal for some belief about the other player, and the actions those beliefs weight form $X_\ell^{t+1}$. If it continues indefinitely, $a_i^*$ is *rationalizable*. If at some stage an action is justified by no belief, it is not (p. 353).

Take sets $Z_1,Z_2$ with $a_i^*\in Z_i$, where every action in $Z_1$ is a best response to a belief on $Z_2$ and vice versa. Then the process can be continued. Conversely, if it can be continued indefinitely, let $Z_i=\{a_i^*\}\cup\bigcup_{t\text{ even}}X_i^t$ and $Z_j=\bigcup_{t\text{ odd}}X_j^t$. These sets have the same property (pp. 353–354). This gives:

**Definition 354.1.** Action $a_i^*$ of player $i$ is *rationalizable* if for each player $j$ there is a set $Z_j$ of actions such that (i) $Z_i$ contains $a_i^*$, and (ii) every action $a_j\in Z_j$ is a best response to a belief of $j$ on $Z_{-j}$. Here $Z_{-j}$ is the set of all $a_{-j}$ with $a_k\in Z_k$ for every other player $k$ (p. 354).

**Link to Nash equilibrium.** If $a^*$ is a pure Nash equilibrium, set $Z_i=\{a_i^*\}$. Each $a_i^*$ is a best response to the belief with probability one on $a_{-i}^*$, so $a^*$ is rationalizable (p. 354).

**Proposition 354.2.** Every action used with positive probability in some mixed strategy Nash equilibrium is rationalizable.
*Proof.* Let $Z_i$ be the set of actions to which $i$'s equilibrium strategy gives positive probability. Each action in $Z_i$ is a best response to the belief equal to the distribution generated by the others' mixed strategies. That belief puts positive probability only on profiles in $Z_{-i}$ (p. 354). ✷

**The converse fails (Figure 355.1).** The game has unique Nash equilibrium $(M,C)$ (Exercise 354.3 asks to show there is no nondegenerate mixed equilibrium). Yet every action is a best response to some action of the other player: T to R, M to C, B to L. Take $Z_1=\{T,M,B\}$ and $Z_2=\{L,C,R\}$. Then every action is rationalizable, including T and B, which no equilibrium uses (p. 354).

*Why T is rationalizable.* Player 2 might choose R if she thinks 1 plays B. That is reasonable if 1 thinks 2 plays L, which is reasonable if 2 thinks 1 plays T, and so on (p. 354).

**Weaker than Nash.** Even when every rationalizable action is used in some equilibrium, rationalizability predicts actions for each player, not a profile. In Figure 355.2 (equilibria $(T,L)$ and $(B,R)$), T, B, L, R are all rationalizable, so any of the four outcomes is allowed (p. 355).

> *Intuition note.* Rationalizability keeps every action that some chain of reasonable beliefs can support. Nash equilibrium demands that the beliefs also match what players actually do, so it says more.

### 12.2 Iterated elimination of strictly dominated actions (pp. 355–358)

**Definition 355.1.** An action is a *never best response* if it is a best response to no belief about the others' actions (p. 355).

**Definition 355.2.** Action $a_i$ is *strictly dominated* if some mixed strategy $\alpha_i$ satisfies $U_i(\alpha_i,a_{-i})>u_i(a_i,a_{-i})$ for all $a_{-i}$ (p. 355).

*Examples.*
- In the Prisoner's Dilemma, Quiet is strictly dominated by Fink (p. 356).
- In Figure 356.1, no action is strictly dominated by another *action*. But R of player 2 gets 1 against anything, while the mixture ½L + ½C gets 3/2 (p. 356).
- The mixture $qL+(1-q)C$ gets $3q$ against T and $3(1-q)$ against B. It strictly dominates R when $3q>1$ and $3(1-q)>1$, that is, when $\tfrac13<q<\tfrac23$ (p. 356).

**Strictly dominated ⇒ never best response.** Let $a_i^*$ be strictly dominated by $\alpha_i$ and let $\mu_i$ be any belief. Then
$$\sum_{a_{-i}}\mu_i(a_{-i})U_i(\alpha_i,a_{-i})>\sum_{a_{-i}}\mu_i(a_{-i})u_i(a_i^*,a_{-i}).$$
So $a_i^*$ is not a best response to $\mu_i$. Since $\mu_i$ was arbitrary, $a_i^*$ is a never best response (p. 356).

**Lemma 356.1.** In a finite strategic game, an action is a never best response if and only if it is strictly dominated. The converse direction is easy to find plausible, but the author says its proof is not trivial and does not give it (p. 356).

*Intuition note.* No belief can make a strictly dominated action best, because some strategy beats it against every profile of the others' actions. For finite games the lemma says that strict dominance is the only way to be a never best response.

**Rationalizability = iterated elimination.** Each step of the argument removes the never-best-response (equivalently strictly dominated) actions of the game left after the previous step. So each step is one more round of eliminating strictly dominated actions, and rationalizable actions are those that survive all rounds (pp. 356–357). We need not remove all the strictly dominated actions of a player at each stage:

**Definition 357.1.** Let $X_i^t$ be sets of actions with: $X_i^1=A_i$; $X_i^{t+1}\subseteq X_i^t$; every action in $X_i^t\setminus X_i^{t+1}$ is strictly dominated in the game where each $j$ has action set $X_j^t$; and no action in $X_i^T$ is strictly dominated in the game with action sets $X_j^T$. The profiles $a$ with $a_i\in X_i^T$ for all $i$ *survive iterated elimination of strictly dominated actions* (p. 357).

**Proposition 357.2.** In any finite strategic game, the set of profiles surviving iterated elimination of strictly dominated actions is unique (it does not depend on order or on how many actions are removed per stage). It coincides with the set of rationalizable profiles (p. 357).

**Example 357.3 (BoS extended with Book, Figure 358.1).**
1. For player 2, B is strictly dominated by Book.
2. After removing it, player 1's B is strictly dominated.
3. After removing that, player 2's Book is strictly dominated.

The only rationalizable action of each player is S (pp. 357–358).

### 12.3 Iterated elimination of weakly dominated actions (pp. 359–361)

**Definition 359.1.** Action $a_i$ is *weakly dominated* if some mixed strategy $\alpha_i$ has $U_i(\alpha_i,a_{-i})\ge u_i(a_i,a_{-i})$ for all $a_{-i}$ and $U_i(\alpha_i,a_{-i})>u_i(a_i,a_{-i})$ for some $a_{-i}$ (p. 359).

In Figure 359.1, T weakly but not strictly dominates B. A weakly but not strictly dominated action is a best response to some belief (by Lemma 356.1). For example, B is optimal if player 1 is sure of R. But the case for it is weak: with the slightest suspicion that 2 plays L, T is better, and against R, T is no worse (p. 359).

Iterating the removal (mark all weakly dominated actions of every player, remove them, repeat) is less compelling, because the result may depend on what is removed (pp. 359–360). In Figure 360.1:
- Remove L (weakly dominated by C), then T (weakly dominated by B). Player 1 chooses B and the payoffs are (1, 2).
- Remove R (weakly dominated by C), then B (weakly dominated by T). Player 1 chooses T and the payoffs are (1, 1) (p. 360).

**Example 360.1 (card game).** There are $n$ cards, the $k$-th showing $k$ on one side and $k+1$ on the other. One card is drawn at random. Player 1 sees a randomly chosen side and player 2 sees the other. Each player vetoes or accepts. If either vetoes, the players tie. If both accept, the player seeing the higher number wins (p. 360).

An action is the set of numbers a player accepts. For $n=2$ each player has 8 actions. Payoff is P(win) − P(lose). Example: player 1 plays \{3\} and player 2 plays \{2,3\}. Player 1 vetoes card 2–3 when she sees 2 and wins when she sees 3. Payoffs are $\tfrac14$ and $-\tfrac14$ (p. 360).

*Claim.* Only pairs in which each player accepts only $n+1$ or accepts nothing survive iterated elimination of weakly dominated actions (p. 360).

*Argument.*
- An action $a_i$ accepting 1 is weakly dominated by $a_i'$, which differs only by vetoing 1. They differ only when the player sees 1. There $a_i$ loses (if the other accepts 2) or ties, while $a_i'$ surely ties (p. 360).
- After removing all actions accepting 1, an action accepting 2 is weakly dominated by the same action vetoing 2. When she sees 2, the other player's remaining actions all veto 1, so $a_i$ never wins. It loses or ties, while $a_i'$ ties (p. 360).
- Continue up to $n$. What remains is "accept only $n+1$" or "accept nothing". Against the remaining actions both give payoff 0, so neither is eliminated (p. 361).

**Dominance solvability.** Suppose *all* weakly dominated actions of each player are removed at every step. If all players are indifferent among all profiles that survive, the game is *dominance solvable* (p. 361).

> *Intuition note.* Strict dominance gives an order-free answer tied to rationality. Weak dominance needs the extra judgement that a player should avoid an action that is a best response to some belief but is never better than another action. The answer can then depend on the order of deletion.

## Toy example (ours)
Game (payoffs: player 1, player 2):

| | L | R |
|---|---|---|
| T | 2, 1 | 0, 0 |
| B | 1, 2 | 3, 1 |

- **Player 2.** L gives 1 against T and 2 against B. R gives 0 and 1. So L strictly dominates R. Player 1 has no dominated action at the start: T beats B against L (2 > 1), but B beats T against R (3 > 0).
- **Eliminate R.** In the game with only column L, T gives 2 and B gives 1. So B is strictly dominated. The survivor is (T, L).
- **Check with beliefs.** Let $p$ be player 1's probability on L. T yields $2p$ and B yields $p+3(1-p)=3-2p$. B is a best response only if $3-2p\ge 2p$, that is $p\le \tfrac34$. So B needs some weight on R. But R is a best response to no belief of player 2, because L is always strictly better. So the chain of justification for B breaks, and B is not rationalizable.
- **Equilibrium.** T is best against L (2 > 1) and L is best against T (1 > 0). (T, L) is the unique rationalizable profile and also a Nash equilibrium.

## Concepts
- [[best-response]] — the action maximizing expected payoff given a belief about the others (p. 349)
- [[belief]] (new) — a probability distribution over the other players' action profiles $A_{-i}$ (p. 349)
- [[rationalizability]] (new) — an action is rationalizable if it lies in sets $Z_j$ whose members are best responses to beliefs on the others' sets (Def. 354.1, p. 354)
- [[never-best-response]] (new) — an action that is a best response to no belief (p. 355)
- [[dominant-dominated-strategy]] — strictly dominated: a mixed strategy does strictly better against every $a_{-i}$; weakly dominated: at least as good everywhere, strictly better somewhere (pp. 355, 359)
- [[iterated-elimination-of-dominated-strategies]] — repeatedly deleting dominated actions. Here the strict version equals rationalizability (p. 357)
- [[nash-equilibrium]] — a profile of mutual best responses. Every action used with positive probability in a mixed equilibrium is rationalizable (p. 354)
- [[dominance-solvable]] (new) — a game where eliminating all weakly dominated actions each round leaves profiles among which all players are indifferent (p. 361)

## Canonical instances
- [[bargaining-split-4-game]] (new) — demands of \$0, \$1, then \$4, then \$3 are eliminated stepwise, leaving \$2 (pp. 350–352)
- [[prisoners-dilemma]] — Quiet is strictly dominated. A belief weighting Quiet cannot start the justification chain (pp. 353, 356)
- [[bach-or-stravinsky]] — the extension with Book is solved by iterated strict dominance, leaving (S, S) (p. 357)
- [[card-veto-game]] (new) — Littlewood's card game solved by iterated weak dominance (p. 360)

## Bridges (candidates)
- [structural-analogy] Layers "I assume she assumes I am rational…" ↔ mutual vs. common knowledge: each round adds one level of knowledge about rationality (canon link; not stated in this unit)
- [structural-analogy] Finite rounds of elimination ↔ level-k reasoning: both reason a limited number of steps about others (canon link; not stated in this unit)
- [same-math] Strictly dominated by a mixed strategy ↔ the dominance notion used in iterated elimination of dominated strategies: the same definition used on a different footing.

## Questions this raises
- Why is the converse in Lemma 356.1 true, and why is its proof nontrivial?
- In games with many players, should beliefs be allowed to correlate the others' actions? (The chapter treats beliefs as distributions over profiles $A_{-i}$, but does not discuss this.)
- Can another criterion give a unique answer for weak dominance when order matters, as in Figure 360.1?
- What more is needed beyond rationalizability to reach a Nash equilibrium?

## Exercises worth doing
- Ex. 354.3 (p. 354) — shows Figure 355.1 has no nondegenerate mixed equilibrium, so rationalizability is strictly broader than equilibrium — difficulty: medium
- Ex. 358.1 (p. 358) — apply iterated strict dominance to a 2×3 game — difficulty: easy
- Ex. 358.3 (p. 358) — rationalizable contributions in a public good game, using iterated dominance — difficulty: hard
- Ex. 361.1 (p. 361) — find the equilibria, show dominance solvability, and find an order where more than one outcome survives — difficulty: medium
- Ex. 361.2 (p. 361) — the bargaining game with $\epsilon=0$ is dominance solvable — difficulty: medium
- Ex. 361.3 (p. 361) — dominance solvability in discrete Bertrand duopoly — difficulty: hard

## Reading notes
- Source is an author's draft, version 00/11/6, copyright 1995–2000, not the published book. The notes section is marked "[Highly incomplete.]" (p. 361).
- Page numbers: the labels give printed 13 for pdf 329, "?" for pdf 330–331 and 269–278 for pdf 332–341. The pages themselves show 349–361, so I cite those. Printed = pdf + 20.
- Def. 357.1 says "for each $t=0,\dots,T-1$" although the sets $X_i^t$ start at $t=1$ (first bullet), so $t=0$ looks like a misprint. L3 above omits this index range.
- Ex. 358.3 reads "Exercise 42.1in" (missing space). Ex. 358.4 contains an unresolved draft note "[not needed?, …]".
- Page 361 has a stray word "candidates," after the definition of dominance solvable. This is a draft artifact.
- Figure 353.1 is a diagram. The page image shows only its caption, with no readable content, so my account of it relies on the text.
- The Notes name Bernheim (1984) and Pearce (1984) as sources of rationalizability, and Littlewood (1953) for the card game (p. 361).
