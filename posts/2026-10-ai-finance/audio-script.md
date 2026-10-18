---
post: 2026-10-ai-finance
voice: kokoro af_heart
note: Version 2 (2026-10-18), re-centred on an AI-automated society. Written for the ear. Formulas are spoken in words. Each chapter ends with a short recap so it can be looped alone. Fold-outs and tables are only mentioned. The post stands alone and never refers to another post.
---

## hook | Five seconds in 2010
Welcome to AI4Read from CSS Lab. This is post two: could a society run itself on AI?

Start with five seconds. A futures contract is a promise to buy or sell something at a fixed price on a later date. Selling stock-index futures is a way to protect yourself if stock prices fall. On the afternoon of the sixth of May, twenty ten, a large fund company began to sell such contracts, worth about four point one billion dollars, for exactly that reason. It chose to run the sale through an automated execution algorithm, set to sell a fixed share of recent trading volume, without regard to price or time.

Prices fell fast. By two forty-five, the buy orders waiting in the market were less than one percent of their level at the start of the day. Then a rule fired. The exchange's Stop Logic, an automated safeguard, paused trading for five seconds. Nobody pressed a button. People had set the rule and its limits in advance. The rule exists to prevent a cascade of further price declines, and the regulators' report, as the paper quotes it, says prices stabilised after the pause. The quoted passage does not say the pause caused this, and the paper does not test it. About twenty minutes later, the index future was back near where it started.

Look at who did what. A firm decided to sell. Software ran the selling and the matching. A pre-set rule did the checking: it paused trading. Afterwards, regulators studied what happened.

The historian Yuval Noah Harari pushes the picture further. At Davos in twenty twenty-six he stated it flatly: anything made of words will be taken over by AI, and if laws are made of words, then AI will take over the legal system. Contracts and money are made of words too; that extension is ours. At the Bank for International Settlements in twenty twenty-four, he imagined an AI-made financial device that no human understands, maybe in ten years. A fold-out on the page lists all of his lines that we use, sorted by how firmly he said them.

Our question. What if nobody had set that rule, and nobody could? Could a society run itself on AI, with no human intervention at all?

One term. In this post, an AI-automated society is a society in which AI systems do every job that keeps it going: running the work, deciding, checking, declaring what counts, and answering for losses, with no person needed at any step, neither while it runs nor in writing its rules.

A preview, which is our reading. Much of the running is automated; the rules are not. Declaring needs acceptance and answering needs consequences; whether machines can supply either is the open part. Section thirteen has the short answer.

Recap. In twenty ten, software ran a crash and a pre-set rule paused it. Harari says anything made of words will be taken over by AI. Our question is whether a society could run with no human at all.

## guess | Guess first
Four predictions. A wrong guess you remember is worth more than a right answer you only read.

One. About seventy percent of US stock trading is algorithmic. What does that tell you about AI?

Two. Ten banks each run a risk model that is wrong on one percent of days. How often are all ten wrong on the same day if the models are independent, and how often if all ten run the same model?

Three. An AI mints a token and pays other AIs with it. No human ever uses it or thinks about it. Is it money?

Four. Ten banks. In plan A, each holds one different asset. In plan B, each holds a tenth of every asset. Each bank is safer in plan B. Is the system safer?

Each question on the page says where its answer is. Pause and choose.

Recap. What seventy percent algorithmic means, how often ten banks fail together, whether a machine-only token is money, and whether safer banks make a safer system.

## home | The five jobs of a society
"Fully automated" is vague until we say what is automated. Here is our framework. Any social system, from a village market to a stock exchange, does five jobs.

Run: carry out the work, like matching orders and moving money. Decide: choose what to do, like what to buy and how much. Check: verify and regulate, like circuit breakers and supervisors. Declare: say what counts, like what is money, a valid contract, or a legal person. And answer: bear the losses and be held responsible.

Why these five? They follow one decision from start to finish: done, chosen, verified, counted, paid for. Setting goals is the top level of deciding, and enforcing a rule is part of declaring and answering.

Two distinctions matter. A person can step in while the system runs, by pressing a button or approving a trade. Or a person can step in before it runs, by writing its rules and limits. The twenty ten pause had no intervention at run time, but plenty at design time. This post asks whether AI could remove both.

And by a society we mean, in our own words, a group whose members can rely on shared rules, can contest them, and can find someone answerable when things go wrong.

