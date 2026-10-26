"""Lightweight, owned illustrations for the individual detail-page subjects."""
from html import escape as e
from brand import MARK

PATHS={
 'arrow':'M5 12H19M13 6L19 12L13 18',
 'check':'M5 12L10 17L20 7',
 'code':'M8 6L2 12L8 18M16 6L22 12L16 18M14 3L10 21',
 'shield':'M12 2L21 6V12C21 17 17 20 12 23C7 20 3 17 3 12V6ZM8 12L11 15L17 8',
 'mail':'M3 5H21V19H3ZM3 5L12 13L21 5',
 'pin':'M18 10C18 15 12 22 12 22S6 15 6 10A6 6 0 0 1 18 10ZM14 10A2 2 0 1 1 10 10A2 2 0 1 1 14 10',
 'chart':'M3 3V21H22M6 16L11 10L15 13L21 5',
 'calendar':'M3 5H21V22H3ZM3 10H21M8 2V7M16 2V7M7 14H10M14 14H17M7 18H10',
 'person':'M16 7A4 4 0 1 1 8 7A4 4 0 1 1 16 7M4 22V19C4 12 20 12 20 19V22',
 'box':'M2 6L12 1L22 6V18L12 23L2 18ZM2 6L12 12L22 6M12 12V23M7 4L17 9',
 'search':'M15 9A6 6 0 1 1 3 9A6 6 0 1 1 15 9M13 14L21 22',
 'globe':'M22 12A10 10 0 1 1 2 12A10 10 0 1 1 22 12M2 12H22M12 2C5 8 5 16 12 22C19 16 19 8 12 2',
 'spark':'M12 1L15 9L23 12L15 15L12 23L9 15L1 12L9 9Z',
 'phone':'M6 2H18V22H6ZM10 5H14M11 19H13',
 'document':'M5 2H15L20 7V22H5ZM15 2V7H20M8 11H17M8 15H17M8 19H14',
}

def glyph(name):
    return f'<svg class="detail-glyph" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="{PATHS.get(name,PATHS["spark"])}"/></svg>'

def chrome(name):
    return f'<div class="ds-chrome"><span><i></i><i></i><i></i></span><small>{e(name)}</small><b>{glyph("arrow")}</b></div>'

def browser(title,content,cls=''):
    return f'<div class="ds-browser {cls}">{chrome(title)}<div class="ds-browser-inner">{content}</div></div>'

def focus_cards(labels,icon='document'):
    return ''.join(f'<div class="ds-focus-card" data-detail-item="{i}"><span>{glyph(icon)}</span><b>{e(label)}</b><i></i><i></i></div>' for i,label in enumerate(labels))

