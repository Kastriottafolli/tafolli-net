"""Apply the homepage's visual language to every service and company page.

The pass replaces presentation only: offer copy, forms, reference URLs, schema,
and existing section IDs remain in the generated document.
"""
from dataclasses import dataclass,field
from hashlib import sha256
from html import escape,unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import re
from detail_catalog import PAGES
from detail_art import scene,glyph
from pricing import CATALOG

@dataclass
class Element:
    tag:str
    start:int
    open_end:int
    attrs:dict
    parent:object=None
    children:list=field(default_factory=list)
    end:int=0
    close_start:int=0

    def has(self,name):return name in self.attrs.get('class','').split()
    def inside(self,node):
        parent=self.parent
        while parent:
            if parent is node:return True
            parent=parent.parent
        return False

class Document(HTMLParser):
    VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self,text):
        super().__init__(convert_charrefs=False)
        self.text=text;self.offsets=[0]+[m.end() for m in re.finditer('\n',text)]
        self.elements=[];self.stack=[];self.feed(text)
    def position(self):line,col=self.getpos();return self.offsets[line-1]+col
    def handle_starttag(self,tag,attrs):
        start=self.position();node=Element(tag,start,start+len(self.get_starttag_text()),dict(attrs),self.stack[-1] if self.stack else None)
        if node.parent:node.parent.children.append(node)
        self.elements.append(node)
        if tag not in self.VOID:self.stack.append(node)
        else:node.end=node.open_end;node.close_start=node.open_end
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if self.stack and self.stack[-1].tag==tag:
            node=self.stack.pop();node.end=node.open_end;node.close_start=node.open_end
    def handle_endtag(self,tag):
        for index in range(len(self.stack)-1,-1,-1):
            if self.stack[index].tag==tag:
                node=self.stack[index];node.close_start=self.position();node.end=self.text.find('>',node.close_start)+1
                del self.stack[index:];break
    def inner(self,node):return self.text[node.open_end:node.close_start]
    def outer(self,node):return self.text[node.start:node.end]

def text(markup):return ' '.join(unescape(re.sub('<[^>]+>',' ',markup)).split())

def top_sections(doc):
    main=next(node for node in doc.elements if node.tag=='main')
    return [node for node in doc.elements if node.tag=='section' and node.inside(main) and not any(parent.tag=='section' for parent in ancestors(node))]

def ancestors(node):
    parent=node.parent
    while parent:yield parent;parent=parent.parent

def patch(source,edits):
    for start,end,replacement in sorted(edits,reverse=True):source=source[:start]+replacement+source[end:]
    return source

def prefix_assets(markup,base):
    return markup.replace('src="assets/','src="'+base+'assets/').replace('href="assets/','href="'+base+'assets/') if base else markup

PALETTES={
 'brand':('50 94 177','#edf3ff'),'social':('139 81 137','#f6eff7'),
 'photo':('64 86 114','#eef2f7'),'security':('37 115 119','#eaf4f3'),
 'automation':('103 87 188','#f0effc'),'knowledge':('77 99 170','#edf1fa'),
 'health':('48 128 124','#edf7f4'),'product':('94 101 189','#f0f2fd'),
 'strategy':('126 98 69','#f6f1e9'),'procurement':('120 102 75','#f7f3ed'),
 'contracts':('97 104 135','#f1f2f8'),'rebate':('62 123 103','#edf6f0'),
 'costs':('62 114 99','#eef5f1'),'inventory':('89 109 130','#edf2f6'),
 'leadership':('122 94 83','#f6f0ec'),'analytics':('58 113 137','#edf4f8'),
 'people':('123 92 142','#f5f0f8'),'local':('37 117 143','#edf6f8'),
 'contact':('46 99 159','#eef4fc'),'career':('95 110 129','#eff2f6'),
 'translation':('96 103 170','#f0f1fc'),
}

