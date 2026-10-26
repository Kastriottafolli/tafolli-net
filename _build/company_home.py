"""Company homepage: spacious product presentation, original service visuals."""
import hashlib
from html import escape
from pathlib import Path
from brand import instagram_link, lockup, MARK, FAVICON, TOUCH_ICON
from navigation import nav, toggle
from seo import structured
from company_content import HOME
from apple_content import APPLE
from content_refresh import content
from partners import strip as partner_strip
import work
from agency import art
from planner import section as planner_section
from presence import section as presence_section
from boosty import widget as boosty_widget

ROOT=Path(__file__).resolve().parent.parent
LANGUAGES=[('de','','Deutsch','de_DE'),('en','en','English','en_GB'),('sq','sq','Shqip','sq_AL')]
ARROW='<span aria-hidden="true">↗</span>'
CHEVRON='<span aria-hidden="true">›</span>'

def page(lang):
    C,P,E=content(lang,HOME[lang],APPLE[lang])
    _,folder,_,locale=next(L for L in LANGUAGES if L[0]==lang)
    base='../' if folder else ''
    current=folder+'/' if folder else 'index.html'
    home='/'+(folder+'/' if folder else '')
    canonical='https://tafolli.net/'+(folder+'/' if folder else '')
    e=escape
    a=lambda path:base+path
    css=['kt.css','experience.css','corporate.css','company.css','motion.css','creative.css','agency.css','boosty.css','planner.css','planner-studio.css']
    assets=css+['navigation.js','motion.js','creative.js','partners.js','boosty.js','planner.js','planner-model.mjs','planner-catalog.mjs','form-delivery.mjs']
    version=hashlib.sha256(b''.join((ROOT/'assets'/name).read_bytes() for name in assets)).hexdigest()[:10]
    styles=''.join(f'<link rel="stylesheet" href="{a("assets/"+name)}?v={version}">' for name in ['schriften.css',*css])
    alternates=''.join(f'<link rel="alternate" hreflang="{code}" href="https://tafolli.net/{directory+"/" if directory else ""}">' for code,directory,_,_ in LANGUAGES)
    languages=''.join(f'<a href="/{directory+"/" if directory else ""}" lang="{code}" hreflang="{code}" aria-label="{name}"'+(' aria-current="page"' if code==lang else '')+f'>{code.upper()}</a>' for code,directory,name,_ in LANGUAGES)
    anchors=['marketing','technology','consulting','automation']
    service_cards=''
    quicklinks=''
    for i,(copy,service) in enumerate(zip(P['service_cards'],C['services'])):
        related=''.join(f'<li><a href="{a(href)}">{e(label)}</a></li>' for href,label in E['details'][i])
        service_cards+=f'''<article class="c-service c-service-{anchors[i]}" id="{anchors[i]}"><div class="c-service-copy"><h3>{e(copy['name'])}</h3><p class="c-service-title">{e(copy['headline'])}</p><p class="c-service-description">{e(copy['text'])}</p><a class="c-text-link" href="{a(service['href'])}">{e(copy['cta'])}{CHEVRON}</a><ul class="c-service-links" aria-label="{e(E['details_label'])}">{related}</ul></div>{art(['marketing','technology','consulting','ai'][i],base)}</article>'''
        quicklinks+=f'<a href="#{anchors[i]}">{e(copy["name"])}</a>'
    process=''.join(f'<article><span class="c-step">0{i+1}</span><h3>{e(item["title"])}</h3><p>{e(item["text"])}</p></article>' for i,item in enumerate(P['process']))
    faq=''.join(f'<details><summary>{e(q)}<span aria-hidden="true">+</span></summary><p>{e(answer)}</p></details>' for q,answer in C['faq'])
    footer_services=''.join(f'<a href="{a(s["href"])}">{e(s["name"])}</a>' for s in C['services'])
    company_links={'de':[('ueber-mich.html','Unternehmen'),('referenzen.html','Referenzen & Netzwerk'),('wissen.html','Wissen'),('kontakt.html','Kontakt')],'en':[('ueber-mich.html','Company'),('referenzen.html','References & network'),('wissen.html','Insights'),('kontakt.html','Contact')],'sq':[('ueber-mich.html','Kompania'),('referenzen.html','Referenca & rrjeti'),('wissen.html','Njohuri'),('kontakt.html','Kontakt')]}[lang]
    footer_company=''.join(f'<a href="{a(h)}">{e(t)}</a>' for h,t in company_links)
    skip={'de':'Zum Inhalt springen','en':'Skip to content','sq':'Kaloni te përmbajtja'}[lang]
    legal={'de':['Impressum','Datenschutz'],'en':['Legal notice','Privacy'],'sq':['Të dhënat ligjore','Privatësia']}[lang]
    illustration={'de':'Gestaltungsbeispiel: Webanwendung und mobile App.','en':'Design concept: web application and mobile app.','sq':'Koncept dizajni: aplikacion web dhe aplikacion mobil.'}[lang]
    tech_links=['softwareentwicklung.html','webdesign.html','app-entwicklung.html','cybersecurity.html']
    tech_items=''.join(f'<a href="{a(link)}">{e(label)}{CHEVRON}</a>' for label,link in zip(P['technology_items'],tech_links))
    hero_lines=' '.join(f'<span>{e(line)}</span>' for line in P['hero_lines'])
    use_cards=''.join(f'<article><h3>{e(title)}</h3><p>{e(text)}</p><a class="c-text-link" href="{a(href)}">{e(label)}{CHEVRON}</a></article>' for title,text,href,label in E['use_cases'])
    use_cases=f'<section class="c-use-cases c-section" id="anwendungen"><div class="shell"><div class="c-section-heading"><p class="c-eyebrow">{e(E["use_label"])}</p><h2>{e(E["use_title"])}</h2></div><div class="c-use-grid">{use_cards}</div></div></section>'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(C['title'])}</title><meta name="description" content="{e(C['description'])}"><meta name="author" content="Tafolli &amp; Co."><link rel="canonical" href="{canonical}">{alternates}<link rel="alternate" hreflang="x-default" href="https://tafolli.net/">
