---
post: 2026-12-surprise
voice: kokoro af_heart
status: written and checked at S4; audio NOT recorded (Kunhao reviews the text first)
note: Written for the ear. Formulas are spoken in words. Widgets are described, not read. Fold-outs and tables are only mentioned. Each chapter ends with a short recap so it can be looped alone. The post stands alone and never refers to another post. Chapter ids match the section ids of the page.
---

## hook | Counting messages, and what the count misses
Welcome to AI4Read from CSS Lab. This is post four: how much is a surprise worth?

Here is the answer in one line, so you can hold it while you listen. A surprise is worth the number of fair yes or no questions it saves you. The rarer the news, the more questions it saves. And the average over all the news a source can send is called its entropy.

Start with the engineers. In the nineteen twenties, telegraph engineers asked how much one line can carry. Pierce, in his nineteen sixty-one history of the field, reports Nyquist's answer from nineteen twenty-four. The speed of a line depends on how many different current values it can send. A line that only switches on and off has two values. With four values, the speed doubles, as it did in the quadruplex telegraph. With three values, plus, zero and minus, the speed rises by sixty per cent. In words, and this is our reading: each time the number of values doubles, the speed grows by the same step.

Then Hartley, in nineteen twenty-eight, took the sender's side. A message is measured by how many different messages the sender could have picked from a set of symbols. Shannon names both papers as the basis for a general theory. Pierce says the count fits only if successive symbols are chosen independently, and each symbol is equally likely to be selected. Hartley also noted that some letters are chosen more often than others, E more than Z, and that this should govern the lengths of signals. Morse, Pierce says, himself understood this. What was missing was a number that weighs each message by how likely it is.

Here is the pain, and this is our own point. A count gives one number to every message from the same list. In a town where it rains most days, it rained today and it snowed in July are both one pick from the same list of weather reports. The first tells you almost nothing. The second is news. A count cannot see the difference. We need one number for how much did this message tell me that still works when the choices are not equally likely. This post builds it in a coffee shop, checks it in a village, and asks what it leaves out.

Three words need fixing before we go on. Worth means the number of fair yes or no questions an outcome saves you. It does not mean usefulness or importance. Surprise means how unlikely an outcome was under a stated model of the source, a list of how likely each message is. It does not mean a feeling. And information is used in Shannon's engineering sense: one choice from a set of possible messages. Pierce warns that the everyday sense, knowledge, creeps in and confuses the discussion.

Now a guess, before you read on. A submarine hides in one of sixty-four squares, and every square is equally likely. You fire at one square and miss. How much news is that miss worth, counted in fair yes or no questions? Option one: almost nothing, a few hundredths of one question's worth. Option two: about one question's worth, because a plain no is still an answer. Option three: exactly nothing, because you still do not know where it is. Option four: about six questions' worth, the same as finally finding it. Pause and choose. The answer comes in the section on the submarine.

Recap. Old measures counted possible messages, and they are right only for independent, equally likely choices. A count cannot tell news from non-news. We want one number that weighs each message by how likely it is.

## cafe | The guessing barista
Picture a loud café. The grinder drowns every word, so a customer can only nod for yes or shake their head for no. The owner knows from the till that out of every eight regulars, four want a flat white, two a latte, one a mocha and one a matcha. The new barista wants each regular's drink with as few questions as possible, because each costs a second and the queue is long.

The old way: split the menu. The menu board is a grid with two drinks on top and two below. The barista asks, is it on the left side of the board? And then, is it the top one? Two questions, and she always knows. That looks fair, but it wastes time. Half of the regulars want the flat white, and she spends two questions on each of them. She spends as many on the matcha, which only one regular in eight wants. She split the drinks into equal halves, and ignored how many customers stand behind each drink.

The rule that changes: split the customers. The first question is, flat white? A nod settles four customers out of eight in one second. A shake leaves four, and she asks, latte? A nod settles two more. A shake leaves two, and she asks, mocha? After that answer she knows, because only the matcha is left. The flat white costs one question, the latte two, the mocha and the matcha three each. Over eight customers that is four plus four plus three plus three: fourteen questions. One and three quarters for each customer, against two for the old way. The rare drinks cost more, and that is fair. A matcha order is unusual news, and it took the most questions to find out. The rarer the order, the bigger the surprise, and the more questions it is worth.

On the page, two small diagrams show the two ways side by side. Tap between them. In the old way every drink costs two questions. In the new way the costs are one, two, three and three.

