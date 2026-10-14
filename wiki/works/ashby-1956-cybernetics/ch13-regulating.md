---
id: ashby-1956-cybernetics/ch13-regulating
work: ashby-1956-cybernetics
unit: "13 Regulating the Very Large System"
pages: 244–264
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Regulating the Very Large System

## L0 — One line
In a very large system the difficulty of regulation usually lies in the variety of the disturbances, not in size, so finding a constraint (a restriction on which disturbances occur) can make regulation possible, and making a regulator is itself a measurable act of selection.

## L1 — The gist (≤ 120 words)
How can a regulator cope with a very large system, and where does a regulator come from? Size is usually not the real difficulty; the variety (count of distinguishable states) of the disturbances is. If the regulator's capacity is fixed, finding a constraint (a restriction on which disturbances occur) may turn "impossible" into "possible". Disturbances that repeat show such a constraint. Making a machine is selection, measurable in bits. Selecting by groups (halving the possibilities) can be vastly faster than item-by-item search, and the fast method can be used if the machine is reducible (built of separately settable parts). A regulator chosen from general mechanisms arises only by natural selection or by another regulator's making.

**Prerequisites:** variety and the law of Requisite Variety (earlier chapters); logarithms to base 2 (bits); what a "machine" with states, inputs and a transformation table is; basic counting of combinations.

## L2 — Key ideas
- **Size is usually not the real difficulty.** Size tends to be correlated with the variety in the disturbances D; when the two are separated, size is usually found irrelevant in itself (pp. 244–245).
- **Fixed capacity means a hard limit.** If the regulator R is much smaller than the system T and its channel capacity is fixed, the law of Requisite Variety bounds the regulation achievable. One should aim near that maximum, as Fisher and Shannon taught for statistics and channels (p. 245).
- **Constraint is the hope.** A *constraint* is a dependence among the components of D, so that D's real variety is below the first estimate. If R's capacity is fixed, discovering it is the only way to make "impossible" regulation possible (pp. 246–247).
- **Repetition gives a constraint.** Most regulations repeat. A year's disturbances form a "Grand Disturbance", a long vector (ordered list) of ordinary disturbances. Its record together with the responses defines a machine, so the Grand Response can come from a machine with input (pp. 247–251).
- **Design is selection and communication.** "Designing" a machine means picking one from a set. This is equivalent to fixing an input at a permanent value, and it is measured in the same units as variety (pp. 252–256).
- **Selection adds up at most.** Selection done in stages cannot exceed the sum of the stage selections (in logarithms). It can be supplemented by other selectors, including chance (pp. 257–259).
- **Selecting by groups is fast.** In "successive dichotomies" each step chooses between two groups, not single items. The unique-atom example takes just over four minutes against astronomically many centuries item by item (pp. 260–261).
- **Reducibility enables the fast method.** If a machine is reducible (its sub-systems have separate inputs), its parts can be selected one after another. Reducibility is extremely common in terrestrial systems (p. 262).
- **A regulator needs a regulator, or natural selection.** Making a good regulator is itself regulation. A regulator made by another regulator need not be bounded by the maker's capacity (pp. 262–264).

## L3 — Walkthrough

