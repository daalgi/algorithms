"""
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate an n x n matrix filled 
with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20
"""
from typing import List


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def moving_boundaries(n: int) -> List[List[int]]:
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    def update_boundary(move_id: int, boundary: List[int]) -> tuple:
        # Update the boundary list upon the current `move_id`
        if move_id == 0:
            # r_start += 1
            boundary[0] += 1
        elif move_id == 1:
            # c_end -= 1
            boundary[3] -= 1
        elif move_id == 2:
            # r_end -= 1
            boundary[1] -= 1
        elif move_id == 3:
            # c_start += 1
            boundary[2] += 1
        return boundary

    def valid_boundary(boundary: List[int]):
        # A boundary list is valid as long as the row and col
        # start and end don't cross:
        return boundary[0] <= boundary[1] and boundary[2] <= boundary[3]

    def point_within_boundary(r: int, c: int, boundary: List[int]):
        # A point is within the boundary when both conditions are met:
        # r_start <= r <= r_end
        # c_start <= c <= c_end
        return boundary[0] <= r <= boundary[1] and boundary[2] <= c <= boundary[3]

    # Initialize the result matrix `mat`
    mat = [[0] * n for _ in range(n)]
    # Boundary list [r_start, r_end, c_start, c_end]
    boundary = [0, n - 1, 0, n - 1]
    # Current pointer moves: (row, col)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # Index of the current move
    move_id = 0
    # row, col of the current cell or pointer
    r, c = 0, 0
    dr, dc = moves[move_id]
    # Current number `i`
    i = 1
    # Loop while the boundary list is valid (start and end don't cross)
    while valid_boundary(boundary):

        while point_within_boundary(r, c, boundary):
            mat[r][c] = i
            i += 1
            r += dr
            c += dc
        # Undo the last row-col update
        r, c = r - dr, c - dc

        # Update `boundary` list and `move_id` for next iteration
        boundary = update_boundary(move_id, boundary)
        move_id = (move_id + 1) % 4
        dr, dc = moves[move_id]
        r, c = r + dr, c + dc

    # print_matrix(mat)
    return mat


if __name__ == "__main__":
    print("-" * 60)
    print("Spiral matrix II")
    print("-" * 60)

    test_cases = [
        (1, [[1]]),
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
    ]

    for n, solution in test_cases:

        print(f"Matrix size: {n} x {n}")

        result = moving_boundaries(n)
        output = f"\t moving_boundaries = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += "\n" + " " * 55
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
