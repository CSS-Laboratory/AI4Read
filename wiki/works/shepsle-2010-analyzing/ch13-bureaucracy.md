---
id: shepsle-2010-analyzing/ch13-bureaucracy
work: shepsle-2010-analyzing
unit: 13 Bureaucracy and Intergovernmental Relations
pages: 407-444
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 21
pipeline_version: 0.1
---
# Bureaucracy and Intergovernmental Relations

## L0 — One line
Whether bureaucrats or politicians have the upper hand depends on the model: Niskanen gives bureaus an information advantage, Miller–Moe give rough bargaining parity, and McNollgast treat bureaus as agents of politicians, who can anticipate bureaucratic drift and try to reduce it.

## L1 — The gist (≤ 120 words)
How should we explain the relation between policy makers (mainly legislators) and policy implementers (mainly bureaucrats)? Shepsle compares three rational-choice answers. Niskanen: budget-maximizing bureaus exploit private cost information and a passive legislature, so they overproduce. Miller and Moe: an active legislature makes it a bilateral bargain. McNollgast: the legislature creates the bureau as its agent, but the agent still "drifts" towards its own preferences within limits set by the enacting coalition. Shepsle adds capture and coalitional drift, and an FTC test favouring the principal-agent view. The point: the politics of policy and of administration cannot be separated, and each model captures part of the truth.

**Prerequisites:** reading supply/demand-type curves; maximizing a quadratic with a derivative; ideal points in a two-dimensional policy space; the idea that committees gather information (previous chapter).

## L2 — Key ideas (5–10 bullets)
- Niskanen replaces the "public servant" ideal with a bureau chief who maximizes the budget. Why they want it (pay, prestige, mission) does not matter (p. 410).
- In Niskanen's model the bureau's cost is private, the legislature's willingness to pay is known, and the legislature is passive. Output then exceeds the social optimum: $Q^0 \le Q^{**} \le Q^*$ (pp. 411–415).
- Changing motives changes the result: slack-maximizing gives the right output at too high a cost, and a quiet life probably gives underproduction (pp. 416–417).
- Miller and Moe treat the legislature as an active bargainer, so it is not clear that the bureau dominates (pp. 418–420).
- Shepsle objects that Congress creates and sustains bureaus (pp. 420–421); McNollgast therefore treat bureaus as agents of an enacting coalition. A bureau can "drift" from the policy $x$ to $x'$ because punishment needs the whole enacting coalition to agree (pp. 425–428).
- Politicians limit drift before the fact by choosing appointees and by procedural rules. Oversight comes in police-patrol, fire-alarm and fire-extinguisher forms (pp. 428–432).
- Slippage takes four forms: budgetary exploitation, bureaucratic drift, capture, and coalitional drift. Protection from coalitional drift comes at the price of more potential for bureaucratic drift (pp. 433–437).
- The FTC episode of 1979 fits the principal-agent view better than the "runaway agency" view (pp. 438–440).

## L3 — Walkthrough

### Introduction (pp. 407–408)
Popular opinion expects public servants to be selfless, unlike people in the market. Shepsle calls this unrealistic and a largely useless basis for analysis (pp. 407–408). He studies bureaucracy as a case of **intergovernmental relations**: the link between policy formulators (mainly legislators) and implementers (mainly bureaucrats) (p. 408).

### Intergovernmental relations I: budget-maximizing bureaucrats and a passive sponsor (pp. 408–417)

**Motivation (pp. 408–410).** Niskanen treats a bureau like a division of a private firm. Its chief is assumed to maximize the bureau's budget, as a private manager maximizes profit (p. 409). Possible reasons are pay and perks, prestige and power over subordinates, and belief in the bureau's mission (pp. 409–410). Shepsle's point, about Niskanen's assumption, is that it does not really matter why the bureaucrat wants a big budget; what matters is that she wants more resources rather than less (p. 410).

