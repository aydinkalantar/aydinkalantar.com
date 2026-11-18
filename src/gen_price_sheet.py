"""Builds public/files/aydin-kalantar-price-sheet.pdf from the prices in gen_pricing.py.

Run: python3 src/gen_price_sheet.py   (needs Node with Playwright and Chromium installed)
"""
import html
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gen_pricing import MENU, PACKAGES, money  # noqa: E402

ROOT = Path(__file__).parent.parent
PDF = ROOT / 'public' / 'files' / 'aydin-kalantar-price-sheet.pdf'
e = html.escape

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');
@page { size: Letter; margin: 0 }
* { margin: 0; padding: 0; box-sizing: border-box }
html, body { background: #FAFAF7 }
body { font-family: Inter, sans-serif; color: #1A1A18; font-size: 8.6pt; line-height: 1.5;
       width: 8.5in; height: 11in; padding: .5in .6in .45in; overflow: hidden; display: flex; flex-direction: column }
.h { font-family: 'Space Grotesk'; font-weight: 700; letter-spacing: -.02em; line-height: 1.05 }
.label { font-size: 6.6pt; font-weight: 500; letter-spacing: .12em; text-transform: uppercase; color: #6B6B64 }
.soft { color: #44443F }
header { display: flex; justify-content: space-between; align-items: flex-start; padding-bottom: .22in; border-bottom: 1px solid #E5E5DF }
header .name { font-size: 20pt }
header .rule { width: .5in; height: 1.5px; background: #A65B32; margin: .1in 0 .08in }
header .contact { text-align: right; line-height: 1.7 }
h1 { font-size: 22pt; margin-top: .2in }
h1 span { color: #A65B32 }
.intro { margin-top: .08in; max-width: 5.4in }
.pk { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid #E5E5DF; margin-top: .18in }
.pk > div { padding: .17in .17in .2in; display: flex; flex-direction: column }
.pk > div + div { border-left: 1px solid #E5E5DF }
.pk .rec { background: #1A1A18; color: #FAFAF7 }
.pk .rec .soft, .pk .rec .label { color: #B9B9B0 }
.pk .top { display: flex; justify-content: space-between; align-items: center; height: .18in }
.tag { border: 1px solid #55554F; padding: 1px 5px; font-size: 5.8pt; letter-spacing: .1em; text-transform: uppercase; color: #B9B9B0 }
.pk .t { font-size: 13pt; margin-top: .1in }
.pk .for { margin-top: .05in; min-height: .48in }
.pk .price { border-top: 1px solid #E5E5DF; margin-top: .1in; padding-top: .1in }
.pk .rec .price { border-color: #3A3A36 }
.pk .mo { font-size: 18pt }
.pk .mo small { font-family: Inter; font-weight: 400; font-size: 8pt }
.pk ul { list-style: none; margin-top: .1in }
.pk li { display: flex; gap: 6px; margin-top: 3px }
.pk li::before { content: '—'; color: #8A8A82 }
.terms { margin-top: .08in; font-size: 7.2pt }
.menu { display: grid; grid-template-columns: 1fr 1fr; column-gap: .35in; margin-top: .2in }
.grp { break-inside: avoid; margin-bottom: .1in }
.grp ul { list-style: none; border-top: 1px solid #E5E5DF; margin-top: .05in }
.grp li { display: flex; justify-content: space-between; gap: 10px; border-bottom: 1px solid #E5E5DF; padding: 2.5px 0 }
.grp li span:last-child { text-align: right; color: #44443F; max-width: 60% }
.grp li span:first-child { min-width: 38% }
.grp li span.nw { white-space: nowrap }
footer { margin-top: auto; border-top: 1px solid #E5E5DF; padding-top: .1in; display: flex; justify-content: space-between; align-items: flex-end; font-size: 7.6pt }
footer b { font-weight: 600 }
"""


def page():
    cards = []
    for i, p in enumerate(PACKAGES, 1):
        rec = p.get('recommended')
        items = ''.join(f'<li><span>{e(x)}</span></li>' for x in p['includes'])
        cards.append(f'''<div class="{'rec' if rec else ''}">
  <div class="top"><span class="label">{i:02d}</span>{'<span class="tag">Recommended</span>' if rec else ''}</div>
  <div class="h t">{e(p['name'])}</div>
  <p class="for soft">{e(p['for'])}</p>
  <div class="price"><div class="h mo">{money(p['monthly'])}<small>/mo</small></div><div class="label" style="text-transform:none;letter-spacing:.02em">+ {money(p['setup'])} one-time setup</div></div>
  <ul>{items}</ul>
</div>''')
    # Two columns: first two groups left, rest right.
    groups = [f'''<div class="grp"><div class="label">{e(n)}</div><ul>{''.join(f'<li><span>{e(a)}</span><span{" class=nw" if len(b) < 24 else ""}>{e(b)}</span></li>' for a, b, _ in rows)}</ul></div>''' for n, rows in MENU]
    left, right = ''.join(groups[:2]), ''.join(groups[2:])
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>Aydin Kalantar · Price sheet</title><style>{CSS}</style></head><body>
<header>
  <div><div class="h name">AYDIN KALANTAR</div><div class="rule"></div><div class="label">AI Automation · Websites · Local SEO</div></div>
  <div class="contact soft"><b style="color:#1A1A18">216-339-8948</b><br>hello@aydinkalantar.com<br>aydinkalantar.com/pricing</div>
</header>
<h1 class="h">Never miss another lead<span>.</span></h1>
<p class="intro soft">Clear prices for small businesses in Cleveland, Northeast Ohio and beyond. Pick a package, or mix services from the list. Either way, you get the scope and price in writing before any work starts.</p>
<div class="pk">{''.join(cards)}</div>
<p class="terms soft">Monthly plans: 3-month minimum, then month to month. Setup: half to start, half at launch. Ad spend is paid directly to Google or Meta. Prices in USD.</p>
<div class="menu"><div><div class="label" style="margin-bottom:.08in;color:#1A1A18">Individual services · starting prices</div>{left}</div><div style="padding-top:.2in">{right}</div></div>
<footer>
  <div class="soft">Scope and price in writing before work starts.<br>I meet clients in person across Cleveland and Northeast Ohio.</div>
  <div style="text-align:right"><b>Aydin Kalantar</b> · Mayfield Heights, Ohio<br><span class="soft">216-339-8948 · hello@aydinkalantar.com</span></div>
</footer>
</body></html>'''


RENDER = """
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  await p.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
"""

if __name__ == '__main__':
    PDF.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'sheet.html'
        src.write_text(page())
        js = Path(tmp) / 'render.js'
        js.write_text(RENDER)
        subprocess.run(['node', str(js), str(src), str(PDF)], check=True)
    print(f'wrote {PDF}')
