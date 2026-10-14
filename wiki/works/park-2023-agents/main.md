---
id: park-2023-agents/main
work: park-2023-agents
unit: paper
pages: pdf 1–22 (printed page numbers not visible; see Reading notes)
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Generative Agents: Interactive Simulacra of Human Behavior

## L0 — One line
Wrapping a language model in a natural-language memory stream with scored retrieval, reflection and planning yields simulated characters that behave believably over days and show emergent social behaviour.

## L1 — The gist (≤ 120 words)
How can language models drive believable, long-lived simulated people? The authors build an architecture around ChatGPT: a natural-language memory stream, retrieval scored by recency, importance and relevance, periodic reflection, and recursive planning. Twenty-five agents live in a Sims-like town, Smallville. In an interview-based test, 100 human raters judged the full architecture more believable than ablations and a crowdworker baseline. Over two game days, information spread, relationships formed, and a party was coordinated from a seeded party intent. Errors included failed retrieval, memory embellishment and overly formal, agreeable speech.

**Prerequisites:** prompting a chat LLM; embeddings and cosine similarity; exponential decay; min-max scaling; basic graph density; rank-based statistics (Elo-style ratings, Kruskal-Wallis).

## L2 — Key ideas (5–10 bullets)
- **Problem:** a bare LLM can act plausibly at one moment, but long-term coherence needs memory that grows, is retrieved selectively, and is generalised. The full memory does not fit the context window and may distract the model (pdf 2, pdf 8).
- **Memory stream:** a list of natural-language memory objects (observations, reflections, plans) with timestamps. Everything in the architecture is recorded and reasoned over as text (pdf 8).
- **Retrieval:** a weighted sum of min-max-normalised recency (decay 0.995 per game hour), LLM-rated importance (1–10) and embedding cosine relevance. All weights are 1, and top-ranked items that fit the context window go in the prompt (pdf 9).
- **Reflection:** triggered when recent importance sums exceed 150. The LLM proposes questions, these serve as retrieval queries, and the LLM then writes insights that cite evidence. Reflections can cite reflections, so they form trees (pdf 9, pdf 10).
- **Planning and reacting:** day plan, then hour chunks, then 5–15 minute chunks. At each step the agent decides whether to continue its plan or react; if it reacts, the plan is regenerated from that time (pdf 10, pdf 11).
- **Controlled evaluation:** the full architecture ranked above all ablations (versions with a component switched off) and a crowdworker baseline, on a TrueSkill rating (a score derived from rankings; μ = 29.89 vs 21.21 for the no-memory condition). All pairwise differences were significant except crowdworker vs no-memory baseline (pdf 14).
- **End-to-end evaluation:** over two game days, knowledge of one agent's candidacy rose from 1 to 8 of 25 agents, and knowledge of the party from 1 to 13. Network density (the share of possible agent pairs that know each other) rose from 0.167 to 0.74. Five of the twelve invited agents attended the party (pdf 16).
- **Limits and risks:** retrieval failures, embellishment, misread location norms, and politeness that the authors think may come from instruction tuning (training a model to follow instructions). Cost is high, and the authors flag the risks of parasocial attachment (one-sided emotional bonds with agents), deepfakes and over-reliance (pdf 16–18).

## L3 — Walkthrough

