"""Page-specific search intent, shared identity and honest service coverage."""
import json
from html import escape
from navigation import TITLES, parent
from seo_copy import META

HOST = 'https://tafolli.net'
ORIGIN = HOST + '/'
SITEMAP_LASTMOD = '2026-10-19'
OG_IMAGE = HOST + '/assets/social-preview.png'
OG_ALT = 'Kastriot Tafolli · Webdesign, Software und KI'
COUNTRIES = [{'@type': 'Country', 'name': name} for name in ['Germany', 'Austria', 'Switzerland', 'Kosovo']]
ADDRESS = {
    '@type': 'PostalAddress',
    'streetAddress': 'Hauptstraße 1',
    'postalCode': '18609',
    'addressLocality': 'Ostseebad Binz',
    'addressCountry': 'DE',
}
# Kept on disk for a later decision, but not offered in navigation, sitemap or search.
NOINDEX_PATHS = {
    'fb-beratung.html', 'lieferantenvereinbarungen.html', 'getraenkevertraege.html', 'rueckverguetungen.html',
    'wareneinsatz-kalkulation.html', 'inventur-warenwirtschaft.html', 'interim-fb-management.html',
    'revenue-controlling.html', 'personal-recruiting.html', 'wissen-ki-im-hotel.html',
    'wissen-getraenkevertrag.html', 'wissen-direktbuchungen.html',
}


def _path(key):
    if key.endswith('.html') or key.endswith('/'):
        return key
    return key + '.html'


PAGE_META = {_path(key): value for key, value in META.items()}
SERVICE_META = {key: value for key, value in META.items() if _path(key) == key + '.html'}

HOME_ALT = [
    ('de', ORIGIN),
    ('en', ORIGIN + 'en/'),
    ('sq', ORIGIN + 'sq/'),
    ('x-default', ORIGIN),
]
KI_ALT = [
    ('de', ORIGIN + 'ki-automatisierung-kleine-unternehmen.html'),
    ('sq', ORIGIN + 'sq/automatizim-ia.html'),
    ('x-default', ORIGIN + 'ki-automatisierung-kleine-unternehmen.html'),
]
TEXT_ALT = [
    ('de', ORIGIN + 'angebot/'),
    ('sq', ORIGIN + 'sq/faqe-dhe-perkthime.html'),
    ('x-default', ORIGIN + 'angebot/'),
]
ALTERNATES = {
    'index.html': HOME_ALT,
    'en/': HOME_ALT,
    'en/index.html': HOME_ALT,
    'sq/': HOME_ALT,
    'sq/index.html': HOME_ALT,
    'ki-automatisierung-kleine-unternehmen.html': KI_ALT,
    'sq/automatizim-ia.html': KI_ALT,
    'angebot/': TEXT_ALT,
    'angebot/index.html': TEXT_ALT,
    'sq/faqe-dhe-perkthime.html': TEXT_ALT,
}
ANGEBOT_FAQ = [
    ('Was kosten die drei Pakete?', 'Dokument oder Prospekt: 99 €, etwa 1.200 Wörter, 3 Werktage. Website-Text: 199 €, etwa 1.500 Wörter inklusive Title und Meta, 5 Werktage. Content-Paket: 299 €, etwa 3.000 Wörter inklusive Glossar, 7 Werktage.'),
    ('Für welche Sprachen gelten die Preise?', 'Für eine Zielsprache. Deutsch, Englisch oder Albanisch, in jeder Richtung. Eine weitere Sprache ist ein Aufpreis nach Absprache.'),
    ('Lesen Sie den Text selbst?', 'Ja. Ich nutze KI für den ersten Entwurf. Bevor der Text an Sie geht, lese und korrigiere ich ihn selbst.'),
    ('Gibt es beglaubigte Übersetzungen?', 'Nein. Beglaubigte Übersetzungen von Urkunden oder Zeugnissen biete ich nicht an. Rechts- und Medizintexte auch nicht.'),
    ('Was kostet ein Eilauftrag?', 'Weitere Sprache, Eilauftrag und mehr Umfang sind ein Aufpreis nach Absprache.'),
]


