"""
https://leetcode.com/problems/split-array-largest-sum/

Given an array nums which consists of non-negative 
integers and an integer m, you can split the array 
into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among 
these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.length)
"""
from typing import List
from functools import lru_cache


def dp_recursion(nums: List[int], m: int) -> int:
    # Dynamic programming - Recursion - Top-down approach
    # Time complexity: O(n²m)
    # Space complexity: O(mn)
    """
    nums = [1 5 2 3 4], m = 2
    1  (1)       5 2 3 4 (14) -> max = 14
    1 5 (6)      2 3 4 (9)    -> max = 9
    1 5 2 (8)    3 4 (7)      -> max = 8
    1 5 2 3 (11) 4 (4)        -> max = 11
    ----> min = 8

    nums = [1 5 2 3 4], m = 3
    1 (1)        5 (5)          2 3 4 (9)  -> max = 9
    1 (1)        5 2 (7)        3 4 (7)    -> max = 7
    1 (1)        5 2 3 (10)     4 (4)      -> max = 10
    1 5 (6)      2 (2)          3 4 (7)    -> max = 7
    1 5 (6)      2 3 (5)        4 (4)      -> max = 6
    1 5 2 (8)    3 (3)          4 (4)      -> max = 8
    ----> min = 6

    DP
    Recurrence relation:
    F[curr_index, subarray_count] = min(
        max(sum[curr_index, i], F[i + 1, subarray_count - 1])
        for i in range(curr_index, n - subarray_count)
    )
    Base case (can calculate the result for the subproblem
    without using the above recurrence relation):
    --> when there's only one subarray remaining, all of the
    numbers remaining must go in that subarray, so when
    `subarray_count` is 1, we can simply return the sum of the
    numbers between `curr_index` and the end of the array.
    """

    @lru_cache(maxsize=None)
    def get_min_largest_split_num(curr_index: int, subarray_left: int) -> int:
        # Base case
        if subarray_left == 1:
            return prefix_sum[n] - prefix_sum[curr_index]

        # Otherwise, use the recurrence relation
        min_largest_split_sum = prefix_sum[n]
        for i in range(curr_index, n - subarray_left + 1):
            # Store the sum of the first subarray
            first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]
            # Find the max subarray for the current first split
            largest_split_sum = max(
                first_split_sum,
                get_min_largest_split_num(i + 1, subarray_left - 1),
            )
            # Find the min among all possible combinations
            min_largest_split_sum = min(min_largest_split_sum, largest_split_sum)
            # Early stop
            if first_split_sum >= min_largest_split_sum:
                break

        return min_largest_split_sum

    # Build the prefix sum list to later on calculate
    # the sum of any range of elements in constant time
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    n = len(nums)
    return get_min_largest_split_num(0, m)


def dp_iter(nums: List[int], m: int) -> int:
    # Dynamic programming - Iterative - Bottom-up approach
    # Time complexity: O(n²m)
    # Space complexity: O(mn)
    n = len(nums)
    # Build the prefix sum list to later on calculate
    # the sum of any range of elements in constant time
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    memo = [[0] * (m + 1) for _ in range(n)]

    for subarray_count in range(1, m + 1):
        for curr_index in range(n):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                memo[curr_index][subarray_count] = (
                    prefix_sum[n] - prefix_sum[curr_index]
                )
                continue

            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(
                    first_split_sum, memo[i + 1][subarray_count - 1]
                )

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(
                    minimum_largest_split_sum, largest_split_sum
                )

                if first_split_sum >= minimum_largest_split_sum:
                    break

            memo[curr_index][subarray_count] = minimum_largest_split_sum

    return memo[0][m]


def dp_iter_opt(nums: List[int], m: int) -> int:
    # Dynamic programming - Iterative - Bottom-up approach
    # Time complexity: O(n²m)
    # Space complexity: O(mn)
    n = len(nums)

    # Build the prefix sum list to later on calculate
    # the sum of any range of elements in constant time
    accum = [nums[0]]
    for i in range(1, n):
        accum.append(accum[-1] + nums[i])

    prev = accum
    for i in range(1, m):
        curr = [float("inf")] * n
        # print(f">> Subarray: {i}")
        for j in range(n):
            for k in range(0, j):
                # output = f"{j, k} -> \tmin({curr[j]:>3}, "
                # output += f"max({prev[k]:>3}, {accum[j] - accum[k]:>3}))"
                curr[j] = min(curr[j], max(prev[k], accum[j] - accum[k]))
                # output += f" = {curr[j]:>3}"
            #     print(output)
            # print(curr)
        prev = curr

    return prev[n - 1]


def binary_search(nums: List[int], m: int) -> int:
    # Time complexity: O(n log(sum(nums) - max(nums)))
    # Space complexity: O(1)
    # where `s` is the sum of integers in the array
    # The total number of iterations in the
    # binary search is log(s), and for each such iteration,
    # we call `min_subarrays_required`, which takes
    # O(n) time.

    def min_subarrays_required(max_sum_allowed: int) -> int:
        current_sum = 0
        splits_required = 0

        for element in nums:
            # Add element only if the sum doesn't exceed max_sum_allowed
            if current_sum + element <= max_sum_allowed:
                current_sum += element
            else:
                # If the element addition makes sum more than max_sum_allowed
                # Increment the splits required and reset sum
                current_sum = element
                splits_required += 1

        # Return the number of subarrays, which is the number of splits + 1
        return splits_required + 1

    # Define the left and right boundary of binary search
    left = max(nums)
    right = sum(nums)
    while left <= right:
        # Find the mid value
        max_sum_allowed = (left + right) // 2

        # Find the minimum splits. If splits_required is less than
        # or equal to m move towards left i.e., smaller values
        if min_subarrays_required(max_sum_allowed) <= m:
            right = max_sum_allowed - 1
            minimum_largest_split_sum = max_sum_allowed
        else:
            # Move towards right if splits_required is more than m
            left = max_sum_allowed + 1

    return minimum_largest_split_sum


if __name__ == "__main__":
    print("-" * 60)
    print("Split array largest sum")
    print("-" * 60)

    test_cases = [
        # (nums, m, solution)
        ([1, 4, 4], 3, 4),
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2, 3, 4, 5], 2, 9),
        ([7, 2, 5, 10, 8, 2, 3], 2, 23),
        ([7, 2, 5, 10, 8, 2, 3], 3, 14),
        ([7, 2, 5, 10, 8, 2, 3], 4, 13),
        ([1, 4, 4, 3, 2, 35, 23, 12, 453, 65, 334, 26, 26, 3456, 2435], 3, 3456),
    ]

    for nums, m, solution in test_cases:

        print("Nums:", nums)
        print("m:", m)

        result = dp_recursion(nums, m)
        output = f"     dp_recursion = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter(nums, m)
        output = f"          dp_iter = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter_opt(nums, m)
        output = f"      dp_iter_opt = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search(nums, m)
        output = f"    binary_search = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
