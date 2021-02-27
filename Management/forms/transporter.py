from django import forms
from django.forms import formset_factory, widgets

from Management.models import Settings


class TransporterWidget(forms.MultiWidget):
    def subwidgets(self, name, value, attrs=None):
        return super().subwidgets(name, value, attrs)

    def __init__(self, *args, **kwargs):
        size = kwargs.pop('size')
        widgets = {
            'size': forms.HiddenInput(attrs={
                'value': size,
                'class': 'transporter_size'
            }),
            'value': forms.NumberInput(attrs={
                'min': 0,
                'required': True,
                'class': 'transporter_field'
            }),
            'occupied_seats': forms.HiddenInput(attrs={
                'class': 'transporter_occupied_seats'
            }),
        }
        super(TransporterWidget, self).__init__(widgets, *args, **kwargs)


    def decompress(self, value):
        if value:
            return [value[0], value[1]]
        return [None, None]

    class Media:
        js = ('js/jquery-3.0.0.js','Management/js/transporter_widget.js')


class TransporterField(forms.MultiValueField):

    def __init__(self, *args, **kwargs):
        size = kwargs.pop('size')
        fields = (
            forms.IntegerField(),
            forms.IntegerField(),
        )
        super(TransporterField, self).__init__(fields, *args, **kwargs)
        self.widget = TransporterWidget(size=size)

    def compress(self, data_list):
        return {'size': data_list[0],
                'count': data_list[1],
                'occupied_seats': data_list[0] * data_list[1]}


class TransporterForm(forms.Form):

    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True
    }))

    soldiers_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'readonly': True,
        'class': 'soldier_count'
    }))

    big_transporter = TransporterField(size=Settings.objects.get_settings().big_transporter_size)

    medium_transporter = TransporterField(size=Settings.objects.get_settings().medium_transporter_size)

    small_transporter = TransporterField(size=Settings.objects.get_settings().small_transporter_size)

    soldiers_reminder = forms.IntegerField(widget=forms.NumberInput(attrs={
        'readonly': True,
        'class': 'soldiers_remainders'
    }))


TransporterFormSet = formset_factory(TransporterForm, extra=0)


class TransporterStationForm(forms.Form):

    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True
    }))

    soldiers_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'readonly': True,
        'class': 'soldiers_count'
    }))

    seats_count = forms.IntegerField(widget=forms.NumberInput(attrs={
        'readonly': True,
        'class': 'seats_count'
    }))

    soldiers_reminder = forms.IntegerField(widget=forms.NumberInput(attrs={
        'readonly': True,
        'class': 'soldiers_remainder'
    }))
