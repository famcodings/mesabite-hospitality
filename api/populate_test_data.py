import random
from menus.factories import FolderFactory, CategoryFactory

FOLDER_COUNT = 10
CATEGORIES_COUNT = 10

folders = []
for _ in range(FOLDER_COUNT):
    folder = FolderFactory()
    folders.append(folder)


for _ in range(CATEGORIES_COUNT):
    CategoryFactory(folder=random.choice(folders))