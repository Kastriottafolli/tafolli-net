"""One source for planner budgets, project types and their minimums."""
from pathlib import Path
from hashlib import sha256
import json
import re

CATALOG=json.loads(Path(__file__).with_name('planner-pricing.json').read_text())

def build(root):
    source='// Generated from _build/planner-pricing.json. Edit the source catalog.\n'
    source+='export const catalog='+json.dumps(CATALOG,ensure_ascii=False,separators=(',',':'))+';\n'
    root.joinpath('assets/planner-catalog.mjs').write_text(source)
    # Version the full import chain: a new page must not reuse a cached old model.
    for module,dependency in [('planner-model.mjs','planner-catalog.mjs'),('planner.js','planner-model.mjs'),('planner.js','form-delivery.mjs')]:
        path=root/'assets'/module
        version=sha256((root/'assets'/dependency).read_bytes()).hexdigest()[:10]
        pattern=r"(['\"])(\./"+re.escape(dependency)+r")(?:\?v=[a-f0-9]+)?\1"
        path.write_text(re.sub(pattern,lambda m:m[1]+m[2]+'?v='+version+m[1],path.read_text()))
