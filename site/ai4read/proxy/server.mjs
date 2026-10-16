// Cloud Run proxy: Worker → (shared secret) → this service → Claude on Vertex AI (keyless: the service's own service account).
// Deploy (owner runs, after approval):
//   gcloud iam service-accounts create ai4read-claude --project playground-491901
//   gcloud projects add-iam-policy-binding playground-491901 --member serviceAccount:ai4read-claude@playground-491901.iam.gserviceaccount.com --role roles/aiplatform.user
//   printf '%s' "$(openssl rand -hex 32)" | gcloud secrets create ai4read-proxy-secret --data-file=- --project playground-491901
//   gcloud run deploy ai4read-claude --source . --region asia-northeast1 --project playground-491901 \
//     --service-account ai4read-claude@playground-491901.iam.gserviceaccount.com --allow-unauthenticated \
//     --set-secrets PROXY_SECRET=ai4read-proxy-secret:latest --set-env-vars PROJECT=playground-491901,MODEL=claude-sonnet-5-5 \
//     --max-instances 2 --concurrency 20 --timeout 120
//   Then: wrangler secret put CLAUDE_PROXY_SECRET (same value, read from Secret Manager by the owner) and set CLAUDE_PROXY_URL.
import http from "node:http";
import { timingSafeEqual } from "node:crypto";
const { PROXY_SECRET = "", PROJECT, MODEL = "claude-sonnet-5-5", PORT = 8080 } = process.env;
let tok = { v: "", exp: 0 };
async function token() {
  if (Date.now() < tok.exp - 60e3) return tok.v;
  const r = await fetch("http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token", { headers: { "Metadata-Flavor": "Google" } });
  const j = await r.json(); tok = { v: j.access_token, exp: Date.now() + j.expires_in * 1000 }; return tok.v;
}
const same = (a, b) => { const x = Buffer.from(a), y = Buffer.from(b); return x.length === y.length && timingSafeEqual(x, y); };
http.createServer(async (req, res) => {
  if (req.method !== "POST" || !PROXY_SECRET || !same(String(req.headers["x-proxy-secret"] || ""), PROXY_SECRET)) { res.writeHead(403).end(); return; }
  let body = ""; for await (const c of req) { body += c; if (body.length > 400_000) { res.writeHead(413).end(); return; } }
  let p; try { p = JSON.parse(body); } catch { res.writeHead(400).end(); return; }
  p.max_tokens = Math.min(+p.max_tokens || 1500, 2000);          // hard caps, whatever the caller sends
  const url = `https://aiplatform.googleapis.com/v1/projects/${PROJECT}/locations/global/publishers/anthropic/models/${MODEL}:streamRawPredict`;
  const up = await fetch(url, { method: "POST", headers: { authorization: `Bearer ${await token()}`, "content-type": "application/json" }, body: JSON.stringify(p) });
  res.writeHead(up.status, { "content-type": up.headers.get("content-type") || "text/event-stream" });
  if (!up.body) { res.end(); return; }
  for await (const chunk of up.body) res.write(chunk);
  res.end();
}).listen(PORT);
