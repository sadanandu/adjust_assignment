from .models import Dataset
from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Dataset
        fields = ['date', 'installs', 'impressions', 'os', 'channel', 'country', \
                    'clicks', 'spend', 'revenue', 'cpi']

class DatasetSerializer1(serializers.ModelSerializer):
    #total_impressions = serializers.IntegerField()
    total_installs = serializers.IntegerField()
    #total_clicks = serializers.IntegerField()
    #total_spend = serializers.IntegerField()
    #total_revenue = serializers.IntegerField()

    class Meta:
        model=Dataset
        fields = ['date', 'total_installs']
