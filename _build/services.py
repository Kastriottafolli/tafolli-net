"""Editorial service catalogue. Each topic has its own substantial, linked page."""
from icons import iconize
import html
from urllib.parse import quote
from bausteine import seite_rahmen, cta_block
from seo import region

from visuals import hero_visual, service_interlude, family
from conversion import TOPICS
from presence import local_listings

SERVICES=[]
def add(slug,title,group,lead,problem,approach,modules,example,outputs,faq,related):
    SERVICES.append(dict(slug=slug,title=title,group=group,lead=lead,problem=problem,approach=approach,modules=modules,example=example,outputs=outputs,faq=faq,related=related))

add('digitalisierung','Digitalisierung','Technologie',
'Ein digitaler Betrieb beginnt mit Abläufen, die zusammenpassen. Wir verbinden betriebliche Anforderungen mit der technischen Umsetzung.',
'Eine Reservierung steht im PMS, die Veranstaltungsdetails liegen in einer E-Mail und der Dienstplan lebt in einer Tabelle. Sobald Informationen mehrfach gepflegt werden, entstehen Rückfragen, Fehler und unnötige Handgriffe. Digitalisierung soll diesen Alltag vereinfachen und Ihrem Team eine verlässliche Grundlage geben.',
'Wir nehmen zunächst einen konkreten Ablauf auf: Wer benötigt welche Information, wann und in welchem System? Gemeinsam legen wir fest, welche Schritte bleiben, welche entfallen und wo eine technische Verbindung sinnvoll ist. Erst danach wählen wir Software und Schnittstellen aus.',
[('Systemlandschaft verstehen','Fachanwendungen, Kundendaten, Warenwirtschaft und Kommunikation werden als zusammenhängender Ablauf betrachtet. Datenquellen, Zuständigkeiten und doppelte Arbeit werden sichtbar.'),('Werkzeuge verbinden','Schnittstellen oder strukturierte Importe übertragen Informationen zwischen den vereinbarten Systemen. Wo eine direkte Anbindung fehlt, planen wir einen nachvollziehbaren Übergang statt einer fragilen Abkürzung.'),('Menschen mitnehmen','Neue Abläufe werden mit den Mitarbeitenden erprobt und dokumentiert. Schulung, Verantwortlichkeiten und Rückmeldungen gehören zur Einführung ebenso wie die Technik.')],
'Bei einer Veranstaltungsanfrage werden Informationen einmal strukturiert erfasst. Angebot, interne Abstimmung und Checkliste greifen auf dieselbe Grundlage zu; Änderungen müssen nicht in mehreren Dokumenten nachgetragen werden.',
['Übersicht Ihrer Systeme und Datenwege','Priorisierte Liste sinnvoller Verbesserungen','Ein abgegrenzter erster digitaler Ablauf','Dokumentation, Übergabe und vereinbarte Betreuung'],
[('Müssen wir unsere bestehende Software ersetzen?','Oft lässt sich mit vorhandenen Werkzeugen anfangen. Ein Wechsel wird erst sinnvoll, wenn konkrete Anforderungen mit dem bisherigen System nicht zuverlässig erfüllt werden können.'),('Wo beginnt ein kleiner Betrieb?','Bei einem häufigen und klar begrenzten Problem, etwa Veranstaltungsanfragen, Bestellungen oder täglichen Berichten. Ein funktionierender erster Ablauf schafft eine bessere Grundlage als ein großes unübersichtliches Projekt.')],
['softwareentwicklung','ki-entwicklung','ki-automatisierung'])

add('cybersecurity',
'Cybersecurity & IT-Sicherheit',
'Technology',
'Anwendungen, Websites, Zugänge und Unternehmensdaten strukturiert absichern. Umfang und Maßnahmen richten sich nach Ihren Systemen und dem konkreten Schutzbedarf.',
'Geteilte Konten, unklare Rechte, veraltete Anwendungen oder ungeprüfte Backups können den Betrieb beeinträchtigen. Bei neuen und bestehenden digitalen Lösungen müssen Sicherheit, Zuständigkeiten und Wiederanlauf zusammen betrachtet werden.',
'Wir erfassen die vereinbarten Anwendungen, Infrastruktur und Zugänge und priorisieren die erkennbaren Risiken. Daraus entstehen konkrete Schutzmaßnahmen und ein abgestimmter Umsetzungsplan. Spezialisierte Angriffsprüfungen oder Zertifizierungen sind eigenständige Leistungen mit geeigneten Fachpartnern.',
[('Zugänge und Berechtigungen', 'Persönliche Konten, Mehrfaktor-Anmeldung und definierte Rollen unterstützen den kontrollierten Zugriff. Eintritte, Rollenwechsel und Austritte erhalten nachvollziehbare Abläufe.'), ('Sichere Anwendungen und Systeme', 'Konfiguration, Updates, Abhängigkeiten, Schnittstellen und der Umgang mit vertraulichen Daten werden im vereinbarten Umfang betrachtet. Sicherheitsanforderungen fließen auch in neue Software- und Webprojekte ein.'), ('Backups und Betriebsabläufe', 'Sicherungen, Wiederherstellung, Überwachung und Verantwortlichkeiten werden dokumentiert. Tests des Wiederanlaufs sowie ein Vorgehen bei Störungen werden nach Bedarf vereinbart.')],
'Eine Unternehmensanwendung wird vor der Einführung auf Rollen, Zugänge und Datensicherung geprüft. Für ausgeschiedene Beschäftigte werden Zugriffe entzogen; die Wiederherstellung der benötigten Daten wird anhand eines abgestimmten Szenarios erprobt.',
['Bestandsaufnahme im vereinbarten Umfang', 'Priorisierte Schutzmaßnahmen und Zuständigkeiten', 'Dokumentierte Zugangs- und Wartungsabläufe', 'Abgestimmter Backup- und Wiederanlaufplan'],
[('Gehört ein Penetrationstest dazu?', 'Eine spezialisierte Angriffsprüfung wird als eigener Umfang vereinbart. Die grundlegende Absicherung ist keine Zertifizierung und ersetzt einen solchen Test nicht.'), ('Ist absolute Sicherheit möglich?', 'Nein. Ziel ist die nachvollziehbare Verringerung konkreter Risiken. Maßnahmen, Zuständigkeiten und die Grenzen des Auftrags werden ausdrücklich festgelegt.')],
['softwareentwicklung', 'webdesign', 'domain-hosting-email', 'digitalisierung'])

