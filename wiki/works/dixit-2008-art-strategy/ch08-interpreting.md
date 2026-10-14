---
id: dixit-2008-art-strategy/ch08-interpreting
work: dixit-2008-art-strategy
unit: "8. Interpreting and Manipulating Information"
pages: 223-253
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Interpreting and Manipulating Information

## L0 — One line
When some players know more than others, their words alone cannot be trusted when interests differ, so players use actions whose cost differs by type (signals and screens) to reveal, conceal or elicit private information.

## L1 — The gist (≤ 120 words)
How can you trust what interested parties tell you, and how can you make your own claims believable? The chapter's answer is that actions speak louder than words. An action is a credible signal only if it costs less, or pays more, for the type that has the good information. Informed players signal, jam signals, or even countersignal. Uninformed players screen by offering choices that make each type pick differently. Examples: warranties, MBAs, pass/fail grades, poker bets, airline fare classes. Mixed strategies mean actions reveal information only partly, and Bayes' Rule measures how much. This matters because your own actions are often being interpreted.

**Prerequisites:** basic probability (conditional probability, expected value); the idea of mixed strategies from earlier chapters; simple profit arithmetic.

## L2 — Key ideas
- The more someone's interests conflict with yours, the less you can trust their statements. With totally opposed interests, the right response is to ignore the statement, neither believing it nor assuming its opposite (p. 224, p. 245).
- General principle: "Actions (including tattoos) speak louder than words." Watch what others do, and, knowing they will read your actions the same way, shape your own actions for the information they carry (p. 226).
- Credible signal: the action is optimal if, but only if, the player has the specific information. This works through a cost-difference property, as with warranties and MBAs (pp. 229, 235).
- Screening is the less-informed side's version: set up a situation where each type chooses differently. Signaling is initiated by the informed side, and the same principle underlies both (pp. 226–227, 229, 237).
- Failing to signal also sends a signal, and often bad news (pass/fail, coinvesting). Sometimes the strongest signal is not signaling (countersignaling) (pp. 239–241).
- Signal-jamming equilibria can be pooling, separating or semi-separating. When types mix, Bayes' Rule converts an observed action into updated probabilities (pp. 243–247).
- Price discrimination by versioning is screening. Incentive-compatibility and participation constraints cost the seller some profit (pp. 247–252).

## L3 — Walkthrough

### The Marrying Kind? / Tell It Like It Is? (pp. 223–225)
- **Sue's story.** Sue wanted a credible signal (a cousin of a commitment device, but weaker) that her partner was serious. A public demonstration was impossible because his children would find out. She asked for a small, hidden tattoo of her name. It is cheap if he is in for the long run and embarrassing if not. He balked and she left (pp. 223–224).
- **Interests and truth.** Communication can be trusted when interests are aligned (the waiter and your steak order). Trust falls as conflict rises (recommended entrée or wine) (p. 224).
- **Hardy's insight**, as told by C. P. Snow: if the Archbishop says he does not believe in God, "one can take it he means what he says," which the authors cite as an example of strategic insight about speakers' interests (p. 224).
- **Opposed interests.** A penalty kicker who announces which way he will shoot should not be believed. The goalie also should not assume "left," because the kicker may be lying by telling the truth. The only rational reaction is to ignore the assertion and play the equilibrium of the actual game (p. 224).

### King Solomon's Dilemma (p. 225)
- Solomon proposed cutting the baby in two. The true mother begged that the baby be given to the other woman, and the other woman said "cut him." Solomon gave the baby to the first (p. 225).
- The authors say the device would not have worked if the false claimant had understood it. She should simply have repeated what the first woman said, so the king could not tell them apart. Solomon was "more lucky than wise." A better design is promised in chapter 14 (p. 225).

### Devices for Manipulating Information (pp. 226–228)
- Some players know more than others about something affecting everyone's payoffs. Those with extra information may want to conceal it (the false claimant) or reveal it (the true mother). Less-informed players want to elicit it (p. 226).
- **Signaling:** choosing actions whose information leakage is favourable to you. **Signal jamming:** reducing unfavourable leakage, typically by mimicking behaviour appropriate to other circumstances. **Screening:** setting up a situation where the other player takes one action if the information is of one kind and another if of another kind, so the action reveals it. Sue's tattoo request was a screen (pp. 226–227).
- Poker: the optimal mix of bids differs by hand strength, so bids carry some information (p. 227).
- An effective signal "should be incapable of being mimicked by a rational liar": it must be unprofitable when the truth differs from what you want to convey (p. 227).
- Examples:
  - A law firm's lavish hospitality for interns signals that it values them; what matters is the price, not the food.
  - A good degree signals general ability, which employers cannot easily observe (p. 227).
