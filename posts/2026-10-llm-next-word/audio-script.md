---
post: 2026-10-llm-next-word
voice: kokoro af_heart
note: Written for the ear. Formulas are spoken in words. Each chapter ends with a short recap so it can be looped alone.
---

## hook | The guessing game
Welcome to AI4Read. This is post one: what does a language model know when it predicts the next word?

Let's start with a game. Take a book you have never read. Cover the page, and uncover it one letter at a time. Before each letter, guess what it will be. If you are wrong, guess again, until you are right. Then write down how many guesses you needed.

Claude Shannon ran this experiment and published it in nineteen fifty-one. Most of the time, the answer was one. The person guessed right on the first try. In one run, seventy-nine of one hundred and two letters were right on the first guess. That is about seventy-seven percent.

Then Shannon made a surprising point. Imagine an identical twin of the guesser. Give the twin only the list of guess numbers. At each position, the twin guesses in the same order as the first person, and stops at the right number. So the twin can rebuild the whole text. The lesson is simple, and it is the seed of this whole post. A good predictor is also a good compressor. The better you predict, the shorter the message you need.

Today we have machines that play exactly this game, at a huge scale. A large language model reads text one token at a time. A token is a word, or a piece of a word. For every possible next token, the model gives a probability.

Here is an example from the GPT-3 paper. "Alice was friends with Bob. Alice went to visit her friend, blank." The answer is: Bob. To fill that blank, you need more than spelling. You need to keep track of who is who.

So here is our question. To predict the next word this well, what does a machine have to know? Only which words follow which? Facts about the world? Or something about the minds of the people who wrote the text?

Recap. Shannon's guessing game shows that prediction and compression are two sides of one coin. A language model is a machine that plays this game. Our job is to find out what kind of knowledge the game requires.

## guess | Guess first
Before we go on, make three predictions. Say your answer out loud. A wrong guess you remember is worth more than a right answer you only read.

Prediction one. Shannon asked people to predict English text, with a long context of up to one hundred letters. On average, how much new information does one letter carry? Is it about four point seven bits, about two point six bits, about one bit, or about a tenth of a bit?

Prediction two. GPT-3 has one hundred and seventy-five billion weights. It can learn a new task from five examples written in the prompt. When it does, how many of those weights change? All of them, a few million, or none?

Prediction three. GPT-4 answers a classic false-belief story correctly almost every time: ninety-seven point five percent. Researchers change one small detail. An object is put on a box, instead of in it, so the person coming back can see where it is. How often is GPT-4 right now? About ninety-five percent, seventy percent, forty percent, or about zero?

Hold on to your answers. You will hear them in the next chapters.

## home | How a language model is built
All the models in this story, from two thousand and three to two thousand and twenty, are trained on the same task. Only the machinery changes. Here is the story in eight short steps.

Step one. A sentence is a chain of guesses. The probability of "the cat sat" is the probability of "the", times the probability of "cat" after "the", times the probability of "sat" after "the cat". This is just the rule of conditional probability, used again and again. So a model that predicts the next token well can also score whole texts.

Step two. Counting runs out of data. The oldest method is to count how often one word follows a few others. These are called n-gram models. But the numbers explode. Bengio and colleagues give an example: to model ten words in a row, with a vocabulary of one hundred thousand words, you would need up to ten to the power of fifty free numbers. Most word sequences never appear in any corpus. This is called the curse of dimensionality.

Step three, two thousand and three. Give every word a vector, a short list of thirty to one hundred numbers, and learn these vectors together with the predictor. Similar words are expected to end up close together. Then one sentence, "the cat is walking in the bedroom", also helps the model with "a dog was running in a room".

Step four, twenty thirteen. Mikolov and colleagues made word vectors cheap enough to train on billions of words. And they found a surprise. Some relations became directions in space. The vector for "biggest", minus "big", plus "small", lands near "smallest".

Step five, twenty seventeen. Attention. In a Transformer, every position looks at other positions and takes a weighted average of what it finds. To predict text from left to right, a mask stops each position from looking at the future.

Step six, twenty nineteen. Tasks are text too. Put "T L D R" after a news article, and the model tends to continue with a summary. The summaries were weak. But the GPT-2 authors made a speculation that frames this whole post: a model with enough capacity will begin to infer and perform the tasks shown in text, in order to better predict them.

Step seven, twenty twenty. Learning inside the prompt. Show GPT-3 a few examples of a task, and it often continues the pattern. This is called in-context learning. And here is the answer to prediction two. The number of weights that change is: none. The learning happens while the model reads the prompt. The weights stay the same.

Step eight. Scaling laws. Kaplan and colleagues found that the loss on new text falls smoothly as models get bigger. Each doubling of model size multiplies the loss by about zero point nine five. But they warn that a smooth loss may hide sudden changes in what the model can do.