add('ki-entwicklung','KI-Entwicklung & KI-Assistenten','Technologie',
'KI wird nützlich, wenn sie Ihren Betrieb versteht. Wir entwickeln Assistenten für konkrete Aufgaben, mit ausgewählten Wissensquellen und klaren Grenzen.',
'Ein allgemeiner Chatbot kennt weder Ihre internen Regeln noch die aktuellen betrieblichen Abläufe. Ohne passende Informationen entstehen Antworten, die überzeugend klingen, aber nicht zum Betrieb passen. Gute KI-Entwicklung beginnt deshalb mit einer präzisen Aufgabe und einem verlässlichen Wissensbestand.',
'Wir definieren Nutzer, Fragen und gewünschte Ergebnisse. Wir strukturieren die geeigneten Quellen, entwickeln die technische Anbindung und prüfen Antworten anhand typischer sowie schwieriger Fälle. Informationen, die fehlen oder widersprüchlich sind, sollen sichtbar werden und an einen Menschen weitergegeben werden.',
[('Wissen nutzbar machen','Unternehmensinformationen, interne Anleitungen und freigegebene Dokumente werden geordnet. Der Assistent erhält nur Zugriff auf die Quellen und Funktionen, die für seine Aufgabe benötigt werden.'),('Antworten und Aktionen trennen','Ein Antwortentwurf braucht andere Rechte als eine Buchungsänderung. Wir legen fest, was die KI vorschlagen darf und welche Aktionen eine ausdrückliche Freigabe benötigen.'),('Qualität laufend prüfen','Beispielfragen, Quellenbezug und festgelegte Kriterien machen die Qualität überprüfbar. Rückmeldungen aus dem Betrieb helfen, Inhalte und Regeln gezielt zu verbessern.')],
'Ein interner Assistent beantwortet Fragen zum Bankettstandard anhand freigegebener Anleitungen. Findet er keine passende Quelle, markiert er die Lücke und nennt die zuständige Person, statt einen Ablauf zu erfinden.',
['Aufgabenbeschreibung und Wissensstruktur','Prototyp mit ausgewählten Quellen','Prüffälle und dokumentierte Grenzen','Anbindung, Einführung und Betreuung nach Vereinbarung'],
[('Trainieren Sie ein eigenes großes Sprachmodell?','Für viele Aufgaben ist ein bestehendes Modell mit passenden Wissensquellen und Regeln sinnvoller. Ob zusätzliche Anpassungen notwendig sind, entscheidet sich anhand der Aufgabe und der Tests.'),('Was passiert mit sensiblen Daten?','Vor der Umsetzung legen wir fest, welche Daten überhaupt benötigt werden, wer darauf zugreifen darf und welcher Anbieter geeignet ist. Die Datenverarbeitung wird als konkrete Projektanforderung behandelt.')],
['ki-automatisierung','teamo-ki','softwareentwicklung'])

add('softwareentwicklung',
'Individuelle Softwareentwicklung',
'Technology',
'Unternehmenssoftware, Fachanwendungen und Schnittstellen nach Ihren Anforderungen. Von der Konzeption über die Entwicklung bis zu Einführung, Wartung und Weiterentwicklung.',
'Standardsoftware bildet nicht jeden Ablauf passend ab. Zusätzliche Tabellen, manuelle Übertragungen und getrennte Datenquellen erschweren die Arbeit. Eine individuelle Anwendung kann konkrete Lücken schließen, wenn Anforderungen, Betrieb und langfristige Zuständigkeiten klar sind.',
'Wir klären Nutzer, Geschäftsabläufe, Daten und Integrationen und legen einen überprüfbaren Funktionsumfang fest. Daraus entstehen Architektur und erste Ansichten, danach die schrittweise Entwicklung und Prüfung. Ob Webanwendung, Backend, mobile App oder ergänzende Desktop-Lösung sinnvoll ist, entscheiden die Anforderungen.',
[('Anwendungen und Geschäftsprozesse', 'Fachanwendungen, Kundenportale, Dashboards, Freigaben und interne Werkzeuge werden auf die vorgesehenen Rollen und Aufgaben ausgerichtet. Bereits verfügbare Lösungen werden bei der Entscheidung berücksichtigt.'), ('Plattformen und Integration', 'Webanwendungen, mobile Apps für Apple iOS und Android sowie projektbezogene Desktop-Anwendungen können Teil einer Lösung sein. APIs, Datenbanken und bestehende Systeme werden über geeignete Schnittstellen verbunden.'), ('Qualität, Sicherheit und Betrieb', 'Prüfung wichtiger Abläufe, Rollen und Fehlerfälle gehört zur Umsetzung. Cybersecurity, Datenschutzanforderungen, Dokumentation, Bereitstellung und spätere Wartung werden mit dem Auftrag abgestimmt.')],
'Ein Unternehmen erfasst Kundenanfragen in einem Portal. Mitarbeitende prüfen Angaben, erstellen Angebote und verfolgen den Bearbeitungsstand. Vorhandene Systeme bleiben über abgestimmte Schnittstellen eingebunden; Zugriffe sind nach Rollen geregelt.',
['Anforderungsbeschreibung und abgestimmter Funktionsumfang', 'Architektur und Entwicklung der vereinbarten Anwendung', 'Prüfung relevanter Funktionen, Rollen und Integrationen', 'Dokumentation, Einführung und vereinbarte Betreuung'],
[('Welche Art von Software entwickeln Sie?', 'Das Angebot umfasst individuelle Unternehmensanwendungen, Weblösungen, Schnittstellen und mobile Anwendungen. Die technische Lösung und die unterstützten Plattformen werden anhand Ihrer Ziele, vorhandenen Systeme und des Budgets festgelegt.'), ('Kann vorhandene Software erweitert werden?', 'Ja, sofern Quellcode, Lizenzbedingungen oder geeignete Schnittstellen die gewünschte Erweiterung ermöglichen. Vor der Zusage prüfen wir Grundlage, Risiken und Aufwand.'), ('Wie unterscheiden sich Entwicklung und laufende Betreuung?', 'Der Entwicklungsauftrag legt die zu liefernden Funktionen und die Übergabe fest. Wartung, Hosting, Support oder Weiterentwicklung erhalten einen ausdrücklich vereinbarten Umfang.')],
['app-entwicklung', 'webdesign', 'cybersecurity', 'digitalisierung', 'ki-entwicklung'])

add('app-entwicklung',
'Apps für iOS, Android & Web',
'Technology',
'Mobile Anwendungen für Apple iOS und Android sowie browserbasierte Web-Apps. Plattform, Funktionen und Integrationen werden passend zum Einsatz geplant.',
'Eine Anwendung muss zu den Geräten und Aufgaben ihrer Nutzer passen. Ein interner Arbeitsablauf braucht andere Funktionen als eine Kunden-App. Offline-Nutzung, Gerätefunktionen, Zugriffsrechte und vorhandene Systeme beeinflussen die Entscheidung zwischen Web-App und nativer oder plattformübergreifender Anwendung.',
'Wir klären Zielgruppen, unterstützte Geräte und die wichtigsten Nutzungsschritte. Auf dieser Grundlage entstehen ein Bedienkonzept und ein abgegrenzter erster Funktionsumfang. Entwicklung, Anbindung und Tests erfolgen schrittweise; Veröffentlichung und Betrieb werden früh berücksichtigt.',
[('iOS und Android', 'Apps für iPhone, iPad und Android-Geräte werden nach dem vereinbarten Funktionsumfang entwickelt. Ob native oder plattformübergreifende Umsetzung sinnvoll ist, hängt von Gerätefunktionen, Leistung und Wartungsbedarf ab.'), ('Web-Apps und Systemanbindung', 'Browserbasierte Anwendungen, Portale und mobile Oberflächen können mit vorhandenen Datenbanken, APIs und Fachsystemen verbunden werden. Rollen, Freigaben und Offline-Anforderungen werden im Konzept festgelegt.'), ('Einführung und Weiterentwicklung', 'Tests auf vereinbarten Geräten, Datenschutz- und Sicherheitsanforderungen sowie die Bereitstellung gehören zur Planung. Bei Store-Veröffentlichungen werden die jeweiligen Vorgaben berücksichtigt; Updates und Betreuung werden separat abgestimmt.')],
'Ein Serviceteam erfasst Aufträge auf mobilen Geräten. Je nach Arbeitsumgebung wird eine iOS-/Android-App mit benötigten Gerätefunktionen oder eine Web-App eingesetzt. Der Bearbeitungsstand wird mit der bestehenden Unternehmenssoftware abgeglichen.',
['Bedienkonzept und abgestimmte Zielplattformen', 'App oder Web-App mit vereinbarten Funktionen', 'Schnittstellen, Rollen und geprüfte Nutzungsschritte', 'Vorbereitung der Bereitstellung und dokumentierte Übergabe'],
[('Entwickeln Sie für Apple und Android?', 'Ja. Apps für iOS auf iPhone und iPad sowie für Android sind Teil des Angebots. Welche Versionen, Geräte und Funktionen unterstützt werden, wird für das konkrete Projekt festgelegt.'), ('Brauchen wir eine App oder reicht eine Website?', 'Das hängt unter anderem von Nutzungshäufigkeit, Gerätefunktionen und Offline-Anforderungen ab. Eine Web-App kann ein geeigneter Einstieg sein; die Entscheidung folgt den Anforderungen.'), ('Übernehmen Sie auch die Veröffentlichung?', 'Vorbereitung und Begleitung einer Veröffentlichung können vereinbart werden. Dafür werden erforderliche Konten, Inhalte und Plattformvorgaben rechtzeitig geklärt; die Freigabe durch einen Store liegt beim jeweiligen Betreiber.')],
['softwareentwicklung', 'webdesign', 'cybersecurity', 'digitalisierung'])

