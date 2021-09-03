from django.db import models
from location_field.models.spatial import LocationField
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='place')
    location= LocationField(based_fields=['pulchowk campus'],zoom=7,default=Point(85.3178166,27.6828417))

    def __str__(self):
        return self.name
    
