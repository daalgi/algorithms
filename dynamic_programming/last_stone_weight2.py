"""
https://leetcode.com/problems/last-stone-weight-ii/

You are given an array of integers stones where stones[i] 
is the weight of the ith stone.

We are playing a game with the stones. On each turn, we 
choose any two stones and smash them together. Suppose 
the stones have weights x and y with x <= y. 
The result of this smash is:
- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, and the 
stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. 
If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array 
converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array 
converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array 
converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array 
converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
"""
from typing import List
from functools import lru_cache


def dp_memoization(stones: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(NS)
    # Space complexity: O(S)
    # where `S = sum(stones)`
    # Strategy: divide the stones into two groups such that
    # the difference of the sum of weights of each group is minimum,
    # which would be equivalent to merging the stones into 2 "giant" stones
    # and smashing them:
    # i.e. [1, 3, 2, 5]
    #   Division 1: [1], [3, 2, 5] --> abs(1 - 10) = 9
    #   Division 2: [1, 3], [2, 5] --> abs(4 - 7) = 3
    #   Division 3: [1, 3, 2], [5] --> abs(6 - 5) = 1
    # We have to explore all the combinations 2^n,
    # but we can improve the time complexity with memoization

    @lru_cache(maxsize=None)
    def dfs(index: int, sum1: int, sum2: int) -> int:
        # Depth First Search recursive function

        # Base cases
        # Out-of-bounds
        if index == n:
            return abs(sum1 - sum2)

        return min(
            # Option 1: add the current stone to `sum1`
            dfs(index + 1, sum1 + stones[index], sum2),
            # Option 2: add the current stone to `sum2`
            dfs(index + 1, sum1, sum2 + stones[index]),
        )

    n = len(stones)
    return dfs(0, 0, 0)


def dp_memoization2(stones: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(NS)
    # Space complexity: O(S)
    # where `S = sum(stones)`

    def dfs(index: int, sum1: int, sum2: int) -> int:
        # Depth First Search recursive function

        # Base cases
        # Out-of-bounds
        if index == n:
            return abs(sum1 - sum2)

        if (index, sum1) in memo:
            return memo[(index, sum1)]

        memo[(index, sum1)] = min(
            # Option 1: add the current stone to `sum1`
            dfs(index + 1, sum1 + stones[index], sum2),
            # Option 2: add the current stone to `sum2`
            dfs(index + 1, sum1, sum2 + stones[index]),
        )
        return memo[(index, sum1)]

    n = len(stones)
    memo = {}
    return dfs(0, 0, 0)


def dp_tabulation(stones: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(NS)
    # Space complexity: O(S)
    # where `S = sum(stones)`
    pass


def dp_bottom_up(stones: List[int]) -> int:
    # Dynamic programming - Bottom up
    # Time complexity: O(NS)
    # Space complexity: O(S)
    # where `S = sum(stones)`

    # Set of achievable sums
    dp = {0}
    for stone in stones:
        # `|` represents the union operation of two sets
        dp |= {stone + s for s in dp}

    # Minimum of `sum_group1 - sum_group2 = total - sum_group2 - sum_group2`
    total = sum(stones)
    return min(abs(total - s - s) for s in dp)


if __name__ == "__main__":
    print("-" * 60)
    print("Last stone weight II")
    print("-" * 60)

    test_cases = [
        ([0], 0),
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 3], 0),
        ([2, 7, 4, 1, 8, 1], 1),
        ([31, 26, 33, 21, 40], 5),
        ([31, 26, 33, 21, 40, 33, 21, 40, 33, 33, 21, 40, 33, 21, 40], 0),
    ]

    for stones, solution in test_cases:

        print("Stones:", stones)

        result = dp_memoization(stones)
        output = f"      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_memoization2(stones)
        output = f"     dp_memoization2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        # result = dp_tabulation(stones)
        # output = f"      dp_tabulation = "
        # output += " " * (10 - len(output))
        # test_ok = solution == result
        # output += str(result)
        # output += " " * (50 - len(output))
        # output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        result = dp_bottom_up(stones)
        output = f"       dp_bottom_up = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
