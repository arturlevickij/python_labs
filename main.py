from PreciousStone import PreciousStone

if __name__ == '__main__':
    stones = [PreciousStone.PreciousStone() for _ in range(2)]
    stones[1] = PreciousStone.PreciousStone("Diamond", 2.356, "Blue", 0.72, 29.2)
    print(stones[1].get_total_price())
    print(stones[1].increase_clarity())
    print(stones[1].increase_price(20))
    stones[1].get_instance()
    stones[1].get_instance()
    for stone in stones:
        print(stone)
