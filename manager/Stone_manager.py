"""
This Class for managing stones.
"""


class StoneManager:
    """
    Class representing a stone manager.

    This class manages a collection of stones and provides methods for managing and querying stones.

    Attributes:
        stones (list): A list of stones managed by the manager.
    """

    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        """
        Adds a stones to the manager's collection.

        Args:
            stone (Stone): The stone to add.
        """
        self.stones.append(stone)

    def find_all_with_weight_greater_than(self, weight):
        """
        Finds stones with the greater than some weight.

        Args:
            weight (float): The weight to search for.

        Returns:
            list: A list of stones with the greater weight than.
        """
        return [stone for stone in self.stones if stone.weight_in_gram > weight]

    def find_with_color(self, color):
        """
        Finds stones with the specified color.

        Args:
            color (string): The color to search for.

        Returns:
            list: A list of stadiums with the specified color.
        """
        return [stone for stone in self.stones if stone.color == color]
