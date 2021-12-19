"""
https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of 
the symbols '+' and '-' before each integer in nums and then 
concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and 
a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, 
which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the 
sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from functools import lru_cache
from typing import List


def dp_memoization(nums: List[int], target: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(tn)
    # Space complexity: O(tn)

    @lru_cache(maxsize=None)
    def dfs(target: int, i: int) -> int:
        # Base case
        if i == n:
            # When the pointer reaches the end of the list `nums`,
            # return True if the current `target` is 0,
            # False otherwise
            return target == 0

        # Choice 1: add the current number with a negative sign `-`
        count = dfs(target - nums[i], i + 1)
        # Choice 2: add the current number with a positive sign `+`
        count += dfs(target + nums[i], i + 1)
        # Return the total number of times that `target`
        # reached `0` at the end of the list
        return count

    n = len(nums)
    return dfs(target, 0)


def dp_tabulation(nums: List[int], target: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(tn)
    # Space complexity: O(tn)
    # TODO
    pass


if __name__ == "__main__":

    print("-" * 60)
    print("Target sum")
    print("-" * 60)

    test_cases = [
        ([1], 1, 1),
        ([1], 8, 0),
        ([1, 1, 1, 1, 1], 5, 1),
        ([1, 1, 1, 1, 1], 3, 5),
        ([1, 2, 3, 54, 2, 23, 23, 3], 86, 0),
        ([1, 2, 3, 54, 2, 23, 23, 3], 13, 4),
        ([1, 2, 3, 2, 1, 23, 3], 13, 2),
    ]

    for nums, target, solution in test_cases:

        print(f"Nums: {nums}")
        print(f"Target: {target}")

        result = dp_memoization(nums, target)
        string = f"dp_memoization = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        # result = dp_tabulation(nums, target)
        # string = f" dp_tabulation = "
        # string += " " * (25 - len(string))
        # string += str(result)
        # string += " " * (60 - len(string))
        # test_ok = solution == result
        # string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(string)

        print()
