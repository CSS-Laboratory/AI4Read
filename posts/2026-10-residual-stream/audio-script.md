---
post: 2026-10-residual-stream
voice: kokoro af_heart
note: Written for the ear. Formulas are spoken in words. Widgets are described, not read. Fold-outs and tables are only mentioned. Each chapter ends with a short recap so it can be looped alone. The post stands alone and never refers to another post.
---

## hook | The list in the middle
Welcome to AI4Read from CSS Lab. This is post three: what is a hidden state?

Stop a language model halfway through its work and copy out the list of numbers it holds for one word. The list is long. The small model GPT-2 has seven hundred and sixty-eight numbers in it. Qwen3 one point seven billion, whose configuration file we read for the notebooks, has two thousand and forty-eight. A list of numbers is called a vector, and the number of entries in it is its dimension.

People do three things with such lists. They train a small classifier on them, to see whether a property of the text can be read off. They compare the lists from two models. And they add one list to another, to push the model somewhere. All three treat the list as a definite object. So what is it?

Keep one everyday picture, as a picture only, and the picture is ours. A bank balance on the twentieth of the month is the opening balance plus every deposit and withdrawal since then, and a later withdrawal can cancel an earlier deposit. Now imagine thousands of accounts at once, with each part of the model depositing or withdrawing in every account, and none overwriting what is there. The post tests how far this holds.

A short version, again ours. The list is a running sum of what the earlier parts of the model wrote. Reading it along a direction is a dot product. Pushing it is adding a vector. Whether a concept is a direction is a bet, not a fact.

We check the first claim on a real model in the two notebooks that come with this post. The vocabulary and the bets come from three published sources, none of them about today's model families. The post says so where each first appears.

Recap. A hidden state is a long list of numbers. People probe it, compare it and push it. The post asks what the list is, and answers with a running sum that we can check.

## guess | Three predictions
Three predictions. Commit to an answer before you read on. A wrong guess you remember is worth more than a right answer you only read. The answers come in the sections named on the page.

Question one. A model is a stack of rounds of work called blocks. You stop it after block six and copy the list it holds for one word. What is that list?
Pause.
Option one: the model's best guess so far, written as a list of numbers. Option two: a running total, the word's starting list plus every addition made so far. Option three: the newest block's output alone, with nothing kept from before. Option four: a summary of the whole sentence, shared by all of its words.

Question two. A shared list already holds two, two. Block three now writes minus two, minus two into it. What can a later block read from the list?
Pause.
Option one: both vectors, kept as two separate items in order of arrival. Option two: only minus two, minus two, because the newest write replaces the old one. Option three: only the sum, zero, zero, and neither vector can be read back on its own. Option four: only two, two, because the first write is kept for good.

Question three. A probe gives each point in a cloud a score: multiply its two coordinates by two fixed numbers and add the results. Now add the same vector to every point of the cloud. By how much does each score change?
Pause.
Option one: by the same amount for every point. Option two: by more for points far from the origin. Option three: only for points that lie near the probe's line. Option four: by an amount that depends on each point's length.

Recap. Three questions: what the list is after block six, what a later block can read after two writes cancel, and how a score moves when every point is pushed by the same vector. Keep your three guesses.

## sum | The stream is a running sum
Start from words. A language model reads text as tokens: whole words or pieces of words. Its first step is a lookup. A table holds one list of numbers for each token, and the model copies out the list for the token it is reading. We call this starting list the embedding and write it x zero. We keep the word embedding for this one list, because the sources use it in four ways. GPT-2 also adds a learned list for the token's position.

From that start, the model keeps one working list for the token, and every part of the model changes it by adding to it. We call it the residual stream, or the stream. GPT-2 small has seven hundred and sixty-eight numbers in it and twelve blocks. Our toy uses two numbers, so that every list can be drawn on paper.

