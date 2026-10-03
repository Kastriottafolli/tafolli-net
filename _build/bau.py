# -*- coding: utf-8 -*-
"""Erzeugt die Startseite in drei Sprachen aus einer Quelle.

Zur Laufzeit bleibt die Seite, was sie war: reines HTML, CSS und JavaScript,
ohne Abhaengigkeit und ohne Anfrage an fremde Server. Der Bauschritt
existiert nur hier, damit drei Sprachen nicht dreimal von Hand gepflegt
werden muessen.
"""
import hashlib, pathlib, sys, html as H
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from inhalt_de import DE
from inhalt_en import EN
from inhalt_sq import SQ

WURZEL = pathlib.Path(__file__).resolve().parent.parent
LOGO = (pathlib.Path(__file__).parent / 'logo.svg').read_text()
SPRACHEN = [DE, EN, SQ]
VER = hashlib.sha256(
    (WURZEL / 'assets/kt.css').read_bytes() + (WURZEL / 'assets/kt.js').read_bytes()
).hexdigest()[:8]


def wipe(zeilen, start=0):
    """Ueberschrift, deren Zeilen hinter einer Maske hervorlaufen."""
    out = []
    for i, zeile in enumerate(zeilen):
        teile = zeile if isinstance(zeile, list) else [zeile]
        for t in teile:
            out.append(f'<span><span style="--i:{start + len(out)}">{t}</span></span>')
    return "".join(out)


def kicker(nummer, text):
    return f'<p class="tag rise"><span class="n">// {nummer}</span>&nbsp;&nbsp;{text}</p>'


def odometer(wert):
    """Rollende Ziffernkette. Der Wert steht zur Bauzeit fest, darum reicht
    reines CSS mit animation-timeline: view() — ohne Unterstuetzung zeigt
    die Spalte die Ziffer einfach sofort, kein Laufzeit-JS noetig."""
    spalten = "".join(
        f'<span class="odo-col"><span class="odo-strip" style="--t:{ziffer}">'
        + "".join(f'<span>{n}</span>' for n in range(10)) + '</span></span>'
        for ziffer in str(wert)
    )
    return f'<span class="odo">{spalten}</span>'


def seite(L):
    basis = '../' if L['dir'] else ''
    a = lambda p: f'{basis}{p}'

    # hreflang: jede Sprache zeigt auf jede, inklusive sich selbst.
    alt = "".join(
        f'<link rel="alternate" hreflang="{s["code"]}" href="https://tafolli.net/{s["dir"] + "/" if s["dir"] else ""}">'
        for s in SPRACHEN
    ) + '<link rel="alternate" hreflang="x-default" href="https://tafolli.net/">'

    kanonisch = f'https://tafolli.net/{L["dir"] + "/" if L["dir"] else ""}'

    sprachwahl = "".join(
        f'<a href="/{s["dir"] + "/" if s["dir"] else ""}" hreflang="{s["code"]}" '
        f'{"aria-current=\"true\" " if s["code"] == L["code"] else ""}'
        f'lang="{s["code"]}" title="{s["name"]}">{s["code"].upper()}</a>'
        for s in SPRACHEN
    )

    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in L['nav'])
    blatt = "".join(f'<a href="{h}">{t}</a>' for h, t in L['nav'])

    # ── Hero ──────────────────────────────────────────────────────────
    term = "".join(
        f'<div data-z style="opacity:0" class="{"c" if z.startswith("$") else ""}">{H.escape(z)}</div>'
        for z in L['term'])

    hero = f'''
<section class="hero">
  <div class="floor"></div>
  <div class="glow" style="width:620px;height:620px;background:rgba(0,224,140,.10);top:-280px;left:-180px"></div>
  <div class="orbit" aria-hidden="true"><i></i></div>
  <div class="shell" style="position:relative;z-index:1;padding-block:clamp(52px,7vw,104px)">
    <div class="split">
      <div>
        <p class="tag rise" style="display:flex;align-items:center;gap:11px;flex-wrap:wrap;margin-bottom:30px">
          <span class="dot pulse"></span> {L['hero_status']}
          <span style="color:var(--line)">│</span>
          <span>{L['hero_orte'][0]}</span>
        </p>
        <h1 class="d1 wipe-3d recede-exit" style="margin-bottom:32px">{wipe(L['hero_h1'])}</h1>
        <p class="lede rise" style="--i:1;margin-bottom:40px">{L['hero_text']}</p>
        <div class="rise" style="--i:2;display:flex;flex-wrap:wrap;gap:13px">
          <a href="{a('kontakt.html')}" class="btn btn-1">{L['hero_cta1']}</a>
          <a href="{a('rechner.html')}" class="btn btn-2">{L['hero_cta2']}</a>
        </div>
      </div>
      <div class="pop-wrap">
        <div class="pop ticks" style="--i:1;background:var(--ink-2);border:1px solid var(--line);
             box-shadow:0 60px 120px -50px rgba(0,0,0,.9)">
         <div class="tilt">
          <div style="display:flex;align-items:center;gap:7px;padding:13px 15px;border-bottom:1px solid var(--line-soft)">
            <span style="width:8px;height:8px;border-radius:999px;background:var(--line)"></span>
            <span style="width:8px;height:8px;border-radius:999px;background:var(--line)"></span>
            <span style="width:8px;height:8px;border-radius:999px;background:var(--acc)"></span>
            <span class="mono" style="font-size:.7rem;color:var(--paper-mute);margin-left:8px">{L['term_titel']}</span>
          </div>
          <div class="term" id="term" style="padding:19px 17px 24px;min-height:268px">{term}<span class="cursor blink"></span></div>
         </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

    # ── Kennzahlen ────────────────────────────────────────────────────
    stats = "".join(
        f'''<div class="rise" style="--i:{i}">
          <div class="d3 mono" style="color:var(--acc)">{odometer(z)}{s}</div>
          <p style="font-size:.86rem;color:var(--paper-mute);margin-top:7px">{t}</p>
        </div>''' for i, (z, s, t) in enumerate(L['stats']))

    kennzahlen = f'''
