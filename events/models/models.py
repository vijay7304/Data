from unicodedata import name
from django.db import models

# Create your models here.

class Events(models.Model):
    event_id = models.IntegerField(default=1)
    user_id = models.IntegerField(default=1)
    email = models.CharField(max_length=10)
    mobile = models.IntegerField()
    name = models.CharField(max_length=30)
    event_time = models.CharField(max_length=30,default= "null")
    event_date = models.CharField(max_length=30,default= "null")
    event_location = models.CharField(max_length=30,default= "null")
    event_address = models.CharField(max_length=100,default= "null")
   

