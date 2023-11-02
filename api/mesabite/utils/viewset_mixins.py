from django.db import models

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from mesabite.utils.rest_paginator import StandardResultsSetPagination
from mesabite.utils.rest_permissions import DjangoModelPermissions


class PaginationMixin:
    pagination_class = StandardResultsSetPagination


class RestFilterMixin:
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = None
    filter_fields = None
    search_fields = None
    exclude_filter_fields = []
    
    def __init__(self, *args, **kwargs):
        super(RestFilterMixin, self).__init__(*args, **kwargs)
        if not self.filter_fields and not self.filterset_fields:
            filterable_fields = [f.name for f in self.model._meta.fields if f.name not in self.exclude_filter_fields]
            self.filterset_fields = filterable_fields
        if not self.search_fields:
            searchable_fields = [f.name for f in self.model._meta.fields if f.name not in self.exclude_filter_fields and not isinstance(f, models.ForeignKey)]
            self.search_fields = searchable_fields


class OrderingMixin:
    ordering_fields = '__all__'
    ordering = ['-id'] # Default Ordering


class AuthenticationMixin:
    permission_classes = (IsAuthenticated, )


class GenericAuthenticatedRestMixin(AuthenticationMixin, RestFilterMixin, OrderingMixin, PaginationMixin):
    pass