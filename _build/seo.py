"""Page-specific search intent, shared identity and honest service coverage."""
import json
from html import escape
from navigation import TITLES, parent
from brand import NAME, MARK

ORIGIN='https://tafolli.net/'
COUNTRIES=[{'@type':'Country','name':name} for name in ['Germany','Austria','Switzerland','Kosovo']]
# Editorial intent, not keyword-volume or ranking claims.
SERVICE_META={
 'ki-automatisierung':('KI-Automatisierung & Workflows | Tafolli & Co.', 'KI-Assistenten, automatisierte Workflows und Systemanbindung für Unternehmen. Konzeption, Umsetzung und laufende Betreuung in DACH und Kosovo.'),
 'ki-entwicklung':('KI-Entwicklung & Assistenten | Tafolli & Co.','KI-Assistenten für Ihren Betrieb: eigene Wissensquellen, geprüfte Antworten und klare Freigaben. Entwicklung und Integration in DACH und Kosovo. Projekt besprechen.'),
 'teamo-ki':('TeamO: KI-Assistent für Hospitality | Tafolli & Co.', 'TeamO unterstützt Hotels und Gastronomie bei ausgewählten Anfragen und Abläufen. Funktionsumfang, Datenquellen und menschliche Freigaben werden abgestimmt.'),
 'digitalisierung':('Digitalisierung & Systemintegration | Tafolli & Co.', 'Abläufe, Fachanwendungen und Datenquellen sinnvoll verbinden. Bestandsaufnahme, Systemintegration und Einführung für Unternehmen in DACH und Kosovo.'),
 'softwareentwicklung':('Softwareentwicklung für Unternehmen | Tafolli & Co.', 'Individuelle Software, Kundenportale, Web-Apps und Schnittstellen für Ihr Unternehmen. Von der Planung bis zur Einführung. Jetzt Ihr Projekt besprechen.'),
 'app-entwicklung':('Apps für iOS, Android & Web | Tafolli & Co.', 'Mobile Anwendungen für Apple iOS und Android sowie Web-Apps. Bedienkonzept, Entwicklung, Systemanbindung und Einführung nach abgestimmten Anforderungen.'),
 'cybersecurity':('Cybersecurity & IT-Sicherheit | Tafolli & Co.', 'Anwendungen, Websites, Zugänge und Daten absichern. Bestandsaufnahme, Schutzmaßnahmen und Betriebsabläufe für Unternehmen in DACH und Kosovo.'),
 'fb-beratung':('Unternehmensberatung & F&B-Consulting | Tafolli & Co.', 'Prozesse verbessern, Einkauf strukturieren und Wirtschaftlichkeit prüfen. Unternehmensberatung mit besonderer Erfahrung in Hotellerie und Gastronomie.'),
 'lieferantenvereinbarungen':('Lieferantenvereinbarungen für Gastronomie | Tafolli & Co.','Lieferantenangebote, Konditionen und Leistungspflichten strukturiert vergleichen. Einkaufsberatung für Hotels und Gastronomie in DACH und Kosovo. Gespräch anfragen.'),
 'getraenkevertraege':('Getränkeverträge & Einkaufsberatung | Tafolli & Co.','Getränkeverträge für Hotels und Gastronomie prüfen: Preise, Bindungen, Ausstattung und Lieferleistung gemeinsam betrachten. Beratung in DACH und Kosovo anfragen.'),
 'rueckverguetungen':('Rückvergütungen im Gastronomie-Einkauf | Tafolli & Co.','Rückvergütungen und Boni nachvollziehbar machen: Bezugsgrößen, Nachweise und Abrechnung im Einkauf prüfen. Für Hotels und Gastronomie in DACH und Kosovo.'),
 'wareneinsatz-kalkulation':('Wareneinsatz & Gastronomie-Kalkulation | Tafolli & Co.','Rezepturen, Wareneinsatz und Deckungsbeiträge als Entscheidungsgrundlage nutzen. Kalkulationsberatung für Hotels und Restaurants in DACH und Kosovo. Jetzt anfragen.'),
 'inventur-warenwirtschaft':('Inventur & Warenwirtschaft für Gastronomie | Tafolli & Co.','Bestände, Bestellung und Inventur sinnvoll verbinden. Warenwirtschaft für Hotels und Gastronomie mit klaren Verantwortlichkeiten in DACH und Kosovo. Projekt besprechen.'),
 'interim-fb-management':('Interim F&B-Management für Hotels | Tafolli & Co.','F&B-Führung auf Zeit: Teams, Standards und Zahlen im Hotelbetrieb strukturieren. Einsätze in DACH und Kosovo nach abgestimmtem Auftrag und Verfügbarkeit anfragen.'),
 'revenue-controlling':('Revenue Management & F&B-Controlling | Tafolli & Co.','Budget, Forecast und Outlet-Kennzahlen für Hotels und Gastronomie nutzbar machen. Revenue- und F&B-Controlling in DACH und Kosovo. Erstgespräch vereinbaren.'),
 'personal-recruiting':('Hospitality-Recruiting & Teamentwicklung | Tafolli & Co.','Rollen, Auswahl, Onboarding und Schulung für Hotellerie und Gastronomie. Recruiting und Teamentwicklung in DACH und Kosovo. Ihren konkreten Bedarf besprechen.'),
 'online-marketing':('Marketing, SEO, Social Media & Design | Tafolli & Co.', 'Logos, Corporate Design, SEO, Social Media, Kampagnen, Websites, Visitenkarten und Flyer. Marketing von Tafolli & Co. Jetzt Ihr Projekt besprechen.'),
 'webdesign':('Website-Erstellung & Webdesign | Tafolli & Co.', 'Ihre Unternehmenswebsite: Design, Inhalte, Entwicklung und mobile Bedienung. Neue Websites, Landingpages und Relaunch mit klaren Kontaktwegen. Projekt besprechen.'),
 'suchmaschinenoptimierung':('SEO & lokale Einträge für Unternehmen | Tafolli & Co.','Suchmaschinenoptimierung und lokale Einträge: Google-Unternehmensprofil, Apple Maps, Bing Places und Verzeichnisse. Ihre Sichtbarkeit mit Tafolli & Co. verbessern.'),
 'domain-hosting-email':('Domain, Hosting & E-Mail für Betriebe | Tafolli & Co.','Domains, Hosting und professionelle E-Mail strukturiert einrichten oder umziehen. Dokumentierte Zugänge und Betreuung für DACH und Kosovo. Bedarf besprechen.'),
 'social-media':('Social-Media-Betreuung & Content | Tafolli & Co.','Social-Media-Betreuung für Unternehmen: Strategie, Redaktionsplan, Posts und Reels für Instagram, Facebook, LinkedIn und TikTok. Jetzt Betreuung besprechen.'),
 'foto-video':('Foto, Video & Unternehmensinhalte | Tafolli & Co.', 'Visuelle Inhalte für Marke, Produkte, Unternehmenskommunikation und Kampagnen. Bildkonzept, Foto und Video mit abgestimmten Formaten und Nutzungsrechten.')}
