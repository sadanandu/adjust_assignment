from django.db import models

app_lable='dataset'

# Create your models here.
class Dataset(models.Model):
    class Meta:
        db_table= 'dataset'
        managed = False

    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    channel = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
