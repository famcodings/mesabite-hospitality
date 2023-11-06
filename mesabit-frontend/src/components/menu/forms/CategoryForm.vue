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
import { useForm } from "vee-validate";
import { string, object } from "yup";

const blankCategory = {
  id: null,
  name: null,
  description: null,
  image: null,
  folderId: null,
};
const form = ref({...blankCategory})
const isSubmitting = ref(false);
const categoryFolders = ref([{id: 23, name: 'Salad'}, {id: 323, name: 'Drinks'}]);
const isFetchingCategoryFolders = ref(false);


const { setErrors, errors, meta, validate, resetForm } = useForm({
  validationSchema: object().shape({
    name: string().required().max(50).label("Name"),
  })
});


async function handleSave() {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  isSubmitting.value = true
}

</script>