Three checks. If she asked, matcha? first, almost every answer would be a shake, and she would learn almost nothing. A question helps most when both answers are likely. If all four drinks sold equally, the clever order would save nothing, and an order built for the old shares would do worse than the plain board. The next section gives the numbers. And if every regular ordered the same drink, she would not need to ask anything.

Who does what. The customer knows the drink. As the barista asks the agreed questions, the customer's nods and shakes turn the drink into a string of answers, for example shake, shake, nod. The barista sees only that string, and she holds the same list of questions. She turns the string back into a drink. Both must hold the same list before the day starts, or a nod means nothing. We call the agreed list the script.

The page lists ten parts of the café, and the next section points back to them by number. One, the four drinks. Two, the share of regulars who want each drink, as the till records it. It can be out of date. Three, one question, answered by a nod or a shake. Four, the script. Five, the customer, who knows the drink. Six, the string of nods and shakes. Seven, the barista, who has only the string and the script. Eight, the number of questions one drink costs. Nine, the day's average. Ten, the menu board, the old way.

Check yourself. Which customers get the longest run of questions, and why? The mocha and matcha customers, three each. Each is one regular in eight, and only three shakes in a row reach them. Second question: on a day when all four drinks sell equally, would the clever order still be best? No. It would cost more than two questions on average. A script is built for the shares it was made for.

Recap. Split the customers, not the menu. Common drinks get short runs of questions, rare drinks get long runs, and the average falls from two to one and three quarters. The customer encodes the drink into a string, and the barista, with the same script, decodes it.

## village | The weather village, equal chances first
Now leave the café for the field's own setting. A village radio sends one word a day: rain, sun, wind or snow. The shares of days are one half, one quarter, one eighth and one eighth. These are the owner's numbers with drinks swapped for weather words. Shannon's example sends one of four symbols with these shares, and Cover and Thomas use the same numbers. We call each symbol a day. Shannon assumes successive symbols are chosen independently, and so do we, though real weather is not like that. Each equation is followed by a line that starts, in the café. Its numbers point to the ten parts you just heard.

Step one: equal chances, count the halvings. A guess first. One of thirty-two cups of water is poisoned. A rat that drinks any poisoned cup dies within the hour, and you have one hour. All the rats drink at the same time, each from any cups you choose. What is the smallest number of rats that is always enough? Four, five, six or eight? Pause. The answer is at the end of this chapter.

The cups and rats are our framing, not from a source. The same game with questions in turn is in MacKay's book: one of sixty-four objects is chosen, and you find it with yes or no questions. MacKay writes that the best questions successively divide the sixty-four possibilities into equal sized sets, and six questions suffice.

With thirty-two cups, one good question halves them: thirty-two, sixteen, eight, four, two, one. That is five halvings. Write each answer as zero or one, and the five answers spell a number. MacKay's object thirty-five of sixty-four gives one, zero, zero, zero, one, one. The rat version asks all five at once. Number the cups from zero to thirty-one in five binary digits. Rat one drinks from every cup whose first digit is one, rat two from every cup whose second digit is one, and so on. The rats that die spell the number of the poisoned cup.

Thirty-two is two multiplied by itself five times, and sixty-four is six times. One answer of a fair yes or no question is one bit, a word Shannon credits to J. W. Tukey. MacKay also uses bit for a zero or one variable. Here it is a unit of worth.

The formula, call it equation one. For N equally likely options, the number of questions k satisfies: N equals two to the power k. So k is the log, base two, of N. In words: the number of questions is the number of times you must halve N to reach one. The log, base two, asks: two multiplied by itself how many times gives this number? MacKay's raw bit content is this quantity, a lower bound for the number of binary questions that are always guaranteed to identify an outcome. Guaranteed means in the worst case, not on average. Hartley's measure is the same idea, with Pierce's two conditions: independent and equally likely. The pairing with Hartley is ours.

The check. The log, base two, of thirty-two is five. The log, base two, of sixty-four is six. Cover and Thomas open with the same case: thirty-two equally likely outcomes, five bits. What it does not say: four rats cannot decide thirty-two cups, because two to the fourth is sixteen, and sixteen is less than thirty-two. That is ours.

In the café. N is the number of drinks on the menu board when all sell equally. That is parts one and ten. k is the number of nod-or-shake questions, part three. The two in two to the k is the two replies to one question. Halving the board is the old way, part ten.

The answer to the guess. Five rats. Five rats give five answers at once, spelling one of thirty-two labels. Four rats give only sixteen labels.

A fold-out on the page, Nyquist and Hartley in symbols, goes deeper. It also records that Pierce's page thirty-eight says eight values give four times the speed, which is a slip. By Nyquist's rule it is three times, and that is our computation.

