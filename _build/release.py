"""Package only public pages and their local dependencies for static hosting."""
from argparse import ArgumentParser
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
import json
import re
import shutil
import zipfile
from pages import generated_pages

ROOT=Path(__file__).resolve().parent.parent
CSS_URL=re.compile(r'url\(\s*[\'"]?([^\'"\)]+)')
JS_IMPORT=re.compile(r'(?:import\s+(?:[^\n;]*?\sfrom\s*)?|export\s+[^\n;]*?\sfrom\s*)[\'"]([^\'"]+)[\'"]')

def dependencies(path):
    text=path.read_text()
    links=[]
    if path.suffix in {'.html','.svg'}:
        class Links(HTMLParser):
            def handle_starttag(self,tag,attributes):
                for key,value in attributes:
                    if not value:continue
                    if key in {'src','href','poster','content','data-src','data-image'}:links.append(value)
                    elif key=='srcset':links.extend(part.strip().split()[0] for part in value.split(',') if part.strip())
                    elif key=='style':links.extend(CSS_URL.findall(value))
        parser=Links();parser.feed(text)
    if path.suffix=='.css':links.extend(CSS_URL.findall(text))
    if path.suffix in {'.js','.mjs'}:links.extend(JS_IMPORT.findall(text))
    for value in links:
        u=urlsplit(value.strip())
        if u.scheme and (u.scheme!='https' or u.netloc!='tafolli.net'):continue
        if u.netloc and u.netloc!='tafolli.net':continue
        if not u.path:continue
        # Content metadata is often text rather than a file reference.
        if not (u.netloc or value.startswith(('./','../','/','assets/')) or Path(u.path).suffix in {'.html','.css','.js','.mjs','.svg','.png','.webp','.jpg','.ico','.woff2'}):continue
        target=(ROOT/unquote(u.path).lstrip('/')) if u.netloc or u.path.startswith('/') else (path.parent/unquote(u.path))
        target=target.resolve()
        if target.is_dir():target=target/'index.html'
        try:relative=target.relative_to(ROOT)
        except ValueError:raise ValueError(f'Public dependency escapes website: {value}')
        if relative.parts[0] in {'_build','.git','.github'}:raise ValueError(f'Internal file linked publicly: {value}')
        if not target.is_file():raise FileNotFoundError(f'{path.relative_to(ROOT)}: missing dependency {value}')
        yield target

def package(output,archive=None):
    if output.exists():raise FileExistsError(f'Refusing to overwrite existing output: {output}')
    output.mkdir(parents=True)
    pending=generated_pages(ROOT)
    included=set()
    while pending:
        path=pending.pop().resolve()
        if path in included:continue
        included.add(path)
        if path.suffix in {'.html','.svg','.css','.js','.mjs'}:pending.extend(dependencies(path))
    included.update(ROOT/name for name in ['robots.txt','sitemap.xml','CNAME'])
    for path in sorted(included):
        destination=output/path.relative_to(ROOT)
        destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,destination)
    (output/'.nojekyll').touch()
    files=sorted(path for path in output.rglob('*') if path.is_file())
    manifest={'files':{str(path.relative_to(output)):{'sha256':sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size} for path in files}}
    if archive:
        archive.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for path in files:
                item=zipfile.ZipInfo(str(path.relative_to(output)),date_time=(1980,1,1,0,0,0))
                item.compress_type=zipfile.ZIP_DEFLATED;item.external_attr=0o100644<<16
                z.writestr(item,path.read_bytes())
        manifest['archive']={'name':archive.name,'sha256':sha256(archive.read_bytes()).hexdigest(),'bytes':archive.stat().st_size}
    output.with_name(output.name+'-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'PASS: public package contains {len(files)} files ({sum(path.stat().st_size for path in files):,} bytes); no build sources or internal notes.')

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--archive',type=Path)
    args=parser.parse_args();package(args.output.resolve(),args.archive.resolve() if args.archive else None)
