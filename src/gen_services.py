"""Generates src/pages/services/*.html: the services hub and one page per service.

Each page carries its own JSON-LD (Service, FAQPage, BreadcrumbList) so search engines
and AI assistants can tie the service to Aydin, Mayfield Heights and the Cleveland area.
Run with python3 after editing the text below, then `npm run build`.
"""
import html, json, os, pathlib

OUT = pathlib.Path(__file__).resolve().parent / 'pages' / 'services'
SITE = 'https://aydinkalantar.com'

# Places served in person; shown on every page and listed in the structured data.
AREAS = ['Mayfield Heights', 'Cleveland', 'Lyndhurst', 'Beachwood', 'Highland Heights',
         'Pepper Pike', 'Mayfield Village', 'Euclid', 'Shaker Heights', 'Cleveland Heights']
AREA_LINE = ('Based in Mayfield Heights, Ohio. I meet clients in person across Cleveland and the east side, '
             'Lyndhurst, Beachwood, Highland Heights, Pepper Pike, Shaker Heights and Cleveland Heights, '
             'and work remotely with businesses anywhere in the United States.')

CASES = {
    'tbsp': ('The Best Screen Printing', 'E-commerce · SEO', 'Website rebuild for a Los Angeles print shop: online ordering, a voice agent, and 2,662 old URLs migrated with search traffic intact.'),
    'virtual-fashion': ('Virtual Fashion', 'AI apparel design', 'A browser studio that turns a garment idea into on-model photos and video in seconds.'),
    'catch-lead': ('Catch Lead', 'Conversational AI', 'An AI sales agent that answers website visitors by chat or voice, quotes and books appointments.'),
    'auto-alpha': ('Auto Alpha', 'Fintech · Dashboards', 'A dashboard that makes automated crypto strategies and their records easy to read.'),
}

STEPS = [
    ('A short call', 'You tell me about the business, the goal and the deadline. I ask questions until the problem is clear.'),
    ('A written plan', 'You get the scope, timeline and price in writing before any work starts.'),
    ('Design and build', 'I design and build it myself, sharing progress as I go, so nothing is lost between idea and launch.'),
    ('Launch and support', 'I launch it, check it in search and analytics, and stay on call for changes after.'),
]

