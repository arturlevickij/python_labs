from PreciousStone import PreciousStone

if __name__ == '__main__':
    stones = [PreciousStone() for _ in range(3)]
    stones[0] = PreciousStone("Diamond", 2.356, "Blue", 0.72, 29.2)
    stones[1].get_instance()
    stones[2].get_instance()
    for stone in stones:
        print(stone)