- **Rat race:** if the more able get a little more education and the less able find it profitable to imitate, the able must get more. True abilities are unchanged and the investment is wasteful. The authors say individuals cannot fix this and a public-policy solution is needed (pp. 227–228).

> *Intuition note.* A signal is believable only when a liar would find it too costly or unprofitable to copy. If everyone can send it cheaply, it carries no information.

### Is the Quality Guaranteed? (pp. 228–230)
- A used-car warranty is relatively costless for the seller of a good car and likely a loss for the seller of a poor car, even after the higher price it brings. So it implies "I know the quality is good enough that I can afford this" (p. 228).
- **Definition:** a signal is an action meant to convey private information. To be a credible carrier of a specific item of information, the action must be optimal for the player if, but only if, he has that information (p. 229).
- **Numbers:** expected repair cost $500 (good car), $2,000 (poor car), warranty price difference $800. A seller offering the warranty must know his car is good ($800 > $500, but $800 < $2,000) (p. 229).
- **Screening version:** the buyer can offer $800 extra on condition that the seller gives a warranty. It pays the seller only if his car is good. Any warranty price between $500 and $2,000 separates the types, so the parties can bargain in that range. Signaling and screening can reveal information similarly, although the resulting equilibria can differ technically. Which is used may depend on historical, cultural or institutional context (p. 229).
- **Not credible:** an offer to let you have the car inspected. If a flaw is found and you walk away, the owner is no worse off whatever the car's condition, so a bad-car owner can make the same offer (pp. 229–230).
- The warranty must itself be enforceable. This is harder with a private seller (may move, lack money, or be costly to sue) than with a dealership that has a reputation. Hyundai in 1999 signaled its improved quality with a 10-year, 100,000-mile power-train warranty (p. 230).

### A Little History (pp. 230–233)
- **Akerlof's lemons.** Lemons: owner will sell at $1,000, buyers pay $1,500. Peaches: owner sells at $3,000, buyers pay $4,000. If quality were observable, all cars would trade (p. 230).
- If sellers know quality and buyers know only that half are lemons and half peaches, the buyers' maximum price is given by a formula that is missing in the text. (added step) By the obvious computation it is $\tfrac12(1{,}500)+\tfrac12(4{,}000)=\$2{,}750$, below the $3{,}000$ peach owners need. The text says peach owners will not sell at this price, so only lemons are offered, buyers offer at most $1,500, and the market for peaches collapses (p. 231).
- Dixit and fellow students noticed that most of them drove good used cars. Real markets cope through mechanical knowledge, friends' inspections, networks, and owners who must sell (moving, growing families) (p. 231).
- **Spence** supplied the next breakthrough: strategic actions can communicate information, and the key property is the difference in payoffs from an action across players with different information (pp. 231–232).
- **Screening** evolved from Mirrlees and Vickrey and was stated most clearly by Rothschild and Stiglitz on insurance. Different plans (deductibles, coinsurance) are chosen differently by low-risk types (smaller premium, more risk borne) and high-risk types, so the choice reveals type (p. 232).
- **Adverse selection.** A policy charging 5 cents per dollar of coverage is especially attractive to people with mortality above 5 percent. Raising the price can worsen the pool: the Groucho Marx effect (anyone willing to buy at those prices is not someone you would want to insure). The name adverse selection comes from this and is now the name of the whole research area (p. 232).
- **Positive selection (Capital One).** Customer types: maxpayers (pay in full), revolvers (borrow and repay), deadbeats (borrow and default). The issuer loses on deadbeats and also on maxpayers, and revolvers are the most profitable. A balance-transfer offer attracts those with large balances who plan to repay and holds little appeal for the other two types. Capital One may not be able to identify types, but the offer screens: "any customer who accepts your offer is one you want to take" (p. 233).

> *Intuition note.* If a deal looks best to the customers you least want, good ones leave and the market can unravel (adverse selection). If it looks best to the ones you most want, the offer filters for you (positive selection).

