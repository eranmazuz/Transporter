from django import forms

from Management.models import City
#
#
# class CityForm(forms.ModelForm):
#
#     class Meta:
#         model = City

CityFormSet = forms.modelformset_factory(City, fields=('name', 'station', 'id'), can_delete=True)
