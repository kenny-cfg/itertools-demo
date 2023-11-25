from typing import Iterable


def get_combinations(total: int, coins: list[int]) -> Iterable[list[int]]:
    if len(coins) == 1:
        candidates = [
            coins * count
            for count in range(total // coins[0] + 1)
        ]
        for solution in filter(lambda candidate: sum(candidate) == total, candidates):
            yield solution
        return
    for coin in [coin for coin in coins if coin <= total]:
        new_coins = filter(lambda new_coin: new_coin <= coin, coins)
        smaller_combinations = get_combinations(total - coin, list(new_coins))
        for combo in [new_combination + [coin] for new_combination in smaller_combinations]:
            yield combo
        smaller_coins = filter(lambda new_coin: new_coin < coin, new_coins)
        for combo in get_combinations(total, list(smaller_coins)):
            yield combo
