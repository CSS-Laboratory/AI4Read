/* AI4Read annotations.
   Select text in <main> -> "Annotate" -> right-hand drawer with saved items (Note / Question / Claude's answer),
   a Markdown editor (upper) and live preview (lower), "Save as note" and "Ask Claude".
   Storage: one db document per annotation in "annotations" (doc id = annotation id), mirrored in localStorage
   ("ai4read-p01-anno-<id>"). Anchors are text-quote selectors re-found on every load. Legacy "notes" docs are
   migrated into section-level annotations "legacy-<id>". Deletions are soft (deleted:true) so they sync. */
(function(){
"use strict";
const MAIN=document.querySelector("main"); if(!MAIN) return;
const PFX="ai4read-p01-anno-", COLL="annotations", LEGACY="notes";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const now=()=>new Date().toISOString();
const uid=p=>p+Date.now().toString(36)+Math.random().toString(36).slice(2,8);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const mq=q=>{try{return matchMedia(q).matches}catch(e){return false}};
const coarse=()=>mq("(pointer: coarse)"), reduced=()=>mq("(prefers-reduced-motion: reduce)");
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const newer=(a,b)=>String(a.updatedAt||"")>String(b.updatedAt||"");
function h(tag,attrs,...kids){const e=document.createElement(tag);
  for(const k in attrs||{}){const v=attrs[k];if(v==null||v===false)continue;
    if(k==="class")e.className=v;else if(k==="text")e.textContent=v;else if(k==="html")e.innerHTML=v;
    else if(k.startsWith("on"))e.addEventListener(k.slice(2),v);else e.setAttribute(k,v===true?"":v)}
  for(const c of kids)if(c!=null)e.append(c);return e}
const fmtTime=iso=>{try{return new Intl.DateTimeFormat(undefined,{month:"short",day:"numeric",hour:"2-digit",minute:"2-digit"}).format(new Date(iso))}catch(e){return ""}};
const TYPE={note:"Note",question:"Question",answer:"Claude’s answer"};

/* ---------- Markdown (marked + DOMPurify + KaTeX MathML), with an escaped-text fallback ---------- */
const MATH_RE=/(```[\s\S]*?```|`[^`\n]+`)|\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|\$([^\s$](?:[^$\n]*[^\s$\\])?)\$(?!\d)/g;
function renderTex(tex,display){const K=window.katex;
  if(K&&K.renderToString){try{return K.renderToString(tex,{output:"mathml",throwOnError:false,displayMode:display})}catch(e){}}
  return `<code>${esc(display?"$$"+tex+"$$":"$"+tex+"$")}</code>`}
function md(src){
  src=String(src||"");const M=window.marked,P=window.DOMPurify;
  if(!M||typeof M.parse!=="function"||!P||typeof P.sanitize!=="function")
    return src.trim()?"<p>"+esc(src).replace(/\n/g,"<br>")+"</p>":"";
  const maths=[];
  const prot=src.replace(MATH_RE,(m,code,d1,d2,i1,i2,off,str)=>{
    if(code)return m; if(off>0&&str[off-1]==="\\")return m;
    const display=d1!=null||d2!=null; maths.push(renderTex((d1||d2||i1||i2).trim(),display));
    return ""+(maths.length-1)+""});
  let html;try{html=P.sanitize(M.parse(prot,{gfm:true,breaks:true}))}catch(e){return "<p>"+esc(src).replace(/\n/g,"<br>")+"</p>"}
  return html.replace(/(\d+)/g,(_,i)=>maths[+i]||"")}
const firstLine=s=>String(s||"").replace(/[#>*_`~\[\]]/g,"").replace(/\$+/g,"").split("\n").map(x=>x.trim()).find(Boolean)||"";

/* ---------- Local mirror ---------- */
const LS={
  all(){const out=[];try{for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);
    if(k&&k.startsWith(PFX)&&k.length>PFX.length){try{const a=JSON.parse(localStorage.getItem(k));if(a&&a.id)out.push(a)}catch(e){}}}}catch(e){}return out},
  put(a){try{localStorage.setItem(PFX+a.id,JSON.stringify(a))}catch(e){}}
};
const S=new Map(); LS.all().forEach(a=>{if(!Array.isArray(a.items))a.items=[];S.set(a.id,a)});
const live=()=>[...S.values()].filter(a=>!a.deleted&&a.items&&a.items.length);
let pending=null;                       // a new annotation not yet saved (no items)
const getA=id=>pending&&pending.id===id?pending:S.get(id);
const DETACHED=new Set();

/* ---------- Text map: normalized (whitespace-collapsed) text of a section, with positions back to text nodes ---------- */
const EXCL="[data-anno-ui],.sec-tools,script,style,annotation,button,svg,input,textarea,select,noscript";
function textMap(root){
  const nodes=[],pos=[];let text="",prevWs=true;
  const tw=document.createTreeWalker(root,NodeFilter.SHOW_ELEMENT|NodeFilter.SHOW_TEXT,{acceptNode(n){
    if(n.nodeType===1)return n.matches(EXCL)?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_SKIP;return NodeFilter.FILTER_ACCEPT}});
  let n;while((n=tw.nextNode())){const s=n.data,idx=new Array(s.length+1),ni=nodes.length;
    for(let k=0;k<s.length;k++){idx[k]=text.length;const c=s.charCodeAt(k);
      const ws=c===32||c===10||c===9||c===13||c===12||c===160;
      if(ws){if(prevWs)continue;text+=" ";pos.push(ni,k);prevWs=true}else{text+=s[k];pos.push(ni,k);prevWs=false}}
    idx[s.length]=text.length;nodes.push({node:n,idx})}
  const byNode=new Map();nodes.forEach((e,i)=>byNode.set(e.node,i));
  return {text,pos,nodes,byNode}}
