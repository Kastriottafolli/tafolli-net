# Tafolli & Co. · tafolli.net

Lokaler Unternehmensauftritt mit vier gleichwertigen Bereichen: Marketing, Technology, Consulting und AI Automation. Die Domain und alle bestehenden Seitenadressen bleiben erhalten. Hotellerie und Gastronomie sind eine besondere Kompetenz; die Leistungen für Technologie und Marketing sprechen Unternehmen branchenübergreifend an.

Stand 27. Oktober 2026: Der Unternehmensauftritt umfasst 53 Seiten einschließlich der erhaltenen Angebots- und Zielgruppenseiten. Die drei Startseiten verwenden eine neue, an Apple angelehnte Unternehmensgestaltung mit einer pausierbaren CSS-3D-Szene und gezielten Einblendungen. Die Darstellung berücksichtigt reduzierte Bewegung. Eine kurze, sofort überspringbare Logoanimation begleitet Seitenaufrufe und interne Seitenwechsel. Marketing umfasst Strategie, Marke, Inhalte, Kampagnen und digitale sowie gedruckte Materialien. Technology umfasst individuelle Software, Web-Apps, iOS-/Android-Apps, Schnittstellen und Cybersecurity. Der über Runway erzeugte Logoentwurf entwickelt das vorhandene Gehirnsymbol mit Codeklammern und einem orangefarbenen Impulspunkt weiter. Er ist lokal in Kopfzeilen, im Einstieg der Startseiten, in Icons und der Linkvorschau eingebaut und ist mit dem abgestimmten Unternehmensauftritt verbunden. Impressum und Datenschutzerklärung enthalten die bisherige deutsche Anbieteridentität. Konkrete Angaben zur genannten Kosovo-Gesellschaft wurden nicht geliefert und nicht ergänzt.

Gestaltungsauftrag, Dateien, Prüfungen und offene Angaben: `../artifacts/tafolli-co/gestaltung-und-uebergabe.md`. Der verwendete Runway-Auftrag liegt daneben als JSON. Die Erzeugung erfolgte im angemeldeten Runway-Browser, da die Plugin-Verbindung weiterhin eine gesonderte erneute Autorisierung verlangte.

## Aufbau

Statische HTML-, CSS- und JavaScript-Dateien, ohne Framework oder externe Laufzeitabhängigkeiten. Alle Schriftarten und Grafiken werden lokal geladen. Die Startseiten sind Deutsch, Englisch und Albanisch; die Unterseiten sind auf Deutsch.

Die HTML-Seiten werden aus `_build/` erzeugt. Änderungen an Inhalten dort pflegen und anschließend neu bauen, statt nur die erzeugten Dateien zu ändern.

