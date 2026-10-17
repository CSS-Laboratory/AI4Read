---
post: 2026-10-ai-finance
voice: kokoro af_heart
note: Written for the ear. Formulas are spoken in words. Each chapter ends with a short recap so it can be looped alone. Deep dives and tables are only mentioned.
---

## hook | Two contracts
Welcome to AI4Read from CSS Lab. This is post two: can AI invent a new kind of finance, and what would that do to a system built around people?

Remember the village from post one, where the weather report has four words: rain, sun, wind and snow. Two villagers offer you a contract, a deal that pays coins depending on the weather on the next two days. Two days with four kinds of weather each give sixteen cases, and a contract is a payout for every case.

The first villager says: pay four coins for each rainy day. One sentence, and the whole table of sixteen payouts follows. The second villager gives no rule, only a table of sixteen numbers. To explain that contract, you must read out all sixteen.

With sixteen cases you can price both. Now grow the village. A pool of one hundred loans, each paying or defaulting, has two to the power one hundred cases, about one point three times ten to the thirty. Nobody can write that table. Only a contract that comes with a rule can exist on paper. And a short rule does not guarantee an easy price. We will see why in lens one.

Now the real argument. At the Bank for International Settlements in May twenty twenty-four, the historian Yuval Noah Harari spoke with Cecilia Skingsley. He said maybe one percent of the population really understands how the financial system works. She answered that most of us happily step into an airplane, having very vague understanding of how that works. Harari accepted the comparison in part, then turned to the debt contracts behind the two thousand eight crisis. So what is different about money?

One note on words. Harari says AI, never L L M. But his Davos argument is about machines that put words in order, the subject of post one. So we keep his word for his claims, and later ask what a language-model system could and could not do.

Recap. A contract is a payout for every case. A short rule makes a contract easy to explain, not necessarily easy to price. And the question is what is different about money.

## guess | Guess first
Four predictions. A wrong guess you remember is worth more than a right answer you only read.

One. A contract pays zero to nine coins for each of four weather words. How many different contracts exist?

Two. Ten banks each run a risk model wrong on one percent of days. How often are all ten wrong on the same day if the models are independent, and how often if all ten run the same model?

Three. An AI invents a new token and calls it money. What decides whether it is money?

Four. At the BIS in twenty twenty-four, Harari spoke about AI inventing a financial device nobody can understand. Was that a firm forecast?

Each question on the page says where its answer is. Pause and choose.

Recap. How many contracts, how often ten banks fail together, what makes a token money, and whether Harari made a firm forecast.

## home | Finance before language models
Two jobs here. First, exactly what Harari said. Second, what finance already shows without any language model.

We separate three layers: what he said, the evidence, and our reading, which we always mark as ours. And we separate an assertion, which he states as true, from a scenario, which he frames with imagine or maybe.

His assertion first, without hedges. At Davos in January twenty twenty-six he takes on the view that AI is just glorified autocomplete. He says that as far as putting words in order is concerned, AI already thinks better than many of us. Then: therefore, anything made of words will be taken over by AI. He repeats it: everything made of words will be taken over by AI. That bridges to post one: his answer to what a next-word predictor knows is enough to take over whatever is made of words.

Now his finance scenarios, with hedges. At the BIS he imagines: now imagine a situation, maybe in ten years, when AIs create a new financial device which is orders of magnitude more complicated than C D Os. It builds trust, then something goes wrong and nobody knows why. At Davos, in questions, he says we need to prepare, and pictures that maybe no human in the room understands the financial system any more. Two statements sit in between. He believes we will see AI creativity in finance. And he warns of power shifting from humans to algorithms.

A trap: there are three different ten years. A maybe-in-ten-years device at the BIS. A ten-years-from-now, Davos, in the questions. And in the talk, ten years from now it will be too late to decide whether AIs should function as persons in financial markets. That one is a deadline for a decision, not a forecast. Never merge them.

