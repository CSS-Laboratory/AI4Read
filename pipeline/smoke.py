"""Gate 0 smoke test.  python -m pipeline.smoke online | batch <jpeg>"""
import base64
import json
import sys
import time

from google.cloud import storage

from . import state
from .vertex import CFG, online, batch_create, batch_wait, cost

PROMPT = "Reply with exactly: OK"


def run_online():
    r = online({"max_tokens": 16, "messages": [{"role": "user", "content": PROMPT}]})
    u = r["usage"]
    usd = cost(u, "online_global")
    state.add_spend(usd, "gate0-smoke-online", usage=u)
    print("model:", r.get("model"), "| text:", r["content"][-1].get("text"), "| usage:", u, f"| ${usd:.6f}")


def run_batch(jpeg):
    img = base64.b64encode(open(jpeg, "rb").read()).decode()
    rows = [
        {"custom_id": "smoke-text", "request": {
            "anthropic_version": CFG["anthropic_version"], "max_tokens": 16,
            "messages": [{"role": "user", "content": PROMPT}]}},
        {"custom_id": "smoke-image", "request": {
            "anthropic_version": CFG["anthropic_version"], "max_tokens": 64,
            "messages": [{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": img}},
                {"type": "text", "text": "What is the printed page number on this page? Reply with the number only."}]}]}},
    ]
    bucket = CFG["bucket"].removeprefix("gs://")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    blob = f"{CFG['gcs_prefix']}/smoke/{stamp}/input.jsonl"
    b = storage.Client(project=CFG["project"]).bucket(bucket)
    b.blob(blob).upload_from_string("\n".join(json.dumps(r) for r in rows) + "\n")
    out = f"gs://{bucket}/{CFG['gcs_prefix']}/smoke/{stamp}/output"
    job = batch_create(f"ai4read-smoke-{stamp}", f"gs://{bucket}/{blob}", out)
    print("job:", job["name"])
    j = batch_wait(job["name"], every=30)
    print(json.dumps({k: j.get(k) for k in ("state", "error", "completionStats")}, indent=1))
    for bl in b.list_blobs(prefix=f"{CFG['gcs_prefix']}/smoke/{stamp}/output"):
        if not bl.name.endswith(".jsonl"):
            continue
        for line in bl.download_as_text().splitlines():
            r = json.loads(line)
            resp = r.get("response") or {}
            u = resp.get("usage", {})
            usd = cost(u, "batch_us")
            state.add_spend(usd, "gate0-smoke-batch", custom_id=r.get("custom_id"), usage=u)
            txt = [c.get("text") for c in resp.get("content", []) if c.get("type") == "text"]
            print(r.get("custom_id"), "|", txt, "|", u, f"| ${usd:.6f}", "| status:", r.get("status"))


if __name__ == "__main__":
    {"online": lambda: run_online(), "batch": lambda: run_batch(sys.argv[2])}[sys.argv[1]]()
