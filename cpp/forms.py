from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CarProperties, Brand, Model, Series
from django.forms import ModelForm, RadioSelect
from django.core import serializers
import inspect

CAR_DETAIL_CHOICES = [(0, 'Unavailable'), (1, 'Available'), (2, 'Unimportant')]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PricePredictionForm(ModelForm):
    class Meta:
        model = CarProperties
        fields=[f.name for f in model._meta.get_fields()][1:]#or [1:] ?
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        radio_fields = [f.name for f in CarProperties._meta.get_fields()][13:]
        for field in radio_fields:
            self.fields[field].widget = forms.RadioSelect(choices=CAR_DETAIL_CHOICES)
        self.fields['series'].queryset = Series.objects.none()
        self.fields['model'].queryset = Model.objects.none()
        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['series'].queryset = Series.objects.filter(brand_id=brand_id).order_by('series_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['series'].queryset = self.instance.brand.series_set.order_by('series_name')

        if 'series' in self.data:
            try:
                series_id = int(self.data.get('series'))
                self.fields['model'].queryset = Model.objects.filter(series_id=series_id).order_by('model_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.series.model_set.order_by('model_name')