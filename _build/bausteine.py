# -*- coding: utf-8 -*-
"""Gemeinsame Bausteine fuer alle Unterseiten. Kopf- und Fusszeile sind
identisch zur Startseite, damit die Seite wie aus einem Guss wirkt."""
import hashlib, pathlib, html
from brand import lockup, MARK, FAVICON, TOUCH_ICON
from navigation import nav as site_nav, toggle as nav_toggle, breadcrumbs, TITLES
from seo import metadata, structured, region, SERVICE_META
from explore import explore, HUBS
from visuals import enrich
from work import dialog as work_dialog
from boosty import widget as boosty_widget

WURZEL = pathlib.Path(__file__).resolve().parent.parent
LOGO = lockup()

def intro(*args, **kwargs):
    """Legacy standalone pages no longer display an animated brand entrance."""
    return ''

VER = hashlib.sha256(
    (WURZEL / 'assets/kt.css').read_bytes() + (WURZEL / 'assets/kt.js').read_bytes()
    + (WURZEL / 'assets/experience.css').read_bytes()
    + (WURZEL / 'assets/corporate.css').read_bytes()
    + (WURZEL / 'assets/motion.css').read_bytes()
    + (WURZEL / 'assets/motion.js').read_bytes()
    + (WURZEL / 'assets/creative.css').read_bytes()
    + (WURZEL / 'assets/agency.css').read_bytes()
    + (WURZEL / 'assets/boosty.css').read_bytes()
    + (WURZEL / 'assets/boosty.js').read_bytes()
    + (WURZEL / 'assets/creative.js').read_bytes()
    + (WURZEL / 'assets/navigation.js').read_bytes()
    + (WURZEL / 'assets/contact.js').read_bytes()
    + (WURZEL / 'assets/form-delivery.mjs').read_bytes()
).hexdigest()[:8]

NAV = [
    ("ki-automatisierung.html", "AI Automation"),
    ("ueber-mich.html", "Unternehmen"),
    ("leistungen.html", "Leistungen"),
    ("teamo-ki.html", "TeamO KI"),
    ("rechner.html", "Rechner"),
    ("kontakt.html", "Kontakt"),
]
FOOT_L1 = NAV + [("werdegang.html", "Werdegang"), ("wissen.html", "Wissen"), ("referenzen.html", "Referenzen")]
FOOT_L2 = [
    ("fb-beratung.html", "F&B-Beratung"),
    ("online-marketing.html", "Online-Marketing & Web"),
    ("ki-automatisierung.html", "KI-Automatisierung"),
    ("ki-entwicklung.html", "KI-Entwicklung"),
    ("cybersecurity.html", "Cybersecurity"),
    ("digitalisierung.html", "Digitalisierung"),
    ("softwareentwicklung.html", "Softwareentwicklung"),
    ("lieferantenvereinbarungen.html", "Lieferantenvereinbarungen"),
    ("rueckverguetungen.html", "Rückvergütungen"),
    ("rechner.html", "Rechner"),
]


def wipe(zeilen, start=0, klasse="wipe"):
    out = []
    for zeile in zeilen:
        teile = zeile if isinstance(zeile, list) else [zeile]
        for t in teile:
            out.append(f'<span><span style="--i:{start + len(out)}">{t}</span></span>')
    return " ".join(out)


def kicker(nummer, text):
    return f'<p class="tag rise"><span class="n">// {nummer}</span>&nbsp;&nbsp;{text}</p>'


