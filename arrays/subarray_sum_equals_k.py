"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, 
return the total number of continuous subarrays 
whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

NOTE:
Given that the values can be negative, we can't use
a `two-pointer` or `sliding-window` approach, since:
- adding a value in the subarray doesn't guarantee that
the sum is going to increase.
- removing a value in the subarray doesn't guarantee that
the sum is going to decrease.
"""
from sys import prefix
from typing import List
from collections import defaultdict
from unittest import TestCase


def brute_force(nums: List[int], k: int) -> int:
    # Time complexity: O(n³)
    # Space complexity: O(1)

    # Try all the combinations of subarrays
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = sum(nums[i : j + 1])
            if curr_sum == k:
                count += 1

    return count


def cumulative_sum(nums: List[int], k: int) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n)

    # Build a cumulative sum list,
    # where each element at index `i` is used to
    # store the cumulative sum of `nums` up to `i - 1`,
    # so later on we can find the sum of any
    # subarray `nums[i:j]` as `sum[j+1] - sum[i]`, i.e.
    #   indices 0 1 2 3 4  5  6
    #   nums    1 5 2 1 3  2
    #   cum_sum 0 1 6 7 8 11 13
    #       start, end = 1, 3
    #       sum = 7 - 1 = 6
    cum_sum = [0]
    n = len(nums)
    for i in range(1, n + 1):
        cum_sum.append(nums[i - 1] + cum_sum[-1])

    count = 0
    for start in range(n):
        for end in range(start + 1, n + 1):
            if cum_sum[end] - cum_sum[start] == k:
                count += 1

    return count


def cumulative_sum2(nums: List[int], k: int) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)

    # Similar approach to `brute_force`, but
    # keeping track of the cumulative sum
    # from `i` to `j` to reduce the time complexity
    n = len(nums)
    count = 0
    for start in range(n):
        curr_sum = 0
        for end in range(start, n):
            curr_sum += nums[end]
            if curr_sum == k:
                count += 1

    return count


def hashmap(nums: List[int], k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    """
    Example:
    k = 3
    indices      0  1  2  3  4  5
    nums         1 -1  1  1  1  1
    cum_sum      1  0  1  2  3  4
    diff         2  3  2  1  0 -1
    hashmap  {0: 1}
       i=0  diff=-2  {0: 1, 1: 1}
       i=1  diff=-3  {0: 2, 1: 1}
       i=2  diff=-2  {0: 2, 1: 2}
       i=3  diff=-1  {0: 2, 1: 2, 2: 1}
       i=4  diff= 0  {0: 2, 1: 2, 2: 1, 3: 1}        count += 2 = 2
       i=5  diff= 1  {0: 2, 1: 2, 2: 1, 3: 1, 4: 1}  count += 2 = 4
    """
    # Notes:
    # subarray[L..R] = pref[R] - pref[L-1]
    # pref[R] - pref[L-1] = k
    # pref[L-1] = pref[R] - k
    # check if pref[L-1] exists in the hashmap
    # add pref[R] to the hashmap
    # (later will turn into pref[L-1] as we check for a greater R)

    # Map the prefix_sum to the number of times achieved
    # { prefix_sum: count }, where prefix_sum is cumulative
    # sum from the first element (i=0) to the current element.
    # Ultimately we want to know how many
    sums = defaultdict(int)
    # Take into account the possibility that at some point the
    # cumulative sum can be exactly `k`, so the difference
    # `cum_sum - k` must be in the hashmap
    sums[0] = 1
    # Loop over the items of `nums` keeping track of the
    # cumulative sum and the count of subarrays adding up `k`
    cum_sum = count = 0
    for num in nums:
        cum_sum += num
        diff = cum_sum - k
        # Check if we already have a prefix_sum equal to `diff`
        # in the hashmap
        if diff in sums:
            # Add the number of prefixes we have previously counted
            count += sums[diff]
        # Add the current cumulative sum to the hashmap
        sums[cum_sum] += 1

    return count


def hashmap2(nums: List[int], k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Small optimizations

    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    curr_sum = count = 0
    for num in nums:
        curr_sum += num
        count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] += 1

    return count


def hashmap_verbose(nums: List[int], k: int) -> int:
    sums = defaultdict(int)
    sums[0] = 1
    curr_sum = count = 0
    for i, num in enumerate(nums):
        curr_sum += num
        diff = curr_sum - k
        if diff in sums:
            count += sums[diff]
        print("\n>>Iteration:", i)
        print(nums[: i + 1])
        print(f"Num: {num:4}\tPrefix_sum:{curr_sum:4}\t\tDiff: {diff:4}")
        print("Sums (before):", dict(sums))
        sums[curr_sum] += 1
        print("Sums  (after):", dict(sums))
        print("Count:", count)

    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Subarray sum equals k")
    print("-" * 60)

    test_cases = [
        # (nums, k, solution)
        ([0], 0, 1),
        ([1, -1, 1, 1, 1, 1], 3, 4),
        ([1, 1, 1, 1, 1, 1, 1], 3, 5),
        ([-1, 0, 1], 0, 2),
        ([0, 1, -1, 2], 1, 3),
        ([-1, 3, -1, 2], 2, 3),
        ([-1, 3, 1, 2, -2, 0, 2], 3, 6),
        ([-1, 3, 1, 2, -1, 0, 2], 3, 4),
        (
            [1, 2, 3, 5, 7, 2, 4, 2, 4, 1, 4, 3, 0, 0, 0, 2, 2, -1, 2, -1, 2, -3],
            8,
            7,
        ),
    ]

    for nums, k, solution in test_cases:

        print("Array:", nums)
        print("Target sum:", k)

        result = brute_force([*nums], k)
        output = f"     brute_force = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = cumulative_sum([*nums], k)
        output = f"  cumulative_sum = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = cumulative_sum2([*nums], k)
        output = f" cumulative_sum2 = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap([*nums], k)
        output = f"         hashmap = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2([*nums], k)
        output = f"        hashmap2 = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()

    nums, k, solution = test_cases[-2]
    print("\n\nHashmap verbose example: " + "-" * 35)
    print("Array:", nums)
    print("Target sum:", k)
    hashmap_verbose(nums, k)
