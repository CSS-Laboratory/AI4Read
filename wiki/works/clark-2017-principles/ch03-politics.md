---
id: clark-2017-principles/ch03-politics
work: clark-2017-principles
unit: 3 What Is Politics?
pages: 49–86
fields: [political-science]
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
# What Is Politics? (the Exit, Voice, and Loyalty Game)

## L0 — One line
Politics is behavior involving power or influence, and a simple sequential game of exit, voice and loyalty shows that a citizen can influence a state only if she has a credible exit threat and the state depends on her.

## L1 — The gist (≤ 120 words)
The chapter defines politics as the part of human behavior that involves power or influence. It then builds the Exit, Voice, and Loyalty (EVL) Game between a citizen and a state that has just taken a benefit from her. Solving the game by backward induction (working from the last move back to the first) gives four scenarios. The state responds to the citizen's voice only if she has a credible exit option and the state depends on her loyalty. Several lessons follow: power may be invisible because it works through anticipation, and silence or loyalty is not proof of satisfaction. The chapter ends with a method for writing and solving sequential games, the Senate Race Game, and practice problems.

**Prerequisites:** comparing numbers and inequalities; reading a decision tree; the idea of "best response" (choosing what is best given what others will do). No calculus.

## L2 — Key ideas (5–10 bullets)
- Politics is the subset of human behavior that involves power or influence. Power is involved when people cannot reach their goals without influencing others or resisting their influence (p. 50).
- When something bad happens, a person can exit (adapt), use voice (complain, protest, lobby) or stay loyal (do nothing). The best choice depends on what the other actor will do, so political situations are strategic and can be analysed as games (pp. 51–53).
- A sequential game (players move in turn) is solved by backward induction (reasoning from the last move back to the first), which gives a subgame perfect equilibrium (SPE: the list of best choices at every decision point). The SPE lists choices at every node (decision point), including nodes never reached, because anticipated moves drive behavior (pp. 58–62).
- Main result: the state responds to voice only if the citizen has a credible exit threat (her exit payoff is higher than her loyalty payoff, $E>0$) and the state is dependent (it values her loyalty more than the benefit it took, $L>1$). Exit threat alone is not enough (pp. 66–67).
- Without a credible exit option, the citizen is a "sitting duck". Credible exit is necessary, though not sufficient, for avoiding exploitation (p. 68).
- Observed quiet or loyalty is a poor guide to preferences or dependence. A dependent state may ignore citizens who cannot exit. In the East German example, the authors argue that apparent stability may have hidden a regime that did depend on its citizens (pp. 68–69).
- If the game includes the state's choice to take the benefit, a dependent state facing a citizen with credible exit never exploits her, so she never needs voice. Power can be most effective when least observable (pp. 62, 69–70).
- The model leaves things unexplained: unresponsive states despite voice, voice with negative cost, and incomplete information (pp. 70, 74).
- The chapter gives a three-step recipe for writing and solving extensive form games (sequential games drawn as trees), with the Senate Race Game as worked example (pp. 75–79).

## L3 — Walkthrough

### Introduction (pp. 49–50)
- Political science is the study of politics in a scientific manner. This chapter defines politics, after Chapter 2 defined science (p. 50).
- **Definition:** politics is the subset of human behavior that involves the use of power or influence. Power is involved whenever individuals cannot accomplish their goals without trying to influence the behavior of others, or trying to get free from others' influence (p. 50).
- Home, work and play typically involve such attempts, so politics is part of much of everyday life (p. 50).
- The model is a reformulation and extension of Hirschman's (1970) *Exit, Voice, and Loyalty*. Hirschman mainly addresses consumers and firms; this chapter addresses citizens and states (p. 50).
- The model is meant to explain when citizens take direct action, when states respond positively, and when states ignore citizens. More generally it asks who has power, why, and how it is used (p. 50).