Recap. One training signal runs through all eight steps: make the next token less surprising. Everything an LLM can do either comes from this signal, or rides along with it.

## lens-info | Lens one: information theory
Our first lens is information theory. Here the link is not an analogy. It is the same math. The training loss of a language model is Shannon's average surprise.

Shannon's nineteen forty-eight paper begins by setting meaning aside. He says the meaning of a message is irrelevant to the engineering problem. What matters is that a message is chosen from a set of possible messages. Remember this choice. It made the theory possible, and it also limits what this lens can tell us.

If something has probability p, its surprise is minus log base two of p, measured in bits. A fair coin flip carries one bit. Something with probability one eighth carries three bits. Entropy is the average surprise of a source. Cover and Thomas give a nice picture: entropy is about the smallest average number of yes or no questions you need to find out what happened. For our weather example later, it is exactly that number.

Now the key fact. Suppose the truth is p, but your model is q. Then your average surprise is not the entropy of p. It is the entropy of p, plus an extra cost called the K L divergence, or relative entropy. The K L divergence is the price of believing q when the truth is p. It is never negative, and it is zero only when the model is exactly right.

A language model is trained to make its average surprise on real text as small as possible. The entropy of the language is fixed. So the only thing training can reduce is the K L divergence: the distance between the model and the truth about text.

A warning about names. In machine learning, entropy plus K L divergence is called cross-entropy. But in Cover and Thomas, cross entropy is listed as another name for relative entropy itself. And Shannon used "relative entropy" for something else again. Always check what a writer means.

Context lowers surprise. If you know nothing at all, a letter of English carries about four point seven bits. Using letter frequencies, about four point one. Knowing one letter before it, about three point six. And with long context, up to one hundred letters, he estimated something of the order of one bit per letter. That is the answer to prediction one: about one bit. It is a careful estimate from human guessers on one book, not a law of nature.

Kaplan made a related guess about machines. His scaling laws probably break down at or before about one point seven nats per token. A nat is like a bit, but uses natural logarithms. He adds a conjecture: that number might roughly estimate the entropy of language. He says it could be off by a factor of ten.

Recap. In this lens, the model knows exactly as many bits about text as it saves. That is precise and measurable. But Shannon built the theory by setting meaning aside. So this lens cannot tell us what those bits are about.

## lens-linalg | Lens two: linear algebra
Our second lens is linear algebra. Attention is the same math as a weighted average. But the idea that meaning is geometry is only a structural analogy, and it only partly holds.

Mikolov, Yih and Zweig took a model trained only to predict words. Nothing in it was built for grammar or meaning. Yet relations appeared as rough directions. Apple minus apples was close to car minus cars. To answer "a is to b as c is to what?", you take b, subtract a, add c, and look for the nearest word, measured by the angle between vectors. This is called cosine similarity.

How well does it work? Their best model got about forty percent of eight thousand grammar questions exactly right. A later model, with much more data, reached about sixty-six percent. So the arrows are real, but rough. About forty to sixty-six percent of analogies work exactly.

Now attention. Each position makes three vectors. A query: what am I looking for? A key: what do I contain? And a value: what do I pass on? The output is an average of the values, weighted by how well the query matches each key. The match scores go through a softmax, which turns any list of numbers into probabilities. Before the softmax, the scores are divided by the square root of the vector size, to keep them from growing too large.

Some attention heads seem to link a pronoun like "its" to the noun it refers to. But a picture of attention weights is a hint, not proof.

Recap. In this lens, the model knows relations between words, stored as positions and directions, and it has a way to mix information from earlier words. The geometry is real but approximate. Whether geometry is meaning is a question for lens four.

## lens-bayes | Lens three: Bayesian inference
Our third lens is Bayesian inference.

Here is a puzzle. "Albert Einstein was German. Mahatma Gandhi was Indian. Marie Curie was." The model says: Polish. Nobody told it the task is nationality. How does it know?

Xie and colleagues offer an idea. Imagine every document in the training data was written under some hidden concept: a topic, a format, a task. To predict the next word of a document well, the model has to guess which concept is active. A perfect predictor does this guessing implicitly, by averaging over all concepts, weighted by how likely each concept is, given the prompt.

A few-shot prompt is evidence. Each example makes the true concept more likely, and the wrong ones less likely. When the evidence piles up, the model in effect selects one concept. So in-context learning looks like Bayesian inference, with no change to the weights.

Xie proves this, but only inside a simplified world. Documents come from a mixture of hidden Markov models. The model fits its training data exactly. And the concepts must be different enough from each other. Their synthetic tests also show limits. With concepts never seen in training, in-context learning failed. And just changing the order of the examples moved accuracy by ten to forty percent.

