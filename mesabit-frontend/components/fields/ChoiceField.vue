<template>
  <div class="field-container d-flex align-items-center" :class="{'vertical': props.vertical}">
    <label v-if="label" :for="props.id" class="label">
      {{props.label}} <span v-if="props.required" class="required-span" style="display:inline !important;">*</span>
    </label>
    <select 
      :id="props.id"
      :required="props.required"
      :disabled="props.disabled || props.loading"
      :loading="props.loading"
      :value="modelValue"
      class="form-control form-select"
      :class="{ 'is-invalid' : hasErrors }"
      @input="handleChange"
      @change="emit('change', $event.target.value)"
    >
      <option
        v-for="choice in choices"
        :key="props.id + '-' + choice.id"
        :value="choice[choiceValueField]"
      >
        {{ choice[choiceLabelField] ? choice[choiceLabelField] : choice }}
      </option>
    </select>
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


<script>
export default {
  inheritAttrs: false,
};
</script>


<script setup>
import { computed } from "vue";
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
  name: {
    type: String,
    required: true
  },
  label: {
    type: String,
    default: ""
  },
  choices: {
    type: Array,
    default: () => ([])
  },
  choiceLabelField: {
    type: String,
    default: ""
  },
  choiceValueField: {
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
  errors: {
    type: Array,
    default: () => ([])
  },
});

const emit = defineEmits(["update:modelValue", "change"]);

const { errors: fieldErrors, handleChange: handleChangeVeeValidate } = useField(props.name);

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
.field-container select {
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
</style>