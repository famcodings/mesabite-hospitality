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
        <input v-model.trim="search" class="form-control form-control-lg" type="text" placeholder="Search Category" @input="handleSearchInput">
      </div>
    </div>

    <div class="d-flex">
      <nuxt-link class="btn btn-text text-primary" to="/menu/create-category-folder">
        <i class="bi bi-folder-plus"></i> Create Category Folder
      </nuxt-link>

      <nuxt-link class="btn btn-text text-primary" to="/menu/create-category">
        <i class="bi bi-bookmark-plus"></i> Create Category
      </nuxt-link>
    </div>

    <div class="row  mt-3">
      <div v-for="(folder, index) in categoryFolders" :key="`folder-${index}`" class="col-12 mb-3">
        <MenuCategoryFolder :folder="folder" @deleted="handleFolderDeleted">
          <div class="row">
            <div v-for="(category, index1) in folder.categories" :key="`folder-${index}-category-${index1}`" class="col-12 col-sm-6 col-md-4 col-lg-3">
              <MenuCategory :category="category" @deleted="handleCategoryDeleted" />
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
              <MenuCreateCategoryButton :folder-id="folder.id" />
            </div>
          </div>
        </MenuCategoryFolder>
      </div>
    </div>

    <!-- End of Folders -->
    <p class="text-center"><i class="bi bi-dot end-of-folders fs-1"></i></p>

    <div class="row">
      <div v-for="(category, index) in categories" :key="`category-${index}`" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
        <MenuCategory :category="category" @deleted="handleCategoryDeleted" />
      </div>

      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <MenuCreateCategoryButton />
      </div>
    </div>

    <!-- Loading indicator -->
    <!-- <div v-if="isFetchingCategories || isFetchingCategoryFolders" class="loading-indicator">Loading...</div> -->

    <!-- End of Categories -->
    <p class="text-center"><i class="bi bi-dot end-of-categories fs-1"></i></p>
  </div>
</template>

<script setup lang="ts">
import type { Folder } from '~/types/folder'
import type { Category } from '~/types/category'

definePageMeta({
  middleware: ["auth"]
})
const toast = useToast();
const timer = ref(null);

const isFetchingCategories = ref(false)
const isFetchingCategoryFolders = ref(false)
const isCategoriesReachedEnd = ref(false)
const isCategoryFoldersReachedEnd = ref(false)
const categories = ref<Category[]>([])
const categoryFolders = ref<Folder[]>([])
const search = ref("")
const foldersPage = ref(1)
const categoriesPage = ref(1)

onMounted(() => {
  loadMoreFolders()
  loadMoreCategories()

  const endOfFoldersObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      loadMoreFolders()
    }
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.2,
  });

  const endOfCategoriesObserver = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      loadMoreCategories()
    }
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.2,
  });
  
  endOfFoldersObserver.observe(document.querySelector('.end-of-folders'));
  endOfCategoriesObserver.observe(document.querySelector('.end-of-categories'));

  onUnmounted(() => {
    endOfFoldersObserver.disconnect();
    endOfCategoriesObserver.disconnect();
  });
})

const loadMoreFolders = async () => {
  if (isFetchingCategoryFolders.value || isCategoryFoldersReachedEnd.value) return;
  isFetchingCategoryFolders.value = true;

  try {
    const res = await useGetFolders({page: foldersPage.value});
    categoryFolders.value = [...categoryFolders.value, ...res.data.results];
    if (res.data.next) {
      foldersPage.value++;
    } else {
      isCategoryFoldersReachedEnd.value = true;
    }
    isFetchingCategoryFolders.value = false;
  } catch (error) {
    isFetchingCategoryFolders.value = false;
    toast.error("Failed to fetch category folders.")
  }
};

const loadMoreCategories = async () => {
  if (isFetchingCategories.value || isCategoriesReachedEnd.value) return;
  isFetchingCategories.value = true;

  try {
    const res = await useGetCategories({
      folder__isnull: true,
      page: categoriesPage.value,
    });
    categories.value = [...categories.value, ...res.data.results];
    if (res.data.next) {
      categoriesPage.value++;
    } else {
      isCategoriesReachedEnd.value = true;
    }
    isFetchingCategories.value = false;
  } catch (error) {
    isFetchingCategories.value = false;
    toast.error("Failed to fetch categories.")
  }
};

const handleFolderDeleted = (idToRemove) => {
  categoryFolders.value = categoryFolders.value.filter(item => item.id != idToRemove)
}

const handleCategoryDeleted = (idToRemove) => {
  categories.value = categories.value.filter(item => item.id != idToRemove)
}

const debouncedSearch = async (searchValue) => {
  if (!searchValue) {
    fetchFolders()
    fetchCategories()
    return
  }
  isFetchingCategories.value = true
  try {
    const res = await useGetCategories({
      search: searchValue
    });
    categories.value = res.data.results.categories 
    categoryFolders.value = res.data.results.folders 
    isFetchingCategories.value = false
  } catch (error) {
    toast.error("Failed to fetch categories.")
    isFetchingCategories.value = true
  }
}

const handleSearchInput = () => {
  if (timer.value) {
    clearTimeout(timer.value);
  }
  
  timer.value = setTimeout(() => {
    debouncedSearch(search.value);
  }, 400);
}

</script>

<style scoped>
@media (min-width: 768px) {
  .mt-md-6rem {
    margin-top: 6rem;
  }
}

@media (max-width: 767px) {
  .hero-image::before {
    width: 100%;
  }
}

</style>
