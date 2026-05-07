import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://toolmixr.com',
  output: 'static',
  build: {
    inlineStylesheets: 'auto',
  },
  integrations: [sitemap()],
});
