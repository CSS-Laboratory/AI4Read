# Post 03 notebooks · results for citation

Produced 2026-10-25 in the build container. Every number below is printed by the saved notebook cell named in its row;
cell numbers are the execution counts `[n]` shown in Jupyter. Re-running gives the same numbers on the same versions
(no sampling; the one random direction is seeded).

## Environment of the reference run

| Item | Value |
|---|---|
| Python | 3.13.16, Linux x86_64 (2 CPUs, 7 GB RAM, no GPU) |
| torch | 2.14.1 (system install; the venv for TransformerLens reused it and did not replace or downgrade it) |
| transformers | 5.19.0 |
| transformer_lens | 4.3.0 (notebook 01). Also run under 3.9.0, both API paths, see "Cross-version check" |
| numpy / pandas / matplotlib | 2.5.3 / 3.0.5 / 3.11.2 |
| huggingface_hub / tokenizers / safetensors | 2.2.0 / 0.23.3 / 0.8.0 |
| dtype, device | float32, CPU, for every number below |
| Attention implementation | `eager` (Hugging Face models in both notebooks; TransformerLens forces it, see L1) |
| Offline | both notebooks were executed with `AI4READ_LOCAL_ONLY=1` (no network) after the models were cached |
| Prompt | "The cat sat on the mat because" |
| Models | 01: `gpt2` via TransformerLens and Hugging Face. 02: `openai-community/gpt2` (run with `AI4READ_MODEL_PATH=openai-community/gpt2`), a tiny random Qwen3 built from the `Qwen/Qwen3-1.7B-Base` config.json only, and a tiny random Gemma 3 text model from the library's default config |

**Tokenisation differs between the notebooks.** TransformerLens prepends `<|endoftext|>` (L4), so notebook 01 has
8 positions with the BOS token at position 0. The Hugging Face GPT-2 tokenizer adds no BOS, so notebook 02 has
7 positions starting at "The". Stream numbers are therefore not comparable across the two notebooks.

## Notebook 01 · `01_bus_gpt2.ipynb` (TransformerLens 4.3.0, GPT-2 small)

GPT-2 small, from the config (cell [4]): 12 blocks, d_model 768, 12 heads of 64, d_mlp 3072, vocabulary 50257,
context 1024, `gelu_new`, LayerNorm, learned position embedding.

