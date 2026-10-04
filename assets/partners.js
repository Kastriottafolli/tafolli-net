/* A small logo rail: native horizontal scrolling, local images, accessible pause. */
(() => {
  'use strict';
  const reduced=matchMedia('(prefers-reduced-motion:reduce)');
  document.querySelectorAll('[data-partner-slider]').forEach(section=> {
    const viewport=section.querySelector('.partner-slider-viewport');
    const track=section.querySelector('.partner-slider-track');
    const button=section.querySelector('.partner-slider-pause');
    let paused=reduced.matches, hovering=false, focused=false, touching=false, visible=false;
    let frame=0,last=0,cycle=0,position=0;
    // Repeated logos stay clickable but create no duplicate tab stops or announcements.
    const original=[...track.children];
    original.forEach(li=> { const clone=li.cloneNode(true);clone.dataset.clone='';clone.setAttribute('aria-hidden','true');clone.querySelector('a').tabIndex=-1;track.append(clone); });
    function measure(){cycle=track.children[original.length].offsetLeft-track.children[0].offsetLeft;}
    function shouldRun(){return !paused && !hovering && !focused && !touching && visible && !document.hidden && !document.documentElement.classList.contains('motion-paused');}
    function tick(now){
      frame=0;
      if(!shouldRun()){last=0;return;}
      if(last){position+=Math.min(now-last,60)*.022;if(cycle && position>=cycle)position-=cycle;viewport.scrollLeft=position;}
      last=now;frame=requestAnimationFrame(tick);
    }
    function sync(){
      const globalPaused=document.documentElement.classList.contains('motion-paused');
      const stopped=paused||globalPaused;button.disabled=globalPaused;
      button.setAttribute('aria-pressed',String(stopped));button.setAttribute('aria-label',section.dataset[stopped?'playLabel':'pauseLabel']);button.querySelector('span').textContent=stopped?'▷':'Ⅱ';
      if(shouldRun()&&!frame){position=viewport.scrollLeft;frame=requestAnimationFrame(tick);}
      else if(!shouldRun()&&frame){cancelAnimationFrame(frame);frame=0;last=0;}
    }
    button.hidden=false;
    button.addEventListener('click',()=>{paused=!paused;sync();});
    viewport.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse'){hovering=true;sync();}});
    viewport.addEventListener('pointerleave',()=>{hovering=false;sync();});
    viewport.addEventListener('focusin',()=>{focused=true;sync();});
    viewport.addEventListener('focusout',()=>{focused=viewport.contains(document.activeElement);sync();});
    viewport.addEventListener('pointerdown',()=>{touching=true;sync();});
    window.addEventListener('pointerup',()=>{touching=false;sync();},{passive:true});
    window.addEventListener('pointercancel',()=>{touching=false;sync();},{passive:true});
    document.addEventListener('visibilitychange',sync);
    reduced.addEventListener('change',()=>{paused=reduced.matches;sync();});
    new MutationObserver(sync).observe(document.documentElement,{attributes:true,attributeFilter:['class']});
    if('IntersectionObserver'in window)new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;sync();}).observe(section);
    else visible=true;
    if('ResizeObserver'in window)new ResizeObserver(measure).observe(viewport);
    window.addEventListener('resize',measure,{passive:true});
    measure();sync();
  });
})();