add('webdesign','Website-Erstellung & Webdesign','Digitaler Auftritt',
'Ein Unternehmensauftritt darf begeistern und muss den nächsten Schritt einfach machen. Wir entwickeln Websites mit Persönlichkeit, klarer Struktur und passenden Kontakt- oder Buchungswegen.',
'Kunden möchten Ihr Angebot verstehen und konkrete Antworten finden: Leistungen, Nutzen, Ansprechpartner und der nächste Schritt. Wenn die Website diese Informationen versteckt oder auf dem Smartphone schwer zu bedienen ist, verlieren selbst schöne Bilder ihre Wirkung. Gestaltung und Nutzbarkeit müssen zusammenarbeiten.',
'Wir strukturieren Angebote und Zielgruppen, schreiben passende Inhalte und entwickeln ein visuelles Konzept. Animationen unterstützen die Geschichte Ihrer Marke. Buchungsstrecke, Kontakt und mobile Bedienung werden früh mitgedacht und vor dem Start geprüft.',
[('Gestaltung mit Charakter','Typografie, Bildsprache und Bewegung bilden einen zusammenhängenden Auftritt. Das Design wird aus Ihrer Marke entwickelt und bleibt auch ohne Animation verständlich.'),('Technische Umsetzung','Responsive Seiten, verständliche Navigation und schlanke Medien unterstützen die Nutzung auf unterschiedlichen Geräten. Bestehende Buchungsanbieter werden im vereinbarten Umfang eingebunden.'),('Inhalte und Auffindbarkeit','Eigene Seiten für Angebote, Zimmer oder Veranstaltungen beantworten konkrete Suchfragen. Titel, Beschreibungen und interne Links geben Menschen und Suchmaschinen Orientierung.')],
'Eine Restaurantseite zeigt Atmosphäre, aktuelle Speisekarte, Öffnungszeiten und Reservierung an einem Ort. Wer über die Suche auf eine Veranstaltung gelangt, findet direkt die passende Anfrage statt nur die allgemeine Startseite.',
['Seitenstruktur und visuelles Konzept','Responsive Umsetzung mit individuellen Inhalten','Buchungs- oder Kontaktanbindung','Prüfung und Einführung vor dem Start'],
[('Kann meine vorhandene Website modernisiert werden?','Ja. Inhalte, bestehende Adressen und benötigte Anbindungen werden zuerst aufgenommen. So kann die Modernisierung auf einer verlässlichen Grundlage erfolgen.'),('Wer aktualisiert später Karten und Angebote?','Das kann Ihr Team oder Tafolli &amp; Co. übernehmen. Die passende Lösung und die Zuständigkeit für laufende Änderungen werden vor dem Projekt festgelegt.')],
['suchmaschinenoptimierung','domain-hosting-email','foto-video'])

add('suchmaschinenoptimierung','Suchmaschinenoptimierung & lokale Sichtbarkeit','Digitaler Auftritt',
'Gefunden werden, wenn passende Kunden nach Ihrem Angebot suchen. Suchmaschinenoptimierung verbindet Technik, hilfreiche Inhalte und lokale Relevanz.',
'Eine Website kann viele Seiten haben und trotzdem die wichtigsten Fragen unbeantwortet lassen. Suchende möchten wissen, ob Ihr Unternehmen zu ihrem konkreten Bedarf passt und welche Leistungen es anbietet. Dafür brauchen sie hilfreiche Informationen und eindeutige Einstiegsseiten.',
'Wir prüfen vorhandene Seiten, Suchfragen und technische Hindernisse. Daraus entsteht eine priorisierte Inhalts- und Maßnahmenplanung. Wir verbessern zunächst die Seiten mit dem größten Bezug zu Ihrem Angebot und beobachten anschließend, welche Suchanfragen und Kontakte daraus entstehen.',
[('Technische Grundlage','Indexierbarkeit, Seitentitel, interne Links und mobile Nutzbarkeit werden geprüft. Beim Umbau bestehender Websites werden bisherige URLs und nötige Weiterleitungen berücksichtigt.'),('Hilfreiche Angebotsseiten','Jede wichtige Leistung oder Zielgruppe erhält passende Informationen. Inhalte beantworten konkrete Fragen, statt nur Suchbegriffe zu wiederholen.'),('Lokale Auffindbarkeit','Unternehmensdaten, Öffnungszeiten und regionale Inhalte werden konsistent aufbereitet. Vorhandene Unternehmensprofile und deren Verbindung zur Website fließen in die Bestandsaufnahme ein.')],
'Ein Hotel mit Tagungsangebot bekommt eine eigene Seite mit Raumgrößen, Möglichkeiten, Anreise und Anfrageweg. So finden Veranstaltungsplaner die relevanten Informationen auch ohne die gesamte Website zu durchsuchen.',
['Bestandsaufnahme von Technik und Inhalten','Plan für relevante Suchfragen und Angebotsseiten','Umsetzung priorisierter Verbesserungen','Auswertung anhand vereinbarter Kennzahlen'],
[('Ist mehr Text automatisch besser?','Nein. Ein Text hilft, wenn er eine echte Frage beantwortet und zum Angebot passt. Zusätzliche Seiten brauchen einen eigenen Zweck und sollten sich inhaltlich unterscheiden.'),('Garantieren Sie Platz eins?','Nein. Sichtbarkeit hängt von Wettbewerb, Suchanfrage und vielen weiteren Faktoren ab. Vereinbart werden konkrete Maßnahmen und nachvollziehbare Kennzahlen.')],
['webdesign','online-marketing','social-media'])

