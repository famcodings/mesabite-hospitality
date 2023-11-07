<template>
  <div class="card-body">
    <img src="~/assets/images/favicon.png" class="img-fluid logo-img" style="height: auto;" alt="img4">
    <h2 class="mb-2 text-center">Login</h2>
    <p class="text-center">Sign in to stay connected.</p>
    <form @submit.prevent="submitLoginForm">
      <div class="row">
        <div class="col-lg-12 mt-4">
          <FieldsInputField
            v-model="email"
            id="email"
            name="email"
            type="email"
            label="Email"
            :vertical="true"
          />
        </div>
        <div class="col-lg-12 mt-4">
          <FieldsInputField
            v-model="password"
            id="password"
            name="password"
            type="password"
            label="Password"
            :vertical="true"
          />
        </div>
        <div class="col-lg-12 d-flex justify-content-end">
          <a href="#">Forgot Password?</a>
        </div>
      </div>
      <div v-if="isError" class="mt-3">
        <div v-for="(message, index) in errorMessage" :key="`login-error-${index}`" class="alert alert-bottom alert-danger " role="alert">
          <span> {{ message }}</span>
        </div>
      </div>
      <div class="d-flex justify-content-center mt-2">
        <button type="submit" class="btn btn-primary">Login</button>
      </div>
      <p class="mt-3 text-center">
        Don't have an account? <nuxt-link to="/account/register" class="text-underline">Click here to register.</nuxt-link>
      </p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { useForm } from "vee-validate";
import { string, object } from "yup";

definePageMeta({
  layout: 'account-layout',
  middleware: ["no-auth"]
});

const authStore = useAuthStore();
const userStore = useUserStore();
const isError = ref(false)
const password = ref('');
const email = ref('');
const errorMessage = ref<string[]>([])

const { setErrors, errors, meta, validate, resetForm } = useForm({
  validationSchema: object().shape({
    email: string().email().required().max(50).label("Email"),
    password: string().required().label("Password"),
  })
});

const submitLoginForm = async () => {
  const { valid } = await validate();
  if (!valid) {
    return;
  }
  const formData = {
    username: email.value,
    password: password.value,
  }
  const res = await useLogin(formData);
  if (checkStatusOK(res.status)) {
    const authToken = res.body.token
    const userRes = await useGetUser(authToken)
    isError.value = false
    if (checkStatusOK(userRes.status)) {
      isError.value = false
      const user = userRes.body
      authStore.setAuthenticated(true)
      user.auth_token = authToken
      userStore.setUser(user)
      return navigateTo("/", { replace: true });
    } else {
      isError.value = true
      errorMessage.value = getErrorMessageArray(userRes.body)
    }
  } else {
    isError.value = true
    errorMessage.value = getErrorMessageArray(res.body)
  }
};

</script>