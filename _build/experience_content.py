"""Localized copy for the interactive automation experience.

Business credentials and the long-form FAQs stay in inhalt_*.py.
Demo examples are fictional and savings are explicitly estimates.
"""

COPY = {
    'de': {
        'title': 'Kastriot Tafolli · AI Automation, die Freiraum schafft',
        'description': 'AI Automation as a Service: individuelle KI-Workflows, Integration und laufende Betreuung von Kastriot Tafolli. Für Hotellerie, Gastronomie und Unternehmen.',
        'nav': ['Automation', 'Leistungen', 'Über mich', 'Kontakt'],
        'talk': 'Projekt besprechen', 'menu': 'Menü', 'motion': 'Bewegung',
        'status': 'OFFEN FÜR NEUE PROJEKTE', 'location': 'OSTSEEBAD BINZ',
        'hero': ['WENIGER', 'ROUTINE.', 'Mehr möglich.'],
        'hero_text': 'Ich baue KI-Systeme, die Arbeit übernehmen. Damit Ihr Team wieder Zeit für das hat, was Menschen am besten können.',
        'hero_cta': 'Entdecken Sie Automation', 'hero_link': 'Lernen wir uns kennen',
        'art_label': 'MENSCHLICHE IDEEN. INTELLIGENTE SYSTEME.',
        'scroll': 'SCROLLEN & ENTDECKEN', 'intro': 'TECHNOLOGIE MIT GESPÜR FÜR MENSCHEN',
        'manifesto': ['Ihr nächster', 'Mitarbeiter', 'ist ein System.'],
        'manifesto_text': 'Eine Anfrage um 23:48 Uhr. Eine Rechnung, die niemand abtippen möchte. Ein Bericht, der morgens fertig sein sollte. Genau da beginnt gute Automatisierung.',
        'manifesto_small': 'Sie geben die Richtung vor. Ich verbinde Ihre Abläufe, Ihre Systeme und KI zu etwas, das im Alltag wirklich hilft.',
        'service_label': 'DAS ANGEBOT', 'service_title': ['AI Automation', 'as a Service.'],
        'service_text': 'Für Ihr Unternehmen gebaut. In Ihre bestehenden Systeme integriert. Von mir laufend betreut. Vom ersten Workflow bis zum nächsten Schritt.',
        'service_tags': ['Individuelle Workflows', 'Menschliche Kontrolle', 'Laufende Betreuung'],
        'lab_label': '01 / AUTOMATION ZUM AUSPROBIEREN', 'lab_title': ['Keine Blackbox.', 'Ein Aha-Moment.'],
        'lab_text': 'Wählen Sie einen Ablauf und schicken Sie ihn durch die Demo. So wird aus einer kleinen Routine ein intelligenter Workflow.',
        'demo_label': 'INTERAKTIVE DEMO · FIKTIVE BEISPIELDATEN',
        'scenarios': ['Kundenanfrage', 'Rechnung', 'E-Mail'],
        'stages': ['Eingang', 'Verstehen', 'Handeln', 'Prüfen', 'Ergebnis'],
        'stage_notes': [
            'Eine neue Anfrage kommt an. Ihr Team muss noch nichts tun.',
            'Die KI erkennt Absicht, Sprache und wichtige Informationen.',
            'Der Workflow bereitet die passende Aktion in Ihrem System vor.',
            'Regeln prüfen das Ergebnis. Unklare Fälle gehen an Ihr Team.',
            'Der Vorgang ist vorbereitet, dokumentiert und bereit zur Freigabe.'
        ],
        'incoming': 'EINGANG', 'outgoing': 'ERGEBNIS', 'ready': 'Bereit für einen Testlauf',
        'run': 'Workflow starten', 'running': 'Workflow läuft', 'replay': 'Noch einmal abspielen',
        'demo_hint': 'Eine Simulation zur Erklärung. Es werden keine Nachrichten versendet oder Buchungen vorgenommen.',
        'demos': [
            {'source': 'KUNDENANFRAGE / 23:48', 'subject': 'Ein Gespräch nächste Woche?', 'message': 'Guten Abend! Haben Sie am 16. oder 17. Oktober Zeit für ein kurzes Gespräch? Es geht um eine Website und einen Ablauf, den wir automatisieren wollen.', 'fields': ['Absicht: Terminanfrage', 'Zeitraum: 16.–17. Oktober', 'Thema: Website und Automatisierung'], 'result_title': 'Persönliche Antwort vorbereitet.', 'result': 'Terminanfrage und Thema erkannt. Offene Punkte zur Prüfung an Ihr Team übergeben. Antwortentwurf liegt bereit.', 'receipt': 'ANFRAGE STRUKTURIERT · FREIGABE DURCH IHR TEAM'},
            {'source': 'BUCHHALTUNG / 09:12', 'subject': 'Eine Rechnung. Kein Abtippen.', 'message': 'Rechnung #2026-1042 · Musterlieferant GmbH · 840,00 € netto + 159,60 € USt. · Gesamt: 999,60 € · Fällig: 30. Oktober.', 'fields': ['Beleg: Rechnung #2026-1042', 'Gesamtbetrag: 999,60 €', 'Fälligkeit: 30. Oktober'], 'result_title': 'Beleg erfasst. Zahlen geprüft.', 'result': 'Lieferant, Positionen und Beträge ausgelesen. Nettobetrag und Umsatzsteuer abgeglichen. Buchungsvorschlag zur Freigabe vorbereitet.', 'receipt': 'BELEG STRUKTURIERT · FREIGABE DURCH BUCHHALTUNG'},
            {'source': 'POSTEINGANG / 14:06', 'subject': 'Die richtige Nachricht. Beim richtigen Team.', 'message': 'Hallo, wir planen ein internes Projekt mit 40 Personen. Könnten Sie uns ein Angebot für Einführung und Schulung schicken?', 'fields': ['Absicht: Projektanfrage', 'Teilnehmende: 40 Personen', 'Ziel: Ihr Team'], 'result_title': 'Anfrage sortiert. Team informiert.', 'result': 'Projektanfrage erkannt und dem richtigen Team zugeordnet. Fehlende Angaben markiert. Rückfrage zu Datum und Umfang als Entwurf vorbereitet.', 'receipt': 'ANFRAGE ZUGEORDNET · ANTWORTENTWURF BEREIT'}
        ],
        'care_label': '02 / MEHR ALS EIN EINMALIGES SETUP', 'care_title': ['Läuft.', 'Und wird besser.'],
        'care_text': 'Automation as a Service heißt: Ich begleite Ihr System auch nach dem Start. Wenn sich Ihr Betrieb verändert, entwickelt sich Ihr Workflow mit.',
        'care_items': [('Verbinden', 'Ihre Tools bleiben. Ich baue die Verbindung zwischen Posteingang, Dokumenten und Team.'), ('Betreuen', 'Antworten prüfen, Fehler erkennen, Kosten beobachten und bei Bedarf eingreifen.'), ('Weiterentwickeln', 'Neue Abläufe ergänzen, Regeln anpassen und aus echten Rückmeldungen lernen.')],
        'care_note': 'IHR TEAM BEHÄLT DAS LETZTE WORT.', 'care_orbit': ['TOOLS', 'KI', 'TEAM', 'BETREUUNG'],
        'roi_label': '03 / IHR POTENZIAL', 'roi_title': ['Zeit ist wertvoll.', 'Holen Sie sie zurück.'],
        'roi_text': 'Was könnte ein automatisierter Ablauf freimachen? Verändern Sie die Werte und entdecken Sie eine mögliche Größenordnung.',
        'roi_labels': ['Vorgänge pro Arbeitstag', 'Minuten pro Vorgang', 'Interner Stundensatz', 'Automatisierbarer Anteil'],
        'roi_units': ['Vorgänge', 'Min.', '€', '%'], 'hours': 'Stunden / Monat', 'value': 'Rechnerischer Zeitwert / Monat',
        'roi_note': 'Modellrechnung mit 22 Arbeitstagen pro Monat. Zeitwert vor Servicekosten, keine garantierte Einsparung. Der tatsächliche Anteil hängt vom Workflow ab.',
        'roi_cta': 'Mein Potenzial besprechen',
        'services_label': '04 / WAS ICH NOCH BEWEGE', 'services_title': ['Eine Perspektive.', 'Viele Möglichkeiten.'],
        'services': [('01', 'AI & AUTOMATION', 'Ein System, das mitarbeitet.', 'Individuelle KI-Workflows, laufende Betreuung und TeamO als digitaler Mitarbeiter.', 'ki-automatisierung.html', 'Automation ansehen'), ('02', 'F&B-BERATUNG', 'Bessere Abläufe. Bessere Zahlen.', 'Operative Erfahrung für Einkauf, Wareneinsatz, Verträge und Führung in Ihrem Haus.', 'fb-beratung.html', 'F&B entdecken'), ('03', 'DIGITAL & WEB', 'Ein Auftritt, der etwas bewegt.', 'Websites, Sichtbarkeit und Online-Marketing mit einem klaren Ziel: mehr direkte Anfragen.', 'online-marketing.html', 'Digital entdecken')],
        'about_label': '05 / DER MENSCH HINTER DEN SYSTEMEN', 'about_title': ['Ich kenne den Alltag.', 'Und den Code.'],
        'about_text': 'Ich bin Kastriot Tafolli. Über 15 Jahre Führung in der 5-Sterne-Hotellerie haben mir gezeigt, wo Zeit verloren geht. Als Softwareingenieur mit Schwerpunkt KI baue ich die Systeme, die genau dort ansetzen.',
        'about_link': 'Mehr über mich', 'about_caption': 'KASTRIOT TAFOLLI / TB SOLUTIONS',
        'credentials': [('15+', 'Jahre 5-Sterne-Hotellerie'), ('200+', 'Mitarbeitende gleichzeitig geführt'), ('50+', 'Nachwuchskräfte ausgebildet')],
        'experience_label': 'BERUFLICHE STATIONEN',
        'process_label': '06 / VON DER IDEE IN DEN ALLTAG', 'process_title': ['Groß denken.', 'Konkret anfangen.'],
        'process': [('Zuhören.', 'Wir sprechen über Ihren Betrieb, Ihre Engpässe und den Ablauf, der wirklich Zeit kostet.'), ('Bauen.', 'Ein klar begrenzter erster Workflow. Mit Ihren Tools, Ihren Regeln und Tests mit Ihrem Team.'), ('Begleiten.', 'Nach dem Start beobachte ich die Ergebnisse und entwickle das System mit Ihnen weiter.')],
        'faq_label': '07 / GUTE FRAGEN', 'faq_title': 'Noch etwas offen?',
        'cta_label': 'DER NÄCHSTE SCHRITT IST EIN GESPRÄCH.', 'cta_title': ['Was wäre, wenn', 'das einfach', 'laufen würde?'],
        'cta_text': 'Erzählen Sie mir von einem Ablauf, der Sie Zeit kostet. Wir finden heraus, was möglich ist.',
        'cta_button': 'Lassen Sie uns sprechen', 'cta_note': '30 MINUTEN. UNVERBINDLICH. MENSCH ZU MENSCH.',
        'footer_tag': 'MENSCHLICH DENKEN. INTELLIGENT HANDELN.', 'top': 'Zurück nach oben',
        'detail_hero': ['INTELLIGENTE', 'ABLÄUFE.', 'Mehr Freiraum.'],
        'story_label': 'VOM DURCHEINANDER ZUM ZUSAMMENSPIEL',
        'story_titles': ['Zu viele Handgriffe.', 'Ein verbundenes System.', 'Mehr Zeit für Menschen.'],
        'story_copies': ['Posteingang, Belege, Anrufe. Jede kleine Aufgabe zieht Aufmerksamkeit vom Wesentlichen ab.', 'Ihre Informationen finden ihren Weg. Die KI strukturiert, Regeln prüfen, Ihr Team entscheidet.', 'Weniger hin und her. Mehr Raum für Kunden, Ideen und die Arbeit, die Sie voranbringt.'],
        'story_tasks': ['E-MAIL', 'RECHNUNG', 'ANRUF', 'BERICHT', 'ANFRAGE', 'DATEN'],
        'story_outcome': 'FREIRAUM',
    },
    'en': {
        'title': 'Kastriot Tafolli · AI automation that makes room for more',
        'description': 'AI Automation as a Service: custom AI workflows, integration and ongoing care by Kastriot Tafolli. For hospitality, restaurants and businesses.',
        'nav': ['Automation', 'Services', 'About me', 'Contact'], 'talk': 'Let’s talk', 'menu': 'Menu', 'motion': 'Motion',
        'status': 'OPEN FOR NEW PROJECTS', 'location': 'OSTSEEBAD BINZ',
        'hero': ['LESS', 'ROUTINE.', 'More possible.'],
        'hero_text': 'I build AI systems that take work off your hands. So your team can get back to what people do best.',
        'hero_cta': 'Discover automation', 'hero_link': 'Let’s get to know each other', 'art_label': 'HUMAN IDEAS. INTELLIGENT SYSTEMS.',
        'scroll': 'SCROLL TO DISCOVER', 'intro': 'TECHNOLOGY WITH A FEEL FOR PEOPLE',
        'manifesto': ['Your next', 'team member', 'is a system.'],
        'manifesto_text': 'An enquiry at 11:48 pm. An invoice nobody wants to type up. A report that should be ready in the morning. That’s where good automation begins.',
        'manifesto_small': 'You set the direction. I connect your processes, your tools and AI into something that makes everyday work easier.',
        'service_label': 'THE OFFER', 'service_title': ['AI Automation', 'as a Service.'],
        'service_text': 'Built for your business. Connected to your existing tools. Continuously managed by me. From the first workflow to the next opportunity.',
        'service_tags': ['Custom workflows', 'Human oversight', 'Ongoing care'],
        'lab_label': '01 / EXPERIENCE AUTOMATION', 'lab_title': ['No black box.', 'A lightbulb moment.'],
        'lab_text': 'Choose a process and run it through the demo. See an everyday task become an intelligent workflow.',
        'demo_label': 'INTERACTIVE DEMO · FICTIONAL SAMPLE DATA', 'scenarios': ['Customer enquiry', 'Invoice', 'Email'],
        'stages': ['Receive', 'Understand', 'Act', 'Check', 'Result'],
        'stage_notes': ['A new request arrives. Your team doesn’t need to act yet.', 'AI identifies intent, language and key information.', 'The workflow prepares the right action in your system.', 'Rules check the result. Unclear cases go to your team.', 'The request is structured, documented and ready for approval.'],
        'incoming': 'INPUT', 'outgoing': 'OUTPUT', 'ready': 'Ready for a test run', 'run': 'Run workflow', 'running': 'Workflow running', 'replay': 'Play again',
        'demo_hint': 'An explanatory simulation. No messages are sent and no bookings are made.',
        'demos': [
            {'source': 'CUSTOMER ENQUIRY / 23:48', 'subject': 'A call next week?', 'message': 'Good evening! Do you have time on 16 or 17 October for a short call? It is about a website and a workflow we want to automate.', 'fields': ['Intent: meeting request', 'Dates: 16–17 October', 'Topic: website and automation'], 'result_title': 'A personal response, prepared.', 'result': 'Meeting request and topic identified. Open points passed to your team for checking. A response draft is ready.', 'receipt': 'REQUEST STRUCTURED · YOUR TEAM APPROVES'},
            {'source': 'ACCOUNTING / 09:12', 'subject': 'An invoice. Without the typing.', 'message': 'Invoice #2026-1042 · Example Supplier Ltd. · €840.00 net + €159.60 VAT · Total: €999.60 · Due: 30 October.', 'fields': ['Document: invoice #2026-1042', 'Total: €999.60', 'Due: 30 October'], 'result_title': 'Captured. Numbers checked.', 'result': 'Supplier, items and amounts extracted. Net amount and VAT reconciled. An accounting entry is prepared for approval.', 'receipt': 'DOCUMENT STRUCTURED · ACCOUNTING APPROVAL REQUIRED'},
            {'source': 'INBOX / 14:06', 'subject': 'The right message. The right team.', 'message': 'Hello, we are planning an internal project for 40 people. Could you send us a quote for onboarding and training?', 'fields': ['Intent: project enquiry', 'People: 40', 'Destination: your team'], 'result_title': 'Sorted. Team notified.', 'result': 'Project enquiry identified and assigned to the right team. Missing details highlighted. A question about date and scope is drafted.', 'receipt': 'REQUEST ASSIGNED · RESPONSE DRAFT READY'}
        ],
        'care_label': '02 / BEYOND THE INITIAL SETUP', 'care_title': ['It works.', 'And gets better.'],
        'care_text': 'Automation as a Service means I stay with your system after launch. As your business changes, your workflows evolve with it.',
        'care_items': [('Connect', 'Keep your tools. I connect your inbox, documents and team.'), ('Manage', 'Review responses, detect errors, monitor costs and step in when needed.'), ('Evolve', 'Add workflows, adapt rules and learn from real feedback.')],
        'care_note': 'YOUR TEAM HAS THE FINAL SAY.', 'care_orbit': ['TOOLS', 'AI', 'TEAM', 'CARE'],
        'roi_label': '03 / YOUR POTENTIAL', 'roi_title': ['Time is valuable.', 'Take it back.'],
        'roi_text': 'How much time could an automated process free up? Adjust the inputs to explore a possible outcome.',
        'roi_labels': ['Tasks per working day', 'Minutes per task', 'Internal hourly rate', 'Automatable share'],
        'roi_units': ['tasks', 'min.', '€', '%'], 'hours': 'hours / month', 'value': 'Estimated time value / month',
        'roi_note': 'Model based on 22 working days per month. Time value before service costs, not guaranteed savings. The actual share depends on the workflow.', 'roi_cta': 'Discuss my potential',
        'services_label': '04 / OTHER WAYS I HELP', 'services_title': ['One perspective.', 'Many possibilities.'],
        'services': [('01', 'AI & AUTOMATION', 'A system that works alongside you.', 'Custom AI workflows, ongoing care and TeamO as your digital colleague.', 'ki-automatisierung.html', 'Explore automation'), ('02', 'F&B CONSULTING', 'Better processes. Better numbers.', 'Hands-on expertise in purchasing, cost control, contracts and leadership.', 'fb-beratung.html', 'Explore F&B'), ('03', 'DIGITAL & WEB', 'A presence that makes a difference.', 'Websites, visibility and online marketing with one goal: more direct enquiries.', 'online-marketing.html', 'Explore digital')],
        'about_label': '05 / THE PERSON BEHIND THE SYSTEMS', 'about_title': ['I know the everyday.', 'And the code.'],
        'about_text': 'I’m Kastriot Tafolli. Over 15 years leading teams in five-star hospitality showed me where time gets lost. As a software engineer focused on AI, I build systems that solve those very problems.',
        'about_link': 'More about me', 'about_caption': 'KASTRIOT TAFOLLI / TB SOLUTIONS',
        'credentials': [('15+', 'years in five-star hospitality'), ('200+', 'employees led simultaneously'), ('50+', 'young professionals trained')], 'experience_label': 'CAREER STATIONS',
        'process_label': '06 / FROM IDEA TO EVERYDAY', 'process_title': ['Think big.', 'Start with something real.'],
        'process': [('Listen.', 'We discuss your business, your bottlenecks and the process that takes up your time.'), ('Build.', 'A focused first workflow. With your tools, your rules and tests with your team.'), ('Stay.', 'After launch, I monitor results and keep improving your system with you.')],
        'faq_label': '07 / GOOD QUESTIONS', 'faq_title': 'Anything else on your mind?',
        'cta_label': 'THE NEXT STEP IS A CONVERSATION.', 'cta_title': ['What if', 'it just', 'worked?'],
        'cta_text': 'Tell me about a process that takes up your time. Let’s find out what’s possible.',
        'cta_button': 'Let’s talk', 'cta_note': '30 MINUTES. NO OBLIGATION. HUMAN TO HUMAN.',
        'footer_tag': 'THINK HUMAN. ACT INTELLIGENT.', 'top': 'Back to top', 'detail_hero': ['INTELLIGENT', 'WORKFLOWS.', 'More freedom.'],
        'story_label': 'FROM SCATTERED TASKS TO CONNECTED WORK',
        'story_titles': ['Too many little tasks.', 'One connected system.', 'More time for people.'],
        'story_copies': ['Emails, invoices, phone calls. Each small task pulls your attention away from what matters.', 'Your information finds its way. AI structures it, rules check it, your team decides.', 'Less back and forth. More room for customers, ideas and work that moves you forward.'],
        'story_tasks': ['EMAIL', 'INVOICE', 'CALL', 'REPORT', 'ENQUIRY', 'DATA'], 'story_outcome': 'FREEDOM',
    },
    'sq': {
        'title': 'Kastriot Tafolli · Automatizim me AI për më shumë kohë',
        'description': 'AI Automation as a Service: procese të personalizuara me AI, integrim dhe mirëmbajtje nga Kastriot Tafolli. Për hotele, restorante dhe biznese.',
        'nav': ['Automatizimi', 'Shërbimet', 'Rreth meje', 'Kontakti'], 'talk': 'Të flasim', 'menu': 'Menu', 'motion': 'Lëvizja',
        'status': 'I HAPUR PËR PROJEKTE TË REJA', 'location': 'OSTSEEBAD BINZ',
        'hero': ['MË PAK', 'RUTINË.', 'Më shumë mundësi.'],
        'hero_text': 'Ndërtoj sisteme me AI që marrin përsipër punën. Që ekipi juaj të ketë kohë për atë që njerëzit bëjnë më mirë.',
        'hero_cta': 'Zbuloni automatizimin', 'hero_link': 'Të njihemi', 'art_label': 'IDE NJERËZORE. SISTEME INTELIGJENTE.',
        'scroll': 'LËVIZNI PËR TË ZBULUAR', 'intro': 'TEKNOLOGJI ME NDJESHMËRI PËR NJERËZIT',
        'manifesto': ['Anëtari juaj', 'i ardhshëm', 'është një sistem.'],
        'manifesto_text': 'Një kërkesë në 23:48. Një faturë që askush nuk dëshiron ta shkruajë. Një raport që duhet të jetë gati në mëngjes. Këtu fillon automatizimi i mirë.',
        'manifesto_small': 'Ju përcaktoni drejtimin. Unë lidh proceset, mjetet dhe AI-në për t’ju ndihmuar në punën e përditshme.',
        'service_label': 'OFERTA', 'service_title': ['AI Automation', 'as a Service.'],
        'service_text': 'Ndërtuar për biznesin tuaj. Integruar në sistemet ekzistuese. Mirëmbajtur vazhdimisht nga unë. Nga procesi i parë te mundësia e ardhshme.',
        'service_tags': ['Procese të personalizuara', 'Kontroll njerëzor', 'Mirëmbajtje e vazhdueshme'],
        'lab_label': '01 / PROVONI AUTOMATIZIMIN', 'lab_title': ['Pa mistere.', 'Gjithçka bëhet e qartë.'],
        'lab_text': 'Zgjidhni një proces dhe nisni demonstrimin. Shihni si një detyrë rutinë bëhet një proces inteligjent.',
        'demo_label': 'DEMONSTRIM INTERAKTIV · TË DHËNA FIKTIVE', 'scenarios': ['Kërkesë klienti', 'Faturë', 'Email'],
        'stages': ['Marrja', 'Kuptimi', 'Veprimi', 'Kontrolli', 'Rezultati'],
        'stage_notes': ['Mbërrin një kërkesë e re. Ekipi ende nuk ka nevojë të veprojë.', 'AI identifikon qëllimin, gjuhën dhe informacionin e rëndësishëm.', 'Procesi përgatit veprimin e duhur në sistemin tuaj.', 'Rregullat kontrollojnë rezultatin. Rastet e paqarta i kalojnë ekipit.', 'Kërkesa është e strukturuar, e dokumentuar dhe gati për miratim.'],
        'incoming': 'HYRJA', 'outgoing': 'REZULTATI', 'ready': 'Gati për provë', 'run': 'Nisni procesin', 'running': 'Procesi po punon', 'replay': 'Luajeni përsëri',
        'demo_hint': 'Një simulim shpjegues. Nuk dërgohen mesazhe dhe nuk bëhen rezervime.',
        'demos': [
            {'source': 'KËRKESË KLIENTI / 23:48', 'subject': 'Një bisedë javën tjetër?', 'message': 'Mirëmbrëma! A keni kohë më 16 ose 17 tetor për një bisedë të shkurtër? Bëhet fjalë për një faqe web dhe një proces që duam ta automatizojmë.', 'fields': ['Qëllimi: kërkesë takimi', 'Data: 16–17 tetor', 'Tema: faqe web dhe automatizim'], 'result_title': 'Përgjigje personale e përgatitur.', 'result': 'Kërkesa për takim dhe tema u identifikuan. Pikat e hapura i kalojnë ekipit tuaj për kontroll. Drafti i përgjigjes është gati.', 'receipt': 'KËRKESË E STRUKTURUAR · MIRATIM NGA EKIPI JUAJ'},
            {'source': 'KONTABILITET / 09:12', 'subject': 'Një faturë. Pa shkrim manual.', 'message': 'Fatura #2026-1042 · Furnitori Shembull · 840,00 € neto + 159,60 € TVSH · Gjithsej: 999,60 € · Afati: 30 tetor.', 'fields': ['Dokumenti: fatura #2026-1042', 'Gjithsej: 999,60 €', 'Afati: 30 tetor'], 'result_title': 'Regjistruar. Shifrat u kontrolluan.', 'result': 'Furnitori, artikujt dhe shumat u nxorën. Shuma neto dhe TVSH u krahasuan. Regjistrimi kontabël është gati për miratim.', 'receipt': 'DOKUMENT I STRUKTURUAR · MIRATIM NGA KONTABILITETI'},
            {'source': 'POSTA / 14:06', 'subject': 'Mesazhi i duhur. Ekipi i duhur.', 'message': 'Përshëndetje, planifikojmë një projekt të brendshëm me 40 persona. Mund të na dërgoni ofertë për prezantim dhe trajnim?', 'fields': ['Qëllimi: kërkesë projekti', 'Pjesëmarrës: 40 persona', 'Destinacioni: ekipi juaj'], 'result_title': 'Sistemuar. Ekipi u njoftua.', 'result': 'Kërkesa u identifikua dhe iu caktua ekipit të duhur. U shënuan të dhënat që mungojnë. U përgatit pyetja për datën dhe vëllimin.', 'receipt': 'KËRKESË E CAKTUAR · DRAFT PËRGJIGJEJE GATI'}
        ],
        'care_label': '02 / PËRTEJ INSTALIMIT FILLESTAR', 'care_title': ['Funksionon.', 'Dhe përmirësohet.'],
        'care_text': 'Automation as a Service do të thotë që e mbështes sistemin edhe pas nisjes. Ndërsa biznesi ndryshon, proceset zhvillohen me të.',
        'care_items': [('Lidhja', 'Mjetet tuaja mbeten. Lidh postën, dokumentet dhe ekipin.'), ('Mirëmbajtja', 'Kontrolloj përgjigjet, identifikoj gabimet, ndjek kostot dhe ndërhyj kur duhet.'), ('Zhvillimi', 'Shtoj procese, përshtat rregullat dhe mësoj nga reagimet reale.')],
        'care_note': 'EKIPI JUAJ KA FJALËN E FUNDIT.', 'care_orbit': ['MJETET', 'AI', 'EKIPI', 'KUJDESI'],
        'roi_label': '03 / POTENCIALI JUAJ', 'roi_title': ['Koha ka vlerë.', 'Rikthejeni.'],
        'roi_text': 'Sa kohë mund të lirojë një proces i automatizuar? Ndryshoni vlerat për të zbuluar një rezultat të mundshëm.',
        'roi_labels': ['Detyra për ditë pune', 'Minuta për detyrë', 'Kostoja e orës', 'Pjesa e automatizueshme'], 'roi_units': ['detyra', 'min.', '€', '%'],
        'hours': 'orë / muaj', 'value': 'Vlera e llogaritur e kohës / muaj',
        'roi_note': 'Model me 22 ditë pune në muaj. Vlera para kostove të shërbimit, jo kursim i garantuar. Pjesa reale varet nga procesi.', 'roi_cta': 'Të flasim për potencialin tim',
        'services_label': '04 / SHËRBIME TË TJERA', 'services_title': ['Një perspektivë.', 'Shumë mundësi.'],
        'services': [('01', 'AI & AUTOMATIZIM', 'Një sistem që punon me ju.', 'Procese me AI, mirëmbajtje dhe TeamO si koleg digjital.', 'ki-automatisierung.html', 'Zbuloni automatizimin'), ('02', 'KONSULENCË F&B', 'Procese më të mira. Shifra më të mira.', 'Përvojë në blerje, kontroll kostosh, kontrata dhe drejtim.', 'fb-beratung.html', 'Zbuloni F&B'), ('03', 'DIGJITAL & WEB', 'Një prezencë që sjell ndryshim.', 'Faqe web, dukshmëri dhe marketing me një synim: më shumë kërkesa direkte.', 'online-marketing.html', 'Zbuloni shërbimet digjitale')],
        'about_label': '05 / NJERIU PAS SISTEMEVE', 'about_title': ['Njoh përditshmërinë.', 'Dhe kodin.'],
        'about_text': 'Jam Kastriot Tafolli. Mbi 15 vjet drejtim në hoteleri me pesë yje më kanë treguar ku humbet koha. Si inxhinier softueri me fokus në AI, ndërtoj sisteme që zgjidhin këto probleme.', 'about_link': 'Më shumë rreth meje', 'about_caption': 'KASTRIOT TAFOLLI / TB SOLUTIONS',
        'credentials': [('15+', 'vjet hoteleri me pesë yje'), ('200+', 'punonjës të drejtuar njëkohësisht'), ('50+', 'profesionistë të rinj të trajnuar')], 'experience_label': 'ETAPAT PROFESIONALE',
        'process_label': '06 / NGA IDEJA NË PËRDITSHMËRI', 'process_title': ['Mendoni gjerë.', 'Filloni konkretisht.'],
        'process': [('Dëgjoj.', 'Flasim për biznesin, pengesat dhe procesin që ju merr kohë.'), ('Ndërtoj.', 'Një proces fillestar i kufizuar qartë. Me mjetet, rregullat dhe testet me ekipin tuaj.'), ('Mbështes.', 'Pas nisjes monitoroj rezultatet dhe zhvilloj sistemin bashkë me ju.')],
        'faq_label': '07 / PYETJE TË MIRA', 'faq_title': 'Diçka ende e paqartë?',
        'cta_label': 'HAPI TJETËR ËSHTË NJË BISEDE.', 'cta_title': ['Po sikur', 'thjesht të', 'funksiononte?'],
        'cta_text': 'Më tregoni një proces që ju merr kohë. Të zbulojmë çfarë është e mundur.', 'cta_button': 'Të flasim', 'cta_note': '30 MINUTA. PA DETYRIM. NJERI ME NJERI.',
        'footer_tag': 'MENDONI SI NJERI. VEPRONI ME INTELIGJENCË.', 'top': 'Kthehu lart', 'detail_hero': ['PROCESE', 'INTELIGJENTE.', 'Më shumë liri.'],
        'story_label': 'NGA DETYRAT E SHPËRNDARA TE PUNA E LIDHUR',
        'story_titles': ['Shumë detyra të vogla.', 'Një sistem i lidhur.', 'Më shumë kohë për njerëzit.'],
        'story_copies': ['Email, fatura, telefonata. Çdo detyrë e vogël largon vëmendjen nga ajo që ka rëndësi.', 'Informacioni gjen rrugën e vet. AI e strukturon, rregullat e kontrollojnë, ekipi vendos.', 'Më pak vajtje-ardhje. Më shumë hapësirë për klientë, ide dhe punë që ju çon përpara.'],
        'story_tasks': ['EMAIL', 'FATURË', 'TELEFON', 'RAPORT', 'KËRKESË', 'TË DHËNA'], 'story_outcome': 'LIRI',
    },
}