### Screening and Signaling (pp. 234–243)
- **MBA as a screen.** You want managers with natural talent; candidates know their own talent, you do not. An MBA costs about $200,000 (tuition plus foregone salary). Non-MBA graduates earn $50,000. Amortized over five years, the cost is $40,000 per year, so you must pay at least $90,000 (p. 234).
- It works only if the talented find the MBA easier or cheaper. Assume the talented surely pass and the untalented pass with probability 50% (p. 234).
- Offer $100,000 to MBAs. The talented go. For the untalented, a 50% chance of doubling pay yields only $25,000 extra on average, which cannot repay the cost over five years, so they stay away (pp. 234–235). The MBA then sorts the pool, and works because its cost is lower for those you want to attract (p. 235).
- Cost of the screen: you pay the talented over $90,000 instead of just over $50,000, an extra $40,000 a year for five years. The untalented cause this by existing: a negative externality (spillover cost to others), here an "informational externality" (p. 235).
- **Is it worth it?** Suppose 25% of graduates lack talent and each can lose $1 million before being found out. Random hiring then costs $250,000 per hire on average, against $200,000 ($40,000 × 5) for screening by MBA. The authors say the true talented share is probably much smaller and the potential loss much larger, which strengthens the case (pp. 235–236).
- **Box: a reason to get an MBA.** An employer may fear a young woman will leave the labor force to have children. An MBA signals intent to work for several years. If she planned to drop out within a year, the two years of MBA would not make sense, as recovering the cost likely takes at least five years (p. 236).
- **Cheaper alternatives:** a probationary period, backloaded or performance-related pay (the talented accept, the rest prefer a sure $50,000), or luring away proven managers. Competition raises the talented's pay above the minimum, but in the example salaries cannot rise above $130,000. Above that the untalented would also find the MBA worth trying and the pool would be "contaminated" (pp. 236–237). (added step) At $130,000: $0.5 \times 130{,}000 + 0.5 \times 50{,}000 = 90{,}000$, exactly the $50{,}000+40{,}000$ the untalented need.
- **Signaling version:** a candidate with an MBA can offer to work for the firm for more than $75,000 a year. The authors say it is attractive to the firm so long as the facts about business schools' ability to discriminate talent are clear. Screening and signaling differ in who initiates, but the same principle underlies both (p. 237).

> *Intuition note.* The MBA does not need to teach anything for the screen to work. It only needs to be cheaper for the talented than for the untalented. The firm pays for the screen through higher wages.

- **Signaling via bureaucracy (Workers' Compensation).** Claimants and doctors know more than administrators, and an estimate says 20% or more of claims involve cheating (pp. 237–238). Surveillance is costly. Long forms and waits screen out those who can earn good money, while those truly unable to work can spare the time. The authors say bureaucratic delay "may sometimes" be a valuable response to information problems. In-kind benefits (a wheelchair instead of cash) work similarly because a non-needy recipient gains little from reselling (p. 238).
- **Signaling by not signaling.** Holmes's dog that did not bark: no signal conveys information, usually bad news. The pass/fail example runs as follows (pp. 238–239):
  - Students think a P equals an average passing grade (at least a B+).
  - The top students take letter grades to stand out, so the pass/fail pool loses its upper end.
  - Then the next group leaves, and so on.
  - Eventually strategic readers interpret a P as C or worse (p. 239).
- John, the deal-maker, was allowed to coinvest in the sale of his company to reassure the buyer. The buyer saw that not coinvesting would be read as a bad sign, so the option became a requirement (pp. 239–240).
- **Countersignaling (Feltovich, Harbaugh, To).** Examples: the old rich scorn displays of wealth, the best students do not answer trivial questions, and the well educated scribble illegibly. Sometimes the best way to signal type is not to signal (pp. 240–241).
  - *Prenup model:* three types of mate: gold digger, question mark, true love. The partner can distinguish true loves from gold diggers but is confused about question marks (p. 241).
  - If question marks sign and the others do not, a signer is read as a question mark. Not signing then identifies gold diggers or true loves, whom the partner can tell apart. So the true love refuses to sign (p. 241).
  - If question marks also stop signing, whether that pays depends on whether they would be mistaken for gold diggers or for true loves. If they are more likely seen as gold diggers, not signing is a bad idea (p. 241).
- The very fact that someone is signaling is a signal that they are trying to differentiate themselves from some other type that can't afford the same signal. Nash and the mathematicians: Fagi Levinson says mediocre mathematicians had to toe the line and good ones could do anything (p. 241).
- **Voicemail data.** Across twenty-six University of California and California State University "systems" (count as printed), under 4% of economists at schools with a Ph.D. program used a title on voicemail, against 27% at schools without one. All had Ph.D.s (pp. 241–242).
- **Quiz: "A Trip to the Bar."** On a first date, find credible signals of your quality and screens for your date. The authors give no answer because it depends on the reader's situation (p. 242).

> *Intuition note.* Signals sort people only relative to what the audience can already tell. A top type who is already recognised can skip the signal. A middle type has reason to signal to avoid being taken for the bottom type.

- **Signal jamming (clean used car).** A clean car is a weak signal because cleaning costs a careless owner no more than a careful one (pp. 242–243). Small cost differences may exist (pride, time). Whether they suffice depends on the proportions of types (p. 243).
- *Few careless owners:* a clean car is a favourable sign, so even careless owners clean it. All types do the same and the action is uninformative: a **pooling equilibrium**. *Separating equilibrium:* one type acts and the other does not, so the action identifies type (p. 243).
- *Many careless owners:* if everyone cleaned, a clean car would not impress, so careless owners would not bother. No pooling. But if careless owners did not clean, one who did would be taken for careful, so a single deviation pays. No separating. What happens is a mixed strategy: careless owners clean with positive probability below one (p. 243).
- Buyers infer the probability that a clean car's owner is careful (using Bayes' Rule). Their willingness to pay makes careless owners indifferent between cleaning and not. This is **semi-separating**. The authors say the calculation gets "somewhat intricate" (pp. 243–244).

