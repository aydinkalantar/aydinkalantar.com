"""Generates the marquetry gallery pages (src/pages/art/**) from src/art/works.json.

Run `python3 src/gen_art.py`, then `npm run build`.
"""
import html, json, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'pages', 'art')
DATA = json.load(open(os.path.join(ROOT, 'art', 'works.json')))

# Works without a photo yet show an empty slot. Turn off before launch to list only photographed pieces.
SHOW_PENDING = True

EMAIL = 'hello@aydinkalantar.com'  # CONFIRM: replace with the real contact email (also in layout.html)
PHONE, PHONE_HREF = '216-339-8948', 'tel:+12163398948'
FILMS = [('00vjf7zV2Vo', 'Studio film 01'), ('atCx2KVDeFA', 'Studio film 02'), ('eBr9JblMa5I', 'Studio film 03')]

e = html.escape
COLLECTIONS = {c['id']: c for c in DATA['collections']}


def slug(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


works = [dict(w, slug=slug(w['title'])) for w in DATA['works']]
works = [w for w in works if SHOW_PENDING or w.get('photo')]
# Photographed pieces lead each collection.
works.sort(key=lambda w: (list(COLLECTIONS).index(w['collection']), not w.get('photo')))


SITE = 'https://aydinkalantar.com'


def meta_comment(title, description, nav='art', image=None, noindex=False):
    meta = {'title': title, 'description': description, 'nav': nav, 'contact': 'Looking for a piece, or one of your own?', 'theme': 'dark'}
    if image:
        meta['image'] = image  # social preview (og:image)
    if noindex:
        meta['noindex'] = True  # keep placeholder pages out of search until they have a photo
    return '<!-- ' + json.dumps(meta) + ' -->\n'


def alt_text(w, on_wall=False):
    kind = 'portrait' if w['collection'] == 'portraits' else 'wall art'
    where = ', shown hanging on a gallery wall' if on_wall else ''
    return f"{w['title']}, natural wood veneer marquetry {kind} by Aydin Kalantar{where}"


def room_picture(w, cls, eager=False, tall_only=False):
    """Room shot of a piece: a tall crop on phones, the wide scene on larger screens."""
    r = f"/assets/art/rooms/{w['room']}"
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    if tall_only:
        return (f'<picture><source srcset="{r}-tall.webp" type="image/webp">'
                f'<img src="{r}-tall.jpg" width="800" height="1237" alt="{e(alt_text(w, True))}" {load} decoding="async" class="{cls}"></picture>')
    return (f'<picture>'
            f'<source media="(max-width: 767px)" srcset="{r}-tall.webp" type="image/webp">'
            f'<source media="(max-width: 767px)" srcset="{r}-tall.jpg">'
            f'<source srcset="{r}-wide.webp" type="image/webp">'
            f'<img src="{r}-wide.jpg" width="1600" height="1120" alt="{e(alt_text(w, True))}" {load} decoding="async" class="{cls}"></picture>')


def mailto(subject):
    return f'mailto:{EMAIL}?subject=' + subject.replace(' ', '%20').replace(',', '%2C')


def picture(w, cls, eager=False):
    if not w.get('photo'):
        return (f'<div class="{cls} grid place-items-center bg-canvas">'
                '<span class="meta">Photo coming</span></div>')
    alt = alt_text(w)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<picture><source srcset="/assets/art/{w["photo"]}.webp" type="image/webp">'
            f'<img src="/assets/art/{w["photo"]}.jpg" width="648" height="810" alt="{e(alt)}" {load} decoding="async" class="{cls} object-cover"></picture>')


def facts(w):
    rows = [('Collection', COLLECTIONS[w['collection']]['name']), ('Medium', 'Natural wood veneer marquetry')]
    for key, label in (('format', 'Format'), ('size', 'Size'), ('woods', 'Woods'), ('year', 'Year')):
        if w.get(key):
            rows.append((label, w[key]))
    return rows


