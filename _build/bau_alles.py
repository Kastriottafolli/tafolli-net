# -*- coding: utf-8 -*-
"""Baut die komplette Seite: drei Startseiten und alle Unterseiten.

    python3 _build/bau_alles.py
"""
import pathlib, re, subprocess, sys
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
WURZEL = HIER.parent

from icons import iconize

import seiten_a, seiten_b, seiten_c, seiten_d, kern, experience, artwork, services

SEITEN = {
    'ueber-mich.html': seiten_a.ueber_mich,
    'werdegang.html': seiten_a.werdegang,
    'leistungen.html': seiten_a.leistungen,
    'fb-beratung.html': seiten_b.fb_beratung,
    'ki-automatisierung-kleine-unternehmen.html': kern.ki_kleine,
    'landingpage-erstellen-lassen.html': kern.landingpage,
    'online-marketing.html': seiten_b.online_marketing,
    'teamo-ki.html': seiten_b.teamo,
    'rechner.html': seiten_c.rechner,
    'wissen.html': seiten_c.wissen,
    'wissen-ki-im-hotel.html': seiten_c.wissen_ki,
    'wissen-getraenkevertrag.html': seiten_c.wissen_getraenke,
    'wissen-direktbuchungen.html': seiten_c.wissen_direkt,
    'referenzen.html': seiten_d.referenzen,
    'kontakt.html': seiten_d.kontakt,
    'impressum.html': seiten_d.impressum,
    'datenschutz.html': seiten_d.datenschutz,
    '404.html': seiten_d.fehler404,
}

def angebot_auffrischen():
    """angebot/index.html is hand-authored. Refresh shared chrome so it matches the build."""
    from bausteine import VER, fusszeile, kopfzeile
    from brand import intro
    pfad = WURZEL / 'angebot' / 'index.html'
    text = pfad.read_text()
    start = text.find('<div class="brand-intro"')
    grain = text.find('<div class="grain"')
    header = text.find('<header')
    main = text.find('<main')
    footer = text.find('<footer')
    script = text.find('<script', footer)
    if min(start, grain, header, main, footer, script) < 0:
        raise SystemExit('angebot/index.html: chrome markers missing')
    text = text[:start] + intro('de', '../') + '\n' + text[grain:header] + iconize(kopfzeile('angebot/', '../')) + '\n\n' + text[main:footer] + iconize(fusszeile('../')) + '\n' + text[script:]
    text = re.sub(r'(assets/(?:schriften|kt|experience)\.css\?v=)[0-9a-f]+', r'\g<1>' + VER, text)
    text = re.sub(r'(assets/(?:navigation|brand|kt)\.js\?v=)[0-9a-f]+', r'\g<1>' + VER, text)
    pfad.write_text(text)
    print(f"  {'angebot/index.html':30} {len(text):>7} Zeichen")

if __name__ == '__main__':
    artwork.build()
    experience.build()
    services.build(WURZEL)
    for datei, fn in SEITEN.items():
        html = iconize(fn())
        (WURZEL / datei).write_text(html)
        print(f"  {datei:30} {len(html):>7} Zeichen")
    angebot_auffrischen()
