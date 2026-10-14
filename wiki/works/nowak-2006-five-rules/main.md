---
id: nowak-2006-five-rules/main
work: nowak-2006-five-rules
unit: paper
pages: (pdf-only HTML source; Science 314(5805):1560–1563)
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
# Five Rules for the Evolution of Cooperation

## L0 — One line
Natural selection alone favours defectors, but five mechanisms (kin selection, direct, indirect and network reciprocity, group selection) can each let cooperation evolve, and each yields a simple rule: the benefit-to-cost ratio $b/c$ must exceed a critical value.

## L1 — The gist (≤ 120 words)
In a well-mixed population, selection reduces cooperation, even though all-cooperator populations have the highest average fitness. Nowak asks which mechanisms can reverse this. He presents five and gives a short rule for each: $r>c/b$, $w>c/b$, $q>c/b$, $b/c>k$, $b/c>1+n/m$. He then shows that each mechanism can be written as a 2×2 payoff matrix. From the matrix one can test whether cooperation is evolutionarily stable (ESS), risk-dominant (RD) or advantageous (AD). The framework unifies very different models and links them to standard evolutionary game dynamics. Nowak also notes mechanisms he leaves out, including punishment; he says it is unclear whether punishment alone is a mechanism.

**Prerequisites:** 2×2 payoff matrices; Prisoner's Dilemma; probability and expected value; the geometric series (expected number of rounds $1/(1-w)$); the idea of fitness as reproductive success.

## L2 — Key ideas (5–10 bullets)
- A cooperator pays cost $c$ so another gets benefit $b$. In any mixed population defectors have higher fitness, so cooperators decline (§ intro, Fig. 1).
- All-cooperator populations have the highest average fitness. Selection still lowers average fitness here because it is frequency-dependent, so Fisher's theorem does not apply (§ intro).
- Kin selection: Hamilton's rule $r>c/b$, where $r$ is relatedness (§ "Kin selection").
- Direct reciprocity needs $w>c/b$, where $w$ is the probability of another encounter. Tit-for-tat, the winner of Axelrod's tournaments, was later replaced by generous-tit-for-tat and then win-stay, lose-shift, because errors make its performance decline (§ "Direct reciprocity").
- Indirect reciprocity (reputation) needs $q>c/b$. Network reciprocity needs $b/c>k$. Group selection allows cooperation provided $b/c>1+n/m$, in the limit of weak selection and rare group splitting (§§ on each).
- Success is measured by ESS ($\alpha>\gamma$), risk dominance ($\alpha+\beta>\gamma+\delta$) and advantage ($\alpha+2\beta>\gamma+2\delta$) (§ "Evolutionary success").
- Each mechanism is a 2×2 matrix (Table 1). Kin selection, network reciprocity and group selection give one condition for all three measures. Direct and indirect reciprocity need slightly stricter conditions for RD and AD (§ "Comparative analysis").
- Punishment, green-beard models and voluntary participation are not analysed as mechanisms here (§ "Conclusion").

## L3 — Walkthrough

### Introduction (before "Kin selection")
- Nowak says competition in evolution should reward only selfish behaviour, yet cooperation is seen at many levels: genes, chromosomes, cells, organisms, humans (§ intro).
- **Cooperator:** pays cost $c$ so another gets benefit $b$. **Defector:** pays no cost and gives no benefit. Costs and benefits are fitness; reproduction can be genetic or cultural (§ intro).
- In any mixed population defectors have higher average fitness, so cooperators vanish. Yet an all-cooperator population has the highest average fitness and an all-defector one the lowest (§ intro).
- Fisher's fundamental theorem (average fitness rises under constant selection) does not apply, because selection is *frequency-dependent*: fitness depends on the relative abundance of cooperators (§ intro).
- Fig. 1 caption: with $N$ individuals, $i$ cooperators and $N-i$ defectors:
$$f_C=\frac{b(i-1)}{N-1}-c,\qquad f_D=\frac{bi}{N-1},\qquad \bar f=\frac{(b-c)i}{N}.$$
Here $f_D>f_C$ in every mixed population ($1\le i\le N-1$) (added step: $f_D-f_C=\frac{b}{N-1}+c>0$) (§ Fig. 1 caption).

*Intuition note:* Each cooperator's gift goes to others, but cooperators never get the saved cost. So a defector in the same mixed population does better (by $\frac{b}{N-1}+c$ in the formulas above). The group as a whole does best when everyone cooperates.

