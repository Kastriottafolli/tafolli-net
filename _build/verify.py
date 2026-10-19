"""Check generated HTML, local assets, anchors, translations and demo data."""
from collections import Counter
from html.parser import HTMLParser
from icons import GLYPHS
import json
from services import SERVICES
from seo import NOINDEX_PATHS, SITEMAP_LASTMOD, alternates_for
from partners import visible_projects, visible_tech, SOURCES
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
        self.visible_text=''; self.hidden_text=[]; self.icon_count=0
        self.hreflang=[]; self.images=[]
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in ['head','script','style']: self.hidden_text.append(tag)
        if tag=='svg' and 'site-icon' in attrs.get('class','').split():
            self.icon_count+=1
            assert attrs.get('aria-hidden')=='true' and attrs.get('focusable')=='false', f'{self.path}: decorative icon must not be announced'
        if tag == 'html': self.lang=attrs.get('lang','')
        if tag == 'h1': self.h1+=1
        if tag == 'title': self.in_title=True
        if tag == 'nav' and attrs.get('id')=='site-navigation': self.in_nav=True
        if tag == 'nav' and attrs.get('aria-label')=='Brotkrumennavigation': self.breadcrumbs+=1
        if tag == 'a' and self.in_nav: self.nav_links.append(attrs.get('href',''))
        if tag == 'link' and attrs.get('rel')=='canonical': self.canonical=attrs.get('href','')
        if tag == 'link' and attrs.get('rel')=='alternate' and attrs.get('hreflang'):
            self.hreflang.append((attrs.get('hreflang'), attrs.get('href','')))
        if tag == 'img': self.images.append(attrs)
        if 'brand-intro' in attrs.get('class','').split(): self.intros+=1
        if tag == 'script' and attrs.get('type')=='application/ld+json': self.in_schema=True;self.schema_text=''
        if 'id' in attrs: self.ids.append(attrs['id'])
        for key in ['src','href']:
            if key in attrs: self.links.append(attrs[key])
        if tag == 'meta': self.meta[attrs.get('name',attrs.get('property',''))]=attrs.get('content','')
        if tag == 'script' and attrs.get('id') == 'experience-config': self.in_config=True
    def handle_data(self,data):
        if not self.hidden_text: self.visible_text+=data
        if self.in_config: self.config+=data
        if self.in_title: self.title+=data
        if self.in_schema: self.schema_text+=data
    def handle_endtag(self,tag):
        if self.hidden_text and tag==self.hidden_text[-1]: self.hidden_text.pop()
        if tag=='title': self.in_title=False
        if tag=='nav': self.in_nav=False
        if tag == 'script':
            self.in_config=False
            if self.in_schema: self.schemas.append(json.loads(self.schema_text));self.in_schema=False

def node_types(node):
    raw = node.get('@type')
    if isinstance(raw, list):
        return set(raw)
    return {raw} if raw else set()

def banned_schema(node):
    if isinstance(node, dict):
        if node_types(node) & {'AggregateRating', 'Review', 'Rating'}:
            return True
        if 'aggregateRating' in node or 'review' in node:
            return True
        return any(banned_schema(value) for value in node.values())
    if isinstance(node, list):
        return any(banned_schema(value) for value in node)
    return False

