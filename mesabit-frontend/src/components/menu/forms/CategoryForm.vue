<template>
  <div>
    <div class="my-5">
      <FieldsImageField
        v-model="form.image"
        name="image"
        id="category-image"
      />
    </div>
    <div class="my-5">
      <FieldsChoiceField
        v-model="form.folderId"
        id="category-folder-id"
        label="Folder"
        name="folderId"
        class="mb-2"
        choice-label-field="name"
        choice-value-field="id"
        :choices="categoryFolders"
        :vertical="true"
        :loading="isFetchingCategoryFolders"
      />
    </div>
    <div class="my-5">
      <FieldsInputField
        v-model="form.name"
        id="category-name"
        name="name"
        type="text"
        label="Name"
        maxlength="50"
        :vertical="true"
      />
    </div>
    <div class="my-5">
      <FieldsInputField
        v-model="form.description"
        id="category-description"
        name="description"
        type="textarea"
        label="Description"
        maxlength="50"
        :vertical="true"
      />
    </div>

    <div class="d-flex justify-content-between pt-5">
      <button class="btn btn-secondary rounded" @click="$router.back()">
        Cancel
      </button>
      <Button
        class="btn btn-primary rounded"
        type="submit"
        :loading="isSubmitting"
        @click="handleSave"
      >
        Submit
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Folder } from '~/types/folder'
import { useForm } from "vee-validate";
import { string, object } from "yup";

const props = defineProps({
  category: {
    type: Object,
    default: () => ({})
  }
})

const route = useRoute()
const toast = useToast();
const userStore = useUserStore();
const blankCategory = {
  id: null,
  name: null,
  description: null,
  image: null,
  folderId: null,
};
const form = ref({...blankCategory})
const isSubmitting = ref(false);
const isFetchingCategoryFolders = ref(false);
const defaultCategoryFolders = ref([{id: 0, name: "No Folder"}])
const categoryFolders = ref<Folder[]>([])

const { setErrors, errors, meta, validate, resetForm } = useForm({
  validationSchema: object().shape({
    name: string().required().max(50).label("Name"),
  })
});

watch(() => props.category, (newVal) => {
  setForm();  
}, {
  deep: true
});

onMounted(() => {
  fetchFolders().then(() => {
    if (Object.prototype.hasOwnProperty.call(route.query, 'folder')) {
      const folderId = route.query.folder
      form.value.folderId = folderId
    }
  })
  setForm();
});

const setForm = () => {
  if (props.category?.id) {
    resetForm({values: props.category})
    form.value.id = props.category.id;
    form.value.name = props.category.name;
    form.value.description = props.category.description;
    form.value.folderId = props.category.folder;
    form.value.image = props.category.image;
  }
}

const fetchFolders = async () => {
  isFetchingCategoryFolders.value = true
  try {
    const res = await useGetFolders();
    categoryFolders.value = res.data.results.length ? res.data.results : defaultCategoryFolders.value
    isFetchingCategoryFolders.value = false
  } catch (error) {
    toast.error("Failed to fetch category folders.")
    isFetchingCategoryFolders.value = true
  }
}

const handleSave = async () => {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  const formData = new FormData();
  formData.append("name", form.value.name);
  if (form.value.description.trim()) {
    formData.append("description", form.value.description.trim());
  }
  if (form.value.folderId) {
    formData.append("folder", form.value.folderId);
  }
  if (form.value.image !== props.category.image) {
    if (!form.value.image) {
      formData.append('image', new File([], ''));
    } else {
      formData.append("image", form.value.image);
    }
  }
  if (form.value.id) {
    updateCategory(form.value.id, formData)
  } else {
    createCategory(formData)
  }
}

const createCategory = async (category) => {
  console.log(category);
  try {
    isSubmitting.value = true
    const res = await useCreateCategory(category);
    isSubmitting.value = false
    toast.success("Category Created Successfully!")
    return navigateTo("/menu")
  } catch (error) {
    isSubmitting.value = false
    toast.error("Failed to create Category!")
  }
}

const updateCategory = async (id, category) => {
  try {
    isSubmitting.value = true
    const res = await useUpdateCategory(id, category);
    isSubmitting.value = false
    toast.success("Category Updated Successfully!")
    return navigateTo("/menu")
  } catch (error) {
    console.log(error);
    
    isSubmitting.value = false
    toast.error("Failed to update Category!")
  }
}

</script>