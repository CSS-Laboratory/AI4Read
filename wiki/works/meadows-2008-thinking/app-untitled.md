---
id: meadows-2008-thinking/app-untitled
work: meadows-2008-thinking
unit: Appendix (glossary, principles summary, system traps, leverage points, guidelines, model equations)
pages: 187–203
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Appendix: Glossary, Principles, Traps, Leverage Points, Model Equations

## L0 — One line
A system's structure is the source of its behavior (p. 188), and the appendix collects the book's definitions, rules of thumb, traps, leverage points and the equations of its nine simulation models.

## L1 — The gist (≤ 120 words)
This appendix is a reference sheet for the whole book. It defines core terms (stock, flow, balancing and reinforcing loop, resilience). It summarizes the book's principles. It names eight recurring "system traps" with ways out. It ranks twelve places to intervene in a system and lists fifteen guidelines for living with systems. Finally it gives the exact equations, parameters and run settings of the nine models behind the book's figures. All of them share one update rule: new stock = old stock + (inflows − outflows) × dt. The recurring point: system structure is the source of behavior, and systems with similar feedback structures produce similar behaviors.

**Prerequisites:** basic arithmetic with percentages; reading a simple graph; the idea of a quantity that changes by a fixed rule each time step.

## L2 — Key ideas
- A stock is an accumulation. It rises if inflows exceed outflows, falls if outflows exceed inflows, and is in dynamic equilibrium if they are equal (pp. 187–188).
- Balancing loops seek goals and resist change. Reinforcing loops give exponential growth or runaway collapse (p. 189).
- A delay in a balancing loop makes oscillation likely, and changing the delay length can change behavior a lot (p. 189).
- In physical, exponentially growing systems there must be at least one reinforcing loop driving the growth and at least one balancing loop constraining it, because nothing can grow forever in a finite environment (p. 190).
- Eight traps, such as the tragedy of the commons and shifting the burden, are common structures. Each comes with a "way out" (pp. 191–193).
- Leverage points are ranked from numbers (least effective) up to transcending paradigms (most effective) (p. 194).
- All nine models use one update rule: stock(t) = stock(t − dt) + (inflow − outflow) × dt. What differs between models is mainly the flow rules, parameters and run settings (pp. 195–203).

## L3 — Walkthrough

### Glossary (pp. 187–188)
Definitions are the author's.
- **Balancing feedback loop**: a stabilizing, goal-seeking loop. It is also called "negative" because it opposes whatever change is imposed (p. 187).
- **Reinforcing feedback loop**: an amplifying loop, also called "positive". Vicious cycles and virtuous circles are examples (p. 187).
- **Feedback loop**: a closed chain of causal links from a stock, through decisions or actions that depend on its level, back through a flow to change that stock (p. 187).
- **Stock**: an accumulation of material or information built up over time. **Flow**: material or information entering or leaving a stock (pp. 187–188).
- **Dynamic equilibrium**: a stock is steady despite flows, which is possible only when all inflows equal all outflows (p. 187).
- **Linear relationship**: constant proportion between cause and effect. **Nonlinear**: no proportional effect (p. 187).
- **Limiting factor**: the necessary input that limits the system's activity at a particular moment (p. 187).
- **Bounded rationality**: logic that makes sense in one part of a system but not in the wider context (p. 187).
- **Suboptimization**: a subsystem's goals dominate at the expense of the whole system's goals (p. 188).
- **Resilience**: ability to recover from perturbation. **Self-organization**: ability to structure itself, create new structure, learn or diversify. **Shifting dominance**: relative strengths of competing loops change over time (p. 188).
- Also defined: archetypes, dynamics, hierarchy, system (p. 187–188).

