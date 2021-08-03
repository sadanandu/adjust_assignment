from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Dataset
from rest_framework import viewsets
from .serializers import DatasetSerializer, DatasetSerializer1
from django.db.models import F, Sum
from rest_framework.response import Response
import django_filters
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


#Dataset.objects.filter(date__lte='2017-05-31', date__gte='2017-05-01', os='ios').values('date').annotate(total_installs=Sum('installs')).order_by('date')


class DatasetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dataset.objects.all() #Dataset.objects.annotate(
    serializer_class = DatasetSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = DatasetFilter

    def list(self, request):
        q = super().get_queryset()
        qs = DatasetFilter(request.GET, queryset=q).qs
        print('**********8after filter**********8')
        print(str(qs.query))
        for each in request.query_params:
            if each == 'groupby':
                val = request.query_params[each]
                qs = qs.values(val)
                print('***********after group**************')
                print(str(qs.query))
            if each == 'total':
                val = request.query_params[each]
                if val == 'installs':
                    qs = qs.annotate(total_installs=Sum('installs'))
                    print('***********after total**************')
                    print(str(qs.query))

        d = self.get_serializer_class()(qs, many=True)
        print(d)
        
        return Response(d.data)

