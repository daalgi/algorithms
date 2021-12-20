"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an integer array nums, return the number of 
longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences 
are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence 
is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:
1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
from typing import List


def brute_force(nums: List[int]) -> bool:
    # Time complexity: O(2^n),
    # Space complexity: O(n)
    pass


def dp_memoization(nums: List[int]) -> bool:
    # Dynamic programming - Memoization
    # Time complexity: O(n²)
    # Space complexity: O(n²)
    pass


def dp_tabulation(nums: List[int]) -> bool:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    n = len(nums)

    # List to keep track to the length of the maximum LIS at each index.
    # Initialize it with 1s (each element can be
    # considered to be a LIS = 1)
    lis = [1] * n
    # List ot keep track of the number of LIS at each index.
    # Initilize it with 1s
    count = [1] * n

    # Use two pointers to compare pairs all pairs of values
    # in increasing order
    for right in range(1, n):
        for left in range(right):
            # If the number at the `right` is greater
            # than the one at the `left`, it may contribute
            # to the LIS at up to the index `right`
            if nums[right] > nums[left]:
                if lis[right] < 1 + lis[left]:
                    # If the current LIS at `right` is less
                    # than one plus LIS at `left`, update the LIS
                    lis[right] = 1 + lis[left]
                    # Update the count of LIS at `right`, which
                    # is the same as the count at `left`
                    # (no new LIS)
                    count[right] = count[left]
                elif lis[right] == 1 + lis[left]:
                    # If the current LIS at `right` is EQUAL
                    # to one plus LIS at `left`, there is a new
                    # LIS, so we add the count from `left`
                    count[right] += count[left]

    # The number of LIS is equal to the sum of the elements in `count`
    # for which the corresponding `lis[i]` equals to the `max(lis)`
    longest_length = max(lis)
    return sum([count[i] for i in range(n) if lis[i] == longest_length])


if __name__ == "__main__":

    print("-" * 60)
    print("Number of longest increasing subsequences")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([1, 1, 1], 3),
        ([2, 2, 1], 3),
        ([3, 2, 2, 1], 4),
        ([1, 3, 5, 4, 7], 2),
        ([1, 3, 5, 1, 4, 7], 2),
        ([1, 3, 5, 1, 2, 4, 7], 4),
        ([3, 2, 2, 2, 1, 1145, 23, 23, 2, 1325, 4, 6, 566, 44, 3, 23, 25], 1),
    ]

    for nums, solution in test_cases:

        output = str(nums)
        if len(nums) > 20:
            output = output[:60] + "...]"
        print("Numbers:", output)

        # result = dp_memoization(nums)
        # output = f"     dp_memoization = "
        # output += " " * (25 - len(output))
        # output += str(result)
        # output += " " * (60 - len(output))
        # test_ok = solution is result
        # output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        result = dp_tabulation(nums)
        output = f"      dp_tabulation = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