### Summary of Systems Principles (pp. 188–191)
- **Systems.** A system is more than the sum of its parts. Many interconnections work through information flow. Function or purpose is often the least obvious part but the most crucial determinant of behavior. Structure is the source of behavior; behavior shows itself as events over time (p. 188).
- **Stocks and flows.** A stock is the memory of the history of changing flows. A stock can be raised by cutting its outflow as well as by raising its inflow. Stocks act as delays, buffers or shock absorbers and let inflows and outflows be independent (pp. 188–189).
- **Feedback loops.** Balancing loops are sources of stability and of resistance to change. Reinforcing loops lead to exponential growth or runaway collapse. Feedback information can affect only future behavior; it cannot deliver a signal fast enough to correct the behavior that drove the current feedback. A stock-maintaining balancing loop needs its goal set to compensate for draining or inflowing processes; otherwise it falls short of or exceeds the target. Similar feedback structures produce similar dynamics (p. 189).
- **Shifting dominance, delays, oscillation.** Complex behavior often arises as first one loop and then another dominates. A delay in a balancing loop makes oscillation likely (p. 189).
- **Scenarios and models.** System dynamics models ask "what if" questions. A model is useful if it responds with a realistic *pattern* of behavior, not if its scenarios are realistic (pp. 189–190).
- **Constraints.** Exponentially growing physical systems need at least one reinforcing and one balancing loop, because nothing grows forever in a finite environment. Nonrenewable resources are stock-limited; renewable ones are flow-limited (p. 190).
- **Resilience and hierarchy.** There are always limits to resilience. Systems must be managed for resilience, not only productivity or stability. Hierarchies evolve from the bottom up, and the upper layers serve the lower ones (p. 190).
- **Surprises.** Many relationships are nonlinear. There are no separate systems; where to draw a boundary depends on purpose. The most limiting input is the most important at a given time. A quantity growing exponentially toward a limit reaches it surprisingly fast. With long feedback delays, foresight is essential. Each actor's bounded rationality may not serve the whole (pp. 190–191).
- **Mindsets.** Everything we think we know is a model. Models are strongly congruent with the world but fall far short of representing it fully (p. 191).

*Intuition note:* (our reading) The principles above connect through the stock rule: a stock is the memory of its changing flows, feedback loops work by affecting flows, and a delay in a balancing loop makes oscillation likely (p. 189).

### Springing the System Traps (pp. 191–193)
Each entry gives the trap, then the way out.
1. **Policy resistance.** When actors pull the state toward different goals, the result can be policy resistance: any new policy, especially an effective one, pulls the state farther from other actors' goals and provokes more resistance. *Way out:* let go; bring all actors together to find mutually satisfactory goals or larger shared goals (p. 191).
2. **Tragedy of the commons.** Each user gains from use but shares the costs of abuse, so feedback from the resource to users is weak and the resource is overused. *Way out:* educate users and restore the missing feedback by privatizing or by regulating access (p. 191).
3. **Drift to low performance.** Standards that follow past performance, especially with a negative bias, form a reinforcing loop of eroding goals. *Way out:* keep standards absolute, or let them be raised by the best actual performance (pp. 191–192).
4. **Escalation.** Each stock is set by trying to surpass another, giving exponential growth; if nothing is done, the spiral is stopped by someone's collapse. *Way out:* avoid it; refuse to compete, or negotiate balancing loops (p. 192).
5. **Success to the successful.** If winners are systematically rewarded with the means to win again and the loop is allowed to proceed uninhibited, the winners eventually take all while the losers are eliminated. *Way out:* diversification, limits on any one winner's share, levelling the playing field, rewards that do not bias the next round (p. 192).
6. **Shifting the burden to the intervenor.** A solution hides symptoms but does not fix the problem. If it makes the system's own self-maintaining capacity atrophy, a destructive reinforcing loop of dependence starts. *Way out:* avoid symptom-relieving policies; focus on long-term restructuring. An intervenor should restore the system's own ability and then leave. A dependent system should rebuild its capacity at once, since waiting makes withdrawal harder (pp. 192–193).
7. **Rule beating.** Rules lead to behavior that looks compliant but distorts the system. *Way out:* design rules that release creativity toward the rules' purpose (p. 193).
8. **Seeking the wrong goal.** If goals or indicators are defined inaccurately, the system may obediently produce an unwanted result. *Way out:* specify indicators that reflect real welfare; do not confuse effort with result (p. 193).

