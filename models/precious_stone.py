"""
This module provides a Stone class for managing stones.
"""
from models.stone import Stone


class PreciousStone(Stone):
    """
        Class representing a Precious stone.

        This class inherits from the Stone class and provides
        specific implementation for a precious stone.

        Attributes:
            name (str): The unique name of the stone.
            color (str): The color of the stone.
            carat (float): The carat of the stone.
            clarity (float): The clarity of the stone.
            weight_in_gram (float): The weight of the stone in grams.
            price_per_gram (float): The price per gram of the stone.
        """

    # pylint: disable=too-many-arguments
    def __init__(self, name="", color="", carat=0.0, clarity=0.0,
                 price_per_gram=0.0, weight_in_gram=0):
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_gram = price_per_gram
        self.weight_in_gram = weight_in_gram

    def get_total_price(self):
        """
            Returns a stones total price.
        """
        return self.price_per_gram * self.carat

    def increase_price(self, percentage):
        """
            Returns a stones increase price.
        """
        return self.get_total_price() * percentage / 100 + self.get_total_price()

    def get_full_price(self):
        """
            Returns a stones full price.
        """
        return self.price_per_gram * self.weight_in_gram

    def __str__(self):
        return f'{super().__str__()}, Carat: {self.carat} Clarity: {self.clarity}, ' \
               f'Price per carat: {self.price_per_gram}, Weight in gram: {self.weight_in_gram}'