### 13/1–13/2. Regulation in the very large system (pp. 244–245)
- Biologists, economists, sociologists and psychotherapists face systems with almost uncountably many parts, such as an ecosystem with climate, soil, hosts, predators and competitors. At first sight these look so unlike the simple mechanisms of earlier chapters that one may wonder whether the earlier results are inapplicable (p. 244).
- Ashby says this is not so. Many earlier propositions are stated so that the size of the system is irrelevant. Some mention the number of states or variables, but remain true whatever the number (p. 244).
- Largeness in itself is not the source of difficulty. It is so regarded partly because it is obvious and partly because variations in size tend to be correlated with variations in the real source, the variety in the disturbances D (p. 244).
- Why size and variety in D go together: (i) if T has many parts and the initial state of any part is uncertain, that variety is allocated to D (S.11/19). (ii) If parts are not isolated, each part's input adds variety to D. More parts then mean more components in D, and, if the components have some independence, more variety. Ashby adds that there may be other reasons too (p. 245).
- When the effects of size are separated from those on D's variety, the former will usually be found irrelevant in itself, and what matters is the latter (p. 245).
- When T is very large and R much smaller (a common case in biology), the law of Requisite Variety is likely to play a dominating part. If R's channel capacity is fixed, the law places an absolute limit on the regulation R can achieve, however R is rearranged inside and however great the opportunity in T (p. 245).
- The ecologist, if his capacity is unchangeable, may at best achieve a fraction of what he would like. He may dispose that fraction in various ways (outbreaks rather than extensions; virus rather than bacillary), but the quantity of control stays bounded. The economist may have to decide which aspect to devote his powers to, and the psychotherapist which symptoms to neglect and which to control (p. 245).
- Analogy: Fisher showed that any extraction of information from data has a maximum. Shannon showed the same for channels. The law of Requisite Variety likewise tells the would-be regulator to get near his maximum, since beyond it he cannot go. So the very large system should be approached without extravagant ideas of what is achievable (p. 245).

*Intuition note.* A big system is hard mainly because it throws many different disturbances at you, not because it has many parts. A small regulator facing many disturbance types can handle only so much, so choose what to handle.

### 13/3. The boundary between D and T (p. 246)
- In a very large system the boundary between D (source of disturbances) and T (system that yields the outcome) may be vague. It can often be drawn in several equally satisfactory ways (p. 246).
- Terrestrial systems tend to consist of loosely coupled subsystems (S.4/20). Each subsystem consists of smaller, more closely coupled ones. In a herd of cattle, coupling between members is looser than between the four limbs of one animal, and these are looser than the coupling of molecules within a bone (p. 246).
- So the chief source of disturbance D is often other systems loosely coupled to T, and often similar enough to those in T that they might equally have been included in it. Some boundary must still be drawn, at least in practical scientific work, or no definite statement can be made (p. 246).

### 13/4. Ways regulation may be made possible (p. 246)
- If regulation is not possible, the organism perishes, an extremely common outcome that must not be forgotten, though it needs no detailed consideration (p. 246).
- Possible ways: lower what counts as acceptable (a "somewhat trivial solution"), or increase the scope and power of R until its capacity is adequate. Neither is considered in detail. Ashby takes up the case in which regulation, apparently most difficult or impossible, is actually possible (p. 246).

### 13/5–13/6. Constraints (pp. 246–247)
- For the case in which regulation looks impossible but is actually possible, Ashby says the law of Requisite Variety implies that the variety in D is not really as large as it seems. In other words (S.7/8), the disturbances show a *constraint* (p. 246).
- The case: D has many components, each showing variety. The first estimate of D's variety puts it too high. We are then in danger of deducing, if R's capacity is given, that regulation of E (the essential variables) to a certain degree is impossible (p. 246).
- Further examination may show that the components are not independent, so the real variety is much lower. With R's capacity given, this smaller variety may be regulated against, and full regulation achieved. Discovery of a constraint "may convert 'regulation impossible' to 'regulation possible'" (p. 246).
- If R's capacity is fixed, it is the only way. When a constraint exists it can be turned to use (S.7/14) (p. 246).
- If R's capacity is not easily increased and the other methods are not possible, then the law says that discovering a constraint is the would-be regulator's only hope (p. 247).
- Constraints do not fall into a few simply described classes (S.7/10). Ashby studies one form that is of interest in itself, illustrates the previous chapter's thesis and matters in practice (p. 247).

*Intuition note.* Counting all conceivable disturbances can wrongly suggest regulation is hopeless. If the disturbances are tied to one another, far fewer really occur, and a regulator of fixed capacity may then be enough.

### Repetitive disturbance, 13/7 (pp. 247–248)
- Many disturbances and their regulatory responses are repetitive, especially over a long time. Examples: the cough reflex, most physiological regulators, the coastal lifeboat. The singular "the regulatory response" in earlier chapters was only because one action is typical of the set (pp. 247–248).
- A regulation acting once only is hard to find. Ashby's candidate is an observatory preparing for a supernova, which might not recur in the director's lifetime. The director would draw up a table like that of S.11/4 (uncertainties D, resources R, outcomes E) and inspect it (p. 248).
- Non-repetitive cases exist but are uncommon. From here the disturbance and response occur more than once, and such cases show constraint of which advantage can be taken (p. 248).

