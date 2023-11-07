from menus.serializers import FolderDetailSerializer, CategorySerializer


def group_categories_based_on_folder(request, categories_queryset):
    folders = dict()
    categories = list()
    for category in categories_queryset:
        category_data = CategorySerializer(category, context={'request': request}).data
        if category.folder:
            if not category.folder.id in folders:
                folders[category.folder.id] = FolderDetailSerializer(category.folder, context={'request': request}).data
                folders[category.folder.id]['categories'] = list()
            folders[category.folder.id]['categories'].append(category_data)
        else:
            categories.append(category_data)
    return folders.values(), categories