### Kin selection
- **Haldane's remark:** he would jump into the river to save two brothers or eight cousins. Nowak says this anticipated Hamilton's rule (§ "Kin selection").
- Natural selection can favour cooperation if donor and recipient are genetic relatives. Relatedness $r$ must exceed the cost-to-benefit ratio:
$$r>c/b \tag{1}$$
- Relatedness is the probability of sharing a gene: $1/2$ for brothers and $1/8$ for cousins (§ "Kin selection").
- The behaviour's effect on kin who may carry the same gene must be counted. This is called kin selection or inclusive fitness (§ "Kin selection").

### Direct reciprocity
- Trivers proposed this mechanism for cooperation between non-relatives. The same two individuals meet repeatedly, which is the repeated Prisoner's Dilemma (§ "Direct reciprocity").
- **Tit-for-tat:** cooperate first, then copy the other player's previous move. It won Axelrod's two computer tournaments (§ "Direct reciprocity").
- Its weakness: with erroneous moves ("trembling hands") one accidental defection starts a long chain of retaliation, so its performance declines (§ "Direct reciprocity").
- **Generous-tit-for-tat** sometimes cooperates after the partner defected, with probability $1-c/b$. Natural selection can promote forgiveness (§ "Direct reciprocity").
- **Win-stay, lose-shift:** repeat your last move if you are doing well, otherwise change. By various measures it is more robust than tit-for-tat or generous-tit-for-tat. Tit-for-tat is an efficient catalyst when nearly everyone defects; win-stay, lose-shift better maintains cooperation once established (§ "Direct reciprocity").
- General rule: direct reciprocity can only lead to cooperation if the probability $w$ of another encounter exceeds $c/b$:
$$w>c/b \tag{2}$$

*Intuition note:* Direct reciprocity can lead to cooperation only if the chance $w$ of meeting again exceeds $c/b$. The cheaper the help relative to its benefit (small $c/b$), the lower that chance can be.

### Indirect reciprocity
- Interactions among humans are often asymmetric and fleeting, so direct return is impossible. Nowak compares direct reciprocity to barter and indirect reciprocity to money, with reputation as the money (§ "Indirect reciprocity").
- Standard framework: random pairwise encounters with donor and recipient. A subset of the population observes and may inform others. Strategies that base help on the recipient's reputation are favoured (§ "Indirect reciprocity").
- Studies show more helpful people are more likely to receive help. Only humans seem to play the full game. It makes cognitive demands and needs language. Nowak says selection for it and for language presumably shaped human intelligence (§ "Indirect reciprocity").
- Rule: indirect reciprocity can only promote cooperation if the probability $q$ of knowing someone's reputation exceeds $c/b$:
$$q>c/b \tag{3}$$

### Network reciprocity
- The case for defection (Fig. 1) assumes a well-mixed population. In real populations some individuals interact more than others (§ "Network reciprocity").
- In evolutionary graph theory individuals sit on vertices and edges say who interacts. A cooperator pays $c$ for each neighbour to get $b$. Cooperators can prevail by forming clusters that help each other (§ "Network reciprocity").
- Games on graphs are easy to simulate but hard to analyse. A simple rule still holds: $b/c$ must exceed the average number of neighbours $k$:
$$b/c>k \tag{4}$$

### Group selection
- Model (Traulsen and Nowak): the population is split into groups. Cooperators help within their group; offspring join the parent's group. A group that reaches a certain size may split in two, and another group goes extinct to hold the total constant (§ "Group selection").
- Only individuals reproduce, but selection acts on two levels. Within groups it favours defectors; between groups it favours cooperators, because pure-cooperator groups grow and split faster (§ "Group selection").
- This is group fecundity selection. Group viability selection (cooperator groups less likely to go extinct) is mentioned as an alternative (§ "Group selection").
- In the limit of weak selection and rare group splitting, with $n$ the maximum group size and $m$ the number of groups, cooperation can evolve provided
$$b/c>1+n/m \tag{5}$$

*Intuition note:* Within a group, defectors win; between groups, cooperative groups win. The threshold $1+n/m$ falls toward 1 when the number of groups $m$ is large compared with the maximum group size $n$ (our reading: the between-group advantage of cooperators is then easier to realise).

