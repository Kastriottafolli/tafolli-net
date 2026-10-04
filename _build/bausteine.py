# -*- coding: utf-8 -*-
"""Gemeinsame Bausteine fuer alle Unterseiten. Kopf- und Fusszeile sind
identisch zur Startseite, damit die Seite wie aus einem Guss wirkt."""
import hashlib, pathlib
from brand import lockup, intro

WURZEL = pathlib.Path(__file__).resolve().parent.parent
LOGO = lockup()
VER = hashlib.sha256(
    (WURZEL / 'assets/kt.css').read_bytes() + (WURZEL / 'assets/kt.js').read_bytes()
    + (WURZEL / 'assets/experience.css').read_bytes()
    + (WURZEL / 'assets/brand.js').read_bytes()
).hexdigest()[:8]

NAV = [
    ("ki-automatisierung.html", "AI Automation"),
    ("ueber-mich.html", "Über mich"),
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
    kanonisch = f"https://tafolli.net/{kanonisch_pfad}"
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
<meta name="author" content="Kastriot Tafolli">
<link rel="canonical" href="{kanonisch}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kastriot Tafolli">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{beschreibung}">
<meta property="og:url" content="{kanonisch}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#f3f1e9">
<link rel="icon" type="image/svg+xml" href="assets/brand/favicon.svg">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" as="image" href="assets/brand/logo-mark.webp" fetchpriority="high">
<link rel="preload" as="font" type="font/woff2" href="assets/schriften/space-grotesk-var.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/schriften/ibm-plex-sans-400.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/schriften/bodoni-moda-400-italic.woff2" crossorigin>
<link rel="stylesheet" href="assets/schriften.css?v={VER}">
<link rel="stylesheet" href="assets/kt.css?v={VER}">
<link rel="stylesheet" href="assets/experience.css?v={VER}">
</head>'''


def kopfzeile(aktiv):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"true\"" if h == aktiv else ""}>{t}</a>'
        for h, t in NAV)
    blatt = nav
    sprachwahl = (
        '<a href="/" hreflang="de" aria-current="true" lang="de" title="Deutsch">DE</a>'
        '<a href="/en/" hreflang="en" lang="en" title="English">EN</a>'
        '<a href="/sq/" hreflang="sq" lang="sq" title="Shqip">SQ</a>'
    )
    return f'''<header class="bar">
  <div class="shell bar-in">
    <a href="index.html" style="flex-shrink:0;color:var(--paper)" aria-label="Kastriot Tafolli">{LOGO}</a>
    <nav class="nav" aria-label="Seiten">{nav}</nav>
    <div style="display:flex;align-items:center;gap:11px;flex-shrink:0">
      <nav class="lang" aria-label="Sprache / Language / Gjuha">{sprachwahl}</nav>
      <a href="kontakt.html" class="btn btn-1" style="padding:.8em 1.3em;font-size:.85rem">Gespräch</a>
      <button type="button" class="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="sheet">
        <span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="sheet" id="sheet">{blatt}</div>
</header>'''


def fusszeile():
    sp = lambda titel, links: (
        f'<div><p class="tag" style="color:var(--paper);margin-bottom:17px">{titel}</p>' +
        "".join(f'<a href="{h}" class="lnk" style="display:block;color:var(--paper-dim);'
                f'font-size:.9rem;padding:5px 0">{t}</a>' for h, t in links) + '</div>')
    return f'''<footer class="rule" style="background:var(--ink-2);padding-block:clamp(52px,6vw,82px) 30px">
  <div class="shell">
    <div class="foot-grid">
      <div>
        <div style="color:var(--paper);margin-bottom:18px">{LOGO}</div>
        <p style="color:var(--paper-dim);font-size:.9rem;max-width:34ch;margin-bottom:18px">Gastronomische Führung, Digitalisierung, KI-Automatisierung und KI-Lösungen für Hotellerie und Gastronomie.</p>
        <p class="tag" style="color:var(--acc);display:flex;align-items:center;gap:9px">
          <span class="dot"></span> TB SOLUTIONS · ONLINE</p>
      </div>
      {sp("Seiten", FOOT_L1)}
      {sp("Schwerpunkte", FOOT_L2)}
      <div>
        <p class="tag" style="color:var(--paper);margin-bottom:17px">Kontakt</p>
        <a href="tel:+4917664616146" class="lnk" style="display:block;color:var(--paper-dim);font-size:.9rem;padding:5px 0">0176 64616146</a>
        <a href="mailto:info@tafolli.net" class="lnk" style="display:block;color:var(--paper-dim);font-size:.9rem;padding:5px 0">info@tafolli.net</a>
        <p style="color:var(--paper-dim);font-size:.9rem;padding:5px 0">Hauptstraße 1, 18609 Ostseebad Binz</p>
        <p style="color:var(--paper-dim);font-size:.9rem;padding:5px 0">Schluchsee, Hochschwarzwald</p>
      </div>
    </div>
    <div class="rule" style="padding-top:26px;display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center">
      <span style="font-size:.84rem;color:var(--paper-mute)">© 2026 Kastriot Tafolli · tafolli.net · Ostseebad Rügen / Schluchsee</span>
      <span style="display:flex;gap:22px">
        <a href="impressum.html" style="font-size:.84rem;color:var(--paper-mute)">Impressum</a>
        <a href="datenschutz.html" style="font-size:.84rem;color:var(--paper-mute)">Datenschutz</a>
      </span>
      <span class="mono" style="font-size:.72rem;color:var(--paper-mute)">HOTELLERIE · GASTRONOMIE · TECHNOLOGIE</span>
    </div>
  </div>
</footer>'''


def seite_rahmen(aktiv, titel, beschreibung, kanonisch_pfad, inhalt):
    return f'''{seiten_kopf(titel, beschreibung, kanonisch_pfad)}
<body>
{intro()}
<div class="grain" aria-hidden="true"></div>

<a href="#inhalt" class="btn btn-1" style="position:absolute;left:-9999px;top:0;z-index:200"
   onfocus="this.style.left='12px';this.style.top='12px'" onblur="this.style.left='-9999px'">Zum Inhalt springen</a>

{kopfzeile(aktiv)}

<main id="inhalt">{inhalt}</main>
{fusszeile()}
<script src="assets/brand.js?v={VER}" defer></script>
<script src="assets/kt.js?v={VER}" defer></script>
</body>
</html>
'''


# ── Wiederverwendbare Inhalts-Bausteine ──────────────────────────────────

def hero_klein(nummer, tag, zeilen, text, chips):
    chip_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
    return f'''
<section class="hero" style="padding-block:clamp(40px,6vw,84px) clamp(32px,4vw,56px)">
  <div class="floor"></div>
  <div class="glow" style="width:520px;height:520px;background:rgba(0,224,140,.09);top:-240px;left:-160px"></div>
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
  <div class="floor"></div>
  <div class="glow" style="width:520px;height:520px;background:rgba(0,224,140,.1);bottom:-240px;right:-150px"></div>
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
