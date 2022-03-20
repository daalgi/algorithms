"""
https://leetcode.com/problems/subarray-product-less-than-k/

Given an array of integers nums and an integer k, 
return the number of contiguous subarrays where the 
product of all the elements in the subarray is 
strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 
is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""
from typing import List
import math
import bisect


def brute_force(nums: List[int], k: int) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)

    # Try all the combinations of subarrays
    n = len(nums)
    count = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            if prod < k:
                count += 1

    return count


def binary_search(nums: List[int], k: int) -> int:
    # Time complexity: O(nlogn)
    # Time complexity: O(n)

    # Note: prod(x1 + x2 + ... + xn) = sum(log(x1) + log(x2) + ... + log(xn))
    # Therefore, we can reduce the problem to subarray sums,
    # and use a prefix sum

    if k == 0:
        return 0

    k = math.log(k)
    
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + math.log(num))

    n = len(prefix)
    count = 0
    for i in range(n):
        j = bisect.bisect(prefix, prefix[i] + k - 1e-9, i + 1)
        count += j - i - 1
    
    return count


def sliding_window(nums: List[int], k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Edge case: if `k` is zero or one, since nums[i] > 0,
    # there can't be any element smaller than `k`
    if k <= 1:
        return 0

    # Sliding window.
    # Use `left` and `right` pointers to keep track
    # of the range of elements whose product is less than `k`
    left, n, prod, count = 0, len(nums), 1, 0
    for right in range(n):
        prod *= nums[right]

        # If the current product is more or equal to `k`,
        # move the `left` pointer
        while prod >= k:
            prod //= nums[left]
            left += 1

        # Count the number of intervals with subarray
        # product less than `k`
        count += right - left + 1

    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Subarray product less than k")
    print("-" * 60)

    test_cases = [
        # (nums, k, solution)
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 1, 1], 1, 0),
        (
            [1, 2, 3, 2, 23, 1, 2, 3, 5, 6, 43, 7, 8, 8, 9, 8, 7, 6, 4, 4, 3, 23, 2, 3],
            86,
            54,
        ),
        (
            [1, 2, 3, 2, 23, 1, 2, 3, 5, 6, 43, 7, 8, 8, 9, 8, 7, 6, 4, 4, 3, 23, 2, 3],
            1986,
            95,
        ),
    ]

    for nums, k, solution in test_cases:

        print("Array:", nums)
        print("k:", k)

        result = brute_force([*nums], k)
        output = f"     brute_force = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search([*nums], k)
        output = f"   binary_search = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window([*nums], k)
        output = f"  sliding_window = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
