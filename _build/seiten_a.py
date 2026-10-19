# -*- coding: utf-8 -*-
from bausteine import *
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
        ("01", "Praxis vor Theorie", "Ich baue, was im Alltag benutzt wird. Ich empfehle nichts, nur weil es in einer Präsentation gut aussieht."),
        ("02", "Zahlen als Grundlage", "Entscheidungen brauchen eine Basis. Ich rechne, bevor ich rate, und lege die Rechnung offen."),
        ("03", "Auf Augenhöhe", "Ich rede mit der Person, die die Arbeit macht, genauso wie mit der Geschäftsführung. Beratung heißt, mit Ihrem Team zu arbeiten."),
        ("04", "Diskretion", "Zahlen und interne Themen bleiben, wo sie hingehören. Referenzen nenne ich nur mit Zustimmung, Details nie."),
    ]
    sprache = [
        ("Albanisch", "Muttersprache. Texte und Gespräche für Betriebe in Deutschland, im Kosovo und in Albanien."),
        ("Deutsch C2", "Texte, Websites und Abstimmungen auf Deutsch."),
        ("Englisch C1", "Texte und Abstimmungen auf Englisch."),
        ("Drei Richtungen", "Deutsch, Englisch und Albanisch. Jede Richtung. Die Festpreise stehen auf der Angebotsseite."),
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
          <p>Mein Weg begann im Kosovo. 2018 bin ich an die Ostsee gekommen. Der Sitz von TB Solutions ist Ostseebad Binz.</p>
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
    <p class="lede rise" style="--i:1;margin-bottom:clamp(40px,5vw,64px)">Vier Dinge, auf die Sie sich verlassen können, ob es um eine Automatisierung, eine Website oder einen Text geht.</p>
    {karten_grid(haltung, "g2")}
  </div>
</section>

<section class="pad">
  <div class="shell">
    {kicker("03", "Ausbildung und Weiterbildung")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Zwei Welten,"],["bewusst gelernt."]])}</h2>
    <div class="g2 pop-wrap">{bildung("// sprachen", sprache, 0)}{bildung("// technik & digitales", technik, 1)}</div>
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
         "Abgeschlossene sechsmonatige Spezialisierung auf KI Engineering. Schwerpunkt: Automatisierung von Geschäftsprozessen. Dazu eine dreimonatige Schulung zum Prompt Engineer. Das ist die Grundlage für TeamO.",
         ["Prozessautomatisierung", "Prompt Engineering", "Systemintegration"]),
        ("davor", "Ausbildung Softwareingenieur", "Software und Systeme",
         "Softwareentwicklung, Datenbanken und Systemarchitektur. Darauf bauen die Websites, Web-Apps und Automationen auf, die ich heute anbiete.",
         ["Python", "JavaScript", "SQL"]),
        ("heute", "TB Solutions", "Ostseebad Binz",
         "Gemeinsam mit Boriss Bockans. KI-Automatisierung, Software, Websites und Texte auf Deutsch, Englisch und Albanisch. Projekte begleiten wir direkt.",
         ["KI", "Web", "Texte"]),
    ]
    tl = "".join(f'''<div class="tl-item rise">
        <p class="tl-jahr">{j}</p>
        <h3 class="d3" style="font-size:clamp(1.2rem,2vw,1.6rem)">{t}</h3>
        <p class="tl-ort">{o}</p>
        <p style="color:var(--paper-dim);font-size:.95rem;max-width:72ch">{d}</p>
        <div class="tl-chips">{"".join(f'<span class="chip">{c}</span>' for c in ch)}</div>
      </div>''' for j, t, o, d, ch in stationen)

    erste = [
        ("Sprachen", "Albanisch, Deutsch, Englisch", "Texte und Gespräche in diesen drei Sprachen."),
        ("Sitz", "Ostseebad Binz", "TB Solutions, Hauptstraße 1. Arbeit für Betriebe in Deutschland, Österreich, der Schweiz und im Kosovo."),
    ]
    erste_html = "".join(f'''<div class="rise" style="--i:{i};display:grid;grid-template-columns:minmax(110px,170px) 1fr;gap:18px;padding:15px 0;border-bottom:1px solid var(--line-soft)">
        <span class="mono" style="font-size:.78rem;color:var(--acc)">{j}</span>
        <span><b style="font-size:.95rem">{t}</b><span style="display:block;font-size:.86rem;color:var(--paper-mute);margin-top:3px">{o}</span></span>
      </div>''' for i, (j, t, o) in enumerate(erste))

    kompetenzen = [
        ("01", "KI und Automatisierung", "Assistenten und Abläufe für E-Mail, Angebote oder Termine. Freigabe bleibt bei Ihnen."),
        ("02", "Softwareentwicklung", "Python, JavaScript, HTML, CSS, SQL, C und C++. Datenbanken und Webanwendungen."),
        ("03", "Web-Apps", "Checklisten, Bestellungen und Freigaben auf dem Telefon. Rollen und ein klarer Status."),
        ("04", "Websites", "Kleine Seiten und Landingpages. Auf dem Telefon lesbar, mit Weg zur Anfrage."),
        ("05", "Texte", "Deutsch, Englisch und Albanisch. Festpreise 49, 59 und 99 €. Ich prüfe jeden Text selbst."),
        ("06", "Online-Marketing", "SEO, Google Ads, Social Media, Content und lokale Sichtbarkeit. Ohne Versprechen auf einen Platz in der Suche."),
    ]
    werkzeug = [
        ("// programmiersprachen", ["Python", "JavaScript", "HTML", "CSS", "SQL", "C", "C++"]),
        ("// marketing und analyse", ["Google Ads", "Analytics", "Search Console", "Meta Business", "Canva", "Adobe", "Squarespace"]),
    ]
    werkzeug_html = "".join(f'''<div class="rise" style="--i:{i};margin-bottom:26px">
        <p class="tag" style="color:var(--acc);margin-bottom:12px">{t}</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{"".join(f'<span class="chip">{c}</span>' for c in cs)}</div>
      </div>''' for i, (t, cs) in enumerate(werkzeug))

    inhalt = hero_klein("02", "Werdegang", [["Software, KI"], ["und drei Sprachen."]],
        "Was ich gelernt habe und was ich heute anbiete.",
        ["Software", "KI Engineering", "3 Sprachen"]) + f'''
<section class="pad">
  <div class="shell">
    {kicker("01", "Lernen und Angebot")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Vom Lernen"], ["zum eigenen Angebot."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">Die technische Weiterbildung und TB Solutions. Was ich heute anbiete, steht unter Leistungen: KI, Software, Web, Marketing und Texte.</p>
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
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(40px,5vw,64px)">{wipe([["Was ich"], ["heute kann."]])}</h2>
    {karten_grid(kompetenzen, "g3")}
    <div style="margin-top:clamp(48px,5vw,76px)">{werkzeug_html}</div>
  </div>
</section>''' + cta_block("// nächster schritt", [["Welches Thema"], ["soll das erste sein?"]],
        "Als Projekt oder als laufende Betreuung. Sagen Sie mir, woran es gerade hakt.",
        "Anfragen", "kontakt.html", "Leistungen ansehen", "leistungen.html")

    return seite_rahmen("werdegang.html", "Werdegang · Kastriot Tafolli",
        "Stationen und Kompetenzen von Kastriot Tafolli: Softwareentwicklung, KI Engineering und frühere Projekte.",
        "werdegang.html", inhalt)