### The Exit, Voice, and Loyalty Game (pp. 50–56)
**Negative changes and winners/losers (pp. 50–51).**
- Examples of changes someone may dislike: tax increases, a handgun ban, a court ruling on school prayer, a falling currency, imports of fuel-efficient cars, worse peaches at a fruit stand (p. 50).
- Others may see the same change as an improvement. Political situations nearly always involve some people benefiting at others' expense, so politics is frequently about winners and losers (p. 51).

**Three responses (p. 51, Table 3.1 on p. 52).**
- **Exit:** accept the negative change and alter your behavior to get the best outcome in the new environment (e.g., move to another state, buy mangoes).
- **Voice:** complain, protest, lobby or take direct action to try to restore the original environment.
- **Loyalty:** accept the change and make no change to your behavior.
- Table 3.1 gives the author's parallel examples. For a tax increase: reallocate your portfolio (exit), organize a tax revolt (voice), pay and keep quiet (loyalty).

**Strategic situations and game theory (pp. 52–53).**
- The citizen's best choice depends on what she expects the state to do after voice, and the state's choice depends on what it expects of her. The authors call this strategic aspect "the essence of politics" (p. 52).
- A **strategic situation** is one where one actor's choices depend on others' choices. **Game theory** is the tool for analysing such situations (p. 52).
- A **game** is a situation where an individual's ability to reach her goals depends on the choices of other identifiable actors. Games have players with sets of choices and rules for how decisions are made. The basic rule is that players choose what they believe is in their best interest (p. 53).
- **Payoffs** show how players value outcomes. Higher is preferred (p. 53).
- In an **extensive form game** players choose sequentially, and the game is drawn as a game tree. In a **normal (strategic) form game** players choose simultaneously, and the game is drawn as a payoff matrix (p. 53).
- Parts of a tree: **choice nodes** (where a player chooses), **branches** (actions), the **initial node** (the start), **terminal nodes** (the end, labeled with payoffs). The whole structure is the **game tree** (pp. 53–54).

**The EVL game tree (Figure 3.1, pp. 54–55).**
- *Prehistory:* the state has already caused a negative change that transferred a benefit from the citizen to the state (e.g., a tax hike) (p. 54).
- Move 1, citizen: Exit gives O1 (state keeps benefit, citizen takes a substitute). Loyalty gives O2 (state keeps benefit, citizen suffers loss silently). Voice passes the move to the state (p. 54).
- Move 2, state, after voice: Respond gives O3 (benefit returned). Ignore passes to the citizen (pp. 54–55).
- Move 3, citizen, after being ignored: Loyalty gives O4 (state keeps benefit, citizen suffers loss). Exit gives O5 (state keeps benefit, citizen takes a substitute) (p. 55).
- Footnote 4: the citizen could use voice again, but if nothing has changed the state would ignore her again, so the model allows only exit or loyalty at this point (p. 55).

**Payoffs (Table 3.2, pp. 55–56).** Citizen's payoff first, state's second:

| Outcome | Citizen | State |
|---|---|---|
| O1 | $E$ | $1$ |
| O2 | $0$ | $1+L$ |
| O3 | $1-c$ | $L$ |
| O4 | $0-c$ | $1+L$ |
| O5 | $E-c$ | $1$ |

- $E$ is the citizen's exit payoff (attractiveness of her exit option). Some citizens have high $E$, others low (p. 55).
- Loyalty gives the citizen 0 (she accepts the loss).
- $c>0$ is the cost of voice. It covers effort, and in repressive states possibly imprisonment, job loss or death (pp. 55–56).
- The state's baseline payoff for keeping the benefit is 1. The value 1 is chosen for presentational ease (p. 56).
- $L>0$ is the extra payoff the state gets from a loyal citizen who does not exit. It can reflect support or "legitimacy", or continued investment in the economy. Its size varies across states and citizens (p. 56).
- **Assumption** $E<1-c$: exit is worth less than successfully using voice. This restricts attention to situations where voice is at least possible. If the assumption did not hold, the citizen would always exit whatever the state does (p. 56).
- Assumptions in total: $c>0$, $L>0$, $E<1-c$ (Figure 3.2, p. 57).

