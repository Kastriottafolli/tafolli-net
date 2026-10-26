/* Motion is decorative: copy and links are present before JavaScript runs. */
(() => {
  'use strict';
  const root=document.documentElement;
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const fine=matchMedia('(hover: hover) and (pointer: fine)');
  const control=document.querySelector('[data-motion-toggle]');
  const scene=document.querySelector('[data-scene3d]');
  const cards=[...document.querySelectorAll('.c-service')];
  let userChoice=null,paused=reduced.matches;
  const animations=new Set();
  const visible=new WeakSet();
  let observer,sceneObserver,sceneVisible=true;
  function syncFloat(){const floater=scene?.querySelector('.d-float');if(floater)floater.style.animationPlayState=document.hidden||!sceneVisible||paused?'paused':'running';}
  function resetTransforms(){
    scene?.querySelector('.d-rig')?.style.removeProperty('--scene-rx');
    scene?.querySelector('.d-rig')?.style.removeProperty('--scene-ry');
    cards.forEach(card=>['--tilt-x','--tilt-y','--tilt-z'].forEach(key=>card.style.removeProperty(key)));
  }
  function sync(){
    paused=userChoice===null?reduced.matches:userChoice;
    root.dataset.motion=paused?'paused':'running';
    if(control){
      control.hidden=false;
      control.setAttribute('aria-pressed',String(paused));
      control.querySelector('span').textContent=paused?control.dataset.play:control.dataset.pause;
      control.querySelector('path').setAttribute('d',paused?'M5 3l8 5-8 5z':'M5 3v10M11 3v10');
    }
    if(paused){animations.forEach(a=>a.finish());animations.clear();resetTransforms();}
    syncFloat();
  }
  control?.addEventListener('click',()=>{userChoice=!paused;sync();});
  reduced.addEventListener('change',()=>{userChoice=null;sync();});
  fine.addEventListener('change',resetTransforms);
  sync();
  // Reveal once, using transform and opacity; no content is hidden in the source.
  const selectors='.c-services-section .c-section-heading,.c-service-copy,.c-technology .shell,.c-use-grid article,.c-process-grid article,.c-work .c-section-heading,.c-faq-grid,.c-contact .shell,.service-editorial,.service-modules,.region-grid';
  const targets=[...document.querySelectorAll(selectors)];
  if('IntersectionObserver' in window){
    observer=new IntersectionObserver(entries=>{
      entries.forEach(({isIntersecting,target})=>{
        if(!isIntersecting||visible.has(target))return;
        visible.add(target);observer.unobserve(target);
        if(paused||typeof target.animate!=='function')return;
        const animation=target.animate([{opacity:0,transform:'translate3d(0,22px,0)'},{opacity:1,transform:'translate3d(0,0,0)'}],{duration:620,easing:'cubic-bezier(.22,1,.36,1)'});
        animations.add(animation);animation.onfinish=()=>animations.delete(animation);
      });
    },{threshold:.08,rootMargin:'0px 0px 30px 0px'});
    targets.forEach(target=>observer.observe(target));
  }
  function pointerTilt(target,callback){
    let frame=0,point=null;
    target.addEventListener('pointermove',event=>{
      if(paused||!fine.matches||event.pointerType==='touch')return;
      point={x:event.clientX,y:event.clientY};
      if(frame)return;
      frame=requestAnimationFrame(()=>{
        frame=0;
        if(paused||!point)return;
        const box=target.getBoundingClientRect();
        callback((point.x-box.left)/box.width-.5,(point.y-box.top)/box.height-.5);
      });
    },{passive:true});
    target.addEventListener('pointerleave',()=>{if(frame)cancelAnimationFrame(frame);frame=0;point=null;resetTransforms();},{passive:true});
    window.addEventListener('pagehide',()=>{if(frame)cancelAnimationFrame(frame);},{once:true});
  }
  if(scene){
    const rig=scene.querySelector('.d-rig');
    if('IntersectionObserver' in window){sceneObserver=new IntersectionObserver(entries=>{sceneVisible=entries[0].isIntersecting;syncFloat();});sceneObserver.observe(scene);}
    pointerTilt(scene,(x,y)=>{rig.style.setProperty('--scene-rx',(-7-y*6).toFixed(2)+'deg');rig.style.setProperty('--scene-ry',(-10+x*14).toFixed(2)+'deg');});
  }
  cards.forEach(card=>pointerTilt(card,(x,y)=>{card.style.setProperty('--tilt-x',(-y*7).toFixed(2)+'deg');card.style.setProperty('--tilt-y',(x*9).toFixed(2)+'deg');card.style.setProperty('--tilt-z','14px');}));
  document.addEventListener('visibilitychange',()=>{
    syncFloat();
    if(document.hidden)resetTransforms();
  });
  window.addEventListener('pagehide',()=>{observer?.disconnect();sceneObserver?.disconnect();animations.forEach(a=>a.cancel());animations.clear();},{once:true});
})();
