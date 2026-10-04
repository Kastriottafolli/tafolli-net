"""Page-specific search intent, shared identity and honest service coverage."""
import json
from html import escape
from navigation import TITLES, parent

ORIGIN='https://tafolli.net/'
COUNTRIES=[{'@type':'Country','name':name} for name in ['Germany','Austria','Switzerland','Kosovo']]
# Editorial intent, not keyword-volume or ranking claims.
SERVICE_META={
 'ki-automatisierung':('KI-Automatisierung als Service | Kastriot Tafolli','KI-Automatisierung für Hotels, Gastronomie und Unternehmen: Workflows, Systemanbindung und laufende Betreuung in Deutschland, Österreich, Schweiz und Kosovo.'),
 'ki-entwicklung':('KI-Entwicklung & Assistenten | Kastriot Tafolli','KI-Assistenten für Ihren Betrieb: eigene Wissensquellen, geprüfte Antworten und klare Freigaben. Entwicklung und Integration in DACH und Kosovo. Projekt besprechen.'),
 'teamo-ki':('TeamO: KI-Mitarbeiter für Hotels | Kastriot Tafolli','TeamO unterstützt Hotels und Restaurants bei Telefon, Nachrichten und wiederkehrenden Anfragen. KI-Lösungen für DACH und Kosovo. Möglichkeiten im Gespräch klären.'),
 'digitalisierung':('Digitalisierung für Hotels & Betriebe | Kastriot Tafolli','Hotelsoftware, Kasse und Kommunikation sinnvoll verbinden. Digitalisierung mit Bestandsaufnahme, Umsetzung und Team-Einführung in DACH und Kosovo. Jetzt anfragen.'),
 'softwareentwicklung':('Individuelle Softwareentwicklung | Kastriot Tafolli','Individuelle Software, Datenbanken, Dashboards und Schnittstellen für Ihren Betrieb. Von der Anforderung bis zur Übergabe in DACH und Kosovo. Projekt besprechen.'),
 'app-entwicklung':('App- & Web-App-Entwicklung | Kastriot Tafolli','Web-Apps für Checklisten, Bestellungen und Freigaben: mobil nutzbar, mit Rollen und passenden Schnittstellen. Entwicklung für DACH und Kosovo. Projekt anfragen.'),
 'cybersecurity':('Cybersecurity & IT-Sicherheit | Kastriot Tafolli','Zugänge, E-Mail, Backups und Website praktisch absichern. IT-Sicherheit für Hotels und Unternehmen in DACH und Kosovo. Umfang und Maßnahmen gemeinsam festlegen.'),
 'fb-beratung':('F&B-Beratung für Hotels & Gastronomie | Kastriot Tafolli','F&B-Beratung aus operativer Hotelpraxis: Einkauf, Wareneinsatz, Teams und Abläufe verbessern. Für Deutschland, Österreich, Schweiz und Kosovo. Erstgespräch anfragen.'),
 'lieferantenvereinbarungen':('Lieferantenvereinbarungen für Gastronomie | Tafolli','Lieferantenangebote, Konditionen und Leistungspflichten strukturiert vergleichen. Einkaufsberatung für Hotels und Gastronomie in DACH und Kosovo. Gespräch anfragen.'),
 'getraenkevertraege':('Getränkeverträge & Einkaufsberatung | Kastriot Tafolli','Getränkeverträge für Hotels und Gastronomie prüfen: Preise, Bindungen, Ausstattung und Lieferleistung gemeinsam betrachten. Beratung in DACH und Kosovo anfragen.'),
 'rueckverguetungen':('Rückvergütungen im Gastronomie-Einkauf | Tafolli','Rückvergütungen und Boni nachvollziehbar machen: Bezugsgrößen, Nachweise und Abrechnung im Einkauf prüfen. Für Hotels und Gastronomie in DACH und Kosovo.'),
 'wareneinsatz-kalkulation':('Wareneinsatz & Gastronomie-Kalkulation | Tafolli','Rezepturen, Wareneinsatz und Deckungsbeiträge als Entscheidungsgrundlage nutzen. Kalkulationsberatung für Hotels und Restaurants in DACH und Kosovo. Jetzt anfragen.'),
 'inventur-warenwirtschaft':('Inventur & Warenwirtschaft für Gastronomie | Tafolli','Bestände, Bestellung und Inventur sinnvoll verbinden. Warenwirtschaft für Hotels und Gastronomie mit klaren Verantwortlichkeiten in DACH und Kosovo. Projekt besprechen.'),
 'interim-fb-management':('Interim F&B-Management für Hotels | Kastriot Tafolli','F&B-Führung auf Zeit: Teams, Standards und Zahlen im Hotelbetrieb strukturieren. Einsätze in DACH und Kosovo nach abgestimmtem Auftrag und Verfügbarkeit anfragen.'),
 'revenue-controlling':('Revenue Management & F&B-Controlling | Tafolli','Budget, Forecast und Outlet-Kennzahlen für Hotels und Gastronomie nutzbar machen. Revenue- und F&B-Controlling in DACH und Kosovo. Erstgespräch vereinbaren.'),
 'personal-recruiting':('Hospitality-Recruiting & Teamentwicklung | Tafolli','Rollen, Auswahl, Onboarding und Schulung für Hotellerie und Gastronomie. Recruiting und Teamentwicklung in DACH und Kosovo. Ihren konkreten Bedarf besprechen.'),
 'online-marketing':('Online-Marketing für Hotels & Restaurants | Tafolli','Website, Suchmaschinen und Inhalte auf Anfragen und Direktbuchungen ausrichten. Online-Marketing für Hotels und Restaurants in DACH und Kosovo. Projekt besprechen.'),
 'webdesign':('Webdesign für Hotels & Unternehmen | Kastriot Tafolli','Individuelle Websites mit klaren Inhalten, mobiler Bedienung und Buchungsnähe. Webdesign und Webentwicklung für DACH und Kosovo. Ihren neuen Auftritt besprechen.'),
 'suchmaschinenoptimierung':('SEO für Hotels & Restaurants | Kastriot Tafolli','Technische SEO, hilfreiche Angebotsseiten und lokale Sichtbarkeit für Hotels und Restaurants. Suchmaschinenoptimierung in DACH und Kosovo. Website prüfen lassen.'),
 'domain-hosting-email':('Domain, Hosting & E-Mail für Betriebe | Tafolli','Domains, Hosting und professionelle E-Mail strukturiert einrichten oder umziehen. Dokumentierte Zugänge und Betreuung für DACH und Kosovo. Bedarf besprechen.'),
 'social-media':('Social Media für Hotels & Gastronomie | Tafolli','Redaktionsplanung, Beiträge und Reels mit klarem Weg zur Anfrage. Social-Media-Betreuung für Hotels und Gastronomie in DACH und Kosovo. Inhalte gemeinsam planen.'),
 'foto-video':('Foto & Video für Hotels & Gastronomie | Tafolli','Atmosphäre, Küche und Menschen in Bildern zeigen. Foto- und Videoinhalte für Websites und Social Media in DACH und Kosovo. Aufnahmeumfang und Termine besprechen.')}
