"""Dependency-free, localized automation experience. Built from source."""
from icons import iconize
import hashlib, html, json, pathlib
from inhalt_de import DE
from inhalt_en import EN
from inhalt_sq import SQ
from experience_content import COPY
from companies import company_link
from brand import lockup, intro
from navigation import nav as site_nav, toggle as nav_toggle, breadcrumbs
from seo import metadata, structured, region
from portrait import portrait
from partners import strip as partner_strip

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGUAGES = [DE, EN, SQ]
ARROW = '<span aria-hidden="true">↗</span>'

def heading(lines):
    return '<br>'.join(f'<span>{line}</span>' for line in lines)

def page(L, detail=False):
    C = dict(COPY[L['code']])
    if detail:
        C.update(description=C['automation_description'], hero_text=C['automation_hero_text'], hero_cta=C['automation_cta'])
    title = 'AI Automation as a Service · Kastriot Tafolli' if detail else C['title']
    if detail: title, C['description'] = metadata('ki-automatisierung.html', title, C['description'])
    version = hashlib.sha256(b''.join((ROOT / f'assets/{f}').read_bytes() for f in ['kt.css', 'kt.js', 'experience.css', 'experience.js', 'partners.js', 'brand.js', 'navigation.js'])).hexdigest()[:10]
    a = lambda p: p if p.startswith(('../', '/', '#', 'mailto:', 'https:')) else ('../' if L['dir'] else '') + p
    home = '/' + (L['dir'] + '/' if L['dir'] else '')
    canonical = 'https://tafolli.net/' + ('ki-automatisierung.html' if detail else (L['dir'] + '/' if L['dir'] else ''))
    current = 'ki-automatisierung.html' if detail else (L['dir']+'/' if L['dir'] else 'index.html')
    nav = site_nav(current, '../' if L['dir'] else '', L['code'])
    languages = ''.join(f'<a href="/{s["dir"] + "/" if s["dir"] else ""}" lang="{s["code"]}" hreflang="{s["code"]}" aria-label="{s["code"].upper()} – {s["name"]}"'+(' aria-current="page"' if s['code']==L['code'] and not detail else '')+f'>{s["code"].upper()}</a>' for s in LANGUAGES)
    alternatives = '' if detail else ''.join(f'<link rel="alternate" hreflang="{s["code"]}" href="https://tafolli.net/{s["dir"] + "/" if s["dir"] else ""}">' for s in LANGUAGES)+'<link rel="alternate" hreflang="x-default" href="https://tafolli.net/">'
    hero_lines = C['detail_hero'] if detail else C['hero']
    hero = f'''
<section class="x-hero" id="top"><div class="x-shell">
 <div class="x-hero-meta"><span><i class="x-dot"></i>{C['status']}</span><span>{C['location']}</span></div>
 <div class="x-hero-stage"><h1><span class="x-line"><span>{hero_lines[0]}</span></span><span class="x-line"><span>{hero_lines[1]}</span></span><span class="x-line x-serif"><span>{hero_lines[2]}</span></span></h1>
 <div class="x-art" aria-hidden="true"><div class="x-art-orbit"></div><img class="x-bloom-fallback" src="{a('assets/intelligence.svg')}" width="640" height="640" alt=""><canvas id="intelligence" width="640" height="640"></canvas><span class="x-art-node x-node-a">NEURAL OS <i>↗</i></span><span class="x-art-node x-node-b">HUMAN IN THE LOOP</span><span class="x-art-caption">{C['art_label']}</span></div></div>
 <div class="x-hero-bottom"><div><p>{C['hero_text']}</p><div class="x-actions"><a class="x-button x-button-dark" href="{'#ki' if detail else a('leistungen.html')}">{C['hero_cta']}{ARROW}</a><a class="x-text-link" href="{a('kontakt.html')}">{C['hero_link']} ↗</a></div></div><a class="x-scroll" href="{'#ki' if detail else '#idee'}" {'hidden' if detail else ''}><span>↓</span>{C['scroll']}</a></div>
</div></section>'''
    manifesto = f'''
<section class="x-manifesto x-section" id="idee"><div class="x-shell"><p class="x-label" data-reveal>{C['intro']}</p><div class="x-manifesto-grid"><h2 data-reveal>{heading(C['manifesto'])}</h2><div data-reveal><p class="x-large-copy">{C['manifesto_text']}</p><p>{C['manifesto_small']}</p><span class="x-spark" aria-hidden="true">✳</span></div></div></div></section>
<div class="x-ticker-wrap" aria-hidden="true"><div class="x-ticker"><div>{''.join('<span>AUTOMATE THE ORDINARY <i>✳</i> MAKE ROOM FOR THE EXTRAORDINARY <i>✳</i></span>' for _ in range(4))}</div></div></div>'''
    story = f'''<section class="x-story" aria-label="{C['story_label']}"><div class="x-story-pin"><div class="x-shell"><p class="x-label">{C['story_label']}</p><div class="x-story-grid"><div class="x-story-scenes">{''.join(f'<article class="x-story-scene" data-scene="{i}"><span class="x-label">0{i+1} / 03</span><h2>{title}</h2><p>{body}</p></article>' for i,(title,body) in enumerate(zip(C['story_titles'],C['story_copies'])))}</div><div class="x-story-art" aria-hidden="true"><svg viewBox="0 0 500 400" fill="none"><path d="M90 100L250 200L410 100M90 300L250 200L410 300M250 45V355" stroke="currentColor" stroke-width="1" stroke-dasharray="4 6"/></svg><div class="x-story-hub">✳</div>{''.join(f'<div class="x-task x-task-{i}"><span>{["↙","≡","⌁","▤","↗","◎"][i]}</span>{task}<i>↗</i></div>' for i,task in enumerate(C['story_tasks']))}<span class="x-story-outcome">{C['story_outcome']} ↗</span></div></div><div class="x-story-bottom"><span>SCROLL → CONNECT → CREATE</span><div class="x-story-indicators" aria-hidden="true"><i></i><i></i><i></i></div></div></div></div></section>'''
    tabs = ''.join(f'<button type="button" class="x-tab" role="tab" id="scenario-{i}" aria-controls="demo-panel" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}" data-scenario="{i}"><span>0{i+1}</span>{t}</button>' for i,t in enumerate(C['scenarios']))
    stages = ''.join(f'<li data-stage="{i}"><span>0{i+1}</span><b>{t}</b><i aria-hidden="true"></i></li>' for i,t in enumerate(C['stages']))
    demo = C['demos'][0]
    lab = f'''
<section class="x-automation x-section" id="ki"><div class="x-shell">
 <div class="x-product" data-reveal><p class="x-label">{C['service_label']}</p><h2>{heading(C['service_title'])}</h2><div><p>{C['service_text']}</p><ul>{''.join(f'<li>{t}</li>' for t in C['service_tags'])}</ul></div></div>
 <div class="x-section-heading"><div data-reveal><p class="x-label">{C['lab_label']}</p><h3>{heading(C['lab_title'])}</h3></div><p data-reveal>{C['lab_text']}</p></div>
 <div class="x-lab" data-reveal><div class="x-lab-top"><span><i class="x-dot"></i>AUTOMATION LAB</span><span>{C['demo_label']}</span></div><div class="x-tabs" role="tablist" aria-label="{C['lab_title'][0]}">{tabs}</div>
 <div id="demo-panel" role="tabpanel" aria-labelledby="scenario-0" tabindex="0"><div class="x-demo-grid">
 <article class="x-input-card"><p class="x-label" id="demo-source">{demo['source']}</p><div class="x-mail-icon" aria-hidden="true">↙</div><h4 id="demo-subject">{demo['subject']}</h4><p id="demo-message">{demo['message']}</p></article>
 <div class="x-engine" aria-hidden="true"><div class="x-engine-ring"></div><div class="x-engine-ring"></div><span>AI<span aria-hidden="true">✳</span></span><small>TAFOLLI ENGINE</small></div>
 <article class="x-output-card"><p class="x-label">{C['outgoing']}</p><div class="x-output-idle" id="demo-idle"><span aria-hidden="true">↗</span><p>{C['ready']}</p></div><div id="demo-result" hidden><ul id="demo-fields"></ul><h4 id="demo-result-title"></h4><p id="demo-result-copy"></p><p class="x-receipt" id="demo-receipt"></p></div></article></div>
 <ol class="x-stages" aria-label="{C['lab_label']}">{stages}</ol><div class="x-demo-control"><p id="demo-status" role="status" aria-live="polite">{C['ready']}</p><button type="button" class="x-button x-button-lime" id="run-workflow">{C['run']}{ARROW}</button></div></div><p class="x-demo-hint">{C['demo_hint']}</p></div>
</div></section>'''
    care = f'''
<section class="x-care x-section"><div class="x-shell x-care-grid"><div><p class="x-label" data-reveal>{C['care_label']}</p><h2 data-reveal>{heading(C['care_title'])}</h2><p class="x-care-copy" data-reveal>{C['care_text']}</p><div class="x-care-items">{''.join(f'<article data-reveal><span>0{i+1}</span><div><h3>{t}</h3><p>{b}</p></div></article>' for i,(t,b) in enumerate(C['care_items']))}</div></div><div class="x-care-art" data-reveal><div class="x-orbit-map" aria-hidden="true"><div class="x-orbit-track"></div><div class="x-orbit-track x-orbit-track-2"></div><div class="x-orbit-core">✳</div>{''.join(f'<span class="x-satellite x-satellite-{i}">{t}</span>' for i,t in enumerate(C['care_orbit']))}<i class="x-orbit-particle"></i></div><p class="x-label">{C['care_note']}</p></div></div></section>'''
    vals = [(40,0,200,1),(4,1,20,1),(30,10,150,5),(70,0,100,5)]
    sliders = ''.join(f'<div class="x-range-row"><div><label for="roi-{i}">{label}</label><output for="roi-{i}" id="roi-value-{i}">{value} {C["roi_units"][i]}</output></div><input id="roi-{i}" type="range" min="{mn}" max="{mx}" step="{step}" value="{value}" data-roi="{i}"></div>' for i,(label,(value,mn,mx,step)) in enumerate(zip(C['roi_labels'],vals)))
    roi = f'''
<section class="x-roi x-section" id="potenzial"><div class="x-shell"><div class="x-section-heading"><div data-reveal><p class="x-label">{C['roi_label']}</p><h2>{heading(C['roi_title'])}</h2></div><p data-reveal>{C['roi_text']}</p></div><div class="x-roi-grid" data-reveal><div class="x-roi-inputs">{sliders}</div><div class="x-roi-result"><span class="x-label">TIME, REIMAGINED.</span><div class="x-hour-value"><output id="roi-hours">41</output><span aria-hidden="true">↗</span></div><p>{C['hours']}</p><div class="x-roi-money"><span>{C['value']}</span><output id="roi-money">1.232 €</output></div><a class="x-button x-button-dark" id="roi-contact" href="mailto:info@tafolli.net">{C['roi_cta']}{ARROW}</a></div></div><p class="x-roi-note">{C['roi_note']}</p></div></section>'''
    cards = ''.join(f'<a href="{a(h)}" class="x-service x-service-{i}" data-reveal><div class="x-service-top"><span>{nr} / {label}</span>{ARROW}</div><div class="x-service-art" aria-hidden="true">{["✳","↗","◎"][i]}</div><h3>{t}</h3><p>{b}</p><span class="x-service-link">{cta} ↗</span></a>' for i,(nr,label,t,b,h,cta) in enumerate(C['services']))
    services = f'<section class="x-services x-section" id="leistungen"><div class="x-shell"><p class="x-label" data-reveal>{C["services_label"]}</p><h2 data-reveal>{heading(C["services_title"])}</h2><div class="x-service-grid">{cards}</div><a class="x-button x-button-dark x-portfolio-cta" href="{a('leistungen.html')}">{C['portfolio_link']} {ARROW}</a></div></section>'
    bio = f'''
<section class="x-about x-section" id="ueber"><div class="x-shell"><div class="x-about-grid"><figure data-reveal>{portrait('../' if L['dir'] else '', L['code'])}<figcaption class="x-label">{C['about_caption']}</figcaption></figure><div class="x-about-copy"><p class="x-label" data-reveal>{C['about_label']}</p><h2 data-reveal>{heading(C['about_title'])}</h2><p data-reveal>{C['about_text']}</p><a class="x-text-link" href="{a('ueber-mich.html')}">{C['about_link']} ↗</a><div class="x-credentials">{''.join(f'<div data-reveal><b>{n}</b><span>{t}</span></div>' for n,t in C['credentials'])}</div></div></div><div class="x-experience"><p class="x-label">{C['experience_label']}</p><div>{''.join(company_link(t) for t in L['haeuser'][:6])}</div></div></div></section>'''
    process = f'<section class="x-process x-section" id="ablauf"><div class="x-shell"><p class="x-label" data-reveal>{C["process_label"]}</p><h2 data-reveal>{heading(C["process_title"])}</h2><div class="x-process-grid">'+''.join(f'<article data-reveal><span class="x-process-number">0{i+1}</span><h3>{t}</h3><p>{b}</p></article>' for i,(t,b) in enumerate(C['process']))+'</div></div></section>'
    faq = f'<section class="x-faq x-section"><div class="x-shell x-faq-grid"><div><p class="x-label" data-reveal>{C["faq_label"]}</p><h2 data-reveal>{C["faq_title"]}</h2><span class="x-faq-star" aria-hidden="true">✳</span></div><div>'+''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{answer}</p></details>' for q,answer in L['faq'][:6])+'</div></div></section>'
    closing = f'<section class="x-closing x-section" id="kontakt"><div class="x-shell"><p class="x-label" data-reveal>{C["cta_label"]}</p><div class="x-closing-grid"><h2 data-reveal>{heading(C["cta_title"])}</h2><div data-reveal><div class="x-closing-arrow" aria-hidden="true">↗</div><p>{C["cta_text"]}</p><a class="x-button x-button-dark" href="{a("kontakt.html")}">{C["cta_button"]}{ARROW}</a><small>{C["cta_note"]}</small></div></div></div></section>'
    footlinks = ''.join(f'<a href="{a(h)}">{t}</a>' for h,t in L['foot_l1'])
    footer = f'<footer class="x-footer"><div class="x-shell"><div class="x-footer-top"><a class="tafolli-brand-link" href="{home}" aria-label="Kastriot Tafolli">{lockup("../" if L["dir"] else "")}</a><p class="x-label">{C["footer_tag"]}</p><a href="#top" class="x-back-top">{C["top"]} ↑</a></div><div class="x-footer-links">{footlinks}</div><div class="x-footer-contact"><a href="mailto:info@tafolli.net">info@tafolli.net ↗</a><a href="tel:+4917664616146">+49 176 64616146</a><span>Deutschland · Österreich · Schweiz · Kosovo</span></div><div class="x-footer-bottom"><span>© 2026 Kastriot Tafolli · TB Solutions</span><div><a href="{a("impressum.html")}">{L["foot_impressum"]}</a><a href="{a("datenschutz.html")}">{L["foot_datenschutz"]}</a></div><span>MADE WITH INTENTION. ✳</span></div></div></footer>'
    config = json.dumps({k:C[k] for k in ['demos','stages','stage_notes','ready','run','running','replay','roi_units']},ensure_ascii=False).replace('<','\\u003c')
    schema = structured(current,title,C['description'],L['code'])
    return f'''<!doctype html><html lang="{L['code']}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{html.escape(C['description'])}"><meta name="author" content="Kastriot Tafolli"><link rel="canonical" href="{canonical}">{alternatives}
<meta property="og:type" content="website"><meta property="og:site_name" content="Kastriot Tafolli"><meta property="og:locale" content="{L['locale']}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(C['description'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://tafolli.net/assets/social-preview.png"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#f3f1e9">
<link rel="icon" type="image/svg+xml" href="{a('assets/brand/favicon.svg')}"><link rel="apple-touch-icon" href="{a('assets/brand/apple-touch-icon.png')}"><link rel="preload" as="image" href="{a('assets/brand/logo-mark.webp')}" fetchpriority="high"><link rel="preload" as="font" type="font/woff2" href="{a('assets/schriften/space-grotesk-var.woff2')}" crossorigin><link rel="preload" as="font" type="font/woff2" href="{a('assets/schriften/ibm-plex-sans-400.woff2')}" crossorigin><link rel="preload" as="font" type="font/woff2" href="{a('assets/schriften/bodoni-moda-400-italic.woff2')}" crossorigin><link rel="stylesheet" href="{a('assets/schriften.css')}?v={version}"><link rel="stylesheet" href="{a('assets/experience.css')}?v={version}">{schema}</head>
<body class="experience{' service-detail' if detail else ''}"><a href="#inhalt" class="x-skip">{L['skip']}</a><div class="x-progress" aria-hidden="true"></div>{intro(L["code"], "../" if L["dir"] else "")}
<header class="x-header site-header"><div class="x-shell x-header-inner"><a class="tafolli-brand-link" href="{home}" aria-label="Kastriot Tafolli">{lockup("../" if L["dir"] else "")}</a>{nav}<div class="x-header-controls site-header-controls"><nav class="x-languages" aria-label="Sprache / Language / Gjuha">{languages}</nav><button class="x-motion" type="button" aria-pressed="false" aria-label="{C['motion']}"><span aria-hidden="true">Ⅱ</span><span class="x-motion-label">{C['motion']}</span></button>{nav_toggle(L['code'])}</div></div></header>
<main id="inhalt">{breadcrumbs(current) if detail else ""}{hero}{(story+lab+care+roi+services+bio+region(service="KI-Automatisierung als Service")+process+faq) if detail else (partner_strip(L['code'], '../' if L['dir'] else '')+manifesto+services+bio+region(L["code"], "../" if L["dir"] else "")+lab)}{closing}</main>{footer}
<noscript><style>.x-tabs,.x-demo-control,.x-motion,.x-roi-grid{{display:none}}.x-nav{{display:flex;flex-wrap:wrap}}.x-header-inner{{height:auto;min-height:88px;flex-wrap:wrap;padding-block:15px}}</style><p class="x-shell">{C['demo_hint']}</p></noscript>
<script type="application/json" id="experience-config">{config}</script><script src="{a('assets/navigation.js')}?v={version}" defer></script><script src="{a('assets/brand.js')}?v={version}" defer></script><script src="{a('assets/experience.js')}?v={version}" defer></script><script src="{a('assets/partners.js')}?v={version}" defer></script></body></html>'''

def build():
    for L in LANGUAGES:
        target = ROOT / (L['dir']+'/index.html' if L['dir'] else 'index.html')
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(iconize(page(L)))
        print(f'  {target.relative_to(ROOT)} [{L["name"]}]')
    (ROOT/'ki-automatisierung.html').write_text(iconize(page(DE,detail=True)))
    print('  ki-automatisierung.html [Deutsch]')

if __name__ == '__main__':
    build()
