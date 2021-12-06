from django.db import models
from location_field.models.spatial import PointField
# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    location = PointField()