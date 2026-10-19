# -*- coding: utf-8 -*-
"""Eine Seite pro Suchbegriff. Preise bleiben die schon veröffentlichten."""
from bausteine import cta_block, faq_block, hero_klein, karten_grid, kicker, punkte_liste, seite_rahmen, wipe
from seo import PAGE_META, SERVICE_META

KI_ALT = [
    ('de', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
    ('sq', 'https://tafolli.net/sq/automatizim-ia.html'),
    ('x-default', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
]
TEXT_ALT = [
    ('de', 'https://tafolli.net/angebot/'),
    ('sq', 'https://tafolli.net/sq/faqe-dhe-perkthime.html'),
    ('x-default', 'https://tafolli.net/angebot/'),
]

for _key in (
    'website-fuer-handwerker', 'ki-automatisierung-arztpraxen', 'website-fuer-vereine',
    'website-pflege-kleine-betriebe', 'onlineshop-kleine-haendler'):
    _title, _desc = SERVICE_META[_key]
    if len(_title) > 60 or len(_desc) > 155:
        raise SystemExit(f'{_key}: title {len(_title)}, description {len(_desc)}')
for _path in ('sq/faqe-dhe-perkthime.html', 'sq/automatizim-ia.html'):
    _title, _desc = PAGE_META[_path]
    if len(_title) > 60 or len(_desc) > 155:
        raise SystemExit(f'{_path}: title {len(_title)}, description {len(_desc)}')


def _aktionen(anfrage='Anfragen', rechner='Zum Rechner', base=''):
    return f'''<div class="rise" style="display:flex;flex-wrap:wrap;gap:13px;margin-top:22px">
      <a class="btn btn-1" href="{base}kontakt.html">{anfrage}</a>
      <a class="btn btn-2" href="{base}rechner.html">{rechner}</a>
    </div>'''


def _links(paare):
    items = ''.join(f'<a href="{href}">{label} <span aria-hidden="true">↗</span></a>' for href, label in paare)
    return f'<section class="pad"><div class="shell"><p class="tag">Das passt dazu</p><h2 class="d2" style="margin:14px 0 22px">Weiter auf tafolli.net</h2><div class="portfolio-links">{items}</div></div></section>'


def _seite(pfad, inhalt, faq, **kwargs):
    return seite_rahmen(pfad, '', '', pfad, inhalt, faq=faq, **kwargs)


def handwerker():
    faq = [
        ('Was kostet eine Website für einen Handwerksbetrieb?', 'Den Preis für die Website nenne ich, wenn der Umfang klar ist. Das ist ein Festpreis-Angebot auf Anfrage. Einen Betrag vor diesem Gespräch nenne ich nicht.'),
        ('Was kostet ein Text für die Seite?', 'Ein Website-Text kostet 59 €. Das sind bis etwa 500 Wörter, zum Beispiel die Startseite. Mehrere Seiten zusammen sind das Content-Paket für 99 €, bis etwa 1.000 Wörter.'),
        ('Kann die Seite auf dem Telefon bedient werden?', 'Ja. Nummer, Leistungen und Einsatzgebiet müssen auf dem Telefon sofort zu finden sein. Das prüfe ich vor dem Start.'),
        ('Wer ändert später einen Satz?', 'Sie können mich dafür beauftragen. Die Pflege ist ein eigener Auftrag. Was dazu gehört und was es kostet, schreibe ich vorher auf.'),
        ('Bauen Sie auch einen Shop für Ersatzteile?', 'Ein kleiner Shop ist ein eigenes Angebot. Schauen Sie auf die Seite für kleine Händler, wenn Sie Waren verkaufen wollen.'),
    ]
    inhalt = hero_klein(
        '01', 'Für Handwerker',
        [['Website'], ['für Handwerker.']],
        'Kunden suchen Ihren Betrieb auf dem Telefon. Sie wollen sehen, was Sie machen, wo Sie hinfahren und wie sie Sie erreichen.',
        ['Festpreis nach Umfang', 'Texte 59 € und 99 €', 'Anfrage auf dem Telefon'],
    ) + _aktionen() + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Was oft hakt')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Die Arbeit ist da.'], ['Die Seite sagt es nicht.']])}</h2>
    <div class="prose rise">
      <p>Jemand sucht einen Elektriker, eine Malerin oder einen Schreiner. Die Seite zeigt ein altes Logo und keine Leistungen.</p>
      <p>Das Einsatzgebiet fehlt. Die Telefonnummer ist klein. Ein Foto von der fertigen Arbeit gibt es nicht.</p>
      <p>Anfragen laufen nur über einen Messenger. Am Abend sieht die niemand.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Pakete')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Was es kostet.'], ['Nur die Preise, die schon gelten.']])}</h2>
    {karten_grid([
        ('01', 'Kleine Website', 'Seiten für Leistungen, Einsatzgebiet und Kontakt. Den Festpreis schreibe ich auf, wenn klar ist, wie viele Seiten es sind und ob die Texte schon da sind.'),
        ('02', 'Website-Text · 59 €', 'Bis etwa 500 Wörter. Zum Beispiel die Startseite: was Sie tun, für wen, und wie man Sie ruft. Eine Korrekturrunde. Lieferzeit: 3 Werktage.'),
        ('03', 'Content-Paket · 99 €', 'Bis etwa 1.000 Wörter, mehrere Seiten zusammen. Eine Korrekturrunde. Lieferzeit: 5 Werktage. Eine weitere Sprache kostet 79 € dazu.'),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Die Pflege danach ist kein Teil dieser Preise. Den Umfang der Pflege nenne ich extra, bevor Sie zusagen.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Das bekommen Sie')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Konkret.'], ['Nicht ein Stapel Folien.']])}</h2>
    {punkte_liste([
        'Eine Seite, die auf dem Telefon lesbar ist',
        'Leistungen in klaren Sätzen, ohne Werbesprache',
        'Einsatzgebiet und Kontakt oben auf der Seite',
        'Ein Weg zur Anfrage per E-Mail',
        'Texte, die ich selbst lese, bevor sie online gehen',
        'Den Preis schriftlich, bevor die Arbeit startet',
    ])}
  </div>