Recap. With equal chances, the number of questions is the number of halvings, the log, base two, of the number of options. One answer is one bit. Thirty-two cups need five rats.

## surprisal | Step 2: unequal chances, surprisal
Step two. The village again: rain one half, sun one quarter, wind one eighth, snow one eighth. The best questions go like the barista's: rain? Then sun? Then wind? And then only snow is left. Rain costs one question, sun two, wind three and snow three. Write yes as zero and no as one, and the answers are zero, one-zero, one-one-zero and one-one-one. Cover and Thomas say the first question splits the probability in half. That holds for this example only. That caveat is ours.

What rule gives the number of questions an outcome costs? A share of one half needs one halving of the queue, one quarter needs two, one eighth three. The cost is how many times you halve the whole queue to arrive at that share.

The formula, equation two. For an outcome x whose share is P of x, the cost, h of x, is the log, base two, of one over P of x. In words: the surprisal of x is the log, base two, of one over the share of x. MacKay calls it the Shannon information content. Gibson and colleagues call it surprisal, and in the same sentence information content. Shannon's nineteen forty-eight paper uses neither word for one outcome, by our search of the whole text. We use the word surprisal.

The check. For snow, the share is one eighth, and the log, base two, of eight is three. The four words give one, two, three, three, as the questions did. On the page, a slider lets you move the chance of an event. Share zero point zero zero one is worth ten questions. Zero point zero one gives six point six. Zero point one gives three point three, zero point two gives two point three, and zero point five gives one. Those are MacKay's numbers. A second curve shows the average over the event and its opposite, which the next step explains.

A second concept: independent days add. Rain today, snow tomorrow. The days are independent, so the pair has share one half times one eighth, which is one sixteenth, and the log, base two, of sixteen is four. The separate costs are one and three, and one plus three is four. In general, for independent x and y, the chance of the pair is the product, and a log turns a product into a sum. That is equation three: the surprisal of the pair is the surprisal of x plus the surprisal of y. MacKay's reason is that we might want any measure of the amount of information gained to have the property of additivity. It needs independence, which the village assumes.

What it does not say. Only halves, quarters and eighths cost a whole number of questions. A share of zero point three would cost one point seven four, and a question cannot be asked one point seven four times. So Gibson and colleagues say the information content approximates the length of the shortest uniquely decipherable script. Step seven returns to this.

In the café. x is a drink, here a weather word, part one. P of x is its share in the till, part two. h of x is the questions that drink costs under the best script, part eight. The log of one over the share is how often the queue is halved, parts three and four. Additivity is two customers in a row, with their strings joined, parts five and six.

Recap. The surprisal of an outcome is the log, base two, of one over its share. Rain costs one, sun two, wind and snow three. Surprisals of independent events add.

## entropy | Step 3: the average, entropy
Step three. A guess first. With the best script of questions, how many questions does one day's word from the village radio cost on average? One point two five, one point five, one point seven five, or two? Pause. The answer follows.

Take eight days that match the shares: four rain, two sun, one wind, one snow. Rain costs one question each, sun two, wind three, snow three. The total is four plus four plus three plus three, fourteen questions in eight days: one point seven five per day. What one number describes the source? Weigh each word's cost by how often it comes, and add.

The formula, equation four. The entropy H of a source is the sum, over all words, of the share of the word times its cost. That is the average surprisal. An outcome with share zero contributes zero, by a convention in MacKay's book. For the village: one half times one, plus one quarter times two, plus one eighth times three, plus one eighth times three, equals one point seven five. Cover and Thomas write of the same tree that the resulting expected number of binary questions required is one point seven five.

Two checks. First, the tree gives one point seven five. Second, the grouping rule, equation five. The first question splits rain from the rest. The rest have shares one half, one quarter, one quarter, with entropy one point five. With chance one half we are in that group, so H equals one plus one half times one point five, which is one point seven five. That is Shannon's decomposition rule. Before and after the crucial change: two-question labels cost two questions a day, and the script built for the shares costs one point seven five.

On the page, a widget lets you set four weights, for rain, sun, wind and snow. Bars show each word's surprisal. Three settings are worth trying. All equal: the entropy is two, the most possible for four words. Only rain: the entropy is zero, and Shannon writes that no channel is required. Reversed: the entropy is still one point seven five, because it depends only on the shares, not on which word carries which.

A script has its own average, equation nine. A script that spends L of x questions on word x averages the sum of the share times L of x. The village script on the village: one point seven five, which equals H. On a village where all four words have share one quarter, the same script averages one quarter times one plus two plus three plus three, which is two point two five. That is worse than the two of plain labels. On only rain it averages one, since it still asks one question. A script is right only for the shares it was built for.

