# -*- coding: utf-8 -*-
from bausteine import *
from companies import company_link
from services import catalogue
from portrait import portrait


def ueber_mich():
    steckbrief = [
        ("Unternehmen", "TB Solutions, mit Boriss Bockans"),
        ("Sitz", "Ostseebad Binz, Rügen"),
        ("Weiterbildung", "KI Engineering und Prompt Engineering, MSIT Berlin"),
        ("Sprachen", "Albanisch, Deutsch C2, Englisch C1"),
        ("Schwerpunkte", "KI, Software, Web, Texte"),
    ]
    daten = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in steckbrief)

    haltung = [
        ("01", "Praxis vor Theorie", "Ich habe selbst am Pass gestanden, Dienstpläne geschrieben und Inventuren gemacht. Ich empfehle nichts, was im Tagesgeschäft nicht funktioniert, nur weil es in einer Präsentation gut aussieht."),
        ("02", "Zahlen als Grundlage", "Entscheidungen brauchen eine Basis. Ich rechne, bevor ich rate, und lege die Rechnung offen."),
        ("03", "Auf Augenhöhe", "Ich rede mit dem Küchenchef genauso wie mit der Geschäftsführung. Beratung heißt nicht, Ihrem Team zu erklären, was es falsch macht, sondern mit ihm zu arbeiten."),
        ("04", "Diskretion", "Zahlen, Verträge und interne Themen bleiben, wo sie hingehören. Referenzen nenne ich nur mit Zustimmung, Details nie."),
    ]
    hotel = [
        ("Ausbildung Restaurantfachmann", "Klassische Serviceausbildung mit Haute-Cuisine-Techniken: Flambieren, Filetieren, Tranchieren"),
        ("Hotel- und Restaurantmanagement", "Betriebswirtschaft, Kalkulation, Revenue Management, Qualitätsmanagement"),
        ("Führung und Ausbildereignung", "Teamaufbau, Mitarbeiterführung, Ausbildung von über 50 Nachwuchskräften"),
        ("Sterne- und Bankettgastronomie", "Michelin-ausgezeichnete Restaurants, Veranstaltungen und Großgastronomie"),
    ]
    technik = [
        ("Ausbildung Softwareingenieur", "Softwareentwicklung, Datenbanken, Systemarchitektur"),
        ("KI Engineering, MSIT Berlin", "Abgeschlossene sechsmonatige Spezialisierung auf die Automatisierung von Geschäftsprozessen"),
        ("Prompt Engineering, MSIT Berlin", "Dreimonatige Schulung zum Prompt Engineer"),
        ("Online-Marketing", "SEO, Google Ads, Social Media, Analytics, Content und lokale Sichtbarkeit"),
    ]
    def bildung(titel, eintraege, i):
        z = "".join(f'<div style="padding:16px 0;border-bottom:1px solid var(--line-soft)">'
                    f'<b style="display:block;font-size:.98rem;margin-bottom:5px">{t}</b>'
                    f'<span style="font-size:.88rem;color:var(--paper-dim)">{d}</span></div>' for t, d in eintraege)
        return f'<div class="card pop ticks" style="--i:{i}"><p class="tag" style="color:var(--acc);margin-bottom:8px">{titel}</p>{z}</div>'

    inhalt = hero_klein("01", "Über mich",
        [["Software, Web und KI."], ["Persönlich umgesetzt."]],
        "Ich entwickle Software und KI-Workflows, gestalte Websites und schreibe Texte auf Deutsch, Englisch und Albanisch. TB Solutions hat seinen Sitz in Ostseebad Binz.",
        ["TB Solutions", "DE · EN · Albanisch", "DACH und Kosovo"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Vom Lernen zum Bauen,"],["und jetzt zu eigenen Projekten."]])}</h2>
        <div class="prose rise">
          <p>Mein Weg begann im Kosovo. Über Stationen im Vertrieb, im Marketing und in der Projektarbeit bin ich 2018 an die Ostsee gekommen. Der Sitz von TB Solutions ist Ostseebad Binz.</p>
          <p>Parallel dazu habe ich programmieren gelernt. Eine Ausbildung zum Softwareingenieur, eine abgeschlossene sechsmonatige Spezialisierung auf KI Engineering mit Fokus auf die Automatisierung von Geschäftsprozessen und eine dreimonatige Schulung zum Prompt Engineer.</p>
          <p>Mit TB Solutions, das ich gemeinsam mit meinem Geschäftspartner Boriss Bockans aufgebaut habe, setze ich das um: KI-Automatisierung, Software und Apps, Websites, Online-Marketing und Texte auf Deutsch, Englisch und Albanisch. Wir sind keine anonyme Agentur, sondern zwei Leute, die Projekte direkt begleiten.</p>
        </div>
      </div>
      <div class="pop-wrap" style="position:sticky;top:110px">
        {portrait()}
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">// auf einen blick</p>
          <dl class="daten" style="margin:0">{daten}</dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Haltung")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Wie ich arbeite."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Vier Dinge, auf die Sie sich verlassen können, ganz gleich ob es um eine Vertragsverhandlung oder um eine Website geht.</p>
    {karten_grid(haltung, "g2")}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ausbildung und Weiterbildung")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Zwei Welten,"],["bewusst gelernt."]])}</h2>
    <div class="g2 pop-wrap">{bildung("// hotellerie & gastronomie", hotel, 0)}{bildung("// technik & digitales", technik, 1)}</div>
    {zitat_block("Ich habe programmieren gelernt, weil ich sah, wie viel Arbeitszeit verbrennt, die eine Maschine übernehmen könnte.", "Kastriot Tafolli")}
  </div>
