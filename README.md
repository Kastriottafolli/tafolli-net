# Tafolli & Co. · tafolli.net

Lokaler Unternehmensauftritt mit vier gleichwertigen Bereichen: Marketing, Technology, Consulting und AI Automation. Die Domain und alle bestehenden Seitenadressen bleiben erhalten. Hotellerie und Gastronomie sind eine besondere Kompetenz; die Leistungen für Technologie und Marketing sprechen Unternehmen branchenübergreifend an.

Stand 25. Oktober 2026: Der Unternehmensauftritt ist auf allen 38 Seiten überarbeitet. Die drei Startseiten verwenden eine neue, an Apple angelehnte Unternehmensgestaltung mit einer pausierbaren CSS-3D-Szene und gezielten Einblendungen. Die Darstellung berücksichtigt reduzierte Bewegung und enthält weiterhin keine blockierende Startanimation. Marketing umfasst Strategie, Marke, Inhalte, Kampagnen und digitale sowie gedruckte Materialien. Technology umfasst individuelle Software, Web-Apps, iOS-/Android-Apps, Schnittstellen und Cybersecurity. Der über Runway erzeugte Logoentwurf entwickelt das vorhandene Gehirnsymbol mit Codeklammern und einem orangefarbenen Impulspunkt weiter. Er ist lokal in Kopfzeilen, im Einstieg der Startseiten, in Icons und der Linkvorschau eingebaut und steht zur Beurteilung durch den Inhaber bereit. Anbieterangaben der bereits gegründeten Kosovo-Gesellschaft müssen vor Veröffentlichung ergänzt werden; Impressum und Datenschutzerklärung enthalten die bisherige Bestandsfassung.

Gestaltungsauftrag, Dateien, Prüfungen und offene Angaben: `../artifacts/tafolli-co/gestaltung-und-uebergabe.md`. Der verwendete Runway-Auftrag liegt daneben als JSON. Die Erzeugung erfolgte im angemeldeten Runway-Browser, da die Plugin-Verbindung weiterhin eine gesonderte erneute Autorisierung verlangte.

## Aufbau

Statische HTML-, CSS- und JavaScript-Dateien, ohne Framework oder externe Laufzeitabhängigkeiten. Alle Schriftarten und Grafiken werden lokal geladen. Die Startseiten sind Deutsch, Englisch und Albanisch; die Unterseiten sind auf Deutsch.

Die HTML-Seiten werden aus `_build/` erzeugt. Änderungen an Inhalten dort pflegen und anschließend neu bauen, statt nur die erzeugten Dateien zu ändern.

- `company_home.py`, `company_content.py`: neue Unternehmensstartseiten auf Deutsch, Englisch und Albanisch; vier Leistungsbereiche, eigene Vektorillustrationen, Referenz-Websites, Projektablauf, FAQs und Kontakt. `apple_content.py` und `content_refresh.py` ergänzen die Präsentationstexte, konkrete Anwendungsfälle, Leistungslinks und FAQs in drei Sprachen. Die Inhalte und Links stehen vollständig im HTML; Navigation und Bewegung werden mit JavaScript ergänzt.
- `experience.py`, `experience_content.py`, `inhalt_de.py`, `inhalt_en.py`, `inhalt_sq.py`: Erzeugung und Inhalte der vertieften Automation-Seite; ruft für die drei Startseiten die neue Unternehmensvorlage auf. Die interaktive Demo und der Zeitwert-Rechner bleiben auf der Automation-Seite.
- `seiten_a.py` bis `seiten_d.py`: Unternehmensseite unter dem bestehenden URL `ueber-mich.html`, persönlicher Werdegang, Leistungsübersicht, Ratgeber, Referenzen, Kontakt und Rechtliches.
- `services.py`: vertiefte Leistungsseiten und der gemeinsame Leistungskatalog mit 22 Angeboten.
- `brand.py`: gemeinsame Wortmarke und Symbolpfad. Die frühere Startanimation wird nicht mehr eingebunden. Das aktive Symbol ist `assets/brand/tafolli-co-neural-code.webp`. Das bisherige Gehirnsymbol bleibt als `assets/brand/logo-mark.webp` erhalten; der abgelehnte T-Entwurf ist außerhalb der Website unter `../artifacts/tafolli-co/rejected-t-monogram/` archiviert.
- `bausteine.py`, `navigation.py`, `seo.py`: gemeinsamer Seitenrahmen, vollständige Navigation, Metadaten, strukturierte Daten und Einsatzgebiete.
- `partners.py`, `companies.py`, `hotels.py`: eingeordnete Projekte, Anbieterlinks und persönliche Hotelstationen des Gründers. Quellen der lokalen Partnergrafiken: `assets/partners/sources.json`.
- `artwork.py`, `icons.py`, `portrait.py`, `boost.py`, `explore.py`: dekorative Grafik, SVG-Bedienelemente, Gründerporträt, Tafolli-Boost-Verweis und verwandte Inhalte.
- `assets/company.css`: zentrierte Unternehmensstartseiten, Systemtypografie, große Bildflächen, blaue Schaltflächen und vier Leistungsbereiche in zwei Spalten, auf kleinen Bildschirmen untereinander.
- `showcase.py`: reproduzierbare eigene SVG-Illustrationen in `assets/showcase/`. Oberflächen und Geräte sind als Gestaltungsbeispiel gekennzeichnet; sie behaupten keine realen Kunden- oder Leistungsdaten.
- `assets/corporate.css`: gemeinsame Unternehmensgestaltung, Navigation und ruhigere Darstellung aller bestehenden Unterseiten.
- `assets/experience.css`, `assets/kt.css`: erhaltene Basisbausteine; neue Unternehmensgestaltung wird anschließend geladen.
- `assets/experience.js`: ausschließlich Workflow-Demo und Zeitwert-Rechner, ohne dekorative Animation. `assets/kt.js` erhält bestehende Rechner. `assets/navigation.js` steuert die gemeinsame Tastatur- und Mobilnavigation. `partners.js` steuert die beiden bewegten Referenzreihen. Die ältere Datei `brand.js` wird nicht geladen. `assets/motion.css` und `assets/motion.js` steuern die räumliche Szene, die Pausenfunktion und gezielte Einblendungen.
- `_build/social-preview.html`: Vorlage für die 1200 × 630 Pixel große Linkvorschau in `assets/social-preview.png`. Bei einem späteren Logowechsel ebenfalls aktualisieren und neu aufnehmen.
- `_build/logo-export.html`: lokale Exportvorlage für Symbol und exakt gesetzten Schriftzug; keine öffentliche Seite. Die fertigen PNG-Dateien liegen unter `../artifacts/tafolli-co/`.

