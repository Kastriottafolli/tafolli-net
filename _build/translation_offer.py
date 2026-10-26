"""Retain /angebot/ in the current company design."""
from pathlib import Path
from bausteine import seite_rahmen
from html.parser import HTMLParser

def visible_faq(content):
    class Questions(HTMLParser):
        def __init__(self):super().__init__();self.inside=False;self.question=False;self.q='';self.a='';self.pairs=[]
        def handle_starttag(self,tag,attrs):
            if tag=='details':self.inside=True;self.q='';self.a=''
            if tag=='summary':self.question=True
        def handle_data(self,text):
            if self.inside:
                if self.question:self.q+=text
                else:self.a+=text
        def handle_endtag(self,tag):
            if tag=='summary':self.question=False
            if tag=='details':
                if self.q.strip() and self.a.strip():self.pairs.append((' '.join(self.q.split()),' '.join(self.a.split())))
                self.inside=False
    parsed=Questions();parsed.feed(content);return parsed.pairs

def build(root):
    content=Path(__file__).with_name('translation-offer.html').read_text()
    output=seite_rahmen('angebot/','','','angebot/',content,faq=visible_faq(content),base='../')
    from icons import iconize
    (root/'angebot').mkdir(exist_ok=True)
    (root/'angebot/index.html').write_text(iconize(output))
