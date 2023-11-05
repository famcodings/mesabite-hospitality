
<template>
  <div class="field-container d-flex align-items-center" :class="{'vertical': props.vertical}">
    <span v-if="props.type === 'text' && props.maxlength" class="limit-counter">
      {{ props.modelValue ? props.modelValue.length : 0 }} / {{ props.maxlength }}
    </span>
    <label v-if="label" :for="props.id" class="label">
      {{props.label}} <span v-if="props.required" class="required-span" style="display:inline !important;">*</span>
    </label>
    <textarea
      v-if="props.type === 'textarea'"
      :id="props.id"
      v-bind="$attrs"
      :disabled="props.disabled || props.loading"
      :loading="props.loading"
      :placeholder="props.placeholder"
      :name="props.name"
      class="form-control"
      :class="{ 'is-invalid' : hasErrors }"
      :value="props.modelValue"
      @input="handleChange"
      @blur="handleBlur"
      @keydown="handleKeydown"
    ></textarea>
    <input
      v-else 
      :id="props.id"
      v-bind="$attrs"
      :disabled="props.disabled || props.loading"
      :loading="props.loading"
      :type="props.type"
      :placeholder="props.placeholder"
      :name="props.name"
      class="form-control"
      :class="{ 'is-invalid' : hasErrors }"
      :value="props.modelValue"
      :maxlength="props.maxlength"
      @input="handleChange"
      @blur="handleBlur"
      @keydown="handleKeydown"
    />
    <div v-if="props.loading" class="icon-container">
      <div class="spinner-border text-primary spinner-border-sm" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div v-if="hasErrors" class="invalid-feedback d-block">
      <span v-for="(error, errorIndex) in allErrors" :key="`error-${id}-${errorIndex}`">
        {{ error }}
      </span>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  inheritAttrs: false,
};
</script>

<script setup lang="ts">
import { useField } from "vee-validate";

const props = defineProps({
  modelValue: {
    type: [String, Number],
    default: "",
  },
  id: {
    type: String,
    required: true
  },
  label: {
    type: String,
    default: ""
  },
  loading: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  vertical: {
    type: Boolean,
    default: false
  },
  placeholder: {
    type: String,
    default: ""
  },
  type: {
    type: String,
    default: ""
  },
  maxlength: {
    type: String,
    default: ""
  },
  name: {
    type: String,
    required: true
  },
  errors: {
    type: Array,
    default: () => ([])
  },
});

const emit = defineEmits(["update:modelValue", "change"]);

const { errors: fieldErrors, handleChange: handleChangeVeeValidate, handleBlur: handleBlurVeeValidate } = useField(props.name);

const hasErrors = computed(() => {
  return (props.errors && props.errors.length) || fieldErrors.value.length; 
});
const allErrors = computed(() => {
  return [...props.errors, ...fieldErrors.value];
});

function handleChange(event) {
  emit('update:modelValue', event.target.value)
  handleChangeVeeValidate(event)
}

function handleBlur(event) {
  emit('update:modelValue', event.target.value)
  handleBlurVeeValidate(event)
}

function handleKeydown(e) {
  if (props.type === "number" && (e.key === "E" || e.key === "e" || e.key === "-" || e.key === "+" )) {
    e.preventDefault();
  }
}
</script>

<style scoped>
.field-container {
  position: relative;
}
.field-container.vertical {
  flex-direction: column;
}
.field-container .label {
  width: 30%;
  margin-bottom: 0;
}
.field-container.vertical .label {
  width: 100%;
  margin-bottom: 0.5rem;
}
.field-container:not(.d-flex) .label{
  width: 100%;
}
.field-container select[disabled] {
  cursor: not-allowed;
}
.field-container input {
  width: 100%;
}
.field-container select[loading="true"] {
  cursor: wait;
}
.field-container .icon-container {
  width: 10%;
  display: flex;
  justify-content: center;
  position: absolute;
  right: 3px;
  top: 10px;
}
.field-container:not(.d-flex) .icon-container{
  top: 27px;
  right: 15px;
}
span.limit-counter {
  position: absolute;
  bottom: -25px;
  right: 0px;
  font-size: small;
}
.invalid-feedback {
  position: absolute;
  bottom: -25px;
}
</style>