### Abstract and 1 Introduction (pdf 1–3)
- **Goal.** Build "generative agents": agents drawing on generative models to simulate believable human behaviour. Believable means acting consistently with past experience and reacting plausibly to the environment (pdf 2).
- **Gap.** LLMs can simulate behaviour at a single moment, but general agents with long-term coherence need an architecture for constantly growing memories and cascading multi-agent social dynamics (pdf 2).
- **Three components** (pdf 2): (1) the *memory stream*, a long-term natural-language record, with a retrieval model combining relevance, recency and importance; (2) *reflection*, which synthesises memories into higher-level inferences; (3) *planning*, which turns conclusions and environment into high-level plans, then detailed behaviour. Reflections and plans are fed back into the memory stream.
- **Implementation.** The architecture is connected to ChatGPT. It drives 25 agents in a game world; users interact in natural language (pdf 2). The authors claim that telling one agent she wants to throw a party suffices, whereas a traditional game would need manual scripting of tens of characters (pdf 2).
- Footnote 1: "going to places" is shorthand. The agents' behaviours, like animated Disney characters, aim at believability but do not imply genuine agency (pdf 2).
- **Two evaluations** (pdf 3): a controlled one and an end-to-end one over two game days. Ablations limit access to memory, reflection and planning. The most common errors were failure to retrieve relevant memories, fabricated embellishments, and overly formal speech inherited from the LLM.
- **Contributions** (pdf 3): the agents; the architecture; two evaluations that "establish causal effects" of components and show breakdowns; and a discussion of opportunities and risks.

### 2 Related work (pdf 3–4)
- **2.1 Human-AI interaction.** The authors situate the work among interactive machine learning, prompt-based authoring, and language/agent-based interaction (SHRDLU, ELIZA). They say it "reopens the door" to questions about cognitive models (GOMS, KLM), prototyping tools and ubiquitous computing (pdf 3).
- **2.2 Believable proxies.** Believable agents give an "illusion of life", like Disney characters. Game worlds serve as testbeds (pdf 3). Rule-based approaches (finite-state machines, behavior trees) rely on manual authoring and cannot perform procedures that were not scripted. Reinforcement learning has succeeded mainly in adversarial games with definable rewards (pdf 4). Cognitive architectures (e.g. SOAR, ICARUS) kept short- and long-term memories and ran perceive-plan-act cycles, but their actions were limited to manually crafted procedures and they were deployed mostly in non-open-world settings (pdf 4). The authors' argument is that LLMs offer an opportunity to re-examine this, *provided* an effective architecture synthesises memories into behaviour (pdf 4).
- **2.3 LLMs and behaviour.** LLMs encode a wide range of human behaviour; with narrow context they can generate believable behaviour. The existing literature largely relies on "first-order" templates (few-shot, chain-of-thought) conditioned on the current environment (pdf 4). Believable agents also need conditioning on a vast past, which is a poor fit with first-order prompting and currently impossible because of context-window limits (pdf 4). Prior attempts add a static knowledge base with retrieval, or simple summarisation. This paper extends these ideas to dynamically updated memory mixed with current context and plans, which may either reinforce or contradict one another (pdf 4).

### 3 Generative agent behaviour and interaction (pdf 4–7)
- **3.1 Avatar and communication.** 25 agents live in Smallville. Each has one authored paragraph (occupation, relationships). Each semicolon-delimited phrase becomes an initial memory (pdf 5). The example is the John Lin description, which lists family and neighbours.
- **3.1.1 Inter-agent communication.** At each time step an agent outputs a natural-language statement of its current action (e.g. that Isabella is writing in her journal). This is translated into movement, and an LLM also converts it into emojis shown over the avatar (pdf 5). Agents talk in full natural language. The architecture decides whether they walk by or converse (pdf 5). Footnote 3: the style can feel overly formal, "likely" because of instruction tuning (pdf 5).
- **3.1.2 User controls.** The user speaks as a stated persona (e.g. a "reporter"). To command an agent directly, the user speaks as its "inner voice", which makes the agent "more likely" to treat it as a directive. Told, as John's inner voice, that he is going to run against Sam, John decides to run and shares his candidacy with his wife and son (pdf 6).
- **3.2 Environment.** Smallville has a cafe, bar, park, school, dorm, houses and stores, with subareas and objects (Figure 2, pdf 5, pdf 6). Users can enter as an agent, which others treat like any other agent (pdf 6). Users can rewrite object states in natural language, e.g. a command stating that the stove in Isabella's kitchen is burning. Isabella notices and turns off the stove. A "leaking" shower leads her to fetch tools and try to fix the leak (pdf 6).
- **3.3 A day in the life.** John wakes at 7 a.m., does his morning routine, and talks with Eddy before Eddy leaves. When Mei asks about Eddy, John recalls the conversation. John opens the pharmacy by 9 a.m. (pdf 6). Figure 3's caption says John wakes "around 6 am" (pdf 7).
- **3.4 Emergent social behaviours.** The authors describe these as emergent rather than pre-programmed (pdf 6).
  - *Information diffusion:* Sam tells Tom about his mayoral candidacy. Later Tom and John, who heard the news from another source, discuss it (pdf 6, pdf 7).
  - *Relationship memory:* Sam meets Latoya in the park. Later he asks about her photography project, so the earlier meeting is remembered (pdf 7).
  - *Coordination:* Isabella is initialised with the intent to hold a Valentine's Day party (14 Feb, 5–7 p.m.). She invites people, decorates, and enlists Maria. Maria (whose description includes a crush on Klaus) invites Klaus. Five agents arrive on the day (pdf 7). The user set only Isabella's intent and Maria's crush. The rest was initiated by the architecture (pdf 7).

