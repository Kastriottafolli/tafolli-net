# -*- coding: utf-8 -*-
"""Baut die komplette Seite: drei Startseiten und alle Unterseiten.

    python3 _build/bau_alles.py
"""
import pathlib, re, subprocess, sys
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
WURZEL = HIER.parent

from icons import iconize

import seiten_a, seiten_b, seiten_c, seiten_d, kern, pakete, experience, artwork, services, landings

SEITEN = {
    'ueber-mich.html': seiten_a.ueber_mich,
    'werdegang.html': seiten_a.werdegang,
    'leistungen.html': seiten_a.leistungen,
    'fb-beratung.html': seiten_b.fb_beratung,
    'ki-automatisierung-kleine-unternehmen.html': kern.ki_kleine,
    'landingpage-erstellen-lassen.html': kern.landingpage,
    'website-pflege.html': pakete.website_pflege,
    'onlineshop.html': pakete.onlineshop,
    'web-apps.html': pakete.web_apps,
    'firmenprofile.html': pakete.firmenprofile,
    'preisrechner.html': pakete.preisrechner,
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

def sitemap_schreiben():
    """Sitemap aus den gebauten Seiten. noindex bleibt draußen."""
    gruppen = {
        'https://tafolli.net/': [('de', 'https://tafolli.net/'), ('en', 'https://tafolli.net/en/'), ('sq', 'https://tafolli.net/sq/'), ('x-default', 'https://tafolli.net/')],
        'https://tafolli.net/en/': [('de', 'https://tafolli.net/'), ('en', 'https://tafolli.net/en/'), ('sq', 'https://tafolli.net/sq/'), ('x-default', 'https://tafolli.net/')],
        'https://tafolli.net/sq/': [('de', 'https://tafolli.net/'), ('en', 'https://tafolli.net/en/'), ('sq', 'https://tafolli.net/sq/'), ('x-default', 'https://tafolli.net/')],
        'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html': [
            ('de', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
            ('sq', 'https://tafolli.net/sq/automatizim-ia.html'),
            ('x-default', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html')],
        'https://tafolli.net/sq/automatizim-ia.html': [
            ('de', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html'),
            ('sq', 'https://tafolli.net/sq/automatizim-ia.html'),
            ('x-default', 'https://tafolli.net/ki-automatisierung-kleine-unternehmen.html')],
        'https://tafolli.net/angebot/': [
            ('de', 'https://tafolli.net/angebot/'),
            ('sq', 'https://tafolli.net/sq/faqe-dhe-perkthime.html'),
            ('x-default', 'https://tafolli.net/angebot/')],
        'https://tafolli.net/sq/faqe-dhe-perkthime.html': [
            ('de', 'https://tafolli.net/angebot/'),
            ('sq', 'https://tafolli.net/sq/faqe-dhe-perkthime.html'),
            ('x-default', 'https://tafolli.net/angebot/')],
    }
    dateien = [*WURZEL.glob('*.html'), * (WURZEL / 'en').glob('*.html'), * (WURZEL / 'sq').glob('*.html'), WURZEL / 'angebot' / 'index.html']
    orte = []
    for datei in dateien:
        text = datei.read_text()
        if 'name="robots" content="noindex"' in text:
            continue
        relativ = datei.relative_to(WURZEL).as_posix()
        if relativ == 'index.html':
            ort = 'https://tafolli.net/'
        elif relativ.endswith('/index.html'):
            ort = 'https://tafolli.net/' + relativ[:-len('index.html')]
        else:
            ort = 'https://tafolli.net/' + relativ
        orte.append(ort)
    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for ort in sorted(set(orte), key=lambda wert: (wert != 'https://tafolli.net/', wert)):
        zeilen.append('  <url>')
        zeilen.append(f'    <loc>{ort}</loc>')
        for code, href in gruppen.get(ort, []):
            zeilen.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{href}"/>')
        zeilen.append('  </url>')
    zeilen.append('</urlset>')
    (WURZEL / 'sitemap.xml').write_text('\n'.join(zeilen) + '\n')
    print(f'  {"sitemap.xml":30} {len(orte):>7} Adressen')


def angebot_auffrischen():
    """angebot/index.html is hand-authored. Refresh shared chrome so it matches the build."""
    import json
    from bausteine import VER, fusszeile, kopfzeile
    from brand import intro
    from seo import texte_angebot
    pfad = WURZEL / 'angebot' / 'index.html'
    text = pfad.read_text()
    mark = '<script type="application/ld+json">'
    begin = text.find(mark)
    end = text.find('</script>', begin)
    if begin < 0 or end < 0:
        raise SystemExit('angebot/index.html: missing structured data')
    data = json.loads(text[begin+len(mark):end])
    angebot = texte_angebot()
    data['@graph'] = [node for node in data['@graph'] if node.get('@id') != angebot['@id']]
    place = next(i for i,node in enumerate(data['@graph']) if node.get('@type') == 'BreadcrumbList')
    data['@graph'].insert(place, angebot)
    blob = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
    text = text[:begin+len(mark)] + blob + text[end:]
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
    landings.build(WURZEL)
    sitemap_schreiben()
