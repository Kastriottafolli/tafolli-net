"""Verify redesign coverage and the accessible relationships of its controls."""
from pathlib import Path
from detail_design import Document
from detail_catalog import PAGES
from navigation import SECTIONS

ROOT=Path(__file__).resolve().parent.parent

def check():
    required={url.split('#')[0] for key,_,url,_,groups in SECTIONS if key in {'leistungen','profil'} for _,links in groups for url,_ in links if url not in {'index.html','en/','sq/'}}|{'leistungen.html'}
    assert required<=PAGES.keys(),f'Menu pages without visual direction: {required-PAGES.keys()}'
    headlines=[];explorers=0
    for path,config in PAGES.items():
        file=ROOT/(path+'index.html' if path.endswith('/') else path);doc=Document(file.read_text())
        bodies=[n for n in doc.elements if n.tag=='body'];assert len(bodies)==1
        assert bodies[0].has('detail-page') and bodies[0].attrs.get('data-detail-page')==path,path
        assert any('assets/detail.css?v=' in n.attrs.get('href','') for n in doc.elements),path
        assert any('assets/detail.js?v=' in n.attrs.get('src','') for n in doc.elements),path
        if config['kind']=='planner':
            assert any('data-planner' in n.attrs for n in doc.elements),path;continue
        heroes=[n for n in doc.elements if 'data-detail-hero' in n.attrs];assert len(heroes)==1,path
        assert len([n for n in doc.elements if n.tag=='h1'])==1,path
        controls=[n for n in doc.elements if 'data-detail-focus' in n.attrs]
        notes=[n for n in doc.elements if 'data-detail-note' in n.attrs]
        assert len(controls)==len(notes)==len(config['topics']),path
        assert sum(n.attrs.get('aria-pressed')=='true' for n in controls)==1,path
        assert {n.attrs['data-detail-focus'] for n in controls}=={n.attrs['data-detail-note'] for n in notes},path
        for tab in [n for n in doc.elements if n.attrs.get('role')=='tab' and n.attrs.get('id','').startswith('detail-tab-')]:
            panel=next((n for n in doc.elements if n.attrs.get('id')==tab.attrs.get('aria-controls')),None)
            assert panel and panel.attrs.get('role')=='tabpanel' and panel.attrs.get('aria-labelledby')==tab.attrs.get('id'),path
            explorers+=1
        h1=next(n for n in doc.elements if n.tag=='h1');headlines.append(doc.inner(h1))
    assert len(headlines)==len(set(headlines)),'Repeated detail-page headlines'
    print(f'PASS: {len(required)} service/company URLs and {len(PAGES)} designed detail pages; scene controls, unique headlines and {explorers} tab/panel relationships.')

if __name__=='__main__':check()