### 4 Generative agent architecture (pdf 8–11)
Agents take current environment and past experiences as input and output behaviour (pdf 8). The implementation uses gpt3.5-turbo (ChatGPT). The authors expect the basics (memory, planning, reflection) will probably stay the same as models improve. GPT-4's API was invitation-only at the time (pdf 8).

**4.1 Memory and retrieval.**
- *Challenge:* summarising all of Isabella's experiences into the context window gave an uninformative answer to the question of what she is passionate about these days. Retrieving relevant memories instead gave a specific answer (welcoming people, planning events, the Valentine's party) (pdf 8).
- *Memory stream:* a list of memory objects, each with a natural-language description, a creation timestamp and a most-recent-access timestamp. The basic element is an *observation*, an event directly perceived (e.g. the refrigerator is empty) (pdf 8).
- *Retrieval function:* takes the current situation and returns a subset of the stream (pdf 8). Three components (pdf 9):
  - **Recency:** exponential decay over sandbox game hours since the memory was last retrieved, decay factor 0.995.
  - **Importance:** the LLM is asked to rate "poignancy" on a 1–10 scale (1 = mundane, e.g. brushing teeth; 10 = extremely poignant, e.g. a break up). The prompt returned 2 for cleaning up the room and 8 for asking your crush out on a date. It is generated when the memory object is created.
  - **Relevance:** relative to a *query* memory. The LLM gives an embedding of each memory's text, and relevance is the cosine similarity between memory and query embeddings.
- *Final score:* recency, relevance and importance are min-max normalised to $[0,1]$ and combined:

$$score = \alpha_{recency}\cdot recency + \alpha_{importance}\cdot importance + \alpha_{relevance}\cdot relevance$$

  All $\alpha$ are set to 1. The top-ranked memories that fit in the context window go in the prompt (pdf 9).
- *Author's example (Figure 6, pdf 9):* for the question about what she is looking forward to most right now, memories score 2.34 = 0.91 + 0.63 + 0.80 (Valentine's party), 2.21 = 0.87 + 0.63 + 0.71 (ordering decorations), 2.20 = 0.85 + 0.73 + 0.62 (researching ideas), as (recency + importance + relevance). Isabella answers that she looks forward to the party.

*Intuition note:* retrieval is a ranking step that decides which few memories the LLM sees. Recent, important and topically close memories are favoured; the three signals are added with equal weights.

