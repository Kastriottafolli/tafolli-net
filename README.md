# tafolli.net

Persönliche Webseite von Kastriot Tafolli. F&B Manager in der 5-Sterne-Hotellerie,
Softwareingenieur mit Schwerpunkt Künstliche Intelligenz, Inhaber von TB Solutions.

Sechzehn Seiten in reinem HTML, CSS und JavaScript. Kein Framework, keine
Abhängigkeiten, kein Bauschritt, keine Anfrage an fremde Server. Die Dateien
können so wie sie sind auf jeden Webserver gelegt werden.

## Inhalt

| Datei | Seite |
| --- | --- |
| `index.html` | Startseite |
| `ueber-mich.html` | Über mich |
| `werdegang.html` | Werdegang und Kompetenzen |
| `leistungen.html` | Leistungsübersicht |
| `fb-beratung.html` | F&B-Beratung im Detail |
| `online-marketing.html` | Online-Marketing und Webentwicklung |
| `teamo-ki.html` | TeamO, der digitale KI-Mitarbeiter |
| `rechner.html` | Vier Rechner, laufen im Browser |
| `wissen.html` | Übersicht der Fachartikel |
| `wissen-ki-im-hotel.html` | Artikel: KI im Hotel |
| `wissen-getraenkevertrag.html` | Artikel: Getränkevertrag |
| `wissen-direktbuchungen.html` | Artikel: Direktbuchungen |
| `referenzen.html` | Referenzen und Partner |
| `kontakt.html` | Kontakt |
| `impressum.html` | Impressum |
| `datenschutz.html` | Datenschutzerklärung |
| `404.html` | Fehlerseite |

```
assets/
  stil.css          gesamtes Aussehen
  schriften.css     Schrifteinbindung
  seite.js          Animationen, Terminal, Rechner
  favicon.svg       Browser-Symbol, das Monogramm
  schriften/        neun Schriftschnitte, 178 kB
  bilder/           Fotos, 584 kB
```

## Die Rechner

Auf `rechner.html` laufen vier Rechner vollständig im Browser des Besuchers.
Es werden keine Daten gespeichert und nichts an einen Server geschickt.

1. Personalkosten, die durch einen KI-Mitarbeiter frei werden
2. Portalprovision gegenüber Direktbuchung
3. Rückvergütung im Getränkeeinkauf
4. Reichweite und Anfragen über Social Media

Die Formeln stehen in `assets/seite.js` in der Funktion `render()`. Wer die
Annahmen ändern will, ändert sie dort. Die Übernahmequote der KI liegt bei
70 Prozent, die organische Reichweite je Beitrag bei 35 Prozent.

## Schriften liegen lokal

Bodoni Moda, IBM Plex Sans und JetBrains Mono liegen unter
`assets/schriften/` auf dem eigenen Server. Das hat zwei Gründe: Die Seite lädt
schneller, und es geht keine Anfrage an Google, bei der die IP-Adresse des
Besuchers in die Vereinigten Staaten übertragen würde. Genau dafür gab es in
Deutschland Abmahnungen.

Wer die Schriften austauscht, muss `assets/schriften.css` anpassen.

## Gestaltung

| Farbe | Wert |
| --- | --- |
| Messing | `#C6A15B` |
| Tinte | `#0C0B0A` |
| Panel | `#131110` |
| Papier | `#F1ECE2` |
| Elfenbein | `#F7F3EA` |
| Daten | `#7FD3B4` |

Das Logo im Kopfbereich und in der Fußzeile steckt als Vektorkurve direkt im
HTML. Es braucht weder Schriftdatei noch Bilddatei.

## Veröffentlichen

### GitHub Pages

Die Datei `CNAME` enthält bereits `tafolli.net`, der Ablauf unter
`.github/workflows/pages.yml` veröffentlicht bei jedem Push automatisch.

1. Repository auf GitHub anlegen, diese Dateien hochladen.
2. Unter Settings, Pages als Quelle **GitHub Actions** wählen.
3. Beim Domainanbieter diese Einträge setzen:

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  <benutzername>.github.io
```

4. In den Pages-Einstellungen `tafolli.net` als Custom Domain eintragen und
   danach "Enforce HTTPS" aktivieren.

### Anderer Webserver

Alle Dateien in das Web-Verzeichnis kopieren, zum Beispiel per FTP nach
`public_html`. Mehr ist nicht nötig, es gibt keinen Bauschritt.

## Noch zu erledigen

- [ ] Postfach `info@tafolli.net` beim Anbieter einrichten
- [ ] Im Impressum die Angabe zur Umsatzsteuer vervollständigen
- [ ] Impressum und Datenschutzerklärung anwaltlich prüfen lassen
- [ ] Logos der Getränkepartner einsetzen, sobald die Dateien vorliegen
- [ ] Google Search Console einrichten und `sitemap.xml` einreichen

## Hinweis zu den Partnerlogos

Auf `referenzen.html` stehen die Getränke- und Gastronomiepartner als Text,
weil für diese Marken keine frei verwendbaren Logodateien vorlagen. Die
Technologiepartner tragen Logos aus quelloffenen Sammlungen. Marken gehören
ihren Inhabern, die Nennung erfolgt als Hinweis auf bestehende
Geschäftsbeziehungen.

## Hinweis zu den Rechtstexten

`impressum.html` und `datenschutz.html` sind sorgfältig erstellt und
beschreiben den tatsächlichen technischen Stand dieser Seite, ersetzen aber
keine Rechtsberatung. Sobald etwas hinzukommt, das Daten erhebt, etwa ein
Kontaktformular, ein Newsletter oder eine Kartendarstellung, muss die
Datenschutzerklärung ergänzt werden.
