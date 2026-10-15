import html, os

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent / 'pages' / 'case-studies')

def ul(items):
    return '<ul>\n' + '\n'.join(f'                <li>{i}</li>' for i in items) + '\n              </ul>'

CL_SHOWCASE = '''
      <!-- Catch Lead films: explainer plus social shorts -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">In motion</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Explained in forty seconds, sold in ten.</h3>
            <p class="body reveal mt-4 max-w-prose">An explainer for the website and a set of short vertical films for social, each built around the same moment: a customer reaching out after hours and getting an answer instead of silence.</p>
          </div>
        </div>
        <div class="mt-12">
          <figure class="reveal">
            <div class="overflow-hidden border border-line bg-ink p-px">
              <video data-autoplay muted loop class="block aspect-video w-full object-cover" playsinline controls preload="none" poster="/assets/work/catch-lead/short-missed-call-poster.jpg" aria-label="Catch Lead promo film: a roofer misses a call, and the AI sales agent answers and books the job">
                <source src="/assets/work/catch-lead/short-missed-call.mp4" type="video/mp4">
                <a class="link" href="/assets/work/catch-lead/short-missed-call.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>Promo · Missed call, booked job</span><span>0:10</span></figcaption>
          </figure>
        </div>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden border border-line bg-ink p-px">
              <video class="block aspect-[9/16] w-full object-cover" playsinline controls preload="metadata" poster="/assets/work/catch-lead/how-it-works-poster.jpg" aria-label="Catch Lead explainer film: how the AI sales agent turns missed messages into closed deals">
                <source src="/assets/work/catch-lead/how-it-works.mp4" type="video/mp4">
                <a class="link" href="/assets/work/catch-lead/how-it-works.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>How it works · Explainer, with sound</span><span>0:40</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden border border-line bg-ink p-px">
              <video data-autoplay muted loop class="block aspect-[9/16] w-full object-cover" playsinline controls preload="none" poster="/assets/work/catch-lead/short-law-firm-poster.jpg" aria-label="Catch Lead short: a visitor gets an instant answer from a law firm website at night and becomes a qualified lead">
                <source src="/assets/work/catch-lead/short-law-firm.mp4" type="video/mp4">
                <a class="link" href="/assets/work/catch-lead/short-law-firm.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>Short · Law firm, after hours</span><span>0:10</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden border border-line bg-ink p-px">
              <video data-autoplay muted loop class="block aspect-[9/16] w-full object-cover" playsinline controls preload="none" poster="/assets/work/catch-lead/short-leaking-leads-poster.jpg" aria-label="Catch Lead short: the voice agent greets a visitor and offers to book an appointment">
                <source src="/assets/work/catch-lead/short-leaking-leads.mp4" type="video/mp4">
                <a class="link" href="/assets/work/catch-lead/short-leaking-leads.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>Short · Stop leaking leads</span><span>0:12</span></figcaption>
          </figure>
        </div>
      </section>
'''