PAGE_META={
 'leistungen.html':('Marketing, Software, Beratung & KI | Tafolli & Co.','Marketing, individuelle Software und Apps, Cybersecurity, Unternehmensberatung und KI-Automatisierung. Leistungen für Unternehmen in DACH und Kosovo.'),
 'ueber-mich.html':('Unternehmen | Tafolli & Co.','Tafolli & Co. unterstützt Unternehmen in Marketing, Technology, Consulting und AI Automation. Informationen zu Angebot, Arbeitsweise und Ansprechpartner.'),
 'werdegang.html':('Werdegang: Hotellerie & KI Engineering | Tafolli & Co.','Die beruflichen Stationen von Kastriot Tafolli: Service, F&B-Leitung und operative Verantwortung, ergänzt durch Softwareentwicklung und KI Engineering. Profil entdecken.'),
 'referenzen.html':('Referenzen, Hotels & Partner | Tafolli & Co.','Tafolli Boost, Panorama Hotel Lohme, Marken und Technologieunternehmen aus bisheriger Zusammenarbeit sowie berufliche Hotelstationen. Mit direkten Website-Links.'),
 'wissen.html':('Wissen zu Hotel-KI, Einkauf & Direktbuchungen | Tafolli & Co.','Praxiswissen für Hotels und Gastronomie: KI sinnvoll einsetzen, Getränkeverträge verstehen und Direktbuchungen stärken. Ratgeber und Potenzialrechner entdecken.'),
 'rechner.html':('Hotel-Rechner: KI, Einkauf & Direktbuchungen | Tafolli & Co.','Vier interaktive Rechner zu KI-Zeitpotenzial, Portalprovisionen, Getränkeeinkauf und Social Media. Eigene Werte eingeben und Annahmen nachvollziehen. Ohne Speicherung.'),
 'wissen-ki-im-hotel.html':('KI im Hotel: Anwendungen, Grenzen & Einstieg | Tafolli & Co.','Wo KI im Hotel hilft, welche Aufgaben Freigaben brauchen und wie Sie sinnvoll starten. Praxisratgeber von Kastriot Tafolli mit passenden Leistungen und Rechner.'),
 'wissen-getraenkevertrag.html':('Getränkevertrag prüfen: Konditionen & Bindungen | Tafolli & Co.','Getränkeverträge verstehen: Einkaufspreise, Rückvergütung, Ausstattung und Laufzeit gemeinsam bewerten. Praxiswissen für Hotellerie und Gastronomie von Kastriot Tafolli.'),
 'wissen-direktbuchungen.html':('Mehr Direktbuchungen für Hotels gewinnen | Tafolli & Co.','Website, Suchmaschinen und Buchungsweg gemeinsam verbessern: So stärken Hotels ihre Direktbuchungen. Praxiswissen, Provisionsrechner und Umsetzung mit Kastriot Tafolli.'),
 'kontakt.html':('Kontakt & Beratung in DACH und Kosovo | Tafolli & Co.','KI, Software, Online-Marketing oder Beratung besprechen: Kontakt zu Tafolli & Co. für Projekte in Deutschland, Österreich, Schweiz und Kosovo.'),
 'impressum.html':('Impressum | Tafolli & Co.','Anbieterinformationen und Kontaktdaten für tafolli.net: Kastriot Tafolli, Hauptstraße 1, 18609 Ostseebad Binz. Telefon, E-Mail und Verantwortlichkeit für die Inhalte.'),
 'datenschutz.html':('Datenschutz | Tafolli & Co.','Informationen zur Datenverarbeitung auf tafolli.net: Hosting, Kontakt, lokale Schriftarten, interaktive Beispiele und Rechner. Hinweise und Kontakt zum Anbieter.')}
