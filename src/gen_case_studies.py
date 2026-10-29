import html, os, re

import pathlib
OUT = str(pathlib.Path(__file__).resolve().parent / 'pages' / 'case-studies')

def ul(items):
    return '<ul>\n' + '\n'.join(f'                <li>{i}</li>' for i in items) + '\n              </ul>'

CL_SHOWCASE = '''
      <!-- Catch Lead agent: greeting and conversation panel -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">The agent</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Meet Max: a greeting, then a conversation.</h3>
            <p class="body reveal mt-4 max-w-prose">The orb waits quietly at the foot of the page. A short greeting offers two ways in, typing or talking, and the panel opens into a chat with quick replies for the questions every business gets.</p>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-1 items-end gap-10 sm:grid-cols-2 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-3xl mx-auto">
          <figure class="reveal">
            <picture>
              <source srcset="/assets/work/catch-lead/agent-greeting.webp" type="image/webp">
              <img src="/assets/work/catch-lead/agent-greeting.jpg" width="656" height="906" alt="Catch Lead greeting card from Max over a page: Ask me anything about prices or booking, with Ask a question and Talk buttons above the orb" loading="lazy" class="block h-auto w-full">
            </picture>
            <figcaption class="media-caption"><span>A · Greeting</span><span>Type or talk, the visitor chooses</span></figcaption>
          </figure>
          <figure class="reveal">
            <picture>
              <source srcset="/assets/work/catch-lead/agent-panel.webp" type="image/webp">
              <img src="/assets/work/catch-lead/agent-panel.jpg" width="596" height="860" alt="Catch Lead chat panel: Max greets the visitor, who asks for a quote this week, with quick replies Get a quote, Services and Book a time" loading="lazy" class="block h-auto w-full">
            </picture>
            <figcaption class="media-caption"><span>B · Conversation</span><span>Quick replies for common questions</span></figcaption>
          </figure>
        </div>
      </section>

      <!-- Catch Lead product: the agent on a live client site, then the owner's dashboard -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">On a client's site</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">One tap, and Max picks up.</h3>
            <p class="body reveal mt-4 max-w-prose">Running live for a Los Angeles apparel printer. A single button sits on the page; visitors talk or type, Max remembers returning customers, takes the details, and asks for a rating when the conversation ends.</p>
            <p class="meta reveal mt-4">Try it here: the assistant in the corner of this site is Catch Lead.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line bg-ink p-px">
            <picture>
              <source srcset="/assets/work/catch-lead/instant-preview.webp" type="image/webp">
              <img src="/assets/work/catch-lead/instant-preview.jpg" width="1600" height="975" alt="Catch Lead instant preview: a Los Angeles screen printing company's homepage with the Max orb added at the bottom, generated from the site's address" loading="lazy" class="block h-auto w-full">
            </picture>
          </div>
          <figcaption class="media-caption"><span>Instant preview</span><span>Paste a website address and see Max on it in seconds, before signing up</span></figcaption>
        </figure>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/agent-site.webp" type="image/webp">
                <img src="/assets/work/catch-lead/agent-site.jpg" width="702" height="1260" alt="Catch Lead on a client website: a Los Angeles apparel printer homepage with a glowing Tap to talk with Max button" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>01 · Invite</span><span>Tap to talk, on any page</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/agent-chat.webp" type="image/webp">
                <img src="/assets/work/catch-lead/agent-chat.jpg" width="702" height="1260" alt="Catch Lead agent Max listening in a chat window, greeting a returning customer by name and asking for a phone number" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>02 · Conversation</span><span>Voice or text, remembers returning visitors</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/agent-rating.webp" type="image/webp">
                <img src="/assets/work/catch-lead/agent-rating.jpg" width="702" height="1260" alt="Catch Lead rating prompt asking how was your experience, with five stars and a Submit button" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>03 · Feedback</span><span>Every chat ends with a rating</span></figcaption>
          </figure>
        </div>
        <div class="mt-18 grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">The dashboard</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Every lead arrives already written up.</h3>
            <p class="body reveal mt-4 max-w-prose">The owner's side is a phone-first dashboard in light and dark mode. Each conversation becomes a lead with an AI summary, the exact request and a priced quote, ready to turn into an invoice or a booked visit.</p>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/dash-lead.webp" type="image/webp">
                <img src="/assets/work/catch-lead/dash-lead.jpg" width="702" height="1260" alt="Catch Lead dashboard lead card: AI summary of intent, the request for 72 one-color printed cotton t-shirts, and an itemized quote totaling 822 dollars" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>04 · Lead</span><span>AI summary and an instant quote</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/dash-calendar.webp" type="image/webp">
                <img src="/assets/work/catch-lead/dash-calendar.jpg" width="702" height="1260" alt="Catch Lead dashboard calendar in light mode showing two booked appointments on Wednesday, October 14" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>05 · Calendar</span><span>Booked visits, synced</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/catch-lead/dash-analytics.webp" type="image/webp">
                <img src="/assets/work/catch-lead/dash-analytics.jpg" width="702" height="1260" alt="Catch Lead dashboard analytics in dark mode: conversations, leads captured, conversion rate, average lead score, agent rating and daily activity" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>06 · Analytics</span><span>Conversion, lead score, agent rating</span></figcaption>
          </figure>
        </div>
      </section>
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
        <!-- The app on a phone: three steps of one flow -->
        <div class="mt-18 grid-asym items-end border-t border-line pt-16">
          <div class="md:col-span-3">
            <p class="label">On a phone</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">The full studio, one thumb away.</h3>
            <p class="body reveal mt-4 max-w-prose">The desktop workspace folds into three bottom sheets on mobile. Pick a garment, describe the shot, then set format, quality and cost before anything is generated.</p>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/app/mobile-assets.webp" type="image/webp">
                <img src="/assets/work/app/mobile-assets.jpg" width="718" height="1518" alt="Virtual Fashion mobile app: product sheet showing a sweatshirt collection with a pullover hoodie selected" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>01 · Assets</span><span>Choose a base garment</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/app/mobile-dna.webp" type="image/webp">
                <img src="/assets/work/app/mobile-dna.jpg" width="718" height="1518" alt="Virtual Fashion mobile app: AI prompt sheet with a lighting and lens prompt and a row of locked model identities" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>02 · DNA</span><span>Describe the scene, lock a model</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/app/mobile-create.webp" type="image/webp">
                <img src="/assets/work/app/mobile-create.jpg" width="718" height="1518" alt="Virtual Fashion mobile app: Start Production sheet with canvas format, quality, batch mode and a total cost in credits" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>03 · Create</span><span>Format, quality and cost</span></figcaption>
          </figure>
        </div>
        <!-- Start to finish: Ayden's own recordings, from blank garment to finished video -->
        <div class="mt-18 grid-asym items-end border-t border-line pt-16">
          <div class="md:col-span-3">
            <p class="label">Start to finish</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">From a blank garment to a finished film, on a phone.</h3>
            <p class="body reveal mt-4 max-w-prose">Three real sessions, recorded in the app: pick a garment, add the artwork, cast a model, render the photo, then animate it. Sound on.</p>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <video class="block aspect-[540/1168] w-full rounded-[1.4rem] bg-ink object-contain" controls playsinline preload="none" poster="/assets/work/app/howto-1-poster.jpg" aria-label="Screen recording: a puffer vest is picked, colored and given a graphic in Virtual Fashion, a model is cast, and the finished photo is animated into a video">
                <source src="/assets/work/app/howto-1.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>01 · Puffer vest</span><span>Start to finish · 0:31</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <video class="block aspect-[540/1168] w-full rounded-[1.4rem] bg-ink object-contain" controls playsinline preload="none" poster="/assets/work/app/howto-2-poster.jpg" aria-label="Screen recording: a T-shirt is designed in Virtual Fashion, rendered on a model and animated into a video">
                <source src="/assets/work/app/howto-2.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>02 · T-shirt</span><span>Start to finish · 0:25</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <video class="block aspect-[540/1168] w-full rounded-[1.4rem] bg-ink object-contain" controls playsinline preload="none" poster="/assets/work/app/howto-3-poster.jpg" aria-label="Screen recording: a knit sweater design is uploaded, given a fabric finish, rendered on a model in a rainy street and animated into a walking video">
                <source src="/assets/work/app/howto-3.mp4" type="video/mp4">
              </video>
            </div>
            <figcaption class="media-caption"><span>03 · Knit sweater</span><span>Start to finish · 0:27</span></figcaption>
          </figure>
        </div>
        <div class="mt-18 flex items-baseline justify-between gap-6 border-b border-line pb-5">
          <p class="label">Gallery · Generated outputs</p>
          <p class="meta hidden sm:block">Stills and motion, all made in Virtual Fashion</p>
        </div>
        <div class="mt-10 grid gap-x-6 gap-y-10 md:grid-cols-12">
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/red-hoodie.webp" type="image/webp">
                <img src="/assets/work/gallery/red-hoodie.jpg" width="1344" height="768" alt="Hoodie generated with Virtual Fashion: brand mark on a red pullover, garage set" loading="lazy" class="h-full w-full object-cover">
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
                <img src="/assets/work/gallery/distressed-tee.jpg" width="1600" height="893" alt="Distressed tee generated with Virtual Fashion: penthouse, city view" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Distressed tee</span><span>Penthouse, city view</span></figcaption>
          </figure>
          <figure class="reveal md:col-span-7">
            <div class="aspect-[16/10] overflow-hidden border border-line bg-ink">
              <picture>
                <source srcset="/assets/work/gallery/bucket-hat.webp" type="image/webp">
                <img src="/assets/work/gallery/bucket-hat.jpg" width="1376" height="768" alt="Bucket hat generated with Virtual Fashion: bedroom, natural light" loading="lazy" class="h-full w-full object-cover">
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
                <img src="/assets/work/gallery/long-sleeve.jpg" width="1344" height="768" alt="Long-sleeve tee generated with Virtual Fashion: mid-century living room" loading="lazy" class="h-full w-full object-cover">
              </picture>
            </div>
            <figcaption class="media-caption"><span>Long-sleeve tee</span><span>Mid-century living room</span></figcaption>
          </figure>
        </div>
      </section>
'''

