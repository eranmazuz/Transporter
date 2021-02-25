from django import forms
from django.core.exceptions import ValidationError

from Management.models import Route


class RouteModelForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        if Route.objects.filter(name=data).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Route already exist")
        return data

    class Meta:
        model = Route
        fields = ('name', )
        labels = {
            'name': 'Route Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                }
            )
        }


