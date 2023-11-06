
export const useGetFolders = async () => {
  const axios = useAxios()
  const endpoint = '/menus/api/folders/'
  return await axios.get(endpoint)
}
