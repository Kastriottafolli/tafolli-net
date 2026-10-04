"""One TAFOLLI identity across navigation, footer, references and every page entry."""
def lockup(base=''):
    return f'<span class="tafolli-brand"><img class="tafolli-brand-mark" src="{base}assets/brand/logo-mark.webp" width="42" height="42" alt="" decoding="async"><span class="tafolli-brand-name">TAFOLLI</span></span>'


def intro(lang='de',base=''):
    label,tagline={
      'de':('HOTELLERIE × TECHNOLOGIE','Menschliche Ideen. Intelligente Systeme.'),
      'en':('HOSPITALITY × TECHNOLOGY','Human ideas. Intelligent systems.'),
      'sq':('HOTELERI × TEKNOLOGJI','Ide njerëzore. Sisteme inteligjente.'),
    }[lang]
    paths=['M20 80H90L135 125H175','M0 200H160','M35 315H95L135 275H180','M380 80H310L265 125H225','M400 200H240','M365 315H305L265 275H220']
    network=''.join(f'<path d="{d}" pathLength="1" style="--branch:{i}"/>' for i,d in enumerate(paths))
    return f'''<div class="brand-intro" aria-hidden="true" hidden><div class="brand-intro-center"><p class="brand-intro-label">{label}</p><div class="brand-intro-art"><svg class="brand-intro-network" viewBox="0 0 400 400" fill="none">{network}<g class="brand-intro-nodes"><circle cx="20" cy="80" r="3"/><circle cx="0" cy="200" r="3"/><circle cx="35" cy="315" r="3"/><circle cx="380" cy="80" r="3"/><circle cx="400" cy="200" r="3"/><circle cx="365" cy="315" r="3"/></g></svg><div class="brand-intro-symbol"><img class="brand-intro-left" src="{base}assets/brand/logo-mark.webp" width="180" height="180" alt=""><img class="brand-intro-right" src="{base}assets/brand/logo-mark.webp" width="180" height="180" alt=""></div><div class="brand-intro-halo"></div></div><div class="brand-intro-name">TAFOLLI</div><p class="brand-intro-tagline">{tagline}</p><span class="brand-intro-rule"></span></div></div>'''
