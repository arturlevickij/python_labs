"""
This module provides a Stone class for managing stones.
"""
from models.stone import Stone


class DecorationStone(Stone):
    """
        Class representing a Decoration stone.

        This class inherits from the Stone class and provides specific implementation for a
        decoration stone.

        Attributes:
            name (str): The unique name of the stone.
            color (str): The color of the stone.
            material (str): The material of the stone.
            weight_in_gram (float): The weight of the stone in grams.
            price_per_gram (float): The price per gram of the stone.
        """

    # pylint: disable=too-many-arguments
    def __init__(self, name="", color="",weight = 0, material="", price_per_gram=0, weight_in_gram=0):
        super().__init__(name, color, weight)
        self.material = material
        self.price_per_gram = price_per_gram
        self.weight_in_gram = weight_in_gram

    def get_full_price(self):
        """
            Returns a list of sports supported by the skating rink.
        """
        return self.price_per_gram * self.weight_in_gram

    def __str__(self):
        return f'{super().__str__()}, Material: {self.material}, ' \
               f'Price per carat: {self.price_per_gram}, Weight in gram: {self.weight_in_gram}'
