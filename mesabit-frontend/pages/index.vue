<template>
  <div class="content-inner mt-5 py-0">
    <div class="row">
      <div class="col-md-12 col-lg-12">
          <div class="card border">
            <div class="hero-image p-3" style="background: url('/images/layouts/02.jpg') no-repeat center right;background-size: cover;background-position: center;">
                <div class="card-body p-5">
                  <div class="row banner-container">
                      <div class="col-lg-8 banner-item">
                        <span class="text-primary">
                            <small>Effortless Restaurant Management</small>
                        </span>
                        <div class="banner-text pt-3">
                            <h1 class="fw-bold mb-4">
                              Welcome to the MesaBite Admin Dashboard
                            </h1>
                        </div>
                        <p class="mb-4"> Simplify your <span class="text-primary">operations, enhance efficiency, and delight </span>your customers.</p>
                      </div>
                  </div>
                </div>
            </div>
          </div>
      </div>
    </div>

    <div class="row row-cols-1 row-cols-md-4 g-4">
        <div class="col">
            <div class="card border border-primary" style="background: url('/images/layouts/01.jpg') no-repeat center right;background-size: cover;background-position: center;">
                <div class="card-body opacity-white rounded">
                    <h3 class="card-title text-black">Menu</h3>
                    <p class="card-text text-black">Effortlessly <span class="text-primary">customize, update</span>, and <span class="text-primary">optimize</span> your restaurant's menu with our user-friendly management tools.</p>
                    <nuxt-link to="/menu" class="btn btn-primary">Start Managing Now</nuxt-link>
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<style scoped>
.opacity-white {
  background: rgba(255, 255, 255, 0.84);
}
</style>
