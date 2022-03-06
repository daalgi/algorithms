"""
https://leetcode.com/problems/intervals-between-identical-elements/

You are given a 0-indexed array of n integers arr.

The interval between two elements in arr is defined 
as the absolute difference between their indices. 
More formally, the interval between arr[i] and 
arr[j] is |i - j|.

Return an array intervals of length n where 
intervals[i] is the sum of intervals between 
arr[i] and each element in arr with the same 
value as arr[i].

Note: |x| is the absolute value of x.

Example 1:
Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. 
|0 - 4| = 4
- Index 1: Another 1 is found at index 3. 
|1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. 
|2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. 
|3 - 1| = 2
- Index 4: Another 2 is found at index 0. 
|4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. 
|5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. 
|6 - 2| + |6 - 5| = 5

Example 2:
Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Two more 10s are found at indices 2 and 3. 
|0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its 
sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. 
|2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. 
|3 - 0| + |3 - 2| = 4

Constraints:
n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= 10^5
"""
from typing import List
from collections import defaultdict


def brute_force(arr: List[int]) -> List[int]:
    # Time complexity: O(n²)
    # Space complexity: O(n)

    n = len(arr)

    # Map { num: [index1, index2, ...] }
    indices = defaultdict(list)
    for i in range(n):
        indices[arr[i]].append(i)

    res = [0] * n
    for i in range(n):
        suma = 0
        for j in indices[arr[i]]:
            suma += abs(i - j)
        res[i] = suma

    return res


def prefix_sum(arr: List[int]) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    """
    Example:
    indices     0  1  2  3  4  5  6  7
    array       2  8  3  8  2  8  5  8
    indices = {
        8: [1, 3, 5, 7], ...
    }
    for num = 8 and index 7 (last index):
        res[7] = (7 - 1) + (7 - 3) + (7 - 5) + (7 - 7)
               = 7 * 4 - (1 + 3 + 5 + 7) = 12
               = 7 * (i + 1) - presum[i + 1]
    for num = 8 and index 5 (not last index):
        res[5] = (5 - 1) + (5 - 3) + (5 - 5) + (7 - 5)
               = 5 * 3 - (1 + 3 + 5) + 7 - 5 = 8
               = 5 * (i + 1) - presum[i + 1]
                 + (presum[-1] - presum[i])
                 - 5 * (m - i)
    """
    n = len(arr)

    # Map { num: [index1, index2, ...] }
    indices = defaultdict(list)
    for i in range(n):
        indices[arr[i]].append(i)

    res = [0] * n
    for num in indices:
        m = len(indices[num])

        # Prefix sum of the current `num` indices
        acc = [0] * (m + 1)
        for i in range(m):
            acc[i + 1] = acc[i] + indices[num][i]

        for i, v in enumerate(indices[num]):
            # `v` is the index `i` (out of `m` indices)
            #  of `num` in `arr`
            res[v] = (v * (i + 1) - acc[i + 1]) + ((acc[m] - acc[i]) - v * (m - i))

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Intervals between identical elements")
    print("-" * 60)

    test_cases = [
        # (arr, solution)
        ([2, 1, 3, 1, 2, 3, 3], [4, 2, 7, 2, 4, 4, 5]),
        ([10, 5, 10, 10], [5, 0, 3, 4]),
        ([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [45, 37, 31, 27, 25, 25, 27, 31, 37, 45]),
        ([2, 8, 3, 8, 2, 8, 5, 8], [4, 12, 0, 8, 4, 8, 0, 12]),
    ]

    for arr, solution in test_cases:

        print("Array:", arr)

        result = brute_force(arr)
        output = "   brute_force = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = prefix_sum(arr)
        output = "    prefix_sum = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
