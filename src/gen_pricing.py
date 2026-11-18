"""Generates src/pages/pricing.html: packages and starting prices.

Prices confirmed by Ayden on 2026-11-18. Change them here, then run `python3 src/gen_pricing.py` and `npm run build`.
"""
import html
import json
from pathlib import Path

SITE = 'https://aydinkalantar.com'
OUT = Path(__file__).parent / 'pages' / 'pricing.html'
e = html.escape

PACKAGES = [
    {
        'name': 'Get Found',
        'for': 'For businesses that need customers to find them on Google and stop losing missed calls.',
        'setup': 750, 'monthly': 297,
        'includes': [
            'Google Business Profile setup and optimization',
            'Missed-call text-back: every missed caller gets a text right away',
            'Automatic review requests after each job',
            'Monthly Google Business Profile posts',
        ],
    },
    {
        'name': 'Never Miss a Lead',
        'for': 'For businesses that want every call, chat and form answered and booked, day and night.',
        'setup': 2500, 'monthly': 697, 'recommended': True,
        'includes': [
            'Everything in Get Found',
            'AI chat and voice agent on your website and phone line, trained on your business',
            'New 5-page website, or a refresh of your current one',
            'Monthly local SEO',
            'Monthly report: calls answered, leads captured, jobs booked',
        ],
    },
    {
        'name': 'Autopilot',
        'for': 'For growing businesses ready to automate follow-up and run paid ads.',
        'setup': 4500, 'monthly': 1297,
        'includes': [
            'Everything in Never Miss a Lead',
            'Two custom automations, such as quote follow-up, booking or CRM sync',
            'Google Ads management (ad spend paid to Google separately)',
            'Monthly strategy call',
        ],
    },
]

MENU = [
    ('AI & automation', [
        ('AI chat & voice agent', 'from $1,000 setup + $297/mo', '/services/ai-agents/'),
        ('Missed-call text-back', '$300 setup + $97/mo', None),
        ('Business automation', 'from $750 per workflow', '/services/automation/'),
        ('Automation retainer', 'from $750/mo', '/services/automation/'),
        ('Automation audit (credited if you hire me)', '$350', None),
        ('Agentic engineering', 'from $5,000, quoted per project', '/services/agentic-engineering/'),
    ]),
    ('Search & ads', [
        ('Google Business Profile optimization', '$500 one-time', '/services/seo/'),
        ('Local SEO', 'from $500/mo', '/services/seo/'),
        ('Google or Facebook Ads management', '$500 setup + from $500/mo, plus ad spend', '/services/seo/'),
    ]),
    ('Websites & apps', [
        ('Starter website (up to 5 pages)', 'from $2,500', '/services/web-design/'),
        ('Business website (up to 12 pages, SEO, booking)', 'from $4,500', '/services/web-design/'),
        ('Online store (Shopify or custom)', 'from $6,000', '/services/web-design/'),
        ('Hosting & care plan', 'from $79/mo', None),
        ('SaaS, web or mobile app', 'from $15,000, quoted per project', '/services/app-development/'),
        ('UI & UX design', 'from $85/hr, or quoted per project', '/services/ui-ux-design/'),
    ]),
    ('Design', [
        ('Logo & brand identity', 'from $1,500', '/services/branding/'),
        ('3D product rendering', 'from $250 per image', '/services/3d-rendering/'),
    ]),
]

FAQ = [
    ('Are there any hidden fees?', 'No. After a short call you get the scope, timeline and price in writing before any work starts. Ad spend, if you run ads, is paid directly to Google or Meta.'),
    ('Is there a contract?', 'Monthly plans have a 3-month minimum, then continue month to month.'),
    ('How is the setup fee paid?', 'Half to start and half at launch.'),
    ('Why does a done-for-you AI agent cost more than a $79 app?', 'The app is only the software. I set it up, train it on your services and prices, connect it to your phone, calendar and CRM, and check every month that it answers well and books jobs. You get the result without learning another tool.'),
    ('Do you meet in person?', 'Yes. I am based in Mayfield Heights and meet clients in person across Cleveland and Northeast Ohio. I also work remotely with businesses anywhere in the United States.'),
    ('What if I need something that is not listed?', 'Email or call with a few lines about what you need. Most projects mix a few services, and I quote them together.'),
]

DETAIL = '''          <details class="group border-b border-line py-6">
            <summary class="flex cursor-pointer list-none items-baseline justify-between gap-6 font-heading text-lg font-bold tracking-tight text-ink transition-colors hover:text-accent [&::-webkit-details-marker]:hidden">{q}<span aria-hidden="true" class="meta transition-transform duration-400 group-open:rotate-45">+</span></summary>
            <p class="body mt-4 max-w-prose">{a}</p>
          </details>'''


def money(n):
    return f'${n:,}'


def mailto(subject):
    return 'mailto:hello@aydinkalantar.com?subject=' + subject.replace(' ', '%20').replace('&', '%26')


