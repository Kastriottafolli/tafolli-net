"""Distinct visual context for each service; no injected client galleries."""
from html import escape as e
from agency import art
from work import image
from conversion import brief, TOPICS
TECH={'softwareentwicklung','app-entwicklung','digitalisierung','domain-hosting-email','web-apps','onlineshop','onlineshop-kleine-haendler'}
MARKETING={'webdesign','suchmaschinenoptimierung','social-media','foto-video','online-marketing','website-pflege','firmenprofile','landingpage-erstellen-lassen','website-fuer-handwerker','website-fuer-vereine','website-pflege-kleine-betriebe','angebot/','sq/faqe-dhe-perkthime'}
AI={'ki-entwicklung','ki-automatisierung','teamo-ki','ki-automatisierung-kleine-unternehmen','ki-automatisierung-arztpraxen','sq/automatizim-ia'}
CONSULT={'lieferantenvereinbarungen','rueckverguetungen','getraenkevertraege','wareneinsatz-kalkulation','inventur-warenwirtschaft','interim-fb-management','revenue-controlling','personal-recruiting','fb-beratung'}
def family(slug):
 return 'security' if slug=='cybersecurity' else 'technology' if slug in TECH else 'marketing' if slug in MARKETING else 'ai' if slug in AI else 'consulting'
def hero_visual(slug):
 if slug=='softwareentwicklung':
  return '<div class="service-visual v-hero v-technology"><div class="v-media-topline"><span class="v-kicker">UNSER EIGENES PRODUKT / TAFOLLI BOOST</span></div><div class="v-hero-screen">'+image('tafolli-boost-desktop.webp','Tafolli Boost – unsere eigene Webanwendung',eager=True)+'</div><div class="v-media-bottom"><strong>Eine Idee wird zur Anwendung.</strong><a class="v-product-link" href="https://tafolliboost.com/" target="_blank" rel="noopener noreferrer">Tafolli Boost ansehen ↗</a></div></div>'
 kind={'website-fuer-handwerker':'web','website-fuer-vereine':'web','landingpage-erstellen-lassen':'web','website-pflege':'web','website-pflege-kleine-betriebe':'web','onlineshop':'web','onlineshop-kleine-haendler':'web','firmenprofile':'seo','suchmaschinenoptimierung':'seo','social-media':'social','foto-video':'social','webdesign':'web','wissen-direktbuchungen':'web'}.get(slug,family(slug))
 return '<div class="service-visual v-hero v-owned-art">'+art(kind)+'</div>'

FLOWS={
 'ai':[
 ('Anfragen','Eine Anfrage wird zum vorbereiteten nächsten Schritt.',['Anfrage','Informationen ordnen','Entwurf prüfen','Antwort freigeben'],'Die KI ordnet Inhalte und bereitet eine Antwort vor. Bei fehlenden Angaben oder Ausnahmen bleibt der Vorgang bei einer verantwortlichen Person.'),
 ('Dokumente','Von vorhandenen Informationen zu einem brauchbaren Entwurf.',['Dokument','Inhalte auslesen','Entwurf bearbeiten','Exportieren'],'Tafolli Boost zeigt dieses Prinzip als Produkt: Lebenslauf und Stellenanzeige bilden die Grundlage, Menschen prüfen die erstellten Texte.'),
 ('Wissen','Das richtige Wissen im richtigen Moment.',['Frage','Freigegebene Quellen','Antwort mit Kontext','Rückfrage klären'],'Ein interner Assistent arbeitet mit ausgewählten Unterlagen. Fehlende oder widersprüchliche Informationen werden für die Klärung sichtbar.')],
 'security':[
 ('Zugänge','Jede Person erhält die passenden Rechte.',['Persönliches Konto','Mehrfaktor-Anmeldung','Passende Rolle','Zugriff überprüfen'],'Die erste Ebene ist Identität: Wer darf auf welche Anwendung zugreifen? Rollenwechsel und Austritte brauchen klare Zuständigkeiten.'),
 ('Anwendungen','Sicherheit wird Teil der Entwicklung.',['Anforderungen','Sichere Umsetzung','Funktionen prüfen','Updates planen'],'Rollen, Datenflüsse, Abhängigkeiten und Fehlerfälle werden im vereinbarten Umfang berücksichtigt. Spezialisierte Prüfungen erhalten einen eigenen Auftrag.'),
 ('Wiederanlauf','Ein Backup ist erst mit der Wiederherstellung vollständig.',['Sichern','Wiederherstellen','Ablauf erproben','Verantwortung klären'],'Gemeinsam wird geklärt, welche Daten und Funktionen benötigt werden, wie sie wiederhergestellt werden und wer bei einer Störung handelt.')],
}