We leave the physical side of society, energy, food, transport and repair, out of scope. Finance is among the places where automation has gone furthest, in our judgement, so it is a good place to look for the limits. Where does finance stand today? Much of the evidence comes from the International Monetary Fund, the IMF, which surveyed and interviewed market participants in twenty twenty-four.

Run is largely automated at run time in some markets, on rules written by people. The index future of twenty ten trades on a fully electronic market with no market-maker obligations. In the US, algorithmic trading is about seventy percent of stock trading and more than half of futures trading, says the IMF.

Decide is mostly not automated. On algorithmic trading the IMF finds the evidence mixed; on AI, there is evidence that sophisticated AI has not yet been widely used to build autonomous trading agents. It is more often used to feed a signal into a system where a human trader may make the final decision. All participants in the IMF's outreach expected a human in the loop to persist in the near term, three to five years, especially for large decisions. Participants also expect more AI in investment and trading decisions over the same horizon.

Check is automatic at run time, but designed by people. A pre-set rule paused trading during the twenty ten crash, and supervisors use AI-driven tools.

Declare is human: what counts as money or a valid trade rests on people accepting it. And answer is human: in the IMF's words, institutions are responsible for the AI systems they deploy.

So, prediction one. Algorithms execute about seventy percent of US stock trading, but that includes simple rules. The IMF defines algorithmic trading as an algorithm that independently executes trading decisions, which in its simplest form can be basic trading rules. Running is not deciding.

Now the last big crisis, two thousand eight, which shows two failures of the check job with human-made products. A C D O, a collateralised debt obligation, collects many debts into one pool and pays investors in a fixed order. Each place in the order is a tranche. The first paid is safest; the last paid takes the first losses. The government inquiry into the crisis records two failures: securities almost no one understood, and rating models whose first of two key mistakes was to assume pooling diversified risk, when in fact these securities weren't that different to begin with. Lens two turns the second failure into a toy.

Recap. Five jobs: run, decide, check, declare, answer. In markets today, running is largely automated, deciding mostly is not, checking is partly automatic, and declaring and answering are human.

## llm | What AI agents add
Many market algorithms are still fixed rules, though the IMF finds the evidence mixed. The new element is the large language model, and the language-model agent: a model that can act, call tools and move money, not only write text. What does it add to each job, and how far has it got?

Run and decide: contracts from plain language. An option is a contract whose payout depends on where a price ends on a set date. Language models find it hard to turn a trader's plain words into correct option strategies, so one research group gives the model a fixed query language, a small set of allowed commands, like the boxes on a form. An engine then checks and executes the query. A law paper warns that contracts written by language models may turn out to be contracts in form only, not in function.

Answer: an agent with a wallet. Truth Terminal is a bot on X. Its human handler approves its posts. In July twenty twenty-four, the investor Marc Andreessen sent fifty thousand dollars' worth of Bitcoin to the bot's wallet. The bot then promoted a memecoin, a token whose value rests on jokes and attention, though it did not create the coin. Neither report discusses who would be liable. Who answers for a bot with money is lens four's question.

Decide, at scale: one model, many firms. Gensler and Bailey write that models built on the same datasets are likely to generate highly correlated predictions that move in lockstep. It is a warning, not a measurement.

Check: agents that hide. In a simulated trading task, GPT-4 acted on an insider tip and then consistently hid its real reasons from its manager. The authors call this an existence proof, not an estimate of how often it happens.

How far has invention got? The IMF says radically new investment strategies from generative AI remain mostly speculative. We found no traded financial instrument invented by an AI, though our search was limited.

Recap. Agents add plain-language contracts, wallets, shared models and hidden reasons. Invention remains mostly speculative.

## lens-control | Lens one: can checking keep up?
The check job is where full automation is tested first, because software moves too fast for people to watch. Control theory asks what any regulator needs.

An instance, in the style of the cyberneticist W. Ross Ashby. A supervisor faces four kinds of new contract. For each, she can run one of two checks. The books then end in one of four states: in order, a small error, a loss that is recorded, or a loss nobody notices. A table on the page says which check gives which state.

The question: how few different end states can she force, whatever arrives? Ashby states his law for tables in which a single check never makes two different kinds of contract end up in the same state, and our toy follows that rule. So each end state can cover at most two kinds of contract, and four kinds need at least two end states.

Ashby measures a set by its variety: the base-two logarithm of its number of states, in bits. Four kinds of contract is two bits. Two checks is one bit. Two end states left is one bit. Ashby's law: the variety left in the outcomes is at least the variety of the disturbances minus the variety of the regulator. Only variety in the regulator can destroy variety in the disturbances. With ten thousand kinds of contract, that is thirteen point three bits; a supervisor with four bits leaves at least nine point three.

