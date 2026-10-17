"""Assemble the full system prompt for each phase-2 role from the house rules, so a rule change
reaches every agent at once.  Usage: python3 phase2/assemble.py  ->  phase2/prompts/build/<role>.md
Each built prompt = role prompt + CHARTER.md + WRITING.md + phase2/rubric.md (+ component README for
the writer and critic), with a header recording the source versions (git short hash of each file)."""
import pathlib, subprocess
R = pathlib.Path(__file__).resolve().parent.parent
P = R / "phase2" / "prompts"; OUT = P / "build"; OUT.mkdir(exist_ok=True)
HOUSE = ["CHARTER.md", "WRITING.md", "phase2/rubric.md"]
EXTRA = {"writer": ["site/ai4read/components/README.md", "notation.md", "toyworlds.md"],
         "critic": ["site/ai4read/components/README.md"], "planner": ["toyworlds.md"], "factcheck": []}
def ver(f):
    try: return subprocess.run(["git", "log", "-1", "--format=%h", "--", f], cwd=R, capture_output=True, text=True).stdout.strip() or "uncommitted"
    except Exception: return "?"
for role in ["planner", "writer", "factcheck", "critic"]:
    files = HOUSE + EXTRA[role]
    head = "<!-- built by phase2/assemble.py from: " + ", ".join(f"{f}@{ver(f)}" for f in [f"phase2/prompts/{role}.md"] + files) + " -->\n"
    body = (P / f"{role}.md").read_text()
    for f in files: body += f"\n\n---\n# House rule file: {f}\n\n" + (R / f).read_text()
    (OUT / f"{role}.md").write_text(head + body)
    print(f"{role}: {len(body.split())} words")
