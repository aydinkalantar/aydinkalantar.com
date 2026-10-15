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

// Ambient music: off by default (browsers block sound that starts on its own).
// The toggle fades a looping track in and out, and the choice is remembered between pages.
(() => {
  const buttons = document.querySelectorAll('[data-sound]');
  const AudioCtx = window.AudioContext || window.webkitAudioContext;
  if (!buttons.length || !AudioCtx) { buttons.forEach((b) => b.remove()); return; }
  const SRC = '/assets/audio/ambient.mp3', LOOP = 64, LEVEL = 0.35, KEY = 'ak-sound';
  let ctx, gain, source, buffer, on = false, ducked = false;
  const store = (v) => { try { localStorage.setItem(KEY, v); } catch (e) {} };
  const stored = () => { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  const render = () => buttons.forEach((b) => {
    b.setAttribute('aria-pressed', String(on));
    b.setAttribute('aria-label', on ? 'Pause ambient music' : 'Play ambient music');
  });
  const ramp = (to, secs) => {
    const t = ctx.currentTime;
    gain.gain.cancelScheduledValues(t);
    gain.gain.setValueAtTime(gain.gain.value, t);
    gain.gain.linearRampToValueAtTime(to, t + secs);
  };
  const start = async () => {
    if (!ctx) { ctx = new AudioCtx(); gain = ctx.createGain(); gain.gain.value = 0; gain.connect(ctx.destination); }
    if (ctx.state === 'suspended') await ctx.resume();
    if (!buffer) buffer = await fetch(SRC).then((r) => r.arrayBuffer()).then((a) => ctx.decodeAudioData(a));
    if (!source) {
      source = ctx.createBufferSource();
      source.buffer = buffer; source.loop = true;
      source.loopStart = 0; source.loopEnd = Math.min(LOOP, buffer.duration);
      source.connect(gain); source.start();
    }
    if (on && !ducked) ramp(LEVEL, 2.5);
  };
  const setOn = (value) => {
    on = value; store(on ? 'on' : 'off'); render();
    if (on) start().catch(() => { on = false; render(); });
    else if (ctx) ramp(0, 1.2);
  };
  buttons.forEach((b) => b.addEventListener('click', () => setOn(!on)));
  render();

  // Visitors who turned it on earlier get it back on their first tap or key press.
  if (stored() === 'on') {
    on = true; render();
    const resume = () => { start().catch(() => { on = false; render(); }); };
    ['pointerdown', 'keydown', 'touchstart'].forEach((ev) => window.addEventListener(ev, resume, { once: true, passive: true }));
  }

  // Step aside while a video with sound is playing.
  document.querySelectorAll('video').forEach((v) => {
    v.addEventListener('play', () => { if (!v.muted && ctx) { ducked = true; ramp(0, 0.6); } });
    const back = () => { if (ducked) { ducked = false; if (on && ctx) ramp(LEVEL, 2); } };
    v.addEventListener('pause', back); v.addEventListener('ended', back);
    v.addEventListener('volumechange', () => { if (!v.paused && !v.muted && ctx) { ducked = true; ramp(0, 0.6); } else if (v.muted) back(); });
  });
})();
