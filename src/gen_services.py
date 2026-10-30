"""Generates src/pages/services/*.html and src/pages/industries/*.html: hubs and one page per service or industry.

Each page carries its own JSON-LD (Service, FAQPage, BreadcrumbList) so search engines
and AI assistants can tie the service to Aydin. Services that sell locally ('local': True) name
Cleveland; the rest are pitched to the whole United States.
Run with python3 after editing the text below, then `npm run build`.
"""
import html, json, os, pathlib

OUT = pathlib.Path(__file__).resolve().parent / 'pages' / 'services'
SITE = 'https://aydinkalantar.com'

# Places served in person; shown on every page and listed in the structured data.
AREAS = ['Mayfield Heights', 'Cleveland', 'Lyndhurst', 'Beachwood', 'Highland Heights',
         'Pepper Pike', 'Mayfield Village', 'Euclid', 'Shaker Heights', 'Cleveland Heights']
AREA_LINE = ('I work remotely with businesses across the United States. I am based in Mayfield Heights, Ohio, '
             'near Cleveland, and meet Cleveland-area clients in person. I also have deep roots in Los Angeles, '
             'where I built brands and websites for local companies from 2017 to 2020 and still work with clients today.')

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
        'slug': 'ui-ux-design',
        'faq_heading': 'About UI & UX.',
        'name': 'UI & UX design',
        'short': 'UI & UX',
        'type': 'UI design and UX design',
        'title': 'UI & UX Design for Apps, SaaS & Websites · Aydin Kalantar, UI/UX Designer',
        'desc': 'UI and UX design for SaaS products, web and mobile apps and websites: user research, flows, wireframes, prototypes, interface design and design systems for businesses across the US, by Aydin Kalantar.',
        'headline': 'Interfaces people understand the first time they use them.',
        'lede': 'I am a UI and UX specialist. I design how a product works and how it looks: the flows, the screens, every state and detail, so customers find what they need, trust what they see and finish what they started. And because I also write the code, the design ships the way it was drawn.',
        'card': 'User flows, wireframes, prototypes, interfaces and design systems for apps, SaaS and websites.',
        'for': ['Startups that need a product designed before it is built', 'SaaS and apps where users get lost, stall or cancel', 'Teams with developers but no designer', 'Businesses whose site looks dated or converts poorly'],
        'includes': ['UX audit of your current product or site', 'User research, journeys and user flows', 'Wireframes and clickable prototypes', 'UI design for web, mobile and dashboards', 'Design systems: components, type, color and states', 'Developer-ready files, or I build it myself'],
        'cases': ['virtual-fashion', 'catch-lead', 'auto-alpha'],
        'faq': [
            ('What is the difference between UI and UX design?', 'UX design is how a product works: what a user needs, the steps they take and where they get stuck. UI design is how it looks and feels on screen: layout, type, color and every button state. I do both, and they work best together.'),
            ('Can you hand designs to my developers?', 'Yes. I hand over organized design files with every screen, state and spacing rule, or I build the interface myself so nothing is lost between design and code.'),
            ('Can you improve an app or site that already exists?', 'Yes. A UX audit finds where users stall or leave, then I redesign those screens first, so you see results without a full rebuild.'),
            ('What have you designed?', 'Virtual Fashion, Catch Lead and Auto Alpha: an AI design studio, a chat and voice sales agent with an owner dashboard, and a trading dashboard built to make complex data easy to read. All three are live.'),
            ('Do you also design for mobile?', 'Yes. Every design covers phone, tablet and desktop, and the apps I build install on mobile.'),
        ],
    },
    {
        'slug': 'web-design',
        'faq_heading': 'About websites.',
        'name': 'Web design & development',
        'short': 'Web design',
        'type': 'Web design and development',
        'title': 'Web Design & Development in Cleveland, Ohio · Aydin Kalantar',
        'local': True,
        'desc': 'Custom website design and development for businesses in Cleveland, Northeast Ohio and across the US: fast, search-ready sites, online ordering and redesigns that keep your Google rankings.',
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
        'slug': 'app-development',
        'faq_heading': 'About apps.',
        'name': 'SaaS, web & mobile apps',
        'short': 'Apps',
        'type': 'Custom software, SaaS, web app and mobile app development',
        'title': 'SaaS, Web App & Mobile App Development · Aydin Kalantar',
        'desc': 'Custom SaaS, web app and mobile app development from scratch for startups and businesses across the United States: product design, code, payments, dashboards and launch.',
        'headline': 'Your app, from first sketch to paying users.',
        'lede': 'I design and build software products from scratch: SaaS platforms, web apps, mobile apps and internal tools. One person handles the product thinking, the interface and the code, so the idea survives all the way to launch.',
        'card': 'SaaS platforms, web and mobile apps and internal tools, designed and built from scratch.',
        'for': ['Founders with an idea who need a working product, not just designs', 'Businesses that want their own customer portal or app', 'Teams outgrowing spreadsheets that need an internal tool', 'Companies with an existing app that needs a redesign or new features'],
        'includes': ['Product planning: features, users and a first version you can launch', 'UX and interface design for web and mobile', 'Front end, back end, database and APIs', 'Accounts, subscriptions and payments', 'Dashboards, admin panels and reporting', 'AI features built in: generation, chat, search and recommendations', 'Hosting, launch and ongoing improvements'],
        'cases': ['virtual-fashion', 'catch-lead', 'auto-alpha'],
        'faq': [
            ('Can you build an app from scratch?', 'Yes. Virtual Fashion, Catch Lead and Auto Alpha are SaaS products I designed and built from the first sketch to live, paying-ready software. Each is online today.'),
            ('Do you build mobile apps?', 'Yes. I build mobile apps and installable web apps that work on phones, tablets and desktop. Virtual Fashion and Catch Lead both run as installable apps on mobile.'),
            ('How long does it take to build a first version?', 'It depends on the features. Most products start with a focused first version that real users can try, then grow from what they do. You get the scope, timeline and price in writing before work starts.'),
            ('Will I own the code?', 'Yes. The code, designs and accounts are yours.'),
            ('Can you add AI to my product?', 'Yes. All three of my products use AI: image and video generation in Virtual Fashion, chat and voice in Catch Lead, and strategy automation in Auto Alpha.'),
        ],
    },
    {
        'slug': 'automation',
        'faq_heading': 'About automation.',
        'name': 'Business automation',
        'short': 'Automation',
        'type': 'Business process automation and AI workflow automation',
        'title': 'Business Automation & AI Workflow Solutions · Aydin Kalantar',
        'desc': 'Business process automation for companies across the United States: connect your tools, automate quotes, orders, follow-ups and reports, and add AI where it saves hours every week.',
        'headline': 'Stop doing by hand what software can do for you.',
        'lede': 'I find the repetitive work in your business, like copying data between tools, chasing leads, building quotes or sending reports, and automate it. Smart solutions that save hours every week and cut mistakes.',
        'card': 'Connect your tools and automate quotes, orders, follow-ups and reports, with AI where it helps.',
        'for': ['Owners spending evenings on admin and data entry', 'Teams that copy information between apps by hand', 'Businesses that lose leads because follow-up is slow', 'Companies that want to use AI but do not know where to start'],
        'includes': ['A review of where your time goes and what to automate first', 'Connecting your apps: CRM, email, forms, spreadsheets, payments', 'Automatic lead follow-up, quotes and booking', 'Order, invoice and inventory workflows', 'Automatic reports and dashboards', 'AI that reads, sorts and drafts: emails, documents and requests'],
        'cases': ['catch-lead', 'tbsp', 'auto-alpha'],
        'faq': [
            ('What can be automated in a small business?', 'Usually more than people expect: replying to new leads, sending quotes, booking appointments, moving orders between systems, invoicing, reminders and weekly reports. We start with the task that costs you the most time.'),
            ('Do I have to change the software I use?', 'Usually not. Most automation connects the tools you already have so they share information without anyone copying it by hand.'),
            ('Where does AI fit in?', 'AI handles the work that needs reading or writing: answering customer questions, sorting incoming requests, pulling details from documents and drafting replies for you to approve.'),
            ('Have you built automation before?', 'Yes. Catch Lead automates lead capture, quoting and booking for service businesses, and Auto Alpha runs trading strategies automatically on users\' own exchange accounts.'),
        ],
    },
    {
        'slug': 'ai-agents',
        'faq_heading': 'About AI agents.',
        'name': 'AI chat & voice agents',
        'short': 'AI agents',
        'type': 'AI chatbot and voice agent development',
        'title': 'AI Chat & Voice Agents for Businesses · Aydin Kalantar',
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
        'local': True,
        'desc': 'SEO for businesses in Cleveland, Northeast Ohio and across the US: technical SEO, local SEO and Google Business Profile, AI search visibility in ChatGPT and Google AI, plus Google Ads and Facebook Ads.',
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
        'local': True,
        'desc': 'Logo design, brand identity and graphic design for businesses in Cleveland, Northeast Ohio and across the US: print, apparel, signage and ad creative, from a designer trained in fine art.',
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
        'title': '3D Modeling, Product Rendering & Animation · Aydin Kalantar',
        'desc': '3D modeling, photoreal product rendering and animation for products, apparel and ads, by Aydin Kalantar, for brands across the US. CGI experience from film to AI product imagery.',
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
    ('Do you work with clients outside Ohio?', 'Yes, most of my work is remote, with businesses anywhere in the United States. I am based in Mayfield Heights, near Cleveland, and have worked with Los Angeles companies since 2017.'),
    ('What kinds of businesses do you work with?', 'Mostly small and growing businesses: local services, shops, manufacturers and startups. I have also built and run my own products, so I know the owner\'s side of the table.'),
    ('Can you handle the whole project?', 'Yes. Brand, website, app, automation, AI, search and ads can all come from one person, so nothing gets lost between agencies.'),
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
          <h2 class="display-md reveal">Nationwide, from Cleveland.</h2>
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


NATIONAL_LD = [{'@type': 'Country', 'name': 'United States'}, {'@type': 'City', 'name': 'Cleveland, Ohio'}, {'@type': 'City', 'name': 'Los Angeles, California'}]
LOCAL_LD = NATIONAL_LD + [{'@type': 'City', 'name': f'{a}, Ohio'} for a in AREAS if a != 'Cleveland']


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
         'provider': {'@id': SITE + '/#business'}, 'areaServed': LOCAL_LD if s.get('local') else NATIONAL_LD},
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
            <p class="label reveal">{e(s['name'])} · {'Cleveland, Ohio + nationwide' if s.get('local') else 'Nationwide, remote'}</p>
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
    title = 'Services · UI/UX Design, Web & App Development, AI & SEO · Aydin Kalantar'
    desc = 'UI and UX design, web design, SaaS, web and mobile app development, business automation, AI agents, SEO and local SEO, branding and 3D rendering for businesses across the United States, from Aydin Kalantar, based in Cleveland, Ohio.'
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
          <p class="lede reveal mt-8 max-w-prose">I help businesses across the United States get found, look the part and turn visitors into customers. One person from UX and brand to website, app, automation and search, so nothing gets lost in a handoff.</p>
          <div class="reveal mt-12 flex flex-col gap-3 sm:flex-row">
            <a href="{mailto('New project')}" class="btn-primary group">Start a project <span aria-hidden="true" class="arrow">↗</span></a>
            <a href="tel:+12163398948" class="btn-secondary">Call 216-339-8948</a>
          </div>
          <p class="reveal mt-8"><a class="link" href="/industries/">See how I help your industry</a></p>
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