**The model (pp. 410–414).**
- The legislature (more precisely its median voter) values output $Q$ with diminishing returns. Its willingness-to-pay curve is $B$. The bureaucrat knows $B$ (pp. 410–411).
- Production has diminishing returns to scale, so total cost $TC$ rises at an increasing rate. $TC$ is private information of the bureau (p. 412).
- Footnote 3 gives the equations, with $a,b,c,d>0$:
$$B = aQ - bQ^2,\qquad TC = cQ + dQ^2 .$$
- The bureau must cover its costs, so it can only choose $Q$ where $B \ge TC$. This is the interval $[L,H]$ (p. 412).
- The bureaucrat picks the $Q$ with the highest point on $B$ within $[L,H]$. Footnote 4 states it as: maximize $aQ-bQ^2$ subject to $aQ-bQ^2 \ge cQ+dQ^2$ (p. 412).
- **Case 1 (Fig. 13.1).** The unconstrained peak of $B$ lies inside $[L,H]$. Footnote 5: $a-2bQ=0$, so
$$Q^* = \frac{a}{2b}.$$
The bureau gets a "profit" $B-TC$ at $Q^*$. The legislature cannot see it, because it does not know $TC$. No owners can pocket it; instead the bureau has "pin money" with which its managers can "consume on the job" (p. 413).
- **Case 2 (Fig. 13.2).** Costs rise so steeply that $Q^*$ lies outside $[L,H]$. The best feasible output $Q^{**}$ is where $B=TC$ (p. 413). Footnote 7:
$$Q^{**}=\frac{a-c}{b+d}.$$
(added step: setting $aQ-bQ^2=cQ+dQ^2$ and dividing by $Q>0$ gives $a-c=(b+d)Q$.)
- Niskanen compares $Q^*$ (demand-constrained) and $Q^{**}$ (cost-constrained) with the **socially optimal** $Q^0$, which maximizes $B-TC$. This is akin to the choice of a profit-maximizing firm, on the assumption that society, not the bureau, keeps the profit (p. 414).
- Result: $Q^0 \le Q^{**} \le Q^*$. Bureaus seeking maximal budgets produce too much (p. 414). Niskanen concludes that bureaucracies are too big, budgets too large and output more than society wishes (pp. 414–415).

*Intuition note:* The legislature says how much it would pay for each amount of output, and the bureau picks the point that gives the biggest budget it can afford. Society would prefer to stop earlier, where the gap between value and cost is largest.

**Variations on Niskanen (pp. 415–417).** Shepsle's method: a critic should name the assumption to change, not just attack the conclusion (p. 415).
- *Slack-seekers.* If bureaucrats maximize $B-TC$ and can hide costs, output is $Q^0$, the socially optimal level. The "profit" (called organizational slack) is not returned. Bureaus are then not too large but too expensive. Shepsle suggests the root of the problem lies in the secrecy that protects costs (p. 416).
- *Quiet life.* If bureaucrats are risk averse and want routine ("minimal squawk"), Shepsle says it "seems likely" they will underproduce relative to $Q^*$, $Q^{**}$ and $Q^0$. He has not formalized this (p. 417).
- Lesson: bureaus may overproduce, underproduce, or produce at the optimum inefficiently. The analyst must think hard about which motivational hypothesis is more appropriate in each application; Shepsle thinks it likely that no single hypothesis fits everywhere equally well (p. 417 and n. 11).

### Intergovernmental relations II: bilateral bargaining (pp. 417–420)
- Miller and Moe criticize two Niskanen assumptions: asymmetric information and a passive legislature. Niskanen's setting is a monopoly bureau with private information and a passive sponsor. Miller and Moe liken the known $B$ to a used-car customer who announces her maximum price for every car (p. 418).
- Shepsle argues that legislators would soon realize they are being hoodwinked if they stayed passive (p. 418). The bureau can research legislators' preferences from their constituents, but legislators can research too: committees collect information on production costs, hold hearings, request documents, use staff, and later do oversight. Shepsle says the legislature can be much more proactive than Niskanen credits, and in the real world is (p. 419).
- **Miller and Moe's view:** the realistic picture in American politics is *bilateral monopoly*, one customer (a committee) bargaining with one supplier (the bureau). Each has information the other may or may not know (p. 419).
- They show that the bureau need not be in the driver's seat. A committee that learns the bureau's costs, or hides its own willingness to pay, can force the bureau to reveal a menu of production possibilities from which the legislature chooses (pp. 419–420). Whether bureaus are then too big or too small depends on more complicated considerations (p. 420).

### Intergovernmental relations III: principals and agents (pp. 420–430)