- `company_home.py`, `company_content.py`: neue Unternehmensstartseiten auf Deutsch, Englisch und Albanisch; vier Leistungsbereiche, eigene Vektorillustrationen, Referenz-Websites, Projektablauf, FAQs und Kontakt. `apple_content.py` und `content_refresh.py` ergänzen die Präsentationstexte, konkrete Anwendungsfälle, Leistungslinks und FAQs in drei Sprachen. Die Inhalte und Links stehen vollständig im HTML; Navigation und Bewegung werden mit JavaScript ergänzt.
- `experience.py`, `experience_content.py`, `inhalt_de.py`, `inhalt_en.py`, `inhalt_sq.py`: Erzeugung und Inhalte der vertieften Automation-Seite; ruft für die drei Startseiten die neue Unternehmensvorlage auf. Die interaktive Demo und der Zeitwert-Rechner bleiben auf der Automation-Seite.
- `seiten_a.py` bis `seiten_d.py`: Unternehmensseite unter dem bestehenden URL `ueber-mich.html`, persönlicher Werdegang, Leistungsübersicht, Ratgeber, Referenzen, Kontakt und Rechtliches.
- `services.py`: vertiefte Leistungsseiten und der gemeinsame Leistungskatalog mit 22 Angeboten.
- `brand.py`: gemeinsame Wortmarke und Symbolpfad. Die frühere Logoanimation wird über `loading.py` in den aktuellen Farben wieder auf allen Seiten eingebunden. Das aktive Symbol ist `assets/brand/tafolli-co-neural-code.webp`. Das bisherige Gehirnsymbol bleibt als `assets/brand/logo-mark.webp` erhalten; der abgelehnte T-Entwurf ist außerhalb der Website unter `../artifacts/tafolli-co/rejected-t-monogram/` archiviert.
- `bausteine.py`, `navigation.py`, `seo.py`: gemeinsamer Seitenrahmen, vollständige Navigation, Metadaten, strukturierte Daten und Einsatzgebiete.
- `partners.py`, `companies.py`, `hotels.py`: eingeordnete Projekte, Anbieterlinks und persönliche Hotelstationen des Gründers. Quellen der lokalen Partnergrafiken: `assets/partners/sources.json`.
- `artwork.py`, `icons.py`, `portrait.py`, `boost.py`, `explore.py`: dekorative Grafik, SVG-Bedienelemente, Gründerporträt, Tafolli-Boost-Verweis und verwandte Inhalte.
- `assets/company.css`: zentrierte Unternehmensstartseiten, Systemtypografie, große Bildflächen, blaue Schaltflächen und vier Leistungsbereiche in zwei Spalten, auf kleinen Bildschirmen untereinander.
- `showcase.py`: reproduzierbare eigene SVG-Illustrationen in `assets/showcase/`. Oberflächen und Geräte sind als Gestaltungsbeispiel gekennzeichnet; sie behaupten keine realen Kunden- oder Leistungsdaten.
- `assets/corporate.css`: gemeinsame Unternehmensgestaltung, Navigation und ruhigere Darstellung aller bestehenden Unterseiten.
- `assets/experience.css`, `assets/kt.css`: erhaltene Basisbausteine; neue Unternehmensgestaltung wird anschließend geladen.
- `assets/experience.js`: ausschließlich Workflow-Demo und Zeitwert-Rechner, ohne dekorative Animation. `assets/kt.js` erhält bestehende Rechner. `assets/navigation.js` steuert die gemeinsame Tastatur- und Mobilnavigation. `partners.js` steuert die beiden bewegten Referenzreihen. `assets/brand.js` und `assets/brand-loader.css` steuern die kurze Logoanimation beim Seitenaufruf und bei internen Seitenwechseln. `assets/motion.css` und `assets/motion.js` steuern die räumliche Szene, die Pausenfunktion und gezielte Einblendungen.
- `_build/social-preview.html`: Vorlage für die 1200 × 630 Pixel große Linkvorschau in `assets/social-preview.png`. Bei einem späteren Logowechsel ebenfalls aktualisieren und neu aufnehmen.
- `_build/logo-export.html`: lokale Exportvorlage für Symbol und exakt gesetzten Schriftzug; keine öffentliche Seite. Die fertigen PNG-Dateien liegen unter `../artifacts/tafolli-co/`.

## Bauen und prüfen

Im Ordner `website/` ausführen:

```sh
python3 _build/check.py
```

Der bestehende Prüflauf kontrolliert alle 53 Seiten: lokale Links und Anker, Dateien, individuelle Titel und Beschreibungen, Sprachkonfiguration, vollständige Menüabdeckung, strukturierte Daten, SVG-Symbole und Sitemap.

Für eine lokale Vorschau:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Dann `http://127.0.0.1:8765/` öffnen. Die lokale Vorschau ist unabhängig von der Veröffentlichung über den GitHub-Pages-Workflow auf `main`.

## Interaktionen und inhaltliche Grenzen

Die KI-Demo arbeitet mit fiktiven Beispieldaten und versendet nichts. Der Zeitwert-Rechner nutzt 22 Arbeitstage pro Monat und zeigt einen rechnerischen Zeitwert vor Servicekosten, keine garantierte Einsparung. Werte werden erst über den angeklickten Kontaktlink ins eigene E-Mail-Programm übernommen.

Die Unternehmensstartseiten ergänzen statische Inhalte um eine pausierbare CSS-3D-Szene. Die kurze Logoanimation lässt sich mit Klick, Tastendruck oder Scrollen sofort überspringen; unabhängige Zeitgrenzen verhindern eine hängenbleibende Abdeckung. Tastaturbedienung und eine Bedienung ohne JavaScript werden berücksichtigt. Die Workflow-Demo auf der Automation-Seite berücksichtigt `prefers-reduced-motion`. Es gibt keine Tracker oder externen Schriftabrufe. Die Boosty-Einstellungen werden für die Browsersitzung lokal gespeichert. Eine Beratungsanfrage übermittelt erst beim Absenden die Kontaktdaten und ausgewählte Planung über FormSubmit.

Die persönlichen Berufsstationen und Kennzahlen gehören ausdrücklich zum Gründerprofil. Sie bezeichnen keine Teamgröße der Firma. Es wurden keine Mitarbeiterprofile, internationalen Büros, Registerdaten oder Rechtsformen ergänzt.

## Inhalt, SEO und 3D

Die aktuelle Prüfung und der maschinenlesbare SEO-Seitenbericht liegen unter `../artifacts/tafolli-co/seo-und-animationen.md` und `../artifacts/tafolli-co/seo-pruefung.json`. `motion.css` und `motion.js` sind lokal, ohne externe Bibliotheken. Ohne JavaScript bleiben Inhalte und Navigation erreichbar; bei reduzierter Bewegung startet die Szene ruhig.