PAGE_META.update({slug+'.html':meta for slug,meta in SERVICE_META.items()})
from extended_meta import SERVICE_META as EXTENDED_SERVICES, PAGE_META as EXTENDED_PAGES
SERVICE_META.update(EXTENDED_SERVICES)
PAGE_META.update(EXTENDED_PAGES)

def metadata(path,title,description):return PAGE_META.get(path,(title,description))

def language_alternates(path):
 groups=[
  [('de',ORIGIN+'ki-automatisierung-kleine-unternehmen.html'),('sq',ORIGIN+'sq/automatizim-ia.html'),('x-default',ORIGIN+'ki-automatisierung-kleine-unternehmen.html')],
  [('de',ORIGIN+'angebot/'),('sq',ORIGIN+'sq/faqe-dhe-perkthime.html'),('x-default',ORIGIN+'angebot/')]
 ]
 url=ORIGIN+('angebot/' if path=='angebot/index.html' else path)
 return next((group for group in groups if any(href==url for _,href in group)),[])

def write_sitemap(root):
 """Use the actual canonical pages; dates record content work, not build times."""
 from html.parser import HTMLParser
 import xml.etree.ElementTree as ET
 ns='http://www.sitemaps.org/schemas/sitemap/0.9';xhtml='http://www.w3.org/1999/xhtml'
 ET.register_namespace('',ns);ET.register_namespace('xhtml',xhtml)
 updated={p:'2026-10-26' for p in ['index.html','en/index.html','sq/index.html','webdesign.html','social-media.html','suchmaschinenoptimierung.html','online-marketing.html','datenschutz.html']}
 class Canonical(HTMLParser):
  def __init__(self,text):super().__init__();self.url='';self.noindex=False;self.feed(text)
  def handle_starttag(self,tag,attributes):
   a=dict(attributes)
   if tag=='link' and a.get('rel')=='canonical':self.url=a.get('href','')
   if tag=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content',''):self.noindex=True
 tree=ET.Element('{'+ns+'}urlset')
 from pages import generated_pages
 files=generated_pages(root)
 for path in files:
  page=Canonical(path.read_text())
  if page.noindex or not page.url:continue
  url=ET.SubElement(tree,'{'+ns+'}url');ET.SubElement(url,'{'+ns+'}loc').text=page.url
  relative=path.relative_to(root).as_posix()
  ET.SubElement(url,'{'+ns+'}lastmod').text=updated.get(relative,'2026-10-26' if relative in EXTENDED_PAGES or relative=='angebot/index.html' else '2026-10-25')
  if relative in {'index.html','en/index.html','sq/index.html'}:
   for lang,target in [('de',''),('en','en/'),('sq','sq/'),('x-default','')]:
    ET.SubElement(url,'{'+xhtml+'}link',{'rel':'alternate','hreflang':lang,'href':ORIGIN+target})
  else:
   for lang,target in language_alternates(relative):
    ET.SubElement(url,'{'+xhtml+'}link',{'rel':'alternate','hreflang':lang,'href':target})
 ET.indent(tree,space='  ')
 ET.ElementTree(tree).write(root/'sitemap.xml',encoding='UTF-8',xml_declaration=True)