What it means. We measured the average number of fair questions per word, for a source whose shares we assume are known. It predicts the cost of the best script when the shares are halves. It does not say what a word means, how long a real message is, or how good the script is on other shares. A fold-out on the page records the names: uncertainty is another name for entropy, and not a feeling.

In the café. The sum means: go through the day's customers, part nine. P of x is how often that drink is ordered, part two. The log of one over P of x is the questions that drink costs, part eight. H is the day's average, part nine. And the script's own average uses L of x, the questions the script spends on one drink, parts four and eight.

Check yourself. Predict first: what does the village script cost on a day when all four words are equally likely? Two point two five.

The answer to the guess. One point seven five questions. Four days in eight cost one, two cost two, two cost three, fourteen in eight. Plain two-question labels give two. The other options are below the minimum: Cover and Thomas say one point seven five turns out to be the minimum expected number of binary questions.

Recap. Entropy is the average surprisal, the sum of share times cost. The village has entropy one point seven five. It is largest, two, when all four words are equally likely, and zero when one word is certain. A script is right only for its own shares.

## weighing | Step 4: a question is an experiment
Step four. MacKay's weighing problem. Twelve balls look alike. One is heavier or lighter than the rest, and we do not know which. A balance scale has three outcomes: left pan down, right pan down, or balance. There are twenty-four hypotheses: twelve balls, each heavy or light. Two weighings give at most three squared, nine outcomes. Three weighings give three cubed, twenty-seven, enough in principle.

Which first weighing is best? A weighing is a question with three answers, and a good one has answers that are about equally likely. MacKay says that at each step of an optimal procedure, the three outcomes are as close as possible to equiprobable. Put four balls on each pan. The left pan goes down if the odd ball is heavy and on the left, or light and on the right: eight of the twenty-four hypotheses. The right pan, likewise, eight. They balance if the odd ball is left out: four times two, eight. The split is eight, eight, eight. With six on each pan the pans can never balance, and the split is twelve, twelve, zero.

The worth of a weighing is the entropy of its three outcomes, equation seven. Four against four: three times one third times the log of three, which is the log of three, one point five eight five bits. Six against six: one half plus one half, one bit. All twenty-four cases need the log of twenty-four, four point five eight five bits, so one weighing gives at most one point five eight five of them. MacKay writes, with a hedge, thus we might conclude that the outcome of a random experiment is guaranteed to be most informative if the probability distribution over outcomes is uniform. It is a conclusion from this example, not a theorem about every question.

On the page, a slider sets the balls in each pan, from one to six. The bars show the three outcome chances. One against one is worth zero point eight one seven bits. Two against two, one point two five two. Three against three, one point five. Four against four, one point five eight five. Five against five, one point four eight three. Six against six, one point zero zero zero.

Does six against six tell you nothing? MacKay reports that some say it conveys no information at all, and asks the reader to explain why both groups are right and wrong. He prints no solution. Ours: about which ball, it tells you zero bits, because after left heavier every ball is still possible. About which ball and heavy or light, it tells you one bit.

In the café. A weighing is a question with three replies: a nod, a shake and a shrug, part three. Each reply's chance is the share of hypotheses it covers, part two. Choosing the first weighing is choosing the script's first question, part four. Halving the menu, part ten, is the wrong split. Halving the customers, part two, is the right one.

Check yourself. Before you move the slider, what is the worth of six against six about which ball? Zero bits.

Recap. The best question is the one whose answers are most nearly equally likely. Four against four gives one point five eight five bits, six against six only one.

## submarine | Step 5: the submarine, one answer, six bits
Step five. A submarine hides in one of the sixty-four squares of an eight by eight grid, all equally likely. You fire at squares one by one. The first shot hits with chance one in sixty-four. What are a hit and a miss worth, and what do many misses add up to?

A hit names the square among sixty-four: six halvings. A miss crosses off one square, a sliver of the options. After thirty-two misses half of the squares are gone: exactly one question's worth. A later hit names the square among the few left, so it is worth less. The total is the same whenever the hit comes.

A check by hand on four squares. Misses are worth the log of four thirds, zero point four one five, then the log of three halves, zero point five eight five, then the log of two, one. The sum is two, which is the log of four.

The formula, equation eight. The chances multiply, and the fractions cancel in a chain: the log of sixty-four over sixty-three, times sixty-three over sixty-two, and so on down to n over one, equals the log of sixty-four, which is six, whatever n is. This is MacKay's telescoping product.

