// Assembles src/pages/**/*.html into public/ using src/partials/layout.html.
//
// Page files start with a JSON comment holding their metadata:
//   <!-- {"title": "...", "description": "...", "nav": "about"} -->
// Partials are included with {{> name}} or {{> name class="w-full"}}.
// No dependencies: run with `node build.js` (npm run build also compiles the CSS).

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

for (const file of walk(PAGES)) {
  const raw = fs.readFileSync(file, 'utf8');
  const match = raw.match(/^<!--\s*(\{[\s\S]*?\})\s*-->\s*/);
  if (!match) throw new Error(`Missing metadata comment in ${file}`);
  const meta = JSON.parse(match[1]);

  // src/pages/about.html -> /about/ ; src/pages/index.html -> / ; src/pages/case-studies/index.html -> /case-studies/
  const rel = path.relative(PAGES, file).replace(/\\/g, '/').replace(/\.html$/, '');
  const urlPath = rel === 'index' ? '/' : `/${rel.replace(/\/?index$/, '')}/`;

  let html = layout
    .replace('{{content}}', raw.slice(match[0].length))
    .replace(/\{\{title\}\}/g, meta.title)
    .replace(/\{\{description\}\}/g, meta.description)
    .replace(/\{\{path\}\}/g, urlPath);
  html = includePartials(html);
  if (meta.nav) html = html.replace(new RegExp(`data-nav="${meta.nav}"`, 'g'), `data-nav="${meta.nav}" aria-current="page"`);

  const outFile = path.join(OUT, urlPath, 'index.html');
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, html);
  console.log(`built ${urlPath}`);
}