> **Intuition note.** The game turns a political complaint into two decisions. The citizen picks exit, voice or silence, and the state picks respond or ignore. The numbers $E$, $L$ and $c$ summarise how good her alternatives are, how much the state needs her, and how costly protest is.

### Solving the Exit, Voice, and Loyalty Game (pp. 57–66)
- **Rational** here means only that a player does what she believes is in her best interest given what she knows when choosing (p. 57).
- Extensive form games are typically solved for the **subgame perfect equilibrium (SPE)** using **backward induction**: reason from the end of the game back to the start (p. 58).
- Players think ahead and anticipate others' responses, as chess players do. At the final nodes players pick the highest payoff. Then, at each earlier node, they pick the action with the highest payoff given what will happen later (p. 58).

**Scenario 1: credible exit ($E>0$), dependent state ($L>1$) (Figures 3.3–3.5, pp. 58–61).**
1. *Last node (citizen, after being ignored):* exit gives $E-c$, loyalty gives $0-c$. Since $E>0$, $E-c>0-c$, so she exits (p. 59). $E>0$ is read as a *credible exit threat*: exit is better than loyalty (p. 58).
2. *State's node:* respond gives $L$. Ignore leads to the citizen's exit, so the state gets 1. Since $L>1$, the state responds (p. 59). $L>1$ means the state is *dependent*: it values loyalty more than the benefit it took (p. 59).
3. *First node (citizen):* exit gives $E$, loyalty gives 0, voice leads to "respond" and gives $1-c$. Because $E<1-c$ (the assumption) and $0<1-c$ *(added step: $0<E<1-c$)*, she uses voice (p. 60).

- **Outcome:** (Voice, Respond), with payoffs $(1-c,\,L)$ (p. 61).
- **SPE notation:** list all the first player's choices at all her nodes, then a semicolon, then the second player's choices. Here: **(Voice, Exit; Respond)** (pp. 61–62).
- **Why list unreached choices:** the citizen never reaches her second node. But the state responds because it anticipates that she would exit there. So the SPE must list choices at every node (p. 62).
- Choices not taken are often as important as observed ones. The authors write that power is often most effective when least observable (p. 62).
- Footnote 6 offers an analogy. An SPE is two complete sets of instructions given to agents. An agent might make a mistake, so the other must know what to do at every node (p. 62).

> **Intuition note.** The state gives in because it can see that ignoring the citizen would make her leave. The threat of exit never has to be carried out. It shapes the state's behavior anyway.

**Scenario 2: no credible exit ($E<0$), dependent state ($L>1$) (Figure 3.6, pp. 62–64).**
- Last node: loyalty ($0-c$) beats exit ($E-c$) because $E<0$ (p. 63).
- State: respond gives $L$, ignore gives $1+L$. Since $1+L>L$, the state ignores whatever the value of $L$ (p. 63).
- First node: voice would give $0-c$, exit gives $E$, loyalty gives 0. She is loyal (p. 63).
- **SPE (Loyalty, Loyalty; Ignore); outcome O2; payoffs $(0,\,1+L)$** (pp. 63–64).

**Scenario 3: credible exit ($E>0$), autonomous state ($L<1$) (Figure 3.7, pp. 64–65).**
- Last node: exit (as in scenario 1) (p. 64).
- State: respond gives $L$, ignore gives 1. Since $L<1$, it ignores (p. 65). $L<1$ means the state is *autonomous* (p. 64).
- First node: voice gives $E-c$, exit gives $E$, loyalty gives 0. She exits (p. 65).
- **SPE (Exit, Exit; Ignore); outcome O1; payoffs $(E,\,1)$** (p. 65).