AA_HERO = '''      <figure class="container-site grid-asym reveal items-start py-16 lg:py-22">
        <div class="md:col-span-9">
          <div class="border border-line bg-ink p-px">
            <video id="aa-explainer" class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/auto-alpha/how-autoalpha-works-poster.jpg" aria-label="Voiced explainer from autoalpha.trade, with demo data: create a free account, connect an exchange with a trade-only API key, pick a strategy from its backtest, set an amount and start on paper or live, then watch each trade in the dashboard and pause any time">
              <source src="/assets/work/auto-alpha/how-autoalpha-works.mp4" type="video/mp4">
              <a class="link" href="/assets/work/auto-alpha/how-autoalpha-works.mp4">Download the video</a>
            </video>
          </div>
          <figcaption class="media-caption"><span>Fig. 01</span><span>How Auto Alpha works · the voiced explainer on autoalpha.trade, demo data · 1:07</span></figcaption>
        </div>
        <div class="md:col-span-3">
          <p class="label">Chapters</p>
          <ol class="mt-4 border-t border-line text-[0.9375rem]">
            <li><button type="button" data-target="aa-explainer" data-seek="0" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">01</span><span class="text-ink transition-colors group-hover:text-accent">What Auto Alpha does</span><span class="meta ml-auto">0:00</span></button></li>
            <li><button type="button" data-target="aa-explainer" data-seek="10" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">02</span><span class="text-ink transition-colors group-hover:text-accent">Create your account</span><span class="meta ml-auto">0:10</span></button></li>
            <li><button type="button" data-target="aa-explainer" data-seek="18" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">03</span><span class="text-ink transition-colors group-hover:text-accent">Connect your exchange</span><span class="meta ml-auto">0:18</span></button></li>
            <li><button type="button" data-target="aa-explainer" data-seek="28" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">04</span><span class="text-ink transition-colors group-hover:text-accent">Pick a strategy</span><span class="meta ml-auto">0:28</span></button></li>
            <li><button type="button" data-target="aa-explainer" data-seek="40" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">05</span><span class="text-ink transition-colors group-hover:text-accent">Set an amount, start</span><span class="meta ml-auto">0:40</span></button></li>
            <li><button type="button" data-target="aa-explainer" data-seek="48" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">06</span><span class="text-ink transition-colors group-hover:text-accent">Let it trade</span><span class="meta ml-auto">0:48</span></button></li>
          </ol>
        </div>
      </figure>
'''

