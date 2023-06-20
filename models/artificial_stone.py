"""
This module provides a Stone class for managing stones.
"""
from models.stone import Stone


class ArtificialPreciousStone(Stone):
    """
    Class representing an Artificial precious stone.

    This class inherits from the Stone class and provides specific implementation for an
    artificial precious stone.

    Attributes:
        name (str): The unique name of the stone.
        color (str): The color of the stone.
        lab_name (str): The name of the laboratory.
        weight_in_gram (float): The weight of the stone in grams.
        price_per_gram (float): The price per gram of the stone.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name="", color="", lab_name="",
                 weight_in_gram=0.0, price_per_gram=0.0):
        super().__init__(name, color)
        self.lab_name = lab_name
        self.weight_in_gram = weight_in_gram
        self.price_per_gram = price_per_gram

    def __iter__(self):
        return iter(self.weight)

    def get_full_price(self):
        """
            Returns a list of sports supported by the skating rink.
        """
        return self.price_per_gram * self.weight_in_gram

    def __str__(self):
        return f'{super().__str__()}, Lab Name: {self.lab_name}' \
               f'Weight (grams): {self.weight_in_gram}, Price per Gram: {self.price_per_gram}'
