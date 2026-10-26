"""Real work, product imagery and accessible visual case-study components."""
from html import escape as e

PROJECTS = [
 dict(key='boost', name='Tafolli Boost', url='https://tafolliboost.com/', file='tafolli-boost-desktop.webp', category='KI · Web-App · Produktentwicklung', text='Unser eigenes Produkt: eine Web-App, die Lebenslauf und Stellenangebot in bearbeitbare Bewerbungsdokumente übersetzt.'),
]

LANG = {
 'de':dict(selected='Ausgewählte Projekte', preview='Vorschau öffnen', visit='Website besuchen', close='Vorschau schließen', choose='Projekt im Laptop auswählen', view='Aktuelle Website-Ansichten aus unseren Projekten.', boost_label='EIGENES PRODUKT / TAFOLLI BOOST', boost_title='KI, die etwas<br>für Menschen tut.', boost_text='Eine Bewerbung beginnt oft vor einem leeren Blatt. Tafolli Boost macht aus einem Lebenslauf und einer Stellenanzeige vier bearbeitbare Dokumente. Mit einer klaren Oberfläche, drei Sprachen und Boosty als Begleiter.', boost_cta='Tafolli Boost entdecken', boost_note='Web-App · Deutsch, English, Shqip · PDF & Word', docs=['Lebenslauf','Anschreiben','Motivation','E-Mail'], gallery_title='Arbeit, die man<br>ansehen kann.', gallery_text='Eigene Produkte und ausgewählte Website-Projekte. Öffnen Sie eine Vorschau oder erleben Sie die jeweilige Website direkt.'),
 'en':dict(selected='Selected projects', preview='Open preview', visit='Visit website', close='Close preview', choose='Choose a project in the laptop', view='Current website views from our projects.', boost_label='OUR OWN PRODUCT / TAFOLLI BOOST', boost_title='AI that does something<br>for people.', boost_text='A job application often begins with a blank page. Tafolli Boost turns a CV and a job advert into four editable documents, with a clear interface, three languages and Boosty as a guide.', boost_cta='Explore Tafolli Boost', boost_note='Web app · Deutsch, English, Shqip · PDF & Word', docs=['CV','Cover letter','Motivation','Email'], gallery_title='Work you<br>can explore.', gallery_text='Our own products and selected website projects. Open a preview or experience each website directly.'),
 'sq':dict(selected='Projekte të përzgjedhura', preview='Hap pamjen', visit='Vizito faqen', close='Mbyll pamjen', choose='Zgjidh projektin në laptop', view='Pamje aktuale të faqeve nga projektet tona.', boost_label='PRODUKTI YNË / TAFOLLI BOOST', boost_title='AI që bën diçka<br>për njerëzit.', boost_text='Një aplikim për punë shpesh fillon me një faqe bosh. Tafolli Boost krijon katër dokumente të redaktueshme nga CV-ja dhe shpallja e punës, me një ndërfaqe të qartë, tri gjuhë dhe Boosty si udhërrëfyes.', boost_cta='Zbulo Tafolli Boost', boost_note='Aplikacion web · Deutsch, English, Shqip · PDF & Word', docs=['CV','Letër aplikimi','Motivimi','Email'], gallery_title='Punë që mund<br>ta shikoni.', gallery_text='Produktet tona dhe projekte të përzgjedhura web. Hapni një pamje ose vizitoni secilën faqe.'),
}
TRANSLATIONS={
 'en':[
 ('AI · Web app · Product development','From a CV and job advert to an editable application package. A web application with AI, document export and its own visual identity.'),
 ('Web design · 3D · Product communication','Glass manufacturing explained digitally, with a spatial product presentation, clear content and a direct path to an enquiry.'),
 ('Brand · Website · Local search','A clear digital presence for a construction business. Services, site photography, a before-and-after comparison and a calculator make the offer tangible.'),
 ('Hospitality · Website · Reservations','A restaurant website that conveys its atmosphere and connects the key steps: menu, opening hours and table reservations.')],
 'sq':[
 ('AI · Aplikacion web · Zhvillim produkti','Nga CV-ja dhe shpallja e punës te dokumentet e redaktueshme të aplikimit. Aplikacion web me AI, eksport dokumentesh dhe identitetin e vet vizual.'),
 ('Dizajn web · 3D · Komunikim produkti','Prodhimi i xhamit i shpjeguar me një prezantim hapësinor, përmbajtje të kuptueshme dhe rrugë të drejtpërdrejtë drejt kërkesës për ofertë.'),
 ('Markë · Website · Kërkim lokal','Prani digjitale e qartë për një kompani ndërtimi. Shërbimet, fotot, krahasimi para/pas dhe kalkulatori e bëjnë ofertën të prekshme.'),
 ('Hospitality · Website · Rezervime','Një faqe restoranti që përcjell atmosferën dhe lidh menynë, orarin dhe rezervimin e tavolinave.')],
}

def project_data(lang='de'):
 result=[dict(p) for p in PROJECTS]
 if lang in TRANSLATIONS:
  for p,(category,text) in zip(result,TRANSLATIONS[lang]):p.update(category=category,text=text)
 return result

def image(file,alt='',base='',cls='',eager=False):
 return f'<img class="{cls}" src="{base}assets/work/{file}" alt="{e(alt)}" width="1280" height="720" loading="{'eager' if eager else 'lazy'}" decoding="async">'

