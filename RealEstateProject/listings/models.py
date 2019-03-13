from django.db import models
from datetime import datetime
from realtors.models import Realtor 

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # If the realtor is deleted then do nothing 
    title = models.CharField(max_length=200) 
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=12)
    description = models.TextField(blank=True)  # if its blank it wont give us an error
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=2)
    garage = models.IntegerField(default=0)  # 0 is a default value for garages
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')  #this goes in the main media folder of django
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  #this goes in the main media folder of django
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self): # Main Field
        return self.title






