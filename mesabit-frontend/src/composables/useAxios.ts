import axios from 'axios'
import { baseUrl } from "~/settings";

const getauthToken = () => {
  const userStore = useUserStore()
  return userStore.user.auth_token
}

export default function () {
  const token = getauthToken();
  const instance = axios.create({
    baseURL: baseUrl,
    headers: {'Authorization': `Token ${token}`}
  });
  return instance
}