**4.2 Reflection.**
- *Challenge:* with only raw observations, agents struggle to generalise. Asked whom Klaus would spend an hour with, observation-only memory picks Wolfgang (most frequent contact, but only passing encounters). A reflection that Klaus and Maria share a research passion makes him choose Maria (pdf 9, pdf 10).
- *Trigger:* reflections are generated when the sum of importance scores of the latest perceived events exceeds 150. In practice agents reflected roughly two or three times a day (pdf 10).
- *Step 1, what to reflect on:* prompt the LLM with the 100 most recent records, asking for the 3 most salient high-level questions that can be answered about the subjects of those statements (pdf 10).
- *Step 2:* use each question as a retrieval query, gathering memories including other reflections.
- *Step 3:* prompt the LLM with numbered statements, asking for 5 high-level insights, each written with the numbers of the supporting statements (example format: insight (because of 1, 5, 3)) (pdf 10). Example output: Klaus Mueller is dedicated to his research on gentrification (because of 1, 2, 8, 15). The statement is parsed and stored with pointers to the cited memories (pdf 10).
- Reflections can cite other reflections, so agents build trees. Leaves are observations and higher nodes are more abstract (Figure 7, pdf 10).

*Intuition note:* reflection turns many low-level events into a few stored conclusions, which can then be retrieved like any memory. This may let later decisions use a generalisation rather than raw frequency.

**4.3 Planning and reacting.**
- *Challenge:* prompting only for the action at the current moment gives implausible sequences. Klaus would eat lunch at 12, 12:30 and 1 pm. "Optimizing for believability in the moment sacrifices believability over time" (pdf 10, pdf 11).
- *Plan format:* location, start time and duration. Plans are stored in the memory stream and retrieved like other memories. Agents may change plans midstream (pdf 11).
- *Top-down generation* (pdf 11): (1) prompt with the agent's summary description (name, traits, recent experience) plus a summary of the previous day, giving a day plan of five to eight chunks. For Eddy: wake at 8:00, classes at 10:00, composition 1:00–5:00 pm, dinner 5:30, bed by 11. (2) Decompose into hour-long chunks. (3) Decompose into 5–15 minute chunks, e.g. 4:00 pm snack, 4:05 short walk, 4:50 clean up. The plan is saved to the memory stream. The granularity can be adjusted.

**4.3.1 Reacting and updating plans.** At each time step, agents perceive and store observations. The LLM is prompted with the summary description, the time, the agent's status, the observation, and a summary of relevant context retrieved from memory. It is asked whether to continue the plan or react (pdf 11). The context summary comes from two retrieval queries: one about the observer's relationship with the observed entity, and one built from the observed entity's current action status (pdf 11). In the example, John sees Eddy walking and may ask about his composition. The plan is then regenerated from the time of the reaction. If the reaction is an inter-agent interaction, dialogue is generated (pdf 11).

**4.3.2 Dialogue.** An utterance is generated by conditioning on the summarised memory about the other agent plus the intended reaction (and, for replies, the dialogue history). John asks Eddy how the music composition project for his class is going. Eddy retrieves his own memories and replies. This continues until one agent ends the dialogue (pdf 11, pdf 12).

### 5 Sandbox implementation (pdf 12–13)
- Built with the Phaser web game framework. A server keeps a JSON structure per agent (location, current action description, object being used). Each step it applies agents' changes, moves them, and updates object states. It also sends agents and objects within a preset visual range to each agent's memory (pdf 12).
- *Initialisation:* the semicolon-delimited description is split into initial memories (pdf 12).
- **5.1 Grounding in natural language.** The world is a tree (root, areas, objects) where edges mean containment. A stove that is a child of the kitchen becomes a sentence saying there is a stove in the kitchen (pdf 12). Each agent keeps its own subgraph, which it updates as it perceives areas. Agents "are not omniscient" and the tree may go out of date (pdf 12).
- *Choosing action locations:* starting at the root, the LLM is prompted recursively to pick the most suitable area, then sub-area, until a leaf. The prompt includes an instruction to prefer the current area if the activity can be done there. Eddy's walk resolves to The Lin family's house: garden: house garden. Traditional path algorithms then animate the move (pdf 12, pdf 13).
- *Object states:* when an agent acts on an object, the LLM is asked how the state changes, e.g. the coffee machine goes from "off" to "brewing coffee" (pdf 13).