On the page, a table steps through the grid. Shot one is a miss, worth zero point zero two two seven. Shot two, zero point zero two three one, for a total of zero point zero four five eight. MacKay prints zero point zero two three zero for shot two because he cuts digits off. We round. Shots three to thirty-two, thirty more misses, bring the total to exactly one. Shots thirty-three to forty-eight bring it to two. Then a hit on shot forty-nine, with sixteen squares left, is worth four, and the total is six.

What it means. MacKay says it might seem a little strange that one binary outcome can convey six bits. His verdict, with his I think, is that the submarine example makes quite a convincing case for the claim that the Shannon information content is a sensible measure. That is an argument, not a proof. A single answer is worth the log of one over the share of what happened, so one yes or no answer does not always carry one bit.

In the café. The squares are the drinks still possible, parts one and two, and they shrink as answers arrive. Suppose matcha is one order in sixty-four and the barista asks, matcha? first. A shake costs zero point zero two two seven of a question, part three. A nod costs six. Whichever path she takes, the total worth of finding the drink is the same, part eight.

Check yourself. Five misses in a row from a fresh grid: is the fifth worth more or less than the first? Slightly more. The misses are worth zero point zero two two seven, zero point zero two three one, zero point zero two three five, zero point zero two three eight and zero point zero two four two, because fewer squares are left each time.

The answer to the first guess. Almost nothing. A first miss is worth about zero point zero two two seven questions. A hit on the first shot would be worth six. One whole question's worth takes thirty-two misses.

A fold-out on the page, Wenglish, is MacKay's made-up language where each letter carries a different amount but the five letters of a word always add to fifteen bits.

Recap. A hit is worth six, a first miss about two hundredths, and the total for finding the target is always six. A single answer is worth the log of one over its share.

## roles | Step 6: who encodes and who decodes
Step six. In the café, the customer wants a mocha. The barista asks, flat white? A shake. Latte? A shake. Mocha? A nod. Write a nod as zero and a shake as one. The string is one, one, zero. Which side encodes, and which decodes?

The encoder holds the original, here the drink, and the agreed script, and turns the original into a string. The decoder holds only the string and the same script, and turns the string back. Shannon's diagram has the same roles: the receiver ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the signal. The script is the codebook both sides hold before the day starts. MacKay writes that the questioning strategy defines a way of encoding the random variable as a binary file. That can sound as if the asker encodes. The strategy is the shared script. The secret-holder's answers make the string.

On the page, a diagram in three steps shows it. The customer knows the drink and the script. The script turns mocha into answers: no, no, yes. The barista has only the answers and the same script, and names the drink.

Shannon's twin game. In nineteen fifty-one Shannon selected a short passage unfamiliar to the person who is to do the predicting. So the first person has not seen the text. He knows it only up to the current point, guesses the next letter, and is told whether he was right. The record of his guesses is the reduced text. A twin, mathematically, not just biologically identical, with only that record will respond in the same way when faced with the same problem, so the reduced text can be considered to be an encoded form of the original. Had the first person held the whole text in advance, every guess would be right and the record would carry nothing. That gloss is ours.

A toy walk-through, ours. The predictor is a fixed ranked list of letters: E, T, A, and so on. The original is T, E, A. The encoding side finds T second, E first, A third, and writes two, one, three. The decoding side, with only two, one, three and the same list, recovers T, E, A. Shannon's real predictor uses the preceding text.

In the café. The customer is part five and encodes. The string is part six. The script is part four, and both sides hold it. The barista is part seven and decodes.

Check yourself. In the café, who encodes? In Shannon's twin game, who decodes? The customer encodes and the barista decodes. In the twin game, the side with the original text and a predictor encodes, and the twin, with only the reduced text and an identical predictor, decodes. In both cases the shared script or predictor is what lets the string be read.

Recap. The side that holds the original and the script encodes. The side that holds only the string and the same script decodes. The script, agreed in advance, is what makes the string mean anything.

## nothalves | Step 7: when the shares are not halves
Step seven. The village is too nice. Halves, quarters and eighths give whole numbers of questions, so the average equals the entropy exactly. Do not take that as a rule. In general the best average lies between H and H plus one, equation six. Cover and Thomas state it in their chapter on codes, after saying: we now digress to show the equivalence of coding and the game of twenty questions. A sequence of questions is a code, and the average number of questions is the average code length. We quote the bound and do not prove it.

