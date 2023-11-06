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


const handleSave = async () => {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  isSubmitting.value = true

}


</script>