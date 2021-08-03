from .models import Dataset
from rest_framework import serializers

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Dataset
        fields = ['date', 'installs','impressions', 'os', 'channel', 'country', \
                  'clicks', 'spend', 'revenue', 'cpi']
