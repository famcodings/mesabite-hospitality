<template>
  <div class="container pt-2">
    <h1 class="mb-3">
      Edit Category Folder #{{ id }}
    </h1>
    <MenuFormsCategoryFolderForm :folder="folder"/>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})

const toast = useToast()
const route = useRoute()

const id = route.params.id

const isFetchingCategoryFolder = ref(false)
const folder = ref(null)

onMounted(() => {
  getCategory()
})

const getCategory = async () => {
  isFetchingCategoryFolder.value = true
  try {
    const res = await useGetFolder(id)
    folder.value = res.data
    isFetchingCategoryFolder.value = false
  } catch (error) {
    isFetchingCategoryFolder.value = true
  }
}

</script>