# The homepage introduces the independent offers. Automation keeps its own page.
OFFERS={
 'de':[
  ('01','KI-AUTOMATISIERUNG','KI Automatisierung für kleine Unternehmen.','Die erste Automatisierung zum Festpreis: E-Mail, Angebote oder Termine. Nichts geht ohne Ihre Freigabe hinaus.','ki-automatisierung-kleine-unternehmen.html','Angebot ansehen'),
  ('02','WEBSITE & LANDINGPAGE','Landingpage erstellen lassen.','Website oder Landingpage zum Festpreis, inklusive Pflege und einem technischen Check.','landingpage-erstellen-lassen.html','Angebot ansehen'),
  ('03','TEXTE & ÜBERSETZUNGEN','Deutsch, Englisch, Albanisch.','Texte und Übersetzungen in diesen drei Sprachen. Die Festpreise stehen auf der Angebotsseite.','angebot/','Preise ansehen')],
 'en':[
  ('01','AI AUTOMATION','AI automation for small businesses.','A first automation at a fixed price: email, quotes or appointments. Nothing goes out without your approval.','ki-automatisierung-kleine-unternehmen.html','View the offer'),
  ('02','WEBSITE & LANDING PAGE','A landing page, built for you.','A website or landing page at a fixed price, including care and a technical check.','landingpage-erstellen-lassen.html','View the offer'),
  ('03','TEXTS & TRANSLATION','German, English, Albanian.','Texts and translations in these three languages. The fixed prices are on the offer page.','angebot/','View the prices')],
 'sq':[
  ('01','AUTOMATIZIM ME IA','Automatizim me IA për biznese të vogla.','Automatizimi i parë me çmim fiks: email, oferta ose takime. Asgjë nuk del pa miratimin tuaj.','ki-automatisierung-kleine-unternehmen.html','Shikoni ofertën'),
  ('02','FAQE WEB & LANDINGPAGE','Një faqe që të çon te kontakti.','Faqe web ose landingpage me çmim fiks, me mirëmbajtje dhe një kontroll teknik.','landingpage-erstellen-lassen.html','Shikoni ofertën'),
  ('03','TEKSTE & PËRKTHIME','Gjermanisht, anglisht, shqip.','Tekste dhe përkthime në këto tri gjuhë. Çmimet fikse janë në faqen e ofertës.','angebot/','Shikoni çmimet')]}