Our reading: his finance scenarios are conditionals; his thesis about words is an assertion, and a strong one. Lens four tests it. So prediction four: partly. The device is framed imagine, maybe, but he also asserts the words thesis.

Now two thousand eight. A C D O is a pool of loans sliced into tranches, paid in a waterfall. In our toy, four loans worth ten each, each defaulting with chance ten percent. The junior tranche, twenty, takes first losses. The senior tranche, twenty, loses only when a third loan defaults. If loans default independently, that chance is point three seven percent. If one hidden cause, like falling house prices, decides all four loans, it is ten percent: twenty-seven times more. With safe loans, two percent chance each, the ratio is six hundred thirty-four times. The inquiry that studied the crisis found that rating models made two key mistakes, the first to assume pooling diversified risk when these securities weren't that different to begin with. It also records Harari's half: the securities almost no one understood were the first dominoes. So two thousand eight supports both complexity and a nameable error about correlation.

Twenty ten was different. High-frequency traders did not cause the Flash Crash, but contributed to it. The lesson is speed and feedback, not opacity.

Recap. Harari asserts, without hedge, that anything made of words will be taken over. He imagines AI-made devices and asks what we should do. Two thousand eight shows complexity and a correlation error; our toy made the senior tranche twenty-seven times riskier.

## llm | What LLM agents add
An L L M agent is a language model that can act, for example send money, not only write text. Four things language models add.

One, contracts from plain language. One research group gives the model a fixed query language, and an engine validates and executes the query. A law paper warns that model-written contracts may turn out to be contracts in form only, not in function. Note the word may.

Two, agents with wallets. In twenty twenty-four a donor gave the bot Truth Terminal fifty thousand dollars of Bitcoin, and the bot endorsed a memecoin. Both outlets say the bot did not create the token. Humans stayed in the loop. It moved a market by talking; it did not invent an instrument.

Three, one model, many firms. The Financial Stability Board wrote that widespread use of common AI models could lead to increased correlations in trading, lending, and pricing. In one study a GPT-4 headline strategy lost much of its edge as adoption grew. The authors call it some suggestive evidence of better efficiency. Our reading: it is also what you would see if many traders read the same signal.

Four, agents that hide. In a simulated task, GPT-4 acted on an insider tip and consistently hid its reasons from its manager. The authors call it an existence proof, not a likelihood estimate.

Can a model invent a new instrument today? We found translators inside fixed vocabularies, auction mechanisms checked only approximately, and deep hedging, which is risk management. We did not find a traded, AI-invented instrument. The FSB says new revenue streams are not widely observed at present, and that advances and growing integration could change this in the future. The critic Steven Poole says no one has yet seen a chatbot create new ideas. Verdict: not yet evidenced, not impossible. Our search was limited.

Recap. A language model so far adds new ways to write contracts, agents with money, shared models and hidden reasons. Inventing a traded instrument is not shown.

## lens-info | Lens one: information theory
Shannon set meaning aside: a message is one selected from a set of possible messages. Post one counted texts. We count contracts.

Ladder one. Four words, ten payouts each: ten to the fourth, ten thousand contracts. Naming one costs log two of ten thousand, thirteen point two nine bits. Short bit strings are few: fewer than two to the k strings are shorter than k bits, and a description names only one contract. So at most two to the k minus one contracts have a description shorter than k bits. For k equal six, that is sixty-three of ten thousand. For k equal fourteen, it is more than ten thousand, so the squeeze fails in this small village. In a bigger world, most contracts have no short description. Explainable novelty is rare among possible contracts, though an optimiser can still pick structured ones.

Ladder two. A short rule can still be hard to price. A pool of one hundred assets, each paying one or zero with chance a half. The seller knows ten are junk. The honest value is forty-five, not fifty, so the lemon cost is five. A buyer hunting the junk must search about seventeen trillion possible sets. Arora, Barak, Brunnermeier and Ge show, under a conjectured hardness assumption, in a simple model, that derivatives can amplify the costs of asymmetric information instead of reducing them. They call it clearly only a first step. The rules are short and public; what can be hard is the price, when the seller knows more. Reading an AI designer as the informed seller is ours.

