"""Page-specific search intent, shared identity and honest service coverage."""
import json
from html import escape
from navigation import TITLES, parent

ORIGIN='https://tafolli.net/'
COUNTRIES=[{'@type':'Country','name':name} for name in ['Germany','Austria','Switzerland','Kosovo']]
# Kept on disk for a later decision, but not offered in navigation, sitemap or search.
NOINDEX_PATHS={
 'fb-beratung.html','lieferantenvereinbarungen.html','getraenkevertraege.html','rueckverguetungen.html',
 'wareneinsatz-kalkulation.html','inventur-warenwirtschaft.html','interim-fb-management.html',
 'revenue-controlling.html','personal-recruiting.html','wissen-ki-im-hotel.html',
 'wissen-getraenkevertrag.html','wissen-direktbuchungen.html'}
# Editorial intent, not keyword-volume or ranking claims.
SERVICE_META={
 'ki-automatisierung':('KI-Automatisierung als Service | Kastriot Tafolli','KI-Automatisierung für Unternehmen: Workflows, Systemanbindung und laufende Betreuung in Deutschland, Österreich, Schweiz und Kosovo.'),
 'ki-automatisierung-kleine-unternehmen':('KI Automatisierung für kleine Unternehmen | Kastriot Tafolli','KI Automatisierung für kleine Unternehmen: die erste Automatisierung zum Festpreis, zum Beispiel für E-Mail, Angebote oder Termine. Immer mit Ihrer Freigabe. Festpreis-Angebot auf Anfrage.'),
 'landingpage-erstellen-lassen':('Landingpage erstellen lassen | Kastriot Tafolli','Landingpage erstellen lassen oder eine Website zum Festpreis, inklusive Pflege und technischem Check. Barrierefreiheit und Datenschutz nur als technische Prüfung. Festpreis-Angebot auf Anfrage.'),
 'ki-entwicklung':('KI-Entwicklung & Assistenten | Kastriot Tafolli','KI-Assistenten für Ihren Betrieb: eigene Wissensquellen, geprüfte Antworten und klare Freigaben. Entwicklung und Integration in DACH und Kosovo. Projekt besprechen.'),
 'teamo-ki':('TeamO: digitaler KI-Mitarbeiter | Kastriot Tafolli','TeamO übernimmt Telefon, Nachrichten und wiederkehrende Anfragen. KI-Lösungen für DACH und Kosovo. Möglichkeiten im Gespräch klären.'),
 'digitalisierung':('Digitalisierung für Betriebe | Kastriot Tafolli','Bestehende Systeme und Kommunikation sinnvoll verbinden. Digitalisierung mit Bestandsaufnahme, Umsetzung und Einführung in DACH und Kosovo. Jetzt anfragen.'),
 'softwareentwicklung':('Individuelle Softwareentwicklung | Kastriot Tafolli','Individuelle Software, Datenbanken, Dashboards und Schnittstellen für Ihren Betrieb. Von der Anforderung bis zur Übergabe in DACH und Kosovo. Projekt besprechen.'),
 'app-entwicklung':('App- & Web-App-Entwicklung | Kastriot Tafolli','Web-Apps für Checklisten, Bestellungen und Freigaben: mobil nutzbar, mit Rollen und passenden Schnittstellen. Entwicklung für DACH und Kosovo. Projekt anfragen.'),
 'cybersecurity':('Cybersecurity & IT-Sicherheit | Kastriot Tafolli','Zugänge, E-Mail, Backups und Website praktisch absichern. IT-Sicherheit für Unternehmen in DACH und Kosovo. Umfang und Maßnahmen gemeinsam festlegen.'),
 'fb-beratung':('F&B-Beratung für Hotels & Gastronomie | Kastriot Tafolli','F&B-Beratung aus operativer Hotelpraxis: Einkauf, Wareneinsatz, Teams und Abläufe verbessern. Für Deutschland, Österreich, Schweiz und Kosovo. Erstgespräch anfragen.'),
 'lieferantenvereinbarungen':('Lieferantenvereinbarungen für Gastronomie | Tafolli','Lieferantenangebote, Konditionen und Leistungspflichten strukturiert vergleichen. Einkaufsberatung für Hotels und Gastronomie in DACH und Kosovo. Gespräch anfragen.'),
 'getraenkevertraege':('Getränkeverträge & Einkaufsberatung | Kastriot Tafolli','Getränkeverträge für Hotels und Gastronomie prüfen: Preise, Bindungen, Ausstattung und Lieferleistung gemeinsam betrachten. Beratung in DACH und Kosovo anfragen.'),
 'rueckverguetungen':('Rückvergütungen im Gastronomie-Einkauf | Tafolli','Rückvergütungen und Boni nachvollziehbar machen: Bezugsgrößen, Nachweise und Abrechnung im Einkauf prüfen. Für Hotels und Gastronomie in DACH und Kosovo.'),
 'wareneinsatz-kalkulation':('Wareneinsatz & Gastronomie-Kalkulation | Tafolli','Rezepturen, Wareneinsatz und Deckungsbeiträge als Entscheidungsgrundlage nutzen. Kalkulationsberatung für Hotels und Restaurants in DACH und Kosovo. Jetzt anfragen.'),
 'inventur-warenwirtschaft':('Inventur & Warenwirtschaft für Gastronomie | Tafolli','Bestände, Bestellung und Inventur sinnvoll verbinden. Warenwirtschaft für Hotels und Gastronomie mit klaren Verantwortlichkeiten in DACH und Kosovo. Projekt besprechen.'),
 'interim-fb-management':('Interim F&B-Management für Hotels | Kastriot Tafolli','F&B-Führung auf Zeit: Teams, Standards und Zahlen im Hotelbetrieb strukturieren. Einsätze in DACH und Kosovo nach abgestimmtem Auftrag und Verfügbarkeit anfragen.'),
 'revenue-controlling':('Revenue Management & F&B-Controlling | Tafolli','Budget, Forecast und Outlet-Kennzahlen für Hotels und Gastronomie nutzbar machen. Revenue- und F&B-Controlling in DACH und Kosovo. Erstgespräch vereinbaren.'),
 'personal-recruiting':('Hospitality-Recruiting & Teamentwicklung | Tafolli','Rollen, Auswahl, Onboarding und Schulung für Hotellerie und Gastronomie. Recruiting und Teamentwicklung in DACH und Kosovo. Ihren konkreten Bedarf besprechen.'),
 'online-marketing':('Online-Marketing & Digitalstrategie | Kastriot Tafolli','Website, Suchmaschinen und Inhalte auf Anfragen ausrichten. Online-Marketing für Unternehmen in DACH und Kosovo. Projekt besprechen.'),
 'webdesign':('Webdesign & Webentwicklung | Kastriot Tafolli','Individuelle Websites mit klaren Inhalten und mobiler Bedienung. Webdesign und Webentwicklung für DACH und Kosovo. Ihren neuen Auftritt besprechen.'),
 'suchmaschinenoptimierung':('Suchmaschinenoptimierung | Kastriot Tafolli','Technische SEO, hilfreiche Angebotsseiten und lokale Sichtbarkeit für Unternehmen. Suchmaschinenoptimierung in DACH und Kosovo. Website prüfen lassen.'),
 'domain-hosting-email':('Domain, Hosting & E-Mail für Betriebe | Tafolli','Domains, Hosting und professionelle E-Mail strukturiert einrichten oder umziehen. Dokumentierte Zugänge und Betreuung für DACH und Kosovo. Bedarf besprechen.'),
 'social-media':('Social Media & Content | Kastriot Tafolli','Redaktionsplanung, Beiträge und Reels mit klarem Weg zur Anfrage. Social-Media-Betreuung für Unternehmen in DACH und Kosovo. Inhalte gemeinsam planen.'),
 'foto-video':('Foto & Video | Kastriot Tafolli','Menschen, Produkte und Räume in Bildern zeigen. Foto- und Videoinhalte für Websites und Social Media in DACH und Kosovo. Aufnahmeumfang und Termine besprechen.'),
 'website-pflege':('Website-Pflege im Monatsabo | Kastriot Tafolli','Website-Pflege in drei Stufen: 99, 199 oder 299 € im Monat. Updates, Backups und kleine Änderungen, monatlich kündbar.'),
 'onlineshop':('Onlineshop | Kastriot Tafolli','Onlineshop einrichten und einweisen. Stufe Start 990 €, Stufe Erweitert 1.990 €. Hosting und Shop-Software laufen beim Kunden oder beim Anbieter.'),
 'web-apps':('Web-App oder Tool nach Maß | Kastriot Tafolli','Kleine Web-App oder ein Tool nach Maß ab 390 €. Ein Ablauf im Browser. Größere Projekte zum Festpreis nach Angebot.'),
 'firmenprofile':('Firmenprofile im Netz einrichten | Kastriot Tafolli','Google-Unternehmensprofil und Verzeichnisse mit einheitlichen Angaben. Festpreis 399 oder 899 €. Die Bestätigung bei Google machen Sie selbst.')}
