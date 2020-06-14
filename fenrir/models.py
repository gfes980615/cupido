from django.db import models

# Create your models here.
class Rate(models.Model):
    country = models.CharField(max_length=100)
    cash_rate_buy = models.CharField(max_length=100)
    cash_rate_sell = models.CharField(max_length=100)
    realtime_rate_buy = models.CharField(max_length=100)
    realtime_rate_sell = models.CharField(max_length=100)
    added_time = models.DateTimeField(auto_now_add=True)