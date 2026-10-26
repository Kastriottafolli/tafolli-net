/* Local presentation only. No tracking, automatic navigation or external requests. */
(() => {
 'use strict';
 const page=document.querySelector('body.detail-page');if(!page)return;
 const root=document.documentElement,reduced=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(hover: hover) and (pointer: fine)');
 const animations=new Set(),observers=[],cleanups=[],scenes=[...page.querySelectorAll('[data-detail-scene],[data-detail-static-scene],.detail-explorer-art')];
 const visible=new WeakMap();
 const paused=()=>reduced.matches||root.dataset.motion==='paused';
 function animate(target,keyframes,options){
  if(paused()||typeof target.animate!=='function')return;
  const item=target.animate(keyframes,options);animations.add(item);item.onfinish=()=>animations.delete(item);
 }
 function stop(){animations.forEach(item=>item.cancel());animations.clear();scenes.forEach(scene=>{scene.style.removeProperty('--detail-rx');scene.style.removeProperty('--detail-ry');});}
 function sync(){
  if(paused())stop();
  scenes.forEach(scene=>scene.dataset.motionState=document.hidden||paused()||visible.get(scene)===false?'off':'on');
 }
 page.querySelectorAll('[data-detail-scene]').forEach(scene=>{
  const buttons=[...scene.querySelectorAll('[data-detail-focus]')],notes=[...scene.querySelectorAll('[data-detail-note]')];
  buttons.forEach(button=>button.addEventListener('click',()=>{
   const selected=button.dataset.detailFocus;if(scene.dataset.focus===selected)return;
   scene.dataset.focus=selected;buttons.forEach(item=>item.setAttribute('aria-pressed',String(item===button)));notes.forEach(note=>note.hidden=note.dataset.detailNote!==selected);
   const note=notes.find(item=>item.dataset.detailNote===selected);
   if(note)animate(note,[{opacity:.25,transform:'translateY(4px)'},{opacity:1,transform:'translateY(0)'}],{duration:250,easing:'ease-out'});
  }));
  let frame=0,point=null;
  const reset=()=>{if(frame)cancelAnimationFrame(frame);frame=0;point=null;scene.style.removeProperty('--detail-rx');scene.style.removeProperty('--detail-ry');};
  scene.addEventListener('pointermove',event=>{
   if(paused()||!fine.matches||event.pointerType==='touch')return;
   point={x:event.clientX,y:event.clientY};if(frame)return;
   frame=requestAnimationFrame(()=>{frame=0;if(!point||paused())return;const b=scene.getBoundingClientRect();scene.style.setProperty('--detail-rx',(-((point.y-b.top)/b.height-.5)*4).toFixed(2)+'deg');scene.style.setProperty('--detail-ry',(((point.x-b.left)/b.width-.5)*6).toFixed(2)+'deg');});
  },{passive:true});
  scene.addEventListener('pointerleave',reset,{passive:true});cleanups.push(reset);
 });
 page.querySelectorAll('[data-detail-explorer]').forEach(explorer=>{
  const tabs=[...explorer.querySelectorAll('[role=tab]')],panels=[...explorer.querySelectorAll('[data-explorer-panel]')];
  if(!tabs.length||tabs.length!==panels.length)return;
  const select=(index,focus=false)=>{
   tabs.forEach((tab,i)=>{tab.setAttribute('aria-selected',String(i===index));tab.tabIndex=i===index?0:-1;});
   panels.forEach((panel,i)=>panel.hidden=i!==index);explorer.dataset.current=String(index);
   if(focus)tabs[index].focus();
   animate(panels[index],[{opacity:.3,transform:'translateY(5px)'},{opacity:1,transform:'translateY(0)'}],{duration:280,easing:'ease-out'});
  };
  tabs.forEach((tab,index)=>{
   tab.addEventListener('click',()=>select(index));
   tab.addEventListener('keydown',event=>{
    let next;if(event.key==='ArrowRight')next=(index+1)%tabs.length;if(event.key==='ArrowLeft')next=(index+tabs.length-1)%tabs.length;if(event.key==='Home')next=0;if(event.key==='End')next=tabs.length-1;
    if(next!==undefined){event.preventDefault();select(next,true);}
   });
  });
  explorer.dataset.enhanced='true';select(0);
 });
 if('IntersectionObserver' in window){
  const sceneObserver=new IntersectionObserver(entries=>{entries.forEach(entry=>visible.set(entry.target,entry.isIntersecting));sync();},{rootMargin:'100px'});scenes.forEach(scene=>sceneObserver.observe(scene));observers.push(sceneObserver);
  const reveal=new IntersectionObserver(entries=>{
   entries.forEach(entry=>{if(!entry.isIntersecting)return;reveal.unobserve(entry.target);animate(entry.target,[{opacity:.2,transform:'translateY(18px)'},{opacity:1,transform:'translateY(0)'}],{duration:550,easing:'cubic-bezier(.22,1,.36,1)'});});
  },{threshold:.06});
  page.querySelectorAll('.detail-route li,.detail-explorer,.detail-page .card,.tl-item,.mk-chapter,.partner-tile,.local-platforms article').forEach(target=>reveal.observe(target));observers.push(reveal);
  const links=[...page.querySelectorAll('[data-detail-chapter]')],targets=links.map(link=>document.getElementById(link.hash.slice(1))).filter(Boolean);
  if(targets.length){
   const chapters=new IntersectionObserver(entries=>{
    const current=entries.find(entry=>entry.isIntersecting);if(!current)return;
    links.forEach(link=>{if(link.hash.slice(1)===current.target.id)link.setAttribute('aria-current','true');else link.removeAttribute('aria-current');});
   },{rootMargin:'-130px 0px -60% 0px',threshold:0});targets.forEach(target=>chapters.observe(target));observers.push(chapters);
  }
 }
 const motionObserver=new MutationObserver(sync);motionObserver.observe(root,{attributes:true,attributeFilter:['data-motion']});
 reduced.addEventListener('change',sync);fine.addEventListener('change',stop);document.addEventListener('visibilitychange',sync);sync();
 window.addEventListener('pagehide',()=>{observers.forEach(observer=>observer.disconnect());motionObserver.disconnect();cleanups.forEach(cleanup=>cleanup());stop();},{once:true});
})();
