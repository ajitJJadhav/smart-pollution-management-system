from django.db import models
from django.utils import timezone
import datetime

class Data(models.Model):
    pollution = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    # date_values = models.DateTimeField(default=datetime.datetime.now()-datetime.timedelta(days=2))

    def __str__(self):
    	return str(self.pollution) +"," +str(self.latitude) +"," + str(self.longitude) + "," + str(self.created_on.date())