## Budgetplaner und SEO-Feinschliff · 26. Oktober 2026

Der lange Leistungskatalog unter Tafolli Boost wurde durch den Budgetplaner ersetzt. `planner.py` erzeugt die Oberfläche in DE, EN und SQ. `assets/planner-model.mjs` enthält das transparente Szenariomodell; `planner.js` steuert Eingaben, Skalierungskurve, Textexport und Beratungsanfrage. Die Zahlen sind veränderbare Beispielbudgets und Annahmen, keine Preisliste oder Prognose. Der Berechnungstest läuft mit `node --test _build/test_planner.mjs`.

Anfragen gehen über die bestätigte FormSubmit-Formularadresse an `info@tafolli.net`. Die Aktivierungen für `https://tafolli.net/` und die lokale Vorschau `http://127.0.0.1:8765/` wurden im Geschäftspostfach geprüft und auf den Anbieter-Seiten jeweils mit „Form Activated“ bestätigt. Am 26.10.2026 wurde die Testanfrage `BP-261026-A` direkt aus dem Budgetplaner erfolgreich gesendet und im Posteingang einschließlich vollständiger Planung, Budgets, Annahmen und Ergebnisse geprüft. Empfänger und Reply-To wurden ebenfalls geprüft. Die Anbindung ist in allen drei Sprachversionen hinterlegt; die Website ist weiterhin nur lokal geändert. Keine API-Schlüssel oder Postfachzugänge stehen im Frontend.

`seo_content.py` ergänzt die vertieften Texte und Kaufentscheidungsfragen für Website-Erstellung, Social-Media-Betreuung und SEO. `search_faq.py` enthält die Startseitenfragen in drei Sprachen. `seo.write_sitemap()` schreibt die tatsächlichen kanonischen Seiten einschließlich Sprachalternativen und dokumentierter Inhaltsdaten. Diese Daten werden bei zukünftigen Inhaltsänderungen bewusst gepflegt, nicht bei jedem Build auf das Tagesdatum gesetzt.

## Abschließende Integration und Übergabe · 26. Oktober 2026

Die fünf neueren Änderungen aus `origin/main` wurden in den Unternehmensauftritt integriert. Die zusätzlichen 15 Angebots- und Zielgruppenseiten behalten ihre Adressen; vorhandene Preise wurden übernommen. Der neue Budgetplaner verwendet weiterhin ausdrücklich veränderbare Beispielbudgets. Bereits aus dem öffentlichen Profil entfernte Hotelstationen wurden nicht wieder eingefügt. FAQ-Daten werden gegen die tatsächlichen Seiteninhalte geprüft; Sprachalternativen sind wechselseitig verlinkt.

Das allgemeine Kontaktformular sendet jetzt ebenfalls direkt an info@tafolli.net. `delivery.py` enthält die gemeinsame bestätigte öffentliche Formularadresse. `assets/form-delivery.mjs` verarbeitet Versand, Fehler und Zeitüberschreitungen; `contact.js` übernimmt Themenvorbelegung, Kontaktformular und E-Mail-Alternative. Der reale Kontakttest `KT-261026-B` ist im Posteingang mit Thema, Zeitraum, Nachricht und korrekter Antwortadresse bestätigt. Sechs zusätzliche Transporttests prüfen Erfolgs- und Fehlerfälle, ohne echte Nachrichten zu senden.

`check.py` baut alle Seiten, prüft alle 53 Seiten und die JavaScript-Syntax und führt die 15 Modell- und Versandtests aus. Die GitHub-Workflows verwenden dieselben Prüfungen vor dem Veröffentlichen. `release.py` erzeugt aus den HTML-Seiten und ihren tatsächlich benötigten lokalen Abhängigkeiten ein sauberes Veröffentlichungspaket. Interne Vorlagen, Bauprogramme, Dokumentation und unbenutzte Kundenscreenshots werden nicht ausgeliefert.

```sh
python3 _build/release.py --output _site --archive ../tafolli-net.zip
```

Das Zielverzeichnis darf noch nicht existieren. Das zugehörige Manifest enthält Dateigrößen und SHA-256-Prüfsummen. `.nojekyll` und die unveränderte Domainkonfiguration sind enthalten.

Die Texte zur Anbieteridentität enthalten weiter die bisherigen deutschen Gewerbeangaben. Für die neue Kosovo-Gesellschaft fehlen die vom Inhaber angekündigten konkreten Gesellschaftsdaten. Deshalb wird die neue Fassung als fertige Vorschau und Änderungsvorschlag übergeben und nicht ungeprüft nach `main` veröffentlicht. Es wurden keine Rechtsform, Registerdaten, Steuerdaten, Mitarbeiter oder Büros erfunden.

