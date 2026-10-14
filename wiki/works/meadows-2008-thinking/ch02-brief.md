---
id: meadows-2008-thinking/ch02-brief
work: meadows-2008-thinking
unit: "Chapter Two — A Brief Visit to the Systems Zoo"
pages: 35-72
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# A Brief Visit to the Systems Zoo

## L0 — One line
Simple stock-and-feedback structures (two balancing loops, one reinforcing plus one balancing loop, delayed balancing loops, growth limited by a resource) each produce a characteristic behavior, and similar structures produce similar behavior.

## L1 — The gist (≤ 120 words)
Meadows asks what behavior simple feedback structures produce. Through five small "zoo animals" she shows how stocks behave with two balancing loops (thermostat), a reinforcing and a balancing loop (population, capital), delayed balancing loops (car inventory), and growth constrained by a nonrenewable or renewable resource (oil, fishery). Behavior (settling short of a goal, growth, decline, oscillation, overshoot, collapse) depends on which loop dominates, how loop strengths shift, how long delays are, and how the goal is set. Systems with similar structures behave alike. The lesson: study structure to anticipate behavior, and beware well-meant fixes that make it worse.

**Prerequisites:** stocks and flows; balancing and reinforcing loops (bathtub, coffee-cup cooling from Chapter 1); percent growth and doubling time.

## L2 — Key ideas
- **Competing balancing loops can leave a stock short of its goal.** A thermostat room settles slightly below the setting because heat keeps leaking out, so the goal must be set to include draining or filling flows (pp. 38–40).
- **Feedback information only affects future behavior,** so delays in responding always exist (p. 39).
- **Loop dominance shifts.** One reinforcing plus one balancing loop on a stock gives growth, decline, levelling-off, or a sequence of these, depending on which loop is stronger over time (pp. 44–45).
- **Similar feedback structures give similar behavior,** even when systems look unlike: population and industrial capital share one structure (pp. 49–51).
- **Delays in a balancing loop make oscillation likely.** Acting faster in the inventory model made oscillations worse ("high leverage, wrong direction"), while a longer response delay damped them (pp. 54–57).
- **Exponential growth toward a limit reaches it surprisingly fast.** Doubling a nonrenewable resource buys only about 14 years of extra time to the extraction peak in the oil model (p. 63).
- **A renewable resource can end in equilibrium, oscillation or collapse,** depending on the regeneration threshold and how fast the balancing loop slows capital growth (pp. 71–72).
- **System dynamics models usually explore "what if" scenarios rather than predict.** Three questions test a model's value, and its utility depends on a realistic pattern of behavior, not on realistic scenarios (pp. 47–48).

## L3 — Walkthrough

### Introduction (p. 35)
- Meadows teaches through examples. The chapter is a "zoo": it shows a variety of systems grouped by family (single-stock, two-stock). Like a zoo, it is too neat. Real systems are mixed together and interact (p. 35).

### One-stock systems

#### A stock with two competing balancing loops: a thermostat (pp. 36–42)
**Structure (Fig. 15, p. 36).** One stock, room temperature. Loop 1 (left): the discrepancy between thermostat setting and room temperature controls heat flow from the furnace. Loop 2 (right): the discrepancy between inside and outside temperature controls heat flow out. Both are balancing (B). Loop 2 behaves like a cooling coffee cup (pp. 36–37).

**Each loop alone.**
- Furnace loop alone, cold room, setting 18 °C (65 °F): the room warms and holds exactly at the target (Fig. 16, p. 36–37).
- Leak loop alone, warm room, outside 10 °C: the room cools slowly toward the outside temperature; better insulation means slower cooling (Fig. 17, p. 37).

**Both together.** With sufficient insulation and a properly sized furnace, the heating loop dominates, so the room ends up warm (Fig. 18, p. 37). The room warms nearly to the target, then the furnace cycles on and off. It levels off slightly below 18 °C because the leak drains heat even as the furnace replaces it (p. 38).
- Author's analogy: keeping a bucket full when there is a hole in the bottom. The hole is itself governed by a feedback loop (more water, more pressure, more outflow); likewise the warmer the room, the faster it loses heat (p. 38).
- A well-insulated house is more comfortable than a poorly insulated one, even one with a big furnace (p. 38).
- People set the thermostat slightly higher than their real target. The right amount is tricky because outflow is higher on cold days, but for thermostats you can muddle through (pp. 38–39).
- For other systems with competing balancing loops, the stock keeps changing while you try to control it, which can cause real problems. Examples: store inventory (orders take time, and goods sell meanwhile), cash balance, reservoir level, chemical concentration in a flow reactor (p. 39).

