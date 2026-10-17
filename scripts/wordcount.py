"""Visible word count of a post for the length rule (WRITING / rubric criterion 6).
Usage: python3 scripts/wordcount.py posts/<slug>/src/content.html
Counts visible text outside <details class="deep"> fold-outs, the Sources section, the English section,
the contents list, <script>/<style> blocks and widget configs. Display math counts as 0, inline math as 1 word."""
import sys, re, html
from html.parser import HTMLParser
SKIP_SECTIONS = {"sources", "english"}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.stack=[]; s.skip=0; s.main=[]; s.fold=[]; s.infold=0; s.sec=None; s.secw={}
    def handle_starttag(s, t, a):
        a=dict(a); cls=a.get("class") or ""
        if t=="section" and a.get("id"): s.sec=a["id"]
        skip = t in ("script","style","math") or (t=="details" and "toc" in cls) or (t=="section" and a.get("id") in SKIP_SECTIONS)
        fold = t=="details" and "deep" in cls
        s.stack.append((t,skip,fold)); s.skip+=skip; s.infold+=fold
    def handle_endtag(s, t):
        while s.stack:
            tt,sk,fo=s.stack.pop(); s.skip-=sk; s.infold-=fo
            if tt==t: break
    def handle_data(s, d):
        if s.skip: 
            return
        w=len(re.findall(r"[\w’'\-.%]+", d))
        if s.infold: s.fold.append(w)
        else: s.main.append(w); s.secw[s.sec]=s.secw.get(s.sec,0)+w
src=open(sys.argv[1],encoding="utf-8").read()
src=re.sub(r"\\\[[\s\S]+?\\\]"," ",src); src=re.sub(r"\\\([\s\S]+?\\\)"," x ",src)
p=P(); p.feed(src)
print(f"main text: {sum(p.main)} words (cap 7,500; excludes fold-outs, Sources, English, contents)")
print(f"fold-outs: {sum(p.fold)} words")
for k,v in p.secw.items(): print(f"  {k}: {v}")