function pointIdx(map,c,o){
  if(c.nodeType===3){const i=map.byNode.get(c);if(i!=null)return map.nodes[i].idx[Math.min(o,c.data.length)]}
  const p=document.createRange();try{p.setStart(c,o)}catch(e){return null}
  for(const e of map.nodes){try{if(p.comparePoint(e.node,0)>=0)return e.idx[0]}catch(err){}}
  return map.text.length}
const norm=s=>String(s||"").replace(/\s+/g," ");
function anchorFromRange(r){
  const el=n=>n.nodeType===1?n:n.parentElement;
  let sec=el(r.startContainer)&&el(r.startContainer).closest("section");
  if(!sec||!MAIN.contains(sec))sec=el(r.endContainer)&&el(r.endContainer).closest("section");
  if(!sec||!MAIN.contains(sec)||!sec.id)return null;
  const map=textMap(sec);
  let s=sec.contains(r.startContainer)?pointIdx(map,r.startContainer,r.startOffset):0;
  let e=sec.contains(r.endContainer)?pointIdx(map,r.endContainer,r.endOffset):map.text.length;
  if(s==null||e==null)return null;
  while(s<e&&map.text[s]===" ")s++;while(e>s&&map.text[e-1]===" ")e--;
  if(e-s<1)return null;
  return {section:sec.id,quote:map.text.slice(s,e),prefix:map.text.slice(Math.max(0,s-32),s),suffix:map.text.slice(e,e+32)}}
function locate(map,a){
  const q=norm(a.quote).trim();if(!q)return null;const T=map.text,hits=[];
  for(let i=T.indexOf(q);i>=0&&hits.length<500;i=T.indexOf(q,i+1))hits.push(i);
  if(!hits.length)return null;
  const pre=norm(a.prefix),suf=norm(a.suffix);let best=hits[0],bs=-1;
  for(const x of hits){const p=T.slice(Math.max(0,x-pre.length),x),s=T.slice(x+q.length,x+q.length+suf.length);
    if(p===pre&&s===suf)return [x,x+q.length];
    let sc=0;while(sc<p.length&&sc<pre.length&&p[p.length-1-sc]===pre[pre.length-1-sc])sc++;
    let sc2=0;while(sc2<s.length&&sc2<suf.length&&s[sc2]===suf[sc2])sc2++;
    if(sc+sc2>bs){bs=sc+sc2;best=x}}
  return [best,best+q.length]}
const kind=a=>a.items.some(t=>t.type!=="note")?"q":"n";
function applyMarks(map,s,e,a,isPending){
  const pieces=new Map();
  for(let i=s;i<e;i++){const ni=map.pos[2*i],k=map.pos[2*i+1],r=pieces.get(ni);if(!r)pieces.set(ni,[k,k+1]);else r[1]=k+1}
  const cls="anno "+kind(a)+(isPending?" pending":"");let first=true;
  for(const [ni,[k0,k1]] of pieces){const node=map.nodes[ni].node,par=node.parentElement;if(!par)continue;
    const math=par.closest("math");
    if(math){const host=math.closest(".katex")||math.parentElement;if(host&&MAIN.contains(host)){
      host.classList.add("anno-m",kind(a));if(isPending)host.classList.add("pending");
      const ids=(host.dataset.annoIds||"").split(" ").filter(Boolean);if(!ids.includes(a.id))ids.push(a.id);host.dataset.annoIds=ids.join(" ")}continue}
    const t=node.data.slice(k0,k1);if(!/\S/.test(t)&&/\n/.test(t))continue;
    let target=node;if(k1<node.data.length)node.splitText(k1);if(k0>0)target=node.splitText(k0);
    const m=document.createElement("mark");m.className=cls;m.dataset.id=a.id;
    if(first){m.tabIndex=0;m.title="Open note";first=false}
    target.parentNode.insertBefore(m,target);m.appendChild(target)}}
function wrap(a,isPending){
  const tryIn=sec=>{if(!sec||!MAIN.contains(sec))return false;const map=textMap(sec),at=locate(map,a);
    if(!at)return false;applyMarks(map,at[0],at[1],a,isPending);return true};
  const home=document.getElementById(a.section);if(tryIn(home))return true;
  if(norm(a.quote).trim().length<12)return false;
  for(const sec of $$("section",MAIN))if(sec!==home&&tryIn(sec))return true;
  return false}
function clearMarks(){const parents=new Set();
  $$("mark.anno",MAIN).forEach(m=>{const p=m.parentNode;if(!p)return;while(m.firstChild)p.insertBefore(m.firstChild,m);p.removeChild(m);parents.add(p)});
  parents.forEach(p=>{if(p.isConnected)p.normalize()});
  $$(".anno-m",MAIN).forEach(x=>{x.classList.remove("anno-m","q","n","pending");delete x.dataset.annoIds})}
const selActive=()=>{const s=getSelection();return !!(s&&s.rangeCount&&!s.isCollapsed&&MAIN.contains(s.getRangeAt(0).commonAncestorContainer))};
let needRepaint=false;
function paint(){
  if(selActive()){needRepaint=true;return}needRepaint=false;
  clearMarks();DETACHED.clear();
  const list=live().sort((x,y)=>String(x.createdAt).localeCompare(String(y.createdAt)));
  for(const a of list)if(!a.sectionLevel&&!wrap(a,false))DETACHED.add(a.id);
  if(pending&&!pending.sectionLevel)wrap(pending,true);
  secPills();updateCount()}

