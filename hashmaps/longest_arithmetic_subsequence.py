"""
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Given an integer array arr and an integer difference, 
return the length of the longest subsequence in arr 
which is an arithmetic sequence such that the 
difference between adjacent elements in the subsequence 
equals difference.

A subsequence is a sequence that can be derived from 
arr by deleting some or no elements without changing 
the order of the remaining elements.

Example 1:
Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is 
[1,2,3,4].

Example 2:
Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is 
any single element.

Example 3:
Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is 
[7,5,3,1].

Constraints:
1 <= arr.length <= 10^5
-104 <= arr[i], difference <= 10^4
"""
from typing import List
from collections import defaultdict


def hashmap(nums: List[int], difference: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    prev = defaultdict(int)
    for num in nums:
        target = num - difference
        if target in prev:
            prev[num] = prev[target] + 1
        else:
            prev[num] = 1

    return max(prev.values())


if __name__ == "__main__":
    print("-" * 60)
    print("Longest arithmetic subsequence of given difference")
    print("-" * 60)

    test_cases = [
        # ( array, difference, solution )
        ([1, 2, 3, 4], 1, 4),
        ([1, 3, 5, 7], 1, 1),
        ([1, 3, 6, 7], 2, 2),
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4),
    ]

    for nums, difference, solution in test_cases:

        print("Nums:", nums)
        print("Difference:", difference)

        result = hashmap(nums, difference)
        output = f"      hashmap = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
