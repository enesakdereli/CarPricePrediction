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

class Location(models.Model):
    city = models.CharField(max_length=200)

class Fuel(models.Model):
    fuel = models.CharField(max_length=200)
class Gear(models.Model):
    gear = models.CharField(max_length=200)
class CaseType(models.Model):
    case_type = models.CharField(max_length=200)
class EnginePower(models.Model):
    engine_power = models.CharField(max_length=200)

class UserPreference(models.Model):#bu + _list yapiyor
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.brand+"-"+self.series
