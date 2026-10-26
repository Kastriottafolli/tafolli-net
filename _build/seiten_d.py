# -*- coding: utf-8 -*-
from icons import icon
from bausteine import *
from hotels import hotel_cards
from partners import PROJECTS, GASTRO, TECH, tiles


def referenzen():
    inhalt = hero_klein("05", "Referenzen & Partner", [["Gute Arbeit entsteht"], ["im Zusammenspiel."]],
        "Betriebe, digitale Auftritte und ein Netzwerk aus Gastronomie und Technologie. Die Auswahl zeigt bestehende Projektbezüge und die persönliche Berufserfahrung von Gründer Kastriot Tafolli.",
        ["Eigenes Produkt & Projekte", "Gastronomie & Technologie", "6 berufliche Stationen"]) + '''
    <div class="shell"><nav class="partner-jump" aria-label="Referenzbereiche"><a href="#betriebe">Produkte & Projekte ↗</a><a href="#gastronomie">Gastronomiepartner ↗</a><a href="#technologie">Technologiepartner ↗</a><a href="#stationen">Berufliche Stationen ↗</a></nav></div>''' + f'''
<section class="pad" id="betriebe" style="scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("01", "Produkte & Projekte")}<h2 class="d2" style="margin-top:20px">Eigene Entwicklung.<br> Bestehende Verbindungen.</h2></div><p>Tafolli Boost ist unser eigenes KI-Produkt. Das Panorama Hotel Lohme gehört zu den bisherigen Projektbezügen; Gastronomie, Marken und Technologieunternehmen finden Sie gebündelt in den weiteren Bereichen.</p></div>
 {tiles(PROJECTS,projects=True)}
 <p class="tag" style="color:var(--acc);margin-top:40px">Weitere Betriebe aus der bisherigen Zusammenarbeit</p><div class="partner-more"><span>Bukowina</span><span>Bistro Cappuccino</span><span>Salsa Latino</span><span>El Restaurante</span><span>MBJ · My Jasharaj</span></div>
</div></section>
<section class="pad" id="gastronomie" style="background:var(--ink-2);scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("02", "Getränke- und Gastronomiepartner")}<h2 class="d2" style="margin-top:20px">Vom guten Einkauf<br> zum guten Geschmack.</h2></div><p>Getränke, Kaffee, Foodservice und Großhandel: Die operative Erfahrung des Gründers verbindet Sortiment, Lieferfähigkeit und wirtschaftliche Konditionen. Hier finden Sie die genannten Marken und Lieferanten direkt.</p></div>
 {tiles(GASTRO)}
</div></section>
<section class="pad" id="technologie" style="scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("03", "Technologiepartner")}<h2 class="d2" style="margin-top:20px">Technologie.<br> Zusammenarbeit.</h2></div><p>Verbindungen aus der bisherigen Zusammenarbeit und dem technischen Projektumfeld: unter anderem Google, Microsoft, OpenAI und weitere Plattformen für Marketing, Software und KI.</p></div>
 {tiles(TECH)}
</div></section>
<section class="pad" id="stationen" style="background:var(--ink-2);scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("04", "Berufliche Stationen")}<h2 class="d2" style="margin-top:20px">Berufliche Stationen<br> des Gründers.</h2></div><p>Kastriot Tafolli kennt Hotellerie aus der täglichen Verantwortung: Teams führen, Gastronomie gestalten und mehrere Häuser koordinieren. Seine persönliche Führungsverantwortung in diesen Häusern bildet eine fachliche Grundlage der heutigen Beratung.</p></div>
 {hotel_cards()}
 <div class="career-transfer"><div><p class="tag">Für Ihr nächstes Projekt</p><h3>Hotellerie verstehen.<br> Möglichkeiten umsetzen.</h3><p>Auf dieser Grundlage verbindet Tafolli &amp; Co. F&B-Beratung mit Digitalisierung und KI-Automatisierung: Lösungen, die zu Ihren Teams, Abläufen und wirtschaftlichen Zielen passen.</p></div><div class="career-transfer-actions"><a class="btn btn-1" href="kontakt.html">Über Ihren Betrieb sprechen ↗</a><a class="btn btn-2" href="fb-beratung.html">F&B-Beratung entdecken ↗</a></div></div>
 <p style="color:var(--paper-mute);font-size:.88rem;margin-top:28px;max-width:70ch">Weitere Referenzen werden auf Anfrage und nur mit Zustimmung der jeweiligen Häuser genannt. Zahlen und interne Details bleiben grundsätzlich vertraulich.</p>
</div></section>''' + cta_block("// nächster schritt", [["Gute Verbindungen."], ["Neue Möglichkeiten."]],
        "Ob gemeinsames Projekt, ein konkreter Auftrag oder eine neue Zusammenarbeit: Beschreiben Sie, was Sie bewegen möchten.",
        "Zusammenarbeit besprechen", "kontakt.html", "Leistungen ansehen", "leistungen.html")
    return seite_rahmen("referenzen.html", "Referenz-Websites & Partner · Tafolli & Co.",
        "Tafolli Boost, Panorama Hotel Lohme, Gastronomiepartner und Technologieunternehmen. Referenzen, Zusammenarbeit und berufliche Erfahrung mit direkten Links.",
        "referenzen.html", inhalt)


