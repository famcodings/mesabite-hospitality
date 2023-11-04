// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,
  css: [
    '~/assets/css/aprycot.min.css?v=1.0.0',
    '~/assets/css/core/libs.min.css'
  ],
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        {rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css'}
      ],
      script: [
        { 
          src: '/js/core/libs.min.js',
          body: true,
         },
        { 
          src: '/js/app.js',
          body: true,
        }
      ],
    },
  },
})
