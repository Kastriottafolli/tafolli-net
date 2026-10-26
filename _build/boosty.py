"""The original Boosty mascot as a lightweight, contextual website guide."""
import json
from html import escape as e

COPY={
 'de':dict(label='BOOSTY / IHR WEGWEISER',open='Boosty: Wegweiser öffnen',close='Schließen',pause='Animation pausieren',play='Animation aktivieren',hide='Ausblenden',show='Boosty anzeigen',intro='Hallo, ich bin Boosty.',note='Ihr Weg zu den passenden Leistungen.',product='Boosty kommt von Tafolli Boost',topics={
  'welcome':['Was möchten Sie voranbringen?','Eine neue Website, Social Media oder lokale Einträge? Hier finden Sie den passenden Einstieg.','index.html#digitaler-auftritt','Digitalen Auftritt entdecken'],
  'website':['Ihre Website. Ihr erster Eindruck.','Struktur, Design, Inhalte und Entwicklung – mit einem klaren Weg zur Anfrage.','webdesign.html','Website-Erstellung ansehen'],
  'social':['Ihre Marke im Gespräch.','Beiträge, Reels und laufende Betreuung für die Kanäle, auf denen Sie Ihre Kunden erreichen.','social-media.html','Social Media entdecken'],
  'local':['In Ihrer Nähe gefunden werden.','Unternehmensprofile, Karten und Verzeichnisse mit aktuellen Angaben zu Ihrem Betrieb.','suchmaschinenoptimierung.html#lokale-eintraege','Lokale Einträge ansehen'],
  'marketing':['Eine Marke. Viele Möglichkeiten.','Logos, Kampagnen, SEO und Print: Ihr Auftritt bekommt eine gemeinsame Richtung.','online-marketing.html','Marketing entdecken'],
  'technology':['Von Ihrer Idee zur Anwendung.','Individuelle Software, Web-Apps, iOS und Android – passend zu Ihren Abläufen.','softwareentwicklung.html','Software & Apps entdecken'],
  'consulting':['Klarheit für den nächsten Schritt.','Prozesse, Prioritäten und Wirtschaftlichkeit gemeinsam betrachten.','fb-beratung.html','Beratung kennenlernen'],
  'ai':['KI, die im Alltag unterstützt.','Assistenten und Workflows übernehmen vorbereitende Aufgaben. Menschen prüfen und entscheiden.','ki-automatisierung.html','KI-Automatisierung entdecken'],
  'contact':['Erzählen Sie uns von Ihrer Idee.','Beschreiben Sie Ihre Aufgabe. Wir klären gemeinsam Umfang und nächste Schritte.','kontakt.html#projektanfrage','Projekt besprechen']
 }),
 'en':dict(label='BOOSTY / YOUR GUIDE',open='Boosty: open the guide',close='Close',pause='Pause animation',play='Enable animation',hide='Hide',show='Show Boosty',intro="Hi, I’m Boosty.",note='Find the services that fit your project.',product='Boosty is from Tafolli Boost',topics={
  'welcome':['What would you like to build?','A new website, social media or local listings? Find your starting point here.','index.html#digitaler-auftritt','Explore your online presence'],
  'website':['Your website. Your first impression.','Structure, design, content and development with a clear route to an enquiry.','webdesign.html','Explore website creation'],
  'social':['Bring your brand into the conversation.','Posts, reels and ongoing support for the channels your customers use.','social-media.html','Explore social media'],
  'local':['Help nearby customers find you.','Business profiles, maps and directories with accurate information.','suchmaschinenoptimierung.html#lokale-eintraege','Explore local listings'],
  'marketing':['One brand. Many possibilities.','Logos, campaigns, SEO and print with a shared direction.','online-marketing.html','Explore marketing'],
  'technology':['Turn your idea into an application.','Custom software, web, iOS and Android apps for your workflows.','softwareentwicklung.html','Explore software & apps'],
  'consulting':['Clarity for your next step.','Review processes, priorities and business operations together.','fb-beratung.html','Explore consulting'],
  'ai':['AI that supports everyday work.','Assistants prepare information and workflows; people review and decide.','ki-automatisierung.html','Explore AI automation'],
  'contact':['Tell us about your idea.','Describe your task so we can establish the scope and next steps together.','kontakt.html#projektanfrage','Discuss your project']
 }),
 'sq':dict(label='BOOSTY / UDHËRRËFYESI JUAJ',open='Boosty: hap udhërrëfyesin',close='Mbyll',pause='Ndalo animacionin',play='Aktivizo animacionin',hide='Fshih',show='Shfaq Boosty',intro='Përshëndetje, unë jam Boosty.',note='Gjeni shërbimet e duhura për projektin tuaj.',product='Boosty vjen nga Tafolli Boost',topics={
  'welcome':['Çfarë dëshironi të zhvilloni?','Website, rrjete sociale apo regjistrime lokale? Gjeni pikënisjen tuaj këtu.','index.html#digitaler-auftritt','Zbuloni praninë online'],
  'website':['Website juaj. Përshtypja e parë.','Strukturë, dizajn, përmbajtje dhe zhvillim me një rrugë të qartë drejt kontaktit.','webdesign.html','Zbuloni krijimin e websiteve'],
  'social':['Marka juaj në bisedë.','Postime, reels dhe menaxhim për kanalet e klientëve tuaj.','social-media.html','Zbuloni rrjetet sociale'],
  'local':['Të gjendeni pranë klientëve.','Profile biznesi, harta dhe drejtori me të dhëna aktuale.','suchmaschinenoptimierung.html#lokale-eintraege','Zbuloni regjistrimet lokale'],
  'marketing':['Një markë. Shumë mundësi.','Logo, fushata, SEO dhe materiale të shtypura me një drejtim të përbashkët.','online-marketing.html','Zbuloni marketingun'],
  'technology':['Nga ideja te aplikacioni.','Softuer, aplikacione web, iOS dhe Android sipas proceseve tuaja.','softwareentwicklung.html','Zbuloni softuerin dhe aplikacionet'],
  'consulting':['Qartësi për hapin tjetër.','Shqyrtojmë proceset, prioritetet dhe ekonominë e biznesit.','fb-beratung.html','Zbuloni konsulencën'],
  'ai':['IA që ndihmon në përditshmëri.','Asistentët përgatisin informacionin; njerëzit kontrollojnë dhe vendosin.','ki-automatisierung.html','Zbuloni automatizimin me IA'],
  'contact':['Na tregoni idenë tuaj.','Përshkruani detyrën që të përcaktojmë hapat e ardhshëm.','kontakt.html#projektanfrage','Diskutoni projektin']
 })
}