<meta property="og:type" content="website"><meta property="og:site_name" content="Tafolli &amp; Co."><meta property="og:locale" content="{locale}"><meta property="og:title" content="{e(C['title'])}"><meta property="og:description" content="{e(C['description'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://tafolli.net/assets/social-preview.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{e(C['title'])}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image:alt" content="{e(C['title'])}"><meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/svg+xml" href="{a(FAVICON)}"><link rel="apple-touch-icon" href="{a(TOUCH_ICON)}"><link rel="preload" as="image" href="{a(MARK)}" fetchpriority="high"><link rel="preload" as="image" href="{a('assets/work/tafolli-boost-desktop.webp')}" fetchpriority="high">{styles}{structured(current,C['title'],C['description'],lang)}</head>
<body class="company-site"><a class="c-skip" href="#inhalt">{skip}</a>
<header class="bar site-header"><div class="shell bar-in"><a class="tafolli-brand-link" href="{home}" aria-label="Tafolli &amp; Co.">{lockup(base)}</a>{nav(current,base,lang)}<div class="site-header-controls"><nav class="lang" aria-label="Sprache / Language / Gjuha">{languages}</nav>{instagram_link(lang)}<a class="btn btn-1 site-talk" href="{a('kontakt.html')}">{e(C['primary'])}</a>{toggle(lang)}</div></div></header>
<main id="inhalt">
<section class="c-hero" id="top"><div class="c-hero-copy"><div class="c-hero-brand" role="img" aria-label="Tafolli &amp; Co.">{lockup(base)}</div><h1>{hero_lines}</h1><p class="c-lead">{e(P['hero_text'])}</p><div class="c-actions"><a class="btn btn-1" href="{a('kontakt.html')}#projektanfrage">{ {'de':'Projekt besprechen','en':'Discuss your project','sq':'Diskutoni projektin'}[lang] }</a><a class="btn btn-2" href="#leistungen">{ {'de':'Leistungen entdecken','en':'Explore our services','sq':'Shihni shërbimet'}[lang] }</a></div></div>{work.scene(lang,base)}<nav class="c-quicklinks" aria-label="{e(P['services_label'])}">{quicklinks}</nav></section>
{partner_strip(lang,base)}
{presence_section(lang,base)}
<section class="c-services-section" id="leistungen"><div class="c-section-heading"><p class="c-eyebrow">{e(P['services_label'])}</p><h2>{e(P['services_title'])}</h2></div><div class="c-services-grid">{service_cards}</div></section>
{work.boost(lang,base)}
{planner_section(lang,base)}
<section class="c-approach c-section" id="ablauf"><div class="shell"><div class="c-section-heading"><h2>{e(P['approach_title'])}</h2><p>{e(P['approach_text'])}</p></div><div class="c-process-grid">{process}</div><a class="c-text-link c-company-link" href="{a('ueber-mich.html')}">{e(C['company_link'])}{CHEVRON}</a></div></section>
<section class="c-faq c-section"><div class="shell c-faq-grid"><div><p class="c-eyebrow">{e(C['faq_label'])}</p><h2>{e(C['faq_title'])}</h2></div><div>{faq}</div></div></section>
<section class="c-contact c-section" id="kontakt"><div class="shell"><h2>{e(P['contact_title'])}</h2><p>{e(P['contact_text'])}</p><a class="btn btn-1" href="{a('kontakt.html')}">{e(P['contact_cta'])}</a><a class="c-contact-email" href="mailto:info@tafolli.net">info@tafolli.net</a></div></section>
</main>
<footer class="c-footer"><div class="shell"><div class="c-footer-grid"><div><a class="tafolli-brand-link" href="{home}" aria-label="Tafolli &amp; Co.">{lockup(base)}</a><p>{e(C['footer_text'])}</p></div><div><h2>{e(C['footer_services'])}</h2>{footer_services}</div><div><h2>{e(C['footer_company'])}</h2>{footer_company}</div><div><h2>{e(C['footer_contact'])}</h2><a href="mailto:info@tafolli.net">info@tafolli.net</a><a href="tel:+4917664616146">+49 176 64616146</a><p>{e(C['location'])}</p></div></div><div class="c-footer-bottom"><span>© 2026 Tafolli &amp; Co.</span><div><a href="{a('impressum.html')}">{legal[0]}</a><a href="{a('datenschutz.html')}">{legal[1]}</a><a href="#top">{e(C['top'])} ↑</a></div></div></div></footer>
{boosty_widget(lang,base,current)}
<script src="{a('assets/navigation.js')}?v={version}" defer></script><script src="{a('assets/motion.js')}?v={version}" defer></script><script src="{a('assets/creative.js')}?v={version}" defer></script><script src="{a('assets/partners.js')}?v={version}" defer></script><script src="{a('assets/boosty.js')}?v={version}" defer></script><script type="module" src="{a('assets/planner.js')}?v={version}"></script></body></html>'''
