from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter, FilterSet
from rest_framework.filters import SearchFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_fields = ['creator',]
    # search_fields = ['status',]
    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at', 'creator',]
