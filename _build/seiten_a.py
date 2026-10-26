# -*- coding: utf-8 -*-
from bausteine import *
from companies import company_link
from services import catalogue
from portrait import portrait


def ueber_mich():
    kompetenzen = [
        ("01", "Marketing", "Strategie, Positionierung und Markenauftritt. Dazu Kampagnen, Content, Social Media, Suchmaschinen und laufende Auswertung."),
        ("02", "Technology", "Individuelle Software, Websites und Anwendungen für iOS, Android und Web. Schnittstellen, Systemintegration und Cybersecurity gehören zum technischen Angebot."),
        ("03", "Consulting", "Prozesse, Organisation und Wirtschaftlichkeit strukturiert verbessern. Besondere Erfahrung besteht in Hotellerie, Gastronomie, Einkauf und operativer Führung."),
        ("04", "AI Automation", "KI-Assistenten und automatisierte Abläufe auf konkrete Aufgaben ausrichten. Datenquellen, Zuständigkeiten und Freigaben werden vor der Umsetzung festgelegt."),
    ]
    haltung = [
        ("01", "Praxis als Ausgangspunkt", "Die Arbeit beginnt bei den Menschen, Aufgaben und Systemen in Ihrem Unternehmen. Erst daraus entsteht die passende Lösung."),
        ("02", "Klare Vereinbarungen", "Ziele, Umfang, Zuständigkeiten und Kosten werden vor der Umsetzung abgestimmt. Ergebnisse werden anhand der vereinbarten Kriterien betrachtet."),
        ("03", "Zusammenarbeit auf Augenhöhe", "Die Menschen, die täglich mit einem Ablauf arbeiten, werden in Analyse, Erprobung und Übergabe einbezogen."),
        ("04", "Diskretion", "Interne Zahlen, Verträge und Informationen werden vertraulich behandelt. Referenzen und Projektdetails werden nur mit entsprechender Zustimmung genannt."),
    ]
    steckbrief = [
        ("Gründer & Ansprechpartner", "Kastriot Tafolli"),
        ("Erfahrung des Gründers", "15 Jahre gehobene Hotellerie und operative Führung"),
        ("Technischer Hintergrund", "Softwareentwicklung, KI Engineering und Prompt Engineering"),
        ("Sprachen", "Albanisch, Deutsch und Englisch"),
        ("Zusammenarbeit", "Deutschland, Österreich, Schweiz und Kosovo"),
    ]
    daten = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in steckbrief)
    inhalt = hero_klein("01", "Unternehmen",
        [["Marketing. Technologie."], ["Beratung. KI-Automatisierung."]],
        "Tafolli &amp; Co. unterstützt Unternehmen in Marketing, Technology, Consulting und AI Automation. Wir planen, entwickeln und begleiten Lösungen nach den Anforderungen Ihres Unternehmens.",
        ["Marketing", "Technology", "Consulting", "AI Automation"]) + f'''
<section class="pad" id="unternehmen"><div class="shell">
  {kicker("01", "Tafolli &amp; Co.")}
  <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
    <div><h2 class="d2 wipe recede-exit" style="margin:20px 0 24px">{wipe([["Leistungen im Zusammenhang."]])}</h2>
    <p class="lede rise">Digitale Lösungen und betriebliche Beratung gehören zusammen, wenn sie den Alltag eines Unternehmens verbessern sollen.</p></div>
    <div class="prose rise"><p>Eine Website braucht klare Inhalte und einen verlässlichen Anfrageweg. Eine Automatisierung braucht geeignete Daten und definierte Zuständigkeiten. Eine neue Software muss zu den Menschen passen, die damit arbeiten.</p>
    <p>Tafolli &amp; Co. betrachtet diese Themen im Zusammenhang: Ziele verstehen, einen sinnvollen Umfang festlegen, die Lösung umsetzen und ihre Nutzung begleiten. Die Zusammenarbeit ist auch über Ländergrenzen hinweg möglich.</p>
    <p>Hotellerie und Gastronomie bilden eine besondere fachliche Grundlage. KI, Software, Websites und Online-Marketing stehen ebenso Unternehmen anderer Branchen offen.</p></div>
  </div>
  <div style="margin-top:clamp(40px,5vw,64px)">{karten_grid(kompetenzen, "g2")}</div>
</div></section>
<section class="pad" id="gruender" style="background:var(--ink-2)"><div class="shell">
  {kicker("02", "Der Gründer")}
  <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px);margin-top:28px">
    <div><h2 class="d2" style="margin-bottom:24px">Kastriot Tafolli.</h2>
    <div class="prose rise"><p>Die Verbindung von Betrieb und Technologie geht auf den beruflichen Weg von Kastriot Tafolli zurück: vom klassischen Service im Grand Hotel Prishtina über Führungsaufgaben in der gehobenen Hotellerie bis zur Softwareentwicklung und KI.</p>
    <p>Zu seinen Stationen gehören Grand Hotel Binz, Cerês am Meer, Rösing Touristik und die Raulff-Hotels. Diese Stationen beschreiben seine persönliche Berufserfahrung.</p>
    <p>Eine Ausbildung zum Softwareingenieur, die abgeschlossene sechsmonatige Spezialisierung auf KI Engineering und eine dreimonatige Schulung zum Prompt Engineer ergänzen die operative Erfahrung. Im Online-Marketing gehören SEO, Google Ads, Social Media und digitale Sichtbarkeit zu seinem Hintergrund.</p>
    <p>Mit Boriss Bockans hat Kastriot unter dem Namen TB Solutions digitale Projekte aufgebaut. Diese Erfahrung in digitalen Projekten fließt in die Weiterentwicklung des Angebots unter Tafolli &amp; Co. ein.</p></div>
    <a href="werdegang.html" class="btn btn-2" style="margin-top:18px">Beruflichen Werdegang ansehen ↗</a></div>
    <div class="pop-wrap">{portrait()}<div class="card pop ticks" style="margin-top:22px"><p class="tag" style="color:var(--acc);margin-bottom:12px">// auf einen blick</p><dl class="daten" style="margin:0">{daten}</dl></div></div>
  </div>
</div></section>
<section class="pad"><div class="shell">
  {kicker("03", "Zusammenarbeit")}
  <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px">{wipe([["Klar im Umfang."],["Persönlich im Kontakt."]])}</h2>
  <p class="lede rise" style="margin-bottom:36px">Für jedes Projekt werden ein Ansprechpartner, die erforderlichen Kompetenzen und die konkreten Verantwortlichkeiten festgelegt.</p>
  {karten_grid(haltung, "g2")}
</div></section>''' + cta_block("// nächster schritt", [["Lernen wir uns kennen."]],
        "Beschreiben Sie Ihre Aufgabe. Gemeinsam klären wir, welche Form der Zusammenarbeit zu Ihrem Unternehmen passt.",
        "Projekt besprechen", "kontakt.html", "Leistungen ansehen", "leistungen.html")
    return seite_rahmen("ueber-mich.html", "Unternehmen & Gründer · Tafolli & Co.",
        "Tafolli & Co.: Marketing, Technology, Consulting und AI Automation. Informationen zum Unternehmen, zur Zusammenarbeit und zum Gründer.",
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
        "Von der klassischen Serviceausbildung über Michelin-ausgezeichnete Restaurants bis zur Direktion von Hotelgruppen mit mehreren hundert Mitarbeitenden.",
        ["seit 2011", "7 Hauptstationen", "3 Sprachen"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Stationen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Fünfzehn Jahre,"], ["ein roter Faden."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">Vom Oberkellner im Grand Hotel Prishtina bis zur Direktion von Hotelgruppen an der Ostsee. Jede Station hat die persönliche Erfahrung von Gründer Kastriot Tafolli erweitert, die heute in die Beratung einfließt.</p>
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
        "Als Beratung, als Projekt oder als F&B-Leitung auf Zeit. Beschreiben Sie, welche Unterstützung Ihr Unternehmen benötigt.",
        "Beratungsgespräch vereinbaren", "kontakt.html", "Leistungen ansehen", "leistungen.html")

    return seite_rahmen("werdegang.html", "Werdegang · Kastriot Tafolli",
        "Stationen und Kompetenzen von Kastriot Tafolli: vom Oberkellner bis zur Direktion von Hotelgruppen, dazu Softwareentwicklung und KI Engineering.",
        "werdegang.html", inhalt)


def leistungen():
    bereiche = [
        ("01", "Marketing", "Strategie, Marke und Kommunikation für Ihr Unternehmen.",
         ["Marketingstrategie und Positionierung", "Branding und Corporate Design", "Kampagnen, Content und Social Media", "SEO, Werbung und Auswertung"], "online-marketing.html", "Marketing ansehen"),
        ("02", "Technology", "Individuelle Software und eine verlässliche technische Grundlage.",
         ["Software und Fachanwendungen", "Apps für iOS, Android und Web", "Websites, Schnittstellen und Integration", "Cybersecurity und technische Betreuung"], "softwareentwicklung.html", "Technology ansehen"),
        ("03", "Consulting", "Abläufe, Organisation und Wirtschaftlichkeit gemeinsam betrachten.",
         ["Prozess- und Betriebsberatung", "Einkauf und Lieferantenvereinbarungen", "Kalkulation und Controlling", "Hospitality- und F&B-Management"], "fb-beratung.html", "Consulting ansehen"),
        ("04", "AI Automation", "Wiederkehrende Arbeit mit geeigneten KI-Systemen vereinfachen.",
         ["KI-Assistenten und Wissenssysteme", "Automatisierte Workflows", "Daten- und Systemanbindung", "Prüfung, Freigaben und laufende Betreuung"], "ki-automatisierung.html", "AI Automation ansehen"),
    ]
    karten = "".join(f'''<article class="card pop ticks" style="--i:{i};display:flex;flex-direction:column">
      <p class="tag" style="color:var(--acc);margin-bottom:12px">{nr} / LEISTUNGSBEREICH</p>
      <h3 class="d2" style="font-size:clamp(1.6rem,2.8vw,2.3rem);margin-bottom:14px">{titel}</h3>
      <p style="color:var(--paper-dim);font-size:.95rem;margin-bottom:22px">{text}</p>
      {punkte_liste(punkte)}<a href="{href}" class="btn btn-2" style="margin-top:26px;align-self:flex-start">{cta} ↗</a>
    </article>''' for i,(nr,titel,text,punkte,href,cta) in enumerate(bereiche))
    ablauf = [
        ("01", "Aufgabe und Ziele", "Wir klären Ihre Anforderungen, Zielgruppen und bestehenden Grundlagen. Daraus entsteht eine erste Einschätzung zu Vorgehen und Umfang."),
        ("02", "Konzept und Angebot", "Sie erhalten einen abgestimmten Leistungsumfang mit Prioritäten, Kosten, Zuständigkeiten und den vorgesehenen Ergebnissen."),
        ("03", "Umsetzung und Abstimmung", "Entwicklung, Gestaltung oder Beratung erfolgen mit vereinbarten Zwischenständen. Feedback und Freigaben bleiben Teil des Ablaufs."),
        ("04", "Übergabe und Betreuung", "Ergebnisse und benötigte Dokumentation werden übergeben. Wartung, Weiterentwicklung oder laufende Betreuung können separat vereinbart werden."),
    ]
    faq = [
        ("Können wir einzelne Leistungen beauftragen?", "Ja. Ein einzelnes Thema ist ebenso möglich wie ein Projekt über mehrere Leistungsbereiche. Der Umfang richtet sich nach Ihrer Aufgabe."),
        ("Welche Anwendungen entwickeln Sie?", "Zum Angebot gehören individuelle Unternehmenssoftware, Websites, Web-Apps sowie Anwendungen für iOS und Android. Plattformen, Integrationen und Betrieb werden anhand Ihrer Anforderungen festgelegt."),
        ("Gehört Cybersecurity zum Angebot?", "Ja. Wir unterstützen die grundlegende Absicherung von Anwendungen, Websites, Zugängen und Daten sowie die Planung geeigneter Schutzmaßnahmen. Spezialisierte Prüfungen werden als eigener Umfang vereinbart."),
        ("Arbeiten Sie nur für Hotels und Gastronomie?", "Nein. Marketing, Technology und AI Automation stehen Unternehmen verschiedener Branchen offen. In der Beratung bilden Hotellerie und Gastronomie einen besonderen Erfahrungsschwerpunkt."),
        ("Ist eine laufende Betreuung möglich?", "Ja. Inhalte, Kampagnen, Software, Hosting und Automatisierungen können im vereinbarten Umfang laufend betreut und weiterentwickelt werden."),
        ("Wie beginnt die Zusammenarbeit?", "Beschreiben Sie Ihre Aufgabe und Ihr wichtigstes Ziel. Im Erstgespräch klären wir die Grundlagen und einen sinnvollen nächsten Schritt."),
    ]
    schritte = "".join(f'<article class="card rise"><p class="tag">{nr}</p><h3 class="d3" style="margin:14px 0">{t}</h3><p style="color:var(--paper-dim)">{b}</p></article>' for nr,t,b in ablauf)
    inhalt = hero_klein("03", "Leistungen", [["Vier Leistungsbereiche."], ["Ein abgestimmtes Angebot."]],
        "Marketing, Technology, Consulting und AI Automation für Unternehmen. Vom einzelnen Auftrag bis zum zusammenhängenden Projekt.",
        ["Marketing", "Technology", "Consulting", "AI Automation"]) + f'''
<section class="pad"><div class="shell">
 {kicker("01", "Leistungsbereiche")}<h2 class="d2" style="margin:20px 0 24px">Leistungen nach Ihrem Bedarf.</h2>
 <p class="lede rise" style="margin-bottom:38px">Die vier Bereiche ergänzen sich. Welche Leistungen im Projekt zusammenkommen, legen wir anhand Ihrer Anforderungen und der vorhandenen Grundlagen fest.</p>
 <div class="g2 pop-wrap">{karten}</div>
</div></section>
<section class="pad" style="background:var(--ink-2)"><div class="shell">
 {kicker("02", "Leistungen im Detail")}<h2 class="d2" style="margin:20px 0 36px">Das gesamte Angebot.</h2>{catalogue()}
</div></section>
<section class="pad"><div class="shell">
 {kicker("03", "Zusammenarbeit")}<h2 class="d2" style="margin:20px 0 36px">Von der Aufgabe zur Umsetzung.</h2><div class="g2">{schritte}</div>
</div></section>''' + faq_block("04", "Häufige Fragen", [["Fragen zur Zusammenarbeit."]], faq) + region() + cta_block(
        "// Kontakt", [["Projekt besprechen."]], "Beschreiben Sie Ihr Unternehmen, Ihre Aufgabe und das gewünschte Ergebnis.",
        "Kontakt aufnehmen", "kontakt.html", "Unternehmen kennenlernen", "ueber-mich.html")
    return seite_rahmen("leistungen.html", "Marketing, Technology, Consulting & AI Automation · Tafolli & Co.",
        "Marketing, individuelle Software und Apps, Cybersecurity, Unternehmensberatung und KI-Automatisierung: Leistungen von Tafolli & Co.", "leistungen.html", inhalt)