**Shepsle's objection (pp. 420–422).** Both earlier models treat the structure as fixed in advance. In fact Congress created the executive departments, agencies and many other bodies by acts. It also set personnel and administrative procedures, drafts laws, approves appropriations and oversees their use (pp. 420–421). Shepsle finds it hard to square a dominant bureaucracy with these facts, and thinks abuses are unlikely to last long without implicit approval of key legislators (p. 421). Miller–Moe's parity also hides the legislature's power to create, sustain or destroy a bureau (p. 422). So he turns to the subordinate-bureaucracy view (p. 422).

**Principal–agent relationships (pp. 423–425).** A principal hires an agent for specialized skill but cannot easily observe quality, as in the kitchen contractor example (p. 423). Control tools:
- *Before the fact:* reputation, recommendations, certification, credentials, interviews. These rely on the agent valuing his reputation (pp. 423–424).
- *After the fact:* payment tied to completion, bonuses, bonds, inspection, lawsuits (p. 424).
- The agent also works for himself, so conflicts of interest arise, and the controls are imperfect (p. 424).

**McNollgast (pp. 425–430).**
- Legislation creating an agency sets up a principal-agent relation between an *enacting coalition* (legislators in both houses and the president) and the agency. The coalition wants faithful implementation and durability (p. 425).
- *EPA example (Fig. 13.3).* Axes: authority (horizontal) and resources (vertical). The House ($H$) wants little of both. The Senate ($S$) wants wide authority but only slightly more resources than the House. The president ($P$) is in between on authority and wants lots of resources. The agency's ideal $B$ exceeds all three on both dimensions (p. 426). The coalition agrees on a compromise $x$ (p. 426).
- If the agency implements a policy outside the triangle $HSP$, such as $y$, some alternative is unanimously preferred by the three principals, so they would react (p. 427). Inside or on the triangle, any move away from a point hurts at least one principal, and punishment needs a House majority, a Senate majority and the president together (p. 428).
- So the best the agency can do is $x'$, the point of the triangle closest to $B$. The gap $x \to x'$ is **bureaucratic drift** (p. 428).
- Footnote 18: if the agency cannot spend more than appropriated, $x'$ slides down the triangle's side to the height of $x$ (p. 428).
- After-the-fact controls (hearings, annual appropriations, watchdogs like the Government Accountability Office) are weak. The bureau pre-empts them by choosing $x'$ (p. 428).
- *Before-the-fact controls:* (1) **appointments**: by nominating and confirming, president and Senate can shift the location of $B$, which is a self-enforcing mechanism (p. 429). (2) **Procedural controls**: the Administrative Procedures Act and tailored rules. Requiring the EPA to proceed case by case should favour business, which can mobilize case by case, against environmental groups, who mobilize more easily for a few big decisions (pp. 429–430).
- Summary: the bureau is an agent whose own goals may conflict with the coalition's. The agent will be spared punishment as long as no alternative is preferred by all members of the coalition to whatever the agent does. (Dog on a leash: no pulling as long as the leash is slack.) McNollgast stress an asymmetric advantage for politicians; the coalition can anticipate drift and write provisions into the enabling legislation to reduce it, "if not eliminate it altogether" (p. 430).

*Intuition note:* A bureau can move toward its own ideal until the move would make all principals unhappy at once. Since punishing needs all of them to agree, the safe region is the triangle between their ideal points.

### Case 13.1: Oversight (pp. 431–432)
- Monitoring is central to any principal-agent relation (p. 431).
- McCubbins and Schwartz: **police-patrol** oversight is centralized, direct, and started by Congress. **Fire-alarm** oversight is decentralized and reactive. Congress sets rules that let affected private parties raise alarms (pp. 431–432).
- Shepsle adds **fire-extinguisher** oversight, in which service recipients get legal standing to sue in court (p. 432).
- Legislators often prefer fire alarms and extinguishers because they cost less time and use outside expertise (p. 432).

