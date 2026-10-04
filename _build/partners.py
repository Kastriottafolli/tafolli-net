"""Shared references and partner identity. Brand sources live beside local assets."""
import html, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
SOURCES=json.loads((ROOT/'assets/partners/sources.json').read_text())

def brand(key,name,url,field,mono=False):
    return dict(key=key,name=name,url=url,field=field,mono=mono)
PROJECTS=[
 brand('tafolli-glass','Tafolli Glass','https://www.tafolliglass.net/','Glas & Gestaltung',True),
 brand('ab-bau','A&B Bau','https://www.ab-bau23.de/','Bau & Sanierung'),
 brand('wochenmarkt','Restaurant Wochenmarkt','https://www.restaurant-wochenmarkt.de/','Gastronomie · Binz'),
 brand('mel-maler','MEL · wir renovieren','https://www.mel-maler.de/','Malerarbeiten & Renovierung'),
 brand('panorama','Panorama Hotel Lohme','https://www.panorama-hotel-lohme.de/','Hotellerie · Rügen'),
 brand('tafolli','Kastriot Tafolli','https://www.tafolli.net/','Eigener digitaler Auftritt'),
]
GASTRO=[
 brand('krombacher','Krombacher','https://www.krombacher.de/','Bier & Brauereien'),
 brand('bitburger','Bitburger','https://www.bitburger.de/','Bier & Brauereien'),
 brand('heineken','Heineken','https://www.heineken.com/de/de/','Bier & Brauereien',True),
 brand('jaegermeister','Jägermeister','https://de.jagermeister.com/','Spirituosen'),
 brand('campari','Campari Deutschland','https://www.campari.com/de-de/','Spirituosen & Aperitif',True),
 brand('nordmann','Getränke Nordmann','https://getraenke-nordmann.de/','Getränkegroßhandel',True),
 brand('chefs-culinar','CHEFS CULINAR','https://www.chefsculinar.de/','Gastronomie & Großhandel'),
 brand('ruegen-cash-carry','Rügen C&C','https://ruegencc-webshop.de/login/','Gastronomie & Großhandel'),
 brand('pernod-ricard','Pernod Ricard','https://www.pernod-ricard.com/en/locations/germany','Spirituosen'),
 brand('fachingen','Staatlich Fachingen','https://www.fachingen.de/','Mineralwasser'),
 brand('melitta','Melitta','https://www.melitta.de/','Kaffee'),
 brand('monin','MONIN','https://monin1912.com/','Sirup & Bar'),
 brand('mionetto','Mionetto','https://de.mionetto.com/','Prosecco & Wein'),
 brand('granini','granini','https://www.granini.de/','Säfte & Fruchtgetränke'),
 brand('bauer','Bauer Fruchtsaft','https://www.bauer-fruchtsaft.de/','Säfte & Fruchtgetränke'),
 brand('coca-cola','Coca-Cola','https://www.coca-cola.com/de/de','Erfrischungsgetränke'),
 brand('schweppes','Schweppes','https://www.schweppes.de/','Mixer & Bar'),
 brand('rauch','RAUCH','https://www.rauch.cc/de/','Säfte & Fruchtgetränke'),
 brand('red-bull','Red Bull','https://www.redbull.com/de-de/','Energy Drinks'),
]
TECH=[
 brand('google','Google','https://about.google/','Suche & digitale Sichtbarkeit'),
 brand('meta','Meta','https://about.meta.com/','Social Media & Kampagnen'),
 brand('apple','Apple','https://www.apple.com/de/','Geräte & Ökosystem'),
 brand('android','Android','https://www.android.com/intl/de_de/','Mobile Anwendungen'),
 brand('openai','OpenAI','https://openai.com/','KI & Sprachmodelle'),
 brand('anthropic','Anthropic','https://www.anthropic.com/','KI & Sprachmodelle'),
 brand('grok','Grok','https://grok.com/','KI & Recherche'),
 brand('microsoft','Microsoft','https://www.microsoft.com/de-de/','Produktivität & Cloud'),
 brand('squarespace','Squarespace','https://www.squarespace.com/','Websites & Content',True),
 brand('dreamhost','DreamHost','https://www.dreamhost.com/','Hosting & Infrastruktur',True),
]
ALL={p['key']:p for p in PROJECTS+GASTRO+TECH}


