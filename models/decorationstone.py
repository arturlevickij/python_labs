from models.stone import Stone

class DecorationStone(Stone):
    def __init__(self, name="", color="", material=""):
        """
        Parameters:
        name (str): The name of the stone.
        color (str): The color of the stone.
        material (str): The material of the stone.
        """
        super().__init__(name, color)
        self.material = material

    def __str__(self):
        return f'Name: {self.name}, Color: {self.color}, Material: {self.material}'
