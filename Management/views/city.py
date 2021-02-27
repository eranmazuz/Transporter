from django.shortcuts import render
from Management.forms import CityFormSet

def city_for_station_view(request):
    if request.method == 'GET':
        city_formset = CityFormSet()
        return render(request, "Management/city/list.html", {'formset' : city_formset})

    city_formset = CityFormSet(request.POST)

    if city_formset.is_valid():
        city_formset.save()

    return render(request, "Management/city/list.html", {'formset': city_formset})