# Industry pages: /industries/<slug>/. Only industries with real proof behind them, each with its own
# problems and answers, so no page is a copy of another with a word swapped.
IND_OUT = OUT.parent / 'industries'
SVC = {s['slug']: s for s in SERVICES}

INDUSTRIES = [
    {
        'slug': 'print-and-apparel',
        'name': 'Print shops & apparel brands',
        'title': 'Websites, AI Agents & Mockups for Print Shops and Apparel Brands · Aydin Kalantar',
        'desc': 'Websites with online ordering, AI order-taking agents, product mockups and SEO for screen printers, embroidery shops, sign shops and apparel brands across the US.',
        'headline': 'For print shops that want orders, not just quote requests.',
        'lede': 'I learned screen printing end to end, ran an apparel decoration business, and did the branding, websites and ads for a Los Angeles print shop and a sign company. I know how your customers buy, and where they give up.',
        'card': 'Online ordering with design placement, an agent that takes orders, mockups and SEO.',
        'problems': [
            ('Customers ask for quotes instead of ordering', 'A catalog of real products where customers place their design, see the price and pay online, as on The Best Screen Printing.'),
            ('The phone rings with the same questions all day', 'A voice and chat agent that answers sizing, pricing and turnaround questions and takes the order details.'),
            ('Mockups and product photos slow every job', 'On-model photos and video of your blanks with the customer\'s design, made in minutes instead of a shoot.'),
            ('A new website would wipe out your Google traffic', 'A redirect plan for every old page. The Best Screen Printing moved 2,662 URLs and kept 96% of its clicks.'),
        ],
        'services': ['web-design', 'ai-agents', '3d-rendering', 'seo', 'branding'],
        'cases': ['tbsp', 'virtual-fashion'],
        'faq': [
            ('Have you worked in the print industry?', 'Yes. I took a screen printing course, ran an apparel decoration business, and from 2017 to 2020 handled branding, web, SEO and ads for The Best Screen Printing and Signs Market in Los Angeles. In 2026 I rebuilt The Best Screen Printing\'s website.'),
            ('Can customers upload a design and order online?', 'Yes. Customers choose a product, place their artwork, pick sizes and colors, and check out, with pricing that follows your real rules.'),
            ('Can you make mockups without physical samples?', 'Yes. Virtual Fashion, the studio I built, places a design on garments and consistent models and exports photos and video.'),
        ],
    },
    {
        'slug': 'fashion-and-ecommerce',
        'name': 'Fashion brands & online stores',
        'title': 'UX, E-commerce & AI Product Imagery for Fashion Brands · Aydin Kalantar',
        'desc': 'UI/UX, online store design and development, and AI product photos and video for fashion brands and e-commerce businesses across the US.',
        'headline': 'Product pages and imagery that sell the garment.',
        'lede': 'I build the store, design the shopping experience and make the product imagery. Virtual Fashion, my AI apparel studio, came from the same problem every brand has: great product, slow and costly photos.',
        'card': 'Store design, product imagery without shoots, and UX that turns browsing into buying.',
        'problems': [
            ('Every new product needs a photo shoot', 'Studio-quality on-model photos and short videos generated from the garment, with consistent models across the catalog.'),
            ('Visitors browse but do not buy', 'A UX review of the product page and checkout, then a redesign of the screens where shoppers drop off.'),
            ('The store is slow on phones', 'A fast, mobile-first build, with images and code tuned so pages load in a blink.'),
            ('Launches need content you do not have time to make', 'Lookbook videos, product loops and ad creative made with the same tools.'),
        ],
        'services': ['ui-ux-design', 'web-design', '3d-rendering', 'app-development', 'branding'],
        'cases': ['virtual-fashion', 'tbsp'],
        'faq': [
            ('Can you improve the store I already have?', 'Yes. I can redesign the screens that lose shoppers on your current store, or build a custom store when the brand needs something the platform cannot do.'),
            ('Are AI product photos realistic enough to sell with?', 'Virtual Fashion is built for exactly that: consistent models, real garment shapes and 4K export. See the case study for examples.'),
            ('Can you keep my brand look consistent?', 'Yes. I set up the models, scenes and style once, so every new product matches the rest of the catalog.'),
        ],
    },
    {
        'slug': 'home-services',
        'name': 'Home & local services',
        'title': 'AI Answering, Websites & Local SEO for Home Service Businesses · Aydin Kalantar',
        'desc': 'AI chat and voice agents that answer missed calls and book jobs, websites and local SEO for contractors, HVAC, plumbers, cleaners, movers and other home service businesses across the US.',
        'headline': 'Every missed call is a job someone else gets.',
        'lede': 'Contractors, cleaners, movers and repair companies lose work while they are on a job. I built Catch Lead so a business never misses an inquiry, and I have run a moving company myself, so I know the owner\'s side of the phone.',
        'card': 'Answer every call and inquiry, quote fast, book jobs and show up in local search.',
        'problems': [
            ('Calls come in while you are on a job', 'An AI agent answers by voice or chat, quotes from your real prices and books the appointment on your calendar.'),
            ('Quotes take days to send', 'Automatic quotes for standard jobs, and a clean summary of every other request so you can price it in minutes.'),
            ('You do not show up in "near me" searches', 'A complete Google Business Profile, consistent listings, service-area pages and a review routine.'),
            ('Happy customers never leave reviews', 'An automatic review request after every finished job.'),
        ],
        'services': ['ai-agents', 'automation', 'seo', 'web-design'],
        'cases': ['catch-lead', 'tbsp'],
        'faq': [
            ('Will an AI agent sound like a robot to my customers?', 'Catch Lead speaks naturally and answers in plain language. Try it: the assistant in the corner of this page is Catch Lead.'),
            ('What happens with jobs it cannot price?', 'It collects the details, photos and contact information, and sends you a ready-to-call lead.'),
            ('Do you understand service businesses?', 'Yes. Before I built software I started and ran a relocation company, so I have been the owner answering the phone between jobs.'),
        ],
    },
    {
        'slug': 'law-firms',
        'name': 'Law firms & professional services',
        'title': 'AI Intake Agents, Websites & SEO for Law Firms · Aydin Kalantar',
        'desc': 'AI intake agents that answer after hours and book consultations, trustworthy website design and local SEO for law firms, accountants and other professional service firms across the US.',
        'headline': 'Turn the 9 p.m. visitor into tomorrow\'s consultation.',
        'lede': 'People look for a lawyer or an accountant when something goes wrong, often at night. I build intake that answers right away, websites that earn trust in seconds, and search visibility that brings the right cases to you.',
        'card': 'After-hours intake that books consultations, a site that earns trust, and local SEO.',
        'problems': [
            ('After-hours inquiries go to voicemail', 'An AI intake agent answers by chat or voice, collects the case details and books a consultation.'),
            ('The website does not build trust', 'A clear, modern design that explains what you do, who you help and what happens next.'),
            ('Intake forms are retyped by hand', 'Automation that moves intake details into your case management tools and sends confirmations.'),
            ('Clients cannot find you locally', 'Local SEO, practice-area pages and structured data that search engines and AI assistants can read.'),
        ],
        'services': ['ai-agents', 'ui-ux-design', 'web-design', 'automation', 'seo'],
        'cases': ['catch-lead'],
        'faq': [
            ('Will the AI give legal advice?', 'No. It is set up to answer only from the information you approve, such as practice areas, fees and next steps, then collect details and book a consultation.'),
            ('Can it screen out cases we do not take?', 'Yes. It asks your qualifying questions and routes or politely declines inquiries outside your practice areas.'),
            ('Is there an example?', 'The Catch Lead case study includes a short film of a law firm website visitor at night becoming a qualified lead.'),
        ],
    },
    {
        'slug': 'startups-and-saas',
        'name': 'Startups & SaaS founders',
        'title': 'Product Design & MVP Development for Startups and SaaS Founders · Aydin Kalantar',
        'desc': 'UI/UX design and full-stack development for startups and SaaS founders across the US: from idea to a launched MVP, with AI features, payments and dashboards.',
        'headline': 'From idea to a product people pay for.',
        'lede': 'I have taken three products of my own from sketch to live software: Virtual Fashion, Catch Lead and Auto Alpha. I design the experience and write the code, so founders get one partner instead of a designer, an agency and a hand-off gap.',
        'card': 'UX, design and code for your first version, built by someone who has shipped three.',
        'problems': [
            ('You have the idea but no product', 'A focused first version: the core flow designed, built and launched so real users can try it.'),
            ('Designs that developers cannot build', 'Design and code from the same person, so what ships matches what was designed.'),
            ('Users sign up and disappear', 'A UX audit of onboarding and the first session, then redesigned screens that get users to value faster.'),
            ('You need AI in the product', 'Generation, chat, voice and automation features built in, as in all three of my products.'),
        ],
        'services': ['ui-ux-design', 'app-development', 'web-design', 'ai-agents', 'branding'],
        'cases': ['virtual-fashion', 'catch-lead', 'auto-alpha'],
        'faq': [
            ('Can you build our MVP?', 'Yes. I plan the first version with you, design it and build it, including accounts, payments and an admin panel.'),
            ('Do you work with existing teams?', 'Yes. I can lead design for your developers, or join as the designer who also codes.'),
            ('Will we own everything?', 'Yes. Code, designs and accounts are yours.'),
        ],
    },
    {
        'slug': 'fintech',
        'name': 'Fintech & data products',
        'title': 'UI/UX Design & Development for Fintech and Data Dashboards · Aydin Kalantar',
        'desc': 'UI/UX design and development of fintech products and data dashboards across the US: complex numbers made clear, trust built into every screen, automation underneath.',
        'headline': 'Complex numbers, made clear enough to trust.',
        'lede': 'Money products live or die on trust. I designed and built Auto Alpha, where users run automated crypto strategies on their own exchange accounts, so every screen had to explain risk, performance and control at a glance.',
        'card': 'Dashboards and fintech flows that make complex data clear and earn users\' trust.',
        'problems': [
            ('Users do not understand the numbers', 'Dashboards that show performance, history and risk in a form people read at a glance.'),
            ('Users do not trust where their money goes', 'Flows that state plainly who holds the funds, what the product can and cannot do, and how to stop it.'),
            ('Onboarding loses people at the hard steps', 'Guided setup for steps like connecting accounts and API keys, with clear checks at each stage.'),
            ('Manual work behind the scenes', 'Automation that runs strategies, reports and alerts without anyone babysitting it.'),
        ],
        'services': ['ui-ux-design', 'app-development', 'automation'],
        'cases': ['auto-alpha'],
        'faq': [
            ('Have you built a fintech product?', 'Yes. Auto Alpha runs rule-based crypto strategies on users\' own exchange accounts, with funds that never leave the exchange.'),
            ('Can you design dashboards for complex data?', 'Yes. That was the core of Auto Alpha: backtests and live records presented so they read clearly at a glance.'),
            ('Do you build the back end too?', 'Yes. I build the data, automation and integrations behind the interface.'),
        ],
    },
]


