from django.db import models

# Create your models here.

class Pizza(models.Model):
    ptype = models.CharField(max_length=70, blank=False, default='')
    size = models.CharField(max_length=70, blank=False, default='')
    toppings = models.CharField(max_length=200,blank=False, default='')