"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Given an array of positive integers arr, calculate 
the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and 
their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 
1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, 
[1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66

Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""
from typing import List
from itertools import accumulate


def brute_force(nums: List[int]) -> int:
    # Time complexity: O(n³)
    # Space complexity: O(1)
    n = len(nums)
    res = 0
    for left in range(1, n + 1, 2):
        for right in range(n - left + 1):
            res += sum(nums[right : right + left])
    return res


def prefix_sum(nums: List[int]) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n)

    n = len(nums)
    acc = [nums[0]]
    for i in range(1, n):
        acc.append(acc[-1] + nums[i])

    # Sum of size 1 subarrays
    res = sum(nums)

    # Sum of subarrays starting at element 0
    for right in range(2, n, 2):
        res += acc[right]

    # Sum of subarrays starting at the rest of elements
    for left in range(1, n):
        for right in range(left + 2, n, 2):
            res += acc[right] - acc[left - 1]

    return res


def frequencies(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    """
    There are:
    k = (i + 1) * (n - i) subarrays that contain nums[i]
    (k + 1) // 2          odd-length subarrays that contain nums[i]
    k // 2                even-length subarrays that contain nums[i]

    Example:
    len = 5
    index  0  1  2  3  4
    nums   1  4  2  5  3
    times  3  4  5  4  3
    subarrays length=1 --> [1],[4],[2],[5],[3]
    subarrays length=3 --> [1,4,2],[4,2,5],[2,5,3]
    subarrays length=5 --> [1,4,2,5,3]

    index 0, num 1 appears 3 times, ((0 + 1) * (5 - 0) + 1) // 2 = 3
    index 1, num 4 appears 4 times, ((1 + 1) * (5 - 1) + 1) // 2 = 4
    index 2, num 2 appears 5 times, ((2 + 1) * (5 - 2) + 1) // 2 = 5
    index 3, num 5 appears 4 times, ((3 + 1) * (5 - 3) + 1) // 2 = 4
    index 4, num 3 appears 3 times, ((4 + 1) * (5 - 4) + 1) // 2 = 3
    index i, num _ appears x times, ((i + 1) * (n - i) + 1) // 2 = x
                                    (end_at  * start_at + 1) // 2
    index  0  1  2  3  4
    nums   1  4  2  5  3
    start  5  4  3  2  1   start = n - i
    end    1  2  3  4  5     end = i + 1
    total  5  8  9  8  5   total = start * end
    odd    3  4  5  4  3     odd = (total + 1) // 2
    """
    res, n = 0, len(nums)
    for i in range(n):
        # Count the number of times that `nums[i]`
        # will be used to form odd-length subarrays
        # freq = ((i + 1) * (n - 1) + 1) // 2
        res += ((i + 1) * (n - i) + 1) // 2 * nums[i]

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Sum of all odd length subarrays")
    print("-" * 60)

    test_cases = [
        # (nums, solution)
        ([1], 1),
        ([1, 2], 3),
        ([1, 4, 2, 5, 3], 58),
        ([10, 11, 12], 66),
        ([1, 2, 3, 23, 53, 1, 3, 2, 52, 534], 4395),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

        result = brute_force(nums)
        output = "   brute_force = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = prefix_sum(nums)
        output = "    prefix_sum = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = frequencies(nums)
        output = "   frequencies = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
