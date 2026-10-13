"""Non-blocking smoke for prompts v2.1 (reviews/gate2b.md): P1 + P2 on one unit, outside the state machine.

python -m pipeline.smoke21 [unit_id]   -> pipeline/results/smoke-v21/
"""
import json
import sys
import time

from . import PIPE, state
from .build import p1_request, p2_request, target_words, units
from .checks import check, sections, split_frontmatter
from .run import bucket, parse_verdict, strip_fence, text_of, usage_parts
from .vertex import CFG, batch_create, batch_wait, cost

OUT = PIPE / "results" / "smoke-v21"


def one(kind, uid, req):
    stamp = time.strftime("%Y%m%d-%H%M%S")
    blob = f"{CFG['gcs_prefix']}/smoke-v21/{kind}-{stamp}/input.jsonl"
    bucket().blob(blob).upload_from_string(json.dumps({"custom_id": "smoke", "request": req}) + "\n")
    out = f"gs://{bucket().name}/{CFG['gcs_prefix']}/smoke-v21/{kind}-{stamp}/output"
    job = batch_create(f"ai4read-smoke21-{kind}-{stamp}", f"gs://{bucket().name}/{blob}", out)
    print("submitted", kind, job["name"].split("/")[-1], flush=True)
    batch_wait(job["name"], every=60)
    for bl in bucket().list_blobs(prefix=out.removeprefix(f"gs://{bucket().name}/")):
        if bl.name.endswith("predictions.jsonl"):
            resp = json.loads(bl.download_as_text().splitlines()[0]).get("response") or {}
            u = resp.get("usage", {})
            usd = cost(u, "batch_us")
            state.add_spend(usd, f"smoke21-{kind}", unit_id=uid, usage=usage_parts(u))
            return resp, usd
    return {}, 0.0


def main(uid):
    OUT.mkdir(parents=True, exist_ok=True)
    row = units()[uid]
    req, st = p1_request(uid)
    resp, usd1 = one("p1", uid, req)
    md = strip_fence(text_of(resp))
    (OUT / "p1.md").write_text(md)
    _, body = split_frontmatter(md)
    words = len(body.split())
    req2, st2 = p2_request(uid, md)
    resp2, usd2 = one("p2", uid, req2)
    txt = text_of(resp2)
    (OUT / "p2.txt").write_text(txt)
    v = parse_verdict(txt)
    w4_digest = [l for l in md.splitlines() if "272" in l][:3]
    w4_flags = [i for i in (v["issues"] or []) if "272" in json.dumps(i, ensure_ascii=False)]
    w4_h = [h for h in (v["h_checks"] or []) if isinstance(h, dict) and "272" in json.dumps(h, ensure_ascii=False)]
    rep = {"unit": uid, "source_words": st["source_words"], "target_words": st["target_words"], "digest_words": words,
           "ratio": round(words / st["target_words"], 2), "p1_usage": usage_parts(resp.get("usage", {})),
           "p2_usage": usage_parts(resp2.get("usage", {})), "usd": round(usd1 + usd2, 4),
           "mandatory_items": st2.get("mandatory_items"), "verdict": v["verdict"],
           "w4_digest_lines": w4_digest, "w4_issues": w4_flags, "w4_h_checks": w4_h,
           "det": [i["msg"] for i in check(md, row, uid) if i["level"] == "error"]}
    (OUT / "report.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1))
    print(json.dumps(rep, ensure_ascii=False, indent=1)[:3000])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "wittgenstein-1953-investigations/ch04-private")