def enquiry(config,base):
    if config['path']=='kontakt.html':return '#projektanfrage'
    family='marketing' if config['kind'] in {'brand','browser','landing','search','local','social','photo','craft','calendar','translation','maintenance','commerce'} else 'ai' if config['kind'] in {'automation','knowledge','health','product'} else 'consulting' if config['kind'] in {'strategy','procurement','contracts','rebate','costs','inventory','leadership','analytics','people','company','career','network'} else 'technology'
    return base+'kontakt.html?thema='+family+'&amp;leistung='+quote(config['label'].title())+'#projektanfrage'

def budget_badge(path):
    project={'landingpage-erstellen-lassen.html':'landing','webdesign.html':'landing','onlineshop.html':'shop','onlineshop-kleine-haendler.html':'shop'}.get(path)
    if project:
        item=next(t for t in CATALOG['websiteTypes'] if t['id']==project)
        return ('Landingpage ' if path=='webdesign.html' else '')+'ca. '+f'{item["min"]:,}'.replace(',','.')+' €'
    return {'suchmaschinenoptimierung.html':'SEO & Inhalte ab 450 € / Monat','firmenprofile.html':'Betreuung ab 550 € / Monat','website-pflege.html':'99 · 199 · 299 € / Monat','website-pflege-kleine-betriebe.html':'Pflege ab 99 € / Monat'}.get(path,'')

def hero(config,base,old_ids,first_anchor):
    sq=config['lang']=='sq';kind=config['kind']
    topics=config['topics'];heading='<br>'.join('<span>'+escape(line)+'</span>' for line in config['lines'])
    toggles=''.join(f'<button type="button" data-detail-focus="{i}" aria-pressed="{str(i==0).lower()}" aria-describedby="detail-scene-note">{escape(name)}</button>' for i,(name,_) in enumerate(topics))
    notes=''.join(f'<p data-detail-note="{i}"{(" hidden" if i else "")}>{escape(note)}</p>' for i,(_,note) in enumerate(topics))
    secondary='Zbuloni më shumë' if sq else 'Mehr erfahren'
    pause='Ndaloni animacionin' if sq else 'Animation pausieren';play='Luani animacionin' if sq else 'Animation abspielen'
    budget=budget_badge(config['path'])
    badge=f'<a class="detail-budget" href="{base}preisrechner.html#budgetplaner">{escape(budget)} {glyph("arrow")}</a>' if budget else ''
    proof=f'<a class="detail-proof" href="https://tafolliboost.com/" target="_blank" rel="noopener noreferrer">Eigenes Produkt: Tafolli Boost {glyph("arrow")}</a>' if config['path']=='softwareentwicklung.html' else ''
    anchors=''.join(f'<span id="{escape(name,quote=True)}" class="detail-anchor" aria-hidden="true"></span>' for name in old_ids)
    return f'''<section class="detail-hero" data-detail-hero>{anchors}<div class="shell detail-hero-grid"><div class="detail-hero-copy"><p class="detail-eyebrow"><span></span>{escape(config['label'])}</p><h1>{heading}</h1><p class="detail-lead">{escape(config['intro'])}</p><div class="detail-actions"><a class="btn btn-1" href="{enquiry(config,base)}">{escape(config['cta'])} {glyph('arrow')}</a><a class="detail-secondary" href="#{first_anchor}">{secondary} {glyph('arrow')}</a></div>{badge}{proof}<div class="detail-hero-foot"><span>TAFOLLI &amp; CO.</span><span>{'NGA IDEJA TE REALIZIMI' if sq else 'VON DER IDEE BIS ZUR UMSETZUNG'}</span></div></div><figure class="detail-scene" data-detail-scene data-focus="0"><div class="detail-scene-topline"><span>{'KONCEPT VIZUAL' if sq else 'VISUELLER EINBLICK'}</span><button type="button" class="detail-motion" data-motion-toggle data-play="{play}" data-pause="{pause}" aria-pressed="false" hidden><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3v10M11 3v10"/></svg><span>{pause}</span></button></div>{scene(config)}<div class="detail-scene-controls" role="group" aria-label="{'Zgjidhni pamjen e konceptit' if sq else 'Konzeptansicht auswählen'}">{toggles}</div><figcaption id="detail-scene-note"><small>{'ILUSTRIM' if sq else 'KONZEPTDARSTELLUNG'}</small>{notes}</figcaption></figure></div></section>'''

