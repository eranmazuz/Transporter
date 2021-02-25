from django import forms
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, redirect

from Management.models import Route, Station

class RouteModelForm(forms.ModelForm):
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
StationFormset = modelformset_factory(
    Station,
    fields=('name', ),
    extra=1,
    widgets={
        'name': forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    }

)

def create_route_with_stations(request):
    template_name = 'Management/testing.html'
    if request.method == 'GET':
        routeform = RouteModelForm(request.GET or None)
        formset = StationFormset(queryset=Station.objects.none())
    elif request.method == 'POST':
        routeform = RouteModelForm(request.POST)
        formset = StationFormset(request.POST)
        if routeform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            route = routeform.save()
            for form in formset:
                # so that `book` instance can be attached.
                station = form.save(commit=False)
                station.route = route
                station.save()
            return redirect('a3')
    return render(request, template_name, {
        'routeform': routeform,
        'formset': formset,
    })
