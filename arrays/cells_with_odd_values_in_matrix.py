"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

There is an m x n matrix that is initialized to all 0's. 
There is also a 2D array indices where each 
indices[i] = [ri, ci] represents a 0-indexed location 
to perform some increment operations on the matrix.

For each location indices[i], do both of the following:
- Increment all the cells on row ri.
- Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued 
cells in the matrix after applying the increment to 
all locations in indices.

Example 1:
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes 
[[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 
6 odd numbers.

Example 2:
Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. 
There are no odd numbers in the final matrix.

Constraints:
1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n


Follow up: Could you solve this in O(n + m + indices.length) 
time with only O(n + m) extra space?
"""
from typing import List


def brute_force(m: int, n: int, indices: List[int]) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    mat = [[0] * n for _ in range(m)]

    for row, col in indices:
        for r in range(m):
            mat[r][col] += 1
        for c in range(n):
            mat[row][c] += 1

    return sum(v & 1 for row in mat for v in row)


def efficient(m: int, n: int, indices: List[int]) -> int:
    # Time complexity: O(m*n)
    # Space complexity: O(m+n)

    rows = [False] * m
    cols = [False] * n

    for r, c in indices:
        rows[r] = rows[r] ^ 1
        cols[c] = cols[c] ^ 1

    count = 0
    for r in rows:
        for c in cols:
            count += r ^ c

    return count


def efficient2(m: int, n: int, indices: List[int]) -> int:
    # Time complexity: O(m+n)
    # Space complexity: O(m+n)

    rows = [False] * m
    cols = [False] * n

    for r, c in indices:
        rows[r] = rows[r] ^ 1
        cols[c] = cols[c] ^ 1

    row_even = row_odd = col_even = col_odd = 0
    for r in rows:
        if r & 1:
            row_odd += 1
        else:
            row_even += 1

    for c in cols:
        if c & 1:
            col_odd += 1
        else:
            col_even += 1

    # All the combinations generating an odd number
    return row_even * col_odd + row_odd * col_even


if __name__ == "__main__":
    print("-" * 60)
    print("Cells with odd values in a matrix")
    print("-" * 60)

    length = 10
    test_cases = [
        # (m, n, indices, solution)
        (2, 3, [[0, 1], [1, 1]], 6),
        (2, 2, [[1, 1], [0, 0]], 0),
    ]

    for m, n, indices, solution in test_cases:

        print(f"Matrix size: {m} x {n}")
        print("Indices:", indices)

        result = brute_force(m, n, indices)
        output = f"      brute_force = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = efficient(m, n, indices)
        output = f"        efficient = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = efficient2(m, n, indices)
        output = f"       efficient2 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
