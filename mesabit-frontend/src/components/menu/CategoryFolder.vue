<template>
  <div class="card border border-primary">
    <div class="pt-2 pb-1 px-3 border-bottom border-primary">
      <div class="d-flex justify-content-between align-items-center">
        <h5 class="card-title text-primary">{{ folder.name }}</h5>
        <div>
          <button class="btn btn-icon">
            <i class="bi bi-trash"></i>
          </button>
          <nuxt-link :to="`/menu/folder/${folder.id}/edit`">
            <i class="bi bi-pencil"></i>
          </nuxt-link>
        </div>
      </div>
    </div>
    <div class="card-body">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">

defineProps({
  folder: {
    type: Object,
    required: true
  }
})

</script>

<style scoped>
i {
  border: 1px solid #EA6A12;
  background-color: #EA6A12;
  color: #fff;
  border-radius: 100%;
  padding: 3px 6px;
}
</style>
