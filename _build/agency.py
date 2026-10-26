"""Company-owned visual examples and a concise, linked capabilities catalogue."""
from html import escape as e
from brand import MARK


def art(kind='marketing',base='',variant=''):
 mark=f'<img src="{base}{MARK}" width="64" height="64" alt="">'
 if kind=='marketing':
  return f'''<div class="agency-art art-brand" aria-hidden="true"><div class="brand-poster"><span>TAFOLLI &amp; CO.</span><strong>Ideen.<br>Identität.<br>Wirkung.</strong><i></i><small>MARKETING &amp; DESIGN</small></div><div class="brand-card">{mark}<strong>TAFOLLI <small>&amp; CO.</small></strong><span>info@tafolli.net<br>tafolli.net</span></div><div class="brand-colours"><i></i><i></i><i></i><span>Brand system</span></div></div>'''
 if kind=='technology':
  return f'''<div class="agency-art art-platforms" aria-hidden="true"><div class="platform-browser"><span class="platform-top">tafolli.net / development</span><div class="platform-code"><small>BUILD SOMETHING USEFUL.</small><strong>&lt;your idea /&gt;</strong><span>Web · iOS · Android</span></div><div class="platform-modules"><i>Interface</i><i>API</i><i>Database</i></div></div><div class="platform-phone"><span></span><b>App.</b><i>iOS</i><i>Android</i></div><span class="art-caption">SOFTWARE · WEB · MOBILE · SECURITY</span></div>'''
 if kind=='security':
  return '<div class="agency-art art-security" aria-hidden="true"><div class="security-core"><svg viewBox="0 0 100 112" fill="none"><path d="M50 5 91 21v33c0 24-16 41-41 53C25 95 9 78 9 54V21Z" stroke="currentColor" stroke-width="3"/><path d="m30 55 14 14 28-31" stroke="currentColor" stroke-width="5"/></svg></div><span class="secure-label sl-one">Identität</span><span class="secure-label sl-two">Anwendungen</span><span class="secure-label sl-three">Daten</span><span class="secure-label sl-four">Wiederanlauf</span><span class="art-caption">CYBERSECURITY / SCHUTZ IM ZUSAMMENSPIEL</span></div>'
 if kind=='ai':
  return '<div class="agency-art art-automation" aria-hidden="true"><span class="automation-source">Anfrage<br><i>Dokument · E-Mail · Daten</i></span><span class="automation-line"></span><div class="automation-core">AI<span>ordnen · vorbereiten</span></div><span class="automation-line"></span><span class="automation-review">Prüfen &amp;<br>freigeben</span><span class="art-caption">WORKFLOWS MIT KLAREN ZUSTÄNDIGKEITEN</span></div>'
 if kind=='seo':
  return '<div class="agency-art art-search" aria-hidden="true"><div class="search-query">Ihre Leistung. Ihre Zielgruppe.<span>⌕</span></div><div class="search-result"><small>tafolli.net</small><strong>Marketing, Software &amp; KI | Tafolli &amp; Co.</strong><p>Leistungen verständlich erklären. Inhalte strukturieren. Den nächsten Schritt leicht machen.</p><span>Technik</span><span>Inhalte</span><span>Lokal</span></div><span class="art-caption">SUCHVORSCHAU / GESTALTUNGSBEISPIEL</span></div>'
 if kind=='social':
  return '<div class="agency-art art-social" aria-hidden="true"><div class="social-post"><small>TAFOLLI &amp; CO.</small><strong>Eine Idee.<br>Viele<br>Formate.</strong><span>CONTENT / 01</span></div><div class="social-reel"><small>9:16</small><span>▶</span><strong>Bewegung.<br>Mit Botschaft.</strong></div><span class="art-caption">REDAKTION · DESIGN · REELS · KAMPAGNEN</span></div>'
 if kind=='web':
  return f'<div class="agency-art art-web" aria-hidden="true"><div class="own-web"><span>{mark}<b>TAFOLLI &amp; CO.</b><i>Menü +</i></span><strong>Ein klarer<br>digitaler Auftritt.</strong><p>Inhalt. Gestaltung. Kontakt.</p><div><i>Leistungen</i><i>Projekt anfragen ↗</i></div></div><span class="art-caption">WEBDESIGN / GESTALTUNGSSKIZZE</span></div>'
 return '<div class="agency-art art-consulting" aria-hidden="true"><div class="consult-sheet"><small>VOM ÜBERBLICK ZUR ENTSCHEIDUNG</small><strong>Ein Plan.<br>Klare Prioritäten.</strong><div><span><i>01</i>Analysieren</span><span><i>02</i>Entscheiden</span><span><i>03</i>Umsetzen</span></div></div><span class="art-caption">PROZESSE · WIRTSCHAFTLICHKEIT · UMSETZUNG</span></div>'