/* ---------- Section-level annotations: a pill under the heading; a button in each .sec-tools row ---------- */
const secTitle=sec=>{const h2=sec&&$("h2",sec);return h2?h2.textContent.trim():(sec&&sec.id)||""};
const titleOf=id=>{const s=document.getElementById(id);return s?secTitle(s):id};
function secPills(){
  $$(".anno-secpill",MAIN).forEach(x=>x.remove());const by={};
  live().filter(a=>a.sectionLevel).forEach(a=>(by[a.section]=by[a.section]||[]).push(a));
  for(const sid in by){const sec=document.getElementById(sid),list=by[sid];
    if(!sec||!MAIN.contains(sec)){list.forEach(a=>DETACHED.add(a.id));continue}
    const n=list.length,q=list.some(a=>kind(a)==="q");
    const b=h("button",{type:"button",class:"anno-secpill"+(q?" q":""),"data-anno-ui":"",
      "aria-label":`${n} note${n>1?"s":""} on this section`,onclick:()=>n===1?openAnno(list[0].id):openList(sid)},
      h("span",{"aria-hidden":"true",text:"✎"}),` ${n} note${n>1?"s":""} on this section`);
    const h2=$("h2",sec);if(h2)h2.after(b);else sec.prepend(b)}}
function addSecButtons(){
  $$("section[data-ch]",MAIN).forEach(sec=>{const t=[...sec.children].find(c=>c.classList.contains("sec-tools"));
    if(!t||t.querySelector(".anno-secbtn"))return;
    t.append(h("button",{type:"button",class:"anno-secbtn",onclick:()=>startSection(sec)},"Note on this section"))})}

/* ---------- Floating controls ---------- */
const fab=h("div",{class:"anno-fab","data-anno-ui":""});
const annDock=h("button",{type:"button",class:"anno-annot",hidden:true},"Annotate");
const notesBtn=h("button",{type:"button",class:"anno-notes","aria-label":"All notes"},"Notes");
fab.append(annDock,notesBtn);
const annFloat=h("button",{type:"button",class:"anno-annot anno-float","data-anno-ui":"",hidden:true},"Annotate");
document.body.append(fab,annFloat);
function updateCount(){const n=live().length;notesBtn.textContent=n?`Notes · ${n}`:"Notes";notesBtn.setAttribute("aria-label",n?`All notes, ${n}`:"All notes")}
notesBtn.addEventListener("click",()=>openList(null));

let selAnchor=null,hideT=0,selT=0;
function hideAnn(){annDock.hidden=true;annFloat.hidden=true}
function scheduleHide(){clearTimeout(hideT);hideT=setTimeout(()=>{hideAnn();selAnchor=null;if(needRepaint&&!selActive())paint()},700)}
function onSel(){
  const sel=getSelection();if(!sel||!sel.rangeCount||sel.isCollapsed){scheduleHide();return}
  const r=sel.getRangeAt(0);if(!MAIN.contains(r.commonAncestorContainer)){scheduleHide();return}
  const an=anchorFromRange(r);if(!an){scheduleHide();return}
  clearTimeout(hideT);selAnchor=an;
  if(coarse()){annFloat.hidden=true;annDock.hidden=false;return}
  annDock.hidden=true;annFloat.hidden=false;
  const rects=r.getClientRects(),last=rects.length?rects[rects.length-1]:r.getBoundingClientRect();
  const vw=document.documentElement.clientWidth,bw=annFloat.offsetWidth||96;
  const left=Math.max(8,Math.min(vw-bw-8,last.right-bw/2));
  annFloat.style.left=(left+window.scrollX)+"px";annFloat.style.top=(last.bottom+window.scrollY+8)+"px"}
document.addEventListener("selectionchange",()=>{clearTimeout(selT);selT=setTimeout(onSel,120)});
[annDock,annFloat].forEach(b=>{
  b.addEventListener("mousedown",e=>e.preventDefault());
  b.addEventListener("pointerdown",()=>clearTimeout(hideT));
  b.addEventListener("click",()=>{if(selAnchor)startNew(selAnchor)})});

function startNew(an){
  if(!closeGuard())return;
  pending={id:uid("a-"),section:an.section,quote:an.quote,prefix:an.prefix,suffix:an.suffix,sectionLevel:false,items:[],createdAt:now(),updatedAt:now()};
  selAnchor=null;hideAnn();try{getSelection().removeAllRanges()}catch(e){}
  paint();openAnno(pending.id)}
function startSection(sec){
  if(!closeGuard())return;
  pending={id:uid("a-"),section:sec.id,quote:"",prefix:"",suffix:"",sectionLevel:true,items:[],createdAt:now(),updatedAt:now()};
  paint();openAnno(pending.id)}

/* Tap a highlight (or the highlighted math) to open it. Single click only, so double-click selection still works. */
let clickT=0;
document.addEventListener("click",e=>{
  const t=e.target instanceof Element?e.target:null;if(!t||!MAIN.contains(t))return;
  const m=t.closest("mark.anno,.anno-m");if(!m||t.closest("a,button,input,label,summary,textarea,select"))return;
  if(e.detail>1){clearTimeout(clickT);return}
  const id=m.dataset.id||(m.dataset.annoIds||"").split(" ").filter(Boolean).pop();if(!id)return;
  clearTimeout(clickT);clickT=setTimeout(()=>{if(!selActive())openAnno(id)},e.detail===0?0:260)});
document.addEventListener("keydown",e=>{
  if((e.key==="Enter"||e.key===" ")&&e.target instanceof Element&&e.target.matches("mark.anno[data-id]")){e.preventDefault();openAnno(e.target.dataset.id)}});

