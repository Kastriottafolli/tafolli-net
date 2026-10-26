import {calculate,scaling,defaults,catalog} from './planner-model.mjs?v=fd5c59e2a3';
import {deliverInquiry} from './form-delivery.mjs?v=90b48f7a37';

document.querySelectorAll('[data-planner]').forEach(section=>{
 'use strict';
 const config=JSON.parse(section.querySelector('[data-planner-config]').textContent),L=config.labels;
 const locale={de:'de-DE',en:'en-GB',sq:'sq-AL'}[config.lang]||'de-DE';
 const number=new Intl.NumberFormat(locale,{maximumFractionDigits:0});
 const euro=new Intl.NumberFormat(locale,{style:'currency',currency:'EUR',maximumFractionDigits:0});
 const decimal=new Intl.NumberFormat(locale,{maximumFractionDigits:2});
 const reduce=matchMedia('(prefers-reduced-motion:reduce)');
 const serviceKeys=['website','social','seo','local','ads'];
 const assumptions=['baseVisitors','socialViews','socialCtr','seoVisits','localViews','localCtr','cpc','adCtr','baseCvr','targetCvr','closeRate'];
 const range=section.querySelector('[data-plan-ad-range]'),form=section.querySelector('[data-plan-form]');
 const status=section.querySelector('[data-plan-status]'),submit=form.querySelector('[type=submit]');
 let result,summary='',updateFrame=0,animation=null,liveTimer=0,initialized=false;
 const motionButton=section.querySelector('[data-plan-motion]');
 function syncMotion(){
  const paused=section.dataset.planMotionState==='paused';
  motionButton.setAttribute('aria-pressed',String(paused||reduce.matches));
  motionButton.disabled=reduce.matches;
  motionButton.querySelector('span').textContent=reduce.matches?L.reduced:(paused?L.play:L.pause);
  if(paused||reduce.matches)animation?.cancel();
 }
 motionButton.addEventListener('click',()=>{section.dataset.planMotionState=section.dataset.planMotionState==='paused'?'running':'paused';syncMotion();});
 reduce.addEventListener('change',syncMotion);syncMotion();
 const observer=new IntersectionObserver(entries=>{section.dataset.planVisible=String(entries[0].isIntersecting);},{rootMargin:'100px'});observer.observe(section);
 function read(){
  return {websiteType:section.querySelector('[data-plan-type]:checked').value,active:Object.fromEntries(serviceKeys.map(key=>[key,section.querySelector('[data-plan-active="'+key+'"]').checked])),values:Object.fromEntries(Object.keys(defaults).map(key=>[key,section.querySelector('[data-plan-value="'+key+'"]').valueAsNumber]))};
 }
 const output=(key,value)=>{section.querySelectorAll('[data-plan-output="'+key+'"]').forEach(item=>item.textContent=value);};
 const priceGuide=type=>(type.priceMode==='from'?L.from_label:L.guide_label)+' '+euro.format(type.min);
 function makeSummary(){
  const r=result,v=r.values;
  const lines=['TAFOLLI & CO. — BUDGETPLANER','Unverbindliches Rechenszenario / illustrative scenario','',L.type_label+': '+(r.active.website?r.websiteType.labels[config.lang]:'—'),...(r.active.website?[L.range+': '+priceGuide(r.websiteType),L.scope_note]:[]),'',...serviceKeys.map((key,i)=>L.services[i]+': '+(r.active[key]?euro.format(v[key])+' / '+(key==='website'?L.once:L.monthly):'—')),'',L.once_label+': '+euro.format(r.once),L.monthly_label+': '+euro.format(r.monthly),'',L.metrics[0]+': '+number.format(r.impressions),L.metrics[1]+': '+number.format(r.addedVisits),L.metrics[2]+': '+decimal.format(r.addedLeads),L.metrics[3]+': '+number.format(r.low)+'–'+number.format(r.high),'',...assumptions.map((key,i)=>L.fields[i]+': '+decimal.format(v[key])),'',L.model_note,L.formula,L.organic,'','https://tafolli.net/#budgetplaner'];
  return lines.join('\n');
 }
 function updateMailto(){
  const data=new FormData(form);
  const body=[L.name+': '+String(data.get('name')||''),L.company+': '+String(data.get('company')||''),L.email+': '+String(data.get('email')||''),L.phone+': '+String(data.get('phone')||''),'',String(data.get('message')||''),'',summary].join('\n');
  section.querySelector('[data-plan-mailto]').href='mailto:'+config.recipient+'?subject='+encodeURIComponent(L.subject)+'&body='+encodeURIComponent(body);
 }
 function drawChart(input){
  const max=Math.max(2000,Math.ceil((result.active.ads?result.values.ads:0)/500)*500);
  const values=Array.from({length:5},(_,i)=>i*max/4),points=scaling(input,values);
  const min=Math.min(0,...points.map(p=>p.customers)),high=Math.max(1,...points.map(p=>p.customers));
  const span=(high-min)*1.15;
  const xy=p=>[36+p.budget/max*429,112-(p.customers-min)/span*94];
  const coordinates=points.map(xy),path=coordinates.map((p,i)=>(i?'L':'M')+p.map(x=>x.toFixed(2)).join(' ')).join(' ');
  section.querySelector('[data-plan-chart-line]').setAttribute('d',path);
  section.querySelector('[data-plan-chart-area]').setAttribute('d',path+' L465 112 L36 112 Z');
  const selected={budget:result.active.ads?result.values.ads:0,customers:result.customers},[cx,cy]=xy(selected);
  const dot=section.querySelector('[data-plan-chart-dot]');dot.setAttribute('cx',cx.toFixed(2));dot.setAttribute('cy',cy.toFixed(2));
  const ticks=section.querySelector('[data-plan-chart-ticks]');ticks.replaceChildren(...values.map(value=>{const span=document.createElement('span');span.textContent=euro.format(value);return span;}));
  const axis=section.querySelector('[data-plan-chart-axis]');axis.replaceChildren(...[min,high].map((value,i)=>{const text=document.createElementNS('http://www.w3.org/2000/svg','text');text.setAttribute('x','0');text.setAttribute('y',i?'23':'115');text.textContent=number.format(value);return text;}));
  const title=section.querySelector('#planner-chart-title');title.textContent=L.chart+': '+points.map(p=>euro.format(p.budget)+' → '+decimal.format(p.customers)).join('; ');
 }
 function update(){
  if(updateFrame)cancelAnimationFrame(updateFrame);
  updateFrame=0;const input=read();result=calculate(input);
  const type=result.websiteType;
  section.querySelector('[data-plan-value=website]').min=String(type.min);
  section.querySelector('[data-plan-type-range]').textContent=priceGuide(type);
  section.querySelector('[data-plan-type-note]').textContent=type.notes[config.lang];
  section.querySelector('[data-plan-preview]').dataset.kind=type.id;
  section.querySelector('[data-plan-preview-title]').textContent=type.labels[config.lang];
  section.querySelector('[data-plan-preview-pages]').textContent=type.pages;
  Object.entries(result.channels).forEach(([key,visits])=>{section.querySelector('[data-plan-channel="'+key+'"]').dataset.enabled=String(visits>0);section.querySelector('[data-plan-channel-node="'+key+'"]').dataset.enabled=String(visits>0);});
  serviceKeys.forEach(key=>{
   const active=result.active[key],field=section.querySelector('[data-plan-value="'+key+'"]');
   section.querySelector('[data-planner-service="'+key+'"]').dataset.active=String(active);field.disabled=!active;
   if(document.activeElement!==field)field.value=String(result.values[key]);
  });
  section.querySelector('[data-plan-value=targetCvr]').disabled=!result.active.website;
  range.disabled=!result.active.ads;range.max=String(Math.max(5000,Math.ceil(result.values.ads/1000)*1000));range.value=String(result.values.ads);
  section.querySelector('[data-plan-ad-label]').textContent=euro.format(result.values.ads);
  const rangeLabels=range.nextElementSibling;rangeLabels.lastElementChild.textContent=euro.format(Number(range.max));
  output('once',euro.format(result.once));output('monthly',euro.format(result.monthly));output('impressions',number.format(result.impressions));output('addedVisits',number.format(result.addedVisits));output('addedLeads',number.format(result.addedLeads));
  output('customers',result.low===result.high?number.format(result.low):number.format(result.low)+'–'+number.format(result.high));
  section.querySelector('[data-plan-assumption-line]').textContent=decimal.format(result.values.cpc)+' € '+L.rate_labels[0]+' · '+decimal.format(result.effectiveCvr)+' % '+L.rate_labels[1]+' · '+decimal.format(result.values.closeRate)+' % '+L.rate_labels[2];
  summary=makeSummary();section.querySelector('[data-plan-mail-summary]').value=summary;
  section.querySelector('[data-plan-send-summary]').textContent=(result.active.website?type.labels[config.lang]+'\n':'')+serviceKeys.filter(key=>result.active[key]).map(key=>L.services[serviceKeys.indexOf(key)]).join(' · ')+'\n'+euro.format(result.once)+' '+L.once+' / '+euro.format(result.monthly)+' '+L.monthly;
  updateMailto();drawChart(input);
  if(!reduce.matches&&document.documentElement.dataset.motion!=='paused'&&section.dataset.planMotionState!=='paused'){
   animation?.cancel();const box=section.querySelector('.planner-metrics');if(typeof box.animate==='function')animation=box.animate([{opacity:.55,transform:'translateY(3px)'},{opacity:1,transform:'translateY(0)'}],{duration:220,easing:'ease-out'});
  }
  if(initialized){clearTimeout(liveTimer);liveTimer=setTimeout(()=>{section.querySelector('[data-plan-live]').textContent=L.updated+': '+euro.format(result.once)+' '+L.once+', '+euro.format(result.monthly)+' '+L.monthly;},500);}initialized=true;
 }
 function schedule(){if(!updateFrame)updateFrame=requestAnimationFrame(update);}
 section.querySelectorAll('[data-plan-value]').forEach(input=>{
  const commit=()=>{input.value=String(calculate(read()).values[input.dataset.planValue]);schedule();};
  input.addEventListener('input',schedule);input.addEventListener('change',commit);input.addEventListener('blur',commit);
 });
 section.querySelectorAll('[data-plan-active]').forEach(input=>input.addEventListener('change',schedule));
 section.querySelectorAll('[data-plan-type]').forEach(input=>input.addEventListener('change',()=>{
  const type=catalog.websiteTypes.find(type=>type.id===input.value);
  section.querySelector('[data-plan-value=website]').value=String(type.min);
  section.querySelector('[data-plan-active=website]').checked=true;
  update();
 }));
 range.addEventListener('input',()=>{section.querySelector('[data-plan-value=ads]').value=range.value;schedule();});
 form.addEventListener('input',updateMailto);
 section.querySelector('[data-plan-download]').addEventListener('click',()=>{
  update();const url=URL.createObjectURL(new Blob([summary],{type:'text/plain;charset=utf-8'})),a=document.createElement('a');a.href=url;a.download='tafolli-projektplanung.txt';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
 });
 let sending=false;
 form.addEventListener('submit',async event=>{
  event.preventDefault();if(sending||!form.reportValidity())return;
  if(form.elements._honey.value)return;
  update();sending=true;submit.disabled=true;status.textContent=L.sending;status.dataset.state='sending';
  const payload=Object.fromEntries(new FormData(form));payload._subject='Tafolli & Co. | '+L.subject;payload.Planung=summary;payload.Website='https://tafolli.net/#budgetplaner';
  try{
   await deliverInquiry(config.endpoint,payload);
   status.textContent=L.success;status.dataset.state='success';
  }catch(error){status.textContent=error.message==='activation'?L.activation:L.error;status.dataset.state='error';submit.disabled=false;}
  finally{sending=false;}
 });
 section.querySelector('[data-planner-interface]').hidden=false;
 update();
});