SERVICES = [
    {
        'slug': 'web-design',
        'faq_heading': 'About websites.',
        'name': 'Web design & development',
        'short': 'Web design',
        'type': 'Web design and development',
        'title': 'Web Design & Development in Cleveland, Ohio · Aydin Kalantar',
        'desc': 'Custom website design and development for businesses in Cleveland and Northeast Ohio: fast, search-ready sites, online ordering and redesigns that keep your Google rankings.',
        'headline': 'Websites that bring in business, designed and built by one person.',
        'lede': 'I design and code custom websites for small and growing businesses: fast, easy to update, built to rank in Google and to turn visitors into calls, orders and bookings.',
        'card': 'Custom websites and online stores, designed and coded by hand, built to load fast and rank.',
        'for': ['Local service businesses that need more calls and booked jobs', 'Shops that want customers to order and pay online', 'Companies whose current site is slow, dated or hard to edit', 'Startups that need a product site and a working app'],
        'includes': ['Site plan, page structure and copy guidance', 'Custom design, desktop and mobile', 'Hand-written code on fast hosting (Cloudflare)', 'Online ordering, payments and booking', 'Redesigns and platform moves that keep your rankings, with every old URL redirected', 'Search setup on launch: Search Console, Bing, sitemaps and structured data'],
        'cases': ['tbsp', 'virtual-fashion', 'catch-lead'],
        'faq': [
            ('How much does a website cost?', 'It depends on the number of pages and features, such as online ordering or booking. After a short call you get the scope and price in writing, so you know what you are paying for before anything starts.'),
            ('Will I lose my Google rankings if I redesign my site?', 'Not if the move is planned. On The Best Screen Printing rebuild, every one of 2,662 old addresses was kept, redirected or retired on purpose, and the pages that were kept carry 96% of the clicks the old site earned.'),
            ('Can I edit the site myself?', 'Yes. I set the site up so the things you change often, like prices, products or photos, are easy to update, and I show you how.'),
            ('Do you work with businesses outside Cleveland?', 'Yes. I am based in Mayfield Heights and happy to meet locally, and I work remotely with clients anywhere in the United States.'),
            ('Do you use WordPress or templates?', 'I usually build custom, lightweight sites because they load faster and are more secure. If WordPress or Shopify is the right fit for your team, I work with those too.'),
        ],
    },
    {
        'slug': 'ai-agents',
        'faq_heading': 'About AI agents.',
        'name': 'AI chat & voice agents',
        'short': 'AI agents',
        'type': 'AI chatbot and voice agent development',
        'title': 'AI Chat & Voice Agents for Businesses · Aydin Kalantar, Cleveland',
        'desc': 'AI chat and voice agents for business websites: answer visitors 24/7, quote from your real prices, capture leads and book appointments. Built by Aydin Kalantar, creator of Catch Lead.',
        'headline': 'An assistant that answers every visitor, day and night.',
        'lede': 'I build AI agents that talk to your customers by chat or voice. They answer questions from your own prices and policies, collect contact details and book the appointment, then send the lead to you.',
        'card': 'Chat and voice assistants that answer customers 24/7, quote from your prices and book appointments.',
        'for': ['Service businesses that miss calls and after-hours inquiries', 'Shops that answer the same product questions every day', 'Teams that want leads qualified before they call back', 'Companies exploring AI tools for internal work'],
        'includes': ['An agent trained on your site, prices and policies', 'Chat and natural voice conversations', 'Lead capture with instant email or text alerts', 'Appointment booking and quote requests', 'A dashboard with every conversation and lead', 'Custom AI tools and automations for your workflow'],
        'cases': ['catch-lead', 'tbsp'],
        'faq': [
            ('What is an AI website agent?', 'It is an assistant on your website that answers visitors in plain language, by typing or by voice. Unlike a scripted chatbot, it understands questions in the visitor\'s own words and answers from your real information.'),
            ('Will it make things up?', 'It answers from the material you approve, such as your services, prices and policies. When it does not know, it says so and takes the visitor\'s details so you can follow up.'),
            ('Can I try one before buying?', 'Yes. The assistant in the corner of this page is Catch Lead, the product I built. Ask it anything about my work.'),
            ('Does it work with my current website?', 'Usually yes. It is added with one line of code and works on WordPress, Shopify, Wix, Squarespace and custom sites.'),
            ('Can it take orders by voice?', 'Yes. On The Best Screen Printing site, Max takes apparel orders by voice, remembers returning customers and asks for a rating at the end.'),
        ],
    },
    {
        'slug': 'seo',
        'faq_heading': 'About search.',
        'name': 'SEO, local SEO & AI search',
        'short': 'SEO',
        'type': 'Search engine optimization',
        'title': 'SEO, Local SEO & AI Search Optimization in Cleveland · Aydin Kalantar',
        'desc': 'SEO for Cleveland and Northeast Ohio businesses: technical SEO, local SEO and Google Business Profile, AI search visibility in ChatGPT and Google AI, plus Google Ads and Facebook Ads.',
        'headline': 'Get found on Google, on the map and in AI answers.',
        'lede': 'I help businesses show up when customers search: in Google results, in the local map pack, and in the answers ChatGPT, Google AI and Perplexity give. When you need results faster, I run Google Ads and Facebook Ads too.',
        'card': 'Technical and local SEO, AI search visibility, and Google and Facebook ads that bring in customers.',
        'for': ['Local businesses that want to appear in the Google map pack', 'Sites that lost traffic after a redesign or platform move', 'Companies that want to be named in ChatGPT and Google AI answers', 'Businesses ready to test paid ads with a clear budget'],
        'includes': ['Technical SEO audit and fixes: speed, indexing, structure', 'Local SEO: Google Business Profile, Bing Places, Apple Maps and citations', 'Structured data that tells search engines and AI who you are and what you do', 'AI search visibility: crawler access, llms.txt and pages written to be quoted', 'Safe site migrations with full redirect maps', 'Google Ads and Facebook Ads setup and management'],
        'cases': ['tbsp'],
        'faq': [
            ('What is local SEO?', 'Local SEO helps your business appear when people nearby search for what you do, such as "web designer near me", in the Google map pack and local results. Much of it rests on a complete Google Business Profile, consistent listings and reviews.'),
            ('What is AI search optimization?', 'More customers now ask ChatGPT, Google AI Overviews or Perplexity instead of searching. AI search optimization makes your site easy for those assistants to read, trust and quote: clear facts, structured data, crawler access and pages that answer real questions.'),
            ('How long does SEO take?', 'Technical fixes can show results within weeks. Rankings for competitive searches usually take a few months of steady work. Paid ads can bring traffic from the first day while SEO builds.'),
            ('Have you done SEO before?', 'Yes. From 2017 to 2020 I ran SEO, Google Ads and Facebook Ads for The Best Screen Printing and Signs Market in Los Angeles, and in 2026 I moved The Best Screen Printing to a new site with its search traffic intact.'),
            ('Do you manage Google Ads and Facebook Ads?', 'Yes. I set up campaigns, tracking and landing pages, and report on what each dollar brought in.'),
        ],
    },
    {
        'slug': 'branding',
        'faq_heading': 'About branding.',
        'name': 'Branding & graphic design',
        'short': 'Branding',
        'type': 'Branding and graphic design',
        'title': 'Branding, Logo & Graphic Design in Cleveland, Ohio · Aydin Kalantar',
        'desc': 'Logo design, brand identity and graphic design for businesses in Cleveland and Northeast Ohio: print, apparel, signage and ad creative, from a designer trained in fine art.',
        'headline': 'A brand that looks as good as the work you do.',
        'lede': 'I design logos, brand identities and the graphics that carry them: print, apparel, signs, social posts and ads. I trained as a painter and spent years in a print shop, so the designs are made to work on screen and in production.',
        'card': 'Logos, identities and graphics for print, apparel, signs, social and ads, ready for production.',
        'for': ['New businesses that need a name to look established', 'Companies whose logo no longer fits who they are', 'Brands that need apparel, signage or packaging graphics', 'Teams that need steady ad and social creative'],
        'includes': ['Logo and brand identity', 'Brand guidelines: colors, type and usage', 'Print design: cards, flyers, menus, brochures', 'Apparel and merch graphics, separated for screen printing', 'Signage and large-format graphics', 'Social media and ad creative'],
        'cases': ['tbsp', 'virtual-fashion'],
        'faq': [
            ('What do I get with a logo project?', 'Final logo files for print and screen, color and black-and-white versions, and a short guide to the colors and fonts so your brand stays consistent.'),
            ('Can you design for screen printing and embroidery?', 'Yes. I learned screen printing end to end and ran apparel decoration work, so artwork comes ready for production, with the right colors and separations.'),
            ('What is your design background?', 'I studied oil painting at the Azerbaijan Fine Art College, worked in my father\'s printing company in Baku, and from 2017 to 2020 led branding for The Best Screen Printing and Signs Market in Los Angeles.'),
            ('Can you also build the website?', 'Yes. Brand, website and marketing can come from one person, which keeps everything consistent.'),
        ],
    },
    {
        'slug': '3d-rendering',
        'faq_heading': 'About 3D work.',
        'name': '3D modeling & rendering',
        'short': '3D rendering',
        'type': '3D modeling and rendering',
        'title': '3D Modeling, Product Rendering & Animation · Aydin Kalantar, Cleveland',
        'desc': '3D modeling, photoreal product rendering and animation for products, apparel and ads, by Aydin Kalantar in Mayfield Heights, Ohio. CGI experience from film to AI product imagery.',
        'headline': 'Products shown at their best, before a photo is taken.',
        'lede': 'I model and render products, apparel and scenes in 3D: photoreal images for your store, mockups for pitches, and short animations for ads and launches. I started in CGI for film and today build AI tools for product imagery.',
        'card': 'Photoreal product renders, apparel mockups and short animations for stores, pitches and ads.',
        'for': ['Brands launching a product before samples exist', 'Online stores that need consistent product images', 'Apparel companies that need on-model mockups', 'Marketing teams that need motion for ads and social'],
        'includes': ['3D models of products and packaging', 'Photoreal renders on white or in scenes', 'Apparel mockups and on-model imagery', 'Short product animations and loops', 'AI-assisted image and video production'],
        'cases': ['virtual-fashion'],
        'faq': [
            ('What do you need to start a product render?', 'Photos, drawings or measurements of the product, plus logos and colors. A physical sample helps but is not required.'),
            ('Do you make product animations?', 'Yes. Short loops and launch videos for ads, social and product pages.'),
            ('What 3D experience do you have?', 'I began with 3D modeling, animation and rendering for film and television in Baku, including CGI for The Temple\'s Heart in 2005, and now build Virtual Fashion, an AI studio for apparel imagery.'),
            ('Can you produce on-model apparel images without a photo shoot?', 'Yes. Virtual Fashion, the studio I built, places garments with your design on consistent models and exports photos and video.'),
        ],
    },
]