add('domain-hosting-email','Domain, Hosting & E-Mail','Digitaler Auftritt',
'Eine verlässliche Basis für Ihren digitalen Auftritt: eigene Domain, betreute Website und professionelle E-Mail-Adressen.',
'Wenn eine Domain auf den früheren Dienstleister läuft oder niemand die Zugangsdaten kennt, wird selbst eine kleine Änderung schwierig. Website, E-Mail und DNS müssen nachvollziehbar verwaltet werden. Klare Zuständigkeiten verhindern, dass der Betrieb bei einem Wechsel den Überblick verliert.',
'Wir prüfen Anbieter, Eigentümerschaft, Zugänge und die benötigten Funktionen. Danach planen wir Einrichtung oder Umzug mit Blick auf Website und E-Mail. Wartung, Sicherungen und Ansprechpartner werden dokumentiert, damit die technische Grundlage langfristig handhabbar bleibt.',
[('Domain und DNS','Die Domain wird dem richtigen Inhaber zugeordnet; relevante Einträge werden dokumentiert. Änderungen werden mit den beteiligten Anbietern abgestimmt.'),('Hosting und Wartung','Ein geeigneter Hostingumfang richtet sich nach der Website und den eingesetzten Anwendungen. Updates, Sicherungen und Zuständigkeiten werden ausdrücklich vereinbart.'),('E-Mail im Betrieb','Persönliche Postfächer, Funktionsadressen und Zugriffsregeln erhalten eine klare Struktur. Bei einem Umzug prüfen wir die benötigten Nachrichten, Geräte und Übergangsabläufe.')],
'Eine neue Restaurantleitung übernimmt den Betrieb. Domain und Postfächer werden mit dokumentierten Zugängen übergeben; allgemeine Anfragen gehen an eine Funktionsadresse und hängen nicht am Konto einer einzelnen Person.',
['Anbieter- und Zugangsübersicht','Einrichtung oder abgestimmter Umzugsplan','Dokumentierte Domain- und Postfachstruktur','Betreuung mit festgelegtem Umfang'],
[('Kann die bestehende Domain bleiben?','Ja. Häufig ändern sich nur Anbieter oder Verwaltung. Vor einer Änderung wird geprüft, wie die Domain aktuell mit Website und E-Mail verbunden ist.'),('Ist laufende Betreuung enthalten?','Der Betreuungsumfang wird im Angebot beschrieben. Dazu können Wartung, Sicherungen und Unterstützung bei Änderungen gehören; er wird auf Ihren Bedarf abgestimmt.')],
['cybersecurity','webdesign','digitalisierung'])

add('social-media','Social Media & Content','Digitaler Auftritt',
'Zeigen, was Ihr Unternehmen besonders macht. Mit Inhalten, die zu Ihrem Betrieb passen und einen klaren Weg zur Anfrage bieten.',
'Zwischen Tagesgeschäft und Kundenbetreuung bleibt wenig Zeit für regelmäßige Beiträge. Spontane Posts zeigen einzelne Momente, ergeben aber selten eine erkennbare Geschichte. Ein durchdachter Plan verbindet Fachwissen, Angebote und die Menschen hinter Ihrem Unternehmen.',
'Wir klären Zielgruppen, Kanäle und die wichtigsten Themen. Daraus entstehen ein Redaktionsplan und wiederverwendbare Formate. Inhalte werden mit Ihrem Team abgestimmt, Freigaben organisiert und Ergebnisse anhand der tatsächlich relevanten Reaktionen ausgewertet.',
[('Themen und Planung','Angebote, Fachthemen, Veranstaltungen und Teamgeschichten bilden einen planbaren Rhythmus. Die Frequenz richtet sich nach verfügbarer Qualität und Kapazität.'),('Beiträge und Reels','Text, Bild und kurze Videos werden für den jeweiligen Kanal gestaltet. Jeder Inhalt bekommt eine verständliche Aussage und bei Bedarf einen passenden Anfrageweg.'),('Betreuung und Auswertung','Kommentare, Zuständigkeiten und Freigaben werden geregelt. Neben Reichweite betrachten wir etwa Profilbesuche, Website-Klicks oder qualifizierte Anfragen.')],
'Ein saisonales Menü wird nicht nur einmal angekündigt: Ein Küchenmoment, die Geschichte einer Zutat und ein klarer Reservierungshinweis erzählen zusammen, warum sich ein Besuch lohnt.',
['Kanal- und Themenplanung','Abgestimmter Redaktionskalender','Gestaltete Beiträge und vereinbarte Formate','Auswertung und Anpassung der Inhalte'],
[('Müssen wir auf jedem Kanal aktiv sein?','Nein. Entscheidend ist, wo Ihre Zielgruppen erreicht werden können und welche Inhalte Sie verlässlich bereitstellen können. Wenige gut betreute Kanäle können sinnvoller sein.'),('Können Mitarbeitende Inhalte zuliefern?','Ja. Ein einfacher Ablauf für Material, Einwilligungen und Freigaben hilft dabei, authentische Momente aus dem Alltag nutzbar zu machen.')],
['foto-video','online-marketing','webdesign'])

add('foto-video','Foto, Video & visuelle Inhalte','Digitaler Auftritt',
'Produkte, Arbeitswelten und Menschen so zeigen, dass Ihr Unternehmen erlebbar wird. Visuelle Inhalte für Website, Kampagnen und soziale Kanäle.',
'Ein Bild kann zeigen, wie ein Zimmer aussieht. Eine durchdachte Bildserie zeigt, wie sich ein Aufenthalt anfühlt. Häufig fehlt Betrieben eine konsistente Auswahl für Website, Angebote und Social Media; vorhandenes Material passt weder zum Format noch zum aktuellen Auftritt.',
'Wir planen Motive, Einsatzorte und Formate vor dem Termin. Eine Aufnahmeplanung berücksichtigt den laufenden Betrieb, das Licht und beteiligte Personen. Produktion und Bearbeitung werden abgestimmt; besondere Aufnahmen wie Drohnenmaterial werden mit geeigneten Partnern und den erforderlichen Voraussetzungen geplant.',
[('Bildkonzept und Motive','Produkte, Dienstleistungen, Räume und Menschen bekommen eine gemeinsame Bildsprache. Eine Motivliste hilft, wichtige Angebote vollständig abzubilden.'),('Formate für den Einsatz','Website benötigt andere Ausschnitte als ein Reel oder eine Anzeige. Die benötigten Varianten werden von Beginn an berücksichtigt.'),('Auswahl und Übergabe','Das Material wird für die vereinbarten Kanäle geordnet und passend aufbereitet. Nutzungsumfang, Freigaben und Übergabeformate werden vorab geklärt.')],
'Für ein neues Dinnerangebot entstehen ein starkes Titelbild, Detailaufnahmen und kurze vertikale Sequenzen. Website und soziale Kanäle erzählen dieselbe Geschichte, ohne dass jedes Motiv neu produziert werden muss.',
['Motivliste und Aufnahmeplanung','Abgestimmte Foto- und Videoformate','Bearbeitete Auswahl für vereinbarte Kanäle','Geordnete Übergabe mit Nutzungsumfang'],
[('Ist ein großer Produktionstag nötig?','Nicht immer. Je nach Ziel können ein begrenzter Termin oder mehrere kleinere Einheiten sinnvoll sein. Die Planung richtet sich nach benötigtem Material und Betrieb.'),('Bieten Sie Drohnenaufnahmen an?','Drohnenmaterial kann projektbezogen geplant werden. Standort, Genehmigungen, geeignete Durchführung und Nutzungsumfang werden vor einer Zusage geklärt.')],
['webdesign','social-media','online-marketing'])

