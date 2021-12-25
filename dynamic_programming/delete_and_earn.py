"""
https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums. You want to maximize the number of 
points you get by performing the following operation any number of times:

- Pick any nums[i] and delete it to earn nums[i] points. 
Afterwards, you must delete every element equal to nums[i] - 1 and every 
element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above 
operation some number of times.

Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
"""
from typing import List
from functools import lru_cache
from collections import Counter


def dp_memoization(nums: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)
    # TODO not working properly

    @lru_cache(maxsize=False)
    def dfs(i: int) -> int:
        if i >= n:
            return 0

        curr = nums[i] * count[nums[i]]
        return max(
            # Option 1: consider the current number
            curr + dfs(i + 2)
            if i + 1 < n and nums[i] + 1 == nums[i + 1]
            else dfs(i + 1),
            # Option 2: don't consider the current number
            dfs(i + 1),
        )

    count = Counter(nums)
    nums = sorted(list(set(nums)))
    n = len(nums)
    return dfs(0)


def dp_tabulation(nums: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Counter of the elements in `nums`
    count = Counter(nums)
    # Sort and remove duplicates in `nums`
    nums = sorted(list(set(nums)))

    # Table to keep track of the maximum points
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]

    for i in range(2, n + 1):
        curr = nums[i - 1] * count[nums[i - 1]]
        if nums[i - 1] == nums[i - 2] + 1:
            dp[i] = max(dp[i - 1], dp[i - 2] + curr)
        else:
            dp[i] = dp[i - 1] + curr

    return dp[-1]


def dp_tabulation_opt(nums: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(1)

    count = Counter(nums)
    nums = sorted(list(set(nums)))
    # Instead of using a table, keep track only
    # of the two previous maximum points
    prev = prev2 = 0
    n = len(nums)
    for i in range(n):
        curr = nums[i] * count[nums[i]]
        if i > 0 and nums[i] == nums[i - 1] + 1:
            prev, prev2 = max(prev2 + curr, prev), prev
        else:
            prev, prev2 = prev + curr, prev
    return prev


if __name__ == "__main__":
    print("-" * 60)
    print("Delete and earn")
    print("-" * 60)

    test_cases = [
        # (nums, solution)
        ([1], 1),
        ([3, 4, 2], 6),
        ([3, 5, 7], 15),
        ([1, 2, 3, 4, 5], 9),
        ([7, 6, 4, 3, 1], 12),
        ([1, 2, 3, 0, 2], 4),
        ([2, 2, 3, 3, 3, 4], 9),
        ([3, 2, 1, 5, 6, 6, 6, 6], 28),
    ]

    for nums, solution in test_cases:

        output = f"Nums: {nums}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        # result = dp_memoization([*nums])
        # output = f"\t     dp_memoization = "
        # output += " " * (10 - len(output))
        # test_ok = solution == result
        # output += str(result)
        # output += " " * (55 - len(output))
        # output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        result = dp_tabulation([*nums])
        output = f"\t      dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt([*nums])
        output = f"\t  dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