ART = {
    'name': 'Marquetry commissions',
    'card': 'Original portraits, calligraphy and abstract pieces in natural wood veneer, cut and fitted by hand.',
    'url': '/art/commissions/',
}

HUB_FAQ = [
    ('Where are you based?', 'Mayfield Heights, Ohio, on the east side of Cleveland. I meet local clients in person and work remotely with businesses anywhere in the United States.'),
    ('What kinds of businesses do you work with?', 'Mostly small and growing businesses: local services, shops, manufacturers and startups. I have also built and run my own products, so I know the owner\'s side of the table.'),
    ('Can you handle the whole project?', 'Yes. Brand, website, AI agent, search and ads can all come from one person, so nothing gets lost between agencies.'),
    ('How do we start?', 'Email hello@aydinkalantar.com or call 216-339-8948 with a few lines about the business and what you need. I reply personally.'),
]

DETAIL = '''          <details class="group border-b border-line py-6">
            <summary class="flex cursor-pointer list-none items-baseline justify-between gap-6 font-heading text-lg font-bold tracking-tight text-ink transition-colors hover:text-accent [&::-webkit-details-marker]:hidden">{q}<span aria-hidden="true" class="meta transition-transform duration-400 group-open:rotate-45">+</span></summary>
            <p class="body mt-4 max-w-prose">{a}</p>
          </details>'''

