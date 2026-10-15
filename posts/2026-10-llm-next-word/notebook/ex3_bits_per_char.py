# Exercise 3: bits per token vs bits per character, English vs Japanese (GPT-2 small).
import math, torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2").eval()

texts = {
    "English": "The better you predict the next letter, the shorter the code you need to send the text.",
    "Japanese": "次の文字をうまく予測できるほど、文章を送るために必要な符号は短くなる。",
}
for lang, s in texts.items():
    ids = tok(s, return_tensors="pt").input_ids
    with torch.no_grad():
        loss = model(ids, labels=ids).loss.item()      # mean nats per predicted token
    n_pred = ids.shape[1] - 1                           # the first token is not predicted
    bits = loss * n_pred / math.log(2)                  # total bits for the text
    print(f"{lang:9s} tokens={ids.shape[1]:3d}  chars={len(s):3d}  "
          f"bits/token={bits / n_pred:5.2f}  bits/char={bits / len(s):5.2f}")