Now add two vectors by hand, before any diagram. A part of the model adds the vector two, minus one to a stream that holds one, two. Add the first numbers: one plus two is three. Add the second numbers: two plus minus one is one. The answer is three, one. As a rule: the vector a, b plus the vector c, d is a plus c, b plus d. First plus first, second plus second. The same rule holds for seven hundred and sixty-eight numbers.

A model has a stack of blocks. Each block has two parts in a fixed order: first attention, then an MLP, short for multi-layer perceptron, a small network. We say block for the pair and sub-layer for each part, because the word layer is confusing. Each sub-layer looks at the stream, computes a vector, and adds it to the stream. It never overwrites it. We call the vector a sub-layer adds its write. Call a k the write of attention in block k, and f k the write of the MLP.

Now the toy. The embedding is one, two. Block one writes two, minus one and then minus one, one. Block two writes three, minus two and then minus one, two. In the stepper, tap Next to add each row. The stream goes one, two; then three, one; then two, two; then five, zero; and ends at four, two. In the bus diagram, the same five writers add to one shared stream, and the last box only looks at it. The second number of the last write, plus two, undoes the minus two that attention wrote. Writes add, so they can cancel.

The pattern: the stream after k blocks is the embedding plus every write up to block k. Elhage and colleagues put it this way: the residual stream is simply the sum of the output of all the previous layers and the original embedding. This sum is bookkeeping. It tells you what is in the stream, not what any writer meant. It is also the picture of Elhage and colleagues' toy models, which ignore layer normalization. Real models differ.

One stream per position. Take the two-word input red car. The model keeps one stream for each word, at every depth. Only attention carries information between positions, and in a decoder-only model, only from earlier positions. So there is no hidden state of a sentence.

Is the hidden state the stream? Libraries do not say residual stream. They return lists they call hidden states, and none of the three sources uses that phrase, so we have to test the identity. Copy the list the library returns after k blocks. Separately, record the starting list and every write inside the blocks, and add them. If the sum equals the copied list, up to rounding, the two are the same vector.

We ran this on GPT-2 small, with twelve blocks, on a CPU, with thirty-two-bit numbers. Adding the writes in the model's own order gave a difference of exactly zero. That proves little, because the check repeats the model's own additions. The informative lines are these. Adding the same writes in another order gave a relative difference of about one in a million, one point oh three times ten to the minus six, which is what thirty-two-bit rounding gives. And the TransformerLens stream agreed with the Hugging Face list within seven point eight times ten to the minus seven, relative.

The index convention matters. Entry l of the library's list is the input of block l, so it is the stream after l blocks, and entry zero is the embedding. The last entry is different: the library replaces it with the model's final output, which has been through the final norm. So the hidden state at the last layer is not a stream vector.

What we did not run: any trained Qwen3, Llama, Gemma or Mistral model. For Qwen3 and Gemma 3 we ran tiny random models, which test indexing and hooks. For Llama and Mistral we only read code. In Gemma 3 the code scales the embedding by the square root of the width, and norms each sub-layer's output before adding it. In the tiny Gemma 3, hooks on the attention and MLP modules failed the additivity check, and hooks on the two norm layers passed.

There is a short term box on the three names, and a trap box on where the bus picture misleads: a computer bus has one writer at a time and addresses, and the stream has neither.

Prediction one. The answer is a running total. In GPT-2 small, the list after block k is the embedding plus every write so far, up to rounding. Limits: one list per word, the last list is normalised, and no trained Qwen3, Llama, Gemma or Mistral model was run.

Recap. The stream is the embedding plus every write, one list per word. We checked it on GPT-2 small, up to rounding, with the last entry as the exception. The informative checks are the reordered sum and the library comparison. We ran no trained Qwen3, Llama, Gemma or Mistral model.

## bets | Three bets
The lens we want to end with has three parts: concepts live as directions, behaviours are circuits, and the same things recur in different models. We cannot prove any of them here. Olah and colleagues, writing in twenty twenty about an image-recognition network, offered them as three claims and said: these claims are deliberately speculative. We treat each as a bet, and say how firmly the authors held it.