VF_SHOWCASE = '''
      <!-- Made with the product: muted reel that plays while in view -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">Made with Virtual Fashion</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">A lookbook generated entirely in the product.</h3>
            <p class="body reveal mt-4 max-w-prose">Caps, hoodies, tanks and mugs carrying a real brand, placed on models in real-looking scenes, then animated into a short film. No photographer, set or samples.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line bg-ink p-px">
            <video data-autoplay class="block aspect-video w-full" muted loop playsinline controls preload="none" poster="/assets/work/virtual-fashion-lookbook-poster.jpg" aria-label="Lookbook film of apparel and products generated with Virtual Fashion">
              <source src="/assets/work/virtual-fashion-lookbook.mp4" type="video/mp4">
              <a class="link" href="/assets/work/virtual-fashion-lookbook.mp4">Download the lookbook film</a>
            </video>
          </div>
          <figcaption class="media-caption"><span>Fig. 02</span><span>Lookbook film generated with Virtual Fashion · 0:23</span></figcaption>
        </figure>
        <div class="mt-18 flex items-baseline justify-between gap-6 border-b border-line pb-5">
          <p class="label">Gallery · Generated outputs</p>
          <p class="meta hidden sm:block">Stills and motion, all made in Virtual Fashion</p>
        </div>
        <div class="mt-10 grid gap-x-6 gap-y-10 md:grid-cols-12">
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/red-hoodie.webp" type="image/webp">
                <img src="/assets/work/gallery/red-hoodie.jpg" alt="Hoodie generated with Virtual Fashion: brand mark on a red pullover, garage set" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Hoodie</span><span>Brand mark on a red pullover, garage set</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-5">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <video data-autoplay class="h-full w-full object-cover" muted loop playsinline preload="none" poster="/assets/work/gallery/cap-video.jpg" aria-label="Baseball cap video generated with Virtual Fashion">
                <source src="/assets/work/gallery/cap-video.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>Baseball cap</span><span>Motion, brick loft · Video</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-5">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <video data-autoplay class="h-full w-full object-cover" muted loop playsinline preload="none" poster="/assets/work/gallery/tank-video.jpg" aria-label="Cotton tank video generated with Virtual Fashion">
                <source src="/assets/work/gallery/tank-video.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>Cotton tank</span><span>Motion, warehouse · Video</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/distressed-tee.webp" type="image/webp">
                <img src="/assets/work/gallery/distressed-tee.jpg" alt="Distressed tee generated with Virtual Fashion: penthouse, city view" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Distressed tee</span><span>Penthouse, city view</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/bucket-hat.webp" type="image/webp">
                <img src="/assets/work/gallery/bucket-hat.jpg" alt="Bucket hat generated with Virtual Fashion: bedroom, natural light" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Bucket hat</span><span>Bedroom, natural light</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-5">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <video data-autoplay class="h-full w-full object-cover" muted loop playsinline preload="none" poster="/assets/work/gallery/mug-video.jpg" aria-label="Mug video generated with Virtual Fashion">
                <source src="/assets/work/gallery/mug-video.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>Mug</span><span>Motion, garage set · Video</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-5">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <video data-autoplay class="h-full w-full object-cover" muted loop playsinline preload="none" poster="/assets/work/gallery/zip-hoodie-video.jpg" aria-label="Zip hoodie video generated with Virtual Fashion">
                <source src="/assets/work/gallery/zip-hoodie-video.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>Zip hoodie</span><span>Motion, botanical garden · Video</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/long-sleeve.webp" type="image/webp">
                <img src="/assets/work/gallery/long-sleeve.jpg" alt="Long-sleeve tee generated with Virtual Fashion: mid-century living room" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Long-sleeve tee</span><span>Mid-century living room</span></figcaption>
          </figure>
        </div>
      </section>
'''

VF_HERO = '''      <figure class="container-site grid-asym reveal items-start py-16 lg:py-22">
        <div class="md:col-span-9">
          <div class="border border-line bg-ink p-px">
            <video id="vf-demo" class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/virtual-fashion-demo-poster.jpg" aria-label="Product demo of Virtual Fashion, from choosing a garment to the final AI-generated film">
              <source src="/assets/work/virtual-fashion-demo.mp4" type="video/mp4">
              <a class="link" href="/assets/work/virtual-fashion-demo.mp4">Download the demo</a>
            </video>
          </div>
          <figcaption class="media-caption"><span>Fig. 01</span><span>Product demo · 0:55</span></figcaption>
        </div>
        <div class="md:col-span-3">
          <p class="label">Chapters</p>
          <ol class="mt-4 border-t border-line text-[0.9375rem]">
            <li><button type="button" data-target="vf-demo" data-seek="2" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">01</span><span class="text-ink transition-colors group-hover:text-accent">Choose a garment</span><span class="meta ml-auto">0:02</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="6" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">02</span><span class="text-ink transition-colors group-hover:text-accent">Place graphics</span><span class="meta ml-auto">0:06</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="12" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">03</span><span class="text-ink transition-colors group-hover:text-accent">Apply a pattern</span><span class="meta ml-auto">0:12</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="22" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">04</span><span class="text-ink transition-colors group-hover:text-accent">Prompt and cast</span><span class="meta ml-auto">0:22</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="30" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">05</span><span class="text-ink transition-colors group-hover:text-accent">Render</span><span class="meta ml-auto">0:30</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="42" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">06</span><span class="text-ink transition-colors group-hover:text-accent">Add motion</span><span class="meta ml-auto">0:42</span></button></li>\n            <li><button type="button" data-target="vf-demo" data-seek="50" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">07</span><span class="text-ink transition-colors group-hover:text-accent">Final film</span><span class="meta ml-auto">0:50</span></button></li>\n          </ol>
        </div>
      </figure>
'''

