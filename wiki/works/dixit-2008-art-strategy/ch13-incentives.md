---
id: dixit-2008-art-strategy/ch13-incentives
work: dixit-2008-art-strategy
unit: 13. Incentives
pages: 355-375
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Incentives (moral hazard and how to pay for effort)

## L0 — One line
When you cannot observe someone's effort, pay them a base amount plus a reward tied to an observable outcome, sized so that working hard is in their own interest while the job still looks attractive.

## L1 — The gist (≤ 120 words)
How do you motivate a worker whose effort you cannot see? This is called moral hazard. The answer is a compromise between a flat wage, which handles incentives poorly, and a pure piece rate, which may make the job too risky to accept. Pay a base plus a bonus tied to an imperfect indicator of effort. The bonus must be large enough to make hard work pay, and the base is set so the worker still accepts the job. Weaker incentives suit noisy outcomes. Career concerns, repeated play, relative-performance comparisons, task structure, intrinsic motivation and several bosses all change the best design. A chess-programmer example gives exact numbers.

**Prerequisites:** expected value (probability-weighted average); percentages; the idea of a participation constraint and of information asymmetry (from the chapter on screening).

## L2 — Key ideas (5–10 bullets)
- **Moral hazard** is a hidden-action problem: effort is unobservable, so pay must rest on an observable, noisy outcome (pp. 357–358).
- A good scheme **mixes** a fixed part, which secures participation (the worker accepts the job), with an outcome-linked part, which secures effort (p. 357). Averages are fixed by alternatives elsewhere; spreads supply the incentive (pp. 360–361).
- The **noisier** the outcome is as a signal of effort, the weaker the incentives should be (pp. 358–359). Linear schemes (pay proportional to outcome) are robust. Quota or bonus schemes can be sharper but are easy to break or manipulate (pp. 359–360).
- **Efficiency wage:** pay enough above the outside option, with firing on detected shirking, deters cheating. In the example the minimum premium is $3,200 over the $48,000 break-even (pp. 363–364).
- **Task structure:** group complementary tasks (effort on one raises the productivity of effort on the other) together and keep substitute tasks (effort on one lowers it) separate (pp. 365–366). More **bosses** weaken aggregate incentives (p. 370).
- **Relative performance** (pay judged against peers) helps when luck is shared across workers (p. 367). Repeated observations help when luck is independent over time (p. 363).
- **Intrinsic motivation** (caring about the job for its own sake) can be crowded out; paying a little may be worse than paying nothing or paying a lot (pp. 368–369).
- In the **Wizard 1.0** example, a $100,000 success bonus and a −$10,000 base reproduces the observable-effort profit of $90,000. Without fines or worker capital, profit falls to $80,000 (pp. 370–372).

## L3 — Walkthrough

### Opening (p. 355)
The authors say socialist systems failed because workers and managers lacked adequate incentives; most importantly, there was no reward for doing a good job rather than a merely adequate one. They cut corners, for example fulfilling quantity quotas while slacking on quality. The Soviet quip was: "They only pretend to pay us, so we only pretend to work." (p. 355) Markets have the profit motive, but individual employees are not fully exposed to competition. Firms must design internal rewards, and two firms in a joint project must share incentives in a contract (p. 355).

### Incentives for effort: the proofreader (pp. 356–358)
- **Setting.** An author hires a student to proofread printer's proofs because his own eyes glaze over (p. 356). The author wants all errors found. He cannot see the student's effort. Even the outcome is visible only later, when some reader reports missed errors, perhaps months or years afterward (p. 356).
- **Why simple pay fails.** A flat sum invites shirking. A pure piece rate is risky for the student: if the typesetter did a perfect job, he works a week and earns nothing, so he may refuse the job (p. 356).
- **Moral hazard.** The author is the uninformed party, but the hidden thing is the student's deliberate choice, so it is not adverse selection (p. 357). Insurers call such behaviour *moral hazard*, as when an insured owner is careless with locks. Game theorists regard responding to incentives as natural and put the onus on the other player to design a better scheme (p. 357).
- **Link to screening.** Incentive payment schemes face the same two restrictions as screening: incentive compatibility and participation. A flat sum does not handle the incentive aspect well. A pure piece rate does not handle the participation aspect well. So use a flat sum plus a bonus per error found (p. 357).
- **Dixit's case.** 600-page book, $600 fixed ($1 per page) plus $1 per error found. The student found 274 errors and took about 70 hours. Average pay was $12.49/hour, i.e. $(600+274)/70$ (added step: $874/70 \approx 12.49$). About 30 missed errors surfaced later. The authors do not claim the scheme was optimal (p. 357).
- **Wider use.** Software designers and copywriters have hard-to-monitor effort, so part of pay is tied to project or company success via stock or options: basic salary plus outcome bonus. Higher-level managers are paid the same way, even though such schemes can be manipulated (pp. 357–358).