A fold-out on the page has the smallest case with shares that are not halves, ours, run in code. Rain has share zero point seven, and the other three words zero point one each. The entropy is one point three five seven bits. The best script of whole questions has lengths one, two, three, three and averages one point five. One point three five seven is at most one point five, which is less than two point three five seven. The gap, zero point one four three, is the price of whole questions.

In the café. Only whole questions can be asked, part three. A drink that seventy per cent of regulars want still costs one whole question, though only zero point five one five questions' worth of news arrives when it is ordered. The extra is the price of whole questions. The script, part four, keeps the average, part nine, as close to H as whole questions allow.

Recap. The best script averages at least H and less than H plus one. Equal to H only when every share is a power of one half.

## answer | Short answer, and what it really is
This is the abstract layer. First, a short answer, and it is our reading, not a finding.

How much? One outcome is worth the log, base two, of one over its share, in fair yes or no questions, under a stated model of the source. The average over everything the source can send is the entropy: one point seven five questions a day for the village. A surprise? Improbability under a model. The number belongs to the model, not to the event: two forecasters with different shares give the same snow different numbers. Worth? Questions saved, not importance, truth or meaning. Shannon sets meaning aside for the engineering problem. That is a decision about scope, not a claim that meaning does not matter. Our verdict: the measure is a good price for improbability under a stated model, and a poor price for anything else. What would change it: evidence that, for cases we care about, the number predicts something beyond improbability. Lens two, coming next, has one such claim, still unproven.

What it really is. Strip away the cafés, villages and submarines. Surprisal rewrites a share in units that add for independent events; the logarithm turns a product of shares into a sum. Entropy is the average surprisal under the same shares, and depends only on the shares, not on what the outcomes are. It is zero only when one outcome is certain, and at most the log of the number of outcomes, with equality only when all are equally likely. Mixing the shares toward equality raises it, except a mere swap between outcomes. The surprisal approximates the length of the shortest uniquely decipherable script for the outcome. Approximates is the authors' word. This is equations two and four without the café.

A fold-out on the page gives Shannon's three properties and his Theorem two. Shannon himself writes that the theorem and its assumptions are in no way necessary for the present theory.

Recap. Surprisal is a re-coding of share into units that add. Entropy is its average. Neither says what a message means.

## lenses | The same idea elsewhere
Five lenses. For each, a link type, what it adds, and what it does not explain.

Lens one, statistical mechanics. The link is same math in form only. Shannon writes that the form of H will be recognized as that of entropy as defined in certain formulations of statistical mechanics. A toy, ours: a box of four cells, with shares equal to the chance that a given particle sits in each. All in one cell gives zero. Spread equally gives two. These are the village's numbers in another story. Pierce says the ideas behind the two entropies are quite different. We stop at the form. It adds that the sum is about distributions wherever shares exist. It does not explain that the two entropies are one thing.

Lens two, psycholinguistics. A structural analogy: the same quantity, but its role in minds is an empirical claim, not a theorem. Gibson and colleagues use surprisal for colour words, word length and, through other work, processing. For minds they write: since language processing effort is associated with predictability. The references are Hale and Levy. Read the hedge: is associated with. This is a review that points to studies we have not seen. It adds the only lens where the number is tested against behaviour. It does not explain cause. Associated with is not caused by.

Lens three, communication theory. A metaphor. Our café roles are Shannon's transmitter, signal and receiver. The scope is narrow on purpose: these semantic aspects of communication are irrelevant to the engineering problem. It adds the roles, and an honest boundary. It does not explain meaning, truth or effect, where the study of communication in the social sciences begins. That summary is ours, and we have not read Weaver's essay, so we use none of his levels.

Lens four, Bayesian probability. A structural analogy: a share can be a degree of belief, so surprisal is relative to a believer. The village's shares come from a long record. A one-off event has none, which is our point. MacKay describes the Bayesian view, in which beliefs can be probabilities, even for a single proposition. As MacKay puts that view, you cannot do inference without making assumptions. He warns that this is not yet a globally held view, and that people with the same assumptions and data will draw identical conclusions. Our inference: different beliefs give different surprisal for the same event. It adds a way to price one-off events. It does not explain whether the beliefs are right.

Lens five, search and decision. Same math. A tree of yes or no questions is a code. The designer's view: to find something fast, choose the experiment with the most equal outcomes. It adds the step from describing a source to choosing what to ask. It does not explain questions whose costs differ, or answers that can be misheard.

How the five differ, ours. Lens one asks where else the same sum appears; lens two, whether minds use it; lens three, what it leaves out; lens four, where the shares come from; lens five, what to do with it. For your research: in computation, a language model's next-word share gives a surprisal under that model. In communication, a headline's surprisal depends on whose model prices it. In collaboration, the same sum applies to shares of topics or ties. These are connections, not findings. A fold-out on the page gives more hedges from Shannon, Pierce, and Gibson and colleagues.