*Intuition note:* Several traps are described through a loop structure: weak feedback from the resource to users (commons, p. 191), a reinforcing loop of eroding goals (drift, p. 192), a reinforcing loop of dependence (shifting the burden, p. 193). For shifting the burden the author says to move the focus from short-term relief to long-term restructuring (p. 193).

### Places to Intervene (p. 194)
Listed in increasing order of effectiveness, from 12 (least) to 1 (most): 12 numbers (taxes, standards); 11 buffers; 10 stock-and-flow structures; 9 delays; 8 balancing loops (their strength relative to the impacts they correct); 7 reinforcing loops (the gain of driving loops); 6 information flows; 5 rules; 4 self-organization; 3 goals; 2 paradigms; 1 transcending paradigms (p. 194).

### Guidelines for Living in a World of Systems (pp. 194–195)
Fifteen guidelines: get the beat of the system; expose mental models; honor, respect and distribute information; use language with care and enrich it with systems concepts; attend to what is important, not just quantifiable; make feedback policies for feedback systems; go for the good of the whole; listen to the wisdom of the system; locate responsibility within the system; stay humble and a learner; celebrate complexity; expand time horizons; defy the disciplines; expand the boundary of caring; don't erode the goal of goodness (pp. 194–195).

### Model Equations (pp. 195–203)
The models were built in STELLA. The equations are meant to translate into Vensim, STELLA or iThink (p. 195). "Converters" are constants or calculations from other elements. Time is $t$, the time step is $dt$ (p. 195). Every model uses the same update rule:
$$S(t)=S(t-dt)+(\text{inflow}-\text{outflow})\,dt$$

**Chapter One**
- **Bathtub (Figs 5–7).** Initial water 50 gal; $dt=1$ min; 10 min run. Inflow is 0 gal/min for times 0–5 and 5 gal/min for times 6–10. Outflow is 5 gal/min (p. 195).
- **Coffee cooling (Figs 10–11).** $\text{cooling}=0.10\times\text{discrepancy}$, with $\text{discrepancy}=\text{coffee temp}-\text{room temp}$ and room temp $=18^\circ$C. Start at 100, 80, 60°C; 8 min; $dt=1$ min (p. 196).
- **Coffee warming.** $\text{heating}=0.10\times(\text{room temp}-\text{coffee temp})$, added to the stock. Start at 0, 5, 10°C (p. 196).
- **Bank account (Figs 12–13).** $\text{interest added}=\text{money}\times\text{interest rate}$. Start \$100; rates 2, 4, 6, 8, 10% per year; $dt=1$ year; 12 years (p. 196).

**Chapter Two**
- **Thermostat (Figs 14–20).** $dt=1$ hour; runs of 8 and 24 hours. Start at 10°C (cold room) or 18°C (warm room). Thermostat setting is 18°C (p. 197).
  - Furnace heat $=\min(\text{desired-minus-actual discrepancy},\,5)$.
  - Discrepancy $=\max(\text{setting}-\text{room temp},\,0)$.
  - Heat to outside $=(\text{room}-\text{outside temp})\times 10\%$ for a "normal" house and $\times 30\%$ for a very leaky house.
  - Outside temp is constant 10°C in Figs 16–18. Figs 19–20 use a 24-hour cycle between 10°C by day and −5°C at night (graph p. 197).
- **Population (Figs 21–26).** $\text{births}=\text{pop}\times\text{fertility}$, $\text{deaths}=\text{pop}\times\text{mortality}$. Start 6.6 billion; $dt=1$ year; 100 years (pp. 197–198).
  - Fig 22: mortality .009, fertility .021.
  - Fig 23: mortality .030, fertility .021.
  - Fig 24: mortality .009; fertility falls from .021 to .009 (graph p. 198).
  - Fig 26: mortality .009; fertility falls from .021 to .009, then rises to .030 (graph p. 199).