/* ---------- Drawer ---------- */
const scrim=h("div",{class:"anno-scrim","data-anno-ui":"",hidden:true});
const panel=h("aside",{class:"anno-panel","data-anno-ui":"",role:"dialog","aria-label":"Notes","aria-hidden":"true",tabindex:"-1"});
panel.inert=true;
const scroller=h("div",{class:"anno-scroll"});
const head=h("header",{class:"anno-head"});
const guard=h("div",{class:"anno-guard",hidden:true,role:"alert"});
const body=h("div",{class:"anno-body"});
const ed=h("textarea",{class:"anno-ed",id:"anno-ed",spellcheck:"true",placeholder:"Write a note or a question. Markdown works; $x^2$ for math."});
const pv=h("div",{class:"anno-pv anno-md","aria-label":"Preview"});
const edLbl=h("label",{class:"anno-lbl",for:"anno-ed"},h("span",{class:"anno-lbl-t",text:"Write"}),h("span",{class:"anno-hint",text:"Markdown · $…$ math"}));
const bSave=h("button",{type:"button",class:"anno-btn"},"Save as note");
const bAsk=h("button",{type:"button",class:"anno-btn ghost",hidden:true},"Ask Claude");
const bCancel=h("button",{type:"button",class:"anno-btn ghost",hidden:true},"Cancel");
const status=h("p",{class:"anno-status",role:"status"});
const syncLine=h("p",{class:"anno-sync"});
const composer=h("div",{class:"anno-composer"},edLbl,ed,h("div",{class:"anno-lbl"},h("span",{class:"anno-lbl-t",text:"Preview"})),pv,
  h("div",{class:"anno-row"},bSave,bAsk,bCancel),status);
scroller.append(head,guard,body,composer,syncLine);panel.append(scroller);
document.body.append(scrim,panel);

let view="closed",cur=null,listFilter=null,lastFocus=null;
let mode={m:"new",item:null};                // new | edit (item id) | fromAnswer (answer id)
const drafts={};
function showPanel(){
  if(view==="closed"){lastFocus=document.activeElement}
  panel.inert=false;panel.removeAttribute("aria-hidden");panel.classList.add("open");scrim.hidden=false;
  document.documentElement.classList.add("anno-open");hideAnn()}
function closePanel(force){
  if(!force&&!closeGuard())return;
  if(cur&&view==="anno"&&mode.m==="new")drafts[cur]=ed.value;
  if(pending&&!asking.has(pending.id)){pending=null;paint()}
  view="closed";cur=null;guard.hidden=true;
  panel.classList.remove("open");panel.setAttribute("aria-hidden","true");panel.inert=true;scrim.hidden=true;
  document.documentElement.classList.remove("anno-open");
  if(lastFocus&&lastFocus.isConnected&&typeof lastFocus.focus==="function"){try{lastFocus.focus({preventScroll:true})}catch(e){}}lastFocus=null}
/* Unsaved text in a brand-new annotation: ask in the page before throwing it away. Returns true if it is OK to leave. */
function closeGuard(){
  if(view!=="anno"||!pending||cur!==pending.id||!ed.value.trim()||asking.has(pending.id))return true;
  guard.hidden=false;guard.replaceChildren(h("span",{text:"This note is not saved yet."}),
    h("button",{type:"button",class:"anno-btn danger",onclick:()=>{ed.value="";updPv();guard.hidden=true;closePanel(true)}},"Discard"),
    h("button",{type:"button",class:"anno-btn ghost",onclick:()=>{guard.hidden=true;ed.focus()}},"Keep editing"));
  guard.querySelector("button").focus();return false}
scrim.addEventListener("click",()=>closePanel());
document.addEventListener("keydown",e=>{
  if(e.key!=="Escape"||view==="closed")return;
  const c=panel.querySelector(".anno-confirm:not([hidden])");
  if(c){c.hidden=true;return}
  if(!guard.hidden){guard.hidden=true;ed.focus();return}
  closePanel()});

function headRow(title,extra){
  return h("div",{class:"anno-head-row"},h("p",{class:"anno-kicker",text:title}),
    h("span",{class:"anno-head-btns"},extra||null,
      h("button",{type:"button",class:"anno-sbtn anno-x","aria-label":"Close notes",onclick:()=>closePanel()},"Close")))}
function openAnno(id,opts){
  const a=getA(id);if(!a)return;
  if(cur&&cur!==id&&!closeGuard())return;
  if(pending&&pending.id!==id&&!asking.has(pending.id)){pending=null;paint()}
  if(cur&&view==="anno"&&mode.m==="new")drafts[cur]=ed.value;
  const changed=cur!==id||view!=="anno";
  view="anno";cur=id;showPanel();composer.hidden=false;
  if(changed){setMode("new");ed.value=drafts[id]||"";updPv();status.textContent=""}
  renderAnno();
  if(opts&&opts.scroll)reveal(id);
  if(changed){scroller.scrollTop=0;
    if(!a.items.length&&!coarse())ed.focus({preventScroll:true});else panel.focus({preventScroll:true})}}
function reveal(id){
  const t=MAIN.querySelector(`mark.anno[data-id="${CSS.escape(id)}"]`)||[...MAIN.querySelectorAll(".anno-m")].find(x=>(x.dataset.annoIds||"").split(" ").includes(id));
  const a=getA(id);const target=t||(a&&a.sectionLevel&&document.getElementById(a.section));
  if(!target)return;
  target.scrollIntoView({block:"center",behavior:reduced()?"auto":"smooth"});
  if(t){const all=MAIN.querySelectorAll(`mark.anno[data-id="${CSS.escape(id)}"]`);all.forEach(m=>{m.classList.remove("flash");void m.offsetWidth;m.classList.add("flash")});
    setTimeout(()=>all.forEach(m=>m.classList.remove("flash")),1600)}}