Recap. Five lenses: same sum in physics, a claim about minds, the engineering boundary, beliefs as shares, and questions as a code. Each one says what it does not explain.

## fails | Where it fails
Each boundary is an assumption you can find in the concrete layer, with the place where the café breaks.

One, meaning. The formula has only the share in it, so two words with equal share get equal surprisal, understood or not. Shannon sets meaning aside. Gibson and colleagues say the theory as specified so far is entirely agnostic to the form and content of messages. Pierce notes that a completely random pattern is mathematically the most surprising, and also the dullest of all patterns. The café breaks: the barista cares which drink it is, and whether the customer is allergic to milk. The script is blind to taste.

Two, a known, stable distribution. Shannon: these probabilities are known but that is all we know concerning which event will occur. In Pierce's simplest case the chances must not change with time. The café breaks: the till's record gets old, and the village script costs two point two five on a uniform day.

Three, independent days. Shannon's symbols are chosen independently, and additivity needs it. The café breaks: a rainy morning makes hot drinks likelier, and the same people come on the same days.

Four, one-off events, and whose model. The formula needs a share, and the village takes it from a record. A source that can produce only one particular message has entropy zero and no channel is required. That is about transmission, not about the message being unimportant. The café breaks: a single event has no till. On the page, a widget lets two forecasters, Ana and Ben, write two shares for the same snow. Ana says one eighth, Ben one half. Ana is surprised by three, Ben by one. The gap is two. Equal beliefs give equal numbers. The number belongs to the model, not to the snow.

Five, estimation. The village shares are given. In practice they are estimated, and as Gibson and colleagues write, it is difficult to get reliable estimates of these information-theoretic quantities without very large datasets. The bias is our computation from the notebook. Draw n village days, put the observed shares into the entropy formula, repeat two thousand times with a fixed seed. The true entropy is one point seven five. For ten days the mean estimate is one point five zero four, a gap of minus zero point two four six. For thirty days, one point six seven five. For a hundred, one point seven two five. For a thousand, one point seven four seven. The estimate is biased low for small samples, because a rare word that never appears gets share zero. The gaps are in bits, not relative.

Six, whole questions, no noise. Whole numbers of questions only for halves, and a string that always arrives intact. The café breaks: a script rounds up, one point five against one point three five seven, and real nods can be misread. Noise is outside this post.

Check yourself. Label each statement as a theorem, a definition, an assumption, an empirical claim or a computation. One: the village's entropy is one point seven five bits. A computation. Two: the shares must be known. An assumption. Three: reading effort follows surprisal. An empirical claim, made by others and hedged as is associated with. Not a theorem. Four: the surprisal of two independent events adds. A property that follows from the definition, given independence.

Recap. Six limits: meaning, stable shares, independence, one-off events and whose model, estimation, and whole noiseless questions. Each is an assumption of the village, and each breaks the café somewhere.

## imagination | The CSS imagination: whose model sets the price of a surprise?
This is the layer that turns the idea toward society. We use C. Wright Mills, in the two thousand Oxford edition of his nineteen fifty-nine book, The Sociological Imagination.

Mills argued that people need a quality of mind that shows how a life and its time fit together. The imagination, he wrote, enables us to grasp history and biography and the relations between the two within society. His advice is not findings, and he hedges it: there are definite ways, I believe, of stimulating the sociological imagination. He wrote in nineteen fifty-nine and used the word men for people. Inside quotation marks we keep his words. The four move names below are ours, and his list has seven items. One caution: his word information, in this Age of Fact, means facts and news, not Shannon's sense. Joining the two senses is our metaphor.

Move one: trouble and issue. Mills called the distinction between the personal troubles of milieu and the public issues of social structure perhaps the most fruitful one. His example is hypothetical, not data: one man unemployed in a city of a hundred thousand is his personal trouble, while fifteen million men unemployed in a nation of fifty million employees is an issue. An issue is not a trouble multiplied. It is, he says, unlike even widespread trouble.

Our case, ours. One reader cannot tell which of her two hundred messages matters, and blames herself for what she misses: a trouble. It becomes an issue only if the cause lies in an arrangement she cannot change, such as a ranking system whose model, not hers, prices every message for everyone. A test: if changing the ranking changes what many readers miss, and individual effort does not, it is an issue in Mills' sense. Otherwise it is many troubles. Pierce's one sourced anchor: we can be surprised repeatedly only by contrast with that which is familiar. Whose idea of the familiar prices the message?

