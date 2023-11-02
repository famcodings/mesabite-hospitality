from django.urls import include, path
from rest_framework import routers

from menus import views

router = routers.DefaultRouter()
router.register(r'folders', views.FolderViewset)
router.register(r'categories', views.CategoryViewset)


urlpatterns = [
    path('api/', include(router.urls), name="menus_rest_api"),
]