PAGE_META={
 'leistungen.html':('KI, F&B & digitale Dienstleistungen | Kastriot Tafolli','22 Leistungsbereiche für Hotels, Gastronomie und Unternehmen: KI, Software, F&B-Beratung und Web. In Deutschland, Österreich, Schweiz und Kosovo. Portfolio entdecken.'),
 'ueber-mich.html':('Kastriot Tafolli: Hotellerie, F&B & KI-Kompetenz','Vom Hotelbetrieb zur Software und KI: Lernen Sie Kastriot Tafolli kennen. Operative Erfahrung, technische Ausbildung und persönliche Beratung für DACH und Kosovo.'),
 'werdegang.html':('Werdegang: Hotellerie & KI Engineering | Tafolli','Die beruflichen Stationen von Kastriot Tafolli: Service, F&B-Leitung und operative Verantwortung, ergänzt durch Softwareentwicklung und KI Engineering. Profil entdecken.'),
 'referenzen.html':('Referenzen, Hotels & Partner | Kastriot Tafolli','Entdecken Sie Referenz-Websites, berufliche Hotelstationen und das Netzwerk von Kastriot Tafolli und TB Solutions. Mit Logos, Einordnung und direkten Website-Links.'),
 'wissen.html':('Wissen zu Hotel-KI, Einkauf & Direktbuchungen | Tafolli','Praxiswissen für Hotels und Gastronomie: KI sinnvoll einsetzen, Getränkeverträge verstehen und Direktbuchungen stärken. Ratgeber und Potenzialrechner entdecken.'),
 'rechner.html':('Hotel-Rechner: KI, Einkauf & Direktbuchungen | Tafolli','Vier interaktive Rechner zu KI-Zeitpotenzial, Portalprovisionen, Getränkeeinkauf und Social Media. Eigene Werte eingeben und Annahmen nachvollziehen. Ohne Speicherung.'),
 'wissen-ki-im-hotel.html':('KI im Hotel: Anwendungen, Grenzen & Einstieg | Tafolli','Wo KI im Hotel hilft, welche Aufgaben Freigaben brauchen und wie Sie sinnvoll starten. Praxisratgeber von Kastriot Tafolli mit passenden Leistungen und Rechner.'),
 'wissen-getraenkevertrag.html':('Getränkevertrag prüfen: Konditionen & Bindungen | Tafolli','Getränkeverträge verstehen: Einkaufspreise, Rückvergütung, Ausstattung und Laufzeit gemeinsam bewerten. Praxiswissen für Hotellerie und Gastronomie von Kastriot Tafolli.'),
 'wissen-direktbuchungen.html':('Mehr Direktbuchungen für Hotels gewinnen | Tafolli','Website, Suchmaschinen und Buchungsweg gemeinsam verbessern: So stärken Hotels ihre Direktbuchungen. Praxiswissen, Provisionsrechner und Umsetzung mit Kastriot Tafolli.'),
 'kontakt.html':('Kontakt & Beratung in DACH und Kosovo | Kastriot Tafolli','KI, F&B-Beratung, Software oder Webdesign besprechen: Kontakt zu Kastriot Tafolli und TB Solutions. Deutschland, Österreich, Schweiz und Kosovo. Erstgespräch anfragen.'),
 'impressum.html':('Impressum | Kastriot Tafolli','Anbieterinformationen und Kontaktdaten für tafolli.net: Kastriot Tafolli, Hauptstraße 1, 18609 Ostseebad Binz. Telefon, E-Mail und Verantwortlichkeit für die Inhalte.'),
 'datenschutz.html':('Datenschutz | Kastriot Tafolli','Informationen zur Datenverarbeitung auf tafolli.net: Hosting, Kontakt, lokale Schriftarten, Logo-Animation und Rechner. Hinweise und Kontakt zu Kastriot Tafolli.')}
