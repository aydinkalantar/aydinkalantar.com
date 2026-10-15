/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

// Every token resolves to a CSS variable defined in src/input.css (:root),
// so colors and fonts can be changed in one place without a rebuild of the markup.
const rgb = (name) => `rgb(var(--color-${name}) / <alpha-value>)`;

module.exports = {
  content: ['./public/**/*.html', './public/assets/main.js'],
  theme: {
    // Strict system: 1px hairlines carry depth, so shadow utilities are reduced to `none`.
    boxShadow: { none: 'none' },
    dropShadow: { none: '0 0 #0000' },

    extend: {
      colors: {
        canvas: rgb('canvas'),            // #FAFAF7 warm off-white background
        ink: {
          DEFAULT: rgb('ink'),            // #1A1A18 obsidian headings and dark surfaces
          soft: rgb('ink-soft'),          // #5C5C57 secondary text
          faint: rgb('ink-faint'),        // #8F8F88 metadata on dark surfaces
        },
        slate: { soft: rgb('slate-soft') }, // #44443F soft slate body text
        line: {
          DEFAULT: rgb('line'),           // #E5E5DF stone hairlines on canvas
          dark: rgb('line-dark'),         // #33332F hairlines on ink surfaces
        },
        accent: {
          DEFAULT: rgb('accent'),         // #A65B32 walnut / burnt sienna: interactive states only
          deep: rgb('accent-deep'),       // #8C4A26 pressed state on accent fills
        },
      },

      fontFamily: {
        heading: ['var(--font-heading)', ...defaultTheme.fontFamily.sans],  // Space Grotesk
        sans: ['var(--font-body)', ...defaultTheme.fontFamily.sans],        // Inter
      },

      fontSize: {
        'display-xl': ['clamp(2.75rem, 5vw + 1rem, 6rem)', { lineHeight: '1' }],
        'display-lg': ['clamp(2.25rem, 3.2vw + 1rem, 4rem)', { lineHeight: '1.05' }],
        'display-md': ['clamp(1.625rem, 1.4vw + 1rem, 2.25rem)', { lineHeight: '1.15' }],
        label: ['0.6875rem', { lineHeight: '1rem', letterSpacing: '0.14em' }],
      },

      maxWidth: { site: '78rem', prose: '34rem' },
      spacing: { 18: '4.5rem', 22: '5.5rem', 30: '7.5rem', 36: '9rem' },
      borderRadius: { sm: '2px' },

      transitionTimingFunction: { craft: 'cubic-bezier(.2,.7,.2,1)' },
      transitionDuration: { 400: '400ms', 900: '900ms' },
    },
  },
  plugins: [],
};
