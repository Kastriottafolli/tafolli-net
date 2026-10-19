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
    from seo import SITEMAP_LASTMOD, alternates_for
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
        schluessel = 'index.html' if ort == 'https://tafolli.net/' else ort.removeprefix('https://tafolli.net/')
        zeilen.append('  <url>')
        zeilen.append(f'    <loc>{ort}</loc>')
        zeilen.append(f'    <lastmod>{SITEMAP_LASTMOD}</lastmod>')
        for code, href in alternates_for(schluessel):
            zeilen.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{href}"/>')
        zeilen.append('  </url>')
    zeilen.append('</urlset>')
    (WURZEL / 'sitemap.xml').write_text('\n'.join(zeilen) + '\n')
    print(f'  {"sitemap.xml":30} {len(orte):>7} Adressen')


def angebot_auffrischen():
    """angebot/index.html is hand-authored. Refresh shared chrome so it matches the build."""
    from bausteine import VER, fusszeile, kopfzeile
    from brand import intro
    from seo import ANGEBOT_FAQ, meta_block
    pfad = WURZEL / 'angebot' / 'index.html'
    text = pfad.read_text()
    block = meta_block('angebot/', '', '', 'de', ANGEBOT_FAQ).rstrip()
    title_at = text.find('<title>')
    script_at = text.find('<script type="application/ld+json">')
    script_end = text.find('</script>', script_at)
    if min(title_at, script_at, script_end) < 0 or not title_at < script_at:
        raise SystemExit('angebot/index.html: head metadata missing')
    text = text[:title_at] + block + text[script_end + len('</script>'):]
    text = re.sub(r'\n?<link rel="preload" as="image" href="\.\./assets/brand/logo-mark\.webp">', '', text)
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
    crumb = '<div class="shell site-breadcrumb"><nav aria-label="Brotkrumennavigation"><a href="../index.html">Startseite</a><span aria-hidden="true">/</span><a href="../leistungen.html">Leistungen</a><span aria-hidden="true">/</span><span aria-current="page">Texte und Übersetzungen</span></nav></div>'
    text, count = re.subn(r'<div class="shell site-breadcrumb"><nav aria-label="Brotkrumennavigation">.*?</nav></div>', crumb, text, count=1)
    if count != 1:
        raise SystemExit('angebot/index.html: breadcrumb missing')
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