function renderAnno(){
  const a=getA(cur);if(!a){closePanel(true);return}
  const sec=document.getElementById(a.section);
  const det=DETACHED.has(a.id);
  const kick=(sec?secTitle(sec):"Section “"+a.section+"”")+(det?" · detached":"");
  const nodes=[headRow(kick,h("button",{type:"button",class:"anno-sbtn",onclick:()=>openList(null)},"All notes"))];
  if(a.sectionLevel){nodes.push(h("blockquote",{class:"anno-quote whole",text:"Note on the whole section"}))}
  else{const q=h("blockquote",{class:"anno-quote clamp",text:a.quote});nodes.push(q);
    const more=h("button",{type:"button",class:"anno-more",hidden:true,"aria-expanded":"false"},"Show all");
    more.addEventListener("click",()=>{const open=q.classList.toggle("clamp");more.textContent=open?"Show all":"Show less";more.setAttribute("aria-expanded",String(!open))});
    nodes.push(more);requestAnimationFrame(()=>{if(q.scrollHeight>q.clientHeight+2)more.hidden=false})}
  if(det)nodes.push(h("p",{class:"anno-note",text:"This passage was not found in the current text, so it has no highlight. The note is kept."}));
  if(a.status==="addressed")nodes.push(h("p",{class:"anno-chip ok",text:"Addressed"}));
  head.replaceChildren(...nodes);
  renderCards(a);bAsk.hidden=!canAsk()||mode.m!=="new"}
const cards=h("div",{class:"anno-cards"});
function renderCards(a){
  a=a||getA(cur);if(!a)return;body.replaceChildren(cards);
  const kids=a.items.map(it=>card(a,it));
  if(!kids.length)kids.push(h("p",{class:"anno-empty",text:a.sectionLevel?"Write a note about this section below, or ask Claude about it.":"Write a note about the marked text below, or ask Claude about it."}));
  cards.replaceChildren(...kids)}
function card(a,it,bare){
  const t=it.type in TYPE?it.type:"note";
  const c=h("article",{class:"anno-card t-"+t,"data-item":it.id||""});
  const time=it.at?fmtTime(it.at)+(it.editedAt?" · edited":""):"";
  c.append(h("div",{class:"anno-card-h"},h("span",{class:"anno-type",text:TYPE[t]}),h("time",{datetime:it.editedAt||it.at||"",text:time})));
  const b=h("div",{class:"anno-md"});b.innerHTML=md(it.md);c.append(b);
  if(bare)return c;
  const acts=h("div",{class:"anno-acts"});
  const confirm=h("div",{class:"anno-confirm",hidden:true});
  const askDel=()=>{confirm.hidden=false;confirm.replaceChildren(h("span",{text:`Delete this ${t==="answer"?"answer":t}?`}),
    h("button",{type:"button",class:"anno-btn danger",onclick:()=>delItem(a,it.id)},"Delete"),
    h("button",{type:"button",class:"anno-btn ghost",onclick:()=>{confirm.hidden=true}},"Keep"));confirm.querySelector("button").focus()};
  if(t==="answer"){
    const saved=a.items.some(x=>x.fromAnswer===it.id);
    acts.append(h("button",{type:"button",class:"anno-sbtn",disabled:saved,onclick:()=>{
        a.items.push({id:uid("i-"),type:"note",md:it.md,at:now(),fromAnswer:it.id});commitAnno(a);renderCards(a);status.textContent="Saved as a note. You can edit it any time."}},saved?"Saved as note ✓":"Save as note"),
      h("button",{type:"button",class:"anno-sbtn",onclick:()=>{setMode("fromAnswer",it.id);ed.value=it.md;updPv();ed.focus({preventScroll:true});composer.scrollIntoView({block:"start",behavior:reduced()?"auto":"smooth"})}},"Edit, then save"))}
  else acts.append(h("button",{type:"button",class:"anno-sbtn",onclick:()=>{setMode("edit",it.id);ed.value=it.md;updPv();ed.focus({preventScroll:true});composer.scrollIntoView({block:"start",behavior:reduced()?"auto":"smooth"})}},"Edit"));
  acts.append(h("button",{type:"button",class:"anno-sbtn danger",onclick:askDel},"Delete"));
  c.append(acts,confirm);return c}
function delItem(a,itemId){
  a.items=a.items.filter(x=>x.id!==itemId);
  if(mode.item===itemId){setMode("new");ed.value="";updPv()}
  if(!a.items.length){if(pending===a){closePanel(true);return}a.deleted=true;commitAnno(a);closePanel(true);return}
  commitAnno(a);renderCards(a);status.textContent="Deleted."}

function setMode(m,item){mode={m,item:item||null};
  const lbl=$(".anno-lbl-t",edLbl);
  if(m==="edit"){const it=(getA(cur)||{items:[]}).items.find(x=>x.id===item);lbl.textContent="Editing "+((it&&TYPE[it.type])||"note").toLowerCase();bSave.textContent="Save changes"}
  else if(m==="fromAnswer"){lbl.textContent="New note from Claude’s answer";bSave.textContent="Save as note"}
  else{lbl.textContent="Write";bSave.textContent="Save as note"}
  bCancel.hidden=m==="new";bAsk.hidden=m!=="new"||!canAsk()}
let pvRaf=0;
function updPv(){cancelAnimationFrame(pvRaf);pvRaf=requestAnimationFrame(()=>{const v=ed.value;pv.innerHTML=v.trim()?md(v):'<p class="anno-ph">The preview appears here.</p>'})}
ed.addEventListener("input",()=>{updPv();if(mode.m==="new"&&cur)drafts[cur]=ed.value});
bCancel.addEventListener("click",()=>{setMode("new");ed.value=drafts[cur]||"";updPv();status.textContent=""});
bSave.addEventListener("click",()=>{
  const text=ed.value.trim();if(!text){status.textContent="Write something first.";ed.focus();return}
  const a=getA(cur);if(!a)return;let newId=null;
  if(mode.m==="edit"){const it=a.items.find(x=>x.id===mode.item);
    if(it&&it.md!==text){it.md=text;it.editedAt=now();commitAnno(a)}newId=mode.item;status.textContent="Changes saved."}
  else{const it={id:uid("i-"),type:"note",md:text,at:now()};if(mode.m==="fromAnswer")it.fromAnswer=mode.item;
    a.items.push(it);commitAnno(a);newId=it.id;status.textContent="Saved."}
  ed.value="";drafts[a.id]="";setMode("new");updPv();renderAnno();
  const c=cards.querySelector(`[data-item="${CSS.escape(newId)}"]`);if(c)c.scrollIntoView({block:"nearest",behavior:reduced()?"auto":"smooth"})});