## Individuelle Unterseiten · 27. Oktober 2026

Alle 41 Ziele der Menüs Leistungen und Unternehmen verwenden die Bildsprache der Startseite. Kontakt und Wissen sind ebenfalls einbezogen: insgesamt 47 gestaltete Unterseiten. Startseiten, bestätigte Richtpreise, vorhandene Formulare und Referenzziele bleiben erhalten.

- `_build/detail_catalog.py` enthält Seiteneinstiege, Motive, Themen und die beschrifteten Prozessschritte. Jede Seite hat eine eigene Überschrift und einen fachlichen Schwerpunkt.
- `_build/detail_art.py` erzeugt eigene CSS-/SVG-Konzepte: Browser, mobile Geräte, lokale Karte, Markenmaterial, Kamera, Infrastruktur, Sicherheitsmodell, Wissensquellen, Einkauf, Kalkulation, Warenbestand und Unternehmensgeschichte. Tatsächliche Bilder werden nur für das eigene Produkt und das vorhandene Gründerporträt verwendet.
- `_build/detail_design.py` führt die Gestaltung als letzten Schritt des vollständigen Seitenbaus aus. Bestehende Abschnitte und Anker bleiben erreichbar. Die ursprünglichen Leistungsbausteine werden bei den Fachseiten in bedienbare Register umgewandelt; die Inhalte bleiben im HTML.
- `assets/detail.css` kapselt Farben, Abstände, Szenen und Zustände unter `.detail-page`. `assets/detail.js` steuert die Konzeptansichten, Register, Kapitelnavigation und dezente Einblendungen, ohne Netzwerkaufrufe oder Tracking.

Register verwenden `tablist`, `tab`, `tabpanel` und wechselseitige ARIA-Verweise. Pfeiltasten, Home und End wechseln das Register. Ohne JavaScript sind alle Inhalte sichtbar. Die Animationssteuerung verwendet denselben globalen Bewegungszustand wie die Startseite; reduzierte Bewegung, ein verborgenes Dokument und Szenen außerhalb des sichtbaren Bereichs pausieren die Darstellung. Technische Konzeptgrafiken sind als Illustrationen gekennzeichnet und dekorativ für assistive Technik ausgeblendet.

`_build/check_detail.py` kontrolliert Menüabdeckung, eindeutige Seiteneinstiege, Szenensteuerung und die Registerbeziehungen. Der reguläre Prüflauf schließt diese Kontrolle ein. Das Veröffentlichungsarchiv übernimmt nur die benötigten öffentlichen Dateien.

## Ladebildschirm · 27. Oktober 2026

`loading.py` ergänzt alle 53 Dokumente einschließlich EN, SQ und verschachtelter Angebotsseiten. Das vorhandene Gehirnsymbol setzt sich aus zwei Hälften zusammen, die Verbindungslinien zeichnen sich und das Symbol wandert in die gemeinsame Kopfzeile. Hintergrund, Systemtypografie, Blau und orangefarbener Impuls entsprechen der aktuellen Gestaltung.

`brand.js` wird früh im Kopf geladen, damit der Bildschirm vor dem Seiteninhalt erscheint. Die normale Animation endet nach etwa einer Sekunde. Native Links, Browsernavigation und Formulare werden nicht umgeleitet oder verzögert. Ankersprünge innerhalb derselben Seite, externe Links, Downloads und neue Tabs lösen keine ausgehende Abdeckung aus. Zurück-/Vorwärts-Wiederherstellung wird ebenfalls behandelt. Der Loader bleibt ohne JavaScript verborgen, berücksichtigt reduzierte Bewegung sowie die Animationspause und benötigt weder Speicherzugriff noch externe Verbindungen. JavaScript- und CSS-Zeitgrenzen sowie Nutzereingaben räumen die Abdeckung unabhängig auf.

## Veröffentlichung · 27. Oktober 2026

Der Inhaber hat die Veröffentlichung der Vorschaufassung freigegeben. PR 8 wurde als `d87a2cb6575bfb6ac9c09612878ee45fa067c253` zusammengeführt; die automatische Prüfung und der Pages-Workflow sind erfolgreich. HTTPS wird für `tafolli.net` erzwungen. Die vorhandenen deutschen Anbieterangaben bleiben erhalten. Frühere Hinweise in dieser Dokumentation beschreiben den damaligen Entwurfsstand.

Die Fehlerseite verwendet für den gemeinsamen Loader absolute Assetpfade. Damit werden Logo, Stylesheet und Skript auch bei verschachtelten unbekannten Seitenadressen von der Domainwurzel geladen.