POSITIONING={
'de':dict(title='KI, Websites und Texte für kleine Unternehmen | Kastriot Tafolli',description='Drei Angebote von Kastriot Tafolli: KI Automatisierung für kleine Unternehmen, Landingpage erstellen lassen und Texte auf Deutsch, Englisch und Albanisch. Festpreis nach Umfang.',hero=['KI, WEBSITES','UND TEXTE.','Für kleine Unternehmen.'],hero_text='Drei Angebote: die erste KI-Automatisierung, eine Website oder Landingpage, und Texte auf Deutsch, Englisch und Albanisch.',hero_cta='Anfrage senden',offers_link='Angebote ansehen',manifesto=['Ein Ablauf.','Eine Seite.','Ein Text.'],manifesto_text='Ein Ablauf kann Arbeit vorbereiten. Eine Seite kann den Weg zur Anfrage kurz machen. Ein Text kann auf Deutsch, Englisch oder Albanisch ankommen.',manifesto_small='Die erste Automatisierung, eine Website oder Landingpage und Übersetzungen. Den Festpreis nenne ich nach dem Umfang.',services_label='DIE ANGEBOTE',services_title=['Drei Angebote.','Klar getrennt.'],portfolio_link='Weitere Leistungen ansehen',about_title=['Code, Web und Texte.','Aus einer Hand.'],about_text='Ich bin Kastriot Tafolli, Inhaber von TB Solutions in Ostseebad Binz. Ich richte eine erste Automatisierung ein, baue Websites und Landingpages und prüfe Texte auf Deutsch, Englisch und Albanisch selbst.',cta_text='KI-Automatisierung, eine Landingpage oder eine Übersetzung: Schreiben Sie mir, worum es geht.',ask='Anfragen',credentials=[('TB Solutions','Sitz in Ostseebad Binz'),('DE · EN · SQ','Texte und Übersetzungen'),('KI & Code','Automatisierung und Websites')]),
'en':dict(title='AI, websites and texts for small businesses | Kastriot Tafolli',description='Three offers from Kastriot Tafolli: a first AI automation, a website or landing page, and texts in German, English and Albanian. The fixed price follows the scope.',hero=['AI, WEBSITES','AND TEXTS.','For small businesses.'],hero_text='Three offers: a first AI automation, a website or landing page, and texts in German, English and Albanian.',hero_cta='Send a request',offers_link='View the offers',manifesto=['One workflow.','One page.','One text.'],manifesto_text='A workflow can prepare the work. A page can make the enquiry short. A text can arrive in German, English or Albanian.',manifesto_small='The first automation, a website or landing page, and translations. I name the fixed price after the scope is clear.',services_label='THE OFFERS',services_title=['Three offers.','Clearly separated.'],portfolio_link='See further services',about_title=['Code, web and texts.','From one person.'],about_text='I’m Kastriot Tafolli, owner of TB Solutions in Ostseebad Binz. I set up a first automation, build websites and landing pages, and review texts in German, English and Albanian myself.',cta_text='AI automation, a landing page or a translation: tell me what you need.',ask='Get in touch',credentials=[('TB Solutions','Based in Ostseebad Binz'),('DE · EN · SQ','Texts and translations'),('AI & code','Automation and websites')]),
'sq':dict(title='IA, faqe web dhe tekste për biznese të vogla | Kastriot Tafolli',description='Tri oferta nga Kastriot Tafolli: automatizimi i parë me IA, një faqe web ose landingpage, dhe tekste në gjermanisht, anglisht dhe shqip. Çmimi fiks pas qartësimit të vëllimit.',hero=['IA, FAQE WEB','DHE TEKSTE.','Për biznese të vogla.'],hero_text='Tri oferta: automatizimi i parë me IA, një faqe web ose landingpage, dhe tekste në gjermanisht, anglisht dhe shqip.',hero_cta='Dërgoni një kërkesë',offers_link='Shikoni ofertat',manifesto=['Një proces.','Një faqe.','Një tekst.'],manifesto_text='Një proces mund të përgatisë punën. Një faqe e bën kontaktin të shkurtër. Një tekst mund të vijë në gjermanisht, anglisht ose shqip.',manifesto_small='Automatizimi i parë, një faqe web ose landingpage dhe përkthime. Çmimin fiks e them pasi të qartësohet vëllimi.',services_label='OFERTAT',services_title=['Tri oferta.','Të ndara qartë.'],portfolio_link='Shikoni shërbimet e tjera',about_title=['Kod, web dhe tekste.','Nga një dorë.'],about_text='Jam Kastriot Tafolli, pronar i TB Solutions në Ostseebad Binz. Vendos automatizimin e parë, ndërtoj faqe web dhe landingpage dhe i kontrolloj vetë tekstet në gjermanisht, anglisht dhe shqip.',cta_text='Automatizim me IA, landingpage apo përkthim: më shkruani për çfarë keni nevojë.',ask='Na shkruani',credentials=[('TB Solutions','Selia në Ostseebad Binz'),('DE · EN · SQ','Tekste dhe përkthime'),('IA & kod','Automatizim dhe faqe web')])}
for language,values in POSITIONING.items():
    COPY[language]['automation_description']=COPY[language]['description']
    COPY[language]['automation_hero_text']=COPY[language]['hero_text']
    COPY[language]['automation_cta']=COPY[language]['hero_cta']
    COPY[language].update(values)
    COPY[language]['services']=OFFERS[language]

