from django.db import models
from django.utils import timezone

class Data(models.Model):
    pollution = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
