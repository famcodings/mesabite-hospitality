from rest_framework.viewsets import ModelViewSet

from mesabite.utils.viewset_mixins import GenericAuthenticatedRestMixin
from menus.models import Folder, Category
from menus.serializers import FolderSerializer, CategorySerializer


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
    exclude_filter_fields = {'image'}
