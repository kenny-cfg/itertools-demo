# Print out all the ways of making £2.47 using UK coins
import itertools


def get_possible_list(total: int, coin: int) -> list[int]:
    return [coin] * (total // coin)


def get_combinations(total: int, coins: list[int]) -> list[list[int]]:
    coins_to_choose_from = [
        repeated_coin
        for coin in coins
        for repeated_coin in get_possible_list(total, coin)
    ]
    combinations = set([
        x
        for size in range(len(coins_to_choose_from))
        for x in set(itertools.combinations(coins_to_choose_from, size))
        if sum(x) == total
    ])
    return [list(x) for x in combinations]

