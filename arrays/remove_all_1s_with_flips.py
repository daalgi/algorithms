"""
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

You are given an m x n binary matrix grid.

In one operation, you can choose any row or column 
and flip each value in that row or column 
(i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's 
from grid using any number of operations or 
false otherwise.

Example 1:
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column

Example 2:
Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1's from grid.

Example 3:
Input: grid = [[0]]
Output: true
Explanation: There are no 1's in grid.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is either 0 or 1.
"""
from typing import List


def row_patterns(grid: List[List[int]]) -> bool:
    # Time complexity: O(rows * cols)
    # Space complexity: O(cols)

    # Notes:
    # - It only makes sense to flip a row (or a col) no more than once.
    # - If all the rows are equal, we can flip the columns with 1s
    # to achieve a matrix full of 0s.
    # - If all the cols are equal, we can flip the rows with 1s
    # to achieve a matrix full of 0s.
    # - If one row is different, we can only achieve a 0s matrix
    # if that row has an inverse pattern respect the others, i.e.
    #   01101                01101                            00000
    #   10010 -> flip row -> 01101 -> flip columns with 1s -> 00000

    # In order to being able to achieve all 0s,
    # all the rows (or columns) must have the same
    # pattern or the inverse pattern, i.e.
    # pattern = 00010, inverse = 11101
    # pattern = 11010, inverse = 00101
    original_pattern = grid[0]
    inverted_pattern = [1 - v for v in grid[0]]
    rows = len(grid)
    for r in range(1, rows):
        if grid[r] != original_pattern and grid[r] != inverted_pattern:
            return False

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Remove all ones with row and column flips")
    print("-" * 60)

    test_cases = [
        ([[0]], True),
        ([[0, 1, 0], [1, 0, 1], [0, 1, 0]], True),
        ([[1, 1, 0], [0, 0, 0], [0, 0, 0]], False),
    ]

    for grid, solution in test_cases:

        print("Grid:", grid)

        result = row_patterns(grid)
        output = "    row_patterns = "
        print_result = str(result)
        if len(print_result) > 30:
            print_result = print_result[:25] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
