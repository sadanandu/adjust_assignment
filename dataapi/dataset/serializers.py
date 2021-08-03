from .models import Dataset
from rest_framework import serializers

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Dataset
        fields = '__all__'
