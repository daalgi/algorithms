"""
https://leetcode.com/problems/longest-increasing-subsequence/

VARIATION: RESTORE THE SUBSEQUENCE

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

    # O(n²)
    # Loop over the list backwards
    for i in range(n - 1, -1, -1):
        # At every index `i` check the LIS for each element
        # that comes after
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                # If `j` points to an element > than `i`
                # consider it as a candidate for the LIS[i]
                lis[i] = max(lis[i], 1 + lis[j])

    # Track the length of the LIS
    # O(n)
    next_max_length = max(lis)
    # List to append the resulting subsequence
    sub = list()
    # Loop over the elements at the list LIS
    # to add iteratively the elements of the subsequence
    # O(n)
    for i in range(n):
        if lis[i] == next_max_length:
            # If the current element has the current max length
            if not len(sub) or nums[i] > sub[-1]:
                # If the subsequence hasn't been initialized
                # or if the current element is greater than
                # the last element in the subsequence,
                # add it to the resulting list
                sub.append(nums[i])
                # Subtract one to find the next max length
                # subsequence element
                next_max_length -= 1

    return sub


if __name__ == "__main__":

    print("-" * 60)
    print("Longest increasing subsequence - RESTORE THE SUBSEQUENCE")
    print("-" * 60)

    test_cases = [
        ([0, 1, 3, 1], [0, 1, 3]),
        ([1, 2, 4, 3], [1, 2, 4]),
        ([0, 1, 3, 5], [0, 1, 3, 5]),
        ([0, -1, -3, 5], [0, 5]),
        ([3, -1, 5, 0, 6, 2], [3, 5, 6]),
        ([10, 9, 2, 5, 3, 7, 101, 18], [2, 5, 7, 101]),
        ([0, 1, 0, 3, 2, 3], [0, 1, 2, 3]),
        ([7, 7, 7, 7, 7, 7], [7]),
        ([-1, 8, 9, 7, 7, 7, 7, 7], [-1, 8, 9]),
    ]

    for nums, solution in test_cases:

        result = dfs_cache(nums)
        string = f"dfs_cache({nums}) = "
        string += " " * (45 - len(string))
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
