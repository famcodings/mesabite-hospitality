<template>
  <div class="content-inner my-5 py-0">
    <div class="row">
      <div class="col-md-12 col-lg-12">
          <div class="card border">
            <div class="hero-image p-3" style="background: url('/images/layouts/01.jpg') no-repeat center right;background-size: cover;background-position: center;">
                <div class="card-body p-5">
                  <div class="row banner-container">
                      <div class="col-lg-8 banner-item">
                        <span class="text-primary">
                            <small>Streamline Your Menu Management</small>
                        </span>
                        <div class="banner-text pt-3">
                            <h1 class="fw-bold mb-4">
                              Menu
                            </h1>
                        </div>
                        <p class="mb-4">Efficiently <span class="text-primary">organize and navigate </span>your menu.</p>
                      </div>
                  </div>
                </div>
            </div>
          </div>
      </div>
    </div>

    <div class="row mb-3">
      <div class="col-md-12 col-lg-12 mb-3">
        <input class="form-control form-control-lg" type="text" placeholder="Search Category">
      </div>
    </div>

    <nuxt-link class="btn btn-text text-primary" to="/menu/create-category-folder">
      <i class="bi bi-folder-plus"></i> Create Category Folder
    </nuxt-link>

    <div class="row  mt-3">
      <div class="col-12 mb-3">
        <MenuCategoryFolder :folder="folder">
          <div class="row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
              <MenuCategory :category="category" />
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
              <MenuCategory :category="category" />
            </div>
          </div>
        </MenuCategoryFolder>
      </div>
    </div>

    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
        <MenuCategory :category="category" />
      </div>
      <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
        <MenuCategory :category="category" />
      </div>
      <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
        <MenuCategory :category="category" />
      </div>

      <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3 mt-md-6rem">
        <MenuCreateCategoryButton />
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">

const folder = {
  id: 12,
  name: "Salad",
  image: "/images/layouts/salad.jpg"
}

const category = {
  id: 13,
  name: 'Mushroom',
  image: "/images/layouts/mashrum.jpg",
  description: 'Indulge in a savory mushroom dish that harmoniously combines earthy flavors with a hint of umami. Our mushroom creation features tender, sautéed mushrooms, delicately seasoned to perfection, and served with a side of buttery garlic sauce. Indulge in a savory mushroom dish that harmoniously combines earthy flavors with a hint of umami. Our mushroom creation features tender, sautéed mushrooms, delicately seasoned to perfection, and served with a side of buttery garlic sauce. Indulge in a savory mushroom dish that harmoniously combines earthy flavors with a hint of umami. Our mushroom creation features tender, sautéed mushrooms, delicately seasoned to perfection, and served with a side of buttery garlic sauce. Indulge in a savory mushroom dish that harmoniously combines earthy flavors with a hint of umami. Our mushroom creation features tender, sautéed mushrooms, delicately seasoned to perfection, and served with a side of buttery garlic sauce.',
  folder: 23,
}

</script>

<style scoped>
@media (min-width: 768px) {
  .mt-md-6rem {
    margin-top: 6rem;
  }
}
</style>
