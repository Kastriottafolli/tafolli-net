# -*- coding: utf-8 -*-
"""Weitere Festpreise: Pflege, Shop, Web-App, Firmenprofile, Preisrechner.

Die Beträge sind die vom Inhaber genannten Endpreise. Keine fremden Paketnamen.
"""
import html
from bausteine import VER, cta_block, faq_block, hero_klein, karten_grid, kicker, seite_rahmen, wipe

END = "Endpreis. Gemäß § 19 UStG wird keine Umsatzsteuer berechnet."


def hinweis():
    return f'<p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">{END} <a href="impressum.html">Impressum</a></p>'


def dazu(links):
    items = ''.join(
        f'<a href="{href}">{html.escape(label)} <span aria-hidden="true">↗</span></a>'
        for href, label in links)
    return (
        '<section class="pad"><div class="shell"><p class="tag">Das passt dazu</p>'
        '<h2 class="d2" style="margin:14px 0 22px">Weiter auf tafolli.net</h2>'
        f'<div class="portfolio-links">{items}</div></div></section>')


def website_pflege():
    fragen = [
        ("Kann ich monatlich kündigen?", "Ja. Die Kündigung gilt zum Ende des laufenden Monats. Es gibt keine Mindestlaufzeit."),
        ("Machen Sie das Hosting?", "Nein. Die Website bleibt bei Ihnen oder bei Ihrem Hoster. Wir arbeiten mit den Zugängen, die Sie uns geben."),
        ("Ist die Seite dann rund um die Uhr betreut?", "Nein. Wir antworten an Werktagen in der Frist der Stufe. Es gibt keine Notfallbereitschaft."),
        ("Sichern Sie ein Ranking zu?", "Nein. Die Pflege hält Ihre Seite aktuell. Eine Platzierung versprechen wir nicht."),
    ]
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
        ("99 €", "Basis", "Updates, soweit wir Zugang haben. Einmal im Monat prüfen wir das Backup. Eine kleine Änderung im Monat: Text, Bild oder ein Kontaktfeld. Antwort innerhalb von fünf Werktagen. Kurze Monatsnotiz per E-Mail."),
        ("199 €", "Laufend", "Alles aus Basis. Bis zu vier kleine Änderungen im Monat. Antwort innerhalb von drei Werktagen. Monatlicher Bericht: erledigt, offen, nicht angefasst. Wir prüfen Startseite und Kontaktweg."),
        ("299 €", "Intensiv", "Alles aus Laufend. Bis zu acht kleine Änderungen im Monat. Eine davon ist ein neuer Abschnitt auf einer bestehenden Seite. Keine neue Website. Antwort innerhalb von zwei Werktagen. Monatsbericht und eine kurze Liste. Wir setzen Ihre Texte ein. Pro Text bis zu einer Seite."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">Eine kleine Änderung ist ein Tausch von Text oder Bild oder eine Korrektur an einem bestehenden Element. Eine neue Website, ein Shop oder eine neue Funktion sind ein eigener Auftrag. Hosting zahlen Sie an Ihren Anbieter.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor dem"], ["Abo."]], fragen) + dazu([
        ('webdesign.html', 'Webdesign'),
        ('onlineshop.html', 'Onlineshop'),
        ('preisrechner.html', 'Preisrechner'),
        ('kontakt.html', 'Kontakt'),
    ]) + cta_block(
        "// nächster schritt", [["Welche Stufe"], ["passt?"]],
        "Schreiben Sie uns, welche Website es ist und welche Stufe Sie meinen. Die Schätzung im Preisrechner ist unverbindlich.",
        "Anfrage senden", "kontakt.html#projektanfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "website-pflege.html",
        "Website-Pflege im Monatsabo | Kastriot Tafolli",
        "Website-Pflege in drei Stufen: 99, 199 oder 299 € im Monat. Updates, Backups und kleine Änderungen, monatlich kündbar.",
        "website-pflege.html", inhalt, faq=fragen)


