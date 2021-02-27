from django import forms
import os.path
from django.core.exceptions import ValidationError
from django.forms import ClearableFileInput

from Management import error
from Management.mechanisms.upload import IMPORTS


class UploadForm(forms.Form):
    file = forms.FileField(widget=ClearableFileInput(attrs={'accept': ",".join(IMPORTS.keys())}))

    def clean_file(self):
        data = self.cleaned_data['file']
        extension = os.path.splitext(data.name)[1]
        self.__validate_format(extension)

        return data



    def __validate_format(self, extension):
        if extension in IMPORTS:
            return

        raise ValidationError(error.INVALID_FORMAT_MESSAGE, code=error.INVALID_FORMAT_CODE,
                              params={'format': extension})
