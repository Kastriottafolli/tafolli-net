import {calculate,scaling,defaults} from './planner-model.mjs';
import {deliverInquiry} from './form-delivery.mjs';

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
 let result,summary='',updateFrame=0,animation=null;
 function read(){
  return {active:Object.fromEntries(serviceKeys.map(key=>[key,section.querySelector('[data-plan-active="'+key+'"]').checked])),values:Object.fromEntries(Object.keys(defaults).map(key=>[key,section.querySelector('[data-plan-value="'+key+'"]').valueAsNumber]))};
 }
 const output=(key,value)=>{section.querySelectorAll('[data-plan-output="'+key+'"]').forEach(item=>item.textContent=value);};
 function makeSummary(){
  const r=result,v=r.values;
  const lines=['TAFOLLI & CO. — BUDGETPLANER','Unverbindliches Rechenszenario / illustrative scenario','',...serviceKeys.map((key,i)=>L.services[i]+': '+(r.active[key]?euro.format(v[key])+' / '+(key==='website'?L.once:L.monthly):'—')),'',L.once_label+': '+euro.format(r.once),L.monthly_label+': '+euro.format(r.monthly),'',L.metrics[0]+': '+number.format(r.impressions),L.metrics[1]+': '+number.format(r.addedVisits),L.metrics[2]+': '+decimal.format(r.addedLeads),L.metrics[3]+': '+number.format(r.low)+'–'+number.format(r.high),'',...assumptions.map((key,i)=>L.fields[i]+': '+decimal.format(v[key])),'',L.model_note,L.formula,L.organic,'','https://tafolli.net/#budgetplaner'];
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
  updateFrame=0;const input=read();result=calculate(input);
  serviceKeys.forEach(key=>{const active=result.active[key];section.querySelector('[data-planner-service="'+key+'"]').dataset.active=String(active);section.querySelector('[data-plan-value="'+key+'"]').disabled=!active;});
  section.querySelector('[data-plan-value=targetCvr]').disabled=!result.active.website;
  range.disabled=!result.active.ads;range.max=String(Math.max(5000,Math.ceil(result.values.ads/1000)*1000));range.value=String(result.values.ads);
  section.querySelector('[data-plan-ad-label]').textContent=euro.format(result.values.ads);
  const rangeLabels=range.nextElementSibling;rangeLabels.lastElementChild.textContent=euro.format(Number(range.max));
  output('once',euro.format(result.once));output('monthly',euro.format(result.monthly));output('impressions',number.format(result.impressions));output('addedVisits',number.format(result.addedVisits));output('addedLeads',number.format(result.addedLeads));
  output('customers',result.low===result.high?number.format(result.low):number.format(result.low)+'–'+number.format(result.high));
  section.querySelector('[data-plan-assumption-line]').textContent=decimal.format(result.values.cpc)+' € '+L.rate_labels[0]+' · '+decimal.format(result.effectiveCvr)+' % '+L.rate_labels[1]+' · '+decimal.format(result.values.closeRate)+' % '+L.rate_labels[2];
  summary=makeSummary();section.querySelector('[data-plan-mail-summary]').value=summary;
  section.querySelector('[data-plan-send-summary]').textContent=serviceKeys.filter(key=>result.active[key]).map(key=>L.services[serviceKeys.indexOf(key)]).join(' · ')+'\n'+euro.format(result.once)+' '+L.once+' / '+euro.format(result.monthly)+' '+L.monthly;
  updateMailto();drawChart(input);
  if(!reduce.matches&&document.documentElement.dataset.motion!=='paused'){
   animation?.cancel();const box=section.querySelector('.planner-metrics');if(typeof box.animate==='function')animation=box.animate([{opacity:.55,transform:'translateY(3px)'},{opacity:1,transform:'translateY(0)'}],{duration:220,easing:'ease-out'});
  }
 }
 function schedule(){if(!updateFrame)updateFrame=requestAnimationFrame(update);}
 section.querySelectorAll('[data-plan-value]').forEach(input=>{input.addEventListener('input',schedule);input.addEventListener('change',()=>{input.value=String(calculate(read()).values[input.dataset.planValue]);schedule();});});
 section.querySelectorAll('[data-plan-active]').forEach(input=>input.addEventListener('change',schedule));
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