**General principle (p. 39).** Information delivered by a feedback loop, even nonphysical information, can only affect future behavior. It cannot correct the behavior that produced the current feedback. Hence there are always delays in responding. A flow cannot react instantly to a flow. It can only react to a change in a stock, after a slight delay. Author's criticism: many economic models wrongly assume production or consumption responds immediately to price (p. 39).

**Specific principle (pp. 39–40).** In thermostat-like systems, take draining and filling processes into account, or you will not reach the target. Examples: set the thermostat a little above the desired temperature; raise credit-card repayment enough to cover new charges including interest; hire fast enough to offset quits when gearing up a workforce. A stock-maintaining balancing loop must have its goal set to compensate for draining or inflowing processes. Otherwise it falls short of or exceeds the target (p. 40).

> **Intuition note.** In the thermostat, the leak keeps draining heat even while the furnace is putting it back, so the room settles slightly below the setting. So the goal has to be set to allow for such draining or filling flows, or you will be surprised by the result.

**Varying outside temperature (Figs. 19–20, pp. 40–42).**
- In a well-functioning system over 24 hours with the outside dipping well below freezing, furnace inflow tracks heat outflow and room temperature varies hardly at all once warmed up (Fig. 19, p. 40).
- Every balancing loop has a breakdown point, where other loops pull the stock from its goal more strongly than it pulls back. This happens if the heating loop is weakened (smaller furnace) or the cooling loop strengthened (colder outside, less insulation, larger leaks) (p. 40–41).
- Fig. 20 (faster heat loss, same outside temperatures): at first the furnace inflow exceeds the leak and the room warms. For an hour or two the room stays near the target. As the outside cools, the furnace cannot replace the heat, so the room cools. When the outside warms again, the furnace, still at full tilt, pulls ahead and the room warms (p. 41).
- Bathtub rule restated: the temperature rises when the furnace inflow exceeds the leak, and falls when the inflow falls behind. Behavior unfolds from two loops shifting in strength relative to each other (pp. 41–42).

#### A stock with one reinforcing and one balancing loop: population and industrial economy (pp. 42–51)
**Population (Fig. 21, p. 42).** Births (driven by fertility) form a reinforcing loop; deaths (driven by mortality) form a balancing loop. Meadows says this structure describes every living population and every economy (p. 42).
- If fertility and mortality are constant (rarely true in real systems), the population grows exponentially or dies off, depending on whether the births loop is stronger than the deaths loop (p. 42).
- Numbers for 2007: world population 6.6 billion; fertility about 21 births per 1,000 people per year; mortality 9 deaths per 1,000. The reinforcing loop dominates. If rates stay unchanged, a child born now will see the population more than double by age 60 (Fig. 22, pp. 42–43).
- If mortality rose to 30 per 1,000 with fertility at 21, the death loop dominates and the population gradually declines (Fig. 23, p. 43).
- UN long-range projections generally assume fertility declines as countries develop (approaching replacement, 1.85 children per woman on average). They assumed mortality would decline more slowly. Because of HIV/AIDS, the UN now assumes the rise in life expectancy slows in affected regions (p. 44).
- Changing flows bend the stock's line. If fertility falls steadily to equal mortality by 2035 and both then stay constant, the population levels off, with births exactly balancing deaths, a dynamic equilibrium (Fig. 24, pp. 44–45).

**Shifting dominance (pp. 44–45).** When one loop dominates another, it has a stronger impact on behavior. Systems often have several competing loops, and the dominant ones determine behavior. In the population example, the reinforcing loop dominates at first, then weakens as fertility falls, until it equals the balancing loop; then neither dominates (pp. 44–45). The thermostat showed the same shift (heating loop to cooling loop) in the leaky house (p. 45).