CASES = [
 dict(
  slug='virtual-fashion', num='01', hero=VF_HERO, after_solution=VF_SHOWCASE, name='Virtual Fashion', url='https://virtualfashion.app', domain='virtualfashion.app',
  schematic='schematic-vf', fig='Workspace: tool rail, garment canvas, finish panel',
  title='Virtual Fashion case study · Aydin Kalantar',
  desc='How Virtual Fashion turns apparel photography into a browser canvas: AI garment design, consistent models, scenes and 4K video export.',
  headline='Turning apparel photography into a browser canvas.',
  facts=[('Role','Product design & development'),('Type','B2C SaaS'),('Platform','Web app, installable'),('Live','<a class="link" href="https://virtualfashion.app" target="_blank" rel="noopener">virtualfashion.app</a>')],
  parts=[
   ('Overview', '''<p>Virtual Fashion is a browser studio for designing apparel and producing the imagery to sell it. A designer picks a garment, places artwork on it, casts a model, sets the scene and exports studio-quality photos and video, all in one workspace.</p>'''),
   ('Challenge', '''<p>Apparel imagery has always been expensive. It takes samples, a photographer, models and a location, or 3D software with a steep learning curve. Small brands and creators need convincing visuals before a garment physically exists.</p>
              <p>Generative AI can produce the pictures, but a bare prompt box is the wrong tool for a designer. The challenge was to make a powerful generation pipeline feel like a <strong>design tool</strong>: direct, predictable and consistent from one image to the next.</p>'''),
   ('Approach', '''<p>I organized the product around how a real shoot is planned: the product, the model, the set, then the motion. That sequence became the navigation itself: Workspace, Identity, Motion and Showcase.</p>
              ''' + ul([
                '<strong>The canvas stays central.</strong> AI handles tedious steps such as placement and pattern repeats; the designer keeps every decision.',
                '<strong>Consistency is the core requirement.</strong> A brand needs the same face across every photo and video, so identity is its own step, not a prompt detail.',
                '<strong>Never make people wait.</strong> Rendering is slow, so it runs in the background while design continues.'])),
   ('Solution', '''<h3>A smart canvas</h3>
              <p>Logos in PNG, JPG or SVG are placed automatically. One uploaded pattern repeats across the garment and follows the fabric folds. Material finishes simulate embroidery, puff print, screen print and sublimation.</p>
              <h3>Identity</h3>
              <p>A library of lifestyle and runway models stays consistent across shoots. Designers can cast their own face from a single selfie, or upload a full-body photo for a personal virtual try-on.</p>
              <h3>Scene and motion</h3>
              <p>Nine scene presets, from studio gray to a golden-hour desert, switch with one click. A short prompt makes the model walk, pose or spin, exported as 9:16 for Reels and TikTok or 16:9 for lookbooks.</p>
              <h3>A production queue</h3>
              <p>Renders run in the cloud and save to a private gallery. Batch Mode queues large image runs at half the credit cost and sends an email when they finish.</p>'''),
   ('Outcome', '''<p>Virtual Fashion is live, with free starter credits for every new account.</p>
              ''' + ul([
                'Exports PNG, WebP and MP4, with 2K images and 4K video.',
                'Full commercial rights for e-commerce, social and pitch decks.',
                'One credit system across images and video, with Starter, Creator and Agency plans plus top-up packs.',
                'A referral loop that rewards both sides with credits.']) + '''
              <!-- ADD METRICS: sign-ups, renders generated, conversion from free credits to paid -->'''),
  ]),
 dict(
  slug='catch-lead', num='02', after_solution=CL_SHOWCASE, name='Catch Lead', url='https://catchlead.dev', domain='catchlead.dev',
  schematic='schematic-cl', fig='Chat and voice assistant on a client site',
  title='Catch Lead case study · Aydin Kalantar',
  desc='How Catch Lead gives service businesses an AI sales agent that answers by chat or voice, quotes from real prices and books appointments.',
  headline='A sales agent that never misses a visitor.',
  facts=[('Role','Product design & development'),('Type','B2B SaaS'),('Platform','Website widget + PWA'),('Live','<a class="link" href="https://catchlead.dev" target="_blank" rel="noopener">catchlead.dev</a>')],
  parts=[
   ('Overview', '''<p>Catch Lead adds an AI assistant to a service business's website. It answers visitors by chat or voice, in their language, quotes from the business's own prices, books appointments and emails the owner every lead.</p>'''),
   ('Challenge', '''<p>Plumbers, roofers, HVAC teams and law firms lose customers after hours and while they are out on jobs. A missed call is often a lost job.</p>
              <p>The owners are rarely technical and have no time for scripts or integrations. And an assistant that invents a price does more damage than no assistant at all. It had to be <strong>simple to set up and impossible to embarrass the business</strong>.</p>'''),
   ('Approach', '''<p>I treated setup as the product and trust as the constraint.</p>
              ''' + ul([
                '<strong>Three steps to live.</strong> Anything more than a pasted link and one line of code would lose the owner.',
                '<strong>Grounded answers only.</strong> The assistant learns from the business\'s own website, and the owner can edit everything it learned.',
                '<strong>Two moments, two designs.</strong> The visitor gets a conversation that feels like a phone call; the owner gets a dashboard built for a phone between jobs.'])),
   ('Solution', '''<h3>Onboarding in three steps</h3>
              <p>Paste the website address and Catch Lead reads the services, prices and service area. Add one line to Wix, WordPress, Squarespace or any site. Leads and bookings start arriving. Before signing up, an owner can enter their URL and see the widget on a screenshot of their own site in about ten seconds.</p>
              <h3>The orb</h3>
              <p>Visitors tap a glowing orb to talk, or type. They can interrupt naturally, as on a call, and send photos of the job. The assistant detects the visitor's language across 13 options and offers 30 voices.</p>
              <h3>Guardrails</h3>
              <p>Quotes come only from published prices. When a visitor needs a person, the assistant collects their name, contact details and needs, then emails the owner right away.</p>
              <h3>The owner's dashboard</h3>
              <p>Leads, conversations and bookings live in one installable app with a swipeable weekly calendar. A quote becomes an invoice in one tap, and marking a job done sends the invoice automatically.</p>'''),
   ('Outcome', '''<p>Catch Lead is live with a 14-day free trial that needs no card.</p>
              ''' + ul([
                'Plans run from solo operators to agencies, with white-label and multi-location support at the top tier.',
                'Leads are never hard-blocked at a plan limit; owners get usage alerts at 80% and 100% instead.',
                'The product grew into an omnichannel inbox for Instagram, WhatsApp and SMS, with Stripe deposits and review automation.']) + '''
              <!-- ADD METRICS: businesses onboarded, conversations handled, bookings created -->'''),
  ]),
 dict(
  slug='auto-alpha', num='03', name='Auto Alpha', url='https://autoalpha.trade', domain='autoalpha.trade',
  schematic='schematic-aa', fig='Strategy dashboard: key figures, equity curve, trade list',
  title='Auto Alpha case study · Aydin Kalantar',
  desc='How Auto Alpha designs trust into automated crypto trading: risk shown beside return, every trade visible, and funds that never leave the exchange.',
  headline='Designing trust into an automated trading dashboard.',
  facts=[('Role','Product design & development'),('Type','Fintech SaaS'),('Platform','Web dashboard'),('Live','<a class="link" href="https://autoalpha.trade" target="_blank" rel="noopener">autoalpha.trade</a>')],
  parts=[
   ('Overview', '''<p>Auto Alpha runs rule-based crypto strategies on a user's own exchange account, around the clock. Funds never leave the exchange; Auto Alpha only places trades.</p>'''),
   ('Challenge', '''<p>Automated trading products tend to lead with their best return and bury the risk. People are asked to connect real money to a system they cannot see inside.</p>
              <p>The challenge was to make a product whose <strong>trust is earned through transparency</strong>, and to make dense performance data readable for people who are not quants.</p>'''),
   ('Approach', '''<p>I set a few rules for every screen before designing any of them.</p>
              ''' + ul([
                '<strong>Show the drop next to the gain.</strong> Worst drop in testing sits beside every return figure.',
                '<strong>Label every hypothetical.</strong> Backtests and simulated records are always marked as such.',
                '<strong>Show every trade, losses included.</strong>',
                '<strong>Make stopping easier than starting.</strong>',
                '<strong>The money never moves.</strong> Connections are trade-only, with withdrawals disabled.'])),
   ('Solution', '''<h3>Strategy cards</h3>
              <p>Each card puts backtest return, the period covered, risk level, worst drop and the simulated record since launch in one compact frame, so strategies can be compared honestly at a glance. Detail pages add a log-scale equity curve and an every-trade ledger.</p>
              <h3>Practice first</h3>
              <p>Every account starts with $10,000 of paper money at live prices, so people can watch a strategy behave before risking anything.</p>
              <h3>A careful connection flow</h3>
              <p>Users create a trade-only API key locked to Auto Alpha's IP address, and two-factor sign-in is required before any real-money trade.</p>
              <h3>Visible guardrails and stop controls</h3>
              <p>Late signals are dropped rather than chased, stop-losses sit on the exchange itself, and leverage is capped at 1×. Users can pause new entries, let open trades close, or stop everything at market in one action.</p>
              <h3>Pricing that explains itself</h3>
              <p>A calculator compares the profit-share plan with the flat monthly plan for the user's own numbers and shows where one becomes cheaper than the other.</p>'''),
   ('Outcome', '''<p>Auto Alpha is live on Binance for spot and futures, with more exchanges in progress.</p>
              ''' + ul([
                'A library of six strategies in ten versions, plus private TradingView strategies on Pro.',
                'Weekly email reports and yearly CSV export of real-money trades.',
                'Risk disclosures written in plain language and linked from every strategy.']) + '''
              <!-- ADD METRICS: accounts connected, paper-to-live conversion -->
              <p class="meta">Trading involves risk of loss. Backtests and simulated records are hypothetical and do not reflect real-money results.</p>'''),
  ]),
]