</section>''' + cta_block("// nächster schritt", [["Lernen wir uns kennen."]],
        "Am schnellsten merken Sie in einem Gespräch von dreißig Minuten, ob wir zusammenpassen.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Werdegang ansehen", "werdegang.html")

    return seite_rahmen("ueber-mich.html", "Über mich · Kastriot Tafolli",
        "Kastriot Tafolli: Softwareentwicklung, KI Engineering, Websites und Texte. Inhaber von TB Solutions in Ostseebad Binz.",
        "ueber-mich.html", inhalt)


def werdegang():
    stationen = [
        ("2026", "Weiterbildung KI Engineering", "Master School Institute of Technology · Berlin",
         "Abgeschlossene sechsmonatige Spezialisierung auf KI Engineering mit Fokus auf die Automatisierung allgemeiner Geschäftsprozesse, ergänzt durch eine dreimonatige Schulung zum Prompt Engineer. Grundlage für die Entwicklung von TeamO.",
         ["Prozessautomatisierung", "Prompt Engineering", "Systemintegration"]),
        ("2025", "Gastronomischer Direktor", "Raulff-Hotels OHG · Sassnitz",
         "Leitung von zwei Hotels mit 267 Zimmern und sechs F&B-Outlets, Führung von 120+ Mitarbeitenden, Steigerung der Gästezufriedenheit um 70 Prozent. Zusätzlich verantwortlich für die gesamte Hotelgruppe mit Hotel Badehaus Goor, Schlosshotel Ralswiek, Kurhotel Sassnitz, Rügen-Hotel und Rosencafé Putbus, inklusive Preisgestaltung, Einkauf und Vertragsverhandlungen.",
         ["267 Zimmer", "6 Outlets", "Gruppenverantwortung", "+70 % Zufriedenheit"]),
        ("2024", "Director of Operations", "Rösing Touristik GmbH · Sassnitz",
         "Gesamtverantwortung für drei Hotels sowie ein Resort mit fünf Restaurants, Führung eines Teams von 150+ Mitarbeitenden. Schwerpunkt auf Vereinheitlichung von Standards, Einkauf und Personalplanung über mehrere Häuser hinweg.",
         ["3 Hotels", "5 Restaurants", "150+ Mitarbeitende"]),
        ("2022 bis 2023", "F&B Manager", "Cerês am Meer · Ostseebad Binz",
         "Operatives Management im F&B-Bereich eines 5-Sterne-Superior Designhotels mit Michelin-Stern-Restaurant, Führung von 30+ Mitarbeitenden. Höchste Ansprüche an Service, Ablauf und Detailgenauigkeit.",
         ["5 Sterne Superior", "Michelin-Stern", "30+ Mitarbeitende"]),
        ("2018 bis 2022", "F&B Manager", "Grand Hotel Binz · Ostseebad Binz",
         "Operative Verantwortung für Restaurant, Bar, Frühstück, Room Service und Bankett, Führung von 100+ Mitarbeitenden. Aufbau von Abläufen, Schulungskonzepten und Ausbildung zahlreicher Nachwuchskräfte.",
         ["5 Outlets", "100+ Mitarbeitende", "Ausbildungsbetrieb"]),
    ]
    tl = "".join(f'''<div class="tl-item rise">
        <p class="tl-jahr">{j}</p>
        <h3 class="d3" style="font-size:clamp(1.2rem,2vw,1.6rem)">{t}</h3>
        <p class="tl-ort">{company_link(o)}</p>
        <p style="color:var(--paper-dim);font-size:.95rem;max-width:72ch">{d}</p>
        <div class="tl-chips">{"".join(f'<span class="chip">{c}</span>' for c in ch)}</div>
      </div>''' for j, t, o, d, ch in stationen)

    erste = [
        ("2017 bis 2018", "Online Marketing Manager", "Private Palace Hotels and Resorts, Grand Hotel Binz"),
        ("2017", "Restaurant Manager", "Merlin Entertainments plc, Soltau"),
        ("2017", "Teamleiter Call Center (DHL)", "IQ to Link, Prizren"),
        ("2017", "Verkaufs- und Marketingleiter", "Gjirafa.com, Prizren"),
        ("2014 bis 2016", "Verkaufs-Regionalleiter und Marketingleiter", "Swiss Concept International Ltd, Prizren"),
        ("2013 bis 2014", "Restaurantleiter", "Premium Park Hotel, Prizren"),
        ("2011 bis 2013", "Oberkellner", "Grand Hotel Prishtina, mit klassischen Serviertechniken der Haute Cuisine"),
    ]
    erste_html = "".join(f'''<div class="rise" style="--i:{i};display:grid;grid-template-columns:minmax(110px,170px) 1fr;gap:18px;padding:15px 0;border-bottom:1px solid var(--line-soft)">
        <span class="mono" style="font-size:.78rem;color:var(--acc)">{j}</span>
        <span><b style="font-size:.95rem">{t}</b><span style="display:block;font-size:.86rem;color:var(--paper-mute);margin-top:3px">{o}</span></span>
      </div>''' for i, (j, t, o) in enumerate(erste))

    kompetenzen = [
        ("01", "Hotel- und Gastronomiemanagement", "Operative Leitung mehrerer Häuser und Outlets, Prozessoptimierung, Qualitätsmanagement, Standardisierung über Standorte hinweg."),
        ("02", "F&B-Management", "Konzeptentwicklung, Sterne- und Bankettgastronomie, Menü- und Getränkekalkulation, Wareneinsatzsteuerung, Inventur."),
        ("03", "Revenue Management und Controlling", "Budgetplanung, Forecast, Deckungsbeitragsrechnung, Preisgestaltung, Kosten- und Personalkostenkontrolle."),
        ("04", "HR und Leadership", "Recruiting, Teamaufbau, Dienstplanung, Schulungskonzepte, Ausbildung, Employer Branding, Mitarbeiterbindung."),
        ("05", "Einkauf und Verhandlung", "Getränke- und Lieferverträge, Rückvergütungen, Boni, Marketingzuschüsse, Lieferkonditionen und Jahresvereinbarungen."),
        ("06", "Digitalisierung und IT", "Einführung und Betrieb von Hotel- und Kassensystemen, Schnittstellen, Reporting, Automatisierung von Routineaufgaben."),
        ("07", "Online-Marketing", "SEO, Google Ads, Social Media, Content, Analytics, lokale Sichtbarkeit und Direktbuchungsstrategie."),
        ("08", "KI und Automatisierung", "Entwicklung KI-gestützter Assistenten, Prozessautomatisierung, Prompt Engineering, Anbindung an bestehende Systeme."),
        ("09", "Softwareentwicklung", "Python, JavaScript, HTML, CSS, SQL, C und C++, Datenbanken und Webanwendungen."),
    ]
    werkzeug = [
        ("// programmiersprachen", ["Python", "JavaScript", "HTML", "CSS", "SQL", "C", "C++"]),
        ("// hotel- und kassensoftware", ["Fidelio", "Protel", "Suite8", "Gastronovi", "Micros", "Lightspeed", "Shiji", "Customer Alliance", "Dailypoint"]),
        ("// marketing und analyse", ["Google Ads", "Analytics", "Search Console", "Meta Business", "Canva", "Adobe", "Squarespace"]),
    ]
    werkzeug_html = "".join(f'''<div class="rise" style="--i:{i};margin-bottom:26px">
        <p class="tag" style="color:var(--acc);margin-bottom:12px">{t}</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{"".join(f'<span class="chip">{c}</span>' for c in cs)}</div>
      </div>''' for i, (t, cs) in enumerate(werkzeug))

    inhalt = hero_klein("02", "Werdegang", [["Jede Station hat"], ["etwas hinzugefügt."]],
        "Von früheren Projekten bis zu Softwareentwicklung und KI Engineering. Die Stationen, die ich hier nenne, sind abgeschlossene Aufgaben, nicht das Angebot dieser Website.",
        ["seit 2011", "Software und KI", "3 Sprachen"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Stationen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Siebzehn Jahre,"], ["ein roter Faden."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">Frühere Stationen und die technische Weiterbildung. Was ich heute anbiete, steht unter Leistungen: KI, Software, Web, Marketing und Texte.</p>
    <div class="timeline">{tl}</div>
    <div style="margin-top:clamp(30px,4vw,56px)">
      <p class="tag rise" style="margin-bottom:14px">// erste stationen</p>
      <div style="border-top:1px solid var(--line-soft)">{erste_html}</div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Kompetenzen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Operative Führung trifft"], ["digitales Handwerk."]])}</h2>
    {karten_grid(kompetenzen, "g3")}
    <div style="margin-top:clamp(48px,5vw,76px)">{werkzeug_html}</div>
  </div>
</section>''' + cta_block("// nächster schritt", [["Diese Erfahrung"], ["können Sie mieten."]],
        "Als Projekt oder als laufende Betreuung. Sagen Sie mir, woran es gerade hakt.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Leistungen ansehen", "leistungen.html")

    return seite_rahmen("werdegang.html", "Werdegang · Kastriot Tafolli",
        "Stationen und Kompetenzen von Kastriot Tafolli: Softwareentwicklung, KI Engineering und frühere Projekte.",
        "werdegang.html", inhalt)