def metadata(path, title, description):
    return PAGE_META.get(path, (title, description))


def page_url(path):
    if path in ('index.html', ''):
        return ORIGIN
    if path.endswith('/index.html'):
        return ORIGIN + path[:-len('index.html')]
    return ORIGIN + path


def alternates_for(path):
    return ALTERNATES.get(path, [])


def faq_node(url, pairs):
    return {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'mainEntity': [
        {'@type': 'Question', 'name': question, 'acceptedAnswer': {'@type': 'Answer', 'text': answer}}
        for question, answer in pairs]}


def offer(name, price, monthly=False, description=None):
    node = {'@type': 'Offer', 'name': name, 'price': str(price), 'priceCurrency': 'EUR'}
    if description:
        node['description'] = description
    if monthly:
        node['priceSpecification'] = {
            '@type': 'UnitPriceSpecification',
            'price': str(price),
            'priceCurrency': 'EUR',
            'unitCode': 'MON',
            'referenceQuantity': {'@type': 'QuantitativeValue', 'value': 1, 'unitCode': 'MON'},
        }
    return node


def _monthly():
    return [offer('Basis', '99', True), offer('Laufend', '199', True), offer('Intensiv', '299', True)]


def _texte():
    return [
        offer('Übersetzung Dokument/Prospekt', '99'),
        offer('Website-Text', '199'),
        offer('Content-Paket', '299'),
    ]


def _shop():
    return [offer('Start', '990'), offer('Erweitert', '1990')]


OFFERS = {
    'website-pflege.html': _monthly(),
    'website-pflege-kleine-betriebe.html': _monthly(),
    'onlineshop.html': _shop(),
    'onlineshop-kleine-haendler.html': _shop() + [offer('Website-Text', '199'), offer('Content-Paket', '299')],
    'web-apps.html': [offer('Kleines Werkzeug', '390', description='Einstieg, wenn der Ablauf klein bleibt. Größere Projekte auf Anfrage.')],
    'firmenprofile.html': [offer('Basis', '399'), offer('Komplett', '899')],
    'website-fuer-handwerker.html': _texte() + _monthly(),
    'website-fuer-vereine.html': _texte() + _monthly(),
    'angebot/': _texte(),
    'angebot/index.html': _texte(),
    'sq/faqe-dhe-perkthime.html': _texte(),
}


def texte_angebot():
    """Fixed text prices. Extra language and rush work have no published amount."""
    return {
        '@type': 'Service', '@id': ORIGIN + 'angebot/#texte', 'name': 'Texte und Übersetzungen',
        'url': ORIGIN + 'angebot/', 'description': 'Weitere Sprache und Eilauftrag: Aufpreis nach Absprache.',
        'provider': {'@id': ORIGIN + '#business'}, 'areaServed': COUNTRIES, 'offers': _texte(),
    }


