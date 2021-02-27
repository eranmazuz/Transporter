from django import forms

from Management.models import Route, Station

StationFormSet = forms.inlineformset_factory(parent_model=Route,
                                             model=Station,
                                             fields=('name','id'),
                                             extra=1)