e = html.escape


def faq_section(faq, heading):
    items = '\n'.join(DETAIL.format(q=e(q), a=e(a)) for q, a in faq)
    return f'''    <section id="faq" class="section scroll-mt-16 border-t border-line">
      <div class="container-site grid-asym">
        <div class="md:col-span-4">
          <p class="label reveal">Questions</p>
          <h2 class="display-md reveal mt-8">{heading}</h2>
        </div>
        <div class="reveal border-t border-line md:col-span-7 md:col-start-6">
{items}
        </div>
      </div>
    </section>'''


def steps_section():
    items = '\n'.join(f'''          <li class="reveal border-t border-line pt-6">
            <span class="meta">0{i}</span>
            <h3 class="mt-4 text-xl">{e(t)}</h3>
            <p class="body mt-3">{e(d)}</p>
          </li>''' for i, (t, d) in enumerate(STEPS, 1))
    return f'''    <section class="section border-t border-line">
      <div class="container-site">
        <p class="label reveal">How we work together</p>
        <ol class="mt-12 grid gap-10 sm:grid-cols-2 lg:grid-cols-4 lg:gap-6">
{items}
        </ol>
      </div>
    </section>'''


def area_section():
    return f'''    <section class="section border-t border-line">
      <div class="container-site grid-asym">
        <p class="label reveal md:col-span-3">Service area</p>
        <div class="md:col-span-9">
          <h2 class="display-md reveal">Local to Cleveland, working everywhere.</h2>
          <p class="lede reveal mt-6 max-w-prose">{e(AREA_LINE)}</p>
        </div>
      </div>
    </section>'''


