"""
Module for the mechanism of importing the soldiers from excel File.
"""
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from .soldiers_import import SoldiersImport
import pandas as pd


class SoldiersImportExcel(SoldiersImport):
    FORMATS = ["xlsx"]  # The mechanism can import from xlsx (excel) files.

    SOLDIER_ID_COLUMN_NAME = 'מספר אישי' 

    def load_source(self, source):
        """
        Load the soldiers information from the xlsx file.
        :param source: The xlsx file.
        :return: The soldiers information.
        """
        return pd.read_excel(source, sheet_name=0)

    def pre_operations(self, data):
        """
        Do operations on the soldiers information before the validation.
        :param data: The soldiers information before the operations.
        :return: The soldiers information after the operations.
        """
        return data

    def validations(self, data):
        """
        Run validations on the soldiers information.
        :param data: The soldiers information.
        """
        self.__validate_ID_duplicates(data)

    def __validate_ID_duplicates(self, data):
        duplicates = data[self.SOLDIER_ID_COLUMN_NAME].duplicated(keep=False)

        if duplicates.any():
            grouped_duplicate = data[duplicates].groupby(self.SOLDIER_ID_COLUMN_NAME, as_index=False).size()
            message = "The following duplicate IDs found:"
            for id, duplicate_count in grouped_duplicate.values:
                message = message + '<br/>- %s : %s times.' % (id, duplicate_count)
            raise ValidationError(mark_safe(message))

    def post_operations(self, data):
        """
        Do operations on the soldiers information after the validation.
        :param data: The soldiers information before the operations.
        :return: The soldiers information after the operations.
        """
        return data.to_dict('records')
