from models.stone import Stone


class ArtificialPreciousStone(Stone):
    def __init__(self, name="", carat=0.0, color="", clarity=0.0, price_per_carat=0.0,
                 lab_name="", weight_grams=0.0, price_per_gram=0.0):
        """
        Parameters:
        name (str): The unique name of the stone.
        carat (float): The carat of the stone.
        color (str): The color of the stone.
        clarity (float): The clarity of the stone.
        price_per_carat (float): The price per carat of the stone.
        lab_name (str): The name of the laboratory.
        weight_grams (float): The weight of the stone in grams.
        price_per_gram (float): The price per gram of the stone.
        """
        super().__init__(name, carat, color, clarity, price_per_carat)
        self.lab_name = lab_name
        self.weight_grams = weight_grams
        self.price_per_gram = price_per_gram

    def __str__(self):
        return f'Name: {self.name}, Carat: {self.carat}, Color: {self.color}, Clarity: {self.clarity}, ' \
               f'Price per Carat: {self.price_per_carat}, Lab Name: {self.lab_name}, ' \
               f'Weight (grams): {self.weight_grams}, Price per Gram: {self.price_per_gram}'

    def get_full_price(self):
        return self.price_per_gram * self.weight_grams
