"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must appear as many 
times as it shows in both arrays and you may 
return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
- What if the given array is already sorted? 
How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? 
Which algorithm is better?
- What if elements of nums2 are stored on disk, and the 
memory is limited such that you cannot load all elements 
into the memory at once?
"""
from typing import List
from collections import Counter


def hashmap(nums1: List[int], nums2: List[int]) -> List[int]:
    # Time complexity: O(m+n)
    # Space complexity: O(m)
    #  where `m` is the size of the smallest list

    # Force `nums1` to be the smallest list, so we
    # use the least memory
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Counter hashmap for the smallest list
    count = {}
    for num in nums1:
        count[num] = count.get(num, 0) + 1

    res = []
    for num in nums2:
        if num in count:
            res.append(num)
            count[num] -= 1
            if count[num] == 0:
                del count[num]

    return res


def hashmap2(nums1: List[int], nums2: List[int]) -> List[int]:
    # Time complexity: O(m+n)
    # Space complexity: O(m)
    #  where `m` is the size of the smallest list

    # Force `nums1` to be the smallest list
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    count = Counter(nums1)
    res = []
    for num in nums2:
        if count[num] > 0:
            res.append(num)
            count[num] -= 1
    return res


def two_pointers(nums1: List[int], nums2: List[int]) -> List[int]:
    # Time complexity: O(m+n)
    # Space complexity: O(1)
    # Best approach if the lists are sorted (space complexity O(1))

    # Assumption: already sorted lists
    nums1.sort()
    nums2.sort()

    m, n = len(nums1), len(nums2)
    i = j = 0
    res = []
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Intersection of two arrays II")
    print("-" * 60)

    test_cases = [
        ([1], [1], [1]),
        ([1, 2, 1], [1], [1]),
        ([1, 2, 1, 2, 1], [3], []),
        ([1, 2, 1, 2, 2, 22, 2, 1, 2], [2, 2, 23], [2, 2]),
    ]

    for nums1, nums2, solution in test_cases:

        print(f"Array 1: {nums1}")
        print(f"Array 2: {nums2}")

        result = hashmap(nums1, nums2)
        output = f"         hashmap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(nums1, nums2)
        output = f"        hashmap2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = two_pointers([*nums1], [*nums2])
        output = f"    two_pointers = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
