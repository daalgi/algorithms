"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/

You are given an m x n integer matrix points (0-indexed). 
Starting with 0 points, you want to maximize the number 
of points you can get from the matrix.

To gain points, you must pick one cell in each row. 
Picking the cell at coordinates (r, c) will add 
points[r][c] to your score.

However, you will lose points if you pick a cell too far 
from the cell that you picked in the previous row. 
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), 
picking cells at coordinates (r, c1) and (r + 1, c2) will 
subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:
x for x >= 0.
-x for x < 0.


Example 1:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, 
which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 
from your score.
Your final score is 11 - 2 = 9.

Example 2:
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, 
which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 
from your score.
Your final score is 12 - 1 = 11.

Constraints:
m == points.length
n == points[r].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
0 <= points[r][c] <= 10^5
"""
from typing import List
from copy import deepcopy


def print_matrix(mat: List[List[int]]):
    for row in mat:
        print(" " * 3 + "".join(f"{v:>4}" for v in row))


def brute_force(points: List[List[int]]) -> int:
    # Time complexity: O(r c²)
    # Space complexity: O(c)
    rows, cols = len(points), len(points[0])
    if rows == 1:
        return max(points[0])

    prev = points[0]
    for r in range(1, rows):
        curr = [0] * cols
        for c in range(cols):
            curr[c] = points[r][c] + max(prev[j] - abs(c - j) for j in range(cols))
        prev = curr
    return max(curr)


def dp_iter(points: List[List[int]]) -> int:
    # Time complexity: O(r * 6c + c) = O(rc)
    # Space complexity: O(c)

    def acc_max_from_left(arr: List[int]) -> List[int]:
        # Time complexity: O(c)
        res = [arr[0]]
        for c in range(1, cols):
            res.append(max(res[-1] - 1, arr[c]))
        return res

    def acc_max_from_right(arr: List[int]) -> List[int]:
        # Time complexity: O(2c)
        res = [0] * (cols - 1) + [arr[-1]]
        for c in range(cols - 2, -1, -1):
            res[c] = max(res[c + 1] - 1, arr[c])
        return res

    rows, cols = len(points), len(points[0])
    if rows == 1:
        return max(points[0])

    prev = points[0]
    for r in range(1, rows):
        # Build the auxiliary rows with the maximum starting
        # from left and right, O(3c)
        left, right = acc_max_from_left(prev), acc_max_from_right(prev)
        curr = [0] * cols  # O(c)
        # Loop over the cols to find the max, O(c)
        for c in range(cols):
            curr[c] = points[r][c] + max(left[c], right[c])
        prev = curr

    # O(c)
    return max(curr)


def dp_iter2(points: List[List[int]]) -> int:
    # Time complexity: O(r * 4c + c) = O(rc)
    # Space complexity: O(c)
    rows, cols = len(points), len(points[0])
    if rows == 1:
        return max(points[0])

    prev = points[0]
    for r in range(1, rows):

        # Max of previous row comming from the left
        left = [prev[0]]
        for c in range(1, cols):
            left.append(max(left[-1] - 1, prev[c]))

        # Max of previous row comming from the right
        right = [0] * (cols - 1) + [prev[-1]]
        for c in range(cols - 2, -1, -1):
            right[c] = max(right[c + 1] - 1, prev[c])

        # Max of current row
        curr = []
        for c in range(cols):
            curr.append(points[r][c] + max(left[c], right[c]))

        prev = curr

    return max(curr)


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum number of points with cost")
    print("-" * 60)

    test_cases = [
        # (points, solution)
        ([[1, 2, 3]], 3),
        ([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9),
        ([[1, 5], [2, 3], [4, 2]], 11),
        ([[1, 2, 3], [1, 5, 1], [3, 1, 1], [9, 8, 1], [9, 1, 0], [9, 1, 99]], 124),
        ([[99, 3, 1, 1, 1, 1, 1, 0], [2, 3, 1, 1, 1, 1, 1, 99]], 191),
    ]

    for points, solution in test_cases:

        print("Points:")
        print_matrix(points)

        result = brute_force(deepcopy(points))
        output = f"   brute_force = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter(deepcopy(points))
        output = f"       dp_iter = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_iter2(deepcopy(points))
        output = f"      dp_iter2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