Move two: extremes and inverted scale. Mills writes that often you get the best insights by considering extremes, by thinking of the opposite of that with which you are directly concerned. He adds that he still strives to gain and to maintain a sense of proportion. His extremes are opposite types; the numbers are our reading. A village where it always rains has entropy zero, and no channel is required. With all four words equally likely, the entropy is two, the most for four words. Now invert the scale. Mills asks: what would pre-literate villages look like with populations of thirty millions? Give the weather village thirty million listeners. Each listener's surprisal for snow is the same. What changes is who writes the forecast, and who pays when it is wrong.

Move three: another discipline's eyes. Mills defines the imagination as the capacity to shift from one perspective to another. He suggests asking how a political scientist, an experimental psychologist or a historian would see a problem. Shift between views of one message, snow tomorrow. A farmer asks what to do with the sheep. A weather service asks whom to warn, and who pays when it is wrong. An engineer asks what the report costs in questions. A psycholinguist asks whether listeners track surprisal, an association claimed in the literature, not a theorem. A journalist asks what counts as news; meaning and consequence are what the number leaves out. None of them sees who owns the model.

Move four: comparison. Mills: the search for comparable cases, either in one civilization and historical period or in several, gives you leads. Our extension: compare the entropy of topic mixes across platforms or periods, or the surprisal of headlines across outlets. It means something only if one model prices every case, and, in Mills' spirit, if it sits in a historical frame. A fold-out gives Mills' two-sided view of counting.

Two open research questions. They are ours, invitations, not findings. One, computation and communication: do posts that are more surprising under a language model spread further, after controlling for topic and emotion? Data: posts with share counts and a topic label, plus token probabilities from one fixed model. Method: a regression with topic fixed effects, reporting how the result moves when the model changes. Two, collaboration and communication: how does the entropy of a platform's daily topic mix change around a crisis? Data: posts labelled by topic. Method: plug-in entropy with bias correction and bootstrap intervals, before and after a dated event.

Recap. Trouble becomes issue only when the cause lies in an institution, here whoever owns the model. Extremes and scale, other disciplines and comparison all point to the same question: whose model prices a surprise?

## turn | A market stall and a notebook
Your turn. First, a transfer challenge. A market stall sells five items with shares one half, one quarter, one eighth, one sixteenth and one sixteenth. Build the script of questions. Compute the average number of questions and the entropy. Then change the shares to one quarter, one quarter, one quarter, one eighth and one eighth. What does the old script cost now, and what does the best script cost? A hint: halve the customers each time. The two rarest items get four questions each. Pause.

The solution, ours, run in code. The lengths are one, two, three, four, four. The average is one point eight seven five, and the entropy is one point eight seven five. They are equal because every share is a power of one half. After the change, the old script costs two point five. The entropy is two point two five, and the new best lengths are two, two, two, three, three, which cost two point two five. The old script stops being best because it was built for the old shares.

Second, the notebook. It has eight exercises, each with a hint and a folded solution. It needs Python three point nine or later, numpy and matplotlib, and uses fixed seeds. Run a cell, change one line, and watch the number move. Every number from the reference run is in the results file, with its cell and what was run.

Recap. The stall teaches that a script is right only for its own shares. The notebook lets you move one number at a time.

## recall | Test yourself
Eight questions. Answer aloud, then listen to the answer. The ones marked as returning will come back in later posts.

One. Why does the measure use a logarithm? The chances of independent days multiply, and a log turns a product into a sum, so surprisals add.

Two. What is the surprisal of an outcome whose share is one sixteenth? Four questions' worth.

Three. What does one point seven five bits mean for the village? The best script of fair yes or no questions needs one point seven five questions per day on average, in this village.

Four. Why is one point seven five lower than two, and when would the best script average exactly two? The shares are uneven, so common words get short strings. For four equally likely words.

Five. What does entropy not measure? Meaning, value, truth or importance. Shannon sets meaning aside for the engineering problem: scope, not denial.

Six. Who encodes and who decodes? The side with the original and the script encodes. The side with only the string and the same script decodes.

Seven. Name two assumptions needed before an entropy means anything. Any two of: known shares, stable shares, independent days, enough data to estimate the shares.

Eight. Which claim about reading effort is empirical, and who makes it? That effort is associated with predictability: Gibson and colleagues, citing Hale and Levy. Not a theorem.

Recap. A surprise is worth the log of one over its share. Entropy is the average. It depends on a stated model, and it leaves meaning out. That is the whole post.