function commitAnno(a){
  if(pending&&pending.id===a.id)pending=null;
  a.updatedAt=now();if(a.items.length)a.deleted=false;
  S.set(a.id,a);LS.put(a);paint();push(a.id)}

/* ---------- All notes ---------- */
function openList(filter){
  if(view==="anno"&&!closeGuard())return;
  if(cur&&view==="anno"&&mode.m==="new")drafts[cur]=ed.value;
  if(pending&&!asking.has(pending.id)){pending=null;paint()}
  view="list";cur=null;listFilter=filter||null;showPanel();composer.hidden=true;status.textContent="";
  renderList();scroller.scrollTop=0;panel.focus({preventScroll:true})}
function renderList(){
  const all=live(),secs=$$("section",MAIN),order=new Map(secs.map((s,i)=>[s.id,i]));
  const shown=listFilter?all.filter(a=>a.section===listFilter):all;
  head.replaceChildren(headRow(listFilter?titleOf(listFilter):`All notes · ${all.length}`,
    listFilter?h("button",{type:"button",class:"anno-sbtn",onclick:()=>{listFilter=null;renderList()}},"All notes"):null));
  if(!shown.length){body.replaceChildren(h("p",{class:"anno-empty",html:"No notes yet. Select any text in the post and tap <b>Annotate</b>, or use <b>Note on this section</b> at the end of a section."}));return}
  const groups=new Map();
  shown.forEach(a=>{const k=order.has(a.section)?a.section:"__detached";if(!groups.has(k))groups.set(k,[]);groups.get(k).push(a)});
  const keys=[...groups.keys()].sort((x,y)=>(order.has(x)?order.get(x):1e9)-(order.has(y)?order.get(y):1e9));
  const wrapEl=h("div",{class:"anno-list"});
  for(const k of keys){const g=h("div",{class:"anno-group"},h("p",{class:"anno-group-h",text:k==="__detached"?"Detached (section not found)":titleOf(k)}));
    groups.get(k).sort((x,y)=>{const d=(x.sectionLevel?0:1)-(y.sectionLevel?0:1);return d||String(x.createdAt).localeCompare(String(y.createdAt))})
      .forEach(a=>{const first=a.items[0],det=DETACHED.has(a.id);
        const b=h("button",{type:"button",class:"anno-entry "+kind(a),onclick:()=>openAnno(a.id,{scroll:!det})},
          a.sectionLevel?h("span",{class:"anno-entry-q whole",text:"Whole section"}):h("span",{class:"anno-entry-q",text:"“"+a.quote+"”"}),
          h("span",{class:"anno-entry-f",text:firstLine(first&&first.md)}),
          h("span",{class:"anno-entry-m",text:[a.items.length+" item"+(a.items.length>1?"s":""),a.items.some(x=>x.type==="answer")?"Q&A":"",det?"detached":"",a.status==="addressed"?"addressed":""].filter(Boolean).join(" · ")}));
        g.append(b)});
    wrapEl.append(g)}
  body.replaceChildren(wrapEl)}
function refreshPanel(){if(view==="anno"&&cur){if(getA(cur))renderAnno();else closePanel(true)}else if(view==="list")renderList()}

/* ---------- Ask Claude ---------- */
let SAMPLE=null,askOff=false;const asking=new Set();let ctl=null;
const canAsk=()=>!!SAMPLE&&!askOff;
const BLOCK=/^(P|DIV|SECTION|H1|H2|H3|H4|H5|LI|UL|OL|FIGURE|FIGCAPTION|TABLE|TR|PRE|BLOCKQUOTE|DL|DT|DD|DETAILS|SUMMARY|HEADER|MAIN|ASIDE|BR)$/;
const EXCL_PLAIN="[data-anno-ui],.sec-tools,script,style,button,svg,input,textarea,select,noscript";
function plain(root){const out=[];
  (function walk(n){for(const c of n.childNodes){
    if(c.nodeType===3){out.push(c.data);continue}if(c.nodeType!==1||c.matches(EXCL_PLAIN))continue;
    if(c.localName==="math"){const t=c.querySelector("annotation");const tex=t?t.textContent.trim():c.textContent;
      out.push(c.getAttribute("display")==="block"?"\n$$"+tex+"$$\n":"$"+tex+"$");continue}
    const b=BLOCK.test(c.tagName);if(b)out.push("\n");if(c.tagName==="TD"||c.tagName==="TH")out.push(" | ");walk(c);if(b)out.push("\n")}})(root);
  return out.join("").replace(/[ \t ]+/g," ").replace(/ *\n */g,"\n").replace(/\n{3,}/g,"\n\n").trim()}
