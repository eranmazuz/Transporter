from Management.models import Settings
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class SettingsModelForm(forms.ModelForm):

    def clean_big_transporter_size(self):
        big_size = self.cleaned_data['big_transporter_size']

        return big_size

    def clean_medium_transporter_size(self):
        medium_size = self.cleaned_data['medium_transporter_size']
        big_size = self.cleaned_data['big_transporter_size']

        if big_size > medium_size:
            return medium_size

        self.add_error('medium_transporter_size', _('medium transporter must have less seats then big transporter.'))
        return medium_size

    def clean_small_transporter_size(self):
        small_size = self.cleaned_data['small_transporter_size']
        medium_size = self.cleaned_data['medium_transporter_size']
        if medium_size > small_size:
            return small_size

        self.add_error('small_transporter_size', _('small transporter must have less seats then medium transporter.'))
        return small_size





    class Meta:
        model = Settings
        fields = ['big_transporter_size', 'medium_transporter_size', 'small_transporter_size']
        labels = {
            'big_transporter_size' : _('Big Transporter'),
            'medium_transporter_size': _('Medium Transporter'),
            'small_transporter_size': _('Small Transporter'),
        }
        widgets = {
            'big_transporter_size': forms.NumberInput(attrs={
                'min' : 1
            }),
            'medium_transporter_size': forms.NumberInput(attrs={
                'min': 1
            }),
            'small_transporter_size': forms.NumberInput(attrs={
                'min': 1
            }),
        }