def ind_page(i):
    url = f"/industries/{i['slug']}/"
    probs = '\n'.join(f'''          <div class="card reveal">
            <h3 class="text-xl">{e(p)}</h3>
            <p class="body mt-4">{e(a)}</p>
          </div>''' for p, a in i['problems'])
    svcs = '\n'.join(f'            <li><a class="link" href="/services/{s}/">{e(SVC[s]["name"])}</a></li>' for s in i['services'])
    cards = '\n'.join(f'''          <a href="/case-studies/{c}/" class="card group reveal">
            <span class="tag self-start">{e(CASES[c][1])}</span>
            <h3 class="card-title mt-10">{e(CASES[c][0])}</h3>
            <p class="body mb-10 mt-4">{e(CASES[c][2])}</p>
            <span class="meta mt-auto flex items-center justify-between border-t border-line pt-5 group-hover:text-accent"><span>Read case study</span><span class="arrow">→</span></span>
          </a>''' for c in i['cases'])
    others = '\n'.join(f'            <li><a class="link" href="/industries/{o["slug"]}/">{e(o["name"])}</a></li>' for o in INDUSTRIES if o is not i)
    ld = jsonld([
        {'@type': 'Service', '@id': SITE + url + '#service', 'name': f"Design, development and AI for {i['name'].lower()}",
         'description': i['desc'], 'url': SITE + url, 'provider': {'@id': SITE + '/#business'},
         'audience': {'@type': 'BusinessAudience', 'name': i['name']}, 'areaServed': NATIONAL_LD},
        faq_ld(i['faq']),
        crumbs_ld([('Home', '/'), ('Industries', '/industries/'), (i['name'], url)]),
    ])
    return f'''{meta(i['title'], i['desc'], 'Tell me about your business.').replace('"nav": "services"', '"nav": "industries"')}
{ld}
    <section class="relative border-b border-line">
      <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
      <div class="container-site relative pb-18 pt-12 md:pt-20 lg:pb-22">
        <nav aria-label="Breadcrumb" class="meta reveal"><a class="transition-colors hover:text-accent" href="/industries/">Industries</a> <span class="text-ink-faint">/</span> {e(i['name'])}</nav>
        <div class="grid-asym mt-12 items-end">
          <div class="md:col-span-8">
            <p class="label reveal">{e(i['name'])} · Nationwide</p>
            <h1 class="display-lg reveal mt-6">{e(i['headline'])}</h1>
            <p class="lede reveal mt-8 max-w-prose">{e(i['lede'])}</p>
          </div>
          <div class="reveal flex flex-col gap-3 md:col-span-4 md:col-start-9 lg:col-span-3 lg:col-start-10">
            <a href="{mailto(i['name'] + ' project')}" class="btn-primary group">Start a project <span aria-hidden="true" class="arrow">↗</span></a>
            <a href="tel:+12163398948" class="btn-secondary">Call 216-339-8948</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container-site">
        <div class="grid-asym">
          <p class="label reveal md:col-span-3">Problems I solve</p>
          <h2 class="display-md reveal md:col-span-9">What gets in the way, and what fixes it.</h2>
        </div>
        <div class="hairline-grid mt-14 md:grid-cols-2">
{probs}
        </div>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site grid-asym">
        <p class="label reveal md:col-span-3">Services that fit</p>
        <ul class="reveal flex flex-wrap gap-x-8 gap-y-3 md:col-span-9">
{svcs}
        </ul>
      </div>
    </section>

    <section class="section border-t border-line">
      <div class="container-site">
        <div class="grid-asym">
          <p class="label reveal md:col-span-3">Proof</p>
          <h2 class="display-md reveal md:col-span-9">Work that is live today.</h2>
        </div>
        <div class="hairline-grid mt-14 md:grid-cols-{min(len(i['cases']), 3)}">
{cards}
        </div>
      </div>
    </section>

{faq_section(i['faq'], 'Common questions.')}

{area_section()}

    <nav aria-label="Other industries" class="border-t border-line">
      <div class="container-site grid-asym py-16 lg:py-22">
        <p class="label md:col-span-3">Other industries</p>
        <ul class="flex flex-wrap gap-x-8 gap-y-3 md:col-span-9">
{others}
        </ul>
      </div>
    </nav>
'''


