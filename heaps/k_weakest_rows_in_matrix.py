"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

You are given an m x n binary matrix mat of 1's (representing soldiers) 
and 0's (representing civilians). The soldiers are positioned in 
front of the civilians. That is, all the 1's will appear to the 
left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:
- The number of soldiers in row i is less than the number 
of soldiers in row j.
- Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered 
from weakest to strongest.

Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 
Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
from typing import List
import heapq


def heap(mat: List[int], k: int) -> List[int]:
    # Time complexity: O(m(n + logm) + klogm)
    # Space complexity: O(m)
    # where `m` is the number of rows

    rows, cols = len(mat), len(mat[0])
    heap = []
    # Loop over the rows of the matrix to evaluate the
    # strength of each row
    # O(m)
    for row in range(rows):
        strength, col = 0, 0
        # O(n)
        while col < cols and mat[row][col] == 1:
            strength += 1
            col += 1
        # Add a tuple (stregth, row) to the heap.
        # The heap will keep the elements sorted by
        # strength and row, respectively
        # O(logm)
        heapq.heappush(heap, (strength, row))

    # Pop the `k` weakest rows from the heap and store
    # the indices in the `weakest` list
    weakest = list()
    row = 0
    # O(k)
    while row < k and len(heap) > 0:
        # O(logm)
        curr = heapq.heappop(heap)
        weakest.append(curr[1])
        row += 1

    return weakest


def heap_bsearch(mat: List[int], k: int) -> List[int]:
    # Time complexity: O(m(logn + logm) + klogm)
    # Space complexity: O(m)
    # where `m` is the number of rows
    # Optimization: count the number of 1s per row using
    # binary search

    def count_ones(row: List[int], left: int, right: int) -> int:
        # Using Binary Search,
        # identify the index `k` of the first 0, so the
        # number of 1s = k
        while left < right:
            mid = (right + left) // 2
            if row[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return left

    rows, cols = len(mat), len(mat[0])
    heap = []
    # Loop over the rows of the matrix to evaluate the
    # strength of each row
    # O(m)
    for row in range(rows):
        # O(logn)
        strength = count_ones(mat[row], 0, cols)

        # Add a tuple (stregth, row) to the heap.
        # The heap will keep the elements sorted by
        # strength and row, respectively
        # O(logm)
        heapq.heappush(heap, (strength, row))

    # Pop the `k` weakest rows from the heap and store
    # the indices in the `weakest` list
    weakest = list()
    row = 0
    # O(k)
    while row < k and len(heap) > 0:
        # O(logm)
        curr = heapq.heappop(heap)
        weakest.append(curr[1])
        row += 1

    return weakest


if __name__ == "__main__":
    print("-" * 60)
    print("The K weakest rows in a matrix")
    print("-" * 60)

    matrices = (
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0]],
        [[1] * i + [0] * (8 - i) for i in range(8)],
        [[1] * (8 - i) + [0] * i for i in range(8)],
        [[1] * (86 - i) + [0] * i for i in range(86)],
    )

    test_cases = [
        # (matrix, k, solution)
        (matrices[0], 3, [2, 0, 3]),
        (matrices[1], 2, [0, 2]),
        (matrices[1], 1, [0]),
        (matrices[1], 3, [0, 2, 3]),
        (matrices[2], 3, [0, 3, 2]),
        (matrices[2], 5, [0, 3, 2, 4, 1]),
        (matrices[3], 8, [0, 1, 2, 3, 4, 5, 6, 7]),
        (matrices[4], 8, [7, 6, 5, 4, 3, 2, 1, 0]),
        (matrices[5], 3, [85, 84, 83]),
    ]

    for nums, k, solution in test_cases:

        output = f"Matrix: {nums}"
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

        result = heap_bsearch(nums, k)
        output = f"\t heap_bsearch = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