def route(config):
    steps=''.join(f'<li><span>0{i+1}</span><strong>{escape(label)}</strong>{glyph("arrow") if i<len(config["flow"])-1 else glyph("check")}</li>' for i,label in enumerate(config['flow']))
    return '<div class="detail-route"><div class="shell"><p>'+('NË NJË VËSHTRIM' if config['lang']=='sq' else 'IM ZUSAMMENHANG')+'</p><ol>'+steps+'</ol></div></div>'

def explorer(config,doc,module):
    articles=[n for n in doc.elements if n.tag=='article' and n.inside(module)]
    if not articles:return doc.outer(module)
    tabs=[];panels=[];module_labels=[]
    for i,article in enumerate(articles):
        h=next(n for n in doc.elements if n.tag=='h3' and n.inside(article))
        title=text(doc.inner(h));label=title
        for separator in [' und ',' & ',':',',']:
            candidate=title.split(separator)[0]
            if 7<=len(candidate)<=29:label=candidate;break
        if len(label)>32:label=label[:32].rsplit(' ',1)[0]+'…'
        module_labels.append(label)
        tabs.append(f'<button id="detail-tab-{i}" type="button" role="tab" aria-label="{escape(title,quote=True)}" aria-selected="{str(i==0).lower()}" aria-controls="detail-panel-{i}" tabindex="{0 if i==0 else -1}">{escape(label)}<span>0{i+1}</span></button>')
        inner=doc.inner(article)
        inner=re.sub(r'^\s*<span class="tag">.*?</span>','',inner,flags=re.S)
        panels.append(f'<article id="detail-panel-{i}" class="detail-tabpanel" role="tabpanel" aria-labelledby="detail-tab-{i}" tabindex="0" data-explorer-panel="{i}"><p class="detail-panel-kicker">0{i+1} / {escape(config["label"])}</p>{inner}</article>')
    diagram=''.join(f'<div class="dx-step"><i>{glyph("document" if i==0 else "code" if i==1 else "check" if i==3 else "spark")}</i><span>{escape(label)}</span></div>' for i,label in enumerate(module_labels))
    return f'<div class="detail-explorer" data-detail-explorer><div class="detail-tablist" role="tablist" aria-label="Leistungsbaustein auswählen">{"".join(tabs)}</div><div class="detail-explorer-grid"><div class="detail-explorer-art" aria-hidden="true"><div class="dx-orbit"></div><div class="dx-symbol">{glyph("shield" if config["kind"]=="security" else "chart" if config["kind"] in {"analytics","rebate","costs"} else "code" if config["kind"] in {"software","app","webapp"} else "spark")}</div><div class="dx-diagram" style="--detail-modules:{len(module_labels)}">{diagram}</div><span class="dx-caption">LEISTUNGSBAUSTEINE / IM ZUSAMMENSPIEL</span></div><div class="detail-panel-stack">{"".join(panels)}</div></div></div>'

