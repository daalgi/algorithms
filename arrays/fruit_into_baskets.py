"""
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of 
fruit trees arranged from left to right. The trees 
are represented by an integer array fruits where 
fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. 
However, the owner has some strict rules that you 
must follow:
- You only have two baskets, and each basket can only 
hold a single type of fruit. There is no limit on the 
amount of fruit each basket can hold.
- Starting from any tree of your choice, you must 
pick exactly one fruit from every tree (including 
the start tree) while moving to the right. The picked 
fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit 
in your baskets, you must stop.

Given the integer array fruits, return the maximum 
number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only 
pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only 
pick from trees [1,2].

Constraints:
1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
"""
from typing import List
from collections import defaultdict


def brute_force(fruits: List[int]) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    n = len(fruits)
    max_fruits = 1
    for i in range(n):
        j = i + 1
        nums = {fruits[i]}
        while j < n and len(nums) < 3:
            nums.add(fruits[j])
            j += 1

        if len(nums) == 3:
            max_fruits = max(j - 1 - i, max_fruits)
        else:
            max_fruits = max(j - i, max_fruits)

    return max_fruits


def sliding_window(fruits: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(2) = O(1)
    # Problem: find the longest subarray with at most 2
    # different numbers
    # Strategy: sliding window

    # Counter of the elements of the current subarray
    count = defaultdict(int)
    # Two pointers
    left, n = 0, len(fruits)
    for right in range(n):
        # Expand the sliding window (`right` pointer)
        count[fruits[right]] += 1

        # If the subarray contains more than two elements
        if len(count) > 2:
            # Shrink the sliding window (`left` pointer)
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

    # Longest sliding window from the last element (n - 1)
    # to the `left` pointer + 1: n - 1 - left + 1 = n - left
    return n - left


if __name__ == "__main__":
    print("-" * 60)
    print("Fruit into baskets")
    print("-" * 60)

    test_cases = [
        # (fruits, solution)
        ([2], 1),
        ([2, 1], 2),
        ([2, 0, 1], 2),
        ([2, 1, 2], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5),
    ]

    for fruits, solution in test_cases:

        print("Fruits:", fruits)

        result = brute_force(fruits)
        output = "       brute_force = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window(fruits)
        output = "    sliding_window = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
