"""One crawlable, categorized navigation for every generated page."""
from html import escape

SERVICE_GROUPS = [
 ('KI & Technologie', [
  ('ki-automatisierung.html','AI Automation as a Service'), ('ki-entwicklung.html','KI-Entwicklung & Assistenten'),
  ('teamo-ki.html','TeamO · digitaler KI-Mitarbeiter'), ('digitalisierung.html','Digitalisierung'),
  ('softwareentwicklung.html','Softwareentwicklung'), ('app-entwicklung.html','App- & Web-App-Entwicklung'), ('cybersecurity.html','Cybersecurity & IT-Sicherheit')]),
 ('Hotellerie & Gastronomie', [
  ('fb-beratung.html','F&B-Beratung'), ('lieferantenvereinbarungen.html','Lieferantenvereinbarungen'),
  ('getraenkevertraege.html','Getränkeverträge'), ('rueckverguetungen.html','Rückvergütungen'),
  ('wareneinsatz-kalkulation.html','Wareneinsatz & Kalkulation'), ('inventur-warenwirtschaft.html','Inventur & Warenwirtschaft'),
  ('interim-fb-management.html','Interim F&B-Management'), ('revenue-controlling.html','Revenue & F&B-Controlling'), ('personal-recruiting.html','Recruiting & Teamentwicklung')]),
 ('Web & Sichtbarkeit', [
  ('online-marketing.html','Online-Marketing & Digitalstrategie'), ('webdesign.html','Webdesign & Webentwicklung'),
  ('suchmaschinenoptimierung.html','Suchmaschinenoptimierung'), ('domain-hosting-email.html','Domain, Hosting & E-Mail'),
  ('social-media.html','Social Media & Content'), ('foto-video.html','Foto & Video')])]
SECTIONS = [
 ('leistungen','Leistungen','leistungen.html','Alle 22 Leistungsbereiche',SERVICE_GROUPS),
 ('profil','Über mich','ueber-mich.html','Kastriot Tafolli kennenlernen',[
  ('Mensch & Erfahrung',[('ueber-mich.html','Über mich'),('werdegang.html','Mein Werdegang'),('referenzen.html','Referenzen & Partner'),('referenzen.html#stationen','Berufliche Stationen')]),
  ('Netzwerk',[('referenzen.html#betriebe','Betriebe & Referenz-Websites'),('referenzen.html#gastronomie','Gastronomiepartner'),('referenzen.html#technologie','Technologiepartner')]),
  ('Startseiten & Sprachen',[('index.html','Deutsch'),('en/','English'),('sq/','Shqip')])]),
 ('wissen','Wissen','wissen.html','Alle Ratgeber & Werkzeuge',[
  ('Wissen für Ihren Betrieb',[('wissen.html','Wissen · Übersicht'),('wissen-ki-im-hotel.html','KI im Hotel: Möglichkeiten & Grenzen'),('wissen-getraenkevertrag.html','Getränkeverträge verstehen'),('wissen-direktbuchungen.html','Mehr Direktbuchungen gewinnen')]),
  ('Potenzial berechnen',[('rechner.html','Alle Potenzialrechner'),('rechner.html#ki','KI: Zeit & Arbeitsaufwand'),('rechner.html#direkt','Direktbuchungen & Provisionen'),('rechner.html#einkauf','Getränkeeinkauf & Konditionen'),('rechner.html#social','Social Media & Sichtbarkeit')])]),
 ('kontakt','Kontakt','kontakt.html','Ein Projekt besprechen',[
  ('Zusammenarbeit',[('kontakt.html','Kontakt & Erstgespräch'),('kontakt.html#einsatzgebiet','Deutschland · Österreich · Schweiz · Kosovo'),('mailto:info@tafolli.net','E-Mail schreiben'),('tel:+4917664616146','+49 176 64616146')]),
  ('Rechtliches & Orientierung',[('impressum.html','Impressum'),('datenschutz.html','Datenschutz'),('404.html','Seite nicht gefunden · 404')])])]
LABELS = {'de':['Leistungen','Über mich','Wissen','Kontakt'],'en':['Services','About me','Insights','Contact'],'sq':['Shërbimet','Rreth meje','Njohuri','Kontakt']}
TITLES = {url: label for _,_,_,_,groups in SECTIONS for _,links in groups for url,label in links if '#' not in url and ':' not in url}
TITLES.update({'leistungen.html':'Leistungen','index.html':'Startseite','en/':'English','sq/':'Shqip'})

def nav( current='index.html', base='', lang='de'):
 def link(url,label,cls=''):
  href=url if ':' in url else base+url
  active=' aria-current="page"' if url==current else ''
  language=' lang="de"' if lang!='de' and url.endswith('.html') and url!='index.html' else ''
  return f'<a href="{escape(href,quote=True)}" class="{cls}"{active}{language}>{escape(label)}<span aria-hidden="true">↗</span></a>'
 sections=[]
 for i,(key,label,url,overview,groups) in enumerate(SECTIONS):
  active=any(h==current for _,links in groups for h,_ in links) or url==current
  columns=''.join(f'<div class="site-nav-column"><p>{escape(group)}</p>{"".join(link(h,t) for h,t in links)}</div>' for group,links in groups)
  note={'de':'Unterseiten auf Deutsch · Startseiten in DE / EN / SQ','en':'Detail pages in German · Homepages in DE / EN / SQ','sq':'Nënfaqet në gjermanisht · Faqja kryesore DE / EN / SQ'}[lang]
  sections.append(f'<details class="site-nav-section" data-section="{key}"><summary{" data-current" if active else ""}>{LABELS[lang][i]}<span aria-hidden="true">⌄</span></summary><div class="site-nav-panel" lang="de"><div class="site-nav-panel-top"><span>0{i+1} / {escape(label)}</span>{link(url,overview,"site-nav-overview")}</div><div class="site-nav-columns">{columns}</div><div class="site-nav-panel-bottom"><span>PRAXIS × TECHNOLOGIE</span><span lang="{lang}">{note}</span></div></div></details>')
 return '<nav id="site-navigation" class="site-navigation" aria-label="'+{'de':'Hauptnavigation','en':'Main navigation','sq':'Navigimi kryesor'}[lang]+'">'+''.join(sections)+'</nav>'

def toggle(lang='de'):
 label={'de':'Menü','en':'Menu','sq':'Menu'}[lang]
 return f'<button class="site-nav-toggle" type="button" aria-expanded="false" aria-controls="site-navigation" aria-label="{label}" data-nav-toggle><span>{label}</span><i aria-hidden="true">+</i></button>'

def parent(path):
 for key,label,url,_,groups in SECTIONS:
  if any(path==h for _,links in groups for h,_ in links):
   return (label,url) if path!=url and key!='kontakt' else None
 return None

def breadcrumbs(path):
 if path in ['index.html','en/','sq/','404.html']:return ''
 title=TITLES.get(path,path)
 trail=parent(path)
 parts='<a href="index.html">Startseite</a>'
 if trail:parts+=f'<span aria-hidden="true">/</span><a href="{trail[1]}">{escape(trail[0])}</a>'
 parts+=f'<span aria-hidden="true">/</span><span aria-current="page">{escape(title)}</span>'
 return '<div class="shell site-breadcrumb"><nav aria-label="Brotkrumennavigation">'+parts+'</nav></div>'
