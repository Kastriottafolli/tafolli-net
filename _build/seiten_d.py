# -*- coding: utf-8 -*-
from icons import icon
from bausteine import *
from hotels import hotel_cards
from partners import PROJECTS, GASTRO, TECH, tiles


def referenzen():
    inhalt = hero_klein("05", "Referenzen & Partner", [["Gute Arbeit entsteht"], ["im Zusammenspiel."]],
        "Betriebe, digitale Auftritte und ein Netzwerk aus Gastronomie und Technologie. Entdecken Sie die Menschen, Marken und Plattformen hinter meiner Arbeit.",
        ["6 Referenz-Websites", "30 Marken & Partner", "6 berufliche Stationen"]) + '''
    <div class="shell"><nav class="partner-jump" aria-label="Referenzbereiche"><a href="#betriebe">Referenz-Websites ↗</a><a href="#gastronomie">Gastronomiepartner ↗</a><a href="#technologie">Technologiepartner ↗</a><a href="#stationen">Berufliche Stationen ↗</a></nav></div>''' + f'''
<section class="pad" id="betriebe" style="scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("01", "Betriebe & Referenz-Websites")}<h2 class="d2" style="margin-top:20px">Betriebe, die ich mit<br> TB Solutions begleite.</h2></div><p>Eine Auswahl zum direkten Entdecken: Bau, Glas, Gastronomie und Hotellerie. Tafolli Glass ergänzt das Netzwerk als Partner; tafolli.net zeigt meinen eigenen digitalen Auftritt.</p></div>
 {tiles(PROJECTS,projects=True)}
 <p class="tag" style="color:var(--acc);margin-top:40px">Weitere Betriebe aus meiner Zusammenarbeit</p><div class="partner-more"><span>Bukowina</span><span>Bistro Cappuccino</span><span>Salsa Latino</span><span>El Restaurante</span><span>MBJ · My Jasharaj</span></div>
</div></section>
<section class="pad" id="gastronomie" style="background:var(--ink-2);scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("02", "Getränke- und Gastronomiepartner")}<h2 class="d2" style="margin-top:20px">Vom guten Einkauf<br> zum guten Geschmack.</h2></div><p>Getränke, Kaffee, Foodservice und Großhandel: Mein F&B-Alltag verbindet Sortiment, Lieferfähigkeit und wirtschaftliche Konditionen. Hier finden Sie die genannten Marken und Lieferanten direkt.</p></div>
 {tiles(GASTRO)}
</div></section>
<section class="pad" id="technologie" style="scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("03", "Technologiepartner")}<h2 class="d2" style="margin-top:20px">Die Werkzeuge.<br> Die Möglichkeiten.</h2></div><p>KI, Software, Sichtbarkeit und Infrastruktur. Diese Plattformen und Werkzeuge gehören zu meinem digitalen Arbeitsumfeld. Welche davon in Ihrem Projekt sinnvoll sind, entscheidet der konkrete Bedarf.</p></div>
 {tiles(TECH)}
</div></section>
<section class="pad" id="stationen" style="background:var(--ink-2);scroll-margin-top:110px"><div class="shell">
 <div class="partner-section-intro"><div>{kicker("04", "Berufliche Stationen")}<h2 class="d2" style="margin-top:20px">Häuser, für die ich<br> Verantwortung getragen habe.</h2></div><p>Ich kenne Hotellerie aus der täglichen Verantwortung: Teams führen, Gastronomie gestalten und mehrere Häuser koordinieren. Diese Erfahrung bringe ich in Ihre Beratung ein – mit Verständnis für Ihre Gäste, Ihre Mitarbeitenden und die Wirtschaftlichkeit Ihres Betriebs.</p></div>
 {hotel_cards()}
 <div class="career-transfer"><div><p class="tag">Für Ihr nächstes Projekt</p><h3>Hotellerie verstehen.<br> Möglichkeiten umsetzen.</h3><p>Auf dieser Grundlage verbinde ich F&B-Beratung mit Digitalisierung und KI-Automatisierung: Lösungen, die zu Ihren Teams, Abläufen und wirtschaftlichen Zielen passen.</p></div><div class="career-transfer-actions"><a class="btn btn-1" href="kontakt.html">Über Ihren Betrieb sprechen ↗</a><a class="btn btn-2" href="fb-beratung.html">F&B-Beratung entdecken ↗</a></div></div>
 <p style="color:var(--paper-mute);font-size:.88rem;margin-top:28px;max-width:70ch">Weitere Referenzen nenne ich auf Anfrage und nur mit Zustimmung der jeweiligen Häuser. Zahlen und interne Details bleiben grundsätzlich vertraulich.</p>
</div></section>''' + cta_block("// nächster schritt", [["Gute Verbindungen."], ["Neue Möglichkeiten."]],
        "Ob gemeinsames Projekt, ein konkreter Auftrag oder eine neue Zusammenarbeit: Erzählen Sie mir, was Sie bewegen möchten.",
        "Zusammenarbeit besprechen", "kontakt.html", "Leistungen ansehen", "leistungen.html")
    return seite_rahmen("referenzen.html", "Referenz-Websites & Partner · Kastriot Tafolli",
        "Referenz-Websites von A&B Bau, Tafolli Glass, Restaurant Wochenmarkt, MEL und Panorama Hotel Lohme. Gastronomie- und Technologiepartner mit Logos und Links.",
        "referenzen.html", inhalt)


