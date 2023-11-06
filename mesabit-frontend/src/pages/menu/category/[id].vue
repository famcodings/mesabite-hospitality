<template>
  <div class="container pt-2 mb-5 pb-5">
    <h1>
      Edit Category #{{ id }}
    </h1>
    <MenuFormsCategoryForm />
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["auth"]
})

const route = useRoute()


const id = route.params.id;

</script>
