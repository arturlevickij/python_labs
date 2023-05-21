from models.stone import Stone


class PreciousStone(Stone):
    def __init__(self, name="", carat=0.0, color="", clarity=0.0, price_per_carat=0.0):
        """
        Parameters:
        name (str): The unique name of the stone.
        carat (float): The carat of the stone.
        color (str): The color of the stone.
        clarity (float): The clarity of the stone.
        price_per_carat (float): The price per carat of the stone.
        """
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def __str__(self):
        return f'Name: {self.name}, Carat: {self.carat}, Color: {self.color}, Clarity: {self.clarity}, ' \
               f'Price per Carat: {self.price_per_carat}'

    def get_total_price(self):
        return self.price_per_carat * self.carat

    def increase_price(self, percentage):
        return self.get_total_price() * percentage / 100 + self.get_total_price()