## Bauen und prüfen

Im Ordner `website/` ausführen:

```sh
python3 _build/bau_alles.py
python3 _build/verify.py
node --check assets/experience.js
node --check assets/partners.js
node --check assets/brand.js
node --check assets/navigation.js
node --check assets/kt.js
```

Der bestehende Prüflauf kontrolliert alle 38 Seiten: lokale Links und Anker, Dateien, individuelle Titel und Beschreibungen, Sprachkonfiguration, vollständige Menüabdeckung, strukturierte Daten, SVG-Symbole und Sitemap.

Für eine lokale Vorschau:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Dann `http://127.0.0.1:8765/` öffnen. Es wurde nichts veröffentlicht oder auf einen Hostingserver übertragen.

## Interaktionen und inhaltliche Grenzen

Die KI-Demo arbeitet mit fiktiven Beispieldaten und versendet nichts. Der Zeitwert-Rechner nutzt 22 Arbeitstage pro Monat und zeigt einen rechnerischen Zeitwert vor Servicekosten, keine garantierte Einsparung. Werte werden erst über den angeklickten Kontaktlink ins eigene E-Mail-Programm übernommen.

Die Unternehmensstartseiten ergänzen statische Inhalte um eine pausierbare CSS-3D-Szene. Es gibt keine blockierende Startanimation. Tastaturbedienung und eine Bedienung ohne JavaScript werden berücksichtigt. Die Workflow-Demo auf der Automation-Seite berücksichtigt `prefers-reduced-motion`. Es gibt keine Tracker oder externen Schriftabrufe. Die Boosty-Einstellungen werden für die Browsersitzung lokal gespeichert. Eine Beratungsanfrage übermittelt erst beim Absenden die Kontaktdaten und ausgewählte Planung über FormSubmit.

Die persönlichen Berufsstationen und Kennzahlen gehören ausdrücklich zum Gründerprofil. Sie bezeichnen keine Teamgröße der Firma. Es wurden keine Mitarbeiterprofile, internationalen Büros, Registerdaten oder Rechtsformen ergänzt.

## Inhalt, SEO und 3D

Die aktuelle Prüfung und der maschinenlesbare SEO-Seitenbericht liegen unter `../artifacts/tafolli-co/seo-und-animationen.md` und `../artifacts/tafolli-co/seo-pruefung.json`. `motion.css` und `motion.js` sind lokal, ohne externe Bibliotheken. Ohne JavaScript bleiben Inhalte und Navigation erreichbar; bei reduzierter Bewegung startet die Szene ruhig.

## Budgetplaner und SEO-Feinschliff · 26. Oktober 2026

Der lange Leistungskatalog unter Tafolli Boost wurde durch den Budgetplaner ersetzt. `planner.py` erzeugt die Oberfläche in DE, EN und SQ. `assets/planner-model.mjs` enthält das transparente Szenariomodell; `planner.js` steuert Eingaben, Skalierungskurve, Textexport und Beratungsanfrage. Die Zahlen sind veränderbare Beispielbudgets und Annahmen, keine Preisliste oder Prognose. Der Berechnungstest läuft mit `node --test _build/test_planner.mjs`.

Anfragen gehen über die bestätigte FormSubmit-Formularadresse an `info@tafolli.net`. Die Aktivierungen für `https://tafolli.net/` und die lokale Vorschau `http://127.0.0.1:8765/` wurden im Geschäftspostfach geprüft und auf den Anbieter-Seiten jeweils mit „Form Activated“ bestätigt. Am 26.10.2026 wurde die Testanfrage `BP-261026-A` direkt aus dem Budgetplaner erfolgreich gesendet und im Posteingang einschließlich vollständiger Planung, Budgets, Annahmen und Ergebnisse geprüft. Empfänger und Reply-To wurden ebenfalls geprüft. Die Anbindung ist in allen drei Sprachversionen hinterlegt; die Website ist weiterhin nur lokal geändert. Keine API-Schlüssel oder Postfachzugänge stehen im Frontend.

`seo_content.py` ergänzt die vertieften Texte und Kaufentscheidungsfragen für Website-Erstellung, Social-Media-Betreuung und SEO. `search_faq.py` enthält die Startseitenfragen in drei Sprachen. `seo.write_sitemap()` schreibt die tatsächlichen kanonischen Seiten einschließlich Sprachalternativen und dokumentierter Inhaltsdaten. Diese Daten werden bei zukünftigen Inhaltsänderungen bewusst gepflegt, nicht bei jedem Build auf das Tagesdatum gesetzt.
