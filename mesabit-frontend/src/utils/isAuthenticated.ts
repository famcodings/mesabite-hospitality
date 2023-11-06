import { useUserStore } from "@/stores/user";
import { useAuthStore } from "@/stores/auth";

export const isAuthenticated = () => {
  const userStore = useUserStore();
  const authStore = useAuthStore();
  return authStore.isAuthenticated && userStore.user.auth_token !== undefined
};