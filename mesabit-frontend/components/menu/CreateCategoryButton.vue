<template>
  <nuxt-link class="btn btn-lg border create-category-button rounded w-100 py-5 border-3" to="/menu/create-category">
    <i class="bi bi-plus-circle-dotted fs-1"></i>
    <p class="fs-4 mt-4">
      ADD NEW CATEGORY
    </p>
  </nuxt-link>
</template>

<style scoped>
.create-category-button {
  border-style: dashed !important;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
</style>