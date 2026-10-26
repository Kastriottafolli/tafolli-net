"""Build and run the same checks locally and in continuous integration."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent.parent

def run(*args,quiet=False):
    result=subprocess.run(args,cwd=ROOT,text=True,stdout=subprocess.PIPE if quiet else None,stderr=subprocess.STDOUT if quiet else None)
    if result.returncode:
        if quiet: print(result.stdout)
        raise SystemExit(result.returncode)

if __name__=='__main__':
    run(sys.executable,'_build/bau_alles.py',quiet=True)
    run(sys.executable,'_build/verify.py')
    run(sys.executable,'_build/check_detail.py')
    scripts=sorted([*ROOT.joinpath('assets').glob('*.js'),*ROOT.joinpath('assets').glob('*.mjs')])
    for script in scripts:run('node','--check',str(script.relative_to(ROOT)))
    print(f'PASS: syntax checked for {len(scripts)} JavaScript modules and scripts.',flush=True)
    run('node','--test',*(str(path.relative_to(ROOT)) for path in sorted(ROOT.joinpath('_build').glob('test_*.mjs'))))
