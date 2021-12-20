"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from functools import lru_cache
from typing import List


def brute_force(nums: List[int]) -> bool:
    # Time complexity: O(2^n),
    # Space complexity: O(n)
    pass


def dp_memoization(nums: List[int]) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n*sum)
    # Space complexity: O(n*sum)

    @lru_cache(maxsize=None)
    def dfs(sum1: int, sum2: int, i: int) -> bool:
        # Base cases
        # End of the list reached
        if i == n:
            return sum1 == sum2

        if dfs(sum1, sum2, i + 1) or dfs(sum1 - nums[i], sum2 + nums[i], i + 1):
            return True
        return False

    n = len(nums)
    return dfs(sum(nums), 0, 0)


def dp_memoization_opt1(nums: List[int]) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n*sum)
    # Space complexity: O(n*sum)
    # Optimization:
    # - If the sum of all the elements is an odd number,
    # there's no possible partition.
    # - Taken only the sum of one part of the array as an input
    # for the recursive function to reduce the state parameters
    # to only two (sum1, i) instead of three (sum1, sum2, i)

    @lru_cache(maxsize=None)
    def dfs(sum1: int, i: int) -> bool:
        # Base cases

        # End of the list reached
        if i == n:
            # Return True if the sum equal to zero,
            # which is equivalent to
            return sum1 == 0

        if dfs(sum1, i + 1) or dfs(sum1 - nums[i], i + 1):
            return True
        return False

    total = sum(nums)
    if total & 1:
        # If the total sum is an odd number,
        # there can't be a partition of equal sum
        return False

    n = len(nums)
    return dfs(total // 2, 0)


def dp_memoization_opt2(nums: List[int]) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n*sum)
    # Space complexity: O(n*sum/)
    # See dp_memoization_opt1
    # Further optimization: memoization with a
    # list of lists (matrix) instead of lru_cache or dictionary

    def dfs(sum1: int, i: int) -> bool:
        # Base cases

        # End of the list reached
        if i == n:
            # Return True if the sum equal to zero,
            # which is equivalent to
            return sum1 == 0

        if memo[i][sum1] is not None:
            return memo[i][sum1]

        if dfs(sum1, i + 1) or dfs(sum1 - nums[i], i + 1):
            memo[i][sum1] = True
            return True

        memo[i][sum1] = False
        return False

    total = sum(nums)
    if total & 1:
        # If the total sum is an odd number,
        # there can't be a partition of equal sum
        return False

    n = len(nums)
    half = total // 2
    memo = [[None] * (half + 1) for _ in range(n)]
    return dfs(half, 0)


def dp_tabulation(nums: List[int]) -> bool:
    # Dynamic programming - Tabulation
    # Time complexity: O(n*sum)
    # Space complexity: O(sum)

    total = sum(nums)

    # If the total sum is an odd number,
    # there can't be a partition of equal sum:
    #   total = 2 * half
    #   half = total / 2
    #   if all elements are integer, half can only be an integer if total is even
    if total & 1:
        return False

    # Table to store whether a sum can be achieved.
    # We only need to check if `half` can be achieved.
    half = total // 2
    dp = [False] * (half + 1)
    # Initialize the first element to True
    #   dp[0] = True (can sum = 0 be achieved? Yes)
    dp[0] = True

    # Loop over the numbers in the list
    for num in nums:
        # Loop over the possible sums,
        # from `half` to the current number `num`
        for s in range(half, num - 1, -1):
            if dp[s - num]:
                # If the current sum `s` minus the current number `num` (s - num)
                # was previously defined as True (could be achieved), then,
                # `s` can as well (s - num + num = s)
                dp[s] = True

    # Return if the sum `half` can be achieved
    return dp[half]


def bitset(nums: List[int]) -> bool:
    # Using bitset
    # Time complexity: O(n)
    # Space complexity: O(1)

    total = sum(nums)
    # If the total sum is an odd number,
    # there can't be a partition of equal sum:
    #   total = 2 * half
    #   half = total / 2
    #   if all elements are integer, half can only be an integer if total is even
    if total & 1:
        return False

    # Use a bitset to keep track of the achievable sums, i.e.
    # nums = [2, 6, 8]
    # bit index (sum of)  876543210
    #     initial state   000000001
    #           num = 2   000000101
    #           num = 6   101000101
    #           ...
    # bits (1=achievable) 101000101
    #          half = 8, 8th-bit = 1 --> True
    #
    # Initialize the bitset to `1` (sum of 0 achievable)
    # sum of     x...3210,
    # achievable 0...0001, sum of `0` (first bit) is achievable (first bit = 1)
    dp = 1
    for num in nums:
        dp |= dp << num

    half = total // 2
    return (dp >> half) & 1


if __name__ == "__main__":

    print("-" * 60)
    print("Target sum")
    print("-" * 60)

    test_cases = [
        ([1], False),
        ([1, 1], True),
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 2, 1, 3, 8, 25, 13, 89], False),
        ([1, 2, 1, 3, 8, 25, 13, 89, 1, 2, 11, 13, 18, 25, 13, 89], True),
        (
            [
                34,
                16,
                5,
                72,
                28,
                99,
                90,
                67,
                81,
                27,
                22,
                48,
                85,
                35,
                41,
                37,
                59,
                94,
                60,
                60,
                49,
                38,
                80,
                63,
                26,
                96,
                3,
                40,
                82,
                59,
                3,
                12,
                94,
                82,
                9,
                56,
                33,
                65,
                26,
                73,
                52,
                65,
                54,
                55,
                84,
                9,
                80,
                42,
                16,
                51,
                24,
                16,
                96,
                33,
                45,
                11,
                39,
                57,
                9,
                89,
                21,
                82,
                43,
                93,
                31,
                43,
                95,
                28,
                40,
                100,
                67,
                21,
                32,
                55,
                36,
                77,
                3,
                2,
                95,
                73,
                56,
                84,
                9,
                56,
                91,
                54,
                28,
                6,
                90,
                22,
                42,
                2,
                94,
                47,
                82,
                91,
                86,
                77,
                40,
                93,
            ],
            False,
        ),
    ]

    for nums, solution in test_cases:

        output = str(nums)
        if len(nums) > 20:
            output = output[:60] + "...]"
        print(output)

        result = dp_memoization(nums)
        output = f"     dp_memoization = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution is result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_memoization_opt1(nums)
        output = f"dp_memoization_opt1 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution is result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_memoization_opt2(nums)
        output = f"dp_memoization_opt2 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution is result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(nums)
        output = f"      dp_tabulation = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bitset(nums)
        output = f"             bitset = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