**Scenario 4: no credible exit ($E<0$), autonomous state ($L<1$) (Figure 3.8, pp. 65–66).**
- The same reasoning as scenario 2 applies: the citizen is loyal at the last node, the state ignores since $1+L>L$ whatever $L$, and she is loyal at the start (p. 66).
- **SPE (Loyalty, Loyalty; Ignore); outcome O2; payoffs $(0,\,1+L)$** (p. 66).
- (The text of p. 66 says "autonomous ($L>1$)". This is a misprint; Figure 3.8 states $L<1$. See Reading notes.)

> **Skip path.** Carry forward Table 3.3: only (credible exit, dependent state) gives voice and a positive response.

### Evaluating the Exit, Voice, and Loyalty Game (pp. 66–70)
**Table 3.3 (p. 67):**

| Citizen \ State | Autonomous ($L<1$) | Dependent ($L>1$) |
|---|---|---|
| Credible exit ($E>0$) | (Exit, Exit; Ignore) — O1 | (Voice, Exit; Respond) — O3 |
| No credible exit ($E<0$) | (Loyalty, Loyalty; Ignore) — O2 | (Loyalty, Loyalty; Ignore) — O2 |

**Point 1 (pp. 66–67).** The state responds positively only when both conditions hold: $E>0$ and $L>1$. A credible exit threat alone is not enough. An autonomous state never responds positively, even when the citizen can credibly exit (p. 66). Footnote 7: a citizen with credible exit has an advantage over one without. The point is that exit alone is not sufficient for influence (p. 66).
- *Everyday application:* to get a raise, have other employers willing to hire you (credible exit) and be someone your employer depends on. If either is missing, the employer feels free to ignore you (p. 67).
- The text invites the reader to apply this to parents, professors and friends (p. 67).

> **Intuition note.** Influence needs two things at once: you can realistically walk away (exit beats staying loyal), and the other side would be hurt if you did. Remove either and the threat is empty.

**Point 2: the "sitting duck" (pp. 67–68).**
- With no credible exit ($E<0$), the state can take benefits and the citizen can only accept (p. 67).
- *Example (hedged by the authors):* "some have argued" that the US Democratic Party has not done enough for African American voters. If so, the game suggests a reason. Democrats depend on those votes (little chance of national office without them), but African Americans rarely vote Republican. This may signal that they lack a credible exit option, so the Democrats can partly ignore and exploit them. The authors say they do not wish to enter that debate (p. 67).
- Credible exit options are a necessary, though not sufficient, condition for not being exploited. The authors suggest, "perhaps somewhat counterintuitively", that such voters might signal credible exit by voting Republican, and only then would the Democratic Party take them seriously (p. 68).
- The "benefit" taken in the prehistory can be civil rights, property, or even an unfair advantage such as a market licence. So a responsive state is not inherently good, nor is an unresponsive one inherently bad. Demands are often called "special interests" and officials can be applauded for ignoring them (p. 68).

**Point 3: observation is misleading (pp. 68–69).**
- From her action we can always infer whether the citizen has credible exit. Exit or voice requires it, and loyalty implies its absence (p. 68).
- It is not easy to tell whether the state is dependent or autonomous when she has no credible exit, because both types ignore her in the same way. She expects this, so she stays loyal (p. 68).
- So we should not infer that regimes with little voice or opposition (the text lists Burma, China, Iran and North Korea) are autonomous. They may be dependent yet free to ignore citizens who cannot exit (p. 68).
- *East Germany:* one can argue that, apart from the 1953 Berlin Uprising, East Germans were loyal before 1989 because they lacked credible exit. To many observers the regime looked stable and relatively autonomous (p. 69). The Hungarian border opening to Austria in May 1989 gave a credible exit option for the first time since the Berlin Wall (1961). Mass voice followed in Leipzig and East Berlin. One can argue that the regime eventually opened the Wall because it did depend on its citizens (p. 69). Footnote 8: by building the Wall the regime removed their one credible exit option (p. 69).
- Likewise, political mobilization (voting, lobbying, contributions) or its absence is not a straightforward revelation of preferences. Silence can mean satisfaction or expected ineffectiveness (p. 69).

