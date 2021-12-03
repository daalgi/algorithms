"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest 
strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array 
by deleting some or no elements without changing the order 
of the remaining elements. For example, [3,6,2,7] is a 
subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""


def brute_force(nums: int) -> int:
    # Time complexity: O(2^n)
    # Space complexity: O()
    # For each value we have two choices (include it or not),
    # then 2 * 2 * ... * 2 = 2^n
    # Generate all the subsequences
    n = len(nums)

    def recursion(i: int, current_max: int) -> int:
        # Recursive function

        # Base case
        if i == n:
            # When the pointer reaches the length of the
            # `nums` list, finish the recursion
            return 0

        # Check whether the current element nums[i] is
        # greater than the `current_max`
        if nums[i] > current_max:
            # Add the maximum of both choices:
            # - considering the current element and checking
            # the next one
            # - not considering the current element and
            # checking the next one
            return max(
                # considering the current element:
                1 + recursion(i + 1, nums[i]),
                # not considering the current element:
                recursion(i + 1, current_max),
            )

        # If nums[i] <= current_max,
        # don't consider the current element
        # and continue with next one
        return recursion(i + 1, current_max)

    # Start with the smallest `current_max` possible
    # (assuming a 32bit signed integer)
    min_int = -(2 ** 31)
    # Call the recursive function from index 0 with the
    # minimum possible value as the `current_max`
    return recursion(0, min_int)


def dfs_cache(nums: int) -> int:
    # Time complexity: O(n^2)
    # We start at the end, we go backwards and at each index
    # we check each position afterwards (every value after).
    # Space complexity: O(n)

    n = len(nums)
    # List of the longest increasing subsequence (LIS)
    # at each index in the `nums` list.
    # Each position is initialized to 1, as it's the
    # minimum LIS if we only take that element into account
    lis = [1] * n
    # For any index `i`
    # LIS[i] = max(1, 1 + LIS[i+1], 1 + LIS[i+2], ...)
    #   if nums[i] < nums[i+1] ...

    # Loop over the list backwards
    for i in range(n - 1, -1, -1):
        # At every index `i` check the LIS for each element
        # that comes after
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                # If `j` points to an element > than `i`
                # consider it as a candidate for the LIS[i]
                lis[i] = max(lis[i], 1 + lis[j])

    return max(lis)


def stable_sort(nums: int) -> int:
    # Time complexity: O(nlogn)
    pass


if __name__ == "__main__":

    print("-" * 60)
    print("Longest increasing subsequence")
    print("-" * 60)

    test_cases = [
        ([0, 1, 3, 1], 3),
        ([1, 2, 4, 3], 3),
        ([0, 1, 3, 5], 4),
        ([0, -1, -3, 5], 2),
        ([3, -1, 5, 0, 6, 2], 3),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7], 1),
        ([-1, 8, 9, 7, 7, 7, 7, 7], 3),
    ]

    for nums, solution in test_cases:

        result = brute_force(nums)
        string = f"brute_force({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dfs_cache(nums)
        string = f"dfs_cache({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
