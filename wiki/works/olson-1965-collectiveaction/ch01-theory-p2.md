---
id: olson-1965-collectiveaction/ch01-theory-p2
work: olson-1965-collectiveaction
unit: "Chapter I (part 2/2): sections D–F, Small Groups; Exclusive and Inclusive Groups; A Taxonomy of Groups"
pages: 22-52
fields: [political-science]
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
# A Theory of Groups and Organizations (part 2/2): small groups, exclusive/inclusive groups, taxonomy

## L0 — One line
Whether a group can supply itself with a collective good without coercion or outside inducements depends on the share of benefit each member gets and on whether members' actions are noticeable to one another, so small and large groups seem to differ in kind as well as in degree.

## L1 — The gist (≤ 120 words)
This part asks when groups can further their common interests voluntarily; small groups do so better than large ones. He builds a model in which each member compares his own share of the group's gain with the cost. A member with a large share may provide the good alone, but provision is normally suboptimal, and the largest member carries a disproportionate burden. Market groups want fewer members, while non-market groups usually want more. The chapter ends with a taxonomy: privileged, intermediate and latent groups. Latent (very large) groups need "selective incentives" (rewards or punishments aimed at individuals). This matters because it separates the existence of large associations from the logic that explains small groups.

**Prerequisites:** derivatives and setting a derivative to zero for a maximum; fractions and shares; marginal vs total cost; price elasticity of demand (basic idea).

