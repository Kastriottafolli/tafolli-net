"""Shared, localized page transition for every public document, including nested URLs."""
from hashlib import sha256
import re
from brand import intro
from pages import generated_pages

def build(root):
    version=sha256((root/'assets/brand-loader.css').read_bytes()+(root/'assets/brand.js').read_bytes()).hexdigest()[:10]
    for file in generated_pages(root):
        source=file.read_text()
        lang=re.search(r'<html lang="([^"]+)"',source).group(1)
        base='/' if file.name=='404.html' else '../'*(len(file.relative_to(root).parts)-1)
        head=f'<link rel="stylesheet" href="{base}assets/brand-loader.css?v={version}"><script src="{base}assets/brand.js?v={version}"></script>'
        source=source.replace('</head>',head+'</head>',1)
        source=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+intro(lang,base),source,count=1)
        file.write_text(source)
    print('  Brand loading screen: every page entry and native internal navigation.')