def onlineshop():
    fragen = [
        ("Was kostet ein Onlineshop?", "Für einen Onlineshop planen wir mit einem unverbindlichen Richtpreis von ca. 6.500 €. Größere Shops mit mehreren Märkten und Schnittstellen beginnen bei 15.000 €. Das konkrete Angebot richtet sich nach dem Umfang."),
        ("Wo wird der Shop betrieben?", "Konten, Domain und Zugänge bleiben bei Ihnen. Shop-System, Hosting, Zahlungsanbieter und laufende Kosten stimmen wir vor dem Start ab."),
        ("Schreiben Sie die Rechtstexte?", "Die Rechtstexte liefern Sie oder Ihre dafür beauftragte Stelle. Wir binden die abgestimmten Texte ein."),
        ("Welche Anbindungen sind möglich?", "Zum Beispiel Zahlung, Versand, Warenwirtschaft und Produktdaten. Wir prüfen die Schnittstellen und legen den vereinbarten Umfang im Angebot fest."),
    ]
    inhalt = hero_klein(
        "01", "E-Commerce",
        [["Ihr Sortiment."], ["Ein starker Onlineshop."]],
        "Vom überschaubaren Sortiment bis zum größeren Commerce-Projekt: Wir gestalten und entwickeln Shops mit klarer Produktführung, mobilem Checkout und den passenden Anbindungen.",
        ["ca. 6.500 €", "größere Shops ab 15.000 €", "nach Ihrem Bedarf"],
    ) + f'''
<section class="pad" id="umfang"><div class="shell">
    {kicker("02", "Passender Umfang")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 40px">{wipe([["Ein Shop, der heute passt."], ["Und morgen mitwächst."]])}</h2>
    {karten_grid([
        ("ca. 6.500 €", "Onlineshop", "Individuelle Gestaltung, Produktstruktur, Produktseiten, Warenkorb und Checkout. Zahlungs- und Versandwege stimmen wir auf Ihr Sortiment ab. Dazu gehören eine Einweisung und die geordnete Übergabe."),
        ("ab 15.000 €", "Größerer Onlineshop", "Mehr Produkte, mehrere Märkte oder Sprachen und Anbindungen an Warenwirtschaft oder andere Systeme. Die Umsetzung beginnt bei 15.000 €. Den konkreten Preis kalkulieren wir anhand der Funktionen und Anbindungen."),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">Unverbindliche Richtpreise. Den konkreten Leistungsumfang und Preis erhalten Sie im Angebot. Hosting, Softwarelizenzen, Zahlungsgebühren und laufende Betreuung werden gesondert abgestimmt.</p>
</div></section>''' + faq_block("03", "Häufige Fragen", [["Vor Ihrem"], ["Shop-Projekt."]], fragen) + dazu([
        ('webdesign.html', 'Webdesign'), ('website-pflege.html', 'Website-Pflege'),
        ('preisrechner.html#budgetplaner', 'Projekt kalkulieren'), ('kontakt.html', 'Kontakt'),
    ]) + cta_block("// nächster schritt", [["Was möchten Sie"], ["online verkaufen?"]],
        "Erzählen Sie uns von Sortiment, Märkten und vorhandenen Systemen. Wir planen mit Ihnen den passenden Shop.",
        "Shop-Projekt besprechen", "kontakt.html?leistung=Onlineshop#projektanfrage", "Budget planen", "preisrechner.html#budgetplaner")
    return seite_rahmen("onlineshop.html", "Onlineshop erstellen lassen | Tafolli & Co.",
        "Individuelle Onlineshops für ca. 6.500 €. Größere Commerce-Projekte mit Schnittstellen ab 15.000 €. Planung, Design, Entwicklung und Übergabe.",
        "onlineshop.html", inhalt, faq=fragen)



def web_apps():
    fragen = [
        ("Ist 390 € immer der Preis?", "Nein. 390 € ist der Einstieg für ein kleines Werkzeug. Sobald der Ablauf größer wird, nennen wir den Festpreis im Angebot, bevor die Arbeit beginnt."),
        ("Ist das die KI-Automatisierung?", "Nein. KI-Automatisierung ist ein eigenes Angebot. Preis auf Anfrage."),
        ("Speichert das Werkzeug Daten auf Ihrer Website?", "Nur, wenn wir das vorher so festlegen. Ein reiner Rechner im Browser speichert nichts. Steht eine Speicherung im Umfang, sagen wir das vor dem Start."),
        ("Betreiben Sie das Werkzeug rund um die Uhr?", "Nein. Wir übergeben es und erkläre den Umgang. Eine Bereitschaft nachts oder am Wochenende ist kein Teil dieses Preises."),
    ]
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
        ("ab 390 €", "Kleines Werkzeug", "Ein Ablauf im Browser: zum Beispiel ein Rechner, eine Checkliste oder ein Formular, das etwas vorbereitet. Ohne Anbindung an ein großes Fremdsystem. Den Festpreis schreiben wir auf, bevor wir anfangen. 390 € ist der Einstieg, wenn der Ablauf klein bleibt."),
        ("Angebot", "Größeres Projekt", "Mehrere Abläufe oder eine Anbindung an ein System, das Sie schon nutzen. Dafür nennen wir keinen Betrag auf dieser Seite. Sie bekommen ein Festpreis-Angebot, wenn Ablauf, Daten und Anbindung klar sind."),
    ])}
    {hinweis()}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">KI-Automatisierung ist ein eigenes Angebot. Preis auf Anfrage. Eine App für den App-Store, Dauerbetrieb und Rechtsberatung gehören nicht dazu.</p>
  </div>