- **Capital (Figs 27–28).** $\text{investment}=\text{annual output}\times\text{investment fraction}$, $\text{depreciation}=\text{capital}/\text{lifetime}$, $\text{annual output}=\text{capital}\times\text{output per unit capital}$. Investment fraction is 20%, output per unit capital is 1/3, lifetime is 10, 15 or 20 years. Start 100; 50 years (p. 199).
  - (added step) Net change per year $=K\left(0.2\cdot\tfrac13-\tfrac1L\right)=K\left(\tfrac1{15}-\tfrac1L\right)$. It is zero for $L=15$, negative for $L=10$ and positive for $L=20$.
- **Business inventory (cars on a lot, Figs 29–36).** Start 200 cars; $dt=1$ day; 100 days (pp. 199–200).
  - Deliveries are 20 for times 0–5, then orders to factory delayed by the delivery delay.
  - $\text{sales}=\min(\text{inventory},\,\text{customer demand})$.
  - Demand is 20 per day for times 0–25 and 22 per day for times 26–100.
  - Perceived sales are sales smoothed over the perception delay. Desired inventory is perceived sales × 10, and discrepancy is desired minus actual inventory.
  - Orders $=\max(\text{perceived sales}+\text{discrepancy},0)$ for Fig 32. For Figs 34–36, orders $=\max(\text{perceived sales}+\text{discrepancy}/\text{response delay},0)$ (p. 200).
  - Delays (perception, response, delivery), in days (p. 200):

| Figure | Perception | Response | Delivery |
|---|---|---|---|
| 30 | 0 | 0 | 0 |
| 32 | 5 | 3 | 5 |
| 34 | 2 | 3 | 5 |
| 35 | 5 | 2 | 5 |
| 36 | 5 | 6 | 5 |

- **Renewable stock with a nonrenewable resource (Figs 37–41).** Resource: $R(t)=R(t-dt)-\text{extraction}\cdot dt$, with $\text{extraction}=\text{capital}\times\text{yield per unit capital}$. Start 1000 (Figs 38, 40, 41); 1000, 2000 and 4000 in Fig 39 (pp. 200–201).
  - Capital starts at 5. $\text{investment}=\min(\text{profit},\text{growth goal})$, $\text{depreciation}=\text{capital}/20$.
  - $\text{profit}=\text{price}\times\text{extraction}-0.10\,\text{capital}$. Growth goal is $10\%$ of capital, or 6, 8, 10, 12% in Fig 40.
  - Price is 3 in Figs 38–40. In Fig 41 it rises from 1.2 to 10 as yield per unit capital falls.
  - Yield starts at 1 when the resource is high and falls to 0 as it declines (graphs p. 201). Run: 100 years (p. 201).
- **Renewable stock with a renewable resource (Figs 42–45).** $R(t)=R(t-dt)+(\text{regeneration}-\text{harvest})dt$. Regeneration $=R\times\text{regeneration rate}$, harvest $=\text{capital}\times\text{yield}$. Start $R=1000$; 100 years (p. 202).
  - Capital rules are as above, but $\text{profit}=\text{price}\times\text{harvest}-\text{capital}$ (p. 202).
  - The price curve is the same as before. Regeneration rate is 0 when the resource is full or empty and peaks near 0.5 mid-range (pp. 202–203).
  - Yield falls non-linearly as the resource falls. It is least efficient in Fig 43, slightly more in Fig 44, and most in Fig 45 (p. 203).

*Intuition note:* In each model the stock changes by flows × time step. The models differ in what each flow depends on, for example a discrepancy (coffee cooling, thermostat), the stock itself (bank interest), or a smoothed signal (perceived sales) (pp. 196–200).

## Toy example (ours, not from the text)
A cup at 40°C in a 20°C room, cooling $=10\%$ of discrepancy, $dt=1$ min (same structure as the coffee model).
- t=0: discrepancy $=40-20=20$; cooling $=0.10\times20=2$; new temp $=40-2=38$.
- t=1: discrepancy $=18$; cooling $=1.8$; new temp $=36.2$.
- t=2: discrepancy $=16.2$; cooling $=1.62$; new temp $=34.58$.

