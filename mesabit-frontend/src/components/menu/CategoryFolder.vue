<template>
  <div class="card border border-primary">
    <div class="pt-2 pb-1 px-3 border-bottom border-primary">
      <div class="d-flex justify-content-between align-items-center">
        <h5 class="card-title text-primary">{{ folder.name }}</h5>
        <div>
          <button class="btn btn-icon" :disabled="isDeletingFolder" @click="handleDelete">
            <div v-if="isDeletingFolder" class="spinner-border spinner-border-sm text-primary me-1" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <i v-else class="bi bi-trash"></i>
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

const props = defineProps({
  folder: {
    type: Object,
    required: true
  }
})
const toast = useToast()
const isDeletingFolder = ref(false)

const emit = defineEmits(['deleted'])

const handleDelete = async () => {
  if (!confirm(`Are you sure you want to delete folder #${props.folder.id}?`)) {
    return
  }
  isDeletingFolder.value = true
  try {
    await useDeleteFolder(props.folder.id)
    isDeletingFolder.value = false
    console.log("emit", props.folder.id);
    
    emit("deleted", props.folder.id)
    toast.success("Folder deleted!")
  } catch (error) {
    console.log(error);
    isDeletingFolder.value = false
    toast.error("Failed to delete folder!")
  }

}

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