</section>''' + faq_block('05', 'Häufige Fragen', [['Kurz'], ['beantwortet.']], faq) + _links([
        ('landingpage-erstellen-lassen.html', 'Landingpage erstellen lassen'),
        ('webdesign.html', 'Webdesign'),
        ('angebot/', 'Texte und Übersetzungen'),
        ('website-pflege-kleine-betriebe.html', 'Website-Pflege für kleine Betriebe'),
        ('onlineshop-kleine-haendler.html', 'Onlineshop für kleine Händler'),
        ('rechner.html', 'Rechner'),
    ]) + cta_block('// nächster schritt', [['Welche Leistung'], ['soll auf der Seite stehen?']],
        'Schreiben Sie mir Ihren Beruf und Ihren Ort. Danach bekommen Sie ein Festpreis-Angebot.',
        'Anfragen', 'kontakt.html', 'Zum Rechner', 'rechner.html')
    return _seite('website-fuer-handwerker.html', inhalt, faq)


def praxen():
    faq = [
        ('Nehmen Sie Patientendaten in die KI?', 'Nein. Diese Seite ist für Termine und E-Mails. Befunde, Akten und Gesundheitsdaten gehören nicht in den Ablauf.'),
        ('Was kostet die erste Automatisierung?', 'Festpreis-Angebot auf Anfrage. Den Preis nenne ich, wenn klar ist, ob es um E-Mail oder um Termine geht und welches Programm Sie nutzen.'),
        ('Geht eine Antwort allein an die Patientin?', 'Nein. Was nach außen geht, legen Sie frei. Ohne Ihre Freigabe wird nichts gesendet und kein Termin fest gebucht.'),
        ('Ist das eine medizinische oder rechtliche Beratung?', 'Nein. Ich richte einen technischen Ablauf ein. Ob der Ablauf zu Ihren Pflichten passt, klärt eine dafür zuständige Stelle.'),
        ('Können Therapeuten denselben Start nutzen?', 'Ja. Auch hier geht es um Terminanfragen und kurze Mails. Nicht um Behandlungsdaten.'),
        ('Brauchen wir dafür eine neue Website?', 'Nein. Der Ablauf kann an die Mail und den Kalender ansetzen, die Sie schon haben. Eine neue Seite ist ein eigener Auftrag.'),
    ]
    inhalt = hero_klein(
        '02', 'Für Praxen',
        [['KI-Automatisierung'], ['für Praxen und Therapeuten.']],
        'Am Empfang klingelt das Telefon, während jemand in der Behandlung ist. Die gleichen Fragen kommen noch einmal per E-Mail.',
        ['Termine und E-Mail', 'Freigabe bleibt bei Ihnen', 'keine Patientendaten'],
    ) + _aktionen() + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Was Zeit frisst')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Dieselbe Frage.'], ['Immer wieder.']])}</h2>
    <div class="prose rise">
      <p>Jemand fragt nach einem Termin. Jemand sagt einen Termin ab. Jemand schickt eine Mail mit drei kurzen Fragen.</p>
      <p>Das sind feste Abläufe. Trotzdem tippt sie jemand von Hand, zwischen zwei Behandlungen.</p>
      <p>Gesundheitsdaten haben in so einem Ablauf nichts zu suchen. Darum bleibt der Start bei Termin und E-Mail.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Paket')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Ein Ablauf.'], ['Ein Festpreis.']])}</h2>
    {karten_grid([
        ('01', 'E-Mail vorbereiten', 'Eingehende Mails werden sortiert. Ein Antwortentwurf liegt bereit. Sie lesen ihn und entscheiden, was rausgeht.'),
        ('02', 'Termin vorbereiten', 'Eine Terminanfrage wird gesammelt. Ein Vorschlag steht da. Gebucht wird der Termin erst, wenn Sie ihn freigeben.'),
        ('03', 'Festpreis-Angebot auf Anfrage', 'Es gibt hier keinen Listenpreis. Ich schreibe den Umfang und den Preis auf, nachdem der Ablauf und die Anbindung klar sind.'),
    ], 'g3')}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Texte für die Praxis-Website sind ein anderes Angebot: 59 € für einen Website-Text, 99 € für ein Content-Paket. Die stehen auf der Angebotsseite.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Das bekommen Sie')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Ein enger Rahmen.'], ['Absichtlich.']])}</h2>
    {punkte_liste([
        'Einen ersten Ablauf, nicht ein ganzes System',
        'Entwürfe für E-Mail oder Termin',
        'Eine Freigabe, bevor etwas rausgeht',
        'Keine Befunde und keine Akten im Ablauf',
        'Eine schriftliche Grenze, was die KI nicht tun soll',
        'Den Festpreis, bevor die Einrichtung startet',
    ])}
  </div>
</section>''' + faq_block('05', 'Häufige Fragen', [['Vor dem'], ['ersten Ablauf.']], faq) + _links([
        ('ki-automatisierung-kleine-unternehmen.html', 'KI Automatisierung für kleine Unternehmen'),
        ('ki-automatisierung.html', 'KI-Automatisierung'),
        ('sq/automatizim-ia.html', 'Automatizim me IA auf Albanisch'),
        ('angebot/', 'Texte und Übersetzungen'),
        ('rechner.html', 'Rechner'),
    ]) + cta_block('// nächster schritt', [['E-Mail oder Termin.'], ['Was soll der erste Schritt sein?']],
        'Schreiben Sie mir, welches Programm Sie für Mail und Kalender nutzen. Patientendaten brauchen Sie mir nicht zu schicken.',
        'Anfragen', 'kontakt.html', 'Zum Rechner', 'rechner.html')
    return _seite('ki-automatisierung-arztpraxen.html', inhalt, faq)


