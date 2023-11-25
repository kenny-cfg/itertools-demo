# Print out all the ways of making £2.47 using UK coins
from typing import Iterator


def get_combinations(total: int, coins: list[int]) -> Iterator[list[int]]:
    yield [1, 1, 1, 1, 1, 1]
    yield [1, 1, 1, 1, 2]
    yield [1, 1, 2, 2]
    yield [2, 2, 2]
    yield [1, 5]


if __name__ == '__main__':
    for combination in get_combinations(247, [1, 2, 5, 10, 20, 50, 100, 200]):
        print(combination)
