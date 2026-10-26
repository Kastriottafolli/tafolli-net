"""Editorial direction for each detail page. Illustrations never imply client results."""
PAGES={}

def add(path,kind,label,lines,intro,topics,flow,*,cta='Projekt besprechen',lang='de'):
    PAGES[path]=dict(path=path,kind=kind,label=label,lines=lines,intro=intro,topics=topics,flow=flow,cta=cta,lang=lang)

add('leistungen.html','hub','UNSERE LEISTUNGEN',('Gute Ideen.','Gemeinsam umgesetzt.'),
    'Marketing, Software, Beratung und KI: Entdecken Sie, was Ihr Unternehmen jetzt weiterbringt – und wie die einzelnen Leistungen zusammenwirken.',
    [('Marketing','Ein stimmiger Auftritt von der Website bis zur Kampagne.'),('Technology','Anwendungen und Systeme für Ihre konkreten Aufgaben.'),('Consulting','Betriebliche Erfahrung wird zu umsetzbaren Entscheidungen.'),('AI Automation','Wiederkehrende Aufgaben mit passenden Freigaben vereinfachen.')],['Aufgabe','Konzept','Umsetzung','Einführung'])
add('online-marketing.html','brand','MARKETING · MARKE · KOMMUNIKATION',('Ihre Marke.','Mit einer klaren Richtung.'),
    'Strategie, Corporate Design, Websites, Kampagnen und Content. Wir verbinden die einzelnen Kontaktpunkte zu einem Auftritt, an dem man Ihr Unternehmen wiedererkennt.',
    [('Identität','Farben, Typografie und Gestaltung erzählen dieselbe Geschichte.'),('Kampagne','Botschaft, Werbemittel und Landingpage greifen ineinander.'),('Kontakt','Aus Aufmerksamkeit wird ein nachvollziehbarer nächster Schritt.')],['Positionierung','Gestaltung','Kanäle','Anfragen'],cta='Marketingprojekt planen')
add('webdesign.html','browser','WEBSITE-ERSTELLUNG & WEBDESIGN',('Websites mit Charakter.','Und einem klaren Ziel.'),
    'Wir gestalten und entwickeln Ihren digitalen Auftritt: mit passenden Inhalten, einer starken mobilen Ansicht und einem einfachen Weg zur Anfrage. Von der Landingpage bis zur integrierten Web-App.',
    [('Desktop','Großzügige Gestaltung und klare Orientierung auf großen Bildschirmen.'),('Mobil','Inhalte und Kontaktwege funktionieren auch auf kleinen Geräten.'),('Anfrage','Angebot, Nutzen und nächster Schritt gehören zusammen.')],['Inhalte','Design','Entwicklung','Livegang'],cta='Websiteprojekt besprechen')
add('suchmaschinenoptimierung.html','search','SEO & LOKALE SICHTBARKEIT',('Gefunden werden.','Mit den richtigen Antworten.'),
    'Technik, Inhalte und lokale Unternehmensdaten bilden die Grundlage Ihrer Sichtbarkeit. Wir verbessern die Stellen, an denen Ihre Kunden nach Ihrem Angebot suchen.',
    [('Suchfragen','Jede wichtige Leistung bekommt einen verständlichen Einstieg.'),('Inhalte','Hilfreiche Seiten beantworten den konkreten Bedarf Ihrer Kunden.'),('Lokal','Website und Unternehmensprofile verwenden stimmige Angaben.')],['Prüfen','Priorisieren','Verbessern','Auswerten'],cta='SEO-Vorhaben besprechen')
add('social-media.html','social','SOCIAL MEDIA & CONTENT',('Eine Marke.','Viele gute Kontaktpunkte.'),
    'Strategie, Redaktionsplan, Posts und Reels für die passenden Kanäle. Wir entwickeln Inhalte, die Ihre Marke zeigen und einen sinnvollen Weg zum Gespräch eröffnen.',
    [('Beiträge','Ein wiedererkennbares Gestaltungssystem für Ihre Themen.'),('Reels','Bewegte Inhalte mit einer klaren Botschaft und passenden Formaten.'),('Planung','Themen, Freigaben und Veröffentlichung sind aufeinander abgestimmt.')],['Themen','Produktion','Freigabe','Veröffentlichung'],cta='Social Media planen')