def verify():
    pages={p.resolve():Page(p) for p in [*ROOT.glob('*.html'),*(ROOT/'en').glob('*.html'),*(ROOT/'sq').glob('*.html'),ROOT/'angebot/index.html']}
    errors=[]
    svg_ids={path.resolve():{node.get('id') for node in ET.parse(path).iter() if node.get('id')} for path in ROOT.rglob('*.svg')}
    for path,page in pages.items():
        relative=path.relative_to(ROOT)
        glyphs=set(page.visible_text)&set(GLYPHS)
        if glyphs: errors.append(f'{relative}: font glyph icons still visible: '+', '.join(sorted(glyphs)))
        if not page.icon_count: errors.append(f'{relative}: SVG interface icons missing')
        if page.h1 != 1: errors.append(f'{relative}: expected one h1, got {page.h1}')
        if not page.lang: errors.append(f'{relative}: missing language')
        if not page.meta.get('description'): errors.append(f'{relative}: missing description')
        if not page.title.strip(): errors.append(f'{relative}: missing title')
        if page.title.strip() and not 50 <= len(page.title.strip()) <= 60:
            errors.append(f'{relative}: title length {len(page.title.strip())}')
        if page.meta.get('description') and not 150 <= len(page.meta['description']) <= 160:
            errors.append(f'{relative}: description length {len(page.meta["description"])}')
        expected_canonical='https://tafolli.net/'+('' if str(relative)=='index.html' else str(relative).replace('/index.html','/'))
        if page.canonical!=expected_canonical: errors.append(f'{relative}: incorrect canonical')
        if page.meta.get('og:url')!=page.canonical: errors.append(f'{relative}: og:url must match the canonical')
        if not str(page.meta.get('og:image','')).startswith('https://tafolli.net/'):
            errors.append(f'{relative}: og:image must be an absolute tafolli.net URL')
        if page.meta.get('twitter:image')!=page.meta.get('og:image'):
            errors.append(f'{relative}: twitter:image must match og:image')
        key=relative.as_posix()
        if key.endswith('/index.html'): key=key[:-len('index.html')]
        if page.hreflang!=alternates_for(key):
            errors.append(f'{relative}: hreflang does not match the real language equivalents')
        for needle in ('Hauptstraße 1', 'info@tafolli.net', '0176 64616146'):
            if needle not in page.visible_text: errors.append(f'{relative}: contact line missing {needle}')
        for img in page.images:
            src=img.get('src','')
            if 'alt' not in img: errors.append(f'{relative}: image without alt {src}')
            if not img.get('width') or not img.get('height'): errors.append(f'{relative}: image without dimensions {src}')
        for link in page.links:
            if urlsplit(link).path.endswith('/logo-mark.webp'):
                errors.append(f'{relative}: full-size logo in HTML {link}')
        if page.intros!=1: errors.append(f'{relative}: expected one brand intro')
        nav_targets=set()
        for href in page.nav_links:
            parsed=urlsplit(href)
            if parsed.scheme or parsed.netloc: continue
            target=(ROOT/parsed.path.lstrip('/')).resolve() if parsed.path.startswith('/') else (path.parent/parsed.path).resolve()
            if target.is_dir():target=target/'index.html'
            nav_targets.add(target)
        indexable={p for p,pg in pages.items() if 'noindex' not in pg.meta.get('robots','')}
        missing=indexable-nav_targets
        if missing:errors.append(f'{relative}: pages missing from main menu: '+', '.join(sorted(p.name for p in missing)))
        graph=[node for schema in page.schemas for node in schema.get('@graph',[schema])]
        types=set()
        for node in graph: types |= node_types(node)
        if not {'Organization','Person','WebSite'}<=types: errors.append(f'{relative}: missing identity schema')
        if banned_schema(graph): errors.append(f'{relative}: ratings or reviews are not allowed')
        is_home=str(relative) in ['index.html','en/index.html','sq/index.html']
        if not is_home and str(relative)!='404.html':
            if page.breadcrumbs!=1 or 'BreadcrumbList' not in types:errors.append(f'{relative}: missing or duplicate breadcrumbs')
        if str(relative)=='404.html' and page.meta.get('robots')!='noindex':errors.append('404 must remain noindex')
        for node in graph:
            if {'Organization','Service'} & node_types(node):
                if {country['name'] for country in node.get('areaServed',[])}!={'Germany','Austria','Switzerland','Kosovo'}:errors.append(f'{relative}: incorrect service coverage')
            if 'FAQPage' in node_types(node):
                for question in node.get('mainEntity') or []:
                    name=question.get('name','')
                    if name and name not in page.visible_text:
                        errors.append(f'{relative}: FAQ not visible: {name}')
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
            elif parsed.fragment and target in svg_ids and unquote(parsed.fragment) not in svg_ids[target]:
                errors.append(f'{relative}: missing SVG symbol {link}')
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
    robots=(ROOT/'robots.txt').read_text()
    if 'Sitemap: https://tafolli.net/sitemap.xml' not in robots or 'Disallow: /' in robots:
        errors.append('robots.txt must allow the site and name the sitemap')
    sitemap=ET.parse(ROOT/'sitemap.xml')
    sm='{http://www.sitemaps.org/schemas/sitemap/0.9}'
    xhtml='{http://www.w3.org/1999/xhtml}'
    urls=[]
    for url in sitemap.findall(f'.//{sm}url'):
        loc=url.find(f'{sm}loc').text
        urls.append(loc)
        lastmod=url.find(f'{sm}lastmod')
        if lastmod is None or lastmod.text!=SITEMAP_LASTMOD:
            errors.append(f'{loc}: sitemap lastmod must be {SITEMAP_LASTMOD}')
        key='index.html' if loc=='https://tafolli.net/' else loc.removeprefix('https://tafolli.net/')
        pairs=[(el.get('hreflang'), el.get('href')) for el in url.findall(f'{xhtml}link')]
        if pairs!=alternates_for(key):
            errors.append(f'{loc}: sitemap hreflang does not match the page')
    assert 'https://tafolli.net/ki-automatisierung.html' in urls
    indexable={path for path,page in pages.items() if 'noindex' not in page.meta.get('robots','')}
    assert set(urls)=={pages[path].canonical for path in indexable}, 'Sitemap must match the indexable canonical pages'
    assert len(urls)==len(set(urls)), 'Duplicate sitemap entries'
    for service in SERVICES:
        path=(ROOT/(service['slug']+'.html')).resolve()
        assert path in pages
        if 'noindex' not in pages[path].meta.get('robots',''):
            assert 'https://tafolli.net/'+path.name in urls
        assert {'ausgangslage','umfang','praxis','ergebnisse','fragen'} <= set(pages[path].ids)
    references=pages[(ROOT/'referenzen.html').resolve()]
    for partner in visible_projects()+visible_tech():
        assert partner['url'] in references.links, f"Missing partner link: {partner['name']}"
        if partner['key']!='tafolli':
            assert (ROOT/'assets/partners'/SOURCES[partner['key']]['file']).is_file()
    for location in ['index.html','en/index.html','sq/index.html']:
        assert 'partner' in pages[(ROOT/location).resolve()].ids
    for rel in sorted(NOINDEX_PATHS):
        page=pages[(ROOT/rel).resolve()]
        if page.meta.get('robots')!='noindex': errors.append(f'{rel}: must stay noindex while kept for a later decision')
        if pages[(ROOT/rel).resolve()].canonical in urls: errors.append(f'{rel}: noindex page must leave the sitemap')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; local links, anchors, assets, metadata, all-page menu coverage, structured data, breadcrumbs, localized demos and sitemap.')

if __name__=='__main__':verify()
