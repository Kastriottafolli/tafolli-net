"""Check generated HTML, local assets, anchors, translations and demo data."""
from collections import Counter
from html.parser import HTMLParser
import json
from services import SERVICES
from companies import COMPANIES
from hotels import HOTELS
from partners import PROJECTS, GASTRO, TECH, SOURCES
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.h1 = path, [], [], 0
        self.lang, self.meta, self.config = '', {}, ''
        self.in_config = False
        self.in_nav=False; self.nav_links=[]; self.canonical=''; self.title=''; self.in_title=False
        self.schemas=[]; self.schema_text=''; self.in_schema=False
        self.breadcrumbs=0; self.intros=0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'html': self.lang=attrs.get('lang','')
        if tag == 'h1': self.h1+=1
        if tag == 'title': self.in_title=True
        if tag == 'nav' and attrs.get('id')=='site-navigation': self.in_nav=True
        if tag == 'nav' and attrs.get('aria-label')=='Brotkrumennavigation': self.breadcrumbs+=1
        if tag == 'a' and self.in_nav: self.nav_links.append(attrs.get('href',''))
        if tag == 'link' and attrs.get('rel')=='canonical': self.canonical=attrs.get('href','')
        if 'brand-intro' in attrs.get('class','').split(): self.intros+=1
        if tag == 'script' and attrs.get('type')=='application/ld+json': self.in_schema=True;self.schema_text=''
        if 'id' in attrs: self.ids.append(attrs['id'])
        for key in ['src','href']:
            if key in attrs: self.links.append(attrs[key])
        if tag == 'meta': self.meta[attrs.get('name',attrs.get('property',''))]=attrs.get('content','')
        if tag == 'script' and attrs.get('id') == 'experience-config': self.in_config=True
    def handle_data(self,data):
        if self.in_config: self.config+=data
        if self.in_title: self.title+=data
        if self.in_schema: self.schema_text+=data
    def handle_endtag(self,tag):
        if tag=='title': self.in_title=False
        if tag=='nav': self.in_nav=False
        if tag == 'script':
            self.in_config=False
            if self.in_schema: self.schemas.append(json.loads(self.schema_text));self.in_schema=False

def verify():
    pages={p.resolve():Page(p) for p in [*ROOT.glob('*.html'),ROOT/'en/index.html',ROOT/'sq/index.html']}
    errors=[]
    for path,page in pages.items():
        relative=path.relative_to(ROOT)
        if page.h1 != 1: errors.append(f'{relative}: expected one h1, got {page.h1}')
        if not page.lang: errors.append(f'{relative}: missing language')
        if not page.meta.get('description'): errors.append(f'{relative}: missing description')
        if not page.title.strip(): errors.append(f'{relative}: missing title')
        expected_canonical='https://tafolli.net/'+('' if str(relative)=='index.html' else str(relative).replace('/index.html','/'))
        if page.canonical!=expected_canonical: errors.append(f'{relative}: incorrect canonical')
        if page.intros!=1: errors.append(f'{relative}: expected one brand intro')
        nav_targets=set()
        for href in page.nav_links:
            parsed=urlsplit(href)
            if parsed.scheme or parsed.netloc: continue
            target=(ROOT/parsed.path.lstrip('/')).resolve() if parsed.path.startswith('/') else (path.parent/parsed.path).resolve()
            if target.is_dir():target=target/'index.html'
            nav_targets.add(target)
        missing=set(pages)-nav_targets
        if missing:errors.append(f'{relative}: pages missing from main menu: '+', '.join(p.name for p in missing))
        graph=[node for schema in page.schemas for node in schema.get('@graph',[schema])]
        types={node.get('@type') for node in graph}
        if not {'Organization','Person','WebSite'}<=types: errors.append(f'{relative}: missing identity schema')
        is_home=str(relative) in ['index.html','en/index.html','sq/index.html']
        if not is_home and str(relative)!='404.html':
            if page.breadcrumbs!=1 or 'BreadcrumbList' not in types:errors.append(f'{relative}: missing or duplicate breadcrumbs')
        if str(relative)=='404.html' and page.meta.get('robots')!='noindex':errors.append('404 must remain noindex')
        for node in graph:
            if node.get('@type') in ['Organization','Service']:
                if {country['name'] for country in node.get('areaServed',[])}!={'Germany','Austria','Switzerland','Kosovo'}:errors.append(f'{relative}: incorrect service coverage')
            for asset in ['logo','image']:
                if node.get(asset,'').startswith('https://tafolli.net/assets/') and not (ROOT/urlsplit(node[asset]).path.lstrip('/')).is_file():errors.append(f'{relative}: missing schema asset {node[asset]}')

        for key,count in Counter(page.ids).items():
            if count>1: errors.append(f'{relative}: duplicate id {key}')
        for link in page.links:
            parsed=urlsplit(link)
            if parsed.scheme or parsed.netloc: continue
            if not parsed.path: target=path
            elif parsed.path.startswith('/'): target=(ROOT/unquote(parsed.path).lstrip('/')).resolve()
            else: target=(path.parent/unquote(parsed.path)).resolve()
            if target.is_dir(): target=target/'index.html'
            if not target.exists(): errors.append(f'{relative}: broken link {link}')
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{relative}: missing anchor {link}')
        if page.config:
            cfg=json.loads(page.config)
            assert len(cfg['demos'])==3 and len(cfg['stages'])==5 and len(cfg['stage_notes'])==5
            for demo in cfg['demos']:
                assert all(demo[k] for k in ['source','subject','message','fields','result_title','result','receipt'])
    for attribute in ['title','description']:
        values=[page.title if attribute=='title' else page.meta.get('description') for page in pages.values()]
        if len(set(values))!=len(values):errors.append(f'Duplicate {attribute}')
    for code,location in [('de','index.html'),('en','en/index.html'),('sq','sq/index.html')]:
        assert pages[(ROOT/location).resolve()].lang==code
    assert (ROOT/'assets/social-preview.png').exists(), 'Missing sharing image'
    sitemap=ET.parse(ROOT/'sitemap.xml')
    urls=[el.text for el in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert 'https://tafolli.net/ki-automatisierung.html' in urls
    assert set(urls)=={page.canonical for path,page in pages.items() if path.name!='404.html'}, 'Sitemap must contain all 37 indexable canonical pages'
    assert len(urls)==len(set(urls)), 'Duplicate sitemap entries'
    for service in SERVICES:
        path=(ROOT/(service['slug']+'.html')).resolve()
        assert path in pages and 'https://tafolli.net/'+path.name in urls
        assert {'ausgangslage','umfang','praxis','ergebnisse','fragen'} <= set(pages[path].ids)
    homepage=pages[(ROOT/'index.html').resolve()]
    for name,url in COMPANIES:
        assert url in homepage.links, f'Missing official station link: {name}'
    references=pages[(ROOT/'referenzen.html').resolve()]
    for partner in PROJECTS+GASTRO+TECH+HOTELS:
        assert partner['url'] in references.links, f"Missing partner link: {partner['name']}"
        if partner['key']!='tafolli':
            assert (ROOT/'assets/partners'/SOURCES[partner['key']]['file']).is_file()
    for location in ['index.html','en/index.html','sq/index.html']:
        assert 'partner' in pages[(ROOT/location).resolve()].ids
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; local links, anchors, assets, metadata, all-page menu coverage, structured data, breadcrumbs, localized demos and sitemap.')

if __name__=='__main__':verify()