*Intuition note.* You can only reward what you can see. A fixed part keeps the worker willing to join, and a variable part makes extra effort pay.

### How to write an incentive contract (pp. 358–362)
**Noise.** If outcome were a perfect, certain function of effort, effort could be controlled perfectly. In practice chance also matters. An insurer's profit depends on hurricanes as well as on effort (p. 358). Rewarding outcomes partly rewards luck. If chance is large, outcome-based incentives are weak and you should not offer them much. If chance is small, stronger and sharper incentives can be used (pp. 358–359).

**Nonlinear schemes.** *Linear* means the payment rises in strict proportion to the outcome, as with pay per error or a percentage commission. A quota bonus is nonlinear (p. 359).
- A quota is powerful if hard effort gives a good chance of meeting it and slacking sharply lowers that chance (p. 359).
- A quota is useless if it is so demanding that the salesman has little chance even with superhuman effort (p. 359).
- Luck during the year can break a well-set quota. After bad luck in the first half, he gives up. After meeting the quota in June, he relaxes, and he could even get customers to postpone orders to next year (pp. 359–360).
- The authors' conclusion: nonlinear schemes must be designed just right and are prone to manipulation. Linear schemes are less finely targeted but more robust to changing circumstances and misuse. Real schemes often combine a percentage commission with a quota bonus and larger bonuses at higher thresholds (p. 360).
- Trip to the Gym No. 9 asks about the incentive in a 6% real-estate commission (p. 360).

*Intuition note.* A sharp threshold gives a strong push only near the threshold. Elsewhere it can give no push at all. A proportional rule gives the same extra pay for each extra unit of outcome.

**Carrots versus sticks.** A scheme has two features: the *average payment*, which must satisfy the participation constraint, and the *spread* between good and bad outcomes, which creates the incentive. A bigger spread means a stronger incentive (p. 360).
- Example with spread 50 and average 100. Carrot: 99 most of the time, 149 with 2% chance of exceptional performance. Stick: 101 most of the time, 51 with 2% chance of exceptionally poor performance (pp. 360–361).
- Check (added step): $0.98\cdot 99+0.02\cdot 149=100$, and $0.98\cdot101+0.02\cdot51=100$. Both have average 100 and spread 50 (p. 361).
- The average is set by what the worker could earn elsewhere. Seeking workers with poor alternatives may bring adverse selection (p. 361).
- Stalin: low pay even for good work and Siberia for bad work, with no outside options. The authors say this could have been a powerful, cheap scheme. It failed because punishment was not tied to effort, since people were denounced almost as easily whether they worked hard or shirked (p. 361).
- CEO pay: it seems that CEOs get large sums if the firm does well, only slightly smaller sums if it does okay, and a golden parachute if it fails. The average seems far above what is needed to take the job, so the participation constraints look "grossly overfulfilled" (p. 361). The authors' explanation is competition: the relevant comparison is another company's guaranteed offer (e.g. $10 million), not driving a cab or playing golf (pp. 361–362). In Europe, where pay is lower, the relevant comparison is other European firms, because many candidates will not move to the US (p. 362).

### The many dimensions of incentive schemes (pp. 362–370)
**Career concerns (pp. 362–363).** Over a multi-year job, future raises and promotions can motivate. This works best for younger employees at lower and middle levels. It works less for people near retirement and little for newcomers who expect to change jobs. Assistant professors are motivated by tenure. The proofreader may be motivated by the professor's future letters of recommendation, which makes immediate cash less important (pp. 362–363).

**Repeated relationships (p. 363).** If luck at different times is independent, then by the law of large numbers average output measures average effort more accurately. That allows more powerful incentives, because a claim of persistent bad luck is less plausible than a single hard-luck story (p. 363).

