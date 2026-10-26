# -*- coding: utf-8 -*-
"""The three public offers. No invented prices, reviews or results."""
from bausteine import cta_block, faq_block, hero_klein, karten_grid, kicker, seite_rahmen, wipe

KI_ALT = [
    ('de', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
    ('sq', 'https://tafolli.net/sq/automatizim-ia.html'),
    ('x-default', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
]


def ki_kleine():
    ablauf = [
        ("Gespräch", "Sie beschreiben einen Ablauf, der wiederkehrt: E-Mails, Angebote oder Termine. Wir grenzen einen ersten Schritt ab."),
        ("Entwurf", "Wir richten diesen einen Ablauf ein. Was nach außen oder in ein System gehen soll, bleibt ein Entwurf."),
        ("Ihre Freigabe", "Sie prüfen den Entwurf und geben ihn frei. Ohne diese Freigabe wird nichts versendet und nichts gebucht."),
        ("Festpreis", "Den Umfang und den Preis schreiben wir vorher auf. Festpreis-Angebot auf Anfrage, kein Preis von der Stange."),
    ]
    inhalt = hero_klein(
        "01", "KI-Automatisierung",
        [["KI Automatisierung"], ["für kleine Unternehmen."]],
        "Die erste Automatisierung zum Festpreis. Zum Beispiel für E-Mails, Angebote oder Termine. Jede Ausgabe, die nach außen geht, geben Sie frei.",
        ["Festpreis-Angebot auf Anfrage", "Freigabe durch Sie", "ein Ablauf zum Start"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Womit wir anfangen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Ein Ablauf."], ["Nicht ein ganzes System."]])}</h2>
    {karten_grid([
        ("01", "E-Mail", "Eingehende Anfragen werden sortiert und als Antwortentwurf vorbereitet. Sie lesen den Entwurf und entscheiden, was rausgeht."),
        ("02", "Angebote", "Aus einer Anfrage entsteht ein Angebotsentwurf mit den Angaben, die schon da sind. Preis und Zusage prüfen Sie selbst."),
        ("03", "Termine", "Terminanfragen werden gesammelt und ein Vorschlag vorbereitet. Bestätigt wird der Termin erst von Ihnen."),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">Welche Systeme angebunden werden, hängt von dem ab, was Sie schon nutzen. Das steht im Festpreis-Angebot, nicht als pauschales Versprechen.</p>
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch">Ein einzelnes Werkzeug oder eine kleine Web-App ist ein anderes Angebot und beginnt bei 390 €. <a href="web-apps.html">Web-App oder Tool nach Maß</a></p>
  </div>
</section>
<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("03", "Ablauf")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["So entsteht"], ["der Festpreis."]])}</h2>
    {karten_grid(ablauf)}
  </div>
</section>''' + faq_block("04", "Häufige Fragen", [["Vor dem"], ["ersten Ablauf."]], (faq := [
        ("Was kostet die erste Automatisierung?", "Festpreis-Angebot auf Anfrage. Den Preis nennen wir, nachdem der Ablauf und die Anbindung klar sind. Einen Betrag vor diesem Gespräch nennen wir nicht."),
        ("Geht etwas ohne mich raus?", "Nein. Entwürfe, die nach außen gehen oder einen Termin oder ein Angebot festmachen, brauchen Ihre Freigabe."),
        ("Ersetzen Sie mein Team?", "Nein. Der Ablauf bereitet Arbeit vor. Entscheidungen bleiben bei Ihnen."),
        ("Ist das Rechtsberatung zum Datenschutz?", "Nein. Wir richten den Ablauf technisch ein und sage, welche Daten der Entwurf sieht. Eine rechtliche Prüfung ist keine Leistung dieser Seite."),
    ])) + cta_block(
        "// nächster schritt", [["Welcher Ablauf"], ["soll der erste sein?"]],
        "Schreiben Sie uns, ob es um E-Mail, Angebote oder Termine geht. Danach bekommen Sie ein Festpreis-Angebot.",
        "Anfrage senden", "kontakt.html#projektanfrage", "Weitere KI-Seiten", "ki-automatisierung.html")
    return seite_rahmen(
        "ki-automatisierung-kleine-unternehmen.html",
        "KI Automatisierung für kleine Unternehmen · Kastriot Tafolli",
        "KI Automatisierung für kleine Unternehmen: erste Automatisierung zum Festpreis.",
        "ki-automatisierung-kleine-unternehmen.html", inhalt, faq=faq, alternates=KI_ALT)


def landingpage():
    inhalt = hero_klein(
        "02", "Website",
        [["Landingpage"], ["erstellen lassen."]],
        "Eine Landingpage oder Mini-Website ab 1.500 €. Design, Inhalte und Funktionen bestimmen den Umfang. Vor dem Start erhalten Sie ein konkretes Angebot. Pflege vereinbaren wir bei Bedarf gesondert.",
        ["ab 1.500 €", "Pflege nach Vereinbarung", "technischer Check"],
    ) + f'''
<section class="pad" id="umfang">
  <div class="shell">
    {kicker("02", "Was dazugehört")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Eine Seite,"], ["die zur Anfrage führt."]])}</h2>
    {karten_grid([
        ("01", "Website oder Landingpage", "Eine klare Seite oder eine kleine Website. Besucher sehen, was Sie anbieten, und finden den Weg zur Anfrage."),
        ("02", "Pflege und Wartung", "Nach dem Start können wir Texte, Technik und kleine Änderungen betreuen. Der Umfang steht im Festpreis-Angebot, nicht als offene Pauschale."),
        ("03", "Technischer Website-Check", "Wir prüfen, ob die Seite auf dem Telefon bedienbar ist, ob Titel und Beschreibungen da sind und ob der Kontaktweg funktioniert."),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:28px">Die laufende Pflege gibt es auch als Monatsabo: 99, 199 oder 299 €. <a href="website-pflege.html">Website-Pflege im Monatsabo</a></p>
  </div>
</section>
<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("03", "Technischer Check")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Barrierefreiheit und Datenschutz"], ["nur als Technik."]])}</h2>
    <div class="prose rise">
      <p>Zum Check gehören technische Punkte: Kontrast, Beschriftungen, Bedienung mit der Tastatur, ob Bilder einen Alternativtext haben und ob ein Formular Daten auf der Website speichert.</p>
      <p>Das ist keine Rechtsberatung und keine Zertifizierung. Ob eine Seite eine gesetzliche Pflicht erfüllt, prüfen wir nicht. Wenn Sie eine rechtliche Bewertung brauchen, holen Sie die bei einer dafür zugelassenen Stelle ein.</p>
    </div>
  </div>
</section>''' + faq_block("04", "Häufige Fragen", [["Vor dem"], ["Festpreis."]], (faq := [
        ("Was kostet eine Landingpage?", "Landingpages und Mini-Websites beginnen bei 1.500 €. Eine Landingpage planen wir je nach Umfang mit 1.500–3.500 €. Vor der Umsetzung stimmen wir Design, Inhalte und Funktionen im konkreten Angebot ab."),
        ("Ist die Pflege im ersten Preis enthalten?", "Nur, wenn wir sie in den Umfang schreiben. Sonst ist die Pflege ein eigener Auftrag. Das Monatsabo steht unter <a href=\"website-pflege.html\">Website-Pflege</a>: 99, 199 oder 299 €."),
        ("Prüfen Sie die Seite rechtlich?", "Nein. Barrierefreiheit und Datenschutz prüfen wir als Technik: Bedienung, Beschriftung, Kontrast und ob Daten auf der Website gespeichert werden. Eine rechtliche Bewertung ist nicht Teil dieser Leistung."),
        ("Kann eine vorhandene Seite überarbeitet werden?", "Ja, wenn die Zugänge da sind. Was bleibt und was neu wird, steht vor dem Start im Angebot."),
    ])) + cta_block(
        "// nächster schritt", [["Welche Seite"], ["soll entstehen?"]],
        "Schreiben Sie uns, ob Sie eine Landingpage oder eine kleine Website brauchen. Danach bekommen Sie ein Festpreis-Angebot.",
        "Anfrage senden", "kontakt.html#projektanfrage", "Texte und Übersetzungen", "angebot/")
    return seite_rahmen(
        "landingpage-erstellen-lassen.html",
        "Landingpage erstellen lassen · Kastriot Tafolli",
        "Landingpage erstellen lassen, zum Festpreis.",
        "landingpage-erstellen-lassen.html", inhalt, faq=faq)