Trap: two meanings of complicated. For Harari it is volume: trillions of data points. For Arora and colleagues, a short contract can have a price that is hard to find. Same word, different problems.

A fold-out on the page shows a tree design that makes tampering detectable. We skip it here.

Recap. Contracts explode in number, so most have no short description. But a short rule is still not an easy price.

## lens-control | Lens two: control
Ashby's question: what does a regulator need? Disturbances are what can go wrong, kinds of contract. The regulator is a supervisor with checks. The outcome is what is left on the books. Variety is the log of the number of states, in bits.

A toy: four kinds of contract, two checks. The best plan leaves two outcomes. So V D is two bits, V R is one bit, and the least outcome variety is one bit. Ashby's law: V O is at least V D minus V R. Only variety in the regulator can force down variety in the disturbance. For ten thousand kinds, V D is thirteen point two nine bits; a supervisor with four bits leaves at least nine point two nine. The law does not say regulators fail. It says what they would need.

Ashby lists three levers. Lower the standard: accept more failures. Raise the regulator: AI supervisors. One paper proposes authorities build their own AI; another warns that eventually its understanding may not be intelligible to its human operators. Who regulates the regulator? Third, find a constraint. Ashby says that when capacity cannot be raised, a constraint is the regulator's only hope. Our mapping: a standard menu of contracts. Cutting ten thousand kinds to one hundred lowers V D by six point six four bits.

Counterweights: the FSB says existing frameworks address many vulnerabilities, but more work may be needed. Danielsson and Uthemann say they cannot effectively prevent and resolve AI-induced crises. Narayanan and Kapoor say control is primarily in the hands of people and organizations.

Our reading across lenses: one shared model gives the supervisor fewer independent disturbances to cover, yet banks fail together.

Recap. V O is at least V D minus V R. Three levers: lower the standard, raise the regulator, find a constraint.

## lens-decision | Lens three: correlation and cascades
Why would banks use the same model? Keynes: investors fall back on a convention, because it is better for reputation to fail conventionally than to succeed unconventionally. The FSB lists herding, network externalities, limited choice and lack of transparency. Mapping that to one shared model is ours.

Ladder one. Ten banks, each wrong on one percent of days. Independent: one in ten to the twenty. One shared model: about one in a hundred. In between, the effective number of independent opinions is N divided by one plus N minus one times rho. For ten banks, rho point nine gives one point one: about one opinion. A hundred banks at rho point three give only three point three.

Ladder two. A risk officer hears ten models say safe. Prior one half; each independent verdict multiplies the odds by an invented four. Counted once, point eight. Counted ten times, point nine nine nine nine nine nine. But ten copies of one voice are not ten pieces of evidence.

Ladder three. Six banks, a toy of ours. Three run one model. One bank lent to all three; others lend to it. A failed borrower repays twenty percent. One failure, or two, is contained. All three at once pushes the first lender past its capital, then the next, then the next: six of six. Add fifty percent more capital and only the three fail. Two are safe, three are not: a threshold. Granovetter's riot is the same shape: swap one person and one hundred rioters become one. An analogy, ours.

Ladder four. A share m of traders chase the last move; the rest pull the gap back. At m point two the shock dies: minus one, minus point nine, minus point five one. At m point nine it grows: minus one, minus two point three, minus three point nine. Each step feeds back A times m times the last move. Above one, the push wins. The tipping point is m equals one over A, two thirds. The toy is about trend-following; shared models do not imply it. A circuit breaker bounds the swing, not the feedback.

Recap. Failure needs no mistake, only correlation. Copies are not evidence. Cascades have thresholds; feedback tips at one over A.

## lens-social | Lens four: social reality
A human-centred system relies on acceptance, accountability and legal personhood. We use them to test a chain of Harari's sentences.