def card(w, n):
    coll = COLLECTIONS[w['collection']]['name']
    return f'''        <li class="reveal" data-collection="{w['collection']}">
          <a href="/art/works/{w['slug']}/" class="group block">
            <div class="overflow-hidden border border-line">
              {picture(w, 'aspect-[4/5] w-full transition-transform duration-900 ease-craft group-hover:scale-[1.03]')}
            </div>
            <div class="mt-4 flex items-baseline justify-between gap-4">
              <span class="font-heading text-lg font-bold tracking-tight text-ink transition-colors group-hover:text-accent">{e(w['title'])}</span>
              <span class="meta">{n:02d}</span>
            </div>
            <p class="meta mt-1">{coll}{' · ' + e(w['price']) if w.get('price') else ''}</p>
          </a>
        </li>'''


def films_section():
    items = '\n'.join(f'''          <figure class="reveal">
            <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener" data-yt="{vid}" class="group relative block aspect-video overflow-hidden border border-line-dark bg-ink" aria-label="Play marquetry {label.lower()}">
              <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" width="480" height="360" alt="" loading="lazy" decoding="async" class="h-full w-full object-cover opacity-80 transition duration-900 ease-craft group-hover:scale-[1.02] group-hover:opacity-100">
              <span class="absolute inset-0 grid place-items-center"><span class="grid h-14 w-14 place-items-center rounded-full border border-canvas/70 text-canvas transition-colors group-hover:border-accent group-hover:bg-accent">▶</span></span>
            </a>
            <figcaption class="media-caption"><span>{label}</span><span>YouTube</span></figcaption>
          </figure>''' for vid, label in FILMS)
    return f'''    <!-- How it's made -->
    <section id="process" class="surface-ink section scroll-mt-16">
      <div class="container-site">
        <div class="grid-asym items-end">
          <div class="md:col-span-6">
            <p class="label reveal">How it's made</p>
            <h2 class="display-lg reveal mt-8">From drawing to wall, by hand.</h2>
          </div>
          <p class="reveal leading-relaxed md:col-span-5 md:col-start-8">Each piece starts as a drawing. Veneers are chosen for their grain and tone, cut fragment by fragment, fitted, glued and pressed, then finished to bring out the wood's own color. Nothing is stained or printed.</p>
        </div>
        <div class="mt-14 grid gap-10 md:grid-cols-3 md:gap-6">
{items}
        </div>
      </div>
    </section>
'''


def commission_cta(heading='Have a piece in mind?'):
    return f'''    <!-- Commission -->
    <section class="section border-t border-line">
      <div class="container-site grid-asym items-end">
        <div class="md:col-span-7">
          <p class="label reveal">Commissions</p>
          <h2 class="display-lg reveal mt-8">{heading}</h2>
          <p class="lede reveal mt-6">A portrait from your own photo, a family name, a verse, or an abstract piece sized for one wall. Tell me what you have in mind and I'll come back with a drawing and a wood selection.</p>
        </div>
        <div class="reveal flex flex-col gap-3 md:col-span-4 md:col-start-9">
          <a href="/art/commissions/" class="btn-primary group">Start a commission <span aria-hidden="true" class="arrow">→</span></a>
          <a href="{PHONE_HREF}" class="btn-secondary">Call {PHONE}</a>
        </div>
      </div>
    </section>
'''


FAQ = [
    ('What is marquetry?', 'Marquetry is the craft of building a picture from thin sheets of wood veneer. Each fragment is cut to shape and fitted against its neighbors, so the image comes from the natural grain and color of the wood rather than paint.'),
    ('Which woods do you use?', 'Natural veneers such as walnut, oak, maple and a range of exotic species, chosen piece by piece for tone and grain.'),
    ('Is any of it painted or stained?', "No. Every color and shadow in a piece is the wood's own."),
    ('Can I order a piece in a different size?', 'Yes. Most pieces can be made again at a size that suits your wall. Ask about the piece you like and I will tell you what is possible.'),
    ('How do I buy a piece?', 'Pieces marked Buy check out securely with Stripe. For anything else, use Enquire and I will reply personally.'),
]