PAGE_META={
 'leistungen.html':('Leistungsübersicht: KI, Software, Web und Texte | Tafolli','Übersicht der Angebote: KI-Automatisierung, Software, Webdesign, Online-Marketing und Übersetzungen für Unternehmen in Deutschland, Österreich, Schweiz und Kosovo.'),
 'ueber-mich.html':('Kastriot Tafolli: KI, Software und Web','Lernen Sie Kastriot Tafolli kennen: Softwareentwicklung, KI, Websites und Texte auf Deutsch, Englisch und Albanisch. TB Solutions in Ostseebad Binz.'),
 'werdegang.html':('Werdegang: Software, KI und Projekte | Tafolli','Stationen von Kastriot Tafolli: Softwareentwicklung, KI Engineering und frühere Projektverantwortung. Profil entdecken.'),
 'referenzen.html':('Referenzen und Partner | Kastriot Tafolli','Referenz-Websites und Technologiepartner von Kastriot Tafolli und TB Solutions. Mit Logos, Einordnung und direkten Website-Links.'),
 'wissen.html':('Wissen zu KI, Software und Web | Tafolli','Orientierung zu KI-Automatisierung, Software und digitaler Sichtbarkeit. Ratgeber und Potenzialrechner von Kastriot Tafolli.'),
 'rechner.html':('Rechner: KI-Zeit und Social Media | Tafolli','Zwei interaktive Rechner zu KI-Zeitpotenzial und Social Media. Eigene Werte eingeben und Annahmen nachvollziehen. Ohne Speicherung.'),
 'wissen-ki-im-hotel.html':('KI im Hotel: Anwendungen, Grenzen & Einstieg | Tafolli','Wo KI im Hotel hilft, welche Aufgaben Freigaben brauchen und wie Sie sinnvoll starten. Praxisratgeber von Kastriot Tafolli mit passenden Leistungen und Rechner.'),
 'wissen-getraenkevertrag.html':('Getränkevertrag prüfen: Konditionen & Bindungen | Tafolli','Getränkeverträge verstehen: Einkaufspreise, Rückvergütung, Ausstattung und Laufzeit gemeinsam bewerten. Praxiswissen für Hotellerie und Gastronomie von Kastriot Tafolli.'),
 'wissen-direktbuchungen.html':('Mehr Direktbuchungen für Hotels gewinnen | Tafolli','Website, Suchmaschinen und Buchungsweg gemeinsam verbessern: So stärken Hotels ihre Direktbuchungen. Praxiswissen, Provisionsrechner und Umsetzung mit Kastriot Tafolli.'),
 'kontakt.html':('Kontakt & Beratung in DACH und Kosovo | Kastriot Tafolli','KI, Software, Webdesign, Marketing oder Übersetzungen besprechen: Kontakt zu Kastriot Tafolli und TB Solutions. Deutschland, Österreich, Schweiz und Kosovo.'),
 'impressum.html':('Impressum | Kastriot Tafolli','Anbieterinformationen und Kontaktdaten für tafolli.net: Kastriot Tafolli, Hauptstraße 1, 18609 Ostseebad Binz. Telefon, E-Mail und Verantwortlichkeit für die Inhalte.'),
 'datenschutz.html':('Datenschutz | Kastriot Tafolli','Informationen zur Datenverarbeitung auf tafolli.net: Hosting, Kontakt, lokale Schriftarten, Logo-Animation und Rechner. Hinweise und Kontakt zu Kastriot Tafolli.'),
 'preisrechner.html':('Preisrechner | Kastriot Tafolli','Unverbindliche Preisschätzung für KI, Website, Shop, Web-App, Pflege-Abo, Firmenprofile und Texte. Die Rechnung bleibt im Browser.')}