Recap. In this lens, the model knows a prior over the kinds of documents people write, and it can narrow that prior down from a prompt. It is a clean story. But it is a theorem about a model of text, not proof that real language models compute posteriors. The authors call it a first step.

## lens-meaning | Lens four: philosophy of meaning
Our fourth lens is the philosophy of meaning.

Bender and Koller define meaning as the relation between a form, like a sentence, and the speaker's communicative intent. From this they argue that a model trained only on form cannot, in principle, learn meaning.

They tell a story. Two people, A and B, are stranded on two islands. They talk through an underwater cable. A clever octopus taps the cable. It learns the patterns of their messages, and starts answering in B's place. In small talk, the octopus may pass. Then A writes that a bear is attacking, and asks how to defend herself with some sticks. The octopus has never seen a bear or a stick. It can only produce text that looks like an answer.

But note: Bender and Koller do not say language models learn nothing. They grant that BERT has probably learned something about meaning.

Piantadosi and Hill reply. The octopus argument assumes that meaning is fixed by reference, by pointing to things in the world. But many words, like "justice", have no clear thing to point to. On the conceptual role view, meaning comes mostly from how a concept relates to other concepts. Whether next-word prediction can discover those relations is an empirical question. So far, they say, the answer is a promising, partial yes.

Mahowald and colleagues offer a cleaner split. Formal competence is knowing the rules and patterns of a language. Functional competence is using language to do things in the world. In the human brain, these rely on different systems. For English, language models are close to human level on formal competence. Their functional competence is patchy.

Recap. What the model knows here depends on your theory of meaning. If meaning needs a link to intentions and the world, form alone gives a reflection at best. If meaning is mostly relations between concepts, prediction may build part of it. That is why more data alone cannot settle this debate.

## lens-tom | Lens five: theory of mind
Our fifth lens is theory of mind: the ability to think about what other people believe, even when their beliefs are false.

A classic test. A bag full of popcorn has a label that says "chocolate". Sam has never looked inside. What does Sam think is in the bag? To answer, you must track what Sam believes, not what is true.

Kosinski gave forty tasks like this to a series of models, with strict scoring. A task counted only if every version of the story was answered correctly. ChatGPT-4 solved seventy-five percent, which he compares to six-year-old children. He suggests this ability may emerge as a by-product of language training. And he is careful: failures do not necessarily show inability, and successes do not prove theory of mind.

Ullman made small changes to such stories. For example, make the popcorn bag transparent, so Sam can see the popcorn. On one of two prompts, GPT-3.5 still answered "chocolate" with high confidence. Ullman's rule is that one clear failure can outweigh many average successes. Has theory of mind emerged? His answer: probably not.

Shapira and colleagues tested fifteen models on six datasets. No model showed robust theory of mind on all of them. And here is the answer to prediction three. GPT-4 scored ninety-seven point five percent on the original stories, and zero percent when the object was put on the box instead of in it.

But there is a twist. Strachan and colleagues tested almost two thousand humans as well. Humans also failed about half of Ullman-style changes. And when GPT-4 seemed to fail at noticing a faux pas, it was mostly refusing to commit. Asked what was more likely, it answered perfectly.

One more warning. Ullman and Shapira criticized an earlier preprint of Kosinski's paper, which reported higher scores. The published version uses stricter controls and lower scores. Always check which version a critique answers.

Recap. The model knows enough about how people write about beliefs to pass many standard tests, but not robustly under small changes. And the two sides disagree about evidence itself: does one failure decide, or does a failure not necessarily show inability?

## ladder | The math ladder, spoken
This chapter walks through the math ladder in words. The page has the numbers and the interactive versions.

Rung one, the chain rule. Shannon's small language has three letters, A, B and C. The chance of the text "B A B" is the chance of B, sixteen over twenty-seven, times the chance of A after B, one half, times the chance of B after A, four fifths. That is about zero point two four.

Rung two, entropy. Our toy village has four weather words: rain with probability one half, sun one quarter, wind one eighth, and snow one eighth. Their surprises are one, two, three and three bits. The average, weighted by probability, is one point seven five bits. A code of zero, one-zero, one-one-zero and one-one-one has exactly that average length.

Rung three, cross-entropy. If your model thinks all four words are equally likely, you pay two bits per word: one point seven five for the language, plus zero point two five for being wrong. If your model has the order reversed, you pay two point six two five bits. The extra part is the K L divergence.

Rung four, perplexity. Two to the power of the average surprise. The true weather model has perplexity about three point three six. The uniform model, four. The reversed model, about six point one seven. Read it as: the model is as unsure as if it were choosing among this many equally likely words.

