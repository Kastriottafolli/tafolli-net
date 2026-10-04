"""Useful next steps on section hubs, grounded in existing content."""
from html import escape
HUBS={
 'ueber-mich.html':('ERFAHRUNG, DIE IN IHR PROJEKT EINFLIESST.','Was diese Verbindung für Sie bedeutet.',[
  ('Betrieb verstehen.','Ich verbinde Service, Teamführung und wirtschaftliche Verantwortung. Ihre Abläufe werden mit den Menschen besprochen, die sie täglich umsetzen.',[('werdegang.html','Meinen Werdegang ansehen'),('referenzen.html#stationen','Berufliche Hotelstationen entdecken')]),
  ('Technik umsetzen.','Von der Bestandsaufnahme bis zu Software und KI: Die technische Lösung entsteht aus einem konkreten betrieblichen Bedarf und wird nachvollziehbar übergeben.',[('digitalisierung.html','Digitalisierung im Detail'),('ki-automatisierung.html','KI-Automatisierung erleben')]),
  ('Persönlich zusammenarbeiten.','Mit TB Solutions begleite ich Hotels, Gastronomie und weitere Unternehmen. Klare Zuständigkeiten, ein abgestimmter Umfang und direkter Kontakt bilden die Grundlage.',[('referenzen.html','Betriebe & Partner kennenlernen'),('kontakt.html','Über Ihren Betrieb sprechen')])]),
 'wissen.html':('VOM VERSTEHEN ZUM UMSETZEN.','Wählen Sie Ihr Thema.',[
  ('KI & Automatisierung','Welche Aufgabe eignet sich für KI? Beginnen Sie mit einem begrenzten Ablauf, prüfen Sie die Daten und legen Sie Freigaben fest. Ratgeber, Demo und Rechner helfen bei der Einordnung.',[('wissen-ki-im-hotel.html','Praxisratgeber: KI im Hotel'),('ki-automatisierung.html','Workflows in der Demo erleben'),('rechner.html#ki','Ihr Zeitpotenzial berechnen')]),
  ('Einkauf & Ergebnis','Preis allein erklärt keinen guten Vertrag. Lieferfähigkeit, Bindungen, Boni und Wareneinsatz müssen zusammenpassen. Vertiefen Sie den Ratgeber mit den passenden Leistungen.',[('wissen-getraenkevertrag.html','Getränkeverträge verstehen'),('rueckverguetungen.html','Rückvergütungen im Detail'),('wareneinsatz-kalkulation.html','Wareneinsatz & Kalkulation')]),
  ('Web & Direktbuchungen','Sichtbarkeit wird wertvoll, wenn daraus eine Anfrage oder Buchung entstehen kann. Inhalte, mobile Bedienung und ein verständlicher Buchungsweg gehören zusammen.',[('wissen-direktbuchungen.html','Mehr Direktbuchungen gewinnen'),('rechner.html#direkt','Portalprovisionen berechnen'),('webdesign.html','Webdesign & Buchungsnähe')])]),
 'kontakt.html':('MIT EINER KONKRETEN FRAGE BEGINNEN.','Worum geht es in Ihrem Betrieb?',[
  ('KI, Software & Abläufe','Welche Arbeit wiederholt sich? Welche Systeme nutzen Sie? Eine kurze Beschreibung des Ablaufs genügt, um Ziele, Daten und die nächsten Schritte zu besprechen.',[('ki-automatisierung.html','AI Automation as a Service'),('softwareentwicklung.html','Individuelle Softwareentwicklung')]),
  ('F&B, Einkauf & Teams','Geht es um Konditionen, Wareneinsatz oder operative Führung? Nennen Sie Betriebstyp und die wichtigste Herausforderung. Wir legen gemeinsam den sinnvollen Umfang fest.',[('fb-beratung.html','F&B-Beratung entdecken'),('lieferantenvereinbarungen.html','Lieferantenvereinbarungen')]),
  ('Website & Sichtbarkeit','Planen Sie einen neuen Auftritt oder möchten Sie mehr passende Anfragen? Senden Sie Ihre Website und das wichtigste Ziel. Gestaltung, Inhalte und Technik werden zusammen betrachtet.',[('webdesign.html','Webdesign & Webentwicklung'),('suchmaschinenoptimierung.html','SEO für Hotels & Restaurants')])])}

def explore(path):
 kicker,title,cards=HUBS[path]
 return '<section class="hub-explore"><div class="shell"><p class="region-kicker">'+kicker+'</p><h2>'+title+'</h2><div class="hub-explore-grid">'+''.join('<article><h3>'+escape(t)+'</h3><p>'+escape(body)+'</p>'+''.join(f'<a href="{url}">{escape(label)} ↗</a>' for url,label in links)+'</article>' for t,body,links in cards)+'</div></div></section>'