AUTOMATION={
 'de':dict(description='KI-Automatisierung als Service: Workflows, Systemanbindung und laufende Betreuung von Kastriot Tafolli. Für Unternehmen in Deutschland, Österreich, der Schweiz und Kosovo.',hero_text='Ich baue KI-Systeme, die Arbeit übernehmen. Damit Ihr Team wieder Zeit für das hat, was Menschen am besten können.',hero_cta='Automation entdecken'),
 'en':dict(description='AI automation as a service: workflows, system integration and ongoing care by Kastriot Tafolli. For businesses in Germany, Austria, Switzerland and Kosovo.',hero_text='I build AI systems that take work off your hands. So your team can get back to what people do best.',hero_cta='Explore automation'),
 'sq':dict(description='Automatizim me IA si shërbim: procese, integrim sistemesh dhe mirëmbajtje nga Kastriot Tafolli. Për biznese në Gjermani, Austri, Zvicër dhe Kosovë.',hero_text='Ndërtoj sisteme me IA që marrin përsipër punën. Që ekipi juaj të ketë kohë për atë që njerëzit bëjnë më mirë.',hero_cta='Zbuloni automatizimin')}
for code,values in AUTOMATION.items():
    COPY[code]['automation_description']=values['description']
    COPY[code]['automation_hero_text']=values['hero_text']
    COPY[code]['automation_cta']=values['hero_cta']

# Service geography confirmed by the owner; the content stays language-specific.
for code, values in {
 'de': dict(location='DEUTSCHLAND · ÖSTERREICH · SCHWEIZ · KOSOVO'),
 'en': dict(location='GERMANY · AUSTRIA · SWITZERLAND · KOSOVO'),
 'sq': dict(location='GJERMANI · AUSTRI · ZVICËR · KOSOVË')
}.items():
 COPY[code].update(values)
