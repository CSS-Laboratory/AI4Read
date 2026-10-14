---
id: osborne-2004-introduction/ch02-nash-p2
work: osborne-2004-introduction
unit: "Chapter 2 — Nash Equilibrium: Theory (part 2/2: §§2.8–2.10 and Notes)"
pages: 33-52
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
# Best response functions, dominated actions and symmetric equilibria (Osborne, Ch. 2, part 2)

## L0 — One line
A Nash equilibrium is exactly an action profile in which every player's action is a best response to the others' actions, and this lets us find equilibria with best-response functions and discard strictly dominated actions.

## L1 — The gist (≤ 120 words)
How can we find Nash equilibria when the action lists are long or infinite? The unit defines each player's best-response function and shows that equilibria are the profiles where all players best-respond at once. Tables (starring best payoffs) and diagrams (intersecting best-response lines) then locate the equilibria. Under stated assumptions, a public-good model shows that usually only one person contributes. Next, strictly dominated actions are never used in a Nash equilibrium. Weakly dominated actions can be used in a nonstrict equilibrium, but not in a strict one. Voting and median-policy examples use weak domination. Finally, symmetric games model one anonymous population, and the matching solution is the symmetric Nash equilibrium.

**Prerequisites:** strategic games with ordinal preferences, Nash equilibrium and strict equilibrium (earlier in Ch. 2); reading payoff tables; solving two linear equations; basic quadratics.

## L2 — Key ideas (5–10 bullets)
- The best-response function $B_i(a_{-i})$ is the set of player $i$'s best actions against $a_{-i}$; it may contain several actions (p. 34).
- Proposition 34.1: $a^*$ is a Nash equilibrium if and only if $a_i^*\in B_i(a_{-i}^*)$ for every $i$; with unique best responses this is $n$ equations in $n$ unknowns (p. 34).
- Method: find each player's best responses, then find profiles where all are best responses. Tables use stars; interval games use diagrams, where intersections are equilibria (pp. 35–38).
- Example 37.1 has a unique equilibrium $(c,c)$. In the public-good model (under its stated assumptions, p. 41), if $b_1(0)\ne b_2(0)$ only the person who gives more when the other gives nothing contributes (pp. 38, 42).
- An action is strictly dominated if another action of the same player is strictly better against every list of the others' actions; such an action is not a best response to anything, so it is not used in any Nash equilibrium (p. 44).
- An action is weakly dominated if another action is at least as good against every list of the others' actions and strictly better against some; such an action can be used in a nonstrict equilibrium but not in a strict one (p. 45).
- Weak domination organizes the voting and median-policy examples; naming one's favorite policy weakly dominates all other actions (pp. 46, 48).
- Symmetric games model one anonymous population. The steady state is a symmetric Nash equilibrium, which may not exist (pp. 49–51).

## L3 — Walkthrough

### Unit start: end of Exercise 32.3 (Braess-type network) (p. 33)
The unit opens in the middle of an exercise on travel from A to B (Figure 33.1). Per-car times are given for roads used by 1–4 cars. A new road X–Y gives four routes (A–X–B, A–Y–B, A–X–Y–B, A–Y–X–B). Travellers on A–X–Y–B share the A–X leg with A–X–B travellers and the Y–B leg with A–Y–B travellers. On X–Y one car takes 7 minutes and each extra car adds 1 minute per car. The task: find the Nash equilibria and compare each person's time with the equilibrium before the road was built (p. 33).

### 2.8 Best response functions

**2.8.1 Definition.** For fixed actions $a_{-i}$ of the others, player $i$'s best actions are those with the highest payoff. In BoS, player 1 has a single best action against each action of player 2. In the game of Figure 31.1, both $T$ and $B$ are best for player 1 against $L$ (both give 1) (p. 33). The set of best actions is $B_i(a_{-i})$, defined by

