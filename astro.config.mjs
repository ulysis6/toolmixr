import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://toolmixr.com',
  output: 'static',
  build: {
    inlineStylesheets: 'auto',
  },
});