def leistungen():
    spektrum = [
        ("01", "Online-Marketing & Digitalstrategie", "Strategie, Kampagnenplanung und Budgetsteuerung. Gezielt auf Anfragen und Direktbuchungen ausgerichtet statt auf Reichweite ohne Wirkung."),
        ("02", "Webdesign & Webentwicklung", "Schnelle Websites für Hotels und Restaurants, auch als Modernisierung. Mit Buchungsanbindung, Speisekarten und mehrsprachigen Inhalten."),
        ("03", "Suchmaschinenoptimierung", "Technik, Inhalte und lokale Sichtbarkeit, damit Ihr Haus gefunden wird, wenn jemand nach Restaurant, Hotel oder Ihrer Region sucht."),
        ("04", "Domain, Hosting & E-Mail", "Professionelle Domains, schnelles Hosting und E-Mail-Adressen unter Ihrem eigenen Namen, betreut und gewartet."),
        ("05", "Social Media & Content", "Redaktionsplan, Beiträge, Reels und Betreuung der Kanäle. Inhalte, die Ihr Haus zeigen, wie es wirklich ist."),
        ("06", "App- & Web-App-Entwicklung", "Individuelle Anwendungen für interne Abläufe: Dienstpläne, Checklisten, Bestellungen, Reporting und Schnittstellen zwischen Systemen."),
        ("07", "KI-gestützte Lösungen", "Individuell trainierte KI-Systeme für Kommunikation, Reservierung und Reporting, bis hin zum digitalen Mitarbeiter TeamO."),
        ("08", "KI-Automatisierung & KI-Management", "Wiederkehrende Abläufe automatisieren und das laufende System dauerhaft betreuen: prüfen, nachschärfen, eingreifen, wenn etwas nicht passt."),
        ("09", "Cybersicherheit", "Absicherung von Website, E-Mail und Systemen, Backups, Zugriffsrechte und Schutz von Gästedaten."),
        ("10", "F&B-Consulting", "Konzeptentwicklung, Prozessoptimierung, Vertrags- und Partnerberatung sowie strategische Betriebsberatung aus fünfzehn Jahren Praxis."),
        ("11", "Hospitality-Recruiting", "Teamaufbau, Stellenprofile, Auswahlverfahren, Schulungskonzepte und Employer Branding für Hotellerie und Gastronomie."),
    ]
    ablauf = [
        ("01", "Erstgespräch, unverbindlich", "Dreißig Minuten am Telefon oder vor Ort. Sie schildern die Lage, ich stelle Fragen und sage offen, ob und wo ich helfen kann."),
        ("02", "Analyse", "Ich sehe mir an, was relevant ist: Abläufe, Systeme, Website, Sichtbarkeit und Texte."),
        ("03", "Angebot mit klarem Umfang", "Sie bekommen schriftlich, was gemacht wird, in welcher Reihenfolge, was es kostet und welches Ergebnis realistisch ist."),
        ("04", "Umsetzung", "Ich arbeite mit Ihrem Team, nicht an ihm vorbei. Die technische Umsetzung übernimmt TB Solutions."),
        ("05", "Kontrolle und Nachjustierung", "Nach vereinbarter Zeit sehen wir uns die Zahlen an und schärfen nach. Auf Wunsch bleibe ich dauerhaft Ansprechpartner."),
    ]
    schritte = "".join(f'''<div class="rise" style="--i:{i};padding:0 0 clamp(28px,3.2vw,42px) clamp(26px,3vw,46px)">
          <p class="mono" style="font-size:.72rem;letter-spacing:.2em;color:var(--acc);margin-bottom:9px">{n}</p>
          <h3 class="d3" style="font-size:clamp(1.15rem,1.7vw,1.45rem);margin-bottom:9px">{t}</h3>
          <p style="color:var(--paper-dim);font-size:.94rem;max-width:64ch">{b}</p>
        </div>''' for i, (n, t, b) in enumerate(ablauf))
    faq = [
        ("Arbeiten Sie nur auf Rügen?", "Nein. Ich biete alle Leistungen in Deutschland, Österreich, der Schweiz und Kosovo an. Analyse und digitale Zusammenarbeit sind aus der Ferne möglich; Termine vor Ort stimmen wir passend zu Aufgabe und Verfügbarkeit ab."),
        ("Können wir mit einem kleinen Auftrag starten?", "Ja. Viele Projekte beginnen mit einem einzelnen Thema, etwa einer Website, einem Workflow oder einem Text, und wachsen später. Ein Gesamtpaket ist keine Voraussetzung."),
        ("Wie schnell sehen wir Ergebnisse?", "Das hängt vom Auftrag ab. Eine Übersetzung oder ein klarer Workflow ist kürzer als eine neue Website oder eine Suchmaschinenoptimierung. Den realistischen Rahmen nenne ich im Angebot."),
        ("Können wir einzelne Leistungen buchen statt ein Gesamtpaket?", "Ja. Sie wählen das Thema, das zuerst zählt. Alles andere kann später dazukommen."),
        ("Übernehmen Sie auch die laufende Betreuung?", "Ja. Website, Hosting, Kampagnen, Social Media und KI-Workflows betreue ich auf Wunsch dauerhaft. Den Umfang legen wir vorher fest."),
        ("Arbeiten Sie auch mit kleinen Betrieben?", "Ja. Der Umfang richtet sich nach der Aufgabe, nicht nach der Größe des Unternehmens."),
    ]
    def schwerpunkt(i, label, titel, text, punkte, href, cta):
        return f'''<div class="card pop ticks" style="--i:{i};display:flex;flex-direction:column">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">{label}</p>
          <h3 class="d2" style="font-size:clamp(1.6rem,2.8vw,2.3rem);margin-bottom:14px">{titel}</h3>
          <p style="color:var(--paper-dim);font-size:.95rem;margin-bottom:22px">{text}</p>
          {punkte_liste(punkte)}
          <a href="{href}" class="btn btn-2 lnk" style="margin-top:26px;align-self:flex-start">{cta} <span class="arrow">&rarr;</span></a>
        </div>'''

    inhalt = hero_klein("03", "Leistungen", [["KI, Software, Web."], ["Und klare Texte."]],
        "Ich setze um, statt nur zu empfehlen: Automatisierung, Software, Websites, Marketing und Übersetzungen auf Deutsch, Englisch und Albanisch.",
        ["KI und Software", "Web und Marketing", "DE · EN · Albanisch"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Drei Schwerpunkte")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Womit wir"], ["anfangen können."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Ein System, das Arbeit vorbereitet. Ein Auftritt, der Anfragen erleichtert. Texte, die in der richtigen Sprache ankommen. Alles mit TB Solutions, persönlich abgestimmt.</p>
    <div class="g3 pop-wrap">
      {schwerpunkt(0, "Künstliche Intelligenz", "KI Automatisierung für kleine Unternehmen", "Die erste Automatisierung zum Festpreis, zum Beispiel für E-Mail, Angebote oder Termine. Nichts geht ohne Ihre Freigabe hinaus.", ["E-Mail, Angebote oder Termine", "Freigabe bleibt bei Ihnen", "Festpreis-Angebot auf Anfrage", "Ein Ablauf zum Start"], "ki-automatisierung-kleine-unternehmen.html", "Angebot ansehen")}
      {schwerpunkt(1, "Website", "Landingpage erstellen lassen", "Website oder Landingpage zum Festpreis, inklusive Pflege und einem technischen Check. Keine Rechtsberatung.", ["Eine Seite mit Weg zur Anfrage", "Pflege nach Vereinbarung", "Technischer Website-Check", "Festpreis-Angebot auf Anfrage"], "landingpage-erstellen-lassen.html", "Angebot ansehen")}
      {schwerpunkt(2, "Sprache", "Texte und Übersetzungen", "Deutsch, Englisch und Albanisch. Ich nutze KI für den ersten Entwurf und prüfe jeden Text selbst.", ["Website-Text, Dokument oder Content-Paket", "Drei Sprachen, jede Richtung", "Festpreise 49, 59 und 99 €", "Eine Korrekturrunde"], "angebot/", "Zum Übersetzungsangebot")}
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Das gesamte Spektrum")}
    <div id="spektrum" style="scroll-margin-top:110px"></div>
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Das ganze Portfolio."], ["Jedes Thema im Detail."]])}</h2>
    {catalogue()}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ablauf")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["So läuft die"], ["Zusammenarbeit."]])}</h2>
    <div class="thread">{schritte}</div>
  </div>
</section>''' + faq_block("04", "Häufige Fragen", [["Was Kunden"], ["vorher wissen wollen."]], faq) + region() + cta_block(
        "// nächster schritt", [["Welches Thema"], ["brennt am meisten?"]],
        "Sagen Sie mir in zwei Sätzen, wo es hakt, und ich sage Ihnen ehrlich, ob es sich lohnt.",
        "Anfrage senden", "kontakt.html#anfrage", "Rechner öffnen", "rechner.html")

    return seite_rahmen("leistungen.html", "Leistungen · Kastriot Tafolli",
        "KI-Automatisierung, Software, Webdesign, Online-Marketing und Übersetzungen. Leistungen von Kastriot Tafolli und TB Solutions.",
        "leistungen.html", inhalt)
