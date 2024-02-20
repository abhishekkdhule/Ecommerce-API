from django.db import models

# Create your models here.
class Address(models.Model):
    #TODO: from zipcode, country, state, city should be filled in automatically
    state = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    country = models.CharField(max_length=125)
    zipcode = models.IntegerField()