add('foto-video.html','photo','FOTO · VIDEO · VISUELLE INHALTE',('Zeigen, was Sie','besonders macht.'),
    'Menschen, Produkte und Räume für Website, Social Media und Kampagnen. Wir planen die Motive und Formate entlang Ihrer Marke und des vorgesehenen Einsatzes.',
    [('Bildsprache','Licht, Perspektive und Motivwahl geben Ihrem Auftritt Charakter.'),('Bewegung','Kurze Filme und Sequenzen erklären Ihr Angebot im passenden Rhythmus.'),('Formate','Ein Bildkonzept wird für die vereinbarten Kanäle aufbereitet.')],['Konzept','Aufnahme','Bearbeitung','Ausgabe'],cta='Inhalte produzieren lassen')
add('softwareentwicklung.html','software','INDIVIDUELLE SOFTWAREENTWICKLUNG',('Software, die','für Sie arbeitet.'),
    'Fachanwendungen, Portale und Schnittstellen nach Ihren Anforderungen. Wir verbinden Bedienung, Geschäftsabläufe und technische Umsetzung zu einer passenden Anwendung.',
    [('Oberfläche','Menschen sehen die Aufgaben und Informationen, die sie brauchen.'),('Abläufe','Regeln und Freigaben werden Teil der Anwendung.'),('Integration','Vorhandene Systeme werden über passende Schnittstellen verbunden.')],['Anforderung','Prototyp','Entwicklung','Übergabe'],cta='Softwareprojekt besprechen')
add('app-entwicklung.html','app','APPS FÜR IOS · ANDROID · WEB',('Ihre Idee.','Auf dem richtigen Gerät.'),
    'Mobile Apps und Webanwendungen für Ihre Nutzer. Wir planen Funktionen, Bedienung und Anbindungen passend zur Aufgabe – vom ersten Nutzungsschritt bis zur Veröffentlichung.',
    [('iOS','Bedienkonzepte und Funktionen für die vorgesehenen Apple-Geräte.'),('Android','Die Anwendung wird für die vereinbarten Android-Geräte geprüft.'),('Web','Eine browserbasierte Lösung kann unabhängig vom App-Store erreichbar sein.')],['Nutzer','Oberflächen','Funktionen','Veröffentlichung'],cta='App-Idee besprechen')
add('cybersecurity.html','security','CYBERSECURITY & IT-SICHERHEIT',('Sicherheit.','Im Zusammenspiel.'),
    'Zugänge, Anwendungen und Unternehmensdaten gemeinsam betrachten. Wir priorisieren konkrete Schutzmaßnahmen und klären die Verantwortung für einen verlässlicheren Betrieb.',
    [('Identität','Konten, Rollen und Mehrfaktor-Anmeldung schaffen klare Zugriffe.'),('Anwendungen','Sicherheit gehört zu Konfiguration, Entwicklung und Pflege.'),('Wiederanlauf','Sicherungen werden mit einem nachvollziehbaren Wiederherstellungsweg verbunden.')],['Bestand','Risiken','Maßnahmen','Betrieb'],cta='Sicherheitsbedarf klären')
add('domain-hosting-email.html','cloud','DOMAIN · HOSTING · E-MAIL',('Eine gute Adresse.','Eine verlässliche Basis.'),
    'Domain, Website und geschäftliche E-Mail gehören zusammen. Wir richten die vereinbarte Grundlage ein und sorgen für verständliche Zuständigkeiten und eine geordnete Übergabe.',
    [('Domain','Ihre Unternehmensadresse wird mit den richtigen Diensten verbunden.'),('Hosting','Die technische Umgebung richtet sich nach Ihrer Website und Anwendung.'),('E-Mail','Geschäftliche Kommunikation erhält eine eigene, passende Adresse.')],['Adresse','Einrichtung','Verbindung','Übergabe'],cta='Technische Grundlage planen')
add('digitalisierung.html','integration','DIGITALISIERUNG & SYSTEMINTEGRATION',('Weniger Umwege.','Mehr Zusammenhang.'),
    'Wir verbinden vorhandene Systeme und Arbeitsabläufe dort, wo heute doppelte Eingaben und manuelle Übergaben entstehen. Mit einem sinnvollen Einstieg und klaren Zuständigkeiten.',
    [('Daten','Informationen werden an den benötigten Stellen verfügbar.'),('Systeme','Schnittstellen verbinden geeignete Anwendungen miteinander.'),('Menschen','Neue Abläufe werden mit den Menschen eingeführt, die damit arbeiten.')],['Aufnehmen','Verbinden','Erproben','Einführen'],cta='Digitalisierung besprechen')
