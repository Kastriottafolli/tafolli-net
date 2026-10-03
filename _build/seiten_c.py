# -*- coding: utf-8 -*-
from bausteine import *


def _regler(key, label, mn, mx, step, val, einheit=""):
    return f'''<div class="calc-feld">
      <label for="r-{key}">{label} <b><span data-v="{key}">{val}</span>{einheit}</b></label>
      <input id="r-{key}" class="range" type="range" min="{mn}" max="{mx}" step="{step}" value="{val}" data-in="{key}">
    </div>'''


def _rechner(anker, nr, titel, text, regler, gross1_label, gross1, gross2_label, gross2, bar1_label, bar1, bar2_label, bar2, hinweis, link_label, link_href, bars=True):
    balken = ""
    if bars:
        balken = f'''<div style="margin-top:22px">
          <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--paper-mute)"><span>{bar1_label}</span><span class="mono" data-v="{bar1}Txt"></span></div>
          <div class="calc-bar"><i class="grau" data-bar="{bar1}"></i></div>
          <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--paper-mute)"><span>{bar2_label}</span><span class="mono" data-v="{bar2}Txt"></span></div>
          <div class="calc-bar"><i data-bar="{bar2}"></i></div>
        </div>'''
    return f'''
<div id="{anker}" class="card pop ticks" style="scroll-margin-top:110px;margin-bottom:clamp(28px,3.5vw,46px)">
  <p class="tag" style="color:var(--acc);margin-bottom:12px">{nr}</p>
  <h3 class="d2" style="font-size:clamp(1.6rem,3vw,2.4rem);margin-bottom:12px">{titel}</h3>
  <p style="color:var(--paper-dim);font-size:.95rem;max-width:70ch;margin-bottom:30px">{text}</p>
  <div class="calc">
    <div>{"".join(regler)}</div>
    <div class="calc-out">
      <p class="tag" style="margin-bottom:6px">{gross1_label}</p>
      <p class="gross" data-v="{gross1}" style="margin-bottom:20px"></p>
      <p class="tag" style="margin-bottom:6px">{gross2_label}</p>
      <p class="gross" data-v="{gross2}"></p>
      {balken}
      <p class="calc-hinweis">{hinweis}</p>
      <a href="{link_href}" class="lnk" style="display:inline-block;margin-top:16px;color:var(--acc);font-size:.9rem;font-weight:600">{link_label} <span class="arrow">&rarr;</span></a>
    </div>
  </div>
</div>'''