def kontakt():
    daten = [("Telefon", '<a href="tel:+4917664616146">0176 64616146</a>'),
             ("E-Mail", '<a href="mailto:info@tafolli.net">info@tafolli.net</a>'),
             ("Web", "tafolli.net"),
             ("TB Solutions", "Hauptstraße 1, 18609 Ostseebad Binz"),
             ("Zweiter Standort", "Schluchsee, Hochschwarzwald"),
             ("Erreichbarkeit", "Vormittags und abends ab 22 Uhr, Rückruf am selben Tag"),
             ("Team", "Gemeinsam mit Boriss Bockans, TB Solutions")]
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in daten)
    schritte = [("Sie schildern die Lage", "Art des Betriebs, Größe, was gerade nicht läuft. Zahlen brauchen Sie dafür nicht parat zu haben."),
                ("Ich stelle Fragen", "Meist sind es zehn bis fünfzehn, zu Einkauf, Karte, Team, Sichtbarkeit und Systemen. Daran merken Sie schnell, ob ich das Geschäft kenne."),
                ("Ehrliche Einschätzung", "Wo Potenzial liegt, wo nicht, was zuerst angegangen werden sollte und ob sich eine Zusammenarbeit überhaupt lohnt. Auch wenn die Antwort nein lautet.")]
    pipe = ""
    for i, (t, d) in enumerate(schritte):
        pipe += f'<div class="pipe-node rise" style="--i:{i}"><i></i><b>{t}</b><span>{d}</span></div>'
        if i < len(schritte) - 1:
            pipe += f'<div class="pipe-track"><span class="pipe-particle" style="--i:{i}"></span></div>'

    inhalt = hero_klein("08", "Kontakt", [["Lassen Sie"], ["uns sprechen."]],
        "Ob F&amp;B-Beratung, Website, Kampagne, KI-Automatisierung oder TeamO: Der erste Schritt ist immer ein Gespräch, und das kostet nichts.",
        ["Deutschland · Österreich · Schweiz · Kosovo", "unverbindlich", "persönlich"]) + f'''
<section class="pad">
  <div class="shell">
    <div class="split" style="align-items:start;gap:clamp(36px,5vw,90px)">
      <div>
        <h2 class="d2 wipe recede-exit" style="font-size:clamp(1.8rem,3.6vw,3rem);margin-bottom:30px">{wipe([["Ein Gespräch, dreißig Minuten,"], ["unverbindlich."]])}</h2>
        <div class="prose rise">
          <p>Ich bin immer offen für ein unverbindliches Gespräch, ganz gleich ob es um eine Beratung, ein Digitalprojekt oder eine neue Zusammenarbeit geht. Rufen Sie an oder schreiben Sie kurz, worum es geht, ich melde mich zeitnah.</p>
          <p>Am besten erreichen Sie mich vormittags oder nach 22 Uhr. Wenn ich nicht drangehe, bin ich im Service und rufe zurück.</p>
        </div>
        <div class="rise" style="display:flex;flex-wrap:wrap;gap:13px;margin:8px 0 34px">
          <a href="mailto:info@tafolli.net" class="btn btn-1">E-Mail schreiben</a>
          <a href="tel:+4917664616146" class="btn btn-2">Anrufen</a>
        </div>
        <div class="card pop ticks">
          <p class="tag" style="color:var(--acc);margin-bottom:12px">// womit Sie mir helfen</p>
          <p style="color:var(--paper-dim);font-size:.94rem">Schreiben Sie mir kurz: Art des Betriebs, Anzahl der Outlets oder Zimmer, und woran es gerade konkret hakt. Dann kann ich im ersten Gespräch schon etwas Brauchbares sagen statt nur Fragen zu stellen.</p>
        </div>
      </div>
      <div class="pop-wrap" style="position:sticky;top:110px">
        <div class="card pop ticks">
          <div class="dash-top" style="margin-bottom:8px"><span class="dot pulse"></span><span class="mono" style="font-size:.8rem">erreichbar · TB Solutions</span></div>
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
    {zitat_block("Ich bin immer offen für ein unverbindliches Gespräch.", "Kastriot Tafolli")}
  </div>
</section>''' + region(anchor=True) + cta_block("// nächster schritt", [["Schreiben Sie mir"], ["zwei Sätze."]],
        "Art des Betriebs und woran es hakt. Mehr brauche ich für den Anfang nicht.",
        "E-Mail an info@tafolli.net", "mailto:info@tafolli.net", "0176 64616146", "tel:+4917664616146")
    return seite_rahmen("kontakt.html", "Kontakt · Kastriot Tafolli",
        "Kontakt zu Kastriot Tafolli und TB Solutions: Telefon 0176 64616146, info@tafolli.net. Erstgespräch unverbindlich, Rückruf am selben Tag.",
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
<li>Die Rechner auf der Seite laufen vollständig in Ihrem Browser. Ihre Eingaben verlassen Ihr Gerät nicht und werden nirgends gespeichert.</li>
<li>Es gibt kein Kontaktformular. Wenn Sie mir schreiben, tun Sie das über Ihr eigenes E-Mail-Programm oder Telefon.</li>
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
<h2>Die Logo-Animation</h2>
<p>Die kurze Logo-Animation erscheint bei jedem Seitenaufruf und läuft vollständig in Ihrem Browser. Dafür werden keine Daten gespeichert oder an einen Server übertragen. Wenn Sie in Ihrem Gerät reduzierte Bewegung eingestellt haben, wird die Animation übersprungen.</p>
<h2>Die Rechner auf dieser Seite</h2>
<p>Auf der Seite Rechner können Sie eigene Werte eingeben, etwa die Zahl der Anrufe pro Tag oder den jährlichen Getränkeeinkauf. Diese Berechnungen laufen vollständig in Ihrem Browser ab. Es findet keine Übertragung an einen Server statt, nichts wird gespeichert, und nach dem Schließen der Seite sind Ihre Eingaben verschwunden.</p>
<h2>Kontaktaufnahme</h2>
<p>Wenn Sie mir per E-Mail oder telefonisch schreiben, verarbeite ich die von Ihnen mitgeteilten Daten, um Ihre Anfrage zu beantworten. Rechtsgrundlage ist Artikel 6 Absatz 1 Buchstabe b der Datenschutz-Grundverordnung, soweit es um die Anbahnung oder Durchführung eines Vertrags geht, sonst Artikel 6 Absatz 1 Buchstabe f, mein berechtigtes Interesse an der Beantwortung von Anfragen.</p>
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
<p style="font-size:.88rem;color:var(--paper-mute)">Dieser Text beschreibt den tatsächlichen Stand dieser Website und ist sorgfältig erstellt, aber keine Rechtsberatung. Sobald Sie etwas hinzufügen, das Daten erhebt, etwa ein Kontaktformular, einen Newsletter, eine Kartendarstellung oder ein Buchungswerkzeug, muss diese Erklärung ergänzt werden. Sagen Sie mir Bescheid, dann schreibe ich den passenden Abschnitt.</p>'''
    return _rechtstext("datenschutz.html", "10", "Datenschutz", [["Datenschutz&shy;erklärung."]],
        "Diese Seite kommt ohne Cookies, ohne Tracking und ohne Werbenetzwerke aus. Was trotzdem an Daten anfällt, steht hier vollständig.",
        ["keine Cookies", "kein Tracking", "Stand Oktober 2026"], k,
        "Datenschutzerklärung · Kastriot Tafolli", "Datenschutzerklärung von tafolli.net: keine Cookies, kein Tracking, Schriften auf dem eigenen Server.", "datenschutz.html",
        "Noch Fragen offen?", "Wenn etwas unklar ist, schreiben Sie mir. Ich erkläre es Ihnen.")


def fehler404():
    return f'''{seiten_kopf("Seite nicht gefunden · Kastriot Tafolli", "Diese Seite gibt es nicht.", "404.html").replace('<meta name="author"', '<meta name="robots" content="noindex">\n<meta name="author"').replace('href="assets/', 'href="/assets/')}
<body>
{intro("de", "/")}
{kopfzeile("404.html", "/")}
<div class="grain" aria-hidden="true"></div>
<main style="min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden">
  <div class="floor"></div>
  <div class="glow" style="width:560px;height:560px;background:rgba(0,224,140,.1);top:-200px;right:-160px"></div>
  <div class="shell" style="position:relative;z-index:1">
    <p class="tag"><span class="n">//</span>&nbsp;&nbsp;404</p>
    <h1 class="d1" style="margin:20px 0 24px;font-size:clamp(2.8rem,8vw,6.5rem)">Diese Seite<br>gibt es nicht.</h1>
    <p class="lede" style="margin-bottom:34px">Vielleicht hat sich die Adresse geändert. Von der Startseite aus finden Sie alles Weitere.</p>
    <div style="display:flex;flex-wrap:wrap;gap:13px">
      <a href="/" class="btn btn-1">Zur Startseite</a>
      <a href="/kontakt.html" class="btn btn-2">Kontakt</a>
    </div>
    <pre class="mono" style="margin:48px 0 0;font-size:.78rem;color:var(--paper-mute)">$ curl tafolli.net{{pfad}}
<span style="color:var(--acc)">{icon('dot')} 404 · nicht gefunden</span></pre>
  </div>
</main>
<script>(function(){{var p=document.querySelector('pre');if(p)p.innerHTML=p.innerHTML.replace('{{pfad}}',location.pathname.replace(/[<>&]/g,''));}})();</script>
<script src="/assets/navigation.js?v={VER}" defer></script>
<script src="/assets/brand.js?v={VER}" defer></script>
<script src="/assets/kt.js?v={VER}" defer></script>
</body>
</html>
'''
