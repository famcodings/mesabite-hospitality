from rest_framework import serializers

from menus.models import Folder, Category


class FolderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Folder
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('__all__')