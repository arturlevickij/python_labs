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

    def __len__(self):
        return len(self.stones)

    def __getitem__(self, index):
        return self.stones[index]

    def __iter__(self):
        return iter(self.stones)

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
            list: A list of stones with the specified color.
        """
        return [stone for stone in self.stones if stone.color == color]

    def get_all_stones_full_price_list(self):
        """
        Get max stones weight.

        Returns:
            list: A list of stones with the specified weight.
        """
        return [stone.get_full_price() for stone in self.stones]

    def enumerated_objects(self):
        """
        Returns a concatenation of object and its index in the manager's list.

        Returns:
            list: A list of concatenated strings.
        """
        return [f'{index}: {stone}' for index, stone in enumerate(self.stones)]

    def get_zip_results(self):
        """
        Returns a combination of object and result of do_something method.

        Returns:
            list: A list of tuples containing the stone objects and their corresponding full price list.
        """
        full_price_list = self.get_all_stones_full_price_list()
        return [(stone, price) for stone, price in zip(self.stones, full_price_list)]

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes filtered by the specified data type.

        Args:
            data_type (type): The data type to filter attributes.

        Returns:
            dict: A dictionary of attributes filtered by data type.
        """
        return {attribute: type_of_attr for obj in self.stones for attribute, type_of_attr in obj.__dict__.items()
                if isinstance(type_of_attr, data_type)}

    def check_conditions(self, condition):
        """
        Checks if all objects or any object satisfies the specified condition.

        Args:
            condition (callable): The condition to check.

        Returns:
            dict: A dictionary with "all" and "any" keys indicating the result of the condition.
        """
        return {
            'all': all(condition(obj) for obj in self.stones),
            'any': any(condition(obj) for obj in self.stones)
        }

