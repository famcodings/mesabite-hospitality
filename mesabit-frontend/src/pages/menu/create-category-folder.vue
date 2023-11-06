<template>
  <div class="container pt-2">
    <h1>
      Create New Category Folder
    </h1>
    <p class="mb-4">Here you can create new Category Folders that <b>icludes other categories under it.</b></p>
    <MenuFormsCategoryFolderForm />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})
</script>
