from django.db import models

# Create your models here.
class SensorData(models.Model):
    celsius = models.FloatField()
    fahrenheit = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)