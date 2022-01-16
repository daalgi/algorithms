"""
https://leetcode.com/problems/4sum-ii/

Given four integer arrays nums1, nums2, nums3, and nums4 
all of length n, return the number of tuples (i, j, k, l) 
such that:
- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 
Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> 
nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> 
nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:
n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
"""
from typing import List
from collections import Counter


def hashtable(
    nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    # Create a hashtable with the count of the sum of pairs of
    # two of the arrays
    counter = {}
    for m in nums1:
        for n in nums2:
            curr = m + n
            counter[curr] = counter.get(curr, 0) + 1

    # Iterate over the other two arrays to find
    # how many the tuples add up 0 using the previously
    # defined `counter`
    count = 0
    for m in nums3:
        for n in nums4:
            diff = -m - n
            if diff in counter:
                count += counter[diff]

    return count


def hashtable2(
    nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n²)
    count = Counter(a + b for a in nums1 for b in nums2)
    return sum(count[-c - d] for c in nums3 for d in nums4)


if __name__ == "__main__":
    print("-" * 60)
    print("Four sum II")
    print("-" * 60)

    test_cases = [
        ([0], [0], [0], [0], 1),
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        (
            [1, 2, 3, 5, 6, 4],
            [-2, -1, 4, 3, 2, 1],
            [-1, 2, -4, -2, 0, 4],
            [0, 2, 0, -1, 3, 5],
            49,
        ),
    ]

    for nums1, nums2, nums3, nums4, solution in test_cases:

        print("Array 1:", nums1)
        print("Array 2:", nums2)
        print("Array 3:", nums3)
        print("Array 4:", nums4)
        print("Target:", 0)

        res = hashtable(nums1, nums2, nums3, nums4)
        output = "    hashtable = "
        output += str(res)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if res == solution else "NOT OK"}'
        print(output)

        res = hashtable2(nums1, nums2, nums3, nums4)
        output = "   hashtable2 = "
        output += str(res)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if res == solution else "NOT OK"}'
        print(output)

        print()
