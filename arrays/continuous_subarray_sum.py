"""
https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return 
true if nums has a continuous subarray of size at least 
two whose elements sum up to a multiple of k, or false 
otherwise.

An integer x is a multiple of k if there exists an integer 
n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 
whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray 
of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""
from typing import List


def brute_force(nums: List[int], k) -> bool:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    n = len(nums)
    for i in range(n - 1):
        curr = nums[i]
        for j in range(i + 1, n):
            curr += nums[j]
            if curr % k == 0:
                return True

    # Not found
    # Note: the subarray must be of at least 2 elements,
    # so the edge case of an array of 1 element multiple of `k`
    # should return False as well
    return False


def hashmap(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Hashmap { number: index } to keep track
    # of the first occurrence of a remainder (s % k).
    seen = {0: -1}

    n = len(nums)
    running_sum = 0
    for i in range(n):
        running_sum += nums[i]
        if k:
            running_sum %= k

        # Check if the current `running_sum`
        # exists in the hashmap
        prev = seen.get(running_sum, None)
        if prev is not None:
            if i - prev > 1:
                # If it exists, and the previous index
                # is at least two elements away,
                # the remainder has seen before, so
                # the subarray sum is a multiple of `k`
                return True
        else:
            seen[running_sum] = i

    return False


def hashmap2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    seen, curr = {0: -1}, 0
    for i, num in enumerate(nums):
        curr = (curr + num) % k if k else curr + num
        if i - seen.setdefault(curr, i) > 1:
            return True
    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Continuous subarray sum")
    print("-" * 60)

    test_cases = [
        # (nums, k, solution)
        ([1], 1, False),
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
        ([5, 0, 0, 0], 3, True),
    ]

    for nums, k, solution in test_cases:

        print("Nums:", nums)
        print("k:", k)

        result = brute_force(nums, k)
        output = "    brute_force = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap(nums)
        output = "        hashmap = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(nums)
        output = "       hashmap2 = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