def structured(path, title, description, lang='de', faq=None, home_label='Startseite', home_url=None):
    title, description = metadata(path, title, description)
    url = page_url(path)
    business = {
        '@type': ['Organization', 'ProfessionalService'],
        '@id': ORIGIN + '#business',
        'name': 'Kastriot Tafolli',
        'alternateName': 'TB Solutions',
        'url': ORIGIN,
        'logo': ORIGIN + 'assets/brand/logo-mark.webp',
        'image': ORIGIN + 'assets/brand/logo-mark.webp',
        'email': 'info@tafolli.net',
        'telephone': '+4917664616146',
        'address': ADDRESS,
        'areaServed': COUNTRIES,
        'contactPoint': {
            '@type': 'ContactPoint',
            'contactType': 'project enquiries',
            'email': 'info@tafolli.net',
            'telephone': '+4917664616146',
            'areaServed': COUNTRIES,
            'availableLanguage': ['de', 'en', 'sq'],
        },
    }
    identity = [
        business,
        {
            '@type': 'Person', '@id': ORIGIN + '#kastriot', 'name': 'Kastriot Tafolli',
            'url': ORIGIN + 'ueber-mich.html', 'image': ORIGIN + 'assets/bilder/kastriot-tafolli-portraet.jpg',
            'email': 'info@tafolli.net', 'telephone': '+4917664616146', 'address': ADDRESS,
            'worksFor': {'@id': ORIGIN + '#business'},
        },
        {
            '@type': 'WebSite', '@id': ORIGIN + '#website', 'name': 'Kastriot Tafolli', 'url': ORIGIN,
            'publisher': {'@id': ORIGIN + '#business'}, 'inLanguage': ['de', 'en', 'sq'],
        },
    ]
    page = {
        '@type': 'WebPage', '@id': url + '#page', 'url': url, 'name': title, 'description': description,
        'inLanguage': lang, 'isPartOf': {'@id': ORIGIN + '#website'},
    }
    if path == 'ueber-mich.html':
        page.update({'@type': 'ProfilePage', 'mainEntity': {'@id': ORIGIN + '#kastriot'}})
    if path == 'kontakt.html':
        page['@type'] = 'ContactPage'
    if path in ['leistungen.html', 'wissen.html', 'referenzen.html']:
        page['@type'] = 'CollectionPage'
    graph = identity + [page]
    slug = path.removesuffix('.html')
    if path == 'preisrechner.html':
        graph.append({
            '@type': 'WebApplication', '@id': url + '#app', 'name': 'Preisrechner', 'url': url,
            'description': description, 'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Web',
            'browserRequirements': 'Requires JavaScript. The estimate stays in the browser.',
            'isAccessibleForFree': True, 'inLanguage': 'de', 'provider': {'@id': ORIGIN + '#business'},
        })
    elif path in ('angebot/', 'angebot/index.html'):
        graph.append(texte_angebot())
    elif path == 'sq/faqe-dhe-perkthime.html':
        node = texte_angebot()
        node.update({'@id': url + '#service', 'url': url, 'name': 'Faqe web dhe përkthime'})
        graph.append(node)
    elif path == 'sq/automatizim-ia.html' or slug in SERVICE_META:
        service_name = TITLES.get(path) or title.split(' | ')[0]
        service = {
            '@type': 'Service', '@id': url + '#service', 'name': service_name, 'serviceType': service_name,
            'url': url, 'description': description, 'provider': {'@id': ORIGIN + '#business'}, 'areaServed': COUNTRIES,
        }
        priced = OFFERS.get(path)
        if priced:
            service['offers'] = priced
        graph.append(service)
    if path.startswith('wissen-'):
        graph.append({
            '@type': 'Article', '@id': url + '#article', 'headline': title.split(' | ')[0],
            'author': {'@id': ORIGIN + '#kastriot'}, 'publisher': {'@id': ORIGIN + '#business'},
            'inLanguage': 'de', 'mainEntityOfPage': {'@id': url + '#page'},
        })
    if path not in ['index.html', 'en/', 'sq/', '404.html']:
        home = home_url or ORIGIN
        items = [(home_label, home)]
        trail = parent(path)
        if trail:
            items.append((trail[0], ORIGIN + trail[1]))
        items.append((TITLES.get(path, title), url))
        graph.append({
            '@type': 'BreadcrumbList', '@id': url + '#breadcrumbs',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': name, 'item': item} for i, (name, item) in enumerate(items)],
        })
        page['breadcrumb'] = {'@id': url + '#breadcrumbs'}
    if faq:
        graph.append(faq_node(url, faq))
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c') + '</script>'


