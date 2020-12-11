from django.db import models

# Create your models here.
class Info(models.Model):
    iata = models.CharField(max_length=5)
    icao = models.CharField(max_length=5)
    name= models.CharField(max_length=200)
    location= models.CharField(max_length=500)
    gps= models.CharField(max_length=200)

    def __str__(self):
        return self.iata