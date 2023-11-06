// import { useAuthStore } from "~/stores/auth"
import { useUserStore } from "@/stores/user";
import { AUTH_BASE_URL } from "~/settings";


const getauthToken = () => {
  const userStore = useUserStore()
  return userStore.user.auth_token
}

type Headers = {
  'Content-Type': string;
  Authorization?: string;
}

type BodyType = { [key: string]: any } | null;


const baseFetch = async (url: string, method: string, body: BodyType = {}, useToken: boolean = false, authToken: string = '') => {

  const headers: HeadersInit = {
    'Content-Type': 'application/json'
  };

  if (authToken) {
    headers['Authorization'] = `Token ${authToken}`;
  } else if (useToken) {
    const token = getauthToken();
    headers['Authorization'] = `Token ${token}`;
  }

  const fetchOptions: RequestInit = {
    method: method,
    headers: headers,
  };

  if (method !== 'GET') {
    fetchOptions['body'] = JSON.stringify(body);
  }

  try {
    const response = await fetch(url, fetchOptions);

    if (!response.ok) {
      // Error body might not be JSON
      const errorText = await response.text();
      try {
        const errorBody = JSON.parse(errorText); // Try parsing as JSON
        return { status: response.status, body: errorBody };
      } catch {
        return { status: response.status, body: errorText }; // Not JSON, return as text
      }
    }

    const contentType = response.headers.get("Content-Type");
    let data;
    if (contentType && contentType.includes("application/json")) {
      data = await response.json();
    } else {
      // If not JSON, read as text
      data = await response.text();
    }
    return { status: response.status, body: data };

  } catch (error) {
    console.error("Network error:", error);
    return { status: 0, body: null };
  }
}


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
