# -*- coding: utf-8 -*-
from bausteine import *
from services import link


def fb_beratung():
    leistungen = [
        ("01", "Getränke- und Lieferverträge", "Prüfung bestehender Verträge, Ausschreibung, Verhandlung und Abschluss mit Brauereien, Getränkefachgroßhandel, Spirituosen- und Weinlieferanten sowie Großhändlern."),
        ("02", "Rückvergütungen und Boni", "Aushandeln von Rückvergütungen, Jahresboni und Zielvereinbarungen. Prüfung, ob zustehende Beträge tatsächlich abgerufen und gutgeschrieben werden."),
        ("03", "Marketingzuschüsse", "Zuschüsse von Brauereien und Lieferanten für Ausstattung, Werbemittel, Veranstaltungen und Außenbestuhlung, die viele Betriebe nie anfragen."),
        ("04", "Einkaufspreise und Konditionen", "Optimierung von Verkaufsförderungsmodellen, Staffelpreisen, Mindestabnahmen, Liefer- und Zahlungskonditionen."),
        ("05", "Wareneinsatz und Kalkulation", "Analyse des Wareneinsatzes, Kalkulation von Speisen und Getränken, Deckungsbeiträge pro Artikel, Karte nach Ertrag statt nach Gewohnheit."),
        ("06", "Inventur und Kontrolle", "Aufbau funktionierender Inventurprozesse, Schwund- und Bruchkontrolle, Schnittstellen zwischen Kasse, Lager und Buchhaltung."),
        ("07", "Abläufe und Qualität", "Servicestandards, Übergaben, Checklisten, Briefings und Qualitätssicherung über mehrere Outlets hinweg."),
        ("08", "Personal und Schulung", "Dienstplanung, Personalkostensteuerung, Schulungskonzepte, Ausbildung und Aufbau von Führungsstrukturen im Team."),
        ("09", "Externe F&B-Leitung", "Interimsleitung des F&B-Bereichs bei Vakanz, Umbau oder Neueröffnung, mit festem Tagesumfang pro Monat."),
    ]
    ausgangslage = ["Der Getränkevertrag läuft seit Jahren unverändert weiter.",
                    "Rückvergütungen werden nicht geprüft oder nicht abgerufen.",
                    "Der Wareneinsatz schwankt, ohne dass jemand sagen kann warum.",
                    "Die Karte ist gewachsen statt kalkuliert.",
                    "Es fehlt eine Führungskraft, die den F&amp;B-Bereich zusammenhält."]
    fuer_wen = ["Hotels und Resorts mit mehreren F&amp;B-Outlets", "Restaurants, auch mit gehobenem Anspruch",
                "Bars, Cafés und Bistros", "Strandrestaurants und Saisonbetriebe",
                "Pensionen und kleinere Häuser", "Hotelgruppen mit mehreren Standorten"]

    inhalt = hero_klein("03.3", "Consulting", [["Beratung zu Prozessen"], ["und Wirtschaftlichkeit."]],
        "Wir unterstützen bei der Analyse und Weiterentwicklung betrieblicher Abläufe, Organisation und Einkauf. Ein besonderer Schwerpunkt liegt auf Hotellerie, Gastronomie und F&amp;B-Management.",
        ["Prozesse & Organisation", "Einkauf & Kennzahlen", "Hospitality & F&B"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Betriebliche Aufgaben"], ["strukturiert bearbeiten."]])}</h2>
        <div class="prose rise">
          <p>Ausgangspunkt ist eine konkrete betriebliche Frage: unklare Abläufe, fehlende Zuständigkeiten, aufwendige Abstimmung oder Kennzahlen, die keine ausreichende Orientierung geben. Wir betrachten die vorhandenen Grundlagen und legen gemeinsam Prioritäten fest.</p>
          <p>Die Beratung kann Prozessaufnahme, Organisationsfragen, Einkauf, Kalkulation und Controlling umfassen. Bei digitalen Aufgaben werden die Bereiche Technology und AI Automation einbezogen. Ziele, Entscheidungsspielräume und die erwarteten Ergebnisse werden vorab vereinbart.</p>
          <p>Für Hotellerie und Gastronomie besteht besondere operative Erfahrung: Lieferanten- und Getränkevereinbarungen, Wareneinsatz, Inventur, Teamabläufe und F&amp;B-Führung. Die folgenden Leistungen vertiefen diesen fachlichen Schwerpunkt.</p>
        </div>
        <a href="kontakt.html" class="btn btn-1 rise" style="margin-top:12px">Beratungsbedarf besprechen</a>
      </div>
      <div class="pop-wrap">
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">// hospitality-schwerpunkt</p>
          <ul class="checks">{"".join(f"<li>{p}</li>" for p in ausgangslage)}</ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Hospitality & F&B im Detail")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Leistungen für"], ["Hotellerie und Gastronomie."]])}</h2>
    {karten_grid(leistungen, "g3")}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ergebnisse")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Operative Erfahrung"], ["des Gründers."]])}</h2>
    <p class="lede rise" style="--i:1">Die folgenden Kennzahlen stammen aus früheren beruflichen Positionen von Gründer Kastriot Tafolli und beschreiben seine persönliche Führungsverantwortung.</p>
    {stat_row([("70", " %", "mehr Gästezufriedenheit bei Raulff-Hotels"), ("267", "", "Zimmer und 6 Outlets in einer Verantwortung"), ("5", "", "Häuser einer Gruppe in Einkauf und Preisgestaltung"), ("200", "+", "geführte Mitarbeitende gleichzeitig")])}
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("04", "Für wen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Für welche Betriebe"], ["wir arbeiten."]])}</h2>
    <div class="split" style="align-items:start">
      <ul class="checks rise">{"".join(f"<li>{p}</li>" for p in fuer_wen)}</ul>
      <div class="pop-wrap"><div class="card pop ticks">
        <p class="tag" style="color:var(--acc);margin-bottom:14px">// ehrlich gesagt</p>
        <p style="color:var(--paper-dim);font-size:.96rem;margin-bottom:14px">Nicht jedes Haus braucht Beratung. Wenn Ihr Wareneinsatz stimmt, Ihre Verträge aktuell verhandelt sind und Ihr Team stabil läuft, sprechen wir das im Erstgespräch offen an.</p>
        <p style="color:var(--paper);font-size:.96rem">Wenn aber seit drei Jahren niemand mehr mit Ihrer Brauerei gesprochen hat, lohnt sich ein Blick fast immer.</p>
      </div></div>
    </div>
    {zitat_block("Ein guter Einkaufspreis nützt wenig, wenn hinten im Betrieb die Struktur fehlt.", "Kastriot Tafolli")}
  </div>
