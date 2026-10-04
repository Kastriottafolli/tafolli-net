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
    node --check assets/kt.js

Die Prüfung kontrolliert alle erzeugten Seiten, lokale Links und Anker,
Assets, Metadaten, übersetzte Demo-Daten und den Sitemap-Eintrag. Ein
GitHub-Actions-Check baut die Seiten bei Pull Requests neu und prüft,
dass die eingecheckten Dateien dem Ergebnis entsprechen.