add('lieferantenvereinbarungen','Lieferantenvereinbarungen & Einkauf','F&B & Hospitality',
'Ein guter Einkauf endet nicht beim Stückpreis. Wir verbinden Bedarf, Lieferfähigkeit und nachvollziehbare Konditionen zu einer belastbaren Vereinbarung.',
'Ein scheinbar günstiger Preis kann durch Mindestmengen, Lieferkosten oder unpassende Gebinde relativiert werden. In der Hotellerie zählen zusätzlich Verfügbarkeit, Qualität und schnelle Reaktion bei Veranstaltungen. Lieferantenvereinbarungen müssen zum tatsächlichen Verbrauch und zum Alltag in Küche und Service passen.',
'Wir nehmen Bedarf, vorhandene Lieferanten und Vereinbarungen auf. Angebote werden auf einer vergleichbaren Grundlage gegenübergestellt. Anschließend bereiten wir Verhandlung und Entscheidung vor; auf Wunsch begleiten wir die Gespräche und dokumentieren die vereinbarten wirtschaftlichen Eckpunkte.',
[('Bedarf und Sortiment','Verbrauch, Qualität und Einsatz der Produkte werden gemeinsam mit dem Team betrachtet. So lässt sich erkennen, wo Bündelung hilft und wo Vielfalt für das Konzept wichtig bleibt.'),('Konditionen vergleichen','Preise, Fracht, Zahlungsziele, Mindestbestellungen und Rückvergütungen werden zusammen betrachtet. Ein Vergleich bewertet den realistischen Gesamtbezug statt isolierter Rabattzahlen.'),('Vereinbarungen nachhalten','Ansprechpartner, Laufzeiten und zugesagte Leistungen werden dokumentiert. Regelmäßige Abgleiche zeigen, ob Abrechnung und Lieferung der Vereinbarung entsprechen.')],
'Zwei Outlets bestellen ähnliche Produkte bei verschiedenen Lieferanten. Ein Vergleich prüft, ob eine gebündelte Beschaffung bessere Bedingungen bringt, ohne Qualität oder Lieferfähigkeit zu verschlechtern.',
['Bedarfs- und Lieferantenübersicht','Vergleich relevanter Gesamtkonditionen','Vorbereitung oder Begleitung der Verhandlung','Dokumentierte Vereinbarungen und Kontrollpunkte'],
[('Müssen wir den Lieferanten wechseln?','Nein. Oft lohnt zuerst ein strukturierter Abgleich und ein Gespräch mit dem bestehenden Partner. Ein Wechsel wird anhand von Qualität, Wirtschaftlichkeit und Zuverlässigkeit bewertet.'),('Ist das eine juristische Vertragsprüfung?','Im Mittelpunkt stehen betriebliche und wirtschaftliche Konditionen. Wenn eine rechtliche Prüfung notwendig ist, wird dafür eine entsprechend qualifizierte Beratung hinzugezogen.')],
['rueckverguetungen','getraenkevertraege','wareneinsatz-kalkulation'])

add('rueckverguetungen','Rückvergütungen, Boni & Jahresvereinbarungen','F&B & Hospitality',
'Was vereinbart wurde, soll auch nachvollziehbar ankommen. Wir machen Rückvergütungen und Bonusmodelle im Einkauf transparent.',
'Boni stehen manchmal in Nebenabreden, Jahresvereinbarungen oder wechselnden Abrechnungen. Mengenstaffeln, Produktgruppen und Fristen machen den Überblick schwierig. Ohne regelmäßigen Abgleich bleibt unklar, welche Beträge erwartet werden dürfen und welche Bedingungen bereits erfüllt sind.',
'Wir sammeln die relevanten Vereinbarungen und strukturieren die Berechnungsgrundlage. Bezugsdaten werden den Bedingungen gegenübergestellt. Daraus entsteht eine nachvollziehbare Übersicht für Abrechnung, Rückfragen und die nächste Verhandlungsrunde. Erwartete Beträge werden von tatsächlich bestätigten Gutschriften getrennt.',
[('Modelle sichtbar machen','Mengenboni, Umsatzstaffeln, Marketingzuschüsse und weitere vereinbarte Leistungen werden separat erfasst. Produktbezug, Zeitraum und Bedingungen bleiben nachvollziehbar.'),('Abrechnung abgleichen','Bezogene Mengen oder Nettoumsätze werden mit der vereinbarten Basis verglichen. Abweichungen und fehlende Gutschriften können gezielt beim Lieferanten geklärt werden.'),('Nächste Vereinbarung vorbereiten','Die tatsächliche Entwicklung liefert eine Grundlage für die kommende Jahresvereinbarung. Unrealistische Schwellen und unklare Bedingungen werden vor der Verhandlung sichtbar.')],
'Eine Jahresgutschrift fällt niedriger aus als erwartet. Der strukturierte Abgleich zeigt, welche Produktgruppen berücksichtigt wurden und ob die vereinbarte Mengenstaffel mit den Bezugsdaten übereinstimmt.',
['Übersicht aller relevanten Bonusvereinbarungen','Nachvollziehbare Berechnungsgrundlagen','Abgleich erwarteter und bestätigter Beträge','Fristen und Vorbereitung der Jahresgespräche'],
[('Wie hoch ist die mögliche Rückvergütung?','Das hängt von Ihren bestehenden Vereinbarungen, Bezugsvolumen und Produktgruppen ab. Eine belastbare Größenordnung ergibt sich erst aus dem Abgleich dieser Daten.'),('Ist eine Rückvergütung immer besser als ein günstigerer Preis?','Nein. Entscheidend sind die Gesamtkosten und die Bedingungen. Ein niedrigerer Bezugspreis kann wirtschaftlicher sein als ein hoher Bonus mit schwer erreichbarer Schwelle.')],
['lieferantenvereinbarungen','getraenkevertraege','rechner'])

add('getraenkevertraege','Getränkeverträge & Brauereivereinbarungen','F&B & Hospitality',
'Getränkeverträge prägen Kosten, Sortiment und Spielraum über Jahre. Wir unterstützen die wirtschaftliche Vorbereitung und Verhandlung.',
'Getränkepreise, Bezugspflichten, Ausstattung und Zuschüsse stehen oft in einem gemeinsamen Paket. Der sichtbare Vorteil am Anfang sagt wenig über die Gesamtkosten während der Laufzeit aus. Ein passender Vertrag muss Absatz, Gastronomiekonzept und betriebliche Entwicklung zusammen berücksichtigen.',
'Wir erfassen vorhandene Vereinbarungen, Absatzdaten und geplante Veränderungen. Alternativen werden auf einer vergleichbaren Basis gerechnet. So gehen Sie mit einer klaren Entscheidungsgrundlage in die Verhandlung; rechtliche Detailfragen werden bei Bedarf separat geprüft.',
[('Absatz und Sortiment','Tatsächliche Mengen, Gebinde und Verkaufspreise bilden die Grundlage. Geplante Änderungen im Outlet oder Konzept werden vor einer neuen Bindung berücksichtigt.'),('Gesamtkonditionen','Bezugspreise, Boni, Ausstattung, Zuschüsse und Laufzeit werden gemeinsam betrachtet. Wichtig ist, welche Leistung an welche Verpflichtung geknüpft ist.'),('Verhandlung und Nachhalten','Anforderungen und Verhandlungsspielräume werden vorbereitet. Vereinbarte wirtschaftliche Bedingungen werden dokumentiert und später mit der Abrechnung abgeglichen.')],
'Ein Restaurant erhält ein Angebot mit neuer Schankanlage und Zuschuss. Die Bewertung stellt Investition und laufende Bezugskonditionen über die geplante Laufzeit gegenüber und prüft, ob der erwartete Absatz zur Vereinbarung passt.',
['Bestandsaufnahme und Absatzübersicht','Vergleich der wirtschaftlichen Konditionen','Vorbereitete Verhandlungsposition','Abgestimmte Kontrollpunkte für die Laufzeit'],
[('Wann sollte eine neue Vereinbarung vorbereitet werden?','Mit ausreichend Vorlauf vor einem Vertragsende oder einer geplanten Veränderung. Bestehende Fristen und Verpflichtungen werden zuerst aufgenommen.'),('Kann ich einen Vertrag einfach kündigen?','Das hängt von der konkreten Vereinbarung ab. Rechtliche Fragen zu Kündigung, Bindung und Wirksamkeit müssen anhand des Vertrags gesondert geprüft werden.')],
['lieferantenvereinbarungen','rueckverguetungen','wissen-getraenkevertrag'])

