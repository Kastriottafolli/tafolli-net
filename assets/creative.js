/* Small, local interactions. All content and outbound links remain usable without them. */
(() => {
 'use strict';
 const reduce=matchMedia('(prefers-reduced-motion: reduce)');
 document.querySelectorAll('[data-project-viewer]').forEach(viewer=>{
  const screen=viewer.querySelector('[data-project-screen]');
  viewer.querySelectorAll('[data-project-pick]').forEach(button=>button.addEventListener('click',()=>{
   if(button.getAttribute('aria-pressed')==='true')return;
   viewer.querySelectorAll('[data-project-pick]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
   screen.src=button.dataset.src;screen.alt=button.dataset.name+' – Website';
   const link=viewer.querySelector('[data-project-visit]');link.href=button.dataset.url;
   viewer.querySelector('[data-project-name]').textContent=button.dataset.name;
   if(!reduce.matches&&typeof screen.animate==='function')screen.animate([{opacity:.2,transform:'scale(.985)'},{opacity:1,transform:'scale(1)'}],{duration:300,easing:'ease-out'});
  }));
 });
 const dialog=document.querySelector('.work-dialog');let opener=null;
 if(dialog&&typeof dialog.showModal==='function'){
  document.querySelectorAll('[data-work-open]').forEach(button=>button.addEventListener('click',()=>{
   opener=button;dialog.querySelector('h2').textContent=button.dataset.title;
   const img=dialog.querySelector('[data-work-full]');img.src=button.dataset.image;img.alt=button.dataset.title+' – Website';
   dialog.querySelector('[data-work-live]').href=button.dataset.url;
   dialog.showModal();
  }));
  dialog.querySelector('[data-work-close]').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{if(event.target===dialog){const b=dialog.getBoundingClientRect();if(event.clientX<b.left||event.clientX>b.right||event.clientY<b.top||event.clientY>b.bottom)dialog.close();}});
  dialog.addEventListener('close',()=>opener?.focus());
 }
 document.querySelectorAll('[data-flow]').forEach(section=>{
  section.querySelectorAll('[data-flow-tab]').forEach(button=>button.addEventListener('click',()=>{
   section.querySelectorAll('[data-flow-tab]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
   section.querySelectorAll('[data-flow-panel]').forEach(panel=>panel.hidden=panel.dataset.flowPanel!==button.dataset.flowTab);
  }));
 });
 const money=new Intl.NumberFormat('de-DE',{style:'currency',currency:'EUR',maximumFractionDigits:0});
 document.querySelectorAll('[data-mini-calc]').forEach(card=>{
  const revenue=card.querySelector('[data-calc-revenue]'),rate=card.querySelector('[data-calc-rate]');
  const set=(name,value)=>card.querySelector('[data-calc-'+name+']').textContent=value;
  const update=()=>{
   const r=Number(revenue.value),p=Number(rate.value),cost=r*p/100;
   set('revenue-label',money.format(r));set('rate-label',p+' %');set('cost',money.format(cost));set('left',money.format(r-cost));set('point',money.format(r/100));
   card.querySelector('[data-calc-bar]').style.width=p+'%';
  };
  revenue.addEventListener('input',update);rate.addEventListener('input',update);update();
 });
})();
(() => {
 'use strict';
 document.querySelectorAll('[data-goal-finder]').forEach(section=>{
  section.querySelectorAll('[data-goal-choice]').forEach(button=>button.addEventListener('click',()=>{
   section.querySelectorAll('[data-goal-choice]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
   section.querySelectorAll('[data-goal-panel]').forEach(panel=>panel.hidden=panel.dataset.goalPanel!==button.dataset.goalChoice);
  }));
 });
})();

(() => {
 document.querySelectorAll('[data-format-viewer]').forEach(section=>{
  section.querySelectorAll('[data-format-choice]').forEach(button=>button.addEventListener('click',()=>{
   section.querySelectorAll('[data-format-choice]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
   section.querySelectorAll('[data-format-panel]').forEach(panel=>panel.hidden=panel.dataset.formatPanel!==button.dataset.formatChoice);
  }));
 });
})();