def logo(p,base=''):
    if p['key']=='tafolli':return '<span class="partner-own-logo" aria-hidden="true">TAFOLLI<span>✳</span></span>'
    filename=SOURCES[p['key']]['file']
    return f'<img class="partner-logo{ " partner-logo-mono" if p["mono"] else ""} partner-logo-{p["key"]}" src="{base}assets/partners/{filename}" width="240" height="96" alt="" loading="lazy" decoding="async">'


def tiles(items,projects=False):
    cards=[]
    for i,p in enumerate(items):
        tag='PARTNER' if p['key']=='tafolli-glass' else 'EIGENER AUFTRITT' if p['key']=='tafolli' else f'0{i+1} / WEBSITE'
        domain=p['url'].split('/')[2].removeprefix('www.')
        cards.append(f'''<a class="partner-card{' partner-project' if projects else ''}" href="{html.escape(p['url'])}" target="_blank" rel="noopener noreferrer"><div class="partner-card-top"><span>{tag if projects else html.escape(p['field'])}</span><span aria-hidden="true">↗</span></div><div class="partner-logo-stage">{logo(p)}</div><div class="partner-card-bottom"><h3>{html.escape(p['name'])}</h3><span>{domain if projects else 'Website entdecken'}</span></div></a>''')
    return '<div class="partner-grid'+(' partner-project-grid' if projects else '')+'">'+''.join(cards)+'</div>'


def strip(lang,base=''):
    copy={
      'de':['REFERENZEN & PARTNER','Gute Arbeit verbindet.','Einblicke in mein Netzwerk aus Betrieben, Gastronomie und Technologie.','Alle Referenzen & Partner','Logo-Slider pausieren','Logo-Slider abspielen'],
      'en':['REFERENCES & PARTNERS','Good work connects.','A glimpse of my network across businesses, hospitality and technology.','All references & partners','Pause logo slider','Play logo slider'],
      'sq':['REFERENCA & PARTNERË','Puna e mirë na lidh.','Një vështrim në rrjetin tim të bizneseve, gastronomisë dhe teknologjisë.','Të gjitha referencat & partnerët','Ndaloni rrëshqitjen e logove','Luani rrëshqitjen e logove'],
    }[lang]
    keys=['tafolli-glass','ab-bau','wochenmarkt','panorama','krombacher','nordmann','chefs-culinar','openai','anthropic','google','microsoft','mel-maler']
    cards=''.join(f'<li><a href="{html.escape(ALL[key]["url"])}" target="_blank" rel="noopener noreferrer" aria-label="{html.escape(ALL[key]["name"])}">{logo(ALL[key],base)}<span class="partner-slider-name">{html.escape(ALL[key]["name"])}</span></a></li>' for key in keys)
    return f'''<section class="partner-strip" id="partner" data-partner-slider aria-label="{copy[0]}" data-pause-label="{copy[4]}" data-play-label="{copy[5]}"><div class="x-shell"><div class="partner-strip-heading"><div><p class="x-label">{copy[0]}</p><h2>{copy[1]}</h2><p>{copy[2]}</p></div><div class="partner-strip-actions"><a href="{base}referenzen.html">{copy[3]} ↗</a><button type="button" class="partner-slider-pause" aria-pressed="false" aria-label="{copy[4]}" hidden><span aria-hidden="true">Ⅱ</span></button></div></div><div class="partner-slider-viewport"><ul class="partner-slider-track">{cards}</ul></div></div></section>'''