add('ki-automatisierung.html','automation','KI-AUTOMATISIERUNG & WORKFLOWS',('Wiederkehrende Arbeit.','Intelligent vorbereitet.'),
    'Anfragen strukturieren, Dokumente verarbeiten und nächste Schritte vorbereiten. Wir entwickeln passende Abläufe mit ausgewählten Datenquellen, klaren Regeln und menschlichen Freigaben.',
    [('Eingang','E-Mails, Dokumente und Formulare bilden den vereinbarten Ausgangspunkt.'),('Verarbeitung','Informationen werden geordnet und Entwürfe vorbereitet.'),('Freigabe','Verantwortliche Personen behalten die Kontrolle über wichtige Entscheidungen.')],['Eingang','Einordnung','Entwurf','Freigabe'],cta='KI-Ablauf besprechen')
add('ki-entwicklung.html','knowledge','KI-ENTWICKLUNG & ASSISTENTEN',('Ihr Wissen.','Im richtigen Moment.'),
    'Ein KI-Assistent wird nützlich, wenn Aufgabe, Quellen und Grenzen klar sind. Wir entwickeln Anwendungen mit geeigneten Wissensbeständen und überprüfbaren Antworten.',
    [('Quellen','Freigegebene Dokumente liefern den fachlichen Zusammenhang.'),('Antwort','Die Anwendung bereitet die benötigten Informationen verständlich auf.'),('Prüfung','Fehlende Angaben und schwierige Fälle gehören zur Erprobung.')],['Aufgabe','Quellen','Assistent','Prüfung'],cta='KI-Anwendung planen')
add('teamo-ki.html','product','TEAMO · KI FÜR HOSPITALITY',('Ein Assistent.','Mit Blick auf den Betrieb.'),
    'TeamO verbindet die Idee eines KI-Assistenten mit konkreten Aufgaben aus Hotellerie und Gastronomie. Wir besprechen, welche Informationen und Abläufe zu Ihrem Betrieb passen.',
    [('Service','Wiederkehrende Fragen lassen sich mit geeigneten Quellen vorbereiten.'),('Organisation','Informationen und Zuständigkeiten bleiben im Zusammenhang.'),('Freigaben','Der Betrieb legt fest, welche Schritte menschliche Bestätigung benötigen.')],['Betrieb','Wissen','Assistenz','Kontrolle'],cta='TeamO kennenlernen')
add('fb-beratung.html','strategy','UNTERNEHMENS- & F&B-BERATUNG',('Vom Überblick','in die Umsetzung.'),
    'Abläufe, Teams und Wirtschaftlichkeit gemeinsam betrachten. Wir verbinden betriebliche Erfahrung mit einer klaren Priorisierung und begleiten die vereinbarten nächsten Schritte.',
    [('Organisation','Aufgaben, Übergaben und Verantwortlichkeiten werden greifbar.'),('Wirtschaftlichkeit','Zahlen unterstützen die Entscheidung über konkrete Maßnahmen.'),('Umsetzung','Ein guter Plan braucht Zuständigkeiten und einen Weg in den Alltag.')],['Verstehen','Entscheiden','Umsetzen','Begleiten'],cta='Beratungsbedarf besprechen')
add('lieferantenvereinbarungen.html','procurement','LIEFERANTEN & EINKAUF',('Gute Konditionen.','Klar vereinbart.'),
    'Sortiment, Lieferfähigkeit, Preise und Verpflichtungen gehören an einen Tisch. Wir strukturieren Angebote und bereiten die Grundlage für nachvollziehbare Lieferantenentscheidungen.',
    [('Angebote','Leistungen und Konditionen werden vergleichbar aufbereitet.'),('Gespräch','Ziele und offene Punkte werden vor der Verhandlung geordnet.'),('Vereinbarung','Die besprochenen Grundlagen und Zuständigkeiten werden dokumentiert.')],['Bedarf','Vergleich','Verhandlung','Vereinbarung'])
add('getraenkevertraege.html','contracts','GETRÄNKEVERTRÄGE',('Das ganze Angebot.','Im Blick.'),
    'Ein Getränkekonzept besteht aus mehr als einem Listenpreis. Wir betrachten Bindung, Ausstattung, Lieferung und wirtschaftliche Verpflichtungen im Zusammenhang.',
    [('Konditionen','Preise und Bezugsgrößen werden auf eine gemeinsame Basis gebracht.'),('Bindung','Laufzeiten und Verpflichtungen fließen in die betriebliche Entscheidung ein.'),('Ausstattung','Leihgaben und Unterstützung gehören zum Gesamtbild des Angebots.')],['Unterlagen','Vergleich','Abstimmung','Entscheidung'])
