import { AUTH_BASE_URL } from "~/settings";

export const useLogin = async (body: { email: string, password: string }) => {
  const endpoint = '/login'
  const url = AUTH_BASE_URL + endpoint
  return await baseFetch(url, 'POST', body)
}


export const useGetUser = async (token: string) => {
  const endpoint = '/details'
  const url = AUTH_BASE_URL + endpoint
  return await baseFetch(url, 'GET', {}, false, token)
}


export const useLogout = async () => {
  const userStore = useUserStore()
  const authStore = useAuthStore()
  const endpoint = '/logout'
  const url = AUTH_BASE_URL + endpoint
  const res = await baseFetch(url, 'GET', {}, true)
  authStore.setAuthenticated(false)
  authStore.$reset();
  userStore.$reset();
  return res
}



export const useUserCreate = async (body: { email: string, first_name: string, last_name: string, password: string}) => {
  const endpoint = '/register'
  const url = AUTH_BASE_URL + endpoint
  return await baseFetch(url, 'POST', body)
}
