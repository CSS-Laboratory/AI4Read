(function(){
"use strict";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const LS={get(k,d){try{const v=localStorage.getItem("ai4read-p01-"+k);return v==null?d:JSON.parse(v)}catch(e){return d}},
          set(k,v){try{localStorage.setItem("ai4read-p01-"+k,JSON.stringify(v))}catch(e){}}};
const f3=x=>Number.isFinite(x)?x.toFixed(3):"∞", f2=x=>x.toFixed(2);
const log2=Math.log2;
const el=(tag,attrs={},html)=>{const e=document.createElement(tag);for(const k in attrs){if(k==="class")e.className=attrs[k];else e.setAttribute(k,attrs[k])}if(html!=null)e.innerHTML=html;return e};
function slider(host,{id,label,min,max,step,value,fmt=f2},on){
  const row=el("div",{class:"sl"});
  const lab=el("label",{for:id},label); const inp=el("input",{type:"range",id,min,max,step,value}); const out=el("output",{for:id});
  row.append(lab,inp,out); host.append(row);
  const upd=()=>{out.textContent=fmt(+inp.value);on()}; inp.addEventListener("input",upd); out.textContent=fmt(+inp.value);
  return inp;
}

/* ---------- capabilities (db for notes/guesses, sample for questions) ---------- */
let DB=null, SAMPLE=null, DL=null;
const capsReady=(async()=>{
  try{ if(window.claude&&window.claude.use){ DB=await window.claude.use("db"); } }catch(e){DB=null}
  try{ if(window.claude&&window.claude.use){ SAMPLE=await window.claude.use("sample"); } }catch(e){SAMPLE=null}
  try{ if(window.claude&&window.claude.use){ DL=await window.claude.use("downloads"); } }catch(e){DL=null}
  document.dispatchEvent(new Event("caps"));
})();
async function dbAdd(coll,data){ if(!DB) return false; try{ await DB.collection(coll).add(data); return true }catch(e){ return false } }
async function dbSet(path,data){ if(!DB) return false; try{ await DB.doc(path).set(data); return true }catch(e){ return false } }

/* ---------- Guess first ---------- */
const guesses=LS.get("guesses",{});
$$(".quiz").forEach(qz=>{
  const id=qz.dataset.q, btns=$$(".opts button",qz), your=$(".your",qz);
  const mark=i=>{btns.forEach((b,j)=>b.setAttribute("aria-pressed",String(i===j)));your.hidden=false;
    your.textContent="Your guess is saved. The answer is in section "+({g1:"4 (Lens 1)",g2:"3 (Step 7)",g3:"4 (Lens 5)"}[id])+".";};
  btns.forEach((b,i)=>{b.setAttribute("aria-pressed","false");b.addEventListener("click",()=>{
    guesses[id]={i,text:b.textContent,at:new Date().toISOString()};LS.set("guesses",guesses);mark(i);unlock(id);
    dbSet("guesses/"+id,{question:id,choice:b.textContent,at:guesses[id].at});
  })});
  if(guesses[id]) mark(guesses[id].i);
});
function unlock(id){const r=$(`.reveal[data-for="${id}"]`); if(r) r.classList.remove("locked")}
$$(".reveal").forEach(r=>{ if(!guesses[r.dataset.for]) r.classList.add("locked");
  r.addEventListener("click",()=>r.classList.remove("locked")); r.tabIndex=0;
  r.addEventListener("keydown",e=>{if(e.key==="Enter")r.classList.remove("locked")}); });

/* ---------- Shannon's guessing game ---------- */
(function(){
  const PHRASE="A GOOD GUESS IS A SHORT MESSAGE", ALPH="ABCDEFGHIJKLMNOPQRSTUVWXYZ ";
  const textHost=$("#game-text"), keys=$("#game-keys"), stats=$("#game-stats"), bounds=$("#game-bounds");
  let st=LS.get("game",null); if(!st||st.phrase!==PHRASE) st={phrase:PHRASE,pos:0,counts:[],tried:[]};
  const cells=[...PHRASE].map(()=>{const c=el("div",{class:"gch"},'<span class="l"></span><span class="n"></span>');textHost.append(c);return c});
  const kb=[...ALPH].map(ch=>{const b=el("button",{type:"button","aria-label":ch===" "?"space":ch},ch===" "?"␣":ch);
    b.addEventListener("click",()=>guess(ch));keys.append(b);return b});
  function guess(ch){ if(st.pos>=PHRASE.length||st.tried.includes(ch))return; st.tried.push(ch);
    if(ch===PHRASE[st.pos]){st.counts[st.pos]=st.tried.length;st.pos++;st.tried=[]} save();render(); }
  function save(){LS.set("game",st); if(st.pos>=PHRASE.length) dbSet("game/result",{counts:st.counts,at:new Date().toISOString()})}
  $("#game-reveal").addEventListener("click",()=>{if(st.pos<PHRASE.length){st.counts[st.pos]=null;st.pos++;st.tried=[];save();render()}});
  $("#game-reset").addEventListener("click",()=>{st={phrase:PHRASE,pos:0,counts:[],tried:[]};save();render()});
  function render(){
    cells.forEach((c,i)=>{const done=i<st.pos;c.classList.toggle("cur",i===st.pos);
      $(".l",c).textContent=done?(PHRASE[i]===" "?"␣":PHRASE[i]):"";
      const n=$(".n",c);n.textContent=done?(st.counts[i]==null?"–":st.counts[i]):"";n.classList.toggle("one",done&&st.counts[i]===1)});
    kb.forEach((b,j)=>b.disabled=st.pos>=PHRASE.length||st.tried.includes(ALPH[j]));
    const got=st.counts.slice(0,st.pos).filter(x=>x!=null);
    if(!got.length){stats.textContent="Your reduced text will appear here.";bounds.textContent="Play the guessing game in section 1 to see your own bounds here.";return}
    const n=got.length, ones=got.filter(x=>x===1).length, maxI=Math.max(...got);
    const q=[];for(let i=1;i<=maxI+1;i++)q[i]=got.filter(x=>x===i).length/n;
    let up=0,lo=0;for(let i=1;i<=maxI;i++){if(q[i]>0)up-=q[i]*log2(q[i]);lo+=i*(q[i]-(q[i+1]||0))*log2(i)}
    stats.textContent=`Reduced text: ${got.join(" ")}\nFirst-try hits: ${ones} of ${n} (${Math.round(100*ones/n)}%).`+(st.pos>=PHRASE.length?" Done. Shannon’s subject got 77% right on the first guess (79 of 102 letters).":"");
    bounds.textContent=`From your ${n} letters: upper bound −Σ q·log q = ${f2(up)} bits/letter; lower bound Σ i(qᵢ−qᵢ₊₁)log i = ${f2(lo)} bits/letter. With so few letters these are rough, and this phrase is short and easy to guess.`;
  }
  stats.style.whiteSpace="pre-line"; render();
})();

/* ---------- Shannon chart: first-guess % by context (Shannon 1951, p. 57) ---------- */
(function(){
  const N=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","100"], V=[18.2,29.2,36,47,51,58,48,66,66,67,62,58,66,72,60,80];
  const W=340,H=170,L=30,B=24,T=8,bw=(W-L-6)/N.length;
  let s=`<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Bar chart: first-guess success rises from 18% with no letters known to 80% with 100 letters known">`;
  [0,25,50,75,100].forEach(t=>{const y=T+(H-B-T)*(1-t/100);s+=`<line x1="${L}" x2="${W-4}" y1="${y}" y2="${y}" stroke="var(--rule)" stroke-width="1"/><text x="${L-4}" y="${y+3.5}" text-anchor="end">${t}%</text>`});
  V.forEach((v,i)=>{const x=L+3+i*bw,h=(H-B-T)*v/100;s+=`<rect x="${x+1}" y="${H-B-h}" width="${bw-3}" height="${h}" fill="${i===15?"var(--stamp)":"var(--ink)"}" opacity="${i===15?1:.8}"/>`;
    if(i%2===0||i===15)s+=`<text x="${x+bw/2-1}" y="${H-B+13}" text-anchor="middle">${N[i]}</text>`});
  s+=`<text x="${L+(W-L)/2}" y="${H-1}" text-anchor="middle">letters known before guessing</text></svg>`;
  $("#fig-shannon").insertAdjacentHTML("beforeend",s);
})();

/* ---------- Cross-entropy lab ---------- */
(function(){
  const P=[.5,.25,.125,.125], W=["rain","sun","wind","snow"], H=1.75;
  const barsHost=$("#xent-bars"), sl=$("#xent-sliders"), read=$("#xent-read");
  const bars=W.map((w,i)=>{const b=el("div",{class:"bar"},`<div class="pair"><i class="p" style="height:${P[i]*100}%"></i><i class="q"></i></div><span>${w}</span>`);barsHost.append(b);return $(".q",b)});
  const ins=W.map((w,i)=>slider(sl,{id:"xq"+i,label:"q("+w+")",min:.01,max:1,step:.01,value:.25},upd));
  function q(){const r=ins.map(x=>+x.value),s=r.reduce((a,b)=>a+b,0);return r.map(x=>x/s)}
  function upd(){const Q=q();Q.forEach((v,i)=>bars[i].style.height=(v*100)+"%");
    const ce=-P.reduce((a,p,i)=>a+p*log2(Q[i]),0),D=ce-H;
    $("#xent-stack .seg-h").style.width=(100*H/Math.max(ce,4))+"%";$("#xent-stack .seg-d").style.width=(100*D/Math.max(ce,4))+"%";
    read.textContent=`q = (${Q.map(f3).join(", ")})\ncost H+D = ${f3(ce)} bits  =  H ${f3(H)}  +  D ${f3(D)}\nperplexity 2^${f3(ce)} = ${f2(2**ce)}`;}
  read.style.whiteSpace="pre-line";
  $$("#lab-xent .presets button").forEach(b=>b.addEventListener("click",()=>{b.dataset.q.split(",").forEach((v,i)=>{ins[i].value=v;ins[i].dispatchEvent(new Event("input"))})}));
  upd();
})();

/* ---------- A/B/C text generator ---------- */
(function(){
  const L="ABC", PI=[9/27,16/27,2/27], T=[[0,.8,.2],[.5,.5,0],[.5,.4,.1]];
  const F=[log2(3),1.2538,0.9340], PP=[3,2.3847,1.9106];
  let order=2; const out=$("#gen-out"), read=$("#gen-read");
  const pick=p=>{let r=Math.random(),c=0;for(let i=0;i<p.length;i++){c+=p[i];if(r<c)return i}return p.length-1};
  function gen(){let s="",prev=pick(PI);for(let k=0;k<48;k++){const i=order===0?pick([1/3,1/3,1/3]):order===1?pick(PI):pick(T[prev]);s+=L[i];prev=i}
    out.textContent=s; read.textContent=`F = ${F[order].toFixed(3)} bits per letter, perplexity ${PP[order].toFixed(2)}`+(order===2?"  ·  never AA, never BC":"");}
  $$("#lab-gen .seg button").forEach(b=>b.addEventListener("click",()=>{order=+b.dataset.o;$$("#lab-gen .seg button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));gen()}));
  $("#gen-go").addEventListener("click",gen); gen();
})();

/* ---------- Attention lab ---------- */
(function(){
  const K=[[1,0],[0,1],[1,1]], V=[[1,0],[0,1],[2,2]];
  const sl=$("#att-sliders"), heat=$("#att-heat"), read=$("#att-read");
  const qx=slider(sl,{id:"aqx",label:"query x",min:-2,max:2,step:.1,value:1,fmt:x=>x.toFixed(1)},upd);
  const qy=slider(sl,{id:"aqy",label:"query y",min:-2,max:2,step:.1,value:1,fmt:x=>x.toFixed(1)},upd);
  const sc=slider(sl,{id:"asc",label:"sharpness",min:.25,max:4,step:.25,value:1,fmt:x=>"×"+x},upd);
  function upd(){const Q=[[1,0],[0,1],[+qx.value,+qy.value]],k=+sc.value;
    let h='<div class="hd"></div>'+["t1","t2","t3"].map(t=>`<div class="hd">key ${t}</div>`).join("");let o3=[0,0];
    for(let i=0;i<3;i++){const s=K.slice(0,i+1).map(kk=>k*(Q[i][0]*kk[0]+Q[i][1]*kk[1])/Math.SQRT2),m=Math.max(...s),e=s.map(x=>Math.exp(x-m)),z=e.reduce((a,b)=>a+b,0),w=e.map(x=>x/z);
      h+=`<div class="hd">q t${i+1}</div>`;for(let j=0;j<3;j++){if(j>i)h+='<div class="masked">–</div>';else h+=`<div style="background:color-mix(in srgb,var(--stamp) ${Math.round(w[j]*85)}%,transparent);color:${w[j]>.55?"var(--paper)":"var(--ink)"}">${w[j].toFixed(3)}</div>`}
      if(i===2)o3=[0,1].map(d=>w.reduce((a,wj,j)=>a+wj*V[j][d],0));}
    heat.innerHTML=h; read.textContent=`token 3 output = (${o3[0].toFixed(3)}, ${o3[1].toFixed(3)})  ·  values: (1,0) (0,1) (2,2)`;}
  upd();
})();

/* ---------- Analogy lab ---------- */
(function(){
  const base={man:[1,0,0],woman:[0,1,0],king:[.6,0,.8]}; const sl=$("#ana-sliders"), rank=$("#ana-rank");
  const qs=["x","y","z"].map((a,i)=>slider(sl,{id:"aq"+a,label:"queen "+a,min:-1,max:1,step:.05,value:[0,.6,.8][i]},upd));
  const cos=(a,b)=>{const d=a[0]*b[0]+a[1]*b[1]+a[2]*b[2],n=Math.hypot(...a)*Math.hypot(...b);return n?d/n:0};
  function upd(){const W={...base,queen:qs.map(x=>+x.value)};const y=W.king.map((v,i)=>v-W.man[i]+W.woman[i]);
    const r=Object.entries(W).map(([w,v])=>[w,cos(v,y)]).sort((a,b)=>b[1]-a[1]);
    rank.innerHTML=r.map(([w,c],i)=>`<div class="${i===0?"win":""}"><span>${w}</span><i style="width:${Math.max(0,c)*100}%"></i><span>${c.toFixed(3)}</span></div>`).join("")+
      `<p class="small" style="margin:4px 0 0">y = king − man + woman = (${y.map(v=>v.toFixed(2)).join(", ")}). ${r[0][0]==="queen"?"The analogy works.":"The analogy fails: "+r[0][0]+" is closest. Excluding the input words would change the answer."}</p>`;}
  upd();
})();

/* ---------- ICL posterior lab ---------- */
(function(){
  const sl=$("#icl-sliders"), bars=$("#icl-bars"), read=$("#icl-read");
  const n=slider(sl,{id:"in",label:"examples n",min:0,max:10,step:1,value:2,fmt:x=>String(x)},upd);
  const lr=slider(sl,{id:"ilr",label:"evidence ratio",min:1,max:8,step:.5,value:4,fmt:x=>x+"×"},upd);
  const pr=slider(sl,{id:"ipr",label:"prior θ*",min:.05,max:.95,step:.05,value:.5},upd);
  function upd(){const N=+n.value,R=+lr.value,p0=+pr.value;const a=p0*Math.pow(R,N),post=a/(a+(1-p0));const right=.9*post+.1*(1-post);
    bars.innerHTML=`<div><span>P(θ* | prompt)</span><i style="width:${post*100}%"></i><span>${post.toFixed(3)}</span></div><div class="ans"><span>P(right answer)</span><i style="width:${right*100}%"></i><span>${right.toFixed(3)}</span></div>`;
    read.textContent=`posterior = ${p0}·${R}^${N} / (${p0}·${R}^${N} + ${(1-p0).toFixed(2)}) = ${post.toFixed(3)}\nP(right) = 0.9·${post.toFixed(3)} + 0.1·${(1-post).toFixed(3)} = ${right.toFixed(3)}`;}
  read.style.whiteSpace="pre-line"; upd();
})();

/* ---------- Copy buttons ---------- */
$$(".code[data-copy]").forEach(box=>{const b=el("button",{type:"button",class:"copy"},"Copy");box.append(b);
  b.addEventListener("click",()=>{const t=$("code",box).textContent;const done=()=>{b.textContent="Copied";setTimeout(()=>b.textContent="Copy",1500)};
    try{navigator.clipboard.writeText(t).then(done,()=>sel(box))}catch(e){sel(box)}})});
function sel(box){const r=document.createRange();r.selectNodeContents($("code",box));const s=getSelection();s.removeAllRanges();s.addRange(r)}

/* ---------- Audio player ----------
   The artifact frame may block some ways of loading media. On load we probe, without playing:
   direct file URL, blob URL, data URL (all in an <audio> element), and Web Audio decoding.
   The first method that works becomes the engine. Results are saved to the page db ("diag")
   so problems on a phone can be diagnosed. */
const CH=window.CHAPTERS||[];
const P={i:Math.min(LS.get("ch",0),Math.max(0,CH.length-1)),mode:LS.get("mode","off"),rate:LS.get("rate",1),engine:null};
const bar=el("div",{class:"player",role:"region","aria-label":"Audio player"});
bar.innerHTML=`<div class="player-in"><button type="button" class="pbtn" id="p-play" aria-label="Play"></button>
<button type="button" class="pinfo" id="p-info" aria-label="Show chapters"><b id="p-title"></b><span class="prog"><i id="p-prog"></i></span><small id="p-msg" class="pmsg" hidden></small></button>
<div class="pctl"><button type="button" id="p-loop" title="Loop">Loop</button><button type="button" id="p-rate" title="Speed">1×</button></div></div>`;
document.body.append(bar);
const ICON={play:'<svg viewBox="0 0 16 16"><path d="M4 2l10 6-10 6z"/></svg>',pause:'<svg viewBox="0 0 16 16"><path d="M3 2h4v12H3zM9 2h4v12H9z"/></svg>'};
const fmtT=s=>{s=Math.round(s||0);return Math.floor(s/60)+":"+String(s%60).padStart(2,"0")};
function msg(t){const m=$("#p-msg");if(!m)return;m.textContent=t||"";m.hidden=!t}
const BLOB={}, BURL={}, DURL={}, BUF={};
const idx=i=>((i%CH.length)+CH.length)%CH.length;
async function getBlob(i){const c=CH[idx(i)];if(BLOB[c.id])return BLOB[c.id];const r=await fetch(c.src);if(!r.ok)throw new Error("HTTP "+r.status);
  const b=await r.blob();BLOB[c.id]=b.type?b:new Blob([b],{type:"audio/mpeg"});BURL[c.id]=URL.createObjectURL(BLOB[c.id]);return BLOB[c.id]}
async function getData(i){const c=CH[idx(i)];if(DURL[c.id])return DURL[c.id];const b=await getBlob(i);
  DURL[c.id]=await new Promise((ok,no)=>{const fr=new FileReader();fr.onload=()=>ok(String(fr.result).replace(/^data:[^;]*;/,"data:audio/mpeg;"));fr.onerror=no;fr.readAsDataURL(b)});return DURL[c.id]}
async function cacheOne(i){try{await getBlob(i);if(P.engine==="data")await getData(i);return true}catch(e){return false}}
function testEl(url){return new Promise(res=>{const a=new Audio();let done=false;const fin=r=>{if(done)return;done=true;a.removeAttribute("src");try{a.load()}catch(e){}res(r)};
  a.preload="metadata";a.addEventListener("loadedmetadata",()=>fin({ok:true,dur:Math.round(a.duration)}));
  a.addEventListener("error",()=>fin({ok:false,code:a.error&&a.error.code,m:a.error&&a.error.message||""}));setTimeout(()=>fin({ok:false,m:"timeout"}),8000);a.src=url;a.load()})}
let AC=null;
function ac(){if(!AC){const C=window.AudioContext||window.webkitAudioContext;AC=new C();try{if(navigator.audioSession)navigator.audioSession.type="playback"}catch(e){}}if(AC.state==="suspended")AC.resume();return AC}
async function probe(){const r={at:new Date().toISOString(),ua:navigator.userAgent.slice(0,160),audioSession:!!navigator.audioSession};
  try{await getBlob(0);r.fetch={ok:true,type:BLOB[CH[0].id].type,size:BLOB[CH[0].id].size}}catch(e){r.fetch={ok:false,m:String(e.message||e)}}
  r.direct=await testEl(CH[0].src);
  if(r.fetch.ok){r.blob=await testEl(BURL[CH[0].id]);try{r.data=await testEl(await getData(0))}catch(e){r.data={ok:false,m:String(e)}}
    try{const C=window.OfflineAudioContext||window.webkitOfflineAudioContext;const oc=new C(1,44100,44100);const ab=await BLOB[CH[0].id].arrayBuffer();
      const b=await new Promise((ok,no)=>oc.decodeAudioData(ab,ok,no));r.webaudio={ok:true,dur:Math.round(b.duration)}}catch(e){r.webaudio={ok:false,m:String(e&&e.message||e)}}}
  r.engine=r.direct.ok?"direct":(r.blob&&r.blob.ok)?"blob":(r.data&&r.data.ok)?"data":(r.webaudio&&r.webaudio.ok)?"wa":"none";
  window.AI4R_AUDIO=r;try{await capsReady;if(DB)DB.collection("diag").add(r).catch(()=>{})}catch(e){}
  return r}
/* Element engine */
const audio=document.createElement("audio");audio.preload="auto";audio.setAttribute("playsinline","");audio.hidden=true;document.body.append(audio);
/* Web Audio engine */
let src=null,startAt=0,offset=0,playingWA=false;
async function buf(i){const c=CH[idx(i)];if(BUF[c.id])return BUF[c.id];const b=await getBlob(i);const ab=await b.arrayBuffer();BUF[c.id]=await new Promise((ok,no)=>ac().decodeAudioData(ab,ok,no));return BUF[c.id]}
function waStop(keep){if(src){src.onended=null;try{src.stop()}catch(e){}src=null}if(keep&&playingWA)offset+=(AC.currentTime-startAt)*P.rate;playingWA=false}
async function waPlay(){const ctx=ac();if(!BUF[CH[P.i].id])msg("Loading…");try{const b=await buf(P.i);msg("");waStop(false);src=ctx.createBufferSource();src.buffer=b;src.playbackRate.value=P.rate;src.connect(ctx.destination);
  src.onended=()=>{playingWA=false;offset=0;ended()};startAt=ctx.currentTime;src.start(0,Math.min(offset,b.duration-0.05));playingWA=true;paint();buf(P.i+1).catch(()=>{})}catch(e){msg("Audio could not load ("+(e.message||e)+").");paint()}}
function isPlaying(){return P.engine==="wa"?playingWA:!audio.paused&&!audio.ended&&audio.readyState>2}
function curTime(){return P.engine==="wa"?(playingWA?offset+(AC.currentTime-startAt)*P.rate:offset):audio.currentTime}
function duration(){const c=CH[P.i];return P.engine==="wa"?(BUF[c.id]?BUF[c.id].duration:c.dur):(audio.duration||c.dur)}
function elSrc(i){const c=CH[idx(i)];return P.engine==="direct"?c.src:P.engine==="blob"?BURL[c.id]:DURL[c.id]}
function play(){if(!P.engine){msg("Checking how this device can play audio… tap again in a moment.");return}
  if(P.engine==="none"){msg("This view cannot play audio. Use “Save as one MP3” in the chapter list.");return}
  if(P.engine==="wa"){waPlay();return}
  const c=CH[P.i],u=elSrc(P.i);if(!u){msg("Loading…");cacheOne(P.i).then(()=>msg("Ready. Tap play."));return}
  if(audio.getAttribute("data-id")!==c.id){audio.src=u;audio.setAttribute("data-id",c.id)}
  audio.playbackRate=P.rate;audio.play().then(()=>{msg("");paint()}).catch(e=>{msg(e&&e.name==="NotAllowedError"?"Tap play to start.":"Could not play ("+(e&&e.name)+").");paint()});
  cacheOne(P.i+1)}
function pause(){if(P.engine==="wa"){waStop(true);paint()}else audio.pause()}
function load(i,go){if(P.engine==="wa")waStop(false);offset=0;P.i=idx(i);LS.set("ch",P.i);audio.removeAttribute("data-id");paint();
  if("mediaSession" in navigator){try{navigator.mediaSession.metadata=new MediaMetadata({title:CH[P.i].title,artist:"AI4Read",album:"Post 01 · What does an LLM know?"})}catch(e){}}
  if(go)play();else cacheOne(P.i)}
function ended(){if(P.mode==="one"){offset=0;if(P.engine!=="wa")audio.currentTime=0;play()}else if(P.i<CH.length-1)load(P.i+1,true);else if(P.mode==="all")load(0,true);else paint()}
function paint(){$("#p-title").textContent=`${P.i+1}/${CH.length} · ${CH[P.i].title}`;const on=isPlaying()||(P.engine!=="wa"&&!audio.paused);$("#p-play").innerHTML=on?ICON.pause:ICON.play;$("#p-play").setAttribute("aria-label",on?"Pause":"Play");
  const L={off:"Loop off",one:"Loop 1",all:"Loop all"}[P.mode];const lb=$("#p-loop");lb.textContent={off:"Loop",one:"Loop 1",all:"All"}[P.mode];lb.setAttribute("aria-label",L);lb.setAttribute("aria-pressed",String(P.mode!=="off"));
  $("#p-rate").textContent=P.rate+"×";}
if(CH.length){
  $("#p-play").addEventListener("click",()=>{if(P.engine==="wa")ac();(isPlaying()||(P.engine!=="wa"&&!audio.paused))?pause():play()});
  ["play","pause","playing","waiting"].forEach(ev=>audio.addEventListener(ev,paint));audio.addEventListener("ended",ended);
  audio.addEventListener("error",()=>{if(P.engine==="wa")return;msg("Audio error "+(audio.error&&audio.error.code)+". Switching to the backup player; tap play again.");P.engine="wa";paint()});
  setInterval(()=>{const d=duration();$("#p-prog").style.width=(d?Math.min(100,100*curTime()/d):0)+"%"},500);
  $("#p-loop").addEventListener("click",()=>{P.mode={off:"one",one:"all",all:"off"}[P.mode];LS.set("mode",P.mode);paint()});
  $("#p-rate").addEventListener("click",()=>{const R=[0.75,1,1.25,1.5];const was=isPlaying();if(P.engine==="wa"&&was)waStop(true);P.rate=R[(R.indexOf(P.rate)+1)%R.length];audio.playbackRate=P.rate;LS.set("rate",P.rate);if(P.engine==="wa"&&was)waPlay();paint()});
  $("#p-info").addEventListener("click",openChapters);
  if("mediaSession" in navigator){const ms=navigator.mediaSession;try{
    ms.setActionHandler("play",()=>play());ms.setActionHandler("pause",()=>pause());
    ms.setActionHandler("previoustrack",()=>load(P.i-1,true));ms.setActionHandler("nexttrack",()=>load(P.i+1,true));
    ms.setActionHandler("seekbackward",()=>{if(P.engine!=="wa")audio.currentTime=Math.max(0,audio.currentTime-15)});ms.setActionHandler("seekforward",()=>{if(P.engine!=="wa")audio.currentTime+=15});}catch(e){}}
  paint();
  probe().then(r=>{P.engine=r.engine;if(r.engine==="none")msg("This view cannot play audio here. Use “Save as one MP3” in the chapter list.");cacheOne(P.i)});
} else bar.hidden=true;

/* ---------- Sheets ---------- */
let scrim=null,sheet=null;
function openSheet(build){closeSheet();scrim=el("div",{class:"scrim"});sheet=el("div",{class:"sheet",role:"dialog","aria-modal":"true"});
  const inn=el("div",{class:"sheet-in"});sheet.append(inn);build(inn);document.body.append(scrim,sheet);scrim.addEventListener("click",closeSheet);
  const f=sheet.querySelector("textarea,button");if(f)f.focus();}
function closeSheet(){if(scrim)scrim.remove();if(sheet)sheet.remove();scrim=sheet=null}
document.addEventListener("keydown",e=>{if(e.key==="Escape")closeSheet()});
function openChapters(){openSheet(inn=>{inn.innerHTML=`<div class="sheet-h"><b>Chapters</b><button type="button" class="x">Close</button></div><p class="status">Loop 1 repeats one chapter; All repeats the whole post. The audio is written for listening, so it is shorter than the page and says formulas in words.</p>`;
  $(".x",inn).addEventListener("click",closeSheet);
  const off=el("div",{class:"row"});const bAll=el("button",{type:"button",class:"btn"},"Keep all audio for the train (12 MB)");off.append(bAll);
  const bSave=el("button",{type:"button",class:"btn ghost"},"Save as one MP3 to this device");if(DL)off.append(bSave);
  const st=el("p",{class:"status"},Object.keys(BLOB).length===CH.length?"All chapters are loaded. They keep playing without signal while this page stays open.":"Loading keeps every chapter in memory, so tunnels and weak signal do not stop playback. Keep this page open (closing it clears the memory).");
  inn.append(off,st);
  const D=window.AI4R_AUDIO;const dg=el("p",{class:"status"});
  dg.textContent=D?`Audio method on this device: ${D.engine}. Tests — file: ${D.direct.ok?"ok":"blocked"}, blob: ${D.blob&&D.blob.ok?"ok":"blocked"}, data: ${D.data&&D.data.ok?"ok":"blocked"}, Web Audio: ${D.webaudio&&D.webaudio.ok?"ok":"no"}.`:"Audio check still running…";
  inn.append(dg);
  bAll.addEventListener("click",async()=>{bAll.disabled=true;let ok=0;for(let i=0;i<CH.length;i++){st.textContent=`Loading chapter ${i+1} of ${CH.length}…`;if(await cacheOne(i))ok++}
    st.textContent=ok===CH.length?"All chapters are loaded. They keep playing without signal while this page stays open.":`Loaded ${ok} of ${CH.length} chapters. Try again when the signal is better.`;bAll.disabled=false});
  bSave.addEventListener("click",async()=>{bSave.disabled=true;st.textContent="Preparing the MP3…";
    try{const r=await fetch("audio/all.mp3");if(!r.ok)throw new Error("fetch");const b=await r.blob();const res=await DL.save({filename:"AI4Read-01-what-does-an-LLM-know.mp3",data:b});st.textContent=res&&res.status==="saved"?"Saved. Play it from your Files or music app, even offline.":"Sent to your device."}
    catch(e){st.textContent=(e&&e.code==="declined")?"Not saved.":(e&&e.code==="too_large")?"The file is too large to save from here.":"Could not save the file ("+((e&&(e.code||e.message))||"error")+")."}
    bSave.disabled=false});
  const list=el("div",{class:"chlist"});
  CH.forEach((c,i)=>{const b=el("button",{type:"button","aria-current":String(i===P.i)},`<b>${i+1}. ${c.title}</b><span>${fmtT(c.dur)}</span>`);b.addEventListener("click",()=>{load(i,true);closeSheet()});list.append(b)});inn.append(list)})}

/* ---------- Section tools: listen (notes are added by annotate.js) ---------- */
$$("section[data-ch]").forEach(sec=>{
  const tools=el("div",{class:"sec-tools"}); const ci=CH.findIndex(c=>c.id===sec.dataset.ch);
  if(ci>=0){const b=el("button",{type:"button"},`Listen · ${fmtT(CH[ci].dur)}`);b.addEventListener("click",()=>load(ci,true));tools.append(b)}
  sec.append(tools);
});
document.addEventListener("caps",()=>{});
})();
