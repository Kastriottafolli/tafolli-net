/* Native disclosure navigation: one shared tree for desktop and mobile. */
(() => {
  'use strict';
  const nav=document.getElementById('site-navigation');
  if(!nav)return;
  const toggle=document.querySelector('[data-nav-toggle]');
  const sections=[...nav.querySelectorAll('.site-nav-section')];
  const desktop=matchMedia('(min-width:1101px)');
  document.documentElement.classList.add('nav-ready');
  function closeSections(){sections.forEach(section=>section.open=false);}
  function close(){
    closeSections();nav.classList.remove('is-open');
    toggle?.setAttribute('aria-expanded','false');
  }
  sections.forEach(section=>section.addEventListener('toggle',()=>{
    if(section.open)sections.forEach(other=>{if(other!==section)other.open=false;});
  }));
  toggle?.addEventListener('click',()=>{
    const open=toggle.getAttribute('aria-expanded')!=='true';
    closeSections();nav.classList.toggle('is-open',open);toggle.setAttribute('aria-expanded',String(open));
  });
  document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!toggle?.contains(e.target))close();});
  document.addEventListener('keydown',e=>{
    if(e.key!=='Escape')return;
    const opened=sections.find(section=>section.open);
    if(opened){opened.open=false;opened.querySelector('summary').focus();}
    else if(nav.classList.contains('is-open')){close();toggle?.focus();}
  });
  nav.addEventListener('focusout',e=>{
    if(desktop.matches&&!nav.contains(e.relatedTarget))closeSections();
  });
  nav.addEventListener('click',e=>{if(e.target.closest('a'))close();});
  desktop.addEventListener('change',close);
  window.addEventListener('pagehide',close);
})();
