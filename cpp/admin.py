from django.contrib import admin
from .models import Brand,Series,Model,UserPreference
# Register your models here.

admin.site.register(Brand)
admin.site.register(Series)
admin.site.register(Model)
admin.site.register(UserPreference)