def kontakt():
    daten = [("Telefon", '<a href="tel:+4917664616146">0176 64616146</a>'),
             ("E-Mail", '<a href="mailto:info@tafolli.net">info@tafolli.net</a>'),
             ("Web", "tafolli.net"),
             ("Kontaktanschrift", "Hauptstraße 1, 18609 Ostseebad Binz"),
             ("Ansprechpartner", "Kastriot Tafolli"),
             ("Zusammenarbeit", "Deutschland, Österreich, Schweiz und Kosovo")]
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in daten)
    schritte = [("Sie schildern die Lage", "Sie beschreiben Ihr Unternehmen, die Aufgabe und das gewünschte Ergebnis. Vorhandene Unterlagen oder Systemübersichten können Sie ergänzen."),
                ("Wir klären den Bedarf", "Ziele, Zielgruppen, vorhandene Systeme und die wichtigsten Abläufe bilden die Grundlage für eine passende Einschätzung."),
                ("Nächste Schritte", "Sie erhalten eine Einschätzung zum Vorgehen. Leistungsumfang, Zeitplan, Zuständigkeiten und Kosten werden vor einer Beauftragung abgestimmt.")]
    pipe = ""
    for i, (t, d) in enumerate(schritte):
        pipe += f'<div class="pipe-node rise" style="--i:{i}"><i></i><b>{t}</b><span>{d}</span></div>'
        if i < len(schritte) - 1:
            pipe += f'<div class="pipe-track"><span class="pipe-particle" style="--i:{i}"></span></div>'

    inhalt = hero_klein("08", "Kontakt", [["Lassen Sie"], ["uns sprechen."]],
        "Marketing, Technologie, Beratung oder KI-Automatisierung: Beschreiben Sie Ihr Vorhaben. Wir besprechen Anforderungen, Umfang und die nächsten Schritte.",
        ["Deutschland · Österreich · Schweiz · Kosovo", "unverbindlich", "persönlich"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Ihr Projekt beginnt"], ["mit einem Gespräch."]])}</h2>
        <div class="prose rise">
          <p>Tafolli &amp; Co. begleitet Unternehmen bei digitalen und betrieblichen Aufgaben. Rufen Sie an oder beschreiben Sie kurz Ihr Vorhaben per E-Mail.</p>
          <p>Für eine gezielte Abstimmung können Sie einen Gesprächstermin mit Kastriot Tafolli vereinbaren. Kontakt, Umfang und nächste Schritte werden persönlich besprochen.</p>
        </div>
        <div class="rise" style="display:flex;flex-wrap:wrap;gap:13px;margin:8px 0 34px">
          <a href="mailto:info@tafolli.net" class="btn btn-1">E-Mail schreiben</a>
          <a href="tel:+4917664616146" class="btn btn-2">Anrufen</a>
        </div>
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">// für einen guten Einstieg</p>
          <p style="color:var(--paper-dim);font-size:.94rem">Beschreiben Sie Ihr Unternehmen, die konkrete Aufgabe und das wichtigste Ziel. Falls vorhanden, helfen ein Link zur Website oder eine kurze Übersicht der eingesetzten Systeme.</p>
        </div>
      </div>
      <div class="pop-wrap" style="position:sticky;top:110px">
        <div class="card pop ticks">
          <div class="dash-top" style="margin-bottom:8px"><span class="dot pulse"></span><span class="mono" style="font-size:.8rem">Kontakt · Tafolli &amp; Co.</span></div>
          <dl class="daten" style="margin:0">{dl}</dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker("02", "Erstgespräch")}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(48px,5.5vw,80px)">{wipe([["Was im ersten"], ["Gespräch passiert."]])}</h2>
    <div class="pipe rise">{pipe}</div>
  </div>
</section>''' + region(anchor=True) + cta_block("// nächster schritt", [["Beschreiben Sie"], ["Ihr Vorhaben."]],
        "Ihr Unternehmen, die Aufgabe und Ihr wichtigstes Ziel: Das genügt für den ersten Kontakt.",
        "E-Mail an info@tafolli.net", "mailto:info@tafolli.net", "0176 64616146", "tel:+4917664616146")
    return seite_rahmen("kontakt.html", "Kontakt · Tafolli & Co.",
        "Kontakt zu Tafolli & Co. und Ansprechpartner Kastriot Tafolli: Telefon 0176 64616146, info@tafolli.net. Besprechen Sie Ihr Projekt.",
        "kontakt.html", inhalt)


def _rechtstext(aktiv, nummer, tag, zeilen, lede, chips, koerper, titel, beschr, datei, cta_h, cta_t):
    inhalt = hero_klein(nummer, tag, zeilen, lede, chips) + f'''
<section class="pad" style="padding-top:clamp(28px,4vw,52px)">
  <div class="shell"><article class="prose rise">{koerper}</article></div>
</section>''' + cta_block("// nächster schritt", [[cta_h]], cta_t,
        "E-Mail an info@tafolli.net", "mailto:info@tafolli.net", "Zur Startseite", "index.html")
    return seite_rahmen(aktiv, titel, beschr, datei, inhalt)


def impressum():
    k = '''
<h2>Anbieter</h2>
<p>Kastriot Tafolli<br>Hauptstraße 1<br>18609 Ostseebad Binz<br>Deutschland</p>
<p>Einzelunternehmen, angemeldetes Kleingewerbe.</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="tel:+4917664616146">0176 64616146</a><br>E-Mail: <a href="mailto:info@tafolli.net">info@tafolli.net</a></p>
<h2>Umsatzsteuer</h2>
<p>Gemäß § 19 Umsatzsteuergesetz wird keine Umsatzsteuer berechnet und daher auch nicht in Rechnungen ausgewiesen.</p>
<h2>Verantwortlich für den Inhalt</h2>
<p>Verantwortlich für den Inhalt nach § 18 Absatz 2 Medienstaatsvertrag ist Kastriot Tafolli, Hauptstraße 1, 18609 Ostseebad Binz.</p>
<h2>Streitbeilegung</h2>
<p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2>
<p>Als Diensteanbieter bin ich nach den allgemeinen Gesetzen für eigene Inhalte auf diesen Seiten verantwortlich. Ich bin jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben davon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen entferne ich diese Inhalte umgehend.</p>
<h2>Haftung für Links</h2>
<p>Dieses Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Deshalb kann ich für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft, rechtswidrige Inhalte waren nicht erkennbar. Eine permanente inhaltliche Kontrolle ohne konkrete Anhaltspunkte einer Rechtsverletzung ist nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen entferne ich derartige Links umgehend.</p>
<h2>Urheberrecht</h2>
<p>Die durch mich erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen meiner schriftlichen Zustimmung. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.</p>
<p>Die auf dieser Seite genannten Marken- und Firmennamen sowie abgebildete Markenzeichen sind Eigentum der jeweiligen Inhaber. Die Nennung erfolgt ausschließlich als Hinweis auf bestehende oder vergangene Geschäftsbeziehungen und begründet keine Aussage über eine Partnerschaft im markenrechtlichen Sinne.</p>
<h2>Berufliche Tätigkeit</h2>
<p>Diese Seite stellt meine persönliche berufliche Tätigkeit dar. Die dargestellte Beratung erfolgt im Rahmen meines angemeldeten Kleingewerbes und außerhalb meiner Tätigkeit als Angestellter. Ein Zusammenhang mit meinem Arbeitgeber besteht nicht.</p>
<p style="font-size:.88rem;color:var(--paper-mute)">Dieser Text ist eine sorgfältig erstellte Vorlage, aber keine Rechtsberatung. Lassen Sie ihn vor der Veröffentlichung einmal von einer Anwältin oder einem Anwalt prüfen.</p>'''
    return _rechtstext("impressum.html", "09", "Impressum", [["Impressum."]],
        "Angaben gemäß § 5 Digitale-Dienste-Gesetz und § 18 Absatz 2 Medienstaatsvertrag.", ["Stand September 2026"], k,
        "Impressum · Kastriot Tafolli", "Impressum von tafolli.net, Kastriot Tafolli, Hauptstraße 1, 18609 Ostseebad Binz.", "impressum.html",
        "Fragen zur Seite?", "Schreiben Sie mir, ich melde mich zeitnah.")


def datenschutz():
    k = '''
<h2>Verantwortlicher</h2>
<p>Verantwortlich für die Datenverarbeitung auf dieser Website im Sinne der Datenschutz-Grundverordnung ist:</p>
<p>Kastriot Tafolli<br>Hauptstraße 1<br>18609 Ostseebad Binz<br>Telefon: <a href="tel:+4917664616146">0176 64616146</a><br>E-Mail: <a href="mailto:info@tafolli.net">info@tafolli.net</a></p>
<h2>Kurz gefasst</h2>
<p>Damit Sie nicht alles lesen müssen, hier das Wesentliche in vier Punkten:</p>
<ul>
<li>Diese Seite setzt keine Cookies und verwendet keine Analyse- oder Werbewerkzeuge.</li>
<li>Die Schriften liegen auf dem eigenen Server. Es wird keine Verbindung zu Google aufgebaut.</li>
<li>Die Berechnungen laufen lokal in Ihrem Browser. Nur wenn Sie die Beratungsanfrage ausdrücklich absenden, werden Ihre Kontaktdaten und die ausgewählte Planung übermittelt.</li>
<li>Kontakt ist per E-Mail, Telefon, Kontaktformular oder über die Beratungsanfrage im Budgetplaner möglich. Erst beim Absenden des Formulars werden Ihre Angaben und die ausgewählte Planung übermittelt.</li>
</ul>
<h2>Aufruf der Website und Server-Logfiles</h2>
<p>Diese Website wird bei GitHub Pages gehostet, einem Dienst der GitHub Inc., 88 Colin P Kelly Jr Street, San Francisco, CA 94107, USA. Beim Aufruf einer Seite werden durch den Hoster automatisch Informationen verarbeitet, die Ihr Browser übermittelt. Das sind insbesondere:</p>
<ul>
<li>die angeforderte Adresse und der Zeitpunkt des Aufrufs</li>
<li>die IP-Adresse Ihres Geräts</li>
<li>der verwendete Browser und das Betriebssystem</li>
<li>die zuvor besuchte Seite, sofern Ihr Browser diese übermittelt</li>
</ul>
<p>Diese Verarbeitung ist technisch notwendig, damit die Seite überhaupt ausgeliefert werden kann, und dient der Sicherheit und Stabilität des Betriebs. Rechtsgrundlage ist Artikel 6 Absatz 1 Buchstabe f der Datenschutz-Grundverordnung, mein berechtigtes Interesse am zuverlässigen Betrieb dieser Seite. Ich selbst habe keinen Zugriff auf diese Protokolle und werte sie nicht aus.</p>
<p>Da der Hoster seinen Sitz in den Vereinigten Staaten hat, kann eine Übermittlung von Daten in ein Drittland stattfinden. GitHub hat sich nach eigenen Angaben dem EU-US Data Privacy Framework unterworfen und setzt Standardvertragsklauseln ein. Die Datenschutzerklärung von GitHub finden Sie unter <a href="https://docs.github.com" rel="noopener">docs.github.com</a>.</p>
<h2>Schriftarten</h2>
<p>Die verwendeten Schriftarten Space Grotesk, IBM Plex Sans und JetBrains Mono sind fest auf dem Server dieser Website hinterlegt und werden von dort geladen. Es wird keine Verbindung zu Servern von Google oder anderen Anbietern aufgebaut, und es werden keine Daten an Dritte übertragen.</p>
<h2>Cookies, Analyse und Werbung</h2>
<p>Diese Website setzt keine Cookies. Es kommen keine Werkzeuge zur Reichweitenmessung, keine Analysedienste und keine Werbenetzwerke zum Einsatz. Es findet kein Profiling statt, und es werden keine Daten für Werbezwecke ausgewertet oder weitergegeben.</p>
<h2>Boosty als Wegweiser</h2>
<p>Boosty ist eine interaktive Navigationshilfe. Die Einstellungen zum Pausieren der Animation und Ausblenden der Figur werden im Sitzungsspeicher Ihres Browsers (sessionStorage) unter tafolli-boosty für die aktuelle Browsersitzung abgelegt. Diese Einstellungen werden lokal verarbeitet und nicht an einen Server übertragen.</p>
<h2>Die Rechner auf dieser Seite</h2>
<p>Auf der Seite Rechner können Sie eigene Werte eingeben, etwa die Zahl der Anrufe pro Tag oder den jährlichen Getränkeeinkauf. Diese Berechnungen laufen vollständig in Ihrem Browser ab. Es findet keine Übertragung an einen Server statt, nichts wird gespeichert, und nach dem Schließen der Seite sind Ihre Eingaben verschwunden.</p>
<h2 id="budgetplaner-datenschutz">Budgetplaner und Beratungsanfrage</h2>
<p>Die Berechnung von Budgets, Sichtkontakten, Anfragen und Kundenpotenzial läuft lokal in Ihrem Browser. Die Werte sind veränderbare Rechenannahmen. Ohne Absenden des Formulars erfolgt keine Übermittlung dieser Planung.</p>
<p>Wenn Sie das Kontaktformular oder die Beratungsanfrage im Budgetplaner absenden, werden Ihr Name, Ihre E-Mail-Adresse, freiwillige Unternehmens- und gegebenenfalls Telefonangaben sowie Ihre Nachricht über den Formularanbieter FormSubmit an info@tafolli.net übermittelt. Die Projektanfrage enthält außerdem das ausgewählte Thema und den gewünschten Zeitraum. Bei einer Anfrage aus dem Budgetplaner werden zusätzlich die ausgewählten Leistungen, Budgets, Annahmen und Rechenergebnisse übermittelt. Eine Verbindung zu FormSubmit wird erst beim Absenden aufgebaut. FormSubmit verarbeitet die Anfrage zur Zustellung und hält Formulareingänge nach eigener Dokumentation bis zu 30 Tage vor. Weitere Informationen: <a href="https://formsubmit.co/documentation" target="_blank" rel="noopener noreferrer">FormSubmit-Dokumentation</a>.</p>
<h2>Kontaktaufnahme</h2>
<p>Wenn Sie mich per E-Mail, telefonisch oder über die Beratungsanfrage kontaktieren, verarbeite ich die von Ihnen mitgeteilten Daten, um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Artikel 6 Absatz 1 Buchstabe b der Datenschutz-Grundverordnung, soweit es um die Anbahnung oder Durchführung eines Vertrags geht, sonst Artikel 6 Absatz 1 Buchstabe f, mein berechtigtes Interesse an der Beantwortung von Anfragen.</p>
<p>Ihre Anfrage und die zugehörige Korrespondenz bewahre ich auf, solange sie für die Bearbeitung erforderlich ist. Danach lösche ich sie, sofern keine gesetzlichen Aufbewahrungsfristen entgegenstehen. Für Geschäftsbriefe gelten die handels- und steuerrechtlichen Fristen von sechs beziehungsweise zehn Jahren.</p>
<h2>Verschlüsselung</h2>
<p>Diese Website wird über eine verschlüsselte Verbindung ausgeliefert, erkennbar am Schlosssymbol in der Adresszeile Ihres Browsers und an der Adresse, die mit https beginnt. Damit können die Daten, die Sie an diese Seite übermitteln, nicht von Dritten mitgelesen werden.</p>
<h2>Ihre Rechte</h2>
<p>Sie haben jederzeit das Recht auf:</p>
<ul>
<li>Auskunft über die zu Ihrer Person gespeicherten Daten nach Artikel 15</li>
<li>Berichtigung unrichtiger Daten nach Artikel 16</li>
<li>Löschung Ihrer Daten nach Artikel 17</li>
<li>Einschränkung der Verarbeitung nach Artikel 18</li>
<li>Datenübertragbarkeit nach Artikel 20</li>
<li>Widerspruch gegen eine Verarbeitung auf Grundlage berechtigter Interessen nach Artikel 21</li>
</ul>
<p>Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Wenden Sie sich dafür formlos an <a href="mailto:info@tafolli.net">info@tafolli.net</a>.</p>
<h2>Beschwerderecht</h2>
<p>Wenn Sie der Ansicht sind, dass die Verarbeitung Ihrer Daten gegen das Datenschutzrecht verstößt, können Sie sich bei einer Aufsichtsbehörde beschweren. Zuständig ist:</p>
<p>Der Landesbeauftragte für Datenschutz und Informationsfreiheit<br>Mecklenburg-Vorpommern<br>Werderstraße 74 a, 19055 Schwerin</p>
<h2>Änderungen</h2>
<p>Ich passe diese Datenschutzerklärung an, sobald sich die Seite technisch ändert oder neue rechtliche Vorgaben das erfordern. Es gilt jeweils die hier veröffentlichte Fassung.</p>
'''
    return _rechtstext("datenschutz.html", "10", "Datenschutz", [["Datenschutz&shy;erklärung."]],
        "Diese Seite kommt ohne Cookies, ohne Tracking und ohne Werbenetzwerke aus. Was trotzdem an Daten anfällt, steht hier vollständig.",
        ["keine Cookies", "kein Tracking", "Stand Oktober 2026"], k,
        "Datenschutzerklärung · Kastriot Tafolli", "Datenschutzerklärung von tafolli.net: keine Cookies, kein Tracking, Schriften auf dem eigenen Server.", "datenschutz.html",
        "Noch Fragen offen?", "Wenn etwas unklar ist, schreiben Sie mir. Ich erkläre es Ihnen.")


def fehler404():
    return f'''{seiten_kopf("Seite nicht gefunden · Tafolli & Co.", "Diese Seite gibt es nicht.", "404.html").replace('<meta name="author"', '<meta name="robots" content="noindex">\n<meta name="author"').replace('href="assets/', 'href="/assets/')}
<body>
{kopfzeile("404.html", "/")}
<main style="min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden">
  <div class="shell" style="position:relative;z-index:1">
    <p class="tag"><span class="n">//</span>&nbsp;&nbsp;404</p>
    <h1 class="d1" style="margin:20px 0 24px;font-size:clamp(2.8rem,8vw,6.5rem)">Diese Seite<br>gibt es nicht.</h1>
    <p class="lede" style="margin-bottom:34px">Vielleicht hat sich die Adresse geändert. Von der Startseite aus finden Sie alles Weitere.</p>
    <div style="display:flex;flex-wrap:wrap;gap:13px">
      <a href="/" class="btn btn-1">Zur Startseite</a>
      <a href="/kontakt.html" class="btn btn-2">Kontakt</a>
    </div>

  </div>
</main>
<script src="/assets/navigation.js?v={VER}" defer></script>
<script src="/assets/kt.js?v={VER}" defer></script>
</body>
</html>
'''