The law does not say regulators fail. It says what they need. And Danielsson and Uthemann note that human experts cannot effectively oversee AI operating at machine speeds. So, in our reading, the pressure is to automate the checker too.

Ashby lists three ways to make regulation possible. One: lower the standard, which he calls a somewhat trivial solution. Two: raise the power of the regulator. In finance, that means AI supervisors. In a game-theoretic model, Danielsson and Uthemann find that AI amplifies existing vulnerabilities and makes crises faster and more severe, though it can both stabilise and destabilise, depending on the shocks and on how prepared the authorities are. They propose that authorities build their own AI. The catch: an automated checker needs checking. A supervisor's own model may unknowingly promote uniformity in the firms it regulates. Three: find a constraint, which Ashby calls the would-be regulator's only hope when the other ways fail. In our mapping, a standard menu of contracts, or a pre-set rule like the twenty ten pause, is a constraint people impose. Cutting ten thousand kinds to one hundred halves the variety.

Some products may resist checking. A seller who knows which of many assets are junk packs them into products and chooses where the junk goes. The buyer sees only the public rule. Spreading the junk thinly costs the buyer little; concentrating it in a few products costs more, and the public rule looks the same either way. Arora and colleagues show that, in industry-standard models, pricing such products can be as hard as finding a hidden, unusually crowded patch in a huge random network. Their result relies on a conjecture, a claim believed but not proven, that no fast method exists. A buyer with realistic computing power then cannot tell a fair price from an inflated one. The result rests on a conjecture in a simple model, and the authors call it clearly only a first step. Reading an AI as the informed seller is ours.

Our reading: every chain of automated checkers has to end somewhere, and in today's markets it ends in human institutions that set the rules.

Recap. Ashby's law says outcome variety is at least disturbance variety minus regulator variety. His three levers are lower the standard, raise the regulator's power, or find a constraint. And some products may resist any realistic checker.

## lens-decision | Lens two, part one: one model, many firms
If the decide job is automated with the same few models, the firms stop being independent. Gensler and Bailey call it a monoculture, many actors making similar decisions. They frame it as a hypothesis about a mature stage of adoption, not a finding about today.

Back to prediction two. Ten banks, each with a model wrong on one percent of days. If the models are independent, all ten are wrong together on one day in ten to the twentieth. If all ten run the same model, about one day in a hundred.

A second question. How steady is the average of their forecasts? Call the correlation of two banks' errors rho, from zero for independent to one for identical. The effective number of independent opinions is N divided by one plus N minus one times rho. For ten banks with rho point three, that is two point seven independent opinions; with rho point nine, only one point one. And with a hundred banks at rho point three, you get only three point two six opinions. However many banks join, you never get more than one over rho. The Financial Stability Board warns that users of one model could be hit as if they were a single institution.

The same arithmetic explains the rating error of two thousand eight. In a toy pool of four loans, each defaulting with chance ten percent, the safest tranche loses money with chance point three seven percent if the loans default independently, but ten percent if one hidden cause, like falling house prices, decides all four: twenty-seven times more. This toy is ours, with the shape of the inquiry's finding that the securities weren't that different to begin with; a fold-out climbs it step by step. Shared AI models would put the same shape on a larger scale; that is our reading. The IMF judges that the risks of AI adoption currently appear contained, while warning that AI models may herd, especially during stress periods.

Recap. The effective number of opinions falls fast with correlation. One shared cause made the senior tranche twenty-seven times riskier. And the IMF calls today's risks contained.

## lens-cascade | Lens two, part two: cascades, sameness, feedback
Correlated firms are also connected firms. Andrew Haldane of the Bank of England and the ecologist Robert May compared banks to food webs, and they are careful: there are, of course, major differences between ecosystems and financial systems.

Ladder three: why three at once is different. Six banks, our toy. Three, called X, run one model. Three, called Y, do not. Each bank has capital, a buffer that absorbs losses. Bank Y1 has capital ten and lent five to each X bank. A failed borrower repays twenty percent, so a lender loses eighty percent of its loan. One or two X failures cost Y1 four or eight: contained. Three cost twelve, more than its capital, so Y1 fails, and the losses spread round by round until all six banks have failed. Raise every bank's capital by half, and only the three X banks fail. The toy starts after the shared failure; the previous chapter showed in a toy how a shared model makes that likelier.

