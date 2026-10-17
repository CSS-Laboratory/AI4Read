/* AI4Read post template: citation pop-overs and guess-first questions inside answers. */
/* ---- Citation popovers: tap or hover a citation to see the full reference, with Copy ---- */
(function(){
  const pop=document.createElement("div");pop.className="citepop";pop.setAttribute("role","dialog");pop.hidden=true;document.body.append(pop);
  let cur=null,hideT=null;
  function refText(key){const li=document.getElementById("src-"+key);return li?li.textContent.replace(/\s+/g," ").trim():""}
  function show(c){const key=c.dataset.src,t=refText(key);if(!t)return;cur=c;clearTimeout(hideT);
    pop.innerHTML=`<p class="cp-ref"></p><div class="cp-row"><button type="button" class="cp-copy">Copy</button><a class="cp-all" href="#src-${key}">In Sources</a></div>`;
    pop.querySelector(".cp-ref").textContent=t;
    pop.querySelector(".cp-copy").addEventListener("click",e=>{e.stopPropagation();const b=e.currentTarget;
      const ok=()=>{b.textContent="Copied";setTimeout(()=>b.textContent="Copy",1400)};
      try{navigator.clipboard.writeText(t).then(ok,()=>sel())}catch(err){sel()}
      function sel(){const r=document.createRange();r.selectNodeContents(pop.querySelector(".cp-ref"));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent="Selected: copy it"}});
    pop.querySelector(".cp-all").addEventListener("click",()=>{pop.hidden=true});
    pop.hidden=false;const r=c.getBoundingClientRect(),W=Math.min(360,window.innerWidth-24);pop.style.width=W+"px";
    let x=Math.max(12,Math.min(r.left+r.width/2-W/2,window.innerWidth-W-12));let y=r.bottom+8;
    pop.style.left=x+"px";pop.style.top=(y+window.scrollY)+"px";
    const ph=pop.getBoundingClientRect().height;if(y+ph>window.innerHeight-80)pop.style.top=(r.top-ph-8+window.scrollY)+"px";}
  function hide(){pop.hidden=true;cur=null}
  document.querySelectorAll(".cite[data-src]").forEach(c=>{
    c.addEventListener("click",e=>{e.stopPropagation();if(cur===c&&!pop.hidden)hide();else show(c)});
    c.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();show(c)}});
    c.addEventListener("mouseenter",()=>{if(matchMedia("(hover:hover)").matches)show(c)});
    c.addEventListener("mouseleave",()=>{if(matchMedia("(hover:hover)").matches)hideT=setTimeout(()=>{if(!pop.matches(":hover"))hide()},300)});});
  pop.addEventListener("mouseleave",()=>{if(matchMedia("(hover:hover)").matches)hideT=setTimeout(hide,300)});
  document.addEventListener("click",e=>{if(!pop.hidden&&!pop.contains(e.target))hide()});
  document.addEventListener("keydown",e=>{if(e.key==="Escape")hide()});
  window.addEventListener("scroll",()=>{if(!pop.hidden&&cur&&matchMedia("(hover:none)").matches){}},{passive:true});
})();

/* ---- Show each guess-first question at the top of its answer box ---- */
(function(){document.querySelectorAll(".reveal[data-for]").forEach(r=>{const q=document.querySelector(`.quiz[data-q="${r.dataset.for}"] .q`);if(!q)return;
  const p=document.createElement("p");p.className="reveal-q";p.textContent=q.textContent.replace(/\s+/g," ").trim();
  const h=r.querySelector(".reveal-h");h.after(p)})})();