AA_SHOWCASE = '''
      <!-- Auto Alpha testing: how a strategy earns its place -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">The bar for a strategy</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Eight new strategy ideas tested in September. None made the cut.</h3>
            <p class="body reveal mt-4 max-w-prose">A strategy is designed on Bitcoin from 2018 to 2023, then judged only on what it never saw: 2024 onward, and ten other coins with the same settings. It also has to pass four stress tests. Most ideas fail, and the ones that fail are not published.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line p-6 sm:p-10">
            <div class="flex h-14 w-full gap-px bg-line" role="img" aria-label="Timeline from January 2018 to October 2026: rules designed on 2018 to 2023, judged on 2024 onward">
              <div class="bg-ink-faint" style="width:68%"></div>
              <div class="bg-ink" style="width:32%"></div>
            </div>
            <div class="meta relative mt-3 h-5"><span class="absolute left-0">Jan 2018</span><span class="absolute -translate-x-1/2" style="left:68%">2024</span><span class="absolute right-0">Oct 2026</span></div>
            <dl class="mt-8 grid grid-cols-1 gap-8 sm:grid-cols-3">
              <div class="border-t border-ink-faint pt-4">
                <dt class="label">Designed on</dt>
                <dd class="display-md mt-3">6 years</dd>
                <dd class="meta mt-2">Bitcoin daily candles, 2018 to 2023</dd>
              </div>
              <div class="border-t border-ink pt-4">
                <dt class="label">Judged on unseen data</dt>
                <dd class="display-md mt-3">2024 →</dd>
                <dd class="meta mt-2">Plus ten other coins, same settings</dd>
              </div>
              <div class="border-t border-line pt-4">
                <dt class="label">Stress tests to pass</dt>
                <dd class="display-md mt-3">4</dd>
                <dd class="meta mt-2">Other coins · settings ±20% · 2023 on · triple costs</dd>
              </div>
            </dl>
          </div>
          <figcaption class="media-caption"><span>Fig. 02</span><span>The test every strategy goes through before it is published · no returns shown, because backtests are hypothetical</span></figcaption>
        </figure>
      </section>

      <!-- Auto Alpha strategy explainers -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">Strategy explainers</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Every strategy, explained before anyone starts it.</h3>
            <p class="body reveal mt-4 max-w-prose">Each strategy family has its own voiced film on its page: the idea in one line, when it buys and sells, what the Long and Short version adds, the safety stop, and its backtest, labelled hypothetical on screen and in the voiceover.</p>
          </div>
        </div>
        <div class="mt-12 grid grid-cols-1 gap-10 md:grid-cols-3 md:gap-6 lg:gap-10">
          <figure class="reveal">
            <div class="border border-line bg-ink p-px">
              <video class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/auto-alpha/keltnerpulse-poster.jpg" aria-label="Voiced explainer for the KeltnerPulse strategy: the channel it draws, when it buys and sells, the Long and Short rules, its safety stop, and its hypothetical Bitcoin backtest with the disclaimer">
                <source src="/assets/work/auto-alpha/keltnerpulse.mp4" type="video/mp4">
                <a class="link" href="/assets/work/auto-alpha/keltnerpulse.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>KeltnerPulse</span><span>Breakouts with momentum · 1:42</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="border border-line bg-ink p-px">
              <video class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/auto-alpha/gaussian-channel-poster.jpg" aria-label="Voiced explainer for the Gaussian Channel strategy: the idea, when it buys and sells, the Long and Short rules, risk controls, and its hypothetical Bitcoin backtest with the disclaimer">
                <source src="/assets/work/auto-alpha/gaussian-channel.mp4" type="video/mp4">
                <a class="link" href="/assets/work/auto-alpha/gaussian-channel.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>Gaussian Channel</span><span>A slow trend follower · 1:41</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="border border-line bg-ink p-px">
              <video class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/auto-alpha/gaussbreaker-poster.jpg" aria-label="Voiced explainer for the GaussBreaker strategy: the idea, when it buys and sells, the Long and Short rules, risk controls, and its hypothetical Bitcoin backtest with the disclaimer">
                <source src="/assets/work/auto-alpha/gaussbreaker.mp4" type="video/mp4">
                <a class="link" href="/assets/work/auto-alpha/gaussbreaker.mp4">Download the video</a>
              </video>
            </div>
            <figcaption class="media-caption"><span>GaussBreaker</span><span>Joins breakouts, steps aside · 1:31</span></figcaption>
          </figure>
        </div>
      </section>

      <!-- Auto Alpha on the live site: desktop, then phone -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">On the live site</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Pick one. Every number labelled.</h3>
            <p class="body reveal mt-4 max-w-prose">The home page says what Auto Alpha does and what it costs in one paragraph. Strategy cards lead with this year's backtest, but the hypothetical label, the worst drop and the strategy's own simulated record since launch sit right beside it, and the disclaimer comes before any number.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line bg-ink p-px">
            <picture>
              <source srcset="/assets/work/auto-alpha/home-desktop.webp" type="image/webp">
              <img src="/assets/work/auto-alpha/home-desktop.jpg" width="2000" height="1250" alt="Auto Alpha home page: headline Trade crypto while you sleep, a paragraph on spot and futures strategies that trade your own exchange account with a fee only on new profit, and Start with AutoAlpha and See the strategies buttons" loading="lazy" class="block h-auto w-full">
            </picture>
          </div>
          <figcaption class="media-caption"><span>Fig. 03</span><span>Home page · autoalpha.trade</span></figcaption>
        </figure>
        <figure class="reveal mt-12">
          <div class="border border-line bg-ink p-px">
            <picture>
              <source srcset="/assets/work/auto-alpha/strategies-desktop.webp" type="image/webp">
              <img src="/assets/work/auto-alpha/strategies-desktop.jpg" width="2000" height="1250" alt="Auto Alpha featured strategies: Pick one. It trades itself, a hypothetical-results notice, tabs for three strategies, and a KeltnerPulse Pro card with its 2026 backtest labelled hypothetical, its simulated record since launch, risk level and worst drop" loading="lazy" class="block h-auto w-full">
            </picture>
          </div>
          <figcaption class="media-caption"><span>Fig. 04</span><span>Featured strategies · backtest labelled hypothetical, simulated record and worst drop beside it</span></figcaption>
        </figure>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <picture>
                <source srcset="/assets/work/auto-alpha/home-mobile.webp" type="image/webp">
                <img src="/assets/work/auto-alpha/home-mobile.jpg" width="640" height="1385" alt="Auto Alpha home page on a phone with Start with AutoAlpha and See the strategies buttons" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>01 · Home</span><span>What it does, in one paragraph</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <picture>
                <source srcset="/assets/work/auto-alpha/strategy-mobile.webp" type="image/webp">
                <img src="/assets/work/auto-alpha/strategy-mobile.jpg" width="640" height="1385" alt="KeltnerPulse v3.0 Pro strategy page on a phone: market, timeframe, direction and fee tiles, the rules in plain words, and a hypothetical-results notice" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>02 · Strategy</span><span>The rules before the return</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-ink p-1.5">
              <picture>
                <source srcset="/assets/work/auto-alpha/testing-mobile.webp" type="image/webp">
                <img src="/assets/work/auto-alpha/testing-mobile.jpg" width="640" height="1385" alt="How we test our strategies page on a phone, with a hypothetical-results notice and the steps from idea to live" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>03 · Method</span><span>How every strategy is tested</span></figcaption>
          </figure>
        </div>
      </section>
'''

