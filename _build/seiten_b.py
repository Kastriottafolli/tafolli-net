# -*- coding: utf-8 -*-
from bausteine import *


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

    inhalt = hero_klein("03.1", "F&amp;B-Beratung", [["Verträge, Einkauf"], ["und Abläufe, die tragen."]],
        "Professionelle Food-and-Beverage-Beratung für Hotels, Restaurants und Bars: von der Verhandlung mit Brauereien und Lieferanten bis zur externen F&amp;B-Leitung auf Zeit.",
        ["Verträge und Rückvergütungen", "Wareneinsatz", "Interimsleitung"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["In fast jedem Haus liegt Geld"], ["im Getränkevertrag."]])}</h2>
        <div class="prose rise">
          <p>Brauereien, Getränkefachgroßhandel, Spirituosenlieferanten, Weinhändler und Großhändler arbeiten mit Rückvergütungen, Boni, Marketingzuschüssen und Verkaufszielen. Wer diese Systeme kennt, verhandelt anders. Wer sie nicht kennt, unterschreibt den Standardvertrag und zahlt jahrelang drauf.</p>
          <p>Ich habe diese Verhandlungen jahrelang selbst geführt, zuletzt für eine Hotelgruppe mit fünf Häusern und sechs F&amp;B-Outlets. Preisgestaltung, Einkauf und Vertragsverhandlungen lagen komplett bei mir. Ich kenne die Hebel, die Reihenfolge und die Stellen, an denen ein Lieferant tatsächlich nachgibt.</p>
          <p>Dazu kommt alles, was danach passiert: Wareneinsatz, Kalkulation, Inventur, Karten, Abläufe und Personal. Ein guter Einkaufspreis nützt wenig, wenn hinten im Betrieb die Struktur fehlt.</p>
        </div>
        <a href="rechner.html#einkauf" class="btn btn-1 rise" style="margin-top:12px">Rückvergütung berechnen</a>
      </div>
      <div class="pop-wrap">
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">// typische ausgangslage</p>
          <ul class="checks">{"".join(f"<li>{p}</li>" for p in ausgangslage)}</ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Leistungen im Detail")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Was ich konkret"], ["übernehme."]])}</h2>
    {karten_grid(leistungen, "g3")}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ergebnisse")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Was dabei"], ["herauskommen kann."]])}</h2>
    <p class="lede rise" style="--i:1">Zahlen aus meiner eigenen operativen Verantwortung. Sie sind kein Versprechen, aber sie zeigen die Größenordnung, um die es geht.</p>
    {stat_row([("70", " %", "mehr Gästezufriedenheit bei Raulff-Hotels"), ("267", "", "Zimmer und 6 Outlets in einer Verantwortung"), ("5", "", "Häuser einer Gruppe in Einkauf und Preisgestaltung"), ("200", "+", "geführte Mitarbeitende gleichzeitig")])}
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("04", "Für wen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Mit welchen Betrieben"], ["ich arbeite."]])}</h2>
    <div class="split" style="align-items:start">
      <ul class="checks rise">{"".join(f"<li>{p}</li>" for p in fuer_wen)}</ul>
      <div class="pop-wrap"><div class="card pop ticks">
        <p class="tag" style="color:var(--acc);margin-bottom:14px">// ehrlich gesagt</p>
        <p style="color:var(--paper-dim);font-size:.96rem;margin-bottom:14px">Nicht jedes Haus braucht Beratung. Wenn Ihr Wareneinsatz stimmt, Ihre Verträge aktuell verhandelt sind und Ihr Team stabil läuft, sage ich Ihnen das im Erstgespräch und wir sparen uns beide die Zeit.</p>
        <p style="color:var(--paper);font-size:.96rem">Wenn aber seit drei Jahren niemand mehr mit Ihrer Brauerei gesprochen hat, lohnt sich ein Blick fast immer.</p>
      </div></div>
    </div>
    {zitat_block("Ein guter Einkaufspreis nützt wenig, wenn hinten im Betrieb die Struktur fehlt.", "Kastriot Tafolli")}
  </div>
