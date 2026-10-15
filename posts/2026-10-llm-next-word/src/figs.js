/* Illustrations and extra labs for post 01 (toy numbers are ours unless stated). */
(function(){
"use strict";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const NS="http://www.w3.org/2000/svg";
const esc=t=>String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;");
const svg=(w,h,body,label)=>`<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="${esc(label||"")}" class="fig">${body}</svg>`;
const txt=(x,y,t,o={})=>`<text x="${x}" y="${y}" text-anchor="${o.a||"middle"}" class="${o.c||"t"}"${o.s?` font-size="${o.s}"`:""}>${esc(t)}</text>`;
const box=(x,y,w,h,c="bx",r=4)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" class="${c}"/>`;
const arrow=(x1,y1,x2,y2,c="ar")=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${c}" marker-end="url(#ah)"/>`;
const DEFS=`<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ahd"/></marker></defs>`;

/* ---- Prediction 3: in vs on (Ullman 2023, p. 6) ---- */
(function(){const host=$("#fig-inon");if(!host)return;
  const cat=(x,y,vis)=>`<g class="${vis?"cat":"cat ghost"}"><ellipse cx="${x}" cy="${y}" rx="15" ry="10"/><circle cx="${x+13}" cy="${y-9}" r="7"/><path d="M${x+8} ${y-14}l2-7 4 5zM${x+15} ${y-15}l4-6 2 7z"/><path d="M${x-15} ${y}q-10 -8 -6 -18" fill="none"/></g>`;
  const panel=(ox,title,inside,thought,ok)=>{let g=`<g transform="translate(${ox},0)">`+txt(85,16,title,{c:"th"});
    g+=box(14,92,58,40,"basket",6)+txt(43,148,"basket",{c:"ts"});
    g+=box(98,92,58,40,"crate",2)+txt(127,148,"box",{c:"ts"});
    g+=inside?cat(127,114,false)+`<line x1="98" y1="92" x2="156" y2="92" class="lid"/>`:cat(124,80,true);
    g+=`<g class="john"><circle cx="16" cy="44" r="7"/><line x1="16" y1="51" x2="16" y2="70"/><line x1="16" y1="70" x2="9" y2="84"/><line x1="16" y1="70" x2="23" y2="84"/><line x1="7" y1="58" x2="25" y2="58"/></g>`+txt(16,30,"John",{c:"ts"});
    g+=`<path d="M38 34 h84 a6 6 0 0 1 6 6 v18 a6 6 0 0 1 -6 6 h-80 l-6 7 v-7 a6 6 0 0 1 -4 -6 v-18 a6 6 0 0 1 6 -6z" class="bubble"/>`+txt(80,52,thought,{s:11})+txt(80,176,ok,{c:"tn"});
    return g+"</g>"};
  host.innerHTML=svg(360,190,DEFS+panel(0,"Original: cat IN the box",true,"in the basket","hidden: false belief")+panel(185,"Altered: cat ON the box",false,"on the box","visible: he should know"),"In versus on");
})();

/* ---- Step 3: toy word map ---- */
(function(){const host=$("#fig-wordmap");if(!host)return;
  const P=[["cat",62,150],["dog",92,132],["walking",150,58],["running",184,46],["bedroom",268,150],["room",292,128],["the",204,170],["in",40,60]];
  let b=`<line x1="20" y1="190" x2="340" y2="190" class="ax"/><line x1="20" y1="190" x2="20" y2="14" class="ax"/>`+txt(330,184,"direction 1",{a:"end",c:"ts"})+txt(26,24,"direction 2",{a:"start",c:"ts"});
  [["cat","dog"],["walking","running"],["bedroom","room"]].forEach(([a,c])=>{const A=P.find(p=>p[0]===a),C=P.find(p=>p[0]===c);b+=`<ellipse cx="${(A[1]+C[1])/2}" cy="${(A[2]+C[2])/2}" rx="44" ry="26" class="halo"/>`});
  P.forEach(([w,x,y])=>{b+=`<circle cx="${x}" cy="${y}" r="4" class="dot"/>`+txt(x+7,y-7,w,{a:"start"})});
  host.innerHTML=svg(360,200,b,"Toy word map")+`<figcaption>A toy map with two directions (real vectors have 30 to 100 or more). Neighbours share what the model learns about each other. Positions are ours, for illustration.</figcaption>`;
})();

/* ---- Lens 1: question tree for the weather ---- */
(function(){const host=$("#fig-qtree");if(!host)return;
  let b=DEFS;
  const q=(x,y,t)=>box(x-38,y-14,76,28,"bx",14)+txt(x,y+5,t);
  const leaf=(x,y,w,n,p)=>box(x-34,y-14,68,28,"leaf",4)+txt(x,y+1,w,{s:12})+txt(x,y+26,`${n} q · ${p}`,{c:"ts"});
  b+=q(60,30,"rain?")+arrow(60,44,60,82)+txt(66,66,"yes",{a:"start",c:"ts"})+leaf(60,98,"rain",1,"½");
  b+=arrow(98,30,150,30)+txt(124,24,"no",{c:"ts"})+q(188,30,"sun?")+arrow(188,44,188,82)+txt(194,66,"yes",{a:"start",c:"ts"})+leaf(188,98,"sun",2,"¼");
  b+=arrow(226,30,268,30)+txt(247,24,"no",{c:"ts"})+q(306,30,"wind?")+arrow(296,44,268,82)+arrow(316,44,340,82)+txt(272,64,"yes",{a:"end",c:"ts"})+txt(338,64,"no",{a:"start",c:"ts"});
  b+=leaf(262,98,"wind",3,"⅛")+leaf(336,98,"snow",3,"⅛");
  host.innerHTML=svg(380,140,b,"Question tree")+`<figcaption>Ask about the most likely word first. Average number of questions: ½·1 + ¼·2 + ⅛·3 + ⅛·3 = 1.75.</figcaption>`;
})();

/* ---- Step 4: three architectures (cost formulas: Mikolov et al. 2013a, pp. 3–4) ---- */
(function(){const host=$("#arch-svg");if(!host)return;const read=$("#arch-read");
  const fmt=n=>n.toLocaleString("en-US");
  const D=500,H=500,V=1e6,LV=20; // our example sizes; log2(10^6) ≈ 20
  function draw(m){let b=DEFS;const W=360;
    const word=(x,y,t,c="wd")=>box(x-28,y-12,56,24,c,12)+txt(x,y+4,t,{s:11});
    if(m==="nnlm"){const xs=[70,180,290],lab=["w(t−3)","w(t−2)","w(t−1)"];
      xs.forEach((x,i)=>{b+=word(x,232,lab[i])+arrow(x,219,x,196)+box(x-30,170,60,24,"emb")+txt(x,186,"vector C",{s:10})+arrow(x,169,180,146)});
      b+=box(80,118,200,26,"hid")+txt(180,135,"hidden layer: H units, tanh",{s:11})+arrow(180,117,180,94);
      b+=box(80,66,200,26,"out")+txt(180,83,"softmax: a probability for each of V words",{s:11})+arrow(180,65,180,44)+word(180,30,"w(t)","wt");
      b+=txt(W-6,140,"N×D×H",{a:"end",c:"tn"});}
    else if(m==="cbow"){const xs=[48,128,232,312],lab=["w(t−2)","w(t−1)","w(t+1)","w(t+2)"];
      xs.forEach((x,i)=>{b+=word(x,232,lab[i])+arrow(x,219,x,196)+box(x-30,170,60,24,"emb")+txt(x,186,"vector C",{s:10})+arrow(x,169,180,146)});
      b+=box(100,120,160,24,"avg")+txt(180,136,"average the vectors",{s:11});
      b+=box(80,92,200,22,"gone")+txt(180,107,"hidden layer removed",{s:10,c:"tgone"})+arrow(180,119,180,72);
      b+=box(80,46,200,26,"out")+txt(180,63,"word tree (≈ log₂V outputs)",{s:11})+arrow(180,45,180,30)+word(180,16,"w(t)","wt");}
    else{const xs=[48,128,232,312],lab=["w(t−2)","w(t−1)","w(t+1)","w(t+2)"];
      b+=word(180,232,"w(t)","wt")+arrow(180,219,180,196)+box(150,170,60,24,"emb")+txt(180,186,"vector C",{s:10});
      b+=box(80,128,200,22,"gone")+txt(180,143,"hidden layer removed",{s:10,c:"tgone"});
      b+=arrow(180,169,180,104)+box(80,78,200,26,"out")+txt(180,95,"word tree, once per neighbour",{s:11});
      xs.forEach((x,i)=>{b+=arrow(180,77,x,46)+word(x,30,lab[i])});}
    host.innerHTML=svg(W,250,b,"Model diagram");
    const nn=10*D+10*D*H+H*V, nnT=10*D+10*D*H+H*LV, cb=8*D+D*LV, sg=5*(D+D*LV);
    read.textContent={nnlm:`Bengio-style network, N = 10 previous words (the diagram draws 3), D = H = 500, V = 1,000,000 (our example sizes):\ncost ≈ N·D + N·D·H + H·V = ${fmt(nn)} operations per example (parameters touched).\nWith a word tree at the output (H·log₂V): ${fmt(nnT)} — now the hidden layer (2,500,000) is almost all of it.`,
      cbow:`CBOW, 8 context words (4 before, 4 after; the diagram draws 4), D = 500, word tree:\ncost ≈ N·D + D·log₂V = ${fmt(cb)} per example — about ${Math.round(nnT/cb)}× cheaper than the network with a word tree.`,
      sg:`Skip-gram, neighbours up to C = 5 away, D = 500, word tree:\ncost ≈ C·(D + D·log₂V) = ${fmt(sg)} per example.`}[m];}
  read.style.whiteSpace="pre-line";
  $$("#lab-arch .seg button").forEach(b=>b.addEventListener("click",()=>{$$("#lab-arch .seg button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));draw(b.dataset.m)}));
  draw("nnlm");
})();

/* ---- Step 5: who looks at whom (toy vectors) ---- */
(function(){const host=$("#sent-toks");if(!host)return;const bars=$("#sent-bars"),read=$("#sent-read");
  const T=["Alice","was","friends","with","Bob",".","Alice","went","to","visit","her","friend"];
  // features: person, female, male, friendship, travel, grammar word
  const K={Alice:[1,1,0,0,0,0],was:[0,0,0,0,0,1],friends:[0,0,0,1,0,0],with:[0,0,0,0.3,0,1],Bob:[1,0,1,1,0,0],".":[0,0,0,0,0,0.5],went:[0,0,0,0,1,0],to:[0,0,0,0,0.3,1],visit:[0,0,0,0.5,1,0],her:[0.5,1,0,0,0,0],friend:[0.5,0,0,1,0,0]};
  const Q={her:[2,2,0,0,0,0],friend:[1.5,0,0,2,0,0],visit:[0.5,0,0,0,2,0],went:[1,0,0,0,0,0]};
  let sel=11;
  const btns=T.map((w,i)=>{const b=document.createElement("button");b.type="button";b.textContent=w;b.addEventListener("click",()=>{sel=i;upd()});host.append(b);return b});
  function upd(){const t=T[sel],q=Q[t]||K[t];
    const s=T.slice(0,sel+1).map(w=>2*K[w].reduce((a,v,j)=>a+v*q[j],0)/Math.sqrt(6)),m=Math.max(...s),e=s.map(x=>Math.exp(x-m)),z=e.reduce((a,b)=>a+b,0),w=e.map(x=>x/z);
    btns.forEach((b,i)=>{b.setAttribute("aria-pressed",String(i===sel));b.disabled=false;b.style.background=i<=sel?`color-mix(in srgb,var(--stamp) ${Math.round((i===sel?0:w[i])*90)}%,var(--paper))`:"";b.classList.toggle("future",i>sel)});
    bars.innerHTML=T.slice(0,sel+1).map((x,i)=>`<div><span>${i+1}. ${esc(x)}</span><i style="width:${w[i]*100}%"></i><span>${w[i].toFixed(2)}</span></div>`).join("");
    const top=w.map((v,i)=>[v,i]).sort((a,b)=>b[0]-a[0])[0];
    read.textContent=`“${t}” gives its largest weight (${top[0].toFixed(2)}) to word ${top[1]+1}, “${T[top[1]]}”. Later words are masked: “${t}” cannot see them.`;}
  upd();
})();

/* ---- Step 8: Kaplan's fitted line L(N) = (8.8e13/N)^0.076 (Kaplan et al. 2020, p. 4) ---- */
(function(){const host=$("#scale-chart");if(!host)return;const sl=$("#scale-sliders"),read=$("#scale-read");
  const L=n=>Math.pow(8.8e13/n,0.076);const lo=4,hi=10;
  const row=document.createElement("div");row.className="sl";row.innerHTML=`<label for="sN">parameters</label><input type="range" id="sN" min="${lo}" max="${hi}" step="0.1" value="6"><output for="sN"></output>`;sl.append(row);
  const inp=$("#sN",row),out=$("output",row);
  const W=340,H=170,X0=40,Y0=150,X1=318,Y1=12,ymin=1.5,ymax=6;
  const x=v=>X0+(v-lo)/(hi-lo)*(X1-X0),y=l=>Y0-(Math.log10(l)-Math.log10(ymin))/(Math.log10(ymax)-Math.log10(ymin))*(Y0-Y1);
  const fmtN=n=>n>=1e9?(n/1e9).toFixed(n>=1e10?0:1)+" billion":n>=1e6?(n/1e6).toFixed(n>=1e7?0:1)+" million":Math.round(n/1e3)+" thousand";
  function upd(){const v=+inp.value,n=Math.pow(10,v),l=L(n);out.textContent=fmtN(n).replace(" billion","B").replace(" million","M").replace(" thousand","k");
    let b=`<line x1="${X0}" y1="${Y0}" x2="${X1}" y2="${Y0}" class="ax"/><line x1="${X0}" y1="${Y0}" x2="${X0}" y2="${Y1}" class="ax"/>`;
    for(let k=lo;k<=hi;k+=2)b+=`<line x1="${x(k)}" y1="${Y0}" x2="${x(k)}" y2="${Y0+4}" class="ax"/>`+txt(x(k),Y0+16,"10"+String(k).split("").map(d=>"⁰¹²³⁴⁵⁶⁷⁸⁹"[+d]).join(""),{c:"ts"});
    [2,3,4,5,6].forEach(l=>{b+=`<line x1="${X0}" y1="${y(l)}" x2="${X1}" y2="${y(l)}" class="grid"/>`+txt(X0-5,y(l)+4,l,{a:"end",c:"ts"})});
    b+=`<line x1="${x(lo)}" y1="${y(L(1e4))}" x2="${x(hi)}" y2="${y(L(1e10))}" class="fitl"/>`+`<circle cx="${x(v)}" cy="${y(l)}" r="5" class="fitd"/>`;
    b+=txt(X1,Y1+8,"loss (nats/token), log scale",{a:"end",c:"ts"});
    host.innerHTML=svg(W,H+4,b,"Kaplan power law on log-log axes");
    read.textContent=`N = ${fmtN(n)} parameters → L = ${l.toFixed(2)} nats per token (${(l/Math.LN2).toFixed(2)} bits).\nHalf as many parameters: ${L(n/2).toFixed(2)}. Twice as many: ${L(2*n).toFixed(2)} — ×${(L(2*n)/l).toFixed(3)} per doubling, at every size.`;}
  read.style.whiteSpace="pre-line";inp.addEventListener("input",upd);upd();
})();

/* ---- Lens 1: 32 cups, 5 rats ---- */
(function(){const grid=$("#cups-grid");if(!grid)return;const ratsH=$("#cups-rats"),read=$("#cups-read");
  let poison=21,rat=-1;const bin=n=>n.toString(2).padStart(5,"0");
  const cups=[...Array(32)].map((_,i)=>{const b=document.createElement("button");b.type="button";b.innerHTML=`<b>${i}</b><span>${bin(i)}</span>`;b.addEventListener("click",()=>{poison=i;rat=-1;upd()});grid.append(b);return b});
  const rats=[...Array(5)].map((_,r)=>{const b=document.createElement("button");b.type="button";b.addEventListener("click",()=>{rat=rat===r?-1:r;upd()});ratsH.append(b);return b});
  function upd(){const pb=bin(poison);
    cups.forEach((b,i)=>{b.classList.toggle("poison",i===poison);b.classList.toggle("drinks",rat>=0&&bin(i)[rat]==="1")});
    rats.forEach((b,r)=>{const dead=pb[r]==="1";b.className=dead?"dead":"alive";b.setAttribute("aria-pressed",String(r===rat));b.innerHTML=`Rat ${r+1}<small>digit ${r+1} · ${dead?"dies → 1":"lives → 0"}</small>`});
    const dead=[...pb].map((d,r)=>d==="1"?r+1:0).filter(Boolean);
    read.textContent=(rat>=0?`Rat ${rat+1} drinks from the 16 highlighted cups (digit ${rat+1} is 1).\n`:"")+`Poison in cup ${poison} = ${pb} in binary. Dead rats: ${dead.length?dead.join(", "):"none"} → read 1 for dead, 0 for alive → ${pb} → cup ${poison}.`;}
  read.style.whiteSpace="pre-line";upd();
})();
})();
