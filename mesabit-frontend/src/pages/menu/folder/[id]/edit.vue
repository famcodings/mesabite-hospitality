<template>
  <div class="container pt-2">
    <h1 class="mb-3">
      Edit Category Folder #{{ id1 }}
    </h1>
    <MenuFormsCategoryFolderForm />
  </div>
</template>

<script setup lang="ts">

definePageMeta({
  middleware: ["auth"]
})

const route1 = useRoute()


const id1 = route1.params.id;

</script>