</section>''' + cta_block("// nächster schritt", [["Lassen Sie mich einen Blick"], ["auf Ihre Verträge werfen."]],
        "Ein Gespräch, eine ehrliche Einschätzung. Wenn nichts zu holen ist, sage ich Ihnen das.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Rückvergütung berechnen", "rechner.html#einkauf")
    return seite_rahmen("leistungen.html", "F&amp;B-Beratung für Hotels und Restaurants · Kastriot Tafolli",
        "F&B-Beratung aus der Praxis: Getränke- und Lieferverträge, Rückvergütungen, Wareneinsatz, Kalkulation und externe F&B-Leitung auf Zeit.",
        "fb-beratung.html", inhalt)


def online_marketing():
    werkzeuge = ["Google Ads", "Analytics", "Search Console", "Google Business", "Meta Business", "Instagram",
                 "Facebook", "Squarespace", "WordPress", "DreamHost", "Adobe", "Canva"]
    leistungen = [
        ("01", "Website und Webentwicklung", "Neue Website oder Modernisierung der bestehenden. Schnell, auf dem Telefon gedacht, mehrsprachig, mit Speisekarten, Zimmerdarstellung und Anbindung an Ihr Buchungssystem."),
        ("02", "Suchmaschinenoptimierung", "Technik, Struktur und Inhalte so aufgebaut, dass Ihr Haus bei den Suchanfragen auftaucht, die wirklich Gäste bringen, statt bei Begriffen ohne Kaufabsicht."),
        ("03", "Lokale Sichtbarkeit", "Google-Unternehmensprofil, Karten, Verzeichnisse und Bewertungen. Vollständig gepflegt, mit Bildern, Öffnungszeiten und aktuellen Angaben."),
        ("04", "Google Ads", "Kampagnen mit klarem Budgetrahmen und messbarer Rendite, saisonal gesteuert, auf Direktbuchungen und Anfragen ausgerichtet."),
        ("05", "Social Media", "Redaktionsplan, Beiträge, Reels und Betreuung von Instagram und Facebook. Mit einem Ton, der zu Ihrem Haus passt, nicht zu einer Agenturvorlage."),
        ("06", "Content und Text", "Texte für Website, Karten, Newsletter und Kampagnen. Verständlich, konkret und ohne die Floskeln, die jeder Gast überliest."),
        ("07", "Foto, Video und Drohne", "Produktfotografie, Zimmer- und Restaurantaufnahmen, Imagefilme und Luftaufnahmen. Das Material gehört anschließend Ihnen."),
        ("08", "Domain, Hosting und E-Mail", "Eigene Domain, schnelles und sicheres Hosting, E-Mail-Adressen unter Ihrem Namen, laufend betreut."),
        ("09", "Cybersicherheit", "Absicherung von Website und Systemen, Backups, Zugriffsrechte, Schutz von Gäste- und Buchungsdaten."),
    ]
    ablauf = [
        ("Bestandsaufnahme", "Wir sehen uns an, was vorhanden ist: Website, Sichtbarkeit, Bewertungen, Kanäle, Buchungswege und woher Ihre Gäste heute tatsächlich kommen."),
        ("Konzept", "Struktur, Inhalte, Bildsprache und Maßnahmenplan. Sie sehen vorab, wie die Seite aussehen und was sie leisten soll."),
        ("Produktion", "Umsetzung von Website, Texten und Bildern, Aufsetzen von Kampagnen und Profilen, Einrichtung von Hosting und E-Mail."),
        ("Start und Messung", "Veröffentlichung, Einrichtung der Auswertung und Übergabe. Sie sehen, was passiert, nicht nur, dass etwas passiert."),
        ("Betreuung", "Auf Wunsch laufend: Pflege, Inhalte, Kampagnensteuerung, Sicherheit und regelmäßige Auswertung als monatliche Pauschale."),
    ]
    pipe = ""
    for i, (t, d) in enumerate(ablauf):
        pipe += f'<div class="pipe-node rise" style="--i:{i}"><i></i><b>{t}</b><span>{d}</span></div>'
        if i < len(ablauf) - 1:
            pipe += f'<div class="pipe-track"><span class="pipe-particle" style="--i:{i}"></span></div>'

    inhalt = hero_klein("03.2", "Online-Marketing &amp; Web", [["Sichtbarkeit, die"], ["Direktbuchungen bringt."]],
        "Website, Suchmaschinen, Kampagnen und Inhalte für Hotels und Restaurants. Aufgebaut von jemandem, der beide Seiten kennt, die Technik und den Betrieb.",
        ["Website ab 1.100 €", "SEO und Ads", "Foto, Video, Drohne"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Gefunden werden."], ["Direkt gebucht werden."]])}</h2>
        <div class="prose rise">
          <p>Die meisten Häuser zahlen zweimal: einmal für die Sichtbarkeit auf Portalen und dann noch einmal Provision für jede Buchung, die darüber kommt. Der Ausweg ist keine neue Plattform, sondern eine eigene digitale Präsenz, die trägt.</p>
          <p>Mit TB Solutions baue ich diese Präsenz auf: eine Website, die schnell lädt und auf dem Telefon funktioniert, Inhalte, die gefunden werden, Kampagnen mit klarem Budget und Bilder, die Ihr Haus so zeigen, wie es ist.</p>
          <p>Der Unterschied zu einer klassischen Agentur: Ich weiß, wie ein Reservierungsbuch aussieht, was ein Halbpensionsgast kostet und warum um 18 Uhr niemand Zeit hat, Texte freizugeben. Das ändert, wie wir arbeiten.</p>
        </div>
        <a href="rechner.html#direkt" class="btn btn-1 rise" style="margin-top:12px">Provision berechnen</a>
      </div>
      <div class="pop-wrap">
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:16px">// womit wir arbeiten</p>
          <div style="display:flex;flex-wrap:wrap;gap:8px">{"".join(f'<span class="chip">{w}</span>' for w in werkzeuge)}</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Leistungen im Detail")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Alles, was online"], ["über Sie entscheidet."]])}</h2>
    {karten_grid(leistungen, "g3")}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ablauf")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(48px,5.5vw,80px)">{wipe([["Von der ersten Skizze"], ["bis zur laufenden Betreuung."]])}</h2>
    <div class="pipe rise">{pipe}</div>
    {zitat_block("Eine schöne Website ist kein Selbstzweck. Sie muss Anfragen bringen, sonst ist sie nur teuer.", "Kastriot Tafolli")}
  </div>
</section>''' + cta_block("// nächster schritt", [["Wie sichtbar ist"], ["Ihr Haus wirklich?"]],
        "Ich sehe mir Ihre Seite und Ihre Sichtbarkeit an und sage Ihnen konkret, wo die größten Lücken sind.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Provision berechnen", "rechner.html#direkt")
    return seite_rahmen("leistungen.html", "Online-Marketing und Webentwicklung · Kastriot Tafolli",
        "Website, SEO, Google Ads, Social Media, Foto und Video für Hotels und Restaurants. Sichtbarkeit, die Direktbuchungen bringt statt Portalprovision.",
        "online-marketing.html", inhalt)


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
        ("01", "Rund um die Uhr einsatzbereit", "Auch nachts, am Wochenende und in der Hochsaison. Keine Wartezeit in der Leitung, keine unbeantwortete Anfrage über Nacht."),
        ("02", "Keine Ausfälle", "Keine Krankheitstage, kein Urlaub, keine Einarbeitung bei Personalwechsel. Das Wissen bleibt im System."),
        ("03", "Mehrsprachig", "Antwortet in der Sprache, in der gefragt wird. Gerade in touristischen Regionen ein spürbarer Unterschied."),
        ("04", "Individuell trainiert", "Auf Ihre Karten, Zimmer, Preise, Abläufe und Ihren Ton. Kein Standardassistent mit austauschbaren Antworten."),
        ("05", "Datenschutzkonform", "Integration nach den Vorgaben der Datenschutz-Grundverordnung, mit klaren Regeln, welche Daten wo verarbeitet werden."),
        ("06", "Nahtlose Anbindung", "Verbindung zu bestehenden Hotel- und Kassensystemen, Reservierungssoftware, E-Mail und Kalendern."),
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
        ("Merkt der Gast, dass er mit einer KI spricht?", "Sie entscheiden, wie transparent TeamO auftritt. In vielen Häusern wird offen kommuniziert, dass ein digitaler Assistent annimmt und bei Bedarf an einen Menschen übergibt. Das wird erfahrungsgemäß gut angenommen."),
        ("Was passiert bei komplizierten Anliegen?", "TeamO erkennt, wenn ein Anliegen über seinen Rahmen hinausgeht, und leitet an die zuständige Person weiter, mit einer Zusammenfassung des bisherigen Gesprächs."),
        ("Wie steht es um den Datenschutz?", "Die Integration erfolgt nach den Vorgaben der Datenschutz-Grundverordnung. Vorab wird festgelegt, welche Daten verarbeitet werden, wo sie liegen und wie lange sie gespeichert bleiben."),
        ("Funktioniert das mit unserem bestehenden System?", "In der Regel ja. TeamO wird an gängige Hotel- und Kassensysteme, Reservierungssoftware, E-Mail und Kalender angebunden. Was konkret möglich ist, klären wir in der Analyse."),
        ("Wer kümmert sich nach dem Start um TeamO?", "Ich. Das ist der Teil, den ich KI-Management nenne: Antworten prüfen, nachschärfen, wenn sich Preise oder Abläufe ändern, und eingreifen, bevor eine kleine Abweichung beim Gast ankommt."),
        ("Was kostet TeamO?", "KI-gestützte Lösungen starten bei 4.200 Euro für Einrichtung und Training, je nach Umfang der Anbindung. Dazu kommt eine laufende monatliche Betreuung. Sie bekommen vorab ein Angebot mit festem Umfang."),
    ]
    inhalt = hero_klein("04", "KI-Produkt", [["TeamO, der digitale"], ["KI-Mitarbeiter."]],
        "Entwickelt für Hotels, Restaurants und Gastronomiebetriebe. TeamO nimmt Anrufe an, beantwortet Anfragen in mehreren Sprachen, pflegt Reservierungen und berichtet der Geschäftsführung, rund um die Uhr.",
        ["24 h erreichbar", "mehrsprachig", "DSGVO-konform", "ab 4.200 €"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Mehr als ein Chatbot."], ["Ein Mitarbeiter, der nicht schläft."]])}</h2>
        <div class="prose rise">
          <p>TeamO ist ein vollwertiger digitaler Mitarbeiter, entwickelt speziell für Hotels, Restaurants und Gastronomiebetriebe. Basierend auf moderner KI-Technologie und erweitert durch eine eigene Systemlogik vereint TeamO Kommunikation, Organisation und Management in einem Assistenten.</p>
          <p>Er nimmt Anrufe an, beantwortet E-Mails und Nachrichten in mehreren Sprachen, pflegt Reservierungen, verschickt Angebote und legt der Geschäftsführung morgens einen fertigen Tagesbericht hin. Rund um die Uhr, ohne Wartezeit, ohne Krankheitstage.</p>
          <p>Jeder TeamO wird individuell auf den jeweiligen Betrieb trainiert: auf Ihre Karten, Ihre Zimmer, Ihre Preise, Ihre Öffnungszeiten und Ihren Ton. Die Anbindung an bestehende Systeme erfolgt datenschutzkonform nach den Vorgaben der Datenschutz-Grundverordnung.</p>
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
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Was TeamO"], ["besonders macht."]])}</h2>
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
</section>''' + faq_block("05", "Häufige Fragen", [["Was Häuser"], ["vorher wissen wollen."]], faq) + f'''
<section class="pad"><div class="shell">{zitat_block("Abends um halb elf ruft jemand an, um einen Tisch zu verschieben. TeamO nimmt ab.", "TeamO · TB Solutions")}</div></section>''' + cta_block(
        "// nächster schritt", [["TeamO für Ihr Haus."]],
        "Im Erstgespräch sehen wir uns an, wo bei Ihnen die meiste Zeit verloren geht. Daraus entsteht der konkrete Einsatzbereich.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Ersparnis berechnen", "rechner.html#ki")
    return seite_rahmen("teamo-ki.html", "TeamO, der digitale KI-Mitarbeiter für Hotels · Kastriot Tafolli",
        "TeamO nimmt Anrufe an, beantwortet Anfragen mehrsprachig, pflegt Reservierungen und erstellt Tagesberichte. Individuell trainiert, DSGVO-konform, ab 4.200 €.",
        "teamo-ki.html", inhalt)