### Bodyguard of Lies (pp. 244–247)
- Churchill: in wartime, truth should always be "attended by a bodyguard of lies" (p. 244). The Minsk/Pinsk story: one businessman says he is going to Minsk; the asker accuses him of saying so to make him think Pinsk, but adds that he knows the other really is going to Minsk, so why is he lying? (p. 244).
- **Marwan.** Marwan, son-in-law of Egypt's president, offered his services to Israel's Mossad. In April 1973 he sent the code "Radish" (war imminent) and Israel mobilised in what turned out to be a false alarm. On October 5 he sent it again. The head of military intelligence thought him a double agent and took the message as evidence that war was not imminent. The attack came next day. Whether Marwan was a spy or double agent remains uncertain (pp. 244–245).
- With mixed strategies you cannot fool the opposition every time. When talking to someone who wants to mislead you, it may be best to ignore what he says rather than accept it or infer the opposite. But his actions still carry some evidence, because the right mixing proportions depend on his payoffs (p. 245).
- **Poker.** A "tight" player who never bluffs seldom wins big. A "loose" player who bluffs too much is always called. The best strategy mixes the two (pp. 245–246).
- **Setup.** The rival, with a good hand, raises 2/3 and calls 1/3 of the time. With a poor hand, he folds 2/3 and raises 1/3 (never calls). Prior: good and poor hands equally likely. (The probability table is missing in the text; this is read from the text on p. 246. The cells are chances, not payoffs.) Fold means a poor hand, call means a good hand (p. 246).
- **Bayes' Rule.** The chance of a good hand given bid X equals the chance of both a good hand and bid X, divided by the chance of ever bidding X (p. 246).
- **Raise:** $P(\text{good and raise}) = \tfrac12\cdot\tfrac23 = \tfrac13$. $P(\text{bad and raise}) = \tfrac12\cdot\tfrac13 = \tfrac16$. Total $P(\text{raise}) = \tfrac13+\tfrac16=\tfrac12$. Hence $P(\text{good}\mid\text{raise}) = \dfrac{1/3}{1/2} = \tfrac23$ (p. 247). The raise raises the chance of a good hand from 1/2 to 2/3; the odds are 2:1 (p. 246).

> *Intuition note.* Bluffing makes a raise only a partial clue. You cannot be sure he is strong, but the raise is still more likely to come from a strong hand than a weak one. Bayes' Rule just counts the share of all raises that come from strong hands.