### Evolutionary success
- Payoff matrix for the row player, rows and columns ordered C, D, with entries $\alpha=$ C vs C, $\beta=$ C vs D, $\gamma=$ D vs C, $\delta=$ D vs D:
$$\begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}$$
- Without a mechanism, defectors dominate: $\alpha<\gamma$ and $\beta<\delta$ (§ "Evolutionary success").
- **ESS:** if $\alpha>\gamma$, cooperation is an evolutionarily stable strategy. An infinite cooperator population cannot be invaded by defectors under deterministic dynamics.
- **Risk-dominant (RD):** if $\alpha+\beta>\gamma+\delta$. If both strategies are ESS, the risk-dominant one has the bigger basin of attraction.
- **Advantageous (AD):** if $\alpha+2\beta>\gamma+2\delta$. This matters for stochastic dynamics in finite populations. The *fixation probability* is the chance that one mutant's lineage takes over the whole population. An AD strategy has fixation probability above $1/N$. Equivalent "1/3 rule": the invader's fitness at frequency $1/3$ exceeds the resident's. This holds under weak selection.
- Some mechanisms even make cooperators dominate: $\alpha>\gamma$ and $\beta>\delta$ (§ "Evolutionary success"; Fig. 2).

### Comparative analysis
Each mechanism becomes a 2×2 matrix (Table 1), the same shape as above (rows C, D; columns C, D; D vs D is 0). The text layer of Table 1 is flattened; entries are reconstructed in this order: C-vs-C, C-vs-D / D-vs-C, D-vs-D (§ Table 1).

| Mechanism | C vs C | C vs D | D vs C |
|---|---|---|---|
| Kin | $(b-c)(1+r)$ | $br-c$ | $b-rc$ |
| Direct | $(b-c)/(1-w)$ | $-c$ | $b$ |
| Indirect | $b-c$ | $-c(1-q)$ | $b(1-q)$ |
| Network | $b-c$ | $H-c$ | $b-H$ |
| Group | $(b-c)(m+n)$ | $(b-c)m-cn$ | $bn$ |

For network reciprocity, $H=\frac{(b-c)k-2c}{(k+1)(k-2)}$ (§ Table 1).

Conditions on $b/c$ (§ Table 1):

| Mechanism | ESS | RD | AD |
|---|---|---|---|
| Kin | $>1/r$ | $>1/r$ | $>1/r$ |
| Direct | $>1/w$ | $>(2-w)/w$ | $>(3-2w)/w$ |
| Indirect | $>1/q$ | $>(2-q)/q$ | $>(3-2q)/q$ |
| Network | $>k$ | $>k$ | $>k$ |
| Group | $>1+n/m$ | $>1+n/m$ | $>1+n/m$ |

- **How the matrices arise:** kin selection uses Maynard Smith's inclusive fitness: your payoff times $r$ is added to mine. Direct reciprocity: cooperators play tit-for-tat, defectors always-defect, with expected number of rounds $1/(1-w)$; tit-for-tat vs always-defect cooperates only on the first move. Indirect: a cooperator helps unless the other's reputation (known with probability $q$) marks a defector; defectors never help. Network: expected cooperator frequency follows a replicator equation with a transformed payoff matrix. Group: the within-group and between-group matrices are added (§ "Comparative analysis").
- Check (added step), kin ESS: $\alpha>\gamma$ means $(b-c)(1+r)>b-rc$, i.e. $b+br-c-rc>b-rc$, i.e. $br>c$, i.e. $r>c/b$.
- Results: for kin, network and group the same condition holds for all three measures, because when it holds cooperators dominate defectors. For direct and indirect reciprocity the ESS conditions are $w>c/b$ and $q>c/b$; RD and AD need slightly more stringent conditions (§ "Comparative analysis").
- Details and limitations are in the Supporting Online Material, which was not supplied (§ "Comparative analysis").

*Intuition note:* Every rule has the form "benefit-to-cost ratio above a threshold". In Table 1 the kin, direct and indirect thresholds are $1/r$, $1/w$ and $1/q$, so they equal 1 when $r$, $w$ or $q$ equals 1; the network threshold is $k$ (our reading: the better a mechanism lets help return to cooperators, the lower the threshold).

### Conclusion
- Each rule is a benefit-to-cost threshold. The payoff matrices can be imported into standard evolutionary game dynamics, for example replicator equations on graphs, for group selection and for kin selection (§ "Conclusion").
- **Not covered:** green-beard models (cooperators recognise arbitrary labels); voluntary games (some cooperation usually prevails in oscillations); punishment. Nowak says it is unclear whether punishment alone is a mechanism, since all models so far rest on indirect reciprocity, group selection or network reciprocity. It can raise cooperation in such models (§ "Conclusion").
- Kin selection theory based on the Price equation is more general and can compare mechanisms; Nowak does not take that approach here (§ "Conclusion").
- Nowak proposes that "natural cooperation" might be a third principle of evolution beside mutation and selection (§ "Conclusion").

