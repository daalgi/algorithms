"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of 
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List
from copy import deepcopy


def brute_force(nums: List[int]) -> int:
    # Time complexity: O(n³)
    # Space complexity: O(1)

    # Special case
    if not nums:
        return 0

    max_count = 1

    # Loop over the list of numbers, O(n)
    for num in nums:
        curr_num = num
        curr_cons = 1

        # Check if next number is in the list
        # and repeat until it's not, O(n²)
        while curr_num + 1 in nums:
            curr_num += 1
            curr_cons += 1

        if curr_cons > max_count:
            max_count = curr_cons

    return max_count


def sorting(nums: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(1)

    # Special case
    if not nums:
        return 0

    # Sort the list, O(nlogn)
    nums.sort()

    # Keep track of the current and the maximum
    # length of consecutive numbers
    max_count = 1
    cur_count = 1

    # Loop over the sorted list, O(n)
    n = len(nums)
    for i in range(1, n):
        if nums[i] - 1 == nums[i - 1]:
            # If the current number is consecutive,
            # increase the current counter by one
            cur_count += 1
        else:
            # If the current number is not consecutive,
            # restart the current count of consecutive numbers
            cur_count = 1

        # If the current count is greater than the max,
        # update the max
        if cur_count > max_count:
            max_count = cur_count

    return max_count


def hashset(nums: List[int]) -> int:

    # Special case
    if not nums:
        return 0

    # Create a hashset, O(n)
    nums = set(nums)

    # Keep track of the current and the maximum
    # length of consecutive numbers
    max_count = 1

    # Loop over the elements of the list, O(n + n) = O(n)
    for num in nums:

        # Only check if the current number is the start of
        # a streak: num, num + 1, num + 2, ...
        # This way we can avoid a quadratic time complexity
        if num - 1 not in nums:

            cur_num = num
            cur_count = 1
            # While there exists the consecutive number,
            # increase the current count
            while cur_num + 1 in nums:
                cur_num += 1
                cur_count += 1

            # If the current count is greater than the max,
            # update the max
            if cur_count > max_count:
                max_count = cur_count

    return max_count


if __name__ == "__main__":
    print("-" * 60)
    print("Longest consecutive sequence")
    print("-" * 60)

    test_cases = [
        ([], 0),
        ([1, 2, 3], 3),
        ([1, 3, 5, 4, 2], 5),
        ([1, 3, 5, 4, 0], 3),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ]

    for nums, solution in test_cases:

        print("Numbers:", nums)

        result = brute_force(deepcopy(nums))
        output = f"\t   brute_force = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorting(deepcopy(nums))
        output = f"\t       sorting = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashset(deepcopy(nums))
        output = f"\t       hashset = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