Bet one: features are directions. The claim: features are the fundamental unit of neural networks; they correspond to directions. A feature is a property of the input that a model can compute. A concept, in this post, is our human label for a feature, such as calm. By direction they mean a linear combination of neurons in a layer: a weighted mix of units. The stream has no neurons, Nanda writes. So for the stream, direction means a weighted mix of its coordinates, drawn as an arrow. That is ours.

How firmly? Olah and colleagues write that thousands of hours of studying individual neurons have led them to believe that neurons are typically understandable, and they concede that the community is divided on whether this is true. Nanda backs features as directions with an intuition, not evidence. About the neuron version he writes that there is a decent amount of empirical evidence for Inceptionv1, but it seems at best only slightly true for transformers. For the stream of a language model, none of the three sources tests whether concepts are directions.

Bet two: features are connected by weights, forming circuits. A circuit is a computational subgraph of a neural network: some features and the weighted connections between them. It has nothing to do with electricity. Their strong line is about small circuits: statements about behavior become questions of mathematical reasoning. The step to whole behaviours is hedged: it seems like, with sufficient effort, statements about model behavior could be broken down into statements about circuits. The evidence is two circuits in a vision network. The test they propose, editing the weights and checking a prediction, is a plan. They give no example of a behaviour such as refusal or trust.

Bet three: the same features and circuits recur across models. The authors suspect it is likely true, but the only evidence they can offer is anecdotal. It is the only one of the three that, in their words, wouldn't be completely fatal to circuits research if false. Nothing in the page is about one model before and after fine-tuning.

A trap: three sources, three vintages. Olah uses a vision network. Elhage studies attention-only transformers with two layers or fewer. Nanda writes a glossary that is mostly a description of how GPT-2 works. None of the three says anything about Qwen3, Llama, Gemma or Mistral, about base versus instruct models, or about post-training. There is a fold-out that sorts Olah's lines by firmness.

Recap. Three bets: features are directions, circuits are the way features connect, and the same things recur across models. All three are deliberately speculative. The third is the only one not fatal if false. The sources are about older and smaller models than the ones people use now.

## rw | Reads and writes
Every part of the model also reads the stream before it writes. Take one small reader inside block two's MLP: a neuron with an input vector r equal to one, two. It looks at the stream after attention two, which holds five, zero. What single number does it get? Multiply matching numbers and add: one times five plus two times zero is five. The vector r says how much to care about each place. With r equal to one, zero the reader takes only the first number.

The formula: r dot x equals r one times x one plus r two times x two. First times first plus second times second. This is the dot product. Nanda says reading is a projection, and Elhage and colleagues say layers read by performing a linear projection. In our terms, a linear projection is a set of dot products. We call the number a score.

Who hears whom. The stream is a sum, and the dot product of a sum is the sum of the dot products. So a read splits into one share for each writer. With r equal to one, two, the shares are five for the embedding, zero for attention one, one for MLP one, and minus one for attention two. They add up to five, the same as the direct read. In the widget, you can change r and watch the shares. Can you find a reader that cannot hear attention one?

Two things to notice. First, attention one wrote two, minus one and it sits in the stream, yet this reader hears none of it. Two vectors whose dot product is zero are called orthogonal, at right angles. Second, reading is not the opposite of writing. Nanda: these operations are not opposites. A reader along r does not get back what a writer put along r, unless the other writers are orthogonal to r.

Does the split work on a real stream? In notebook two, GPT-2 small's stream at the last position after six blocks, read by a random unit vector, gives seven point two one one five six one, and the sum of its thirteen shares gives the same. The difference is exactly zero because the shares are added in the model's own order. It is the toy's arithmetic, nothing more. A real model also puts a norm in front of every read. There is a fold-out on what a norm does to the arithmetic, at the end of the next section.