def workflow(kind='ai'):
 rows=FLOWS[kind]; id='flow-'+kind
 buttons=''.join(f'<button type="button" data-flow-tab="{i}" aria-pressed="{str(i==0).lower()}" aria-controls="{id}-{i}">{e(row[0])}</button>' for i,row in enumerate(rows))
 panels=''
 for i,(_,title,steps,text) in enumerate(rows):
  nodes=''.join(f'<div class="flow-node"><span>0{j+1}</span><strong>{e(step)}</strong></div>' for j,step in enumerate(steps))
  panels+=f'<div class="flow-panel" id="{id}-{i}" data-flow-panel="{i}"{(" hidden" if i else "")}><h3>{e(title)}</h3><div class="flow-track">{nodes}</div><p>{e(text)}</p></div>'
 label='Schutzebenen entdecken' if kind=='security' else 'Ein Ablauf wird verständlich'
 return f'<section class="visual-interlude workflow-section" data-flow><div class="shell"><div class="visual-section-heading"><div><p class="v-kicker">INTERAKTIVE PROZESSSKIZZE</p><h2>{label}.</h2></div><p>Wählen Sie ein Thema und sehen Sie, wie die einzelnen Schritte zusammenhängen.</p></div><div class="flow-switch" role="group" aria-label="Ablauf auswählen">{buttons}</div>{panels}</div></section>'

def calculator(slug=''):
 return '''<section class="visual-interlude mini-calculation"><div class="shell mini-calc-grid"><div><p class="v-kicker">ZAHLEN GREIFBAR MACHEN</p><h2>Ein kleiner Anteil.<br>Eine echte Entscheidung.</h2><p>Wie verändert der Wareneinsatz den verbleibenden Betrag? Bewegen Sie die Regler und vergleichen Sie ein einfaches Monatsmodell.</p><p class="v-model-note">Rechenbeispiel mit frei gewählten Werten. Der verbleibende Betrag ist kein Gewinn; Personal, Miete und weitere Kosten sind noch nicht berücksichtigt.</p><a class="lnk" href="rechner.html">Weitere betriebliche Rechner ↗</a></div><div class="mini-calc-card" data-mini-calc><div class="mini-calc-label"><label>Monatsumsatz netto <output data-calc-revenue-label>30.000 €</output><input data-calc-revenue type="range" min="10000" max="100000" step="1000" value="30000"></label><label>Wareneinsatz <output data-calc-rate-label>30 %</output><input data-calc-rate type="range" min="15" max="55" step="1" value="30"></label></div><div class="calc-stack" aria-hidden="true"><span data-calc-bar></span></div><div class="calc-key"><span><i></i>Wareneinsatz <b data-calc-cost>9.000 €</b></span><span><i></i>Vor weiteren Kosten <b data-calc-left>21.000 €</b></span></div><div class="mini-calc-result" aria-live="polite"><span>Ein Prozentpunkt entspricht hier</span><strong data-calc-point>300 €</strong><small>pro Monat</small></div></div></div></section>'''


def service_interlude(slug):
 kind=family(slug)
 return workflow(kind) if kind in {'ai','security'} else calculator(slug) if kind=='consulting' else ''

def enrich(path,content):
 slug=path.removesuffix('.html')
 if slug in {'impressum','datenschutz','404'} or 'class="service-hero"' in content or 'data-specialized-page' in content:return content
 first=content.find('<section class="hero"')
 if first>=0:
  shell=content.find('<div class="shell"',first);start=content.find('>',shell)+1;end=content.find('</section>',start);close=content.rfind('</div>',start,end)
  kind='technology' if slug in {'leistungen','kontakt','wissen'} else 'consulting' if slug in {'ueber-mich','werdegang','referenzen'} else family(slug)
  visual=hero_visual({'wissen-ki-im-hotel':'ki-entwicklung','wissen-getraenkevertrag':'getraenkevertraege','wissen-direktbuchungen':'webdesign'}.get(slug,slug)) if slug not in {'leistungen','kontakt','wissen','ueber-mich','werdegang','referenzen'} else '<div class="v-hub-owned">'+art(kind)+'</div>'
  actions=''
  if slug in {'fb-beratung','leistungen','ueber-mich','teamo-ki','kontakt'}:
   href='#projektanfrage' if slug=='kontakt' else 'kontakt.html?thema='+kind+'#projektanfrage'
   label='Projekt beschreiben' if slug=='kontakt' else TOPICS[kind]['cta'] if slug not in {'leistungen','ueber-mich'} else 'Projekt besprechen'
   actions='<div class="v-hub-actions"><a class="btn btn-1" href="'+href+'">'+label+' ↗</a></div>'
  content=content[:start]+'<div class="v-hub-grid"><div>'+content[start:close]+actions+'</div>'+visual+'</div>'+content[close:]
 # An addition only where it has a distinct job; references and marketing keep their own content.
 addition=brief() if slug=='kontakt' else workflow('ai') if slug in {'teamo-ki','wissen-ki-im-hotel'} else ''
 if not addition:return content
 end=content.find('</section>')
 return content[:end+10]+addition+content[end+10:] if end>=0 else addition+content