add('rueckverguetungen.html','rebate','RÜCKVERGÜTUNGEN & BONI',('Wissen, was','zurückkommen kann.'),
    'Bezugsgrößen, Nachweise und Abrechnung nachvollziehbar machen. Wir ordnen die vereinbarten Konditionen und schaffen eine verständliche Grundlage für deren Prüfung.',
    [('Grundlage','Die vereinbarten Mengen, Zeiträume und Bedingungen werden erfasst.'),('Nachweis','Verfügbare Belege werden den passenden Vereinbarungen zugeordnet.'),('Abrechnung','Ansatz und tatsächliche Abrechnung lassen sich gegenüberstellen.')],['Vereinbarung','Belege','Abgleich','Klärung'])
add('wareneinsatz-kalkulation.html','costs','WARENEINSATZ & KALKULATION',('Jede Zutat.','Eine klare Rechnung.'),
    'Rezepturen, Einkauf und Verkaufspreise zusammenbringen. Wir strukturieren die Kalkulation so, dass betriebliche Entscheidungen auf einer nachvollziehbaren Grundlage stehen.',
    [('Rezeptur','Mengen und Bezugseinheiten bilden die Grundlage der Rechnung.'),('Einkauf','Die passenden Einstandspreise werden den Zutaten zugeordnet.'),('Kalkulation','Wareneinsatz und weitere Annahmen bleiben nachvollziehbar.')],['Rezeptur','Einstand','Kalkulation','Entscheidung'])
add('inventur-warenwirtschaft.html','inventory','INVENTUR & WARENWIRTSCHAFT',('Bestände kennen.','Abläufe verbinden.'),
    'Von der Bestellung bis zur Inventur: Wir betrachten Warenbewegungen, Erfassung und Verantwortlichkeiten und verbinden sie mit den vorhandenen betrieblichen Systemen.',
    [('Bestellen','Bedarf und Zuständigkeiten werden in einem klaren Ablauf verbunden.'),('Erfassen','Wareneingang und Bewegungen brauchen verständliche Erfassungsregeln.'),('Abgleichen','Inventur und Systembestand werden auf derselben Grundlage betrachtet.')],['Bestellung','Eingang','Bestand','Inventur'])
add('interim-fb-management.html','leadership','INTERIM F&B-MANAGEMENT',('Verantwortung.','Auf Zeit übernommen.'),
    'Operative Führung und konkrete Unterstützung in einer Übergangsphase. Ziele, Umfang und Zuständigkeiten werden vor dem Einsatz mit Ihrem Betrieb abgestimmt.',
    [('Orientierung','Die aktuelle Lage und die dringendsten Aufgaben werden geklärt.'),('Führung','Teams erhalten einen abgestimmten Rahmen für den Alltag.'),('Übergabe','Erkenntnisse, Maßnahmen und offene Punkte werden geordnet übergeben.')],['Auftrag','Einsatz','Stabilisierung','Übergabe'])
add('revenue-controlling.html','analytics','REVENUE & F&B-CONTROLLING',('Zahlen verstehen.','Gezielter entscheiden.'),
    'Budget, Forecast und betriebliche Kennzahlen in einen brauchbaren Zusammenhang bringen. Wir machen Annahmen und Entwicklungen für die vereinbarten Entscheidungen sichtbar.',
    [('Budget','Ziele und Annahmen werden nachvollziehbar aufbereitet.'),('Entwicklung','Verfügbare Ist-Werte zeigen Veränderungen im Zeitverlauf.'),('Entscheidung','Abweichungen werden mit konkreten Handlungsoptionen verbunden.')],['Daten','Analyse','Forecast','Maßnahmen'])
add('personal-recruiting.html','people','RECRUITING & TEAMENTWICKLUNG',('Die passende Rolle.','Ein guter Einstieg.'),
    'Anforderungen, Auswahl und Einarbeitung aufeinander abstimmen. Wir begleiten die vereinbarten Schritte im Recruiting und in der Entwicklung Ihrer betrieblichen Teams.',
    [('Rolle','Aufgabe und benötigte Kompetenzen werden konkret beschrieben.'),('Auswahl','Gespräche und Entscheidungen erhalten eine nachvollziehbare Grundlage.'),('Einarbeitung','Ein klarer Einstieg verbindet neue Menschen mit dem Betrieb.')],['Rolle','Ansprache','Auswahl','Einstieg'])
