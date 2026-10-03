# tafolli.net

Persönliche Webseite von Kastriot Tafolli. F&B Manager in der 5-Sterne-Hotellerie,
Softwareingenieur mit Schwerpunkt Künstliche Intelligenz, Inhaber von TB Solutions.

Reines HTML, CSS und JavaScript. Kein Framework, keine Abhängigkeiten zur
Laufzeit, keine Anfrage an fremde Server. Die Dateien können so wie sie sind
auf jeden Webserver gelegt werden.

Alle Seiten werden aus `_build/` erzeugt:

    python3 _build/bau_alles.py

- `_build/bau.py` mit `inhalt_de.py`, `inhalt_en.py`, `inhalt_sq.py`:
  die Startseite auf Deutsch, Englisch und Albanisch (`/`, `/en/`, `/sq/`).
- `_build/bausteine.py`: Kopf- und Fusszeile sowie wiederverwendbare
  Abschnitte fuer alle Unterseiten.
- `_build/seiten_a.py` bis `seiten_d.py`: Inhalt und Aufbau der 16
  Unterseiten (Ueber mich, Werdegang, Leistungen, F&B-Beratung,
  Online-Marketing, TeamO, Rechner, Wissen mit drei Artikeln, Referenzen,
  Kontakt, Impressum, Datenschutz, 404).

Gestaltung und Bewegung liegen in `assets/kt.css`, das wenige JavaScript
(Menue, Terminal, Rechner, Zeiger) in `assets/kt.js`. Nach jeder Aenderung
an diesen beiden Dateien muss der Lauf wiederholt werden, weil ihre
Versionsmarke in allen Seiten steht.

Die Unterseiten sind derzeit nur auf Deutsch vorhanden.
