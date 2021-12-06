"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses 
along a street. Each house has a certain amount of 
money stashed. All houses at this place are arranged 
in a circle. That means the first house is the neighbor 
of the last one. Meanwhile, adjacent houses have a 
security system connected, and it will automatically 
contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount of 
money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and 
then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then 
rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


def bf_recursion(nums: list) -> int:
    # Brute force with recursion
    # Time complexity: O(2^n)
    # We have two choices for each house (rob or not):
    # 2 * 2 * ... = 2^n
    # Space complexity: O(n)
    # Max depth of the stack: n

    def recursion(start: int, end: int) -> int:
        # Recursive function

        # Base case
        if start >= end:
            return 0

        return max(
            # - don't rob the current house, go for the next one
            recursion(start + 1, end),
            # - rob the current house, skip the next one
            nums[start] + recursion(start + 2, end),
        )

    size = len(nums)
    # If there're only 1 or 2 houses, can't rob them
    if size < 3:
        return 0

    # Call the recursive function.
    # Since the first and the last houses can be considered
    # as adjacent houses, we can solve two problems:
    # - houses from 0 to  n-1
    # (including the first but not the last)
    # - houses from 1 to n
    # (including the last but not the first)
    return max(
        # first, not last
        recursion(0, size - 1),
        # last, not first
        recursion(1, size),
    )


def dp_recursion(nums: list) -> int:
    # Dynamic programming with memoization (recursive)
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Same as in the brute force algorithm, but now using
    # memoization to avoid repeated computations.

    def recursion(start: int, end: int, memo: list) -> int:
        # Recursive function

        # Base case
        if start >= end:
            return 0

        # Check if the result has been already computed
        if memo[start] is not None:
            return memo[start]

        # Max of the current house
        memo[start] = max(
            recursion(start + 1, end, memo),
            nums[start] + recursion(start + 2, end, memo),
        )
        return memo[start]

    size = len(nums)
    # If there're only 1 or 2 houses, can't rob them
    if size < 3:
        return 0

    # Call the recursive function.
    # Since the first and the last houses can be considered
    # as adjacent houses, we can solve two problems:
    # - houses from 0 to  n-1
    # (including the first but not the last)
    # - houses from 1 to n
    # (including the last but not the first)
    return max(
        # first, not last
        recursion(0, size - 1, memo=[None] * size),
        # last, not first
        recursion(1, size, memo=[None] * size),
    )


def dp_iter(nums: list) -> int:
    # Dynamic programming with tabulation (iterative)
    # Time complexity: O(n)
    # Space complexity: O(n)

    size = len(nums)
    # If there're only 1 or 2 houses, can't rob them
    if size < 3:
        return 0

    def solve(start: int, end: int) -> int:
        # Table to store the results from the bottom up.
        # Each element represents the maximum robbed possible
        # value considering the previous houses
        table = nums[start:end]
        if end - start < 3:
            return max(table)

        table[1] = max(table[:2])
        # Loop over the houses
        for house in range(start + 2, end):
            # For the current house, take the maximum considering:
            table[house - start] = max(
                # - not robbing the current house, but the prev one
                table[house - 1 - start], 
                # - robbing the current house and the prev to the prev one
                nums[house] + table[house - 2 - start]
            )

        # Return the value of the last index in the table, which
        # denotes the maximum value for all the houses
        return table[-1]

    # Since the first and the last houses can be considered
    # as adjacent houses, we can solve two problems:
    # - houses from 0 to  n-1
    # (including the first but not the last)
    # - houses from 1 to n
    # (including the last but not the first)
    return max(solve(0, size - 1), solve(1, size))


def dp_iter_opt(nums: list) -> int:
    # Dynamic programming with tabulation (iterative)
    # Time complexity: O(n)
    # Space complexity: O(1)
    # TODO
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("House robber II")
    print("-" * 60)

    test_cases = [
        ([1], 0),
        ([0], 0),
        ([8, 13], 0),
        ([2, 3, 2], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 11),
        ([20, 7, 2, 100, 110], 120),
        ([20, 7, 2, 100, 1, 2, 3, 110], 219),
        ([20, 7, 2, 100, 1, 20, 3, 110], 237),
    ]

    for nums, solution in test_cases:

        print(nums)

        result = bf_recursion(nums)
        string = f" bf_recursion = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_recursion(nums)
        string = f" dp_recursion = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(nums)
        string = f"      dp_iter = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
