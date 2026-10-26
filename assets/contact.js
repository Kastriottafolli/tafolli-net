import {deliverInquiry} from './form-delivery.mjs';

const form=document.querySelector('[data-project-brief]');
if(form){
 const topic=form.elements.thema,message=form.elements.message;
 const status=form.querySelector('[data-brief-status]'),submit=form.querySelector('[type=submit]');
 const fallback=form.querySelector('[data-brief-mailto]');
 const query=new URLSearchParams(location.search),requested=query.get('thema');
 if([...topic.options].some(option=>option.value===requested))topic.value=requested;
 const service=query.get('leistung');
 if(service&&!message.value)message.value='Ich möchte ein Projekt zum Thema '+service+' besprechen. ';
 let sending=false;
 function payload(){
  return {...Object.fromEntries(new FormData(form)),Thema:topic.selectedOptions[0].textContent,Website:'https://tafolli.net/kontakt.html'};
 }
 function updateFallback(){
  const p=payload();
  const body=['Name: '+p.name,'E-Mail: '+p.email,'Unternehmen: '+p.company,'Thema: '+p.Thema,'Zeitraum: '+p.zeitraum,'',p.message].join('\n');
  fallback.href='mailto:info@tafolli.net?subject='+encodeURIComponent('Projektanfrage: '+p.Thema)+'&body='+encodeURIComponent(body);
 }
 form.addEventListener('input',updateFallback);form.addEventListener('change',updateFallback);
 form.addEventListener('submit',async event=>{
  event.preventDefault();if(sending||!form.reportValidity()||form.elements._honey.value)return;
  sending=true;submit.disabled=true;form.setAttribute('aria-busy','true');
  status.dataset.state='sending';status.textContent='Ihre Anfrage wird übermittelt …';
  try{
   await deliverInquiry(form.dataset.deliveryEndpoint,payload());
   status.dataset.state='success';status.textContent='Ihre Anfrage wurde an den Versanddienst übergeben. Vielen Dank – wir melden uns bei Ihnen.';
   submit.textContent='Anfrage gesendet';
  }catch(error){
   status.dataset.state='error';submit.disabled=false;
   status.textContent=error.message==='activation'?'Der Formularversand ist derzeit nicht verfügbar. Bitte nutzen Sie den E-Mail-Entwurf.':'Die Übermittlung konnte nicht bestätigt werden. Ihre Eingaben bleiben erhalten. Bitte versuchen Sie es erneut oder nutzen Sie den E-Mail-Entwurf.';
  }finally{sending=false;form.removeAttribute('aria-busy');}
 });
 updateFallback();
}

