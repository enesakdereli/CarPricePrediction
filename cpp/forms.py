from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserPreference, Brand, Model, Series

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ('brand', 'series', 'model')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['series'].queryset = Series.objects.none()
        self.fields['model'].queryset = Model.objects.none()
        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                #series_id = int(self.data.get('series'))
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
        