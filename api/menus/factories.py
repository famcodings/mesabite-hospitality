import factory
from factory.django import DjangoModelFactory

from menus.models import Folder, Category


class FolderFactory(DjangoModelFactory):
    class Meta:
        model = Folder

    name = factory.Faker("first_name")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    folder = factory.SubFactory(FolderFactory)
    name = factory.Faker("first_name")
    description = factory.Faker(
        "sentence",
        nb_words=5,
        variable_nb_words=True
    )