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

*Recursive solutions
"""
MAX_INT = 2 ** 31 - 1


def count_ways(coins: list, target: int) -> int:
    memo = [0] * (target + 1)

    def f(coins: list, target: int) -> int:
        # Base cases
        if target == 0:
            return 1
        if target < 0:
            return 0

        # Already computed result
        if memo[target] > 0:
            return memo[target]

        count = 0
        for coin in coins:
            diff = target - coin
            if diff >= 0:
                count += f(coins, diff)

        memo[target] = count
        return count

    return f(coins, target)


def count_max_num_coins(coins: list, target: int) -> int:
    memo = [-1] * (target + 1)

    def f(coins: list, target: int) -> int:
        # Base case
        if target == 0:
            return 0

        # Already computed result
        if memo[target] >= 0:
            return memo[target]

        max_coins = -1

        # Loop over the different coins available
        for coin in coins:
            diff = target - coin
            # Skip a coin if its value is less than amount
            # remaining `diff`
            if diff >= 0:
                curr_max_coins = f(coins, diff)
                if curr_max_coins > max_coins:
                    max_coins = curr_max_coins

        # Add back the coin removed recursively
        memo[target] = max_coins + 1
        return memo[target]

    ans = f(coins, target)
    return ans if ans <= MAX_INT else -1


def count_min_num_coins(coins: list, target: int) -> int:
    memo = [-1] * (target + 1)

    def f(coins: list, target: int) -> int:
        # Base case
        if target == 0:
            return 0

        # Already computed result
        if memo[target] >= 0:
            return memo[target]

        min_coins = MAX_INT

        # Loop over the different coins available
        for coin in coins:
            diff = target - coin
            # Skip a coin if its value is greater than amount
            # remaining `diff`
            if diff >= 0:
                curr_min_coins = f(coins, diff)
                if curr_min_coins < min_coins:
                    min_coins = curr_min_coins

        # Add back the coin removed recursively
        memo[target] = min_coins + 1
        return memo[target]

    ans = f(coins, target)
    return ans if ans <= MAX_INT else -1


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

    coins = [1, 2, 5, 10, 25]
    test_cases = [
        (coins, 1),
        (coins, 2),
        (coins, 5),
        (coins, 6),
        (coins, 16),
        (coins, 26),
        (coins, 49),
        ([2, 6], 13),
        (coins, 888),
    ]

    for coins, target in test_cases:

        print("Coins:", coins, "\tTarget:", target)
        print("Number of possible change combinations", count_ways(coins, target))
        print("Minimum number of coins", count_min_num_coins(coins, target))
        print("Maximum number of coins", count_max_num_coins(coins, target))

        print()

    # print("\n>>> Custom jumps")
    # steps = 20
    # jumps = [1, 3]
    # print("\nsteps:", steps)
    # print("jumps:", jumps)
    # print("Ways count:", dp_iterative_custom_jumps(steps, jumps))
    # steps = 20
    # jumps = [3, 6]
    # print("\nsteps:", steps)
    # print("jumps:", jumps)
    # print("Ways count:", dp_iterative_custom_jumps(steps, jumps))