def ind_hub():
    cards = '\n'.join(f'''          <a href="/industries/{i['slug']}/" class="card group reveal">
            <span class="meta">0{n}</span>
            <h2 class="card-title mt-10">{e(i['name'])}</h2>
            <p class="body mb-10 mt-4">{e(i['card'])}</p>
            <span class="meta mt-auto flex items-center justify-between border-t border-line pt-5 group-hover:text-accent"><span>Learn more</span><span class="arrow">→</span></span>
          </a>''' for n, i in enumerate(INDUSTRIES, 1))
    title = 'Industries · Design, Apps, AI & SEO by Industry · Aydin Kalantar'
    desc = 'How Aydin Kalantar helps print shops, fashion brands, home service businesses, law firms, startups and fintech companies across the US with UI/UX, websites, apps, AI agents, automation and SEO.'
    ld = jsonld([crumbs_ld([('Home', '/'), ('Industries', '/industries/')])])
    return f'''{meta(title, desc, 'Tell me about your business.').replace('"nav": "services"', '"nav": "industries"')}
{ld}
    <section class="relative border-b border-line">
      <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
      <div class="container-site grid-asym relative pb-18 pt-16 md:pt-24 lg:pb-22">
        <p class="label reveal md:col-span-3">Industries</p>
        <div class="md:col-span-9">
          <h1 class="display-xl reveal">Built for the way your business works.</h1>
          <p class="lede reveal mt-8 max-w-prose">The same skills, shaped by what I have learned in each field. These are the industries where I have shipped real work. Do not see yours? Most problems are the same underneath, so <a class="link" href="{mailto('New project')}">ask me</a>.</p>
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

{area_section()}
'''


os.makedirs(OUT, exist_ok=True)
(OUT / 'index.html').write_text(hub())
print('wrote services/index')
for s in SERVICES:
    (OUT / f"{s['slug']}.html").write_text(page(s))
    print('wrote services/' + s['slug'])

os.makedirs(IND_OUT, exist_ok=True)
(IND_OUT / 'index.html').write_text(ind_hub())
print('wrote industries/index')
for i in INDUSTRIES:
    (IND_OUT / f"{i['slug']}.html").write_text(ind_page(i))
    print('wrote industries/' + i['slug'])
