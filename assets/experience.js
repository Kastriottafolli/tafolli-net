/* Interactive workflow example and transparent time estimate. No decorative animation. */
(() => {
  'use strict';
  const configEl = document.getElementById('experience-config');
  if (!configEl) return;
  const config = JSON.parse(configEl.textContent);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const $ = id => document.getElementById(id);
  // A deterministic demonstration, never a live booking or a model request.
  const tabs = [...document.querySelectorAll('[data-scenario]')];
  const stages = [...document.querySelectorAll('[data-stage]')];
  const runButton = $('run-workflow');
  const lab = document.querySelector('.x-lab');
  let selected = 0, running = false, demoTimers = [];
  function clearDemoTimers() {
    demoTimers.forEach(clearTimeout);
    demoTimers = [];
    running = false;
    lab.removeAttribute('data-running');
    runButton.disabled = false;
  }
  function setRunLabel(label) {
    const arrow = runButton.querySelector('span').cloneNode(true);
    runButton.replaceChildren(document.createTextNode(label), arrow);
  }
  function selectScenario(index, focus = false) {
    clearDemoTimers(); selected = index;
    tabs.forEach((tab,i) => {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
    });
    $('demo-panel').setAttribute('aria-labelledby', tabs[index].id);
    if (focus) tabs[index].focus();
    const demo = config.demos[index];
    $('demo-source').textContent = demo.source;
    $('demo-subject').textContent = demo.subject;
    $('demo-message').textContent = demo.message;
    $('demo-idle').hidden = false;
    $('demo-result').hidden = true;
    $('demo-status').textContent = config.ready;
    stages.forEach(el => el.classList.remove('is-active','is-done'));
    setRunLabel(config.run);
  }
  tabs.forEach((tab,index) => {
    tab.addEventListener('click', () => selectScenario(index));
    tab.addEventListener('keydown', e => {
      let next;
      if (e.key === 'ArrowRight') next = (index+1)%tabs.length;
      if (e.key === 'ArrowLeft') next = (index+tabs.length-1)%tabs.length;
      if (e.key === 'Home') next = 0;
      if (e.key === 'End') next = tabs.length-1;
      if (next !== undefined) { e.preventDefault(); selectScenario(next,true); }
    });
  });
  function setStage(index) {
    stages.forEach((el,i) => {
      el.classList.toggle('is-active',i === index);
      el.classList.toggle('is-done',i < index);
    });
    $('demo-status').textContent = config.stage_notes[index];
  }
  function completeDemo() {
    clearDemoTimers();
    setStage(4);
    stages.forEach(el => el.classList.add('is-done'));
    const demo = config.demos[selected];
    $('demo-fields').replaceChildren(...demo.fields.map(text => {
      const li = document.createElement('li'); li.textContent = text; return li;
    }));
    $('demo-result-title').textContent = demo.result_title;
    $('demo-result-copy').textContent = demo.result;
    $('demo-receipt').textContent = demo.receipt;
    $('demo-idle').hidden = true;
    $('demo-result').hidden = false;
    setRunLabel(config.replay);
  }
  runButton.addEventListener('click', () => {
    selectScenario(selected);
    if (reduced.matches) { completeDemo(); return; }
    running = true;
    lab.setAttribute('data-running','');
    runButton.disabled = true;
    setRunLabel(config.running);
    setStage(0);
    for (let i=1;i<5;i++) demoTimers.push(setTimeout(() => setStage(i),i*850));
    demoTimers.push(setTimeout(completeDemo,4300));
  });

  // Transparent savings model: tasks * minutes * 22 days * share / 60.
  const roiInputs = [...document.querySelectorAll('[data-roi]')];
  const locale = document.documentElement.lang === 'en' ? 'en-GB' : document.documentElement.lang === 'sq' ? 'sq-AL' : 'de-DE';
  const number = new Intl.NumberFormat(locale,{ maximumFractionDigits:0 });
  const money = new Intl.NumberFormat(locale,{ style:'currency',currency:'EUR',maximumFractionDigits:0 });
  function calculate() {
    const values = roiInputs.map(input => Number(input.value));
    roiInputs.forEach((input,i) => {
      $('roi-value-'+i).textContent = number.format(values[i])+' '+config.roi_units[i];
      input.style.setProperty('--fill',((values[i]-Number(input.min))/(Number(input.max)-Number(input.min))*100)+'%');
    });
    const hours = values[0]*values[1]*22*(values[3]/100)/60;
    $('roi-hours').textContent = number.format(hours);
    $('roi-money').textContent = money.format(hours*values[2]);
    const labels = roiInputs.map((input,i) => document.querySelector('label[for="'+input.id+'"]').textContent+': '+values[i]+' '+config.roi_units[i]);
    const body = 'AI Automation as a Service\n\n'+labels.join('\n')+'\n\n'+number.format(hours)+' '+document.querySelector('.x-roi-result>p').textContent;
    $('roi-contact').href = 'mailto:info@tafolli.net?subject='+encodeURIComponent('AI Automation as a Service')+'&body='+encodeURIComponent(body);
  }
  roiInputs.forEach(input => input.addEventListener('input',calculate));
  if(roiInputs.length) calculate();


  reduced.addEventListener('change', () => { if (reduced.matches && running) completeDemo(); });
  window.addEventListener('pagehide', clearDemoTimers);
})();
