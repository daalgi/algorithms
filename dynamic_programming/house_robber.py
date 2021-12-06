"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along 
a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems 
connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of 
money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then 
rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), 
rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
import time
from random import randint


def bf_recursion(nums: list) -> int:
    # Brute force with recursion
    # Time complexity: O(2^n)
    # We have two choices for each house (rob or not): 
    # 2 * 2 * ... = 2^n
    # Space complexity: O(n)
    # Max depth of the stack: n

    houses = len(nums)

    def recursion(house: int) -> int:
        # Recursive function

        # Base case
        if house >= houses:
            return 0

        # Max of:
        # - don't rob the current house, go for the next one
        # - rob the current house, skip the next one
        return max(
            recursion(house + 1), 
            nums[house] + recursion(house + 2)
        )

    # Call the recursive function starting from the house 0
    return recursion(0)


def dp_recursion(nums: list) -> int:
    # Dynamic programming with memoization (recursive)
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Same as in the brute force algorithm, but now using
    # memoization to avoid repeated computations.

    houses = len(nums)
    memo = [None] * (houses + 1)

    def recursion(house: int) -> int:
        # Recursive function

        # Base case
        if house >= houses:
            return 0
        
        # Check if the result has been already computed
        if memo[house] is not None:
            return memo[house]

        # Max of the current house
        memo[house] = max(
            recursion(house + 1),
            nums[house] + recursion(house + 2)
        )
        return memo[house]

    # Call the recursive function starting at house 0
    return recursion(0)


def dp_iter(nums: list) -> int:
    # Dynamic programming with tabulation (iterative)
    # Time complexity: O(n)
    # Space complexity: O(n)

    houses = len(nums)

    if houses == 1:
        return nums[0]

    # Table to store the results from the bottom up.
    # Each element represents the maximum robbed possible 
    # value considering the previous houses
    table = [*nums]
    table[1] = max(nums[0], nums[1])

    # Loop over the houses
    for house in range(2, houses):
        # For the current house, take the maximum considering:
        # - not robbing the current house, but the prev one
        # - robbing the current house and the prev to the prev one
        table[house] = max(
            table[house - 1], 
            nums[house] + table[house - 2]
        )
    # Return the value of the last index in the table, which
    # denotes the maximum value for all the houses
    return table[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("House robber")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([0], 0),
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([20, 7, 2, 100, 1], 120),
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


print("\n\n>>> Performance tests:")
for size in [30, 500, 20000]:

    nums = [randint(0, 100) for _ in range(size)]
    print('\n>Array size:', size)

    if size < 40:
        t = time.time()
        print(f"\n Brute force: f = {bf_recursion(nums)}")
        t = time.time() - t
        print(f"Computation time: {t*1e3:>8.0f} ms")
    
    if size < 1000:
        t = time.time()
        print(f"\nDp recursion: f = {dp_recursion(nums)}")
        t = time.time() - t
        print(f"Computation time: {t*1e3:>8.0f} ms")

    t = time.time()
    print(f"\n     Dp iter: f = {dp_iter(nums)}")
    t = time.time() - t
    print(f"Computation time: {t*1e3:>8.0f} ms")
    print()