**Efficiency wages (pp. 363–364).** The numbers:
- Good effort is worth $60,000/year to the employer. The worker's cost of effort is $8,000/year. A dead-end job pays $40,000 (p. 363).
- Shirking is detected with probability 25%. Contract: pay above $40,000 as long as no shirking is found out. If it is found, fire him and tell other employers, so he never earns more than $40,000 again (pp. 363–364).
- At or below $48,000 ($40,000 + $8,000) he would take the job only if planning to shirk. Write salary as $48,000 + X, so he is X better off than the alternative (p. 364).
- Shirking gains $8,000 this year. With probability 0.25 he is found out and loses $X this year and every year after (p. 364).
- At interest rate 10%, an extra $X a year is like a bond of face value $10X. He will not shirk if $8{,}000 < 0.25 \times 10X$, i.e. $X > 8{,}000/2.5 = 3{,}200$ (p. 364).
- Salary $48,000 + $3,200 = $51,200 deters shirking. The *efficiency premium* (excess over the basic outside wage) is $11,200 (p. 364).
- Car-mechanic application: pay a little more than the lowest rate, so the steady extra profit deters cheating. This is a premium for honesty (p. 364).

*Intuition note.* A well-paid job you could lose becomes a hostage. Cheating gains a little once and risks a stream of future extra income, so a high enough premium makes honesty pay.

**Multiple tasks (pp. 365–366).** Tasks are *substitutes* if effort on one lowers the productivity of effort on the other (corn and dairy). They are *complements* if effort on one raises productivity on the other (bees and apples) (p. 365).
- With substitutes, strong incentives on each task hurt the other, so both must be weaker than if each were considered alone. With complements, both can be strong (p. 365).
- Organization design: give each employee, and each division, a set of mutually complementary tasks, and put substitutes in different divisions (p. 365).
- Heathrow example: within one airport the activities are complements, and separate airports are substitutes. The rule says each airport should have one management, with airports competing. The UK did the opposite: BAA owns all three London airports, while functions inside each are split among the BAA, the police and a regulator. The authors cite too little security space and landing fees set too low as symptoms (pp. 365–366).
- Teaching and research: French separation would fit substitutes, and the US combination fits complements. The authors say the comparative success of the two forms is evidence for complements (p. 366).
- They do not know whether the tasks in the Department of Homeland Security are substitutes or complements (p. 366).

**Competition between workers (pp. 366–367).** When workers do similar tasks at the same time, chance is highly correlated across them. Comparing outcomes then gives a good indication of relative effort, so pay can rest on relative performance or on prizes, as for fund managers (pp. 366–367).
- Two proofreaders with overlapping pages: payment based on relative performance on the overlap sharpens incentives. Do not tell either who the other is (collusion) or which pages overlap (care only there) (p. 367).
- The inefficiency of the overlap can be more than offset by better incentives. This is an advantage of dual sourcing (p. 367).
- For the book, Barry paid $2 per typo to the first finder among his Yale students. This led to heavy duplication. The winner, assistant Catherine Pichotta, started at the back of the book (p. 367).

**Motivated workers (pp. 368–369).** Some workers care about the job itself, especially in nonprofits, health care, education and creative tasks. They need fewer or weaker material incentives. Psychologists find that extrinsic monetary incentives can diminish intrinsic motivation (p. 368).
- Gneezy and Rustichini: 50 IQ-test questions; groups paid nothing, 3¢, 30¢ or 90¢ per correct answer. The 30¢ and 90¢ groups got 34 right on average, versus 28 for no bonus. The 3¢ group did worst, with 23 (p. 368).
- Explanation: once money enters it becomes the main motivation, and 3¢ is too little. It may also signal that the task is unimportant. Their conclusion: offer significant financial rewards or none at all (pp. 368–369).

**Hierarchical organizations (p. 369).** Each boss must anticipate strategic behaviour by those below. If a worker's pay depends on the supervisor's quality certification, the supervisor may pass shoddy work to meet his own target. Designing against this generally weakens incentives at those levels (p. 369).

**Multiple owners (pp. 369–370).** One worker may answer to several bosses with misaligned interests. Each can offset the others' incentives, so aggregate incentives weaken (p. 369). In the parents' example, a reward for grades and another for athletics offset each other, because time spent studying cuts time for sport. The total offset is not necessarily complete (p. 370). The authors say mathematical models show overall incentive strength is inversely proportional to the number of bosses, and suggest this may explain difficulty in the UN and WTO (p. 370). If interests are totally opposed, incentives may have no power, as in "No man can serve two masters" (p. 370).

