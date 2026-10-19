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
        <a href="kontakt.html" class="btn btn-1 rise" style="margin-top:12px">Gespräch vereinbaren</a>
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
        "Beratungsgespräch vereinbaren", "kontakt.html", "Leistungen ansehen", "leistungen.html")
    inhalt += '<section class="service-section"><div class="shell"><p class="tag">EINZELNE LEISTUNGEN IM DETAIL</p><h2 class="d2">Vertiefen Sie Ihr Thema.</h2><div class="portfolio-links">' + "".join(link(slug) for slug in ['lieferantenvereinbarungen', 'getraenkevertraege', 'rueckverguetungen', 'wareneinsatz-kalkulation', 'inventur-warenwirtschaft', 'interim-fb-management', 'revenue-controlling', 'personal-recruiting']) + '</div></div></section>'

    return seite_rahmen("leistungen.html", "F&amp;B-Beratung für Hotels und Restaurants · Kastriot Tafolli",
        "F&B-Beratung aus der Praxis: Getränke- und Lieferverträge, Rückvergütungen, Wareneinsatz, Kalkulation und externe F&B-Leitung auf Zeit.",
        "fb-beratung.html", inhalt)


def online_marketing():
    werkzeuge = ["Google Ads", "Analytics", "Search Console", "Google Business", "Meta Business", "Instagram",
                 "Facebook", "Squarespace", "WordPress", "DreamHost", "Adobe", "Canva"]
    leistungen = [
        ("01", "Website und Webentwicklung", "Neue Website oder Modernisierung der bestehenden. Schnell, auf dem Telefon gedacht, mehrsprachig, mit klarem Weg zur Anfrage."),
        ("02", "Suchmaschinenoptimierung", "Technik, Struktur und Inhalte so aufgebaut, dass Ihr Betrieb bei den Suchanfragen auftaucht, die zu Ihrem Angebot passen."),
        ("03", "Lokale Sichtbarkeit", "Google-Unternehmensprofil, Karten, Verzeichnisse. Vollständig gepflegt, mit Bildern, Öffnungszeiten und aktuellen Angaben."),
        ("04", "Google Ads", "Kampagnen mit klarem Budgetrahmen, auf Anfragen ausgerichtet. Eine Rendite verspreche ich nicht."),
        ("05", "Social Media", "Redaktionsplan, Beiträge, Reels und Betreuung von Instagram und Facebook. Mit einem Ton, der zu Ihrem Betrieb passt."),
        ("06", "Content und Text", "Texte für Website, Newsletter und Kampagnen. Verständlich, konkret und ohne leere Floskeln."),
        ("07", "Foto, Video und Drohne", "Produktfotografie, Aufnahmen aus dem Betrieb, Imagefilme und Luftaufnahmen. Das Material gehört anschließend Ihnen."),
        ("08", "Domain, Hosting und E-Mail", "Eigene Domain, schnelles und sicheres Hosting, E-Mail-Adressen unter Ihrem Namen, laufend betreut."),
        ("09", "Cybersicherheit", "Absicherung von Website und Systemen, Backups, Zugriffsrechte und Schutz der Daten, die Sie uns anvertrauen."),
    ]
    ablauf = [
        ("Bestandsaufnahme", "Wir sehen uns an, was vorhanden ist: Website, Sichtbarkeit, Kanäle und woher Ihre Anfragen heute kommen."),
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

    inhalt = hero_klein("03.2", "Online-Marketing &amp; Web", [["Sichtbarkeit, die"], ["Anfragen bringt."]],
        "Website, Suchmaschinen, Kampagnen und Inhalte für Unternehmen. Aufgebaut so, dass Besucher Sie finden und sich melden können.",
        ["Festpreis-Angebot auf Anfrage", "SEO und Ads", "Foto, Video, Drohne"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Gefunden werden."], ["Anfragen bekommen."]])}</h2>
        <div class="prose rise">
          <p>Sichtbarkeit allein reicht nicht, wenn niemand den nächsten Schritt findet. Eine eigene Website, klare Inhalte und Kampagnen mit einem Ziel gehören zusammen.</p>
          <p>Mit TB Solutions baue ich diese Präsenz auf: eine Website, die schnell lädt und auf dem Telefon funktioniert, Inhalte, die gefunden werden, Kampagnen mit klarem Budget und Bilder, die Ihr Angebot zeigen.</p>
          <p>Sie bekommen vorab einen Umfang. Laufende Betreuung für Website, Inhalte und Kampagnen ist möglich, aber ein eigener Auftrag.</p>
        </div>
        <a href="rechner.html#social" class="btn btn-1 rise" style="margin-top:12px">Social Media einordnen</a>
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
    {zitat_block("Eine schöne Website ist kein Selbstzweck. Der Weg zur Anfrage muss klar sein.", "Kastriot Tafolli")}
  </div>
</section>''' + cta_block("// nächster schritt", [["Wie sichtbar ist"], ["Ihre Website?"]],
        "Ich sehe mir Ihre Seite und Ihre Sichtbarkeit an und sage Ihnen konkret, wo die größten Lücken sind.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Social Media einordnen", "rechner.html#social")
    inhalt += '<section class="service-section"><div class="shell"><p class="tag">EINZELNE LEISTUNGEN IM DETAIL</p><h2 class="d2">Vertiefen Sie Ihr Thema.</h2><div class="portfolio-links">' + "".join(link(slug) for slug in ['webdesign', 'suchmaschinenoptimierung', 'domain-hosting-email', 'social-media', 'foto-video', 'firmenprofile', 'preisrechner']) + '</div></div></section>'

    faq = [
        ("Was kostet Online-Marketing?", "Festpreis-Angebot auf Anfrage. Der Preis hängt davon ab, ob es um eine Website, um Kampagnen oder um laufende Betreuung geht. Einen Betrag vor diesem Gespräch nenne ich nicht."),
        ("Garantieren Sie einen Platz in der Suche?", "Nein. Ich richte Seiten, Technik und Inhalte so aus, dass Menschen das Angebot finden können. Einen Rang verspreche ich nicht."),
        ("Ist die laufende Betreuung im ersten Preis enthalten?", "Nur, wenn wir sie in den Umfang schreiben. Sonst ist die Betreuung ein eigener Auftrag, mit festem Umfang vor dem Start."),
        ("Können wir mit einer Sache starten?", "Ja. Oft ist das die Website oder ein klarer Kanal. Den Rest können wir später dazunehmen."),
        ("Arbeiten Sie auch für kleine Betriebe?", "Ja. Der Umfang richtet sich nach der Aufgabe, nicht nach der Größe des Unternehmens."),
    ]
    inhalt += faq_block("04", "Häufige Fragen", [["Vor dem"], ["ersten Schritt."]], faq)
    return seite_rahmen("leistungen.html", "Online-Marketing und Webentwicklung · Kastriot Tafolli",
        "Website, SEO, Google Ads, Social Media, Foto und Video für Unternehmen. Sichtbarkeit, die Anfragen bringt.",
        "online-marketing.html", inhalt, faq=faq)


def teamo():
    funktionen = [
        ("01", "Telefonate annehmen und vorbereiten", ["Eingehende Anrufe annehmen", "Anliegen notieren", "Rückruf notieren", "Auskunft zu Leistungen, Preisen und Öffnungszeiten, soweit Sie das freigeben", "Weiterleitung an eine zuständige Person, wenn es nötig ist"], "Erreichbar, auch wenn niemand im Büro ist."),
        ("02", "Nachrichten und Anfragen vorbereiten", ["E-Mails als Entwurf vorbereiten", "Chats auf der Website sichten", "Anfragen über Social Media sammeln", "Angebotsentwürfe mit den Angaben, die schon da sind", "Kommunikation in mehreren Sprachen"], "Im Ton Ihres Betriebs. Versand erst nach Ihrer Freigabe."),
        ("03", "Tagesberichte", ["Kurze Tagesberichte", "Offene Anfragen", "Was erledigt ist und was wartet", "Zusammenfassung für die Geschäftsführung"], "Zahlen nur aus den Quellen, die Sie anbinden."),
        ("04", "Termine und Angebote", ["Terminvorschläge sammeln", "Angebotsentwurf bereitstellen", "Absagen notieren", "Rückfragen am Vorgang lassen"], "Bestätigt wird ein Termin erst von Ihnen."),
        ("05", "Wiederkehrende Auskünfte", ["Öffnungszeiten und Leistungen nennen", "Gruppenanfragen sammeln", "Unterlagen an die richtige Person geben", "Bestellhinweise weiterleiten, wenn das vereinbart ist"], "Was Ermessen braucht, geht an einen Menschen."),
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
        ("01", "Auch außerhalb der Bürozeit", "Anrufe und Mails können vorbereitet werden, wenn niemand da ist. Was rausgeht, geben Sie frei."),
        ("02", "Wissen bleibt im Ablauf", "Öffnungszeiten, Leistungen und Ton liegen im System. Ein Personalwechsel löscht sie nicht."),
        ("03", "Mehrsprachig", "Antwortet in der Sprache, in der gefragt wird. Deutsch, Englisch und Albanisch sind der übliche Rahmen."),
        ("04", "Auf Ihren Betrieb trainiert", "Auf Ihre Leistungen, Preise, Öffnungszeiten und Ihren Ton. Kein Standardtext für jeden."),
        ("05", "Datenschutz", "Integration nach den Vorgaben der Datenschutz-Grundverordnung. Vorher steht fest, welche Daten verarbeitet werden."),
        ("06", "Anbindung", "Verbindung zu E-Mail, Kalender und den Programmen, die Sie schon nutzen. Was geht und was nicht, steht im Angebot."),
    ]
    einf = [
        ("Analyse Ihres Betriebs", "Wir sehen uns an, wo die meiste Zeit verloren geht: Telefon, E-Mail, Termine oder Berichte. Daraus entsteht der Einsatzbereich."),
        ("Training auf Ihren Betrieb", "TeamO lernt Ihre Leistungen, Preise, Öffnungszeiten und Ihren Ton. Sie geben vor, was er sagen darf und was nicht."),
        ("Anbindung und Test", "Verbindung zu Telefon, E-Mail, Website, Messenger und Ihren Systemen. Danach Probebetrieb, in dem Sie jede Antwort prüfen können."),
        ("Start und Feinschliff", "TeamO geht live. In den ersten Wochen wird nachjustiert, bis Ton und Abläufe sitzen. Danach läuft er, und Sie bekommen die Berichte."),
    ]
    pipe = ""
    for i, (t, d) in enumerate(einf):
        pipe += f'<div class="pipe-node rise" style="--i:{i}"><i></i><b>{t}</b><span>{d}</span></div>'
        if i < len(einf) - 1:
            pipe += f'<div class="pipe-track"><span class="pipe-particle" style="--i:{i}"></span></div>'
    faq = [
        ("Ersetzt TeamO unsere Mitarbeitenden?", "Nein. TeamO bereitet vor, was sonst liegen bleibt: das Telefon, Anfragen nach Feierabend, wiederkehrende Auskünfte und Berichte. Entscheidungen bleiben bei Ihrem Team."),
        ("Merkt die anrufende Person, dass sie mit einer KI spricht?", "Sie entscheiden, wie offen TeamO auftritt. Sie können sagen lassen, dass ein digitaler Assistent annimmt und bei Bedarf an einen Menschen übergibt."),
        ("Was passiert bei komplizierten Anliegen?", "TeamO erkennt, wenn ein Anliegen über seinen Rahmen hinausgeht, und leitet an die zuständige Person weiter, mit einer Zusammenfassung des bisherigen Gesprächs."),
        ("Wie steht es um den Datenschutz?", "Die Integration erfolgt nach den Vorgaben der Datenschutz-Grundverordnung. Vorab wird festgelegt, welche Daten verarbeitet werden, wo sie liegen und wie lange sie gespeichert bleiben."),
        ("Funktioniert das mit unserem bestehenden System?", "Das hängt vom System ab. TeamO kann an E-Mail, Kalender und weitere Programme angebunden werden, wenn eine Schnittstelle da ist. Was konkret möglich ist, klären wir in der Analyse."),
        ("Wer kümmert sich nach dem Start um TeamO?", "Ich. Antworten prüfen, nachschärfen, wenn sich Preise oder Abläufe ändern, und eingreifen, bevor eine kleine Abweichung bei der Kundin ankommt."),
        ("Was kostet TeamO?", "Festpreis-Angebot auf Anfrage. Den Umfang der Einrichtung und einer möglichen Betreuung schreibe ich nach dem Gespräch auf. Einen Betrag vor diesem Gespräch nenne ich nicht."),
    ]
    inhalt = hero_klein("04", "KI-Produkt", [["TeamO, der digitale"], ["KI-Mitarbeiter."]],
        "Ein digitaler Mitarbeiter für Anrufe, Nachrichten und wiederkehrende Anfragen. In mehreren Sprachen, mit Freigabe durch Ihr Team.",
        ["24 h erreichbar", "mehrsprachig", "Festpreis-Angebot auf Anfrage"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Mehr als ein Chatbot."], ["Ein Mitarbeiter, der nicht schläft."]])}</h2>
        <div class="prose rise">
          <p>TeamO ist ein digitaler Mitarbeiter für Anrufe, Nachrichten und wiederkehrende Aufgaben. Basierend auf moderner KI-Technologie und erweitert durch eine eigene Systemlogik vereint TeamO Kommunikation, Organisation und Auswertungen in einem Assistenten.</p>
          <p>Er nimmt Anrufe an, beantwortet E-Mails und Nachrichten in mehreren Sprachen, verschickt Angebote und legt morgens einen fertigen Tagesbericht hin. Rund um die Uhr, ohne Wartezeit, ohne Krankheitstage.</p>
          <p>Jeder TeamO wird auf den jeweiligen Betrieb trainiert: auf Ihre Angebote, Ihre Preise, Ihre Öffnungszeiten und Ihren Ton. Die Anbindung an bestehende Systeme erfolgt nach den Vorgaben der Datenschutz-Grundverordnung.</p>
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
            <div>anrufe angenommen ........ 12</div>
            <div>termine vorbereitet ...... 4</div>
            <div>mails als entwurf ........ 9</div>
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
</section>''' + faq_block("05", "Häufige Fragen", [["Was Betriebe"], ["vorher wissen wollen."]], faq) + f'''
<section class="pad"><div class="shell">{zitat_block("Abends ruft jemand an, weil eine Frage nicht bis morgen warten soll. TeamO nimmt das Anliegen auf.", "TeamO · TB Solutions")}</div></section>''' + cta_block(
        "// nächster schritt", [["TeamO für Ihren Betrieb."]],
        "Im Erstgespräch sehen wir uns an, wo bei Ihnen die meiste Zeit verloren geht. Daraus entsteht der konkrete Einsatzbereich.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Ersparnis berechnen", "rechner.html#ki")
    return seite_rahmen("teamo-ki.html", "TeamO, der digitale KI-Mitarbeiter · Kastriot Tafolli",
        "TeamO nimmt Anrufe an, beantwortet Anfragen mehrsprachig und erstellt Tagesberichte. Individuell trainiert. Festpreis-Angebot auf Anfrage.",
        "teamo-ki.html", inhalt, faq=faq)
