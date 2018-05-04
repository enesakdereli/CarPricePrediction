from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    def __str__(self):
        return self.brand_name

class Series(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=200)
    def __str__(self):
        return self.series_name

class Model(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name

class UserPreference(models.Model):#bu + _list yapiyor
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.brand+"-"+self.series