def widget(lang='de',base='',path='index.html'):
 if path in {'impressum.html','datenschutz.html','404.html'}:return ''
 c=COPY[lang]
 topic='website' if path=='webdesign.html' else 'social' if path=='social-media.html' else 'local' if path=='suchmaschinenoptimierung.html' else 'marketing' if path in {'online-marketing.html','foto-video.html'} else 'contact' if path=='kontakt.html' else 'technology' if path in {'softwareentwicklung.html','app-entwicklung.html','cybersecurity.html','domain-hosting-email.html','digitalisierung.html'} else 'ai' if path in {'ki-automatisierung.html','ki-entwicklung.html','teamo-ki.html'} else 'welcome'
 topics={key:[*values[:2],base+values[2],values[3]] for key,values in c['topics'].items()}
 if lang!='de':topics['welcome'][2]='#digitaler-auftritt' if path in {'en/','sq/'} else base+lang+'/#digitaler-auftritt'
 config=json.dumps(dict(topics=topics,initial=topic,pause=c['pause'],play=c['play']),ensure_ascii=False).replace('<','\\u003c')
 links=''.join(f'<a href="{e(topics[key][2])}">{e(topics[key][3])}<span aria-hidden="true">↗</span></a>' for key in ['website','social','local'])
 return f'''<aside class="boosty-guide" data-boosty-guide hidden aria-label="{e(c['intro'])}">
 <div class="boosty-panel" id="boosty-panel" hidden><div class="boosty-panel-top"><span>{e(c['label'])}</span><button type="button" data-guide-close aria-label="{e(c['close'])}"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 6 12 12M18 6 6 18"/></svg></button></div><p class="boosty-intro">{e(c['intro'])}</p><h2 data-guide-title>{e(topics[topic][0])}</h2><p data-guide-copy>{e(topics[topic][1])}</p><a class="boosty-context-link" data-guide-link href="{e(topics[topic][2])}"><span data-guide-link-label>{e(topics[topic][3])}</span> <span aria-hidden="true">↗</span></a><nav class="boosty-shortcuts" aria-label="{e(c['note'])}">{links}</nav><a class="boosty-origin" href="https://tafolliboost.com/" target="_blank" rel="noopener noreferrer">{e(c['product'])} ↗</a><div class="boosty-options"><button type="button" data-guide-pause aria-pressed="false">{e(c['pause'])}</button><button type="button" data-guide-hide>{e(c['hide'])}</button></div></div>
 <button class="boosty-launcher" type="button" data-guide-toggle aria-controls="boosty-panel" aria-expanded="false" aria-label="{e(c['open'])}"><span class="boosty-satellite" aria-hidden="true"><i></i><i></i><i></i></span><span class="boosty-float"><img src="{base}assets/work/boosty.webp" width="1200" height="1200" alt="" decoding="async"></span><span class="boosty-name" aria-hidden="true">Boosty <b>+</b></span></button>
 <button class="boosty-restore" type="button" data-guide-show hidden>{e(c['show'])}</button>
 <script type="application/json" id="boosty-config">{config}</script></aside>'''
