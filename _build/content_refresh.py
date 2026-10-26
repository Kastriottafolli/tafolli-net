"""Concrete, customer-focused homepage content in the three supported languages."""
from copy import deepcopy

EXTRA = {
 'de': {
  'hero_lines':['Marketing. Software.','KI-Automatisierung.'],
  'hero_text':'Wir machen Ihr Angebot sichtbar, entwickeln passende Anwendungen und verbinden Ihre Geschäftsprozesse. Mit Beratung, Umsetzung und Betreuung aus einem abgestimmten Projekt.',
  'services_title':'Was Ihr Unternehmen voranbringt.',
  'service_cards':[
   {'name':'Marketing','headline':'Sichtbar werden. Klar erkennbar bleiben.','text':'Von Positionierung und Markenauftritt bis zu Content, Werbung und Kampagnen. Abgestimmt auf Ihre Zielgruppe und den Weg zur Anfrage.','cta':'Marketing & Markenauftritt'},
   {'name':'Technology','headline':'Software, die zu Ihrem Alltag passt.','text':'Individuelle Software, Websites und Apps für iOS und Android. Wir verbinden Systeme und berücksichtigen Sicherheit von Anfang an.','cta':'Softwareentwicklung entdecken'},
   {'name':'Consulting','headline':'Klarheit für die nächsten Schritte.','text':'Prozesse, Verantwortlichkeiten und Kosten gemeinsam betrachten. Daraus entsteht ein umsetzbarer Plan – mit besonderer Erfahrung in Hotellerie und Gastronomie.','cta':'Unternehmensberatung ansehen'},
   {'name':'AI Automation','headline':'Weniger Routine. Mehr Freiraum.','text':'Anfragen, Dokumente und interne Informationen strukturiert verarbeiten. KI-Workflows mit definierten Datenquellen, Prüfungen und Freigaben.','cta':'KI-Automatisierung entdecken'}],
  'technology_title':'Von der Idee zur Anwendung.',
  'technology_text':'Kundenportal, internes Werkzeug oder mobile App: Die Anwendung richtet sich nach Ihren Nutzern und Abläufen. Wir klären Funktionen, Daten und Schnittstellen, entwickeln die Lösung und begleiten Einführung und Weiterentwicklung.',
  'approach_title':'Ein klarer Weg zur Umsetzung.',
  'approach_text':'Sie wissen, was entwickelt wird, wann Ihre Rückmeldung gebraucht wird und was zur Übergabe gehört.',
  'process':[
   {'title':'Verstehen & planen.','text':'Ziele, Nutzer, vorhandene Systeme und Budget klären. Sie erhalten ein Angebot mit Leistungsumfang, Zuständigkeiten und nächsten Schritten.'},
   {'title':'Umsetzen & prüfen.','text':'Entwürfe, Anwendungen oder Kampagnen schrittweise entwickeln. Zwischenergebnisse besprechen und anhand der vereinbarten Anforderungen prüfen.'},
   {'title':'Einführen & begleiten.','text':'Ergebnisse, Zugänge und Dokumentation geordnet übergeben. Pflege, Wartung oder laufende Betreuung auf Wunsch mit festem Umfang vereinbaren.'}],
  'contact_title':'Welche Aufgabe sollen wir lösen?',
  'contact_text':'Erzählen Sie uns von Ihrem Vorhaben, den vorhandenen Systemen und Ihrem Ziel. Gemeinsam klären wir einen sinnvollen Einstieg.',
  'use_label':'Konkrete Anwendungen','use_title':'Aus einer Aufgabe wird eine Lösung.',
  'use_cases':[
   ('Mehr passende Anfragen','Angebot und Zielgruppe schärfen, eine verständliche Website aufbauen und Kampagnen mit einem klaren Kontaktweg verbinden.','online-marketing.html','Marketing planen'),
   ('Informationen an einem Ort','Ein Kundenportal oder eine interne Anwendung bündelt Daten, Aufgaben und Freigaben. Bestehende Systeme werden über Schnittstellen angebunden.','softwareentwicklung.html','Software entwickeln'),
   ('Wiederkehrende Abläufe entlasten','Eingehende Dokumente oder Anfragen erfassen, Informationen zuordnen und den nächsten Schritt vorbereiten. Ihr Team prüft und gibt frei.','ki-automatisierung.html','Abläufe automatisieren')],
  'details_label':'Passende Leistungen',
  'details':[
   [('suchmaschinenoptimierung.html','SEO & Sichtbarkeit'),('social-media.html','Social Media & Content'),('foto-video.html','Foto & Video')],
   [('webdesign.html','Webdesign & Web-Apps'),('app-entwicklung.html','iOS- & Android-Apps'),('cybersecurity.html','Cybersecurity')],
   [('digitalisierung.html','Prozesse & Digitalisierung'),('fb-beratung.html','F&B-Consulting'),('revenue-controlling.html','Controlling')],
   [('ki-entwicklung.html','KI-Assistenten'),('ki-automatisierung.html#ki','Workflow-Beispiel'),('teamo-ki.html','TeamO für Hospitality')]],
  'faq':[
   ('Welche Leistungen bietet Tafolli & Co. an?','Wir verbinden Marketing, individuelle Softwareentwicklung, Unternehmensberatung und KI-Automatisierung. Dazu gehören Markenauftritt, Kampagnen, Websites, Web-Apps, mobile Apps, Schnittstellen und Cybersecurity. Einzelne Leistungen können separat beauftragt werden.'),
   ('Entwickeln Sie Apps für iOS und Android?','Ja. Wir planen und entwickeln mobile Anwendungen für iPhone, iPad und Android sowie browserbasierte Web-Apps. Funktionen, Geräte, Schnittstellen und die passende technische Umsetzung legen wir gemeinsam fest.'),
   ('Kann bestehende Software eingebunden werden?','Häufig ja. Zuerst prüfen wir verfügbare Schnittstellen, Zugänge, Datenqualität und Lizenzbedingungen. Auf dieser Grundlage planen wir die Verbindung oder eine geeignete Alternative.'),
   ('Wie starten wir und was kostet ein Projekt?','Im Erstgespräch klären wir Ziele, Ausgangslage und den gewünschten Umfang. Danach erhalten Sie ein Angebot mit Leistungen, Zuständigkeiten und Kosten. Erweiterungen werden vor ihrer Umsetzung abgestimmt.'),
   ('Wie werden KI-Abläufe geprüft?','Wir legen Datenquellen, Regeln und Prüffälle fest. Kritische Ergebnisse können zur menschlichen Freigabe vorbereitet werden. Ein abgegrenzter erster Workflow zeigt, wie sich die Lösung im Betrieb einsetzen lässt.'),
   ('Ist eine laufende Betreuung möglich?','Ja. Marketingbetreuung, Websitepflege, Softwarewartung und die Begleitung von KI-Workflows können mit einem definierten Umfang vereinbart werden. Die Zusammenarbeit ist auch aus der Ferne möglich.')]
 },
 'en': {
  'hero_lines':['Marketing. Software.','AI automation.'],
  'hero_text':'We make your offer visible, develop applications that fit and connect your business processes. Consulting, delivery and support are coordinated around your project.',
  'services_title':'Services that move your business forward.',
  'service_cards':[
   {'name':'Marketing','headline':'Get seen. Be recognised.','text':'From positioning and brand presence to content, advertising and campaigns. Built around your audience and a clear path to an enquiry.','cta':'Marketing & brand presence'},
   {'name':'Technology','headline':'Software that fits your working day.','text':'Custom software, websites and apps for iOS and Android. We connect systems and consider security from the start.','cta':'Explore software development'},
   {'name':'Consulting','headline':'Clarity for your next steps.','text':'Review processes, responsibilities and costs together. Turn the findings into a practical plan, informed by particular experience in hospitality.','cta':'Explore business consulting'},
   {'name':'AI Automation','headline':'Less routine. More room to work.','text':'Process enquiries, documents and internal information in a structured way. AI workflows with defined sources, checks and approvals.','cta':'Explore AI automation'}],
  'technology_title':'From the idea to the application.',
  'technology_text':'A customer portal, internal tool or mobile app: the application follows your users and workflows. We define functions, data and integrations, develop the solution and support its introduction and ongoing development.',
  'approach_title':'A clear path to delivery.',
  'approach_text':'You know what is being developed, when your feedback is needed and what the handover includes.',
  'process':[
   {'title':'Understand & plan.','text':'Establish goals, users, existing systems and budget. Receive a proposal setting out the scope, responsibilities and next steps.'},
   {'title':'Develop & review.','text':'Develop designs, applications or campaigns step by step. Review interim results against the agreed requirements.'},
   {'title':'Introduce & support.','text':'Hand over results, access details and documentation. Arrange maintenance or ongoing support with a defined scope if needed.'}],
  'contact_title':'What should we help you solve?',
  'contact_text':'Tell us about the project, your existing systems and your goal. Together, we will identify a sensible starting point.',
  'use_label':'Practical applications','use_title':'Turn a task into a solution.',
  'use_cases':[
   ('More relevant enquiries','Clarify your offer and audience, build an understandable website and connect campaigns to a clear contact route.','online-marketing.html','Plan your marketing'),
   ('Information in one place','A customer portal or internal application brings data, tasks and approvals together. Integrations connect existing systems.','softwareentwicklung.html','Develop software'),
   ('Support recurring workflows','Capture incoming documents or enquiries, organise information and prepare the next step. Your team reviews and approves.','ki-automatisierung.html','Automate workflows')],
  'details_label':'Related services',
  'details':[
   [('suchmaschinenoptimierung.html','SEO & visibility'),('social-media.html','Social media & content'),('foto-video.html','Photo & video')],
   [('webdesign.html','Websites & web apps'),('app-entwicklung.html','iOS & Android apps'),('cybersecurity.html','Cybersecurity')],
   [('digitalisierung.html','Processes & digitalisation'),('fb-beratung.html','F&B consulting'),('revenue-controlling.html','Management reporting')],
   [('ki-entwicklung.html','AI assistants'),('ki-automatisierung.html#ki','Workflow example'),('teamo-ki.html','TeamO for hospitality')]],
  'faq':[
   ('What does Tafolli & Co. offer?','We bring marketing, custom software development, business consulting and AI automation together. Services include branding, campaigns, websites, web and mobile apps, integrations and cybersecurity. Individual services can be commissioned separately.'),
   ('Do you develop iOS and Android apps?','Yes. We plan and develop apps for iPhone, iPad and Android as well as browser-based web apps. Functions, devices, integrations and the appropriate technical approach are agreed together.'),
   ('Can existing software be connected?','Often, yes. We first check available APIs, access, data quality and licence conditions. This provides the basis for an integration or an appropriate alternative.'),
   ('How do we start and what does a project cost?','The initial discussion establishes goals, the starting point and scope. You then receive a proposal with services, responsibilities and costs. Extensions are agreed before implementation.'),
   ('How are AI workflows checked?','We define data sources, rules and test cases. Important results can be prepared for human approval. A focused first workflow shows how the solution can be used in day-to-day operations.'),
   ('Is ongoing support available?','Yes. Marketing support, website care, software maintenance and AI workflow support can be arranged with a defined scope. We can also work remotely.')]
 },
 'sq': {
  'hero_lines':['Marketing. Softuer.','Automatizim me IA.'],
  'hero_text':'E bëjmë ofertën tuaj të dukshme, zhvillojmë aplikacione të përshtatshme dhe lidhim proceset e biznesit tuaj. Konsulencë, zbatim dhe mbështetje të koordinuara për projektin tuaj.',
  'services_title':'Shërbime që e çojnë biznesin përpara.',
  'service_cards':[
   {'name':'Marketing','headline':'Bëhuni të dukshëm dhe të dallueshëm.','text':'Nga pozicionimi dhe identiteti i markës te përmbajtja, reklamat dhe fushatat. Sipas audiencës suaj dhe një rruge të qartë drejt kontaktit.','cta':'Marketing dhe identitet i markës'},
   {'name':'Technology','headline':'Softuer që i përshtatet punës suaj.','text':'Softuer i personalizuar, faqe web dhe aplikacione për iOS e Android. Lidhim sistemet dhe marrim parasysh sigurinë që në fillim.','cta':'Zbuloni zhvillimin e softuerit'},
   {'name':'Consulting','headline':'Qartësi për hapat e ardhshëm.','text':'Shqyrtojmë proceset, përgjegjësitë dhe kostot. Nga gjetjet krijohet një plan konkret, me përvojë të veçantë në hoteleri e gastronomi.','cta':'Zbuloni konsulencën'},
   {'name':'AI Automation','headline':'Më pak rutinë. Më shumë hapësirë.','text':'Përpunim i strukturuar i kërkesave, dokumenteve dhe informacionit të brendshëm. Procese me IA, burime të përcaktuara, kontrolle dhe miratime.','cta':'Zbuloni automatizimin me IA'}],
  'technology_title':'Nga ideja te aplikacioni.',
  'technology_text':'Portal për klientët, mjet i brendshëm apo aplikacion mobil: zgjidhja ndjek përdoruesit dhe proceset tuaja. Përcaktojmë funksionet, të dhënat dhe integrimet, zhvillojmë aplikacionin dhe mbështesim futjen në përdorim e zhvillimin e mëtejshëm.',
  'approach_title':'Një rrugë e qartë drejt zbatimit.',
  'approach_text':'E dini çfarë zhvillohet, kur nevojitet reagimi juaj dhe çfarë përfshin dorëzimi.',
  'process':[
   {'title':'Kuptim dhe planifikim.','text':'Sqarojmë qëllimet, përdoruesit, sistemet ekzistuese dhe buxhetin. Merrni një ofertë me përmbajtjen, përgjegjësitë dhe hapat e ardhshëm.'},
   {'title':'Zhvillim dhe kontroll.','text':'Zhvillojmë dizajnet, aplikacionet ose fushatat hap pas hapi. Rezultatet ndërmjetëse shqyrtohen sipas kërkesave të dakorduara.'},
   {'title':'Përdorim dhe mbështetje.','text':'Dorëzojmë rezultatet, qasjet dhe dokumentacionin. Mirëmbajtja dhe mbështetja e vazhdueshme dakordohen me përmbajtje të përcaktuar.'}],
  'contact_title':'Cilën detyrë dëshironi të zgjidhim?',
  'contact_text':'Na tregoni për projektin, sistemet ekzistuese dhe qëllimin tuaj. Së bashku përcaktojmë një pikënisje të arsyeshme.',
  'use_label':'Zbatime konkrete','use_title':'Nga një detyrë te një zgjidhje.',
  'use_cases':[
   ('Kërkesa më të përshtatshme','Qartësoni ofertën dhe audiencën, ndërtoni një faqe të kuptueshme dhe lidhni fushatat me një rrugë të qartë kontakti.','online-marketing.html','Planifikoni marketingun'),
   ('Informacion në një vend','Një portal ose aplikacion i brendshëm bashkon të dhënat, detyrat dhe miratimet. Integrimet lidhin sistemet ekzistuese.','softwareentwicklung.html','Zhvilloni softuerin'),
   ('Lehtësoni proceset rutinë','Regjistroni dokumentet ose kërkesat hyrëse, organizoni informacionin dhe përgatitni hapin tjetër. Ekipi juaj kontrollon dhe miraton.','ki-automatisierung.html','Automatizoni proceset')],
  'details_label':'Shërbime të lidhura',
  'details':[
   [('suchmaschinenoptimierung.html','SEO dhe dukshmëria'),('social-media.html','Rrjete sociale dhe përmbajtje'),('foto-video.html','Foto dhe video')],
   [('webdesign.html','Faqe dhe aplikacione web'),('app-entwicklung.html','Aplikacione iOS dhe Android'),('cybersecurity.html','Siguri kibernetike')],
   [('digitalisierung.html','Procese dhe digjitalizim'),('fb-beratung.html','Konsulencë F&B'),('revenue-controlling.html','Kontrolli i biznesit')],
   [('ki-entwicklung.html','Asistentë me IA'),('ki-automatisierung.html#ki','Shembull procesi'),('teamo-ki.html','TeamO për hoteleri')]],
  'faq':[
   ('Çfarë ofron Tafolli & Co.?','Bashkojmë marketingun, zhvillimin e softuerit, konsulencën dhe automatizimin me IA. Shërbimet përfshijnë markën, fushatat, faqet web, aplikacionet, integrimet dhe sigurinë kibernetike. Shërbimet mund të porositen veçmas.'),
   ('Zhvilloni aplikacione për iOS dhe Android?','Po. Planifikojmë dhe zhvillojmë aplikacione për iPhone, iPad e Android dhe aplikacione web. Funksionet, pajisjet, integrimet dhe qasja teknike përcaktohen së bashku.'),
   ('Mund të lidhet softueri ekzistues?','Shpesh po. Fillimisht kontrollojmë API-të, qasjet, cilësinë e të dhënave dhe kushtet e licencës. Më pas planifikojmë integrimin ose një alternativë të përshtatshme.'),
   ('Si fillojmë dhe sa kushton projekti?','Në bisedën fillestare sqarojmë qëllimet, gjendjen dhe përmbajtjen e dëshiruar. Më pas merrni ofertë me shërbimet, përgjegjësitë dhe kostot. Zgjerimet dakordohen para zbatimit.'),
   ('Si kontrollohen proceset me IA?','Përcaktojmë burimet, rregullat dhe rastet e testimit. Rezultatet e rëndësishme mund të përgatiten për miratim njerëzor. Një proces fillestar i kufizuar tregon përdorimin në punën e përditshme.'),
   ('Ofrohet mbështetje e vazhdueshme?','Po. Marketingu, kujdesi për faqet web, mirëmbajtja e softuerit dhe proceset me IA mund të mbështeten me përmbajtje të përcaktuar. Bashkëpunimi është i mundur edhe në distancë.')]
 }
}

