<template>
  <nuxt-link
    class="btn btn-lg border create-category-button rounded py-5 border-3"
    :to="`/menu/create-category${folderId ? `?folder=${folderId}` : ''}`"
  >
    <i class="bi bi-plus-circle-dotted fs-1"></i>
    <p class="fs-4 mt-4">
      ADD NEW CATEGORY
    </p>
  </nuxt-link>
</template>

<script setup lang="ts">
defineProps({
  folderId: {
    type: Number,
    default: null
  }
})
</script>

<style scoped>
.create-category-button {
  border-style: dashed !important;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin-top: 75px;
  height: 300px;
}
</style>