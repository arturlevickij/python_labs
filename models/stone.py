from abc import ABC, abstractmethod

class Stone(ABC):
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
        This method must be implemented by the subclasses.
        """
        pass
