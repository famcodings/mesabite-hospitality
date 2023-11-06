
const getauthToken = () => {
  const userStore = useUserStore()
  return userStore.user.auth_token
}

type Headers = {
  'Content-Type': string;
  Authorization?: string;
}

type BodyType = { [key: string]: any } | null;

export const baseFetch = async (
  url: string,
  method: string,
  body: BodyType = {},
  useToken: boolean = false,
  authToken: string = '',
  customHeaders: Headers = {
    'Content-Type': 'application/json'
  }
) => {

  const headers: HeadersInit = customHeaders;

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