/* Original motion and interactive explanations. Everything runs locally. */
(() => {
  'use strict';
  const root = document.documentElement;
  const configEl = document.getElementById('experience-config');
  if (!configEl) return;
  const config = JSON.parse(configEl.textContent);
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let userPaused = null;
  let paused = reduced.matches;
  const $ = id => document.getElementById(id);

  // Native focus stays visible. The artwork follows the pointer, not the cursor.
  const menuButton = document.querySelector('.x-menu-button');
  const menu = $('x-menu');
  function closeMenu() {
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
  }
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menu.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
  });
  menu.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !menu.hidden) { closeMenu(); menuButton.focus(); }
  });
  document.addEventListener('click', e => {
    if (!menu.hidden && !e.target.closest('.x-header')) closeMenu();
  });
  matchMedia('(min-width:801px)').addEventListener('change', e => { if (e.matches) closeMenu(); });

  const reveals = [...document.querySelectorAll('[data-reveal]')];
  const motionButton = document.querySelector('.x-motion');
  let revealObserver;
  if ('IntersectionObserver' in window && !paused) {
    root.classList.add('x-ready');
    revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0, rootMargin: '0px 0px -30px 0px' });
    reveals.forEach(el => { el.classList.add('will-reveal'); revealObserver.observe(el); });
  }
  function syncMotion() {
    paused = userPaused === null ? reduced.matches : userPaused;
    root.classList.toggle('motion-paused', paused);
    motionButton.setAttribute('aria-pressed', String(paused));
    motionButton.querySelector('span').textContent = paused ? '▷' : 'Ⅱ';
    if (paused) reveals.forEach(el => el.classList.add('is-visible'));
    if (paused && running) completeDemo();
    requestDraw();
    updateScroll();
  }
  motionButton.addEventListener('click', () => { userPaused = !paused; syncMotion(); });
  reduced.addEventListener('change', () => { userPaused = null; syncMotion(); });

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
    runButton.textContent = label;
    const arrow = document.createElement('span');
    arrow.setAttribute('aria-hidden', 'true'); arrow.textContent = '↗';
    runButton.appendChild(arrow);
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
    if (paused) { completeDemo(); return; }
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
  calculate();

  // Sculptural torus: a lit, breathing mesh rendered without WebGL or a library.
  const canvas = $('intelligence');
  const art = document.querySelector('.x-art');
  const ctx = canvas.getContext('2d');
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  let pointerX = 0, pointerY = 0, rotationX = 0, rotationY = 0;
  let artVisible = true, frame = 0, lastFrame = 0, elapsed = 0;
  let dpr = Math.min(devicePixelRatio || 1,1.5);
  function resizeCanvas() {
    canvas.width = Math.round(640*dpr); canvas.height = Math.round(640*dpr);
    if (ctx) ctx.setTransform(dpr,0,0,dpr,0,0);
    requestDraw();
  }
  if (fine) {
    document.querySelector('.x-hero').addEventListener('pointermove',e => {
      const bounds = art.getBoundingClientRect();
      pointerX = Math.max(-1,Math.min(1,(e.clientX-bounds.left-bounds.width/2)/bounds.width));
      pointerY = Math.max(-1,Math.min(1,(e.clientY-bounds.top-bounds.height/2)/bounds.height));
      requestDraw();
    },{passive:true});
    document.querySelector('.x-hero').addEventListener('pointerleave',() => { pointerX=0;pointerY=0; });
  }
  function rotate(x,y,z,ax,ay,az) {
    let yy=y*Math.cos(ax)-z*Math.sin(ax),zz=y*Math.sin(ax)+z*Math.cos(ax);
    let xx=x*Math.cos(ay)+zz*Math.sin(ay);zz=-x*Math.sin(ay)+zz*Math.cos(ay);
    return [xx*Math.cos(az)-yy*Math.sin(az),xx*Math.sin(az)+yy*Math.cos(az),zz];
  }
  function draw(time) {
    if (!ctx) return;
    ctx.clearRect(0,0,640,640);
    const drift = paused ? 0 : time;
    const ax=1.02+rotationY*.3+Math.sin(drift*.0002)*.2;
    const ay=.32+rotationX*.4+Math.sin(drift*.00016)*.24;
    const az=-.56+Math.sin(drift*.00015)*.1;
    const ringCount=64, tubeCount=24, points=[], normals=[], faces=[];
    const breathe=paused?0:Math.sin(time*.00055)*.04;
    for(let i=0;i<=ringCount;i++) {
      const u=i/ringCount*Math.PI*2;
      points[i]=[];normals[i]=[];
      for(let j=0;j<=tubeCount;j++) {
        const v=j/tubeCount*Math.PI*2;
        const minor=.56+.09*Math.sin(5*u+time*.00045)+.035*Math.sin(3*v+time*.0006)+breathe;
        const radius=1.23+minor*Math.cos(v);
        const p=rotate(radius*Math.cos(u),radius*Math.sin(u),minor*Math.sin(v),ax,ay,az);
        const n=rotate(Math.cos(v)*Math.cos(u),Math.cos(v)*Math.sin(u),Math.sin(v),ax,ay,az);
        const perspective=5.4/(5.4-p[2]);
        points[i][j]=[320+p[0]*145*perspective,315+p[1]*145*perspective,p[2]];
        normals[i][j]=n;
      }
    }
    for(let i=0;i<ringCount;i++)for(let j=0;j<tubeCount;j++) {
      const quad=[points[i][j],points[i+1][j],points[i+1][j+1],points[i][j+1]];
      faces.push({quad,n:normals[i][j],z:quad.reduce((sum,p)=>sum+p[2],0)/4});
    }
    faces.sort((a,b)=>a.z-b.z);
    ctx.lineWidth=.65;
    for(const {quad,n} of faces) {
      const light=Math.max(0,n[0]*-.38+n[1]*-.5+n[2]*.75);
      const shine=Math.pow(light,14);
      const luminosity=26+light*42+shine*19;
      ctx.fillStyle='hsl('+(66+light*6)+', '+(44+light*21)+'%, '+luminosity+'%)';
      ctx.strokeStyle='rgba(38,49,12,'+(.12+light*.08)+')';
      ctx.beginPath();ctx.moveTo(quad[0][0],quad[0][1]);
      for(let k=1;k<4;k++)ctx.lineTo(quad[k][0],quad[k][1]);
      ctx.closePath();ctx.fill();ctx.stroke();
    }
    art.classList.add('is-rendered');
  }
  function tick(now) {
    frame=0;
    if (document.hidden || !artVisible) return;
    if (now-lastFrame>32 || paused) {
      if (!paused) elapsed += Math.min(now-lastFrame,50);
      lastFrame=now;
      rotationX+=(pointerX-rotationX)*.07;
      rotationY+=(pointerY-rotationY)*.07;
      draw(elapsed);
    }
    if (!paused) frame=requestAnimationFrame(tick);
  }
  function requestDraw() {
    if (!frame && ctx && artVisible && !document.hidden) frame=requestAnimationFrame(tick);
  }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      artVisible=entries[0].isIntersecting;
      if (artVisible) { lastFrame=performance.now();requestDraw(); }
      else if (frame) { cancelAnimationFrame(frame);frame=0; }
    },{rootMargin:'60px'}).observe(art);
  }
  document.addEventListener('visibilitychange',() => {
    if (document.hidden) { cancelAnimationFrame(frame);frame=0; }
    else { lastFrame=performance.now();requestDraw(); }
  });
  const progress=document.querySelector('.x-progress');
  const story=document.querySelector('.x-story');
  const scenes=[...document.querySelectorAll('[data-scene]')];
  const indicators=[...document.querySelectorAll('.x-story-indicators i')];
  const storyMedia=matchMedia('(min-width:801px) and (min-height:600px)');
  let storyStage=-1;
  let scrollFrame=0;
  function updateScroll() {
    scrollFrame=0;
    const total=document.documentElement.scrollHeight-innerHeight;
    progress.style.transform='scaleX('+(total>0?scrollY/total:0)+')';
    if(story) {
      const rect=story.getBoundingClientRect();
      const fraction=Math.max(0,Math.min(1,(87-rect.top)/(rect.height-innerHeight+87)));
      const stage=paused||!storyMedia.matches?0:Math.min(2,Math.floor(fraction*3));
      if(stage!==storyStage) {
        storyStage=stage;
        scenes.forEach((scene,i)=>scene.classList.toggle('is-active',i===stage));
        indicators.forEach((el,i)=>el.classList.toggle('is-active',i===stage));
        story.classList.toggle('is-connected',stage>0);
        story.classList.toggle('is-free',stage===2);
        story.querySelector('.x-story-art').style.setProperty('--connect',stage===1?'1':'0');
        story.querySelector('.x-story-art').style.setProperty('--freedom',stage===2?'1':'0');
      }
    }
  }
  addEventListener('scroll',() => { if(!scrollFrame)scrollFrame=requestAnimationFrame(updateScroll); },{passive:true});
  addEventListener('resize',() => { dpr=Math.min(devicePixelRatio||1,1.5);resizeCanvas();updateScroll(); },{passive:true});
  resizeCanvas();
  syncMotion();
})();
