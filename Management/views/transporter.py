from django.db.models import Count, Min
from django.shortcuts import render

from Management.models import Station, Transporter
from Management.mechanisms.organization import ORGANIZATIONS
from Management.forms import TransporterFormSet


def __create_transporters(transporter_data, platform, station_id):
    for transporter_number in range(1, transporter_data['count'] + 1):
        transporter = Transporter.objects.create(size=transporter_data['size_symbol'],
                                                 platform=platform,
                                                 number=transporter_number)
        occupied_seats_count = min(transporter_data['occupied_seats'], transporter_data['size'])
        transporter_data['occupied_seats'] = max(transporter_data['occupied_seats'] - transporter_data['size'], 0)
        transporter.stations.add(station_id, through_defaults={'occupied_seats': occupied_seats_count})

        platform = platform + 1
    return platform


def set_station_transporters_view(request):
    if request.method == 'GET':
        cites_soldiers_count = Station.objects.annotate(soldiers_count=Count('soldier')).values('id', 'name',
                                                                                                'soldiers_count')
        ORGANIZATIONS['AVG'](cites_soldiers_count)
        transporter_formset = TransporterFormSet(initial=cites_soldiers_count)
        return render(request, 'Management/transporter/form.html', {'formset': transporter_formset})

    transporter_formset = TransporterFormSet(request.POST)

    if not transporter_formset.is_valid():
        return render(request, 'Management/transporter/form.html', {'formset': transporter_formset})

    Transporter.objects.all().delete()
    platform = 1
    for transporter_data in transporter_formset.cleaned_data:
        transporter = transporter_data['big_transporter']
        transporter['size_symbol'] = Transporter.LARGE_TRANSPORTER
        transporter['occupied_seats'] = min(transporter_data['soldiers_count'], transporter['occupied_seats'])
        transporter_data['soldiers_count'] = transporter_data['soldiers_count'] - transporter['occupied_seats']
        platform = __create_transporters(transporter_data=transporter,
                                         platform=platform,
                                         station_id=transporter_data['id'])

        transporter = transporter_data['medium_transporter']
        transporter['size_symbol'] = Transporter.MEDIUM_TRANSPORTER
        transporter['occupied_seats'] = min(transporter_data['soldiers_count'], transporter['occupied_seats'])
        transporter_data['soldiers_count'] = transporter_data['soldiers_count'] - transporter['occupied_seats']
        platform = __create_transporters(transporter_data=transporter,
                                         platform=platform,
                                         station_id=transporter_data['id'])

        transporter = transporter_data['small_transporter']
        transporter['size_symbol'] = Transporter.SMALL_TRANSPORTER
        transporter['occupied_seats'] = min(transporter_data['soldiers_count'], transporter['occupied_seats'])
        transporter_data['soldiers_count'] = transporter_data['soldiers_count'] - transporter['occupied_seats']
        platform = __create_transporters(transporter_data=transporter,
                                         platform=platform,
                                         station_id=transporter_data['id'])

    return render(request, 'Management/transporter/form.html', {'formset': transporter_formset})


def set_transporter_stations_view(request):
    pass
