from django.db.models import Model
from django.shortcuts import render
from Management.mechanisms.upload import IMPORTS
from Management.forms import UploadForm, ValidationError
from Management.models import Soldier, Station, City
import os.path


SOLDIER_ID = 'מספר אישי'
SOLDIER_TAGS = 'תגיות - הוספה'
SOLDIER_FIRST_NAME = 'שם פרטי'
SOLDIER_LAST_NAME = 'שם משפחה'
SOLDIER_CITY = 'עיר'
SOLDIER_PHONE = 'טלפון'

def __get_soldier_station(city):
    try:
        return Station.objects.get(name=city)
    except Station.DoesNotExist:
        return City.objects.get(name=city).station

def upload_view(request):
    if request.method == "GET":
        form = UploadForm()
        return render(request, 'Management/upload/form.html', {'form': form})

    form = UploadForm(request.POST, request.FILES)

    if not form.is_valid():
        return render(request, 'Management/upload/form.html', {'form': form})

    source = request.FILES['file']
    extension = os.path.splitext(source.name)[1]
    import_mechanism = IMPORTS[extension]
    try:
        data = import_mechanism(source)
        Soldier.objects.all().delete()
        for soldier_data in data:
            city = soldier_data[SOLDIER_CITY]
            Soldier.objects.create(identification_number=soldier_data[SOLDIER_ID],
                                   first_name=soldier_data[SOLDIER_FIRST_NAME],
                                   last_name=soldier_data[SOLDIER_LAST_NAME],
                                   structure=soldier_data[SOLDIER_TAGS],
                                   city=city,
                                   station= __get_soldier_station(city))
        return render(request, 'Management/upload/form.html', {'form': form})

    except ValidationError as e:
        form.add_error('file', e.message)
        return render(request, 'Management/upload/form.html', {'form': form})

