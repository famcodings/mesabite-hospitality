from django.db import models

from mesabite.base_models import TimeStampedModel


class Folder(TimeStampedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='folder/images/',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='category/images/',
        null=True,
        blank=True
    )
    folder = models.ForeignKey(
        Folder,
        related_name="categories",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name