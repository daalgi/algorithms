"""
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more 
than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
 
Follow-up: Could you solve the problem in 
linear time and in O(1) space?
"""
from typing import List
from collections import Counter


def hashmap(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    max_elem, max_count = None, float("-inf")
    for k, v in count.items():
        if v > max_count:
            max_elem, max_count = k, v

    return max_elem


def hashmap2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    count = Counter(nums)
    return max(count.keys(), key=count.get)


def moore_voting(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    elem, count = nums[0], 1
    n = len(nums)
    for i in range(1, n):
        if count == 0:
            elem, count = nums[i], 1
        elif nums[i] == elem:
            count += 1
        else:
            count -= 1

    return elem


if __name__ == "__main__":
    print("-" * 60)
    print("Majority element")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([1, 2, 1], 1),
        ([1, 2, 1, 2, 1], 1),
        ([1, 2, 1, 2, 2, 22, 2, 1, 2], 2),
    ]

    for nums, solution in test_cases:

        print(f"Array: {nums}")

        result = hashmap(nums)
        output = f"         hashmap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(nums)
        output = f"        hashmap2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = moore_voting(nums)
        output = f"    moore_voting = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
