class StoneManager:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def find_all_with_weight_greater_than(self, weight):
        return [stone for stone in self.stones if isinstance(stone, ArtificialPreciousStone) and
                stone.weight_grams > weight]

    def find_with_legs(self):
        return [stone for stone in self.stones if isinstance(stone, PreciousStone) and stone.color == "Blue"]
