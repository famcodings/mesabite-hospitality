<template>
  <div>
    <label
      class="image-label rounded d-flex align-items-center justify-content-center flex-column"
      :class="[selectedImage && 'border', fieldErrors.length && 'border-danger']"
      :style="{ backgroundImage: `url(${selectedImage})` }"
      @dragover.prevent
      @dragenter.prevent
      @dragleave.prevent
      @drop="handleDrop"
    >
      <i v-if="!selectedImage" class="bi bi-upload fs-1"></i>
      <span v-if="!selectedImage">Drag or click here to upload an image</span>
      <span v-if="!selectedImage && !required">(Optional)</span>
      <input type="file" accept="image/*" @change="handleFileSelect" ref="fileInput" class="d-none" />
      <button
        v-if="selectedImage"
        @click.prevent="clearImage"
        class="btn btn-icon btn-lg clear-image fs-3"
      >
        <i class="bi bi-x-circle-fill"></i>
      </button>
    </label>
    <div v-if="fieldErrors" class="invalid-feedback d-block">
      <span v-for="(error, errorIndex) in fieldErrors" :key="`error-${id}-${errorIndex}`">
        {{ error }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useField } from "vee-validate";

const props = defineProps({
  id: {
    type: String,
    required: true
  },
  name: {
    type: String,
    required: true
  },
  required: {
    type: Boolean,
    default: false
  },
  modelValue: {
    type: String,
    default: "",
  },
});

const emit = defineEmits(['update:modelValue'])

const selectedImage = ref(props.modelValue);

const { errors: fieldErrors, setErrors, handleChange } = useField(props.name);

watch(props, (newProps) => {
  if (newProps.modelValue !== selectedImage.value) {
    selectedImage.value = newProps.modelValue;
  }
});

const handleDrop = (event) => {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  loadImage(file);
};

const handleFileSelect = (event) => {
  const file = event.target.files[0];
  loadImage(file);
};

const loadImage = (file) => {
  if (!file) {
    if (props.required && !selectedImage.value) {
      setErrors(['Please upload an image.'])
    }
    return;
  }
  if (file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = () => {
      selectedImage.value = reader.result;
      emit('update:modelValue', selectedImage.value); // Emit the updated modelValue to the parent component
      handleChange(selectedImage.value)
    };
    reader.readAsDataURL(file);
  } else {
    alert('Please select a valid image file.');
  }
};

const clearImage = () => {
  selectedImage.value = null;
  emit('update:modelValue', null); // Emit the updated modelValue to the parent component
};
</script>

<style scoped>
.image-label {
  position: relative;
  display: block;
  height: 350px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-style: dashed;
  cursor: pointer;
}

.input-file {
  display: none;
}

.clear-image {
  position: absolute;
  top: 5px;
  right: 7px;
  color: rgb(241 134 62);
  transition: opacity 0.3s;
  cursor: pointer;
}

.clear-image:hover {
  opacity: 0.8;
}
</style>