def package_card(i, p):
    items = '\n'.join(f'              <li class="flex gap-3"><span aria-hidden="true" class="meta pt-[0.2rem]">—</span><span>{e(x)}</span></li>' for x in p['includes'])
    rec = p.get('recommended')
    tag = '<span class="tag">Recommended</span>' if rec else ''
    btn = 'btn-primary' if rec else 'btn-secondary'
    return f'''          <article class="card reveal{' surface-ink' if rec else ''}">
            <div class="flex h-7 items-center justify-between gap-4"><span class="meta">{i:02d}</span>{tag}</div>
            <h2 class="display-md mt-10">{e(p['name'])}</h2>
            <p class="body mt-4{' !text-canvas/70' if rec else ''}">{e(p['for'])}</p>
            <div class="mt-10 border-t {'border-line-dark' if rec else 'border-line'} pt-6">
              <p class="font-heading text-4xl font-bold tracking-tight {'text-canvas' if rec else 'text-ink'}">{money(p['monthly'])}<span class="body text-base{' !text-canvas/70' if rec else ''}">/mo</span></p>
              <p class="meta mt-2">+ {money(p['setup'])} one-time setup</p>
            </div>
            <ul class="body mt-8 mb-10 space-y-3{' !text-canvas/80' if rec else ''}">
{items}
            </ul>
            <a href="{mailto(p['name'] + ' package')}" class="{btn} group mt-auto{' !border-canvas !bg-canvas !text-ink hover:!border-accent hover:!bg-accent hover:!text-canvas' if rec else ''}">Get started <span aria-hidden="true" class="arrow">↗</span></a>
          </article>'''


def menu_group(name, rows):
    items = '\n'.join(
        f'''            <li class="flex flex-col gap-1 border-b border-line py-4 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6">
              <span class="text-ink">{f'<a class="link" href="{u}">{e(n)}</a>' if u else e(n)}</span>
              <span class="body tabular-nums sm:text-right">{e(p)}</span>
            </li>''' for n, p, u in rows)
    return f'''        <div class="reveal">
          <p class="label">{e(name)}</p>
          <ul class="mt-4 border-t border-line">
{items}
          </ul>
        </div>'''


def jsonld():
    offers = [{
        '@type': 'Offer',
        'name': f"{p['name']} package",
        'description': '; '.join(p['includes']),
        'priceCurrency': 'USD',
        'priceSpecification': [
            {'@type': 'UnitPriceSpecification', 'price': p['monthly'], 'priceCurrency': 'USD', 'unitText': 'MONTH', 'name': 'Monthly'},
            {'@type': 'PriceSpecification', 'price': p['setup'], 'priceCurrency': 'USD', 'name': 'One-time setup'},
        ],
        'seller': {'@id': SITE + '/#business'},
        'areaServed': [{'@type': 'City', 'name': 'Cleveland, Ohio'}, {'@type': 'Country', 'name': 'United States'}],
    } for p in PACKAGES]
    graph = [
        {'@type': 'OfferCatalog', '@id': SITE + '/pricing/#packages', 'name': 'Packages and pricing, Aydin Kalantar', 'itemListElement': offers},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Pricing', 'item': SITE + '/pricing/'}]},
    ]
    data = json.dumps({'@context': 'https://schema.org', '@graph': graph}, indent=2, ensure_ascii=False)
    return f'    <script type="application/ld+json">\n{data}\n    </script>'


def build():
    meta = {
        'title': 'Pricing · AI Agents, Websites & Local SEO in Cleveland, Ohio · Aydin Kalantar',
        'description': 'Clear prices for small businesses in Cleveland and Northeast Ohio: AI chat and voice agents, missed-call text-back, websites, local SEO and automation. Packages from $297 a month, with scope and price in writing before work starts.',
        'nav': 'pricing',
        'contact': 'Not sure which fits? Ask me.',
    }
    cards = '\n'.join(package_card(i, p) for i, p in enumerate(PACKAGES, 1))
    menu = '\n'.join(menu_group(n, r) for n, r in MENU)
    faq = '\n'.join(DETAIL.format(q=e(q), a=e(a)) for q, a in FAQ)
    return f'''<!-- {json.dumps(meta)} -->
{jsonld()}
    <section class="relative border-b border-line">
      <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
      <div class="container-site grid-asym relative pb-18 pt-16 md:pt-24 lg:pb-22">
        <p class="label reveal md:col-span-3">Pricing</p>
        <div class="md:col-span-9">
          <h1 class="display-xl reveal">Never miss another lead.</h1>
          <p class="lede reveal mt-8 max-w-prose">Clear prices for small businesses in Cleveland, Northeast Ohio and beyond. Pick a package, or mix services from the list below. Either way, you get the scope and price in writing before any work starts.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container-site">
        <div class="hairline-grid lg:grid-cols-3">
{cards}
        </div>
        <p class="meta reveal mt-6">Monthly plans: 3-month minimum, then month to month. Setup: half to start, half at launch. Prices in USD.</p>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site grid-asym">
        <div class="md:col-span-4">
          <p class="label reveal">Individual services</p>
          <h2 class="display-md reveal mt-8">Starting prices.</h2>
          <p class="body reveal mt-6 max-w-sm">Final prices depend on scope. After a short call you get an exact quote in writing.</p>
        </div>
        <div class="space-y-14 md:col-span-7 md:col-start-6">
{menu}
        </div>
      </div>
    </section>

    <section id="faq" class="section scroll-mt-16 border-t border-line">
      <div class="container-site grid-asym">
        <div class="md:col-span-4">
          <p class="label reveal">Questions</p>
          <h2 class="display-md reveal mt-8">About pricing.</h2>
        </div>
        <div class="reveal border-t border-line md:col-span-7 md:col-start-6">
{faq}
        </div>
      </div>
    </section>
'''


OUT.write_text(build())
print(f'wrote {OUT}')
