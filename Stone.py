class PreciousStone:
    def __init__(self, name, carat, color, clarity, pricepercarat):
        """
            Parameters:
            name (str): The unique name of the stone.
            carat (float): The carat of the stone.
            color (str): The color of the stone.
            clarity (float): The clarity of the stone.
            pricePerCarat (float): The rice per carat of the stone.
        """
        self.name = name
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.pricePerCarat = pricepercarat


    def __str__(self):
        return f'Name: {self.name} , Carat: {self.carat}, Color: {self.color}, Clarity: {self.clarity} ' \
           f', Price per Carat: {self.pricePerCarat}'


    def increase_clarity(self):
        self.clarity = self.clarity + 1
        return self.clarity


    def get_total_price(self):
        return self.pricePerCarat * self.carat


    def increase_price(self, percentage):
        return self.get_total_price() * percentage / 100 + self.get_total_price()