let BRIEF=null;try{const b=document.getElementById("brief-data");BRIEF=b?JSON.parse(b.textContent):null}catch(e){BRIEF=null}
const bytes=s=>new TextEncoder().encode(s).length;
async function buildTurns(a,q){
  let max=262144;try{const l=await SAMPLE.limits();if(l&&l.maxPromptBytes)max=l.maxPromptBytes}catch(e){}
  const budget=max-12000;
  const sec=document.getElementById(a.section),title=sec?secTitle(sec):a.section;
  const pairs=[];a.items.forEach(it=>{if(it.type!=="question")return;const ans=a.items.find(x=>x.type==="answer"&&x.askedAbout===it.id);if(ans)pairs.push([it.md,ans.md])});
  const notes=a.items.filter(x=>x.type==="note").map(x=>"- "+x.md.replace(/\n/g,"\n  ")).join("\n");
  const rules=`You are the AI4Read tutor for Kunhao, an assistant professor in computational social science. His English is B2–C1. He has marked a passage in the AI4Read post "What does an LLM know when it predicts the next word?" and asks about it.
How to answer:
- Explain as if to a curious high-school student, but never skip steps.
- Start with a concrete instance (small numbers, a real example), then generalise.
- Ground every claim in the post or the source brief below and give the page reference, e.g. (Shannon 1951, p. 56). Keep the authors' hedges.
- If you use knowledge from outside these sources, start that part with "Beyond our sources:".
- Markdown is fine (short paragraphs, lists, bold). Write inline math as $...$ and display math as $$...$$.
- About 250 words unless he asks for more.`;
  const passage=a.sectionLevel?`HE IS ASKING ABOUT THE WHOLE SECTION "${title}".`:
    `THE MARKED PASSAGE (section "${title}"; the marked words are between [[ and ]]):\n…${a.prefix||""}[[${a.quote}]]${a.suffix||""}…`;
  const tail=[...pairs.flat(),q].join("\n");
  let secText=sec?plain(sec):"";
  const fixed=rules+"\n\n"+passage+(notes?"\n\nHIS OWN NOTES ON THIS PASSAGE:\n"+notes:"")+"\n\nTHE SECTION:\n";
  const room=budget-bytes(fixed)-bytes(tail)-200;
  if(bytes(secText)>room)secText=secText.slice(0,Math.max(0,Math.floor(room/3)))+"\n[section text shortened]";
  let ctx=fixed+secText;
  const post=plain(MAIN);
  if(bytes(ctx)+bytes(tail)+bytes(post)+100<budget)ctx+="\n\nTHE WHOLE POST:\n"+post;
  if(BRIEF&&bytes(ctx)+bytes(tail)+bytes(BRIEF)+100<budget)ctx+="\n\nSOURCE BRIEF (claims with page references, from the AI4Read reading digests):\n"+BRIEF;
  const turns=[];
  if(pairs.length){turns.push({role:"user",content:ctx+"\n\nQUESTION:\n"+pairs[0][0]},{role:"assistant",content:pairs[0][1]});
    pairs.slice(1).forEach(([qq,aa])=>turns.push({role:"user",content:qq},{role:"assistant",content:aa}));
    turns.push({role:"user",content:q})}
  else turns.push({role:"user",content:ctx+"\n\nQUESTION:\n"+q});
  return turns}
function setAskBusy(on){bAsk.textContent=on?"Stop":"Ask Claude";bSave.disabled=on;bAsk.classList.toggle("busy",on)}
bAsk.addEventListener("click",async()=>{
  if(asking.size){if(ctl)ctl.abort();return}
  const q=ed.value.trim();if(!q){status.textContent="Write your question first.";ed.focus();return}
  if(!canAsk())return;
  const a=getA(cur);if(!a)return;
  asking.add(a.id);ctl=new AbortController();const myCtl=ctl;
  ed.value="";drafts[a.id]="";updPv();status.textContent="";
  const qCard=card(a,{type:"question",md:q,at:now()},true);qCard.classList.add("live");
  const aCard=card(a,{type:"answer",md:"",at:""},true);aCard.classList.add("live");
  const aBody=$(".anno-md",aCard);aBody.innerHTML='<p class="anno-thinking">Thinking…</p>';
  const empty=$(".anno-empty",cards);if(empty)empty.remove();
  cards.append(qCard,aCard);aCard.scrollIntoView({block:"nearest",behavior:reduced()?"auto":"smooth"});
  setAskBusy(true);
  let raf=0,latest="";
  try{
    const turns=await buildTurns(a,q);
    const res=await SAMPLE(turns,{modelTier:"complex",cache:false,signal:myCtl.signal,onText:({text})=>{latest=text;
      if(!raf)raf=requestAnimationFrame(()=>{raf=0;aBody.innerHTML=md(latest)})}});
    cancelAnimationFrame(raf);
    const qi={id:uid("i-"),type:"question",md:q,at:now()};
    const ai={id:uid("i-"),type:"answer",md:res.text+(res.truncated?"\n\n*(The answer was cut short.)*":""),at:now(),askedAbout:qi.id};
    a.items.push(qi,ai);commitAnno(a);
    if(cur===a.id&&view==="anno"){renderAnno();status.textContent="Question and answer saved. “Save as note” keeps the answer as your own note."}
  }catch(e){
    cancelAnimationFrame(raf);qCard.remove();aCard.remove();
    const code=e&&e.code;
    if(cur===a.id&&view==="anno"){ed.value=q;updPv();if(!a.items.length)renderCards(a)}else drafts[a.id]=q;
    const msg={not_granted:"Asking Claude is not allowed in this view. Your question is back in the editor; save it as a note instead.",
      sampling_disabled:"Claude is not available for this account. Your question is back in the editor; save it as a note.",
      not_declared:"Asking Claude is not available on this page. Save your question as a note.",
      capability_disabled:"Asking Claude is not available here. Save your question as a note.",
      capability_removed:"Asking Claude is not available here. Save your question as a note.",
      rate_limited:"Too many questions in a short time. Wait a minute, then ask again. Your question is still in the editor.",
      session_expired:"Your Claude session has expired. Sign in again, then ask. Your question is still in the editor.",
      refused:"Claude did not answer this question. Try asking it differently.",
      prompt_too_large:"The question and context were too long. Try a shorter question.",
      cancelled:""}[code];
    if(["not_granted","sampling_disabled","not_declared","capability_disabled","capability_removed"].includes(code)){askOff=true;bAsk.hidden=true}
    status.textContent=msg!=null?msg:`The answer did not arrive (${code||"error"}). Your question is still in the editor: ask again or save it as a note.`;
  }finally{asking.delete(a.id);if(ctl===myCtl)ctl=null;setAskBusy(false);
    if(pending&&pending.id===a.id&&!a.items.length&&cur!==a.id){pending=null;paint()}}});