def faq_section():
    rows = '\n'.join(f'''          <details class="group border-b border-line py-6">
            <summary class="flex cursor-pointer list-none items-baseline justify-between gap-6 font-heading text-lg font-bold tracking-tight text-ink transition-colors hover:text-accent [&::-webkit-details-marker]:hidden">{e(q)}<span aria-hidden="true" class="meta transition-transform duration-400 group-open:rotate-45">+</span></summary>
            <p class="body mt-4 max-w-prose">{e(a)}</p>
          </details>''' for q, a in FAQ)
    return f'''    <!-- FAQ -->
    <section id="faq" class="section scroll-mt-16 border-t border-line">
      <div class="container-site grid-asym">
        <div class="md:col-span-4">
          <p class="label reveal">Questions</p>
          <h2 class="display-md reveal mt-8">About the work.</h2>
        </div>
        <div class="reveal border-t border-line md:col-span-7 md:col-start-6">
{rows}
        </div>
      </div>
    </section>
'''


def gallery_page():
    chips = ''.join(
        f'<li><button type="button" data-filter="{cid}" class="tag cursor-pointer transition-colors hover:border-accent hover:text-accent aria-pressed:border-ink aria-pressed:text-ink" aria-pressed="false">{c["name"]}</button></li>'
        for cid, c in COLLECTIONS.items())
    cards = '\n'.join(card(w, i + 1) for i, w in enumerate(works))
    featured = [next(w for w in works if w['slug'] == sl) for sl in DATA.get('featured', [])]
    slides = '\n'.join(f'''          <li class="slide relative w-full shrink-0 snap-start" id="slide-{w['slug']}" aria-roledescription="slide" aria-label="{n} of {len(featured)}: {e(w['title'])}">
            {room_picture(w, 'block aspect-[800/1237] w-full object-cover md:aspect-[10/7]', eager=n == 1)}
            <div class="theme-light md:absolute md:inset-y-0 md:right-[6%] md:flex md:w-[38%] md:items-center">
              <div class="bg-canvas px-5 py-8 text-center md:bg-transparent md:p-0">
                <p class="label">{COLLECTIONS[w['collection']]['name']} · Marquetry</p>
                <h2 class="display-lg mt-4">{e(w['title'])}</h2>
                <p class="body mx-auto mt-4 max-w-sm">{e(w['description'])}</p>
                <div class="mt-6 flex flex-wrap justify-center gap-3">
                  <a href="/art/works/{w['slug']}/" class="btn-primary group !px-5 !py-3">View the piece <span aria-hidden="true" class="arrow">→</span></a>
                  <a href="/art/commissions/" class="btn-secondary !px-5 !py-3">Commission one</a>
                </div>
              </div>
            </div>
          </li>''' for n, w in enumerate(featured, 1))
    dots = ''.join(f'<li><button type="button" data-slide-to="{n}" class="block h-px w-8 bg-line transition-colors aria-[current=true]:bg-ink hover:bg-accent" aria-label="Show {e(w["title"])}"><span class="sr-only">{e(w["title"])}</span></button></li>' for n, w in enumerate(featured))
    hero_img = f"{SITE}/assets/art/rooms/{featured[0]['room']}-wide.jpg" if featured else None
    return meta_comment(
        'Marquetry Art Gallery · Aydin Kalantar',
        'Original natural wood veneer marquetry by Aydin Kalantar: portraits, abstract pieces and the Bismillah collection, cut and fitted by hand. Buy a piece or commission your own.',
        image=hero_img,
    ) + f'''
    <!-- Intro -->
    <section class="pb-10 pt-14 lg:pb-14 lg:pt-20">
      <div class="container-site grid-asym items-end">
        <div class="md:col-span-7">
          <p class="label reveal">Marquetry Art · Gallery</p>
          <h1 class="display-xl reveal mt-8">Pictures made of wood.</h1>
        </div>
        <p class="lede reveal md:col-span-4 md:col-start-9">Original wall art assembled by hand from natural wood veneers. Every tone is the wood's own grain and color, cut and fitted one fragment at a time.</p>
      </div>
    </section>

    <!-- Featured pieces: swipe or use the arrows; nothing moves on its own -->
    <section class="pb-22 lg:pb-30" aria-roledescription="carousel" aria-label="Featured pieces" data-slider>
      <div class="container-site">
        <div class="relative overflow-hidden border border-line">
          <ul class="flex snap-x snap-mandatory overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden" data-slider-track>
{slides}
          </ul>
        </div>
        <div class="mt-5 flex items-center justify-between gap-6">
          <ol class="flex items-center gap-2" aria-label="Choose a piece">{dots}</ol>
          <div class="flex gap-2">
            <button type="button" data-slide-step="-1" class="grid h-10 w-10 place-items-center border border-line text-ink transition-colors hover:border-accent hover:text-accent" aria-label="Previous piece">←</button>
            <button type="button" data-slide-step="1" class="grid h-10 w-10 place-items-center border border-line text-ink transition-colors hover:border-accent hover:text-accent" aria-label="Next piece">→</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Works -->
    <section id="works" class="section scroll-mt-16 border-t border-line !pt-18">
      <div class="container-site">
        <div class="flex flex-wrap items-end justify-between gap-6 border-b border-line pb-6">
          <div>
            <p class="label">The works</p>
            <h2 class="display-md mt-4">{len(works)} pieces in {len(COLLECTIONS)} collections.</h2>
          </div>
          <ul class="flex flex-wrap gap-2" aria-label="Filter by collection">
            <li><button type="button" data-filter="all" class="tag cursor-pointer transition-colors hover:border-accent hover:text-accent aria-pressed:border-ink aria-pressed:text-ink" aria-pressed="true">All</button></li>{chips}
          </ul>
        </div>
        <ul id="works-grid" class="mt-12 grid gap-x-6 gap-y-14 sm:grid-cols-2 lg:grid-cols-3">
{cards}
        </ul>
      </div>
    </section>

{films_section()}
{commission_cta()}
{faq_section()}'''