DEFAULT_HERO = '''      <figure class="container-site reveal py-16 lg:py-22">
        <div class="media blueprint p-6 text-ink sm:p-12 lg:p-16">
          <!-- PROJECT IMAGE SLOT: replace the schematic with <img src="/assets/work/{c[slug]}-hero.jpg" alt="..."> -->
          {{{{> {c[schematic]} class="w-full"}}}}
        </div>
        <figcaption class="media-caption"><span>Fig. 01</span><span>{c[fig]}</span></figcaption>
      </figure>
'''

ORDER = [c['slug'] for c in CASES]

def page(c):
    i = ORDER.index(c['slug']); nxt = CASES[(i + 1) % len(CASES)]
    facts = '\n'.join(f'            <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in c['facts'])
    parts = ''
    for n, (label, body) in enumerate(c['parts'], 1):
        parts += f'''
      <section id="{label.lower()}" class="scroll-mt-20 border-t border-line py-16 lg:py-22">
        <div class="grid-asym">
          <div class="md:col-span-3">
            <p class="label md:sticky md:top-28"><span class="text-ink-faint">0{n}</span>&nbsp;&nbsp;{label}</p>
          </div>
          <div class="reveal md:col-span-8 md:col-start-5">
            <div class="prose-case">
              {body}
            </div>
          </div>
        </div>
      </section>
'''
        if label == 'Solution' and c.get('after_solution'):
            parts += c['after_solution']
    hero = c.get('hero') or DEFAULT_HERO.format(c=c)
    meta = '{"title": "%s", "description": "%s", "nav": "case-studies"}' % (c['title'], c['desc'])
    return f'''<!-- {meta} -->
    <article>
      <header class="relative border-b border-line">
        <div class="blueprint pointer-events-none absolute inset-0 opacity-50 [mask-image:linear-gradient(to_bottom,black,transparent_90%)]" aria-hidden="true"></div>
        <div class="container-site relative pb-18 pt-12 md:pt-20 lg:pb-22">
          <nav aria-label="Breadcrumb" class="meta reveal"><a class="transition-colors hover:text-accent" href="/case-studies/">Case studies</a> <span class="text-ink-faint">/</span> {c['num']}</nav>
          <div class="grid-asym mt-12 items-end">
            <div class="md:col-span-8">
              <p class="label reveal">{c['name']}</p>
              <h1 class="display-lg reveal mt-6">{c['headline']}</h1>
            </div>
            <div class="reveal md:col-span-4 md:col-start-9 lg:col-span-3 lg:col-start-10">
              <a href="{c['url']}" target="_blank" rel="noopener" class="btn-secondary group w-full justify-between">Visit {c['domain']} <span aria-hidden="true" class="arrow">↗</span></a>
            </div>
          </div>
          <dl class="facts reveal mt-14">
{facts}
          </dl>
        </div>
      </header>

{hero}
      <div class="container-site pb-16">
{parts}
      </div>

      <nav aria-label="Next case study" class="border-t border-line">
        <a href="/case-studies/{nxt['slug']}/" class="container-site group grid-asym items-center py-16 lg:py-22">
          <p class="label md:col-span-3">Next case study</p>
          <p class="display-lg md:col-span-8 md:col-start-5 transition-colors group-hover:text-accent">{nxt['name']} <span aria-hidden="true" class="arrow">→</span></p>
        </a>
      </nav>
    </article>
'''

os.makedirs(OUT, exist_ok=True)
for c in CASES:
    open(f"{OUT}/{c['slug']}.html", 'w').write(page(c))
    print('wrote', c['slug'])