def leistungen():
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
<section class="pad" id="fuer-wen" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker("01b", "Für wen")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([["Eine Seite"], ["pro Zielgruppe."]])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:28px">Dieselben Leistungen, zugeschnitten auf einen Betrieb. Die Preise sind dieselben wie auf den Angebotsseiten.</p>
    <div class="portfolio-links">
      <a href="website-fuer-handwerker.html">Website für Handwerker <span aria-hidden="true">↗</span></a>
      <a href="ki-automatisierung-arztpraxen.html">KI für Arztpraxen und Therapeuten <span aria-hidden="true">↗</span></a>
      <a href="website-fuer-vereine.html">Website für Vereine <span aria-hidden="true">↗</span></a>
      <a href="website-pflege-kleine-betriebe.html">Website-Pflege für kleine Betriebe <span aria-hidden="true">↗</span></a>
      <a href="onlineshop-kleine-haendler.html">Onlineshop für kleine Händler <span aria-hidden="true">↗</span></a>
      <a href="sq/faqe-dhe-perkthime.html" lang="sq">Faqe web dhe përkthime <span aria-hidden="true">↗</span></a>
      <a href="sq/automatizim-ia.html" lang="sq">Automatizim me IA <span aria-hidden="true">↗</span></a>
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
        "leistungen.html", inhalt, faq=faq)