def vereine():
    faq = [
        ('Was kostet eine Website für einen Verein?', 'Festpreis-Angebot auf Anfrage. Der Preis hängt davon ab, wie viele Seiten es sind und ob Texte schon vorliegen.'),
        ('Was kostet der Text für die Startseite?', '59 €. Das ist ein Website-Text bis etwa 500 Wörter, mit einer Korrekturrunde. Lieferzeit: 3 Werktage.'),
        ('Wir haben mehrere Seiten: Vorstand, Termine, Mitgliedschaft.', 'Dafür gibt es das Content-Paket für 99 €, bis etwa 1.000 Wörter. Eine weitere Sprache kostet 79 € dazu.'),
        ('Kann der Vorstand später selbst einen Termin ändern?', 'Ja, wenn wir das so einrichten. Sonst übernehme ich die Änderung als Pflege. Den Umfang schreibe ich vorher auf.'),
        ('Müssen wir ein großes System kaufen?', 'Nein. Für viele Vereine reicht eine kleine Seite mit Kontakt und den nächsten Terminen.'),
    ]
    inhalt = hero_klein(
        '03', 'Für Vereine',
        [['Website'], ['für Vereine.']],
        'Mitglieder und Gäste des Vereins suchen Termine, den Vorstand und einen Weg zur Mitgliedschaft. Oft steht das nur in einer alten PDF.',
        ['Festpreis nach Umfang', 'Texte 59 € und 99 €', 'kleine Seite reicht oft'],
    ) + _aktionen() + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Was liegen bleibt')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Das Ehrenamt hat'], ['wenig Abend übrig.']])}</h2>
    <div class="prose rise">
      <p>Der nächste Termin steht im Chat, nicht auf der Seite.</p>
      <p>Wer mitmachen will, findet keine Adresse. Die Satzung liegt als Datei, die auf dem Telefon schlecht aufgeht.</p>
      <p>Niemand im Vorstand will ein Programm lernen, nur um einen Satz zu ändern.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Pakete')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Klein starten.'], ['Preise bleiben.']])}</h2>
    {karten_grid([
        ('01', 'Vereinsseite', 'Start, Termine, Kontakt, Mitgliedschaft. Den Festpreis nenne ich, wenn die Seitenzahl klar ist. Es gibt keinen Preis von der Stange für die ganze Seite.'),
        ('02', 'Website-Text · 59 €', 'Ein Text bis etwa 500 Wörter. Zum Beispiel „Über den Verein“ oder die Startseite. Eine Korrekturrunde. 3 Werktage.'),
        ('03', 'Content-Paket · 99 €', 'Mehrere Texte zusammen, bis etwa 1.000 Wörter. Eine Korrekturrunde. 5 Werktage.'),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Ein kurzes Dokument, zum Beispiel ein Hinweisblatt, ist die Übersetzung für 49 €. Das gilt, wenn der Text schon da ist und nur in eine andere Sprache soll.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Das bekommen Sie')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Eine Seite,'], ['die jemand pflegen kann.']])}</h2>
    {punkte_liste([
        'Klare Seiten statt einer langen PDF',
        'Termine und Kontakt ohne Umweg',
        'Einen Text zur Mitgliedschaft',
        'Eine Darstellung, die auf dem Telefon lesbar ist',
        'Eine Absprache, wer später Sätze ändert',
        'Den Preis, bevor der Vorstand ja sagt',
    ])}
  </div>
