import type { Category } from '~/types/category'

export const useCreateCategory = async (payload: Category) => {
  const axios = useAxios();
  const endpoint = '/menus/api/categories/'
  return await axios.post(endpoint, payload, {
    headers: {'content-type': 'multipart/form-data'}
  })
}

export const useUpdateCategory = async (id: number, payload: Category) => {
  const axios = useAxios();
  const endpoint = `/menus/api/categories/${id}/`
  return await axios.put(endpoint, payload, {
    headers: {'content-type': 'multipart/form-data'}
  })
}

export const useGetCategories = async (query: {} = {}) => {
  const axios = useAxios()
  const endpoint = '/menus/api/categories/'
  return await axios.get(endpoint, { params: query })
}

export const useGetCategory = async (id: string) => {
  const axios = useAxios()
  const endpoint = `/menus/api/categories/${id}`
  return await axios.get(endpoint)
}


export const useDeleteCategory = async (id: string) => {
  const axios = useAxios()
  const endpoint = `/menus/api/categories/${id}`
  return await axios.delete(endpoint)
}
