"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a 
positive integer target, return the minimal length 
of a contiguous subarray 
[numsl, numsl+1, ..., numsr-1, numsr] of which the 
sum is greater than or equal to target. If there is 
no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length 
under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
 
Follow up: If you have figured out the O(n) solution, 
try coding another solution of which the time complexity 
is O(n log(n)).
"""
from typing import List


def brute_force(nums: List[int], target: int) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    shortest, n = float("inf"), len(nums)
    for i in range(n):
        acc = 0
        for j in range(i, n):
            acc += nums[j]
            if acc >= target:
                shortest = min(shortest, j - i + 1)
                # Shortest starting from `i` already found,
                # so we can early stop and try with next `i`
                break

    return shortest if shortest < float("inf") else 0


def sliding_window(nums: List[int], target: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Two pointers marking the edges of the sliding window
    left, n, shortest, acc = 0, len(nums), float("inf"), 0
    for right in range(n):
        # Expand the window
        acc += nums[right]

        while acc >= target:
            # If the current window sum is at least `target`,
            # check if the current window size is minimum
            shortest = min(shortest, right - left + 1)
            # shrink the window
            acc -= nums[left]
            left += 1

    return shortest if shortest < float("inf") else 0


def binary_search(nums: List[int], target: int) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(1)

    def find_left(left: int, right: int, acc: int) -> int:
        # Binary search to find the largest index `left`
        # of the `prefix_sum` that satisifies:
        #   prefix_sum[right] - prefix_sum[left] >= target
        #   acc - prefix_sum[left] >= target
        while left < right:
            mid = (left + right) // 2
            if acc - prefix_sum[mid] >= target:
                # Note: prefix_sum[right] - prefix_sum[left-1]
                # that's why we update the interval left
                # boundary to `mid + 1`
                left = mid + 1
            else:
                right = mid

        return left

    prefix_sum = [nums[0]]
    n = len(nums)
    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    # Loop over the `prefix_sum`
    left, shortest = 0, float("inf")
    for right in range(n):
        if prefix_sum[right] >= target:
            # When prefix sum is at least `target`,
            # find the closest `left` index that satisfies
            #    prefix_sum[right] - prefix_sum[left-1] >= target
            left = find_left(left, right, prefix_sum[right])
            shortest = min(shortest, right - left + 1)

    return shortest if shortest < float("inf") else 0


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum size subarray sum")
    print("-" * 60)

    test_cases = [
        # (nums, target, solution)
        ([2], 1, 1),
        ([8], 9, 0),
        ([2, 1], 3, 2),
        ([2, 1, 1, 2, 4, 2, 3, 4], 7, 2),
        ([2, 4, 1], 1, 1),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11, 0),
    ]

    for nums, target, solution in test_cases:

        print("Nums:", nums)
        print("Target:", target)

        result = brute_force(nums, target)
        output = "       brute_force = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window(nums, target)
        output = "    sliding_window = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search(nums, target)
        output = "     binary_search = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
