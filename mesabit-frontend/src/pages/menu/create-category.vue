<template>
  <div class="container pt-2 mb-5 pb-5">
    <h1>
      Add New Category
    </h1>
    <MenuFormsCategoryForm />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})
</script>