PAGE_META.update({slug+'.html':meta for slug,meta in SERVICE_META.items()})

def metadata(path,title,description):return PAGE_META.get(path,(title,description))

def texte_angebot():
 """Fixed text prices. Extra language and rush work have no published amount."""
 return {'@type':'Service','@id':ORIGIN+'angebot/#texte','name':'Texte und Übersetzungen','url':ORIGIN+'angebot/','description':'Weitere Sprache und Eilauftrag: Aufpreis nach Absprache.','provider':{'@id':ORIGIN+'#business'},'areaServed':COUNTRIES,'offers':[
  {'@type':'Offer','name':'Übersetzung Dokument/Prospekt','price':'99','priceCurrency':'EUR'},
  {'@type':'Offer','name':'Website-Text','price':'199','priceCurrency':'EUR'},
  {'@type':'Offer','name':'Content-Paket','price':'299','priceCurrency':'EUR'}]}

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
 if path=='preisrechner.html':
  graph.append({'@type':'WebApplication','@id':url+'#app','name':'Preisrechner','url':url,'description':description,'applicationCategory':'BusinessApplication','offers':{'@type':'Offer','price':'0','priceCurrency':'EUR'},'provider':{'@id':ORIGIN+'#business'}})
 elif path in ('angebot/','angebot/index.html'):
  graph.append(texte_angebot())
 elif slug in SERVICE_META:
  service_name=TITLES.get(path) or title.split(' | ')[0]
  graph.append({'@type':'Service','@id':url+'#service','name':service_name,'serviceType':service_name,'url':url,'description':description,'provider':{'@id':ORIGIN+'#business'},'areaServed':COUNTRIES})
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
