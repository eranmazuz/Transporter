"""
Module for the mechanism of importing the soldiers from excel File.
"""
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from pandas import DataFrame

import pandas as pd

from Management.models import City, Station

FORMATS = ["xlsx"]  # The mechanism can upload from xlsx (excel) files.

SOLDIER_ID_COLUMN_NAME = 'מספר אישי'
SOLDIER_CITY_COLUMN_NAME = 'עיר'

def __load_source(source):
    """
    Load the soldiers information from the xlsx file.m
    :param source: The xlsx file.
    :return: The soldiers information.
    """
    return pd.read_excel(source, sheet_name=0)

def __validations(data):
    """
    Run validations on the soldiers information.
    :param data: The soldiers information.
    """
    __validate_ID_duplicates(data)
    __validate_soldier_station(data)


def __validate_ID_duplicates(self, data):
    duplicates = data[self.SOLDIER_ID_COLUMN_NAME].duplicated(keep=False)

    if duplicates.any():
        grouped_duplicate = data[duplicates].groupby(self.SOLDIER_ID_COLUMN_NAME, as_index=False).size()
        message = "The following duplicate IDs found:"
        for id, duplicate_count in grouped_duplicate.values:
            message = message + '\n- %s : %s times.' % (id, duplicate_count)
        raise ValidationError(_(message))


def __validate_soldier_station(self, data: DataFrame):
    cites = City.objects.values_list('name', flat=True).union(Station.objects.values_list('name', flat=True))
    known_cites = data[self.SOLDIER_CITY_COLUMN_NAME].isin(cites)
    unknown_cites = data[~known_cites][self.SOLDIER_CITY_COLUMN_NAME]

    if unknown_cites.any():
        message = "The following Cities are not registered:"
        for unknown_city in unknown_cites.unique():
            message = message + '\n- %s.' % unknown_city
        raise ValidationError(_(message))


def __post_operations(self, data):
    """
    Do operations on the soldiers information after the validation.
    :param data: The soldiers information before the operations.
    :return: The soldiers information after the operations.
    """
    return data.to_dict('records')

def import_soldiers(source):
    """
    Load the soldiers information
    :param source: The soldiers information source.
    :return: The records of the soldiers information.
    """
    data = __load_source(source)  # Load the information from the source.
    __validations(data)  # Validation of the loaded soldiers information (raise exception on failure).
    data = __post_operations(data)  # Operations on the loaded soldiers information after validation.
    return data  # Return the loaded soldiers information.



