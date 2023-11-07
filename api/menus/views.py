from rest_framework.viewsets import ModelViewSet

from mesabite.utils.viewset_mixins import GenericAuthenticatedRestMixin
from menus.models import Folder, Category
from menus.serializers import FolderSerializer, CategorySerializer
from menus.utils.categories import group_categories_based_on_folder


class FolderViewset(GenericAuthenticatedRestMixin, ModelViewSet):
    """
    A viewset to perform CRUD of Folder instances.
    """

    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    model = Folder
    exclude_filter_fields = {'image'}


class CategoryViewset(GenericAuthenticatedRestMixin, ModelViewSet):
    """
    A viewset to perform CRUD of Category instances.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category

    filterset_fields = {
        'id': ["exact", "in"],
        'name': ["exact", "in"],
        'folder': ["exact", "isnull"],
    }
    
    def list(self, request, *args, **kwargs):
        search_term = self.request.query_params.get('search')
        response = super().list(request, *args, **kwargs)
        if search_term:
            categories_queryset = self.filter_queryset(self.get_queryset()).select_related('folder')
           
            # Group Searched Categories based on folders
            folders, categories = group_categories_based_on_folder(request, categories_queryset)
            
            response.data['results'] = dict()
            response.data['results']['folders'] = folders
            response.data['results']['categories'] = categories
        return response