### Agency slippage (pp. 433–437)
Policies are not self-implementing. **Agency slippage** (drift) means the implemented policy departs from the one the principals formulated. It arises from agent discretion, agent preferences that differ from the coalition's, and imperfect controls (p. 433). Four forms:
- **Budgetary exploitation (Niskanen):** the bureau's informational advantage is turned into on-the-job consumption (pp. 433–434).
- **Bureaucratic drift (McNollgast):** authority and resources are used for other policy goals. This is safe as long as the bureau avoids unanimous opposition from the coalition's components (p. 434).
- **Bureaucratic capture:** in Fig. 13.3 the Senate and the president both prefer $x'$ to $x$, and only the House loses (p. 435). Real chambers have many ideal points, so Shepsle says it is very likely that a number of members sympathize with the bureau. He thinks it likely that the committees with jurisdiction are outliers who share its preferences and can protect it through gatekeeping and agenda control; interest groups and constituencies will be pleased too. This is the "cozy little triangle" or "policy whirlpool" (pp. 435–436). The tension is then between insiders and outsiders of the whirlpool, not between politician and bureaucrat (p. 436).
- **Coalitional drift:** politicians want deals to endure, but American coalitions shift (p. 436). Legislative structure, such as the Agriculture Committees protecting grain subsidies, helps only partly (p. 436). Politicians can insulate the bureau with long lives for agencies, long terms for heads, overlapping terms and secure revenue (p. 437). **Trade-off:** protection from coalitional drift comes at the price of more bureaucratic drift (p. 437).

*Intuition note:* A coalition that fears losing power wants to shield its deal from future legislators, but the same shield also shields the bureau from today's legislators.

### Case 13.2: How to test Niskanen? (pp. 438–440)
Weingast and Moran study the FTC. In 1979 Congress curbed it by criticism, halted activities and cut funds. Within about eighteen months the FTC curtailed its controversial activity (p. 438).
- **Niskanen-like view:** the FTC was a runaway agency that Congress finally clamped down on (pp. 438–439).
- **McNollgast/coalitional-drift view:** Congress was in control all along. The oversight committees' composition and preferences changed, and the new principals pulled the leash (p. 439).
- **Test:** Americans for Democratic Action (ADA) liberalism ratings (0–100) of members of the Senate consumer-affairs subcommittees. They show a significant conservative drift between 1976 and 1979, after more than a decade of virtually no change. They also show substantial membership turnover (pp. 439–440). In the two decades before, the panels were much more liberal, suggesting the FTC was then a loyal agent (p. 440).
- **Conclusion:** the evidence is consistent with McNollgast. The FTC seems to have been an agent that failed to notice its principal had changed (p. 440).

### Conclusion (pp. 440–441)
Shepsle says political scientists no longer hold that policy making and policy implementation can be sealed off from one another (p. 440). Niskanen: bureaucracy exploits information. Miller–Moe: informed, proactive politicians yield balanced bargaining. McNollgast: any asymmetry favours the political principals (p. 441). Shepsle says it is not a horse race, and the approaches together show the tensions and trade-offs (p. 441).

### Problems (pp. 442–444)
Six problems; the most useful are listed under Exercises below.

## Toy example (ours, not from the text)
Take $B=10Q-Q^2$ ($a=10,b=1$) and $TC=2Q+Q^2$ ($c=2,d=1$).
- Demand-constrained peak: $Q^*=a/2b=10/2=5$. At $Q=5$: $B=50-25=25$, $TC=10+25=35>B$, so the bureau cannot cover costs. The peak is infeasible.
- Cost-constrained: $Q^{**}=(a-c)/(b+d)=8/2=4$. Check: $B=40-16=24$, $TC=8+16=24$, so $B=TC$. Because $B$ rises on $[0,5]$, this is the largest feasible budget: $24$.
- Social optimum: maximize $B-TC=8Q-2Q^2$. The derivative $8-4Q=0$ gives $Q^0=2$. At $Q=2$: $B=16$, $TC=8$, net $=8$.
- At $Q^{**}=4$ the net social gain is $24-24=0$, against $8$ at $Q^0$. The ordering $2\le4\le5$ matches $Q^0\le Q^{**}\le Q^*$. The bureau produces twice the socially optimal output and uses up all the gain.