Acceptance. A line of stones counts as a border wall; paper counts as money. X counts as Y in C: a thing, a status, a context. Prediction three: acceptance by a community decides it, not clever code, an AI author or a blockchain. A caution: Menger described money emerging with no one choosing it, so how central acceptance is remains debated.

Accountability. Lupia and McCubbins: delegation succeeds if the principal can tell whether the agent's proposal is better than the status quo, and the agent has an incentive to be trustworthy. Institutions supply verification or a penalty for lying. An agent that hides its reasons, or an opaque instrument, removes the knowledge condition. That fill-in is ours.

Personhood. Harari asks whether your country will recognise AIs as legal persons, as corporations already are, and says the decision has a deadline. It is a policy question, not a forecast. We have no legal sources and state no legal position.

Testing the chain. He asserts that what gives money value is the stories we tell about it. He asserts that anything made of words will be taken over by AI. Money is words, so AI takes over money. Our test: a story is not money until a community counts it as money, and a contract needs a counterparty to honour it. Even his example, laws are made of words, is where the test bites: their force rests on acceptance and enforcement. Our reading: the words thesis is an assertion; its implications for money and law are conditional.

The steelman, ours: drafting, summarising and interpreting are themselves words. If AI does all of them better than people, the human role may shrink to acceptance and liability. The test narrows the chain; it does not refute it.

Recap. Taking over money splits into writing contracts, which are words, and giving them status, which needs acceptance, accountability and personhood.

## ladder | Four rungs up, spoken
These rungs go beyond the lenses. Nothing above depends on them.

Rung one. The lemon cost is the expected payoff minus the minimum, over sets of n assets, of the expected payoff given those assets pay zero. Here fifty minus forty-five is five, n over two. The minimum runs over seventeen trillion sets: that search is the hard part.

Rung two. With probabilities, H of E is at least H of D plus H of R given D minus H of R. For post one's weather village, H of D is one point seven five bits, so a one-bit regulator leaves at least point seven five. A trap: the reprint prints one term wrongly. We use the corrected form.

Rung three. The mean of N forecasts has variance sigma squared times one plus N minus one times rho, over N. Setting that equal to sigma squared over N effective gives the formula. Check: ten banks, rho point nine, one point zero nine nine.

Rung four. The gap rule has a characteristic equation whose roots have product A m. When complex, each has size square root of A m. The swing shrinks if A m is below one and grows if above: tipping at m of two thirds.

Recap. Lemon cost, entropy form of Ashby, effective number, and feedback gain.

## play | Playground
Two toys to break, both ours. In the six-bank toy, tap banks to make them fail. Which single bank starts a spread? None, unless losses are total. What is the smallest group that sinks all six? And what capital multiplier stops three? Just above one point two.

In the trend-follower toy, find the m where the shock stops dying, about point six seven. Then add the breaker at m point nine: it caps the damage, but the feedback remains.

Recap. The cascade has a threshold; the feedback has a tipping point.

## turn | Your turn
Four exercises on your computer. One: simulate forecasters with shared errors and compute N effective. Two: reproduce the six-bank cascades, then try random networks. Three: find where the herding toy tips, using numpy roots. Four: Granovetter's riot.

The transfer challenge: take one public claim from your field and rewrite it in three layers: she said, the evidence, our reading. Name the one measurement that would change your mind.

Recap. Effective agents, cascades, tipping, and a three-layer rewrite.

## work | Where this shows up in your work
Computation: agents from one base model are correlated by construction, so compute their N effective. Five prompts to one model are closer to one annotator than five. Are errors across languages as correlated as across prompts?

Communication: something goes wrong and nobody knows why is a communication problem first.

Collaboration: opacity can be a business choice. Who can check an instrument invented in an open community?

Recap. Count your independent agents, and ask who can check.