# Overview text stays concise; detailed disciplines live on their dedicated pages.
EXTRA['de']['services_title']='Marketing. Technologie. Beratung. KI.'
EXTRA['de']['service_cards'][0].update(headline='Marke, Marketing & Design.',text='Logos und Corporate Design, Websites, SEO, Social Media und Kampagnen. Dazu Visitenkarten, Flyer und weitere Werbemittel – einzeln oder als abgestimmter Markenauftritt.',cta='Marketingleistungen ansehen')
EXTRA['de']['service_cards'][1].update(headline='Individuelle Software & Apps.',text='Unternehmenssoftware, Webanwendungen und Apps für iOS und Android. Von den ersten Funktionen bis zu Schnittstellen, Cybersecurity und laufender Weiterentwicklung.')
EXTRA['de']['service_cards'][2].update(headline='Betriebliche Entscheidungen umsetzen.',text='Organisation, Prozesse, Einkauf und Controlling. Wir klären Prioritäten und begleiten die Umsetzung – mit besonderer Erfahrung in Hotellerie und Gastronomie.')
EXTRA['de']['service_cards'][3].update(headline='KI-Assistenten & automatisierte Abläufe.',text='Dokumente verarbeiten, Anfragen strukturieren und Wissen zugänglich machen. Mit passenden Systemanbindungen, definierten Regeln und menschlichen Freigaben.')
EXTRA['de']['details'][0]=[('online-marketing.html#marke','Logo & Corporate Design'),('suchmaschinenoptimierung.html','SEO'),('social-media.html','Social Media'),('online-marketing.html#print','Visitenkarten & Flyer')]
EXTRA['en']['service_cards'][0].update(headline='Brand, marketing & design.',text='Logos and brand identity, websites, SEO, social media and campaigns. Plus business cards, flyers and other marketing materials, individually or as a coordinated brand presence.')
EXTRA['sq']['service_cards'][0].update(headline='Markë, marketing dhe dizajn.',text='Logo, identitet vizual, website, SEO, rrjete sociale dhe fushata. Gjithashtu kartëvizita, fletushka dhe materiale të tjera marketingu.')