### How to reward work effort: Wizard 1.0 (pp. 370–373)
- **Setup.** Success pays $200,000, failure nothing. High-quality effort gives 80% success. Routine effort gives 60%. Programmers cost $50,000 for routine effort and $70,000 for high effort (p. 370).
- **If effort were observable.** Routine: $0.6\times200{,}000-50{,}000=70{,}000$. High: $0.8\times200{,}000-70{,}000=90{,}000$. Hire the high-effort programmer (p. 371).
- **Problem.** Effort is unobservable. She could take $70,000 and give routine effort, and blame failure on chance (p. 371).
- **Bonus size.** Pay depends on outcome. High effort must raise her expected earnings by $20,000 (from $50,000 to $70,000). Success probability rises by 20 percentage points (0.60 to 0.80), so the bonus is at least $100,000, since $0.2\times100{,}000=20{,}000$ (p. 371).
- **Base pay.** At routine effort the $100,000 bonus is worth $0.6\times100{,}000=60{,}000$, which is $10,000 more than the market requires. So base pay is −$10,000: $90,000 on success and a $10,000 fine on failure (p. 372).
- **Result.** Her average pay is $0.8\times90{,}000+0.2\times(-10{,}000)=70{,}000$. The owner's average profit is $160{,}000-70{,}000=90{,}000$, the same as with observable effort. "The unobservability of effort hasn't made any difference." (p. 372)
- **Equity version.** This is equivalent to selling 50% of the firm to her for $10,000 plus her effort. Only the name differs, though the authors add that the name may matter (p. 372).
- **Constraints.** If fines are illegal or she has no capital, pay $100,000 on success and nothing on failure. Her average is $80,000, and profit falls to $80,000, because revenue stays $160,000. This is $10,000 worse, so now unobservability matters (pp. 372–373).
- **Risk.** A $100,000 gamble may make her value pay below its average, so she must be compensated for bearing risk. The bigger the risk, the bigger the compensation. The authors say the best solution is often a compromise: reduce risk by giving weaker incentives, which motivates less than ideal effort (p. 373).
- **More signals.** Repeated projects by the same expert let you attribute repeated failure to poor effort. Several experts on related projects with correlated outcomes allow relative-performance rewards, i.e. prizes (p. 373).

*Intuition note.* The bonus is the extra pay needed to make high effort worthwhile, divided by how much high effort raises the success chance. The base is then pushed down until the worker is no better off than the market requires. If the base cannot be negative, the owner must overpay.

### Case study: Treat them like royalty (pp. 373–375)
- **Royalties and advances.** Authors typically get about 15% of list price on hardcover and 10% on paperback, plus an advance paid in parts (signing, delivery and acceptance, publication) (pp. 373–374).
- **Effects of the advance.** Holding part back gives an incentive to finish on time. The advance shifts risk to the publisher, who may spread it over many projects. Its size is a credible signal of the publisher's enthusiasm, since a large advance is costly if you do not expect large sales (p. 374).
- **List price conflict.** Royalties are a percentage of total revenue, so the author wants the revenue-maximizing price. The publisher maximizes profit (revenue net of cost) and always wants a higher price than the revenue-maximizing one. Starting from the revenue-maximizing price, going up a little keeps revenue almost constant but reduces sales and thus costs (pp. 374–375). The authors negotiated the list price into their own contract (p. 375).
- Trip to the Gym No. 10 asks how big the wedge is (p. 374). Two more incentive cases follow in the next chapter (p. 375).

## Toy example (ours, not from the text)
A shop owner earns $100 if a project succeeds and $0 if it fails. A freelancer can do routine work (50% success) or careful work (90% success). The market wage is $10 for routine work and $20 for careful work. The owner cannot see effort.

1. Bonus: careful work must raise expected pay by $10 (the $20 − $10 gap). The success chance rises by $0.9-0.5=0.4$. So $0.4B=10$, hence $B=25$.
2. Base: at routine effort the bonus is worth $0.5\times25=12.5$, which is $2.5 above the $10 market wage. So the base is $-2.5$. Pay is $22.5$ on success and $-2.5$ on failure.
3. Check the incentive. Careful: $0.9\times22.5+0.1\times(-2.5)=20.25-0.25=20$. Routine: $0.5\times22.5+0.5\times(-2.5)=11.25-1.25=10$. The $10 difference exactly covers the effort cost, so she is just willing to work carefully.
4. Owner's profit: $0.9\times100-20=70$, the same as with observable effort ($90-20$).
5. If fines are impossible, pay $25$ on success and $0$ on failure. Careful effort gives average pay $0.9\times25=22.5$, so profit is $90-22.5=67.5$. The loss of $2.5$ equals the missing negative base.