add('ki-automatisierung-kleine-unternehmen.html','automation','KI FÜR KLEINE UNTERNEHMEN',('Klein anfangen.','Einen Ablauf verbessern.'),
    'Die erste Automatisierung beginnt mit einer konkreten Aufgabe: etwa einer E-Mail, einem Angebot oder einem Termin. Wir grenzen den Umfang ab und behalten die Freigabe bei Ihnen.',
    [('E-Mail','Eine wiederkehrende Anfrage wird zu einem vorbereiteten Entwurf.'),('Angebot','Benötigte Angaben werden vor der Bearbeitung zusammengeführt.'),('Termin','Der nächste organisatorische Schritt wird nachvollziehbar vorbereitet.')],['Aufgabe','Anbindung','Erprobung','Freigabe'])
add('landingpage-erstellen-lassen.html','landing','LANDINGPAGE ERSTELLEN LASSEN',('Ein Angebot.','Ein überzeugender Auftritt.'),
    'Eine Landingpage bringt Ihr Angebot auf den Punkt: mit klarer Botschaft, passender Gestaltung und einem direkten Anfrageweg. Richtpreis ca. 990 €; den konkreten Umfang stimmen wir mit Ihnen ab.',
    [('Botschaft','Besucher verstehen, für wen Ihr Angebot gedacht ist.'),('Gestaltung','Die Seite verbindet Ihre Marke mit einer klaren Blickführung.'),('Anfrage','Der nächste Schritt bleibt vom Einstieg bis zum Abschluss erreichbar.')],['Angebot','Inhalte','Gestaltung','Kontakt'],cta='Landingpage planen')
add('website-pflege.html','maintenance','WEBSITE-PFLEGE',('Ihr Auftritt.','Gut weiterbetreut.'),
    'Updates, Backups und vereinbarte Änderungen im Monatsabo. Sie wählen den passenden Umfang; wir halten fest, was erledigt wurde und welche Aufgaben offen sind.',
    [('Aktualisieren','Vereinbarte technische und redaktionelle Änderungen werden umgesetzt.'),('Prüfen','Website und Sicherungen werden im gewählten Umfang betrachtet.'),('Überblick','Eine verständliche Rückmeldung zeigt den Stand der Betreuung.')],['Aufgabe','Änderung','Prüfung','Rückmeldung'],cta='Website-Pflege besprechen')
add('onlineshop.html','commerce','ONLINESHOP & E-COMMERCE',('Ihr Sortiment.','Ein guter Weg zum Kauf.'),
    'Produktführung, Gestaltung und Checkout für Ihr Sortiment. Ein Onlineshop liegt bei ca. 6.500 €, größere Shops beginnen bei 15.000 €. Funktionen und Anbindungen bestimmen das konkrete Angebot.',
    [('Produkte','Sortiment und Produktinformationen bekommen eine klare Struktur.'),('Checkout','Warenkorb und die vereinbarten Zahlungswege greifen ineinander.'),('Anbindung','Produktdaten und weitere Systeme werden nach Bedarf verbunden.')],['Sortiment','Shop','Checkout','Übergabe'],cta='Shop-Projekt besprechen')
add('web-apps.html','webapp','WEB-APPS & WERKZEUGE',('Eine Aufgabe.','Ihr eigenes Werkzeug.'),
    'Vom kleinen Browser-Rechner bis zur individuellen Anwendung: Wir entwickeln Funktionen, die einen klaren Ablauf unterstützen. Umfang, Daten und Anbindung werden vorab vereinbart.',
    [('Eingabe','Menschen erfassen genau die Informationen, die der Ablauf benötigt.'),('Verarbeitung','Regeln und Funktionen werden passend zur Aufgabe entwickelt.'),('Ergebnis','Eine verständliche Ausgabe hilft beim nächsten Arbeitsschritt.')],['Aufgabe','Oberfläche','Funktion','Übergabe'],cta='Web-App besprechen')
add('firmenprofile.html','local','LOKALE EINTRÄGE & UNTERNEHMENSPROFILE',('Ihr Unternehmen.','Am richtigen Ort präsent.'),
    'Google-Unternehmensprofil, Apple Maps, Bing Places und passende Verzeichnisse. Wir vereinheitlichen Ihre Angaben und betreuen die vereinbarten Profile – mit echten Unternehmensdaten.',
    [('Standort','Adresse, Einzugsgebiet und Kategorien werden passend aufbereitet.'),('Profil','Kontaktdaten, Öffnungszeiten und Website bleiben stimmig.'),('Pflege','Veränderte Angaben werden im vereinbarten Umfang aktualisiert.')],['Bestand','Daten','Verifizierung','Pflege'],cta='Lokale Einträge besprechen')
