from typing import Iterable


def get_combinations(total: int, coins: list[int]) -> Iterable[list[int]]:
    if len(coins) == 1:
        if total % coins[0] == 0:
            combination = [coins[0]] * (total // coins[0])
            yield combination
        return
    new_coins = coins[1::]
    for count in range(total // coins[0] + 1):
        new_total = total - count * coins[0]
        for smaller_combination in get_combinations(new_total, new_coins):
            combination = [coins[0]] * count + smaller_combination
            yield combination


if __name__ == '__main__':
    for x in get_combinations(247, [1, 2, 5, 10, 20, 50, 100, 200]):
        print(x)