def rechner():
    r1 = _rechner("ki", "01 · Künstliche Intelligenz", "Was kostet Sie das Telefon?",
        "Anrufe und Nachrichten binden jeden Tag Arbeitszeit, die niemand als Posten in der Bilanz sieht. TeamO übernimmt erfahrungsgemäß rund 70 Prozent dieser wiederkehrenden Vorgänge.",
        [_regler("anrufe", "Anrufe pro Tag", 0, 200, 1, 45), _regler("nachrichten", "Nachrichten pro Tag (E-Mail, Chat, Social Media)", 0, 300, 1, 70),
         _regler("minuten", "Bearbeitungszeit pro Vorgang", 1, 12, 1, 4, " Min."), _regler("lohn", "Personalkosten pro Stunde", 15, 60, 1, 26, " €")],
        "Gebundene Zeit pro Monat", "kiStunden", "Ersparnis pro Jahr", "kiJahr", "Heute gebunden", "kiBar1", "Mit TeamO übrig", "kiBar2",
        "Annahme: 30 Tage pro Monat, Übernahmequote 70 Prozent. Die Ersparnis ist gewonnene Arbeitszeit, kein automatischer Personalabbau.", "TeamO ansehen", "teamo-ki.html")
    r2 = _rechner("direkt", "02 · Direktbuchungen", "Wie viel Provision zahlen Sie im Jahr?",
        "Jede Buchung über ein Portal kostet Provision. Eine eigene, gut auffindbare Website verschiebt einen Teil dieser Buchungen zu Ihnen. Schon wenige Prozentpunkte machen einen spürbaren Unterschied.",
        [_regler("naechte", "Übernachtungen pro Monat", 50, 4000, 10, 900), _regler("preis", "Durchschnittlicher Zimmerpreis", 40, 600, 5, 145, " €"),
         _regler("portal", "Anteil Portalbuchungen", 0, 100, 1, 55, " %"), _regler("prov", "Provisionssatz", 5, 25, 1, 15, " %"),
         _regler("shift", "Verschiebung zu Direktbuchungen", 0, 50, 1, 15, " %")],
        "Provision pro Jahr, heute", "provJahr", "Ersparnis pro Jahr", "direktJahr", "Provision heute", "dBar1", "Provision nach Verschiebung", "dBar2",
        "Gerechnet wird auf Jahresbasis. Die Verschiebung bezeichnet den Anteil aller Buchungen, der künftig direkt bei Ihnen landet statt über ein Portal.", "Web und Marketing", "online-marketing.html")
    r3 = _rechner("einkauf", "03 · Einkauf", "Was liegt in Ihrem Getränkevertrag?",
        "Brauereien und Getränkefachgroßhandel arbeiten mit Rückvergütungen, Boni und Zielvereinbarungen. Wer die Systematik kennt, verhandelt einen anderen Satz als wer den Standardvertrag unterschreibt.",
        ['''<div class="calc-feld">
      <label for="r-einkauf">Getränkeeinkauf pro Jahr <b><span data-v="einkaufTxt">180.000</span> €</b></label>
      <input id="r-einkauf" class="range" type="range" min="10000" max="1000000" step="5000" value="180000" data-in="einkauf">
    </div>''', _regler("aktuell", "Aktueller Rückvergütungssatz", 0, 15, 0.5, 3, " %"), _regler("ziel", "Verhandelbarer Satz", 0, 15, 0.5, 8, " %")],
        "Rückvergütung heute", "rvHeute", "Zusätzlich pro Jahr", "rvPlus", "Heute", "rBar1", "Verhandelt", "rBar2",
        "Die erreichbaren Sätze hängen von Abnahmemenge, Laufzeit und Sortiment ab. Was in Ihrem Fall realistisch ist, sehe ich beim Blick in den Vertrag.", "F&amp;B-Beratung", "fb-beratung.html")
    r4 = _rechner("social", "04 · Sichtbarkeit", "Was bringt regelmäßiges Posten?",
        "Social Media wirkt nicht über einzelne Beiträge, sondern über Frequenz. Der Rechner zeigt, wie sich Reichweite, Profilbesuche und daraus entstehende Anfragen entwickeln, wenn regelmäßig gepostet wird.",
        [_regler("posts", "Beiträge pro Woche", 0, 14, 1, 3), '''<div class="calc-feld">
      <label for="r-follower">Follower <b><span data-v="followerTxt">2.500</span></b></label>
      <input id="r-follower" class="range" type="range" min="100" max="50000" step="100" value="2500" data-in="follower">
    </div>''', '''<div class="calc-feld">
      <label for="r-erate">Interaktionsrate <b><span data-v="erateTxt">3.0</span> %</b></label>
      <input id="r-erate" class="range" type="range" min="5" max="100" step="1" value="30" data-in="erate">
    </div>'''],
        "Sichtkontakte pro Monat", "smImpr", "Anfragen pro Monat, geschätzt", "smAnfragen", "", "", "", "",
        "Schätzmodell: rund 35 Prozent organische Reichweite je Beitrag, zusätzlich Multiplikation über Interaktion, davon 4 Prozent Profilbesuche und daraus 3 Prozent konkrete Anfragen. Reale Werte schwanken nach Branche und Region.", "Social Media und Content", "online-marketing.html", bars=False)

    inhalt = hero_klein("06", "Rechner", [["Vier Rechner, die"], ["im Browser laufen."]],
        "Personalkosten durch Künstliche Intelligenz, Portalprovision gegen Direktbuchung, Rückvergütung im Getränkeeinkauf und Reichweite über Social Media. Schieben Sie die Regler und sehen Sie live, worüber wir reden.",
        ["läuft lokal im Browser", "keine Daten werden gespeichert", "Annahmen offen gelegt"]) + f'''
<section class="pad" style="padding-top:clamp(32px,4vw,56px)">
  <div class="shell">
    {kicker("01", "Zahlen statt Versprechen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Rechnen Sie selbst nach,"], ["bevor Sie mit mir sprechen."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Vier Rechner aus meiner täglichen Praxis. Sie laufen direkt hier im Browser, es wird nichts gespeichert und nichts verschickt. Die Annahmen dahinter stehen jeweils darunter, damit Sie nachvollziehen können, wie gerechnet wird.</p>
    <div class="pop-wrap" data-rechner>{r1}{r2}{r3}{r4}</div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Einordnung")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Rechner ersetzen"], ["kein Gespräch."]])}</h2>
    <p class="lede rise" style="--i:1">Die Zahlen hier oben sind Modellrechnungen mit offen gelegten Annahmen. Sie zeigen Größenordnungen, keine Garantien. Was in Ihrem Haus tatsächlich möglich ist, hängt von Verträgen, Auslastung, Team und Region ab. Genau das sehe ich mir im Erstgespräch an, und wenn nichts zu holen ist, sage ich Ihnen das.</p>
  </div>
</section>''' + cta_block("// nächster schritt", [["Prüfen wir Ihre"], ["echten Zahlen."]],
        "Bringen Sie Ihre Werte mit, dann rechnen wir im Gespräch mit echten Verträgen statt mit Annahmen.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Leistungen ansehen", "leistungen.html")
    return seite_rahmen("rechner.html", "Rechner: KI-Ersparnis, Portalprovision, Rückvergütung · Kastriot Tafolli",
        "Vier Rechner im Browser: Was kostet Sie das Telefon, wie viel Portalprovision zahlen Sie, was liegt im Getränkevertrag und was bringt Social Media.",
        "rechner.html", inhalt)


