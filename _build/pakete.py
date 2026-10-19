# -*- coding: utf-8 -*-
"""Weitere Festpreise: Pflege, Shop, Web-App, Firmenprofile, Preisrechner.

Die Beträge sind die vom Inhaber genannten Endpreise. Keine fremden Paketnamen.
"""
from bausteine import VER, cta_block, faq_block, hero_klein, karten_grid, kicker, seite_rahmen, wipe

END = "Endpreis. Gemäß § 19 UStG wird keine Umsatzsteuer berechnet."


def hinweis():
    return f'<p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">{END} <a href="impressum.html">Impressum</a></p>'


def website_pflege():
    inhalt = hero_klein(
        "01", "Website-Pflege",
        [["Website-Pflege"], ["im Monatsabo."]],
        "Updates, Backups und kleine Änderungen in drei Stufen. 99, 199 oder 299 € im Monat. Monatlich kündbar.",
        ["99 €", "199 €", "299 € im Monat"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Drei Stufen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Drei Stufen."], ["Klar getrennt."]])}</h2>
    {karten_grid([
        ("99 €", "Basis", "Updates, soweit ich Zugang habe. Einmal im Monat prüfe ich das Backup. Eine kleine Änderung im Monat: Text, Bild oder ein Kontaktfeld. Antwort innerhalb von fünf Werktagen. Kurze Monatsnotiz per E-Mail."),
        ("199 €", "Laufend", "Alles aus Basis. Bis zu vier kleine Änderungen im Monat. Antwort innerhalb von drei Werktagen. Monatlicher Bericht: erledigt, offen, nicht angefasst. Ich prüfe Startseite und Kontaktweg."),
        ("299 €", "Intensiv", "Alles aus Laufend. Bis zu acht kleine Änderungen im Monat. Eine davon ist ein neuer Abschnitt auf einer bestehenden Seite. Keine neue Website. Antwort innerhalb von zwei Werktagen. Monatsbericht und eine kurze Liste. Ich setze Ihre Texte ein. Pro Text bis zu einer Seite."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">Eine kleine Änderung ist ein Tausch von Text oder Bild oder eine Korrektur an einem bestehenden Element. Eine neue Website, ein Shop oder eine neue Funktion sind ein eigener Auftrag. Hosting zahlen Sie an Ihren Anbieter.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor dem"], ["Abo."]], [
        ("Kann ich monatlich kündigen?", "Ja. Die Kündigung gilt zum Ende des laufenden Monats. Es gibt keine Mindestlaufzeit."),
        ("Machen Sie das Hosting?", "Nein. Die Website bleibt bei Ihnen oder bei Ihrem Hoster. Ich arbeite mit den Zugängen, die Sie mir geben."),
        ("Ist die Seite dann rund um die Uhr betreut?", "Nein. Ich antworte an Werktagen in der Frist der Stufe. Es gibt keine Notfallbereitschaft."),
        ("Sichern Sie ein Ranking zu?", "Nein. Die Pflege hält Ihre Seite aktuell. Eine Platzierung verspreche ich nicht."),
    ]) + cta_block(
        "// nächster schritt", [["Welche Stufe"], ["passt?"]],
        "Schreiben Sie mir, welche Website es ist und welche Stufe Sie meinen. Die Schätzung im Preisrechner ist unverbindlich.",
        "Anfrage senden", "kontakt.html#anfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "website-pflege.html",
        "Website-Pflege im Monatsabo | Kastriot Tafolli",
        "Website-Pflege in drei Stufen: 99, 199 oder 299 € im Monat. Updates, Backups und kleine Änderungen, monatlich kündbar.",
        "website-pflege.html", inhalt)


def onlineshop():
    inhalt = hero_klein(
        "01", "Onlineshop",
        [["Onlineshop."], ["Ab 990 €."]],
        "Ein kleiner Shop: Einrichtung und eine Einweisung. Festpreis 990 oder 1.990 €. Hosting und Shop-Software laufen bei Ihnen oder beim Anbieter.",
        ["ab 990 €", "bis 1.990 €", "Einweisung"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Zwei Festpreise")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Einrichten."], ["Zeigen. Übergeben."]])}</h2>
    {karten_grid([
        ("990 €", "Start", "Kleiner Shop bei dem Anbieter, den wir vorher festlegen. Kategorien und Produkte aus einer Liste, die Sie liefern. Ein Zahlungsweg, den der Anbieter unterstützt. Versand nach Ihren Angaben. Eine Einweisung. Hosting und Software zahlen Sie an den Anbieter, nicht an mich."),
        ("1.990 €", "Erweitert", "Alles aus Start. Mehrere Kategorien. Mehr als ein Zahlungsweg, soweit der Anbieter das hergibt. Produktdaten aus einer Datei, die Sie liefern. Einweisung plus eine kurze schriftliche Übergabe."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">Nicht im Preis: Rechtstexte, Produktfotos, Bestellungen und Werbung. Umsätze kann ich nicht versprechen.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor dem"], ["Shop."]], [
        ("Liegt der Shop bei Ihnen?", "Nein. Konto, Hosting und Software bleiben bei Ihnen oder beim Anbieter. Ich richte ein und zeige Ihnen den Umgang."),
        ("Schreiben Sie die Rechtstexte?", "Nein. AGB, Widerruf und Datenschutz kommen von Ihnen oder von einer Stelle, die das darf. Ich baue sie nicht."),
        ("Was ist ein kleiner Shop?", "Ein überschaubares Sortiment, das Sie als Liste oder Datei liefern. Ein großes Warenwirtschaftssystem ist ein eigener Auftrag."),
        ("Ist 990 € der Endpreis?", "Ja, für die Stufe Start. Die Stufe Erweitert kostet 1.990 €. Beides sind Endpreise."),
    ]) + cta_block(
        "// nächster schritt", [["Welcher Shop"], ["soll entstehen?"]],
        "Schreiben Sie mir, wo der Shop liegen soll und wie viele Produkte Sie mitbringen. Die Schätzung im Preisrechner ist unverbindlich.",
        "Anfrage senden", "kontakt.html#anfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "onlineshop.html",
        "Onlineshop | Kastriot Tafolli",
        "Onlineshop einrichten und einweisen. Stufe Start 990 €, Stufe Erweitert 1.990 €. Hosting und Shop-Software laufen beim Kunden oder beim Anbieter.",
        "onlineshop.html", inhalt)


def web_apps():
    inhalt = hero_klein(
        "01", "Web-App",
        [["Ein Werkzeug."], ["Ab 390 €."]],
        "Eine kleine Web-App oder ein Tool nach Maß. Ein klarer Ablauf beginnt bei 390 €. Größere Projekte zum Festpreis, nachdem der Umfang feststeht.",
        ["ab 390 €", "ein Ablauf", "Festpreis nach Umfang"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Was dazugehört")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Klein starten."], ["Größer nur mit Preis."]])}</h2>
    {karten_grid([
        ("ab 390 €", "Kleines Werkzeug", "Ein Ablauf im Browser: zum Beispiel ein Rechner, eine Checkliste oder ein Formular, das etwas vorbereitet. Ohne Anbindung an ein großes Fremdsystem. Den Festpreis schreibe ich auf, bevor ich anfange. 390 € ist der Einstieg, wenn der Ablauf klein bleibt."),
        ("Angebot", "Größeres Projekt", "Mehrere Abläufe oder eine Anbindung an ein System, das Sie schon nutzen. Dafür nenne ich keinen Betrag auf dieser Seite. Sie bekommen ein Festpreis-Angebot, wenn Ablauf, Daten und Anbindung klar sind."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">KI-Automatisierung ist ein eigenes Angebot. Preis auf Anfrage. Eine App für den App-Store, Dauerbetrieb und Rechtsberatung gehören nicht dazu.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor dem"], ["Werkzeug."]], [
        ("Ist 390 € immer der Preis?", "Nein. 390 € ist der Einstieg für ein kleines Werkzeug. Sobald der Ablauf größer wird, nenne ich den Festpreis im Angebot, bevor die Arbeit beginnt."),
        ("Ist das die KI-Automatisierung?", "Nein. KI-Automatisierung ist ein eigenes Angebot. Preis auf Anfrage."),
        ("Speichert das Werkzeug Daten auf Ihrer Website?", "Nur, wenn wir das vorher so festlegen. Ein reiner Rechner im Browser speichert nichts. Steht eine Speicherung im Umfang, sage ich das vor dem Start."),
        ("Betreiben Sie das Werkzeug rund um die Uhr?", "Nein. Ich übergebe es und erkläre den Umgang. Eine Bereitschaft nachts oder am Wochenende ist kein Teil dieses Preises."),
    ]) + cta_block(
        "// nächster schritt", [["Welcher Ablauf"], ["soll es sein?"]],
        "Beschreiben Sie den einen Ablauf. Danach sage ich, ob er bei 390 € beginnt oder ein eigenes Festpreis-Angebot braucht.",
        "Anfrage senden", "kontakt.html#anfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "web-apps.html",
        "Web-App oder Tool nach Maß | Kastriot Tafolli",
        "Kleine Web-App oder ein Tool nach Maß ab 390 €. Ein Ablauf im Browser. Größere Projekte zum Festpreis nach Angebot.",
        "web-apps.html", inhalt)


def firmenprofile():
    inhalt = hero_klein(
        "01", "Firmenprofile",
        [["Firmenprofile"], ["im Netz."]],
        "Dieselben Angaben an den Stellen, die wir vorher festlegen. Basis 399 €, Komplett 899 €. Sie bestätigen das Google-Profil selbst.",
        ["399 €", "899 €", "einheitliche Angaben"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Basis bis Komplett")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Gleiche Daten."], ["Klare Liste."]])}</h2>
    {karten_grid([
        ("399 €", "Basis", "Sie liefern Name, Adresse, Telefon, Website, Öffnungszeiten und eine kurze Beschreibung. Ich lege das Google-Unternehmensprofil an oder gleiche es an. Google prüft das Profil mit Ihnen. Ohne echten Standort geht es nicht online. Dieselben Angaben in bis zu fünf Verzeichnissen."),
        ("899 €", "Komplett", "Alles aus Basis. Bis zu fünfzehn Verzeichnisse. Vorhandene Social-Profile auf denselben Namen, dieselbe Website und dieselbe Kurzbeschreibung bringen. Keine neuen Kanäle und keine laufenden Beiträge. Am Ende eine Liste der Profile. Die Zugänge bleiben bei Ihnen."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">Jedes Verzeichnis entscheidet selbst. Bewertungen, ein Ranking oder ein erfundener Standort gehören nicht dazu.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor den"], ["Profilen."]], [
        ("Geht das Google-Profil ohne mich online?", "Nein. Google prüft das Profil mit Ihnen. Ohne echten Standort geht es nicht online."),
        ("Legen Sie neue Social-Media-Kanäle an?", "Nein. In der Stufe Komplett gleiche ich Profile an, die Sie schon haben. Neue Kanäle und laufende Beiträge sind ein anderer Auftrag."),
        ("Warum 399 und 899 €?", "399 € deckt das Datenblatt, das Google-Profil und bis zu fünf Verzeichnisse. 899 € erweitert das auf bis zu fünfzehn Verzeichnisse, vorhandene Social-Profile und die Liste zur Übergabe."),
        ("Wer behält die Zugänge?", "Sie. Konten und Passwörter bleiben bei Ihnen."),
    ]) + cta_block(
        "// nächster schritt", [["Welche Profile"], ["fehlen?"]],
        "Schreiben Sie mir den Firmennamen und ob es schon ein Google-Profil gibt. Die Schätzung im Preisrechner ist unverbindlich.",
        "Anfrage senden", "kontakt.html#anfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "firmenprofile.html",
        "Firmenprofile im Netz einrichten | Kastriot Tafolli",
        "Google-Unternehmensprofil und Verzeichnisse mit einheitlichen Angaben. Festpreis 399 oder 899 €. Die Bestätigung bei Google machen Sie selbst.",
        "firmenprofile.html", inhalt)


def preisrechner():
    inhalt = hero_klein(
        "01", "Preisrechner",
        [["Unverbindliche"], ["Preisschätzung."]],
        "Wählen Sie eine Leistung. Der Rechner zeigt eine Spanne aus den veröffentlichten Preisen. Es ist kein Angebot.",
        ["im Browser", "keine Speicherung", "E-Mail auf Wunsch"],
    ) + f'''
<section class="pad" id="rechner">
  <div class="shell">
    {kicker("02", "Schätzen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Leistung wählen."], ["Spanne sehen."]])}</h2>
    <form id="preisrechner" class="anfrage-form preis-form">
      <fieldset>
        <legend>Leistung</legend>
        <label class="choice"><input type="radio" name="leistung" value="ki"> KI-Automatisierung</label>
        <label class="choice"><input type="radio" name="leistung" value="website" checked> Website oder Landingpage</label>
        <label class="choice"><input type="radio" name="leistung" value="shop"> Onlineshop</label>
        <label class="choice"><input type="radio" name="leistung" value="app"> Web-App oder Tool</label>
        <label class="choice"><input type="radio" name="leistung" value="pflege"> Website-Pflege im Monatsabo</label>
        <label class="choice"><input type="radio" name="leistung" value="profile"> Firmenprofile im Netz</label>
        <label class="choice"><input type="radio" name="leistung" value="texte"> Texte und Übersetzungen</label>
      </fieldset>
      <div data-panel="ki" hidden>
        <p>KI-Automatisierung ist ein eigenes Angebot. Preis auf Anfrage.</p>
      </div>
      <div data-panel="website">
        <p>Für eine neue Website oder Landingpage gibt es hier keinen Betrag. Den Festpreis nenne ich nach dem Umfang.</p>
        <label class="choice"><input type="checkbox" data-mit-pflege> Pflege-Abo in derselben Schätzung</label>
        <label>Pflege-Stufe
          <select data-pflege disabled>
            <option value="99">Basis, 99 € pro Monat</option>
            <option value="199">Laufend, 199 € pro Monat</option>
            <option value="299">Intensiv, 299 € pro Monat</option>
          </select>
        </label>
      </div>
      <div data-panel="shop" hidden>
        <fieldset>
          <legend>Shop-Stufe</legend>
          <label class="choice"><input type="radio" name="shop" value="start" checked> Start, 990 €</label>
          <label class="choice"><input type="radio" name="shop" value="erweitert"> Erweitert, 1.990 €</label>
        </fieldset>
      </div>
      <div data-panel="app" hidden>
        <fieldset>
          <legend>Umfang</legend>
          <label class="choice"><input type="radio" name="app" value="klein" checked> Kleines Werkzeug, ab 390 €</label>
          <label class="choice"><input type="radio" name="app" value="gross"> Größeres Projekt, Festpreis nach Angebot</label>
        </fieldset>
      </div>
      <div data-panel="pflege" hidden>
        <label>Pflege-Stufe
          <select data-pflege>
            <option value="99">Basis, 99 € pro Monat</option>
            <option value="199">Laufend, 199 € pro Monat</option>
            <option value="299">Intensiv, 299 € pro Monat</option>
          </select>
        </label>
      </div>
      <div data-panel="profile" hidden>
        <fieldset>
          <legend>Profil-Stufe</legend>
          <label class="choice"><input type="radio" name="profil" value="basis" checked> Basis, 399 €</label>
          <label class="choice"><input type="radio" name="profil" value="komplett"> Komplett, 899 €</label>
        </fieldset>
      </div>
      <div data-panel="texte" hidden>
        <fieldset>
          <legend>Textart</legend>
          <label class="choice"><input type="radio" name="text" value="dokument" checked> Dokument oder Prospekt, 49 €</label>
          <label class="choice"><input type="radio" name="text" value="website"> Website-Text, 59 €</label>
          <label class="choice"><input type="radio" name="text" value="content"> Content-Paket, 99 €</label>
          <label class="choice"><input type="checkbox" data-weitere> Weitere Sprache</label>
          <label class="choice"><input type="checkbox" data-eil> Eilauftrag, plus 30 %</label>
        </fieldset>
      </div>
      <p id="preis-ergebnis" aria-live="polite" aria-atomic="true"></p>
      <a class="btn btn-1" id="preis-mail" href="mailto:info@tafolli.net?subject=Preissch%C3%A4tzung%20von%20tafolli.net">Schätzung per E-Mail senden</a>
    </form>
    <noscript><p>Ohne JavaScript gibt es hier keine Schätzung. Die Preise stehen auf den Angebotsseiten.</p></noscript>
    <div class="portfolio-links">
      <a href="website-pflege.html">Website-Pflege <span aria-hidden="true">↗</span></a>
      <a href="onlineshop.html">Onlineshop <span aria-hidden="true">↗</span></a>
      <a href="web-apps.html">Web-App oder Tool <span aria-hidden="true">↗</span></a>
      <a href="firmenprofile.html">Firmenprofile <span aria-hidden="true">↗</span></a>
      <a href="angebot/">Texte und Übersetzungen <span aria-hidden="true">↗</span></a>
      <a href="landingpage-erstellen-lassen.html">Landingpage <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</section>
<script src="assets/preisrechner.js?v={VER}" defer></script>''' + cta_block(
        "// nächster schritt", [["Lieber direkt"], ["schreiben?"]],
        "Die Schätzung ersetzt kein Gespräch. Wenn der Umfang klarer ist, nenne ich den Festpreis.",
        "Anfrage senden", "kontakt.html#anfrage", "Alle Angebote", "leistungen.html")
    return seite_rahmen(
        "preisrechner.html",
        "Preisrechner | Kastriot Tafolli",
        "Unverbindliche Preisschätzung für KI, Website, Shop, Web-App, Pflege-Abo, Firmenprofile und Texte. Die Rechnung bleibt im Browser.",
        "preisrechner.html", inhalt)