Rung five, context. For the three-letter language, the uncertainty of the next letter falls from about one point five nine bits with no knowledge, to one point two five with letter frequencies, to zero point nine three if you know the previous letter.

Rung six, attention by hand. Three tokens, with scores turned into weights by a softmax. For the third token, the weights come out as about a quarter, a quarter, and a half.

Rung seven, analogies. King minus man plus woman gives a vector closest to queen, with cosine about zero point nine two.

Rung eight, in-context learning as a posterior. With two concepts and evidence four times stronger for the true one in each example, the posterior climbs from one half to zero point eight, then zero point nine four, then above zero point nine eight.

Rung nine, power laws. Each doubling of model size multiplies the loss by two to the power of minus zero point zero seven six, which is about zero point nine five. But scaling only shrinks the K L part. The floor is the entropy of language.

Rung ten. Shannon turned guess numbers into bits. The entropy of the guess numbers is an upper bound on the entropy of the text, because the guess numbers are a code for the text.

## answer | So what does it know?
Let's put the five lenses together. They give four layers of answer, from the most certain to the most contested.

Layer one: bits about text. This is certain and measurable. A lower loss means the model is closer to the true distribution of text.

Layer two: structure in text. This is well supported. Grammar, close to human level in English. Relations between words, as directions that work for about forty to sixty-six percent of analogies. And task formats that a prompt can select, proved in a simplified model.

Layer three: meaning. This depends on your theory of meaning. At most a reflection, if meaning needs intentions and the world. Possibly part of the foundation, if meaning is mostly relations between concepts.

Layer four: minds. This is contested. Many tests are passed, but small changes often break the result, and humans fail some of those changes too.

Here is the one sentence to remember. The loss tells you how much a model knows about text. It cannot tell you what kind of knowledge that is. To learn that, you must change the test in small ways and see what breaks, or look inside at the relations the model has built.

## work | Where this shows up in your work
Five links to your research.

For LLM surrogate labeling: if few-shot prompting works by selecting a concept, your examples are evidence, not instructions. In Xie's synthetic tests, example order alone moved accuracy by ten to forty percent. So randomize the order across runs, and report the spread.

For cross-lingual safety: tokens cover different amounts of text in different languages. Per-token loss cannot be compared directly. Use bits per character, or per byte. In our test with GPT-2, a Japanese sentence looked better per token, but was far worse per character.

For explainable representations: directions in embedding space are real but rough. Before you name a direction, check how often it gives the exact answer.

For framing and misinformation: surprise is measurable. It tells you how far a post is from a community's usual language. It does not tell you whether the post is true.

And for social simulation with language model agents: agents may pass standard belief stories, and still fail under small changes. Add perturbation tests to your checks.

## recall | Recall questions
Here are recall questions. After each one, pause the audio and answer out loud. Then listen to the answer.

Question one. Why is a good predictor also a good compressor?
Answer. Because the list of guess numbers is a code for the text. An identical predictor can decode it.

Question two. The training loss of a language model has two parts. Name them, and say which one training can reduce.
Answer. The entropy of the language, and the K L divergence between the truth and the model. Training can only reduce the K L divergence.

Question three. What is the perplexity of the uniform weather model?
Answer. Four. Two to the power of two bits.

Question four. In Xie's account, what does a few-shot prompt do?
Answer. It is evidence about a hidden concept. The model in effect selects the concept, with no change to its weights. This is proved only in a simplified model.

Question five. What does the octopus argument assume, according to Piantadosi and Hill?
Answer. That reference, the link to things in the world, determines meaning.

Question six. Why does it matter which version of Kosinski's paper a critic answers?
Answer. The critics answered an earlier preprint with higher scores. The published version reports lower scores, with stricter controls.

## english | How to say it in English
Ten useful phrases from this post. Listen, then repeat each example sentence.

One. To set something aside. Shannon set meaning aside to solve the engineering problem.

Two. A by-product of. Theory of mind may be a by-product of language training.

Three. In principle. Bender and Koller argue that form alone cannot lead to meaning, in principle.

Four. To be agnostic about. The GPT-3 authors are agnostic about whether the model learns tasks from scratch.

Five. To hold up under. The result did not hold up under small changes to the story.

Six. To over-generalize from. Shapira argues that earlier work over-generalized from a handful of examples.

Seven. An upper bound on. The entropy of the guess numbers is an upper bound on the entropy of the text.

Eight. To be at ceiling. On the basic false-belief test, both humans and GPT-4 were at ceiling.

Nine. A talking point, not a result. Our bits-per-letter conversion is a talking point, not a result.

Ten. The burden of proof lies with. Ullman thinks the burden of proof lies with those who claim the ability has emerged.

That's the end of post one. Thank you for listening.
