# -*- coding: utf-8 -*-
"""Baut die komplette Seite: drei Startseiten und alle Unterseiten.

    python3 _build/bau_alles.py
"""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
WURZEL = HIER.parent

from pricing import build as build_pricing
build_pricing(WURZEL)

from icons import iconize

import seiten_a, seiten_b, seiten_c, seiten_d, experience, artwork, services
import kern, pakete, landings, translation_offer
from seo import write_sitemap

SEITEN = {
    'ki-automatisierung-kleine-unternehmen.html': kern.ki_kleine,
    'landingpage-erstellen-lassen.html': kern.landingpage,
    'website-pflege.html': pakete.website_pflege,
    'onlineshop.html': pakete.onlineshop,
    'web-apps.html': pakete.web_apps,
    'firmenprofile.html': pakete.firmenprofile,
    'preisrechner.html': pakete.preisrechner,
    'ueber-mich.html': seiten_a.ueber_mich,
    'werdegang.html': seiten_a.werdegang,
    'leistungen.html': seiten_a.leistungen,
    'fb-beratung.html': seiten_b.fb_beratung,
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

if __name__ == '__main__':
    artwork.build()
    experience.build()
    services.build(WURZEL)
    for datei, fn in SEITEN.items():
        html = iconize(fn())
        (WURZEL / datei).write_text(html)
        print(f"  {datei:30} {len(html):>7} Zeichen")
    translation_offer.build(WURZEL)
    landings.build(WURZEL)
    write_sitemap(WURZEL)