**Point 4: why would the state take the benefit at all? (pp. 69–70).**
- The game as written cannot answer this. If we add an initial state move (exploit or not), the state does not exploit whenever it depends on a citizen with credible exit. It knows it would have to respond to her voice anyway, so she never needs voice (pp. 69–70).
- Such citizens wield considerable influence without opening their mouths. The authors link this to Thatcher's epigraph: "Being powerful is like being a lady. If you have to tell people you are, you aren't." (p. 70).
- *Structural Marxist analogy:* on this view, capitalists have credible exit and the state depends on them for investment, jobs, growth and tax revenue. Capital is generally more mobile than labor, so capitalists typically have significantly more influence than workers. This holds even if the state depends on both (p. 70). Chapter 9 treats this view (p. 70).
- *Measurement problem:* in many cases the most powerful actors are the least likely to act, so a researcher may never see their power used. It may be wrong to infer that non-protesting citizens have no influence. Likewise, presidents who rarely veto may still be powerful: the veto threat leads legislatures to send only bills the president wants (Cameron 2000) (p. 70).
- This is one reason game theory, which can analyse strategic dynamics that produce non-action, has become central to political science (p. 70).

> **Intuition note.** Anticipation can replace action. If actors expect a protest or veto to work, it may rarely need to happen, so counting visible protests or vetoes may under-measure power.