add('angebot/','translation','TEXTE & ÜBERSETZUNGEN',('Drei Sprachen.','Eine klare Botschaft.'),
    'Texte und Übersetzungen auf Deutsch, Englisch und Albanisch. Für Dokumente, Websites und die vereinbarten Inhalte – mit persönlicher Prüfung und einem klaren Paketumfang.',
    [('Deutsch','Verständliche Formulierungen für Ihre deutschsprachigen Leser.'),('English','Der Zusammenhang Ihrer Botschaft bleibt auch im Englischen erkennbar.'),('Shqip','Përmbajtje të qarta për lexuesit që flasin shqip.')],['Vorlage','Bearbeitung','Prüfung','Übergabe'],cta='Textprojekt besprechen')
add('website-fuer-handwerker.html','craft','WEBSITES FÜR HANDWERKSBETRIEBE',('Gute Arbeit.','Ein starker erster Eindruck.'),
    'Zeigen Sie, was Ihr Betrieb kann, wo Sie arbeiten und wie Kunden Sie erreichen. Wir gestalten eine Website mit klaren Leistungen, passender Bildsprache und einem einfachen Anfrageweg.',
    [('Leistungen','Kunden finden die Arbeiten, die Ihr Betrieb tatsächlich anbietet.'),('Einsatzgebiet','Ihr regionaler Bezug wird auf der Website verständlich dargestellt.'),('Anfrage','Besucher können ihren Bedarf direkt und unkompliziert schildern.')],['Betrieb','Inhalte','Website','Anfrage'])
add('ki-automatisierung-arztpraxen.html','health','KI FÜR ARZTPRAXEN & THERAPEUTEN',('Organisation entlasten.','Verantwortung behalten.'),
    'Administrative Abläufe rund um allgemeine Anfragen und Terminorganisation betrachten. Der Einstieg erfolgt mit einem klar abgegrenzten Auftrag, ohne Patientendaten und mit Ihrer Freigabe.',
    [('Anfragen','Allgemeine organisatorische Fragen werden passend eingeordnet.'),('Vorbereitung','Ein abgestimmter Ablauf bereitet den nächsten Schritt vor.'),('Freigabe','Verantwortliche Personen prüfen, was nach außen geht.')],['Organisation','Regeln','Entwurf','Freigabe'])
add('website-fuer-vereine.html','calendar','WEBSITES FÜR VEREINE',('Ihr Verein.','Ein gemeinsamer Treffpunkt.'),
    'Termine, Angebote und Kontakt an einem verständlichen Ort. Wir gestalten Vereinswebsites, die auf dem Smartphone ebenso gut Orientierung geben wie am großen Bildschirm.',
    [('Aktuelles','Wichtige Nachrichten und Termine bekommen einen klaren Platz.'),('Mitmachen','Interessierte erfahren, wie sie Teil Ihres Vereins werden können.'),('Kontakt','Die richtigen Ansprechpersonen und Kontaktwege sind leicht zu finden.')],['Verein','Struktur','Inhalte','Übergabe'])
add('website-pflege-kleine-betriebe.html','maintenance','WEBSITE-PFLEGE FÜR KLEINE BETRIEBE',('Aktuell bleiben.','Ohne jedes Mal neu anzufangen.'),
    'Eine neue Öffnungszeit, ein anderes Bild oder ein technisches Update: Wir übernehmen die vereinbarte Pflege Ihrer bestehenden Website und geben verständlich Rückmeldung.',
    [('Texte','Bestehende Inhalte werden im vereinbarten Umfang aktualisiert.'),('Technik','Updates und Sicherungen richten sich nach Ihrer Umgebung und dem Paket.'),('Kontaktweg','Die wichtigen Einstiegsseiten und Anfragewege bleiben im Blick.')],['Änderung','Umsetzung','Kontrolle','Rückmeldung'])
add('onlineshop-kleine-haendler.html','commerce','ONLINESHOPS FÜR KLEINE HÄNDLER',('Gute Produkte.','Ein eigener digitaler Laden.'),
    'Ein überschaubares Sortiment braucht eine klare Produktführung und einen guten Weg zur Bestellung. Wir planen Ihren Shop mit dem Umfang, den Ihr Alltag tatsächlich braucht.',
    [('Sortiment','Produkte und Kategorien werden verständlich gegliedert.'),('Information','Preis, Beschreibung und vereinbarte Versandangaben gehören zusammen.'),('Bestellung','Kunden finden den passenden Weg zum Kauf oder zur Anfrage.')],['Produkte','Struktur','Shop','Einweisung'])
