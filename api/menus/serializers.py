from rest_framework import serializers

from menus.models import Folder, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('__all__')


class FolderSerializer(serializers.ModelSerializer):
    
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Folder
        fields = ('__all__')


class FolderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Folder
        fields = ('__all__')