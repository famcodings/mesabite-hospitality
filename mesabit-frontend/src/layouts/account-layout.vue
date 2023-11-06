<template>
  <div class="wrapper">
    <section class="container-fluid bg-circle-login">
      <div class="row align-items-center">
        <div class="col-md-12 col-lg-7 col-xl-4">
          <slot/>
        </div>
        <div class="col-md-12 col-lg-5 col-xl-8 d-lg-block d-none vh-100 overflow-hidden">
          <img src="~/assets/images/auth/09.png" class="img-fluid sign-in-img" alt="images">
        </div>
      </div>
    </section>
  </div>
</template>
