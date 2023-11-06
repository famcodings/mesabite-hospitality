<template>
  <div class="d-flex justify-content-center mb-0">
    <div class="card-body mt-5">
        <img src="~/assets/images/favicon.png" class="img-fluid logo-img" alt="img5">
        <h2 class="mb-2 text-center">Register</h2>
        <p class="text-center">Create your account.</p>
        <form @submit.prevent="submitRegistrationForm">
          <div class="row">
              <div class="col-lg-6 mb-5">
                <FieldsInputField
                  v-model="firstName"
                  id="firstName"
                  name="firstName"
                  type="text"
                  label="First Name"
                  :vertical="true"
                />
              </div>
              <div class="col-lg-6 mb-5">
                <FieldsInputField
                  v-model="lastName"
                  id="lastName"
                  name="lastName"
                  type="text"
                  label="Last Name"
                  :vertical="true"
                />
              </div>
              <div class="col-lg-6 mb-5">
                <FieldsInputField
                  v-model="email"
                  id="email"
                  name="email"
                  type="email"
                  label="Email"
                  :vertical="true"
                />
              </div>
              <div class="col-lg-6 mb-5">
                <FieldsInputField
                  v-model="password"
                  id="password"
                  name="password"
                  type="password"
                  label="Password"
                  :vertical="true"
                />
              </div>
              <div class="col-lg-6 mb-5">
                <FieldsInputField
                  v-model="confirmPassword"
                  id="confirmPassword"
                  name="confirmPassword"
                  type="password"
                  label="Confirm Password"
                  :vertical="true"
                />
              </div>
          </div>
          <div v-if="isError" class="mt-3">
            <div v-for="(message, index) in errorMessage" :key="`login-error-${index}`" class="alert alert-bottom alert-danger " role="alert">
              <span> {{ message }}</span>
            </div>
          </div>
          <div class="d-flex justify-content-center mt-3">
              <Button type="submit" :loading="isSubmitting" class="btn btn-primary">Register</Button>
          </div>
          <p class="mt-3 text-center">
              Already have an Account? <nuxt-link href="/account/login" class="text-underline">Login</nuxt-link>
          </p>
        </form>
    </div>
  </div>    
</template>

<script setup lang="ts">
import { useForm } from "vee-validate";
import { string, object, ref as yupRef} from "yup";

definePageMeta({
  layout: 'account-layout',
  middleware: ["no-auth"]
});

const firstName = ref('')
const lastName = ref('')
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const isError = ref(false)
const isSuccess = ref(false)
const isSubmitting = ref(false)
const errorMessage = ref<string[]>([])

const { setErrors, errors, meta, validate, resetForm } = useForm({
  validationSchema: object().shape({
    firstName: string().required().max(50).label("First Name"),
    lastName: string().required().max(50).label("Last Name"),
    email: string().email().required().max(50).label("Email"),
    password: string().required().max(32).label("Password"),
    confirmPassword: string()
    .oneOf([yupRef('password'), null], 'Passwords must match')
    .required('Confirm password is required'),
  })
});

const submitRegistrationForm = async () => {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  const formData = {
    last_name: lastName.value,
    first_name: firstName.value,
    email: email.value,
    password: password.value,
  }
  isSubmitting.value = true
  const res = await useUserCreate(formData)
  isSubmitting.value = false
  if (checkStatusOK(res.status)) {
    isSuccess.value = true
    isError.value = false
    await navigateTo("/account/login");
  } else {
    isError.value = true
    isSuccess.value = false
    errorMessage.value = getErrorMessageArray(res.body)
  }
};
</script>