# -*- coding: utf-8 -*-
from bausteine import *
from companies import company_link
from services import catalogue


def ueber_mich():
    steckbrief = [
        ("Aktuell", "F&B Manager, Vier Jahreszeiten am Schluchsee"),
        ("Unternehmen", "TB Solutions, mit Boriss Bockans"),
        ("Weiterbildung", "KI Engineering und Prompt Engineering, MSIT Berlin"),
        ("Standorte", "Schluchsee und Ostseebad Rügen"),
        ("Sprachen", "Albanisch, Deutsch C2, Englisch C1"),
        ("Schwerpunkte", "F&B, Einkauf, Digitalisierung, KI"),
    ]
    daten = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in steckbrief)

    haltung = [
        ("01", "Praxis vor Theorie", "Ich habe selbst am Pass gestanden, Dienstpläne geschrieben und Inventuren gemacht. Ich empfehle nichts, was im Tagesgeschäft nicht funktioniert, nur weil es in einer Präsentation gut aussieht."),
        ("02", "Zahlen als Grundlage", "Wareneinsatz, Deckungsbeitrag, Auslastung, Kosten pro Gast. Entscheidungen brauchen eine Basis. Ich rechne, bevor ich rate, und lege die Rechnung offen."),
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
        [["Ich komme aus dem Service."], ["Deshalb funktioniert,"], ["was ich baue."]],
        "Fünfzehn Jahre in der 5-Sterne-Hotellerie, eine Ausbildung zum Softwareingenieur und ein eigenes Unternehmen für digitale Lösungen.",
        ["Kosovo → Ostsee → Schwarzwald", "5-Sterne-Plus-Resort", "TB Solutions"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Vom Service am Tisch zur Direktion,"],["und jetzt zur Digitalisierung."]])}</h2>
        <div class="prose rise">
          <p>Mein Weg begann im Kosovo, an einem Tisch im Grand Hotel Prishtina, mit Flambieren, Filetieren und Tranchieren. Was ich dort gelernt habe, trage ich bis heute: Gastfreundschaft ist Handwerk. Sie entsteht nicht aus Leitbildern, sondern aus hundert Kleinigkeiten, die jeden Abend stimmen müssen.</p>
          <p>Über Stationen im Vertrieb, im Marketing und im Restaurantmanagement bin ich 2018 an die Ostsee gekommen und dort geblieben. Grand Hotel Binz, Cerês am Meer mit seinem Michelin-Stern-Restaurant, die Vier Jahreszeiten in Binz mit drei Häusern und sieben Outlets, Rösing Touristik, zuletzt die Raulff-Hotels mit zwei Häusern, 267 Zimmern und sechs Outlets sowie der Verantwortung für die gesamte Gruppe.</p>
          <p>Seit Juni 2026 bin ich F&amp;B Manager im Hotel Vier Jahreszeiten am Schluchsee im Schwarzwald, einem 5-Sterne-Plus-Wellness- und Familienresort. Mein zweites Zuhause bleibt Ostseebad Rügen, wo TB Solutions seinen Sitz hat. Ich bin heute an beiden Standorten aktiv: im Schwarzwald operativ, an der Ostsee unternehmerisch.</p>
          <p>Parallel dazu habe ich getan, was in dieser Branche selten ist: Ich habe programmieren gelernt. Eine Ausbildung zum Softwareingenieur, eine abgeschlossene sechsmonatige Spezialisierung auf KI Engineering mit Fokus auf die Automatisierung von Geschäftsprozessen und eine dreimonatige Schulung zum Prompt Engineer. Nicht als Hobby, sondern weil ich jeden Tag gesehen habe, wie viel Arbeitszeit in Häusern verbrennt, die eine Maschine übernehmen könnte.</p>
          <p>Mit TB Solutions, das ich gemeinsam mit meinem Geschäftspartner Boriss Bockans aufgebaut habe, bringe ich beides zusammen. Wir sind keine anonyme Agentur, sondern zwei Leute aus der Hotellerie, die verstehen, warum um 18 Uhr niemand Zeit hat, eine E-Mail zu beantworten.</p>
        </div>
      </div>
      <div class="pop-wrap" style="position:sticky;top:110px">
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
        "Kastriot Tafolli: fünfzehn Jahre 5-Sterne-Hotellerie, Ausbildung zum Softwareingenieur, KI Engineering und Inhaber von TB Solutions.",
        "ueber-mich.html", inhalt)


def werdegang():
    stationen = [
        ("2026", "Weiterbildung KI Engineering", "Master School Institute of Technology · Berlin",
         "Abgeschlossene sechsmonatige Spezialisierung auf KI Engineering mit Fokus auf die Automatisierung allgemeiner Geschäftsprozesse, ergänzt durch eine dreimonatige Schulung zum Prompt Engineer. Grundlage für die Entwicklung von TeamO.",
         ["Prozessautomatisierung", "Prompt Engineering", "Systemintegration"]),
        ("seit 2026", "F&B Manager", "Hotel Vier Jahreszeiten am Schluchsee · Schwarzwald",
         "Verantwortung für mehrere F&B-Outlets eines 5-Sterne-Plus-Wellness- und Familienresorts: Panorama, Lucia, Gugelhupf, Kachelofen und Bar, mit 100+ Mitarbeitenden. Halbpension, à la carte, Bankett und Bar unter einem Dach.",
         ["5 Outlets", "100+ Mitarbeitende", "5 Sterne Plus"]),
        ("2025", "Gastronomischer Direktor", "Raulff-Hotels OHG · Sassnitz",
         "Leitung von zwei Hotels mit 267 Zimmern und sechs F&B-Outlets, Führung von 120+ Mitarbeitenden, Steigerung der Gästezufriedenheit um 70 Prozent. Zusätzlich verantwortlich für die gesamte Hotelgruppe mit Hotel Badehaus Goor, Schlosshotel Ralswiek, Kurhotel Sassnitz, Rügen-Hotel und Rosencafé Putbus, inklusive Preisgestaltung, Einkauf und Vertragsverhandlungen.",
         ["267 Zimmer", "6 Outlets", "Gruppenverantwortung", "+70 % Zufriedenheit"]),
        ("2024", "Director of Operations", "Rösing Touristik GmbH · Sassnitz",
         "Gesamtverantwortung für drei Hotels sowie ein Resort mit fünf Restaurants, Führung eines Teams von 150+ Mitarbeitenden. Schwerpunkt auf Vereinheitlichung von Standards, Einkauf und Personalplanung über mehrere Häuser hinweg.",
         ["3 Hotels", "5 Restaurants", "150+ Mitarbeitende"]),
        ("2023 bis 2024", "Gastronomischer Direktor / Director of Operations", "Vier Jahreszeiten / Meersinn / Suite Hotel · Ostseebad Binz",
         "Verantwortung für drei Hotels und sieben F&B-Outlets, darunter ein mehrfach ausgezeichnetes Sterne-Restaurant, Führung von 180+ Mitarbeitenden. Konzeptarbeit, Qualitätssicherung und Aufbau von Führungsstrukturen in den einzelnen Häusern.",
         ["3 Hotels", "7 Outlets", "Sterne-Restaurant", "180+ Mitarbeitende"]),
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
        "Von der klassischen Serviceausbildung über Michelin-ausgezeichnete Restaurants bis zur Direktion von Hotelgruppen mit mehreren hundert Mitarbeitenden.",
        ["seit 2011", "7 Hauptstationen", "3 Sprachen"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Stationen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Siebzehn Jahre,"], ["ein roter Faden."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">Vom Oberkellner im Grand Hotel Prishtina bis zur Direktion von Hotelgruppen an der Ostsee. Jede Station hat etwas hinzugefügt, das ich heute in der Beratung einsetze.</p>
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
        "Als Beratung, als Projekt oder als F&B-Leitung auf Zeit. Sagen Sie mir, woran es gerade hakt.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Leistungen ansehen", "leistungen.html")

    return seite_rahmen("werdegang.html", "Werdegang · Kastriot Tafolli",
        "Stationen und Kompetenzen von Kastriot Tafolli: vom Oberkellner bis zur Direktion von Hotelgruppen, dazu Softwareentwicklung und KI Engineering.",
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
        ("02", "Analyse", "Ich sehe mir an, was relevant ist: Verträge, Wareneinsatz, Karten und Preise, Website, Sichtbarkeit, Abläufe und Systeme."),
        ("03", "Angebot mit klarem Umfang", "Sie bekommen schriftlich, was gemacht wird, in welcher Reihenfolge, was es kostet und welches Ergebnis realistisch ist."),
        ("04", "Umsetzung", "Ich arbeite mit Ihrem Team, nicht an ihm vorbei. Verhandlungen führe ich auf Wunsch selbst, technische Umsetzung übernimmt TB Solutions."),
        ("05", "Kontrolle und Nachjustierung", "Nach vereinbarter Zeit sehen wir uns die Zahlen an und schärfen nach. Auf Wunsch bleibe ich dauerhaft Ansprechpartner."),
    ]
    schritte = "".join(f'''<div class="rise" style="--i:{i};padding:0 0 clamp(28px,3.2vw,42px) clamp(26px,3vw,46px)">
          <p class="mono" style="font-size:.72rem;letter-spacing:.2em;color:var(--acc);margin-bottom:9px">{n}</p>
          <h3 class="d3" style="font-size:clamp(1.15rem,1.7vw,1.45rem);margin-bottom:9px">{t}</h3>
          <p style="color:var(--paper-dim);font-size:.94rem;max-width:64ch">{b}</p>
        </div>''' for i, (n, t, b) in enumerate(ablauf))
    faq = [
        ("Arbeiten Sie nur auf Rügen und im Schwarzwald?", "Nein. Vor Ort bin ich regelmäßig an der Ostsee und im Hochschwarzwald, beraten und umgesetzt wird aber bundesweit. Vieles lässt sich aus der Ferne klären, für Verhandlungen und Bestandsaufnahmen komme ich ins Haus."),
        ("Ist das nicht ein Interessenkonflikt zu Ihrer Festanstellung?", "Nein. TB Solutions ist ein angemeldetes Nebengewerbe, die Beratung findet außerhalb meiner Arbeitszeit statt und betrifft keine Wettbewerber meines Arbeitgebers. Diskretion in beide Richtungen ist selbstverständlich."),
        ("Wie schnell sehen wir Ergebnisse?", "Bei Getränke- und Lieferverträgen oft schon mit der nächsten Jahresvereinbarung, also innerhalb weniger Wochen. Bei Sichtbarkeit und Suchmaschinen dauert es meist drei bis sechs Monate, bei Google Ads dagegen wenige Tage."),
        ("Können wir einzelne Leistungen buchen statt ein Gesamtpaket?", "Ja. Viele Häuser starten mit einem einzelnen Thema, etwa der Website oder der Vertragsverhandlung, und erweitern später. Ein Gesamtpaket ist nie Voraussetzung."),
        ("Übernehmen Sie auch die laufende Betreuung?", "Ja. Website, Hosting, Kampagnen und Social Media betreue ich auf Wunsch dauerhaft als monatliche Pauschale. Genauso können Sie mich als externe F&B-Leitung für einen festen Tagesumfang im Monat buchen."),
        ("Arbeiten Sie auch mit kleinen Betrieben?", "Ja. Ein Bistro mit acht Mitarbeitenden hat andere Fragen als ein Resort mit zweihundert, aber die gleichen Grundprobleme: Einkauf, Sichtbarkeit und Zeit. Der Umfang wird entsprechend angepasst."),
    ]
    def schwerpunkt(i, label, titel, text, punkte, href, cta):
        return f'''<div class="card pop ticks" style="--i:{i};display:flex;flex-direction:column">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">{label}</p>
          <h3 class="d2" style="font-size:clamp(1.6rem,2.8vw,2.3rem);margin-bottom:14px">{titel}</h3>
          <p style="color:var(--paper-dim);font-size:.95rem;margin-bottom:22px">{text}</p>
          {punkte_liste(punkte)}
          <a href="{href}" class="btn btn-2 lnk" style="margin-top:26px;align-self:flex-start">{cta} <span class="arrow">&rarr;</span></a>
        </div>'''

    inhalt = hero_klein("03", "Leistungen", [["Beratung aus der Praxis,"], ["Umsetzung aus einer Hand."]],
        "Ich berate nicht aus dem Lehrbuch, sondern aus fünfzehn Jahren Verantwortung für Häuser, Teams und Zahlen. Und ich setze um, statt nur zu empfehlen.",
        ["22 Leistungsbereiche", "aus einer Hand", "bundesweit"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Drei Schwerpunkte")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Was ich für Hotels"], ["und Restaurants tue."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Der eine Teil betrifft das, was im Haus passiert. Der andere das, was draußen über Sie zu sehen ist. Und der dritte das, was eine Maschine übernehmen kann. Alles mache ich gemeinsam mit meinem Team von TB Solutions.</p>
    <div class="g3 pop-wrap">
      {schwerpunkt(0, "Operativ", "F&amp;B-Beratung", "Getränkeverträge, Einkauf, Kalkulation und Abläufe. Hier liegt in fast jedem Haus Geld, das niemand hebt, weil die Verhandlung Zeit kostet und Erfahrung braucht.", ["Verträge mit Brauereien und Lieferanten", "Rückvergütungen, Boni, Marketingzuschüsse", "Wareneinsatz, Kalkulation, Inventur", "Externe F&amp;B-Leitung auf Zeit"], "fb-beratung.html", "Zur F&amp;B-Beratung")}
      {schwerpunkt(1, "Digital", "Online-Marketing &amp; Web", "Website, Sichtbarkeit, Kampagnen und Inhalte. Damit Gäste Sie finden und direkt bei Ihnen buchen statt über ein Portal mit fünfzehn Prozent Provision.", ["Website und Webentwicklung", "SEO und lokale Sichtbarkeit", "Google Ads und Social Media", "Foto, Video und Drohne"], "online-marketing.html", "Zu den Digitalleistungen")}
      {schwerpunkt(2, "Künstliche Intelligenz", "AI Automation as a Service", "Für Ihren Betrieb gebaute KI-Workflows, in Ihre Systeme integriert und laufend betreut. Bis hin zum digitalen Mitarbeiter TeamO.", ["Telefon, Mail und Chat automatisiert", "Dokumente auslesen und einordnen", "Laufende Betreuung und menschliche Kontrolle", "TeamO, der digitale KI-Mitarbeiter"], "ki-automatisierung.html", "Automation ausprobieren")}
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Das gesamte Spektrum")}
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
</section>''' + faq_block("04", "Häufige Fragen", [["Was Kunden"], ["vorher wissen wollen."]], faq) + cta_block(
        "// nächster schritt", [["Welches Thema"], ["brennt am meisten?"]],
        "Sagen Sie mir in zwei Sätzen, wo es hakt, und ich sage Ihnen ehrlich, ob es sich lohnt.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Rechner öffnen", "rechner.html")

    return seite_rahmen("leistungen.html", "Leistungen · Kastriot Tafolli",
        "F&B-Beratung, Online-Marketing, Webentwicklung, KI-Automatisierung und TeamO: 22 Leistungsbereiche für Hotels und Restaurants aus einer Hand.",
        "leistungen.html", inhalt)