### 6 Controlled evaluation (pdf 13–15)
- **6.1 Procedure.** Agents are "interviewed" in natural language. Five categories × five questions probe self-knowledge, memory, plans, reactions and reflections (e.g. a reaction question about a burning breakfast) (pdf 13). Agents were sampled from the end of a two-game-day full-architecture simulation. 100 evaluators were within-subjects and watched a replay of a random agent's life with access to its memory stream. For one random question per category they ranked the believability of five conditions' answers from most to least believable (pdf 13).
- **6.2 Conditions** (pdf 13, pdf 14): full architecture; *no reflection*; *no reflection, no planning* (observations only); *no observation, no reflection, no planning* (no memory-stream access; the authors say this effectively represents the previous state of the art for LLM-based agents); and a human crowdworker condition. Each of the 25 agents had a unique crowdworker who watched the replay, inspected the memory stream and role-played the answers. This is a baseline of basic competency, not maximal human performance. Four crowdworker sets failed a quality check by the first author and were regenerated (pdf 14). Ablations were given equivalent access to all memories accrued in the full run. The authors say this makes the differences "likely" a conservative estimate, because re-simulation would diverge (pdf 13).
- **6.3 Evaluators.** US-based, English-fluent, older than 18, recruited from Prolific, paid \$15/hour, about 30 minutes. Demographics: 25 female, 73 male, 2 non-binary (pdf 14).
- **6.4 Analysis.** Ranks were converted to interval data with TrueSkill (a generalisation of Elo to multiplayer settings), giving a mean $\mu$ and standard deviation $\sigma$ per condition. Equal ratings mean roughly a toss-up (pdf 14). Significance: Kruskal-Wallis on raw ranks, then Dunn post-hoc tests with Holm-Bonferroni correction. The first author also did qualitative open coding (pdf 14).
- **6.5.1 Results** (Figure 8, pdf 14): full architecture $\mu=29.89,\ \sigma=0.72$; no reflection $26.88,\ 0.69$; no reflection or planning $25.64,\ 0.68$; crowdworker $22.95,\ 0.69$; no observation, planning or reflection $21.21,\ 0.70$. TrueSkill models skill as $\mathcal{N}(\mu,\sigma^2)$, so Cohen's $d$ is available. Full vs the prior-work condition gives $d=8.16$, "eight standard deviations". Kruskal-Wallis: $H(4)=150.29,\ p<0.001$. All pairwise Dunn differences were significant ($p<0.001$) except crowdworker vs fully ablated baseline, the two worst (pdf 14).
- **6.5.2 Remember, with embellishments** (pdf 15):
  - With memory, Abigail recalls Rajiv. Without observational memory she denied knowing him.
  - *Retrieval failures:* Rajiv said he had not followed the election, despite having heard of Sam's candidacy. Tom retrieved the plan to discuss the election at the party, but not hearing about the party, so he doubted the party existed.
  - *Hallucination:* rarely a complete fabrication. Agents did not affirmatively claim experiences they had not had, but they embellished. Isabella said Sam would make an announcement the next day, though no such plan was discussed. Yuriko described Adam Smith as author of *Wealth of Nations*, drawing on LLM world knowledge.
- **6.5.3 Reflection is required for synthesis.** Without reflection, Maria could not say what to get Wolfgang for his birthday, despite many interactions. With reflection she suggested things related to his interest in mathematical music composition (pdf 15).

*Intuition note:* raters preferred each added component, and the full system beat the human-authored baseline on this believability ranking. The crowdworker baseline was a basic-competence check, so this is not a claim about expert humans.

### 7 End-to-end evaluation (pdf 15–17)
25 agents ran continuously for two game days (pdf 15).

