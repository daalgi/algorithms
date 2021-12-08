"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially 
positioned at the array's first index, and each element 
in the array represents your maximum jump length at 
that position.

Return true if you can reach the last index, 
or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, 
then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible 
to reach the last index.
 
Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from functools import lru_cache


def bf_recursion(nums: list) -> bool:
    # Brute force - recursion
    # Time complexity: O(2^n)
    # Space complexity: O(n)

    # First definte the size of the string to be used
    # in the recursive function
    size = len(nums)

    def dfs(i: int) -> bool:

        # Base case: last element reached
        if i == size - 1:
            return True
        if i >= size:
            return False

        # Current element defines the maximum jump
        maxi = nums[i]
        # If the maximum jump is 0, can't reach the end
        if maxi == 0:
            return False

        # Loop over the different possible jumps
        for jump in range(maxi, 0, -1):
            if dfs(i + jump):
                # If any combination reaches the end,
                # early stop, return True
                return True

        # If no combination allowed us to reach the end,
        # it can't be reached for the current path
        return False

    # Call the recursivee function from index 0
    return dfs(0)


def dp_recursion(nums: list) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    # First definte the size of the string to be used
    # in the recursive function
    size = len(nums)

    # List to store partial results
    memo = [None] * size

    def dfs(i: int) -> bool:
        # Base cases
        # Last element reached
        if i == size - 1:
            return True
        # Last element passed
        if i >= size:
            return False

        # Check repeated work
        if memo[i] is not None:
            return memo[i]

        # Current element defines the maximum jump
        maxi = nums[i]
        # If the maximum jump is 0, can't reach the end
        if maxi == 0:
            return False

        # Loop over the different possible jumps, but
        # start from the maximum jump (potentially faster
        # to reach the end of the list)
        for jump in range(maxi, 0, -1):
            memo[i] = dfs(i + jump)
            if memo[i]:
                # If any combination reaches the end,
                # early stop, return True
                return True

        # If no combination allowed us to reach the end,
        # it can't be reached for the current path
        memo[i] = False
        return False

    # Call the recursivee function from index 0
    return dfs(0)


def dp_lru_cache(nums: list) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    # First definte the size of the string to be used
    # in the recursive function
    size = len(nums)

    # Uses python built-in memoization
    @lru_cache(maxsize=None)
    def dfs(i: int) -> bool:
        # Base cases
        # Last element reached
        if i == size - 1:
            return True
        # Last element passed
        if i >= size:
            return False

        # Current element defines the maximum jump
        maxi = nums[i]
        # If the maximum jump is 0, can't reach the end
        if maxi == 0:
            return False

        # Loop over the different possible jumps, but
        # start from the maximum jump (potentially faster
        # to reach the end of the list)
        for jump in range(maxi, 0, -1):
            if dfs(i + jump):
                # If any combination reaches the end,
                # early stop, return True
                return True

        # If no combination allowed us to reach the end,
        # it can't be reached for the current path
        return False

    # Call the recursivee function from index 0
    return dfs(0)


def dp_iter(nums: list) -> bool:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n)
    # Problem not well suited for tabulation
    size = len(nums)
    table = [False] * size
    table[0] = True
    for i in range(size):

        # Early stop if the current element hasn't been reached
        if table[i] is False:
            return False

        # Maximum jump
        maxi = nums[i]
        # Loop over the possible jumps
        for jump in range(maxi, 0, -1):
            curr = i + jump
            # If the current index+jump reaches the end, early stop
            if curr >= size - 1:
                return True
            table[curr] = True

    return table[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Jump game")
    print("-" * 60)

    test_cases = [
        ([2], True),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([1, 1, 1, 2, 0, 4], True),
        ([1, 1, 1, 2, 0, 0, 4], False),
        ([4, 3, 2, 2, 0, 0, 4], False),
        ([4, 0, 0, 0, 2, 0, 4], True),
        ([3, 8, 1, 0, 4, 2, 3, 46, 3, 2, 1, 0, 4], True),
        ([i for i in range(100000, -1, -1)], True),
        ([i for i in range(1, 1000)], True),
    ]

    for nums, solution in test_cases:

        s = str(nums)
        if len(nums) > 20:
            s = str(nums)[:30] + " ...]"
        print(s)

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

        result = dp_lru_cache(nums)
        string = f" dp_lru_cache = "
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