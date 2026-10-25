# Post 03 notebooks: the residual stream, checked numerically

| Notebook | What it does | Models |
|---|---|---|
| `01_bus_gpt2.ipynb` | TransformerLens on GPT-2 small: per-block additivity, telescoping from the embedding, stream norm by layer and position, logit lens with and without the final LayerNorm, the W9 toy numbers in numpy, TransformerLens versus Hugging Face. | `gpt2` |
| `02_bus_my_model.ipynb` | Plain Hugging Face + forward hooks on your own model: module tree and source, `hidden_states` versus the embedding, hooks on the modules found by inspection, per-block additivity, the last entry versus the final norm, one explicit position and layer, arithmetic along a random direction, then tiny random Qwen3 and Gemma 3 models (code path only). | `MODEL_PATH` (default `Qwen/Qwen3-1.7B-Base`, falls back to `openai-community/gpt2`) |

`results.md` lists every number from the reference run, the cell that produced it, and the library source lines
behind each claim about library behaviour.

## Install (Mac, Python 3.10 or later)

```bash
python3 -m venv ~/venvs/ai4read-tl
source ~/venvs/ai4read-tl/bin/activate
pip install "torch>=2.6" "transformers==5.19.0" "transformer_lens==4.3.0" numpy pandas matplotlib jupyter
```

The reference run used torch 2.14.1, transformers 5.19.0, transformer_lens 4.3.0, numpy 2.5.3, pandas 3.0.5 and
matplotlib 3.11.2. Other versions should work, but the line numbers printed by `cite(...)` will differ, and numbers
may differ in the last digits. Notebook 01 also runs with transformer_lens 3.x (it uses `TransformerBridge` if present,
else `HookedTransformer`; set `TL_API` to force one). TransformerLens 4 removed `HookedTransformer`.
After installing, check that pip did not replace your torch: `python -c "import torch; print(torch.__version__)"`.

## First run (downloads), then offline

1. Open Jupyter in this folder: `jupyter lab` (or `jupyter notebook`).
2. First run: keep `LOCAL_ONLY = False` in the settings cell. This fills the Hugging Face cache (`~/.cache/huggingface`):
   * `gpt2` (about 0.55 GB) for notebook 01;
   * `Qwen/Qwen3-1.7B-Base` (3.44 GB download) for notebook 02, plus `openai-community/gpt2` (about 0.55 GB) if you
     want the fallback cached too. `gpt2` and `openai-community/gpt2` are stored as two separate cache entries.
3. Afterwards, set `LOCAL_ONLY = True` (or start Jupyter with `AI4READ_LOCAL_ONLY=1 jupyter lab`). Nothing then touches
   the network; a missing model raises an error instead (notebook 02 then falls back to GPT-2 if that is cached).

To use another model in notebook 02, set `MODEL_PATH` to a Hub id or a local folder, or start Jupyter with
`AI4READ_MODEL_PATH=/path/to/model`.

## Memory and runtime

* Everything runs in float32 on the CPU (`DEVICE = "cpu"`), on purpose: the equality checks need float32 (half
  precision or MPS will not match to the same digits).
* Notebook 01: peak memory 3.1 GB measured (GPT-2 is loaded three times: processed, raw, Hugging Face). Reference
  run: 16 s on 2 CPU cores with the model cached.
* Notebook 02 with GPT-2: peak memory 1.5 GB measured; reference run 11 s on 2 cores.
* Notebook 02 with Qwen3-1.7B-Base: the weights alone take 6.9 GB in float32 (1,720,574,976 parameters); with the
  GPT-2-run overhead added, a Mac with 16 GB is the minimum and more is safer (estimate, not measured). Close other
  large programs. Not run in the build container (7 GB RAM): expect loading to take
  well under a minute from a local SSD and one forward pass on 7 tokens to take a few seconds, but this is an estimate.
  If it fails for memory, the notebook falls back to GPT-2 and prints why.

## What to expect

Reference numbers (GPT-2 small, "The cat sat on the mat because"):

* per-block additivity `resid_post − (resid_pre + attn_out + mlp_out)`: 0.0 in every block (bit-exact in float32);
* the same writes summed in another order: max relative error about 1e−6 (rounding);
* final norm + unembedding on the stream after the last block reproduces the logits exactly (0.0);
* `hidden_states[l]` is the stream after l blocks for l = 0..n−1; `hidden_states[n]` is the final norm of the stream,
  so the last difference does not match the last block's writes;
* the TransformerLens processed stream equals the Hugging Face stream minus its mean coordinate (relative error 1e−6).

The exercise cells at the end of each notebook are blank on purpose.