def jsonld(graph):
    data = json.dumps({'@context': 'https://schema.org', '@graph': graph}, indent=2, ensure_ascii=False)
    return f'    <script type="application/ld+json">\n{data}\n    </script>'


def faq_ld(faq):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}


def crumbs_ld(items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items, 1)]}


AREA_LD = [{'@type': 'City', 'name': f'{a}, Ohio'} for a in AREAS] + [{'@type': 'Country', 'name': 'United States'}]


def meta(title, desc, contact):
    return '<!-- ' + json.dumps({'title': title, 'description': desc, 'nav': 'services', 'contact': contact}) + ' -->'


def mailto(subject):
    return 'mailto:hello@aydinkalantar.com?subject=' + subject.replace(' ', '%20').replace('&', '%26')


def page(s):
    url = f"/services/{s['slug']}/"
    cta = mailto(s['name'] + ' project')
    for_items = '\n'.join(f'            <li>{e(x)}</li>' for x in s['for'])
    inc_items = '\n'.join(f'            <li>{e(x)}</li>' for x in s['includes'])
    cards = '\n'.join(f'''          <a href="/case-studies/{c}/" class="card group reveal">
            <span class="tag self-start">{e(CASES[c][1])}</span>
            <h3 class="card-title mt-10">{e(CASES[c][0])}</h3>
            <p class="body mb-10 mt-4">{e(CASES[c][2])}</p>
            <span class="meta mt-auto flex items-center justify-between border-t border-line pt-5 group-hover:text-accent"><span>Read case study</span><span class="arrow">→</span></span>
          </a>''' for c in s['cases'])
    others = '\n'.join(f'            <li><a class="link" href="/services/{o["slug"]}/">{e(o["name"])}</a></li>' for o in SERVICES if o is not s)
    ld = jsonld([
        {'@type': 'Service', '@id': SITE + url + '#service', 'name': s['name'], 'serviceType': s['type'],
         'description': s['desc'], 'url': SITE + url,
         'provider': {'@id': SITE + '/#business'}, 'areaServed': AREA_LD},
        faq_ld(s['faq']),
        crumbs_ld([('Home', '/'), ('Services', '/services/'), (s['name'], url)]),
    ])
    return f'''{meta(s['title'], s['desc'], 'Tell me about your project.')}
{ld}
    <section class="relative border-b border-line">
      <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
      <div class="container-site relative pb-18 pt-12 md:pt-20 lg:pb-22">
        <nav aria-label="Breadcrumb" class="meta reveal"><a class="transition-colors hover:text-accent" href="/services/">Services</a> <span class="text-ink-faint">/</span> {e(s['short'])}</nav>
        <div class="grid-asym mt-12 items-end">
          <div class="md:col-span-8">
            <p class="label reveal">{e(s['name'])} · Cleveland, Ohio</p>
            <h1 class="display-lg reveal mt-6">{e(s['headline'])}</h1>
            <p class="lede reveal mt-8 max-w-prose">{e(s['lede'])}</p>
          </div>
          <div class="reveal flex flex-col gap-3 md:col-span-4 md:col-start-9 lg:col-span-3 lg:col-start-10">
            <a href="{cta}" class="btn-primary group">Start a project <span aria-hidden="true" class="arrow">↗</span></a>
            <a href="tel:+12163398948" class="btn-secondary">Call 216-339-8948</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container-site grid-asym">
        <div class="md:col-span-5">
          <p class="label reveal">Who it's for</p>
          <ul class="prose-case reveal mt-8">
{for_items}
          </ul>
        </div>
        <div class="md:col-span-6 md:col-start-7">
          <p class="label reveal">What's included</p>
          <ul class="prose-case reveal mt-8">
{inc_items}
          </ul>
        </div>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site">
        <div class="grid-asym">
          <p class="label reveal md:col-span-3">Proof</p>
          <h2 class="display-md reveal md:col-span-9">Work that is live today.</h2>
        </div>
        <div class="hairline-grid mt-14 md:grid-cols-{min(len(s['cases']), 3)}">
{cards}
        </div>
      </div>
    </section>

{steps_section()}

{faq_section(s['faq'], s['faq_heading'])}

{area_section()}

    <nav aria-label="Other services" class="border-t border-line">
      <div class="container-site grid-asym py-16 lg:py-22">
        <p class="label md:col-span-3">Other services</p>
        <ul class="flex flex-wrap gap-x-8 gap-y-3 md:col-span-9">
{others}
            <li><a class="link" href="{ART['url']}">{ART['name']}</a></li>
        </ul>
      </div>
    </nav>
'''