add('wareneinsatz-kalkulation','Wareneinsatz & Kalkulation','F&B & Hospitality',
'Eine gute Karte überzeugt Gäste und trägt den Betrieb. Wir bringen Rezepturen, Einkauf und Verkaufspreise in eine nachvollziehbare Rechnung.',
'Ein Gericht verkauft sich gut und bringt trotzdem zu wenig Beitrag zum Ergebnis. Rezepturänderungen, steigende Einkaufspreise oder unklare Portionen verschieben die Kalkulation schleichend. Ohne klare Bezugsgrößen bleibt der Wareneinsatz eine Zahl, deren Ursachen niemand zuverlässig erklären kann.',
'Wir betrachten Rezepturen, Mengen, Einkaufspreise und Verkaufszahlen. Speisen und Getränke werden auf einer einheitlichen Basis kalkuliert. Anschließend prüfen wir gemeinsam, welche Änderungen wirtschaftlich und im Service sinnvoll sind, ohne das Konzept Ihres Hauses aus dem Blick zu verlieren.',
[('Rezepturen und Portionen','Mengen, Ausbeuten und Portionsstandards werden gemeinsam mit Küche und Bar geklärt. Eine dokumentierte Grundlage macht Änderungen und Preisentwicklungen sichtbar.'),('Deckungsbeiträge','Erlöse und relevante variable Kosten werden vergleichbar gegenübergestellt. Absolute Beiträge und Absatz zeigen mehr als eine isolierte Wareneinsatzquote.'),('Karte und Abläufe','Produktmix, Verkauf und Umsetzung werden zusammen betrachtet. Empfehlungen müssen zu Gästen, Einkauf und den Kapazitäten des Teams passen.')],
'Ein beliebtes Menü wird anhand seiner tatsächlichen Rezeptur und aktuellen Bezugspreise neu berechnet. Das Team kann beurteilen, ob Preis, Portion oder Beilage angepasst werden sollte und welche Wirkung zu erwarten ist.',
['Einheitliche Kalkulationsgrundlagen','Auswertung ausgewählter Speisen und Getränke','Priorisierte Maßnahmen für Karte und Einkauf','Kontrollrhythmus für Preis- und Rezepturänderungen'],
[('Welche Wareneinsatzquote ist richtig?','Das hängt unter anderem von Konzept, Sortiment und Preisniveau ab. Eine Zielquote wird mit den tatsächlichen Zahlen des Betriebs hergeleitet.'),('Muss dafür die gesamte Karte geändert werden?','Nein. Häufig beginnt die Arbeit mit häufig verkauften oder besonders kostenintensiven Positionen. Die Analyse zeigt, wo eine Änderung tatsächlich sinnvoll ist.')],
['inventur-warenwirtschaft','lieferantenvereinbarungen','revenue-controlling'])

add('inventur-warenwirtschaft','Inventur & Warenwirtschaft','F&B & Hospitality',
'Bestände, Verbrauch und Bestellung miteinander verbinden. Für weniger Überraschungen zwischen Lager, Küche und Monatsabschluss.',
'Unterschiedliche Zähleinheiten, offene Umbuchungen und ungeklärte Brüche machen Inventuren mühsam. Wenn die Grundlage ungenau ist, lassen sich Fehlmengen oder der tatsächliche Verbrauch nur schwer beurteilen. Eine verlässliche Warenwirtschaft braucht gemeinsame Regeln und einen Ablauf, der unter Zeitdruck funktioniert.',
'Wir nehmen Lagerstruktur, Artikeldaten und die bestehenden Zählprozesse auf. Wir vereinheitlichen Einheiten und Verantwortlichkeiten und testen den Ablauf mit dem Team. Abweichungen werden anschließend gezielt untersucht, statt jede Inventur wieder von vorn zu erklären.',
[('Artikel und Einheiten','Gebinde, Zähleinheiten und Bewertung werden eindeutig festgelegt. Doppelte oder veraltete Artikel erschweren die Auswertung und werden bereinigt.'),('Inventur im Alltag','Zählbereiche, Zeitpunkte und Verantwortlichkeiten erhalten eine klare Struktur. Dokumentierte Umbuchungen und Bewegungen machen Bestandsänderungen nachvollziehbar.'),('Bestellung und Kontrolle','Mindestbestände und Bestellrhythmen richten sich nach Verbrauch, Lieferzeiten und Veranstaltungen. Auffällige Differenzen werden regelmäßig besprochen.')],
'Die Bar zählt Flaschen, während die Warenwirtschaft Liter erwartet. Nach der Vereinheitlichung der Zähleinheit lassen sich Bestände korrekt bewerten und vermeintliche Verbrauchsabweichungen auflösen.',
['Strukturierte Artikel- und Lagergrundlage','Dokumentierter Inventurablauf','Zuständigkeiten und Zähleinheiten','Auswertung und Bearbeitung von Abweichungen'],
[('Brauchen wir ein neues Warenwirtschaftssystem?','Nicht zwingend. Zuerst wird geprüft, ob vorhandene Software die benötigten Regeln und Auswertungen unterstützt. Gute Stammdaten bleiben auch bei einem Wechsel entscheidend.'),('Wie oft sollte gezählt werden?','Der sinnvolle Rhythmus hängt von Warengruppe, Verbrauch und Kontrollbedarf ab. Häufige Teilinventuren können eine vollständige Bestandsaufnahme ergänzen.')],
['wareneinsatz-kalkulation','digitalisierung','lieferantenvereinbarungen'])

add('interim-fb-management','Interim F&B-Management','F&B & Hospitality',
'Führung auf Zeit, wenn Ihr Betrieb Klarheit und Entlastung braucht. Operative Verantwortung mit vereinbartem Auftrag und sauberer Übergabe.',
'Eine vakante Führungsposition, ein neues Outlet oder eine Saison mit hoher Belastung kann ein Team schnell an seine Grenzen bringen. In solchen Phasen braucht es Entscheidungen, sichtbare Ansprechpartner und verlässliche Abläufe. Externe F&B-Leitung kann eine Lücke überbrücken und zugleich Strukturen verbessern.',
'Vor dem Einsatz legen wir Auftrag, Entscheidungsspielraum, Präsenz und Zielsetzung fest. Wir arbeiten mit den bestehenden Führungskräften und dem Team an den priorisierten Aufgaben. Fortschritt und offene Punkte werden regelmäßig besprochen; die Übergabe wird von Anfang an mitgeplant.',
[('Operative Orientierung','Abläufe in Restaurant, Frühstück, Bar und Bankett werden gemeinsam betrachtet. Akute Engpässe und Verantwortlichkeiten bekommen zuerst eine klare Struktur.'),('Führung und Zahlen','Dienstplanung, Qualitätsstandards und relevante Kennzahlen werden in einen nutzbaren Arbeitsrhythmus gebracht. Entscheidungen werden mit den verantwortlichen Personen abgestimmt.'),('Übergabe und Kontinuität','Standards und offene Aufgaben werden dokumentiert. Die spätere Führung soll auf nachvollziehbaren Strukturen aufbauen können.')],
'Nach einem Führungswechsel fehlt die Abstimmung zwischen Küche, Service und Veranstaltungsverkauf. Ein befristeter Einsatz ordnet Besprechungen, Zuständigkeiten und Übergaben, während die dauerhafte Nachfolge aufgebaut wird.',
['Klarer Einsatzauftrag und Zuständigkeiten','Priorisierte operative Maßnahmen','Regelmäßige Abstimmung mit der Geschäftsführung','Dokumentierte Übergabe an die Folgeorganisation'],
[('Sind Sie dauerhaft vor Ort?','Präsenz und Umfang werden abhängig vom Auftrag und der vereinbarten Verfügbarkeit vereinbart. Ein Interim-Einsatz wird vorab zeitlich und organisatorisch abgestimmt.'),('Ist das auch für ein einzelnes Restaurant möglich?','Ja. Der Auftrag kann sich auf einen Betrieb oder ein bestimmtes Outlet beziehen. Wichtig sind eine klare Aufgabe und die nötigen Entscheidungswege.')],
['fb-beratung','personal-recruiting','revenue-controlling'])