def structured(path,title,description,lang='de'):
 url=ORIGIN+('' if path=='index.html' else path)
 identity=[
  {'@type':'Organization','@id':ORIGIN+'#business','name':NAME,'url':ORIGIN,'logo':ORIGIN+MARK,'email':'info@tafolli.net','telephone':'+4917664616146','areaServed':COUNTRIES,'contactPoint':{'@type':'ContactPoint','contactType':'project enquiries','email':'info@tafolli.net','telephone':'+4917664616146','availableLanguage':['de','en','sq']}},
  {'@type':'Person','@id':ORIGIN+'#kastriot','name':'Kastriot Tafolli','url':ORIGIN+'ueber-mich.html','image':ORIGIN+'assets/bilder/kastriot-tafolli-portraet.jpg','worksFor':{'@id':ORIGIN+'#business'}},
  {'@type':'WebSite','@id':ORIGIN+'#website','name':NAME,'url':ORIGIN,'publisher':{'@id':ORIGIN+'#business'},'inLanguage':['de','en','sq']}]
 page={'@type':'WebPage','@id':url+'#page','url':url,'name':title,'description':description,'inLanguage':lang,'isPartOf':{'@id':ORIGIN+'#website'}}
 if path=='ueber-mich.html':page['@type']='AboutPage'
 if path=='kontakt.html':page['@type']='ContactPage'
 if path in ['leistungen.html','wissen.html','referenzen.html']:page['@type']='CollectionPage'
 page['about']={'@id':ORIGIN+'#business'}
 page['primaryImageOfPage']={'@type':'ImageObject','url':ORIGIN+'assets/social-preview.png','width':1200,'height':630}
 graph=identity+[page]
 if path in ['index.html','en/','sq/']:
  from company_content import HOME
  from apple_content import APPLE
  from content_refresh import content
  home,presentation,extra=content(lang,HOME[lang],APPLE[lang])
  services=[]
  for item,copy in zip(home['services'],presentation['service_cards']):
   service_url=ORIGIN+item['href']
   node={'@type':'Service','@id':service_url+'#service','name':copy['name'],'serviceType':item['title'],'url':service_url,'description':copy['text'],'provider':{'@id':ORIGIN+'#business'},'areaServed':COUNTRIES}
   graph.append(node)
   services.append({'@type':'ListItem','position':len(services)+1,'name':copy['name'],'item':{'@id':node['@id']}})
  service_list={'@type':'ItemList','@id':url+'#services','name':presentation['services_label'],'itemListElement':services}
  graph.append(service_list)
  page['mainEntity']={'@id':service_list['@id']}
 slug=path.removesuffix('.html')
 if slug in SERVICE_META:
  graph.append({'@type':'Service','@id':url+'#service','name':TITLES[path],'serviceType':TITLES[path],'url':url,'description':description,'provider':{'@id':ORIGIN+'#business'},'areaServed':COUNTRIES})
 if path.startswith('wissen-'):
  graph.append({'@type':'Article','@id':url+'#article','headline':title.split(' | ')[0],'author':{'@id':ORIGIN+'#kastriot'},'publisher':{'@id':ORIGIN+'#business'},'inLanguage':'de','mainEntityOfPage':{'@id':url+'#page'}})
 if path not in ['index.html','en/','sq/','404.html']:
  items=[('Startseite',ORIGIN)];trail=parent(path)
  if trail:items.append((trail[0],ORIGIN+trail[1]))
  items.append((TITLES.get(path,title),url))
  graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumbs','itemListElement':[{'@type':'ListItem','position':i+1,'name':name,'item':item} for i,(name,item) in enumerate(items)]})
  page['breadcrumb']={'@id':url+'#breadcrumbs'}
 return '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<','\\u003c')+'</script>'