</section>''' + faq_block('05', 'Häufige Fragen', [['Für den'], ['Vorstand.']], faq) + _links([
        ('landingpage-erstellen-lassen.html', 'Landingpage erstellen lassen'),
        ('angebot/', 'Texte und Übersetzungen'),
        ('website-pflege-kleine-betriebe.html', 'Website-Pflege für kleine Betriebe'),
        ('website-fuer-handwerker.html', 'Website für Handwerker'),
        ('domain-hosting-email.html', 'Domain, Hosting und E-Mail'),
    ]) + cta_block('// nächster schritt', [['Wie viele Seiten'], ['braucht der Verein?']],
        'Schreiben Sie mir den Namen des Vereins und was heute schon online ist. Den Festpreis bekommen Sie danach.',
        'Anfragen', 'kontakt.html', 'Zum Rechner', 'rechner.html')
    return _seite('website-fuer-vereine.html', inhalt, faq)


def pflege():
    faq = [
        ('Gibt es einen festen Monatspreis für die Pflege?', 'Nein. Auf dieser Seite steht keiner, weil keiner vereinbart ist. Ich schreibe den Umfang und den Preis auf, bevor die Pflege startet.'),
        ('Was kann ein einzelner Text kosten?', 'Ein Website-Text kostet 59 €. Das ist ein Text bis etwa 500 Wörter, mit einer Korrekturrunde. Nicht die ganze Betreuung der Seite.'),
        ('Prüfen Sie, ob das Formular noch geht?', 'Ja, wenn das im Auftrag steht. Dazu gehören der Kontaktweg, die Ansicht auf dem Telefon und ob Titel und Beschreibung da sind.'),
        ('Ist das eine rechtliche Prüfung?', 'Nein. Ich prüfe die Technik. Ob eine Seite eine Pflicht erfüllt, sage ich nicht.'),
        ('Können Sie auch die Domain und die E-Mail mit betreuen?', 'Ja, als eigener Punkt im Auftrag. Zugänge und Anbieter klären wir vorher.'),
        ('Wie kündigen wir die Pflege?', 'Das steht im Angebot, zusammen mit dem Umfang. Einen offenen Vertrag ohne Ende gibt es bei mir nicht als Standard.'),
    ]
    inhalt = hero_klein(
        '04', 'Pflege',
        [['Website-Pflege'], ['für kleine Betriebe.']],
        'Die Seite ist online. Danach ändert sich der Preis, die Öffnungszeit oder ein Satz. Oft bleibt der alte Stand stehen.',
        ['Umfang vor dem Start', 'kein Listenpreis pro Monat', 'Texte einzeln 59 €'],
    ) + _aktionen() + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Was nach dem Start passiert')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Die Seite altert,'], ['wenn niemand hinsieht.']])}</h2>
    <div class="prose rise">
      <p>Eine Öffnungszeit stimmt nicht mehr. Ein Formular kommt nicht an. Ein Bild ist zu groß für das Telefon.</p>
      <p>Die Person, die die Seite gebaut hat, ist nicht mehr da. Die Zugänge kennt niemand.</p>
      <p>Kleine Betriebe brauchen dafür kein großes Team. Sie brauchen eine klare Liste, was geprüft und geändert wird.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Pakete')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Pflege ist ein Auftrag.'], ['Kein offener Topf.']])}</h2>
    {karten_grid([
        ('01', 'Pflege-Auftrag', 'Zum Beispiel Texte tauschen, ein Formular prüfen, Titel und Kontaktweg ansehen. Den Preis nenne ich, wenn die Liste feststeht. Einen Monatspreis erfinde ich hier nicht.'),
        ('02', 'Website-Text · 59 €', 'Wenn nur ein Text neu soll: bis etwa 500 Wörter, eine Korrekturrunde, 3 Werktage. Das ist der bestehende Textpreis, nicht die ganze Pflege.'),
        ('03', 'Technischer Check', 'Telefon-Ansicht, Tastatur, Alternativtexte, ob ein Formular Daten auf der Website speichert. Das ist Technik, keine Rechtsberatung und kein Zertifikat.'),
    ])}
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Das bekommen Sie')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Eine Liste.'], ['Dann die Arbeit.']])}</h2>
    {punkte_liste([
        'Eine schriftliche Liste, was gepflegt wird',
        'Den Preis, bevor ich anfange',
        'Geänderte Texte, die ich selbst lese',
        'Einen Blick auf Telefon, Kontakt und Formular',
        'Eine Notiz, wo Domain und Zugänge liegen',
        'Einen klaren Rahmen, wann der Auftrag endet',
    ])}
  </div>
</section>''' + faq_block('05', 'Häufige Fragen', [['Zur'], ['Pflege.']], faq) + _links([
        ('landingpage-erstellen-lassen.html', 'Landingpage erstellen lassen'),
        ('domain-hosting-email.html', 'Domain, Hosting und E-Mail'),
        ('angebot/', 'Texte und Übersetzungen'),
        ('website-fuer-handwerker.html', 'Website für Handwerker'),
        ('website-fuer-vereine.html', 'Website für Vereine'),
    ]) + cta_block('// nächster schritt', [['Was soll sich'], ['auf der Seite ändern?']],
        'Schicken Sie mir die Adresse der Seite und einen Satz, was nicht mehr stimmt. Den Preis nenne ich danach.',
        'Anfragen', 'kontakt.html', 'Zum Rechner', 'rechner.html')
    return _seite('website-pflege-kleine-betriebe.html', inhalt, faq)


