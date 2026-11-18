// Renders the resume and CV from src/resume/*.html into PDFs under public/.
// Not part of `npm run build` (Cloudflare has no browser): run it by hand after editing,
// then commit the PDFs.  Usage: node src/gen_resume.js   (needs Playwright + Chromium)
const path = require('path');
const { chromium } = require('playwright');

const SRC = path.join(__dirname, 'resume');
const OUT = path.join(__dirname, '..', 'public');
const docs = [
  ['resume.html', 'aydin-kalantar-resume.pdf'],
  ['cv.html', 'aydin-kalantar-cv.pdf'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [src, out] of docs) {
    await page.goto('file://' + path.join(SRC, src), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({
      path: path.join(OUT, out),
      format: 'Letter',
      printBackground: true,
      preferCSSPageSize: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate:
        '<div style="width:100%;font:7pt Arial,Helvetica,sans-serif;color:#6B6B64;padding:0 0.6in;display:flex;justify-content:space-between">' +
        '<span>Aydin Kalantar · aydinkalantar.com</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    });
    console.log('wrote public/' + out);
  }
  await browser.close();
})();