def meta_block(path, title, description, lang='de', faq=None, home_label='Startseite', home_url=None):
    title, description = metadata(path, title, description)
    url = page_url(path)
    safe_title, safe_description = escape(title), escape(description)
    alt = ''.join(f'<link rel="alternate" hreflang="{code}" href="{href}">\n' for code, href in alternates_for(path))
    locale = {'de': 'de_DE', 'en': 'en_US', 'sq': 'sq_AL'}[lang]
    others = ''.join(
        f'<meta property="og:locale:alternate" content="{ {"de": "de_DE", "en": "en_US", "sq": "sq_AL"}[code] }">\n'
        for code in ('de', 'en', 'sq') if code != lang)
    schema = structured(path, title, description, lang, faq, home_label, home_url)
    return f'''<title>{safe_title}</title>
<meta name="description" content="{safe_description}">
<meta name="author" content="Kastriot Tafolli">
<link rel="canonical" href="{url}">
{alt}<meta property="og:type" content="website">
<meta property="og:site_name" content="Kastriot Tafolli">
<meta property="og:locale" content="{locale}">
{others}<meta property="og:title" content="{safe_title}">
<meta property="og:description" content="{safe_description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{escape(OG_ALT)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{safe_title}">
<meta name="twitter:description" content="{safe_description}">
<meta name="twitter:image" content="{OG_IMAGE}">
{schema}
'''


def _guard():
    seen_titles, seen_descriptions = set(), set()
    for path, (title, description) in PAGE_META.items():
        if not 50 <= len(title) <= 60 or not 150 <= len(description) <= 160:
            raise SystemExit(f'{path}: title {len(title)}, description {len(description)}')
        if title in seen_titles or description in seen_descriptions:
            raise SystemExit(f'{path}: duplicate metadata')
        seen_titles.add(title)
        seen_descriptions.add(description)


_guard()

REGION_COPY = {
    'de': ('NAH AM BETRIEB. ÜBER GRENZEN HINWEG.', 'Ihre Idee kennt keine Landesgrenze.', 'Alle Leistungen biete ich in Deutschland, Österreich, der Schweiz und Kosovo an. Analyse, Abstimmung und digitale Umsetzung sind ortsunabhängig möglich. Workshops, Foto- und Videotermine oder operative Einsätze vor Ort planen wir passend zu Ihrem Auftrag und meiner Verfügbarkeit.', 'Deutschland', 'Österreich', 'Schweiz', 'Kosovo', 'Zusammenarbeit besprechen'),
    'en': ('CLOSE TO YOUR BUSINESS. ACROSS BORDERS.', 'Your idea travels further.', 'All services are available in Germany, Austria, Switzerland and Kosovo. Analysis, coordination and digital delivery can take place remotely. We arrange on-site workshops, photo and video sessions or operational assignments around your project and my availability.', 'Germany', 'Austria', 'Switzerland', 'Kosovo', 'Discuss a project'),
    'sq': ('PRANË BIZNESIT. PËRTEJ KUFIJVE.', 'Ideja juaj nuk njeh kufij.', 'Të gjitha shërbimet ofrohen në Gjermani, Austri, Zvicër dhe Kosovë. Analiza, koordinimi dhe zbatimi digjital mund të kryhen në distancë. Punëtoritë, fotografimi, videot dhe angazhimet në vend planifikohen sipas projektit dhe disponueshmërisë sime.', 'Gjermani', 'Austri', 'Zvicër', 'Kosovë', 'Diskutoni bashkëpunimin'),
}


def region(lang='de', base='', anchor=False, service=None):
    kicker, title, copy, *rest = REGION_COPY[lang]
    if service:
        title = service + ' · in DACH und Kosovo'
        copy = 'Mein Angebot für ' + service + ' steht Ihnen in Deutschland, Österreich, der Schweiz und Kosovo zur Verfügung. Wir klären zuerst Ziele, vorhandene Systeme und die Verantwortung im Betrieb. Digitale Abstimmung und Umsetzung erfolgen aus der Ferne; nötige Termine im Haus werden im Angebot mit Umfang und Verfügbarkeit abgestimmt.'
    return f'<section class="region-section"{" id=\"einsatzgebiet\"" if anchor else ""}><div class="shell x-shell region-grid"><div><p class="region-kicker">{kicker}</p><h2>{escape(title)}</h2><div class="region-countries">' + ''.join(f'<span><i aria-hidden="true">↗</i>{name}</span>' for name in rest[:4]) + f'</div></div><div><p>{escape(copy)}</p><a href="{base}kontakt.html" class="region-link">{rest[4]} <span aria-hidden="true">↗</span></a></div></div></section>'
