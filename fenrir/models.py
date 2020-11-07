from django.db import models

# Create your models here.
class Rate(models.Model):
    country = models.CharField(max_length=100)
    cash_rate_buy = models.CharField(max_length=100)
    cash_rate_sell = models.CharField(max_length=100)
    realtime_rate_buy = models.CharField(max_length=100)
    realtime_rate_sell = models.CharField(max_length=100)
    added_time = models.DateTimeField(auto_now_add=True)

class TouristAttractionList(models.Model):
    url = models.CharField(unique=True, max_length=200)
    place = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    activity_time = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourist_attraction_list'