def work_page(w, i):
    coll = COLLECTIONS[w['collection']]
    rows = '\n'.join(f'            <div class="flex justify-between gap-6 border-b border-line py-3"><dt class="label">{k}</dt><dd class="text-right text-ink">{e(v)}</dd></div>' for k, v in facts(w))
    if w.get('stripe'):
        buy = f'<a href="{e(w["stripe"])}" class="btn-primary group" rel="noopener">Buy{" · " + e(w["price"]) if w.get("price") else ""} <span aria-hidden="true" class="arrow">↗</span></a>'
    else:
        buy = f'<a href="{mailto("Enquiry: " + w["title"])}" class="btn-primary group">Enquire about this piece <span aria-hidden="true" class="arrow">↗</span></a>'
    price = e(w['price']) if w.get('price') else 'Price on request'
    others = [o for o in works if o['collection'] == w['collection'] and o is not w and o.get('photo')]
    others += [o for o in works if o['collection'] != w['collection'] and o.get('photo')]
    more = '\n'.join(card(o, works.index(o) + 1) for o in others[:3])
    desc = w.get('description') or coll['blurb']
    url = f"{SITE}/art/works/{w['slug']}/"
    images = []
    if w.get('room'):
        images += [f"{SITE}/assets/art/rooms/{w['room']}-wide.jpg", f"{SITE}/assets/art/rooms/{w['room']}-tall.jpg"]
    if w.get('photo'):
        images.append(f"{SITE}/assets/art/{w['photo']}.jpg")
    artwork = {
        '@context': 'https://schema.org', '@type': 'VisualArtwork', '@id': url + '#artwork', 'url': url,
        'name': w['title'], 'description': desc, 'artform': 'Marquetry', 'artMedium': 'Natural wood veneer',
        'creator': {'@type': 'Person', '@id': f'{SITE}/#person', 'name': 'Aydin Kalantar'},
        'isPartOf': {'@type': 'Collection', 'name': f"{coll['name']} · Marquetry by Aydin Kalantar", 'url': f'{SITE}/art/'},
    }
    if images:
        artwork['image'] = images
    if w.get('year'):
        artwork['dateCreated'] = str(w['year'])
    if w.get('price_usd') and w.get('stripe'):
        artwork['offers'] = {'@type': 'Offer', 'price': str(w['price_usd']), 'priceCurrency': 'USD', 'url': w['stripe'], 'availability': 'https://schema.org/InStock'}
    main_img = (room_picture(w, 'w-full', eager=True, tall_only=True) if w.get('room')
                else picture(w, 'aspect-[4/5] w-full', eager=True))
    return meta_comment(
        f"{w['title']} · Marquetry by Aydin Kalantar",
        f"{desc} Original natural wood veneer marquetry by Aydin Kalantar, {coll['name']} collection.",
        image=images[0] if images else None, noindex=not w.get('photo'),
    ) + f'''
    <script type="application/ld+json">{json.dumps(artwork, ensure_ascii=False)}</script>
    <section class="pb-22 pt-10 lg:pb-30 lg:pt-14">
      <div class="container-site">
        <nav aria-label="Breadcrumb" class="meta"><a class="link" href="/art/">Gallery</a> <span aria-hidden="true">/</span> <a class="link" href="/art/?c={coll['id']}#works">{coll['name']}</a></nav>
        <div class="grid-asym mt-10 items-start">
          <figure class="md:col-span-7">
            <div class="overflow-hidden border border-line">{main_img}</div>
          </figure>
          <div class="md:sticky md:top-28 md:col-span-4 md:col-start-9">
            <p class="label">{coll['name']} · {i:02d}</p>
            <h1 class="display-lg mt-6">{e(w['title'])}</h1>
            <p class="body mt-6">{e(desc)}</p>
            <p class="mt-8 font-heading text-2xl font-bold tracking-tight text-ink">{price}</p>
            <div class="mt-6 flex flex-col gap-3">
              {buy}
              <a href="/art/commissions/" class="btn-secondary">Commission one like it</a>
            </div>
            <dl class="mt-10 border-t border-line">
{rows}
            </dl>
          </div>
        </div>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site">
        <div class="flex items-baseline justify-between gap-6 border-b border-line pb-5">
          <p class="label">More from the gallery</p>
          <a class="link meta" href="/art/#works">All works</a>
        </div>
        <ul class="mt-10 grid gap-x-6 gap-y-14 sm:grid-cols-2 lg:grid-cols-3">
{more}
        </ul>
      </div>
    </section>
'''