def hub():
    rows = SERVICES + [{'slug': None, 'name': ART['name'], 'card': ART['card'], 'url': ART['url']}]
    cards = '\n'.join(f'''          <a href="{r.get('url') or f"/services/{r['slug']}/"}" class="card group reveal">
            <span class="meta">0{i}</span>
            <h2 class="card-title mt-10">{e(r['name'])}</h2>
            <p class="body mb-10 mt-4">{e(r['card'])}</p>
            <span class="meta mt-auto flex items-center justify-between border-t border-line pt-5 group-hover:text-accent"><span>Learn more</span><span class="arrow">→</span></span>
          </a>''' for i, r in enumerate(rows, 1))
    title = 'Services · Web Design, AI Agents, SEO & Branding in Cleveland · Aydin Kalantar'
    desc = 'Web design and development, AI chat and voice agents, SEO and local SEO, branding and 3D rendering for businesses in Cleveland, Mayfield Heights and Northeast Ohio, from Aydin Kalantar.'
    ld = jsonld([
        {'@type': 'OfferCatalog', '@id': SITE + '/services/#catalog', 'name': 'Services by Aydin Kalantar',
         'itemListElement': [{'@type': 'Offer', 'itemOffered': {'@id': f"{SITE}/services/{s['slug']}/#service"}} for s in SERVICES]},
        faq_ld(HUB_FAQ),
        crumbs_ld([('Home', '/'), ('Services', '/services/')]),
    ])
    return f'''{meta(title, desc, 'Tell me what you need.')}
{ld}
    <section class="relative border-b border-line">
      <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
      <div class="container-site grid-asym relative pb-18 pt-16 md:pt-24 lg:pb-22">
        <p class="label reveal md:col-span-3">Services</p>
        <div class="md:col-span-9">
          <h1 class="display-xl reveal">Design, code and growth for your business.</h1>
          <p class="lede reveal mt-8 max-w-prose">I help businesses in Cleveland and across the country get found, look the part and turn visitors into customers. One person from brand to website to AI agent to search, so nothing gets lost in a handoff.</p>
          <div class="reveal mt-12 flex flex-col gap-3 sm:flex-row">
            <a href="{mailto('New project')}" class="btn-primary group">Start a project <span aria-hidden="true" class="arrow">↗</span></a>
            <a href="tel:+12163398948" class="btn-secondary">Call 216-339-8948</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container-site">
        <div class="hairline-grid md:grid-cols-2 lg:grid-cols-3">
{cards}
        </div>
      </div>
    </section>

{steps_section()}

{faq_section(HUB_FAQ, 'Before we talk.')}

{area_section()}
'''


os.makedirs(OUT, exist_ok=True)
(OUT / 'index.html').write_text(hub())
print('wrote services/index')
for s in SERVICES:
    (OUT / f"{s['slug']}.html").write_text(page(s))
    print('wrote services/' + s['slug'])
