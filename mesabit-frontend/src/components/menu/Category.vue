<template>
  <div class="card card-white dish-card category-card profile-img mb-0 index border border-primary" :class="[category.image && 'has-image']">
    <div class="profile-img21">
      <img v-if="category.image" :src="category.image" class="img-fluid rounded-pill avatar-170 blur-shadow position-bottom" alt="profile-image">
      <img v-if="category.image" :src="category.image" class="img-fluid rounded-pill avatar-170 " alt="profile-image">
    </div>
    <div class="card-body menu-image rounded">
      <div>
        <h5 class="heading-title fw-bolder mb-1" :class="[category.image && 'mt-4']">
          {{ category.name }}
        </h5>
        <p class="line-clamp" :class="[category.image && 'line-clamp-3', !category.image && 'line-clamp-6']">
          {{ category.description }}
        </p>
      </div>
      <div class="d-flex flex-row-reverse align-items-center">
        <nuxt-link :to="`/menu/category/${category.id}/edit`">
          <i class="bi bi-pencil"></i>
        </nuxt-link>
        <button class="btn btn-icon" :disabled="isDeletingCategory" @click="handleDelete">
          <div v-if="isDeletingCategory" class="spinner-border spinner-border-sm text-primary me-1" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
          <i v-else class="bi bi-trash"></i>
        </button>
      </div>
    </div>
  </div>  
</template>

<script setup lang="ts">

const props = defineProps({
  category: {
    type: Object,
    required: true
  }
})

const toast = useToast()
const isDeletingCategory = ref(false)

const emit = defineEmits(['deleted'])

const handleDelete = async () => {
  if (!confirm(`Are you sure you want to delete category #${props.category.id}?`)) {
    return
  }
  isDeletingCategory.value = true
  try {
    await useDeleteCategory(props.category.id)
    isDeletingCategory.value = false
    
    emit("deleted", props.category.id)
    toast.success("Category deleted!")
  } catch (error) {
    console.log(error);
    isDeletingCategory.value = false
    toast.error("Failed to delete category!")
  }

}

</script>

<style scoped>
.dish-card .menu-image {
  margin-top: 0 !important;
}
.category-card {
  margin-top: 75px;
  height: calc(100% - 75px) !important;
}

.category-card .card-body {
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.category-card.has-image .card-body {
  padding-top: 100px;
}

.line-clamp {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  max-height: 5em;
}
.line-clamp-3 {
  -webkit-line-clamp: 3;
  max-height: 5em;
}
.line-clamp-6 {
  -webkit-line-clamp: 6;
    max-height: 10em;
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