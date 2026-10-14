---
id: osborne-2004-introduction/ch08-coalitional
work: osborne-2004-introduction
unit: "8 Coalitional Games and the Core"
pages: 235–267
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Coalitional Games and the Core

## L0 — One line
A coalitional game gives actions to groups, and the core is the set of grand-coalition actions that no group can break away from and improve upon; Osborne applies it to markets, house exchange, voting and matching; it gives a very precise prediction in the horse and house markets but can be empty, as in majority voting.

## L1 — The gist (≤ 120 words)
Strategic and extensive games start from individual players' actions. Coalitional games start from what each group can achieve. The question is which action of the whole group is stable against every possible group breaking away. The answer is the core: actions that no coalition can improve upon (all its members prefer some action of their own). Osborne computes cores in land-ownership economies (wages at most marginal product, a worker's added output), a horse market (one uniform price), house exchange (top trading cycle), majority voting (the core is the Condorcet winner or empty) and marriage matching (deferred acceptance). The core can be empty, as in majority games and the roommate problem. It helps show which institutions give stable outcomes.

**Prerequisites:** Chapter 1 ideas (players, preferences, payoff functions); strategic-game Nash equilibrium (for contrast); simple linear inequalities; partitions of a set; the concept of a function with decreasing increments.

## L2 — Key ideas (5–10 bullets)
- A coalitional game assigns actions to every group; the actions of a group are taken as given, not derived from individual choices (pp. 235–236).
- The core is the set of grand-coalition actions that no coalition can improve upon. It always exists as a set, but may be empty (p. 239). With transferable payoff (each coalition's possibilities summarised by one number, its worth $v(S)$) the test is $x_S(a_N)\ge v(S)$ for every $S$ (p. 239).
- Land economies: with one landowner and decreasing marginal product, each worker gets at most her marginal product (the extra output of one more worker) $f(n)-f(n-1)$ in the core. With equal small landowners the core is the equal split. Under majority-controlled collective ownership the core is empty (pp. 243–246).
- Horse market: every core action has one common trading price in a narrow range, as in competitive equilibrium (the price at which demand equals supply, assuming one price). The theory derives uniform price rather than assuming it (pp. 249–251).
- House exchange with strict preferences: the top trading cycle procedure (repeatedly find a cycle of players each of whose favourite remaining house belongs to the next player in the cycle, and give each her favourite) gives an assignment in the core; the strong core (no coalition can make some members better off and none worse off) is exactly that assignment (pp. 253–255).
- Majority voting: with strict preferences the core is the Condorcet winner (a policy that a majority prefers to every other policy) if one exists, otherwise empty. With one-dimensional single-peaked preferences (each player has a favourite and prefers policies closer to it on either side) it is the median favourite; in higher dimensions it is generally empty (pp. 257–258).
- Matching: the core is nonempty. Deferred acceptance (one side proposes, the other holds its best offer and rejects the rest) gives a core matching, best for the proposing side and worst for the other (p. 262). The roommate problem (one-sided pairing of people) can have an empty core (p. 263).
- The core requires a deviating member to assume that no subgroup of her comrades will deviate further, or at least that she stays better off if they do (pp. 265–266).

## L3 — Walkthrough

### 8.1 Coalitional games (pp. 235–239)

**Definition (p. 235).** A *coalitional game* associates a set of actions with every group of players (a *coalition*); the set of all players is the *grand coalition* $N$; a typical coalition is $S$. An *outcome* is a partition of the players into groups plus an action for each group. Osborne treats only games where each player cares only about the action of the group in the partition she belongs to (p. 235).

**Definition 235.1.** A coalitional game consists of a set of players; for each coalition, a set of actions; for each player, preferences over all actions of all coalitions she belongs to (p. 235).

- Preferences may be given by a payoff function (p. 236).
- If a coalition controls a good, an action is an *$S$-allocation* of the good among its members; an $N$-allocation is just an *allocation* (p. 236).
- A coalition's actions are given, not derived from members' individual actions (p. 236).

**Definition 236.1 (cohesive).** A game is cohesive if, for every partition $\{S_1,\dots,S_k\}$ and every combination $(a_{S_1},\dots,a_{S_k})$ of actions, $N$ has an action at least as desirable for every player $i$ as $a_{S_j}$, where $S_j$ is $i$'s group. The concepts that follow may be applied to any game but have attractive interpretations only for cohesive games (p. 236).

**Examples.**
- *Two-player unanimity (236.2):* two people can produce one unit of output together, none alone. $N$'s actions are $(x_1,x_2)$ with $x_1+x_2=1$, $x_i\ge0$. Cohesive (pp. 236–237).
- *Landowner and workers (237.1):* an estate with $k$ workers produces $f(k+1)$, $f$ increasing, $f(0)=0$; $m$ workers. A coalition of workers only gets nothing. Cohesive, because the grand coalition produces the most and in any partition only one coalition produces anything (p. 237).
- *Three-player majority (237.2):* any coalition of two or three players controls one unit of output. Cohesive, because any partition has at most one majority coalition (p. 237).

**Transferable payoff (p. 238).** When a coalition's possible payoff distributions can be summarised by one number, the game has *transferable payoff*. That number is the coalition's *worth* $v(S)$, and the game is specified by $N$ and $v$.
- Unanimity: $v(\{1\})=v(\{2\})=0$, $v(\{1,2\})=1$.
- Majority: $v(\{i\})=0$, $v(S)=1$ for every other $S$.
- Landowner game: $v(S)=0$ if the landowner is not in $S$ (p. 238; the formula as printed is inconsistent with Example 237.1, see Reading notes).

**Two games without transferable payoff (p. 238).**
- *House allocation (238.1):* each of $n$ people owns one house; any subgroup may reassign its members' houses one per person. Cohesive. Not transferable: players 1 and 2 can achieve only $(v_1,w_2)$ or $(v_2,w_1)$, where $v_i$ ($w_i$) is player 1's (2's) payoff from house $i$.
- *Marriage market (238.2):* a coalition's actions are all matchings of its members into male–female pairs and singles. Cohesive (p. 239).

### 8.2 The core (pp. 239–243)

**Definition 239.1 (core).** The core is the set of actions $a_N$ of the grand coalition such that no coalition has an action that all its members prefer to $a_N$. A coalition that has such an action *can improve upon* $a_N$ (p. 239).

- The core is a set of actions, so it always exists, but may be empty. Then no grand-coalition action is immune to deviation (p. 239).
- Members of a deviating coalition need not guess other players' behaviour, so an interpretation of the core does not require experienced players. The main interpretations of Nash equilibrium and subgame perfect equilibrium do (p. 239).
- **Transferable payoff.** $S$ can improve upon $a_N$ if and only if $v(S)$ exceeds its members' total payoff in $a_N$. So $a_N$ is in the core if and only if
$$x_S(a_N)\ge v(S)\quad\text{for every coalition } S,$$
where $x_S(a_N)$ is the total payoff $a_N$ gives $S$'s members (p. 239).

*Intuition note.* With transferable payoff, a core action is "stable" in the sense that every group already gets at least what it could produce alone. Finding the core means writing one inequality per coalition and solving them together.

**Method (p. 240).** Check each grand-coalition action; for each coalition, require that it cannot make all its members better off.

**Example 240.1 (unanimity).** The core is all divisions $\{(x_1,x_2): x_1+x_2=1,\ x_i\ge0\}$: a single player gets nothing by deviating, and a different division hurts someone (p. 240). Variant where player 1 alone gets $p$ and player 2 alone gets $q$: the core is $\{(x_1,x_2): x_1+x_2=1,\ x_1\ge p,\ x_2\ge q\}$. If $p+q>1$ (the game is then not cohesive) the core is empty (p. 240).

**Example 240.2 (landowner, two workers).** $(x_1,x_2,x_3)$ is in the core if and only if
$$x_1\ge f(1),\ x_2\ge0,\ x_3\ge0,\ x_1+x_2\ge f(2),\ x_1+x_3\ge f(2),\ x_1+x_2+x_3=f(3).$$
Substituting $x_1=f(3)-x_2-x_3$ gives
$$0\le x_2\le f(3)-f(2),\quad 0\le x_3\le f(3)-f(2),\quad x_2+x_3\le f(3)-f(1).$$
Each worker gets at most the extra output of the third player, and the two workers together get at most the extra output of players 2 and 3 together (pp. 240–241).

**Exercise 241.1** asks for the empty core of the three-player majority game and the core when player 1 has three votes (p. 241).

**Example 241.2 (one owner, two buyers).** The owner holds one indivisible good and values only money. Each buyer has plenty of money and values the good at 1 unit of money. A coalition can assign the good and money among its members.

1. *The owner does not keep the good in any core action.* Let $a_N$ have the owner keep it, with buyers transferring $m_1,m_2$ to the owner. Take $a'_N$: the good goes to buyer 1, who pays $m_1+2\epsilon$; buyer 2 pays $m_2-\epsilon$; $0<\epsilon<\tfrac12$. Payoff changes: owner $+\epsilon$, buyer 1 $+(1-2\epsilon)$, buyer 2 $+\epsilon$. So $a_N$ is not in the core (pp. 241–242).
2. *If buyer 1 gets the good in a core action, she pays 1 and buyer 2 pays 0.* If buyer 2 pays something she improves by acting alone; if buyer 1 pays more than 1 she improves alone; if buyer 1 pays $m_1<1$, the owner and buyer 2 improve by trading at $\tfrac12(1+m_1)$ (owner gets more than $m_1$, buyer 2 a positive payoff) (p. 242).
3. *Conclusion:* the core has exactly two actions: the good goes to one buyer at price 1, so the winning buyer is no better off than if she did not trade. Competition between buyers causes this: any lower price is beaten by the owner and the *other* buyer (p. 242).

*Intuition note.* Core outcomes are those that survive all re-bargaining among groups. Here the owner and the losing buyer can always offer each other a deal that beats any price below 1.

Exercises 242.1 (heterogeneous buyers, valuations 1 and $v<1$) and 242.2 (vote trading over bills A, B, C, Figure 242.1, with three variants) follow (pp. 242–243).

### 8.3 Ownership and the distribution of wealth (pp. 243–247)

**Setup (p. 243).** $n\ge3$ people; $f(k)$ is output when $k$ people work all the land; $f$ increasing, $f(0)=0$, and $f(k)-f(k-1)$ decreasing in $k$ (Figure 243.1). Each person cares only about food she gets.

**8.3.1 Single landowner (pp. 243–245).**
- The action where the landowner takes all of $f(n)$ is in the core, because every producing coalition contains her and none can make her better off (pp. 243–244).
- Let the landowner be player 1. The coalitions best placed to deviate are the landowner plus all workers but one; they produce $f(n-1)$. So $(x_1+\dots+x_n)-x_j\ge f(n-1)$ for every worker $j$, which gives $x_j\le f(n)-f(n-1)$. Hence a core action has $0\le x_j\le f(n)-f(n-1)$ for every worker (p. 244).
- Exercise 244.1: every such action is in the core (hint given: $f(n)-f(k)\ge(n-k)(f(n)-f(n-1))$) (p. 244).
- **Result:** the core is all actions with $0\le x_i\le f(n)-f(n-1)$ for each worker and the landowner getting the rest. The marginal product of a worker is $f(n)-f(n-1)$; so each worker gets at most her marginal product. Competition among coalitions of the landowner and other workers holds shares down (p. 244).
- Exercise 244.2: if groups of fewer than $n-1$ workers refuse to work with the landowner, find the core (p. 244).

*Intuition note.* If one worker's share exceeds her marginal product, the other workers and the landowner can leave without her and all gain. So workers' own comrades limit what each can claim.

**Link to competitive equilibrium (p. 245).** Suppose the landowner can hire any number of workers at fixed wage $w$. Every worker wants to work if $w\ge0$; the landowner wants all $n-1$ workers if $w\le f(n)-f(n-1)$, and fewer if $w$ is higher. So supply equals demand if and only if $0\le w\le f(n)-f(n-1)$; each such $w$ is a competitive equilibrium (p. 245).

**Increasing marginal product (p. 245, Figure 245.1).** If each added worker adds more output than the previous one, no competitive equilibrium exists (the landowner wants indefinitely many workers). Exercise 245.1 asks to show the core contains the equal split, assuming $f(k)/k<f(k+1)/(k+1)$ (p. 245).

**8.3.2 Small landowners (p. 246).** Land is equally divided among all $n$ people; a coalition of $k$ people produces $(k/n)f(n)$. The equal split $f(n)/n$ is in the core, since each coalition receives exactly what it produces. No other action is: someone would get less than $f(n)/n$ and could improve alone. So the core is the single equal-split action (p. 246).

**8.3.3 Collective ownership (p. 246).** Any coalition of more than $n/2$ players can distribute all of $f(n)$ among its members; coalitions of at most $n/2$ players get nothing. The core is empty: in any grand-coalition action someone gets a positive amount, and the other players (a majority) can give her nothing and share everything. Osborne notes that if each player held a share entitling her to $1/n$ of output, a majority of $k$ could claim only $k/n$, and a stable distribution might exist. In this model that has no interesting implications because only one sensible land use exists; it might matter if there were choices of crops (pp. 246–247).

### 8.4 Exchanging homogeneous horses (pp. 247–252)

**8.4.1 Model (pp. 247–248).** Owners hold one indivisible horse each; nonowners hold only money. Player $i$ values a horse at $v_i$. Assumptions: at least two owners and two nonowners; some owner's valuation is below some nonowner's (a trade is worthwhile); some nonowner's valuation is below some owner's; no two valuations equal; money never constrains anyone; nobody wants more than one horse. Payoff: $v_i+r$ with a horse and $r$ more money than originally; $r$ without a horse. Actions of $S$: all allocations of $S$'s horses and money in which each player gets at most one horse. Coalitions are not restricted to bilateral trades (p. 248).

**8.4.2 Core (pp. 248–251).** Number owners in ascending order of valuation $\sigma_i$ and nonowners in descending order $\beta_i$ (Figure 249.1). Let $k^*$ be the largest $i$ with $\beta_i>\sigma_i$. Let $a_N$ be a core action; $L^*$ the owners who sell (no horse in $a_N$), $B^*$ the nonowners who buy; $|L^*|=|B^*|$ (conservation of horses). Let $r_i$ be money received by owner $i$ and $p_j$ the amount paid by nonowner $j$.

1. *Non-buyers have $p_j=0$.* If $p_j>0$, $j$ improves by keeping her money. If $p_j<0$, the coalition of everyone but $j$ copies the horse assignment and shares the money shortfall equally, each getting $|p_j|/(n-1)$ more (p. 249).
2. *Non-sellers have $r_i=0$* by a similar argument (p. 249).
3. *Uniform price.* If $r_i<p_j$ for a seller $i$ and buyer $j$, then $\{i,j\}$ improve by trading at $\tfrac12(r_i+p_j)$: $i$ gets $\tfrac12(r_i+p_j)>r_i$, $j$ gets $\beta_j-\tfrac12(r_i+p_j)>\beta_j-p_j$. So $r_i\ge p_j$ for all seller–buyer pairs. Money conserved and $|L^*|=|B^*|$ give $r_i=p_j=:p^*$ for all sellers and buyers (p. 249).
4. *Who trades.* An owner with valuation below $p^*$ must sell (otherwise she and a buyer could trade at a price between her valuation and $p^*$). An owner with valuation above $p^*$ does not sell (her payoff would be negative). Likewise, nonowners with valuation above $p^*$ buy and those below do not (p. 250).
5. *Range of $p^*$* (Exercise 250.1): $p^*\ge\max\{\sigma_{k^*},\beta_{k^*+1}\}$ and $p^*\le\min\{\beta_{k^*},\sigma_{k^*+1}\}$ (p. 250).
6. *Equal valuation trades.* If nonowner $i$'s valuation equals $p^*$, then owner $i$'s valuation is below $p^*$ and owner $i+1$'s is above (valuations are distinct), so exactly $i$ owners trade, so exactly $i$ nonowners trade, so nonowner $i$ trades. Symmetrically for owners (p. 250).

**Summary (250.2).** In every core action: (i) every nonowner who buys pays the same price; (ii) the price is at least $\max\{\sigma_{k^*},\beta_{k^*+1}\}$ and at most $\min\{\beta_{k^*},\sigma_{k^*+1}\}$; (iii) every owner whose valuation is at most the price sells; (iv) every nonowner whose valuation is at least the price gets a horse. Payoffs are $\max\{v_i,p^*\}$ for owners and $\max\{v_i,p^*\}-p^*$ for nonowners (p. 250).

**Every such action is in the core (pp. 250–251).** Given the optimal assignment of a coalition's horses (to its highest-valuing members; a horse moved from $i$ to $j$ with $v_i<v_j$, plus a money transfer between $v_i$ and $v_j$, helps both), money transfers cannot raise total payoff. So $S$ can improve upon $a_N$ if and only if its total payoff under $a_N$ is less than its total payoff with optimal horse assignment. Let $S$ have $\ell$ owners and $b$ nonowners, and let $S^*$ be its $\ell$ highest-valuation members. Optimal total payoff is $\sum_{i\in S^*}v_i$. Under $a_N$ the total is
$$\sum_{i\in S}\max\{v_i,p^*\}-bp^*=\sum_{i\in S^*}\max\{v_i,p^*\}+\sum_{i\in S\setminus S^*}\max\{v_i,p^*\}-bp^*.$$
The optimal total is never higher, because $S\setminus S^*$ has $b$ members, so $\sum_{S\setminus S^*}\max\{v_i,p^*\}-bp^*\ge0$, and $\max\{v_i,p^*\}\ge v_i$ (added step). Hence the core is exactly the set of actions satisfying (250.2) (p. 251).

*Intuition note.* A coalition can do no better than give horses to its highest-valuers. At the common price no group gains from regrouping. Under a core action each coalition's members together get at least as much as that best total.

**Comparison with competitive equilibrium (p. 251).** The outcome matches competitive equilibrium. But that theory *assumes* a single price and lets "market pressures" fix it. The core models each group's trading explicitly and *shows* uniform price is necessary. Exercises 251.1 (single owner) and 251.2 (owner with two horses; are prices uniform?) (pp. 251–252).

### 8.5 Exchanging heterogeneous houses (pp. 252–256)

**8.5.1 Model (p. 252).** Each of $n$ people owns one house; any subgroup may reassign its members' houses, one each. Each person has a strict ranking of houses. A *house exchange game* has the same form as Example 238.1. Osborne says that for any preferences a slight variant of the core yields a unique stable outcome (p. 252).

**8.5.2 Top trading cycle (pp. 252–254).**
- Anyone who owns her favourite house keeps it in every core assignment, since she can always keep her house (p. 252).
- Let $o(i)$ be the owner of $i$'s favourite house. With two people: if $o(1)=1$ or $o(2)=2$, the single core assignment is no trade. If $o(1)=2$ and $o(2)=1$ (a "2-cycle"), the single core assignment swaps houses (pp. 252–253). Longer cycles: $o(i)=j$, $o(j)=k$, $o(k)=i$ is a 3-cycle; $o(i)=i$ is a 1-cycle (p. 253).
- Three people: with at least two owning favourites, the single core assignment is no trade. With exactly one, she keeps hers and the other two are analysed as a two-player game. With none, a 2-cycle $ij$ gives the only core assignment (swap, third keeps hers). Otherwise $o(i)=j$, $o(j)=k$, $o(k)=i$ is a 3-cycle, and giving everyone her favourite is in the core (this does not show it is the only core assignment) (p. 253).
- **Top trading cycle procedure (p. 253).** Find cycles among the players' top-ranked houses and give each member of each cycle her favourite. Remove these players and houses, find cycles among the remaining top choices, and repeat until all are assigned.
- *Example (Figure 254.1).* Player 1 top $h_2$; player 2 top $h_1$; player 3 ranks $h_1,h_2,h_4,h_3$; player 4 ranks $h_3,h_2,h_4$. Round 1: $12$ is a 2-cycle, so 1 gets $h_2$ and 2 gets $h_1$. Round 2: $34$ is a 2-cycle, so 3 gets $h_4$ and 4 gets $h_3$. If player 3's ranking of $h_3,h_4$ were reversed, 3 would get $h_3$ in round 2 and 4 would get $h_4$ in round 3 (p. 254).
- **Result:** for any strict preferences, the top trading cycle assignment is in the core. *Argument:* players assigned in round 1 get their favourite, so no coalition containing one can improve. A coalition with round-2 players but no round-1 players lacks the round-1 houses, so its round-2 members already get their favourites among the houses it owns; similarly for later rounds (p. 254).
- Exercise 254.1: core when everyone has the same ranking (p. 254).

**8.5.3 Strong core (pp. 254–255).** The core may contain more than the TTC assignment. Take Figure 255.1: player 1 ranks $h_3,h_2,h_1$; player 2 ranks $h_1,h_2,h_3$; player 3 ranks $h_2,h_3,h_1$. $123$ is a 3-cycle, so TTC gives each her favourite. The assignment $a'_N$ (1 gets $h_2$, 2 gets $h_1$, 3 keeps $h_3$) is also in the core: player 2 has her favourite; players 1 and 3 alone cannot improve; coalition $\{1,3\}$ owns $h_1,h_3$ and giving $h_1$ to either leaves her worse off. But $N$ can give players 1 and 3 something better while 2 is unchanged, a "weak" improvement (p. 255).

**Definition (strong core, p. 255).** The strong core is the set of actions $a_N$ such that no coalition $S$ has an action $a_S$ that some of its members prefer to $a_N$ and all its members regard as at least as good. $a'_N$ is in the core but not the strong core.

**Result (proof omitted by Osborne):** for any strict preferences the strong core consists of the single assignment from the top trading cycle procedure (p. 255). Side effect: if players may be indifferent, the core of the strengthened kind may be empty (Exercise 255.1, Figure 256.1: find the core and show the strong core is empty) (pp. 255–256).

*Intuition note.* In house exchange, one simple procedure delivers the unique assignment that survives even "weak" deviations. If ties are allowed, the strengthened core may be empty (Exercise 255.1).

### 8.6 Voting (pp. 256–258)

**Modelling change (p. 256).** Any majority coalition may choose a policy that affects everyone; minorities are powerless. With an odd number of players, each with preferences over policies, the actions of a coalition containing a majority are all policies; every other coalition has a single action. A player prefers an outcome with a majority coalition to one without. The core is the set of grand-coalition actions that no majority coalition can improve upon (pp. 256–257).

**Core = Condorcet winner (p. 257).** If policy $x$ is in the core, no majority prefers another policy. So for every $y\ne x$ the players who prefer $x$ or are indifferent form a majority. With strict preferences, a majority prefers $x$ to every $y\neq x$, so $x$ is a *Condorcet winner* (a policy that a majority prefers to every other policy; Osborne refers to Exercise 74.1). There is at most one. So with strict preferences the core is empty if there is no Condorcet winner, and otherwise is the single Condorcet winner (p. 257).

**One dimension (p. 257).** A policy is a number, player $i$ has favourite $x_i^*$ and *single-peaked* preferences: if $x<x'<x_i^*$ or $x_i^*<x'<x$ then she prefers $x'$ to $x$. The median favourite position is the Condorcet winner and the unique core member (Exercise 257.1: median voter theorem).

**Higher dimensions (pp. 257–258).** Osborne says that for most configurations of preferences a Condorcet winner does not exist in two or more dimensions, so the core is empty. Illustration: three players with favourites $x_1^*,x_2^*,x_3^*$ (Figure 258.1), disliking a policy by its distance from the favourite. A policy $x$ is beaten by any policy in the lens where two players' circles overlap. By "checking a few other policies" Osborne says one can be convinced that no policy escapes all such lenses. A Condorcet winner exists only for special configurations, for example favourites on a line (the middle one) (p. 258).

**$q$-rule games (p. 258).** Fix $q$ with $n/2\le q\le n$; only coalitions with at least $q$ players choose policies. Roughly, the larger $q$, the larger the core. Exercise 258.1: core for single-peaked one-dimensional preferences, and for $q=3$ in the Figure 258.1 example.

*Intuition note.* Group deviation is what makes majority rule unstable: in several dimensions, for most configurations of preferences, any policy can be beaten by some majority.

### 8.7 Matching (pp. 259–265)

**8.7.1 Model (p. 259).** Two sides, X's and Y's. A *matching* $\mu$ splits a set of people into X–Y pairs and singles; $\mu(i)$ is $i$'s partner, $\mu(i)=i$ if single. Preferences are strict. $i$'s *acceptable partners* are those she prefers to being single. The *two-sided one-to-one matching game*: players all X's and Y's; actions of $S$ are all matchings of $S$; preferences depend only on one's partner (p. 259). Figure 260.1 gives example rankings.

**8.7.2 Core and deferred acceptance (pp. 259–262).**

*Core characterization (pp. 259–260).* A matching is in the core if and only if (a) each player prefers her partner to being single, and (b) for no X–Y pair $(i,j)$ does $i$ prefer $j$ to $\mu(i)$ and $j$ prefer $i$ to $\mu(j)$. *Proof:* if (a) fails a player improves alone; if (b) fails the pair improves. Conversely, if $\mu$ is not in the core, some $S$ has $\mu'$ preferred by all; if $S$ is a single player, (a) fails; otherwise take $i\in S$ and $j=\mu'(i)$: $i$ prefers $j$ to $\mu(i)$ and $j$ prefers $i$ to $\mu(j)$, so (b) fails (p. 260).

*Example (Figure 260.1).* $x_1$: $y_2,y_1$; $x_2$: $y_1,y_2,y_3$; $x_3$: $y_1,y_2$; $y_1$: $x_1,x_3,x_2$; $y_2$: $x_2,x_1,x_3$; $y_3$: $x_1,x_3,x_2$. Matching $\mu$: $(x_1,y_1),(x_2,y_2)$, with $x_3,y_3$ single, is in the core. Singles cannot improve because matched partners are acceptable. Pairs with $x_3$ or $y_3$ fail since $x_1,x_2$ prefer their partners to $y_3$ and $y_1,y_2$ prefer theirs to $x_3$. $\{x_1,y_2\}$ fails because $y_2$ prefers her partner $x_2$; $\{x_2,y_1\}$ fails because $y_1$ prefers $x_1$ (p. 260).

*Deferred acceptance with proposals by X's (pp. 260–261).* Each stage has two steps:
1. Each X (a) whose offer was rejected at the previous stage and (b) with some acceptable Y left proposes to her top-ranked Y among those who have not rejected her.
2. Each Y rejects every unacceptable proposer, and is engaged to the X she likes best among all who proposed to her and her previous fiancé.

It stops when no X's proposal is rejected or each rejected X has run out of acceptable Y's (p. 261).

*Trace (Figure 261.1).* Stage 1: $x_1\to y_2$; $x_2,x_3\to y_1$; $y_1$ rejects $x_2$. Stage 2: $x_2\to y_2$; $y_2$ keeps $x_2$, rejects $x_1$. Stage 3: $x_1\to y_1$; $y_1$ keeps $x_1$, rejects $x_3$. Stage 4: $x_3\to y_2$; rejected. Result: $(x_1,y_1),(x_2,y_2)$, with $x_3,y_3$ alone (p. 261).

*Why the result is in the core (pp. 261–262).* The procedure stops because there are finitely many players. By the characterization, check singles and pairs. No single player improves because no X proposes to an unacceptable Y and every Y rejects unacceptable X's. For a pair $(i,j)$ where $i$ (an X) prefers $j$ to $\mu(i)$: $i$ must have proposed to $j$ and been rejected before proposing to $\mu(i)$, so $j$ had a better proposal and prefers $\mu(j)$ to $i$ (p. 262).

*Other results (p. 262).* The Y-proposing version also gives a core matching. The two matchings may be the same or different. Osborne states that it "can be shown" that the X-proposing matching gives each X her most preferred core partner and each Y her least preferred; the Y-proposing version gives the reverse. Summary: every two-sided one-to-one matching game has a nonempty core containing both procedures' matchings; the procedure's matching is best in the core for the proposing side and worst for the other (p. 262). Exercises 262.1 and 262.2 (Figure 262.1).

**8.7.3 Variants (pp. 262–264).**
- *Strategic behaviour (p. 263).* In the strategic game where each player names a ranking and the outcome is the X-proposing deferred acceptance matching, one can show that each X's naming her true ranking is a dominant action. Equilibrium rankings of Y's may not be true, but the equilibrium outcome is in the core of the game defined by the true rankings. Exercise 263.1 (Figure 263.1).
- *Many-to-one (p. 263).* Under mild assumptions the results hold with minor changes; the strong core is nonempty and a variant of deferred acceptance generates matchings in it.
- *Roommate problem (pp. 263–264).* One-sided matching; Exercise 263.2 (Figure 264.1) shows a four-person example where, for any preferences of $\ell$ (everyone's least favourite), the core is empty. So core nonemptiness is not universal. Exercise 264.1 uses spatial preferences.

**Box: Matching doctors with hospitals (pp. 264–265).**
- Around 1900 US doctors could take internships. Competition for interns pushed agreements earlier, to two years ahead by 1944. Later attempts (information embargo; 10-day response in 1945; all offers at 12:01AM on 15 November from 1949) caused coordination problems and inefficient matches (p. 264).
- A centralized procedure was designed. Osborne says it yields a core matching for any stated preferences and, though differing from the many-to-one generalization of Gale–Shapley, the same matching, the one best for hospitals. The designers and Gale–Shapley learned of each other's work in the mid-1970s (pp. 264–265).
- Participation was over 95% early, around 85% in the mid-1970s. Many nonparticipants were married couples seeking posts in the same city. The couples mechanism could produce a matching a couple could improve on, and with such couples the core may be empty for some preferences (p. 265).
- In the 1990s student associations argued the procedure favoured hospitals and allowed strategic behaviour. Alvin E. Roth designed a new procedure, stable and as favourable as possible to applicants, first used in 1998, matching around 20,000 doctors a year (p. 265).

### 8.8 Other solution concepts (pp. 265–266)
The core assumes more than Nash equilibrium does. A single deviator is sure of her action. A member of a deviating group must assume no subgroup deviates further, or that she stays better off if it does (p. 265). *Example:* in the three-player majority game, $(\tfrac12,\tfrac12,0)$ is not in the core, because $\{1,3\}$ can get $(x,0,1-x)$ with $\tfrac12<x<1$. But $\{2,3\}$ can then offer $(0,y,1-y)$ with $0<y<x$, making both better off. That threat may dampen player 1's enthusiasm for joining player 3 (pp. 265–266). Other solution concepts address this, but none has so far had "anything like the success of the core" (p. 266).

### Notes (pp. 266–267)
Attributions as printed: coalitional games to von Neumann and Morgenstern (1944); the core introduced by Gillies in the early 1950s and developed by Shapley and Shubik; Section 8.3 based on Shapley and Shubik (1967); the horse market first studied by Shapley and Shubik (1971/72); median voter theorem to Black; Section 8.5 to Shapley and Scarf (1974), crediting Gale for TTC, with the strong-core result due to Roth and Postlewaite (1977); Section 8.7 to Gale and Shapley (1962), with the strategic results from Dubins–Freedman, Roth and others (p. 266–267).

## Toy example (ours, not from the text)
Three players, transferable payoff: $v(\{i\})=0$, $v(\{1,2\})=2$, $v(\{1,3\})=2$, $v(\{2,3\})=0$, $v(N)=3$. Think of player 1 as a landowner, as in Example 240.2.

Core conditions: $x_1,x_2,x_3\ge0$; $x_1+x_2\ge2$; $x_1+x_3\ge2$; $x_2+x_3\ge0$; $x_1+x_2+x_3=3$.

Substitute the sum. $x_1+x_2\ge2$ becomes $3-x_3\ge2$, so $x_3\le1$. $x_1+x_3\ge2$ becomes $x_2\le1$. $x_2+x_3\ge0$ is automatic. So the core is $0\le x_2\le1$, $0\le x_3\le1$, $x_1=3-x_2-x_3$.

- Check $(2,0.5,0.5)$: $x_1+x_2=2.5\ge2$, $x_1+x_3=2.5\ge2$, $x_2+x_3=1\ge0$, sum $=3$. In the core.
- Check $(0.5,1.25,1.25)$: $x_1+x_2=1.75<2$. Coalition $\{1,2\}$ can produce 2, enough to give both more. Not in the core.

Each non-landowner gets at most her marginal contribution $v(N)-v(\{1,\cdot\})=3-2=1$.

## Concepts
- [[coalitional-game]] (new) — model giving a set of actions to every coalition; actions of a coalition are taken as given (p. 235)
- [[cohesive-game]] (new) — the grand coalition can do at least as well for everyone as any partition into subgroups (p. 236)
- [[transferable-payoff]] (new) — a coalition's payoff possibilities are summarised by its total worth $v(S)$ (p. 238)
- [[core]] (new) — actions of the grand coalition that no coalition can improve upon (p. 239)
- [[strong-core]] (new) — actions that no coalition can make some members better off while leaving all at least as well off (p. 255)
- [[competitive-equilibrium]] (new) — wage or price at which demand equals supply, assuming a uniform price (pp. 245, 251)
- [[condorcet-winner]] (new) — policy preferred by a majority to every alternative; with strict preferences the core of majority voting is the Condorcet winner if one exists (p. 257)
- [[top-trading-cycle]] (new) — procedure assigning each member of a top-choice cycle her favourite house, then repeating (p. 253)
- [[deferred-acceptance]] (new) — proposal/rejection procedure producing a core matching, best for the proposing side (p. 260)
- [[nash-equilibrium]] — contrasted: rules out deviations by single players only (pp. 239, 256, 265)
- [[dominant-strategy]] — each X's naming her true ranking is dominant in the matching revelation game (p. 263)

## Canonical instances
- [[two-player-unanimity-game]] — core is all divisions; no coalition constrains $N$ (p. 240)
- [[landowner-worker-game]] — core gives workers at most marginal product (pp. 243–245)
- [[three-player-majority-game]] — empty core; illustrates unstable deviations (pp. 237, 241, 265)
- [[market-one-owner-two-buyers]] — price driven to 1 by buyer competition (pp. 241–242)
- [[horse-trading-game]] — uniform price in core, matches competitive equilibrium (pp. 247–251)
- [[house-exchange-game]] — top trading cycle; strong core is a single assignment (pp. 252–255)
- [[majority-voting-core]] — Condorcet winner; median voter theorem (pp. 256–258)
- [[two-sided-matching-game]] — marriage market with deferred acceptance (pp. 259–262)
- [[roommate-problem]] — a matching game with an empty core (p. 263)
- [[nrmp-doctor-hospital-matching]] — real-world centralized matching procedures (pp. 264–265)

## Bridges (candidates)
- [structural-analogy] core stability (no group profitable deviation) ↔ Nash equilibrium: no single player's profitable deviation — the core extends the deviation test from individuals to groups.
- [structural-analogy] core of the horse market ↔ competitive equilibrium (economics): same outcome, but uniform price derived rather than assumed.
- [structural-analogy] empty core in majority voting ↔ social choice: lack of a Condorcet winner in multidimensional policy space.
- [structural-analogy] deferred acceptance and its strategy-proofness for proposers ↔ mechanism design: incentive compatibility of a procedure (p. 263).

## Questions this raises
- When is the core nonempty for games with transferable payoff in general, given it is empty for the three-player majority game?
- How do the strong-core results for houses change if some players are indifferent (Exercise 255.1)?
- Since the core ignores further subgroup deviations (8.8), which alternative concepts fix this, and why have they been less useful?
- How does the Y-proposing procedure differ on Figure 260.1 (Exercise 262.1)?

## Exercises worth doing
- Ex. 241.1 (p. 241) — empty core of the majority game; core with a three-vote player — difficulty: easy
- Ex. 244.1 (p. 244) — verify the landowner–worker core claim — difficulty: medium
- Ex. 255.1 (p. 255) — strong core empty with ties — difficulty: medium
- Ex. 257.1 (p. 257) — median voter theorem — difficulty: medium
- Ex. 262.2 (p. 262) — run both deferred acceptance procedures and verify best/worst properties — difficulty: medium
- Ex. 263.2 (p. 263) — empty core in the roommate problem — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 8. The text is an author's draft (running header: "Draft chapter from An introduction to game theory", version 00/11/6, copyright 1995–2000), not the published book; cross-references (e.g. Definition 11.1, Exercise 74.1, Section 17.3) point outside this unit.
- Misprints visible in the images/text: p. 238 gives $N=\{1,\dots,m+1\}$ but lists workers as "$2,\dots,m$"; the worth formula $v(S)=f(k)$ for the landowner with $k$ workers conflicts with the output $f(k+1)$ of Example 237.1 and with Example 240.2 ($f(1)$ for the landowner alone). I followed the latter in L3.
- p. 249–250: the summary says "$r_i=p_i=p^*$", which should read $r_i=p_j$. On p. 249 the text writes $p_j/(n-1)$ extra money for a negative $p_j$; the amount that makes sense is $|p_j|/(n-1)$, which L3 uses.
- p. 255: "the core may be empty" when indifferences are allowed; the exercise (p. 256) concerns the strong core, which is the intended object.
- Minor typos: "aciton" (p. 256), "Secton" (p. 266), "Find the core the game" (p. 242).
- Exercise solutions are not printed in this unit.
