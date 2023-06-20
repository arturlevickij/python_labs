"""
This module provides a StoneManager class for managing stones.
"""
from manager.stone_manager import StoneManager
from models.artificial_stone import ArtificialPreciousStone
from models.decoration_stone import DecorationStone
from models.precious_stone import PreciousStone
from models.semi_precious_stone import SemiPreciousStone

if __name__ == '__main__':
    stone_manager = StoneManager()
    stone_manager.add_stone(PreciousStone("Diamond", "Blue", 10.5, 1.2, 100.5, 50))
    stone_manager.add_stone(PreciousStone("Sapphire", "White", 3.75, 1.5, 250.8, 75))
    stone_manager.add_stone(SemiPreciousStone("Ruby", "Red", 5.8, 0.8, 150, 18))
    stone_manager.add_stone(SemiPreciousStone("Stoke", "White", 5, 8.1, 100, 100))
    stone_manager.add_stone(DecorationStone("Land", "White", "Clear", 2.1, 30.6))
    stone_manager.add_stone(DecorationStone("Amethyst", "Purple", "Mat", 2.1, 30.6))
    stone_manager.add_stone(ArtificialPreciousStone("Lapis", "Blue",  "Metal", 0.95, 41.2))
    stone_manager.add_stone(ArtificialPreciousStone("Quartz", "White",  "Glass", 0.45, 11.6))

    for stone in stone_manager.stones:
        print(stone)
    print("\n")

    find_all_with_weight_greater_than = stone_manager.find_all_with_weight_greater_than(10)
    print("Stone with greater weight:")
    for stone in find_all_with_weight_greater_than:
        print(stone)
    print("\n")

    find_with_color = stone_manager.find_with_color("Blue")
    print("Stone with color:")
    for stone in find_with_color:
        print(stone)