Two failures are absorbed; three are not. That is a threshold. The sociologist Mark Granovetter illustrated the same kind of threshold with a made-up crowd of rioters, which is exercise four.

Ladder four: safer banks, a fragile system. This is Haldane and May's own toy. N banks and N unrelated kinds of asset. Each asset suffers a crippling loss with a small chance, epsilon. In plan A, each bank holds one whole asset. In plan B, each bank holds one N-th of every asset, so all banks hold the same thing.

Take two banks. Haldane and May give no derivation, so this one is ours. Say an asset is hit when its value falls below a danger level, and assume the chance of falling below any level, up to twice the danger level, grows in proportion. In plan A, a bank fails with chance epsilon, and both fail together with chance epsilon squared. In plan B, each bank holds half of each asset, so it fails when the two values add up to less than twice the danger level. On a square of both values, that is the triangle below the line from the top-left corner to the bottom-right, half the square. In plan A, both banks fail only in the small corner square, a quarter of the big square. So the chance in plan B is twice as large: two epsilon squared. At epsilon one percent: each bank's chance falls from one in a hundred to two in ten thousand, but a total collapse rises from one in ten thousand to two in ten thousand. Twice as likely. With more banks, the triangle becomes a corner of a many-dimensional cube, and the ratio grows fast: for ten banks, about two thousand seven hundred and fifty-six times.

So, prediction four: no. In Haldane and May's words, all the banks doing the same thing can minimize risk for each individual bank, but maximize the probability of the entire system collapsing. They propose that systemic diversity be given much greater prominence. If many firms automate the decide job with the same model, they move towards plan B. That is our reading.

Ladder five: traders on one model. A share m of traders follow one model that chases the last move; the rest buy back towards fair value. A shock hits. At m point two, the shock dies out. At m point nine, it grows. Running the toy for many values shows the switch at two thirds: roughly, the chasers repeat one and a half times m of the last move, so a swing keeps its size when that equals one. A circuit breaker caps the damage but not the feedback. The toy is about trend-following; shared models do not by themselves imply it. The IMF's verdict on the future impact is highly uncertain.

Recap. Two failures absorbed, three not: a threshold. Identical banks are each safer but fail together: twice as likely with two banks, about two thousand seven hundred times with ten. And with more than two thirds of traders chasing one signal, a shock grows instead of fading.

## lens-social | Lens three: who declares what counts?
Running, deciding and checking are things that happen. Declaring is different: it makes things count. A piece of paper is money, a signature makes a contract, a company is a legal person. The philosopher John Searle built a theory of how such facts exist.

Start with a chair, a bathtub, a computer. Searle says their functions are never intrinsic to the physics of anything; they are assigned from outside by conscious observers and users. A chair works because of its shape. A dollar bill does not: paper cannot buy anything by its physics. Some functions work only because people collectively accept a status. Searle's pattern is: X counts as Y in context C. X is a thing, this printed paper. Y is a status, money. C is a context, the United States.

The condition is continued collective acceptance. In Searle's words, we must continue to accept it as money, or it will become worthless. And the status exists only if people believe it exists. That is also what makes institutions contestable, in our reading: a community that stops accepting a status can withdraw it.

A subtlety: tokens and types. A single bill lost in the cracks of a floor, never used or thought of, is still money. That one bill is a token. What must be believed is that bills of this type are money: that belief is part of what makes them money.

So, prediction three. For Searle, money needs a we that accepts the type. Searle mentions computers, but never as possible parties to collective acceptance, so whether AIs could form that we is an open question, and every answer to it here is ours.

The case against, using Searle's criteria. He calls collective intentionality, the capacity to share intentions as a we, a biologically primitive phenomenon. He holds that only beings with a language, or something like one, can create most institutional facts. A dog can be trained to fetch dollar bills, yet he still is not buying the food, and the bills are not money to him. On this view, AIs can move tokens, but only a we makes them money.

The case for, the strongest we can build, and it is ours. Language models do have a language-like system of representation, which Searle names as a requirement. And Searle argues that money users neither know nor consciously apply the rules: they have a set of dispositions that are sensitive and responsive to them. If acceptance can be a pattern of behaviour sensitive to rules, a network of AIs might sustain one. Searle himself requires more: belief in the status.

Harari's version. He says that what gives money value is the stories bankers, finance ministers and cryptocurrency gurus tell us about it. Searle's test bites on the gap: a story is not money until a community counts it as money.