add('sq/faqe-dhe-perkthime.html','translation','FAQE WEB & PËRKTHIME',('Tri gjuhë.','Një mesazh i qartë.'),
    'Faqe web dhe tekste në gjermanisht, anglisht dhe shqip. Nga struktura e përmbajtjes te dizajni dhe përkthimi, me vëllim të qartë dhe kontroll personal.',
    [('Website','Përmbajtja, dizajni dhe kontakti krijojnë një faqe të kuptueshme.'),('Tekste','Mesazhi përshtatet me lexuesin dhe përdorimin e përmbajtjes.'),('Përkthime','Gjermanisht, anglisht dhe shqip, sipas projektit të dakorduar.')],['Ideja','Përmbajtja','Kontrolli','Dorëzimi'],cta='Diskutoni projektin',lang='sq')
add('sq/automatizim-ia.html','automation','AUTOMATIZIM ME IA',('Më pak përsëritje.','Më shumë qartësi.'),
    'Një proces i qartë për email, ofertë ose organizim takimesh. Përcaktojmë burimet, lidhjet dhe rregullat; hapat e rëndësishëm mbeten me miratimin tuaj.',
    [('Hyrja','Informacioni i nevojshëm merret nga burimet e dakorduara.'),('Përgatitja','IA rendit informacionin dhe përgatit hapin tjetër.'),('Miratimi','Personi përgjegjës kontrollon çfarë dërgohet jashtë.')],['Detyra','Burimet','Drafti','Miratimi'],cta='Diskutoni automatizimin',lang='sq')
add('ueber-mich.html','company','UNTERNEHMEN & ARBEITSWEISE',('Praxis trifft Technologie.','Aus Ideen wird Umsetzung.'),
    'Tafolli & Co. verbindet Marketing, Software, Beratung und KI-Automatisierung. Wir beginnen bei Ihrer Aufgabe und entwickeln daraus eine Lösung, die zu Ihrem Unternehmen passt.',
    [('Marketing','Ein stimmiger Auftritt für Marke, Website und Kommunikation.'),('Technology','Software und Anwendungen entlang Ihrer Anforderungen.'),('Consulting','Betriebliche Erfahrung unterstützt die Umsetzung.'),('AI Automation','Passende Abläufe mit klaren Zuständigkeiten und Freigaben.')],['Verstehen','Planen','Umsetzen','Begleiten'],cta='Lernen wir uns kennen')
add('werdegang.html','career','DER BERUFLICHE WEG DES GRÜNDERS',('Erfahrung, die bleibt.','Ideen, die weitergehen.'),
    'Vom klassischen Service über operative Führungsaufgaben bis zu Software und KI. Entdecken Sie die beruflichen Stationen von Kastriot Tafolli und die Verbindung zwischen Betrieb und Technologie.',
    [('Service','Die Grundlage entsteht in der täglichen Arbeit mit Gästen und Teams.'),('Führung','Operative Verantwortung erweitert den Blick auf Abläufe und Wirtschaftlichkeit.'),('Technologie','Software und KI ergänzen die betriebliche Erfahrung um digitale Möglichkeiten.')],['Service','Verantwortung','Führung','Technologie'])
add('referenzen.html','network','REFERENZEN & ZUSAMMENARBEIT',('Gute Verbindungen.','Neue Möglichkeiten.'),
    'Eigene Produkte, Projektbezüge und ein Netzwerk aus Gastronomie und Technologie. Die Auswahl verbindet bisherige Zusammenarbeit mit der persönlichen Berufserfahrung des Gründers.',
    [('Projekte','Eigene Entwicklung und bisherige Projektbezüge sind direkt verlinkt.'),('Gastronomie','Marken und Lieferanten aus dem betrieblichen Umfeld des Gründers.'),('Technologie','Plattformen und Technologieunternehmen aus dem bisherigen Projektumfeld.')],['Erfahrung','Austausch','Projekt','Zusammenarbeit'],cta='Zusammenarbeit besprechen')

# The budget planner already has its own complete interactive studio.
PAGES['preisrechner.html']=dict(path='preisrechner.html',kind='planner',lang='de')

