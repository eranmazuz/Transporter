from django import forms
from django.forms import inlineformset_factory

from Management.models import Station, Route

# StationFormset = modelformset_factory(
#     Station,
#     fields=('name', ),
#     extra=1,
#     widgets={
#         'name': forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     }
# )

StationFormset = inlineformset_factory(
    Route,
    Station,
    fields=('name',),
    extra=1,
    widgets={
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    }

)
