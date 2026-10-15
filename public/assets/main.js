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