$$B_i(a_{-i})=\{a_i\in A_i : u_i(a_i,a_{-i})\ge u_i(a_i',a_{-i})\ \text{for all } a_i'\in A_i\}.$$

$B_i$ is the **best response function**. It is *set-valued*. Each member of $B_i(a_{-i})$ is a best response to $a_{-i}$. In BoS, $B_1(Bach)=\{Bach\}$ and $B_1(Stravinsky)=\{Stravinsky\}$; in Figure 31.1, $B_1(L)=\{T,B\}$ (p. 34).

**2.8.2 Equilibrium via best responses.**

**Proposition 34.1.** The profile $a^*$ is a Nash equilibrium of a strategic game with ordinal preferences if and only if
$$a_i^* \in B_i(a_{-i}^*)\ \text{for every player } i. \tag{34.2}$$
If each player has a single best response to every $a_{-i}$, write $B_i(a_{-i})=\{b_i(a_{-i})\}$. Then (34.2) is equivalent to
$$a_i^*=b_i(a_{-i}^*)\ \text{for every player } i, \tag{34.3}$$
which is $n$ equations in $n$ unknowns. For two players: $a_1^*=b_1(a_2^*)$ and $a_2^*=b_2(a_1^*)$ (pp. 34–35).

*Intuition note.* "No player can gain by changing" and "everyone is already best-responding" say the same thing. The second form turns equilibrium-finding into solving equations or intersecting curves.

**2.8.3 Method and examples.** Two steps: find each player's best-response function, then find the profiles satisfying (34.2) (p. 35).

*Figure 35.1* (rows $T,M,B$; columns $L,C,R$; payoffs player 1, player 2). Player 1's best responses: $M$ against $L$, $T$ against $C$, and both $T$ and $B$ against $R$. Player 2's best responses: $L$ against $T$, both $L$ and $C$ against $M$, and $R$ against $B$. Star each best-response payoff. The boxes with two stars are $(M,L)$ and $(B,R)$, the two Nash equilibria (p. 35).

*Figure 36.2* shows the same functions as a diagram. Player 1's actions are on the horizontal axis and player 2's on the vertical axis. Circles mark player 1's best responses and dots mark player 2's. Pairs with both a circle and a dot are Nash equilibria (p. 36). Exercises 35.1, 36.1 and 36.2 practise this (pp. 35–37).

*Example 37.1 (synergistic relationship).* Each of two individuals chooses an effort $a_i\ge 0$. The payoff is $a_i(c+a_j-a_i)$ with $c>0$. There are infinitely many actions, so no table is possible. Given $a_j$, the payoff is a quadratic in $a_i$ that is zero at $a_i=0$ and at $a_i=c+a_j$ and has a maximum between. By the symmetry of quadratics (Section 17.4, cited, not in this unit) the best response is
$$b_i(a_j)=\tfrac12(c+a_j).$$
The author notes that calculus (setting the derivative to zero) gives the same answer (p. 37). In Figure 38.1 the two lines cross once. At a crossing, $a_1=b_1(a_2)$ and $a_2=b_2(a_1)$, so every crossing is a Nash equilibrium; in general there may be several crossings (p. 38). Solve (34.3):
$$a_1=\tfrac12(c+a_2),\qquad a_2=\tfrac12(c+a_1).$$
Substituting the second into the first: $a_1=\tfrac12\big(c+\tfrac12(c+a_1)\big)=\tfrac34c+\tfrac14a_1$, so $a_1=c$, and then $a_2=c$. The unique Nash equilibrium is $(c,c)$. The diagram shows at once that it is unique and that both actions exceed $\tfrac12 c$, which checks the algebra (p. 38).

*Intuition note.* Each player's best effort rises with the other's effort, but only at half speed. The lines therefore cross once, at the point where each effort equals $c$.

**More general shapes.** If a player has several best responses to some actions of the others, her best-response function is "thick" there (p. 39). Figure 39.1 illustrates several possibilities, with the set of equilibria consisting of one isolated pair $(a_1^*,a_2^*)$ plus a stretch of player 2's function between $(a_1^{**},a_2^{**})$ and $(a_1^{***},a_2^{***})$ (p. 39). Player 1's function $b_1$ is discontinuous there. If a best-response function is discontinuous, then depending on where the discontinuity occurs the functions may not intersect at all, and the game may then have no Nash equilibrium, like Matching Pennies (pp. 39–40). Exercises 39.1, 40.1 and 40.2 follow (pp. 39–40).

**2.8.4 Illustration: contributing to a public good.** Person $i$ has wealth $w_i$, contributes $c_i$ ($0\le c_i\le w_i$) and spends $w_i-c_i$ on private goods. The public good equals $c_1+c_2$. Payoff is $v_i(c_1+c_2)+w_i-c_i$, represented equivalently (since $w_i$ is constant) by
$$u_i(c_1,c_2)=v_i(c_1+c_2)-c_i.$$
Players are the two people; actions are contributions in $[0,w_i]$ (p. 40).

Assumptions (p. 41):
- $u_1(c_1,0)$ increases up to a maximum and then decreases, so $b_1(0)$ is unique.
- $0<b_1(0)<w_1$.

For $c_2=k>0$:
$$u_1(c_1,k)=u_1(c_1+k,0)+k.$$
*(added step: indeed $u_1(c_1+k,0)+k=v_1(c_1+k)-(c_1+k)+k=v_1(c_1+k)-c_1$.)* The graph of $u_1(\cdot,k)$ is the graph of $u_1(\cdot,0)$ shifted left $k$ units and up $k$ units (Figure 41.1). Hence $b_1(k)=b_1(0)-k$ if $k\le b_1(0)$, and $b_1(k)=0$ if $k>b_1(0)$ (p. 41).

The same holds for player 2, whose $v_2$ may differ, so $b_2(0)$ may differ from $b_1(0)$. Both functions have slope $-1$ where positive (Figure 42.1). Conclusions (p. 42):
- If $b_1(0)>b_2(0)$, the unique Nash equilibrium is $(b_1(0),0)$.
- If $b_1(0)<b_2(0)$, the unique Nash equilibrium is $(0,b_2(0))$.
- Only if $b_1(0)=b_2(0)$ do both contribute. Then the sloped parts coincide and any $(c_1,c_2)$ with $c_1+c_2=b_1(0)$ and $c_i\ge0$ is a Nash equilibrium.

The author summarizes: except in unusual circumstances, only one person contributes, when each payoff has the form $v_i(c_1+c_2)+w_i-c_i$, each $v_i(c_i)-c_i$ increases to a maximum and then decreases, and each person optimally contributes less than her entire wealth when the other contributes nothing. That person is the one who wants to contribute more when the other contributes nothing. The identity of the contributor does not depend on the wealth distribution, provided each person would optimally give less than her whole wealth when the other gives nothing (p. 42).

*Intuition note.* A unit more from the other person makes my own unit unnecessary. The person with the stronger own desire for the good therefore ends up providing all of it.

Exercise 42.1 (pp. 42–43) adds an interaction term $(w_i-c_i)(c_1+c_2)$ and asks for the equilibrium, a welfare comparison, and the $n$-person case.

### 2.9 Dominated actions

**2.9.1 Strict domination.** Opening example: pulling into the free left lane is better at a red light whether or not the car in the right lane turns right (p. 43).

**Definition 43.1.** In a strategic game with ordinal preferences, player $i$'s action $a_i''$ *strictly dominates* her action $a_i'$ if
$$u_i(a_i'',a_{-i})>u_i(a_i',a_{-i})\ \text{for every list } a_{-i}.$$
In the Prisoner's Dilemma, *Fink* strictly dominates *Quiet*. In BoS neither action strictly dominates the other (pp. 43–44).

A strictly dominated action is not a best response to any actions of the others. Hence **a strictly dominated action is not used in any Nash equilibrium** (p. 44). We can drop such actions when searching for equilibria; in the Prisoner's Dilemma this leaves $(Fink,Fink)$ as the only candidate, and it is an equilibrium (p. 44).

That $a_i''$ strictly dominates $a_i'$ does not mean $a_i''$ dominates all actions; $a_i''$ may itself be dominated. Figure 44.1 gives player 1's payoffs only (columns $L,R$):
- Left game: $T=(1,0)$, $M=(2,1)$, $B=(1,3)$. $M$ strictly dominates $T$, but $B$ beats $M$ against $R$, so the game may have no equilibrium using $M$.
- Right game: $T=(1,0)$, $M=(2,1)$, $B=(3,2)$. $B$ strictly dominates $M$, so in any Nash equilibrium player 1's action is $B$ (p. 44).

The author adds that a strictly dominated action is incompatible with rational behaviour even for a player facing a game for the first time. This is the first step of a different theory, explored in Chapter 12 (p. 44).

*Intuition note.* If another action is better whatever the others do, there is never a reason to choose the dominated one. It cannot appear in a profile where everyone best-responds.

**2.9.2 Weak domination.** Left lane versus right lane when the left-lane car cannot turn right: the left lane is never worse and sometimes better (pp. 44–45).

**Definition 45.1.** $a_i''$ *weakly dominates* $a_i'$ if
$$u_i(a_i'',a_{-i})\ge u_i(a_i',a_{-i})\ \text{for every } a_{-i}\quad\text{and}\quad u_i(a_i'',a_{-i})>u_i(a_i',a_{-i})\ \text{for some } a_{-i}.$$
Figure 45.1 (player 1's payoffs, columns $L,R$): $T=(1,0)$, $M=(2,0)$, $B=(2,1)$. $M$ weakly dominates $T$; $B$ weakly dominates $M$; $B$ strictly dominates $T$ (p. 45).

Results (p. 45):
- In a *strict* Nash equilibrium (Section 2.7.8, cited, not in this unit), no player's equilibrium action is weakly dominated. Every other action gives her strictly less, so none can weakly dominate the equilibrium action.
- In a nonstrict equilibrium a weakly dominated action can be used. In both games of Figure 46.1, $B$ weakly (not strictly) dominates $C$ for both players, yet $(C,C)$ is a Nash equilibrium. Both games also have the equilibrium $(B,B)$, in which no action is weakly dominated.
  - Left game: payoffs $(B,B)=(1,1)$, all other profiles $(0,0)$. $(B,B)$ is better for both than $(C,C)$.
  - Right game: $(B,B)=(1,1)$, $(B,C)=(2,0)$, $(C,B)=(0,2)$, $(C,C)=(2,2)$. $(B,B)$ is worse for both than $(C,C)$ (pp. 45–46).

Exercises 45.2 and 46.1 follow (pp. 45–46).

*Intuition note.* Weak domination only says "never worse". When the others play so that the two actions tie, a player has no strict reason to leave a weakly dominated action, and that is why it can survive in a nonstrict equilibrium.

**2.9.3 Illustration: voting.** Two candidates $A$ and $B$; an odd number of citizens, each voting for one candidate (no abstention); the one with more votes wins. A majority prefer $A$ to win. Players are the citizens. Each is indifferent among all profiles in which the same candidate wins. Some players (a majority) prefer $A$-winning profiles to $B$-winning ones; the others prefer the reverse (p. 46).

Claim: voting for one's less preferred candidate is weakly dominated by voting for the favorite. Fix the others' votes. If citizen $i$ (who prefers $A$) switches from $B$ to $A$, either the outcome does not change or $A$ wins instead of $B$. The switch cannot make $B$ win instead of $A$ (p. 46).

The game has equilibria in which some or all actions are weakly dominated. For example, all citizens voting for $B$ is a Nash equilibrium, since no single switch changes the outcome (p. 47). Exercise 47.1 asks for all equilibria. With more than two candidates, voting for the least preferred candidate is weakly dominated by all her other actions. Exercise 47.2 asks the reader to show that no other action is weakly dominated, under a stated tie assumption. Exercise 47.3 covers approval voting (p. 47).

**2.9.4 Illustration: collective decision-making.** The $n$ people ($n$ odd) are affected by a policy, a number. Person $i$ has favorite policy $x_i^*$ and prefers $y$ to $z$ if and only if $y$ is closer to $x_i^*$. Each names a policy and the median is chosen. For example, from $-2,0,0.6,5,10$ the chosen policy is $0.6$ (p. 47). The game: players are the $n$ people; actions are policies; person $i$ prefers profile $a$ to $a'$ if and only if the median in $a$ is closer to $x_i^*$ than the median in $a'$ (p. 48).

*Claim:* naming $x_i^*$ weakly dominates all other actions. Take $x_i\ne x_i^*$, first $x_i>x_i^*$. For the others' actions, let $\underline a$ and $\overline a$ be the values with half the others' actions at most $\underline a$ and half at least $\overline a$ (so $\underline a\le\overline a$; the labelling printed in the source looks swapped, see Reading notes).

- (a) *At least as well off for all others' actions.*
  - If $\overline a\le x_i^*$ or $\underline a\ge x_i$, the median is the same whether $i$ names $x_i^*$ or $x_i$.
  - If $\overline a>x_i^*$ and $\underline a<x_i$, then naming $x_i^*$ gives a median at most the greater of $x_i^*$ and $\underline a$, while naming $x_i$ gives a median at least the lesser of $x_i$ and $\overline a$. So she is worse off naming $x_i$.
- (b) *Better off for some others' actions.* Suppose half of the others name policies below $x_i^*$ and half name policies above $x_i$. Then the outcome is $x_i^*$ if she names $x_i^*$ and $x_i$ if she names $x_i$.

The case $x_i<x_i^*$ is symmetric (p. 48). Hence truth-telling weakly dominates all other actions, and the profile where everyone names her favorite is a Nash equilibrium (p. 48).

*Intuition note.* Naming a policy beyond the current median can only push the median away from your favorite. It can never pull it closer, so honesty is never worse and sometimes strictly better.

Exercise 49.1 asks for other equilibria. Exercise 49.2 asks whether the same holds when the *mean* replaces the median (p. 49).

### 2.10 Symmetric games and symmetric equilibria
A Nash equilibrium corresponds to a steady state of interaction among members of several populations, one per player. Sometimes the situation involves a single homogeneous population meeting anonymously, such as pedestrians on a sidewalk (p. 49). The unit restricts attention to two-player interactions.

**Definition 49.3.** A two-player strategic game with ordinal preferences is *symmetric* if both players have the same set of actions and their preferences are represented by payoff functions with
$$u_1(a_1,a_2)=u_2(a_2,a_1)\ \text{for every action pair } (a_1,a_2).$$
In particular $u_1(a,a)=u_2(a,a)$ for every $a$ (p. 49). A two-action game is symmetric if its payoffs have the form of Figure 50.1: $(A,A)=(w,w)$, $(A,B)=(x,y)$, $(B,A)=(y,x)$, $(B,B)=(z,z)$. The Prisoner's Dilemma, the two-player Stag Hunt (Figure 50.2) and the game of Exercise 36.2 are symmetric; BoS and Matching Pennies are not (pp. 49–50). Exercise 50.1 follows.

For one population there is only one role. A steady state is a single action $a^*$ used by everyone, and it qualifies if no player can do better by another action when the others use $a^*$. This holds if and only if $(a^*,a^*)$ is a Nash equilibrium (p. 50).

**Definition 50.2.** An action profile $a^*$ in a strategic game with ordinal preferences, in which each player has the same set of actions, is a *symmetric Nash equilibrium* if it is a Nash equilibrium and $a_i^*$ is the same for every player $i$ (p. 50).

*Example (Figure 51.1, approaching pedestrians).* Actions are $Left$ and $Right$; payoff is 1 each if both step the same way and 0 each otherwise. The symmetric Nash equilibria are $(Left,Left)$ and $(Right,Right)$, two steady states. The author remarks that the latter seems to prevail in the USA and Canada (pp. 50–51).

A symmetric game may have no symmetric Nash equilibrium. In Figure 51.2 ($(X,X)=(0,0)$, $(X,Y)=(1,1)$, $(Y,X)=(1,1)$, $(Y,Y)=(0,0)$) the equilibria are $(X,Y)$ and $(Y,X)$, neither symmetric. Whether a steady state exists with players not always taking the same action is deferred to Section 4.7 (p. 51). Exercise 51.1 (Figure 51.3) follows (p. 51).

*Intuition note.* With one anonymous population, "player 1" and "player 2" are only labels. A stable convention is then one action that is a best response to itself.

### Notes (pp. 51–52)
Historical and bibliographic remarks only (not argued). The source attributes:
- the strategic game to Borel (1921) and von Neumann (1928), and Nash equilibrium to Nash (1950a), with an idea going back at least to Cournot (1838);
- the Prisoner's Dilemma, which appears to have first been considered by Dresher and Flood (RAND experiment, January 1950), and its story to Tucker (1950);
- the first consideration of Matching Pennies to von Neumann (1928);
- the first consideration of voluntary contributions to a public good to Olson (1965);
- the §2.8.4 result to Warr (1983) and Bergstrom, Blume and Varian (1986);
- the first formal study of approval voting to Brams and Fishburn (1978, 1983);
- Exercise 32.3 to Braess (1968).

## Toy example (ours, not from the text)
Player 1 chooses a row, player 2 a column; payoffs are (player 1, player 2).

| | L | R |
|---|---|---|
| T | 1, 2 | 0, 0 |
| M | 3, 1 | 2, 3 |
| B | 0, 0 | 4, 1 |

*Best responses.*
- Player 1, against $L$: payoffs $1,3,0$, so $M$. Against $R$: payoffs $0,2,4$, so $B$. Thus $B_1(L)=\{M\}$ and $B_1(R)=\{B\}$.
- Player 2, against $T$: $2>0$, so $L$. Against $M$: $1<3$, so $R$. Against $B$: $0<1$, so $R$. Thus $B_2(T)=\{L\}$, $B_2(M)=\{R\}$ and $B_2(B)=\{R\}$.

*Equilibrium.* The only box with both players' best-response stars is $(B,R)$. Check by deviation: player 1 moving to $M$ gets $2<4$ and to $T$ gets $0<4$; player 2 moving to $L$ gets $0<1$. So $(B,R)$ is the unique Nash equilibrium. It is also strict, since each deviation is strictly worse.

*Domination.* $M$ strictly dominates $T$ for player 1: $3>1$ against $L$ and $2>0$ against $R$. So $T$ is not used in any equilibrium, consistent with the result. $M$ does not dominate $B$ ($3>0$ against $L$ but $2<4$ against $R$), so $M$ stays a candidate until the best-response check removes it.

## Concepts
- [[best-response]] — $B_i(a_{-i})$: set-valued, the actions maximizing $i$'s payoff given $a_{-i}$ (p. 34)
- [[nash-equilibrium]] — here characterized as: every player's action lies in her best-response set against the others' actions (Prop. 34.1, p. 34)
- [[best-response-function-method]] (new) — find all $B_i$, then the profiles satisfying (34.2); stars in tables, intersections in diagrams (p. 35)
- [[dominant-dominated-strategy]] — strict domination: strictly better against every $a_{-i}$; never a best response, so never in a Nash equilibrium (pp. 43–44)
- [[weak-domination]] (new) — at least as good everywhere and strictly better against some $a_{-i}$; can appear in nonstrict but not strict equilibria (p. 45)
- [[strict-nash-equilibrium]] (new) — every deviation gives strictly less; defined earlier (Sec. 2.7.8) and used here (p. 45)
- [[symmetric-game]] (new) — same action sets and $u_1(a_1,a_2)=u_2(a_2,a_1)$ (p. 49)
- [[symmetric-nash-equilibrium]] (new) — a Nash equilibrium in which all players take the same action; the steady state for one population (p. 50)

## Canonical instances
- [[synergistic-relationship]] (new) — payoff $a_i(c+a_j-a_i)$; linear best responses; unique equilibrium $(c,c)$ (p. 37)
- [[public-good-contribution]] (new) — payoff $v_i(c_1+c_2)-c_i$; best responses with slope $-1$; usually one contributor (pp. 40–42)
- [[prisoners-dilemma]] — *Fink* strictly dominates *Quiet*; symmetric game (pp. 43, 50)
- [[bos]] — neither action strictly dominates the other; not symmetric (pp. 44, 50)
- [[matching-pennies]] — no equilibrium; not symmetric (pp. 40, 50)
- [[stag-hunt]] — two-player version is symmetric (p. 50)
- [[two-candidate-voting]] (new) — voting for the favorite weakly dominates the other vote; some equilibria use weakly dominated actions (pp. 46–47)
- [[median-policy-mechanism]] (new) — naming one's favorite policy weakly dominates all other actions (p. 48)
- [[approaching-pedestrians]] (new) — symmetric game (both step the same way is better) with two symmetric equilibria (pp. 50–51)
- [[braess-network]] (new) — travel-time game with a new road (Exercise 32.3, p. 33)

## Bridges (candidates)
- [structural-analogy] Median mechanism with truthful dominant action ↔ mechanism design: truth-telling is optimal under the rules (the source links this only via the "telling the truth" reading, p. 48).
- [same-math] Intersection of best-response lines $a_i=b_i(a_j)$ ↔ solving a fixed-point system $x=f(x)$ for the vector of actions (the equilibrium conditions (34.3) are literally such a system).
- [structural-analogy] Symmetric equilibrium as a steady state of a single population ↔ convention: a self-sustaining regularity (pedestrian example, p. 51).
- [metaphor] Public-good free-riding ↔ "tragedy of the commons" (named in the Notes, p. 52): the source mentions the idea but does not model it in this way.

## Questions this raises
- When does a game have no symmetric Nash equilibrium, and what is the steady state for a single population then (the source defers this to Section 4.7, p. 51)?
- If strictly dominated actions can be removed, can this be repeated after each removal? The source points to a different theory in Chapter 12 (p. 44).
- Given that weakly dominated actions can appear in equilibria, which equilibria are more reasonable? Compare the two games of Figure 46.1 (p. 46).
- Does the one-contributor result in the public-good model survive when the contribution payoff includes an interaction term, as in Exercise 42.1 (pp. 42–43)?

## Exercises worth doing
- Ex. 35.1 (p. 35) — find best-response functions in the standard games and in Figure 36.1; builds the basic method — difficulty: easy
- Ex. 36.2 (p. 36) — "Dividing money": best responses plotted as in Figure 36.2 — difficulty: medium
- Ex. 40.2 (p. 40) — joint project with two payoff forms; asks if both can do better than at equilibrium — difficulty: medium
- Ex. 42.1 (p. 42) — public good with interaction term; equilibrium versus half-wealth contributions, then $n$ people — difficulty: hard
- Ex. 47.1 (p. 47) — find all equilibria of the two-candidate voting game — difficulty: hard
- Ex. 49.2 (p. 49) — does naming one's favorite policy still weakly dominate when the mean replaces the median? — difficulty: medium

## Reading notes
- The unit starts mid-Exercise 32.3 (printed p. 33 = pdf 45), with §2.8 beginning on the same page, and ends with the Notes on printed p. 52 (pdf 64). Offset: printed = pdf − 12.
- The source is an author's draft of selected chapters (copyright 1995–2000), not the published 2004 book, so numbering and content may differ from the published edition. This is only what the unit's metadata states.
- Primes on $a_i'$ and $a_i''$ in Definitions 43.1 and 45.1 and the text layer of Figures 36.2 and 39.1 are garbled; I used the page images.
- Misprint p. 38: "(a1,a2) is on the graph of b2, player 1's best response function" should read "player 2's".
- Probable misprint p. 48: the text assigns $\underline a$ to the $\tfrac12(n-1)$th highest and $\overline a$ to the $\tfrac12(n+1)$th highest of the others' actions. Its own parenthetical ("at most $\underline a$", "at least $\overline a$") requires the reverse. I used the parenthetical's meaning ($\underline a\le\overline a$).
- Ex. 50.1 refers to Exercise 29.1, which is outside this unit and not summarized. The Notes (p. 52) mention boxes on p. 20 and p. 30, and §2.8.4 (p. 40) cites Exercise 31.1; all of these are outside this unit and not summarized.