def haendler():
    faq = [
        ('Was kostet ein kleiner Onlineshop?', 'Festpreis-Angebot auf Anfrage. Der Preis hängt von der Zahl der Produkte, der Zahlung und dem Versand ab. Einen Betrag vor diesem Gespräch nenne ich nicht.'),
        ('Was kosten die Produkttexte?', 'Ein Website-Text kostet 59 €, bis etwa 500 Wörter. Mehrere Produkttexte zusammen sind das Content-Paket für 99 €, bis etwa 1.000 Wörter.'),
        ('Brauchen wir ein großes Shopsystem?', 'Oft nein. Ein kleines Sortiment braucht eine klare Liste, einen Preis und einen Weg zur Bestellung oder zur Anfrage.'),
        ('Richten Sie Zahlung und Versand ein?', 'Nur, was wir vorher aufschreiben. Welche Anbieter dazukommen, steht im Festpreis-Angebot, nicht als pauschales Versprechen.'),
        ('Können Leute auch nur anfragen, statt sofort zu zahlen?', 'Ja. Für manche Waren ist eine Anfrage der bessere Weg. Das legen wir vor dem Bau fest.'),
    ]
    inhalt = hero_klein(
        '05', 'Für Händler',
        [['Onlineshop'], ['für kleine Händler.']],
        'Sie verkaufen ein überschaubares Sortiment. Die Ware steht auf Fotos in einem Messenger. Ein eigener Shop fehlt, oder er ist zu groß für den Alltag.',
        ['Festpreis nach Umfang', 'Produkttexte 59 € und 99 €', 'kleines Sortiment'],
    ) + _aktionen() + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Was Kunden nicht sehen')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Die Ware ist da.'], ['Der Weg zur Bestellung nicht.']])}</h2>
    <div class="prose rise">
      <p>Preise stehen in einer Tabelle. Versandkosten stehen nirgends. Wer bezahlen will, schreibt eine private Nachricht.</p>
      <p>Ein großes Shopsystem hat mehr Knöpfe, als der Laden Produkte hat.</p>
      <p>Produkttexte fehlen. Auf dem Telefon ist die Liste unlesbar.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Pakete')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Shop und Texte'], ['getrennt rechnen.']])}</h2>
    {karten_grid([
        ('01', 'Kleiner Shop', 'Produktliste, Preis, Versand oder Anfrage. Den Festpreis nenne ich, wenn die Produktzahl und die Zahlung klar sind.'),
        ('02', 'Website-Text · 59 €', 'Ein Text bis etwa 500 Wörter. Zum Beispiel eine Warengruppe oder die Seite zum Versand. Eine Korrekturrunde. 3 Werktage.'),
        ('03', 'Content-Paket · 99 €', 'Mehrere Produkttexte zusammen, bis etwa 1.000 Wörter. Eine Korrekturrunde. 5 Werktage.'),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Zahlung, Versand und Steuer richten sich nach Ihrem Fall. Was davon im Auftrag liegt, steht im Angebot. Eine Rechtsberatung ist das nicht.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Das bekommen Sie')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Ein Shop,'], ['der zum Sortiment passt.']])}</h2>
    {punkte_liste([
        'Eine Produktliste, die auf dem Telefon lesbar ist',
        'Preis und Versand oder ein klarer Anfrageweg',
        'Texte, die ich selbst prüfe',
        'Eine Absprache, wer neue Produkte einträgt',
        'Den Festpreis, bevor der Shop gebaut wird',
        'Keine Funktionen, die Sie nicht brauchen',
    ])}
  </div>
