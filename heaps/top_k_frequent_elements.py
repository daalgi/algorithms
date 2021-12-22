"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better 
than O(n log n), where n is the array's size.
"""
from typing import List
import heapq
from collections import Counter


def heap(nums: List[int], k: int) -> List[int]:
    # Time complexity: O(n + klogn)
    # Space complexity: O(n)

    n = len(nums)

    # If `k` is equal to the length of the list `nums`,
    # since `k` is in the range [1, num_unique_numbers],
    # the result will be the list itself
    # O(1)
    if k == n:
        return nums

    # Create a frequency table (hashtable)
    # O(n)
    freq = dict()
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Build a min-heap of tuples (-freq, num)
    # O(n)
    heap = [(-k, v) for v, k in freq.items()]
    heapq.heapify(heap)

    # Get the k most frequent numbers
    # O(klogn)
    ans = []
    while k > 0:
        ans.append(heapq.heappop(heap)[1])
        k -= 1

    return ans


def heap2(nums: List[int], k: int) -> List[int]:
    # Time complexity: O(n + nlogk)
    # Space complexity: O(n)

    n = len(nums)

    # If `k` is equal to the length of the list `nums`,
    # since `k` is in the range [1, num_unique_numbers],
    # the result will be the list itself
    # O(1)
    if k == n:
        return nums

    # Frequency hashtable, O(n)
    freq = dict()
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Build heap of top k frequent elements and return a list
    # O(nlogk)
    return heapq.nlargest(k, freq.keys(), key=freq.get)


def bucket_sort(nums: List[int], k: int) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(nums)

    # If `k` is equal to the length of the list `nums`,
    # since `k` is in the range [1, num_unique_numbers],
    # the result will be the list itself
    # O(1)
    if k == n:
        return nums

    # Frequencies hashtable
    # O(n)
    freq = Counter(nums)

    # List of buckets, each bucket for a different frequency
    # [[], [], [], [1, 2], []]
    # --> freq 0, 1, 2, 4 have no numbers
    # --> freq 3 has the numbers [1, 2]
    # O(n)
    buckets = [[] for _ in range(n + 1)]
    for num, f in freq.items():
        buckets[f].append(num)

    # Loop over the buckets and its elements to fill
    # the `ans` list with the k most frequent elements
    # O(n)
    ans = []
    # Start from the last bucket (greater frequency)
    i = n
    while k > 0:
        while k > 0 and buckets[i]:
            # Note: reverse order of nums with equal frequency
            # when compared with previous algorithms
            ans.append(buckets[i].pop())
            k -= 1
        i -= 1
    return ans


if __name__ == "__main__":
    print("-" * 60)
    print("Top K frequent elements")
    print("-" * 60)

    test_cases = [
        ([1, 1], 1, [1]),
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([3, 4, 3, 3], 2, [3, 4]),
        ([2, 1, 2, 2, 3, 3], 2, [2, 3]),
        (
            [
                1,
                1,
                1,
                3,
                3,
                3,
                3,
                2,
                2,
                6,
                7,
                8,
            ],
            3,
            [3, 1, 2],
        ),
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

        result = heap2(nums, k)
        output = f"\t        heap2 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bucket_sort(nums, k)
        output = f"\t  bucket_sort = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
