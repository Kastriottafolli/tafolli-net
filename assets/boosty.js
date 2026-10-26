/* A contextual guide and a scroll-responsive scene. No remote service or tracking. */
(() => {
 'use strict';
 const root=document.documentElement,guide=document.querySelector('[data-boosty-guide]');
 const scene=document.querySelector('[data-boosty-scene]'),presence=scene?.closest('[data-presence]');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(hover:hover) and (pointer:fine)');
 const configElement=document.querySelector('#boosty-config');
 let config;try{config=configElement?JSON.parse(configElement.textContent):null;}catch{return;}
 let userPaused=false,minimized=false,sceneVisible=false,frame=0,lastDraw=0,pointerX=0,pointerY=0;
 try{const state=JSON.parse(sessionStorage.getItem('tafolli-boosty')||'{}');userPaused=state.paused===true;minimized=state.minimized===true;}catch{}
 const stopped=()=>reduced.matches||userPaused||root.dataset.motion==='paused';
 const store=()=>{try{sessionStorage.setItem('tafolli-boosty',JSON.stringify({paused:userPaused,minimized}));}catch{}};
 const launcher=guide?.querySelector('[data-guide-toggle]'),panel=guide?.querySelector('#boosty-panel');
 const restore=guide?.querySelector('[data-guide-show]'),pause=guide?.querySelector('[data-guide-pause]');
 let topic=config?.initial||'welcome';
 const topicForId={top:'welcome',marketing:'marketing',technology:'technology',consulting:'consulting',automation:'ai','tafolli-boost':'ai',ablauf:'consulting',kontakt:'contact',projektanfrage:'contact',marke:'marketing',kampagnen:'marketing',seo:'local',social:'social',print:'marketing',web:'website'};
 function setTopic(next){
  if(!config?.topics[next])return;
  topic=next;const [title,copy,href,label]=config.topics[topic];
  guide.querySelector('[data-guide-title]').textContent=title;
  guide.querySelector('[data-guide-copy]').textContent=copy;
  const link=guide.querySelector('[data-guide-link]');link.href=href;link.querySelector('[data-guide-link-label]').textContent=label;
  guide.dataset.topic=topic;
 }
 function openPanel(open,returnFocus=false){
  if(!panel)return;panel.hidden=!open;launcher.setAttribute('aria-expanded',String(open));
  if(open)panel.querySelector('[data-guide-close]').focus();else if(returnFocus)launcher.focus();
 }
 function sync(){
  root.dataset.boostyPaused=String(userPaused);
  if(guide){guide.dataset.minimized=String(minimized);restore.hidden=!minimized;guide.hidden=false;pause.setAttribute('aria-pressed',String(userPaused));pause.textContent=userPaused?config.play:config.pause;}
  if(stopped()){if(frame)cancelAnimationFrame(frame);frame=0;lastDraw=0;pointerX=0;pointerY=0;scene?.style.setProperty('--scene-x','0');scene?.style.setProperty('--scene-y','0');drawParticles(0);}
  requestUpdate();
  if(sceneVisible&&!stopped()&&!document.hidden&&!frame)frame=requestAnimationFrame(animate);
 }
 if(guide&&config){
  setTopic(topic);
  launcher.addEventListener('click',()=>openPanel(panel.hidden));
  guide.querySelector('[data-guide-close]').addEventListener('click',()=>openPanel(false,true));
  guide.querySelector('[data-guide-hide]').addEventListener('click',()=>{openPanel(false);minimized=true;store();sync();restore.focus();});
  restore.addEventListener('click',()=>{minimized=false;store();sync();launcher.focus();});
  pause.addEventListener('click',()=>{userPaused=!userPaused;store();sync();});
  document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!panel.hidden)openPanel(false,true);});
  document.addEventListener('click',event=>{if(!panel.hidden&&!guide.contains(event.target))openPanel(false);});
  document.addEventListener('focusin',event=>{guide.dataset.editing=String(event.target.matches('input,textarea,select,[contenteditable=true]'));});
 }
 const sections=[...document.querySelectorAll('[data-boosty-section],.c-hero,.c-service[id],.mk-chapter[id],#kontakt,#projektanfrage')];
 let updateFrame=0;
 function requestUpdate(){if(!updateFrame)updateFrame=requestAnimationFrame(update);}
 function update(){
  updateFrame=0;
  if(guide){
   let selected=config.initial||'welcome',best=-Infinity;
   sections.forEach(section=>{const box=section.getBoundingClientRect();if(box.top<innerHeight*.55&&box.bottom>innerHeight*.20&&box.top>best){const candidate=section.dataset.boostySection||topicForId[section.id];if(candidate){best=box.top;selected=candidate;}}});
   if(selected!==topic&&!guide.contains(document.activeElement))setTopic(selected);
   if(!stopped()&&!minimized){const progress=scrollY/Math.max(1,document.documentElement.scrollHeight-innerHeight);guide.style.setProperty('--guide-turn',(Math.sin(progress*Math.PI*5)*13).toFixed(2));guide.style.setProperty('--guide-rise',(Math.sin(progress*Math.PI*3)*7).toFixed(2));}
  }
  if(scene&&!stopped()){
   const b=scene.getBoundingClientRect(),travel=Math.max(-1,Math.min(1,(innerHeight*.5-(b.top+b.height*.5))/innerHeight));
   scene.style.setProperty('--scene-travel',travel.toFixed(3));scene.style.setProperty('--scene-spread',(Math.abs(travel)*.7).toFixed(3));
  }
 }
 document.addEventListener('scroll',requestUpdate,{passive:true});window.addEventListener('resize',requestUpdate,{passive:true});
 if(presence){
  presence.querySelectorAll('[data-presence-choice]').forEach(button=>button.addEventListener('click',()=>{
   const choice=button.dataset.presenceChoice;presence.dataset.presence=choice;presence.dataset.boostySection=choice;
   presence.querySelectorAll('[data-presence-choice]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));
   if(guide)setTopic(choice);drawParticles(performance.now());
  }));
  scene.addEventListener('pointermove',event=>{
   if(stopped()||!fine.matches||event.pointerType==='touch')return;
   const b=scene.getBoundingClientRect();pointerX=(event.clientX-b.left)/b.width-.5;pointerY=(event.clientY-b.top)/b.height-.5;
   scene.style.setProperty('--scene-x',pointerX.toFixed(3));scene.style.setProperty('--scene-y',pointerY.toFixed(3));
  },{passive:true});
  scene.addEventListener('pointerleave',()=>{pointerX=0;pointerY=0;scene.style.setProperty('--scene-x','0');scene.style.setProperty('--scene-y','0');});
 }
 const canvas=scene?.querySelector('canvas');let ctx=null,width=0,height=0;
 try{ctx=canvas?.getContext('2d',{alpha:true});}catch{}
 // The same small point cloud rearranges between an orbit, a helix and a map route.
 let socialBlend=0,localBlend=0;
 const count=150,points=Array.from({length:count},(_,i)=>({angle:i/count*Math.PI*2,band:i%3,seed:Math.sin(i*127.1)*.5+.5}));
 function resize(){
  if(!ctx)return;const rect=scene.getBoundingClientRect();width=rect.width;height=rect.height;const ratio=Math.min(devicePixelRatio||1,1.5);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);ctx.setTransform(ratio,0,0,ratio,0,0);drawParticles(0);
 }
 function drawParticles(time){
  if(!ctx||!width)return;ctx.clearRect(0,0,width,height);
  const t=stopped()?0:time*.00009,kind=presence.dataset.presence,scale=Math.min(width/900,1),radius=210*scale;
  socialBlend+=((kind==='social'?1:0)-socialBlend)*(stopped()?1:.11);localBlend+=((kind==='local'?1:0)-localBlend)*(stopped()?1:.11);
  const plotted=points.map(p=>{
   const a=p.angle+t,band=p.band;
   let x=Math.cos(a)*radius*(1+band*.13),y=Math.sin(a)*60*scale,z=Math.sin(a)*radius*.6;
   const orbitBlend=1-socialBlend-localBlend;
   x=x*orbitBlend+Math.cos(a)*radius*.8*socialBlend+(p.angle/Math.PI-1)*radius*1.35*localBlend;
   y=y*orbitBlend+((p.angle/Math.PI-1)*110*scale+Math.sin(a*3+t)*14)*socialBlend+Math.sin(p.angle*2+t)*55*scale*localBlend;
   z=z*orbitBlend+Math.sin(a)*radius*.6*socialBlend+Math.cos(p.angle)*radius*.45*localBlend;
   const rx=x*Math.cos(.23+pointerX*.2)-z*Math.sin(.23+pointerX*.2),rz=x*Math.sin(.23+pointerX*.2)+z*Math.cos(.23+pointerX*.2),perspective=650/(650+rz);
   return {x:width*.5+rx*perspective,y:height*.51+y*perspective+rz*.24+pointerY*5,z:rz,r:(.65+p.seed*.7)*perspective,alpha:.17+(1-rz/(radius||1))*.17};
  }).sort((a,b)=>b.z-a.z);
  for(const p of plotted){ctx.fillStyle='rgba(49,110,211,'+p.alpha.toFixed(3)+')';ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();}
 }
 function animate(time){
  frame=0;if(stopped()||!sceneVisible||document.hidden)return;
  if(time-lastDraw>32){drawParticles(time);lastDraw=time;}frame=requestAnimationFrame(animate);
 }
 let intersection;
 if(scene){
  resize();if('ResizeObserver'in window)new ResizeObserver(resize).observe(scene);
  if('IntersectionObserver'in window){intersection=new IntersectionObserver(entries=>{sceneVisible=entries[0].isIntersecting;presence.dataset.sceneVisible=String(sceneVisible);if(guide)guide.dataset.inScene=String(entries[0].intersectionRatio>.3);if(sceneVisible)sync();else{cancelAnimationFrame(frame);frame=0;lastDraw=0;}},{threshold:[0,.3]});intersection.observe(scene);}else sceneVisible=true;
 }
 const planner=document.querySelector('[data-planner]');
 if(guide&&planner&&'IntersectionObserver'in window)new IntersectionObserver(entries=>{guide.dataset.inPlanner=String(entries[0].isIntersecting);}).observe(planner);
 reduced.addEventListener('change',sync);
 const observer=new MutationObserver(sync);observer.observe(root,{attributes:true,attributeFilter:['data-motion']});
 document.addEventListener('visibilitychange',()=>{root.dataset.boostyBackground=String(document.hidden);if(document.hidden){cancelAnimationFrame(frame);frame=0;}else sync();});
 window.addEventListener('pagehide',()=>{cancelAnimationFrame(frame);cancelAnimationFrame(updateFrame);frame=0;updateFrame=0;lastDraw=0;});
 window.addEventListener('pageshow',()=>{resize();sync();});
 sync();
})();