A write adds, and writes can cancel. MLP two writes minus one, two into a stream that holds five, zero. Nothing is replaced: five, zero plus minus one, two is four, two. The extreme case is the second prediction. The list holds two, two and block three writes minus two, minus two. The sum is zero, zero, and every reader gets zero. Does this happen in real models? Elhage and colleagues offer only a hint, that some neurons and heads may perform a kind of memory management role. Our toy shows cancellation is possible by arithmetic, not that models do it.

Prediction two. Only the sum, zero, zero. A write adds, it does not replace, and it is not kept as a separate item.

Cashing in bet two. The widget's table gives one number for every pair of writer and reader. That is the shape of a weighted edge in a circuit, so it is like an edge weight, in our words. It is not one of Olah's edges. The word linear has three uses here. The stream is a sum of writes. A read is linear in the stream. And a concept can be read linearly is a bet. The layers' own computations are not linear.

Recap. A read is a dot product. It splits into one share per writer. A writer whose vector is orthogonal to the reader goes unheard. Writes can cancel. All of this is exact arithmetic, and none of it shows that real models behave this way.

## dir | Probe and push
Now many streams at once. Take six streams at one depth, for six short prompts. These are toy numbers, ours. Three are labelled calm and three urgent. The calm points are three, one; four, two; five, three. The urgent points are one, three; two, four; three, five. Can one number per point tell the groups apart? Try the coordinates. Along the first axis the groups overlap at three, and along the second axis too. No single coordinate separates them.

Now turn a reading arrow. A direction is an arrow of length one, by our convention. The arrow minus one, one has length root two. Divide by it and you get u equal to minus zero point seven oh seven, zero point seven oh seven: second minus first, scaled. The score of a point is u dot x. For the calm point four, two the score is minus one point four one four. Every calm point scores minus one point four one four, and every urgent point scores plus one point four one four. One number separates the groups. The gap between them, which we call the margin, the lowest urgent score minus the highest calm score, is two point eight two eight.

With the angle phi measured from the first axis, a unit arrow is cosine phi, sine phi, so the score is x one cosine phi plus x two sine phi. In the widget, drag the blue arrow and watch the margin. At zero degrees the margin is minus four, at forty-five degrees minus two point eight two eight, at ninety degrees zero, at one hundred and twenty degrees two, and at one hundred and thirty-five degrees two point eight two eight. At forty-five degrees both groups get the same three scores. That probe is blind.

A probe is a read whose direction was fitted on labelled examples. Nanda defines a probe as a one-dimensional linear map, corresponding to a direction in activation space, which likely corresponds to that feature. Keep the word likely. A high score shows that information is present along the direction. It does not show that the model uses it. Cashing in bet one: if concepts were directions, this is what it would look like. Nothing here shows that a language model stores calm this way.

Steering is a translation. Add the same vector v to every point. The dot product of a sum is the sum of the dot products, so every score moves by the same amount, u dot v. The formula: s of x plus v equals s of x plus u dot v. With v equal to two u, every score rises by two. Push sideways, and u dot v is zero, so no score moves, although every point moved. A push is a translation. It is not linear, because a linear map sends zero to zero, and adding v sends zero to v. A linear step plus a constant is affine.

What this does not say. Steering and activation addition do not occur in any of the three sources, so nothing here says that adding a vector changes behaviour as intended. On a real stream the arithmetic holds: in notebook two, u dot of h plus alpha u, minus u dot h, minus alpha, was zero for every alpha we tried.

Prediction three. By the same amount for every point.

Turn everything. Rotate the whole toy by ninety degrees: each x, y becomes minus y, x, and so does the reader. Every coordinate changes, but lengths and angles do not, so no dot product changes. The four shares are still five, zero, one and minus one. In symbols, R r dot R x equals r dot x. In the widget, the shares stay put at every angle while the second coordinate of the stream moves. A basis is the set of axes we write coordinates in. Elhage and colleagues assert, for their idealised linear stream, that it does not have a privileged basis. Nanda adds that the standard basis is always slightly privileged. The neurons of an MLP are different. So never read dimension seventeen as a feature. Compare vectors by dot products.