<section class="rule" style="background:var(--ink-2)">
  <div class="shell" style="padding-block:clamp(34px,4vw,54px)">
    <div class="g4" style="align-items:start">{stats}</div>
    <div class="rule" style="margin-top:clamp(26px,3vw,38px);padding-top:clamp(20px,2.4vw,28px);
         display:flex;gap:18px;align-items:baseline;flex-wrap:wrap">
      <span class="tag">{L['sprachen_label']}</span>
      <span class="mono" style="font-size:1rem;letter-spacing:.08em">{L['sprachen_wert']}</span>
      <span class="tag">{L['sprachen_stufe']}</span>
    </div>
  </div>
</section>'''

    # ── Laufband. Das einzige auf der Seite. ──────────────────────────
    spur = "".join(f'<span class="mono" style="font-size:.84rem;color:var(--paper-mute);white-space:nowrap">{h}</span>'
                   for h in L['haeuser'])
    marquee = f'''
<section style="padding-block:clamp(26px,3vw,38px);border-bottom:1px solid var(--line-soft)">
  <div class="marq"><div class="marq-track">{spur}</div><div class="marq-track" aria-hidden="true">{spur}</div></div>
</section>'''

    # ── Positionierung ────────────────────────────────────────────────
    chips = "".join(f'<span class="chip">{c}</span>' for c in L['pos_a_chips'])
    pos = f'''
<section class="pad">
  <div class="shell">
    {kicker('01', L['pos_tag'])}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px">{wipe(L['pos_h2'])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,76px)">{L['pos_text']}</p>
    <div class="g2 pop-wrap">
      <div class="card pop ticks" style="--i:0">
        <p class="tag" style="color:var(--acc);margin-bottom:16px">{L['pos_a_tag']}</p>
        <h3 class="d3" style="margin-bottom:15px">{L['pos_a_h3']}</h3>
        <p style="color:var(--paper-dim);font-size:.96rem;margin-bottom:24px">{L['pos_a_text']}</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px">{chips}</div>
      </div>
      <div class="card pop ticks" style="--i:1">
        <p class="tag" style="color:var(--acc);margin-bottom:16px">{L['pos_b_tag']}</p>
        <h3 class="d3" style="margin-bottom:15px">{L['pos_b_h3']}</h3>
        <p style="color:var(--paper-dim);font-size:.96rem;margin-bottom:24px">{L['pos_b_text']}</p>
        <pre class="mono" style="margin:0;font-size:.76rem;line-height:1.95;color:var(--paper-dim);overflow-x:auto"><span style="color:var(--acc)">class</span> Haus:
  <span style="color:var(--acc)">def</span> __init__(self, outlets, zimmer):
    self.outlets      = outlets
    self.wareneinsatz = <span style="color:var(--acc)">0.28</span>
    self.vertraege    = laden(<span style="color:var(--acc)">"getraenke"</span>)

  <span style="color:var(--acc)">def</span> optimieren(self):
    <span style="color:var(--acc)">for</span> v <span style="color:var(--acc)">in</span> self.vertraege:
      v.rueckverguetung = verhandeln(v)
    self.teamo = TeamO(sprachen=<span style="color:var(--acc)">3</span>)
    <span style="color:var(--acc)">return</span> self.deckungsbeitrag()</pre>
      </div>
    </div>
  </div>