CL_HERO = '''      <figure class="container-site reveal py-16 lg:py-22">
        <div class="border border-line bg-canvas p-px">
          <video data-autoplay class="block aspect-[1600/830] w-full" muted loop playsinline controls preload="none" poster="/assets/work/catch-lead/desktop-demo-poster.jpg" aria-label="Screen recording: a visitor taps the orb on the Catch Lead website and Max answers by voice, explaining the product and the free trial">
            <source src="/assets/work/catch-lead/desktop-demo.mp4" type="video/mp4">
            <a class="link" href="/assets/work/catch-lead/desktop-demo.mp4">Download the recording</a>
          </video>
        </div>
        <figcaption class="media-caption"><span>Fig. 01</span><span>Max answering by voice on a live site · unmute for sound · 0:19</span></figcaption>
      </figure>
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

TBSP_HERO = '''      <figure class="container-site grid-asym reveal items-start py-16 lg:py-22">
        <div class="md:col-span-9">
          <div class="border border-line bg-ink p-px">
            <video id="tbsp-max" class="block aspect-video w-full" controls playsinline preload="none" poster="/assets/work/tbsp/max-explainer-poster.jpg" aria-label="Voiced explainer from the TBSP home page: a customer asks Max for 100 tees, 50 hoodies and 50 hats for a 5K race, picks navy, uploads a logo that appears on every item, gets sizes split and one priced total, then orders and pays">
              <source src="/assets/work/tbsp/max-explainer.mp4" type="video/mp4">
              <a class="link" href="/assets/work/tbsp/max-explainer.mp4">Download the video</a>
            </video>
          </div>
          <figcaption class="media-caption"><span>Fig. 01</span><span>Meet Max · the voiced explainer on the TBSP home page · 0:49</span></figcaption>
        </div>
        <div class="md:col-span-3">
          <p class="label">Chapters</p>
          <ol class="mt-4 border-t border-line text-[0.9375rem]">
            <li><button type="button" data-target="tbsp-max" data-seek="3" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">01</span><span class="text-ink transition-colors group-hover:text-accent">Tell Max what you need</span><span class="meta ml-auto">0:03</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="11" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">02</span><span class="text-ink transition-colors group-hover:text-accent">He picks the products</span><span class="meta ml-auto">0:11</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="17" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">03</span><span class="text-ink transition-colors group-hover:text-accent">Pick a color</span><span class="meta ml-auto">0:17</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="23" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">04</span><span class="text-ink transition-colors group-hover:text-accent">Upload your logo</span><span class="meta ml-auto">0:23</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="29" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">05</span><span class="text-ink transition-colors group-hover:text-accent">Sizes, split for you</span><span class="meta ml-auto">0:29</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="33" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">06</span><span class="text-ink transition-colors group-hover:text-accent">One total, free shipping</span><span class="meta ml-auto">0:33</span></button></li>
            <li><button type="button" data-target="tbsp-max" data-seek="39" class="group flex w-full items-baseline gap-3 border-b border-line py-3 text-left transition-colors hover:text-accent"><span class="meta w-6 shrink-0">07</span><span class="text-ink transition-colors group-hover:text-accent">Order and pay</span><span class="meta ml-auto">0:39</span></button></li>
          </ol>
        </div>
      </figure>
