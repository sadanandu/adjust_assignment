from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Dataset
from rest_framework import viewsets
from .serializers import DatasetSerializer


# Create your views here.

class DatasetFilter(django_filters.FilterSet):
    date = django_filters.DateRangeFilter(field_name='date', lookup_expr='')
    channel = django_filters.CharFilter(field_name='date', lookup_expr='')
    country = django_filters.CharFilter(field_name='date', lookup_expr='')
    os = django_filters.CharFilter(field_name='date', lookup_expr='')
    impressions = django_filters.NumberFilter(field_name='impressions')
    min_impressions = django_filters.NumberFilter(field_name='impressions', lookup_expr='gte')
    max_impressions = django_filters.NumberFilter(field_name='impressions', lookup_expr='lte')
    clicks = django_filters.NumberFilter(field_name='clicks')
    min_clicks = django_filters.NumberFilter(field_name='clicks', lookup_expr='gte')
    max_clicks = django_filters.NumberFilter(field_name='clicks', lookup_expr='lte')
    installs = django_filters.NumberFilter(field_name='installs')
    min_installs = django_filters.NumberFilter(field_name='installs', lookup_expr='gte')
    max_installs = django_filters.NumberFilter(field_name='installs', lookup_expr='lte')
    spend = django_filters.NumericRangeFilter(field_name='spend')
    min_spend = django_filters.NumberFilter(field_name='spend', lookup_expr='gte')
    max_spend = django_filters.NumberFilter(field_name='spend', lookup_expr='lte')

    revenue = django_filters.NumberFilter(field_name='revenue')
    min_revenue = django_filters.NumberFilter(field_name='revenue', lookup_expr='gte')
    max_revenue = django_filters.NumberFilter(field_name='revenue', lookup_expr='lte')
    class Meta:
        model = Dataset
        fields = ['date', 'installs','impressions', 'os', 'channel', 'country', \
                  'clicks', 'spend', 'revenue']


class DatasetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DatasetFilter

    
 