</section>'''

    # ── Leistungsfelder als echter Sticky-Stack ───────────────────────
    karten = ""
    for i, (nr, label, titel, text, punkte, href, cta) in enumerate(L['felder']):
        lis = "".join(f'<li style="padding:11px 0;border-bottom:1px solid var(--line-soft);'
                      f'font-size:.9rem;color:var(--paper-dim)">{p}</li>' for p in punkte)
        karten += f'''
    <div class="stack-item">
     <div class="stack-pin">
      <div class="card ticks" style="background:var(--ink-2)">
        <div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px;align-items:baseline;margin-bottom:20px">
          <p class="tag"><span class="n">{nr}</span>&nbsp;&nbsp;{label}</p>
          <span class="mono" style="font-size:.7rem;color:var(--paper-mute)">{i+1} / {len(L['felder'])}</span>
        </div>
        <h3 class="d2" style="font-size:clamp(1.8rem,3.4vw,3rem);margin-bottom:18px">{titel}</h3>
        <div class="split" style="gap:clamp(24px,4vw,64px);align-items:start">
          <p style="color:var(--paper-dim);font-size:1rem">{text}</p>
          <ul style="list-style:none;margin:0;padding:0;border-top:1px solid var(--line-soft)">{lis}</ul>
        </div>
        <a href="{a(href) if not href.startswith('..') else href}" class="btn btn-2 lnk" style="margin-top:26px">
          {cta} <span class="arrow">&rarr;</span></a>
      </div>
     </div>
    </div>'''

    felder = f'''
<section id="felder" class="pad" style="scroll-margin-top:96px;background:var(--ink-2)">
  <div class="shell">
    {kicker('02', L['felder_tag'])}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px">{wipe(L['felder_h2'])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">{L['felder_text']}</p>
    <div class="stack" style="perspective:1600px">{karten}</div>
  </div>
</section>'''

    # ── Rechner ───────────────────────────────────────────────────────
    zeilen = "".join(
        f'''<div class="rise" style="--i:{i};display:flex;justify-content:space-between;gap:20px;
             padding:15px 0;border-bottom:1px solid var(--line-soft)">
          <span style="color:var(--paper-dim);font-size:.92rem">{k}</span>
          <span class="mono" style="color:var(--paper);font-size:.92rem;white-space:nowrap">{v}</span>
        </div>''' for i, (k, v) in enumerate(L['rech_zeilen']))

    rechner = f'''
