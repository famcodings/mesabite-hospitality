// When environmental variables are absent, specify the local host on port 8000.
export const baseUrl = process.env.BASE_URL || "http://localhost:8000"
export const AUTH_BASE_URL = baseUrl + '/profiles'