## L2 — Key ideas
- A member of a group gains from providing a collective good (one that others in the group cannot be kept from enjoying) alone if his fraction $F_i$ of the group gain exceeds $C/V_g$ (total cost divided by total group gain). Then there is a presumption that the good is provided (p. 24).
- Each member would buy up to the point where $F_i(dV_g/dT)=dC/dT$. Because others cannot be excluded, the sum of these purchases falls short of the group optimum (pp. 24, 27–28).
- Suboptimality is worse the smaller the largest member's $F_i$, so, other things equal, it is worse in larger groups. Unequal members make provision more likely, but the largest bears a disproportionate burden: "exploitation" of the great by the small (pp. 28–29).
- Cournot's theory of oligopoly is a special case of the same model. A firm restricts output only if its share of industry output $F_i$ is at least the industry's elasticity of demand $E$ (pp. 25–26).
- Market groups seek an "exclusive" collective good (a higher price, fixed in supply), so they want fewer members. Non-market groups seek an "inclusive" good, so they usually welcome members. Which one applies depends on the objective, not on the members (pp. 37–39).
- Exclusive groups almost always need 100% participation, so a single holdout (a member who stays out to demand more) gains bargaining power, and more bargaining is likely. Inclusive groups, except in marginal cases, do not need full participation and evidently show much less strategic interaction (pp. 40–43).
- Taxonomy: privileged (someone gains by paying all), intermediate (indeterminate), latent (no one's action is noticeable). Latent groups act only through selective incentives (rewards or punishments applied to individuals according to whether they contribute) (pp. 49–51).
- Three cumulative factors disadvantage large groups, including organization costs that rise with group size (pp. 46–48).

## L3 — Walkthrough

### D. Small groups (pp. 22–36)

**Cost and gain setup.** Groups differ in how much each member values the good and in their cost functions. Total cost rises with the amount provided. Fixed or initial costs are very likely: setting up an organization, or the "lumpiness" of public goods, makes the first unit expensive. Costs also rise disproportionately for "excessive" demands. So cost $C=f(T)$, where $T$ is the level of the good obtained, and average cost curves are U-shaped (p. 22). If some quantity can be had so cheaply that one person would gain from providing it alone, there is a presumption it will be provided (p. 22).

**Definitions.** The group's "size" $S_g$ depends on the number of members and on the value of a unit to each. Example: property owners lobbying for a tax rebate; $S_g$ is total assessed valuation and $T$ is the rebate rate per dollar (p. 23). Group gain is $V_g=S_gT$. Individual gain is $V_i$. The fraction is $F_i=V_i/V_g$, so $V_i=F_iS_gT$. Individual advantage is $A_i=V_i-C$ (p. 23).

**The individual optimum.** What the group does depends on what individuals do, so look at how $A_i$ changes with $T$:
$$dA_i/dT=dV_i/dT-dC/dT.$$
At a maximum, $dA_i/dT=0$ (second-order condition $d^2A_i/dT^2<0$; fn. 40). With $F_i$ and $S_g$ constant,
$$d(F_iS_gT)/dT-dC/dT=0\quad\Rightarrow\quad F_iS_g-dC/dT=0 .$$
(If they are not constant: $F_iS_g+F_iT(dS_g/dT)+S_gT(dF_i/dT)-dC/dT=0$; fn. 41.) This gives the amount an independent individual would buy, if he buys any (p. 24). Since $dV_i/dT=F_i(dV_g/dT)$ (the author's step on p. 24),
$$F_i(dV_g/dT)=dC/dT .$$
So the rate of group gain must exceed the rate of cost increase by the multiple $1/F_i=V_g/V_i$ (p. 24).

**Whether any good is provided.** This matters more than how much. If $F_i>C/V_g$, then $V_i/V_g>C/V_g$, so $V_i>C$: the individual gains more than the whole cost (p. 24). Summary rule: there is a presumption of provision if, where $dV_g/dT=(1/F_i)(dC/dT)$, the group's benefit is a larger multiple of cost than the group's gain is of the individual's gain: $V_g/C>V_g/V_i$ (p. 25).

*Intuition note:* If a person's own slice of the benefit is bigger than the whole bill, there is a presumption he will provide the collective good alone. The bigger his slice, the easier that is to meet.

**Market application (Cournot).** Take an industry of independent profit-maximizing firms with zero marginal cost. Now $T$ is price, $S_g$ industry sales, $S_i$ firm sales, $F_i=S_i/S_g$. Elasticity is $E=-\,T/S_g\,(dS_g/dT)$, so $dS_g/dT=-ES_g/T$ (p. 25). The firm's optimum:
$$dA_i/dT=d(S_iT)/dT=0;\quad S_i+T(dS_i/dT)=0;\quad F_iS_g+T(dS_i/dT)=0 .$$
The firm acts independently, expecting no reaction from others, so $dS_i=dS_g$ as printed. Then $F_iS_g+T(dS_g/dT)=0$, hence $F_iS_g-T(ES_g/T)=0$, hence $S_g(F_i-E)=0$ (p. 25). This holds only when $F_i=E$. A firm has an incentive to restrict output only when industry elasticity is less than or equal to its share of output (p. 26).

Examples (p. 26):
- If $E=1/4$, a 1% output cut raises price 4%, so a firm with one fourth of output should restrict.
- With 1000 equal firms, $E$ would have to be $1/1000$ or less before any restriction.
- Hence no profits in equilibrium in an industry with a really large number of firms.

The author says this is identical with Cournot's analysis, which is a special case of the general theory (p. 26).

*Intuition note:* A firm that supplies a small share of the market loses all of the revenue from its own restraint but gets only a small share of the gain from the resulting higher price.

**Two questions for individual and group.** A nonmarket individual asks (1) whether total benefit exceeds total cost, and (2) how much to provide, which depends on marginal values (p. 27). For the group, the Pareto-optimal amount is where $dV_g/dT=dC/dT$ (p. 27). Each member buys until $F_i(dV_g/dT)=dC/dT$ and the $F_i$ sum to one. So it first appears that individual purchases would add up to the group optimum, with burdens shared in proportion to benefits (p. 27). The author then says this is not so (p. 27).

**Suboptimality and burden.** Normally provision is "strikingly suboptimal" and the burden "highly arbitrary" (pp. 27–28). The reason is that what one member provides for himself automatically goes to the others. Nobody has an incentive to provide more once the member with the largest $F_i$ has bought his preferred amount (p. 28; fn. 44 assumes equal amounts for all, as with a pure public good). The shortfall is more serious the smaller the largest $F_i$; more members mean smaller $F_i$'s, so larger groups generally perform less efficiently (p. 28). $F_i$ also depends on the member's "size" $S_i$, the extent to which he benefits (an estate owner vs. a cottager). A group with unequal members is less suboptimal and more likely to provide some good than an otherwise identical equal group (pp. 28–29). The member with the largest $F_i$ bears a disproportionate share of the burden. Hence a systematic tendency for the "exploitation" of the great by the small (p. 29; fn. 47 says the word carries no moral conclusion).

**Qualifications.** Strategic bargaining is neglected (fn. 48). Olson argues that a large member's threat to cut his provision is not credible, because he would suffer more, so bargaining probably leads to the same results (fn. 48). Income effects would tend to keep the largest member from bearing all of the burden (fn. 46). Institutional arrangements can change the results (p. 30).

**Condition for optimality.** Optimal voluntary provision requires marginal costs to be shared in exactly the proportion of additional benefits, so each member's marginal cost equals his marginal benefit while total marginal cost equals total marginal benefit (pp. 30–31). Any other sharing gives suboptimal provision. Supraoptimal provision does not arise: in a voluntary group, members whose cost share exceeds their benefit share stop contributing (p. 31). Footnote 50 gives share tenancy as an illustration. Footnote 51 links the argument to "public squalor" amid "private splendor".

**The figure (p. 32).** Horizontal axis $T$, vertical axis dollars. The steep line is $S_gT=V_g$. The flatter line is $F_iS_gT=V_i$. The curve $C$ starts above zero (fixed cost) and rises steeply at the right. At an amount $B$: $C=EB$, $V_g=HB$, $F_i=DB/HB$, and since $DB>EB$, $F_i>C/V_g$. The individual's $V_i$ line is above the cost curve for every amount between $V$ and $W$, so he would presumably be better off having provided any amount in that range, optimal or not (pp. 32–33).

**Two things to determine** (p. 33): the individual optimum $F_i(dV_g/dT)=dC/dT$ (if $F_i$ is not constant: $F_i(dV_g/dT)+V_g(dF_i/dT)=dC/dT$; fn. 52), and whether some member has $F_i>C/V_g$ there.

**Hume (fn. 53).** Olson says Hume sensed that small groups can reach common purposes and large ones cannot, but notes that Hume's argument is somewhat different from his own. In Hume's example two neighbours can agree to drain a meadow, while a thousand persons find it very difficult, indeed impossible in Hume's words, to agree, each seeking to lay the burden on others (pp. 33–34).

**Nontechnical summary (pp. 33–36).**
- In some small groups at least one member would gain even if he paid the whole cost; then provision is presumed. Very small groups, and especially unequal ones, are most likely to provide (p. 34).
- Even so, provision is not usually optimal. A member gets only part of the benefit of any expenditure, and what he receives free from others further reduces his incentive. The larger the group, the farther it falls short (p. 35).
- Only special institutional arrangements give incentives that add up to the group optimum (pp. 34–35).
- The smaller member, once he has what the largest gives free, has no incentive to buy. The "great" are exploited by the small (p. 35).
- The argument may apply to burden-sharing in the UN and NATO and to neutralism among small countries (p. 36). It may also apply to metropolitan local governments (the central city bears disproportionate shares) and to price leadership (p. 36).
- The most important point: small groups may provide a collective good simply because of its attraction to individual members. The larger the group, the less it will further common interests (p. 36).

### E. "Exclusive" and "inclusive" groups (pp. 36–43)

**Opposite attitudes to membership.** Firms want fewer rivals, ideally a monopoly. Nonmarket associations usually want more members, since more members may lower costs for those already in, and may even try to make membership compulsory (p. 37). **Why:** in a market, the "collective good" (higher price) is fixed in supply, so what one firm captures another cannot. In a nonmarket group, what one consumes another may also enjoy (p. 37). A prospering firm becomes a more formidable rival, while a prospering member may have an incentive to pay more (pp. 37–38).

**Terms.** An *exclusive collective good* has a fixed supply that members divide. An *inclusive collective good* automatically expands with the group (p. 38). Footnote 58 relates these to Head's two properties of public goods (infeasibility of exclusion; jointness of supply) and to Buchanan's club theory.

**Depends on objective.** Whether a group behaves exclusively or inclusively depends on the objective, not on members' characteristics (p. 39). Firms are exclusive when restricting output for a higher price, but inclusive when seeking lower taxes or tariffs. Unions illustrate the ambivalence: "solidarity" and closed shops, yet apprenticeship rules that limit entrants (p. 39; fn. 59 suggests that unions' political aims may explain wage demands that reduce employment).

**Participation.**
- *Inclusive:* as many as possible will be included in organized effort. Except in marginal cases (good only just worth its cost), it is not essential that every individual participate, because a nonparticipant does not take benefits away from cooperators (p. 40). Fn. 61: this does not require pure public goods; if there is crowding, dues must at least equal the loss to old members.
- *Exclusive:* collusion almost always needs 100% participation. Unless its own costs rise too rapidly with output, a single nonparticipating firm can usually expand output and take all the benefit until the colluders have cut output to zero (p. 41). Fn. 62: if the holdout's marginal costs rise very steeply, a holdout need not be fatal but is still costly.
- This resembles a unanimity rule. A holdout has extraordinary bargaining power, and anyone can try to be one. This makes group action less likely and bargaining more intense (p. 41; fn. 63 cites Buchanan and Tullock).
- Footnote 60 argues that Riker's minimum-winning-coalition argument does not weaken these conclusions, since the book's situations are not zero-sum.

**Strategic interaction.** Where groups are small enough for one member's action to affect another, exclusive groups show oligopolistic interdependence. Each firm watches for price wars, is both a rival and an indispensable collaborator, and may hold out. This increases "the intensity and complexity of oligopolistic reactions" (p. 42). In inclusive groups, even small ones, bargaining and strategic interaction are evidently much less common. There is no wish to eliminate anyone, and no unanimity is needed. So independent behavior frequently describes members reasonably well (pp. 42–43).

*Intuition note:* In a market, the prize is a fixed pie, so the holdout's gain is the colluders' loss. In a lobby, the prize grows with membership, so holdouts take little from others.

### F. A taxonomy of groups (pp. 43–52)

**Intermediate size.** Strategic interaction is relatively important in one size range: the group is not so small that one member would buy the good himself, but small enough that each member's contribution or lack of it noticeably affects others (p. 43). If one member stops paying, others' costs rise noticeably and they may stop too. He might realize this, and he "might; or he might not". The result is indeterminate, as in oligopoly. The author says there seems to be no way at present of getting a general, valid and determinate solution at this level of abstraction (p. 43). Footnote 64 compares this to logrolling: all interests gain if logs are rolled, but bargaining over terms may break down.

**Range of indeterminateness.**
- If some member would gain by paying all the cost, there is a presumption of provision (p. 44).
- If no member would, but each is important enough to be noticed, the result is indeterminate (p. 44).
- In a large group where no single contribution makes a perceptible difference, "it is certain" that the good will not be provided without coercion or outside inducements (p. 44; but see fn. 68).
- Footnote 66 (**objection from a "friendly critic"**): a large organization could continue providing a good by a plebiscite pledge. **Olson replies:** the argument is mistaken. An individual gets the benefits whether he pledges or not, so he has no incentive to pledge unless unanimity is required or his one pledge would for some other reason decide whether the good is provided. If unanimity is required, any one member could hold out for bribes, and others could do the same, so provision is unlikely (fn. 66).

**What matters: perceptible interdependence.** Whether any two or more members have perceptible interdependence separates the group so large that it definitely cannot provide itself with a good from the oligopoly-sized group that may do so without coercion or outside inducements (p. 45). This depends to a striking degree on number, but not solely on number. Unequal interests and a very valuable good make provision more likely, much as, in market structure, the number of firms compatible with oligopoly varies from case to case (p. 45). Footnote 67: noticeability depends on the knowledge and institutional arrangements actually in the group, but Olson knows of no practical example of a group doing much beyond improving information.

**Organization costs** (pp. 46–47).
- Smallest groups (someone would pay all) may get along without any agreement or organization; neither is indispensable (p. 46).
- In intermediate groups, at least tacit coordination is needed (p. 46).
- Larger groups need more agreement and organization, and costs of organization are "an increasing function of the number of individuals" (p. 46). Total costs rise with membership, though cost per person need not, because of economies of scale (pp. 46–47).
- If a group is already organized for another purpose, these costs are already met (p. 47).
- These costs differ from direct resource costs. They are the costs of communication, bargaining, and creating, staffing and maintaining an organization (p. 47).
- There is a minimum amount of organization, so minimal costs exist and rise with group size. Added to other initial costs, they make the first unit of a good expensive. The higher the absolute total costs, the less likely even a minimal amount is obtained without coercion or outside incentives (pp. 47–48).

**Three cumulative factors against large groups** (p. 48):
1. The larger the group, the smaller the fraction of benefit any person acting in the group interest receives, so the farther the group falls short of an optimal supply.
2. The smaller the share going to any individual or small subset, the less likely that any of them gains enough to bear the burden, so oligopolistic interaction is less likely.
3. Organization costs are greater, so the hurdle before any good can be obtained is higher.

Very large groups normally will not, absent coercion or separate incentives, provide even minimal amounts (p. 48). Footnote 68 gives one empirically "trivial" case in which a large group gets a minute amount: a cheap good that one original member would pay for alone even as millions join. Olson keeps the theory refutable by treating the large-group result as an empirical hypothesis, not a definition (fn. 68).

**Classification** (pp. 49–51). For markets (from Olson and McFarland): pure monopoly (one firm), oligopoly (few firms, noticeable effects), atomistic competition (no noticeable effect), subdivided further (p. 49). For nonmarket groups:
- *Analogue of monopoly:* a single individual seeking a non-collective good (p. 49).
- **Privileged group:** each member, or at least one member, has an incentive to see the good provided even if he bears the full burden. A presumption of provision, possibly with no organization at all (p. 50). Fn. 70: it is conceivable that bargaining fails, or members each wait for the others, but Olson thinks they would not make this mistake permanently.
- **Intermediate group:** no single member gets enough to provide alone, but members notice each other's contributions. The good "may, or equally well may not" be obtained, and never without some coordination or organization (p. 50). Fn. 71 quotes Simmel on the mixed character of intermediate structures.
- **Latent group** (analogue of atomistic competition): one member's contribution or lack of it noticeably affects no one else, so no one reacts. The individual therefore has no incentive to contribute, however valuable the good is to the group (p. 50).

**Selective incentives** (pp. 50–51). A latent group acts only through separate, "selective" incentives that treat contributors and noncontributors differently. They can be negative (coercion) or positive (rewards). A latent group so led to act is a "mobilized" latent group. "Latent" means it has a capacity for action that can be realized only with selective incentives (p. 51). Footnote 72 defines the incentives in terms of indifference curves: they must be worth more to each individual than his share of the cost. Smaller ones will not mobilize a latent group (fn. 72).

**Conclusion.** The chances of group-oriented action differ by category. Sometimes one may expect provision, sometimes provision is ruled out absent selective incentives, and sometimes it could go either way. Size is a determining factor, and small groups will further their common interests better than large ones (pp. 51–52). Olson concludes that it "now seems" small groups are "qualitatively" as well as quantitatively different, and the existence of large associations cannot be explained by the factors that explain small groups (p. 52).

## Toy example (ours, not from the text)
Two members, A and B. Group gain $V_g=S_gT=10T$. Cost $C=T^2$, so $dC/dT=2T$. A gets $F_A=0.6$, B gets $F_B=0.4$.

- A's optimum: $F_AS_g=dC/dT\Rightarrow 0.6\cdot10=2T\Rightarrow T=3$. B alone would choose $0.4\cdot10=2T\Rightarrow T=2$.
- Does A provide? $V_A=0.6\cdot10\cdot3=18$, $C=9$, $A_A=18-9=9>0$. Also $F_A=0.6>C/V_g=9/30=0.3$ (check: $V_g=30$).
- B already receives $T=3$ free. This is more than the 2 he would buy, so B adds nothing.
- Group optimum: $dV_g/dT=dC/dT\Rightarrow10=2T\Rightarrow T=5$. Provision is 3, below 5.
- Group net at 5: $50-25=25$. At 3: $30-9=21$. So the group loses 4 from suboptimality.
- Burden: A pays 100% of cost (9) for a 60% share of benefit. B pays 0 for a 40% share. A's net is $18-9=9$, and B's net is $0.4\cdot30=12$. This is the "exploitation of the great by the small".
- Proportional marginal-cost sharing: at $T=5$, marginal cost is 10. A pays $0.6\cdot10=6$ (equal to his marginal benefit 6) and B pays 4 (equal to his marginal benefit 4). Both are willing to go on to $T=5$.
- Large-group contrast: with 1000 equal members, $F_i=0.001$. Suppose a fixed organization cost of 1 is added, so $C=1+T^2$. The member's optimum is $0.001\cdot10=2T\Rightarrow T=0.005$. His gain is $V_i=0.001\cdot10\cdot0.005=0.00005$, while $C=1.000025$. So $A_i<0$ and nobody provides.

## Concepts
- [[collective action problem]] — a group with common interests fails to provide itself with the good because of the logic of individual incentives; this logic depends on group size (p. 36, p. 52)
- [[public good]] — here "collective good": others cannot be excluded once one member provides it (p. 28; fn. 44 on Samuelson's pure public good)
- [[free rider]] — a member who receives the good free from others and has no incentive to contribute (the idea is stated, not the term) (p. 35)
- [[selective incentive]] — reward or punishment applied to individuals according to whether they contribute; the only thing that stimulates a rational member of a latent group (p. 51)
- [[fraction-of-group-gain]] (new) — $F_i=V_i/V_g$, the member's share of group gain; drives his incentive to provide (p. 23)
- [[suboptimal-provision]] (new) — voluntary provision below the group's Pareto optimum, worse with group size (pp. 27–28)
- [[exploitation-of-the-great-by-the-small]] (new) — the member with the largest $F_i$ bears a disproportionate share of the burden (p. 29)
- [[exclusive-collective-good]] (new) — benefit fixed in supply (e.g. supracompetitive price), so members want fewer others (p. 38)
- [[inclusive-collective-good]] (new) — benefit expands with the group, so members welcome new members (p. 38)
- [[holdout]] (new) — a member who withholds participation to extract a larger share, powerful when full participation is needed (p. 41)
- [[noticeability]] (new) — whether one member's contribution perceptibly affects another's burden or benefit; the standard that separates intermediate from latent groups (pp. 44–45)
- [[organization-costs]] (new) — costs of communication, bargaining and creating or maintaining an organization; rise with group size (pp. 46–47)
- [[privileged-group]] (new) — a group in which some member gains from providing the good even if he pays all the cost (p. 49)
- [[intermediate-group]] (new) — no one would provide alone, but members notice each other; outcome indeterminate (p. 50)
- [[latent-group]] (new) — very large group, no noticeable individual contributions; needs selective incentives (p. 50)

## Canonical instances
- [[cournot-oligopoly]] — a firm restricts output only if its share $F_i\ge E$; a special case of the general model (pp. 25–26)
- [[property-tax-rebate-lobby]] — illustrates $S_g$, $T$ and $F_i$ (p. 23)
- [[share-tenancy]] — landlord and tenant share the output as a public good, with inefficient factor use (fn. 50, p. 31)
- [[alliance-burden-sharing]] — apparent tendency for large countries to bear disproportionate shares in the UN and NATO, which the small-group analysis could help explain (p. 36)
- [[metropolitan-local-governments]] — the analysis suggests the largest local government (e.g. the central city) would bear disproportionate shares of spillover goods (p. 36)
- [[union-ambivalence-on-entry]] — "solidarity" and closed shops vs. apprenticeship limits on new entrants (p. 39)
- [[logrolling]] — indeterminate bargaining parallel to oligopoly (fn. 64, pp. 43–44)
- [[hume-meadow]] — two neighbours can drain a meadow; a thousand persons cannot easily agree (fn. 53, pp. 33–34)

## Bridges (candidates)
- [same-math] Olson's $F_i = E$ condition ↔ industrial organization: Cournot's firm-level first-order condition — the author states that the analyses are identical.
- [structural-analogy] The 100%-participation holdout in exclusive groups ↔ political science: veto players under a unanimity rule — one actor's consent is needed, giving bargaining power.
- [structural-analogy] Disproportionate burden on the member with the largest $F_i$ ↔ international relations: large allies bearing alliance costs.
- [structural-analogy] Latent groups needing selective incentives ↔ political science: collective action problems and free riders in large associations.
- [metaphor] "Noticeability" threshold ↔ social network scale: groups where each member can see the others' actions are easier to coordinate.

## Questions this raises
- If no member's action is noticed in a latent group, what exactly makes a selective incentive worth more than the cost share (fn. 72)?
- How much would explicit bargaining, which the model sets aside, change the suboptimality results (fn. 48)?
- Do institutional arrangements that make contributions publicly known really increase noticeability (fn. 67)?
- Can groups pursuing both exclusive and inclusive goods be studied with this distinction (p. 39)?

## Reading notes
- This part starts at the very end of section C (a paragraph fragment about "oligopolistic groups", p. 22), then begins section D. It ends at the end of the chapter on printed p. 52, after section F. Printed page numbers are given on all pages.
- Page images were given only for pdf 36, 37, 38 and 45. Other equations were taken from the text layer, which is garbled in places (e.g. "$F_i$" appears as "F," or "Pi"). On p. 27 the sum "$\sum F_i=1$" is garbled in the text layer ("P,= 1"); I read it as $\sum F_i = 1$ from the context.
- On p. 25 the independence assumption is given as $dS_i=dS_g$ (as the image shows).
- Some words in the text layer are garbled ("tlexploitation", "Ammcan"); these are OCR artefacts.
- Footnote 54 on p. 36 is marked "[Footnote added in 1970.]". Footnote 68 refers to "page 161, note 94", which is outside this unit.
- The long Hume passage (fn. 53) and several footnotes (e.g. on Lindahl, Buchanan, Riker, Simmel) are summarized only briefly.