def seiten_kopf(titel, beschreibung, kanonisch_pfad):
    """<head>-Block. kanonisch_pfad z.B. 'ueber-mich.html'."""
    titel, beschreibung = metadata(kanonisch_pfad, titel, beschreibung)
    schema = structured(kanonisch_pfad, titel, beschreibung)
    titel, beschreibung = html.escape(titel), html.escape(beschreibung)
    kanonisch = f"https://tafolli.net/{kanonisch_pfad}"
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
<meta name="author" content="Tafolli &amp; Co.">
<link rel="canonical" href="{kanonisch}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Tafolli &amp; Co.">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{beschreibung}">
<meta property="og:url" content="{kanonisch}">
<meta property="og:image" content="https://tafolli.net/assets/social-preview.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{titel}">
<meta name="twitter:card" content="summary_large_image">
{schema}
<meta name="theme-color" content="#f7f8f5">
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<link rel="apple-touch-icon" href="{TOUCH_ICON}">
<link rel="preload" as="image" href="{MARK}" fetchpriority="high">
<link rel="preload" as="font" type="font/woff2" href="assets/schriften/space-grotesk-var.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/schriften/ibm-plex-sans-400.woff2" crossorigin>
<link rel="stylesheet" href="assets/schriften.css?v={VER}">
<link rel="stylesheet" href="assets/kt.css?v={VER}">
<link rel="stylesheet" href="assets/experience.css?v={VER}">
<link rel="stylesheet" href="assets/corporate.css?v={VER}">
<link rel="stylesheet" href="assets/motion.css?v={VER}">
<link rel="stylesheet" href="assets/creative.css?v={VER}">
<link rel="stylesheet" href="assets/agency.css?v={VER}">
<link rel="stylesheet" href="assets/boosty.css?v={VER}">
</head>'''


def kopfzeile(aktiv, base=""):
    sprachwahl = '<a href="/" hreflang="de" lang="de" title="Deutsch">DE</a><a href="/en/" hreflang="en" lang="en" title="English">EN</a><a href="/sq/" hreflang="sq" lang="sq" title="Shqip">SQ</a>'
    return f'''<header class="bar site-header"><div class="shell bar-in"><a class="tafolli-brand-link" href="{base}index.html" aria-label="Tafolli &amp; Co. · Startseite">{lockup(base)}</a>{site_nav(aktiv, base)}<div class="site-header-controls"><nav class="lang" aria-label="Sprache / Language / Gjuha">{sprachwahl}</nav><a href="{base}kontakt.html" class="btn btn-1 site-talk">Gespräch ↗</a>{nav_toggle()}</div></div></header>'''


def fusszeile():
    def links(items):
        return ''.join(f'<a href="{href}">{label}</a>' for href,label in items)
    services = links([
        ('online-marketing.html','Marketing'),
        ('softwareentwicklung.html','Technology'),
        ('fb-beratung.html','Consulting'),
        ('ki-automatisierung.html','AI Automation'),
    ])
    company = links([
        ('ueber-mich.html','Unternehmen'),
        ('referenzen.html','Projekte & Referenzen'),
        ('wissen.html','Wissen'),
        ('kontakt.html','Kontakt'),
    ])
    return f'''<footer class="company-footer"><div class="shell">
      <div class="company-footer-grid">
        <div><a class="tafolli-brand-link" href="index.html" aria-label="Tafolli &amp; Co. · Startseite">{LOGO}</a>
          <p>Marketing, Technologie, Beratung und KI-Automatisierung. Von der Planung bis zur Umsetzung für Ihr Unternehmen.</p></div>
        <div><h2>Leistungen</h2>{services}</div>
        <div><h2>Unternehmen</h2>{company}</div>
        <div><h2>Kontakt</h2><a href="mailto:info@tafolli.net">info@tafolli.net</a><a href="tel:+4917664616146">+49 176 64616146</a><p>Deutschland · Österreich · Schweiz · Kosovo</p></div>
      </div>
      <div class="company-footer-bottom"><span>© 2026 Tafolli &amp; Co.</span><div><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></div><span>tafolli.net</span></div>
    </div></footer>'''


def seite_rahmen(aktiv, titel, beschreibung, kanonisch_pfad, inhalt):
    extra = explore(kanonisch_pfad) if kanonisch_pfad in HUBS and kanonisch_pfad != 'online-marketing.html' else ''
    if kanonisch_pfad.removesuffix('.html') in SERVICE_META and 'class="region-section"' not in inhalt:
        extra += region(service=TITLES[kanonisch_pfad])
    if extra:
        position = inhalt.rfind('<section class="pad" style="overflow:hidden">')
        if position < 0: position = len(inhalt)
        inhalt = inhalt[:position] + extra + inhalt[position:]
    inhalt = enrich(kanonisch_pfad, inhalt)
    # Keep the technical example readable without replaying a terminal animation.
    inhalt = inhalt.replace('id="term"', '')
    contact_script=f'<script type="module" src="assets/contact.js?v={VER}"></script>' if aktiv=='kontakt.html' else ''
    return f'''{seiten_kopf(titel, beschreibung, kanonisch_pfad)}
<body class="corporate-pages">

<a href="#inhalt" class="btn btn-1" style="position:absolute;left:-9999px;top:0;z-index:200"
   onfocus="this.style.left='12px';this.style.top='12px'" onblur="this.style.left='-9999px'">Zum Inhalt springen</a>

{kopfzeile(kanonisch_pfad)}

