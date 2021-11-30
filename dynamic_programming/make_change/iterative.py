"""
MAKING CHANGE
Given an infinite amount of `coins` (i.e. 1, 5, 10, and 25 cents)
implement algorithms to find combinations of coins to 
sum up to a `target` change:
- Count the different combinations of change.
- Count the maximum number of coins for a given `target`.
- Count the minimum number of coins for a given `target`.
- Return all the possible combinations of coins for a given `target`.
- Return the combination of coins of maximum number of coins.
- Return the combination of coins of minimum number of coins.

*Iterative solutions
"""


def count_ways(coins: list, target: int) -> int:
    if target == 0:
        return 0

    memo = [0] * (target + 1)

    for i in range(1, target + 1):
        diff = target - i
        for coin in coins:
            if diff < coin or coin < i:
                # If the current coin adds to much to reach the 
                # target, or the current coin is less than
                # the current sum `i`, continue with next iter
                continue
            # The current sum count equals the sum
            # for `i - coin`
            memo[i] += memo[i - coin] + 1


def count_max_num_coins(coins: list, target: int) -> int:
    pass


def count_min_num_coins(coins: list, target: int) -> int:
    pass


def all_changes(coins: list, target: int) -> int:
    pass


def max_coins_change(coins: list, target: int) -> int:
    pass


def min_coins_change(coins: list, target: int) -> int:
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Making change")
    print("-" * 60)

    coins = [1, 5, 10, 25]
    test_cases = [
        (coins, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (13, 1705),
        (20, 121415),
        (25, 2555757),
    ]

    for num, solution in test_cases:

        string = f" brute_force({num}) = "
        string += " " * (25 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_recursion({num}) = "
        string += " " * (25 - len(string))
        result = dp_recursion(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_iterative({num}) = "
        string += " " * (25 - len(string))
        result = dp_iterative(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    print("\n>>> Custom jumps")
    steps = 20
    jumps = [1, 3]
    print("\nsteps:", steps)
    print("jumps:", jumps)
    print("Ways count:", dp_iterative_custom_jumps(steps, jumps))
    steps = 20
    jumps = [3, 6]
    print("\nsteps:", steps)
    print("jumps:", jumps)
    print("Ways count:", dp_iterative_custom_jumps(steps, jumps))
