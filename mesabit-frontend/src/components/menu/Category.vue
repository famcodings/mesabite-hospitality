<template>
  <div class="card card-white dish-card profile-img mb-0 index border border-primary">
    <div class="profile-img21">
      <img :src="category.image" class="img-fluid rounded-pill avatar-170 blur-shadow position-bottom" alt="profile-image">
      <img :src="category.image" class="img-fluid rounded-pill avatar-170 " alt="profile-image">
    </div>
    <div class="card-body menu-image">
      <h5 class="heading-title fw-bolder mt-4 mb-0">{{ category.name }}</h5>
      <p class="line-clamp">
        {{ category.description }}
      </p>
      <div class="d-flex flex-row-reverse align-items-center">
        <nuxt-link :to="`/menu/category/${category.id}`">
          <i class="bi bi-pencil"></i>
        </nuxt-link>
        <button class="btn btn-icon">
          <i class="bi bi-trash"></i>
        </button>
      </div>
    </div>
  </div>  
</template>

<script setup lang="ts">

defineProps({
  category: {
    type: Object,
    required: true
  }
})

</script>

<style scoped>
.dish-card {
  margin-top: 6rem;
}

.line-clamp {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  max-height: 5em;
}
i {
  border: 1px solid #EA6A12;
  background-color: #EA6A12;
  color: #fff;
  border-radius: 100%;
  padding: 3px 6px;
}
.dish-card:hover {
  cursor: auto;
}
.dish-card:hover i {
  background-color: #fff;
  color: #EA6A12;
}
</style>