</section>''' + faq_block('05', 'Häufige Fragen', [['Vor dem'], ['kleinen Shop.']], faq) + _links([
        ('webdesign.html', 'Webdesign'),
        ('app-entwicklung.html', 'Web-App'),
        ('angebot/', 'Texte und Übersetzungen'),
        ('website-fuer-handwerker.html', 'Website für Handwerker'),
        ('landingpage-erstellen-lassen.html', 'Landingpage erstellen lassen'),
        ('rechner.html', 'Rechner'),
    ]) + cta_block('// nächster schritt', [['Wie viele Produkte'], ['sollen in den Shop?']],
        'Schreiben Sie mir, was Sie verkaufen und ob Leute direkt zahlen oder erst anfragen sollen.',
        'Anfragen', 'kontakt.html', 'Zum Rechner', 'rechner.html')
    return _seite('onlineshop-kleine-haendler.html', inhalt, faq)


def faqe_dhe_perkthime():
    faq = [
        ('Sa kushton një tekst?', 'Teksti i faqes kushton 59 €, deri në rreth 500 fjalë, me një raund korrigjimi. Paketa e përmbajtjes kushton 99 €, deri në rreth 1.000 fjalë. Një dokument i shkurtër kushton 49 €.'),
        ('A janë çmimet për një gjuhë?', 'Po. Gjuhët janë gjermanisht, anglisht dhe shqip, në çdo drejtim. Një gjuhë tjetër kushton shtesë: 35 €, 40 € ose 79 €, sipas paketës.'),
        ('A i bëni përkthime të noterizuara?', 'Jo. Nuk përkthej dokumente zyrtare si certifikata. Nuk shkruaj as tekste juridike apo mjekësore.'),
        ('Sa kushton vetë faqja e internetit?', 'Çmimin fiks e them pasi të di sa faqe duhen dhe a i keni tekstet gati. Nuk kam një çmim të gatshëm për çdo faqe.'),
        ('Kush e lexon tekstin para se të ma dërgoni?', 'Unë. IA mund të bëjë draftin e parë. Tekstin e lexoj dhe e korrigjoj vetë, para se të vijë te ju.'),
        ('A punoni edhe për biznese në Shqipëri?', 'Po. Faqja u drejtohet bizneseve që flasin shqip në Gjermani, në Kosovë dhe në Shqipëri. Punën e bashkërendojmë online.'),
    ]
    inhalt = hero_klein(
        '01', 'Shqip · DE · EN',
        [['Faqe web.'], ['Tekste në tri gjuhë.']],
        'Klienti në Gjermani lexon gjermanisht. Partneri në Kosovë lexon shqip. Një faqe me një gjuhë të vetme i lë të dy jashtë.',
        ['49 €, 59 €, 99 €', 'gjermanisht, anglisht, shqip', 'çmimi i faqes pas vëllimit'],
    ) + _aktionen('Na shkruani', 'Te kalkulatori', '../') + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Ku ngec')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Teksti duket i përkthyer.'], ['Jo i shkruar.']])}</h2>
    <div class="prose rise">
      <p>Faqja është vetëm në gjermanisht. Numri i telefonit gjendet pas tre klikimeve.</p>
      <p>Përkthimi fjalë për fjalë tingëllon i huaj. Fjalët e zejes suaj nuk janë ato që do të përdornit vetë.</p>
      <p>Askush në ekip nuk ka kohë të ulet dhe të shkruajë të njëjtin tekst tri herë.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Paketat')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Çmimet që janë tashmë.'], ['Asnjë shifër e re.']])}</h2>
    {karten_grid([
        ('01', 'Dokument · 49 €', 'Deri në rreth 600 fjalë. Një dokument i shkurtër ose një fletëpalosje. Një raund korrigjimi. 2 ditë pune. Gjuhë tjetër: +35 €.'),
        ('02', 'Tekst faqeje · 59 €', 'Deri në rreth 500 fjalë. Për shembull faqja e fillimit. Përkthim ose tekst i ri. 3 ditë pune. Gjuhë tjetër: +40 €.'),
        ('03', 'Paketë përmbajtjeje · 99 €', 'Deri në rreth 1.000 fjalë, disa tekste që shkojnë bashkë. 5 ditë pune. Gjuhë tjetër: +79 €.'),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Faqen e internetit e ndërtoj veç. Çmimin fiks e them pasi të qartësohet vëllimi. Porosia minimale për tekste është 30 €. Nën 24 orë: +30 %.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Çfarë merrni')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Tekst që mund'], ['ta përdorni.']])}</h2>
    {punkte_liste([
        'Gjermanisht, anglisht ose shqip, sipas nevojës',
        'Tonin e biznesit tuaj, jo një përkthim të ngurtë',
        'Një raund korrigjimi',
        'Çmimin para se të filloj',
        'Leximin tim, pasi drafti të jetë gati',
        'Një faqe, nëse e porosisni veç e veç',
    ])}
  </div>
</section>''' + faq_block('05', 'Pyetje', [['Para se'], ['të porosisni.']], faq) + _links([
        ('../angebot/', 'Çmimet në gjermanisht'),
        ('../landingpage-erstellen-lassen.html', 'Faqe ose landingpage'),
        ('../sq/automatizim-ia.html', 'Automatizim me IA'),
        ('../website-fuer-handwerker.html', 'Website für Handwerker'),
        ('../kontakt.html', 'Kontakt'),
    ]) + cta_block('// hapi tjetër', [['Çfarë duhet'], ['të lexohet?']],
        'Më shkruani gjuhën që keni dhe gjuhën që doni. Çmimin e tekstit e dini që këtu. Çmimin e faqes e them pasi të shoh vëllimin.',
        'Na shkruani', '../kontakt.html', 'Te kalkulatori', '../rechner.html')
    return _seite(
        'sq/faqe-dhe-perkthime.html', inhalt, faq, base='../', lang='sq', alternates=TEXT_ALT,
        home_href='index.html', home_label='Kreu')