Cashing in bet three. Let model B be model A with everything rotated. The coordinates differ and every dot product is the same, so analogous can only mean the same up to a rotation, never the same coordinates. That is ours.

There are two fold-outs. One shows what a norm does to a read, with a toy where doubling the stream changes nothing after the norm. The other shows the logit lens as one more read: the last step of a model is a set of dot products, one per token.

Recap. A probe is a dot product along a fitted direction. In the toy, a turn of the arrow separates the groups, and one angle is blind. A push shifts every score by u dot v. Rotating everything changes every coordinate and no dot product. None of this shows what real models do.

## answer | Short answer
Here is the short answer, our reading and not a finding.

What is the list? In GPT-2 small, the list a library returns after k blocks, for k from zero to eleven, is the embedding plus every earlier write, up to rounding, at one position. The largest relative differences were seven point eight times ten to the minus seven against an independent record of the stream, and one point oh three times ten to the minus six with the writes added in another order. The library's last entry is final-normed, so it is the exception. For a trained Qwen3, Llama, Gemma or Mistral model we have no measurement. In code and tiny random models we found that Gemma 3 scales its embedding and norms each sub-layer's output before adding it. What would change our mind: an additivity error above rounding with the hooks placed correctly. None of the three sources uses the words hidden state.

What can you do with it? A probe is a dot product. Steering is a translation: it moves every score by the same amount, u dot v. Compare lists from two models by dot products, not coordinates, because the stream has no privileged basis, asserted for an idealised stream. All this is exact arithmetic. What a score means, or whether a push changes behaviour, the algebra does not say, and the sources never mention steering.

How firm is the lens? All three of Olah and colleagues' claims are deliberately speculative, and their evidence is a vision network. For language models the three sources give no test, so we hold all three as bets. The toys say what each bet would mean, not whether it is true.

Recap. The list is a running sum, checked in GPT-2 small. Probes and pushes are exact arithmetic. The lens is three bets, held lightly.

## lens-linalg | Lens one: linear algebra
The first lens is linear algebra, and the link is the same mathematics. The stream is a sum of vectors. A write is a vector addition. A read is a dot product. Steering is a translation. No privileged basis means a rotation leaves dot products unchanged. Only this bookkeeping is the same mathematics. The sub-layers themselves are not linear.

Seeing is not doing, in our words. A probe observes: it reads the stream. Steering intervenes: it writes into it. A high probe score shows that information is present along a direction, not that later parts of the model use it. That needs tests this post does not run, and none of the three sources addresses it directly. Nanda's caution about ablation, which means removing a part, is a reminder that edits can mislead. Zero ablation, he writes, is arguably unprincipled, because the model may be using that part as a bias term.

The sources differ in method. Elhage and colleagues pull apart the streams of communication in terms of virtual weights, rather than studying it directly. Nanda writes: the central object of a transformer is the residual stream. This is a difference of method, not of fact. Our reads sit on Nanda's side.

One more limit. Cosine similarity divides by two lengths, so it is not additive. In notebook two, with v equal to three u, the cosine of h plus v with u was zero point one three one eight, while the cosine of h with u plus the cosine of v with u was one point oh nine three five. A dot product splits over writers. A cosine does not.

Connection to your research, computation. Probing, similarity analysis and steering are three statements about one vector. This lens fixes what the vector is and which operations on it are exact.

Recap. Linear algebra gives exactness for the bookkeeping: a sum to check, a read that splits, a coordinate to distrust, a push to measure. It does not explain why concepts would be directions, anything nonlinear, or whether a probe's direction is used by the model.