def scene(config):
    kind=config['kind'];labels=[x[0] for x in config['topics']];labels3=labels[:3]
    mark=f'<img src="{MARK}" width="94" height="94" alt="" decoding="async">'
    kicker='KONZEPT' if config['lang']=='de' else 'KONCEPT'
    content=''
    if kind=='calendar':
        days=''.join(f'<i class="{"calendar-mark" if i in {3,11,19,24} else ""}">{i+1 if i<30 else ""}</i>' for i in range(35))
        content=browser('Vereinsleben / concept',f'<div class="ds-site-nav"><b>Zusammen mehr bewegen.</b>{glyph("calendar")}</div><div class="ds-club-calendar">{days}</div><div class="ds-club-notes">'+focus_cards(labels3,'person')+'</div>')
        content+='<div class="ds-floating ds-phone-tag">'+glyph('calendar')+'<b>Termine.<br>Gemeinsam im Blick.</b></div>'
    elif kind=='maintenance':
        content=browser('website care / concept','<div class="ds-site-nav"><b>Ihr Auftritt. Gut betreut.</b>'+glyph('globe')+'</div><div class="ds-care-loop"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="39"/><path d="M50 11A39 39 0 1 1 11 50"/></svg>'+glyph('check')+'</div><div class="ds-care-tasks">'+''.join(f'<div data-detail-item="{i}">{glyph("check")}<b>{e(label)}</b><span></span></div>' for i,label in enumerate(labels3))+'</div>')
        content+='<div class="ds-floating ds-phone-tag">'+glyph('document')+'<b>Ändern. Prüfen.<br>Rückmeldung geben.</b></div>'
    elif kind in {'browser','landing','craft'}:
        top={'landing':'Ein Angebot. Ein nächster Schritt.','craft':'Gute Arbeit. Gut sichtbar.','calendar':'Zusammen mehr bewegen.','browser':'Ein Auftritt mit Charakter.'}[kind]
        decorative='calendar' if kind=='calendar' else 'box' if kind=='craft' else 'globe'
        features=focus_cards(labels3,decorative)
        content=browser('website / design concept',f'<div class="ds-site-nav"><b>Ihre Marke.</b><i></i><i></i><span>{glyph("arrow")}</span></div><div class="ds-site-hero"><small>{kicker} / WEBSITE</small><strong>{top}</strong><div class="ds-site-object">{glyph(decorative)}<i></i></div><em>Kontakt</em></div><div class="ds-site-features">{features}</div>')
        content+='<div class="ds-floating ds-phone-tag">'+glyph('phone')+'<div><small>RESPONSIVE</small><b>Desktop &amp; Mobile</b></div></div>'
    elif kind=='software':
        content=browser('Tafolli Boost / eigenes Produkt','<img class="ds-real-screen" src="assets/work/tafolli-boost-desktop.webp" width="1280" height="800" alt="" decoding="async">')
        content+='<div class="ds-code-stack">'+''.join(f'<div data-detail-item="{i}"><span>{glyph("code")}</span><b>{e(label)}</b><i></i></div>' for i,label in enumerate(labels3))+'</div>'
    elif kind in {'app','webapp'}:
        if kind=='app':
            content='<div class="ds-phone-row">'+''.join(f'<div class="ds-device" data-detail-item="{i}"><span class="ds-device-notch"></span><small>{e(label)}</small><div class="ds-app-symbol">{glyph("spark" if i==0 else "calendar" if i==1 else "globe")}</div><b>Ein guter<br>nächster Schritt.</b><div class="ds-app-rows"><i></i><i></i><i></i></div><span class="ds-app-action">{glyph("arrow")}</span></div>' for i,label in enumerate(labels3))+'</div>'
        else:
            content=browser('workspace / concept',f'<div class="ds-workspace"><aside><b>{glyph("code")}</b><i></i><i></i><i></i></aside><div><small>IHRE ANWENDUNG</small><strong>Alles an einem Ort.</strong><div class="ds-app-workflow">'+focus_cards(labels3,'document')+'</div><div class="ds-app-table"><i></i><i></i><i></i></div></div></div>')
            content+='<div class="ds-floating ds-app-tag">'+glyph('check')+'<b>Ein Ablauf.<br>Ihr Werkzeug.</b></div>'
    elif kind in {'automation','health','product','knowledge'}:
        central='AI' if kind!='knowledge' else 'Wissen'
        cards=''.join(f'<div class="ds-ai-document ds-ai-document-{i}" data-detail-item="{i}"><span>{glyph("mail" if i==0 else "document" if i==1 else "check")}</span><b>{e(label)}</b><i></i><i></i></div>' for i,label in enumerate(labels3))
        content=f'<svg class="ds-connectors" viewBox="0 0 560 400"><path d="M90 100C240 100 150 200 280 200S380 100 470 100M90 300C240 300 150 200 280 200S380 300 470 300"/><path class="ds-signal" d="M90 100C240 100 150 200 280 200S380 300 470 300"/></svg><div class="ds-ai-orbits"><i></i><i></i><i></i></div><div class="ds-ai-core">{mark if kind=="product" else "<b>"+central+"</b>"}<span>{"QUELLEN & KONTEXT" if kind=="knowledge" else "MIT MENSCHLICHER FREIGABE"}</span></div>{cards}'
    elif kind=='security':
        content='<div class="ds-shield-rings"><i></i><i></i><i></i></div><div class="ds-shield">'+glyph('shield')+'</div>'
        content+=''.join(f'<div class="ds-security-node ds-security-node-{i}" data-detail-item="{i}">{glyph(["person","code","document"][i])}<b>{e(label)}</b></div>' for i,label in enumerate(labels3))
    elif kind in {'cloud','integration'}:
        layers=['Domain / DNS','Hosting / Web','Business / E-Mail'] if kind=='cloud' else ['Ihre Systeme','Schnittstellen','Gemeinsamer Ablauf']
        content='<div class="ds-server-stack">'+''.join(f'<div class="ds-server-layer" data-detail-item="{i}"><span>{glyph("mail" if i==2 and kind=="cloud" else "code")}</span><b>{e(text)}</b><i></i><i></i><i></i></div>' for i,text in enumerate(layers))+'</div>'
        content+='<div class="ds-cloud-orbit">'+glyph('globe')+'</div><div class="ds-floating ds-cloud-tag">'+glyph('check')+'<b>Verbunden.<br>Nach Ihrem Bedarf.</b></div>'
    elif kind in {'brand','print'}:
        if kind=='print':
            content=f'<div class="ds-brochure"><div><small>TAFOLLI &amp; CO.</small><strong>Eine Idee.<br>Ein Format.<br>Ein Eindruck.</strong>{mark}</div><div><span></span><span></span><i></i><i></i><i></i><b>MARKETING · DESIGN</b></div></div>'
        else:
            content=f'<div class="ds-brand-poster"><small>TAFOLLI &amp; CO.</small><strong>Mehr<br>Marke.</strong><div class="ds-brand-sculpture"><i></i><i></i><i></i></div><span>KLAR. WIEDERERKENNBAR. SIE.</span></div><div class="ds-brand-card">{mark}<b>TAFOLLI &amp; CO.</b><span>TECHNOLOGY · MARKETING · CONSULTING</span></div>'
        content+='<div class="ds-brand-swatches">'+''.join(f'<i data-detail-item="{i}"></i>' for i in range(3))+'</div>'
    elif kind=='social':
        content=f'<div class="ds-social-post" data-detail-item="0"><small>IHRE MARKE / CONTENT</small><div class="ds-social-sculpture"><i></i><i></i><i></i></div><strong>Eine Idee.<br>Die bleibt.</strong><span>4:5 / POST</span></div><div class="ds-social-reel" data-detail-item="1"><span>9:16 / REEL</span><div class="ds-reel-wave"><i></i><i></i><i></i><i></i></div><b>In<br>Bewegung.</b></div><div class="ds-floating ds-social-calendar" data-detail-item="2">{glyph("calendar")}<span>THEMA · FORMAT · FREIGABE</span></div>'
    elif kind=='photo':
        content='<div class="ds-camera"><div class="ds-camera-top"></div><span>VISUAL STORIES.</span><div class="ds-lens"><i></i><i></i><i></i><b></b></div><em></em></div><div class="ds-filmstrip">'+''.join(f'<div data-detail-item="{i}"><i></i><span>{e(label)}</span></div>' for i,label in enumerate(labels3))+'</div><div class="ds-photo-frame"></div>'
    elif kind in {'search','local','contact'}:
        if kind=='search':
            content=browser('search / illustrative preview',f'<div class="ds-searchbox">{glyph("search")}<span>Ihre Leistung. Ihr Ort.</span></div><div class="ds-search-list">'+''.join(f'<div data-detail-item="{i}"><small>GESTALTUNGSBEISPIEL</small><b>{e(label)} für Ihr Unternehmen.</b><i></i><i></i></div>' for i,label in enumerate(labels3))+'</div>')
            content+='<div class="ds-floating ds-search-pin">'+glyph('pin')+'<b>Auch lokal<br>stimmig.</b></div>'
        elif kind=='local':
            content='<div class="ds-map"><div class="ds-map-grid"></div><div class="ds-map-park"></div>'+''.join(f'<div class="ds-map-pin ds-map-pin-{i}" data-detail-item="{i}">{glyph("pin")}</div>' for i in range(3))+'</div><div class="ds-local-card"><small>PROFIL / KONZEPT</small><b>Ihr Unternehmen.</b><span>Adresse · Öffnungszeiten · Kontakt</span><div>'+glyph('globe')+glyph('mail')+glyph('pin')+'</div></div>'
        else:
            content=f'<div class="ds-contact-envelope"><div>{mark}<b>Eine Idee<br>wird ein Projekt.</b></div><i></i></div><div class="ds-contact-orbit">'+''.join(f'<span data-detail-item="{i}">{glyph(["mail","person","arrow"][i])}</span>' for i in range(3))+'</div>'
    elif kind=='commerce':
        products=''.join(f'<div class="ds-product" data-detail-item="{i}"><div class="ds-product-shape shape-{i}"></div><b>{e(labels3[i])}</b><i></i></div>' for i in range(3))
        content=browser('your store / concept',f'<div class="ds-site-nav"><b>Ihr Sortiment.</b><i></i><i></i>{glyph("box")}</div><div class="ds-product-grid">{products}</div><div class="ds-shop-checkout"><span>Ein guter Weg zum Kauf.</span>{glyph("arrow")}</div>')
        content+='<div class="ds-floating ds-shop-tag">'+glyph('box')+'<div><small>E-COMMERCE</small><b>Ihr digitaler Laden.</b></div></div>'
    elif kind=='inventory':
        content='<div class="ds-warehouse">'+''.join(f'<div class="ds-inventory-box inventory-{i}" data-detail-item="{i}">{glyph("box")}<span>{e(label)}</span><b></b></div>' for i,label in enumerate(labels3))+'</div><div class="ds-stock-sheet"><small>BESTAND / KONZEPT</small><strong>Alles im Blick.</strong><i></i><i></i><i></i><div>'+glyph('check')+'<span>Erfassen · Abgleichen</span></div></div>'
    elif kind=='leadership':
        content=browser('operative Verantwortung / concept','<div class="ds-site-nav"><b>Gemeinsam im nächsten Schritt.</b>'+glyph('person')+'</div><div class="ds-leadership-board">'+''.join(f'<div data-detail-item="{i}"><b>{e(label)}</b><span><i></i><i></i></span><span><i></i><i></i></span></div>' for i,label in enumerate(labels3))+'</div>')
        content+='<div class="ds-floating ds-people-tag">'+glyph('check')+'<b>Verantwortung.<br>Klar übergeben.</b></div>'
    elif kind=='people':
        content='<div class="ds-role-cards">'+''.join(f'<div data-detail-item="{i}"><div class="ds-role-avatar">{glyph("person")}</div><small>{"ROLLE & AUFGABE" if kind=="people" else "VERANTWORTUNG"}</small><b>{e(label)}</b><i></i><i></i></div>' for i,label in enumerate(labels3))+'</div><div class="ds-floating ds-people-tag">'+glyph('check')+'<b>Gemeinsam<br>im nächsten Schritt.</b></div>'
    elif kind=='hub':
        content='<div class="ds-hub-platform"></div><div class="ds-hub-tiles">'+''.join(f'<div data-detail-item="{i}"><span>{glyph(["spark","code","chart","globe"][i])}</span><b>{e(label)}</b><i></i></div>' for i,label in enumerate(labels))+'</div>'
        content+='<div class="ds-hub-mark">'+mark+'</div>'
    elif kind=='company':
        content='<div class="ds-company-orbits"><i></i><i></i><i></i></div><div class="ds-company-core">'+mark+'</div>'+''.join(f'<div class="ds-company-node company-node-{i}" data-detail-item="{i}"><span>{glyph(["spark","code","chart","globe"][i])}</span><b>{e(label)}</b></div>' for i,label in enumerate(labels))
    elif kind=='career':
        content='<div class="ds-career-photo"><img src="assets/bilder/kastriot-tafolli-portraet.jpg" width="886" height="886" alt="" decoding="async"><span>KASTRIOT TAFOLLI</span></div><div class="ds-career-path">'+''.join(f'<div data-detail-item="{i}"><small>{year}</small><b>{e(label)}</b><span></span></div>' for i,(year,label) in enumerate(zip(['2011','2018','2026'],labels3)))+'</div>'
    elif kind=='network':
        content='<div class="ds-network-core">'+mark+'</div><svg class="ds-network-lines" viewBox="0 0 560 400"><path d="M90 90L280 200L470 90M90 310L280 200L470 310M280 45V350"/></svg>'
        content+=''.join(f'<div class="ds-network-label network-{i}">{name}</div>' for i,name in enumerate(['Krombacher','Google','Microsoft','Panorama Hotel','Tafolli Boost','Nordmann']))
    elif kind=='translation':
        content='<div class="ds-language-cards">'+''.join(f'<div data-detail-item="{i}"><small>{code}</small><b>{word}</b><i></i><i></i><i></i><span>{glyph("check")}</span></div>' for i,(code,word) in enumerate([('DE','Guten Tag.'),('EN','Hello.'),('SQ','Përshëndetje.')]))+'</div>'
    elif kind=='costs':
        content='<div class="ds-cost-plate"><div><small>KALKULATION / KONZEPT</small>'+glyph('chart')+'<b>Jede Zutat zählt.</b></div></div><div class="ds-cost-ingredients">'+''.join(f'<span data-detail-item="{i}"><i>0{i+1}</i><b>{e(label)}</b></span>' for i,label in enumerate(labels3))+'</div>'
    elif kind=='rebate':
        content='<div class="ds-rebate-card"><small>VEREINBARUNG / ABGLEICH</small><strong>Was kommt<br>zurück?</strong><svg viewBox="0 0 120 100"><path d="M25 38C25 8 95 8 95 48S25 91 25 63M12 36L25 48L38 36"/></svg><div>'+''.join(f'<span data-detail-item="{i}"><b>{e(label)}</b><i></i></span>' for i,label in enumerate(labels3))+'</div></div><div class="ds-rebate-slip">'+glyph('document')+'<b>Grundlage.<br>Nachweis.<br>Abrechnung.</b><i></i><i></i><i></i></div>'
    elif kind=='procurement':
        content='<div class="ds-offer-comparison">'+''.join(f'<div data-detail-item="{i}"><small>KONZEPT / 0{i+1}</small><strong>{e(label)}</strong><span>{glyph("document")}</span><i></i><i></i><i></i><b>{glyph("check")}</b></div>' for i,label in enumerate(labels3))+'</div>'
    elif kind=='contracts':
        content='<div class="ds-contract-folder"><div></div><div><small>DAS GESAMTE ANGEBOT</small><strong>Verstehen.<br>Vergleichen.<br>Vereinbaren.</strong><i></i><i></i><i></i></div></div><div class="ds-contract-tabs">'+''.join(f'<span data-detail-item="{i}">{glyph("document")}<b>{e(label)}</b></span>' for i,label in enumerate(labels3))+'</div>'
    else:
        finance=kind=='analytics'
        if finance:
            chart='<svg class="ds-data-chart" viewBox="0 0 300 120"><path class="ds-data-grid" d="M0 30H300M0 70H300M0 110H300"/><path class="ds-data-area" d="M0 100L50 80L100 86L150 50L200 60L250 30L300 20V120H0Z"/><path class="ds-data-line" d="M0 100L50 80L100 86L150 50L200 60L250 30L300 20"/></svg>'
            content=browser('planning / example',f'<small class="ds-ledger-kicker">DARSTELLUNGSBEISPIEL</small><strong class="ds-ledger-title">{e(config["lines"][0])}</strong>{chart}<div class="ds-data-columns">'+''.join(f'<div data-detail-item="{i}"><span>{e(label)}</span><i style="--bar:{[65,40,80][i]}%"></i></div>' for i,label in enumerate(labels3))+'</div>')
            content+='<div class="ds-floating ds-finance-tag">'+glyph('chart')+'<b>Nachvollziehbar.<br>Entscheidbar.</b></div>'
        else:
            content='<div class="ds-strategy-sheets"><div></div><div></div><div><small>VOM ÜBERBLICK ZUM NÄCHSTEN SCHRITT</small><strong>'+e(config['lines'][0])+'</strong>'+''.join(f'<span data-detail-item="{i}"><em>0{i+1}</em><b>{e(label)}</b>'+glyph('check')+'</span>' for i,label in enumerate(labels3))+'</div></div><div class="ds-strategy-stamp">'+glyph('arrow')+'</div>'
    return f'<div class="detail-scene-art detail-art-{kind}" aria-hidden="true"><div class="detail-scene-grid"></div><div class="detail-scene-halo"></div><div class="detail-rig"><div class="detail-assembly">{content}</div></div></div>'
