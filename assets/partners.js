/* Linked reference rails. Pause on hover, focus, touch, reduced motion or global pause. */
(() => {
 'use strict';
 const reduced=matchMedia('(prefers-reduced-motion:reduce)');
 document.querySelectorAll('[data-partner-slider]').forEach(section=>{
  const button=section.querySelector('.partner-slider-pause');
  const rails=[...section.querySelectorAll('.partner-slider-viewport')].map((viewport,index)=>{
   const track=viewport.querySelector('.partner-slider-track'),original=[...track.children];
   original.forEach(li=>{const clone=li.cloneNode(true);clone.dataset.clone='';clone.setAttribute('aria-hidden','true');clone.querySelectorAll('a').forEach(a=>a.tabIndex=-1);track.append(clone);});
   return {viewport,track,count:original.length,cycle:0,position:0,speed:index?.020:.025};
  });
  let paused=reduced.matches,hover=false,focus=false,touch=false,visible=false,frame=0,last=0;
  const globalPause=()=>document.documentElement.classList.contains('motion-paused')||document.documentElement.dataset.motion==='paused';
  const runs=()=>!paused&&!hover&&!focus&&!touch&&visible&&!document.hidden&&!globalPause();
  function measure(){rails.forEach(r=>r.cycle=r.track.children[r.count].offsetLeft-r.track.children[0].offsetLeft);}
  function tick(now){frame=0;if(!runs()){last=0;return;}if(last)rails.forEach(r=>{r.position+=Math.min(now-last,60)*r.speed;if(r.cycle&&r.position>=r.cycle)r.position-=r.cycle;r.viewport.scrollLeft=r.position;});last=now;frame=requestAnimationFrame(tick);}
  function sync(){
   const stopped=paused||globalPause();button.disabled=globalPause();button.setAttribute('aria-pressed',String(stopped));button.setAttribute('aria-label',section.dataset[stopped?'playLabel':'pauseLabel']);
   const icon=button.querySelector('use');if(icon)icon.setAttribute('href',icon.getAttribute('href').split('#')[0]+(stopped?'#play':'#pause'));
   if(runs()&&!frame){rails.forEach(r=>r.position=r.viewport.scrollLeft);frame=requestAnimationFrame(tick);}else if(!runs()&&frame){cancelAnimationFrame(frame);frame=0;last=0;}
  }
  button.hidden=false;button.addEventListener('click',()=>{paused=!paused;sync();});
  rails.forEach(r=>{
   r.viewport.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse'){hover=true;sync();}});
   r.viewport.addEventListener('pointerleave',()=>{hover=false;sync();});
   r.viewport.addEventListener('focusin',()=>{focus=true;sync();});
   r.viewport.addEventListener('focusout',()=>{focus=rails.some(r=>r.viewport.contains(document.activeElement));sync();});
   r.viewport.addEventListener('pointerdown',()=>{touch=true;sync();});
  });
  window.addEventListener('pointerup',()=>{touch=false;sync();},{passive:true});window.addEventListener('pointercancel',()=>{touch=false;sync();},{passive:true});
  document.addEventListener('visibilitychange',sync);reduced.addEventListener('change',()=>{paused=reduced.matches;sync();});
  const mutation=new MutationObserver(sync);mutation.observe(document.documentElement,{attributes:true,attributeFilter:['class','data-motion']});
  const intersection='IntersectionObserver'in window?new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;sync();}):null;if(intersection)intersection.observe(section);else visible=true;
  const resize='ResizeObserver'in window?new ResizeObserver(measure):null;rails.forEach(r=>resize?.observe(r.viewport));window.addEventListener('resize',measure,{passive:true});
  window.addEventListener('pagehide',()=>{cancelAnimationFrame(frame);frame=0;last=0;});
  window.addEventListener('pageshow',()=>{measure();sync();});measure();sync();
 });
})();