def automatizim():
    faq = [
        ('Sa kushton automatizimi i parë?', 'Çmimin fiks e them pasi të di a bëhet fjalë për email, për ofertë apo për takim, dhe çfarë programi përdorni. Një shifër para kësaj bisede nuk jap.'),
        ('A del diçka pa mua?', 'Jo. Ajo që shkon te klienti ose që cakton një takim mbetet draft, derisa ta miratoni ju.'),
        ('A zëvendëson kjo ekipin?', 'Jo. Puna përgatitet. Vendimi mbetet te ju.'),
        ('A futen të dhëna pacientësh?', 'Jo në këtë ofertë. Nuk e ndërtoj automatizimin mbi akte, diagnoza ose të dhëna shëndetësore.'),
        ('A është kjo këshillë juridike për të dhënat?', 'Jo. Them cilat të dhëna i sheh drafti. Vlerësimin ligjor e bën dikush që e ka këtë detyrë.'),
        ('A vlen edhe për Shqipërinë?', 'Po. U drejtohem bizneseve që flasin shqip në Gjermani, në Kosovë dhe në Shqipëri.'),
    ]
    inhalt = hero_klein(
        '02', 'IA për biznesin',
        [['Automatizim me IA.'], ['Një hap, jo një sistem i tërë.']],
        'Të njëjtat email vijnë çdo ditë. Ofertat kopjohen nga një dokument i vjetër. Kërkesat për takim humbasin në telefon.',
        ['çmim fiks pas bisedës', 'miratim nga ju', 'pa të dhëna të ndjeshme'],
    ) + _aktionen('Na shkruani', 'Te kalkulatori', '../') + f'''
<section class="pad" id="probleme" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('02', 'Ku shkon koha')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['E njëjta punë.'], ['Çdo mëngjes.']])}</h2>
    <div class="prose rise">
      <p>Dikush pyet për një takim. Dikush kërkon një ofertë me të njëjtat pika si javën e kaluar.</p>
      <p>Ju nuk doni që një sistem të dërgojë një përgjigje vetë. Doni një draft, pastaj vendimin tuaj.</p>
      <p>Të dhënat e ndjeshme, përfshirë ato shëndetësore, nuk hyjnë në këtë hap të parë.</p>
    </div>
  </div>
</section>
<section class="pad" id="pakete" style="background:var(--ink-2);scroll-margin-top:110px">
  <div class="shell">
    {kicker('03', 'Paketa')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Një proces.'], ['Një çmim i shkruar.']])}</h2>
    {karten_grid([
        ('01', 'Email', 'Mesazhet hyjnë të renditura. Drafti i përgjigjes është gati. Ju vendosni çfarë del.'),
        ('02', 'Ofertë ose takim', 'Nga kërkesa del një draft oferte, ose një propozim takimi. Çmimi dhe data konfirmohen nga ju.'),
        ('03', 'Çmim fiks pas bisedës', 'Nuk ka çmim liste. E shkruaj vëllimin dhe çmimin pasi të jetë e qartë lidhja me programin që përdorni.'),
    ])}
    <p class="rise" style="color:var(--paper-mute);font-size:.95rem;max-width:68ch;margin-top:22px">Nëse doni edhe tekstin e faqes, çmimet janë të njëjtat: 59 € për një tekst faqeje, 99 € për paketën e përmbajtjes.</p>
  </div>
</section>
<section class="pad" id="leistung" style="scroll-margin-top:110px">
  <div class="shell">
    {kicker('04', 'Çfarë merrni')}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 22px">{wipe([['Një kufi i qartë.']])}</h2>
    {punkte_liste([
        'Një proces të parë, jo një platformë të tërë',
        'Draft për email, ofertë ose takim',
        'Miratimin tuaj para se të dalë diçka',
        'Pa akte dhe pa të dhëna shëndetësore',
        'Një shënim se çfarë nuk bën sistemi',
        'Çmimin me shkrim, para se të filloj',
    ])}
  </div>
</section>''' + faq_block('05', 'Pyetje', [['Para hapit'], ['të parë.']], faq) + _links([
        ('../ki-automatisierung-kleine-unternehmen.html', 'Oferta në gjermanisht'),
        ('../ki-automatisierung-arztpraxen.html', 'IA për ordinanca, në gjermanisht'),
        ('../sq/faqe-dhe-perkthime.html', 'Faqe web dhe përkthime'),
        ('../rechner.html', 'Kalkulatori'),
        ('../kontakt.html', 'Kontakt'),
    ]) + cta_block('// hapi tjetër', [['Email, ofertë'], ['apo takim?']],
        'Më shkruani cilin nga të tre e doni të parin. Çmimin fiks e merrni pasi ta shohim bashkë.',
        'Na shkruani', '../kontakt.html', 'Te kalkulatori', '../rechner.html')
    return _seite(
        'sq/automatizim-ia.html', inhalt, faq, base='../', lang='sq', alternates=KI_ALT,
        home_href='index.html', home_label='Kreu')


def build(root):
    from icons import iconize
    paare = {
        'website-fuer-handwerker.html': handwerker,
        'ki-automatisierung-arztpraxen.html': praxen,
        'website-fuer-vereine.html': vereine,
        'website-pflege-kleine-betriebe.html': pflege,
        'onlineshop-kleine-haendler.html': haendler,
    }
    for name, fn in paare.items():
        text = iconize(fn())
        (root / name).write_text(text)
        print(f'  {name:30} {len(text):>7} Zeichen')
    sq = root / 'sq'
    sq.mkdir(exist_ok=True)
    for name, fn in {'faqe-dhe-perkthime.html': faqe_dhe_perkthime, 'automatizim-ia.html': automatizim}.items():
        text = iconize(fn())
        (sq / name).write_text(text)
        print(f'  {("sq/" + name):30} {len(text):>7} Zeichen')