**The possible behaviors (p. 45).** For a stock governed by linked reinforcing and balancing loops: it grows exponentially if the reinforcing loop dominates; it dies off if the balancing loop dominates; it levels off if the two are of equal strength (Fig. 25). It does a sequence of these if their relative strengths change (Fig. 26, p. 47). Meadows says these are the only ones possible for a simple system of one reinforcing and one balancing loop (p. 45).

> **Intuition note.** The stock rises when its inflow exceeds its outflow and falls when the inflow falls behind (p. 41). Growth, decline and levelling-off are three cases of "inflow bigger / smaller / equal". Complex curves come from the balance tipping over time.

**Three questions for testing a model's value (boxed, pp. 45, 47–48).**
1. *Are the driving factors likely to unfold this way?* This is a guess about an uncertain future and cannot be answered factually. Systems analysis tests several scenarios. You judge which to take seriously. Dynamic-systems studies usually do not predict; they explore what would happen if driving factors unfold in various ways (pp. 45–47).
2. *If they did, would the system react this way?* This is the more scientific question about whether the model captures the system's inherent dynamics. For the population scenarios the answer is roughly yes. The model is simple (a detailed one would distinguish age groups), "the numbers are off, but the basic behavior pattern is realistic" (pp. 47–48).
3. *What is driving the driving factors?* This is a question about system boundaries: are the drivers independent, or embedded in the system? Fertility and mortality are themselves governed by feedback loops, and some are affected by population size. The population is one piece of a larger system (p. 48).

Model utility depends on whether it responds with a realistic pattern of behavior, not on whether its driving scenarios are realistic, since no one can know that for sure (margin note, p. 48).

**Industrial capital (Fig. 27, pp. 48–51).** Same kind of structure (p. 48).
- More physical capital (machines, factories) and more output per unit of capital mean more annual output. Investing a fraction of output builds new capital: a reinforcing loop, like births. The investment fraction is equivalent to fertility (p. 49).
- Depreciation (obsolescence, wearing out) is a balancing loop, like deaths. Capital "mortality" is set by average capital lifetime. The longer the lifetime, the smaller the fraction retired each year (p. 49).
- Same structure, so the same repertoire of behaviors. World capital has recently been dominated by its reinforcing loop and has grown exponentially. The future depends on the investment fraction, the efficiency of capital, and the average capital lifetime (p. 49).
- With a constant investment fraction and constant efficiency, capital declines, stays constant or grows depending on lifetime (Fig. 28, p. 50). Parameters of Fig. 28: output per unit capital ratio of 1:3 and investment fraction of 20 percent; a 15-year lifetime just keeps up with depreciation, a shorter lifetime declines, and a 20-year lifetime grows exponentially (pp. 49–50). Longer lifetime means faster growth. A stock can be grown by decreasing its outflow rate as well as increasing its inflow rate (pp. 49–50).
- Many factors influence these parameters (interest rates, technology, tax policy, consumption habits, prices). Population and capital influence each other (labor, consumption, health care, birth and death rates). Any long-term model of a real economy should link the two structures. The central question of economic development: how to keep capital accumulation from growing more slowly than population growth, so that people get richer rather than poorer (p. 50).

**Key insight (pp. 50–51).** The two systems look different but share a stock with a reinforcing growth loop and a balancing death loop, plus an aging process. One central insight of systems theory is that systems with similar feedback structures produce similar dynamic behaviors, even if they look completely dissimilar. A cooling coffee cup is like a cooling warm room, a decaying radioactive substance, or a population or economy aging and dying: each declines through a balancing loop (p. 51).

> **Intuition note.** What matters is the pattern of loops, not the material. Systems that share a loop diagram produce similar dynamic behavior, even if they look unlike.

#### A system with delays: business inventory (pp. 51–58)
**Setup (Fig. 29, pp. 51–52).** A car dealer's inventory has inflow deliveries and outflow sales. She wants inventory to cover ten days of sales. She needs a buffer because daily deliveries and purchases do not match and customer purchases are unpredictable. She monitors perceived sales and adjusts orders: higher sales lead to higher perceived sales, a larger discrepancy to desired inventory, higher orders, more deliveries, and higher inventory (p. 52). This is a version of the thermostat: one balancing loop of sales draining the stock, and a competing balancing loop resupplying it (p. 52).

