"""
Module for the mechanism that will be used as base for all the soldiers information importing mechanisms.
"""

from abc import ABC, abstractmethod


class SoldiersImport(ABC):
    """
    Class used as base for the mechanisms of importing soldiers information.
    """

    FORMATS = []  # The formats that the mechanism can import the soldiers information from.
    def import_soldiers(self, source):
        """
        Load the soldiers information
        :param source: The soldiers information source.
        :return: The records of the soldiers information.
        """
        data = self.load_source(source) # Load the information from the source.
        data = self.pre_operations(data) # Operations on the loaded soldiers information before validation.
        self.validations(data)  # Validation of the loaded soldiers information (raise exception on failure).
        data = self.post_operations(data)  # Operations on the loaded soldiers information after validation.
        return data  # Return the loaded soldiers information.

    @abstractmethod
    def load_source(self, source):
        """
        Load the soldiers information from the source.
        :param source: The soldiers information source.
        :return: The soldiers information.
        """
        pass

    @abstractmethod
    def pre_operations(self, data):
        """
        Do operations on the soldiers information before the validation.
        :param data: The soldiers information before the operations.
        :return: The soldiers information after the operations.
        """
        pass

    @abstractmethod
    def validations(self, data):
        """
        Run validations on the soldiers information.
        :param data: The soldiers information.
        """

    @abstractmethod
    def post_operations(self, data):
        """
        Do operations on the soldiers information after the validation.
        :param data: The soldiers information before the operations.
        :return: The soldiers information after the operations.
        """
        pass
