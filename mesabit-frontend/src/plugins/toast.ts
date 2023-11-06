
import Toast, { type PluginOptions } from 'vue-toastification'

const options: PluginOptions = {
  timeout: 5000,
}

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(Toast, options)
})