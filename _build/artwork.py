"""Original neural brain artwork: two hemispheres, circuits and an OS frame."""
import pathlib, math
ROOT = pathlib.Path(__file__).resolve().parent.parent

def build():
    shape = 'M309 127 C288 90 249 87 226 110 C194 95 164 113 159 141 C124 143 111 165 119 192 C82 210 84 250 102 267 C78 300 93 329 114 340 C100 375 117 401 142 409 C137 442 161 466 191 460 C208 487 242 486 265 468 C294 475 307 451 309 428 Z'
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640"><defs><linearGradient id="brain" x2="1" y2="1"><stop stop-color="#3f5132"/><stop offset=".55" stop-color="#202b22"/><stop offset="1" stop-color="#192219"/></linearGradient><linearGradient id="core" x2="0" y2="1"><stop stop-color="#f28857"/><stop offset="1" stop-color="#d1ed78"/></linearGradient></defs>']
    parts.append('<g fill="none" stroke="#20231f" stroke-opacity=".25"><path d="M77 147V77H147M493 77H563V147M563 493V563H493M147 563H77V493"/><path d="M77 320H103M537 320H563M320 77V105M320 523V563" stroke-dasharray="3 5"/></g>')
    for mirror in [False, True]:
        parts.append('<g'+(' transform="translate(640 0) scale(-1 1)"' if mirror else '')+'>')
        parts.append(f'<defs><clipPath id="hemisphere{int(mirror)}"><path d="{shape}"/></clipPath></defs><path d="{shape}" fill="url(#brain)" stroke="#a7c975" stroke-width="1.3"/>')
        parts.append(f'<g clip-path="url(#hemisphere{int(mirror)})" fill="none" stroke="#b4d47c" stroke-opacity=".28" stroke-width=".65">')
        for row in range(24):
            pts=[]
            for col in range(16):
                x=82+col*16+6*math.sin(row*.55+col*.4)
                y=96+row*17+8*math.sin(col*.5+row*.3)
                pts.append((x,y))
            parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'"/>')
        for col in range(16):
            pts=[(82+col*16+6*math.sin(row*.55+col*.4),96+row*17+8*math.sin(col*.5+row*.3)) for row in range(24)]
            parts.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'"/>')
        parts.append('</g>')
        folds=['M226 110C205 140 242 169 218 192S157 175 159 141','M119 192C161 203 135 239 165 253S231 233 250 266','M102 267C151 274 122 310 154 327S216 295 238 326','M142 409C161 377 206 417 223 390S197 344 242 358','M191 460C172 433 234 447 254 415','M309 167C276 141 258 191 279 211S261 257 282 277','M309 301C278 302 268 332 286 351S267 384 288 407','M172 131C184 159 164 172 189 183','M139 350C172 337 176 367 196 354','M265 468C260 442 299 430 284 411']
        for d in folds: parts.append(f'<path d="{d}" fill="none" stroke="#d1ed78" stroke-width="1.2" stroke-linecap="round" opacity=".4"/>')
        for row in range(7):
            for col in range(5):
                x=151+col*31+9*math.sin(row*2+col); y=173+row*40+8*math.cos(col*2+row)
                if col==0 and row in (0,6): continue
                parts.append(f'<path d="M{x:.1f} {y:.1f}h18l12 13" fill="none" stroke="#f3f1e9" stroke-opacity=".4" stroke-width=".8"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{3 if (row+col)%3 else 4}" fill="{ "#f28857" if (row+col)%5==0 else "#f3f1e9"}"/>')
        parts.append('</g>')
    parts.append('<path d="M317 156V461Q315 487 301 510M325 156V461Q327 487 341 510" fill="none" stroke="url(#core)" stroke-width="3"/><rect x="292" y="284" width="56" height="56" rx="7" fill="#20231f" stroke="#f28857"/><text x="320" y="319" text-anchor="middle" font-family="monospace" font-size="19" fill="#d1ed78">AI</text><g fill="#40562e" font-family="monospace" font-size="9" letter-spacing="2"><text x="91" y="64">NEURAL OS / TAFOLLI</text><text x="91" y="589">KNOWLEDGE / REASON / ACTION</text><text x="440" y="589">HUMAN CONTROL</text></g></svg>')
    (ROOT/'assets/intelligence.svg').write_text(''.join(parts))
if __name__=='__main__': build()
