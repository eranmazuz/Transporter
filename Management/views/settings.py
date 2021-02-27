from django.shortcuts import render
from Management import forms
from Management.models import Settings


def settings_view(request):

    if request.method == 'GET':
        settings_form = forms.SettingsModelForm(instance= Settings.objects.get_settings())
    else:
        settings_form = forms.SettingsModelForm(request.POST, instance= Settings.objects.get_settings())

        if settings_form.is_valid():
            settings_form.save()

    return render(request, 'Management/settings/form.html', {'form' : settings_form})