## Concepts
- [[budget-maximizing-bureaucrat]] (new) — Niskanen's assumed motive: the bureau chief wants as large a budget as the legislature will give; reasons are irrelevant (pp. 409–410).
- [[principal-agent-problem]] — principal hires a specialist agent whose interests and effort are imperfectly controlled; here legislature/coalition and bureau (pp. 423–425).
- [[bilateral-monopoly]] (new) — one buyer (a committee) bargaining with one seller (the bureau), each with information the other may or may not know (p. 419).
- [[organizational-slack]] (new) — $B-TC$, spent on comfort on the job when costs are hidden (p. 416, n. 8).
- [[enacting-coalition]] (new) — House and Senate majorities plus the president that agree on the legislation creating or directing an agency (p. 425).
- [[bureaucratic-drift]] (new) — gap between the politically agreed policy $x$ and the policy implemented by the agency $x'$ (p. 428).
- [[agency-slippage]] (new) — implemented policy departing from the principals' policy, caused by discretion, differing preferences and weak control (p. 433).
- [[bureaucratic-capture]] (new) — drift that pleases key legislators, interest groups and constituencies inside a "policy whirlpool" (pp. 435–436).
- [[coalitional-drift]] (new) — risk that today's enacting coalition is replaced, undoing its deal; insulation reduces it but raises bureaucratic drift (pp. 436–437).
- [[police-patrol-fire-alarm-oversight]] (new) — direct congressional monitoring versus reactive monitoring by affected parties; fire-extinguisher (courts) is Shepsle's addition (pp. 431–432).
- [[veto-player]] — (canon link; not stated in this unit) punishing the agency needs all coalition members to agree (p. 428).

## Canonical instances
- [[niskanen-bureau-model]] — budget maximizer with private costs; $Q^0\le Q^{**}\le Q^*$ (pp. 410–414).
- [[epa-triangle-drift]] — House, Senate, president and EPA ideal points; $x\to x'$ (pp. 426–428).
- [[ftc-1979-weingast-moran]] — test of runaway-agency versus principal-change explanations (pp. 438–440).
- [[kitchen-contractor]] — agent whose work quality the principal cannot observe (p. 423).
- [[case-by-case-procedure]] — a procedural rule that shifts advantage to business over environmental groups (pp. 429–430).

## Bridges (candidates)
- [structural-analogy] Niskanen's bureau with private costs ↔ asymmetric-information monopoly pricing in economics: seller knows costs, buyer announces demand.
- [structural-analogy] McNollgast's triangle $HSP$ ↔ veto players and the winset of the status quo: points in the triangle that no unanimous coalition of principals can improve on (canon link; not stated in this unit).
- [structural-analogy] Bureaucratic drift ↔ principal–agent "shirking" under delegation (hidden action).
- [metaphor] Coalitional drift versus bureaucratic drift ↔ time-inconsistency/commitment problems: insulating a policy makes it durable but also uncontrollable.

## Questions this raises
- Which of the three models best predicts bureau behaviour in settings other than the FTC, and what data would separate them?
- When is "quiet life" better modelled as risk aversion, and what output does it predict once formalized?
- If fire-alarm oversight relies on affected groups, which groups get a voice (as in the case-by-case procedure) and which do not?
- How much insulation is optimal if it trades coalitional drift against bureaucratic drift?

## Exercises worth doing
- Ex. 3 (pp. 442–443) — compute a Niskanian bureau's maximum budget with demand and cost constraints, then add an audit probability and fine — difficulty: medium
- Ex. 2 (p. 442) — assess Niskanen's three strong assumptions and the solutions legislatures use — difficulty: easy
- Ex. 5 (pp. 443–444) — audit/work-or-shirk game: dominant strategies, equilibria, mixing probabilities — difficulty: hard
- Ex. 4 (p. 443) — compare control of legislators by elections with control of bureaucrats by before- and after-the-fact tools — difficulty: medium
- Ex. 1 (p. 442) — apply the principal-agent framework to term limits — difficulty: medium

## Reading notes
- Page labels carry printed numbers; printed = pdf − 11. Source notes say the scan lacks printed pp. 251–252 in Chapter 8, which does not affect this unit.
- Footnote 7 reads "(b +cf)" in the text layer. By the algebra it is $(b+d)$, and I used that.
- The text layer garbles the symbols $Q^0$ ("o0", "Cf", "QO") and "≤" ("s"). Page images were available for pp. 410, 411, 414, 427 and 434 and were checked; the footnote equations on pp. 412–413 rest on the text layer.
- Page images for pp. 442–444 were not provided. The problem 5 payoff table is garbled in the text layer, so its payoffs are not reproduced here.
- Text-layer misspellings (possibly scan errors; page images of pp. 408 and 417 were not available): "Gouernmerit" in footnote 1 (p. 408) and "Tunnessee" in footnote 10 (p. 417).
