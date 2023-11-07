<template>
  <div class="container pt-2 mb-5 pb-5">
    <h1>
      Edit Category #{{ id }}
    </h1>
    <MenuFormsCategoryForm :category="category"/>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})

const toast = useToast()
const route = useRoute()

const id = route.params.id

const isFetchingCategory = ref(false)
const category = ref(null)

onMounted(() => {
  getCategory()
})

const getCategory = async () => {
  isFetchingCategory.value = true
  try {
    const res = await useGetCategory(id)
    category.value = res.data
    isFetchingCategory.value = false
  } catch (error) {
    isFetchingCategory.value = true
  }
}
</script>