**Without delays:** a permanent 10-percent demand rise starting on day 25 gives a smooth, unsurprising step up in inventory (Fig. 30, p. 52).

**With three delays (Fig. 31, pp. 52–54):**
- *Perception delay* (intentional): she averages sales over the past five days to separate real trends from blips (p. 53).
- *Response delay:* she makes up one-third of any shortfall with each order, that is, partial adjustment over three days (p. 53).
- *Delivery delay:* five days for the factory to receive, process and deliver an order (pp. 53–54).

**Result (Fig. 32, p. 54).** The same demand rise now produces oscillations. Sequence told by the author: sales rise, so inventory drops; she waits to be sure; she orders more; inventory drops further before the orders arrive, so she orders more; then the large orders arrive, inventory recovers and overshoots; she cuts back, but earlier large orders are still arriving, so she orders even less and, almost inevitably, too little; inventory gets too low again, and so on around the new desired level (p. 54).

**Why (p. 54).** Not because the dealer is stupid. She operates without timely information and with physical delays. This is common. Example: a shower with a very long pipe between mixer and showerhead gives hot-and-cold oscillation from a long response delay (p. 54). Margin rule: a delay in a balancing feedback loop makes a system likely to oscillate (p. 54).

> **Intuition note.** In Fig. 31 the dealer's discrepancy compares inventory on the lot with desired inventory; the diagram shows no link from orders already on the way (our reading of the figure). With delays in information and delivery she orders too much, then too little. A balancing loop working with late information and slow physical effects can oscillate.

**Trying to fix it (pp. 54–57).** *Dealer's view:* she finds the oscillations intolerable (p. 55). There is not much she can do about the delivery delay, so she tries to react faster herself.
- Perception delay shortened from five days to two (Fig. 34, pp. 55–56): not much happens; oscillations are if anything a bit worse (p. 56).
- Reaction time shortened (making up shortfalls in two days instead of three): things get very much worse (Fig. 35, p. 56).
- She says to herself "High leverage, wrong direction" (p. 57). Meadows: a fixer is attracted to a lever that has a strong effect, then pulls it the wrong way. This is one example of how we can be surprised by counterintuitive system behavior (p. 57).
- Part of the problem is that she has been reacting too quickly, not too slowly, that is, overreacting. If she increases the response delay from three days to six, oscillations are greatly damped and the system reaches its new equilibrium fairly efficiently (Fig. 36, p. 57).
- The most important delay is the factory delivery delay, which she does not control, but she can still manage inventory quite well (p. 57).
- Margin note: delays are pervasive and strong determinants of behavior. Changing a delay's length may or may not (depending on the type of delay and the relative lengths of other delays) make a large change in behavior (p. 57). System thinkers watch for where delays occur, how long they are, and whether they are in information streams or physical processes. Some delays can be policy levers (p. 58).

**Scaling up (p. 58).** Imagine the inventory of all unsold automobiles in America. Orders affect steel, rubber, glass, textiles and energy producers, each with perception, production, delivery and construction delays. A jobs loop (more production, more jobs, more car buyers) is reinforcing and works in both directions. Share speculation is another reinforcing loop. Interconnected industries responding through delays, entraining each other's oscillations, and amplified by multipliers and speculators are, according to Meadows, the primary cause of business cycles. Presidents can ease or intensify them but do not originate them. Economies are full of balancing loops with delays and are inherently oscillatory (p. 58).

### Two-stock systems

#### Constraints on growth (pp. 58–60)
- Earlier models ignored the environment (capital needing no raw materials, populations needing no food, a furnace never running out of oil), which let their internal dynamics show (pp. 58–59). Any real physical entity exchanges things with its environment and needs a place for its wastes (p. 59).
- Any physical, growing system hits some constraint sooner or later: a balancing loop that shifts dominance away from the growth loop, by strengthening an outflow or weakening an inflow (p. 59).
- Systems thinkers call growth in a constrained environment the "limits-to-growth" archetype (archetypes are developed in Chapter Five). For any growing entity (population, corporation, bank account, rumor, epidemic, new-product sales) look for the reinforcing loops driving it and the balancing loops that will constrain it, even if not yet dominant (p. 59). Margin rule: in physical, exponentially growing systems there must be at least one reinforcing loop driving growth and at least one balancing loop constraining it, because no physical system can grow forever in a finite environment (p. 59).
- A pollution constraint can be renewable (the environment has finite, usually variable, capacity to remove it) or nonrenewable (no capacity). Resource-constrained dynamics apply to pollution with opposite flow directions (pp. 59–60).
- Limits may be temporary or permanent. Eventually there is accommodation: the system adjusts, or the constraint, or both. Whether the resource is renewable or not does not change whether growth can continue forever (it cannot), only how growth is likely to end (p. 60).