## lens-info | Lens two: information theory
The second lens is information theory, and here the link is weaker. It is a structural analogy, ours: many writers add into one shared vector, and a reader sees only the sum. The words bus and bandwidth are metaphors. No theorem or number transfers.

This lens asks a question and does not answer it. A stream has d numbers, and a model may have more things to say than d. How many separate messages can one reader recover, if some interference is tolerated? The sources give no capacity number.

What the sources say. Elhage and colleagues note that a single MLP layer typically has four times more neurons than the residual stream has dimensions. They call the stream's dimensions something like memory or bandwidth: the words count dimensions. Nanda defines superposition as the case when a model represents more than n features in an n-dimensional activation space, and argues that with fifty thousand tokens and seven hundred and sixty-eight dimensions there almost has to be more features than dimensions. Almost matters: it is an argument, not a measurement. Olah and colleagues say that cars and dogs can share a neuron as long as they don't co-occur.

MacKay sets an exercise on a channel with two sets of inputs and one output. In a simple case the output is the arithmetic sum of the two inputs: zero, one or two, with no noise. If the output is one, the input state was zero, one or one, zero, and the receiver cannot tell who sent the one. We use no result from the exercise.

A toy, ours. The stream has two numbers. Three features are written along directions at zero, one hundred and twenty and two hundred and forty degrees. Each feature has a strength, and the stream is the sum. Three readers read along the same three directions. Write only feature one: the stream is one, zero and the readers hear one, minus one half and minus one half. Readers two and three hear something nobody wrote for them. Write all three: the stream is zero, zero, and the readers hear zero, as if nothing were written. The pattern: each direction dotted with itself is one, and two different directions give minus one half, the cosine of one hundred and twenty degrees. So read j equals c j minus one half of the other two strengths added. In the widget, find a setting that looks exactly like silence.

Where the analogy breaks. MacKay's users cannot hear the output of the channel, while later parts of a transformer read the stream before they write. His channel has two senders and one receiver. The stream has many writers and many readers. The sources give no rate, capacity or interference bound for the stream, so we do not claim it is a multiple-access channel.

Connection to your research, computation. If features share a stream, one probe direction may pick up several at once. Nanda writes, as an intuition, that for a bottleneck such as the stream the only interference to care about is other features with non-zero dot product with that direction. So any claim that a probe isolates a concept should say what else lies on the same line.

Recap. Information theory adds the question of limits: d dimensions, many messages, interference when directions are not orthogonal, and a case, all three on, that looks like silence. It does not tell us how much a real model packs in.

## turn | Your turn
Two notebooks, five exercises, one open question. Run the two notebooks that come with this post on your own computer. Notebook one uses GPT-2 small through TransformerLens. It checks the sum block by block, plots the stream's norm by depth, and runs the logit lens. Notebook two uses plain Hugging Face with hooks: set the model path to a model you have, and it finds which modules write, and tests additivity and the score-shift arithmetic. Each ends with blank exercise cells.

What to look for. The stream's norm grows with depth: the median over ordinary positions is about five before block one, fifty-eight after one block, and four hundred and seventy-two after twelve. Position zero, the start token, is far larger, and then drops at the end. We describe this and do not explain it. The final norm plus the unembedding reproduces the model's logits. TransformerLens, in compatibility mode, gives the Hugging Face stream minus its mean coordinate. In a tiny random Gemma 3, the guessed hooks fail the additivity check and the hooks on the two norms pass.

Exercise one, add. With the toy, compute the stream after block one and after block two, then find the MLP write that makes block two leave the stream unchanged.
Exercise two, who hears whom. For r equal to one, two, compute the four shares. Which writer is inaudible, and why?
Exercise three, project. Score the six points on one, zero; zero, one; and minus one, one over root two. Which gives a gap? Which direction gives both groups the same scores?
Exercise four, steer. Add minus two, two to every point and show every score on the probe rises by u dot v. Then add two, two. What changes, and which probe angle would see it?
Exercise five, rotate. Turn everything by ninety degrees, including r. Show that the four shares do not change. What does that say about coordinate two of the stream?
The solutions are folded on the page.

