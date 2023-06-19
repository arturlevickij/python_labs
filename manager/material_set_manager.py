class MaterialSetManager:
    def __init__(self, stone_manager):
        self.stone_manager = stone_manager
        self.index = 0

    def __iter__(self):
        return self

    def __len__(self):
        return sum(len(obj.data_set) for obj in self.stone_manager)

    def __getitem__(self, index):
        for obj in self.stone_manager:
            if index < len(obj.data_set):
                return list(obj.data_set)[index]
            index -= len(obj.data_set)
        raise IndexError("Index out of range")

    def __next__(self):
        sets = [stone.data_set for stone in self.stone_manager.stones]
        flattened_list = [item for item_set in sets for item in item_set]
        if self.index < len(flattened_list):
            item = flattened_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