CATALOGUE={
 'de':('DAS KÖNNEN WIR FÜR SIE UMSETZEN','Von der Visitenkarte<br>bis zur eigenen App.','Ein einzelner Auftrag oder ein verbundenes Projekt: Wählen Sie die Leistungen, die Sie gerade brauchen.',[
 ('01','Softwareentwicklung','Fachanwendungen, Portale & Schnittstellen','softwareentwicklung.html'),
 ('02','Website-Erstellung & Web-Apps','Unternehmensseiten, Landingpages & Shops','webdesign.html'),
 ('03','iOS- & Android-Apps','Mobile Anwendungen für Ihre Nutzer','app-entwicklung.html'),
 ('04','Cybersecurity','Zugänge, Anwendungen & Unternehmensdaten','cybersecurity.html'),
 ('05','Online-Marketing','Strategie, Werbung & Kampagnen','online-marketing.html#kampagnen'),
 ('06','Suchmaschinenoptimierung','Technisches SEO, Inhalte & lokale Suche','suchmaschinenoptimierung.html'),
 ('07','Social Media','Kanalstrategie, Beiträge, Reels & Betreuung','social-media.html'),
 ('08','Logos & Corporate Design','Markenidentität, Farben & Gestaltungssystem','online-marketing.html#marke'),
 ('09','Visitenkarten & Flyer','Printdesign, Broschüren & Werbemittel','online-marketing.html#print'),
 ('10','Foto, Video & Content','Inhalte für Marke, Website & Kampagnen','foto-video.html'),
 ('11','KI-Assistenten & Workflows','Dokumente, Anfragen & Abläufe automatisieren','ki-automatisierung.html'),
 ('12','Beratung & Digitalisierung','Prozesse, Organisation & Wirtschaftlichkeit','fb-beratung.html'),
 ('13','Lokale Einträge','Google, Apple Maps, Bing & Verzeichnisse','suchmaschinenoptimierung.html#lokale-eintraege')]),
 'en':('WHAT WE CAN BUILD FOR YOU','From a business card<br>to your own app.','A focused task or a connected project: choose the services you need now.',[
 ('01','Custom software','Business applications, portals & integrations','softwareentwicklung.html'),('02','Websites & web apps','Company sites, landing pages & commerce','webdesign.html'),('03','iOS & Android apps','Mobile applications for your users','app-entwicklung.html'),('04','Cybersecurity','Accounts, applications & business data','cybersecurity.html'),('05','Online marketing','Strategy, advertising & campaigns','online-marketing.html#kampagnen'),('06','Search engine optimisation','Technical SEO, content & local search','suchmaschinenoptimierung.html'),('07','Social media','Channels, posts, reels & ongoing support','social-media.html'),('08','Logos & brand identity','Visual identity, colours & design systems','online-marketing.html#marke'),('09','Business cards & flyers','Print design, brochures & marketing material','online-marketing.html#print'),('10','Photo, video & content','Content for brand, website & campaigns','foto-video.html'),('11','AI assistants & workflows','Automate documents, enquiries & processes','ki-automatisierung.html'),('12','Consulting & digitalisation','Processes, organisation & business operations','fb-beratung.html'),('13','Local listings','Google, Apple Maps, Bing & directories','suchmaschinenoptimierung.html#lokale-eintraege')]),
 'sq':('ÇFARË MUND TË REALIZOJMË PËR JU','Nga kartëvizita<br>te aplikacioni juaj.','Një detyrë e vetme ose një projekt i lidhur: zgjidhni shërbimet që ju duhen tani.',[
 ('01','Zhvillim softueri','Aplikacione biznesi, portale dhe integrime','softwareentwicklung.html'),('02','Website dhe aplikacione web','Faqe kompanie, landing pages dhe dyqane','webdesign.html'),('03','Aplikacione iOS dhe Android','Aplikacione mobile për përdoruesit tuaj','app-entwicklung.html'),('04','Siguri kibernetike','Llogari, aplikacione dhe të dhëna biznesi','cybersecurity.html'),('05','Marketing online','Strategji, reklama dhe fushata','online-marketing.html#kampagnen'),('06','Optimizim SEO','Teknikë, përmbajtje dhe kërkim lokal','suchmaschinenoptimierung.html'),('07','Rrjete sociale','Kanale, postime, reels dhe menaxhim','social-media.html'),('08','Logo dhe identitet vizual','Identitet marke, ngjyra dhe sistem dizajni','online-marketing.html#marke'),('09','Kartëvizita dhe fletushka','Dizajn shtypi, broshura dhe materiale','online-marketing.html#print'),('10','Foto, video dhe përmbajtje','Përmbajtje për markën dhe fushatat','foto-video.html'),('11','Asistentë dhe procese me AI','Automatizim dokumentesh dhe kërkesash','ki-automatisierung.html'),('12','Konsulencë dhe digjitalizim','Procese, organizim dhe ekonomi biznesi','fb-beratung.html'),('13','Regjistrime lokale','Google, Apple Maps, Bing dhe drejtori','suchmaschinenoptimierung.html#lokale-eintraege')]),
}

def catalogue(lang='de',base=''):
 label,title,text,items=CATALOGUE[lang]
 links=''.join(f'<a href="{base}{href}"><span>{n}</span><div><h3>{e(name)}</h3><p>{e(desc)}</p></div><b aria-hidden="true">↗</b></a>' for n,name,desc,href in items)
 return f'<section class="agency-catalogue" id="kompetenzen"><div class="shell"><div class="visual-section-heading"><div><p class="v-kicker">{label}</p><h2>{title}</h2></div><p>{e(text)}</p></div><div class="agency-catalogue-grid">{links}</div></div></section>'
