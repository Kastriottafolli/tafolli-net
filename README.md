# tafolli.net

Persönliche Webseite von Kastriot Tafolli. F&B Manager in der 5-Sterne-Hotellerie,
Softwareingenieur mit Schwerpunkt Künstliche Intelligenz, Inhaber von TB Solutions.

Reines HTML, CSS und JavaScript. Kein Framework, keine Abhängigkeiten zur
Laufzeit, keine Anfrage an fremde Server. Die Dateien können so wie sie sind
auf jeden Webserver gelegt werden.

Alle Seiten werden aus `_build/` erzeugt:

    python3 _build/bau_alles.py

- `_build/experience.py` mit `experience_content.py` und den vorhandenen
  Inhalten in `inhalt_de.py`, `inhalt_en.py`, `inhalt_sq.py`: die Startseite
  auf Deutsch, Englisch und Albanisch (`/`, `/en/`, `/sq/`) sowie die eigene
  Angebotsseite `ki-automatisierung.html`. `_build/bau.py` bleibt als
  kompatibler Einstieg für diese Seiten erhalten.
- `_build/artwork.py`: erzeugt das originale SVG-Objekt als statischen
  Ersatz für die animierte Canvas-Grafik.
- `_build/bausteine.py`: Kopf- und Fusszeile sowie wiederverwendbare
  Abschnitte fuer alle Unterseiten.
- `_build/seiten_a.py` bis `seiten_d.py`: Inhalt und Aufbau der 16
  Unterseiten (Ueber mich, Werdegang, Leistungen, F&B-Beratung,
  Online-Marketing, TeamO, Rechner, Wissen mit drei Artikeln, Referenzen,
  Kontakt, Impressum, Datenschutz, 404).

- `_build/services.py`: 18 vertiefte Leistungsseiten mit Ausgangslage, konkretem
  Umfang, Anwendungsbeispiel, Zusammenarbeit, FAQ und passenden internen Links.
  Zusammen mit den vier bestehenden Leistungsseiten bildet dies 22 Bereiche.
- `_build/companies.py`: verifizierte offizielle Links der sechs beruflichen Stationen.

Das neue Design und die Interaktionen liegen in `assets/experience.css`
und `assets/experience.js`: animiertes neuronales KI-Gehirn, Scroll-Erzählung,
Workflow-Demo mit drei Szenarien, Zeitwert-Rechner, mobile Navigation und
Bewegungsschalter. Die vorhandenen Unterseiten verwenden weiterhin die
Grundbausteine aus `assets/kt.css` und den Rechner aus `assets/kt.js`,
ergänzt um das gemeinsame helle Design. Nach Änderungen an diesen Dateien
den Bau wiederholen, damit die Versionsmarken aktualisiert werden.

Die Demo verwendet ausschließlich fiktive Beispieldaten und versendet
nichts. Der neue Rechner verwendet 22 Arbeitstage pro Monat und zeigt
einen rechnerischen Zeitwert vor Servicekosten, keine garantierte
Einsparung. Seine Werte werden nur dann in das eigene E-Mail-Programm
übernommen, wenn ein Besucher den Kontakt-Link anklickt.

Bewegung kann über den Schalter in der Navigation pausiert werden.
`prefers-reduced-motion` wird automatisch berücksichtigt; das Canvas
pausiert außerhalb des sichtbaren Bereichs und in inaktiven Tabs. Auf
kleinen Bildschirmen und bei reduzierter Bewegung wird die Scroll-Erzählung
als normale, vollständig lesbare Liste dargestellt. Schriftarten und
Grafiken werden lokal geladen; es gibt keine Tracker, Cookies oder
externen Bibliotheken.

Die Unterseiten sind derzeit nur auf Deutsch vorhanden. Die Navigation führt
zu echten Seiten. Die Startseite zeigt die Verbindung aus Hospitality und
Technologie; Scroll-Erzählung, Betreuung und Zeitwert-Rechner liegen auf der
eigenen Automation-Seite. Das Gesamtangebot ist über `leistungen.html` erreichbar.
Die gemeinsame Palette verwendet Cremeweiß, Grün, Orange und dunkle Neutraltöne.

Prüfen:

    python3 _build/verify.py
    node --check assets/experience.js
    node --check assets/partners.js
    node --check assets/brand.js
    node --check assets/kt.js

Die Prüfung kontrolliert alle erzeugten Seiten, lokale Links und Anker,
Assets, Metadaten, übersetzte Demo-Daten und den Sitemap-Eintrag. Ein
GitHub-Actions-Check baut die Seiten bei Pull Requests neu und prüft,
dass die eingecheckten Dateien dem Ergebnis entsprechen.