ARTIKEL = [
    ("wissen-ki-im-hotel.html", "Künstliche Intelligenz", "6 Min.", "Was ein KI-Mitarbeiter im Hotel wirklich übernimmt",
     "Zwischen Chatbot-Marketing und Betriebsrealität liegt ein weiter Weg. Was heute funktioniert, was nicht, und wo die Grenze verläuft."),
    ("wissen-getraenkevertrag.html", "Einkauf", "7 Min.", "Der Getränkevertrag, den niemand liest",
     "Rückvergütungen, Boni, Marketingzuschüsse. Wie diese Systeme funktionieren und warum die meisten Betriebe Geld liegen lassen."),
    ("wissen-direktbuchungen.html", "Sichtbarkeit", "6 Min.", "Warum Ihre Gäste über ein Portal buchen",
     "Fünfzehn Prozent Provision sind kein Naturgesetz. Was eine eigene Website leisten muss, damit Gäste direkt buchen."),
]


def wissen():
    karten = "".join(f'''<a href="{h}" class="card pop lnk ticks" style="--i:{i};display:flex;flex-direction:column;gap:14px">
          <div style="display:flex;justify-content:space-between;gap:12px"><p class="tag" style="color:var(--acc)">{k}</p><p class="tag">{z}</p></div>
          <h3 class="d3" style="font-size:clamp(1.25rem,1.9vw,1.6rem)">{t}</h3>
          <p style="color:var(--paper-dim);font-size:.92rem;flex:1">{b}</p>
          <span style="color:var(--acc);font-size:.9rem;font-weight:600">Artikel lesen <span class="arrow">&rarr;</span></span>
        </a>''' for i, (h, k, z, t, b) in enumerate(ARTIKEL))
    kommt = [("01", "Wareneinsatz richtig rechnen", "Warum die übliche Prozentrechnung in die Irre führt und wie ein Deckungsbeitrag pro Gericht die Karte verändert."),
             ("02", "Dienstplan ohne Dauerkrise", "Planung, Springerlogik und die Frage, warum gute Leute wegen des Plans gehen und nicht wegen des Gehalts."),
             ("03", "Die ersten neunzig Tage", "Was eine neue F&B-Leitung in den ersten drei Monaten tun sollte, und was sie auf keinen Fall zuerst anfassen darf."),
             ("04", "KI-Management im Alltag", "Was nach dem Start eines KI-Systems passieren muss, damit es in einem Jahr noch so gut antwortet wie am ersten Tag.")]
    inhalt = hero_klein("07", "Wissen", [["Aufgeschrieben,"], ["weil ich es ständig erkläre."]],
        "Fachtexte aus der Praxis zu Künstlicher Intelligenz im Hotel, zum Getränkevertrag und zur Frage, warum Gäste über Portale buchen statt direkt.",
        ["3 Artikel", "offene Rechenwege", "aus der Praxis"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Artikel")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Drei Themen, die in fast jedem"], ["Haus Geld kosten."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Kein Blog mit Neuigkeiten, sondern ausgearbeitete Texte zu Fragen, die mir in Gesprächen immer wieder begegnen. Mit offenen Rechnungen und ohne Marketingfloskeln.</p>
    <div class="g3 pop-wrap">{karten}</div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "In Arbeit")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Was als Nächstes kommt."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Die Reihe wächst. Wenn Sie ein Thema besonders interessiert, schreiben Sie mir, dann rücke ich es nach vorne.</p>
    {karten_grid(kommt, "g2", pop=False)}
  </div>
</section>''' + cta_block("// nächster schritt", [["Ein Thema,"], ["das hier fehlt?"]],
        "Schreiben Sie mir, worüber Sie mehr wissen wollen. Oft ist die Antwort schneller als ein Artikel.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Rechner öffnen", "rechner.html")
    return seite_rahmen("wissen.html", "Wissen · Kastriot Tafolli",
        "Fachtexte aus der Praxis: KI-Mitarbeiter im Hotel, der Getränkevertrag und warum Gäste über Portale buchen statt direkt.",
        "wissen.html", inhalt)


def _artikel(datei, nummer, rubrik, zeilen, lede, chips, koerper, cta_tag, cta_zeilen, cta_text, c1, h1, c2, h2, titel, beschr):
    weitere = "".join(f'''<a href="{h}" class="card pop lnk ticks" style="--i:{i};display:flex;flex-direction:column;gap:12px">
          <p class="tag" style="color:var(--acc)">{k}</p><h3 class="d3" style="font-size:1.15rem">{t}</h3>
          <span style="color:var(--acc);font-size:.88rem;font-weight:600">Lesen <span class="arrow">&rarr;</span></span></a>'''
        for i, (h, k, z, t, b) in enumerate([a for a in ARTIKEL if a[0] != datei]))
    inhalt = hero_klein(nummer, rubrik, zeilen, lede, chips) + f'''
<section class="pad" style="padding-top:clamp(28px,4vw,52px)">
  <div class="shell">
    <article class="prose rise">{koerper}
      <p style="margin-top:2.6em;padding-top:1.4em;border-top:1px solid var(--line);font-size:.92rem">Kastriot Tafolli · F&amp;B Manager und Digitalberater · <a href="kontakt.html">Fragen dazu? Schreiben Sie mir.</a></p>
    </article>
  </div>
</section>
<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    <p class="tag rise" style="margin-bottom:24px">// weiterlesen</p>
    <div class="g2 pop-wrap">{weitere}</div>
  </div>
</section>''' + cta_block(cta_tag, cta_zeilen, cta_text, c1, h1, c2, h2)
    return seite_rahmen("wissen.html", titel, beschr, datei, inhalt)


def wissen_ki():
    k = '''
<p>Jedes Haus kennt die Situation. Es ist Freitagabend, das Restaurant ist voll, an der Rezeption steht eine Familie mit drei Koffern, und das Telefon klingelt zum vierten Mal. Jemand möchte einen Tisch von Samstag auf Sonntag verschieben. Die Kollegin nimmt ab, weil sie es immer tut, und der Gast am Tresen wartet weitere zwei Minuten.</p>
<p>Über ein Jahr summieren sich diese zwei Minuten zu Wochen. Sie tauchen in keiner Kostenstelle auf, weil sie in Löhnen stecken, die ohnehin gezahlt werden. Genau hier setzt ein KI-Mitarbeiter an, und genau deshalb wird sein Nutzen regelmäßig falsch eingeschätzt: Er spart selten Stellen, er gibt Zeit zurück.</p>
<h2>Was heute zuverlässig funktioniert</h2>
<p>Aus der Arbeit mit Systemen wie TeamO lässt sich ziemlich genau sagen, welche Aufgaben stabil laufen. Gemeinsames Merkmal: klare Regeln, wiederkehrende Muster, vorhandene Datenbasis.</p>
<ul>
<li>Anrufe annehmen, Verfügbarkeiten prüfen, Reservierungen aufnehmen und bestätigen</li>
<li>Auskünfte zu Öffnungszeiten, Anfahrt, Parkplatz, Hunden, Wellnessbereich und Halbpension</li>
<li>E-Mails, Website-Chats und Nachrichten über Messenger in mehreren Sprachen beantworten</li>
<li>Angebote nach hinterlegten Preisen erstellen und versenden</li>
<li>Tagesberichte, Auslastungs- und Umsatzübersichten automatisch zusammenstellen</li>
<li>Gruppen- und Eventanfragen vorqualifizieren und strukturiert weitergeben</li>
</ul>
<p>Das klingt unspektakulär. In der Praxis ist es das Gegenteil: Diese Vorgänge machen in vielen Häusern den überwiegenden Teil der telefonischen und schriftlichen Kommunikation aus.</p>
<blockquote>Ein KI-Mitarbeiter spart selten Stellen. Er gibt Zeit zurück, und zwar genau dann, wenn es voll ist.</blockquote>
<h2>Wo die Grenze verläuft</h2>
<p>Ebenso wichtig ist, was ein solches System nicht leisten sollte. Beschwerden mit emotionalem Gewicht gehören an einen Menschen. Preisverhandlungen bei Gruppen und Veranstaltungen gehören an einen Menschen. Alles, was Ermessen verlangt, etwa eine Kulanzentscheidung nach einem verdorbenen Aufenthalt, gehört an einen Menschen.</p>
<p>Ein gut eingerichtetes System erkennt diese Fälle und übergibt. Es tut das mit einer Zusammenfassung des bisherigen Gesprächs, sodass der Gast nicht alles zweimal erzählen muss. Wer diese Grenze nicht sauber zieht, bekommt die Beschwerden, die er vermeiden wollte.</p>
<h2>Was es kostet und was zurückkommt</h2>
<p>Rechnen wir mit einem mittelgroßen Haus: 45 Anrufe und 70 Nachrichten pro Tag, im Schnitt vier Minuten Bearbeitung, Personalkosten von 26 Euro pro Stunde.</p>
<div class="rechnung">
<p class="tag" style="margin:0 0 6px;font-size:.69rem">// beispielrechnung</p>
<div><span>Gebundene Zeit pro Monat</span><b>230 Stunden</b></div>
<div><span>Übernahme durch das System</span><b>rund 70 %</b></div>
<div><span>Zurückgewonnene Zeit pro Monat</span><b>161 Stunden</b></div>
<div class="summe"><span>Gegenwert pro Jahr</span><b>rund 50.000 €</b></div>
<div><span>Einrichtung und Training</span><b>ab 4.200 €</b></div>
</div>
<p>Diese Zahlen sind eine Modellrechnung, keine Garantie. Sie zeigen aber, warum die Frage selten lautet, ob sich so ein System rechnet, sondern eher, wie schnell. Auf der <a href="rechner.html#ki">Rechnerseite</a> können Sie die Werte Ihres Hauses selbst einsetzen.</p>
<h2>Worauf Sie bei der Einführung achten sollten</h2>
<ul>
<li>Das System muss auf Ihr Haus trainiert werden, nicht auf die Branche allgemein</li>
<li>Sie legen fest, was gesagt werden darf und was nicht, schriftlich und vorab</li>
<li>Vor dem Start gehört ein Probebetrieb dazu, in dem Sie jede Antwort prüfen</li>
<li>Die Anbindung an Ihr bestehendes System entscheidet über den Nutzen, nicht die KI selbst</li>
<li>Datenschutz wird vorher geklärt: welche Daten, wo verarbeitet, wie lange gespeichert</li>
</ul>
<p>Und ein letzter Punkt aus der Praxis: Nehmen Sie Ihr Team mit. Ein KI-Mitarbeiter, der ohne Erklärung eingeführt wird, erzeugt Unsicherheit. Einer, der sichtbar das Telefon während des Services übernimmt, wird nach zwei Wochen verteidigt.</p>'''
    return _artikel("wissen-ki-im-hotel.html", "07.1", "Künstliche Intelligenz",
        [["Was ein KI-Mitarbeiter"], ["im Hotel wirklich übernimmt"]],
        "Zwischen Chatbot-Marketing und Betriebsrealität liegt ein weiter Weg. Was heute tatsächlich funktioniert, was nicht, und wo die Grenze verläuft.",
        ["Lesezeit 6 Minuten", "Praxis", "TeamO"], k, "// nächster schritt", [["TeamO für Ihr Haus prüfen."]],
        "Im Erstgespräch sehen wir uns an, wo bei Ihnen die meiste Zeit verloren geht.", "TeamO ansehen", "teamo-ki.html", "Ersparnis berechnen", "rechner.html#ki",
        "Was ein KI-Mitarbeiter im Hotel wirklich übernimmt · Kastriot Tafolli",
        "Was ein KI-Mitarbeiter im Hotel heute zuverlässig übernimmt, wo die Grenze verläuft und was es kostet. Mit Beispielrechnung.")


def wissen_getraenke():
    k = '''
<p>Der Getränkevertrag ist das am meisten unterschätzte Dokument in der Gastronomie. Er wird einmal unterschrieben, meist unter Zeitdruck bei einer Eröffnung oder Übernahme, und läuft danach jahrelang weiter. Niemand liest ihn noch einmal, weil er funktioniert: Die Ware kommt, die Rechnung geht raus, der Zapfhahn läuft.</p>
<p>Genau darauf ist er ausgelegt. Lieferanten verdienen nicht an dem Betrieb, der jedes Jahr nachverhandelt, sondern an dem, der es nicht tut.</p>
<h2>Die vier Hebel</h2>
<p>Wer verhandeln will, muss wissen, woran gedreht werden kann. In den allermeisten Verträgen gibt es vier Stellschrauben, und sie hängen zusammen.</p>
<ul>
<li>Der Einkaufspreis pro Gebinde, meist gestaffelt nach Abnahmemenge</li>
<li>Die Rückvergütung, ein Prozentsatz auf den Jahresumsatz, oft an Ziele gekoppelt</li>
<li>Marketingzuschüsse für Ausstattung, Gläser, Sonnenschirme, Außenbestuhlung, Veranstaltungen</li>
<li>Konditionen: Lieferrhythmus, Mindestabnahme, Zahlungsziel, Skonto, Laufzeit, Leergutregelung</li>
</ul>
<p>Der Fehler, den viele machen: Sie verhandeln nur über den ersten Punkt. Der Preis pro Fass ist aber oft der Punkt, an dem der Lieferant am wenigsten nachgibt, weil er intern hart kalkuliert ist. Die Rückvergütung und die Zuschüsse liegen dagegen in einem Budget, das ohnehin für Kundenbindung vorgesehen ist.</p>
<blockquote>Lieferanten verdienen nicht an dem Betrieb, der jedes Jahr nachverhandelt, sondern an dem, der es nicht tut.</blockquote>
<h2>Was ein Prozentpunkt bedeutet</h2>
<p>Rechnen wir mit einem Haus, das für 180.000 Euro im Jahr Getränke einkauft, was für ein mittleres Hotel mit Restaurant und Bar nicht ungewöhnlich ist.</p>
<div class="rechnung">
<p class="tag" style="margin:0 0 6px;font-size:.69rem">// rückvergütung</p>
<div><span>Getränkeeinkauf pro Jahr</span><b>180.000 €</b></div>
<div><span>Rückvergütung bei 3 %</span><b>5.400 €</b></div>
<div><span>Rückvergütung bei 8 %</span><b>14.400 €</b></div>
<div class="summe"><span>Unterschied pro Jahr</span><b>9.000 €</b></div>
<div class="summe"><span>Unterschied über 5 Jahre Laufzeit</span><b>45.000 €</b></div>
</div>
<p>Fünf Prozentpunkte klingen nach wenig. Über eine übliche Vertragslaufzeit sind sie die Sanierung einer Küche. Und sie kosten niemanden etwas außer einem Termin und Vorbereitung.</p>
<h2>Was Sie vorbereiten müssen</h2>
<p>Ohne Zahlen keine Verhandlung. Wer ohne Vorbereitung in ein Gespräch geht, verhandelt gegen jemanden, der seine Zahlen genau kennt. Diese Unterlagen brauchen Sie.</p>
<ul>
<li>Den aktuellen Vertrag, vollständig, inklusive aller Anlagen und Nachträge</li>
<li>Die Einkaufsvolumen der letzten drei Jahre, aufgeschlüsselt nach Sortiment</li>
<li>Die tatsächlich erhaltenen Rückvergütungen und Zuschüsse, mit Nachweis</li>
<li>Eine realistische Prognose für die kommenden Jahre</li>
<li>Mindestens ein Vergleichsangebot eines Wettbewerbers</li>
</ul>
<p>Der letzte Punkt ist der wirksamste. Ein Vergleichsangebot verändert ein Gespräch grundlegend, auch wenn Sie gar nicht wechseln wollen.</p>
<h2>Der häufigste Fehler</h2>
<p>Er besteht nicht darin, schlecht zu verhandeln. Er besteht darin, ausgehandelte Beträge nie abzurufen. Rückvergütungen werden oft an Bedingungen geknüpft: Mindestmengen, Sortimentstreue, fristgerechte Meldung. Wer nicht meldet, bekommt nicht. Ich habe Betriebe gesehen, die über Jahre Ansprüche hatten und nie eine Gutschrift bekamen, weil niemand den Termin im Kalender hatte.</p>
<p>Deshalb gehört zu jeder Verhandlung ein zweiter Schritt: ein einfacher Kontrollprozess, der prüft, ob das Vereinbarte auch ankommt. Das ist keine Raketenwissenschaft, sondern ein Termin im Jahresverlauf und eine Liste.</p>'''
    return _artikel("wissen-getraenkevertrag.html", "07.2", "Einkauf",
        [["Der Getränkevertrag,"], ["den niemand liest"]],
        "Rückvergütungen, Boni, Marketingzuschüsse und Verkaufsförderung. Wie diese Systeme funktionieren und warum die meisten Betriebe Geld liegen lassen.",
        ["Lesezeit 7 Minuten", "Einkauf", "Verhandlung"], k, "// nächster schritt", [["Was steht in Ihrem Vertrag?"]],
        "Schicken Sie mir Ihren aktuellen Getränkevertrag, und ich sage Ihnen, wo Spielraum liegt.", "F&amp;B-Beratung ansehen", "fb-beratung.html", "Rückvergütung berechnen", "rechner.html#einkauf",
        "Der Getränkevertrag, den niemand liest · Kastriot Tafolli",
        "Rückvergütungen, Boni und Marketingzuschüsse im Getränkevertrag: die vier Hebel, was ein Prozentpunkt bedeutet und der häufigste Fehler.")


def wissen_direkt():
    k = '''
<p>Ein Gast, der über ein Portal bucht, hat Ihr Haus meist schon vorher gesehen. Er hat gesucht, verglichen, sich entschieden und dann dort gebucht, wo der Weg am kürzesten war. In den allermeisten Fällen war das nicht Ihre Website, sondern ein Portal mit einem Buchungsknopf, der seit Jahren optimiert wird.</p>
<p>Die Provision dafür liegt je nach Anbieter und Vereinbarung meist zwischen zehn und achtzehn Prozent. Bei einem Haus mit 900 Übernachtungen im Monat und 145 Euro Durchschnittspreis, von denen 55 Prozent über Portale kommen, sind das rund 129.000 Euro im Jahr.</p>
<div class="rechnung">
<p class="tag" style="margin:0 0 6px;font-size:.69rem">// provision</p>
<div><span>Übernachtungen pro Monat</span><b>900</b></div>
<div><span>Durchschnittlicher Zimmerpreis</span><b>145 €</b></div>
<div><span>Anteil über Portale</span><b>55 %</b></div>
<div><span>Provision bei 15 %</span><b>129.195 € pro Jahr</b></div>
<div class="summe"><span>Ersparnis bei 15 % Verschiebung</span><b>35.235 € pro Jahr</b></div>
</div>
<blockquote>Niemand muss die Portale abschaffen. Es genügt, einen Teil der Buchungen zu verschieben.</blockquote>
<h2>Der entscheidende Punkt wird meist übersehen</h2>
<p>Viele Häuser reagieren darauf mit einer neuen Website. Das ist richtig und reicht trotzdem nicht. Denn eine Website verschiebt keine Buchung, solange drei Dinge nicht stimmen: Sie muss gefunden werden, sie muss schneller zum Ziel führen als das Portal, und sie muss einen Grund liefern, direkt zu buchen.</p>
<h2>1. Gefunden werden</h2>
<p>Portale investieren enorme Summen in Sichtbarkeit. Dagegen gewinnt niemand auf breiten Begriffen. Gewinnen können Sie dort, wo Portale schwach sind: beim eigenen Namen, bei der Region in Verbindung mit einem konkreten Anlass, bei allem Lokalen.</p>
<ul>
<li>Der eigene Hausname muss unangefochten auf Platz eins stehen, inklusive falscher Schreibweisen</li>
<li>Das Google-Unternehmensprofil vollständig gepflegt, mit aktuellen Bildern und Öffnungszeiten</li>
<li>Seiten für konkrete Anlässe statt einer allgemeinen Angebotsseite</li>
<li>Bewertungen aktiv einsammeln und beantworten, auch die schlechten</li>
</ul>
<h2>2. Schneller zum Ziel</h2>
<p>Prüfen Sie es selbst: Wie viele Klicks braucht ein Gast auf Ihrer Seite vom Start bis zur bestätigten Buchung? Beim Portal sind es meist drei bis vier. Wenn es bei Ihnen sieben sind, oder wenn sich ein Buchungsfenster öffnet, das auf dem Telefon nicht bedienbar ist, verlieren Sie den Gast genau dort.</p>
<p>Dazu kommt die Ladezeit. Jede Sekunde kostet messbar Buchungen. Eine Seite, die auf dem Telefon über einem Mobilfunknetz vier Sekunden lädt, hat verloren, bevor sie überhaupt gezeigt wurde.</p>
<h2>3. Einen Grund liefern</h2>
<p>Der Gast weiß, dass Sie Provision zahlen. Geben Sie ihm einen konkreten Vorteil dafür, dass er direkt bucht, und benennen Sie ihn deutlich. Das muss kein Rabatt sein, der Ihre Marge frisst.</p>
<ul>
<li>Späterer Check-out oder früherer Check-in bei Direktbuchung</li>
<li>Ein Getränk, ein Frühstück, ein Wellnessgutschein, der Sie wenig kostet und viel wert wirkt</li>
<li>Kostenfreie Stornierung zu besseren Bedingungen als beim Portal</li>
<li>Die Bestpreisgarantie, sichtbar und einlösbar, nicht im Kleingedruckten</li>
</ul>
<h2>Was realistisch ist</h2>
<p>Niemand verschiebt fünfzig Prozent seiner Buchungen. Zehn bis zwanzig Prozent sind über ein bis zwei Jahre erreichbar, wenn alle drei Punkte bearbeitet werden. Bei dem Beispielhaus oben sind das rund 35.000 Euro im Jahr, die nicht mehr als Provision abfließen. Das rechtfertigt eine neue Website mehrfach, und zwar im ersten Jahr.</p>'''
    return _artikel("wissen-direktbuchungen.html", "07.3", "Sichtbarkeit",
        [["Warum Ihre Gäste"], ["über ein Portal buchen"]],
        "Fünfzehn Prozent Provision sind kein Naturgesetz. Was eine eigene Website leisten muss, damit Gäste direkt bei Ihnen landen.",
        ["Lesezeit 6 Minuten", "Web", "Direktbuchung"], k, "// nächster schritt", [["Wie sichtbar ist"], ["Ihr Haus wirklich?"]],
        "Ich sehe mir Ihre Seite an und sage Ihnen konkret, wo die größten Lücken sind.", "Web und Marketing", "online-marketing.html", "Provision berechnen", "rechner.html#direkt",
        "Warum Ihre Gäste über ein Portal buchen · Kastriot Tafolli",
        "Portalprovision gegen Direktbuchung: gefunden werden, schneller zum Ziel, einen Grund liefern. Mit Beispielrechnung für ein Hotel.")