add('revenue-controlling','Revenue Management & F&B-Controlling','F&B & Hospitality',
'Zahlen verstehen und daraus Entscheidungen machen. Wir unterstützen Budget, Forecast und Ergebnissteuerung mit Blick auf den operativen Alltag.',
'Hoher Umsatz ist kein ausreichendes Zeichen für ein gutes Ergebnis. Personaleinsatz, Wareneinsatz, Auslastung und Produktmix müssen gemeinsam betrachtet werden. Unterschiedliche Datenquellen und uneinheitliche Berichte erschweren oft den Blick darauf, wo sich eine Veränderung tatsächlich lohnt.',
'Wir klären die verfügbaren Daten und die Entscheidungen, die daraus entstehen sollen. Kennzahlen erhalten eindeutige Definitionen und einen passenden Berichtszeitraum. Abweichungen werden mit dem Betrieb eingeordnet; daraus folgen konkrete Maßnahmen statt zusätzlicher Tabellen ohne Verantwortliche.',
[('Budget und Forecast','Planannahmen werden mit Saison, Kapazität und Angebot verbunden. Neue Informationen fließen in einen nachvollziehbaren Forecast ein.'),('Kennzahlen und Berichte','Umsatz je Outlet, Personaleinsatz, Wareneinsatz und Deckungsbeiträge werden passend zum Betrieb strukturiert. Datenqualität und Bezugsgrößen bleiben sichtbar.'),('Preis und Kapazität','Preisgestaltung und verfügbare Leistung werden gemeinsam bewertet. Ein Angebot muss nicht nur Nachfrage schaffen, sondern auch mit Küche, Service und Kapazität umsetzbar sein.')],
'Ein Bankett erzielt hohen Umsatz, bindet aber mehr Personal als geplant. Eine Auswertung von Erlös, Wareneinsatz und Einsatzstunden zeigt, wie künftige Angebote und Personaleinteilung angepasst werden können.',
['Definition relevanter Kennzahlen','Struktur für Budget und Forecast','Nutzbare regelmäßige Berichte','Maßnahmen mit Zuständigkeit und Kontrolltermin'],
[('Reichen unsere Kassendaten aus?','Sie sind oft ein guter Einstieg. Ob zusätzliche Angaben benötigt werden, hängt von der Fragestellung ab; Datenlücken werden bei der Analyse ausdrücklich benannt.'),('Wird alles automatisch ausgewertet?','Erst wenn Daten und Definitionen verlässlich sind, lohnt eine automatische Auswertung. Die Interpretation wichtiger Abweichungen bleibt eine gemeinsame betriebliche Aufgabe.')],
['wareneinsatz-kalkulation','softwareentwicklung','digitalisierung'])

add('personal-recruiting','Hospitality-Recruiting & Teamentwicklung','F&B & Hospitality',
'Passende Menschen finden, gut einarbeiten und gemeinsam führen. Mit Rollen und Standards, die zur Realität von Hotellerie und Gastronomie passen.',
'Eine offene Stelle ist selten nur eine fehlende Person. Unklare Rollen, fehlende Einarbeitung oder ein nicht planbarer Alltag erschweren die Besetzung und Bindung. Erfolgreicher Teamaufbau beginnt deshalb mit einem ehrlichen Blick auf Aufgaben, Führung und die Arbeitsbedingungen im Betrieb.',
'Wir unterstützen die Definition von Rollen, die Vorbereitung des Auswahlverfahrens und die Struktur der Einarbeitung. Gemeinsam entwickeln wir verständliche Standards und geeignete Schulungsformate. Die operative Perspektive hilft, Anforderungen konkret zu formulieren und neue Mitarbeitende schneller ins Team einzubinden.',
[('Rollen und Auswahl','Aufgaben, Verantwortung und Schnittstellen werden beschrieben. Gespräche und praktische Fragen orientieren sich an den tatsächlichen Anforderungen der Position.'),('Onboarding und Ausbildung','Ein planbarer Einstieg verbindet Ansprechpartner, Lernschritte und Rückmeldungen. Serviceabläufe und wichtige Hausstandards werden verständlich vermittelt.'),('Führung und Bindung','Regelmäßige Abstimmung, klarer Dienstplanprozess und erkennbare Entwicklungsmöglichkeiten unterstützen die Zusammenarbeit. Maßnahmen werden an den jeweiligen Betrieb angepasst.')],
'Eine neue Restaurantleitung erhält einen strukturierten Einstieg: Hausstandards, Kalkulationsgrundlagen, Ansprechpartner und konkrete Ziele. Das Team weiß, welche Entscheidungen die neue Rolle übernimmt und wo Abstimmung nötig ist.',
['Rollenprofile und Anforderungsgrundlage','Strukturierter Auswahl- und Einarbeitungsablauf','Passende Schulungsschwerpunkte','Verantwortlichkeiten und regelmäßige Rückmeldung'],
[('Garantieren Sie die Besetzung einer Stelle?','Nein. Die Unterstützung verbessert Profil, Ansprache und Auswahlprozess; eine konkrete Besetzung hängt auch von Markt, Bedingungen und Kandidaten ab.'),('Können bestehende Teams begleitet werden?','Ja. Schulungen, Rollenklärung und Führungsabläufe können unabhängig von einer Neueinstellung vereinbart werden.')],
['interim-fb-management','fb-beratung','werdegang'])

# All existing service URLs remain assigned to one of the four main areas.
for item in SERVICES:
    if item['slug'] == 'ki-entwicklung':
        item['group'] = 'AI Automation'
    elif item['slug'] in ['suchmaschinenoptimierung', 'social-media', 'foto-video']:
        item['group'] = 'Marketing'
    elif item['group'] in ['F&B & Hospitality']:
        item['group'] = 'Consulting'
    else:
        item['group'] = 'Technology'

from seo_content import apply as refresh_search_content
refresh_search_content(SERVICES)

for service in SERVICES:
    if service['slug']=='webdesign':
        service['lead']+=' Landingpages und Mini-Websites beginnen bei 1.500 €. Umfang, Design und Funktionen bestimmen das Angebot.'
        service['faq'].append(('Was kostet eine neue Website?', 'Landingpages und Mini-Websites beginnen bei 1.500 €, One-Pager bei 2.500 € und Smart-Pages mit mehreren Unterseiten bei 4.500 €. Onlineshops planen wir ab 6.500 €; größere Shops und integrierte Web-Apps nach Umfang. Die Spannen im Projektplaner sind unverbindliche Orientierungswerte.'))
    elif service['slug']=='suchmaschinenoptimierung':
        service['lead']+=' SEO und Inhalte planen wir ab 450 € im Monat, die laufende Betreuung lokaler Einträge ab 550 € im Monat.'
        service['faq'].append(('Welche Budgets sollte ich für SEO und lokale Einträge planen?', 'SEO und Inhalte beginnen bei 450 € monatlich. Für die laufende Betreuung lokaler Einträge planen wir mindestens 550 € monatlich. Die einmalige Profileinrichtung beginnt ebenfalls bei 550 € und wird gesondert vereinbart. Maßnahmen, Standorte und Umfang stehen im konkreten Angebot.'))

