"""
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, 
you are initially positioned at the first index 
of the array.

Each element in the array represents your maximum 
jump length at that position.

Your goal is to reach the last index in the minimum 
number of jumps.

You can assume that you can always reach the 
last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the 
last index is 2. Jump 1 step from index 0 to 1, 
then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""
from typing import List
from functools import lru_cache


def brute_force(nums: List[int]) -> int:
    # Brute force
    # Time complexity: O(n!)
    # Space complexity: O(n)
    # at each index `i` we have `n-i` choices:
    # O(n * (n-1) * (n-2) ... 1) = O(n!)
    pass


def dp_recursion(nums: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n²)
    # Space complexity: O(n)

    @lru_cache(maxsize=None)
    def dfs(i: int) -> int:
        # Base cases
        # Last element reached
        if i == size - 1:
            return 0
        # Last element passed
        if i >= size or nums[i] == 0:
            return float("inf")

        return min(1 + dfs(i + x) for x in range(1, nums[i] + 1) if x > 0)

    size = len(nums)

    # Call the recursivee function from index 0
    return dfs(0)


def dp_iter(nums: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n)
    n = len(nums)
    # DP table
    dp = [float("inf")] * n
    # Base case: zero jumps to the first element (index 0)
    dp[0] = 0
    # Loop over the elements of `nums`
    for i in range(n):
        # If the current jump is 0, skip it
        if nums[i] == 0:
            continue
        # Loop over the possible jumps from the current element
        for inc in range(1, nums[i] + 1):
            new_i = i + inc
            if new_i < n:
                # Minimum jumps to get to `new_i`
                dp[new_i] = min(dp[new_i], dp[i] + 1)

    return dp[-1]


def greedy(nums: List[int]) -> int:
    # Greedy
    # Time complexity: O(n)
    # Space complexity: O(1)

    n = len(nums)
    # Edge case
    if n == 1:
        return 0

    # Two pointer to keep track of the range of steps
    # reachable at each iteration
    left, right = 0, nums[0]

    # Parameter to keep track of the number of jumps
    jumps = 1

    while right < n - 1:
        jumps += 1
        furthest = max([i + nums[i] for i in range(left, right + 1)])
        left, right = right, furthest

    return jumps


if __name__ == "__main__":
    print("-" * 60)
    print("Jump game")
    print("-" * 60)

    test_cases = [
        ([2], 0),
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([2, 3, 0, 1, 4, 5, 1], 3),
        ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

        result = dp_recursion(nums)
        output = f"     dp_recursion = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter(nums)
        output = f"          dp_iter = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = greedy(nums)
        output = f"           greedy = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