#### A renewable stock constrained by a nonrenewable stock: an oil economy (pp. 60–66)
**Structure (Fig. 37, p. 60).** An oil company has discovered a huge field. It is the capital model, using "profit" instead of "output" (p. 61).
- Depreciation: capital lifetime of 20 years, so 1/20 (5 percent) of capital leaves service each year (p. 61).
- Reinforcing loop: more capital allows more extraction, hence profit, hence investment. The company has a goal of 5 percent annual growth of capital; if profit is too low, it invests what it can (p. 61).
- Profit = income − cost. Income = price × amount extracted. Cost = capital × operating cost per unit of capital. Price and operating cost per unit capital are assumed constant for now (p. 61).
- The resource is nonrenewable, so its stock has no input. As it is extracted, the next barrel is harder to get (deeper, more dilute, less pressure). Yield per unit of capital falls (p. 61).
- New balancing loop: more capital, higher extraction, lower resource stock, lower yield per unit capital, lower profit, lower investment, slower capital growth (p. 61). Resource depletion could also feed back through operating cost; the pattern would be the same, the classic dynamics of depletion (p. 61).

**Behavior (Fig. 38, pp. 61–62).**
- Initial deposit: enough for 200 years at the initial scale of operation. Extraction nevertheless peaks at about 40 years, because of exponential growth (pp. 61–62).
- With an investment rate of 10 percent per year and 5 percent depreciation, capital and extraction grow at 5 percent per year and double in the first 14 years (p. 62). (Added step: 5 % growth doubles in about $\ln 2/0.05 \approx 13.9$ years.)
- After 28 years capital has quadrupled but extraction lags because of falling yield. By year 50 the cost of maintaining capital has overwhelmed income, profit cannot keep investment ahead of depreciation, and the operation quickly shuts down. The last and most expensive oil stays in the ground (p. 62).

**Bigger resource (Fig. 39, p. 63).** Doubling or quadrupling the resource changes the total extractable a lot. But with the same 10 percent reinvestment goal, each doubling shifts the extraction peak (and the lifetime of dependent jobs and communities) by only about 14 years (p. 63). Margin: a quantity growing exponentially toward a limit reaches it in a surprisingly short time (p. 63). The higher and faster you grow, the farther and faster you fall. Doubling or quadrupling the resource gives little added time to develop alternatives (p. 63).