<main id="inhalt">{breadcrumbs(kanonisch_pfad)}{inhalt}</main>
{fusszeile()}{work_dialog() if 'data-work-open' in inhalt else ''}
{boosty_widget(path=kanonisch_pfad)}
<script src="assets/navigation.js?v={VER}" defer></script>
<script src="assets/kt.js?v={VER}" defer></script>
<script src="assets/motion.js?v={VER}" defer></script>
<script src="assets/creative.js?v={VER}" defer></script>
<script src="assets/boosty.js?v={VER}" defer></script>
{contact_script}
</body>
</html>
'''


# ── Wiederverwendbare Inhalts-Bausteine ──────────────────────────────────

def hero_klein(nummer, tag, zeilen, text, chips):
    chip_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
    return f'''
<section class="hero" style="padding-block:clamp(40px,6vw,84px) clamp(32px,4vw,56px)">
  <div class="shell" style="position:relative;z-index:1">
    {kicker(nummer, tag)}
    <h1 class="d1 wipe-3d recede-exit" style="margin:20px 0 26px;font-size:clamp(2.6rem,6.4vw,5.6rem)">{wipe(zeilen)}</h1>
    <p class="lede rise" style="--i:1;margin-bottom:28px">{text}</p>
    <div class="rise" style="--i:2;display:flex;flex-wrap:wrap;gap:9px">{chip_html}</div>
  </div>
</section>'''


def karten_grid(karten, spalten="g3", pop=True):
    """karten: Liste von (titel, text) oder (nr, titel, text)."""
    klasse = "pop" if pop else "rise"
    out = []
    for i, k in enumerate(karten):
        if len(k) == 2:
            titel, text = k
            kopf = f'<h3 class="d3" style="font-size:1.15rem;margin-bottom:11px">{titel}</h3>'
        else:
            nr, titel, text = k
            kopf = (f'<p class="tag" style="color:var(--acc);margin-bottom:13px">{nr}</p>'
                    f'<h3 class="d3" style="font-size:1.15rem;margin-bottom:11px">{titel}</h3>')
        out.append(f'<div class="card {klasse} ticks" style="--i:{i}">{kopf}'
                    f'<p style="color:var(--paper-dim);font-size:.92rem">{text}</p></div>')
    return f'<div class="{spalten} pop-wrap">{"".join(out)}</div>'


def punkte_liste(punkte):
    return '<ul style="list-style:none;margin:0;padding:0;border-top:1px solid var(--line-soft)">' + "".join(
        f'<li style="padding:12px 0;border-bottom:1px solid var(--line-soft);font-size:.9rem;'
        f'color:var(--paper-dim)">{p}</li>' for p in punkte) + '</ul>'


def faq_block(nummer, tag, h2_zeilen, fragen):
    items = "".join(
        f'''<details class="faq-item"><summary>{f}<span class="faq-plus"></span></summary><p>{a}</p></details>'''
        for f, a in fragen)
    return f'''
<section class="pad" style="background:var(--ink-2)">
  <div class="shell">
    {kicker(nummer, tag)}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(44px,5vw,64px)">{wipe(h2_zeilen)}</h2>
    <div class="faq-list rise" style="max-width:860px">{items}</div>
  </div>
</section>'''


def zitat_block(text, quelle):
    return f'''<figure class="rise" style="margin:clamp(52px,6vw,88px) 0 0;padding-top:clamp(36px,4vw,56px);border-top:1px solid var(--line)">
      <blockquote class="d3" style="margin:0 0 16px;max-width:34ch;font-weight:400">
        <span style="color:var(--acc)">&ldquo;</span>{text}</blockquote>
      <figcaption class="tag">{quelle}</figcaption>
    </figure>'''


def cta_block(tag, zeilen, text, cta1_label, cta1_href, cta2_label, cta2_href):
    return f'''
<section class="pad" style="overflow:hidden">
  <div class="shell" style="position:relative;z-index:1">
    <p class="tag rise">{tag}</p>
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px;max-width:20ch">{wipe(zeilen)}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:36px">{text}</p>
    <div class="rise" style="--i:2;display:flex;flex-wrap:wrap;gap:13px">
      <a href="{cta1_href}" class="btn btn-1">{cta1_label}</a>
      <a href="{cta2_href}" class="btn btn-2">{cta2_label}</a>
    </div>
  </div>
</section>'''


def stat_row(stats):
    """stats: Liste von (wert, suffix, label)."""
    out = "".join(
        f'''<div class="rise" style="--i:{i}">
          <div class="d3 mono" style="color:var(--acc)">{w}{s}</div>
          <p style="font-size:.84rem;color:var(--paper-mute);margin-top:7px">{l}</p>
        </div>''' for i, (w, s, l) in enumerate(stats))
    return f'<div class="g4" style="align-items:start;margin:clamp(40px,4.5vw,64px) 0">{out}</div>'