def apply_page(source,config,version):
    path=config['path'];base='../' if '/' in path else ''
    kind=config['kind'];palette,tint=PALETTES.get(kind,('43 103 187','#eef4fc'))
    if kind!='planner':
        doc=Document(source);sections=top_sections(doc);old_hero=sections[0]
        old_ids=[n.attrs['id'] for n in doc.elements if (n is old_hero or n.inside(old_hero)) and n.attrs.get('id')]
        body_sections=sections[1:]
        first_anchor=next((n.attrs['id'] for n in body_sections if n.attrs.get('id')), 'detail-inhalt')
        if body_sections and not body_sections[0].attrs.get('id'):
            first_anchor='detail-inhalt'
        new_hero=hero(config,base,old_ids,first_anchor)+route(config)
        edits=[(old_hero.start,old_hero.end,prefix_assets(new_hero,base))]
        for section in body_sections:
            if section.has('mini-calculation') or section.has('workflow-section'):
                edits.append((section.start,section.end,''))
        for module in [n for n in doc.elements if n.has('service-modules')]:
            if not module.inside(old_hero):edits.append((module.start,module.end,explorer(config,doc,module)))
        source=patch(source,edits)
        # Stable IDs make every visual chapter reachable without JavaScript.
        doc=Document(source);sections=top_sections(doc)[1:];edits=[];chapters=[]
        for i,section in enumerate(sections):
            identity=section.attrs.get('id') or ('detail-inhalt' if i==0 else f'detail-kapitel-{i+1}')
            if not section.attrs.get('id'):
                opening=source[section.start:section.open_end]
                edits.append((section.start,section.open_end,opening[:-1]+' id="'+identity+'">'))
            title_node=next((n for n in doc.elements if n.tag=='h2' and n.inside(section)),None)
            if title_node:chapters.append((identity,text(doc.inner(title_node))))
        if chapters:
            choices=chapters[:5]
            links=''.join(f'<a href="#{identity}" data-detail-chapter><span>0{i+1}</span>{escape(label)}</a>' for i,(identity,label) in enumerate(choices))
            nav='<nav class="detail-chapters" aria-label="'+('Në këtë faqe' if config['lang']=='sq' else 'Auf dieser Seite')+'"><div class="shell">'+links+'</div></nav>'
            hero_section=top_sections(doc)[0]
            # Insert after the route; it is outside the section hierarchy.
            route_end=source.find('</ol></div></div>',hero_section.end)
            insertion=route_end+len('</ol></div></div>') if route_end>=0 else hero_section.end
            edits.append((insertion,insertion,nav))
        source=patch(source,edits)
        # Each timeline stop gets a real anchor rather than a simulated result.
        if kind=='career':
            doc=Document(source);items=[n for n in doc.elements if n.has('tl-item')];edits=[];years=[]
            for i,item in enumerate(items):
                y=next((n for n in doc.elements if n.has('tl-jahr') and n.inside(item)),None)
                if not y:continue
                name='berufsstation-'+str(i+1);opening=source[item.start:item.open_end]
                edits.append((item.start,item.open_end,opening[:-1]+f' id="{name}">'));years.append((name,text(doc.inner(y))))
            timeline=next((n for n in doc.elements if n.has('timeline')),None)
            if timeline:
                nav='<nav class="detail-year-nav" aria-label="Berufliche Station auswählen">'+''.join(f'<a href="#{name}">{escape(year)}</a>' for name,year in years)+'</nav>'
                edits.append((timeline.start,timeline.start,nav))
            source=patch(source,edits)
        # A contextual map belongs beside the actual local-profile content.
        if path=='suchmaschinenoptimierung.html':
            local=PAGES['firmenprofile.html'];art=prefix_assets(scene(local),base)
            source=source.replace('<div class="local-platforms">','<div class="detail-local-map" data-detail-static-scene>'+art+'</div><div class="local-platforms">',1)
    def body(match):
        classes=match.group(1)
        return f'<body class="{classes} detail-page" data-detail-page="{escape(path,quote=True)}" data-detail-kind="{kind}" style="--detail-accent:{palette};--detail-tint:{tint}">'
    source=re.sub(r'<body class="([^"]+)">',body,source,count=1)
    source=source.replace('</head>',f'<link rel="stylesheet" href="{base}assets/detail.css?v={version}"></head>',1)
    source=source.replace('</body>',f'<script src="{base}assets/detail.js?v={version}" defer></script><noscript><style>.detail-scene-controls,.detail-tablist,.detail-motion{{display:none!important}}.detail-tabpanel{{display:block!important}}</style></noscript></body>',1)
    return source

def build(root):
    version=sha256((root/'assets/detail.css').read_bytes()+(root/'assets/detail.js').read_bytes()).hexdigest()[:10]
    from icons import iconize
    for path,config in PAGES.items():
        target=root/(path+'index.html' if path.endswith('/') else path)
        target.write_text(iconize(apply_page(target.read_text(),config,version)))
    print(f'  Visual detail design: {len(PAGES)} pages, individual subjects and motion.')