add('kontakt.html','contact','KONTAKT & ERSTGESPRÄCH',('Eine gute Zusammenarbeit','beginnt mit Ihrer Idee.'),
    'Erzählen Sie uns, was Sie vorhaben. Gemeinsam klären wir Anforderungen, Umfang und den passenden ersten Schritt – persönlich und mit einem klaren Kontaktweg.',
    [('Vorhaben','Ein paar Sätze zu Ihrer Aufgabe helfen beim Einstieg.'),('Austausch','Ziele und vorhandene Grundlagen werden gemeinsam besprochen.'),('Nächster Schritt','Umfang, Zeitplan und Kosten werden vor einer Beauftragung abgestimmt.')],['Ihre Idee','Unser Gespräch','Der Umfang','Ihr Projekt'],cta='Projektanfrage öffnen')
add('wissen.html','knowledge','WISSEN & ORIENTIERUNG',('Gute Fragen.','Verständliche Antworten.'),
    'Einblicke in KI, betriebliche Entscheidungen und digitale Sichtbarkeit. Die Beiträge helfen, Möglichkeiten einzuordnen und die richtigen Fragen für Ihr Unternehmen zu stellen.',
    [('KI','Möglichkeiten, Anforderungen und menschliche Verantwortung zusammen betrachten.'),('Betrieb','Konditionen und wirtschaftliche Grundlagen verständlich einordnen.'),('Digital','Websites und Kontaktwege aus Sicht Ihrer Kunden betrachten.')],['Frage','Zusammenhang','Einordnung','Entscheidung'])
add('wissen-ki-im-hotel.html','automation','WISSEN · KI IM HOTEL',('Was KI kann.','Und was Menschen entscheiden.'),
    'Ein verständlicher Einstieg in KI für den Hotelbetrieb: Welche Aufgaben kommen infrage, welche Grundlagen werden gebraucht und wo bleibt menschliche Verantwortung notwendig?',
    [('Aufgabe','Ein konkreter betrieblicher Ablauf ist der richtige Ausgangspunkt.'),('Grundlage','Geeignete Informationen und Zuständigkeiten werden vorab geklärt.'),('Verantwortung','Entscheidungen und wichtige Freigaben bleiben nachvollziehbar.')],['Aufgabe','Information','Entwurf','Prüfung'])
add('wissen-getraenkevertrag.html','contracts','WISSEN · GETRÄNKEVERTRÄGE',('Mehr als ein Preis.','Ein Vertrag im Zusammenhang.'),
    'Lieferung, Ausstattung und Verpflichtungen beeinflussen die betriebliche Entscheidung. Dieser Beitrag ordnet wichtige Fragen zu Getränkevereinbarungen verständlich ein.',
    [('Leistung','Was wird geliefert und welche Unterstützung ist vereinbart?' ),('Verpflichtung','Welche Bindungen und Bezugsgrößen gehören zum Angebot?'),('Gesamtbild','Einzelne Vorteile werden mit dem gesamten Umfang verglichen.')],['Angebot','Bedingungen','Vergleich','Fragen'])
add('wissen-direktbuchungen.html','browser','WISSEN · DIREKTBUCHUNGEN',('Vom Interesse','zum direkten Kontakt.'),
    'Website, Informationen und Anfrageweg gehören zusammen. Der Beitrag zeigt, welche Fragen Gäste vor der Buchung klären möchten und wie der eigene Auftritt dabei unterstützt.',
    [('Angebot','Passende Informationen erleichtern die Orientierung.'),('Vertrauen','Ein nachvollziehbarer Auftritt beantwortet konkrete Fragen.'),('Kontakt','Der Weg zur Buchung oder Anfrage bleibt verständlich.')],['Interesse','Information','Vertrauen','Kontakt'])
add('rechner.html','analytics','BETRIEBLICHE POTENZIALRECHNER',('Annahmen verändern.','Zusammenhänge verstehen.'),
    'Spielen Sie einfache Szenarien zu Zeitaufwand, Direktbuchungen, Einkauf und Social Media durch. Die Rechner machen Annahmen sichtbar und ersetzen keine individuelle Prognose.',
    [('Annahmen','Ihre Eingaben bestimmen das jeweilige Rechenbeispiel.'),('Zusammenhang','Veränderte Werte zeigen den Einfluss einzelner Größen.'),('Einordnung','Das Ergebnis ist eine Gesprächsgrundlage, kein Leistungsversprechen.')],['Eingabe','Modell','Ergebnis','Einordnung'])
