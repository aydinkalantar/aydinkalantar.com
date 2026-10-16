(() => {
  const header = document.querySelector('header');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const btn = document.getElementById('menu-btn');
  const menu = document.getElementById('mobile-menu');
  const setMenu = (open) => {
    btn.setAttribute('aria-expanded', String(open));
    btn.querySelector('.sr-only').textContent = open ? 'Close menu' : 'Open menu';
    btn.querySelector('.menu-open').classList.toggle('hidden', open);
    btn.querySelector('.menu-close').classList.toggle('hidden', !open);
    menu.classList.toggle('hidden', !open);
  };
  btn.addEventListener('click', () => setMenu(btn.getAttribute('aria-expanded') !== 'true'));
  menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

  // Large headings: wrap each word so it can rise out of its own mask (see .split in input.css).
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.reveal:is(.display-xl, .display-lg, .display-md)').forEach((h) => {
      let i = 0;
      const walk = (node) => [...node.childNodes].forEach((n) => {
        if (n.nodeType === 1) return walk(n);
        if (n.nodeType !== 3 || !n.textContent.trim()) return;
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(part); return; }
          const w = document.createElement('span'); w.className = 'w';
          const inner = document.createElement('span'); inner.textContent = part; inner.style.setProperty('--i', i++);
          w.append(inner); frag.append(w);
        });
        n.replaceWith(frag);
      });
      walk(h);
      h.classList.add('split');
    });
  }

  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add('is-visible'));
  }

  document.getElementById('year').textContent = new Date().getFullYear();
})();

// YouTube facade: show a thumbnail, load the privacy-enhanced player only when clicked.
document.querySelectorAll('[data-yt]').forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const frame = document.createElement('iframe');
    frame.src = `https://www.youtube-nocookie.com/embed/${link.dataset.yt}?autoplay=1&rel=0`;
    frame.title = link.getAttribute('aria-label') || 'Video';
    frame.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
    frame.allowFullscreen = true;
    frame.className = 'absolute inset-0 h-full w-full';
    link.replaceChildren(frame);
    link.removeAttribute('href');
  }, { once: true });
});

// Video chapters: buttons with data-seek (seconds) and data-target (video id) jump to a step and play.
document.querySelectorAll('[data-seek]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const video = document.getElementById(btn.dataset.target);
    if (!video) return;
    const seek = () => { video.currentTime = Number(btn.dataset.seek); video.play(); };
    if (video.readyState >= 1) seek();
    else { video.preload = 'metadata'; video.addEventListener('loadedmetadata', seek, { once: true }); video.load(); }
  });
});

// Muted reels: play only while on screen, and never under reduced motion.
const reels = document.querySelectorAll('video[data-autoplay]');
if (reels.length && 'IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const reelObserver = new IntersectionObserver((entries) => {
    entries.forEach(({ target, isIntersecting }) => {
      if (isIntersecting) { target.preload = 'auto'; target.play().catch(() => {}); }
      else target.pause();
    });
  }, { threshold: 0.4 });
  reels.forEach((v) => reelObserver.observe(v));
}

// Gallery filters: chips with data-filter show one collection; ?c=<collection> opens the gallery filtered.
const chips = document.querySelectorAll('[data-filter]');
if (chips.length) {
  const cards = document.querySelectorAll('#works-grid > [data-collection]');
  const show = (id) => {
    if (![...chips].some((c) => c.dataset.filter === id)) id = 'all';
    chips.forEach((c) => c.setAttribute('aria-pressed', String(c.dataset.filter === id)));
    cards.forEach((card) => { card.hidden = id !== 'all' && card.dataset.collection !== id; if (!card.hidden) card.classList.add('is-visible'); });
  };
  chips.forEach((c) => c.addEventListener('click', () => {
    show(c.dataset.filter);
    const url = new URL(location.href);
    if (c.dataset.filter === 'all') url.searchParams.delete('c'); else url.searchParams.set('c', c.dataset.filter);
    history.replaceState(null, '', url);
  }));
  const wanted = new URLSearchParams(location.search).get('c');
  if (wanted) show(wanted);
}

// Featured slider: native swipe/scroll with snap points; arrows and dots move it. It never advances on its own.
document.querySelectorAll('[data-slider]').forEach((root) => {
  const track = root.querySelector('[data-slider-track]');
  const slides = [...track.children];
  const dots = [...root.querySelectorAll('[data-slide-to]')];
  let current = 0;
  const go = (i) => {
    current = (i + slides.length) % slides.length;
    track.scrollTo({ left: slides[current].offsetLeft, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  };
  const mark = (i) => { current = i; dots.forEach((d, n) => d.setAttribute('aria-current', String(n === i))); };
  mark(0);
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => entries.forEach((en) => { if (en.isIntersecting) mark(slides.indexOf(en.target)); }), { root: track, threshold: 0.6 });
    slides.forEach((s) => io.observe(s));
  }
  root.querySelectorAll('[data-slide-step]').forEach((b) => b.addEventListener('click', () => go(current + Number(b.dataset.slideStep))));
  dots.forEach((d) => d.addEventListener('click', () => go(Number(d.dataset.slideTo))));
  track.tabIndex = 0;
  track.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { e.preventDefault(); go(current + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); go(current - 1); }
  });
});