# The online presence services are a prominent, concrete entry point.
EXTRA['de']['hero_text']='Wir gestalten Websites, betreuen Social Media und machen Ihren Betrieb lokal auffindbar. Dazu entwickeln wir individuelle Software und KI-Automatisierungen – mit Beratung, Umsetzung und laufender Betreuung.'
EXTRA['en']['hero_text']='We build websites, manage social media and help local customers find your business. We also develop custom software and AI automation, with consulting, delivery and ongoing support.'
EXTRA['sq']['hero_text']='Krijojmë website, menaxhojmë rrjete sociale dhe e bëjmë biznesin tuaj më të lehtë për t’u gjetur në zonë. Zhvillojmë edhe softuer dhe automatizime me IA, me konsulencë dhe mbështetje.'
EXTRA['de']['service_cards'][0]['text']='Website-Erstellung, SEO, lokale Einträge und Social Media. Dazu Logos, Kampagnen, Visitenkarten und Flyer – einzeln beauftragbar oder als gemeinsamer Markenauftritt.'
EXTRA['de']['details'][0]=[('webdesign.html','Website-Erstellung'),('social-media.html','Social Media'),('suchmaschinenoptimierung.html#lokale-eintraege','Lokale Einträge'),('online-marketing.html#print','Design & Print')]
EXTRA['en']['details'][0]=[('webdesign.html','Website creation'),('social-media.html','Social media'),('suchmaschinenoptimierung.html#lokale-eintraege','Local listings'),('online-marketing.html#print','Design & print')]
EXTRA['sq']['details'][0]=[('webdesign.html','Krijim website'),('social-media.html','Rrjete sociale'),('suchmaschinenoptimierung.html#lokale-eintraege','Regjistrime lokale'),('online-marketing.html#print','Dizajn dhe shtyp')]

from search_faq import FAQ as SEARCH_FAQ
for language,questions in SEARCH_FAQ.items():
    EXTRA[language]['faq']=questions

META = {
 'de':('Webdesign, Marketing, Software & KI | Tafolli & Co.','Websites erstellen lassen, Social Media betreuen und lokal sichtbar werden. Dazu individuelle Software, Apps und KI-Automatisierung. Jetzt Ihr Projekt besprechen.'),
 'en':('Marketing, Software & AI Automation | Tafolli & Co.','Website creation, social media management and local listings. Custom software, apps, consulting and AI automation for your business. Discuss your project.'),
 'sq':('Marketing, Softuer & Automatizim me IA | Tafolli & Co.','Krijim website, menaxhim i rrjeteve sociale dhe regjistrime lokale. Softuer, aplikacione, konsulencë dhe automatizim me IA. Diskutoni projektin tuaj.')
}

def content(lang,home,presentation):
    c,p=deepcopy(home),deepcopy(presentation)
    extra=EXTRA[lang]
    p.update({key:value for key,value in extra.items() if key in p})
    c.update(title=META[lang][0],description=META[lang][1],faq=extra['faq'])
    return c,p,extra
