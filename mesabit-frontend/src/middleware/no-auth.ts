export default defineNuxtRouteMiddleware((to, from) => {
  
  if (isAuthenticated() === true) {
    return navigateTo('/')
  }
})
