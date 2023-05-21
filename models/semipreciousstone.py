from models.stone import Stone


class SemiPreciousStone(Stone):
    def __init__(self, name="", color="", hardness=0):
        """
        Parameters:
        name (str): The name of the stone.
        color (str): The color of the stone.
        hardness (int): The hardness of the stone.
        """
        super().__init__(name, color)
        self.hardness = hardness

    def __str__(self):
        return f'Name: {self.name}, Color: {self.color}, Hardness: {self.hardness}'
