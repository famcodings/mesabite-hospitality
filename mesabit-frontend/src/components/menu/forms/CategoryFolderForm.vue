<template>
  <div>
    <div class="mb-3">
      <FieldsInputField
        v-model="form.name"
        id="category-folder-name"
        name="name"
        type="text"
        label="Name"
        maxlength="50"
        :vertical="true"
      />
    </div>
    <div class="my-5">
      <FieldsImageField
        v-model="form.image"
        name="image"
        id="category-folder-image"
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
import { ref } from "vue";
import { useForm } from "vee-validate";
import { string, object } from "yup";

const props = defineProps({
  folder: {
    type: Object,
    default: () => ({})
  }
})

const toast = useToast();
const blankCategoryFolder = {
  id: null,
  name: null,
  image: null
};
const form = ref({...blankCategoryFolder})
const isSubmitting = ref(false);

const { setErrors, errors, meta, validate, resetForm } = useForm({
  validationSchema: object().shape({
    name: string().required().max(50).label("Name"),
  })
});

watch(() => props.folder, (newVal) => {
  setForm();  
}, {
  deep: true
});

onMounted(() => {
  setForm();
});

const setForm = () => {
  if (props.folder?.id) {
    resetForm({values: props.folder})
    form.value.id = props.folder.id;
    form.value.name = props.folder.name;
    form.value.image = props.folder.image;
  }
}


const handleSave = async () => {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  const formData = new FormData();
  formData.append("name", form.value.name);
  if (form.value.image !== props.folder.image) {
    if (!form.value.image) {
      formData.append('image', new File([], ''));
    } else {
      formData.append("image", form.value.image);
    }
  }
  if (form.value.id) {
    updateFolder(form.value.id, formData)
  } else {
    createFolder(formData)
  }
}

const createFolder = async (folder) => {
  try {
    isSubmitting.value = true
    const res = await useCreateFolder(folder);
    isSubmitting.value = false
    toast.success("Folder Created Successfully!")
    return navigateTo("/menu")
  } catch (error) {
    isSubmitting.value = false
    toast.error("Failed to create Folder!")
  }
}

const updateFolder = async (id, folder) => {
  try {
    isSubmitting.value = true
    const res = await useUpdateFolder(id, folder);
    isSubmitting.value = false
    toast.success("Folder Updated Successfully!")
    return navigateTo("/menu")
  } catch (error) {
    console.log(error);
    
    isSubmitting.value = false
    toast.error("Failed to update Folder!")
  }
}

</script>