### Price Discrimination by Screening (pp. 247–252)
- Customers differ in willingness to pay. Sellers do not know which is which and want to avoid resale. They offer versions priced differently so that customers self-select, revealing willingness to pay (p. 247).
- **Examples:**
  - *Hardcover then paperback:* costs differ little, and the price difference screens the impatient (p. 248).
  - *Software "lite" versions:* often made by disabling features, so slightly costlier to produce but cheaper to buy (p. 248).
  - *IBM laser printer:* the E version, 5 pages per minute, was made slower by a firmware chip. The fast version, 10 pages per minute, cost $200 more (p. 248).
  - *Sharp DVD players:* a hidden PAL-to-NTSC function that users could restore (p. 249).
- **Pie-In-The-Sky (PITS)**, Podunk to South Succotash. 30% business travelers, 70% tourists; figures are per 100 customers. Reservation prices (max willingness to pay) and costs (table missing in the text; values are those given on p. 250):

| | Business | Tourist | Cost |
|---|---|---|---|
| First class | $300 | $175 | $150 |
| Economy | $225 | $140 | $100 |

- **Perfect price discrimination** (types known, no resale or legal limits). Businessperson: first class profit $300 − 150 = 150, economy $225 − 100 = 125, so first class. Tourist: first class $175 − 150 = 25, economy $140 − 100 = 40, so economy. Profit:
$$(140-100)\times 70+(300-150)\times 30 = 2800+4500 = 7300.$$ (p. 250)
- **Screening (types unknown).** Business travelers could take economy and keep surplus $225 − 140 = 85. At $300 first class they would defect. So first class can cost at most $300 − 85 = $215 (the authors ignore the trivial difference of $214). Profit:
$$(140-100)\times 70+(215-150)\times 30 = 40\times 70+65\times 30 = 2800+1950 = 4750.$$ (pp. 250–251)
- The loss from indirect discrimination is $7300 − 4750 = 2550 = 85 \times 30$ (p. 251).
- **Incentive compatibility constraint:** the requirement that the intended type not defect to the choice meant for another type. **Participation constraint:** the requirement that a type remains willing to buy at all (p. 251).
- PITS could charge business travelers more than $215 without inducing their defection only by raising the economy fare. At first class $240 and economy $165, business surplus is $300 − 240 = 60 and $225 − 165 = 60, so they are just willing to take first class (p. 251). But economy at $140 is already the tourists' limit; $141 would lose them (p. 251).
- The authors assert (without proof) that $215/$140 is the most profitable for PITS, being squeezed between the tourists' participation constraint and the business travelers' incentive compatibility constraint (p. 252).
- **If 50% were business travelers:** screening yields $(140-100)\times 50+(215-150)\times 50 = 2000+3250 = 5250$, but serving only business travelers in first class at $300 yields $(300-150)\times 50 = 7500$. With few low-willingness customers, it may be better not to serve them (p. 252).
- The basic idea in all such schemes is the interplay of incentive compatibility and participation (p. 252).

> *Intuition note.* To keep high-paying customers from taking the cheap version, the seller must leave them at least as much surplus from the expensive version as the cheap one gives. The profit given up is the surplus the buyers keep, here $85 per business traveler.

### Case Study: Going Undercover (p. 253)
- Tanya, an anthropologist studying London witches, was welcomed because the witches took her statement that she was an anthropologist as a clever cover story. Their meetings are held nude. Why? (p. 253)
- **Discussion:** any outsider group worries that members may be observers. Nudity is cheap for a true believer and costly for a skeptic, so it screens. Gang initiation rites (tattoos, crimes) work similarly, being cheap for the sincere and costly for an undercover cop (p. 253).

## Toy example (ours, not from the text)
A tutoring firm wants to hire "serious" students as helpers, and it cannot observe seriousness. Offering a prize for completing a hard course screens them as follows (all numbers are made up).
- Type S (serious): course costs 6 units of effort. Type C (casual): costs 14 units. Everyone can instead earn 10 units elsewhere. The firm pays $W$ units to course finishers.
- S takes it if $W-6 \ge 10$, i.e. $W\ge 16$. C declines if $W-14<10$, i.e. $W<24$.
- So any $W$ with $16\le W<24$ separates. Try $W=20$: S nets $20-6=14>10$ and takes it. C nets $20-14=6<10$ and does not. A finisher is serious.
- Try $W=30$: C nets $30-14=16>10$, so both types finish and the signal is useless (pooling).
- If costs were equal (6 for both), $W=16$ makes both take it, so no sorting. The cost difference (6 vs 14) is what does the work, as in the MBA example.