The transfer challenge. Take a direction you have used. Write one sentence each on the depth and position it was read at, whether a norm stood between the stream and the probe, what a shift of length alpha along it adds to every score, and which of these arithmetic settles and which needs a behavioural test.

One open question. Suppose, as a toy assumption, that a block acts on the stream as the matrix two, one; one, two. It turns one, zero into two, one, a new direction. But it sends one, one to three, three and one, minus one to one, minus one: only stretched, by three and by one. Are there always such directions? And if the stream has no privileged basis, could they be the natural axes that coordinates do not give us? Left open.

Recap. Run both notebooks and compare their numbers with the post. Do the five exercises by hand. Answer the transfer challenge for a probe you use. Keep the open question.

## work | In your work
Where this shows up in your work, in three parts.

Computation, reading: probing. A probe score shows that information is present along a direction, not that the model uses it. Nanda writes that a probe likely corresponds to the feature. With every probe result, state the depth, the position, and whether a norm stood between the stream and the probe. Run notebook two on your own model, and claim the identity only where its additivity check passes.

Computation, comparing and steering. Compare lists by dot products, not by coordinates. A steering vector is a translation, and the score shift is u dot v whatever the data. What it does to behaviour is an empirical question that none of the three sources addresses.

Communication, framing and priming. This is a candidate bridge. In the algebra, a prime or a frame added to a model is one more write along a direction. Whether a frame behaves like a direction is a bet of the same kind as bet one. It is a candidate, not a finding. For collaboration, there is no link in this post.

A working assumption, untested here. It is tempting to assume that a base model and its instruction-tuned version share the same stream space and directions. The sources define fine-tuning and RLHF only as training procedures, and say nothing about what they change inside a model. Testing that is later work.

Recap. Report the depth, position and norm placement of every probe. Compare by dot products. Treat framing as a bridge to test, and the base-versus-instruct assumption as untested.

## recall | Test yourself
Eight questions. Answer aloud, then listen to the answer.

One. What is the list that a library returns at index k, and what did the notebook check?
Pause.
For GPT-2 small and k from zero to eleven, the stream after k blocks. Writes added in another order differed by at most one point oh three times ten to the minus six, relative. The in-model checks give zero only because they repeat the model's additions. The last entry is final-normed.

Two. What must MLP two write to undo attention two, which wrote three, minus two?
Pause.
Minus three, two. Writes add, so they can cancel.

Three. Why does a read split over the writers, and when does a writer go unheard?
Pause.
The dot product of a sum is the sum of the dot products: one share per writer. A writer is unheard when its vector is orthogonal to the reader.

Four. Why does no coordinate separate calm from urgent in the toy cloud, and what does the blind probe show?
Pause.
Both groups reach three on each axis. At forty-five degrees both groups score the same three numbers.

Five. A push v moves every score by what? Why is it affine, not linear?
Pause.
By u dot v. A linear map sends zero to zero, and adding v sends zero to v. A linear step plus a constant is affine.

Six. What does no privileged basis let you do, and what does it not cover?
Pause.
Turn the stream and every reader together without changing any dot product, so compare by dot products, not coordinates. It does not cover MLP neurons, which have a privileged basis.

Seven. Which of Olah's three claims would not be fatal to circuits research if false?
Pause.
Universality. All three are deliberately speculative.

Eight. In attention, why divide the scores by the square root of d k?
Pause.
If the parts of q and k are independent with mean zero and variance one, q dot k has variance d k. Large scores push the softmax into regions with tiny gradients, the authors suspect. Scaling keeps them moderate.

Recap. The list is a running sum. Reads are dot products that split by writer. Pushes are translations. Coordinates mean nothing alone. The three claims are bets.