PAGE_META.update({slug+'.html':meta for slug,meta in SERVICE_META.items()})

def metadata(path,title,description):return PAGE_META.get(path,(title,description))

def structured(path,title,description,lang='de'):
 url=ORIGIN+('' if path=='index.html' else path)
 identity=[
  {'@type':'Organization','@id':ORIGIN+'#business','name':'Kastriot Tafolli · TB Solutions','url':ORIGIN,'logo':ORIGIN+'assets/brand/logo-mark.webp','email':'info@tafolli.net','telephone':'+4917664616146','areaServed':COUNTRIES,'contactPoint':{'@type':'ContactPoint','contactType':'project enquiries','email':'info@tafolli.net','telephone':'+4917664616146','availableLanguage':['de','en','sq']}},
  {'@type':'Person','@id':ORIGIN+'#kastriot','name':'Kastriot Tafolli','url':ORIGIN+'ueber-mich.html','image':ORIGIN+'assets/bilder/kastriot-tafolli-portraet.jpg','worksFor':{'@id':ORIGIN+'#business'}},
  {'@type':'WebSite','@id':ORIGIN+'#website','name':'Kastriot Tafolli','url':ORIGIN,'publisher':{'@id':ORIGIN+'#business'},'inLanguage':['de','en','sq']}]
 page={'@type':'WebPage','@id':url+'#page','url':url,'name':title,'description':description,'inLanguage':lang,'isPartOf':{'@id':ORIGIN+'#website'}}
 if path=='ueber-mich.html':page.update({'@type':'ProfilePage','mainEntity':{'@id':ORIGIN+'#kastriot'}})
 if path=='kontakt.html':page['@type']='ContactPage'
 if path in ['leistungen.html','wissen.html','referenzen.html']:page['@type']='CollectionPage'
 graph=identity+[page]
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
 'de':('NAH AM BETRIEB. ÜBER GRENZEN HINWEG.','Ihre Idee kennt keine Landesgrenze.','Alle Leistungen biete ich in Deutschland, Österreich, der Schweiz und Kosovo an. Analyse, Abstimmung und digitale Umsetzung sind ortsunabhängig möglich. Workshops, Foto- und Videotermine oder operative Einsätze vor Ort planen wir passend zu Ihrem Auftrag und meiner Verfügbarkeit.','Deutschland','Österreich','Schweiz','Kosovo','Zusammenarbeit besprechen'),
 'en':('CLOSE TO YOUR BUSINESS. ACROSS BORDERS.','Your idea travels further.','All services are available in Germany, Austria, Switzerland and Kosovo. Analysis, coordination and digital delivery can take place remotely. We arrange on-site workshops, photo and video sessions or operational assignments around your project and my availability.','Germany','Austria','Switzerland','Kosovo','Discuss a project'),
 'sq':('PRANË BIZNESIT. PËRTEJ KUFIJVE.','Ideja juaj nuk njeh kufij.','Të gjitha shërbimet ofrohen në Gjermani, Austri, Zvicër dhe Kosovë. Analiza, koordinimi dhe zbatimi digjital mund të kryhen në distancë. Punëtoritë, fotografimi, videot dhe angazhimet në vend planifikohen sipas projektit dhe disponueshmërisë sime.','Gjermani','Austri','Zvicër','Kosovë','Diskutoni bashkëpunimin')}

def region(lang='de',base='',anchor=False,service=None):
 kicker,title,copy,*rest=REGION_COPY[lang]
 if service:
  title=service+' · in DACH und Kosovo'
  copy='Mein Angebot für '+service+' steht Ihnen in Deutschland, Österreich, der Schweiz und Kosovo zur Verfügung. Wir klären zuerst Ziele, vorhandene Systeme und die Verantwortung im Betrieb. Digitale Abstimmung und Umsetzung erfolgen aus der Ferne; nötige Termine im Haus werden im Angebot mit Umfang und Verfügbarkeit abgestimmt.'
 return f'<section class="region-section"{" id=\"einsatzgebiet\"" if anchor else ""}><div class="shell x-shell region-grid"><div><p class="region-kicker">{kicker}</p><h2>{escape(title)}</h2><div class="region-countries">'+''.join(f'<span><i aria-hidden="true">↗</i>{name}</span>' for name in rest[:4])+f'</div></div><div><p>{escape(copy)}</p><a href="{base}kontakt.html" class="region-link">{rest[4]} <span aria-hidden="true">↗</span></a></div></div></section>'
