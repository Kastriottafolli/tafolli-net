/* Short page-entry signature. Native navigation and form submission stay native. */
(() => {
 'use strict';
 const root=document.documentElement,reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const timers=new Set(),animations=new Set();
 let phase=null,started=0,flight=null;
 const later=(fn,delay)=>{const id=setTimeout(()=>{timers.delete(id);fn();},delay);timers.add(id);};
 function finish(){
  timers.forEach(clearTimeout);timers.clear();animations.forEach(a=>a.cancel());animations.clear();
  flight?.remove();flight=null;phase=null;delete root.dataset.brandLoading;
 }
 const allowed=()=>!reduced.matches&&root.dataset.motion!=='paused'&&!document.hidden;
 function handoff(){
  if(phase!=='enter')return;
  const loader=document.getElementById('page-loader'),symbol=loader?.querySelector('.page-loader-symbol');
  const source=symbol?.querySelector('img'),target=document.querySelector('.site-header .tafolli-brand-mark');
  if(!loader||!symbol||!allowed()){finish();return;}
  if(typeof loader.animate!=='function'){finish();return;}
  const from=symbol.getBoundingClientRect(),to=target?.getBoundingClientRect();
  if(source?.naturalWidth&&to?.width&&from.width){
   flight=source.cloneNode();flight.className='page-loader-flight';flight.setAttribute('aria-hidden','true');
   Object.assign(flight.style,{left:from.left+'px',top:from.top+'px',width:from.width+'px',height:from.height+'px'});
   document.body.append(flight);
   const move=flight.animate([{transform:'translate(0,0) scale(1)',opacity:1},{transform:`translate(${to.left-from.left}px,${to.top-from.top}px) scale(${to.width/from.width})`,opacity:1}],{duration:430,easing:'cubic-bezier(.65,0,.2,1)',fill:'forwards'});
   animations.add(move);phase='handoff';root.dataset.brandLoading='handoff';
  }
  const fade=loader.animate([{opacity:1},{opacity:0}],{duration:430,easing:'ease-in-out',fill:'forwards'});
  animations.add(fade);fade.onfinish=finish;
  later(finish,500);
 }
 function scheduleHandoff(){if(phase==='enter')later(handoff,Math.max(0,680-(performance.now()-started)));}
 function enter(){
  finish();if(!allowed())return;
  phase='enter';started=performance.now();root.dataset.brandLoading='enter';
  later(finish,1700); // Independent escape hatch; no waiting on fonts, images or the network.
  if(document.readyState!=='loading')scheduleHandoff();
 }
 function leave(){
  finish();if(!allowed())return;
  phase='leave';root.dataset.brandLoading='leave';later(finish,3900);
 }
 // A synchronous head script enables the cover before the page's first paint.
 enter();
 document.addEventListener('DOMContentLoaded',scheduleHandoff,{once:true});
 document.addEventListener('click',event=>{
  if(event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
  const link=event.target instanceof Element?event.target.closest('a[href]'):null;
  if(!link||link.hasAttribute('download')||(link.target&&link.target!=='_self')||link.relList.contains('external'))return;
  let url;try{url=new URL(link.href,location.href);}catch{return;}
  if(url.origin!==location.origin||!/^https?:$/.test(url.protocol))return;
  if(/\.[^/]+$/.test(url.pathname)&&!url.pathname.endsWith('.html'))return;
  const key=u=>u.pathname.replace(/\/index\.html$/,'/')+u.search;
  if(url.hash&&key(url)===key(new URL(location.href)))return;
  // Let dialogs and other link handlers cancel the action before showing a cover.
  queueMicrotask(()=>{if(!event.defaultPrevented)leave();});
 });
 ['pointerdown','keydown','wheel','touchstart'].forEach(event=>window.addEventListener(event,finish,{passive:true,capture:true}));
 reduced.addEventListener('change',()=>{if(reduced.matches)finish();});
 new MutationObserver(()=>{if(root.dataset.motion==='paused')finish();}).observe(root,{attributes:true,attributeFilter:['data-motion']});
 document.addEventListener('visibilitychange',()=>{if(document.hidden)finish();});
 window.addEventListener('pagehide',finish);
 window.addEventListener('pageshow',event=>{if(event.persisted)enter();});
})();
