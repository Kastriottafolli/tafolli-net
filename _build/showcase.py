"""Original vector illustrations for the company's service presentation."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent/'assets'/'showcase'

def svg(body, width=1200, height=600, dark=False):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {width} {height}" fill="none"><defs>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#e4e7ea"/><stop offset=".5" stop-color="#a6adb3"/><stop offset="1" stop-color="#e5e7e9"/></linearGradient>
<linearGradient id="blue" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#82b7ff"/><stop offset=".55" stop-color="#4d6cde"/><stop offset="1" stop-color="#b9b9fb"/></linearGradient>
<linearGradient id="orange" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffe8d7"/><stop offset="1" stop-color="#f5ad87"/></linearGradient>
<linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#f0f1f5"/></linearGradient>
<filter id="shadow" x="-40%" y="-40%" width="180%" height="220%"><feDropShadow dx="0" dy="20" stdDeviation="22" flood-color="#15223d" flood-opacity=".17"/></filter>
<filter id="soft" x="-40%" y="-40%" width="180%" height="220%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0a1021" flood-opacity=".1"/></filter>
</defs><g font-family="-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif">{body}</g></svg>'''

def laptop(x=150,y=55,w=800,h=420):
    # An illustrative custom workspace, without fabricated commercial figures.
    return f'''<g transform="translate({x} {y}) scale({w/800} {h/420})" filter="url(#shadow)">
<rect width="800" height="420" rx="22" fill="url(#metal)"/><rect x="4" y="4" width="792" height="410" rx="19" fill="#202124"/><rect x="13" y="14" width="774" height="385" rx="10" fill="#fff"/><circle cx="400" cy="8" r="2" fill="#747b82"/>
<path d="M13 24a10 10 0 0 1 10-10h754a10 10 0 0 1 10 10v26H13z" fill="#f5f5f7"/><circle cx="31" cy="32" r="4" fill="#d0d2d7"/><circle cx="45" cy="32" r="4" fill="#d0d2d7"/><circle cx="59" cy="32" r="4" fill="#d0d2d7"/><rect x="282" y="23" width="238" height="18" rx="6" fill="#e9e9ee"/><text x="400" y="36" text-anchor="middle" fill="#777b86" font-size="9">tafolli.net</text>
<rect x="13" y="50" width="145" height="349" fill="#f7f8fb"/><text x="32" y="83" fill="#1d1d1f" font-size="14" font-weight="700">TAFOLLI <tspan font-size="9">&amp; CO.</tspan></text>
<rect x="28" y="111" width="114" height="29" rx="8" fill="#e3edff"/><rect x="39" y="121" width="10" height="10" rx="3" fill="#0071e3"/><text x="58" y="130" fill="#1266b5" font-size="10">Workspace</text>
<g fill="#9ca4b1"><rect x="39" y="159" width="10" height="10" rx="3"/><rect x="58" y="161" width="55" height="6" rx="3"/><rect x="39" y="196" width="10" height="10" rx="3"/><rect x="58" y="198" width="45" height="6" rx="3"/><rect x="39" y="233" width="10" height="10" rx="3"/><rect x="58" y="235" width="60" height="6" rx="3"/></g>
<text x="189" y="91" fill="#8b8e98" font-size="9" letter-spacing="2">TAFOLLI &amp; CO.</text><text x="189" y="131" fill="#1d1d1f" font-size="30" font-weight="600">Your business. Connected.</text>
<rect x="189" y="157" width="344" height="208" rx="16" fill="url(#blue)"/><circle cx="361" cy="260" r="68" stroke="#ffffff3d" stroke-width="1"/><circle cx="361" cy="260" r="47" stroke="#ffffff66" stroke-width="1"/>
<path d="M316 260h90m-45-45v90" stroke="#fff" stroke-width="2" opacity=".7"/><rect x="337" y="236" width="48" height="48" rx="13" fill="#fff"/><path d="m350 260 8 8 15-17" stroke="#5578d8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g font-size="12" fill="#1d1d1f"><rect x="551" y="157" width="202" height="41" rx="10" fill="#f7f8fb"/><circle cx="571" cy="177" r="6" fill="#f0ad87"/><text x="589" y="182">Marketing</text><rect x="551" y="212" width="202" height="41" rx="10" fill="#f7f8fb"/><circle cx="571" cy="232" r="6" fill="#6b9ee8"/><text x="589" y="237">Technology</text><rect x="551" y="267" width="202" height="41" rx="10" fill="#f7f8fb"/><circle cx="571" cy="287" r="6" fill="#a59dce"/><text x="589" y="292">Consulting</text><rect x="551" y="322" width="202" height="41" rx="10" fill="#f7f8fb"/><circle cx="571" cy="342" r="6" fill="#6daaa5"/><text x="589" y="347">AI Automation</text></g>
<path d="M-60 417H860l-28 15a30 30 0 0 1-14 3H-18a30 30 0 0 1-14-3z" fill="url(#metal)"/><path d="M325 417h150l-8 6H333z" fill="#949da6"/></g>'''

def phone(x=860,y=160,s=1):
    return f'''<g transform="translate({x} {y}) scale({s})" filter="url(#shadow)"><rect x="-3" width="178" height="352" rx="33" fill="url(#metal)"/><rect width="172" height="350" rx="31" fill="#202124"/><rect x="6" y="7" width="160" height="336" rx="26" fill="#fff"/><rect x="63" y="15" width="46" height="12" rx="6" fill="#202124"/><circle cx="86" cy="107" r="41" fill="url(#blue)"/><path d="m71 108 11 11 20-25" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><text x="86" y="172" text-anchor="middle" fill="#1d1d1f" font-size="16" font-weight="600">Tafolli &amp; Co.</text><text x="86" y="192" text-anchor="middle" fill="#86868b" font-size="9">Marketing. Technology. AI.</text><g fill="#f0f2f7"><rect x="23" y="216" width="126" height="27" rx="8"/><rect x="23" y="251" width="126" height="27" rx="8"/></g><g fill="#aab4c5"><circle cx="37" cy="230" r="4"/><rect x="49" y="227" width="70" height="5" rx="2"/><circle cx="37" cy="265" r="4"/><rect x="49" y="262" width="57" height="5" rx="2"/></g><rect x="31" y="297" width="110" height="25" rx="13" fill="#0071e3"/><path d="M77 309h17m-5-5 5 5-5 5" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="59" y="334" width="54" height="3" rx="2" fill="#1d1d1f"/></g>'''

def build():
    ROOT.mkdir(exist_ok=True)
    (ROOT/'screen.svg').write_text(svg(laptop(0,0,800,420),800,420).replace('viewBox="0 0 800 420"','viewBox="13 14 774 385"'))
    (ROOT/'mobile-screen.svg').write_text(svg(phone(0,0,1),172,350).replace('viewBox="0 0 172 350"','viewBox="6 7 160 336"'))
    (ROOT/'workspace.svg').write_text(svg(laptop(180,40,790,415)+phone(880,156,.94),1200,550))
    (ROOT/'technology.svg').write_text(svg(laptop(80,65,800,420)+phone(865,190,.9),1100,560))
    marketing='''<g transform="translate(152 65) rotate(-9 180 210)" filter="url(#shadow)"><rect width="315" height="380" rx="8" fill="url(#orange)"/><text x="27" y="48" font-size="17" font-weight="600" fill="#532a22">TAFOLLI &amp; CO.</text><circle cx="157" cy="204" r="104" fill="#f7d2bb"/><circle cx="157" cy="204" r="73" fill="#efb590"/><circle cx="157" cy="204" r="43" fill="#f7d2bb"/><circle cx="157" cy="204" r="13" fill="#a95e3d"/><text x="27" y="346" fill="#75432f" font-size="11" letter-spacing="2">MARKETING · BRAND · CONTENT</text></g><g transform="translate(399 100) rotate(9 70 150)" filter="url(#shadow)"><rect width="174" height="296" rx="24" fill="#fff"/><rect x="9" y="9" width="156" height="278" rx="18" fill="#f6f3ef"/><text x="27" y="47" font-size="10" font-weight="600" fill="#342e29">Tafolli &amp; Co.</text><rect x="23" y="70" width="128" height="130" rx="9" fill="#e2a988"/><path d="M23 165c34-90 85 50 128-30v65H23" fill="#f8cfb5"/><circle cx="105" cy="102" r="15" fill="#fff4e8"/><rect x="24" y="222" width="108" height="5" rx="2" fill="#b3a99f"/><rect x="24" y="235" width="85" height="5" rx="2" fill="#d8cfc6"/><rect x="24" y="255" width="64" height="17" rx="9" fill="#c2845e"/></g>'''
    (ROOT/'marketing.svg').write_text(svg(marketing,720,500))
    consulting='''<g transform="translate(165 68) rotate(-8 180 180)" filter="url(#shadow)"><rect width="338" height="350" rx="15" fill="#fff"/><text x="32" y="47" font-size="13" fill="#86868b">TAFOLLI &amp; CO.</text><text x="32" y="89" font-size="25" font-weight="600" fill="#1d1d1f">Consulting.</text><rect x="32" y="111" width="174" height="5" rx="3" fill="#d2d2d7"/><path d="M49 166v112" stroke="#c4c7d2" stroke-width="2"/><g fill="#e7ecff" stroke="#abbce9"><circle cx="49" cy="162" r="15"/><circle cx="49" cy="218" r="15"/><circle cx="49" cy="274" r="15"/></g><g fill="#7d91bb"><rect x="83" y="156" width="161" height="9" rx="4"/><rect x="83" y="173" width="119" height="5" rx="2" opacity=".35"/><rect x="83" y="212" width="137" height="9" rx="4"/><rect x="83" y="229" width="175" height="5" rx="2" opacity=".35"/><rect x="83" y="268" width="168" height="9" rx="4"/><rect x="83" y="285" width="112" height="5" rx="2" opacity=".35"/></g></g><g transform="translate(429 255) rotate(9 80 75)" filter="url(#shadow)"><rect width="159" height="140" rx="18" fill="#8599cb"/><path d="m42 71 25 25 51-58" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>'''
    (ROOT/'consulting.svg').write_text(svg(consulting,720,500))
    automation='''<path d="M176 255h125m118 0h125" stroke="#8aa0c9" stroke-width="3"/><circle cx="239" cy="255" r="5" fill="#a9c4ff"/><circle cx="481" cy="255" r="5" fill="#a9c4ff"/><g filter="url(#shadow)"><rect x="80" y="185" width="130" height="140" rx="28" fill="#20232b" stroke="#444b59"/><path d="M120 222h50m-50 15h50m-50 15h36m-36 15h50m-50 15h25" stroke="#aebdd9" stroke-width="4" stroke-linecap="round"/><rect x="291" y="154" width="138" height="202" rx="35" fill="url(#blue)"/><path d="m334 239-16 16 16 16m52-32 16 16-16 16m-17-39-17 46" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><rect x="510" y="185" width="130" height="140" rx="28" fill="#20232b" stroke="#444b59"/><circle cx="575" cy="255" r="30" fill="#174f48"/><path d="m559 254 12 12 22-26" stroke="#9ce8d3" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'''
    (ROOT/'automation.svg').write_text(svg(automation,720,500,True))

def scene(lang='de',base=''):
    labels={
      'de':('Gestaltungsbeispiel: individuelle Software und mobile App.','Bewegung pausieren','Bewegung aktivieren'),
      'en':('Design concept: custom software and mobile app.','Pause motion','Enable motion'),
      'sq':('Koncept dizajni: softuer i personalizuar dhe aplikacion mobil.','Ndaloni lëvizjen','Aktivizoni lëvizjen'),
    }[lang]
    faces=''.join(f'<span class="d-cube-face d-cube-{side}">{text}</span>' for side,text in [('front','Web'),('back','App'),('right','AI'),('left','{ }'),('top','+'),('bottom','Co.')])
    return f'''<figure class="c-hero-visual scene-figure">
<div class="d-scene" data-scene3d aria-hidden="true"><div class="d-ground"></div><div class="d-rig"><div class="d-float">
<div class="d-laptop"><div class="d-screen-back"></div><div class="d-screen"><span class="d-camera"></span><img src="{base}assets/showcase/screen.svg" width="774" height="385" alt="" fetchpriority="high" decoding="async"></div><div class="d-deck"><div class="d-keys"></div><span></span></div></div>
<div class="d-phone"><img src="{base}assets/showcase/mobile-screen.svg" width="160" height="336" alt="" decoding="async"></div>
<div class="d-cube">{faces}</div><div class="d-floating-label"><i></i>Marketing · Consulting</div>
</div></div></div><figcaption><span>{labels[0]}</span><button class="motion-control" data-motion-toggle type="button" hidden aria-pressed="false" data-pause="{labels[1]}" data-play="{labels[2]}"><svg class="site-icon motion-control-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5 3v10M11 3v10" stroke="currentColor" stroke-width="2"/></svg><span>{labels[1]}</span></button></figcaption></figure>'''

if __name__=='__main__':build()