## Concepts
- [[moral-hazard]] (new) — hidden action: a party's effort or care cannot be observed, so it responds to incentives (p. 357)
- [[adverse-selection]] (new) — a hidden innate characteristic rather than a deliberate choice; the chapter says moral hazard is not this problem (p. 357)
- [[incentive-compatibility]] — the scheme must give the worker enough incentive to put in the desired effort; the text names it together with participation without defining it (p. 357)
- [[participation-constraint]] (new) — pay must beat what the worker could get elsewhere (pp. 357, 360–361)
- [[linear-vs-nonlinear-incentive-scheme]] (new) — pay proportional to outcome versus threshold or quota bonus (p. 359)
- [[efficiency-wage]] (new) — wage above the outside option, paid so long as no shirking is found, so that cheating is not worth it (p. 364)
- [[relative-performance-pay]] (new) — pay based on comparison with peers, useful when luck is shared (p. 367)
- [[task-substitutes-and-complements]] (new) — whether effort on one task lowers or raises the productivity of effort on another (p. 365)
- [[crowding-out-of-intrinsic-motivation]] (new) — extrinsic money can diminish intrinsic motivation (p. 368)
- [[shadow-of-the-future]] — in the efficiency wage and career concerns, future income or rewards make current good behaviour pay (pp. 362–364)

## Canonical instances
- [[proofreader-contract]] — fixed fee plus $1 per error found; mixture of flat and piece rate (p. 357)
- [[efficiency-wage-example]] — $51,200 salary, $3,200 minimum premium over $48,000 (p. 364)
- [[wizard-1-0]] — chess-game programmer; $100,000 bonus with −$10,000 base (pp. 370–372)
- [[gneezy-rustichini-iq-experiment]] — 3¢ per answer performed worst; no pay or large pay did better (p. 368)
- [[heathrow-airport-organization]] — complementary tasks split, substitute airports merged under one owner (p. 366)
- [[ceo-pay-participation-constraint]] — CEO pay set by competition for CEOs, not by the cab-driving alternative (pp. 361–362)
- [[soviet-incentive-failure]] — punishment not tied to effort (p. 361)

## Bridges (candidates)
- [structural-analogy] Moral hazard contract ↔ mechanism design: incentive-compatibility and participation constraints appear in both; the chapter itself draws the parallel to screening (p. 357).
- [structural-analogy] Efficiency wage ↔ repeated game: a threatened loss of a future stream of rents deters one-time cheating, as in cooperation sustained by a long shadow of the future (p. 364).
- [structural-analogy] Relative-performance pay ↔ statistics: comparing with peers removes the common luck shock, like subtracting a shared noise term (p. 367).
- [structural-analogy] Repeated observations make average output a better measure of effort ↔ sample means: averaging independent noise improves precision (p. 363).

## Questions this raises
- How does the best bonus change if the worker dislikes risk, and how much weaker should incentives become? The chapter only says a compromise is common (p. 373).
- How can a firm tell whether two tasks are substitutes or complements? The authors use institutions as indirect evidence (p. 366).
- Do relative-performance schemes invite collusion or sabotage among workers? The text only warns against revealing identities in the proofreader case (p. 367).
- What are the "mathematical models" behind the claim that incentive strength is inversely proportional to the number of bosses? The text does not give them (p. 370).

## Exercises worth doing
- Trip to the Gym No. 9 (p. 360) — the text's hint says an extra $20,000 in price does not bring the agent $1,200 under a 6% commission; design a better scheme and discuss its problems — difficulty: medium
- Trip to the Gym No. 10 (p. 374) — estimate the author–publisher gap in preferred price; uses revenue versus profit maximization (pp. 374–375) — difficulty: medium
- Case study "Treat them like royalty" (pp. 373–375) — find where authors' and publishers' interests diverge and whether a better payment scheme exists — difficulty: easy

## Reading notes
- Printed page numbers equal pdf numbers (355–375).
- The table on p. 371 (profit comparison) is not in the text layer. Page images were not supplied with this unit. The figures I give are from the surrounding prose and I recomputed them.
- Footnote texts for the asterisks on pp. 357, 364 and 372, the dagger on p. 357, and note numbers 1–3 (pp. 358, 368, 370), are not included in the pages given.
- The text layer reads "Stanstead" (p. 366).
- The text speaks of "the authors" (e.g. p. 366); Avinash (Dixit) appears only in passing on p. 357 and Barry on p. 367.
- The "Bay Bridge" and "But One Life to Lay Down for Your Country" cases (p. 375) are in the next chapter and not covered here.