## Concepts
- [[signaling]] — informed player takes an action to credibly reveal private information; credible only if optimal if, but only if, the information holds (pp. 226, 229)
- [[screening]] (new) — less-informed player sets up a choice so that each type's action reveals its type (pp. 226–227)
- [[signal-jamming]] (new) — acting to reduce unfavourable leakage, typically by mimicking another type's behaviour (p. 226)
- [[adverse-selection]] (new) — a deal selectively attracts the worst types (insurance, lemons) (p. 232)
- [[pooling-vs-separating-equilibrium]] (new) — all types act alike and the action is uninformative, versus types act differently and are revealed; "semi-separating" means a mixture with partial information (p. 243)
- [[countersignaling]] (new) — a high type avoids the signal that a middle type needs, to be distinguished from that middle type (pp. 240–241)
- [[bayes-rule]] (new) — updating the probability of a type after seeing an action: joint chance divided by the chance of the action (p. 246)
- [[mixed-strategy]] — randomizing so that actions reveal information only partly (p. 245)
- [[incentive-compatibility-constraint]] (new) — the screener's constraint that each type prefers the option designed for it, so that no type defects (p. 251)
- [[participation-constraint]] (new) — a type must still be willing to buy (p. 251)
- [[price-discrimination]] (new) — selling versions at different prices so that buyers self-select by willingness to pay (p. 247)
- [[credible-commitment]] — related; Sue wants something weaker, a credible signal (p. 223)

## Canonical instances
- [[sue-tattoo]] — a hidden tattoo as a screen for commitment (pp. 223, 227)
- [[solomon-dilemma]] — the baby test works only because the false claimant erred (p. 225)
- [[used-car-warranty]] — warranty as signal and screen via a repair-cost difference (p. 229)
- [[akerlof-lemons]] — adverse selection collapses the market for peaches (p. 231)
- [[capital-one-balance-transfer]] — positive selection (p. 233)
- [[mba-screening]] — an MBA works because it is cheaper for the talented (p. 234)
- [[pass-fail-unraveling]] — not signaling is read as bad news (p. 239)
- [[poker-bayes-raise]] — P(good | raise) = 2/3 (p. 247)
- [[pits-airline-pricing]] — first class vs economy; $7,300 vs $4,750 (pp. 249–251)
- [[witch-nudity]] — nudity screens believers from observers (p. 253)

## Bridges (candidates)
- [same-math] Bayes' Rule in the poker example ↔ probability/statistics: posterior = joint probability ÷ marginal — the same formula applied to a bid.
- [structural-analogy] Incentive-compatibility and participation constraints in PITS ↔ mechanism design: the designer chooses menus so each type self-selects and still participates.
- [structural-analogy] Adverse selection in insurance and used cars ↔ selection bias in data: the sample that accepts an offer is not representative of the population.
- [metaphor] Costly signals (tattoo, MBA, warranty) ↔ biology: costly displays that cheaper types cannot afford to copy.
- [structural-analogy] Pass/fail unraveling ↔ iterated elimination of dominated strategies: each round removes the top of the pool.

## Questions this raises
- When does a small cost difference suffice for a separating equilibrium? The text only says it depends on type proportions and leads to a semi-separating mix.
- How should a screener choose among several screens, and how do competing firms change the optimum?
- Could Solomon have designed a better test? The authors defer this to chapter 14.
- How can a rat race of signaling be limited when no individual can stop it?

## Exercises worth doing
- Trip to the Gym No. 5 (p. 251) — check the business travelers' participation constraint and the tourists' incentive-compatibility constraint at $215/$140 — difficulty: easy
- A Trip to the Bar (p. 242) — design credible signals and screens for a first date; self-graded — difficulty: medium

## Reading notes
- Printed page = pdf page (no offset).
- Page images were available for pdf 247, 250 and 252 only. The text layer is missing several displayed items: the Akerlof maximum-price formula (p. 231, blank), the poker probability table (p. 246) and the PITS table (p. 249). I rebuilt them from the surrounding prose and labelled them as such (the $2,750 is my added step).
- Asterisk footnotes (pp. 227, 230, 231, 237, 240, 241, 253) and numbered endnotes have no text in this unit.
- The "twenty-six ... systems" voicemail count is reproduced as printed (p. 242). The MBA and used-car passages have minor typos ("manger," p. 237; "warrantees," p. 230); none affect the results.