REGION_COPY={
 'de':('NAH AM BETRIEB. ÜBER GRENZEN HINWEG.','Zusammenarbeit in DACH und Kosovo.','Unsere Leistungen bieten wir in Deutschland, Österreich, der Schweiz und Kosovo an. Analyse, Abstimmung und digitale Umsetzung sind ortsunabhängig möglich. Workshops, Foto- und Videotermine oder operative Einsätze vor Ort planen wir passend zu Ihrem Auftrag und der abgestimmten Verfügbarkeit.','Deutschland','Österreich','Schweiz','Kosovo','Zusammenarbeit besprechen'),
 'en':('CLOSE TO YOUR BUSINESS. ACROSS BORDERS.','Working across DACH and Kosovo.','All services are available in Germany, Austria, Switzerland and Kosovo. Analysis, coordination and digital delivery can take place remotely. We arrange on-site workshops, photo and video sessions or operational assignments around your project and the agreed availability.','Germany','Austria','Switzerland','Kosovo','Discuss a project'),
 'sq':('PRANË BIZNESIT. PËRTEJ KUFIJVE.','Bashkëpunim në DACH dhe Kosovë.','Të gjitha shërbimet ofrohen në Gjermani, Austri, Zvicër dhe Kosovë. Analiza, koordinimi dhe zbatimi digjital mund të kryhen në distancë. Punëtoritë, fotografimi, videot dhe angazhimet në vend planifikohen sipas projektit dhe disponueshmërisë së dakorduar.','Gjermani','Austri','Zvicër','Kosovë','Diskutoni bashkëpunimin')}

def region(lang='de',base='',anchor=False,service=None):
 kicker,title,copy,*rest=REGION_COPY[lang]
 if service:
  title=service+' · in DACH und Kosovo'
  copy='Unser Angebot für '+service+' steht Ihnen in Deutschland, Österreich, der Schweiz und Kosovo zur Verfügung. Wir klären zuerst Ziele, vorhandene Systeme und die Verantwortung im Betrieb. Digitale Abstimmung und Umsetzung erfolgen aus der Ferne; nötige Termine im Haus werden im Angebot mit Umfang und Verfügbarkeit abgestimmt.'
 return f'<section class="region-section"{" id=\"einsatzgebiet\"" if anchor else ""}><div class="shell x-shell region-grid"><div><p class="region-kicker">{kicker}</p><h2>{escape(title)}</h2><div class="region-countries">'+''.join(f'<span><i aria-hidden="true">↗</i>{name}</span>' for name in rest[:4])+f'</div></div><div><p>{escape(copy)}</p><a href="{base}kontakt.html" class="region-link">{rest[4]} <span aria-hidden="true">↗</span></a></div></div></section>'