**7.1 Emergent social behaviours.**
- *Information diffusion:* two items, Sam's candidacy and Isabella's party, known initially only to their originators. At the end each agent was asked whether it knew of a Valentine's Day party and who is running for mayor. Responses were labelled yes/no, and each "yes" was checked against the memory stream for hallucination (pdf 15).
- *Relationship formation:* each agent was asked, at start and end, whether it knew of each other agent. A pair counts as related if both know each other. The undirected graph has 25 vertices and mutual-knowledge edges. Network density is

$$\eta = \frac{2\,|E|}{|V|\,(|V|-1)}$$

  where $|V|$ is the number of vertices and $|E|$ the number of edges (pdf 15, pdf 16).
- *Coordination:* count how many agents who heard of the party attended (pdf 16).
- **Results** (pdf 16): candidacy knowledge rose 1 (4%) → 8 (32%); party knowledge 1 (4%) → 13 (52%), with no user intervention and no hallucinated claims among those who claimed to know. Density rose 0.167 → 0.74. Of 453 responses about other agents, 1.3% (n = 6) were hallucinated. The party invitation reached 12 agents besides Isabella (Figure 9). Five of the twelve invited agents attended. Of the seven who did not, three cited conflicts (e.g. Rajiv, busy with his show) and four said they were interested but did not plan to come on the day (pdf 16).
- (added step) For 25 vertices the maximum edge count is $25\cdot 24/2 = 300$, so $\eta=0.167$ is about 50 mutual pairs and $\eta=0.74$ about 222.

**7.2 Boundaries and errors** (pdf 16, pdf 17). Three modes:
1. Larger memory and more known locations make retrieval and location choice harder. Some agents chose less typical places, e.g. the bar for lunch rather than the cafe.
2. Misjudged norms that are hard to express in language. Some agents entered the one-person dorm bathroom while it was occupied. Some entered shops after their ~5 pm closing time. The authors suggest the fix "could likely" be adding norms to location descriptions (e.g. "one-person bathroom").
3. Possible effects of instruction tuning: overly formal speech (Mei and John) and overly cooperative agents. Isabella rarely refused suggestions that did not fit her interests, and over time others' interests shaped hers.

### 8 Discussion (pdf 17–18)
- **8.1 Applications.** Populating social-prototyping forums, VR metaverses, or physical spaces with robots (if paired with multimodal models). Human-centred design: a generative agent as a proxy for "Sal" in a ubiquitous-computing vignette (pdf 17).
- **8.2 Future work and limitations.**
  - Retrieval functions could be fine-tuned.
  - *Cost:* simulating 25 agents for two days cost thousands of dollars in token credits and took multiple days. Parallelisation or purpose-built models are suggested.
  - *Evaluation:* only short timescales, and the crowdworker baseline is not the maximal human performance.
  - *Robustness:* largely unknown. Possible vulnerabilities include prompt hacking, "memory hacking" (a crafted conversation convincing an agent of a past event that never occurred) and hallucination.
  - Imperfections of the underlying LLMs will be inherited; the agents may show biased behaviour or stereotypes and may struggle to behave believably for some subpopulations, particularly marginalised ones. The authors believe that addressing this fundamentally requires improving the underlying LLMs (pdf 17, pdf 18).
- **8.3 Ethics** (pdf 18). Four risks and proposals: (1) *parasocial relationships*: agents should disclose that they are computational and be value-aligned (e.g. not reciprocate confessions of love); (2) *impact of errors*: this paper's game setting makes harms unlikely, and other domains need human-AI design best practices; (3) *deepfakes, misinformation, tailored persuasion*: platforms should keep an audit log of inputs and outputs, which cannot directly prevent misuse but may reduce the likelihood of motivated actors trying; the authors add that building such an architecture oneself is time-consuming (roughly a year in their case), which may deter some actors; (4) *over-reliance*: agents should "never be a substitute for real human input; they should instead be used to prototype ideas early in design.

### 9 Conclusion (pdf 18)
The authors summarise the architecture and say evaluations "suggest" that it creates believable behaviour.

