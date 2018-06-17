from django.db import models

# Create your models here.

class Place(models.Model):
	place_name = models.CharField(max_length=200)
	lon = models.DecimalField(max_digits=10, decimal_places=5)
	lat = models.DecimalField(max_digits=10, decimal_places=5)