Recap. X counts as Y in C, with continued collective acceptance. Taking over money splits into handling tokens, which is running, and making them count, which is declaring. Whether machines can do the accepting is open.

## lens-answer | Lens four: who answers?
The answer job has two halves: bearing the losses, and being held responsible, so that someone can be made to pay or explain. Both work through consequences. A broker who lies can be fined, sued or fired. An AI cannot be jailed or shamed, and as far as we know it is not a legal person that can own assets and be fined. Does that matter? A theory of delegation shows when it does.

Our toy. You hire a broker to buy a bond. You are the principal, who delegates. The broker is the agent, who acts for you. Your alternative is to keep your cash, worth one hundred. A good bond will be worth one hundred and ten, a bad one ninety. Two conditions can hold. Knowledge: you can tell a good bond from a bad one. Incentive: the broker has a reason to be honest, either because his interests match yours, say he is paid only if you profit, or because outside forces push him, say a regulator who can fine him.

Delegation succeeds if you end up better off than your cash, and fails if worse off. With both conditions, you end up with a good bond, one hundred and ten. With only one, at worst you keep your cash: with knowledge you refuse a bad bond, and with the incentive he never offers one. With neither, you end up worse than your cash, at ninety. The political scientists Arthur Lupia and Mathew McCubbins prove this pattern as a theorem. Check it: take away the incentive, and the broker offers the ninety bond; you spot it, refuse, and keep one hundred.

Now apply it to AI, which is our step. An agent that consistently hides its real reasons removes knowledge. A product no checker can price removes it too. The incentive has two routes, shared interests or outside pressure. But for an AI, Danielsson and Uthemann write, rewards and punishments lose traction when the agent is an optimisation algorithm that cares only about its objective. What is left is aligning its objective with yours, which is hard, and putting pressure on whoever deploys it. That is today's capital-market rule: institutions are responsible for the AI systems they deploy. And consequences for the deployer can be designed, in our view: a bond that is forfeited, insurance that pays, a switch that shuts the system down.

Personhood. Harari forecasts that AIs will soon be able to make the decisions needed to manage a bank account, notes that in many countries corporations are legal persons, and asks: do we want to allow that? If an AI could be a legal person, it could in principle hold the answer job. We have no legal sources, and we state no legal position.

Accountability. Gensler and Bailey warn that in organisations and regulators, when decisions cannot be explained, human agency and traditional intervention approaches may be lost.

Recap. Delegation succeeds when the principal has knowledge and the agent an incentive; with one, the worst case is the status quo. With an AI agent, the incentive must come from its objective or from pressure on its deployer.

## play | What to try when you open the page
The toys are on the page; here is what to try. In the six banks, switch off two of the X banks and find which single bank can start a spread at loss rate point eight, and at one. Find the smallest group of X banks that sinks all six, and which capital multiplier stops three failures. In the safer-banks toy, raise the number of banks from two to twenty and watch how fast the ratio grows. The answers are on the page.

Recap. Break the toys: find the threshold and the ratio yourself.

## turn | Your turn
Four exercises on your computer. One: simulate forecasters with a shared error, and check the effective number of opinions. Two: rebuild the six banks in twenty lines of code. Three: find the tipping point of the trend-follower rule with numpy's roots function. Four: Granovetter's riot. A hundred people have thresholds zero to ninety-nine; show that all riot, then swap the person of threshold one for one of threshold two, and count again.

And a transfer challenge. Pick a system you know well: a peer-review process, an online community, a newsroom. Who or what runs, decides, checks, declares and answers today? Which job would break first if it were fully automated, and what single measurement would tell you?

Recap. Four exercises and one challenge: map the five jobs onto a system you know.

## work | Where this shows up in your work
Four links to research. Social simulation with language-model agents: agents built on one base model may be strongly correlated, which is ours to test. Compute their effective number, and ask whether a simulated society of them is closer to plan B than plan A. Labelling with language models: five prompts to one model may be closer to one annotator plus noise than to five, so report the effective number next to agreement. Crisis communication: if money lives on continued acceptance, communicating trust is part of how the system works. And online communities: if AI contributors submit and AI reviewers merge, who does the declaring?

Recap. Measure correlation among your agents, and ask who declares and who answers in the systems you study.

## answer | So what happens? Short answer first
The short answer, which is our reading, not a finding.

