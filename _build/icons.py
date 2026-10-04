"""Replace decorative font glyphs with our shared SVG assets at build time.

Keep this final pass common to every page, including the localized homepages.
Scripts, metadata and existing artwork remain untouched.
"""
import hashlib
import html
from html.parser import HTMLParser
from pathlib import Path

ASSET = Path(__file__).resolve().parent.parent / 'assets/icons.svg'
VERSION = hashlib.sha256(ASSET.read_bytes()).hexdigest()[:10]
GLYPHS = {
    '↗': 'arrow-up-right', '↙': 'arrow-down-left', '→': 'arrow-right',
    '↑': 'arrow-up', '↓': 'arrow-down', '⌄': 'chevron-down',
    '✳': 'spark', '◎': 'target', 'Ⅱ': 'pause', '▷': 'play',
    '≡': 'list', '⌁': 'signal', '▤': 'document', '●': 'dot',
}

def icon(name):
    return (f'<svg class="site-icon" data-icon="{name}" viewBox="0 0 24 24" '
            f'width="24" height="24" aria-hidden="true" focusable="false">'
            f'<use href="/assets/icons.svg?v={VERSION}#{name}"></use></svg>')

class IconMarkup(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'}
    PROTECTED = {'head', 'script', 'style', 'svg', 'textarea', 'code', 'pre'}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())
        if tag not in self.VOID:
            self.stack.append((tag, dict(attrs)))

    def handle_startendtag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.parts.append(f'</{tag}>')
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def replace(self, data):
        if any(tag in self.PROTECTED for tag, _ in self.stack):
            return data
        # FAQ/menu plus signs are graphics; phone numbers and arithmetic are text.
        if data.strip() == '+' and self.stack and self.stack[-1][1].get('aria-hidden') == 'true':
            return data.replace('+', icon('plus'))
        return ''.join(icon(GLYPHS[c]) if c in GLYPHS else c for c in data.replace('\ufe0f', ''))

    def handle_data(self, data):
        self.parts.append(self.replace(data))

    def handle_entityref(self, name):
        original = f'&{name};'
        decoded = html.unescape(original)
        self.parts.append(self.replace(decoded) if decoded in GLYPHS else original)

    def handle_charref(self, name):
        original = f'&#{name};'
        decoded = html.unescape(original)
        self.parts.append(self.replace(decoded) if decoded in GLYPHS else original)

    def handle_decl(self, decl):
        self.parts.append(f'<!{decl}>')

    def handle_comment(self, data):
        self.parts.append(f'<!--{data}-->')

def iconize(markup):
    parser = IconMarkup()
    parser.feed(markup)
    parser.close()
    return ''.join(parser.parts)