### 13/8. How the constraint arises (pp. 248–250)
- A disturbance may be a vector (an ordered list of components). At least two main types: (1) components acting simultaneously (S.11/17), for example an air-conditioner regulating temperature and humidity at once; (2) components occurring in succession, as in a thermostatically controlled water bath (p. 248).
- The bath can be judged over a short interval, where "the disturbance" is such an event as immersing a flask and the response is what happens in the next minute. It can also be judged over a long interval, where the year's disturbances are a *Grand Disturbance* (many small disturbances $d$) and the responses a *Grand Response* (many $r$). By some standard of what a bath should do over a year, one judges a Grand Outcome Good or Bad (p. 249).
- "Good" for the Grand Outcome does not follow necessarily from "good" ($\eta$) in the individual outcomes. It must be defined anew (p. 249).
  - Lottery with three tickets: 1 good + 2 bad individual results counts as Good.
  - Tried three times for murder, acquitted once: the same 1 good + 2 bad counts as Bad.
  - If each individual disturbance threatens death, Good must mean that every one of the individual outcomes is good.
- Grand Disturbances are vectors whose components are the individual disturbances in time order, and these vectors show constraint. Contrast the vector A (age of car, horse power, colour) with B (age of Jack's car, Jill's car, Tom's car). The variety among the left-hand words is three in A and one in B, so B is restricted (p. 249).
- Vectors like B occur in probability as "sampling with replacement". A coin spun six times in succession can give $2^6 = 64$ results, such as (H,H,T,H,T,H) (p. 249).
- In such a set of vectors, whose components all come from one basic class, two varieties can be distinguished: (i) the variety within the basic class; (ii) the variety built by using the class $n$ times. If the basic variety is $k$ and the vector has $n$ components, the two are at most $k$ and $k^n$. For the coin they are 2 and 64 (p. 250).
- If the variety of the basic class has some limit, a suitably large $n$ makes the second variety larger than that limit (p. 250).

### 13/9. The water-bath example and the machine (pp. 250–251)
- In each minute the bath may be hit by (a) a draught cooling it, (b) sunshine warming it, (c) a cold object immersed in it. Variety is three, which hardly represents what occurs over a long time. A year gives a long vector, e.g. 400 components: $(a,b,a,b,b,a,c,b,b,c,c,b,b,\dots,c,b,a,b)$ (p. 250).
- The individually correct responses are $\alpha,\beta,\gamma$ respectively, so the matching Grand Response is $(\alpha,\beta,\alpha,\beta,\beta,\alpha,\gamma,\beta,\beta,\gamma,\gamma,\beta,\beta,\dots)$ (p. 250).
- If there is no constraint from component to component, the set of possible Disturbances has variety $3^{400}$. The Grand Response must have at least as much if full regulation is to be obtained (p. 250).
- The point: the double sequence as it occurred in time (events $a\,b\,a\,b\,b\,a\,c\,b\,b\,c\,c\dots$ paired with $\alpha\,\beta\,\alpha\,\beta\,\beta\,\alpha\,\gamma\,\beta\,\beta\,\gamma\,\gamma\dots$, not necessarily at equal intervals) shows the characteristic constraint of a machine. It defines a machine up to an isomorphism (p. 250).
- Taken as a protocol, the sequence defines the machine with input in the table below (rows: input; columns: state). Each input $a,b,c$ sends every state to $\alpha,\beta,\gamma$ respectively (p. 251).

| ↓ | α | β | γ |
|---|---|---|---|
| a | α | α | α |
| b | β | β | β |
| c | γ | γ | γ |

- Hence when the Grand Disturbance is a vector whose components are all from a basic set, the Grand Response can be either a vector of equal variety or the output of a suitable machine with input (p. 251).

*Intuition note.* A long record of "what happened" and "what we did" can be replaced by a short rule that maps each disturbance to its response. A machine embodying that rule can then do the regulating indefinitely.

### 13/10. Q: act as regulator, or build one? (p. 251)
- Let Q be the entity responsible for the regulation, often the possessor of the essential variables. When disturbances are repetitive, Q can either act as R or build a machine that will act as R for indefinite length without further action by Q (p. 251).
- A second reason to ask how a regulator is made: Part III assumed the regulator existed and asked what properties it must have. S.10/5 showed the advantage of having one but gave no means of getting it. So the design of a regulatory machine must now be considered. Ashby has in mind the brain developing regulatory machinery within nervous material, or a sociologist wanting a regulatory organisation (p. 251).

### Designing the regulator, 13/11. Design as communication (pp. 251–253)
- Ashby's section heading is printed "3|11" (see Reading notes). The scheme of an entity Ω designing a machine M is to cover: genes determining the heart; a mechanic making a bicycle; one part of the brain fixing the connexions of a nerve-net; a works-manager laying out a factory; a mathematician programming a computer (p. 252).
- The cybernetic interest is not in shaping matter but in what determines the final model, i.e. how it comes to be selected. Like a telephone mechanic matching each wire at one end to a wire at the other, one relates a set of possible initial causes to a set of final machines (p. 252).
- The treatment exemplifies MacKay's thesis: quantity of information, as measured here, always corresponds to some quantity (intensity) of selection, actual or imaginable (p. 252).
- Example: the gene-pattern in *Lumbricus* leads to an earthworm's heart, in *Rana* to a frog's, in *Homo* to a man's. Control and regulation are both involved: whatever state the molecules are initially in, the variety disappears and a standard heart appears (p. 252).
- Design concepts apply essentially to sets. "The gene-pattern determines the form of the heart" is shorthand for a correspondence between gene-patterns across species and hearts, like wires at two ends of a cable. So designing a machine is essentially an act of communication from Maker to Made, and communication theory applies. The measures for reducing many possible messages to one apply to reducing many possible machines to one (p. 253).
- A device: imagine the design done through a telephone, so that the quantities of variety can be identified with the actual quantity of information that must be transmitted (p. 253).

### 13/12–13/13. Selecting a machine is fixing an input (pp. 253–255)
- Three equivalent cases for a radio receiver: a buyer picks one of three machines; a designer picks one of three circuits; an owner moves a switch among three built-in circuits. Abstractly, selecting one machine from three equals selecting one value from three at a parameter (p. 253).
- Machines $\alpha,\beta,\gamma$ on states $a,b$: $\alpha: a\to b,\ b\to a$; $\beta: a\to a,\ b\to a$; $\gamma: a\to b,\ b\to b$ (p. 253). Selecting $\beta$ is identical with having a machine with a three-valued input (table below) and fixing the input permanently at $\beta$ (p. 254).

| input | a | b |
|---|---|---|
| α | b | a |
| β | a | a |
| γ | b | b |

- The processes are "identical" in the sense that an observer watching only the results cannot tell which occurred, except by reference to other, unmentioned, criteria (p. 254).
- Fixing the input leaves an absolute system (no input). If the result is to be a machine with input, the original must have two or more inputs, so that fixing one leaves the others free (p. 254).
- Result: the designer's act of selecting one model from many is equivalent to some determining factor fixing an input at a permanent value (p. 254).
- 13/13 (minor complication): what if the choice is between machines on different state sets, $a\to b, b\to a$ and $p\to r, q\to q, r\to r$? This is contained in the former case by a change of notation. Take a (reducible) machine whose states are couples $(a,p),\dots,(b,r)$. Input $\mu$ sends $(a,\cdot)\mapsto(b,\cdot)$ and $(b,\cdot)\mapsto(a,\cdot)$. Input $\nu$ sends $(\cdot,p)\mapsto(\cdot,r)$, $(\cdot,q)\mapsto(\cdot,q)$, $(\cdot,r)\mapsto(\cdot,r)$. The dots stand for values that do not matter. Choosing $\mu$ gives the first machine and choosing $\nu$ the second (pp. 254–255).

### 13/14. Design in a Black Box (p. 255)
- Design can be carried out within a Black Box that has an input. An owner of the radio set who knows nothing of its contents but knows how the output is affected by the switch performs design in a Black Box by setting the switch to get the desired behaviour (p. 255).
- A dominating machine whose activities fix the switch position can be said to "design" the radio set, provided we remember the sense of the word. One part of a brain, perhaps a basal structure, can show towards a neural network it dominates the objective behaviour of a designer (p. 255).
- So one machine designing another can be stated exactly: experiment can show objectively whether the relationship holds (p. 255).

### Quantity of selection, 13/15–13/16 (pp. 255–257)
- The reduction from many initial possibilities to the final few or one is measured on the same scales as variety and information (S.7/7, 9/11), directly or logarithmically. The measure gives the capacity the channel C from Designer to Machine must have for the necessary variety to be transmitted (pp. 255–256).
- The measure does not tell how much design there is in a machine considered without reference to what it might have been. It exists only over the set of possibilities and applies to the act of communication, not to the resulting thing (p. 256).
- 13/16: the variety between two Markovian machines (transition-probability matrices) is just 1 bit, for we choose between two objects and their inner fractions are irrelevant. This differs from the 1.58 bits associated with the right-hand matrix (all entries 1/3) regarded as an information source (p. 257).

*Intuition note.* "How much design" only makes sense relative to the set of machines that were possible. A choice between two machines costs 1 bit however complicated each machine is.

### 13/17. Selection in stages (pp. 257–258)
- A driver choosing a car narrows the possibilities criterion by criterion (under £1000, seats five, …); somehow the reduction must reach one, even if a coin is the final selector (p. 257).
- For a machine with states $a,b,c,d$: $T:\ a,b,c,d\to *,*,*,*$ leaves all open. $U:\ a\to c,\ c\to b$, with $b,d$ undecided, is a partial selection (a smaller set of transformations). $V:\ a\to(b\text{ or }c)$, rest undecided, excludes all single-valued transformations containing $a\to a$ or $a\to d$ (pp. 257–258).
- Fundamental quantitatively: the overall selection achieved cannot be more than the sum, measured logarithmically, of the separate selections (selection is the fall in variety). With a pack of cards, a 2-bit selection followed by a 3-bit one cannot indicate a unique card unless a further selection of at least 0.7 bits is made, since $\log_2 52 \approx 5.7$. The limitation is absolute and has nothing to do (if a machine is selected) with the type of machine or the mode of selection (p. 258).

*Intuition note.* Narrowing a choice in several steps cannot create more narrowing than the steps contain. If 5.7 bits are needed and only 5 are supplied, at least 0.7 bits are still missing.

### 13/18. Supplementation of selection (pp. 258–259)
- Because selection can go in stages, more than one selector may act, each supplementing the other (p. 258). Examples:
  - A husband fixes a price limit and lets his wife make the rest of the selection; in a variant, the wife, having reduced the choice to two models, spins a coin.
  - At Bridge, the state at the first lead was selected partly by bids and partly by the chance of shuffling. The rules assign a definite part of the determination to chance.
  - A Roman general left the remainder to birds or entrails.
- The first deliberate use of wholly uncorrelated selectors to complete the experimenter's selection in science was apparently Fisher's (p. 259).
- "Random" refers to a factor's relation to the main system, not to the factor itself. A block of a thousand digits of $\pi$ is determinate but may serve for agricultural experiments, because it is probably uncorrelated with the peculiarities of the plots. Supplementation by chance, apart from minor special requirements, means taking variety from a system uncorrelated with the main system. Yesterday's gold-share price might suit a rat in a maze, but not a portion of the financial-economic system (p. 259).

### Selection and machinery, 13/19. Selection by machine (pp. 259–260)
- The selector L in $L \to M$ must itself be considered a machine (p. 259). Ways a machine selects: (i) following one trajectory, so that after state $i$ it goes to $j$ and not to any other state (p. 260); (ii) every determinate machine reduces its variety from the initial maximum to the number of its basins (S.7/24) (p. 260); (iii) one part vetoes states of equilibrium in another part (S.5/13) until one is kept permanently (p. 260).
- Of these, Ashby says that a machine built as a selector will, as far as Ashby can see, have to act by vetoing, which is the way of the second-order feedback of Fig. 5/14/1 (supplemented in S.12/15). Other methods doubtless exist. In Shannon's theory every act of communication is also an act of selection (p. 260).

### 13/20. Duration of selection (pp. 260–261)
- Estimates of the selection needed may suggest a time beyond the cosmological, and one may jump to the conclusion that the actual selection must take equally long. This is far from the case (p. 260).
- Shannon: to select 1 from $N$, if the selector can only indicate whether the element is in a given set, the fastest method is successive dichotomies, with early selections between group and group. It is much faster than examining the $N$ one by one, and becomes almost incomparably faster as $N$ grows (p. 260).
- Example, find one unique atom in the visible universe (figures as printed, p. 261): about $10^8$ galaxies, each with about $10^{11}$ suns and systems, each system about 300000 earth-like bodies, the earth about $10^{12}$ cubic miles, a cubic mile about $10^{21}$ dust particles, each with about $10^{16}$ atoms. Ashby calls this 1 *mega-pick*, about 1 from $10^{73}$ (p. 261).
- Method 1: test a million atoms per second. The number of centuries needed would take more than the width of the page to write, so this dooms the selection to failure for practical purposes (p. 261).
- Method 2: dichotomy, one step per second: just over four minutes (p. 261). (added step: $\log_2 10^{73} \approx 73 \times 3.32 \approx 242.5$ steps, about 4 minutes.)
- Item-by-item search becomes excessively long exactly when group search shows its power (p. 261).

### 13/21. Selection and reducibility (pp. 261–262)
- Take a machine with 50 inputs, each with 25 values, with one form sought: about 1 megapick, so item-by-item selection is hopeless. Group selection needs some practical way of grouping the input states (pp. 261–262).
- Important case: the whole machine is reducible (S.4/14) and the inputs go separately to the sub-systems. Then selecting the right value for part 1 on its input, then for part 2 on its input, and so on, is selection by groups, the fast method. If the machine is reducible the fast method can be used (p. 262).
- Reducibility is extremely common in terrestrial systems, so common that it is usually taken for granted. If it were lost, so that every variable affected every other, turning a page might change the lights, move the table and alter the clock. Were the world really irreducible, regulation would be so difficult as to be impossible, and no organised life could persist (S.7/17) (p. 262).
- Conclusion: if the entity (Ω of S.13/10) designs a machine to regulate a very large system, so that the regulator is itself somewhat large, getting the selection done in reasonable time is likely to depend much on whether the regulator can be made in reducible form (p. 262).

*Intuition note.* Setting 50 knobs one at a time takes about 50 small searches. Searching all combinations at once takes a hopeless number. Our world's reducibility (parts with separate inputs) is what makes the first way available.

### 13/22. Whence the Regulator? (pp. 262–263)
- Making a machine with desired properties implies selection. The maker worked successfully to a goal, whatever the initial variety of components and designs, so the maker acted as a regulator. Making a machine of desired properties is an act of regulation (p. 263).
- If that machine is a regulator of Part III, it must be made "by another regulator". Ashby asks whether this is a reductio ad absurdum and answers "I think not" (p. 263).
- Where it starts: the earth has existed a long time, selection has acted throughout, and selection favours the appearance of regulators (S.10/3, 10/5). These facts alone suffice to account for many good regulators today. No further explanation is needed if some of them have as goal bringing some mechanism to a standard form, even that of a regulator. The scientist would be merely mildly curious why something doable directly in one stage is done in two (p. 263).
- Hence a regulator can be selected from a general set of mechanisms (many of them non-regulatory) only by being the survivor of natural selection, or by being made by another regulator (p. 263).

### 13/23. Two stages: wasteful? (pp. 263–264)
- **Worry (Ashby's own voice, a question and an exclamatory remark):** Ashby asks whether making the regulator in two stages is wasteful, and remarks that needing two stages suggests the problem of getting a regulator always has to be solved before it can be tackled (p. 263). He does not answer directly here; p. 264 concedes that regulation by stages is necessarily wasteful, but adds that it opens up remarkable possibilities (p. 264).
- A second question: if the very large system is the social and economic world and the responsible entity is a set of sociologists with the capacity of members of *Homo*, does this mean no advance in regulation is possible, since the regulator must be built by such members? Ashby: it does not. When a regulator $R_1$ brings a regulator $R_2$ into existence, $R_2$'s capacity is not bounded by that of $R_1$. $R_2$ may have greater capacity, so that an amplification occurs. This is studied in the next chapter (pp. 263–264).

## Toy example (ours, not from the text)
**Part A — repetition gives a constraint.** A bath is hit each minute by $a$, $b$ or $c$, and the correct responses are $\alpha,\beta,\gamma$. We watch five minutes. Disturbances: $(c,a,a,b,c)$. Responses: $(\gamma,\alpha,\alpha,\beta,\gamma)$.
- With no component-to-component constraint, the number of possible five-long Grand Disturbances is $3^5 = 243$, which is $5\log_2 3 = 5 \times 1.585 \approx 7.92$ bits.
- The record is consistent with the three-row rule $a\to\alpha,\ b\to\beta,\ c\to\gamma$ (as in the p. 251 table). A machine with that rule produces the right response to any of the 243 sequences.

**Part B — selecting by parts.** A designer must choose three settings, each one of 4 values, so $4^3 = 64$ machines, which is $\log_2 64 = 6$ bits.
- Item by item: up to 64 tries.
- By parts (the settings are independent, as in a reducible machine): halve the 4 values of setting 1 (2 yes/no questions), then setting 2 (2), then setting 3 (2). That is $3 \times 2 = 6$ questions, and $2^6 = 64$.
- Staged limit: a 2-bit criterion followed by a 3-bit one removes $2^5 = 32$-fold of the 64, leaving $64/32 = 2$ machines. At least $6 - 5 = 1$ more bit of selection is needed.

## Concepts
- [[law of requisite variety]] — if R's channel capacity is fixed, the law places an absolute limit on the regulation R can achieve (p. 245)
- [[variety]] — number of distinguishable states or elements of a set; in vectors, $k$ within the class and at most $k^n$ for $n$ components (p. 250)
- [[disturbance and noise]] — here: D, the source of disturbances, against T, the system yielding the outcome. In very large systems the boundary between them may be drawn in several equally good ways (p. 246)
- [[black box]] — a system whose contents are unknown but whose output is known to respond to an input such as a switch. Setting the switch to get the desired behaviour is design in a Black Box (p. 255)
- [[constraint]] (new) — dependence among components of D (or restriction of a set of possibilities) that makes real variety lower than the first estimate (p. 246)
- [[repetitive disturbance and grand disturbance]] (new) — a disturbance recurring over time; a long period's disturbances are treated as one vector, the Grand Disturbance, with a Grand Response (p. 249)
- [[design as selection]] (new) — "designing" a machine is picking one from a set, equivalent to fixing an input permanently, and an act of communication from Maker to Made (pp. 253–255)
- [[quantity of selection]] (new) — fall in variety, measured in the same units as variety and information. The overall selection cannot exceed the sum of the stage selections (in logs) (p. 258)
- [[selection by groups (dichotomy)]] (new) — choosing between groups, not single items, at each step. It can be much faster than item-by-item search (p. 260)
- [[reducibility]] (new) — machine made of sub-systems (S.4/14, defined earlier). Here: if its inputs go separately to the sub-systems, parts can be selected in turn. Very common on earth (p. 262)
- [[supplementation of selection]] (new) — completing a selection by another selector, including chance; "random" means uncorrelated with the main system (p. 259)
- [[regulation by stages]] (new) — a regulator $R_1$ makes a regulator $R_2$; $R_2$'s capacity is not bounded by $R_1$'s (p. 263)

## Canonical instances
- [[thermostat water bath over a year]] — long record of disturbances and responses defines a machine (pp. 250–251)
- [[coin spun six times]] — basic variety 2, vector variety 64 (p. 249)
- [[radio set with three circuits]] — selecting a machine equals fixing an input (p. 253)
- [[gene-pattern and heart]] — design as correspondence of sets, with control and regulation (p. 252)
- [[unique atom and the mega-pick]] — just over four minutes by dichotomy, against more centuries than a page's width can write item by item (p. 261)
- [[card-pack selection]] — 2 bits plus 3 bits leaves at least 0.7 bits still to select out of $\log_2 52 \approx 5.7$ (p. 258)
- [[Bridge shuffle and digits of pi]] — chance supplementing selection; randomness as relation (p. 259)
- [[cattle herd loose coupling]] — loosely coupled systems and the D/T boundary (p. 246)

## Bridges (candidates)
- [same-math] quantity of selection as bits ↔ information theory: $\log_2$ of the number of equally available options — Ashby uses the same scale as information (pp. 255–256)
- [same-math] selection by successive dichotomies ↔ computer science: binary search finds one of $N$ in about $\log_2 N$ yes/no steps (p. 260)
- [structural-analogy] part-by-part selection of a reducible machine ↔ optimisation: searching separable coordinates one at a time against a joint search (p. 262)
- [structural-analogy] supplementing selection with uncorrelated chance ↔ statistics: randomised experimental design, which Ashby credits to Fisher (p. 259)
- [metaphor] regulator made by regulator, capacity unbounded by the maker ↔ learning systems that build better learners (pp. 263–264)

## Questions this raises
- How can a regulator actually discover a constraint in D, when it cannot first count every disturbance?
- The chapter says $R_2$ may exceed $R_1$ in capacity. What mechanism of amplification does the next chapter give, and what does it cost?
- How can a machine be built to do the "vetoing" selection of S.13/19 so that it reaches a good regulator in reasonable time?
- When is the boundary between D and T chosen badly enough to change a regulation conclusion, given Ashby's remark that sometimes an equally reasonable boundary would not significantly affect the final conclusions (p. 246)?

## Exercises worth doing
- Ex. 1, after S.13/15 (p. 256) — three resistances with seven values each: variety the designer must supply to reduce to one — easy
- Ex. 3, after S.13/15 (p. 256) — parallel resistances: compare counting component values with counting the electrical properties to be reduced to one — medium
- Ex. 5, after S.13/15 (p. 256) — penny stamp (dots versus three submitted forms), "explain the lack of agreement": tests the point that the measure applies to a set of possibilities — medium
- Ex. 6, after S.13/15 (p. 256) — variety needed to reduce to one the possible machines on $n$ states — medium
- Ex. 4–5, after S.13/17 (p. 258) — selection exerted by "no state of equilibrium" on $n$ states, and its limit as $n$ grows — hard
- Ex. 6–7, after S.13/17 (p. 258) — information gained in systematic versus random search for a card in a pack — hard

## Reading notes
- Printed pages 244–264. Each PDF page holds two printed pages: pdf N = printed $2N-16$ and $2N-15$ (pdf 130 = pp. 244–245; pdf 140 = p. 264 plus a blank page).
- Page images were given for pdf 133–137 and 140. The pages with text layer only (pdf 130–132, 138, 139, i.e. pp. 244–249 and 260–263) were not checked against images.
- The section heading on p. 251 is printed "3|11" for 13/11.
- The page image and text layer both show "3400" and "kn" (p. 250). The context (400 components; $k^n$) shows these are exponents $3^{400}$ and $k^n$ with flattened superscripts.
- Misprints visible in the images: "loo ohms" for 100 (p. 256, Ex. 1); "1 58 bits" without a decimal point (p. 257); "Ex. I" for Ex. 1 (p. 258, Ex. 3); "al" for $a_1$ (p. 258, Ex. 4).
- The responsible entity is called Q in 13/10 and 13/22 and Ω in 13/11, 13/21 (which refers to "S.13/10") and 13/23. Ashby mixes the symbols; I kept each as printed.
- The text layer on pp. 262–263 has small garbles ("an with", "thin", "o"); I read them from context. "(man, non- regulatory)" on p. 263 is read as "many non-regulatory". The p. 262 reference to "Design …" and "Iterated systems" is truncated in the text; the earlier work is not named in full here.
- The exercises have no printed solutions in these pages.