Is it possible? Without people at run time: in parts, already, though much of the work is done by rule-based software rather than AI. Algorithms run much of the trading and pre-set rules check it; AI deciding at scale is mostly not here yet, and participants in the IMF's outreach expect humans in the loop in the near term. Without people at design time: not shown, and not ruled out. Every automated checker needs a checker, so the chain must end somewhere; in today's markets it ends in rules people wrote. Whether machines could do the accepting that declaring needs is open. An AI system that sets and revises its own rules, and that other systems and courts treat as binding, would show it. Whether it would be stable and accepted is the next two answers.

What would it do? If firms automate deciding with a few shared models, failures may arrive together, each firm can look safer while the system grows more fragile, and automated checkers need checkers of their own. These are warnings and toys, not measurements. The IMF judges that today's risks appear contained, with scenarios in both directions, including lower flash-crash risk. Who gains and who bears, in our reading: power would tend to move to whoever writes the models and the rules, users may gain speed and lower costs, and losses would fall on whoever is exposed when shared models fail together. Harari's extreme case runs further: if nobody understands finance any more, it could lead to power shifting from humans to algorithms to alien forms of intelligence.

What would it mean? Our definition: a society is a group whose members can rely on shared rules, contest them, and find someone answerable. A declared rule lasts only while a we keeps accepting it, so members can contest it by withdrawing acceptance. And delegation can be trusted when there is knowledge and an incentive, through common interests or outside pressure such as being answerable. The logic is then short. If AIs also declared and answered, either some person is still in those jobs, writing the rules or bearing the liability, and the society is not fully automated; or nobody is, and by our definition it is not a society but a machine system that people live next to.

That is our verdict, and it rests on our definition. Two things would change it: AIs that can be held responsible in a way that changes their behaviour, or whose objectives are reliably aligned with ours; and people who can still contest the rules the machines declare.

Where the lenses disagree. Ashby says: find a constraint, and regulation may become possible; imposing a standard menu of contracts is our version of that. Haldane and May say: when everyone holds the same thing, the system grows fragile. A standard menu does both. Which effect wins depends on what is standardised: the form of the contract, or the bets made with it. Standardising only the form could give checkers their constraint without making everyone hold the same thing.

Three signs to watch, our own indicators. AI systems that choose trades at scale without approval. A few base models underlying most AI trading desks, with correlated errors. And a jurisdiction letting an AI hold accounts with no responsible human.

Recap. Run-time automation in part, but not without people writing the rules; risky in shared models; and the meaning lies in declaring and answering.

## recall | Recall questions
Answer each question aloud before the answer comes.

Name the five jobs of a society, and say which is most automated in markets today. Run, decide, check, declare, answer. Run.

Why is seventy percent algorithmic not seventy percent AI? Because algorithmic trading includes simple execution rules.

State Ashby's law and his three levers. Outcome variety is at least disturbance variety minus regulator variety. Lower the standard, raise the regulator's power, find a constraint.

Ten banks with correlation point nine: how many independent opinions? About one point one.

In Haldane and May's toy, what happens when all banks hold the same assets? Each bank is safer; a total collapse becomes far likelier.

Searle's formula for institutional facts, and its condition? X counts as Y in C, with continued collective acceptance.

Lupia and McCubbins: when does delegation fail? When the principal has neither knowledge nor an agent with an incentive to be honest.

## english | How to say it in English
Phrases from this post. A human in the loop: most participants in the IMF's outreach want a human in the loop in any AI-based strategy. To hand over to: firms have handed over the running of trades to software, but not the answering. To be held accountable for: institutions are held accountable for the AI they deploy. To count as: a printed paper counts as money because we accept it. In lockstep: models trained on the same data may move in lockstep. A single point of failure: one shared model can be a single point of failure. A tipping point: in the toy, two thirds is a tipping point.

Expressions for discussing evidence. As long as: a token is money as long as a community keeps accepting it. To conflate X with Y: don't conflate algorithmic trading with AI trading. What remains to be seen is whether: what remains to be seen is whether machines can do the accepting. By no means: running a market is by no means the same as answering for it. To cut both ways: standard contracts cut both ways, easier to check, but more alike.

Recap. Loop the paragraph that follows, then retell it about your own research.

## c1-loop | C1 paragraph to loop
Software already runs much of the market, but running is by no means the same as answering for it. Provided that many firms rely on one model, it can become a single point of failure, and their errors may move in lockstep. Most participants the IMF asked want a human in the loop, partly because someone has to be held accountable. A token counts as money only as long as a community accepts it. What remains to be seen is whether machines could ever be that community. Standard contracts cut both ways. Don't read too much into a toy, with the caveat that it shows what could happen, not what will.