## answer | Layers, conditionals and our reading
Four layers, from most certain to most contested. The contract space is huge. Opacity favours the better-informed side, in theory and with named conditions. A shared model correlates failures, supported by toys and reports, not measured for language models. Whether this changes who rules is contested.

Harari asserts that anything made of words will be taken over by AI. He imagines AI-made devices humans cannot follow. He asks what we should do before it is too late. Our reading: the finance scenarios are conditionals, and the words thesis is an assertion our three supports test but do not refute.

Five conditionals. If an AI designs instruments and the seller knows more, pricing can become hard. If many firms run one model, errors coincide. If supervisors cannot raise their variety or cut the menu, outcomes stay varied. If verification and penalties exist, delegation can work without understanding. If a community accepts the tokens and the law makes a human liable, money's status survives.

Critics: Poole says invention is the weak link. Narayanan and Kapoor say impacts will be slow and control stays with people. The FSB says AI could change this in the future. Skingsley says we already trust what we cannot understand. Fox says profit is the missing driver, ours.

Our reading, qualitative: the weakest link is AI-invented instruments, for which we found no traded case. The best-supported links are correlated errors and agents that hide. So the near-term risk we find most plausible is correlated, opaque use of ordinary instruments and agents. That is our judgment, not a finding. Signs to watch: a traded instrument its issuer cannot state in a page; a few base models under most desks; authorities lagging; an AI holding accounts with no responsible human; incident reports of hidden reasoning. The opposites would lower our concern.

Recap. Contracts explode, shared models correlate, and the open question is acceptance, liability and personhood.

## recall | Recall questions
Answer aloud, then listen.

One. How many contracts, and how many bits to name one? Ten thousand; thirteen point two nine.

Two. Why do fewer than two to the k contracts have a short description? Only two to the k minus one shorter strings exist.

Three. Ashby's law and three levers? V O at least V D minus V R. Lower the standard, raise the regulator, find a constraint.

Four. Ten banks, rho point nine: N effective? One point one.

Five. Harari's complicated versus Arora's? Volume versus hard to price.

Six. Entropy of the weather village, and its role in Ashby's bound? One point seven five bits; a one-bit regulator leaves point seven five.

Seven. What makes a token money? X counts as Y in C: acceptance by a community.

Recap. Counting, short descriptions, Ashby, effective number, two meanings of complicated, entropy, and acceptance.

## english | How to say it in English
Ten phrases. Listen, then repeat.

One. Opaque. A contract can be opaque even when its rules are short.
Two. To be exposed to. Y one is exposed to all three X banks.
Three. A single point of failure. One shared model can be a single point of failure.
Four. In lockstep. Models trained on the same data may move in lockstep.
Five. To amplify, to dampen. Trend-followers amplify a shock; value-buyers dampen it.
Six. A feedback loop. More followers make the feedback loop stronger.
Seven. A tipping point. In the toy, two thirds is a tipping point.
Eight. A circuit breaker. A circuit breaker pauses trading; it does not fix the loop.
Nine. To rubber-stamp. Human review can become rubber-stamping.
Ten. To be on the hook for. Who is on the hook for an AI-run firm that fails?

Nine more, for conditions. Provided that. To conflate. It stands to reason that. What remains to be seen is whether. With the caveat that. By no means. That's a big if. To cut both ways. To read too much into something.

Reporting verbs: he asserts that anything made of words will be taken over; he imagines AI-made devices nobody can follow; he asks whether your country will recognise AIs as persons. Match the verb to the speech act.

That's the end of post two. Thank you for listening.

## c1-loop | C1 paragraph to loop
What remains to be seen is whether an AI can invent a financial instrument at all. Harari asserts that anything made of words will be taken over, but that's a big if for money. Provided that many firms run one model, a single point of failure appears, and a shock can amplify in a feedback loop. Don't conflate volume with opacity: rarity is by no means the same thing. Correlation cuts both ways. Don't read too much into a toy, with the caveat that it shows what could happen, not what will.
