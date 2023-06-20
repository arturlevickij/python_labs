"""
The module that contains the Stone class is an abstract class that represents a stone.
"""
from abc import ABC, abstractmethod


class Stone(ABC):
    """
        Abstract base class representing a stone.

        This class defines the common attributes and methods that are
        expected to be implemented by concrete stones

        Attributes:
        name (str): The name of the stone.
        color (str): The color of the stone.
        """

    def __init__(self, name="", color=""):
        """
        Parameters:
        name (str): The name of the stone.
        color (str): The color of the stone.
        """
        self.name = name
        self.color = color


    @abstractmethod
    def get_full_price(self):
        """
        Abstract method to get the full price of the stone.
        """

    def do_something(self):
        pass

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __str__(self):
        return f"Name - {self.name}, Color = {self.color}"