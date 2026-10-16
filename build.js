// Assembles src/pages/**/*.html into public/ using src/partials/layout.html.
//
// Page files start with a JSON comment holding their metadata:
//   <!-- {"title": "...", "description": "...", "nav": "about"} -->
// Partials are included with {{> name}} or {{> name class="w-full"}}.
// No dependencies: run with `node build.js` (npm run build also compiles the CSS).

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, 'src');
const PAGES = path.join(SRC, 'pages');
const PARTIALS = path.join(SRC, 'partials');
const OUT = path.join(__dirname, 'public');

const partial = (name) => fs.readFileSync(path.join(PARTIALS, `${name}.html`), 'utf8');

const includePartials = (html) =>
  html.replace(/\{\{>\s*([\w-]+)(?:\s+class="([^"]*)")?\s*\}\}/g, (_, name, cls = '') =>
    includePartials(partial(name)).replace(/\{\{class\}\}/g, cls)
  );

const walk = (dir) =>
  fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? walk(full) : entry.name.endsWith('.html') ? [full] : [];
  });

const layout = partial('layout');

// Assets are cached for a week, so their URLs carry a content hash: a change ships a new URL.
// The CSS is compiled after this script, so its hash covers everything Tailwind reads.
const fingerprint = (files) => {
  const h = crypto.createHash('sha1');
  files.forEach((f) => h.update(fs.readFileSync(f)));
  return h.digest('hex').slice(0, 8);
};
const cssVersion = fingerprint([
  path.join(SRC, 'input.css'),
  path.join(__dirname, 'tailwind.config.js'),
  ...walk(PAGES).sort(),
  ...walk(PARTIALS).sort(),
]);
const jsVersion = fingerprint([path.join(OUT, 'assets', 'main.js')]);

for (const file of walk(PAGES)) {
  const raw = fs.readFileSync(file, 'utf8');
  const match = raw.match(/^<!--\s*(\{[\s\S]*?\})\s*-->\s*/);
  if (!match) throw new Error(`Missing metadata comment in ${file}`);
  const meta = JSON.parse(match[1]);

  // src/pages/about.html -> /about/ ; src/pages/index.html -> / ; src/pages/case-studies/index.html -> /case-studies/
  const rel = path.relative(PAGES, file).replace(/\\/g, '/').replace(/\.html$/, '');
  const urlPath = rel === 'index' || rel === '404' ? '/' : `/${rel.replace(/\/?index$/, '')}/`;

  let html = layout
    .replace('{{content}}', raw.slice(match[0].length))
    .replace(/\{\{title\}\}/g, meta.title)
    .replace(/\{\{description\}\}/g, meta.description)
    .replace(/\{\{path\}\}/g, urlPath)
    .replace('{{contact}}', meta.contact || 'Have a product that deserves craft?');
  html = includePartials(html)
    .replace('/assets/styles.css"', `/assets/styles.css?v=${cssVersion}"`)
    .replace('/assets/main.js"', `/assets/main.js?v=${jsVersion}"`);
  // Per-page social image (large preview card) and noindex for pages not ready for search.
  if (meta.image) html = html.replace('<meta property="og:image" content="https://aydinkalantar.com/assets/aydin-kalantar.jpg">', `<meta property="og:image" content="${meta.image}">`).replace('content="summary"', 'content="summary_large_image"');
  if (meta.noindex) html = html.replace('<meta name="author"', '<meta name="robots" content="noindex, follow">\n  <meta name="author"');
  // Dark pages (the marquetry gallery) swap the color tokens; see .theme-dark in src/input.css.
  if (meta.theme === 'dark') html = html.replace('<body class="', '<body class="theme-dark ').replace('content="#FAFAF7"', 'content="#161614"');
  if (meta.nav) html = html.replace(new RegExp(`data-nav="${meta.nav}"`, 'g'), `data-nav="${meta.nav}" aria-current="page"`);

  // src/pages/404.html becomes public/404.html, which Cloudflare serves for any missing address.
  const outFile = rel === '404' ? path.join(OUT, '404.html') : path.join(OUT, urlPath, 'index.html');
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, html);
  console.log(`built ${urlPath}`);
}