'''

TBSP_SHOWCASE = '''
      <!-- TBSP migration: what happened to every old URL -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">The migration</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">2,662 old URLs. Every one with a decision.</h3>
            <p class="body reveal mt-4 max-w-prose">Each address on the old site was checked against 16 months of Search Console data before anything moved. The pages people actually found were kept at the same URL and rewritten. The rest were folded into the page that answers the same search, or retired.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line p-6 sm:p-10">
            <div class="flex h-14 w-full gap-px bg-line" role="img" aria-label="Bar of 2,662 URLs: 104 kept, 2,503 redirected, 55 retired">
              <div class="bg-ink" style="width:3.9%"></div>
              <div class="bg-canvas" style="width:94.0%; background-image:repeating-linear-gradient(135deg, rgb(var(--color-line)) 0 1px, transparent 1px 7px)"></div>
              <div class="bg-ink-faint" style="width:2.1%"></div>
            </div>
            <dl class="mt-8 grid grid-cols-1 gap-8 sm:grid-cols-3">
              <div class="border-t border-ink pt-4">
                <dt class="label">Kept and rewritten</dt>
                <dd class="display-md mt-3">104</dd>
                <dd class="meta mt-2">Same URL, new copy · 96% of past clicks</dd>
              </div>
              <div class="border-t border-line pt-4">
                <dt class="label">Redirected (301)</dt>
                <dd class="display-md mt-3">2,503</dd>
                <dd class="meta mt-2">2,479 were auto-generated service and city pages</dd>
              </div>
              <div class="border-t border-ink-faint pt-4">
                <dt class="label">Retired (410)</dt>
                <dd class="display-md mt-3">55</dd>
                <dd class="meta mt-2">Page-builder fragments and test leftovers</dd>
              </div>
            </dl>
          </div>
          <figcaption class="media-caption"><span>Fig. 02</span><span>Old WordPress URLs by outcome · clicks and impressions from Search Console, 16 months</span></figcaption>
        </figure>
      </section>

      <!-- TBSP on the live site: desktop, then phone -->
      <section class="border-t border-line py-16 lg:py-22">
        <div class="grid-asym items-end">
          <div class="md:col-span-3">
            <p class="label">On the live site</p>
          </div>
          <div class="md:col-span-8 md:col-start-5">
            <h3 class="display-md reveal">Shop first, with Max one tap away.</h3>
            <p class="body reveal mt-4 max-w-prose">The home page opens on a real order mocked up on a real blank, with the price per piece and the minimum in the first sentence. Ask Max sits inside the search bar, and on a phone he takes the center of the tab bar.</p>
          </div>
        </div>
        <figure class="reveal mt-12">
          <div class="border border-line bg-canvas p-px">
            <picture>
              <source srcset="/assets/work/tbsp/home-desktop.webp" type="image/webp">
              <img src="/assets/work/tbsp/home-desktop.jpg" width="2000" height="1250" alt="TBSP home page: headline Custom merch, done right, tees from $9.25 each, Shop products and Talk to Max buttons, and a black tee mockup with a tour print on the back, with an Ask Max button in the search bar" loading="lazy" class="block h-auto w-full">
            </picture>
          </div>
          <figcaption class="media-caption"><span>Fig. 03</span><span>Home page · thebestscreenprinting.com</span></figcaption>
        </figure>
        <figure class="reveal mt-12">
          <div class="border border-line bg-canvas p-px">
            <picture>
              <source srcset="/assets/work/tbsp/product-design-desktop.webp" type="image/webp">
              <img src="/assets/work/tbsp/product-design-desktop.jpg" width="2000" height="1250" alt="TBSP product page for a red Gildan 18500 hoodie with a TBSP wordmark placed on the front in the design preview, color swatches and quantity by size" loading="lazy" class="block h-auto w-full">
            </picture>
          </div>
          <figcaption class="media-caption"><span>Fig. 04</span><span>Product page · artwork placed on the front in the live preview</span></figcaption>
        </figure>
        <div class="mt-12 grid grid-cols-1 gap-10 sm:grid-cols-3 sm:gap-6 lg:gap-10 max-w-sm sm:max-w-none mx-auto">
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/tbsp/home-mobile.webp" type="image/webp">
                <img src="/assets/work/tbsp/home-mobile.jpg" width="640" height="1385" alt="TBSP home page on a phone with Shop products and Talk to Max buttons and a bottom tab bar with Max in the center" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>01 · Home</span><span>Max in the center of the tab bar</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/tbsp/product-mobile.webp" type="image/webp">
                <img src="/assets/work/tbsp/product-mobile.jpg" width="640" height="1385" alt="TBSP product page on a phone: red hoodie with a dashed front print area to add artwork, and Add to cart and Order and pay buttons" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>02 · Product</span><span>Add artwork, then order and pay</span></figcaption>
          </figure>
          <figure class="reveal">
            <div class="overflow-hidden rounded-[1.75rem] border border-line bg-canvas p-1.5">
              <picture>
                <source srcset="/assets/work/tbsp/quote-mobile.webp" type="image/webp">
                <img src="/assets/work/tbsp/quote-mobile.jpg" width="640" height="1385" alt="TBSP quote form on a phone: Tell us what you need, with garment, quantity, decoration and a Send my quote request button" loading="lazy" class="block h-auto w-full rounded-[1.4rem]">
              </picture>
            </div>
            <figcaption class="media-caption"><span>03 · Quote</span><span>A person is still one form away</span></figcaption>
          </figure>
        </div>
      </section>
