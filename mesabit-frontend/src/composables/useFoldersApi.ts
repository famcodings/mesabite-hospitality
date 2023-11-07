import type { Folder } from '~/types/folder'

export const useCreateFolder = async (payload: Folder) => {
  const axios = useAxios();
  const endpoint = '/menus/api/folders/'
  return await axios.post(endpoint, payload, {
    headers: {'content-type': 'multipart/form-data'}
  })
}

export const useUpdateFolder = async (id: number, payload: Folder) => {
  const axios = useAxios();
  const endpoint = `/menus/api/folders/${id}/`
  return await axios.put(endpoint, payload, {
    headers: {'content-type': 'multipart/form-data'}
  })
}

export const useGetFolder = async (id: string) => {
  const axios = useAxios()
  const endpoint = `/menus/api/folders/${id}`
  return await axios.get(endpoint)
}


export const useGetFolders = async () => {
  const axios = useAxios()
  const endpoint = '/menus/api/folders/'
  return await axios.get(endpoint)
}


export const useDeleteFolder = async (id: string) => {
  const axios = useAxios()
  const endpoint = `/menus/api/folders/${id}`
  return await axios.delete(endpoint)
}