Referenzen und Partner werden zentral in `_build/partners.py` gepflegt.
Die sechs Referenz-Websites sowie Getränke-, Gastronomie- und Technologiepartner
haben lokale Logos und direkte Website-Links. Die Herkunft der Logos steht in
`assets/partners/sources.json`. Beim normalen Seitenbau wird nichts heruntergeladen.
Die Startseiten enthalten eine kompakte Logo-Leiste aus einer Auswahl des Netzwerks.
`assets/partners.js` ermöglicht langsames Gleiten und eine Pause, stoppt bei Fokus,
Mauszeiger und unsichtbaren Tabs und berücksichtigt reduzierte Bewegung sowie den
globalen Bewegungsschalter. Ohne JavaScript bleibt eine manuell scrollbare Leiste.

Die sechs Hotelstationen auf der Referenzseite werden in `_build/hotels.py` gepflegt.
Jede Karte verbindet das verlinkte Logo mit Funktion, Zeitraum, Verantwortungsumfang
und einem konkreten Kundennutzen aus der vorhandenen Berufserfahrung. Die Logos
kommen von offiziellen Websites; bei Cerês am Meer ist die heutige Marke A-ROSA
mit einem Hinweis auf der Karte sichtbar. Es werden keine neuen Erfolgszahlen behauptet.

Das TAFOLLI-Markenzeichen verbindet eine Gehirn-Silhouette mit einem T im
Negativraum und einem warmen Signalpunkt. `_build/brand.py` erzeugt den gemeinsamen
Logo-Auftritt und die lokalisierte Startanimation. Das Originalzeichen liegt
optimiert unter `assets/brand/`; Navigation, Fußzeile, Referenzkarte und Favicons
verwenden dieselbe Identität. `assets/brand.js` zeigt
auf allen Seiten eine höchstens 1,8 Sekunden lange Animation bei jedem Aufruf,
Neuladen und Seitenwechsel, auch beim Zurück-/Vorwärtsgehen im Browser.
Das Zeichen verbindet sich aus zwei Hälften und wandert in die Kopfzeile.
Reduzierte Bewegung und inaktive Tabs überspringen das Intro. Ankersprünge
innerhalb des bereits geöffneten Dokuments starten es nicht erneut. Jede
Interaktion beendet es sofort; Inhalt und Navigation bleiben zugänglich. Ohne JavaScript ist das Intro verborgen und das Logo statisch sichtbar.
Für die Animation wird nichts im Browser gespeichert.


### Navigation, Porträt und SEO

`_build/navigation.py` definiert die gemeinsame Hauptnavigation: Leistungen
mit drei Gruppen und 22 Angeboten, Über mich mit Profil und Netzwerk, Wissen
mit Ratgebern und vier Rechnern sowie Kontakt mit Zusammenarbeit und Rechtlichem.
Alle 38 HTML-Seiten sind darin direkt verlinkt, einschließlich der drei Sprach-
Startseiten und der 404-Orientierungsseite. Desktop- und Mobilansicht verwenden
denselben Baum. Native `details` funktionieren ohne JavaScript;
`assets/navigation.js` ergänzt gegenseitiges Schließen, Außenklick, Escape,
Fokusrückkehr und den mobilen Menüknopf. Die aktive Detailseite ist markiert.

`_build/portrait.py` zeigt das natürliche Farbfoto mit einer grafischen Signatur.
Beim Darüberfahren läuft ein kurzer Impuls entlang des Rahmens. Reduzierte
Bewegung und der Animations-Pauseknopf unterbinden diesen Effekt.

`_build/seo.py` verwaltet individuelle Titel und Beschreibungen, konsistente
Organization-/Person-/WebSite-Daten, Service-Daten für alle 22 Angebote,
Artikel-Daten für die drei Ratgeber sowie sichtbare und strukturierte
Brotkrumennavigation. Alle Leistungen haben sichtbare Einsatzgebiet-Inhalte
für Deutschland, Österreich, Schweiz und Kosovo. Die Startseiten lokalisieren
diese Aussage; die deutschsprachigen Unterseiten bleiben ausdrücklich als
solche gekennzeichnet. Die Sitemap enthält die 37 indexierbaren Seiten;
404 bleibt `noindex`. Der Prüflauf kontrolliert zusätzlich vollständige
Menüabdeckung, eindeutige Metadaten, Schema-Assets und Einsatzgebiete.
