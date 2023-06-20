from manager.stone_manager import StoneManager


class MaterialSetManager:
    def __init__(self, regular_manager: StoneManager):
        self.regular_manager = regular_manager

    def __iter__(self):
        for stone in self.regular_manager:
            yield from stone.materials

    def __len__(self):
        return sum(len(stone.materials) for stone in self.regular_manager)

    def __getitem__(self, index):
        for stone in self.regular_manager:
            if index < len(stone.materials):
                return list(stone.materials)[index]
            index -= len(stone.materials)
        raise IndexError("Index out of range")

    def __next__(self):
        for stone in self.regular_manager:
            for material in stone.materials:
                yield material