The drops shrink (2, 1.8, 1.62). This shows a balancing loop approaching its goal. Contrast a reinforcing loop: \$100 at 10% gives interest 10, so \$110, then interest 11, so \$121. Here the flow grows with the stock.

## Concepts
- [[feedback]] — a closed chain from a stock, via decisions, back to a flow changing that stock (p. 187)
- [[negative (balancing) feedback]] — stabilizing, goal-seeking loop that opposes imposed change (p. 187)
- [[positive (reinforcing) feedback]] — amplifying loop giving exponential growth or runaway collapse (pp. 187, 189)
- [[delay (dead time)]] — in a balancing loop it makes oscillation likely (p. 189)
- [[reference (set point)]] — the loop's "goal" (e.g. thermostat setting 18°C), used loosely here (pp. 189, 197)
- [[stock-and-flow]] (new) — stock accumulates inflows minus outflows; it is the system's memory (pp. 187–188)
- [[dynamic equilibrium]] (new) — stock steady because inflows equal outflows (p. 187)
- [[shifting dominance]] (new) — relative strength of competing loops changes over time (p. 188)
- [[resilience]] (new) — ability to recover from perturbation (p. 188)
- [[bounded rationality]] (new) — logic that makes sense within one part of a system but not in the wider context; each actor's version may not serve the whole (pp. 187, 191)
- [[system traps]] (new) — recurring structures such as policy resistance, with remedies (pp. 191–193)
- [[leverage points]] (new) — twelve ranked places to intervene (p. 194)

## Canonical instances
- [[bathtub]] (new) — stock with step change in inflow (p. 195)
- [[coffee-cup-cooling]] (new) — balancing loop toward room temperature (p. 196)
- [[bank-account-interest]] (new) — reinforcing loop, exponential growth (p. 196)
- [[thermostat-house]] (new) — balancing loop with capped furnace and heat leak (p. 197)
- [[car-dealer-inventory]] (new) — balancing loop with perception, response, delivery delays (pp. 199–200)
- [[tragedy-of-the-commons]] (new) — shared resource with weak feedback (p. 191)

## Bridges (candidates)
- [structural-analogy] balancing loop with discrepancy ↔ control theory: negative feedback on error signal = reference − output. The thermostat's discrepancy is an error signal, but it is floored at 0 and the furnace heat is capped at 5 (p. 197).
- [structural-analogy] delay in a balancing loop causes oscillation ↔ control theory: delay as a cause of overshoot and oscillation.
- [same-math] stock update $S(t)=S(t-dt)+\text{net flow}\cdot dt$ ↔ numerical (Euler) integration of a differential equation — the same step rule.
- [metaphor] "goal drift" (eroding standards) ↔ a controller whose reference moves toward the output.

## Questions this raises
- Why does a delay in a balancing loop produce oscillation, and how does the car-dealer table (perception 5 vs 2 days; response 2 vs 6 days) show it?
- Are leverage points really ordered by effectiveness, and could a numbers change ever beat a rules change?
- How does the thermostat's cap of 5 on furnace heat change the closed-loop behavior compared with an uncapped loop?
- Which trap would show up in a social-science dataset you know, and what is its missing or misplaced link?

## Reading notes
- Printed page = pdf − 17 (pdf 204 = p. 187). Running header on pages: "TIS final pgs".
- Text layer matched the images. The graphs (outside temperature, fertility, price, yield, regeneration) appear only as curves; values are read qualitatively.
- Misprints in the source: "also know as" (p. 187). The nonrenewable model says growth goal "for Figures 30–40" (p. 201); Fig 30 belongs to the inventory model, so 38–40 was probably meant (my inference). Fig 32's order formula omits response delay, though 3 days is listed for it (p. 200). The renewable model's profit subtracts capital, while the nonrenewable one subtracts 10% of capital (pp. 201–202).
- The Figures (5–45) themselves are not in these pages.
- The appendix does not label the model instances as balancing or reinforcing; those labels in Canonical instances are our reading of the equations.
