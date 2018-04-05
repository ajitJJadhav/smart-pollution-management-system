from django.db import models
from django.utils import timezone

class Data(models.Model):
    pollution = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
    	return str(self.pollution) +"," +str(self.latitude) +"," + str(self.longitude) + "," + str(self.created_on.date())