STEPS = [
    ('Tell me the idea', 'A photo, a name, a verse or a feeling for a room. Send what you have, along with the wall it is for.'),
    ('Drawing and woods', 'I draw the piece and choose the veneers that will carry it, then share both with you before any wood is cut.'),
    ('Cut and fitted by hand', 'Every fragment is cut, fitted, glued and pressed in the studio. You get progress photos along the way.'),
    ('Finished and delivered', 'The piece is finished to bring out the grain, then packed and shipped ready to hang.'),
]


def commissions_page():
    steps = '\n'.join(f'''          <li class="reveal border-t border-line pt-6">
            <span class="meta">{n:02d}</span>
            <h3 class="mt-4 text-xl">{t}</h3>
            <p class="body mt-3">{d}</p>
          </li>''' for n, (t, d) in enumerate(STEPS, 1))
    return meta_comment(
        'Commission a Marquetry Piece · Aydin Kalantar',
        'Commission an original natural wood veneer marquetry piece from Aydin Kalantar: a portrait from your photo, calligraphy, or an abstract piece made for your wall.',
        image=f'{SITE}/assets/art/rooms/mona-lisa-wide.jpg',
    ) + f'''
    <section class="pb-22 pt-14 lg:pb-30 lg:pt-22">
      <div class="container-site grid-asym items-end">
        <div class="md:col-span-7">
          <nav aria-label="Breadcrumb" class="meta"><a class="link" href="/art/">Gallery</a> <span aria-hidden="true">/</span> Commissions</nav>
          <h1 class="display-xl reveal mt-10">Made for your wall.</h1>
          <p class="lede reveal mt-8">A portrait from your own photo, a family name, a verse, or an abstract piece in the woods that suit your room. Every commission is drawn, cut and fitted by hand.</p>
        </div>
        <div class="reveal flex flex-col gap-3 md:col-span-4 md:col-start-9">
          <a href="{mailto('Marquetry commission')}" class="btn-primary group">Email {EMAIL} <span aria-hidden="true" class="arrow">↗</span></a>
          <a href="{PHONE_HREF}" class="btn-secondary">Call {PHONE}</a>
          <p class="meta mt-2">Or ask Max, the assistant in the corner of this page.</p>
        </div>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site">
        <p class="label reveal">How a commission works</p>
        <ol class="mt-12 grid gap-10 sm:grid-cols-2 lg:grid-cols-4 lg:gap-6">
{steps}
        </ol>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site grid-asym">
        <div class="md:col-span-4">
          <p class="label reveal">What to send</p>
          <h2 class="display-md reveal mt-8">A few details help me quote.</h2>
        </div>
        <ul class="prose-case reveal md:col-span-7 md:col-start-6">
          <li><strong>The subject.</strong> A clear photo for a portrait, or the words and script for calligraphy.</li>
          <li><strong>The size.</strong> Roughly how wide and tall, or a photo of the wall it will hang on.</li>
          <li><strong>The mood.</strong> Light or dark woods, warm or cool, and any piece in the gallery you like.</li>
          <li><strong>The date.</strong> If it is a gift, when you need it.</li>
        </ul>
      </div>
    </section>

{films_section()}
{faq_section()}'''