## Toy example (ours, not from the text)
Direct reciprocity with $b=3$, $c=1$, $w=0.5$ (so $b/c=3$).
- Matrix from Table 1: $\alpha=(b-c)/(1-w)=2/0.5=4$; $\beta=-c=-1$; $\gamma=b=3$; $\delta=0$.
- ESS: $\alpha>\gamma$, $4>3$, so yes. Rule check: $w=0.5>c/b=1/3$.
- RD: $\alpha+\beta=3$ vs $\gamma+\delta=3$. Not strictly greater, so no. Threshold check: $(2-w)/w=1.5/0.5=3$, and $b/c=3$ is not $>3$.
- AD: $\alpha+2\beta=2$ vs $\gamma+2\delta=3$, so no. Threshold check: $(3-2w)/w=2/0.5=4>3$.
- With $w=0.2$: $\alpha=2/0.8=2.5<3$ and $0.2<1/3$. Cooperation is not ESS.

So tit-for-tat resists invasion by always-defect at $w=0.5$, yet is neither risk-dominant nor advantageous there.

## Concepts
- [[reciprocity (direct, indirect, network)]] — Nowak's three reciprocity mechanisms; direct = repeated meetings, indirect = reputation, network = clusters on a graph (§ "Direct reciprocity", "Indirect reciprocity", "Network reciprocity")
- [[evolutionarily stable strategy]] — here $\alpha>\gamma$: cooperators in an infinite population resist defector invasion (§ "Evolutionary success")
- [[replicator dynamics]] — used for cooperator frequency on graphs via a transformed payoff matrix (§ "Comparative analysis")
- [[dominant / dominated strategy]] — defectors dominate without a mechanism: $\alpha<\gamma$, $\beta<\delta$ (§ "Evolutionary success")
- [[strategic (normal-form) game]] — each mechanism is a 2×2 matrix game (§ "Comparative analysis")
- [[shadow of the future]] — canon link; here $w$, the probability of another round, sets the threshold $w>c/b$ (§ "Direct reciprocity")
- [[kin-selection]] (new) — selection favouring helping relatives; Hamilton's rule $r>c/b$ (§ "Kin selection")
- [[frequency-dependent-selection]] (new) — fitness depends on the relative abundance of types (§ intro)
- [[risk-dominance]] (new) — $\alpha+\beta>\gamma+\delta$; the bigger basin of attraction if both are ESS (§ "Evolutionary success")
- [[fixation-probability]] (new) — chance one mutant's lineage takes over; AD means above $1/N$ (§ "Evolutionary success")
- [[group-selection]] (new) — selection at two levels: within groups favours defectors, between groups cooperators (§ "Group selection")
- [[tit-for-tat]] (new), [[win-stay-lose-shift]] (new) — repeated-game strategies (§ "Direct reciprocity")

## Canonical instances
- [[prisoners-dilemma-repeated]] — framework for direct reciprocity (§ "Direct reciprocity")
- [[axelrod-tournaments]] — tit-for-tat won two computer tournaments (§ "Direct reciprocity")
- [[haldane-brothers-cousins]] — Haldane's "two brothers or eight cousins" remark illustrates $r$ (§ "Kin selection")

## Bridges (candidates)
- [structural-analogy] Direct-reciprocity threshold $w>c/b$ ↔ decision-game-theory: shadow of the future — higher continuation probability makes cooperation pay.
- [same-math] ESS condition $\alpha>\gamma$ ↔ Nash equilibrium: cooperation being a strict best response to itself, so (C,C) is a strict Nash equilibrium of the 2×2 game.
- [structural-analogy] Win-stay, lose-shift ↔ satisficing: keep your action while payoff meets an aspiration, otherwise change.
- [metaphor] Indirect reciprocity as "money" ↔ economics: reputation as a medium of exchange.

## Questions this raises
- Why do the RD and AD thresholds for direct and indirect reciprocity differ, while the three kin/network/group thresholds coincide?
- How do punishment or green-beard effects fit into the same matrix framework?
- How sensitive are the rules to the weak-selection and rare-splitting limits?
- Can empirical $r$, $w$, $q$, $k$, $n/m$ be measured well enough to test the rules?

## Reading notes
- Source is the PMC author manuscript (HTML) of Science 314(5805):1560–1563, 8 Dec 2006. It has no page numbers, so citations use section headings. The task metadata gives 4709 words for the source.
- Table 1 is flattened in the text layer. Matrices are reconstructed from the order shown; the fraction in $H$ and the ratios in the ESS/RD/AD columns are re-read as fractions. I checked one entry (kin ESS) by algebra.
- The Fig. 1 formulas come from the figure caption. Figures 1–3 themselves (graphics) were not available, only captions.
- The Supporting Online Material (derivations of the matrices) was not provided.
