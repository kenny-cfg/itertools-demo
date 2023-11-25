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
    combinations = (
        combination
        for size in range(len(coins_to_choose_from))
        for combination in set(itertools.combinations(coins_to_choose_from, size))
    )
    max_length = 0
    combinations_considered = 0
    for combination in combinations:
        if len(combination) > max_length:
            max_length = len(combination)
            print(f'Combination of size {max_length}')
        combinations_considered += 1
        if combinations_considered > 150:
            print(f'{combinations_considered} combinations considered')
        if sum(combination) != total:
            continue
        yield list(combination)


if __name__ == '__main__':
    for x in get_combinations(247, [1, 2, 5, 10, 20, 50, 100, 200]):
        print(x)