</section>''' + faq_block("03", "Häufige Fragen", [["Vor dem"], ["Werkzeug."]], fragen) + dazu([
        ('app-entwicklung.html', 'App- und Web-App-Entwicklung'),
        ('softwareentwicklung.html', 'Softwareentwicklung'),
        ('preisrechner.html', 'Preisrechner'),
        ('kontakt.html', 'Kontakt'),
    ]) + cta_block(
        "// nächster schritt", [["Welcher Ablauf"], ["soll es sein?"]],
        "Beschreiben Sie den einen Ablauf. Danach sagen wir, ob er bei 390 € beginnt oder ein eigenes Festpreis-Angebot braucht.",
        "Anfrage senden", "kontakt.html#projektanfrage", "Preisrechner", "preisrechner.html")
    return seite_rahmen(
        "web-apps.html",
        "Web-App oder Tool nach Maß | Kastriot Tafolli",
        "Kleine Web-App oder ein Tool nach Maß ab 390 €. Ein Ablauf im Browser. Größere Projekte zum Festpreis nach Angebot.",
        "web-apps.html", inhalt, faq=fragen)


def firmenprofile():
    fragen = [
        ("Was kostet die Einrichtung lokaler Einträge?", "Die Einrichtung und Vereinheitlichung der vereinbarten Profile beginnt bei 550 € einmalig. Umfang, Standorte und Verzeichnisse werden im Angebot festgelegt."),
        ("Was kostet die laufende Betreuung?", "Für die laufende Betreuung lokaler Einträge planen Sie ab 550 € pro Monat. Welche Profile, Aktualisierungen und Auswertungen enthalten sind, vereinbaren wir vorab."),
        ("Wer bestätigt das Unternehmensprofil?", "Sie bestätigen die Angaben und führen die vom jeweiligen Anbieter verlangte Verifizierung durch. Wir begleiten die Einrichtung und verwenden tatsächliche Unternehmensdaten."),
        ("Wer behält die Zugänge?", "Sie behalten die Inhaberschaft und die Zugänge. Wir arbeiten mit den vereinbarten Berechtigungen."),
    ]
    inhalt = hero_klein("01", "Lokale Sichtbarkeit",
        [["Ihr Unternehmen."], ["Am richtigen Ort gefunden."]],
        "Google-Unternehmensprofil, Apple Maps, Bing Places und passende Verzeichnisse: Wir bringen Ihre Unternehmensdaten zusammen und halten Ihren lokalen Auftritt aktuell.",
        ["Einrichtung ab 550 €", "Betreuung ab 550 € / Monat", "echte Unternehmensdaten"],
    ) + f'''
<section class="pad" id="umfang"><div class="shell">
    {kicker("02", "Einrichten und betreuen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 40px">{wipe([["Korrekte Daten."], ["Ein stimmiger Auftritt."]])}</h2>
    {karten_grid([
        ("ab 550 € einmalig", "Profile einrichten", "Bestand prüfen, Unternehmensdaten abstimmen und die vereinbarten Profile anlegen oder korrigieren. Name, Adresse, Kontakt, Öffnungszeiten, Kategorien und Website werden einheitlich aufbereitet. Die Verifizierung erfolgt mit Ihnen."),
        ("ab 550 € / Monat", "Lokal präsent bleiben", "Laufende Pflege der vereinbarten Profile, Aktualisierung von Öffnungszeiten und Unternehmensangaben sowie abgestimmte Inhalte. Wir werten verfügbare Profilkennzahlen aus und besprechen die nächsten Schritte."),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">Unverbindliche Einstiegspreise. Anzahl der Standorte, Profilbestand und Betreuungsumfang bestimmen das Angebot. Anbieter entscheiden über die Freigabe; ein Ranking oder eine bestimmte Zahl neuer Kunden wird nicht zugesagt.</p>
</div></section>''' + faq_block("03", "Häufige Fragen", [["Vor Ihrem"], ["lokalen Auftritt."]], fragen) + dazu([
        ('suchmaschinenoptimierung.html#lokale-eintraege', 'Lokales SEO'), ('social-media.html', 'Social Media'),
        ('preisrechner.html#budgetplaner', 'Budget planen'), ('kontakt.html', 'Kontakt'),
    ]) + cta_block("// nächster schritt", [["Wie sichtbar ist"], ["Ihr Unternehmen vor Ort?"]],
        "Schicken Sie uns Ihren Unternehmensnamen und die vorhandenen Profile. Wir prüfen, wo sich Ihr Auftritt verbessern lässt.",
        "Lokale Einträge besprechen", "kontakt.html?leistung=Lokale%20Eintr%C3%A4ge#projektanfrage", "Budget planen", "preisrechner.html#budgetplaner")
    return seite_rahmen("firmenprofile.html", "Lokale Einträge ab 550 € | Tafolli & Co.",
        "Google-Unternehmensprofil und lokale Verzeichnisse einrichten ab 550 €. Laufende Betreuung ab 550 € im Monat. Einheitliche Daten und klare Zuständigkeiten.",
        "firmenprofile.html", inhalt, faq=fragen)



def preisrechner():
    from planner import section
    inhalt = section(heading='h1')
    return seite_rahmen(
        "preisrechner.html",
        "Website- und Marketing-Budget planen | Tafolli & Co.",
        "Website-Typen ab 990 €, Marketingbudgets und Kundenpotenzial interaktiv planen. Unverbindlich kalkulieren und direkt ein Beratungsgespräch anfragen.",
        "preisrechner.html", inhalt)