/* ---------- db sync ---------- */
let DB=null,dbRO=false;const run={},again={};
function setSync(s){syncLine.textContent={ok:"Synced to your account.",local:"Saved on this device only.",quota:"The notes store is full; new notes are saved on this device only.",busy:"Saving…"}[s]||"";syncLine.dataset.s=s}
setSync("local");
const toDoc=a=>{const o={};for(const k of ["section","quote","prefix","suffix","sectionLevel","items","createdAt","updatedAt","deleted","legacyFrom","legacyReply","status"])if(a[k]!==undefined)o[k]=a[k];
  o.sectionLevel=!!o.sectionLevel;o.deleted=!!o.deleted;return JSON.parse(JSON.stringify(o))};
const fromDoc=d=>{const o=JSON.parse(JSON.stringify(d.data()||{}));o.id=d.id;if(!Array.isArray(o.items))o.items=[];return o};
async function push(id){
  if(!DB||dbRO)return;if(run[id]){again[id]=true;return}
  run[id]=true;
  try{do{again[id]=false;const a=S.get(id);if(!a)break;await writeDoc(a,true)}while(again[id]&&DB&&!dbRO)}
  finally{run[id]=false}}
async function writeDoc(a,retry){
  const body=toDoc(a);setSync("busy");
  try{await DB.collection(COLL).doc(a.id).set(body);setSync("ok")}
  catch(e){const c=e&&e.code;
    if(c==="unavailable"&&retry){await sleep(700+Math.random()*1200);return writeDoc(a,false)}
    if(c==="quota_exceeded"){setSync("quota");return}
    if(c!=="unavailable"&&c!=="resource_exhausted")dbRO=true;
    setSync("local")}}
function merge(r){const l=S.get(r.id);if(!l||newer(r,l)){S.set(r.id,r);LS.put(r);return 1}if(newer(l,r))return -1;return 0}
async function migrateLegacy(){
  let snap;try{snap=await DB.collection(LEGACY).get()}catch(e){return}
  for(const d of snap.docs){if(!d.exists)continue;const o=d.data()||{},id="legacy-"+d.id;
    let a=S.get(id),changed=false;
    if(!a){const at=o.at||now(),q=String(o.q||"").trim(),isAsk=o.kind==="ask"&&!!o.a;
      a={id,section:String(o.section||""),quote:"",prefix:"",suffix:"",sectionLevel:true,items:[],createdAt:at,updatedAt:at,legacyFrom:d.id};
      if(q)a.items.push({id:id+"-q",type:isAsk?"question":"note",md:q,at});
      if(o.a)a.items.push({id:id+"-a",type:"answer",md:String(o.a),at,askedAbout:id+"-q"});
      if(!a.items.length)continue;changed=true}
    else a=JSON.parse(JSON.stringify(a));
    if(!a.deleted&&o.reply&&String(o.reply)!==a.legacyReply){const r=String(o.reply),it=a.items.find(x=>x.id===id+"-r");
      if(it){it.md=r;it.editedAt=now()}else a.items.push({id:id+"-r",type:"answer",md:r,at:o.repliedAt||now(),askedAbout:(a.items[0]||{}).id});
      a.legacyReply=r;changed=true}
    if(o.status&&o.status!==a.status){a.status=String(o.status);changed=true}
    if(changed){a.updatedAt=now();S.set(id,a);LS.put(a);await push(id)}}}
async function initDb(){
  let db=null;try{if(window.claude&&typeof window.claude.use==="function")db=await window.claude.use("db")}catch(e){db=null}
  if(!db)return;DB=db;
  let snap=null;
  for(let i=0;i<2&&!snap;i++){try{snap=await DB.collection(COLL).get()}catch(e){if(e&&e.code==="unavailable"&&i===0){await sleep(1000);continue}DB=null;return}}
  if(!snap){DB=null;return}
  const remote=new Set(),toPush=[];
  snap.docs.forEach(d=>{if(!d.exists)return;const r=fromDoc(d);remote.add(r.id);if(merge(r)<0)toPush.push(r.id)});
  for(const id of S.keys())if(!remote.has(id))toPush.push(id);
  setSync("ok");
  for(const id of toPush)await push(id);
  await migrateLegacy();
  paint();refreshPanel();
  DB.collection(COLL).onSnapshot(qs=>{let ch=false;
    for(const c of qs.docChanges()){if(c.type==="removed"||!c.doc.exists)continue;
      const r=fromDoc(c.doc);if(asking.has(r.id))continue;if(merge(r)>0)ch=true}
    if(ch){paint();if(!(view==="anno"&&mode.m!=="new"))refreshPanel()}},()=>{});}

async function initSample(){
  let s=null;try{if(window.claude&&typeof window.claude.use==="function")s=await window.claude.use("sample")}catch(e){s=null}
  if(typeof s==="function"){SAMPLE=s;if(view==="anno"&&mode.m==="new")bAsk.hidden=!canAsk()}}

/* ---------- start ---------- */
addSecButtons();
try{const mo=new MutationObserver(addSecButtons);$$("section",MAIN).forEach(s=>mo.observe(s,{childList:true}))}catch(e){}
document.addEventListener("DOMContentLoaded",()=>setTimeout(addSecButtons,0));
paint();updPv();
initDb();initSample();
})();
