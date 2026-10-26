"""Tafolli & Co. neural-code identity, evolved from the existing brain symbol."""
from pathlib import Path

NAME = 'Tafolli & Co.'
HTML_NAME = 'Tafolli &amp; Co.'
_ROOT = Path(__file__).resolve().parent.parent
MARK = 'assets/brand/tafolli-co-neural-code.webp'
FAVICON = 'assets/brand/tafolli-co-neural-code-icon.svg'
TOUCH_ICON = 'assets/brand/tafolli-co-neural-code-touch.png'

def lockup(base=''):
    return f'<span class="tafolli-brand"><img class="tafolli-brand-mark" src="{base}{MARK}" width="42" height="42" alt="" decoding="async"><span class="tafolli-brand-name">TAFOLLI<span class="tafolli-brand-company"> &amp; CO.</span></span></span>'


def intro(lang='de',base=''):
    label,tagline={
      'de':('MARKETING · TECHNOLOGY · CONSULTING · AI','Intelligente Systeme. Starke Sichtbarkeit.'),
      'en':('MARKETING · TECHNOLOGY · CONSULTING · AI','Intelligent systems. A stronger presence.'),
      'sq':('MARKETING · TEKNOLOGJI · KËSHILLIM · IA','Sisteme inteligjente. Prani më e fortë.'),
    }[lang]
    paths=['M20 80H90L135 125H175','M0 200H160','M35 315H95L135 275H180','M380 80H310L265 125H225','M400 200H240','M365 315H305L265 275H220']
    network=''.join(f'<path d="{d}" pathLength="1" style="--branch:{i}"/>' for i,d in enumerate(paths))
    return f'''<div class="page-loader" id="page-loader" aria-hidden="true" hidden><div class="page-loader-center"><p class="page-loader-label">{label}</p><div class="page-loader-art"><svg class="page-loader-network" viewBox="0 0 400 400" fill="none" aria-hidden="true" focusable="false">{network}<g class="page-loader-nodes"><circle cx="20" cy="80" r="3"/><circle cx="0" cy="200" r="3"/><circle cx="35" cy="315" r="3"/><circle cx="380" cy="80" r="3"/><circle cx="400" cy="200" r="3"/><circle cx="365" cy="315" r="3"/></g></svg><div class="page-loader-symbol"><img class="page-loader-left" src="{base}{MARK}" width="180" height="180" alt="" fetchpriority="high"><img class="page-loader-right" src="{base}{MARK}" width="180" height="180" alt=""></div><div class="page-loader-halo"></div></div><div class="page-loader-name">TAFOLLI<span> &amp; CO.</span></div><p class="page-loader-tagline">{tagline}</p><span class="page-loader-line"><i></i></span></div></div>'''