// Ambient music: off by default (browsers block sound that starts on its own).
// The toggle fades a looping track in and out, and the choice is remembered between pages.
(() => {
  const buttons = document.querySelectorAll('[data-sound]');
  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  if (!buttons.length || !AudioCtx) { buttons.forEach((b) => b.remove()); return; }
  const SRC = '/assets/audio/ambient.mp3', LOOP = 64, LEVEL = 0.35, KEY = 'ak-sound';
  let ctx, gain, source, buffer, on = false;
  const holds = new Set(); // reasons to stay quiet: a video with sound, a voice chat with Max
  const store = (v) => { try { localStorage.setItem(KEY, v); } catch (e) {} };
  const stored = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  // Until the browser lets audio run (it needs a tap on each new page), the bars stay still.
  const running = () => !!ctx && ctx.state === 'running';
  const render = () => buttons.forEach((b) => {
    b.setAttribute('aria-pressed', String(on));
    b.toggleAttribute('data-waiting', on && !running());
    b.setAttribute('aria-label', on ? (running() ? 'Pause ambient music' : 'Resume ambient music') : 'Play ambient music');
  });
  const ramp = (to, secs) => {
    const t = ctx.currentTime;
    gain.gain.cancelScheduledValues(t);
    gain.gain.setValueAtTime(gain.gain.value, t);
    gain.gain.linearRampToValueAtTime(to, t + secs);
  };
  const setup = () => {
    if (ctx) return;
    ctx = new AudioCtx(); gain = ctx.createGain(); gain.gain.value = 0; gain.connect(ctx.destination);
    ctx.onstatechange = render;
  };
  let loading;
  const load = () => (loading = loading || fetch(SRC).then((r) => r.arrayBuffer()).then((a) => new Promise((ok, no) => ctx.decodeAudioData(a, ok, no))));
  const start = async () => {
    setup();
    // resume() has to be called inside the tap itself, before anything is awaited.
    const resumed = ctx.state === 'running' ? null : ctx.resume();
    buffer = buffer || await load();
    if (resumed) await resumed;
    if (!source) {
      source = ctx.createBufferSource();
      source.buffer = buffer; source.loop = true;
      source.loopStart = 0; source.loopEnd = Math.min(LOOP, buffer.duration);
      source.connect(gain); source.start();
    }
    render();
    if (on && !holds.size) ramp(LEVEL, 2.5);
  };
  const fail = () => { on = false; render(); };
  const setOn = (value) => {
    on = value; store(on ? 'on' : 'off'); render();
    if (on) start().catch(fail);
    else if (ctx) ramp(0, 1.2);
  };
  // A tap on bars that are waiting starts the music rather than switching it off.
  buttons.forEach((b) => b.addEventListener('click', (e) => {
    if (on && !running()) { e.stopPropagation(); start().catch(fail); } else setOn(!on);
  }));
  render();

  // Music that was on keeps going on the next page from the visitor's first tap or key press.
  // Only these events let a page start sound (touchstart and pointerdown don't on iPhone).
  const GESTURES = ['click', 'touchend', 'pointerup', 'keydown'];
  const onGesture = () => {
    if (!on || running()) return;
    start().then(() => { if (running()) GESTURES.forEach((ev) => window.removeEventListener(ev, onGesture, true)); }).catch(() => {});
  };
  const waitForGesture = () => GESTURES.forEach((ev) => window.addEventListener(ev, onGesture, { capture: true, passive: true }));
  if (stored() === 'on') {
    on = true; setup(); render();
    load().then((d) => { buffer = d; }).catch(() => {}); // fetch ahead, so the first tap only has to press play
    waitForGesture();
  }
  // Phones pause audio in background tabs; pick it up again on the next tap after returning.
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && on && ctx && !running()) { ctx.resume().catch(() => {}); render(); waitForGesture(); }
  });

  const hold = (why) => { holds.add(why); if (ctx) ramp(0, 0.6); };
  const release = (why) => { if (holds.delete(why) && !holds.size && on && ctx) ramp(LEVEL, 2); };

  // Step aside while a video with sound is playing.
  document.querySelectorAll('video').forEach((v) => {
    v.addEventListener('play', () => { if (!v.muted) hold(v); });
    const back = () => release(v);
    v.addEventListener('pause', back); v.addEventListener('ended', back);
    v.addEventListener('volumechange', () => { if (!v.paused && !v.muted) hold(v); else if (v.muted) back(); });
  });

  // And while a visitor is talking with Max (the layout reports when the widget's microphone opens and closes).
  const voice = (active) => (active ? hold('voice') : release('voice'));
  window.addEventListener('ak:voice', (e) => voice(e.detail.active));
  if (window.akVoiceActive && window.akVoiceActive()) voice(true);
})();