| # | Quantity | Value | Cell |
|---|---|---|---|
| 1 | Tokens (position: token) | 0 `<|endoftext|>`, 1 The, 2 cat, 3 sat, 4 on, 5 the, 6 mat, 7 because | [5] |
| 2 | Per-block additivity `resid_post − (resid_pre + attn_out + mlp_out)`, all 12 blocks, processed weights | max abs **0.0**, max rel **0.0** (bit-exact) | [6] |
| 3 | Same, raw (unprocessed) weights | max abs 0.0, max rel 0.0 | [6] |
| 4 | `resid_mid − (resid_pre + attn_out)` and `resid_pre[L+1] − resid_post[L]`, all blocks | 0.0 | [6] |
| 5 | `resid_pre[0]` vs `hook_embed + hook_pos_embed` | 0.0 | [7] |
| 6 | Telescoping: stream after L blocks vs embedding + position embedding + all writes of blocks 0..L−1, L = 1..12 | max abs 0.0, max rel 0.0 | [7] |
| 7 | Same writes summed in another order (x₀ + Σattn + Σmlp) vs stream after 12 blocks | max abs **4.27e−4**, max rel **1.03e−6** (float32 rounding; float32 epsilon is 1.19e−7) | [7] |
| 8 | Why rows 2–6 are exactly 0 | the check adds the same float32 tensors in the same order as the model code; row 7 shows the size of rounding error when the order changes | [6], [7] |
| 9 | Stream norm, ordinary positions (1–7), median by blocks applied 0..12 | 5.3, 58.0, 58.2, 61.4, 64.7, 72.7, 81.1, 92.2, 105.5, 131.1, 172.7, 259.7, 472.4 | [8] |
| 10 | Stream norm, position 0 (BOS), blocks 0..12 | 10.3, 165.2, 641.8, 2577.0, 2775.8, 2929.7, 3026.1, 3084.1, 3119.1, 3141.1, 3152.7, 3155.5, 417.4 | [8] |
| 11 | Ratio of BOS norm to the median of the others, blocks 0..12 | 1.94, 2.85, 11.03, 41.95, 42.87, 40.28, 37.30, 33.45, 29.56, 23.96, 18.25, 12.15, 0.88 | [8] |
| 12 | Last position ("because"), norm after 0 / 6 / 12 blocks | 4.8 / 76.6 / 492.5 | [8] |
| 13 | Logit lens check: `unembed(ln_final(stream after block 12))` vs model logits | max abs **0.0** (processed and raw) | [9] |
| 14 | `unembed(stream after block 12)` without the final norm vs model logits (raw weights) | max abs 834.6 | [9] |
| 15 | Model's top next token after the prompt | " it" (log-prob −1.382) | [9] |
| 16 | Logit lens with final norm, top-1 at the last position, blocks 0..12 | destro, the, the, of, they, they, they, they, it, he, it, it, it | [9] |
| 17 | Rank of " it" under the lens with norm, blocks 0..12 | 2025, 1, 2, 3, 4, 2, 2, 1, 0, 1, 0, 0, 0 | [9] |
| 18 | Log-prob of " it" under the lens with norm, blocks 0..12 | −31.656, −1.805, −2.309, −2.217, −2.761, −2.856, −2.141, −1.822, −1.278, −1.608, −0.778, −0.400, −1.382 | [9] |
| 19 | Lens without norm (raw `W_U·x + b_U`), top-1, blocks 0..12 | because, then " the" at every block 1..12 | [9] |
| 20 | Rank of " it" without norm, blocks 0..12 | 377, 4, 4, 4, 4, 5, 3, 2, 2, 1, 1, 2, 12 | [9] |
| 21 | W9 toy, card §7 and §9 E1–E5, guess-first Q2/Q3, open question (M(1,0) = (2,1), M(1,1) = (3,3), M(1,−1) = (1,−1)) | all reproduced; each one is an `assert` | [10] |
| 22 | HF `len(hidden_states)` for 12 blocks | 13 | [11] |
| 23 | Raw TransformerLens stream after k blocks vs HF `hidden_states[k]`, k = 0..11 | max abs 4.88e−4, max rel 7.8e−7 (k = 0: exactly 0) | [11] |
| 24 | Raw TL stream after 12 blocks vs HF `hidden_states[12]` | max abs 404.3, rel 4.70 (mismatch: HF's last entry is final-normed, row 25) | [11] |
| 25 | `raw.ln_final(stream after 12 blocks)` vs HF `hidden_states[12]` | max abs 4.58e−5 | [11] |
| 26 | Processed TL stream vs HF `hidden_states[k]`, k = 0..11 | max rel 2.5e−2 to 4.3e−2 (they differ) | [11] |
| 27 | Processed TL stream vs (HF `hidden_states[k]` minus its mean over the 768 coordinates), k = 0..11 | max abs 7.3e−4, max rel 1.09e−6: **the processed stream is the HF stream with its mean coordinate removed** | [11] |
| 28 | Largest mean coordinate of an HF stream, k = 0..11 | 5.8e−3 (k = 0) rising to 4.90 (k = 11) | [11] |
| 29 | Norm ratio processed/raw stream, over positions and k | 0.9991 to 1.0000 (centring changes the norm by < 0.1% here) | [11] |
| 30 | Logits: raw TL vs HF | max abs 4.58e−5 | [11] |
| 31 | Logits: processed TL vs HF | max abs 108.9 | [11] |
| 32 | Logits: processed TL vs (HF minus its mean over the vocabulary) | max abs 5.13e−5 | [11] |
| 33 | Log-softmax: processed TL vs HF | max abs 4.20e−5 | [11] |
| 34 | HF `wte(ids) + wpe(positions)` vs raw `hook_embed + hook_pos_embed` | 0.0 | [11] |

## Notebook 02 · `02_bus_my_model.ipynb` (plain Hugging Face + forward hooks)

### 02-A · GPT-2 small (`openai-community/gpt2`, pretrained), 7 tokens, no BOS

| # | Quantity | Value | Cell |
|---|---|---|---|
| 35 | Found by inspection | blocks `transformer.h` (12); block children `ln_1, attn, ln_2, mlp`; final norm `ln_f` (LayerNorm, eps 1e−5); position embedding `wpe` added to the stream; no rotary module; `tie_word_embeddings` True and `lm_head` shares storage with `wte` | [4] |
| 36 | `hidden_states[0]` vs embedding module `wte(ids)` | rel 3.63 (relative to the norm of the reference, here the table rows; no match) | [7] |
| 37 | `hidden_states[0]` vs `wte(ids) + wpe(positions)` | 0.0 | [7] |
| 38 | Pair search, block 0: the two children whose outputs sum to (block output − block input) | `attn` + `mlp`, error 0.0 (next best pair: rel 0.90) | [8] |
| 39 | Child that receives (block input + attention write) as its input | `ln_2`, error 0.0 | [8] |
| 40 | (a) block output − (block input + attn + mlp), all 12 blocks | max rel **0.0** | [9] |
| 41 | (b) `hidden_states[l]` vs input of block l, l = 0..11 | 0.0 for every l | [9] |
| 42 | (c) `hidden_states[l+1]` vs output of block l | 0.0 for l = 0..10; **0.986 at l = 11** | [9] |
| 43 | (d) `hidden_states[l+1] − hidden_states[l]` vs attn + mlp writes | max rel 6.2e−6 (relative to the norm of the block's own two writes, not the stream; S5 r3 V3B-01) for l = 0..10 (max abs 1.75e−4); **rel 2.04 (abs 370) at l = 11** | [9] |
| 44 | `hidden_states[-1]` vs output of the last block | max abs 370, rel 0.986 | [10] |
| 45 | `hidden_states[-1]` vs `ln_f(output of the last block)` | 0.0 | [10] |
| 46 | `lm_head(hidden_states[-1])` vs model logits | 0.0 | [10] |
| 47 | Explicit position and layer: position 6 ("because"), after 6 blocks; d = 768; ‖h‖ | 77.1585 | [11] |
| 48 | h vs `hidden_states[0]` + the 12 hooked writes of blocks 0–5 | max abs 0.0 | [11] |
| 49 | Random unit u (seed 0): u·h, and the sum of its 13 read-shares | 7.211561 and 7.211561 (difference 0.0); largest shares mlp0 3.314, attn0 1.754, mlp5 0.952 | [11] |
| 50 | Steering arithmetic: u·(h + αu) − u·h − α for α = 0.5, 1, 2, 5, −3 | 0 for every α | [12] |
| 51 | Read linearity u·(x₁ + x₂) − (u·x₁ + u·x₂) | −5.72e−6 (rounding) | [12] |
| 52 | Steering is affine: steer(x₁ + x₂) − (steer(x₁) + steer(x₂)), α = 2 | norm 2.0000 | [12] |
| 53 | Cosine not additive, v = 3u: cos(h + v, u) vs cos(h, u) + cos(v, u) | 0.1318 vs 1.0935 | [12] |

### 02-B · tiny random models, code path only (cell [13])

Shrunk to 4 blocks, d = 64 (Qwen3: 4 heads, 2 KV heads, head_dim 16, MLP 192; Gemma 3: same, MLP 128, vocabulary 1000).
Random weights, seed 0. These numbers test indexing, hooks and norm handling, not anything about a trained stream.

| # | Quantity | GPT-2 (pretrained) | tiny Qwen3 (config only) | tiny Gemma 3 text (default config) |
|---|---|---|---|---|
| 54 | `len(hidden_states)` | 13 | 5 | 5 |
| 55 | `hidden_states[0]` matches | `wte(ids) + wpe(pos)` | raw table rows `E.weight[ids]` (no scaling) | the embedding *module* `E(ids)`, not the table rows |
| 56 | ‖hs[0]‖ / ‖E.weight[ids]‖ at position 0 | 3.7246 (position vector added) | 1.0000 | **8.0000** (= √64, see L17) |
| 57 | Guessed writes (attention, MLP modules) | `attn`, `mlp` | `self_attn`, `mlp` | `self_attn`, `mlp` |
| 58 | Additivity with the guessed writes (max rel) | 0.0 | 0.0 | **9.7 (fails)** |
| 59 | Writes found by the pair search | `attn`, `mlp` | `self_attn`, `mlp` | **`post_attention_layernorm`, `post_feedforward_layernorm`** |
| 60 | Additivity with the found writes (max rel) | 0.0 | 0.0 | 0.0 |
| 61 | Child reading (block input + attention write) | `ln_2` | `post_attention_layernorm` | `pre_feedforward_layernorm` |
| 62 | `hs[l+1] − hs[l]` = writes, l < n−1 (max rel) | 6.2e−6 | 1.1e−7 | 8.6e−8 |
| 63 | Same at l = n−1 (rel) | 2.0 (fails) | 33 (fails) | 1.4 (fails) |
| 64 | `hs[-1]` vs output of the last block (rel) | 0.99 | 22 | 0.64 |
| 65 | `hs[-1]` vs final_norm(output of the last block) (rel) | 0.0 | 0.0 | 0.0 |
| 66 | `lm_head(hs[-1])` vs logits (abs) | 0.0 | 0.0 | 0.0 |
| 67 | `tie_word_embeddings` / lm_head shares storage | True / True | True / True | True / True |

Qwen3 tokenizer (`Qwen/Qwen3-1.7B-Base`, cell [13]): the prompt gives 7 tokens `The, Ġcat, Ġsat, Ġon, Ġthe, Ġmat, Ġbecause`;
`bos_token` is None (nothing is prepended); padding side right. Full-size config (cell [13]): hidden_size 2048, 28 blocks,
16 heads, 8 KV heads, head_dim 128, MLP 6144, `rms_norm_eps` 1e−6, `tie_word_embeddings` true, vocabulary 151936.
Parameter count from that config (meta-device build, not in a notebook): 1,720,574,976, i.e. 6.9 GB in float32.

**Where additivity holds and where it fails, and why.** For every model tried, `hidden_states[l]` is exactly the input
of block l, for l = 0..n−1, so `hidden_states[l]` is the residual stream after l blocks. It fails at the last index
only: `hidden_states[n]` is the final norm applied to the stream after n blocks (L12, L13), so
`hidden_states[n] − hidden_states[n−1]` is not the last block's write. The stream after the last block is
available only from a hook on the last block. In Gemma 3 there is a second failure, at every block: a norm is applied to
each sub-layer's output before it is added (L18), so hooks on `self_attn` and `mlp` do not give the writes. The
writes are the outputs of `post_attention_layernorm` and `post_feedforward_layernorm`. Note the name clash: in Qwen3,
Llama and Mistral, `post_attention_layernorm` is the norm *before* the MLP (it reads the mid-block stream, row 61,
L15, L19); in Gemma 3 it is the norm on the attention output. Qwen3's `q_norm`/`k_norm` sit inside the attention
module (L16) and do not affect additivity.

## Library facts, with installed source lines

Paths are relative to `site-packages` (or `dist-packages`). Line numbers are for transformer_lens 4.3.0 and
transformers 5.19.0. The notebooks print these lines live with `cite(...)`/`show_source(...)`, so on another version
they show the right lines for that version.

| ID | Fact | Source (file:line) | Also shown numerically |
|---|---|---|---|
| L1 | `TransformerBridge.boot_transformers` returns **raw HF weights by default**; activations and logits match HF, not legacy `HookedTransformer`; `enable_compatibility_mode()` gives HookedTransformer-equivalent numerics. Attention is forced to `eager`; the docstring advises loading HF with `eager` for comparison. | transformer_lens/model_bridge/sources/transformers/source.py:69–72, 74–77 | rows 23, 30 |
| L2 | `enable_compatibility_mode` defaults: `fold_ln`, `center_writing_weights`, `center_unembed`, `fold_value_biases` all True, "Defaults match HookedTransformer's load-time processing". | transformer_lens/model_bridge/transformer_bridge.py:548, 552–555, 560 | rows 26–33 |
| L3 | `HookedTransformer` was removed in TransformerLens 4.0 (import raises an error pointing to `TransformerBridge`). In 3.9.0 it exists: `from_pretrained` defaults `fold_ln`, `center_writing_weights`, `center_unembed`, `fold_value_biases` True; `from_pretrained_no_processing` sets them False. | transformer_lens/__init__.py:46 (4.3.0); transformer_lens/HookedTransformer.py:1159–1174, 1492–1520 (3.9.0) | cross-version check |
| L4 | `to_tokens` prepends BOS unless told otherwise (`default_prepend_bos` defaults to True). | transformer_lens/model_bridge/transformer_bridge.py:924; transformer_lens/config/transformer_lens_config.py:69 | row 1 |
| L5 | Hook names in the bridge: `hook_resid_pre` = block `hook_in`, `hook_resid_mid` = `ln2.hook_in`, `hook_resid_post` = block `hook_out`, `hook_attn_out` = `attn.hook_out`, `hook_mlp_out` = `mlp.hook_out`; if a block has a post-sub-layer norm (`ln1_post`), `hook_attn_out` is redirected to its output. | transformer_lens/model_bridge/generalized_components/block.py:45–53, 84–87 | rows 2–4 |
| L6 | Weight processing order: fold LN, then centre writing weights, then centre unembed, then fold value biases. For RMSNorm models, folding only folds the norm weights (`fold_biases=False, center_weights=False`) and **writing weights are not centred** (only for `LN`/`LNPre`, not `final_rms`); `center_unembed` is applied regardless. | transformer_lens/weight_processing.py:1627, 1682–1684, 1706–1713 | GPT-2 only (rows 27, 32); the RMSNorm branch is source-only |
| L7 | `center_writing_weights` subtracts the mean over d_model from `W_E`, `W_pos` (and the output weights of attention and MLP). | transformer_lens/weight_processing.py:1177, 1182–1183, 1219, 1244 | row 27 |
| L8 | `center_unembed`: "As softmax is translation invariant, this changes the logits but not the log probs". | transformer_lens/weight_processing.py:1392, 1398 | rows 31–33 |
| L9 | Before processing, tied embed/unembed weights are untied so that centring affects only the unembedding. | transformer_lens/model_bridge/transformer_bridge.py:779 | — |
| L10 | `hidden_states` is collected by forward hooks on the class in `_can_record_outputs`. Index 0 is the **input of the first hooked layer** ("Historically, the first hidden_states output is actually the input of layer 0 (or inputs_embeds)"). | transformers/utils/output_capturing.py:115–124 | rows 37, 41 |
| L11 | Each hooked layer's output is appended (first element if the output is a tuple). | transformers/utils/output_capturing.py:133–136 | rows 41, 42 |
| L12 | **The last entry is overwritten with `last_hidden_state`** unless `config.tie_last_hidden_states` is False ("true for all language models"). | transformers/utils/output_capturing.py:243–246, 296–305 | rows 24–25, 42–45, 63–65 |
| L13 | GPT-2: `_can_record_outputs` hooks `GPT2Block`; stream = `wte(ids) + wpe(pos)` then dropout; block adds `attn_output + residual`, then `residual + mlp`; `ln_f` applied after the last block; `lm_head` tied to `wte`. | transformers/models/gpt2/modeling_gpt2.py:424, 577, 603, 282, 307, 619, 637 | rows 34, 37–46 |
| L14 | Qwen3RMSNorm: x·rsqrt(mean(x²)+eps) in float32, times a weight, no mean subtraction, no bias. | transformers/models/qwen3/modeling_qwen3.py:49, 62–63 | — (definition only) |
| L15 | Qwen3 decoder layer: `residual + self_attn(input_layernorm(x))`, then `residual + mlp(post_attention_layernorm(x))`; no norm between a sub-layer and its add. | transformers/models/qwen3/modeling_qwen3.py:296–297, 308, 311–312, 314 | rows 58–61 |
| L16 | Qwen3 attention applies RMSNorm to queries and keys per head (`q_norm`, `k_norm`), inside the attention module. | transformers/models/qwen3/modeling_qwen3.py:229–230 | — |
| L16b | Qwen3 model: stream starts as `embed_tokens(ids)` with no scaling and nothing positional added (rotary position embeddings are computed and passed to the layers); final `self.norm` after the last layer; `_can_record_outputs` hooks `Qwen3DecoderLayer`; `lm_head` tie declared. `Qwen3Config` defaults `tie_word_embeddings` to False, but the 1.7B-Base config.json sets it True. | transformers/models/qwen3/modeling_qwen3.py:373, 401–402, 415, 332, 424; transformers/models/qwen3/configuration_qwen3.py:74 | rows 55–56, 65, 67 |
| L17 | Gemma 3 embedding is scaled inside the module: `Gemma3TextScaledWordEmbedding.forward` multiplies by `embed_scale`, set to `hidden_size**0.5`. | transformers/models/gemma3/modeling_gemma3.py:105, 116, 485 | row 56 (8.0 = √64) |
| L18 | Gemma 3 decoder layer: `residual + post_attention_layernorm(self_attn(input_layernorm(x)))`, then `residual + post_feedforward_layernorm(mlp(pre_feedforward_layernorm(x)))`. | transformers/models/gemma3/modeling_gemma3.py:397–416 | rows 58–61 |
| L19 | Llama and Mistral decoder layers have the same pre-norm pattern as Qwen3 (no norm between sub-layer and add); `hidden_states` hooks the decoder layer class. | transformers/models/llama/modeling_llama.py:294–312, 330, 402; transformers/models/mistral/modeling_mistral.py:220–238, 256, 375 | source only (not run) |

## Cross-version check (TransformerLens)

Notebook 01 was also executed (outputs not saved) under transformer_lens 3.9.0 with the same torch and transformers:

* `TL_API="hooked"` (`HookedTransformer.from_pretrained` / `from_pretrained_no_processing`): additivity and
  telescoping 0.0; reordered sum max abs 1.83e−4, rel 4.6e−7; logit-lens check 0.0; raw logits vs HF 6.87e−5;
  processed vs HF−mean 5.17e−5; `ln_final` vs `hidden_states[-1]` 7.63e−5; all W9 asserts pass. A DeprecationWarning
  says `from_pretrained` will be removed.
* `TL_API="auto"` (the 3.9.0 `TransformerBridge`): same numbers as 4.3.0. Some `cite` lines print "not importable here"
  because the files moved between versions; that is expected.

## What could not be verified here

1. **A full-size Qwen3-1.7B-Base run.** Not attempted: float32 needs about 6.9 GB for the weights alone (container: 7 GB
   RAM), and the download is 3.44 GB. Only the code path was exercised, on a random 4-block model built from the
   config. Whether the trained Qwen3 stream has the same additivity numbers, its norm profile, and a BOS-like outlier
   position is **unverified**. Expect the structure (rows 54–67) to hold, since it depends on the code, not the weights.
2. **Gemma 3, Llama 3, Mistral checkpoints.** Gemma 3 was run only as a tiny random model from the library's default
   `Gemma3TextConfig`; Llama and Mistral only by reading the installed source (L19). No trained checkpoint was loaded.
3. **TransformerLens on Qwen3 or any RMSNorm model.** The claim that TL does not centre writing weights for RMSNorm
   models (L6) is from source only.
4. **Kunhao's Mac.** Not run on macOS or Apple silicon. MPS was not used; the notebooks pin `DEVICE = "cpu"`. Line
   numbers in the citations will differ if the installed versions differ.
5. **The logit-lens definition** (card T8) is not settled by the notebook. It only shows that final norm + unembedding
   applied to the last block's stream reproduces the logits, and prints the per-layer readouts.
6. **The saved-sources instruction in card T1** (copy the relevant library lines into `sources/` with the version) was
   not carried out: this task may write only inside `notebook/`. The file:line table above is the record.

## Points that differ from, or sharpen, the topic card's flags

* **T6.** In TransformerLens 4.x the default loader does *not* rewrite weights; only `enable_compatibility_mode()` does
  (L1, L2). `HookedTransformer` and `from_pretrained_no_processing` no longer exist in 4.x (L3). The processed stream
  is the Hugging Face stream minus its mean coordinate (row 27); the norm changes by < 0.1% (row 29); logits shift by
  a per-position constant, so log-probs are unchanged (rows 31–33).
* **T1.** `hidden_states[L]` = stream after L blocks for L = 0..n−1 (0-based: index 0 = embedding). The last entry is
  final-normed (L12), so "the hidden state at the last layer" is not a residual-stream vector.
* **T2.** The Gemma 3 suspicion is confirmed by the installed source and by the tiny-model run (L18, rows 58–59).
* **T3.** Gemma 3 scales the embedding by √d inside the embedding module (L17, row 56); Qwen3 does not (row 56).
  Qwen3-1.7B-Base ties the unembedding to the embedding (config true; class default false, L16b).
* **T7.** Additivity is *bit-exact* (0.0) when the check adds tensors in the model's own order (rows 2–6, 40); a
  reordered sum shows float32 rounding of about 1e−6 relative (row 7); differences of consecutive `hidden_states`
  show up to 6.2e−6 relative (row 43).
* **W9 margin.** The card's margin values (0 at 0°, −2.828 at 45°) hold with margin defined as the larger of the two
  orientations, max(min urgent − max calm, min calm − max urgent). The post should state that definition.


**Correction (2026-10-25, meta-manager, after S5 r3 V3B-01).** "rel" everywhere in notebook 02 is ‖a − b‖ / ‖b‖ with b the second argument of `err` (the reference). For row 43/62 the reference is the block's two writes, not the stream; relative to the stream the same differences are about 4e−8 to 7e−7 (the S5 checker's rerun). The helper's docstring said "the stream's norm"; it is corrected (no number changes).
