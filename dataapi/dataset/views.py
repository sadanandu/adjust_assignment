from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Dataset
from rest_framework import viewsets
from .serializers import DatasetSerializer
from django.db.models import F

# Create your views here.

class DatasetFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date')
    before_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    after_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    channel_contains = django_filters.CharFilter(field_name='channel', lookup_expr='contains')
    channel = django_filters.CharFilter(field_name='channel')
    country = django_filters.CharFilter(field_name='country')
    country_contains = django_filters.CharFilter(field_name='country', lookup_expr='contains')
    os = django_filters.CharFilter(field_name='os')
    os_contains = django_filters.CharFilter(field_name='os', lookup_expr='contains')
    impressions = django_filters.NumberFilter(field_name='impressions')
    min_impressions = django_filters.NumberFilter(field_name='impressions', lookup_expr='gte')
    max_impressions = django_filters.NumberFilter(field_name='impressions', lookup_expr='lte')
    clicks = django_filters.NumberFilter(field_name='clicks')
    min_clicks = django_filters.NumberFilter(field_name='clicks', lookup_expr='gte')
    max_clicks = django_filters.NumberFilter(field_name='clicks', lookup_expr='lte')
    installs = django_filters.NumberFilter(field_name='installs')
    min_installs = django_filters.NumberFilter(field_name='installs', lookup_expr='gte')
    max_installs = django_filters.NumberFilter(field_name='installs', lookup_expr='lte')
    spend = django_filters.NumberFilter(field_name='spend')
    min_spend = django_filters.NumberFilter(field_name='spend', lookup_expr='gte')
    max_spend = django_filters.NumberFilter(field_name='spend', lookup_expr='lte')

    revenue = django_filters.NumberFilter(field_name='revenue')
    min_revenue = django_filters.NumberFilter(field_name='revenue', lookup_expr='gte')
    max_revenue = django_filters.NumberFilter(field_name='revenue', lookup_expr='lte')

    cpi = django_filters.NumberFilter(label='cpi', method='filter_cpi')
    min_cpi = django_filters.NumberFilter(lookup_expr='gte', label='cpi', method='filter_min_cpi')
    max_cpi = django_filters.NumberFilter(lookup_expr='lte', label='cpi', method='filter_max_cpi')

    class Meta:
        model = Dataset
        fields = ['date', 'installs','impressions', 'os', 'channel', 'country', \
                  'clicks', 'spend', 'revenue', 'cpi']

    def filter_cpi(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(Dataset__cpi=F('spend')/F('installs')).filter(Dataset__cpi=value)
        return queryset

    def filter_min_cpi(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(Dataset__cpi=F('spend')/F('installs')).filter(Dataset__cpi__gte=value)
        return queryset

    def filter_max_cpi(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(Dataset__cpi=F('spend')/F('installs')).filter(Dataset__cpi__lte=value)
        return queryset


class DatasetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DatasetFilter

    
 