LOOKUP={s['slug']:s for s in SERVICES}
EXISTING={'ki-automatisierung':'AI Automation','teamo-ki':'TeamO · KI-Assistent für Hospitality','fb-beratung':'Consulting & F&B-Beratung','online-marketing':'Marketingstrategie, Branding & Kampagnen','rechner':'Potenzialrechner','wissen-getraenkevertrag':'Wissen: Getränkeverträge','werdegang':'Werdegang des Gründers'}

def link(slug):
    title=LOOKUP[slug]['title'] if slug in LOOKUP else EXISTING[slug]
    return f'<a href="{slug}.html">{html.escape(title)} <span aria-hidden="true">↗</span></a>'

def catalogue():
    groups = [
        ('Marketing', ['online-marketing','suchmaschinenoptimierung','social-media','foto-video']),
        ('Technology', ['softwareentwicklung','app-entwicklung','webdesign','cybersecurity','domain-hosting-email','digitalisierung']),
        ('Consulting', ['fb-beratung','lieferantenvereinbarungen','getraenkevertraege','rueckverguetungen','wareneinsatz-kalkulation','inventur-warenwirtschaft','interim-fb-management','revenue-controlling','personal-recruiting']),
        ('AI Automation', ['ki-automatisierung','ki-entwicklung','teamo-ki']),
    ]
    descriptions = ['Strategie, Marke und Kommunikation.','Anwendungen, Systeme und Sicherheit.','Prozesse, Organisation und Wirtschaftlichkeit.','KI-Assistenten und automatisierte Abläufe.']
    return '<div class="portfolio-groups">'+''.join(f'<section><p class="tag">0{i+1} / {label}</p><h3>{descriptions[i]}</h3><div class="portfolio-links">'+''.join(link(slug) for slug in slugs)+'</div></section>' for i,(label,slugs) in enumerate(groups))+'</div>'

def page(s):
    path=s['slug']+'.html'; title=html.escape(s['title']); desc=html.escape(s['lead'])
    enquiry='kontakt.html?thema='+family(s['slug'])+'&amp;leistung='+quote(s['title'])+'#projektanfrage'
    modules=''.join(f'<article><span class="tag">0{i+1}</span><h3>{t}</h3><p>{b}</p></article>' for i,(t,b) in enumerate(s['modules']))
    faq=''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in s['faq'])
    related=''.join(link(slug) for slug in s['related'])
    content=f'''<section class="service-hero"><div class="shell"><div class="service-hero-grid"><div><p class="tag">{s['group']} / TAFOLLI &amp; CO.</p><h1>{title}</h1><p class="lede">{s['lead']}</p><a href="{enquiry}" class="btn btn-1">{TOPICS[family(s['slug'])]['cta']} ↗</a></div>{hero_visual(s['slug'])}</div><nav class="service-toc" aria-label="Auf dieser Seite"><a href="#ausgangslage">01 Ausgangslage</a><a href="#umfang">02 Leistungen</a><a href="#praxis">03 Praxis</a><a href="#ergebnisse">04 Zusammenarbeit</a><a href="#fragen">05 Fragen</a></nav></div></section>
<section class="service-section" id="ausgangslage"><div class="shell service-editorial"><div><p class="tag">01 / AUSGANGSLAGE</p><h2>Ausgangslage<br>und Vorgehen.</h2></div><div><p>{s['problem']}</p><p>{s['approach']}</p></div></div></section>
<section class="service-section service-tint" id="umfang"><div class="shell"><p class="tag">02 / WAS DAZUGEHÖRT</p><h2>Leistungsumfang.</h2><div class="service-modules">{modules}</div></div></section>
{service_interlude(s['slug'])}
<section class="service-section" id="praxis"><div class="shell service-editorial"><div><p class="tag">03 / EIN MÖGLICHER ANWENDUNGSFALL</p><h2>Anwendungsbeispiel.</h2></div><div class="service-example"><span aria-hidden="true">↗</span><p>{s['example']}</p><small>Zur Erklärung: ein beispielhafter Ablauf, keine Kundenerfolgsmeldung.</small></div></div></section>
<section class="service-section service-tint" id="ergebnisse"><div class="shell service-editorial"><div><p class="tag">04 / ZUSAMMENARBEIT</p><h2>Ergebnisse und<br>Zusammenarbeit.</h2></div><div><ul class="service-outputs">{''.join('<li>'+t+'</li>' for t in s['outputs'])}</ul><p>Am Anfang steht ein Gespräch über Ihren Betrieb. Danach erhalten Sie ein Angebot mit Umfang, Prioritäten und Zuständigkeiten. Wir beginnen mit einem überschaubaren Auftrag und prüfen gemeinsam, wie die Ergebnisse in Ihren Alltag passen. Eine laufende Begleitung kann separat vereinbart werden.</p><p>Tafolli &amp; Co. verbindet Software, KI und Online-Marketing mit betrieblicher Beratung. Die persönliche Erfahrung des Gründers in Hotellerie und Gastronomie ergänzt den Blick auf Abläufe, Teams und Wirtschaftlichkeit.</p></div></div></section>
<section class="service-section" id="fragen"><div class="shell service-editorial"><div><p class="tag">05 / HÄUFIGE FRAGEN</p><h2>Häufige Fragen.</h2></div><div class="service-faq">{faq}</div></div></section>
<section class="service-section service-related"><div class="shell"><p class="tag">DAS PASST DAZU</p><h2>Verwandte Leistungen.</h2><div class="portfolio-links">{related}</div><a class="lnk" href="leistungen.html">Das gesamte Portfolio ansehen ↗</a></div></section>'''
    if s['slug']=='suchmaschinenoptimierung':
        content=content.replace('<section class="service-section" id="praxis">',local_listings()+'<section class="service-section" id="praxis">')
        content=content.replace('<a href="#fragen">05 Fragen</a>','<a href="#fragen">05 Fragen</a><a href="#lokale-eintraege">Lokale Einträge</a>')
    if s['slug'] in {'webdesign','suchmaschinenoptimierung'}:
        content=content.replace('<a href="#fragen">05 Fragen</a>','<a href="#fragen">05 Fragen</a><a href="preisrechner.html#budgetplaner">Budget planen ↗</a>')
    for old,new in zip(['Ausgangslage<br>und Vorgehen.','Leistungsumfang.','Anwendungsbeispiel.','Ergebnisse und<br>Zusammenarbeit.','Häufige Fragen.'],s.get('headings',[])):
        content=content.replace('<h2>'+old+'</h2>','<h2>'+new+'</h2>')
    content+=region(service=s['title'])
    content+=cta_block('// nächster schritt',[["Projekt besprechen."]],f'Beschreiben Sie uns, was Sie bei {title} verbessern möchten. Gemeinsam klären wir den passenden ersten Schritt.','Gespräch vereinbaren',enquiry,'Unternehmen kennenlernen','ueber-mich.html')
    return seite_rahmen('leistungen.html',title+' · Tafolli & Co.',desc,path,content)

def build(root):
    for s in SERVICES:
        (root/(s['slug']+'.html')).write_text(iconize(page(s)))
        print('  '+s['slug']+'.html [Leistung]')