</section>''' + cta_block("// nächster schritt", [["Beratungsbedarf besprechen."]],
        "Beschreiben Sie die Ausgangslage und das gewünschte Ergebnis. Gemeinsam klären wir einen passenden Beratungsumfang.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Rückvergütung berechnen", "rechner.html#einkauf")
    inhalt += '<section class="service-section"><div class="shell"><p class="tag">EINZELNE LEISTUNGEN IM DETAIL</p><h2 class="d2">Vertiefen Sie Ihr Thema.</h2><div class="portfolio-links">' + "".join(link(slug) for slug in ['lieferantenvereinbarungen', 'getraenkevertraege', 'rueckverguetungen', 'wareneinsatz-kalkulation', 'inventur-warenwirtschaft', 'interim-fb-management', 'revenue-controlling', 'personal-recruiting']) + '</div></div></section>'

    return seite_rahmen("leistungen.html", "Consulting & F&B-Beratung · Tafolli & Co.",
        "Beratung zu Prozessen, Organisation und Wirtschaftlichkeit. Besondere Kompetenz in Hotellerie, Gastronomie, Einkauf und F&B-Management.",
        "fb-beratung.html", inhalt)


def online_marketing():
    from marketing import page
    return page()


def teamo():
    funktionen = [
        ("01", "Telefonate annehmen und bearbeiten", ["Automatische Annahme eingehender Anrufe", "Reservierungen entgegennehmen", "Verfügbarkeiten prüfen", "Auskunft zu Zimmern, Preisen, Öffnungszeiten und Veranstaltungen", "Weiterleitung an zuständige Mitarbeitende, wenn es nötig ist"], "Rund um die Uhr erreichbar, ohne Wartezeiten."),
        ("02", "Nachrichten und Anfragen beantworten", ["E-Mails automatisch beantworten", "WhatsApp und Website-Chats verwalten", "Anfragen über Social Media bearbeiten", "Angebote erstellen und versenden", "Kommunikation in mehreren Sprachen"], "Schnell, professionell und immer im Ton Ihres Hauses."),
        ("03", "Tagesberichte und Auswertungen", ["Automatische Tagesberichte", "Auslastungsanalysen", "Umsatzübersichten", "Personal- und Serviceberichte", "Zusammenfassungen für die Geschäftsführung"], "Alle relevanten Zahlen, strukturiert aufbereitet."),
        ("04", "Rezeption und Reservierung", ["Reservierungsverwaltung", "Angebotsversand und Buchungsbestätigungen", "Stornobearbeitung", "Gästekommunikation vor, während und nach dem Aufenthalt", "Pflege von Gästedaten und Sonderwünschen"], "Entlastet die Rezeption genau dann, wenn es voll wird."),
        ("05", "Restaurantmanagement", ["Tischreservierungen verwalten", "Event- und Gruppenanfragen bearbeiten", "Menü- und Allergeninformationen bereitstellen", "Feedback und Bewertungen analysieren", "Dienstpläne vorbereiten", "Bestell- und Warenprozesse unterstützen"], "Der Überblick bleibt, auch wenn das Haus voll ist."),
    ]
    karten = ""
    for i, (nr, titel, punkte, fazit) in enumerate(funktionen):
        lis = "".join(f'<li style="padding:11px 0;border-bottom:1px solid var(--line-soft);font-size:.9rem;color:var(--paper-dim)">{p}</li>' for p in punkte)
        karten += f'''
    <div class="stack-item"><div class="stack-pin">
      <div class="card ticks" style="background:var(--ink-2)">
        <div style="display:flex;justify-content:space-between;gap:16px;align-items:baseline;margin-bottom:18px">
          <p class="tag"><span class="n">{nr}</span>&nbsp;&nbsp;Funktion</p>
          <span class="mono" style="font-size:.7rem;color:var(--paper-mute)">{i+1} / {len(funktionen)}</span>
        </div>
        <h3 class="d2" style="font-size:clamp(1.7rem,3.2vw,2.7rem);margin-bottom:18px">{titel}</h3>
        <div class="split" style="gap:clamp(24px,4vw,64px);align-items:start">
          <p class="d3" style="font-size:1.15rem;color:var(--acc);font-weight:400">{fazit}</p>
          <ul style="list-style:none;margin:0;padding:0;border-top:1px solid var(--line-soft)">{lis}</ul>
        </div>
      </div>
    </div></div>'''
    besonders = [
        ("01", "Rund um die Uhr einsatzbereit", "Eine erweiterte Erreichbarkeit kann mit geeigneter Telefon- und Systemanbindung eingerichtet werden. Verfügbarkeit und Übergabewege werden vereinbart."),
        ("02", "Dokumentiertes Betriebswissen", "Freigegebene Informationen bleiben nachvollziehbar im System. Änderungen und Zuständigkeiten werden strukturiert gepflegt."),
        ("03", "Mehrsprachig", "Antwortet in der Sprache, in der gefragt wird. Gerade in touristischen Regionen ein spürbarer Unterschied."),
        ("04", "Individuell trainiert", "Auf Ihre Karten, Zimmer, Preise, Abläufe und Ihren Ton. Kein Standardassistent mit austauschbaren Antworten."),
        ("05", "Geregelte Datenverarbeitung", "Verarbeitete Daten, Anbieter, Zugriffsrechte und Speicherfristen werden vor der Umsetzung geklärt."),
        ("06", "Abgestimmte Systemanbindung", "Vorhandene Schnittstellen und Berechtigungen bestimmen, wie Hotelsoftware, E-Mail oder Kalender verbunden werden können."),
    ]
    einf = [
        ("Analyse Ihres Betriebs", "Wir sehen uns an, wo die meiste Zeit verloren geht: Telefon, E-Mail, Reservierungen, Gruppenanfragen oder Reporting. Daraus entsteht der Einsatzbereich."),
        ("Training auf Ihr Haus", "TeamO lernt Ihre Karten, Zimmer, Preise, Öffnungszeiten, Hausregeln und Ihren Ton. Sie geben vor, was er sagen darf und was nicht."),
        ("Anbindung und Test", "Verbindung zu Telefon, E-Mail, Website, Messenger und Ihren Systemen. Danach Probebetrieb, in dem Sie jede Antwort prüfen können."),
        ("Start und Feinschliff", "TeamO geht live. In den ersten Wochen wird nachjustiert, bis Ton und Abläufe sitzen. Danach läuft er, und Sie bekommen die Berichte."),
    ]
    pipe = ""
    for i, (t, d) in enumerate(einf):
        pipe += f'<div class="pipe-node rise" style="--i:{i}"><i></i><b>{t}</b><span>{d}</span></div>'
        if i < len(einf) - 1:
            pipe += f'<div class="pipe-track"><span class="pipe-particle" style="--i:{i}"></span></div>'
    faq = [
        ("Ersetzt TeamO unsere Mitarbeitenden?", "Nein. TeamO übernimmt das, was ohnehin liegen bleibt: das Telefon während des Services, Anfragen nach Feierabend, wiederkehrende Auskünfte und Berichte. Ihr Team gewinnt dadurch Zeit für die Gäste, die im Haus sind."),
        ("Merkt der Gast, dass er mit einer KI spricht?", "Die KI-Unterstützung wird transparent gestaltet. Hinweise auf den Assistenten und die Übergabe an eine zuständige Person werden in der Konzeption festgelegt."),
        ("Was passiert bei komplizierten Anliegen?", "TeamO erkennt, wenn ein Anliegen über seinen Rahmen hinausgeht, und leitet an die zuständige Person weiter, mit einer Zusammenfassung des bisherigen Gesprächs."),
        ("Wie steht es um den Datenschutz?", "Die Integration erfolgt nach den Vorgaben der Datenschutz-Grundverordnung. Vorab wird festgelegt, welche Daten verarbeitet werden, wo sie liegen und wie lange sie gespeichert bleiben."),
        ("Funktioniert das mit unserem bestehenden System?", "Das hängt von den verfügbaren Schnittstellen, Zugriffsrechten und Anforderungen ab. Die technische Machbarkeit einer Anbindung prüfen wir vor der Zusage."),
        ("Wer kümmert sich nach dem Start um TeamO?", "Die laufende Betreuung wird im Angebot geregelt: Antworten prüfen, Inhalte bei geänderten Preisen oder Abläufen aktualisieren und Abweichungen bearbeiten. Ansprechpartner und Umfang werden festgelegt."),
        ("Was kostet TeamO?", "KI-gestützte Lösungen starten bei 4.200 Euro für Einrichtung und Training, je nach Umfang der Anbindung. Dazu kommt eine laufende monatliche Betreuung. Sie bekommen vorab ein Angebot mit festem Umfang."),
    ]
    inhalt = hero_klein("04", "KI-Produkt", [["TeamO."], ["KI-Unterstützung für Hospitality."]],
        "Entwickelt für Hotels, Restaurants und Gastronomiebetriebe. TeamO kann wiederkehrende Anfragen und ausgewählte Abläufe unterstützen. Funktionsumfang, Systemanbindung und menschliche Kontrolle werden im Projekt festgelegt.",
        ["KI-Assistent", "Betriebswissen", "Klare Freigaben"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Anfragen und Abläufe"], ["mit KI unterstützen."]])}</h2>
        <div class="prose rise">
          <p>TeamO ist ein KI-Assistent für Hotels, Restaurants und Gastronomiebetriebe. Er unterstützt definierte Aufgaben in Kommunikation, Organisation und Auswertung auf Grundlage der freigegebenen Betriebsinformationen.</p>
          <p>Je nach vereinbartem Funktionsumfang können Telefon- und Nachrichtenanfragen, Reservierungsabläufe, Angebotsentwürfe und Tagesberichte unterstützt werden. Aktionen, die Buchungen oder andere betriebliche Daten verändern, erhalten festgelegte Berechtigungen und Freigaben.</p>
          <p>Wissensquellen, Sprache und Regeln werden auf Ihren Betrieb abgestimmt. Vor einer Anbindung klären wir Datenverarbeitung, Zugriffsrechte, technische Voraussetzungen und die Übergabe an zuständige Menschen.</p>
        </div>
        <div class="rise" style="display:flex;flex-wrap:wrap;gap:13px;margin-top:12px">
          <a href="kontakt.html" class="btn btn-1">TeamO anfragen</a>
          <a href="rechner.html#ki" class="btn btn-2">Ersparnis berechnen</a>
        </div>
      </div>
      <div class="pop-wrap">
        <div class="dash pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:8px">Beispielhafte Ansicht</p>
          <p style="color:var(--paper-dim);font-size:.86rem;margin-bottom:18px">So meldet sich TeamO morgens bei der Geschäftsführung. Werte sind ein Beispiel.</p>
          <div class="dash-top"><span class="dot pulse"></span><span class="mono" style="font-size:.82rem">TeamO · online</span></div>
          <div class="term" style="font-size:.78rem">
            <div class="c">$ teamo --bericht heute</div>
            <div>anrufe angenommen ........ 38</div>
            <div>reservierungen ........... 14</div>
            <div>mails beantwortet ........ 51</div>
            <div>an mitarbeitende ......... 3</div>
            <div class="c">● alle offenen vorgänge erfasst</div>
          </div>
          <div class="dash-bar"><i></i></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Funktionen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Was TeamO übernimmt."]])}</h2>
    <div class="stack" style="perspective:1600px">{karten}</div>
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Unterschiede")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Grundlagen des Einsatzes."]])}</h2>
    {karten_grid(besonders, "g3")}
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("04", "Einführung")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["In vier Schritten"], ["im Einsatz."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(48px,5.5vw,80px)">Die Einführung läuft parallel zum Tagesgeschäft. Ihr Team muss nichts umstellen, bis TeamO wirklich läuft.</p>
    <div class="pipe rise">{pipe}</div>
  </div>
</section>''' + faq_block("05", "Häufige Fragen", [["Fragen zu TeamO."]], faq) + f'''
<section class="pad"><div class="shell">{zitat_block("Abends um halb elf ruft jemand an, um einen Tisch zu verschieben. TeamO nimmt ab.", "TeamO · Tafolli & Co.")}</div></section>''' + cta_block(
        "// nächster schritt", [["TeamO für Ihr Haus."]],
        "Im Erstgespräch sehen wir uns an, wo bei Ihnen die meiste Zeit verloren geht. Daraus entsteht der konkrete Einsatzbereich.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Ersparnis berechnen", "rechner.html#ki")
    return seite_rahmen("teamo-ki.html", "TeamO: KI-Assistent für Hospitality · Tafolli & Co.",
        "TeamO unterstützt Hotels und Gastronomie als KI-Assistent bei ausgewählten Anfragen und Abläufen. Funktionsumfang, Daten und Freigaben werden abgestimmt.",
        "teamo-ki.html", inhalt)