**Point 5: what the game does not explain (pp. 70, 74).**
- In the game as it stands, citizens use voice only when they expect it to be effective, so the model cannot explain states being unresponsive to voice (p. 70).
- *Voice may not be costly.* Some citizens may enjoy self-expression, networking at rallies or civic pride. This can be modelled as $c<0$. Then voice always gives a higher payoff than exit or loyalty, whatever the state does. Footnote 9: this leaves the puzzle of why citizens sometimes do not use voice (p. 74).
- *Information.* The EVL Game has complete information (each player knows everything about the game and others' preferences). Models with incomplete information, shown later (Chapter 8), let a state misjudge a citizen's exit threat, or a citizen misjudge the state's dependence. A state may think a citizen is bluffing (p. 74).

### Box 3.1: U.S. bailouts of financial and auto sectors (pp. 71–73)
- The authors say a full assessment of the policy is beyond their scope. The EVL model "can help to explain" why governments respond differently to different sectors (p. 71).
- *Finance, Sept. 2008:* Lehman Brothers went bankrupt on 15 Sept. and Merrill Lynch was bought by Bank of America. The next day the Fed planned an $85 billion loan to AIG. TARP, authorizing up to $700 billion, was signed on 3 Oct. (p. 71).
- *Autos:* Big Three executives met Speaker Pelosi on 17 Sept. and left with few concrete commitments. They asked for $25 billion of TARP money on 18 Nov. and received a chilly reception. They returned on 4 Dec. asking for $34 billion. The House approved a $14 billion plan, which did not reach a Senate vote. The Bush administration announced $13.4 billion of the remaining TARP money, which many observers thought enough only to delay bankruptcy until January 2009 (pp. 71–72).
- Other differences noted: auto executives were chastised for corporate jets, while Treasury went to the banks and told bank chiefs they would not leave until they agreed to take the money (p. 72). The auto industry was concentrated in battleground states just before an election (p. 72).
- It is "difficult to establish" whether the government was equally dependent on both sectors, but a collapse of either would have been costly for the incumbent government (p. 72).
- *EVL reading:* the authors say the model suggests the difference can be attributed to the credibility of exit threats. Liquid asset holders can respond to bad news with great speed and magnitude (the sell-off after Lehman). The automakers' fixed assets make offshoring too slow for politicians focused on short-term interests such as reelection. So governments anticipate the needs of actors with credible exit on whom they depend, and are less responsive to similarly imperiled actors with less credible exit (p. 73). Chapter 6 returns to this (p. 73).

### Conclusion (pp. 74–75)
- Interactions are political when actors cannot reach goals without considering others' behavior, so attempts to influence or escape influence matter, and power is exercised (p. 74).
- Three basic strategies: change the environment (voice), change location (exit), or neither (loyalty). They are metaphors. Exit need not mean emigrating; it can be changing industries, production processes or parties. Voice ranges "from a ballot to a bullet" (pp. 74–75).
- Loyalty is also used metaphorically, "indeed, euphemistically", since for most of history many people may have had neither feasible voice nor exit (p. 75).
- The next chapter asks where the state and citizen come from (p. 75).

### Preparation for the problems (pp. 75–76)
1. **Writing the game:** identify players. Draw the tree with choices and order, and label each node with the mover. Determine payoffs for each outcome. Write payoffs at terminal nodes, first mover's first, separated by commas (pp. 75–76).
2. **Solving by backward induction:** at each final node, make bold the branch with the highest payoff for the mover. Then go to the previous node, and continue back to the start (p. 76).
3. **Identifying outcome, payoffs, equilibrium:** follow the bold lines from the start to a terminal node. This path is the **equilibrium path**, and its end node is the expected outcome. The payoffs there are what players receive. The SPE lists every player's choices at all of their nodes, players separated by semicolons (p. 76).

### Example: Potential Entry in a Senate Race (pp. 76–79)
- *Setup:* incumbent Staton chooses whether to run a preemptive advertising campaign. Challenger Reenock then chooses to enter or stay out (p. 76). Four outcomes (p. 77).
- *Staton's ranking* (reasoning: reelection is likely, over 90% for incumbents per Jacobson 2001, and ads cost money): (don't advertise; stay out) > (advertise; stay out) > (don't advertise; enter) > (advertise; enter) (p. 77).
- *Reenock's ranking* (he will probably lose if he enters, but wants name recognition; reasoning given for stay-out outcomes): (don't advertise; enter) > (advertise; stay out) > (don't advertise; stay out) > (advertise; enter) (p. 77).
- *Ordinal payoffs* are 4 (best) to 1 (worst) and show only the ordering. In Figure 3.9 (Staton, Reenock): advertise–enter $(1,1)$; advertise–stay out $(3,3)$; don't–enter $(2,4)$; don't–stay out $(4,2)$ (p. 78).
- *Solve:* after "advertise", Reenock compares 1 (enter) with 3 (stay out) and stays out. After "don't advertise", he compares 4 with 2 and enters. Staton then compares 3 (advertise, since Reenock stays out) with 2 (don't, since Reenock enters) and advertises (pp. 78–79).
- **Outcome (advertise, stay out); payoffs $(3,3)$**, both players' second-best. **SPE (advertise; stay out, enter)** (p. 79).
- *Interpretation:* an incumbent may advertise preemptively to deter a challenger. This is a generic Entry Deterrence Game. In Epstein and Zemsky (1995) a challenger enters only if the incumbent is weak, so incumbents may signal strength with a campaign "war chest". Their game is basically similar (p. 79).

### Problems (pp. 79–86; set-ups only)
- **Problem 1** asks for the outcome, payoffs and SPE of Generic Games I, II and III (Figures 3.10–3.12, pp. 80–81). Games I and II have two players; Game III has three players (pp. 79–81).
- **Problem 2:** reverse the Senate Race move order (Reenock first, Figure 3.13). Keep the same preference orderings, fill in payoffs, solve, and ask whether the order of moves matters (pp. 80–82).
- **Problem 3, Terrorism Game** (after Bueno de Mesquita 2006): a social group chooses violence (terrorist act) or negotiate. If it negotiates, the government chooses to repress or negotiate (Figure 3.14). Two group types (True Believers, Reluctant Terrorists) and two government types (Repressive, Responsive) have given preference orderings. Parts a–h ask for the games to be solved for each pairing, whether government type matters, whether terrorists must be fanatics, and what public "we never negotiate" declarations do (pp. 82–84).
- **Problem 4, Legislative Pay Raise Game:** three legislators vote sequentially. A raise passes if at least two vote yes. Each legislator's ordering is: raise and I voted no > raise and I voted yes > no raise and I voted no > no raise and I voted yes (p. 85). Parts ask which position is best to vote from, to complete the payoffs in Figure 3.15, solve it, and consider agenda-setting (pp. 85–86).
- **Problem 5:** write and solve your own two-player and three-player sequential games (p. 86).

## Toy example (ours, not from the text)
Citizen's voice costs $c=0.2$. We vary $E$ and $L$. Each case assumes $E<1-c=0.8$.

**Case A: $E=0.5$, $L=2$ (credible exit, dependent state).**
1. Last citizen node: exit $E-c=0.5-0.2=0.3$; loyalty $0-c=-0.2$. She exits.
2. State: respond gives $L=2$. Ignore leads to exit, so it gets 1. Since $2>1$, it responds.
3. First node: voice $1-c=0.8$; exit $0.5$; loyalty $0$. She uses voice.
- SPE (Voice, Exit; Respond); payoffs $(0.8,\,2)$.

**Case B: $E=0.5$, $L=0.5$ (credible exit, autonomous state).**
1. Last node: exit gives 0.3 versus $-0.2$, so she exits.
2. State: respond gives 0.5. Ignore gives 1. It ignores.
3. First node: voice gives $E-c=0.3$; exit gives $0.5$; loyalty $0$. She exits.
- SPE (Exit, Exit; Ignore); payoffs $(0.5,\,1)$.

**Case C: $E=-0.3$, $L=2$ (no credible exit, dependent state).**
1. Last node: exit $-0.3-0.2=-0.5$; loyalty $-0.2$. She is loyal.
2. State: respond gives 2. Ignore gives $1+L=3$. It ignores.
3. First node: voice gives $-0.2$; exit $-0.3$; loyalty $0$. She is loyal.
- SPE (Loyalty, Loyalty; Ignore); payoffs $(0,\,3)$.

Only Case A produces a state response. Case C shows a dependent state exploiting a citizen who cannot exit.

## Concepts
- [[politics]] — the subset of human behavior involving power or influence (p. 50) (new)
- [[power]] — present when people cannot reach goals without influencing others or resisting their influence (p. 50) (new)
- [[exit-voice-loyalty]] — here the citizen's three responses to a harmful state action: adapt (exit), try to reverse it (voice), or accept it (loyalty). Applied to citizens and states, extending Hirschman's firm–consumer setting (pp. 50–51)
- [[game-theory]] — tool for analysing strategic situations where one actor's choices depend on others' (p. 52) (new)
- [[strategic-situation]] — a situation where one actor's choices depend on the choices of other actors (p. 52) (new)
- [[extensive-form-game]] — a sequential-move game drawn as a tree of choice nodes, branches and terminal nodes (p. 53) (new)
- [[payoff]] — number showing how a player values an outcome (p. 53) (new)
- [[backward-induction]] — reasoning from the last choice node back to the first, choosing the best action at each node given later play (p. 58) (new)
- [[subgame-perfect-equilibrium]] — the profile of choices at all nodes found by backward induction, including nodes not reached (pp. 58, 62) (new)
- [[credible-exit-threat]] — the citizen's exit payoff exceeds her loyalty payoff, $E>0$ (p. 58) (new)
- [[state-dependence]] — the state values the loyalty of the citizen more than the benefit it took, $L>1$. Autonomous means $L<1$ (pp. 59, 64) (new)
- [[complete-information]] — each player knows everything about the game and others' preferences (p. 74) (new)
- [[ordinal-payoffs]] — payoffs that show only the order of preferences (p. 78) (new)
- [[entry-deterrence]] — an incumbent acts (e.g., advertises) to discourage a potential challenger from entering (p. 79) (new)

## Canonical instances
- [[evl-game]] — citizen–state sequential game; the four scenarios and Table 3.3 (pp. 54–67) (new)
- [[east-german-collapse-1989]] — the authors argue that loyalty before 1989 may have hidden state dependence. A credible exit appeared when the Hungarian border opened (p. 69) (new)
- [[us-bailouts-2008]] — differing government responses to finance and autos, read through exit credibility (pp. 71–73) (new)
- [[senate-race-game]] — preemptive advertising to deter a challenger, solved by backward induction (pp. 76–79) (new)
- [[presidential-veto-threat]] — the threat of a veto shapes bills sent to the president, so power is used without being observed (p. 70) (new)
- [[democrats-and-african-american-voters]] — an illustration, hedged as "some have argued", of a dependent party facing voters without credible exit (pp. 67–68) (new)

## Bridges (candidates)
- [structural-analogy] Presidential veto threat (p. 70) ↔ veto player: an actor whose agreement is needed shapes outcomes through anticipation, even if it rarely acts.
- [structural-analogy] Loyal-looking East Germans before 1989 (p. 69) ↔ preference falsification: observed quiet does not reveal private preferences or fragility.
- [structural-analogy] Sudden mass voice after the Hungarian border opened (p. 69) ↔ revolutionary threshold/cascade: a change in the cost of protest or the availability of exit can trigger mass action.
- [structural-analogy] EVL game with $E$, $L$, $c$ and the voice option ↔ exit/voice/loyalty (Hirschman): the chapter's own reformulation of Hirschman's framework for citizens and states.
- [structural-analogy] Problem 4e on agenda or rule-setting (p. 86) ↔ agenda control: who moves when, or sets the order of votes, can steer outcomes.
- [structural-analogy] Capitalists' credible exit and state dependence (p. 70) ↔ principal–agent / delegation: an actor with an outside option can influence one who depends on it.

## Questions this raises
- If exit is only metaphorical (change party, industry), how can a researcher measure $E$ and $L$ in a real case?
- If power is exercised through anticipation, what evidence could distinguish a powerful quiet actor from a powerless quiet actor?
- What would the extended game (state first chooses whether to take the benefit) look like in full, and what happens with incomplete information about $E$ or $L$?
- Why do citizens sometimes not use voice even when voice has negative cost (footnote 9)?

## Exercises worth doing
- Ex. 1 (p. 79) — practice backward induction on three generic trees, including a three-player game — difficulty: easy
- Ex. 2 (p. 80) — reverse the move order in the Senate Race Game and see whether order changes the outcome — difficulty: medium
- Ex. 3 (p. 81) — Terrorism Game with different group and government types; tests the inference that terrorists must be fanatics and the effect of "never negotiate" declarations — difficulty: hard
- Ex. 4 (p. 84) — Legislative Pay Raise Game; the value of voting position and of agenda control — difficulty: medium
- Ex. 5 (p. 86) — write and solve your own two- and three-player games — difficulty: medium

## Reading notes
- Printed page = pdf page − 37 (pdf 86 = p. 49). All page references are printed numbers.
- The pages shown carry no edition line. The task metadata says this PDF is the 2nd edition (2013), not the 3rd (2017) named in the work id.
- **Misprint, p. 66:** the text says "the state is autonomous ($L>1$)" for Scenario 4. Figure 3.8 and the table logic use $L<1$.
- **Figure 3.6 (p. 63):** the image shows the Exit branch bold at the final citizen node. The text says loyalty is chosen there because $E<0$ (and Figure 3.8 correctly shows loyalty bold). I followed the text.
- **Running heads:** pages 80–86 carry template remnants ("Chapter 4: The Origins of the Modern State"; "Recto Running Head Is The First A-Head"). Ignore them.
- The text does not treat the knife-edge cases $E=0$ and $L=1$.
- Problem figures (3.13, 3.15)