### Appendix A: Architecture optimisations (pdf 21)
- A cached *[Agent's Summary Description]* is synthesised at intervals from three retrievals (core characteristics, current daily occupation, and feeling about recent progress), each summarised by the LLM. Name, age and traits are concatenated with these three summaries (pdf 21).
- Only the high-level plan is generated ahead. The near future is decomposed just in time because plans change. Other possible optimisations: batching dialogue generation, and re-planning that updates only the parts that need it. The system runs sequentially at 1 real second = 1 game minute and could be parallelised across agents (pdf 21).

### Appendix B: Interview questions (pdf 21, pdf 22)
25 questions in five categories (self-knowledge, memory, plans, reactions, reflections), with sample answers from Klaus Mueller. Examples: a plan question about 6am, a memory question about a person Klaus does not recognise (he says he is not sure who that is), and the occupied-bathroom reaction question. Bracketed names in the memory questions are randomly chosen from agents the subject has interacted with; in the reflection questions they are the agents with whom the subject interacted most frequently (pdf 21, pdf 22).

## Toy example
*(Ours, not from the paper.)* Illustrates the retrieval score of §4.1. Query: "What are you looking forward to?" Three memories, $\alpha$'s all 1.

| Memory | Hours since last retrieved | Importance (1–10) | Cosine relevance |
|---|---|---|---|
| A: "ate toast" | 1 | 2 | 0.2 |
| B: "planning the party" | 10 | 8 | 0.9 |
| C: "read old email" | 100 | 5 | 0.5 |

1. Recency $=0.995^{h}$: A $=0.995$; B $=0.995^{10}\approx0.951$; C $=0.995^{100}\approx0.606$.
2. Min-max recency: range $0.995-0.606=0.389$. A $=1$; B $=(0.951-0.606)/0.389\approx0.887$; C $=0$.
3. Min-max importance: range $8-2=6$. A $=0$; B $=1$; C $=(5-2)/6=0.5$.
4. Min-max relevance: range $0.9-0.2=0.7$. A $=0$; B $=1$; C $=(0.5-0.2)/0.7\approx0.429$.
5. Scores: A $=1+0+0=1.00$; B $=0.887+1+1=2.887$; C $=0+0.5+0.429=0.929$.

Ranking B > A > C. If the context window holds only one memory, the party memory is passed to the LLM. The recent but irrelevant "toast" memory ranks second only because of recency.

## Concepts
- [[generative agent]] — an LLM wrapped with memory stream, reflection and planning, simulating a believable individual in a sandbox world (pdf 1, pdf 2)
- [[memory-stream]] (new) — list of natural-language memory objects (observations, reflections, plans) with creation and last-access timestamps (pdf 8)
- [[retrieval-score]] (new) — weighted sum of min-max-normalised recency, importance and relevance; all weights 1 (pdf 9)
- [[reflection]] (new) — periodic LLM-generated higher-level inferences with cited evidence, stored back as memories and forming trees (pdf 10)
- [[agent-planning]] (new) — top-down recursive decomposition of a day plan into hour and 5–15 minute actions, with re-planning on reactions (pdf 11)
- [[believability]] (new) — the dependent variable: human raters' ranking of how believable behaviour is (pdf 13)
- [[ablation]] (new) — conditions that remove access to observation, planning or reflection memory, used to test components (pdf 13)
- [[trueskill-rating]] (new) — Elo-like Bayesian rating converting rank data into $\mu,\sigma$ per condition (pdf 14)
- [[network-density]] (new) — $2|E|/(|V|(|V|-1))$ of the mutual-knowledge graph; the measure of relationship formation (pdf 16)
- [[emergent social behavior]] (new) — information diffusion, relationship formation and coordination arising without scripting (pdf 6, pdf 15)
- [[word embedding]] — here an LLM-generated vector of each memory's text; relevance is the cosine similarity (pdf 9)
- [[context window]] (new) — LLM input limit that motivates selective retrieval over summarising the whole history (pdf 4, pdf 8)
- [[few-shot / chain-of-thought templates]] (new) — "first-order" prompting the authors say conditions only on the current environment (pdf 4)
- [[instruction-tuning-effects]] (new) — possible cause of overly formal speech and over-agreeable agents (pdf 5, pdf 17)

## Canonical instances
- [[valentines-day-party]] — one seeded intent leads to invitations, decorating, dates and five attendees (pdf 7, pdf 16)
- [[klaus-reflection-tree]] — observations about research become a reflection that Klaus is highly dedicated to research (pdf 10)
- [[isabella-passion-retrieval]] — summarising everything gives a vague answer; retrieval gives a specific one (pdf 8)
- [[john-eddy-dialogue]] — observation, reaction, dialogue generation from summarised relationship memory (pdf 11, pdf 12)
- [[agent-interview-evaluation]] — five questions in each of five categories (25 in all), 100 raters ranking five conditions (pdf 13, pdf 14)
- [[tom-party-partial-retrieval]] — an incomplete retrieved fragment gives certainty about plans but doubt the party exists (pdf 15)

## Bridges (candidates)
- [structural-analogy] retrieval-score ranking ↔ information retrieval: ranking documents by combined relevance and other signals — here with an added recency decay.
- [same-math] relevance as cosine similarity of embeddings ↔ distributional semantics: similarity of dense vectors.
- [same-math] network density of mutual-knowledge graph ↔ graph theory/network science: density is edges over possible edges.
- [structural-analogy] reflection tree ↔ hierarchical summarisation: higher nodes abstract lower ones, though here they are generated by a prompted LLM and cite evidence.
- [structural-analogy] interviewing agents ↔ silicon samples and algorithmic fidelity: both use LLM outputs as proxies for human respondents.
- [structural-analogy] ablations removing memory components ↔ mechanistic ablation studies of model components: removing a part to test its causal role.
- [metaphor] memory stream ↔ residual stream: both are running records read from and written to by components. (The first is text and the second a vector.)

## Questions this raises
- How sensitive is believability to the weights $\alpha$ (all set to 1) and to the decay 0.995, which the paper does not vary?
- Do the results hold for longer than two game days, given the authors' own caution on timescale (pdf 17)?
- How much of the "emergent" behaviour comes from LLM world knowledge versus the architecture, since only the full system versus ablations was compared?
- Can memory hacking and instruction-tuned over-agreeableness be reduced without losing believability (pdf 17)?

## Reading notes
- **Page numbers:** the labels give printed numbers only for pdf 4–18 (printed = pdf − 3). The images show no printed numbers, and the other pages are unlabeled. As the unit metadata gives printed pages as unknown, all references here use (pdf N).
- The source carries the arXiv v2 stamp (6 Aug 2023) and a UIST '23 header; the ACM reference format on pdf 2 gives a length of 22 pages.
- Several equation glyphs in the text layer (e.g. $\alpha$, $\mu$, $\sigma$, $\eta$) are garbled. I read them from the page images.
- *Inconsistencies in the source:* Figure 3's caption has John waking "around 6 am", while §3.3 says 7 a.m. §4.3.1 describes Eddy's walk once as in the house garden and once as around his workplace. In the text layer of pdf 17, Mei's closing line (good talking to you as always) begins with "11" where an opening quotation mark would be expected. This is probably an extraction artefact; no image of that page was available to check.
- I could not reproduce $d=8.16$ (pdf 14) from the printed values. The difference of means is 8.68 and the $\sigma$ values are about 0.7, so the paper's formula seems to differ from the simple pooled-$\sigma$ one. The paper does not state it.
- The 453 responses (pdf 16) are not explained further in these pages. Appendix B's 25 questions match §6.1's five questions in each of five categories.
- Reference list (pdf 19–21) and acknowledgments were not digested.