<section id="rechner" class="pad" style="scroll-margin-top:96px">
  <div class="shell">
    <div class="split" style="align-items:start">
      <div>
        {kicker('03', L['rech_tag'])}
        <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px">{wipe(L['rech_h2'])}</h2>
        <p class="lede rise" style="--i:1;margin-bottom:34px">{L['rech_text']}</p>
        <a href="{a('rechner.html')}" class="btn btn-1 rise" style="--i:2">{L['rech_cta']}</a>
      </div>
      <div class="pop-wrap">
        <div class="card pop ticks">
          <p class="tag" style="margin-bottom:20px">{L['rech_titel']}</p>
          {zeilen}
          <div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding-top:22px">
            <span class="tag">{L['rech_summe_label']}</span>
            <span class="d3 mono" style="color:var(--acc)">{L['rech_summe']}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

    # ── Ablauf ────────────────────────────────────────────────────────
    schritte = "".join(
        f'''<div class="rise" style="--i:{i};padding:0 0 clamp(30px,3.4vw,46px) clamp(26px,3vw,46px)">
          <p class="mono" style="font-size:.72rem;letter-spacing:.2em;color:var(--acc);margin-bottom:10px">{nr}</p>
          <h3 class="d3" style="font-size:clamp(1.15rem,1.7vw,1.5rem);margin-bottom:10px">{t}</h3>
          <p style="color:var(--paper-dim);font-size:.94rem;max-width:62ch">{b}</p>
        </div>''' for i, (nr, t, b) in enumerate(L['abl']))

    ablauf = f'''
<section id="ablauf" class="pad" style="scroll-margin-top:96px;background:var(--ink-2)">
  <div class="shell">
    {kicker('04', L['abl_tag'])}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px">{wipe(L['abl_h2'])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:clamp(44px,5vw,72px)">{L['abl_text']}</p>
    <div class="thread">{schritte}</div>
  </div>
</section>'''

    # ── Wissen ────────────────────────────────────────────────────────
    artikel = "".join(
        f'''<a href="{h}" class="card pop lnk ticks" style="--i:{i};display:flex;flex-direction:column;gap:14px">
          <p class="tag" style="color:var(--acc)">{k}</p>
          <h3 class="d3" style="font-size:clamp(1.2rem,1.8vw,1.55rem)">{t}</h3>
          <p style="color:var(--paper-dim);font-size:.92rem;flex:1">{b}</p>
          <span style="color:var(--acc);font-size:.9rem;font-weight:600">{L['wis_lesen']} <span class="arrow">&rarr;</span></span>
        </a>''' for i, (k, t, b, h) in enumerate(
            [(k, t, b, (a(h) if not h.startswith('..') else h)) for k, t, b, h in L['wis']]))

    wissen = f'''
<section id="wissen" class="pad" style="scroll-margin-top:96px">
  <div class="shell">
    {kicker('05', L['wis_tag'])}
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 clamp(44px,5vw,72px)">{wipe(L['wis_h2'])}</h2>
    <div class="g3 pop-wrap">{artikel}</div>
    <figure class="rise" style="margin:clamp(52px,6vw,88px) 0 0;padding-top:clamp(36px,4vw,56px);border-top:1px solid var(--line)">
      <blockquote class="d3" style="margin:0 0 16px;max-width:30ch;font-weight:400">
        <span style="color:var(--acc)">&ldquo;</span>{L['zitat']}</blockquote>
      <figcaption class="tag">{L['zitat_quelle']}</figcaption>
    </figure>
  </div>
</section>'''

    # ── Abschluss ─────────────────────────────────────────────────────
    schluss = f'''
<section class="pad" style="overflow:hidden">
  <div class="floor"></div>
  <div class="glow" style="width:560px;height:560px;background:rgba(0,224,140,.11);bottom:-260px;right:-160px"></div>
  <div class="shell" style="position:relative;z-index:1">
    <p class="tag rise">{L['cta_tag']}</p>
    <h2 class="d2 wipe recede-exit" style="margin:20px 0 26px;max-width:18ch">{wipe(L['cta_h2'])}</h2>
    <p class="lede rise" style="--i:1;margin-bottom:38px">{L['cta_text']}</p>
    <div class="rise" style="--i:2;display:flex;flex-wrap:wrap;gap:13px">
      <a href="{a('kontakt.html')}" class="btn btn-1">{L['cta_1']}</a>
      <a href="{a('rechner.html')}" class="btn btn-2">{L['cta_2']}</a>
    </div>
  </div>
</section>'''

    # ── Fusszeile ─────────────────────────────────────────────────────
    sp = lambda titel, links: (
        f'<div><p class="tag" style="color:var(--paper);margin-bottom:17px">{titel}</p>' +
        "".join(f'<a href="{h if h.startswith("..") else a(h)}" class="lnk" '
                f'style="display:block;color:var(--paper-dim);font-size:.9rem;padding:5px 0">{t}</a>'
                for h, t in links) + '</div>')

    fuss = f'''
<footer class="rule" style="background:var(--ink-2);padding-block:clamp(52px,6vw,82px) 30px">
  <div class="shell">
    <div class="foot-grid">
      <div>
        <div style="color:var(--paper);margin-bottom:18px">{LOGO}</div>
        <p style="color:var(--paper-dim);font-size:.9rem;max-width:34ch;margin-bottom:18px">{L['foot_text']}</p>
        <p class="tag" style="color:var(--acc);display:flex;align-items:center;gap:9px">
          <span class="dot"></span> {L['foot_status']}</p>
      </div>
      {sp(L['foot_sp1'], L['foot_l1'])}
      {sp(L['foot_sp2'], L['foot_l2'])}
      <div>
        <p class="tag" style="color:var(--paper);margin-bottom:17px">{L['foot_sp3']}</p>
        <a href="tel:+4917664616146" class="lnk" style="display:block;color:var(--paper-dim);font-size:.9rem;padding:5px 0">0176 64616146</a>
        <a href="mailto:info@tafolli.net" class="lnk" style="display:block;color:var(--paper-dim);font-size:.9rem;padding:5px 0">info@tafolli.net</a>
        {"".join(f'<p style="color:var(--paper-dim);font-size:.9rem;padding:5px 0">{z}</p>' for z in L['foot_adresse'])}
      </div>
    </div>
    <div class="rule" style="padding-top:26px;display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between;align-items:center">
      <span style="font-size:.84rem;color:var(--paper-mute)">{L['foot_copy']}</span>
      <span style="display:flex;gap:22px">
        <a href="{a('impressum.html')}" style="font-size:.84rem;color:var(--paper-mute)">{L['foot_impressum']}</a>
        <a href="{a('datenschutz.html')}" style="font-size:.84rem;color:var(--paper-mute)">{L['foot_datenschutz']}</a>
      </span>
      <span class="mono" style="font-size:.72rem;color:var(--line)">{L['foot_shell']}</span>
    </div>
  </div>
</footer>'''

    return f'''<!doctype html>
<html lang="{L['code']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{L['titel']}</title>
<meta name="description" content="{L['beschreibung']}">
<meta name="author" content="Kastriot Tafolli">
<link rel="canonical" href="{kanonisch}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kastriot Tafolli">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:title" content="{L['titel']}">
<meta property="og:description" content="{L['beschreibung']}">
<meta property="og:url" content="{kanonisch}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#08090B">
<link rel="icon" type="image/svg+xml" href="{a('assets/favicon.svg')}">
<link rel="preload" as="font" type="font/woff2" href="{a('assets/schriften/space-grotesk-var.woff2')}" crossorigin>
<link rel="stylesheet" href="{a('assets/schriften.css')}?v={VER}">
<link rel="stylesheet" href="{a('assets/kt.css')}?v={VER}">
</head>
<body>
<script>(function(){{try{{if(sessionStorage.getItem("kt-intro")){{document.documentElement.className+=" intro-seen";}}else{{sessionStorage.setItem("kt-intro","1");}}}}catch(e){{}}}})();</script>
<div class="intro" aria-hidden="true">
  <div class="intro-veil"></div>
  <svg class="intro-mark" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="3" y="4" width="26" height="4" fill="currentColor"/>
    <rect x="14" y="4" width="4" height="24" fill="currentColor"/>
  </svg>
</div>
<div class="grain" aria-hidden="true"></div>

<a href="#inhalt" class="btn btn-1" style="position:absolute;left:-9999px;top:0;z-index:200"
   onfocus="this.style.left='12px';this.style.top='12px'" onblur="this.style.left='-9999px'">{L['skip']}</a>

<header class="bar">
  <div class="shell bar-in">
    <a href="{a('index.html') if not L['dir'] else '/' + L['dir'] + '/'}" style="flex-shrink:0;color:var(--paper)" aria-label="Kastriot Tafolli">{LOGO}</a>
    <nav class="nav" aria-label="{L['foot_sp1']}">{nav}</nav>
    <div style="display:flex;align-items:center;gap:11px;flex-shrink:0">
      <nav class="lang" aria-label="Sprache / Language / Gjuha">{sprachwahl}</nav>
      <a href="{a('kontakt.html')}" class="btn btn-1" style="padding:.8em 1.3em;font-size:.85rem">{L['cta_nav']}</a>
      <button type="button" class="burger" aria-label="{L['menu_auf']}" aria-expanded="false" aria-controls="sheet">
        <span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="sheet" id="sheet">{blatt}</div>
</header>

<main id="inhalt">{hero}{kennzahlen}{marquee}{pos}{felder}{rechner}{ablauf}{wissen}{schluss}</main>
{fuss}
<script src="{a('assets/kt.js')}?v={VER}" defer></script>
</body>
</html>
'''


if __name__ == '__main__':
    for L in SPRACHEN:
        ziel = WURZEL / (f"{L['dir']}/index.html" if L['dir'] else 'index.html')
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(seite(L))
        print(f"  {str(ziel.relative_to(WURZEL)):22} {len(ziel.read_text()):>7} Zeichen  [{L['name']}]")
    print(f"\nAsset-Version: {VER}")
