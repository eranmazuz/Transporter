from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from Management.mechanisms import IMPORTS
import os.path

from Management.models import Soldier, City
from Management.models.forms import UploadForm

SOLDIER_ID = 'מספר אישי'
SOLDIER_TAGS = 'תגיות - הוספה'
SOLDIER_FIRST_NAME = 'שם פרטי'
SOLDIER_LAST_NAME = 'שם משפחה'
SOLDIER_CITY = 'עיר'
SOLDIER_PHONE = 'טלפון'

def upload(request):
    if not request.method == 'POST' or not request.FILES['file']:
        form = UploadForm()
        return render(request, 'Management/upload.html', {'formats': ','.join(IMPORTS.keys()), 'form': form})

    form = UploadForm(request.POST, request.FILES)

    if not form.is_valid():
        return render(request, 'Management/upload.html', {'formats': ','.join(IMPORTS.keys()), 'form': form})

    source = request.FILES['file']
    extension = os.path.splitext(source.name)[1]
    import_mechanism = IMPORTS[extension]
    try:
        data = import_mechanism.import_soldiers(source)
        for soldier_data in data:
            city, _ = City.objects.get_or_create(name=soldier_data[SOLDIER_CITY])
            Soldier.objects.create(identification_number=soldier_data[SOLDIER_ID],
                                   first_name=soldier_data[SOLDIER_FIRST_NAME],
                                   last_name=soldier_data[SOLDIER_LAST_NAME],
                                   structure=soldier_data[SOLDIER_TAGS],
                                   city= city)
        return render(request, 'Management/upload.html', {'formats': ','.join(IMPORTS.keys()), 'form': form})

    except ValidationError as e:
        form.add_error('file', e.message)
        return render(request, 'Management/upload.html', {'formats': ','.join(IMPORTS.keys()), 'form': form})
