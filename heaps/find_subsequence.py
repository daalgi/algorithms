"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

You are given an integer array nums and an integer k. 
You want to find a subsequence of nums of length k 
that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another 
array by deleting some or no elements without changing the 
order of the remaining elements.

Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

Constraints:
1 <= nums.length <= 1000
-105 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from typing import List
import heapq


def heap(nums: List[int], k: int) -> List[int]:
    # Time complexity: O((n + k) logn)
    # Space complexity: O(n)

    # Build a max-heap using the "trick" of changin the
    # sign to the values
    # O(n)
    heap = [(-n, i) for i, n in enumerate(nums)]
    heapq.heapify(heap)

    # Create a list with the maximum `k` values
    # O(klogn)
    res = list()
    while k > 0:
        v, i = heapq.heappop(heap)
        # We keep the index to sort the `k` values later
        res.append((i, -v))
        k -= 1

    # In order to return a subsequence, the order of the
    # maximum `k` values must respect the relative order
    # of those values in the original list `nums`:
    # - Sort the list of tuples (i, value)
    # - Return a list containing those values in the correct order
    # O(nlogn + n)
    return [n[1] for n in sorted(res)]


if __name__ == "__main__":
    print("-" * 60)
    print("Find subsequence of length K with the largest sum")
    print("-" * 60)

    test_cases = [
        ([2, 1, 3, 3], 2, [3, 3]),
        ([-1, -2, 3, 4], 3, [-1, 3, 4]),
        ([3, 4, 3, 3], 2, [3, 4]),
    ]

    for nums, k, solution in test_cases:

        output = f"Nums: {nums}"
        if len(output) > 30:
            output = output[:60] + "...]"
        print(output)
        print("k:", k)

        result = heap(nums, k)
        output = f"\t         heap = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
