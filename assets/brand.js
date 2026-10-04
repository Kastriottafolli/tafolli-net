/* A brief signature on every page entry. The page stays usable throughout. */
(() => {
  'use strict';
  const intro=document.querySelector('.brand-intro');
  if(!intro)return;
  const root=document.documentElement;
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  if(reduced.matches || root.classList.contains('motion-paused'))return;
  const source=intro.querySelector('img');
  let finished=false,flight=null,timers=[],animations=[];
  const interruptEvents=['pointerdown','keydown','wheel','touchstart'];
  function finish(){
    if(finished)return;finished=true;
    timers.forEach(clearTimeout);animations.forEach(a=>a.cancel());
    intro.hidden=true;flight?.remove();root.classList.remove('brand-intro-active');
    interruptEvents.forEach(event=>window.removeEventListener(event,finish));
    reduced.removeEventListener('change',motionChange);
    document.removeEventListener('visibilitychange',visibilityChange);
    window.removeEventListener('pagehide',finish);
    observer.disconnect();
  }
  function motionChange(){if(reduced.matches)finish();}
  function visibilityChange(){if(document.hidden)finish();}
  const observer=new MutationObserver(()=>{if(root.classList.contains('motion-paused'))finish();});
  async function start(){
    // Never wait on a slow asset, and never leave a loading screen behind.
    if(!source.complete){
      await Promise.race([source.decode().catch(()=>{}),new Promise(r=>setTimeout(r,250))]);
    }
    if(!source.naturalWidth || reduced.matches || document.hidden || root.classList.contains('motion-paused') || !intro.animate)return;
    intro.hidden=false;root.classList.add('brand-intro-active');
    interruptEvents.forEach(event=>window.addEventListener(event,finish,{passive:true}));
    reduced.addEventListener('change',motionChange);
    document.addEventListener('visibilitychange',visibilityChange);
    window.addEventListener('pagehide',finish,{once:true});
    observer.observe(root,{attributes:true,attributeFilter:['class']});
    timers.push(setTimeout(()=>{
      if(finished)return;
      const target=document.querySelector('.x-header .tafolli-brand-mark, .bar .tafolli-brand-mark');
      const symbol=intro.querySelector('.brand-intro-symbol');
      const from=symbol.getBoundingClientRect(),to=target?.getBoundingClientRect();
      if(to && to.width){
        flight=source.cloneNode();flight.className='brand-intro-flight';flight.setAttribute('aria-hidden','true');
        Object.assign(flight.style,{left:from.left+'px',top:from.top+'px',width:from.width+'px',height:from.height+'px'});
        document.body.append(flight);symbol.style.opacity='0';
        const move=flight.animate([
          {transform:'translate(0,0) scale(1)',opacity:1},
          {transform:`translate(${to.left-from.left}px,${to.top-from.top}px) scale(${to.width/from.width})`,opacity:1}
        ],{duration:650,easing:'cubic-bezier(.65,0,.2,1)',fill:'forwards'});
        animations.push(move);
      }
      const fade=intro.animate([{opacity:1},{opacity:0}],{duration:600,fill:'forwards',easing:'ease-in-out'});
      animations.push(fade);
    },1050));
    timers.push(setTimeout(finish,1800));
  }
  function play(){
    finish();
    finished=false;flight=null;timers=[];animations=[];
    intro.querySelector('.brand-intro-symbol').style.opacity='';
    start();
  }
  // Back/forward may restore the document without rerunning its scripts.
  window.addEventListener('pageshow',event=>{if(event.persisted)play();});
  play();
})();