**Goals matter (p. 63).** If the concern is to extract fast and make money, the resource size is the most important number. For a worker concerned with job and community stability, two numbers matter: resource size and desired capital growth rate (a case of a feedback loop's goal being crucial). The real choice: get rich very fast, or get less rich but stay that way longer (p. 63).

**Growth rate (Fig. 40, p. 64).** Desired growth rates above depreciation of 1, 3, 5 and 7 percent. The extraction peak comes much sooner as the reinvested fraction rises. At 7 percent, extraction of the "200-year supply" peaks within 40 years (p. 64).

**Rising price (Fig. 41, pp. 64–65).** Suppose the resource is so vital that a higher price does not cut demand in the short term. Then scarcity raises price steeply. Higher profit raises investment, so capital grows higher and more costly resource can be extracted. Compared with Fig. 38, the main effect is to build capital higher before it collapses; the resource is depleted even faster at the end (pp. 64–65). The same behavior results if technology lowers operating costs (examples: advanced oil-well recovery, taconite beneficiation, cyanide leaching of mine tailings) (p. 64).

**Local and global limits (pp. 65–66).** Mines, oil fields and aquifers deplete; abandoned mining towns show it. Companies shift investment to new deposits before depletion hurts. Meadows leaves open whether local limits imply global limits. She points out that by the dynamics of depletion, the larger the initial resource and the more new discoveries, the longer growth loops elude the control loops, and the higher capital and extraction grow, and the earlier, faster and farther the fall after the peak. "Unless, perhaps, the economy can learn to operate entirely from renewable resources" (p. 66).

> **Intuition note.** Exponential growth makes a big resource look small: each doubling of the stock buys only one more doubling time of growth. Faster growth is a faster ride to the same wall.

#### Renewable stock constrained by a renewable stock: a fishing economy (pp. 66–72)
**Renewable resources (pp. 66–67).** Same capital system, but the resource stock now has an inflow (Fig. 42, p. 67). Living resources (fish, trees, grass) regenerate from themselves through a reinforcing loop. Nonliving ones (sunlight, wind, river water) are refilled by a steady input regardless of stock level (p. 66). Other cases with this structure: a cold-virus epidemic (victims recover and can catch another cold), sales of a regularly needed product (customers regenerate), an insect infestation that destroys part but not all of a plant (p. 66).

**The fishery (pp. 66–67).** Capital lifetime 20 years; industry grows at 5 percent per year if it can. As fish get scarce, harvesting costs more capital (bigger boats, sonar, long drift nets, refrigeration) (p. 66). Regeneration depends on fish density: when dense, reproduction is near zero (food, habitat limits); when the population falls a bit, regeneration speeds up; at some point reproduction hits a maximum; with further depletion it slows (fish cannot find each other, or another species moves into the niche) (pp. 66–67). Three nonlinear relationships: price (scarcer fish cost more), regeneration rate, and yield per unit of capital (p. 67).

**Behavior 1: equilibrium (Fig. 43, pp. 67–69).** Capital and harvest rise exponentially at first. The fish stock falls, but this stimulates reproduction. For decades the resource supports an exponentially rising harvest. Eventually the fish population is low enough to cut fleet profitability. The balancing feedback of falling harvest reducing profit cuts investment quickly enough to bring fleet and fish into equilibrium. The fleet cannot grow forever but can keep a high and steady harvest forever. In this run there is a small overshoot before levelling off (pp. 68–69).

**Behavior 2: oscillation (Fig. 44, p. 69–70).** A minor change in the strength of the controlling balancing loop through yield per unit of capital changes things: technology (e.g., sonar) keeps catch per boat up a little longer as fish decline. The result is overshoot and oscillation around a stable value in harvest, capital and resource. Meadows calls this another case of "high leverage, wrong direction": a productivity gain for all fishermen throws the system into instability (pp. 69–71).

**Behavior 3: collapse (Fig. 45, pp. 70–71).** If technology improves even more, boats stay economic at very low fish densities. The result can be a nearly complete wipeout of the fish and the industry, "the marine equivalent of desertification". The fish have become, for all practical purposes, a nonrenewable resource (p. 71).

**Real renewable systems (p. 71).** In many real systems a very small surviving population can rebuild once the capital driving the harvest is gone, and the pattern repeats decades later. Example: New England logging, now in its third cycle of growth, overcutting, collapse and regeneration. This is not true for all resource populations; technology and harvest efficiency increasingly can drive populations to extinction. Survival depends on what happens while the resource is severely depleted (vulnerability to pollution, storms, loss of genetic diversity, soil erosion, a competitor filling the niche) (p. 71).

**Stock-limited vs flow-limited (margin boxes, p. 71).**
- Nonrenewable resources are stock-limited: the whole stock is available at once and can be extracted at any rate (limited mainly by extraction capital), but since it is not renewed, the faster the extraction, the shorter its lifetime (p. 71).
- Renewable resources are flow-limited: they can support extraction indefinitely, but only at a finite flow rate equal to their regeneration rate. If extracted faster than they regenerate, they may eventually be driven below a critical threshold and become, for all practical purposes, nonrenewable (p. 71).

**What decides the outcome (p. 72).** Three behaviors: overshoot and adjustment to a sustainable equilibrium; overshoot then oscillation around it; overshoot then collapse of resource and industry. The outcome depends on (1) the critical threshold beyond which the resource's ability to regenerate is damaged, and (2) the rapidity and effectiveness of the balancing loop that slows capital growth as the resource is depleted. If the feedback stops capital growth before the threshold, the system comes smoothly to equilibrium. If it is slower and less effective, the system oscillates. If the balancing loop is very weak, so that capital keeps growing while the resource is pushed below the threshold, both resource and industry collapse (p. 72).

> **Intuition note.** Whether a fishery survives depends on a race: does the "stop investing" signal arrive before the fish pass the point of no recovery? Better fishing technology weakens that signal, so it can turn a stable fishery into an unstable one.

**Closing (p. 72).** Neither renewable nor nonrenewable limits allow a physical stock to grow forever, but their constraints are dynamically different, because of the difference between stocks and flows. The trick is to recognize which structures contain which latent behaviors and what conditions release them. Where possible, arrange structures and conditions to reduce the probability of destructive behaviors and encourage beneficial ones (p. 72).

## Toy example (ours, not from the text)
**Idea:** a balancing loop that reacts to a gap, but whose corrections arrive late, overshoots. A weaker correction damps the swing. (This echoes the dealer story on pp. 54–57; the numbers are ours.)

**Rules.** A tank holds stock $S$. Goal = 100. Each step we order $o(t)=g\,(100-S(t))$ (negative means removing stock, as a thermostat can cool as well as heat). An order arrives one step later than the next step: $S(t+1)=S(t)+o(t-1)$. Start: $S(0)=90$, $o(-1)=0$.

**Full correction, $g=1$:**
- $o(0)=10$; $S(1)=90+o(-1)=90$.
- $o(1)=10$; $S(2)=90+o(0)=100$.
- $o(2)=0$; $S(3)=100+o(1)=110$.
- $o(3)=-10$; $S(4)=110+o(2)=110$.
- $o(4)=-10$; $S(5)=110+o(3)=100$.
- $o(5)=0$; $S(6)=100+o(4)=90$.
- $o(6)=10$; $S(7)=90+o(5)=90$.
- $o(7)=10$; $S(8)=90+o(6)=100$.

So $S$ = 90, 90, 100, 110, 110, 100, 90, 90, 100. It swings forever between 90 and 110. Without the delay, one step would reach 100.

**Half correction, $g=0.5$:**
- $o(0)=5$; $S(1)=90$.
- $o(1)=5$; $S(2)=90+5=95$.
- $o(2)=2.5$; $S(3)=95+5=100$.
- $o(3)=0$; $S(4)=100+2.5=102.5$.
- $o(4)=-1.25$; $S(5)=102.5+0=102.5$.
- $o(5)=-1.25$; $S(6)=102.5-1.25=101.25$.
- $o(6)=-0.625$; $S(7)=101.25-1.25=100$.
- $o(7)=0$; $S(8)=100-0.625=99.375$.

So $S$ = 90, 90, 95, 100, 102.5, 102.5, 101.25, 100, 99.375. The swings shrink (overshoot +2.5, then −0.625). Same structure and same delay; the weaker response gives damped oscillation, as in Fig. 36 (p. 57).

## Concepts
- [[stock-and-flow]] (new) — stocks rise or fall as inflow exceeds or falls behind outflow (p. 41); a flow cannot react instantly to a flow, only to a change in a stock after a slight delay (p. 39).
- [[negative-feedback]] — balancing loop (B); pulls a stock toward a goal, e.g., furnace loop, depreciation, deaths (pp. 36, 42).
- [[positive-feedback]] — reinforcing loop (R); drives exponential growth, e.g., births, investment of output (pp. 42, 49).
- [[reference-set-point]] — the goal of a loop (thermostat setting, desired inventory, growth goal); here it must include compensation for leaks (pp. 36, 40, 63).
- [[error-signal]] — the "discrepancy" between goal and actual stock that drives corrections (pp. 36, 52).
- [[delay]] — perception, response, delivery and other delays; the author says a delay in a balancing loop makes oscillation likely (pp. 39, 52–54).
- [[shifting-dominance]] (new) — the stronger loop determines behavior, and which loop is stronger can change over time (p. 44).
- [[dynamic-equilibrium]] (new) — a stock constant because inflow equals outflow (births = deaths) (p. 44).
- [[limits-to-growth]] (new) — a growing physical system meets a balancing loop (resource, pollution) that constrains it (p. 59).
- [[renewable-vs-nonrenewable-resource]] (new) — stock-limited (no regeneration) versus flow-limited (finite regeneration rate) (p. 71).
- [[overshoot-and-collapse]] (new) — growth beyond a sustainable level, followed by decline; ending in equilibrium, oscillation or collapse (pp. 71–72).
- [[system-boundary]] (new) — the question of which factors are inside the model, i.e. what drives the driving factors (p. 48).
- [[behavior-from-structure]] (new) — systems with similar feedback structures yield similar dynamic behavior (p. 51).
- [[high-leverage-wrong-direction]] (new) — a policy lever with a strong effect pulled the wrong way, worsening behavior (p. 57).
- [[stability]] — in this unit, only informally: oscillation, damping, equilibrium (pp. 54, 57, 69).

## Canonical instances
- [[thermostat-room]] — two balancing loops on room temperature; settles slightly below the setting; breakdown with a leaky house (pp. 36–42).
- [[population-two-loops]] — births (R) and deaths (B); growth, decline, levelling-off with 2007 numbers (pp. 42–47).
- [[capital-stock-model]] — investment (R) and depreciation (B); lifetime of 15 years balances in Fig. 28 (pp. 48–50).
- [[car-dealer-inventory]] — delayed balancing loops give oscillation; shorter reaction time worsens it (pp. 51–57).
- [[coffee-cup-cooling]] — balancing decline, compared to room cooling and radioactive decay (p. 51).
- [[oil-extraction-model]] — capital growth ends in a peak and collapse; doubling the resource adds about 14 years (pp. 60–66).
- [[fishery-model]] — equilibrium, oscillation or collapse depending on yield per unit capital (pp. 66–72).
- [[shower-delay]] — long pipe causes hot/cold oscillation (p. 54).

## Bridges (candidates)
- [same-math] Constant fertility and mortality, $dP/dt=(f-m)P$ ↔ control-theory: first-order linear system with eigenvalue $f-m$ (growth if positive, decay if negative, levelling at zero) — the book states the cases verbally (p. 45), and the equation is our addition.
- [same-math] Capital lifetime threshold (Fig. 28) ↔ linear stability: with output $=K/3$, investment fraction 0.2, lifetime $L$, $dK/dt=(0.2/3-1/L)K$, which is zero at $L=15$ (our arithmetic from the figure caption, p. 50).
- [structural-analogy] Thermostat settling below its setting ↔ proportional-only control leaving a steady offset; the integral-action fix is not in this unit (canon link; not stated in this unit).
- [structural-analogy] Delay in a balancing loop leading to oscillation ↔ feedback with dead time: loop gain times delay limits stability; acting faster (higher gain) worsened oscillation (p. 56).
- [structural-analogy] Weak or slow balancing loop in the fishery ↔ a controller too slow relative to plant growth: the loop must act before the threshold is crossed (p. 72).
- [metaphor] "Zoo animals" (structures with characteristic behaviors) ↔ library of canonical feedback motifs (p. 35).

## Questions this raises
- What exactly determines whether a delayed balancing loop damps or oscillates? The book says changing a delay's length may or may not make a large difference, depending on delay type and relative lengths (p. 57), but gives no rule.
- In the oil model, is the claim of an earlier, faster and farther fall for larger resources (p. 66) consistent with the 14-year later peak per doubling (p. 63)? What is "earlier" measured against?
- How can one test question 3 (what drives the drivers) in practice, so that a model's boundary is drawn well (p. 48)?
- Meadows leaves open whether local limits imply global limits (p. 65). What structures would make renewable-resource use stay in the equilibrium case (p. 72)?

## Reading notes
- Printed page = pdf page − 17. Figure captions and numbers cited here are as printed on these pages.
- **Inconsistency in the source:** the text says the dealer averages sales over the past **five** days (p. 53), and the Fig. 34 passage uses five days (p. 55–56). The Fig. 33 caption says she averages the change over **3** days (p. 55).
- Fig. 45 caption reads "a patterns of overshoot" (typo, p. 70).
- Superscript note numbers (1–5) appear in the text; the notes themselves are not in this unit.
- Quantities in the graphs (inventory levels, harvest peaks) are read from figures and mostly not given in text; I omitted most of them. Text-given numbers are kept.
- No exercises in this unit, so no Exercises section.
