---
id: osborne-2004-introduction/ch13-evolutionary
work: osborne-2004-introduction
unit: "13 Evolutionary Equilibrium"
pages: 279–304
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
# Evolutionary Equilibrium (Osborne, ch. 13)

## L0 — One line
An action or mixed strategy is evolutionarily stable (an ESS) when it is a Nash equilibrium and also beats every rival best response in encounters between mutants, so that rare mutants die out.

## L1 — The gist (≤ 120 words)
How can game theory predict behaviour when organisms do not choose, but inherit behaviour and are sometimes mutated? Payoffs measure offspring. A strategy is evolutionarily stable if rare mutants do strictly worse than the normal population. Stability requires a Nash equilibrium plus a second test against alternative best responses. Strict equilibria always pass. In the symmetric Hawk–Dove game with costly injury ($c>v$), the only ESS is mixed. Some games have no ESS. With owner/intruder roles, pure conventions such as "bourgeois" are stable. Among siblings, shared genes change the stability conditions and can sustain cooperation. The chapter links Nash equilibrium to selection without conscious choice.

**Prerequisites:** symmetric strategic games; Nash equilibrium (strict and non-strict); mixed strategies and expected payoff; best response; basic probability and inequalities; one derivative (minimum).

## L2 — Key ideas
- Payoffs are biological fitness (expected offspring). Behaviour is inherited, or mutated rarely, and players do not choose (p. 279). This lets equilibrium logic apply without conscious decisions.
- A pure action $a^*$ is evolutionarily stable if rare mutants earn strictly less than normal organisms. This is equivalent to Definition 284.1: $(a^*,a^*)$ is a Nash equilibrium, and $u(b,b)<u(a^*,b)$ for every other best response $b$ (pp. 283–284).
- Every strict Nash equilibrium (one where each player's equilibrium action is the unique best response) is stable. Non-strict equilibria need the second condition, which asks how a mutant fares against other mutants (p. 284).
- With mixed strategies, the ESS (Def. 286.3) has the same two conditions. A pure-stable action need not be an ESS, because a mixed mutant can invade (pp. 286–288).
- A mixed ESS can be read as one population where each organism randomizes, or as a polymorphic population (several pure strategies coexisting) with fractions equal to the probabilities (pp. 288–289). In Hawk–Dove with $v\le c$, the ESS $(v/c,1-v/c)$ shows fights declining as injury cost rises (pp. 290–291).
- Some games have no ESS. In some of them mixed strategies are neutrally stable (mutants neither die out nor take over): all mixed strategies in the trivial game of Fig. 292.1. In Fig. 293.1 not even neutral stability exists (pp. 292–293).
- With asymmetric roles (owner/intruder) and $v<c$, $V<c$, Hawk–Dove has no mixed ESS and two pure ESSs: bourgeois (AP: aggressive as owner, passive as intruder) and paradoxical (PA: the reverse). In both, disputes end without fights (pp. 293–295).
- Among siblings, asexual reproduction means only actions maximizing $u(a^*,a^*)$ can be stable, and a strict maximum suffices (a Prisoner's Dilemma gives C). Sexual reproduction gives conditions on two transformed games $v$ and $w$ (pp. 296–301).
- For many-player interactions (digger wasps), the methods of the earlier sections are generalized (p. 301). The digger–invader mixed equilibrium is not evolutionarily stable (pp. 301–303).

## L3 — Walkthrough

### 13.1 Introduction (pp. 279–280)
- Darwinian theory: the modes of behaviour that survive are those most successful in producing offspring. Reproductive success may depend on what everyone else does, so game theory applies (p. 279).
- Players are representatives of an evolving population. Payoffs measure increments in biological fitness (e.g. expected number of healthy offspring), not subjective feelings. Actions are modes of behaviour the player is programmed to follow (p. 279).
- A mode of behaviour is inherited with high probability from the parent. With low but positive probability it is assigned by mutation. Mostly each player has a single parent and copies it. The author says this simple model captures the essential features of both genetic and social inheritance (learning by imitating parents) (p. 279).
- The author chooses each player's action set to contain every mode of behaviour that mutation will eventually generate (an assumption). If action $a$ gives more fitness than $a'$ given the others' behaviour, adherents of $a$ reproduce faster. Very roughly, adherents of actions that are not best responses are eventually overwhelmed, so the argument suggests that evolutionarily stable outcomes are related to Nash equilibria (p. 280).

### 13.2 Monomorphic pure strategy equilibrium

**13.2.1 Setting (p. 280).** One large population is repeatedly randomly matched in pairs. This is modelled as a symmetric strategic game in which $u(a,a')$ is the expected number of offspring of an organism taking $a$ against an opponent taking $a'$. Adherents multiply at a rate proportional to payoff. Reproduction is asexual. A configuration is stable if, when a small fraction of mutants taking the same action appears, every mutant's expected payoff is lower than that of any nonmutant. The case of several mutant types at once is ignored. "Monomorphic" means "one form": all organisms except mutants use the same non-random action (pp. 280–281).

**13.2.2 Examples (pp. 281–282).** Left game of Fig. 281.1: payoffs (X,X)=2,2; (Y,Y)=1,1; off-diagonal 0,0. Right game: same except (Y,Y)=0,0.
- Left game, all normal organisms take X, mutant fraction $\epsilon$ takes Y. Normal payoff $2(1-\epsilon)+0\cdot\epsilon=2(1-\epsilon)$. Mutant payoff $0\cdot(1-\epsilon)+1\cdot\epsilon=\epsilon$. For small $\epsilon$ the first exceeds the second, so X is evolutionarily stable (p. 281).
- Left game, normal action Y: normal payoff $1-\epsilon$, mutant (taking X) payoff $2\epsilon$. For small $\epsilon$ the normal payoff is larger, so Y is also stable. The critical $\epsilon$ is smaller than for X, but the author attaches no significance to its size. Only the existence of some critical value matters (p. 281).
- Right game: X is stable by a similar argument. If normal is Y, a normal organism gets 0 against both types, and an X-mutant gets 2 against a mutant and 0 against a normal. The mutant is better off for any $\epsilon$, so Y is not stable (pp. 281–282).
- Both games have (X,X) and (Y,Y) as Nash equilibria. The essential difference is $u(X,Y)<u(Y,Y)$ in the left game but $u(X,Y)=u(Y,Y)$ in the right game. In the right game a mutant loses nothing against normals, so any gain against other mutants wins (p. 282).

**13.2.3 General definitions (pp. 282–284).** Take a symmetric game with finitely many actions. Mutants take $b\ne a^*$ with fraction $\epsilon$. Stability here is strong: mutants must be driven out, and merely equal payoffs would not count (p. 282). Expected payoffs:
- mutant: $(1-\epsilon)u(b,a^*)+\epsilon u(b,b)$;
- normal: $(1-\epsilon)u(a^*,a^*)+\epsilon u(a^*,b)$.

Mutants die out if
$$(1-\epsilon)u(a^*,a^*)+\epsilon u(a^*,b) > (1-\epsilon)u(b,a^*)+\epsilon u(b,b)\quad\text{for all } b\neq a^*. \tag{283.1}$$

**Definition.** $a^*$ is evolutionarily stable if there exists $\bar\epsilon>0$ such that $a^*$ satisfies (283.1) for all $\epsilon<\bar\epsilon$ (p. 283).

The author reformulates this to avoid $\bar\epsilon$ (pp. 283–284):
1. *Necessity of Nash.* Suppose $(a^*,a^*)$ is not a Nash equilibrium. Then some $b$ has $u(b,a^*)>u(a^*,a^*)$. So (283.1) is strictly violated at $\epsilon=0$, and hence for all sufficiently small $\epsilon>0$. (If $w<x$ and $y,z$ are any numbers, then $(1-\epsilon)w+\epsilon y<(1-\epsilon)x+\epsilon z$ for small enough $\epsilon$.) So no $\bar\epsilon$ exists. Hence being a Nash equilibrium is necessary (p. 283).
2. *Sufficiency of strictness.* If $(a^*,a^*)$ is a strict Nash equilibrium, then $u(b,a^*)<u(a^*,a^*)$ for all $b$. So (283.1) holds strictly at $\epsilon=0$ and for small positive $\epsilon$. Hence strictness is sufficient (p. 283).
3. *Non-strict equilibrium.* If $b\ne a^*$ is a best response to $a^*$, so $u(b,a^*)=u(a^*,a^*)$, then (283.1) reduces to $u(a^*,b)>u(b,b)$. Then $a^*$ is stable if and only if this holds (p. 283).

**Definition 284.1.** An action $a^*$ in a symmetric two-player game is *evolutionarily stable with respect to mutants using pure strategies* if
- $(a^*,a^*)$ is a Nash equilibrium, and
- $u(b,b)<u(a^*,b)$ for every best response $b$ to $a^*$ with $b\ne a^*$ (p. 284).

For a strict Nash equilibrium the only best response is $a^*$, so the second condition holds vacuously. The inequality is strict, because equality would admit mutants that neither multiply nor die out (p. 284).

*Intuition note.* A stable action must be a best response to itself, so no mutant does better against the normals. A mutant that does equally well against normals must do worse against other mutants. Otherwise mutants could reproduce as fast as the normals or faster.

**13.2.4 Examples (pp. 284–286).**
- Left game of Fig. 281.1: both (X,X) and (Y,Y) are strict, so both X and Y are stable. Right game: (X,X) is strict, (Y,Y) is not. X is a best response to Y with $u(X,X)>u(Y,X)$, so Y fails the second condition and only X is stable (p. 284).
- Prisoner's Dilemma: unique symmetric Nash equilibrium (D,D), strict, so D is the only stable action. BoS has no symmetric pure Nash equilibrium, hence no stable action in the pure sense (p. 284).
- **Hawk–Dove (Example 284.2).** Two animals contest a resource of value $v>0$. Each is aggressive (A) or passive (P). If both are aggressive they fight, each wins with probability ½, and the loser suffers a loss $c$. So each gets $\tfrac12 v+\tfrac12(-c)=\tfrac12(v-c)$. If both are passive each gets the resource with probability ½, so $\tfrac12 v$. If A meets P, the aggressor gets $v$ and the passive animal 0 (pp. 284–285). Payoffs (Fig. 285.1): (A,A) $=\tfrac12(v-c),\tfrac12(v-c)$; (A,P) $=v,0$; (P,A) $=0,v$; (P,P) $=\tfrac12 v,\tfrac12 v$.
  - $v>c$: unique Nash equilibrium (A,A), strict, so A is the unique stable action (p. 285).
  - $v=c$: (A,A) is the unique Nash equilibrium but not strict. The second condition holds: $v/2=u(P,P)<u(A,P)=v$. So A is the unique stable action (pp. 285–286).
  - In both cases a passive population can be invaded by aggressive mutants (p. 286).
  - $v<c$: no symmetric pure Nash equilibrium, so no stable action. Only asymmetric Nash equilibria exist (p. 286).

The text also has a history box (p. 285). It reports that Darwin gave an implicit game-theoretic argument for a 50:50 sex ratio in 1871. Hamilton (1967) proposed an explicit model of sex-ratio evolution. Maynard Smith (1972a) and Maynard Smith and Price (1973) introduced the evolutionarily stable strategy.

Exercises 286.1 and 286.2 follow here (see Exercises). The author names three routes for games with no stable action: mixed strategies, polymorphic populations, and asymmetric equilibria. The first two come next (p. 286).

### 13.3 Mixed strategies and polymorphic equilibrium

**13.3.1 Definition (pp. 286–287).** If mixed strategies can be inherited and mutated, an analogous argument gives:

**Definition 286.3.** An *evolutionarily stable strategy* (ESS) in a symmetric two-player game is a mixed strategy $\alpha^*$ such that
- $(\alpha^*,\alpha^*)$ is a Nash equilibrium, and
- $U(\beta,\beta)<U(\alpha^*,\beta)$ for every best response $\beta\ne\alpha^*$ to $\alpha^*$,

where $U(\alpha,\alpha')$ is the expected payoff of a player using $\alpha$ against $\alpha'$ (pp. 286–287).

Can animals randomize? **Maynard Smith's argument** is that a randomizing device could evolve if advantageous. He says that "[p]erhaps the one undoubted example of a mixed ESS" is the production of equal numbers of X and Y gametes by the heterogametic sex: "if the gonads can do it, why not the brain?" (p. 287). Brockmann et al. (1979) give evidence that certain wasps use mixed strategies (p. 287).

**13.3.2 Pure versus mixed (pp. 287–288).** A pure strategy is a special case of a mixed one. If $a^*$ is stable in the sense of Def. 284.1, then $(\alpha^*,\alpha^*)$ is a mixed Nash equilibrium. But $\alpha^*$ (probability 1 on $a^*$) need not be an ESS, since a mixed mutant may invade (p. 287).

Game of Fig. 287.1 (row, column payoffs):

| | X | Y | Z |
|---|---|---|---|
| X | 2, 2 | 1, 2 | 1, 2 |
| Y | 2, 1 | 0, 0 | 3, 3 |
| Z | 2, 1 | 3, 3 | 0, 0 |

- X is stable in the Def. 284.1 sense. (X,X) is a Nash equilibrium, and the other best responses Y, Z satisfy $u(Y,Y)=0<1=u(X,Y)$ and $u(Z,Z)=0<1=u(X,Z)$ (p. 288).
- Let $\beta=(\tfrac12 \text{ on } Y,\ \tfrac12 \text{ on } Z)$. It is a best response to X, since Y and Z are. Against itself the outcomes (Y,Y), (Y,Z), (Z,Y), (Z,Z) each have probability ¼. So $U(\beta,\beta)=\tfrac14\cdot0+\tfrac14\cdot3+\tfrac14\cdot3+\tfrac14\cdot0=\tfrac32$. Also $U(\alpha^*,\beta)=1$. Since $U(\alpha^*,\beta)=1<\tfrac32=U(\beta,\beta)$, the mixed mutant $\beta$ invades, and X is not an ESS (p. 288).
- Reason: Y types do poorly against each other, and so do Z types, but a Y–Z pair is very productive. Mutants that mix meet a different type half the time (p. 288).

*Intuition note.* Stability against pure mutants is weaker than stability against all mixed mutants. A mixed mutant can gain because two mutants who meet are of different, complementary types half the time.

**13.3.3 Strict equilibria (p. 288).** A strict Nash equilibrium is an ESS (vacuous second condition). No mixed equilibrium that puts positive probability on two or more actions is strict. In a mixed equilibrium every action in the support is a best response, and so is every mixed strategy with the same support (Prop. 111.1). So the second condition is never vacuous there. One must check $U(\beta,\beta)<U(\alpha^*,\beta)$ for every $\beta\ne\alpha^*$ with the same support (p. 288).

**13.3.4 Polymorphic steady states (pp. 288–289).** A mixed ESS corresponds either to a monomorphic state (each organism randomizes with the mixed strategy's probabilities) or to a polymorphic state (several pure strategies coexist, each with the population fraction equal to its probability). The earlier argument for pure monomorphic states carries over to the monomorphic mixed case. A different argument (Hammerstein and Selten 1994, 948–951) shows the two ESS conditions are also necessary and sufficient for stability of a polymorphic steady state: mutations that change the fractions cause payoff changes that push the fractions back (p. 289).

**13.3.5 Examples (pp. 289–291).**
- **Example 289.1 (BoS).** Payoffs (L,L) $=0,0$; (L,D) $=2,1$; (D,L) $=1,2$; (D,D) $=0,0$. The unique symmetric equilibrium is $\alpha^*=(\tfrac23,\tfrac13)$. Let $\beta=(p,1-p)$. Against $\beta$ itself, (L,D) and (D,L) each have probability $p(1-p)$, so $U(\beta,\beta)=3p(1-p)$. Also $U(\alpha^*,\beta)=\tfrac43-p$. We need $3p(1-p)<\tfrac43-p$ for all $p\ne\tfrac23$. This is equivalent to $(p-\tfrac23)^2>0$, which is true. So $\alpha^*$ is an ESS (p. 289).
- **Example 289.2 (coordination game, Fig. 290.1).** (X,X) $=2,2$; (Y,Y) $=1,1$; off-diagonal $0,0$. X and Y are strict, hence ESSs. The mixed equilibrium $\alpha^*=(\tfrac13,\tfrac23)$ is not an ESS: with $\beta=(1,0)$, $U(\beta,\beta)=2$ and $U(\alpha^*,\beta)=\tfrac23$. An X-mutant does better than normals against both mutants and normals. In fact, a mutant following any strategy different from $\alpha^*$ invades. So there is no mixed ESS (p. 290).
- **Example 290.1 (mixed Hawk–Dove).** If $v>c$, the only ESS is A. If $v\le c$, the unique symmetric mixed equilibrium is $\alpha^*=(v/c,\,1-v/c)$. Let $\beta=(p,1-p)$. Then
$$U(\beta,\beta)=p^2\cdot\tfrac12(v-c)+p(1-p)\,v+p(1-p)\cdot0+(1-p)^2\cdot\tfrac12 v,$$
$$U(\alpha^*,\beta)=(v/c)\,p\cdot\tfrac12(v-c)+(v/c)(1-p)\,v+(1-v/c)(1-p)\cdot\tfrac12 v.$$
The author states that on simplification
$$U(\alpha^*,\beta)-U(\beta,\beta)=\tfrac12 c\,(v/c-p)^2,$$
which is positive if $p\ne v/c$. So $\alpha^*$ is the unique ESS when $v\le c$ (p. 290).
- Interpretation. If $c\le v$, only aggression survives. If $c>v$, a pure A population is invaded by passive mutants and a pure P population by aggressive ones, so the only ESS is mixed. It can be read as a fraction $v/c$ aggressive and $1-v/c$ passive. As injury cost rises, the aggressive fraction falls, fights become rarer, and more disputes end "conventionally" (pp. 290–291).

*Intuition note.* When fighting is costly, neither pure type can hold the population. The mix settles where aggressive and passive animals do equally well. The formula $\tfrac12 c(v/c-p)^2$ shows that any deviation from that mix earns less than $\alpha^*$ does against it.

Exercises 291.1–291.3 follow (see Exercises).

- **Example 292.1 (War of attrition, symmetric, $v_1=v_2=v$).** Actions are display times, and the longest display wins. The only symmetric equilibrium is mixed with distribution function $F(t)=1-e^{-t/v}$. It gives positive probability to every interval, so every strategy is a best response. So it is an ESS if and only if $U(G,G)<U(F,G)$ for every $G\ne F$. The author calls the full proof difficult and checks only pure $G$ (the action $a$). Then $U(G,G)=\tfrac12 v-a$ and
$$U(F,G)=\int_0^a(-s)F'(s)\,ds+(1-F(a))(v-a)=v\,(2e^{-a/v}-1).$$
So $U(F,G)-U(G,G)=2ve^{-a/v}-\tfrac32 v+a$, which is positive for all $a$ (find the minimum by setting the derivative to zero). *(added step:)* the derivative $-2e^{-a/v}+1$ vanishes at $a=v\ln 2$, where the expression equals $v(\ln 2-\tfrac12)>0$. So no pure-strategy mutant can invade (p. 292).

**13.3.6 Games with no ESS (pp. 292–293).**
- Trivial game of Fig. 292.1 (all payoffs 1,1). Every mixed $\alpha$ gives a Nash equilibrium $(\alpha,\alpha)$. But $U(X,X)=1=U(\alpha,X)$ violates the second condition. A mutant using X reproduces at the same rate, so it neither dies out nor dominates. There is no ESS, but every mixed strategy is *neutrally stable* (the author's term: mutants do not die out but also do not take over) (p. 292).
- Fig. 293.1, with $\gamma>0$: payoffs on the diagonal $\gamma,\gamma$; (A,B) $=-1,1$; (A,C) $=1,-1$; (B,A) $=1,-1$; (B,C) $=-1,1$; (C,A) $=-1,1$; (C,B) $=1,-1$. If $\gamma=0$ it would be Rock, paper, scissors. The unique symmetric Nash equilibrium is $\alpha^*=(\tfrac13,\tfrac13,\tfrac13)$. Every pure strategy $a$ is a best response, and $U(a,a)=\gamma>\gamma/3=U(\alpha^*,a)$. This violates the second condition strictly, so there is not even a neutrally stable strategy. Evolutionary stability, even in weak form, makes no prediction for this game (p. 293).

### 13.4 Asymmetric equilibria

**13.4.1 Introduction (p. 293).** In a heterogeneous population (players differ in size, weight, ownership status, etc.), asymmetric equilibria may be relevant even if the differences do not affect payoffs. The author restricts attention to one example.

**13.4.2 Hawk–Dove with owner and intruder (pp. 293–295).** One animal is the owner and the other the intruder, each with probability ½ in any given encounter. A strategy specifies the action as owner and as intruder: AA, AP, PA, PP (the first letter is the owner action). The owner values the site at $V$ and the intruder at $v$, with $v<c$ and $V<c$ (p. 294). Example: AA against AP. With probability ½ the AA animal is owner and gets $V$ (actions (A,P)). With probability ½ it is intruder and gets $\tfrac12(v-c)$ (actions (A,A)). So its payoff is $\tfrac12V+\tfrac14(v-c)=\tfrac14(2V+v-c)$ (p. 294).

Fig. 294.1, row player's payoffs ×4 (the game is symmetric):

| | AA | AP | PA | PP |
|---|---|---|---|---|
| AA | $V+v-2c$ | $2V+v-c$ | $V+2v-c$ | $2V+2v$ |
| AP | $V-c$ | $2V$ | $V+v-c$ | $2V+v$ |
| PA | $v-c$ | $V+v-c$ | $2v$ | $V+2v$ |
| PP | $0$ | $V$ | $v$ | $V+v$ |

- (AP,AP) and (PA,PA) are strict symmetric Nash equilibria, so AP and PA are ESSs whatever the relative sizes of $v$ and $V$ (p. 294).
- A mixed ESS $\alpha^*$ would make $(\alpha^*,\alpha^*)$ a mixed equilibrium. Suppose $\alpha^*$ put positive probability on AP. Then AP would be a best response to $\alpha^*$, and an ESS would need $U(AP,AP)<U(\alpha^*,AP)$. This contradicts (AP,AP) being a Nash equilibrium. So $\alpha^*$ gives AP zero probability, and likewise PA. Exercise 295.1 asks the reader to show that there is no symmetric mixed equilibrium supported only on AA and PP. Conclusion: no mixed ESS (pp. 294–295).
- Result for $v<c$, $V<c$: two ESSs. In the **bourgeois** strategy (AP) the player is aggressive as owner and passive as intruder, so the intruder concedes. In the **paradoxical** strategy (PA) the owner concedes. Both resolve disputes without a fight. The bourgeois strategy has many examples in nature. The paradoxical strategy leads to constant role change, since the intruder becomes the owner (p. 295).

*Intuition note.* An arbitrary asymmetry such as ownership can act as a convention. If everyone follows the rule "owner fights, intruder yields", nobody gains by deviating. Hence stable peaceful outcomes arise even though no symmetric pure equilibrium existed in the original game.

**Box "Explaining the outcomes of contests in nature" (pp. 295–296; marked "rough" in the draft).** Earlier theory said conflicts end without a fight because it is not in the species' interest to lose members. The author says this theory does not explain how individual-level evolution could produce species-benefiting behaviour. It also says nothing on when peaceful resolution is likely. The game-theoretic analysis at the individual level suggests that in a symmetric contest the relation between resource value and escalation cost determines escalation. In an asymmetric contest, no escalation is predicted regardless of value and cost, and "owner always wins" is stable. For funnel web spiders (*Agelenopsis aperta*), the owner usually wins when weights are similar and the heavier spider wins when weights differ. Hammerstein and Riechert (1988) estimate fitnesses from field observations and conclude that the ESS gives good predictions (pp. 295–296).

Exercises 295.1, 295.2, 296.1 appear in this section (see Exercises).

### 13.5 Variation on a theme: sibling behavior (pp. 296–301)
Matching is no longer uniformly random. Players interact with siblings. Pairwise play, fitness payoffs, and pure strategies only are retained (p. 296).

**13.5.1 Asexual reproduction (pp. 296–297).** All offspring of a mutant using $b$ inherit $b$. So their payoff with siblings is $u(b,b)$, against $u(a^*,a^*)$ for normals. Mutant behaviour $b$ invades if and only if $u(b,b)>u(a^*,a^*)$ and is driven out if and only if $u(b,b)<u(a^*,a^*)$. Hence:

> If $a^*$ is evolutionarily stable then $u(a^*,a^*)\ge u(b,b)$ for every $b$; if $u(a^*,a^*)>u(b,b)$ for every $b$ then $a^*$ is evolutionarily stable. (p. 297)

No Nash requirement appears. In the Prisoner's Dilemma of Fig. 297.1 (CC $=2,2$; CD $=0,3$; DC $=3,0$; DD $=1,1$), the only stable action between siblings is C, against D between unrelated organisms. One may think of it as each player assuming its sibling copies its action. The conclusion relies on asexual reproduction. Bergstrom (1995) is quoted as saying careful observers of human siblings will not be surprised that sexual species' behaviour is not so perfectly cooperative (p. 297).

**13.5.2 Sexual reproduction (pp. 297–301).** Genes are the unit of analysis. Each animal has two genes. Each offspring gets one randomly chosen gene from each parent, and this pair is its genotype. Genotype $xx$ is programmed to take action $a$ and $XX$ takes $b\ne a$. In an $xx\times XX$ mating all offspring are $Xx$. If they take $b$, $X$ is dominant. If they take $a$, $X$ is recessive. Mating is monogamous, so siblings share both parents. Animals differ in survival chance to adulthood, not in fecundity (pp. 297–298). The question is whether a population of $xx$ animals choosing $a^*$ resists a mutant gene $X$ (p. 298).

*Dominant $X$* (action $b\ne a^*$ for $XX$ and $Xx$):
- Almost every mutant $Xx$ has one $xx$ parent. Each of its siblings is $xx$ with probability ½ and $Xx$ with probability ½ (p. 298).
- A mutant's expected payoff is $\tfrac12 u(b,a^*)+\tfrac12 u(b,b)$. A normal $xx$ in a normal family has all siblings $xx$ and gets $u(a^*,a^*)$ (p. 298).
- So no dominant mutant gene can invade if $\tfrac12 u(b,a^*)+\tfrac12 u(b,b)<u(a^*,a^*)$ for every $b$. A dominant mutant can invade if this inequality is reversed for some $b$ (pp. 298–299).
- Define $v(b,a)=\tfrac12 u(b,a)+\tfrac12 u(b,b)$. Since $v(a,a)=u(a,a)$, the condition is $v(b,a^*)<v(a^*,a^*)$ for all $b$. This says $(a^*,a^*)$ is a strict Nash equilibrium of the game with payoff $v$ (sufficient). Being a Nash equilibrium of this game is necessary (p. 299).

*Recessive $X$* ($Xx$ takes $a^*$):
- In families $xx\times Xx$, all offspring take $a^*$ and get $u(a^*,a^*)$. So $X$ neither invades nor is eliminated at this level. One must look at the next smallest group, families with two $Xx$ parents, where a fourth of offspring are $XX$ (p. 299).
- In those families offspring are ¼ $xx$, ½ $Xx$, ¼ $XX$. The author omits the details of the pairwise-sibling analysis and states that the expected payoff of an $X$ gene is
$$\tfrac18 u(b,b)+\tfrac18 u(a^*,b)+\tfrac38 u(b,a^*)+\tfrac38 u(a^*,a^*).$$
The normal gene's payoff is $u(a^*,a^*)$ (p. 299).
- No invasion if $\tfrac18u(b,b)+\tfrac18u(a^*,b)+\tfrac38u(b,a^*)+\tfrac38u(a^*,a^*)<u(a^*,a^*)$, which the author rewrites as $\tfrac15u(b,b)+\tfrac15u(a^*,b)+\tfrac35u(b,a^*)<u(a^*,a^*)$ (p. 300).
- Define $w(a,b)=\tfrac15u(a,a)+\tfrac15u(b,a)+\tfrac35u(a,b)$. The condition becomes $w(b,a^*)<w(a^*,a^*)$ for all $b$. So a strict Nash equilibrium of the game with payoff $w$ is sufficient, and a Nash equilibrium is necessary (p. 300).

**Evolutionary stability (p. 300).** The action must resist both dominant and recessive invaders. If $(a^*,a^*)$ is a strict Nash equilibrium of both the $v$-game and the $w$-game, a population of $xx$ players choosing $a^*$ is evolutionarily stable. If $(a^*,a^*)$ is not a Nash equilibrium of both games, $a^*$ is not stable (p. 300). The earlier necessary conditions are stated for each game separately, so failing either game rules out stability.

**Prisoner's Dilemma applications.**
- Fig. 300.1: $u$: CC $=5,5$; CD $=0,6$; DC $=6,0$; DD $=2,2$. The derived games: $v$ has CD $=\tfrac52,4$, DC $=4,\tfrac52$, with the diagonal unchanged. $w$ has CD $=\tfrac{11}{5},4$, DC $=4,\tfrac{11}{5}$, with the diagonal unchanged. (C,C) is a Nash equilibrium of both and (D,D) of neither. So C is the only stable action (p. 300).
- Fig. 301.1: $u$: CC $=3,3$; CD $=0,6$; DC $=6,0$; DD $=2,2$. In $v$, CD $=\tfrac32,4$. In $w$, CD $=\tfrac95,4$. Here (D,D) is a Nash equilibrium of both games and (C,C) of neither. So D is the only stable action (pp. 300–301).
- Conclusion: when the gain from defecting is small, cooperation is evolutionarily stable, because of siblings' genetic similarity. When it is large enough, relatedness cannot overcome the pressure to defect (p. 301).

*Intuition note.* Siblings share genes, so a mutant's siblings tend to behave like it. In $v$, a player's payoff is the average of its original payoff and the payoff it would get if its sibling mimicked it; $w$ is a similar weighted mix. In the Prisoner's Dilemma examples, cooperation is stable when the gain from defecting is small (p. 301).

Exercise 301.1 follows (see Exercises).

### 13.6 Variation on a theme: nesting behavior of wasps (pp. 301–303)
Here the payoff depends on the whole population, not on a pairwise interaction (p. 301).

**Model.** Female great golden digger wasps (*Sphex ichneumoneus*) lay eggs in burrows stocked with katydids. Each wasp digs its own burrow or invades one. An invader fights the occupant and loses with probability $\pi$. Payoff is eggs per unit time, with one egg per nest. Let $T_d$ be the time to build and stock a burrow and $T_i$ the time spent by an invader on a nest, with $T_i<T_d$ (p. 302).
- Let $p$ be the fraction who dig. A digger can invade $T_d/T_i$ nests per period $T_d$, and there are $(1-p)/p$ invaders per digger. So the probability a digger is invaded is $q=\dfrac{1-p}{p}\dfrac{T_d}{T_i}=\dfrac{(1-p)T_d}{pT_i}$, assuming this is at most 1 (p. 302).
- A digger faces this lottery: not invaded with probability $1-q$, invaded and wins with probability $q\pi$, invaded and loses with probability $q(1-\pi)$ (whole time $T_d$ wasted). Its payoff is $(1-q+q\pi)/T_d$. An invader's payoff is $(1-\pi)/T_i$ (p. 302).

**Equilibria (p. 302).**
1. All dig: this is an equilibrium if $1/T_d\ge(1-\pi)/T_i$, since then $q=0$ and digging pays at least as much as invading.
2. All invade: clearly not an equilibrium, because there would be no nests to invade.
3. Coexistence: equal payoffs, $(1-q+q\pi)/T_d=(1-\pi)/T_i$. Substituting $q=(1-p)T_d/(pT_i)$ gives $p=(1-\pi)T_d/T_i$. Then $q\le1$ if $\pi T_i\le(1-\pi)T_d$, so this is indeed an equilibrium.

**Stability (pp. 302–303).**
- The all-dig equilibrium is stable if $1/T_d>(1-\pi)/T_i$. Then invading mutants earn less and die out. The knife-edge case of equality is not considered (p. 302).
- The coexistence equilibrium is not evolutionarily stable. A small rise in $p$ lowers $q$, so digging pays more while invading's payoff is unchanged. Diggers prosper relative to invaders and $p$ rises further (pp. 302–303).
- The polymorphic equilibrium can be read as a mixed equilibrium in which each wasp digs with probability $p$. In the populations Brockmann et al. (1979) observed, digging and invading coexist, and individual wasps do both. This raises the question of how the model could be modified so that the mixed equilibrium is evolutionarily stable. Brockmann et al. suggest two variants. In one, a digger is better off if she is invaded and wins than if she is not invaded (the invader may have helped stock the nest). Their data from one site fit the predicted $p$ very well and the data from another do not (p. 303).

Exercise 303.1 (Darwin's sex ratio) follows (see Exercises).

**Notes (pp. 303–304; marked "[Incomplete.]").** Main ideas are due to Maynard Smith. The chapter draws on Hammerstein and Selten (1994) and van Damme (1987, ch. 9). Darwin's sex-ratio theory was found independently by Fisher (1930), and Darwin retracted it in the second edition (1874) for reasons not apparent. Bulmer (1994) seems to have been first to notice that "Fisher's theory" was Darwin's. Hawk–Dove is due to Maynard Smith and Price (1973). Section 13.4 follows van Damme (1987, §9.5). Ex. 295.2 is a slightly less general version of Lemma 9.2.4 of van Damme. Section 13.5 is from Bergstrom (1995). Section 13.6 is from Brockmann, Grafen and Dawkins (1979), simplified along the lines of Bergstrom and Varian (1987, 324–327) (p. 304).

## Toy example (ours, not from the text)
Hawk–Dove with $v=2$, $c=4$. Payoffs from Fig. 285.1: $u(A,A)=\tfrac12(2-4)=-1$, $u(A,P)=2$, $u(P,A)=0$, $u(P,P)=1$.
- No pure ESS (matches $v<c$). Mutant P in a normal A population at fraction $\epsilon$: normal $(1-\epsilon)(-1)+\epsilon\cdot2=-1+3\epsilon$; mutant $(1-\epsilon)\cdot0+\epsilon\cdot1=\epsilon$. The mutant wins when $\epsilon>-1+3\epsilon$, i.e. $\epsilon<\tfrac12$. So every small $\epsilon$ invades. Mutant A in a normal P population: normal $1-\epsilon$; mutant $2(1-\epsilon)+(-1)\epsilon=2-3\epsilon$. The mutant wins when $2-3\epsilon>1-\epsilon$, i.e. $\epsilon<\tfrac12$.
- Mixed equilibrium $\alpha^*=(v/c,1-v/c)=(\tfrac12,\tfrac12)$. Against $\alpha^*$, A earns $\tfrac12(-1)+\tfrac12(2)=0.5$ and P earns $\tfrac12(0)+\tfrac12(1)=0.5$. So $\alpha^*$ is a Nash equilibrium and all strategies are best responses.
- Second condition, with the formula $U(\alpha^*,\beta)-U(\beta,\beta)=\tfrac12c(v/c-p)^2=2(\tfrac12-p)^2$.
  - $\beta=$ pure A ($p=1$): $U(\beta,\beta)=-1$; $U(\alpha^*,A)=\tfrac12(-1)+\tfrac12(0)=-0.5$; difference $0.5=2\cdot\tfrac14$ ✓.
  - $\beta=$ pure P ($p=0$): $U(\beta,\beta)=1$; $U(\alpha^*,P)=\tfrac12(2)+\tfrac12(1)=1.5$; difference $0.5$ ✓.
  - $p=\tfrac34$: $U(\beta,\beta)=\tfrac9{16}(-1)+\tfrac3{16}(2)+\tfrac1{16}(1)=-\tfrac18$. $U(\alpha^*,\beta)=\tfrac12(-\tfrac34+\tfrac24)+\tfrac12(0+\tfrac14)=-\tfrac18+\tfrac18=0$. Difference $\tfrac18=2\cdot\tfrac1{16}$ ✓.

In each case $\alpha^*$ strictly beats the mutant $\beta$ when it meets $\beta$, so $\alpha^*$ is an ESS.

## Concepts
- [[evolutionarily stable strategy]] — a Nash-equilibrium strategy that also does strictly better against any other best response than that response does against itself (Defs. 284.1, 286.3) (pp. 284, 286)
- [[Nash equilibrium]] — used as a necessary condition: $(a^*,a^*)$ must be an equilibrium for $a^*$ to be stable (p. 283)
- [[mixed strategy]] — can be inherited or mutated. Read as one randomizing organism or a polymorphic population (pp. 286, 288–289)
- [[best response]] — a mutant that is a best response to $a^*$ is the case where the second ESS condition matters (p. 283)
- [[strategic (normal-form) game]] — here a symmetric two-player game between randomly matched organisms with fitness payoffs (p. 280)
- strict-nash-equilibrium (new) — each player's equilibrium action is the unique best response; sufficient for ESS (p. 283)
- monomorphic-vs-polymorphic-steady-state (new) — one form in the population versus several pure strategies coexisting in fixed fractions (pp. 280, 288–289)
- neutral-stability (new) — mutants neither die out nor take over; the second ESS condition holds weakly (p. 292)
- biological-fitness-payoff (new) — payoff as expected offspring, not subjective utility (p. 279)
- bourgeois-strategy (new) — owner takes A, intruder takes P; an ESS of owner/intruder Hawk–Dove (p. 295)

## Canonical instances
- [[hawk-dove]] — aggression versus passivity over a resource with value $v$ and loser's cost $c$; pure ESS if $v\ge c$, mixed ESS $(v/c,1-v/c)$ if $v\le c$ (pp. 284–285, 290–291)
- [[prisoners-dilemma]] — D is the only stable action between unrelated organisms. Between siblings, C (asexual) or C/D depending on payoffs (sexual) (pp. 284, 297, 300–301)
- [[bach-or-stravinsky]] — no pure ESS; the mixed equilibrium $(\tfrac23,\tfrac13)$ is an ESS (p. 289)
- [[war-of-attrition]] — symmetric mixed equilibrium $F(t)=1-e^{-t/v}$ resists pure mutants (p. 292)
- [[rock-paper-scissors-variant]] — Fig. 293.1: no ESS and not even a neutrally stable strategy (p. 293)
- [[digger-wasp-nesting]] — dig versus invade; coexistence equilibrium not evolutionarily stable (pp. 301–303)
- [[sex-ratio]] — Darwin's argument for an equal sex ratio, posed as Exercise 303.1 (pp. 285, 303)

## Bridges (candidates)
- [structural-analogy] ESS second condition ($u(b,b)<u(a^*,b)$ for alternative best responses) ↔ refinements of Nash equilibrium: stability against small perturbations selects among equilibria.
- [same-math] Mixed ESS as a polymorphic population (fractions = probabilities) ↔ mixed-strategy equilibrium interpreted as population proportions (the author cites Section 4.1) (p. 289).
- [structural-analogy] Sibling payoff functions $v$ and $w$ (weighted averages of own payoff and mimicked payoff) ↔ social preferences: a player's effective payoff includes a term from others' outcomes. The mechanism here is genetic relatedness, not altruism.
- [metaphor] Bourgeois/paradoxical strategies as conventions ↔ convention: a self-sustaining regularity (the chapter itself uses the word "convention" for peaceful settlement) (p. 295).

## Questions this raises
- The chapter says stable states are restored after mutations in the polymorphic case. How does the population move between fractions over time (an explicit dynamic)? The chapter here only discusses steady states.
- If an equilibrium in the sibling model must satisfy conditions for both a dominant and a recessive gene, what changes when mating is not monogamous or siblings share fewer genes? The text assumes monogamy.
- How does evolutionary stability change when several mutant types arrive at once, which the chapter explicitly ignores (p. 280)?
- In games with no ESS (Fig. 293.1), what does evolution predict instead?

## Exercises worth doing
- Ex. 286.1 (p. 286) — does an evolutionarily stable action weakly dominate every other action? Can another action weakly dominate it? Tests the definition's logic — difficulty: medium
- Ex. 291.1 (p. 291) — find the ESSs of Hawk–Dove–Retaliator ($\delta<\tfrac12v$); applies Def. 286.3 to a 3-action game — difficulty: hard
- Ex. 295.2 (p. 295) — generalizes the "no ESS puts weight on AP or PA" argument to any mixed equilibrium — difficulty: medium
- Ex. 301.1 (p. 301) — for which $x>1$ is X uniquely stable between siblings; uses the $v$ and $w$ games — difficulty: medium
- Ex. 303.1 (p. 303) — Darwin's sex-ratio argument via grandchildren; another application of the main ideas of evolutionary game theory — difficulty: medium
- Ex. 291.3 (p. 291) — bargaining with ESSs on demands {2,8} and {4,6}; practice in checking ESS conditions with mixed strategies — difficulty: hard

## Reading notes
- Source is an author's draft, not the published book. Title page reads "Draft chapter … Version: 99/11/19. Copyright © 1995–1999 Martin J. Osborne." Page numbering in this unit is printed 279–304 and pdf 342–367, so printed = pdf − 63.
- Draft markers visible: the box on p. 295 begins "[Note: this box is rough.]" and the Notes section on p. 303 begins "[Incomplete.]". Cross-references to other chapters (e.g. "Figure 13.1", "Figure 16.1", Chapter 4 propositions) point to draft numbering that is not in this unit.
- The text layer dropped the symbol $\epsilon$ in places and some Greek letters. I checked equations against the page images where provided (pdf 344, 346–367). For pdf 342, 343 and 345 no image was provided, and the text layer was used.
- The author spells Brockmann et al. as "Brockman" on p. 287, both ways on p. 303, and "Brockmann" in the Notes (p. 304).
- p. 295 says the paradoxical convention is described "in the box on p. 295". The box discusses the bourgeois-type outcome (spiders) and says nothing about the paradoxical strategy, so the reference is unclear.
- The printed summary sentence on p. 300, "If $(a^*,a^*)$ is not a Nash equilibrium of both these games then $a^*$ is not evolutionarily stable", is ambiguous. The preceding necessary conditions apply to each game separately, so I read it as: failing either one rules out stability.
- On p. 290 the text says "If $v\le c$" for the mixed equilibrium. At $v=c$ the mixed strategy $(v/c,1-v/c)$ equals pure A, which agrees with the earlier result for $v=c$.
- The author omits the details of the recessive-gene calculation (p. 299). I copy only the stated result.