def scene(lang='de',base=''):
 L=LANG[lang]; projects=project_data(lang); first=projects[0]
 buttons=''.join(f'<button type="button" class="project-pick" data-project-pick data-src="{base}assets/work/{p["file"]}" data-name="{e(p["name"])}" data-url="{e(p["url"])}" aria-pressed="{str(i==0).lower()}"><span class="project-dot project-dot-{p["key"]}"></span>{e(p["name"])}</button>' for i,p in enumerate(projects))
 return f'''<figure class="c-hero-visual scene-figure real-scene" data-project-viewer>
<div class="own-product-label">TAFOLLI BOOST <span>{ {"de":"Unser eigenes KI-Produkt","en":"Our own AI product","sq":"Produkti ynë me AI"}[lang] }</span></div>
<div class="d-scene" data-scene3d><div class="d-ground"></div><div class="d-rig"><div class="d-float">
<div class="d-laptop"><div class="d-screen-back"></div><div class="d-screen"><span class="d-camera"></span><img data-project-screen src="{base}assets/work/{first['file']}" width="1280" height="460" alt="{e(first['name'])} – Website" fetchpriority="high" decoding="async"></div><div class="d-deck"><div class="d-keys"></div><span></span></div></div>
<div class="d-product-orbit" aria-hidden="true"><img src="{base}assets/work/boosty.webp" width="400" height="400" alt=""><span>Meet Boosty.</span></div>
<a class="d-floating-label" data-project-visit href="{first['url']}" target="_blank" rel="noopener noreferrer"><i></i><span data-project-name>{e(first['name'])}</span><b aria-hidden="true">↗</b></a>
</div></div></div><figcaption><span>{ {'de':'Tafolli Boost – entwickelt von Tafolli & Co.','en':'Tafolli Boost – built by Tafolli & Co.','sq':'Tafolli Boost – zhvilluar nga Tafolli & Co.'}[lang] }</span><button class="motion-control" data-motion-toggle type="button" hidden aria-pressed="false" data-pause="{'Pause motion' if lang=='en' else 'Ndaloni lëvizjen' if lang=='sq' else 'Bewegung pausieren'}" data-play="{'Enable motion' if lang=='en' else 'Aktivizoni lëvizjen' if lang=='sq' else 'Bewegung aktivieren'}"><svg class="site-icon motion-control-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M5 3v10M11 3v10" stroke="currentColor" stroke-width="2"/></svg><span>{'Pause motion' if lang=='en' else 'Ndaloni lëvizjen' if lang=='sq' else 'Bewegung pausieren'}</span></button></figcaption></figure>'''

def gallery(lang='de',base='',heading=True):
 L=LANG[lang]; cards=''
 for i,p in enumerate(project_data(lang)):
  cards+=f'''<article class="work-card work-card-{p['key']}"><button class="work-image-button" type="button" data-work-open data-image="{base}assets/work/{p['file']}" data-title="{e(p['name'])}" data-url="{p['url']}" aria-label="{L['preview']}: {e(p['name'])}"><div class="work-browser"><i></i><i></i><i></i><span>{p['url'].split('//')[1].strip('/')}</span></div>{image(p['file'],p['name']+' – Website',base)}<span class="work-zoom">{L['preview']} <b aria-hidden="true">↗</b></span></button><div class="work-card-copy"><p class="v-kicker">{e(p['category'])}</p><h3><a href="{p['url']}" target="_blank" rel="noopener noreferrer">{e(p['name'])}<span aria-hidden="true">↗</span></a></h3><p>{e(p['text'])}</p></div></article>'''
 head=f'<div class="visual-section-heading"><div><p class="v-kicker">{L["selected"]}</p><h2>{L["gallery_title"]}</h2></div><p>{L["gallery_text"]}</p></div>' if heading else ''
 return f'<section class="real-work-section" id="projektgalerie"><div class="shell">{head}<div class="real-work-grid">{cards}</div></div></section>'

def boost(lang='de',base=''):
 L=LANG[lang]
 docs=''.join(f'<span><i aria-hidden="true">0{i+1}</i>{e(t)}</span>' for i,t in enumerate(L['docs']))
 return f'''<section class="boost-feature"><div class="shell boost-feature-grid"><div class="boost-feature-copy"><p class="v-kicker">{L['boost_label']}</p><h2>{L['boost_title']}</h2><p>{L['boost_text']}</p><div class="boost-documents">{docs}</div><a class="btn btn-1" href="https://tafolliboost.com/" target="_blank" rel="noopener noreferrer">{L['boost_cta']} ↗</a><small>{L['boost_note']}</small></div><div class="boost-product-stage"><div class="boost-orbit boost-orbit-one"></div><div class="boost-orbit boost-orbit-two"></div><div class="boost-product-screen">{image('tafolli-boost-desktop.webp','Tafolli Boost – Bewerbungsassistent',base)}<span>tafolliboost.com</span></div><img class="boost-mascot" src="{base}assets/work/boosty.webp" width="600" height="600" alt="Boosty, der Begleiter von Tafolli Boost" loading="lazy"><span class="boost-sticker">4 {'documents' if lang=='en' else 'dokumente' if lang=='sq' else 'Dokumente'}.<br>1 {'next step' if lang=='en' else 'hap i ri' if lang=='sq' else 'nächster Schritt'}.</span></div></div></section>'''

def dialog(lang='de'):
 L=LANG[lang]
 return f'<dialog class="work-dialog" aria-labelledby="work-dialog-title"><div class="work-dialog-bar"><h2 id="work-dialog-title"></h2><button type="button" data-work-close aria-label="{L["close"]}">×</button></div><img data-work-full alt=""><div class="work-dialog-footer"><span>{L["selected"]}</span><a data-work-live target="_blank" rel="noopener noreferrer">{L["visit"]} ↗</a></div></dialog>'
