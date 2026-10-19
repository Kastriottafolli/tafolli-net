"""Useful next steps on section hubs, grounded in existing content."""
from html import escape
HUBS={
 'ueber-mich.html':('ERFAHRUNG, DIE IN IHR PROJEKT EINFLIESST.','Was diese Verbindung für Sie bedeutet.',[
  ('Projekt verstehen.','Wir sprechen über Ablauf, Ziel und die Menschen, die das Ergebnis nutzen. Daraus entsteht ein klarer erster Schritt.',[('werdegang.html','Meinen Werdegang ansehen'),('referenzen.html','Referenzen ansehen')]),
  ('Technik umsetzen.','Von der Bestandsaufnahme bis zu Software und KI: Die technische Lösung entsteht aus einem konkreten Bedarf und wird nachvollziehbar übergeben.',[('digitalisierung.html','Digitalisierung im Detail'),('ki-automatisierung.html','KI-Automatisierung erleben')]),
  ('Persönlich zusammenarbeiten.','Mit TB Solutions begleite ich Unternehmen in DACH und Kosovo. Klare Zuständigkeiten, ein abgestimmter Umfang und direkter Kontakt bilden die Grundlage.',[('referenzen.html','Betriebe & Partner kennenlernen'),('kontakt.html','Projekt besprechen')])]),
 'wissen.html':('VOM VERSTEHEN ZUM UMSETZEN.','Wählen Sie Ihr Thema.',[
  ('KI & Automatisierung','Welche Aufgabe eignet sich für KI? Beginnen Sie mit einem begrenzten Ablauf, prüfen Sie die Daten und legen Sie Freigaben fest.',[('ki-automatisierung.html','Workflows in der Demo erleben'),('rechner.html#ki','Ihr Zeitpotenzial berechnen'),('ki-entwicklung.html','KI-Assistenten ansehen')]),
  ('Software & Apps','Wenn Standardsoftware den Ablauf nicht abbildet, entsteht eine Lösung nach Maß. Web-Apps bringen den Vorgang auf die Geräte, die Ihr Team nutzt.',[('softwareentwicklung.html','Softwareentwicklung'),('app-entwicklung.html','App- & Web-App-Entwicklung')]),
  ('Web, Marketing & Texte','Sichtbarkeit wird wertvoll, wenn daraus eine Anfrage entstehen kann. Texte gibt es auf Deutsch, Englisch und Albanisch.',[('webdesign.html','Webdesign ansehen'),('online-marketing.html','Online-Marketing ansehen'),('angebot/','Texte und Übersetzungen')])]),
 'kontakt.html':('MIT EINER KONKRETEN FRAGE BEGINNEN.','Worum geht es?',[
  ('KI, Software & Abläufe','Welche Arbeit wiederholt sich? Welche Systeme nutzen Sie? Eine kurze Beschreibung des Ablaufs genügt, um Ziele, Daten und die nächsten Schritte zu besprechen.',[('ki-automatisierung.html','AI Automation as a Service'),('softwareentwicklung.html','Individuelle Softwareentwicklung')]),
  ('Texte & Übersetzungen','Deutsch, Englisch oder Albanisch: Schreiben Sie, welchen Text Sie brauchen. Den Preis nenne ich vorab.',[('angebot/','Texte und Übersetzungen'),('kontakt.html','Kurz schreiben')]),
  ('Website & Sichtbarkeit','Planen Sie einen neuen Auftritt oder möchten Sie mehr passende Anfragen? Senden Sie Ihre Website und das wichtigste Ziel.',[('webdesign.html','Webdesign & Webentwicklung'),('social-media.html','Social Media & Content')])])}

def explore(path):
 kicker,title,cards=HUBS[path]
 return '<section class="hub-explore"><div class="shell"><p class="region-kicker">'+kicker+'</p><h2>'+title+'</h2><div class="hub-explore-grid">'+''.join('<article><h3>'+escape(t)+'</h3><p>'+escape(body)+'</p>'+''.join(f'<a href="{url}">{escape(label)} ↗</a>' for url,label in links)+'</article>' for t,body,links in cards)+'</div></div></section>'