if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, 'works'))
shown = [w for w in works if w.get('photo')]
gallery_ld = {
    '@context': 'https://schema.org', '@type': 'CollectionPage', 'url': f'{SITE}/art/',
    'name': 'Marquetry Art Gallery · Aydin Kalantar', 'author': {'@id': f'{SITE}/#person'},
    'mainEntity': {'@type': 'ItemList', 'itemListElement': [
        {'@type': 'ListItem', 'position': n, 'url': f"{SITE}/art/works/{w['slug']}/", 'name': w['title']} for n, w in enumerate(shown, 1)]},
}
open(os.path.join(OUT, 'index.html'), 'w').write(gallery_page() + f'\n    <script type="application/ld+json">{json.dumps(gallery_ld, ensure_ascii=False)}</script>\n')
open(os.path.join(OUT, 'commissions.html'), 'w').write(commissions_page())
for i, w in enumerate(works, 1):
    open(os.path.join(OUT, 'works', w['slug'] + '.html'), 'w').write(work_page(w, i))
print(f'wrote gallery, commissions and {len(works)} work pages')

# Image sitemap for the gallery, so search engines find every photo with its title.
def image_entry(src, title):
    return f'    <image:image><image:loc>{SITE}{src}</image:loc><image:title>{e(title)}</image:title></image:image>\n'


urls = [(f'{SITE}/art/', ''.join(image_entry(f"/assets/art/rooms/{w['room']}-wide.jpg", w['title']) for w in works if w.get('room'))),
        (f'{SITE}/art/commissions/', '')]
for w in shown:
    imgs = ''
    if w.get('room'):
        imgs += image_entry(f"/assets/art/rooms/{w['room']}-wide.jpg", f"{w['title']} on a gallery wall")
        imgs += image_entry(f"/assets/art/rooms/{w['room']}-tall.jpg", f"{w['title']} on a gallery wall")
    imgs += image_entry(f"/assets/art/{w['photo']}.jpg", f"{w['title']}, marquetry by Aydin Kalantar")
    urls.append((f"{SITE}/art/works/{w['slug']}/", imgs))
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
           + ''.join(f'  <url>\n    <loc>{u}</loc>\n{imgs}  </url>\n' for u, imgs in urls) + '</urlset>\n')
open(os.path.join(ROOT, '..', 'public', 'sitemap-art.xml'), 'w').write(sitemap)
print(f'wrote sitemap-art.xml with {len(urls)} pages')