'''

CASES = [
 dict(
  slug='tbsp', num='01', hero=TBSP_HERO, after_solution=TBSP_SHOWCASE, name='The Best Screen Printing', url='https://thebestscreenprinting.com', domain='thebestscreenprinting.com',
  schematic='schematic-cl', fig='',
  title='The Best Screen Printing case study · Aydin Kalantar',
  desc='How Aydin Kalantar rebuilt thebestscreenprinting.com for a Los Angeles print shop: a buy-first catalog, an AI merch agent that takes orders by voice, and a WordPress migration that kept its search traffic.',
  headline='Rebuilding a print shop\'s website so customers can order, not just ask.',
  facts=[('Role','Design, development & SEO'),('Type','E-commerce + local SEO'),('Platform','Astro on Cloudflare Workers'),('Live','<a class="link" href="https://thebestscreenprinting.com" target="_blank" rel="noopener">thebestscreenprinting.com</a>')],
  parts=[
   ('Overview', '''<p>The Best Screen Printing (TBSP) is a screen printing and embroidery shop in Downtown Los Angeles, with a second production facility in Cleveland. I worked there from 2017 to 2020 on the brand, the website, SEO and paid ads.</p>
              <p>In 2026 I came back to rebuild thebestscreenprinting.com from the ground up: from a WordPress site where every order started with a quote form, to a fast static site where customers browse real products, place their design, pick a deadline and pay, or simply tell Max what they need. Max is the agent I built for <a class="link" href="/case-studies/catch-lead/">Catch Lead</a>, here working as the shop's merch agent.</p>'''),
   ('Challenges', ul([
                '<strong>Years of search history on the line.</strong> The old site had 2,662 URLs, and the home page alone had about 245,000 search impressions in 16 months. A careless migration would have thrown that away.',
                '<strong>Most pages were thin.</strong> Nearly 2,500 of those URLs were auto-generated "service in city" pages, the kind search engines now treat as noise.',
                '<strong>Every order started with a wait.</strong> Buyers filled in a form and waited for a reply before they saw a price, which is where many of them left.',
                '<strong>Custom merch is hard to picture.</strong> Print placement, print method, size splits and turnaround fees are decisions a first-time buyer doesn\'t know how to make.'])),
   ('UI/UX solutions', '''<p>I designed the site around one change: let people buy first, and keep a quote and a real person one tap away for everything else.</p>
              <h3>A catalog you can order from</h3>
              <p>403 blank styles from brands buyers already know, grouped the way people shop: tees, hoodies, hats, polos, bags. Each product page has a design preview with the print areas for that garment (front, back, chest, sleeves), size steppers that show the price per piece, a recommended print method, and Normal, Rush or Super Rush turnaround with the fee shown up front.</p>
              <h3>Max as the front door</h3>
              <p>The search bar takes plain language ("50 black tees for our tour, front and back, by Friday") and hands it to Max. One tap starts a voice call. Max picks the product, splits the sizes, checks each design and places it front, back or sleeve, and returns a priced order card. Change anything out loud and the price updates. The details he collects fill the checkout, and the customer approves a free proof before anything prints.</p>
              <h3>Pages that answer the search</h3>
              <p>The pages worth keeping were rewritten with local facts, and new pages were added where searches had no good answer: industry pages for bands, teams, schools and companies, and regional shipping pages built from past out-of-state quote requests. The same facts (6-piece minimum, turnaround, free shipping from $300) read the same everywhere.</p>
              <h3>Built for the phone</h3>
              <p>A bottom tab bar, a cart that remembers, and an order tracker, because most customers find the shop from a search on their phone.</p>'''),
   ('Technical solutions', '''<h3>A migration driven by data</h3>
              <p>Every old URL lives in one spreadsheet with its clicks, impressions and average position, and an action: keep, 301 or 410. A build script turns it into a redirect table, and a Cloudflare Worker answers old URLs before any page is served. A check script then requests every old URL against the preview and fails on anything unexpected. Kept pages stay at their exact address, trailing slash included, so rankings carry over without a redirect.</p>
              <h3>Static and fast</h3>
              <p>The site is built with Astro into 585 static pages and served from Cloudflare's edge. Styles are inlined into each page and hashed assets are cached for a year, so pages paint complete on the first frame.</p>
              <h3>One source of truth</h3>
              <p>The business name, address, hours, minimum and turnaround options live in one file that feeds every page, the structured data for search, and the quote emails. The catalog syncs from the shop's admin, and refuses an update that would shrink it by more than half.</p>
              <h3>Live voice in the browser</h3>
              <p>The shop's studio issues a short-lived token with Max's instructions and tools locked in. The browser then streams the caller's microphone to the voice model over a WebSocket and plays the reply back as it arrives, so callers can interrupt him mid-sentence. When Max picks a product or places a design, the tool call comes back as a card in the chat. The audio pipeline is the one from the Catch Lead widget.</p>
              <h3>Quotes the shop can act on</h3>
              <p>A request that still needs a person is sent by the Worker with the customer's artwork, rendered mockups, placements and sizes, plus a branded PDF summary for the shop and the customer.</p>
              <h3>A weekly SEO loop</h3>
              <p>A script pulls Search Console every week and writes a report: pages seen but not clicked, pages ranking just off page one with the searches to answer, searches with no good page yet, and traffic still landing on redirected URLs. New pages are announced to search engines through IndexNow.</p>'''),
   ('Outcome', '''<p>The new thebestscreenprinting.com is live, replacing the WordPress site in October 2026.</p>
              ''' + ul([
                'Customers can go from a blank tee to a paid order without waiting for a reply.',
                'Max takes orders by voice or text on every page, with designs placed and priced in the conversation.',
                'All 2,662 old URLs are accounted for, with the 104 kept pages carrying 96% of the clicks the old site earned.',
                'A weekly Search Console report drives what gets written or fixed next.']) + '''
              <!-- ADD METRICS: orders placed online, Max conversations and orders, search clicks before and after launch -->'''),
  ]),
 dict(
  slug='virtual-fashion', num='02', hero=VF_HERO, after_solution=VF_SHOWCASE, name='Virtual Fashion', url='https://virtualfashion.app', domain='virtualfashion.app',
  schematic='schematic-vf', fig='Workspace: tool rail, garment canvas, finish panel',
  title='Virtual Fashion case study · Aydin Kalantar',
  desc='How Virtual Fashion turns apparel photography into a browser canvas: AI garment design, consistent models, scenes and 4K video export.',
  headline='Turning apparel photography into a browser canvas.',
  facts=[('Role','Product design & development'),('Type','B2C SaaS'),('Platform','Web app, installable'),('Live','<a class="link" href="https://virtualfashion.app" target="_blank" rel="noopener">virtualfashion.app</a>')],
  parts=[
   ('Overview', '''<p>Virtual Fashion is a browser studio for designing apparel and producing the imagery to sell it. A designer picks a garment, places artwork on it, casts a model, sets the scene and exports studio-quality photos and video, all in one workspace.</p>'''),
   ('Challenges', ul([
                '<strong>Photography is the bottleneck.</strong> Convincing apparel imagery needs samples, a photographer, models and a location, or 3D software with a steep learning curve. Small brands and creators need it before a garment physically exists.',
                '<strong>A prompt box is the wrong tool for a designer.</strong> Generative AI can make the pictures, but typing descriptions gives no direct control over where a logo sits or how a print wraps.',
                '<strong>The same face, every time.</strong> A brand needs one model to look identical across every photo and video, which generative models do not do on their own.',
                '<strong>Rendering is slow and costly.</strong> High-resolution images and video take minutes and real compute, so waiting on a spinner would stall the creative work.'])),
   ('UI/UX solutions', '''<p>I organized the product around how a real shoot is planned: the product, the model, the set, then the motion. That sequence became the navigation itself: Workspace, Identity, Motion and Showcase.</p>
              <h3>A smart canvas, not a prompt</h3>
              <p>The garment stays at the center of the screen and the designer works on it directly. Logos are dropped on and placed automatically, one uploaded pattern repeats across the garment, and material finishes (embroidery, puff print, screen print, sublimation) are picked from a panel rather than described in words.</p>
              <h3>Identity as its own step</h3>
              <p>Casting is a dedicated screen with a library of lifestyle and runway models. Designers can also cast their own face from a single selfie, or upload a full-body photo for a personal try-on, so consistency is a choice made once instead of a prompt detail repeated every time.</p>
              <h3>One-click scenes and motion</h3>
              <p>Nine scene presets, from studio gray to a golden-hour desert, switch with one tap. A short instruction makes the model walk, pose or spin, with the output format (9:16 for Reels and TikTok, 16:9 for lookbooks) chosen up front.</p>
              <h3>Never make people wait</h3>
              <p>Renders run in the background while design continues, and land in a private gallery. The same flow works on a phone, where the studio is one thumb away.</p>'''),
   ('Technical solutions', '''<h3>A generation pipeline behind the canvas</h3>
              <p>Each canvas action becomes structured input for the image models: garment, artwork placement, material finish, model identity and scene. That keeps results predictable and repeatable, instead of depending on how a prompt happens to be worded.</p>
              <h3>Automatic artwork placement</h3>
              <p>PNG, JPG and SVG logos are positioned on the garment automatically, and uploaded patterns are tiled so the repeat follows the folds of the fabric rather than sitting flat on top.</p>
              <h3>Identity that stays consistent</h3>
              <p>A model's identity is stored once and reused in every image and video render, so the same face carries across a whole shoot. A single selfie is enough to create a new identity.</p>
              <h3>A cloud render queue</h3>
              <p>Image and video jobs run in the cloud and save to the user's private gallery. Video is generated with Kling 2.6 Pro, Kling 3.0 Pro or Veo 3.1, in 4, 6 or 8 second clips, directed by a preset motion style or a written camera direction, and the cost in credits is shown before anything starts. Batch Mode queues large runs at half the credit cost and emails the user when they finish. Exports cover PNG, WebP and MP4 at 2K for images and 4K for video.</p>
              <h3>One credit system</h3>
              <p>Images and video draw from a single credit balance across Starter, Creator and Agency plans, with top-up packs and a referral loop that rewards both sides. The app is installable on phone and desktop.</p>'''),
   ('Outcome', '''<p>Virtual Fashion is live, with free starter credits for every new account.</p>
              ''' + ul([
                'Exports PNG, WebP and MP4, with 2K images and 4K video.',
                'Full commercial rights for e-commerce, social and pitch decks.',
                'One credit system across images and video, with Starter, Creator and Agency plans plus top-up packs.',
                'A referral loop that rewards both sides with credits.']) + '''
              <!-- ADD METRICS: sign-ups, renders generated, conversion from free credits to paid -->'''),
  ]),
 dict(
  slug='catch-lead', num='03', hero=CL_HERO, after_solution=CL_SHOWCASE, name='Catch Lead', url='https://catchlead.dev', domain='catchlead.dev',
  schematic='schematic-cl', fig='Chat and voice assistant on a client site',
  title='Catch Lead case study · Aydin Kalantar',
  desc='How Catch Lead gives service businesses an AI sales agent that answers by chat or voice, quotes from real prices and books appointments.',
  headline='A sales agent that never misses a visitor.',
  facts=[('Role','Product design & development'),('Type','B2B SaaS'),('Platform','Website widget + PWA'),('Live','<a class="link" href="https://catchlead.dev" target="_blank" rel="noopener">catchlead.dev</a>')],
  parts=[
   ('Overview', '''<p>Catch Lead adds an AI assistant to a service business's website. It answers visitors by chat or voice, in their language, quotes from the business's own prices, books appointments and emails the owner every lead.</p>'''),
   ('Challenges', ul([
                '<strong>Missed calls are lost jobs.</strong> Plumbers, roofers, HVAC teams and law firms lose customers after hours and while they are out on jobs.',
                '<strong>Owners are not technical.</strong> They have no time for scripts, integrations or training a bot, so setup had to take minutes.',
                '<strong>A wrong price is worse than no answer.</strong> An assistant that invents a quote damages the business, so every answer had to come from the business itself.',
                '<strong>One script on someone else\'s website.</strong> The widget has to look right and work on any site (Wix, WordPress, Squarespace or custom code) without breaking the page around it.'])),
   ('UI/UX solutions', '''<p>I treated setup as the product and trust as the constraint, and designed for two different moments: the visitor, who should feel like they are on a phone call, and the owner, who checks leads on a phone between jobs.</p>
              <h3>Onboarding in three steps</h3>
              <p>Paste the website address, add one line of code, and leads start arriving. Before signing up, an owner can enter their URL and see the assistant on a preview of their own site in seconds.</p>
              <h3>The orb</h3>
              <p>A single glowing orb invites visitors to talk or type. They can interrupt naturally, as on a call, send photos of the job, and switch to text at any time. Max greets them with a short card first, so the voice never starts without a tap.</p>
              <h3>A handoff that feels personal</h3>
              <p>When a visitor needs a person, the assistant collects their name, contact details and needs in the conversation itself, then tells them the owner will follow up.</p>
              <h3>A dashboard built for the truck</h3>
              <p>Leads, conversations and bookings live in one installable app with a swipeable weekly calendar. Each lead arrives already written up with a summary and quote. A quote becomes an invoice in one tap, and marking a job done sends it.</p>'''),
   ('Technical solutions', '''<h3>One script tag, fully isolated</h3>
              <p>The widget loads from a single script and renders inside a closed Shadow DOM, so the host site's styles cannot break it and the widget cannot leak styles into the page. It follows the site's light or dark theme and is configured through attributes on the script tag.</p>
              <h3>Real-time voice</h3>
              <p>Voice runs over one streaming WebSocket connection to Google's Gemini Live, which gives a natural voice and lets visitors interrupt mid-sentence. The assistant detects the visitor's language across 13 options and offers 30 voices.</p>
              <h3>Grounded answers</h3>
              <p>At setup Catch Lead reads the business's website for services, prices and service area. The assistant answers only from that knowledge, which the owner can edit, and quotes only published prices.</p>
              <h3>Leads, bookings and payments</h3>
              <p>Every conversation is turned into a lead with a summary and quote, and the owner is emailed right away. Bookings land in the calendar, Stripe handles deposits, and the same inbox now covers Instagram, WhatsApp and SMS. Usage alerts at 80% and 100% replace hard limits, so a lead is never blocked.</p>'''),
   ('Outcome', '''<p>Catch Lead is live with a 14-day free trial that needs no card.</p>
              ''' + ul([
                'Plans run from solo operators to agencies, with white-label and multi-location support at the top tier.',
                'Leads are never hard-blocked at a plan limit; owners get usage alerts at 80% and 100% instead.',
                'The product grew into an omnichannel inbox for Instagram, WhatsApp and SMS, with Stripe deposits and review automation.']) + '''
              <!-- ADD METRICS: businesses onboarded, conversations handled, bookings created -->'''),
  ]),
 dict(
  slug='auto-alpha', num='04', hero=AA_HERO, after_solution=AA_SHOWCASE, name='Auto Alpha', url='https://autoalpha.trade', domain='autoalpha.trade',
  schematic='schematic-aa', fig='Strategy dashboard: key figures, equity curve, trade list',
  title='Auto Alpha case study · Aydin Kalantar',
  desc='How Aydin Kalantar designed and built Auto Alpha: automated crypto strategies on your own exchange account, explained in voiced films, tested on years they never saw, with funds that never leave the exchange.',
  headline='Designing trust into an automated trading dashboard.',
  facts=[('Role','Product design & development'),('Type','Fintech SaaS'),('Platform','Web dashboard'),('Live','<a class="link" href="https://autoalpha.trade" target="_blank" rel="noopener">autoalpha.trade</a>')],
  parts=[
   ('Overview', '''<p>Auto Alpha runs rule-based crypto strategies on a user's own exchange account, around the clock. Funds never leave the exchange; Auto Alpha only places trades.</p>
              <p>I designed and built the whole product: the strategies and their testing, the trading engine, the dashboard, and the voiced explainer films that walk people through it before they connect any money.</p>'''),
   ('Challenges', ul([
                '<strong>Trust before money.</strong> People are asked to connect real money to a system they cannot see inside.',
                '<strong>Products that hide the risk.</strong> Automated trading tools tend to lead with their best return and bury the losses.',
                '<strong>Dense data for non-experts.</strong> Equity curves, drawdowns and trade logs had to be readable by people who are not quants.',
                '<strong>Security of exchange keys.</strong> The product places trades on the user\'s own exchange account, so a leaked key or forged signal must never be able to move funds.'])),
   ('UI/UX solutions', '''<p>I set a few rules before designing any screen: show the drop next to the gain, label every hypothetical, show every trade (losses included), and make stopping easier than starting.</p>
              <h3>Strategy cards</h3>
              <p>Each card puts backtest return, the period covered, risk level, worst drop and the simulated record since launch in one compact frame, so strategies can be compared honestly at a glance. Detail pages add a log-scale equity curve and an every-trade ledger.</p>
              <h3>Shown, then explained</h3>
              <p>A one-minute film on the home page walks through the whole setup with demo data, and each strategy has its own film that explains its rules in plain words before anyone allocates to it.</p>
              <h3>Practice first</h3>
              <p>Every account starts with $10,000 of paper money at live prices, so people can watch a strategy behave before risking anything.</p>
              <h3>A guided, careful connection</h3>
              <p>Connecting an exchange is a step-by-step flow that explains each setting, such as why the key must be trade-only, before anything is saved.</p>
              <h3>Stop controls in reach</h3>
              <p>Users can pause new entries, let open trades close, or stop everything at market in one action, from the desktop or a phone.</p>
              <h3>Pricing that explains itself</h3>
              <p>A calculator compares the profit-share plan with the flat monthly plan for the user's own numbers and shows where one becomes cheaper than the other.</p>'''),
   ('Technical solutions', '''<h3>Funds never leave the exchange</h3>
              <p>Users create a trade-only API key locked to Auto Alpha's IP address. Keys with withdrawal rights are refused, stored keys are encrypted with AES-256, and two-factor sign-in is required before any real-money trade.</p>
              <h3>Signals that can't be forged or replayed</h3>
              <p>Incoming TradingView webhooks are validated and protected against replay before any order goes out, and signals that arrive late are dropped rather than chased.</p>
              <h3>Risk limits at the exchange</h3>
              <p>Stop-losses are placed on the exchange itself, so they hold even if Auto Alpha is offline, and leverage is capped at 1×.</p>
              <h3>Honest testing</h3>
              <p>The backtest replays the same code that trades live, candle by candle from January 2018, deciding on a closed candle and filling at the next open, with fees and slippage on every entry and exit. Every active strategy is re-tested on the 1st of each month. Backtest, simulated and real-money figures are stored and shown separately, never mixed.</p>
              <h3>An exchange earns real money</h3>
              <p>Each exchange has to complete a full testnet run (entries, strategy exits, stops and reconciliation against the exchange's own records) before it accepts real-money keys. Until then it stays listed for paper and testnet only.</p>
              <h3>Reporting</h3>
              <p>Paper accounts run at live prices, weekly email reports summarize activity, and real-money trades export to CSV for the tax year.</p>'''),
   ('Outcome', '''<p>Auto Alpha is live for real money on Binance (spot and futures) and Coinbase (spot), with more exchanges on testnet.</p>
              ''' + ul([
                'Six strategies in ten versions, each with a stress-test badge and a public record of every signal since launch, and voiced explainers for the main families.',
                'Private TradingView strategies on Pro.',
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

def slug(label):
    return re.sub(r'[^a-z]+', '-', label.lower()).strip('-')

def page(c):
    i = ORDER.index(c['slug']); nxt = CASES[(i + 1) % len(CASES)]
    facts = '\n'.join(f'            <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in c['facts'])
    parts = ''
    for n, (label, body) in enumerate(c['parts'], 1):
        parts += f'''
      <section id="{slug(label)}" class="scroll-mt-20 border-t border-line py-16 lg:py-22">
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
        if label == 'UI/UX solutions' and c.get('after_solution'):
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
