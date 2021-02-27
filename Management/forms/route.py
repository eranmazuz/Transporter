from django import forms
from django.core.exceptions import ValidationError

from Management.models import Route



class RouteModelForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        if Route.objects.filter(name=data).exclude(pk=self.instance.pk).exists():
            self.add_error('name',"Route already exist")
        return data

    class Meta:
        model = Route
        fields = ('name', 'id' )
        labels = {
            'name': 'Route Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'forms-control forms-control-lg',
                }
            )
        }


